---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-15-english-cli-guide-cer0-b-cisco-emergency-responder-cli-guide-15-cer0--6efdbea80a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/15/english/cli/guide/cer0_b_cisco-emergency-responder-cli-guide-15/cer0_b_cisco-emergency-responder-cli-guide-1251su1_chapter_00.html
retrieved_at: 2026-08-21T15:26:24.913646+00:00
---

Cisco Emergency Responder Command Line Interface Guide for Release 15 and SUs

# Cisco Emergency Responder Command Line Interface Guide for Release 15 and SUs

Find Matches in This Book

## Results

Updated: February 5, 2026

Chapter: CLI Basics

## Chapter: CLI Basics

# CLI Basics

## CLI Overview

The File I/O Reporting Service (FIOR) provides a kernel-based daemon
                                          			 for collecting file I/O per process. It must be enabled from the CLI; it is
                                          			 disabled by default.

## Start CLI Session

You can
                              		  access the CLI remotely or locally using the following methods:

- You can access the CLI
                                 			 remotely from a web client workstation, such as the workstation that you use
                                 			 for Emergency Responder administration, by using secure shell (SSH) to connect
                                 			 securely to the Emergency Responder.

- You can access the CLI
                                 			 locally by using the monitor and keyboard that you used during installation or
                                 			 by using a terminal server that is connected to the serial port. Use this
                                 			 method if a problem exists with the IP address.

### Before you begin

Ensure that
                              		  you have the following information, which is defined during installation:

- A primary IP address and
                                 			 hostname

- An administrator ID

- An administrator password

You need
                              		  this information to log in to the Emergency Responder platform.

Step 1

Depending on
                                       			 your method of access, do one of the following actions:

From a remote
                                             				  system, use SSH to connect securely to the Emergency Responder platform. In
                                             				  your SSH client, enter:

ssh adminname @ hostname

adminnam specifies the administrator ID and hostname specifies the hostname that was defined during
                                             				  installation.

For example, ssh
                                                					 admin@cer-1

From a direct
                                             				  connection, you receive this prompt automatically:

```
cer-1 login:
```

cer-1 represents the host name of the system.

Enter the
                                             				  administrator ID that was defined during installation.

Step 2

Enter the
                                       			 password that was defined at installation.

The CLI prompt
                                          				appears. The prompt represents the administrator ID; for example:

```
admin:
```

You can now use
                                          				any CLI command.

## Command
                        	 Completion

To complete
                              		  commands, use Tab :

Enter the start
                                 			 of a command and press Tab to complete the command. For example, if
                                 			 you enter se and press Tab , se is expanded to the set command.

Enter a full
                                 			 command name and press Tab to display all the commands or subcommands
                                 			 that are available. For example, if you enter set and press Tab , you see all of the set subcommands. An asterisk (*) identifies the commands that
                                 			 have subcommands.

Press Tab to continue. The current command
                                 			 line repeats; no additional expansion is available.

## Obtain Command Help

Detailed help
                                       				that includes a definition of the command and an example of its use

Short query help
                                       				that includes only command syntax

Step 1

To get detailed
                                       			 help, at the CLI prompt enter the help command
                                       			 which specifies the command name or the command and parameter.

### Example:

```
admin:help file list activelog
activelog help:
This will list active logging files

options are:
page - pause output
detail - show detailed listing
reverse - reverse sort order
date - sort by date
size - sort by size

file-spec can contain '*' as wildcards

Example:
admin:file list activelog platform detail
02 Dec,2004 12:00:59 <dir> drf
02 Dec,2004 12:00:59 <dir> log
16 Nov,2004 21:45:43 8,557 enGui.log
27 Oct,2004 11:54:33 47,916 startup.log
dir count = 2, file count = 2
```

Step 2

To query only
                                       			 command syntax, at the CLI prompt enter ? , which
                                       			 represents the command name or the command and parameter.

If you enter a
                                                      				  question mark ( ? )
                                                      				  after a menu command, such as set , the
                                                      				  question mark functions like the Tab key
                                                      				  and lists the commands that are available.

### Example:

```
admin:file list activelog?Syntax:
file list activelog file-spec [options]
file-spec mandatory file to view
options optional page|detail|reverse|[date|size]
```

## End CLI Session

To end a CLI
                                       			 session, enter quit at the CLI prompt.

## Unsupported VMware
                        	 Commands

The following list shows the VMware commands currently not supported.

show environment fans

show environment
                                    				power-supply

show environment
                                    				temperatures

show memory size

show memory count

show memory modules all

utils create report
                                    				hardware

utils snmp hardware-agents
                                    				restart

utils snmp hardware-agents
                                    				start

utils snmp hardware-agents
                                    				status

utils snmp hardware-agents
                                    				stop

| Note | The File I/O Reporting Service (FIOR) provides a kernel-based daemon
                                          			 for collecting file I/O per process. It must be enabled from the CLI; it is
                                          			 disabled by default. |
|---|---|

| Step 1 | Depending on
                                       			 your method of access, do one of the following actions: From a remote
                                             				  system, use SSH to connect securely to the Emergency Responder platform. In
                                             				  your SSH client, enter: ssh adminname @ hostname adminnam specifies the administrator ID and hostname specifies the hostname that was defined during
                                             				  installation. For example, ssh
                                                					 admin@cer-1 From a direct
                                             				  connection, you receive this prompt automatically: cer-1 login: cer-1 represents the host name of the system. Enter the
                                             				  administrator ID that was defined during installation. |
|---|---|
| Step 2 | Enter the
                                       			 password that was defined at installation. The CLI prompt
                                          				appears. The prompt represents the administrator ID; for example: admin: You can now use
                                          				any CLI command. |

| Step 1 | To get detailed
                                       			 help, at the CLI prompt enter the help command
                                       			 which specifies the command name or the command and parameter. Example: admin:help file list activelog
activelog help:
This will list active logging files

options are:
page - pause output
detail - show detailed listing
reverse - reverse sort order
date - sort by date
size - sort by size

file-spec can contain '*' as wildcards

Example:
admin:file list activelog platform detail
02 Dec,2004 12:00:59 <dir> drf
02 Dec,2004 12:00:59 <dir> log
16 Nov,2004 21:45:43 8,557 enGui.log
27 Oct,2004 11:54:33 47,916 startup.log
dir count = 2, file count = 2 |
|---|---|
| Step 2 | To query only
                                       			 command syntax, at the CLI prompt enter ? , which
                                       			 represents the command name or the command and parameter. Note If you enter a
                                                      				  question mark ( ? )
                                                      				  after a menu command, such as set , the
                                                      				  question mark functions like the Tab key
                                                      				  and lists the commands that are available. Example: admin:file list activelog?Syntax:
file list activelog file-spec [options]
file-spec mandatory file to view
options optional page\|detail\|reverse\|[date\|size] | Note | If you enter a
                                                      				  question mark ( ? )
                                                      				  after a menu command, such as set , the
                                                      				  question mark functions like the Tab key
                                                      				  and lists the commands that are available. |
| Note | If you enter a
                                                      				  question mark ( ? )
                                                      				  after a menu command, such as set , the
                                                      				  question mark functions like the Tab key
                                                      				  and lists the commands that are available. |

| Note | If you enter a
                                                      				  question mark ( ? )
                                                      				  after a menu command, such as set , the
                                                      				  question mark functions like the Tab key
                                                      				  and lists the commands that are available. |
|---|---|

| To end a CLI
                                       			 session, enter quit at the CLI prompt. If you are
                                       			 logged in remotely, you are logged off and the SSH session is drops. If you are
                                       			 logged in locally, you are logged off and the login prompt returns. |
|---|