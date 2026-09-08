---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-plm-10-5-1-userguide-cplm-bk-ud1156ad-00-user-guide-rel-1051-cplm-bk-ud-57f4068c1a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/plm/10_5_1/userguide/CPLM_BK_UD1156AD_00_user-guide-rel-1051/CPLM_BK_UD1156AD_00_user-guide-rel-1051_appendix_0110.html
retrieved_at: 2026-09-08T05:03:23.603121+00:00
---

Cisco Prime License Manager User Guide, Release 10.5(1)

# Cisco Prime License Manager User Guide, Release 10.5(1)

Updated: July 30, 2014

Chapter: Cisco Prime License Manager CLI Commands

## Chapter: Cisco Prime License Manager CLI Commands

# Cisco Prime License Manager CLI Commands

## Introduction

The commands in this section are specific to Cisco Prime License Manager. For platform-specific commands, see Command Line Interface Guide for Cisco Unified Communications Solutions .

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
	 change user

This command takes
		  parameters interactively and changes the username or password of the
		  administrator.

license management change user { name | password }

## Syntax Description

Specifies
					 the administrator username.

Specifies
					 the administrator password.

The
						password must be at least six characters long, and can contain any combination
						of alphanumeric characters or the following special characters: underscore (_),
						exclamation mark (!), at sign (@), pound sign (#), dollar sign ($), percentage
						sign (%), caret (^), and ampersand (&).

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

| Parameters | Description |
|---|---|
| diagnose | Prints diagnostic information of the selected file. |
| get | Creates a TAR file of the license file(s) on the system and
					 transfers the TAR file to a remote area. |

| Parameters | Description |
|---|---|
| name | Specifies
					 the administrator username. |
| password | Specifies
					 the administrator password. Note The
						password must be at least six characters long, and can contain any combination
						of alphanumeric characters or the following special characters: underscore (_),
						exclamation mark (!), at sign (@), pound sign (#), dollar sign ($), percentage
						sign (%), caret (^), and ampersand (&). | Note | The
						password must be at least six characters long, and can contain any combination
						of alphanumeric characters or the following special characters: underscore (_),
						exclamation mark (!), at sign (@), pound sign (#), dollar sign ($), percentage
						sign (%), caret (^), and ampersand (&). |
| Note | The
						password must be at least six characters long, and can contain any combination
						of alphanumeric characters or the following special characters: underscore (_),
						exclamation mark (!), at sign (@), pound sign (#), dollar sign ($), percentage
						sign (%), caret (^), and ampersand (&). |

| Note | The
						password must be at least six characters long, and can contain any combination
						of alphanumeric characters or the following special characters: underscore (_),
						exclamation mark (!), at sign (@), pound sign (#), dollar sign ($), percentage
						sign (%), caret (^), and ampersand (&). |
|---|---|

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