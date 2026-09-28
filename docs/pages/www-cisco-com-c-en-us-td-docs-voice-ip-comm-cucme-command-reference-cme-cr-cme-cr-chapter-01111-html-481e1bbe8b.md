---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-command-reference-cme-cr-cme-cr-chapter-01111-html-481e1bbe8b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/command/reference/cme_cr/cme_cr_chapter_01111.html
retrieved_at: 2026-08-21T22:56:57.140810+00:00
---

Cisco Unified Communications Manager Express Command Reference

# Cisco Unified Communications Manager Express Command Reference

Updated: July 19, 2018

Chapter: Cisco Unified CME Commands: R

## Chapter: Cisco Unified CME Commands: R

# Cisco Unified CME Commands: R

## refer target dial-peer

To populate the Refer To portion of a SIP Refer message with the
                              		  address from the dial peer for the directory number being configured, use the refer target dial-peer command in voice register dn configuration mode. To return to
                              		  the default, use the no form of this command.

refer target dial-peer

no refer target

### Syntax Description

This command has no arguments or keywords.

### Command Default

Call is transferred to the destination as specified in the SIP Refer
                              		  message.

### Command Modes

Voice register dn configuration (config-register-dn)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(11)XW2

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

Use this command in voice register dn configuration mode to specify
                              		  that the destination address for this directory number be the dial peer. If
                              		  this command is not configured, Cisco IOS software will transfer the call to
                              		  the destination in the SIP Refer message and if that destination address is
                              		  Cisco Unified CME, call SIP will send out and route back to CME before sending
                              		  to the directory number, creating two extra call legs.

The following partial output from the show working-configuration command shows the
                              		  configuration for three directory numbers. This configuration will populate the
                              		  Refer To portion of the SIP Refer message with the address from the dial peer
                              		  for each of the directory numbers.

```
voice register dn  1
 session-server 1
 number 8999
 allow watch
 refer target dial-peer
!
voice register dn  2
 session-server 1
 number 8001
 allow watch
 refer target dial-peer
!
voice register dn  3
 session-server 1
 number 8101
 allow watch
 refer target dial-peer
```

## refer-ood enable

To enable out-of-dialog refer (OOD-R) processing, use the refer-ood enable command SIP user-agent configuration mode.
                              		  To disable OOD-R, use the no form of this command.

refer-ood enable [request-limit]

no refer-ood enable

### Syntax Description

request-limit

(Optional) Maximum number of concurrent incoming OOD-R
                                          						requests that the router can process. Range: 1 to 500. Default: 500.

### Command Default

OOD-R processing is disabled.

### Command Modes

SIP UA configuration (config-sip-ua)

## Command History

Release

Cisco product

Modification

12.4(11)XJ

Cisco Unified CME 4.1

This command was introduced.

12.4(15)T

Cisco Unified CME 4.1

This command was integrated into Cisco IOS Release
                                          						12.4(15)T.

### Usage Guidelines

Out of dialog Refer allows applications to establish calls using the
                              		  SIP gateway or Cisco Unified CME. The application sets up the call and the user
                              		  does not dial out from their own phone.

## Examples

The following example shows how to enable OOD-R:

```
Router(config)# sip-ua Router(config-sip-ua)# refer-ood enable
```

### Related Commands

Description

authenticate (voice register global)

Defines the authenticate mode for SIP phones in a Cisco
                                          						Unified CME or Cisco Unified SRST system.

credential load

Reloads a credential file into flash memory.

debug voip application

Displays all application debug messages.

## reference-pooltype

To inherit the
                              		  properties from the nearest supported phone model for a Cisco Unified SIP IP
                              		  phone on Cisco Unified CME, use the reference-pooltype command in voice register
                              		  pooltype mode. To remove the pool- type configuration, use the no form of
                              		  this command.

reference- pooltype phone-type

no reference- pooltype phone-type

## Syntax Description

Unique
                                       					 number that represents the phone model.

### Command Default

There is no
                              		  reference phone to inherit the properties. This is the only command which has
                              		  the no form as the default form.

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
                              		  to inherit the properties from the nearest supported phone model for a Cisco
                              		  Unified SIP IP phone on Cisco Unified CME.

## Examples

The following
                              		  example shows how to enter voice register pool configuration mode and inherit
                              		  the properties from the nearest supported phone model SIP phones on a Cisco
                              		  Unified CME system:

```
Router# configure terminal Router(config)# voice register pool-type 9900 Router(config--register-pool-type)# reference-pooltype 9971
```

### Related Commands

Command

Description

Adds a new Cisco Unified SIP IP phone to Cisco Unified CME.

## regenerate (ctl-client)

To create a new CTLFile.tlv file after making changes to the CTL
                              		  client configuration, use the regenerate command in CTL-client
                              		  configuration mode. The no form of this command has no effect in the
                              		  configuration.

regenerate

no regenerate

### Syntax Description

This command has no arguments or keywords.

### Command Default

A new CTLFile.tlv file is not created until this command is used.

### Command Modes

CTL-client configuration (config-ctl-client)

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

The following example gives the instruction to regenerate the CTL file
                              		  with the current information.

```
Router(config)# ctl-client Router(config-ctl-client)# server capf 10.2.2.2 trustpoint capftrust Router(config-ctl-client)# server cme 10.2.2.3 trustpoint cmetp Router(config-ctl-client)# server tftp 10.2.2.4 trustpoint tftptp Router(config-ctl-client)# sast1 trustpoint sast1tp Router(config-ctl-client)# sast2 trustpoint sast2tp Router(config-ctl-client)# regenerate
```

## register-id

To create an ID for explicitly identifying an external feature server
                              		  during Register requests, use the register-id command in voice register session-server configuration mode. To
                              		  remove an ID, use the no form of this command.

register-id name

no register-id name

### Syntax Description

name

String of up to 30 alphanumeric characters.

### Command Default

No identifier is created.

### Command Modes

Voice register session-server configuration (config-register-fs)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(11)XW2

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

Use this command to create an ID for identifying a route point during
                              		  Register requests. Cisco Unified CME challenges and authenticates the initial
                              		  keepalive Register request and issues a system-wide unique Cisco-referenceID to
                              		  be included in the response to the Register request from this route point.

## Examples

The following partial output shows the configuration of a session
                              		  manager for an external feature server, including the register ID of CSR1:

```
router# show running-configuration !
!
voice register session-server 1
 register-id CSR1
 keepalive 360
```

### Related Commands

Command

Description

keepalive

Duration for registration after which the registration
                                          						expires unless the feature server reregisters before the registration expiry.

## registrar server (SIP)

To enable SIP registrar functionality, use the registrar server command in SIP configuration mode. To
                              		  disable SIP registrar functionality, use the no form of the command.

registrar server [ expires [ max sec ] [ min sec ]]

no registrar server

### Syntax Description

expires

(Optional) Sets the active time for an incoming
                                          						registration.

max sec

(Optional) Maximum expires time for a registration, in
                                          						seconds. The range is from 600 to 86400. The default is 3600.

min sec

(Optional) Minimum expires time for a registration, in
                                          						seconds. The range is from 60 to 3600. The default is 60.

### Command Default

SIP registrar functionality on the Cisco Unified CME router id
                              		  disabled.

### Command Modes

SIP configuration (config-voi-sip)

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

Cisco CME 3.4 and Cisco SIP SRST 3.4

This command was added to Cisco CME.

### Usage Guidelines

When this command is entered, the router accepts incoming SIP
                              		  Register messages. If SIP Register message requests are for a shorter
                              		  expiration time than what is set with this command, the SIP Register message
                              		  expiration time is used.

This command is mandatory for Cisco Unified SIP SRST or Cisco Unified
                              		  CME and must be entered before any voice register pool or voice register global commands are configured.

If the WAN is down and you reboot your Cisco Unified CME or Cisco
                              		  Unified SIP SRST router, when the router reloads it will have no database of
                              		  SIP phone registrations. The SIP phones will have to register again, which
                              		  could take several minutes, because SIP phones do not use a keepalive
                              		  functionality. To shorten the time before the phones re-register, the
                              		  registration expiry can be adjusted with this command. The default expiry is
                              		  3600 seconds; an expiry of 600 seconds is recommended.

## Examples

The following partial sample output from the show running-config command shows that SIP registrar
                              		  functionality is set:

```
voice service voip
 allow-connections sip-to-sip
 sip
  registrar server expires max 1200 min 300
```

### Related Commands

Description

sip

Enters SIP configuration mode from voice service VoIP
                                          						configuration mode.

voice register global

Enters voice register global configuration mode in order to
                                          						set global parameters for all supported Cisco SIP phones in a Cisco Unified CME
                                          						or Cisco Unified SIP SRST environment.

voice register pool

Enters voice register pool configuration mode for SIP
                                          						phones.

## reset (ephone)

To perform a complete reboot of a single phone associated with a
                              		  Cisco CallManager Express (Cisco CME) router, use the reset command in ephone configuration mode.

reset

### Syntax Description

This command has no arguments or keywords.

### Command Default

No reset is performed.

### Command Modes

Ephone configuration (config-ephone)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.1(5)YD

Cisco ITS 1.0

This command was introduced

12.2(8)T

Cisco ITS 2.0

This command was integrated into Cisco IOS Release 12.2(8)T

### Usage Guidelines

After you update information for one or more phones associated with a
                              		  Cisco CME router, the phone or phones must be rebooted. There are two commands
                              		  to reboot the phones: reset and restart. The reset command performs a “hard” reboot
                              		  similar to a power-off-power-on sequence. It reboots the phone and contacts the
                              		  Dynamic Host Configuration Protocol (DHCP) server and the TFTP server to update
                              		  from their information as well. The restart command performs a “soft” reboot by
                              		  simply rebooting the phone without contacting the DHCP and TFTP servers. The reset command takes significantly longer to
                              		  process than the restart command when you are updating
                              		  multiple phones, but it must be used after updating phone firmware, user
                              		  locale, network locale, or URL parameters. For simple button, line, or
                              		  speed-dial changes, you can use the restart command.

Use the reset (ephone) command to perform a complete reboot of an IP phone
                              		  when you are in ephone configuration mode. This command has the same effect as
                              		  a reset (telephony-service) command that is used to reset a single
                              		  phone.

This command has a no form, but the no form has no effect.

## Examples

The following example resets the SCCP phone with a phone-tag of 1:

```
Router(config)# ephone 1 Router(config-ephone)# reset
```

### Related Commands

Description

reset (telephony-service)

Performs a complete reboot of one or all phones associated
                                          						with a Cisco CME router.

restart (ephone)

Performs a fast reboot of a single phone associated with a
                                          						Cisco CME router.

restart (telephony-service)

Performs a fast reboot of one or all phones associated with
                                          						a Cisco CME router.

## reset (telephony-service)

To perform a complete reboot of one or all phones associated with a
                              		  Cisco CallManager Express (Cisco CME) router, use the reset command in telephony-service
                              		  configuration mode. To interrupt and cancel a sequential reset cycle, use the no form of the command with the sequence-all keyword.

reset { all [time-interval] | cancel | mac-address | sequence-all }

no reset { all [time-interval] | cancel | mac-address | sequence-all }

### Syntax Description

all

Resets all Cisco IP phones served by the Cisco CME router.
                                          						The router pauses for 15 seconds between the reset starts for each successive
                                          						phone unless the time-interval argument is used to change that value.

time-interval

(Optional) Time interval, in seconds, between each phone
                                          						reset. Range is from 0 to 60. Default is 15.

cancel

Interrupts a sequential reset cycle that was started with a reset sequence-all command.

mac-address

MAC address of a particular Cisco IP phone.

sequence-all

Resets all phones in strict one-at-a-time order by waiting
                                          						for one phone to reregister before starting the reset for the next phone. The
                                          						sequencing of resets prevents possible conflicts between phones trying to
                                          						access TFTP services simultaneously. There is a reset timeout of 4 minutes,
                                          						after which the router stops waiting for the currently registering phone to
                                          						complete registration and starts to reset the next phone.

### Command Default

No reset is performed.

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

The time-interval range maximum was increased from 15 to 60 and the
                                          						default was changed from 0 to 15.

12.2(11)YT1

Cisco ITS 2.1

The cancel and sequence-all keywords were
                                          						introduced.

12.2(15)T

Cisco ITS 2.1

This command was integrated into Cisco IOS Release
                                          						12.2(15)T.

### Usage Guidelines

After you update information for one or more phones associated with a
                              		  Cisco CME router, the phone or phones must be rebooted using either the reset command or the restart command . The reset command performs a “hard” reboot similar to a
                              		  power-off-power-on sequence and contacts the Dynamic Host Configuration
                              		  Protocol (DHCP) server and the TFTP server for updated information as well. The restart command performs a “soft” reboot by
                              		  simply rebooting the phone without contacting the DHCP and TFTP servers. The reset command takes significantly longer to
                              		  process than the restart command when you are updating
                              		  multiple phones, but it must be used after you make changes to phone firmware,
                              		  user locale, network locale, or URL parameters. For simple button, line, or
                              		  speed-dial changes, you can use the restart command.

When you use the reset command, the default time interval of
                              		  15 seconds is recommended so that phone reset operations are staggered in order
                              		  to avoid all phones attempting to access router system resources at the same
                              		  time. A shorter interval may be used on systems with only a small number of
                              		  phones or for cases where a simple reset of the phones is desired that does not
                              		  result in the phones downloading updates to the phone firmware (using the
                              		  router’s TFTP service).

When you use the reset sequence-all command, the router waits for one
                              		  phone to complete its reset and reregister before starting to reset the next
                              		  phone. The delay provided by this command prevents multiple phones from
                              		  attempting to access the TFTP server simultaneously and therefore failing to
                              		  reset properly. Each reset operation can take several minutes when you use this
                              		  command. There is a reset timeout of 4 minutes, after which the router stops
                              		  waiting for the currently registering phone to complete registration and starts
                              		  to reset the next phone.

If the router configuration is changed so that the eXtensible Markup
                              		  Language (XML) configuration files for the phones are modified (changes are
                              		  made to user locale, network locale, or phone firmware), then whenever you use
                              		  the reset all or restart all command, the router automatically executes the r eset sequence-all command instead. The reset sequence-all command resets phones one at a time
                              		  in order to prevent multiple phones from trying to contact the TFTP server
                              		  simultaneously. This one-at-a-time sequencing can take a long time if there are
                              		  many phones. To avoid this automatic behavior, use the reset all time-interval or the restart all time-interval with an explicit argument that is not equal to the default
                              		  15-second time interval; for example, set a time interval of 14 seconds. If a reset sequence-all command has been started in error,
                              		  use the reset cancel command to interrupt and cancel the
                              		  sequence of resets.

The restart command allows the system to perform
                              		  quick phone resets in which only the button template, line information, and
                              		  speed-dial information is updated. See the documentation for the restart command for more information.

The no form of this command has an effect only
                              		  when used with the all or sequence-all keyword, when it interrupts and cancels the sequential
                              		  resetting of phones.

## Examples

The following example resets all IP phones served by the Cisco CME
                              		  router:

```
Router(config)# telephony-service Router(config-telephony)# reset all
```

The following example resets the Cisco IP phone with the MAC address
                              		  CFBA.321B.96FA:

```
Router(config)# telephony-service Router(config-telephony)# reset CFBA.321B.96FA
```

The following example resets all IP phones in sequential,
                              		  not-overlapping order:

```
Router(config)# telephony-service Router(config-telephony)# reset sequence-all
```

### Related Commands

Description

reset (ephone)

Performs a complete reboot of a single phone associated
                                          						with a Cisco CME router.

restart (ephone)

Performs a fast reboot of a single phone associated with a
                                          						Cisco CME router.

restart (telephony-service)

Performs a fast reboot of one or all phones associated with
                                          						a Cisco CME router.

telephony-service

Enters telephony-service configuration mode.

## reset (voice logout-profile and voice user-profile)

To perform a complete reboot of all IP phones on which a particular
                              		  extension-mobility profile is downloaded, use the reset command in voice logout-profile
                              		  configuration mode or voice user-profile configuration mode.

reset

### Syntax Description

This command has no arguments or keywords.

### Command Default

No reset is performed.

### Command Modes

Voice logout-profile configuration (voice-logout-profile) Voice user-profile configuration (voice-user-profile)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(11)XW2

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

Use this command to perform a “hard” reboot similar to a
                              		  power-off-power-on sequence, which includes downloading updated information
                              		  from the Dynamic Host Configuration Protocol (DHCP) server and the TFTP server.

Configure this command in voice logout-profile configuration mode
                              		  after creating or modifying a logout profile for extension mobility.

Configure this command in voice user-profile configuration mode after
                              		  creating or modifying an individual user’s profile for extension mobility.

This command has a no form, but the no form has no effect.

## Examples

The following example shows how to modify a logout profile by adding
                              		  speed-dial definitions and then reset all IP phones on which this logout
                              		  profile is downloaded to propagate the modification:

```
Router# configure terminal Router(config)# voice logout-profile 12 Router(config-user-profile)# speed-dial 1 3001 Router(config-user-profile)# speed-dial 2 3002 blf Router (config-logout-profile)# reset Router (config-logout-profile)# exit Router(config)#
```

## reset (voice register global)

To perform a complete reboot of all SIP phones associated with a
                              		  Cisco CallManager Express (Cisco CME) router, use the reset command in voice register global
                              		  configuration mode.

reset

### Syntax Description

This command has no arguments or keywords.

### Command Default

No reset is performed.

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

After you update information for one or more SIP phones associated
                              		  with a Cisco CME router, reboot the phones by using the reset command. The reset command performs a “hard” reboot
                              		  similar to a power-off-power-on sequence and contacts the Dynamic Host
                              		  Configuration Protocol (DHCP) server and the TFTP server for updated
                              		  information as well. Configure the reset command after you make changes to phone
                              		  firmware, user locale, network locale, or URL parameters.

The time interval between each phone reset is 15 seconds, thereby
                              		  avoiding an attempt by all phones to access router system resources at the same
                              		  time.

This command has a no form, but the no form has no effect.

## Examples

The following example shows how to reset all SIP phones served by the
                              		  Cisco CME router:

```
Router(config)# voice register global Router(config-register-global)# reset
```

### Related Commands

Description

reset (voice register pool)

Performs a complete reboot of a single SIP phone associated
                                          						with a Cisco CME router.

## reset (voice register pool)

To perform a complete reboot of a specific SIP phone associated with
                              		  a Cisco CallManager Express (Cisco CME) router, use the reset command in voice register pool
                              		  configuration mode. To interrupt a reset cycle, use the no form of this command.

reset

no reset

### Syntax Description

This command has no arguments or keywords.

### Command Default

No reset is performed.

### Command Modes

Voice register pool configuration (config-register-pool)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4

This command was introduced.

### Usage Guidelines

After you update information for one or more phones associated with a
                              		  Cisco CME router, the phones must be rebooted by using the reset command. The reset command performs a “hard” reboot
                              		  similar to a power-off-power-on sequence and contacts the Dynamic Host
                              		  Configuration Protocol (DHCP) server and the TFTP server for updated
                              		  information as well. Configure the reset command after you make changes to phone
                              		  firmware, user locale, network locale, or URL parameters.

Use this command to perform a complete reboot of an individual SIP
                              		  phone when you are in voice register pool configuration mode. To reset all SIP
                              		  phones, use the reset (voice register global) command.

This command has a no form, but the no form has no effect.

## Examples

The following example shows how to reset SIP phone 1 served by the
                              		  Cisco CME router:

```
Router(config)# voice register pool 1 Router(config-register-pool)# reset
```

### Related Commands

Description

reset (voice register global)

Performs a complete reboot of all SIP phones associated
                                          						with a Cisco CME router.

## reset (voice-gateway)

To perform a complete reboot of all analog phones associated with the
                              		  voice gateway and registered to Cisco Unified CME, use the reset command in voice-gateway configuration
                              		  mode.

reset

### Syntax Description

This command has no arguments or keywords.

### Command Default

No reset is performed.

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

After you update information for one or more analog phones associated
                              		  with the voice gateway, reboot the phones by using the reset command. The reset command performs a “hard” reboot
                              		  similar to a power-off-power-on sequence and contacts the Dynamic Host
                              		  Configuration Protocol (DHCP) server and the TFTP server for updated
                              		  information. Use the reset command after you make changes to phone
                              		  firmware, user or network locales, or URL parameters.

The time interval between each phone reset is 15 seconds, to avoid an
                              		  attempt by all phones to access system resources at the same time.

This command has a no form, but the no form has no effect.

## Examples

The following example shows how to reset all analog phones associated
                              		  with the voice gateway:

```
Router(config)# voice-gateway system 1 Router(config-voice-gateway)# reset
```

### Related Commands

Command

Description

restart (voice-gateway)

Performs a fast restart of all analog endpoints associated
                                          						with the voice gateway.

## reset tapi

To reset the connection between a Telephony Application Programmer's
                              		  Interface (TAPI) application and a particular SCCP phone in Cisco Unified CME,
                              		  use the reset tapi command in ephone configuration mode.

reset tapi

### Syntax Description

This command has no arguments or keywords.

### Command Default

No reset of the connection between the TAPI application and the
                              		  router is performed.

### Command Modes

Ephone configuration (config-ephone)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(20)YA

Cisco Unified CME 7.0(1)

This command was introduced.

12.4(22)T

Cisco Unified CME 7.0(1)

This command was integrated into Cisco IOS Release
                                          						12.4(22)T.

### Usage Guidelines

This command in ephone configuration mode resets the connection
                              		  between a TAPI application and a particular SCCP phone. This command does not
                              		  reset the Ethernet phone.

To disassociate and reestablish the connection without using this
                              		  command, you must reboot the router.

This command has a no form, but the no form has no effect.

## Examples

The following example shows how to reset the connection between a
                              		  TAPI application and the SCCP phone associated with the ephone-tag of 1:

```
Router(config)# ephone 1 Router(config-ephone)# reset tapi
```

## restart (ephone)

To perform a fast reboot of an IP phone associated with a Cisco
                              		  CallManager Express (Cisco CME) router, use the restart command in ephone configuration mode. To cancel the reboot, use
                              		  the no form of this command.

restart

no restart

### Syntax Description

This command has no arguments or keywords.

### Command Default

No restart is performed.

### Command Modes

Ephone configuration (config-ephone)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(11)YT1

Cisco ITS 2.1

This command was introduced.

12.2(15)T

Cisco ITS 2.1

This command was integrated into Cisco IOS Release
                                          						12.2(15)T.

### Usage Guidelines

This command causes the system to perform a fast phone reboot in
                              		  which only the button template, lines, and speed-dial numbers are updated on
                              		  the phone. For updates related to phone firmware, user locale, network locale,
                              		  or URL parameters, use the reset command . The restart command is much faster than the reset command because the phone does not need
                              		  to access the DHCP or TFTP server.

To restart all phones in a Cisco CME system for quick changes to
                              		  buttons, lines, and speed-dial numbers, use the restart command in telephony-service configuration mode.

This command has a no form, but the no form has no effect.

## Examples

The following example restarts the phone with phone-tag 1:

```
Router(config)# ephone 1 Router(config-ephone)# restart
```

### Related Commands

Description

reset (ephone)

Performs a complete reboot of a Cisco IP phone associated
                                          						with a Cisco CME router.

reset (telephony-service)

Performs a complete reboot of one or all phones associated
                                          						with a Cisco CME router.

restart (telephony-service)

Performs a fast reboot of one or all phones associated with
                                          						a Cisco CME router.

## restart (telephony-service)

To perform a fast reboot of one or all phones associated with a Cisco
                              		  CallManager Express (Cisco CME) router, use the restart command in telephony-service configuration mode. To cancel the
                              		  reboot, use the no form of this command.

restart { all [time-interval] | mac-address }

no restart { all [time-interval] | mac-address }

### Syntax Description

all

Restarts all phones associated with the Cisco CME router.

time-interval

(Optional) Time between each phone restart, in seconds.
                                          						Range is from 0 to 60. Default is 15.

mac-address

MAC address of the phone to be restarted.

### Command Default

Time-interval is 15 seconds.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(11)YT1

Cisco ITS 2.1

This command was introduced.

12.2(15)T

Cisco ITS 2.1

This command was integrated into Cisco IOS Release
                                          						12.2(15)T.

### Usage Guidelines

This command causes the system to perform a fast phone reset in which
                              		  only the button template, lines, and speed-dial numbers are updated on the
                              		  phone. For updates related to phone firmware, user locale, network locale, or
                              		  URL parameters, use the reset command.

Use the restart command to reboot IP phones after quick changes to buttons,
                              		  lines, and speed-dial numbers. This command is much faster than the reset command because the phone does not
                              		  access the DHCP or TFTP server.

To restart a single phone, use the restart c ommand with the mac-address argument or use the restart command in ephone configuration mode.

If the router configuration is changed so that the eXtensible Markup
                              		  Language (XML) configuration files for the phones are modified (changes are
                              		  made to user locale, network locale, or phone firmware), then whenever you use
                              		  the reset all or restart all command, the router automatically executes
                              		  the reset sequence-all command instead. The reset sequence-all command resets phones one at a time
                              		  in order to prevent multiple phones trying to contact the TFTP server
                              		  simultaneously. This one-at-a-time sequencing can take a long time if there are
                              		  many phones. To avoid this automatic behavior, use the reset all time-interva l command or the restart all time-interval command with an
                              		  explicit argument that is not equal to the default 15-second time interval; for
                              		  example, set a time interval of 14 seconds. If a reset sequence-all command has been started in error,
                              		  use the reset cancel command to interrupt and cancel the
                              		  sequence of resets.

The no form of this command has an effect only
                              		  when used with the all keyword, when it interrupts and cancels
                              		  the sequential restarting of phones.

## Examples

The following example performs a quick restart of all phones in a
                              		  Cisco CME system:

```
Router(config)# telephony-service Router(config-telephony)# restart all
```

### Related Commands

Description

reset (ephone)

Performs a complete reboot of a Cisco IP phone associated
                                          						with a Cisco CME router.

reset (telephony-service)

Performs a complete reboot of one or all phones associated
                                          						with a Cisco CME router.

restart (ephone)

Performs a fast reboot of a single phone associated with a
                                          						Cisco CME router.

## restart (voice register)

To perform a fast reset of one or all SIP phones associated with a
                              		  Cisco Unified CME router, use the restart command in voice register global or voice register pool
                              		  configuration mode. To cancel the reboot, use the no form of this command.

restart

no restart

### Syntax Description

This command has no arguments or keywords.

### Command Default

SIP phones are not restarted.

### Command Modes

Voice register global configuration (config-register-global) Voice register pool configuration (config-register-pool)

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

This command causes the system to perform a fast phone reset in which
                              		  only the button template, lines, and speed-dial numbers are updated on the
                              		  phone. For updates related to phone firmware, user locale, network locale, or
                              		  URL parameters, use the reset command.

Use this command to reboot SIP phones after quick changes to buttons,
                              		  lines, and speed-dial numbers. This command is much faster than the reset command because the phone does not
                              		  access the DHCP or TFTP server.

To restart a single SIP phone, use the restart command in voice register pool configuration mode. To restart
                              		  all SIP phones in a Cisco Unified CME system, use the restart command in voice register global
                              		  configuration mode.

This command has a no form, however the no form has no effect.

## Examples

The following example performs a quick restart of all SIP phones in a
                              		  Cisco Unified CME system:

```
Router(config)# voice register global Router(config-register-global)# restart
```

The following example performs a quick restart of SIP phone 10:

```
Router(config)# voice register pool 10 Router(config-register-pool)# restart
```

### Related Commands

Description

reset (voice register pool)

Performs a complete reboot of a single SIP phone associated
                                          						with a Cisco Unified CME router.

reset (voice register global)

Performs a complete reboot of all SIP phones associated
                                          						with a Cisco Unified CME router.

## restart (voice-gateway)

To perform a fast restart of all analog phones associated with the
                              		  voice gateway and registered to Cisco Unified CME, use the restart command in voice-gateway configuration mode.

restart

### Syntax Description

This command has no arguments or keywords.

### Command Default

Analog phones are not restarted.

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

This command initiates a quick phone restart in which only the
                              		  buttons, lines, and speed-dial numbers are updated on the phone. For updates
                              		  related to phone firmware, user and network locales, or URL parameters, use the reset command.

Use this command to reboot all analog phones on the voice gateway
                              		  after simple configuration changes to buttons, lines, and speed-dial numbers.
                              		  This command is faster than the reset command because the phone does not
                              		  access the DHCP server.

This command has a no form, although the no form has no effect.

## Examples

The following example shows how to perform a quick restart of all
                              		  analog phones:

```
Router(config)# voice-gateway system 1 Router(config-voice-gateway)# restart
```

### Related Commands

Command

Description

reset (voice-gateway)

Performs a complete reboot of all analog endpoints
                                          						associated with the voice gateway.

## ring (ephone-dn)

To set the ring pattern for all incoming calls to an ephone-dn, use
                              		  the ring command in ephone-dn configuration mode.
                              		  To return to the standard ring pattern, use the no form of this command.

ring { external | feature | internal } [ primary | secondary ]

no ring

### Syntax Description

external

External ring pattern is used for all incoming calls.

feature

Feature ring pattern is used for all incoming calls.

internal

Internal ring pattern is used for all incoming calls.

primary

(Optional) Ring pattern is used on primary number only.

secondary

(Optional) Ring pattern is used on secondary number only.

### Command Default

Standard ring pattern is used.

### Command Modes

Ephone-dn configuration (config-ephone-dn)

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

This command allows you to select one of the three ring styles
                              		  supported by SCCP—internal, external, or feature ring. The ring pattern is used
                              		  for all types of incoming calls to this directory number, on all phones on
                              		  which the directory number appears. If the phone is already in use, an incoming
                              		  call is presented as a call-waiting call and uses the distinctive call-waiting
                              		  beep.

If the primary or secondary keyword is used, the distinctive
                              		  ring is used only if the incoming called number matches the primary number or
                              		  secondary number defined for the ephone-dn. If there is no secondary number
                              		  defined for the ephone-dn, the secondary keyword has no effect.

By default, Cisco Unified CME uses the internal ring pattern for
                              		  calls between local IP phones and uses the external ring pattern for all other
                              		  types of calls.

You can associate the feature ring pattern with a specific button on
                              		  a phone by using the button f command. This command assigns the ring pattern
                              		  to the button on the phone so that different phones that share the same
                              		  directory number can use a different ring style.

## Examples

The following example sets external ringing for all incoming calls on
                              		  extension 2389.

```
ephone-dn 24
 number 2389
 ring external
```

### Related Commands

Description

button

Associates ephone-dns with individual buttons on an IP
                                          						phone and specifies line type or ring behavior.

## route-code

To enable phone users to dial a route code to specify special routing
                              		  for a call, use the route-code command in voice MLPP
                              		  configuration mode. To reset to the default, use the no form of this command.

route-code

no route-code

### Syntax Description

This command has no arguments or keywords.

### Command Default

Route code is disabled.

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

This command enables users to specify special routing for an MLPP
                              		  call by dialing a route code. The route code is a two-digit number beginning
                              		  with 1.

## Examples

The following example shows how to enable users to dial a route code:

```
Router(config)# voice mlpp Router(config-voice-mlpp)# route-code
```

### Related Commands

Command

Description

access-digit

Defines the access digit that phone users dial to request a
                                          						precedence call.

mlpp preemption

Enables preemption capability on an SCCP phone or analog
                                          						FXS port.

service-digit

Enables phone users to dial a service digit to request
                                          						off-net services.

## rule (voice
                        	 translation-rule)

To define a
                              		  translation rule, use the rule command
                              		  in voice translation-rule configuration mode. To delete the translation rule,
                              		  use the no form of this command.

### Match and
                              			 Replace Rule

rule precedence /match-pattern/
                                 				  /replace-pattern/ [ type {match-type
                                 				  replace-type} [ plan {match-type replace-type} ]]

no rule precedence

### Reject
                              			 Rule

rule predence reject precedence /match-pattern/ /replace-pattern/ /match-pattern/ [ type {match-type [ plan {match-type r ]]

no rule precedence

### Syntax Description

precedence

Priority of the translation rule. Range is from 1 to 15.

/ match - pattern /

Stream
                                          						editor (SED) expression used to match incoming call information. The slash ‘/’
                                          						is a delimiter in the pattern.

/ replace - pattern /

SED
                                          						expression used to replace the match pattern in the call information. The slash
                                          						‘/’ is a delimiter in the pattern.

type match - type replace-type

(Optional) Number type of the call. Valid values for the match-type argument are as follows:

- abbreviated —Abbreviated representation of the
                                             						  complete number as supported by this network.

- any —Any type of called number.

- international —Number called to reach a subscriber
                                             						  in another country.

- national —Number called to reach a subscriber in
                                             						  the same country, but outside the local network.

- network —Administrative or service number specific
                                             						  to the serving network.

- reserved —Reserved for extension. subscriber —Number called to reach a subscriber in
                                             						  the same local network.

- unknown —Number of a type that is unknown by the
                                             						  network.

Valid
                                          						values for the replace-type argument are as follows:

- abbreviated —Abbreviated representation of the
                                             						  complete number as supported by this network.

- international —Number called to reach a subscriber
                                             						  in another country.

- national —Number called to reach a subscriber in
                                             						  the same country, but outside the local network.

type match - type replace - type (continued)

- network —Administrative or service number specific
                                             						  to the serving network.

- reserved —Reserved for extension.

- subscriber —Number called to reach a subscriber in
                                             						  the same local network.

- unknown —Number of a type that is unknown by the
                                             						  network.

plan match - type replace - type

(Optional) Numbering plan of the call. Valid values for the match - type argument are as follows:

- any —Any
                                             						  type of dialed number.

- data

- ermes

- isdn

- national —Number called to reach a subscriber in
                                             						  the same country, but outside the local network.

- private

- reserved —Reserved for extension.

- telex

- unknown —Number of a type that is unknown by the
                                             						  network.

Valid
                                          						values for the replace-type argument are as follows:

- data

- ermes

- isdn

- national —Number called to reach a subscriber in
                                             						  the same country, but outside the local network.

- private

- reserved —Reserved for extension.

- telex

- unknown —Number of a type that is unknown by the
                                             						  network.

reject

The
                                          						match pattern of a translation rule is used for call-reject purposes.

### Command Default

No default
                              		  behavior or values

### Command Modes

Voice translation-rule configuration

## Command History

Release

Modification

12.2(11)T

This
                                          						command was introduced with a new syntax in voice-translation-rule
                                          						configuration mode.

15.1(4)M

This
                                          						command was introduced with an increase in the maximum value of the precidence
                                          						variable from 15 to 100.

### Usage Guidelines

A translation
                              		  rule applies to a calling party number (automatic number identification [ANI])
                              		  or a called party number (dialed number identification service [DNIS]) for
                              		  incoming, outgoing, and redirected calls within Cisco H.323 voice-enabled
                              		  gateways.

Number
                              		  translation occurs several times during the call routing process. In both the
                              		  originating and terminating gateways, the incoming call is translated before an
                              		  inbound dial peer is matched, before an outbound dial peer is matched, and
                              		  before a call request is set up. Your dial plan should account for these
                              		  translation steps when translation rules are defined.

The below table
                              		  shows examples of match patterns, input strings, and result strings for the
                              		  rule (voice translation-rule) command.

Match
                                          					 Pattern

Replacement Pattern

Input
                                          					 String

Result
                                          					 String

Description

/^.*/

//

4085550100

Any
                                          					 string to null string.

//

//

4085550100

4085550100

Match
                                          					 any string but no replacement. Use this to manipulate the call plan or call
                                          					 type.

/\(^...\)456\(...\)/

/\1555\2/

4084560177

4085550177

Match
                                          					 from the middle of the input string.

/\(.*\)0120/

/\10155/

4081110120

4081110155

Match
                                          					 from the end of the input string.

/^1#\(.*\)/

/\1/

1#2345

2345

Replace
                                          					 match string with null string.

/^408...\(8333\)/

/555\1/

4087770100

5550100

Match
                                          					 multiple patterns.

/1234/

/00&00/

5550100

55500010000

Match
                                          					 the substring.

/1234/

/00\000/

5550100

55500010000

Match
                                          					 the substring (same as &).

The software
                              		  verifies that a replacement pattern is in a valid E.164 format that can include
                              		  the permitted special characters. If the format is not valid, the expression is
                              		  treated as an unrecognized command.

The number type
                              		  and calling plan are optional parameters for matching a call. If either
                              		  parameter is defined, the call is checked against the match pattern and the
                              		  selected type or plan value. If the call matches all the conditions, the call
                              		  is accepted for additional processing, such as number translation.

Several rules
                              		  may be grouped together into a translation rule, which gives a name to the rule
                              		  set. A translation rule may contain up to 15 rules. All calls that refer to
                              		  this translation rule are translated against this set of criteria.

The precedence
                              		  value of each rule may be used in a different order than that in which they
                              		  were typed into the set. Each rule’s precedence value specifies the priority
                              		  order in which the rules are to be used. For example, rule 3 may be entered
                              		  before rule 1, but the software uses rule 1 before rule 3.

The software
                              		  supports up to 128 translation rules. A translation profile collects and
                              		  identifies a set of these translation rules for translating called, calling,
                              		  and redirected numbers. A translation profile is referenced by trunk groups,
                              		  source IP groups, voice ports, dial peers, and interfaces for handling call
                              		  translation.

## Examples

The following
                              		  example applies a translation rule. If a called number starts with 5550105 or
                              		  70105, translation rule 21 uses the rule command to forward the number to
                              		  14085550105 instead.

```
Router(config)# voice translation-rule 21 Router(cfg-translation-rule)# rule 1 /^5550105/ /14085550105/ Router(cfg-translation-rule)# rule 2 /^70105/ /14085550105/
```

In the next
                              		  example, if a called number is either 14085550105 or 014085550105, after the
                              		  execution of translation rule 345, the forwarding digits are 50105. If the
                              		  match type is configured and the type is not “unknown,” dial-peer matching is
                              		  required to match the input string numbering type.

```
Router(config)# voice translation-rule 345 Router(cfg-translation-rule)# rule 1 /^14085550105/ /50105/ plan any national Router(cfg-translation-rule)# rule 2 /^014085550105/ /50105/ plan any national
```

### Related Commands

Command

Description

show voice translation-rule

Displays the parameters of a translation rule.

voice translation-rule

Initiates the voice translation-rule definition.

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XW2 | Cisco Unified CME 4.2 | This command was introduced. |
| 12.4(15)XY | Cisco Unified CME 4.2(1) | This command was introduced. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| request-limit | (Optional) Maximum number of concurrent incoming OOD-R
                                          						requests that the router can process. Range: 1 to 500. Default: 500. |
|---|---|

| Release | Cisco product | Modification |
|---|---|---|
| 12.4(11)XJ | Cisco Unified CME 4.1 | This command was introduced. |
| 12.4(15)T | Cisco Unified CME 4.1 | This command was integrated into Cisco IOS Release
                                          						12.4(15)T. |

|  | Description |
|---|---|
| authenticate (voice register global) | Defines the authenticate mode for SIP phones in a Cisco
                                          						Unified CME or Cisco Unified SRST system. |
| credential load | Reloads a credential file into flash memory. |
| debug voip application | Displays all application debug messages. |

| phone-type | Unique
                                       					 number that represents the phone model. |
|---|---|

| Cisco
                                    				  IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.3(3)M | Cisco SIP
                                       					 CME 10.0 | This
                                       					 command was introduced. |

| Command | Description |
|---|---|
| voice register pool-type | Adds a new Cisco Unified SIP IP phone to Cisco Unified CME. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| name | String of up to 30 alphanumeric characters. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XW2 | Cisco Unified CME 4.2 | This command was introduced. |
| 12.4(15)XY | Cisco Unified CME 4.2(1) | This command was introduced. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| keepalive | Duration for registration after which the registration
                                          						expires unless the feature server reregisters before the registration expiry. |

| expires | (Optional) Sets the active time for an incoming
                                          						registration. |
|---|---|
| max sec | (Optional) Maximum expires time for a registration, in
                                          						seconds. The range is from 600 to 86400. The default is 3600. |
| min sec | (Optional) Minimum expires time for a registration, in
                                          						seconds. The range is from 60 to 3600. The default is 60. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SIP SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SIP SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(4)T | Cisco CME 3.4 and Cisco SIP SRST 3.4 | This command was added to Cisco CME. |

|  | Description |
|---|---|
| sip | Enters SIP configuration mode from voice service VoIP
                                          						configuration mode. |
| voice register global | Enters voice register global configuration mode in order to
                                          						set global parameters for all supported Cisco SIP phones in a Cisco Unified CME
                                          						or Cisco Unified SIP SRST environment. |
| voice register pool | Enters voice register pool configuration mode for SIP
                                          						phones. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco ITS 1.0 | This command was introduced |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T |

|  | Description |
|---|---|
| reset (telephony-service) | Performs a complete reboot of one or all phones associated
                                          						with a Cisco CME router. |
| restart (ephone) | Performs a fast reboot of a single phone associated with a
                                          						Cisco CME router. |
| restart (telephony-service) | Performs a fast reboot of one or all phones associated with
                                          						a Cisco CME router. |

| all | Resets all Cisco IP phones served by the Cisco CME router.
                                          						The router pauses for 15 seconds between the reset starts for each successive
                                          						phone unless the time-interval argument is used to change that value. |
|---|---|
| time-interval | (Optional) Time interval, in seconds, between each phone
                                          						reset. Range is from 0 to 60. Default is 15. |
| cancel | Interrupts a sequential reset cycle that was started with a reset sequence-all command. |
| mac-address | MAC address of a particular Cisco IP phone. |
| sequence-all | Resets all phones in strict one-at-a-time order by waiting
                                          						for one phone to reregister before starting the reset for the next phone. The
                                          						sequencing of resets prevents possible conflicts between phones trying to
                                          						access TFTP services simultaneously. There is a reset timeout of 4 minutes,
                                          						after which the router stops waiting for the currently registering phone to
                                          						complete registration and starts to reset the next phone. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco ITS 1.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |
| 12.2(11)YT | Cisco ITS 2.1 | The time-interval range maximum was increased from 15 to 60 and the
                                          						default was changed from 0 to 15. |
| 12.2(11)YT1 | Cisco ITS 2.1 | The cancel and sequence-all keywords were
                                          						introduced. |
| 12.2(15)T | Cisco ITS 2.1 | This command was integrated into Cisco IOS Release
                                          						12.2(15)T. |

|  | Description |
|---|---|
| reset (ephone) | Performs a complete reboot of a single phone associated
                                          						with a Cisco CME router. |
| restart (ephone) | Performs a fast reboot of a single phone associated with a
                                          						Cisco CME router. |
| restart (telephony-service) | Performs a fast reboot of one or all phones associated with
                                          						a Cisco CME router. |
| telephony-service | Enters telephony-service configuration mode. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XW2 | Cisco Unified CME 4.2 | This command was introduced. |
| 12.4(15)XY | Cisco Unified CME 4.2(1) | This command was introduced. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

|  | Description |
|---|---|
| reset (voice register pool) | Performs a complete reboot of a single SIP phone associated
                                          						with a Cisco CME router. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

|  | Description |
|---|---|
| reset (voice register global) | Performs a complete reboot of all SIP phones associated
                                          						with a Cisco CME router. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| restart (voice-gateway) | Performs a fast restart of all analog endpoints associated
                                          						with the voice gateway. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(20)YA | Cisco Unified CME 7.0(1) | This command was introduced. |
| 12.4(22)T | Cisco Unified CME 7.0(1) | This command was integrated into Cisco IOS Release
                                          						12.4(22)T. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(11)YT1 | Cisco ITS 2.1 | This command was introduced. |
| 12.2(15)T | Cisco ITS 2.1 | This command was integrated into Cisco IOS Release
                                          						12.2(15)T. |

|  | Description |
|---|---|
| reset (ephone) | Performs a complete reboot of a Cisco IP phone associated
                                          						with a Cisco CME router. |
| reset (telephony-service) | Performs a complete reboot of one or all phones associated
                                          						with a Cisco CME router. |
| restart (telephony-service) | Performs a fast reboot of one or all phones associated with
                                          						a Cisco CME router. |

| all | Restarts all phones associated with the Cisco CME router. |
|---|---|
| time-interval | (Optional) Time between each phone restart, in seconds.
                                          						Range is from 0 to 60. Default is 15. |
| mac-address | MAC address of the phone to be restarted. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(11)YT1 | Cisco ITS 2.1 | This command was introduced. |
| 12.2(15)T | Cisco ITS 2.1 | This command was integrated into Cisco IOS Release
                                          						12.2(15)T. |

|  | Description |
|---|---|
| reset (ephone) | Performs a complete reboot of a Cisco IP phone associated
                                          						with a Cisco CME router. |
| reset (telephony-service) | Performs a complete reboot of one or all phones associated
                                          						with a Cisco CME router. |
| restart (ephone) | Performs a fast reboot of a single phone associated with a
                                          						Cisco CME router. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XJ | Cisco Unified CME 4.1 | This command was introduced. |
| 12.4(15)T | Cisco Unified CME 4.1 | This command was integrated into Cisco IOS Release
                                          						12.4(15)T. |

| Note | This command requires firmware load 8-0-2-14 or later versions; it
                                       		  is not supported in older SIP phone loads. To support this command on SIP
                                       		  phones using older firmware, you must upgrade all your phone firmware. |
|---|---|

|  | Description |
|---|---|
| reset (voice register pool) | Performs a complete reboot of a single SIP phone associated
                                          						with a Cisco Unified CME router. |
| reset (voice register global) | Performs a complete reboot of all SIP phones associated
                                          						with a Cisco Unified CME router. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| reset (voice-gateway) | Performs a complete reboot of all analog endpoints
                                          						associated with the voice gateway. |

| external | External ring pattern is used for all incoming calls. |
|---|---|
| feature | Feature ring pattern is used for all incoming calls. |
| internal | Internal ring pattern is used for all incoming calls. |
| primary | (Optional) Ring pattern is used on primary number only. |
| secondary | (Optional) Ring pattern is used on secondary number only. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

|  | Description |
|---|---|
| button | Associates ephone-dns with individual buttons on an IP
                                          						phone and specifies line type or ring behavior. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| access-digit | Defines the access digit that phone users dial to request a
                                          						precedence call. |
| mlpp preemption | Enables preemption capability on an SCCP phone or analog
                                          						FXS port. |
| service-digit | Enables phone users to dial a service digit to request
                                          						off-net services. |

| precedence | Priority of the translation rule. Range is from 1 to 15. |
|---|---|
| / match - pattern / | Stream
                                          						editor (SED) expression used to match incoming call information. The slash ‘/’
                                          						is a delimiter in the pattern. |
| / replace - pattern / | SED
                                          						expression used to replace the match pattern in the call information. The slash
                                          						‘/’ is a delimiter in the pattern. |
| type match - type replace-type | (Optional) Number type of the call. Valid values for the match-type argument are as follows: abbreviated —Abbreviated representation of the
                                             						  complete number as supported by this network. any —Any type of called number. international —Number called to reach a subscriber
                                             						  in another country. national —Number called to reach a subscriber in
                                             						  the same country, but outside the local network. network —Administrative or service number specific
                                             						  to the serving network. reserved —Reserved for extension. subscriber —Number called to reach a subscriber in
                                             						  the same local network. unknown —Number of a type that is unknown by the
                                             						  network. Valid
                                          						values for the replace-type argument are as follows: abbreviated —Abbreviated representation of the
                                             						  complete number as supported by this network. international —Number called to reach a subscriber
                                             						  in another country. national —Number called to reach a subscriber in
                                             						  the same country, but outside the local network. |
| type match - type replace - type (continued) | network —Administrative or service number specific
                                             						  to the serving network. reserved —Reserved for extension. subscriber —Number called to reach a subscriber in
                                             						  the same local network. unknown —Number of a type that is unknown by the
                                             						  network. |
| plan match - type replace - type | (Optional) Numbering plan of the call. Valid values for the match - type argument are as follows: any —Any
                                             						  type of dialed number. data ermes isdn national —Number called to reach a subscriber in
                                             						  the same country, but outside the local network. private reserved —Reserved for extension. telex unknown —Number of a type that is unknown by the
                                             						  network. Valid
                                          						values for the replace-type argument are as follows: data ermes isdn national —Number called to reach a subscriber in
                                             						  the same country, but outside the local network. private reserved —Reserved for extension. telex unknown —Number of a type that is unknown by the
                                             						  network. |
| reject | The
                                          						match pattern of a translation rule is used for call-reject purposes. |

| Release | Modification |
|---|---|
| 12.2(11)T | This
                                          						command was introduced with a new syntax in voice-translation-rule
                                          						configuration mode. |
| 15.1(4)M | This
                                          						command was introduced with an increase in the maximum value of the precidence
                                          						variable from 15 to 100. |

| Note | Use this
                                       		  command in conjunction after the voice translation-rule command. An earlier version of
                                       		  this command uses the same name but is used after the translation-rule command and has a slightly
                                       		  different command syntax. In the older version, you cannot use the square
                                       		  brackets when you are entering command syntax. They appear in the syntax only
                                       		  to indicate optional parameters, but are not accepted as delimiters in actual
                                       		  command entries. In the newer version, you can use the square brackets as
                                       		  delimiters. Going forward, we recommend that you use this newer version to
                                       		  define rules for call matching. Eventually, the translation-rule command will not be supported. |
|---|---|

| Match
                                          					 Pattern | Replacement Pattern | Input
                                          					 String | Result
                                          					 String | Description |
|---|---|---|---|---|
| /^.*/ | // | 4085550100 |  | Any
                                          					 string to null string. |
| // | // | 4085550100 | 4085550100 | Match
                                          					 any string but no replacement. Use this to manipulate the call plan or call
                                          					 type. |
| /\(^...\)456\(...\)/ | /\1555\2/ | 4084560177 | 4085550177 | Match
                                          					 from the middle of the input string. |
| /\(.*\)0120/ | /\10155/ | 4081110120 | 4081110155 | Match
                                          					 from the end of the input string. |
| /^1#\(.*\)/ | /\1/ | 1#2345 | 2345 | Replace
                                          					 match string with null string. |
| /^408...\(8333\)/ | /555\1/ | 4087770100 | 5550100 | Match
                                          					 multiple patterns. |
| /1234/ | /00&00/ | 5550100 | 55500010000 | Match
                                          					 the substring. |
| /1234/ | /00\000/ | 5550100 | 55500010000 | Match
                                          					 the substring (same as &). |

| Command | Description |
|---|---|
| show voice translation-rule | Displays the parameters of a translation rule. |
| voice translation-rule | Initiates the voice translation-rule definition. |