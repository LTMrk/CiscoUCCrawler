---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-command-reference-cme-cr-cme-cr-chapter-010110-html-bd7f352547
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/command/reference/cme_cr/cme_cr_chapter_010110.html
retrieved_at: 2026-08-21T22:57:30.184319+00:00
---

Cisco Unified Communications Manager Express Command Reference

# Cisco Unified Communications Manager Express Command Reference

Updated: July 19, 2018

Chapter: Cisco Unified CME Commands: X

## Chapter: Cisco Unified CME Commands: X

# Cisco Unified CME Commands: X

## xml-config

To define the
                              		  phone-specific XML tags that can be used in the configuration file, use the xml-config command in the voice register pooltype mode. To remove the XML tags, use the no form of
                              		  this command.

xml-config [ maxNumcalls maxNumCalls | busyTrigger busyTrigger | custom custom ]

no xml-config [ maxNumcalls maxNumCalls | busyTrigger busyTrigger | custom custom ]

### Syntax Description

maxNumcalls

Defines
                                          						the maximum number of calls allowed per line.

busyTrigger

Defines
                                          						the number of calls that triggers call forward busy per line on the SIP phone.

custom

Defines
                                          						the custom XML tags that can be appended at the end of the phone-specific CNF
                                          						configuration profile using the custom option.

### Command Default

The
                              		  phone-specific XML tags are not defined.

### Command Modes

Voice Register Pool Configuration (config-register-pool)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

15.3(3)M

Cisco
                                          						SIP CME 10.0

This
                                          						command was introduced.

### Usage Guidelines

Use this command
                              		  to define the phone specific XML tags that can be used in the configuration
                              		  file. the maximum nunber of call allowed per line and the number of call that
                              		  triggers call forward busy per line information will be used while generating
                              		  the XML file.

## Examples

The following
                              		  example shows how to define the phone specific XML tags that can be used in the
                              		  configuration file:

```
Router# configure terminal
Router(config)# voice register pool-type 9900
Router(config-register-pool-type)# xml-config maxNumCalls 3
Router(config-register-pool-type)# xml-config busyTrigger 3
Router(config-register-pool-type)# xml-config custom <custom-sftp>1</custom-sftp>
```

### Related Commands

Command

Description

voice register pool-type

Adds a
                                          						new Cisco Unified SIP IP phone to Cisco Unified CME.

phoneload-support

Enables support for phone loads.

## xmlschema

Effective with Cisco Unified CME 4.0, the xmlschema command was made obsolete.

For earlier releases, to specify the URL for a Cisco CME eXtensible
                              		  Markup Language (XML) application program interface (API) schema, use the xmlschema command in telephony-service
                              		  configuration mode. To set the URL for the XML API schema to the default, use
                              		  the no form of this command.

xmlschema schema-url

no xmlschema

### Syntax Description

schema-url

Local or remote URL as defined in RFC 2396.

### Command Default

Url for Cisco XML API schema is srst-its.xsd.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco CME 3.0

This command was introduced.

12.3(4)T

Cisco CME 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

12.4(4)XC

Cisco Unified CME 4.0

This command was made obsolete.

12.4(9)T

Cisco Unified CME 4.0

This command was made obsolete in Cisco IOS Release
                                          						12.4(9)T.

Cisco IOS XE Gibraltar 16.11.1a Release

Unified CME 12.6

The command is deprecated. It is not supported on Unified CME 12.6 and later releases.

## Examples

The following example specifies a URL for an XML API schema:

```
Router(config)# telephony-service Router(config-telephony)# xmlschema http://server2.example.com/schema/schema1.xsd
```

### Related Commands

Description

telephony-service

Enters telephony-service configuration mode.

## xmltest

Effective with Cisco Unified CME 4.0, the xmltest command was made obsolete.

For earlier releases, to specify that the HTTP payload in eXtensible
                              		  Markup Language (XML) application program interface (API) queries be
                              		  interpreted as having form format, use the xmltest command in telephony-service
                              		  configuration mode. To specify that the HTTP payload should be interpreted as
                              		  plain text (no form) format, use the no form of this command.

xmltest

no xmltest

### Syntax Description

This command has no arguments or keywords.

### Command Default

Default format is plain text (no form) format.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco CME 3.0

This command was introduced.

12.3(4)Ts

Cisco CME 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

12.4(4)XC

Cisco Unified CME 4.0

This command was made obsolete.

12.4(9)T

Cisco Unified CME 4.0

This command was made obsolete in Cisco IOS Release
                                          						12.4(9)T.

Cisco IOS XE Gibraltar 16.11.1a Release

Unified CME 12.6

The command is deprecated. It is not supported on Unified CME 12.6 and later releases.

## Examples

The following example specifies that the HTTP payload in XML API
                              		  queries be interpreted as having form format:

```
Router(config)# telephony-service Router(config-telephony)# xmltest
```

### Related Commands

Description

telephony-service

Enters telephony-service configuration mode.

## xmlthread

Effective with Cisco Unified CME 4.0, the xmlthread command was made obsolete.

For earlier releases, to set the maximum number of concurrent Cisco
                              		  CME eXtensible Markup Language (XML) application program interface (API)
                              		  queries, use the xmlthread command in telephony-service
                              		  configuration mode. To set the maximum number of queries to the default, use
                              		  the no form of this command.

xmlthread number

no xmlthread

### Syntax Description

number

Maximum number of XML API queries. Range is from 1 to 5.
                                          						Default is 2.

### Command Default

The maximum number of queries is 2.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco CME 3.0

This command was introduced.

12.3(4)T

Cisco CME 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

12.4(4)XC

Cisco Unified CME 4.0

This command was made obsolete.

12.4(9)T

Cisco Unified CME 4.0

This command was made obsolete in Cisco IOS Release
                                          						12.4(9)T.

Cisco IOS XE Gibraltar 16.11.1a Release

Unified CME 12.6

The command is deprecated. It is not supported on Unified CME 12.6 and later releases.

## Examples

The following example sets the maximum number of XML API queries to
                              		  5:

```
Router(config)# telephony-service Router(config-telephony)# xmlthread 5
```

### Related Commands

Description

telephony-service

Enters telephony-service configuration mode.

## xml user

To define a user who is authorized to use XML applications to execute
                              		  commands, use the xml user command in telephony-service configuration mode. To delete the
                              		  user, use the no form of this command.

xml user user-name password [0|6] password privilege-level

no xml user user-name password password privilege-level

### Syntax Description

user-name

Unique string used by authorized user to access Cisco
                                          						Unified CME. Maximum length of string: 19 alphanumeric characters.

password password

Alphanumeric string to be used with this user name to
                                          						provide access to Cisco Unified CME. Maximum length of string: 19 alphanumeric
                                          						characters.

privilege-level

Level of access to Cisco IOS commands to be granted to this
                                          						user. Only the commands with the same or a lower level can be executed via XML.
                                          						Range is 0 to 15.

### Command Default

User name is not defined.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)XC

Cisco Unified CME 4.0

This command was introduced.

12.4(9)T

Cisco Unified CME 4.0

This command was integrated into Cisco IOS Release
                                          						12.4(9)T.

Cisco IOS XE Gibraltar 16.11.1a Release

Unified CME 12.6

The command was enhanced for password encryption, based on Unified CME password policy.

### Usage Guidelines

This command creates a credential be used by an authorized user to
                              		  access Cisco Unified CME via XML and enable the user to execute all the Cisco
                              		  IOS commands associated with a particular privilege level.

To change the default privilege level for one or more Cisco IOS
                              		  commands, use the privilege command in global configuration
                              		  mode.

From Unified CME 12.6 onwards, you must configure password encryption using the parameters [0|6] . This in accordance with Unified CME Password Policy. The 0 in the parameter [0|6] mentioned in the CLI command represents
                              plain, unencrypted text and 6 represents level 6 password encryption.

## Examples

The following example defines user23 as an authorized user at level
                              		  15:

```
Router(config)# telephony-service Router(config-telephony)# xml user user23 password 3Rs92uzQ 15
```

### Related Commands

Command

Description

privilege

Configures a new privilege level for users and associates
                                          						commands with that privilege level.

| maxNumcalls | Defines
                                          						the maximum number of calls allowed per line. |
|---|---|
| busyTrigger | Defines
                                          						the number of calls that triggers call forward busy per line on the SIP phone. |
| custom | Defines
                                          						the custom XML tags that can be appended at the end of the phone-specific CNF
                                          						configuration profile using the custom option. |

| Note | When the
                                       		  reference-pooltype command is configured, the XML configuration value of the
                                       		  reference phone is inherited. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 15.3(3)M | Cisco
                                          						SIP CME 10.0 | This
                                          						command was introduced. |

| Command | Description |
|---|---|
| voice register pool-type | Adds a
                                          						new Cisco Unified SIP IP phone to Cisco Unified CME. |
| phoneload-support | Enables support for phone loads. |

| schema-url | Local or remote URL as defined in RFC 2396. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was made obsolete. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was made obsolete in Cisco IOS Release
                                          						12.4(9)T. |
| Cisco IOS XE Gibraltar 16.11.1a Release | Unified CME 12.6 | The command is deprecated. It is not supported on Unified CME 12.6 and later releases. |

|  | Description |
|---|---|
| telephony-service | Enters telephony-service configuration mode. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)Ts | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was made obsolete. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was made obsolete in Cisco IOS Release
                                          						12.4(9)T. |
| Cisco IOS XE Gibraltar 16.11.1a Release | Unified CME 12.6 | The command is deprecated. It is not supported on Unified CME 12.6 and later releases. |

|  | Description |
|---|---|
| telephony-service | Enters telephony-service configuration mode. |

| number | Maximum number of XML API queries. Range is from 1 to 5.
                                          						Default is 2. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was made obsolete. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was made obsolete in Cisco IOS Release
                                          						12.4(9)T. |
| Cisco IOS XE Gibraltar 16.11.1a Release | Unified CME 12.6 | The command is deprecated. It is not supported on Unified CME 12.6 and later releases. |

|  | Description |
|---|---|
| telephony-service | Enters telephony-service configuration mode. |

| user-name | Unique string used by authorized user to access Cisco
                                          						Unified CME. Maximum length of string: 19 alphanumeric characters. |
|---|---|
| password password | Alphanumeric string to be used with this user name to
                                          						provide access to Cisco Unified CME. Maximum length of string: 19 alphanumeric
                                          						characters. |
| privilege-level | Level of access to Cisco IOS commands to be granted to this
                                          						user. Only the commands with the same or a lower level can be executed via XML.
                                          						Range is 0 to 15. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |
| Cisco IOS XE Gibraltar 16.11.1a Release | Unified CME 12.6 | The command was enhanced for password encryption, based on Unified CME password policy. |

| Command | Description |
|---|---|
| privilege | Configures a new privilege level for users and associates
                                          						commands with that privilege level. |