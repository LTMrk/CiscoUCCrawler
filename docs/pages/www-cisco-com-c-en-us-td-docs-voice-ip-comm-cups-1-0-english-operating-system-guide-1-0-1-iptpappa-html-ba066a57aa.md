---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-english-operating-system-guide-1-0-1-iptpappa-html-ba066a57aa
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0/english/operating_system/guide/1_0_1/iptpappa.html
retrieved_at: 2026-08-21T02:47:30.024530+00:00
---

Cisco Unified Communications Operating System Administration Guide, Release 1.0(1)

# Cisco Unified Communications Operating System Administration Guide, Release 1.0(1)

Updated: July 17, 2006

Chapter: Command Line Interface

## Chapter: Command Line Interface

## Command Line Interface

## Overview

This appendix describes commands that you can use on the Cisco IPT Platform to perform basic operating system functions. The Cisco IPT Platform Administration GUI application also makes these functions available. Typically you would use the command-line interface (CLI) only when a problem occurs while you are using the Cisco IPT Platform Administration interface.

## Starting a CLI Session

You can access the Cisco IPT Platform CLI remotely or locally:

• From a web client workstation, such as the workstation that you use for Cisco IPT Platform Administration, you can use SSH to connect securely to the Cisco IPT Platform.

• You can access the Cisco IPT Platform CLI directly by using the monitor and keyboard that you used during installation or by using a terminal server that is connected to the serial port. Use this method if a problem exists with the IP address.

Before You Begin

Ensure you have the following information that gets defined during installation:

• A primary IP address and hostname

• An administrator ID

• A password

You will need this information to log in to the Cisco IPT Platform.

Perform the following steps to start a CLI session:

Step 1 Do one of the following actions depending on your method of access:

• From a remote system, use SSH to connect securely to the Cisco IPT Platform. In your SSH client, enter

ssh adminname @ hostname

where adminname specifies the Administrator ID and hostname specifies the hostname that was defined during installation.

For example, ssh admin@ipt-1 .

• From a direct connection, you receive this prompt automatically:

```
ipt-1 login:
```

where ipt-1 represents the host name of the system.

Enter the administrator ID that was defined during installation.

In either case, the system prompts you for a password.

Step 2 Enter the password that was defined at installation.

The CLI prompt displays. The prompt represents the Administrator ID; for example:

admin:

You can now use any CLI command.

## CLI Basics

The following section contains basic tips for using the command line interface.

### Completing Commands

To complete commands, use Tab :

• Enter the start of a command and press Tab to complete the command. For example, if you enter se and press Tab , set gets completed.

• Enter a full command name and press Tab to display all the commands or subcommands that are available. For example, if you enter set and press Tab, you see all the set subcommands. An * identifies the commands that have subcommands.

• If you reach a command, keep pressing Tab , and the current command line repeats; this indicates that no additional expansion is available.

### Getting Help on Commands

You can get two kinds of help on any command:

• Detailed help that includes a definition of the command and an example of its use

• Short query help that includes only command syntax

To get detailed help, at the CLI prompt, enter

help command

Where command specifies the command name or the command and parameter. See Example 1 .

To query only command syntax, at the CLI prompt, enter

command ?

Where command represents the command name or the command and parameter. See Example 2 .

Note If you enter a ? after a menu command, such as set , it acts like the Tab key and lists the commands that are available.

Example 1 Detailed Help Example:

```
admin:help file list activelog
```

```
activelog help:
```

```
This will list active logging files
```

```
options are:
```

```
page    - pause output
```

```
detail  - show detailed listing
```

```
reverse - reverse sort order
```

```
date    - sort by date
```

```
size    - sort by size
```

```
file-spec can contain '*' as wildcards
```

```
Example:
```

```
admin:file list activelog platform detail
```

```
02 Dec,2004 12:00:59      <dir>    drf
```

```
02 Dec,2004 12:00:59      <dir>    log
```

```
16 Nov,2004 21:45:43        8,557  enGui.log
```

```
27 Oct,2004 11:54:33       47,916  startup.log
```

```
dir count = 2, file count = 2
```

Example 2 Query Example:

```
admin:file list activelog?
```

```
Syntax:
```

```
file list activelog file-spec [options]
```

```
file-spec   mandatory   file to view
```

```
options     optional    page|detail|reverse|[date|size]
```

### Ending a CLI Session

At the CLI prompt, enter quit . If you are logged in remotely, you get logged off, and the ssh session gets dropped. If you are logged in locally, you get logged off, and the login prompt returns.

## Cisco IPT Platform CLI Commands

The following tables list and describe the CLI commands that are available for the Cisco Unified Communications Operating System and for Cisco Unified CallManager.

### File Commands

The following table lists and explains the CLI File commands:

Table A-1 File Commands

file check

[ detection-size-kb ]

Where

detection-size-kb specifies the minimum file size change that is required for the command to display the file as changed.

Default minimum size: 100 KB

The command notifies you about a possible impact to system performance and asks you whether you want to continue.

Options

None

This command checks the /usr directory tree to see whether any files or directories have been added, removed, or changed in size since the last fresh installation or upgrade and displays the results. The display includes both deleted and new files.

Command privilege level: 0

Allowed during upgrade: No

file delete

activelog directory/filename [ detail ] [ noconfirm ]

inactivelog directory/filename [ detail ] [ noconfirm ]

install directory/filename [ detail ] [ noconfirm ]

tftp directory/filename [ detail ]

Where

• activelog specifies a log on the active side.

• inactivelog specifies a log on the inactive side.

• install specifies an installation log.

• tftp specifies a TFTP file.

You can use the wildcard character, *, for filename .

If you delete a TFTP data file on the inactive side, you may need to manually restore that file if you switch versions to the inactive side.

Options

• detail —Displays a listing of deleted files with the date and time.

• noconfirm —Deletes files without asking you to confirm each deletion.

This command deletes one or more files.

Command privilege level: 1

Allowed during upgrade: Yes

Example: Delete the install log

```
file delete install install.log
```

file dump

activelog directory/filename [detail] [hex ]

inactivelog directory/filename [detail] [hex ]

install directory/filename [detail] [hex ]

tftp directory/filename [detail] [hex ]

Where

• activelog specifies a log on the active side.

• inactivelog specifies a log on the inactive side.

• install specifies an installation log.

• tftp specifies a TFTP file.

You can use the wildcard character, *, for filename as long as it resolves to one file.

Options

• detail —Displays listing with the date and time.

• hex —Displays output in hexadecimal.

This command dumps the contents of a file to the screen, a page at a time.

Command privilege level: 1 for logs, 0 for TFTP files

Allowed during upgrade: Yes

Example: Dump contents of file _cdrIndex.idx

```
file dump activelog 
cm/cdr/_cdrIndex.idx
```

file get

activelog directory/filename [ reltime ] [ abstime ] [ match ] [ recurs ]

inactivelog directory/filename [ reltime ] [ abstime ] [ match ] [ recurs ]

install directory/filename [ reltime ] [ abstime ] [ match ] [ recurs ]

tftp directory/filename [ reltime ] [ abstime ] [ match ] [ recurs ]

Where

• activelog specifies a log on the active side.

• inactivelog specifies a log on the inactive side.

• install specifies an installation log.

• tftp specifies a TFTP file.

Options

• abstime —Absolute time period, specified as

hh:mm:MM/DD/YY hh:mm:MM/DD/YY

• reltime —Relative time period, specified as

minutes | hours | days | weeks | months <value>

• match —Match a particular string in the filename, specified as

```
<string value>
```

• recurs —Get all files, including subdirectories

After the command identifies the specified files, you get prompted to enter an SFTP host, username, and password.

This command sends the file to another system by using SFTP.

Command privilege level: 0

Allowed during upgrade: Yes

Example 1: Get all files in the activelog operating system directory that match the string "plat"

```
file get activelog platform match plat
```

Example 2: Get all operating system log files for a particular time period

```
file get activelog platform/log abstime 
18:00:9/27/200 18:00:9/28/2005
```

file list

activelog directory [ page] [detail] [reverse] [ date | size ]

inactivelog directory [ page] [detail] [reverse] [ date | size ]

install directory [ page] [detail] [reverse] [ date | size ]

tftp directory [ page] [detail] [reverse] [ date | size ]

Where

• activelog specifies a log on the active side.

• inactivelog specifies a log on the inactive side.

• install specifies an installation log.

• tftp specifies a TFTP file.

Note You can use a wildcard character, *, for directory name as long as it resolves to one directory.

Options

• detail —Long listing with date and time

• date —Sort by date

• size —Sort by file size

• reverse —Reverse sort direction

• page —Displays the output one screen at a time

This command lists the log files in an available log directory.

Command privilege level: 1 for logs, 0 for TFTP files

Allowed during upgrade: Yes

Example 1: List Operating System Log files with details

```
file list activelog platform/log page 
detail
```

Example 2: List directories in CDR Repository

```
file list activelog cm/cdr_repository
```

Example 3: List CDR files in a specified directory by size

```
file list activelog 
cm/cdr_repository/processed/20050812 
size
```

file search

activelog directory/filename reg-exp [abstime hh : mm : ss mm / dd / yyyy hh : mm : ss mm / dd / yyyy ] [ ignorecase ] [reltime { days|hours|minutes} timevalue ]

inactivelog directory/filename reg-exp [abstime hh : mm : ss mm / dd / yyyy hh : mm : ss mm / dd / yyyy ] [ ignorecase ] [reltime { days|hours|minutes} timevalue ]

install directory/filename reg-exp [abstime hh : mm : ss mm / dd / yyyy hh : mm : ss mm / dd / yyyy ] [ ignorecase ] [reltime { days|hours|minutes} timevalue ]

tftp directory/filename reg-exp [abstime hh : mm : ss mm / dd / yyyy hh : mm : ss mm / dd / yyyy ] [ ignorecase] [reltime { days|hours|minutes} timevalue ]

Where

• activelog specifies a log on the active side.

• inactivelog specifies a log on the inactive side.

• install specifies an installation log.

• tftp specifies a TFTP file.

• reg-exp represents a regular expression.

Note You can use the wildcard character, *, to represent all or part of the filename.

Options

• abstime —Specifies which files to search based on file creation time. Enter a start time and an end time.

• days|hours|minutes —Specifies whether the file age is in days, hours, or minutes.

• ignorecase —Ignores case when searching

• reltime —Specifies which files to search based on file creation time. Enter the age of files to search.

• hh : mm : ss mm / dd / yyyy —An absolute time, in the format hours:minutes:seconds month/day/year.

• timevalue —The age of files to search. The unit of this value is specified with the { days|hours|minutes} option.

This command searches the content of a log and displays the matching lines a page at a time.

Write the search term in the form of a regular expression, which is a special text string for describing a search pattern.

If the search term is found in only one file, the filename appears at the top of the output. If the search term is found in multiple files, each line of the output begins with the filename in which the matching line was found.

Command privilege level: 0

Allowed during upgrade: Yes

Example

```
file search activelog 
platform/log/platform.log Err[a-z] 
ignorecase
```

file tail

activelog directory/filename [ detail] [hex] [lines ]

inactivelog directory/filename [ detail] [hex] [lines ]

install directory/filename [ detail] [hex] [lines ]

tftp directory/filename [ detail] [hex] [lines ]

Where

• activelog specifies a log on the active side.

• inactivelog specifies a log on the inactive side.

• install specifies an installation log.

• tftp specifies a TFTP file.

You can use the wildcard character, *, for filename so long as it resolves to one file.

Options

• detail —Long listing with date and time

• hex —Hexadecimal listing

• lines —Number of lines to display

This command tails (prints the last few lines) of a log file.

Command privilege level: 1 for logs, 0 for TFTP files

Allowed during upgrade: Yes

Example: Tail the operating system CLI log file

```
file tail activelog 
platform/log/cli00001.log
```

file view

activelog directory/filename

inactivelog directory/filename

install directory/filename

tftp directory/filename

Where

• activelog specifies a log on the active side.

• inactivelog specifies a log on the inactive side.

• install specifies an installation log.

• tftp specifies a TFTP file.

Note You can use the wildcard character, *, for filename so long as it resolves to one file.

This command displays the contents of a file.

Command privilege level: 0

Allowed during upgrade: Yes

Example 1: Display the install log

```
file view install install.log
```

Example 2: Display a particular CDR file

```
file view activelog 
/cm/cdr_repository/processed/20058012/{
filename}
```

### Show Commands

The following table lists and explains the CLI Show commands:

Table A-2 Show Commands

show account

None

This command lists current administrator accounts, except the master administrator account.

Command privilege level: 4

Allowed during upgrade: Yes

show cert

own filename

trust filename

list {own | trust}

Where

• filename represents the name of the certificate file.

• own specifies owned certificates.

• trust specifies trusted certificates.

• list specifies a certificate trust list.

Options

None

This command displays certificate contents and certificate trust lists.

Command privilege level: 1

Allowed during upgrade: Yes

Example: Display own certificate trust lists

```
show cert list own
```

show firewall

list [ detail ] [ page ] [ file filename ]

Where

• detail —Displays detailed statistics on every available device on the system

• page —Displays the output one page at a time

• file filename —Outputs the information to a file

Note The file option saves the information to platform/cli/ filename .txt. The file name cannot contain the "." character.

This command displays system aspects of the server.

Command privilege level: 1

Allowed during upgrade: Yes

show hardware

None

This command displays the following information on the platform hardware:

• Platform

• Serial number

• BIOS build level

• BIOS manufacturer

• Active processors

• RAID controller status

Command privilege level: 0

Allowed during upgrade: Yes

show ipsec

policy

association policy

information policy association

Where

• policy displays all IPSec policies on the node.

• association displays the association list and status for the policy.

• information displays the association details and status for the policy.

• policy represents the name of a specific IPSec policy.

• association represents the association name.

Options

None

This command displays information on IPSec policies and associations.

Command privilege level: 1

Allowed during upgrade: yes

Example: Display IPSec policies

```
show ipsec policy
```

show myself

None

This command displays information about the current account.

Command privilege level: 0

Allowed during upgrade: Yes

show network

eth0 [ detail ]

failover [ detail ] [ page ]

route [ detail ]

status [ detail ] [ listen ] [ process] [ all ] [ nodns ] [ search stext ]

all [ detail ]

Where

• eth0 specifies Ethernet 0.

• failover specifies Network Fault Tolerance information.

• route specifies network routing information.

• status specifies active Internet connections.

• all specifies all basic network information.

Options

• detail —Displays additional information

• page —Displays information 1 page at a time.

• listen —Displays only listening sockets

• process —Displays the process ID and name of the program to which each socket belongs

• all —Displays both listening and nonlistening sockets

• nodns —Displays numerical addresses without any DNS information

• search stext —Searches for the stext in the output

This command displays network information.

The eth0 parameter Ethernet port 0 settings, including DHCP and DNS configurations.

Command privilege level: 0

Allowed during upgrade: Yes

Example: Display active Internet connections

```
show network status
```

show packages

active name [ page ]

inactive name [ page ]

Where

name represents the package name.

To display all active or inactive packages, use the wildcard character, *.

Options

page —Displays the output one page at a time

This command displays the name and version for installed packages.

Command privilege level: 0

Allowed during upgrade: Yes

show perf

counterhelp class-name counter-name

Where

• class-name represents the class name that contains the counter.

• counter-name represents the counter that you want to view.

Note If the class name or counter name contains white spaces, enclose the name in double quotation marks.

Options

None

This command displays the explanation text for the specified perfmon counter.

Command privilege level: 0

Allowed during upgrade: Yes

show perf

list categories

Options

None

This command lists all categories in the perfmon system.

Command privilege level: 0

Allowed during upgrade: Yes

show perf

list classes [ -t category ] [ -d ]

Options

• -d —Displays detailed information

• -t category —Displays perfmon classes for the specified category

This commands lists the perfmon classes or objects.

Command privilege level: 0

Allowed during upgrade: Yes

show perf

list counters class-name [ -d ]

Where

class-name represents a perfmon class name for which you want to list the counters.

Note If the class name contains white spaces, enclose the name in double quotation marks.

Options

-d —Displays detailed information

This command lists perfmon counters for the specified perfmon class.

Command privilege level: 0

Allowed during upgrade: Yes

show perf

list instances class-name [ -d ]

Where

class-name represents a perfmon class name for which you want to list the counters.

Note If the class name contains white spaces, enclose the name in double quotation marks.

Options

-d —Displays detailed information

The command lists the perfmon instances for the specified perfmon class.

Command privilege level: 0

Allowed during upgrade: Yes

show perf

query class class-name [, class-name ...]

Where

class-name specifies the perfmon class that you want to query.

You can specify a maximum of 5 classes per command.

Note If the class name contains white spaces, enclose the name in double quotation marks.

Options

None

This command queries a perfmon class and displays all the instances and counter values of each instance.

Command privilege level: 0

Allowed during upgrade: Yes

show perf

query counter class-name counter-name [, counter-name ...]

Where

• class-name specifies the perfmon class that you want to query.

• counter-name specifies the counter to view.

You can specify a maximum of 5 counters per command.

Note If the class name or counter name contains white spaces, enclose the name in double quotation marks.

Options

None

This command queries the specified counter and displays the counter value of all instances.

Command privilege level: 0

Allowed during upgrade: Yes

show perf

query instance class-name instance-name [, instance-name ...]

Where

• class-name specifies the perfmon class that you want to query.

• instance-name specifies the perfmon instance to view.

You can specify a maximum of 5 instances per command.

Note If the class name or instance name contains white spaces, enclose the name in double quotation marks.

Options

None

This command queries the specified instance and displays all its counter values.

Note This command does not apply to singleton perfmon classes.

Command privilege level: 0

Allowed during upgrade: Yes

show perf

query path path-spec [, path-spec ...]

Where path-spec gets defined as follows:

• For an instance-based perfmon class, specify path-spec as class-name ( instance-name )\ counter-name .

• For a noninstance-based perfmon class (a singleton), specify path-spec as class-name \ counter-name .

You can specify a maximum of 5 paths per command.

Note If the path name contains white spaces, enclose the name in double quotation marks.

Options

None

This command queries a specified perfmon path.

Command privilege level: 0

Allowed during upgrade: Yes

Example

```
show perf query path "Cisco 
Phones(phone-0)\CallsAttempted", 
"Cisco Unified CallManager\T1Channel
sActive"
```

show process

load [ cont ] [ clear ] [ noidle ] [ num xx ] [ thread ] [ cpu ] [ memory ] [ time ] [ specified ] [ page ]

list [ page ] [ short ] [ detail ] [ thread] [ fd ] [ cont ] [ clear ] [ process id id ] [ argument id id ] [ owner name name ]

Where

• load displays the CPU load for each active process.

• list displays all processes.

Options

• cont —Command repeats continuously

• clear —Clears screen before displaying output

• noidle —Ignore idle or zombie processes

• num xx —Sets the number of processes to display (Default=10, all = all processes)

• thread —Displays threads

• cpu —Displays output by CPU usage

• memory —Sorts output by memory usage

• short—Displays short listing

• time —Sorts output by time usage

• page —Displays one page at a time

• detail —Displays a detailed listing

• process id id —Shows only specific process number or command name

• argument name name —Show only specific process with argument name

• thread —Include thread processes in the listing

• fd —Show file descriptors that are associated with a process

This command displays process and load information.

Command privilege level: 1

Allowed during upgrade: Yes

Example: Show detailed process listing one page at a time

```
show process list detail page
```

show registry

system component [ name ] [page]

Where

• system represents the registry system name.

• component represents the registry component name.

• name represents the name of the parameter to show.

Note To display all items, enter the wildcard character, *.

Display Options

page —Displays one page at a time

This command displays the contents of the registry.

Command privilege level: 1

Allowed during upgrade: Yes

Example: show contents of the cm system, dbl/sdi component

```
show registry cm dbl/sdi
```

show risdb

list [ file filename ]

query table1 table2 table3 ... [ file filename ]

Where

• list displays the tables supported in the Realtime Information Service (RIS) database.

• query displays the contents of the RIS tables.

Options

file filename —Outputs the information to a file

Note The file option saves the information to platform/cli/ filename .txt. The file name cannot contain the "." character.

This command displays RIS database table information.

Command privilege level: 0

Allowed during upgrade: Yes

Example: Display list of RIS database tables

```
show risdb list
```

show smtp

None

This command displays the name of the SMTP host.

Command privilege level: 0

Allowed during upgrade: Yes

show stats

io [ kilo ] [ detail ] [ page ] [ file filename ]

Options

• kilo —Displays statistics in kilobytes

• detail —Displays detailed statistics on every available device on the system and overrides the kilo option

• file filename —Outputs the information to a file

Note The file option saves the information to platform/cli/ filename .txt. The file name cannot contain the "." character.

This command displays system IO statistics.

Command privilege level: 1

Allowed during upgrade: Yes

show status

None

This command displays the following basic platform status:

• Host name

• Date

• Time zone

• Locale

• Product version

• Platform version

• CPU usage

• Memory and disk usage

Command privilege level: 0

show tech

all [ page ] [ file filename ]

Options

• page —Displays one page at a time

• file filename —Outputs the information to a file

Note The file option saves the information to platform/cli/ filename .txt. The file name cannot contain the "." character.

This command displays the combined output of all show tech commands.

Command privilege level: 1

Allowed during upgrade: Yes

show tech

ccm_service

Options

None

This command displays information on all Cisco Unified CallManager services that can run on the system.

Command privilege level: 0

Allowed during upgrade: Yes

show tech

database

Options

None

This command creates a CSV file of the entire database.

Command privilege level: 1

Allowed during upgrade: Yes

show tech

dbinuse

Options

None

This command displays the database in use.

Command privilege level: 1

Allowed during upgrade: Yes

show tech

dbschema

Options

None

This command displays the database schema in a CSV file.

Command privilege level: 1

Allowed during upgrade: Yes

show tech

devdefaults

Options

None

This command displays the device defaults table.

Command privilege level: 1

Allowed during upgrade: Yes

show tech

gateway

Options

None

This command displays the gateway table from the database.

Command privilege level: 1

Allowed during upgrade: Yes

show tech

locales

Options

None

This command displays the locale information for devices, device pools, and end users.

Command privilege level: 1

Allowed during upgrade: Yes

show tech

network [ page ] [ file filename ]

Options

• page —Displays one page at a time

• file filename —Outputs the information to a file

Note The file option saves the information to platform/cli/ filename .txt. The file name cannot contain the "." character.

This command displays network aspects of the server.

Command privilege level: 1

Allowed during upgrade: Yes

show tech

notify

Options

None

This command displays the database change notify monitor.

Command privilege level: 1

Allowed during upgrade: Yes

show tech

params all

Options

None

This command displays all the database parameters.

Command privilege level: 1

Allowed during upgrade: Yes

show tech

params enterprise

Options

None

This command displays the database enterprise parameters.

Command privilege level: 1

Allowed during upgrade: Yes

show tech

params service

Options

None

This command displays the database service parameters.

Command privilege level: 1

Allowed during upgrade: Yes

show tech

procedures

Options

None

This command displays the procedures in use for the database.

Command privilege level: 1

Allowed during upgrade: Yes

show tech

routepatterns

Options

None

This command displays the route patterns that are configured for the system.

Command privilege level: 1

Allowed during upgrade: Yes

show tech

routeplan

Options

None

This command displays the route plan that are configured for the system.

Command privilege level: 1

Allowed during upgrade: Yes

show tech

runtime [ page ] [ file filename ]

Options

page —Displays one page at a time

file filename —Outputs the information to a file

Note The file option saves the information to platform/cli/ filename .txt. The file name cannot contain the "." character.

This command displays runtime aspects of the server.

Command privilege level: 1

Allowed during upgrade: Yes

show tech

systables

Options

None

This command displays the name of all tables in the sysmaster database.

Command privilege level: 1

Allowed during upgrade: Yes

show tech

system [ page ] [ file filename ]

Options

page —Displays one page at a time

file filename —Outputs the information to a file

Note The file option saves the information to platform/cli/ filename .txt. The file name cannot contain the "." character.

This command displays system aspects of the server.

Command privilege level: 1

Allowed during upgrade: Yes

show tech

table table_name [ page ] [ csv ]

Where

table_name represents the name of the table to display.

Options

page —Displays the output one page at a time

csv —Sends the output to a comma separated values file

This command displays the contents of the specified database table.

Command privilege level: 1

Allowed during upgrade: Yes

show tech

triggers

Options

None

This command displays table names and the triggers that are associated with those tables.

Command privilege level: 1

Allowed during upgrade: Yes

show tech

version [page]

Options

Page—Displays the output one page at a time

This command displays the version of the installed components.

Command privilege level: 1

Allowed during upgrade: Yes

show timezone

config

list [ page ]

Where

• config displays the current time zone settings.

• list displays the available time zones.

Options

page —Displays the output one page at a time

This command displays time zone information.

Command privilege level: 0

Allowed during upgrade: Yes

show trace

[ task_name ]

Where

task_name represents the name of the task for which you want to display the trace information.

Note If you do not enter any parameters, the command returns a list of available tasks.

Options

None

This command displays trace information for a particular task.

Command privilege level: 0

Allowed during upgrade: Yes

Example: Display trace information for cdp

```
show trace cdps
```

show version

active

inactive

Options

None

This command displays the software version on the active or inactive partition.

Command privilege level: 0

Allowed during upgrade: Yes

show web-security

None

This command displays the contents of the current web-security certificate.

Command privilege level: 0

Allowed during upgrade: Yes

show workingdir

None

This command retrieves the current working directory for activelog, inactivelog, install, and TFTP.

Command privilege level: 0

Allowed during upgrade: Yes

### Set Commands

The following table lists and explains the CLI Set commands.

Table A-3 Set Commands

set account

name

Where

name represents the username for the new account.

Note After you enter the username, the system prompts you to enter the privilege level and password for the new account.

Options

None

This command sets up a new account on the operating system.

Command privilege level: 0

Allowed during upgrade: No

set cert

regen unit-name

Where

unit-name represents the name of the certificate that you want to regenerate.

Options

None

This command enables you to regenerate the specified security certificate.

Command privilege level: 1

Allowed during upgrade: No

set ipsec

policy { ALL | policy-name }

association policy-name { ALL | association-name }

Where

• policy-name represents an IPSec policy.

• association-name represents an IPSec association.

Options

None

This command allows you to set IPSec policies and associations.

Command privilege level: 1

Allowed during upgrade: No

set logging

{ enable | disable }

Options

None

This command allows you to enable or disable logging.

Command privilege level: 0

Allowed during upgrade: Yes

set network

dhcp eth0 { enable | disable }

Where

• eth0 specifies Ethernet interface 0.

The system asks whether you want to continue to execute this command.

Options

None

This command enables or disables DHCP for Ethernet interface 0.

Command privilege level: 1

Allowed during upgrade: No

set network

dns { primary | secondary } ip-address

Where

ip-address represents the IP address of the primary or secondary DNS server.

The system asks whether you want to continue to execute this command.

Options

None

This command sets the IP address for the primary or secondary DNS server.

Command privilege level: 1

Allowed during upgrade: No

set network

dns options [ timeout seconds ] [ attempts number ] [ rotate ]

Where

• timeout sets the DNS request timeout.

• attempts sets the number of times to attempt a DNS request before quitting.

• rotate causes the system to rotate among the configured DNS servers, distributing the load.

• seconds specifies the DNS timeout period, in seconds.

• number specifies the number of attempts.

Options

None

This command sets DNS options.

Command privilege level: 0

Allowed during upgrade: Yes

set network

domain domain-name

Where

domain-name represents the system domain that you want to assign.

The system asks whether you want to continue to execute this command.

Options

None

This command sets the domain name for the system.

Command privilege level: 1

Allowed during upgrade: No

set network

failover { enable | disable }

Where

• enable enables Network Fault Tolerance.

• disable disables Network Fault Tolerance.

Options

None

This command enables and disables Network Fault Tolerance.

Command privilege level: 1

Allowed during upgrade: No

set network

gateway ip-address

Where

ip-address represents the IP address of the network gateway that you want to assign.

The system asks whether you want to continue to execute this command.

Options

None

This command enables you to configure the IP address of the network gateway.

Command privilege level: 1

Allowed during upgrade: No

set network

ip eth0 ip-address ip-mask

Where

• eth0 specifies Ethernet interface 0.

• ip-address represents the IP address that you want assign.

• ip-mask represents the IP mask that you want to assign.

The system asks whether you want to continue to execute this command.

Options

None

This command sets the IP address for Ethernet interface 0.

Command privilege level: 1

Allowed during upgrade: No

set network

nic eth0 [ auto en | dis ] [ speed 10 | 100 ] [ duplex half | full ]

Where

• eth0 specifies Ethernet interface 0.

• auto specifies whether auto negotiation gets enabled or disabled.

• speed specifies whether the speed of the Ethernet connection: 10 or 100 Mbps.

• duplex specifies half-duplex or full-duplex.

The system asks whether you want to continue to execute this command.

Note You can enable only one active NIC at a time.

Options

None

This command sets the properties of the Network Interface Card (NIC).

Command privilege level: 1

Allowed during upgrade: No

set network

status eth0 { up | down }

Where

eth0 specifies Ethernet interface 0.

Options

None

This command sets the status of Ethernet 0 to up or down.

Command privilege level: 1

Allowed during upgrade: No

set output

{ enable | disable }

Options

None

This command allows you to enable or disable the operating system output.

Command privilege level: 0

Allowed during upgrade: Yes

set password

{ admin | security }

The systems prompts you for the old and new passwords.

Note The password must contain at least six characters, and the system checks it for strength.

This command allows you to change the administrator and security passwords.

Command privilege level: 1

Allowed during upgrade: No

set smtp

hostname

Where

hostname represents the SMTP server name.

Options

None

This command sets the SMTP server hostname.

Command privilege level: 0

Allowed during upgrade: No

set timezone

timezone

Note Enter enough characters to uniquely identify the new time zone. Be aware that the time-zone name is case-sensitive.

Options

None

This command lets you change the system time zone.

Command privilege level: 0

Allowed during upgrade: No

Example: Set the time zone to Pacific time

```
set timezone Pac
```

set trace

enable Error tname

enable Special tname

enable State_Transition tname

enable Significant tname

enable Entry_exit tname

enable Arbitrary tname

enable Detailed tname

disable tname

Where

• tname represents the task for which you want to enable or disable traces.

• enable Error sets task trace settings to the error level.

• enable Special sets task trace settings to the special level.

• enable State_Transition sets task trace settings to the state transition level.

• enable Significant sets task trace settings to the significant level.

• enable Entry_exit sets task trace settings to the entry_exit level.

• enable Arbitrary sets task trace settings to the arbitrary level.

• enable Detailed sets task trace settings to the detailed level.

• disable unsets the task trace settings.

Options

None

This command sets trace activity for the the specified task.

Command privilege level: 1

Allowed during upgrade: No

set web-security

orgunit orgname locality state country

Where

• orgunit represents the organizational unit.

• orgname represents the organizational name.

• locality represents the organization's location.

• state represents the organization's state.

• country represents the organization's country.

Options

None

This command sets the web security certificate information for the operating system.

Command privilege level: 0

Allowed during upgrade: No

set workingdir

activelog directory

inactivelog directory

install directory

tftp directory

Where

• activelog sets the working directory for active logs.

• inactivelog set the working directory for inactive logs.

• install sets the working directory for installation logs.

• tftp sets the working directory for TFTP files.

• directory represents the current working directory.

Options

None

This command sets the working directory for active, inactive, and installation logs.

Command privilege level: 0 for logs, 1 for TFTP

Allowed during upgrade: Yes

### Unset Commands

The following table lists and explains the CLI Unset commands:

Table A-4 Unset Commands

unset ipsec

policy { ALL | policy-name }

association policy-name { ALL | association-name }

Where

• policy-name represents the name of an IPSec policy.

• association-name represents the name of an IPSec association.

Options

None

This command allows you to disable IPSec policies and associations.

Command privilege level: 1

Allowed during upgrade: No

### Delete Commands

The following table lists and explains the CLI Delete commands:

Table A-5 Delete Commands

delete account

account-name

Where

account-name represents the name of an administrator account.

Options

None

This command allows you to delete an administrator account.

Command privilege level: 4

Allowed during upgrade: No

delete dns

ip-address

Where

ip-address represents the IP address of the DNS server you want to delete.

The system asks whether you want to continue to execute this command.

Options

None

This command allows you to delete the IP address for a DNS server.

Command privilege level: 1

Allowed during upgrade: No

delete ipsec

policy { ALL | policy-name }

association policy name { ALL | association-name }

Where

• policy-name represents an IPSec policy.

• association-name represents an IPSec association.

Options

None

This command allows you to delete IPSec policies and associations.

Command privilege level: 1

Allowed during upgrade: No

delete process

process-id [ force | terminate | crash ]

Where

• process-id represents the process ID number.

Options

• force— Tells the process to stop

• terminate —Tells the operating system to terminate the process

• crash —Crashes the process and produces a crash dump

Note Use the force option only if the command alone does not delete the process and use the terminate option only if force does not delete the process.

This command allows you to delete a particular process.

Command privilege level: 1

Allowed during upgrade: Yes

delete smtp

None

This command allows you to delete the SMTP host.

Command privilege level: 1

Allowed during upgrade: No

### Utility Commands

The following table lists and explains the CLI Utility commands:

Table A-6 Utility Commands

utils csa

disable

The system disables CSA.

Options

None

This command stops Cisco Security Agent (CSA).

Command privilege level: 1

Allowed during upgrade: No

utils csa

enable

The system prompts you to confirm that you want to enable CSA.

Options

None

This command enables Cisco Security Agent (CSA).

Command privilege level: 1

Allowed during upgrade: No

utils csa

status

The system indicates whether CSA is running or not.

Options

None

This command displays the current status of Cisco Security Agent (CSA).

Command privilege level: 0

Allowed during upgrade: No

utils disaster_ recovery

backup tape tapeid

Where

tapeid represents the ID of an available tape device.

Options

None

This command starts a backup job and stores the resulting tar file on tape.

Command privilege level: 1

Allowed during upgrade: No

utils disaster_ recovery

backup network path servername username

Where

• path represents the location of the backup files on the remote server.

• servername represents the IP address or host name of the server where you stored the backup files.

• username represents the username that is needed to log in to the remote server.

Note The system prompts you to enter the password for the account on the remote server.

Options

None

This command starts a backup job and stores the resulting tar file on a remote server.

Command privilege level: 1

Allowed during upgrade: No

utils disaster_ recovery

cancel_bakckup

The system prompts you to confirm that you want to cancel the backup job.

Options

None

This command cancels the ongoing backup job.

Command privilege level: 1

Allowed during upgrade: No

utils disaster_ recovery

restore tape server tarfilename tapeid

Where

• server specifies the hostname of the server that you want to restore.

• tarfilename specifies the name of the file to restore.

• tapeid specifies the name of the tape device from which to perform the restore job.

Options

None

This command starts a restore job and takes the backup tar file from tape.

Command privilege level: 1

Allowed during upgrade: No

utils disaster_ recovery

restore network restore_server tarfilename path servername username

Where

• restore_server specifies the hostname of the server that you want to restore.

• tarfilename specifies the name of the file to restore.

• path represents the location of the backup files on the remote server.

• servername represents the IP address or host name of the server where you stored the backup files.

• username represents the username that is needed to log in to the remote server.

Note The system prompts you to enter the password for the account on the remote server.

Options

None

This command starts a restore job and takes the backup tar file from a remote server.

Command privilege level: 1

Allowed during upgrade: No

utils disaster_ recovery

show_backupfiles network path servername username

Where

• path represents the location of the backup files on the remote server.

• servername represents the IP address or host name of the server where you stored the backup files.

• username represents the username that is needed to log in to the remote server.

Note The system prompts you to enter the password for the account on the remote server.

Options

None

This command displays information about the backup files that are stored on a remote server.

Command privilege level: 1

Allowed during upgrade: Yes

utils disaster_ recovery

show_bakcupfiles tape tapeid

Where

tapeid represents the ID of an available tape device.

Options

None

This command displays information about the backup files that are stored on a tape.

Command privilege level: 1

Allowed during upgrade: Yes

utils disaster_ recovery

show_registration hostname

Where

hostname specifies the server for which you want to display registration information.

Options

None

This command displays the registered features and components on the specified server.

Command privilege level: 1

Allowed during upgrade: Yes

utils disaster_ recovery

show_tapeid

Options

None

This command displays a list of tape device IDs.

Command privilege level: 1

Allowed during upgrade: Yes

utils disaster_ recovery

status operation

Where

operation specifies the name of the ongoing operation: backup or restore .

Options

None

This command displays the status of the current backup or restore job.

Command privilege level: 1

Allowed during upgrade: Yes

utils netdump

client start ip-address-of-netdump-server

client status

client stop

Where

• client start starts the netdump client.

• client status displays the status of the netdump client.

• client stop stops the netdump client.

• ip-address-of-netdump-server specifies the IP address of the netdump server to which the client will send diagnostic information.

Options

None

This command configures the netdump client.

In the event of a kernel panic crash, the netdump client sends diagnostic information about the crash to a netdump server.

Command privilege level: 0

Allowed during upgrade: No

utils netdump

server add-client ip-address-of-netdump-client

server delete-client ip-address-of-netdump-client

server list-clients

server start

server status

server stop

Where

• server add-client adds a netdump client.

• server delete-client deletes a netdump client.

• server list-clients lists the clients that are registered with this netdump server.

• server start starts the netdump server.

• server status displays the status of the netdump server.

• server stop stops the netdump server.

• ip-address-of-netdump-client specifies the IP address of a netdump client.

Options

None

This command configures the netdump server.

In the event of a kernel panic crash, a netdump-enabled client system sends diagnostic information about the crash to the netdump server.

netdump diagnostic information is stored in the following location on the netdump server: /var/log/active/crash/. The subdirectories whose names consist of a client IP address and a date contain netdump information.

You can configure each Cisco Unified Communications Operating System server as both a netdump client and server.

If the server is on another Cisco Unified Communications Operating System server, only the kernel panic trace signature is sent to the server; otherwise, an entire core dump gets sent.

Command privilege level: 0

Allowed during upgrade: No

utils network

arp list [ host host ][ page ][ numeric ]

arp set { host } { address }

arp delete host

Where

• arp list lists the contents of the address resolution protocol table.

• arp set sets an entry in the address resolution protocol table.

• arp delete deletes an entry in the address resolution table.

• host represents the host name or IP address of the host to add or delete to the table.

• address represents the MAC address of the host to be added. Enter the MAC address in the following format: XX:XX:XX:XX:XX:XX.

Options

page —Displays the output one page at a time

numeric —Displays hosts as dotted IP addresses

This command lists, sets, or deletes Address Resolution Protocol (ARP) table entries.

Command privilege level: 0

Allowed during upgrade: Yes

utils network

capture eth0 [ page ] [ numeric ] [ file fname ] [ count num ] [ size bytes ] [ src addr ] [ dest addr ] [ port num ]

Where

eth0 specifies Ethernet interface 0.

Options

• page —Displays the output one page at a time

Note When you use the page or file options, the complete capture of all requested packets must occur before the command completes.

• numeric —Displays hosts as dotted IP addresses

• file fname —Outputs the information to a file

Note The file option saves the information to platform/cli/ fname .cap. The filename cannot contain the "." character.

count num —Sets a count of the number of packets to capture

Note For screen output, the maximum count equals 1000, and, for file output, the maximum count equals 10,000.

• size bytes —Sets the number of bytes of the packet to capture

Note For screen output, the maximum number of bytes equals 128, for file output, the maximum of bytes can be any number or ALL

• src addr —Specifies the source address of the packet as a host name or IPV4 address

• dest addr —Specifies the destination address of the packet as a host name or IPV4 address

• port num —Specifies the port number of the packet, either source or destination

This command captures IP packets on the specified Ethernet interface. You can display the packets on the screen or save them to a file. Line wrapping can occur in the output.

Command privilege level: 0

Allowed during upgrade: Yes

utils network

host hostname [ server server-name ] [ page ] [ detail ] [ srv]

Where

hostname represents the host name or IP address that you want to resolve.

Options

server-name —Specifies an alternate domain name server

page —Displays the output one screen at a time

detail —Displays a detailed listing

srv —Displays DNS SRV records.

This command resolves a host name to an address or an address to a host name.

Command privilege level: 0

Allowed during upgrade: Yes

utils network

ping destination [ count ]

Where

destination represents the hostname or IP address of the server that you want to ping.

Options

count —Specifies the number of times to ping the external server. The default count equals 4.

This command allows you to ping another server.

Command privilege level: 0

Allowed during upgrade: Yes

utils network

tracert destination

Where

destination represents the hostname or IP address of the server to which you want to send a trace.

Options

None

This command traces IP packets that are sent to a remote destination.

Command privilege level: 0

Allowed during upgrade: Yes

utils ntp

{ status | config }

This command displays the NTP status or configuration.

Command privilege level: 0

Allowed during upgrade: Yes

utils remote_ account

status

enable

disable

create username life

Where

username specifies the name of the remote account. The username can contain only lowercase characters and must be more than six-characters long.

life specifies the life of the account in days. After the specified number of day, the account expires.

Note You can have only one remote account that is enabled at a time.

Options

None

This command allows you to enable, disable, create, and check the status of a remote account.

Note A remote account generates a pass phrase that allows Cisco Systems support personnel to get access to the system for the specified life of the account.

Command privilege level: 1

Allowed during upgrade: Yes

Example

```
utils remote_account status
```

utils service

list [ page ]

Options

page —Displays the output one page at a time

This command retrieves a list of all services and their status.

Command privilege level: 0

Allowed during upgrade: Yes

utils service

start service-name

stop service-name

restart service-name

Where

service-name represents the name of the service that you want to stop or start the following services:

• System NTP

• System SSH

• Service Manager

• A Cisco DB

• Cisco Tomcat

• Cisco Database Layer Monitor

• Cisco Unified CallManager Serviceability

Options

None

This command stops, starts, or restarts a service.

Command privilege level: 1

Allowed during upgrade: No

utils snmp

test

Options

None

This commands tests the SNMP host by sending sample alarms to local syslog, remote syslog, and SNMP trap.

Command privilege level: 0

Allowed during upgrade: No

utils soap

realtimeservice test remote-ip remote-https-user remote-https-password

Where

• remote-ip specifies the IP address of the server under test.

• remote-https-user specifies a username with access to the SOAP API.

• remote-https-password specifies the password for the account with SOAP API access.

Options

None

This command executes a number of test cases on the remote server.

Command privilege level: 0

Allowed during upgrade: N

utils system

{ restart | shutdown | switch-version }

Note The system prompts you to confirm the action that you choose.

The utils system shutdown command has a 5-minute timeout. If the system does not shut down within 5 minutes, the command gives you the option of doing a forced shutdown.

This command allows you to restart the system on the same partition, restart the system on the inactive partition, or shut down the system.

Command privilege level: 1

Allowed during upgrade: No

### Run Commands

The following table lists and explains the CLI Run commands:

Table A-7 Run Commands

run sql

sql_statement

Where

sql_statement represents the SQL command to run.

Options

None

This command allows you to run an SQL command.

Command privilege level: 1

Allowed during upgrade: No

Example: Run an SQL command

```
run sql select name from device
```

| Command | Parameters and Options | Description |
|---|---|---|
| file check | [ detection-size-kb ] Where detection-size-kb specifies the minimum file size change that is required for the command to display the file as changed. Default minimum size: 100 KB The command notifies you about a possible impact to system performance and asks you whether you want to continue. Warning Because running this command can affect system performance, Cisco recommends that you run the command during off-peak hours. Options None | This command checks the /usr directory tree to see whether any files or directories have been added, removed, or changed in size since the last fresh installation or upgrade and displays the results. The display includes both deleted and new files. Command privilege level: 0 Allowed during upgrade: No |
| file delete | activelog directory/filename [ detail ] [ noconfirm ] inactivelog directory/filename [ detail ] [ noconfirm ] install directory/filename [ detail ] [ noconfirm ] tftp directory/filename [ detail ] Where • activelog specifies a log on the active side. • inactivelog specifies a log on the inactive side. • install specifies an installation log. • tftp specifies a TFTP file. You can use the wildcard character, *, for filename . Caution You cannot recover a deleted file except, possibly, by using the Disaster Recovery System. If you delete a TFTP data file on the inactive side, you may need to manually restore that file if you switch versions to the inactive side. Options • detail —Displays a listing of deleted files with the date and time. • noconfirm —Deletes files without asking you to confirm each deletion. | This command deletes one or more files. Command privilege level: 1 Allowed during upgrade: Yes Example: Delete the install log file delete install install.log |
| file dump | activelog directory/filename [detail] [hex ] inactivelog directory/filename [detail] [hex ] install directory/filename [detail] [hex ] tftp directory/filename [detail] [hex ] Where • activelog specifies a log on the active side. • inactivelog specifies a log on the inactive side. • install specifies an installation log. • tftp specifies a TFTP file. You can use the wildcard character, *, for filename as long as it resolves to one file. Options • detail —Displays listing with the date and time. • hex —Displays output in hexadecimal. | This command dumps the contents of a file to the screen, a page at a time. Command privilege level: 1 for logs, 0 for TFTP files Allowed during upgrade: Yes Example: Dump contents of file _cdrIndex.idx file dump activelog 
cm/cdr/_cdrIndex.idx |
| file get | activelog directory/filename [ reltime ] [ abstime ] [ match ] [ recurs ] inactivelog directory/filename [ reltime ] [ abstime ] [ match ] [ recurs ] install directory/filename [ reltime ] [ abstime ] [ match ] [ recurs ] tftp directory/filename [ reltime ] [ abstime ] [ match ] [ recurs ] Where • activelog specifies a log on the active side. • inactivelog specifies a log on the inactive side. • install specifies an installation log. • tftp specifies a TFTP file. Options • abstime —Absolute time period, specified as hh:mm:MM/DD/YY hh:mm:MM/DD/YY • reltime —Relative time period, specified as minutes \| hours \| days \| weeks \| months <value> • match —Match a particular string in the filename, specified as <string value> • recurs —Get all files, including subdirectories After the command identifies the specified files, you get prompted to enter an SFTP host, username, and password. | This command sends the file to another system by using SFTP. Command privilege level: 0 Allowed during upgrade: Yes Example 1: Get all files in the activelog operating system directory that match the string "plat" file get activelog platform match plat Example 2: Get all operating system log files for a particular time period file get activelog platform/log abstime 
18:00:9/27/200 18:00:9/28/2005 |
| file list | activelog directory [ page] [detail] [reverse] [ date \| size ] inactivelog directory [ page] [detail] [reverse] [ date \| size ] install directory [ page] [detail] [reverse] [ date \| size ] tftp directory [ page] [detail] [reverse] [ date \| size ] Where • activelog specifies a log on the active side. • inactivelog specifies a log on the inactive side. • install specifies an installation log. • tftp specifies a TFTP file. Note You can use a wildcard character, *, for directory name as long as it resolves to one directory. Options • detail —Long listing with date and time • date —Sort by date • size —Sort by file size • reverse —Reverse sort direction • page —Displays the output one screen at a time | This command lists the log files in an available log directory. Command privilege level: 1 for logs, 0 for TFTP files Allowed during upgrade: Yes Example 1: List Operating System Log files with details file list activelog platform/log page 
detail Example 2: List directories in CDR Repository file list activelog cm/cdr_repository Example 3: List CDR files in a specified directory by size file list activelog 
cm/cdr_repository/processed/20050812 
size |
| file search | activelog directory/filename reg-exp [abstime hh : mm : ss mm / dd / yyyy hh : mm : ss mm / dd / yyyy ] [ ignorecase ] [reltime { days\|hours\|minutes} timevalue ] inactivelog directory/filename reg-exp [abstime hh : mm : ss mm / dd / yyyy hh : mm : ss mm / dd / yyyy ] [ ignorecase ] [reltime { days\|hours\|minutes} timevalue ] install directory/filename reg-exp [abstime hh : mm : ss mm / dd / yyyy hh : mm : ss mm / dd / yyyy ] [ ignorecase ] [reltime { days\|hours\|minutes} timevalue ] tftp directory/filename reg-exp [abstime hh : mm : ss mm / dd / yyyy hh : mm : ss mm / dd / yyyy ] [ ignorecase] [reltime { days\|hours\|minutes} timevalue ] Where • activelog specifies a log on the active side. • inactivelog specifies a log on the inactive side. • install specifies an installation log. • tftp specifies a TFTP file. • reg-exp represents a regular expression. Note You can use the wildcard character, *, to represent all or part of the filename. Options • abstime —Specifies which files to search based on file creation time. Enter a start time and an end time. • days\|hours\|minutes —Specifies whether the file age is in days, hours, or minutes. • ignorecase —Ignores case when searching • reltime —Specifies which files to search based on file creation time. Enter the age of files to search. • hh : mm : ss mm / dd / yyyy —An absolute time, in the format hours:minutes:seconds month/day/year. • timevalue —The age of files to search. The unit of this value is specified with the { days\|hours\|minutes} option. | This command searches the content of a log and displays the matching lines a page at a time. Write the search term in the form of a regular expression, which is a special text string for describing a search pattern. If the search term is found in only one file, the filename appears at the top of the output. If the search term is found in multiple files, each line of the output begins with the filename in which the matching line was found. Command privilege level: 0 Allowed during upgrade: Yes Example file search activelog 
platform/log/platform.log Err[a-z] 
ignorecase |
| file tail | activelog directory/filename [ detail] [hex] [lines ] inactivelog directory/filename [ detail] [hex] [lines ] install directory/filename [ detail] [hex] [lines ] tftp directory/filename [ detail] [hex] [lines ] Where • activelog specifies a log on the active side. • inactivelog specifies a log on the inactive side. • install specifies an installation log. • tftp specifies a TFTP file. You can use the wildcard character, *, for filename so long as it resolves to one file. Options • detail —Long listing with date and time • hex —Hexadecimal listing • lines —Number of lines to display | This command tails (prints the last few lines) of a log file. Command privilege level: 1 for logs, 0 for TFTP files Allowed during upgrade: Yes Example: Tail the operating system CLI log file file tail activelog 
platform/log/cli00001.log |
| file view | activelog directory/filename inactivelog directory/filename install directory/filename tftp directory/filename Where • activelog specifies a log on the active side. • inactivelog specifies a log on the inactive side. • install specifies an installation log. • tftp specifies a TFTP file. Note You can use the wildcard character, *, for filename so long as it resolves to one file. Caution Do not use this command to view binary files because this can corrupt the terminal session. | This command displays the contents of a file. Command privilege level: 0 Allowed during upgrade: Yes Example 1: Display the install log file view install install.log Example 2: Display a particular CDR file file view activelog 
/cm/cdr_repository/processed/20058012/{
filename} |

| Command | Parameters and Options | Description |
|---|---|---|
| show account | None | This command lists current administrator accounts, except the master administrator account. Command privilege level: 4 Allowed during upgrade: Yes |
| show cert | own filename trust filename list {own \| trust} Where • filename represents the name of the certificate file. • own specifies owned certificates. • trust specifies trusted certificates. • list specifies a certificate trust list. Options None | This command displays certificate contents and certificate trust lists. Command privilege level: 1 Allowed during upgrade: Yes Example: Display own certificate trust lists show cert list own |
| show firewall | list [ detail ] [ page ] [ file filename ] Where • detail —Displays detailed statistics on every available device on the system • page —Displays the output one page at a time • file filename —Outputs the information to a file Note The file option saves the information to platform/cli/ filename .txt. The file name cannot contain the "." character. | This command displays system aspects of the server. Command privilege level: 1 Allowed during upgrade: Yes |
| show hardware | None | This command displays the following information on the platform hardware: • Platform • Serial number • BIOS build level • BIOS manufacturer • Active processors • RAID controller status Command privilege level: 0 Allowed during upgrade: Yes |
| show ipsec | policy association policy information policy association Where • policy displays all IPSec policies on the node. • association displays the association list and status for the policy. • information displays the association details and status for the policy. • policy represents the name of a specific IPSec policy. • association represents the association name. Options None | This command displays information on IPSec policies and associations. Command privilege level: 1 Allowed during upgrade: yes Example: Display IPSec policies show ipsec policy |
| show myself | None | This command displays information about the current account. Command privilege level: 0 Allowed during upgrade: Yes |
| show network | eth0 [ detail ] failover [ detail ] [ page ] route [ detail ] status [ detail ] [ listen ] [ process] [ all ] [ nodns ] [ search stext ] all [ detail ] Where • eth0 specifies Ethernet 0. • failover specifies Network Fault Tolerance information. • route specifies network routing information. • status specifies active Internet connections. • all specifies all basic network information. Options • detail —Displays additional information • page —Displays information 1 page at a time. • listen —Displays only listening sockets • process —Displays the process ID and name of the program to which each socket belongs • all —Displays both listening and nonlistening sockets • nodns —Displays numerical addresses without any DNS information • search stext —Searches for the stext in the output | This command displays network information. The eth0 parameter Ethernet port 0 settings, including DHCP and DNS configurations. Command privilege level: 0 Allowed during upgrade: Yes Example: Display active Internet connections show network status |
| show packages | active name [ page ] inactive name [ page ] Where name represents the package name. To display all active or inactive packages, use the wildcard character, *. Options page —Displays the output one page at a time | This command displays the name and version for installed packages. Command privilege level: 0 Allowed during upgrade: Yes |
| show perf | counterhelp class-name counter-name Where • class-name represents the class name that contains the counter. • counter-name represents the counter that you want to view. Note If the class name or counter name contains white spaces, enclose the name in double quotation marks. Options None | This command displays the explanation text for the specified perfmon counter. Command privilege level: 0 Allowed during upgrade: Yes |
| show perf | list categories Options None | This command lists all categories in the perfmon system. Command privilege level: 0 Allowed during upgrade: Yes |
| show perf | list classes [ -t category ] [ -d ] Options • -d —Displays detailed information • -t category —Displays perfmon classes for the specified category | This commands lists the perfmon classes or objects. Command privilege level: 0 Allowed during upgrade: Yes |
| show perf | list counters class-name [ -d ] Where class-name represents a perfmon class name for which you want to list the counters. Note If the class name contains white spaces, enclose the name in double quotation marks. Options -d —Displays detailed information | This command lists perfmon counters for the specified perfmon class. Command privilege level: 0 Allowed during upgrade: Yes |
| show perf | list instances class-name [ -d ] Where class-name represents a perfmon class name for which you want to list the counters. Note If the class name contains white spaces, enclose the name in double quotation marks. Options -d —Displays detailed information | The command lists the perfmon instances for the specified perfmon class. Command privilege level: 0 Allowed during upgrade: Yes |
| show perf | query class class-name [, class-name ...] Where class-name specifies the perfmon class that you want to query. You can specify a maximum of 5 classes per command. Note If the class name contains white spaces, enclose the name in double quotation marks. Options None | This command queries a perfmon class and displays all the instances and counter values of each instance. Command privilege level: 0 Allowed during upgrade: Yes |
| show perf | query counter class-name counter-name [, counter-name ...] Where • class-name specifies the perfmon class that you want to query. • counter-name specifies the counter to view. You can specify a maximum of 5 counters per command. Note If the class name or counter name contains white spaces, enclose the name in double quotation marks. Options None | This command queries the specified counter and displays the counter value of all instances. Command privilege level: 0 Allowed during upgrade: Yes |
| show perf | query instance class-name instance-name [, instance-name ...] Where • class-name specifies the perfmon class that you want to query. • instance-name specifies the perfmon instance to view. You can specify a maximum of 5 instances per command. Note If the class name or instance name contains white spaces, enclose the name in double quotation marks. Options None | This command queries the specified instance and displays all its counter values. Note This command does not apply to singleton perfmon classes. Command privilege level: 0 Allowed during upgrade: Yes |
| show perf | query path path-spec [, path-spec ...] Where path-spec gets defined as follows: • For an instance-based perfmon class, specify path-spec as class-name ( instance-name )\ counter-name . • For a noninstance-based perfmon class (a singleton), specify path-spec as class-name \ counter-name . You can specify a maximum of 5 paths per command. Note If the path name contains white spaces, enclose the name in double quotation marks. Options None | This command queries a specified perfmon path. Command privilege level: 0 Allowed during upgrade: Yes Example show perf query path "Cisco 
Phones(phone-0)\CallsAttempted", 
"Cisco Unified CallManager\T1Channel
sActive" |
| show process | load [ cont ] [ clear ] [ noidle ] [ num xx ] [ thread ] [ cpu ] [ memory ] [ time ] [ specified ] [ page ] list [ page ] [ short ] [ detail ] [ thread] [ fd ] [ cont ] [ clear ] [ process id id ] [ argument id id ] [ owner name name ] Where • load displays the CPU load for each active process. • list displays all processes. Options • cont —Command repeats continuously • clear —Clears screen before displaying output • noidle —Ignore idle or zombie processes • num xx —Sets the number of processes to display (Default=10, all = all processes) • thread —Displays threads • cpu —Displays output by CPU usage • memory —Sorts output by memory usage • short—Displays short listing • time —Sorts output by time usage • page —Displays one page at a time • detail —Displays a detailed listing • process id id —Shows only specific process number or command name • argument name name —Show only specific process with argument name • thread —Include thread processes in the listing • fd —Show file descriptors that are associated with a process | This command displays process and load information. Command privilege level: 1 Allowed during upgrade: Yes Example: Show detailed process listing one page at a time show process list detail page |
| show registry | system component [ name ] [page] Where • system represents the registry system name. • component represents the registry component name. • name represents the name of the parameter to show. Note To display all items, enter the wildcard character, *. Display Options page —Displays one page at a time | This command displays the contents of the registry. Command privilege level: 1 Allowed during upgrade: Yes Example: show contents of the cm system, dbl/sdi component show registry cm dbl/sdi |
| show risdb | list [ file filename ] query table1 table2 table3 ... [ file filename ] Where • list displays the tables supported in the Realtime Information Service (RIS) database. • query displays the contents of the RIS tables. Options file filename —Outputs the information to a file Note The file option saves the information to platform/cli/ filename .txt. The file name cannot contain the "." character. | This command displays RIS database table information. Command privilege level: 0 Allowed during upgrade: Yes Example: Display list of RIS database tables show risdb list |
| show smtp | None | This command displays the name of the SMTP host. Command privilege level: 0 Allowed during upgrade: Yes |
| show stats | io [ kilo ] [ detail ] [ page ] [ file filename ] Options • kilo —Displays statistics in kilobytes • detail —Displays detailed statistics on every available device on the system and overrides the kilo option • file filename —Outputs the information to a file Note The file option saves the information to platform/cli/ filename .txt. The file name cannot contain the "." character. | This command displays system IO statistics. Command privilege level: 1 Allowed during upgrade: Yes |
| show status | None | This command displays the following basic platform status: • Host name • Date • Time zone • Locale • Product version • Platform version • CPU usage • Memory and disk usage Command privilege level: 0 |
| show tech | all [ page ] [ file filename ] Options • page —Displays one page at a time • file filename —Outputs the information to a file Note The file option saves the information to platform/cli/ filename .txt. The file name cannot contain the "." character. | This command displays the combined output of all show tech commands. Command privilege level: 1 Allowed during upgrade: Yes |
| show tech | ccm_service Options None | This command displays information on all Cisco Unified CallManager services that can run on the system. Command privilege level: 0 Allowed during upgrade: Yes |
| show tech | database Options None | This command creates a CSV file of the entire database. Command privilege level: 1 Allowed during upgrade: Yes |
| show tech | dbinuse Options None | This command displays the database in use. Command privilege level: 1 Allowed during upgrade: Yes |
| show tech | dbschema Options None | This command displays the database schema in a CSV file. Command privilege level: 1 Allowed during upgrade: Yes |
| show tech | devdefaults Options None | This command displays the device defaults table. Command privilege level: 1 Allowed during upgrade: Yes |
| show tech | gateway Options None | This command displays the gateway table from the database. Command privilege level: 1 Allowed during upgrade: Yes |
| show tech | locales Options None | This command displays the locale information for devices, device pools, and end users. Command privilege level: 1 Allowed during upgrade: Yes |
| show tech | network [ page ] [ file filename ] Options • page —Displays one page at a time • file filename —Outputs the information to a file Note The file option saves the information to platform/cli/ filename .txt. The file name cannot contain the "." character. | This command displays network aspects of the server. Command privilege level: 1 Allowed during upgrade: Yes |
| show tech | notify Options None | This command displays the database change notify monitor. Command privilege level: 1 Allowed during upgrade: Yes |
| show tech | params all Options None | This command displays all the database parameters. Command privilege level: 1 Allowed during upgrade: Yes |
| show tech | params enterprise Options None | This command displays the database enterprise parameters. Command privilege level: 1 Allowed during upgrade: Yes |
| show tech | params service Options None | This command displays the database service parameters. Command privilege level: 1 Allowed during upgrade: Yes |
| show tech | procedures Options None | This command displays the procedures in use for the database. Command privilege level: 1 Allowed during upgrade: Yes |
| show tech | routepatterns Options None | This command displays the route patterns that are configured for the system. Command privilege level: 1 Allowed during upgrade: Yes |
| show tech | routeplan Options None | This command displays the route plan that are configured for the system. Command privilege level: 1 Allowed during upgrade: Yes |
| show tech | runtime [ page ] [ file filename ] Options page —Displays one page at a time file filename —Outputs the information to a file Note The file option saves the information to platform/cli/ filename .txt. The file name cannot contain the "." character. | This command displays runtime aspects of the server. Command privilege level: 1 Allowed during upgrade: Yes |
| show tech | systables Options None | This command displays the name of all tables in the sysmaster database. Command privilege level: 1 Allowed during upgrade: Yes |
| show tech | system [ page ] [ file filename ] Options page —Displays one page at a time file filename —Outputs the information to a file Note The file option saves the information to platform/cli/ filename .txt. The file name cannot contain the "." character. | This command displays system aspects of the server. Command privilege level: 1 Allowed during upgrade: Yes |
| show tech | table table_name [ page ] [ csv ] Where table_name represents the name of the table to display. Options page —Displays the output one page at a time csv —Sends the output to a comma separated values file | This command displays the contents of the specified database table. Command privilege level: 1 Allowed during upgrade: Yes |
| show tech | triggers Options None | This command displays table names and the triggers that are associated with those tables. Command privilege level: 1 Allowed during upgrade: Yes |
| show tech | version [page] Options Page—Displays the output one page at a time | This command displays the version of the installed components. Command privilege level: 1 Allowed during upgrade: Yes |
| show timezone | config list [ page ] Where • config displays the current time zone settings. • list displays the available time zones. Options page —Displays the output one page at a time | This command displays time zone information. Command privilege level: 0 Allowed during upgrade: Yes |
| show trace | [ task_name ] Where task_name represents the name of the task for which you want to display the trace information. Note If you do not enter any parameters, the command returns a list of available tasks. Options None | This command displays trace information for a particular task. Command privilege level: 0 Allowed during upgrade: Yes Example: Display trace information for cdp show trace cdps |
| show version | active inactive Options None | This command displays the software version on the active or inactive partition. Command privilege level: 0 Allowed during upgrade: Yes |
| show web-security | None | This command displays the contents of the current web-security certificate. Command privilege level: 0 Allowed during upgrade: Yes |
| show workingdir | None | This command retrieves the current working directory for activelog, inactivelog, install, and TFTP. Command privilege level: 0 Allowed during upgrade: Yes |

| Command | Parameters | Description |
|---|---|---|
| set account | name Where name represents the username for the new account. Note After you enter the username, the system prompts you to enter the privilege level and password for the new account. Options None | This command sets up a new account on the operating system. Command privilege level: 0 Allowed during upgrade: No |
| set cert | regen unit-name Where unit-name represents the name of the certificate that you want to regenerate. Options None | This command enables you to regenerate the specified security certificate. Command privilege level: 1 Allowed during upgrade: No |
| set ipsec | policy { ALL \| policy-name } association policy-name { ALL \| association-name } Where • policy-name represents an IPSec policy. • association-name represents an IPSec association. Options None | This command allows you to set IPSec policies and associations. Command privilege level: 1 Allowed during upgrade: No |
| set logging | { enable \| disable } Options None | This command allows you to enable or disable logging. Command privilege level: 0 Allowed during upgrade: Yes |
| set network | dhcp eth0 { enable \| disable } Where • eth0 specifies Ethernet interface 0. The system asks whether you want to continue to execute this command. Warning If you continue, this command causes the system to restart. Cisco also recommends that you restart all nodes whenever any IP address gets changed. Options None | This command enables or disables DHCP for Ethernet interface 0. Command privilege level: 1 Allowed during upgrade: No |
| set network | dns { primary \| secondary } ip-address Where ip-address represents the IP address of the primary or secondary DNS server. The system asks whether you want to continue to execute this command. Warning If you continue, this command causes a temporary loss of network connectivity. Options None | This command sets the IP address for the primary or secondary DNS server. Command privilege level: 1 Allowed during upgrade: No |
| set network | dns options [ timeout seconds ] [ attempts number ] [ rotate ] Where • timeout sets the DNS request timeout. • attempts sets the number of times to attempt a DNS request before quitting. • rotate causes the system to rotate among the configured DNS servers, distributing the load. • seconds specifies the DNS timeout period, in seconds. • number specifies the number of attempts. Options None | This command sets DNS options. Command privilege level: 0 Allowed during upgrade: Yes |
| set network | domain domain-name Where domain-name represents the system domain that you want to assign. The system asks whether you want to continue to execute this command. Warning If you continue, this command causes a temporary loss of network connectivity. Options None | This command sets the domain name for the system. Command privilege level: 1 Allowed during upgrade: No |
| set network | failover { enable \| disable } Where • enable enables Network Fault Tolerance. • disable disables Network Fault Tolerance. Options None | This command enables and disables Network Fault Tolerance. Command privilege level: 1 Allowed during upgrade: No |
| set network | gateway ip-address Where ip-address represents the IP address of the network gateway that you want to assign. The system asks whether you want to continue to execute this command. Warning If you continue, this command causes the system to restart. Options None | This command enables you to configure the IP address of the network gateway. Command privilege level: 1 Allowed during upgrade: No |
| set network | ip eth0 ip-address ip-mask Where • eth0 specifies Ethernet interface 0. • ip-address represents the IP address that you want assign. • ip-mask represents the IP mask that you want to assign. The system asks whether you want to continue to execute this command. Warning If you continue, this command causes the system to restart. Options None | This command sets the IP address for Ethernet interface 0. Command privilege level: 1 Allowed during upgrade: No |
| set network | nic eth0 [ auto en \| dis ] [ speed 10 \| 100 ] [ duplex half \| full ] Where • eth0 specifies Ethernet interface 0. • auto specifies whether auto negotiation gets enabled or disabled. • speed specifies whether the speed of the Ethernet connection: 10 or 100 Mbps. • duplex specifies half-duplex or full-duplex. The system asks whether you want to continue to execute this command. Note You can enable only one active NIC at a time. Warning If you continue, this command causes a temporary loss of network connections while the NIC gets reset. Options None | This command sets the properties of the Network Interface Card (NIC). Command privilege level: 1 Allowed during upgrade: No |
| set network | status eth0 { up \| down } Where eth0 specifies Ethernet interface 0. Options None | This command sets the status of Ethernet 0 to up or down. Command privilege level: 1 Allowed during upgrade: No |
| set output | { enable \| disable } Options None | This command allows you to enable or disable the operating system output. Command privilege level: 0 Allowed during upgrade: Yes |
| set password | { admin \| security } The systems prompts you for the old and new passwords. Note The password must contain at least six characters, and the system checks it for strength. | This command allows you to change the administrator and security passwords. Command privilege level: 1 Allowed during upgrade: No |
| set smtp | hostname Where hostname represents the SMTP server name. Options None | This command sets the SMTP server hostname. Command privilege level: 0 Allowed during upgrade: No |
| set timezone | timezone Note Enter enough characters to uniquely identify the new time zone. Be aware that the time-zone name is case-sensitive. Caution You must restart the system after you change the time zone. Options None | This command lets you change the system time zone. Command privilege level: 0 Allowed during upgrade: No Example: Set the time zone to Pacific time set timezone Pac |
| set trace | enable Error tname enable Special tname enable State_Transition tname enable Significant tname enable Entry_exit tname enable Arbitrary tname enable Detailed tname disable tname Where • tname represents the task for which you want to enable or disable traces. • enable Error sets task trace settings to the error level. • enable Special sets task trace settings to the special level. • enable State_Transition sets task trace settings to the state transition level. • enable Significant sets task trace settings to the significant level. • enable Entry_exit sets task trace settings to the entry_exit level. • enable Arbitrary sets task trace settings to the arbitrary level. • enable Detailed sets task trace settings to the detailed level. • disable unsets the task trace settings. Options None | This command sets trace activity for the the specified task. Command privilege level: 1 Allowed during upgrade: No |
| set web-security | orgunit orgname locality state country Where • orgunit represents the organizational unit. • orgname represents the organizational name. • locality represents the organization's location. • state represents the organization's state. • country represents the organization's country. Options None | This command sets the web security certificate information for the operating system. Command privilege level: 0 Allowed during upgrade: No |
| set workingdir | activelog directory inactivelog directory install directory tftp directory Where • activelog sets the working directory for active logs. • inactivelog set the working directory for inactive logs. • install sets the working directory for installation logs. • tftp sets the working directory for TFTP files. • directory represents the current working directory. Options None | This command sets the working directory for active, inactive, and installation logs. Command privilege level: 0 for logs, 1 for TFTP Allowed during upgrade: Yes |

| Command | Parameters | Description |
|---|---|---|
| unset ipsec | policy { ALL \| policy-name } association policy-name { ALL \| association-name } Where • policy-name represents the name of an IPSec policy. • association-name represents the name of an IPSec association. Options None | This command allows you to disable IPSec policies and associations. Command privilege level: 1 Allowed during upgrade: No |

| Command | Parameters | Description |
|---|---|---|
| delete account | account-name Where account-name represents the name of an administrator account. Options None | This command allows you to delete an administrator account. Command privilege level: 4 Allowed during upgrade: No |
| delete dns | ip-address Where ip-address represents the IP address of the DNS server you want to delete. The system asks whether you want to continue to execute this command. Warning If you continue, this command causes a temporary loss of network connectivity. Options None | This command allows you to delete the IP address for a DNS server. Command privilege level: 1 Allowed during upgrade: No |
| delete ipsec | policy { ALL \| policy-name } association policy name { ALL \| association-name } Where • policy-name represents an IPSec policy. • association-name represents an IPSec association. Options None | This command allows you to delete IPSec policies and associations. Command privilege level: 1 Allowed during upgrade: No |
| delete process | process-id [ force \| terminate \| crash ] Where • process-id represents the process ID number. Options • force— Tells the process to stop • terminate —Tells the operating system to terminate the process • crash —Crashes the process and produces a crash dump Note Use the force option only if the command alone does not delete the process and use the terminate option only if force does not delete the process. | This command allows you to delete a particular process. Command privilege level: 1 Allowed during upgrade: Yes |
| delete smtp | None | This command allows you to delete the SMTP host. Command privilege level: 1 Allowed during upgrade: No |

| Command | Parameters | Description |
|---|---|---|
| utils csa | disable The system disables CSA. Options None | This command stops Cisco Security Agent (CSA). Command privilege level: 1 Allowed during upgrade: No |
| utils csa | enable The system prompts you to confirm that you want to enable CSA. Caution You must restart the system after you start CSA. Options None | This command enables Cisco Security Agent (CSA). Command privilege level: 1 Allowed during upgrade: No |
| utils csa | status The system indicates whether CSA is running or not. Options None | This command displays the current status of Cisco Security Agent (CSA). Command privilege level: 0 Allowed during upgrade: No |
| utils disaster_ recovery | backup tape tapeid Where tapeid represents the ID of an available tape device. Options None | This command starts a backup job and stores the resulting tar file on tape. Command privilege level: 1 Allowed during upgrade: No |
| utils disaster_ recovery | backup network path servername username Where • path represents the location of the backup files on the remote server. • servername represents the IP address or host name of the server where you stored the backup files. • username represents the username that is needed to log in to the remote server. Note The system prompts you to enter the password for the account on the remote server. Options None | This command starts a backup job and stores the resulting tar file on a remote server. Command privilege level: 1 Allowed during upgrade: No |
| utils disaster_ recovery | cancel_bakckup The system prompts you to confirm that you want to cancel the backup job. Options None | This command cancels the ongoing backup job. Command privilege level: 1 Allowed during upgrade: No |
| utils disaster_ recovery | restore tape server tarfilename tapeid Where • server specifies the hostname of the server that you want to restore. • tarfilename specifies the name of the file to restore. • tapeid specifies the name of the tape device from which to perform the restore job. Options None | This command starts a restore job and takes the backup tar file from tape. Command privilege level: 1 Allowed during upgrade: No |
| utils disaster_ recovery | restore network restore_server tarfilename path servername username Where • restore_server specifies the hostname of the server that you want to restore. • tarfilename specifies the name of the file to restore. • path represents the location of the backup files on the remote server. • servername represents the IP address or host name of the server where you stored the backup files. • username represents the username that is needed to log in to the remote server. Note The system prompts you to enter the password for the account on the remote server. Options None | This command starts a restore job and takes the backup tar file from a remote server. Command privilege level: 1 Allowed during upgrade: No |
| utils disaster_ recovery | show_backupfiles network path servername username Where • path represents the location of the backup files on the remote server. • servername represents the IP address or host name of the server where you stored the backup files. • username represents the username that is needed to log in to the remote server. Note The system prompts you to enter the password for the account on the remote server. Options None | This command displays information about the backup files that are stored on a remote server. Command privilege level: 1 Allowed during upgrade: Yes |
| utils disaster_ recovery | show_bakcupfiles tape tapeid Where tapeid represents the ID of an available tape device. Options None | This command displays information about the backup files that are stored on a tape. Command privilege level: 1 Allowed during upgrade: Yes |
| utils disaster_ recovery | show_registration hostname Where hostname specifies the server for which you want to display registration information. Options None | This command displays the registered features and components on the specified server. Command privilege level: 1 Allowed during upgrade: Yes |
| utils disaster_ recovery | show_tapeid Options None | This command displays a list of tape device IDs. Command privilege level: 1 Allowed during upgrade: Yes |
| utils disaster_ recovery | status operation Where operation specifies the name of the ongoing operation: backup or restore . Options None | This command displays the status of the current backup or restore job. Command privilege level: 1 Allowed during upgrade: Yes |
| utils netdump | client start ip-address-of-netdump-server client status client stop Where • client start starts the netdump client. • client status displays the status of the netdump client. • client stop stops the netdump client. • ip-address-of-netdump-server specifies the IP address of the netdump server to which the client will send diagnostic information. Options None | This command configures the netdump client. In the event of a kernel panic crash, the netdump client sends diagnostic information about the crash to a netdump server. Command privilege level: 0 Allowed during upgrade: No |
| utils netdump | server add-client ip-address-of-netdump-client server delete-client ip-address-of-netdump-client server list-clients server start server status server stop Where • server add-client adds a netdump client. • server delete-client deletes a netdump client. • server list-clients lists the clients that are registered with this netdump server. • server start starts the netdump server. • server status displays the status of the netdump server. • server stop stops the netdump server. • ip-address-of-netdump-client specifies the IP address of a netdump client. Options None | This command configures the netdump server. In the event of a kernel panic crash, a netdump-enabled client system sends diagnostic information about the crash to the netdump server. netdump diagnostic information is stored in the following location on the netdump server: /var/log/active/crash/. The subdirectories whose names consist of a client IP address and a date contain netdump information. You can configure each Cisco Unified Communications Operating System server as both a netdump client and server. If the server is on another Cisco Unified Communications Operating System server, only the kernel panic trace signature is sent to the server; otherwise, an entire core dump gets sent. Command privilege level: 0 Allowed during upgrade: No |
| utils network | arp list [ host host ][ page ][ numeric ] arp set { host } { address } arp delete host Where • arp list lists the contents of the address resolution protocol table. • arp set sets an entry in the address resolution protocol table. • arp delete deletes an entry in the address resolution table. • host represents the host name or IP address of the host to add or delete to the table. • address represents the MAC address of the host to be added. Enter the MAC address in the following format: XX:XX:XX:XX:XX:XX. Options page —Displays the output one page at a time numeric —Displays hosts as dotted IP addresses | This command lists, sets, or deletes Address Resolution Protocol (ARP) table entries. Command privilege level: 0 Allowed during upgrade: Yes |
| utils network | capture eth0 [ page ] [ numeric ] [ file fname ] [ count num ] [ size bytes ] [ src addr ] [ dest addr ] [ port num ] Where eth0 specifies Ethernet interface 0. Options • page —Displays the output one page at a time Note When you use the page or file options, the complete capture of all requested packets must occur before the command completes. • numeric —Displays hosts as dotted IP addresses • file fname —Outputs the information to a file Note The file option saves the information to platform/cli/ fname .cap. The filename cannot contain the "." character. count num —Sets a count of the number of packets to capture Note For screen output, the maximum count equals 1000, and, for file output, the maximum count equals 10,000. • size bytes —Sets the number of bytes of the packet to capture Note For screen output, the maximum number of bytes equals 128, for file output, the maximum of bytes can be any number or ALL • src addr —Specifies the source address of the packet as a host name or IPV4 address • dest addr —Specifies the destination address of the packet as a host name or IPV4 address • port num —Specifies the port number of the packet, either source or destination | This command captures IP packets on the specified Ethernet interface. You can display the packets on the screen or save them to a file. Line wrapping can occur in the output. Command privilege level: 0 Allowed during upgrade: Yes |
| utils network | host hostname [ server server-name ] [ page ] [ detail ] [ srv] Where hostname represents the host name or IP address that you want to resolve. Options server-name —Specifies an alternate domain name server page —Displays the output one screen at a time detail —Displays a detailed listing srv —Displays DNS SRV records. | This command resolves a host name to an address or an address to a host name. Command privilege level: 0 Allowed during upgrade: Yes |
| utils network | ping destination [ count ] Where destination represents the hostname or IP address of the server that you want to ping. Options count —Specifies the number of times to ping the external server. The default count equals 4. | This command allows you to ping another server. Command privilege level: 0 Allowed during upgrade: Yes |
| utils network | tracert destination Where destination represents the hostname or IP address of the server to which you want to send a trace. Options None | This command traces IP packets that are sent to a remote destination. Command privilege level: 0 Allowed during upgrade: Yes |
| utils ntp | { status \| config } | This command displays the NTP status or configuration. Command privilege level: 0 Allowed during upgrade: Yes |
| utils remote_ account | status enable disable create username life Where username specifies the name of the remote account. The username can contain only lowercase characters and must be more than six-characters long. life specifies the life of the account in days. After the specified number of day, the account expires. Note You can have only one remote account that is enabled at a time. Options None | This command allows you to enable, disable, create, and check the status of a remote account. Note A remote account generates a pass phrase that allows Cisco Systems support personnel to get access to the system for the specified life of the account. Command privilege level: 1 Allowed during upgrade: Yes Example utils remote_account status |
| utils service | list [ page ] Options page —Displays the output one page at a time | This command retrieves a list of all services and their status. Command privilege level: 0 Allowed during upgrade: Yes |
| utils service | start service-name stop service-name restart service-name Where service-name represents the name of the service that you want to stop or start the following services: • System NTP • System SSH • Service Manager • A Cisco DB • Cisco Tomcat • Cisco Database Layer Monitor • Cisco Unified CallManager Serviceability Options None | This command stops, starts, or restarts a service. Command privilege level: 1 Allowed during upgrade: No |
| utils snmp | test Options None | This commands tests the SNMP host by sending sample alarms to local syslog, remote syslog, and SNMP trap. Command privilege level: 0 Allowed during upgrade: No |
| utils soap | realtimeservice test remote-ip remote-https-user remote-https-password Where • remote-ip specifies the IP address of the server under test. • remote-https-user specifies a username with access to the SOAP API. • remote-https-password specifies the password for the account with SOAP API access. Options None | This command executes a number of test cases on the remote server. Command privilege level: 0 Allowed during upgrade: N |
| utils system | { restart \| shutdown \| switch-version } Note The system prompts you to confirm the action that you choose. The utils system shutdown command has a 5-minute timeout. If the system does not shut down within 5 minutes, the command gives you the option of doing a forced shutdown. | This command allows you to restart the system on the same partition, restart the system on the inactive partition, or shut down the system. Command privilege level: 1 Allowed during upgrade: No |

| Command | Parameters | Description |
|---|---|---|
| run sql | sql_statement Where sql_statement represents the SQL command to run. Options None | This command allows you to run an SQL command. Command privilege level: 1 Allowed during upgrade: No Example: Run an SQL command run sql select name from device |