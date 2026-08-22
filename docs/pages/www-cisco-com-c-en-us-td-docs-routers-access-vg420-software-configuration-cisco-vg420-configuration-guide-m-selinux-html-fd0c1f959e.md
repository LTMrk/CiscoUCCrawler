---
doc_id: www-cisco-com-c-en-us-td-docs-routers-access-vg420-software-configuration-cisco-vg420-configuration-guide-m-selinux-html-fd0c1f959e
source_url: https://www.cisco.com/c/en/us/td/docs/routers/access/vg420/software-configuration/cisco-vg420-configuration-guide/m_selinux.html
retrieved_at: 2026-08-22T01:17:56.831848+00:00
---

Cisco VG420 Voice Gateway Software Configuration Guide

# Cisco VG420 Voice Gateway Software Configuration Guide

Updated: August 27, 2024

Chapter: Support for Security-Enhanced Linux

## Chapter: Support for Security-Enhanced Linux

# Support for Security-Enhanced Linux

This chapter describes the SELinux feature, and includes the following sections:

## Overview

Security-Enhanced Linux (SELinux) is a solution composed of Linux kernel security module and system utilities to incorporate
                           a strong, flexible Mandatory Access Control (MAC) architecture into Cisco IOS-XE platforms.

SELinux provides an enhanced mechanism to enforce the separation of information, based on confidentiality and integrity requirements,
                           which addresses threats of tampering and bypassing of application security mechanisms and enables the confinement of damage
                           that malicious or flawed applications can cause.

## Prerequisites for SELinux

There are no specific prerequisites for this feature.

## Restrictions for SELinux

There are no specific restrictions for this feature.

## Information About SELinux

SELinux enforces mandatory access control policies that confine user programs and system services to the minimum privilege
                           required to perform their assigned functionality. This reduces or eliminates the ability of these programs and daemons to
                           cause harm when compromised (for example, through buffer overflows or misconfigurations). This is a practical implementation
                           of principle of least privilege by enforcing MAC on Cisco IOS-XE platforms. This confinement mechanism works independently
                           of the traditional Linux access control mechanisms. SELinux provides the capability to define policies to control the access
                           from an application process to any resource object, thereby allowing for the clear definition and confinement of process behavior.

SELinux can operate either in Permissive mode or Enforcing mode when enabled on a system.

In Permissive mode, SELinux does not enforce the policy, and only generates system logs for any denials caused by violation
                                 of the resource access policy. The operation is not denied, but only logged for resource access policy violation.

In Enforcing mode, the SELinux policy is enabled and enforced. It denies resource access based on the access policy rules,
                                 and generates system logs.

SELinux is enabled in Enforcing mode by default on supported Cisco IOS XE platforms. In the Enforcing mode, any system resource
                           access that does not have the necessary allow policy is treated as a violation, and the operation is denied. The violating
                           operation fails when a denial occurs, and system logs are generated. In Enforcing mode, the solution works in access-violation
                           prevention mode.

## Configuring SELinux

The are no additional requirements or configuration steps needed to enable or use the SELinux feature in Enforcing mode.

The following commands are introduced as part of the SELinux feature:

```
set platform software selinux {default | enforcing | permissive}
```

```
platform security selinux {enforcing | permissive}
```

```
show platform software selinux
```

These new commands are implemented as service internal commands.

### Configuring SELinux (EXEC Mode)

Use the set platform software selinux command to configure SELinux in EXEC mode.

The following example shows SELinux configuration in EXEC mode:

```
Device# set platform software selinux ? default 	Set SELinux mode to default
enforcing 	Set SELinux mode to enforcing
permissive 	Set SELinux mode to permissive
```

### Configuring SELinux (CONFIG Mode)

Use the platform security selinux command to configure SELinux in configuration mode.

The following example shows SELinux configuration in CONFIG mode:

```
Device(config)# platform security selinux enforcing 	Set SELinux policy to Enforcing mode
permissive 	Set SELinux policy to Permissive mode

Device(config)# platform security selinux permissive Device(config)#
*Oct 20 21:52:45.155: %IOSXE-1-PLATFORM: R0/0:
SELINUX_MODE_PROG: Platform Selinux confinement mode downgraded to permissive!

Device(config)#
```

### Examples for SELinux

The following example shows the output for changing the mode from Enforcing to Permissive:

```
“*Oct 20 21:44:03.609: %IOSXE-1-PLATFORM: R0/0:
SELINUX_MODE_PROG: Platform Selinux confinement mode downgraded to permissive!”
```

The following example shows the output for changing the mode from Permissive to Enforcing:

```
“*Oct 20 21:44:34.160: %IOSXE-1-PLATFORM: R0/0:
SELINUX_MODE_PROG: Platform Selinux confinement mode upgraded to enforcing!”
```

If the SELinux mode is changed, this change is considered a system security event, and a system log message is generated.

### SysLog Message Reference

Facility-Severity-Mnemonic

%SELINUX-1-VIOLATION

Severity-Meaning

Alert Level Log

Message

N/A

Message Explanation

Resource access was made by the process for which a resource access policy does not exist. The operation was flagged, and
                                             resource access was denied. A system log was generated with information that process resource access has been denied.

Component

SELINUX

Recommended Action

Contact Cisco TAC with the following relevant information as attachments:

The exact message as it appears on the console or in the system

Output of the show tech-support command (text file)

Archive of Btrace files from the box using the following command:

request platform software trace archive target <URL>

Output of the show platform software selinux command

The following examples demonstrate sample syslog messages:

Example 1:

```
*Nov 14 00:09:04.943: %SELINUX-1-VIOLATION: R0/0: audispd: type=AVC 
msg=audit(1699927057.934:129): avc: denied { getattr } for pid=5899 comm="ls" 
path="/root/test" dev="rootfs" ino=25839 
scontext=system_u:system_r:polaris_iosd_t:s0 
tcontext=system_u:object_r:admin_home_t:s0 tclass=file permissive=0
```

Example 2:

```
*Nov 14 00:09:04.947: %SELINUX-1-VIOLATION: R0/0: audispd: t type=AVC 
msg=audit(1699927198.486:130): avc: denied { write } for pid=6012 comm="echo" 
path="/root/test" dev="rootfs" ino=25839 
scontext=system_u:system_r:polaris_iosd_t:s0 
tcontext=system_u:object_r:admin_home_t:s0 tclass=file permissive= 0
```

## Verifying SELinux Enablement

Use the show platform software selinux command to view the SELinux configuration mode:

```
Device# show platform software selinux
=========================================
IOS-XE SELINUX STATUS
=========================================
SElinux Status :   	Enabled
Current Mode :     	Enforcing
Config file Mode : 	Enforcing
```

## Troubleshooting SELinux

If there is an instance of an SELinux violation on your device or network, please reach out to Cisco TAC with the following
                           details:

The message exactly as it appears on the console or in the system log. For example:

```
device#request platform software trace archive target
    flash:selinux_btrace_logs
```

Output of the show tech-support command (text file)

Archive of Btrace files from the box using the following command:

request platform software trace archive target <URL>

Output of the show platform software selinux command

| Note | These new commands are implemented as service internal commands. |
|---|---|

| Note | If the SELinux mode is changed, this change is considered a system security event, and a system log message is generated. |
|---|---|

| Facility-Severity-Mnemonic | %SELINUX-1-VIOLATION |
|---|---|
| Severity-Meaning | Alert Level Log |
| Message | N/A |
| Message Explanation | Resource access was made by the process for which a resource access policy does not exist. The operation was flagged, and
                                             resource access was denied. A system log was generated with information that process resource access has been denied. |
| Component | SELINUX |
| Recommended Action | Contact Cisco TAC with the following relevant information as attachments: The exact message as it appears on the console or in the system Output of the show tech-support command (text file) Archive of Btrace files from the box using the following command: request platform software trace archive target <URL> Output of the show platform software selinux command |