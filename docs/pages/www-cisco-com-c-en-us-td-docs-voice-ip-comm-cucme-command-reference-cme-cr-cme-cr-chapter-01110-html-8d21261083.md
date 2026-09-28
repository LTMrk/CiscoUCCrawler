---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-command-reference-cme-cr-cme-cr-chapter-01110-html-8d21261083
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/command/reference/cme_cr/cme_cr_chapter_01110.html
retrieved_at: 2026-08-21T22:56:52.315575+00:00
---

Cisco Unified Communications Manager Express Command Reference

# Cisco Unified Communications Manager Express Command Reference

Updated: July 19, 2018

Chapter: Cisco Unified CME Commands: P

## Chapter: Cisco Unified CME Commands: P

# Cisco Unified CME Commands: P

## paging

To define an extension (ephone-dn) as a paging extension that can be
                              		  called to broadcast an audio page to a set of Cisco IP phones, use the paging command in ephone-dn configuration
                              		  mode. To disable this feature, use the no form of this command.

paging [ ip multicast-address port udp-port-number ]

no paging [ ip ]

### Syntax Description

ip multicast-address

(Optional) Uses an IP multicast address to multicast voice
                                          						packets for audio paging; for example, 239.0.1.1. Note that IP phones do not
                                          						support multicast at 224.x.x.x addresses. Default is that multicast is not used
                                          						and IP phones are paged individually using IP unicast transmission (up to ten
                                          						phones).

port udp-port-number

(Optional) Uses this UDP port for the multicast. Range is
                                          						from 2000 to 65535. Default is 2000.

### Command Default

No paging number is established.

### Command Modes

Ephone-dn configuration (config-ephone-dn)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(2)XT

Cisco ITS 2.0

This command was introduced.

12.2(8)T

Cisco ITS 2.0

This command was integrated into Cisco IOS Release
                                          						12.2(8)T.

### Usage Guidelines

To configure a set of phones to receive an audio page, follow these
                              		  steps:

- Use the paging command in ephone-dn configuration
                                 			 mode to define a number that people can dial to send a page. The following
                                 			 example defines a paging-dn tag (21) and extension number (34455) to dial to
                                 			 send a page.

```
ephone-dn 21
 paging 
 number 34455
```

- Use the paging-dn command in ephone configuration
                                 			 mode to assign the same paging-dn tag that you defined in Step 1 to all the
                                 			 phones that you want to receive the page. This set of phones is called a
                                 			 “paging set.” You can have more than one paging set in a Cisco CME system. The
                                 			 following example assigns the paging-dn tag from Step 1 (21) to two phones (3
                                 			 and 4) so that they will receive audio pages.

```
ephone 3
 paging-dn 21
ephone 4
 paging-dn 21
```

The paging command configures an ephone-dn as an
                              		  extension that people can dial to broadcast audio pages to a specified set of
                              		  idle Cisco IP phones. The extension associated with this command does not
                              		  appear on any ephone; it is a “dummy” extension. The dn-tag associated with
                              		  this extension becomes the paging-dn tag for this paging set.

When a person dials the number assigned to the dummy extension and
                              		  speaks into the phone, the audio stream is sent as a page to the paging set
                              		  (the set of all phones that have been configured with this paging-dn tag as an
                              		  argument to the paging-dn command). Idle phones in the paging
                              		  set automatically answer the paging call in one-way speakerphone mode. Paging
                              		  sets can be joined into a single combined paging group with the paging group command.

The optional ip keyword and multicast-address argument define a paging
                              		  multicast address for this paging set. If an IP multicast address is not
                              		  configured, IP phones are paged individually using IP unicast transmission (to
                              		  a maximum of ten IP phones). The recommended operation is with an IP multicast
                              		  address. When multiple paging-dn tags are configured using the paging command, each paging-dn tag should use
                              		  a unique IP multicast address.

Each ephone-dn and paging-dn tag that is used for paging can support
                              		  a maximum of ten distinct targets (IP addresses and interfaces). A multicast
                              		  address counts as a single target for each physical interface in use
                              		  (regardless of the number of phones connected via the interface). Paging using
                              		  a single IP multicast address that requires output on three different Ethernet
                              		  interfaces represents use of three counts out of the maximum ten. Each unicast
                              		  target counts as a single target, such that paging that does not use multicast
                              		  at all is limited to paging ten phones. For example, ten IP phones paged
                              		  through multicast on Fast Ethernet interface 0/1.1 plus five IP phones paged
                              		  through multicast on Fast Ethernet interface 0/1.2 are counted as two targets.

For simultaneous paging to more than one paging ephone-dn, Cisco
                              		  recommends that you use different IP multicast addresses (not just different
                              		  port numbers) for paging configuration.

## Examples

The following example creates a paging extension number that uses IP
                              		  multicast paging:

```
Router(config)# ephone-dn 20 Router(config-ephone-dn) number 2000 Router(config-ephone-dn) paging ip 239.0.1.1 port 2000
```

A more complete configuration example follows, in which paging sets
                              		  20 and 21 are created. Pages to extension 2000 are multicast to ephones 1 and
                              		  2. Pages to extension 2001 are multicast to ephones 3 and 4.

```
ephone-dn 1
 number 2345
ephone-dn 2
 number 2346
ephone-dn 3
 number 2347
ephone-dn 4
 number 2348
ephone-dn 20
 number 2000
 paging ip 239.0.1.20 port 2000
ephone-dn 21
 number 2001
 paging ip 239.0.1.21 port 2000
ephone 1
 button 1:1
 paging-dn 20
ephone 2
 button 1:2
 paging-dn 20
ephone 3
 button 1:3
 paging-dn 21
ephone 4
 button 1:4
 paging-dn 21
```

### Related Commands

Command

Description

paging-dn

Assigns audio paging reception capability to a Cisco IP
                                          						phone.

paging group

Combines two or more paging sets into a combined paging
                                          						group.

## paging group

To create a combined paging group from two or more previously
                              		  established paging sets, use the paging group command in ephone-dn configuration mode. To remove a paging
                              		  group, use the no form of this command.

paging group paging-dn-tag,
                                 				  paging-dn-tag...

no paging group

### Syntax Description

paging-dn-tag

Comma-separated list of paging-dn-tags (unique sequence
                                          						numbers associated with paging ephone-dns) that have previously been associated
                                          						with the paging extension of a paging set using the paging-dn or paging-dn (voice register) command. You can include up to ten paging-dn-tags
                                          						separated by commas. For example, 4, 6, 7, 8.

### Command Default

Paging is disabled on all Cisco IP phones.

### Command Modes

Ephone-dn configuration (config-ephone-dn)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(2)XT

Cisco ITS 2.0

This command was introduced.

12.2(8)T

Cisco ITS 2.0

This command was integrated into Cisco IOS Release
                                          						12.2(8)T.

15.2(2)T

Cisco Unifide CME 9.0

This command was modified to include voice register pools
                                          						in the ephone-dn and paging groups.

### Usage Guidelines

Use this command to combine previously defined sets of phones
                              		  associated with individual paging extensions (ephone-dns) into a combined group
                              		  to enable a single page to be sent to large numbers of phones at once. To
                              		  remove a paging group, use the no form of the command. All paging-dn tags
                              		  included in the list must have already been defined as paging-dns using the paging or paging-dn (voice register) command.

The use of paging groups not only allows phones to participate in a
                              		  small local paging set (for example, paging to four phones in a company’s
                              		  shipping and receiving department) but also supports company-wide paging when
                              		  needed (for example, by combining the paging sets for shipping and receiving
                              		  with the paging sets for accounting, customer support, and sales into a single
                              		  paging group).

## Examples

In the following example, paging sets 20 and 21 are defined and then
                              		  combined into paging group 22. Paging set 20 has a paging extension of 2000.
                              		  When someone dials extension 2000 to deliver a page, the page is sent to Cisco
                              		  IP phones (ephones) 1 and 2. Paging set 21 has a paging extension of 2001. When
                              		  someone dials extension 2001 to deliver a page, the page is sent to ephones 3
                              		  and 4. Paging group 22 combines sets 20 and 21, and when someone dials its
                              		  paging extension, 2002, the page is sent to all the phones in both sets and to
                              		  ephone 5, which is directly subscribed to the combined paging group.

```
ephone-dn 20
 number 2000
 paging ip 239.0.1.20 port 2000
ephone-dn 21
 number 2001
 paging ip 239.0.1.21 port 2000
ephone-dn 22
 number 2002
 paging ip 239.0.2.22 port 2000
 paging group 20,21
ephone 1
 button 1:1
 paging-dn 20
ephone 2
 button 1:2
 paging-dn 20
ephone 3
 button 1:3
 paging-dn 21
ephone 4
 button 1:4
 paging-dn 21
ephone 5
 button 1:5
 paging-dn 22
```

The following example shows how the paging group command is used to configure combined paging
                              		  groups composed of ephone and voice register directory numbers.

The first set of configuration tasks shows how to configure a
                              		  combined paging group composed of Cisco Unified SCCP IP phone directory numbers
                              		  only.

When extension 2000 is dialed, a page is sent to ephones 1 and 2
                              		  (first single paging group). When extension 2001 is dialed, a page is sent to
                              		  ephones 3 and 4 (second single paging group). Finally, when extension 2002 is
                              		  dialed, a page is sent to ephones 1, 2, 3, 4, and 5, producing the combined
                              		  paging group (composed of the first single paging group, the second single
                              		  paging group, and ephone 5).

Ephones 1 and 2 are included in paging ephone-dn 22 through the
                              		  membership of ephone-dn 20 as paging group 20 in the combined paging group.
                              		  Ephones 3 and 4 are included in paging ephone-dn 22 through membership of
                              		  ephone-dn 21 as paging group 21 in the combined paging group. Ephone 5 is
                              		  directly subscribed to paging-dn 22.

```
ephone-dn 20
 number 2000
 paging ip 239.0.1.20 port 20480
ephone-dn 21
 number 2001
 paging ip 239.1.1.21 port 20480
ephone-dn 22
 number 2002
 paging ip 239.1.1.22 port 20480
 paging group 20,21
ephone-dn 6
 number 1103
ephone-dn 7
 number 1104
ephone-dn 8
 number 1105
ephone-dn 9
 number 1199
ephone-dn 10
 number 1198
ephone 1
 mac-address 1234.8903.2941
 button 1:6
 paging-dn 20
ephone 2
 mac-address CFBA.321B.96FA
 button 1:7
 paging-dn 20
ephone 3
 mac-address CFBB.3232.9611
 button 1:8
 paging-dn 21
ephone 4
 mac-address 3928.3012.EE89
 button 1:9
 paging-dn 21
ephone 5
 mac-address BB93.9345.0031
 button 1:10
 paging-dn 22
```

The second set of configuration tasks shows how Cisco Unified SIP IP
                              		  phone directory numbers can be configured and added to the previously
                              		  established paging groups of the first set of configuration tasks to form a new
                              		  combined paging group composed of ephone and voice register directory numbers.

When extension 2000 is dialed, a page is sent to ephones 1 and 2 and
                              		  voice register pools 1 and 2 (new first single paging group). When extension
                              		  2001 is dialed, a page is sent to ephones 3 and 4 and voice register pools 3
                              		  and 4 (newsecond single paging group). Finally, when extension 2002 is dialed,
                              		  a page is sent to ephones 1, 2, 3, 4, and 5 and voice register pools 1, 2, 3,
                              		  4, and 5 (new combined paging group).

Ephones 1 and 2 and voice register pools 1 and 2 are included in
                              		  paging ephone-dn 22 through the membership of ephone-dn 20 as paging group 20
                              		  in the combined paging group. Ephones 3 and 4 and voice register pools 3 and 4
                              		  are included in paging ephone-dn 22 through membership of ephone-dn 21 as
                              		  paging group 21 in the combined paging group. Ephone 5 and voice register pool
                              		  5 are directly subscribed to paging-dn 22.

```
voice register dn 1
 number 1201
voice register dn 2
 number 1202
voice register dn 3
 number 1203
voice register dn 4
 number 1204
voice register dn 5
 number 1205
voice register pool 1
 id mac 0019.305D.82B8
 type 7961
 number 1 dn 1
 paging-dn 20
voice register pool  2
 id mac 0019.305D.2153
 type 7961
 number 1 dn 2
 paging-dn 20
voice register pool  3
 id mac 1C17.D336.58DB
 type 7961
 number 1 dn 3
 paging-dn 21
voice register pool  4
 id mac 0017.9437.8A60
 type 7961
 number 1 dn 4
 paging-dn 21
voice register pool  5
 id mac 0016.460D.E469
 type 7961
 number 1 dn 5
 paging-dn 22
```

### Related Commands

Command

Description

paging

Creates a paging extension (ephone-dn) that can be called
                                          						in order to broadcast an audio page to a group of Cisco IP phones.

paging-dn

Assigns a paging extension (paging-dn) to a Cisco IP phone.

paging-dn (voice register)

Registers a Cisco Unified SIP IP phone to an ephone-dn
                                          						paging directory number.

## paging-dn

To create a paging extension (paging-dn) to receive audio pages on a
                              		  Cisco Unified IP phone in a Cisco Unified CME system, use the paging-dn command in ephone or
                              		  ephone-template configuration mode. To disable this feature, use the no form of this command.

paging-dn paging-dn-tag { multicast | unicast }

paging-dn no

### Syntax Description

paging-dn-tag

Dn-tag of an ephone-dn that was designated as a paging
                                          						ephone-dn with the paging command.

multicast

Uses multicast if available. By default, audio paging is
                                          						transmitted to the Cisco Unified IP phone using multicast.

unicast

Forces unicast paging for this phone. This keyword
                                          						indicates that the Cisco Unified IP phone is not capable of receiving audio
                                          						paging through multicast and requests that all pages to this phone be sent
                                          						through unicast. The maximum number of phones supported through unicast is ten.

### Command Default

Paging is disabled on all Cisco Unified IP phones.

### Command Modes

Ephone configuration (config-ephone) Ephone-template configuration (config-ephone-template)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(2)XT

Cisco ITS 2.0

This command was introduced.

12.2(8)T

Cisco ITS 2.0

This command was integrated into Cisco IOS Release
                                          						12.2(8)T.

12.4(4)XC

Cisco Unified CME 4.0

This command was made available in ephone-template
                                          						configuration mode.

12.4(9)T

Cisco Unified CME 4.0

This command in ephone-template configuration mode was
                                          						integrated into Cisco IOS Release 12.4(9)T.

### Usage Guidelines

To configure a set of phones to receive an audio page, follow these
                              		  steps:

- Use the paging command in ephone-dn configuration
                                 			 mode to define a number that people can dial to send a page. The following
                                 			 example defines a paging-dn tag (21) and extension number (34455) to dial to
                                 			 send a page.

```
ephone-dn 21
 paging 
 number 34455
```

- Use the paging-dn command in ephone configuration
                                 			 mode to assign the same paging-dn tag that you defined in Step 1 to all the
                                 			 phones that you want to receive the page. This set of phones is called a
                                 			 “paging set.” You can have more than one paging set in a Cisco Unified CME
                                 			 system. The following example assigns the paging-dn tag from Step 1 (21) to two
                                 			 phones (3 and 4) so that they will receive audio pages.

```
ephone 3
 paging-dn 21
ephone 4
 paging-dn 21
```

This command creates a paging extension (paging-dn) associated with
                              		  an IP phone. Each phone can support only one paging-dn extension. This
                              		  extension does not occupy a phone button and is therefore not configured on the
                              		  phone with the button command. The paging-dn allows the
                              		  phone to automatically answer audio pages in one-way speakerphone mode. There
                              		  is no press-to-answer option as there is with an intercom extension.

The paging-dn-tag argument in this command takes
                              		  the value of the dn-tag of an extension (ephone-dn) that has been made a paging
                              		  ephone-dn using the paging command. This command is the extension
                              		  that callers dial to deliver an audio page. All of the phones that are going to
                              		  receive the same audio pages are configured with the same paging-dn-tag . These phones form a paging
                              		  set.

An IP phone can belong to only one paging set, but any number of
                              		  phones can belong to the same paging set using multicast. There can be any
                              		  number of paging sets in a Cisco Unified CME system, and paging sets can be
                              		  joined to create a combined paging group using the paging group command. For example, you may create separate
                              		  paging sets for each department (sales, support, shipping) and combine them
                              		  into a single combined paging group (all departments). Only single-level
                              		  grouping is supported (no support for groups of groups).

Normal phone calls that are received while an audio page is in
                              		  progress interrupt the page.

The paging mechanism supports audio distribution using IP multicast,
                              		  replicated unicast, and a mixture of both (so that multicast is used where
                              		  possible, and unicast is used with specific phones that cannot be reached
                              		  through multicast).

If you use an ephone template to apply a command to a phone and you
                              		  also use the same command in ephone configuration mode for the same phone, the
                              		  value that you set in ephone configuration mode has priority.

## Examples

The following example creates paging number 5001 on ephone-dn 22 and
                              		  adds ephone 4 as a member of the paging set. Multicast is set for the
                              		  paging-dn. Note that IP phones do not support multicast at 224.x.x.x addresses.

```
ephone-dn 1
 number 5123
ephone-dn 22
 name Paging Shipping
 number 5001
 paging ip 239.1.1.10 port 2000
ephone 4
 mac-address 0030.94c3.8724
 button 1:1
 paging-dn 22 multicast
```

### Related Commands

Description

ephone-template (ephone)

Applies a template to an ephone configuration.

number

Configures a valid number for the Cisco Unified IP phone.

paging

Creates a paging extension (ephone-dn) that can be called
                                          						in order to broadcast an audio page to a group of Cisco Unified IP phones.

paging group

Combines two or more paging sets into a combined paging
                                          						group.

## paging-dn (voice register)

To register a Cisco Unified SIP IP phone to an ephone-dn paging
                              		  directory number (DN), use the paging-dn command in voice register pool or
                              		  voice register template configuration mode. To unregister the Cisco Unified SIP
                              		  IP phone from the paging directory number, use the no form of this command.

paging-dn paging-dn-tag { multicast | unicast }

no paging-dn

### Syntax Description

paging-dn-tag

Ephone-dn tag designated as the paging ephone-dn to which a
                                          						Cisco Unified SIP IP phone is registered.

multicast

Transmits audio paging to the Cisco Unified IP phone using
                                          						multicast. This is the default.

unicast

Transmits audio paging to the Cisco Unified IP phone using
                                          						unicast.This indicates that the Cisco Unified IP phone is not capable of
                                          						receiving audio paging through multicast and requests that all pages to this
                                          						phone be sent through unicast. The maximum number of phones supported through
                                          						unicast is 12.

### Command Default

The Cisco Unified SIP IP phone is not registered to an ephone-dn
                              		  paging DN and paging is disabled.

### Command Modes

Voice register pool configuration (config-register-pool)

Voice register template configuration (config-register-temp)

## Command History

Release

Modification

15.2(2)T

This command was introduced.

### Usage Guidelines

The paging-dn command applies to both voice
                              		  register pool and voice register template configuration modes. When voice
                              		  register pool is configured with the template and paging is configured in voice
                              		  register pool configuration mode, paging in voice register pool configuration
                              		  mode has higher precedence over paging in voice register template configuration
                              		  mode.

The correct paging port for the paging-dn of Cisco Unified SIP IP
                              		  phones in the paging command is an even number from 20480
                              		  to 32768. If you enter a wrong port number, a SIP REFER message request is sent
                              		  to the IP phone but the Cisco Unified SIP IP phone is not paged.

## Examples

The following example shows how the Cisco Unified 7961 SIP IP phone
                              		  is registered to both paging-dns 251 and 252:

```
ephone-dn  2  dual-line
 number 60012
ephone-dn  250
number 7770
 paging ip 239.1.1.0 port 20480
 paging group 251,252
ephone-dn  251
 number 7771
 paging ip 239.1.1.1 port 20480
ephone-dn  252
 number 7772
 paging ip 239.1.1.2 port 20480
 
ephone-dn  253
 number 7773
 paging ip 239.1.1.3 port 20480
ephone  2
 mac-address 001E.4A91.F27D
 paging-dn 252
 type 7961
 button  1:2
voice register dn  1
 number 60001
voice register dn  2
 number 60002
voice register pool  1
 id mac 0019.305D.82B8
 type 7961
 number 1 dn 1
 codec g711ulaw
 paging-dn 251
voice register pool  2
 id mac 0019.305D.2153
 type 7961
 number 1 dn 2
 codec g711ulaw
 paging-dn 252
```

### Related Commands

Command

Description

paging-dn

Creates a paging extension to receive audio pages on a
                                          						Cisco Unified SCCP IP phone in a Cisco Unified CME system.

paging group

Creates a combined paging group from two or more previously
                                          						established paging sets.

## param

To load and configure parameters in a package or a service
                              		  (application) on the gateway, use the param command in application configuration
                              		  mode. To reset a parameter to its default value, use the no form of this command.

param param-name [ param max-retries | param passwd | param passwd-prompt filename | param user-prompt filename | param term-digit | param abort-digit | param max-digits ]

no param param-name

### Syntax Description

param-name

Name of the parameter.

param max-retries

(Optional) Number of attempts to re-enter account or
                                          						password. Value ranges from 0-10, default value is 0.

param passwd

(Optional) Character string that defines a predefined
                                          						password for authorization.

param passwd-prompt filename

(Optional) Announcement URL to request password input.
                                          						filename defines the name and location of the audio filename to be used for
                                          						playing the password prompt.

param user-prompt filename

(Optional) Announcement URL to request authorization code
                                          						username. filename defines the name and location of the audio filename to be
                                          						used for playing the username prompt.

param term-digit

Digit for terminating username or password digit input.

param abort-digit

Digit for aborting username or password digit input.
                                          						Default value is *.

param max-digits

Maximum number of digits in a username or password. Range
                                          						of valid value: 1 - 32. Default value is 32.

### Command Default

No default behavior or value.

### Command Modes

Application configuration

## Command History

Release

Modification

12.3(14)T

This command was introduced.

15.1(3)T

This command was modified. The following keywords and
                                          						arguments were added: param max-retries, param passwd, param passwd-prompt
                                          						filename, param user-prompt filename, param term-digit, param max-digit.

### Usage Guidelines

Use this command in application parameter configuration mode to
                              		  configure parameters in a package or service. A package is a linkable set of C
                              		  or Tcl functions that provide functionality invoked by applications or other
                              		  packages. A service is a standalone application.

The parameters available for configuration differ depending on the
                              		  package or service that is loaded on the gateway. The param register Tcl command in a service or package
                              		  registers a parameter and provides a description and default values which allow
                              		  the parameter to be configured using the CLI. The param register command is executed when the service or
                              		  package is loaded or defined, along with commands such as package provide , which register the capability of the
                              		  configured module and its associated scripts. You must configure and load the
                              		  Tcl scripts for your service or package and load the package in order to
                              		  configure its parameters. See the Tcl IVR API Version 2.0 Programming Guide for more information.

When a package or service is defined on the gateway, the parameters
                              		  in that package or service become available for configuration when you use this
                              		  command. Additional arguments and keywords are available for different
                              		  parameters. To see a list of available parameters, enter param ?.

To avoid problems with applications or packages using the same
                              		  parameter names, the parameter namespace, or parameterspace concept is introduced. When a service or a
                              		  package is defined on the gateway, its parameter namespace is automatically
                              		  defined. This is known as the service or package’s local parameterspace, or
                              		  “myparameterspace.” When you use this command to configure a service or
                              		  package’s parameters, the parameters available for configuration are those
                              		  contained in the local parameterspace. If you want to use parameter definitions
                              		  found in different parameterspace, you can use the paramspace parameter-namespace command to map the package’s
                              		  parameters to a different parameterspace. This allows that package to use the
                              		  parameter definitions found in the new parameterspace, in addition to its local
                              		  parameterspace.

Use this command in Cisco Unified Communication Manager Express 8.5
                              		  and later versions to define the username and password parameters to
                              		  authenticate packages for Forced Authorization Code (FAC)

When a predefined password is entered using the param passwd keyword,
                              		  callers are not requested to enter a password. You must define a filename for
                              		  user-prompt to play an audio prompt requesting the caller to enter a valid
                              		  username (in digits) for authorization. Similarly, you must define a filename
                              		  for passwd-prompt to play an audio prompt requesting the caller to enter a
                              		  valid password (in digits) for authorization.

## Examples

The following example shows how to configure a parameter in the
                              		  httpios package:

```
application
package httpios
param paramA value4
```

### Related Commands

Command

Description

call application voice

Defines the name of a voice application and specify the
                                          						location of the Tcl or VoiceXML document to load for this application.

param account-id-method

Configures an application to use a particular method to
                                          						assign the account identifier.

param convert-discpi-after-connect

Enables or disables conversion of a DISCONNECT message with
                                          						Progress Indicator set to PROG_INBAND (PI=8) to a regular DISCONNECT message
                                          						when the call is in the active state.

param event-log

Enables or disables logging for linkable Tcl functions
                                          						(packages).

param language

Configures the language parameter in a service or package
                                          						on the gateway.

param mode

Configures the call transfer mode for a package.

param pin-len

Defines the number of characters in the personal
                                          						identification number (PIN) for an application.

param redirect-number

Defines the telephone number to which a call is
                                          						redirected—for example, the operator telephone number of the service
                                          						provider—for an application.

param reroutemode

Configures the call transfer reroutemode (call forwarding)
                                          						for a package.

param retry-count

Defines the number of times a caller is permitted to
                                          						reenter the PIN for a designated application and passes that information to the
                                          						application.

param security

Configures security for linkable Tcl functions (packages).

paramspace

Enables an application to use parameters from the local
                                          						parameter space of another application.

param uid-length

Defines the number of characters in the UID for a package.

param warning-time

Defines the number of seconds of warning that a user
                                          						receives before the allowed calling time expires.

## param aa-hunt

To declare a Cisco Unified CME B-ACD menu number and associate it
                              		  with the pilot number of an ephone hunt group, use the param aa-hunt command in application-parameter configuration mode. To remove the menu
                              		  number and the ephone hunt group pilot number, use the no form of this command.

param aa-hunt menu-number pilot-number

no param aa-hunt menu-number pilot-number

### Syntax Description

menu-number

Number that callers must dial to reach the pilot number of
                                          						an ephone hunt group. The range is from 1 to 10. The default is 1.

pilot-number

Ephone hunt group pilot number.

### Command Default

Menu number 1 is configured, but it is not associated with a pilot
                              		  number .

### Command Modes

Application-parameter configuration (config-app-param)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)XC

Cisco CME 3.3

This command was introduced to replace the call application voice aa-hunt command.

### Usage Guidelines

This command is used with Cisco Unified CME Basic Automatic Call
                              		  Distribution and Auto-Attendant (B-ACD) service. It is configured under the service command for the call-queue script.

Up to ten aa-hunt menu options, or hunt groups, are allowed per
                              		  call-queue service. You can use any of the allowable numbers in any order.

This command associates a menu option with the pilot number of an
                              		  ephone hunt group. When a caller presses the digit of a menu option that has
                              		  been associated with an ephone hunt group using this command, the call is
                              		  routed to the pilot number of the hunt group.

Menu options for B-ACD services can be set up in many ways. For more
                              		  information, see the Cisco Unified CallManager Express B-ACD and Tcl Call-Handling
                                 			 Applications document for your release.

The highest aa-hunt number that you establish using this command also
                              		  automatically maps to zero (0) and can therefore be used to represent operator
                              		  services to your callers. In the following example, callers can dial either 8
                              		  or 0 to reach aa-hunt8, the hunt group with the pilot number 8888.

```
application
 service queue flash:
  param aa-hunt1 1111
  param aa-hunt3 3333
  param aa-hunt8 8888
```

For any configuration changes to take effect, you must reload the
                              		  Cisco Unified CME B-ACD scripts.

## Examples

The following example configures a call-queue service called queue to
                              		  associate three menu numbers with three pilot numbers of three ephone hunt
                              		  groups:

- Pilot number 1111 for ephone hunt group 1 (sales)

- Pilot number 2222 for ephone hunt group 2 (customer service)

- Pilot number 3333 for ephone hunt group 3 (operator)

If a caller presses 2 for customer service, the call is transferred
                              		  to 2222 and then is sent to the next available ephone-dn from the group of
                              		  ephone-dns assigned to ephone hunt group 1: 2001, 2002, 2003, 2004, 2005, and
                              		  2006. The sequencing of ephone-dns within a hunt group is handled by the ephone
                              		  hunt group itself, not by the B-ACD service. (Note that the configuration for
                              		  ephone hunt groups used with Cisco Unified CME B-ACD services do not use the final command.)

```
ephone-hunt 1 peer
 pilot 1111
 list 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010
ephone-hunt 2 peer
 pilot 2222
 list 2001, 2002, 2003, 2004, 2005, 2006
ephone-hunt 3 peer
 pilot 3333
 list 3001, 3002, 3003, 3004
application
 service queue flash:
  param aa-hunt1 1111
  param aa-hunt2 2222
  param aa-hunt3 3333
.
.
.
```

### Related Commands

Description

application

Enters application configuration mode.

service

Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application.

## param aa-pilot

To assign a pilot number to a Cisco Unified CME B-ACD automated
                              		  attendant (AA) service, use the param aa-pilot command in application-parameter configuration mode. To remove the AA
                              		  pilot number, use the no form of this command.

param aa-pilot aa-pilot-number

no param aa-pilot aa-pilot-number

### Syntax Description

aa-pilot-number

Telephone number that callers dial in order to reach this
                                          						AA service.

### Command Default

Cisco Unified CME B-ACD menu number 1 is configured, but it has no
                              		  pilot number .

### Command Modes

Application-parameter configuration (config-app-param)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(14)T

Cisco CME 3.3

This command was introduced to replace the call application voice aa-pilot command.

### Usage Guidelines

This command is used with the Cisco Unified CME Basic Automatic Call
                              		  Distribution and Auto-Attendant (B-ACD) service. Each AA has one AA pilot
                              		  number, although there may be more than one AA used with a B-ACD service.

For any configuration changes to take effect, you must reload the
                              		  Cisco Unified CME B-ACD scripts.

For more information, see the Cisco Unified CallManager Express B-ACD and Tcl Call-Handling
                                 			 Applications document for your release.

## Examples

The following example sets up a B-ACD with two AAs, both in
                              		  drop-through mode. The first AA is called acdaa and it has an AA pilot number
                              		  of (800) 555-0121. The second AA is aa-bcd and has an AA pilot number of (800)
                              		  555-0123. Both AAs use the call-queue service named callq. Incoming POTS dial
                              		  peers are established for both AA pilot numbers.

```
dial-peer voice 1010 pots 
 service acdaa 
 port 1/1/0 
 incoming called-number 8005550121
dial-peer voice 1020 pots 
 service aa-bcd 
 port 1/1/1 
 incoming called-number 8005550123
.
.
.
application 
 service callq tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd.tcl
  param queue-manager-debugs 1
  param aa-hunt1 5071
  param aa-hunt2 5072
  param number-of-hunt-grps 2
  param queue-len 10
!
 service acdaa tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl
  paramspace english location tftp://192.168.254.254/user1/prompts/ 
  paramspace english index 0
  paramspace english language en
  param aa-pilot 8005550121
  param service-name callq
  param max-time-vm-retry 2
  param voice-mail 5007
  param call-retry-timer 20
  param number-of-hunt-grps 1
  param drop-through-prompt _bacd_welcome.au
  param drop-through-option 2
  param second-greeting-time 45
  param handoff-string acdaa
  param max-time-call-retry 360
!
 service aa-bcd tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl
  paramspace english location tftp://192.168.254.254/user1/prompts/ 
  paramspace english index 0
  paramspace english language en
  param aa-pilot 8005550123
  param service-name callq
  param second-greeting-time 60
  param max-time-call-retry 180
  param max-time-vm-retry 2
  param voice-mail 5007
  param call-retry-timer 5
  param handoff-string aa-bcd
  param drop-through-option 1
  param number-of-hunt-grps 1
```

### Related Commands

Description

application

Enters application configuration mode.

service

Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application.

## param call-retry-timer

To specify the time interval before each attempt to retry to connect
                              		  a call to an ephone hunt group used with a Cisco CME B-ACD service, use the param call-retry-timer command in application-parameter configuration mode. To return to the
                              		  default, use the no form of this command.

param call-retry-timer seconds

no param call-retry-timer seconds

### Syntax Description

seconds

Time that a call must wait before attempting or
                                          						reattempting to transfer a call to an ephone hunt group pilot number, in
                                          						seconds. Range is from 5 to 30 seconds.

### Command Default

Default is 15 seconds.

### Command Modes

Application-parameter configuration (config-app-param)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(14)T

Cisco CME 3.3

This command was introduced to replace the call application voice call-retry-timer command.

### Usage Guidelines

This command is used with Cisco Unified CME Basic Automatic Call
                              		  Distribution and Auto-Attendant (B-ACD) service. This command is configured
                              		  under the service command for an AA service. A Cisco
                              		  Unified CME B-ACD service can have more than one AA, and each AA can specify a
                              		  different interval for retries to connect to ephone hunt group phones.

For any configuration changes to take effect, you must reload the
                              		  Cisco Unified CME B-ACD scripts.

For more information, see the Cisco Unified CallManager Express B-ACD and Tcl Call-Handling
                                 			 Applications document for your release.

## Examples

The following example sets up a B-ACD with two AAs. The first AA is
                              		  called acdaa and it has an AA pilot number of (800) 555-0121. The second AA is
                              		  aa-bcd and has an AA pilot number of (800) 555-0123. Both AAs use the
                              		  call-queue service named callq. The first AA has a call-retry timer set to 10
                              		  seconds, and the second AA has a call-retry timer set to 5 seconds.

```
dial-peer voice 1010 pots 
 service acdaa 
 port 1/1/0 
 incoming called-number 8005550121
dial-peer voice 1020 pots 
 service aa-bcd 
 port 1/1/1 
 incoming called-number 8005550123
.
.
.
application 
 service callq tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd.tcl
  param queue-manager-debugs 1
  param aa-hunt1 5071
  param aa-hunt2 5072
  param number-of-hunt-grps 2
  param queue-len 10
!
 service acdaa tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl
  paramspace english location tftp://192.168.254.254/user1/prompts/ 
  paramspace english index 0
  paramspace english language en
  param aa-pilot 8005550121
  param service-name callq
  param max-time-vm-retry 2
  param voice-mail 5007
  param call-retry-timer 10
  param number-of-hunt-grps 1
  param drop-through-prompt _bacd_welcome.au
  param drop-through-option 2
  param second-greeting-time 45
  param handoff-string acdaa
  param max-time-call-retry 60
!
 service aa-bcd tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl
  paramspace english location tftp://192.168.254.254/user1/prompts/ 
  paramspace english index 0
  paramspace english language en
  param aa-pilot 8005550123
  param service-name callq
  param second-greeting-time 60
  param max-time-call-retry 180
  param max-time-vm-retry 2
  param voice-mail 5007
  param call-retry-timer 5
  param handoff-string aa-bcd
  param drop-through-option 1
  param number-of-hunt-grps 1
```

### Related Commands

Description

application

Enters application configuration mode.

service

Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application.

## param co-did-max

To set the upper boundary of the range of valid digits coming from
                              		  the PSTN Central Office (CO) for use with the Direct Inward Dial (DID) Digit
                              		  Translation Service, use the param co-did-max command in application-parameter
                              		  configuration mode. To disable this option, use the no form of this command.

param co-did-max max-co-value

no param co-did-max max-co-value

### Syntax Description

max-co-value

Maximum value of digits coming from the CO. The digit
                                          						string can be any length, but the string length must be the same in the param co-did-min , param co-did-max , param store-did-min , and param store-did-max commands.

### Command Default

No maximum value is defined for the range of digits coming from the CO.

### Command Modes

Application-parameter configuration (config-app-param)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)XC

Cisco Unified CME 4.0

This command was introduced to replace the call application voice co-did-max command.

12.4(9)T

Cisco Unified CME 4.0

This command replaced the call application voice co-did-max command and was integrated into Cisco IOS Release
                                          						12.4(9)T.

### Usage Guidelines

This command defines the upper limit of the range of digits accepted
                              		  from the CO when it is used with the Cisco Unified CallManager Express (Cisco
                              		  Unified CME) DID Digit Translation Service. This service provides number
                              		  translation for DID calls when the range of DID digits provided by the PSTN
                              		  Central Office (CO) does not match the digits in the Cisco Unified CME
                              		  extension numbers.

The Tcl script that provides the service accepts PSTN DID numbers of
                              		  any length and maps them to the internal extension numbers that are assigned by
                              		  a system administrator. Where necessary, a prefix is appended to the DID digits
                              		  to create a valid extension number. The script uses the parameters that you
                              		  input to determine the valid range of digits to be accepted from the CO, the
                              		  valid range of digits in the local dial plan, and the prefix to append, if
                              		  necessary. The script also handles DID calls that map to invalid extension
                              		  numbers: a prompt is played and the calls are disconnected.

## Examples

The following example configures DID Digit Translation Service on the
                              		  Cisco Unified CME router. It sets a lower boundary of 00 and an upper boundary
                              		  of 79 for the valid range of digits coming from the CO.

```
application
 service didapp tftp://192.168.254.254/scripts/did/app-THD-DID-2.0.0.1.tcl
  paramspace english index 1
  paramspace english language en
  paramspace english location tftp://192.168.254.254/apps/dir25/
  param secondary-prefix 4
  param did-prefix 5
  param co-did-min 00
  param co-did-max 79
  param store-did-min 00
  param store-did-max 79
```

### Related Commands

Description

application

Enters application configuration mode.

service

Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application.

param co-did-min

Sets the lower boundary of the range of valid digits coming
                                          						from the PSTN Central Office (CO) that is used with the DID Digit Translation
                                          						Service.

param store-did-max

Sets the upper boundary of the range of digits that is
                                          						valid in the Cisco Unified CME numbering plan that is used with the DID Digit
                                          						Translation Service.

param store-did-min

Sets the lower boundary of the range of digits that is
                                          						valid in the Cisco Unified CME numbering plan that is used with the DID Digit
                                          						Translation Service.

## param co-did-min

To set the lower boundary of the range of valid digits coming from
                              		  the PSTN Central Office (CO) that is used with the Direct Inward Dial (DID)
                              		  Digit Translation Service, use the param co-did-min command in application-parameter
                              		  configuration mode. To disable this option, use the no form of this command.

param co-did-min min-co-value

no param co-did-min min-co-value

### Syntax Description

min-co-value

Minimum value of digits coming from the CO. The digit
                                          						string can be any length, but the string length must be the same in the param co-did-max , param co-did-max , param store-did-min , and param store-did-max commands.

### Command Default

No minimum value is defined for the range of digits coming from the CO.

### Command Modes

Application-parameter configuration (config-app-param)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)XC

Cisco Unified CME 4.0

This command was introduced to replace the call application voice co-did-min command.

12.4(9)T

Cisco Unified CME 4.0

This command replaced the call application voice co-did-min command and was integrated
                                          						into Cisco IOS Release 12.4(9)T.

### Usage Guidelines

This command defines the upper limit of the range of digits accepted
                              		  from the CO when it is used with the Cisco Unified CallManager Express (Cisco
                              		  Unified CME) DID Digit Translation Service. This service provides number
                              		  translation for DID calls when the range of DID digits provided by the PSTN
                              		  Central Office (CO) does not match the digits in the Cisco Unified CME
                              		  extension numbers.

The Tcl script that provides the service accepts PSTN DID numbers of
                              		  any length and maps them to the internal extension numbers that are assigned by
                              		  a system administrator. Where necessary, a prefix is appended to the DID digits
                              		  to create a valid extension number. The script uses the parameters that you
                              		  input to determine the valid range of digits to be accepted from the CO, the
                              		  valid range of digits in the local dial plan, and the prefix to append, if
                              		  necessary. The script also handles DID calls that map to invalid extension
                              		  numbers: a prompt is played and the calls are disconnected.

## Examples

The following example configures DID Digit Translation Service on the
                              		  Cisco Unified CME router. It sets a lower boundary of 00 and an upper boundary
                              		  of 79 for the valid range of digits coming from the CO.

```
application
 service didapp tftp://192.168.254.254/scripts/did/app-THD-DID-2.0.0.1.tcl
  paramspace english index 1
  paramspace english language en
  paramspace english location tftp://192.168.254.254/apps/dir25/
  param secondary-prefix 4
  param did-prefix 5
  param co-did-min 00
  param co-did-max 79
  param store-did-min 00
  param store-did-max 79
```

### Related Commands

Description

application

Enters application configuration mode.

service

Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application.

param co-did-max

Sets the upper boundary of the range of valid digits coming
                                          						from the PSTN Central Office (CO) that is used with the DID Digit Translation
                                          						Service.

param store-did-max

Sets the upper boundary of the range of digits that is
                                          						valid in the Cisco Unified CME numbering plan that is used with the DID Digit
                                          						Translation Service.

param store-did-min

Sets the lower boundary of the range of digits that is
                                          						valid in the Cisco Unified CME numbering plan that is used with the DID Digit
                                          						Translation Service.

## param dial-by-extension-option

To assign a menu number to an Cisco CME B-ACD option by which callers
                              		  can directly dial known extension numbers, use the param dial-by-extension-option command in
                              		  application-parameter configuration mode. To disable this option, use the no form of this command.

param dial-by-extension-option menu-number

no param dial-by-extension-option menu-number

### Syntax Description

menu-number

Menu option number to be associated with the
                                          						dial-by-extension option. Range is from 1 to 9. There is no default.

### Command Default

Dial-by-extension option is not assigned.

### Command Modes

Application-parameter configuration (config-app-param)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(14)T

Cisco CME 3.3

This command was introduced to replace the call application voice dial-by-extension-option command.

### Usage Guidelines

This command is used with the Cisco Unified CME Basic Automatic Call
                              		  Distribution and Auto-Attendant (B-ACD) service. This command is configured
                              		  under the service command for an AA service.

This command allows you to designate a menu option number for callers
                              		  to press if they want to dial an extension number that they already know. This
                              		  command also enables the playing of the en_bacd_enter_dest.au audio file after
                              		  a caller presses the dial-by-extension menu number. The default announcement in
                              		  this audio file is “Please enter the extension number you want to reach.”

For any configuration changes to take effect, you must reload the
                              		  Cisco Unified CME B-ACD scripts.

For more information, see the Cisco Unified CallManager Express B-ACD and Tcl Call-Handling
                                 			 Applications document for your release.

## Examples

The following example sets up a B-ACD with an AA called acd1, which
                              		  has an AA pilot number of (800) 555-0121. The call-queue service used with this
                              		  AA is named callq. Callers to (800) 555-0121 can press 1 to dial an extension
                              		  number ( param dial-by-extension-option 1 under service acd1 ) or press 2 to be connected to the hunt group
                              		  with the pilot number 5072 ( param aa-hunt2 5072 under service callq ).

```
dial-peer voice 1010 pots 
 service acd1 
 port 1/1/0 
 incoming called-number 8005550121
.
.
.
application 
 service callq tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd.tcl
  param queue-manager-debugs 1
  param aa-hunt2 5072
  param number-of-hunt-grps 1
  param queue-len 10
!
 service acd1 tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl
  paramspace english location tftp://192.168.254.254/user1/prompts/ 
  paramspace english index 0
  paramspace english language en
  param handoff-string acd1
  param service-name callq
  param aa-pilot 8005550121
  param number-of-hunt-grps 1
  param dial-by-extension-option 1
  param second-greeting-time 45
  param call-retry-timer 20
  param max-time-call-retry 360
  param max-time-vm-retry 2
  param voice-mail 5007
```

### Related Commands

Description

application

Enters application configuration mode.

service

Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application.

## param did-prefix

To set a prefix to add to digits coming from the PSTN Central Office
                              		  (CO) to create valid extension numbers when using the Direct Inward Dial (DID)
                              		  Digit Translation Service, use the param did-prefix command in application-parameter
                              		  configuration mode. To disable this option, use the no form of this command.

param did-prefix did-prefix

no param did-prefix did-prefix

### Syntax Description

did-prefix

Prefix to add. Range is from 0 to 99.

### Command Default

No prefix is defined.

### Command Modes

Application-parameter configuration (config-app-param)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)XC

Cisco Unified CME4.0

This command was introduced to replace the call application voice did-prefix command .

12.4(9)T

Cisco Unified CME4.0

This command replaced the call application voice did-prefix command and was integrated into Cisco IOS Release
                                          						12.4(9)T.

### Usage Guidelines

This command is used with the Cisco Unified CallManager Express
                              		  (Cisco Unified CME) DID Digit Translation Service, which provides number
                              		  translation for DID calls when the range of DID digits provided by the PSTN
                              		  Central Office (CO) does not match the digits in the Cisco Unified CME
                              		  extension numbers.

The Tcl script that provides the service accepts PSTN DID numbers of
                              		  any length and maps them to the internal extension numbers that are assigned by
                              		  a system administrator. Where necessary, a prefix is appended to the DID digits
                              		  to create a valid extension number. The script uses the parameters that you
                              		  input to determine the valid range of digits to be accepted from the CO, the
                              		  valid range of digits in the local dial plan, and the prefix to append, if
                              		  necessary. The script also handles DID calls that map to invalid extension
                              		  numbers: a prompt is played and the calls are disconnected.

## Examples

The following example configures DID Digit Translation Service on the
                              		  Cisco Unified CME router. It specifies that a prefix of 5 should be applied to
                              		  the digits coming from the CO in order to construct a valid extension number.

```
application
 service didapp tftp://192.168.254.254/scripts/did/app-THD-DID-2.0.0.1.tcl
  paramspace english index 1
  paramspace english language en
  paramspace english location tftp://192.168.254.254/apps/dir25/
  param secondary-prefix 4
  param did-prefix 5
  param co-did-min 00
  param co-did-max 79
  param store-did-min 00
  param store-did-max 79
```

### Related Commands

Description

application

Enters application configuration mode.

service

Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application.

## param drop-through-option

To assign the drop-through option to a Cisco Unified CME B-ACD
                              		  auto-attendant (AA) application, use the param drop-through option command in application-parameter
                              		  configuration mode. To disable this option, use the no form of this command.

param drop-through-option menu-number

no param drop-through-option menu-number

### Syntax Description

menu-number

Menu option number (aa-hunt number) to be associated with
                                          						the drop-through option.

### Command Default

Drop-through option is not assigned.

### Command Modes

Application-parameter configuration (config-app-param)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(14)T

Cisco CME 3.3

This command was introduced to replace the call application voice drop-through-option command.

### Usage Guidelines

This command is used with the Cisco Unified CME Basic Automatic Call
                              		  Distribution and Auto-Attendant (B-ACD) service. This command is configured
                              		  under the service command for an AA service.

When an AA is configured for drop-through mode, the AA sends incoming
                              		  calls directly to the call queue associated with the menu number specified in
                              		  this command. Once in the queue, a caller hears ringback if an agent is
                              		  available or music on hold (MOH) if all agents are busy. If a greeting prompt
                              		  for drop-through mode is configured using the param drop-through-prompt command, a caller hears the
                              		  prompt before being sent to the queue as described.

The menu option number is an aa-hunt number that is associated with
                              		  an ephone hunt group using the param aa-hunt command.

For any configuration changes to take effect, you must reload the
                              		  Cisco Unified CME B-ACD scripts.

For more information, see the Cisco Unified CallManager Express B-ACD and Tcl Call-Handling
                                 			 Applications document for your release.

## Examples

The following example sets up a B-ACD with two AAs, both in
                              		  drop-through mode. The first AA is called acdaa and it has an AA pilot number
                              		  of (800) 555-0121. The second AA is aa-bcd and has an AA pilot number of (800)
                              		  555-0123. Both AAs use the call-queue service named callq. Callers to (800)
                              		  555-0121 drop directly through to the hunt group with the pilot number 5072
                              		  after hearing the greeting prompt in the audio file named en_dto_welcome.au.
                              		  Callers to (800) 555-0123 drop directly through to the hunt group with the
                              		  pilot number 5071 without hearing any greeting.

```
dial-peer voice 1010 pots 
 service acdaa 
 port 1/1/0 
 incoming called-number 8005550121
dial-peer voice 1020 pots 
 service aa-bcd 
 port 1/1/1 
 incoming called-number 8005550123
.
.
.
application 
 service callq tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd.tcl
  param queue-manager-debugs 1
  param aa-hunt1 5071
  param aa-hunt2 5072
  param number-of-hunt-grps 2
  param queue-len 10
!
 service acdaa tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl
  paramspace english location tftp://192.168.254.254/user1/prompts/ 
  paramspace english index 0
  paramspace english language en
  param aa-pilot 8005550121
  param service-name callq
  param max-time-vm-retry 2
  param voice-mail 5007
  param call-retry-timer 20
  param number-of-hunt-grps 1
  param drop-through-prompt _bacd_dto_welcome.au
  param drop-through-option 2
  param second-greeting-time 45
  param handoff-string acdaa
  param max-time-call-retry 360
!
 service aa-bcd tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl
  paramspace english location tftp://192.168.254.254/user1/prompts/ 
  paramspace english index 0
  paramspace english language en
  param aa-pilot 8005550123
  param service-name callq
  param second-greeting-time 60
  param max-time-call-retry 180
  param max-time-vm-retry 2
  param voice-mail 5007
  param call-retry-timer 5
  param handoff-string aa-bcd
  param drop-through-option 1
  param number-of-hunt-grps 1
```

### Related Commands

Description

application

Enters application configuration mode.

service

Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application.

## param drop-through-prompt

To associate an audio prompt file with the drop-through option for a
                              		  Cisco Unified CME B-ACD automated attendant (AA) application, use the param drop-through-prompt command in
                              		  application-parameter configuration mode. To disable the prompt, use the no form of this command.

param drop-through-prompt audio-filename

no param drop-through-prompt audio-filename

### Syntax Description

audio-filename

Identifying part of the filename of the prompt to be played
                                          						when calls for the drop-through option are answered.

### Command Default

No prompt is designated for the drop-through option.

### Command Modes

Application-parameter configuration (config-app-param)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(14)T

Cisco CME 3.3

This command was introduced to replace the call application voice drop-through-prompt command.

### Usage Guidelines

This command is used with the Cisco Unified CME Basic Automatic Call
                              		  Distribution and Auto-Attendant (B-ACD) service. This command is configured
                              		  under the service command for an AA service.

When an AA is configured for drop-through mode, the AA sends incoming
                              		  calls directly to the call queue associated with the menu number specified in
                              		  this command. Once in the queue, a caller hears ringback if an agent is
                              		  available or music on hold (MOH) if all agents are busy. If an greeting prompt
                              		  for drop-through mode is configured, a caller hears the prompt before being
                              		  sent to the queue as described.

The menu option number is an aa-hunt number that is associated with
                              		  an ephone hunt group using the param aa-hunt command.

For any configuration changes to take effect, you must reload the
                              		  Cisco Unified CME B-ACD scripts.

For more information, see the Cisco Unified CallManager Express B-ACD and Tcl Call-Handling
                                 			 Applications document for your release.

## Examples

The following example sets up a B-ACD with two AAs, both in
                              		  drop-through mode. The first AA is called acdaa and it has an AA pilot number
                              		  of (800) 555-0121. The second AA is aa-bcd and has an AA pilot number of (800)
                              		  555-0123. Both AAs use the call-queue service named callq. Callers to (800)
                              		  555-0121 drop directly through to the hunt group with the pilot number 5072
                              		  after hearing the greeting prompt in the audio file named en_dto_welcome.au.
                              		  (The prefix en is specified in the paramspace language command and is automatically added to the
                              		  filename provided in the param drop-through-prompt command.) Callers to (800)
                              		  555-0123 drop directly through to the hunt group with the pilot number 5071
                              		  without hearing any greeting.

```
dial-peer voice 1010 pots 
 service acdaa 
 port 1/1/0 
 incoming called-number 8005550121
dial-peer voice 1020 pots 
 service aa-bcd 
 port 1/1/1 
 incoming called-number 8005550123
.
.
.
application 
 service callq tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd.tcl
  param queue-manager-debugs 1
  param aa-hunt1 5071
  param aa-hunt2 5072
  param number-of-hunt-grps 2
  param queue-len 10
!
 service acdaa tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl
  paramspace english location tftp://192.168.254.254/user1/prompts/ 
  paramspace english index 0
  paramspace english language en
  param aa-pilot 8005550121
  param service-name callq
  param max-time-vm-retry 2
  param voice-mail 5007
  param call-retry-timer 20
  param number-of-hunt-grps 1
  param drop-through-prompt _bacd_dto_welcome.au
  param drop-through-option 2
  param second-greeting-time 45
  param handoff-string acdaa
  param max-time-call-retry 360
!
 service aa-bcd tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl
  paramspace english location tftp://192.168.254.254/user1/prompts/ 
  paramspace english index 0
  paramspace english language en
  param aa-pilot 8005550123
  param service-name callq
  param second-greeting-time 60
  param max-time-call-retry 180
  param max-time-vm-retry 2
  param voice-mail 5007
  param call-retry-timer 5
  param handoff-string aa-bcd
  param drop-through-option 1
  param number-of-hunt-grps 1
```

### Related Commands

Description

application

Enters application configuration mode.

service

Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application.

## param ea-password

To create a password for accessing the extension assigner
                              		  application, use the param ea-password command in application-parameter
                              		  configuration mode.

param ea-password password

### Syntax Description

password

Numeric string to be used as password for the extension
                                          						assigner application. Password string must be 2 to 10 characters long and can
                                          						contain numbers 0 to 9.

### Command Default

No password is created.

### Command Modes

Application-parameter configuration (config-app-param)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)XC4

Cisco Unified CME 4.0(3)

This command was introduced.

12.4(11)XJ

Cisco Unified CME 4.1

This command was introduced.

12.4(15)T

Cisco Unified CME 4.1

This command was integrated into Cisco IOS Release
                                          						12.4(15)T.

### Usage Guidelines

This command creates a password for using the extension assigner
                              		  application.

If this command is not configured, you cannot use the extension
                              		  assigner application.

## Examples

The following example shows that a password (1234) is configured for
                              		  the extension assigner application:

```
application
 service EA flash:ea/app-cme-ea-2.0.0.0.tcl
  paramspace english index 0
  paramspace english language en
  param ea-password 1234
  paramspace english location flash:ea/
  
paramspace english prefix en
```

### Related Commands

Description

application

Enters application configuration mode.

service

Loads and configures a specific, standalone application on
                                          						a dial peer.

## param handoff-string

To specify the name of a Cisco Unified CME B-ACD auto-attendant (AA)
                              		  to be passed to the call-queue script, use the param handoff-string command in application-parameter
                              		  configuration mode. To disable the handoff string, use the no form of this
                              		  command.

param handoff-string aa-service-name

no param drop-through-prompt aa-service-name

### Syntax Description

aa-service-name

Service name that was assigned to the AA script with the service command.

### Command Default

No string is designated to be passed to the call-queue service.

### Command Modes

Application-parameter configuration (config-app-param)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(14)T

Cisco CME 3.3

This command was introduced to replace the call application voice handoff-string command.

### Usage Guidelines

This command is used with the Cisco Unified CME Basic Automatic Call
                              		  Distribution and Auto-Attendant (B-ACD) service. This command is configured
                              		  under the service command for an AA service.

The handoff string is used only when the call-queue script starts for
                              		  the first time or restarts after a failure.

For any configuration changes to take effect, you must reload the
                              		  Cisco Unified CME B-ACD scripts.

For more information, see the Cisco Unified CallManager Express B-ACD and Tcl Call-Handling
                                 			 Applications document for your release.

## Examples

The following example sets parameters for an AA application called aa
                              		  and a call-queue application called queue. The direct-dial number to reach the
                              		  AA service is (800) 555-0100. Callers to this number drop through to the ephone
                              		  hunt group that has a pilot number of 5071 after hearing the initial prompt
                              		  from the file en_dt_prompt.au. The AA name, aa is passed to the call-queue
                              		  service in the param handoff-string command.

```
dial-peer voice 1000 pots 
 service aa 
 port 1/1/0 
 incoming called-number 8005550100
ephone-hunt 10 sequential 
 pilot 5071
 list 5011, 5012, 5013, 5014, 5015
!
application 
 service callq tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd.tcl
  param queue-manager-debugs 1
  param aa-hunt1 5071
  param number-of-hunt-grps 1
  param queue-len 10
!
 service aa tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl
  paramspace english location tftp://192.168.254.254/user1/prompts/ 
  paramspace english index 0
  paramspace english language en
  param aa-pilot 8005550100 
  param number-of-hunt-groups 1
  param service-name callq 
  param handoff-string aa
  param second-greeting-time 60 
  param drop-through-option 1
  param drop-through-prompt _dt_prompt.au
  param call-retry-timer 15 
  param max-time-call-retry 700 
  param voice-mail 5000 
  param max-time-vm-retry 2
```

### Related Commands

Description

application

Enters application configuration mode.

service

Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application.

## param max-extension-length

To specify the maximum number of digits callers can dial when they
                              		  choose the dial-by-extension option from the Cisco Unified CME B-ACD service,
                              		  use the param max-extension-length command in
                              		  application-parameter configuration mode. To return to the default, use the no form of this command.

param max-extension-length number

no param max-extension-length number

### Syntax Description

number

Number of digits. The lower limit is 0; there is no upper
                                          						limit. The default is 5.

### Command Default

The default number of digits callers can dial using the dial-by-extension option is 5.

### Command Modes

Application-parameter configuration (config-app-param)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(14)T

Cisco CME 3.3

This command was introduced to replace the call application voice max-extension-length command.

### Usage Guidelines

This command is used with the Cisco Unified CME Basic Automatic Call
                              		  Distribution and Auto-Attendant (B-ACD) service. This command is configured
                              		  under the service command for an AA service.

Use this command to restrict the number of digits that callers can
                              		  dial when using the dial-by-extension option.

For any configuration changes to take effect, you must reload the
                              		  Cisco Unified CME B-ACD scripts.

For more information, see the Cisco Unified CallManager Express B-ACD and Tcl Call-Handling
                                 			 Applications document for your release.

## Examples

The following example sets parameters for an AA application called aa
                              		  and a call-queue application called queue. The direct-dial number to reach the
                              		  AA service is (800) 555-0100. Callers to this number can press 1 to be
                              		  connected to the ephone hunt group with the pilot number 5071 or can press 2 to
                              		  dial an extension number of 4 or fewer digits.

```
dial-peer voice 1000 pots 
 service aa 
 port 1/1/0 
 incoming called-number 8005550100
ephone-hunt 10 sequential 
 pilot 5071
 list 5011, 5012, 5013, 5014, 5015
!
application 
 service callq tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd.tcl
  param queue-manager-debugs 1
  param aa-hunt1 5071
  param number-of-hunt-grps 1
  param queue-len 10
!
 service aa tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl
  paramspace english location tftp://192.168.254.254/user1/prompts/ 
  paramspace english index 0
  paramspace english language en
  param aa-pilot 8005550100 
  param welcome-prompt _aa_welcome.au
  param number-of-hunt-groups 1
  param dial-by-extension-option 2
  param max-extension-length 4
  param service-name callq 
  param handoff-string aa
  param second-greeting-time 60 
  param call-retry-timer 15 
  param max-time-call-retry 700 
  param voice-mail 5000 
  param max-time-vm-retry 2
```

### Related Commands

Description

application

Enters application configuration mode.

service

Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application.

## param max-time-call-retry

To specify the maximum length of time for which calls to the Cisco
                              		  Unified CME B-ACD service can stay in a call queue, use the param max-time-call-retry command in application-parameter configuration mode. To return to the
                              		  default, use the no form of this command.

param max-time-call-retry seconds

no param max-time-call-retry

### Syntax Description

seconds

Maximum length of time that the call-queue service can keep
                                          						redialing a hunt group pilot number, in seconds. Range: 20 to 3600. Default:
                                          						600.

### Command Default

A call in a B-ACD call queue continues to try to connect to a hunt
                              		  group for 600 seconds.

### Command Modes

Application-parameter configuration (config-app-param)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(14)T

Cisco CME 3.3

This command was introduced to replace the call application voice max-time-call-retry command.

12.4(20)YA

Cisco Unified CME 7.0(1)

The minimum value of the seconds argument was increased from
                                          						0 to 20.

12.4(22)T

Cisco Unified CME 7.0(1)

This command was integrated into Cisco IOS Release
                                          						12.4(22)T.

### Usage Guidelines

This command is used with the Cisco Unified CME Basic Automatic Call
                              		  Distribution (B-ACD) and Auto-Attendant (AA) service. Configure this command
                              		  under the service command for an AA service.

A call to a Cisco Unified CME B-ACD service is put into a call queue
                              		  if the hunt group that the call tried to reach has no phones available to take
                              		  the call because they are all busy. While the call is in the queue, a second
                              		  greeting is played at intervals specified by the param second-greeting-time command. From the queue, the
                              		  call makes retries to connect at intervals specified by the param call-retry-timer command until the maximum amount
                              		  of time to be spent in the queue expires. The maximum amount of time is set by
                              		  the param max-time-call-retry command. After the maximum
                              		  amount of time expires, the call is routed to the alternate destination
                              		  specified in the param voice-mail command. If the alternate destination
                              		  number is busy, the call makes the number of retries to connect specified in
                              		  the param max-time-vm-retry command. If the call is unable to connect to the alternate
                              		  destination after the number of retries that has been specified, it is
                              		  disconnected.

For any configuration changes to take effect, you must reload the
                              		  Cisco Unified CME B-ACD scripts.

For configuration information, see the “Setting
                                 			 Up Call-Queue and AA Services” section in the Cisco Unified CME B-ACD and Tcl Call-Handling Applications document.

## Examples

The following example sets parameters for an AA application called aa
                              		  and a call-queue application called queue. The direct-dial number to reach the
                              		  AA service is (800) 555-0100. Callers to this number can press 1 to be
                              		  connected to the ephone hunt group with the pilot number 5071 or can press 2 to
                              		  dial an extension number of 4 or fewer digits.

If a caller presses 2 and all the phones in ephone-hunt group 10 are
                              		  busy, the call is put into a queue for hunt group 10. Every 60 seconds, the
                              		  caller hears the second greeting, which is “Please continue to hold. An agent
                              		  will be with you shortly.” Every 15 seconds, the call-queue service tries again
                              		  to connect the call to the hunt group. If no phones become available before 700
                              		  seconds expire, the call is routed to extension 5000. If that extension is
                              		  busy, the call-queue service retries it 2 times more. If the call still cannot
                              		  be connected, it is disconnected.

```
dial-peer voice 1000 pots 
 service aa 
 port 1/1/0 
 incoming called-number 8005550100
 
ephone-hunt 10 sequential 
 pilot 5071
 list 5011, 5012, 5013, 5014, 5015
!
application 
 service callq tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd.tcl
  param queue-manager-debugs 1
  param aa-hunt1 5071
  param number-of-hunt-grps 1
  param queue-len 10
!
 service aa tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl
  paramspace english location tftp://192.168.254.254/user1/prompts/ 
  paramspace english index 0
  paramspace english language en
  param aa-pilot 8005550100 
  param welcome-prompt _aa_welcome.au
  param number-of-hunt-groups 1
  param dial-by-extension-option 2
  param max-extension-length 4
  param service-name callq 
  param handoff-string aa
  param second-greeting-time 60 
  param call-retry-timer 15 
  param max-time-call-retry 700 
  param voice-mail 5000 
  param max-time-vm-retry 2
```

### Related Commands

Command

Description

application

Enters application configuration mode.

call application voice load

Reloads the selected voice application script after it is
                                          						modified.

param call-retry-timer

Specifies the time interval before each attempt to retry to
                                          						connect a call to an ephone hunt group in a Cisco Unified CME B-ACD service.

param max-time-vm-retry

Specifies the maximum number of times that calls in a Cisco
                                          						Unified CME B-ACD call queue can attempt to connect to the alternate
                                          						destination number.

param second-greeting-time

Sets the length of the intervals between replays of the
                                          						second greeting to calls waiting in hunt group call queues that are part of a
                                          						Cisco Unified CME B-ACD service.

param voice-mail

Sets an alternate destination number to which to route
                                          						calls that cannot be connected to a hunt group that is part of a Cisco Unified
                                          						CME B-ACD service.

service

Enters application-parameter configuration mode to specify
                                          						the name of the application and the location of the Tcl script to load.

## param max-time-vm-retry

To specify the maximum number of times that calls in a Cisco Unified
                              		  CME B-ACD call queue can attempt to connect to the alternate destination
                              		  number, use the param max-time-vm-retry command
                              		  in application-parameter configuration mode. To return to the
                              		  default, use the no form of this command.

param max-time-vm-retry number

no param max-time-vm-retry number

### Syntax Description

number

Number of times that the alternate destination number is
                                          						redialed by the call-queue service. Range is from 1 to 3. Default is 1.

### Command Default

A call in a B-ACD call queue tries to connect to an alternate destination number 1 time.

### Command Modes

Application-parameter configuration (config-app-param)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(14)T

Cisco CME 3.3

This command was introduced to replace the call application voice max-time-vm-retry command.

### Usage Guidelines

This command is used with the Cisco Unified CME Basic Automatic Call
                              		  Distribution and Auto-Attendant (B-ACD) service. This command is configured
                              		  under the service command for an AA service.

A call to a Cisco Unified CME B-ACD service is put into a call queue
                              		  if the hunt group that the call tried to reach has no phones available to take
                              		  the call because they are all busy. While the call is in the queue, a second
                              		  greeting is played at intervals specified by the param second-greeting-time command. From the queue, the
                              		  call makes retries to connect at intervals specified by the param call-retry-timer command until the maximum amount
                              		  of time to be spent in the queue expires. The maximum amount of time is set by
                              		  the param max-time-call-retry command. After the maximum
                              		  amount of time expires, the call is routed to the alternate destination
                              		  specified in the param voice-mail command. If the alternate destination
                              		  number is busy, the call makes the number of retries to connect specified in
                              		  the param max-time-vm-retry command. If the call is unable to connect to the
                              		  alternate destination after the number of retries that has been specified, it
                              		  is disconnected.

For any configuration changes to take effect, you must reload the
                              		  Cisco Unified CME B-ACD scripts.

For more information, see the Cisco Unified CallManager Express B-ACD and Tcl Call-Handling
                                 			 Applications document for your release.

## Examples

The following example sets parameters for an AA application called aa
                              		  and a call-queue application called queue. The direct-dial number to reach the
                              		  AA service is (800) 555-0100. Callers to this number can press 1 to be
                              		  connected to the ephone hunt group with the pilot number 5071 or can press 2 to
                              		  dial an extension number of 4 or fewer digits.

If a caller presses 2 and all the phones in ephone-hunt group 10 are
                              		  busy, the call is put into a queue for hunt group 10. Every 60 seconds, the
                              		  caller hears the second greeting, which is “Please continue to hold. An agent
                              		  will be with you shortly.” Every 15 seconds, the call-queue service tries again
                              		  to connect the call to the hunt group. If no phones become available before 700
                              		  seconds expire, the call is routed to extension 5000. If that extension is
                              		  busy, the call-queue service retries it 2 times more. If the call still cannot
                              		  be connected, it is now disconnected.

```
dial-peer voice 1000 pots 
 service aa 
 port 1/1/0 
 incoming called-number 8005550100
ephone-hunt 10 sequential 
 pilot 5071
 list 5011, 5012, 5013, 5014, 5015
!
application 
 service callq tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd.tcl
  param queue-manager-debugs 1
  param aa-hunt1 5071
  param number-of-hunt-grps 1
  param queue-len 10
!
 service aa tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl
  paramspace english location tftp://192.168.254.254/user1/prompts/ 
  paramspace english index 0
  paramspace english language en
  param aa-pilot 8005550100 
  param welcome-prompt _aa_welcome.au
  param number-of-hunt-groups 1
  param dial-by-extension-option 2
  param max-extension-length 4
  param service-name callq 
  param handoff-string aa
  param second-greeting-time 60 
  param call-retry-timer 15 
  param max-time-call-retry 700 
  param voice-mail 5000 
  param max-time-vm-retry 2
```

### Related Commands

Description

application

Enters application configuration mode.

service

Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application.

## param menu-timeout

To set the number of times the AA service will loop the menu prompt
                              		  before connecting the caller to an operator if the caller does not select a
                              		  menu option, use the param menu-timeout command in application-parameter
                              		  configuration mode. To return to the default, use the no form of this command.

param menu-timeout number

no param menu-timeout

### Syntax Description

number

Times to replay menu prompt before connecting a caller to
                                          						an operator. Range: 0 to 10. Default: 4.

### Command Default

Auto-attendant service replays menu prompt 4 times before connecting
                              		  the caller to an operator.

### Command Modes

Application-parameter configuration (config-app-param)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(14)T

Cisco CME 3.3

This command was introduced.

12.4(22)YA

Cisco Unified CME 7.0(1)

The minimum value of the number argument was decreased from
                                          						1 to 0.

12.4(22)T

Cisco Unified CME 7.0(1)

This command was integrated into Cisco IOS Release
                                          						12.4(22)T.

### Usage Guidelines

This command is used with Cisco Unified CME Basic Automatic Call
                              		  Distribution (B-ACD) and Auto-Attendant (AA) service.

If a caller does not select a menu option before the timeout set with
                              		  this command expires, the call is transferred to the operator hunt group. The
                              		  operator hunt-group is the hunt group with the highest aa-hunt number set with
                              		  the param aa-hunt command.

For any configuration changes to take effect, you must reload the
                              		  Cisco Unified CME B-ACD scripts.

For configuration information, see the “Setting
                                 			 Up Call-Queue and AA Services” section in the Cisco Unified CME B-ACD and Tcl Call-Handling Applications document.

## Examples

The following example shows the menu timeout set to 5 replays for the
                              		  AA application called order1-aa:

```
application
  service acme-aa1 tftp://192.168.254.254/acme/bacd/app-b-acd-aa-2.1.2.3.tcl
  paramspace english index 1
  param menu-timeout 5
  param handoff-string acme-aa1
  param dial-by-extension-option 2
  paramspace english language en
  param max-time-vm-retry 2
  param max-extension-length 4
  param aa-pilot 8005550100
  paramspace english location flash:/bacd/
  param second-greeting-time 60
  param welcome-prompt _aa_welcome.au
  param number-of-hunt-groups 1
  param call-retry-timer 15
  param max-time-call-retry 700
  param voice-mail 5000
  param service-name callq
```

### Related Commands

Command

Description

application

Enters application configuration mode.

call application voice load

Reloads the selected voice application script after it is
                                          						modified.

param aa-hunt

Declares a Cisco Unified CME B-ACD menu number and
                                          						associates it with the pilot number of an ephone hunt group.

service

Enters application-parameter configuration mode to specify
                                          						the name of the application and the location of the Tcl script to load.

## param number-of-hunt-grps

To specify the number of hunt groups used with a Cisco Unified CME
                              		  B-ACD call-queue or AA service, use the param number-of-hunt-grps command in
                              		  application-parameter configuration mode. To return to the default, use the no form of this command.

param number-of-hunt-grps number

no param number-of-hunt-grps number

### Syntax Description

number

Number of ephone hunt groups used by the service. Range is
                                          						1 to 10 for the call-queue service and 1 to 3 for an automated attendant (AA)
                                          						service.

### Command Default

This parameter is not set.

### Command Modes

Application-parameter configuration (config-app-param)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(14)T

Cisco CME 3.3

This command was introduced to replace the call application voice number-of-hunt-grps command.

### Usage Guidelines

This command is used with the Cisco Unified CME Basic Automatic Call
                              		  Distribution and Auto-Attendant (B-ACD) service. This command is configured
                              		  both under the service command for the call-queue service
                              		  and under the service command for an AA service.

The number of hunt groups specified for the call-queue service is the
                              		  total of the number of hunt groups used with all the AAs with which it is
                              		  associated. For example, if a B-ACD has three AAs, each with two hunt groups,
                              		  the number of hunt groups for each AA is two and the number of hunt groups for
                              		  the call-queue service is six.

For any configuration changes to take effect, you must reload the
                              		  Cisco Unified CME B-ACD scripts.

For more information, see the Cisco Unified CallManager Express B-ACD and Tcl Call-Handling
                                 			 Applications document for your release.

## Examples

A call-queue service called CQ is set up to work with two AA
                              		  services. CQ lists 4 as the number of hunt groups it uses. AA1 is associated
                              		  with 3 hunt groups, and its callers hear the following prompt: “Press 1 for
                              		  sales, press 2 for service, press 0 for operator.” AA2 uses drop-through mode.
                              		  Its callers do not hear a prompt and are directly connected to the single hunt
                              		  group that is associated with it.

```
application
 service CQ tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd.tcl
  param queue-manager-debugs 1
  param aa-hunt1 1001
  param aa-hunt2 2001
  param aa-hunt3 3001
  param aa-hunt4 4001
  param number-of-hunt-grps 4
  param queue-len 10
 service AA1 tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl
  paramspace english location tftp://192.168.254.254/user1/prompts/ 
  paramspace english index 0
  paramspace english language en
  param aa-pilot 8005550111 
  param number-of-hunt-groups 3 
  param service-name CQ 
  param welcome-prompt _bacd_welcome.au 
  param handoff-string AA1 
 service AA2 tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl
  paramspace english location tftp://192.168.254.254/user1/prompts/ 
  paramspace english index 0
  paramspace english language en
  param aa-pilot 8005550122 
  param number-of-hunt-groups 1 
  param service-name CQ 
  param drop-through-option 4 
  param handoff-string AA2
```

### Related Commands

Description

application

Enters application configuration mode.

service

Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application.

## param queue-exit-extension

To assign an extension number to a call-queue exit option, use the param queue-exit-extension command in
                              		  application-parameter configuration mode. To remove an exit option, use the no form of this command.

param queue-exit-extension option-number extension-number

no param queue-exit-extension option-number

### Syntax Description

option-number

Number of the call-queue exit option. Range: 1 to 3. There
                                          						is no default.

extension-number

Extension number associated with the exit option.

### Command Default

Call-queue exit option is not defined.

### Command Modes

Application-parameter configuration (config-app-param)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(22)YA

Cisco Unified CME 7.0(1)

This command was introduced.

12.4(22)T

Cisco Unified CME 7.0(1)

This command was integrated into Cisco IOS Release
                                          						12.4(22)T.

### Usage Guidelines

This command is used with the Cisco Unified CME Basic Automatic Call
                              		  Distribution (B-ACD) and Auto-Attendant (AA) service.

Use this command together with the param queue-exit-option command to enable callers to
                              		  select from up to three different options to exit from a call queue. The option-number argument in this command
                              		  corresponds to the option-number argument in the param queue-exit-option command.

You can record a customized second greeting that offers callers up to
                              		  three options to exit from the call queue. For example, you might record a
                              		  message that says, “To leave a message, press 6; to hear more options, press 7;
                              		  to speak to an operator, press 8.”

This second greeting is stored in the audio file named
                              		  en_bacd_allagentsbusy.au. You can record over the default message in this file,
                              		  provided you do not change the name of the file.

For any configuration changes to take effect, you must reload the
                              		  Cisco Unified CME B-ACD scripts.

For configuration information, see the “Setting
                                 			 Up Call-Queue and AA Services” section in the Cisco Unified CME B-ACD and Tcl Call-Handling Applications document.

## Examples

The following example shows that the acme-aa1 application has three
                              		  exit options defined for its call-queue service:

```
application
  service acme-aa1 tftp://192.168.254.254/acme/bacd/app-b-acd-aa-2.1.2.3.tcl
  param dial-by-extension-option 7
  param handoff-string acme-aa1
  paramspace english index 1
  param queue-exit-option2 7
  param max-time-vm-retry 2
  paramspace english language en
  param aa-pilot 801
  param max-extension-length 4
  param queue-overflow-extension 101
  param queue-exit-extension2 101
  param second-greeting-time 20
  param queue-exit-option1 6
  paramspace english location flash:/bacd/
  param send-account true
  param call-retry-timer 20
  param queue-exit-option3 8
  param voice-mail 444
  param max-time-call-retry 60
  param service-name sf-queue
  param queue-exit-extension1 202
  param number-of-hunt-grps 1
  param drop-through-option 1
  param queue-exit-extension3 444
```

### Related Commands

Command

Description

application

Enters application configuration mode.

call application voice load

Reloads the selected voice application script after it is
                                          						modified.

param queue-exit-option

Assigns a menu number to a call-queue exit option.

service

Enters application-parameter configuration mode to specify
                                          						the name of the application and the location of the Tcl script to load.

## param queue-exit-option

To assign a menu number to a call-queue exit option, use the param queue-exit-option command in application-parameter
                              		  configuration mode. To disable this option, use the no form of this command.

param queue-exit-option option-number menu-number

no param queue-exit-option option-number

### Syntax Description

option-number

Number of the call-queue exit option. Range: 1 to 3. There
                                          						is no default.

menu-number

Menu option number associated with the exit option.

### Command Default

Call-queue exit option is not assigned.

### Command Modes

Application-parameter configuration (config-app-param)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(22)YA

Cisco Unified CME 7.0(1)

This command was introduced.

12.4(22)T

Cisco Unified CME 7.0(1)

This command was integrated into Cisco IOS Release
                                          						12.4(22)T.

### Usage Guidelines

This command is used with the Cisco Unified CME Basic Automatic Call
                              		  Distribution (B-ACD) and Auto-Attendant (AA) service.

Use this command together with the param queue-exit-extension command to enable callers to
                              		  select from up to three different options to exit from a call queue. The option-number argument in this command
                              		  corresponds to the option-number argument in the param queue-exit-extension command.

You can record a customized second greeting that offers callers up to
                              		  three options to exit from the call queue. For example, you might record a
                              		  message that says, “To leave a message, press 6; to hear more options, press 7;
                              		  to speak to an operator, press 8.”

This second greeting is stored in the audio file named
                              		  en_bacd_allagentsbusy.au. You can record over the default message in this file,
                              		  provided you do not change the name of the file.

For any configuration changes to take effect, you must reload the
                              		  Cisco Unified CME B-ACD scripts.

For configuration information, see the “Setting
                                 			 Up Call-Queue and AA Services” section in the Cisco Unified CME B-ACD and Tcl Call-Handling Applications document.

## Examples

The following example shows that the acme-aa1 application has three
                              		  exit options defined for its call-queue service:

```
application
  service acme-aa1 tftp://192.168.254.254/acme/bacd/app-b-acd-aa-2.1.2.3.tcl
  param dial-by-extension-option 7
  param handoff-string acme-aa1
  paramspace english index 1
  param queue-exit-option2 7
  param max-time-vm-retry 2
  paramspace english language en
  param aa-pilot 801
  param max-extension-length 4
  param queue-overflow-extension 101
  param queue-exit-extension2 101
  param second-greeting-time 20
  param queue-exit-option1 6
  paramspace english location flash:/bacd/
  param send-account true
  param call-retry-timer 20
  param queue-exit-option3 8
  param voice-mail 444
  param max-time-call-retry 60
  param service-name sf-queue
  param queue-exit-extension1 202
  param number-of-hunt-grps 1
  param drop-through-option 1
  param queue-exit-extension3 444
```

### Related Commands

Command

Description

application

Enters application configuration mode.

call application voice load

Reloads the selected voice application script after it is
                                          						modified.

param queue-exit-extension

Assigns an extension number to a call-queue exit option.

service

Enters application-parameter configuration mode to specify
                                          						the name of the application and the location of the Tcl script to load.

## param queue-len

To specify the number of calls that can be held in each call queue in
                              		  a Cisco Unified CME B-ACD service, use the param queue-len command in application-parameter
                              		  configuration mode. To return to the default, use the no form of this command.

param queue-len number

no param queue-len number

### Syntax Description

number

Number of calls that can be held in a call queue. Range is
                                          						1 to 30. Default is 10.

### Command Default

The default queue length is 10.

### Command Modes

Application-parameter configuration (config-app-param)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(14)T

Cisco CME 3.3

This command was introduced to replace the call application voice queue-len command.

### Usage Guidelines

This command is used with the Cisco Unified CME Basic Automatic Call
                              		  Distribution and Auto-Attendant (B-ACD) service. This command is configured
                              		  under the service command for a call-queue service.

This command specifies the maximum number of calls that can be held
                              		  in a call queue for a hunt group used with B-ACD when all of the hunt group
                              		  member phones are busy.

Note that having calls in queue keeps PSTN ports occupied for a
                              		  longer time, and you may want to plan for more ports if you have longer queues.
                              		  The maximum number of calls allowed in the queues of ephone hunt groups must be
                              		  based on the number of ports or trunks available. For example, if you have 20
                              		  foreign exchange office (FXO) ports and two ephone hunt groups, you can
                              		  configure a maximum of ten calls per ephone hunt-group queue using the param queue-len 10 command. You can use the same configuration if
                              		  you have a single T1 trunk, which supports 23 channels.

For any configuration changes to take effect, you must reload the
                              		  Cisco Unified CME B-ACD scripts.

For more information, see the Cisco Unified CallManager Express B-ACD and Tcl Call-Handling
                                 			 Applications document for your release.

## Examples

A call-queue service called CQ is set up to work with two AA
                              		  services. CQ lists four as the number of hunt groups it uses. AA1 is associated
                              		  with three hunt groups, and its callers hear the following prompt: “Press 1 for
                              		  sales, press 2 for service, press 0 for operator.” AA2 uses drop-through mode.
                              		  Its callers do not hear a prompt and are directly connected to the single hunt
                              		  group that is associated with it. Up to 12 calls can be held in the call queue
                              		  for each hunt group if all the phones in the hunt group are busy.

```
application
 service CQ tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd.tcl
  param queue-manager-debugs 1
  param aa-hunt1 1001
  param aa-hunt2 2001
  param aa-hunt3 3001
  param aa-hunt4 4001
  param number-of-hunt-grps 4
  param queue-len 12
 service AA1 tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl
  paramspace english location tftp://192.168.254.254/user1/prompts/ 
  paramspace english index 0
  paramspace english language en
  param aa-pilot 8005550111 
  param number-of-hunt-groups 3 
  param service-name CQ 
  param welcome-prompt _bacd_welcome.au 
  param handoff-string AA1 
 service AA2 tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl
  paramspace english location tftp://192.168.254.254/user1/prompts/ 
  paramspace english index 0
  paramspace english language en
  param aa-pilot 8005550122 
  param number-of-hunt-groups 1 
  param service-name CQ 
  param drop-through-option 4 
  param handoff-string AA2
```

### Related Commands

Description

application

Enters application configuration mode.

service

Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application.

## param queue-manager-debugs

To enable the collection of call-queue debug information in a Cisco
                              		  Unified CME B-ACD service, use the param queue-manager-debugs command in
                              		  application-parameter configuration mode. To remove the setting, use the no form of this command with the keyword that
                              		  was previously used.

param queue-manager-debugs [ 0 | 1 ]

no param queue-manager-debugs [ 0 | 1 ]

### Syntax Description

0

Disables collection of call-queue debug information.

1

Enables collection of call-queue debug information

### Command Default

Collection of debug information is disabled.

### Command Modes

Application-parameter configuration (config-app-param)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(14)T

Cisco CME 3.3

This command was introduced to replace the call application voice queue-manager-debugs command.

### Usage Guidelines

This command is used with the Cisco Unified CME Basic Automatic Call
                              		  Distribution and Auto-Attendant (B-ACD) service. This command is configured
                              		  under the service command for the call-queue service.

This command enables the collection of data regarding call queue
                              		  activity. It is used in conjunction with the debug voip ivr script command. Both commands must be enabled at the same
                              		  time.

For any configuration changes to take effect, you must reload the
                              		  Cisco Unified CME B-ACD scripts.

For more information, see the Cisco Unified CallManager Express B-ACD and Tcl Call-Handling
                                 			 Applications document for your release.

## Examples

A call-queue service called CQ is set up to work with two AA
                              		  services. CQ lists four as the number of hunt groups it uses. AA1 is associated
                              		  with three hunt groups, and its callers hear the following prompt: “Press 1 for
                              		  sales, press 2 for service, press 0 for operator.” AA2 uses drop-through mode.
                              		  Its callers do not hear a prompt and are directly connected to the single hunt
                              		  group that is associated with it. Up to ten calls can be held in the call queue
                              		  for each hunt group if all the phones in the hunt group are busy with other
                              		  calls. Call-queue debugging is enabled.

```
application
 service CQ tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd.tcl
  param queue-manager-debugs 1
  param aa-hunt1 1001
  param aa-hunt2 2001
  param aa-hunt3 3001
  param aa-hunt4 4001
  param number-of-hunt-grps 4
  param queue-len 10
 service AA1 tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl
  paramspace english location tftp://192.168.254.254/user1/prompts/ 
  paramspace english index 0
  paramspace english language en
  param aa-pilot 8005550111 
  param number-of-hunt-groups 3 
  param service-name CQ 
  param welcome-prompt _bacd_welcome.au 
  param handoff-string AA1 
 service AA2 tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl
  paramspace english location tftp://192.168.254.254/user1/prompts/ 
  paramspace english index 0
  paramspace english language en
  param aa-pilot 8005550122 
  param number-of-hunt-groups 1 
  param service-name CQ 
  param drop-through-option 4 
  param handoff-string AA2
```

### Related Commands

Description

application

Enters application configuration mode.

service

Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application.

## param queue-overflow-extension

To set the extension number to route calls to when the call queue for
                              		  the auto-attendant service is full, use the param queue-overflow-extension command in application-parameter configuration mode. To return
                              		  to the default, use the no form of this command.

param queue-overflow-extension extension-number

no param queue-overflow-extension

### Syntax Description

extension-number

Extension number to which the auto-attendant service
                                          						forwards calls when the call queue is full.

### Command Default

No overflow extension is defined. Calls disconnect if the queue
                              		  becomes full.

### Command Modes

Application-parameter configuration (config-app-param)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(22)YA

Cisco Unified CME 7.0(1)

This command was introduced.

12.4(22)T

Cisco Unified CME 7.0(1)

This command was integrated into Cisco IOS Release
                                          						12.4(22)T.

### Usage Guidelines

This command is used with the Cisco Unified CME Basic Automatic Call
                              		  Distribution (B-ACD) and Auto-Attendant (AA) service.

This command specifies the extension number where calls are sent when
                              		  the number of calls waiting in a B-ACD call queue exceeds the number set with
                              		  the param queue-len command.

For any configuration changes to take effect, you must reload the
                              		  Cisco Unified CME B-ACD scripts.

For configuration information, see the “Setting
                                 			 Up Call-Queue and AA Services” section in the Cisco Unified CME B-ACD and Tcl Call-Handling Applications document.

## Examples

The following example shows that the AA application named acme-aa1
                              		  uses the call-queue service named CQ. When the number of calls in the queue
                              		  exceeds 12, new calls that cannot be answered by an agent are sent to extension
                              		  5100.

```
application 
  service CQ tftp://192.168.254.254/acme/bacd/app-b-acd.tcl 
  param queue-manager-debugs 1 
  param aa-hunt1 1001 
  param aa-hunt2 2001 
  param aa-hunt3 3001 
  param aa-hunt4 4001 
  param number-of-hunt-grps 4 
  param queue-len 12 
  !
!
 application
  service acme-aa1 tftp://192.168.254.254/acme/bacd/app-b-acd-aa-2.1.2.3.tcl
  paramspace english index 1
  param handoff-string acme-aa1
  param dial-by-extension-option 2
  paramspace english language en
  param aa-pilot 8005550100
  param queue-overflow-extension 5100
  paramspace english location flash:/bacd/
  param welcome-prompt _aa_welcome.au
  param number-of-hunt-groups 1
  param voice-mail 5000
  param service-name CQ
```

### Related Commands

Command

Description

application

Enters application configuration mode.

call application voice load

Reloads the selected voice application script after it is
                                          						modified.

param queue-len

Specifies the number of calls that can be held in each call
                                          						queue in a Cisco Unified CME B-ACD service.

service

Enters application-parameter configuration mode to specify
                                          						the name of the application and the location of the Tcl script to load.

## param secondary-prefix

To set a prefix to add to digits coming from the PSTN Central Office
                              		  (CO) to route calls from a secondary Cisco Unified CME router to a primary
                              		  Cisco Unified CME router when using the Direct Inward Dial (DID) Digit
                              		  Translation Service, use the param secondary-prefix command in application-parameter
                              		  configuration mode. To disable this option, use the no form of this command.

param secondary-prefix secondary-prefix

no param secondary-prefix secondary-prefix

### Syntax Description

secondary-prefix

Prefix to add to digits in order to route calls to the
                                          						primary Cisco Unified CME router. Range is from 0 to 99.

### Command Default

No prefix is defined.

### Command Modes

Application-parameter configuration (config-app-param)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)XC

Cisco Unified CME 4.0

This command was introduced to replace the call application voice secondary-prefix command.

12.4(9)T

Cisco Unified CME 4.0

This command replaced the call application voice secondary-prefix command and was integrated into Cisco IOS Release
                                          						12.4(9)T.

### Usage Guidelines

This command is used with the Cisco Unified CallManager Express
                              		  (Cisco Unified CME) DID Digit Translation Service, which provides number
                              		  translation for DID calls when the range of DID digits provided by the PSTN
                              		  Central Office (CO) does not match the digits in the Cisco Unified CME
                              		  extension numbers.

The Tcl script that provides the service accepts PSTN DID numbers of
                              		  any length and maps them to the internal extension numbers that are assigned by
                              		  a system administrator. Where necessary, a prefix is appended to the DID digits
                              		  to create a valid extension number. The script uses the parameters that you
                              		  input to determine the valid range of digits to be accepted from the CO, the
                              		  valid range of digits in the local dial plan, and the prefix to append, if
                              		  necessary. The script also handles DID calls that map to invalid extension
                              		  numbers: a prompt is played and the calls are disconnected.

When calls are received by a secondary Cisco Unified CME router, they
                              		  are routed to the primary router by configuring an H.323 VoIP dial peer and
                              		  matching the destination pattern for that dial peer. The DID prefix that was
                              		  configured for use with the DID script is appended to the incoming DID digits
                              		  first. The secondary prefix is appended next. For example, if the incoming DID
                              		  digits are 25, the DID prefix is 3, and the secondary prefix is 7, the
                              		  transformed number will be 7325. The transformed number matches a VoIP dial
                              		  peer, which uses the forward-digits command to send only the three
                              		  relevant digits, the extension number, to the primary router.

See the Cisco Unified CallManager Express B-ACD and Tcl Call-Handling
                                 			 Applications document for your release.

## Examples

The following example configures a Basic DID application on the Cisco
                              		  Unified CME router. It sets a prefix of 5 to apply to the digits coming from
                              		  the CO in order to construct a valid extension number. Then the secondary
                              		  prefix (4) is appended. If the incoming DID digits are 25, the DID prefix is 5,
                              		  and the secondary prefix is 4, then the transformed number is 4525. The
                              		  transformed number matches VoIP dial peer 1000. The VoIP dial peer sends calls
                              		  to the primary Cisco Unified CME router using the IP address that is entered in
                              		  the session target command. The dial peer uses the forward-digits command to send the extension
                              		  number, 525, to the primary Cisco Unified CME router.

```
dial-peer voice 1000 voip
 destination-pattern 45..
 session target ipv4:10.1.1.1
 dtmf-relay h245-alphanumeric
 codec g711ulaw
 forward-digits 3
application
 service didapp tftp://192.168.254.254/scripts/did/app-THD-DID-2.0.0.1.tcl
  paramspace english index 1
  paramspace english language en
  paramspace english location tftp://192.168.254.254/apps/dir25/
  param secondary-prefix 4
  param did-prefix 5
  param co-did-min 00
  param co-did-max 79
  param store-did-min 00
  param store-did-max 79
```

### Related Commands

Description

application

Enters application configuration mode.

service

Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application.

## param second-greeting-time

To set the length of the intervals between playouts of the second
                              		  greeting to calls waiting in hunt group call queues that are part of a Cisco
                              		  Unified CME B-ACD service, use the param second-greeting-time command
                              		  in application-parameter configuration mode. To return to the
                              		  default, use the no form of this command

param second-greeting-time seconds

no param max-time-vm-retry seconds

### Syntax Description

seconds

Length of time intervals between playouts of the second
                                          						greeting to calls in a B-ACD call queue, in seconds. Range is from 30 to 120.
                                          						Default is 60.

### Command Default

The second greeting is played out every 60 seconds to calls in B-ACD
                              		  call queues.

### Command Modes

Application-parameter configuration (config-app-param)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(14)T

Cisco CME 3.3

This command was introduced to replace the call application voice second-greeting-time command.

### Usage Guidelines

This command is used with the Cisco Unified CME Basic Automatic Call
                              		  Distribution and Auto-Attendant (B-ACD) service. This command is configured
                              		  under the service command for an AA service.

A call to a Cisco Unified CME B-ACD service is put into a call queue
                              		  if the hunt group that the call tried to reach has no phones available to take
                              		  the call because they are all busy. While the call is in the queue, a second
                              		  greeting is played at intervals specified by the param second-greeting-time command. From the queue, the
                              		  call retries to connect to the hunt group at intervals specified by the param call-retry-timer command until the maximum amount
                              		  of time to be spent in the queue expires. The maximum amount of time is set by
                              		  the param max-time-call-retry command. After the maximum
                              		  amount of time expires, the call is routed to the alternate destination
                              		  specified in the param voice-mail command. If the alternate destination
                              		  number is busy, the call makes the number of retries to connect specified in
                              		  the param max-time-vm-retry command. If the call is unable to connect to the
                              		  alternate destination after the number of retries that has been specified, it
                              		  is disconnected.

The second greeting is stored in the audio file named
                              		  en_bacd_allagentsbusy.au. You can rerecord over the default message that is
                              		  provided in the file, but you cannot change the name of the file.

For any configuration changes to take effect, you must reload the
                              		  Cisco Unified CME B-ACD scripts.

For more information, see the Cisco Unified CallManager Express B-ACD and Tcl Call-Handling
                                 			 Applications document for your release.

## Examples

The following example sets parameters for an AA application called aa
                              		  and a call-queue application called queue. The direct-dial number to reach the
                              		  AA service is (800) 555-0100. Callers to this number can press 1 to be
                              		  connected to the ephone hunt group with the pilot number 5071 or can press 2 to
                              		  dial an extension number of 4 or fewer digits.

If a caller presses 2 and all the phones in ephone-hunt group 10 are
                              		  busy, the call is put into a queue for hunt group 10. Every 60 seconds, the
                              		  caller hears the second greeting, which is “Please continue to hold. An agent
                              		  will be with you shortly.” Every 15 seconds, the call-queue service tries again
                              		  to connect the call to the hunt group. If no phones become available before 700
                              		  seconds expire, the call is routed to extension 5000. If that extension is
                              		  busy, the call-queue service retries it 2 times more. If the call still cannot
                              		  be connected, it is now disconnected.

```
dial-peer voice 1000 pots 
 service aa 
 port 1/1/0 
 incoming called-number 8005550100
ephone-hunt 10 sequential 
 pilot 5071
 list 5011, 5012, 5013, 5014, 5015
!
application 
 service callq tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd.tcl
  param queue-manager-debugs 1
  param aa-hunt1 5071
  param number-of-hunt-grps 1
  param queue-len 10
!
 service aa tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl
  paramspace english location tftp://192.168.254.254/user1/prompts/ 
  paramspace english index 0
  paramspace english language en
  param aa-pilot 8005550100 
  param welcome-prompt _aa_welcome.au
  param number-of-hunt-groups 1
  param dial-by-extension-option 2
  param max-extension-length 4
  param service-name callq 
  param handoff-string aa
  param second-greeting-time 60 
  param call-retry-timer 15 
  param max-time-call-retry 700 
  param voice-mail 5000 
  param max-time-vm-retry 2
```

### Related Commands

Description

application

Enters application configuration mode.

service

Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application.

## param send-account true

To generate call detail records (CDRs) for calls that are handled by
                              		  the Cisco Unified CME B-ACD service, use the param send-account command in application-parameter
                              		  configuration mode. To return to the default, use the no form of this command.

param send-account true

no param send-account true

### Syntax Description

This command has no arguments or keywords.

### Command Default

CDRs are not generated.

### Command Modes

Application-parameter configuration (config-app-param)

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

This command captures CDRs in RADIUS format for calls handled by the
                              		  Cisco Unified CME Basic Automatic Call Distribution (B-ACD) and Auto-Attendant
                              		  (AA) service. The call record includes the name of the AA service, hunt group
                              		  pilot-number, and globally unique identifier (GUID).

For configuration information, see the “Setting
                                 			 Up Call-Queue and AA Services” section in the Cisco Unified CME B-ACD and Tcl Call-Handling Applications document.

For information on enabling RADIUS accounting, see the CDR
                                 			 Accounting for Cisco IOS Voice Gateways guide.

## Examples

The following example shows that calls using the acme-aa1 service
                              		  generate a call detail record:

```
application
  service acme-aa1 tftp://192.168.254.254/acme/bacd/
app-b-acd-aa-2.1.2.3.tcl
  paramspace english index 1
  param handoff-string acme-aa1
  param dial-by-extension-option 2
  paramspace english language en
  param aa-pilot 8005550100
  paramspace english location flash:/bacd/
  param welcome-prompt _aa_welcome.au
  param send-account true
  param number-of-hunt-groups 1
  param voice-mail 5000
  param service-name callq
```

### Related Commands

Command

Description

application

Enters application configuration mode.

call application voice load

Reloads the selected voice application script after it is
                                          						modified.

gw-accounting aaa

Enables the gateway to send accounting CDRs to the RADIUS
                                          						server using VSAs (attribute 26).

service

Enters application-parameter configuration mode to specify
                                          						the name of the application and the location of the Tcl script to load.

## param service-name

To specify a Cisco Unified CME B-ACD call-queue service to use with
                              		  an automated attendant (AA) service, use the param service-name command in application-parameter
                              		  configuration mode. To return to the default, use the no form of this command.

param service-name queue-service-name

no param service-name queue-service-name

### Syntax Description

queue-service-name

Name that was assigned to the B-ACD call-queue service with
                                          						the service command.

### Command Default

No call-queue service is specified.

### Command Modes

Application-parameter configuration (config-app-param)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(14)T

Cisco CME 3.3

This command was introduced to replace the call application voice service-name command.

### Usage Guidelines

This command is used with the Cisco Unified CME Basic Automatic Call
                              		  Distribution and Auto-Attendant (B-ACD) service. This command is configured
                              		  under the service command for an AA service.

For any configuration changes to take effect, you must reload the
                              		  Cisco Unified CME B-ACD scripts.

For more information, the Cisco Unified CallManager Express B-ACD and Tcl Call-Handling
                                 			 Applications document for your release.

## Examples

A call-queue service called CQ is set up to work with two AA
                              		  services. CQ lists four as the number of hunt groups it uses. AA1 is associated
                              		  with three hunt groups, and its callers hear the following prompt: “Press 1 for
                              		  sales, press 2 for service, press 0 for operator.” AA2 uses drop-through mode.
                              		  Its callers do not hear a prompt and are directly connected to the single hunt
                              		  group that is associated with it. Up to ten calls can be held in the call queue
                              		  for each hunt group if all the phones in the hunt group are busy with other
                              		  calls. Call-queue debugging is enabled.

```
application
 service CQ tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd.tcl
  param queue-manager-debugs 1
  param aa-hunt1 1001
  param aa-hunt2 2001
  param aa-hunt3 3001
  param aa-hunt4 4001
  param number-of-hunt-grps 4
  param queue-len 10
 service AA1 tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl
  paramspace english location tftp://192.168.254.254/user1/prompts/ 
  paramspace english index 0
  paramspace english language en
  param aa-pilot 8005550111 
  param number-of-hunt-groups 3 
  param service-name CQ 
  param welcome-prompt _bacd_welcome.au 
  param handoff-string AA1 
 service AA2 tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl
  paramspace english location tftp://192.168.254.254/user1/prompts/ 
  paramspace english index 0
  paramspace english language en
  param aa-pilot 8005550122 
  param number-of-hunt-groups 1 
  param service-name CQ 
  param drop-through-option 4 
  param handoff-string AA2
```

### Related Commands

Description

application

Enters application configuration mode.

service

Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application.

## param store-did-max

To set the upper boundary of the range of digits that is valid in the
                              		  Cisco Unified CME numbering plan used with the Direct Inward Dial (DID) Digit
                              		  Translation Service, use the param store-did-max command in global configuration
                              		  mode. To disable this option, use the no form of this command.

param store-did-max max-store-value

no param store-did-max max-store-value

### Syntax Description

max-store-value

Maximum value of digits in the Cisco Unified CME dial plan.
                                          						The digit string can be any length, but the string length must be the same in
                                          						the param co-did-max , param co-did-min , param store-did-max , and param store-did-min commands.

### Command Default

No maximum value is defined for the range of digits in the dial plan.

### Command Modes

Application-parameter configuration (config-app-param)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)XC

Cisco Unified CME 4.0

This command was introduced to replace the call application voice store-did-max command.

12.4(9)T

Cisco Unified CME 4.0

This command replaced the call application voice store-did-max command and was integrated into Cisco IOS Release
                                          						12.4(9)T.

### Usage Guidelines

This command defines the upper limit of the range of digits in the
                              		  site dial plan for the Cisco Unified CallManager Express (Cisco Unified CME)
                              		  Direct Inward Dial Digit Translation Service, which provides number translation
                              		  for DID calls when the DID digits provided by the PSTN Central Office (CO) do
                              		  not match the digits in the Cisco Unified CME extension numbers.

The Tcl script that provides the service accepts PSTN DID numbers of
                              		  any length and maps them to the internal extension numbers that are assigned by
                              		  a system administrator. Where necessary, a prefix is appended to the DID digits
                              		  to create a valid extension number. The script uses the parameters that you
                              		  input to determine the valid range of digits to be accepted from the CO, the
                              		  valid range of digits in the local dial plan, and the prefix to append, if
                              		  necessary. The script also handles DID calls that map to invalid extension
                              		  numbers. A prompt is played and the calls are disconnected.

## Examples

The following example configures Direct Inward Dial Digit Translation
                              		  Service on the Cisco Unified CME router. It sets a lower boundary of 00 and an
                              		  upper boundary of 79 for the range of digits in the Cisco Unified CME extension
                              		  dial plan. Notice that the length of the digit string is the same (2 digits)
                              		  for all related commands.

```
application
 service didapp tftp://192.168.254.254/scripts/did/app-THD-DID-2.0.0.1.tcl
  paramspace english index 1
  paramspace english language en
  paramspace english location tftp://192.168.254.254/apps/dir25/
  param secondary-prefix 4
  param did-prefix 5
  param co-did-min 00
  param co-did-max 79
  param store-did-min 00
  param store-did-max 79
```

### Related Commands

Command

Description

application

Enters application configuration mode.

service

Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application.

param co-did-max

Sets the upper boundary of the range of valid digits coming
                                          						from the PSTN Central Office (CO) that is used with the Direct Inward Dial
                                          						Digit Translation Service.

param co-did-min

Sets the lower boundary of the range of valid digits coming
                                          						from the PSTN Central Office (CO) that is used with the Direct Inward Dial
                                          						Digit Translation Service.

param store-did-min

Sets the lower boundary of the range of digits that is
                                          						valid in the Cisco Unified CME numbering plan that is used with the Direct
                                          						Inward Dial Digit Translation Service.

## param store-did-min

To set the lower boundary of the range of digits that is valid in the
                              		  Cisco Unified CME numbering plan used with the Direct Inward Dial (DID) Digit
                              		  Translation Service, use the param store-did-min command in application-parameter
                              		  configuration mode. To disable this option, use the no form of this command.

param store-did-min min-store-value

no param store-did-min min-store-value

### Syntax Description

min-store-value

Minimum value of digits in the Cisco Unified CME dial plan.
                                          						The digit string can be any length, but the string length must be the same in
                                          						the param co-did-max , param co-did-min , param store-did-max , and param store-did-min commands.

### Command Default

No minimum value is defined for the range of digits in the dial plan.

### Command Modes

Application-parameter configuration (config-app-param)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)XC

Cisco Unified CME 4.0

This command was introduced to replace the call application voice store-did-min command.

12.4(9)T

Cisco Unified CME 4.0

This command replaced the call application voice store-did-min command and was integrated into Cisco IOS Release
                                          						12.4(9)T.

### Usage Guidelines

This command defines the lower limit of the range of digits in the
                              		  site dial plan when it is used with the Cisco Unified CallManager Express
                              		  (Cisco Unified CME) DID Digit Translation Service. This service provides number
                              		  translation for DID calls when the range of DID digits provided by the PSTN
                              		  Central Office (CO) does not match the digits in the Cisco Unified CME
                              		  extension numbers.

The Tcl script that provides the service accepts PSTN DID numbers of
                              		  any length and maps them to the internal extension numbers that are assigned by
                              		  a system administrator. Where necessary, a prefix is appended to the DID digits
                              		  to create a valid extension number. The script uses the parameters that you
                              		  input to determine the valid range of digits to be accepted from the CO, the
                              		  valid range of digits in the local dial plan, and the prefix to append, if
                              		  necessary. The script also handles DID calls that map to invalid extension
                              		  numbers: a prompt is played and the calls are disconnected.

## Examples

The following example configures DID Digit Translation Service on the
                              		  Cisco Unified CME router. It sets a lower boundary of 00 and an upper boundary
                              		  of 79 for the range of digits in the Cisco Unified CME extension dial plan.

```
application
 service didapp tftp://192.168.254.254/scripts/did/app-THD-DID-2.0.0.1.tcl
  paramspace english index 1
  paramspace english language en
  paramspace english location tftp://192.168.254.254/apps/dir25/
  param secondary-prefix 4
  param did-prefix 5
  param co-did-min 00
  param co-did-max 79
  param store-did-min 00
  param store-did-max 79
```

### Related Commands

Description

application

Enters application configuration mode.

service

Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application.

param co-did-max

Sets the upper boundary of the range of valid digits coming
                                          						from the PSTN Central Office (CO) that is used with the DID Digit Translation
                                          						Service.

param co-did-min

Sets the lower boundary of the range of valid digits coming
                                          						from the PSTN Central Office (CO) that is used with the DID Digit Translation
                                          						Service.

param store-did-max

Sets the upper boundary of the range of digits that is
                                          						valid in the Cisco Unified CME numbering plan that is used with the DID Digit
                                          						Translation Service.

## param voice-mail

To set an alternate destination number to which to route calls that
                              		  cannot be connected to a hunt group that is part of a Cisco Unified CME B-ACD
                              		  service, use the param voice-mail command
                              		  in application-parameter configuration mode. To return to the
                              		  default, use the no form of this command

param voice-mail number

no param voice-mail number

### Syntax Description

number

Extension number to which to route calls. The number must
                                          						be associated with a dial peer that is reachable by the Cisco Unified CME
                                          						system.

### Command Default

No alternate destination number is set.

### Command Modes

Application-parameter configuration (config-app-param)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(14)T

Cisco CME 3.3

This command was introduced to replace the call application voice voice-mail command.

### Usage Guidelines

This command is used with the Cisco Unified CME Basic Automatic Call
                              		  Distribution and Auto-Attendant (B-ACD) service. This command is configured
                              		  under the service command for an AA service.

Calls are diverted to an alternate destination only when one of the
                              		  following criteria is met:

- The hunt group to which the call has been transferred is
                                 			 unavailable because all members are logged out.

- The call-queue maximum retry timer has expired.

The alternate destination can be any number at which you can assure
                              		  call coverage, such as a voice-mail number, a permanently staffed number, or a
                              		  number that rings an overhead night bell. Once a call is diverted to an
                              		  alternate destination, it is no longer controlled by the B-ACD service. This
                              		  parameter is set with the param voice-mail command.

If you send calls to a voice-mail system as an alternate destination,
                              		  be sure to set up the voice-mail system as specified in the documentation for
                              		  the system.

If you specify a number for an alternate destination, the number must
                              		  be associated with a dial peer that is reachable by the Cisco Unified CME
                              		  system.

For any configuration changes to take effect, you must reload the
                              		  Cisco Unified CME B-ACD scripts.

For more information about B-ACD, see the Cisco Unified CallManager Express B-ACD and Tcl Call-Handling
                                 			 Applications document for your release.

## Examples

The following example sets parameters for an AA application called aa
                              		  and a call-queue application called queue. The direct-dial number to reach the
                              		  AA service is (800) 555-0100. Callers to this number can press 1 to be
                              		  connected to the ephone hunt group with the pilot number 5071 or can press 2 to
                              		  dial an extension number of 4 or fewer digits.

If a caller presses 2 and all the phones in ephone-hunt group 10 are
                              		  busy, the call is put into a queue for hunt group 10. Every 60 seconds, the
                              		  caller hears the second greeting, which is “Please continue to hold. An agent
                              		  will be with you shortly.” Every 15 seconds, the call-queue service tries again
                              		  to connect the call to the hunt group. If no phones become available before 700
                              		  seconds expire, the call is routed to extension 5000, which is the alternate
                              		  destination. If that extension is busy, the call-queue service retries it 2
                              		  times more. If the call still cannot be connected, it is disconnected.

```
dial-peer voice 1000 pots 
 service aa 
 port 1/1/0 
 incoming called-number 8005550100
ephone-hunt 10 sequential 
 pilot 5071
 list 5011, 5012, 5013, 5014, 5015
!
application 
 service callq tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd.tcl
  param queue-manager-debugs 1
  param aa-hunt1 5071
  param number-of-hunt-grps 1
  param queue-len 10
!
 service aa tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl
  paramspace english location tftp://192.168.254.254/user1/prompts/ 
  paramspace english index 0
  paramspace english language en
  param aa-pilot 8005550100 
  param welcome-prompt _aa_welcome.au
  param number-of-hunt-groups 1
  param dial-by-extension-option 2
  param max-extension-length 4
  param service-name callq 
  param handoff-string aa
  param second-greeting-time 60 
  param call-retry-timer 15 
  param max-time-call-retry 700 
  param voice-mail 5000 
  param max-time-vm-retry 2
```

### Related Commands

Description

application

Enters application configuration mode.

service

Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application.

## param welcome-prompt

To specify an audio file containing a prompt to be played as a
                              		  welcome for callers to an automated attendant (AA) that is part of a Cisco
                              		  Unified CME B-ACD service, use the param welcome-prompt command
                              		  in application-parameter configuration mode. To return to the
                              		  default, use the no form of this command.

param welcome-prompt audio-filename

no param welcome-prompt audio-filename

### Syntax Description

audio-filename

Identifier part of name of the audio file that contains the
                                          						welcome greeting to be played when callers first reach the Cisco Unified CME
                                          						B-ACD service. This name does not include the language prefix and it must begin
                                          						with an underscore. Default is _bacd_welcome.au.

### Command Default

The audio file named en_bacd_welcome.au is used as a welcome prompt.

### Command Modes

Application-parameter configuration (config-app-param)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(14)T

Cisco CME 3.3

This command was introduced to replace the call application voice voice-mail command.

### Usage Guidelines

This command is used with the Cisco Unified CME Basic Automatic Call
                              		  Distribution and Auto-Attendant (B-ACD) service. This command is configured
                              		  under the service command for an AA service.

Each AA service that is used with the Cisco Unified CME B-ACD service
                              		  needs a welcome greeting to tell callers the destination they have reached and,
                              		  sometimes, the options that they have. The en_bacd_welcome. au audio file is
                              		  used by default. It announces “Thank you for calling,” and includes a
                              		  two-second pause after the message. The filename of the welcome prompt audio
                              		  file has two parts: a two-letter prefix that denotes a language code specified
                              		  in the paramspace language command, and the identifying part that
                              		  indicates the purpose of the file. In the default welcome prompt audio file,
                              		  the prefix is en and the identifying part is _bacd_welcome.au. Note that the
                              		  identifying part starts with an underscore.

If your Cisco Unified CME B-ACD service uses a single AA application,
                              		  you can record a custom welcome greeting in the audio file named
                              		  en_welcome_prompt.au and record instructions about menu choices in the audio
                              		  file named en_bacd_options_menu.au.

If your Cisco Unified CME B-ACD service uses multiple AA
                              		  applications, you will need separate greetings and menu options for each AA.
                              		  Use the following guidelines:

- Record a separate welcome prompt for each AA application, using a
                                 			 different name for the audio file for each welcome prompt. For example,
                                 			 en_welcome_aa1.au and en_welcome_aa2.au. The welcome prompts that you record in
                                 			 these files should include both the greeting and the instructions about menu
                                 			 options.

- Record silence in the audio file en_bacd_options_menu.au. A
                                 			 minimum of one second of silence must be recorded. Note that you cannot change
                                 			 the identifier part of the name of this audio file.

For any Cisco Unified CME B-ACD configuration changes to take effect,
                              		  you must reload the scripts.

For more information, see the Cisco Unified CallManager Express B-ACD and Tcl Call-Handling
                                 			 Applications document for your release.

## Examples

The following example sets parameters for two AA applications, called
                              		  aa1 and aa2, and a call-queue application called queue. The direct-dial numbers
                              		  to reach the AA services are (800) 555-0100 for aa1 and (800) 555-0110 for aa2.
                              		  Callers to aa1 can press 1 to be connected to the ephone hunt group with the
                              		  pilot number 5071 or can press 2 to dial an extension number of 4 or fewer
                              		  digits. Callers to aa2 can press 2 to dial an extension number of 4 or fewer
                              		  digits or press 3 to be connected to the ephone hunt group with the pilot
                              		  number 5073. Both AAs share an operator hunt group, which is menu option 4.

The welcome prompt for aa1 is “Thank you for calling the Sales
                              		  department. Press 1 to place an order. Press 2 if you know the extension of the
                              		  party you want, or press 0 to speak to an operator.” The filename of the audio
                              		  file that contains this welcome prompt is en_aa1_welcome.au.

The welcome prompt for aa2 is “Thank you for calling the Service
                              		  department. Press 2 if you know the extension of the party you want. Press 3 to
                              		  speak to a service technician or press 0 to speak to an operator.” The filename
                              		  of the audio file that contains this welcome prompt is en_aa2_welcome.au.

```
dial-peer voice 1000 pots 
 service aa1 
 port 1/1/0 
 incoming called-number 8005550100
dial-peer voice 1100 pots 
 service aa2 
 port 1/1/1 
 incoming called-number 8005550110
ephone-hunt 10 sequential 
 pilot 5071
 list 5011, 5012, 5013, 5014, 5015
ephone-hunt 11 sequential 
 pilot 5073
 list 5021, 5022, 5023, 5024, 5025
!
application 
 service callq tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd.tcl
  param queue-manager-debugs 1
  param aa-hunt1 5071
  param aa-hunt3 5073
  param aa-hunt4 6000
  param number-of-hunt-grps 3
  param queue-len 10
!
 service aa1 tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl
  paramspace english location tftp://192.168.254.254/user1/prompts/ 
  paramspace english index 0
  paramspace english language en
  param aa-pilot 8005550100 
  param welcome-prompt _aa1_welcome.au
  param number-of-hunt-groups 2
  param dial-by-extension-option 2
  param max-extension-length 4
  param service-name callq 
  param handoff-string aa1
  param second-greeting-time 60 
  param call-retry-timer 15 
  param max-time-call-retry 700 
  param voice-mail 5000 
  param max-time-vm-retry 2 
 service aa2 tftp://192.168.254.254/user1/CallQ/B-ACD/app-b-acd-aa.tcl
  paramspace english location tftp://192.168.254.254/user1/prompts/ 
  paramspace english index 0
  paramspace english language en
  param aa-pilot 8005550110 
  param welcome-prompt _aa2_welcome.au
  param number-of-hunt-groups 2
  param dial-by-extension-option 2
  param max-extension-length 4
  param service-name callq 
  param handoff-string aa2
  param second-greeting-time 60 
  param call-retry-timer 15 
  param max-time-call-retry 700 
  param voice-mail 5000 
  param max-time-vm-retry 2
```

### Related Commands

Description

application

Enters application configuration mode.

service

Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application.

## paramspace callsetup after-hours-exempt

To specify that an individual dial peer does not have any of its
                              		  calls blocked by the Cisco router even though call blocking has been enabled,
                              		  use the paramspace callsetup after-hours-exempt command in dial-peer
                              		  configuration mode. To return to the default, use the no form of this command.

paramspace callsetup after-hours-exempt { true | false }

no paramspace callsetup after-hours-exempt

### Syntax Description

true

Dial peer is exempt from call-blocking configuration.

false

Dial peer is subject to call-blocking configuration. This
                                          						is default.

### Command Default

All dial peers are subject to call-blocking configuration.

### Command Modes

Dial-peer configuration (config-dial-peer)

## Command History

Cisco IOS Release

Cisco Products

Modification

12.4(4)T

Cisco CME 3.4 Cisco SRST 3.4

This command was introduced.

### Usage Guidelines

This command is intended to allow H.323 and SIP trunk calls to
                              		  utilize the voice gateway in spite of the the after-hours configuration in
                              		  Cisco Unified CME or Cisco Unified SRST.

A Cisco voice gateway (session application) accesses the after-hours
                              		  call-blocking configuration set by Cisco Unified CME or Cisco Unified SRST and
                              		  blocks all SCCP, SIP, H.323, and POTS calls that go through the Cisco
                              		  router regardless of whether the call is from a phone controlled by the Cisco
                              		  router or from a phone controlled by some other call control application, such
                              		  as Cisco Unified CallManager.

To disable the After Hours Call Blocking feature for incoming calls
                              		  from phones other than those registered to a Cisco Unified CME or Cisco Unified
                              		  SRST router, use this command to exempt an individual H.323, SIP, or POTS dial
                              		  peer from the call blocking configuration.

To disable the After Hours Call Blocking feature for an individual IP
                              		  phone registered in Cisco Unified CME or Cisco Unified SRST:

- In Cisco CME 3.4 and later, disable the After Hours Call Blocking
                                 			 feature for a directory number on a SIP phone by using the after-hour exempt command in voice register pool or voice
                                 			 register dn configuration mode.

- In Cisco CME 3.0 and later, disable the After Hours Call Blocking
                                 			 feature for an individual SCCP phone by using the after-hour exempt command in ephone or ephone-template
                                 			 configuration mode.

- In Cisco SIP SRST 3.4 and later, disable the After Hours Call
                                 			 Blocking feature for SIP phones in a voice register pool by using the after-hour exempt command in voice register pool
                                 			 configuration mode.

- In Cisco SRST, you cannot create an exemption for an individual
                                 			 phone from the call-blocking configuration.

## Examples

The following example shows how to set the After Hours Call Blocking
                              		  feature in Cisco Unified CME, and how to configure a particular dial peer (255)
                              		  so that outgoing calls through this dial peer are exempt from this after-hours
                              		  call blocking configuration:

```
Router(config)# telephony-service Router(config-telephony)# after-hours block pattern 1 9011 Router(config-telephony)# exit Router(config)# dial-peer voice 255 voip Router(config-dial-peer)# paramspace callsetup after-hours-exempt true
```

### Related Commands

Description

after-hour exempt

Specifies that a SCCP phone does not have any of its
                                          						outgoing calls blocked even though call blocking has been defined.

after-hour exempt (voice register dn)

Specifies that an individual SIP IP phone or a phone
                                          						extension on a SIP IP phone does not have any of its outgoing calls blocked
                                          						even though call blocking has been defined.

after-hour exempt (voice register pool)

Specifies that an individual SIP IP phone or phones in a
                                          						voice register pool does not have any of its outgoing calls blocked even though
                                          						call blocking has been defined.

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

## park reservation-group

To assign a call-park reservation group to a phone, use the reservation-group command in ephone, ephone-template, voice register pool, or
                              		  voice register template configuration mode. To remove the group from the phone,
                              		  use the no form of this command.

park reservation-group group-number

no park reservation-group

### Syntax Description

group-number

Unique number that identifies the reservation group. String
                                          						can contain up to 32 digits.

### Command Default

Extension does not belong to any reservation group.

### Command Modes

Ephone configuration (config-ephone) Ephone-template configuration (config-ephone-template) Voice register pool configuration (config-register-pool) Voice register template configuration (config-register-temp)

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

This command allows you to assign ownership to call-park slots by
                              		  using Park Reservation Groups. A phone configured with a park reservation group
                              		  can retrieve calls only from park slots configured with the same park
                              		  reservation group. A phone without a park reservation group can retrieve calls
                              		  from any park slot without an assigned park reservation group.

To assign a reservation group to a park-slot extension, use the park-slot reservation-group command.

If you use a template to apply a command to a phone and you also use
                              		  the same command in ephone or voice register pool configuration mode for the
                              		  same phone, the value that you set in the phone configuration mode has
                              		  priority.

## Examples

The following example shows park reservation-group 1 is assigned to
                              		  phone 3 (SCCP). When calls for the Pharmacy are parked at extension 8126, phone
                              		  3 can retrieve them:

```
ephone-dn  26
 number 8126
 park-slot reservation-group 1 timeout 15 limit 2 transfer 8100
 description park slot for Pharmacy
!
!
ephone  3
 park reservation-group 1
 mac-address 002D.264E.54FA
 type 7962
 button  1:3
```

The following example shows park reservation-group 1 is assigned to
                              		  phone 120 (SIP). When calls for the Pharmacy are parked at extension 8126,
                              		  phone 120 can retrieve them:

```
voice register pool  120
 park reservation-group 1
 id mac 0030.94C2.A22A
 type 7962
 number 1 dn 20
```

### Related Commands

Command

Description

call-park system

Defines system parameters for the call-park feature.

park-slot

Creates an extension (call-park slot) at which calls can be
                                          						temporarily held (parked).

## park-slot

To create an extension (call-park slot) at which calls can be
                              		  temporarily held (parked), use the park-slot command in ephone-dn configuration
                              		  mode. To disable the extension, use the no form of this command.

park-slot [ directed ] [ reservation-group group-number ] [ reserved-for extension-number ] [ [ timeout seconds limit count ] [ notify extension-number [ only ]] [ recall ] [ transfer extension-number ] [ alternate extension-number ] [ retry seconds limit count ]]

no park-slot [ directed ] [ reservation-group group-number ] [ reserved-for extension-number ] [ [ timeout seconds limit count ] [ notify extension-number [ only ]] [ recall ] [ transfer extension-number ] [ alternate extension-number ] [ retry seconds limit count ]]

### Syntax Description

directed

(Optional) Enables Directed Call Park for this extension.

reservation-group group-number

(Optional) Reserves this slot for phones configured with
                                          						the same reservation group.

reserved-for extension-number

(Optional) Reserves this slot as a private park slot for
                                          						the phone with the specified extension number as its primary line. All lines on
                                          						that phone can use this park slot.

timeout seconds

(Optional) Sets the call-park reminder timeout in seconds.
                                          						Range: 0 to 65535. This reminder sends a 1-second ring to the IP phone that
                                          						parked the call and displays a message on the LCD panel of all phones in the
                                          						Cisco Unified CME system, indicating that a call is on hold. By default, the
                                          						reminder ring is sent only to the phone that parked the call.

limit count

(Optional) Sets a limit on the number of reminder or retry
                                          						timeouts. Range: 1 to 65535.

notify extension-number

(Optional) Sends a reminder ring to the specified extension
                                          						in addition to the reminder ring that is sent to the phone that parked the
                                          						call.

only

(Optional) Sends a reminder ring only to the extension
                                          						specified with the notify keyword and does not send a
                                          						reminder ring to the phone that parked the call. This option allows all
                                          						reminder rings for parked calls to be sent to a receptionist’s phone or an
                                          						attendant’s phone, for example.

recall

(Optional) Returns the call to the phone that parked it
                                          						after the timeout expires.

transfer extension-number

(Optional) Returns the call to the specified extension
                                          						after the timeout expires.

alternate extension-number

(Optional) Returns the call to this second target number if
                                          						the recall or transfer target phone is in use on any of its extensions (ringing
                                          						or connected).

retry seconds

(Optional) Sets the delay before another attempt to recall
                                          						or transfer a parked call, in seconds. Range: 0 to 65535. Number of attempts is
                                          						set by the limit keyword.

### Command Default

No call-park slot is defined.

### Command Modes

Ephone-dn configuration (config-ephone-dn)

## Command History

Release

Cisco Product

Modification

12.3(7)T

Cisco CME 3.1

This command was introduced.

12.4(4)XC

Cisco Unified CME 4.0

The reserved-for , recall , transfer , alternate , and retry keywords were added.

12.4(9)T

Cisco Unified CME 4.0

This command was integrated into Cisco IOS Release
                                          						12.4(24)T.

12.4(22)YB

Cisco Unified CME 7.1

The directed and reservation-group keywords and
                                          						support for SIP phones was added.

12.4(24)T

Cisco Unified CME 7.1

This command was integrated into Cisco IOS Release
                                          						12.4(24)T.

### Usage Guidelines

This command creates a call-park slot that is a floating extension,
                              		  or ephone-dn that is not bound to a physical phone, at which phone users can
                              		  place calls on hold for later retrieval from the same phone or from another
                              		  phone.

At least one call-park slot must be defined with this command before
                              		  the Park soft key displays on IP phones in a Cisco Unified CME system.

Phone users park calls using the Park soft key. A phone user can then
                              		  retrieve a call by dialing the extension number of the call-park slot. On SCCP
                              		  phones, the phone user who parks the call can also retrieve the call by using
                              		  the PickUp soft key and an asterisk (*). Other SCCP phone users can retrieve
                              		  the call by using the PickUp soft key and dialing the extension number of the
                              		  call-park slot.

Calls can also be transferred to a call-park slot using the Transfer
                              		  key; a transfer to a call-park slot is always a blind transfer. Calls can also
                              		  be forwarded to a call-park slot, and callers can directly dial call-park
                              		  slots.

When a call that uses a G.711 codec is parked, the caller hears the
                              		  music-on-hold (MOH) audio stream; otherwise, the caller hears the on-hold tone.

The directed keyword enables the extension as a
                              		  park slot for Directed Call Park. To retrieve a call from a directed call-park
                              		  slot, you must define the retrieval prefix with the fac command. The retrieval prefix is
                              		  supported for both SCCP and SIP phones.

The reservation-group keyword allows you to
                              		  assign ownership to call-park slots by using Park Reservation Groups. A park
                              		  slot configured with a park reservation group can only be used by phones
                              		  configured with the same park reservation group. A park slot without a park
                              		  reservation group can be used by any phone not assigned to a park reservation
                              		  group.

A reminder ring can be sent to the extension that parked the call by
                              		  using the timeout keyword, which sets the interval
                              		  length to wait before sending call-park reminder rings. The number of time-out
                              		  intervals and reminder rings are configured with the limit keyword and argument. For example, a
                              		  limit of 3 timeout intervals sends 2 reminder rings (interval 1, ring 1,
                              		  interval 2, ring 2, interval 3). The timeout and limit keywords and arguments also set the
                              		  maximum time that calls stay parked. For example, a timeout interval of 10
                              		  seconds and a limit of 5 timeout intervals ( park-slot timeout 10 limit 5 ) will park calls for approximately 50 seconds.

If the timeout keyword is not used with this
                              		  command, no reminder ring is sent to the extension that parked the call. If the timeout keyword is used, a reminder ring is
                              		  sent only to the extension that parked the call unless the notify keyword is also used to specify an
                              		  additional extension number to receive a reminder ring. When an additional
                              		  extension number is specified using the notify keyword, the phone user at that
                              		  extension can retrieve a call from this slot by pressing the PickUp soft key
                              		  and an asterisk (*).

Each call-park slot can hold one call at a time, so the number of
                              		  simultaneous calls that can be parked is equal to the number of slots that have
                              		  been created. The reserved-for keyword creates a call-park slot
                              		  that is dedicated for use by one extension so that extension always has a slot
                              		  available at which to park a call. With nonreserved slots, multiple call-park
                              		  slots can be created with the same extension number so that all the calls that
                              		  are parked for a particular group can be parked at a known extension number.
                              		  For example, at a hardware store, calls for the plumbing department can be
                              		  parked at extension 101, calls for lighting can be parked at 102, and so forth.
                              		  Then, anyone in the plumbing department can pick up calls from extension 101.
                              		  When multiple calls are parked at the same extension number, they are picked up
                              		  in the order in which they were parked; that is, the call that has been parked
                              		  the longest is the first call picked up from that extension number.

IP phone users park calls at their dedicated call-park slots using
                              		  the Park soft key. Phone users can also transfer calls to dedicated call-park
                              		  slots using the Transfer soft key and a standard or custom feature access code
                              		  (FAC) for call park. On analog phones, users transfer calls to dedicated
                              		  call-park slots using hookflash and a standard or custom FAC for call park. The
                              		  standard FAC for call park is **6. Custom FACs are created using the fac command.

If a dedicated park slot is not found for an ephone-dn attempting to
                              		  park a call, Cisco Unified CME uses the standard call-park procedure; that is,
                              		  the system searches for a preferred park slot (one with an ephone-dn number
                              		  that matches the last two digits of the ephone-dn attempting to park the call)
                              		  and if none is found, uses any available call-park slot.

If a name has been specified for a call-park slot, that name is
                              		  displayed instead of an extension number on a recall or transfer of the call.

A parked call can have the following dispositions after its timeouts
                              		  expire:

- Recall—If you specify that a call should be recalled to the
                                 			 parking phone after the timeout interval expires, the call is always returned
                                 			 to the phone's primary extension number, regardless of which extension on the
                                 			 phone did the parking.

- Transfer—If you specify a transfer target, the call is transferred
                                 			 to the specified number after the timeout intervals expire instead of returning
                                 			 to the primary number of the phone that did the parking.

- Alternate—You can also specify an alternate target extension to
                                 			 which to transfer a parked call if the recall or transfer target is in use. In use is defined as either ringing or connected to a call.
                                 			 For example, a call is parked at the dedicated park slot for the phone with the
                                 			 primary extension of 2001. After the timeouts expire, the system attempts to
                                 			 recall the call to extension 2001, but that line is now connected to a
                                 			 different call. The system transfers the call to the alternate target that was
                                 			 specified when the park slot was defined.

- Disconnect—When a timeout limit is set and no other disposition
                                 			 has been specified, a call parked at a call-park slot is disconnected after the
                                 			 number of reminder timeouts are reached.

## Examples

## Examples

The following example shows a basic call-park slot at extension 1001.
                              		  After a call is parked at this number, the system provides 10 reminder rings at
                              		  intervals of 30 seconds to the extension that parked the call. Any phone can
                              		  retrieve calls parked at this extension.

```
ephone-dn 45
 number 1001
 park-slot timeout 30 limit 10
```

## Examples

The following example shows two call-park slots, extension 3110 and
                              		  3111, that can be used to park calls for the pharmacy using Directed Call Park.

```
ephone-dn  10
 number 3110
 park-slot directed
 description park-slot for Pharmacy
!
ephone-dn  11
 number 3111
 park-slot directed
 description park-slot for Pharmacy
```

## Examples

The following example shows park reservation groups set up for two
                              		  call-park slots. Extension 8126 is configured for group 1 and assigned to
                              		  phones 3 and 4. Extension 8127 is configured for group 2 and assigned to phones
                              		  10 and 11. When calls for the Pharmacy are parked at extension 8126, only
                              		  phones 3 and 4 can retrieve them.

```
ephone-dn  26
 number 8126
 park-slot reservation-group 1 timeout 15 limit 2 transfer 8100
 description park slot for Pharmacy
!
ephone-dn  27
 number 8127
 park-slot reservation-group 2 timeout 15 limit 2 transfer 8100
 description park slot for Auto
!
!
ephone  3
 park reservation-group 1
 mac-address 002D.264E.54FA
 type 7962
 button  1:3
!
ephone  4
 park reservation-group 1
 mac-address 0030.94C3.053E
 type 7962
 button  1:4
!
ephone  10
 park reservation-group 2
 mac-address 00E1.CB13.0395
 type 7960
 button  1:10
!
ephone  11
 park reservation-group 2
 mac-address 0016.9DEF.1A70
 type 7960
 button  1:11
```

## Examples

The following example shows a dedicated call-park slot, 2558, that is
                              		  reserved for the phone that has the primary extension of 2977. Both extension
                              		  2977 and 2976 are on the same phone, so they both can use this slot, which is
                              		  reserved only for the extensions on that phone. After three timeout intervals
                              		  of 60 seconds, a parked call is recalled to extension 2977. If extension 2977
                              		  is busy, the call is rerouted to extension 3754.

```
ephone-dn 24
 number 2977
 
ephone-dn 25
 number 2976
 
ephone-dn 27
 number 3754
 
ephone-dn 30
 number 2558
 name Park 2977
 park-slot reserved-for 2977 timeout 60 limit 3 recall alternate 3754
 
ephone 44
 button 1:24 2:25
 
ephone 45
 button 1:27
```

### Related Commands

Command

Description

call-park system

Defines system parameters for the call-park feature.

fac

Enables standard FACs or creates custom FACs.

number

Associates a telephone or extension number with a directory
                                          						number.

park reservation-group

Assigns a call-park reservation group to a phone.

## password
                        	 (auto-register)

To configure the
                              		  mandatory password for automatic registration of SIP phones with the Cisco
                              		  Unified CME system, use the password command in voice auto register configuration mode. This
                              		  command is a sub-mode CLI of the command auto-register . To disable configuring password for auto registration of SIP
                              		  phones, use the no form of
                              		  this command.

password [0|6] string

no password

### Syntax Description

password string

The
                                          						mandatory word string that administrator provides for auto registration of
                                          						phones on Unified CME.

### Command Default

By default, this
                              		  command is disabled.

### Command Modes

voice auto register configuration (config-voice-auto-register)

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

Cisco IOS XE Gibraltar 16.11.1a Release

Unified CME 12.6

The command was enhanced for password encryption, based on Unified CME password policy.

### Usage Guidelines

This command
                              		  enables the administrator to configure the password credentials for SIP phones
                              		  auto registering on Unified CME. It is mandatory that the password is
                              		  configured before assigning the DN range.

From Unified CME 12.6 onwards, you must configure password encryption using the parameters [0|6] . This in accordance with Unified CME Password Policy. The 0 in the parameter [0|6] mentioned in the CLI command represents
                              plain, unencrypted text and 6 represents level 6 password encryption.

## Examples

The following
                              		  example shows how to configure password for auto registration of SIP phones:

```
Router(config)#voice register global
Router(config-register-global)#auto-register
Router(config-voice-auto-register)# ?

VOICE auto register configuration commands: auto-assign Define DN range for auto assignment default Set a command to its defaults exit Exit from voice register group configuration mode no Negate a command or set its defaults password Default password for auto-register phones service-enable Enable SIP phone Auto-Registration template Default template for auto-register phones

Router(config-voice-auto-register)#password ?
 WORD Password string
```

### Related Commands

Command

Description

service-enable (auto-register)

Temporarily disables the auto registration process, but retains
                                          						the password and DN range configurations. Once auto-register command is
                                          						entered, the service is enabled by default.

auto-register

Enables
                                          						automatic registration of SIP phones with the Cisco Unified CME system.

auto-assign (auto-register)

Configures the mandatory range of directory numbers for phones
                                          						auto registering on Unified CME.

template (auto-register)

Creates
                                          						a basic configuration template that supports all the configurations available
                                          						on the voice register template.

auto-reg-ephone

Enables automatic registration of ephones with the Cisco Unified CME system.

## password-persistent

To configure password-persistent option for a vpn-profile, use
                              		  the password-persistent command in vpn-profile configuration mode.

password-persistent [ enable | disable ]

### Syntax Description

enable

Enables password-persistent to authenticate.

disable

Disables password-persistent to authenticate.

### Command Default

Password-persistent is disabled.

### Command Modes

Vpn-profile configuration (conf-vpn-profile)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.1(3)T

Cisco Unified CME 8.5

This command was introduced.

### Usage Guidelines

Use this command to enable or disable password-persistent option for
                              		  a vpn-profile.

## Examples

The following example shows the password-persistent command enabled
                              		  for vpn-profile 2:

```
Router#show run
!
!
voice service voip
 ip address trusted list
  ipv4 20.20.20.1
 vpn-group 1
  vpn-gateway 1 https://9.10.60.254/SSLVPNphone
  vpn-trustpoint 1 trustpoint cme_cert root
  vpn-hash-algorithm sha-1
 vpn-profile 1
  keepalive 50
  host-id-check disable
 vpn-profile 2
  mtu 1300
  password-persistent enable
  host-id-check enable
 sip
!
voice class media 10
 media flow-around
!
```

### Related Commands

Command

Description

vpn-profile

Defines a VPN-profile.

## pattern (voice register dialplan)

To define a dial pattern for a SIP dial plan, use the pattern command in voice register dialplan
                              		  configuration mode. To remove the pattern, use the no form of this command.

pattern tag string [ button button-number ] [ timeout seconds ] [ user { ip | phone }]

no pattern tag

### Syntax Description

tag

Number that identifies the dial pattern. Range: 1 to 24.

string

Dial pattern, such as the area code, prefix, and first one
                                          						or two digits of the telephone number, plus wildcard characters or dots (.) for
                                          						the remainder of the dialed digits.

button button-number

(Optional) Button to which the dial pattern applies.

timeout seconds

(Optional) Time, in seconds, that the system waits before
                                          						dialing the number entered by the user. Range: 0 to 30. To have the number
                                          						dialed immediately, specify 0. If this parameter is not used, the phone's
                                          						default interdigit timeout value is used (10 seconds).

user

(Optional) Tag that automatically gets added to the dialed
                                          						number. Do not use this keyword if Cisco Unified CME is the only SIP call
                                          						agent.

ip

(Optional) Sets the value of the user tag to IP in the
                                          						dialed number.

phone

(Optional) Sets the value of the user tag to phone in the
                                          						dialed number.

### Command Default

No pattern is defined.

### Command Modes

Voice register dialplan configuration (config-register-dialplan)

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

This command defines a pattern of dialed digits that are matched by
                              		  the phone and passed to Cisco Unified CME to initiate a call. Dial strings that
                              		  match the pattern trigger the sending of a SIP INVITE message to Cisco Unified
                              		  CME. Patterns are matched sequentially in order of the tag number.

You must first use the type command to specify the type of phone
                              		  that the dial plan is being defined for before you can enter a pattern. Enter
                              		  this command for each dial pattern that is part of the dial plan definition.
                              		  After you define a dial plan, assign it to a SIP phone by using the dialplan command.

The button keyword specifies the button to which
                              		  the dial pattern applies. If the user is initiating a call on line button 1,
                              		  only the dial patterns specified for button 1 apply. If this keyword is not
                              		  configured, the dial pattern applies to all lines on the phone. This keyword is
                              		  not supported on Cisco Unified IP Phones 7905 or 7912. The button number
                              		  corresponds to the order of the buttons on the side of the screen, from top to
                              		  bottom, with 1 being the top button.

The pattern command and filename command are mutually exclusive. You
                              		  can use either the pattern command to define dial patterns
                              		  manually for a dial plan, or the filename command to select a custom dial
                              		  pattern file that is loaded in system flash.

## Examples

The following example shows the dial patterns set for SIP dial plan
                              		  10:

```
Router(config)# voice register dialplan 10 Router(config-register-dialplan)# type 7905-7912 Router(config-register-dialplan)# pattern 52... Router(config-register-dialplan)# pattern 91.......
```

### Related Commands

Description

dialplan

Assigns a dial plan to a SIP phone.

filename

Specifies a custom configuration file that contains dial
                                          						patterns to use for the SIP dial plan.

show voice register dialplan

Displays all configuration information for a specific SIP
                                          						dial plan.

type (voice register dialplan)

Defines a phone type for a SIP dial plan.

## pattern direct

To configure the dual tone multifrequency (DTMF) digit pattern
                              		  forwarding necessary to activate the voice-mail system when a user presses the
                              		  Messages button on an IP phone in a Cisco CallManager Express (Cisco CME)
                              		  system, use the pattern direct command in voice-mail integration
                              		  configuration mode. To disable DTMF pattern forwarding when a user presses the
                              		  Messages button on a phone, use the no form of this command.

pattern direct tag1 { CDN | CGN | FDN } [ tag2 { CDN | CGN | FDN }] [ tag3 { CDN | CGN | FDN }] [last-tag]

no pattern direct

### Syntax Description

tag1

Alphanumeric string of fewer than four DTMF digits in
                                          						length. The alphanumeric string can consist of a combination of four letters
                                          						(A, B, C, and D), two symbols (* and #), and ten digits (0 to 9). The tag
                                          						numbers match the numbers defined in the voice-mail system’s integration file
                                          						and immediately precede the number of the calling party, the number of the
                                          						called party, or a forwarding number.

CDN

Called number (CDN) information is sent to the voice-mail
                                          						system.

CGN

Calling number (CGN) information is sent to the voice-mail
                                          						system.

FDN

Forwarding number (FDN) information is sent to the
                                          						voice-mail system.

tag2, tag3

(Optional) Same as tag1 . The router supports a maximum
                                          						of four tags.

last-tag

(Optional) Same as tag1 . This tag indicates the end of
                                          						the pattern.

### Command Default

This feature is disabled.

### Command Modes

Voice-mail integration configuration (config-vm-integration)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(2)XT

2.0

This command was introduced

12.2(8)T

2.0

This command was integrated into Cisco IOS Release
                                          						12.2(8)T.

### Usage Guidelines

The pattern direct command is used to configure the sequence
                              		  of dual tone multifrequency (DTMF) digits passed to a voice-mail system
                              		  attached to the router through one or more voice ports. When a call is placed
                              		  directly from a Cisco IP phone attached to the router, the voice-mail system
                              		  expects to receive a sequence of DTMF digits at the beginning of the call to
                              		  identify the user’s mailbox, accompanied by a string of digits to indicate that
                              		  the caller is attempting to access the designated mailbox in order to retrieve
                              		  messages.

Although it is unlikely that you will use multiple instances of the CDN , CGN , or FDN keywords in a single command line, it is permissible to do so.

## Examples

The following example sets the DTMF pattern for a calling number
                              		  (CGN) for a direct call to the voice-mail system:

```
Router(config) vm-integration Router(config-vm-integration) pattern direct 2 CGN *
```

### Related Commands

Description

pattern ext-to-ext busy

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension fails to connect to a
                                          						busy extension and the call is forwarded to voice mail.

pattern ext-to-ext no-answer

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension attempts to connect
                                          						to an extension that does not answer and the call is forwarded to voice mail.

pattern trunk-to-ext busy

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an external trunk call reaches a busy
                                          						extension and the call is forwarded to voice mail.

pattern trunk-to-ext no-answer

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when an external trunk call reaches an
                                          						unanswered extension and the call is forwarded to voice mail.

vm-integration

Enters voice-mail integration configuration mode and
                                          						enables voice-mail integration with DTMF and an analog voice-mail systems.

## pattern ext-to-ext busy

To configure the dual tone multifrequency (DTMF) digit pattern
                              		  forwarding necessary to activate a voice-mail system after an internal
                              		  extension attempts to connect to a busy extension and the call is forwarded to
                              		  voice mail, use the pattern ext-to-ext busy command in voice-mail integration
                              		  configuration mode. To disable the feature, use the no form of this command.

pattern ext-to-ext busy tag1 { CDN | CGN | FDN } [ tag2 { CDN | CGN | FDN }] [ tag3 { CDN | CGN | FDN }] [last-tag]

no pattern ext-to-ext busy

### Syntax Description

tag1

Alphanumeric string of fewer than four DTMF digits in
                                          						length. The alphanumeric string can consist of a combination of four letters
                                          						(A, B, C, and D), two symbols (* and #), and ten digits (0 to 9). The tag
                                          						numbers match the numbers defined in the voice-mail system’s integration file
                                          						and immediately precede the number of the calling party, the number of the
                                          						called party, or a forwarding number.

CDN

Called number (CDN) information is sent to the voice-mail
                                          						system.

CGN

Calling number (CGN) information is sent to the voice-mail
                                          						system.

FDN

Forwarding number (FDN) information is sent to the
                                          						voice-mail system.

tag2, tag3

(Optional) Same as tag1 . The router supports a maximum
                                          						of four tags.

last-tag

(Optional) Same as tag1 . This tag indicates the end of
                                          						the pattern.

### Command Default

This feature is disabled.

### Command Modes

Voice-mail integration configuration (config-vm-integration)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(2)XT

Cisco ITS 2.0

This command was introduced.

12.2(8)T

Cisco ITS 2.0

This command was integrated into Cisco IOS Release
                                          						12.2(8)T.

12.2(13)T

Cisco SRST 2.02

This command was added for Cisco SRST.

### Usage Guidelines

The pattern ext-to-ext busy command is used to configure the sequence of
                              		  DTMF digits passed to a voice-mail system attached to the router through one or
                              		  more voice ports. When a call is routed to the voice-mail system by call
                              		  forward on busy from a Cisco IP phone attached to the router, the voice-mail
                              		  system expects to receive digits that identify the mailbox associated with the
                              		  forwarding phone together with digits that identify the extension number of the
                              		  calling IP phone.

Although it is unlikely that you will use multiple instances of the CDN , CGN , or FDN keywords in a single command line, it is
                              		  permissible to do so.

## Examples

The following example sets the DTMF pattern for a local call
                              		  forwarded on busy to the voice-mail system:

```
Router(config) vm-integration Router(config-vm-integration) pattern ext-to-ext busy 7 FDN * CGN *
```

### Related Commands

Description

pattern direct

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when the user presses the Messages button on the
                                          						phone.

pattern ext-to-ext no-answer

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension fails to connect to
                                          						an extension that does not answer and the call is forwarded to voice mail.

pattern trunk-to-ext busy

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an external trunk call reaches a busy
                                          						extension and the call is forwarded to voice mail.

pattern trunk-to-ext no-answer

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when an external trunk call reaches an
                                          						unanswered extension and the call is forwarded to voice mail.

vm-integration

Enters voice-mail integration configuration mode and
                                          						enables voice-mail integration with DTMF and an analog voice-mail systems.

## pattern ext-to-ext no-answer

To configure the dual tone multifrequency (DTMF) pattern forwarding
                              		  necessary to activate the voice-mail system once an internal extension fails to
                              		  connect to a non answering extension and the call is forwarded to voice mail,
                              		  use the pattern ext-to-ext no-answer command in voice-mail integration
                              		  configuration mode. To disable this feature, use the no form of this command.

pattern ext-to-ext no-answer tag1 { CDN | CGN | FDN } [ tag2 { CDN | CGN | FDN }] [ tag3 { CDN | CGN | FDN }] [last-tag]

no pattern ext-to-ext no-answer

### Syntax Description

tag1

Alphanumeric string of fewer than four DTMF digits in
                                          						length. The alphanumeric string can consist of a combination of four letters
                                          						(A, B, C, and D), two symbols (* and #), and ten digits (0 to 9). The tag
                                          						numbers match the numbers defined in the voice-mail system’s integration file
                                          						and immediately precede the number of the calling party, the number of the
                                          						called party, or a forwarding number.

CDN

Called number (CDN) information is sent to the voice-mail
                                          						system.

CGN

Calling number (CGN) information is sent to the voice-mail
                                          						system.

FDN

Forwarding number (FDN) information is sent to the
                                          						voice-mail system.

tag2, tag3

(Optional) Same as tag1 . The router supports a maximum
                                          						of four tags.

last-tag

(Optional) Same as tag1 . This tag indicates the end of
                                          						the pattern.

### Command Default

This feature is disabled.

### Command Modes

Voice-mail integration configuration (config-vm-integration)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(2)XT

Cisco ITS 2.0

This command was introduced.

12.2(8)T

Cisco ITS 2.0

This command was integrated into Cisco IOS Release
                                          						12.2(8)T.

12.2(13)T

Cisco SRST 2.02

This command was added for Cisco SRST.

### Usage Guidelines

The pattern ext-to-ext no-answer command is used to configure the
                              		  sequence of DTMF digits passed to a voice-mail system attached to the router
                              		  through one or more voice ports. When a call is routed to the voice-mail system
                              		  by call forward on no-answer from an IP phone attached to the router, the
                              		  voice-mail system expects to receive digits that identify the mailbox
                              		  associated with the forwarding phone together with digits that identify the
                              		  extension number of the calling IP phone.

Although it is unlikely that you will use multiple instances of the CDN , CGN , or FDN keywords in a single command line, it is
                              		  permissible to do so.

## Examples

The following example sets the DTMF pattern for a local call
                              		  forwarded on no-answer to the voice-mail system:

```
Router(config) vm-integration Router(config-vm-integration) pattern ext-to-ext no-answer 5 FDN * CGN *
```

### Related Commands

Description

pattern direct

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when the user presses the Messages button on the
                                          						phone.

pattern ext-to-ext busy

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension fails to connect to
                                          						an extension and the call is forwarded to voice mail.

pattern trunk-to-ext busy

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an external trunk call reaches a busy
                                          						extension and the call is forwarded to voice mail.

pattern trunk-to-ext no-answer

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when an external trunk call reaches an
                                          						unanswered extension and the call is forwarded to voice mail.

vm-integration

Enters voice-mail integration configuration mode and
                                          						enables voice-mail integration with DTMF and an analog voice-mail systems.

## pattern trunk-to-ext busy

To configure the dual tone multifrequency (DTMF) digit pattern
                              		  forwarding necessary to activate the voice-mail system once an external trunk
                              		  call reaches a busy extension and the call is forwarded to voice mail, use the pattern trunk-to-ext busy command in voice-mail integration
                              		  configuration mode. To return to the default, use the no form of this command.

pattern trunk-to-ext busy tag1 { CDN | CGN | FDN } [ tag2 { CDN | CGN | FDN }] [ tag3 { CDN | CGN | FDN }] [last-tag]

no pattern trunk-to-ext busy

### Syntax Description

tag1

Alphanumeric string of fewer than four DTMF digits in
                                          						length. The alphanumeric string can consist of a combination of four letters
                                          						(A, B, C, and D), two symbols (* and #), and ten digits (0 to 9). The tag
                                          						numbers match the numbers defined in the voice-mail system’s integration file
                                          						and immediately precede the number of the calling party, the number of the
                                          						called party, or a forwarding number.

CDN

Called number (CDN) information is sent to the voice-mail
                                          						system.

CGN

Calling number (CGN) information is sent to the voice-mail
                                          						system.

FDN

Forwarding number (FDN) information is sent to the
                                          						voice-mail system.

tag2, tag3

(Optional) Same as tag1 . The router supports a maximum
                                          						of four tags.

last-tag

(Optional) Same as tag1 . This tag indicates the end of
                                          						the pattern.

### Command Default

This feature is disabled by default.

### Command Modes

Voice-mail integration configuration (config-vm-integration)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(2)XT

Cisco ITS 2.0

This command was introduced.

12.2(8)T

Cisco SRST 2.02

This command was integrated into Cisco IOS Release
                                          						12.2(8)T.

12.2(13)T

Cisco ITS 2.0

This command was added for Cisco SRST.

### Usage Guidelines

The pattern trunk-to-ext busy command is used to configure the sequence of
                              		  DTMF digits passed to a voice-mail system attached to the router through one or
                              		  more voice ports. When a call is routed to the voice-mail system by call
                              		  forward on busy from an IP phone attached to the router, the voice-mail system
                              		  expects to receive a sequence of digits identifying the mailbox associated with
                              		  the forwarding phone together with digits indicating that the call originated
                              		  from a PSTN or VoIP caller.

Although it is unlikely that you will use multiple instances of the CDN , CGN , or FDN keywords in a single command line, it is
                              		  permissible to do so.

## Examples

The following example sets the DTMF pattern for call forwarding when
                              		  an external trunk call reaches a busy extension and the call is forwarded to
                              		  the voice-mail system:

```
Router(config) vm-integration Router(config-vm-integration) pattern trunk-to-ext busy 6 FDN * CGN *
```

### Related Commands

Description

pattern direct

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when the user presses the Messages button on the
                                          						phone.

pattern ext-to-ext busy

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension fails to connect to
                                          						an extension and the call is forwarded to voice mail.

pattern ext-to-ext no-answer

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension fails to connect to
                                          						an extension and the call is forwarded to voice mail.

pattern trunk-to-ext no-answer

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when an external trunk call reaches an
                                          						unanswered extension and the call is forwarded to voice mail.

vm-integration

Enters voice-mail integration configuration mode and
                                          						enables voice-mail integration with DTMF and an analog voice-mail systems.

## pattern trunk-to-ext no-answer

To configure the dual tone multifrequency (DTMF) digit pattern
                              		  forwarding necessary to activate the voice-mail system when an external trunk
                              		  call reaches an unanswered extension and the call is forwarded to voice mail,
                              		  use the pattern trunk-to-ext no-answer command in voice-mail integration
                              		  configuration mode. To disable this feature, use the no form of this command.

pattern trunk-to-ext no-answer tag1 { CDN | CGN | FDN } [ tag2 { CDN | CGN | FDN }] [ tag3 { CDN | CGN | FDN }] [last-tag]

no pattern trunk-to-ext no-answer

### Syntax Description

tag1

Alphanumeric string of fewer than four DTMF digits in
                                          						length. The alphanumeric string can consist of a combination of four letters
                                          						(A, B, C, and D), two symbols (* and #), and ten digits (0 to 9). The tag
                                          						numbers match the numbers defined in the voice-mail system’s integration file
                                          						and immediately precede the number of the calling party, the number of the
                                          						called party, or a forwarding number.

CDN

Called number (CDN) information is sent to the voice-mail
                                          						system.

CGN

Calling number (CGN) information is sent to the voice-mail
                                          						system.

FDN

Forwarding number (FDN) information is sent to the
                                          						voice-mail system.

tag2, tag3

(Optional) Same as tag1 . The router supports a maximum
                                          						of four tags.

last-tag

(Optional) Same as tag1 . This tag indicates the end of
                                          						the pattern.

### Command Default

This feature is disabled.

### Command Modes

Voice-mail integration configuration (config-vm-integration)

## Command History

Cisco IOS Release

Cisco CME Version

Modification

12.2(2)XT

2.0

This command was introduced.

12.2(8)T

2.0

This command was integrated into Cisco IOS Release
                                          						12.2(8)T.

12.2(13)T

2.02

This command was added for Cisco SRST.

### Usage Guidelines

The pattern trunk-to-ext no-answer command is used to configure the
                              		  sequence of DTMF digits passed to a voice-mail system attached to the router
                              		  through one or more voice ports. When a call is routed to the voice-mail system
                              		  by call forward on no-answer from an IP phone attached to the router, the
                              		  voice-mail system expects to receive digits that identify the mailbox
                              		  associated with the forwarding phone together with digits that indicate that
                              		  the call originated from a PSTN or VoIP caller.

Although it is unlikely that you will use multiple instances of the CDN , CGN , or FDN keywords in a single command line, it is
                              		  permissible to do so.

## Examples

The following example sets the DTMF pattern for call forwarding when
                              		  an external trunk call reaches an unanswered extension and the call is
                              		  forwarded to a voice-mail system:

```
Router(config) vm-integration Router(config-vm-integration) pattern trunk-to-ext no-answer 4 FDN * CGN *
```

### Related Commands

Description

pattern direct

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when the user presses the Messages button on the
                                          						phone.

pattern ext-to-ext busy

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension fails to connect to
                                          						an extension and the call is forwarded to voice mail.

pattern ext-to-ext no-answer

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension fails to connect to
                                          						an extension and the call is forwarded to voice mail.

pattern trunk-to-ext busy

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an external trunk call reaches a busy
                                          						extension and the call is forwarded to voice mail.

vm-integration

Enters voice-mail integration configuration mode and
                                          						enables voice-mail integration with DTMF and an analog voice-mail systems.

## phone-display

To enable a phone
                              		  user to display voice hunt group information using the Services button on the
                              		  phone, use the phone-display command in voice hunt group configuration mode. To
                              		  remove the configuration, use the no form of
                              		  this command.

phone-display

no phone-display

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

By default, this
                              		  command is disabled.

### Command Modes

## Command History

This
                                       					 command was introduced.

### Usage Guidelines

This command when
                              		  configured, enables the user to view the information of a specific voice hunt
                              		  group on the phone.

## Examples

The following
                              		  example shows how the voice hunt group display option is enabled for a phone :

```
Router(config)# voice hunt-group 1 parallel Router(config-voice-hunt-group)# phone-display
```

## phone-mode
                        	 only

To enable Jabber
                              		  phone-only client support, use the phone-mode only command. To remove t the configuration, use the no form of
                              		  this command.

phone-mode phone only

no phone-mode phone
                                 				  only

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

By default, this
                              		  feature is disabled.

### Command Modes

voice register global (config-register global)

voice register pool (config-register pool)

voice register template (config-register template)

## Command History

This
                                       					 command was introduced.

### Usage Guidelines

This command
                              		  enables Jabber phone-only client support.

## Examples

The following
                              		  example shows how phone-mode is enabled:

```
Router(config)# voice register pool Router(config-register pool)# phone-mode phone-only
```

### Related Commands

Command

Description

voice register global

Enters
                                          						voice register global configuration mode.

voice register pool

Enters
                                          						voice register pool configuration mode.

voice register template

Enters
                                          						voice register template configuration mode.

## phone-key-size

To specify the size of the RSA key pair that is generated on phones,
                              		  use the phone-key-size command in CAPF-server
                              		  configuration mode. To return the size to the default, use the no form of this command.

phone-key-size { 512 | 1024 | 2048 }

no phone-key-size

### Syntax Description

512

512 bits

1024

1024 bits. This is the default key size.

2048

2048 bits

### Command Default

RSA key pair size is 1024.

### Command Modes

CAPF-server configuration (config-capf-server)

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

This command is used with Cisco Unified CME phone authentication.

If you choose a higher key size than the default setting, the phones
                              		  take longer to generate the entropy that is required to generate the keys. Key
                              		  generation, which is set at low priority, allows the phone to function while
                              		  the action occurs. Depending on the phone model, you may notice that key
                              		  generation takes up to 30 or more minutes to complete.

## Examples

The following example specifies a key size of 2048 bits.

```
Router(config)# capf-server Router(config-capf-server)# source address 10.10.10.1 Router(config-capf-server)# trustpoint-label server25 Router(config-capf-server)# cert-oper upgrade all Router(config-capf-server)# cert-enroll-trustpoint server12 password 0 x8oWiet Router(config-capf-server)# auth-mode auth-string Router(config-capf-server)# auth-string generate all Router(config-capf-server)# port 3000 Router(config-capf-server)# keygen-retry 5 Router(config-capf-server)# keygen-timeout 45 Router(config-capf-server)# phone-key-size 2048
```

## phoneload

To define the phone firmware support for a phone type, use the phoneload command in ephone-type configuration mode. To remove firmware
                              		  support, use the no form of this command.

phoneload

no phoneload

### Syntax Description

This command has no arguments or keywords.

### Command Default

Phone type supports firmware configuration.

### Command Modes

Ephone-type configuration (config-ephone-type)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)XZ

Cisco Unified CME 4.3 Cisco Unified SRST 4.3

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

This command specifies whether the phone type defined in the
                              		  phone-type template supports firmware configuration using the load command.

## Examples

The following example shows that support for phone firmware is
                              		  disabled for the Nokia E61 phone type:

```
Router(config)# ephone-type E61 Router(config-ephone-type)# no phoneload
```

### Related Commands

Command

Description

device-name

Assigns a name to a phone type in an ephone-type template.

load

Associates a type of Cisco Unified IP phone with a phone
                                          						firmware file.

## phoneload-support

To define the
                              		  phone support for firmware download from CME, use the phoneload-support command in voice register
                              		  pool-type mode. To disable phoneload support, use the no form of
                              		  this command.

phoneload-support

no poneload-support

### Syntax
                              		  Description

This command has
                              		  no arguments or keywords.

### Command Default

The phoneload
                              		  support is disabled. When the reference-pooltype command is configured,
                              		  phoneload support property of the reference phone is inherited.

### Command Modes

Voice Register Pool Configuration (config-register-pool)

## Command History

15.3(3)M

Cisco SIP
                                       					 CME 10.0

This
                                       					 command was introduced.

### Usage Guidelines

Use this command
                              		  to define the default transport type. If the new phone supports the phoneload,
                              		  you can use the load command
                              		  in voice register global” mode to configure the corresponding phoneload for the
                              		  new phone model. When you use the no form of this command, the inherited
                              		  properties of the reference phone takes precedence over the default value.

## Examples

The following
                              		  example shows how to define the phoneload support for a new phone model using
                              		  the phoneload-support command:

```
Router(config)# voice register global Router(config--register-global)# mode cme Router(config-register-global)# load 9900 P0S3-06-0-00 Router(config-register-global)# phoneload-support
```

### Related Commands

Command

Description

Adds a new Cisco Unified SIP IP phone to Cisco Unified CME.

Associates a type of IP phone with a phone firmware file.

## phone-redirect-limit (voice register global)

To set the number of 3XX responses an originating SIP phone in a
                              		  Cisco CallManager Express (Cisco CME) system can accept for a single call, use
                              		  the phone-redirect-limit command in voice
                              		  register global configuration mode. To revert to the default, use the no form of this command.

phone-redirect-limit number

no phone-redirect-limit

### Syntax Description

number

Maximum number of 3XX responses accepted for a single call.
                                          						Range: 5 to 20. Default: 5.

### Command Default

Default is 5

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

Use this command to control how many subsequent 3XX responses an
                              		  originating SIP phone can handle for a single call. The terminating side is any
                              		  forwarding party which does not use B2BUA, but sends 3XX directly to the
                              		  originating calling phone. When Cisco CME gets a 3XX from the terminating side,
                              		  Cisco CME relays the 3XX to the originating SIP phone. The default number of
                              		  3XXs that the originating phone can accept is 5.

The following example shows how to set the maximum number of
                              		  redirects to 6:

```
Router(config)# voice register global Router(config-register-global)# phone-redirect-limit 6
```

### Related Commands

Description

voice register global

Enters voice register global configuration mode in order to
                                          						set global parameters for all supported Cisco SIP phones in a Cisco CME or
                                          						Cisco SIP SRST environment.

## phone-ui
                        	 park-list

To enable a phone
                              		  user to view the list of active parked calls, use the phone-ui park-list command in the ephone
                              		  configuration mode. To remove the configuration, use the no form of
                              		  this command.

phone-ui park-list

no phone-ui park-list

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

By default, this
                              		  feature is enabled for Skinny Call Control Protocol (SCCP) phones.

### Command Modes

ephone configuration (config-ephone)

## Command History

This
                                       					 command was introduced.

### Usage Guidelines

This command
                              		  enables the park-list menu option under My-Phone-Apps service button menu.

## Examples

The following
                              		  example shows how to enable the park list display option for phone 7:

```
Router(config)# ephone 7 Router(config-ephone-type)# phone-ui park-list
```

## Examples

The following
                              		  example shows how to disable park list display option for phone 7:

```
Router(config)# ephone 7 Router(config-ephone-type)# no phone-ui park-list
```

### Related Commands

Command

Description

url button

Enables
                                          						the configuration of the URL Services feature button on a line key.

url services

Associates a URL with the Programmable Services feature
                                          						button on the supported Cisco Unified SCCP phones.

## phone-ui speeddial-fastdial

To enable a phone user to configure speed-dial and fast-dial numbers
                              		  from their phone, use the phone-ui speeddial-fastdial command in ephone configuration
                              		  mode. To reset to the default value, use the no form of this command.

phone-ui speeddial-fastdial

no phone-ui speeddial-fastdial

### Syntax Description

This command has no arguments or keywords.

### Command Default

Enabled (speed-dial and fast-dial numbers are configurable from
                              		  phone).

### Command Modes

Ephone configuration (config-ephone)

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

This command enables the speed-dial and fast-dial configuration menu
                              		  on the phone so that users can configure these options directly.

The services URL must be configured using the url services command.

## Examples

The following example shows that the speed-dial and fast-dial user
                              		  interface is disabled for phone 7:

```
Router(config)# ephone 7 Router(config-ephone-type)# no phone-ui speeddial-fastdial
```

### Related Commands

Command

Description

fastdial

Creates an entry for a personal speed-dial number.

speed-dial

Creates speed-dial definitions for a phone.

url services

Associates a URL with the programmable Services feature
                                          						button on supported Cisco Unified IP phones.

## phone-ui
                        	 voice-hunt-groups

To enable a Skinny
                              		  Call Control Protocol (SCCP) phone user to display voice hunt group information
                              		  using the Services button on a phone, use the phone-ui voice-hunt-groups command in ephone configuration mode. To remove the
                              		  configuration, use the no form of
                              		  this command.

phone-ui voice-hunt-groups

no phone-ui voice-hunt-groups

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

By default, this
                              		  command is enabled.

### Command Modes

ephone configuration (config-ephone)

## Command History

This
                                       					 command was introduced.

### Usage Guidelines

This command
                              		  enables the Voice Hunt Groups menu option under the My-Phone-Apps service
                              		  button menu .

## Examples

The following
                              		  example shows how to disable the voice hunt group display option for phone 7:

```
Router(config)# ephone 7 Router(config-ephone-type)# no phone-ui voice-hunt-groups
```

### Related Commands

Command

Description

url services

Associates a URL with the Programmable Services feature button on supported
                                          						Cisco Unified IP phones.

## pickup-call any-group

To enable a phone user to pickup a ringing call on extensions in any
                              		  pickup group, use the pickup-call any-group command in ephone-dn or voice register dn configuration mode.
                              		  To reset to the default value, use the no form of this command.

pickup-call any-group

no pickup-call any-group

### Syntax Description

This command has no arguments or keywords.

### Command Default

User can pickup calls in other groups by pressing GPickUp soft key
                              		  and dialing pickup group number.

### Command Modes

Ephone-dn configuration (config-ephone-dn) Voice register dn configuration (config-register-dn)

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

This command allows a phone user to pickup any ringing call within
                              		  the local Cisco Unified CME system by pressing the GPickUp soft key and
                              		  asterisk (*), if the ringing extension is configured with a pickup group using
                              		  the pickup-group command.

If this command is not configured, a phone user can pickup calls only
                              		  from their local group by pressing the GPickUp soft key and *. To pickup calls
                              		  in another group, the user must press the GPickUp soft key and dial the pickup
                              		  group number.

## Examples

The following example shows that extension 1020 can pick up calls
                              		  ringing on extension 1030 by pressing the GPickUp softkey and *:

```
ephone-dn  102
 number 1020
 pickup-call any-group
!
ephone-dn  103
 number 1030
 pickup-group 5
```

### Related Commands

Command

Description

pickup-group

Assigns an extension to a call-pickup group.

service directed-pickup

Enables Directed Call Pickup and modifies the function of
                                          						the GPickUp and PickUp soft keys.

softkeys idle

Modifies the soft-key display on IP phones during the idle
                                          						call state.

## pickup-group

To assign an extension to a call-pickup group, use the pickup-group command in ephone-dn, ephone-dn-template, or voice register dn
                              		  configuration mode. To remove the extension from a group, use the no form of this command.

pickup-group group-number

no pickup-group

### Syntax Description

group-number

String representing a pickup group. The string can contain
                                          						up to 32 characters.

### Command Default

An extension does not belong to any pickup group.

### Command Modes

Ephone-dn configuration (config-ephone-dn) Ephone-dn-template configuration (config-ephone-dn-template) Voice register dn configuration (config-register-dn)

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

This command was added to ephone-dn-template configuration
                                          						mode.

## Command History

12.4(9)T

Cisco Unified CME 4.0

This command in ephone-dn-template configuration mode was
                                          						integrated into Cisco IOS Release 12.4(9)T.

12.4(22)YB

Cisco Unified CME 7.1

This command was added to voice register dn configuration
                                          						mode for SIP directory numbers.

12.4(24)T

Cisco Unified CME 7.1

This command was integrated into Cisco IOS Release
                                          						12.4(24)T.

### Usage Guidelines

This command allows you to assign an individual directory number to a
                              		  call-pickup group. Phone users can pick up ringing calls within their own
                              		  pickup group more easily than calls outside their group.

You can assign each directory number to only one pickup group. There
                              		  is no limit to the number of directory numbers that can be assigned to a single
                              		  pickup group, and there is no limit to the number of pickup groups that can be
                              		  defined in a Cisco Unified CME system.

Pickup group numbers can vary in length, but must have unique leading
                              		  digits. For example, you cannot define pickup group 17 and pickup group 177 in
                              		  the same Cisco Unified CME system because a pickup in group 17 will always be
                              		  triggered before the user can enter the final 7 for group 177. You can,
                              		  however, define pickup groups 27 and 177 in the same Cisco Unified CME system.

If you use an ephone-dn template to apply a command to an ephone-dn
                              		  and you also use the same command in ephone-dn configuration mode for the same
                              		  ephone-dn, the value that you set in ephone-dn configuration mode has priority.

## Examples

The following examples assign extension 3242 to pickup group 25:

```
Router(config)# ephone-dn 4 Router(config-ephone-dn)# number 3242 Router(config-ephone-dn)# pickup-group 25 Router(config)# voice register dn 4 Router(config-register-dn)# number 3242 Router(config-register-dn)# pickup-group 25
```

The following example uses an ephone-dn-template to assign extension
                              		  3242 to pickup group 25:

```
Router(config)# ephone-dn-template 8 Router(config-ephone-dn-template)# pickup-group 25 Router(config-ephone-dn-template)# exit Router(config)# ephone-dn 4 Router(config-ephone-dn)# number 3242 Router(config-ephone-dn)# ephone-dn-template 8
```

### Related Commands

Command

Description

ephone-dn-template (ephone-dn)

Applies a template to an ephone-dn configuration.

service directed-pickup

Enables Directed Call Pickup and modifies the function of
                                          						the PickUp and GPickUp soft keys.

## pilot

To define the ephone-dn that callers dial to reach a Cisco
                              		  CallManager Express (Cisco CME) ephone hunt group, use the pilot command in ephone-hunt configuration
                              		  mode. To remove the pilot number from the ephone hunt group, use the no form of this command.

pilot number [ secondary number ]

no pilot number [ secondary number ]

### Syntax Description

number

String of up to 27 characters that represents an E.164
                                          						telephone number. Normally the string is composed of digits, but the string may
                                          						contain alphabetic characters if the number is dialed only by the router, as
                                          						with an intercom number, or is not intended to be dialed at all. Secondary
                                          						numbers can contain wildcards in the string. For details, see “Usage
                                          						Guidelines.”

secondary

(Optional) Defines the number that follows as an additional
                                          						pilot number for the ephone hunt group.

### Command Default

No pilot number is defined.

### Command Modes

Ephone-hunt configuration (config-ephone-hunt)

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

12.3(7)T

Cisco CME 3.1

The secondary secondary- number keyword-argument pair was introduced.

### Usage Guidelines

This command defines a valid number for an ephone-dn (extension) that
                              		  is to be assigned to an ephone hunt pilot group. The dial-plan pattern can be
                              		  applied to the pilot number.

The secondary keyword allows you to associate a
                              		  second telephone number with this ephone-dn so that the hunt group can be
                              		  called by dialing either the main or secondary phone number. The secondary
                              		  number may contain one or more wildcards instead of digits, even if the
                              		  wildcard number overlaps the primary number. For example, 50.. (the number 50
                              		  followed by periods, which stand for wildcards) matches all four-digit
                              		  extensions that start with 50. Wildcard characters cannot be used in the
                              		  primary pilot number.

Alphabetic characters can be used to create a primary or secondary
                              		  pilot number that cannot be dialed from a phone and is not part of the dial
                              		  plan.

## Examples

The following example sets the pilot number to 2345 for peer ephone
                              		  hunt group number 5:

```
ephone-hunt 5 peer
 pilot 2345
 list 2346, 2347, 2348
 hops 3
 timeout 45
 final 6000
```

The following example sets the pilot number for ephone hunt group 3
                              		  to 2222 and the secondary pilot number to 4444:

```
ephone-hunt 3 sequential
 pilot 2222 secondary 4444
 list 2555, 2556, 2557
 final 6000
```

The following example uses wildcards in the secondary pilot number to
                              		  create a hunt group that receives the calls made to all numbers that start with
                              		  555. The primary pilot number, A0, cannot be dialed.

```
ephone-hunt 1 longest-idle
 pilot A0 secondary 555....
 list 1000, 1001, 1002
 timeout 5
 hops 3
 final 1100
```

### Related Commands

Description

ephone-hunt

Enters ephone-hunt configuration mode to define a Cisco CME
                                          						ephone hunt group.

final

Defines the last ephone-dn in an ephone hunt group.

hops

Defines the number of times that a call is redirected to
                                          						the next ephone-dn in a peer ephone-hunt-group list before proceeding to the
                                          						final ephone-dn.

list

Lists the ephone-dns that participate in an ephone hunt
                                          						group.

max-redirect

Changes the current number of allowable redirects in a
                                          						Cisco CME system.

no-reg (ephone-hunt)

Specifies that the pilot number of an ephone hunt group
                                          						should not register with the H.323 gatekeeper.

preference (ephone-hunt)

Sets preference order for the ephone-dn associated with an
                                          						ephone-hunt-group pilot number.

timeout (ephone-hunt)

Sets the number of seconds after which a call that is not
                                          						answered is redirected to the next number in the ephone-hunt-group list.

## pilot (voice hunt-group)

To define the number that callers dial to reach a Cisco Unified CME
                              		  voice hunt group, use the pilot command in voice hunt-group
                              		  configuration mode. To remove the pilot number from the voice hunt group, use
                              		  the no form of this command.

pilot number [ secondary number ]

no pilot

### Syntax Description

number

String of up to 32 characters that represents an extension
                                          						or E.164 telephone number.

secondary

(Optional) Defines an additional pilot number for the voice
                                          						hunt group.

### Command Default

No pilot number is defined.

### Command Modes

Voice hunt-group configuration (config-voice-hunt-group)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4

This command was introduced.

### Usage Guidelines

This command defines an extension that is assigned as the pilot
                              		  number of a voice hunt group. The dial-plan pattern can be applied to the pilot
                              		  number.

Normally the pilot number is composed of digits, but the string may
                              		  contain alphabetic characters if the number is dialed only by the router, as
                              		  with an intercom number, or is not intended to be dialed at all.

The secondary keyword allows you to associate a second
                              		  telephone number so that the hunt group can be called by dialing either the
                              		  primary or secondary phone number. The secondary number can contain one or more
                              		  wild cards instead of digits, even if the wildcard number overlaps the primary
                              		  number. For example, 50.. (the number 50 followed by periods, which stand for
                              		  wild card) matches all four-digit extensions that start with 50. Wildcard
                              		  characters cannot be used in the primary pilot number.

Alphabetic characters can be used to create a primary or secondary
                              		  pilot number that cannot be dialed from a phone and is not part of the dial
                              		  plan.

Voice hunt groups do not support the expansion of pilot numbers using
                              		  the dialplan-pattern command. To enable external
                              		  phones to dial the pilot number, you must configure a secondary pilot number
                              		  using a fully qualified E.164 number.

## Examples

The following example shows how to set the pilot number to 2345 for
                              		  voice hunt group hunt group number 5:

```
voice-hunt 5 peer
 pilot 2345
 list 2346, 2347, 2348
 hops 3
 timeout 45
 final 6000
```

The following example shows how to set the pilot number for voice
                              		  hunt group 3 to 2222 and the secondary pilot number to 4444:

```
voice hunt-group 3 sequential
 pilot 2222 secondary 4444
 final 6000
```

The following example shows how to use wild cards in the secondary
                              		  pilot number to create a voice hunt group that receives the calls made to all
                              		  numbers that start with 55501. The primary pilot number, A0, cannot be dialed.

```
voice hunt-group 1 longest-idle
 pilot A0 secondary 55501..
 list 1000, 1001, 1002
 timeout 5
 hops 3
 final 1100
```

The following example shows how to use a secondary pilot number in a
                              		  parallel hunt group. Local phones can dial the primary pilot number, 1100.
                              		  External phones (PSTN) must dial the full E.164 number, 4085550100.

```
voice hunt-group 4 parallel
 final 1109
 list 1101,1102,1103,1104
 timeout 60
 pilot 1100 4085550100
```

### Related Commands

Description

dialplan-pattern

Defines a pattern that is used to expand extension numbers
                                          						into fully qualified E.164 numbers.

final (voice hunt-group)

Defines the last extension in a voice hunt group.

hops (voice hunt-group)

Defines the number of times that a call is redirected to
                                          						the next directory number in a peer voice hunt-group list before proceeding to
                                          						the final directory number.

list (voice hunt-group)

Defines the directory numbers that participate in a hunt
                                          						group.

voice hunt-group

Defines the type of hunt group.

## pin

To set a personal identification number (PIN) for an IP phone in a
                              		  Cisco CallManager Express (Cisco CME) system, use the pin command in ephone configuration mode. To
                              		  remove a PIN, use the no form of this command.

pin number

no pin

### Syntax Description

number

PIN that will be used to log in to a Cisco IP phone. This
                                          						is a numeric string from four to eight digits in length.

### Command Default

No PIN is set.

### Command Modes

Ephone configuration (config-ephone)

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

The pin command allows individual phone users to
                              		  override call-blocking patterns that are associated with defined time periods.
                              		  Call-blocking patterns that are in effect at all times (7 days a week, 24 hours
                              		  a day) cannot be overridden using a PIN.

Call blocking on IP phones is defined in the following way. First,
                              		  one or more patterns of outgoing digits to be blocked are defined using the after-hours block pattern command. Next, one or more time periods
                              		  during which calls to those patterns are to be blocked are defined using the after-hours date or after-hours day command or both. By default, all IP phones in
                              		  a Cisco CME system are restricted if at least one pattern and at least one time
                              		  period are defined. Individual phones can be completely exempted from call
                              		  blocking using the after-hour exempt command . An individual with a PIN can
                              		  override call blocking by entering the PIN after pressing the Login soft key to
                              		  log in to a phone that has been configured for that PIN using the pin command.

The PIN functionality applies only to IP phones that have soft keys,
                              		  such as the Cisco IP Phones 7940 and 7940G and the Cisco IP Phones 7960 and
                              		  7960G.

## Examples

The following example sets a PIN for an IP phone:

```
Router(config)# ephone 1 Router(config-ephone)# pin 1000
```

### Related Commands

Description

after-hour exempt

Specifies that an IP phone does not have any of its
                                          						outgoing calls blocked even though call blocking has been defined for a Cisco
                                          						CME system.

after-hours block pattern

Defines a pattern of digits to be blocked for outgoing
                                          						calls from IP phones.

after-hours date

Defines a recurring period based on month and day during
                                          						which outgoing calls that match defined call-block patterns are blocked on IP
                                          						phones.

after-hours day

Defines a recurring period based on day of the week during
                                          						which outgoing calls that match defined call-block patterns are blocked on IP
                                          						phones.

login

Defines when IP phones in a Cisco CME system are logged out
                                          						automatically.

show ephone login

Displays the login states of all phones.

## pin (voice logout-profile and voice user-profile)

To configure a personal identification number (PIN) for accessing a
                              		  particular IP phone that is enabled for extension mobility, use the pin command in voice logout-profile
                              		  configuration mode or voice user-profile configuration mode. To remove a PIN,
                              		  use the no form of this command.

pin [0|6] number

no pin [0|6] number

### Syntax Description

number

Four- to eight-digit numeric string for accessing Cisco
                                          						Unified IP phone.

[0|6]

The 0 in the parameter [0|6] mentioned in the CLI command represents plain, unencrypted text and 6 represents level 6 password
                                          encryption.

### Command Default

No PIN is configured.

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

Cisco Unified CME 4.2(‘1)

This command was introduced.

12.4(15)XZ

Cisco Unified CME 4.3

This command was introduced.

Cisco IOS XE Gibraltar 16.11.1a  Release

Unified CME 12.6

The command was enhanced for password encryption.

### Usage Guidelines

Use this command in voice logout-profile configuration mode to create
                              		  a PIN to be used by a phone user to disable the call blocking configuration for
                              		  a Cisco Unified IP phone on which a logout profile is downloaded.

Use this command in voice user-profile configuration mode to create a
                              		  PIN to be used by a phone user to disable the call blocking configuration for a
                              		  Cisco Unified IP phone on which a user profile is downloaded.

PIN functionality applies only to IP phones that have soft keys, such
                              		  as the Cisco Unified IP Phone 7940 and 7940G.

From Unified CME 12.6 onwards, you must configure password encryption using the parameters [0|6] for this command. The 0 in the parameter [0|6] mentioned in the CLI command represents plain, unencrypted text and 6 represents
                              level 6 password encryption.

## Examples

The following example shows the configuration for a user profile to
                              		  be downloaded when a phone user logs into a Cisco Unified IP phone that is
                              		  enabled for extension mobility, including a PIN of 12345:

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

Enable an SCCP phone for Extension Mobility and apply
                                          						logout profile to phone being configured.

reset (voice logout-profile and voice user-profile)

Performs complete reboot of all IP phones on which a
                                          						particular logout-profile or user-profile is downloaded.

## pin (voice register pool)

To set a personal identification number (PIN) to bypass the
                              		  after-hour call block on a Cisco Unified SIP IP phone, use the pin command in voice register pool
                              		  configuration mode. To remove the PIN, use the no form of the command.

pin [0|6] digits

no pin

### Syntax Description

digits

PIN to bypass the after-hour call block on the Cisco
                                          						Unified SIP IP phone. Numeric string from four to eight digits in length.

The 0 in the parameter [0|6] mentioned in the CLI command represents plain, unencrypted text and 6 represents level 6 password
                                          encryption.

### Command Default

No valid PIN is set.

### Command Modes

Voice register pool configuration (config-register-pool)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.2(2)T

This command was introduced.

Cisco IOS XE Gibraltar 16.11.1a  Release

Unified CME 12.6

The command was enhanced for password encryption.

### Usage Guidelines

The pin command allows individual Cisco Unified
                              		  SIP IP phone users to override call-blocking patterns that are associated with
                              		  defined time periods. Call-blocking patterns that are in effect at all times (7
                              		  days a week, 24 hours a day) cannot be overridden using a PIN.

From Unified CME 12.6 onwards, you must configure password encryption using the parameters [0|6] for this command. The 0 in the parameter [0|6] mentioned in the CLI command represents plain, unencrypted text and 6 represents
                              level 6 password encryption.

## Examples

The following example shows how to set a PIN to bypass the after-hour
                              		  call block on a Cisco Unified SIP IP phone in voice register pool 80:

```
Router(config)# voice register pool 80 Router(config-register-pool)# pin 12345
```

### Related Commands

Command

Description

voice register pool

Enters voice register pool configuration mode and creates a
                                          						pool configuration for Cisco Unified SIP IP phones in Cisco Unified CME.

## port (CAPF-server)

To define the TCP port number on which the CAPF server listens for
                              		  incoming socket connections, use the port command in CAPF-server configuration
                              		  mode. To use the default, use the no form of this command.

port tcp-port

no port

### Syntax Description

tcp-port

Port for secure communication. Range is from 2000 to 9999.
                                          						Default is 3804.

### Command Default

TCP port number 3804.

### Command Modes

CAPF-server configuration (config-capf-server)

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

This command is used with Cisco Unified CME phone authentication.

## Examples

The following example specifies TCP port 3000 instead of the default
                              		  port 3804:

```
Router(config)# capf-server Router(config-capf-server)# source address 10.10.10.1 Router(config-capf-server)# trustpoint-label server25 Router(config-capf-server)# cert-oper upgrade all Router(config-capf-server)# cert-enroll-trustpoint server12 password 0 x8oWiet Router(config-capf-server)# auth-mode auth-string Router(config-capf-server)# auth-string generate all Router(config-capf-server)# port 3000 Router(config-capf-server)# keygen-retry 5 Router(config-capf-server)# keygen-timeout 45 Router(config-capf-server)# phone-key-size 2048
```

## preemption reserve timer

To set the amount of time to reserve a channel for a preemption call,
                              		  use the preemption reserve timer command in voice MLPP configuration mode. To
                              		  reset to the default, use the no form of this command.

preemption reserve timer seconds

no preemption reserve timer

### Syntax Description

seconds

Number of seconds to reserve the channel. Range: 3 to 30.
                                          						Default: 0.

### Command Default

Preemption reserve timer is disabled (0).

### Command Modes

Voice MLPP configuration (config-voice-mlpp)

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

When a channel on a SCCP phone is preempted by a higher priority MLPP
                              		  call, the channel is reserved for the MLPP call so that other calls cannot use
                              		  that channel before the call is connected.

## Examples

The following example shows the reserve timer set to 10 seconds.

```
Router(config)# voice mlpp Router(config-voice-mlpp)# preemption reserve timer 10
```

### Related Commands

Command

Description

preemption enable

Enables preemption capabilities on a trunk group.

preemption tone timer

Sets the expiry time for the preemption tone for the
                                          						outgoing call being preempted by a DDR backup call.

preemption user

Enables phones to preempt calls.

## preemption tone timer (voice MLPP)

To set the amount of time the preemption tone plays on the called
                              		  phone when a lower precedence call is being preempted, use the preemption tone timer command in voice MLPP configuration mode. To
                              		  reset to the default, use the no form of this command.

preemption tone timer seconds

no preemption tone timer

### Syntax Description

seconds

Length of preemption tone, in seconds. Range: 3 to 30.
                                          						Default: 0.

### Command Default

Preemption tone timer is disabled (0).

### Command Modes

Voice MLPP configuration (config-voice-mlpp)

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

This command sets how long a phone user hears the preemption tone
                              		  play when a lower precedence call is being preempted by a higher priority call.
                              		  The preemption tone stops playing when the timer expires or the user goes
                              		  onhook.

For calls to Cisco Unified IP phones, the called party can hang up
                              		  immediately to connect to the new higher precedence call, or if the called
                              		  party does not hang up, Cisco Unified CME forces the phone on-hook after the
                              		  preemption tone timer expires and connects the call.

For FXS ports, the called party must acknowledge the preemption by
                              		  going on-hook, before being connected to the new higher precedence call.

The mlpp indication command must be enabled (default) for a
                              		  phone to play preemption tones.

## Examples

The following example shows the tone timer is set to 15 seconds:

```
Router(config)# voice mlpp Router(config-voice-mlpp)# preemption tone timer 15
```

### Related Commands

Command

Description

mlpp indication

Enables MLPP indication on an SCCP phone or analog FXS
                                          						port.

mlpp preeemption

Enables the preemption capability on an SCCP phone or
                                          						analog FXS port.

preemption reserve timer

Sets the amount time to reserve a channel for a preemption
                                          						call.

preemption user

Enables the preemption capability for all supported phones.

## preemption trunkgroup

To enable preemption capabilities for trunk groups, use the preemption trunkgroup command in voice MLPP configuration
                              		  mode. To disable preemption capabilities, use the no form of this command.

preemption trunkgroup

no preemption trunkgroup

### Syntax Description

This command has no arguments or keywords.

### Command Default

Preemption is disabled for trunk groups.

### Command Modes

Voice MLPP configuration (config-voice-mlpp)

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

The following example enables preemption capabilities for trunk
                              		  groups:

```
Router(config)# voice mlpp Router(config-voice-mlpp)# preemption trunkgroup
```

### Related Commands

Command

Description

mlpp preemption

Enables calls on an SCCP phone or analog FXS port to be
                                          						preempted.

preemption user

Enables phones to preempt calls.

## preemption user

To enable phones to preempt calls, use the preemption user command in voice MLPP configuration mode. To
                              		  disable preemption capabilities, use the no form of this command.

preemption user

no preemption user

### Syntax Description

This command has no arguments or keywords.

### Command Default

Preemption is disabled for phones.

### Command Modes

Voice MLPP configuration (config-voice-mlpp)

## Command History

Cisco IOS Release

Cisco Products

Modification

12.4(22)YB

Cisco Unified CME 7.1

This command was introduced.

12.4(24)T

Cisco Unified CME 7.1

This command was integrated into Cisco IOS Release
                                          						12.4(24)T.

This command enables SCCP and analog FXS phones in the system to
                              		  preempt calls if the called party is busy with lower precedence calls.

## Examples

The following example enables preemption capabilities for phones:

```
Router(config)# voice mlpp Router(conf-voi-mlpp)# preemption user
```

### Related Commands

Command

Description

mlpp preemption

Enables preemption capabilities on an SCCP phone or analog
                                          						FXS port.

preemption trunkgroup

Enables preemption capabilities on a trunk group.

## preference (ephone-dn)

To set dial-peer preference order for an extension (ephone-dn)
                              		  associated with a Cisco IP phone, use the preference command in ephone-dn configuration
                              		  mode. To reset the preference order to the default, use the no form of this command.

preference preference-order [ secondary secondary-order ]

no preference

### Syntax Description

preference-order

Preference order for the primary number associated with an
                                          						extension (ephone-dn). Type ? for a range, where 0 is the
                                          						highest preference. Default is 0.

secondary secondary-order

(Optional) Preference order for the secondary number
                                          						associated with the ephone-dn. Type ? for a range, where 0 is the
                                          						highest preference. Default is 9.

### Command Default

Preference order for the primary number is 0 (highest preference).
                              		  Preference order for the secondary number is 9 (lowest preference).

### Command Modes

Ephone-dn configuration (config-ephone)

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

The secondary secondary-order keyword-argument
                                          						pair was introduced.

12.3(4)T

Cisco CME 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

When you create an ephone-dn for an IP phone in a Cisco CallManager
                              		  Express (Cisco CME) system, you automatically create a virtual voice port and
                              		  one to four virtual dial peers to be used by that ephone-dn. This command sets
                              		  a preference value for the primary and secondary numbers that are associated
                              		  with the ephone-dn that you are creating. The preference values are passed
                              		  transparently into the dial peer or dial peers created by the ephone-dn. The
                              		  preference values allow you to control the selection of a desired dial peer
                              		  when multiple dial peers are matched on the same destination-pattern (target)
                              		  number value. In this way, the preference command can be used to establish a
                              		  hunt strategy for incoming calls.

The huntstop command can be used to prevent
                              		  further hunting for a dial-peer match when an ephone-dn is busy or does not
                              		  answer.

## Examples

The following example sets a preference of 2 for the directory number
                              		  3000:

```
ephone-dn 1
 number 3000
 preference 2
```

In the following example, the number 1222 under ephone-dn 4 has a
                              		  higher preference than the number 1222 under ephone-dn 5.

```
ephone-dn 4
 number 1222
 preference 0
!
!
ephone-dn 5
 number 1222
 preference 1
```

The following example shows an ephone-dn with two numbers. The
                              		  primary number has a higher preference than the secondary number.

```
ephone-dn 6
 number 2233 secondary 2234
 preference 0 secondary 1
```

### Related Commands

Command

Description

ephone-dn

Enters ephone-dn configuration mode.

huntstop

Discontinues call hunting behavior for an extension
                                          						(ephone-dn) or an extension channel.

## preference (ephone-hunt)

To set preference order for the ephone-dn associated with an
                              		  ephone-hunt-group pilot number in Cisco Unified CME, use the preference command in ephone-hunt
                              		  configuration mode. To delete this preference order, use the no form of this command.

preference preference-order [ secondary secondary-order ]

no preference preference-order [ secondary secondary-order ]

### Syntax Description

preference-order

Preference order. Range is 0 to 8, where 0 is the highest
                                          						preference and 8 is the lowest preference. Default is 0.

secondary secondary-order

(Optional) Preference order for the secondary pilot number.
                                          						Range is 1 to 8, where 1 is the highest preference and 8 is the lowest
                                          						preference. Default is 7.

### Command Default

Preference order for the primary number is 0 (highest preference).
                              		  Preference order for the secondary number is 7 (lowest preference).

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

The secondary secondary-order keyword-argument
                                          						pair was introduced.

### Usage Guidelines

This command sets a preference value that is used for matching dial
                              		  peers in a Cisco IP phone virtual dial-peer group. The preference value is
                              		  associated with a pilot number for a Cisco CME ephone hunt group. The
                              		  preference value is passed transparently into the dial peer created by the
                              		  pilot number. Setting the preference enables the desired dial peer to be
                              		  selected when multiple dial peers within a hunt group are matched for a dial
                              		  string.

## Examples

The following example sets the preference for the pilot number of
                              		  hunt group 23 to 1:

```
Router(config)# ephone-hunt 23 sequential Router(config-ephone-hunt)# pilot 2355 Router(config-ephone-hunt)# preference 1
```

### Related Commands

Command

Description

final

Defines the last ephone-dn in an ephone hunt group.

hops

Defines the number of times that a call is redirected to
                                          						the next ephone-dn in a peer ephone-hunt-group list before proceeding to the
                                          						final ephone-dn.

list

Lists the ephone-dns that participate in an ephone hunt
                                          						group.

max-redirect

Changes the current number of allowable redirects in an
                                          						Cisco CME system.

no-reg (ephone-hunt)

Specifies that the pilot number of an ephone hunt group not
                                          						register with the H.323 gatekeeper.

pilot

Defines the ephone-dn that callers dial to reach an ephone
                                          						hunt group.

timeout (ephone-hunt)

Sets the number of seconds after which a call that is not
                                          						answered is redirected to the next number in the ephone-hunt-group list.

## preference (voice hunt-group)

To set preference order for the voice dial peer associated with a
                              		  voice hunt-group pilot number in Cisco Unified CME, use the preference command in voice hunt-group
                              		  configuration mode. To delete this preference order, use the no form of this command.

preference preference-order [ secondary secondary-order ]

no preference preference-order [ secondary secondary-order ]

### Syntax Description

preference-order

Preference order for the extension or telephone number
                                          						associated with a dial peer. Range is 0 to 8. Default is 0.

secondary secondary-order

(Optional) Preference order for the secondary pilot number.
                                          						Range is 1 to 8, where 1 is the highest preference and 8 is the lowest
                                          						preference. Default is 7.

### Command Default

Preference for primary number is 0 (highest preference). Preference
                              		  for secondary number is 7 (lower preference).

### Command Modes

Voice hunt-group configuration (config-voice-hunt-group)

## Command History

Cisco IOS Release

Version

Modification

12.4(4)T

Cisco CME 3.4

This command was introduced.

### Usage Guidelines

This command sets a preference value that is used for matching dial
                              		  peers in a Cisco IP phone virtual dial-peer group. The preference value is
                              		  associated with a pilot number for a Cisco CME voice hunt group. The preference
                              		  value is passed transparently into the dial peer created by the pilot number.
                              		  Setting the preference enables the desired dial peer to be selected when
                              		  multiple dial peers within a hunt group are matched for a dial string.

## Examples

The following is an example of a parallel voice hunt group. The pilot
                              		  number is 6000 and the preference assigned to the pilot number is 1:

```
voice hunt-group 2 parallel
 pilot 6000
 preference 1
 list 3000, 3010, 3020
 final 9999
 timeout 10
```

### Related Commands

Command

Description

pilot (voice hunt-group)

Defines the voice dn that callers dial to reach a Cisco
                                          						CallManager Express (Cisco CME) voice hunt group.

voice hunt-group

Defines the type of hunt group.

## preference (voice register dn)

To set the dial-peer preference order for VoIP dial peer to be
                              		  created for a directory number on a SIP phone, use the preference command in voice register dn
                              		  configuration mode. To reset the preference order to the default, use the no form of this command.

preference preference-order

no preference

### Syntax Description

preference-order

Preference order for the extension or telephone number
                                          						associated with a directory number. Range is 0 to 10. Default is 0.

### Command Default

Preference for primary number is 0 (highest preference).

### Command Modes

Voice register dn configuration (config-register-dn)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4 and Cisco SIP SRST 3.4

This command was introduced.

### Usage Guidelines

When you create a directory number for a SIP phone in a Cisco
                              		  CallManager Express (Cisco CME) or Cisco SIP SRST environment, you
                              		  automatically create a virtual voice port and one to four virtual dial peers to
                              		  be used by that directory number. This command sets a preference value for the
                              		  extension or telephone number that is associated with the directory number hat
                              		  you are creating. The preference value is passed transparently to dial peers
                              		  created by the directory number. The preference value allows you to control the
                              		  selection of a desired dial peer when multiple dial peers are matched on the
                              		  same destination pattern (extension or telephone number). In this way, the preference command can be used to establish a
                              		  hunt strategy for incoming calls.

The huntstop command can be used to prevent
                              		  further hunting for a dial-peer match when a number is busy or does not answer.

## Examples

The following example shows how to set a preference of 2 for
                              		  extension number 3000:

```
voice register dn 1
 number 3000
 preference 2
```

In the following example, extension number 1222 under voice register
                              		  dn 4 has a higher preference than number 1222 under voice register dn 5.

```
voice register dn 4
 number 1222
 preference 0
!
!
voice register dn 5
 number 1222
 preference 1
```

### Related Commands

Description

huntstop (voice register dn)

Discontinues call hunting behavior for an extension
                                          						(directory number) or an extension channel.

voice register dn

Enters voice register dn configuration mode to define an
                                          						extension for a SIP phone line.

## preference (voice register pool)

To set the preference order for creating the VoIP dial peers created
                              		  for a number associated with a voice pool, use the preference command in voice register pool
                              		  configuration mode. To put the number in default preference order, use the no form of this command.

preference preference-order

no preference

### Syntax Description

preference-order

Preference order for the extension or telephone number
                                          						associated with a pool. Range is 0 to 10. Default is 0, which is the highest
                                          						preference.

### Command Default

Preference for primary number is 0 (highest preference order).

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

This command was added to Cisco CallManager Express (Cisco
                                          						CME).

### Usage Guidelines

When you create a voice register pool for a SIP phone or a group of
                              		  SIP phones in a Cisco Unified CME or Cisco Unified Session Initiation Protocol
                              		  (SIP) Survivable Remote Site Telephony (SRST) environment, you automatically
                              		  create a virtual voice port and one to four virtual dial peers to be used by
                              		  the number associated with that pool. The preference value is passed
                              		  transparently to dial peers created for the number. The preference value allows
                              		  you to control the selection of a desired dial peer when multiple dial peers
                              		  are matched on the same destination pattern (extension or phone number)
                              		  associated with the pool. In this way, the preference command can be used to establish a
                              		  hunt strategy for incoming calls.

## Examples

The following example shows how to set a preference of 2 for
                              		  extension number 3000:

```
voice register pool 1
 number 3000
 preference 2
```

In the following example, extension number 1222 under voice register
                              		  dn 4 has a higher preference than number 1222 under voice register pool 5.

```
voice register pool 4
 number 1222
 preference 0
!
!
voice register dn 5
 number 1222
 preference 1
```

### Related Commands

Description

id (voice register pool)

Explicitly identifies a locally available individual Cisco
                                          						SIP IP phone, or when running Cisco Unified SIP SRST, set of Cisco SIP IP
                                          						phones.

voice register pool

Enters voice register pool configuration mode for SIP
                                          						phones.

## presence

To enable presence service and enter presence configuration mode, use
                              		  the presence command in global configuration
                              		  mode. To disable presence service, use the no form of this command.

presence

no presence

### Syntax Description

This command has no arguments or keywords.

### Command Default

Presence service is disabled.

### Command Modes

Global configuration (config)

## Command History

Release

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

This command enables the router to perform the following presence
                              		  functions:

- Process presence requests from internal lines to internal lines.
                                 			 Notify internal subscribers of any status change.

- Process incoming presence requests from a SIP trunk for internal
                                 			 lines. Notify external subscribers of any status change.

- Send presence requests to external presentities on behalf of
                                 			 internal lines. Relay status responses to internal lines.

## Examples

The following example shows how to enable presence and enter presence
                              		  configuration mode to set the maximum subscriptions to 150:

```
Router(config)# presence Router(config-presence)# max-subscription 150
```

### Related Commands

Description

allow watch

Allows a directory number on a phone registered to Cisco
                                          						Unified CME to be watched in a presence service.

debug presence

Displays debugging information about the presence service.

max-subscription

Sets the maximum number of concurrent watch sessions that
                                          						are allowed.

presence enable

Allows the router to accept incoming presence requests.

server

Specifies the IP address of a presence server for sending
                                          						presence requests from internal watchers to external presence entities.

show presence global

Displays configuration information about the presence
                                          						service.

show presence subscription

Displays information about active presence subscriptions.

## presence call-list

To enable Busy Lamp Field (BLF) monitoring for call lists and
                              		  directories on phones registered to the Cisco Unified CME router, use the presence call-list command in ephone, presence, or voice
                              		  register pool configuration mode. To disable BLF indicators for call lists, use
                              		  the no form of this command.

presence call-list

no presence call-list

### Syntax Description

This command has no arguments or keywords.

### Command Default

BLF monitoring for call lists is disabled.

### Command Modes

Ephone configuration (config-ephone) Presence configuration (config-presence) Voice register pool configuration (config-register pool)

## Command History

Release

Modification

12.4(11)XJ

This command was introduced.

12.4(15)T

This command was integrated into Cisco IOS Release
                                          						12.4(15)T.

### Usage Guidelines

This command enables a phone to monitor the line status of directory
                              		  numbers listed in a directory or call list, such as a missed calls, placed
                              		  calls, or received calls list. Using this command in presence mode enables the
                              		  BLF call-list feature for all phones. To enable the feature for an individual
                              		  SCCP phone, use this command in ephone configuration mode. To enable the
                              		  feature for an individual SIP phone, use this command in voice register pool
                              		  configuration mode.

If this command is disabled globally and enabled in voice register
                              		  pool or ephone configuration mode, the feature is enabled for that voice
                              		  register pool or ephone.

If this command is enabled globally, the feature is enabled for all
                              		  voice register pools and ephones regardless of whether it is enabled or
                              		  disabled on a specific voice register pool or ephone.

To display a BLF status indicator, the directory number associated
                              		  with a telephone number or extension must have presence enabled with the allow watch command.

For information on the BLF status indicators that display on specific
                              		  types of phones, see the Cisco
                                 			 Unified IP Phone documentation for your phone model.

## Examples

The following example shows the BLF call-list feature enabled for
                              		  ephone 1. The line status of a directory number that appears in a call list or
                              		  directory is displayed on phone 1 if the directory number has presence enabled.

```
Router(config)# ephone 1 Router(config-ephone)# presence call-list
```

### Related Commands

Description

allow watch

Allows a directory number on a phone registered to Cisco
                                          						Unified CME to be watched in a presence service.

blf-speed-dial

Enables BLF monitoring for a speed-dial number on a phone
                                          						registered to Cisco Unified CME.

presence

Enables presence service and enters presence configuration
                                          						mode.

show presence global

Displays configuration information about the presence
                                          						service.

## presence enable

To allow incoming presence requests, use the presence enable command in SIP user-agent configuration
                              		  mode. To block incoming requests, use the no form of this command.

presence enable

no presence enable

### Syntax Description

This command has no arguments or keywords.

### Command Default

Incoming presence requests are blocked.

### Command Modes

SIP UA configuration (config-sip-ua)

## Command History

Release

Modification

12.4(11)XJ

This command was introduced.

12.4(15)T

This command was integrated into Cisco IOS Release
                                          						12.4(15)T.

### Usage Guidelines

This command allows the router to accept incoming presence requests
                              		  (SUBSCRIBE messages) from internal watchers and SIP trunks. It does not impact
                              		  outgoing presence requests.

## Examples

The following example shows how to allow incoming presence requests:

```
Router(config)# sip-ua Router(config-sip-ua)# presence enable
```

### Related Commands

Description

allow subscribe

Allows internal watchers to monitor external presence
                                          						entities (directory numbers).

allow watch

Allows a directory number on a phone registered to Cisco
                                          						Unified CME to be watched in a presence service.

max-subscription

Sets the maximum number of concurrent watch sessions that
                                          						are allowed.

show presence global

Displays configuration information about the presence
                                          						service.

show presence subscription

Displays information about active presence subscriptions.

watcher all

Allows external watchers to monitor internal presence
                                          						entities (directory numbers).

## present-call

To present ephone-hunt-group calls only to member phones that are
                              		  idle or onhook, use the present-call command in ephone-hunt
                              		  configuration mode. To return to the default, use the no form of this command.

present-call { idle-phone | onhook-phone }

no present-call { idle-phone | onhook-phone }

### Syntax Description

idle-phone

Presents calls from the ephone-hunt group only if all lines
                                          						are idle on the phone on which the hunt-group line appears. This option does
                                          						not consider monitored lines that have been configured on the phone using the button m command.

onhook-phone

Presents calls from the ephone-hunt group only if the phone
                                          						on which the number appears is in the onhook state. When this keyword is
                                          						configured, calls in the ringing or hold state that are unrelated to the hunt
                                          						group do not prevent the presentation of calls from the ephone-hunt group.

### Command Default

Ephone hunt group calls are presented to lines (ephone-dns) that are
                              		  not in use, regardless of the state of other lines on the same ephone.

### Command Modes

Ephone-hunt configuration (config-ephone-hunt)

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

If you do not use this command, an ephone hunt group presents calls
                              		  to an ephone whenever the phone line (ephone-dn) that corresponds to a number
                              		  in an ephone-hunt list is available. The status of other phone lines on the
                              		  phone is not considered.

The present-call command adds additional controls that allow you to take into
                              		  account the activity on all lines of a phone that has an ephone-dn that is
                              		  assigned to an ephone hunt group. The present-call command allows you to specify
                              		  that hunt groups should present calls to these phones only when they are on
                              		  hook or are not busy with an active call. This keeps hunt group calls from
                              		  possibly going unanswered because a phone is occupied with a call on a line
                              		  other than the line assigned to the hunt group.

## Examples

The following example sets up a peer hunt group with three ephone-dns
                              		  to answer calls. Incoming calls are sent only to ephone-dns on phones that are
                              		  on-hook.

```
ephone-hunt 17 peer
pilot 3000
list 3011, 3021, 3031
hops 3
final 7600
present-call onhook-phone
```

### Related Commands

Description

ephone-hunt

Defines an ephone hunt group and enters ephone-hunt
                                          						configuration mode.

## present-call
                        	 (voice hunt-group)

To present voice
                              		  hunt-group calls only to member phones that are idle, use the present-call command in voice hunt group configuration mode. To return to the default, use
                              		  the no form of
                              		  this command.

present-call { idle-phone }

no present-call { idle-phone }

### Syntax Description

idle-phone

Presents calls from the voice hunt group only if all lines are idle on the
                                          						phone on which the hunt group line appears.

### Command Default

Voice hunt group
                              		  calls are presented to lines (ephone-dns or voice register dns) that are not in
                              		  use, regardless of the state of other lines on the same ephone or voice
                              		  register pool.

### Command Modes

voice hunt-group configuration (config-voice-hunt)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

Cisco
                                          						IOS XE Everest 16.4.1

15.6(3)M1

Cisco
                                          						Unified CME 11.6

This
                                          						command was introduced for voice hunt group.

### Usage Guidelines

If you do not use
                              		  this command, voice hunt group presents calls to an ephone or voice register
                              		  pool whenever the phone line (ephone-dn or voice register dn) that corresponds
                              		  to a number in a voice hunt group list is available. The status of other phone
                              		  lines on the phone is not considered.

The present-call command adds additional controls that allow you to take into
                              		  account the activity on all lines of a phone that has an ephone-dn or voice
                              		  register dn that is assigned to a voice hunt group. The present-call command allows you to specify that hunt groups should present calls to these
                              		  phones only when they are idle or not busy with an active call. This keeps hunt
                              		  group calls from possibly going unanswered because a phone is occupied with a
                              		  call on a line other than the line assigned to the hunt group.

## Examples

The following
                              		  example sets up a peer hunt group with three ephone-dns to answer calls.
                              		  Incoming calls are sent only to ephone-dns or voice register dns on phones that
                              		  are idle.

```
voice hunt-group 17 peer
pilot 3000
list 3011, 3021, 3031
final 7600
present-call idle-phone
```

### Related Commands

Description

voice hunt-group

Defines
                                          						a voice hunt group and enters voice hunt-group configuration mode.

## privacy (ephone)

To modify privacy support on a specific phone, use the privacy command in ephone or ephone-template
                              		  configuration mode. To reset to the default value, use the no form of this command.

privacy [ off | on ]

no privacy

### Syntax Description

off

(Optional) Disables privacy on the phone.

on

(Optional) Enables privacy on the phone.

### Command Default

Use system-level setting configured with the privacy command in telephony-service mode.

### Command Modes

Ephone configuration (config-ephone) Ephone-template configuration (config-ephone-template)

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

This command modifies the privacy capability of individual phones.
                              		  Privacy prevents other phone users from seeing call information or barging into
                              		  a call on a shared octo-line directory number. Privacy is supported for calls
                              		  on shared octo-line directory numbers only.

If only specific phones require access to privacy, disable privacy at
                              		  the system-level by using the no privacy command in telephony-service configuration mode and enable
                              		  privacy at the phone-level by using the privacy on command.

After a phone that is configured for privacy registers with Cisco
                              		  Unified CME, the feature button on the phone is labeled “Privacy” and a status
                              		  icon displays. If the button has a lamp, it lights. When the phone receives an
                              		  incoming call, the user can make the call private by pressing the Privacy
                              		  feature button. The privacy button toggles between on and off. The privacy
                              		  state is applied to new calls and current calls that the user owns.

Users can dynamically enable privacy for shared-line calls by
                              		  pressing the Privacy feature button on the phone if the privacy-button command is enabled.

The Privacy feature applies to all shared lines on a phone. If a
                              		  phone has multiple shared lines and Privacy is enabled, other phones cannot
                              		  view or barge into calls on any of the shared lines.

If you use an ephone template to apply a command to an ephone and you
                              		  also use the same command in ephone configuration mode for the same ephone, the
                              		  value that you set in ephone configuration mode has priority.

## Examples

The following example shows privacy enabled on a specific phone and
                              		  disabled at the system-level:

```
telephony-service
 no privacy
 privacy-on-hold
 max-ephones 100
 max-dn 240
!
!
ephone  10
 privacy on
 privacy-button
 max-calls-per-button 3
 busy-trigger-per-button 2
 mac-address 00E1.CB13.0395
 type 7960
 button  1:7 2:10
```

### Related Commands

Command

Description

privacy (telephony-service)

Enables privacy globally for all phones in the system.

privacy-button

Enables the privacy feature button on an IP phone.

privacy-on-hold

Enables privacy for calls that are on hold on shared
                                          						octo-line directory numbers.

## privacy (telephony-service)

To enable privacy at the system level for all phones, use the privacy command in telephony-service
                              		  configuration mode. To disable privacy at the system level, use the no form of this command.

privacy

no privacy

### Syntax Description

This command has no arguments or keywords.

### Command Default

Privacy is enabled at the system level for all phones.

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

This command enables privacy for all phones in the system. Privacy
                              		  prevents other phone users from seeing call information or joining a call on a
                              		  shared octo-line directory number. Privacy is supported for calls on shared
                              		  octo-line directory numbers only.

If only specific phones need access to privacy, disable privacy at
                              		  the system-level by using the no privacy command and enable privacy at the phone level by using the privacy on command in ephone or ephone-template
                              		  configuration mode.

After a phone that is configured for privacy registers with Cisco
                              		  Unified CME, the feature button on the phone is labeled “Privacy” and a status
                              		  icon displays. The button lamp, if available, lights to reflect the privacy
                              		  setting of the phone. When the phone receives an incoming call, the user can
                              		  make the call private by pressing the Privacy feature button.

## Examples

The following example shows privacy disabled at the system-level and
                              		  enabled on an individual phone:

```
telephony-service
 no privacy
 privacy-on-hold
 max-ephones 100
 max-dn 240
 timeouts transfer-recall 60
 voicemail 8900
 max-conferences 8 gain -6
 transfer-system full-consult
 fac standard
!
!
ephone  10
 privacy on
 privacy-button
 max-calls-per-button 3
 busy-trigger-per-button 2
 mac-address 00E1.CB13.0395
 type 7960
 button  1:7 2:10
```

### Related Commands

Command

Description

privacy (ephone)

Modifies privacy support on a specific phone.

privacy-button

Enables the privacy feature button on an IP phone.

privacy-on-hold

Enables privacy for calls that are on hold on shared
                                          						octo-line directory numbers.

## privacy (voice register global)

To enable privacy at the system level for all SIP phones, use the privacy command in voice register global
                              		  configuration mode. To disable privacy at the system level, use the no form of this command.

privacy

no privacy

### Syntax Description

This command has no arguments or keywords.

### Command Default

Privacy is enabled at the system level for all phones.

### Command Modes

Voice register global configuration (config-register-global)

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

This command enables privacy for all phones in the system. Privacy
                              		  prevents other phone users from seeing call information or joining a call on a
                              		  shared-line directory number. Privacy is supported for calls on shared-line
                              		  directory numbers only.

If only specific phones need access to privacy, disable privacy at
                              		  the system-level by using the no privacy command and enable privacy at the phone level by using the privacy on command in voice register pool or voice
                              		  register template configuration mode.

After a phone that is configured with the privacy-button command registers with Cisco
                              		  Unified CME, the feature button on the phone is labeled “Privacy” and a status
                              		  icon displays. The button lamp, if available, lights to reflect the privacy
                              		  setting of the phone. When the phone receives an incoming call, the user can
                              		  make the call private by pressing the Privacy feature button.

## Examples

The following example shows privacy disabled at the system-level and
                              		  enabled on an individual phone:

```
voice register global
 mode cme
 privacy-on-hold
 no privacy
 max-dn 300
 max-pool 150
 voicemail 8900
 call-feature-uri pickup http://10.4.212.11/pickup
 call-feature-uri gpickup http://10.4.212.11/gpickup
!
voice register pool  130
 id mac 001A.A11B.500E
 type 7941
 number 1 dn 30
 template 6
 dnd
 privacy ON
```

### Related Commands

Command

Description

privacy (voice register pool)

Modifies privacy support on a specific phone.

privacy-button

Enables the privacy feature button on an IP phone.

privacy-on-hold

Enables privacy for calls that are on hold on shared-line
                                          						directory numbers.

shared-line

Creates a shared-line directory number for a SIP phone.

## privacy (voice register pool)

To modify the phone-level privacy setting on a SIP phone, use the privacy command in voice register pool or
                              		  voice register template configuration mode. To reset to the default value, use
                              		  the no form of this command.

privacy { off | on }

no privacy

### Syntax Description

off

Disables privacy on the phone.

on

Enables privacy on the phone.

### Command Default

Use system-level setting configured with the privacy command in voice register global
                              		  mode.

### Command Modes

Voice register pool configuration (config-register-pool) Voice register template configuration (config-register-temp)

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

This command modifies the privacy setting on the SIP phone. Privacy
                              		  prevents other phone users from viewing call information or barging into a call
                              		  on a shared-line directory number. Privacy is supported for calls on
                              		  shared-line directory numbers only.

After a phone that is configured with the privacy-button command registers with Cisco
                              		  Unified CME, the feature button on the phone is labeled “Privacy” and a status
                              		  icon displays. If the button has a lamp, it lights. When the phone receives an
                              		  incoming call, the user can make the call private by pressing the Privacy
                              		  feature button. The privacy button toggles between on and off. The privacy
                              		  state applies to new calls and current calls that the phone user owns.

The off and on keywords specify the initial Privacy state
                              		  on the phone when the Privacy feature is enabled. The phone user can then
                              		  toggle the privacy state on and off using the Privacy feature button.

The Privacy state applies to all shared lines on a phone. If a phone
                              		  has multiple shared lines, other phones cannot view or barge into calls on any
                              		  of the shared lines if the Privacy state is enabled.

If you use a voice register template to apply a command to a phone
                              		  and you also use the same command in voice register pool configuration mode for
                              		  the same phone, the value that you set in voice register pool configuration
                              		  mode has priority.

## Examples

The following example shows privacy enabled for a specific SIP phone:

```
Router(config)# voice register pool 123 Router(config-register-pool)# privacy on
```

### Related Commands

Command

Description

privacy (voice register global)

Enables privacy at the system level for all SIP phones.

privacy-button

Enables the privacy feature button on an IP phone.

privacy-on-hold

Enables privacy for calls that are on hold on shared-line
                                          						directory numbers.

shared-line

Creates a shared-line directory number for a SIP phone.

softkeys remote-in-use (voice register template)

Modifies the soft-key display during the remote-in-use call
                                          						state on SIP phones.

template (voice register pool)

Applies a template to a SIP phone.

## privacy-button

To enable the privacy feature button on an IP phone, use the privacy-button command in ephone,
                              		  ephone-template, voice logout-profile, and voice user-profile configuration
                              		  mode. To reset to the default value, use the no form of this command.

privacy-button

no privacy-button

### Syntax Description

This command has no arguments or keywords.

### Command Default

Privacy button is disabled.

### Command Modes

Ephone configuration (config-ephone) Ephone-template configuration (config-ephone-template) Voice logout-profile configuration (config-logout-profile) Voice user-profile configuration (config-user-profile)

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

This command allows phone users to dynamically enable or disable
                              		  privacy for calls on shared octo-lines by pressing the Privacy feature button
                              		  on the phone. Privacy prevents other phone users from viewing call information
                              		  or joining calls on a shared octo-line directory number.

Privacy is supported only for calls on shared octo-line directory
                              		  numbers so enable this command only on phones that share an octo-line directory
                              		  number.

After a phone that is configured for privacy registers with Cisco
                              		  Unified CME, the feature button on the phone is labeled “Privacy” and a status
                              		  icon displays. The button lamp, if available, lights to reflect the privacy
                              		  setting of the phone. The privacy feature button toggles between on and off.
                              		  The privacy state is applied to new calls and current calls owned by the user.

Privacy is enabled on the phone with either the privacy command in ephone configuration mode or the privacy command in telephony-service mode.

If you use an ephone template to apply a command to an ephone and you
                              		  also use the same command in ephone configuration mode for the same ephone, the
                              		  value that you set in ephone configuration mode has priority.

## Examples

The following example shows the privacy button is enabled for ephone
                              		  10:

```
ephone  10
 privacy-button
 max-calls-per-button 3
 busy-trigger-per-button 2
 mac-address 00E1.CB13.0395
 type 7960
 button  1:7
```

### Related Commands

Command

Description

privacy (ephone)

Modifies privacy support on a specific phone.

privacy (telephony-service)

Enables privacy globally for all phones in the system.

privacy-on-hold

Enables privacy for calls that are on hold on shared
                                          						octo-line directory numbers.

## privacy-button (voice register pool)

To enable the privacy feature button on an IP phone, use the privacy-button command in voice register pool
                              		  or voice register template configuration mode. To reset to the default value,
                              		  use the no form of this command.

privacy-button

no privacy-button

### Syntax Description

This command has no arguments or keywords.

### Command Default

Privacy button is disabled.

### Command Modes

Voice register pool configuration (config-register-pool) Voice register template configuration (config-register-temp)

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

This command allows phone users to dynamically enable or disable
                              		  privacy for calls on shared lines by pressing the Privacy feature button on the
                              		  phone. Privacy prevents other phone users from viewing call information or
                              		  joining calls on a shared-line directory number.

Privacy is supported only for calls on shared-line directory numbers
                              		  so enable this command only on phones that use a shared-line directory number.

After a phone that is configured with this command registers with
                              		  Cisco Unified CME, the feature button on the phone is labeled “Privacy” and a
                              		  status icon displays. The button lamp, if available, lights to reflect the
                              		  privacy setting of the phone. The privacy feature button toggles between on and
                              		  off. The privacy state is applied to new calls and current calls owned by the
                              		  user.

Privacy is enabled on the phone with either the privacy command in voice register pool configuration mode or the privacy command in voice register global configuration mode.

If you use a voice register template to apply a command to a phone
                              		  and you also use the same command in voice register pool configuration mode for
                              		  the same phone, the value that you set in voice register pool configuration
                              		  mode has priority.

## Examples

The following example shows the privacy button is enabled for phone
                              		  124:

```
voice register pool  124
 busy-trigger-per-button 5
 id mac 0017.E033.0284
 type 7965
 number 1 dn 24
 privacy-button
```

### Related Commands

Command

Description

privacy (voice register global)

Enables privacy globally for all SIP phones in the system.

privacy (voice register pool)

Modifies privacy support on a specific phone.

privacy-on-hold (voice register global)

Enables privacy for calls that are on hold on shared-line
                                          						directory numbers.

shared-line

Creates a shared-line directory number for a SIP phone.

## privacy-on-hold

To enable privacy for calls that are on hold on shared octo-line
                              		  directory numbers, use the privacy-on-hold command in telephony-service
                              		  configuration mode. To disable privacy for calls on hold, use the no form of this command.

privacy-on-hold

no privacy-on-hold

### Syntax Description

This command has no arguments or keywords.

### Command Default

Privacy on hold is disabled.

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

This command prevents other phone users from seeing or retrieving
                              		  calls that are on hold on a shared octo-line directory number.

Privacy is enabled on the phone with either the privacy command in ephone configuration mode or the privacy command in telephony-service mode.

## Examples

The following example shows how to enable privacy on hold for shared
                              		  lines.

```
Router(config)# telephony-service Router(config-telephony)# privacy-on-hold
```

### Related Commands

Command

Description

privacy (ephone)

Modifies privacy support on a specific phone.

privacy (telephony-service)

Enables privacy globally for all phones in the system.

privacy-button

Enables the privacy feature button on an IP phone.

## privacy-on-hold (voice register global)

To enable privacy for calls that are on hold on shared-line directory
                              		  numbers, use the privacy-on-hold command in voice register
                              		  global configuration mode. To disable privacy for calls on hold, use the no form of this command.

privacy-on-hold

no privacy-on-hold

### Syntax Description

This command has no arguments or keywords.

### Command Default

Privacy on hold is disabled.

### Command Modes

Voice register global (config-register-global)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(22)YB

Cisco Unified CME 7.1

This command was introduced.

### Usage Guidelines

This command prevents other phone users from seeing or retrieving
                              		  calls that are on hold on a shared-line directory number.

Privacy is enabled on the phone with either the privacy command in voice register pool configuration mode or the privacy command in voice register global configuration mode.

## Examples

The following example shows how to enable privacy on hold for shared
                              		  lines.

```
Router(config)# voice register global Router(config-register-global)# privacy-on-hold
```

### Related Commands

Command

Description

privacy (voice register global)

Enables privacy globally for all phones in the system.

privacy (voice register pool)

Modifies privacy support on a specific phone.

privacy-button (voice register pool)

Enables the privacy feature button on an IP phone.

shared-line

Creates a shared-line directory number for a SIP phone.

## protocol mode

To configure the Cisco IOS Session Initiation Protocol (SIP) stack,
                              		  use the protocol mode command in SIP user-agent configuration mode. To disable the
                              		  configuration, use the no form of this command.

protocol mode { ipv4 | ipv6 | dual-stack [ preference { ipv4 | ipv6 }]}

no protocol mode

### Syntax Description

ipv4

Specifies the IPv4-only mode.

ipv6

Specifies the IPv6-only mode.

dual-stack

Specifies the dual-stack (that is, IPv4 and IPv6) mode.

preference { ipv4 | ipv6

(Optional) Specifies the preferred dual-stack mode, which
                                          						can be either IPv4 (the default preferred dual-stack mode) or IPv6.

### Command Default

No protocol mode is configured. The Cisco IOS SIP stack operates in
                              		  IPv4 mode when the no protocol mode or protocol mode ipv4 command is configured.

### Command Modes

SIP user-agent configuration (config-sip-ua)

## Command History

Release

Modification

12.4(22)T

This command was introduced.

15.1(1)T

This command was integrated into Cisco IOS Release
                                          						15.1(1)T.

### Usage Guidelines

The protocol mode command is used to configure the Cisco IOS
                              		  SIP stack in IPv4-only, IPv6-only, or dual-stack mode. For dual-stack mode, the
                              		  user can (optionally) configure the preferred family, IPv4 or IPv6.

For a particular mode (for example, IPv6-only), the user can
                              		  configure any address (for example, both IPv4 and IPv6 addresses) and the
                              		  system will not hide or restrict any commands on the router. SIP chooses the
                              		  right address for communication based on the configured mode on a per-call
                              		  basis.

For example, if the domain name system (DNS) reply has both IPv4 and
                              		  IPv6 addresses and the configured mode is IPv6-only (or IPv4-only), the system
                              		  discards all IPv4 (or IPv6) addresses and tries the IPv6 (or IPv4) addresses in
                              		  the order they were received in the DNS reply. If the configured mode is
                              		  dual-stack, the system first tries the addresses of the preferred family in the
                              		  order they were received in the DNS reply. If all of the addresses fail, the
                              		  system tries addresses of the other family.

## Examples

The following example configures dual-stack as the protocol mode:

```
Router(config-sip-ua)# protocol mode dual-stack
```

The following example configures IPv6 only as the protocol mode:

```
Router(config-sip-ua)# protocol mode ipv6
```

The following example configures IPv4 only as the protocol mode:

```
Router(config-sip-ua)# protocol mode ipv4
```

The following example configures no protocol mode:

```
Router(config-sip-ua)# no protocol mode
```

### Related Commands

Command

Description

sip ua

Enters SIP user-agent configuration mode.

## protocol-mode (telephony-service)

To configure a preferred IP address mode for SCCP IP phones in Cisco
                              		  Unified CMEr, use rthe protocol mode command in telephony service configuration
                              		  mode. To disable the router protocol mode, use the no form of this command.

protocol mode { ipv4 | ipv6 | dual-stack [ preference { ipv4 | ipv6 }]}

no protocol mode { ipv4 | ipv6 | dual-stack [ preference { ipv4 | ipv6 }]}

### Syntax Description

ipv4

IPv4-only mode.

ipv6

IPv6-only mode.

dual-stack

Dual-stack mode, ipv4 and ipv6 mode.

preference

Preference dual-stack mode, either ipv4 or ipv6 mode.

### Command Default

No protocol mode is configured

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.0(1)XA

Cisco Unified CME 8.0

This command was introduced.

### Usage Guidelines

The protocol mode command is used to configure SCCP IP phones
                              		  in CUCME in IPv4-only, IPv6-only, or dual-stack mode. For dual-stack mode, the
                              		  user can configure the preferred family, IPv4 or IPv6.

For a specific mode, the user is free to configure any address and
                              		  the system will not hide or restrict any commands on the router. On a per-call
                              		  basis, SCCP phones choose the right address for communication based on the
                              		  configured mode.

For example, if the DNS reply has both IPv4 and IPv6 addresses and
                              		  the configured mode is IPv6-only (or IPv4-only), the system discards all IPv4
                              		  (or IPv6) addresses and tries the IPv6 (or IPv4) addresses in the order they
                              		  were received in the DNS reply. If the configured mode is dual-stack, the
                              		  system first tries the addresses of the preferred family in the order they were
                              		  received in the DNS reply. If all of the addresses fail, the system tries
                              		  addresses of the other family.

## Examples

The following example configures dual-stack as the protocol mode:

```
Router(config)# telephony-service Router(config-telephony)#protocol mode dual-stack preference ?
  ipv4  IPv4 address is prefered
  ipv6  IPv6 address is prefered
```

The following example configures IPv6-only mode as the protocol mode:

```
Router(config)# telephony-service Router(config-telephony)#protocol mode ipv6
```

The following example configures IPv4-only mode as the protocol mode:

```
Router(config)# telephony-service Router(config-telephony)#protocol mode ipv6
```

### Related Commands

Command

Description

ip source-address

Identifies the IP address and port through which IP phones
                                          						communicate with a Cisco Unified CME router.

shutdown

Allows to shut down SCCP server listening sockets.

## provision-tag

To create a
                              		  provision tag for identifying an ephone or voice register pool for the
                              		  extension assigner application, use the provision-tag command in ephone configuration mode or voice register pool configuration mode.
                              		  To remove the provision tag, use the no form of
                              		  this command.

provision-tag tag

no provision-tag tag

### Syntax Description

tag

Unique
                                          						number that identifies this provision tag. Range: 1 to 2147483647.

### Command Default

No provision tag
                              		  is created.

### Command Modes

Ephone configuration (config-ephone)

Voice register
                              		  Pool (config-register-pool)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.4(4)XC4

Cisco
                                          						Unified CME 4.0(3)

This
                                          						command was introduced.

12.4(11)XJ

Cisco
                                          						Unified CME 4.1

This
                                          						command was introduced.

12.4(15)T

Cisco
                                          						Unified CME 4.1

This
                                          						command was integrated into Cisco IOS Release 12.4(15)T.

Cisco IOS XE Everest 16.4.1

15.6(3)M1

Cisco
                                          						Unified CME 11.6

This
                                          						command was supported under voice register pool for SIP phones.

### Usage Guidelines

This command
                              		  creates a provision tag.

For SCCP phones, a
                              		  provision tag enables you to use some number other than an ephone tag, such as
                              		  a jack number or an extension number, to identify an ephone configuration. The
                              		  provision tag can be used with the extension assigner application to assign the
                              		  corresponding ephone configuration to an IP phone. This command is ignored
                              		  unless you also use the extension-assigner tag-type command with the provision-tag keyword.

## Examples

The following
                              		  example shows that provision tag 1001 is configured for ephone 1 and provision
                              		  tag 1002 is configured for ephone 2:

```
Telephony-service
 extension-assigner tag-type provision-tag
 auto assign 101-102
 auto-reg-ephone
Ephone-dn 101
 number 1001
Ephone-dn 102
 number 1002
Ephone 1
 provision-tag 1001
 mac-address 02EA.EAEA.0001
 button 1:101
Ephone 2
 provision-tag 1002
 mac-address 02EA.EAEA.0002
 button 1:102
```

## Examples

For SIP phones,
                              		  a provision tag enables you to assign any number within the range as an
                              		  extension number. The provision tag is used with an extension assigner
                              		  application to assign the corresponding voice register pool configuration to an
                              		  IP phone.

The following
                              		  example shows that provision tag 1001 is configured for voice register pool 1
                              		  and provision tag 1002 is configured for voice register pool 2:

```
Voice register global
 auto-register 
	 password xxxx
  auto assign 101-102
voice register dn 101
 number 1001
voice register dn 102
 number 1002
voice register pool 1
 provision-tag 1001
 mac-address 02EA.EAEA.0001
 number 1 dn 101
voice register pool  2
 provision-tag 1002
 mac-address 02EA.EAEA.0002 
 number 2 dn 102
```

### Related Commands

Description

extension-assigner tag-type

Specifies which type of tag is used by the extension assigner application to
                                          						identify an ephone configuration.

| ip multicast-address | (Optional) Uses an IP multicast address to multicast voice
                                          						packets for audio paging; for example, 239.0.1.1. Note that IP phones do not
                                          						support multicast at 224.x.x.x addresses. Default is that multicast is not used
                                          						and IP phones are paged individually using IP unicast transmission (up to ten
                                          						phones). |
|---|---|
| port udp-port-number | (Optional) Uses this UDP port for the multicast. Range is
                                          						from 2000 to 65535. Default is 2000. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco ITS 2.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |

| Note | IP phones do not support multicast at 224.x.x.x addresses. |
|---|---|

| Command | Description |
|---|---|
| paging-dn | Assigns audio paging reception capability to a Cisco IP
                                          						phone. |
| paging group | Combines two or more paging sets into a combined paging
                                          						group. |

| paging-dn-tag | Comma-separated list of paging-dn-tags (unique sequence
                                          						numbers associated with paging ephone-dns) that have previously been associated
                                          						with the paging extension of a paging set using the paging-dn or paging-dn (voice register) command. You can include up to ten paging-dn-tags
                                          						separated by commas. For example, 4, 6, 7, 8. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco ITS 2.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |
| 15.2(2)T | Cisco Unifide CME 9.0 | This command was modified to include voice register pools
                                          						in the ephone-dn and paging groups. |

| Note | The correct paging port for the paging-dn of Cisco Unified SIP IP
                                       		  phones in the paging command is an even number from 20480
                                       		  to 32768. If you enter a wrong port number, a SIP REFER message request is sent
                                       		  to the IP phone but the Cisco Unified SIP IP phone is not paged. |
|---|---|

| Command | Description |
|---|---|
| paging | Creates a paging extension (ephone-dn) that can be called
                                          						in order to broadcast an audio page to a group of Cisco IP phones. |
| paging-dn | Assigns a paging extension (paging-dn) to a Cisco IP phone. |
| paging-dn (voice register) | Registers a Cisco Unified SIP IP phone to an ephone-dn
                                          						paging directory number. |

| paging-dn-tag | Dn-tag of an ephone-dn that was designated as a paging
                                          						ephone-dn with the paging command. |
|---|---|
| multicast | Uses multicast if available. By default, audio paging is
                                          						transmitted to the Cisco Unified IP phone using multicast. |
| unicast | Forces unicast paging for this phone. This keyword
                                          						indicates that the Cisco Unified IP phone is not capable of receiving audio
                                          						paging through multicast and requests that all pages to this phone be sent
                                          						through unicast. The maximum number of phones supported through unicast is ten. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco ITS 2.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was made available in ephone-template
                                          						configuration mode. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command in ephone-template configuration mode was
                                          						integrated into Cisco IOS Release 12.4(9)T. |

| Note | For unicast paging to all phones, omit the IP multicast address in
                                       		  the ephone-dn configuration. For unicast paging to a specific phone using an
                                       		  ephone-dn configured for multicast, add the unicast keyword as part of the paging-dn command in ephone configuration
                                       		  mode. |
|---|---|

|  | Description |
|---|---|
| ephone-template (ephone) | Applies a template to an ephone configuration. |
| number | Configures a valid number for the Cisco Unified IP phone. |
| paging | Creates a paging extension (ephone-dn) that can be called
                                          						in order to broadcast an audio page to a group of Cisco Unified IP phones. |
| paging group | Combines two or more paging sets into a combined paging
                                          						group. |

| paging-dn-tag | Ephone-dn tag designated as the paging ephone-dn to which a
                                          						Cisco Unified SIP IP phone is registered. |
|---|---|
| multicast | Transmits audio paging to the Cisco Unified IP phone using
                                          						multicast. This is the default. |
| unicast | Transmits audio paging to the Cisco Unified IP phone using
                                          						unicast.This indicates that the Cisco Unified IP phone is not capable of
                                          						receiving audio paging through multicast and requests that all pages to this
                                          						phone be sent through unicast. The maximum number of phones supported through
                                          						unicast is 12. |

| Release | Modification |
|---|---|
| 15.2(2)T | This command was introduced. |

| Command | Description |
|---|---|
| paging-dn | Creates a paging extension to receive audio pages on a
                                          						Cisco Unified SCCP IP phone in a Cisco Unified CME system. |
| paging group | Creates a combined paging group from two or more previously
                                          						established paging sets. |

| param-name | Name of the parameter. |
|---|---|
| param max-retries | (Optional) Number of attempts to re-enter account or
                                          						password. Value ranges from 0-10, default value is 0. |
| param passwd | (Optional) Character string that defines a predefined
                                          						password for authorization. |
| param passwd-prompt filename | (Optional) Announcement URL to request password input.
                                          						filename defines the name and location of the audio filename to be used for
                                          						playing the password prompt. |
| param user-prompt filename | (Optional) Announcement URL to request authorization code
                                          						username. filename defines the name and location of the audio filename to be
                                          						used for playing the username prompt. |
| param term-digit | Digit for terminating username or password digit input. |
| param abort-digit | Digit for aborting username or password digit input.
                                          						Default value is *. |
| param max-digits | Maximum number of digits in a username or password. Range
                                          						of valid value: 1 - 32. Default value is 32. |

| Release | Modification |
|---|---|
| 12.3(14)T | This command was introduced. |
| 15.1(3)T | This command was modified. The following keywords and
                                          						arguments were added: param max-retries, param passwd, param passwd-prompt
                                          						filename, param user-prompt filename, param term-digit, param max-digit. |

| Command | Description |
|---|---|
| call application voice | Defines the name of a voice application and specify the
                                          						location of the Tcl or VoiceXML document to load for this application. |
| param account-id-method | Configures an application to use a particular method to
                                          						assign the account identifier. |
| param convert-discpi-after-connect | Enables or disables conversion of a DISCONNECT message with
                                          						Progress Indicator set to PROG_INBAND (PI=8) to a regular DISCONNECT message
                                          						when the call is in the active state. |
| param event-log | Enables or disables logging for linkable Tcl functions
                                          						(packages). |
| param language | Configures the language parameter in a service or package
                                          						on the gateway. |
| param mode | Configures the call transfer mode for a package. |
| param pin-len | Defines the number of characters in the personal
                                          						identification number (PIN) for an application. |
| param redirect-number | Defines the telephone number to which a call is
                                          						redirected—for example, the operator telephone number of the service
                                          						provider—for an application. |
| param reroutemode | Configures the call transfer reroutemode (call forwarding)
                                          						for a package. |
| param retry-count | Defines the number of times a caller is permitted to
                                          						reenter the PIN for a designated application and passes that information to the
                                          						application. |
| param security | Configures security for linkable Tcl functions (packages). |
| paramspace | Enables an application to use parameters from the local
                                          						parameter space of another application. |
| param uid-length | Defines the number of characters in the UID for a package. |
| param warning-time | Defines the number of seconds of warning that a user
                                          						receives before the allowed calling time expires. |

| menu-number | Number that callers must dial to reach the pilot number of
                                          						an ephone hunt group. The range is from 1 to 10. The default is 1. |
|---|---|
| pilot-number | Ephone hunt group pilot number. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco CME 3.3 | This command was introduced to replace the call application voice aa-hunt command. |

|  | Description |
|---|---|
| application | Enters application configuration mode. |
| service | Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application. |

| aa-pilot-number | Telephone number that callers dial in order to reach this
                                          						AA service. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(14)T | Cisco CME 3.3 | This command was introduced to replace the call application voice aa-pilot command. |

|  | Description |
|---|---|
| application | Enters application configuration mode. |
| service | Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application. |

| seconds | Time that a call must wait before attempting or
                                          						reattempting to transfer a call to an ephone hunt group pilot number, in
                                          						seconds. Range is from 5 to 30 seconds. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(14)T | Cisco CME 3.3 | This command was introduced to replace the call application voice call-retry-timer command. |

|  | Description |
|---|---|
| application | Enters application configuration mode. |
| service | Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application. |

| max-co-value | Maximum value of digits coming from the CO. The digit
                                          						string can be any length, but the string length must be the same in the param co-did-min , param co-did-max , param store-did-min , and param store-did-max commands. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced to replace the call application voice co-did-max command. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command replaced the call application voice co-did-max command and was integrated into Cisco IOS Release
                                          						12.4(9)T. |

|  | Description |
|---|---|
| application | Enters application configuration mode. |
| service | Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application. |
| param co-did-min | Sets the lower boundary of the range of valid digits coming
                                          						from the PSTN Central Office (CO) that is used with the DID Digit Translation
                                          						Service. |
| param store-did-max | Sets the upper boundary of the range of digits that is
                                          						valid in the Cisco Unified CME numbering plan that is used with the DID Digit
                                          						Translation Service. |
| param store-did-min | Sets the lower boundary of the range of digits that is
                                          						valid in the Cisco Unified CME numbering plan that is used with the DID Digit
                                          						Translation Service. |

| min-co-value | Minimum value of digits coming from the CO. The digit
                                          						string can be any length, but the string length must be the same in the param co-did-max , param co-did-max , param store-did-min , and param store-did-max commands. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced to replace the call application voice co-did-min command. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command replaced the call application voice co-did-min command and was integrated
                                          						into Cisco IOS Release 12.4(9)T. |

|  | Description |
|---|---|
| application | Enters application configuration mode. |
| service | Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application. |
| param co-did-max | Sets the upper boundary of the range of valid digits coming
                                          						from the PSTN Central Office (CO) that is used with the DID Digit Translation
                                          						Service. |
| param store-did-max | Sets the upper boundary of the range of digits that is
                                          						valid in the Cisco Unified CME numbering plan that is used with the DID Digit
                                          						Translation Service. |
| param store-did-min | Sets the lower boundary of the range of digits that is
                                          						valid in the Cisco Unified CME numbering plan that is used with the DID Digit
                                          						Translation Service. |

| menu-number | Menu option number to be associated with the
                                          						dial-by-extension option. Range is from 1 to 9. There is no default. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(14)T | Cisco CME 3.3 | This command was introduced to replace the call application voice dial-by-extension-option command. |

|  | Description |
|---|---|
| application | Enters application configuration mode. |
| service | Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application. |

| did-prefix | Prefix to add. Range is from 0 to 99. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME4.0 | This command was introduced to replace the call application voice did-prefix command . |
| 12.4(9)T | Cisco Unified CME4.0 | This command replaced the call application voice did-prefix command and was integrated into Cisco IOS Release
                                          						12.4(9)T. |

|  | Description |
|---|---|
| application | Enters application configuration mode. |
| service | Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application. |

| menu-number | Menu option number (aa-hunt number) to be associated with
                                          						the drop-through option. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(14)T | Cisco CME 3.3 | This command was introduced to replace the call application voice drop-through-option command. |

|  | Description |
|---|---|
| application | Enters application configuration mode. |
| service | Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application. |

| audio-filename | Identifying part of the filename of the prompt to be played
                                          						when calls for the drop-through option are answered. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(14)T | Cisco CME 3.3 | This command was introduced to replace the call application voice drop-through-prompt command. |

|  | Description |
|---|---|
| application | Enters application configuration mode. |
| service | Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application. |

| password | Numeric string to be used as password for the extension
                                          						assigner application. Password string must be 2 to 10 characters long and can
                                          						contain numbers 0 to 9. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC4 | Cisco Unified CME 4.0(3) | This command was introduced. |
| 12.4(11)XJ | Cisco Unified CME 4.1 | This command was introduced. |
| 12.4(15)T | Cisco Unified CME 4.1 | This command was integrated into Cisco IOS Release
                                          						12.4(15)T. |

| Note | There is no no form of this command. To change or remove
                                       		  the password for the extension assigner application, remove the service using
                                       		  the no form of the service command in application configuration
                                       		  mode. |
|---|---|

|  | Description |
|---|---|
| application | Enters application configuration mode. |
| service | Loads and configures a specific, standalone application on
                                          						a dial peer. |

| aa-service-name | Service name that was assigned to the AA script with the service command. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(14)T | Cisco CME 3.3 | This command was introduced to replace the call application voice handoff-string command. |

|  | Description |
|---|---|
| application | Enters application configuration mode. |
| service | Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application. |

| number | Number of digits. The lower limit is 0; there is no upper
                                          						limit. The default is 5. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(14)T | Cisco CME 3.3 | This command was introduced to replace the call application voice max-extension-length command. |

|  | Description |
|---|---|
| application | Enters application configuration mode. |
| service | Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application. |

| seconds | Maximum length of time that the call-queue service can keep
                                          						redialing a hunt group pilot number, in seconds. Range: 20 to 3600. Default:
                                          						600. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(14)T | Cisco CME 3.3 | This command was introduced to replace the call application voice max-time-call-retry command. |
| 12.4(20)YA | Cisco Unified CME 7.0(1) | The minimum value of the seconds argument was increased from
                                          						0 to 20. |
| 12.4(22)T | Cisco Unified CME 7.0(1) | This command was integrated into Cisco IOS Release
                                          						12.4(22)T. |

| Command | Description |
|---|---|
| application | Enters application configuration mode. |
| call application voice load | Reloads the selected voice application script after it is
                                          						modified. |
| param call-retry-timer | Specifies the time interval before each attempt to retry to
                                          						connect a call to an ephone hunt group in a Cisco Unified CME B-ACD service. |
| param max-time-vm-retry | Specifies the maximum number of times that calls in a Cisco
                                          						Unified CME B-ACD call queue can attempt to connect to the alternate
                                          						destination number. |
| param second-greeting-time | Sets the length of the intervals between replays of the
                                          						second greeting to calls waiting in hunt group call queues that are part of a
                                          						Cisco Unified CME B-ACD service. |
| param voice-mail | Sets an alternate destination number to which to route
                                          						calls that cannot be connected to a hunt group that is part of a Cisco Unified
                                          						CME B-ACD service. |
| service | Enters application-parameter configuration mode to specify
                                          						the name of the application and the location of the Tcl script to load. |

| number | Number of times that the alternate destination number is
                                          						redialed by the call-queue service. Range is from 1 to 3. Default is 1. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(14)T | Cisco CME 3.3 | This command was introduced to replace the call application voice max-time-vm-retry command. |

|  | Description |
|---|---|
| application | Enters application configuration mode. |
| service | Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application. |

| number | Times to replay menu prompt before connecting a caller to
                                          						an operator. Range: 0 to 10. Default: 4. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(14)T | Cisco CME 3.3 | This command was introduced. |
| 12.4(22)YA | Cisco Unified CME 7.0(1) | The minimum value of the number argument was decreased from
                                          						1 to 0. |
| 12.4(22)T | Cisco Unified CME 7.0(1) | This command was integrated into Cisco IOS Release
                                          						12.4(22)T. |

| Command | Description |
|---|---|
| application | Enters application configuration mode. |
| call application voice load | Reloads the selected voice application script after it is
                                          						modified. |
| param aa-hunt | Declares a Cisco Unified CME B-ACD menu number and
                                          						associates it with the pilot number of an ephone hunt group. |
| service | Enters application-parameter configuration mode to specify
                                          						the name of the application and the location of the Tcl script to load. |

| number | Number of ephone hunt groups used by the service. Range is
                                          						1 to 10 for the call-queue service and 1 to 3 for an automated attendant (AA)
                                          						service. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(14)T | Cisco CME 3.3 | This command was introduced to replace the call application voice number-of-hunt-grps command. |

|  | Description |
|---|---|
| application | Enters application configuration mode. |
| service | Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application. |

| option-number | Number of the call-queue exit option. Range: 1 to 3. There
                                          						is no default. |
|---|---|
| extension-number | Extension number associated with the exit option. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)YA | Cisco Unified CME 7.0(1) | This command was introduced. |
| 12.4(22)T | Cisco Unified CME 7.0(1) | This command was integrated into Cisco IOS Release
                                          						12.4(22)T. |

| Command | Description |
|---|---|
| application | Enters application configuration mode. |
| call application voice load | Reloads the selected voice application script after it is
                                          						modified. |
| param queue-exit-option | Assigns a menu number to a call-queue exit option. |
| service | Enters application-parameter configuration mode to specify
                                          						the name of the application and the location of the Tcl script to load. |

| option-number | Number of the call-queue exit option. Range: 1 to 3. There
                                          						is no default. |
|---|---|
| menu-number | Menu option number associated with the exit option. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)YA | Cisco Unified CME 7.0(1) | This command was introduced. |
| 12.4(22)T | Cisco Unified CME 7.0(1) | This command was integrated into Cisco IOS Release
                                          						12.4(22)T. |

| Command | Description |
|---|---|
| application | Enters application configuration mode. |
| call application voice load | Reloads the selected voice application script after it is
                                          						modified. |
| param queue-exit-extension | Assigns an extension number to a call-queue exit option. |
| service | Enters application-parameter configuration mode to specify
                                          						the name of the application and the location of the Tcl script to load. |

| number | Number of calls that can be held in a call queue. Range is
                                          						1 to 30. Default is 10. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(14)T | Cisco CME 3.3 | This command was introduced to replace the call application voice queue-len command. |

|  | Description |
|---|---|
| application | Enters application configuration mode. |
| service | Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application. |

| 0 | Disables collection of call-queue debug information. |
|---|---|
| 1 | Enables collection of call-queue debug information |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(14)T | Cisco CME 3.3 | This command was introduced to replace the call application voice queue-manager-debugs command. |

|  | Description |
|---|---|
| application | Enters application configuration mode. |
| service | Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application. |

| extension-number | Extension number to which the auto-attendant service
                                          						forwards calls when the call queue is full. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)YA | Cisco Unified CME 7.0(1) | This command was introduced. |
| 12.4(22)T | Cisco Unified CME 7.0(1) | This command was integrated into Cisco IOS Release
                                          						12.4(22)T. |

| Command | Description |
|---|---|
| application | Enters application configuration mode. |
| call application voice load | Reloads the selected voice application script after it is
                                          						modified. |
| param queue-len | Specifies the number of calls that can be held in each call
                                          						queue in a Cisco Unified CME B-ACD service. |
| service | Enters application-parameter configuration mode to specify
                                          						the name of the application and the location of the Tcl script to load. |

| secondary-prefix | Prefix to add to digits in order to route calls to the
                                          						primary Cisco Unified CME router. Range is from 0 to 99. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced to replace the call application voice secondary-prefix command. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command replaced the call application voice secondary-prefix command and was integrated into Cisco IOS Release
                                          						12.4(9)T. |

|  | Description |
|---|---|
| application | Enters application configuration mode. |
| service | Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application. |

| seconds | Length of time intervals between playouts of the second
                                          						greeting to calls in a B-ACD call queue, in seconds. Range is from 30 to 120.
                                          						Default is 60. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(14)T | Cisco CME 3.3 | This command was introduced to replace the call application voice second-greeting-time command. |

|  | Description |
|---|---|
| application | Enters application configuration mode. |
| service | Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| Command | Description |
|---|---|
| application | Enters application configuration mode. |
| call application voice load | Reloads the selected voice application script after it is
                                          						modified. |
| gw-accounting aaa | Enables the gateway to send accounting CDRs to the RADIUS
                                          						server using VSAs (attribute 26). |
| service | Enters application-parameter configuration mode to specify
                                          						the name of the application and the location of the Tcl script to load. |

| queue-service-name | Name that was assigned to the B-ACD call-queue service with
                                          						the service command. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(14)T | Cisco CME 3.3 | This command was introduced to replace the call application voice service-name command. |

|  | Description |
|---|---|
| application | Enters application configuration mode. |
| service | Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application. |

| max-store-value | Maximum value of digits in the Cisco Unified CME dial plan.
                                          						The digit string can be any length, but the string length must be the same in
                                          						the param co-did-max , param co-did-min , param store-did-max , and param store-did-min commands. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced to replace the call application voice store-did-max command. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command replaced the call application voice store-did-max command and was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| Command | Description |
|---|---|
| application | Enters application configuration mode. |
| service | Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application. |
| param co-did-max | Sets the upper boundary of the range of valid digits coming
                                          						from the PSTN Central Office (CO) that is used with the Direct Inward Dial
                                          						Digit Translation Service. |
| param co-did-min | Sets the lower boundary of the range of valid digits coming
                                          						from the PSTN Central Office (CO) that is used with the Direct Inward Dial
                                          						Digit Translation Service. |
| param store-did-min | Sets the lower boundary of the range of digits that is
                                          						valid in the Cisco Unified CME numbering plan that is used with the Direct
                                          						Inward Dial Digit Translation Service. |

| min-store-value | Minimum value of digits in the Cisco Unified CME dial plan.
                                          						The digit string can be any length, but the string length must be the same in
                                          						the param co-did-max , param co-did-min , param store-did-max , and param store-did-min commands. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced to replace the call application voice store-did-min command. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command replaced the call application voice store-did-min command and was integrated into Cisco IOS Release
                                          						12.4(9)T. |

|  | Description |
|---|---|
| application | Enters application configuration mode. |
| service | Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application. |
| param co-did-max | Sets the upper boundary of the range of valid digits coming
                                          						from the PSTN Central Office (CO) that is used with the DID Digit Translation
                                          						Service. |
| param co-did-min | Sets the lower boundary of the range of valid digits coming
                                          						from the PSTN Central Office (CO) that is used with the DID Digit Translation
                                          						Service. |
| param store-did-max | Sets the upper boundary of the range of digits that is
                                          						valid in the Cisco Unified CME numbering plan that is used with the DID Digit
                                          						Translation Service. |

| number | Extension number to which to route calls. The number must
                                          						be associated with a dial peer that is reachable by the Cisco Unified CME
                                          						system. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(14)T | Cisco CME 3.3 | This command was introduced to replace the call application voice voice-mail command. |

|  | Description |
|---|---|
| application | Enters application configuration mode. |
| service | Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application. |

| audio-filename | Identifier part of name of the audio file that contains the
                                          						welcome greeting to be played when callers first reach the Cisco Unified CME
                                          						B-ACD service. This name does not include the language prefix and it must begin
                                          						with an underscore. Default is _bacd_welcome.au. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(14)T | Cisco CME 3.3 | This command was introduced to replace the call application voice voice-mail command. |

|  | Description |
|---|---|
| application | Enters application configuration mode. |
| service | Enters application-parameter configuration mode and
                                          						specifies a name for the application and the location of the Tcl script to load
                                          						for the application. |

| true | Dial peer is exempt from call-blocking configuration. |
|---|---|
| false | Dial peer is subject to call-blocking configuration. This
                                          						is default. |

| Cisco IOS Release | Cisco Products | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 Cisco SRST 3.4 | This command was introduced. |

|  | Description |
|---|---|
| after-hour exempt | Specifies that a SCCP phone does not have any of its
                                          						outgoing calls blocked even though call blocking has been defined. |
| after-hour exempt (voice register dn) | Specifies that an individual SIP IP phone or a phone
                                          						extension on a SIP IP phone does not have any of its outgoing calls blocked
                                          						even though call blocking has been defined. |
| after-hour exempt (voice register pool) | Specifies that an individual SIP IP phone or phones in a
                                          						voice register pool does not have any of its outgoing calls blocked even though
                                          						call blocking has been defined. |
| after-hours block pattern | Defines a pattern of digits for blocking outgoing calls
                                          						from IP phones. |
| after-hours date | Defines a recurring period based on date during which
                                          						outgoing calls that match defined block patterns are blocked on IP phones. |
| after-hours day | Defines a recurring period based on day of the week during
                                          						which outgoing calls that match defined block patterns are blocked on IP
                                          						phones. |

| group-number | Unique number that identifies the reservation group. String
                                          						can contain up to 32 digits. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| call-park system | Defines system parameters for the call-park feature. |
| park-slot | Creates an extension (call-park slot) at which calls can be
                                          						temporarily held (parked). |

| directed | (Optional) Enables Directed Call Park for this extension. |
|---|---|
| reservation-group group-number | (Optional) Reserves this slot for phones configured with
                                          						the same reservation group. |
| reserved-for extension-number | (Optional) Reserves this slot as a private park slot for
                                          						the phone with the specified extension number as its primary line. All lines on
                                          						that phone can use this park slot. Note This keyword is ignored if the reservation-group keyword is used. | Note | This keyword is ignored if the reservation-group keyword is used. |
| Note | This keyword is ignored if the reservation-group keyword is used. |
| timeout seconds | (Optional) Sets the call-park reminder timeout in seconds.
                                          						Range: 0 to 65535. This reminder sends a 1-second ring to the IP phone that
                                          						parked the call and displays a message on the LCD panel of all phones in the
                                          						Cisco Unified CME system, indicating that a call is on hold. By default, the
                                          						reminder ring is sent only to the phone that parked the call. |
| limit count | (Optional) Sets a limit on the number of reminder or retry
                                          						timeouts. Range: 1 to 65535. |
| notify extension-number | (Optional) Sends a reminder ring to the specified extension
                                          						in addition to the reminder ring that is sent to the phone that parked the
                                          						call. |
| only | (Optional) Sends a reminder ring only to the extension
                                          						specified with the notify keyword and does not send a
                                          						reminder ring to the phone that parked the call. This option allows all
                                          						reminder rings for parked calls to be sent to a receptionist’s phone or an
                                          						attendant’s phone, for example. |
| recall | (Optional) Returns the call to the phone that parked it
                                          						after the timeout expires. |
| transfer extension-number | (Optional) Returns the call to the specified extension
                                          						after the timeout expires. |
| alternate extension-number | (Optional) Returns the call to this second target number if
                                          						the recall or transfer target phone is in use on any of its extensions (ringing
                                          						or connected). |
| retry seconds | (Optional) Sets the delay before another attempt to recall
                                          						or transfer a parked call, in seconds. Range: 0 to 65535. Number of attempts is
                                          						set by the limit keyword. |

| Note | This keyword is ignored if the reservation-group keyword is used. |
|---|---|

| Release | Cisco Product | Modification |
|---|---|---|
| 12.3(7)T | Cisco CME 3.1 | This command was introduced. |
| 12.4(4)XC | Cisco Unified CME 4.0 | The reserved-for , recall , transfer , alternate , and retry keywords were added. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |
| 12.4(22)YB | Cisco Unified CME 7.1 | The directed and reservation-group keywords and
                                          						support for SIP phones was added. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| call-park system | Defines system parameters for the call-park feature. |
| fac | Enables standard FACs or creates custom FACs. |
| number | Associates a telephone or extension number with a directory
                                          						number. |
| park reservation-group | Assigns a call-park reservation group to a phone. |

| password string | The
                                          						mandatory word string that administrator provides for auto registration of
                                          						phones on Unified CME. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 15.6(3)M 16.3.1 | Cisco
                                          						Unified CME 11.5 | This
                                          						command was introduced. |
| Cisco IOS XE Gibraltar 16.11.1a Release | Unified CME 12.6 | The command was enhanced for password encryption, based on Unified CME password policy. |

| Command | Description |
|---|---|
| service-enable (auto-register) | Temporarily disables the auto registration process, but retains
                                          						the password and DN range configurations. Once auto-register command is
                                          						entered, the service is enabled by default. |
| auto-register | Enables
                                          						automatic registration of SIP phones with the Cisco Unified CME system. |
| auto-assign (auto-register) | Configures the mandatory range of directory numbers for phones
                                          						auto registering on Unified CME. |
| template (auto-register) | Creates
                                          						a basic configuration template that supports all the configurations available
                                          						on the voice register template. |
| auto-reg-ephone | Enables automatic registration of ephones with the Cisco Unified CME system. |

| enable | Enables password-persistent to authenticate. |
|---|---|
| disable | Disables password-persistent to authenticate. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(3)T | Cisco Unified CME 8.5 | This command was introduced. |

| Command | Description |
|---|---|
| vpn-profile | Defines a VPN-profile. |

| tag | Number that identifies the dial pattern. Range: 1 to 24. |
|---|---|
| string | Dial pattern, such as the area code, prefix, and first one
                                          						or two digits of the telephone number, plus wildcard characters or dots (.) for
                                          						the remainder of the dialed digits. |
| button button-number | (Optional) Button to which the dial pattern applies. |
| timeout seconds | (Optional) Time, in seconds, that the system waits before
                                          						dialing the number entered by the user. Range: 0 to 30. To have the number
                                          						dialed immediately, specify 0. If this parameter is not used, the phone's
                                          						default interdigit timeout value is used (10 seconds). |
| user | (Optional) Tag that automatically gets added to the dialed
                                          						number. Do not use this keyword if Cisco Unified CME is the only SIP call
                                          						agent. |
| ip | (Optional) Sets the value of the user tag to IP in the
                                          						dialed number. |
| phone | (Optional) Sets the value of the user tag to phone in the
                                          						dialed number. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XJ | Cisco Unified CME 4.1 | This command was introduced. |
| 12.4(15)T | Cisco Unified CME 4.1 | This command was integrated into Cisco IOS Release
                                          						12.4(15)T. |

|  | Description |
|---|---|
| dialplan | Assigns a dial plan to a SIP phone. |
| filename | Specifies a custom configuration file that contains dial
                                          						patterns to use for the SIP dial plan. |
| show voice register dialplan | Displays all configuration information for a specific SIP
                                          						dial plan. |
| type (voice register dialplan) | Defines a phone type for a SIP dial plan. |

| tag1 | Alphanumeric string of fewer than four DTMF digits in
                                          						length. The alphanumeric string can consist of a combination of four letters
                                          						(A, B, C, and D), two symbols (* and #), and ten digits (0 to 9). The tag
                                          						numbers match the numbers defined in the voice-mail system’s integration file
                                          						and immediately precede the number of the calling party, the number of the
                                          						called party, or a forwarding number. |
|---|---|
| CDN | Called number (CDN) information is sent to the voice-mail
                                          						system. |
| CGN | Calling number (CGN) information is sent to the voice-mail
                                          						system. |
| FDN | Forwarding number (FDN) information is sent to the
                                          						voice-mail system. |
| tag2, tag3 | (Optional) Same as tag1 . The router supports a maximum
                                          						of four tags. |
| last-tag | (Optional) Same as tag1 . This tag indicates the end of
                                          						the pattern. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | 2.0 | This command was introduced |
| 12.2(8)T | 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |

|  | Description |
|---|---|
| pattern ext-to-ext busy | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension fails to connect to a
                                          						busy extension and the call is forwarded to voice mail. |
| pattern ext-to-ext no-answer | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension attempts to connect
                                          						to an extension that does not answer and the call is forwarded to voice mail. |
| pattern trunk-to-ext busy | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an external trunk call reaches a busy
                                          						extension and the call is forwarded to voice mail. |
| pattern trunk-to-ext no-answer | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when an external trunk call reaches an
                                          						unanswered extension and the call is forwarded to voice mail. |
| vm-integration | Enters voice-mail integration configuration mode and
                                          						enables voice-mail integration with DTMF and an analog voice-mail systems. |

| tag1 | Alphanumeric string of fewer than four DTMF digits in
                                          						length. The alphanumeric string can consist of a combination of four letters
                                          						(A, B, C, and D), two symbols (* and #), and ten digits (0 to 9). The tag
                                          						numbers match the numbers defined in the voice-mail system’s integration file
                                          						and immediately precede the number of the calling party, the number of the
                                          						called party, or a forwarding number. |
|---|---|
| CDN | Called number (CDN) information is sent to the voice-mail
                                          						system. |
| CGN | Calling number (CGN) information is sent to the voice-mail
                                          						system. |
| FDN | Forwarding number (FDN) information is sent to the
                                          						voice-mail system. |
| tag2, tag3 | (Optional) Same as tag1 . The router supports a maximum
                                          						of four tags. |
| last-tag | (Optional) Same as tag1 . This tag indicates the end of
                                          						the pattern. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco ITS 2.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |
| 12.2(13)T | Cisco SRST 2.02 | This command was added for Cisco SRST. |

|  | Description |
|---|---|
| pattern direct | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when the user presses the Messages button on the
                                          						phone. |
| pattern ext-to-ext no-answer | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension fails to connect to
                                          						an extension that does not answer and the call is forwarded to voice mail. |
| pattern trunk-to-ext busy | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an external trunk call reaches a busy
                                          						extension and the call is forwarded to voice mail. |
| pattern trunk-to-ext no-answer | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when an external trunk call reaches an
                                          						unanswered extension and the call is forwarded to voice mail. |
| vm-integration | Enters voice-mail integration configuration mode and
                                          						enables voice-mail integration with DTMF and an analog voice-mail systems. |

| tag1 | Alphanumeric string of fewer than four DTMF digits in
                                          						length. The alphanumeric string can consist of a combination of four letters
                                          						(A, B, C, and D), two symbols (* and #), and ten digits (0 to 9). The tag
                                          						numbers match the numbers defined in the voice-mail system’s integration file
                                          						and immediately precede the number of the calling party, the number of the
                                          						called party, or a forwarding number. |
|---|---|
| CDN | Called number (CDN) information is sent to the voice-mail
                                          						system. |
| CGN | Calling number (CGN) information is sent to the voice-mail
                                          						system. |
| FDN | Forwarding number (FDN) information is sent to the
                                          						voice-mail system. |
| tag2, tag3 | (Optional) Same as tag1 . The router supports a maximum
                                          						of four tags. |
| last-tag | (Optional) Same as tag1 . This tag indicates the end of
                                          						the pattern. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco ITS 2.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |
| 12.2(13)T | Cisco SRST 2.02 | This command was added for Cisco SRST. |

|  | Description |
|---|---|
| pattern direct | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when the user presses the Messages button on the
                                          						phone. |
| pattern ext-to-ext busy | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension fails to connect to
                                          						an extension and the call is forwarded to voice mail. |
| pattern trunk-to-ext busy | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an external trunk call reaches a busy
                                          						extension and the call is forwarded to voice mail. |
| pattern trunk-to-ext no-answer | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when an external trunk call reaches an
                                          						unanswered extension and the call is forwarded to voice mail. |
| vm-integration | Enters voice-mail integration configuration mode and
                                          						enables voice-mail integration with DTMF and an analog voice-mail systems. |

| tag1 | Alphanumeric string of fewer than four DTMF digits in
                                          						length. The alphanumeric string can consist of a combination of four letters
                                          						(A, B, C, and D), two symbols (* and #), and ten digits (0 to 9). The tag
                                          						numbers match the numbers defined in the voice-mail system’s integration file
                                          						and immediately precede the number of the calling party, the number of the
                                          						called party, or a forwarding number. |
|---|---|
| CDN | Called number (CDN) information is sent to the voice-mail
                                          						system. |
| CGN | Calling number (CGN) information is sent to the voice-mail
                                          						system. |
| FDN | Forwarding number (FDN) information is sent to the
                                          						voice-mail system. |
| tag2, tag3 | (Optional) Same as tag1 . The router supports a maximum
                                          						of four tags. |
| last-tag | (Optional) Same as tag1 . This tag indicates the end of
                                          						the pattern. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco ITS 2.0 | This command was introduced. |
| 12.2(8)T | Cisco SRST 2.02 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |
| 12.2(13)T | Cisco ITS 2.0 | This command was added for Cisco SRST. |

|  | Description |
|---|---|
| pattern direct | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when the user presses the Messages button on the
                                          						phone. |
| pattern ext-to-ext busy | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension fails to connect to
                                          						an extension and the call is forwarded to voice mail. |
| pattern ext-to-ext no-answer | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension fails to connect to
                                          						an extension and the call is forwarded to voice mail. |
| pattern trunk-to-ext no-answer | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when an external trunk call reaches an
                                          						unanswered extension and the call is forwarded to voice mail. |
| vm-integration | Enters voice-mail integration configuration mode and
                                          						enables voice-mail integration with DTMF and an analog voice-mail systems. |

| tag1 | Alphanumeric string of fewer than four DTMF digits in
                                          						length. The alphanumeric string can consist of a combination of four letters
                                          						(A, B, C, and D), two symbols (* and #), and ten digits (0 to 9). The tag
                                          						numbers match the numbers defined in the voice-mail system’s integration file
                                          						and immediately precede the number of the calling party, the number of the
                                          						called party, or a forwarding number. |
|---|---|
| CDN | Called number (CDN) information is sent to the voice-mail
                                          						system. |
| CGN | Calling number (CGN) information is sent to the voice-mail
                                          						system. |
| FDN | Forwarding number (FDN) information is sent to the
                                          						voice-mail system. |
| tag2, tag3 | (Optional) Same as tag1 . The router supports a maximum
                                          						of four tags. |
| last-tag | (Optional) Same as tag1 . This tag indicates the end of
                                          						the pattern. |

| Cisco IOS Release | Cisco CME Version | Modification |
|---|---|---|
| 12.2(2)XT | 2.0 | This command was introduced. |
| 12.2(8)T | 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |
| 12.2(13)T | 2.02 | This command was added for Cisco SRST. |

|  | Description |
|---|---|
| pattern direct | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when the user presses the Messages button on the
                                          						phone. |
| pattern ext-to-ext busy | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension fails to connect to
                                          						an extension and the call is forwarded to voice mail. |
| pattern ext-to-ext no-answer | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension fails to connect to
                                          						an extension and the call is forwarded to voice mail. |
| pattern trunk-to-ext busy | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an external trunk call reaches a busy
                                          						extension and the call is forwarded to voice mail. |
| vm-integration | Enters voice-mail integration configuration mode and
                                          						enables voice-mail integration with DTMF and an analog voice-mail systems. |

| Cisco
                                    				  IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.4(3)M | Cisco Unified CME 10.5 | This
                                       					 command was introduced. |

| Cisco
                                    				  IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.4(3)M | Cisco Unified CME 10.5 | This
                                       					 command was introduced. |

| Command | Description |
|---|---|
| voice register global | Enters
                                          						voice register global configuration mode. |
| voice register pool | Enters
                                          						voice register pool configuration mode. |
| voice register template | Enters
                                          						voice register template configuration mode. |

| 512 | 512 bits |
|---|---|
| 1024 | 1024 bits. This is the default key size. |
| 2048 | 2048 bits |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |

| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |
|---|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco Unified CME 4.3 Cisco Unified SRST 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| device-name | Assigns a name to a phone type in an ephone-type template. |
| load | Associates a type of Cisco Unified IP phone with a phone
                                          						firmware file. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.3(3)M | Cisco SIP
                                       					 CME 10.0 | This
                                       					 command was introduced. |

| Command | Description |
|---|---|
| voice register pool-type | Adds a new Cisco Unified SIP IP phone to Cisco Unified CME. |
| load | Associates a type of IP phone with a phone firmware file. |

| number | Maximum number of 3XX responses accepted for a single call.
                                          						Range: 5 to 20. Default: 5. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

|  | Description |
|---|---|
| voice register global | Enters voice register global configuration mode in order to
                                          						set global parameters for all supported Cisco SIP phones in a Cisco CME or
                                          						Cisco SIP SRST environment. |

| Cisco
                                    				  IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.4(3)M | Cisco Unified CME 10.5 | This
                                       					 command was introduced. |

| Command | Description |
|---|---|
| url button | Enables
                                          						the configuration of the URL Services feature button on a line key. |
| url services | Associates a URL with the Programmable Services feature
                                          						button on the supported Cisco Unified SCCP phones. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| fastdial | Creates an entry for a personal speed-dial number. |
| speed-dial | Creates speed-dial definitions for a phone. |
| url services | Associates a URL with the programmable Services feature
                                          						button on supported Cisco Unified IP phones. |

| Cisco
                                    				  IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.4(3)M | Cisco Unified CME 10.5 | This
                                       					 command was introduced. |

| Command | Description |
|---|---|
| url services | Associates a URL with the Programmable Services feature button on supported
                                          						Cisco Unified IP phones. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| pickup-group | Assigns an extension to a call-pickup group. |
| service directed-pickup | Enables Directed Call Pickup and modifies the function of
                                          						the GPickUp and PickUp soft keys. |
| softkeys idle | Modifies the soft-key display on IP phones during the idle
                                          						call state. |

| group-number | String representing a pickup group. The string can contain
                                          						up to 32 characters. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was added to ephone-dn-template configuration
                                          						mode. |

| 12.4(9)T | Cisco Unified CME 4.0 | This command in ephone-dn-template configuration mode was
                                          						integrated into Cisco IOS Release 12.4(9)T. |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was added to voice register dn configuration
                                          						mode for SIP directory numbers. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| ephone-dn-template (ephone-dn) | Applies a template to an ephone-dn configuration. |
| service directed-pickup | Enables Directed Call Pickup and modifies the function of
                                          						the PickUp and GPickUp soft keys. |

| number | String of up to 27 characters that represents an E.164
                                          						telephone number. Normally the string is composed of digits, but the string may
                                          						contain alphabetic characters if the number is dialed only by the router, as
                                          						with an intercom number, or is not intended to be dialed at all. Secondary
                                          						numbers can contain wildcards in the string. For details, see “Usage
                                          						Guidelines.” |
|---|---|
| secondary | (Optional) Defines the number that follows as an additional
                                          						pilot number for the ephone hunt group. |

| Cisco IOS Release | Cisco product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.3(7)T | Cisco CME 3.1 | The secondary secondary- number keyword-argument pair was introduced. |

|  | Description |
|---|---|
| ephone-hunt | Enters ephone-hunt configuration mode to define a Cisco CME
                                          						ephone hunt group. |
| final | Defines the last ephone-dn in an ephone hunt group. |
| hops | Defines the number of times that a call is redirected to
                                          						the next ephone-dn in a peer ephone-hunt-group list before proceeding to the
                                          						final ephone-dn. |
| list | Lists the ephone-dns that participate in an ephone hunt
                                          						group. |
| max-redirect | Changes the current number of allowable redirects in a
                                          						Cisco CME system. |
| no-reg (ephone-hunt) | Specifies that the pilot number of an ephone hunt group
                                          						should not register with the H.323 gatekeeper. |
| preference (ephone-hunt) | Sets preference order for the ephone-dn associated with an
                                          						ephone-hunt-group pilot number. |
| timeout (ephone-hunt) | Sets the number of seconds after which a call that is not
                                          						answered is redirected to the next number in the ephone-hunt-group list. |

| number | String of up to 32 characters that represents an extension
                                          						or E.164 telephone number. |
|---|---|
| secondary | (Optional) Defines an additional pilot number for the voice
                                          						hunt group. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

|  | Description |
|---|---|
| dialplan-pattern | Defines a pattern that is used to expand extension numbers
                                          						into fully qualified E.164 numbers. |
| final (voice hunt-group) | Defines the last extension in a voice hunt group. |
| hops (voice hunt-group) | Defines the number of times that a call is redirected to
                                          						the next directory number in a peer voice hunt-group list before proceeding to
                                          						the final directory number. |
| list (voice hunt-group) | Defines the directory numbers that participate in a hunt
                                          						group. |
| voice hunt-group | Defines the type of hunt group. |

| number | PIN that will be used to log in to a Cisco IP phone. This
                                          						is a numeric string from four to eight digits in length. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

|  | Description |
|---|---|
| after-hour exempt | Specifies that an IP phone does not have any of its
                                          						outgoing calls blocked even though call blocking has been defined for a Cisco
                                          						CME system. |
| after-hours block pattern | Defines a pattern of digits to be blocked for outgoing
                                          						calls from IP phones. |
| after-hours date | Defines a recurring period based on month and day during
                                          						which outgoing calls that match defined call-block patterns are blocked on IP
                                          						phones. |
| after-hours day | Defines a recurring period based on day of the week during
                                          						which outgoing calls that match defined call-block patterns are blocked on IP
                                          						phones. |
| login | Defines when IP phones in a Cisco CME system are logged out
                                          						automatically. |
| show ephone login | Displays the login states of all phones. |

| number | Four- to eight-digit numeric string for accessing Cisco
                                          						Unified IP phone. |
|---|---|
| [0\|6] | The 0 in the parameter [0\|6] mentioned in the CLI command represents plain, unencrypted text and 6 represents level 6 password
                                          encryption. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XW | Cisco Unified CME 4.2 | This command was introduced. |
| 12.4(15)XY | Cisco Unified CME 4.2(‘1) | This command was introduced. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| Cisco IOS XE Gibraltar 16.11.1a  Release | Unified CME 12.6 | The command was enhanced for password encryption. |

| Command | Description |
|---|---|
| logout-profile | Enable an SCCP phone for Extension Mobility and apply
                                          						logout profile to phone being configured. |
| reset (voice logout-profile and voice user-profile) | Performs complete reboot of all IP phones on which a
                                          						particular logout-profile or user-profile is downloaded. |

| digits | PIN to bypass the after-hour call block on the Cisco
                                          						Unified SIP IP phone. Numeric string from four to eight digits in length. The 0 in the parameter [0\|6] mentioned in the CLI command represents plain, unencrypted text and 6 represents level 6 password
                                          encryption. |
|---|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.2(2)T | Unified CME 9.0 | This command was introduced. |
| Cisco IOS XE Gibraltar 16.11.1a  Release | Unified CME 12.6 | The command was enhanced for password encryption. |

| Command | Description |
|---|---|
| voice register pool | Enters voice register pool configuration mode and creates a
                                          						pool configuration for Cisco Unified SIP IP phones in Cisco Unified CME. |

| tcp-port | Port for secure communication. Range is from 2000 to 9999.
                                          						Default is 3804. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| seconds | Number of seconds to reserve the channel. Range: 3 to 30.
                                          						Default: 0. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| preemption enable | Enables preemption capabilities on a trunk group. |
| preemption tone timer | Sets the expiry time for the preemption tone for the
                                          						outgoing call being preempted by a DDR backup call. |
| preemption user | Enables phones to preempt calls. |

| seconds | Length of preemption tone, in seconds. Range: 3 to 30.
                                          						Default: 0. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| mlpp indication | Enables MLPP indication on an SCCP phone or analog FXS
                                          						port. |
| mlpp preeemption | Enables the preemption capability on an SCCP phone or
                                          						analog FXS port. |
| preemption reserve timer | Sets the amount time to reserve a channel for a preemption
                                          						call. |
| preemption user | Enables the preemption capability for all supported phones. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| mlpp preemption | Enables calls on an SCCP phone or analog FXS port to be
                                          						preempted. |
| preemption user | Enables phones to preempt calls. |

| Cisco IOS Release | Cisco Products | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| mlpp preemption | Enables preemption capabilities on an SCCP phone or analog
                                          						FXS port. |
| preemption trunkgroup | Enables preemption capabilities on a trunk group. |

| preference-order | Preference order for the primary number associated with an
                                          						extension (ephone-dn). Type ? for a range, where 0 is the
                                          						highest preference. Default is 0. |
|---|---|
| secondary secondary-order | (Optional) Preference order for the secondary number
                                          						associated with the ephone-dn. Type ? for a range, where 0 is the
                                          						highest preference. Default is 9. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco ITS 1.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |
| 12.2(15)ZJ | Cisco CME 3.0 | The secondary secondary-order keyword-argument
                                          						pair was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| ephone-dn | Enters ephone-dn configuration mode. |
| huntstop | Discontinues call hunting behavior for an extension
                                          						(ephone-dn) or an extension channel. |

| preference-order | Preference order. Range is 0 to 8, where 0 is the highest
                                          						preference and 8 is the lowest preference. Default is 0. |
|---|---|
| secondary secondary-order | (Optional) Preference order for the secondary pilot number.
                                          						Range is 1 to 8, where 1 is the highest preference and 8 is the lowest
                                          						preference. Default is 7. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.3(7)T | Cisco CME 3.1 | The secondary secondary-order keyword-argument
                                          						pair was introduced. |

| Command | Description |
|---|---|
| final | Defines the last ephone-dn in an ephone hunt group. |
| hops | Defines the number of times that a call is redirected to
                                          						the next ephone-dn in a peer ephone-hunt-group list before proceeding to the
                                          						final ephone-dn. |
| list | Lists the ephone-dns that participate in an ephone hunt
                                          						group. |
| max-redirect | Changes the current number of allowable redirects in an
                                          						Cisco CME system. |
| no-reg (ephone-hunt) | Specifies that the pilot number of an ephone hunt group not
                                          						register with the H.323 gatekeeper. |
| pilot | Defines the ephone-dn that callers dial to reach an ephone
                                          						hunt group. |
| timeout (ephone-hunt) | Sets the number of seconds after which a call that is not
                                          						answered is redirected to the next number in the ephone-hunt-group list. |

| preference-order | Preference order for the extension or telephone number
                                          						associated with a dial peer. Range is 0 to 8. Default is 0. |
|---|---|
| secondary secondary-order | (Optional) Preference order for the secondary pilot number.
                                          						Range is 1 to 8, where 1 is the highest preference and 8 is the lowest
                                          						preference. Default is 7. |

| Cisco IOS Release | Version | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

| Note | It is recommended that the parallel hunt-group pilot number be
                                       		  unique in the system. Parallel hunt groups may not work if there are more than
                                       		  one partial or exact dial-peer match. For example, this happens if the pilot
                                       		  number is “8000” and there is another dial peer that matches “8...”. If
                                       		  multiple matches cannot be avoided, give call parallel hunt group the highest
                                       		  priority to run by assigning a lower preference to the other dial peers. Note
                                       		  that 8 is the lowest preference value. By default, dial peers created by
                                       		  parallel hunt groups have a preference of 0. |
|---|---|

| Command | Description |
|---|---|
| pilot (voice hunt-group) | Defines the voice dn that callers dial to reach a Cisco
                                          						CallManager Express (Cisco CME) voice hunt group. |
| voice hunt-group | Defines the type of hunt group. |

| preference-order | Preference order for the extension or telephone number
                                          						associated with a directory number. Range is 0 to 10. Default is 0. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 and Cisco SIP SRST 3.4 | This command was introduced. |

| Note | This command can also be used for Cisco SIP SRST. |
|---|---|

|  | Description |
|---|---|
| huntstop (voice register dn) | Discontinues call hunting behavior for an extension
                                          						(directory number) or an extension channel. |
| voice register dn | Enters voice register dn configuration mode to define an
                                          						extension for a SIP phone line. |

| preference-order | Preference order for the extension or telephone number
                                          						associated with a pool. Range is 0 to 10. Default is 0, which is the highest
                                          						preference. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SIP SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SIP SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was added to Cisco CallManager Express (Cisco
                                          						CME). |

| Note | Configure the id (voice register pool) command before any other voice register
                                       		  pool commands, including the preference command. The id command identifies a
                                       		  locally available individual SIP phone or set of Cisco SIP phones. |
|---|---|

|  | Description |
|---|---|
| id (voice register pool) | Explicitly identifies a locally available individual Cisco
                                          						SIP IP phone, or when running Cisco Unified SIP SRST, set of Cisco SIP IP
                                          						phones. |
| voice register pool | Enters voice register pool configuration mode for SIP
                                          						phones. |

| Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XJ | Cisco Unified CME 4.1 | This command was introduced. |
| 12.4(15)T | Cisco Unified CME 4.1 | This command was integrated into Cisco IOS Release
                                          						12.4(15)T. |

|  | Description |
|---|---|
| allow watch | Allows a directory number on a phone registered to Cisco
                                          						Unified CME to be watched in a presence service. |
| debug presence | Displays debugging information about the presence service. |
| max-subscription | Sets the maximum number of concurrent watch sessions that
                                          						are allowed. |
| presence enable | Allows the router to accept incoming presence requests. |
| server | Specifies the IP address of a presence server for sending
                                          						presence requests from internal watchers to external presence entities. |
| show presence global | Displays configuration information about the presence
                                          						service. |
| show presence subscription | Displays information about active presence subscriptions. |

| Release | Modification |
|---|---|
| 12.4(11)XJ | This command was introduced. |
| 12.4(15)T | This command was integrated into Cisco IOS Release
                                          						12.4(15)T. |

|  | Description |
|---|---|
| allow watch | Allows a directory number on a phone registered to Cisco
                                          						Unified CME to be watched in a presence service. |
| blf-speed-dial | Enables BLF monitoring for a speed-dial number on a phone
                                          						registered to Cisco Unified CME. |
| presence | Enables presence service and enters presence configuration
                                          						mode. |
| show presence global | Displays configuration information about the presence
                                          						service. |

| Release | Modification |
|---|---|
| 12.4(11)XJ | This command was introduced. |
| 12.4(15)T | This command was integrated into Cisco IOS Release
                                          						12.4(15)T. |

|  | Description |
|---|---|
| allow subscribe | Allows internal watchers to monitor external presence
                                          						entities (directory numbers). |
| allow watch | Allows a directory number on a phone registered to Cisco
                                          						Unified CME to be watched in a presence service. |
| max-subscription | Sets the maximum number of concurrent watch sessions that
                                          						are allowed. |
| show presence global | Displays configuration information about the presence
                                          						service. |
| show presence subscription | Displays information about active presence subscriptions. |
| watcher all | Allows external watchers to monitor internal presence
                                          						entities (directory numbers). |

| idle-phone | Presents calls from the ephone-hunt group only if all lines
                                          						are idle on the phone on which the hunt-group line appears. This option does
                                          						not consider monitored lines that have been configured on the phone using the button m command. |
|---|---|
| onhook-phone | Presents calls from the ephone-hunt group only if the phone
                                          						on which the number appears is in the onhook state. When this keyword is
                                          						configured, calls in the ringing or hold state that are unrelated to the hunt
                                          						group do not prevent the presentation of calls from the ephone-hunt group. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

|  | Description |
|---|---|
| ephone-hunt | Defines an ephone hunt group and enters ephone-hunt
                                          						configuration mode. |

| idle-phone | Presents calls from the voice hunt group only if all lines are idle on the
                                          						phone on which the hunt group line appears. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| Cisco
                                          						IOS XE Everest 16.4.1 15.6(3)M1 | Cisco
                                          						Unified CME 11.6 | This
                                          						command was introduced for voice hunt group. |

|  | Description |
|---|---|
| voice hunt-group | Defines
                                          						a voice hunt group and enters voice hunt-group configuration mode. |

| off | (Optional) Disables privacy on the phone. |
|---|---|
| on | (Optional) Enables privacy on the phone. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| privacy (telephony-service) | Enables privacy globally for all phones in the system. |
| privacy-button | Enables the privacy feature button on an IP phone. |
| privacy-on-hold | Enables privacy for calls that are on hold on shared
                                          						octo-line directory numbers. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| privacy (ephone) | Modifies privacy support on a specific phone. |
| privacy-button | Enables the privacy feature button on an IP phone. |
| privacy-on-hold | Enables privacy for calls that are on hold on shared
                                          						octo-line directory numbers. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| privacy (voice register pool) | Modifies privacy support on a specific phone. |
| privacy-button | Enables the privacy feature button on an IP phone. |
| privacy-on-hold | Enables privacy for calls that are on hold on shared-line
                                          						directory numbers. |
| shared-line | Creates a shared-line directory number for a SIP phone. |

| off | Disables privacy on the phone. |
|---|---|
| on | Enables privacy on the phone. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| privacy (voice register global) | Enables privacy at the system level for all SIP phones. |
| privacy-button | Enables the privacy feature button on an IP phone. |
| privacy-on-hold | Enables privacy for calls that are on hold on shared-line
                                          						directory numbers. |
| shared-line | Creates a shared-line directory number for a SIP phone. |
| softkeys remote-in-use (voice register template) | Modifies the soft-key display during the remote-in-use call
                                          						state on SIP phones. |
| template (voice register pool) | Applies a template to a SIP phone. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| privacy (ephone) | Modifies privacy support on a specific phone. |
| privacy (telephony-service) | Enables privacy globally for all phones in the system. |
| privacy-on-hold | Enables privacy for calls that are on hold on shared
                                          						octo-line directory numbers. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| privacy (voice register global) | Enables privacy globally for all SIP phones in the system. |
| privacy (voice register pool) | Modifies privacy support on a specific phone. |
| privacy-on-hold (voice register global) | Enables privacy for calls that are on hold on shared-line
                                          						directory numbers. |
| shared-line | Creates a shared-line directory number for a SIP phone. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| privacy (ephone) | Modifies privacy support on a specific phone. |
| privacy (telephony-service) | Enables privacy globally for all phones in the system. |
| privacy-button | Enables the privacy feature button on an IP phone. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |

| Command | Description |
|---|---|
| privacy (voice register global) | Enables privacy globally for all phones in the system. |
| privacy (voice register pool) | Modifies privacy support on a specific phone. |
| privacy-button (voice register pool) | Enables the privacy feature button on an IP phone. |
| shared-line | Creates a shared-line directory number for a SIP phone. |

| ipv4 | Specifies the IPv4-only mode. |
|---|---|
| ipv6 | Specifies the IPv6-only mode. |
| dual-stack | Specifies the dual-stack (that is, IPv4 and IPv6) mode. |
| preference { ipv4 \| ipv6 | (Optional) Specifies the preferred dual-stack mode, which
                                          						can be either IPv4 (the default preferred dual-stack mode) or IPv6. |

| Release | Modification |
|---|---|
| 12.4(22)T | This command was introduced. |
| 15.1(1)T | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| sip ua | Enters SIP user-agent configuration mode. |

| ipv4 | IPv4-only mode. |
|---|---|
| ipv6 | IPv6-only mode. |
| dual-stack | Dual-stack mode, ipv4 and ipv6 mode. |
| preference | Preference dual-stack mode, either ipv4 or ipv6 mode. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |

| Command | Description |
|---|---|
| ip source-address | Identifies the IP address and port through which IP phones
                                          						communicate with a Cisco Unified CME router. |
| shutdown | Allows to shut down SCCP server listening sockets. |

| tag | Unique
                                          						number that identifies this provision tag. Range: 1 to 2147483647. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
|  |  |  |
| 12.4(4)XC4 | Cisco
                                          						Unified CME 4.0(3) | This
                                          						command was introduced. |
| 12.4(11)XJ | Cisco
                                          						Unified CME 4.1 | This
                                          						command was introduced. |
| 12.4(15)T | Cisco
                                          						Unified CME 4.1 | This
                                          						command was integrated into Cisco IOS Release 12.4(15)T. |
| Cisco IOS XE Everest 16.4.1 15.6(3)M1 | Cisco
                                          						Unified CME 11.6 | This
                                          						command was supported under voice register pool for SIP phones. |

|  | Description |
|---|---|
| extension-assigner tag-type | Specifies which type of tag is used by the extension assigner application to
                                          						identify an ephone configuration. |