---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-15-0-maintain-and-operate-guide-uccx-a810d5f39e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_15_0/maintain_and_operate/guide/uccx_b_1501_admin-and-operations-guide/uccx_m_1501_command-line-interface.html
retrieved_at: 2026-08-16T21:29:16.718868+00:00
---

Cisco Unified Contact Center Express Administration and Operations Guide, Release 15.0

# Cisco Unified Contact Center Express Administration and Operations Guide, Release 15.0

Updated: April 30, 2025

Chapter: Command Line Interface

## Chapter: Command Line Interface

# Command Line Interface

## Command Line Interface Basics

### Start CLI
                           	 Session

Access the Cisco Unified Contact
                                    			 Center Express ( Unified CCX ) Command Line Interface (CLI) either
                                 		  remotely or locally using one of these two methods:

- From an SSH-enabled client
                                    			 workstation, use SSH to connect securely to the Unified
                                       				CCX .

- Access the Unified
                                       				CCX CLI
                                    			 directly or by using a terminal server that is connected to the serial port.
                                    			 Use this method if a problem exists with the IP address.

To start a CLI session:

Step 1

Perform one of
                                          			 the following tasks:

From a remote system, use SSH to connect securely to the Cisco CCX Platform. In your SSH client, enter

ssh adminname@hostname

where adminname specifies the platform administrator ID and hostname specifies the hostname that was entered during installation.

For example, ssh
                                                      						admin@ccx-1 .

From a
                                                   					 direct connection, you receive this prompt automatically:

```
ccx-1 login:
```

where ccx-1 represents the
                                                   					 hostname of the system.

Enter your
                                                   					 administrator ID.

In either
                                             				case, the system prompts you for a password.

Step 2

Enter
                                          			 password.

The CLI prompt
                                             				displays. The prompt represents the administrator ID, for example:

```
admin:
```

### Get Help with Commands

You can get two kinds of help for any command:

- Detailed help that
                                    			 includes a definition of the command and an example of its use.

- Short query help that
                                    			 includes only command syntax.

To get detailed help, at the CLI prompt, enter

help command

where command specifies the command name or the command and
                                 		  parameter.

Detailed Help Example:

```
admin:help file list activelog help: This will list active logging files options are: page - pause output detail - show detailed listing reverse - reverse sort order date - sort by date size - sort by size file-spec can contain '*' as wildcards
```

```
admin:file list activelog platform detail 02 Dec,2004 12:00:59 <dir> drf 02 Dec,2004 12:00:59 <dir> log 16 Nov,2004 21:45:43 8,557 enGui.log 27 Oct,2004 11:54:33 47,916 startup.log dir count = 2, file count = 2
```

If you enter the help command without specifying the name of a particular
                                             			 command as the optional parameter, the system provides information about the
                                             			 CLI system.

To query only command syntax, at the CLI prompt, enter

command ?

where command represents the command name or the command and
                                 		  parameter.

Query Example

```
admin:file list activelog?Syntax: file list activelog file-spec [options] file-spec mandatory file to view options optional page|detail|reverse|[date|size]
```

If you enter a ? after a menu command, such as set , it acts like the Tab key and lists the commands that are
                                             			 available.

### Exit Command with Ctrl-C Key Sequence

You can stop most interactive commands by entering the Ctrl-C key sequence.

```
admin:utils system upgrade initiate Warning: Do not close this window without first exiting the upgrade command. Source: 1) Remote Filesystem 2) DVD/CD q) quit Please select an option (1 - 2 or "q"): Exiting upgrade command. Please wait... Control-C pressed admin:
```

If you run the command utils system switch-version and enter Yes to start the process, entering Ctrl-C exits the command but does not stop the switch-version process.

### End CLI Session

To end the CLI session, enter quit at the CLI prompt.

If you are logged in remotely, you get logged off, and the SSH session is terminated. If you are logged in locally, you get
                                 logged off, and the login prompt appears.

### Additional CLI Commands

Besides the commands available on Unified CCX , more commands are available that can be run as a part of Unified Operating System. For detailed information about all
                              the CLI commands available for the Cisco Unified Operating System, see the Command Line Interface Reference Guide for Cisco Unified Communications Solutions available here:

https://www.cisco.com/en/US/products/sw/voicesw/ps556/prod_maintenance_guides_list.html

The following Unified Operating System commands are not applicable to Unified CCX :

delete dscp

file delete license

file get license

file list license

file view license

set cert bulk

set dscp

set network cluster publisher

set network dhcp

set network ipv6 dhcp

set network ipv6 service

set network ipv6 static_address

show ctl

show dscp

show itl

show network ipv6 settings

show tech ccm_service

run loadxml

utils sso unavailable

utils system upgrade dataexport initiate

Important

When file get CLI command is used with the abstime as an option to collect log files, this filters the files based on the last modified timestamp. If the last modified time
                                          is updated, this CLI may not give desired results. Use the log collection feature in RTMT instead to collect the log files.

## Show Commands

Custom values are set on the VVB servers by the VoiceBrowser.properties and SIPSubsystem.properties properties files. The following commands may reset the custom values to their default values:

```
show vvb cache *
show vvb call *
show vvb mrcp *
show vvb http client response timeout
```

### show uccx version

This
                              		command displays the Unified CCX versions on
                              		the active partition and the inactive partition. The inactive version is
                              		displayed only if the inactive partition is available.

Command syntax

show uccx version

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 0

Allowed
                              		during upgrade: Yes

Example

```
admin:show uccx version Active UCCX Version: 10.0.0.95000-136
 Inactive UCCX Version: NA
Command successful.
```

### show uccx
                           	 jtapi_client version

This
                              		command displays the JTAPI client version that the Unified CCX is using on the
                              		active and the inactive partitions. The inactive version is displayed only if
                              		the inactive partition is available.

Command syntax

show uccx jtapi_client
                                 		  version

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 0

Allowed
                              		during upgrade: Yes

Example

```
admin:show uccx jtapi_client version 
Active:Cisco JTAPI version 9.0(0.96000)-4 Release
Inactive: NA
Command successful.
```

### show uccx components

This
                              		command displays the various components in Unified CCX for which
                              		tracing can be turned on or off from CLI commands. This command is useful when
                              		you need the list of components to modify the trace settings of Unified CCX .

Command syntax

show uccx components

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 0

Allowed
                              		during upgrade: Yes

Example

```
admin:show uccx components
Various UCCX components are as follows -

 UCCXEngine
 UCCXCVD
 UCCXEditor
 JTAPI_CLIENT
 UCCXAppAdmin
```

### show uccx subcomponents

This
                              		command displays the various subcomponents in specific Unified CCX component.
                              		This command is useful when you need the list of subcomponents to modify the
                              		trace settings of Unified CCX .

Command syntax

show uccx subcomponents component [options]

Options

APP_MGR

ARCHIVE_MGR

BOOTSTRAP_MGR

CFG_MGR

CHANNEL_MGR
                                             				  and so on

page —Displays the
                                    			 output one page at a time

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 0

Allowed
                              		during upgrade: Yes

Example

```
admin:show uccx subcomponents uccxengine
```

### show uccx trace
                           	 levels

This
                              		command displays the names and trace levels of the various Unified CCX components
                              		and subcomponents. If the optional component is specified, then the trace
                              		settings of all the subcomponents of the specified component are displayed. If
                              		both the optional component and subcomponent are specified, then the trace
                              		settings of the specified subcomponent of the specified component are
                              		displayed.

Command syntax

show uccx trace levels
                                 		  [options]

Options

Component —Displays the
                                    			 trace levels of all the subcomponents of this component

Sub-component —Displays
                                    			 the trace levels of this subcomponent for the specified component. The trace
                                    			 levels can be displayed only if the component was specified

page —Displays the
                                    			 output one page at a time

file —Stores the output
                                    			 to a file instead of showing it on the console. The name of the file is
                                    			 displayed after the completion of the command

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 0

Allowed
                              		during upgrade: Yes

Example

```
admin:show uccx trace levels UCCXEngine Trace settings for component 'UCCX_ENGINE' and module  are
  ALARM = true
  DEBUGGING = false
  XDEBUGGING1 = false
  XDEBUGGING2 = false
  XDEBUGGING3 = false
  XDEBUGGING4 = false
  XDEBUGGING5 = false

 Command successful.
```

```
admin:show uccx trace levels UCCXEngine Trace settings for component 'UCCX_ENGINE' and module  are
  ALARM = true
  DEBUGGING = false
  XDEBUGGING1 = false
  XDEBUGGING2 = false
  XDEBUGGING3 = false
  XDEBUGGING4 = false
  XDEBUGGING5 = false

 Command successful.
```

### show uccx provider ip axl

This command shows the Unified CCX AXL provider IP address.

Command syntax

show uccx provider ip axl

Requirements

Level privilege: 0

Command privilege level: 0

Allowed during upgrade: Yes

Example

```
admin: show uccx provider ip axl
Cisco Unified Communications Manager IP is 10.78.14.140

Command Successful.
```

### show uccx provider ip jtapi

This command shows the Unified CCX JTAPI provider IP address.

Command syntax

show uccx provider ip jtapi

Requirements

Level privilege: 0

Command privilege level: 0

Allowed during upgrade: Yes

Example

```
admin: show uccx provider ip jtapi
UCCX JTAPI Provider is 10.78.14.140

Command Successful.
```

### show uccx provider ip rmcm

This command shows the Unified CCX Resource Manager-Contact Manager provider IP address.

Command syntax

show uccx provider ip rmcm

Requirements

Level privilege: 0

Command privilege level: 0

Allowed during upgrade: Yes

Example

```
admin: show uccx provider ip rmcm
UCCX RMCM Provider is 10.78.14.140

Command Successful.
```

### show uccx trace file
                           	 size

This
                              		command shows the trace file size for the specified component.

Command syntax

show uccx trace file size [component]

Options

component—(Mandatory) Component such as UCCXEngine or
                                 		  UCCXEditor

Requirements

Level
                              		privilege: 1

Command
                              		privilege level: 1

Allowed
                              		during upgrade: Yes

Example

```
admin: show uccx trace file size UCCXEngine
Trace file size for UCCXEngine is 3000000 bytes.

Command Successful.
```

### show uccx trace file
                           	 size

This
                              		command shows the trace file size for the specified component.

Command syntax

show uccx trace file size [component]

Options

component—(Mandatory) Component such as UCCXEngine or
                                 		  UCCXEditor

Requirements

Level
                              		privilege: 1

Command
                              		privilege level: 1

Allowed
                              		during upgrade: Yes

Example

```
admin: show uccx trace file size UCCXEngine
Trace file size for UCCXEngine is 3000000 bytes.

Command Successful.
```

### show uccx trace file
                           	 count

This
                              		commands shows the trace file count for the specified component, which is the
                              		maximum number of trace files. The new file overwrites the older files.

Command syntax

show uccx trace file count
                                 		  [component]

Options

component —(Mandatory)
                              		Component such as UCCXEngine or
                                 		  UCCXEditor

Requirements

Level
                              		privilege: 1

Command
                              		privilege level: 1

Allowed
                              		during upgrade: Yes

Example

```
admin: show uccx trace file count UCCXEngine
Trace file count for UCCXEngine is 300.

Command Successful.
```

### show uccx
                           	 livedata connections

This command displays the status of the Socket.IO service and the following details of the LiveData connection:

Total Active Client Connections to Socket.IO server.

Total Long Polling clients connected to Socket.IO server.

Command syntax

show uccx livedata
                                 		  connections

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 0

Allowed
                              		during upgrade: Yes

Example

```
admin:show uccx socketio connection
Server Status: Active
Client Count: 2 (polling: 1)

Command successful.
```

### show tls server cert_type

This command displays the configured certificate type used by the server for TLS connections.

Command syntax

show tls server cert_type

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

```
admin:show tls server cert_type
The server certificate type is set to ECDSA

Command successful
```

### show tls server
                           	 min-version

This command allows
                              		you to show the minimum TLS version in the server that is currently configured.

Command syntax

show tls server min-version
                                 		  [tls server minVersion]

Options

tls server minVersion —Refers to 1.2 (TLS Version 1.2)

Requirements

Level
                              		privilege: 1

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

```
admin:show tls server min-version
The server tls min-version is set to 1.2
Command successful
```

### show tls client
                           	 min-version

This command allows
                              		you to show the minimum TLS version in the client that is currently configured.

Command syntax

show tls client min-version
                                 		  [tls client minVersion]

Options

tls client minVersion —Refers to 1.2 (TLS Version 1.2)

Requirements

Level
                              		privilege: 1

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

```
admin:show tls client min-version
The client tls min-version is set to 1.2
Command successful
```

### show uccx tech dbserver
                           	 all

This
                              		command runs the commands show uccx tech dbserver log
                                 		  diagnostic and show uccx tech dbserver
                                 		  status in succession and stores the output of the commands in a file.

Command syntax

show uccx tech dbserver
                                 		  all

The name of the
                                          		  file containing the output from each show uccx tech command
                                          		  run is automatically generated by the command script. The file path and
                                          		  filename are displayed after the completion of the operation.

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 0

Allowed
                              		during upgrade: Yes

Example

```
admin:show uccx tech dbserver all 
This operation may take a few minutes to complete. Please wait...

Output is in file: uccx/cli/DbServerAll_1250664874580.txt

Command successful.
```

### show uccx tech dbserver log
                           	 diagnostic

This
                              		command checks for the existence of Informix assertion failure and shared
                              		memory dump logs. If logs exist, the name and path of the log files are
                              		displayed.

Command syntax

show uccx tech dbserver log
                                 		  diagnostic [options]

Options

page —Displays the
                              		output one page at a time

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 0

Allowed
                              		during upgrade: Yes

Example

```
admin:show uccx tech dbserver log diagnostic 
This operation may take a few minutes to complete. Please wait...

The following diagnostic logs are available for the UC database server.
 core/log.txt
 core/gskit.log

 Command successful.
```

### show uccx tech dbserver
                           	 status

This
                              		command outputs a detailed status report of the Unified
                                 		  CCX database
                              		server (IDS engine) instance, that is onstat -a to a
                              		txt file.

Command syntax

show uccx tech dbserver status

The name of the
                                          		  file is automatically generated by the command script. The file path and
                                          		  filename are displayed after the completion of the operation.

Requirements

Level
                              		privilege—0

Command
                              		privilege level—0

Allowed
                              		during upgrade—Yes

Example

```
admin:show uccx tech dbserver status 
This operation may take a few minutes to complete. Please wait...

 Output is in file: uccx/cli/DbServerStatus_1250666138379.txt

 Command successful.
```

### show uccx dbcontents

This
                              		command dumps the contents of the specified database. This command can be used
                              		to recreate a customer database on a test system for troubleshooting. For each Unified CCX database table, a
                              		dump csv file is created. Because there are huge numbers of files, these files
                              		are created in a subdirectory which will have the name as
                              		DbContents_<TIMESTAMP>. After the completion of the command, the
                              		subdirectory name and subdirectory path are displayed.

Command syntax

show uccx dbcontents
                                 		  database_name

Arguments

database_name —(Mandatory) Database whose contents will be
                              		output to CSV file

Requirements

Level
                              		privilege: 1

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

```
admin:show uccx dbcontents db_cra 
 This operation may take a few minutes to complete. Please wait...
 Database contents dump is in directory: uccx/cli/DbContents_1250666234370

 Command successful.
```

### show uccx dbtable schema

This
                              		command displays the column names of the specified table.

Command syntax

show uccx dbtable schema
                                 		  database_name table_name [options]

Arguments

database_name—(Mandatory) Name of the database (db_cra,
                              		db_cra_repository etc.,) in which the table resides

table_name—(Mandatory) Name of the table

Options

page—Displays the
                              		output one page at a time

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 0

Allowed
                              		during upgrade: Yes

Example

```
admin:show uccx dbtable schema db_cra_repository documentsfiletbl
List of columns in table 'documentsfiletbl' in database 'db_cra_repository' is -
filename (nvarchar)
parentfolderid (nvarchar)
payload (blob)
lastmodifystamp (datetime year to fraction(3))
lastmodifyuser (nvarchar)
length (int)
checksum (int)

Command successful.
```

### show uccx dbschema

This
                              		command outputs the schema for all the tables, views, and stored procedures in
                              		the specified database to a text file. The output consists of SQL statements
                              		that are necessary to replicate a specified database. The IDS "dbschema" utility is used to create the file. This command only displays the DB schema;
                              		it does not provide any data in the tables.

Command syntax

show uccx dbschema database_name

Arguments

database_name —(Mandatory) Name of the database whose schema
                              		will be output

The name of the
                                          		  file containing the schema is automatically generated by the command script.
                                          		  The file path and filename are displayed after the completion of the operation.

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 0

Allowed
                              		during upgrade: Yes

Example

```
admin:show uccx dbschema db_cra
Output is in file: uccx /cli/schema_db_cra_080212-110543.txt
```

### show uccx dbtable list

This
                              		command displays the names of all the tables contained in the specified Unified
                                 		  CCX IDS database.
                              		The database names can be db_cra, db_cra_repository, FCRasSvr, sysmaster.

Command syntax

show uccx dbtable list database_name
                                 		  [options]

Arguments

database_name—(Mandatory) Database name where tables reside

Options

page—Displays the
                              		output one page at a time

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 0

Allowed
                              		during upgrade: Yes

Example

```
admin:show uccx dbtable list 
db_craList of tables in database 'db_cra' is -
 agentconnectiondetail
 agentroutingsetting
 agentstatedetail
 application
 areacode
 campaign
 campaigncsqmap
 configlog
 configschema
 configschemacolumn
 configseed 
…
…
teamcsqmapping
 workflowtask
 Command successful.
```

### show uccx dbserver disk

This
                              		command displays information for each storage space (chunks and dbspaces).

Command syntax

show uccx dbserver disk [options]

Options

page —Displays the
                              		output one page at a time

file —Outputs the
                              		information to a .txt file. The filename is generated dynamically at runtime
                              		and the filename and path are displayed to user after the completion of the
                              		operation.

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 0

Allowed
                              		during upgrade: Yes

Example

```
admin:show uccx dbserver disk
SNO. DATABASE NAME      TOTAL SIZE (MB) USED SIZE (MB) FREE SIZE (MB) PERCENT FREE
---- ------------------ --------------- -------------- -------------- ------------
 1    rootdbs                     358.4           66.3          292.1          81%
 2    log_dbs                     317.4          307.3           10.1           3%
 3    db_cra                      512.0            8.8          503.2          98%
 4    db_hist                   13000.0         3651.4         9348.6          71%
 5    db_cra_repository            10.2            2.9            7.3          71%
 6    db_frascal                  512.0            2.8          509.2          99%
 7    temp_uccx                  1572.9            0.1         1572.7          99%
 8    uccx_sbspace               3145.7         2988.1          157.6           5%
 9    uccx_er                     204.8            0.1          204.7          99%
 10   uccx_ersb                  1572.9         1494.1           78.8           5%

CHUNK NO. OFFSET TOTAL SIZE (MB) FREE SIZE (MB) FILENAME
--------- ------ --------------- -------------- ---------------------------------------------
 1         0               358.4          292.1  /var/opt/cisco/uccx/db/root_uccx_dbs
 2         0               317.4           10.1  /var/opt/cisco/uccx/db/log_dbs
 3         0               512.0          503.2  /var/opt/cisco/uccx/db/db_cra_dbs
 4         0             13000.0         9348.6  /common/var-uccx/dbc/db_hist_dbs
 5         0                10.2            7.3  /var/opt/cisco/uccx/db/db_cra_repository_dbs
 6         0               512.0          509.2  /var/opt/cisco/uccx/db/db_frascal_dbs
 7         0              1572.9         1572.8  /common/var-uccx/dbc/temp_uccx_dbs
 8         0              3145.7          157.6  /var/opt/cisco/uccx/db/uccx_sbspace_dbs
 9         0               204.8          204.7  /common/var-uccx/dbc/uccx_er_dbs
 10        0              1572.9           78.8  /common/var-uccx/dbc/uccx_ersb_dbs
```

### show uccx dbserver sessions
                           	 all

This
                              		command displays detailed session and SQL-related information for each database
                              		user session. The content of the information displayed is equivalent to running
                              		the IDS command onstat -g ses for each active session.

Command syntax

show uccx dbserver sessions all
                                 		  [options]

Options

page—Displays
                                    			 the output one page at a time

file—Outputs the
                                    			 information to a txt file. The filename is generated dynamically at runtime and
                                    			 the filename and path are displayed to user after the completion of the
                                    			 operation.

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 0

Allowed
                              		during upgrade: Yes

Example

```
admin:show uccx dbserver sessions all
IBM Informix Dynamic Server Version 10.00.UC5XD   -- On-Line -- Up 58 days 02:26:37 -- 444676 Kbytes

session                                      #RSAM    total      used       dynamic
id       user     tty      pid      hostname threads  memory     memory     explain
27       cudbeven -        6750     crslnx   1        151552     75400      off

tid      name     rstcb    flags    curstk   status
75       sqlexec  52477164 Y--P---  4208     cond wait(netnorm)

Memory pools    count 2
name         class addr     totalsize freesize #allocfrag #freefrag
27           V     5309a020 147456    73704    148        50
27*O0        V     5442f020 4096      2448     1          1

name           free       used           name           free       used
overhead       0          3296           scb            0          96
opentable      0          6456           filetable      0          1088

sqscb info
scb      sqscb    optofc   pdqpriority sqlstats optcompind  directives
52fda4d0 53234018 0        0           0        0           1

Sess  SQL            Current            Iso Lock       SQL  ISAM F.E.
Id    Stmt type      Database           Lvl Mode       ERR  ERR  Vers Explain   
27    -              uccxdirdb         CR  Wait 30    0    0    9.03 Off       

Last parsed SQL statement :
  SELECT FIRST 100 *, CAST(Timestamp AS varchar(32)) AS strTimestamp,
    CAST(Object_Id AS varchar(64)) AS strObject_Id FROM
    UccxDb: DbChangeEventQ WHERE EventId > ? ORDER BY EventId ASC
```

### show uccx dbserver session

This
                              		command displays detailed session and SQL-related information for a specific
                              		session, which represents a user connected to the database server. The content
                              		of the information displayed is equivalent to running the IDS command onstat -g ses for an active session specified by the session-id.

Command syntax

show uccx dbserver session session_id
                                 		  [options]

Arguments

session_id—(Mandatory) The Informix session ID number

Options

page —Displays the
                              		output one page at a time

file —Outputs the
                              		information to a .txt file. The filename is generated dynamically at runtime
                              		and the filename and path are displayed to user after the completion of the
                              		operation.

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 0

Allowed
                              		during upgrade: Yes

Example

```
admin:show uccx dbserver session 58
IBM Informix Dynamic Server Version 11.50.UC4     -- On-Line -- Up 14 days 04:43:40 -- 254160 Kbytes

session           effective                            #RSAM    total      used       dynamic
id       user     user      tty      pid      hostname threads  memory     memory     explain
58       uccxuser -         -        -1       sakkumar 1        126976     107496     off

tid      name     rstcb    flags    curstk   status
93       sqlexec  4b2deca0 Y--P---  5680     cond wait  netnorm   -

Memory pools    count 2
name         class addr     totalsize freesize #allocfrag #freefrag
58           V     4caa9028 122880    17064    332        18
58*O0        V     4c9d0028 4096      2416     1          1

name           free       used           name           free       used
overhead       0          3360           scb            0          96
opentable      0          8344           filetable      0          1104
ru             0          464            log            0          16512
temprec        0          21600          keys           0          1392
ralloc         0          5120           gentcb         0          1240
ostcb          0          2600           sqscb          0          29384
sql            0          40             rdahead        0          848
hashfiletab    0          280            osenv          0          1552
sqtcb          0          7464           fragman        0          368
GenPg          0          592            udr            0          5136

sqscb info
scb      sqscb    optofc   pdqpriority sqlstats optcompind  directives
4c907018 4cc92018 1        0           0        2           1

Sess       SQL            Current            Iso Lock       SQL  ISAM F.E.
Id         Stmt type      Database           Lvl Mode       ERR  ERR  Vers  Explain
58         -              db_cra             LC  Not Wait   0    0    9.28  Off

Last parsed SQL statement :
  select campaignen0_.campaignID as campaignID3_, campaignen0_.profileID as
    profileID3_, campaignen0_.recordID as recordID3_, campaignen0_.active as
    active3_, campaignen0_.ansMachineRetry as ansMachi5_3_,
    campaignen0_.cacheSize as cacheSize3_, campaignen0_.callbackTimeLimit as
    callback7_3_, campaignen0_.campaignName as campaign8_3_,
    campaignen0_.createDateTime as createDa9_3_, campaignen0_.dateInactive as
    dateIna10_3_, campaignen0_.description as descrip11_3_,
    campaignen0_.enabled as enabled3_, campaignen0_.endTime as endTime3_,
    campaignen0_.maxAttempts as maxAtte14_3_,
    campaignen0_.missedCallbackAction as missedC15_3_,
    campaignen0_.privateData as private16_3_, campaignen0_.startTime as
    startTime3_ from Campaign campaignen0_ where campaignen0_.active=?
 Command successful.
```

### show uccx dbserver sessions
                           	 list

This
                              		command displays a one-line summary of each active Unified
                                 		  CCX database
                              		session. The summary includes the database name, username, session ID, and
                              		process ID. The session ID information can be used to display more detailed
                              		information about a specified session using the show uccx dbserver session command.

Command syntax

show uccx dbserver sessions list
                                 		  [options]

Options

page —Displays the
                              		output one page at a time

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 0

Allowed
                              		during upgrade: Yes

Example

```
admin:show uccx dbserver sessions list
DATABASE           USERNAME     SESSION PROCESS ID
------------------ ------------ ------- ----------
 db_cra             uccxuser         49         -1
 db_cra             uccxuser         44         -1
 db_cra             uccxuser         46         -1
 db_cra             uccxuser         61         -1
 db_cra             uccxuser         24         -1
 db_cra             uccxuser         18         -1
 db_cra             uccxhruser    31224         -1
 db_cra             uccxuser         62         -1
 db_cra             uccxuser         60         -1
 db_cra             uccxuser         47         -1
 db_cra             uccxuser         59         -1
 db_cra             uccxuser         58         -1
 db_cra             uccxuser         48         -1
 db_cra             uccxuser         50         -1
 db_cra             uccxcliuser   31616         -1

 Command successful.
```

### show uccx dbserver user list

This
                              		command displays a one-line summary of each active uccx database user. The summary
                              		includes the database name, session ID and process ID. The session ID
                              		information can be used to display more detailed information about a specified
                              		user session using the show Unified
                                    			 CCX dbserver
                                 		  session command.

Command syntax

show uccx dbserver user list
                                 		  [option]

Option

page —Displays the
                              		output one page at a time

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 0

Allowed
                              		during upgrade: Yes

Example

```
admin:show uccx dbserver user list
DATABASE           USERNAME     SESSION PROCESS ID
------------------ ------------ ------- ----------
 sysadmin           informix         15          0
 sysadmin           informix         16          0
 sysadmin           informix         17          0
 sysmaster          uccxuser         18         -1
 db_cra             uccxuser         18         -1
 sysmaster          uccxuser         24         -1
 db_cra             uccxuser         24         -1
 db_cra_repository  uccxuser         25         -1
 sysmaster          uccxuser         25         -1
 fcrassvr           uccxuser         26         -1
 sysmaster          uccxuser         26         -1
 sysmaster          uccxuser         44         -1
 db_cra             uccxuser         44         -1
 db_cra_repository  uccxuser         45         -1
 sysmaster          uccxuser         46         -1
 db_cra             uccxuser         46         -1
 sysmaster          uccxuser         47         -1
 db_cra             uccxuser         47         -1
 db_cra             uccxuser         48         -1
 sysmaster          uccxuser         48         -1
 sysmaster          uccxuser         49         -1

 Command successful.
```

### show uccx dbserver user
                           	 waiting

This
                              		command displays a one-line summary of each Unified
                                 		  CCX database user
                              		and also displays whether a user session is waiting for a resource.

Command syntax

show uccx dbserver user waiting
                                 		  [option]

Option

page—Displays the
                              		output one page at a time

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 0

Allowed
                              		during upgrade: Yes

Example

```
admin:show uccx dbserver user waiting
USERNAME     SESSION ID LATCH LOCK BUFFER CHECKPOINT TRANSACTION INCRITICAL
------------ ---------- ----- ---- ------ ---------- ----------- ----------
 informix            16     N    N      N          N           N          N
 informix            17     N    N      N          N           N          N
 informix            15     N    N      N          N           N          N
 uccxcliuser      33927     N    N      N          N           N          N
 uccxcliuser      32784     N    N      N          N           N          N
 uccxcliuser      32737     N    N      N          N           N          N
 uccxcliuser      32631     N    N      N          N           N          N
 uccxcliuser      34424     N    N      N          N           N          N
 uccxcliuser      32522     N    N      N          N           N          N
 uccxcliuser      34364     N    N      N          N           N          N
 uccxcliuser      32508     N    N      N          N           N          N
 uccxcliuser      32480     N    N      N          N           N          N
 uccxcliuser      31616     N    N      N          N           N          N
 uccxcliuser      31601     N    N      N          N           N          N
 uccxcliuser      34327     N    N      N          N           N          N
 uccxcliuser      34071     N    N      N          N           N          N
 uccxcliuser      33981     N    N      N          N           N          N
 uccxcliuser      33939     N    N      N          N           N          N
 uccxhruser       31224     N    N      N          N           N          N
 uccxuser         30278     N    N      N          N           N          N
 uccxuser            60     N    N      N          N           N          N

 Command successful.
```

### show uccx tech dbserver log
                           	 message

This
                              		command displays the most recent messages in the Informix message log. The
                              		number of messages displayed is determined by the lines parameter.

Command syntax

show uccx tech dbserver log message
                                 		  [lines] [option]

Arguments

lines —(Optional) Number
                              		of lines from message log that will be displayed. Defaults to 20.

Option

page —Displays the
                              		output one page at a time

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 0

Allowed
                              		during upgrade: Yes

Example

```
admin:show uccx tech dbserver log message 10
Message Log File: online.uccx.log

The last 10 lines of the log file are -

16:05:19  Maximum server connections 33
16:05:19  Checkpoint Statistics - Avg. Txn Block Time 0.000, # Txns blocked 0, Plog used 21, Llog used 12

16:10:19  Checkpoint Completed:  duration was 0 seconds.
16:10:19  Wed Aug 19 - loguniq 8, logpos 0x93c018, timestamp: 0xb0244c Interval: 4106

16:10:19  Maximum server connections 33
16:10:19  Checkpoint Statistics - Avg. Txn Block Time 0.000, # Txns blocked 0, Plog used 2, Llog used 2

 Command successful.
```

### show uccx dbtable contents

This
                              		command displays the contents of the specified table.

Command syntax

show uccx dbtable contents
                                 		  database_name table_name [option]

Arguments

database_name—(Mandatory) Name of the database for example,
                              		db_cra, db_cra_repository in which the table resides

table_name—(Mandatory) Name of the table

Option

page —Displays the
                              		output one page at a time

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 0

Allowed
                              		during upgrade: Yes

Example

```
admin:show uccx dbtable contents db_cra resource 
Output is in file: uccx/cli/resource_Contents_1250666550481.csv

 Command successful.
```

### show vmtools version

This command displays the current version of the vmtools that are installed on the system.

Command syntax

show vmtools version

Requirements

Level privilege: 0

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:show vmtools version
Current VMWare Tools running version: 10.0.9.55972 (build-3917699)
```

### show vvb cache
                           	 browser_cache_size

This
                              		command shows the currently allocated browser cache size in KB.

Command syntax

show vvb cache
                                 		  browser_cache_size

Requirements

Level
                              		privilege: 1

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

```
admin:show vvb cache browser_cache_size   
  2048000 KB
 Command successful.
```

### show vvb cache
                           	 dom_cache_capacity

This command shows the DOM cache capacity.

Command syntax

show vvb cache dom_cache_capacity

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:show vvb cache dom_cache_capacity  
  64 entries
 Command successful.
```

### show vvb cache
                           	 enable_browser_cache

This command shows if the browser cache is enabled where True is enabled and False is disabled.

Command syntax

show vvb cache enable_browser_cache

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:show vvb cache enable_browser_cache  
  true
 Command successful.
```

### show vvb cache
                           	 enable_browser_cache_trace

This command shows if the browser cache trace is enabled.

Command syntax

show vvb cache enable_browser_cache_trace

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:show vvb cache enable_browser_cache_trace  
  false
 Command successful.
```

### show vvb cache
                           	 extensions

This
                              		command shows the extensions used for Cisco VVB.

Command syntax

show vvb cache
                                 		  extensions

Requirements

Level
                              		privilege: 1

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

```
admin:show vvb cache extensions
  jsp
  ircgi
  nohead
  testingExt
 Command successful.
```

### show vvb cache
                           	 max_file_size

This command shows the maximum cache size of a resource. If the size of the resource exceeds this limit, the resource will
                              not be added to the cache.

Command syntax

show vvb cache
                                 		  max_file_size

Requirements

Level
                              		privilege: 1

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

```
admin:show vvb cache max_file_size
 2048 KB

 Command successful.
```

### show vvb cache
                           	 cache_entries

This command shows all or selected entries that are cached.

Command syntax

show vvb cache
                                    			 cache_entries <start_index> <end_index>

Options

<start_index> -
                                 		  (Optional) Provide start index entry number.

<end_index> -
                                 		  (Optional) Provide end index entry number.

Requirements

Level
                                 		  privilege: 1

Command
                                 		  privilege level: 1

Allowed
                                 		  during upgrade: No

Example 1

```
admin:show vvb cache cache_entries
Total Cache size: 2048000 KB
Total Cache size used: 66 KB
MaxFileSize: 2048 KB
Total number of Cache Entries: 1
Number of Entries retrieved: 1
EntryType       Size(Bytes)     Cache Entry
----------------------------------------------------------------------
File            68192           http://10.78.0.112:7000/CVP/audio/3min.wav
 Command successful.
```

Example 2

```
admin:show vvb cache cache_entries 1 2
Total Cache size: 2048000 KB
Total Cache size used: 66 KB
MaxFileSize: 2048 KB
Total number of Cache Entries: 1
Number of Entries retrieved: 1
EntryType       Size(Bytes)     Cache Entry
----------------------------------------------------------------------
File            68192           http://10.78.0.112:7000/CVP/audio/3min.wav
 Command successful.
```

## Set Commands

### set uccx trace
                           	 defaults

This
                              		command sets the default trace levels for all components and subcomponents in Unified CCX . If the
                              		optional component is specified, it sets the default trace levels only for all
                              		the subcomponents of the specified component. If both the optional component
                              		and subcomponent are specified, it sets the default trace levels only for the
                              		specified subcomponent under the component.

Command syntax

set uccx trace defaults
                                 		  [component] [subcomponent]

Options

Component —(Mandatory)
                                    			 Sets the default trace levels for all the subcomponents of this component. The
                                    			 various components are UCCXEngine, UCCXCvd,
                                       				UCCXAppAdmin and JTAPI_CLIENT .

Sub-component —(Optional) Sets the default trace levels for
                                    			 this subcomponent for the specified component. This trace level can be
                                    			 specified only if the component was specified preceding it.

Requirements

Level
                              		privilege: 1

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

```
admin:set uccx trace defaults uccxengine SS_HTTP Default traces restored successfully for the module.
```

### set uccx trace file size
                           	 component size

This
                              		command sets the trace file size for the specified component.

Command syntax

set uccx trace file size
                                 		  [component] [size]

Parameters

component —(Mandatory)
                              		The component such as UCCXEngine or
                                 		  UCCXEditor

size —(Mandatory)
                              		Specifies the file size in bytes

Requirements

Level
                              		privilege: 1

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

```
admin:set uccx trace file size uccxengine 3145728
Trace file size for uccxengine is set to 3145728 bytes.
```

### set uccx trace file count
                           	 component no-of-files

This
                              		command sets the trace file count for the specified component, that is the
                              		maximum number of trace files after which older files will start getting
                              		overwritten.

Command syntax

set uccx trace file count
                                 		  [component] [no-of-files]

Arguments

component —(Mandatory)
                                    			 The component such as UCCXEngine or
                                       				UCCXEditor .

no-of-files —(Mandatory)
                                    			 Specifies the number of files after which older files will get overwritten.

Requirements

Level
                              		privilege—1

Command
                              		privilege level—1

Allowed
                              		during upgrade—No

Example

```
admin:set uccx trace file count uccxengine 300
Trace file count for uccxengine is set to 300
```

### set uccx trace
                           	 enable

Enables the specified logging level for the sub-component in the component mentioned in the command. The user can enter multiple
                              levels of logging by separating them by commas.

After the completion of the command, a message is displayed showing the current log trace settings enabled.

Restart the Unified CCX services for the trace changes to take effect.

Command syntax

set uccx trace enable [component] [sub-component] [level]

Options

component —(Mandatory) The component such as UCCXEngine or UCCXEditor or JTAPI_CLIENT

sub-component —(Mandatory) The subcomponent within the component such as JTAPI Subsystem within the UCCXEngine component. For the JTAPI_CLIENT component, there are no sub-components.

sub-component —(Mandatory) The subcomponent within the component such as SS_SIP within the UCCXEngine component. For the SS_SIP component, there are no sub-components.

Level —(Mandatory) The logging level which will be enabled. Tracing levels are Debugging, XDebugging1, XDebugging2, XDebugging2,
                              XDebugging3, XDebugging4 and XDebugging5. For the JTAPI_CLIENT, the tracing levels are Warning, Informational, Debug, Jtapi_Debug, JtapiImpl_Debug, Cti_Debug, CtiImpl_Debug,
                                 Protocol_Debug and Misc_Debug.

Level —(Mandatory) The logging level which will be enabled. Tracing levels are Debugging, XDebugging1, XDebugging2, XDebugging2,
                              XDebugging3, XDebugging4 and XDebugging5.

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example 1

```
admin:set uccx trace enable uccxengine SS_VB debugging
 Trace for uccxengine :SS_VB:debugging is enabled.
 Command successful.
```

Example 2

```
admin:set uccx trace enable UCCXengine SS_SIP XDEBUGGING1,XDEBUGGING2
Trace for uccxengine :SS_SIP:XDEBUGGING1 is enabled
Trace for uccxengine :SS_SIP:XDEBUGGING2 is enabled
Command successful.
```

### set uccx trace
                           	 disable

Disables the specified logging level for the subcomponent in the component mentioned in the command. The user can enter multiple
                              levels of logging by separating them by commas. You cannot use this command to turn off Alarm tracing.

After the completion of the command, a message is displayed showing the current log trace settings enabled.

Restart the Unified CCX services for the trace changes to take effect.

Command syntax

set uccx trace disable [component] [sub-component] [level]

Options

Component —The component such as UCCXEngine or UCCXEditor or JTAPI_CLIENT .

Sub-component —The subcomponent within the component such as JTAPI Subsystem within the UCCXEngine component. For the JTAPI_CLIENT component, there are no subcomponents.

Sub-component —The subcomponent within the component such as SS_SIP within the UCCXEngine component.

Level —(Mandatory) The logging level which will be disabled. Tracing levels are Debugging, XDebugging1, XDebugging2, XDebugging2,
                              XDebugging3, XDebugging4 and XDebugging5. The tracing levels will also be available as part of the help of the command.

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example 1

```
admin:set uccx trace disable uccxengine SS_VB debugging
 Trace for uccxengine :SS_VB:debugging is disabled.
 Command successful.
```

Example 2

```
set uccx trace disable UCCXEngine SS_SIP XDEBUGGING1,XDEBUGGING2
Trace for uccxengine :SS_SIP:XDEBUGGING1 is disabled
Trace for uccxengine :SS_SIP:XDEBUGGING2 is disabled
Command successful.
```

### set password user
                           	 security

This command changes the security/SFTP password on Unified CCX . In addition to changing the security password, it also changes the passwords of the internal Unified CCX users.

Command syntax

set password user
                                 		  security

Requirements

Level
                              		privilege: 1

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

```
admin:set password user security   
Please enter the old password: ******
Please enter the new password: ******
Reenter new password to confirm: ******
WARNING:
Please make sure that the security password on the publisher is changed first.
The security password needs to be the same on all cluster nodes,
including the application server, therefore the security password on all nodes
need to be changed.

After changing the security password on a cluster node, please restart that node.

Continue (y/n)?y

Please wait...

Command successful.
```

### set tls server cert_type

Use this command to set the server certificate type to either RSA or ECDSA ciphers for TLS connections. The certificate set
                                 to the specified type is then presented for the cipher negotiations on all incoming TLS communications.

Command syntax

set tls server cert_type  [option]

Option

ecdsa—Sets the certificate type to ECDSA.

rsa—Sets the certificate type to RSA.

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:set tls server cert_type rsa

Configuring the server to use RSA certificates for all inbound connections.

Do you want to continue (y/n) ? y
Yes entered
Configuring the server to use RSA ciphers for inbound connections.

Successfully configured the server to use RSA certificate for all inbound connections.

********************************************************
A system reboot will occur for the changes to take effect.
It is highly recommended that you perform a system backup
after the system reboot.
Ensure all the nodes in the cluster are running on the same
certificate type by running the 'set' command
********************************************************

Broadcast message from root@uccxfirstnode (Mon Jul 5 10:31:04 2021):

The system is going down for reboot in 1 Minute

Broadcast message from root@uccxfirstnode (Mon 2021-07-05 10:31:05 IST):

The system is going down for reboot at Mon 2021-07-05 10:32:04 IST!
```

After the system reboots, the self-signed and CA certificates of the servers, whose certificate type has changed, must be
                                             regenerated and re-uploaded into the client servers.

### set tls server
                           	 min-version

This command allows you to configure the minimum TLS version in the server that can be used for inbound SSL connections. You
                              must restart the system for the changes to take effect.

In a high availability (HA) deployment, run this CLI command on both the nodes of the cluster. Restart both the nodes after
                                          executing the CLI command.

Command syntax

set tls server min-version
                                 		  [tls server minVersion]

Options

tls server minVersion —Refers to 1.2 (TLS Version 1.2)

Requirements

Level
                              		privilege: 1

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

```
admin:set tls server min-version 1.2
**WARNING** If you are lowering the TLS version it can lead to security issues **WARNING**
Do you really want to continue (yes/no) ? yes
Execute this command in the other nodes of the cluster.
Restart the system using the command 'utils system restart' for the changes to take effect
Command successful
```

### set tls client
                           	 min-version

This command allows
                              		you to configure the minimum TLS version in the client that can be used for
                              		outbound SSL connections. You must restart the system for the changes to take
                              		effect.

In a high
                                          		  availability (HA) deployment, run this CLI command on both the nodes of the
                                          		  cluster. Restart both the nodes after executing the CLI command.

Command syntax

set tls client min-version
                                 		  [tls client minVersion]

Options

tls client minVersion —Refers to 1.2 (TLS Version 1.2)

Requirements

Level
                              		privilege: 1

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

```
admin:set tls client min-version 1.2
**WARNING** If you are lowering the TLS version it can lead to security issues **WARNING**
Do you really want to continue (yes/no) ? yes
Execute this command in the other nodes of the cluster.
Restart the system using the command 'utils system restart' for the changes to take effect
Command successful
```

### set uccx provider
                           	 ip axl

This
                              		command sets the Unified CCX AXL provider IP address. Use this command only
                              		when the IP address of Unified Communications Manager has been changed and
                              		Unified CCX is being pointed to the new IP address.

After you run this
                                          		  command, restart the Unified CCX Engine service. After Unified CCX Engine
                                          		  service starts successfully, restart Cisco Tomcat using the CLI command utils service
                                             			 restart Cisco Tomcat .

Command syntax

set uccx provider ip axl
                                 		  [ip-address]

Arguments

[ip-address] —The IP
                              		address of the AXL provider.

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 0

Allowed
                              		during upgrade: No

Example

```
admin: set uccx provider ip axl 10.78.14.140
Cisco Unified Communications Manager IP is set to 10.78.14.140

Command Successful.
```

### set uccx provider
                           	 ip jtapi

This
                              		command sets the Unified CCX JTAPI provider IP address. Use this command only
                              		when the IP address of Unified Communication Manager has been changed and
                              		Unified CCX is being pointed to the new IP address.

After you run this
                                          		  command, restart the Unified CCX Engine service. After Unified CCX Engine
                                          		  service starts successfully, restart Cisco Tomcat using the CLI command utils service
                                             			 restart Cisco Tomcat .

Command syntax

set uccx provider ip jtapi [ip-address]

Arguments

[ip-address] —The IP
                              		address of the JTAPI provider.

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 0

Allowed
                              		during upgrade: No

Example

```
admin: set uccx provider ip jtapi 10.78.14.140
UCCX JTAPI Provider is set to 10.78.14.140

Command Successful.
```

### set uccx provider
                           	 ip rmcm

This
                              		command sets the Unified CCX Resource Manager-Contact Manager provider IP
                              		address. Use this command only when the IP address of Unified Communications
                              		Manager has been changed and Unified CCX is being pointed to the new IP
                              		address.

After you run this
                                          		  command, restart the Unified CCX Engine service. After Unified CCX Engine
                                          		  service starts successfully, restart Cisco Tomcat using the CLI command utils service
                                             			 restart Cisco Tomcat .

Command syntax

set uccx provider ip rmcm [ip-address]

Arguments

[ip-address] —The IP
                              		address of the RMCM provider.

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 0

Allowed
                              		during upgrade: No

Example

```
admin: set uccx provider ip rmcm 10.78.14.140
UCCX RMCM Provider is set to 10.78.14.140

Command Successful.
```

### set uccx appadmin
                           	 administrator

Administrator capability can be added to a user in Unified
                              		Communications Manager using this command.

Run this command
                                          		  to set the administrator for a configured Unified CCX system only.
                                          		  For a newly installed system, you must login with the platform login password
                                          		  that you specified during installation.

Command syntax

set uccx appadmin
                                 		  administrator [username]

Options

[username] —Username is
                              		set as the Cisco Unified CCX application
                              		administration.

Requirements

Level
                              		privilege: 1

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

```
admin:set uccx appadmin administrator username UCCX appadmin adminstrator is set to username
```

You cannot assign
                                          		  Administrator capability to a user ID that is the same as the application
                                          		  administrator user ID that you created during the Unified CCX installation. If you assign Administrator capability to such a user ID, a "Command
                                             			 failed" error message is displayed on the console.

### set
                           	 authmode

This command is
                              		used to set the authentication mode.

Command syntax

set authmode
                                 		  <non_sso>

Options

non_sso - to set
                              		authentication to Non-SSO mode.

Requirements

Level
                              		privilege: 4

Command
                              		privilege level: 4

Allowed
                              		during upgrade: No

Example

```
admin:set authmode non_sso
```

### set uccx asr count clear

This command clears all the counts that were recorded from the ASR hosts.

Command syntax

set uccx asr count clear

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:set uccx asr count clear
ASR reset successfully

Command successful.
```

### set uccx tts count clear

This command clears all the counts that were recorded from the TTS hosts.

Command syntax

set uccx tts count clear

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:set uccx tts count clear
ASR reset successfully

Command successful.
```

## run Commands

### run uccx hrdataexport

This command dumps the historical reporting data and related configuration information to csv files, and a tar file is created that contains all the exported csv files. The tar file is saved in the local file system, under <activelog>/uccx/log/db/hrdataexport .

The command output indicates the filename and specific commands that you must run to transfer the generated tar file to a remote server and to delete the file from the local disk.

If the Start Date and End Date are specified, then the data between those dates, including the start and end dates, is exported.
                                 If only one date parameter is passed, it is considered as start date and all the data from that date onwards is exported.

When the command is run, any previous tar file that was created is deleted. At any point only one Historical Reporting data export file is saved in the local file
                                             system. So after the Historical Reporting data is exported, transfer the tar file to remote server before running the command again.

Command Syntax

run uccx hrdataexport all [Start Date] [End Date]

Dumps all the historical reporting data.

run uccx hrdataexport reports report names [Start Date] [End Date]

Dumps all the historical reporting data for given reports.

run uccx hrdataexport tables table names [Start Date] [End Date]

Dumps all the historical reporting data for given table names.

Parameters

report names —(Mandatory) Comma separated names of the specific reports for which the corresponding data has to be exported. Enclose the
                                 list of report names in " " (double quotes).

table names —(Mandatory) Comma separated names of the specific tables from which the data is exported. Enclose the list of table names
                                 in " " (double quotes). Only the following tables can be exported:

agentconnectiondetail

agentstatedetail

contactcalldetail

contactqueuedetail

contactroutingdetail

dialinglisthistory

skill

skillgroup

resource

resourcegroup

resourceskillmapping

contactservicequeue

team

dialinglist

campaign

textagentconnectiondetail

textcontactdetail

textcontactqueuedetail

textagentstatedetail

textratingdetail

eemcontactemaildetail

eemqueueagentdetail

eememailagentstatedetail

audit_reskill

audit_skillgroup

audit_residualskills

contactwrapupdata

contactholddetail

contactfeedbackdetail

flexlicenseusage

consultlegdetail

textcustomerdetails

-

[Start Date] —(Optional) Must be in the format “yyyy-MM-dd HH:mm:ss”, including the double quotes.

[End Date] —(Optional) Must be in the format “yyyy-MM-dd HH:mm:ss”, including the double quotes.

Examples

```
admin:run uccx hrdataexport all "2012-01-01 00:00:00" "2012-02-01 00:00:00"
```

```
admin:run uccx hrdataexport reports "abandoned call detail activity report,aborted rejected call detail report" 
"2012-01-01 00:00:00" "2012-02-01 00:00:00"
```

```
admin:run uccx hrdataexport tables "agentconnectiondetail,agentstatedetail,contactcalldetail" 
"2012-01-01 00:00:00" "2012-02-01 00:00:00"
```

### run uccx sql database_name sql_query

Runs an SQL "select" statement from the CLI. Read-only operations are permitted. Insert, Update, Delete and any DML statements are disallowed.
                              This command allows queries to be run against the Unified CCX databases (data stores) and sysmaster database for the Unified
                              CCX Informix instance (IDS engine).

Command syntax

run uccx sql database_name sql_query
                                 		  [options]

Arguments

database_name—(Mandatory) Database on which the SQL statement is
                              			 run

sql_query—(Mandatory) The sql statement to run

Options

page—Displays the output one page at a time

file—Stores the output to a file instead of showing it on the
                              			 console. The name of the file is displayed after the completion of the
                              			 command.

Requirements

Level privilege: 0

Command privilege level: 0

Allowed during upgrade: No

Example

```
admin:run uccx sql db_cra select resourceid,resourcename from resource
RESOURCEID      RESOURCENAME
-----------------------
1        b
2        agent22
3        sacagent3
4        sacagent1
7        user
8        sacagent2
9       user agent2
10      user rtlite1
11       agent130
14       sk1
15       sk2
24      User RT Pro
```

### run uccx sp
                           	 database_name sp_name

Runs a stored procedure that is specified as a parameter on the database, which is also mentioned as a parameter. This command
                              runs only a stored procedure.

Command Syntax

run uccx sp database_name
                                 		  sp_name [options]

Arguments

database_name—(Mandatory) Database on which the stored procedure
                              		is run

sp_name—(Mandatory)
                              		The stored procedure to be run

Options

page—Displays the
                              		output one page at a time

file—Stores the
                              		output to a file instead of showing it on the console. The name of the file is
                              		displayed after the completion of the command.

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 0

Allowed
                              		during upgrade: No

Example

```
admin:run uccx sp db_cra sp_email_contact_detail('2016-12-06 18:30:00','2016-12-07 18:29:59','testemailcsq1','FinesseAgent1','')
CONTACT_ID      SEQUENCE_NUMBER CSQ_NAME        AGENT_NAME      RECEIVED        RETRIEVED       REPLIED DISCARDED       FROM_ADDRESS    REPLY_TO_ADDRESS        TO_ADDRESS      SUBJECT CONTACT_TYPE CONTACT_DISPOSITION     EMAIL_REPLY_TO  EMAIL_REPLY_CC  EMAIL_REPLY_BCC
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 D82AC14C1000015800000EFF0A4E5D8A        0       testemailcsq1   FinesseAgent1   2016-12-07 07:22:49.0   2016-12-07 07:59:45.051 2016-12-07 08:00:47.06  null    reboottest2@sky13.sm   "RebootTestUser2 Reboot." <reboottest2@sky13.sm>    reboottest1@sky13.sm   test    1       2       reboottest2@sky13.sm,reboottest1@sky13.sm

 Command successful.
```

## Utils Commands

### utils
                           	 remote_account

This
                              		command allows you to enable, disable, create, and check the status of a remote
                              		account.

Command Syntax

utils
                                    			 remote_account status

utils
                                    			 remote_account enable

utils
                                    			 remote_account disable

utils
                                    			 remote_account create username life

Arguments

username —Specifies the
                                    			 name of the remote account. The username can contain only lowercase characters
                                    			 and must be more than six characters long.

life —Specifies the life
                                    			 of the account in days. After the specified number of days, the account
                                    			 expires.

Usage Guidelines

A remote
                              		account generates a pass phrase that allows Cisco support personnel to access
                              		the system for the specified life of the account. You can have only one remote
                              		account that is enabled at a time.

Example

```
admin:utils remote_account status
Remote Support
Status         : disabled
Decode Version : 2
```

Caution

Avoid creating
                                          		  remote account usernames starting with "uccx" or "UCCX" because such usernames
                                          		  may conflict with system account names that are used internally within the
                                          		  Cisco Unified Contact Center Express server.

### utils
                           	 reset_application_ui_administrator_name

This command resets the application user interface administrator name for Serviceability, CUIC Admin property, and CUIC Administrator.

Command syntax

utils
                                 		  reset_application_ui_administrator_name

Command Modes

Administrator
                              		(admin)

Requirements

Command privilege
                              		level: 0

Allowed during
                              		upgrade: Yes

Restart the service (Cisco Unified Intelligence Center Reporting Service) on all nodes in the cluster to enable the new administrator
                                          to log in to Unified Intelligence Center.

```
admin:utils reset_application_ui_administrator_name

-------------------- utils reset_ui_administrator_name --------------------

Reset user interface administrator user name

New administrator user name:

User_1
Serviceability Administrator user name has been successfully updated to User_1

CUIC Admin property has been successfully updated to User_1

CUIC Administrator user name has been successfully updated to User_1
```

### utils
                           	 service

This command allows start, stop, activate, deactivate, list, auto-restart and restart of the following services:

System SSH

Service Manager

Entropy Monitoring Daemon

Cisco SCSI Watchdog

A Cisco DB

A Cisco DB Replicator

Cisco AMC Service

Cisco Audit Event Service

Cisco CDP

Cisco CDP Agent

Cisco CallManager Serviceability

Cisco Certificate Change Notification

Cisco Certificate Expiry Monitor

Cisco Database Layer Monitor

Cisco DRF Local

Cisco DRF Master

Cisco Finesse Tomcat

Cisco Identity Service

Cisco Log Partition Monitoring Tool

Cisco RIS Data Collector

Cisco RTMT Reporter Servlet

Cisco Syslog Agent

Cisco Tomcat

Cisco Tomcat Stats Servlet

Cisco Trace Collection Service

Cisco Trace Collection Servlet

Cisco Unified Serviceability RTMT

Cisco Finesse Tomcat

Cisco Unified CCX Administration

Cisco Unified CCX CVD Dependent Webapp

Cisco Unified CCX Cluster View Daemon

Cisco Unified CCX Configuration API

Cisco Unified CCX DB Perfmon Counter Service

Cisco Unified CCX Database

Cisco Unified CCX Engine

Cisco Unified CCX Notification Service

Cisco Unified CCX Perfmon Counter Service

Cisco Unified CCX SNMP Java Adapter

Cisco Unified CCX Serviceability

Cisco Unified CCX Socket.IO Service

Cisco Unified CCX Voice Subagent

Cisco Unified CCX WebServices

Cisco Unified Intelligence Center Reporting Service

Cisco Unified Intelligence Center Serviceability Service

Cisco Unified Serviceability RTMT

Cisco Web Proxy Service

Docker Engine

Host Resources Agent

MIB2 Agent

Platform Administrative Web Service

Platform Communication Web Service

SNMP Master Agent

SOAP -Log Collection APIs

SOAP -Performance Monitoring APIs

SOAP -Real-Time Service APIs

System Application Agent

Cisco DirSync

Cisco Serviceability Reporter

Command syntax

utils service [option]
                                 		  [service-name]

Arguments

option —The option to {start | stop | activate | deactivate | list | auto-restart | restart} a service.

service-name —The name of the service.

Requirements

Level
                              		privilege: 1

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

```
admin:utils service start Cisco Unified CCX Administration 
Service Manager is running
Cisco Unified CCX Administration[STARTING]  
Cisco Unified CCX Administration[STARTING]  
Cisco Unified CCX Administration[STARTED]  
Cisco Unified CCX Administration[STARTED]
```

### utils system
                           	 upgrade

This
                              		command allows you to install upgrades and Cisco Option Package (COP) files
                              		from both local and remote directories.

Command syntax

utils system upgrade
                                 		  [Options]

Options

initiate —Starts a new
                              		upgrade wizard or assumes control of an existing upgrade wizard. The wizard
                              		prompts you for the location of the upgrade file for Unified CCX .

status —Displays status
                              		of the upgrade

cancel —Stops the
                              		upgrade process

Example

```
admin:utils system upgrade initiate

Warning: Do not close this window without first canceling the upgrade.

Source:

 1) Remote Filesystem via SFTP
 2) Remote Filesystem via FTP
 3) Local DVD/CD
 q) quit

Please select an option (1 - 3 or "q" ):
```

Do not run utils system upgrade dataexport initiate on a Cisco VVB 15.0(1) FCS or base-release system. Cisco VVB 15.0(1) base release does not support this command. Before running
                                          the command, ensure that Cisco VVB 15.0(1) is updated with ES202511 or a later supported ES to enable the utils system upgrade dataexport initiate command.

### utils system switch-version

This command restarts and switches the system to the Unified CCX product
                              		release that is installed on the inactive partition.

Command syntax

utils system switch-version

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

When the user initiates a switch version, system restart, or system shutdown from the CLI, a warning message is displayed
                              and user confirmation is requested before Unified CCX runs the command. This command is applicable for the following scenarios:

The system detects that a switch version is in progress.

The system detects that a previous switch version was abruptly terminated.

A switch version operation is abruptly terminated  if a power reset or hard reboot is performed on the Unified CCX system
                                          when the operation is in progress.

Example

```
admin:utils system switch-version

   ** There is no inactive side available **
```

### utils uccx database dbserver
                           	 integrity

This
                              		command checks the integrity of the database server disk structures and
                              		displays results. It also checks the DB configuration integrity and performs a
                              		fix if integrity is broken. Detailed information is output to a text file. The
                              		Informix oncheck utility is used for the command.

Command Syntax

utils uccx database dbserver
                                 		  integrity

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 0

Allowed
                              		during upgrade: Yes

Example

```
admin:utils uccx database dbserver integrity
 This operation may take a few minutes to complete. Please wait...

 Output is in file: uccx/cli/DbServerIntegrity_1372844998930.txt

 Command successful.
Starting DB config integrity check
 This operation may take a few minutes to complete. Please wait...

 Output is in file: uccx/cli/DbConfigIntegrity_1372845048816.txt
 Use "file view activelog  uccx/cli/DbConfigIntegrity_1372845048816.txt" command to see output
 Command successful.
```

The
                                          		  name of the file containing the output from all the checks performed is
                                          		  automatically generated by the command script. For the filename to be unique,
                                          		  the naming format is DbServerIntegrity_<TIMESTAMP>.txt. This format
                                          		  ensures the uniqueness across processes and over time. The file path and
                                          		  filename are displayed after the completion of the operation.

### utils uccx jtapi_client update

This command updates the JTAPI Client version on the active
                              		partition on the Unified CCX box to match JTAPI version on the Unified Communications Manager. This
                              		command downloads the JTAPI Client from the Unified Communications Manager and checks whether the
                              		downloaded version needs to be installed. If the downloaded version needs to be
                              		installed, it installs the downloaded JTAPI Client and displays a
                              		message that the JTAPI Client was updated with the previous and the current
                              		versions. If the downloaded version does not need to be installed, it displays a message saying the same and displays the
                              current JTAPI Client
                              		version.

The JTAPI client update occurs only on the local node
                              		and not the second node in case of an HA deployment.

After you run this command, you must reboot the Unified CCX server and
                                          		  restart all the Unified CCX services.

Command syntax

utils uccx jtapi_client update

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:utils uccx jtapi_client update 
Node ID: 1 -- Cisco JTAPI Client versions are consistent
 Command successful.
```

### utils uccx prepend custom_classpath

This command adds the CustomJarName to the classpath ahead of the system classpath.

Caution

Command syntax

utils uccx prepend custom_classpath [CustomJarName]

Arguments

CustomeJarName —Custom jar filename to be prepended to classpath

Example

```
admin:utils uccx add custom_classpath jsafe.jar
Command successful.
```

### utils uccx switch-version
                           	 db-check

This command allows
                              		you to check whether the database was corrupted after an unsuccessful switch
                              		version due to a restart in the middle of a switch version attempt. The command
                              		displays the status of last switch version. If there is a database backup
                              		available that can be restored, it prints the time stamp of the backup and
                              		display the CLI command utils uccx switch-version
                                 		  db-recover to recover from this backup.

Command Syntax

utils uccx switch-version
                                 		  db-check

Requirements

Level privilege: 1

Command privilege
                              		level: 1

Allowed during
                              		upgrade: No

Example

```
admin:utils uccx switch-version db-check ccx DB was found to be corrupted.

Last switch version was aborted at 05/29/2012 16:18:07
05/29/2012 16:18:07|root:Switch Version 9.0.1.10000-41 to 9.0.10000-42 Aborted

There is a CCX backup with timestamp 2012-05-29 16:16:19.000000000 +0530 that was taken during a prior switch version.

!!!WARNING!!! IF YOU CHOOSE TO RECOVER FROM THIS BACKUP, ANY CHANGES DONE TO THE DATABASE AFTER THE TIMESTAMP OF THIS BACKUP WILL BE LOST.

You can run the CLI command "utils uccx switch-version db-recover" to restore the DB from this backup.
```

### utils uccx switch-version
                           	 db-recover

This command first
                              		checks whether the database was corrupted after an unsuccessful switch version
                              		due to the restart in the middle of a switch version attempt. The command
                              		displays the status of the last switch version. If there is a database backup
                              		available that can be restored, it prints the time stamp of the backup and
                              		offer an option to restore the database from this backup. If the restore option
                              		is chosen, the command completes after restoring the database from this backup
                              		and bringing up all the services.

Command Syntax

utils uccx switch-version
                                 		  db-recover

Requirements

Level privilege: 1

Command privilege:1

Allowed during
                              		upgrade: No

Example

```
admin:utils uccx switch-version db-recover CCX DB was found to be corrupted.

Last switch verison was aborted at 05/29/2012 16:18:07
05/29/2012 16:18:07|root:Switch Version 9.0.1.10000-42 Aborted

There is a CCX DB backup with timestamp 2012-05-29 16:16:19:000000000 +530 that was taken during a prior switch version.

!!!WARNING!!! IF YOU CHOOSE TO RECOVER FROM THIS BACKUP, ANY CHANGES DONE TO THE DATABASE AFTER THE TIMESTAMP OF THIS BACKUP WILL BE LOST.

Are you sure you want to continue?
Continue (y/n)?y
This operation may take a few minutes to complete. Please wait
```

### utils uccx syncusers

This command allows you to synchronize the Unified CCX user passwords with the security password.

Command syntax

utils uccx syncusers

Example

```
admin:utils uccx syncusers
Command successful.
```

### utils uccx
                           	 synctocuic

Synchronizes the
                                 		  users, teams and grants permissions to the reports and stock folders from
                                 		  Unified CCX to Unified Intelligence Center. The following are the
                                 		  configurations that are pushed from Unified CCX to Unified Intelligence Center:

Users

Teams

Stock folders

Reports

Value lists

If you make any
                                 		  changes to the above mentioned configurations in Unified Intelligence Center,
                                 		  then such changes are overwritten during the sync.

If the sync fails, then running this command or the auto sync that is part of the purge schedule will not revoke the permissions
                                             for the previously-synced users or user groups.

#### Command
                                 		  Syntax

utils uccx
                                    			 synctocuic

#### Example

```
admin:utils uccx synctocuic 
Warning:
Synchronizing all the data to cuic will take some time.
Are you sure you want to run this command?
Continue (y/n)?y
Synchronization of the data from UCCX to CUIC is in progress...
Command successful.
```

### utils uccx icd clid status

This command allows you to view the current configuration parameter values for the Caller ID (CLID) feature.

Command syntax

utils uccx icd clid status

Example

```
admin:utils uccx icd clid status
CLID Feature: Disabled
CLID Text Header: Caller Details
CLID Text Prefix: Calling Party Number :
```

### utils uccx icd clid enable

This command allows you to enable the CLID feature.

Restart the Unified CCX Engine service for the changes to take effect.

In HA deployments, run this command separately on both the Unified CCX nodes.

After upgrade, run this command again to enable the CLID feature.

Command syntax

utils uccx icd clid enable

Example

```
admin:utils uccx icd clid enable
Successfully enabled the CLID feature
Please restart the "Cisco Unified CCX Engine" service for changes 
to take effect
In case of Cisco Unified CCX HA cluster, enable the CLID feature in 
remote node as well by running the CLI command 
"utils uccx icd clid enable" on the remote node
```

### utils uccx icd clid disable

This command allows you to disable the CLID feature.

Restart the Unified CCX Engine service for the changes to take effect.

In HA deployments, run this command separately on both the Unified CCX nodes.

After  upgrade, run this command again to disable  the CLID feature.

Command syntax

utils uccx icd clid disable

Example

```
admin:utils uccx icd clid disable
Successfully disabled the CLID feature
Please restart the "Cisco Unified CCX Engine" service for changes
to take effect
In case of Cisco Unified CCX HA cluster, disable the CLID feature in 
remote node as well by running the CLI command 
"utils uccx icd clid disable" on the remote node
```

### utils uccx icd clid header

This command allows you to set the display header on the phone screen.

Restart the Unified CCX Engine service for the changes to take effect.

In HA deployments, run this command separately on both the Unified CCX nodes.

After   upgrade, run this command again to set the values for the display header.

If the header string has space, enclose the entire string in double quotes.

You can set the header string to "" if you do not want to provide any values.

Command syntax

utils uccx icd clid header <header string>

Example

```
admin:utils uccx icd clid header "Caller Details"
Successfully set the CLID text header to "Caller Details"
Please restart the "Cisco Unified CCX Engine" service for changes
to take effect
In case of Cisco Unified CCX HA cluster, set the CLID text header in 
remote node as well by running the CLI command 
"utils uccx icd clid header <header string>" on the remote node
```

### utils uccx icd clid prefix

This command allows you to set the prefix string for the calling party number displayed on the phone screen.

Restart the Unified CCX Engine service for the changes to take effect.

In HA deployments, run this command separately on both the Unified CCX nodes.

After   upgrade, run this command again to set the values for the prefix string.

If the prefix  string has space, enclose the entire string in double quotes.

You can set the prefix string to "" if you do not want to provide any values.

Command syntax

utils uccx icd clid prefix <prefix string>

Example

```
admin:utils uccx icd clid prefix "Calling Party Number : "
Successfully set the CLID text prefix to "Caller Party Number: "
Please restart the "Cisco Unified CCX Engine" service for changes
to take effect
In case of Cisco Unified CCX HA cluster, set the CLID text prefix in 
remote node as well by running the CLI command 
"utils uccx icd clid prefix <prefix string>" on the remote node
```

### utils uccx security_filter
                           	 enable

Run this command to
                              		enable Unified CCX administration security filter settings.

In HA deployments, run this
                                 		  command separately on both the Unified CCX nodes.

Command syntax

utils uccx security_filter
                                 		  enable

Requirements

Level privilege: 1

Command privilege
                              		level: 1

Allowed during
                              		upgrade: No

Example

```
admin:utils uccx security_filter enable
The status of security filter is: enabled
Please restart Unified CCX service using 
'utils service restart Cisco Tomcat' for changes to take effect. In case of Cisco Unified CCX HA cluster, set the security filter in
remote node as well.
```

### utils uccx security_filter
                           	 disable

Run this command to
                              		disable Unified CCX administration security filter settings.

In HA deployments, run this
                                 		  command separately on both the Unified CCX nodes.

Command syntax

utils uccx security_filter
                                 		  disable

Requirements

Level privilege: 1

Command privilege
                              		level: 1

Allowed during
                              		upgrade: No

Example

```
admin:utils uccx security_filter disable
The status of security filter is: disabled
Please restart Unified CCX service using 
'utils service restart Cisco Tomcat' for changes to take effect. In case of Cisco Unified CCX HA cluster, set the security filter in
remote node as well.
```

### utils uccx security_filter
                           	 status

Run this command to
                              		check the status of Unified CCX administration security filter flag.

Command syntax

utils uccx security_filter
                                 		  status

Requirements

Level privilege: 1

Command privilege
                              		level: 1

Allowed during
                              		upgrade: No

Example

```
admin:utils uccx security_filter status uccx security filter is :enabled
```

### utils uccx
                           	 dbreplication dump configfiles

Run this command to append the data of dbreplication configuration
                              		files to a text file. This command is only available in the High Availability
                              		deployment of Unified CCX.

Command syntax

utils uccx dbreplication dump configfiles

Requirements

Level privilege: 1

Command privilege level: 0

Allowed during upgrade: No

Example

```
admin:utils uccx dbreplication dump configfiles 
Command Started
Output is in file: DbConfigFiles_120813161827.txt
Use "file view activelog uccx/cli/DbConfigFiles_120813161827.txt" command to view the file
Use "file get activelog uccx/cli/DbConfigFiles_120813161827.txt" command to get the file 
Command Successful
```

### utils uccx database
                           	 healthcheck

This command runs
                              		the database health check script, which checks the health of the Unified
                                 		  CCX database.

After running this command, a health check report is generated. If any issues are found by this script then they are recorded
                              in the health check report. A solution file is also generated that consists of suggested solutions for the problems reported
                              in the health check report file.

Command syntax

utils uccx database healthcheck

Requirements

Level privilege: 1

Command privilege
                              		level: 0

Allowed during
                              		upgrade: No

Example

```
admin:utils uccx database healthcheck 
Command Started
This command may take few minutes to complete
UCCX database health report is available at: /var/log/active/uccx/cli/healthcheck.rpt
UCCX database health report suggested solutions is available at: /var/log/active/uccx/cli/healthcheck.soln
Use "file view activelog uccx/cli/healthcheck.rpt" command to view the file
Use "file get activelog uccx/cli/healthcheck.rpt" command to get the file
Use "file view activelog uccx/cli/healthcheck.soln" command to view the file
Use "file get activelog uccx/cli/healthcheck.soln" command to get the file
Command Successful
```

### utils uccx database dbperf
                           	 start

Run this command to
                              		monitor the CPU and database utilization on the Unified
                                 		  CCX server.

After successfully running this command, a successful message appears on the screen. This command runs in the background for
                              the total duration specified in the command at periodic intervals and generates a file, which consists of the details related
                              to CPU and database utilization.

Command syntax

utils uccx database dbperf start
                                 		  totalHours interval

Arguments

Interval — Period of time between the running the command / operation.

TotalHours —Total duration to run this command.

Requirements

Level privilege: 1

Command privilege
                              		level: 0

Allowed during
                              		upgrade: No

Example

```
admin: utils uccx database dbperf start 10 20
The script runs every 20 minutes over a total duration of 10 hours.
Please collect files after 10 hours
Use "file get activelog uccx/cli/dbperf_250913131546.log" to get the file
Use "file view activelog uccx/cli/dbperf_250913131546.log" to view the file
Command Successful
```

### utils uccx database dbperf
                           	 stop

Run this command to
                              		stop the current active instance of utils
                                    			 uccx database dbperf start before it runs to completion.

Command syntax

utils uccx database dbperf stop

Requirements

Level privilege: 1

Command privilege
                              		level: 0

Allowed during
                              		upgrade: No

Example

```
admin:utils uccx database dbperf stop
Execution of dbperf has been stopped
Command Successful
```

### utils ids
                           	 sync-security-config

This command is used to synchronize the security configuration files from the primary node to secondary node.

This CLI is available only on the secondary node(s) in a cluster.

#### Command
                                 		  Syntax

utils ids
                                    			 sync-security-config

#### Requirements

Level
                                 		  privilege: 0

Command
                                 		  privilege level: 0

Allowed
                                 		  during upgrade: True

#### Example

```
admin:utils ids sync-security-config
```

### utils uccx healthcheck

Run this command to perform checks on the Unified CCX system to ensure that the potential issues are detected at an early
                              stage. When you run this command, you are prompted to enter the category on which health check must be performed. For example,
                              you can select to check the Unified CCX system hardware usage to detect if it is within the threshold limit and return the
                              health check status. A report can be generated with all the plug-in details.

If you run utils uccx healthcheck all , you are not prompted to select the category. This command will run health check on all the categories.

Command Syntax

utils uccx healthcheck

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: Yes

Available Categories:

Hardware Usage

System Parameters

Database

Unified CM Configurations

#### Hardware Usage

This section provides information on the Unified CCX system hardware usage. Plug-ins of this category checks and provides
                              the Unified CCX system CPU usage, memory usage, disk space usage, and disk I/O latency status. If the hardware usage exceeds
                              the threshold limit, then the system will display the appropriate status message.

For example, if the CPU usage in the last ten minutes is within the threshold limit, an OK state is displayed. If the CPU
                              usage in the last ten minutes exceeded the threshold limit, a Not OK state is displayed with the appropriate message.

The following table lists the available plug-ins, their threshold limits and the message displayed when the threshold limit
                              is exceeded.

Plug-in

Threshold Limit

Message Displayed

CPU Usage

System CPU usage exceeds 70 percent.

The CPU usage has exceeded the threshold limit.

Memory Usage

System memory usage exceeds 70 percent.

The memory usage has exceeded the threshold limit.

Disk Space Usage

System disk space usage exceeds 70 percent.

The disk usage has exceeded the threshold limit.

Disk I/O Latency

Total time taken to write 2 MB of data (1000 sequential 2 KB synchronous writes) to the active partition exceeds 500 milliseconds.

Disk I/O exceeded the permissible limit.

Example

```
admin:utils uccx healthcheck
Healthcheck is available for the following categories:
1) Hardware Usage
2) System Parameters
3) Database
4) Unified CM Configurations
q) Quit
Select an option (1 - 4 or "q"):1
       Checking CPU Usage.................................................OK
       Checking Memory Usage..............................................OK
       Checking Disk Usage................................................OK  
       Checking Disk I/O Latency......................................Not OK
              Disk I/O exceeded the premissible limit.
Use 'file get activelog healthcheck/report_2019-11-11-09-40-04.json' command to 
download the health report.
Command Successful.
```

#### CCX Configuration

This section provides information on the Unified CCX system parameters usage. If the configured values for the following system
                                 parameters exceeds the threshold limit, then the Unified CCX system will display the appropriate status message. For example,
                                 if the configured number of agents is within the capacity limits, an OK state is displayed. If the configured number of agents
                                 exceeds the capacity limits, a Not OK state is displayed with the appropriate message.

The following plug-ins check the various configuration limits in the Unified CCX system:

Configured Agents

Configured Agents per Team

Configured CSQs

Configured Skills per Agent

Configured Outbound Campaigns

Configured Supervisors per Team

Configured Teams per Supervisor

Configured Contacts per Outbound Campaign

Configured Contact Service Queues

Configured Skills

Configured Skills per CSQ

For more information on team configuration limits, see Server Capacities and Limits section in the Solution Design Guide for Cisco Unified Contact Center Express .

#### Database

This section provides a list of plug-ins that runs to check the health of database components. The available plug-ins include
                                 the following:

CCX DB Status: This plug-in checks if the Unified CCX database service is running. If the Unified CCX database service is
                                       down, an appropriate status message is displayed.

CCX DB Replication Status: This plug-in checks if all the Unified CCX database replications are running. If the Unified CCX
                                       database replications are not in synchronization, an appropriate status message is displayed.

CCX DB Space Usage: This plug-in checks if all the three Unified CCX database (db_cra, db_cra_repository, and db_hist) usage
                                       is within the threshold limit. If any of the database usage exceeds the threshold limit, the system displays the name of that
                                       particular database along with the percentage used.

CCX Config DB tables consistency in HA: This plug-in checks if the Unified CCX configuration tables are in synchronization
                                       across the Unified CCX cluster.  If any of the configuration tables are not in synchronization, an appropriate status message
                                       is displayed.

Number of Wallboard/External clients: This plug-in checks the number of wallboards and external clients that are connected
                                       to the database. If the configured number of wallboards and external clients is within the threshold limit, an OK state is
                                       displayed. If the configured number of wallboards and external clients exceeds the threshold limit, a Not OK state is displayed
                                       with the appropriate message.

Example

```
admin:utils uccx healthcheck
Healthcheck is available for the following categories:
1) Hardware Usage
2) System Parameters
3) Database
4) Unified CM Configurations
q) Quit
Select an option (1 - 4 or "q"):3
       Checking CCX DB Status.......................................OK
       Checking CCX DB Replication Status.................................OK
       Checking CCX DB Space Usage....................................Not OK
       Reason:DB space usage has exceeded the threshold limit of 75% for the 
       following:db_hist and db_cra_repository
       Checking CCX Config DB tables consistency in HA................Not OK
       Reason:DB table(s) out of sync:Skill
              ID in configseed table out of sync:Crsuser
       Checking the number of Wallboard/External Clients..............Not OK
       Reason:Found 3(allowed:1)wallboard/external clients.
Use 'file get activelog healthcheck/report_2019-11-11-09-40-04.json' command to
download the health report.
Command Successful.
```

#### Unified CM Configurations

This section provides a list of plug-ins that can be run to check the configurations of Unified CM configured in Unified CCX.

The available plug-ins include the following:

AXL Configuration:

This plug-in validates the following:

If the AXL configurations are available in Unified CCX.

If the configured Unified CM is reachable.

If the configured Unified CM certificates stored in Unified CCX are correct.

If the AXL service is running in the configured Unified CM.

If the configured user in Unified CM has AXL API Access role.

If the configured AXL user is available in Unified CM, if the credentials are valid, or if the user is locked in Unified CM.

Telephony Provider (JTAPI) Configuration:

This plug-in validates the following:

If the Telephony Provider configuration is available in Unified CCX.

If the configured Unified CM is reachable or if the CTIManager service is running in the configured Unified CM.

If the configured Telephony Provider in Unified CCX has Standard CTI Enabled role in Unified CM.

If the configured Telephony Provider is available in Unified CM or if the configured Telephony Provider credentials are valid.

If the configured Telephony Provider is locked in Unified CM.

RmCm Provider Configuration:

This plug-in validates the following:

If the RmCm Provider configuration is available in Unified CCX.

If the configured Unified CM is reachable or the CTIManager service is running in the configured Unified CM.

If the configured RmCm Provider has the following different Access Control roles in the Unified CM:

Standard CTI Allow Call Monitoring.

Standard CTI Allow Call Recording.

Standard CTI Allow Control of Phones supporting Connected Xfer and conf.

Standard CTI Enabled.

If the configured RmCm Provider is available in Unified CM or if the credentials are valid.

If the configured RmCm Provider is locked in Unified CM.

Example

```
admin:utils uccx healthcheck
Healthcheck is available for the following categories:
1) Hardware Usage
2) System Parameters
3) Database
4) Unified CM Configurations
q) Quit
Select an option (1 - 4 or "q"):4
       Checking AXL Configuration  .......................................OK
       Checking Telephony Provider (JTAPI) Configuration..................OK
       Checking RmCm Provider Configuration...........................Not OK
       Reason:The configured RmCm Provider is not assigned with the following
       roles in Unified CM: Standard CTI Allow Call Recording
       Checking CCX Config DB tables consistency in HA................Not OK
Use 'file get activelog healthcheck/report_2019-11-11-09-40-04.json' command 
to download the health report.
Command Successful.
```

### utils cloudconnect start

Run this command to start the specified container.

Command Syntax

utils cloudconnect start container_name

Arguments

container_name - Name of the container that has to be started.

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: Yes

Example

```
admin:utils cloudconnect start dataconn
Starting the container dataconn ...
Container dataconn is started successfully.
```

### utils cloudconnect stop

Run this command to stop the specified container.

Command Syntax

utils cloudconnect stop container_name

Arguments

container_name - Name of the container that has to be stopped.

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: Yes

Example

```
admin:utils cloudconnect stop dataconn
Stopping the container dataconn ...
Container dataconn is stopped successfully.
```

### utils fips

This command enables, disables, or displays the status of FIPS 140-2 mode. By default, FIPS 140-2 mode is disabled.

utils fips { enable | disable| status }

For using FIPS 140-2 mode, consider the following points:

FIPS 140-2 mode is supported only on releases that have been through FIPS compliance.

In a HA setup, FIPS 140-2 mode must be first enabled or disabled on the publisher and then on the subscriber. Before enabling
                                    or disabling FIPS 140-2 mode on the subscriber, ensure that all the services are running on the publisher.

Ensure that SRTP is disabled before enabling or disabling FIPS 140-2 mode in Unified CCX. You can enable SRTP after enabling
                                    or disabling FIPS 140-2 mode in Unified CCX.

When FIPS 140-2 mode is enabled or disabled, the keys and certificates are regenerated, and the Unified CCX server reboots.
                                    While rebooting, the system performs the cryptographic modules integrity check, and runs certification self-tests.

After the FIPS 140-2 mode setting is enabled or disabled, the system reboots automatically. To bring the Live Data datasource
                                    online, perform the following:

Open the tomcat-trust certificate in Cisco Unified Operating System Administration

Restart the Cisco Unified Intelligence Center Reporting Service

Caution

Back up the system before and after enabling FIPS 140-2 mode.

If any of the startup self-tests fail, the Unified CCX server halts. Restart the Unified CCX server. If the startup self-test
                                          error persists, it indicates that there is a critical problem in the FIPS module and the only option is to use a recovery
                                          CD.

#### utils fips enable

Use this command to enable FIPS 140-2 mode on the system.

Before enabling security modes such as FIPS, Common Criteria, and Enhanced Security, the cluster security password must be
                                             at least 14 characters. Update the cluster security password by using the set password user security command on all nodes and then run this command.

Caution

After you enable FIPS 140-2 mode on a server, please wait until the server reboots and the phones re-register successfully
                                             before enabling FIPS 140-2 mode on the next server.

Command syntax

utils fips enable

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:utils fips enable

Security Warning: The operation will regenerate certificates for
1)Tomcat
2)IPsec

Any third party CA signed certificates that have been uploaded for the above
components will need to be re-uploaded.
If there are other servers in the cluster, please wait and do not change the
FIPS settings on any other node until the FIPS operation on this node is complete
and the system is back up and running.
*********************************************************************************
This will change the system to FIPS mode and will reboot.
*********************************************************************************

WARNING: Once you continue, do not press Ctrl+C. Canceling this operation after it
starts will leave the system in an inconsistent state; rebooting the system and
running "utils fips status" will be required to recover.
*********************************************************************************

Do you want to continue (yes/no) ? yes

Generating certificates...

Setting FIPS mode in operating system.
FIPS mode enabled.

FIPS mode enabled successfully.
********************************************************
It is highly recommended that after your system restarts,
a system backup is performed.
********************************************************
The system will reboot in a few minutes.
```

#### utils fips status

Use this command to know if FIPS 140-2 mode has been enabled on the system. When you run the utils fips status command, the system runs the certification self-tests and displays the result.

Command syntax

utils fips status

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
The system is operating in FIPS mode. Self test status:

- S T A R T ---------------------
Executing FIPS selftests
runlevel is N3
Start time: Thu Apr 9 08:50:59 IST 2020
NSS self tests passed.
Kernel Crypto tests passed.
Operating System OpenSSL self tests passed.
Libreswan self tests passed.
OpenSSL self tests passed.
CryptoJ self tests passed.
```

#### utils fips disable

Use this command to disable FIPS 140-2 mode on the system.

Command syntax

utils fips disable

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
Security Warning : The operation will regenerate certificates for
1)Tomcat
2)IPsec

Any third party CA signed certificates that have been uploaded for the above
components will need to be re-uploaded.
If there are other servers in the cluster, please wait and do not change the
FIPS settings on any other node until the FIPS operation on this node is complete
and the system is back up and running.
*********************************************************************************
This will change the system to NON FIPS mode and will reboot.
*********************************************************************************

WARNING: Once you continue do not press Ctrl+C. Canceling this operation after it
starts will leave the system in an inconsistent state; rebooting the system and
running "utils fips status" will be required to recover.
*********************************************************************************

Do you want to continue (yes/no) ? yes

Warning: All IPSEC Policies created in FIPS mode will be retained

Generating certificates...

Setting Non FIPS mode in operating system.

FIPS mode disabled successfully.
********************************************************
It is highly recommended that after your system restarts,
a system backup is performed.
********************************************************
The system will reboot in a few minutes.
=============================
```

#### Enhanced Security Mode

Enhanced Security Mode runs on a FIPS-enabled system. Unified CCX can be enabled to operate in Enhanced Security Mode, which
                                 enables the system with the following security and risk management controls:

Stricter credential policy is implemented for user passwords and password changes.

If the protocol for remote audit logging is set to TCP or UDP, the default protocol is changed to TCP. If the protocol for
                                       remote audit logging is set to TLS, the default protocol remains TLS. In Common Criteria Mode, strict hostname verification
                                       is implemented. So, it is required to configure the server with a fully qualified domain name (FQDN) which matches the certificate.

Credential Policy Updates

When the Enhanced Security Mode is enabled, a stricter credential policy takes effect for new user passwords and password
                                 changes. After Enhanced Security Mode is enabled, administrators can use the set password *** series of CLI commands to modify any of the following requirements:

The length of the password must be between 14 and 127 characters.

A password must have at least one lowercase, one uppercase, one numeral, and one special character.

Any of the previous 24 passwords cannot be reused.

Minimum age of the password is one day and maximum age of the password is 60 days.

Character sequence in the newly-generated password must differ by at least four characters from the character sequence in
                                       the old password.

### utils uccx informix_ssl

Use the utils uccx informix_ssl command with the following parameters:

status: utils uccx informix_ssl status

cert generate: utils uccx informix_ssl cert generate

cert info: utils uccx informix_ssl cert info

enable: utils uccx informix_ssl enable

disable: utils uccx informix_ssl disable

All these commands are node specific. In a HA setup, you must run them on each node.

#### utils uccx informix_ssl status

Use this command to know whether the TLS connection to the Informix database is enabled.

Command

utils uccx informix_ssl status

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example 1

```
admin:utils uccx informix_ssl status
TLS connection to the informix database is enabled
```

Example 2

```
admin:utils uccx informix_ssl status
TLS connection to the informix database is disabled
```

#### utils uccx informix_ssl cert generate

Use this command to generate a TLS certificate for the Informix database connection. When you run this command, the following
                                    input parameters are expected:

Company's Domain Name: Enter your company's domain name.

Country Code: Enter your country code.

Keystore password: Enter a password that has a minimum of six characters.

Confirm Keystore Password: Enter the password again for confirmation.

The input parameters are part of the generated TLS certificate for the Informix database connection.

Command

utils uccx informix_ssl cert generate

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:utils uccx informix_ssl cert generate
Generating TLS certificate for Informix database connection
Enter your Company's Domain Name: XYZ
Enter your Country Code: CD
Enter keystore password: ******
Confirm keystore password: ******
Password confirmed and accepted
Generating TLS certificate for Informix database connection
Certificate generated successfully
```

If the certificate is already generated, the following message is displayed:

```
Certificate is already present. Do yu want to regenerate? [yes/no]
```

If you type "yes," the certificate is regenerated. If you type "no," the command is cancelled.

#### utils uccx informix_ssl cert info

Use this command to view the details of the TLS certificate that is generated for the Informix database connection.

Command

utils uccx informix_ssl cert info

The certificate details are displayed.

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

If the certificate isn’t present, the following message is displayed:

```
The TLS certificate for the Informix database connection is not present.
```

#### utils uccx informix_ssl enable

Use this command to enable the TLS connection to the Informix database.

After enabling, the system uses the secure port 9089 along with the non-secure port 1504.

Caution

Ensure that you use this command during off-peak hours to avoid service interruptions.

Command syntax

utils uccx informix_ssl enable

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:uccx informix_ssl enable
Enabling ...
INFO: Stopping Cisco Unified CCX Database ...
Service Manager is running
Cisco Unified CCX Database [Stopping]
Cisco Unified CCX Database [Stopping]
Cisco Unified CCX Database [Stopping]
Cisco Unified CCX Database [Stopped] Command Out of Service
Cisco Unified CCX Database [Stopped] Command Out of Service
Starting Cisco Unified CCX Database ...
Service Manager is running
Cisco Unified CCX Database [Starting]
Cisco Unified CCX Database [Starting]
Cisco Unified CCX Database [Starting]

TLS connection to the Informix database has been enabled successfully.
```

If the TLS certificate for the Informix database connection isn’t generated, the following message is displayed:

```
The TLS certificate for the Informix database is not present. Before enabling the TLS connection to the Informix database, please generate the certificate.
```

If the connection is already enabled, the following message is displayed:

```
TLS connection to the Informix database is already enabled.
```

#### utils uccx informix_ssl disable

Use this command to disable the TLS connection to the Informix database.

After disabling, the system uses only the non-secure port 1504.

Caution

Ensure that you use this command during off-peak hours to avoid service interruptions.

Command syntax

utils uccx informix_ssl disable

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:uccx informix_ssl disable
Disabling ...
INFO: Stopping Cisco Unified CCX Database ...
Service Manager is running
Cisco Unified CCX Database [Stopping]
Cisco Unified CCX Database [Stopping]
Cisco Unified CCX Database [Stopping]
Cisco Unified CCX Database [Stopped] Command Out of Service
Cisco Unified CCX Database [Stopped] Command Out of Service
Starting Cisco Unified CCX Database ...
Service Manager is running
Cisco Unified CCX Database [Starting]
Cisco Unified CCX Database [Starting]
Cisco Unified CCX Database [Starting]

TLS connection to the Informix database has been disabled successfully.
```

If the connection is already disabled, the following message is displayed:

```
TLS connection to the Informix database is already disabled.
```

### utils system tls_ciphers config list

Run this command to view the list of ciphers that are available. In a high availability (HA) deployment, run this CLI command
                                 on any one of the nodes in the cluster.

Command syntax

utils system tls_ciphers config list

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:utils system tls_ciphers config list
 
TLS Cipher Configuration:

+----------------------+--------------------------------------------------+
| APR Cipher           | ALL:+HIGH:!ADH:!AECDH:!EXP:!PSK:!SRP:!LOW:!RC2     |
|                      | !3DES:!SEED:!RC4:!SSLv2:!IDEA:!CAMELLIA            |
|                      | !AES256-SHA:!ECDHE-RSA-AES256-SHA                  |
|                      | !DHE-RSA-AES256-SHA:!AES256-GCM-SHA384             |
|                      | !AES128-GCM-SHA256:!DHE-DSS-AES256-SHA:!AES128-SHA |
|                      | !RSA:!ARIA:!ECDHE-ECDSA-AES128-CCM                 |
|                      | !ECDHE-ECDSA-AES256-CCM:!ECDHE-ECDSA-AES128-CCM8   |
|                      | !ECDHE-ECDSA-AES256-CCM8                           |
|                      | !ECDHE-ECDSA-AES256-SHA384                         |
|                      | !ECDHE-ECDSA-AES128-SHA256:!ECDHE-ECDSA-AES256-SHA |
|                      | !ECDHE-ECDSA-AES128-SHA:!ECDHE-RSA-AES256-SHA384   |
|                      | !ECDHE-RSA-AES128-SHA256:!ECDHE-RSA-AES128-SHA     |
|                      | +ECDHE-RSA-CHACHA20-POLY1305                       |
|                      | +ECDHE-ECDSA-CHACHA20-POLY1305                     |
|                      | +ECDHE-RSA-AES128-GCM-SHA256                       |
|                      | +ECDHE-ECDSA-AES128-GCM-SHA256                     |
|                      | +ECDHE-RSA-AES256-GCM-SHA384                       |
|                      | +ECDHE-ECDSA-AES256-GCM-SHA384                     |
|                      | +DHE-RSA-AES128-GCM-SHA256                         |
|                      | +DHE-RSA-AES256-GCM-SHA384                         |
+----------------------+--------------------------------------------------+
+----------------------+--------------------------------------------------+
| JSSE RSA Cipher      | TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256              |
|                      | TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256        |
|                      | TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384              |
|                      | TLS_DHE_RSA_WITH_AES_128_GCM_SHA256                |
|                      | TLS_DHE_RSA_WITH_AES_256_GCM_SHA384                |
+----------------------+--------------------------------------------------+
+----------------------+--------------------------------------------------+
| JSSE ECDSA Cipher    | TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256            |
|                      | TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256      |
|                      | TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384            |
+----------------------+--------------------------------------------------+
```

### utils system tls_ciphers config export

Run this command to export the TLS cipher list configured in the tls_settings file to a specified SFTP location. In a high availability (HA) deployment, run this CLI command on all the nodes of the cluster.

Command syntax

utils system tls_ciphers config export

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:utils system tls_ciphers config export
 
You can export the TLS ciphers config data to an SFTP server location. Enter the details of the SFTP server:
 
Server:10.86.135.111
User:root
User's Password:********
Directory:/root
 
Successfully exported TLS cipher config data file: tls_settings_20240722104000
```

### utils system tls_ciphers config import

Run this command to import the TLS cipher list from a specified SFTP server location and update the configuration in the tls_settings file. In a high availability (HA) deployment, run this CLI command on all the nodes of the cluster.

Command syntax

utils system tls_ciphers config import

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:utils system tls_ciphers config import
Warning: This action will overwrite the current TLS cipher configuration.
Any changes to the TLS cipher settings can impact both the security and compatibility of the system.
Ensure that the new configuration meets all system security requirements without affecting functionality.
 
You can import the TLS ciphers config data from an SFTP server location. Enter the details of the SFTP server:
 
Server:10.86.135.111
User:root
User's Password:********
Directory:/root
Filename:tls_settings_update
 
Successfully imported TLS cipher config data file
 
Restart the system using the command 'utils system restart' for the changes to take effect
```

### utils system tls_ciphers config reset

Run this command to reset the TLS cipher configuration to the base version available with the product's standard release.
                                 This will undo any modifications made to the TLS cipher configuration, restoring it to the base version. In a high availability
                                 (HA) deployment, run this CLI command on all the nodes of the cluster.

Command syntax

utils system tls_ciphers config reset

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:utils system tls_ciphers config reset
 
Warning: Resetting the current TLS cipher configuration to the base version will impact security and compatibility.
Ensure the new configuration meets system security requirements and does not affect functionality.
 
TLS cipher configuration successfully reset to base version.
 
Restart the system using the command 'utils system restart' for the changes to take effect.
```

### utils uccx database reindex tablename

This command allows you to reindex Unified CCX tables.

Syntax

utils uccx database reindex <TABLE NAME> || [Option]

Table Name —The reindex is applicable only on the following tables:

AgentStateDetail

ContactCallDetail

AgentConnectionDetail

ContactRoutingDetail

ContactQueueDetail

TextContactDetail

Option

all —Re-indexes all the applicable tables.

Requirements

Level privilege: 4

Command privilege level: 4

Allowed during upgrade: No

Example 1

```
admin: utils uccx database reindex ContactQueueDetail
Is this a maintenance window or a low-traffic period with fewer users? (y/n):
Have you taken DRF backup? (y/n)
Reindixing table: ContactQueueDetail

Reindexingprocess completed.

To view logs, check in the following location:
/var/log/active/uccx/cli/reindex/reindex_log_050325184948.log
```

```
admin: utils uccx database reindex ContactQueueDetailh
Error: occurred during reindexing  process.
To view logs, check in the following location:
/var/log/active/uccx/cli/reindex/reindex_log_050325184949.log

Executed command unsuccessfully.

Error: Please enter a valid table name from the following list:
AgentStateDetail ContactCallDetail AgentConnectionDetail ContactRoutingDetail ContactQueueDetail all
Error:

end of the file reached
```

### utils network dns check enable

This command allows you to enable the forward and reverse lookup with DNS after successful change of IP or hostname.

Syntax

utils network dns check enable

Requirements

Level privilege: 4

Command privilege level: 4

Allowed during upgrade: No

Example

```
admin: utils network dns check enable
Executing DNS modification with argument: enable
DNS check enabled successfully
DNS enable operation completed successfully
```

### utils network dns check disable

This command allows you to disable the forward and reverse lookup with DNS during IP or hostname change. This is applicable
                                 when Unified CCX is unable to reach any of the DNS servers.

Syntax

utils network dns check disable

Requirements

Level privilege: 4

Command privilege level: 4

Allowed during upgrade: No

Example

```
admin: utils network dns check disable
Executing DNS modification with argument: disable
DNS check disabled successfully. Make sure to run "utils network dns check enable" after the network change.
DNS disable operation completed successfully
```

## File
                        	 Commands

File commands help
                           		in creating custom files that are stored in a specific directory in UCCX Filesystem.

### file uccx view

Use this
                              		command to view custom files created by Unified
                                 		  CCX scripts.

Command syntax

file uccx view custom_file
                                 		  file-spec

Arguments

file-spec —(Mandatory)
                              		The file to view. The file-spec must resolve to a single file. File-spec can
                              		contain asterisks (*) as wildcards, providing it resolves to a single file.

Options

None

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

```
admin:file uccx view custom_file test.txt
```

### file uccx list custom_file

This
                              		command lists custom files that were created by Unified
                                 		  CCX scripts.

Command syntax

file uccx list custom_file
                                 		  file-spec [options]

Arguments

file-spec —(Mandatory)
                              		The file to view. File-spec can contain asterisks (*) as wildcards.

Options

page —Pauses output

detail —Shows detailed listing

reverse —Reverses sort order

date —Sorts by date

size —Sorts by size

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

```
admin:file uccx list custom_file * detail 
08 Dec,2009 16:56:11 0 text.txt 

dir count = 0, file count = 1
```

### file uccx list
                           	 prompt_file

This command lists
                              		prompt files created for various locales.

Command syntax

file uccx list prompt_file
                                 		  file_spec [options]

Arguments

file-spec —(Mandatory)
                              		The file to view. File-spec can contain asterisks (*) as wildcard.

Options

page —Pauses output

detail —Shows detailed
                              		listing

reverse —Reverses sort
                              		order

date —Sorts by date

size —Sorts by size

Requirements

Level privilege: 0

Command privilege
                              		level: 1

Allowed during
                              		upgrade: No

Example

```
admin:file uccx list prompt_file system/G711_ULAW/en_US detail
16 May,2012 17:50:19      <dir>    AA
16 May,2012 17:50:19      <dir>    ICD
16 May,2012 17:50:19      <dir>    ICM
16 May,2012 17:50:19      <dir>    SNU
16 May,2012 17:50:19      <dir>    SSA
16 May,2012 17:50:19      <dir>    UserDialog
16 May,2012 17:50:19      <dir>    gen
05 Dec,2002 06:19:03       13,822  continue_enter_number.wav
05 Dec,2002 06:19:03        7,280  credit_of.wav
05 Dec,2002 06:19:04       18,310  did_not_hear_name.wav
05 Dec,2002 06:19:04       11,430  enter_phone_number.wav
05 Dec,2002 06:19:05       12,926  finished.wav
05 Dec,2002 06:19:05        4,448  goodbye.wav
05 Dec,2002 06:19:06        8,546  name_cancelled.wav
05 Dec,2002 06:19:06       47,572  name_confirm.wav
05 Dec,2002 06:19:07       22,990  name_not_found.wav
05 Dec,2002 06:19:08       36,142  no_phone_number.wav
05 Dec,2002 06:19:08        3,902  of.wav
05 Dec,2002 06:19:09        5,492  past.wav
05 Dec,2002 06:19:09        5,110  pound.wav
05 Dec,2002 06:19:10        8,070  spell.wav
05 Dec,2002 06:19:10       11,524  spell_again.wav
05 Dec,2002 06:19:11       12,724  spell_another.wav
05 Dec,2002 06:19:11        5,596  star.wav
05 Dec,2002 06:19:12       45,074  system_problem.wav
05 Dec,2002 06:19:12        5,038  thankyou.wav
05 Dec,2002 06:19:13        8,910  try_again.wav
05 Dec,2002 06:19:14       51,810  unrecov_error_rec.wav
05 Dec,2002 06:19:14        5,216  welcome.wav
dir count = 7, file count = 22
admin:
```

```
admin:file vvb list prompt_file system/default/vb detail
no such file or directory can be found
admin:file vvb list prompt_file system/G711_ULAW/default/vb detail
09 May,2017 22:07:43       32,110  ringback.wav
dir count = 0, file count = 1
```

### file uccx get

This command transfers the custom files created by Unified CCX scripts outside the box.

Command syntax

file uccx get custom_file file-spec [options]

Arguments

file-spec —(Mandatory) File to transfer. File-spec can contain asterisks (*) as wildcards.

Options

reltime —(Mandatory) File to transfer. File-spec can contain asteriks (*) as wildcards.

abstime —(Mandatory) Absolute time to filter.

match —Search pattern to filter.

recurs —Obtains all the files located in file-spec and subdirectories

compress —Transfers files as compressed file

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

```
admin:file uccx get custom_file text.txt abstime 00:00:12/01/08 01:00:12/30/08
```

### file uccx tail

This
                              		command will tail a custom file that was created by a Unified
                                 		  CCX script.

Command syntax

file uccx tail custom_file file-spec [options]

Arguments

file-spec —(Mandatory)
                              		File to tail.

Options

hex,[num lines],regexp
                                 		  "expression"

recent —To tail the most
                              		recently changed file in the directory.

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

Tail file
                              		starting with the last ten lines with pagination enabled:

```
admin:file uccx tail custom_file text.txt page 102005-08-03 15:01:41,248 DEBUG [main] - cmdMVL size = 0
2005-08-03 15:01:41,248 INFO [main] - adding command in level3 (password/security)
2005-08-03 15:01:41,249 DEBUG [main] - begin for level4, topVL size = 0
2005-08-03 15:01:41,250 DEBUG [main] - begin for level4, topVL size = 0
2005-08-03 15:01:41,256 DEBUG [main] - begin for level3, topVL size = 0
2005-08-03 15:01:41,257 DEBUG [main] - begin for level2, topVL size = 0
2005-08-03 15:01:41,884 INFO [main] - merging complete
2005-08-03 15:06:27,619 INFO [main] - got to save history
2005-08-03 15:06:27,620 INFO [main] - Exiting CLI
```

### file uccx dump

This
                              		command dumps the contents of a file on the Unified
                                 		  CCX custom files
                              		area.

Command syntax

file uccx dump custom_file file-spec [options]

Arguments

file-spec —(Mandatory)
                              		File to dump.

Options

hex, regexp "expression"

recent —To dump the most
                              		recently changed file in the directory

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

```
admin:file uccx dump custom_file text.txt 
23640935: Dec 06 22:59:43.407 IST Unable to process call, Exception=java.lang.NullPointerException 
23640936: Dec 06 22:59:43.407 IST java.lang.NullPointerException
```

### file uccx delete

This
                              		command deletes a custom file that was created by a Unified
                                 		  CCX script. The
                              		command deletes one or more files on the Unified
                                 		  CCX custom files
                              		area.

Files that are in
                                          		  use cannot be deleted.

Command Syntax

file uccx delete custom_file
                                 		  file-spec [options]

Arguments

file-spec —(Mandatory)
                              		File to delete. File-spec can contain asterisk (*) as a wildcard.

Options

detail, noconfirm

Requirements

Level
                              		privilege: 0

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

```
admin:file uccx delete custom_file log/*.log det noconfirmdeleting file : log/cli00001.log
deleting file : log/cli00002.log
deleting file : log/cli00003.log
deleting file : log/cli00004.log
files:       found = 4, deleted = 4
```

## High Availability
                        	 Commands

If the Unified CCX database in either of the node is down or is Out
                                          			 of Service, High Availability commands do not work.

### show uccx dbreplication tables

This command is only available in the High Availability
                              		deployment of Unified CCX. This commands list all the database tables which are
                              		involved in replication in the high availability deployment.

Command syntax

show uccx dbreplication tables [options]

Options

Page —Displays the output one page at a time

File —Stores the output to a file and displays the filename

Requirements

Level privilege: 0

Command privilege level: 0

Allowed during upgrade: Yes

Example

```
admin:show uccx dbreplication tables 
This operation may take a few minutes to complete. Please wait...

CURRENTLY DEFINED REPLICATES
-------------------------------
REPLICATE:        template_db_cra_pshree_dactyl_sub_uccx_1_2_agentstatedetail
STATE:            Active ON:g_pshree_dactyl_pub_uccx
CONFLICT:         Timestamp
FREQUENCY:        immediate
QUEUE SIZE:       0
PARTICIPANT:      db_cra:informix.agentstatedetail
OPTIONS:          transaction,ris,ats,fullrow
REPLID:           131075 / 0x20003
REPLMODE:         PRIMARY  ON:g_pshree_dactyl_pub_uccx
APPLY-AS:         INFORMIX ON:g_pshree_dactyl_pub_uccx
REPLTYPE:         Master

.............
.............
.............

REPLICATE:        template_fcrassvr_pshree_dactyl_sub_uccx_3_3_fcrascalllogweek
STATE:            Active ON:g_pshree_dactyl_pub_uccx
CONFLICT:         Timestamp
FREQUENCY:        immediate
QUEUE SIZE:       0
PARTICIPANT:      fcrassvr:informix.fcrascalllogweek
OPTIONS:          transaction,ris,ats,fullrow
REPLID:           131104 / 0x20020
REPLMODE:         PRIMARY  ON:g_pshree_dactyl_pub_uccx
APPLY-AS:         INFORMIX ON:g_pshree_dactyl_pub_uccx
REPLTYPE:         Master

 Command successful.
admin:
```

### show uccx dbreplication servers

This command is only available in the High Availability
                              		deployment of Unified CCX. This commands list all the database servers which
                              		are involved in replication in the high availability deployment and whether
                              		replication is still connected or if replication is broken.

Command syntax

show uccx dbreplication servers [options]

Options

Page —Displays the output one page at a time

File —Stores the output to a file and displays the filename

Requirements

Level privilege: 0

Command privilege level: 0

Allowed during upgrade: Yes

Example

```
admin:show uccx dbreplication servers
SERVER                 ID STATE    STATUS     QUEUE  CONNECTION CHANGED
-----------------------------------------------------------------------
10.76.253.106        110 Active   Connected       0 Apr  7 22:01:19
10.76.253.107        100 Active   Local           0
```

### utils uccx modify remote_IPAddress

This command is available only in the High Availability
                              		deployment of Unified CCX. This command updates IP address of remote node in
                              		the server. Use this command during IP address change of remote node.

Use this command only when the IP address of the other node is going
                                          		  to be changed.

After you run this command, reboot the Unified CCX server and restart all the Unified CCX services.

Command syntax

utils uccx modify remote_IPAddress
                                 		  <remote_server_old_ip_address> <remote_server_new_ip_address>

Arguments

remote_server_old_ip_address —Old IP address of the remote server

remote_server_new_ip_address —New IP address of the remote server

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:utils uccx modify remote_IPAddress 10.76.253.82 10.76.253.83
 Old Remote IP Address: 10.76.253.82
 New Remote IP Address: 10.76.253.83

This command should be executed only in case you are changing IP Address of remote server.
Are you sure you want to run this command?
Continue (y/n)?y
 Command successful.
```

### utils uccx modify remote_hostname

This command is available only in the High Availability
                              		deployment of Unified CCX. This command updates hostname of remote node in the
                              		server. Use this command during hostname change of remote node.

Use this command only when the hostname of the other node is changed.

After you run this command, reboot the Unified CCX server and restart all the Unified CCX services.

Command syntax

utils uccx modify remote_hostname <
                                 		  remote_server_old_hostname> <remote_server_new_hostname>

Arguments

remote_server_new_hostname —New hostname of the remote server

remote_server_old_hostname —Old hostname of the remote server

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:utils uccx modify remote_hostname uccx-node-1 uccx-node-2
 Old Remote Hostname: uccx-node-1
 New Remote Hostname: uccx-node-2

This command should be executed only in case you are changing Host name of remote server.
 Are you sure you want to run this command?
Continue (y/n)?y
Command Successful.
```

### utils uccx database forcedatasync

This command gets the data from the other node in the
                              		cluster, effectively overwriting the data on this node.

Command syntax

utils uccx database forcedatasync

Arguments

None

Options

None

Requirements

Level privilege: 1

Command privilege level: 0

Allowed during upgrade: No

Example

```
admin: utils uccx database forcedatasync
Are you sure you want to overwrite the local database? (y/n).
 Command successful.
```

### utils uccx setuppubrestore

This command is available only in high availability mode.

Command syntax

utils uccx setuppubrestore

Example

```
admin:utils uccx setuppubrestore
```

### utils uccx dbreplication setup

This command is available only in the High Availability deployment of Unified CCX. This command is used to set up database
                              replication. The command can be run on any node and it sets up database replication in the cluster.

Command syntax

utils uccx dbreplication setup

Options

Page —Displays the output one page at a time

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:utils uccx dbreplication setup
The DB replication for the UCCX cluster has been setup.
```

### utils uccx dbreplication status

This command is available only in the High Availability
                              		deployment of Unified CCX. This command is used to check the Unified CCX
                              		database replication status.

Command syntax

utils uccx dbreplication status

Options

None

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
utils uccx dbreplication status
SERVER                 ID STATE    STATUS     QUEUE  CONNECTION CHANGED
-----------------------------------------------------------------------
g_alpha_ha_n1_uccx      1 Active   Connected       0 Aug  8 18:45:26
g_alpha_ha_n2_uccx      2 Active   Local           0

------------------------------------------------------------------
REPLICATE                                               STATE
------------------------------------------------------------------
db_cra:informix.agentconnectiondetail                   Active
db_cra:informix.contactcalldetail                       Active
db_cra:informix.contactroutingdetail                    Active
db_cra:informix.eememailstatusdescription               Active
db_cra:informix.eemreasoncodedescription                Active
db_cra:informix.eemcontactemaildetail                   Active
db_cra:informix.eememailagentstatedetail                Active
db_cra_repository:informix.promptsfoldertbl             Active
db_cra_repository:informix.promptsfiletbl               Active
db_cra_repository:informix.grammarsfiletbl              Active
db_cra_repository:informix.documentsfiletbl             Active
db_cra_repository:informix.sysgrammarsfiletbl           Active
db_cra_repository:informix.latestsynchedtime            Active
fcrassvr:informix.fcrascalllogweek                      Inactive
fcrassvr:informix.fcrasrecordlog                        Inactive
fcrassvr:informix.latestsynchedtime                     Inactive
db_cra:informix.agentstatedetail                        Active
db_cra_repository:informix.scriptsfiletbl               Active
fcrassvr:informix.fcrascalllogtoday                     Inactive
db_cra:informix.monitoredresourcedetail                 Active
db_cra:informix.latestsynchedtime                       Active
db_cra:informix.eemactiveemail                          Active
db_cra_repository:informix.grammarsfoldertbl            Active
db_cra_repository:informix.documentsfoldertbl           Active
db_cra_repository:informix.scriptsfoldertbl             Active
fcrassvr:informix.fcrasstatelogtoday                    Inactive
db_cra:informix.contactqueuedetail                      Active
db_cra:informix.remotemonitoringdetail                  Active
db_cra:informix.eemstatedescription                     Active
db_cra:informix.eemqueueagentdetail                     Active
db_cra_repository:informix.sysgrammarsfoldertbl         Active
------------------------------------------------------------------
```

### utils uccx dbreplication templatestatus

This command is available only in the High Availability
                              		deployment of Unified CCX. This command is used to see the template status of
                              		the database replication.

Command syntax

utils uccx dbreplication templatestatus

Options

Page —Displays the output one page at a time

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:utils uccx dbreplication templatestatus
The DB replication templatestatus is as follows.
```

### utils uccx
                           	 dbreplication repair

This command is available only in the High Availability deployment of Unified CCX. You can run this command on any node. This
                              command repairs mismatched data between cluster nodes; it does not repair replication setup. The command initiates the repair,
                              which runs in the background. To monitor the status of the repair process, the user must go to the data store control center
                              in Serviceability Administration. For more information, see the Cisco Unified Serviceability Administration Guide available at: https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

Command syntax :

utils uccx dbreplication
                                 		  repair [database_name]|all

Arguments

[database_name]|all —(Mandatory) Database_name, which
                              		database to repair replication on. (Argument) all—Fix replication on all nodes.

Options

Page —Displays the
                              		output one page at a time

Requirements

Level
                              		privilege: 1

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

```
admin:utils uccx dbreplication repair all
Repair has been initiated in the background...
Please go to Data Control Center in Serviceability Admin to monitor the status of the repair.
```

### utils uccx dbreplication start

This command is available only in the High Availability
                              		deployment of Unified CCX. This command is used to start the database
                              		replication. Run this command on any node to start database replication in the
                              		entire cluster.

Command syntax

utils uccx dbreplication start

Options

Page —Displays the output one page at a time

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:utils uccx dbreplication start
The DB replication for the UCCX cluster has been started.
```

### utils uccx dbreplication stop

This command is available only in the High Availability
                              		deployment of Unified CCX. This command is used to stop database replication.
                              		Run this command on any node to stop database replication in the entire
                              		cluster.

Command syntax

utils uccx dbreplication stop

Options

Page —Displays the output one page at a time

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:utils uccx dbreplication stop
The DB replication for the UCCX cluster has been stopped.
```

### utils uccx dbreplication reset

This command is available only in the High Availability
                              		deployment of Unified CCX. This command is used to reset the database
                              		replication. Resetting replication involves the following activites, in the
                              		same order, and is equivalent to the commands presented in parentheses.

Remove database replication (utils uccx dbreplication teardown)

Setup database replication (utils uccx dbreplication setup)

Initiate a data repair process for all the databases (utils uccx
                                    			 dbreplication repair all)

Command syntax

utils uccx dbreplication reset

Options

Page —Displays the output one page at a time

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:utils uccx dbreplication reset
The DB replication for the UCCX cluster has been reset.
```

### utils uccx dbreplication teardown

This command is available only in the High Availability
                              		deployment of Unified CCX. This command is used to remove the database
                              		replication. Running this command on any node with the cluster removes
                              		database replication between all nodes.

Command syntax

utils uccx dbreplication teardown

Options

page —Displays the output one page at a time

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:utils uccx dbreplication teardown
The DB replication for the UCCX cluster has been teardown.
```

## Cisco Finesse Commands

### utils uccx finesse

Use this command to
                              		activate or deactivate only Cisco Finesse Service on each Unified CCX node in a
                              		cluster.

By default, Cisco
                              		Finesse Service is not activated during the initial component-activation phase
                              		or when the appropriate licenses are updated on a Unified CCX deployment.

Run this command
                              		only if Cisco Unified CCX Cluster View Daemon is running, or else start Cisco
                              		Unified CCX Cluster View Daemon and then run this command.

Cisco Finesse is available and can be activated only in ICD Premium and Standard licensed deployments.

In HA
                                                				deployments, run this command separately on both the Unified CCX nodes.

Command syntax

utils uccx finesse
                                 		  activate

utils uccx finesse
                                 		  deactivate

Arguments

None

Requirements

Level
                              		privilege: 1

Command
                              		privilege level: 1

Allowed
                              		during upgrade: No

Example

Activate Cisco Finesse

```
admin:utils uccx finesse activate

Unified CCX 10.0(1) does not support concurrent use of Cisco Agent/Supervisor Desktop and Cisco Finesse.

If you are using Cisco Agent/Supervisor Desktop, deactivate Cisco Finesse service.

Do you want to proceed? (yes/no) yes

Cisco Finesse activation in progress…
Cisco Finesse activated successfully.

If this is a HA deployment, run this command on both Unified CCX nodes.

admin:
```

Deactivate Cisco
                                 		  Finesse

```
admin:utils uccx finesse deactivate
Cisco Finesse deactivation in progress…
Cisco Finesse deactivated successfully.

If this is a HA deployment, run this command on both Unified CCX nodes.

admin:
```

### utils
                           	 reset_3rdpartygadget_password

Run this command to
                              		set or reset the password of the 3rdpartygadget account (where password is the
                              		new password for the account).

Use the
                              		3rdpartygadget account to upload third-party gadgets to the Cisco Unified CCX
                              		Server so that you can use the gadgets from Cisco Finesse. Before you use this
                              		account, you must set the password.

The password
                                          		  length must be between 5 and 32 characters long and must not contain spaces or
                                          		  double quotes.

Command syntax

utils
                                 		  reset_3rdpartygadget_password

Requirements

Level privilege: 1

Command privilege
                              		level: 1

Allowed during
                              		upgrade: No

```
admin: utils reset_3rdpartygadget_password
New Password:
Confirm New Password:

Updating password for 3rdpartygadget...

Password updated successfully.
admin
```

### Cisco Finesse Trace Logging

Use the following commands to toggle trace logs for Cisco Finesse, enable trace logs for Finesse IPPA, and enable debug logs
                                 for realm.

Enabling trace logging may cause an overload in the system and must be used for debugging purposes only.

utils finesse trace enable :

This command allows you to:

Enable trace logs for Cisco Finesse.

Turn on command dispatcher logs.

Enable trace logs for Finesse IPPA.

Enable debug logs for Realm.

utils finesse trace disable

This command allows you to:

Disable trace logs for Cisco Finesse.

Turn off command dispatcher logs.

Disable trace logs for Finesse IPPA.

Disable debug logs for Realm.

After execution of each command, wait for 60 seconds for the changes to take effect.

utils finesse trace status

This command allows you to displays status as:

Enabled - When all four actions are enabled.

Disabled - When all four actions are disabled.

If all actions are not enabled or disabled, a warning message is displayed.

### Finesse Log Configuration

Use the following CLI commands to add, delete, update, or view the logger configuration in the system for Finesse.

#### utils finesse log configuration add

Creates a custom log configuration in the Finesse system. The logs record information about the encountered issues of different
                                 severity levels for a specific Finesse module.

Command Syntax

utils finesse log configuration add [module] [name] [level]

Options

Adding multiple module names, log configuration names, and log configuration level values are not supported.

Log configuration with name ROOT is not allowed.

module —Unique name of Finesse module for which log configuration has to be added. The module name is case sensitive. The following
                                       are the valid Finesse modules.

admin —Finesse administration module.

audit —Finesse audit module for all administration (including Finesse admin UI and REST client) and supervisor operations.

desktop —Finesse desktop module.

diagnostics —Finesse diagnostics module.

FIPPA —Finesse IP Phone Agent (IPPA) application module.

realm —Finesse realm module.

shindig —Shindig web application module.

valve —Finesse valve module.

webservices —Finesse webservices module.

name —Package name or fully qualified class name of the Finesse application. The name is case sensitive.

level —Defines the different severity level associated with the log configuration. The following are the valid log configuration
                                       levels.

OFF —Turns off the severity level.

ERROR —Sets the severity level to error.

WARN —Sets the severity level to warning.

INFO —Sets the severity level to information.

DEBUG —Sets the severity level to debug.

TRACE —Sets the severity level to trace.

ALL —Sets the severity level to all.

Setting the log configuration level to DEBUG or TRACE impacts system performance. This must be done in consultation with Cisco
                                                   support to ensure that the modules with high log output are not be enabled with TRACE levels in production severs.

Example

The following is the sample output for creating the log configuration named com.cisco.cc.common.subsystem under the Finesse webservices module with log configuration level as DEBUG .

```
admin:utils finesse log configuration add webservices com.cisco.cc.common.subsystem DEBUG

Warning: Creating the custom log configurations may affect the performance of the Finesse system.

Press ENTER to continue. Press any other key to exit :

Creating the log configuration, please wait...

Successfully added the log configuration. Changes might take approximately 30 seconds to take effect..
```

#### utils finesse log configuration update

Updates an existing custom log configuration in the Finesse system.

Updating multiple module names, log configuration names, and log configuration level values are not supported.

Audit log configuration cannot be updated.

Command Syntax

utils finesse log configuration update [module] [name] [level]

Options

module —Unique name of Finesse module for which log configuration has to be updated. The module name is case sensitive. For more
                                       information on the Finesse modules, see utils finesse log configuration add .

name —Package name or fully qualified class name of the Finesse application. The name is case sensitive.

level —Defines the different severity level associated with the log configuration. For more information on the severity levels,
                                       see utils finesse log configuration add .

Setting the log configuration level to DEBUG or TRACE impacts system performance.

Example

The following is the sample output for updating the log configuration named com.cisco.cc.common.subsystem under the Finesse webservices module with log configuration level as TRACE .

```
admin:utils finesse log configuration update webservices com.cisco.cc.common.subsystem TRACE

Warning: Updating the log configuration level to DEBUG or TRACE may affect the performance of the Finesse system.

Press ENTER to continue. Press any other key to exit :

Updating the log configuration, please wait...

Successfully updated the log configuration. Changes might take approximately 30 seconds to take effect.
```

#### utils finesse log configuration delete

Deletes an existing custom log configuration in the Finesse system.

ROOT log configurations cannot be deleted.

Deleting multiple log configuration names are not supported.

Command Syntax

utils finesse log configuration delete [module] [name]

Options

module —Unique name of the Finesse module. The module name is case sensitive.

name —Package name or fully qualified class name of the Finesse application. The name is case sensitive.

Example

The following is the sample output for deleting the log configuration named com.cisco.cc.common.subsystem under the Finesse webservices module.

```
admin:utils finesse log configuration delete webservices com.cisco.cc.common.subsystem
Deleting log configuration, please wait...

Successfully deleted the log configuration. Changes might take approximately 30 seconds to take effect.
```

#### utils finesse log configuration list

Lists all log configurations in the Finesse system.

Command Syntax

utils finesse log configuration list

Example

The following is the sample output for all the log configuration in the Finesse system.

```
admin:utils finesse log configuration list
Requesting log configurations, please wait...
Below is the list of log configurations in Finesse.
+-----+----------------+------------------------------------------------------------------------------------------------------+---------+
| No. |     Module     |                                                  Name                                                |  Level  |
+-----+----------------+------------------------------------------------------------------------------------------------------+---------+
| 1.  | admin          | ROOT                                                                                                 | INFO    |
| 2.  | audit          | ROOT                                                                                                 | INFO    |
| 3.  | desktop        | ROOT                                                                                                 | INFO    |
| 4.  | diagnostics    | ROOT                                                                                                 | INFO    |
| 5.  | FIPPA          | ROOT                                                                                                 | INFO    |
| 6.  | realm          | ROOT                                                                                                 | INFO    |
| 7.  | shindig        | ROOT                                                                                                 | INFO    |
| 8.  | valve          | ROOT                                                                                                 | INFO    |
| 9.  | webservices    | ROOT                                                                                                 | INFO    |
| 10. | FIPPA          | org.jivesoftware                                                                                     | WARN    |
| 11. | webservices    | org.hibernate                                                                                        | INFO    |
| 12. | webservices    | com.cisco.cc.common.subsystem                                                                        | TRACE   |
+-----+----------------+------------------------------------------------------------------------------------------------------+---------+
```

### Toaster Notifications

Toaster notifications are enabled by default after a fresh installation of Cisco Finesse. Use the following CLI commands to
                                 disable, enable, and check the status of the toaster notifications:

utils finesse toaster enable [closeTimeout] : This command enables the Cisco Finesse toaster notification.

While enabling toaster notification, use the closeTimeout parameter (timeout in seconds) to set the time interval after which toaster automatically closes. If no parameter is specified,
                                       timeout is set to 8 seconds by default. The valid range for timeout activity is between 5-15 seconds. The browser must be refreshed for timeout changes to take effect.

The configured timeout for browser notifications depends on the operating system and browser settings. The timeout value is
                                                   honored in Chrome browser in Windows OS. However, the other supported browsers do not honor the configured notification timeout
                                                   value consistently.

utils finesse toaster disable : This command disables the Cisco Finesse toaster notification.

utils finesse toaster status : This command displays the status (enable or disable) of the Cisco Finesse toaster notification.

Cisco Finesse Toaster Notification does not work with Internet Explorer browser.

### Finesse IPPA Inactivity Timeout

Use the following CLI commands to enable or disable the Inactivity Timeout feature in Finesse IPPA. You must either disable
                                 the Finesse Inactivity Timeout feature or increase the timeout in the range of 120 seconds to one day (in seconds), so that
                                 the Finesse IPPA agent is not logged out if on any other screen:

utils finesse ippa_inactivity_timeout enable : This command enables Finesse IPPA Inactivity Timeout.

The default time set for inactivity timeout is 120 seconds.

utils finesse ippa_inactivity_timeout disable : This command disables Finesse IPPA Inactivity Timeout.

When inactivity timeout is disabled, you will not be logged out of Finesse IPPA, if the agent is on any other screen.

utils finesse ippa_inactivity_timeout enable inactivity_timeout : This command enables the Finesse IPPA Inactivity Timeout with timeout set to n seconds.

Minimum value of n must be 120 seconds and maximum value can be up to one day (86400 seconds).

utils finesse ippa_inactivity_timeout status : This command checks the status of Finesse IPPA Inactivity Timeout.

The Finesse IPPA Inactivity Timeout CLIs should be run on primary and secondary Finesse servers. Enabling or disabling this
                                             feature requires a restart of Cisco Finesse Tomcat, and restart must be done in the maintenance window. During upgrade, the
                                             inactivity timeout configuration is not retained and should be re-configured post upgrade.

### Supported Content Security Policy Directives

To enable this feature in Cisco Finesse, install Finesse 12.5(1) ES3 COP or higher.

Content Security Policy (CSP) is a standardized set of security directives that can inform the browser of the policies to
                                 be used to help mitigate various forms of attacks.

#### frame-ancestor

The CSP frame-ancestor policy defines the allowable locations from where the Finesse desktop can be accessed as an embedded
                                 HTML content, which can help prevent click-jacking attacks.

From Cisco Finesse Release 12.5(1) ES4 COP onward, all references to whitelist in the CLIs are changed to allowed_list .

Use the following CLI commands to view, add, or delete the frame-access sources in the response header of Cisco Finesse. This
                                 ensures that only the configured sources can embed the Cisco Finesse in an iFrame within their HTML pages.

Internet Explorer does not support frame-ancestors, and therefore will not block any websites from loading Cisco Finesse within
                                             it.

utils finesse frame_access_ allowed_list add [source1,source2] —This command adds one or more frame sources, thereby allowing the configured sources to embed the Cisco Finesse in their
                                       iFrames. Multiple sources can be provided as a comma-separated list. The source should be of the following format:

https://<fqdn>:[port]

https://IP:[port]

https://<fqdn1>:port, https://<fqdn2>:port

Wildcard character * is also supported for the FQDN and port entries, which indicates that all the legal FQDN or ports are
                                                         valid.

The maximum number of characters (cumulative) that are permissible in allowed list is 2000.

```
admin:utils finesse frame_access_ allowed_list add https://www.abc.com:8445,https://*.abc.com,https://*.abc.com:*,https://10.21.255.25

Source(s) successfully added.
Ensure Source(s) is added to the frame access list in all Finesse nodes in the cluster.

Restart Cisco Finesse Tomcat and Cisco Finesse Notification Service for the changes to take effect:
utils service restart Cisco Finesse Tomcat
utils service restart Cisco Finesse Notification Service
```

utils finesse frame_access_ allowed_list delete —This command displays an indexed list of all the configured frame sources that have been allowed to access Cisco Finesse.
                                       Enter the corresponding index number to delete a single source or all the configured sources.

```
admin:utils finesse frame_access_ allowed_list delete 

1: https://www.abc.com:8445
2: https://*.abc.com
3: https://*.abc.com:* 
4: https://10.21.255.25
a: all
q: quit

Select the index of source to be deleted [1-4 or a,q]: 1
Sources deleted successfully.

Restart Cisco Finesse Tomcat and Cisco Finesse Notification Service for the changes to take effect:
 utils service restart Cisco Finesse Tomcat
 utils service restart Cisco Finesse Notification Service
```

```
admin:utils finesse frame_access_ allowed_list list

The following source(s) are configured in the frame access list:
1: https://www.abc.com:8445
2: https://*.abc.com
3: https://*.abc.com:* 
4: https://10.21.255.25
```

### Finesse System Commands

Configure the following Cisco Finesse system CLIs:

Node Statistics

Use the following CLI command to view the run-time statistics for the current node.

To view: utils finesse node_statistics list

```
admin:utils finesse node_statistics list

Warning: Running this command frequently will affect system performance.
Press ENTER to continue. Press any other key to exit :

Wait while the statistics (updated every 5 secs) are being fetched...

The following are the runtime statistics for the current node.

Active Dialogs Count: 0

Active Tasks Count: 0

Average Configured Media per Agent Count: 0

Average Logged in Media per Agent Count: 0

Average Skill Groups per Agent Count: 0

Max Skill Groups per Agent Count: 0

Total Time for Finesse to Start (in seconds): 32

Logged in Agents on current node: 0

Unique Configured Skill Groups per Agent Count: 0
```

For more information, see RuntimeConfigInfo API Parameters section in the Cisco Finesse Web Services Developer Guide at https://developer.cisco.com/docs/finesse/ .

### Desktop Properties

Configure the desktop properties using the following CLIs for the features.

Refresh the browser for the changes to take effect.

Use the following CLI commands to enable or disable the active call details:

To enable: utils finesse set_property desktop showActiveCallDetails true

To disable: utils finesse set_property desktop showActiveCallDetails false

Use the following CLI commands to enable or disable the agent history:

To enable: utils finesse set_property desktop showAgentHistoryGadgets true

To disable: utils finesse set_property desktop showAgentHistoryGadgets false

Use the following CLI commands to enable or disable the force wrap-up reason:

This is applicable to both voice and non-voice channels.

To enable: utils finesse set_property desktop forceWrapUp true

To disable: utils finesse set_property desktop forceWrapUp false

Use the following CLI commands to show or hide the timer in wrap-up state:

This is applicable to both voice and non-voice channels.

To hide the timer in wrap-up state: utils finesse set_property desktop showWrapUpTimer false

To display the timer in wrap-up state: utils finesse set_property desktop showWrapUpTimer true

By default, the value of this property is set to true.

Use the following CLI commands to set the wrap-up timer to count down or count up the time:

This is applicable to both voice and non-voice channels.

To count up the time: utils finesse set_property desktop wrapUpCountDown false

To count down the time: utils finesse set_property desktop wrapUpCountDown true

By default, the value of this property is set to true.

Use the following CLI commands to update the desktop notification connection type as WebSockets or BOSH:

For WebSockets: utils finesse set_property desktop notificationConnectionType websocket

For BOSH: utils finesse set_property desktop notificationConnectionType bosh

By default, the connection type is WebSockets.

Use the following CLI commands to enable or disable the attachment support in Desktop Chat:

To enable: utils finesse set_property desktop desktopChatAttachmentEnabled true

To disable: utils finesse set_property desktop desktopChatAttachmentEnabled false

By default, attachments are enabled in the Desktop Chat.

Use the following CLI commands to configure the attachment size in Desktop Chat:

utils finesse set_property desktop desktopChatMaxAttachmentSize Attachment Size

For example, to set the maximum attachment size to 6 MB, use:

utils finesse set_property desktop desktopChatMaxAttachmentSize 6000000

The maximum attachment size is configurable in the range of 5 to 10 MB.

If you don't configure the maximum attachment size, by default, the maximum attachment size is set to 5 MB.

The .exe, .msi, .sh, and .bat file types are not supported by default. Use the following CLI commands to override the default
                                    list and customize the file types that won't be supported in the Desktop Chat:

utils finesse set_property desktop desktopChatUnsupportedFileTypes File Types

For example, to set the .jar and .bin as unsupported file types, use:

utils finesse set_property desktop desktopChatUnsupportedFileTypes jar,bin

Multiple file types can be added using a comma-separated string.

Automatic Desktop Login Retries

Cisco Finesse supports automatic desktop login retries when the desktop login fails due to device-related errors. The following
                                 properties allow the administrator to control how this feature behaves:

To enable: utils finesse set_property desktop enableRetryLoginFeature true

Attention

The utils finesse set_property desktop enableRetryLoginFeature true command is not enabling automatic desktop login retries. So, to enable automatic desktop login retries, use the following
                                                   command:

utils finesse set_property desktop retryLoginAfterLogoutPhoneFailure true

To view the status of automatic desktop login retries, use the following command:

utils finesse show_property desktop retryLoginAfterLogoutPhoneFailure

To disable the automatic desktop login retries, use the following command:

utils finesse set_property desktop enableRetryLoginFeature false

If this feature is enabled, you can define the retry attempts and intervals.

To set the number of retry attempts: utils finesse set_property desktop loginFailureRetryAttempts <value>

The maximum retry attempts are 10. Default value is 3.

To set intervals: utils finesse set_property desktop loginFailureRetryInterval <value>

The login retry has a configurable amount of delay between each retry to allow the device to recover. The minimum and maximum
                                             interval between retries is 15-180 seconds. Default value is 60 seconds.

Reducing the retry interval increases the load on the system when there is a system-wide outage of devices.

By default, the value of this property is set to true.

Use the following CLI commands to enable or disable the keyboard shortcuts for the Cisco Finesse agent and supervisor desktop:

To enable: utils finesse set_property desktop enableShortCutKeys true

To disable: utils finesse set_property desktop enableShortCutKeys false

By default, the value of this property is set to true.

Use the following CLI commands to enable or disable the drag-and-drop and resize features for a gadget or component in the
                                    Cisco Finesse desktop:

To enable: utils finesse set_property desktop enableDragDropAndResizeGadget true

To disable: utils finesse set_property desktop enableDragDropAndResizeGadget false

By default, the value of this property is set to false. For more information on using the drag-and-drop and resize features,
                                    see the Cisco Finesse Agent and Supervisor Desktop User Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-user-guide-list.html .

Use the following CLI commands to configure the OU-based user search for the base LDAP context for desktop chat in HCS for
                                    CC:

To set field key: utils finesse set_property desktop desktopChatOUSearchFieldKey <value>

To set field value: utils finesse set_property desktop desktopChatOUSearchFieldValue <value>

By default, the whole LDAP base context is configured in Cisco Unified Communications Manager IM and Presence Service LDAP
                                    search settings. For more details on desktop search see, Desktop Chat Server Settings .

The following example displays the search criteria set for chat users who belong to specific OU.

```
admin:utils finesse set_property desktop desktopChatOUSearchFieldKey "OU"

Property successfully updated.
Ensure property is updated in all Finesse nodes in the cluster.

No service restart required. Ensure browser is refreshed for the changes to take effect.

admin:utils finesse set_property desktop desktopChatOUSearchFieldValue "chat"

Property successfully updated.
Ensure property is updated in all Finesse nodes in the cluster.

No service restart required. Ensure browser is refreshed for the changes to take effect.
```

Use the following CLI commands to enable or disable the preloading of the secondary server resources from the alternate side
                                    during desktop sign in:

To enable: utils finesse set_property desktop preLoadSecondaryResources true

To disable: utils finesse set_property desktop preLoadSecondaryResources false

The preloaded resources are images , CSS , JS , and HTML . The preloading reduces latency and improves performance during desktop failover. By default, the value of this property
                                    is set to true.

Security Banner Message for Desktop Users

Cisco Finesse supports custom banner messages in the desktop Sign In page. The administrator defines the banner message for
                                 Cisco Finesse desktop users so that they are aware of the security policy while using Cisco Finesse. The banner message can
                                 have a maximum of 220 characters. It supports both alphanumeric and special characters. By default, the banner message is
                                 not displayed.

To add the security banner message to the desktop Sign In page: utils finesse set_property desktop securityBannerMessage <value>

The following example displays the sample security banner that is defined for desktop Sign In page.

```
admin:utils finesse set_property desktop securityBannerMessage "IMPORTANT: Finesse may only be accessed by authorized users!"

Property successfully updated.
Ensure property is updated in all Finesse nodes in the cluster.

No service restart required. Ensure browser is refreshed for the changes to take effect.
```

To remove the security banner message in the desktop Sign In page: utils finesse set_property desktop securityBannerMessage ""

Cisco Finesse Administration Console and Cisco Finesse desktop now support messages configured in Cisco Unified OS Administration
                                             by using the custom logon message feature. From Unified CCX Release 12.5(1)SU1, it's recommended that you use the custom logon
                                             message feature as an alternative to the security banner message feature to convey important information to Cisco Finesse
                                             desktop users and administrators. For more information about setting up custom logon message, see the Set Up Customized Logon Message section in the Cisco Unified Operating System Administration Guide for Cisco Unified CCX and Cisco Unified IP IVR at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html .

Enable High Contrast Look and Feel

By default, Cisco Finesse Desktop uses high contrast colors in icons, buttons, text elements, and so on to improve the visibility
                                 of desktop elements.

Use the following CLI commands to enable or disable the high contrast colors in Desktop:

To enable: utils finesse set_property desktop enhanceContrast true

To disable: utils finesse set_property desktop enhanceContrast false

#### Dual-Tone Multi-Frequency (DTMF) Desktop Behavior

To enable this CLI in Cisco Finesse, install Cisco Finesse 12.5(1)ES2 COP or higher.

The Wrap-Up button and the call control buttons, Hold , Transfer , Consult , and End are disabled across all calls when DTMF Keypad is opened, and until the responses to all DTMF requests are completed or have timed out.

DTMF Pending Requests Threshold Count

When the network or the server is slow to respond, then the response to DTMF requests are delayed. DTMF keypad prevents new
                                    operations when more than a configured number of outstanding responses are pending. The default value is 20.

To configure the DTMF threshold count for pending requests: utils finesse set_property desktop pendingDTMFThresholdCount <value>

```
admin:utils finesse set_property desktop pendingDTMFThresholdCount 15

Property successfully updated.
Ensure property is updated in all Finesse nodes in the cluster.

No service restart required. Ensure the desktop browser is refreshed for the changes to take effect.
```

DTMF Request Timeout

Cisco Finesse waits for a configured time for each DTMF request. The default timeout is 5 seconds.

To configure the DTMF timeout for pending requests: utils finesse set_property desktop dtmfRequestTimeoutInMs <value>

The timeout value must be entered in milliseconds.

```
admin:utils finesse set_property desktop dtmfRequestTimeoutInMs 4000

Property successfully updated.
Ensure property is updated in all Finesse nodes in the cluster.

No service restart required. Ensure the desktop browser is refreshed for the changes to take effect.
```

#### Maintenance Mode

When Cisco Finesse maintenance mode is initiated in Unified CCE deployments using Agent PG 12.5 or lower, the agents' part
                                 of the failover experiences a state change of Ready or NotReady as configured in the property agentStateAfterMigration . Use the following CLI commands to control the agent state when migrating to the secondary Cisco Finesse node during maintenance
                                 mode. By default, the agentStateAfterMiigration value is Ready , which can be changed using the following command:

utils finesse set_property desktop agentStateAfterMigration NotReady

If the default state of agents after migration is set as NotReady , administrator has to define the NotReady reason code. The following command is an example to set 5448 as the NotReady reason code, which will be applied while migrating to the alternate side:

utils finesse set_property desktop migrationNotReadyReasonCode 5448

These commands are not applicable when Cisco Finesse is connected to CTI versions that are greater than or equal to 12.6.

#### WebProxy Service

WebProxy Service acts as a transparent reverse proxy between external clients and the Finesse service. It provides SSL termination
                                    and caching services to the Finesse server to reduce latency and improve performance.

Configuration changes done on the Finesse server may not be immediately available to the clients due to the intermediary webproxy
                                    cache. The administrator can clear the intermediary webproxy cache using utils webproxy cache clear .

WebProxy cache is automatically cleared when you restart the Finesse Tomcat service. Static resources (images and scripts),
                                    Shindig gadget XML, and resources are cached until the Finesse Tomcat service is restarted or explicitly cleared by the administrator.

For more information on REST API Response Caching, see REST API Developer Guide at https://developer.cisco.com/docs/finesse/ .

The logging level of the WebProxy Service is managed using the web proxy log-levels CLI.

WebProxy Service CLIs are node-specific and must be run on all nodes in the cluster.

Proxy cache bypassing reduces performance and must be used for debugging purposes during the gadget development or troubleshooting.

Server cache for the Finesse API can be bypassed by including bypassServerCache=true as a query parameter in the request or clear server cache using utils webproxy cache clear .

Server cache for the Finesse desktop can be bypassed by including bypassServerCache=true&nocache as a query parameter in the desktop URL.

##### utils webproxy cache clear

This command clears the cache from the WebProxy Service.

Command Syntax

utils webproxy cache clear { all | | | webproxy | | | desktop | | | rest | | | shindig }

Options

all —Clears all the configured caches.

webproxy —Clears the default webproxy cache.

desktop —Clears the desktop cache. The desktop cache contains static HTML, CSS, scripts, and icons used in the Finesse desktop.

rest —Clears the REST APIs cache. The REST API responses cached are:

MediaDomain

TeamResource APIs include ReasonCodes, WrapUpReasons, MediaPropertiesLayouts, PhoneBooks, and WorkFlows. The responses of
                                                   the TeamResource API are cached at the team-level.

shindig —Clears the Shindig cache. The Shindig cache contains XML gadget definition (ifr request-response) and gadget resources (concat
                                             request-response).

notification_service —Clears the Notification Service cache. The Notification Service cache contains scripts and HTML used by the Finesse desktop
                                             to connect to notification service.

authmode —Clears the UserAuthMode API cache.

Command Modes

Administrator (admin)

Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified CCE, Unified CCX, and Packaged CCE

Example

```
admin:utils webproxy cache clear desktop
Successfully cleared desktop cache
```

##### set webproxy access-log-level

This command sets the log-level for the access logs generated by the WebProxy Service. The access logs record information
                                       about all external requests that reach the proxy. The requests are logged in the access log after the request is processed.

Command Syntax

set webproxy access-log-level { off | | | info | | | debug }

Options

off —Turns off the logging into the access logs of the WebProxy Service.

info —Sets the log-level for access logs of the WebProxy Service to information. This captures the data of each request such as
                                             time, client, host, user, and so on.

debug —Sets the log-level for access logs of the WebProxy Service to debug. This captures the detailed data of each request for
                                             debugging.

Setting the access logs to debug impacts performance. Hence, avoid using in the production deployment.

Command Default

The default value is off .

Command Modes

Administrator (admin)

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified CCE, Unified CCX, and Packaged CCE

Example

```
admin:set webproxy access-log-level off
Webproxy access log-level is turned off
```

```
admin:set webproxy access-log-level info
Successfully set webproxy access log-level to info 
Service restarted
```

##### set webproxy log-severity

This command sets the severity of the error logs that are generated by the WebProxy Service. The error logs record information
                                       about encountered issues of different severity levels.

Command Syntax

set webproxy log-severity { debug | | | warn | | | error | | | crit | | | alert | | | emerg }

Options

debug —Sets the severity level to debug.

Setting the error logs to debug impacts performance. Hence, avoid using in the production deployment.

warn —Sets the severity level to warning.

error —Sets the severity level to error.

crit —Sets the severity level to critical.

alert —Sets the severity level to alert.

emerg —Sets the severity level to emergency.

Command Default

The default value is warn .

Command Modes

Administrator (admin)

Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified CCE, Unified CCX, and Packaged CCE

Example

```
admin:set webproxy log-severity warn
Successfully set webproxy log severity to warn 
Service restarted
```

##### show webproxy access-log-level

This command displays the configured log-level for the access logs of the WebProxy Service.

Command Syntax

show webproxy access-log-level

Command Modes

Administrator (admin)

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified CCE, Unified CCX, and Packaged CCE

Example

```
admin:show webproxy access-log-level
Current webproxy access log-level is: info
```

##### show webproxy log-severity

This command displays the configured severity level for the error logs of the WebProxy Service.

show webproxy log-severity

###### Command Modes

Administrator (admin)

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified CCE, Unified CCX, and Packaged CCE

###### Example

```
admin:show webproxy log-severity
Current webproxy log-severity is: warn
```

### Security Properties

Configure the security properties using the following CLIs for the features.

The CLIs require Cisco Finesse Tomcat restart except for desktop related properties.

#### Enable or Disable Plain XMPP Socket—Port 5222

Use the following CLI commands to enable or disable the Cisco Finesse Notification Service plain XMPP port (5222). This port can be enabled only if you have third-party solutions that connect
                                 directly to the Cisco Finesse Notification Service over plain Transmission Control Protocol (TCP) connection. This port is not required for the Finesse
                                 desktop or BOSH/WebSocket based integrations. By default, the port is disabled.

To enable: utils finesse set_property webservices enableInsecureOpenfirePort true

To disable: utils finesse set_property webservices enableInsecureOpenfirePort false

#### Enable or Disable Secure XMPP Socket—Port 5223

Use the following CLI commands to enable or disable the external access to the Cisco Finesse Notification Service TCP-based XMPP port (5223). The port must be enabled for external client connectivity only if you have
                                 third-party solutions that connect directly to the Cisco Finesse Notification Service over this port. By default, the port is enabled (value is set to true ).

When the port is enabled, it can be accessed by the Cisco Finesse nodes (primary and secondary) and by external clients. When
                                 the port is disabled, it cannot be accessed by external clients.

To enable: utils finesse set_property webservices enableExternalNotificationPortAccess true

To disable: utils finesse set_property webservices enableExternalNotificationPortAccess false

Restart Cisco Finesse Tomcat and Cisco Finesse Notification Services for the
                                             changes to take effect.

#### Restricting Access to the External XMPP Notification Port 5223

To enable this CLI in Cisco Finesse, install Finesse 12.5(1) ES4 COP or higher.

Use the following CLI commands to restrict the IP addresses from accessing the TCP-based XMPP notification port (5223) available
                                 for external client connectivity. You can add, delete, or view the configured IP addresses only when the enableExternalNotificationPortAccess property is enabled on all the Finesse nodes in the cluster.

These restrictions do not affect the desktop XMPP notification port 7443.

To enable access to port 5223 use the CLI command utils finesse set_property webservices enableExternalNotificationPortAccess true .

utils finesse notification external_port_access add [ip1,ip2,ip3] —This command adds one or more IP addresses to the list of hosts that are configured to access Cisco Finesse XMPP notification
                                       port 5223. Multiple IP addresses can be provided as a comma-separated list. Wildcard character * is not supported.

Example

```
admin:utils finesse notification external_port_access add 10.10.10.21,10.10.255.25

Successfully added 2 IP address(es). Ensure that the IP address(es) are added,
and verify that external notification port access is enabled in all the Finesse nodes in the cluster.
Please refer to 'utils finesse show_property webservices enableExternalNotificationPortAccess'.

Restart Cisco Finesse Notification Service for the changes to take effect:
utils service restart Cisco Finesse Notification Service
```

utils finesse notification external_port_access delete —This command deletes one or more IP addresses from the list of hosts that are configured to access Cisco Finesse XMPP notification
                                       port 5223. Multiple IP addresses can be provided as a comma-separated list.

Example

```
admin:utils finesse notification external_port_access delete 10.10.10.21,10.10.255.25

Successfully deleted 2 IP address(es). Verify that the IP address(es) are deleted in all the Finesse nodes in the cluster.

Restart Cisco Finesse Notification Service for the changes to take effect:
utils service restart Cisco Finesse Notification Service
```

utils finesse notification external_port_access delete_all —This command deletes all the configured IP addresses allowed to access the Cisco Finesse XMPP notification port 5223.

Example

```
admin:utils finesse notification external_port_access delete_all

Do you want to delete all IP address(es) (y/n): y

Successfully deleted all IP address(es). Verify that the IP address(es) are deleted in all the Finesse nodes in the cluster.

Restart Cisco Finesse Notification Service for the changes to take effect:
utils service restart Cisco Finesse Notification Service
```

utils finesse notification external_port_access list —This command lists all the configured IP addresses allowed to access the Cisco Finesse XMPP notification port 5223.

Example

```
admin:utils finesse notification external_port_access list

The following IP address(es) are configured to access the notification port:
10.10.10.21
10.10.255.25

External notification port access is disabled in the present node. Verify that is enabled in all the Finesse nodes in the cluster.
Please refer to 'utils finesse show_property webservices enableExternalNotificationPortAccess'.
```

#### Enable or Disable Enforcement of X.509 Certificate Trust Validation

Use the following CLI commands to enable or disable the validation of the X.509 CA or the selfsigned certificate. From Release
                                 12.5(1) onwards, Cisco Finesse validates SSL certificates of all the servers (CUCM and Customer Collaboration Platform ) it communicates. This requires the custom CA providers or the selfsigned certificates of the server it communicates to be
                                 present in the Cisco Finesse Tomcat trust store. If the certificates are not added into the Cisco Finesse trust store, then
                                 certain interactions can fail. It is advised to add the certificates into the Cisco Finesse trust store. If any user chooses
                                 to ignore the validation, enforcement can be turned off. This CLI allows users to disable or enable validation. By default,
                                 the validation is turned on.

To enable: utils finesse set_property webservices trustAllCertificates true

To disable: utils finesse set_property webservices trustAllCertificates false

### Cross-Origin Resource Sharing (CORS)

In a fresh install of Cisco Finesse, CORS mode is in a permissive state ( enable_all ) by default, which permits CORS preflight requests from browser-based applications from any domain. You can configure the
                                 CORS mode to be more restrictive by charging the mode to enable and by adding the required browser origins to be allowed using the following CORS CLIs.

Important

After you make changes to the CORS status or to the allowed origin list, restart Cisco Finesse Tomcat and Notification Services
                                             for the changes to take effect.

utils finesse cors enable : This command allows CORS for Cisco Finesse APIs and OpenFire requests for allowed origin list. It responds to browser CORS
                                       preflight requests and allows valid domains to make Finesse API/OpenFire requests.

Use the utils finesse cors allowed_origin CLI to customize the allowed origin list.

Any custom headers used in the CORS requests must be added using utils finesse cors allowed_headers CLI.

utils finesse cors enable_all : This command allows all origins to make cross domain requests. It responds and allows CORS preflight requests from any domain
                                       to make Finesse API/OpenFire requests.

This isn’t a secure configuration and is included only to support backward compatibility.

utils finesse cors disable : This command restricts CORS for Cisco Finesse APIs and OpenFire requests. It disallows or prevents CORS preflight requests
                                       from any external domain to make Finesse API and OpenFire requests.

If the allowed origin list is already present, the list is preserved and used when CORS is enabled. The CLI changes are reflected
                                                   only after you clear your cache and close and reopen the browser.

utils finesse cors status : This command displays the CORS status (enable_all, enabled, or disabled) on the console.

For allowing any other header, the following set of CLI commands are added to enable CORS for both Cisco Finesse and OpenFire
                                 and to configure the allowed origin list:

utils finesse cors allowed_origin list : This command lists all the origins in the allowed origin list.

utils finesse cors allowed_origin add : This command adds origins to the allowed origin list. Origins can be added by using a comma-separated string. For example:

utils finesse cors allowed_origin add https ://origin1.com:[port]

utils finesse cors allowed_origin add https ://origin1.com: [port], https ://origin2.com:[port]

The wildcard character star (*) isn’t a valid origin in the allowed origin list.

The maximum number of characters (cumulative) that are permissible in allowed origin is 4000.

utils finesse cors allowed_origin delete : This command deletes origins from the allowed origin list.

Delete lists all the origins in the allowed origin list. The origins can be deleted by selecting the appropriate ones from
                                                   the list. For example:

utils finesse cors allowed_origin delete

1: http://google.com

2: https://www.cisco.com

3: https://def.com

4: https://abc.com:7777

a: all

q: quit

Select the index of origin(s) to be deleted [1-4 or a,q]

By default the following headers are allowed and exposed:

allowed_headers : Content-Type, X-Requested-With, accept, Origin, Authorization, Access-Control-Request-Method, Access-Control-Request-Headers,
                                       requestId, Range.

exposed_headers : Access-Control-Allow-Origin, Access-Control-Allow-Credentials, Access-Control-Allow-Methods, Access-Control-Allow-Headers,
                                       Access-Control-Max-Age.

These headers can’t be modified. Custom headers can be added or removed using the following CLIs:

utils finesse cors allowed_headers list : This command lists all the allowed headers for CORS. The list is used to validate incoming requests to Finesse.

utils finesse cors allowed_headers add : This command adds one or more allowed headers for CORS. Multiple headers can be added as a comma-separated string. For example:

utils finesse cors allowed_headers add header1

utils finesse cors allowed_headers add header1,header2,header3

The wildcard character star (*) isn’t supported.

utils finesse cors allowed_headers delete : This command lists the choices for deleting the allowed headers. The choice should be an index as displayed in the list
                                       of allowed headers. The list provides the option to delete a single header or all configured custom headers. For example:

utils finesse cors allowed_headers delete

1: header1

2: header2

a: all

q: quit

Select the index of the allowed header to be deleted [1-2 or a,q]: 1

utils finesse cors exposed_headers list : This command lists all the exposed headers for CORS. The list will be used by the browser to validate the accessible headers
                                       in the response.

utils finesse cors exposed_headers add : This command adds one or more exposed headers for CORS. Multiple headers can be added by a comma-separated string. For example:

utils finesse cors exposed_headers add header1

utils finesse cors exposed_headers add header1,header2,header3

The wildcard character star (*) isn’t supported

utils finesse cors exposed_headers delete : This command lists the choices for deleting the exposed headers. The choice should be an index as displayed in the list
                                       of allowed headers. The list provides option to delete a single header or all configured custom headers. For example:

utils finesse cors exposed_headers delete

1: header1

2: header2

a: all

q: quit

Select the index of the exposed header to be deleted [1-2 or a,q]: 1

All CLIs are node specific and must be run on all nodes in the cluster.

### Gadget Source Allowed List

Shindig proxies requests from the Finesse desktop to external servers and this introduces the possibility of server side request
                                 forgery (SSRF). To prevent SSRF, you can choose to allow outgoing connections for specified sources to be used in the gadgets
                                 by adding URLs to the allowed list. Note that this functionality is disabled by default for Cisco Finesse.

Use the following CLIs to enable or disable Gadget Source allowed list functionality and to configure source(s) in the allowed
                                 list:

From Cisco Finesse Release 12.5(1) ES4 COP onward, all references to whitelist in the CLIs are changed to allowed_list .

utils finesse gadget_source_check enable : This command enables allowed list for Cisco Finesse.

utils finesse gadget_source_check disable : This command disables allowed list for Cisco Finesse.

utils finesse gadget_source_check status : This command prints the allowed list status (enabled or disabled) on Cisco Finesse console.

utils finesse gadget_source_check allowed_list list : This command lists all the source(s) in the allowed list.

utils finesse gadget_source_check allowed_list add : This command adds source(s) to the allowed list. For example,

utils finesse gadget_source_check allowed_list add https://www.abc.com:8445 .

utils finesse gadget_source_check allowed_list add https://www.abc.com:8445, http://www.abc.com.

Wildcard character * is not supported.

The allowed list feature does not perform hostname resolutions. The format of the allowed list entry should match the format
                                             in which the gadget requests for a resource.

If utils finesse gadget_source_check is enabled, you must add the CUIC URLs to utils finesse gadget_source_check allowed_list for the stock gadgets to load. For example,

utils finesse gadget_source_check enable

utils finesse gadget_source_check allowed_list add https://<CUIC_Pub_FQDN>

utils finesse gadget_source_check allowed_list add https://<CUIC_Pub_FQDN>:8444

utils finesse gadget_source_check allowed_list add https://<CUIC_Sub_FQDN>

utils finesse gadget_source_check allowed_list add https://<CUIC_Sub_FQDN>:8444

If you do not add the CUIC URLs, Finesse Desktop fails to load and an appropriate error message is displayed.

utils finesse gadget_source_check allowed_list delete : This command deletes source(s) from the allowed list. For example:

utils finesse gadget_source_check allowed_list delete

1: http://origin1:8080

2: https://origin2:7777

a: all

q: quit

Select the index of origin to be deleted [1-2 or a,q]: 1

All CLIs are node-specific and must be run on all nodes in the cluster.

After any changes are done to gadget source status or to the allowed list, restart Cisco Finesse Tomcat for changes to take
                                             effect.

### Log Collection Schedule

Use the following CLIs to create, list, and delete automatic desktop log collection schedules for agents and supervisors.
                                 This can also be used for debugging purposes.

utils finesse desktop_auto_log_collection create : This command creates a schedule that collects the agent's browser logs. You can create up to five log collection schedules
                                 for up to 15 agents.

While creating the log schedule, specify the agent IDs, log collection interval, and duration up to when the logs are to be
                                 collected.

The log collection interval and the duration have to be between 30 to 900 seconds. The logs that are collected during the
                                 schedule are received in a .zip file format. The logs are collected at: /opt/cisco/desktop/logs/clientlogs .

Example:

```
admin:utils finesse desktop_auto_log_collection create

Initializing command line interface...
Checking Cisco Finesse Tomcat status...

Enter agent IDs to continue. (Maximum 15 agents) [Example : 1001001,1001002] : 1001002
Agent IDs entered: 1001002
Enter duration in seconds.(value between 30 and 900) : 240
Duration entered: 240
Enter interval in seconds.(value between 30 and 240) : 60
Interval entered: 60

Successfully scheduled client log collection for the specified agent(s).

Ensure the same is enabled in all the Finesse nodes in the cluster..
```

utils finesse desktop_auto_log_collection list : This command lists all active log collection schedules.

Example:

```
admin:utils finesse desktop_auto_log_collection list

Initializing command line interface...
Checking Cisco Finesse Tomcat status...
These are the live log collection schedules:

Schedule ID:1 Created At: Thu Jun 6 23:23:53 PDT 2019
Duration: 240 seconds
Frequency: 60 seconds
Agent Ids: 1001002
```

utils finesse desktop_auto_log_collection delete : This command deletes the active log collection schedules. When this command is run, all the active log collection schedules
                                 are displayed and you are prompted to enter the Schedule ID that you want to delete.

Example:

```
admin:utils finesse desktop_auto_log_collection delete

Initializing command line interface...
Checking Cisco Finesse Tomcat status...
These are the live log collection schedules:

Schedule ID:1 Created At: Thu Jun 6 23:23:53 PDT 2019
Duration: 240 seconds
Frequency: 60 seconds
Agent Ids: 1001002
Enter schedule ID to delete (enter 'all' to delete all): 1
Schedule ID entered: 1

Successfully deleted the log collection with schedule id : 1
```

### View Property

Use the following CLIs to view the property values across all property files.

utils finesse show_property fippa property_name : To view the specified Finesse IPPA property's value.

utils finesse show_property desktop property_name : To view the specified desktop property's value.

utils finesse show_property webservices property_name : To view the specified web service property's value.

utils finesse show_property admin securityBannerMessage : To view the specified banner message for the administrator Sign In page.

The View property CLIs do not support multiple values.

### Update Property

Use the following CLIs to update the property values across all property files.

utils finesse set_property desktop property_name property_value : To update an existing property value used by the Finesse desktop service.

utils finesse set_property fippa property_name property_value : To update an existing property value used by the Finesse IPPA service.

utils finesse set_property webservices property_name property_value : To update an existing property value used by the Finesse web service.

utils finesse set_property admin adminSecurityBannerMessage : To update an existing property value used by the Finesse administrator for the security banner message.

### ConnectedUsersInfo

Use the following CLI command to view the list of users connected to the Cisco Finesse server where the CLI is run.

utils finesse show_connected_users summary

Provides the summary information about the connected users in the Cisco Finesse server where the CLI is run.

If the above command is run, it lists the total number of users connected to the Cisco Finesse server where the CLI is run
                                 along with the number of users connected through Cisco Finesse Desktop, Finesse IP Phone, and third-party desktops.

Example is as follows:

```
admin: utils finesse show_connected_users summary
Total Connected Users: 2
Desktop Users: 2
FIPPA Users: 0
Third-party Users: 0
Users connected to Finesse via LAN/WAN: 1
Users connected to Finesse via Proxy: 1
To view the complete list of signed-in users, log in to the Cisco Finesse
Administration Console, and navigate to the Connected Agents tab.
```

utils finesse show_connected_users detail

Provides the detailed information about the connected users in the Cisco Finesse server where the CLI is run.

If the above command is executed, it lists the total number of users connected to the current Cisco Finesse server along with
                                 the number of users connected through Cisco Finesse Desktop, Finesse IP Phone, and third-party desktops with the agent details.

Example is as follows:

```
admin: utils finesse show_connected_users detail
Total Connected Users: 3
Desktop Users: 2
FIPPA Users: 1
Third-party Users: 0
 
Desktop Users List [1001002, 1001003]
FIPPA Users List [1001004]
```

## Cisco Unified Intelligence Center Commands

### show cuic component-status

This command shows the status of the Unified Intelligence Center components. The Component name parameter is mandatory.

Command syntax

show cuic component-status Component name

Component name

CuicStatus —Shows status of Unified Intelligence Center web engine and the DB replication

DBRepStatus —Shows status of database replication on this node

DBStatus —Shows the database status

Requirements

Level privilege: 0

Command privilege level: 0

Allowed during upgrade: No

Example

```
admin:show cuic component-status CuicStatus
```

### show cuic properties

This command shows information about Cisco Unified Intelligence Center properties.

Command syntax

show cuic properties [options]

Options

host-to-ip —Current host-to-IP translation for the Cisco Unified Intelligence Center databases in the cluster

purge-retention —Number of days data is retained in the Cisco Unified Intelligence Center database before it is purged

purge-time —Time of day and the regular interval in minutes when the Cisco Unified Intelligence Center database is purged

session-timeout —Session timeout for the Cisco Unified Intelligence Center web applications

show cuic properties dashboard-customwidget-enabled —Displays the value on or off depending on the current value set for the dashboard-customwidget-enabled property . This value can be set using the CLI set cuic properties dashboard-customwidget-enabled .

Requirements

Level privilege: 0

Command privilege level: 0

Allowed during upgrade: Yes

Example

```
admin:show cuic properties purge-retention
purge_retention
===============
1
```

### show cuic tech

Command syntax

This command provides technical details on the Cisco Unified Intelligence Center setup, such as database tables, triggers,
                              procedures and so on.

show cuic tech procedures

This command displays the stored procedures in use for the database.

show cuic tech systables

This command displays the names of all the tables in the Unified Intelligence Center database.

show cuic tech dbschema

This command displays the database schema in a CSV file. This displays output to a .csv file.

show cuic tech table table_name

The command shows the contents of a table on the Unified Intelligence Center database. This displays output to a .out file.

show cuic tech triggers

This command displays Unified Intelligence Center table names and the triggers associated with those tables.

show cuic tech table cuicreport

This command redirects the contents of the specified database table into a file.

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:show cuic tech dbschema
------------show cuic tech dbschema--------------
Database schema
Output is in /cm/trace/dbi/dbSchema1331705967878.csv
Use "file view activelog/cm/trace/dbi/dbSchema1331705867878.csv" command to see output
```

```
admin:show cuic tech systables
--------Show cuic tech system tables-----------
SYSTEM TABLES
tabname
===================
GL_COLLATE
GL_CTYPE
VERSION
cdr_deltab_000657
cdr_deltab_000658
cdr_deltab_000659
cdr_deltab_000660
cdr_deltab_000661
cdr_deltab_000662
cdr_deltab_000663
cdr_deltab_000664
cdr_deltab_000665
cdr_deltab_000666
cdr_deltab_000667
cdr_deltab_000668
cdr_deltab_000669
cdr_deltab_000670
cdr_deltab_000671
cdr_deltab_000672
cdr_deltab_000673
cdr_deltab_000674
```

```
admin:show cuic tech table ?
Syntax:
			show cuic tech table table_name
			table_name mandatory table name
```

```
admin:show cuic tech triggers
-------------show cuic tech triggers---------

Triggers
tablename		trigger
===========================================

cuiccategory										tr_del_category
cuiccategory										tr_ins_category
cuiccategory										tr_upd_category
cuiccollection								tr_del_collection
cuiccollection								tr_ins_collection
cuiccollection								tr_upd_collection
cuicdashboard									tr_del_dashboard
cuicdashboard									tr_ins_dashboard
cuicdashboard									tr_upd_dashboard
cuicdatasource								tr_del_datasource
cuicdatasource								tr_ins_datasource
cuicdatasource								tr_upd_datasource
cuicreport												tr_del_report
cuicreport												tr_ins_report
cuicreport												tr_upd_report
cuicreportdefinition		tr_del_reportdefinition
cuicreportdefinition		tr_ins_reportdefinition
cuicreportdefinition		tr_upd_reportdefinition
cuicuser														tr_upd_userdefaultgroup
cuicvaluelist									tr_del_valuelist
cuicvaluelist									tr_ins_valuelist
```

### show cuic trace

This command shows the log level and trace masks of the given subsystem. If the logging level is set to DEBUG, the trace mask
                              is displayed. If the logging level is set to INFO, the trace masks are not displayed.

The command is case sensitive and can only be run on the Controller node.

To set traces on the member nodes, use the Operations Console command Device Management > Log And Trace Settings .

Command syntax

show cuic trace cuicserver [options]

Options

CUIC

Infrastructure

CUIC_MODEL_OBJECTS

CUIC_DATA_PROCESSING

CUIC_SECURITY

CUIC_DISPLAY

CUIC_MIGRATION

CUIC_USER_HISTORY

CUIC_JSP

CUIC_STATISTICS

Requirements

Level privilege: 0

Command privilege level: 0

Allowed during upgrade: No

Example

```
admin:show cuic trace cuicserver Infrastructure
Log levels are not set - assumed to be Basic
Since log level is basic trace masks are not in effect for Infrastructure
```

### set cuic analyzer url

This command sets the default URL to launch Customer Journey Analyzer from Cisco Unified Intelligence Center.

### Command Syntax

set cuic analyzer url urlname

In a high availability (HA) deployment, run this CLI command on both the nodes.

You must restart the Cisco Unified Intelligence Center Reporting Services for the change to take effect.

### set cuic properties

Use these commands to set values for the Cisco Unified Intelligence Center database and session
                              timeout.

Command syntax

set cuic properties host-to-ip

Parameter

host —Enter the value for the host DNS name for the server, as displayed on the
                                 Data Sources interface

ip_adddress —Enter the IP address of the server for the historical or real-time
                                 database

Command Syntax

set cuic properties session-timeout

Parameter

#numberofSeconds —This command sets the session timeout for the Cisco Unified
                                 Intelligence Center Reporting web application. The default is 14,400 seconds (4
                                 hours).

Example

```
admin:set cuic properties session-timeout 1900
Value has been successfully set
```

#### Command Syntax

set cuic properties dashboard-customwidget-enabled

Parameter

on|off —This command sets the dashboard-customwidget-enabled property to on or off . By setting the value to on or off , you can enable or disable the Custom Widget feature in Dashboards respectively. By default, the value is set to off .

Enabling the custom widget configuration can lead to injection vulnerabilities.

### unset cuic properties

Use this command to unset the translation of host-to-IP hostname.

Command syntax

unset cuic properties host-to-ip [hostname]

Requirements

Level privilege: 0

Command privilege level: 0

Allowed during upgrade: Yes

Example

```
admin:unset cuic properties host-to-ip ccxbox1
```

### set cuic syslog

Command syntax

set cuic syslog [disable|enable]

disable —To disable Cisco Unified Intelligence Center application remote syslogs

enable —To enable Cisco Unified Intelligence Center application remote syslogs

Requirements

Level privilege: 0

Command privilege level: 0

Allowed during upgrade: Yes

Example

```
admin:set cuic syslog enable
```

### set cuic trace

Use these commands to set or change the log levels and trace setting for the subsystems of the cuicserver process to basic
                              or detailed.

### Command Syntax

set cuic trace basic cuicserver [subsystem] none

set cuic trace infrastructure cuicserver [subsystem] [TRACE_FLAGS |
                                    				  none]

set cuic trace subsystem cuicserver [subsystem] [trace_mask1 trace_mask2]

For cuicserver, the valid subsystems are:

Infrastructure

CUIC

CUIC_MODEL_OBJECTS

CUIC_DATA_PROCESSING

CUIC_SECURITY

CUIC_DISPLAY

CUIC_MIGRATION

CUIC_USER_HISTORY

CUIC_JSP

CUIC_STATISTICS

Detailed log levels are set by enabling trace flags, which allows debug
                              		statements to appear in the logs. You can control debug tracing for specific
                              		functionalities (specified in the TRACE flag name), within specific subsystem
                              		components.

basic indicates to set a basic level of tracing. With this
                              		setting, messages and warnings are displayed.

detailed indicates to set a debug level and allows you to turn on
                              		tracing for specific components.

subsystem indicates the subsystem you are setting and displays the
                              		list of all valid subsystems.

none indicates that you do not want to set a flag for tracing.

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: Yes

Example

```
admin:set cuic trace basic cuicserver CUIC_SECURITY
Log level updated successfully. Trace masks are cleared
```

### utils cuic purge

Command Syntax

utils cuic purge

This command runs a manual purge of the cuic database tables. You might do this if you receive an alert that the database
                              is nearing capacity and you do not want to wait for the daily automatic purge.

The tables purged are:

CuicDataSetInfo

CuicDataSet

CuicReportDefinitionFilter

CuicReportDefinitionFilterField

CuicReportDefinitionFilterParameter

CuicCollection

CuicCollectionValue

This command prompts for the password of the administration user. When the password is confirmed, the purge runs immediately.

Options

None

Requirements

Level privilege—1

Command privilege level—1

Allowed during upgrade—Yes

Example

```
admin:utils cuic purge
Executed Purge Sucessfully
```

### utils cuic user
                           	 make-admin [user-name]

In Single Sign-On
                                 		  (SSO) mode the Application
                                    			 User created during installation will not be able to access the Cisco
                                 		  Unified Intelligence Center application with administrator privileges. To
                                 		  enable the Cisco Unified CCX Administrator to have administrator privileges in
                                 		  Cisco Unified Intelligence Center as well, assign reporting capability first
                                 		  and then run this command to make this user the administrator.

After the Unified
                                 		  Intelligence Center user is made an Administrator using this CLI, this user
                                 		  looses Unified Intelligence Center Administrator capabilities after the
                                 		  upgrade.

Thus, this user would not be able to view all the reports that were available to view before the upgrade. The user would have
                                 access to reports based on the assigned role (Agent or Supervisor) and not as an Administrator. You must run this CLI after
                                 the upgrade such that the user is made the Unified Intelligence Center Administrator.

The domain must always be, UCCX .

In an HA deployment, the Cisco Unified Intelligence Center Reporting
                                 		  Service must be restarted on both the nodes.

#### Command
                                 		  Syntax

utils cuic user
                                    			 make-admin [user-name]

Tip: User name
                                 		  should be the complete user name, including the prefix, as listed in Cisco
                                 		  Unified Intelligence Center User List page.

#### Options

None

#### Example

```
admin:utils cuic user make-admin UCCX\ABCD

Command executed successfully.
```

### utils cuic cluster show

This command shows the current cluster mode enabled on this node and the other member details.

### Command Syntax

utils cuic cluster show

### utils cuic cluster
                           	 mode

This command is used
                              		to switch the CUIC cluster join configuration from Multicast to TCP/IP and vice
                              		versa.

After changing the cluster mode in all the nodes, restart “Intelligence Center Reporting Service ” in all the nodes starting
                                          from the publisher sequentially.

### Command
                              		  Syntax

utils cuic cluster mode

### utils cuic cluster refresh

This command refreshes the cluster node information only when run in the TCP/IP mode and must be run when there is an addition
                              or deletion of nodes to the CUIC cluster.

### Command Syntax

utils cuic cluster refresh

### utils cuic cors

Important

After you make changes to the CORS status, allowed origins list, exposed header, or allowed header, restart Cisco Intelligence
                                          Center Reporting Service for the changes to take effect. All CLIs are node-specific and must be run on all nodes in the cluster.

### Command Syntax

utils cuic cors enable

This command enables Cross Origin Resource Sharing (CORS) support in Unified Intelligence Center.

### Command Syntax

utils cuic cors disable

This command disables CORS support in Unified Intelligence Center.

### Command Syntax

utils cuic cors status

This command displays the current CORS status in Unified Intelligence Center.

### Command Syntax

utils cuic cors allowed_origin list

This command displays the list of allowed URLs that can make CORS requests to Unified Intelligence Center.

### Command Syntax

utils cuic cors allowed_origin add <URL1,URL2,URL3>

Parameter: Comma-separated list of URLs (without spaces) that has to be added to the allowed origins list.

The URL format: http[s]://<hostname>[:port]

This command adds the given set of comma-separated URLs to the allowed origins list.

### Command Syntax

utils cuic cors allowed_origin delete

This command prompts for a choice to delete a particular allowed origin URL or all the allowed origin URLs.

1. http://google.com

2. http://www.cisco.com

a: all

q: quit

Select the index of origin to be deleted [1-2 or a,q]

### Command Syntax

utils cuic cors allowed_headers list

This command lists all the configured allowed headers for CORS. This list is used to validate incoming requests to CUIC.

### Command Syntax

utils cuic cors allowed_headers add <header1,header2,header3>

Parameter : Comma-separated list of headers (without spaces) that have to be added to the allowed headers list.

This command adds one or multiple allowed headers for CORS. You can add multiple headers using a comma-separated string.

### Command Syntax

utils cuic cors allowed_headers delete

This command prompts for a choice to delete a particular custom allowed header or all the custom allowed headers.

1: header1

2: header2

a: all

q: quit

Select the index of allowed header to be deleted [1-2 or a, q]: 1

### Command Syntax

utils cuic cors exposed_headers list

This command lists the response headers available for a client.

### Command Syntax

utils cuic cors exposed_headers add <header1,header2,header3>

Parameter: Comma-separated list of headers (without spaces) that have to be added to the exposed headers list.

This command adds one or multiple exposed headers for CORS. You can add multiple headers using a comma-separated string.

### Command Syntax

utils cuic cors exposed_headers delete

This command prompts for a choice to delete a particular custom exposed header or all the custom exposed headers.

1: header1

2: header2

a: all

q: quit

Select the index of exposed header to be deleted [1-2 or a, q]: 1

### Command Syntax

utils cuic cors private-network-access status

This command displays the status of the private network access for CORS in Cisco Unified Intelligence Center. If the status
                                 is True, you have private network access.

### Command Syntax

utils cuic cors private-network-access enable

This command enables the private network access for CORS in Cisco Unified Intelligence Center. To enable private network access,
                                 run the command on all nodes of CUIC and restart the Intelligence Center Reporting Service.

### Command syntax

utils cuic cors private-network-access disable

This command disables the private network access for CORS in Cisco Unified Intelligence Center. To disable private network
                                 access, run the command on all nodes of CUIC and restart the Intelligence Center Reporting Service.

## utils cuic logging

The utils cuic logging commands update or display the configuration only on the nodes on which the commands are run. To change the logging configuration
                           on each node in the cluster, you must run the command separately on each node.

### utils cuic logging config set

This command sets the value for log file configuration.

### Command Syntax

utils cuic logging config set [config-name] [config-value]

Options

[config-name] - mandatory log file configuration name

Valid configuration names are max-file-size , max-file-count , syslog-primary-host and syslog-secondary-host . The maximum limit of max-file-size and max-file-count is 50 MB and 50 respectively.

Only one [config-name] option can be set at a time.

[config-value] - mandatory log file configuration value.  For syslog-primary-host and syslog-secondary-host configuration names, the configuration values are the primary syslog server hostname and the secondary syslog server hostname,
                                    respectively.

### utils cuic logging config show

This command prints the current log configuration for the given configuration name.

### Command Syntax

utils cuic logging config show [config-name]

Options

[config-name] - mandatory log file configuration
                              name

Valid configuration names are max-file-size , max-file-count , syslog-primary-host and syslog-secondary-host .

Only one [config-name] option can be printed at a time.

### utils cuic logging config clear

This command clears the log file configuration for the primary and secondary syslog servers.

### Command Syntax

utils cuic logging config clear [config-name]

Options

[config-name] - mandatory log file configuration name

Valid configuration names are syslog-primary-host and syslog-secondary-host .

Only one [config-name] option can be cleared at a time.

### utils cuic logging list

This command lists the module and the logging level for the specified module. If a module name is
                              specified, the logging level is displayed only for that module.

### Command Syntax

utils cuic logging list [module-name]

Options

[module-name] - optional

Possible module names for which, the log levels can be printed are as follows:

REPORT, REPORTENGINE, REPORTDEFINITION, SCHEDULER, DASHBOARD, AUTHORIZATION,
                                 AUTHENTICATION, VALUELISTCOLLECTION, SECURITY, CUICUI, DATASOURCE,
                                 CUICCONFIG

### utils cuic logging reset

This command resets any modifications done to the logging configuration to the default value. For
                              all the modules, the default value is Info .

### Command Syntax

utils cuic logging reset

Options

No parameters

### utils cuic logging update

This command updates the log level for the given module name.

### Command Syntax

utils cuic logging update [module-name] [log-level]

Options

[module-name] - mandatory

Possible module names are as follows:

REPORT, REPORTENGINE, REPORTDEFINITION, SCHEDULER, DASHBOARD,
                                       AUTHORIZATION, AUTHENTICATION, VALUELISTCOLLECTION, SECURITY, CUICUI,
                                       DATASOURCE, CUICCONFIG

[log-level] - mandatory

New log level for the module. Valid log-level values are as follows:

ERROR, WARN, INFO, DEBUG

## utils cuic session list

This command lists the current Cisco Unified Intelligence Center sessions.

### Command Syntax

utils cuic session list

Options

No parameters

Example

```
admin:utils cuic session list
Command run successfully
Session ID details saved to file.
To view file, type "file view activelog cuic-session.out"
To SFTP file, type "file get activelog cuic-session.out"
```

## utils cuic session delete

This command deletes the Cisco Unified Intelligence Center sessions based on the session IDs that you pass to this command.

### Command Syntax

utils cuic session delete <sessions ID1,sessions ID2> utils cuic session delete <username 1,username 2>

Parameter

Sessions IDs are IDs of the current Cisco Unified Intelligence Center sessions.

To get the current session IDs , you must first run the utils cuic session list command and then run file view activelog cuic-session.out command.

Example

```
admin:utils cuic session delete a5fB22f89658e97D089Ab51Ee859b2c1 Session Deleted successfully
```

## Specific License Reservation Commands

### license smart reservation enable

Use this command to enable the license reservation feature in Smart Licensing. Before running this command, ensure the following:

Smart Licensing must be enabled.

Smart Account must be enabled for reservation.

Smart Licensing must be in unregistered state.

Command syntax

license smart reservation enable

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:license smart reservation enable
License reservation is enabled successfully.
Command successful.
```

Result: Smart Licensing is enabled and you can continue with the license reservation process.

With license reservation enabled, Smart License Management page, option to Register , update Transport Settings and other allied operations in Unified CCX Administration are not available for this product instance.

### license smart reservation request

Use this command to initiate the license reservation request process. Before running this command, ensure the following:

Enable command has been run.

Command syntax

license smart reservation request specific

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:license smart reservation request specific
License reservation requested successfully.
Reservation Request Code is: CB-ZUCCX:059d8a992467-AAwxxawE5-73
Use this code in Cisco SSM to obtain the Authorization Code.

Reserve the following License Names in Cisco SSM to use the associated features.

SL NO. LICENSE NAME                         MANDATORY
------ --------------------------------- ------------------------------------------------------
1      CCX Flex Standard Seat             Yes, if standard agent seats are required.
2      CCX Flex Premium Seat              Yes, if premium agent seats are required.
3      CCX Inbound Port-Flex              Yes, if Advanced IVR ports are required.
4      CCX Outbound Port-Flex             Yes, if Outbound IVR ports are required.
5      UCCX Version 15                    Yes, to report product version number.

Command successful.
```

Result: Reservation Request Code is generated. Use the code in Cisco SSM to generate the Authorization Code.

### license smart reservation install

Use this command to install or update the license reservation. Before running this command, ensure the following:

Request command has been run.

Authorization Code is obtained from Cisco SSM .

If you have already installed an Authorization Code and want to modify the reserved licenses, you must generate a new Authorization
                                          Code and run this command again.

Command syntax

license smart reservation install " <authorization code> "

The <authorization code> has to be obtained from Cisco SSM . Ensure to put the Authorization Code in double quotes.

Authorization Code is also available in a file. You cannot provide file name as the parameter. You must copy the entire content
                                          of the file and use it as Authorization Code.

After successfully installing the license reservation, restart the system.

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example 1: Install License Reservation for the First Time

```
admin:license smart reservation install "<specificPLR><authorizationCode><flag>A</flag><version>D
</version><piid>109e8ec2-95f9-4a20-bde5-fbf689c046f4</piid><timestamp>1745390561298</timestamp><entitlements>
<entitlement><tag>regid.2019-06.com.cisco.CCX_FLEX_STD,12.5_be49ea3c-8224-4a1c-b3cc-f98b7c63de3b</tag>
<count>1</count><startDate>2024-Jul-16 UTC</startDate><endDate>2025-Jul-16 UTC</endDate><licenseType>TERM</licenseType>
<displayName>CCX Flex Standard Seat</displayName><tagDescription>CCX Flex Standard Licenses</tagDescription>
<subscriptionID></subscriptionID></entitlement></entitlements></authorizationCode><signature>
MEUCIQDv+eQu1fCgdllO18ZWJZgs+Jwj7snD37088K1P2qbIYgIgV2pD0PS3JKOpTd+wqJLjDY0u7/gESf+MWKo0Cuoeygc=</signature>
<udi>P:UCCX,S:53ecfccbfe23</udi></specificPLR>"

This operation has to be performed in maintenance window.
Continue (y/n)?y

License reservation is being installed. Please wait ...
License reservation is installed successfully. Reboot the system for the changes to take effect.
 Command successful.
```

Example 2: Update License Reservation

```
admin:license smart reservation install "<specificPLR><authorizationCode><flag>A</flag><version>C</version>
<piid>4e0f17d0-4d83-4a74-8009-6e1a909f505a</piid><timestamp>1583227289333</timestamp>
<entitlements><entitlement><tag>regid.2019-06.com.cisco.CCX_FLEX_PREMIUM,
12.5_0ecc396f-9a80-4b7b-a4c1-35011a2bc68f</tag><count>1</count><startDate>2020-Feb-26 UTC</startDate>
<endDate>2021-Feb-20 UTC</endDate><licenseType>TERM</licenseType><displayName>
CCX Flex Premium Seat 12.5</displayName><tagDescription>CCX Flex Premium License</tagDescription>
<subscriptionID></subscriptionID></entitlement></entitlements></authorizationCode>
<signature>MEYCIQDNodtb0VfzvyJfLenhGMCeprSELdAMXaCpsqW8e/mBBAIhAIYXW+80inS9e+
9J1i0MSFzWbuJ93YnQM/yoSTcDwzst</signature><udi>P:UCCX,S:1f2b5461b8ed</udi></specificPLR>"

This operation has to be performed in maintenance window.
Continue (y/n)?y

License reservation is being installed. Please wait ...
License reservation is installed successfully. Reboot the system for the changes to take effect.
Confirmation Code is: 125ffe1b
Use this code in Cisco SSM to the complete license reservation update process.
Command successful.
```

Result: Unified CCX gets automatically refreshed with the reserved licenses.

Caution

If the installed licenses are incorrect, all the critical services of the contact center will go down. Be cautious while reserving
                                          licenses and ensure that the appropriate licenses are reserved.

### license smart reservation return

Use this command to return the license reservation if you have already installed the Authorization Code.

Command syntax

license smart reservation return

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:license smart reservation return

This command will return the license reservation and this product instance will transition back to the unregistered state.
Continue (y/n)?y

License reservation is being returned. Please wait ...
License reservation is returned successfully.
Reservation Return Code is: Cb3AEN-61XgQW-YGBXWm-FgS16L-LFRQ7n-aHU9Y1-cJDQGL-DtZGhJ-2D3
Use this code in Cisco SSM to complete the reservation return process.
Command successful.
```

Result: Reservation Return Code is generated and the product instance will transition back to the unregistered state. Enter the code
                              in Cisco SSM to return the reserved licenses to the virtual pool. The product instance will enter evaluation or evaluation expired mode.

The best practice is to restart the system after returning the reservation.

If the evaluation period has expired, this product instance will enter into enforcement mode. For more information on enforcement
                                          mode, see Cisco Unified Contact Center Express Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-feature-guides-list.html .

### license smart reservation return-authorization

Use this command to return the license reservation if you have not yet installed the Authorization Code.

This command is primarily for executing before installing the Authorization Code. However, you can also run this command after
                                          installing the Authorization Code.

Command syntax

license smart reservation return-authorization "<authorization code>"

The <authorization code> that has to be obtained from Cisco SSM . Ensure to put the Authorization Code in double quotes.

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:license smart reservation return-authorization "<specificPLR><authorizationCode><flag>A</flag><version>C</version>
<piid>4e0f17d0-4d83-4a74-8009-6e1a909f505a</piid><timestamp>1583227289333</timestamp>
<entitlements><entitlement><tag>regid.2019-06.com.cisco.CCX_FLEX_PREMIUM,
12.5_0ecc396f-9a80-4b7b-a4c1-35011a2bc68f</tag><count>1</count><startDate>2020-Feb-26 UTC</startDate>
<endDate>2021-Feb-20 UTC</endDate><licenseType>TERM</licenseType><displayName>
CCX Flex Premium Seat 12.5</displayName><tagDescription>CCX Flex Premium License</tagDescription>
<subscriptionID></subscriptionID></entitlement></entitlements></authorizationCode>
<signature>MEYCIQDNodtb0VfzvyJfLenhGMCeprSELdAMXaCpsqW8e/mBBAIhAIYXW+80inS9e+
9J1i0MSFzWbuJ93YnQM/yoSTcDwzst</signature><udi>P:UCCX,S:1f2b5461b8ed</udi></specificPLR>"

License reservation is being returned. Please wait ...
License reservation is returned successfully.
Reservation Return Code is: gfgh677hn
Use this code in Cisco SSM to complete the reservation return process.
Command successful.
```

Result: Reservation Return Code is generated and the product instance will transition back to the unregistered state. Enter the code
                              in Cisco SSM to return the reserved licenses to the virtual pool. The product instance will enter evaluation or evaluation expired mode.

The best practice is to restart the system after returning the reservation.

If the evaluation period has expired, this product instance will enter into enforcement mode. For more information on enforcement
                                          mode, see Cisco Unified Contact Center Express Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-feature-guides-list.html .

### license smart hostname enable

Use this command to enable the privacy of UCCX during smart license registration with CSSM/On-Prem SSM.

Command syntax

license smart hostname enable

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:license smart hostname enable
Command successful.
```

Result: UCCX privacy is enabled, hostname and IP address of  UCCX will not be shared with CSSM/On-Prem SSM. The license serial number
                              of  UCCX will be displayed in CSSM/On-Prem SSM portal, instead of UCCX hostname.

### license smart hostname disable

Use this command to disable the privacy of UCCX during smart license registration with CSSM/On-Prem SSM.

Command syntax

license smart hostname disable

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
license smart hostname disable
Command successful.
```

Result: UCCX privacy is disabled, hostname and IP address of UCCX will be shared with CSSM/On-Prem SSM. The hostname of the UCCX
                              will be displayed in CSSM/On-Prem SSM portal, instead of UCCX license serial number.

Caution

Be aware that when you enable the privacy, you are exposing your internal address or domain details.

After enabling or disabling license smart hostname, utils system restart must be performed.

### license smart reservation cancel

Use this command to cancel the license reservation process for Smart Licensing.

Prerequisites:

Request command has been run.

Authorization Code has not been installed.

Command syntax

license smart reservation cancel

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:license smart reservation cancel
License reservation request is canceled successfully.
Command successful.
```

Result: Reservation Request Code that was generated will be made invalid on the product instance.

Caution

After you run the cancel command, do not use the earlier generated Reservation Request Code to generate Authorization Code.

### license smart reservation disable

Use this command to disable the license reservation feature in Smart Licensing. Before disabling the license reservation,
                              you must return the reserved licenses to the virtual pool, so that you can use the licenses without reservation.

Before running this command, if you have requested or installed license reservation, cancel or return the license reservation
                                          respectively.

Command syntax

license smart reservation disable

Requirements

Level privilege: 1

Command privilege level: 1

Allowed during upgrade: No

Example

```
admin:license smart reservation disable
License reservation is disabled successfully.
Command successful.
```

Result: License Reservation is disabled.

After disabling the license reservation, you have the option to register the product instance by using Smart Licensing in Unified CCX Administration.

| Step 1 | Perform one of
                                          			 the following tasks: From a remote system, use SSH to connect securely to the Cisco CCX Platform. In your SSH client, enter ssh adminname@hostname where adminname specifies the platform administrator ID and hostname specifies the hostname that was entered during installation. For example, ssh
                                                      						admin@ccx-1 . From a
                                                   					 direct connection, you receive this prompt automatically: ccx-1 login: where ccx-1 represents the
                                                   					 hostname of the system. Enter your
                                                   					 administrator ID. In either
                                             				case, the system prompts you for a password. |
|---|---|
| Step 2 | Enter
                                          			 password. The CLI prompt
                                             				displays. The prompt represents the administrator ID, for example: admin: |

| Note | If you enter the help command without specifying the name of a particular
                                             			 command as the optional parameter, the system provides information about the
                                             			 CLI system. |
|---|---|

| Note | If you enter a ? after a menu command, such as set , it acts like the Tab key and lists the commands that are
                                             			 available. |
|---|---|

| Note | If you run the command utils system switch-version and enter Yes to start the process, entering Ctrl-C exits the command but does not stop the switch-version process. |
|---|---|

| Important | When file get CLI command is used with the abstime as an option to collect log files, this filters the files based on the last modified timestamp. If the last modified time
                                          is updated, this CLI may not give desired results. Use the log collection feature in RTMT instead to collect the log files. |
|---|---|

| Note | The name of the
                                          		  file containing the output from each show uccx tech command
                                          		  run is automatically generated by the command script. The file path and
                                          		  filename are displayed after the completion of the operation. |
|---|---|

| Note | The name of the
                                          		  file is automatically generated by the command script. The file path and
                                          		  filename are displayed after the completion of the operation. |
|---|---|

| Note | The name of the
                                          		  file containing the schema is automatically generated by the command script.
                                          		  The file path and filename are displayed after the completion of the operation. |
|---|---|

| Note | The pound "#"
                                             			 sign, that is prefixed for size, indicates the entry is staled. |
|---|---|

| Note | After the system reboots, the self-signed and CA certificates of the servers, whose certificate type has changed, must be
                                             regenerated and re-uploaded into the client servers. |
|---|---|

| Note | In a high availability (HA) deployment, run this CLI command on both the nodes of the cluster. Restart both the nodes after
                                          executing the CLI command. |
|---|---|

| Note | In a high
                                          		  availability (HA) deployment, run this CLI command on both the nodes of the
                                          		  cluster. Restart both the nodes after executing the CLI command. |
|---|---|

| Note | After you run this
                                          		  command, restart the Unified CCX Engine service. After Unified CCX Engine
                                          		  service starts successfully, restart Cisco Tomcat using the CLI command utils service
                                             			 restart Cisco Tomcat . |
|---|---|

| Note | After you run this
                                          		  command, restart the Unified CCX Engine service. After Unified CCX Engine
                                          		  service starts successfully, restart Cisco Tomcat using the CLI command utils service
                                             			 restart Cisco Tomcat . |
|---|---|

| Note | After you run this
                                          		  command, restart the Unified CCX Engine service. After Unified CCX Engine
                                          		  service starts successfully, restart Cisco Tomcat using the CLI command utils service
                                             			 restart Cisco Tomcat . |
|---|---|

| Note | Run this command
                                          		  to set the administrator for a configured Unified CCX system only.
                                          		  For a newly installed system, you must login with the platform login password
                                          		  that you specified during installation. |
|---|---|

| Note | You cannot assign
                                          		  Administrator capability to a user ID that is the same as the application
                                          		  administrator user ID that you created during the Unified CCX installation. If you assign Administrator capability to such a user ID, a "Command
                                             			 failed" error message is displayed on the console. |
|---|---|

| Note | When the command is run, any previous tar file that was created is deleted. At any point only one Historical Reporting data export file is saved in the local file
                                             system. So after the Historical Reporting data is exported, transfer the tar file to remote server before running the command again. |
|---|---|

| agentconnectiondetail | agentstatedetail | contactcalldetail |
|---|---|---|
| contactqueuedetail | contactroutingdetail | dialinglisthistory |
| skill | skillgroup | resource |
| resourcegroup | resourceskillmapping | contactservicequeue |
| team | dialinglist | campaign |
| textagentconnectiondetail | textcontactdetail | textcontactqueuedetail |
| textagentstatedetail | textratingdetail | eemcontactemaildetail |
| eemqueueagentdetail | eememailagentstatedetail | audit_reskill |
| audit_skillgroup | audit_residualskills | contactwrapupdata |
| contactholddetail | contactfeedbackdetail | flexlicenseusage |
| consultlegdetail | textcustomerdetails | - |

| Caution | Avoid creating
                                          		  remote account usernames starting with "uccx" or "UCCX" because such usernames
                                          		  may conflict with system account names that are used internally within the
                                          		  Cisco Unified Contact Center Express server. |
|---|---|

| Note | Restart the service (Cisco Unified Intelligence Center Reporting Service) on all nodes in the cluster to enable the new administrator
                                          to log in to Unified Intelligence Center. |
|---|---|

| Note | Do not run utils system upgrade dataexport initiate on a Cisco VVB 15.0(1) FCS or base-release system. Cisco VVB 15.0(1) base release does not support this command. Before running
                                          the command, ensure that Cisco VVB 15.0(1) is updated with ES202511 or a later supported ES to enable the utils system upgrade dataexport initiate command. |
|---|---|

| Note | A switch version operation is abruptly terminated  if a power reset or hard reboot is performed on the Unified CCX system
                                          when the operation is in progress. Example admin:utils system switch-version

   ** There is no inactive side available ** |
|---|---|

| Note | The
                                          		  name of the file containing the output from all the checks performed is
                                          		  automatically generated by the command script. For the filename to be unique,
                                          		  the naming format is DbServerIntegrity_<TIMESTAMP>.txt. This format
                                          		  ensures the uniqueness across processes and over time. The file path and
                                          		  filename are displayed after the completion of the operation. |
|---|---|

| Note | After you run this command, you must reboot the Unified CCX server and
                                          		  restart all the Unified CCX services. |
|---|---|

| Note | You must use this command when there are common classes being used in the custom code as well as by Unified CCX and there
                                       is a version mismatch between the common classes that are being used. |
|---|---|

| Caution | You must add the custom classpath only if the Custom class files have a newer version than the class files used by Unified
                                       CCX. Adding class files that are of older version at the start of the classpath could lead to system instability. |
|---|---|

| Note | If the sync fails, then running this command or the auto sync that is part of the purge schedule will not revoke the permissions
                                             for the previously-synced users or user groups. |
|---|---|

| Note | This CLI is available only on the secondary node(s) in a cluster. |
|---|---|

| Note | If you run utils uccx healthcheck all , you are not prompted to select the category. This command will run health check on all the categories. |
|---|---|

| Plug-in | Threshold Limit | Message Displayed |
|---|---|---|
| CPU Usage | System CPU usage exceeds 70 percent. | The CPU usage has exceeded the threshold limit. |
| Memory Usage | System memory usage exceeds 70 percent. | The memory usage has exceeded the threshold limit. |
| Disk Space Usage | System disk space usage exceeds 70 percent. | The disk usage has exceeded the threshold limit. |
| Disk I/O Latency | Total time taken to write 2 MB of data (1000 sequential 2 KB synchronous writes) to the active partition exceeds 500 milliseconds. | Disk I/O exceeded the permissible limit. |

| Note | FIPS 140-2 mode is supported only on releases that have been through FIPS compliance. |
|---|---|

| Caution | Back up the system before and after enabling FIPS 140-2 mode. If any of the startup self-tests fail, the Unified CCX server halts. Restart the Unified CCX server. If the startup self-test
                                          error persists, it indicates that there is a critical problem in the FIPS module and the only option is to use a recovery
                                          CD. |
|---|---|

| Note | Before enabling security modes such as FIPS, Common Criteria, and Enhanced Security, the cluster security password must be
                                             at least 14 characters. Update the cluster security password by using the set password user security command on all nodes and then run this command. |
|---|---|

| Caution | After you enable FIPS 140-2 mode on a server, please wait until the server reboots and the phones re-register successfully
                                             before enabling FIPS 140-2 mode on the next server. |
|---|---|

| Note | After enabling, the system uses the secure port 9089 along with the non-secure port 1504. |
|---|---|

| Caution | Ensure that you use this command during off-peak hours to avoid service interruptions. |
|---|---|

| Note | After disabling, the system uses only the non-secure port 1504. |
|---|---|

| Caution | Ensure that you use this command during off-peak hours to avoid service interruptions. |
|---|---|

| Note | Files that are in
                                          		  use cannot be deleted. |
|---|---|

| Note | If the Unified CCX database in either of the node is down or is Out
                                          			 of Service, High Availability commands do not work. |
|---|---|

| Note | Use this command only when the IP address of the other node is going
                                          		  to be changed. After you run this command, reboot the Unified CCX server and restart all the Unified CCX services. |
|---|---|

| Note | Use this command only when the hostname of the other node is changed. After you run this command, reboot the Unified CCX server and restart all the Unified CCX services. |
|---|---|

| Note | This command is available only in high availability mode. |
|---|---|

| Note | Cisco Finesse is available and can be activated only in ICD Premium and Standard licensed deployments. In HA
                                                				deployments, run this command separately on both the Unified CCX nodes. |
|---|---|

| Note | The password
                                          		  length must be between 5 and 32 characters long and must not contain spaces or
                                          		  double quotes. |
|---|---|

| Note | Password values
                                       		entered by the user is not echoed on the console. |
|---|---|

| Note | Enabling trace logging may cause an overload in the system and must be used for debugging purposes only. |
|---|---|

| Note | After execution of each command, wait for 60 seconds for the changes to take effect. |
|---|---|

| Note | Adding multiple module names, log configuration names, and log configuration level values are not supported. Log configuration with name ROOT is not allowed. |
|---|---|

| Note | Setting the log configuration level to DEBUG or TRACE impacts system performance. This must be done in consultation with Cisco
                                                   support to ensure that the modules with high log output are not be enabled with TRACE levels in production severs. |
|---|---|

| Note | Updating multiple module names, log configuration names, and log configuration level values are not supported. Audit log configuration cannot be updated. |
|---|---|

| Note | Setting the log configuration level to DEBUG or TRACE impacts system performance. |
|---|---|

| Note | ROOT log configurations cannot be deleted. Deleting multiple log configuration names are not supported. |
|---|---|

| Note | The configured timeout for browser notifications depends on the operating system and browser settings. The timeout value is
                                                   honored in Chrome browser in Windows OS. However, the other supported browsers do not honor the configured notification timeout
                                                   value consistently. |
|---|---|

| Note | Cisco Finesse Toaster Notification does not work with Internet Explorer browser. |
|---|---|

| Note | The default time set for inactivity timeout is 120 seconds. |
|---|---|

| Note | When inactivity timeout is disabled, you will not be logged out of Finesse IPPA, if the agent is on any other screen. |
|---|---|

| Note | Minimum value of n must be 120 seconds and maximum value can be up to one day (86400 seconds). |
|---|---|

| Note | The Finesse IPPA Inactivity Timeout CLIs should be run on primary and secondary Finesse servers. Enabling or disabling this
                                             feature requires a restart of Cisco Finesse Tomcat, and restart must be done in the maintenance window. During upgrade, the
                                             inactivity timeout configuration is not retained and should be re-configured post upgrade. |
|---|---|

| Note | To enable this feature in Cisco Finesse, install Finesse 12.5(1) ES3 COP or higher. |
|---|---|

| Note | From Cisco Finesse Release 12.5(1) ES4 COP onward, all references to whitelist in the CLIs are changed to allowed_list . |
|---|---|

| Note | Internet Explorer does not support frame-ancestors, and therefore will not block any websites from loading Cisco Finesse within
                                             it. |
|---|---|

| Note | Wildcard character * is also supported for the FQDN and port entries, which indicates that all the legal FQDN or ports are
                                                         valid. The maximum number of characters (cumulative) that are permissible in allowed list is 2000. |
|---|---|

| Note | Refresh the browser for the changes to take effect. |
|---|---|

| Note | This is applicable to both voice and non-voice channels. |
|---|---|

| Note | This is applicable to both voice and non-voice channels. |
|---|---|

| Note | This is applicable to both voice and non-voice channels. |
|---|---|

| Note | The maximum attachment size is configurable in the range of 5 to 10 MB. |
|---|---|

| Attention | The utils finesse set_property desktop enableRetryLoginFeature true command is not enabling automatic desktop login retries. So, to enable automatic desktop login retries, use the following
                                                   command: utils finesse set_property desktop retryLoginAfterLogoutPhoneFailure true To view the status of automatic desktop login retries, use the following command: utils finesse show_property desktop retryLoginAfterLogoutPhoneFailure To disable the automatic desktop login retries, use the following command: utils finesse set_property desktop enableRetryLoginFeature false |
|---|---|

| Note | Reducing the retry interval increases the load on the system when there is a system-wide outage of devices. |
|---|---|

| Note | Cisco Finesse Administration Console and Cisco Finesse desktop now support messages configured in Cisco Unified OS Administration
                                             by using the custom logon message feature. From Unified CCX Release 12.5(1)SU1, it's recommended that you use the custom logon
                                             message feature as an alternative to the security banner message feature to convey important information to Cisco Finesse
                                             desktop users and administrators. For more information about setting up custom logon message, see the Set Up Customized Logon Message section in the Cisco Unified Operating System Administration Guide for Cisco Unified CCX and Cisco Unified IP IVR at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html . |
|---|---|

| Note | To enable this CLI in Cisco Finesse, install Cisco Finesse 12.5(1)ES2 COP or higher. |
|---|---|

| Note | The timeout value must be entered in milliseconds. |
|---|---|

| Note | These commands are not applicable when Cisco Finesse is connected to CTI versions that are greater than or equal to 12.6. |
|---|---|

| Note | WebProxy Service CLIs are node-specific and must be run on all nodes in the cluster. |
|---|---|

| Note | Setting the access logs to debug impacts performance. Hence, avoid using in the production deployment. |
|---|---|

| Note | Setting the error logs to debug impacts performance. Hence, avoid using in the production deployment. |
|---|---|

| Note | The CLIs require Cisco Finesse Tomcat restart except for desktop related properties. |
|---|---|

| Note | Restart Cisco Finesse Tomcat and Cisco Finesse Notification Services for the
                                             changes to take effect. |
|---|---|

| Note | To enable this CLI in Cisco Finesse, install Finesse 12.5(1) ES4 COP or higher. |
|---|---|

| Note | These restrictions do not affect the desktop XMPP notification port 7443. |
|---|---|

| Important | After you make changes to the CORS status or to the allowed origin list, restart Cisco Finesse Tomcat and Notification Services
                                             for the changes to take effect. |
|---|---|

| Note | Use the utils finesse cors allowed_origin CLI to customize the allowed origin list. Any custom headers used in the CORS requests must be added using utils finesse cors allowed_headers CLI. |
|---|---|

| Note | This isn’t a secure configuration and is included only to support backward compatibility. |
|---|---|

| Note | If the allowed origin list is already present, the list is preserved and used when CORS is enabled. The CLI changes are reflected
                                                   only after you clear your cache and close and reopen the browser. |
|---|---|

| Note | The wildcard character star (*) isn’t a valid origin in the allowed origin list. The maximum number of characters (cumulative) that are permissible in allowed origin is 4000. |
|---|---|

| Note | Delete lists all the origins in the allowed origin list. The origins can be deleted by selecting the appropriate ones from
                                                   the list. For example: utils finesse cors allowed_origin delete 1: http://google.com 2: https://www.cisco.com 3: https://def.com 4: https://abc.com:7777 a: all q: quit Select the index of origin(s) to be deleted [1-4 or a,q] |
|---|---|

| Note | These headers can’t be modified. Custom headers can be added or removed using the following CLIs: |
|---|---|

| Note | The wildcard character star (*) isn’t supported. |
|---|---|

| Note | The wildcard character star (*) isn’t supported |
|---|---|

| Note | From Cisco Finesse Release 12.5(1) ES4 COP onward, all references to whitelist in the CLIs are changed to allowed_list . |
|---|---|

| Note | Wildcard character * is not supported. The allowed list feature does not perform hostname resolutions. The format of the allowed list entry should match the format
                                             in which the gadget requests for a resource. If utils finesse gadget_source_check is enabled, you must add the CUIC URLs to utils finesse gadget_source_check allowed_list for the stock gadgets to load. For example, utils finesse gadget_source_check enable utils finesse gadget_source_check allowed_list add https://<CUIC_Pub_FQDN> utils finesse gadget_source_check allowed_list add https://<CUIC_Pub_FQDN>:8444 utils finesse gadget_source_check allowed_list add https://<CUIC_Sub_FQDN> utils finesse gadget_source_check allowed_list add https://<CUIC_Sub_FQDN>:8444 If you do not add the CUIC URLs, Finesse Desktop fails to load and an appropriate error message is displayed. |
|---|---|

| Note | All CLIs are node-specific and must be run on all nodes in the cluster. After any changes are done to gadget source status or to the allowed list, restart Cisco Finesse Tomcat for changes to take
                                             effect. |
|---|---|

| Note | The View property CLIs do not support multiple values. |
|---|---|

| Note | In a high availability (HA) deployment, run this CLI command on both the nodes. You must restart the Cisco Unified Intelligence Center Reporting Services for the change to take effect. |
|---|---|

| Note | Enabling the custom widget configuration can lead to injection vulnerabilities. |
|---|---|

| Note | The domain must always be, UCCX . |
|---|---|

| Note | The member details are available only in the TCP/IP mode. The member details displayed are of the configured members and does
                                       not represent the cluster in real-time. |
|---|---|

| Note | After changing the cluster mode in all the nodes, restart “Intelligence Center Reporting Service ” in all the nodes starting
                                          from the publisher sequentially. |
|---|---|

| Important | After you make changes to the CORS status, allowed origins list, exposed header, or allowed header, restart Cisco Intelligence
                                          Center Reporting Service for the changes to take effect. All CLIs are node-specific and must be run on all nodes in the cluster. |
|---|---|

| Note | With license reservation enabled, Smart License Management page, option to Register , update Transport Settings and other allied operations in Unified CCX Administration are not available for this product instance. |
|---|---|

| Note | If you have already installed an Authorization Code and want to modify the reserved licenses, you must generate a new Authorization
                                          Code and run this command again. |
|---|---|

| Note | Authorization Code is also available in a file. You cannot provide file name as the parameter. You must copy the entire content
                                          of the file and use it as Authorization Code. |
|---|---|

| Caution | If the installed licenses are incorrect, all the critical services of the contact center will go down. Be cautious while reserving
                                          licenses and ensure that the appropriate licenses are reserved. |
|---|---|

| Note | The best practice is to restart the system after returning the reservation. If the evaluation period has expired, this product instance will enter into enforcement mode. For more information on enforcement
                                          mode, see Cisco Unified Contact Center Express Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-feature-guides-list.html . |
|---|---|

| Note | This command is primarily for executing before installing the Authorization Code. However, you can also run this command after
                                          installing the Authorization Code. |
|---|---|

| Note | The best practice is to restart the system after returning the reservation. If the evaluation period has expired, this product instance will enter into enforcement mode. For more information on enforcement
                                          mode, see Cisco Unified Contact Center Express Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-feature-guides-list.html . |
|---|---|

| Caution | Be aware that when you enable the privacy, you are exposing your internal address or domain details. After enabling or disabling license smart hostname, utils system restart must be performed. |
|---|---|

| Caution | After you run the cancel command, do not use the earlier generated Reservation Request Code to generate Authorization Code. |
|---|---|

| Note | Before running this command, if you have requested or installed license reservation, cancel or return the license reservation
                                          respectively. |
|---|---|

| Note | After disabling the license reservation, you have the option to register the product instance by using Smart Licensing in Unified CCX Administration. |
|---|---|