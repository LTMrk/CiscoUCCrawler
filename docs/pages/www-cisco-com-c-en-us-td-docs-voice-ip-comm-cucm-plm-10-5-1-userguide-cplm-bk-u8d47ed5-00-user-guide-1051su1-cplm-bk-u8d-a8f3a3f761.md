---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-plm-10-5-1-userguide-cplm-bk-u8d47ed5-00-user-guide-1051su1-cplm-bk-u8d-a8f3a3f761
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/plm/10_5_1/userguide/CPLM_BK_U8D47ED5_00_user-guide-1051su1/CPLM_BK_U8D47ED5_00_user-guide-1051su1_appendix_0110.html
retrieved_at: 2026-09-08T05:02:46.092591+00:00
---

Cisco Prime License Manager User Guide, Release 10.5(1)SU1

# Cisco Prime License Manager User Guide, Release 10.5(1)SU1

Updated: October 23, 2014

Chapter: Cisco Prime License Manager CLI Commands

## Chapter: Cisco Prime License Manager CLI Commands

# Cisco Prime License Manager CLI Commands

## Introduction

The commands in this section are specific to Cisco Prime License Manager. For platform-specific commands, see the Command Line Interface Guide for Cisco Unified Communications Solutions .

## license
	 file

This command asks to select a license file from a list.

license file { diagnose | get }

## Syntax Description

Prints diagnostic information of the selected file.

Creates a TAR file of the license file(s) on the system and
					 transfers the TAR file to a remote area.

## Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Enterprise License Manager , Cisco Prime License Manager

## license management
	 change user name

This command takes parameters interactively and changes the username
		  of the administrator.

license management change user { name }

## Syntax Description

Specifies the administrator username.

## Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Enterprise License Manager , Cisco Prime License Manager

## license management
	 reset user password

This command
		  takes parameters interactively and changes the username of the administrator.

license management reset user { password }

## Syntax Description

Specifies
					 the administrator password.

## Command Modes

Administrator (admin:)

### Requirements

Command privilege
		  level: 1

Allowed during
		  upgrade: Yes

Applies to: Cisco
			 Prime License Manager

## license management
	 list users

This command lists
		  the administrative users.

license management list users

## Command Modes

Administrator (admin:)

### Requirements

Command privilege
		  level: 1

Allowed during
		  upgrade: Yes

Applies to: Enterprise
			 License Manager , Cisco Prime License Manager

## license management
	 product re-register all

This command
		  forces re-registration of all product instances associated with this Enterprise
		  License Manager/Cisco Prime License Manager server. This command may take some
		  time for re-registration and synchronization with all product instances to
		  complete.

license management product re-register all

## Command Modes

Administrator (admin:)

### Requirements

Command privilege
		  level: 1

Allowed during
		  upgrade: Yes

Applies to: Enterprise
			 License Manager , Cisco
			 Prime License Manager

## license management
	 reset

This command resets the identity, store data, and essentially removes
		  all the installed licenses. It also restarts the Cisco Prime License Manager
		  server process to make the changes effective.

license management reset { identity | registration }

## Syntax Description

Resets the identity

Resets the registration

## Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Enterprise License Manager , Cisco Prime License Manager

## license management
	 security update

This command
		  downloads Cisco Prime License Manager security update from the specified remote
		  server location and installs the contents of the specified security update
		  file.

license management security update

### Requirements

Command privilege
		  level: 1

Allowed during
		  upgrade: Yes

Applies to: Enterprise
			 License Manager , Cisco
			 Prime License Manager

## license management
	 service

This command activates or deactivates a given service on the Cisco
		  Prime License Manager server.

license management service { activate | deactivate }

## Syntax Description

Activates a given service on the Cisco Prime License Manager
					 server.

Deactivates a given service on the Cisco Prime License Manager
					 server.

## Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Enterprise License Manager , Cisco Prime License Manager

## license management
	 show system

This command lists the administrative users.

license management show system

## Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Enterprise License Manager , Cisco Prime License Manager

## license management
	 system remove

This command
		  allows you to remove an unused Cisco Prime License Manager instance from a
		  coresident deployment.

license management system remove

## Command Modes

Administrator (admin:)

### Requirements

Command privilege
		  level: 0

Allowed during
		  upgrade: Yes

Applies to: Cisco
		  Prime License Manager

| Parameters | Description |
|---|---|
| diagnose | Prints diagnostic information of the selected file. |
| get | Creates a TAR file of the license file(s) on the system and
					 transfers the TAR file to a remote area. |

| Parameters | Description |
|---|---|
| name | Specifies the administrator username. |

| Parameters | Description |
|---|---|
| password | Specifies
					 the administrator password. |

| Parameters | Description |
|---|---|
| identity | Resets the identity |
| registration | Resets the registration |

| Parameters | Description |
|---|---|
| activate | Activates a given service on the Cisco Prime License Manager
					 server. |
| deactivate | Deactivates a given service on the Cisco Prime License Manager
					 server. |