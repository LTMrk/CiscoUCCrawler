---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-cli-ref-12-5-1su6-cucm-b-cli-reference-guide-release1251su6-cucm-b-cli--62fea9c53a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/cli_ref/12_5_1SU6/cucm_b_cli_reference-guide_release1251SU6/cucm_b_cli_reference_guide_release_1401_chapter_01.html
retrieved_at: 2026-08-16T23:56:19.542553+00:00
---

Command Line Interface Reference Guide for Cisco Unified Communications Solutions, Release 12.5(1)SU6

# Command Line Interface Reference Guide for Cisco Unified Communications Solutions, Release 12.5(1)SU6

Updated: October 3, 2023

Chapter: About CLI

## Chapter: About CLI

# About CLI

## CLI Privilege
                        	 Levels

Administrator with level 0 privilege—This administrator has read-only access privilege on the interface.

Administrator with level 1 privilege—This administrator has both read and write access privilege on the interface.

After the
                              		  administrators with the various privileges are created, you can start the CLI
                              		  session.

## Start CLI session

This procedure applies to both Unified Communications Manager and the IM and Presence Service. The Operating System for Unified
                                          Communications Manager is called the Cisco Unified Operating System. The Operating System for the IM and Presence Service
                                          is called the Unified IM and Presence Operating System. To start a CLI session for the IM and Presence Service, you must use
                                          the Unified IM and Presence Operating System.

You can access the Cisco Unified Operating System (or, for the IM and Presence Service, the Unified IM and Presence Operating System) remotely or locally:

- From a web client
                                 			 workstation, such as the workstation that you use for Cisco Unified Operating
                                 			 System Administration, you can use SSH to connect securely to the Cisco Unified
                                 			 Operating System.

- You can access the Cisco
                                 			 Unified Operating System CLI directly by using the monitor and keyboard that
                                 			 you used during installation or by using a terminal server that is connected to
                                 			 the serial port. Use this method if a problem exists with the IP address.

### Before you begin

Ensure you have the following information that is defined
                              		  during installation:

- A primary IP address and
                                 			 hostname

- An administrator ID

- A password

You will need this information to log in to the Cisco Unified
                              		  Operating System.

Step 1

Perform one of the following actions depending on your method of
                                       			 access:

From a remote system, use SSH to connect securely to the Cisco
                                             				  Unified Operating System. In your SSH client, enter

ssh adminname@hostname

where adminname specifies the Administrator ID and hostname specifies the hostname that was
                                                					 defined during installation.

For example, ssh admin@ipt-1 .

From a direct connection, you receive this prompt
                                             				  automatically:

```
ipt-1 login:
```

where ipt-1 represents the host name of the
                                                					 system.

Enter the administrator ID that was defined during
                                                					 installation.

Step 2

Enter the password that was defined at installation.

The CLI prompt displays. The prompt represents the Administrator
                                          				ID; for example:

```
admin:
```

You can now use any CLI command.

## Tab completes command

To complete commands, use Tab:

Enter the start of a command and press Tab to complete the command. For example, if
                                    				you enter se and press Tab , set is completed.

Enter a full command name and press Tab to display all the commands or
                                    				subcommands that are available. For example, if you enter set and press Tab , you see all the set subcommands. An *
                                    				identifies the commands that have subcommands.

If you reach a command, keep pressing Tab , and the current command line repeats;
                                    				this indicates that no additional expansion is available.

## Command help

You can get two kinds of help about any command:

Detailed help that includes a definition of the command and an
                                    				example of its use

Short query help that includes only command syntax

If you want to:

At the CLI prompt:

Get detailed help

Enter

help command

Where command specifies the command name or the
                                          						command and parameter. See "Detailed Help Example."

Query only command syntax

Enter

command ?

Where command represents the command name or the
                                          						command and parameter. See "Query Example."

### Troubleshooting Tips

If you enter a ? after a menu command, such as set, it acts like the Tab key and lists the commands that are
                              		  available.

### Detailed Help Example:

```
admin:help file list activelog
activelog help:
This will list active logging files

options are:
page    - pause output
detail  - show detailed listing
reverse - reverse sort order
date    - sort by date
size    - sort by size

file-spec can contain '*' as wildcards

Example:
admin:file list activelog platform detail
02 Dec,2004 12:00:59      <dir>    drf
02 Dec,2004 12:00:59      <dir>    log
16 Nov,2004 21:45:43        8,557  enGui.log
27 Oct,2004 11:54:33       47,916  startup.log
dir count = 2, file count = 2
```

### Query Example:

```
admin:file list activelog?Syntax:
file list activelog file-spec [options]
file-spec   mandatory   file to view
options     optional    page|detail|reverse|[date|size]
```

## Ctrl-C exits command

You can stop most interactive commands by entering the Ctrl-C key sequence, as shown in the following
                              		  example:

### Exiting a Command with Ctrl-C

```
admin:utils system upgrade initiateWarning: Do not close this window without first exiting the upgrade command.
Source:
1) Remote Filesystem
2) DVD/CD
q) quit
Please select an option (1 - 2 or "q" ):
Exiting upgrade command. Please wait...
Control-C pressed
admin:
```

If you execute the command utils system switch-version and enter Yes to start the process, entering Ctrl-C exits the command but does not stop the
                                          			 switch-version process.

## Quit CLI session

At the CLI prompt, enter quit . If you are logged in remotely, you get logged
                              		  off, and the ssh session is dropped. If you are logged in locally, you get
                              		  logged off, and the login prompt returns.

| Note | Administrators can execute CLI commands based on the privileges defined for each of them. |
|---|---|

| Note | This procedure applies to both Unified Communications Manager and the IM and Presence Service. The Operating System for Unified
                                          Communications Manager is called the Cisco Unified Operating System. The Operating System for the IM and Presence Service
                                          is called the Unified IM and Presence Operating System. To start a CLI session for the IM and Presence Service, you must use
                                          the Unified IM and Presence Operating System. |
|---|---|

| Step 1 | Perform one of the following actions depending on your method of
                                       			 access: From a remote system, use SSH to connect securely to the Cisco
                                             				  Unified Operating System. In your SSH client, enter ssh adminname@hostname where adminname specifies the Administrator ID and hostname specifies the hostname that was
                                                					 defined during installation. For example, ssh admin@ipt-1 . From a direct connection, you receive this prompt
                                             				  automatically: ipt-1 login: where ipt-1 represents the host name of the
                                                					 system. Enter the administrator ID that was defined during
                                                					 installation. |
|---|---|
| Step 2 | Enter the password that was defined at installation. The CLI prompt displays. The prompt represents the Administrator
                                          				ID; for example: admin: You can now use any CLI command. |

| If you want to: | At the CLI prompt: |
|---|---|
| Get detailed help | Enter help command Where command specifies the command name or the
                                          						command and parameter. See "Detailed Help Example." |
| Query only command syntax | Enter command ? Where command represents the command name or the
                                          						command and parameter. See "Query Example." |

| Note | If you execute the command utils system switch-version and enter Yes to start the process, entering Ctrl-C exits the command but does not stop the
                                          			 switch-version process. |
|---|---|