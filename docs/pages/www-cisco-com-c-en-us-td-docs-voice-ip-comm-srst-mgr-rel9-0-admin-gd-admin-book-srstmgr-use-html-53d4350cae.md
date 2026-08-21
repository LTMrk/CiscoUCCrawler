---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-admin-gd-admin-book-srstmgr-use-html-53d4350cae
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/Admin_Book/srstmgr_use.html
retrieved_at: 2026-08-21T23:40:12.454639+00:00
---

Administration Guide for Cisco Unified SRST Manager

# Administration Guide for Cisco Unified SRST Manager

Updated: August 11, 2014

Chapter: How to Use the Cisco Unified SRST Manager CLI

## Chapter: How to Use the Cisco Unified SRST Manager CLI

## How to Use the Cisco Unified SRST Manager CLI

This chapter provides helpful tips for understanding and configuring the Cisco Unified SRST Manager software using the CLI.

## About the Cisco Unified SRST Manager CLI

The Cisco Unified SRST Manager command line interface (CLI) provides additional administrative functionality beyond the GUI. Access the CLI using a secure shell (ssh) client.

Cisco Unified SRST Manager CLI commands have a structure similar to that of Cisco IOS CLI commands. For both interfaces, standard Cisco IOS navigation and command-completion conventions apply. For example, ? lists options, TAB completes a command, and | directs show command output.

The following are differences between the Cisco Unified SRST Manager CLI and the Cisco IOS CLI:

- Standard command names and options do not necessarily apply. A notable example is the command for accessing global configuration mode: the Cisco IOS command is configure terminal ; the network module command is config terminal or config t .

- Cisco Unified SRST Manager employs a last-one-wins rule. For example, if two users both try to set the IP address for the same entity at the same time, the system starts and completes one operation before it starts the next. The last IP address set is the final result.

- The Cisco Unified SRST Manager command modes, EXEC and configuration operate similarly to the EXEC and configuration modes in the Cisco IOS CLI.

- After you enter configuration mode, all the CLI commands can be used in the no form. Example:

no hostname < hostname >

This command deletes the configured hostname.

## Understanding Command Modes

The Cisco Unified SRST Manager command environment is divided into two basic modes:

- EXEC—This is the mode that you are in after you log in to the Cisco Unified SRST Manager command environment. Some Cisco Unified SRST Manager EXEC commands only display or clear parameter values, stop or start the entire system, or start troubleshooting procedures. However, unlike Cisco IOS EXEC mode, Cisco Unified SRST Manager EXEC mode has a few commands that change parameter values.

- Configuration—This mode enables you to make system configuration changes, which are stored in the running configuration. If you later save the running configuration to the startup configuration, the changes made with the configuration commands are restored when you reboot the software.

Cisco Unified SRST Manager configuration mode has various subconfiguration levels. The global configuration mode changes the command environment from EXEC to configuration. You can modify many software parameters at this level. However, certain configuration commands change the environment to more specific configuration modes where modifications to the system are entered. For example, the interface ethernet 0 command changes the environment from config to config-interface. At this point, you can enter or modify interface parameter values.

The commands available to you at any given time depend on the current mode. Entering a question mark ( ? ) at the CLI prompt displays a list of commands available for each command mode. The descriptions in this command reference indicate each command’s environment mode.

Table 15 describes how to access and exit various common command modes of the Cisco Unified SRST Manager software. It also shows examples of the prompts displayed for each mode.

Table 15 Accessing and Exiting Command Modes

EXEC

9.0 and later

When the prompt appears, you can enter the enable command, but it is not necessary.

Press CTRL-SHIFT-6 and then enter x .

configuration

9.0 and later

From EXEC mode, use the configure terminal command.

To return to EXEC mode from configuration mode, use the end or exit command.

AAA accounting

8.0 and later

From configuration mode, use the aaa accounting server remote command.

To return to configuration mode, use the end or exit command.

AAA accounting event

8.0 and later

From configuration mode, use the aaa accounting event command.

To return to configuration mode, use the end or exit command.

AAA accounting policy

8.0 and later

From configuration mode, use the aaa policy command.

To return to configuration mode, use the end or exit command.

backup schedule

9.0 and later

From EXEC mode, use the backup schedule command.

To return to EXEC mode, use the end or exit command.

kron-schedule

9.0 and later

From EXEC mode, use the kron schedule command.

To return to EXEC mode, use the end or exit command.

## Entering the Command Environment

After you install Cisco Unified SRST Manager and establish IP connectivity with it, use this procedure to enter the command environment.

Note This procedure describes how to enter the Cisco Unified SRST Manager command environment remotely. From the server hosting the Cisco Unified SRST Manager VM, it is possible to enter the command environment by opening a console window for the VM within the vSphere client. When using this method, the IP address, username, and password are not required.

### Prerequisites

The following information is required to enter the command environment:

- IP address of the Cisco Unified SRST Manager VM

- Username and password to log in to Cisco Unified SRST Manager

### Summary Steps

1. Connect to Cisco Unified SRST Manager using ssh:

ssh username @ IP_address

2. When prompted, enter the Cisco Unified SRST Manager password.

### Detailed Steps

Step 1

Connect to Cisco Unified SRST Manager using ssh:

Use a secure shell client to connect.

username —User name for Cisco Unified SRST Manager

IP_address —IP address of the Cisco Unified SRST Manager VM

Step 2

When prompted, enter the Cisco Unified SRST Manager password.

After entering the password, Cisco Unified SRST Manager displays the command prompt.

## Exiting the Command Environment

To leave the Cisco Unified SRST Manager command environment, in EXEC mode enter the exit command once to exit EXEC mode, and again to exit the application.

The following example illustrates the exit procedure:

## Getting Help

Entering a question mark ( ? ) at the CLI prompt displays a list of commands available for each command mode. You can also get a list of keywords and arguments associated with any command by using the context-sensitive help feature.

To get help specific to a command mode, a command, a keyword, or an argument, use one of the following commands:

Provides a brief description of the help system in any command mode.

Provides a list of commands that begin with a particular character string. (No space between command and question mark.)

Completes a partial command name.

Lists all commands available for a particular command mode.

Lists the keywords or arguments that you must enter next on the command line. (Space between command and question mark.)

## Using the no and default Forms of Commands

Where available, use the no form of a command to disable a function. Use the command without the no keyword to reenable a disabled function or to enable a function that is disabled by default. The command reference entry for each command provides the complete syntax for the configuration commands and describes what the no form of a command does.

Configuration commands can also have a default form, which returns the command settings to the default values. In those cases where a command is disabled by default, using the default form has the same result as using the no form of the command. However, some commands are enabled by default and have variables set to certain default values. In these cases, the default form of the command enables the command and sets the variables to their default values. Where available, the command reference entry describes the effect of the default form of a command if the command does not function the same way as the no form.

## Saving Configuration Changes

Starting in EXEC mode, use the following command to copy the running configuration in flash memory to another location:

ftp: user-id : password @

Username and password for the FTP server. Include the colon (:) and the at sign (@) in your entry.

ftp-server-address

IP address of the FTP server.

/ directory

(Optional) Directory on the FTP server where the copied file will reside. If you use it, precede the name with the forward slash (/).

startup-config

Startup configuration in flash memory.

tftp: tftp-server-address

IP address of the TFTP server.

filename

Name of the destination file that will contain the copied running configuration.

When you copy the running configuration to the startup configuration, enter the command on one line. In the following example, the running configuration is copied to the startup configuration as a file start. In this instance, enter the command on a single line.

When you copy to the FTP or TFTP server, this command becomes interactive and prompts you for the information. You cannot enter the parameters on one line. The following example illustrates this process. In the following example, the running configuration is copied to the FTP server, which requires a username and password. The IP address of the FTP server is 192.0.2.24. The running configuration is copied to the configs directory as file saved_start.

## Troubleshooting Configuration Changes

Problem You lost some configuration data.

Recommended Action Copy your changes to the running configuration at frequent intervals. See the “Copying Configurations” section .

Problem You lost configuration data when you rebooted the system.

Explanation You did not save the data before the reboot.

Recommended Action Issue a copy running-config startup-config command to copy your changes from the running configuration to the startup configuration. When Cisco Unified SRST Manager reboots, it reloads the startup configuration.

Note All configuration changes require an explicit “save configuration” operation to preserve them in the startup configuration.

| Command Mode | Release | Access Method | Prompt | Exit Method |
|---|---|---|---|---|
| EXEC | 9.0 and later | When the prompt appears, you can enter the enable command, but it is not necessary. | with enable: srstmgr# without enable: srstmgr> | Press CTRL-SHIFT-6 and then enter x . |
| configuration | 9.0 and later | From EXEC mode, use the configure terminal command. | srstmgr(config)# | To return to EXEC mode from configuration mode, use the end or exit command. |
| AAA accounting | 8.0 and later | From configuration mode, use the aaa accounting server remote command. | srstmgr-1(aaa-accounting)# | To return to configuration mode, use the end or exit command. |
| AAA accounting event | 8.0 and later | From configuration mode, use the aaa accounting event command. | srstmgr-1(aaa-accounting-event)# | To return to configuration mode, use the end or exit command. |
| AAA accounting policy | 8.0 and later | From configuration mode, use the aaa policy command. | srstmgr-1(aaa-policy)# | To return to configuration mode, use the end or exit command. |
| backup schedule | 9.0 and later | From EXEC mode, use the backup schedule command. | srstmgr(backup-schedule)# | To return to EXEC mode, use the end or exit command. |
| kron-schedule | 9.0 and later | From EXEC mode, use the kron schedule command. | srstmgr(kron-schedule)# | To return to EXEC mode, use the end or exit command. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Connect to Cisco Unified SRST Manager using ssh: ssh username @ IP_address C:\> ssh admin@10.0.0.0 | Use a secure shell client to connect. username —User name for Cisco Unified SRST Manager IP_address —IP address of the Cisco Unified SRST Manager VM |
| Step 2 | When prompted, enter the Cisco Unified SRST Manager password. Password: se-10-0-0-0# | After entering the password, Cisco Unified SRST Manager displays the command prompt. |

| Command | Purpose |
|---|---|
| help | Provides a brief description of the help system in any command mode. |
| abbreviated-command-entry ? | Provides a list of commands that begin with a particular character string. (No space between command and question mark.) |
| abbreviated-command-entry < Tab > | Completes a partial command name. |
| ? | Lists all commands available for a particular command mode. |
| command ? | Lists the keywords or arguments that you must enter next on the command line. (Space between command and question mark.) |

| Keyword or Argument | Description |
|---|---|
| ftp: user-id : password @ | Username and password for the FTP server. Include the colon (:) and the at sign (@) in your entry. |
| ftp-server-address | IP address of the FTP server. |
| / directory | (Optional) Directory on the FTP server where the copied file will reside. If you use it, precede the name with the forward slash (/). |
| startup-config | Startup configuration in flash memory. |
| tftp: tftp-server-address | IP address of the TFTP server. |
| filename | Name of the destination file that will contain the copied running configuration. |