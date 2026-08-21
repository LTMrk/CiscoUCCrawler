---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-command-reference-cme-cr-cme-cr-chapter-01011-html-c668ce8ed9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/command/reference/cme_cr/cme_cr_chapter_01011.html
retrieved_at: 2026-08-21T22:56:32.977838+00:00
---

Cisco Unified Communications Manager Express Command Reference

# Cisco Unified Communications Manager Express Command Reference

Updated: July 19, 2018

Chapter: Cisco Unified CME Commands: M

## Chapter: Cisco Unified CME Commands: M

# Cisco Unified CME Commands: M

## mac-address (ephone)

To associate the MAC address of a Cisco IP phone with an ephone
                              		  configuration in a Cisco CallManager Express (Cisco CME) system, use the mac-address command in ephone configuration
                              		  mode. To disassociate the MAC address from an ephone configuration, use the no form of this command.

mac-address [mac-address] [ reserved ]

no mac-address

### Syntax Description

mac-address

Identifying MAC address of an IP phone, which is found on a
                                          						sticker located on the bottom of the phone.

reserved

Identifies the reserved MAC address of the phone.

### Command Default

There are no default behavior or values for this command.

### Command Modes

Ephone configuration (config-ephone)

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

The mac-address argument was made
                                          						optional to enable automatic MAC address assignment after registration of
                                          						phones.

12.3(4)T

Cisco CME 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

Use this command to specify the MAC address of a specific Cisco IP
                              		  phone in order to physically identify the Cisco IP phone in a Cisco CME
                              		  configuration. The MAC address of each Cisco IP phone is printed on a sticker
                              		  that is placed on the bottom of the phone.

If you choose to register phones before configuring them, the mac-address command can be used during
                              		  configuration without entering the mac-address argument. The Cisco CME system
                              		  detects MAC addresses and automatically populates phone configurations with
                              		  their corresponding MAC addresses and phone types. This capability is not
                              		  supported for voice-mail ports and is supported only by Cisco CME 3.0 and later
                              		  versions. To use this capability, enable Cisco CME by using the following
                              		  commands: max-ephones , max-dn , create cnf-files , and ip source-address. After these commands have been
                              		  used, phones can start to register. Then, when you are configuring a registered
                              		  ephone and you use the mac-address command with no argument, the MAC
                              		  address of the phone is automatically read into the configuration. The
                              		  equivalent functionality is available through the Cisco CME graphic user
                              		  interface (GUI).

If you choose to configure phones before registering them, the MAC
                              		  address for each ephone must be entered during configuration.

## Examples

The following example associates the MAC address CFBA.321B.96FA with
                              		  the IP phone that has phone-tag 22:

```
Router(config)# ephone 22 Router(config-ephone)# mac-address CFBA.321B.96FA
```

### Related Commands

Description

create cnf-files

Builds the XML configuration files that are required for IP
                                          						phones used with Cisco IOS Telephony Services V2.1, Cisco CallManager Express
                                          						3.0, or later versions.

ip source-address

Identifies the IP address and port through which IP phones
                                          						communicate with a Cisco CME router.

max-dn

Sets the maximum number of ephone-dns to be supported by a
                                          						Cisco CME router.

max-ephones

Sets the maximum number of ephones to be supported by a
                                          						Cisco CME router.

show ephone registered

Displays status and information for registered IP phones.

## mac-address (voice-gateway)

To define the MAC address of the voice gateway to autoconfigure, use
                              		  the mac-address command in voice-gateway
                              		  configuration mode. To remove the MAC address from the configuration, use the no form of this command.

mac-address mac-address

no mac-address

### Syntax Description

mac-address

MAC address of the voice gateway.

### Command Default

No MAC address is defined for the voice gateway to be autoconfigured.

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

This command was integrated into Cisco IOS release
                                          						12.4(24)T.

### Usage Guidelines

This command defines the MAC address of the Cisco voice gateway that
                              		  downloads its XML configuration file from Cisco Unified CME using the
                              		  Autoconfiguration feature.

## Examples

The following example associates the MAC address 001F.A30F.8331 for
                              		  the Cisco VG224 voice gateway associated with tag 1:

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

type (voice-gateway)

Defines the type of voice gateway to autoconfigure in Cisco
                                          						Unified CME.

voice-port (voice-gateway)

Identifies the analog ports on the voice gateway that
                                          						register to Cisco Unified CME.

## mailbox-selection (dial-peer)

To set a policy for selecting a mailbox for calls from a Cisco
                              		  Unified CME system that are diverted before being sent to a Cisco Unity Express
                              		  or PBX voice-mail pilot number, use the mailbox-selection command in dial-peer
                              		  configuration mode. To return to the default, use the no form of this command.

mailbox-selection { last-redirect-num | orig-called-num }

no mailbox-selection

### Syntax Description

last-redirect-num

(PBX voice mail only) The mailbox to which the call will be
                                          						sent is the number that diverted the call to the voice-mail pilot number (the
                                          						last number to divert the call).

orig-called-num

(Cisco Unity Express only) The mailbox to which the call
                                          						will be sent is the number that was originally dialed before the call was
                                          						diverted.

### Command Default

Cisco Unity Express uses the last number to which the call was
                              		  diverted before it was sent to voice mail as the mailbox number. Some legacy
                              		  PBX systems use the originally called number as the mailbox number.

### Command Modes

Dial-peer configuration (config-dial-peer)

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

When Cisco Unified CME diverts a call, it captures the reroute
                              		  information which will be used to compose a reroute request. A dial-peer match
                              		  will be performed against the diverted-to number. If this is the voice mail
                              		  pilot number and the mailbox-selection command has been used to
                              		  install a policy, the reroute information will be amended as directed by the
                              		  command. The originator will pick up the modified reroute request, build the
                              		  diversion information and include it in the new diverted call to the voice-mail
                              		  pilot number.

This command should be used on the outbound dial peer for the pilot
                              		  number of the voice-mail system.

This command might not work properly in certain network topologies,
                              		  including the following cases:

- When the last redirecting endpoint is not hosted on Cisco Unified
                                 			 CME. This rarely occurs with a PBX.

- When a call is forwarded across several SIP trunks. Multiple SIP
                                 			 Diversion Headers (stacking hierarchy) are not supported in Cisco IOS software.

- When a call is forwarded across non Cisco voice gateways that do
                                 			 not support the optional H450.3 originalCalledNr field.

## Examples

The following example shows how to set a policy to select the mailbox
                              		  of the originally called number when a call is diverted to a Cisco Unity
                              		  Express or PBX voice-mail system with the pilot number 7000.

```
dial-peer voice 7000 voip
 destination-pattern 7000
 session target ipv4:10.3.34.211
 codec g711ulaw
 no vad
 mailbox-selection orig-called-num
```

## mailbox-selection (ephone-dn)

To set a policy for selecting a mailbox for calls that are diverted
                              		  before being sent to a Cisco Unity voice-mail pilot number, use the mailbox-selection command in ephone-dn
                              		  configuration mode. To return to the default, use the no form of this command.

mailbox-selection last-redirect-num

no mailbox-selection

### Syntax Description

last-redirect-num

The mailbox to which the call will be sent is the last
                                          						number to divert the call.

### Command Default

Cisco Unity uses the originally called number as the mailbox number.

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

This command sets the policy for selecting a mailbox for diverted
                              		  calls.

This command is used on the ephone-dn associated with the voice-mail
                              		  pilot number.

This command can only be used with SCCP phones.

This command might not work properly in certain network topologies,
                              		  including the following cases:

- When the last redirecting endpoint is not hosted on Cisco Unified
                                 			 CME. This may rarely occur with a PBX.

- When a call is forwarded across several SIP trunks. Multiple SIP
                                 			 Diversion Headers (stacking hierarchy) are not supported in Cisco IOS software.

- When a call is forwarded across non Cisco voice gateways that do
                                 			 not support the optional H450.3 originalCalledNr field.

## Examples

The following example sets a policy to select the mailbox of the last
                              		  redirecting number when a call is diverted to a Cisco Unity voice-mail system
                              		  with the pilot number 8000.

```
ephone-dn 2583
 number 8000
 mailbox-selection last-redirect-num
```

## max-calls-per-button

To set the maximum number of calls allowed on an octo-line directory
                              		  number on an SCCP phone, use the max-calls-per-button command in ephone or
                              		  ephone-template configuration mode. To reset to the default, use the no form of this command.

max-calls-per-button number-of-calls

no max-calls-per-button

### Syntax Description

number-of-calls

Maximum number of calls. Range: 1 to 8. Default: 8.

### Command Default

Maximum number of calls allowed on an octo-line is 8.

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

Cisco Unified CME 4.3

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

This command limits the maximum number of calls, both incoming and
                              		  outgoing, that can be active on each octo-line directory number on an SCCP
                              		  phone. This command applies to all octo-line directory numbers on the phone.

This command must be set to a value that is more than or equal to the
                              		  value set with the busy-trigger-per-button command.

For phones that do not support octo-line directory numbers such as
                              		  the Cisco Unified IP Phone 7902, 7920, or 7931, and analog phones connected to
                              		  the Cisco VG224 or Cisco ATA, we recommend that you set the max-calls-per-button command to 2. Otherwise,
                              		  after the phone type is identified with either the type command or during phone registration,
                              		  this command is automatically set to 2.

If you use an ephone template to apply a command to an ephone and you
                              		  also use the same command in ephone configuration mode for the same ephone, the
                              		  value that you set in ephone configuration mode has priority.

## Examples

The following example sets the maximum calls allowed on octo-lines to
                              		  4 on ephone 1.

```
Router(config)# ephone 1 Router(config-ephone)# max-calls-per-button 4
```

### Related Commands

Command

Description

busy-trigger-per-button

Sets the maximum number of incoming calls allowed on an
                                          						octo-line directory number before it triggers Call Forward Busy on the phone.

ephone-dn

Configures a directory number for SCCP phones.

type

Assigns a phone type to an SCCP phone.

## max-conferences

To set the maximum number of three-party conferences that are
                              		  supported simultaneously by the Cisco CallManager Express (Cisco CME) router,
                              		  use the max-conferences command in telephony-service
                              		  configuration mode. To reset this number to the default, use the no form of this command.

max-conferences max-conference-number [gain
                                 				  -6 | 0 | 3 | 6]

no max-conferences

### Syntax Description

max-conference number

Maximum number of three-party conferences that are
                                          						supported simultaneously by the router. This number is platform-dependent, and
                                          						the default is half the maximum for each platform. The following are the
                                          						maximum values for this argument:

- Cisco 1700 series, Cisco 2600 series, Cisco 2801—8

- Cisco 2811, Cisco 2821, Cisco 2851, Cisco 3600 series,
                                             						  Cisco 3700 series—16

- Cisco 3800 series—24 (requires Cisco IOS Release
                                             						  12.3(11)XL or higher)

gain

(Optional) Increases the sound volume of VoIP and public
                                          						switched telephony network (PSTN) parties joining a conference call. The
                                          						allowable decibel units are -6 db, 0 db, 3 db, and 6 db. The default is -6 db.

### Command Default

Default is half the maximum number of simultaneous three-party
                              		  conferences for each platform.

### Command Modes

Telephony-service configuration (config-telephony)

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

12.3(11)XL1

Cisco CME 3.2.1

The gain keyword was added.

12.3(14)T

Cisco CME 3.3

This command was integrated into Cisco IOS Release
                                          						12.3(14)T.

### Usage Guidelines

This command supports three-party conferences for local and on-net
                              		  calls only when all conference participants are using the G.711 codec.
                              		  Conversion between G.711 mu-law and A-law is supported. Mixing of the media
                              		  streams is supported by the Cisco IOS processor. The maximum number of
                              		  simultaneous conferences is limited to the platform-specific maximums.

The gain keyword’s functionality is applied to
                              		  inbound audio packets, so conference participants can more clearly hear a
                              		  remote PSTN or VoIP caller joining their call. Note that this functionality
                              		  cannot discriminate between a remote VoIP/foreign exchange office (FXO) source,
                              		  which requires a volume gain, and a remote VoIP/IP phone, which does not
                              		  require a volume gain and may therefore incur some sound distortions.

## Examples

The following example sets the maximum number of conferences for a
                              		  Cisco IP phone to 4 and configures a gain of 6 db for inbound audio packets
                              		  from remote PSTN or VoIP calls joining a conference:

```
Router(config)# telephony-service Router(config-telephony)# max-conferences 4 gain 6
```

## max-dn

To set the maximum quantity of directory numbers (ephone-dns) that can be configured on a Cisco Unified CME router, use the max-dn command in telephony-service configuration mode. To reset this number to the default value, use the no form of this command.

max-dn max-directory-numbers [ preference preference-order ] [ no-reg { primary | both }]

no max-dn

### Syntax Description

max directory numbers

Maximum number of directory numbers (ephone-dns) to allow in the Cisco CME system. The maximum you can set depends on the
                                          software version, router platform, and amount of memory that you have installed. Type ? to display range. The default is 0.

preference preference-order

(Optional) Sets a preference value for the primary number
                                          						of an ephone-dn. Refer to CLI help for a range of numeric options, where 0 is
                                          						the highest preference. Default is 0.

no-reg

(Optional) Globally disables ephone registration with an
                                          						H.323 gatekeeper or SIP proxy.

primary

Primary ephone-dn numbers only.

both

Both primary and secondary ephone-dn numbers.

### Command Default

The default is 0.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.1(5)YD

Cisco ITS 1.0

This command was introduced

12.2(8)T

Cisco ITS 2.0

This command was integrated into Cisco IOS Release
                                          						12.2(8)T.

12.4(4)XC

Cisco Unified 4.0

The preference , no-reg , primary , and both keywords were introduced.

12.4(9)T

Cisco Unified 4.0

The preference , no-reg , primary , and both keywords were integrated into
                                          						Cisco IOS Release 12.4(9)T.

### Usage Guidelines

The max-dn command limits the number of
                              		  extensions (ephone-dns) available in a Cisco Unified CME system. The maximum
                              		  number of ephone-dns that you can create depends on the software version,
                              		  router platform, and amount of memory that you have installed. Type ? to display range.

The max-ephones command similarly limits the
                              		  number of IP phones in a Cisco Unified CME system.

If registration with an H.323 gatekeeper or SIP proxy is enabled
                              		  globally (the default), you can override the setting per extension by using the no-reg keyword in the number command for individual ephone-dns.

After using this command, you can provision individual extensions
                              		  using the Cisco Unified CME graphic user interface (GUI) or the router CLI in
                              		  ephone-dn configuration mode.

## Examples

The following example sets the maximum number of extensions
                              		  (ephone-dns) to 12:

```
Router(config)# telephony-service Router(config-telephony)# max-dn 12
```

The following example sets the maximum number of extensions to 150
                              		  and specifies that the primary number of each extension should receive a
                              		  dial-peer preference order of 1:

```
Router(config)# telephony-service Router(config-telephony)# max-dn 150 preference 1
```

The following example sets the maximum number of extensions to 200
                              		  and specifies that they should not register both primary and secondary numbers
                              		  with the H.323 gatekeeper:

```
Router(config)# telephony-service Router(config-telephony)# max-dn 200 no-reg both
```

The following example sets the maximum number of extensions to 200
                              		  and specifies that ephone-dn 36 should not register its primary number with the
                              		  gatekeeper:

```
Router(config)# telephony-service Router(config-telephony)# max-dn 200 Router(config-telephony)# exit Router(config)# ephone-dn 36 Router(config-ephone-dn)# number 75373 no-reg primary
```

### Related Commands

Description

ephone-dn

Enters ephone-dn configuration mode.

max-ephones

Sets the maximum number of phones supported by the router.

number

Associates a telephone or extension number with an
                                          						ephone-dn.

## max-dn (voice register global)

To set the maximum number of SIP phone directory numbers (extensions) that are supported by a Cisco router, use the max-dn command in  voice register global configuration mode. To reset to the default, use the no form of this command.

max-dn max-directory-numbers

no max-dn

### Syntax Description

max directory numbers

Maximum number of extensions (ephone-dns) supported by the
                                          						Cisco router. The maximum number is version and platform dependent; type ? to display range.

In Cisco CME 3.4 to Cisco Unified CME 7.0 and in Cisco SIP SRST 3.4 to Cisco Unified SIP SRST 7.0: Default is maximum number
                                                supported by platform.

In Cisco Unified CME 7.1 and Cisco Unified SIP SRST 7.1 and later versions: Default is 0.

### Command Default

Before Cisco Unified CME 7.1 and Cisco Unified SIP SRST 7.1, default
                              		  is maximum number supported by platform.

In Cisco Unified CME 7.1 and Cisco Unified SIP SRST 7.1 and later
                              		  versions, default is 0.

### Command Modes

Voice register global configuration (config-register-global)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was introduced.

12.4(22)YB

Cisco Unified CME 7.1 Cisco Unified SIP SRST 7.1

The default value was changed to 0.

12.4(24)T

Cisco Unified CME 7.1 Cisco Unified SIP SRST 7.1

This command was integrated into Cisco IOS release
                                          						12.4(24)T.

### Usage Guidelines

This command limits the number of SIP phone directory numbers
                              		  (extensions) available in a Cisco Unified CME system. The max-dn command is platform specific. It
                              		  defines the limit for the voice register dn command. The max-pool command similarly limits the number
                              		  of SIP phones in a Cisco CME system.

You can increase the number of allowable extensions to the maximum;
                              		  but after the maximum allowable number is configured, you cannot reduce the
                              		  limit without rebooting the router. You cannot reduce the number of allowable
                              		  extensions without removing the already-configured directory numbers with
                              		  dn-tags that have a higher number than the maximum number to be configured.

## Examples

The following example shows how to set the maximum number of
                              		  directory numbers to 48:

```
Router(config)# voice register global Router(config-register-global)# max-dn 48
```

### Related Commands

Command

Description

voice register dn

Enters voice register dn configuration mode to define an
                                          						extension for a SIP phone line.

max-pool (voice register global)

Sets the maximum number of SIP voice register pools that
                                          						are supported in a Cisco SIP SRST or Cisco CME environment.

## max-ephones

To set the maximum number of Cisco IP phones to be supported by a
                              		  Cisco CallManager Express (Cisco CME) router, use the max-ephones command in telephony-service
                              		  configuration mode. To reset this number to the default value, use the no form of this command.

max-ephones max-phones

no max-ephones

### Syntax Description

max phones

Maximum number of phones supported by the Cisco CME router.
                                          						The maximum number is version- and platform-dependent; refer to Cisco IOS
                                          						command-line interface (CLI) help. Default is 0.

### Command Default

Default is 0.

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

12.4(15)XZ

Cisco Unified CME 4.3

This command was modified to set the maximum number of
                                          						phones that can register to Cisco Unified CME.

12.4(20)T

Cisco Unified CME 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

The max-ephones command limits the number of
                              		  Cisco IP phones supported on the router. The maximum number you can set is
                              		  platform- and version-dependent. Use CLI help to determine the maximum number
                              		  of ephones you can set, as shown in this example:

```
Router(config-telephony)# max-ephones ? <1-48>  Maximum phones to support
```

The max-dn command similarly limits the number of
                              		  extensions (ephone-dns) in a Cisco CME system.

After using this command, configure phones by using the Cisco CME
                              		  graphic user interface (GUI) or the router CLI in ephone configuration mode.

## Examples

The following example sets the maximum number of Cisco IP phones in a
                              		  Cisco CME system to 24:

```
Router(config)# telephony-service Router(config-telephony)# max-ephones 24
```

### Related Commands

Command

Description

ephone

Enters ephone configuration mode.

max-dn

Sets the maximum number of extensions (ephone-dns) that can
                                          						be supported by the router.

## max-idle-time

To create an idle-duration timer for automatically logging out an
                              		  Extension Mobility user, use the max-idle-time command in voice user-profile
                              		  configuration mode. To remove the timer, use the no form of this command.

max-idle-time minutes

no max-idle-time

### Syntax Description

minutes

Maximum number of minutes an Extension Mobility phone is
                                          						idle after which the logged-in user is logged out from Extension Mobility.
                                          						Range:1 to 9999.

### Command Default

No timer is created.

### Command Modes

Voice user-profile configuration (config-user-profile)

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

This command creates an idle-duration timer for automatically logging
                              		  a user out from Extension Mobility. The timer monitors the phone and if the
                              		  specified maximum idle time is exceeded, the EM manager logs out the user.
                              		  Typically this command is used to log out users who fail to manually log out of
                              		  Extension Mobility before leaving a phone.

The call history record is automatically cleared when a user logs out
                              		  from an Extension Mobility phone. To disable Automatic Clear Call History on
                              		  all Extension Mobility phones, use the keep call-history command in telephony-service
                              		  configuration mode.

After creating or modifying a profile, use the reset command in voice user-profile
                              		  configuration mode to reset all phones on which this profile is downloaded to
                              		  propagate the modifications.

## Examples

The following example shows how to create a 30-minute idle-duration
                              		  timer in user profile 1:

```
Router(config)# voice user-profile 1 Router(config-user-profile)# max-idle-time 30 Router(config-user-profile)# reset Router(config-user-profile)#
```

### Related Commands

Command

Description

keep call-history

Disables Automatic Clear Call History for Extension
                                          						Mobility in Cisco Unified CME.

reset (voice logout-profile and voice user-profile)

Performs a complete reboot of all IP phones on which a
                                          						particular logout profile or user profile is downloaded.

## maximum bit-rate (video)

To modify the maximum IP phone video bandwidth in Cisco Unified CME,
                              		  use the maximum bit-rate command in video configuration mode. To
                              		  restore the default maximum bit-rate, use the no form of this command.

maximum bit-rate value

no maximum bit-rate

### Syntax Description

value

Video bandwidth in kb/s Range is 0 to 10000000. Default
                                          						value is 10000000.

### Command Default

Maximum bit-rate of video bandwidth is 1,000,000 kb/s.

### Command Modes

Video configuration (config-tele-video)

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

Use this command to modify the default value of the maximum video
                              		  bandwidth for all video-capable phones associated with a Cisco Unified CME
                              		  router. Default value is 1,000,000 kb/s.

## Examples

The following example sets a maximum bit-rate of 256 kb/s.

```
Router(config)# telephony-service Router(config-telephony)# video Router(conf-tele-video)# maximum bit-rate 256
```

## max-pool (voice register global)

To set the maximum number of Session Initiation Protocol (SIP) voice
                              		  register pools that are supported in Cisco Unified SIP SRST or Cisco Unified
                              		  CME, use the max-pool command in voice register global configuration mode. To reset
                              		  the maximum number to the default, use the no form of this command.

max-pool max-voice-register-pools

no max-pool

### Syntax Description

max voice-register-pools

Maximum number of SIP voice register pools supported by the
                                          						Cisco router. The upper limit of voice register pools is version- and
                                          						platform-dependent; type ? for range.

- In Cisco CME 3.4 to Cisco Unified CME 7.0 and in Cisco
                                             						  SIP SRST 3.4 to Cisco Unified SIP SRST 7.0: Default is maximum number supported
                                             						  by platform.

- In Cisco Unified CME 7.1 and Cisco Unified SIP SRST 7.1
                                             						  and later versions: Default is 0.

### Command Default

Before Cisco Unified CME 7.1 and Cisco Unified SIP SRST 7.1, default
                              		  is maximum number supported by platform. In Cisco Unified CME 7.1 and Cisco
                              		  Unified SIP SRST 7.1 and later versions, default is 0.

### Command Modes

Voice register global configuration (config-register-global)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was introduced.

12.4(22)YB

Cisco Unified CME 7.1 Cisco Unified SIP SRST 7.1

The default value was changed to 0.

12.4(24)T

Cisco Unified CME 7.1 Cisco Unified SIP SRST 7.1

This command was integrated into Cisco IOS release
                                          						12.4(24)T.

### Usage Guidelines

This command limits the number of SIP phones supported by Cisco
                              		  Unified CME. The max-pool command is platform specific and
                              		  defines the limit for the voice register pool command.

The max-dn command similarly limits the number of
                              		  directory numbers (extensions) in Cisco Unified CME.

You can increase the number of phones; but after the maximum
                              		  allowable number is configured, you cannot reduce the limit of the SIP phones
                              		  without rebooting the router.

## Examples

The following example shows how to set the maximum number of Cisco
                              		  SIP IP phones in Cisco Unified SIP SRST or Cisco Unified CME to 24:

```
Router(config)# voice register global Router(config-register-global)# max-pool 24
```

### Related Commands

Command

Description

max-dn (voice register global)

Set the maximum number of SIP phone directory numbers
                                          						(extensions) that are supported by a Cisco Unified CME router.

## max-presentation

To set the number
                              		  of call presentation lines supported by a phone type, use the max-presentation command in ephone-type configuration mode. To reset to the
                              		  default, use the no form of
                              		  this command.

max-presentation number

no max-presentation

### Syntax Description

number

Number
                                          						of presentation lines. Range: 1 to 100. Default: 0. See the table for the
                                          						number of presentation lines supported by each phone type.

### Command Default

No display lines
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
                              		  defines the number of presentation lines that are supported for the type of
                              		  phone being added with an ephone-type template.

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
                              		  example shows that 1 presentation line is specified for the Nokia E61 when
                              		  creating the ephone-type template.

```
Router(config)# ephone-type E61 Router(config-ephone-type)# max-presentation 1
```

### Related Commands

Command

Description

device-id

Specifies the device ID for a phone type in an ephone-type template.

num-buttons

Sets
                                          						the number of line buttons supported by a phone type.

type

Assigns the phone type to an SCCP phone.

## max-redirect

To change the number of times that a call can be redirected by call
                              		  forwarding or transfer within a Cisco Unified CME system, use the max-redirect command in telephony-service configuration mode. To reset to
                              		  the default number of redirects, use the no form of this command.

max-redirect number

no max-redirect

### Syntax Description

number

Number of permissible redirects. Range: 5 to 20. Default:
                                          						10.

### Command Default

Number of redirects is 10.

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

12.4(24)T1

Cisco Unified CME 7.1

The default value was increased from 5 to 10.

15.1(1)T

Cisco Unified CME 8.0

This command was integrated into Cisco IOS Release
                                          						15.1(1)T.

### Usage Guidelines

This command supports Cisco Unified CME ephone hunt groups by
                              		  allowing calls to be redirected more than the default number of times.

## Examples

The following example sets the maximum number of redirects to 8:

```
Router(config)# telephony-service Router(config-telephony)# max-redirect 8
```

### Related Commands

Command

Description

ephone-hunt

Creates an ephone hunt group in Cisco Unified CME.

hops

Sets the number of hops before a call proceeds to the final
                                          						number.

## max-subscription

To set the maximum number of concurrent watch sessions that are
                              		  allowed, use the max-subscription command in presence
                              		  configuration mode. To return to the default, use the no form of this command.

max-subscription number

no max-subscription

### Syntax Description

number

Maximum watch sessions. Range: 100 to 500. Default: 100.

### Command Default

Maximum subscriptions is 100.

### Command Modes

Presence configuration (config-presence)

## Command History

Release

Modification

12.4(11)XJ

This command was introduced.

12.4(15)T

This command was integrated into Cisco IOS Release
                                          						12.4(15)T.

### Usage Guidelines

This command sets the maximum number of concurrent presence
                              		  subscriptions for both internal and external subscribe requests.

## Examples

The following example shows the maximum subscriptions set to 150:

```
Router(config)# presence Router(config-presence)# max-subscription 150
```

### Related Commands

Description

allow watch

Allows a directory number on a phone registered to Cisco
                                          						Unified CME to be watched in a presence service.

allow subscribe

Allows internal watchers to monitor external presence
                                          						entities (directory numbers).

presence enable

Allows incoming presence requests from SIP trunks.

server

Specifies the IP address of a presence server for sending
                                          						presence requests from internal watchers to external presence entities.

watcher all

Allows external watchers to monitor internal presence
                                          						entities (directory numbers).

## max-timeout

To set the maximum combined timeout for the no-answer periods for all
                              		  ephone-dns in the ephone-hunt list, use the max-timeout command in ephone-hunt
                              		  configuration mode. To return this value to the default, use the no form of this command.

max-timeout seconds

no max-timeout seconds

### Syntax Description

seconds

Number of seconds. Range is from 3 to 60000. Default is
                                          						unlimited.

### Command Default

Number of seconds is unlimited.

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

## Examples

The following example shows how to set different no-answer timeouts
                              		  for each ephone-dn in the hunt-group list and no maximum timeout. The first
                              		  call to the hunt group rings extension 1001. If that extension does not answer
                              		  in 7 seconds, the call is forwarded to extension 1002. If that extension does
                              		  not answer after 10 seconds, the call is forwarded to extension 1003. However,
                              		  if extension 1003 does not answer after 8 seconds, the call is sent to the
                              		  final number, extension 4500, because the maximum timeout of 25 seconds has
                              		  been reached.

```
ephone-hunt 3 peer
 pilot 4200
 list 1001, 1002, 1003
 hops 3
 timeout 7, 10, 15
 max-timeout 25
 final 4500
```

### Related Commands

Description

ephone-hunt

Defines an ephone hunt group and enters ephone-hunt
                                          						configuration mode.

## media

To enable media packets to pass directly between the endpoints,
                              		  without the intervention of the Cisco Unified Border Element (Cisco UBE), and
                              		  to enable the incoming and outgoing IP-to-IP call gain/loss feature for audio
                              		  call scoring on either the incoming dial peer or the outgoing dial peer, enter
                              		  the media command in dial peer, voice class, or
                              		  voice service configuration mode. To return to the default IPIPGW behavior, use
                              		  the no form of this command.

media [ flow-around | flow-through | forking | monitoring [max-calls] | statistics | transcoder high-density ]

no media [ flow-around | flow-through | forking | monitoring [max-calls] | statistics | transcoder high-density ]

### Syntax Description

flow-around

(Optional) Enables media packets to pass directly between
                                          						the endpoints, without the intervention of the Cisco UBE. The media packet is
                                          						to flow around the gateway.

flow-through

(Optional) Enables media packets to pass through the
                                          						endpoints, without the intervention of the Cisco UBE.

forking

(Optional) Enables the media forking feature for all calls.

monitoring

Enables the monitoring feature for all calls or a maximum
                                          						number of calls.

max-calls

The maximum number of calls that are monitored.

statistics

(Optional) Enables media monitoring.

transcoder high-density

(Optional) Converts media codecs from one voice standard to
                                          						another to facilitate the interoperability of devices using different media
                                          						standards.

### Command Default

The default behavior of the Cisco UBE is to receive media packets
                              		  from the inbound call leg, terminate them, and then reoriginate the media
                              		  stream on an outbound call leg.

### Command Modes

Dial peer configuration (config-dial-peer) Voice class configuration (config-class) Voice service configuration (config-voi-serv)

## Command History

Release

Modification

12.3(1)T

This command was introduced.

12.4(11)XJ2

This command was modified. The statistics keyword was introduced.

12.4(15)T

This command was integrated into Cisco IOS Release
                                          						12.4(15)T.

12.4(20)T

This command was modified. The transcoder and high-density keywords were
                                          						introduced.

15.0(1)M

This command was modified. The forking and monitoring keywords and the max-calls argument were introduced.

15.1(3)T

This command was modified. The media flow around is now
                                          						supported for the SIP to SIP trunk calls in Cisco Unified CME 8.5.

### Usage Guidelines

With the default configuration, the Cisco UBE receives media packets
                              		  from the inbound call leg, terminates them, and then reoriginates the media
                              		  stream on an outbound call leg. Media flow-around enables media packets to be
                              		  passed directly between the endpoints, without the intervention of the Cisco
                              		  UBE. The Cisco UBE continues to handle routing and billing functions. Media
                              		  flow-around for SIP-to-SIP calls is not supported.

You can specify media flow-around for a voice class, all VoIP calls,
                              		  or individual dial peers.

The transcoder high-density keyword can be enabled in any of the configuration modes with
                              		  the same command format. If you are configuring the transcoder high-density keyword for dial peers, make sure
                              		  that the media transcoder high-density command is configured on both the in
                              		  and out legs.

The software does not support configuring the transcoder high-density keyword on any dial peer that is to
                              		  handle video calls. The following scenarios are not supported:

- Dial peers used for video at any time. Configuring the media transcoder high-density command directly under the dial-peer or a voice-class media
                                 			 configuration is not supported.

- Dial peers configured on a Cisco UBE used for video calls at any
                                 			 time. The global configuration of the media transcoder high-density command under voice service voip is
                                 			 not supported.

To enable the media command on a Cisco 2900 or Cisco 3900
                              		  series Unified Border Element voice gateway, you must first enter the mode border-element command. This enables the media forking and media monitoring commands. Do not configure the mode border-element command on the Cisco 2800 or Cisco
                              		  3800 series platforms.

## Examples

## Examples

The following example shows media flow-around configured on a dial
                              		  peer:

```
Router(config)# dial-peer voice 2 voip Router(config-dial-peer) media flow-around
```

The following example shows media flow-around configured for all VoIP
                              		  calls:

```
Router(config)# voice service voip Router(config-voi-serv) media flow-around
```

The following example shows media flow-around configured for voice
                              		  class calls:

```
Router(config)# voice class media 1 Router(config-class) media flow-around
```

## Examples

The following example shows media flow-around configured on a dial
                              		  peer:

```
Router(config)# dial-peer voice 2 voip Router(config-dial-peer) media flow-through
```

The following example shows media flow-around configured for all VoIP
                              		  calls:

```
Router(config)# voice service voip Router(config-voi-serv) media flow-through
```

The following example shows media flow-around configured for voice
                              		  class calls:

```
Router(config)# voice class media 2 Router(config-class) media flow-through
```

## Examples

The following example shows media monitoring configured for all VoIP
                              		  calls:

```
Router(config)# voice service voip Router(config-voi-serv) media statistics
```

The following example shows media monitoring configured for voice
                              		  class calls:

```
Router(config)# voice class media 1 Router(config-class) media statistics
```

## Examples

The following example shows the media transcoder keyword configured for all VoIP calls:

```
Router(config)# voice service voip Router(conf-voi-serv)# media transcoder high-density
```

The following example shows the media transcoder keyword configured for voice class calls:

```
Router(config)# voice class media 1 Router(config-voice-class)# media transcoder high-density
```

The following example shows the media transcoder keyword configured on a dial peer:

```
Router(config)# dial-peer voice 36 voip Router(config-dial-peer)# media transcoder high-density
```

## Examples

The following example shows how to configure audio call scoring for a
                              		  maximum of 100 calls:

```
mode border-element
media monitoring 100
```

### Related Commands

Command

Description

dial-peer voice

Enters dial peer configuration mode.

mode border-element

Enables the media monitoring capability of the media command.

voice class

Enters voice class configuration mode.

voice service

Enters voice service configuration mode.

## members logout

To configure a Cisco Unified CallManager Express system for all
                              		  non-shared static members or agents in an ephone-hunt with the Hlogout initial
                              		  state, use the members logout command in ephone-hunt configuration mode.
                              		  To return to the default, use the no form of this command.

This command is not allowed after list and hunt-group logout DND are configured or if DNs are shared.

members logout

no members logout

### Syntax Description

This command has no arguments or keywords.

### Command Default

All members are in Hlogin state.

### Command Modes

ephone-hunt configuration (config-ephone hunt)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.2(4)M

Cisco Unified CME 9.1

This command was introduced.

### Usage Guidelines

All members configured under an ephone-hunt are initialized with
                              		  HLogin. Use this command to initialize all non-shared static members to
                              		  Hlogout.

## Examples

The following example configures HLogout as the default for all
                              		  non-shared ephone-hunt static members:

```
Router(config-telephony)# ephone-hunt 1 Router(config-ephone-hunt)# members logout
```

### Related Commands

Command

Description

ephone-hunt

Enters ephone-hunt configuration mode to define a Cisco CME
                                          						ephone-hunt group.

## members logout
                        	 (voice hunt-group)

To configure a
                              		  Cisco Unified CME system for all non-shared static members or agents in a voice
                              		  hunt group with the Hlogout initial state, use the members logout command in voice hunt-group configuration
                              		  mode. To return to the default state, use the no form of this command.

This command is
                              		  not allowed if the CLI command list is
                              		  configured .

members logout

no members logout

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

All members are
                              		  in Hlogin state.

### Command Modes

voice hunt-group

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
                                          						command was introduced.

### Usage Guidelines

All members
                              		  configured under a voice hunt-group are initialized with HLogin. Use this
                              		  command to initialize all non-shared static members to Hlogout. If any member
                              		  of a hunt group in a SIP phone logs out using the CLI command members
                                    				logout , all other DN's of that phone in any hunt group are also
                              		  logged out. This is because SIP phones only support phone level logout. For
                              		  SCCP phones, only the DN that is configured with the CLI command members logout is logged out from the hunt group. Other member DN's do
                              		  not logout as SCCP phones support line level logout.

Members Logout is
                              		  not supported if the CLI command hunt-group logout DND is configured. Also, you cannot configure the CLI
                              		  command members logout if the command list is configured.

## Examples

The following
                              		  example configures HLogout as the default for all non-shared voice hunt-group
                              		  static members:

```
Router(config-register-global)# voice hunt-group 1 Router(config-voice-hunt-group)# members logout
```

### Related Commands

Command

Description

members logout

Enables
                                          						members logout for ephone-hunt groups configured on a Cisco Unified CME.

## missed-calls

To report missed calls to directory numbers on an IP phone, use the missed-calls command in ephone configuration mode. To suppress missed-calls
                              		  reporting, use the no form of this command.

missed-calls [ all ]

no missed-calls

### Syntax Description

all

(Optional) Displays all missed calls including those on
                                          						overlay buttons.

### Command Default

Missed calls are presented on the IP phone and listed in the
                              		  missed-calls directory. Missed calls to overlay buttons are not reported.

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

This command enables Cisco Unified CME to report missed calls on the
                              		  specified phone. Use the all keyword to report missed calls to
                              		  overlaid directory numbers. Only calls to an overlay set that are visibly
                              		  presented on the phone are reported as missed calls. Calls to an overlay that
                              		  are terminated by the caller before they are displayed on the phone are not
                              		  reported as missed calls.

If the unique extension number for a phone is assigned to an overlay
                              		  set on the phone, missed calls to that extension number are not reported unless
                              		  you enable this command using the all keyword.

## Examples

The following example shows that all unanswered calls to 4001 are
                              		  reported on phone 1.

```
ephone-dn  1  dual-line
 number 4001
 
ephone  1
 mac-address 0014.6AAC.24E3
 type 7960
 button  1o1,30,31 2:2 3:3
 missed-calls all
```

### Related Commands

Command

Description

button

Associates directory numbers with individual buttons on a
                                          						Cisco Unified IP Phone and specifies ring behavior.

## mlpp indication

To enable MLPP indication on an SCCP phone or analog FXS port, use
                              		  the mlpp indication command in ephone-template or voice-port configuration mode. To
                              		  disable MLPP indication, use the no form of this command.

mlpp indication

no mlpp indication

### Syntax Description

This command has no arguments or keywords.

### Command Default

MLPP indication is enabled on the phone.

### Command Modes

Ephone-template configuration (config-ephone-template) Voice-port configuration (config-voiceport)

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

This command enables a phone to play precedence and preemption tones,
                              		  and display precedence information for calls. If MLPP indication is disabled,
                              		  calls on the phone can be preempted but there is no visual or audible
                              		  indication.

To apply a template to an SCCP phone, use the ephone-template command in ephone
                              		  configuration mode.

## Examples

The following example shows MLPP indication is disabled in template 5
                              		  and applied to phone 12:

```
ephone-template  5
 mlpp max-precedence 0
 no mlpp indication
!
!
ephone  12
 mac-address 000F.9054.31BD
 ephone-template 5
 type 7960
 button  1:12
```

### Related Commands

Command

Description

ephone-template (ephone)

Applies an ephone template to an SCCP phone.

mlpp max-precedence

Sets the maximum precedence (priority) level that a phone
                                          						user can specify when making an MLPP call.

mlpp preemption

Enables preemption capability on an SCCP phone or analog
                                          						FXS port.

preemption tone timer

Sets the amount of time the preemption tone plays on the
                                          						called phone when a lower precedence call is being preempted.

## mlpp max-precedence

To set the maximum precedence (priority) level that a phone user can
                              		  specify when making an MLPP call, use the mlpp max-precedence command in ephone-template or voice-port configuration mode. To
                              		  reset to the default, use the no form of this command.

mlpp max-precedence number

no mlpp max-precedence

### Syntax Description

number

Number representing the maximum precedence level. Range:
                                          						0 to 4, where 0 is the highest priority. Default: 4.

### Command Default

The MLPP precedence is 4 (routine).

### Command Modes

Ephone-template configuration (config-ephone-template) Voice-port configuration (config-voiceport)

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

This command sets the maximum precedence level that a user can select
                              		  when making MLPP calls from a phone. The phone user can specify a precedence
                              		  level that is less than or equal to this value. Cisco Unified CME rejects the
                              		  call if a user selects a precedence level that is higher than the level set
                              		  with this command and the user receives an error tone.

Emergency 911 calls are automatically assigned precedence level 0.

To apply a template to an SCCP phone, use the ephone-template command.

## Examples

The following example shows the precedence level set to 0 in template
                              		  5 and applied to phone 12:

```
ephone-template  5
 mlpp max-precedence 0
!
!
ephone  12
 mac-address 000F.9054.31BD
 ephone-template 5
 type 7960
 button  1:12
```

### Related Commands

Command

Description

access-digits

Defines the access digit that phone users dial to request a
                                          						precedence call.

ephone-template (ephone)

Applies an ephone template to an SCCP phone.

mlpp indication

Enables MLPP indication on an SCCP phone or analog FXS
                                          						port.

mlpp preemption

Enables the preemption capability on an SCCP phone or
                                          						analog FXS port.

## mlpp preemption

To enable calls on an SCCP phone or analog FXS port to be preempted,
                              		  use the mlpp preemption command in ephone-template or voice-port configuration mode. To
                              		  disable preemption, use the no form of this command.

mlpp preemption

no mlpp preemption

### Syntax Description

This command has no arguments or keywords.

### Command Default

Preemption is enabled on the phone.

### Command Modes

Ephone-template configuration (config-ephone-template) Voice-port configuration (config-voiceport)

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

The command allows an SCCP IP phone or an FXS analog phone to have
                              		  its calls preempted if it is busy with lower precedence calls.

A phone with preemption disabled can still receive precedence calls
                              		  in an MLPP network, but the phone itself does not get preempted. The
                              		  preemption-disabled phone can be connected to a call that is preempted (at
                              		  another device), in which case, that device receives preemption.

To apply a template to an SCCP phone, use the ephone-template command in ephone
                              		  configuration mode.

## Examples

The following example shows preemption disabled in template 5 and
                              		  applied to phone 12:

```
ephone-template  5
 mlpp max-precedence 0
 no mlpp preemption
!
!
ephone  12
 mac-address 000F.9054.31BD
 ephone-template 5
 type 7960
 button  1:12
```

### Related Commands

Command

Description

ephone-template (ephone)

Applies an ephone template to an SCCP phone.

mlpp indication

Enables MLPP indication on an SCCP phone or analog FXS
                                          						port.

mlpp max-precedence

Sets the maximum precedence (priority) level that a phone
                                          						user can specify when making an MLPP call.

preemption tone timer

Defines the expiry time for the preemption tone for the
                                          						call being preempted.

## mlpp service-domain

To set the service domain and maximum precedence (priority) level for
                              		  Multilevel Precedence and Preemption (MLPP) calls, use the mlpp service-domain command in ephone-template or voice-port configuration mode. To
                              		  reset to the default, use the no form of this command.

mlpp service-domain { drsn | dsn } identifier domain-number max-precedence level

no mlpp service-domain

### Syntax Description

drsn

Phone belongs to Defense Red Switched Network (DRSN).

dsn

Phone belongs to Defense Switched Network (DSN).

domain-number

Number to identify the domain, in three-octet format.
                                          						Range: 0x000000 to 0xFFFFFF.

level

Number representing the maximum precedence level, where 0
                                          						is the highest priority. Range is 0 to 4 (DSN) or 0 to 5 (DRSN).

### Command Default

Phone uses global default configured with the service-domain command.

### Command Modes

Ephone-template configuration (config-ephone-template) Voice-port configuration (config-voiceport)

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

This command sets the MLPP domain type and number for the phone, and
                              		  the maximum precedence level that a user can select when making MLPP calls from
                              		  the phone.

The phone user can select a precedence level that is less than or
                              		  equal to the value set with this command. Cisco Unified CME rejects the call if
                              		  a user selects a precedence level that is higher than the level set with this
                              		  command and the user receives an error tone.

If this command and the service-domain command are not enabled, the
                              		  phone cannot make MLPP calls.

Emergency 911 calls are automatically assigned precedence level 0.

To apply a template to an SCCP phone, use the ephone-template command.

## Examples

The following example shows the precedence level set to 1 in template
                              		  5 and applied to phone 15:

```
ephone-template  5
 mlpp service-domain dsn identifier 000010 max-precedence 1
!
!
ephone  15
 mac-address 000F.9054.31BD
 ephone-template 5
 type 7960
 button  1:15
```

### Related Commands

Command

Description

access-digit

Defines the access digit that phone users dial to request a
                                          						precedence call.

ephone-template (ephone)

Applies an ephone template to an SCCP phone.

mlpp indication

Enables MLPP indication on an SCCP phone or analog FXS
                                          						port.

mlpp preemption

Enables the preemption capability on an SCCP phone or
                                          						analog FXS port.

service-domain

Sets the global MLPP domain name and number.

## mobility (ephone-dn)

To enable the Mobility feature on an extension of an SCCP IP phone,
                              		  use the mobility command in ephone-dn configuration mode. To disable mobility on
                              		  the extension, use the no form of this command.

mobility

no mobility

### Syntax Description

This command has no arguments or keywords.

### Command Default

Mobility is not enabled for the extension.

### Command Modes

Ephone-dn configuration (config-ephone-dn)

## Command History

Release

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

This command enables the Mobility feature on the extension, which is
                              		  required to enable the Single Number Reach (SNR) feature.

## Examples

The following example shows extension 1001 is enabled for SNR. After
                              		  a call rings at this number for 5 seconds, the call also rings at the remote
                              		  number 4085550133. If the call is not answered after 20 seconds, the call no
                              		  longer rings the phone and is forwarded to the voice-mail number 2001.

```
ephone-dn 10
 number 1001
 mobility
 snr 4085550133 delay 5 timeout 15 cfwd-noan 2001
```

### Related Commands

Command

Description

number

Associates a telephone or extension number with an
                                          						ephone-dn.

snr

Enables Single Number Reach on an extension of an SCCP IP
                                          						phone.

softkeys connected

Modifies the order and type of soft keys that display on an
                                          						IP phone during the connected call state.

softkeys idle

Modifies the order and type of soft keys that display on an
                                          						IP phone during the idle call state.

## mobility (voice register dn)

To enable the Mobility feature on an extension of a Cisco Unified SIP
                              		  IP phone, use the mobility command in voice register dn
                              		  configuration mode. To disable the Mobility feature on the extension, use the no form of this command.

mobility

no mobility

### Syntax Description

This command has no arguments or keywords.

### Command Default

The Mobility feature is not enabled on the extension of a Cisco
                              		  Unified SIP IP phone.

### Command Modes

Voice register dn configuration (config-register-dn)

## Command History

Release

Modification

15.2(2)T

This command was introduced.

### Usage Guidelines

Use the mobility command to enable a Cisco Unified
                              		  SIP IP phone to receive calls on an extension, which is required to enable the
                              		  Single Number Reach (SNR) feature.

## Examples

The following example shows how to enable the Mobility feature on
                              		  directory number 25:

```
Router(config)# voice register dn 25 Router(config-register-dn)# mobility
```

### Related Commands

Command

Description

snr (voice register dn)

Enables the SNR feature on an extension of a Cisco Unified
                                          						SIP IP phone.

## mode

The mode command under voice register global allows you to select the operating mode for Cisco Unified Call Manager Express and Cisco
                              Unified Survivable Remote Site Telephony. The default operation for voice register global is SRST mode, which may be selected
                              using the no form of this command.

mode [ cme | cme-app | esrst ]

no mode

### Syntax Description

cme

CME mode provides the options to configure SIP phones and features.

cme-app

CME appliance mode provides the options to configure up to 200 SIP phones for routers that are only being used to provide
                                          call control. CME appliance mode is available only for ISR4321 routers.

esrst

E-SRST mode extends SRST features to include the static configuration of SIP phones and features.

### Command Default

Default is SIP
                              		  SRST mode.

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
                                          						CME 3.4 Cisco SIP SRST

This
                                          						command was introduced.

15.3(3)M

Cisco
                                          						CME 10.0

This
                                          						command was modified to add the esrst mode.

Cisco
                                          						IOS XE Everest 16.5.1b

Unified CME 11.7

Unified SRST 11.7

The behavior of no form of this command was modified, to clear all voice register pools and voice register dns, along with mode-specific configurations.

Cisco IOS XE Amsterdam 17.2.1r

Unified CME 12.8

The cme-app mode was added for ISR4321 routers, allowing the configuration of up to 200 phones (For routers dedicated to CME use only).

### Usage Guidelines

The mode command selects the SIP call control application to be used and enables associated configuration commands. By default,
                              the router operates in SRST mode, allowing only phones failing over from Unified Communications Manager to register. Enter cme or cme-app modes to configure SIP phones and features for standalone call control use.

E-SRST mode provides a hybrid of these applications, where CME features may be configured to complement the SRST application.

For releases prior to Unified CME/SRST 11.7, the no form of this command clears only the mode-specific configurations (For example, source-address under voice register global configuration, and user credentials configured under voice register pool configuration). From
                              Cisco IOS XE Everest 16.5.1 (Unified CME/SRST Release 11.7) onwards, the no form of this command clears all the voice register pools and voice register dns, along with mode-specific configurations.

## Examples

The following
                              		  example shows how to set the mode to Cisco CME:

```
Router(config)# voice register global Router(config-register-global)# mode cme
```

### Related Commands

Description

show voice register global

Displays all global configuration information that is associated with SIP phones.

## moh (ephone-dn)

To enable music on hold (MOH) from an external live audio feed
                              		  (standard line-level audio connection) connected directly to the router by an
                              		  foreign office exchange (FXO) or an E&M analog voice port, use the moh command in ephone-dn configuration mode.
                              		  To disable MOH from a live feed or to disable the outcall number or multicast
                              		  capability, use the no form of this command.

moh [ out-call outcall-number ] [ ip ip-address port port-number [ route ip-address ]]

no moh [ out-call outcall-number | ip ]

### Syntax Description

out-call outcall-number

(Optional) Sets up a call to the outcall number in order to
                                          						connect to the MOH feed. If this keyword is not used, the live feed is assumed
                                          						to derive from an incoming call to the ephone-dn under which this command is
                                          						used.

ip ip-address

(Optional) Indicates that this audio stream is to be used
                                          						as a multicast source as well as the MOH source and specifies the destination
                                          						IP address for multicast.

port port-number

(Optional) Specifies the media port for multicast. Range is
                                          						from 2000 to 65535. Port 2000 is recommended because this port is already used
                                          						for normal Real-Time Transport Protocol (RTP) media transmissions between IP
                                          						phones and the Cisco CallManager Express router.

route ip-address

(Optional) Indicates the specific router interface on which
                                          						to transmit the IP multicast packets. The default is that the MOH multicast
                                          						stream is automatically output on the interface that corresponds to the address
                                          						that was configured with the ip source-address command.

### Command Default

MOH is disabled on an extension.

### Command Modes

Ephone-dn configuration (config-ephone)

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

12.2(15)ZJ

Cisco CME 3.0

The ip , port , and route keywords were added.

12.3(4)T

Cisco CME 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

This command takes the specified live-feed audio stream and uses it
                              		  as MOH for a Cisco Unified CME system. The connection for the live-feed audio
                              		  stream is established as an automatically connected voice call. If the out-call keyword is used, the type of
                              		  connection can include VoIP calls if voice activity detection (VAD) is
                              		  disabled. The typical operation is for the MOH ephone-dn to establish a call to
                              		  a local router E&M voice port.

Connection via E&M is the recommended mechanism because it
                              		  requires minimal external components. The E&M port must be placed in 4-wire
                              		  operation, using E&M immediate signaling and with the auto-cut-through option enabled. You directly
                              		  connect a line-level audio feed (standard audio jack) to pins 3 and 6 of an
                              		  E&M RJ-45 connector. The E&M WAN interface card (WIC) has a built-in
                              		  audio transformer that provides appropriate electrical isolation for the
                              		  external audio source. (The audio connection on the E&M port does not
                              		  require loop current.) The signal immediate and auto-cut-through commands disable E&M
                              		  signaling on this voice port. A G.711 audio packet stream is generated by the
                              		  digital signal processor (DSP) on the E&M port.

If you are using an FXO voice port for live-feed MOH instead of an
                              		  E&M port, connect the MOH source to the FXO voice port. This connection
                              		  requires an external adapter to supply normal telephone company (telco) battery
                              		  voltage with the correct polarity to the tip-and-ring leads of the FXO port.
                              		  The adapter must also provide transformer-based isolation between the external
                              		  audio source and the tip-and-ring leads of the FXO port.

Music from a live feed is continuously fed into the MOH playout
                              		  buffer instead of being read from an audio file in flash memory. There is
                              		  typically a two-second delay with live-feed MOH.

If the out-call keyword is used, an outbound call to
                              		  the MOH live-feed source is attempted (or reattempted) every 30 seconds until
                              		  the call is connected to the ephone-dn (extension) that has been configured for
                              		  MOH. Note that this ephone-dn is not associated with any physical phone.

If the moh (ephone-dn) command is used without any
                              		  keywords or arguments, the ephone-dn will accept an incoming call and use the
                              		  audio stream from the call as the source for the MOH stream, displacing any
                              		  audio stream that is available from a flash file. To accept an incoming call,
                              		  the ephone-dn must have an extension or phone number configured for it. A
                              		  typical usage would be for an external H.323-based server device to call the
                              		  ephone-dn to deliver an audio stream to the Cisco CME system. Normally, only a
                              		  single ephone-dn would be configured like this. If there is more than one
                              		  ephone configured to accept incoming calls for MOH, the first ephone-dn that is
                              		  successfully connected to a call (incoming or outgoing) is the MOH source for
                              		  the system.

MOH can also be derived from an audio file when you use the moh command in telephony-service
                              		  configuration mode with the filename argument. There can be only one MOH stream at a time in
                              		  a Cisco CME system, and if both an audio file and a live feed have been
                              		  specified for the MOH stream, the router seeks the live feed from the moh (ephone-dn) command first. If the live feed is
                              		  found, the router displaces the audio file source. If the live feed is not
                              		  found or fails at any time, the router falls back to the audio file source that
                              		  was specified in the moh (telephony-service) command.

If you use the ip keyword to specify a multicast address in
                              		  this command, the audio stream is sent to the multicast address in addition to
                              		  serving as the MOH source. Additionally, if you specify a different multicast
                              		  address using the multicast moh command under telephony-service configuration
                              		  mode, the audio stream is also sent to the multicast address that you named in
                              		  that command. It is therefore possible to send the live-feed audio stream to
                              		  MOH and to two different multicast addresses: the one that is directly
                              		  configured under the moh (ephone-dn) command and the one that is indirectly
                              		  configured under the multicast moh (telephony-service) command.

A related command, the feed command, provides the ability to
                              		  multicast an audio stream that is not the MOH audio stream.

## Examples

The following example establishes a live music-on-hold source by
                              		  setting up a call to extension 7777:

```
Router(config)# ephone-dn 55 Router(config-ephone-dn)# moh out-call 7777
```

### Related Commands

Description

auto-cut-through

Enables call completion when an M-lead response is not
                                          						provided.

ephone-dn

Enters ephone-dn configuration mode to set directory
                                          						numbers and parameters for individual Cisco IP phone extensions.

feed

Enables multicast of an audio stream that is different from
                                          						the music-on-hold audio stream.

ip source-address

Identifies the IP address and port through which IP phones
                                          						communicate with a Cisco CME router.

moh (telephony-service)

Enables music on hold from an audio file.

multicast moh

Enables multicast of the music-on-hold audio stream.

signal

Specifies the type of signaling for a voice port.

## moh (telephony-service)

To generate an audio stream from a file for music on hold (MOH) in a
                              		  Cisco CallManager Express (Cisco CME) system, use the moh command in telephony-service
                              		  configuration mode. To disable the MOH audio stream from this file, use the no form of this command.

moh filename

no moh

### Syntax Description

filename

Name of the audio file to use for the MOH audio stream. The
                                          						file must be copied to flash memory on the Cisco CME router.

### Command Default

Tone on hold (a periodic beep is played to the caller)

### Command Modes

Telephony-service configuration (config-telephony)

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

This command enables MOH from .au and .wav format music files. MOH is
                              		  played for G.711 callers and on-net VoIP and PSTN callers who are on hold in a
                              		  Cisco CME system. Local callers within a Cisco CME system hear a repeating tone
                              		  while they are on hold.

Audio files that are used for MOH must be copied to the Cisco CME
                              		  router flash memory. A MOH file can be in .au or .wav file format; however, the
                              		  file format must contain 8-bit 8-kHz data in A-law or mu-law data format. We
                              		  recommend using a moh-file size greater than 100 KB.

If you want to replace or modify the audio file that is currently
                              		  specified, you must first disable the MOH capability using the no moh command. The following example replaces file1
                              		  with file2:

```
Router(config-telephony)# moh file1 Router(config-telephony)# no moh Router(config-telephony)# moh file2
```

If you specify a second file without first removing the original
                              		  file, the MOH mechanism stops working and may require a router reboot to clear
                              		  the problem.

A related command, the moh command in ephone-dn configuration mode,
                              		  can be used to establish a MOH audio stream from a live feed. If you configure
                              		  both commands, MOH falls back to playing music from the audio file if the live
                              		  music feed is interrupted.

The multicast moh command allows you to use the MOH stream for a
                              		  multicast broadcast.

When the multicast moh and debug ephone moh commands are both enabled, if you also use the no moh command, the debug output can be excessive and
                              		  flood the console. Multicast MOH should be disabled before using the no moh command when the debug ephone moh command is enabled.

## Examples

The following example enables music on hold and specifies a music
                              		  file:

```
Router(config)# telephony-service Router(config-telephony)# moh minuet.wav
```

### Related Commands

Description

debug ephone moh

Displays diagnostic information for music on hold.

moh (ephone-dn)

Enables music on hold from a live audio feed.

multicast moh

Enables multicast of the music-on-hold audio stream.

## moh (voice moh-group)

To enable music on hold (MOH) for a MOH group, use the moh command in voice moh-group configuration
                              		  mode. To disable music on hold, use the no form of this command.

moh filename

no moh filename

### Syntax Description

filename

Name of the music file. The music file must be in the
                                          						system flash.

### Command Default

No MOH is enabled

### Command Modes

Voice moh-group configuration (config-voice-moh-group)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.0(1)XA

Cisco Unified CME/SRST/SIP SRST 8.0

This command was introduced.

15.1(1)T

Cisco Unified CME/SRST/SIP SRST 8.0

This command was integrated into Cisco IOS Release
                                          						15.1(1)T.

### Usage Guidelines

The moh command allows you to specify the .au and
                              		  .wav format music files that are played to callers who have been put on hold.
                              		  MOH works only for G.711 calls and on-net VoIP and PSTN calls. For all other
                              		  calls, callers hear a periodic tone. You must provide the directory and
                              		  filename of the MOH file in URL format. For example: moh flash:/minuet.au

## Examples

The following example enables MOH for voice moh group 1 and specifies
                              		  the music files:

```
Router(config)# 
Router(config)#voice moh-group 1
Router(config-voice-moh-group)# moh flash:/minuet.wav
```

### Related Commands

voice moh-group

Enters voice moh-group configuration mode.

extension-range

Defines extension range for a clients calling a
                                          						voice-moh-group.

moh

Enables music on hold from a flash audio file.

multicast moh

Enables multicast of the music-on-hold audio stream.

## moh-file-buffer

To specify a MOH file buffer size, use the moh-file-buffer command in telephony-service configuration mode. To delete the
                              		  moh-file-buffer size, use the no form of this command.

moh-file-buffer file-size

no moh-file-buffer

### Syntax Description

file-size

Specifies a numeric value for the buffer MOH file size
                                          						between 64 KB and 10000 KB.

### Command Default

No moh-file-buffer is configured.

### Command Modes

Telephony-service configuration (config-telephony-service)

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

This command allows to set a buffer MOH file size limit for new MOH
                              		  files. You can allocate a MOH file buffer size between 64 KB (8 seconds ) and
                              		  10000 KB (20 minutes, approximately). A large buffer size is desirable to cache
                              		  the largest MOH file and better MOH performance. During memory allocation the
                              		  buffer size is aligned to 16KB.

The default maximum file buffer size is 64 KB. If the MOH file size
                              		  is too large, it cannot be cached and the buffer size falls back to 64 KB.

## Examples

The following example shows a moh-file-buffer size of 180 KB assigned
                              		  for future moh files under the telephony-service configuration mode.

```
!
!
!
telephony service
 max-conferences 8 gain -6
 transfer-system full-consult
 moh-file-buffer 180
!
!
line con 0
 exec-timeout 0 0
line aux 0
```

### Related Commands

Command

Description

voice-moh-group

Enter voice-moh-group configuration mode.

moh filename

Enables music on hold from a flash audio feed

multicast moh

Enables multicast of the music-on-hold audio stream.

extension-range

Specifies the extension range for a clients calling a
                                          						voice-moh-group.

## moh-group (ephone-dn)

To assign a MOH group to a directory number, use the moh-group command in ephone-dn configuration mode. To remove the MOH
                              		  group, use the no form of this command.

moh-group tag

no moh-group tag

### Syntax Description

tag

A unique number that identifies a MOH group. Range is from
                                          						1 to 5.

### Command Default

No MOH group is configured.

### Command Modes

Ephone-dn configuration (config-ephone-dn )

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

Use this command to assign a MOH group to a directory number in
                              		  ephone-dn configuration mode. Use the number tag from 1 to 5 to specify the MOH
                              		  group that you want to assign to this directory number.

## Examples

The following example shows how to assign a MOH group to a directory
                              		  number under ephone-dn mode.

```
Router(config)# ephone-dn 98 Router(config-ephone-dn)#moh-group 1
Router(config-ephone-dn)#
```

### Related Commands

description

Displays a brief description about a voice moh-group in
                                          						use.

extension-range

Defines extension range for a clients calling a
                                          						voice-moh-group.

moh

Enables music on hold from a flash audio feed.

multicast moh

Enables multicast of the music-on-hold audio stream.

## mtp

To send voice packets from an IP phone to the Cisco Unified CME
                              		  router, use the mtp command in ephone or ephone-template
                              		  configuration mode. To return to the default, use the no form of this command.

mtp { video-only | both }

no mtp { video-only | both }

### Syntax Description

video-only

Specifies that the video streams must be sent through the
                                          						Cisco Unified CME route.

both

Specifies that both voice and video streams must be sent
                                          						through the Cisco Unified CME route.

### Command Default

If no arguments are given, only voice packets are sent to the router.

An IP phone in a call with another IP phone in the same Cisco Unified
                              		  CME system sends voice and video packets directly to the other phone.

### Command Modes

Ephone configuration (config-ephone) Ephone-template configuration (config-ephone-template)

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

15.1(4)M

Cisco Unified CME 8.6

Support for choosing video streams was added.

### Usage Guidelines

Normally, media packets (RTP packets) that are sent between IP phones
                              		  in the same Cisco Unified CME system go directly to the other phone and do not
                              		  travel through the Cisco Unified CME router. When these packets are sent from a
                              		  remote IP phone to another IP phone in the same Cisco Unified CME system, they
                              		  may be obstructed by a firewall. The mtp command instructs a phone to always send
                              		  its media packets to the Cisco Unified CME router, which acts as a proxy and
                              		  forwards the packets to the destination. Firewalls can then be easily
                              		  configured to pass the RTP packets because the router uses a specified UDP port
                              		  for media packets. In this way, RTP packets from remote IP phones can be
                              		  delivered to IP phones on the same system. The default is that this function is
                              		  off and that RTP packets that are sent from one IP phone to another IP phone in
                              		  the same Cisco Unified CME system go directly to the other phone.

If you use an ephone template to apply a command to a phone and you
                              		  also use the same command in ephone configuration mode for the same phone, the
                              		  value that you set in ephone configuration mode has priority.

## Examples

The following example sends video and audio packets from ephone 437
                              		  to the Cisco Unified CME router for all calls:

```
ephone 437
 button 1:29
 mtp both
```

### Related Commands

Command

Description

ephone-template (ephone)

Applies template to ephone being configured.

## mtu (vpn-profile)

To enter the mtu value in bytes, use the mtu command in vpn-profile configuration mode.

mtu bytes

### Syntax Description

bytes

Mtu value, in bytes. Range: 256 to 1406. Default: 1290.

### Command Default

Default is 1290 bytes.

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

Use the mtu command to define a value in bytes.. The mtu value ranges
                              		  from 256 to 1406 bytes. The defaul value is 1290 bytes.

## Examples

The following example shows the mtu value set to 1300 bytes in
                              		  vpn-profile 2:

```
Router# show run
!
!
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
!
voice register global
 max-pool 10
```

### Related Commands

Command

Description

vpn-profile

Defines a VPN-profile.

## multicast moh

To use the music-on-hold (MOH) audio stream as a multicast source for
                              		  Cisco Unified CME or for a MOH group, use the multicast moh command in telephony-service configuration
                              		  mode or in voice-moh-group configuration modep. To disable multicast use of the
                              		  MOH stream, use the no form of this command.

multicast moh ip-address port port-number [ route ip-address-list ]

no multicast moh

### Syntax Description

ip-address

Specifies the destination IP address for multicast.

port port-number

Specifies the media port for multicast. Range is from 2000
                                          						to 65535. Port 2000 is recommended because this port is already used for normal
                                          						Real-Time Transport Protocol (RTP) media transmissions between IP phones and
                                          						the Cisco CME router.

route ip-address-list

(Optional) Indicates specific router interfaces over which
                                          						to transmit the IP multicast packets. Up to four IP addresses can be listed,
                                          						each separated from the other by a space. The default is that the MOH multicast
                                          						stream is automatically output on the interfaces that correspond to the address
                                          						that was configured with the ip source-address command.

### Command Default

No multicast is enabled.

### Command Modes

Telephony-service configuration (config-telephony) Voice-moh-group configuration (config-voice-moh-group)

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

15.0(1)XA

Cisco Unified CME 8.0

This command was modified. Multicast MOH was enabled under
                                          						voice moh-group configuration mode.

15.1(1)T

Cisco Unified CME 8.0

This command was integrated into Cisco IOS Release
                                          						15.1(1)T.

### Usage Guidelines

This command enables multicast of the audio stream that is designated
                              		  for MOH in a Cisco CME system. Use this command in voice moh-group
                              		  configuration mode to enable multicast of audio stream for a specific MOH
                              		  group.

A related command, the moh (ephone-dn) command, creates a MOH audio stream
                              		  from an external live feed and optionally enables multicast on that stream.
                              		  These two commands can be used concurrently to provide multicast of a live-feed
                              		  MOH audio stream to two different multicast addresses.

Another related command, the feed command, enables multicast of an audio
                              		  stream that is not the MOH audio stream.

When the multicast moh and debug ephone moh commands are both enabled, if you also use the no moh command, the debug output can be excessive and
                              		  flood the console. Multicast MOH should be disabled before using the no moh command when the debug ephone moh command is enabled.

## Examples

The following example enables multicast of the MOH audio stream at
                              		  multicast address 239.10.16.4 and names two router interfaces over which to
                              		  send the multicast packets.

Example 1: Multicast enabled for MOH audio stream under telephony
                              		  service.

```
Router(config)# telephony-service Router(config-telephony)# moh minuet.au Router(config-telephony)# multicast moh 239.10.16.4 port 2000 route 10.10.29.17 10.10.29.33
```

Example 2: Multicast enabled for MOH audio stream under voice
                              		  moh-group configuration mode.

```
Router(config)# voice-moh-group 1 Router(config-voice-moh-group)# moh minuet.au Router(config-voice-moh-group)# multicast moh 239.10.16.4 port 2000 route 10.10.29.17 10.10.29.33
```

### Related Commands

Command

Description

feed

Enables multicast of an audio stream that is not the
                                          						music-on-hold audio stream.

ip source-address

Identifies the IP address and port through which IP phones
                                          						communicate with a Cisco CME router.

moh (ephone-dn)

Enables music on hold from a live audio feed.

moh (telephony-service)

Enables music on hold from an audio file.

voice moh-group

Enters voice moh-group configuration mode

## mwi (ephone-dn and ephone-dn-template)

To enable a specific Cisco Unified IP phone extension to receive
                              		  message-waiting indication (MWI) notification from an external voice-messaging
                              		  system, use the mwi command in ephone-dn or
                              		  ephone-dn-template configuration mode. To disable this feature, use the no form of this command.

mwi { off | on | on-off }

no mwi { off | on | on-off }

### Syntax Description

off

Sets a Cisco Unified IP phone extension to process MWI to
                                          						OFF, using either the main or secondary phone number.

on

Sets a Cisco Unified IP phone extension to process MWI to
                                          						ON, using either the main or secondary phone number.

on-off

Sets a Cisco Unified IP phone extension to process MWI to
                                          						both ON and OFF, using either the main or secondary phone number.

### Command Default

MWI notification is disabled on an extension.

### Command Modes

Ephone-dn configuration (config-ephone-dn) Ephone-dn-template configuration (config-ephone-dn-template)

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

This command was made available in ephone-dn-template
                                          						configuration mode.

12.4(9)T

Cisco Unified CME 4.0

This command in ephone-dn-template configuration mode was
                                          						integrated into Cisco IOS Release 12.4(9)T.

### Usage Guidelines

This command enables a Cisco Unified IP phone extension to receive
                              		  MWI notification from an external voice-messaging system for all the Cisco
                              		  Unified IP phones connected to the Cisco Unified CME router. This extension is
                              		  a “dummy” extension and is not associated with any physical phone. The external
                              		  voice-messaging system is able to communicate MWI status by making telephone
                              		  calls to the dummy extension number, with the MWI information embedded in
                              		  either the called or calling-party IP phone number.

This command cannot be used unless the number command is already configured for this
                              		  extension (ephone-dn).

If you use an ephone-dn template to apply a command to an ephone-dn
                              		  and you also use the same command in ephone-dn configuration mode for the same
                              		  ephone-dn, the value that you set in ephone-dn configuration mode has priority.

## Examples

The following example sets MWI to on:

```
Router(config)# ephone-dn 1 Router(config-ephone-dn) number 8000 Router(config-ephone-dn) mwi on
```

The following example sets MWI to off:

```
Router(config)# ephone-dn 2 Router(config-ephone-dn) number 8001 Router(config-ephone-dn) mwi off
```

The following example sets MWI to both on and off for the primary and
                              		  secondary number, where the MWI information is embedded in the calling-party
                              		  number. A call placed by the voice-mail system to 8002 turns on the MWI light
                              		  for the extension number indicated by the calling-party number for the MWI
                              		  call. A call placed to 8003 turns off the MWI light.

```
Router(config)# ephone-dn 3 Router(config-ephone-dn) number 8002 secondary 8003 Router(config-ephone-dn) mwi on-off
```

The following example sets MWI to both on and off for the primary and
                              		  secondary number, where the MWI information is embedded in the called-party
                              		  number. A call placed by the voice-mail system to 8000*5001*1 turns on the MWI
                              		  light for extension 5001. A call placed to 8000*5001*2 turns off the MWI light.

```
Router(config)# ephone-dn 20 Router(config-ephone-dn) number 8000*....*1 secondary 8000*....*2 Router(config-ephone-dn) mwi on-off
```

The following example uses an ephone-dn-template to set MWI to on:

```
Router(config)# ephone-dn-template 4 Router(config-ephone-dn-template) mwi on Router(config-ephone-dn-template)# exit Router(config)# ephone-dn 1 Router(config-ephone-dn)# number 8000 Router(config-ephone-dn)# ephone-dn-template 4
```

### Related Commands

Description

ephone-dn-template (ephone-dn)

Applies template to ephone-dn being configured.

mwi expires

Sets the expiration timer for registration for either the
                                          						client or the server.

mwi sip (ephone-dn)

Subscribes an extension in a Cisco Unified CME router to
                                          						receive MWI notification from a SIP MWI server.

mwi sip-server (telephony-service)

Configures the IP address and port number for an external
                                          						SIP-based MWI server.

number

Associates a telephone or extension number with an
                                          						extension (ephone-dn) in a Cisco Unified CME system.

## mwi (voice register dn)

To enable a specific Cisco IP phone extension (directory number)
                              		  associated with a SIP phone to receive message-waiting indication (MWI)
                              		  notification, use the mwi command in voice register dn
                              		  configuration mode. To return to the default, use the no form of this command.

mwi

no mwi

### Syntax Description

This command has no arguments or keywords.

### Command Default

This command is disabled

### Command Modes

Voice register dn configuration (config-register-dn)

## Command History

Cisco IOS Release

Version

Modification

12.4(4)T

Cisco CME 3.4

This command was introduced.

### Usage Guidelines

This command enables a particular extension on a SIP IP phone to
                              		  receive MWI notification.

For Cisco Unified CME 4.1 and later versions, MWI requires that SIP
                              		  phones must be configured with a directory number by using
                              		  the number (voice register pool) command with the dn
                              		  keyword; direct line numbers are not supported.

## Examples

The following example shows how to enable MWI for a particular
                              		  extension number associated with a SIP IP phone:

```
Router(config)# voice register dn 4 Router(config-register-dn)# mwi
```

### Related Commands

Description

number (voice register pool)

Configures number patterns for a voice register pool.

## mwi expires

To set the expiration timer for registration for the message-waiting
                              		  indication (MWI) client or server, use the mwi expires command in telephony-service configuration
                              		  mode. To disable the timer, use the no form of this command.

mwi expires seconds

no mwi expires seconds

### Syntax Description

seconds

Expiration time, in seconds. Range is from 600 to 99999.
                                          						Default is 86400 (24 hours).

### Command Default

Default is 86400 seconds (24 hours).

### Command Modes

Telephony-service configuration (config-telephony)

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

## Examples

The following example sets the expiration timer to 1000 seconds:

```
Router(config)# telephony-service Router(config-telephony)# mwi expires 1000
```

### Related Commands

Description

mwi relay (telephony-service)

Enables the Cisco CME router to relay MWI information to
                                          						remote Cisco IP phones.

mwi sip-server (telephony-service)

Configures the IP address and port number for the external
                                          						SIP-based MWI server.

## mwi prefix

To specify a prefix for an extension that will receive unsolicited
                              		  message-waiting indication (MWI) from an external SIP-based MWI server, use the mwi prefix command in telephony-service configuration
                              		  mode. To return to the default, use the no form of this command.

mwi prefix prefix-string

no mwi prefix

### Syntax Description

prefix-string

Digits at the beginning of a number that will be recognized
                                          						as a prefix before a Cisco Unified CME extension number. The maximum prefix
                                          						length is 32 digits.

### Command Default

A prefix is not defined.

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

Central voice-messaging servers that provide mailboxes for several
                              		  Cisco Unified CME sites may use site codes or prefixes to distinguish among
                              		  similarly numbered ranges of extensions at different sites. In Cisco Unified
                              		  CME 4.0 and later versions, you can specify that your Cisco Unified CME system
                              		  should accept unsolicited SIP Notify messages for message-waiting indication
                              		  (MWI) that include a prefix string as a site identifier.

For example, an MWI message might indicate that the central mailbox
                              		  number 5551234 has a voice message. In this example, the digits 555 are set as
                              		  the prefix string or site identifier using the mwi prefix command. The local Cisco Unified CME system
                              		  is able to convert 5551234 to 1234 and deliver the MWI to the correct phone.
                              		  Without this prefix string manipulation, the system would reject an MWI
                              		  indication for 5551234 as not matching the local Cisco Unified CME extension
                              		  1234.

## Examples

The following example identifies the SIP server for MWI notification
                              		  at the IP address 172.16.14.22. It states that the Cisco Unified CME system
                              		  will accept unsolicited SIP Notify messages for known mailbox numbers
                              		  (extension numbers) that are prefixed with the digits 555.

```
sip-ua
 mwi-server 172.16.14.22 unsolicited
telephony-service
 mwi prefix 555
```

### Related Commands

Description

mwi (ephone-dn and ephone-dn-template)

Configures specific Cisco Unified IP phone directory
                                          						numbers to receive MWI notification from an external voice-mail system.

mwi-server

Configures MWI server parameters.

mwi sip (ephone-dn)

Subscribes an extension in a Cisco Unified CME router to
                                          						receive MWI notification from a SIP MWI server.

## mwi qsig

To enable Cisco Unified CME to interrogate a QSIG message center for
                              		  the message-waiting indication (MWI) status of an IP phone extension, use the mwi qsig command in ephone-dn or ephone-dn-template
                              		  configuration mode. To return to the default, use the no form of this command.

mwi qsig

no mwi qsig

### Syntax Description

This command has no arguments or keywords.

### Command Default

An extension is not subscribed to receive MWI using QSIG.

### Command Modes

Ephone-dn configuration (config-ephone-dn) Ephone-dn-template configuration (config-ephone-dn-template)

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

The transfer-system command must be used with the full-consult or full-blind keyword to enable H.450 call
                              		  forwarding.

If you use an ephone-dn template to apply a command to an ephone-dn
                              		  and you also use the same command in ephone-dn configuration mode for the same
                              		  ephone-dn, the value that you set in ephone-dn configuration mode has priority.

## Examples

In the following example, a voice mail extension (7000) and a normal
                              		  extension (7582) are defined. Calls are forwarded to voice mail when extension
                              		  7582 is busy or does not answer. The message-waiting indicator (MWI) on
                              		  extension 7582’s phone is subscribed to receive notifications from the QSIG
                              		  message center.

```
ephone-dn 25
 number 7582
 mwi qsig
 call-forward busy 7000
 call-forward noan 7000 timeout 20
telephony-service
 voicemail 7000
 transfer-system full-consult
```

### Related Commands

Description

ephone-dn-template (ephone-dn)

Applies a template to ephone-dn being configured.

transfer-system

Specifies the call transfer method for Cisco Unified CME
                                          						extensions.

voicemail

Defines the telephone number that is speed-dialed when the
                                          						Messages button on a Cisco Unified IP phone is pressed.

## mwi reg-e164

To register E.164 numbers rather than extension numbers with a
                              		  Session Interface Protocol (SIP) proxy or registrar, use the mwi reg-e164 command in telephony-service
                              		  configuration mode. To return to the default, use the no form of this command.

mwi reg-e164

no mwi reg-e164

### Syntax Description

This command has no keywords or arguments.

### Command Default

Registering extension numbers with the SIP proxy or registrar.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(11)T7 12.4

Cisco CME 3.3

This command was introduced.

### Usage Guidelines

This command is used when setting up extensions to use an external
                              		  SIP-based message-waiting indication (MWI) server. The mwi-server command in SIP user-agent
                              		  configuration mode specifies other settings for MWI service.

## Examples

The following example specifies that E.164 numbers should be used for
                              		  registration with the SIP proxy or registrar:

```
telephony-service
 mwi reg-e164
```

### Related Commands

Description

mwi-server (SIP user-agent)

Specifies voice-mail server settings on a voice gateway or
                                          						user agent (UA).

## mwi relay

To enable a Cisco CallManager Express (Cisco CME) router to relay
                              		  message-waiting indication (MWI) notification to remote Cisco IP phones, use
                              		  the mwi relay command in telephony-service configuration
                              		  mode. To disable MWI relay, use the no form of this command.

mwi relay

no mwi relay

### Syntax Description

This command has no arguments or keywords.

### Command Default

MWI relay is disabled.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(2)XT

Cisco ITS 2.0

This command was introduced command.

12.2(8)T

Cisco ITS 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						command.

### Usage Guidelines

Use this command to enable the Cisco CME router to relay MWI
                              		  notification to remote Cisco IP phones. The router at the central site acts as
                              		  a notifier after this command is used.

## Examples

The following example enables MWI relay:

```
Router(config)# telephony-service Router(config-telephony)# mwi relay
```

### Related Commands

Description

mwi expires

Sets the expiration timer for registration for the client
                                          						or the server.

show mwi relay clients

Displays registration information for MWI relay clients.

## mwi sip

To subscribe an extension in a Cisco Unified CME system to receive
                              		  message-waiting indication (MWI) from a SIP-based MWI server, use the mwi sip command in ephone-dn or ephone-dn-template
                              		  configuration mode. To remove the configuration, use the no form of this command.

mwi sip

no mwi sip

### Syntax Description

This command has no arguments or keywords.

### Command Default

An extension is not subscribed to receive MWI.

### Command Modes

Ephone-dn configuration (config-ephone-dn) Ephone-dn-template configuration (config-ephone-dn-template)

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

This command was made available in ephone-dn-template
                                          						configuration mode.

12.4(9)T

Cisco Unified CME 4.0

This command in ephone-dn-template configuration mode was
                                          						integrated into Cisco IOS Release 12.4(9)T.

### Usage Guidelines

Use this command to subscribe an extension in a Cisco Unified CME
                              		  router to receive MWI notification from a SIP-based MWI server, and use the mwi sip-server command to specify the IP address and
                              		  port number for the external SIP-based MWI server. This function integrates a
                              		  Cisco Unified CME router with a SIP-protocol-based MWI service.

If you use an ephone-dn template to apply a command to an ephone-dn
                              		  and you also use the same command in ephone-dn configuration mode for the same
                              		  ephone-dn, the value that you set in ephone-dn configuration mode has priority.

## Examples

The following example subscribes extension 5001 to receive MWI
                              		  notification from an external Session Initiation Protocol (SIP) MWI server and
                              		  requests the SIP MWI server to send MWI notification messages through SIP to
                              		  the Cisco Unified CME router for extension 5001:

```
Router(config) ephone-dn 1 Router(config-ephone-dn) number 5001 Router(config-ephone-dn) name MWI Router(config-ephone-dn) mwi sip Router(config) telephony-service Router(config-telephony) mwi sip-server 172.30.0.5
```

### Related Commands

Description

ephone-dn

Enters ephone-dn configuration mode.

ephone-dn-template (ephone-dn)

Applies a template to an ephone-dn configuration.

mwi sip-server (telephony-service)

Configures the IP address and port number for the external
                                          						SIP-based MWI server.

show mwi relay clients

Displays registration information for MWI relay clients.

## mwi sip-server

To configure parameters associated with an external SIP-based
                              		  message-waiting indication (MWI) server, use the mwi sip-server command in telephony-service
                              		  configuration mode. To disable MWI server functionality, use the no form of this command.

mwi sip-server ip-address [ transport tcp | transport udp ] [ port port-number ] [ reg-e164 ] [ unsolicited [ prefix prefix-string ]]

no mwi sip-server ip-address [ transport tcp | transport udp ] [ port port-number ] [ reg-e164 ] [ unsolicited [ prefix prefix-string ]]

### Syntax Description

ip-address

IP address of the MWI server.

transport tcp

(Optional) Selects TCP as the transport layer protocol.
                                          						This is the default transport protocol.

transport udp

(Optional) Selects UDP as the transport layer protocol. The
                                          						default if these keywords are not used is TCP.

port port-number

(Optional) Specifies port number for the MWI server. Range
                                          						is from 2000 to 9999. Default is 5060 (SIP standard port).

reg-e164

(Optional) Registers an E.164 number with a Session
                                          						Interface Protocol (SIP) proxy or registrar rather than an extension number.
                                          						Registering with an extension number is the default.

unsolicited

(Optional) Sends SIP Notify message for MWI without any
                                          						need to send a Subscribe message from the Cisco Unified CME router.

prefix prefix-string

(Optional) Allows the specified digits to be present before
                                          						a recognized Cisco Unified CME extension number. The maximum prefix length is
                                          						32 digits.

### Command Default

An external SIP-based MWI server is not defined.

### Command Modes

Telephony-service configuration (config-telephony)

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

12.2(15)ZJ

Cisco CME 3.0

The unsolicited keyword was added.

12.3(4)T

Cisco CME 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

12.4(4)XC

Cisco Unified CME 4.0

The prefix prefix-string keyword-argument pair
                                          						was added.

12.4(9)T

Cisco Unified CME 4.0

This command with the prefix prefix-string keyword-argument pair
                                          						was integrated into Cisco IOS Release 12.4(9)T.

### Usage Guidelines

Use this command to configure the IP address of an external SIP MWI
                              		  server. This IP address is used with the mwi sip (ephone-dn) command to subscribe individual
                              		  ephone-dn extension numbers to the notification list of the MWI SIP server. A
                              		  SIP MWI client runs TCP by default.

The transport tcp keyword is the default setting. The transport udp keyword allows you to integrate with a SIP MWI
                              		  client. The optional port keyword is used to specify a port number
                              		  other than 5060, the default. The default registration is with an extension
                              		  number, so the reg-e164 keyword allows you to register with
                              		  an E.164 ten-digit number.

Central voice-messaging servers that provide mailboxes for several
                              		  Cisco Unified CME sites may use site codes or prefixes to distinguish among
                              		  similarly numbered ranges of extensions at different sites. In Cisco CME 3.2.3
                              		  and later versions, you can specify that your Cisco Unified CME system should
                              		  accept unsolicited SIP Notify messages for message-waiting indication (MWI)
                              		  that include a prefix string as a site identifier.

## Examples

The following example sets MWI for the SIP server and sets individual
                              		  ephone-dn extension numbers to the MWI SIP server’s notification list:

```
Router(config) ephone-dn 1 Router(config-ephone-dn) number 5001 Router(config-ephone-dn) name Accounting Router(config-ephone-dn) mwi sip Router(config-ephone-dn) exit Router(config) telephony-service Router(config-telephony) mwi sip-server 192.168.0.5 transport udp
```

The following example identifies the SIP server for MWI notification
                              		  at the IP address 172.16.14.22. It states that the Cisco Unified CME system
                              		  will accept unsolicited SIP Notify messages that include the prefix 555 as a
                              		  site identifier.

```
telephony-service
 mwi sip-server 172.16.14.22 unsolicited prefix 555
```

### Related Commands

Description

mwi (ephone-dn)

Configures specific Cisco Unified IP phone directory
                                          						numbers to receive MWI notification from an external voice-mail system.

mwi expires

Sets the expiration timer for registration for the client
                                          						or the server.

mwi sip (ephone-dn)

Subscribes an extension in a Cisco Unified CME router to
                                          						receive MWI notification from a SIP MWI server.

show mwi relay clients

Displays the registration information for MWI relay
                                          						clients.

## mwi stutter (voice register global)

To generate a stutter tone for message-waiting indication (MWI) in a
                              		  Cisco CallManager Express (Cisco CME) system using SIP, use the mwi stutter command in voice register global
                              		  configuration mode. To disable MWI stutter, use the no form of this command.

mwi stutter

no mwi stutter

### Syntax Description

This command has no arguments or keywords.

### Command Default

Stutter tone for MWI is disabled.

### Command Modes

Voice register global configuration (config-register-global)

## Command History

Cisco IOS Release

Version

Modification

12.4(4)T

Cisco CME 3.4

This command was introduced.

## Examples

The following example shows how to enable MWI stutter:

```
Router(config)# voice register global Router(config-register-global)# mwi stutter
```

### Related Commands

Description

mwi reg-e164

Registers full E.164 number to the MWI server in Cisco
                                          						Unified CME and enables MWI.

## mwi-line

To designate a line other than the primary line of an ephone to be
                              		  associated with the ephone’s message waiting indicator (MWI) lamp, use the mwi-line command in ephone configuration
                              		  mode. To return to the default, use the no form of this command.

mwi-line line-number

no mwi-line

### Syntax Description

line-number

Line number to be associated with the MWI lamp. Range is
                                          						from 1 to 34.

### Command Default

A phone’s MWI lamp is lit only when there is a message waiting for
                              		  the phone’s primary line (line 1).

### Command Modes

Ephone configuration (config-ephone)

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

This command designates a phone line other than the primary line to
                              		  activate the MWI lamp on the phone. When a message is waiting for an ephone-dn
                              		  associated with the designated line, the MWI lamp is turned on. When the
                              		  message is heard, the MWI lamp is turned off. For phone lines other than the
                              		  line that is designated to receive MWI, an envelope icon is displayed next to
                              		  them when there is a message waiting.

Note that a logical phone “line” is not the same as a phone button. A
                              		  line is a button that has one or more ephone-dns assigned to it. A button that
                              		  has no ephone-dns assigned to it does not count as a line.

In most cases, one ephone-dn is assigned to one button on an ephone.
                              		  When you set the mwi-line command to that button, the MWI lamp
                              		  is turned on when there is a message waiting for that ephone-dn. When you set
                              		  the mwi-line command to a button with a more
                              		  complex configuration, the following rules apply:

- When a button has a single ephone-dn with primary and secondary
                                 			 numbers, the MWI lamp is turned on only when there is a message waiting for the
                                 			 primary number.

- When a button has several ephone-dns overlaid on it, the MWI lamp
                                 			 is turned on only when there is a message waiting for the first number in the
                                 			 list of ephone-dns.

- When a button is an overflow button for an overlay button, the MWI
                                 			 lamp is not turned on for any extension that might overflow to this button. If
                                 			 you set the mwi-line command to this button, the
                                 			 command is ignored.

## Examples

The following example enables MWI on ephone 18 for line 2 (button 2),
                              		  which has overlaid ephone-dns. The MWI lamp on this phone will be lit only if
                              		  there is a message waiting for extension 2021. Button 4 is unused. The line
                              		  numbers in this example are as follows:

- Line 1—Button 1—Extension 2020

- Line 2—Button 2—Extension 2021, 2022, 2023, 2024, 2025

- Line 3—Button 3—Extension 2021, 2022, 2023, 2024, 2025 (rollover
                                 			 line)

- Button 4—Unused

- Line 4—Button 5—Extension 2026

```
ephone-dn 20
 number 2020
ephone-dn 21
 number 2021
ephone-dn 22
 number 2022
ephone-dn 23
 number 2023
ephone-dn 24
 number 2024
ephone-dn 25
 number 2025
ephone-dn 26
 number 2026
ephone 18
 button 1:20 2o21,22,23,24,25 3x2 5:26
 mwi-line 2
```

The following example enables MWI on ephone 17 for line 3 (extension
                              		  609). In this case, the button numbers do not match the line numbers because
                              		  buttons 2 and 4 are not used.

- Line 1—Button 1—Extension 607

- Button 2—Unused

- Line 2—Button 3—Extension 608

- Button 4—Unused

- Line 3—Button 5—Extension 609

```
ephone-dn 17
 number 607
ephone-dn 18
 number 608
ephone-dn 19
 number 609
ephone 25
 button 1:17 3:18 5:19
 mwi-line 3
```

### Related Commands

Description

button

Associates ephone-dns with individual buttons on an SCCP
                                          						phone and to specify line type or ring behavior.

## mwi-type

To specify the type of message-waiting indication (MWI) notification
                              		  that a directory number can receive and process, use the mwi-type command in ephone-dn or
                              		  ephone-dn-template configuration mode. To disable this feature, use the no form of this command.

mwi-type { visual | audio | both }

no mwi-type { visual | audio | both }

### Syntax Description

visual

Sets a directory number to process visual MWI, using either
                                          						the main or secondary phone number.

audio

Sets a directory number to process audible MWI (AMWI),
                                          						using either the main or secondary phone number.

both

Sets a directory number to process both visual and audible
                                          						MWI, using either the main or secondary phone number.

### Command Default

If MWI is enabled for a directory number, directory number will
                              		  receive visual MWI.

### Command Modes

Ephone-dn configuration (config-ephone-dn) Ephone-dn-template configuration (config-ephone-dn-template)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(6)XE

Cisco Unified CME 4.0(2)

This command was introduced.

12.4(4)XC4

Cisco Unified CME 4.0(3)

This command was introduced.

12.4(11)T

Cisco Unified CME 4.0(3)

This command was integrated into Cisco IOS Release
                                          						12.4(11)T.

### Usage Guidelines

This command enables a directory number to receive audible, visual,
                              		  or both audible and visual MWI notification from an external voice-messaging
                              		  system. The external voice-messaging system is able to communicate MWI status
                              		  by making telephone calls to the dummy extension, with the MWI information
                              		  embedded in either the called or calling-party IP phone number.

Based on the capabilities of the IP phone and how the mwi-type command is configured, Message
                              		  Waiting is communicated as follows:

- If the phone supports (visual) MWI and MWI is configured for the
                                 			 phone, Message Waiting light is lit.

- If the phone supports (visual) MWI only, Message Waiting light is
                                 			 lit regardless of the configuration.

- If the phone supports AMWI and AMWI is configured for the phone,
                                 			 stutter dial tone is sent to the phone when it goes off-hook.

- If the phone supports AMWI only and AMWI is configured, stutter
                                 			 dial tone is sent to the phone when it goes off hook regardless of the
                                 			 configuration.

- If a phone supports (visual) MWI and AMWI and both options are
                                 			 configured for the phone, the Message Waiting light is lit and a stutter dial
                                 			 tone is sent to the phone when it goes off-hook.

Before using this command:

- Create the directory number to be configured by using the number

- Enable MWI on this directory number by using the mwi command.

If you use an ephone-dn template to apply a command to a directory
                              		  number and you also use the same command in ephone-dn configuration mode for
                              		  the same number, the value that you set in ephone-dn configuration mode has
                              		  priority.

## Examples

The following example shows how to enable AMWI on extension 8000,
                              		  assuming that the phone to which this directory number is assigned supports
                              		  AMWI. Otherwise, a call placed by the voice-mail system to 8001 turns on the
                              		  MWI light for the extension number indicated by the calling-party number for
                              		  the MWI call.

```
Router(config)# ephone-dn 1 Router(config-ephone-dn) number 8000 Router(config-ephone-dn) MWI on Router(config-ephone-dn) MWI-type audible
```

The following example shows how to enable both audible and visual
                              		  MWI. A call placed by the voice-mail system to 8001 turns on the MWI light for
                              		  the extension number indicated by the calling-party number for the MWI call.
                              		  When the phone user takes the phone off hook, they hear a stutter dial tone:

```
Router(config)# ephone-dn 2 Router(config-ephone-dn) number 8001 Router(config-ephone-dn) MWI on Router(config-ephone-dn) MWI-type both
```

The following example shows how to use an ephone-dn-template to set
                              		  MWI type:

```
Router(config)# ephone-dn-template 4 Router(config-ephone-dn-template) MWI-type both Router(config-ephone-dn-template)# exit Router(config)# ephone-dn 1 Router(config-ephone-dn)# number 8000 Router(config-ephone-dn)# ephone-dn-template 4
```

### Related Commands

Description

ephone-dn-template (ephone-dn)

Applies a template to an ephone-dn configuration.

mwi (ephone and ephone template)

Enables a directory number to receive MWI.

number

Associates a telephone or extension number with a directory
                                          						number in a Cisco Unified CME system.

| mac-address | Identifying MAC address of an IP phone, which is found on a
                                          						sticker located on the bottom of the phone. |
|---|---|
| reserved | Identifies the reserved MAC address of the phone. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco ITS 1.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |
| 12.2(15)ZJ | Cisco CME 3.0 | The mac-address argument was made
                                          						optional to enable automatic MAC address assignment after registration of
                                          						phones. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

|  | Description |
|---|---|
| create cnf-files | Builds the XML configuration files that are required for IP
                                          						phones used with Cisco IOS Telephony Services V2.1, Cisco CallManager Express
                                          						3.0, or later versions. |
| ip source-address | Identifies the IP address and port through which IP phones
                                          						communicate with a Cisco CME router. |
| max-dn | Sets the maximum number of ephone-dns to be supported by a
                                          						Cisco CME router. |
| max-ephones | Sets the maximum number of ephones to be supported by a
                                          						Cisco CME router. |
| show ephone registered | Displays status and information for registered IP phones. |

| mac-address | MAC address of the voice gateway. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command was integrated into Cisco IOS release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| type (voice-gateway) | Defines the type of voice gateway to autoconfigure in Cisco
                                          						Unified CME. |
| voice-port (voice-gateway) | Identifies the analog ports on the voice gateway that
                                          						register to Cisco Unified CME. |

| last-redirect-num | (PBX voice mail only) The mailbox to which the call will be
                                          						sent is the number that diverted the call to the voice-mail pilot number (the
                                          						last number to divert the call). |
|---|---|
| orig-called-num | (Cisco Unity Express only) The mailbox to which the call
                                          						will be sent is the number that was originally dialed before the call was
                                          						diverted. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| last-redirect-num | The mailbox to which the call will be sent is the last
                                          						number to divert the call. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| number-of-calls | Maximum number of calls. Range: 1 to 8. Default: 8. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 4.3 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| busy-trigger-per-button | Sets the maximum number of incoming calls allowed on an
                                          						octo-line directory number before it triggers Call Forward Busy on the phone. |
| ephone-dn | Configures a directory number for SCCP phones. |
| type | Assigns a phone type to an SCCP phone. |

| max-conference number | Maximum number of three-party conferences that are
                                          						supported simultaneously by the router. This number is platform-dependent, and
                                          						the default is half the maximum for each platform. The following are the
                                          						maximum values for this argument: Cisco 1700 series, Cisco 2600 series, Cisco 2801—8 Cisco 2811, Cisco 2821, Cisco 2851, Cisco 3600 series,
                                             						  Cisco 3700 series—16 Cisco 3800 series—24 (requires Cisco IOS Release
                                             						  12.3(11)XL or higher) Note Each individual Cisco IP phone can host a maximum of one
                                                   						conference at a time. You cannot create a second conference on the phone if you
                                                   						already have an existing conference on hold. | Note | Each individual Cisco IP phone can host a maximum of one
                                                   						conference at a time. You cannot create a second conference on the phone if you
                                                   						already have an existing conference on hold. |
|---|---|---|---|
| Note | Each individual Cisco IP phone can host a maximum of one
                                                   						conference at a time. You cannot create a second conference on the phone if you
                                                   						already have an existing conference on hold. |
| gain | (Optional) Increases the sound volume of VoIP and public
                                          						switched telephony network (PSTN) parties joining a conference call. The
                                          						allowable decibel units are -6 db, 0 db, 3 db, and 6 db. The default is -6 db. |

| Note | Each individual Cisco IP phone can host a maximum of one
                                                   						conference at a time. You cannot create a second conference on the phone if you
                                                   						already have an existing conference on hold. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco ITS 2.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |
| 12.3(11)XL1 | Cisco CME 3.2.1 | The gain keyword was added. |
| 12.3(14)T | Cisco CME 3.3 | This command was integrated into Cisco IOS Release
                                          						12.3(14)T. |

| max directory numbers | Maximum number of directory numbers (ephone-dns) to allow in the Cisco CME system. The maximum you can set depends on the
                                          software version, router platform, and amount of memory that you have installed. Type ? to display range. The default is 0. |
|---|---|
| preference preference-order | (Optional) Sets a preference value for the primary number
                                          						of an ephone-dn. Refer to CLI help for a range of numeric options, where 0 is
                                          						the highest preference. Default is 0. |
| no-reg | (Optional) Globally disables ephone registration with an
                                          						H.323 gatekeeper or SIP proxy. |
| primary | Primary ephone-dn numbers only. |
| both | Both primary and secondary ephone-dn numbers. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco ITS 1.0 | This command was introduced |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |
| 12.4(4)XC | Cisco Unified 4.0 | The preference , no-reg , primary , and both keywords were introduced. |
| 12.4(9)T | Cisco Unified 4.0 | The preference , no-reg , primary , and both keywords were integrated into
                                          						Cisco IOS Release 12.4(9)T. |

| Note | You can increase the number of allowable extensions to the
                                       		  maximum; but after the maximum allowable number is configured, you cannot
                                       		  reduce the limit without rebooting the router. |
|---|---|

|  | Description |
|---|---|
| ephone-dn | Enters ephone-dn configuration mode. |
| max-ephones | Sets the maximum number of phones supported by the router. |
| number | Associates a telephone or extension number with an
                                          						ephone-dn. |

| max directory numbers | Maximum number of extensions (ephone-dns) supported by the
                                          						Cisco router. The maximum number is version and platform dependent; type ? to display range. In Cisco CME 3.4 to Cisco Unified CME 7.0 and in Cisco SIP SRST 3.4 to Cisco Unified SIP SRST 7.0: Default is maximum number
                                                supported by platform. In Cisco Unified CME 7.1 and Cisco Unified SIP SRST 7.1 and later versions: Default is 0. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was introduced. |
| 12.4(22)YB | Cisco Unified CME 7.1 Cisco Unified SIP SRST 7.1 | The default value was changed to 0. |
| 12.4(24)T | Cisco Unified CME 7.1 Cisco Unified SIP SRST 7.1 | This command was integrated into Cisco IOS release
                                          						12.4(24)T. |

| Note | This command can also be used for Cisco Unified SIP SRST. |
|---|---|

| Command | Description |
|---|---|
| voice register dn | Enters voice register dn configuration mode to define an
                                          						extension for a SIP phone line. |
| max-pool (voice register global) | Sets the maximum number of SIP voice register pools that
                                          						are supported in a Cisco SIP SRST or Cisco CME environment. |

| max phones | Maximum number of phones supported by the Cisco CME router.
                                          						The maximum number is version- and platform-dependent; refer to Cisco IOS
                                          						command-line interface (CLI) help. Default is 0. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco ITS 1.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was modified to set the maximum number of
                                          						phones that can register to Cisco Unified CME. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Note | You can increase the number of phones; but after the maximum
                                       		  allowable number is configured, you cannot reduce the limit of the Cisco IP
                                       		  phones without rebooting the router. |
|---|---|

| Command | Description |
|---|---|
| ephone | Enters ephone configuration mode. |
| max-dn | Sets the maximum number of extensions (ephone-dns) that can
                                          						be supported by the router. |

| minutes | Maximum number of minutes an Extension Mobility phone is
                                          						idle after which the logged-in user is logged out from Extension Mobility.
                                          						Range:1 to 9999. |
|---|---|

| Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| keep call-history | Disables Automatic Clear Call History for Extension
                                          						Mobility in Cisco Unified CME. |
| reset (voice logout-profile and voice user-profile) | Performs a complete reboot of all IP phones on which a
                                          						particular logout profile or user profile is downloaded. |

| value | Video bandwidth in kb/s Range is 0 to 10000000. Default
                                          						value is 10000000. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| max voice-register-pools | Maximum number of SIP voice register pools supported by the
                                          						Cisco router. The upper limit of voice register pools is version- and
                                          						platform-dependent; type ? for range. In Cisco CME 3.4 to Cisco Unified CME 7.0 and in Cisco
                                             						  SIP SRST 3.4 to Cisco Unified SIP SRST 7.0: Default is maximum number supported
                                             						  by platform. In Cisco Unified CME 7.1 and Cisco Unified SIP SRST 7.1
                                             						  and later versions: Default is 0. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was introduced. |
| 12.4(22)YB | Cisco Unified CME 7.1 Cisco Unified SIP SRST 7.1 | The default value was changed to 0. |
| 12.4(24)T | Cisco Unified CME 7.1 Cisco Unified SIP SRST 7.1 | This command was integrated into Cisco IOS release
                                          						12.4(24)T. |

| Note | This command can also be used for Cisco Unified SIP SRST. |
|---|---|

| Command | Description |
|---|---|
| max-dn (voice register global) | Set the maximum number of SIP phone directory numbers
                                          						(extensions) that are supported by a Cisco Unified CME router. |

| number | Number
                                          						of presentation lines. Range: 1 to 100. Default: 0. See the table for the
                                          						number of presentation lines supported by each phone type. |
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
| device-id | Specifies the device ID for a phone type in an ephone-type template. |
| num-buttons | Sets
                                          						the number of line buttons supported by a phone type. |
| type | Assigns the phone type to an SCCP phone. |

| number | Number of permissible redirects. Range: 5 to 20. Default:
                                          						10. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(24)T1 | Cisco Unified CME 7.1 | The default value was increased from 5 to 10. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| ephone-hunt | Creates an ephone hunt group in Cisco Unified CME. |
| hops | Sets the number of hops before a call proceeds to the final
                                          						number. |

| number | Maximum watch sessions. Range: 100 to 500. Default: 100. |
|---|---|

| Release | Modification |
|---|---|
| 12.4(11)XJ | This command was introduced. |
| 12.4(15)T | This command was integrated into Cisco IOS Release
                                          						12.4(15)T. |

|  | Description |
|---|---|
| allow watch | Allows a directory number on a phone registered to Cisco
                                          						Unified CME to be watched in a presence service. |
| allow subscribe | Allows internal watchers to monitor external presence
                                          						entities (directory numbers). |
| presence enable | Allows incoming presence requests from SIP trunks. |
| server | Specifies the IP address of a presence server for sending
                                          						presence requests from internal watchers to external presence entities. |
| watcher all | Allows external watchers to monitor internal presence
                                          						entities (directory numbers). |

| seconds | Number of seconds. Range is from 3 to 60000. Default is
                                          						unlimited. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

|  | Description |
|---|---|
| ephone-hunt | Defines an ephone hunt group and enters ephone-hunt
                                          						configuration mode. |

| flow-around | (Optional) Enables media packets to pass directly between
                                          						the endpoints, without the intervention of the Cisco UBE. The media packet is
                                          						to flow around the gateway. |
|---|---|
| flow-through | (Optional) Enables media packets to pass through the
                                          						endpoints, without the intervention of the Cisco UBE. |
| forking | (Optional) Enables the media forking feature for all calls. |
| monitoring | Enables the monitoring feature for all calls or a maximum
                                          						number of calls. |
| max-calls | The maximum number of calls that are monitored. |
| statistics | (Optional) Enables media monitoring. |
| transcoder high-density | (Optional) Converts media codecs from one voice standard to
                                          						another to facilitate the interoperability of devices using different media
                                          						standards. |

| Release | Modification |
|---|---|
| 12.3(1)T | This command was introduced. |
| 12.4(11)XJ2 | This command was modified. The statistics keyword was introduced. |
| 12.4(15)T | This command was integrated into Cisco IOS Release
                                          						12.4(15)T. |
| 12.4(20)T | This command was modified. The transcoder and high-density keywords were
                                          						introduced. |
| 15.0(1)M | This command was modified. The forking and monitoring keywords and the max-calls argument were introduced. |
| 15.1(3)T | This command was modified. The media flow around is now
                                          						supported for the SIP to SIP trunk calls in Cisco Unified CME 8.5. |

| Note | The Cisco UBE must be running Cisco IOS Release 12.3(1) or a later
                                       		  release to support media flow-around. |
|---|---|

| Command | Description |
|---|---|
| dial-peer voice | Enters dial peer configuration mode. |
| mode border-element | Enables the media monitoring capability of the media command. |
| voice class | Enters voice class configuration mode. |
| voice service | Enters voice service configuration mode. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.2(4)M | Cisco Unified CME 9.1 | This command was introduced. |

| Command | Description |
|---|---|
| ephone-hunt | Enters ephone-hunt configuration mode to define a Cisco CME
                                          						ephone-hunt group. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| Cisco
                                          						IOS XE Everest 16.4.1 15.6(3)M1 | Cisco
                                          						Unified CME 11.6 | This
                                          						command was introduced. |

| Command | Description |
|---|---|
| members logout | Enables
                                          						members logout for ephone-hunt groups configured on a Cisco Unified CME. |

| all | (Optional) Displays all missed calls including those on
                                          						overlay buttons. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| button | Associates directory numbers with individual buttons on a
                                          						Cisco Unified IP Phone and specifies ring behavior. |

| Cisco IOS Release | Cisco Products | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| ephone-template (ephone) | Applies an ephone template to an SCCP phone. |
| mlpp max-precedence | Sets the maximum precedence (priority) level that a phone
                                          						user can specify when making an MLPP call. |
| mlpp preemption | Enables preemption capability on an SCCP phone or analog
                                          						FXS port. |
| preemption tone timer | Sets the amount of time the preemption tone plays on the
                                          						called phone when a lower precedence call is being preempted. |

| number | Number representing the maximum precedence level. Range:
                                          						0 to 4, where 0 is the highest priority. Default: 4. |
|---|---|

| Cisco IOS Release | Cisco Products | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| access-digits | Defines the access digit that phone users dial to request a
                                          						precedence call. |
| ephone-template (ephone) | Applies an ephone template to an SCCP phone. |
| mlpp indication | Enables MLPP indication on an SCCP phone or analog FXS
                                          						port. |
| mlpp preemption | Enables the preemption capability on an SCCP phone or
                                          						analog FXS port. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| ephone-template (ephone) | Applies an ephone template to an SCCP phone. |
| mlpp indication | Enables MLPP indication on an SCCP phone or analog FXS
                                          						port. |
| mlpp max-precedence | Sets the maximum precedence (priority) level that a phone
                                          						user can specify when making an MLPP call. |
| preemption tone timer | Defines the expiry time for the preemption tone for the
                                          						call being preempted. |

| drsn | Phone belongs to Defense Red Switched Network (DRSN). |
|---|---|
| dsn | Phone belongs to Defense Switched Network (DSN). |
| domain-number | Number to identify the domain, in three-octet format.
                                          						Range: 0x000000 to 0xFFFFFF. |
| level | Number representing the maximum precedence level, where 0
                                          						is the highest priority. Range is 0 to 4 (DSN) or 0 to 5 (DRSN). |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| access-digit | Defines the access digit that phone users dial to request a
                                          						precedence call. |
| ephone-template (ephone) | Applies an ephone template to an SCCP phone. |
| mlpp indication | Enables MLPP indication on an SCCP phone or analog FXS
                                          						port. |
| mlpp preemption | Enables the preemption capability on an SCCP phone or
                                          						analog FXS port. |
| service-domain | Sets the global MLPP domain name and number. |

| Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| number | Associates a telephone or extension number with an
                                          						ephone-dn. |
| snr | Enables Single Number Reach on an extension of an SCCP IP
                                          						phone. |
| softkeys connected | Modifies the order and type of soft keys that display on an
                                          						IP phone during the connected call state. |
| softkeys idle | Modifies the order and type of soft keys that display on an
                                          						IP phone during the idle call state. |

| Release | Modification |
|---|---|
| 15.2(2)T | This command was introduced. |

| Command | Description |
|---|---|
| snr (voice register dn) | Enables the SNR feature on an extension of a Cisco Unified
                                          						SIP IP phone. |

| cme | CME mode provides the options to configure SIP phones and features. |
|---|---|
| cme-app | CME appliance mode provides the options to configure up to 200 SIP phones for routers that are only being used to provide
                                          call control. CME appliance mode is available only for ISR4321 routers. |
| esrst | E-SRST mode extends SRST features to include the static configuration of SIP phones and features. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco
                                          						CME 3.4 Cisco SIP SRST | This
                                          						command was introduced. |
| 15.3(3)M | Cisco
                                          						CME 10.0 | This
                                          						command was modified to add the esrst mode. |
| Cisco
                                          						IOS XE Everest 16.5.1b | Unified CME 11.7 Unified SRST 11.7 | The behavior of no form of this command was modified, to clear all voice register pools and voice register dns, along with mode-specific configurations. |
| Cisco IOS XE Amsterdam 17.2.1r | Unified CME 12.8 | The cme-app mode was added for ISR4321 routers, allowing the configuration of up to 200 phones (For routers dedicated to CME use only). |

|  | Description |
|---|---|
| show voice register global | Displays all global configuration information that is associated with SIP phones. |

| out-call outcall-number | (Optional) Sets up a call to the outcall number in order to
                                          						connect to the MOH feed. If this keyword is not used, the live feed is assumed
                                          						to derive from an incoming call to the ephone-dn under which this command is
                                          						used. |
|---|---|
| ip ip-address | (Optional) Indicates that this audio stream is to be used
                                          						as a multicast source as well as the MOH source and specifies the destination
                                          						IP address for multicast. |
| port port-number | (Optional) Specifies the media port for multicast. Range is
                                          						from 2000 to 65535. Port 2000 is recommended because this port is already used
                                          						for normal Real-Time Transport Protocol (RTP) media transmissions between IP
                                          						phones and the Cisco CallManager Express router. |
| route ip-address | (Optional) Indicates the specific router interface on which
                                          						to transmit the IP multicast packets. The default is that the MOH multicast
                                          						stream is automatically output on the interface that corresponds to the address
                                          						that was configured with the ip source-address command. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(11)YT | Cisco ITS 2.1 | This command was introduced. |
| 12.2(15)T | Cisco ITS 2.1 | This command was integrated into Cisco IOS Release
                                          						12.2(15)T. |
| 12.2(15)ZJ | Cisco CME 3.0 | The ip , port , and route keywords were added. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Note | IP phones do not support multicast at 224.x.x.x addresses. |
|---|---|

|  | Description |
|---|---|
| auto-cut-through | Enables call completion when an M-lead response is not
                                          						provided. |
| ephone-dn | Enters ephone-dn configuration mode to set directory
                                          						numbers and parameters for individual Cisco IP phone extensions. |
| feed | Enables multicast of an audio stream that is different from
                                          						the music-on-hold audio stream. |
| ip source-address | Identifies the IP address and port through which IP phones
                                          						communicate with a Cisco CME router. |
| moh (telephony-service) | Enables music on hold from an audio file. |
| multicast moh | Enables multicast of the music-on-hold audio stream. |
| signal | Specifies the type of signaling for a voice port. |

| filename | Name of the audio file to use for the MOH audio stream. The
                                          						file must be copied to flash memory on the Cisco CME router. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco ITS 2.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |

|  | Description |
|---|---|
| debug ephone moh | Displays diagnostic information for music on hold. |
| moh (ephone-dn) | Enables music on hold from a live audio feed. |
| multicast moh | Enables multicast of the music-on-hold audio stream. |

| filename | Name of the music file. The music file must be in the
                                          						system flash. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME/SRST/SIP SRST 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME/SRST/SIP SRST 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Note | Music-on-hold files can be in .wav or .au file format; however,
                                       		  the file format must contain 8-bit 8-kHz data; for example, CCITT a-law or
                                       		  u-law data format. |
|---|---|

| voice moh-group | Enters voice moh-group configuration mode. |
|---|---|
| extension-range | Defines extension range for a clients calling a
                                          						voice-moh-group. |
| moh | Enables music on hold from a flash audio file. |
| multicast moh | Enables multicast of the music-on-hold audio stream. |

| file-size | Specifies a numeric value for the buffer MOH file size
                                          						between 64 KB and 10000 KB. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Note | When live-feed is enabled there is no file caching for MOH-group
                                       		  0. |
|---|---|

| Command | Description |
|---|---|
| voice-moh-group | Enter voice-moh-group configuration mode. |
| moh filename | Enables music on hold from a flash audio feed |
| multicast moh | Enables multicast of the music-on-hold audio stream. |
| extension-range | Specifies the extension range for a clients calling a
                                          						voice-moh-group. |

| tag | A unique number that identifies a MOH group. Range is from
                                          						1 to 5. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| description | Displays a brief description about a voice moh-group in
                                          						use. |
|---|---|
| extension-range | Defines extension range for a clients calling a
                                          						voice-moh-group. |
| moh | Enables music on hold from a flash audio feed. |
| multicast moh | Enables multicast of the music-on-hold audio stream. |

| video-only | Specifies that the video streams must be sent through the
                                          						Cisco Unified CME route. |
|---|---|
| both | Specifies that both voice and video streams must be sent
                                          						through the Cisco Unified CME route. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |
| 15.1(4)M | Cisco Unified CME 8.6 | Support for choosing video streams was added. |

| Command | Description |
|---|---|
| ephone-template (ephone) | Applies template to ephone being configured. |

| bytes | Mtu value, in bytes. Range: 256 to 1406. Default: 1290. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(3)T | Cisco Unified CME 8.5 | This command was introduced. |

| Command | Description |
|---|---|
| vpn-profile | Defines a VPN-profile. |

| ip-address | Specifies the destination IP address for multicast. |
|---|---|
| port port-number | Specifies the media port for multicast. Range is from 2000
                                          						to 65535. Port 2000 is recommended because this port is already used for normal
                                          						Real-Time Transport Protocol (RTP) media transmissions between IP phones and
                                          						the Cisco CME router. |
| route ip-address-list | (Optional) Indicates specific router interfaces over which
                                          						to transmit the IP multicast packets. Up to four IP addresses can be listed,
                                          						each separated from the other by a space. The default is that the MOH multicast
                                          						stream is automatically output on the interfaces that correspond to the address
                                          						that was configured with the ip source-address command. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was modified. Multicast MOH was enabled under
                                          						voice moh-group configuration mode. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Note | IP phones do not support multicast at 224.x.x.x addresses. |
|---|---|

| Note | Multicast for live feed is not support in MOH groups. |
|---|---|

| Command | Description |
|---|---|
| feed | Enables multicast of an audio stream that is not the
                                          						music-on-hold audio stream. |
| ip source-address | Identifies the IP address and port through which IP phones
                                          						communicate with a Cisco CME router. |
| moh (ephone-dn) | Enables music on hold from a live audio feed. |
| moh (telephony-service) | Enables music on hold from an audio file. |
| voice moh-group | Enters voice moh-group configuration mode |

| off | Sets a Cisco Unified IP phone extension to process MWI to
                                          						OFF, using either the main or secondary phone number. |
|---|---|
| on | Sets a Cisco Unified IP phone extension to process MWI to
                                          						ON, using either the main or secondary phone number. |
| on-off | Sets a Cisco Unified IP phone extension to process MWI to
                                          						both ON and OFF, using either the main or secondary phone number. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco ITS 2.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was made available in ephone-dn-template
                                          						configuration mode. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command in ephone-dn-template configuration mode was
                                          						integrated into Cisco IOS Release 12.4(9)T. |

|  | Description |
|---|---|
| ephone-dn-template (ephone-dn) | Applies template to ephone-dn being configured. |
| mwi expires | Sets the expiration timer for registration for either the
                                          						client or the server. |
| mwi sip (ephone-dn) | Subscribes an extension in a Cisco Unified CME router to
                                          						receive MWI notification from a SIP MWI server. |
| mwi sip-server (telephony-service) | Configures the IP address and port number for an external
                                          						SIP-based MWI server. |
| number | Associates a telephone or extension number with an
                                          						extension (ephone-dn) in a Cisco Unified CME system. |

| Cisco IOS Release | Version | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

|  | Description |
|---|---|
| number (voice register pool) | Configures number patterns for a voice register pool. |

| seconds | Expiration time, in seconds. Range is from 600 to 99999.
                                          						Default is 86400 (24 hours). |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco ITS 2.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |

|  | Description |
|---|---|
| mwi relay (telephony-service) | Enables the Cisco CME router to relay MWI information to
                                          						remote Cisco IP phones. |
| mwi sip-server (telephony-service) | Configures the IP address and port number for the external
                                          						SIP-based MWI server. |

| prefix-string | Digits at the beginning of a number that will be recognized
                                          						as a prefix before a Cisco Unified CME extension number. The maximum prefix
                                          						length is 32 digits. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

|  | Description |
|---|---|
| mwi (ephone-dn and ephone-dn-template) | Configures specific Cisco Unified IP phone directory
                                          						numbers to receive MWI notification from an external voice-mail system. |
| mwi-server | Configures MWI server parameters. |
| mwi sip (ephone-dn) | Subscribes an extension in a Cisco Unified CME router to
                                          						receive MWI notification from a SIP MWI server. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

|  | Description |
|---|---|
| ephone-dn-template (ephone-dn) | Applies a template to ephone-dn being configured. |
| transfer-system | Specifies the call transfer method for Cisco Unified CME
                                          						extensions. |
| voicemail | Defines the telephone number that is speed-dialed when the
                                          						Messages button on a Cisco Unified IP phone is pressed. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(11)T7 12.4 | Cisco CME 3.3 | This command was introduced. |

|  | Description |
|---|---|
| mwi-server (SIP user-agent) | Specifies voice-mail server settings on a voice gateway or
                                          						user agent (UA). |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco ITS 2.0 | This command was introduced command. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						command. |

|  | Description |
|---|---|
| mwi expires | Sets the expiration timer for registration for the client
                                          						or the server. |
| show mwi relay clients | Displays registration information for MWI relay clients. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco ITS 2.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was made available in ephone-dn-template
                                          						configuration mode. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command in ephone-dn-template configuration mode was
                                          						integrated into Cisco IOS Release 12.4(9)T. |

|  | Description |
|---|---|
| ephone-dn | Enters ephone-dn configuration mode. |
| ephone-dn-template (ephone-dn) | Applies a template to an ephone-dn configuration. |
| mwi sip-server (telephony-service) | Configures the IP address and port number for the external
                                          						SIP-based MWI server. |
| show mwi relay clients | Displays registration information for MWI relay clients. |

| ip-address | IP address of the MWI server. |
|---|---|
| transport tcp | (Optional) Selects TCP as the transport layer protocol.
                                          						This is the default transport protocol. |
| transport udp | (Optional) Selects UDP as the transport layer protocol. The
                                          						default if these keywords are not used is TCP. |
| port port-number | (Optional) Specifies port number for the MWI server. Range
                                          						is from 2000 to 9999. Default is 5060 (SIP standard port). |
| reg-e164 | (Optional) Registers an E.164 number with a Session
                                          						Interface Protocol (SIP) proxy or registrar rather than an extension number.
                                          						Registering with an extension number is the default. |
| unsolicited | (Optional) Sends SIP Notify message for MWI without any
                                          						need to send a Subscribe message from the Cisco Unified CME router. |
| prefix prefix-string | (Optional) Allows the specified digits to be present before
                                          						a recognized Cisco Unified CME extension number. The maximum prefix length is
                                          						32 digits. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco ITS 2.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |
| 12.2(15)ZJ | Cisco CME 3.0 | The unsolicited keyword was added. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(4)XC | Cisco Unified CME 4.0 | The prefix prefix-string keyword-argument pair
                                          						was added. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command with the prefix prefix-string keyword-argument pair
                                          						was integrated into Cisco IOS Release 12.4(9)T. |

|  | Description |
|---|---|
| mwi (ephone-dn) | Configures specific Cisco Unified IP phone directory
                                          						numbers to receive MWI notification from an external voice-mail system. |
| mwi expires | Sets the expiration timer for registration for the client
                                          						or the server. |
| mwi sip (ephone-dn) | Subscribes an extension in a Cisco Unified CME router to
                                          						receive MWI notification from a SIP MWI server. |
| show mwi relay clients | Displays the registration information for MWI relay
                                          						clients. |

| Cisco IOS Release | Version | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

|  | Description |
|---|---|
| mwi reg-e164 | Registers full E.164 number to the MWI server in Cisco
                                          						Unified CME and enables MWI. |

| line-number | Line number to be associated with the MWI lamp. Range is
                                          						from 1 to 34. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

|  | Description |
|---|---|
| button | Associates ephone-dns with individual buttons on an SCCP
                                          						phone and to specify line type or ring behavior. |

| visual | Sets a directory number to process visual MWI, using either
                                          						the main or secondary phone number. |
|---|---|
| audio | Sets a directory number to process audible MWI (AMWI),
                                          						using either the main or secondary phone number. |
| both | Sets a directory number to process both visual and audible
                                          						MWI, using either the main or secondary phone number. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(6)XE | Cisco Unified CME 4.0(2) | This command was introduced. |
| 12.4(4)XC4 | Cisco Unified CME 4.0(3) | This command was introduced. |
| 12.4(11)T | Cisco Unified CME 4.0(3) | This command was integrated into Cisco IOS Release
                                          						12.4(11)T. |

|  | Description |
|---|---|
| ephone-dn-template (ephone-dn) | Applies a template to an ephone-dn configuration. |
| mwi (ephone and ephone template) | Enables a directory number to receive MWI. |
| number | Associates a telephone or extension number with a directory
                                          						number in a Cisco Unified CME system. |