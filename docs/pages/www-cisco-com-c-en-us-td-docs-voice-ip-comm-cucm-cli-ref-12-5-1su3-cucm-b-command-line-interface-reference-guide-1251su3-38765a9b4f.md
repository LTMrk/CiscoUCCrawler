---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-cli-ref-12-5-1su3-cucm-b-command-line-interface-reference-guide-1251su3-38765a9b4f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/cli_ref/12_5_1SU3/cucm_b_command-line-interface-reference-guide_1251su3/cucm_b_command-line-interface-reference-guide-1251Su2_chapter_0111.html
retrieved_at: 2026-08-16T23:59:20.352828+00:00
---

Command Line Interface Reference Guide for Cisco Unified Communications Solutions, Release 12.5(1)SU3

# Command Line Interface Reference Guide for Cisco Unified Communications Solutions, Release 12.5(1)SU3

Updated: October 3, 2023

Chapter: Show Commands

## Chapter: Show Commands

# Show Commands

## show account

This command lists current administrator accounts.

show account

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 4

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## show
                        	 accountlocking

This command
                              		  displays the current account locking settings.

show accountlocking

### Command Modes

Administrator (admin:)

### Requirements

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

### Example

```
admin:show accountlocking
Account Lockout is enabled
Unlock Time : 300 seconds
Retry Count : 3 attempts
```

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

## show cert default-ca-list

This command displays all the default CA certificates, which are bundled with Unified Communications Manager and IM and Presence
                              Service.

show cert default-ca-list

### Command Modes

Administrator (admin:)

### Requirements

Applies to: Unified Communications Manager and IM and Presence Service.

### Example

```
admin:show cert default-ca-list

Common Name                   Trust Stores               Purpose

"VeriSign Class 3             tomcat-trust               This certificate is used by UCM
Secure Server CA - G3"                                   to communicate with Cisco if
                                                         Call-Home feature is enabled.

"CAP-RTP-002"                 CallManager-trust,         This certificate was used to
                              CAPF-trust                 sign the MIC installed on Cisco
                                                         endpoint.Presence of this
                                                         certificate allows the end point
                                                         to communicate securely with UCM
                                                         using the MIC when associated
                                                         with a secure profile

"Cisco Manufacturing         CallManager-trust,          This certificate was used to
CA"                          CAPF-trust                  sign the MIC installed on Cisco
                                                         endpoint. Presence of this
                                                         certificate allows the end point
                                                         to communicate securely with UCM
                                                         using the MIC when associated
                                                         with a secure profile.

"CAP-RTP-001"                CallManager-trust,          This certificate was used to
                             CAPF-trust                  sign the MIC installed on Cisco
                                                         endpoint. Presence of this
                                                         certificate allows the end point
                                                         to communicate securely with UCM
                                                         using the MIC when associated
                                                         with a secure profile

"ACT2 SUDI CA"                CallManager-trust,         This certificate was used to
                              CAPF-trust                 sign the MIC installed on Cisco
                                                         endpoint. Presence of this
                                                         certificate allows the end point
                                                         to communicate securely with UCM
                                                         using the MIC when associated
                                                         with a secure profile.

"Cisco Manufacturing          CallManager-trust,         This certificate was used to
CA SHA2"                      CAPF-trust                 sign the MIC installed on Cisco
                                                         endpoint. Presence of this
                                                         certificate allows the end point
                                                         to communicate securely with UCM
                                                         using the MIC when associated
                                                         with a secure profile.

"Cisco Root CA 2048"          CallManager-trust,         This certificate was used to
                              CAPF-trust                 sign the MIC installed on Cisco
                                                         endpoint. Presence of this
                                                         certificate allows the end point
                                                         to communicate securely with UCM
                                                         using the MIC when associated
                                                         with a secure profile.

"Cisco Root CA M2"            CallManager-trust,         This certificate was used to
                              CAPF-trust                 sign the MIC installed on Cisco
                                                         endpoint. Presence of this
                                                         certificate allows the end point
                                                         to communicate securely with UCM
                                                         using the MIC when associated
                                                         with a secure profile.
```

## show cert list

This command displays certificate trust lists.

show cert list { own | trust }

## Syntax Description

Specifies owned certificates.

Specifies trusted certificates.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

### Example

```
admin:cert list own
```

## show cert list
                        	 type

This command displays the available selected type certificate files.

show cert list type { own | trust }

## Syntax Description

Specifies owned certificates.

Specifies trusted certificates.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## show cert own

This command displays certificate contents.

show cert own filename

## Syntax Description

Specifies owned certificates.

Represents the name of the certificate file.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## show cert trust

This command displays certificate contents.

show cert trust filename

## Syntax Description

Specifies trusted certificates.

Represents the name of the certificate file.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## show cli pagination

This command displays the status of automatic CLI automatic pagination.

show cli pagination

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

### Example

```
admin:show cli pagination
Automatic Pagination : Off.
```

## show cli session
                        	 timeout

This command
                              		  displays the CLI session timeout value, which is the amount of time, in
                              		  minutes, that can elapse before a CLI session times out and disconnects.

show cli session timeout

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection.

## show csr
                        	 list

This command
                              		  displays Certificate Sign Request contents and certificate trust lists.

show csr list { own | | trust }

## Syntax Description

Shows a list
                                       					 of owned Certificate Sign Requests.

Shows a list
                                       					 of trusted Certificate Sign Requests.

### Command Modes

Administrator (admin:)

### Usage Guidelines

The certificate name can be obtained by using the show cert list own command.

### Requirements

Command privilege level: 1

Allowed during
                              		  upgrade:

Applies to: Unified Communications Manager ,
                              		  IM and Presence service on Unified Communications Manager ,
                              		  Cisco Unity Connection

### Example

```
admin: show csr list own
```

```
tomcat/tomcat.csr
```

```
Vipr-QuetzalCoatl/Vipr-QuetzalCoatl.csr
```

```
.....
```

```
.....
```

```
.....
```

## show csr list
                        	 type

This command displays the selected own Certificate Sign Request files.

show csr list type own

## Syntax Description

Shows a list of owned Certificate Sign Requests.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager, IM and Presence service on Unified Communications Manager, Cisco Unity Connection

## show csr own

This command
                              		  displays Certificate Sign Request (CSR) contents and certificate trust lists.

show csr own name

## Syntax Description

The name of
                                       					 the CSR file.

### Command Modes

Administrator (admin:)

### Usage Guidelines

The certificate name can be obtained by using the show cert list own command.

### Requirements

Command privilege level: 1

Applies to: Unified Communications Manager ,
                              		  IM and Presence service on Unified Communications Manager ,
                              		  Cisco Unity Connection

### Example

```
admin:show csr own tomcat/tomcat.csr
```

```
[
```

```
[
```

```
-----BEGIN CERTIFICATE SIGN REQUEST-----
```

```
MIIDrDCCAxUCBENeUewwDQYJKoZIhvcNAQEEBQAwggEbMTQwMgYDVQQGEytVbmFibGUgdG8gZmlu
```

```
ZCBDb3VudHJ5IGluIHBsYXRmb3JtIGRhdGFiYXNlMTIwMAYDVQQIEylVbmFibGUgdG8gZmluZCBT
```

```
dGF0ZSBpbiBwbGF0Zm9ybSBkYXRhYmFzZTE1MDMGA1UEBxMsVW5hYmxlIHRvIGZpbmQgTG9jYXRp
```

```
b24gaW4gcGxhdGZvcm0gZGF0YWJhc2UxMDAuBgNVBAoTJ1VuYWJsZSB0byBmaW5kIE9yZyBpbiBw
```

```
bGF0Zm9ybSBkYXRhYmFzZTExMC8GA1UECxMoVW5hYmxlIHRvIGZpbmQgVW5pdCBpbiBwbGF0Zm9y
```

```
bSBkYXRhYmFzZTETMBEGA1UEAxMKYmxkci1jY20zNjAeFw0wNTEwMjUxNTQwMjhaFw0xMDEwMjQx
```

```
NTQwMjhaMIIBGzE0MDIGA1UEBhMrVW5hYmxlIHRvIGZpbmQgQ291bnRyeSBpbiBwbGF0Zm9ybSBk
```

```
YXRhYmFzZTEyMDAGA1UECBMpVW5hYmxlIHRvIGZpbmQgU3RhdGUgaW4gcGxhdGZvcm0gZGF0YWJh
```

```
c2UxNTAzBgNVBAcTLFVuYWJsZSB0byBmaW5kIExvY2F0aW9uIGluIHBsYXRmb3JtIGRhdGFiYXNl
```

```
MTAwLgYDVQQKEydVbmFibGUgdG8gZmluZCBPcmcgaW4gcGxhdGZvcm0gZGF0YWJhc2UxMTAvBgNV
```

```
BAsTKFVuYWJsZSB0byBmaW5kIFVuaXQgaW4gcGxhdGZvcm0gZGF0YWJhc2UxEzARBgNVBAMTCmJs
```

```
ZHItY2NtMzYwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMoZ4eLmk1Q3uEFwmb4iU5nrMbhm
```

```
J7bexSnC3PuDGncxT3Au4zpGgMaQRL+mk+dAt8gDZfFKz8uUkUoibcUhvqk4h3FoTEM+6qgFWVMk
```

```
gSNUU+1i9MST4m1aq5hCP87GljtPbnCXEsFXaKH+gxBq5eBvmmzmO1D/otXrsfsnmSt1AgMBAAEw
```

```
DQYJKoZIhvcNAQEEBQADgYEAKwhDyOoUDiZvlAOJVTNF3VuUqv4nSJlGafB6WFldnh+3yqBWwfGn
```

## show csr own
                        	 name

This command displays Certificate Sign Request (CSR) own certificate
                              		  files.

show csr own name name of certificate sign
                                 				  request

## Syntax Description

The name of the CSR file.

The name of the certificate sign request.

### Command Modes

Administrator (admin:)

### Usage Guidelines

The certificate name can be obtained by using the show cert list own command.

### Requirements

Command privilege level: 1

Applies to: Unified Communications Manager, IM and Presence service on Unified Communications Manager, Cisco Unity Connection

## show ctl

This command displays the contents of the Certificate Trust List (CTL) file on the server. It notifies you if the CTL is invalid.

show ctl

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show cuc cluster
                        	 status

This command shows
                              		  the status of the servers in the cluster.

show cuc cluster status

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Cisco
                              		  Unity Connection

## show cuc config
                        	 groups

This command
                              		  displays a list of the valid configuration group names.

show cuc config groups [ page ]

## Syntax Description

Causes the
                                       					 output to display one page at a time. Be aware that page is case sensitive.

### Command Modes

Administrator (admin:)

### Usage Guidelines

To see a list of the settings for a specified group, run the command show cuc config settings .

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Cisco
                              		  Unity Connection

### Example

```
admin: show cuc config groups

CiscoLicensing
ConfigurationAssistant
Conversations
Directory
Groupware
LogMgr
Messaging
				:
				:
Telephony
```

## show cuc config
                        	 settings

This command
                              		  displays the settings and values for a specified group of Connection
                              		  configuration settings.

show cuc config
                                 				  settings group_name page

## Syntax Description

Specifies
                                       					 the name of the configuration group whose settings you want to display. To see
                                       					 a list of valid group names, run the command show
                                          						cuc config groups . Be aware that group names are case sensitive.

Causes the
                                       					 output to display one page at a time. Be aware that page is case sensitive.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Cisco
                              		  Unity Connection

### Configuration
                              		  Settings for the Group SA

```
admin: show cuc config settings SA

SA Setting      					Value

----------      					-----	

SessionTimeout      	20
Use24HrClockFormat   0
```

## show cuc
                        	 dbconsistency

This command checks
                              		  the tables and indexes of a specified database for inconsistencies.

show cuc
                                 				  dbconsistency [database_name]

## Syntax Description

unitydirdb -Contains
                                                						  the directory and configuration data.

unitydyndb -Contains
                                                						  dynamic data that Connection uses internally.

unitymbxdb 1 to unitymbxdb5 -Contains the data about the current voice
                                                						  messages in the corresponding mailbox store, including pointers to the audio
                                                						  files that are stored in the file system. If only one mailbox store is
                                                						  configured, the name of the mailbox store database is always unitymbxdb1.

unityrptdb -Contains
                                                						  audit log data.

### Command Modes

Administrator (admin:)

### Usage Guidelines

After the command completes, the system saves detailed information in a log file and displays a summary of the results, including
                              the location of the log file. Use the file commands to display the contents of the file.

Caution

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Cisco
                              		  Unity Connection

### Example of a
                              		  Consistency Check of the unityrptdb Database

```
admin: show cuc dbconsistency unityrptdb

Checking consistency of unityrptdb tables. Please wait.

Consistency check of unityrptdb tables successful.

Validation of unityrptdb indexes successful.

Output is in file: cuc/cli/consistency_unityrptdb_070404-123636.txt
```

## show cuc dbcontents

This command exports the data from a specified database to a CSV file.

show cuc dbcontents [database_name]

## Syntax Description

unitydirdb -Contains the directory and configuration data.

unitydyndb -Contains dynamic data that Connection uses internally.

unitymbxdb1 to unitymbxdb5 -Contains the data about the current voice messages in the corresponding mailbox store, including pointers to the audio files
                                                that are stored in the file system. If only one mailbox store is configured, the name of the mailbox store database is always
                                                unitymbxdb1.

unityrptdb -Contains audit log data.

### Command Modes

Administrator (admin:)

### Usage Guidelines

After the command completes, the location of the CSV file displays. Use the file commands to display the contents of the file.

Caution

Saving the contents of a database to a CSV file affects system performance. Run this command only when little or no system
                                          activity is occurring.

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Cisco Unity Connection

### Example of Exporting the Data From the unitydirdb Database to a CSV File and Displays the Location of the File

```
admin: show cuc dbcontents unitydirdb

This operation may take a few minutes to complete. Please wait.

Output is in file: cuc/cli/contents_unitydirdb_070404-124027.csv
```

## show cuc
                        	 dbschema

This command exports
                              		  the SQL statements that are necessary to replicate the schema for a specified
                              		  database to a file.

show cuc dbschema [database_name]

## Syntax Description

unitydirdb -Contains
                                                						  the directory and configuration data.

unitydyndb -Contains
                                                						  dynamic data that Connection uses internally.

unitymbxdb1 to unitymbxdb5 -Contains the data about the current voice
                                                						  messages in the corresponding mailbox store, including pointers to the audio
                                                						  files that are stored in the file system. If only one mailbox store is
                                                						  configured, the name of the mailbox store database is always unitymbxdb1.

unityrptdb -Contains
                                                						  audit log data.

### Command Modes

Administrator (admin:)

### Usage Guidelines

After the command completes, the location of the file displays. Use the file commands to display the file.

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Cisco
                              		  Unity Connection

### Example of
                              		  Exporting the Schema of the unitydirdb Database to a File and Displays the
                              		  Location of the File

```
admin: show cuc dbschema unitydirdb

Output is in file: cuc/cli/schema_unitydirdb_061013-115815.sql
```

## show cuc dbserver
                        	 disk

This command
                              		  displays summary information about informix storage space for all Connection
                              		  databases on the current server.

show cuc dbserver disk [ page ] [ file ]

## Syntax Description

Causes the
                                       					 output to display one page at a time. Be aware that page is case sensitive.

Saves the
                                       					 output to a file. If you include this option, the summary includes the location
                                       					 of the file. Be aware that file is case sensitive.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Cisco
                              		  Unity Connection

## show cuc dbserver session

This command displays summary information about a specified informix database user session.

show cuc dbserver session session_id [ page ] [ file ]

## Syntax Description

Specifies the database user session for which you want to display summary information. To get a list of current sessions,
                                       use either the show cuc dbserver sessions list command or the show cuc dbserver user list command.

Causes the output to display  one page at a time. Be aware that page is case sensitive.

Saves the output to a file. If you include this option, the summary includes the location of the file. Be aware that file is case sensitive.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Cisco Unity Connection

## show cuc dbserver sessions all

This command displays summary information about all the current Informix database user sessions.

show cuc dbserver sessions all [ page ] [ file ]

## Syntax Description

Causes the output to display one page at a time. Be aware that page is case sensitive.

Saves the output to a file. If you include this option, the summary includes the location of the file. Be aware that file is case sensitive.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Cisco Unity Connection

## show cuc dbserver sessions list

This command displays a list of the current Informix database user sessions.

show cuc dbserver sessions list [ page ]

## Syntax Description

Causes the output to display one page at a time. Be aware that page is case sensitive.

### Command Modes

Administrator (admin:)

### Usage Guidelines

The names of internal database users generally correspond with the names of Connection components. Run this command before
                              you run the show cuc dbserver session command to obtain the required session id. Results are sorted by session id.

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Cisco Unity Connection

## show cuc dbserver user list

This command displays a list of the active Connection internal database users.

show cuc dbserver user list [ page ]

## Syntax Description

Causes the output to display one page at a time. Be aware that page is case sensitive.

### Command Modes

Administrator (admin:)

### Usage Guidelines

The names of internal database users generally correspond with the names of Connection components. Results get sorted first by database and then by user.

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Cisco Unity Connection

## show cuc dbserver user waiting

This command displays a list of the Connection internal users that are waiting for a resource.

show cuc dbserver user waiting [ page ]

## Syntax Description

Causes the output to display one page at a time. Be aware that page is case sensitive.

### Command Modes

Administrator (admin:)

### Usage Guidelines

The names of the internal database users generally correspond with the names of Connection components.

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Cisco Unity Connection

## show cuc dbtable contents

This command exports the contents of a specified Connection table to a CSV file.

show cuc dbtable contents { database_name | table_name }

## Syntax Description

unitydirdb —Contains the directory and configuration data.

unitydyndb —Contains dynamic data that Connection uses internally.

unitymbxdb1 to unitymbxdb5 —Contains the data about the current voice messages in the corresponding mailbox store, including pointers to the audio files
                                                that are stored in the file system. If only one mailbox store is configured, the name of the mailbox store database is always unitymbxdb1 .

unityrptdb —Contains audit log data.

For a list of the tables in a specified database, use the show cuc dbtable list command. Be aware that table names are case sensitive.

### Command Modes

Administrator (admin:)

### Usage Guidelines

After the command completes, the location of the CSV file displays. Use the file commands to display the contents of the file.

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Cisco Unity Connection

### Example

```
admin: show cuc dbtable contents unitydirdb tbl_cos

Output is in file: cuc/cli/contents_tbl_cos_1013-113910.csv
```

## show cuc dbtable
                        	 list

This command
                              		  displays a list of the tables in a specified database.

show cuc dbtable
                                 				  list database_name [ page ]

## Syntax Description

unitydirdb —Contains
                                                						  the directory and configuration data.

unitydyndb —Contains
                                                						  dynamic data that Connection uses internally.

unitymbxdb1 to unitymbxdb5 —Contains the data about the current voice
                                                						  messages in the corresponding mailbox store, including pointers to the audio
                                                						  files that are stored in the file system. If only one mailbox store is
                                                						  configured, the name of the mailbox store database is always unitymbxdb1 .

unityrptdb —Contains
                                                						  audit log data.

Causes the
                                       					 output to display one page at a time. Be aware that page is case sensitive.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Cisco
                              		  Unity Connection

### Example

```
admin: show cuc dbtable list unitydirdb

tbl_accountlogonpolicy
tbl_agency
tbl_agencyextensionrange
tbl_alias
tbl_alternatename
tbl_broadcastmessage
tbl_broadcastmessagerecipient
...
tbl_waveformat
```

## show cuc dbtable
                        	 schema

This command
                              		  displays a description for a specified table and a list of the columns in the
                              		  table.

show cuc dbtable schema { database_name | table_name } [ page ]

## Syntax Description

unitydirdb —Contains
                                                						  the directory and configuration data.

unitydyndb —Contains
                                                						  dynamic data that Connection uses internally.

unitymbxdb1 to unitymbxdb5 —Contains the data about the current voice
                                                						  messages in the corresponding mailbox store, including pointers to the audio
                                                						  files that are stored in the file system. If only one mailbox store is
                                                						  configured, the name of the mailbox store database is always unitymbxdb1 .

unityrptdb —Contains
                                                						  audit log data.

For a
                                                      						  list of the tables in a specified database, use the show cuc dbtable list command. Be aware that table
                                                      						  names are case sensitive.

Causes the
                                       					 output to display one page at a time. Be aware that page is case sensitive.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Cisco
                              		  Unity Connection

### Example of
                              		  Displaying the Schema for the Table tbl_user in the unitydirdb Database

```
admin: show cuc dbtable schema unitydirdb tbl_cos

A collection of service privileges for subscribers that control access to features and use 
of the system into classes. Class of Service objects determine which features a subscriber 
is licensed to use, the maximum length of their greetings and messages, what numbers they are 
allowed to dial, and what options are available to the subscriber among other things.

Columns:
displayname
movetodeletefolder
accessunifiedclient
...
accesslivereply
```

## show cuc dbview contents

This command saves the results from a specified SQL view in a CSV file.

show cuc dbview contents { database_name | view_name }

## Syntax Description

unitydirdb —Contains the directory and configuration data.

unitydyndb —Contains dynamic data that Connection uses internally.

unitymbxdb1 to unitymbxdb5 —Contains the data about the current voice messages in the corresponding mailbox store, including pointers to the audio files
                                                that are stored in the file system. If only one mailbox store is configured, the name of the mailbox store database is always unitymbxdb1 .

unityrptdb —Contains audit log data.

For a list of the views in a specified database, use the show cuc dbview list command. Be aware that view names are case sensitive.

### Command Modes

Administrator (admin:)

### Usage Guidelines

After the command completes, the location of the CSV file displays. Use the file commands to display the contents of the file.

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Cisco Unity Connection

### Example

```
admin: show cuc dbview contents unitydirdb vw_cos_061013-113910.csv
```

## show cuc dbview
                        	 list

This command
                              		  displays a list of the views in a specified database.

show cuc dbview list database_name [ page ]

## Syntax Description

unitydirdb —Contains
                                                						  the directory and configuration data.

unitydyndb —Contains
                                                						  dynamic data that Connection uses internally.

unitymbxdb1 to unitymbxdb5 —Contains the data about the current voice
                                                						  messages in the corresponding mailbox store, including pointers to the audio
                                                						  files that are stored in the file system. If only one mailbox store is
                                                						  configured, the name of the mailbox store database is always unitymbxdb1 .

unityrptdb —Contains
                                                						  audit log data.

Causes the
                                       					 output to display one page at a time. Be aware that page is case sensitive.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

### Example

```
admin: show cuc dbview list unitydirdb

vw_agency
vw_agencyextensionrange
vw_alias
vw_alternatename
vw_broadcastmessage
vw_broadcastmessagerecipient
vw_callaction
...
vw_waveformat
```

## show cuc dbview
                        	 schema

This command
                              		  displays the schema for a specified view.

show cuc dbview schema { database_name | view_name } [ page ]

## Syntax Description

unitydirdb —Contains
                                                						  the directory and configuration data.

unitydyndb —Contains
                                                						  dynamic data that Connection uses internally.

unitymbxdb1 to unitymbxdb5 —Contains the data about the current voice
                                                						  messages in the corresponding mailbox store, including pointers to the audio
                                                						  files that are stored in the file system. If only one mailbox store is
                                                						  configured, the name of the mailbox store database is always unitymbxdb1 .

unityrptdb —Contains
                                                						  audit log data.

Causes the
                                       					 output to display one page at a time. Be aware that page is case sensitive.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Cisco
                              		  Unity Connection

### Example

```
admin: show cuc dbview schema unitydirdb vw_cos

A simple view for tbl_Cos.

Columns:
objectid
accessfaxmail
accesstts
callholdavailable
callscreenavailable
canrecordname
...
requiresecuremessages
```

## show cuc jetty ssl
                           	 status

show cuc jetty ssl status

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Cisco
                              		  Unity Connection

### Example

```
admin: show cuc jetty ssl status

Command completed successfully.
SSL notification is DISABLED
```

## show cuc
                        	 locales

This command
                              		  displays a list of the locales currently installed.

show cuc locales

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Cisco
                              		  Unity Connection

### Example

```
admin: show cuc locales

Installed Locale Package			Locale

-------------------------			------

uc-locale-en_GB-6.0.0.0-0		en-GB

uc-locale-fr_CA-6.0.0.0-0		fr-CA
```

## show cuc speechview registration certificate size

This command displays the current certificate bit size used for Speech to Text service registration and Voicemail transcription
                              with Nuance server.

show cuc speechview registration certificate size

### Command Modes

Administrator (admin:)

### Usage Guidelines

To view the current certificate bit size, use the show cuc speechview registration certificate size (Cisco Unity Connection Only) command.

### Requirements

Command privilege level: 4

Allowed during upgrade: Yes

Applies to: Cisco Unity Connection only.

## show cuc sysagent
                        	 task list

This command
                              		  displays a list of the Sysagent tasks.

show cuc sysagent task list [ page ]

## Syntax Description

Causes the
                                       					 output to display one page at a time. Be aware that page is case sensitive.

### Command Modes

Administrator (admin:)

### Usage Guidelines

To run a sysagent task, use the run cuc sysagent task command. If the value of the Is Singleton column is Y for a specified
                              task, the task can only be run on the primary server in a multi-server cluster. If this server is standalone, then all tasks
                              run on this server.

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Cisco
                              		  Unity Connection

### Example

```
admin: show cuc sysagent task list

Task Name																												Is Singleton

------------------------------     		------------

Data.BroadcastMessagePurge																N

Umss.CleanDeletedMessagesTask													Y

Umss.CleanDirectoryStreamFilesTask								Y

Umss.CleanOrphanAttachmentFilesTask							Y

...	

Data.UpdateDatabaseStats																		N
```

## show cuc sysagent
                        	 task results

This command
                              		  displays the times at which the specified task started and completed, with the
                              		  most recent time listed first.

show cuc sysagent task
                                 				  results task_name [ page ]

## Syntax Description

For a
                                                      						  list of task names, run the show cuc sysagent task list command. Be aware that
                                                      						  task names are case sensitive.

Causes the
                                       					 output to display one page at a time. Be aware that page is case sensitive.

### Command Modes

Administrator (admin:)

### Usage Guidelines

To run a Sysagent task, use the run cuc sysagent task command.

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Cisco
                              		  Unity Connection

### Example

```
admin: show cuc sysagent task results Umss.CleanDeletedMessagesTask

Time Started													Time Completed

----------------------			--------------------

2006-10-25 17:31:45.689		2006-10-25 17:31:45.785

2006-10-25	17:16:45.702		2006-10-25	17:16:45.742

2006-10-25	17:01:45.690		2006-10-25 17:01:45.730
```

## show cuc
                        	 sysinfo

This command
                              		  displays a summary of hardware and software system information for the current
                              		  Connection server, including the version installed on the active and inactive
                              		  partitions; whether a cluster is configured; QOS settings; hardware
                              		  specifications; the amount of used and free disk space on the active, inactive,
                              		  and common partitions; licensing information; and so on.

show cuc sysinfo

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: No

Applies to: Cisco
                              		  Unity Connection

### Example

```
admin: show cuc sysinfo

Gather Data/Time : Wed Oct 21 09:45:29 PDT 2009

Connection Install Information:

		Host Name : connection1

		Version:

			Active Version : 8.0.0.98000-210

			Inactive Version : 8.0.0.98000-201

		High Availability (this server is) : Pri_Single_Server

			Publisher : connection1.cisco.com - 10.10.10.10

			Subscriber(s) : None

		QOS Settings :

			Call Signaling DSCP : CS3

			Media Signaling DSCP : EF

		Hardware : 

			HW Platform										: 7825I3

			Processors											: 1

			Type																	: Family: Core 2

			CPU Speed												: 2130

			Memory															: 2048

			Object Id												: 1.3.6.1.4.1.9.1.746

			OS Version											: UCOS 4.0.0.0-31

			...
```

## show cuc tech
                        	 dbschemaversion

This command
                              		  displays the schema version information for each database.

show cuc tech dbschemaversion [ page ]

## Syntax Description

Causes the
                                       					 output to display one page at a time. Be aware that page is case sensitive.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Cisco
                              		  Unity Connection

### Example

```
admin: show cuc tech dbschemaversion

unitydirdb

==========

Schema Version		Product Version		Date

--------------		---------------		-----------------

1.2.363									2.1														2007-02-13 19:10:50.0
```

## show cuc tech dbserver all

This command runs all the show cuc tech commands in sequence and saves the results in a text file.

show cuc tech dbserver all

### Command Modes

Administrator (admin:)

### Usage Guidelines

After the command completes, detailed information gets saved in a text file and the location of the text file displays. Use
                              the file commands to display the contents of the file.

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

### Example

```
admin: show cuc tech dbserver all

Output is in file: cuc/cli/dbserverall_061013-111801.txt
```

## show cuc tech
                        	 dbserver integrity

This command checks
                              		  the integrity of the Informix database server storage space structure.

show cuc tech dbserver integrity

### Command Modes

Administrator (admin:)

### Usage Guidelines

After the command completes, detailed information gets saved in a text file, and a summary of the results displays, including
                              the location of the file. Use the file commands to display the contents of the file.

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Cisco
                              		  Unity Connection

### Example

```
admin: show cuc tech dbserver integrity
Database system catalog tables were successfully validated.
Database disk extents were successfully validated.
Database reserved pages were successfully validated.
Output is in file: cuc/cli/integrity_061013-95853.txt
```

## show cuc tech
                        	 dbserver log diagnostic

This command checks
                              		  for the existence of Informix assertion-failure and shared-memory-dump logs.

show cuc tech dbserver log diagnostic

### Command Modes

Administrator (admin:)

### Usage Guidelines

If the logs exist, their location displays. Use the file commands to display the contents of the files.

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Cisco
                              		  Unity Connection only.

### Example

```
admin:show cuc tech dbserver log diagnostic
The following Informix logs are available for the UC database server:
core/af.3599c
core/af.36858
```

## show cuc tech
                        	 dbserver log message

This command
                              		  displays the end of the Informix message log.

show cuc tech dbserver log message [lines] [ page ]

## Syntax Description

Specifies
                                       					 the number of lines that display at the end of the Informix message log. If the
                                       					 lines parameter is not included, the last 20 lines of the log are displayed.

(Optional)
                                       					 Causes the output to display one page at a time. Be aware that page is case
                                       					 sensitive.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Cisco
                              		  Unity Connection only.

### Example

```
admin:show cuc tech dbserver log message
Message Log File: online.ciscounity.log
18:09:01 Fuzzy Checkpoint Completed: duration was 0 seconds, 6 buffers
not flushed.
18:09:01 Checkpoint loguniq 57, logpos 0x208418, timestamp: 0x33b807
18:09:01 Maximum server connections 159
18:14:01 Fuzzy Checkpoint Completed: duration was 0 seconds, 6 buffers
not flushed.
18:14:01 Checkpoint loguniq 57, logpos 0x20a57c, timestamp: 0x33b9fc
```

## show cuc tech dbserver status

This command saves a detailed status report of the database server instance to a file.

show cuc tech dbserver status

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade:  Yes

Applies to: Cisco Unity Connection only.

### Example

```
admin:show cuc tech dbserver status
Output is in file: cuc/cli/status_061013-95031.txt
```

## show cuc trace levels

This command displays a list of all the diagnostic traces and trace levels that are currently enabled.

show cuc trace levels [page]

## Syntax Description

(Optional) Causes the output to display one page at a time. Be aware that page is case sensitive.

### Command Modes

Administrator (admin:)

### Usage Guidelines

To enable or disable specified traces and trace levels, use the set cuc trace (Cisco Unity Connection only) command.

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Cisco Unity Connection only.

### Example

```
admin:show cuc trace levels
Trace Name Levels
------------------------- --------------
Arbiter -
AudioStore 0
AxlAccess -
BulkAdministrationTool 0
CCL 10,11
CDE 3,14
CDL 11,13,15,17
::
VirtualQueue -
```

## show cuc
                        	 version

This command
                              		  displays the Cisco Unity Connection version that is currently installed on the
                              		  active and inactive partitions.

show cuc version

### Command Modes

Administrator (admin:)

### Usage Guidelines

This command always displays the version in the active partition. If the active partition contains an upgrade, the command
                              also shows the version in the inactive partition. The current Engineering Special also displays.

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Cisco
                              		  Unity Connection only.

### Example

```
admin:show cuc version
Active version: 7.0.1.10000-323
Inactive version: 7.0.0.39700-277
```

## show date

This command
                              		  displays the date and time on the server.

show date

### Command Modes

Administrator (admin:)

### Example

```
admin: show date
Sat Jul 17 01:28:57 IST 2010
```

## show diskusage

This command
                              		  displays disk usage information about specific directories.

show diskusage activelog { activelog | common | inactivelog | install | tftp | tmp } filename filename { directory | sort }

## Syntax Description

Saves the
                                       					 output to a specified file. These files are stored in the platform/cli
                                       					 directory. To view saved files, use the file view activelog command.

Displays the
                                       					 directory sizes only.

Sorts the
                                       					 output on the basis of file size. File sizes display in 1024-byte blocks.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection

## show dscp all

This command displays the current DSCP traffic markings on all the ports. It displays the DSCP markings in decimal and hexidecimal.
                              If the value corresponds to a class then it displays the correct class. If the value does not correspond to a  class, then
                              it displays N/A.

show dscp all

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: No

Applies to: Unified Communications Manager and Cisco Unity Connection

## show dscp defaults

This command displays the default factory DSCP settings. These values take effect if the set dscp defaults command is executed.

show dscp defaults

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: No

Applies to: Unified Communications Manager and Cisco Unity Connection

## show dscp marking

This command displays the current DSCP traffic markings for a particular DSCP value.

show dscp marking value

## Syntax Description

DSCP value. You can enter the name of a well-known DSCP class, or a numeric value in decimal or hexadecimal format. Precede
                                       hexadecimal values with 0x or 0X.

### Command Modes

Administrator (admin:)

### Usage Guidelines

The valid class names as defined by DSCP are:

Class Selector: values CSO , CS1 , CS2 , CS3 , CS5 , CS6 CS7

The class selector (CS) values correspond to IP Precedence values and are fully compatible with IP Precedence.

Expedited Forwarding: value EF

EF PHB is ideally suited for applications such as VoIP that require low bandwidth, guaranteed bandwidth, low delay, and low
                                    jitter.

Best Effort: value BE

Also called default PHB, this value essentially specifies that a packet be marked with 0x00, which gets the traditional best-effort
                                    service from the network router.

Assured Forwarding: values AF11 , AF12 , AF13 , AF21 , AF22 , AF23 , AF41 , AF42 , AF43

There are four types of Assured Forwarding classes, each of which has three drop precedence values. These precedence values
                                    define the order in  which a packet is dropped (if needed) due to network congestion. For example, packets in AF13 class are
                                    dropped before packets in the AF12 class.

### Requirements

Command privilege level: 1

Allowed during upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection

## show dscp status

This command displays the current DSCP traffic markings.

show dscp status { enabled | disabled }

## Syntax Description

Filters the output to show only DSCP traffic markings that are enabled. If you do not specify a status, this filter is the
                                       default option.

Filters the output to show only DSCP traffic markings that are disabled.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection

## show environment
                        	 fans

This command shows the status of the fan sensors.

show environment fans

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show environment
                        	 power-supply

This command shows the status of the power supply for MCS-7845,
                              		  MCS-7835, MCS-7825H3/H4, and MCS-7816H3 servers—those with redundant power
                              		  supply or embedded health hardware.

show tlstrace

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show environment
                        	 temperatures

This command retrieves the status of the temperature sensors.

show environment temperatures

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show fileserver transferspeed

This command shows the reading and writing speed between the IM and Presence Service  node and the external file server. It
                              involves copying a large file onto the mounted directory and then copying it back onto the node. As a result, this command
                              may have a  performance impact on the node from which it is run.

show fileserver transferspeed

### Command Modes

Administrator (admin:)

### Requirements

Applies to: IM and Presence Service on Unified Communications Manager.

### Example

```
admin:show fileserver transferspeed 
 
WARNING: This command involves copying a large file to and from the mounted directory. It can impact the performance of the system.
 
Do you want to continue? (y/n):y
 
Creating a file to perform the test, please wait...

Copying the file onto the mounted file system. Please note the writing speed recorded below.
262144+0 records in
262144+0 records out
1073741824 bytes (1.1 GB) copied, 28.9302 s, 37.1 MB/s

Copying the file from the mounted file system. Please note the reading speed recorded below.
262144+0 records in
262144+0 records out
1073741824 bytes (1.1 GB) copied, 67.7504 s, 15.8 MB/s

Clean-up finised
admin:
```

## show haproxy client-auth

This command displays the client authentication configured on the specified port.

show haproxy client-auth portnum

Parameter

Description

Enter the port number to view the client authentication configured on the specified port.

The supported port numbers are 6971, 6972 and 9443.

### Command Modes

Administrator (admin:)

### Usage Guidelines

Administrator can execute the help show haproxy client-auth <portnum> command to view the help content.

### Requirements

Command privilege level: 0

Applies to: Unified Communications Manager

### Example

```
admin:show haproxy client-auth 9443 Client authentication on the port 9443 is currently set to optional

admin:show haproxy client-auth 9456 Enter valid values for the port. 
Suggested values are 6971, 6972 and 9443
Executed command unsuccessfully

admin:help show haproxy client-auth 9443 show haproxy client-auth help:
This command will display client-auth for the specified port.
Example: 
admin:show haproxy client-auth 6971
Client authentication on the port 6971 is currently set to required.
```

## show haproxy num-threads

This command displays the number of HAProxy threads.

show haproxy num-threads

### Command Modes

Administrator (admin:)

### Usage Guidelines

Administrator can execute the help show haproxy num-threads command to view the help content.

### Requirements

Command privilege level: 0

Applies to: Unified Communications Manager

### Example

```
admin:show haproxy num-threads
HAProxy process running 2 threads
admin:help show haproxy num-threads

show haproxy num-threads:
This command updates the number of threads started by HaProxy service.
Example:
admin:show haproxy num-threads
```

## show hardware

This command displays hardware-related information about the platform.

show hardware

### Command Modes

Administrator (admin:)

### Usage Guidelines

The following information is displayed:

Platform

Serial number

BIOS build level

BIOS manufacturer

Active processors

RAID controller status

Disk partition details

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection

## show ipsec
                        	 information

This command
                              		  displays detailed information about the specified ipsec policy.

show ipsec information { policy_group | policy_name }

## Syntax Description

### Command Modes

Administrator (admin:)

### Usage Guidelines

### Requirements

Command privilege level: 1

Allowed during upgrade: yes

Applies to: Unified Communications Manager and IM and Presence Service on Unified Communications Manager

### Example

```
admin:show ipsec information test test1
PolicyGroup             : test
PolicyName              : test1
Type                    : transport
Source Address          : 10.94.171.3
Source Type             : ip
Destination Address     : 10.94.1.2
Destination Type        : ip
Protocol                : tcp
Source Port             : Any
Destination Port        : Any
Remote Port             : Any
Authentication Method   : psk
Destination Certificate : null
PSK                     : cisco
Phase 1 Life Time       : 3600
Encryption Algorithm    : des
Hash Algorithm          : sha1
Phase 1 DH Value        : null
Phase 2 Life Time       : 3600
ESP                     : null_enc
AH                      : hmac_sha1
Phase 2 DH Value        : null
Peer Type               : null
Status                  : disabled
Source Certificate      : null
```

## show ipsec policy_group

This command displays all the ipsec policy group on the node.

show ipsec policy_group

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager and Cisco Unity Connection

## show ipsec policy_name

This command displays the list of ipsec policy names that exist in the specified policy group.

show ipsec policy_name policy_group

## Syntax Description

Specifies the policy group name.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager and Cisco Unity Connection

## show ipsec
                        	 status

show ipsec status

### Command Modes

Administrator (admin:)

### Usage Guidelines

### Requirements

Command privilege level:

Allowed during upgrade:

Applies to: Unified Communications Manager and IM and Presence Service on Unified Communications Manager

## show itl

This command displays the ITL file contents or prints an error message if the ITL file is invalid.

show itl

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection

## show logins

This command lists recent logins to the server

show login [number]

## Syntax Description

Specifies the number of the most recent logins to display. The default is 20.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager and Cisco Unity Connection

### show logins
                           	 successful

This command shows the previous successful logins.

show logins successful [ last
                                    					 n ]

## Syntax Description

(Optional) Represents the last number of logins. By default,
                                          					 the value of this variable is 20.

#### Command Modes

Administrator (admin:)

#### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

### show logins
                           	 unsuccessful

Use this command
                                 		  to list recent unsuccessful login attempts to the following web applications:

On Unified Communications Manager

Disaster
                                             					 Recovery System

Cisco
                                             					 Unified OS Administration

On IM and Presence
                                          				  Service

IM and
                                             					 Presence Disaster Recovery System

Unified IM and Presence OS Administration

show logins unsuccessful [number]

## Syntax Description

Specifies
                                          					 the number of most recent logins to display. The default is 20.

#### Command Modes

Administrator (admin)

#### Requirements

Command privilege
                                 		  level: 0

Allowed during
                                 		  upgrade: Yes

Applies to Unified Communications Manager and IM and Presence Service

## show key authz encryption

Run this command on any Unified Communications Manager node to view the OAuth signing key checksum that Unified Communications
                              Manager uses to authenticate Cisco Jabber clients.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 4

Allowed during upgrade: No

Applies to: Unified Communications Manager and the IM and Presence Service.

## show key authz signing

Run this command on any Unified Communications Manager node to view the OAuth signing key checksum that Unified Communications
                              Manager uses to authenticate Cisco Jabber clients.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 4

Allowed during upgrade: No

Applies to: Unified Communications Manager and the IM and Presence Service.

## show license
                        	 all

This command
                              		  displays license status, license usage, UDI, and the agent version.

show license all

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager and Cisco Unity Connection

## show license
                        	 status

This command
                              		  displays the smart licensing status.

show license status

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager and Cisco Unity Connection

## show license
                        	 summary

This command
                              		  displays the smart licensing status and the license usage details.

show license summary

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager and Cisco Unity Connection

## show license tech
                        	 support

This command
                              		  displays smart licensing status, product information, and product version.

show license tech support

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager and Cisco Unity Connection

## show license
                        	 trace

This command
                              		  traces the content of smart agent-related logs to the console.

show license trace

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager and Cisco Unity Connection

## show license
                        	 UDI

PID—Product Identifier

SN—Serial Number

UUID—Universal Unique Identifier

show license UDI

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager and Cisco Unity Connection

## show license
                        	 usage

This command
                              		  displays the entitlements that are currently in use.

show license usage

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager and Cisco Unity Connection

## show Login Grace
                        	 Timeout

This command shows the login Grace Timeout.

show Login Grace Timeout

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager, IM and Presence Service on Unified Communications Manager, Cisco Unity Connection

## show media
                        	 streams

This command
                              		  captures information on current media stream connections.

show media streams [options]

## Syntax Description

file fname : Limit
                                                						  (valid characters alphanumeric [a-Z, A-Z, 0-9, (-) ad , (_)]. Default:
                                                						  mediainfo

count # : Range
                                                						  1-1000; Default: 2

sleep # : Range
                                                						  1-300 seconds; Default 5

device {ALL | ANN | CFB | CRA | MOH | MTP} Default: device
                                                   							 ALL

info : Displays
                                                						  extra information

buffers : Displays
                                                						  buffer usage information.

Ignore any kernel messages that display on the console screen
                                                               								when show media streams
                                                                     									 trace is entered.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager and Cisco Unity Connection

### Example

```
admin: show media streams info buffers

Resulting file /platform/log/mediainfo.txt contains:

Time: 2008.03.04 11:01:42
I/F Ver=5, #Apps: Free=		7, Alloc=		4, #Conf: Free= 		12, #Streams: Free=		40
Buffer Size =		652, Allocated Buffers=		1, Free Buffers =  5147
Buffer Size =	8192, Allocated Buffers=		0, Free Buffers = 	 450
App ID=		332, Cfg=CFB, Dead App Timer=86400, Active=Yes, Streams: Available=		92 Active=
4
Conf ID = 16777225, Type = Two No Sum, Streams: Tx =			2, Rx =			2, Active = Yes
Rx Stream: PktCnt= 5979, PID=16777653, PktSz=20ms, Payld=uLaw, IP=10.89.80.178:24652,
MCast=N, Mute=N, UsrMd=N, Actv=Y, QdPkts=2, PktOR=0, DtmfPL=0 DiscTimeSlice=	0 DiscPkts= 0
10:59:42
Buffer Size =		652, Used Buffers =			1
Buffer Size = 8192, Used Buffers =			0
Rx Stream: PktCnt=	6179, PID=16777651, PktSz=20ms, PayId=uLaw, IP=10.89.80.178:24650,
MCast=N, Mute=N, UsrMd=N, Actv=Y, QdPkts=0, PktOR=0, DtmfPL=0 DiscTimeSlice= 0 DiscPkts= 0
10:59:38
Buffer Size =		652, Used Buffers =			0
Buffer Size =	8192, Used Buffers =			0
Tx Stream: PktCnt= 5988, PID=16777653, PktSz=20ms, Payld=uLaw,
IP=10.13.5.189:29450 (24652), MCast=N, Mute=N, UsrMd=N, Actv=Y, DtmfPL=0, DtmfQ=0 10:59:42
Buffer Size =		652, Used Buffers =			0
Buffer Size =	8192, Used Buffers =			0
Tx Stream: PktCnt=	6193, PID=16777651, PktSz=20ms, Payld=uLaw,
IP=10.13.5.182:28516(24650), MCast=N, Mute=N, UsrMd=N, Actv=Y, DtmfPL=0, DtmfQ=0 10:59:42
Buffer Size =		652, Used Buffers =			0
Buffer Size =	8192, Used Buffers =			0
App ID=	331, Cfg=ANN, Dead App Timer=86400, Active=Yes, Streams: Available=		96 Active=
0
App ID=	330, Cfg=MOH, Dead App Timer=86400, Active=Yes, Streams: Available=	658 Active=
0
App ID= 329, Cfg=MTP, Dead App Timer=86400, Active=Yes, Streams: Available=		96 Active=
0
```

## show memory

This command
                              		  displays information about the onboard memory.

show memory { count | modules | size }

## Syntax Description

Displays the
                                       					 number of memory modules on the system.

Displays
                                       					 detailed information about all the memory modules.

Displays the
                                       					 total amount of physical memory.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection

## show myself

This command displays information about the current account.

show myself

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection

## show network all

This command shows network information for listening and nonlistening sockets.

show network all [ detail ] [ page ] [ search srchtext ]

## Syntax Description

Shows additional information.

Displays information one page at a time.

Searches for srchtext in the output.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show network cluster

This command  lists nodes in the network cluster and also shows the remaining timer value when you enable Dynamic Cluster
                              Configuration.

show network cluster

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show network dhcp eth0

This command shows DHCP status information.

show network dhcp eth0

### Command Modes

Administrator (admin:)

### Usage Guidelines

The eth0 parameter displays Ethernet port 0 settings, including DHCP configurations and options.

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show network eth0

This command shows network information for ethernet 0.

show network eth0 [ detail ] [ search srchtxt ]

## Syntax Description

Shows additional information.

Searches for srchtxt in the output.

### Command Modes

Administrator (admin:)

### Usage Guidelines

The eth0 parameter displays Ethernet port 0 settings

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show network failover

This command  shows Network Fault Tolerance information.

show network failover [ detail ] [ page ]

## Syntax Description

Shows additional information.

Shows information one page at a time.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show network ip_conntrack

This command shows ip_conntrack usage information.

show network ip_conntrack

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show network
                        	 ipprefs

This command shows
                              		  the list of ports that have been requested to be opened or translated in the
                              		  firewall.

show network ipprefs { all | enabled | public }

## Syntax Description

Shows all
                                       					 incoming ports that may be used on the product.

Shows all
                                       					 incoming ports that are currently opened.

Shows all
                                       					 incoming ports that are currently opened for a remote client.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

### Example

```
admin:show network ipprefs public
Application IPProtocol PortValue HashLimit (max:rate) H-Status ConnLimit C-Status Type XlatedPort Status  Description
----------- ---------  --------- -------------------- -------- --------- -------- ---- ---------- ------  ------------
sshd            tcp        22        1500:25/second    enabled     -     disabled public   -      enabled sftp and ssh
tomcat          tcp        443       4000:50/second    disabled   300     enabled public  8443    enabled  secure web
tomcat          tcp        80        4000:50/second    disabled   300     enabled public  8080
```

## show network ipv6

This command shows IPv6 network routes and network settings.

show network ipv6 { route | settings }

## Syntax Description

Shows all IPv6 routes.

Shows all IPv6 network settings.

### Command Modes

Administrator (admin:)

### Usage Guidelines

IPv6 is not supported in Cisco Business Edition 5000 .

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , Cisco Unity Connection

## show network max_ip_conntrack

This command shows max_ip_conntrack information.

show network max_ip_conntrack

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show network ntp
                        	 option

This command displays the security option that is configured in the /etc/config file.

show network ntp option

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show network route

This command shows network routing information.

show network route [ detail ] [ search srchtext ]

## Syntax Description

Shows additional information.

Searches for the srchtext in the output.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show network status

This command shows active internet connections.

show network status [ detail ] [ listen ] [ process ] [ all ] [ nodns ] [ search stext ]

## Syntax Description

Shows additional information.

Shows only listening sockets.

Shows the process ID and name of the program to which each socket belongs.

Shows both listening and nonlistening sockets.

Shows numerical addresses without any DNS information.

Searches for the stext in the output.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

### Example

```
admin: show network status
```

## show network
                        	 name-service attributes

This command
                              		  displays name service cache general attributes.

show network name - service attributes

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: No

Example:

```
admin:show network name-service hosts attributes
enable-cache                 yes   
positive-time-to-live        3600  
negative-time-to-live        20    

Successful
```

## show network
                        	 name-service cache-stats

This command
                              		  displays name service cache statistics.

show network name-services [ host ] [ services ] cache-stats

## Syntax Description

host
                                       					 services cache.

services
                                       					 service cache.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: No

Example:

```
admin:show network name-service hosts cache-stats
yes  cache is enabled
             no  cache is persistent
            yes  cache is shared
            211  suggested size
         216064  total data pool size
            272  used data pool size
           3600  seconds time to live for positive entries
             20  seconds time to live for negative entries
              0  cache hits on positive entries
              0  cache hits on negative entries
              2  cache misses on positive entries
              0  cache misses on negative entries
              0% cache hit rate
              2  current number of cached values
              2  maximum number of cached values
              0  maximum chain length searched
              0  number of delays on rdlock
              0  number of delays on wrlock
              0  memory allocations failed
            yes  check /etc/hosts for changes

Successful
```

## show network
                        	 name-service {hosts|services} attributes

This command displays name service cache attributes.

show network name - service {hosts|services} attributes

## Syntax Description

hosts services cache.

services service cache.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: No

Example:

```
admin:show network name-service hosts attributes 
enable-cache                 yes   
positive-time-to-live        3600  
negative-time-to-live        20    
suggested-size               211   
persistent                   no    
max-db-size                  33554432

Successful
```

## show open files
                        	 all

This command shows
                              		  all open files on the system.

show open files all

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show open files
                        	 process

The command shows
                              		  open files that belong to a specified process.

show open files process processID

## Syntax Description

Specifies a
                                       					 process.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show open files
                        	 regexp

This command shows
                              		  open files that match the specified regular expression.

show open files regexp reg_exp

## Syntax Description

Specifies a
                                       					 regular expression.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show open ports
                        	 all

This command shows
                              		  all open ports on the system.

show open ports all

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show open ports
                        	 regexp

This command shows
                              		  open ports that match the specified regular expression.

show open ports regexp reg_exp

## Syntax Description

Specifies a
                                       					 regular expression.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show packages

This command displays the name and version for installed packages.

show packages { active | inactive } name [ page ]

## Syntax Description

Specifies active packages.

Specifies inactive packages.

Specifies the package name. To display all active or inactive packages, use the wildcard character, *.

Shows the output one page at a time

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show password

This command shows information about the configured password.

show password { age | history | inactivity }

## Syntax Description

Shows information about the configured password age parameters

Shows the number of passwords that the history maintains for OS administration accounts.

Shows the status of the password inactivity for OS accounts. Password inactivity is the number of days of inactivity after
                                       a password has expired before the account is disabled.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

### show password
                           	 change-at-login

This command shows
                                 		  whether a user is forced to change passwords after the user signs in to the
                                 		  system the next time.

show password change-at-login userid

## Syntax Description

Specifies
                                          					 the user account that you want to show.

#### Command Modes

Administrator (admin:)

#### Requirements

Command privilege level: 0

Allowed during
                                 		  upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show password
                        	 complexity character

This command
                              		  displays the status of the password complexity rules—whether they are disabled
                              		  or enabled. If the password complexity rules are enabled, this command displays
                              		  the shows their current configuration.

show password complexity character

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show password
                        	 complexity length

This command displays the minimum length of passwords that need to be used for Cisco OS administrator accounts. The default
                              minimum length of a password is six characters.

show password complexity length

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show password expiry

This command shows the configured password expiration parameters.

show password expiry { maximum-age | minimum-age }

## Syntax Description

Shows the maximum number of days for set password expiry.

Shows the minimum number of days for set password expiry.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show password expiry user

This command shows  the configured password expiration parameters for the specified user.

show password expiry user { maximum-age | minimum-age } userid

## Syntax Description

Shows the maximum number of days for set password expiry.

Shows the minimum number of days for set password expiry.

Specifies the user account that you want to show.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show password expiry user list

This command  shows the password maximum age and password minimum age for each CLI user in the system.

show password expiry user

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show perf counterhelp

This command displays information about the specified perfmon counter.

show perf counterhelp class-name counter-name

## Syntax Description

Represents the class name that contains the counter.

### Command Modes

Administrator (admin:)

### Usage Guidelines

If the class name or counter name contains white spaces, enclose the name in double quotation marks.

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show perf list categories

This command lists the categories in the perfmon system.

show perf list categories

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show perf list classes

This command lists perfmon classes (objects).

show perf list classes [ cat category ] [ detail ]

## Syntax Description

Displays perfmon classes for the specified category.

Displays detailed information.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show perf list counters

This command lists perfmon counters for the specified perfmon class.

show perf list counters class-name [ detail ]

## Syntax Description

Represents the class name that contains the counter.

Displays detailed information.

### Command Modes

Administrator (admin:)

### Usage Guidelines

If the class name contains white spaces, enclose the name in double quotation marks.

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show perf list instances

This command lists the perfmon instances for the specified perfmon class.

show perf list instances class-name [ detail ]

## Syntax Description

Represents the class name that contains the counter.

Displays detailed information.

### Command Modes

Administrator (admin:)

### Usage Guidelines

If the class name contains white spaces, enclose the name in double quotation marks.

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show perf query class

This command queries a perfmon class and displays all the instances and counter values of each instance.

show perf query class class-name [ ,class-name... ]

## Syntax Description

Represents the class name that contains the counter.

### Command Modes

Administrator (admin:)

### Usage Guidelines

If the class name contains white spaces, enclose the name in double quotation marks.

You can specify a maximum of five classes for each command.

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show perf query counter

This command queries the specified counter or counters and displays the counter value of all instances.

show perf query counter class-name counter-name [ ,counter-name... ]

## Syntax Description

Represents the class name that contains the counter.

### Command Modes

Administrator (admin:)

### Usage Guidelines

If the class name or counter name contains white spaces, enclose the name in double quotation marks.

You can specify a maximum of five counters for each command.

The output that this command returns depends on the number of endpoints that is configured in the Route Groups in Unified
                                          Communications Manager.

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show perf query instance

This command queries the specified instance and displays all its counter values.

show perf query instance class-name instance-name [ ,instance-name... ]

## Syntax Description

Represents the class name that contains the counter.

### Command Modes

Administrator (admin:)

### Usage Guidelines

If the class name contains white spaces, enclose the name in double quotation marks.

You can specify a maximum of five instances for each command.

This command does not apply to singleton perfmon classes.

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show perf query path

This command queries a specified perfmon path.

show perf query path path-spec [ ,path-spec... ]

## Syntax Description

Specifies a perfmon path.

### Command Modes

Administrator (admin:)

### Usage Guidelines

For an instance-based perfmon class, you must specify path-spec as follows: class-name(instance-name)\counter-name

For a non instance-based perfmon class (a singleton), you must specify path-spec as follows: class-name\counter-name

You can specify a maximum of five paths for each command.

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

### Example

```
admin: show perf query path "Cisco Phones(phone-0)\CallsAttempted","Cisco Unified Communications Manager\T1ChannelsActive"
```

## show process
                        	 list

This command
                              		  displays a list of all the processes and critical information about each
                              		  process and visually indicates the child-parent relationships between the
                              		  processes.

show process list [ file filename ] [ detail ]

## Syntax Description

Outputs the
                                       					 results to the file that is specified by the filename variable.

Specifies
                                       					 the filename.

Displays
                                       					 detailed output.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show process
                        	 load

This command
                              		  displays the current load on the system.

show process load [ cont ] [ clear ] [ noidle ] [ num number ] [ thread ] [ cpu | | memory | | time ] [ page ]

## Syntax Description

Repeats the
                                       					 command continuously.

Clears the
                                       					 screen before displaying output.

Ignores the
                                       					 idle or zombie processes.

Displays the
                                       					 number of processes that are specified by number. The default number of
                                       					 processes equals 10. Set number to all
                                       					 to display all processes.

Displays
                                       					 threads.

Sorts output
                                       					 by CPU usage. This is the default sorting.

Sorts output
                                       					 by memory usage.

Sorts output
                                       					 by time usage.

Displays the
                                       					 output in pages.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show process
                        	 name

This command
                              		  displays the details of processes that share the same name and indicates their
                              		  parent-child relationship.

show process name process [ file filename ]

## Syntax Description

Specifies
                                       					 the name of a process.

Outputs the
                                       					 results to the file that is specified by filename .

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show process name
                        	 process-name

The command shows
                              		  the details of processes that share the same name. This commands displays
                              		  parent-child relationship.

show process name process name [ file vm detail cont ]

## Syntax Description

Specifies
                                       					 the name of a process.

(Optional)
                                       					 Shows the file name where the output is to be received.

(Optional)
                                       					 Shows the virtual memory of the process.

(Optional)
                                       					 Shows the details, such as page fault, virtual memory, and start time of the
                                       					 process.

(Optional)
                                       					 Repeats the command continuously.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show process
                        	 open

This command lists the open file descriptors for a comma separated
                              		  list of process IDs.

show process open file

## Syntax Description

(Optional) Shows the file name where the output is to be
                                       					 received.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show process
                        	 open-fd

This command lists
                              		  the open file descriptors for a comma-separated list of process IDs.

show process open-fd process-id [ ,process-id2 ]

## Syntax Description

Specifies
                                       					 the process-id.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show process
                        	 pid

This command shows a
                              		  specific process number or command name.

show process pid pid [ file filename ]

## Syntax Description

Specifies
                                       					 the process ID number of a process.

Outputs the
                                       					 results to the file that is specified by filename .

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show process
                        	 search

This command
                              		  searches for the pattern that the regular expression regexp specifies in the
                              		  output of the operating system-specific process listing.

show process search regexp [ file filename ]

## Syntax Description

Represents a
                                       					 regular expression.

Outputs the
                                       					 results to the file that is specified by filename .

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show process
                        	 user

This command
                              		  retrieves details of processes that share the user name and displays
                              		  parent-child relationship.

show process user username [ file detail detail detail cont ]

## Syntax Description

Specifies
                                       					 the username.

Outputs the
                                       					 results to the file that is specified by filename .

(Optional) Shows the virtual memory of the process.

(Optional) Shows the details, such as page fault, virtual
                                       					 memory, and start time of the process.

(Optional) Repeats the command continuously.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show process
                        	 using-most cpu

This command
                              		  displays a list of the most CPU-intensive processes.

show process using-most cpu [ number ] [ file filename | |  [ cont ]
                              						]

## Syntax Description

Specifies
                                       					 the number of processes to display. The default specifies 5.

Outputs the
                                       					 results to the file that is specified by filename .

Repeats the command continuosly.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show process
                        	 using-most memory

This command
                              		  displays a list of the most memory-intensive processes.

show process using-most memory [ number ] [ file filename | |  [ cont ]
                              						]

## Syntax Description

Specifies
                                       					 the number of processes to display. The default specifies 5.

Outputs the
                                       					 results to the file that is specified by filename .

Repeats the command continuously.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show
                        	 registry

This command
                              		  displays the contents of the registry.

show registry system component [ name ] [ page ]

## Syntax Description

Represents
                                       					 the registry system name.

Represents
                                       					 the registry component name.

Represents
                                       					 the name of the parameter to show.

Displays one
                                       					 page at a time.

### Command Modes

Administrator (admin:)

### Usage Guidelines

If the name is “page,” and you want to display the output one page at a time, use the command show registry system component name page page

To show all components in a system, enter the wildcard character * in the command: show registry system *

### Requirements

Command privilege
                              		  level: 1

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

### Example

```
admin:show registry cm dbl/sdi
system = cm
   component = dbl/sdi
      tracelevel=127
      enable=1
      outputdebugstringflag=0
      numminutes=1440
      tracefile=/var/log/active/cm/trace/dbl/sdi/dbl.log
      numfiles=250
      numlines=10000
```

## show risdb list

This command displays the tables that are supported in the Realtime Information Service (RIS) database.

show risdb list [ file filename ]

## Syntax Description

Outputs the information to a file.

### Command Modes

Administrator (admin:)

### Usage Guidelines

The file option saves the information to platform/cli/filename.txt . Ensure that the filename does not contain the "." character.

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

### Example

```
admin: show risdb list
```

## show risdb query

This command displays the contents of the specified RIS tables.

show risdb query table1 table2 table3 ... [ file filename ]

## Syntax Description

Specifies the name of a table.

Outputs the information to a file.

### Command Modes

Administrator (admin:)

### Usage Guidelines

The file option saves the information to platform/cli/filename.txt . Ensure that the filename does not contain the "." character.

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show samltrace level

This command displays the trace level that is currently configured.

show samltrace level

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection.

## show session
                        	 maxlimit

This command shows
                              		  the upper limit for concurrent SSH sessions.

show session maxlimit

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show smtp

This command displays the name of the SMTP host.

show smtp

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

### Example

```
admin:show smtp
SMTP hostname: mail.cisco.com
```

## show stats io

This command displays the IO statistics.

show stats io [ kilo ] [ detail ] [ page ] [ file filename ]

## Syntax Description

Displays statistics in kilobytes.

Displays detailed statistics on every available device on the system and overrides the kilo option.

Displays one page at a time.

Outputs the information to a file specified by filename

### Command Modes

Administrator (admin:)

### Usage Guidelines

The file option saves the information to platform/cli/filename.txt . Ensure that the filename does not contain the "." character.

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show status

This command displays basic platform status.

show status

### Command Modes

Administrator (admin:)

### Usage Guidelines

This command displays the following basic platform status:

- hostname

date

- timezone

- locale

- product version

- platform version

- CPU usage

- memory and disk usage

### Requirements

Command privilege level: 0

Allowed during upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show strace

This command lists the current service trace level.

show strace [ servicename ]

## Syntax Description

Represents the service for which the trace is set (enabled/disabled).

### Command Modes

Administrator (admin:)

### Usage Guidelines

If you do not enter any parameters, the command returns a list of available tasks.

### Requirements

Command privilege level: 0

Allowed during upgrade: No

Applies to: IM and Presence Service on Unified Communications Manager

### Example

```
admin: show strace Cisco XCP Router
```

```
Trace is enabled
```

```
Trace level is set to Info
```

## show tech
                        	 activesql

This command
                              		  displays the active queries to the database taken at one minute intervals as
                              		  far back as the logs allow.

show tech activesql

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech
                        	 all

This command
                              		  displays the combined output of all show tech commands.

show tech all [ page ] [ file filename ]

## Syntax Description

Displays one
                                       					 page at a time.

Outputs the
                                       					 information to a file.

### Command Modes

Administrator (admin:)

### Usage Guidelines

The file option saves the information to platform/cli/filename.txt . Ensure that the file name does not contain the "." character

### Requirements

Command privilege level: 1

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech
                        	 ccm_service

This command
                              		  displays information about all services that can run on the system.

show tech ccm_service

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech
                        	 database

This command shows
                              		  information about the database.

show tech database { dump | sessions }

## Syntax Description

Creates a
                                       					 CSV file of the entire database.

Redirects
                                       					 the session and SQL information of the present session IDs to a file.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech
                        	 dberrcode

This command
                              		  displays information (from the database log files) about the error code that is
                              		  specified.

show tech dberrcode errorcode

## Syntax Description

Specifies
                                       					 the error code as a positive integer.

### Command Modes

Administrator (admin:)

### Usage Guidelines

If the error code is a negative number, enter it without the minus sign (-).

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech
                        	 dbhighcputasks

This command displays the currently running high cost tasks and high
                              		  CPU-intensive tasks.

show tech dbhighcputasks

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech dbintegrity

This command displays the database integrity.

show tech dbintegrity

### Command Modes

Administrator (admin:)

### Requirements

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech
                        	 dbschema

This command
                              		  displays the database schema in a CSV file.

show tech dbschema [ car | cm ]

## Syntax Description

Represents
                                       					 the car database.

Represents
                                       					 the cm database.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech
                        	 dbinuse

This command
                              		  displays the database in use.

show tech dbinuse [ car | cm ]

## Syntax Description

Represents
                                       					 the car database.

Represents
                                       					 the cm database.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech
                        	 dbstateinfo

This command
                              		  displays the state of the database.

show tech dbstateinfo [ car | cm ]

## Syntax Description

Represents
                                       					 the car database.

Represents
                                       					 the cm database.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech
                        	 devdefaults

This command
                              		  displays the device defaults table.

show tech devdefaults

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech
                        	 dumpCSVandXML

This command
                              		  provides detailed information for customer support in the case of a standard
                              		  upgrade condition.

show tech dumpCSVandXML

### Command Modes

Administrator (admin:)

### Usage Guidelines

You can get this file in the following ways:

Use the file view activelog cm/trace/dbl/xmlcsv.tar command to view the contents of the file.

Use the file get activelog cm/trace/dbl/xmlcsv.tar command to download the file.

Use RTMT: Trace and Log Central > Collect Files > Cisco Database Cli Output > Install and upgrade log .

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech
                        	 gateway

This command
                              		  displays the gateway table from the database.

show tech gateway

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech
                        	 locales

This command
                              		  displays the locale information for devices, device pools, and end users.

show tech locales

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech network
                        	 all

This command
                              		  displays all network tech information.

show tech network all [ page ] [ search text ] [ file filename ]

## Syntax Description

Displays one
                                       					 page at a time.

Searches the
                                       					 output for the string that text specifies. Be aware that the search is case
                                       					 insensitive.

Outputs the
                                       					 information to a file.

### Command Modes

Administrator (admin:)

### Usage Guidelines

The file option saves the information to platform/cli/filename.txt . Ensure that the file name does not contain the "." character

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech network hosts

This command displays information about hosts configuration.

show tech network hosts [ page ] [ search text ] [ file filename ]

## Syntax Description

Displays one page at a time.

Searches the output for the string that text specifies. Be aware that the search is case insensitive.

Outputs the information to a file.

### Command Modes

Administrator (admin:)

### Usage Guidelines

The file option saves the information to platform/cli/filename.txt . Ensure that the file name does not contain the "." character

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech network
                        	 interfaces

This command
                              		  displays information about the network interfaces.

show tech network interfaces [ page ] [ search text ] [ file filename ]

## Syntax Description

Displays one
                                       					 page at a time.

Searches the
                                       					 output for the string that text specifies. Be aware that the search is case
                                       					 insensitive.

Outputs the
                                       					 information to a file.

### Command Modes

Administrator (admin:)

### Usage Guidelines

The file option saves the information to platform/cli/filename.txt . Ensure that the file name does not contain the "." character

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech network resolv

This command displays information about hostname resolution.

show tech network resolv [ page ] [ search text ] [ file filename ]

## Syntax Description

Displays one page at a time.

Searches the output for the string that text specifies. Be aware that the search is case insensitive.

Outputs the information to a file.

### Command Modes

Administrator (admin:)

### Usage Guidelines

The file option saves the information to platform/cli/filename.txt . Ensure that the file name does not contain the "." character

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech network routes

This command displays information about network routes.

show tech network routes [ page ] [ search text ] [ file filename ]

## Syntax Description

Displays one page at a time.

Searches the output for the string that text specifies. Be aware that the search is case insensitive.

Outputs the information to a file.

### Command Modes

Administrator (admin:)

### Usage Guidelines

The file option saves the information to platform/cli/filename.txt . Ensure that the file name does not contain the "." character

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech network sockets

This command displays the list of open sockets.

show tech network sockets { numeric }

## Syntax Description

Displays the numerical addresses of the ports instead of determining symbolic hosts. This parameter is equivalent to running
                                       the Linux shell numeric [ -n ] command.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech
                        	 notify

This command
                              		  displays the database change notify monitor.

show tech notify [search pattern_to_match]

## Syntax Description

Represents
                                       					 the string that needs to be searched in the command output.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech
                        	 params

This command
                              		  displays the database parameters.

show tech params { all | | enterprise | | service }

## Syntax Description

Displays all
                                       					 the database parameters.

Displays the
                                       					 database enterprise parameters.

Displays the
                                       					 database service parameters.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech
                        	 prefs

This command
                              		  displays database settings.

show tech prefs

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech
                        	 procedures

This command
                              		  displays the CAR or CM procedures that are in use for the database.

show tech procedures { car | | cm }

## Syntax Description

Specifies
                                       					 the CAR procedures.

Specifies
                                       					 the CM procedures.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech
                        	 repltimeout

This command
                              		  displays the replication timeout.

show tech repltimeout

### Command Modes

Administrator (admin:)

### Usage Guidelines

When you increase the replication timeout, ensure that as many servers as possible in a large system are included in the first
                              round of replication setup. If you have the maximum number of servers and devices, set the replication timeout to the maximum
                              value. Be aware that this delays the initial set up of replication to give all servers time to get ready for setup.

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech
                        	 routepatterns

This command
                              		  displays the route patterns that are configured for the system.

show tech routepatterns

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech
                        	 routeplan

This command
                              		  displays the route plans that are configured for the system.

show tech routeplan

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech
                        	 runtime

This command
                              		  displays CPU usage information at the time the command is run.

show tech runtime { all | cpu | disk | env | memory } page file filename

## Syntax Description

Displays all
                                       					 runtime information.

Displays CPU
                                       					 usage information at the time the command is run.

Displays
                                       					 system disk usage information.

Displays
                                       					 environment variables.

Displays
                                       					 memory usage information.

Displays one
                                       					 page at a time.

Outputs the
                                       					 information to a specified file.

This
                                                   						option saves the information to platform/cli/<filename>.txt. Ensure that
                                                   						the file name does not contain the "." character.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , and Cisco Unity Connection

## show tech
                        	 sqlhistory

This command prints
                              		  the history of SQL statements executed.

show tech sqlhistory

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech
                        	 systables

This command
                              		  displays the name of all tables in the sysmaster database.

show tech systables

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech
                        	 system

This command
                              		  displays all the system information.

show tech system { all | bus | hardware | host | kernel modules | software | tools } page file filename

## Syntax Description

Displays all
                                       					 the system information.

Displays
                                       					 information about the data buses on the server.

Displays
                                       					 information about the server hardware.

Displays
                                       					 information about the server.

Lists the
                                       					 installed kernel modules.

Displays
                                       					 information about the installed software versions.

Displays
                                       					 information about the software tools on the server.

Displays one
                                       					 page at a time.

Outputs the
                                       					 information to a file. This option saves the information to
                                       					 platform/cli/<filename>.txt. Ensure that the file name does not contain
                                       					 the "." character.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech
                        	 table

This command
                              		  displays the contents of the specified database table.

show tech table table_name [ page ]

## Syntax Description

Represents
                                       					 the name of the table to display.

Displays the
                                       					 output one page at a time.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech
                        	 triggers

This command
                              		  displays table names and the triggers that are associated with those tables.

show tech triggers

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tech
                        	 version

This command
                              		  displays the version of the installed components.

show tech version [ page ]

## Syntax Description

Displays one
                                       					 page at a time.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show timezone config

This command displays the current timezone settings.

show timezone config

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show timezone list

This command displays the available timezones.

show timezone list [ page ]

## Syntax Description

Displays the output one page at a time.

### Command Modes

Administrator (admin:)

### Usage Guidelines

Although the list of available time zones includes Factory , Unified Communications Manager does not support the Factory timezone.

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tls trace

This command shows the status of TLS trace for a service.

show tls trace [ service ]

## Syntax Description

Represents the TLS tracing status of a service. It is a
                                       					 mandatory parameter.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show tls min-version

This command shows the minimum configured version of Transport Layer Security (TLS) protocol.

show tls min-version

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager and IM and Presence Service on Unified Communications Manager

### Example

```
admin:show tls min-version
Configured TLS minimum version: 1.0
```

## show
                        	 tlsresumptiontimeout

This command shows the TLS session resumption timeout.

show tlsresumptiontimeout

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show trace

This command displays trace information for a particular task.

show trace [ task_name ]

## Syntax Description

Represents the name of the task for which you want to display the trace information.

### Command Modes

Administrator (admin:)

### Usage Guidelines

If you do not enter a parameter, the command returns a list of available tasks.

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

### Example

```
admin: show trace cdps
```

## show ups status

This command shows the current status of the USB-connected APC smart-UPS device and starts the monitoring service if this
                              service is not already started.

show ups status

### Command Modes

Administrator (admin:)

### Usage Guidelines

This command provides full status only for 7835-H2 and 7825-H2 servers.

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show version
                        	 active

This command
                              		  displays the software version on the active partition.

show version active

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show version
                        	 inactive

This command
                              		  displays the software version on the inactive partition

show version inactive

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show vos version

With Unity Connection 12.0(1) and later, Unity Connection supports a specific ISO that is separated from the Unified CM ISO.
                              However, Unity Connection will provide all the latest VOS changes. To see the VOS version integrated with Unity Connection show vos version CLI is introduced.

This command
                              		  displays the VOS version stored in the active and inactive partitions. If there
                              		  is no VOS version in the inactive partition, it displays " VOS version not
                                 			 available ".

For more
                              		  information, see "Support for Cisco Unity Connection ISO" section of the Release Notes
                                 			 for Cisco Unity Connection 12.0(1) available at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-release-notes-list.html

show vos version

### Command Modes

Administrator (admin:)

### Usage
                              		  Guidelines

This command
                              		  always displays the VOS version in the active partition. If the active
                              		  partition contains an upgrade, the command also shows the VOS version in the
                              		  inactive partition.

If you are
                                          			 upgrading from Cisco Unity Connection 11.5(1) or earlier version to 12.0(1) or
                                          			 later, the inactive partition does not contain the information of VOS version.

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Cisco
                              		  Unity Connection

### Example

```
admin:show vos version 
Active version: 12.0.1.10000-1 
Inactive version: VOS version not available
```

## show web-security

This command displays the contents of the current web-security certificate.

show web-security

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show webapp session timeout

This command displays the webapp session timeout value, which is the amount of time, in minutes, that can elapse before a
                              web application times out and logs off the user.

show webapp session timeout

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show workingdir

This command retrieves the current working directory for activelog, inactivelog, install, and TFTP.

show workingdir

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## show logins
                        	 unsuccessful

Use this command
                              		  to list recent unsuccessful login attempts to the following web applications:

On Unified Communications Manager

Disaster
                                          					 Recovery System

Cisco
                                          					 Unified OS Administration

On IM and Presence
                                       				  Service

IM and
                                          					 Presence Disaster Recovery System

Unified IM and Presence OS Administration

show logins unsuccessful [number]

## Syntax Description

Specifies
                                       					 the number of most recent logins to display. The default is 20.

### Command Modes

Administrator (admin)

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to Unified Communications Manager and IM and Presence Service

| Parameters | Description |
|---|---|
| own | Specifies owned certificates. |
| trust | Specifies trusted certificates. |

| Parameters | Description |
|---|---|
| own | Specifies owned certificates. |
| trust | Specifies trusted certificates. |

| Parameters | Description |
|---|---|
| own | Specifies owned certificates. |
| filename | Represents the name of the certificate file. |

| Parameters | Description |
|---|---|
| trust | Specifies trusted certificates. |
| filename | Represents the name of the certificate file. |

| Parameters | Description |
|---|---|
| own | Shows a list
                                       					 of owned Certificate Sign Requests. |
| trust | Shows a list
                                       					 of trusted Certificate Sign Requests. |

| Parameters | Description |
|---|---|
| own | Shows a list of owned Certificate Sign Requests. |

| Parameters | Description |
|---|---|
| name | The name of
                                       					 the CSR file. |

| Parameters | Description |
|---|---|
| name | The name of the CSR file. |
| name of certificate sign
                                          						request | The name of the certificate sign request. |

| Parameters | Description |
|---|---|
| page | Causes the
                                       					 output to display one page at a time. Be aware that page is case sensitive. |

| Parameters | Description |
|---|---|
| group_name | Specifies
                                       					 the name of the configuration group whose settings you want to display. To see
                                       					 a list of valid group names, run the command show
                                          						cuc config groups . Be aware that group names are case sensitive. |
| page page | Causes the
                                       					 output to display one page at a time. Be aware that page is case sensitive. |

| Parameters | Description |
|---|---|
| database_name | Specifies
                                       					 the name of the database that you want to check. Be aware that database names
                                       					 are case sensitive. Connection databases include: unitydirdb -Contains
                                                						  the directory and configuration data. unitydyndb -Contains
                                                						  dynamic data that Connection uses internally. unitymbxdb 1 to unitymbxdb5 -Contains the data about the current voice
                                                						  messages in the corresponding mailbox store, including pointers to the audio
                                                						  files that are stored in the file system. If only one mailbox store is
                                                						  configured, the name of the mailbox store database is always unitymbxdb1. unityrptdb -Contains
                                                						  audit log data. |

| Caution | Checking database consistency makes a significant impact on
                                          			 system performance. Run this command only when little or no system activity is
                                          			 occurring. After the operation begins, you can not cancel it. Do not restart
                                          			 the server during the operation; the operation must complete successfully
                                          			 before Connection will function properly. |
|---|---|

| Parameters | Description |
|---|---|
| database_name | Specifies the name of the database whose data you want to export to a CSV file. Be aware that database names are case sensitive.
                                       Connection databases include: unitydirdb -Contains the directory and configuration data. unitydyndb -Contains dynamic data that Connection uses internally. unitymbxdb1 to unitymbxdb5 -Contains the data about the current voice messages in the corresponding mailbox store, including pointers to the audio files
                                                that are stored in the file system. If only one mailbox store is configured, the name of the mailbox store database is always
                                                unitymbxdb1. unityrptdb -Contains audit log data. |

| Caution | Saving the contents of a database to a CSV file affects system performance. Run this command only when little or no system
                                          activity is occurring. |
|---|---|

| Parameters | Description |
|---|---|
| database_name | Speicifies
                                       					 the name of the database whose schema you want to export. Be aware that
                                       					 database names are case sensitive. Connection databases include: unitydirdb -Contains
                                                						  the directory and configuration data. unitydyndb -Contains
                                                						  dynamic data that Connection uses internally. unitymbxdb1 to unitymbxdb5 -Contains the data about the current voice
                                                						  messages in the corresponding mailbox store, including pointers to the audio
                                                						  files that are stored in the file system. If only one mailbox store is
                                                						  configured, the name of the mailbox store database is always unitymbxdb1. unityrptdb -Contains
                                                						  audit log data. |

| Parameters | Description |
|---|---|
| [ page ] | Causes the
                                       					 output to display one page at a time. Be aware that page is case sensitive. |
| [ file ] | Saves the
                                       					 output to a file. If you include this option, the summary includes the location
                                       					 of the file. Be aware that file is case sensitive. |

| Parameters | Description |
|---|---|
| session_id | Specifies the database user session for which you want to display summary information. To get a list of current sessions,
                                       use either the show cuc dbserver sessions list command or the show cuc dbserver user list command. |
| [ page ] | Causes the output to display  one page at a time. Be aware that page is case sensitive. |
| [ file ] | Saves the output to a file. If you include this option, the summary includes the location of the file. Be aware that file is case sensitive. |

| Parameters | Description |
|---|---|
| [ page ] | Causes the output to display one page at a time. Be aware that page is case sensitive. |
| [ file ] | Saves the output to a file. If you include this option, the summary includes the location of the file. Be aware that file is case sensitive. |

| Parameters | Description |
|---|---|
| [ page ] | Causes the output to display one page at a time. Be aware that page is case sensitive. |

| Parameters | Description |
|---|---|
| [ page ] | Causes the output to display one page at a time. Be aware that page is case sensitive. |

| Parameters | Description |
|---|---|
| [ page ] | Causes the output to display one page at a time. Be aware that page is case sensitive. |

| Parameters | Description |
|---|---|
| database_name | Specifies the database that contains the table whose contents you want to export to a CSV file. Be aware that database names
                                       are case sensitive. Connection databases include: unitydirdb —Contains the directory and configuration data. unitydyndb —Contains dynamic data that Connection uses internally. unitymbxdb1 to unitymbxdb5 —Contains the data about the current voice messages in the corresponding mailbox store, including pointers to the audio files
                                                that are stored in the file system. If only one mailbox store is configured, the name of the mailbox store database is always unitymbxdb1 . unityrptdb —Contains audit log data. |
| table_name | Specifies the table whose contents you want to export to a CSV file. Note For a list of the tables in a specified database, use the show cuc dbtable list command. Be aware that table names are case sensitive. | Note | For a list of the tables in a specified database, use the show cuc dbtable list command. Be aware that table names are case sensitive. |
| Note | For a list of the tables in a specified database, use the show cuc dbtable list command. Be aware that table names are case sensitive. |

| Note | For a list of the tables in a specified database, use the show cuc dbtable list command. Be aware that table names are case sensitive. |
|---|---|

| Parameters | Description |
|---|---|
| database_name | Specifies
                                       					 the database for which you want a list of tables. Be aware that database names
                                       					 are case sensitive. Connection databases include: unitydirdb —Contains
                                                						  the directory and configuration data. unitydyndb —Contains
                                                						  dynamic data that Connection uses internally. unitymbxdb1 to unitymbxdb5 —Contains the data about the current voice
                                                						  messages in the corresponding mailbox store, including pointers to the audio
                                                						  files that are stored in the file system. If only one mailbox store is
                                                						  configured, the name of the mailbox store database is always unitymbxdb1 . unityrptdb —Contains
                                                						  audit log data. |
| [ page ] | Causes the
                                       					 output to display one page at a time. Be aware that page is case sensitive. |

| Parameters | Description |
|---|---|
| database_name | Specifies
                                       					 the database that contains the table show schema you want to display. Be aware
                                       					 that database names are case sensitive. Connection databases include: unitydirdb —Contains
                                                						  the directory and configuration data. unitydyndb —Contains
                                                						  dynamic data that Connection uses internally. unitymbxdb1 to unitymbxdb5 —Contains the data about the current voice
                                                						  messages in the corresponding mailbox store, including pointers to the audio
                                                						  files that are stored in the file system. If only one mailbox store is
                                                						  configured, the name of the mailbox store database is always unitymbxdb1 . unityrptdb —Contains
                                                						  audit log data. |
| table_name | Specifies
                                       					 the table whose schema you want to display. Note For a
                                                      						  list of the tables in a specified database, use the show cuc dbtable list command. Be aware that table
                                                      						  names are case sensitive. | Note | For a
                                                      						  list of the tables in a specified database, use the show cuc dbtable list command. Be aware that table
                                                      						  names are case sensitive. |
| Note | For a
                                                      						  list of the tables in a specified database, use the show cuc dbtable list command. Be aware that table
                                                      						  names are case sensitive. |
| [ page ] | Causes the
                                       					 output to display one page at a time. Be aware that page is case sensitive. |

| Note | For a
                                                      						  list of the tables in a specified database, use the show cuc dbtable list command. Be aware that table
                                                      						  names are case sensitive. |
|---|---|

| Parameters | Description |
|---|---|
| database_name | Specifies the database that contains the view whose results you want to save to a file. Be aware that database names are case
                                       sensitive. Connection databases include: unitydirdb —Contains the directory and configuration data. unitydyndb —Contains dynamic data that Connection uses internally. unitymbxdb1 to unitymbxdb5 —Contains the data about the current voice messages in the corresponding mailbox store, including pointers to the audio files
                                                that are stored in the file system. If only one mailbox store is configured, the name of the mailbox store database is always unitymbxdb1 . unityrptdb —Contains audit log data. |
| view_name | Specifies the view whose results you want to save to a file. Note For a list of the views in a specified database, use the show cuc dbview list command. Be aware that view names are case sensitive. | Note | For a list of the views in a specified database, use the show cuc dbview list command. Be aware that view names are case sensitive. |
| Note | For a list of the views in a specified database, use the show cuc dbview list command. Be aware that view names are case sensitive. |

| Note | For a list of the views in a specified database, use the show cuc dbview list command. Be aware that view names are case sensitive. |
|---|---|

| Parameters | Description |
|---|---|
| database_name | Specifies
                                       					 the database for which you want a list of views. Be aware that database names
                                       					 are case sensitive. Connection databases include: unitydirdb —Contains
                                                						  the directory and configuration data. unitydyndb —Contains
                                                						  dynamic data that Connection uses internally. unitymbxdb1 to unitymbxdb5 —Contains the data about the current voice
                                                						  messages in the corresponding mailbox store, including pointers to the audio
                                                						  files that are stored in the file system. If only one mailbox store is
                                                						  configured, the name of the mailbox store database is always unitymbxdb1 . unityrptdb —Contains
                                                						  audit log data. |
| [ page ] | Causes the
                                       					 output to display one page at a time. Be aware that page is case sensitive. |

| Parameters | Description |
|---|---|
| database_name | Specifies
                                       					 the database that contains the view for which you want to display the schema.
                                       					 Be aware that database names are case sensitive. Connection databases include: unitydirdb —Contains
                                                						  the directory and configuration data. unitydyndb —Contains
                                                						  dynamic data that Connection uses internally. unitymbxdb1 to unitymbxdb5 —Contains the data about the current voice
                                                						  messages in the corresponding mailbox store, including pointers to the audio
                                                						  files that are stored in the file system. If only one mailbox store is
                                                						  configured, the name of the mailbox store database is always unitymbxdb1 . unityrptdb —Contains
                                                						  audit log data. |
| view_name | Specifies
                                       					 the view for which you want to display the schema. Note For a
                                                   						list of the views in a specified database, use the show cuc dbview list
                                                   						command. Be aware that view names are case sensitive. | Note | For a
                                                   						list of the views in a specified database, use the show cuc dbview list
                                                   						command. Be aware that view names are case sensitive. |
| Note | For a
                                                   						list of the views in a specified database, use the show cuc dbview list
                                                   						command. Be aware that view names are case sensitive. |
| [ page ] | Causes the
                                       					 output to display one page at a time. Be aware that page is case sensitive. |

| Note | For a
                                                   						list of the views in a specified database, use the show cuc dbview list
                                                   						command. Be aware that view names are case sensitive. |
|---|---|

| Parameters | Description |
|---|---|
| [ page ] | Causes the
                                       					 output to display one page at a time. Be aware that page is case sensitive. |

| Parameters | Description |
|---|---|
| task_name | Specifies
                                       					 the task for which you want to display information when the task starts and
                                       					 completes. Note For a
                                                      						  list of task names, run the show cuc sysagent task list command. Be aware that
                                                      						  task names are case sensitive. | Note | For a
                                                      						  list of task names, run the show cuc sysagent task list command. Be aware that
                                                      						  task names are case sensitive. |
| Note | For a
                                                      						  list of task names, run the show cuc sysagent task list command. Be aware that
                                                      						  task names are case sensitive. |
| [ page ] | Causes the
                                       					 output to display one page at a time. Be aware that page is case sensitive. |

| Note | For a
                                                      						  list of task names, run the show cuc sysagent task list command. Be aware that
                                                      						  task names are case sensitive. |
|---|---|

| Parameters | Description |
|---|---|
| [ page ] | Causes the
                                       					 output to display one page at a time. Be aware that page is case sensitive. |

| Parameters | Description |
|---|---|
| lines | Specifies
                                       					 the number of lines that display at the end of the Informix message log. If the
                                       					 lines parameter is not included, the last 20 lines of the log are displayed. |
| page | (Optional)
                                       					 Causes the output to display one page at a time. Be aware that page is case
                                       					 sensitive. |

| Parameters | Description |
|---|---|
| page | (Optional) Causes the output to display one page at a time. Be aware that page is case sensitive. |

| Parameters | Description |
|---|---|
| filename filename | Saves the
                                       					 output to a specified file. These files are stored in the platform/cli
                                       					 directory. To view saved files, use the file view activelog command. |
| directory | Displays the
                                       					 directory sizes only. |
| sort | Sorts the
                                       					 output on the basis of file size. File sizes display in 1024-byte blocks. |

| Parameters | Description |
|---|---|
| value | DSCP value. You can enter the name of a well-known DSCP class, or a numeric value in decimal or hexadecimal format. Precede
                                       hexadecimal values with 0x or 0X. |

| Parameters | Description |
|---|---|
| enabled | Filters the output to show only DSCP traffic markings that are enabled. If you do not specify a status, this filter is the
                                       default option. |
| disabled | Filters the output to show only DSCP traffic markings that are disabled. |

| Parameter | Description |
|---|---|
| portnum | Enter the port number to view the client authentication configured on the specified port. Note The supported port numbers are 6971, 6972 and 9443. | Note | The supported port numbers are 6971, 6972 and 9443. |
| Note | The supported port numbers are 6971, 6972 and 9443. |

| Note | The supported port numbers are 6971, 6972 and 9443. |
|---|---|

| Parameters | Description |
|---|---|
| policy_group |  |
| policy_name |  |

| Parameters | Description |
|---|---|
| policy_group | Specifies the policy group name. |

| Parameters | Description |
|---|---|
| number | Specifies the number of the most recent logins to display. The default is 20. |

| Parameters | Description |
|---|---|
| last n | (Optional) Represents the last number of logins. By default,
                                          					 the value of this variable is 20. |

| Parameters | Description |
|---|---|
| number | Specifies
                                          					 the number of most recent logins to display. The default is 20. |

| Parameters | Description |
|---|---|
| options | Enter one of
                                       					 the following options: file fname : Limit
                                                						  (valid characters alphanumeric [a-Z, A-Z, 0-9, (-) ad , (_)]. Default:
                                                						  mediainfo count # : Range
                                                						  1-1000; Default: 2 sleep # : Range
                                                						  1-300 seconds; Default 5 device {ALL \| ANN \| CFB \| CRA \| MOH \| MTP} Default: device
                                                   							 ALL info : Displays
                                                						  extra information buffers : Displays
                                                						  buffer usage information. trace : Activates
                                                						  extra trace from media driver to system log. Note Ignore any kernel messages that display on the console screen
                                                               								when show media streams
                                                                     									 trace is entered. | Note | Ignore any kernel messages that display on the console screen
                                                               								when show media streams
                                                                     									 trace is entered. |
| Note | Ignore any kernel messages that display on the console screen
                                                               								when show media streams
                                                                     									 trace is entered. |

| Note | Ignore any kernel messages that display on the console screen
                                                               								when show media streams
                                                                     									 trace is entered. |
|---|---|

| Parameters | Description |
|---|---|
| count | Displays the
                                       					 number of memory modules on the system. |
| modules | Displays
                                       					 detailed information about all the memory modules. |
| size | Displays the
                                       					 total amount of physical memory. |

| Parameters | Description |
|---|---|
| detail | Shows additional information. |
| page | Displays information one page at a time. |
| search srchtext | Searches for srchtext in the output. |

| Parameters | Description |
|---|---|
| detail | Shows additional information. |
| search srchtxt | Searches for srchtxt in the output. |

| Parameters | Description |
|---|---|
| detail | Shows additional information. |
| page | Shows information one page at a time. |

| Parameters | Description |
|---|---|
| all | Shows all
                                       					 incoming ports that may be used on the product. |
| enabled | Shows all
                                       					 incoming ports that are currently opened. |
| public | Shows all
                                       					 incoming ports that are currently opened for a remote client. |

| Parameters | Description |
|---|---|
| route | Shows all IPv6 routes. |
| settings | Shows all IPv6 network settings. |

| Note | IPv6 is not supported in Cisco Business Edition 5000 . |
|---|---|

| Parameters | Description |
|---|---|
| detail | Shows additional information. |
| search srchtext | Searches for the srchtext in the output. |

| Parameters | Description |
|---|---|
| detail | Shows additional information. |
| listen | Shows only listening sockets. |
| process | Shows the process ID and name of the program to which each socket belongs. |
| all | Shows both listening and nonlistening sockets. |
| nodns | Shows numerical addresses without any DNS information. |
| search stext | Searches for the stext in the output. |

| Parameters | Description |
|---|---|
| hosts | host
                                       					 services cache. |
| services | services
                                       					 service cache. |

| Parameters | Description |
|---|---|
| hosts | hosts services cache. |
| services | services service cache. |

| Parameters | Description |
|---|---|
| processID | Specifies a
                                       					 process. |

| Parameters | Description |
|---|---|
| reg_exp | Specifies a
                                       					 regular expression. |

| Parameters | Description |
|---|---|
| reg_exp | Specifies a
                                       					 regular expression. |

| Parameters | Description |
|---|---|
| active | Specifies active packages. |
| inactive | Specifies inactive packages. |
| name | Specifies the package name. To display all active or inactive packages, use the wildcard character, *. |
| page | Shows the output one page at a time |

| Parameters | Description |
|---|---|
| age | Shows information about the configured password age parameters |
| history | Shows the number of passwords that the history maintains for OS administration accounts. |
| inactivity | Shows the status of the password inactivity for OS accounts. Password inactivity is the number of days of inactivity after
                                       a password has expired before the account is disabled. |

| Parameters | Description |
|---|---|
| userid | Specifies
                                          					 the user account that you want to show. |

| Parameters | Description |
|---|---|
| maximum-age | Shows the maximum number of days for set password expiry. |
| minimum-age | Shows the minimum number of days for set password expiry. |

| Parameters | Description |
|---|---|
| maximum-age | Shows the maximum number of days for set password expiry. |
| minimum-age | Shows the minimum number of days for set password expiry. |
| userid | Specifies the user account that you want to show. |

| Parameters | Description |
|---|---|
| class-name | Represents the class name that contains the counter. |
| counter-name | Represents the counter that you want to view. |

| Parameters | Description |
|---|---|
| cat category | Displays perfmon classes for the specified category. |
| detail | Displays detailed information. |

| Parameters | Description |
|---|---|
| class-name | Represents the class name that contains the counter. |
| detail | Displays detailed information. |

| Parameters | Description |
|---|---|
| class-name | Represents the class name that contains the counter. |
| detail | Displays detailed information. |

| Parameters | Description |
|---|---|
| class-name | Represents the class name that contains the counter. |

| Parameters | Description |
|---|---|
| class-name | Represents the class name that contains the counter. |
| counter-name | Represents the counter that you want to view. |

| Note | The output that this command returns depends on the number of endpoints that is configured in the Route Groups in Unified
                                          Communications Manager. |
|---|---|

| Parameters | Description |
|---|---|
| class-name | Represents the class name that contains the counter. |
| instance-name | Specifies the perfmon instance to view. |

| Parameters | Description |
|---|---|
| path-spec | Specifies a perfmon path. |

| Parameters | Description |
|---|---|
| file | Outputs the
                                       					 results to the file that is specified by the filename variable. |
| filename | Specifies
                                       					 the filename. |
| detail | Displays
                                       					 detailed output. |

| Parameters | Description |
|---|---|
| cont | Repeats the
                                       					 command continuously. |
| clear | Clears the
                                       					 screen before displaying output. |
| noidle | Ignores the
                                       					 idle or zombie processes. |
| num number | Displays the
                                       					 number of processes that are specified by number. The default number of
                                       					 processes equals 10. Set number to all
                                       					 to display all processes. |
| thread | Displays
                                       					 threads. |
| cpu | Sorts output
                                       					 by CPU usage. This is the default sorting. |
| memory | Sorts output
                                       					 by memory usage. |
| time | Sorts output
                                       					 by time usage. |
| page | Displays the
                                       					 output in pages. |

| Parameters | Description |
|---|---|
| process | Specifies
                                       					 the name of a process. |
| file filename | Outputs the
                                       					 results to the file that is specified by filename . |

| Parameters | Description |
|---|---|
| process name | Specifies
                                       					 the name of a process. |
| file | (Optional)
                                       					 Shows the file name where the output is to be received. |
| vm | (Optional)
                                       					 Shows the virtual memory of the process. |
| detail | (Optional)
                                       					 Shows the details, such as page fault, virtual memory, and start time of the
                                       					 process. |
| cont | (Optional)
                                       					 Repeats the command continuously. |

| Parameters | Description |
|---|---|
| file | (Optional) Shows the file name where the output is to be
                                       					 received. |

| Parameters | Description |
|---|---|
| process-id | Specifies
                                       					 the process-id. |

| Parameters | Description |
|---|---|
| pid | Specifies
                                       					 the process ID number of a process. |
| file filename | Outputs the
                                       					 results to the file that is specified by filename . |

| Parameters | Description |
|---|---|
| regexp | Represents a
                                       					 regular expression. |
| file filename | Outputs the
                                       					 results to the file that is specified by filename . |

| Parameters | Description |
|---|---|
| username | Specifies
                                       					 the username. |
| file filename | Outputs the
                                       					 results to the file that is specified by filename . |
| vm | (Optional) Shows the virtual memory of the process. |
| detail | (Optional) Shows the details, such as page fault, virtual
                                       					 memory, and start time of the process. |
| cont | (Optional) Repeats the command continuously. |

| Parameters | Description |
|---|---|
| number | Specifies
                                       					 the number of processes to display. The default specifies 5. |
| file filename | Outputs the
                                       					 results to the file that is specified by filename . |
| cont | Repeats the command continuosly. |

| Parameters | Description |
|---|---|
| number | Specifies
                                       					 the number of processes to display. The default specifies 5. |
| file filename | Outputs the
                                       					 results to the file that is specified by filename . |
| cont | Repeats the command continuously. |

| Parameters | Description |
|---|---|
| system | Represents
                                       					 the registry system name. |
| component | Represents
                                       					 the registry component name. |
| name | Represents
                                       					 the name of the parameter to show. |
| page | Displays one
                                       					 page at a time. |

| Parameters | Description |
|---|---|
| file filename | Outputs the information to a file. |

| Parameters | Description |
|---|---|
| table1 | Specifies the name of a table. |
| file filename | Outputs the information to a file. |

| Parameters | Description |
|---|---|
| kilo | Displays statistics in kilobytes. |
| detail | Displays detailed statistics on every available device on the system and overrides the kilo option. |
| page | Displays one page at a time. |
| file filename | Outputs the information to a file specified by filename |

| Parameters | Description |
|---|---|
| servicename | Represents the service for which the trace is set (enabled/disabled). |

| Parameters | Description |
|---|---|
| page | Displays one
                                       					 page at a time. |
| file filename | Outputs the
                                       					 information to a file. |

| Parameters | Description |
|---|---|
| dump | Creates a
                                       					 CSV file of the entire database. |
| sessions | Redirects
                                       					 the session and SQL information of the present session IDs to a file. |

| Parameters | Description |
|---|---|
| errorcode | Specifies
                                       					 the error code as a positive integer. |

| Parameters | Description |
|---|---|
| car | Represents
                                       					 the car database. |
| cm | Represents
                                       					 the cm database. |

| Parameters | Description |
|---|---|
| car | Represents
                                       					 the car database. |
| cm | Represents
                                       					 the cm database. |

| Parameters | Description |
|---|---|
| car | Represents
                                       					 the car database. |
| cm | Represents
                                       					 the cm database. |

| Parameters | Description |
|---|---|
| page | Displays one
                                       					 page at a time. |
| search text | Searches the
                                       					 output for the string that text specifies. Be aware that the search is case
                                       					 insensitive. |
| file filename | Outputs the
                                       					 information to a file. |

| Parameters | Description |
|---|---|
| page | Displays one page at a time. |
| search text | Searches the output for the string that text specifies. Be aware that the search is case insensitive. |
| file filename | Outputs the information to a file. |

| Parameters | Description |
|---|---|
| page | Displays one
                                       					 page at a time. |
| search text | Searches the
                                       					 output for the string that text specifies. Be aware that the search is case
                                       					 insensitive. |
| file filename | Outputs the
                                       					 information to a file. |

| Parameters | Description |
|---|---|
| page | Displays one page at a time. |
| search text | Searches the output for the string that text specifies. Be aware that the search is case insensitive. |
| file filename | Outputs the information to a file. |

| Parameters | Description |
|---|---|
| page | Displays one page at a time. |
| search text | Searches the output for the string that text specifies. Be aware that the search is case insensitive. |
| file filename | Outputs the information to a file. |

| Parameters | Description |
|---|---|
| numeric | Displays the numerical addresses of the ports instead of determining symbolic hosts. This parameter is equivalent to running
                                       the Linux shell numeric [ -n ] command. |

| Parameters | Description |
|---|---|
| search pattern_to_match | Represents
                                       					 the string that needs to be searched in the command output. |

| Parameters | Description |
|---|---|
| all | Displays all
                                       					 the database parameters. |
| enterprise | Displays the
                                       					 database enterprise parameters. |
| service | Displays the
                                       					 database service parameters. |

| Parameters | Description |
|---|---|
| car | Specifies
                                       					 the CAR procedures. |
| cm | Specifies
                                       					 the CM procedures. |

| Parameters | Description |
|---|---|
| all | Displays all
                                       					 runtime information. |
| cpu | Displays CPU
                                       					 usage information at the time the command is run. |
| disk | Displays
                                       					 system disk usage information. |
| env | Displays
                                       					 environment variables. |
| memory | Displays
                                       					 memory usage information. |
| page | Displays one
                                       					 page at a time. |
| file filename | Outputs the
                                       					 information to a specified file. Note This
                                                   						option saves the information to platform/cli/<filename>.txt. Ensure that
                                                   						the file name does not contain the "." character. | Note | This
                                                   						option saves the information to platform/cli/<filename>.txt. Ensure that
                                                   						the file name does not contain the "." character. |
| Note | This
                                                   						option saves the information to platform/cli/<filename>.txt. Ensure that
                                                   						the file name does not contain the "." character. |

| Note | This
                                                   						option saves the information to platform/cli/<filename>.txt. Ensure that
                                                   						the file name does not contain the "." character. |
|---|---|

| Parameters | Description |
|---|---|
| all | Displays all
                                       					 the system information. |
| bus | Displays
                                       					 information about the data buses on the server. |
| hardware | Displays
                                       					 information about the server hardware. |
| host | Displays
                                       					 information about the server. |
| kernel modules | Lists the
                                       					 installed kernel modules. |
| software | Displays
                                       					 information about the installed software versions. |
| tools | Displays
                                       					 information about the software tools on the server. |
| page | Displays one
                                       					 page at a time. |
| file filename | Outputs the
                                       					 information to a file. This option saves the information to
                                       					 platform/cli/<filename>.txt. Ensure that the file name does not contain
                                       					 the "." character. |

| Parameters | Description |
|---|---|
| table_name | Represents
                                       					 the name of the table to display. |
| page | Displays the
                                       					 output one page at a time. |

| Parameters | Description |
|---|---|
| page | Displays one
                                       					 page at a time. |

| Parameters | Description |
|---|---|
| page | Displays the output one page at a time. |

| Parameters | Description |
|---|---|
| service | Represents the TLS tracing status of a service. It is a
                                       					 mandatory parameter. |

| Parameters | Description |
|---|---|
| task_name | Represents the name of the task for which you want to display the trace information. |

| Note | If you are
                                          			 upgrading from Cisco Unity Connection 11.5(1) or earlier version to 12.0(1) or
                                          			 later, the inactive partition does not contain the information of VOS version. |
|---|---|

| Parameters | Description |
|---|---|
| number | Specifies
                                       					 the number of most recent logins to display. The default is 20. |