---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-admin-gd-admin-book-c-cmds-html-0af14886ab
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/admin_gd/Admin_Book/c_cmds.html
retrieved_at: 2026-08-21T23:40:20.814119+00:00
---

Administration Guide for Cisco Unified SRST Manager

# Administration Guide for Cisco Unified SRST Manager

Updated: August 11, 2014

Chapter: C

## Chapter: C

- clear counters interfaces

- clear crashbuffer

- copy url

## C

Note For information about other CLI commands that are not listed in this document, see the Cisco Unity Express Command Reference for 3.0 and Later Versions.

clear counters interfaces

clear crashbuffer

copy url

## clear counters interfaces

To clear interface counters, use the clear counters interfaces command in EXEC mode.

clear counters interfaces

### Syntax Description

This command has no arguments or keywords.

### Command Default

None. Interface counters are not cleared.

## Command Modes

EXEC

### Command History

9.0

This command was introduced.

### Usage Guidelines

Use this command when you have interface counters you want to clear, for example, the general debug counters. This command clears all counters, including statistics counters.

### Examples

The following example illustrates the use of the clear counters interfaces command.

### Related Commands

clear crashbuffer

Clears the kernel crash buffer.

## clear crashbuffer

To clear the kernel crash buffer, use the clear crashbuffer command in EXEC mode.

clear crashbuffer

### Syntax Description

This command has no arguments or keywords.

### Command Default

None. Crash buffer is not cleared.

## Command Modes

EXEC

### Command History

9.0

This command was introduced.

### Usage Guidelines

Use this command to clear the kernel crash buffer after the reasons for a crash are fully investigated.

### Examples

The following example illustrates the use of the clear crashbuffer command.

### Related Commands

clear counters interfaces

Clears the interface counters.

## copy url

To add support for new phone types to Cisco Unified SRST Manager, use the copy url command in EXEC mode to upload the phonetype.jar file containing updated information for supported phone types.

copy url [ ftp_sitename ]/[ directory_path ]/[ file_name ] phone-config username [ username ] password [ password ]

no copy url

### Syntax Description

ftp_sitename

Name of the ftp site containing the JAR file.

directory_path

Path to the file on the ftp site.

file_name

Name of the JAR file on the ftp site.

username

User name of ftp site account.

password

Password for the ftp site account.

### Command Default

None.

## Command Modes

EXEC

### Command History

9.0

This command was introduced.

### Usage Guidelines

Use this command to upload phonetype.jar, a Java archive (JAR) file containing updated information for phone types supported by Cisco Unified SRST Manager. The updated JAR file can include new phone types to add to Cisco Unified SRST Manager.

JAR File Contents

The uploaded phonetype.jar file must contain the following files:

usr/bin/products/umg/CusmPhoneModels.xml

usr/ccp/classes/PhoneModels.xml

META-INF/MANIFEST.MF

### Examples

The following example illustrates the use of the copy url command.

| Version | Modification |
|---|---|
| 9.0 | This command was introduced. |

| Command | Description |
|---|---|
| clear crashbuffer | Clears the kernel crash buffer. |

| Version | Modification |
|---|---|
| 9.0 | This command was introduced. |

| Command | Description |
|---|---|
| clear counters interfaces | Clears the interface counters. |

| ftp_sitename | Name of the ftp site containing the JAR file. |
|---|---|
| directory_path | Path to the file on the ftp site. |
| file_name | Name of the JAR file on the ftp site. |
| username | User name of ftp site account. |
| password | Password for the ftp site account. |

| Version | Modification |
|---|---|
| 9.0 | This command was introduced. |