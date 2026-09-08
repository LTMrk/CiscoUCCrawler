---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-plm-11-5-1-su-1-userguide-cplm-b-user-guide-rel-1151su1-cplm-b-user-gui-927ee92b9d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/plm/11_5_1_SU_1/userguide/cplm_b_user-guide-rel-1151SU1/cplm_b_user-guide-rel-1151a_appendix_0111.html
retrieved_at: 2026-09-08T04:59:29.247337+00:00
---

Cisco Prime License Manager User Guide, Release 11.5(1)SU1

# Cisco Prime License Manager User Guide, Release 11.5(1)SU1

Updated: November 6, 2016

Chapter: Cisco Prime License Manager CLI Commands

## Chapter: Cisco Prime License Manager CLI Commands

# Cisco Prime License Manager CLI Commands

## Introduction

The commands in
		  this section are specific to Cisco Prime License Manager. For platform-specific
		  commands, see the Command Line Interface Guide
			 for Cisco Unified Communications Solutions .

Different command privilege
		  levels for a user are 0,1 and 4.

Privilege

Definition

Privilege level 0

Specifies an ordinary privilege level. Users with ordinary
					 privileges can run CLI commands with privilege level 0 only.

Privilege level 1

Specifies an advanced privilege level. Users with advanced
					 privileges can run CLI commands with privilege level 1 and below.

Privilege level 4

The administrator account that the system creates when Cisco Unified Communications Manager installs has a privilege level of 4. The administrator can run all commands in
					 the CLI.

## license
	 file

This command asks
		  to select a license file from a list.

license file { diagnose | get }

## Syntax Description

Prints
					 diagnostic information of the selected file.

Creates a
					 TAR file of the license file(s) on the system and transfers the TAR file to a
					 remote area.

## Command Modes

Administrator (admin:)

### Requirements

Command privilege level for diagnose : 1
		  and 4

Command privilege level for get : 4

Allowed during
		  upgrade: No

Applies to: Enterprise
			 License Manager , Cisco
			 Prime License Manager

## license management
	 change user name

This command
		  takes parameters interactively and changes the username of the administrator.

license management change user { name }

## Syntax Description

Specifies
					 the administrator username.

## Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 4

Allowed during
		  upgrade: No

Applies to: Enterprise
			 License Manager , Cisco
			 Prime License Manager

## license management
	 reset user password

This command
		  takes parameters interactively and changes the password of the administrator.

license management reset user { password }

## Syntax Description

Specifies
					 the administrator password.

## Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 4

Allowed during
		  upgrade: No

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

Command privilege level: 0,1,
		  and 4

Allowed during
		  upgrade: No

Applies to: Enterprise
			 License Manager , Cisco Prime
			 License Manager

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

Command privilege level: 1
		  and 4

Allowed during
		  upgrade: No

Applies to: Enterprise
			 License Manager , Cisco
			 Prime License Manager

## license management
	 reset

This command
		  resets the identity, store data, and essentially removes all the installed
		  licenses. It also restarts the Cisco Prime License Manager server process to
		  make the changes effective.

license management reset { identity | registration }

## Syntax Description

Resets
					 the identity

Resets
					 the registration

## Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 4

Allowed during
		  upgrade: No

Applies to: Enterprise
			 License Manager , Cisco
			 Prime License Manager

## license management
	 security update

This command
		  downloads Cisco Prime License Manager security update from the specified remote
		  server location and installs the contents of the specified security update
		  file.

license management security update

### Requirements

Command privilege level: 4

Allowed during
		  upgrade: No

Applies to: Enterprise
			 License Manager , Cisco
			 Prime License Manager

## license management
	 service

This command
		  activates or deactivates a given service on the Cisco Prime License Manager
		  server.

license management service { activate | deactivate }

## Syntax Description

Activates
					 a given service on the Cisco Prime License Manager server.

Deactivates a given service on the Cisco Prime License Manager
					 server.

## Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1
		  and 4

Allowed during
		  upgrade: No

Applies to: Enterprise
			 License Manager , Cisco
			 Prime License Manager

## license management set log level

### license management
	 set log level core_services

This command sets
		  the log level for core services.

license
				  management set log level core_services { error | warning | info | debug }

## Syntax Description

Provides
					 runtime errors or unexpected conditions that could be critical.

Provides
					 messages about potential problems.

Provides
					 general information that may be useful. This parameter is set by default.

Provides
					 detailed information about the flow of the process. We recommend that you use
					 set this parameter on an as needed basis only.

## Command Modes

Administrator (admin:)

#### Requirements

Command privilege level: 0,
		  1, and 4

Allowed during
		  upgrade: No

Applies to: Cisco
			 Prime License Manager .

### license management
	 set log level product_instances

This command sets
		  the log level for product instances.

license management set log level product_instances { error | warning | info | debug }

## Syntax Description

Provides
					 runtime errors or unexpected conditions that could be critical.

Provides
					 messages about potential problems.

Provides
					 general information that may be useful. This parameter is set by default.

Provides
					 detailed information about the flow of the process. We recommend that you use
					 set this parameter on an as needed basis only.

## Command Modes

Administrator (admin:)

#### Requirements

Command privilege level:
		  0,1, and 4

Allowed during
		  upgrade: No

Applies to: Cisco
			 Prime License Manager .

## license management show log level

### license management
	 show log level core_services

This command
		  displays the current log level for core services.

license management show log level core_services

## Command Modes

Administrator (admin:)

#### Requirements

Command privilege level: 0

Allowed during
		  upgrade: No

Applies to: Cisco
			 Prime License Manager .

### license management
	 show log level product_instances

This command
		  displays the current log level for product instances.

license management show log level product_instances

## Command Modes

Administrator (admin:)

#### Requirements

Command privilege level:
		  0,1, and 4

Allowed during
		  upgrade: No

Applies to: Cisco
			 Prime License Manager .

## license management
	 show system

This command lists
		  the administrative users.

license management show system

## Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1
		  and 4

Allowed during
		  upgrade: No

Applies to: Enterprise
			 License Manager , Cisco
			 Prime License Manager

## license management
	 system remove

This command
		  allows you to remove an unused Cisco Prime License Manager instance from a
		  coresident deployment.

license management system remove

## Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 4

Allowed during
		  upgrade: No

Applies to: Cisco
		  Prime License Manager

## license client
	 reset registration

This command
		  resets the license client registration state to unregistered.

## Command Modes

Administrator (admin)

### Requirements

Command privilege
		  level: 1 and 4

Allowed during
		  upgrade: No

Applies to: Cisco
			 Prime License Manager

## license management
	 unlock admin

This command
		  unlocks a Cisco Prime Licence Manager server defined user. The command will
		  prompt for the name of the user to unlock.

## Command Modes

Administrator (admin:)

### Requirements

Command privilege
		  level: 1 and 4

Allowed during
		  upgrade: No

Applies to: Cisco
			 Prime License Manager

| Privilege | Definition |
|---|---|
| Privilege level 0 | Specifies an ordinary privilege level. Users with ordinary
					 privileges can run CLI commands with privilege level 0 only. |
| Privilege level 1 | Specifies an advanced privilege level. Users with advanced
					 privileges can run CLI commands with privilege level 1 and below. |
| Privilege level 4 | The administrator account that the system creates when Cisco Unified Communications Manager installs has a privilege level of 4. The administrator can run all commands in
					 the CLI. |

| Parameters | Description |
|---|---|
| diagnose | Prints
					 diagnostic information of the selected file. |
| get | Creates a
					 TAR file of the license file(s) on the system and transfers the TAR file to a
					 remote area. |

| Parameters | Description |
|---|---|
| name | Specifies
					 the administrator username. |

| Parameters | Description |
|---|---|
| password | Specifies
					 the administrator password. |

| Parameters | Description |
|---|---|
| identity | Resets
					 the identity |
| registration | Resets
					 the registration |

| Parameters | Description |
|---|---|
| activate | Activates
					 a given service on the Cisco Prime License Manager server. |
| deactivate | Deactivates a given service on the Cisco Prime License Manager
					 server. |

| Parameters | Description |
|---|---|
| error | Provides
					 runtime errors or unexpected conditions that could be critical. |
| warning | Provides
					 messages about potential problems. |
| info | Provides
					 general information that may be useful. This parameter is set by default. |
| debug | Provides
					 detailed information about the flow of the process. We recommend that you use
					 set this parameter on an as needed basis only. |

| Parameters | Description |
|---|---|
| error | Provides
					 runtime errors or unexpected conditions that could be critical. |
| warning | Provides
					 messages about potential problems. |
| info | Provides
					 general information that may be useful. This parameter is set by default. |
| debug | Provides
					 detailed information about the flow of the process. We recommend that you use
					 set this parameter on an as needed basis only. |