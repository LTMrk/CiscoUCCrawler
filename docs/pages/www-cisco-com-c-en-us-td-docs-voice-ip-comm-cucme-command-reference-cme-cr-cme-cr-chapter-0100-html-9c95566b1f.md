---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-command-reference-cme-cr-cme-cr-chapter-0100-html-9c95566b1f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/command/reference/cme_cr/cme_cr_chapter_0100.html
retrieved_at: 2026-08-21T22:55:58.833738+00:00
---

Cisco Unified Communications Manager Express Command Reference

# Cisco Unified Communications Manager Express Command Reference

Updated: July 19, 2018

Chapter: Cisco Unified CME Commands: E

## Chapter: Cisco Unified CME Commands: E

# Cisco Unified CME Commands: E

## elin

To create a PSTN number that replaces a 911 caller’s extension, use
                              		  the elin command in voice emergency response
                              		  location configuration mode. To remove the number, use the no form of this command.

elin { 1 | 2 } number

no elin [ 1 | 2 ]

### Syntax Description

{ 1 | 2 }

Number index.

number

PSTN number that replaces a 911 caller’s extension.

### Command Default

No replacement number is created.

### Command Modes

Voice emergency response location configuration (cfg-emrgncy-resp-location)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)T

Cisco Unified CME 4.1 Cisco Unified SRST 4.1 Cisco Unified
                                          						SIP SRST 4.1

This command was introduced. For Cisco Unified CME, this
                                          						command is supported in SRST fallback mode only.

12.4(15)XY

Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1)

This command was added for Cisco Unified CME.

12.4(20)T

Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

Use this command to specify an ELIN, a PSTN number that will replace
                              		  the caller’s extension.

The PSAP will see this number and use it to query the ALI database to
                              		  locate the caller. The PSAP also uses this command for callbacks.

You can configure a second ELIN using the elin 2 command. If two ELINs are configured, the system selects an
                              		  ELIN using a round-robin algorithm. If an ELIN is not defined for the ERL, the
                              		  PSAP sees the original calling number.

## Examples

In the following example, all IP phones with the IP address of
                              		  10.X.X.X or 192.168.X.X are automatically associated with this ERL. If one of
                              		  the phones dials 911, its extension is replaced with 408 555-0100 before it
                              		  goes to the PSAP. The PSAP will see that the caller’s number is 408 555-0100.

```
voice emergency response location 1
 elin 1 4085550100
 subnet 10.0.0.0 255.0.0.0
 subnet 2 192.168.0.0 255.255.0.0
```

### Related Commands

Command

Description

subnet

Defines which IP phones are part of this ERL.

## elin (voice emergency response settings)

To create a default ELIN that is used if no ERL has a subnet mask
                              		  that matches the current 911 caller’s IP phone address, use the elin command in voice emergency response
                              		  settings configuration mode. To remove the number, use the no form of this command.

elin number

no elin

### Syntax Description

number

An E.164 number to be used as the default ELIN.

### Command Default

No default ELIN number is created.

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

Use this command to specify an E.164 number to be the default ELIN if
                              		  the 911 caller’s IP phone address does not match the subnet of any location in
                              		  any ERL zone. The default ELIN can be an existing ELIN already defined in an
                              		  ERL or it can be unique.

## Examples

In this example, the ELIN (4085550101) defined in the voice emergency
                              		  response settings configuration is used if the 911 caller’s IP phone address
                              		  does not match any of the voice emergency response locations. After the 911
                              		  call is placed to the PSAP, the PSAP has 120 minutes to call back 408 555-0101
                              		  to reach the 911 caller. If the call history has expired (after 120 minutes),
                              		  any callback is routed to extension 7500.

```
voice emergency response settings
callback 7500
elin 4085550101
expiry 120
```

### Related Commands

Command

Description

callback

Default phone number to contact if a 911 callback cannot
                                          						find the last 911 caller from the ERL.

expiry

Number of minutes a 911 call is associated to an ELIN in
                                          						case of a callback from the 911 operator.

logging

Syslog informational message printed to the console each
                                          						time an emergency call is made.

voice emergency response settings

Creates a tag for identifying settings for E911 behavior.

## em external

To remove the login page under the Extension Mobility option from the
                              		  Services menu on IP phones in Cisco Unified CME, use the em external command in telephony-service
                              		  configuration mode. To return to default, use the no form of this command.

em external

no em external

### Syntax Description

This command has no keywords or arguments.

### Command Default

Login page for Extension Mobility is accessible under the Extension
                              		  Mobility option in the Services menu.

### Command Modes

Telephony-service configuration (config-telephony)

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

This command removes the Extension Mobility login page from the
                              		  Sevices menu on all IP phones registered in a Cisco Unified CME system on which
                              		  Extension Mobility is enabled.

## Examples

The following partial output shows the configuration for this
                              		  command:

```
router# show running-configuration .
.
.
telephony-service
 em external
 em logout 1:0 
 max-ephones 10
 max-dn 100
 ip source-address 10.0.0.1 port 2000
 url authentication http://10.0.0.1/CCMCIP/authenticate.asp  
 cnf-file location flash:
 cnf-file perphone
 max-conferences 8 gain -6
 transfer-system full-consult
 create cnf-files version-stamp Jan 01 2002 00:00:00
!
```

### Related Commands

Command

Description

ip http server

Enables the HTTP server on the Cisco Unified CME router
                                          						that hosts the service URL for the Extension Mobility Login and Logout page.

## em keep-history

To disable Automatic Clear Call History for Extension Mobility phones
                              		  in Cisco Unified CME, use the em keep-history command in telphony-service
                              		  configuration mode. To return to the default, use the no form of this command.

em keep-history

no em keep-history

### Syntax Description

This command has no arguments or keywords.

### Command Default

Call history record is automatically cleared when a user logs out
                              		  from an Extension Mobility phone.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Release

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

This command disables Automatic Clear Call History for Extension
                              		  Mobility phones in Cisco Unified CME.

In Cisco Unified CME 4.3 and later versions, the EM manager in Cisco
                              		  Unified CME sends commands to a phone to clear call history anytime a user is
                              		  logs out from Extension Mobility. Use this command in telephony-service
                              		  configuration mode to disable this feature at a system-level.

## Examples

The following example shows how to configure Extension Mobility in
                              		  Cisco Unified CME to keep, not clear, call histories after users log out from
                              		  Extension Mobility phones:

```
Router(config)# telephony-service Router(config-telephony)# em keep-history Router(config-telephony)#
```

## em logout

To configure up to three time-of-day based timers for automatically
                              		  logging out all Extension Mobility users, use the em logout command in telephony-service configuration
                              		  mode. To disable the timer, use the no form of this command.

em logout time1 [time2] [time3]

no command time1 [time2] [time3]

### Syntax Description

time

Time of day after which all users that are logged into
                                          						Extension Mobility are logged out from Extension Mobility. Range: 00:00 to
                                          						24:00 on a 24-hour clock.

### Command Default

No time-of-day timer is created for automatically logging out
                              		  Extension Mobility users.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Release

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

This command creates up to three time-of-day timers for automatically
                              		  logging out all Extension Mobility users. If an Extension Mobility user is
                              		  using the phone when automatic logout occurs, the user is logged out after the
                              		  active call is completed.

The call history record is automatically cleared when a user logs out
                              		  from an Extension Mobility phone. To disable Automatic Clear Call History on
                              		  all Extension Mobility phones, use the em keep-history command in telephony-service
                              		  configuration mode.

## Examples

The following example shows how to configure two time-of-day timers
                              		  to automatically log out all logged-on Extension Mobility users at 5:30 PM and
                              		  again at midnight each day:

```
Router(config)# telephony-service Router(config-telephony)# em logout 17:30 24:00 Router(config-telephony)#
```

### Related Commands

Command

Description

em keep-history

Disables Automatic Clear Call History for Extension
                                          						Mobility in Cisco Unified CME.

## emadmin login

To permit an external application to log into a Cisco Unified IP
                              		  phone that is enabled for Extension Mobility in Cisco Unified CME, use
                              		  the emadmin login command in privileged EXEC mode.

emadmin login name ephone-tag

### Syntax Description

name

Credential for Extension Mobility. This credential must be
                                          						already configured by using the user command in voice-user-profile
                                          						configuration mode.

ephone-tag

Unique identifier for IP phone that is enabled for
                                          						Extension Mobility. This tag must already be configured by using the ephone command.

### Command Default

External application cannot log into an Extension Mobility phone.

### Command Modes

Privileged EXEC (#)

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

This command enables an external application, such as a CSTA client
                              		  application, to log into an Extension Mobility phone.

Before using this command, configure a credential in Extension
                              		  Mobility by using the user command in voice-user-profile
                              		  configuration mode.

The IP phone to be accessed must be enabled for Extension Mobility.

The application remains logged into the phone until it is manually or
                              		  automatically logged out from the Extension Mobility phone

This command does not have a no form.

## Examples

The following example shows how to configure this command to log an
                              		  application into an Extension Mobility phone (2) using the “user204”
                              		  credential:

```
Router# login user204 2 Router#
```

### Related Commands

Command

Description

emadmin logout

Logs out an external application from Extension Mobility.

em logout

Creates up to three time-of-day timers for automatically
                                          						logging out all Extension Mobility users.

logout-profile

Enables an IP phone for Extension Mobility.

max-idle-time

Creates an idle-duration timer for automatically logging
                                          						out an Extension Mobility user.

user

Creates an authentication credential to be used by
                                          						Extension Mobility.

## emadmin logout

To manually log out an external application from Extension Mobility,
                              		  use the emadmin logout command in privileged EXEC mode. To return
                              		  to default, use the no form of this command.

emadmin logout name

no emadmin logout name

### Syntax Description

name

Already-configured credential in Extension Mobility user
                                          						profile.

### Command Default

Application remains logged into the Extension Mobility phone until
                              		  logged out.

### Command Modes

Privileged EXEC (#)

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

This command enables an external application, such as a CSTA client
                              		  application, to log out of an Extension Mobility phone.

## Examples

The following example shows how to configure this command to log out
                              		  an application that logged into an Extension Mobility phone using the “user204”
                              		  credential:

```
Router# logout user204 Router#
```

### Related Commands

Command

Description

user

Creates an authentication credential to be used by
                                          						Extension Mobility.

## emergency response callback

To define a dial peer that is used for 911 callbacks from the PSAP,
                              		  use the emergency response callback command in voice dial-peer configuration
                              		  mode. To remove the definition of the dial peer as an incoming link from the
                              		  PSAP, use the no form of this command.

emergency response callback

no emergency response callback

### Syntax Description

This command has no arguments or keywords.

### Command Default

The dial peer is not defined as an incoming link from the PSAP.

### Command Modes

Dial-peer configuration (config-dial-peer)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)T

Cisco Unified CME 4.1 Cisco Unified SRST 4.1 Cisco Unified
                                          						SIP SRST 4.1

This command was introduced. For Cisco Unified CME, this
                                          						command is supported in SRST fallback mode only.

12.4(15)XY

Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1)

This command was added for Cisco Unified CME.

12.4(20)T

Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

Use this command to define which dial peer is used for 911 callbacks
                              		  from the PSAP. You can define multiple dial peers with this command.

## Examples

The following example shows a dial peer defined as an incoming link
                              		  from the PSAP. If 408 555-0100 is configured as the ELIN for an ERL, this dial
                              		  peer recognizes that an incoming call from 408 555-0100 is a 911 callback.

```
dial-peer voice 100 pots
 incoming called-number 4085550100
 port 1/1:D
 direct-inward-dial
 emergency response callback
```

### Related Commands

Command

Description

emergency response location

Associates an ERL to either a SIP phone, ephone, or dial
                                          						peer.

emergency response zone

Defines a dial peer that is used by the system to route
                                          						emergency calls to the PSAP.

voice emergency response location

Creates a tag for identifying an ERL for the enhanced 911
                                          						service.

## emergency response location

To associate an emergency response location (ERL) for Enhanced 911
                              		  Services with a dial peer, ephone, ephone-template, voice register pool, or
                              		  voice register template, use the emergency response location command in dial peer, ephone,
                              		  ephone-template, voice register pool, or voice register template configuration
                              		  mode. To remove the association, use the no form of this command.

emergency response location tag

no emergency response location tag

### Syntax Description

tag

Unique number that identifies an existing ERL tag defined
                                          						by the voice emergency response location command.

### Command Default

No ERL tag is associated with a dial peer, ephone, ephone-template,
                              		  voice register pool, or voice register template.

### Command Modes

Dial-peer configuration (config-dial-peer) Ephone configuration (config-ephone) Ephone-template configuration (config-ephone-template) Voice register pool configuration (config-register-pool) Voice register template configuration (config-register-template)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)T

Cisco Unified CME 4.1 Cisco Unified SRST 4.1 Cisco Unified
                                          						SIP SRST 4.1

This command was introduced. For Cisco Unified CME, this
                                          						command is supported in SRST fallback mode only.

12.4(15)XY

Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1)

This command was added to Cisco Unified CME in the
                                          						ephone-template and voice register template configuration modes.

12.4(20)T

Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

Use this command to assign an ERL to phones individually. Depending
                              		  on the type of phones (endpoints) that you have, you can assign an ERL to a
                              		  phone’s:

- Dial-peer configuration

- Ephone

- Ephone-template

- Voice register pool

- Voice register template

These methods of associating a phone with an ERL are alternatives to
                              		  assigning a group of phones that are on the same subnet as an ERL.

The tag used by this command is an integer from 1 to 2147483647 and
                              		  refers to an existing ERL tag that is defined by the voice emergency response location command. If the tag does not refer to a
                              		  valid ERL configuration, the phone is not associated to an ERL. For Cisco
                              		  Unified IP phones, the IP address is used to find the inclusive ERL subnet. For
                              		  phones on a VoIP trunk or FXS/FXO trunk, the PSAP gets a reorder tone.

## Examples

The following example shows how to assign an ERL to a phone’s dial
                              		  peer:

```
dial-peer voice 12 pots
 emergency response location 18
```

The following example shows how to assign an ERL to a phone’s ephone:

```
ephone  41
 emergency response location 22
```

The following example shows how to assign an ERL to one or more SCCP
                              		  phones:

```
ephone-template 6
 emergency response location 8
```

The following example shows how to assign an ERL to a phone’s voice
                              		  register pool:

```
voice register pool 4
 emergency response location 21
```

The following example shows how to assign an ERL to one or more SIP
                              		  phones:

```
voice register template 4
 emergency response location 8
```

### Related Commands

Command

Description

emergency response callback

Defines a dial peer that is used for 911 callbacks from the
                                          						PSAP.

emergency response zone

Defines a dial peer that is used by the system to route
                                          						emergency calls to the PSAP.

voice emergency response location

Creates a tag for identifying an ERL for the enhanced 911
                                          						service.

## emergency response zone

To define a dial peer that is used by the system to route emergency
                              		  calls to a PSAP, use the emergency response zone command in voice dial-peer
                              		  configuration mode. To remove the definition of the dial peer as an outgoing
                              		  link to the PSAP, use the no form of this command.

emergency response zone zone-tag

no emergency response zone

### Syntax Description

zone-tag

Identifier (1-100) for the emergency response zone.

### Command Default

The dial peer is not defined as an outgoing link to the PSAP.
                              		  Therefore, E911 services are not enabled.

### Command Modes

Dial-peer configuration (config-dial-peer)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)T

Cisco Unified CME 4.1 Cisco Unified SRST 4.1 Cisco Unified
                                          						SIP SRST 4.1

This command was introduced. For Cisco Unified CME, this
                                          						command is supported in SRST fallback mode only.

12.4(15)XY

Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1)

The zone-tag argument was added and
                                          						this command was added for Cisco Unified CME.

12.4(20)T

Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

Use this command to specify that any calls using this dial peer are
                              		  processed by the E911 software. To enable any E911 processing, the emergency
                              		  response zone command must be enabled under a dial peer.

If no zone tag is specified, the system looks for a matching ELIN to
                              		  the E911 caller’s phone by searching each emergency response location that was configured using the emergency response location command.

If a zone tag is specified, the system looks for a matching ELIN
                              		  using sequential steps according to the contents of the configured zone. For
                              		  example, if the E911 caller’s phone has an explicit ERL assigned, the system
                              		  first looks for that ERL in the zone. If not found, it then searches each
                              		  location within the zone according to assigned priority numbers, and so on. If
                              		  all steps fail to find a matching ELIN, the default ELIN is assigned to the
                              		  E911 caller’s phone. If no default ELIN is configured, the E911 caller’s
                              		  automatic number identification (ANI) number is communicated to the Public
                              		  Safety Answering Point (PSAP).

This command can be defined in multiple dial peers. The zone tag
                              		  option allows only ERLs defined in that zone to be routed on this dial peer.
                              		  Also, this command allows callers dialing the same emergency number to be
                              		  routed to different voice interfaces based on the zone that includes their ERL.

## Examples

The following example shows a dial peer defined as an outgoing link
                              		  to the PSAP. Emergency response zone 10 is created and only calls from this
                              		  zone are routed through 1/0/0.

```
dial-peer voice 911 pots
	destination-pattern 9911
	prefix 911
	emergency response zone 10
	port 1/0/0
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

Creates a tag for identifying an ERL for E911 services.

voice emergency response zone

Creates an emergency response zone within which ERLs can be
                                          						grouped.

## encrypt password

To encrypt the password that is configured on Unified CME, use the encrypt password command in telephony-service configuration mode. To disable password encryption, use the no form of this command.

encrypt pasword

no encrypt password

### Syntax Description

This command has no arguments or keywords.

### Command Default

This command is enabled by default.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

Cisco IOS XE Gibraltar 16.11.1a Release

Unified CME 12.6

The command is introduced.

### Usage Guidelines

The CLI command encrypt password is enabled by default on Unified CME router. However, it is mandatory to configure key config-key password-encrypt [key] and password encryption aes along with encrypt password to support encryption on Unified CME router.

If the key used to encrypt the password is replaced with a new key (replace key or re-key), then the password is re-encrypted
                                          with the new key.

### Related Commands

Command

Description

password (auto-register)

Configuress the mandatory password for automatic registration of SIP phones with Unified CME.

## ephone

To enter Ethernet phone (ephone) configuration mode for an IP phone
                              		  for the purposes of creating and configuring an ephone, use the ephone command in global configuration mode.
                              		  To disable the ephone and remove the IP phone configuration, use the no form of this command.

ephone phone-tag

no ephone phone-tag

### Syntax Description

phone-tag

Unique sequence number that identifies an ephone during
                                          						configuration tasks. The maximum number is platform-dependent; refer to Cisco
                                          						IOS command-line interface (CLI) help.

### Command Default

No Cisco IP phone is configured.

### Command Modes

Global configuration (config)

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

Use the ephone command to enter ephone configuration mode. Use ephone
                              		  configuration mode to create and configure Cisco Unified IP phones in Cisco
                              		  Unified CME.

Before this command can be used for the first time, you must set the
                              		  maximum number of ephones using the max-ephones command in telephony-service
                              		  configuration mode. The maximum number of ephones varies by router platform and
                              		  software version.

## Examples

The following example enters ephone configuration mode for a phone
                              		  with the identifier 4 and assigns ephone-dn 1 to button 1:

```
Router(config)# ephone 4 Router(config-ephone)# button 1:1
```

### Related Commands

Command

Description

button

Assigns a button number to the Cisco IP phone directory
                                          						number.

ephone - dn

Enters ephone-dn configuration mode.

mac - address

Configures the MAC address of a Cisco IP phone.

max - ephones

Configures the maximum number of Cisco IP phones that can
                                          						be supported by a router.

restart (ephone)

Performs a fast reboot of a single phone associated with a
                                          						Cisco CME router.

restart all (telephony-service)

Performs a fast reboot of all phones associated with a
                                          						Cisco CME router.

## ephone-dn

To enter ephone-dn configuration mode to configure a directory number
                              		  for an IP phone line, intercom line, paging line, voice-mail port, or
                              		  message-waiting indicator (MWI), use the ephone-dn command in global configuration mode. To delete an ephone-dn, use the no form of this command.

ephone-dn dn-tag [ dual-line | octo-line ]

no ephone-dn dn-tag

### Syntax Description

dn-tag

Unique number that identifies an ephone-dn during
                                          						configuration tasks. Range is 1 to the number set by the max-dn command.

dual-line

(Optional) Enables two calls per directory number.

octo-line

(Optional) Enables eight calls per directory number.

### Command Default

No ephone-dn is configured.

### Command Modes

Global configuration (config)

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

The dual-line keyword was added.

12.3(4)T

Cisco CME 3.4

The dual-line keyword was integrated
                                          						into Cisco IOS Release 12.3(4)T.

12.4(15)XZ

Cisco Unified CME 4.3

The octo-line keyword was added.

12.4(20)T

Cisco Unified CME 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

Use this command to enter ephone-dn configuration mode to create
                              		  directory numbers. In ephone-dn configuration mode, you assign an extension
                              		  number using the number command, a name to appear in the local
                              		  directory using the name command, and other parameters using
                              		  various commands.

Before using the ephone-dn command, you must set the maximum
                              		  number of ephone-dns to support in your system by using the max-dn command. The maximum number of
                              		  ephone-dns that you can create depends on the software version, router
                              		  platform, and amount of memory that you have installed.

A dual-line ephone-dn has one virtual voice port and two channels to
                              		  handle two independent calls. This capacity allows call waiting, call transfer,
                              		  and conference functions within a single directory number. Dual-line mode is
                              		  supported on all phone types, but is not appropriate for voice-mail numbers,
                              		  intercoms, or ephone-dns used for message-waiting indicators, paging, loopback,
                              		  or hunt groups. Overlays of single-line hunt groups onto dual-line buttons are
                              		  supported.

An octo-line directory number supports up to eight active calls, both
                              		  incoming and outgoing, on a single phone button. Unlike a dual-line directory
                              		  number, which is shared exclusively among phones, an octo-line directory number
                              		  can split its channels among the phones sharing the directory number. All
                              		  phones sharing the octo-line directory number are allowed to initiate or
                              		  receive calls on the idle channels of the directory number.

Ephone-dns are created in single-line mode if the dual-line or octo-line keyword is not used. To change an
                              		  ephone-dn from one mode to another, for example from dual-line mode to
                              		  single-line mode, you must delete the ephone-dn and then re-create it.

## Examples

The following example shows how to create directory number 1 with
                              		  extension 5576:

```
Router(config)# ephone-dn 1 Router(config-ephone-dn)# number 5576
```

The following example shows an ephone-dn with the number 1001 in
                              		  dual-line mode. The no huntstop command allows calls to continue to hunt
                              		  to other ephone-dns if this one is busy or does not answer. The huntstop channel command disables call hunting to the
                              		  second channel of this ephone-dn if the first channel is busy or does not
                              		  answer.

```
Router(config)# ephone-dn 10 dual-line Router(config-ephone-dn)# number 1001 Router(config-ephone-dn)# no huntstop Router(config-ephone-dn)# huntstop channel
```

The following example shows an ephone-dn with the number 2001 in
                              		  octo-line mode. The huntstop channel command enables call hunting to up to six
                              		  channels of this ephone-dn. The remaining two channels are available for
                              		  outgoing calls or features such as call transfer, call waiting, and
                              		  conferencing.

```
Router(config)# ephone-dn 20 octo-line Router(config-ephone-dn)# number 2001 Router(config-ephone-dn)# huntstop channel 6
```

### Related Commands

Command

Description

huntstop (ephone-dn and ephone-dn-template)

Disables call hunting for directory numbers or channels.

max-dn

Sets the maximum number of ephone-dns that can be
                                          						configured.

name

Associates a name with an extension (ephone-dn).

number

Associates a telephone or extension number with a directory
                                          						number (ephone-dn).

## ephone-dn-template

To enter ephone-dn-template configuration mode and create an
                              		  ephone-dn template containing a standard set of ephone-dn features, use the ephone-dn-template command in global configuration mode. To delete an ephone-dn
                              		  template, use the no form of this command.

ephone-dn-template template-tag

no ephone-dn-template template-tag

### Syntax Description

template-tag

Identifier for this ephone-dn template. Range is from 1 to
                                          						15.

### Command Default

No ephone-dn template is created.

### Command Modes

Global configuration (config)

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

Use this command to create an ephone-dn template. An ephone-dn
                              		  template contains a set of ephone-dn attributes that you can easily apply to
                              		  one or more ephone-dns.

If you use an ephone-dn template to apply a command to an ephone-dn
                              		  and you also use the same command in ephone-dn configuration mode for the same
                              		  ephone-dn, the value that you set in ephone-dn configuration mode has priority.

Type ? in ephone-dn-template configuration
                              		  mode to see the commands that are available in this mode. The following example
                              		  shows CLI help for ephone-dn-template configuration mode:

```
Router(config-ephone-dn-template)# ? Ephone Dn template configuration commands:
  call-forward         Define E.164 telephone number for call forwarding
  call-waiting         Config call-waiting option
  caller-id            Configure port caller id parameters
  corlist              Class of Restriction on dial-peer for this dn
  default              Set a command to its defaults
  description          dn desc, for DN Qualified Display Name
  exit                 Exit from ephone-dn-template configuration mode
  hold-alert           Set Call On-Hold timeout alert parameters
  huntstop             Stop hunting on Dial-Peers
  mwi                  set message waiting indicator options (mwi)
  no                   Negate a command or set its defaults
  pickup-group         set the call pickup group number for the DN
  translate            Translation rule
  translation-profile  Translation profile
```

After creating an ephone-dn template, apply the template to one or
                              		  more ephone-dns using the ephone-dn-template command in ephone-dn
                              		  configuration mode. Even though you can define up to 15 different ephone
                              		  templates, you cannot apply more than one template to a particular ephone-dn.

If you try to apply a second ephone-dn template to an ephone-dn that
                              		  already has a template applied to it, the second template will overwrite the
                              		  first ephone-dn template configuration after you use the restart command to reboot the phone.

To view your ephone-dn-template configurations, use the show telephony-service ephone-dn-template command. To see which
                              		  ephone-dns have templates applied to them, use the show running-config command.

## Examples

The following example creates ephone-dn template 3, which sets call
                              		  forwarding on busy and no answer to forward calls to extension 4000 and sets
                              		  the pickup group to 4. Ephone-dn template 3 is then applied to ephone-dn 23 and
                              		  ephone-dn 33, which appear on ephones 13 and 14, respectively.

```
ephone-dn-template 3
 call-forwarding busy 4000
 call-forwarding noan 4000 timeout 30
 pickup group 4
ephone-dn 23
 number 2323
 ephone-dn-template 3
ephone-dn 33
 number 3333
 ephone-dn-template 3
ephone 13
 button 1:23
ephone 14
 button 1:33
```

### Related Commands

Command

Description

ephone-dn-template (ephone-dn)

Applies an ephone-dn template to an ephone-dn.

restart (ephone)

Performs a fast reboot of a single phone associated with a
                                          						Cisco Unified CME router.

restart (telephony-service)

Performs a fast reboot of one or all phones associated with
                                          						a Cisco Unified CME router.

show telephony-service ephone-dn-template

Displays ephone-dn-template configurations.

## ephone-dn-template (ephone-dn)

To apply an ephone-dn template to an ephone-dn, use the ephone-dn-template command in ephone-dn configuration mode. To remove the
                              		  ephone-dn template, use the no form of this command.

ephone-dn-template template-tag

no ephone-dn-template template-tag

### Syntax Description

template-tag

The template tag for a template created with the ephone-dn-template command in
                                          						global configuration mode. Range is from 1 to 15.

### Command Default

No ephone-dn template is applied to the ephone-dn.

### Command Modes

Ephone-dn configuration (config-ephone-template)

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

Use the ephone-dn-template command in ephone-dn
                              		  configuration mode to apply an ephone-dn template to an ephone. You cannot
                              		  apply more than one ephone-dn template to an ephone-dn.

If you try to apply a second ephone-dn template to an ephone-dn that
                              		  already has an ephone-dn template applied to it, the second template will
                              		  overwrite the first ephone-dn template configuration.

To view your ephone-dn-template configurations, use the show telephony-service ephone-dn-template command.

## Examples

The following example shows how to create ephone-dn template 3, which
                              		  sets call forwarding on busy and no answer to forward calls to extension 4000
                              		  and sets the pickup group to 4, and apply the template to ephone-dn 23 and
                              		  ephone-dn 33, which appear on ephones 13 and 14, respectively.

```
ephone-dn-template 3
 call-forwarding busy 4000
 call-forwarding noan 4000 timeout 30
 pickup group 4
ephone-dn 23
 number 2323
 ephone-dn-template 3
ephone-dn 33
 number 3333
 ephone-dn-template 3
ephone 13
 button 1:23
ephone 14
 button 1:33
```

### Related Commands

Command

Description

ephone-dn

Enters ephone-dn configuration mode.

ephone-dn-template

Creates an ephone-dn template and enters ephone-dn-template
                                          						configuration mode.

show telephony-service ephone-dn-template

Displays ephone-dn template configurations.

## ephone-hunt

To enter ephone-hunt configuration mode for the purposes of creating
                              		  and configuring a hunt group for use in a Cisco Unified CME system, use the ephone-hunt command in global configuration
                              		  mode. To delete a hunt group, use the no form of this command.

ephone-hunt hunt-tag { longest-idle | peer | sequential }

no ephone-hunt hunt-tag

### Syntax Description

hunt-tag

Unique sequence number that identifies the ephone hunt
                                          						group during configuration tasks. Range is from 1 to 100.

longest-idle

Hunt group in which calls go to the ephone-dn that has been
                                          						idle the longest.

peer

Hunt group in which the first extension to ring is the
                                          						number to the right (in the list) of the extension that was the last one to
                                          						ring when the hunt group was last called. Ringing proceeds in a circular
                                          						manner, left to right, for the number of hops specified when the ephone hunt
                                          						group is defined.

sequential

Hunt group in which extensions ring in the order in which
                                          						they are listed, left to right, when the hunt group is defined.

### Command Default

No hunt group is defined.

### Command Modes

Global configuration (config)

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

12.3(11)T

Cisco CME 3.2

The longest-idle keyword was added.

12.4(4)XC

Cisco Unified CME 4.0

The maximum number of hunt groups was increased from 10 to
                                          						100.

12.4(9)T

Cisco Unified CME 4.0

This command with the maximum number of hunt groups
                                          						increased to 100 was integrated into Cisco IOS Release 12.4(9)T.

### Usage Guidelines

Use the ephone-hunt command to enter ephone-hunt configuration mode. Use
                              		  ephone-hunt configuration mode to create ephone hunt groups in a Cisco Unified
                              		  CME system.

A hunt group is a list of phone numbers that are assigned to take
                              		  turns receiving incoming calls for one number, a pilot number that is defined
                              		  with the pilot command. The list of numbers in the
                              		  hunt group is defined using the list command. If a number in the list is busy
                              		  or does not answer, the call is redirected to the next number in the list. The
                              		  last number tried is the final number, which is defined using the final command.

The order in which the numbers are chosen can be longest-idle, peer,
                              		  or sequential.

- If the order is longest-idle, each hop is directed to the
                                 			 ephone-dn that has been idle the longest. Idle time is determined from the last
                                 			 time that a phone registered, reregistered, or went on-hook.

- If the order is peer, the first number to which calls are directed
                                 			 is the number to the right of the number in the list that was the last number
                                 			 to ring on the previous occasion that the hunt group was called. If that number
                                 			 is busy or does not answer, the call is directed to the next number in the list
                                 			 and, in the process, circles back to the beginning of the list. In peer hunt
                                 			 groups, the hops command specifies how many times a
                                 			 call can hop from number to number before going to the final number, after
                                 			 which the call is no longer forwarded.

- If the order is sequential, the first number to which calls are
                                 			 directed is always the first number in the list. If that number is busy or does
                                 			 not answer, the call is redirected to the next available number in the list,
                                 			 from left to right.

To configure a new hunt group, you must specify the longest-idle , peer , or sequential keyword. To change an existing ephone hunt group configuration,
                              		  the keyword is not required. To change the type of hunt group from peer to
                              		  sequential or sequential to peer, you must remove the existing hunt group first
                              		  using the no form of the command and then recreate it.

## Examples

The following example defines longest-idle ephone hunt group 1 with a
                              		  pilot number 7501, a final number 8000, and 11 numbers in the list. After a
                              		  call is redirected six times (makes six hops), it is redirected to the final
                              		  number 8000.

```
ephone-hunt 1 longest-idle 
 pilot 7501
 members logout 
 list 7001, 7002, 7023, 7028, 7045, 7062, 7067, 7072, 7079, 7085, 7099
 final 8000 
 preference 1 
 hops 6
 timeout 20 
 no-reg
```

The following example defines peer hunt group number 2. Callers dial
                              		  the pilot number 5610 to reach the hunt group. The first extension to ring the
                              		  first time that this hunt group is called is 5601. If 5601 does not answer, the
                              		  hunt proceeds from left to right, beginning with the extension directly to the
                              		  right of 5601, for four hops. If none of those extensions answers before the
                              		  hops limit is reached, the call is forwarded to extension 6000, which is the
                              		  number for the voice-mail service.

If extension 5601 answers the first call, then the second time
                              		  someone calls the hunt group, the first extension to ring is 5602. If this call
                              		  hops until extension 5617 answers it, then the third time someone calls the
                              		  hunt group, the first extension to ring is 5633. If extension 5633 does not
                              		  answer, the call is redirected to extension 5601, and so forth.

```
Router(config)# ephone-hunt 2 peer Router(config-ephone-hunt)# pilot 5610 Router(config-ephone-hunt)# members logout Router(config-ephone-hunt)# list 5601, 5602, 5617, 5633 Router(config-ephone-hunt)# final 6000 Router(config-ephone-hunt)# hops 4 Router(config-ephone-hunt)# preference 1 Router(config-ephone-hunt)# timeout 30 Router(config-ephone-hunt)# exit
```

The following example defines sequential hunt group number 1. When
                              		  callers dial extension 5601, the first phone to ring is 5001, then 5002, 5017,
                              		  and 5028. If none of those extensions answers, the call is forwarded to
                              		  extension 6000, which is the number for the voice-mail service.

```
Router(config)# ephone-hunt 1 sequential Router(config-ephone-hunt)# pilot 5601 Router(config-ephone-hunt)# members logout Router(config-ephone-hunt)# list 5001, 5002, 5017, 5028 Router(config-ephone-hunt)# final 6000 Router(config-ephone-hunt)# preference 1 Router(config-ephone-hunt)# timeout 30 Router(config-ephone-hunt)# exit
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

Defines the ephone-dns that participate in an ephone hunt
                                          						group.

max-redirect

Changes the current number of allowable redirects in a
                                          						Cisco Unified CME system.

members logout

Sets all static members initial state to logout.

The members logout command is rejected if configured
                                          						after the list command.

no-reg (ephone-hunt)

Specifies that the pilot number of this ephone hunt group
                                          						should not register with the H.323 gatekeeper.

pilot

Defines the ephone-dn that is dialed to reach an ephone
                                          						hunt group.

preference (ephone-hunt)

Sets preference order for the ephone-dn associated with an
                                          						ephone-hunt-group pilot number.

timeout (ephone-hunt)

Sets the number of seconds after which a call that is not
                                          						answered is redirected to the next number in the hunt-group list.

## ephone-hunt login

To authorize an ephone-dn to dynamically join and leave an ephone
                              		  hunt group, use the ephone-hunt login command in ephone-dn configuration mode. To
                              		  disable this capability, use the no form of this command.

ephone-hunt login

no ephone-hunt login

### Syntax Description

This command has no arguments or keywords.

### Command Default

An ephone-dn is not allowed to dynamically join and leave ephone hunt
                              		  groups.

### Command Modes

Ephone-dn configuration (config-ephone-dn)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)XC

Cisco Unified CME 4.0

This command was introduced.

12.4(9T

Cisco Unified CME 4.0

This command was integrated into Cisco IOS Release
                                          						12.4(9)T.

### Usage Guidelines

Use the show ephone-hunt command to display current hunt group
                              		  members, including those who joined the group dynamically.

## Examples

The following example creates five ephone-dns and a hunt group that
                              		  includes the first two ephone-dns and two wildcard slots. The last three
                              		  ephone-dns are enabled for group hunt dynamic membership. Each of them can join
                              		  and leave the hunt group whenever one of the slots is available.

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

show ephone-hunt

Displays ephone-hunt group configuration, current status,
                                          						and statistics.

## ephone-hunt statistics write-all

Effective with Cisco Unified CME 9.0, the ephone-hunt statistics write-all command is replaced by the hunt group statistics write-all command in privileged EXEC mode. For
                              		  more information, see the hunt group statistics write-all command.

To write ephone-hunt statistics information to a file, use the ephone-hunt statistics write-all command in privileged EXEC mode.

ephone-hunt statistics write-all location

### Syntax Description

location

The URL or filename to which the statistics should be
                                          						written.

### Command Modes

Privileged EXEC (#)

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

15.2(2)T

Cisco Unified CME 9.0

This command was replaced. See the hunt group statistics write-all command.

### Usage Guidelines

Use this command to write out, in hourly increments, all the ephone
                              		  hunt group statistics for the past seven days. This command is intended be used
                              		  when normal hunt group statistics collection is interrupted, perhaps due to
                              		  TFTP server failure. The commands that are normally used to provide hunt-group
                              		  statistics are hunt-group report delay hours , hunt-group report every hours , hunt-group report url , and statistics collect . These commands allow you to specify
                              		  shorter, more precise reporting periods and file-naming conventions.

## Examples

The following example writes the ephone hunt group statistics to a
                              		  file in flash called “huntstats.” See the hunt-group report url command for explanations of the output fields.

```
Router# ephone-hunt statistics write-all flash:huntstats Writing out all ephone hunt statistics to tftp now. 
11:13:58 UTC Fri Apr 29 2005,
,
01, Fri 11:00 - 12:00, HuntGp, 01, 01, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
01, Fri 12:00 - 13:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
01, Fri 13:00 - 14:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
01, Fri 14:00 - 15:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
01, Fri 15:00 - 16:00, HuntGp, 00, 00, 00000, 00000, 00000, 0000, 0000, 000000, 000000, 0000, 00000, 000000, 000000,
.
.
.
```

### Related Commands

Command

Description

hunt-group report delay hours

Delays hunt-group statistics collection for a specified
                                          						number of hours.

hunt-group report every hours

Sets the hourly interval at which Cisco Unified CME B-ACD
                                          						call statistics are automatically transferred to a file.

hunt-group report url

Sets filename parameters and the URL path where Cisco
                                          						Unified CME B-ACD call statistics are to be sent using TFTP.

show ephone-hunt

Displays ephone hunt group information.

show ephone-hunt statistics

Displays ephone hunt group statistics.

statistics collection

Enables the collection of call statistics for an ephone
                                          						hunt group.

## ephone-template

To create an ephone template to configure a set of phone features and
                              		  to enter ephone-template configuration mode, use the ephone-template command in global configuration mode. To delete an ephone
                              		  template, use the no form of this command.

ephone-template template-tag

no ephone-template template-tag

### Syntax Description

template-tag

Identifier for this ephone template. Range is from 1 to 20.

### Command Default

No ephone template is created.

### Command Modes

Global configuration (config)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(11)T

Cisco CME 3.2

This command was introduced.

12.4(4)XC

Cisco Unified CME 4.0

The maximum number of templates that can be created was
                                          						increased from 5 to 20.

12.4(9)T

Cisco Unified CME 4.0

The modification to increase the maximum number of
                                          						templates that can be created from 5 to 20 was integrated into Cisco IOS
                                          						Release 12.4(9)T.

### Usage Guidelines

Use this command to create an ephone template containing a set of
                              		  ephone commands. The template can then be easily applied to one or more
                              		  ephones.

If you use an ephone template to apply a command to a phone and you
                              		  also use the same command in ephone configuration mode for the same phone, the
                              		  value that you set in ephone configuration mode has priority.

Type ? in ephone-template configuration mode to
                              		  see the commands that are available in this mode and that can be included in an
                              		  ephone-template. The following example shows CLI help for ephone-template
                              		  configuration mode at the time that this document was written:

```
Router(config-ephone-template)# ? Ephone template configuration commands:
  after-hour        ephone exempt from after-hour blocking
  codec             Set preferred codec for calls with other phones on this
                    router
  default           Set a command to its defaults
  exit              Exit from ephone-template configuration mode
  fastdial          Define ip-phone fastdial number
  features          define features blocked
  keep-conference   Do not disconnect conference when conference initiator
                    hangs-up.Connect remaining parties together directly using
                    call transfer.
  keepalive         Define keepalive timeout period to unregister IP phone
  keyphone          Identify an IP phone as keyphone
  mtp               Always send media packets to this router
  network-locale    Select the network locale for this template.  
  night-service     Define night-service bell
  no                Negate a command or set its defaults
  paging-dn         set audio paging dn group for phone
  service           Service configuration in ephone template
  softkeys          define softkeys per state
  speed-dial        Define ip-phone speed-dial number
  transfer          transfer related configuration
  transfer-park     customized transfer to park configuration
  transfer-pattern  customized transfer-pattern configuration
  type              Define ip-phone type
  user-locale       Select the user locale for this template.
```

After creating an ephone template, apply the template to one or more
                              		  ephones using the ephone-template command in ephone
                              		  configuration mode. Even though you can define up to 20 different ephone
                              		  templates, you cannot apply more than one template to a particular ephone.

After applying a template to an ephone or removing a template from an
                              		  ephone, use the following commands:

- restart —Performs a fast reboot of the
                                 			 phone.

- create cnf-files —Rebuilds configuration files.

If you try to apply a second ephone template to an ephone that
                              		  already has an ephone template applied to it, the second template will
                              		  overwrite the first ephone template configuration after you use the restart command to reboot the phone.

To view your ephone-template configurations, use the show telephony-service ephone-template command. To see which ephones have
                              		  templates applied to them, use the show running-config command.

## Examples

The following example creates two ephone templates. The softkeys commands in ephone-template
                              		  configuration mode define what soft keys are displayed and their order.
                              		  Template 1 is applied to ephone 32, which has the extension 2555, and template
                              		  2 is applied to ephone 38, which has the extension 2666.

```
ephone-template 1 
 softkeys idle Dnd Redial Newcall Pickup Login 
 softkeys seized Redial Cfwdall Gpickup Pickup 
 softkeys alerting Callback Endcall
 softkeys connected Confrn Hold Endcall
ephone-template 2 
 softkeys idle Redial Pickup
 softkeys seized Redial Pickup 
 softkeys connected Hold Endcall
ephone-dn 25
 number 2555
ephone-dn 26
 number 2666
ephone 32
 button 1:25
 ephone-template 1
ephone 38
 button 1:26
 ephone-template 2
```

The following example creates an ephone template to block the use of
                              		  Park and Trnsfer soft keys. It is applied to extension 2333.

```
ephone-template 15
 features blocked Park Trnsfer
ephone-dn 2
 number 2333
ephone 3
 button 1:2
 ephone-template 15
```

### Related Commands

Command

Description

create cnf-files

Builds phone configuration files.

ephone-template (ephone)

Applies an ephone template to an ephone.

restart (ephone)

Performs a fast reboot of a single phone associated with a
                                          						Cisco Unified CME router.

restart (telephony-service)

Performs a fast reboot of one or all phones associated with
                                          						a Cisco Unified CME router.

show telephony-service ephone-template

Displays ephone-template configurations.

## ephone-template (ephone)

To apply an ephone template to a particular SCCP phone in Cisco
                              		  Unified CME, use the ephone-template command in ephone configuration mode. To remove the ephone
                              		  template, use the no form of this command.

ephone-template template-tag

no ephone-template template-tag

### Syntax Description

template-tag

Unique identifier for a template created by using the ephone-template command in global
                                          						configuration mode. Range is 1 to 20.

### Command Default

No ephone template is applied to a phone.

### Command Modes

Ephone configuration (config-ephone)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(11)T

Cisco CME 3.2

This command was introduced.

12.4(4)XC

Cisco Unified 4.0

The maximum number of ephone templates that can be created
                                          						was increased from 5 to 20.

12.4(9)T

Cisco Unified 4.0

This command with an increased range for the template-tag argument was
                                          						integrated into Cisco IOS Release 12.4(9)T.

12.4(15)XZ

Cisco Unified CME 4.3

This command was modified to specify that before an ephone
                                          						template can be applied to a particular phone, the Mac address for that phone
                                          						must be present in its configuration file.

12.4(20)T

Cisco Unified CME 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

This command in ephone configuration mode applies an ephone template
                              		  to a particular phone.

In Cisco Unified CME 4.3 and later versions, an ephone template
                              		  cannot be applied to a particular phone unless its configuration file includes
                              		  its MAC address. If you attempt to apply a template to a phone for which the
                              		  MAC address in not configured, a message appears. To configure the MAC address
                              		  for a Cisco Unified IP phone, use the mac-address command in ephone configuration mode.

After applying an ephone template, use the restart command to perform a fast reboot of
                              		  the phone.

You cannot apply more than one ephone template at a time to any
                              		  phone. If you attempt to apply a second ephone template to phone to which an
                              		  ephone template is already applied, the second template will overwrite the
                              		  first ephone template configuration after you reboot the phone.

If you use an ephone template to apply a command to a phone and you
                              		  also use the same command in ephone configuration mode for the same phone, the
                              		  value set in ephone configuration mode has priority over the value set in
                              		  ephone-template configuration mode.

To view your ephone-template configurations, use the show telephony-service ephone-template command.

## Examples

The following example defines ephone templates 1 and 2 and applies
                              		  ephone template 1 to ephones 1 through 3 and ephone template 2 to ephone 4.

```
ephone-template 1 
 softkeys idle Dnd Redial Newcall Pickup Login 
 softkeys seized Redial Cfwdall Gpickup Pickup 
 softkeys alerting Callback Endcall
 softkeys connected Confrn Hold Endcall
 softkeys hold Newcall Resume
ephone-template 2 
 softkeys idle Redial Pickup
 softkeys seized Redial Pickup 
 softkeys alerting Endcall
 softkeys connected Hold Endcall
 softkeys hold Resume
 ephone 1
 ephone-template 1
ephone 2
 ephone-template 1
 ephone 3
 ephone-template 1
ephone 4
 ephone-template 2
ephone 5
 ephone-template 2
The following example creates an ephone template to block the use of Park and Transfer soft keys on extension 2333.
ephone-template 15
 features blocked Park Trnsfer
ephone-dn 2
 number 2333
ephone 3
 button 1:2
 ephone-template 15
```

### Related Commands

Command

Description

ephone-template

Creates an ephone-template and enters ephone-template
                                          						configuration mode.

mac-address

Associates the MAC address of a Cisco Unified IP phone with
                                          						an ephone configuration in Cisco Unified CME.

restart (ephone)

Performs a fast reboot of a single phone in Cisco Unified
                                          						CME.

restart (telephony-service)

Performs a fast reboot of one or all phones in Cisco
                                          						Unified CME.

show telephony-service ephone-template

Displays ephone-template configurations.

## ephone-type

To add a Cisco Unified IP phone type by defining an ephone-type
                              		  template, use the ephone-type command in global configuration
                              		  mode. To remove an ephone type, use the no form of this command.

ephone-type phone-type [ addon ]

no ephone-type phone-type

### Syntax Description

phone-type

Unique label that identifies the type of phone. Value is
                                          						any alphanumeric string up to 32 characters.

addon

(Optional) Phone type is an add-on module, such as the
                                          						Cisco Unified IP Phone 7915 Expansion Module.

### Command Default

Ephone type is not defined.

### Command Modes

Global configuration (config)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)XZ

Cisco Unified CME 4.3 Cisco Unifieid SRST 4.3

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0 Cisco Unifieid SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

This command adds a user-defined template for a phone type to a Cisco
                              		  Unified CME system. This configuration template defines a set of attributes
                              		  that describe the features of the new phone type. Use this command to add phone
                              		  types that are not already defined in the system.

If you use a phone-type argument that matches a system-defined phone
                              		  type, a message displays notifying you that the ephone-type is built-in and
                              		  cannot be changed. For a list of system-defined phone types, see the type command.

Use the create cnf-files command for the new phone type to take
                              		  effect.

## Examples

The following example shows the Nokia E61 added with an ephone-type
                              		  template, which is then assigned to ephone 2:

```
ephone-type  E61
 device-id 376
 device-name E61 Mobile Phone
 num-buttons 1
 max-presentation 1
 no utf8
 no phoneload
!
!
telephony-service
 load E61 SCCP61.8-2-2SR2S
 max-ephones 100
 max-dn 240
 ip source-address 15.7.0.1 port 2000
 cnf-file location flash:
 cnf-file perphone
 voicemail 8900
 max-conferences 8 gain -6
 transfer-system full-consult
 create cnf-files version-stamp 7960 Sep 25 2007 21:25:47
!
!
ephone  2
 mac-address 001C.821C.ED23
 type E61
 button  1:2
```

### Related Commands

Command

Description

create cnf-files

Builds the eXtensible Markup Language (XML) configuration
                                          						files that are required for IP phones.

device-id

Specifies the device ID for a phone type in an ephone-type
                                          						template.

device-name

Assigns a name to a phone type in an ephone-type template.

load

Associates a type of Cisco Unified IP phone with a phone
                                          						firmware file.

type

Assigns a phone type to an SCCP phone.

## exclude

To exclude the availability of local services on a phone’s user
                              		  interface such as, Extension Mobility (EM), My Phone Apps, and Local Directory
                              		  from the phone’s configuration, use the exclude command in ephone or
                              		  ephone-template mode.

exclude [ em | myphoneapp | directory | call-history ]

### Syntax Description

em

Extension mobility (EM) service.

myphoneapp

My Phone Apps service.

directory

Local directory service

call-history

Call history in the missed, received, or placed calls
                                          						directory

### Command Default

Local services are enabled.

### Command Modes

Ephone configuration (config-ephone) Ephone-template configuration (config-ephone-template)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.1(3)T

Cisco Unified CME 8.5

This command was introduced.

15.1(4)M

Cisco Unified CME 8.6

This command was modified. Call-history option was added.

### Usage Guidelines

Use this command to exclude the availability of local services such
                              		  as, EM, my phone apps, and local directory services from the phone
                              		  configuration.

## Examples

The following example shows directory and my phone apps excluded from
                              		  ephone-template 8:

```
Router# conf t
Router#config)#ephone-template 8
Router(config-ephone-template)#exclude ?
  directory   local directory service
  em          extension mobility service
  myphoneapp  my phone apps service
  <cr>
Router(config-ephone-template)#exclude directory
Router(config-ephone-template)#exclude myphoneapp!
```

The following example shows call-history as excluded from ephone 10:

```
!
telephony-service
 max-ephones 40
 max-dn 100
 max-conferences 8 gain -6
 transfer-system full-consult
!
!
ephone-template  5
 exclude call-history
!
!
ephone  10
 exclude call-history
 device-security-mode none
!
```

### Related Commands

Command

Description

ephone-template (ephone)

Applies template to an ephone.

show telephony-service ephone-template

Displays ephone-template configurations.

## exclude (voice register)

To exclude from the Cisco Unified SIP IP phone’s user interface the
                              		  availability of local services such as Extension Mobility (EM), My Phone Apps,
                              		  and Local Directory, use the exclude command in voice register pool or
                              		  voice register template configuration mode.

exclude [ em | myphoneapps | directory ]

### Syntax Description

em

Extension Mobility service is excluded.

myphoneapps

My Phone Apps service is excluded.

directory

Local Directory service is excluded.

### Command Default

Local services are enabled.

### Command Modes

Voice register pool configuration (config-register-pool)

Voice register template configuration (config-register-temp)

## Command History

Release

Modification

15.2(2)T

This command was introduced.

## Examples

The following example shows the Local Directory and My Phone Apps
                              		  services excluded from voice register pool 33:

```
Router(config)# voice register pool 33 Router(config-register-pool)# exclude directory Router(config-register-pool)# exclude myphoneapps
```

### Related Commands

Command

Description

voice register pool

Enters voice register pool configuration mode and creates a
                                          						pool configuration for Cisco Unified SIP IP phones in Cisco Unified CME.

voice register template

Enters voice register template configuration mode and
                                          						defines a template of common parameters for Cisco Unified SIP IP phones.

## expiry

To set the time after which emergency callback history expires, use
                              		  the expiry command in voice emergency response
                              		  settings configuration mode. To remove the number, use the no form of this command.

expiry time

no expiry

### Syntax Description

time

Identifier (2-2880) in minutes for the maximum time the 911
                                          						caller history is available for callback.

### Command Default

The default expiry time is 180 minutes.

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

Use this command to specify the amount of time (in minutes) to keep
                              		  emergency caller history for each ELIN. The time can be an integer in the range
                              		  of 2 to 2880 minutes. The default value is 180 minutes.

## Examples

In this example, the ELIN (4085550101) defined in the voice emergency
                              		  response settings configuration is used if the 911 caller’s IP phone address
                              		  does not match any of the voice emergency response locations. After the 911
                              		  call is placed to the PSAP, the PSAP has 120 minutes to call back 408 555-0101
                              		  to reach the 911 caller. If the call history has expired (after 120 minutes),
                              		  any callback is routed to extension 7500.

```
voice emergency response settings
callback 7500
elin 4085550101
expiry 120
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

logging

Syslog informational message printed to the console every
                                          						time an emergency call is made.

voice emergency response settings

Creates a tag for identifying settings for E911 behavior.

## extension-assigner tag-type

To enable provision tags for identifying ephone configurations when
                              		  using the extension assigner application, use the extension-assigner tag-type command in telephony-service
                              		  configuration mode. To return to the default setting of using the ephone tag,
                              		  use the no form of this command.

extension-assigner tag-type { ephone-tag | provision-tag }

no extension-assigner tag-type

### Syntax Description

ephone-tag

Ephone tags must be used to identify ephone configurations.

provision-tag

Provision tags must be used to identify ephone
                                          						configurations.

### Command Default

Ephone tags are used to identify ephone configurations for the
                              		  extension assigner application.

### Command Modes

Telephony-service configuration (config-telephony)

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

This command enables you to use provision tags for identifying ephone
                              		  configurations to be assigned by the extension application application.

A provision tag is an unique number other than an ephone tag, such as
                              		  a jack number or an extension number, for identifying the ephone configuration
                              		  to be assigned to a particular IP phone by the extension assigner application.

Use this command to specify which type of tag, ephone tag or
                              		  provision tag, is to be used to identify ephone configurations for the
                              		  extension assigner application. The default configuration is ephone tag.

If you use this command with the provision-tag keyword , use the provision-tag command to create provision tags.

## Examples

The following example shows that this command is configured to enable
                              		  provision tags to be used for identifying the ephone configurations to be
                              		  assigned by the extension assigner application. Note that provision tag 1001 is
                              		  configured for ephone 1. During phone installation, the installation technician
                              		  can press 1001 on the telephone keypad to assign the ephone 1 configuration,
                              		  with extension number 1001 on button 1, to the IP phone being installed.

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

### Related Commands

Command

Description

provision-tag

Creates a provision tag for identifying an ephone
                                          						configuration.

## extension-range

To define a range of extension numbers for a specific MOH group in
                              		  Cisco Unified CME or Cisco Unified SRST, use the extension-range command in voice-moh-group configuration mode. To define a
                              		  range of extension numbers for a specific directory number in Cisco Unified
                              		  CME, use the extension-range command in ephone-dn
                              		  configuration mode. To disable the extension-range command, use the no form of this command.

extension-range starting-extension to ending-extension

no extension-range starting-extension to ending-extension

### Syntax Description

starting-extension

Hexadecimal digits (0-9 or A-F) that define the starting
                                          						extension number in an extension range. Maximum length: 32 digits.

ending-extension

Hexadecimal digits (0-9 or A-F) that define the last
                                          						extension number in an extension range. Value of the ending extension must be
                                          						larger than value of the starting extension. Maximum length: 32 digits.

### Command Default

No extension- range is configured.

### Command Modes

Voice MOH group configuration (config-voice-moh-group) Ephone-dn configuration (config-ephone-dn)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.0(1)XA

Cisco Unified CME 8.0 Cisco Unified SRST 8.0

This command was introduced.

15.1(1)T

Cisco Unified CME 8.0 Cisco Unified SRST 8.0

This command was integrated into Cisco IOS Release
                                          						15.1(1)T.

### Usage Guidelines

This command configured in voice moh-group configuration mode
                              		  identifies MOH clients calling extension numbers specified under the extension
                              		  range configured for a MOH group in Cisco Unified CME or Cisco Unified SRST.
                              		  This command in ephone-dn configuration mode identifies MOH clients calling
                              		  extension numbers specified under the extension range configured for a
                              		  directory number in Cisco Unified CME

You can define multiple extension-ranges in the same MOH group or
                              		  directory number.

The extension can be expressed in hexadecimal digits ranging from 0-9
                              		  or A-F and should not exceed the limit of 32 digits.

The starting-extension and ending-extension numbers must contain the
                              		  same number of digits.

The ending extension number must be of a greater value than the
                              		  starting extension number.

Extension-range for a MOH group must not overlap with any other
                              		  extension-range configured in any other MOH group.

## Examples

The following example shows two extension ranges configured under
                              		  voice moh-group 1:

```
Router(config)# voice moh-group 1
Router(config-voice-moh-group)# moh flash:/minuet.wav Router(config-voice-moh-group)# description Marketing
Router(cconfig-voice-moh-group)# extension range 1000 to 1999 Router(config-voice-moh-group)# extension range 3000 to 3999
```

### Related Commands

Command

Description

moh

Enables music on hold from an audio file.

voice-moh-group

Enters voice moh-group configuration mode.

## external-ring (voice register global)

To specify the type of ring sound used on Cisco Session Initiation
                              		  Protocol (SIP) or Cisco SCCP IP phones for external calls, use the external-ring command in voice register global configuration mode. To return
                              		  to the default ring sound, use the no form of this command.

external-ring { bellcore-dr1 | bellcore-dr2 | bellcore-dr3 | bellcore-dr4 | bellcore-dr5 }

no external-ring

### Syntax Description

bellcore-dr1 bellcore-dr2 bellcore-dr3 bellcore-dr4 bellcore-dr5

Standard distinctive ringing patterns as defined in the
                                          						standard GR-506-CORE, LSSGR: Signaling for Analog Interfaces .

### Command Default

The default ring sound is an internal ring pattern.

### Command Modes

Voice register global configuration (config-register-global)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was introduced.

### Usage Guidelines

When set, this command defines varying ring tones so that you can
                              		  discriminate between internal and external calls from Cisco SIP or Cisco SCCP
                              		  IP phones.

## Examples

The following example shows how to specify that Bellcore DR1 be used
                              		  for external ringing on Cisco SIP IP phones:

```
Router(config)# voice register global Router(config-register-global)# external-ring bellcore-dr1
```

| { 1 \| 2 } | Number index. |
|---|---|---|
| number | PSTN number that replaces a 911 caller’s extension. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)T | Cisco Unified CME 4.1 Cisco Unified SRST 4.1 Cisco Unified
                                          						SIP SRST 4.1 | This command was introduced. For Cisco Unified CME, this
                                          						command is supported in SRST fallback mode only. |
| 12.4(15)XY | Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1) | This command was added for Cisco Unified CME. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| subnet | Defines which IP phones are part of this ERL. |

| number | An E.164 number to be used as the default ELIN. |
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
| callback | Default phone number to contact if a 911 callback cannot
                                          						find the last 911 caller from the ERL. |
| expiry | Number of minutes a 911 call is associated to an ELIN in
                                          						case of a callback from the 911 operator. |
| logging | Syslog informational message printed to the console each
                                          						time an emergency call is made. |
| voice emergency response settings | Creates a tag for identifying settings for E911 behavior. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| ip http server | Enables the HTTP server on the Cisco Unified CME router
                                          						that hosts the service URL for the Extension Mobility Login and Logout page. |

| Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| time | Time of day after which all users that are logged into
                                          						Extension Mobility are logged out from Extension Mobility. Range: 00:00 to
                                          						24:00 on a 24-hour clock. |
|---|---|

| Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| em keep-history | Disables Automatic Clear Call History for Extension
                                          						Mobility in Cisco Unified CME. |

| name | Credential for Extension Mobility. This credential must be
                                          						already configured by using the user command in voice-user-profile
                                          						configuration mode. |
|---|---|
| ephone-tag | Unique identifier for IP phone that is enabled for
                                          						Extension Mobility. This tag must already be configured by using the ephone command. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| emadmin logout | Logs out an external application from Extension Mobility. |
| em logout | Creates up to three time-of-day timers for automatically
                                          						logging out all Extension Mobility users. |
| logout-profile | Enables an IP phone for Extension Mobility. |
| max-idle-time | Creates an idle-duration timer for automatically logging
                                          						out an Extension Mobility user. |
| user | Creates an authentication credential to be used by
                                          						Extension Mobility. |

| name | Already-configured credential in Extension Mobility user
                                          						profile. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| user | Creates an authentication credential to be used by
                                          						Extension Mobility. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)T | Cisco Unified CME 4.1 Cisco Unified SRST 4.1 Cisco Unified
                                          						SIP SRST 4.1 | This command was introduced. For Cisco Unified CME, this
                                          						command is supported in SRST fallback mode only. |
| 12.4(15)XY | Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1) | This command was added for Cisco Unified CME. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| emergency response location | Associates an ERL to either a SIP phone, ephone, or dial
                                          						peer. |
| emergency response zone | Defines a dial peer that is used by the system to route
                                          						emergency calls to the PSAP. |
| voice emergency response location | Creates a tag for identifying an ERL for the enhanced 911
                                          						service. |

| tag | Unique number that identifies an existing ERL tag defined
                                          						by the voice emergency response location command. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)T | Cisco Unified CME 4.1 Cisco Unified SRST 4.1 Cisco Unified
                                          						SIP SRST 4.1 | This command was introduced. For Cisco Unified CME, this
                                          						command is supported in SRST fallback mode only. |
| 12.4(15)XY | Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1) | This command was added to Cisco Unified CME in the
                                          						ephone-template and voice register template configuration modes. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Note | The ephone-template and voice register template modes are not for
                                       		  Cisco Unified SRST or Cisco Unified SIP SRST. Voice register pool mode is not
                                       		  available for Cisco Unified SRST. |
|---|---|

| Command | Description |
|---|---|
| emergency response callback | Defines a dial peer that is used for 911 callbacks from the
                                          						PSAP. |
| emergency response zone | Defines a dial peer that is used by the system to route
                                          						emergency calls to the PSAP. |
| voice emergency response location | Creates a tag for identifying an ERL for the enhanced 911
                                          						service. |

| zone-tag | Identifier (1-100) for the emergency response zone. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)T | Cisco Unified CME 4.1 Cisco Unified SRST 4.1 Cisco Unified
                                          						SIP SRST 4.1 | This command was introduced. For Cisco Unified CME, this
                                          						command is supported in SRST fallback mode only. |
| 12.4(15)XY | Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1) | The zone-tag argument was added and
                                          						this command was added for Cisco Unified CME. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 Cisco Unified
                                          						SIP SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| emergency response callback | Defines a dial peer that is used for 911 callbacks from the
                                          						PSAP. |
| emergency response location | Associates an ERL to either a SIP phone, ephone, or dial
                                          						peer. |
| voice emergency response location | Creates a tag for identifying an ERL for E911 services. |
| voice emergency response zone | Creates an emergency response zone within which ERLs can be
                                          						grouped. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| Cisco IOS XE Gibraltar 16.11.1a Release | Unified CME 12.6 | The command is introduced. |

| Note | If the key used to encrypt the password is replaced with a new key (replace key or re-key), then the password is re-encrypted
                                          with the new key. |
|---|---|

| Command | Description |
|---|---|
| password (auto-register) | Configuress the mandatory password for automatic registration of SIP phones with Unified CME. |

| phone-tag | Unique sequence number that identifies an ephone during
                                          						configuration tasks. The maximum number is platform-dependent; refer to Cisco
                                          						IOS command-line interface (CLI) help. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco ITS 1.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |

| Command | Description |
|---|---|
| button | Assigns a button number to the Cisco IP phone directory
                                          						number. |
| ephone - dn | Enters ephone-dn configuration mode. |
| mac - address | Configures the MAC address of a Cisco IP phone. |
| max - ephones | Configures the maximum number of Cisco IP phones that can
                                          						be supported by a router. |
| restart (ephone) | Performs a fast reboot of a single phone associated with a
                                          						Cisco CME router. |
| restart all (telephony-service) | Performs a fast reboot of all phones associated with a
                                          						Cisco CME router. |

| dn-tag | Unique number that identifies an ephone-dn during
                                          						configuration tasks. Range is 1 to the number set by the max-dn command. |
|---|---|
| dual-line | (Optional) Enables two calls per directory number. |
| octo-line | (Optional) Enables eight calls per directory number. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco ITS 1.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |
| 12.2(15)ZJ | Cisco CME 3.0 | The dual-line keyword was added. |
| 12.3(4)T | Cisco CME 3.4 | The dual-line keyword was integrated
                                          						into Cisco IOS Release 12.3(4)T. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | The octo-line keyword was added. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| huntstop (ephone-dn and ephone-dn-template) | Disables call hunting for directory numbers or channels. |
| max-dn | Sets the maximum number of ephone-dns that can be
                                          						configured. |
| name | Associates a name with an extension (ephone-dn). |
| number | Associates a telephone or extension number with a directory
                                          						number (ephone-dn). |

| template-tag | Identifier for this ephone-dn template. Range is from 1 to
                                          						15. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| Command | Description |
|---|---|
| ephone-dn-template (ephone-dn) | Applies an ephone-dn template to an ephone-dn. |
| restart (ephone) | Performs a fast reboot of a single phone associated with a
                                          						Cisco Unified CME router. |
| restart (telephony-service) | Performs a fast reboot of one or all phones associated with
                                          						a Cisco Unified CME router. |
| show telephony-service ephone-dn-template | Displays ephone-dn-template configurations. |

| template-tag | The template tag for a template created with the ephone-dn-template command in
                                          						global configuration mode. Range is from 1 to 15. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| Command | Description |
|---|---|
| ephone-dn | Enters ephone-dn configuration mode. |
| ephone-dn-template | Creates an ephone-dn template and enters ephone-dn-template
                                          						configuration mode. |
| show telephony-service ephone-dn-template | Displays ephone-dn template configurations. |

| hunt-tag | Unique sequence number that identifies the ephone hunt
                                          						group during configuration tasks. Range is from 1 to 100. |
|---|---|
| longest-idle | Hunt group in which calls go to the ephone-dn that has been
                                          						idle the longest. |
| peer | Hunt group in which the first extension to ring is the
                                          						number to the right (in the list) of the extension that was the last one to
                                          						ring when the hunt group was last called. Ringing proceeds in a circular
                                          						manner, left to right, for the number of hops specified when the ephone hunt
                                          						group is defined. |
| sequential | Hunt group in which extensions ring in the order in which
                                          						they are listed, left to right, when the hunt group is defined. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.3(11)T | Cisco CME 3.2 | The longest-idle keyword was added. |
| 12.4(4)XC | Cisco Unified CME 4.0 | The maximum number of hunt groups was increased from 10 to
                                          						100. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command with the maximum number of hunt groups
                                          						increased to 100 was integrated into Cisco IOS Release 12.4(9)T. |

| Note | If the number of times that a call is redirected to a new number
                                       		  exceeds five, the max-redirect command must be used to increase
                                       		  the allowable number of redirects in the Cisco Unified CME system. |
|---|---|

| Command | Description |
|---|---|
| final | Defines the last ephone-dn in an ephone hunt group. |
| hops | Defines the number of times that a call is redirected to
                                          						the next ephone-dn in a peer ephone-hunt-group list before proceeding to the
                                          						final ephone-dn. |
| list | Defines the ephone-dns that participate in an ephone hunt
                                          						group. |
| max-redirect | Changes the current number of allowable redirects in a
                                          						Cisco Unified CME system. |
| members logout | Sets all static members initial state to logout. The members logout command is rejected if configured
                                          						after the list command. |
| no-reg (ephone-hunt) | Specifies that the pilot number of this ephone hunt group
                                          						should not register with the H.323 gatekeeper. |
| pilot | Defines the ephone-dn that is dialed to reach an ephone
                                          						hunt group. |
| preference (ephone-hunt) | Sets preference order for the ephone-dn associated with an
                                          						ephone-hunt-group pilot number. |
| timeout (ephone-hunt) | Sets the number of seconds after which a call that is not
                                          						answered is redirected to the next number in the hunt-group list. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| Command | Description |
|---|---|
| show ephone-hunt | Displays ephone-hunt group configuration, current status,
                                          						and statistics. |

| location | The URL or filename to which the statistics should be
                                          						written. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |
| 15.2(2)T | Cisco Unified CME 9.0 | This command was replaced. See the hunt group statistics write-all command. |

| Note | Each year on the day that daylight saving time adjusts the time
                                       		  back by one hour at 2 a.m., the original 1 a.m. to 2 a.m. statistics for that
                                       		  day are lost because they are overwritten by the new 1 a.m. to 2 a.m.
                                       		  statistics. |
|---|---|

| Command | Description |
|---|---|
| hunt-group report delay hours | Delays hunt-group statistics collection for a specified
                                          						number of hours. |
| hunt-group report every hours | Sets the hourly interval at which Cisco Unified CME B-ACD
                                          						call statistics are automatically transferred to a file. |
| hunt-group report url | Sets filename parameters and the URL path where Cisco
                                          						Unified CME B-ACD call statistics are to be sent using TFTP. |
| show ephone-hunt | Displays ephone hunt group information. |
| show ephone-hunt statistics | Displays ephone hunt group statistics. |
| statistics collection | Enables the collection of call statistics for an ephone
                                          						hunt group. |

| template-tag | Identifier for this ephone template. Range is from 1 to 20. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(11)T | Cisco CME 3.2 | This command was introduced. |
| 12.4(4)XC | Cisco Unified CME 4.0 | The maximum number of templates that can be created was
                                          						increased from 5 to 20. |
| 12.4(9)T | Cisco Unified CME 4.0 | The modification to increase the maximum number of
                                          						templates that can be created from 5 to 20 was integrated into Cisco IOS
                                          						Release 12.4(9)T. |

| Command | Description |
|---|---|
| create cnf-files | Builds phone configuration files. |
| ephone-template (ephone) | Applies an ephone template to an ephone. |
| restart (ephone) | Performs a fast reboot of a single phone associated with a
                                          						Cisco Unified CME router. |
| restart (telephony-service) | Performs a fast reboot of one or all phones associated with
                                          						a Cisco Unified CME router. |
| show telephony-service ephone-template | Displays ephone-template configurations. |

| template-tag | Unique identifier for a template created by using the ephone-template command in global
                                          						configuration mode. Range is 1 to 20. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(11)T | Cisco CME 3.2 | This command was introduced. |
| 12.4(4)XC | Cisco Unified 4.0 | The maximum number of ephone templates that can be created
                                          						was increased from 5 to 20. |
| 12.4(9)T | Cisco Unified 4.0 | This command with an increased range for the template-tag argument was
                                          						integrated into Cisco IOS Release 12.4(9)T. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was modified to specify that before an ephone
                                          						template can be applied to a particular phone, the Mac address for that phone
                                          						must be present in its configuration file. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| ephone-template | Creates an ephone-template and enters ephone-template
                                          						configuration mode. |
| mac-address | Associates the MAC address of a Cisco Unified IP phone with
                                          						an ephone configuration in Cisco Unified CME. |
| restart (ephone) | Performs a fast reboot of a single phone in Cisco Unified
                                          						CME. |
| restart (telephony-service) | Performs a fast reboot of one or all phones in Cisco
                                          						Unified CME. |
| show telephony-service ephone-template | Displays ephone-template configurations. |

| phone-type | Unique label that identifies the type of phone. Value is
                                          						any alphanumeric string up to 32 characters. |
|---|---|
| addon | (Optional) Phone type is an add-on module, such as the
                                          						Cisco Unified IP Phone 7915 Expansion Module. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco Unified CME 4.3 Cisco Unifieid SRST 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unifieid SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| create cnf-files | Builds the eXtensible Markup Language (XML) configuration
                                          						files that are required for IP phones. |
| device-id | Specifies the device ID for a phone type in an ephone-type
                                          						template. |
| device-name | Assigns a name to a phone type in an ephone-type template. |
| load | Associates a type of Cisco Unified IP phone with a phone
                                          						firmware file. |
| type | Assigns a phone type to an SCCP phone. |

| em | Extension mobility (EM) service. |
|---|---|
| myphoneapp | My Phone Apps service. |
| directory | Local directory service |
| call-history | Call history in the missed, received, or placed calls
                                          						directory |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(3)T | Cisco Unified CME 8.5 | This command was introduced. |
| 15.1(4)M | Cisco Unified CME 8.6 | This command was modified. Call-history option was added. |

| Command | Description |
|---|---|
| ephone-template (ephone) | Applies template to an ephone. |
| show telephony-service ephone-template | Displays ephone-template configurations. |

| em | Extension Mobility service is excluded. |
|---|---|
| myphoneapps | My Phone Apps service is excluded. |
| directory | Local Directory service is excluded. |

| Release | Modification |
|---|---|
| 15.2(2)T | This command was introduced. |

| Command | Description |
|---|---|
| voice register pool | Enters voice register pool configuration mode and creates a
                                          						pool configuration for Cisco Unified SIP IP phones in Cisco Unified CME. |
| voice register template | Enters voice register template configuration mode and
                                          						defines a template of common parameters for Cisco Unified SIP IP phones. |

| time | Identifier (2-2880) in minutes for the maximum time the 911
                                          						caller history is available for callback. |
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
| callback | Default phone number to contact if a 911 callback cannot
                                          						find the last 911 caller from the ERL. |
| elin | E.164 number used as the default ELIN if no matching ERL to
                                          						the 911 caller’s IP phone address is found. |
| logging | Syslog informational message printed to the console every
                                          						time an emergency call is made. |
| voice emergency response settings | Creates a tag for identifying settings for E911 behavior. |

| ephone-tag | Ephone tags must be used to identify ephone configurations. |
|---|---|
| provision-tag | Provision tags must be used to identify ephone
                                          						configurations. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC4 | Cisco Unified CME 4.0(3) | This command was introduced. |
| 12.4(11)XJ | Cisco Unified CME 4.1 | This command was introduced. |
| 12.4(15)T | Cisco Unified CME 4.1 | This command was integrated into Cisco IOS Release
                                          						12.4(15)T. |

| Command | Description |
|---|---|
| provision-tag | Creates a provision tag for identifying an ephone
                                          						configuration. |

| starting-extension | Hexadecimal digits (0-9 or A-F) that define the starting
                                          						extension number in an extension range. Maximum length: 32 digits. |
|---|---|
| ending-extension | Hexadecimal digits (0-9 or A-F) that define the last
                                          						extension number in an extension range. Value of the ending extension must be
                                          						larger than value of the starting extension. Maximum length: 32 digits. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 Cisco Unified SRST 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 Cisco Unified SRST 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Note | If an extension range is defined in a MOH group and it is also
                                       		  defined under ephone-dn, the extension range defined under ephone-dn takes
                                       		  precedence. |
|---|---|

| Command | Description |
|---|---|
| moh | Enables music on hold from an audio file. |
| voice-moh-group | Enters voice moh-group configuration mode. |

| bellcore-dr1 bellcore-dr2 bellcore-dr3 bellcore-dr4 bellcore-dr5 | Standard distinctive ringing patterns as defined in the
                                          						standard GR-506-CORE, LSSGR: Signaling for Analog Interfaces . |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was introduced. |