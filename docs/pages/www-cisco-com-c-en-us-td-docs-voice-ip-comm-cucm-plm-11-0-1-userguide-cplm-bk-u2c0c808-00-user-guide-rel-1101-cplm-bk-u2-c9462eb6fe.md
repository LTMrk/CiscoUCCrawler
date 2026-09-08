---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-plm-11-0-1-userguide-cplm-bk-u2c0c808-00-user-guide-rel-1101-cplm-bk-u2-c9462eb6fe
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/plm/11_0_1/userguide/CPLM_BK_U2C0C808_00_user-guide-rel-1101/CPLM_BK_U2C0C808_00_user-guide-rel-1101_appendix_0110.html
retrieved_at: 2026-09-08T05:01:06.175879+00:00
---

Cisco Prime License Manager User Guide, Release 11.0(1)

# Cisco Prime License Manager User Guide, Release 11.0(1)

Updated: September 12, 2017

Chapter: Cisco Prime License Manager CLI Commands

## Chapter: Cisco Prime License Manager CLI Commands

# Cisco Prime License Manager CLI Commands

## Introduction

The commands in
		  this section are specific to Cisco Prime License Manager. For platform-specific
		  commands, see the Command Line Interface Guide
			 for Cisco Unified Communications Solutions .

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

Command privilege level: 1

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

Command privilege level: 1

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

Command privilege level: 1

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

Command privilege level: 1

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

Command privilege level: 1

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

Command privilege level: 1

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

Command privilege level: 1

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

Command privilege level: 1

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

Command privilege level: 1

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

Command privilege level: 1

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

Command privilege level: 0

Allowed during
		  upgrade: No

Applies to: Cisco
		  Prime License Manager

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