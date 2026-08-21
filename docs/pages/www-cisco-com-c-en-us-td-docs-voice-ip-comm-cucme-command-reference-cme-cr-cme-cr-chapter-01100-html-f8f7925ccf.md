---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-command-reference-cme-cr-cme-cr-chapter-01100-html-f8f7925ccf
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/command/reference/cme_cr/cme_cr_chapter_01100.html
retrieved_at: 2026-08-21T22:56:38.689691+00:00
---

Cisco Unified Communications Manager Express Command Reference

# Cisco Unified Communications Manager Express Command Reference

Updated: July 19, 2018

Chapter: Cisco Unified CME Commands: N

## Chapter: Cisco Unified CME Commands: N

# Cisco Unified CME Commands: N

## name (ephone-dn)

To associate a name with a directory number in Cisco Unified CME, use
                              		  the name command in ephone-dn configuration mode.
                              		  To disassociate a name from an extension, use the no form of this command.

name name

no name

### Syntax Description

name

Alphanumeric string of person or group associated with a
                                          						directory number. Name must follow the order specified in the directory (telephony-service) command, either first-name-first or last-name-first . The two parts,
                                          						first and last name or last and first name, of this argument must be separated
                                          						with a space.

### Command Default

This command has no default behavior or values.

### Command Modes

Ephone-dn configuration (config-ephone-dn)

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

### Usage Guidelines

The name argument is used to provide caller ID for calls originating
                              		  from a directory number in Cisco Unified CME and also generates local directory
                              		  information that is accessed by using the Directories button on a Cisco IP
                              		  phone.

The name argument combination must match the
                              		  order specified in the directory (telephony-service) command, either first-name-first or last-name-first .

The name string must contain a space between the
                              		  first and second parts of the string (first last or last first).

The name string cannot contain special characters
                              		  such as an ampersand (&). The only special characters supported in the name
                              		  string are the comma (,) and the percent sign (%).

To display a comma between the last and first names when the pattern
                              		  is last-name-first, add a comma (,) to the end of the first part of the name string (last name), for example: last,
                              		  first.

The second part of the name string can contain spaces, such as “and
                              		  Handling.”

## Examples

The following example configures the username John Smith with the
                              		  pattern first-name-first :

```
Router(config)# ephone-dn 1 Router(config-ephone-dn) name John Smith
```

The following example configures the username Shipping and Handling
                              		  with the pattern first-name-first :

```
Router(config)# ephone-dn 1 Router(config-ephone-dn) name Shipping and Handling
```

The following example configures the username Jane Smith with the
                              		  pattern last-name-first and with a comma:

```
Router(config)# ephone-dn 1 Router(config-ephone-dn) name Smith, Jane
```

### Related Commands

Command

Description

directory (telephony-service)

Defines the name order for the local directory of Cisco IP
                                          						phone users.

## name (ephone-hunt)

To associate a name with a called voice hunt group, use the name command in ephone-hunt configuration
                              		  mode. To dissociate the name of the called voice hunt group, use the no form of this command.

name “primary pilot
                                 				  name“ [secondary “secondary "secondary pilot
                                 				  name” ]

no name “primary pilot
                                 				  name“ [secondary “secondary "secondary pilot
                                 				  name” ]

### Syntax Description

“primary pilot name”

Name of primary pilot number.

secondary “secondary pilot nam e”

(Optional) Name of secondary pilot number.

### Command Default

No name is associated with the called voice hunt group.

### Command Modes

Ephone-hunt configuration (config-ephone-hunt)

## Command History

Release

Modification

15.3(2)T

This command was introduced.

### Usage Guidelines

In Cisco Unified CME 9.5 and Cisco Unified SRST 9.5, when the
                              		  secondary pilot name is not explicitly configured, the primary pilot name is
                              		  applicable to both pilot numbers.

## Examples

The following example configures the primary pilot name for both the
                              		  primary and the secondary pilot numbers:

```
name SALES
```

The following example configures different names for the primary and
                              		  secondary pilot numbers:

```
name SALES secondary SALES-SECONDARY
```

The following example associates a two-word name for the primary
                              		  pilot number and a one-word name for the secondary pilot number:

```
name “CUSTOMER SERVICE” secondary CS
```

The following example associates a one-word name for the primary
                              		  pilot number and a two-word name for the secondary pilot number:

```
name FINANCE secondary “INTERNAL ACCOUNTING”
```

The following example associates two-word names for the primary pilot
                              		  number and the secondary pilot number:

```
name “INTERNAL CALLER” secondary “EXTERNAL CALLER”
```

When incoming call A reaches voice hunt group B and lands on final C,
                              		  extension C does not show the name of the forwarder because the voice hunt
                              		  group is not configured to display the name. To display the name of the
                              		  forwarder and the final number, two separate names are required for the primary
                              		  and secondary pilot numbers.

The following is a sample output of the show run command when the primary and secondary pilot
                              		  names are configured in ephone-hunt configuration mode:

```
ephone-hunt 10 sequential
 pilot 1010 secondary 1020
 list 2004, 2005
 final 2006
 timeout 8, 8 name "EHUNT PRIMARY" secondary "EHUNT SECONDARY" ephone-hunt 11 peer
 pilot 1012 secondary 1022
 list 2004, 2005
 final 2006
 timeout 8, 8 name EHUNT1 secondary EHUNT1-SEC
```

The following is a sample output of the show ephone-hunt command when the primary and secondary pilot names are
                              		  configured in ephone-hunt configuration mode:

```
show ephone-hunt 10
Group 10
    type: sequential
    pilot number: 1010, peer-tag 20010 pilot name: EHUNT PRIMARY secondary number: 1020, peer-tag 20011
```

secondary name: EHUNT SECONDARY

### Related Commands

Command

Description

voice hunt-group

Enters voice hunt-group configuration mode and creates a
                                          						hunt group for phones in a Cisco Unified CME system.

show voice hunt-group

Displays configuration information associated with one or
                                          						all voice hunt groups in a Cisco Unified CME system.

## name (voice emergency response location)

To describe or identify an emergency response location, use the name command in voice emergency response
                              		  location mode. To remove this definition, use the no form of this command.

name string

no name

### Syntax Description

string

String (30 characters) used to describe or identify an
                                          						ERL’s location.

### Command Default

The location is not described.

### Command Modes

Voice emergency response location configuration (cfg-emrgncy-resp-location)

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

Use this command to enable a word or description of the ERL for
                              		  administrative purposes. The most common use of this command is to identify the
                              		  location for the network administrator.

## Examples

In this example, the location description is Your Company
                              		  Incorporated.

```
voice emergency response location 60
subnet 1 209.165.200.224 255.255.0.0
elin 1 4085550101
name Your Company Incorporated,
```

### Related Commands

Command

Description

address

Specifies a comma separated text entry (up to 247
                                          						characters) of an ERL’s civic address.

elin

Specifies a PSTN number to replace the caller’s extension.

subnet

Defines which IP phones are part of this ERL.

voice emergency response location

Creates a tag for identifying an ERL for E911 services.

## name (voice hunt-group)

To associate a name with a called voice hunt group, use the name command in voice hunt-group
                              		  configuration mode. To dissociate the name of the called voice hunt group, use
                              		  the no form of this command.

name “primary pilot
                                 				  name“ [secondary “secondary pilot
                                 				  name” ]

no name “primary pilot
                                 				  name“ [secondary “secondary pilot
                                 				  name” ]

### Syntax Description

“primary pilot name”

Name of primary pilot number.

secondary “secondary pilot name”

(Optional) Name of secondary pilot number.

### Command Default

No name is associated with the called voice hunt group.

### Command Modes

Voice hunt-group configuration (config-voice-hunt-group)

## Command History

Release

Modification

15.3(2)T

This command was introduced.

### Usage Guidelines

In Cisco Unified CME 9.5 and Cisco Unified SRST 9.5, when the
                              		  secondary pilot name is not explicitly configured, the primary pilot name is
                              		  applicable to both pilot numbers.

## Examples

The following example configures the primary pilot name for both the
                              		  primary and the secondary pilot numbers:

```
name SALES
```

The following example configures different names for the primary and
                              		  secondary pilot numbers:

```
name SALES secondary SALES-SECONDARY
```

The following example associates a two-word name for the primary
                              		  pilot number and a one-word name for the secondary pilot number:

```
name “CUSTOMER SERVICE” secondary CS
```

The following example associates a one-word name for the primary
                              		  pilot number and a two-word name for the secondary pilot number:

```
name FINANCE secondary “INTERNAL ACCOUNTING”
```

The following example associates two-word names for the primary and
                              		  secondary pilot numbers:

```
name “INTERNAL CALLER” secondary “EXTERNAL CALLER”
```

When incoming call A reaches voice hunt group B and lands on final C,
                              		  extension C does not show the name of the forwarder because the voice hunt
                              		  group is not configured to display the name. To display the name of the
                              		  forwarder and the final number, two separate names are required for the primary
                              		  and secondary pilots.

The following example shows how the primary and secondary pilot names
                              		  are configured in voice hunt-group configuration mode:

```
voice hunt-group 24 parallel
   final 097
   list 885,886,124,154
   timeout 20 
   pilot 021 secondary 621 name SALES secondary SALES-SECONDARY
```

The following is a sample output of the show voice hunt-group command when the primary and secondary pilot names are
                              		  configured in voice hunt-group configuration mode:

```
show voice hunt-group 1
Group 1
    type: parallel
    pilot number: 1000, peer-tag 2147483647
    secondary number: 2000, peer-tag 2147483646 pilot name: SALES secondary name: SALES-SECONDARY list of numbers: 2004,2005
```

### Related Commands

Command

Description

voice hunt-group

Enters voice hunt-group configuration mode and creates a
                                          						hunt group for phones in a Cisco Unified CME system.

show voice hunt-group

Displays configuration information associated with one or
                                          						all voice hunt groups in a Cisco Unified CME system.

## name (voice register dn)

To associate a name with a directory number in Cisco Unified CME, use
                              		  the name command in voice register dn
                              		  configuration mode. To disassociate a name from an extension, use the no form of this command.

name name

no name

### Syntax Description

name

Name of the person associated with a given extension. Name
                                          						must follow the order specified in the directory (telephony-service)
                                          						command, either first-name-first or last-name-first .

### Command Default

This command has no default behavior or values.

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

The name argument is used to provide caller ID for calls originating
                              		  from a Cisco CME extension.

This command also generates directory information for the local
                              		  directory that is accessed from the Directories button on a Cisco IP phone.

## Examples

The following example shows how to configure the username John Smith
                              		  with the pattern first-name-first :

```
Router(config)# voice register dn 1 Router(config-register-dn) name John Smith
```

The following example shows how to configure the username Jane Smith
                              		  with the pattern last-name-first :

```
Router(config)# voice register dn 1 Router(config-register-dn) name Smith, Jane
```

### Related Commands

Description

directory (telephony-service)

Defines the name order for the local directory of Cisco IP
                                          						phone users.

## network-locale (ephone-template)

To specify a network locale in an ephone template, use the network-locale command in ephone-template
                              		  configuration mode. To reset to the default network locale, use the no form of this command.

network-locale network-locale-tag

no network-locale

### Syntax Description

network-locale-tag

Locale identifier that was assigned to a network locale
                                          						using the network-locale (telephony-service) command.

### Command Default

The default network locale (network locale 0) is used.

### Command Modes

Ephone-template configuration (config-ephone-template)

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

To apply network locales to individual ephones, you must specify
                              		  per-phone configuration files using the cnf-file perphone command and identify the locales using the network-locale (telephony-service) command.

After creating an ephone template that contains a locale tag, use the ephone-template (ephone) command to apply the template to
                              		  individual ephones.

## Examples

The following example defines three alternative locales: JP (Japan),
                              		  FR (France), and ES (Spain). The default is US for all phones that do not have
                              		  the alternatives applied using ephone templates. In this example, ephone 11
                              		  uses JP for its locales, ephone 12 uses FR, ephone 13 uses ES, and ephone 14
                              		  uses the default, US.

```
telephony-service
 cnf-file location flash:
 cnf-file perphone
 create cnf-files
 user-locale 1 JP
 user-locale 2 FR
 user-locale 3 ES
 network-locale 1 JP
 network-locale 2 FR
 network-locale 3 ES
ephone-template 1
 user-locale 1
 network-locale 1
ephone-template 2
 user-locale 2
 network-locale 2
ephone-template 3
 user-locale 3
 network-locale 3
ephone 11
 button 1:25
 ephone-template 1
ephone 12
 button 1:26
 ephone-template 2
ephone 13
 button 1:27
 ephone-template 3
ephone 14
 button 1:28
```

### Related Commands

Description

cnf-file

Specifies the type of configuration files that phones use.

ephone-template (ephone)

Applies an ephone template to an ephone.

network-locale (telephony-service)

Sets the locale for geographically specific tones and
                                          						cadences.

## network-locale (telephony-service)

To select a code for a geographically specific set of tones and
                              		  cadences on supported phone types, use the network-locale command in telephony-service
                              		  configuration mode. To disable selection of a code, use the no form of this command.

network-locale [ network-locale-tag [ user-defined-code ]] locale-code

no network-locale network-locale-tag

### Syntax Description

network-locale-tag

(Optional) Assigns a locale identifier to the locale code.
                                          						Range is 0 to 4. Default is 0.

user-defined code

(Optional) Assigns one of the user-defined codes to the
                                          						specified locale code. Valid codes are U1 , U2 , U3 , U4 , and U5 . There is no default.

locale-code

Locale files for the following ISO 3166 codes are
                                          						predefined in system storage for supported phone types:

- AT —Austria

- CA —Canada

- CH —Switzerland

- DE —Germany

- DK —Denmark

- ES —Spain

- FR —France

- GB —United Kingdom

- IT —Italy

- JP —Japan

- NL —Netherlands

- NO —Norway

- PT —Portugal

- RU —Russian Federation

- SE —Sweden

- US —United States (default)

### Command Default

The default locale code is US (United States).

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(11)YT

Cisco ITS 2.1

This command was introduced.

12.2(15)T

Cisco ITS 2.1

This command was integrated into Cisco IOS Release
                                          						12.2(15)T.

12.4(4)XC

Cisco Unified CME 4.0

The network-locale-tag and user-defined-code arguments were added.

12.4(9)T

Cisco Unified CME 4.0

The network-locale-tag and user-defined-code arguments were integrated into Cisco IOS Release
                                          						12.4(9)T.

### Usage Guidelines

This command designates a a network locale other than US as the
                              		  locale for one or more phones in Cisco Unified CME.

Network locale 0 always holds the default locale, which is used for
                              		  all phones that are not assigned alternative network locales or user-defined
                              		  network locales. You can use this command to change the default locale.

The show telephony-service tftp-bindings command displays the locale-specific call-progress tone files
                              		  that are accessible to IP phones using TFTP.

This command must be followed by a complete phone reboot using the reset command.

Alternative Network Locales

The network-locale-tag argument allows you to specify up to five
                              		  alternative network locales for use in a system using Cisco Unified CME 4.0 or
                              		  a later release. For example, a company can specify network-locale France for
                              		  phones A, B, and C; network-locale Germany for phones D, E, and F; and
                              		  network-locale United States for phones G, H, and I.

Each one of the five alternative network locales that you can use in
                              		  a multi-locale system is identified with a locale tag identifier. The
                              		  identifier 0 always holds the default locale, although you can define this
                              		  default to be any locale code that is supported in the system and is listed in
                              		  the CLI help for the command. For example, if you define network locale 0 to be
                              		  JP (Japanese), the default network locale for the router is JP. If you do not
                              		  specify a locale for the identifier 0, the default is US (United States).

To apply alternative network locales to different phones, you must
                              		  use the cnf-files command to specify per-phone
                              		  configuration files. When you use per-phone configuration files, a phone's
                              		  configuration file automatically uses the default locales in user locale 0 and
                              		  network locale 0. You can override this default for individual ephones by
                              		  assigning alternative locale tag identifiers to the alternative locale codes
                              		  that you want to use and then creating ephone templates to assign the locale
                              		  tag identifiers to individual ephones. For example, you can give the
                              		  alternative locale tag of 2 to the locale code DK (Denmark).

After using the network-locale (telephony-service) command to associate a locale
                              		  tag identifier with a locale code, use the network-locale command in ephone-template
                              		  mode to apply the locale tag to an ephone template. Then use the ephone-template command in ephone
                              		  configuration mode to apply the template to the ephones that should use the
                              		  alternative network locale.

User-Defined Network Locales

XML files for user locales and network locales that are not currently
                              		  provided in the system must be downloaded to use this feature. Beginning in
                              		  Cisco Unified CME 4.0, you can install the files to support a particular user
                              		  and network locale in flash, slot 0, or an external TFTP server. You cannot
                              		  install these files in the system location. These user-locale and
                              		  network-locale files can then be used as default or alternative locales for all
                              		  or some phones.

For example, if you have a site at which the phones should use the
                              		  displays and tones for Traditional Chinese, which is not one of the predefined
                              		  locales, you must download and install the XML files for Traditional Chinese on
                              		  the phones that need to use this locale.

## Examples

The following example sets the default locale tag 0 to France:

```
telephony-service
 network-locale FR
```

The following example sets the default locale tag 0 to France. It
                              		  shows another way to change the default network locale:

```
telephony-service
 network-locale 0 FR
```

The following example sets the alternative locale tag 1 to Germany:

```
telephony-service
 network-locale 1 DE
```

## Examples

The following example defines three alternative locales: JP (Japan),
                              		  FR (France), and ES (Spain). The default is US for all phones that do not have
                              		  the alternatives applied using ephone templates. In this example, ephone 11
                              		  uses JP for its locales, ephone 12 uses FR, ephone 13 uses ES, and ephone 14
                              		  uses the default, US.

```
telephony-service
 cnf-file location flash:
 cnf-file perphone
 user-locale 1 JP
 user-locale 2 FR
 user-locale 3 ES
 network-locale 1 JP
 network-locale 2 FR
 network-locale 3 ES
 create cnf-files
ephone-template 1
 user-locale 1
 network-locale 1
ephone-template 2
 user-locale 2
 network-locale 2
ephone-template 3
 user-locale 3
 network-locale 3
ephone 11
 button 1:25
 ephone-template 1
ephone 12
 button 1:26
 ephone-template 2
ephone 13
 button 1:27
 ephone-template 3
ephone 14
 button 1:28
```

## Examples

The following example applies the alternative locale tag 4 to the
                              		  user-defined code U1, which is defined as ZH. ZH is the code that represents
                              		  Traditional Chinese in ISO 639, the Language Code Reference. Because the code
                              		  for Traditional Chinese is not one of those is provided in the system, the user
                              		  must download the appropriate XML files to support this language.

In addition to the user-defined code, the example also defines three
                              		  alternative locales: JP (Japan), FR (France), and ES (Spain). The default is US
                              		  for all phones that do not have the alternatives applied using ephone
                              		  templates. In this example, ephone 11 uses JP for its locales; ephone 12 uses
                              		  FR; ephone 13 uses ES; ephone 14 uses the default, US; and ephone 15 uses the
                              		  user-defined language, ZH (Traditional Chinese).

```
telephony-service
 cnf-file location flash:
 cnf-file perphone
 user-locale 1 JP
 user-locale 2 FR
 user-locale 3 ES
 user-locale 4 U1 ZH
 network-locale 1 JP
 network-locale 2 FR
 network-locale 3 ES
 network-locale 4 U1 ZH
 create cnf-files
ephone-template 1
 user-locale 1
 network-locale 1
ephone-template 2
 user-locale 2
 network-locale 2
ephone-template 3
 user-locale 3
 network-locale 3
ephone-template 4
 user-locale 4
 network-locale 4
ephone 11
 button 1:25
 ephone-template 1
ephone 12
 button 1:26
 ephone-template 2
ephone 13
 button 1:27
 ephone-template 3
ephone 14
 button 1:28
ephone 15
 button 1:29
 ephone-template 4
```

### Related Commands

Description

cnf-files

Specifies the type of phone configuration files to be
                                          						created.

ephone-template (ephone)

Applies an ephone template to an ephone.

network-locale (ephone-template)

Applies a locale tag identifier to an ephone template.

reset (ephone)

Performs a complete reboot of one phone associated with a
                                          						Cisco Unified CME router.

reset (telephony-service)

Performs a complete reboot of one or all phones associated
                                          						with a Cisco Unified CME router.

show telephony-service tftp-bindings

Displays the current configuration files that are
                                          						accessible to IP phones.

user-locale (telephony-service)

Sets the language for displays on supported phone types.

## network-locale (voice-gateway)

To select a geographically specific set of tones and cadences for the
                              		  voice gateway’s analog endpoints that register to Cisco Unified CME, use the network-locale command in voice-gateway
                              		  configuration mode. To remove a code, use the no form of this command.

network-locale country-code

no network-locale country-code

### Syntax Description

country-code

The following ISO 3166 country codes are supported:

- AE —United Arab Emirates

- AR —Argentina

- AT —Austria

- AU —Australia

- BE —Belgium

- BR —Brazil

- CA —Canada

- CH —Switzerland

- CN —China

- CO —Colombia

- CY —Cyprus

- CZ —Czech Republic

- DE —Germany

- DK —Denmark

- EG —Egypt

- ES —Spain

- FI —Finland

- FR —France

- GB —United Kingdom

- GH —Ghana

- GR —Greece

- HK —Hong Kong

- HU —Hungary

- ID —Indonesia

- IE —Ireland

- IL —Israel

- IN —India

- IS —Iceland

- IT —Italy

- JO —Jordan

- JP —Japan

- KE —Kenya

- KR —Korea Republic

- KW —Kuwait

- LB —Lebanon

- LU —Luxembourg

- MX —Mexico

- MY —Malaysia

- NG —Nigeria

- NL —Netherlands

- NO —Norway

- NP —Nepal

- NZ —New Zealand

- OM —Oman

- PA —Panama

- PE —Peru

- PH —Philippines

- PK —Pakistan

- PL —Poland

- PT —Portugal

- RU —Russian Federation

- SA —Saudi Arabia

- SE —Sweden

- SG —Singapore

- SI —Slovenia

- SK —Slovakia

- TH —Thailand

- TR —Turkey

- TW —Taiwan

- US —United States (default)

- VE —Venezuela

- ZA —South Africa

- ZW —Zimbabwe

### Command Default

The default locale code is US (United States).

### Command Modes

Voice-gateway configuration (config-voice-gateway)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(22)YB

Cisco Unified CME 7.1

This command was introduced.

12.4(24)T

Cisco Unified CME 7.1

This command was integrated into Cisco IOS Release
                                          						12.4(24)T.

### Usage Guidelines

This command designates a network locale other than US as the locale
                              		  for the analog endpoints registered to Cisco Unified CME. All voice ports are
                              		  assigned the same network locale. If you want a different network locale on a
                              		  specific phone, use the cptone command in voice-port configuration
                              		  mode.

The show telephony-service tftp-bindings command displays the locale-specific call-progress tone files
                              		  that are accessible to IP phones using TFTP.

After using this command, you must reboot the phones with the reset command.

## Examples

The following example shows a voice gateway configuration where the
                              		  network locale is set to France:

```
voice-gateway system  1
 network-locale FR
 type VG224
 mac-address 001F.A30F.8331
 voice-port 0-23
 create cnf-files
```

### Related Commands

Command

Description

cptone

Specifies a regional analog voice-interface-related tone,
                                          						ring, and cadence setting.

reset (voice-gateway)

Performs a complete reboot of all analog phones associated
                                          						with the voice gateway and registered to Cisco Unified CME.

show telephony-service tftp-bindings

Displays the current configuration files accessible to IP
                                          						phones.

voice-port (voice-gateway)

Identifies the ports on the voice gateway that will
                                          						register to Cisco Unified CME.

## night-service bell

To mark an IP phone to receive night-service bell notification when
                              		  incoming calls are received on ephone-dns that are marked for night service
                              		  during night-service time periods, use the night-service bell command in ephone or ephone-template
                              		  configuration mode. To remove night-service notification capability from a
                              		  phone, use the no form of this command.

night-service bell

no night-service bell

### Syntax Description

This command has no arguments or keywords.

### Command Default

A phone is not marked for night-service bell notification.

### Command Modes

Ephone configuration (config-ephone) Ephone-template configuration (config-ephone-template)

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

This command was made available in ephone-template
                                          						configuration mode.

12.4(9)T

Cisco Unified CME 4.0

This command in ephone-template configuration mode was
                                          						integrated into Cisco IOS Release 12.4(9)T.

### Usage Guidelines

When an ephone-dn is marked for night-service treatment using the night-service bell (ephone-dn) command, incoming calls that ring
                              		  during the night-service time period on that ephone-dn send an alert indication
                              		  to all IP phones that are marked to receive night-service bell notification
                              		  with this command. The alert notification is in the form of a splash ring (not
                              		  associated with any of the individual lines on the IP phone) and a visible
                              		  display of the ephone-dn extension number. The phone user retrieves the call by
                              		  pressing a PickUp or GPickUp soft key and dialing the appropriate digits.

Night-service periods are defined using the night-service date and night-service day commands. Night service can be manually
                              		  disabled or reenabled from a phone configured with ephone-dns in night-service
                              		  mode if the n ight-service code command has been set.

If you use an ephone template to apply a command to a phone and you
                              		  also use the same command in ephone configuration mode for the same phone, the
                              		  value that you set in ephone configuration mode has priority.

## Examples

The following example designates the IP phone that is being
                              		  configured as a phone that will receive night-service bell notification when
                              		  ephone-dns marked for night service receive incoming calls during a
                              		  night-service period:

```
Router(config)# ephone 4 Router(config-ephone)# night-service bell
```

### Related Commands

Description

ephone-template (ephone)

Applies a template to an ephone configuration.

night-service bell (ephone-dn)

Marks an ephone-dn to send night-service bell notification
                                          						to designated IP phones during night-service time periods.

night-service code

Defines a code to disable or reenable night service on IP
                                          						phones.

night-service date

Defines a recurring time period associated with a month and
                                          						day during which night service is active.

night-service day

Defines a recurring time period associated with a day of
                                          						the week during which night service is active.

## night-service bell (ephone-dn)

To mark an ephone-dn for night-service treatment, use the night-service bell command in ephone-dn configuration mode. To
                              		  remove the night-service treatment from the ephone-dn, use the no form of this command.

night-service bell

no night-service bell

### Syntax Description

This command has no arguments or keywords.

### Command Default

An ephone-dn is not marked for night service.

### Command Modes

Ephone-dn configuration (config-ephone-dn)

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

When an ephone-dn is marked for night-service treatment using this
                              		  command, incoming calls that ring during the night-service time period on that
                              		  ephone-dn send an alert indication to all IP phones that are marked to receive
                              		  night-service bell notification using the night-service bell (ephone) command. The alert notification is in the form of
                              		  a splash ring (not associated with any of the individual lines on the IP phone)
                              		  and a visible display of the ephone-dn extension number. The phone user
                              		  retrieves the call by pressing a PickUp or GPickUp soft key and dialing the
                              		  appropriate digits.

Night-service periods are defined using the n ight-service date and night-service day commands. Night service can be manually
                              		  disabled or enabled from a phone configured with ephone-dns in night-service
                              		  mode if the night-service code command has been set.

## Examples

The following example marks an ephone-dn as a line that will ring on
                              		  IP phones designated to receive night-service bell notification when incoming
                              		  calls are received on this ephone-dn during night-service periods:

```
Router(config)# ephone-dn 16 Router(config-ephone-dn)# night-service bell
```

### Related Commands

Description

night-service bell (ephone)

Marks an IP phone to receive night-service bell
                                          						notification when incoming calls are received on ephone-dns that are marked for
                                          						night service during night-service time periods.

night-service code

Defines a code to disable or reenable night service on IP
                                          						phones.

night-service date

Defines a recurring time period associated with a month and
                                          						day during which night service is active.

night-service day

Defines a recurring time period associated with a day of
                                          						the week during which night service is active.

## night-service
                        	 code

To define a code
                              		  to disable or reenable night service on IP phones, use the night-service code command in telephony-service configuration
                              		  mode. To remove the code, use the no form of
                              		  this command.

night-service code digit-string

no night-service code digit-string

### Syntax Description

digit-string

Digit
                                          						code that a user enters at an IP phone to disable or reenable night service.
                                          						The code must begin with an asterisk (*). The maximum number of characters is
                                          						16, including the asterisk.

### Command Default

No code is
                              		  defined.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.2(15)ZJ

Cisco
                                          						CME 3.0

This
                                          						command was introduced.

12.3(4)T

Cisco
                                          						CME 3.0

This
                                          						command was integrated into Cisco IOS Release 12.3(4)T.

12.3(14)T

Cisco
                                          						CME 3.3

The
                                          						action of this command was changed so that all night-service ephone-dns are
                                          						activated or deactivated when the code is used rather than just the phone on
                                          						which the code is input.

15.6(3)M

16.3.1

Cisco
                                          						Unified CME 11.5

From
                                          						Unified CME 11.5 onwards, this command can be used to activate or deactivate
                                          						the night service from SIP phones as well.

### Usage Guidelines

Night-service
                              		  periods are defined with the night-service date and night-service day commands. When a dn is marked for
                              		  night-service treatment using the night-service bell (ephone-dn or voice register dn) command,
                              		  incoming calls that ring during the night-service time period on that dn send
                              		  an alert indication to all IP phones that are marked to receive night-service
                              		  bell notification using the night-service bell command. The alert notification is in the form of a burst ring
                              		  for SCCP phones and message waiting tone for SIP phones (not associated with
                              		  any of the individual lines on the IP phone). There is a visible display of the
                              		  dn extension number. The phone user retrieves the call by pressing a PickUp or
                              		  GPickUp soft key and dialing the appropriate digits.

When a
                              		  night-service code has been defined using the night-service code command, night service for all night-service dns can be
                              		  manually activated or deactivated from any phone that is configured with a
                              		  night-service dn.

## Examples

The following
                              		  example defines a night-service code of *2985:

```
Router(config)# telephony-service Router(config-telephony)# night-service code *2985
```

### Related Commands

Description

night-service bell (ephone)

Marks
                                          						an IP phone to receive night-service bell notification when incoming calls are
                                          						received on ephone-dns that are marked for night service during night-service
                                          						time periods.

night-service bell (ephone-dn)

Marks
                                          						an ephone-dn to send night-service bell notification to designated IP phones
                                          						during night-service time periods.

night-service bell (voice register pool)

Marks
                                          						a SIP phone to receive night-service bell notification when incoming calls are
                                          						received on voice register DNs that are marked for night service during
                                          						night-service time periods.

night-service bell (voice register dn)

Marks
                                          						a voice register dn to send night-service bell notification to designated SIP
                                          						phones during night-service time periods.

night-service bell (voice register template)

Applies a template to a pool configuration.

night-service date

Defines a recurring time period associated with a month and day during which
                                          						night service is active.

night-service day

Defines a recurring time period associated with a day of the week during which
                                          						night service is active.

## night-service date

To define a recurring time period associated with a date during which
                              		  night service is active, use the night-service date command in telephony-service configuration
                              		  mode. To delete the defined time period, use the no form of this command.

night-service date month day start-time stop-time

no night-service date month day start-time stop-time

### Syntax Description

month

Abbreviated month. The following abbreviations for month
                                          						are valid: jan , feb , mar , apr , may , jun , jul , aug , sep , oct , nov , dec .

day

Day of the month. Range is from 1 to 31.

start-time stop-time

Beginning and ending times for night service, in an HH:MM
                                          						format using a 24-hour clock. The stop time must be greater than the start
                                          						time. The value 24:00 is not valid. If 00:00 is entered as a stop time, it is
                                          						changed to 23:59. If 00:00 is entered for both start time and stop time, night
                                          						service is in effect for the entire 24-hour period on the specified date.

### Command Default

No time period based on date is defined for night service.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco product

Modification

12.2(15)ZJ

Cisco CME 3.0

This command was introduced.

12.3(4)T

Cisco CME 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

After you define night-service periods using this command and the night-service day command, use the night-service bell (ephone-dn) command to specify the extensions that will ring on other phones and
                              		  the night-service bell (ephone) command to specify the phones on which the extensions
                              		  will ring during the designated night-service periods.

## Examples

The following example defines a night-service time period for the
                              		  entire day of January 1:

```
Router(config)# telephony-service Router(config-telephony)# night-service date jan 1 00:00 00:00
```

### Related Commands

Description

night-service bell (ephone)

Marks an IP phone to receive night-service-bell
                                          						notification when incoming calls are received on ephone-dns that are marked for
                                          						night service during night-service time periods.

night-service bell (ephone-dn)

Marks an ephone-dn to send night-service bell notification
                                          						to designated IP phones during night-service time periods.

night-service code

Defines a code to disable or reenable night service on IP
                                          						phones.

night-service day

Defines a recurring time period associated with a day of
                                          						the week during which night service is active.

## night-service day

To define a recurring time period associated with a day of the week
                              		  during which night service is active, use the night-service day command in telephony-service configuration
                              		  mode. To delete the defined time period, use the no form of this command.

night-service day day start-time stop-time

no night-service day day start-time stop-time

### Syntax Description

day

Day of the week abbreviation. The following are valid day
                                          						abbreviations: sun , mon , tue , wed , thu , fri , sat .

start-time stop-time

Beginning and ending times for night service, in an HH:MM
                                          						format using a 24-hour clock. If the stop time is a smaller value than the
                                          						start time, the stop time occurs on the day following the start time. For
                                          						example, mon 19:00 07:00 means “from Monday at 7 p.m. until Tuesday at 7 a.m.”

The value 24:00 is not valid. If 00:00 is entered as a stop
                                          						time, it is changed to 23:59. If 00:00 is entered for both start time and stop
                                          						time, night service is in effect for the entire 24-hour period on the specified
                                          						day.

### Command Default

No time period based on day of the week is defined for night service.

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

After you define night-service periods using this command and the night-service date command, use the night-service bell (ephone-dn) command to specify the extensions that will ring on other
                              		  phones and the night-service bell (ephone) command to specify the phones on which the extensions will ring
                              		  during the designated night-service periods.

## Examples

The following example defines a night-service time period from Monday
                              		  at 7 p.m. to Tuesday at 9 a.m.:

```
Router(config)# telephony-service Router(config-telephony)# night-service day mon 19:00 09:00
```

### Related Commands

Description

night-service bell (ephone)

Marks an IP phone to receive night-service bell
                                          						notification when incoming calls are received on ephone-dns that are marked for
                                          						night service during night-service time periods.

night-service bell (ephone-dn)

Marks an ephone-dn to send night-service bell notification
                                          						to designated IP phones during night-service time periods.

night-service code

Defines a code to disable or reenable night service on IP
                                          						phones.

night-service date

Defines a recurring time period associated with a month and
                                          						day during which night service is active.

## night-service everyday

To define a recurring time period during which night service is
                              		  active every day, use the night-service everyday command in telephony-service
                              		  configuration mode. To delete the defined time period, use the no form of this command.

night-service everyday start-time stop-time

no night-service everyday

### Syntax Description

start-time stop-time

Beginning and ending times for night service, in an HH:MM
                                          						format using a 24-hour clock. If the stop time is a smaller value than the
                                          						start time, the stop time occurs on the day following the start time. For
                                          						example, mon 19:00 07:00 means “from Monday at 7 p.m. until Tuesday at 7 a.m.”

The value 24:00 is not valid. If 00:00 is entered as a stop
                                          						time, it is changed to 23:59. If 00:00 is entered for both start time and stop
                                          						time, night service is in effect for the entire 24-hour period on the specified
                                          						day.

### Command Default

No recurring night-service time period is defined for every day.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)XC

Cisco Unified CME 4.0

This command was introduced.

## Command History

12.4(9)T

Cisco Unified CME 4.0

This command was integrated into Cisco IOS Release
                                          						12.4(9)T.

### Usage Guidelines

After you define recurring night-service time periods, use the night-service bell (ephone-dn) command to specify the extensions that will ring on other
                              		  phones and the night-service bell (ephone) command to specify the phones on which the extensions will ring
                              		  during the designated night-service periods.

## Examples

The following example defines a night-service time period to be in
                              		  effect every day from 7 p.m. to 8 a.m.:

```
Router(config)# telephony-service Router(config-telephony)# night-service everyday 19:00 08:00
```

### Related Commands

Description

night-service bell (ephone)

Marks an IP phone to receive night-service bell
                                          						notification when incoming calls are received on ephone-dns that are marked for
                                          						night service during night-service time periods.

night-service bell (ephone-dn)

Marks an ephone-dn to send night-service bell notification
                                          						to designated IP phones during night-service time periods.

night-service code

Defines a code to disable or reenable night service on IP
                                          						phones.

night-service date

Defines a recurring time period associated with a month and
                                          						day during which night service is active.

night-service day

Defines a recurring time period associated with a day of
                                          						the week during which night service is active.

night-service weekday

Defines a recurring night-service time period to be in
                                          						effect only on weekdays.

night-service weekend

Defines a recurring night-service time period to be in
                                          						effect only on weekends.

## night-service weekday

To define a recurring night-service time period to be in effect on
                              		  all weekdays, use the night-service weekday command in telephony-service configuration
                              		  mode. To delete the defined time period, use the no form of this command.

night-service weekday start-time stop-time

no night-service weekday

### Syntax Description

start-time stop-time

Beginning and ending times for night service, in an HH:MM
                                          						format using a 24-hour clock. If the stop time is a smaller value than the
                                          						start time, the stop time occurs on the day following the start time. For
                                          						example, mon 19:00 07:00 means “from Monday at 7 p.m. until Tuesday at 7 a.m.”

The value 24:00 is not valid. If 00:00 is entered as a stop
                                          						time, it is changed to 23:59. If 00:00 is entered for both start time and stop
                                          						time, night service is in effect for the entire 24-hour period on the specified
                                          						day.

### Command Default

No recurring night-service time period is defined for weekdays.

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

Weekdays are defined as Monday, Tuesday, Wednesday, Thursday, and
                              		  Friday.

After you define night-service periods, use the night-service bell (ephone-dn) command to specify the extensions that will ring on other
                              		  phones and the night-service bell (ephone) command to specify the phones on which the extensions will ring
                              		  during the designated night-service periods.

## Examples

The following example defines a night-service time period every
                              		  weekday from 5 p.m. to 9 a.m.:

```
Router(config)# telephony-service Router(config-telephony)# night-service weekday 17:00 09:00
```

### Related Commands

Description

night-service bell (ephone)

Marks an IP phone to receive night-service bell
                                          						notification when incoming calls are received on ephone-dns that are marked for
                                          						night service during night-service time periods.

night-service bell (ephone-dn)

Marks an ephone-dn to send night-service bell notification
                                          						to designated IP phones during night-service time periods.

night-service code

Defines a code to disable or reenable night service on IP
                                          						phones.

night-service date

Defines a recurring time period associated with a month and
                                          						day during which night service is active.

night-service day

Defines a recurring time period associated with a day of
                                          						the week during which night service is active.

night-service everyday

Defines a recurring night-service time period to be in
                                          						effect everyday.

night-service weekend

Defines a recurring night-service time period to be in
                                          						effect only on weekends.

## night-service weekend

To define a recurring night-service time period to be active on
                              		  weekends, use the night-service weekend command in telephony-service configuration
                              		  mode. To delete the defined time period, use the no form of this command.

night-service weekend start-time stop-time

no night-service weekend

### Syntax Description

start-time stop-time

Beginning and ending times for night service, in an HH:MM
                                          						format using a 24-hour clock. If the stop time is a smaller value than the
                                          						start time, the stop time occurs on the day following the start time. For
                                          						example, mon 19:00 07:00 means “from Monday at 7 p.m. until Tuesday at 7 a.m.”

The value 24:00 is not valid. If 00:00 is entered as a stop
                                          						time, it is changed to 23:59. If 00:00 is entered for both start time and stop
                                          						time, night service is in effect for the entire 24-hour period on the specified
                                          						day.

### Command Default

No recurring night-service time period is defined for weekends.

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

Weekend is defined as Saturday and Sunday.

After you define night-service periods, use the night-service bell (ephone-dn) command to specify the extensions that will ring on other
                              		  phones and the night-service bell (ephone) command to specify the phones on which the extensions will ring
                              		  during the designated night-service periods.

## Examples

The following example defines a night-service time period for all day
                              		  Saturdays and Sundays:

```
Router(config)# telephony-service Router(config-telephony)# night-service weekend 00:00 00:00
```

### Related Commands

Description

night-service bell (ephone)

Marks an IP phone to receive night-service bell
                                          						notification when incoming calls are received on ephone-dns that are marked for
                                          						night service during night-service time periods.

night-service bell (ephone-dn)

Marks an ephone-dn to send night-service bell notification
                                          						to designated IP phones during night-service time periods.

night-service code

Defines a code to disable or reenable night service on IP
                                          						phones.

night-service date

Defines a recurring time period associated with a month and
                                          						day during which night service is active.

night-service day

Defines a recurring time period associated with a day of
                                          						the week during which night service is active.

night-service everyday

Defines a recurring night-service time period to be in
                                          						effect everyday.

night-service weekday

Defines a recurring night-service time period to be in
                                          						effect only on weekdays.

## no-reg

To specify that the pilot number for a Cisco CallManager Express
                              		  (Cisco CME) peer ephone hunt group not register with an H.323 gatekeeper, use
                              		  the no-reg command in ephone-hunt configuration
                              		  mode. To return to the default of the pilot number registering with an H.323
                              		  gatekeeper, use the no form of this command.

no-reg [ both | pilot ]

no no-reg [ both | pilot ]

### Syntax Description

both

(Optional) Both the primary and secondary pilot numbers are
                                          						not registered.

pilot

(Optional) Only the primary pilot number is not registered.

### Command Default

The pilot number registers with the H.323 gatekeeper.

### Command Modes

Ephone-hunt configuration (config-ephone-hunt)

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

12.3(7)T

Cisco CME 3.1

The both and pilot keywords were introduced.

### Usage Guidelines

This command is valid only for Cisco CME peer ephone hunt groups.

## Examples

The following example defines peer ephone hunt group 2 with a primary
                              		  and secondary pilot number, and specifies that the secondary pilot number
                              		  should not register with the H.323 gatekeeper:

```
Router(config)# ephone-hunt 2 peer Router(config-ephone-hunt)# pilot 2222 secondary 4444 Router(config-ephone-hunt)# no-reg
```

### Related Commands

Description

final

Defines the last ephone-dn in an ephone hunt group.

hops

Defines the number of times that a call is redirected to
                                          						the next ephone-dn in a peer ephone-hunt-group list before proceeding to the
                                          						final ephone-dn.

list

Defines the ephone-dns that participate in an ephone hunt
                                          						group.

max-redirect

Changes the current number of allowable redirects in a
                                          						Cisco CME system.

pilot

Defines the ephone-dn that is dialed to reach an ephone
                                          						hunt group.

preference (ephone-hunt)

Sets preference order for the ephone-dn associated with an
                                          						ephone-hunt-group pilot number.

timeout (ephone-hunt)

Sets the number of seconds after which a call that is not
                                          						answered is redirected to the next number in the hunt-group list.

## no-reg (voice register dn)

To specify that a voice DN for a SIP phone line in a Cisco
                              		  CallManager Express (Cisco CME) system not register with an external proxy
                              		  server, use the no-reg command in voice register dn
                              		  configuration mode. To return to the default, use the no form of this command.

no-reg

no no-reg

### Syntax Description

This command has no arguments or keywords.

### Command Default

This command is disabled.

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

This command specifies that a particular voice DN not register with
                              		  the external proxy server. Configure the no-reg command per line. The default is to
                              		  register all SIP lines in the Cisco CME system.

## Examples

The following example shows how to configure bulk registration for
                              		  registering a block of phone numbers starting with 408555 with an external
                              		  registrar and specify that directory number 1, number 4085550100 not register
                              		  with the external registrar:

```
Router(config)# voice register global Router(voice-register-global)# mode cme Router(voice-register-global)# bulk 408555.... Router(voice-register-global)# exit Router(config)# voice register dn 1 Router(config-register-dn)# number 408550100 Router(config-register-dn)# no-reg
```

### Related Commands

Description

number (voice register dn)

Associates a telephone or extension number with a SIP phone
                                          						in a Cisco CME system.

## nte-end-digit-delay

To specify the amount of time that each digit in the RTP NTE end
                              		  event in an RFC 2833 packet is delayed before being sent, use the nte-end-digit-delay command in ephone or ephone-template configuration mode. To
                              		  remove the delay amount, use the no form of this command.

nte-end-digit-delay [milliseconds]

no nte-end-digit-delay

### Syntax Description

milliseconds

Length of delay. Range: 10 to 200. Default: 200 ms.

### Command Default

All digits in the RTP NTE end event are sent in a single burst.

### Command Modes

Ephone configuration (config-ephone)

Ephone-template configuration (config-ephone-template)

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

If your system is configured for RFC 2833 DTMF interworking and if
                              		  the remote system cannot handle the RTP NTE end event sent in a single burst,
                              		  use this command to delay sending each digit in the RTP NTE end event by the
                              		  specified number of milliseconds. The default value for the delay is 100 ms.

This command only specifies the amount of time that each digit in the
                              		  RTP NTE end event is delayed before being sent. To enable the delay, you must
                              		  also configure the dtmf-interworking rtp-nte command in voice-service or dial-peer
                              		  configuration mode.

If the phone user dials digits faster than the configured RTP NTE
                              		  end-event delay, Cisco Unified CME will process the dialed digits and ignore
                              		  the configured RTP NTE end-event delay unless you also configure the keypad-normalize command in ephone or
                              		  ephone-template configuration mode.

If you use an ephone template to apply a command to a phone and you
                              		  also use the same command in ephone configuration mode for the same phone, the
                              		  value that you set in ephone configuration mode has priority.

## Examples

The following example shows the configuration for ephone 43 in which
                              		  the nte-end-digit-delay command is configured for
                              		  a 200 ms delay.

```
Router(config)# show running-config .
.
.
ephone 43 
 button 1:29 
 nte-end-digit-delay 200
 keypad-normalize
```

### Related Commands

Command

Description

dtmf-interworking rtp-nte

Introduces a delay between the dtmf-digit begin and
                                          						dtmf-digit end events in RFC 2833 packets sent from the router.

ephone-template (ephone)

Applies a template to ephone being configured.

keypad-normalize

Ensures that the delay configured for a dtmf-end event is
                                          						always honored.

## ntp-server

To specify the IP address of the Network Time Protocol (NTP) server
                              		  used by SIP phones in a Cisco Unified CME system, use the ntp-server command in voice register global
                              		  configuration mode. To remove the NTP server, use the no form of this command.

ntp-server ip-address [ mode { anycast | directedbroadcast | multicast | unicast }]

no ntp-server

### Syntax Description

ip-address

IP address of the NTP server.

mode

(Optional) Enables the broadcast mode for the server.

anycast

Enables anycast mode.

directedbroadcast

Enables directed broadcast mode.

multicast

Enables multicast mode.

unicast

Enables unicast mode.

### Command Default

An NTP server is not used.

### Command Modes

Voice register global configuration (config-register-global)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(11)XJ

Cisco Unified CME 4.1

This command was introduced.

12.4(15)T

Cisco Unified CME 4.1

This command was integrated into Cisco IOS Release
                                          						12.4(15)T.

### Usage Guidelines

This command synchronizes all SIP phones to the specified NTP server.

This command is not supported on the Cisco Unified IP Phone 7905,
                              		  7912, 7940, or 7960.

## Examples

The following example shows the mode for the NTP server set to
                              		  multicast:

```
Router(config)# voice register global Router(config-register-global)# ntp-server 10.10.10.1 mode multicast
```

### Related Commands

Description

create profile

Generates the configuration profile files required for SIP
                                          						phones.

restart (voice register)

Performs a fast reset of one or all SIP phones associated
                                          						with a Cisco Unified CME router.

## number (ephone-dn)

To associate a telephone or extension number with an ephone-dn in a
                              		  Cisco CallManager Express (Cisco CME) system, use the number command in ephone-dn configuration
                              		  mode. To disassociate a number from an ephone-dn, use the no form of this command.

number number [ secondary number ] [ no-reg [ both | primary ]]

no number

### Syntax Description

number

String of up to 16 characters that represents an E.164
                                          						telephone number. Normally the string is composed of digits, but the string may
                                          						contain alphabetic characters when the number is dialed only by the router, as
                                          						with an intercom number. One or more periods (.) can be used as wildcard
                                          						characters. For details, see “Usage Guidelines.”

secondary

(Optional) Associates the number that follows as an
                                          						additional number for this ephone-dn.

no-reg

(Optional) The E.164 numbers in the dial peer do not
                                          						register with the gatekeeper. If you do not specify an option
                                          						( both or primary ) after the no-reg keyword, only the secondary
                                          						number is not registered.

both

(Optional) Both primary and secondary numbers are not
                                          						registered.

primary

(Optional) Primary number is not registered.

### Command Default

No primary or secondary phone number is associated with the
                              		  ephone-dn.

### Command Modes

Ephone-dn configuration (config-ephone-dn)

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

12.2(15)ZJ

Cisco CME 3.0

The ability to use alphabetic characters as part of the
                                          						number string was introduced.

12.3(4)T

Cisco CME 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

This command defines a valid number for an ephone-dn (extension) that
                              		  is to be assigned to an IP phone. The secondary keyword allows you to associate a
                              		  second telephone number with an ephone-dn so that it can be called by dialing
                              		  either the main or secondary phone number. The secondary number may contain
                              		  wildcards; for example, 50.. (the number 50 followed by periods, which stand
                              		  for wildcards).

The no-reg keyword causes an E.164 number in the
                              		  dial peer not to register with the gatekeeper. If you do not specify both or primary after the no-reg keyword, only the secondary number
                              		  does not register.

A number normally contains only numeric characters, which allow it to
                              		  be dialed from any telephone keypad. However, in certain cases, such as
                              		  intercom numbers, which are normally dialed only by the router, you can insert
                              		  alphabetic characters into the number to prevent phone users from dialing it
                              		  and using the intercom function without authorization.

A number can also contain one or more periods (.) as wildcard
                              		  characters that will match any dialed number in that position. For example,
                              		  51.. rings when 5100 is dialed, when 5101 is dialed, and so forth.

After you use the number command, assign the ephone-dn to an
                              		  ephone using the button command. Following the use of the button command, the restart command must be used to initiate a
                              		  quick reboot of the phone to which this number is assigned.

## Examples

The following example sets 5001 as the primary extension number for a
                              		  Cisco IP phone and 0 as the secondary number. This configuration allows the
                              		  telephone number 5001 to act as a regular extension number and also to act as
                              		  the operator line such that callers who dial 0 are routed to the phone line
                              		  with extension number 5001.

```
Router(config)# ephone-dn 1 Router(config-ephone-dn)# number 5001 secondary 0
```

The following example sets 5001 as the primary extension number for a
                              		  Cisco IP phone and “500.” (the number 500 followed by a period) as the
                              		  secondary number. This configuration allows any calls to extension numbers from
                              		  the range 5000 to 5009 to be routed to extension 5001 if the actual extension
                              		  number dialed cannot be found. For example, IP phones may be active in the
                              		  system with lines that correspond to 5001, 5002, 5004, 5005, and 5009. A call
                              		  to 5003 would be unable to locate a phone with extension 5003, so the call
                              		  would be routed to extension 5001.

```
Router(config-ephone-dn)# number 5001 secondary 500.
```

The following example defines a pair of intercom ephone-dns that are
                              		  programmed to call each other. The intercom numbers contain alphabetic
                              		  characters to prevent anyone from dialing them from another phone. Ephone-dn 19
                              		  is assigned the number A5511 and is programmed to dial A5522, which belongs to
                              		  ephone-dn 20. Ephone-dn 20 is programmed to dial A5511. No one else can dial
                              		  these numbers.

```
Router(config)# ephone-dn 19 Router(config-ephone-dn)# number A5511 Router(config-ephone-dn)# name Intercom Router(config-ephone-dn)# intercom A5522 Router(config-ephone-dn)# exit Router(config)# ephone-dn 20 Router(config-ephone-dn)# number A5522 Router(config-ephone-dn)# name Intercom Router(config-ephone-dn)# intercom A5511
```

### Related Commands

Description

button

Associates ephone-dns with individual buttons on Cisco IP
                                          						phones and specifies ring behavior per button.

intercom

Creates an intercom by programming a pair of extensions
                                          						(ephone-dns) to automatically call and answer each other.

name

Configures a username associated with a directory number.

preference

Sets preference for the attached dial peer for a directory
                                          						number.

restart (ephone)

Performs a fast reboot of a single phone associated with a
                                          						Cisco CME router.

restart (telephony-service)

Performs a fast reboot of one or all phones associated with
                                          						a Cisco CME router.

## night-service bell
                           	 (voice register dn)

To mark a voice
                              		  register dn for night-service treatment, use the night-service bell command in voice register dn configuration mode. To remove the
                              		  night-service treatment from the voice register dn, use the no form of
                              		  this command.

night-service bell

no night-service bell

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

By default, this
                              		  command is disabled.

### Command Modes

voice register dn configuration (config-register-dn)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

15.6(3)M

16.3.1

Cisco
                                          						Unified CME 11.5

This
                                          						command was introduced.

### Usage Guidelines

When a voice
                              		  register dn is marked for night-service treatment using this command, incoming
                              		  calls that ring during the night-service time period on that voice register dn
                              		  sends an alert indication to all IP phones that are marked to receive
                              		  night-service bell notification. This is achieved using the night-service
                                 			 bell (voice register pool) command. The alert notification is in the form
                              		  of a splash ring (not associated with any of the individual lines on the IP
                              		  phone) and a visible display of the voice register extension number. The phone
                              		  user retrieves the call by pressing a GPickUp soft key and dialing the
                              		  appropriate digits.

Night-service
                              		  periods are defined using the night-service
                                 			 date and night-service
                                 			 day commands. Night service can be manually disabled or enabled from a
                              		  phone configured with voice register dn in night-service mode if the night-service code command has been set.

## Examples

The following
                              		  example marks a voice register dn as a line that will ring on IP phones
                              		  designated to receive night-service bell notification when incoming calls are
                              		  received on this voice register dn during night-service periods:

```
Router(config)# voice register dn 16
Router(config-register-dn)# night-service bell
```

### Related Commands

Command

Description

night-service bell (voice register
                                                							 pool)

Marks a
                                          						SIP phone to receive night-service bell notification when incoming calls are
                                          						received on voice register DNs that are marked for night service during
                                          						night-service time periods.

night-service code

Defines
                                          						a code to disable or reenable night service on IP phones.

night-service date

Defines
                                          						a recurring time period associated with a month and day during which night
                                          						service is active.

night-service day

Defines
                                          						a recurring time period associated with a day of the week during which night
                                          						service is active.

## night-service bell
                           	 (voice register pool)

To mark a SIP
                              		  phone to receive night-service bell notification when incoming calls are
                              		  received on voice register dn that are marked for night service during
                              		  night-service time periods, use the night-service bell command in voice register pool configuration mode. To remove
                              		  night-service notification capability from a phone, use the no form of
                              		  this command.

night-service bell

no night-service bell

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

By default, this
                              		  command is disabled.

### Command Modes

voice register pool configuration (config-register-pool)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

15.6(3)M

16.3.1

Cisco
                                          						Unified CME 11.5

This
                                          						command was introduced.

### Usage Guidelines

When a voice
                              		  register dn is marked for night-service treatment using the night-service
                                 			 bell (voice register dn) command, incoming calls that ring during the
                              		  night-service time period on that DN send an alert indication to all SIP phones
                              		  marked to receive night-service bell notification. The alert notification is in
                              		  the form of a splash ring (not associated with any of the individual lines on
                              		  the IP phone) and a visible display of the voice register dn extension number.
                              		  The phone user retrieves the call by pressing the GPickUp soft key and dialing
                              		  the appropriate digits.

Night-service
                              		  periods are defined using the night-service
                                 			 date and night-service
                                 			 day commands. Night service can be manually disabled or re-enabled from a
                              		  phone configured with voice register dn in night-service mode if the night-service
                                 			 code command is set.

If you use a voice
                              		  register template to apply a command to a SIP phone and you also use the same
                              		  command in pool configuration mode for the same phone, the value that you set
                              		  in pool configuration mode has priority.

## Examples

The following
                              		  example designates the SIP phone that is being configured as a phone that will
                              		  receive night-service bell notification when voice register dns marked for
                              		  night service receive incoming calls during a night-service period:

```
Router(config)# voice register pool 4
Router(config-register-pool)# night-service bell
```

### Related Commands

Command

Description

night-service bell (voice register
                                                							 dn)

Marks a
                                          						voice register dn to send night-service bell notification to designated SIP
                                          						phones during night-service time periods.

night-service bell (voice register template)

Applies
                                          						a template to a pool configuration.

night-service code

Defines
                                          						a code to disable or reenable night service on IP phones.

night-service date

Defines
                                          						a recurring time period associated with a month and day during which night
                                          						service is active.

night-service day

Defines a recurring time period associated with a day of the week during which
                                          						night service is active.

## night-service bell
                        	 (voice register template)

To mark a SIP
                              		  phone to receive night-service bell notification when incoming calls are
                              		  received on voice register dn that are marked for night service during
                              		  night-service time periods, use the night-service bell command in voice register template configuration mode. To
                              		  remove night-service notification capability from a phone, use the no form of
                              		  this command.

night-service bell

no night-service bell

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

By default, this
                              		  command is disabled.

### Command Modes

voice register template configuration (config-register-template)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

15.6(3)M

16.3.1

Cisco
                                          						Unified CME 11.5

This
                                          						command was introduced.

### Usage Guidelines

When a voice
                              		  register dn is marked for night-service treatment using the night-service
                                 			 bell (voice register dn) command, incoming calls that ring during the
                              		  night-service time period on that DN send an alert indication to all SIP phones
                              		  marked to receive night-service bell notification. The alert notification is in
                              		  the form of a splash ring (not associated with any of the individual lines on
                              		  the IP phone) and a visible display of the voice register dn extension number.
                              		  The phone user retrieves the call by pressing the GPickUp soft key and dialing
                              		  the appropriate digits.

Night-service
                              		  periods are defined using the night-service
                                 			 date and night-service
                                 			 day commands. Night service can be manually disabled or re-enabled from a
                              		  phone configured with voice register dn in night-service mode if the night-service
                                 			 code command is set.

If you use a voice
                              		  register template to apply a command to a SIP phone and you also use the same
                              		  command in pool configuration mode for the same phone, the value that you set
                              		  in pool configuration mode has priority.

## Examples

The following
                              		  example designates the SIP phone that is being configured as a phone that will
                              		  receive night-service bell notification when voice register dns marked for
                              		  night service receive incoming calls during a night-service period:

```
Router(config)# voice register pool 4
Router(config-register-pool)# night-service bell
```

### Related Commands

Command

Description

night-service bell (voice register
                                                							 dn)

Marks a
                                          						voice register dn to send night-service bell notification to designated SIP
                                          						phones during night-service time periods.

voice register pool

Applies
                                          						a template to a pool configuration.

night-service code

Defines
                                          						a code to disable or reenable night service on IP phones.

night-service date

Defines
                                          						a recurring time period associated with a month and day during which night
                                          						service is active.

night-service day

Defines a recurring time period associated with a day of the week during which
                                          						night service is active.

## number (voice
                        	 register dn)

To associate a
                              		  telephone or extension number with a SIP phone in a Cisco CallManager Express
                              		  (Cisco CME) system, use the number command in voice register dn configuration mode. To disassociate a number, use
                              		  the no form of
                              		  this command.

number number

no number

### Syntax Description

number

String
                                          						of up to 16 characters that represents an E.164 telephone number. Normally the
                                          						string is composed of digits, but the string may contain alphabetic characters
                                          						when the number is dialed only by the router, as with an intercom number.

### Command Default

This command has
                              		  no default behavior or values.

### Command Modes

Voice register dn configuration (config-register-dn)

## Command History

Cisco
                                          						IOS Release

Version

Modification

12.4(4)T

Cisco
                                          						CME 3.4 and Cisco SIP SRST 3.4

This
                                          						command was introduced.

### Usage Guidelines

Valid characters in voice register DN include 0-9, '.' , '+', '*' and
                              		  '#'.

To allow insertion of '#' at any place in voice register dn, the CLI
                              		  "allow-hash-in-dn" is configured in voice register global mode.

When the CLI "allow-hash-in-dn" is configured, the user is required to
                              		  change the dial-peer terminator from '#' (default terminator) to another valid
                              		  terminator in configuration mode. The other terminators that are supported
                              		  include '0'-'9', 'A'-'F', and '*'.

This command
                              		  defines a valid number for an extension that is to be assigned to a SIP phone.
                              		  Use this command before using the other commands in voice register dn
                              		  configuration mode.

A number normally
                              		  contains only numeric characters which allows users to dial the number from any
                              		  telephone keypad. However, in certain cases, such as the numbers for intercom
                              		  extensions, you want to use numbers that can only be dialed internally from the
                              		  Cisco CallManager Express router and not from telephone keypads.

The number command allows you to assign alphabetic characters to the number so that the
                              		  extension can be dialed by the router for intercom calls but not by
                              		  unauthorized individuals from other phones.

After you use the number command, use the reset command to initiate a quick reboot of the phone to which this
                              		  number is assigned.

## Examples

The following
                              		  example shows how to set 5001 as the extension number for directory number 1 on
                              		  a SIP phone.

```
Router(config)# voice register dn 1 Router(config-register-dn)# number 5001
```

### Related Commands

Description

reset (voice register global)

Performs a complete reboot of all SIP phones associated with a Cisco CME
                                          						router.

reset (voice register pool)

Performs a complete reboot of a single SIP phone associated with a Cisco CME
                                          						router.

## number (voice register pool)

To indicate the E.164 phone numbers that the registrar permits to
                              		  handle the Register message from a Cisco Unified SIP IP phone, use the number command in voice register pool
                              		  configuration mode. To disable number registration, use the no form of this command.

number tag { number-pattern [ preference value ] [ huntstop ] | dn dn-tag }

no number tag

### Syntax Description

tag

Telephone number when there are multiple number commands. Range is 1 to 114.

number-pattern

Phone numbers (including wild cards and patterns) that are
                                          						permitted by the registrar to handle the Register message from the Cisco
                                          						Unified SIP IP phone.

preference value

(Optional) Defines the number list preference order. Range
                                          						is 0 to 10. The highest preference is 0. There is no default.

huntstop

(Optional) Stops hunting when the dial peer is busy.

dn dn-tag

Identifies the directory number tag for this phone number
                                          						as defined by the voice register dn command. Range is 1 to 288.

### Command Default

Cisco Unified SIP IP phones cannot register in Cisco Unified CME.

### Command Modes

Voice register pool configuration (config-register-pool)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco SIP SRST 3.0

This command was introduced.

12.3(4)T

Cisco SIP SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was added to Cisco CME and the dn keyword was added.

12.4(11)XJ

Cisco Unified CME 4.1 Cisco Unified SRST 4.1

This command was modified. The number-pattern argument and preference and huntstop keywords were removed from
                                          						Cisco Unified CME.

12.4(15)T

Cisco Unified CME 4.1 Cisco Unified SRST 4.1

The modifications to this command were integrated into
                                          						Cisco IOS Release 12.4(15)T.

15.2(4)M

Cisco Unified CME 9.1 Cisco Unified SIP SRST 9.1

This command was modified to increase the valid value of
                                          						the tag argument to 114.

### Usage Guidelines

The number command indicates the phone numbers
                              		  that are permitted by the registrar to handle the Register message from the
                              		  Cisco Unified SIP IP phone.

In Cisco Unified SRST, the keywords and arguments of this command
                              		  allow for more explicit setting of user preferences regarding what number
                              		  patterns should match the voice register pool.

## Examples

The following example shows three directory numbers assigned to Cisco
                              		  Unified SIP IP phone 1 in Cisco Unified CME:

```
!
voice register pool  1
 id mac 0017.E033.0284
 type 7961
 number 1 dn 10
 number 2 dn 12
 number 3 dn 13
 codec g711ulaw
!
```

The following example shows directory numbers 10, 12, and 13 assigned
                              		  to phone numbers 1, 2, and 55 of Cisco Unified SIP IP phone 2:

```
voice register pool 2
id mac 0017.E033.0284
type 7961
number 1 dn 10
number 2 dn 12
number 55 dn 13
codec g711ulaw
```

The following example shows a telephone number pattern set to 95...
                              		  in Cisco Unified SRST. This means all five-digit numbers beginning with 95 are
                              		  permitted by the registrar to handle the Register message.

```
voice register pool 3
 id network 10.2.161.0 mask 255.255.255.0
 number 1 95... preference 1
 cor incoming call95 1 95011
```

### Related Commands

Command

Description

id (voice register pool)

Explicitly identifies a locally available, individual Cisco
                                          						Unified SIP IP phone or, when running Cisco Unified SIP SRST, a set of Cisco
                                          						Unified SIP IP phones.

voice register dn

Enters voice register dn configuration mode to define an
                                          						extension for a phone line, intercom line, voice-mail port, or a
                                          						message-waiting indicator.

## number (voice user-profile and voice logout-profile)

To create line definitions in a voice-user profile or voice-logout
                              		  profile to be downloaded to a Cisco Unified IP phone that is enabled for
                              		  extension mobility, use the number command in voice user-profile
                              		  configuration mode or voice logout-profile configuration mode. To remove line
                              		  definition from a profile, use the no form of this command.

### Syntax Description

number

String of up to 16 characters that represents an E.164
                                          						telephone number to be associated with and displayed next to a line button on
                                          						an IP phone. This directory number must be already configured by using the number command in ephone-dn or
                                          						voice register dn configuration mode.

[ , ...number ]

(Optional) For overlay lines only, with or without call
                                          						waiting. Directory numbers to roll over to this line. Can contain up to 25
                                          						individual numbers separated by commas (,). This directory number must be
                                          						already configured by using the number command in ephone-dn or
                                          						voice register dn configuration mode.

type

Characteristics to be associated with this line button.

type

Word that describes characteristics to be associated with
                                          						the line button being configured. Valid entries are as follows:

- beep-ring

- feature-ring

- monitor-ring

- silent-ring

- overlay

- cw-overlay

### Command Default

No line definition is created.

### Command Modes

Voice logout-profile configuration (config-logout-profile) Voice user-profile configuration (config-user-profile)

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

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

This command in voice user-profile configuration mode to creates a
                              		  line button definition in a user profile to be downloaded to the IP phone when
                              		  the user is logged into an IP phone that is enabled for extension mobility.

This command in voice logout-profile configuration mode creates a
                              		  line button definition in a default profile to be downloaded to an IP phone
                              		  when no user is logged into an IP phone that is enabled for extension mobility.

For button appearance, extension mobility will associate line
                              		  definitions in the voice-logout profile or voice-user profile to phone buttons
                              		  in a sequential manner. If the profile contains more directory and speed-dial
                              		  numbers than there are buttons on the physical phone to which the profile is
                              		  downloaded, the remaining numbers in the profile are ignored.

On Cisco Unified IP phones, line definitions are assigned to
                              		  available extension buttons before speed-dial definitions, in sequential order,
                              		  starting with the lowest directory number first.

After creating or modifying a profile, use the reset (voice logout-profile or voice
                              		  user-profile) command to reset all phones associated with the profile being
                              		  configured to propagate the changes.

Type ? to list valid options for the type keyword. The following options are valid
                              		  at the time that this document was written:

- beep-ring

Beep but no ring. Audible ring is suppressed for incoming calls but
                              		  call-waiting beeps are allowed. Visible cues are the same as those for a normal
                              		  ring.

- feature-ring

Differentiates incoming calls on a special line from incoming calls
                              		  on other lines on the phone. The feature-ring cadence is a triple pulse, as
                              		  opposed to a single-pulse ring for normal internal calls and a double-pulse
                              		  ring for normal external calls.

- monitor-ring

A line button that is configured for monitor mode on one phone
                              		  provides visual line status for a line that also appears on another phone. When
                              		  monitor mode is set for a button with a shared line, the line status indicates
                              		  that the shared line is either idle or in use. The line and line button are
                              		  available in monitor mode for visual status only. Calls cannot be made or
                              		  received using a line button that has been set in monitor mode. Incoming calls
                              		  on a line button that is in monitor mode do not ring and do not display caller
                              		  ID or call-waiting caller ID. Monitor mode is intended to be used only in the
                              		  context of shared lines so that one user, such as a receptionist, can visually
                              		  monitor the in-use status of several users’ phone extensions (for example, as a
                              		  busy-lamp field).

The line button for a monitored line can be used as a
                              		  direct-station-select for a call transfer when the monitored line is in an idle
                              		  state. In this case, the phone user who transfers a call from a normal line can
                              		  press the Transfer button and then press the line button of the monitored line,
                              		  causing the call to be transferred to the phone number of the monitored line.

- silent-ring

You can configure silent ring on any type of phone. However, you
                              		  typically set silent ring only on buttons of a phone with multiple lines, such
                              		  as a Cisco Unified IP Phone 7940 or Cisco Unified IP Phone 7960 and 7960G. The
                              		  only visible cue is a flashing icon in the phone display.

If you configure a button to have a silent ring, you will not hear a
                              		  call-waiting beep or call-waiting ring regardless of whether the ephone-dn
                              		  associated with the button is configured to generate a call-waiting beep or
                              		  call-waiting ring.

- overlay

Overlay lines are directory numbers that share a single line button
                              		  on a multibutton phone. When more than one incoming call arrives on lines that
                              		  are set on a single button, the line (ephone-dn) that is the left most in the number command list is the primary line and
                              		  is given the highest priority. If this call is answered by another phone or if
                              		  the caller hangs up, the phone selects the next line in its overlay set to
                              		  present as the ringing call. The caller ID display updates to show the caller
                              		  ID for the currently presented call.

Directory numbers that are part of an overlay set can be single-line
                              		  directory numbers or dual-line directory numbers, but the set must contain
                              		  either all single-line or all dual-line directory numbers, and not a mixture of
                              		  the two.

The primary directory number on each phone in a shared-line overlay
                              		  set should be a unique ephone-dn. The unique ephone-dn guarantees that the
                              		  phone will have a line available for outgoing calls, and ensures that the phone
                              		  user can obtain dial-tone even when there are no idle lines available in the
                              		  rest of the shared-line overlay set. Use a unique directory number in this
                              		  manner to provide for a unique calling party identity on outbound calls made by
                              		  the phone so that the called user can see which specific phone is calling.

The name of the first directory number in the overlay set is not
                              		  displayed because it is the default directory number for calls to the phone,
                              		  and the name or number is permanently displayed next to the phone’s button. For
                              		  example, if there are ten numbers in an overlay set, only the last nine numbers
                              		  are displayed when calls are made to them.

- cw-overlay

The same configuration is used for overlaid lines both with and
                              		  without call waiting.

Directory numbers can accept call interruptions, such as call
                              		  waiting, by default. For call waiting to work, the default must be active. To
                              		  ensure that this is the case, remove the no call-waiting beep accept command from the configurations of
                              		  directory numbers for which you want to use call waiting.

Directory numbers that are part of a cw-overlay set can be
                              		  single-line directory numbers or dual-line directory numbers, but the set must
                              		  contain either all single-line or all dual-line directory numbers, and not a
                              		  mixture of the two.

The Cisco Unified IP Phone 7931G cannot support overlays that contain
                              		  directory numbers that are configured for dual-line mode.

## Examples

The following example shows the configuration for a voice-user
                              		  profile to be downloaded when the a phone user logs into a Cisco Unified IP
                              		  phone that is enabled for extension mobility. The lines and speed-dial buttons
                              		  in this profile that are configured on an IP phone after the user logs in
                              		  depend on phone type. For example, if the user logs into a Cisco Unified IP
                              		  Phone 7970, all buttons are configured according to voice-user profile1.
                              		  However, if the phone user logs into a Cisco Unified IP Phone 7960, all six
                              		  lines are mapped to phone buttons, and the speed dial is ignored because there
                              		  is no button available for speed dial.

```
pin 12345
 user me password pass123
 number 2001 type silent-ring
 number 2002 type beep-ring
 number 2003 type feature-ring
 number 2004 type monitor-ring
 number 2005,2006 type overlay
 number 2007,2008 type cw-overly
 speed-dial 1 3001
 speed-dial 2 3002 blf
```

### Related Commands

Command

Description

logout-profile

Enables Cisco Unified IP phone for extension mobility and
                                          						assigns a logout profile to this phone.

reset (voice logout-profile and voice user-profile)

Performs a complete reboot of all IP phones to which a
                                          						particular logout-profile or user-profile is downloaded.

## num-buttons

To set the number
                              		  of line buttons supported by a phone type, use the num-buttons command in ephone-type configuration mode. To reset to the
                              		  default, use the no form of
                              		  this command.

num-buttons number

no num-buttons

### Syntax Description

number

Number
                                          						of line buttons. Range: 1 to 100. Default: 0. See the table for the number of
                                          						buttons supported by each phone type.

### Command Default

No line buttons
                              		  are supported by the phone type.

### Command Modes

Ephone-type configuration (config-ephone-type)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.4(15)XZ

Cisco
                                          						Unified CME 4.3 Cisco Unified SRST 4.3

This
                                          						command was introduced.

12.4(20)T

Cisco
                                          						Unified CME 7.0 Cisco Unified SRST 7.0

This
                                          						command was integrated into Cisco IOS Release 12.4(20)T.

### Usage Guidelines

This command
                              		  defines the number of line buttons supported by the type of phone being added
                              		  with an ephone-type template.

Supported
                                          					 Device

device-id

device-type

num-buttons

max-presentation

Cisco
                                          					 Unified IP Phone 6901

547

6901

1

1

Cisco
                                          					 Unified IP Phone 6911

548

6911

1

10

Cisco
                                          					 Unified IP Phone 7915 Expansion Module with 12 buttons

227

7915

12

0
                                          					 (default)

Cisco
                                          					 Unified IP Phone 7915 Expansion Module with 24 buttons

228

7915

24

0

Cisco
                                          					 Unified IP Phone 7916 Expansion Module with 12 buttons

229

7916

12

0

Cisco
                                          					 Unified IP Phone 7916 Expansion Module with 24 buttons

230

7916

24

0

Cisco
                                          					 Unified Wireless IP Phone 7925

484

7925

6

4

Cisco
                                          					 Unified IP Conference Station 7937G

431

7937

1

6

Nokia
                                          					 E61

376

E61

1

1

## Examples

The following
                              		  example shows that 1 line button is specified for the Nokia E61 when creating
                              		  the ephone-type template.

```
Router(config)# ephone-type E61 Router(config-ephone-type)# num-buttons 1
```

### Related Commands

Command

Description

device-id

Specifies the device ID for a phone type.

max-presentation

Sets
                                          						the number of call presentation lines supported by a phone type.

type

Assigns the phone type to an SCCP phone.

## num-line

To define the
                              		  maximum number of lines supported by new phone, use the num-line command in voice register pool-type mode. To remove the lines configured, use
                              		  the no form of
                              		  this command.

num-line max-line

no num-line max-line

## Syntax Description

Specific
                                       					 the number of lines supported by the phone model. Range is 1-114.

### Command Default

The default value
                              		  of the addons is 1. When the reference-pooltype command is configured, the number of lines supported by the reference phone is
                              		  inherited.

### Command Modes

Voice Register Pool Configuration (config-register-pool)

## Command History

Cisco SIP
                                       					 CME 10.0

This
                                       					 command was introduced.

### Usage Guidelines

Use this command
                              		  to define the maximum number of lines for a Cisco Unified SIP IP phone on Cisco
                              		  Unified CME. When you use the no form of this command, the inherited
                              		  properties of the reference phone takes precedence over the default value.

## Examples

The following
                              		  example shows how to enter voice register pool-type configuration mode and
                              		  define the maximum number of lines for a Cisco Unified SIP IP phone:

```
Router(config)# voice register pool-type 9900 Router(config-register-pool-type)# num-line 5
```

### Related Commands

Command

Description

Adds a new Cisco Unified SIP IP phone to Cisco Unified CME.

| name | Alphanumeric string of person or group associated with a
                                          						directory number. Name must follow the order specified in the directory (telephony-service) command, either first-name-first or last-name-first . The two parts,
                                          						first and last name or last and first name, of this argument must be separated
                                          						with a space. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco ITS 1.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |

| Command | Description |
|---|---|
| directory (telephony-service) | Defines the name order for the local directory of Cisco IP
                                          						phone users. |

| “primary pilot name” | Name of primary pilot number. |
|---|---|
| secondary “secondary pilot nam e” | (Optional) Name of secondary pilot number. |

| Release | Modification |
|---|---|
| 15.3(2)T | This command was introduced. |

| Note | Use quotes (") when input strings have spaces in between. |
|---|---|

| Command | Description |
|---|---|
| voice hunt-group | Enters voice hunt-group configuration mode and creates a
                                          						hunt group for phones in a Cisco Unified CME system. |
| show voice hunt-group | Displays configuration information associated with one or
                                          						all voice hunt groups in a Cisco Unified CME system. |

| string | String (30 characters) used to describe or identify an
                                          						ERL’s location. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XY | Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1) | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| address | Specifies a comma separated text entry (up to 247
                                          						characters) of an ERL’s civic address. |
| elin | Specifies a PSTN number to replace the caller’s extension. |
| subnet | Defines which IP phones are part of this ERL. |
| voice emergency response location | Creates a tag for identifying an ERL for E911 services. |

| “primary pilot name” | Name of primary pilot number. |
|---|---|
| secondary “secondary pilot name” | (Optional) Name of secondary pilot number. |

| Release | Modification |
|---|---|
| 15.3(2)T | This command was introduced. |

| Note | Use quotes (") when input strings have spaces in between. |
|---|---|

| Command | Description |
|---|---|
| voice hunt-group | Enters voice hunt-group configuration mode and creates a
                                          						hunt group for phones in a Cisco Unified CME system. |
| show voice hunt-group | Displays configuration information associated with one or
                                          						all voice hunt groups in a Cisco Unified CME system. |

| name | Name of the person associated with a given extension. Name
                                          						must follow the order specified in the directory (telephony-service)
                                          						command, either first-name-first or last-name-first . |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

|  | Description |
|---|---|
| directory (telephony-service) | Defines the name order for the local directory of Cisco IP
                                          						phone users. |

| network-locale-tag | Locale identifier that was assigned to a network locale
                                          						using the network-locale (telephony-service) command. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

|  | Description |
|---|---|
| cnf-file | Specifies the type of configuration files that phones use. |
| ephone-template (ephone) | Applies an ephone template to an ephone. |
| network-locale (telephony-service) | Sets the locale for geographically specific tones and
                                          						cadences. |

| network-locale-tag | (Optional) Assigns a locale identifier to the locale code.
                                          						Range is 0 to 4. Default is 0. |
|---|---|
| user-defined code | (Optional) Assigns one of the user-defined codes to the
                                          						specified locale code. Valid codes are U1 , U2 , U3 , U4 , and U5 . There is no default. |
| locale-code | Locale files for the following ISO 3166 codes are
                                          						predefined in system storage for supported phone types: AT —Austria CA —Canada CH —Switzerland DE —Germany DK —Denmark ES —Spain FR —France GB —United Kingdom IT —Italy JP —Japan NL —Netherlands NO —Norway PT —Portugal RU —Russian Federation SE —Sweden US —United States (default) Note You can also assign any valid ISO 3166 code that is not
                                                   						listed above to a user-defined code (U1 through U5), but you must first copy
                                                   						the appropriate XML tone files to flash, slot 0, or an external TFTP server and
                                                   						use the cnf-files perphone command to specify the use of
                                                   						per-phone configuration files. | Note | You can also assign any valid ISO 3166 code that is not
                                                   						listed above to a user-defined code (U1 through U5), but you must first copy
                                                   						the appropriate XML tone files to flash, slot 0, or an external TFTP server and
                                                   						use the cnf-files perphone command to specify the use of
                                                   						per-phone configuration files. |
| Note | You can also assign any valid ISO 3166 code that is not
                                                   						listed above to a user-defined code (U1 through U5), but you must first copy
                                                   						the appropriate XML tone files to flash, slot 0, or an external TFTP server and
                                                   						use the cnf-files perphone command to specify the use of
                                                   						per-phone configuration files. |

| Note | You can also assign any valid ISO 3166 code that is not
                                                   						listed above to a user-defined code (U1 through U5), but you must first copy
                                                   						the appropriate XML tone files to flash, slot 0, or an external TFTP server and
                                                   						use the cnf-files perphone command to specify the use of
                                                   						per-phone configuration files. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(11)YT | Cisco ITS 2.1 | This command was introduced. |
| 12.2(15)T | Cisco ITS 2.1 | This command was integrated into Cisco IOS Release
                                          						12.2(15)T. |
| 12.4(4)XC | Cisco Unified CME 4.0 | The network-locale-tag and user-defined-code arguments were added. |
| 12.4(9)T | Cisco Unified CME 4.0 | The network-locale-tag and user-defined-code arguments were integrated into Cisco IOS Release
                                          						12.4(9)T. |

|  | Description |
|---|---|
| cnf-files | Specifies the type of phone configuration files to be
                                          						created. |
| ephone-template (ephone) | Applies an ephone template to an ephone. |
| network-locale (ephone-template) | Applies a locale tag identifier to an ephone template. |
| reset (ephone) | Performs a complete reboot of one phone associated with a
                                          						Cisco Unified CME router. |
| reset (telephony-service) | Performs a complete reboot of one or all phones associated
                                          						with a Cisco Unified CME router. |
| show telephony-service tftp-bindings | Displays the current configuration files that are
                                          						accessible to IP phones. |
| user-locale (telephony-service) | Sets the language for displays on supported phone types. |

| country-code | The following ISO 3166 country codes are supported: |
|---|---|
|  | AE —United Arab Emirates AR —Argentina AT —Austria AU —Australia BE —Belgium BR —Brazil CA —Canada CH —Switzerland CN —China CO —Colombia CY —Cyprus CZ —Czech Republic DE —Germany DK —Denmark EG —Egypt ES —Spain FI —Finland FR —France GB —United Kingdom GH —Ghana GR —Greece | HK —Hong Kong HU —Hungary ID —Indonesia IE —Ireland IL —Israel IN —India IS —Iceland IT —Italy JO —Jordan JP —Japan KE —Kenya KR —Korea Republic KW —Kuwait LB —Lebanon LU —Luxembourg MX —Mexico MY —Malaysia NG —Nigeria NL —Netherlands NO —Norway NP —Nepal NZ —New Zealand | OM —Oman PA —Panama PE —Peru PH —Philippines PK —Pakistan PL —Poland PT —Portugal RU —Russian Federation SA —Saudi Arabia SE —Sweden SG —Singapore SI —Slovenia SK —Slovakia TH —Thailand TR —Turkey TW —Taiwan US —United States (default) VE —Venezuela ZA —South Africa ZW —Zimbabwe |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| cptone | Specifies a regional analog voice-interface-related tone,
                                          						ring, and cadence setting. |
| reset (voice-gateway) | Performs a complete reboot of all analog phones associated
                                          						with the voice gateway and registered to Cisco Unified CME. |
| show telephony-service tftp-bindings | Displays the current configuration files accessible to IP
                                          						phones. |
| voice-port (voice-gateway) | Identifies the ports on the voice gateway that will
                                          						register to Cisco Unified CME. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was made available in ephone-template
                                          						configuration mode. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command in ephone-template configuration mode was
                                          						integrated into Cisco IOS Release 12.4(9)T. |

|  | Description |
|---|---|
| ephone-template (ephone) | Applies a template to an ephone configuration. |
| night-service bell (ephone-dn) | Marks an ephone-dn to send night-service bell notification
                                          						to designated IP phones during night-service time periods. |
| night-service code | Defines a code to disable or reenable night service on IP
                                          						phones. |
| night-service date | Defines a recurring time period associated with a month and
                                          						day during which night service is active. |
| night-service day | Defines a recurring time period associated with a day of
                                          						the week during which night service is active. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

|  | Description |
|---|---|
| night-service bell (ephone) | Marks an IP phone to receive night-service bell
                                          						notification when incoming calls are received on ephone-dns that are marked for
                                          						night service during night-service time periods. |
| night-service code | Defines a code to disable or reenable night service on IP
                                          						phones. |
| night-service date | Defines a recurring time period associated with a month and
                                          						day during which night service is active. |
| night-service day | Defines a recurring time period associated with a day of
                                          						the week during which night service is active. |

| digit-string | Digit
                                          						code that a user enters at an IP phone to disable or reenable night service.
                                          						The code must begin with an asterisk (*). The maximum number of characters is
                                          						16, including the asterisk. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco
                                          						CME 3.0 | This
                                          						command was introduced. |
| 12.3(4)T | Cisco
                                          						CME 3.0 | This
                                          						command was integrated into Cisco IOS Release 12.3(4)T. |
| 12.3(14)T | Cisco
                                          						CME 3.3 | The
                                          						action of this command was changed so that all night-service ephone-dns are
                                          						activated or deactivated when the code is used rather than just the phone on
                                          						which the code is input. |
| 15.6(3)M 16.3.1 | Cisco
                                          						Unified CME 11.5 | From
                                          						Unified CME 11.5 onwards, this command can be used to activate or deactivate
                                          						the night service from SIP phones as well. |

|  | Description |
|---|---|
| night-service bell (ephone) | Marks
                                          						an IP phone to receive night-service bell notification when incoming calls are
                                          						received on ephone-dns that are marked for night service during night-service
                                          						time periods. |
| night-service bell (ephone-dn) | Marks
                                          						an ephone-dn to send night-service bell notification to designated IP phones
                                          						during night-service time periods. |
| night-service bell (voice register pool) | Marks
                                          						a SIP phone to receive night-service bell notification when incoming calls are
                                          						received on voice register DNs that are marked for night service during
                                          						night-service time periods. |
| night-service bell (voice register dn) | Marks
                                          						a voice register dn to send night-service bell notification to designated SIP
                                          						phones during night-service time periods. |
| night-service bell (voice register template) | Applies a template to a pool configuration. |
| night-service date | Defines a recurring time period associated with a month and day during which
                                          						night service is active. |
| night-service day | Defines a recurring time period associated with a day of the week during which
                                          						night service is active. |

| month | Abbreviated month. The following abbreviations for month
                                          						are valid: jan , feb , mar , apr , may , jun , jul , aug , sep , oct , nov , dec . |
|---|---|
| day | Day of the month. Range is from 1 to 31. |
| start-time stop-time | Beginning and ending times for night service, in an HH:MM
                                          						format using a 24-hour clock. The stop time must be greater than the start
                                          						time. The value 24:00 is not valid. If 00:00 is entered as a stop time, it is
                                          						changed to 23:59. If 00:00 is entered for both start time and stop time, night
                                          						service is in effect for the entire 24-hour period on the specified date. |

| Cisco IOS Release | Cisco product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

|  | Description |
|---|---|
| night-service bell (ephone) | Marks an IP phone to receive night-service-bell
                                          						notification when incoming calls are received on ephone-dns that are marked for
                                          						night service during night-service time periods. |
| night-service bell (ephone-dn) | Marks an ephone-dn to send night-service bell notification
                                          						to designated IP phones during night-service time periods. |
| night-service code | Defines a code to disable or reenable night service on IP
                                          						phones. |
| night-service day | Defines a recurring time period associated with a day of
                                          						the week during which night service is active. |

| day | Day of the week abbreviation. The following are valid day
                                          						abbreviations: sun , mon , tue , wed , thu , fri , sat . |
|---|---|
| start-time stop-time | Beginning and ending times for night service, in an HH:MM
                                          						format using a 24-hour clock. If the stop time is a smaller value than the
                                          						start time, the stop time occurs on the day following the start time. For
                                          						example, mon 19:00 07:00 means “from Monday at 7 p.m. until Tuesday at 7 a.m.” The value 24:00 is not valid. If 00:00 is entered as a stop
                                          						time, it is changed to 23:59. If 00:00 is entered for both start time and stop
                                          						time, night service is in effect for the entire 24-hour period on the specified
                                          						day. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

|  | Description |
|---|---|
| night-service bell (ephone) | Marks an IP phone to receive night-service bell
                                          						notification when incoming calls are received on ephone-dns that are marked for
                                          						night service during night-service time periods. |
| night-service bell (ephone-dn) | Marks an ephone-dn to send night-service bell notification
                                          						to designated IP phones during night-service time periods. |
| night-service code | Defines a code to disable or reenable night service on IP
                                          						phones. |
| night-service date | Defines a recurring time period associated with a month and
                                          						day during which night service is active. |

| start-time stop-time | Beginning and ending times for night service, in an HH:MM
                                          						format using a 24-hour clock. If the stop time is a smaller value than the
                                          						start time, the stop time occurs on the day following the start time. For
                                          						example, mon 19:00 07:00 means “from Monday at 7 p.m. until Tuesday at 7 a.m.” The value 24:00 is not valid. If 00:00 is entered as a stop
                                          						time, it is changed to 23:59. If 00:00 is entered for both start time and stop
                                          						time, night service is in effect for the entire 24-hour period on the specified
                                          						day. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |

| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |
|---|---|---|

|  | Description |
|---|---|
| night-service bell (ephone) | Marks an IP phone to receive night-service bell
                                          						notification when incoming calls are received on ephone-dns that are marked for
                                          						night service during night-service time periods. |
| night-service bell (ephone-dn) | Marks an ephone-dn to send night-service bell notification
                                          						to designated IP phones during night-service time periods. |
| night-service code | Defines a code to disable or reenable night service on IP
                                          						phones. |
| night-service date | Defines a recurring time period associated with a month and
                                          						day during which night service is active. |
| night-service day | Defines a recurring time period associated with a day of
                                          						the week during which night service is active. |
| night-service weekday | Defines a recurring night-service time period to be in
                                          						effect only on weekdays. |
| night-service weekend | Defines a recurring night-service time period to be in
                                          						effect only on weekends. |

| start-time stop-time | Beginning and ending times for night service, in an HH:MM
                                          						format using a 24-hour clock. If the stop time is a smaller value than the
                                          						start time, the stop time occurs on the day following the start time. For
                                          						example, mon 19:00 07:00 means “from Monday at 7 p.m. until Tuesday at 7 a.m.” The value 24:00 is not valid. If 00:00 is entered as a stop
                                          						time, it is changed to 23:59. If 00:00 is entered for both start time and stop
                                          						time, night service is in effect for the entire 24-hour period on the specified
                                          						day. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

|  | Description |
|---|---|
| night-service bell (ephone) | Marks an IP phone to receive night-service bell
                                          						notification when incoming calls are received on ephone-dns that are marked for
                                          						night service during night-service time periods. |
| night-service bell (ephone-dn) | Marks an ephone-dn to send night-service bell notification
                                          						to designated IP phones during night-service time periods. |
| night-service code | Defines a code to disable or reenable night service on IP
                                          						phones. |
| night-service date | Defines a recurring time period associated with a month and
                                          						day during which night service is active. |
| night-service day | Defines a recurring time period associated with a day of
                                          						the week during which night service is active. |
| night-service everyday | Defines a recurring night-service time period to be in
                                          						effect everyday. |
| night-service weekend | Defines a recurring night-service time period to be in
                                          						effect only on weekends. |

| start-time stop-time | Beginning and ending times for night service, in an HH:MM
                                          						format using a 24-hour clock. If the stop time is a smaller value than the
                                          						start time, the stop time occurs on the day following the start time. For
                                          						example, mon 19:00 07:00 means “from Monday at 7 p.m. until Tuesday at 7 a.m.” The value 24:00 is not valid. If 00:00 is entered as a stop
                                          						time, it is changed to 23:59. If 00:00 is entered for both start time and stop
                                          						time, night service is in effect for the entire 24-hour period on the specified
                                          						day. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

|  | Description |
|---|---|
| night-service bell (ephone) | Marks an IP phone to receive night-service bell
                                          						notification when incoming calls are received on ephone-dns that are marked for
                                          						night service during night-service time periods. |
| night-service bell (ephone-dn) | Marks an ephone-dn to send night-service bell notification
                                          						to designated IP phones during night-service time periods. |
| night-service code | Defines a code to disable or reenable night service on IP
                                          						phones. |
| night-service date | Defines a recurring time period associated with a month and
                                          						day during which night service is active. |
| night-service day | Defines a recurring time period associated with a day of
                                          						the week during which night service is active. |
| night-service everyday | Defines a recurring night-service time period to be in
                                          						effect everyday. |
| night-service weekday | Defines a recurring night-service time period to be in
                                          						effect only on weekdays. |

| both | (Optional) Both the primary and secondary pilot numbers are
                                          						not registered. |
|---|---|
| pilot | (Optional) Only the primary pilot number is not registered. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.3(7)T | Cisco CME 3.1 | The both and pilot keywords were introduced. |

|  | Description |
|---|---|
| final | Defines the last ephone-dn in an ephone hunt group. |
| hops | Defines the number of times that a call is redirected to
                                          						the next ephone-dn in a peer ephone-hunt-group list before proceeding to the
                                          						final ephone-dn. |
| list | Defines the ephone-dns that participate in an ephone hunt
                                          						group. |
| max-redirect | Changes the current number of allowable redirects in a
                                          						Cisco CME system. |
| pilot | Defines the ephone-dn that is dialed to reach an ephone
                                          						hunt group. |
| preference (ephone-hunt) | Sets preference order for the ephone-dn associated with an
                                          						ephone-hunt-group pilot number. |
| timeout (ephone-hunt) | Sets the number of seconds after which a call that is not
                                          						answered is redirected to the next number in the hunt-group list. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

|  | Description |
|---|---|
| number (voice register dn) | Associates a telephone or extension number with a SIP phone
                                          						in a Cisco CME system. |

| milliseconds | Length of delay. Range: 10 to 200. Default: 200 ms. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| dtmf-interworking rtp-nte | Introduces a delay between the dtmf-digit begin and
                                          						dtmf-digit end events in RFC 2833 packets sent from the router. |
| ephone-template (ephone) | Applies a template to ephone being configured. |
| keypad-normalize | Ensures that the delay configured for a dtmf-end event is
                                          						always honored. |

| ip-address | IP address of the NTP server. |
|---|---|
| mode | (Optional) Enables the broadcast mode for the server. |
| anycast | Enables anycast mode. |
| directedbroadcast | Enables directed broadcast mode. |
| multicast | Enables multicast mode. |
| unicast | Enables unicast mode. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XJ | Cisco Unified CME 4.1 | This command was introduced. |
| 12.4(15)T | Cisco Unified CME 4.1 | This command was integrated into Cisco IOS Release
                                          						12.4(15)T. |

|  | Description |
|---|---|
| create profile | Generates the configuration profile files required for SIP
                                          						phones. |
| restart (voice register) | Performs a fast reset of one or all SIP phones associated
                                          						with a Cisco Unified CME router. |

| number | String of up to 16 characters that represents an E.164
                                          						telephone number. Normally the string is composed of digits, but the string may
                                          						contain alphabetic characters when the number is dialed only by the router, as
                                          						with an intercom number. One or more periods (.) can be used as wildcard
                                          						characters. For details, see “Usage Guidelines.” |
|---|---|
| secondary | (Optional) Associates the number that follows as an
                                          						additional number for this ephone-dn. |
| no-reg | (Optional) The E.164 numbers in the dial peer do not
                                          						register with the gatekeeper. If you do not specify an option
                                          						( both or primary ) after the no-reg keyword, only the secondary
                                          						number is not registered. |
| both | (Optional) Both primary and secondary numbers are not
                                          						registered. |
| primary | (Optional) Primary number is not registered. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco ITS 1.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |
| 12.2(15)ZJ | Cisco CME 3.0 | The ability to use alphabetic characters as part of the
                                          						number string was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

|  | Description |
|---|---|
| button | Associates ephone-dns with individual buttons on Cisco IP
                                          						phones and specifies ring behavior per button. |
| intercom | Creates an intercom by programming a pair of extensions
                                          						(ephone-dns) to automatically call and answer each other. |
| name | Configures a username associated with a directory number. |
| preference | Sets preference for the attached dial peer for a directory
                                          						number. |
| restart (ephone) | Performs a fast reboot of a single phone associated with a
                                          						Cisco CME router. |
| restart (telephony-service) | Performs a fast reboot of one or all phones associated with
                                          						a Cisco CME router. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 15.6(3)M 16.3.1 | Cisco
                                          						Unified CME 11.5 | This
                                          						command was introduced. |

| Command | Description |
|---|---|
| night-service bell (voice register
                                                							 pool) | Marks a
                                          						SIP phone to receive night-service bell notification when incoming calls are
                                          						received on voice register DNs that are marked for night service during
                                          						night-service time periods. |
| night-service code | Defines
                                          						a code to disable or reenable night service on IP phones. |
| night-service date | Defines
                                          						a recurring time period associated with a month and day during which night
                                          						service is active. |
| night-service day | Defines
                                          						a recurring time period associated with a day of the week during which night
                                          						service is active. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 15.6(3)M 16.3.1 | Cisco
                                          						Unified CME 11.5 | This
                                          						command was introduced. |

| Command | Description |
|---|---|
| night-service bell (voice register
                                                							 dn) | Marks a
                                          						voice register dn to send night-service bell notification to designated SIP
                                          						phones during night-service time periods. |
| night-service bell (voice register template) | Applies
                                          						a template to a pool configuration. |
| night-service code | Defines
                                          						a code to disable or reenable night service on IP phones. |
| night-service date | Defines
                                          						a recurring time period associated with a month and day during which night
                                          						service is active. |
| night-service day | Defines a recurring time period associated with a day of the week during which
                                          						night service is active. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 15.6(3)M 16.3.1 | Cisco
                                          						Unified CME 11.5 | This
                                          						command was introduced. |

| Command | Description |
|---|---|
| night-service bell (voice register
                                                							 dn) | Marks a
                                          						voice register dn to send night-service bell notification to designated SIP
                                          						phones during night-service time periods. |
| voice register pool | Applies
                                          						a template to a pool configuration. |
| night-service code | Defines
                                          						a code to disable or reenable night service on IP phones. |
| night-service date | Defines
                                          						a recurring time period associated with a month and day during which night
                                          						service is active. |
| night-service day | Defines a recurring time period associated with a day of the week during which
                                          						night service is active. |

| number | String
                                          						of up to 16 characters that represents an E.164 telephone number. Normally the
                                          						string is composed of digits, but the string may contain alphabetic characters
                                          						when the number is dialed only by the router, as with an intercom number. |
|---|---|

| Cisco
                                          						IOS Release | Version | Modification |
|---|---|---|
| 12.4(4)T | Cisco
                                          						CME 3.4 and Cisco SIP SRST 3.4 | This
                                          						command was introduced. |

| Note | This command
                                       		  can also be used for Cisco SIP SRST. |
|---|---|

|  | Description |
|---|---|
| reset (voice register global) | Performs a complete reboot of all SIP phones associated with a Cisco CME
                                          						router. |
| reset (voice register pool) | Performs a complete reboot of a single SIP phone associated with a Cisco CME
                                          						router. |

| tag | Telephone number when there are multiple number commands. Range is 1 to 114. |
|---|---|
| number-pattern | Phone numbers (including wild cards and patterns) that are
                                          						permitted by the registrar to handle the Register message from the Cisco
                                          						Unified SIP IP phone. |
| preference value | (Optional) Defines the number list preference order. Range
                                          						is 0 to 10. The highest preference is 0. There is no default. |
| huntstop | (Optional) Stops hunting when the dial peer is busy. |
| dn dn-tag | Identifies the directory number tag for this phone number
                                          						as defined by the voice register dn command. Range is 1 to 288. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SIP SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SIP SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was added to Cisco CME and the dn keyword was added. |
| 12.4(11)XJ | Cisco Unified CME 4.1 Cisco Unified SRST 4.1 | This command was modified. The number-pattern argument and preference and huntstop keywords were removed from
                                          						Cisco Unified CME. |
| 12.4(15)T | Cisco Unified CME 4.1 Cisco Unified SRST 4.1 | The modifications to this command were integrated into
                                          						Cisco IOS Release 12.4(15)T. |
| 15.2(4)M | Cisco Unified CME 9.1 Cisco Unified SIP SRST 9.1 | This command was modified to increase the valid value of
                                          						the tag argument to 114. |

| Note | Configure the id (voice register pool) command before any other voice register pool
                                       		  commands, including the number command. The id command identifies a locally available,
                                       		  individual Cisco Unified SIP IP phone or a set of Cisco Unified SIP IP phones. |
|---|---|

| Command | Description |
|---|---|
| id (voice register pool) | Explicitly identifies a locally available, individual Cisco
                                          						Unified SIP IP phone or, when running Cisco Unified SIP SRST, a set of Cisco
                                          						Unified SIP IP phones. |
| voice register dn | Enters voice register dn configuration mode to define an
                                          						extension for a phone line, intercom line, voice-mail port, or a
                                          						message-waiting indicator. |

| number | String of up to 16 characters that represents an E.164
                                          						telephone number to be associated with and displayed next to a line button on
                                          						an IP phone. This directory number must be already configured by using the number command in ephone-dn or
                                          						voice register dn configuration mode. |
|---|---|
| [ , ...number ] | (Optional) For overlay lines only, with or without call
                                          						waiting. Directory numbers to roll over to this line. Can contain up to 25
                                          						individual numbers separated by commas (,). This directory number must be
                                          						already configured by using the number command in ephone-dn or
                                          						voice register dn configuration mode. |
| type | Characteristics to be associated with this line button. |
| type | Word that describes characteristics to be associated with
                                          						the line button being configured. Valid entries are as follows: beep-ring feature-ring monitor-ring silent-ring overlay cw-overlay |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XW | Cisco Unified CME 4.2 | This command was introduced. |
| 12.4(15)XY | Cisco Unified CME 4.2(1) | This command was introduced. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Note | In Cisco IOS Release 12.4(4)XC and later releases, the silent
                                       		  ringing behavior is overridden during active night-service periods. Silent
                                       		  ringing does not apply during designated night-service periods when the s keyword is used. |
|---|---|

| Command | Description |
|---|---|
| logout-profile | Enables Cisco Unified IP phone for extension mobility and
                                          						assigns a logout profile to this phone. |
| reset (voice logout-profile and voice user-profile) | Performs a complete reboot of all IP phones to which a
                                          						particular logout-profile or user-profile is downloaded. |

| number | Number
                                          						of line buttons. Range: 1 to 100. Default: 0. See the table for the number of
                                          						buttons supported by each phone type. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco
                                          						Unified CME 4.3 Cisco Unified SRST 4.3 | This
                                          						command was introduced. |
| 12.4(20)T | Cisco
                                          						Unified CME 7.0 Cisco Unified SRST 7.0 | This
                                          						command was integrated into Cisco IOS Release 12.4(20)T. |

| Supported
                                          					 Device | device-id | device-type | num-buttons | max-presentation |
|---|---|---|---|---|
| Cisco
                                          					 Unified IP Phone 6901 | 547 | 6901 | 1 | 1 |
| Cisco
                                          					 Unified IP Phone 6911 | 548 | 6911 | 1 | 10 |
| Cisco
                                          					 Unified IP Phone 7915 Expansion Module with 12 buttons | 227 | 7915 | 12 | 0
                                          					 (default) |
| Cisco
                                          					 Unified IP Phone 7915 Expansion Module with 24 buttons | 228 | 7915 | 24 | 0 |
| Cisco
                                          					 Unified IP Phone 7916 Expansion Module with 12 buttons | 229 | 7916 | 12 | 0 |
| Cisco
                                          					 Unified IP Phone 7916 Expansion Module with 24 buttons | 230 | 7916 | 24 | 0 |
| Cisco
                                          					 Unified Wireless IP Phone 7925 | 484 | 7925 | 6 | 4 |
| Cisco
                                          					 Unified IP Conference Station 7937G | 431 | 7937 | 1 | 6 |
| Nokia
                                          					 E61 | 376 | E61 | 1 | 1 |

| Command | Description |
|---|---|
| device-id | Specifies the device ID for a phone type. |
| max-presentation | Sets
                                          						the number of call presentation lines supported by a phone type. |
| type | Assigns the phone type to an SCCP phone. |

| description | Specific
                                       					 the number of lines supported by the phone model. Range is 1-114. |
|---|---|

| Release | Cisco Product | Modification |
|---|---|---|
| 15.3(3)M | Cisco SIP
                                       					 CME 10.0 | This
                                       					 command was introduced. |

| Command | Description |
|---|---|
| voice register pool-type | Adds a new Cisco Unified SIP IP phone to Cisco Unified CME. |