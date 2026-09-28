---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-command-reference-cme-cr-cme-cr-chapter-01010-html-23153c3e01
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/command/reference/cme_cr/cme_cr_chapter_01010.html
retrieved_at: 2026-08-21T22:56:26.262616+00:00
---

Cisco Unified Communications Manager Express Command Reference

# Cisco Unified Communications Manager Express Command Reference

Updated: July 19, 2018

Chapter: Cisco Unified CME Commands: L

## Chapter: Cisco Unified CME Commands: L

# Cisco Unified CME Commands: L

## label

To create a text identifier instead of a phone-number display for an
                              		  extension on an IP phone console, use the label command in ephone-dn configuration mode. To delete a label, use the no form of this command.

label string

no label string

### Syntax Description

string

Alphanumeric string of up to 30 characters.

### Command Default

No label is defined.

### Command Modes

Ephone-dn configuration (config-ephone)

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

### Usage Guidelines

One label is allowed per extension (ephone-dn). The ephone-dn must
                              		  already have a number that was set using the number command before a label can be created
                              		  for it.

This command must be followed by a quick reboot of the phone on which
                              		  the label appears, using the restart command.

## Examples

The following example creates three phone labels to appear in place
                              		  of three phone numbers on IP phone console displays:

```
Router(config)# ephone-dn 10 Router(config-ephone-dn)# label user10 Router(config-ephone-dn)# exit Router(config)# ephone-dn 20 Router(config-ephone-dn)# label user20 Router(config-ephone-dn)# exit Router(config)# ephone-dn 30 Router(config-ephone-dn)# label user30 Router(config-ephone-dn)# exit
```

### Related Commands

Command

Description

number

Associates a telephone or extension number with an
                                          						ephone-dn in a Cisco CME system.

restart (ephone)

Performs a fast reboot of a single phone associated with a
                                          						Cisco CME router.

restart (telephony-service)

Performs a fast reboot of one or all phones associated with
                                          						a Cisco CME router.

## label (voice register dn)

To create a text identifier instead of a phone-number display for an
                              		  extension on a SIP phone console, use the label command in voice register dn configuration mode. To delete a label, use
                              		  the no form of this command.

label string

no label string

### Syntax Description

string

Alphanumeric string of up to 30 characters.

### Command Default

No label is created.

### Command Modes

Voice register dn configuration (config-register-dn)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4

This command was introduced.

### Usage Guidelines

One label is allowed per extension (directory number). The directory
                              		  number must already have a number that was set by using the number command before a label can be created
                              		  for it.

After you configure this command, restart the phone by using the reset command.

## Examples

The following example shows how to create three phone labels to
                              		  appear in place of three phone numbers on Cisco IP phone console displays:

```
Router(config)# voice register dn 10 Router(config-register-dn)# label user10 Router(config-register-dn)# exit Router(config)# voice register dn 20 Router(config-register-dn)# label user20 Router(config-register-dn)# exit Router(config)# voice register dn 30 Router(config-register-dn)# label user30 Router(config-register-dn)# exit
```

### Related Commands

Command

Description

number (voice register dn)

Associates a telephone or extension number with a directory
                                          						number in a Cisco CME system.

reset (voice register pool)

Performs a compete reboot of a single SIP phone associated
                                          						with a Cisco CME router.

reset (voice register global)

Performs a complete reboot of all SIP phones associated
                                          						with a Cisco CME router.

## list (ephone-hunt)

To create a list of extensions that are members of a Cisco Unified
                              		  CME ephone hunt group, use the list command in ephone-hunt configuration
                              		  mode. To remove a list from the router configuration, use the no form of this command.

list number [, number ...]

no list

### Syntax Description

number

Preconfigured extension or E.164 number.

An asterisk (*) can take the place of an extension number
                                          						to represent a wildcard slot. An agent at an authorized ephone-dn can
                                          						dynamically join and leave a hunt group if a wildcard slot is available. There
                                          						can be up to 20 wildcard slots in a hunt group.

### Command Default

No list is defined.

### Command Modes

Ephone-hunt configuration (config-ephone)

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

12.3(11)XL

Cisco CME 3.2.1

The number of ephone-dns allowed was increased to 20.

12.3(14)T

Cisco CME 3.3

This command was integrated into Cisco IOS Release
                                          						12.3(14)T.

12.4(4)XC

Cisco Unified CME 4.0

The use of wildcard asterisks (*) in the dn-number argument was introduced.

12.4(9)T

Cisco Unified CME 4.0

The use of wildcard asterisks (*) in the dn-number argument was integrated into Cisco IOS
                                          						Release 12.4(9)T.

### Usage Guidelines

Use this command to create a list of member numbers for defining a
                              		  hunt group.

List must contain 1 to 20 numbers.

A number cannot be added to a list unless it was already defined by
                              		  using the number command.

Add or delete all numbers in a hunt group list at one time. You
                              		  cannot add or single number to an existing list or remove one number from a
                              		  list.

Any number in the list cannot be a pilot number of a parallel hunt
                              		  group.

To allow dynamic membership in a hunt group, use asterisks to
                              		  represent wildcard slots in the list command. To allow an ephone-dn to use
                              		  one of the wildcard slots to dynamically join a hunt group, use the ephone-hunt login command under that ephone-dn. Ephone-dns are
                              		  disallowed from joining hunt groups by default, so you have to explicitly allow
                              		  this behavior for each ephone-dn that you want to be able to log into hunt
                              		  groups.

The show ephone-hunt command displays the numbers
                              		  associated to ephone-dns that are joined to groups at the time that the command
                              		  is run, in addition to static members of the hunt group. Static hunt group
                              		  members are the numbers that are explicitly named in the list command.

## Examples

The following example creates sequential hunt group number 7, which
                              		  contains four static members (ephone-dns):

```
Router(config)# ephone-hunt 7 sequential Router(config-ephone-hunt)# list 7711, 7712, 7713, 7714
```

The following example creates five ephone-dns and a hunt group that
                              		  includes the first two ephone-dns as static members and two wildcard slots for
                              		  dynamic hunt group members. The last three ephone-dns are enabled for dynamic
                              		  membership in the hunt group. Any of them can join the hunt group whenever one
                              		  of the wildcard slots is available. Once an ephone-dn has joined a hunt group,
                              		  it can leave at any time.

```
ephone-dn 22
 number 4566
ephone-dn 23
 number 4567
ephone-dn 24
 number 4568
 ephone-hunt login
ephone-dn 25
 number 4569
 ephone-hunt login
ephone-dn 26
 number 4570
 ephone-hunt login
ephone-hunt 1 peer
 list 4566,4567,*,*
 final 7777
```

### Related Commands

Command

Description

ephone-hunt login

Allows an ephone-dn to dynamically join and leave an ephone
                                          						hunt group.

final

Defines the last ephone-dn in an ephone hunt group.

hops

Defines the number of times that a call is redirected to
                                          						the next ephone-dn in a peer ephone-hunt-group list before proceeding to the
                                          						final ephone-dn.

max-redirect

Changes the current number of allowable redirects in a
                                          						Cisco CME system.

no-reg (ephone-hunt)

Specifies that the pilot number of this ephone hunt group
                                          						should not register with the H.323 gatekeeper.

number (ephone-dn)

Associates an extension or telephone number with a
                                          						directory number.

pilot

Defines the ephone-dn that is dialed to reach an ephone
                                          						hunt group.

preference (ephone-hunt)

Sets preference order for the ephone-dn associated with an
                                          						ephone-hunt-group pilot number.

show ephone-hunt

Displays ephone-hunt group configuration, current status,
                                          						and statistics.

timeout (ephone-hunt)

Sets the number of seconds after which a call that is not
                                          						answered is redirected to the next number in the hunt-group list.

## list (voice
                        	 hunt-group)

To define a list
                              		  of extensions that are members of a voice hunt-group, use the list command
                              		  in voice hunt-group configuration mode. To remove a list, use the no form of
                              		  this command.

list number, number [, number ...]

no list

### Syntax Description

number

Extension or E.164 number assigned to a phone in Cisco Unified CME. List must
                                          						contain 2 to 32 numbers.

### Command Default

By default, hunt
                              		  group list is not defined.

### Command Modes

Voice hunt-group configuration (config-voice-hunt-group)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.4(4)T

Cisco
                                          						CME 3.4

This
                                          						command was introduced.

12.4(15)XZ

Cisco
                                          						Unified CME 4.3

The
                                          						maximum numbers allowed in a list was expanded from 10 to 32 and support for
                                          						SCCP phones was added.

12.4(20)T

Cisco
                                          						Unified CME 7.0

This
                                          						command was integrated into Cisco IOS Release 12.4(20)T.

15.4(3)M

Cisco Unified CME 10.5

This command was modified to include support for wildcards
                                          						which is indicated by " * " . symbol.

### Usage Guidelines

This command
                              		  creates the list of numbers to include in a voice hunt-group. Phones with these
                              		  numbers ring when the hunt group pilot number is dialed. The numbers must be
                              		  assigned to directory numbers with the number command.

All numbers in a
                              		  hunt group list are added or deleted at one time. You cannot add a number to an
                              		  existing list or remove a number from a list.

The pilot number
                              		  of a parallel hunt group and shared-line numbers are not supported.

A phone number
                              		  associated with an FXO port is not supported in parallel hunt groups.

## Examples

The following
                              		  example shows how to create a sequential hunt group containing four extensions
                              		  and a wildcard slot:

```
Router(config)# voice hunt-group 1 sequential Router(config-voice-hunt-group)# list 7711, 7712, 7713, 7714, *
```

### Related Commands

Command

Description

final (voice hunt-group)

Defines
                                          						the last extension in a voice hunt group.

hops (voice hunt-group)

Defines
                                          						the number of times that a call is redirected to the next phone number in a
                                          						peer hunt-group list before proceeding to the final number.

number (ephone-dn)

Associates an extension or telephone number with a directory number.

number (voice register dn)

Associates an extension or telephone number with a directory number.

pilot (voice hunt-group)

Defines the phone number that callers dial to reach a voice hunt group.

timeout (voice hunt-group)

Sets
                                          						the number of seconds after which a call that is not answered is redirected to
                                          						the next number in the hunt-group list and defines the last number in the hunt
                                          						group.

## live-record

To define the extension number that is dialed when the LiveRcd soft
                              		  key is pressed on a Cisco Unified IP Phone, use the live-record command in telephony-service
                              		  configuration mode. To reset to the default value, use the no form of this command.

live-record phone-number

no live-record

### Syntax Description

phone-number

Telephone number that is dialed when the LiveRcd soft key
                                          						is pressed.

### Command Default

Live record is disabled.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)XZ

Cisco Unified CME 4.3

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

This command specifies the telephone number that is speed-dialed to
                              		  access the Live Record feature when the LiveRcd soft key on a Cisco Unified IP
                              		  phone is pressed. This telephone number is used for all Cisco Unified IP phones
                              		  connected to the router.

This telephone number must match the Live Record number configured in
                              		  Cisco Unity Express.

## Examples

The following example shows that the phone number 914085550100 is
                              		  speed-dialed to record a call when the LiveRcd button is pressed:

```
Router(config)# telephony-service Router(config-telephony)# live-record 914085550100
```

### Related Commands

Command

Description

ephone-template (ephone)

Applies an ephone template to an ephone.

softkeys connected

Modifies the order and type of soft keys that display on an
                                          						IP phone during the connected call state.

voicemail

Defines the telephone number that is speed-dialed when the
                                          						Messages button is pressed on an IP phone.

## load (telephony-service)

To associate a type of Cisco Unified IP phone with a phone firmware
                              		  file, use the load command in telephony-service
                              		  configuration mode. To disassociate a type of phone from a phone firmware file,
                              		  use the no form of this command.

load phone-type firmware-file

no load phone-type

### Syntax Description

phone-type

Type of phone. The following phone types are predefined in
                                          						the system:

- 6945 —Cisco Unified IP Phone
                                             						  6945.

- 7902 —Cisco Unified IP Phone
                                             						  7902G.

- 7905 —Cisco Unified IP Phone
                                             						  7905G.

- 7910 —Cisco Unified IP Phone
                                             						  7910 and 7910G.

- 7911 —Cisco Unified IP Phone
                                             						  7911G.

- 7912 —Cisco Unified IP Phone
                                             						  7912G.

- 7914 —Cisco Unified IP Phone
                                             						  7914 Expansion Module.

- 7920 —Cisco Unified Wireless IP
                                             						  Phone 7920.

- 7921 —Cisco Unified Wireless IP
                                             						  Phone 7921.

- 7931 —Cisco Unified IP Phone
                                             						  7931G.

- 7935 —Cisco Unified IP
                                             						  Conference Station 7935.

- 7936 —Cisco Unified IP
                                             						  Conference Station 7936.

- 7941 —Cisco Unified IP Phone
                                             						  7941G.

- 7941GE —Cisco Unified IP Phone
                                             						  7941G-GE.

- 7942 —Cisco Unified IP Phone
                                             						  7942.

- 7945 —Cisco Unified IP Phone
                                             						  7945

- 7960-7940 —Cisco Unified IP
                                             						  Phones 7960 and 7960G and Cisco Unified IP Phone 7940 and 7940G.

- 7961 —Cisco Unified IP Phone
                                             						  7961G.

- 7961GE —Cisco Unified IP Phone
                                             						  7961G-GE.

- 7962 —Cisco Unified IP Phone
                                             						  7962.

- 7965 —Cisco Unified IP Phone
                                             						  7965.

- 7970 —Cisco Unified IP Phone
                                             						  7970G.

- 7971 —Cisco Unified IP Phone
                                             						  7971G-GE.

- 7975 —Cisco Unified IP Phone
                                             						  7975.

- 7985 —Cisco Unified IP Phone
                                             						  7985.

- 8941 —Cisco Unified IP Phone
                                             						  8941.

- 8945 —Cisco Unified IP Phone
                                             						  8945.

- ata —Cisco ATA-186 and Cisco
                                             						  ATA-188.

firmware-file

Filename of the IP phone firmware for a particular phone
                                          						type.

- In Cisco Unified CME 7.0/4.3 and earlier versions, do
                                             						  not use the file suffix (.bin, .sbin, .loads) for any phone type except the
                                             						  Cisco ATA and Cisco Unified IP Phone 7905 and 7912.

- In Cisco Unified CME 7.0(1) and later versions, you must
                                             						  use the complete filename, including the file suffix, for phone firmware
                                             						  versions later than version 8-2-2 for all phone types.

- Filenames are case sensitive.

### Command Default

Firmware files are not associated with phone types.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.1(5)YD

Cisco ITS 1.0

This command was introduced.

12.2(8)T

Cisco ITS 2.0

This command was integrated into Cisco IOS Release
                                          						12.2(8)T.

12.2(11)YT

Cisco ITS 2.1

Support was added for the Cisco IP Phone 7914 Expansion
                                          						Module.

12.2(15)T

Cisco ITS 2.1

This command was integrated into Cisco IOS Release
                                          						12.2(15)T.

12.2(15)ZJ

Cisco CME 3.0

The following keywords were added to this command: 7902 , 7905 , and 7912 .

12.3(4)T

Cisco CME 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

12.3(7)T

Cisco CME 3.1

The 7920 and 7936 keywords were added.

12.3(11)XL

Cisco CME 3.2.1

The 7970 keyword was added.

12.3(14)T

Cisco CME 3.3

The 7971 keyword was added, and this
                                          						command was integrated into Cisco IOS Release 12.3(14)T.

12.4(4)XC

Cisco Unified CME 4.0

The 7911 , 7941 , 7941GE , 7961 , and 7961GE keywords were added.

12.4(9)T

Cisco Unified CME 4.0

This command was integrated into Cisco IOS Release
                                          						12.4(9)T.

12.4(6)XE

Cisco Unified CME 4.0(2)

The 7931 keyword was added.

12.4(4)XC4

Cisco Unified CME 4.0(3)

The 7931 keyword was added.

12.4(11)T

Cisco Unified CME 4.0(3)

This command was integrated into Cisco IOS Release
                                          						12.4(11)T.

12.4(11)XJ2

Cisco Unified CME 4.1

The 7921 and 7985 keywords were introduced.

12.4(15)T

Cisco Unified CME 4.1

This command was integrated into Cisco IOS Release
                                          						12.4(15)T.

12.4(15)T1

Cisco Unified CME 4.1(1)

The 7942 , 7945 , 7962 , 7965 , and 7975 keywords were introduced.

12.4(15)XZ

Cisco Unified CME 4.3

Support for user-defined phone types created with the ephone-type command was added.

12.4(20)T

Cisco Unified CME 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

12.4(20)YA

Cisco Unified CME 7.0(1)

Support for automatically creating bindings for firmware
                                          						files only if the cnf-file location is flash or slot0 was added.

12.4(20)T1

Cisco Unified CME 7.0

The 7925 keyword was introduced.

12.4(22)T

Cisco Unified CME 7.0(1)

This command was integrated into Cisco IOS Release
                                          						12.4(22)T.

15.2(1)T

Cisco Unified CME 8.8

This command was modified. The 6945 , 8941 , and 8945 keywords were added.

### Usage Guidelines

This command updates the Cisco Unified CME configuration file for the
                              		  specified type of Cisco Unified IP phone to add the name of the firmware file
                              		  to be loaded by a particular phone type. The firmware filename also provides
                              		  the version number for the phone firmware that is in the file. When a phone is
                              		  started up or rebooted, the phone reads the configuration file to determine
                              		  which firmware file it must load and then looks for that firmware file on the
                              		  TFTP server.

If applicable, Cisco Unified IP phones update themselves with new
                              		  phone firmware whenever they are started up or rebooted.

A separate load command is needed for each type of
                              		  phone. The Cisco Unified IP Phones 7940 and 7940G and the Cisco Unified IP
                              		  Phones 7960 and 7960G have the same phone firmware and share the 7960-7940 keyword.

Before Cisco Unified CME 7.0(1):

- Do not include the file suffix (.bin, .sbin, .loads) for any phone
                                 			 type except Cisco ATA and Cisco Unified IP Phone 7905 and 7912 when you
                                 			 configure the load command in telephony-service
                                 			 configuration mode. For example:

```
Router(config-telephony)# load 7941 SCCP41.8-2-2SR2S Router(config-telephony)#
```

- You must also configure the tftp-server command to enable TFTP access
                                 			 to the firmware files by Cisco Unified IP phones.

In Cisco Unified CME 7.0(1) and later versions:

- When specifying the load command for phone firmware versions later
                                 			 than version 8-2-2 for all phone types and you use the file suffix in the
                                 			 filename, the tftp-server bindings are automatically added for all the files
                                 			 forwarded for that load. For example:

```
Router(config-telephony)# load 7941 SCCP41.8-3-3S.loads Router(config-telephony)#
```

- The load command is enhanced to automatically
                                 			 create TFTP bindings for phone firmware files if the cnf-file location command is configured with the flash or slot0 keyword. You are no longer required
                                 			 to configure the tftp-server command to create TFTP bindings
                                 			 only if the location of the cnf files is router flash or slot 0 memory. If the cnf-file location command is configured for something
                                 			 other than flash or slot 0, such as a TFTP server (url) or system memory
                                 			 (system:its/), you must still configure the tftp-server command to create TFTP bindings
                                 			 for phone firmware files. Use the complete filename, including the file suffix,
                                 			 when you configure the tftp-server command for phone firmware versions later than version 8-2-2
                                 			 for all phone types.

To verify TFTP bindings, including the dictionary, language, and tone
                              		  configuration files that are associated with the ISO-3166 codes that have been
                              		  selected, use the show telephony-service tftp-bindings command.

After associating a firmware file with a Cisco Unified IP phone, use
                              		  the reset command to reboot the phone.

## Examples

## Examples

The following example shows how to identify the Cisco Unified IP
                              		  phone firmware file to be used by the Cisco Unified IP Phones 7960 and 7960G
                              		  and Cisco Unified IP Phone 7910G:

```
Router(config)# telephony-service Router(config-telephony)# load 7960-7940 P00303020209 Router(config-telephony)# load 7910 P00403020209 Router(config-telephony)# exit Router(config)# tftp-server flash:P00303020209.bin Router(config)# tftp-server flash:P00403020209.bin
```

### Related Commands

Command

Description

cnf-file location

Specifies a storage location for phone configuration files.

ephone-type

Adds a Cisco Unified IP phone type by defining a phone-type
                                          						template.

reset

Resets a Cisco Unified IP phone.

show telephony-service tftp-bindings

Provides a list of configuration files that are accessible
                                          						to IP phones using TFTP.

tftp-server

Enables TFTP access to firmware files on the TFTP server.

## load (voice
                        	 register global)

To associate a
                              		  type of IP phone with a phone firmware file, use the load command
                              		  in voice register global configuration mode. To disassociate a type of phone
                              		  from a phone firmware file, use the no form of
                              		  this command.

load phone-type firmware-file

no load phone-type firmware-file

### Syntax Description

phone-type

Type of
                                          						IP phone. The following choices are valid:

- 3905 —Cisco Unified IP Phone 3905.

- 3951 —Cisco Unified IP Phone 3911 and 3951.

- 6901 —Cisco Unified IP Phone 6901.

- 6911 —Cisco Unified IP Phone 6911.

- 6921 —Cisco Unified IP Phone 6921.

- 6941 —Cisco Unified IP Phone 6941.

- 6945 —Cisco Unified IP Phone 6945.

- 6961 —Cisco Unified IP Phone 6961.

- 7821 —Cisco
                                             						  Unified IP Phone 7821.

- 7841 —Cisco
                                             						  Unified IP Phone 7841.

- 7861 —Cisco
                                             						  Unified IP Phone 7861.

- 7905 —Cisco Unified IP Phone 7905 and 7905G.

- 7906 —Cisco Unified IP Phone 7906G.

- 7911 —Cisco
                                             						  Unified IP Phone 7911G.

- 7912 —Cisco
                                             						  Unified IP Phone 7912 and 7912G.

- 7941 —Cisco
                                             						  Unified IP Phone 7941G.

- 7941GE —Cisco
                                             						  Unified IP Phone 7941GE.

- 7942 —Cisco
                                             						  Unified IP Phone 7942.

- 7945 —Cisco
                                             						  Unified IP Phone 7945.

- 7960–7940 —Cisco Unified IP Phones 7940 and 7940G
                                             						  and Cisco IP Phones 7960 and 7960G.

- 7961 —Cisco
                                             						  Unified IP Phone 7961G.

- 7961GE —Cisco
                                             						  Unified IP Phone 7961GE.

- 7962 —Cisco
                                             						  Unified IP Phone 7962.

- 7965 —Cisco
                                             						  Unified IP Phone 7965.

- 7970 —Cisco
                                             						  Unified IP Phone 7970G.

- 7971 —Cisco
                                             						  Unified IP Phone 7971GE.

- 7975 —Cisco
                                             						  Unified IP Phone 7975.

- ATA —Cisco
                                             						  ATA-186 and Cisco ATA-188.

- ATA-187 —Cisco
                                             						  ATA-187.

- DX650 —Cisco
                                             						  DX650.

firmware-file

Filename for the Cisco Unified IP phone firmware to be associated with the IP
                                          						phone type. Do not use the .bin or .load file extension, except for the Cisco
                                          						Unified IP phone 7905, 7912, or ATA. Filenames are case sensitive.

### Command Default

The firmware file
                              		  is not associated with the type of phone.

### Command Modes

Voice register global configuration (config-register-global)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.4(4)T

Cisco
                                          						CME 3.4

This
                                          						command was introduced.

12.4(11)XJ

Cisco
                                          						Unified CME 4.1

The 3951 , 7911 , 7941 , 7941GE , 7961 , 7961GE , 7970, and 7971 keywords were added.

12.4(15)T

Cisco
                                          						Unified CME 4.1

The 3951 , 7911 , 7941 , 7941GE , 7961 , 7961GE , 7970 , and 7971 keywords were integrated into Cisco IOS Software Release 12.4(15)T.

12.4(15)XZ

Cisco
                                          						Unified CME 4.3

The 7942 , 7945 , 7962 , 7965 , and 7975 keywords were added.

12.4(20)T

Cisco
                                          						Unified CME 7.0

This
                                          						command was integrated into Cisco IOS Release 12.4(20)T.

15.2(1)T

Cisco
                                          						Unified CME 8.8

This
                                          						command was modified. The 3905 keyword was added.

15.2(2)T

Cisco
                                          						Unified CME 9.0

This
                                          						command was modified. The 6901 , 6911 , 6921 , 6941 , 6945 , 6961 , and ATA-187 keywords were added.

15.4(3)M

Cisco
                                          						Unified CME 10.5

This
                                          						command was modified to provide support for Cisco Unified 7821, 7841, 7861 and
                                          						DX650 IP phones.

### Usage Guidelines

This command
                              		  updates the Cisco Unified CME configuration file for the specified type of IP
                              		  phone to add the name of the correct firmware file that the phone should load.
                              		  This filename also provides the version number for the phone firmware that is
                              		  in the file. Later, whenever a phone is started up or rebooted, the phone reads
                              		  the configuration file to determine the name of the firmware file that it
                              		  should load and then looks for that firmware file on the TFTP server.

A separate load command is needed for each type of phone. The Cisco Unified IP Phone 7940 and
                              		  7940G and Cisco Unified IP Phone 7960 and 7960G have the same phone firmware
                              		  and share the 7960-7940 keyword. The Cisco Unified IP Phone 3911 and Cisco Unified IP Phone 3951 have
                              		  the same phone firmware and share the 3951 keyword.

For certain IP
                              		  phones, such as the Cisco Unified IP Phone 7906G, 7911G, 7941G, 7941GE, 7961G,
                              		  7961GE, 7970G, and 7971G, there are multiple firmware files. For these phones,
                              		  use the TERMnn.x-y-x-w.loads or SIPnn.x-y-x-w.loads firmware filename for the load command, without the .loads file extension. For these phones, you do not
                              		  configure the load command for any firmware file other than the
                              		  TERM.loads or SIP.loads firmware file.

Following the load command, use the tftp-server command to enable TFTP access to the file by Cisco Unified IP phones. The file
                              		  extension is required when using the tftp-server command.

The load command must be followed by a reboot of the phones. Plug in a new IP phone or
                              		  use the reset command to reboot an IP phone that is already connected to the Cisco router.

## Examples

The following
                              		  example shows how to configure the load command to indicate which phone firmware is
                              		  to be used by a Cisco Unified IP Phone 7960 and 7960G, a Cisco Unified IP Phone
                              		  7912 and 7912G, and a Cisco Unified IP Phone 7941GEs. The tftp-server command is used to specify the location of the phone firmware files, including
                              		  all firmware files for the Java-based Cisco Unified IP Phone 7941GE. Note that
                              		  while no file extension is used with the load command, the file extension is required when using the tftp-server command.

```
Router(config)# voice register global Router(config-register-global)# load 7960-7940 P00303020209 Router(config-register-global)# load 7912 P00403020209 Router(config-register-global)# load 7941 TERM41.7-0-3-0S Router(config-register-global)# exit Router(config)# tftp-server flash:P00303020209.bin Router(config)# tftp-server flash:P00403020209.bin Router(config)# tftp-server flash:SIP41.8-0-3-0S.loads Router(config)# tftp-server flash:term61.default.loadsterm Router(config)# tftp-server flash:41.default.loads Router(config)# tftp-server flash:CVM41.2-0-2-26.sbn Router(config)# tftp-server flash:cnu41.2-7-6-26.sbn Router(config)# tftp-server flash:Jar41.2-9-2-26.sbn
```

### Related Commands

Command

Description

reset (voice register global)

Performs a complete reboot of all SIP phones associated with a Cisco Unified
                                          						CME router.

show voice register global

Displays all global configuration parameters associated with SIP phones.

tftp-server

Enables TFTP access to firmware files on the TFTP server.

type (voice register pool)

Defines a phone type for a SIP phone.

## load-cfg-file

To load configuration files on the TFTP server and to sign
                              		  configuration files that are not created by Cisco Unified CME, use the load-cfg-file command in telephony-service
                              		  configuration mode. To return to the default, use the no form of this command.

load-cfg-file file-url alias file-alias [ sign ] [ create ]

no load-cfg-file file-url alias file-alias

### Syntax Description

file-url

Complete path of a configuration file in a local directory.

alias file-alias

Name of the file on the TFTP server.

sign

Signs the file and serves it on the TFTP server.

create

Creates the signed file in the local directory.

### Command Default

A file is not loaded on the TFTP server.

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

### Usage Guidelines

This command is used with Cisco Unified CME phone authentication to
                              		  sign configuration files that are not created by Cisco Unified CME. This
                              		  command also loads the signed and unsigned versions of the file on the TFTP
                              		  server. To simply serve an already signed file on the TFTP server, use this
                              		  command without the sign and create keywords.

The create keyword should be used with the sign keyword the first time that this command
                              		  is used for each file. The create keyword is not maintained in the
                              		  running configuration; this prevents signed files from being recreated during
                              		  every reload.

## Examples

The following example creates a file called ringlist.xml.sgn in slot0
                              		  and serves both ringlist.xml and ringlist.xml.sgn on the TFTP server.

```
telephony-service
 load-cfg-file slot0:Ringlist.xml alias Ringlist.xml sign create
```

The following example serves P00307010200.sbn on the TFTP server
                              		  without creating a signed file.

```
telephony-service
 load-cfg-file slot0:P00307010200.sbn alias P00307010200.sbn
```

## loc2

To specify the audio file used for the loss of C2 features
                              		  announcement, use the loc2 command in voice MLPP configuration mode. To disable use of
                              		  this audio file, use the no form of this command.

loc2 audio-url

no loc2

### Syntax Description

audio-url

Location of the announcement audio file in URL format.
                                          						Valid storage locations are TFTP, FTP, HTTP, and flash memory.

### Command Default

No announcement is played.

### Command Modes

Voice MLPP configuration (config-voice-mlpp)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.0(1)XA

Cisco Unified CME 8.0

This command was introduced.

15.1(1)T

Cisco Unified CME 8.0

This command was integrated into Cisco IOS Release
                                          						15.1(1)T.

### Usage Guidelines

This command specifies the G.711 a-law or u-law 8-KHz encoded audio
                              		  file (.wav or .au format) for the announcement that plays to callers when the
                              		  call leaves the Cisco Unified CME router on the trunk or when the user places a
                              		  call to a different domain.

The mlpp indication command must be enabled (default) for a
                              		  phone to play precedence announcements.

This command is not supported by Cisco IOS help. If you type ? , Cisco IOS help does not display a list of
                              		  valid entries.

## Examples

The following example shows that the audio file played for the
                              		  isolated code announcement is named ica.au located in flash:

```
Router(config)# voice mlpp Router(config-voice-mlpp)# loc2 flash:loc2.au
```

### Related Commands

Command

Description

bnea

Specifies the audio file used for the busy station not
                                          						equipped for preemption announcement.

upa

Specifies the audio file used for the unauthorized
                                          						precedence announcement.

vca

Specifies the audio file used for the vacant code
                                          						announcement.

mlpp indication

Enables MLPP indication on an SCCP phone or analog FXS
                                          						port.

mlpp preemption

Enables preemption capability on an SCCP phone or analog
                                          						FXS port.

## location (voice emergency response zone)

To include a location within an emergency response zone, use the location command in voice emergency response
                              		  zone mode. To assign specific priorites to the locations, use the priority tag.
                              		  To remove the location, use the no form of this command.

location location-tag [priority
                                 				  <1-100>]

no location location-tag

### Syntax Description

location-tag

Identifier for the emergency response zone location.

priority 1-100

Identifier (1-100) for the priority ranking of locations, 1
                                          						being the highest priority.

### Command Modes

Voice emergency response zone configuration (cfg-emrgncy-resp-zone)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)XY

Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1)

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

Use this command to create locations within emergency response zones.
                              		  The tag must be the same as the tag that is defined using the voice emergency response location command. This allows routing of 911 calls
                              		  to different public safety answering poins (PSAPs). Priority is optional and
                              		  allows searching locations in a specified priority order. If there are
                              		  locations with assigned priorities and locations configured without priorities,
                              		  the prioritized locations are searched before those without an assigned
                              		  priority.

## Examples

The following example shows an assignment of emergency response
                              		  location (ERLs) to two zones, 10 and 11, to route callers to two different
                              		  PSAPs. The locations for ERLs in zone 10 are searched in sequential order for a
                              		  phone address match. The calls from zone 10 have an emergency location
                              		  identification number (ELIN) from ERLs 8, 9, and 10. The calls from zone 11
                              		  have an ELIN from ERLs 2, 3, 4, and 5. The locations for ERLs in zone 11 have
                              		  priorities assigned and is searched in order of the assigned priority and not
                              		  the ERL tag number.

```
voice emergency response zone 10
location 8
location 9
location 10
voice emergency response zone 11
location 5 priority 1
location 3 priority 2
location 4 priority 3
location 2 priority 10
```

### Related Commands

Command

Description

emergency response callback

Defines a dial peer that is used for 911 callbacks from the
                                          						PSAP.

emergency response location

Associates an ERL to either a SIP phone, ephone, or dial
                                          						peer.

voice emergency response location

Creates a tag for identifying an ERL for the enhanced 911
                                          						service.

voice emergency response zone

Creates an emergency response zone within which ERLs can be
                                          						grouped.

## log password

Effective with Cisco Unified CME 4.0, the log password command was replaced by the xml user command in telephony-service configuration
                              		  mode. See the xml user command for more information.

For Cisco CME 3.4 and earlier versions, to set a local password for
                              		  an eXtensible Markup Language (XML) Application Programming Interface (API)
                              		  query, use the log password command in telephony-service configuration mode. To remove the
                              		  password definition, use the no form of this command.

log password password-string

no log password password-string

### Syntax Description

password-string

Character string that is a password for XML API queries.
                                          						Maximum length is 28 characters. Longer strings are truncated.

### Command Default

No password is defined.

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

This command was replaced by the xml user command.

12.4(9)T

Cisco Unified CME 4.0

This command was replaced by the xml user command.

Cisco IOS XE Gibraltar 16.11.1a Release

Unified CME 12.6

The command is deprecated. It is not supported on Unified CME 12.6 and later releases.

### Usage Guidelines

The local password is used to authenticate XML API requests on the
                              		  network management server. If the password is not set, an XML API query fails
                              		  local authentication.

The password string is stored as plain text. No encryption is
                              		  supported.

## Examples

The following example defines a local password for XML API requests:

```
Router(config)# telephony-service Router(config-telephony)# log password ewvpil
```

## log table

To set parameters for the table used to capture phone events used for
                              		  the eXtensible Markup Language (XML) Application Programming Interface (API),
                              		  use the log table command in telephony-service configuration mode. To reset
                              		  parameters to their default values, use the no form of this command.

log table { max-size entries | retain-timer minutes }

no log table { max-size | retain-timer }

### Syntax Description

max-size entries

Number of entries in the log table. Range is from 0 to
                                          						1000. Default is 150.

retain-timer minutes

Number of minutes to retain entries in the log table. Range
                                          						is from 2 to 500. Default is 15.

### Command Default

Default number of entries in table is 150. default number of minutes
                              		  to retain entries in table is 15.

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

### Usage Guidelines

Cisco Unified CME captures and time-stamps events, such as phones
                              		  registering and unregistering and extension status, and stores them in an
                              		  internal buffer. This command sets the maximum number of events, or entries,
                              		  that can be stored in the table. One event equals one entry. The retain-timer keyword sets the number of
                              		  minutes that events are kept in the buffer before they are deleted.

The event table can be viewed using the show fb-its-log command.

## Examples

The following example sets the maximum size of the table at 750
                              		  events and sets the retention time at 30 minutes:

```
Router(config)# telephony-service Router(config-telephony)# log table max-size 750 Router(config-telephony)# log table retain-timer 30
```

### Related Commands

Command

Description

show fb-its-log

Displays information about the Cisco CME XML API
                                          						configuration, statistics on XML API queries, and event logs.

## logging (voice emergency response settings)

To enable sylog messages to capture emergency call data, use the logging command in voice emergency response
                              		  settings configuration mode. To disable logging, use the no form of this command.

logging

no logging

### Syntax Description

This command has no arguments or keywords.

### Command Default

This command is enabled by default.

### Command Modes

Voice emergency response settings configuration (cfg-emrgncy-resp-settings)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)XY

Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1)

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

Use this command to enable syslog messages to be announced for every
                              		  911 emergency call that is made. The syslog messages can be used by third party
                              		  applications to send pager or e-mail notifications to an in-house support
                              		  number. This optional command is enabled by default.

## Examples

In this example, the ELIN (4085550101) defined in the voice emergency
                              		  response settings configuration is used if the 911 caller’s IP phones address
                              		  does not match any of the voice emergency response locations. After the 911
                              		  call is placed to the PSAP, the PSAP has 120 minutes to call back 408 555-0101
                              		  to reach the 911 caller. If the call history has expired (after 120 minutes),
                              		  any callback is routed to extension 7500. The outbound 911 calls do not emit a
                              		  syslog message to the logging facility (for example, a local buffer, console,
                              		  or remote host).

```
voice emergency response settings
callback 7500
elin 4085550101
expiry 120
no logging
```

### Related Commands

Command

Description

callback

Default phone number to contact if a 911 callback cannot
                                          						find the last 911 caller from the ERL.

elin

E.164 number used as the default ELIN if no matching ERL to
                                          						the 911 caller’s IP phone address is found.

expiry

Number of minutes a 911 call is associated with an ELIN in
                                          						case of a callback from the 911 operator.

voice emergency response settings

Creates a tag for identifying settings for E911 behavior.

## login (telephony-service)

To define the timer for automatically deactivating user login on SCCP
                              		  phones in a Cisco Unified CME system, use the login command in telephony-service configuration mode. To revert to
                              		  the default values for automatic logout, use the no form of this command.

login [ timeout [minutes] ] [ clear time ]

no login

### Syntax Description

timeout

(Optional) Period of phone idleness after which user login
                                          						is deactivated.

minutes

(Optional) Number of minutes for which an IP phone can be
                                          						idle before the user is logged out automatically. Range: 1 to 1440. Default:
                                          						60.

clear time

(Optional) Time of day after which user login for all IP
                                          						phones is deactivated. Range: 00:00 to 24:00 on a 24-hour clock. Default: 24:00
                                          						(midnight).

### Command Default

User login is deactivated after a phone is idle for 60 minutes. User
                              		  login for all phones is deactivated at 24:00.

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

12.4(11)XJ2

Cisco Unified CME 4.1

Minimum value for the minutes argument was lowered from 5 minutes to 1 minute.

12.4(15)T

Cisco Unified CME 4.1

This command with the modifications was integrated into
                                          						Cisco IOS Release 12.4(15)T.

### Usage Guidelines

This command defines the after-hours login timer. Individual users on
                              		  specified phones can override call blocking by logging in using a personal
                              		  identification number (PIN). The after-hours login timer deactivates user login
                              		  on all phones at a specific time and deactivates a login session automatically
                              		  after a phone is idle for a specified period of time.

The login command applies only to IP phones that
                              		  have soft keys, such as the Cisco Unified IP Phone 7940 and 7940G and the Cisco
                              		  Unified IP Phone 7960 and 7960G.

For this command to take effect, fast reboot and reregister all
                              		  phones in Cisco Unified CME by using the restart all command in telephony-service configuration mode.

When a Cisco Unified CME router is rebooted, the login status for all
                              		  phones is reset to the default.

## Examples

The following example sets the after-hours login timer to deactivate
                              		  logged in phone users automatically after a 2-hour idle time and after 11:30
                              		  p.m.

```
Router(config)# telephony-service Router(config-telephony)# login timeout 120 clear 2330
```

### Related Commands

Command

Description

after-hour exempt

Specifies that an IP phone does not have any of its
                                          						outgoing calls blocked even though call blocking has been defined.

after-hours block pattern

Defines a pattern of digits for blocking outgoing calls
                                          						from IP phones.

after-hours date

Defines a recurring period based on date during which
                                          						outgoing calls that match defined block patterns are blocked on IP phones.

after-hours day

Defines a recurring period based on day of the week during
                                          						which outgoing calls that match defined block patterns are blocked on IP
                                          						phones.

pin

Sets a global/individual PIN for phone users to deactivate
                                          						call blocking during call blocking periods.

restart (telephony-service)

Performs a fast reboot of one or all phones associated with
                                          						a Cisco Unified CME router.

show ephone login

Displays the login states of all phones.

## logo (voice register global)

To specify a file to display on SIP phones, use the logo command in voice register global
                              		  configuration mode. To disable the display of the file, use the no form of this command.

logo url

no logo

### Syntax Description

url

URL as defined in RFC 2396.

### Command Default

No file is specified for display on idle phones.

### Command Modes

Voice register global configuration (config-register-global)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4

This command was introduced.

### Usage Guidelines

Use this command to define the URL for the file to be used by SIP
                              		  phones connected in Cisco Unified CME. The file that is displayed must be
                              		  encoded in eXtensible Markup Language (XML) by using the Cisco XML document
                              		  type definition (DTD). For more information about Cisco DTD formats, see the Cisco IP Phone Services Application Development Notes.

After you configure this command, restart the phones by using the reset command.

## Examples

The following example shows how to specify that the file logo.xml
                              		  should be displayed on SIP phones:

```
Router(config)# voice register global Router(config-register-global)# logo http://mycompany.com/files/logo.xml
```

### Related Commands

Command

Description

reset (voice register pool)

Performs a complete reboot of one phone associated with a
                                          						Cisco CME router.

reset (voice register global)

Performs a complete reboot of one or all phones associated
                                          						with a Cisco CME router.

## logout-profile

To enable an IP phone for extension mobility and to apply a default
                              		  logout profile to the phone, use the logout-profile command in ephone
                              		  configuration mode. To disable extension mobility, use the no form of this command.

logout-profile profile-tag

no logout-profile profile-tag

### Syntax Description

profile-tag

Unique identifier for a default logout profile to be
                                          						applied. Previously created by using the voice logout-profile command in voice
                                          						logout-profile configuration mode. Range: 1 to maximum number of phones
                                          						supported by platform.

### Command Default

IP phone is not enabled for extension mobility.

### Command Modes

Ephone configuration (config-ephone), Voice Register Pool configuration (voice register pool)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(11)XW

Cisco Unified CME 4.2

This command was introduced.

12.4(15)XY

Cisco Unified CME 4.2(1)

This command was introduced.

12.4(15)XZ

Cisco Unified CME 4.3

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0

This command is integrated into Cisco IOS Release
                                          						12.4(20)T.

15.1(4)M

Cisco Unified CME 8.6

This command was introduced.

### Usage Guidelines

Use this command in ephone configuration mode to enable a supported
                              		  IP phone registered in Cisco Unified CME for extension mobility and to apply a
                              		  default logout profile to the ephone being configured.

In Cisco Unified CME 4.2, extension mobility is supported only on
                              		  SCCP IP phones.

In Cisco Unified CME 8.6 extension mobility is supported on SIP
                              		  phones.

Extension mobility is not supported on non-display IP phones.

Extension mobility is not supported for analog devices.

Before using this command, you must create a logout profile to be
                              		  applied to this phone by using the voice logout-profile command.

You cannot apply more than one logout profile to an ephone. If you
                              		  attempt to apply a second logout profile to an ephone to which a profile has
                              		  already been applied, the second profile will overwrite the first logout
                              		  profile configuration.

## Examples

The following example shows the ephone configuration for three
                              		  different Cisco Unified IP phones. All three phones are enabled for extension
                              		  mobility and share the same logout profile number (1), to be downloaded when
                              		  these phones boot and when no phone user is logged into these phones:

```
ephone 1
 mac-address 000D.EDAB.3566
 type 7960
 logout-profile 1
ephone 2
 mac-address 0012.DA8A.C43D
 type 7970
 logout-profile 1
ephone 3
 mac-address 1200.80FC.9B01
 type 7911
 logout-profile 1
```

The following example shows the ephone configuration for two
                              		  different Cisco Unified IP phones. Both phones are enabled for extension
                              		  mobility and share the same logout profile number (22), to be downloaded when
                              		  these phones boot and when no phone user is logged into these phones:

```
voice register pool  1
 logout-profile 22
 id mac 0012.0034.0056
 type 7960
voice register pool  2
 logout-profile 22
 id mac 0001.0023.0045
 type 7912
```

### Related Commands

Command

Description

reset (voice logout-profile and voice user-profile)

Performs a complete reboot of all IP phones to which a
                                          						particular logout-profile or user-profile is downloaded.

voice logout-profile

Enters voice profile configuration mode to configure a
                                          						default logout profile for extension mobility.

## loopback-dn

To create a virtual loopback voice port (loopback-dn) to establish a
                              		  demarcation point for VoIP calls and supplementary services, use the loopback-dn command in ephone-dn
                              		  configuration mode. To delete a loopback-dn configuration, use the no form of this command.

loopback-dn dn-tag [ forward number-of-digits | strip number-of-digits ] [ prefix prefix-digit-string ] [ suffix suffix-digit-string ] [ retry seconds ] [ auto-con ] [ codec { g711alaw | g711ulaw }]

no loopback-dn

### Syntax Description

dn-tag

Unique sequence number that identifies the ephone-dn that
                                          						is being paired for loopback with the ephone-dn that is currently being
                                          						configured. The paired ephone-dn must be one that is already defined in the
                                          						system.

forward number-of-digits

(Optional) Number of digits in the original called number
                                          						to forward to the other ephone-dn in the loopback-dn pair. Range is from 1 to
                                          						32 digits. Default is to forward all digits.

strip number-of-digits

(Optional) Number of leading digits to be stripped from the
                                          						original called number before forwarding to the other ephone-dn in the
                                          						loopback-dn pair. Range is from 1 to 32 digits. Default is not to A-law strip
                                          						any digits.

prefix prefix-digit-string

(Optional) Defines a string of digits to add in front of
                                          						the forwarded called number. Maximum number of digits in the string is 32.
                                          						Default is that no prefix is defined.

suffix suffix-digit-string

(Optional) Defines a string of digits to add to the end of
                                          						the forwarded called number. Maximum number of digits in the string is 32.
                                          						Default is that no suffix is defined. If you add a suffix that starts with the
                                          						pound character (#), the string must be enclosed in quotation marks.

retry seconds

(Optional) Number of seconds to wait before retrying the
                                          						loopback target when it is busy or unavailable. Range is from 0 to 32767.
                                          						Default is that retry is disabled and appropriate call-progress tones are
                                          						passed to the call originator.

auto-con

(Optional) Immediately connects the call and provides
                                          						in-band alerting while waiting for the far-end destination to answer. Default
                                          						is that automatic connection is disabled.

codec

(Optional) Explicitly forces the G.711 A-law or G.711
                                          						mu-law voice coding type to be used for calls that pass through the
                                          						loopback-dn. This overrides the G.711 coding type that is negotiated for the
                                          						call and provides mu-law to A-law conversion if needed. Default is that
                                          						Real-Time Transport Protocol (RTP) voice packets are passed through the
                                          						loopback-dn without considering the G.711 coding type negotiated for the calls.

g711alaw

G.711 A-law, 64000 bits per second, for T1.

g711ulaw

G.711 mu-law, 64000 bits per second, for E1.

### Command Default

All calls are set to forward all digits and not to strip any digits.
                              		  Prefix is not defined. Suffix is not defined. Retry is disabled. Automatic
                              		  connection is disabled. RTP voice packets are passed through the loopback-dn
                              		  without considering the G.711 coding type negotiated for the call.

### Command Modes

Ephone-dn configuration (config-ephone-dn)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(2)XT

Cisco ITS 2.0

This command was introduced.

12.2(2)XT3

Cisco ITS 2.0

The suffix keyword was added.

12.2(8)T

Cisco ITS 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and the auto-con keyword was added.

12.2(11)T

Cisco ITS 2.01

The suffix keyword was
                                          						added .

12.2(11)YT

Cisco ITS 2.1

The strip keyword was added.

12.2(11)YT2

Cisco ITS 2.1

The codec keyword was added.

12.2(15)T

Cisco ITS 2.1

This command was integrated into Cisco IOS Release
                                          						12.2(15)T.

### Usage Guidelines

The loopback-dn command is used to configure two
                              		  ephone-dn virtual voice ports as back-to-back-connected voice-port pairs. A
                              		  call presented on one side of the loopback-dn pair is reoriginated as a new
                              		  call on the opposite side of the loopback-dn pair. The forward , strip, prefix , and suffix keywords can be used to manipulate the
                              		  original called number that is presented to the incoming side of the
                              		  loopback-dn pair to generate a modified called number to use when reoriginating
                              		  the call at the opposite side of the loopback-dn pair. For loopback-dn
                              		  configurations, you must always configure ephone-dn virtual voice ports as
                              		  cross-coupled pairs.

The loopback-dn arrangement allows an incoming telephone call to be
                              		  terminated on one side of the loopback-dn port pair and a new pass-through
                              		  outgoing call to be originated on the other side of the loopback-dn port pair.
                              		  The loopback-dn port pair normally works with direct cross-coupling of their
                              		  call states; the alerting call state on the outbound call segment is associated
                              		  with the ringing state on the inbound call segment.

The loopback-dn mechanism allows for call operations (such as call
                              		  transfer and call forward) that are invoked for the call segment on one side of
                              		  the loopback-dn port pair to be isolated from the call segment that is present
                              		  on the opposite side of the loopback-dn port pair. This approach is useful when
                              		  the endpoint devices associated with the two different sides have mismatched
                              		  call-transfer and call-forwarding capabilities. The loopback-dn arrangement
                              		  allows for call-transfer and call-forward requests to be serviced on one side
                              		  of the loopback-dn port pair by creating hairpin-routed calls when necessary.
                              		  The loopback-dn arrangement avoids the propagation of call-transfer and
                              		  call-forward requests to endpoint devices that do not support these functions.

The loopback-dn command provides options for
                              		  controlling the called-number digits that are passed through from the incoming
                              		  side to the outgoing side. The available digits can be manipulated with the forward , strip , prefix , and suffix keywords.

The forward keyword defines the number of digits
                              		  in the original called number to forward to the other ephone-dn in the
                              		  loopback-dn pair. The default is set to forward all digits. The strip keyword defines the number of leading
                              		  digits to be stripped from the original called number before forwarding to the
                              		  other ephone-dn in the loopback-dn pair. The default is set to not strip any
                              		  digits. The forward and strip commands are mutually exclusive and can
                              		  be used with any combination of the prefix and suffix keywords.

The prefix keyword defines a string of digits to
                              		  add in front of the forwarded number.

The suffix keyword is most commonly used to add a
                              		  terminating “#” (pound-sign) character to the end of the forwarded number to
                              		  indicate that no more digits should be expected. The pound-sign character
                              		  indicates to the call-routing mechanism that is processing the forwarded number
                              		  that the forwarded number is complete. Providing an explicit end-of-number
                              		  character also avoids a situation in which the call-processing mechanism waits
                              		  for the interdigit timeout period to expire before routing the call onward
                              		  using the forwarded number.

The retry keyword is used to suppress a far-end
                              		  busy indication on the outbound call segment. Instead of returning a busy
                              		  signal to the call originator (on the incoming call segment), a loopback-dn
                              		  presents an alerting or ringing tone to the caller and then periodically
                              		  retries the call to the final far-end destination (on the outgoing call
                              		  segment). This is not bidirectional. To prevent calls from being routed into
                              		  the idle outgoing side of the loopback-dn port pair during the idle interval
                              		  that occurs between successive outgoing call attempts, configure the outgoing
                              		  side of the loopback-dn without a number so that there is no number to match
                              		  for the inbound call.

The auto-con keyword is used to configure a
                              		  premature trigger for a connected state for an incoming call segment while the
                              		  outgoing call segment is still in the alerting state. This setup forces the
                              		  voice path to open for the incoming call segment and support the generation of
                              		  in-band call progress tones for busy, alerting, or ringback. The disadvantage
                              		  of the auto-con keyword is premature opening of the
                              		  voice path during the alerting stage and also triggering of the beginning of
                              		  billing for the call before the call has been answered by the far end. These
                              		  disadvantages should be considered carefully before you use
                              		  the auto-con keyword.

The codec keyword is used to explicitly select
                              		  the A-law or mu-law type of G.711 and to provide A-law to mu-law conversion if
                              		  needed. Setting the codec type on one side of the loopback-dn forces the
                              		  selection of A-law or mu-law for voice packets that are transmitted from that
                              		  side of the loopback-dn. To force the A-law or mu-law G.711 codec type for both
                              		  voice packet directions, set the codec type on both sides of the loopback-dn.
                              		  Loopback-dn configurations are used only with G.711 calls. Other voice codec
                              		  types are not supported.

## Examples

The following example creates a loopback-dn configured with the forward and prefix keywords:

```
Router(config)# ephone-dn 7 Router(config-ephone-dn)# loopback-dn 15 forward 5 prefix 41
```

The following example creates a loopback-dn that appends the
                              		  pound-sign (#) character to forwarded numbers to indicate the end of the
                              		  numbers:

```
Router(config)# ephone-dn 7 Router(config-ephone-dn)# loopback-dn 16 suffix “#”
```

The following example shows a loopback-dn configuration that pairs
                              		  ephone-dns 15 and 16. An incoming call (for example, from VoIP) to 4085550101
                              		  matches ephone-dn 16. The call is then reoriginated from ephone-dn 15 and sent
                              		  to extension 50101. Another incoming call (for example, from a local IP phone)
                              		  to extension 50151 matches ephone-dn 15. It is reoriginated from ephone-dn 16
                              		  and sent to 4085550151.

```
ephone-dn 15
 number 5015.
 loopback-dn 16 forward 5 prefix 40855
 caller-id local
 no huntstop
!
ephone-dn 16
 number 408555010.
 loopback-dn 15 forward 5
 caller-id local
 no huntstop
```

### Related Commands

Command

Description

ephone-dn

Enters ephone-dn configuration mode.

show ephone-dn loopback

Displays information about loopback ephone-dns that have
                                          						been created in a Cisco CME system.

## lpcor incoming

To associate an incoming call with a logical partitioning class of
                              		  restriction (LPCOR) resource-group policy, use the lpcor incoming command in ephone, ephone-template, trunk group, voice port,
                              		  voice register pool, voice register template, or voice service configuration
                              		  mode. To reset to the default, use the no form of this command.

lpcor incoming lpcor-group

no lpcor incoming

### Syntax Description

lpcor-group

Name of the LPCOR resource group.

### Command Default

LPCOR policy is not associated with the incoming call.

### Command Modes

Ephone configuration (config-ephone) Ephone template configuration (config-ephone-template) Trunk group configuration (config-trunk-group) Voice port configuration (config-voiceport) Voice register pool configuration (config-register-pool) Voice register template configuration (config-register-temp) Voice service configuration (conf-voi-serv)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.0(1)XA

Cisco Unified CME 8.0

This command was introduced.

15.1(1)T

Cisco Unified CME 8.0

This command was integrated into Cisco IOS Release
                                          						15.1(1)T.

### Usage Guidelines

Analog Phones

An incoming call to an analog phone is associated with the LPCOR
                              		  policy specified with this command in the voice port. Otherwise the LPCOR
                              		  policy specified in the trunk group is used.

SCCP IP Phones (Local or Remote)

An incoming call to an SCCP IP phone is associated with the LPCOR
                              		  policy specified with this command in ephone or ephone template configuration
                              		  mode. The ephone configuration has precedence over the ephone-template
                              		  configuration. All directory numbers on the phone share the same LPCOR setting.

SIP IP Phones (Local or Remote)

An incoming call to a SIP IP phone is associated with the LPCOR
                              		  policy specified with this command in voice register pool or voice register
                              		  template configuration mode. The voice register pool configuration has
                              		  precedence over the voice register template configuration. All directory
                              		  numbers on the phone share the same LPCOR setting.

- Phones that share a directory number must be configured with the
                                 			 same LPCOR policy. Different LPCOR settings on shared-line phones are not
                                 			 supported.

PSTN Trunks

An incoming call to the PSTN is associated with the LPCOR policy
                              		  specified with this command in the voice port. Otherwise the LPCOR policy
                              		  specified in the trunk group is used. The voice port configuration takes
                              		  precedence.

VoIP Trunks (H.323 or SIP)

An incoming call to a VoIP trunk is associated with the LPCOR policy
                              		  specified with this command in voice service configuration mode if the remote
                              		  IP address is not found in the IP trunk subnet table created with the voice lpcor ip-trunk subnet incoming command.

## Examples

The following example shows the command used in different
                              		  configuration modes:

```
voice service voip
 lpcor incoming voip_group1
!
trunk group analog1
 lpcor incoming analog_group1
 lpcor outgoing analog_group1
!
voice-port 1/1/0
 lpcor incoming vp_group1
 lpcor outgoing vp_group1
!
voice register pool  3
 lpcor type remote
 lpcor incoming sip_group3
 lpcor outgoing sip_group3
 id mac 001E.BE8F.96C0
 type 7940
 number 1 dn 3
!
ephone 2 
 mac-address 001C.821C.ED23 
 type 7960
 button 1:2
 lpcor type remote
 lpcor incoming ephone_group2
 lpcor outgoing ephone_group2
```

### Related Commands

Command

Description

lpcor outgoing

Associates an outgoing call with a LPCOR resource-group
                                          						policy.

lpcor type

Specifies the LPCOR type for an IP phone.

voice lpcor ip-trunk subnet incoming

Creates a LPCOR IP-trunk subnet table for incoming calls
                                          						from a VoIP trunk.

voice lpcor policy

Creates a LPCOR policy for a resource group.

## lpcor outgoing

To associate an outgoing call with a logical partitioning class of
                              		  restriction (LPCOR) resource-group policy, use the lpcor outgoing command in dial peer, ephone, ephone template, trunk group,
                              		  voice port, voice register pool, or voice register template configuration mode.
                              		  To reset to the default, use the no form of this command.

lpcor outgoing lpcor-group

no lpcor outgoing

### Syntax Description

lpcor-group

Name of the LPCOR resource group.

### Command Default

LPCOR policy is not associated with the outgoing call.

### Command Modes

Dial peer configuration (config-dial-peer) Ephone configuration (config-ephone) Ephone template configuration (config-ephone-template) Trunk group configuration (config-trunk-group) Voice port configuration (config-voiceport) Voice register pool configuration (config-register-pool) Voice register template configuration (config-register-temp)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.0(1)XA

Cisco Unified CME 8.0

This command was introduced.

15.1(1)T

Cisco Unified CME 8.0

This command was integrated into Cisco IOS Release
                                          						15.1(1)T.

### Usage Guidelines

Analog Phones

An outgoing call from an analog phone is associated with the LPCOR
                              		  policy specified with this command in the voice port. Otherwise the LPCOR
                              		  policy specified in the trunk group is used.

SCCP IP Phones (Local or Remote)

An outgoing call from an SCCP IP phone is associated with the LPCOR
                              		  policy specified with this command in ephone configuration or ephone template
                              		  configuration mode. The ephone configuration has precedence over the
                              		  ephone-template configuration. All directory numbers on the phone share the
                              		  same LPCOR setting.

SIP IP Phones (Local or Remote)

An outgoing call from a SIP IP phone is associated with the LPCOR
                              		  policy specified with this command in voice register pool or voice register
                              		  template configuration mode. The voice register pool configuration has
                              		  precedence over the voice register template configuration. All directory
                              		  numbers on the phone share the same LPCOR setting.

- Phones that share a directory number must be configured with the
                                 			 same LPCOR policy. Different LPCOR settings on shared-line phones are not
                                 			 supported.

PSTN Trunks

An outgoing call from the PSTN uses the LPCOR policy specified with
                              		  this command in the voice port if the outbound dial peer is configured with the port command. Otherwise the outgoing call
                              		  uses the LPCOR policy specified with this command in the trunk group if the
                              		  outbound dial peer is configured with the trunkgroup command.

VoIP Trunks (H.323 or SIP)

An outgoing VoIP call uses the LPCOR policy specified with this
                              		  command in the outbound dial peer. Otherwise the outgoing call uses the default
                              		  LPCOR policy.

## Examples

The following example shows the command used in different
                              		  configuration modes:

```
trunk group analog1
 lpcor incoming analog_group1
 lpcor outgoing analog_group1
!
voice-port 1/1/0
 lpcor incoming vp_group1
 lpcor outgoing vp_group1
!
dial-peer voice 2 voip
 destination-pattern 2...
 lpcor outgoing voip_group2
 session protocol sipv2
 session target ipv4:192.168.97.1
!
voice register pool  3
 lpcor type remote
 lpcor incoming sip_group3
 lpcor outgoing sip_group3
 id mac 001E.BE8F.96C0
 type 7940
 number 1 dn 3
!
ephone 2 
 mac-address 001C.821C.ED23 
 type 7960
 button 1:2
 lpcor type remote
 lpcor incoming ephone_group2
 lpcor outgoing ephone_group2
```

### Related Commands

Command

Description

lpcor incoming

Associates an incoming call with a LPCOR resource-group
                                          						policy.

lpcor type

Specifies the LPCOR type for an IP phone.

port (dial-peer)

Associates a dial peer with a voice port.

trunkgroup

Associates a dial peer with a trunk group.

voice lpcor policy

Creates a LPCOR policy for a resource group.

## lpcor type

To specify the logical partitioning class of restriction (LPCOR) type
                              		  for an IP phone, use the lpcor type command in ephone, ephone-template, voice register pool, or
                              		  voice register template configuration mode. To reset to the default, use the no form of this command.

lpcor type { local | mobile | remote }

no lpcor type

### Syntax Description

local

IP phone always registers to Cisco Unified CME through the
                                          						LAN.

mobile

IP phone can register to Cisco Unified CME through the LAN
                                          						or WAN.

remote

IP phone always registers to Cisco Unified CME through the
                                          						WAN.

### Command Default

LPCOR feature is disabled for the IP phone.

### Command Modes

Ephone configuration (config-ephone) Ephone-template configuration (config-ephone-template) Voice register pool configuration (config-register-pool) Voice register template configuration (config-register-temp)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.0(1)XA

Cisco Unified CME 8.0

This command was introduced.

15.1(1)T

Cisco Unified CME 8.0

This command was integrated into Cisco IOS Release
                                          						15.1(1)T.

### Usage Guidelines

According to the Telecom Regulatory Authority of India (TRAI)
                              		  requirements, an IP phone can accept both PSTN and VoIP calls if it is locally
                              		  registered to Cisco Unified CME through the LAN. Select the local keyword for this type of phone.

If an IP phone is registered remotely to Cisco Unified CME through
                              		  the WAN, PSTN calls must be blocked from that remote IP phone. Select the remote keyword for this type of phone.

A static LPCOR policy is applied to an IP phone if the phone
                              		  registers to Cisco Unified CME from the same region (local or remote)
                              		  permanently.

If an IP phone moves between the local and remote regions, such as an
                              		  Extension Mobility phone, Cisco IP Communicator softphone, or remote
                              		  teleworker, select the mobile keyword. The LPCOR policy is assigned
                              		  dynamically based on the phone’s currently registered IP address.

If you use a phone template to apply a command to a phone and you
                              		  also use the same command in the phone configuration of the same phone, the
                              		  value in phone configuration has priority.

## Examples

The following example shows that SCCP IP phone 2 is set to the remote
                              		  LPCOR type:

```
ephone 2 
 mac-address 001C.821C.ED23 
 type 7960
 button 1:2
 lpcor type remote
 lpcor incoming ephone_group2
 lpcor outgoing ephone_group2
```

### Related Commands

Command

Description

lpcor incoming

Associates a LPCOR resource-group policy with an incoming
                                          						call.

lpcor outgoing

Associates a LPCOR resource-group policy with an outgoing
                                          						call.

voice lpcor policy

Creates a LPCOR policy for a resource group.

| string | Alphanumeric string of up to 30 characters. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| number | Associates a telephone or extension number with an
                                          						ephone-dn in a Cisco CME system. |
| restart (ephone) | Performs a fast reboot of a single phone associated with a
                                          						Cisco CME router. |
| restart (telephony-service) | Performs a fast reboot of one or all phones associated with
                                          						a Cisco CME router. |

| string | Alphanumeric string of up to 30 characters. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

| Command | Description |
|---|---|
| number (voice register dn) | Associates a telephone or extension number with a directory
                                          						number in a Cisco CME system. |
| reset (voice register pool) | Performs a compete reboot of a single SIP phone associated
                                          						with a Cisco CME router. |
| reset (voice register global) | Performs a complete reboot of all SIP phones associated
                                          						with a Cisco CME router. |

| number | Preconfigured extension or E.164 number. An asterisk (*) can take the place of an extension number
                                          						to represent a wildcard slot. An agent at an authorized ephone-dn can
                                          						dynamically join and leave a hunt group if a wildcard slot is available. There
                                          						can be up to 20 wildcard slots in a hunt group. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.3(11)XL | Cisco CME 3.2.1 | The number of ephone-dns allowed was increased to 20. |
| 12.3(14)T | Cisco CME 3.3 | This command was integrated into Cisco IOS Release
                                          						12.3(14)T. |
| 12.4(4)XC | Cisco Unified CME 4.0 | The use of wildcard asterisks (*) in the dn-number argument was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | The use of wildcard asterisks (*) in the dn-number argument was integrated into Cisco IOS
                                          						Release 12.4(9)T. |

| Command | Description |
|---|---|
| ephone-hunt login | Allows an ephone-dn to dynamically join and leave an ephone
                                          						hunt group. |
| final | Defines the last ephone-dn in an ephone hunt group. |
| hops | Defines the number of times that a call is redirected to
                                          						the next ephone-dn in a peer ephone-hunt-group list before proceeding to the
                                          						final ephone-dn. |
| max-redirect | Changes the current number of allowable redirects in a
                                          						Cisco CME system. |
| no-reg (ephone-hunt) | Specifies that the pilot number of this ephone hunt group
                                          						should not register with the H.323 gatekeeper. |
| number (ephone-dn) | Associates an extension or telephone number with a
                                          						directory number. |
| pilot | Defines the ephone-dn that is dialed to reach an ephone
                                          						hunt group. |
| preference (ephone-hunt) | Sets preference order for the ephone-dn associated with an
                                          						ephone-hunt-group pilot number. |
| show ephone-hunt | Displays ephone-hunt group configuration, current status,
                                          						and statistics. |
| timeout (ephone-hunt) | Sets the number of seconds after which a call that is not
                                          						answered is redirected to the next number in the hunt-group list. |

| number | Extension or E.164 number assigned to a phone in Cisco Unified CME. List must
                                          						contain 2 to 32 numbers. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco
                                          						CME 3.4 | This
                                          						command was introduced. |
| 12.4(15)XZ | Cisco
                                          						Unified CME 4.3 | The
                                          						maximum numbers allowed in a list was expanded from 10 to 32 and support for
                                          						SCCP phones was added. |
| 12.4(20)T | Cisco
                                          						Unified CME 7.0 | This
                                          						command was integrated into Cisco IOS Release 12.4(20)T. |
| 15.4(3)M | Cisco Unified CME 10.5 | This command was modified to include support for wildcards
                                          						which is indicated by " * " . symbol. |

| Command | Description |
|---|---|
| final (voice hunt-group) | Defines
                                          						the last extension in a voice hunt group. |
| hops (voice hunt-group) | Defines
                                          						the number of times that a call is redirected to the next phone number in a
                                          						peer hunt-group list before proceeding to the final number. |
| number (ephone-dn) | Associates an extension or telephone number with a directory number. |
| number (voice register dn) | Associates an extension or telephone number with a directory number. |
| pilot (voice hunt-group) | Defines the phone number that callers dial to reach a voice hunt group. |
| timeout (voice hunt-group) | Sets
                                          						the number of seconds after which a call that is not answered is redirected to
                                          						the next number in the hunt-group list and defines the last number in the hunt
                                          						group. |

| phone-number | Telephone number that is dialed when the LiveRcd soft key
                                          						is pressed. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| ephone-template (ephone) | Applies an ephone template to an ephone. |
| softkeys connected | Modifies the order and type of soft keys that display on an
                                          						IP phone during the connected call state. |
| voicemail | Defines the telephone number that is speed-dialed when the
                                          						Messages button is pressed on an IP phone. |

| phone-type | Type of phone. The following phone types are predefined in
                                          						the system: 6945 —Cisco Unified IP Phone
                                             						  6945. 7902 —Cisco Unified IP Phone
                                             						  7902G. 7905 —Cisco Unified IP Phone
                                             						  7905G. 7910 —Cisco Unified IP Phone
                                             						  7910 and 7910G. 7911 —Cisco Unified IP Phone
                                             						  7911G. 7912 —Cisco Unified IP Phone
                                             						  7912G. 7914 —Cisco Unified IP Phone
                                             						  7914 Expansion Module. 7920 —Cisco Unified Wireless IP
                                             						  Phone 7920. 7921 —Cisco Unified Wireless IP
                                             						  Phone 7921. 7931 —Cisco Unified IP Phone
                                             						  7931G. 7935 —Cisco Unified IP
                                             						  Conference Station 7935. 7936 —Cisco Unified IP
                                             						  Conference Station 7936. 7941 —Cisco Unified IP Phone
                                             						  7941G. 7941GE —Cisco Unified IP Phone
                                             						  7941G-GE. 7942 —Cisco Unified IP Phone
                                             						  7942. 7945 —Cisco Unified IP Phone
                                             						  7945 7960-7940 —Cisco Unified IP
                                             						  Phones 7960 and 7960G and Cisco Unified IP Phone 7940 and 7940G. 7961 —Cisco Unified IP Phone
                                             						  7961G. 7961GE —Cisco Unified IP Phone
                                             						  7961G-GE. 7962 —Cisco Unified IP Phone
                                             						  7962. 7965 —Cisco Unified IP Phone
                                             						  7965. 7970 —Cisco Unified IP Phone
                                             						  7970G. 7971 —Cisco Unified IP Phone
                                             						  7971G-GE. 7975 —Cisco Unified IP Phone
                                             						  7975. 7985 —Cisco Unified IP Phone
                                             						  7985. 8941 —Cisco Unified IP Phone
                                             						  8941. 8945 —Cisco Unified IP Phone
                                             						  8945. ata —Cisco ATA-186 and Cisco
                                             						  ATA-188. Note You can also add a new phone type to your configuration
                                                   						by using the ephone-type command. | Note | You can also add a new phone type to your configuration
                                                   						by using the ephone-type command. |
|---|---|---|---|
| Note | You can also add a new phone type to your configuration
                                                   						by using the ephone-type command. |
| firmware-file | Filename of the IP phone firmware for a particular phone
                                          						type. In Cisco Unified CME 7.0/4.3 and earlier versions, do
                                             						  not use the file suffix (.bin, .sbin, .loads) for any phone type except the
                                             						  Cisco ATA and Cisco Unified IP Phone 7905 and 7912. In Cisco Unified CME 7.0(1) and later versions, you must
                                             						  use the complete filename, including the file suffix, for phone firmware
                                             						  versions later than version 8-2-2 for all phone types. Filenames are case sensitive. |

| Note | You can also add a new phone type to your configuration
                                                   						by using the ephone-type command. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco ITS 1.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |
| 12.2(11)YT | Cisco ITS 2.1 | Support was added for the Cisco IP Phone 7914 Expansion
                                          						Module. |
| 12.2(15)T | Cisco ITS 2.1 | This command was integrated into Cisco IOS Release
                                          						12.2(15)T. |
| 12.2(15)ZJ | Cisco CME 3.0 | The following keywords were added to this command: 7902 , 7905 , and 7912 . |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.3(7)T | Cisco CME 3.1 | The 7920 and 7936 keywords were added. |
| 12.3(11)XL | Cisco CME 3.2.1 | The 7970 keyword was added. |
| 12.3(14)T | Cisco CME 3.3 | The 7971 keyword was added, and this
                                          						command was integrated into Cisco IOS Release 12.3(14)T. |
| 12.4(4)XC | Cisco Unified CME 4.0 | The 7911 , 7941 , 7941GE , 7961 , and 7961GE keywords were added. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |
| 12.4(6)XE | Cisco Unified CME 4.0(2) | The 7931 keyword was added. |
| 12.4(4)XC4 | Cisco Unified CME 4.0(3) | The 7931 keyword was added. |
| 12.4(11)T | Cisco Unified CME 4.0(3) | This command was integrated into Cisco IOS Release
                                          						12.4(11)T. |
| 12.4(11)XJ2 | Cisco Unified CME 4.1 | The 7921 and 7985 keywords were introduced. |
| 12.4(15)T | Cisco Unified CME 4.1 | This command was integrated into Cisco IOS Release
                                          						12.4(15)T. |
| 12.4(15)T1 | Cisco Unified CME 4.1(1) | The 7942 , 7945 , 7962 , 7965 , and 7975 keywords were introduced. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | Support for user-defined phone types created with the ephone-type command was added. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |
| 12.4(20)YA | Cisco Unified CME 7.0(1) | Support for automatically creating bindings for firmware
                                          						files only if the cnf-file location is flash or slot0 was added. |
| 12.4(20)T1 | Cisco Unified CME 7.0 | The 7925 keyword was introduced. |
| 12.4(22)T | Cisco Unified CME 7.0(1) | This command was integrated into Cisco IOS Release
                                          						12.4(22)T. |
| 15.2(1)T | Cisco Unified CME 8.8 | This command was modified. The 6945 , 8941 , and 8945 keywords were added. |

| Command | Description |
|---|---|
| cnf-file location | Specifies a storage location for phone configuration files. |
| ephone-type | Adds a Cisco Unified IP phone type by defining a phone-type
                                          						template. |
| reset | Resets a Cisco Unified IP phone. |
| show telephony-service tftp-bindings | Provides a list of configuration files that are accessible
                                          						to IP phones using TFTP. |
| tftp-server | Enables TFTP access to firmware files on the TFTP server. |

| phone-type | Type of
                                          						IP phone. The following choices are valid: 3905 —Cisco Unified IP Phone 3905. 3951 —Cisco Unified IP Phone 3911 and 3951. 6901 —Cisco Unified IP Phone 6901. 6911 —Cisco Unified IP Phone 6911. 6921 —Cisco Unified IP Phone 6921. 6941 —Cisco Unified IP Phone 6941. 6945 —Cisco Unified IP Phone 6945. 6961 —Cisco Unified IP Phone 6961. 7821 —Cisco
                                             						  Unified IP Phone 7821. 7841 —Cisco
                                             						  Unified IP Phone 7841. 7861 —Cisco
                                             						  Unified IP Phone 7861. 7905 —Cisco Unified IP Phone 7905 and 7905G. 7906 —Cisco Unified IP Phone 7906G. 7911 —Cisco
                                             						  Unified IP Phone 7911G. 7912 —Cisco
                                             						  Unified IP Phone 7912 and 7912G. 7941 —Cisco
                                             						  Unified IP Phone 7941G. 7941GE —Cisco
                                             						  Unified IP Phone 7941GE. 7942 —Cisco
                                             						  Unified IP Phone 7942. 7945 —Cisco
                                             						  Unified IP Phone 7945. 7960–7940 —Cisco Unified IP Phones 7940 and 7940G
                                             						  and Cisco IP Phones 7960 and 7960G. 7961 —Cisco
                                             						  Unified IP Phone 7961G. 7961GE —Cisco
                                             						  Unified IP Phone 7961GE. 7962 —Cisco
                                             						  Unified IP Phone 7962. 7965 —Cisco
                                             						  Unified IP Phone 7965. 7970 —Cisco
                                             						  Unified IP Phone 7970G. 7971 —Cisco
                                             						  Unified IP Phone 7971GE. 7975 —Cisco
                                             						  Unified IP Phone 7975. ATA —Cisco
                                             						  ATA-186 and Cisco ATA-188. ATA-187 —Cisco
                                             						  ATA-187. DX650 —Cisco
                                             						  DX650. |
|---|---|
| firmware-file | Filename for the Cisco Unified IP phone firmware to be associated with the IP
                                          						phone type. Do not use the .bin or .load file extension, except for the Cisco
                                          						Unified IP phone 7905, 7912, or ATA. Filenames are case sensitive. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco
                                          						CME 3.4 | This
                                          						command was introduced. |
| 12.4(11)XJ | Cisco
                                          						Unified CME 4.1 | The 3951 , 7911 , 7941 , 7941GE , 7961 , 7961GE , 7970, and 7971 keywords were added. |
| 12.4(15)T | Cisco
                                          						Unified CME 4.1 | The 3951 , 7911 , 7941 , 7941GE , 7961 , 7961GE , 7970 , and 7971 keywords were integrated into Cisco IOS Software Release 12.4(15)T. |
| 12.4(15)XZ | Cisco
                                          						Unified CME 4.3 | The 7942 , 7945 , 7962 , 7965 , and 7975 keywords were added. |
| 12.4(20)T | Cisco
                                          						Unified CME 7.0 | This
                                          						command was integrated into Cisco IOS Release 12.4(20)T. |
| 15.2(1)T | Cisco
                                          						Unified CME 8.8 | This
                                          						command was modified. The 3905 keyword was added. |
| 15.2(2)T | Cisco
                                          						Unified CME 9.0 | This
                                          						command was modified. The 6901 , 6911 , 6921 , 6941 , 6945 , 6961 , and ATA-187 keywords were added. |
| 15.4(3)M | Cisco
                                          						Unified CME 10.5 | This
                                          						command was modified to provide support for Cisco Unified 7821, 7841, 7861 and
                                          						DX650 IP phones. |

| Command | Description |
|---|---|
| reset (voice register global) | Performs a complete reboot of all SIP phones associated with a Cisco Unified
                                          						CME router. |
| show voice register global | Displays all global configuration parameters associated with SIP phones. |
| tftp-server | Enables TFTP access to firmware files on the TFTP server. |
| type (voice register pool) | Defines a phone type for a SIP phone. |

| file-url | Complete path of a configuration file in a local directory. |
|---|---|
| alias file-alias | Name of the file on the TFTP server. |
| sign | Signs the file and serves it on the TFTP server. |
| create | Creates the signed file in the local directory. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| audio-url | Location of the announcement audio file in URL format.
                                          						Valid storage locations are TFTP, FTP, HTTP, and flash memory. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| bnea | Specifies the audio file used for the busy station not
                                          						equipped for preemption announcement. |
| upa | Specifies the audio file used for the unauthorized
                                          						precedence announcement. |
| vca | Specifies the audio file used for the vacant code
                                          						announcement. |
| mlpp indication | Enables MLPP indication on an SCCP phone or analog FXS
                                          						port. |
| mlpp preemption | Enables preemption capability on an SCCP phone or analog
                                          						FXS port. |

| location-tag | Identifier for the emergency response zone location. |
|---|---|
| priority 1-100 | Identifier (1-100) for the priority ranking of locations, 1
                                          						being the highest priority. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XY | Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1) | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| emergency response callback | Defines a dial peer that is used for 911 callbacks from the
                                          						PSAP. |
| emergency response location | Associates an ERL to either a SIP phone, ephone, or dial
                                          						peer. |
| voice emergency response location | Creates a tag for identifying an ERL for the enhanced 911
                                          						service. |
| voice emergency response zone | Creates an emergency response zone within which ERLs can be
                                          						grouped. |

| password-string | Character string that is a password for XML API queries.
                                          						Maximum length is 28 characters. Longer strings are truncated. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was replaced by the xml user command. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was replaced by the xml user command. |
| Cisco IOS XE Gibraltar 16.11.1a Release | Unified CME 12.6 | The command is deprecated. It is not supported on Unified CME 12.6 and later releases. |

| max-size entries | Number of entries in the log table. Range is from 0 to
                                          						1000. Default is 150. |
|---|---|
| retain-timer minutes | Number of minutes to retain entries in the log table. Range
                                          						is from 2 to 500. Default is 15. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| show fb-its-log | Displays information about the Cisco CME XML API
                                          						configuration, statistics on XML API queries, and event logs. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XY | Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1) | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| callback | Default phone number to contact if a 911 callback cannot
                                          						find the last 911 caller from the ERL. |
| elin | E.164 number used as the default ELIN if no matching ERL to
                                          						the 911 caller’s IP phone address is found. |
| expiry | Number of minutes a 911 call is associated with an ELIN in
                                          						case of a callback from the 911 operator. |
| voice emergency response settings | Creates a tag for identifying settings for E911 behavior. |

| timeout | (Optional) Period of phone idleness after which user login
                                          						is deactivated. |
|---|---|
| minutes | (Optional) Number of minutes for which an IP phone can be
                                          						idle before the user is logged out automatically. Range: 1 to 1440. Default:
                                          						60. |
| clear time | (Optional) Time of day after which user login for all IP
                                          						phones is deactivated. Range: 00:00 to 24:00 on a 24-hour clock. Default: 24:00
                                          						(midnight). |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(11)XJ2 | Cisco Unified CME 4.1 | Minimum value for the minutes argument was lowered from 5 minutes to 1 minute. |
| 12.4(15)T | Cisco Unified CME 4.1 | This command with the modifications was integrated into
                                          						Cisco IOS Release 12.4(15)T. |

| Command | Description |
|---|---|
| after-hour exempt | Specifies that an IP phone does not have any of its
                                          						outgoing calls blocked even though call blocking has been defined. |
| after-hours block pattern | Defines a pattern of digits for blocking outgoing calls
                                          						from IP phones. |
| after-hours date | Defines a recurring period based on date during which
                                          						outgoing calls that match defined block patterns are blocked on IP phones. |
| after-hours day | Defines a recurring period based on day of the week during
                                          						which outgoing calls that match defined block patterns are blocked on IP
                                          						phones. |
| pin | Sets a global/individual PIN for phone users to deactivate
                                          						call blocking during call blocking periods. |
| restart (telephony-service) | Performs a fast reboot of one or all phones associated with
                                          						a Cisco Unified CME router. |
| show ephone login | Displays the login states of all phones. |

| url | URL as defined in RFC 2396. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

| Command | Description |
|---|---|
| reset (voice register pool) | Performs a complete reboot of one phone associated with a
                                          						Cisco CME router. |
| reset (voice register global) | Performs a complete reboot of one or all phones associated
                                          						with a Cisco CME router. |

| profile-tag | Unique identifier for a default logout profile to be
                                          						applied. Previously created by using the voice logout-profile command in voice
                                          						logout-profile configuration mode. Range: 1 to maximum number of phones
                                          						supported by platform. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XW | Cisco Unified CME 4.2 | This command was introduced. |
| 12.4(15)XY | Cisco Unified CME 4.2(1) | This command was introduced. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command is integrated into Cisco IOS Release
                                          						12.4(20)T. |
| 15.1(4)M | Cisco Unified CME 8.6 | This command was introduced. |

| Command | Description |
|---|---|
| reset (voice logout-profile and voice user-profile) | Performs a complete reboot of all IP phones to which a
                                          						particular logout-profile or user-profile is downloaded. |
| voice logout-profile | Enters voice profile configuration mode to configure a
                                          						default logout profile for extension mobility. |

| dn-tag | Unique sequence number that identifies the ephone-dn that
                                          						is being paired for loopback with the ephone-dn that is currently being
                                          						configured. The paired ephone-dn must be one that is already defined in the
                                          						system. |
|---|---|
| forward number-of-digits | (Optional) Number of digits in the original called number
                                          						to forward to the other ephone-dn in the loopback-dn pair. Range is from 1 to
                                          						32 digits. Default is to forward all digits. |
| strip number-of-digits | (Optional) Number of leading digits to be stripped from the
                                          						original called number before forwarding to the other ephone-dn in the
                                          						loopback-dn pair. Range is from 1 to 32 digits. Default is not to A-law strip
                                          						any digits. |
| prefix prefix-digit-string | (Optional) Defines a string of digits to add in front of
                                          						the forwarded called number. Maximum number of digits in the string is 32.
                                          						Default is that no prefix is defined. |
| suffix suffix-digit-string | (Optional) Defines a string of digits to add to the end of
                                          						the forwarded called number. Maximum number of digits in the string is 32.
                                          						Default is that no suffix is defined. If you add a suffix that starts with the
                                          						pound character (#), the string must be enclosed in quotation marks. |
| retry seconds | (Optional) Number of seconds to wait before retrying the
                                          						loopback target when it is busy or unavailable. Range is from 0 to 32767.
                                          						Default is that retry is disabled and appropriate call-progress tones are
                                          						passed to the call originator. |
| auto-con | (Optional) Immediately connects the call and provides
                                          						in-band alerting while waiting for the far-end destination to answer. Default
                                          						is that automatic connection is disabled. |
| codec | (Optional) Explicitly forces the G.711 A-law or G.711
                                          						mu-law voice coding type to be used for calls that pass through the
                                          						loopback-dn. This overrides the G.711 coding type that is negotiated for the
                                          						call and provides mu-law to A-law conversion if needed. Default is that
                                          						Real-Time Transport Protocol (RTP) voice packets are passed through the
                                          						loopback-dn without considering the G.711 coding type negotiated for the calls. |
| g711alaw | G.711 A-law, 64000 bits per second, for T1. |
| g711ulaw | G.711 mu-law, 64000 bits per second, for E1. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco ITS 2.0 | This command was introduced. |
| 12.2(2)XT3 | Cisco ITS 2.0 | The suffix keyword was added. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and the auto-con keyword was added. |
| 12.2(11)T | Cisco ITS 2.01 | The suffix keyword was
                                          						added . |
| 12.2(11)YT | Cisco ITS 2.1 | The strip keyword was added. |
| 12.2(11)YT2 | Cisco ITS 2.1 | The codec keyword was added. |
| 12.2(15)T | Cisco ITS 2.1 | This command was integrated into Cisco IOS Release
                                          						12.2(15)T. |

| Note | Use of loopback-dn configurations within a VoIP network should be
                                       		  restricted to resolving critical network interoperability service problems that
                                       		  cannot otherwise be solved. Loopback-dn configurations are intended to be used
                                       		  in VoIP network interworking situations in which the only other alternative
                                       		  would be to make use of back-to-back-connected physical voice ports.
                                       		  Loopback-dn configurations emulate the effect of a back-to-back physical
                                       		  voice-port arrangement without the expense of the physical voice-port hardware.
                                       		  A disadvantage of loopback-dn configurations is that, because digital signal
                                       		  processors (DSPs) are not involved in a loopback-dn arrangement, the
                                       		  configuration does not support interworking or transcoding between calls that
                                       		  use different voice codecs. In many cases, the use of back-to-back physical
                                       		  voice ports that do use DSPs to resolve VoIP network interworking issues is
                                       		  preferred, because it introduces fewer restrictions in terms of supported
                                       		  codecs and call flows. Also, loopback-dns do not support T.38 fax relay. |
|---|---|

| Note | We recommend that you create the basic ephone-dn configuration for
                                       		  both ephone-dn entries before configuring the loopback-dn option under each
                                       		  ephone-dn. The loopback-dn mechanism should be used only in situations where
                                       		  the voice call parameters for the calls on either side of the loopback-dn use
                                       		  compatible configurations; for example, compatible voice codec and dual tone
                                       		  multifrequency (DTMF) relay parameters. Loopback-dn configurations should be
                                       		  used only for G.711 voice calls. |
|---|---|

| Note | The Cisco IOS command-line interface (CLI) requires that arguments
                                       		  with character strings that start with the pound-sign (#) character be enclosed
                                       		  within quotation marks; for example, “#”. |
|---|---|

| Command | Description |
|---|---|
| ephone-dn | Enters ephone-dn configuration mode. |
| show ephone-dn loopback | Displays information about loopback ephone-dns that have
                                          						been created in a Cisco CME system. |

| lpcor-group | Name of the LPCOR resource group. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Note | This command is not supported for phones configured with the lpcor type mobility command. |
|---|---|

| Command | Description |
|---|---|
| lpcor outgoing | Associates an outgoing call with a LPCOR resource-group
                                          						policy. |
| lpcor type | Specifies the LPCOR type for an IP phone. |
| voice lpcor ip-trunk subnet incoming | Creates a LPCOR IP-trunk subnet table for incoming calls
                                          						from a VoIP trunk. |
| voice lpcor policy | Creates a LPCOR policy for a resource group. |

| lpcor-group | Name of the LPCOR resource group. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Note | This command is not supported for phones configured with the lpcor type mobility command. |
|---|---|

| Command | Description |
|---|---|
| lpcor incoming | Associates an incoming call with a LPCOR resource-group
                                          						policy. |
| lpcor type | Specifies the LPCOR type for an IP phone. |
| port (dial-peer) | Associates a dial peer with a voice port. |
| trunkgroup | Associates a dial peer with a trunk group. |
| voice lpcor policy | Creates a LPCOR policy for a resource group. |

| local | IP phone always registers to Cisco Unified CME through the
                                          						LAN. |
|---|---|
| mobile | IP phone can register to Cisco Unified CME through the LAN
                                          						or WAN. |
| remote | IP phone always registers to Cisco Unified CME through the
                                          						WAN. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| lpcor incoming | Associates a LPCOR resource-group policy with an incoming
                                          						call. |
| lpcor outgoing | Associates a LPCOR resource-group policy with an outgoing
                                          						call. |
| voice lpcor policy | Creates a LPCOR policy for a resource group. |