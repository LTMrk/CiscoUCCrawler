---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-cli-ref-12-5-1su2-cucm-b-command-line-interface-reference-guide-1251su2-d16a9cba26
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/cli_ref/12_5_1SU2/cucm_b_command-line-interface-reference-guide-1251Su2/cucm_b_command-line-interface-reference-guide-1251Su2_chapter_010.html
retrieved_at: 2026-08-16T23:59:45.766052+00:00
---

Command Line Interface Reference Guide for Cisco Unified Communications Solutions, Release 12.5(1)SU2

# Command Line Interface Reference Guide for Cisco Unified Communications Solutions, Release 12.5(1)SU2

Updated: October 3, 2023

Chapter: Delete Commands

## Chapter: Delete Commands

# Delete Commands

## delete
                        	 account

This command allows
                              		  you to delete an administrator account.

delete account account-name

## Syntax Description

Specifies
                                       					 the name of an administrator account.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during
                              		  upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## delete cuc futuredelivery

This command deletes all messages that have been marked for future delivery.

delete cuc futuredelivery

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Cisco Unity Connection

### Example

The following example deletes two messages that have been marked for future delivery.

```
admin: delete cuc futuredelivery

Deleting File : UmssMtaFutureDelivery/UnityMbxDb1/5C56C086-E64B-11DC-9BAF-41FC55D89593.eml

Deleting File : UmssMtaFutureDelivery/UnityMbxDb1/6D7DD796-E64B-11DC-A0E6-D1FD55D89593.eml

Files : Found = 2, Deleted = 2

Note: Files that are in use cannot be deleted
```

## delete cuc
                        	 locale

This command
                              		  deletes the specified locale and all of the associated files and settings from
                              		  Connection.

delete cuc locale locale-id

## Syntax Description

Specifies
                                       					 the ID of the locale that you want to delete.

### Command Modes

Administrator (admin:)

### Usage Guidelines

Before you run this command, you must stop the Connection Conversation Manager and Connection Mixer services. After you run
                              this command, you must restart the Connection Conversation Manager and Connection Mixer services. While running "delete cuc"
                              locale command, you can choose to retain or not retain the locale mappings at your Unity Connection System. If you choose to retain locale mapping, then after re-install of same locale, all objects like Subscribers and Call handlers  are
                              automatically mapped to retained locale. If you choose not to retain the locale mapping, then after uninstall all locale mappings
                              are lost.

### Requirements

Command privilege
                              		  level: 1

Allowed during
                              		  upgrade: Yes

Applies to: Cisco Unity
                                 			 Connection

### Example

The following
                              		  example deletes the en-GB locale and all of the associated files and settings.

```
admin:delete cuc locale en-GB

en-GB uninstalled
```

## delete dns

This command allows you to delete the IP address for a DNS server.

delete dns addr

## Syntax Description

Represents the IP address of the DNS server that you want to delete.

### Command Modes

Administrator (admin:)

### Usage Guidelines

After you execute this command, the system asks whether you want to continue.

Caution

If you continue, this command causes a temporary loss of network connectivity.

### Requirements

Command privilege level: 1

Allowed during upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## delete dscp

This command
                              		  deletes a DSCP port tag.

delete dscp port-tag

## Syntax Description

Represents
                                       					 a DSCP port tag, which is a string that is mapped to a TCP or UDP port to
                                       					 identify the application that uses the port. This value is for the portTag
                                       					 field displayed when you use the command show dscp
                                             						  defaults . The set of port tags is predefined.

### Command Modes

Administrator (admin:)

### Usage Guidelines

After you delete an enabled port tag, DSCP marking on that port tag stops. You can recreate a deleted port tag when you use
                              the set dscp marking command; enter the name of the port tag that you previously deleted.

Tip

### Requirements

Command privilege level: 1

Applies to: Unified
                                 			 Communications Manager , Cisco Unity
                                 			 Connection

## delete ipsec policy_group

This command deletes all policies within the specified group or all groups.

delete ipsec policy_group { group | | all }

## Syntax Description

Represents a specific group name.

Deletes all groups.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: No

Applies to: Unified Communications Manager , Cisco Unity Connection

## delete ipsec policy_name

This command deletes an IPSec policy with given policy name.

delete ipsec policy_name { policy_group | | policy_name }

## Syntax Description

Represents the policy group.

Represents the policy name.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: No

Applies to: Unified Communications Manager , Cisco Unity Connection

## delete process

This command allows you to delete a particular process.

delete process process-id [ force | terminate | crash ]

## Syntax Description

Represents the process ID number.

Causes the process to stop.

Causes the operating system to terminate the process.

Crashes the process and produces a crash dump.

### Command Modes

Administrator (admin:)

### Usage Guidelines

Use the force option only if the command alone does not delete the process; use the terminate option only if force does not delete the process.

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## delete smtp

This command allows you to delete the SMTP host.

delete smtp

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

| Parameters | Description |
|---|---|
| account-name | Specifies
                                       					 the name of an administrator account. |

| Parameters | Description |
|---|---|
| locale-id | Specifies
                                       					 the ID of the locale that you want to delete. |

| Parameters | Description |
|---|---|
| addr | Represents the IP address of the DNS server that you want to delete. |

| Caution | If you continue, this command causes a temporary loss of network connectivity. |
|---|---|

| Parameters | Description |
|---|---|
| port-tag | Represents
                                       					 a DSCP port tag, which is a string that is mapped to a TCP or UDP port to
                                       					 identify the application that uses the port. This value is for the portTag
                                       					 field displayed when you use the command show dscp
                                             						  defaults . The set of port tags is predefined. |

| Tip | Use
                                          			 the command show dscp
                                                				  defaults to list the configured port tags. |
|---|---|

| Parameters | Description |
|---|---|
| group | Represents a specific group name. |
| all | Deletes all groups. |

| Parameters | Description |
|---|---|
| policy_group | Represents the policy group. |
| policy_name | Represents the policy name. |

| Parameters | Description |
|---|---|
| process-id | Represents the process ID number. |
| force | Causes the process to stop. |
| terminate | Causes the operating system to terminate the process. |
| crash | Crashes the process and produces a crash dump. |