---
doc_id: www-cisco-com-c-en-us-td-docs-routers-access-vg450-software-configuration-guide-vg450-scg-vg450-scg-chapter-00-html-39f14f6f86
source_url: https://www.cisco.com/c/en/us/td/docs/routers/access/vg450/software/configuration/guide/vg450-scg/vg450-scg_chapter_00.html
retrieved_at: 2026-08-22T01:15:01.084641+00:00
---

Cisco VG450 Voice Gateway Software Configuration Guide

# Cisco VG450 Voice Gateway Software Configuration Guide

Updated: April 22, 2022

Chapter: Understanding Interface Numbering and Cisco IOS Software Basics

## Chapter: Understanding Interface Numbering and Cisco IOS Software Basics

# Understanding Interface Numbering and Cisco IOS Software Basics

## Understanding Interface Numbering and Cisco IOS Software Basics

This chapter provides an overview of interface numbering in the Cisco VG450 Voice Gateways (VG). It also describes how to
                           use the Cisco IOS software commands.

This chapter presents the following major topics:

### Identifying Cisco VG450

The following figure shows the front panels of the Cisco VG450 Voice Gateway Chassis:

#### Cisco VG450 Port Numbering Conventions

The following figure shows the Cisco VG450 back panel:

### Understanding Cisco IOS Software Basics

This section describes what you need to know about the Cisco IOS software before you configure the router using the CLI. This
                              chapter includes the following:

Understanding these concepts will save time as you begin to use the commands. If you have never used Cisco IOS software or
                              need a refresher, take a few minutes to read this chapter before you proceed to the next chapter.

If you are already familiar with Cisco IOS software, proceed to the “Configuring the Host Name and Password” section on page 2-1

#### Getting Help

Use the question mark (?) and arrow keys to help you enter commands:

- For a list of available commands, enter a question mark:

```
Router> ?
```

- To complete a command, enter a few known characters followed by a question mark (with no space):

```
Router> s?
```

- For a list of command variables, enter the command followed by a space and a question mark:

```
Router> show ?
```

- To redisplay a command you previously entered, press the Up Arrow key. You can continue to press the Up Arrow key for more
                                    commands.

#### Command Modes

The Cisco IOS user interface is divided into different modes. Each command mode permits you to configure different components
                                 on your router. The commands available at any given time depend on which mode you are currently in. Entering a question mark
                                 ( ? ) at the prompt displays a list of commands available for each command mode. The following table lists the most common command
                                 modes.

Command Mode

Access Method

Router Prompt Displayed

Exit Method

User EXEC

Log in.

Router>

Use the logout command.

Privileged EXEC

From user EXEC mode, enter the enable command.

Router#

To exit to user EXEC mode, use the disable , exit , or logout command.

Global configuration

From the privileged EXEC mode, enter the configure terminal command.

Router (config)#

To exit to privileged EXEC mode, use the exit or end command, or press Ctrl-Z .

Interface configuration

From the global configuration mode, enter the GigabitEthernet interface command such as, gigabitethernet0/0 .

Router (config-if)#

To exit to global configuration mode, use the exit command.

To exit directly to privileged EXEC mode, press Ctrl-Z .

Timesaver

Each command mode restricts you to a subset of commands. If you are having trouble entering a command, check the prompt, and
                                             enter the question mark (?) for a list of available commands. You might be in the wrong command mode or be using the wrong
                                             syntax.

In the following example, notice how the prompt changes after each command, to indicate a new command mode for Cisco VG450:

```
Router> enable Password: <enable password> Router# configure terminal Router(config)# interface gigabitEthernet 0/0/0 Router#
%SYS-5-CONFIG_I: Configured from console by console
```

The last message is normal and does not indicate an error. Press Return to get the Router# prompt.

#### Undoing a Command or Feature

If you want to undo a command you entered or disable a feature, enter the keyword no before most commands; for example, no ip routing .

#### Saving Configuration Changes

You need to enter the copy running-config startup-config command to save your configuration changes to nonvolatile random-access memory (NVRAM), so the changes are not lost if there
                                 is a system reload or power outage. For example:

```
Router# copy running-config startup-config Building configuration...
```

It might take a minute or two to save the configuration to NVRAM. After the configuration has been saved, the following appears:

```
[OK]
Router#
```

### Upgrading to a New Cisco IOS Release

To install or upgrade to a new Cisco IOS release, see How to Update/Upgrade Cisco IOS Software .

### Where to Go Next

Now that you have learned some Cisco IOS software basics, you can begin to configure the router using the CLI.

Remember that:

- You can use the question mark (?) and arrow keys to help you enter commands.

- Each command mode restricts you to a set of commands. If you have difficulty entering a command, check the prompt and then
                                 enter the question mark ( ? ) for a list of available commands. You might be in the wrong command mode or be using the wrong syntax.

- To disable a feature, generally enter the keyword no before the command; for example, no ip routing .

- You need to save your configuration changes to NVRAM so the changes are not lost if there is a system reload or power outage.

Proceed to Chapter 2, “Configuring the Host Name and Password,” to begin configuring the router.

| Command Mode | Access Method | Router Prompt Displayed | Exit Method |
|---|---|---|---|
| User EXEC | Log in. | Router> | Use the logout command. |
| Privileged EXEC | From user EXEC mode, enter the enable command. | Router# | To exit to user EXEC mode, use the disable , exit , or logout command. |
| Global configuration | From the privileged EXEC mode, enter the configure terminal command. | Router (config)# | To exit to privileged EXEC mode, use the exit or end command, or press Ctrl-Z . |
| Interface configuration | From the global configuration mode, enter the GigabitEthernet interface command such as, gigabitethernet0/0 . | Router (config-if)# | To exit to global configuration mode, use the exit command. To exit directly to privileged EXEC mode, press Ctrl-Z . |

| Timesaver | Each command mode restricts you to a subset of commands. If you are having trouble entering a command, check the prompt, and
                                             enter the question mark (?) for a list of available commands. You might be in the wrong command mode or be using the wrong
                                             syntax. |
|---|---|

| Note | Press Ctrl-Z in any mode to immediately return to enable mode (
                                          Router#
                                          ), instead of entering exit , which returns you to the previous mode. |
|---|---|