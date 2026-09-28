---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-cli-ref-12-5-1su5-cucm-b-cli-reference-guide-release1251su5-cucm-b-cli--f702f01821
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/cli_ref/12_5_1SU5/cucm_b_cli_reference-guide_release1251SU5/cucm_b_cli_reference_guide_release_1401_chapter_01000.html
retrieved_at: 2026-08-16T23:57:46.427430+00:00
---

Command Line Interface Reference Guide for Cisco Unified Communications Solutions, Release 12.5(1)SU5

# Command Line Interface Reference Guide for Cisco Unified Communications Solutions, Release 12.5(1)SU5

Updated: October 3, 2023

Chapter: Unset Commands

## Chapter: Unset Commands

# Unset Commands

## unset ipsec policy_group

This command disables the ipsec policy on the specified group.

unset ipsec policy_group policy_group

## Syntax Description

Specifies the group name.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade:  No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## unset ipsec policy_name

This command disables the ipsec policy with the specified name.

unset ipsec policy_name policy_group policy_name

## Syntax Description

Specifies the name of a particular ipsec policy group to disable.

Specifies the policy name to disable.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: No

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## unset  network cluster subscriber details

This command shows  the message that you need to delete a subscriber node from the GUI instead of the command prompt.

unset network cluster subscriber details

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: No

Applies to Unified Communications Manager, IM and Presence Service on Communications Manager, and Cisco Unity Connection

### Message to delete the subscriber from GUI

```
admin: unset network cluster subscriber details  
Please use the Cisco Unified Communications Manager on the first node.
Navigate to System > Server and click “Find”.
			Unable to del: NULL
Executed command unsuccessfully.
```

## unset network cluster subscriber dynamic-cluster-configuration

This command disables Dynamic Cluster Configuration on the publisher. The value of Dynamic Cluster Configuration option is set to zero on publisher.

unset network cluster subscriber dynamic-cluster-configuration

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: No

Applies to Unified Communications Manager, IM and Presence Service on Unified Communications Manager, and Cisco Unity Connection

## unset network dns options

This command unsets DNS options.

unset network dns options [ timeout ] [ attempts ] [ rotate ]

## Syntax Description

Sets the wait time before the system considers a DNS query as failed to the default.

Sets the number of DNS attempts to make before the system fails to the default.

Sets the method for selecting a nameserver to the default. This affects how loads are distributed across nameservers.

### Usage Guidelines

Running this command causes an automatic system restart.

### Command Modes

Administrator (admin:)

### Usage Guidelines

You are asked to confirm that you want to execute this command.

Caution

### Requirements

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

## unset network domain

This command unsets the domain name and restarts the server.

unset network domain

### Command Modes

Administrator (admin:)

### Usage Guidelines

You are asked to confirm that you want to execute this command.

### Requirements

Applies to: Unified Communications Manager , IM and Presence Service on Unified Communications Manager , Cisco Unity Connection

### Example

```
admin: unset network domain
```

```
cmdSetIp.domain.name.change.warning
```

```
Continue (y/n)?
```

```
trying to restart system...
```

```
Warning: Restart could take up to 5 minutes...
```

```
Shutting down Service Manager. Please wait...
```

## unset network ntp
                        	 options

This command
                              		  unsets the domain name and restarts the server.

unset network ntp options

### Command Modes

Administrator (admin:)

### Requirements

Command privilege
                              		  level: 1

Allowed during
                              		  upgrade: Yes

Applies to: Unified Communications Manager, IM and Presence Service on Unified Communications Manager, Cisco Unity Connection

## unset network ipv6
                        	 gateway

This command unsets the IPv6 gateway on the server.

unset network ipv6 gateway [ reboot ]

## Syntax Description

Reboots the server after applying the change.

By default, the reboot on the server does not happen.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade: Yes

Applies to: Unified Communications Manager, IM and Presence Service on Unified Communications Manager, Cisco Unity Connection

## unset network ipv6 static_address

This command unsets the IPV6 static address.

unset network ipv6 static_address [ reboot ]

## Syntax Description

Reboots the server after applying the change.

### Command Modes

Administrator (admin:)

### Requirements

Command privilege level: 1

Allowed during upgrade:  No

Applies to: Unified Communications Manager , Cisco Unity Connection

### Example

```
admin: admin:unset network ipv6 static_address
```

```
W A R N I N G
```

```
The Server must be rebooted for these changes to take effect.
```

```
Please make sure that you reboot this server.
```

```
IPv6 static address was removed.
```

| Parameters | Description |
|---|---|
| policy_group | Specifies the group name. |

| Parameters | Description |
|---|---|
| policy_group | Specifies the name of a particular ipsec policy group to disable. |
| policy_name | Specifies the policy name to disable. |

| Parameters | Description |
|---|---|
| timeout | Sets the wait time before the system considers a DNS query as failed to the default. |
| attempts | Sets the number of DNS attempts to make before the system fails to the default. |
| rotate | Sets the method for selecting a nameserver to the default. This affects how loads are distributed across nameservers. |

| Caution | If you continue, the system loses network connectivity temporarily. |
|---|---|

| Parameters | Description |
|---|---|
| reboot | Reboots the server after applying the change. Note By default, the reboot on the server does not happen. | Note | By default, the reboot on the server does not happen. |
| Note | By default, the reboot on the server does not happen. |

| Note | By default, the reboot on the server does not happen. |
|---|---|

| Parameters | Description |
|---|---|
| reboot | Reboots the server after applying the change. |