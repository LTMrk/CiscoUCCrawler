---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-cli-ref-12-5-1-cucm-b-cli-reference-guide-1251-cucm-b-cli-reference-gui-c446911d42
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/cli_ref/12_5_1/cucm_b_cli-reference-guide-1251/cucm_b_cli-reference-guide-1251_chapter_0101.html
retrieved_at: 2026-08-16T23:54:52.307314+00:00
---

Command Line Interface Reference Guide for Cisco Unified Communications Solutions, Release 12.5(1)

# Command Line Interface Reference Guide for Cisco Unified Communications Solutions, Release 12.5(1)

Updated: August 26, 2025

Chapter: Run Commands

## Chapter: Run Commands

# Run Commands

## run cuc dbquery

This command runs an SQL query and displays the results.

run cuc dbquery database_name sql_query [ page ]

## Syntax Description

Specifies the database that sql_statement operates on.

Be aware that database names are case sensitive.

Connection databases include:

unitydirdb : Contains the directory and configuration data.

unitydyndb : Contains dynamic data that Connection uses internally.

unitymbxdb1 to unitymbxdb5 : Contains the data about the current voice messages in the corresponding mailbox store. This data includes pointers to the
                                       audio files that are stored in the file system. If only one mailbox store is configured, the name of the mailbox store database
                                       is always unitymbxdb1.

unityrptdb : Contains audit log data.

Specifies the SQL query that you want to run.

Shows the output one page at a time.

Be aware that page is case sensitive.

### Command Modes

Administrator (admin:)

### Usage Guidelines

You can also use the run cuc dbquery command with the csp_ConfigurationModify procedure, which configures the Wait for Blind Transfer Ringing timer. The command
                              usage for this timer is as follows:

run cuc dbquery unitydirdb execute procedure csp_ConfigurationModify (pFullName='System.Telephony.WaitForBlindTransferLongTimeoutMs',pvaluelong=" new value "

where, new value specifies the value of the
                              Wait for Blind Transfer Ringing Timer
                              parameter. The default and minimum value of this parameter is
                              500ms. The maximum value of this parameter can be 5000ms.

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Cisco Unity Connection

### Example

```
admin: run cuc dbquery unitydirdb select alias from vw_usertemplate

alias

---------------------

AdministratorTemplate

VoiceMailUserTemplate
```

## run cuc preupgrade test

This command verifies the state of the connection server on which the upgrade process is to be performed and specifies the
                              actions that can be taken before upgrading the system.

run cuc preupgrade test

### Command Modes

Administrator (admin:)

### Usage Guidelines

None

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Cisco Unity Connection only.

### Example

```
admin:run cuc preupgrade test
===========================================================================
DISCLAIMER ::
This cli command should be executed from publisher before upgrade to
check system health. This cli command is not intended to correct the
system state , rather it aims at informing the administrator what all
actions are advised to be taken before running upgrade.
===========================================================================
Checking connection db. Please wait...Done
Checking critical services. Please wait...Done
Checking cluster state. Please wait...Done
Checking cop file installation. Please wait...Done
Checking locales installation. Please wait...Done
Checking drs backup history. Please wait...Done
===========================================================================
R E P O R T    C A R D
===========================================================================
Locales Installation Test: PASS
Connection DB Test: PASS
DRS Backup History Test: FAIL
Cluster State Test: SKIPPED
Critical Services Test: PASS
Cop File Installation Test: SKIPPED
===========================================================================
A C T I O N   S U M M A R Y
===========================================================================
ACTION : Connection DB is online.
         NO constraints were found disabled in :unitydirdb,NO ACTION required before upgrade.
         NO indexes were found disabled in :unitydirdb,NO ACTION required before upgrade.
         NO constraints were found disabled in :unitydyndb,NO ACTION required before upgrade.
         NO indexes were found disabled in :unitydyndb,NO ACTION required before upgrade.
         NO constraints were found disabled in :unitymbxdb1,NO ACTION required before upgrade.
         NO indexes were found disabled in :unitymbxdb1,NO ACTION required before upgrade.
         NO constraints were found disabled in :unityrptdb,NO ACTION required before upgrade.
         NO indexes were found disabled in :unityrptdb,NO ACTION required before upgrade.
        Connection DB state is GOOD,NO ACTION required before upgrade.
ACTION : All Critical services are running ,NO ACTION required before upgrade.
ACTION : Standalone/Cores detected , excluding cluster state checking
ACTION : Skipping COP installation check, product version detected :'8.6.2.21018-1',NO ACTION required before upgrade.
ACTION : No locales were found installed ,NO ACTION required before upgrade.
ACTION : Make Sure DRS backup is taken aleast a day before upgrade.
Check report /var/log/active/cuc/cli/preupgrade_120325-224523.txt for details.
```

## run cuc
                        	 smtptest

This command
                              		  initiates a test that helps to verify the outgoing or incoming SMTP
                              		  configuration for SpeechView transcriptions.

run cuc smtptest email-address

## Syntax Description

Specifies
                                       					 the email address.

### Command Modes

Administrator (admin:)

### Usage Guidelines

The test sends a test message to a specified email address. You then access the email account and reply to the test message
                              without changing the subject line. The test passes after the Cisco Unity Connection server receives the response. The success or failure of parts of the test help to pinpoint problems in the outgoing or incoming
                              SMTP configuration for transcriptions.

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Cisco Unity
                                 			 Connection .

### Example

```
admin: run cuc sysagent task CleanDeletedMessagesTask
```

## run cuc sysagent
                        	 task

This command runs a
                              		  Sysagent task.

run cuc sysagent task task_name

## Syntax Description

Specifies
                                       					 the name of the Sysagent task that you want to run.

run cuc sysagent task task_name
                                    					 HTTP(S)LinkDisplayName

```
admin: run cuc sysagent task Data.LocalNetworkSync HTTP(S)LinkDisplayName1

Data.LocalNetworkSync started
```

Where
                              		  HTTP(S)LinkDisplayName is the display name of the HTTP(S) link with which you
                              		  want to synchronize the directory information.

### Command Modes

Administrator (admin:)

### Usage Guidelines

For a list of
                              		  Sysagent tasks, run the command show cuc sysagent
                                 			 task list (Cisco Unity Connection only). Be aware that sysagent task names
                              		  are case sensitive.

### Requirements

Command privilege
                              		  level: 1

Allowed during
                              		  upgrade: Yes

Applies to: Cisco Unity
                                 			 Connection

### Example

```
admin: run cuc sysagent task Umss.CleanDeletedMessagesTask

Umss.CleanDeletedMessagesTask started
```

## run cuc vui rebuild

This command instructs the voice recognition transport utility to immediately rebuild the voice recognition name grammars
                              with pending changes.

run cuc vui rebuild

### Command Modes

Administrator (admin:)

### Usage Guidelines

This command rebuilds only grammars that have changes flagged in the database. This command ignores name grammar update blackout
                              schedules and executes immediately. Due to the overhead of retrieving potentially large amounts of name-related data from
                              the database, you should use this command sparingly and only when absolutely necessary.

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Cisco Unity Connection

## run
                        	 loadcsv

This command is used on the publisher node to install the csv files
                              		  that are available on a server.

run loadcsv

### Command Modes

Administrator (admin:)

### Usage Guidelines

### Requirements

Command privilege level: 1

Allowed during upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## run loadxml

This command is a workaround for when service parameters or
                              product-specific information does not appear in the administration
                              window as expected.

run loadxml

### Command Modes

Administrator (admin:)

### Usage Guidelines

This command is processor intensive, and you may need to restart  some services after you run this command.

### Requirements

Command privilege level: 1

Allowed during upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## run sql

This command allows
                              		  you to run an SQL command.

run sql sql_statement

## Syntax Description

Specifies
                                       					 the SQL command to run.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: 0

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

Users with
                                          			 ordinary privileges can run read-only SQL commands.

### Example

```
admin: run sql select name from device
```

## run pe sql

This command allows
                              		  you to run an input SQL statement against the specified presence datastore.

run pe sql datastore_name sql_statement

## Syntax Description

Represents
                                       					 the name of the datastore.

Represents
                                       					 the SQL command to run.

### Command Modes

Administrator (admin:)

### Usage Guidelines

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: IM and Presence Service on Unified Communications Manager

Users with ordinary privileges can run read-only SQL commands.

### Example

```
admin: run pe sql ttsoft select * from presenceeventtable
```

| Parameters | Description |
|---|---|
| database_name | Specifies the database that sql_statement operates on. Note Be aware that database names are case sensitive. Connection databases include: unitydirdb : Contains the directory and configuration data. unitydyndb : Contains dynamic data that Connection uses internally. unitymbxdb1 to unitymbxdb5 : Contains the data about the current voice messages in the corresponding mailbox store. This data includes pointers to the
                                       audio files that are stored in the file system. If only one mailbox store is configured, the name of the mailbox store database
                                       is always unitymbxdb1. unityrptdb : Contains audit log data. | Note | Be aware that database names are case sensitive. |
| Note | Be aware that database names are case sensitive. |
| sql_query | Specifies the SQL query that you want to run. |
| page | Shows the output one page at a time. Note Be aware that page is case sensitive. | Note | Be aware that page is case sensitive. |
| Note | Be aware that page is case sensitive. |

| Note | Be aware that database names are case sensitive. |
|---|---|

| Note | Be aware that page is case sensitive. |
|---|---|

| Parameters | Description |
|---|---|
| email-address | Specifies
                                       					 the email address. |

| Parameters | Description |
|---|---|
| task_name | Specifies
                                       					 the name of the Sysagent task that you want to run. |

| Note | Before running
                                       		  the command, make sure that the scheduled task for directory or voice name
                                       		  synchronization is disabled for the specified HTTP(S) link
                                       		  "HTTP(S)LinkDisplayName" to avoid any issues in synchronization. |
|---|---|

| Note | This command is processor intensive, and you may need to restart  some services after you run this command. |
|---|---|

| Parameters | Description |
|---|---|
| sql_statement | Specifies
                                       					 the SQL command to run. |

| Note | Users with
                                          			 ordinary privileges can run read-only SQL commands. |
|---|---|

| Parameters | Description |
|---|---|
| datastore_name | Represents
                                       					 the name of the datastore. |
| sql_statement | Represents
                                       					 the SQL command to run. |

| Note | Users with ordinary privileges can run read-only SQL commands. |
|---|---|