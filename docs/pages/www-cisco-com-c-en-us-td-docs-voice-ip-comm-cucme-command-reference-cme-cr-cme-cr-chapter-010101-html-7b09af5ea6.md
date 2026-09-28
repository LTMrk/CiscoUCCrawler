---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-command-reference-cme-cr-cme-cr-chapter-010101-html-7b09af5ea6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/command/reference/cme_cr/cme_cr_chapter_010101.html
retrieved_at: 2026-08-21T22:57:25.927733+00:00
---

Cisco Unified Communications Manager Express Command Reference

# Cisco Unified Communications Manager Express Command Reference

Updated: July 19, 2018

Chapter: Cisco Unified CME Commands: W

## Chapter: Cisco Unified CME Commands: W

# Cisco Unified CME Commands: W

## web admin customer

To define a username and password for a Cisco Unified CME customer
                              		  administrator, use the web admin customer command in telephony-service
                              		  configuration mode. To disable a customer administrator login, use the no form of this command.

web admin customer name username { password string | secret { 0 | 5 } string }

no web admin customer

### Syntax Description

name username

Username for the customer administrator. String can contain
                                          						a maximum of 28 alphanumeric characters. Default is Customer.

password string

Character string for login authentication, which will be
                                          						stored in the running configuration as plain text. String can contain a maximum
                                          						of 28 alphanumeric characters. Default is no password.

secret { 0 | 5 } string

Character string for login authentication, which will be
                                          						stored in the running configuration as encrypted using Message Digest 5 (MD5).
                                          						The digit 0 or 5 specifies whether the displayed string that follows is
                                          						encrypted:

- 0 —Password that follows is not
                                             						  encrypted.

- 5 —Password that follows is
                                             						  encrypted.

### Command Default

Default is a customer administrator with username Customer and no
                              		  password.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(11)YT

Cisco ITS 2.1

This command was introduced.

12.2(15)T

Cisco ITS 2.1

This command was integrated into Cisco IOS Release
                                          						12.2(15)T.

Cisco IOS XE Gibraltar 16.11.1a Release

Unified CME 12.6

The command is deprecated. It is not supported on Unified CME 12.6 and later releases.

### Usage Guidelines

This command enables customer administrator access for the Cisco
                              		  Unified CME graphical user interface (GUI).

## Examples

The following example defines a customer administrator named user22
                              		  whose password is pw567890:

```
Router(config)# telephony-service Router(config-telephony)# web admin customer name user22 password pw567890
```

### Related Commands

Description

telephony-service

Enters telephony-service configuration mode.

web customize load

Loads and parses an XML file in router flash memory to
                                          						customize a GUI for a customer administrator.

## web admin system

To define a username and password so that a system administrator can
                              		  log in to the Cisco Unified CME router through a web browser, use the web admin system command in telephony-service configuration
                              		  mode. To disable a system administrator login, use the no form of this command.

web admin system [ name username ] [ password string | secret { 0 | 5 } string ]

no web admin system

### Syntax Description

name username

(Optional) Unique alphanumeric string to identify a user
                                          						for this authentication credential only. String can contain a maximum of 28
                                          						alphanumeric characters. Default name is Admin.

password string

(Optional) Unique alphanumeric string to be used by the
                                          						system administrator which will be stored in the running configuration as plain
                                          						text. This password is typically known by more than one administrator user and
                                          						may be created for the default system administrator username. String can
                                          						contain a maximum of 28 alphanumeric characters. Default is no password.

secret { 0 | 5 } string

(Optional) Unique alphanumeric string for a secret password
                                          						which will be stored in the running configuration as unencrypted plain text or
                                          						as encrypted using Message Digest 5 (MD5). This password is typically known by
                                          						only a select number of administrator users.

- 0 —Save string as unencrypted plain text
                                             						  in running configuration..

- 5 —Save encrypted string in running configuration.

### Command Default

Default is a system administrator with username Admin and no
                              		  password.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(11)YT

Cisco ITS 2.1

This command was introduced.

12.2(15)T

Cisco ITS 2.1

This command was integrated into Cisco IOS Release
                                          						12.2(15)T.

Cisco IOS XE Gibraltar 16.11.1a Release

Unified CME 12.6

The command is deprecated. It is not supported on Unified CME 12.6 and later releases.

### Usage Guidelines

This command enables system administrator access for the Cisco
                              		  Unified CME graphical user interface (GUI).

The user name parameter of any authentication credential must be
                              		  unique. Do not use the same value for a user name when you configure any two or
                              		  more authentication credentials in Cisco Unified CME, such as the username for
                              		  any Cisco United CME GUI account and the user name in a profile for Extension
                              		  Mobility.

Use the secret 5 keyword pair to instruct the system to encrypt the system
                              		  administrator password with MD5 and to save the encrypted version in the
                              		  running configuration.

## Examples

The following example establishes a system administrator named user1
                              		  whose secret password will be encrypted in the running configuration:

```
Router(config)# telephony-service Router(config-telephony)# web admin system name user1 secret 5 pw234567
```

An encrypted version of the preceding string is saved in the running
                              		  configuration, as shown in the following partial example. The digit 5 that
                              		  appears after the secret keyword in the running configuration
                              		  indicates that the password that follows is shown in its encrypted version.

```
Router(config)# show running-config !
!
!
web admin system name user1 secret 5 $1$TCyK$OU/NSQ/VtAU2ibHdi8Uau
```

### Related Commands

Description

telephony-service

Enters telephony-service configuration mode.

## web customize load

To load and parse an eXtensible Markup Language (XML) file in router
                              		  flash memory to customize a Cisco CallManager Express graphic user interface
                              		  (GUI) for a customer administrator, use the web customize load command in telephony-service configuration
                              		  mode. To disable the customized GUI and use the system administrator GUI for
                              		  the customer administrator, use the no form of this command.

web customize load filename

no web customize load

### Syntax Description

filename

Name of the XML file in router flash memory that defines
                                          						the customer administrator GUI.

### Command Default

The standard system administrator GUI is used.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(11)YT

Cisco ITS 2.1

This command was introduced.

12.2(15)T

Cisco ITS 2.1

This command was integrated into Cisco IOS Release
                                          						12.2(15)T.

Cisco IOS XE Gibraltar 16.11.1a Release

Unified CME 12.6

The command is deprecated. It is not supported on Unified CME 12.6 and later releases.

### Usage Guidelines

Use this command with Cisco ITS V2.1and later versions.

## Examples

The following example specifies a file named cust_admin_gui.xml as
                              		  the file that defines the GUI for Cisco CME customer administrators:

```
Router(config)# telephony-service Router(config-telephony)# web customize load cust_admin_gui.xml
```

### Related Commands

Description

telephony-service

Enters telephony-service configuration mode.

| name username | Username for the customer administrator. String can contain
                                          						a maximum of 28 alphanumeric characters. Default is Customer. |
|---|---|
| password string | Character string for login authentication, which will be
                                          						stored in the running configuration as plain text. String can contain a maximum
                                          						of 28 alphanumeric characters. Default is no password. |
| secret { 0 \| 5 } string | Character string for login authentication, which will be
                                          						stored in the running configuration as encrypted using Message Digest 5 (MD5).
                                          						The digit 0 or 5 specifies whether the displayed string that follows is
                                          						encrypted: 0 —Password that follows is not
                                             						  encrypted. 5 —Password that follows is
                                             						  encrypted. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(11)YT | Cisco ITS 2.1 | This command was introduced. |
| 12.2(15)T | Cisco ITS 2.1 | This command was integrated into Cisco IOS Release
                                          						12.2(15)T. |
| Cisco IOS XE Gibraltar 16.11.1a Release | Unified CME 12.6 | The command is deprecated. It is not supported on Unified CME 12.6 and later releases. |

|  | Description |
|---|---|
| telephony-service | Enters telephony-service configuration mode. |
| web customize load | Loads and parses an XML file in router flash memory to
                                          						customize a GUI for a customer administrator. |

| name username | (Optional) Unique alphanumeric string to identify a user
                                          						for this authentication credential only. String can contain a maximum of 28
                                          						alphanumeric characters. Default name is Admin. |
|---|---|
| password string | (Optional) Unique alphanumeric string to be used by the
                                          						system administrator which will be stored in the running configuration as plain
                                          						text. This password is typically known by more than one administrator user and
                                          						may be created for the default system administrator username. String can
                                          						contain a maximum of 28 alphanumeric characters. Default is no password. |
| secret { 0 \| 5 } string | (Optional) Unique alphanumeric string for a secret password
                                          						which will be stored in the running configuration as unencrypted plain text or
                                          						as encrypted using Message Digest 5 (MD5). This password is typically known by
                                          						only a select number of administrator users. 0 —Save string as unencrypted plain text
                                             						  in running configuration.. 5 —Save encrypted string in running configuration. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(11)YT | Cisco ITS 2.1 | This command was introduced. |
| 12.2(15)T | Cisco ITS 2.1 | This command was integrated into Cisco IOS Release
                                          						12.2(15)T. |
| Cisco IOS XE Gibraltar 16.11.1a Release | Unified CME 12.6 | The command is deprecated. It is not supported on Unified CME 12.6 and later releases. |

|  | Description |
|---|---|
| telephony-service | Enters telephony-service configuration mode. |

| filename | Name of the XML file in router flash memory that defines
                                          						the customer administrator GUI. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(11)YT | Cisco ITS 2.1 | This command was introduced. |
| 12.2(15)T | Cisco ITS 2.1 | This command was integrated into Cisco IOS Release
                                          						12.2(15)T. |
| Cisco IOS XE Gibraltar 16.11.1a Release | Unified CME 12.6 | The command is deprecated. It is not supported on Unified CME 12.6 and later releases. |

|  | Description |
|---|---|
| telephony-service | Enters telephony-service configuration mode. |