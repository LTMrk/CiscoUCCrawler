---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-cli-ref-15-cucm-b-cli-reference-guide-release-15-cucm-b-cli-reference-g-ae9b98b2d2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/cli_ref/15/cucm_b_cli_reference_guide_release_15/cucm_b_cli_reference_guide_release_1401_chapter_011.html
retrieved_at: 2026-08-16T23:52:54.200862+00:00
---

Command Line Interface Reference Guide for Cisco Unified Communications Solutions, Release 15 and SUs

# Command Line Interface Reference Guide for Cisco Unified Communications Solutions, Release 15 and SUs

Updated: April 6, 2026

Chapter: File Commands

## Chapter: File Commands

# File Commands

## file build log

This command collects log information by service or feature and duration .

file build log service /feature duration

## Syntax Description

specifies the component or functional area from which to retrieve log information

specifies the time period, measured in days, from which the log information is retrieved.

### Command Modes

Administrator (admin:)

### Usage Guidelines

### Requirements

Command privilege level:

Allowed during upgrade:

Applies to: IM and Presence Service on Unified Communications Manager

### Examples

This command collects logs for the Client Profile Agent.

```
admin: file build log cpa 10 Collecting logs

Collecting: logname1.txt
Collecting: logname2.txt

To retrieve run the following command:
 file get epas/trace/acdc_2012-06-28-111258.tar.gz
```

This command collects all logs defined in the xml config.

```
admin:file build log all
Collecting logs

Collecting: logname1.txt
Collecting: logname2.txt

To retrieve run the following command:
 file get epas/trace/acdc_2012-06-28-111258.tar.gz
```

This command collects logs for multiple services.

```
admin:file build log dbmon cpa
Collecting logs

Collecting: logname1.txt
Collecting: logname2.txt

To retrieve run the following command:
 file get epas/trace/acdc_2012-06-28-111258.tar.gz
```

This command shows help.

```
admin:file build log ?
Syntax:
file build log [serviceName [serviceName] ..]

Service Names:
FullName                           ShortName

cisco_client_profile_agent         cpa
cisco_database_layer_monitor       dbmon
cisco_audit_logs                   audit
cisco_ris_dat_collector            risdc
```

This command shows information for the deployment.

```
admin: file build log deployment info 0

DB Queriesmay take up to 5 minutes to complete. Please be patient...
About to start queries for deployment data... please wait...
---------------------------------------------------
Gathering CUCM Version...
ccmversion
11.0.1.100000(9)
---------------------------------------------------
Gathering CUCM Publisher Node
ccmpublisherhostname
gwydlg050498vm1
---------------------------------------------------
Gathering Rosters table...
rosters
3032681
---------------------------------------------------
Gathering Groups table...
groups
1518966
---------------------------------------------------
Gathering Non-Presence contacts...
nonpresencecontacts
502573
---------------------------------------------------
Gathering Number of inter-cluster users...
enduser
0
---------------------------------------------------
Gathering CUCM Nodes in cluster...
processnode
2
---------------------------------------------------
Gathering CUCM Node names in cluster...
name
EnterpriseWideData
processnode
gwydlg050408vm1
---------------------------------------------------
Gathering IM&P nodes in cluster...
processnode
2
---------------------------------------------------
Gathering XCP Routing Node...
paramvalue
t
---------------------------------------------------
Gathering Exchange Calendaring...
pebackendgateway
---------------------------------------------------
Gathering SIP Inter-domain Federation...
domainname

paramvaluegwydlg050408vm2-public.cisco.com
---------------------------------------------------
Gathering XMPP Inter-domain Federation...
xmpps2ssnodes
0
---------------------------------------------------
Gathering Intra-domain Partitioned Federation...
enablepartitionedfedwithacs
f
---------------------------------------------------
Gathering Inter-cluster Peering...
cupsinterclusterpeers

---------------------------------------------------
Gathering Message Archiver...
pkid
8fede7a9-b6a6-4ad4-8da6-b8ea4c8d5411
databasetype
Postgres
databasename
tcmadb
name
gwydlg050408vm2
tknodeusage
0
tkprocessnoderole
2
nodeid
3
---------------------------------------------------
Gathering Third-party compliance...
ftextdbprocessnodemap
0
---------------------------------------------------
Gathering Persistent Chat...
enablepersistentgear
t
databasetype
Postgres
datanasename
tcmadb
name
gwydlg050408vm2
tknodeusage
0
tkprocessnoderole
2
nodeid
2
---------------------------------------------------
Gathering Advanced File Transfer...
tkfiletransfer
2
databasetype
Postgres
datbasename
tcmadb
name
gwydlg050408vm2
tknodeusage
0
tkprocessnoderole
2
nodeid
3
---------------------------------------------------
Gathering AD Groups...
paramvalue
t
---------------------------------------------------
Gathering XEP-198...
paramvalue
t
---------------------------------------------------
Gathering DB Replication Status...
replicationdynamic
2
Services on this node that currently have debug logging enabled are:

Cisco Presence Engine
Cisco DRF Local
Cisco XCP File Transfer Manager

Collecting Logs for deployment_info

Collected: platformConfig.xml
Collected: deployment_info.xml
Collected: system_info.txt

To retrieve the logs, run the following CLI Command:
	file get activelog epas/trace/log_2015-08-17-154010.tar.gz
To maintain a stable system it is recommended that you remove the file after retrieval.
	To do this run the CLI Command:
	file delete activelog epas/trace/log_2015-08-17-154010.tar.gz
Please Note: Debug logging is not enabled for any of the files you have retrieved
```

## file check

This command checks
                              		  the /usr directory tree to see whether files or directories have been added,
                              		  removed, or changed in size since the last fresh installation or upgrade and
                              		  shows the results.

file check [detection-size-kb]

## Syntax Description

Specifies
                                       					 the minimum file size change that is required for the command to display the
                                       					 file as changed.

Default
                                       					 value: 100 KB.

### Command Modes

Administrator (admin:)

### Usage Guidelines

The command notifies you about a possible impact to system performance and asks you whether you want to continue.  The display
                              includes both deleted and new files.

Caution

Because this command can affect system performance, we recommend that you run the command during off-peak hours.

### Requirements

Command privilege level: 1

Allowed during
                              		  upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## file delete

This command deletes
                              		  a log on the active or inactive side.

file delete { activelog | inactivelog } file-spec [ detail ] [ noconfirm ]

## Syntax Description

Specifies a
                                       					 log on the active side.

Specifies a
                                       					 log on the inactive side.

Specifies
                                       					 the path and filename of the log or logs to delete (includes install log
                                       					 files).

Shows a
                                       					 listing of deleted files with the date and time.

Deletes
                                       					 files without asking you to confirm each deletion.

### Command Modes

Administrator (admin:)

### Usage Guidelines

You get prompted for
                              		  confirmation after you enter the command. You cannot delete directories or
                              		  files that are in use.

Caution

You cannot
                                          			 recover a deleted file, but you may be able to with The Disaster Recovery
                                          			 System.

### Requirements

Command privilege
                              		  level: 1

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager, Cisco Unity Connection

## file delete tftp

This command deletes a TFTP file.

file delete tftp file-spec [ detail ] [ noconfirm ]

## Syntax Description

Represents the TFTP file name.

Shows a listing of deleted files with the date and time.

Deletes files without asking you to confirm each deletion.

### Command Modes

Administrator (admin:)

### Usage Guidelines

You get prompted for confirmation after you enter the command. You cannot delete directories or files that are in use.

Caution

You cannot recover a deleted file, but you may be able to with the Disaster Recovery System.

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

### file delete dir tftp

This command deletes the TFTP directory.

file delete dir tftp dir-name [ detail ]

## Syntax Description

Specifies the TFTP directory to delete.

Shows a listing of deleted files with the date and time.

#### Command Modes

Administrator (admin:)

#### Usage Guidelines

Caution

You cannot recover a deleted file, but you may be able to with the Disaster Recovery System.

#### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## file dump

This command dumps the contents of a log, a page at a time.

file dump { activelog | inactivelog | install } file-spec [ hex ] [ recent ] [ regexp expression ]

## Syntax Description

Specifies a log on the active side.

Specifies a log on the inactive side.

Specifies an installation log.

Represents the log file to dump.

Shows output in hexadecimal.

Dumps the most recently changed file in the directory.

Displays only the lines in the file that match the regular expression expression .

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

### Example

```
admin: file dump activelog cm/cdr/_cdrIndex.idx
```

## file dump
                        	 sftpdetails

This command
                              		  specifies the list of files that can be dumped in the SFTP context and allows
                              		  you to choose which file to dump.

file dump sftpdetails

### Command Modes

Administrator (admin:)

### Usage Guidelines

Enter a to dump all SFTP-related files. Enter q to exit this command.

### Requirements

Command privilege level: 1

Allowed during
                              		  upgrade: Yes

Applies to: Unified
                                 			 Communications Manager , Cisco Unity
                                 			 Connection

## file dump
                        	 tftp

This command dumps
                              		  the contents of a TFTP file to the screen, a page at a time.

file dump tftp file-spec [ page ] [ detail ] [ hex ]

## Syntax Description

Represents
                                       					 the name of a TFTP file.

Displays the
                                       					 output one screen at a time.

Displays
                                       					 the listing with the date and time.

Displays
                                       					 the output in hexadecimal.

### Command Modes

Administrator (admin:)

### Usage Guidelines

file-spec must resolve to a single file.

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , Cisco Unity Connection

## file fragmentation sdi

This command shows file fragmentation information about SDI log files.

file fragmentation sdi most { fragmented | recent } [number]

## Syntax Description

Represents the most fragmented log files.

Represents the most recent logs files.

Represents the number of files to list.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

### file fragmentation sdi file

This command shows file fragmentation information about an SDI log file.

file fragmentation sdi file filename [ verbose ]

## Syntax Description

Represents the SDI log file name.

Shows more detailed information on the screen.

#### Command Modes

Administrator (admin:)

#### Requirements

Command privilege level:1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

### file fragmentation sdi all

This command shows file fragmentation information about all SDI log files in the directory.

file fragmentation sdi all filename

## Syntax Description

Specifies the SDI log file name for which you want to show all fragmentation details.

#### Command Modes

Administrator (admin:)

#### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## file fragmentation sdl

This command shows file fragmentation information about the most fragmented SDL log files.

file fragmentation sdl most { fragmented | recent } [number]

## Syntax Description

Represents the most fragmented log files.

Represents the most recent log files.

Represents the number of files to list.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection .

### file fragmentation sdl file

This command displays file fragmentation information about an SDL log file.

file fragmentation sdl file filename [ verbose ]

## Syntax Description

Represents the file name of the SDL log file.

Shows more detailed information on the screen.

#### Command Modes

Administrator (admin:)

#### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection .

### file fragmentation sdl all

This command shows file fragmentation information about all SDL log files in the directory.

file fragmentation sdl all filename

## Syntax Description

Represents the file name for which you want to show all fragmentation details.

#### Command Modes

Administrator (admin:)

#### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection .

## file get

This command sends
                              		  a log to another system by using SFTP.

file get { activelog | inactivelog | install } file-spec [ reltime | abstime ] [ match regex ] [recurs] [compress]

## Syntax Description

Specifies a
                                       					 log on the active side.

Specifies a
                                       					 log on the inactive side.

Specifies an
                                       					 installation log.

Specifies
                                       					 the name of the file to transfer.

The relative
                                       					 time period, specified in minutes | hours | days | weeks | months | time value

The absolute
                                       					 time period, specified as hh:mm:MM/DD/YY hh:mm:MM/DD/YY

Match a
                                       					 particular string in the filename, specified as regex .

Get all
                                       					 files, including subdirectories.

Transfer
                                       					 files as compressed file.

### Command Modes

Administrator (admin:)

### Usage Guidelines

After the command identifies the specified files, you get prompted to enter an SFTP host, username, and password.

### Requirements

Command privilege
                              		  level: 0

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

### Example

```
admin: file get activelog platform match plat
```

```
admin: file get activelog platform/log abstime 18:00:10/20/13 18:00:10/21/13
```

### file get salog

This command sends the partBsalog or salog directory  to another system by using SFTP.

file get { partBsalog | salog } file-spec [ reltime | abstime ] [ match regex ] [recurs] [compress]

## Syntax Description

Specifies the partBsalog directory.

Specifies the salog directory.

Specifies the name of the file to transfer.

The relative time period, specified in minutes | hours | days | weeks | months | time value

The absolute time period, specified as hh:mm:MM/DD/YY hh:mm:MM/DD/YY

Match a particular string in the filename, specified as regex .

Get all files, including subdirectories.

Transfer files as compressed file.

#### Command Modes

Administrator (admin:)

#### Usage Guidelines

After the command identifies the specified files, you get prompted to enter an SFTP host, username, and password.

#### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , Cisco Unity Connection

## file get tftp

This command sends a TFTP file  to another system by using SFTP.

file get tftp file-spec [ reltime | abstime ] [ match regex ] [recurs] [compress]

## Syntax Description

Specifies the name of the TFTP file to transfer.

The relative time period, specified in minutes | hours | days | weeks | months | time value

The absolute time period, specified as hh:mm:MM/DD/YY hh:mm:MM/DD/YY

Match a particular string in the filename, specified as regex .

Get all files, including subdirectories.

Transfer files as compressed file.

### Command Modes

Administrator (admin:)

### Usage Guidelines

After the command identifies the specified files, you get prompted to enter an SFTP host, username, and password.

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , Cisco Unity Connection

## file list

This command lists
                              		  the log files in an available log directory.

file list { activelog | inactivelog | install } file-spec [ page | detail | reverse ] [ date | size ]

## Syntax Description

Specifies a
                                       					 log on the active side.

Specifies a
                                       					 log on the inactive side.

Specifies an
                                       					 installation log.

Specifies
                                       					 the name of the log file .

Shows the
                                       					 output one screen at a time.

Shows a
                                       					 detailed listing with date and time.

Reverses the
                                       					 sort direction.

Sorts files
                                       					 by date.

Sorts files
                                       					 by size.

### Command Modes

Administrator (admin:)

### Usage Guidelines

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

### Example: Log Files with Details

```
admin: file list activelog platform/log page detail
```

### Example: Directories in the CDR Repository

```
admin: file list activelog cm/cdr_repository
```

### Example: CDR Files by Size

```
admin: file list activelog cm/cdr_repository/processed/20050812 size
```

### file list
                           	 salog

This command lists
                                 		  the partBsalog or salog directory.

file list { partBsalog | salog } file-spec [ page | detail | reverse ] [ date | size ]

## Syntax Description

Specifies
                                          					 the partBsalog log directory.

Specifies
                                          					 the salog log directory.

Specifies
                                          					 the path to the file or files to list.

Shows the
                                          					 output one screen at a time.

Shows a
                                          					 detailed listing with date and time.

Reverses the
                                          					 sort direction.

Sorts files
                                          					 by date.

Sorts files
                                          					 by size.

#### Command Modes

Administrator (admin:)

#### Requirements

Command privilege level: 0

Allowed during
                                 		  upgrade: Yes

Applies to: Unified Communications Manager , Cisco Unity
                                    			 Connection

## file list tftp

This command lists TFTP files.

file list tftp file-spec [ page | detail | reverse ] [ date | size ]

## Syntax Description

Specifies the name of the TFTP file .

Shows the output one screen at a time.

Shows a detailed listing with date and time.

Reverses the sort direction.

Sorts files by date.

Sorts files by size.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , Cisco Unity Connection

## file search

This command searches the content of a log and shows the matching lines a page at a time.

file search { activelog | inactivelog | install } file-spec [ reltime | abstime ] [ignorecase]

## Syntax Description

Specifies a log on the active side.

Specifies a log on the inactive side.

Specifies an installation log.

Specifies the name of the file to search.

The relative time period, specified in minutes | hours | days | weeks | months | time value

The absolute time period, specified as hh:mm:MM/DD/YY hh:mm:MM/DD/YY

Ignores case in a search.

### Command Modes

Administrator (admin:)

### Usage Guidelines

Write the search term in the form of a regular expression, which
                              is a special text string to describe a search pattern.

If the search term is found in only one file, the filename
                              appears at the top of the output. If the search term is found in
                              multiple files, each line of the output begins with the filename in
                              which the matching line was found.

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

## file search tftp

This command searches the content of a TFTP file and shows the matching lines a page at a time.

file search tftp file-spec [ reltime | abstime ] [ignorecase]

## Syntax Description

Specifies the name of the TFTP file to search.

The relative time period, specified in minutes | hours | days | weeks | months | time value

The absolute time period, specified as hh:mm:MM/DD/YY hh:mm:MM/DD/YY

Ignores case in a search.

### Command Modes

Administrator (admin:)

### Usage Guidelines

Write the search term in the form of a regular expression, which
                              is a special text string to describe a search pattern.

If the search term is found in only one file, the filename
                              appears at the top of the output. If the search term is found in
                              multiple files, each line of the output begins with the filename in
                              which the matching line was found.

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

## file tail activelog

This command tails (prints the last few lines) of a log file.

file tail { activelog | inactivelog | install } filespec [ hex ] [lines] [ regexp expression ]

## Syntax Description

Specifies a log on the active side.

Specifies a log on the inactive side.

Specifies an installation log.

Specifies the path to the file. You can use the wildcard character, *, for filename as long as it resolves to one file.

Show the listing in hexadecimal.

Specifies the number of lines to display.

Tails log files that match expression

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

### Example

```
admin: file tail activelog platform/log/cli00001.log
```

## file tail tftp

This command tails (prints the last few lines) of a TFTP file.

file tail tftp filespec [ detail ] [ hex ] [lines]

## Syntax Description

Specifies the path to the file. You can use the wildcard character, *, for filename as long as it resolves to one file.

Long listing with date and time

Show the listing in hexadecimal.

Specifies the number of lines to display.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , Cisco Unity Connection

## file view

This command shows the contents of log files.

file view { activelog/ inactivelog/ install} } file-spec

## Syntax Description

Shows the contents of an active side logging files

Shows the contents of an inactive side logging files

Shows the contents of an install logging file

Specifies the path to the file to view. You can use the wildcard character, *, as long as it resolves to one file.

### Command Modes

Administrator (admin:)

### Usage Guidelines

Caution

Do not use this command to view binary files because this can corrupt the terminal session.

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

### Example

```
admin: file view activelog /cm/cdr_repository/processed/20058012/{filename}
```

### file view activelog

This command shows
                                 		  the contents of log files.

file view activelog file-spec

## Syntax Description

Shows the
                                          					 contents of an active side logging files

Specifies
                                          					 the path to the file to view. You can use the wildcard character, *, as long as
                                          					 it resolves to one file.

#### Command Modes

Administrator (admin:)

#### Usage Guidelines

Caution

Do not use this
                                             			 command to view binary files because this can corrupt the terminal session.

This command may use a considerable amount of I/O and running it may impact system performance. It is highly recommended that
                                             this command be run off-hours.

#### Requirements

Command privilege
                                 		  level: 0

Allowed during
                                 		  upgrade: Yes

Applies to: Unified
                                    			 Communications Manager , IM and Presence Service on Unified Communications
                                    			 Manager , Cisco Unity
                                    			 Connection

#### Example

```
admin:file view activelog cm/trace/ccm/sdl/{filename}
```

### file view inactivelog

This command displays the contents of a log on the inactive side.

file view inactivelog { file-spec }

## Syntax Description

Specifies the path to the file to view. You can use the wildcard character, *, for file-spec as long as it resolves to one file.

#### Command Modes

Administrator (admin:)

#### Usage Guidelines

Caution

Do not use this command to view binary files because this can corrupt the terminal session.

This command may use a considerable amount of I/O and running it may impact system performance. It is highly recommended that
                                             this command be run off-hours.

#### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified CM , Unified CM with IM and Presence , Cisco Unity Connection

#### Example

```
admin:file view inactivelog cm/trace/ccm/sdl/{filename}
```

### file view
                           	 system-management-log

This command shows
                                 		  the contents of the Integrated Management Logs (IML).

file view system-management-log

#### Command Modes

Administrator (admin:)

#### Usage Guidelines

Caution

Do not use this
                                             			 command to view binary files because this can corrupt the terminal session.

#### Requirements

Command privilege level: 1

Allowed during
                                 		  upgrade: Yes

Applies to: Unified
                                    			 Communications Manager , Cisco Unity
                                    			 Connection

## file view tftp

This command displays the contents of the installation log.

file view tftp file-spec

## Syntax Description

Specifies the path to the file to view. You can use the wildcard character, *, as long as it resolves to one file.

### Command Modes

Administrator (admin:)

### Usage Guidelines

Caution

Do not use this command to view binary files because this can corrupt the terminal session.

### Requirements

Command privilege level: 0

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , Cisco Unity Connection

| Parameters | Description |
|---|---|
| service/feature | specifies the component or functional area from which to retrieve log information |
| duration | specifies the time period, measured in days, from which the log information is retrieved. |

| Parameters | Description |
|---|---|
| detection-size-kb | Specifies
                                       					 the minimum file size change that is required for the command to display the
                                       					 file as changed. Default
                                       					 value: 100 KB. |

| Caution | Because this command can affect system performance, we recommend that you run the command during off-peak hours. |
|---|---|

| Parameters | Description |
|---|---|
| activelog | Specifies a
                                       					 log on the active side. |
| inactivelog | Specifies a
                                       					 log on the inactive side. |
| file-spec | Specifies
                                       					 the path and filename of the log or logs to delete (includes install log
                                       					 files). |
| detail | Shows a
                                       					 listing of deleted files with the date and time. |
| noconfirm | Deletes
                                       					 files without asking you to confirm each deletion. |

| Caution | You cannot
                                          			 recover a deleted file, but you may be able to with The Disaster Recovery
                                          			 System. |
|---|---|

| Parameters | Description |
|---|---|
| file-spec | Represents the TFTP file name. |
| detail | Shows a listing of deleted files with the date and time. |
| noconfirm | Deletes files without asking you to confirm each deletion. |

| Caution | You cannot recover a deleted file, but you may be able to with the Disaster Recovery System. |
|---|---|

| Parameters | Description |
|---|---|
| dir-name | Specifies the TFTP directory to delete. |
| detail | Shows a listing of deleted files with the date and time. |

| Caution | You cannot recover a deleted file, but you may be able to with the Disaster Recovery System. |
|---|---|

| Parameters | Description |
|---|---|
| activelog | Specifies a log on the active side. |
| inactivelog | Specifies a log on the inactive side. |
| install | Specifies an installation log. |
| file-spec | Represents the log file to dump. |
| hex | Shows output in hexadecimal. |
| recent | Dumps the most recently changed file in the directory. |
| regexp expression | Displays only the lines in the file that match the regular expression expression . |

| Parameters | Description |
|---|---|
| file-spec | Represents
                                       					 the name of a TFTP file. |
| page | Displays the
                                       					 output one screen at a time. |
| detail | Displays
                                       					 the listing with the date and time. |
| hex | Displays
                                       					 the output in hexadecimal. |

| Note | file-spec must resolve to a single file. |
|---|---|

| Parameters | Description |
|---|---|
| most fragmented | Represents the most fragmented log files. |
| most recent | Represents the most recent logs files. |
| number | Represents the number of files to list. |

| Parameters | Description |
|---|---|
| filename | Represents the SDI log file name. |
| verbose | Shows more detailed information on the screen. |

| Parameters | Description |
|---|---|
| filename | Specifies the SDI log file name for which you want to show all fragmentation details. |

| Parameters | Description |
|---|---|
| most fragmented | Represents the most fragmented log files. |
| most recent | Represents the most recent log files. |
| number | Represents the number of files to list. |

| Parameters | Description |
|---|---|
| filename | Represents the file name of the SDL log file. |
| verbose | Shows more detailed information on the screen. |

| Parameters | Description |
|---|---|
| filename | Represents the file name for which you want to show all fragmentation details. |

| Parameters | Description |
|---|---|
| activelog | Specifies a
                                       					 log on the active side. |
| inactivelog | Specifies a
                                       					 log on the inactive side. |
| install | Specifies an
                                       					 installation log. |
| file-spec | Specifies
                                       					 the name of the file to transfer. |
| reltime | The relative
                                       					 time period, specified in minutes \| hours \| days \| weeks \| months \| time value |
| abstime | The absolute
                                       					 time period, specified as hh:mm:MM/DD/YY hh:mm:MM/DD/YY |
| match regex | Match a
                                       					 particular string in the filename, specified as regex . |
| recurs | Get all
                                       					 files, including subdirectories. |
| compress | Transfer
                                       					 files as compressed file. |
| tftp |  |

| Parameters | Description |
|---|---|
| partBsalog | Specifies the partBsalog directory. |
| salog | Specifies the salog directory. |
| file-spec | Specifies the name of the file to transfer. |
| reltime | The relative time period, specified in minutes \| hours \| days \| weeks \| months \| time value |
| abstime | The absolute time period, specified as hh:mm:MM/DD/YY hh:mm:MM/DD/YY |
| match regex | Match a particular string in the filename, specified as regex . |
| recurs | Get all files, including subdirectories. |
| compress | Transfer files as compressed file. |

| Parameters | Description |
|---|---|
| file-spec | Specifies the name of the TFTP file to transfer. |
| reltime | The relative time period, specified in minutes \| hours \| days \| weeks \| months \| time value |
| abstime | The absolute time period, specified as hh:mm:MM/DD/YY hh:mm:MM/DD/YY |
| match regex | Match a particular string in the filename, specified as regex . |
| recurs | Get all files, including subdirectories. |
| compress | Transfer files as compressed file. |

| Parameters | Description |
|---|---|
| activelog | Specifies a
                                       					 log on the active side. |
| inactivelog | Specifies a
                                       					 log on the inactive side. |
| install | Specifies an
                                       					 installation log. |
| file-spec | Specifies
                                       					 the name of the log file . |
| page | Shows the
                                       					 output one screen at a time. |
| detail | Shows a
                                       					 detailed listing with date and time. |
| reverse | Reverses the
                                       					 sort direction. |
| date | Sorts files
                                       					 by date. |
| size | Sorts files
                                       					 by size. |

| Parameters | Description |
|---|---|
| partBsalog | Specifies
                                          					 the partBsalog log directory. |
| salog | Specifies
                                          					 the salog log directory. |
| file-spec | Specifies
                                          					 the path to the file or files to list. |
| page | Shows the
                                          					 output one screen at a time. |
| detail | Shows a
                                          					 detailed listing with date and time. |
| reverse | Reverses the
                                          					 sort direction. |
| date | Sorts files
                                          					 by date. |
| size | Sorts files
                                          					 by size. |

| Parameters | Description |
|---|---|
| file-spec | Specifies the name of the TFTP file . |
| page | Shows the output one screen at a time. |
| detail | Shows a detailed listing with date and time. |
| reverse | Reverses the sort direction. |
| date | Sorts files by date. |
| size | Sorts files by size. |

| Parameters | Description |
|---|---|
| activelog | Specifies a log on the active side. |
| inactivelog | Specifies a log on the inactive side. |
| install | Specifies an installation log. |
| file-spec | Specifies the name of the file to search. |
| reltime | The relative time period, specified in minutes \| hours \| days \| weeks \| months \| time value |
| abstime | The absolute time period, specified as hh:mm:MM/DD/YY hh:mm:MM/DD/YY |
| ignorecase | Ignores case in a search. |

| Parameters | Description |
|---|---|
| file-spec | Specifies the name of the TFTP file to search. |
| reltime | The relative time period, specified in minutes \| hours \| days \| weeks \| months \| time value |
| abstime | The absolute time period, specified as hh:mm:MM/DD/YY hh:mm:MM/DD/YY |
| ignorecase | Ignores case in a search. |

| Parameters | Description |
|---|---|
| activelog | Specifies a log on the active side. |
| inactivelog | Specifies a log on the inactive side. |
| install | Specifies an installation log. |
| filespec | Specifies the path to the file. You can use the wildcard character, *, for filename as long as it resolves to one file. |
| hex | Show the listing in hexadecimal. |
| lines | Specifies the number of lines to display. |
| regexp expression | Tails log files that match expression |

| Parameters | Description |
|---|---|
| filespec | Specifies the path to the file. You can use the wildcard character, *, for filename as long as it resolves to one file. |
| detail | Long listing with date and time |
| hex | Show the listing in hexadecimal. |
| lines | Specifies the number of lines to display. |

| Parameters | Description |
|---|---|
| activelog | Shows the contents of an active side logging files |
| inactivelog | Shows the contents of an inactive side logging files |
| install | Shows the contents of an install logging file |
| file-spec | Specifies the path to the file to view. You can use the wildcard character, *, as long as it resolves to one file. |

| Caution | Do not use this command to view binary files because this can corrupt the terminal session. |
|---|---|

| Parameters | Description |
|---|---|
| activelog | Shows the
                                          					 contents of an active side logging files |
| file-spec | Specifies
                                          					 the path to the file to view. You can use the wildcard character, *, as long as
                                          					 it resolves to one file. |

| Caution | Do not use this
                                             			 command to view binary files because this can corrupt the terminal session. |
|---|---|

| Note | This command may use a considerable amount of I/O and running it may impact system performance. It is highly recommended that
                                             this command be run off-hours. |
|---|---|

| Parameters | Description |
|---|---|
| file-spec | Specifies the path to the file to view. You can use the wildcard character, *, for file-spec as long as it resolves to one file. |

| Caution | Do not use this command to view binary files because this can corrupt the terminal session. |
|---|---|

| Note | This command may use a considerable amount of I/O and running it may impact system performance. It is highly recommended that
                                             this command be run off-hours. |
|---|---|

| Caution | Do not use this
                                             			 command to view binary files because this can corrupt the terminal session. |
|---|---|

| Parameters | Description |
|---|---|
| file-spec | Specifies the path to the file to view. You can use the wildcard character, *, as long as it resolves to one file. |

| Caution | Do not use this command to view binary files because this can corrupt the terminal session. |
|---|---|