---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-command-reference-cme-cr-cme-cr-chapter-010100-html-90586279d1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/command/reference/cme_cr/cme_cr_chapter_010100.html
retrieved_at: 2026-08-21T22:57:22.306359+00:00
---

Cisco Unified Communications Manager Express Command Reference

# Cisco Unified Communications Manager Express Command Reference

Updated: July 19, 2018

Chapter: Cisco Unified CME Commands: V

## Chapter: Cisco Unified CME Commands: V

# Cisco Unified CME Commands: V

## vad (voice register pool)

To enable voice activity detection (VAD) on a VoIP dial peer, use the vad command in voice register pool
                              		  configuration mode. To disable VAD, use the no form of this command.

vad

no vad

### Syntax Description

This command has no arguments or keywords.

### Command Default

VAD is enabled.

### Command Modes

Voice register pool configuration (config-register-pool)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was introduced.

### Usage Guidelines

VAD detects periods of silence in the voice signal and temporarily
                              		  discontinues transmission of the signal during these periods to save bandwidth.
                              		  Because VAD is enabled by default, there is no comfort noise during periods of
                              		  silence. As a result, the call may seem to be disconnected and you may prefer
                              		  to set no vad on the SIP phone pool.

## Examples

The following example shows how to disable VAD for pool 1:

```
Router(config)# voice register pool 1 Router(config-register-pool)# no vad
```

## vad (voice register template)

To enable voice activity detection (VAD) on SIP phones, use the vad command in voice register template
                              		  configuration mode. To return to the default, use the no form of this command.

vad

no vad

### Syntax Description

This command has no arguments or keywords.

### Command Default

VAD is disabled.

### Command Modes

Voice register template configuration (config-register-temp)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4

This command was introduced.

### Usage Guidelines

VAD detects periods of silence in the voice signal and temporarily
                              		  discontinues transmission of the signal during these periods to save bandwidth.
                              		  To apply the template to a SIP phone, use the template command in voice register pool
                              		  configuration mode.

## Examples

The following example shows how to enable VAD:

```
Router(config)# voice register template 1 Router(config-register-temp)# vad
```

### Related Commands

Description

template (voice register pool)

Applies a template to a SIP phone.

## vca

To specify the audio file used for the vacant code announcement, use
                              		  the vca command in voice MLPP configuration mode. To disable use of
                              		  this audio file, use the no form of this command.

vca audio-url voice-class cause-code tag

no vca

### Syntax Description

audio-url

Location of the announcement audio file in URL format.
                                          						Valid storage locations are TFTP, FTP, HTTP, and flash memory.

tag

Number of the voice class that defines the cause codes for
                                          						which the VCA is played. Range: 1 to 64.

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
                              		  file (.wav or .au format) for the announcement that plays to callers when they
                              		  dial an invalid or unassigned number.

The mlpp indication command must be enabled (default) for a
                              		  phone to play precedence announcements.

The VCA plays for the cause codes defined with the voice class cause-code command.

This command is not supported by Cisco IOS help. If you type ? , Cisco IOS help does not display a list of
                              		  valid entries.

## Examples

The following example shows that the audio file played for the vacant
                              		  code announcement is named vca.au and is located in flash. The announcement
                              		  plays for the unassigned-number and invalid-number cause codes, which are
                              		  defined in the matching cause-code voice class.

```
voice class cause-code 1
 unassigned-number
 invalid-number
!
!
voice mlpp
 vca flash:vca.au voice-class cause-code 1
```

### Related Commands

Command

Description

bnea

Specifies the audio file used for the busy station not
                                          						equipped for preemption announcement.

bpa

Specifies the audio file used for the blocked precedence
                                          						announcement.

ica

Specifies the audio file used for the isolated code
                                          						announcement.

mlpp indication

Enables MLPP indication on an SCCP phone or analog FXS
                                          						port.

voice class cause-code

Creates a voice class for defining a set of cause codes.

## video

To enable video capability on Cisco Unified IP Phones 9951 and 9971,
                              		  use the video command in voice register global, voice
                              		  register template, and voice register pool configuration modes. To disable
                              		  video capabilities on Cisco Unified IP Phones 9951 and 9971, use the no form of this command.

video

no video

### Syntax Description

This command has no arguments or keywords.

### Command Default

Video capability is disabled on Cisco Unified IP Phones 9951 and
                              		  9971.

### Command Modes

Voice register global Voice register template Voice register pool

## Command History

Cisco IOS Release

Cisco Product

Modification

15.1(4)M

Cisco Unified CME 8.6

This command was introduced.

### Usage Guidelines

Use this command to enable video capability on Cisco Unified IP
                              		  Phones 9951 and 9971. Video is supported on Cisco Unified IP phone 8961 through
                              		  CUVA. You need to create profile and apply-config or restart to the phone to
                              		  enable the video capability on phones.

## Examples

The following example shows video command configured in voice
                              		  register global:

```
Router#show run
!
!
!
voice service voip
 allow-connections sip to sip
 fax protocol t38 version 0 ls-redundancy 0 hs-redundancy 0 fallback none
!
!
voice register global
 mode cme
 bandwidth video tias-modifier 244 negotiate end-to-end
 max-pool 10
 video
!
voice register template  10
!
!
```

The following example shows video command configured under voice
                              		  register pool 5, you can also configure the video command under voice register
                              		  template:

```
Router#show run
!
!
voice service voip
 allow-connections sip to sip
 fax protocol t38 version 0 ls-redundancy 0 hs-redundancy 0 fallback none
!
!
voice register global
 mode cme
 bandwidth video tias-modifier 244 negotiate end-to-end
 max-pool 10
!
voice register pool  1
 id mac 1111.1111.1111
!
voice register pool  4
!
voice register pool  5
 logout-profile 58
 id mac 0009.A3D4.1234
 video
!
```

### Related Commands

Command

Description

apply-config

Allows to dynamically apply the phone configuration on
                                          						Cisco Unified SIP IP phones 8961, 9951, and 9971,

bandwidth video tias-modifier

Allows to set the maximum video bandwidth bytes per second
                                          						(BPS) for SIP IP phones

## video (ephone)

To enable video capabilities for an SCCP phone in Cisco Unified CME,
                              		  use the video command in ephone configuration mode.
                              		  To reset to default, use the no form of this command.

video

no video

### Syntax Description

This command has no arguments or keywords.

### Command Default

Video capabilities are disabled.

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

This command enables video capabilities in the ephone configuration
                              		  for a particular phone.

Video capabilities for SCCP phones in Cisco Unified CME must be
                              		  enabled globally as well as for individual phones. You must enable video for
                              		  all video-capable SCCP phones associated with a Cisco Unified CME router by
                              		  configuring the videoCapability parameter of the service phone command.

Video parameters, such as maximum bit rate, are set at a system-level
                              		  in video configuration mode.

## Examples

The following example shows the ephone portion from the show running-configuration command:

```
router# show running-configuration .
.
.
ephone  6
 video
 mac-address 000F.F7DE.CAA5
 type 7960
 button  1:6
```

### Related Commands

service phone

Modifies the vendorConfig parameters in phone configuration
                                          						files.

video (telephony-service)

Enters video configuration mode for modifying video
                                          						parameters in Cisco Unified CME.

## video (telephony-service)

To enter video configuration mode for setting video parameters for
                              		  all video-capable phones in Cisco Unified CME, use the video command in telephony-service
                              		  configuration mode. To reset global video parameters, use the no form of this command.

video

no video

### Syntax Description

This command has no arguments or keywords.

### Command Default

Defaults for global video parameters are configured.

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

This command enters video configuration mode for setting video
                              		  parameters for all video-capable Cisco Unified IP phones associated with a
                              		  Cisco Unified CME router.

## Examples

The following example shows how to enter video configuration mode for
                              		  a Cisco Unified CME router. You must enter video configuration mode to set
                              		  video parameters, such as maximum bit rate.

```
Router(config)# telephony-service Router(config-telephony)# video Router(config-tele-video)# maximum bit-rate 256
```

### Related Commands

Description

maximum bit-rate

Sets the maximum video bandwidth for phones in Cisco
                                          						unified CME.

show call active video

Displays call information for SCCP video calls in progress.

show call history video

Displays call history information for SCCP video calls.

## video screening (voice service sip)

To enable transcoding and transsizing between two call legs when
                              		  configuring SIP, use the video screening command in sip configuration mode. To disable transcoding and
                              		  transsizing, use no form of this command.

video screening

no video screening

### Syntax Description

This command has no arguments or keywords.

### Command Default

Video screening is disabled

### Command Modes

Sip

## Command History

Release

Modification

15.1(4)M

The command was introduced.

### Usage Guidelines

Use this command to enable conversion of video streams if there is a
                              		  mismatch between two call legs.

## Examples

The following example enters the voice-card configuration mode and
                              		  enables video screening:

```
Router(config)# voice service voip Router(config-voicecard)# sip Router((conf-serv-sip)# video screening
```

### Related Commands

Command

Description

codec profile

Defines the video capabilities needed for video endpoints.

video codec

Assigns a video codec to a VoIP dial peer.

## video-bitrate (ephone)

To specify the maximum IP phone video bandwidth in Cisco Unified CME,
                              		  use the video-bitrate command in the ephone mode. To restore the default video
                              		  bitrate or suse the no form of this command.

video-bitrate value

no video-bitrate

### Syntax Description

value

Video bandwidth in kb/s. Range is from 64 to 102400 kbps.

### Command Default

Bit rate defaults to the maximum bit-rate configured under video
                              		  configuration.

## Command History

Release

Modification

15.1(4)M

This command was introduced.

### Usage Guidelines

Use this command to modify the value of the maximum video bandwidth
                              		  for video-capable phones that support SIP, SCCP, and H.323.

## Examples

The following example sets a bit-rate of 512 kb/s.

```
Router(config)# ephone
Router(config-ephone)# video-bitrate 512
```

## vm-device-id (ephone)

To define a voice-messaging identification string, use the vm-device-id command in ephone configuration
                              		  mode. To disable this feature, use the no form of this command.

vm-device-id id-string

no vm-device-id

### Syntax Description

id-string

Voice-messaging device port identification (ID) string; for
                                          						example, CiscoUM-VI1 for the first port and CiscoUM-VI2 for the second port.
                                          						Note that the first two characters after the hyphen must be the uppercase
                                          						letters V and I.

### Command Default

No voice-mail identification string is defined.

### Command Modes

Ephone configuration (config-ephone)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(2)XT

Cisco ITS 2.0

This command was introduced

12.2(8)T

Cisco ITS 2.0

This command was integrated into Cisco IOS Release
                                          						12.2(8)T.

### Usage Guidelines

Use this command to define a voice-messaging device ID string. A
                              		  voice-messaging port registers with a device ID instead of a MAC address. To
                              		  distinguish among different voice-messaging ports, the value of the
                              		  voice-messaging device ID is used. The voice-messaging device ID is configured
                              		  to a Cisco IP phone port, which maps to a corresponding voice-messaging port.

## Examples

The following example shows how to set the voice-messaging device ID
                              		  to CiscoUM-VI1:

```
Router(config) ephone 1 Router(config-ephone) vm-device-id CiscoUM-VI1
```

### Related Commands

Description

voicemail (telephony-service)

Configures the telephone number that is speed-dialed when
                                          						the Messages button on a Cisco IP phone is pressed.

## vm-integration

To enter voice-mail integration configuration mode and enable
                              		  voice-mail integration with dual tone multifrequency (DTMF) and analog
                              		  voice-mail systems, use the vm-integration command in global
                              		  configuration mode. To disable voice-mail integration, use the no form of this command.

vm-integration

no vm-integration

### Syntax Description

This command has no arguments or keywords.

### Command Default

DTMF integration with voice-mail system is disabled.

### Command Modes

Global configuration (config)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(11)YT

Cisco SRST 2.1

This command was introduced for Cisco Survivable Remote
                                          						Site Telephony (SRST).

12.2(2)XT

Cisco ITS 2.0

This command was introduced Cisco ITS.

12.2(8)T

Cisco ITS 2.0 Cisco SRST 2.1

This command was integrated into Cisco IOS Release
                                          						12.2(8)T.

### Usage Guidelines

The vm-integration command is used to enter
                              		  voice-mail integration configuration mode to enable in-band DTMF integration
                              		  with a voice-mail system.

## Examples

The following example shows how to enter the voice-mail integration
                              		  configuration mode:

```
Router(config) vm-integration Router(config-vm-integration) pattern direct 2 CGN *
```

### Related Commands

Description

pattern direct (vm-integration)

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when a user presses the Messages button on a
                                          						phone.

pattern ext-to-ext busy (vm-integration)

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension reaches a busy
                                          						extension and the call is forwarded to voice mail.

pattern ext-to-ext no-answer (vm-integration)

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension fails to connect to
                                          						an extension and the call is forwarded to voice mail.

pattern trunk-to-ext busy (vm-integration)

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an external trunk call reaches a busy
                                          						extension and the call is forwarded to voice mail.

pattern trunk-to-ext no-answer (vm-integration)

Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when an external trunk call reaches an
                                          						unanswered extension and the call is forwarded to voice mail.

## voice class mlpp

To create a voice class for the Multilevel Precedence and Preemption
                              		  (MLPP) service, use the voice class mlpp command in global configuration mode. To remove the voice
                              		  class, use the no form of this command.

voice class mlpp tag

no voice class mlpp tag

### Syntax Description

tag

Unique number to identify the voice class. Range: 1 to
                                          						10000.

### Command Default

No voice class is configured for MLPP.

### Command Modes

Global configuration (config)

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

This command creates the voice class for MLPP attributes. Use the voice-class mlpp (dial peer) command to assign the voice class
                              		  to a dial peer.

## Examples

The following example shows the domain name set to DSN in the MLPP
                              		  voice class:

```
Router(config)# voice class mlpp Router(config-class)# service-domain dsn
```

### Related Commands

Command

Description

service-domain (voice class)

Sets the service domain name in the MLPP voice class.

voice-class mlpp (dial peer)

Assigns an MLPP voice class to a POTS or VoIP dial peer.

## voice emergency response location

To create a tag for identifying an emergency response location (ERL)
                              		  for E911 services, use the voice emergency response location command in global configuration mode. To
                              		  remove the ERL tag, use the no form of this command.

voice emergency response location tag

no voice emergency response location tag

### Syntax Description

tag

Unique number that identifies this ERL tag.

### Command Default

No ERL tag is created.

### Command Modes

Global configuration (config)

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

Use this command to create an ERL that identifies an area where
                              		  emergency teams can quickly locate a 911 caller. The ERL definition optionally
                              		  includes which ELINs are associated with the ERL and which IP phones are
                              		  located in the ERL. You can define two or fewer unique IP subnets and two or
                              		  fewer ELINs. If you define one ELIN, this ELIN is always used for phones
                              		  calling from this ERL. If you define two ELINs, the system alternates between
                              		  using each ELIN. If you define zero ELINs and phones use this ERL, the outbound
                              		  calls do not have their calling numbers translated. The PSAP sees the original
                              		  calling numbers for these 911 calls. You can optionally add the civic address
                              		  using the address command and an address description
                              		  using the name command.

## Examples

In the following example, all IP phones with the IP address of
                              		  10.X.X.X or 192.168.X.X are automatically associated with this ERL. If one of
                              		  the phones dials 911, its extension is replaced with 408 555-0100 before it
                              		  goes to the PSAP. The PSAP will see that the caller’s number is 408 555-0100.
                              		  The civic address, 410 Main St, Tooly, CA, and a descriptive identifier, Bldg 3
                              		  are included.

```
voice emergency response location 1
 elin 1 4085550100
 subnet 1 10.0.0.0 255.0.0.0
 subnet 2 192.168.0.0 255.255.0.0
 address 1,408,5550100,410,Main St.,Tooly,CA
 name Bldg 3
```

### Related Commands

Command

Description

address

Specifies a comma separated text entry (up to 250
                                          						characters) of an ERL’s civic address.

elin

Specifies a PSTN number that will replace the caller’s
                                          						extension.

name

Specifies a string (up to 32-characters) used internally to
                                          						identify or describe the emergency response location.

subnet

Defines which IP phones are part of this ERL.

## voice emergency response settings

To define 911 call behavior settings, use the voice emergency response settings command in global configuration mode. To
                              		  remove the settings, use the no form of this command.

voice emergency response settings

no voice emergency response settings

### Syntax Description

This command has no arguments or keywords.

### Command Default

No default behavior or values

### Command Modes

Global configuration (config)

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

Use this command to enable definition of the following 911 call
                              		  behavior settings:

- elin : Default ELIN to use if a 911
                                 			 caller’s IP phone’s address does not match the subnet of any location in any
                                 			 zone.

- expiry : Number of minutes a 911 call is
                                 			 associated to an ELIN in the case of a callback from the 911 operator.

- callback : Default number to contact if a
                                 			 911 callback cannot find the last 911 caller.

- logging : Syslog informational message
                                 			 that is printed to the console each time an emergency call is made. This
                                 			 feature is enabled by default, however you can disable this feature by entering
                                 			 the no form of this command.

## Examples

In the following example, if the 911 caller’s IP phone address does
                              		  not match any of the voice emergency response locations, the ELIN defined in
                              		  the voice emergency response settings configuration (4085550101) is used. After
                              		  the 911 call is placed to the PSAP, the PSAP has 120 minutes (2 hours) to call
                              		  back 408 555-0101 to reach the 911 caller. If during a callback, the last
                              		  caller’s extension number cannot be found, the call is routed to extension
                              		  7500. The outbound 911 calls do not cause a syslog message to the logging
                              		  facility (for example, to the local buffer, console, or remote host).

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

Number of minutes a 911 call is associated to an ELIN in
                                          						the case of a callback from the 911 operator.

logging

Syslog informational message printed to the console every
                                          						time an emergency call is made.

## voice emergency response zone

To create an emergency response zone, use the voice emergency response zone command in global configuration mode. To
                              		  remove the created voice emergency response zone, use the no form of this command.

voice emergency response zone tag

no voice emergency response zone tag

### Syntax Description

tag

Identifier (1-100) for the voice emergency response zone.

### Command Default

No default behavior or values

### Command Modes

Global configuration (config)

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

Use this command to create voice emergency response zones that allow
                              		  routing of 911 calls to different PSAPs.

## Examples

The following example shows an assignment of ERLs to a voice
                              		  emergency response zone. The calls have an ELIN from ERLs 8, 9, and 10. The
                              		  locations for ERLs in zone 10 are searched in the order each CLI is entered for
                              		  a phone address match because no priority order is assigned.

```
voice emergency response zone 10
location 8
location 9
location 10
```

### Related Commands

Command

Description

location

Identifies locations within an emergency response zone and
                                          						optionally assigns a priority order to the location.

## voice
                        	 hunt-group

To create a hunt
                              		  group for phones in a Cisco Unified Communications Manager Express (Cisco
                              		  Unified CME) or Cisco Unified Session Initiation Protocol (SIP) Survivable
                              		  Remote Site Telephony (SRST) system, use the voice hunt-group command in global configuration mode.
                              		  To delete a hunt group, use the no form of
                              		  this command.

voice hunt-group hunt-tag { longest-idle | parallel | peer | sequential }

no voice hunt-group hunt-tag

### Syntax Description

hunt-tag

Unique
                                          						sequence number that identifies the hunt group. Range is 1 to 100.

longest-idle

Allows
                                          						an incoming call to go first to the number that has been idle the longest for
                                          						the number of hops specified when the hunt group was defined. The longest-idle
                                          						time is determined from the last time that a phone registered, reregistered, or
                                          						went on-hook.

parallel

Allows
                                          						an incoming call to simultaneously ring all the numbers in the hunt group
                                          						member list.

peer

Allows
                                          						a round-robin selection of the first extension to ring. Ringing proceeds in a
                                          						circular manner from left to right. The round-robin selection starts with the
                                          						number left of the number that answered when the hunt-group was last called.

sequential

Allows
                                          						an incoming call to ring all the numbers in the left-to-right order in which
                                          						they were listed when the hunt group was defined.

### Command Default

By default, voice
                              		  hunt group is not created.

### Command Modes

Global configuration (config)

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

This
                                          						command was modified to add support for Cisco Unified SCCP IP phones.

12.4(20)T

Cisco
                                          						Unified CME 7.0

This
                                          						command was integrated into Cisco IOS Release 12.4(20)T.

15.2(4)M

Cisco
                                          						Unified SIP SRST 9.1

This
                                          						command was introduced in Cisco Unified SIP SRST 9.1.

15.3(4)M

Cisco
                                          						Unified CME 10.5

This
                                          						command was modified to include support for wildcards which is indicated by " * " . symbol.

### Usage Guidelines

The voice hunt-group command enters voice hunt-group
                              		  configuration mode to define a hunt group. A hunt group is a list of phone
                              		  numbers that take turns receiving incoming calls to a specific number (pilot
                              		  number), which is defined with the pilot command. The specific extensions included in the hunt group and the order and
                              		  maximum number of extensions allowed in the list are defined with the list command.

If a number in
                              		  the list is busy or does not answer, the call is redirected to the next number
                              		  in the list. The last number tried is the final number, which is defined with
                              		  the final command. If the number of times that a call is redirected to a new number
                              		  exceeds 5, you must use the max-redirect command to increase the allowable number of redirects in the
                              		  Cisco Unified CME or Cisco Unified SIP SRST system.

To configure a
                              		  new hunt group, you must specify the longest-idle , parallel , peer , or sequential keyword. To change an existing hunt group configuration, the
                              		  keyword is not required. To change the type of hunt group, for instance from
                              		  peer to sequential or sequential to peer, you must remove the existing hunt
                              		  group first by using the no form of
                              		  this command and then re-create it.

The parallel keyword creates a dial peer to allow an incoming call to ring multiple phones
                              		  simultaneously. The use of parallel hunt groups is also referred to as
                              		  application-level forking because it enables the forking of a call to multiple
                              		  destinations. A pilot dial peer cannot be used as a voice hunt group and a hunt
                              		  group at the same time.

While ephone
                              		  hunt groups only support Cisco Unified SCCP IP phones, a voice hunt group
                              		  supports either a Cisco Unified SCCP IP phone or a Cisco Unified SIP IP phone.

With the voice
                              		  hunt group feature preconfigured in the Cisco Unified SIP SRST router, voice
                              		  hunt groups continue to be supported after phones fallback from a Cisco Unified
                              		  Communications Manager (Cisco Unified CM) to a Cisco Unified SIP SRST router.

## Examples

The following
                              		  example shows how to define longest-idle hunt group 1 with pilot number 7501,
                              		  final number 8000, and nine numbers in the list. After a call is redirected six
                              		  times (makes 6 hops), it is redirected to the final number 8000.

```
Router(config)# voice hunt-group 1 longest-idle Router(config-voice-hunt-group)# pilot 7501 Router(config-voice-hunt-group)# list 7001, 7002, 7023, 7028, 7045, 7062, 7067, 7072, 7079 Router(config-voice-hunt-group)# final 8000 Router(config-voice-hunt-group)# hops 6 Router(config-voice-hunt-group)# timeout 20 Router(config-voice-hunt-group)# exit
```

The following
                              		  example shows how to define peer hunt group number 2. Callers dial the pilot
                              		  number 5610 to reach the hunt group. The first extension to ring the first time
                              		  that this hunt group is called is 5601. If 5601 does not answer, the hunt
                              		  proceeds from left to right, beginning with the extension directly to the
                              		  right. If none of those extensions answer, the call is forwarded to extension
                              		  6000, which is the number for the voice-mail service.

The second time
                              		  someone calls the hunt group, the first extension to ring is 5602 if 5601 was
                              		  answered during the previous call.

```
Router(config)# voice hunt-group 2 peer Router(config-voice-hunt-group)# pilot 5610 Router(config-voice-hunt-group)# list 5601, 5602, 5617, 5633 Router(config-voice-hunt-group)# final 6000 Router(config-voice-hunt-group)# timeout 30 Router(config-voice-hunt-group)# exit
```

The following
                              		  example shows how to define sequential hunt group number 3. When callers dial
                              		  extension 5601, the first phone to ring is 5001, then 5002, 5017, and 5028. If
                              		  none of those extensions answer, the call is forwarded to extension 6000, which
                              		  is the number for the voice-mail service.

```
Router(config)# voice hunt-group 3 sequential Router(config-voice-hunt-group)# pilot 5601 Router(config-voice-hunt-group)# list 5001, 5002, 5017, 5028 Router(config-voice-hunt-group)# final 6000 Router(config-voice-hunt-group)# timeout 30 Router(config-voice-hunt-group)# exit
```

The following
                              		  example shows how to define a parallel hunt group. When callers dial extension
                              		  1000, extensions 1001, 1002, and so forth ring simultaneously. The first
                              		  extension to answer is connected. All other call legs are disconnected. If none
                              		  of the extensions answer, the call is forwarded to extension 2000, which is the
                              		  number for the voice-mail service.

```
Router(config)# voice hunt-group 4 parallel Router(config-voice-hunt-group)# pilot 1000 Router(config-voice-hunt-group)# list 1001, 1002, 1003, 1004 Router(config-voice-hunt-group)# final 2000 Router(config-voice-hunt-group)# timeout 20 Router(config-voice-hunt-group)# exit
```

The following
                              		  example shows the support for wildcard slots in voice hunt-groups.

```
Router(config)# Voice hunt-group 1 parallel Router(config-voice-hunt-group)# pilot number 100 Router(config-voice-hunt-group)# List 1001, 1002, 1002, *, * Router(config-voice-hunt-group)# exit
```

### Related Commands

Command

Description

final (voice hunt-group)

Defines the last extension in a voice hunt group.

hops
                                          						(voice hunt-group)

Defines the number of times that a call is redirected to the next phone number
                                          						in a peer voice hunt-group list before proceeding to the final phone number.

list (voice hunt-group)

Defines the phone numbers that participate in a voice hunt group.

max-redirect

Changes the number of times that a call can be redirected by call forwarding or
                                          						transfer within a Cisco Unified CME system.

pilot (voice hunt-group)

Defines the phone number that callers dial to reach a voice hunt group.

timeout (voice hunt-group)

Sets
                                          						the number of seconds after which a call that is not answered is redirected to
                                          						the next number in the hunt-group list and defines the last phone number in the
                                          						hunt group.

## voice-hunt-groups
                        	 login

To enable a voice
                              		  register dn or ephone dn to join or unjoin voice hunt-groups dynamically, use
                              		  the voice-hunt-groups login command in voice register dn configuration
                              		  mode. To disable this capability, use the no form of
                              		  this command.

voice-hunt-groups login

no voice-hunt-groups login

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

A voice register
                              		  dn or ephone dn is not allowed to dynamically join and unjoin voice hunt
                              		  groups.

### Command Modes

voice register dn configuration (config-voice-register-dn)

ephone  dn configuration (config-ephone-dn)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

15.4(3)M

Cisco
                                          						Unified CME 10.5

This
                                          						command was introduced.

### Usage Guidelines

Use the show voice
                                    				hunt-groups command to display current hunt group members,
                              		  including those who joined the group dynamically.

## Examples

The following
                              		  example creates five voice register dns and a hunt group that includes the
                              		  first two voice register dn and two wildcard slots. The last three voice
                              		  register dns are enabled for voice hunt group dynamic membership. Each of them
                              		  can join and unjoin the hunt group whenever one of the slots is available.

```
voice register dn 22
 number 4566
voice register dn 23
 number 4567
voice register dn 24
 number 4568
 voice-hunt-groups login
voice register dn 25
 number 4569
 voice-hunt-groups login
voice register dn 26
 number 4570
 voice-hunt-groups login
voice-hunt-groups 1 peer
 list 4566,4567,*,*
 final 7777
```

## Examples

The following
                              		  example creates three ephone dns and a hunt group that includes the first two
                              		  ephone dn and two wildcard slots. The last one ephone dn is enabled for voice
                              		  hunt group dynamic membership. Each of them can join and unjoin the hunt group
                              		  whenever one of the slots is available

```
ephone-dn 22
 number 4566
ephone-dn 23
 number 4567
ephone-dn 24
 number 4568
 voice-hunt-groups login
voice-hunt-groups 1 peer
 list 4566,4567,*,*
 final 7777
```

### Related Commands

Command

Description

show voice hunt-groups

Displays voice-hunt group configuration, current status, and statistics.

## voice lpcor
                        	 call-block cause

To define the
                              		  cause code that is used when a call is blocked because LPCOR validation fails,
                              		  use the voice lpcor call-block cause command in global configuration mode. To reset to the default,
                              		  use the no form of
                              		  this command.

voice lpcor call-block cause cause-code

no voice lpcor call-block cause

### Syntax Description

cause-code

Number
                                          						of the cause code to generate when a call is blocked by the LPCOR validation
                                          						process. Range: 1 to 180.

### Command Default

Default cause
                              		  code is 63 (serv/opt-unavail-unspecified).

### Command Modes

Global configuration (config)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

15.0(1)XA

Cisco
                                          						Unified CME 8.0

This
                                          						command was introduced.

15.1(1)T

Cisco
                                          						Unified CME 8.0

This
                                          						command was integrated into Cisco IOS Release 15.1(1)T.

### Usage Guidelines

The following
                              		  table lists the available cause codes.

Message

Description

Code
                                          					 Number

access-info-discard

access
                                          					 info discarded (43)

43

b-cap-not-implemented

bearer
                                          					 capability not implemented (65)

65

b-cap-restrict

restricted digital info bc only (70)

70

b-cap-unauthorized

bearer
                                          					 capability not authorized (57)

57

b-cap-unavail

bearer
                                          					 capability not available (58)

58

call-awarded

call
                                          					 awarded (7)

7

call-cid-in-use

call
                                          					 exists call id in use (83)

83

call-clear

call
                                          					 cleared (86)

86

call-reject

call
                                          					 rejected (21)

21

cell-rate-unavail

cell
                                          					 rate not available (37)

37

channel-unacceptable

channel
                                          					 unacceptable (6)

6

chantype-not-implement

chan
                                          					 type not implemented (66)

66

cid-in-use

call id
                                          					 in use (84)

84

codec-incompatible

codec
                                          					 incompatible (171)

171

cug-incalls-bar

cug
                                          					 incoming calls barred (55)

55

cug-outcalls-bar

cug
                                          					 outgoing calls barred (53)

53

dest-incompatible

incompatible destination (88)

88

dest-out-of-order

destination out of order (27)

27

dest-unroutable

no
                                          					 route to destination (3)

3

dsp-error

dsp
                                          					 error (172)

172

dtl-trans-not-node-id

dtl
                                          					 transit not my node id (160)

160

facility-not-implemented

facility not implemented (69)

69

facility-not-subscribed

facility not subcribed (50)

50

facility-reject

facility rejected (29)

29

glare

glare
                                          					 (15)

15

glaring-switch-pri

glaring
                                          					 switch PRI (180)

180

htspm-oos

HTSPM
                                          					 out of service (129)

129

ie-missing

mandatory ie missing (96)

96

ie-not-implemented

ie not
                                          					 implemented (99)

99

info-class-inconsistent

inconsistency in info and class (62)

62

interworking

interworking (127)

127

invalid-call-ref

invalid
                                          					 call ref value (81)

81

invalid-ie

invalid
                                          					 ie contents (100)

100

invalid-msg

invalid
                                          					 message (95)

95

invalid-number

invalid
                                          					 number (28)

28

invalid-transit-net

invalid
                                          					 transit network (91)

91

misdialled-trunk-prefix

misdialled trunk prefix (5)

5

msg-incomp-call-state

message
                                          					 in incomp call state (101)

101

msg-not-implemented

message
                                          					 type not implemented (97)

97

msgtype-incompatible

message
                                          					 type not compatible (98)

98

net-out-of-order

network
                                          					 out of order (38)

38

next-node-unreachable

next
                                          					 node unreachable (128)

128

no-answer

no user
                                          					 answer (19)

19

no-call-suspend

no call
                                          					 suspended (85)

85

no-channel

channel
                                          					 does not exist (82)

82

no-circuit

no
                                          					 circuit (34)

34

no-cug

non
                                          					 existent cug (90)

90

no-dsp-channel

no dsp
                                          					 channel (170)

170

no-req-circuit

no
                                          					 requested circuit (44)

44

no-resource

no
                                          					 resource (47)

47

no-response

no user
                                          					 response (18)

18

no-voice-resources

no
                                          					 voice resources available (126)

126

non-select-user-clear

non
                                          					 selected user clearing (26)

26

normal-call-clear

normal
                                          					 call clearing (16)

16

normal-unspecified

normal
                                          					 unspecified (31)

31

not-in-cug

user
                                          					 not in cug (87)

87

number-changeed

number
                                          					 changed (22)

22

param-not-implemented

non
                                          					 implemented param passed on (103)

103

perm-frame-mode-oos

perm
                                          					 frame mode out of service (39)

39

perm-frame-mode-oper

perm
                                          					 frame mode operational (40)

40

precedence-call-block

precedence call blocked (46)

46

preempt

preemption (8)

8

preempt-reserved

preemption reserved (9)

9

protocol-error

protocol error (111)

111

qos-unavail

qos
                                          					 unavailable (49)

49

rec-timer-exp

recovery on timer expiry (102)

102

redirect-to-new-destination

redirect to new destination (23)

23

req-vpci-vci-unavail

requested vpci vci not available (35)

35

send-infotone

send
                                          					 info tone (4)

4

serv-not-implemented

service
                                          					 not implemented (79)

79

serv/opt-unavail-unspecified

service
                                          					 or option not available unspecified (63)

63

stat-enquiry-resp

response to status enquiry (30)

30

subscriber-absent

subscriber absent (20)

20

switch-congestion

switch
                                          					 congestion (42)

42

temp-fail

temporary failure (41)

41

transit-net-unroutable

no
                                          					 route to transit network (2)

2

unassigned-number

unassigned number (1)

1

unknown-param-msg-discard

unrecognized param msg discarded (110)

110

unsupported-aal-parms

aal
                                          					 parms not supported (93)

93

user-busy

user
                                          					 busy (17)

17

vpci-vci-assign-fail

vpci
                                          					 vci assignment failure (36)

36

vpci-vci-unavail

no vpci
                                          					 vci available (45)

45

## Examples

The following
                              		  example shows the cause code set to 79:

```
Router(config)# voice lpcor call-block cause 79
```

### Related Commands

Command

Description

voice lpcor policy

Creates a LPCOR policy for a resource group.

## voice lpcor custom

To define the logical partitioning class of restriction (LPCOR)
                              		  resource groups on the Cisco Unified CME router, use the voice lpcor custom command in global configuration mode. To remove the custom
                              		  resource list, use the no form of this command.

voice lpcor custom

no voice lpcor custom

### Syntax Description

This command has no arguments or keywords.

### Command Default

Custom LPCOR resource list is not defined.

### Command Modes

Global configuration (config)

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

This command enters LPCOR custom configuration mode where you define
                              		  the name of each of your resource groups using the index command. Only one custom resource list
                              		  is allowed on a Cisco Unified CME router. After you add a resource group to
                              		  this list, you must then create a LPCOR policy for each resource group that
                              		  requires call restrictions.

## Examples

The following example shows a LPCOR configuration with six resource
                              		  groups:

```
voice lpcor custom
 group 1 sccp_phone_local
 group 2 sip_phone_local
 group 3 analog_phone_local
 group 4 sip_remote
 group 5 sccp_remote
 group 6 isdn_local
```

### Related Commands

Command

Description

group (lpcor custom)

Adds a LPCOR resource group to the custom resource list.

voice lpcor enable

Enables LPCOR functionality on the Cisco Unified CME
                                          						router.

voice lpcor policy

Creates a LPCOR policy for a resource group.

## voice lpcor enable

To enable logical partitioning class of restriction (LPCOR)
                              		  functionality on the Cisco Unified CME router, use the voice lpcor enable command in global configuration mode. To reset to the default,
                              		  use the no form of this command.

voice lpcor enable

no voice lpcor enable

### Syntax Description

This command has no arguments or keywords.

### Command Default

LPCOR capability is disabled.

### Command Modes

Global configuration

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

After using this command, use the voice lpcor custom command to create a list of your LPCOR
                              		  resource groups.

## Examples

The following example shows a configuration with LPCOR enabled and a
                              		  custom resource list :

```
voice lpcor enable
voice lpcor custom
 group 1 local_sccp_phone_1
 group 2 local_sip_phone_1
 group 3 local_analog_phone_1
 group 4 local_sccp_phone_2
!
voice lpcor policy local_sccp_phone_1
 accept local_sip_phone_1
 accept local_analog_phone_1
 accept local_sccp_phone_2
```

### Related Commands

Command

Description

voice lpcor custom

Defines the LPCOR resource groups on the Cisco Unified CME
                                          						router.

voice lpcor policy

Creates a LPCOR policy for a resource group.

## voice lpcor ip-phone mobility

To set the default LPCOR policy for mobility-type phones, use the voice lpcor ip-phone mobility command in global configuration mode. To reset to the default,
                              		  use the no form of this command.

voice lpcor ip-phone mobility { incoming | outgoing } lpcor-group

no voice lpcor ip-phone mobility { incoming | outgoing }

### Syntax Description

incoming

Sets default LPCOR policy for incoming calls.

outgoing

Sets default LPCOR policy for outgoing calls.

lpcor-group

Name of the LPCOR resource group.

### Command Default

Default LPCOR policy is not defined for mobility-type phones.

### Command Modes

Global configuration (config)

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

This command defines the default LPCOR policy for a mobility-type
                              		  phone if the LPCOR policy cannot be provisioned using the LPCOR IP-phone subnet
                              		  table.

## Examples

The following example shows that the default LPCOR policy for
                              		  mobility-type phones is set to remote_group1. Any mobility-type phones with a
                              		  shared IP address from DHCP pool1 are considered local IP phones and are
                              		  associated with the local_group1 LPCOR policy. Other mobility-type phones
                              		  without a shared IP address are considered remote IP phones and are associated
                              		  with the remote_group1 default LPCOR policy.

```
voice lpcor ip-phone subnet incoming
 index 1 local_group1 dhcp-pool pool1
!
voice lpcor ip-phone subnet outgoing
 index 1 local_group1 dhcp-pool pool1
!
voice lpcor ip-phone mobility incoming remote_group1
voice lpcor ip-phone mobility outgoing remote_group1
```

### Related Commands

Command

Description

voice lpcor ip-phone subnet

Creates a LPCOR IP-phone subnet table for calls to or from
                                          						a mobility-type phone.

## voice lpcor ip-phone subnet

To create a logical partitioning class of restriction (LPCOR)
                              		  IP-phone subnet table for calls to or from a mobility-type phone, use the voice lpcor ip-phone subnet command in global configuration mode. To reset to the default,
                              		  use the no form of this command.

voice lpcor ip-phone subnet { incoming | outgoing }

no voice lpcor ip-phone subnet { incoming | outgoing }

### Syntax Description

incoming

Creates IP-phone subnet table for incoming calls from
                                          						mobility-type phone.

outgoing

Creates IP-phone subnet table for outgoing calls from
                                          						mobility-type phone.

### Command Default

IP-phone subnet table is not created.

### Command Modes

Global configuration (config)

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

This command is used for mobility-type phones only, which can include
                              		  Extension Mobility phones, teleworker remote phones, and Cisco IP Communicator
                              		  softphones.

This command enters LPCOR IP-phone subnet configuration mode to add
                              		  LPCOR groups to the incoming or outgoing IP-phone subnet tables. Two IP-phone
                              		  subnet tables, one for incoming calls and one for outgoing calls, can be
                              		  defined on each Cisco Unified CME router and can include up to 50 IP address or
                              		  DHCP pool entries.

A LPCOR policy is dynamically associated with calls to and from a
                              		  mobility-type phone based on its current IP address or DHCP pool.

## Examples

The following example shows :

```
voice lpcor ip-phone subnet incoming
 index 1 local_g2 10.0.10.23 255.255.255.0 vrf vrf-group2
 index 2 remote_g2 171.19.0.0 255.255.0.0
 index 3 local_g1 dhcp-pool pool1
 
voice lpcor ip-phone subnet outgoing
 index 1 local_g4 10.1.10.23 255.255.255.0 vrf vrf-group2
 index 2 remote_g4 171.19.0.0 255.255.0.0
 index 3 local_g5 dhcp-pool pool1
```

### Related Commands

Command

Description

index (ip-phone)

Adds a LPCOR group to the IP-phone subnet table.

lpcor type

Specifies the LPCOR type for an IP phone.

voice lpcor ip-phone mobility

Sets the default LPCOR policy for mobility-type phones.

## voice lpcor ip-trunk subnet incoming

To create a logical partitioning class of restriction (LPCOR)
                              		  IP-trunk subnet table for incoming calls from a VoIP trunk, use the voice lpcor ip-trunk subnet incoming command in global configuration mode. To reset to the default,
                              		  use the no form of this command.

voice lpcor ip-trunk subnet incoming

no voice lpcor ip-trunk subnet incoming

### Syntax Description

This command has no arguments or keywords.

### Command Default

IP-trunk subnet table is not created.

### Command Modes

Global configuration (config)

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

This command enters LPCOR IP-trunk subnet configuration mode to add
                              		  LPCOR groups to the IP-trunk subnet table. One IP-trunk subnet table,
                              		  containing up to 50 index entries, can be defined on each Cisco Unified CME
                              		  router for incoming calls from H.323 or SIP trunks.

Incoming VoIP trunk calls are associated with a LPCOR policy by
                              		  matching the IP address or hostname in the IP-trunk subnet table first. If the
                              		  IP address or hostname is not found in the table, the LPCOR policy specified
                              		  with the lpcor incoming command in voice service configuration
                              		  mode is applied.

## Examples

The following example shows three resource groups are included in the
                              		  IP-trunk subnet table:

```
voice lpcor ip-trunk subnet incoming
 index 1 h323_group1 172.19.33.0 255.255.255.0
 index 2 sip_group1 172.19.22.0 255.255.255.0
 index 3 sip_group2 hostname sipexample
```

### Related Commands

Command

Description

index (lpcor ip-trunk)

Adds a LPCOR resource group to the IP trunk subnet table.

lpcor incoming

Associates a LPCOR resource-group policy with an incoming
                                          						call.

voice lpcor ip-phone subnet

Creates a LPCOR IP-phone subnet table for calls to or from
                                          						a mobility-type phone.

## voice lpcor policy

To create a logical partitioning class of restriction (LPCOR) policy
                              		  for a resource group, use the voice lpcor policy command in global configuration mode. To reset to the default,
                              		  use the no form of this command.

voice lpcor policy lpcor-group

no voice lpcor policy lpcor-group

### Syntax Description

lpcor-group

Name of the LPCOR resource group.

### Command Default

LPCOR policy is not defined.

### Command Modes

Global configuration (config)

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

You can define one policy for each LPCOR resource group. The policy
                              		  defines the other resource groups from which this resource group can accept
                              		  calls. You must first name the policy by including it in the custom resource
                              		  list using the voice lpcor custom command.

If you do not explicitly include any resource groups in the policy by
                              		  using the accept command, that policy blocks all
                              		  incoming calls that are associated with any LPCOR policy other than its own.

If a LPCOR policy is not defined for a target destination, the target
                              		  can accept incoming calls from any resource group.

## Examples

The following examples show a LPCOR configuration with four resource
                              		  groups:

```
voice lpcor custom
 index 1 siptrunk
 index 2 h323trunk
 index 3 pstn
 index 4 voicemail
!
```

The LPCOR policy for h323trunk accepts calls from the voicemail group
                              		  and rejects calls from the siptrunk and pstn groups:

```
voice lpcor policy h323trunk
 accept voicemail
!
```

The LPCOR policy for pstn blocks calls from the siptrunk, h323trunk,
                              		  and voicemail groups:

```
voice lpcor policy pstn
!
```

The LPCOR policy for voicemail accepts calls from the siptrunk,
                              		  h323trunk, and pstn groups:

```
voice lpcor policy voicemail
 accept siptrunk
 accept h323trunk
 accept pstn
```

The siptrunk group does not have a LPCOR policy defined so it can
                              		  accept calls from any of the other resource groups.

### Related Commands

Command

Description

accept

Allows a LPCOR resource group to accept incoming calls from
                                          						another resource group.

show voice lpcor policy

Displays the LPCOR policy for the specified resource group.

voice lpcor custom

Defines the LPCOR resource groups on the Cisco Unified CME
                                          						router.

## voice mlpp

To enter MLPP configuration mode to enable MLPP service, use the
                              		  voice service command in global configuration mode. To disable MLPP service,
                              		  use the no form of this command.

voice mlpp

no voice mlpp

### Syntax Description

This command has no keywords or arguments.

### Command Default

No default behavior or values.

### Command Modes

Global configuration (config)

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

Voice-mlpp configuration mode is used for the gateway globally.

## Examples

The following example shows how to enter voice-mlpp configuration
                              		  mode:

```
Router(config)# voice mlpp Router(config-voice-mlpp)# access-digit
```

### Related Commands

Command

Description

access-digit

Defines the access digit that phone users dial to request a
                                          						precedence call.

mlpp preemption

Enables calls on an SCCP phone or analog FXS port to be
                                          						preempted.

preemption trunkgroup

Enables preemption capabilities on a trunk group.

## voice moh-group

To enter voice-moh-group configuration mode and set up music on hold
                              		  (MOH) group parameters, use the voice moh-group command in global configuration mode. To remove the music on
                              		  hold (MOH) group parameters from the configuration for SCCP IP phones, use the no form of this command.

voice moh-group moh-group tag

no voice moh-group tag

### Syntax Description

tag

Specifies a moh-group number tag (1-5) to be used for music
                                          						on hold group parameters.

### Command Default

No voice-moh-group is enabled.

### Command Modes

Global configuration (config)

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

This command enters the voice-moh-group configuration mode for
                              		  configuring music on hold (MOH) group parameters for SCCP IP phones in Cisco
                              		  Unified CME or in Cisco Unified SRST.

## Examples

The following example shows how to enter voice-moh-group
                              		  configuration mode for configuring a moh group in Cisco Unified CME. This
                              		  example also includes the command to configure a music on hold (MOH) flash file
                              		  for this voice-moh- group.

```
Router(config)# voice-moh-group 1 Router(config-voice-moh-group)#moh minuet.wav
```

### Related Commands

moh

Enables music on hold from a flash audio feed.

multicast moh

Enables multicast of the music-on-hold audio stream.

extension-range

Defines extension range for a clients calling a
                                          						voice-moh-group.

## voice register dialplan

To enter voice register dialplan configuration mode to define a dial
                              		  plan for SIP phones, use the voice register dialplan command in global configuration mode. To
                              		  remove the dialplan, use the no form of this command.

voice register dialplan dialplan-tag

no voice register dialplan dialplan-tag

### Syntax Description

dialplan-tag

Number that identifies the dial plan. Range: 1 to 24.

### Command Default

No dial plan is defined.

### Command Modes

Global configuration (config)

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

A dial plan allows a SIP phone to determine when enough digits are
                              		  collected for call processing to take place. You define a dial plan using this
                              		  command and then apply the dial plan to a SIP phone by using the dialplan command.

Dial plans allow SIP phones to perform pattern recognition as user
                              		  input is collected. After a defined pattern is recognized, a SIP INVITE message
                              		  is automatically sent to Cisco Unified CME and the user does not have to press
                              		  the Dial key or wait for the interdigit timeout.

This command creates a dial plan file that is downloaded to the phone
                              		  when the phone is reset or restarted.

## Examples

The following example shows how to create dial plan 10 for a Cisco
                              		  Unified IP Phone 7905:

```
Router(config)# voice register dialplan 10 Router(config-register-dialplan)# type 7905-7912 Router(config-register-dialplan)# pattern 52... Router(config-register-dialplan)# pattern 91.......
```

### Related Commands

Description

dialplan

Assigns a dial plan to a SIP phone.

filename

Specifies a custom XML configuration file that contains the
                                          						dial patterns to use for a SIP dial plan.

pattern (voice register dialplan)

Defines a dial pattern for a SIP dial plan.

show voice register dialplan

Displays all configuration information for a specific SIP
                                          						dial plan.

type (voice register dialplan)

Defines a phone type for a SIP dial plan.

## voice register dn

To enter voice register dn configuration mode to define an extension
                              		  for a phone line, intercom line, voice-mail port, or a message-waiting
                              		  indicator (MWI), use the voice register dn command in global configuration mode. To remove
                              		  the directory number, use the no form of this command.

voice register dn dn-tag

no voice register dn dn-tag

### Syntax Description

dn-tag

Unique sequence number that identifies a particular
                                          						directory number during configuration tasks. Range is 1 to 150, or the maximum
                                          						defined by the max-dn command.

### Command Default

Directory number is not defined.

### Command Modes

Global configuration (config)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4 and Cisco SIP SRST 3.4

This command was introduced.

### Usage Guidelines

Use this command to create directory numbers for SIP IP phones
                              		  directly connected in Cisco Unified CME. In voice register dn configuration
                              		  mode, you assign an extension number by using the number command, a name to appear in the local
                              		  directory by using the name command, and other provisioning
                              		  parameters by using various commands.

Before using this command, set the maximum number of directory
                              		  numbers to appear in your system by using the max-dn command in voice register global
                              		  configuration mode.

The name or label associated with a directory number configured under voice register dn configuration mode cannot contain special characters such as quotes ("), angle brackets (<, >), ampersand (&), and percentage
                                          (%).

## Examples

The following example shows how to enter voice register dn
                              		  configuration mode for directory number 4 and forward calls to extension 8888
                              		  when extension 1001 does not answer:

```
Router(config)# voice register dn 4 Router(config-register-dn)# number 1001 Router(config-register-dn)# call-forward phone noan 8888 Router(config-register-dn)# call-forward b2bua all 5454 Router(config-register-dn)# call-forward b2bua busy 5705 Router(config-register-dn)# call-forward b2bua mbox 5550 Router(config-register-dn)# call-forward b2bua noan 5050 timeout 20 Router(config-register-dn)# after-hour exempt
```

### Related Commands

Description

max-dn (voice register global)

Sets the maximum number of SIP phone directory numbers
                                          						(extensions) supported by a Cisco CME router.

mode (voice register global)

Enables the mode for provisioning SIP phones in a Cisco
                                          						CallManager Express (Cisco CME) system.

number (voice register pool)

Configures a valid number for a SIP phone.

## voice register global

To enter voice register global configuration mode in order to set
                              		  global parameters for all supported Cisco SIP IP phones in a Cisco Unified CME
                              		  or Cisco Unified Session Initiation Protocol (SIP) Survivable Remote Site
                              		  Telephony (SRST) environment, use the voice register global command in global configuration mode. To
                              		  automatically remove the existing DNs, pools, and global dialplan patterns, use
                              		  the no form of this command.

voice register global

no voice register global

### Syntax Description

This command has no arguments or keywords.

### Command Default

There are no system-level parameters configured for SIP IP phones.

### Command Modes

Global configuration (config)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was introduced.

15.0(1)XA

Cisco SIP SRST 8.0

This command was updated to display the signaling transport
                                          						protocol.

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SRST 8.1

The no form of the command was modified.

### Usage Guidelines

Cisco Unified CME

Use this command to set provisioning parameters for all supported SIP
                              		  phones in a Cisco Unified CME system.

Cisco Unified SIP SRST

Use this command to set provisioning parameters for multiple pools;
                              		  that is, all supported Cisco SIP IP phones in a SIP SRST environment.

Cisco Unified CME 8.1 enhances the no form of voice register global
                              		  command. The no voice register global command clears global configuration along
                              		  with pools and DN configuration and also removes the configurations for voice
                              		  register template, voice register dialplan, and voice register session-server.
                              		  A confirmation is sought before the cleanup is made.

In Cisco Unified SRST 8.1 and later versions, the no voice register
                              		  global command removes pools and DNs along with the global configuration.

The name or label associated with a directory number configured under voice register global configuration mode cannot contain special characters such as quotes ("), angle brackets (<, >), ampersand (&), and percentage
                                          (%).

## Examples

## Examples

The following is a partial sample output from the show voice register global command. All of the parameters listed were set under voice
                              		  register global configuration mode:

```
Router# show voice register global CONFIG [Version=4.0(0)]
========================
Version 4.0(0)
Mode is cme
Max-pool is 48
Max-dn is 48
Source-address is 10.0.2.4 port 5060
Load 7960-40 is P0S3-07-4-07
Time-format is 12
Date-format is M/D/Y
Time-zone is 5
Hold-alert is disabled
Mwi stutter is disabled
Mwi registration for full E.164 is disabled
Dst auto adjust is enabled
 start at Apr week 1 day Sun time 02:00
 stop  at Oct week 8 day Sun time 02:00
```

## Examples

## Examples

The following is a sample output from no voice register global
                              		  command:

```
Router(config)# no voice register global
This will remove all the existing DNs, Pools, Templates,
Dialplan-Patterns, Dialplans and Feature Servers on the system.
Are you sure you want to proceed? Yes/No? [no]:
```

### Related Commands

Command

Description

allow connections sip to sip

Allows connections between SIP endpoints in a Cisco
                                          						multiservice IP-to-IP gateway.

application (voice register global)

Selects the session-level application for all dial peers
                                          						associated with SIP phones.

mode (voice register global)

Enables the mode for provisioning SIP phones in a Cisco
                                          						Unified system.

## voice register pool

To enter voice register pool configuration mode and create a pool
                              		  configuration for a SIP IP phone in Cisco Unified CME or for a set of SIP
                              		  phones in Cisco Unified SIP SRST, use the voice register pool command in global configuration mode. To
                              		  remove the pool configuration, use the no form of this command.

voice register pool pool-tag

no voice register pool pool-tag

### Syntax Description

pool-tag

Unique number assigned to the pool. Range is 1 to 100.

### Command Default

There is no pool configured.

### Command Modes

Global configuration (config)

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

This command was added to Cisco CME.

### Usage Guidelines

Cisco Unified CME

Use this command to set phone-specific parameters for SIP phones in a
                              		  Cisco Unified CME system. Before using this command, enable the mode cme command and set the maximum number of SIP
                              		  phones supported in your system by using the max-pool command.

Cisco Unified SIP SRST

Use this command to enable user control on which registrations are to
                              		  be accepted or rejected by a SIP SRST device. The voice register pool command
                              		  mode can be used for specialized functions and to restrict registrations on the
                              		  basis of MAC, IP subnet, and number range parameters.

## Examples

## Examples

The following example shows how to enter voice register pool
                              		  configuration mode and forward calls to extension 9999 when extension 2001 is
                              		  busy:

```
Router(config)# voice register pool 10 Router(config-register-pool)# type 7960 Router(config-register-pool)# number 1 2001 Router(config-register-pool)# call-forward busy 9999 mailbox 1234
```

## Examples

The following partial sample output from the show running-config command shows that several voice register pool commands are
                              		  configured within voice register pool 3:

```
voice register pool 3
 id network 10.2.161.0 mask 255.255.255.0
 number 1 95... preference 1
 cor outgoing call95 1 95011
 max registrations 5
 voice-class codec 1
```

### Related Commands

Description

max-pool (voice register global)

Sets the maximum number of SIP phones that are supported by
                                          						a Cisco Unified CME system.

mode (voice register global)

Enables the mode for provisioning SIP phones in a Cisco
                                          						Unified CME system.

number (voice register pool)

Configures a valid number for a SIP phone.

type (voice register pool)

Defines a Cisco IP phone type.

## voice register
                        	 pool-type

To enter voice
                              		  register pool-type configuration mode and add a new Cisco Unified SIP IP phone
                              		  to Cisco Unified CME, use the voice register
                                    				pool-type command in global configuration mode. To return to the
                              		  default, use the no form of
                              		  this command.

voice register pool-type [device-reference supported
                                 				  phone-type ] [device-name name {device-type type } [addons max-addons ] {num-lines max-lines } [transport-type {udp | tcp} ] [gsm-handoff] [telnet] [phoneload] [xml-config xml-config value }

no voice register pool-type [device-reference supported
                                 				  phone-type ] [device-name name {device-type type } [addons max-addons ] {num-lines max-lines } [transport-type {udp | tcp} ] [gsm-handoff] [telnet] [phoneload] [xml-config xml-config value }

## Syntax Description

(Optional)
                                       					 Defines the nearest-supported phone from which a new Cisco Unified SIP IP phone
                                       					 can inherit properties without the explicit configuration of the parameters.

For a
                                       					 list of the names, types, and corresponding properties of supported phones, see
                                       					 the below table.

(Optional)
                                       					 Defines the description string for the new phone device.

Defines
                                       					 a phone type for a new Cisco Unified SIP IP phone.

(Optional) Defines the maximum number of add-on modules
                                       					 supported by the new phone device. The maximum allowed value is 3.

Defines
                                       					 the maximum number of lines supported by the phone. Range is 1 to ???.

(Optional) Defines the transport protocol supported by the
                                       					 phone.

- udp—User Datagram
                                             						Protocol (UDP) is used.

- tcp—Transmission Control
                                             						Protocol (TCP) is used.

(Optional) Enables phone support for Global System for Mobile
                                       					 Communications (GSM) handoff.

(Optional) Enables phone support for Telnet access.

(Optional) Enables support for phone loads.

(Optional) Defines the phone-specific XML tags to be used in the
                                       					 configuration file.

- xml-tag—Phone-specific
                                          						XML tag.

- value—Value of the XML
                                          						tag.

### Command Default

The Cisco
                              		  Unified 7965 SIP IP phone model is used as the default phone device reference.

### Command Modes

Global configuration (config)

## Command History

15.3(3)M

This
                                       					 command was introduced.

### Usage Guidelines

When the
                              		  device-reference keyword is not configured and phone properties are not
                              		  explicitly configured, the Cisco Unified 7965 SIP IP phone model is used as the
                              		  default phone device reference and its corresponding phone properties are
                              		  inherited by the new Cisco Unified SIP IP phone.

The description
                              		  string configured with the device-name keyword is displayed as a help string when the new phone type is listed with
                              		  the supported device types for the type (voice register pool) command.

With respect to
                              		  the transport-type keyword, most Cisco Unified SIP IP phones use UDP
                              		  as the default transport protocol to connect to Cisco Unified CME while
                              		  CiscoMobile-iOS and Jabber-Android use TCP. These configurations can be changed
                              		  using the session-transport {udp | tcp} command in voice register pool or voice
                              		  register template configuration mode.

## Examples

The following
                              		  example shows how to inherit the existing features of its phone model (9951)
                              		  using the Fast-Track configuration approach. Phone model “9951” is used as the
                              		  value of the reference-pooltype keyword. The maxNumCalls XML tag defines “3” as
                              		  the maximum number of calls allowed per line while the busyTrigger XML tag
                              		  defines "3" as the number of calls that triggers call forward busy per line on
                              		  the phone.

```
voice register pool-type 9900
reference-pooltype 9951 device-name “SIP Phone 9900 addon module”
num-lines 24
addons 3
transport tcp
telnet
gsm-handoff
phoneload
xml-config maxNumCalls 3
xml-config busyTrigger 3
voice register pool 10
type 9900 addon 1 CKEM 2 CKEM 3 CKEM
id mac 1234.4567.7891
voice register global
mode cme
load 9900 P0S3-06-0-00
```

## Examples

The following
                              		  example shows how to inherit the existing features of its parent phone type
                              		  (Cisco Unified 6921 SIP IP phone) using the Fast-Track configuration approach.
                              		  Parent phone model “6921” is used as the value of the referencetype keyword.

```
voice register pool-type 6922
reference-pooltype 6921 device-name “SIP Phone 6922”

voice register pool 11
type 6922
id mac 1234.4567.7890
```

### Related Commands

Command

Description

Specifies the transport layer protocol that a SIP phone uses
                                          						to connect to Cisco Unified CME.

Defines a phone type for a SIP phone.

## voice register session-server

To enter voice register session-server configuration mode to enable
                              		  and configure a session manager in Cisco Unified CME for an external feature
                              		  server, use the voice register session-server command in global configuration mode. To remove a session
                              		  manager, use the no form of this command.

voice register session-server session-server-tag

no voice register session-server session-server-tag

### Syntax Description

session-server-tag

Explicitly identifies a session manager for configuration
                                          						tasks. Range is 1 to the maximum number of Cisco IP phones supported by a Cisco
                                          						Unified CME router as set by the max-ephones command in telephony-service
                                          						configuration mode.

### Command Default

No session manager is created.

### Command Modes

Global configuration (config)

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

15.2(1)T

Cisco Unified CME 8.8

This command was modified to allow the maximum number of
                                          						Cisco IP phones supported by a Cisco Unified CME router to be identified as the
                                          						session manager.

### Usage Guidelines

Provisioning and configuration information in the Cisco Unified
                              		  Contact Center Express (Cisco Unified CCX) is automatically provided to Cisco
                              		  United CME. Use the voice register session-server command to enter voice register
                              		  session-server configuration mode and reconfigure and enable a session manager
                              		  for Cisco Unified CCX on a Cisco Carrier Routing System when the configuration
                              		  from Cisco Unified CCX is deleted or must be modified.

A single Cisco Unified CME can support multiple session managers.

After creating one or more session managers, use the session-server command in voice register pool
                              		  configuration mode to identify a session manager for controlling a route point.

After creating one or more session managers, use the session-server command in ephone-dn
                              		  configuration mode to specify session managers for monitoring a directory
                              		  numbers.

## Examples

The following is a partial output from the show running-configuration command, showing the
                              		  configuration for the session manager, session-server 1:

```
!
voice register session-server 1
 keepalive 300
 register-id SB-SJ3-UCCX1_1164774025000
!
```

### Related Commands

Command

Description

session-server

Specifies a session server to manage and monitor
                                          						registration and subscription messages for an external feature server.

## voice register template

To enter voice register template configuration mode and define a
                              		  template of common parameters for SIP phones, use the voice register template command in global configuration mode. To
                              		  remove a template, use the no form of this command.

voice register template template-tag

no voice register template template-tag

### Syntax Description

template-tag

Declares a template tag. Range: 1 to 10.

### Command Default

No default behavior or values

### Command Modes

Global configuration (config)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4

This command was introduced.

12.4(11)XJ

Cisco Unified CME 4.1

The maximum number of templates was increased from 5 to 10.

12.4(15)T

Cisco Unified CME 4.1

The increase in the template number was integrated into
                                          						Cisco IOS Release 12.4(15)T.

### Usage Guidelines

Up to ten different templates can be defined and applied to SIP
                              		  phones. You create the template with this command and then apply the template
                              		  to a phone by using the template command in voice register pool
                              		  configuration mode.

## Examples

In the following example, template 1 is created by using the voice register template command.

```
Router(config)# voice register template 1 Router(config-register-temp)# anonymous block Router(config-register-temp)# caller-id block Router(config-register-temp)# voicemail 5001 timeout 15
```

### Related Commands

Description

anonymous block (voice register template)

Enables anonymous call blocking in a SIP phone template.

caller-id block (voice register template)

Enables caller-ID blocking for outbound calls from a
                                          						specific SIP phone.

template (voice register pool)

Applies a template to a SIP phone.

voicemail (voice register template

Defines the extension that calls are forwarded to when an
                                          						extension does not answer.

## voice user-profile

To enter voice user-profile configuration mode and create a user
                              		  profile for downloading by Extension Mobility for a particular individual phone
                              		  user, use the voice user-profile command in global configuration mode. To delete an logout
                              		  profile, use the no form of this command.

voice user-profile profile-tag

no voice user-profile profile-tag

### Syntax Description

profile-tag

Unique number that identifies this profile during
                                          						configuration tasks. Range: 1 to three times the maximum number supported
                                          						phones, where maximum is platform and version dependent and defined by the max-ephone command.

### Command Default

No user profile is created.

### Command Modes

Global configuration (config)

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

Use this command to create a user profile containing a user’s own
                              		  personal settings, such as directory number, speed-dial lists, and services,
                              		  for downloading to the IP phone when the individual phone user logs into a
                              		  Cisco Unified IP phone that is registered in Cisco Unified CME and enabled for
                              		  Extension Mobility.

Type ? in voice profile configuration mode to see
                              		  the commands that are available in this mode and that can be included in a user
                              		  profile. The following example shows a list of commands that were available in
                              		  voice user-profile configuration mode at the time that this document was
                              		  written:

```
Router(config-user-profile)# ? Logout profile configuration commands:
 name				Define username and password for Extension Mobility.
 number				Create ip-phone line definition
 pin					
 reset				Reset all phones associated with the profile being configured
 speed-dial				Define ip-phone speed-dial number
```

All directory numbers to be included in a default logout profile or
                              		  voice-user profile must already be configured in Cisco Unified CME.

After creating or modifying a profile, use the rese t (voice user-profile) command to reset all phones on which
                              		  this profile is downloaded to propagate the modifications.

## Examples

The following example shows the configuration for a voice-user
                              		  profile to be downloaded when a phone user logs into a Cisco Unified IP phone
                              		  that is enabled for Extension Mobility. The lines and speed-dial buttons in
                              		  this profile that are configured on a phone after the user logs in depend on
                              		  the phone type. For example, if the user logs into a Cisco Unified IP Phone
                              		  7970, all buttons are configured according to voice-user profile1. However, if
                              		  the phone user logs into a Cisco Unified IP Phone 7960, all six lines are
                              		  mapped to phone buttons and the speed dial is ignored because no button is
                              		  available for speed dial.

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

Enables Cisco Unified IP phone for Extension Mobility and
                                          						assigns a logout profile to this phone.

reset (voice logout-profile and voice user-profile)

Performs a complete reboot of all IP phones on which a
                                          						particular logout profile or user profile is downloaded.

## voice-class codec (voice register pool)

To assign a previously configured codec selection preference list,
                              		  use the voice-class codec command in voice register pool configuration
                              		  mode. To remove the codec preference assignment from the voice register pool,
                              		  use the no form of this command.

voice-class codec tag

no voice-class codec

### Syntax Description

tag

Unique number assigned to the voice class. Range is from 1
                                          						to 10000. The tag number maps to the tag number created by using the voice class codec command in dial-peer configuration
                                          						mode.

### Command Default

There is no codec preference assignment in the voice register pool
                              		  configuration.

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

This command was added to Cisco CME.

### Usage Guidelines

During Cisco Unified Session Initiation Protocol (SIP) Survivable
                              		  Remote Site Telephony (SRST) or Cisco Unified CallManager Express (Cisco
                              		  Unified CME) registration, a dial peer is created and that dial peer includes
                              		  codec g729r8 by default. This command allows you to change the automatically
                              		  selected default codec.

You can assign one voice class to each voice register pool. If you
                              		  assign another voice class to a pool, the last voice class assigned replaces
                              		  the previous voice class.

## Examples

The following partial sample output from the show running-config command shows that voice register pool 1 has been set up to use
                              		  the previously configured codec voice class 1:

```
voice register pool 1
 id mac 0030.94C2.A22A
 preference 5
 cor incoming call91 1 91011
 translate-outgoing called 1
 proxy 10.2.161.187 preference 1 monitor probe icmp-ping
 alias 1 94... to 91011 preference 8
 voice-class codec 1
```

### Related Commands

Description

codec (voice register pool)

Specifies the codec supported by a single Cisco SIP phone
                                          						or a VoIP dial peer in a Cisco Unified SIP SRST or a Cisco Unified CME
                                          						environment.

id (voice register pool)

Explicitly identifies a locally available individual Cisco
                                          						SIP IP phone, or when running Cisco Unified SIP SRST, set of Cisco SIP IP
                                          						phones.

voice class codec (dial-peer)

Assigns a previously configured codec selection preference
                                          						list (codec voice class) to a VoIP dial peer.

## voice-class mlpp (dial peer)

To assign a Multilevel Precedence and Preemption (MLPP) voice class
                              		  to a POTS or VoIP dial peer, use the voice-class mlpp command in dial-peer
                              		  configuration mode. To remove the voice class from the dial peer, use the no form of this command.

voice-class mlpp tag

no voice-class mlpp tag

### Syntax Description

tag

Unique number that identifies the voice class. Range: 1 to
                                          						10000.

### Command Default

The dial peer does not use an MLPP voice class.

### Command Modes

Dial-peer configuration (config-dial-peer)

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

The voice class that you assign to the dial peer must first be
                              		  configured using the voice class mlpp command in global configuration mode.

You can assign one voice class to each dial peer. If you assign
                              		  another voice class to a dial peer, the last voice class assigned replaces the
                              		  previous voice class.

## Examples

The following example shows that VoIP dial peer 36 is assigned MLPP
                              		  class 2.

```
Router(config)# dial-peer voice 36 voip Router(config-dial-peer)# voice-class mlpp 2
```

### Related Commands

Command

Description

service-domain (voice class)

Sets the service domain name in the MLPP voice class.

show dial-peer voice

Displays the configuration for all dial peers configured on
                                          						the router.

voice class mlpp

Creates an MLPP voice class.

## voice-class stun-usage

To configure voice class, enter voice class configuration mode called
                              		  stun-usage and use the voice-class stun-usage command in global, dial-peer, ephone,
                              		  ephone template, voice register pool, or voice register pool template
                              		  configuration mode. To disable the voice class, use the no form of this command.

voice-class stun-usage tag

no voice-class stun-usage tag

### Syntax Description

tag

Unique identifier in the range 1 to 10000.

### Command Default

The voice class is not defined.

### Command Modes

Global configuration (config) Dial peer configuration (config-dial-peer) Ephone configuration (config-ephone) Ephone template configuration (config-ephone-template) Voice register pool configuration (config-register-pool) Voice register pool template configuration (config-register-pool)

## Command History

Release

Cisco Product

Modification

12.4(22)T

Cisco Unified CME 7.0

This command was introduced.

15.1(2)T

Cisco Unified CME 8.1

This command was modified. This command can be enabled in
                                          						ephone summary, ephone template, voice register pool, or voice register pool
                                          						template configuration mode.

### Usage Guidelines

When the voice-class stun-usage is removed, the same is removed
                              		  automatically from the dial-peer, ephone, ephone template, voice register pool,
                              		  or voice register pool template configurations.

## Examples

The following example shows how to set the voice class stun-usage tag to 10000:

```
Router(config)# voice class stun-usage 10000 Router(config-ephone) # voice class stun-usage 10000 Router(config-voice-register-pool) # voice class stun-usage 10000
```

### Related Commands

Command

Description

stun usage firewall-traversal flowdata

Enables firewall traversal using STUN.

stun flowdata agent-id

Configures the agent ID.

## voice-gateway system

To enter voice-gateway configuration mode and create a voice gateway
                              		  configuration, use the voice-gateway system command in global configuration mode. To
                              		  remove the configuration, use the no form of this command.

voice-gateway system tag

no voice-gateway system tag

### Syntax Description

tag

Unique number that identifies the voice gateway. Range: 1
                                          						to 25. There is no default value.

### Command Default

Gateway configuration is not defined.

### Command Modes

Global configuration (config)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(22)YB

Cisco Unified CME 7.1

This command was introduced.

12.4(24)T

Cisco Unified CME 7.1

This command has been integrated into Cisco IOS Release
                                          						12.4(24)T.

### Usage Guidelines

This command enters voice-gateway configuration mode to define the
                              		  parameters for a voice gateway using the auto-configuration feature. Define a
                              		  configuration for each Cisco voice gateway whose analog FXS ports you want
                              		  under the control of this Cisco Unified CME router.

## Examples

The following example shows a voice gateway configuration:

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

mac-address

Defines the MAC address of the Cisco voice gateway that
                                          						downloads its configuration from Cisco Unified CME.

type

Defines the type of voice gateway to autoconfigure in Cisco
                                          						Unified CME.

voice-port

Identifies the analog ports on the voice gateway that
                                          						register to Cisco Unified CME.

## voicemail (telephony-service)

To define the telephone number that is speed-dialed when the Messages
                              		  button on a Cisco IP phone is pressed, use the voicemail command in telephony-service
                              		  configuration mode. To disable the Messages button, use the no form of this command.

voicemail phone-number

no voicemail

### Syntax Description

phone-number

Phone number that is configured as a speed-dial number for
                                          						retrieving messages.

### Command Default

No phone number is configure and the Messages button is disabled.

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

### Usage Guidelines

This command configures the telephone number that is speed-dialed
                              		  when the Messages button on a Cisco IP phone is pressed. The same telephone
                              		  number is configured for voice messaging for all Cisco IP phones connected to
                              		  the router.

## Examples

The following example sets the phone number 914085550100 as the
                              		  speed-dial number that is dialed to retrieve messages when the Messages button
                              		  is pressed:

```
Router(config)# telephony-service Router(config-telephony)# voicemail 914085550100
```

### Related Commands

Description

telephony-service

Enters telephony-service configuration mode.

vm-device-id (ephone)

Defines the voice-mail ID string.

## voicemail (voice register global)

To define the telephone number that is speed-dialed when the Messages
                              		  button on a Cisco IP phone is pressed, use the voicemail command in voice register global
                              		  configuration mode. To disable the Messages button, use the no form of this command.

voicemail phone-number

no voicemail

### Syntax Description

phone-number

Telephone number that is speed-dialed for retrieving
                                          						messages.

### Command Default

No phone number is configure and the Messages button is disabled.

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

This command configures the telephone number that is speed-dialed
                              		  when the Messages button on a Cisco IP phone is pressed. The same telephone
                              		  number is configured for voice messaging for all Cisco IP phones connected to
                              		  the router.

## Examples

The following example shows how to set telephone number 914085550100
                              		  as the speed-dial number to retrieve messages when the Messages button is
                              		  pressed:

```
Router(config)# voice register global Router(config-register-global)# voicemail 914085550100
```

### Related Commands

Description

url (voice register global)

Provision uniform resource locators (URLs) for feature
                                          						buttons on Cisco IP phones.

voicemail (voice register template)

Defines the extension that calls are forwarded to when an
                                          						extension does not answer.

voice register global

Enters voice register global configuration mode in order to
                                          						set global parameters for all supported Cisco SIP phones in a Cisco CME or
                                          						Cisco SIP SRST environment.

## voicemail (voice register template)

To define the extension that calls are forwarded to when an extension
                              		  does not answer, use the voicemail command in voice register template
                              		  configuration mode. To disable the voicemail extension, use the no form of this command.

voicemail phone-number timeout timeout

no voicemail

### Syntax Description

phone-number

Telephone number to which calls are forwarded when an
                                          						extension does not answer.

timeout seconds

Duration that a call can ring with no answer before the
                                          						call is forwarded to the voicemail extension. Range is 5 to 60000. There is no
                                          						default value.

### Command Default

This command has no default behavior or values.

### Command Modes

Voice register template configuration (config-register-temp)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4

This command was introduced.

### Usage Guidelines

This command defines the destination extension for voicemail when an
                              		  extension on a SIP phone does not answer. To apply the template to a SIP phone,
                              		  use the template command in voice register pool
                              		  configuration mode.

## Examples

The following example shows how to set telephone number 914085550100
                              		  as the number to be dialed to retrieve messages when the Messages button is
                              		  pressed:

```
Router(config)# voice register template 1 Router(config-register-temp)# voicemail 50100 timeout 15
```

### Related Commands

Description

template (voice register pool)

Applies a template to a SIP phone.

url (voice register global)

Provisions uniform resource locators (URLs) for feature
                                          						buttons on Cisco IP phones.

voice register global

Enters voice register global configuration mode in order to
                                          						set global parameters for all supported Cisco SIP phones in a Cisco CME or
                                          						Cisco SIP SRST environment.

voice register template

Enters voice register template configuration mode and
                                          						defines a template of common parameters for SIP phones.

voicemail (voice register global)

Defines the telephone number that is speed-dialed when the
                                          						Messages button on a Cisco IP phone is pressed.

## voice-port (voice-gateway)

To identify the analog ports on the voice gateway that register to
                              		  Cisco Unified CME, use the voice-port command in voice-gateway
                              		  configuration mode. To remove the ports, use the no form of this command.

voice-port port-range

no voice-port

### Syntax Description

port-range

Individual port number, or range of port numbers, on the
                                          						voice gateway controlled by Cisco Unified CME. Enter individual port values
                                          						separated by a comma (,) or enter a range using a hyphen (x-y). There is no
                                          						default value.

### Command Default

No voice ports are supported.

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

This command has been integrated into Cisco IOS Release
                                          						12.4(24)T.

### Usage Guidelines

This command sets the total number of analog endpoints on the voice
                              		  gateway that you intend to register to the Cisco Unified CME router. The Cisco
                              		  VG202 supports two ports, Cisco VG204 supports four ports, and the Cisco VG224
                              		  supports 24 ports, numbered 0 to 23.

## Examples

The following example shows a configuration for a Cisco VG224 voice
                              		  gateway with 24 ports:

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

network-locale (voice-gateway)

Selects a geographically specific set of tones and cadences
                                          						for the voice gateway’s analog endpoints that register to Cisco Unified CME.

type (voice-gateway)

Defines the type of voice gateway to autoconfigure in Cisco
                                          						Unified CME.

## vpn-gateway

To enter vpn-gateway url, use the vpn-gateway command in vpn-group
                              		  configuration mode. To disable the vpn-gateway configuration, use the no form of this command.

vpn-gateway number [ url ]

no vpn-group

### Syntax Description

number

Vpn-gateway numbers. Range: 1-3.

url

VPN concentrator address url as https://<IP>/policy.

### Command Default

vpn-gateway is not configured.

### Command Modes

Vpn-group configuration (conf-vpn-group).

## Command History

Cisco IOS Release

Cisco Product

Modification

15.1(3)T

Cisco Unified CME 8.5

This command was introduced.

### Usage Guidelines

Use this command to enter vpn-gateway urls. You can define up to 3
                              		  vpn-gateways urls for SSLVPN phones.

## Examples

The following example shows vpn-gateway 1 configured for vpn-group 1:

```
Router# show run
!
!
!
voice-card 3
 dspfarm
 dsp services dspfarm
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
  host-id-check disable
 sip
```

### Related Commands

Command

Description

vpn-group

Specifies a vpn-group.

vpn-trustpoint

Specifies a vpn-gateway trustpoint.

## vpn-group

To enter vpn-group mode, use the vpn-group command in voice service
                              		  voip configuration mode. To delete all configurations associated with a
                              		  vpn-group, use the no form of this command.

vpn-group tag

no vpn-group

### Syntax Description

tag

Vpn-group tag number. Range: 1-2.

### Command Default

vpn-group is not configured.

### Command Modes

Voice service voip (conf-voi-serv)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.1(3)T

Cisco Unified CME 8.5

This command was introduced.

### Usage Guidelines

Use this command to create vpn-groups. A vpn-group is a redundancy
                              		  ordered list of up to 3 vpn-gateways that an SSL VPN client on a phone can
                              		  connect to. You can create 2 vpn-groups.

## Examples

The following example shows vpn-group 1:

```
Router# show run
!
!
!
voice-card 3
 dspfarm
 dsp services dspfarm
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
  host-id-check disable
 sip
```

### Related Commands

Command

Description

vpn-gateway

Specifies a vpn-gateway URL.

vpn-trustpoint

Specifies a vpn-gateway trustpoint.

vpn-hash-algorithm

Specifies vpn hash encryption for the trustpoints.

## vpn-hash-algorithm

To specify the algorithm to hash the VPN certificate provided in the
                              		  configuration file downloaded to the phone, use the vpn-hash-algorithm command
                              		  in vpn-group configuration mode. To disable vpn-hash-encryption, use the no form of this command.

vpn-hash-algorithm sha-1

no vpn-hash-algorithm

### Syntax Description

sha-1

Encryption algorithm.

### Command Default

vpn-hash-algorithm is not configured

### Command Modes

Vpn-group configuration (conf-vpn-group)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.1(3)T

Cisco Unified CME 8.5

This command was introduced.

### Usage Guidelines

Use this command to specify the algorithm to hash the VPN certificate
                              		  provided in the configuration file downloaded to the phone.

## Examples

The following example shows vpn-hash-algorithm configured in
                              		  vpn-group 1:

```
Router# show run
!
!
!
voice-card 3
 dspfarm
 dsp services dspfarm
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
  host-id-check disable
 sip
```

### Related Commands

Command

Description

vpn-group

Specifies a vpn-group.

vpn-trustpoint

Specifies a vpn-gateway trustpoint.

## vpn-profile

To enter vpn-profile mode to configure vpn-profiles in Cisco Unified
                              		  CME, use the vpn-profile command in voice service voip
                              		  configuration mode. To remove the entire vpn-profile configuration, use the no
                              		  form of this command.

vpn-profile tag

no vpn-profile

### Syntax Description

tag

Vpn-profile tag number. Range:1-6,

### Command Default

No vpn-profile is configured.

### Command Modes

Voice service voip (conf-voi-serv)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.1(3)T

Cisco Unified CME 8.5

This command was introduced.

### Usage Guidelines

Use this command to create one or more vpn-profiles on Cisco Unified
                              		  CME. You can create 6 vpn-profiles.

## Examples

The following example shows 3 vpn-profiles configured:

```
Router# show run
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
  auto-network-detect enable
  host-id-check disable
 vpn-profile 2
  mtu 1300
  password-persistent enable
  host-id-check enable
 vpn-profile 4
  fail-connect-time 50
 sip
!
!
```

### Related Commands

Command

Description

voice-service-voip

Enters voice-service configuration mode for Voice Over IP
                                          						(VoIP) encapsulation.

vpn-group

Enters vpn-group configuration mode.

## vpn-trustpoint

To configure a vpn gateway trustpoint, use the vpn-trustpoint command
                              		  in vpn-group configuration mode. To disable a vpn-gateway trustpoint associated
                              		  with a vpn-group, use the no form of this command.

vpn-trustpoint number [ raw | trustpoint ] word [ leaf | root ]

no vpn-trustpoint

### Syntax Description

number

Number of allowed trustpoints. Range is from 1 to 10.

raw

(Optional) Allows to enter VPN Gateway Trustpoint in raw
                                          						form.

trustpoint

(Optional) Allows to enter VPN Gateway Trustpoint in IOS
                                          						format.

leaf

Get the 1st leaf cert of the Trustpoint.

root

Get the root cert of the Trustpoint.

### Command Default

vpn-trustpoint is not configured.

### Command Modes

Vpn-group (conf-vpn-group)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.1(3)T

Cisco Unified CME 8.5

This command was introduced.

### Usage Guidelines

Use this command to create vpn-trustpoints for a vpn-group. You can
                              		  configure as many as 10 vpn-trustpoints in a vpn-group. All vpn trustpoints
                              		  must be entered in either raw or trustpoint (IOS) format.

## Examples

The following example shows vpn-trustpoint 1 entered in trustpoint
                              		  (IOS) format:

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
  host-id-check disable
 sip
```

### Related Commands

Command

Description

vpn-grouptrustpoint

Defines a vpn-group.

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was introduced. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

|  | Description |
|---|---|
| template (voice register pool) | Applies a template to a SIP phone. |

| audio-url | Location of the announcement audio file in URL format.
                                          						Valid storage locations are TFTP, FTP, HTTP, and flash memory. |
|---|---|
| tag | Number of the voice class that defines the cause codes for
                                          						which the VCA is played. Range: 1 to 64. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| bnea | Specifies the audio file used for the busy station not
                                          						equipped for preemption announcement. |
| bpa | Specifies the audio file used for the blocked precedence
                                          						announcement. |
| ica | Specifies the audio file used for the isolated code
                                          						announcement. |
| mlpp indication | Enables MLPP indication on an SCCP phone or analog FXS
                                          						port. |
| voice class cause-code | Creates a voice class for defining a set of cause codes. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(4)M | Cisco Unified CME 8.6 | This command was introduced. |

| Command | Description |
|---|---|
| apply-config | Allows to dynamically apply the phone configuration on
                                          						Cisco Unified SIP IP phones 8961, 9951, and 9971, |
| bandwidth video tias-modifier | Allows to set the maximum video bandwidth bytes per second
                                          						(BPS) for SIP IP phones |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| service phone | Modifies the vendorConfig parameters in phone configuration
                                          						files. |
|---|---|
| video (telephony-service) | Enters video configuration mode for modifying video
                                          						parameters in Cisco Unified CME. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

|  | Description |
|---|---|
| maximum bit-rate | Sets the maximum video bandwidth for phones in Cisco
                                          						unified CME. |
| show call active video | Displays call information for SCCP video calls in progress. |
| show call history video | Displays call history information for SCCP video calls. |

| Release | Modification |
|---|---|
| 15.1(4)M | The command was introduced. |

| Command | Description |
|---|---|
| codec profile | Defines the video capabilities needed for video endpoints. |
| video codec | Assigns a video codec to a VoIP dial peer. |

| value | Video bandwidth in kb/s. Range is from 64 to 102400 kbps. |
|---|---|

| Release | Modification |
|---|---|
| 15.1(4)M | This command was introduced. |

| id-string | Voice-messaging device port identification (ID) string; for
                                          						example, CiscoUM-VI1 for the first port and CiscoUM-VI2 for the second port.
                                          						Note that the first two characters after the hyphen must be the uppercase
                                          						letters V and I. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco ITS 2.0 | This command was introduced |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |

|  | Description |
|---|---|
| voicemail (telephony-service) | Configures the telephone number that is speed-dialed when
                                          						the Messages button on a Cisco IP phone is pressed. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(11)YT | Cisco SRST 2.1 | This command was introduced for Cisco Survivable Remote
                                          						Site Telephony (SRST). |
| 12.2(2)XT | Cisco ITS 2.0 | This command was introduced Cisco ITS. |
| 12.2(8)T | Cisco ITS 2.0 Cisco SRST 2.1 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |

|  | Description |
|---|---|
| pattern direct (vm-integration) | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when a user presses the Messages button on a
                                          						phone. |
| pattern ext-to-ext busy (vm-integration) | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension reaches a busy
                                          						extension and the call is forwarded to voice mail. |
| pattern ext-to-ext no-answer (vm-integration) | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an internal extension fails to connect to
                                          						an extension and the call is forwarded to voice mail. |
| pattern trunk-to-ext busy (vm-integration) | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system once an external trunk call reaches a busy
                                          						extension and the call is forwarded to voice mail. |
| pattern trunk-to-ext no-answer (vm-integration) | Configures the DTMF digit pattern forwarding necessary to
                                          						activate the voice-mail system when an external trunk call reaches an
                                          						unanswered extension and the call is forwarded to voice mail. |

| tag | Unique number to identify the voice class. Range: 1 to
                                          						10000. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| service-domain (voice class) | Sets the service domain name in the MLPP voice class. |
| voice-class mlpp (dial peer) | Assigns an MLPP voice class to a POTS or VoIP dial peer. |

| tag | Unique number that identifies this ERL tag. |
|---|---|

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
| address | Specifies a comma separated text entry (up to 250
                                          						characters) of an ERL’s civic address. |
| elin | Specifies a PSTN number that will replace the caller’s
                                          						extension. |
| name | Specifies a string (up to 32-characters) used internally to
                                          						identify or describe the emergency response location. |
| subnet | Defines which IP phones are part of this ERL. |

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
| expiry | Number of minutes a 911 call is associated to an ELIN in
                                          						the case of a callback from the 911 operator. |
| logging | Syslog informational message printed to the console every
                                          						time an emergency call is made. |

| tag | Identifier (1-100) for the voice emergency response zone. |
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
| location | Identifies locations within an emergency response zone and
                                          						optionally assigns a priority order to the location. |

| hunt-tag | Unique
                                          						sequence number that identifies the hunt group. Range is 1 to 100. |
|---|---|
| longest-idle | Allows
                                          						an incoming call to go first to the number that has been idle the longest for
                                          						the number of hops specified when the hunt group was defined. The longest-idle
                                          						time is determined from the last time that a phone registered, reregistered, or
                                          						went on-hook. |
| parallel | Allows
                                          						an incoming call to simultaneously ring all the numbers in the hunt group
                                          						member list. |
| peer | Allows
                                          						a round-robin selection of the first extension to ring. Ringing proceeds in a
                                          						circular manner from left to right. The round-robin selection starts with the
                                          						number left of the number that answered when the hunt-group was last called. |
| sequential | Allows
                                          						an incoming call to ring all the numbers in the left-to-right order in which
                                          						they were listed when the hunt group was defined. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco
                                          						CME 3.4 | This
                                          						command was introduced. |
| 12.4(15)XZ | Cisco
                                          						Unified CME 4.3 | This
                                          						command was modified to add support for Cisco Unified SCCP IP phones. |
| 12.4(20)T | Cisco
                                          						Unified CME 7.0 | This
                                          						command was integrated into Cisco IOS Release 12.4(20)T. |
| 15.2(4)M | Cisco
                                          						Unified SIP SRST 9.1 | This
                                          						command was introduced in Cisco Unified SIP SRST 9.1. |
| 15.3(4)M | Cisco
                                          						Unified CME 10.5 | This
                                          						command was modified to include support for wildcards which is indicated by " * " . symbol. |

| Command | Description |
|---|---|
| final (voice hunt-group) | Defines the last extension in a voice hunt group. |
| hops
                                          						(voice hunt-group) | Defines the number of times that a call is redirected to the next phone number
                                          						in a peer voice hunt-group list before proceeding to the final phone number. |
| list (voice hunt-group) | Defines the phone numbers that participate in a voice hunt group. |
| max-redirect | Changes the number of times that a call can be redirected by call forwarding or
                                          						transfer within a Cisco Unified CME system. |
| pilot (voice hunt-group) | Defines the phone number that callers dial to reach a voice hunt group. |
| timeout (voice hunt-group) | Sets
                                          						the number of seconds after which a call that is not answered is redirected to
                                          						the next number in the hunt-group list and defines the last phone number in the
                                          						hunt group. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 15.4(3)M | Cisco
                                          						Unified CME 10.5 | This
                                          						command was introduced. |

| Command | Description |
|---|---|
| show voice hunt-groups | Displays voice-hunt group configuration, current status, and statistics. |

| cause-code | Number
                                          						of the cause code to generate when a call is blocked by the LPCOR validation
                                          						process. Range: 1 to 180. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco
                                          						Unified CME 8.0 | This
                                          						command was introduced. |
| 15.1(1)T | Cisco
                                          						Unified CME 8.0 | This
                                          						command was integrated into Cisco IOS Release 15.1(1)T. |

| Message | Description | Code
                                          					 Number |
|---|---|---|
| access-info-discard | access
                                          					 info discarded (43) | 43 |
| b-cap-not-implemented | bearer
                                          					 capability not implemented (65) | 65 |
| b-cap-restrict | restricted digital info bc only (70) | 70 |
| b-cap-unauthorized | bearer
                                          					 capability not authorized (57) | 57 |
| b-cap-unavail | bearer
                                          					 capability not available (58) | 58 |
| call-awarded | call
                                          					 awarded (7) | 7 |
| call-cid-in-use | call
                                          					 exists call id in use (83) | 83 |
| call-clear | call
                                          					 cleared (86) | 86 |
| call-reject | call
                                          					 rejected (21) | 21 |
| cell-rate-unavail | cell
                                          					 rate not available (37) | 37 |
| channel-unacceptable | channel
                                          					 unacceptable (6) | 6 |
| chantype-not-implement | chan
                                          					 type not implemented (66) | 66 |
| cid-in-use | call id
                                          					 in use (84) | 84 |
| codec-incompatible | codec
                                          					 incompatible (171) | 171 |
| cug-incalls-bar | cug
                                          					 incoming calls barred (55) | 55 |
| cug-outcalls-bar | cug
                                          					 outgoing calls barred (53) | 53 |
| dest-incompatible | incompatible destination (88) | 88 |
| dest-out-of-order | destination out of order (27) | 27 |
| dest-unroutable | no
                                          					 route to destination (3) | 3 |
| dsp-error | dsp
                                          					 error (172) | 172 |
| dtl-trans-not-node-id | dtl
                                          					 transit not my node id (160) | 160 |
| facility-not-implemented | facility not implemented (69) | 69 |
| facility-not-subscribed | facility not subcribed (50) | 50 |
| facility-reject | facility rejected (29) | 29 |
| glare | glare
                                          					 (15) | 15 |
| glaring-switch-pri | glaring
                                          					 switch PRI (180) | 180 |
| htspm-oos | HTSPM
                                          					 out of service (129) | 129 |
| ie-missing | mandatory ie missing (96) | 96 |
| ie-not-implemented | ie not
                                          					 implemented (99) | 99 |
| info-class-inconsistent | inconsistency in info and class (62) | 62 |
| interworking | interworking (127) | 127 |
| invalid-call-ref | invalid
                                          					 call ref value (81) | 81 |
| invalid-ie | invalid
                                          					 ie contents (100) | 100 |
| invalid-msg | invalid
                                          					 message (95) | 95 |
| invalid-number | invalid
                                          					 number (28) | 28 |
| invalid-transit-net | invalid
                                          					 transit network (91) | 91 |
| misdialled-trunk-prefix | misdialled trunk prefix (5) | 5 |
| msg-incomp-call-state | message
                                          					 in incomp call state (101) | 101 |
| msg-not-implemented | message
                                          					 type not implemented (97) | 97 |
| msgtype-incompatible | message
                                          					 type not compatible (98) | 98 |
| net-out-of-order | network
                                          					 out of order (38) | 38 |
| next-node-unreachable | next
                                          					 node unreachable (128) | 128 |
| no-answer | no user
                                          					 answer (19) | 19 |
| no-call-suspend | no call
                                          					 suspended (85) | 85 |
| no-channel | channel
                                          					 does not exist (82) | 82 |
| no-circuit | no
                                          					 circuit (34) | 34 |
| no-cug | non
                                          					 existent cug (90) | 90 |
| no-dsp-channel | no dsp
                                          					 channel (170) | 170 |
| no-req-circuit | no
                                          					 requested circuit (44) | 44 |
| no-resource | no
                                          					 resource (47) | 47 |
| no-response | no user
                                          					 response (18) | 18 |
| no-voice-resources | no
                                          					 voice resources available (126) | 126 |
| non-select-user-clear | non
                                          					 selected user clearing (26) | 26 |
| normal-call-clear | normal
                                          					 call clearing (16) | 16 |
| normal-unspecified | normal
                                          					 unspecified (31) | 31 |
| not-in-cug | user
                                          					 not in cug (87) | 87 |
| number-changeed | number
                                          					 changed (22) | 22 |
| param-not-implemented | non
                                          					 implemented param passed on (103) | 103 |
| perm-frame-mode-oos | perm
                                          					 frame mode out of service (39) | 39 |
| perm-frame-mode-oper | perm
                                          					 frame mode operational (40) | 40 |
| precedence-call-block | precedence call blocked (46) | 46 |
| preempt | preemption (8) | 8 |
| preempt-reserved | preemption reserved (9) | 9 |
| protocol-error | protocol error (111) | 111 |
| qos-unavail | qos
                                          					 unavailable (49) | 49 |
| rec-timer-exp | recovery on timer expiry (102) | 102 |
| redirect-to-new-destination | redirect to new destination (23) | 23 |
| req-vpci-vci-unavail | requested vpci vci not available (35) | 35 |
| send-infotone | send
                                          					 info tone (4) | 4 |
| serv-not-implemented | service
                                          					 not implemented (79) | 79 |
| serv/opt-unavail-unspecified | service
                                          					 or option not available unspecified (63) | 63 |
| stat-enquiry-resp | response to status enquiry (30) | 30 |
| subscriber-absent | subscriber absent (20) | 20 |
| switch-congestion | switch
                                          					 congestion (42) | 42 |
| temp-fail | temporary failure (41) | 41 |
| transit-net-unroutable | no
                                          					 route to transit network (2) | 2 |
| unassigned-number | unassigned number (1) | 1 |
| unknown-param-msg-discard | unrecognized param msg discarded (110) | 110 |
| unsupported-aal-parms | aal
                                          					 parms not supported (93) | 93 |
| user-busy | user
                                          					 busy (17) | 17 |
| vpci-vci-assign-fail | vpci
                                          					 vci assignment failure (36) | 36 |
| vpci-vci-unavail | no vpci
                                          					 vci available (45) | 45 |

| Command | Description |
|---|---|
| voice lpcor policy | Creates a LPCOR policy for a resource group. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| group (lpcor custom) | Adds a LPCOR resource group to the custom resource list. |
| voice lpcor enable | Enables LPCOR functionality on the Cisco Unified CME
                                          						router. |
| voice lpcor policy | Creates a LPCOR policy for a resource group. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| voice lpcor custom | Defines the LPCOR resource groups on the Cisco Unified CME
                                          						router. |
| voice lpcor policy | Creates a LPCOR policy for a resource group. |

| incoming | Sets default LPCOR policy for incoming calls. |
|---|---|
| outgoing | Sets default LPCOR policy for outgoing calls. |
| lpcor-group | Name of the LPCOR resource group. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| voice lpcor ip-phone subnet | Creates a LPCOR IP-phone subnet table for calls to or from
                                          						a mobility-type phone. |

| incoming | Creates IP-phone subnet table for incoming calls from
                                          						mobility-type phone. |
|---|---|
| outgoing | Creates IP-phone subnet table for outgoing calls from
                                          						mobility-type phone. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| index (ip-phone) | Adds a LPCOR group to the IP-phone subnet table. |
| lpcor type | Specifies the LPCOR type for an IP phone. |
| voice lpcor ip-phone mobility | Sets the default LPCOR policy for mobility-type phones. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| index (lpcor ip-trunk) | Adds a LPCOR resource group to the IP trunk subnet table. |
| lpcor incoming | Associates a LPCOR resource-group policy with an incoming
                                          						call. |
| voice lpcor ip-phone subnet | Creates a LPCOR IP-phone subnet table for calls to or from
                                          						a mobility-type phone. |

| lpcor-group | Name of the LPCOR resource group. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| accept | Allows a LPCOR resource group to accept incoming calls from
                                          						another resource group. |
| show voice lpcor policy | Displays the LPCOR policy for the specified resource group. |
| voice lpcor custom | Defines the LPCOR resource groups on the Cisco Unified CME
                                          						router. |

| Cisco IOS Release | Cisco Products | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| access-digit | Defines the access digit that phone users dial to request a
                                          						precedence call. |
| mlpp preemption | Enables calls on an SCCP phone or analog FXS port to be
                                          						preempted. |
| preemption trunkgroup | Enables preemption capabilities on a trunk group. |

| tag | Specifies a moh-group number tag (1-5) to be used for music
                                          						on hold group parameters. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 Cisco Unified SRST 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 Cisco Unified SRST 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| moh | Enables music on hold from a flash audio feed. |
|---|---|
| multicast moh | Enables multicast of the music-on-hold audio stream. |
| extension-range | Defines extension range for a clients calling a
                                          						voice-moh-group. |

| dialplan-tag | Number that identifies the dial plan. Range: 1 to 24. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XJ | Cisco Unified CME 4.1 | This command was introduced. |
| 12.4(15)T | Cisco Unified CME 4.1 | This command was integrated into Cisco IOS Release
                                          						12.4(15)T. |

|  | Description |
|---|---|
| dialplan | Assigns a dial plan to a SIP phone. |
| filename | Specifies a custom XML configuration file that contains the
                                          						dial patterns to use for a SIP dial plan. |
| pattern (voice register dialplan) | Defines a dial pattern for a SIP dial plan. |
| show voice register dialplan | Displays all configuration information for a specific SIP
                                          						dial plan. |
| type (voice register dialplan) | Defines a phone type for a SIP dial plan. |

| dn-tag | Unique sequence number that identifies a particular
                                          						directory number during configuration tasks. Range is 1 to 150, or the maximum
                                          						defined by the max-dn command. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 and Cisco SIP SRST 3.4 | This command was introduced. |

| Note | This command can also be used for Cisco SIP SRST. |
|---|---|

| Note | The name or label associated with a directory number configured under voice register dn configuration mode cannot contain special characters such as quotes ("), angle brackets (<, >), ampersand (&), and percentage
                                          (%). |
|---|---|

|  | Description |
|---|---|
| max-dn (voice register global) | Sets the maximum number of SIP phone directory numbers
                                          						(extensions) supported by a Cisco CME router. |
| mode (voice register global) | Enables the mode for provisioning SIP phones in a Cisco
                                          						CallManager Express (Cisco CME) system. |
| number (voice register pool) | Configures a valid number for a SIP phone. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was introduced. |
| 15.0(1)XA | Cisco SIP SRST 8.0 | This command was updated to display the signaling transport
                                          						protocol. |
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SRST 8.1 | The no form of the command was modified. |

| Note | The name or label associated with a directory number configured under voice register global configuration mode cannot contain special characters such as quotes ("), angle brackets (<, >), ampersand (&), and percentage
                                          (%). |
|---|---|

| Command | Description |
|---|---|
| allow connections sip to sip | Allows connections between SIP endpoints in a Cisco
                                          						multiservice IP-to-IP gateway. |
| application (voice register global) | Selects the session-level application for all dial peers
                                          						associated with SIP phones. |
| mode (voice register global) | Enables the mode for provisioning SIP phones in a Cisco
                                          						Unified system. |

| pool-tag | Unique number assigned to the pool. Range is 1 to 100. Note For Cisco Unified CME systems, the upper limit for this
                                                   						argument is defined by the max-pool command. | Note | For Cisco Unified CME systems, the upper limit for this
                                                   						argument is defined by the max-pool command. |
|---|---|---|---|
| Note | For Cisco Unified CME systems, the upper limit for this
                                                   						argument is defined by the max-pool command. |

| Note | For Cisco Unified CME systems, the upper limit for this
                                                   						argument is defined by the max-pool command. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SIP SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SIP SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was added to Cisco CME. |

|  | Description |
|---|---|
| max-pool (voice register global) | Sets the maximum number of SIP phones that are supported by
                                          						a Cisco Unified CME system. |
| mode (voice register global) | Enables the mode for provisioning SIP phones in a Cisco
                                          						Unified CME system. |
| number (voice register pool) | Configures a valid number for a SIP phone. |
| type (voice register pool) | Defines a Cisco IP phone type. |

| device-reference supported
                                          						phone-type | (Optional)
                                       					 Defines the nearest-supported phone from which a new Cisco Unified SIP IP phone
                                       					 can inherit properties without the explicit configuration of the parameters. For a
                                       					 list of the names, types, and corresponding properties of supported phones, see
                                       					 the below table. |
|---|---|
| device-name name | (Optional)
                                       					 Defines the description string for the new phone device. |
| device-name type | Defines
                                       					 a phone type for a new Cisco Unified SIP IP phone. |
| addons max-addons | (Optional) Defines the maximum number of add-on modules
                                       					 supported by the new phone device. The maximum allowed value is 3. Note New
                                                   						add-on modules for an existing phone are not supported. | Note | New
                                                   						add-on modules for an existing phone are not supported. |
| Note | New
                                                   						add-on modules for an existing phone are not supported. |
| num-lines max-lines | Defines
                                       					 the maximum number of lines supported by the phone. Range is 1 to ???. |
| transport-type {udp \|
                                          						tcp} | (Optional) Defines the transport protocol supported by the
                                       					 phone. udp—User Datagram
                                             						Protocol (UDP) is used. tcp—Transmission Control
                                             						Protocol (TCP) is used. |
| gsm-handoff | (Optional) Enables phone support for Global System for Mobile
                                       					 Communications (GSM) handoff. Note For
                                                   						Cisco IOS Release 15.3(3)M, only CiscoMobile-iOS and Jabber-Android are
                                                   						supported. | Note | For
                                                   						Cisco IOS Release 15.3(3)M, only CiscoMobile-iOS and Jabber-Android are
                                                   						supported. |
| Note | For
                                                   						Cisco IOS Release 15.3(3)M, only CiscoMobile-iOS and Jabber-Android are
                                                   						supported. |
| telnet | (Optional) Enables phone support for Telnet access. Note For
                                                   						Cisco IOS Release 15.3(3)M, only Cisco Unified 3911, 3951, 7905, 7912, 7960,
                                                   						and 7940 SIP IP phones support Telnet access. | Note | For
                                                   						Cisco IOS Release 15.3(3)M, only Cisco Unified 3911, 3951, 7905, 7912, 7960,
                                                   						and 7940 SIP IP phones support Telnet access. |
| Note | For
                                                   						Cisco IOS Release 15.3(3)M, only Cisco Unified 3911, 3951, 7905, 7912, 7960,
                                                   						and 7940 SIP IP phones support Telnet access. |
| phoneload | (Optional) Enables support for phone loads. |
| xml-config xml-tag
                                          						value | (Optional) Defines the phone-specific XML tags to be used in the
                                       					 configuration file. xml-tag—Phone-specific
                                          						XML tag. value—Value of the XML
                                          						tag. |

| Note | New
                                                   						add-on modules for an existing phone are not supported. |
|---|---|

| Note | For
                                                   						Cisco IOS Release 15.3(3)M, only CiscoMobile-iOS and Jabber-Android are
                                                   						supported. |
|---|---|

| Note | For
                                                   						Cisco IOS Release 15.3(3)M, only Cisco Unified 3911, 3951, 7905, 7912, 7960,
                                                   						and 7940 SIP IP phones support Telnet access. |
|---|---|

| Release | Modification |
|---|---|
| 15.3(3)M | This
                                       					 command was introduced. |

| Command | Description |
|---|---|
| session-transport | Specifies the transport layer protocol that a SIP phone uses
                                          						to connect to Cisco Unified CME. |
| type (voice register pool) | Defines a phone type for a SIP phone. |

| session-server-tag | Explicitly identifies a session manager for configuration
                                          						tasks. Range is 1 to the maximum number of Cisco IP phones supported by a Cisco
                                          						Unified CME router as set by the max-ephones command in telephony-service
                                          						configuration mode. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XW2 | Cisco Unified CME 4.2 | This command was introduced. |
| 12.4(15)XY | Cisco Unified CME 4.2(1) | This command was introduced. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |
| 15.2(1)T | Cisco Unified CME 8.8 | This command was modified to allow the maximum number of
                                          						Cisco IP phones supported by a Cisco Unified CME router to be identified as the
                                          						session manager. |

| Command | Description |
|---|---|
| session-server | Specifies a session server to manage and monitor
                                          						registration and subscription messages for an external feature server. |

| template-tag | Declares a template tag. Range: 1 to 10. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |
| 12.4(11)XJ | Cisco Unified CME 4.1 | The maximum number of templates was increased from 5 to 10. |
| 12.4(15)T | Cisco Unified CME 4.1 | The increase in the template number was integrated into
                                          						Cisco IOS Release 12.4(15)T. |

|  | Description |
|---|---|
| anonymous block (voice register template) | Enables anonymous call blocking in a SIP phone template. |
| caller-id block (voice register template) | Enables caller-ID blocking for outbound calls from a
                                          						specific SIP phone. |
| template (voice register pool) | Applies a template to a SIP phone. |
| voicemail (voice register template | Defines the extension that calls are forwarded to when an
                                          						extension does not answer. |

| profile-tag | Unique number that identifies this profile during
                                          						configuration tasks. Range: 1 to three times the maximum number supported
                                          						phones, where maximum is platform and version dependent and defined by the max-ephone command. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XW | Cisco Unified CME 4.2 | This command was introduced. |
| 12.4(15)XY | Cisco Unified CME 4.2(1) | This command was introduced. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| logout-profile | Enables Cisco Unified IP phone for Extension Mobility and
                                          						assigns a logout profile to this phone. |
| reset (voice logout-profile and voice user-profile) | Performs a complete reboot of all IP phones on which a
                                          						particular logout profile or user profile is downloaded. |

| tag | Unique number assigned to the voice class. Range is from 1
                                          						to 10000. The tag number maps to the tag number created by using the voice class codec command in dial-peer configuration
                                          						mode. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SIP SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SIP SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was added to Cisco CME. |

| Note | The id (voice register pool) command is required
                                       		  and must be configured before any other voice register pool commands. The id command identifies a locally available
                                       		  individual Cisco SIP IP phone or set of Cisco SIP IP phones. |
|---|---|

|  | Description |
|---|---|
| codec (voice register pool) | Specifies the codec supported by a single Cisco SIP phone
                                          						or a VoIP dial peer in a Cisco Unified SIP SRST or a Cisco Unified CME
                                          						environment. |
| id (voice register pool) | Explicitly identifies a locally available individual Cisco
                                          						SIP IP phone, or when running Cisco Unified SIP SRST, set of Cisco SIP IP
                                          						phones. |
| voice class codec (dial-peer) | Assigns a previously configured codec selection preference
                                          						list (codec voice class) to a VoIP dial peer. |

| tag | Unique number that identifies the voice class. Range: 1 to
                                          						10000. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| service-domain (voice class) | Sets the service domain name in the MLPP voice class. |
| show dial-peer voice | Displays the configuration for all dial peers configured on
                                          						the router. |
| voice class mlpp | Creates an MLPP voice class. |

| tag | Unique identifier in the range 1 to 10000. |
|---|---|

| Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)T | Cisco Unified CME 7.0 | This command was introduced. |
| 15.1(2)T | Cisco Unified CME 8.1 | This command was modified. This command can be enabled in
                                          						ephone summary, ephone template, voice register pool, or voice register pool
                                          						template configuration mode. |

| Command | Description |
|---|---|
| stun usage firewall-traversal flowdata | Enables firewall traversal using STUN. |
| stun flowdata agent-id | Configures the agent ID. |

| tag | Unique number that identifies the voice gateway. Range: 1
                                          						to 25. There is no default value. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command has been integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| mac-address | Defines the MAC address of the Cisco voice gateway that
                                          						downloads its configuration from Cisco Unified CME. |
| type | Defines the type of voice gateway to autoconfigure in Cisco
                                          						Unified CME. |
| voice-port | Identifies the analog ports on the voice gateway that
                                          						register to Cisco Unified CME. |

| phone-number | Phone number that is configured as a speed-dial number for
                                          						retrieving messages. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco ITS 1.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |

|  | Description |
|---|---|
| telephony-service | Enters telephony-service configuration mode. |
| vm-device-id (ephone) | Defines the voice-mail ID string. |

| phone-number | Telephone number that is speed-dialed for retrieving
                                          						messages. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

|  | Description |
|---|---|
| url (voice register global) | Provision uniform resource locators (URLs) for feature
                                          						buttons on Cisco IP phones. |
| voicemail (voice register template) | Defines the extension that calls are forwarded to when an
                                          						extension does not answer. |
| voice register global | Enters voice register global configuration mode in order to
                                          						set global parameters for all supported Cisco SIP phones in a Cisco CME or
                                          						Cisco SIP SRST environment. |

| phone-number | Telephone number to which calls are forwarded when an
                                          						extension does not answer. |
|---|---|
| timeout seconds | Duration that a call can ring with no answer before the
                                          						call is forwarded to the voicemail extension. Range is 5 to 60000. There is no
                                          						default value. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

|  | Description |
|---|---|
| template (voice register pool) | Applies a template to a SIP phone. |
| url (voice register global) | Provisions uniform resource locators (URLs) for feature
                                          						buttons on Cisco IP phones. |
| voice register global | Enters voice register global configuration mode in order to
                                          						set global parameters for all supported Cisco SIP phones in a Cisco CME or
                                          						Cisco SIP SRST environment. |
| voice register template | Enters voice register template configuration mode and
                                          						defines a template of common parameters for SIP phones. |
| voicemail (voice register global) | Defines the telephone number that is speed-dialed when the
                                          						Messages button on a Cisco IP phone is pressed. |

| port-range | Individual port number, or range of port numbers, on the
                                          						voice gateway controlled by Cisco Unified CME. Enter individual port values
                                          						separated by a comma (,) or enter a range using a hyphen (x-y). There is no
                                          						default value. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command has been integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| network-locale (voice-gateway) | Selects a geographically specific set of tones and cadences
                                          						for the voice gateway’s analog endpoints that register to Cisco Unified CME. |
| type (voice-gateway) | Defines the type of voice gateway to autoconfigure in Cisco
                                          						Unified CME. |

| number | Vpn-gateway numbers. Range: 1-3. |
|---|---|
| url | VPN concentrator address url as https://<IP>/policy. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(3)T | Cisco Unified CME 8.5 | This command was introduced. |

| Command | Description |
|---|---|
| vpn-group | Specifies a vpn-group. |
| vpn-trustpoint | Specifies a vpn-gateway trustpoint. |

| tag | Vpn-group tag number. Range: 1-2. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(3)T | Cisco Unified CME 8.5 | This command was introduced. |

| Command | Description |
|---|---|
| vpn-gateway | Specifies a vpn-gateway URL. |
| vpn-trustpoint | Specifies a vpn-gateway trustpoint. |
| vpn-hash-algorithm | Specifies vpn hash encryption for the trustpoints. |

| sha-1 | Encryption algorithm. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(3)T | Cisco Unified CME 8.5 | This command was introduced. |

| Command | Description |
|---|---|
| vpn-group | Specifies a vpn-group. |
| vpn-trustpoint | Specifies a vpn-gateway trustpoint. |

| tag | Vpn-profile tag number. Range:1-6, |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(3)T | Cisco Unified CME 8.5 | This command was introduced. |

| Command | Description |
|---|---|
| voice-service-voip | Enters voice-service configuration mode for Voice Over IP
                                          						(VoIP) encapsulation. |
| vpn-group | Enters vpn-group configuration mode. |

| number | Number of allowed trustpoints. Range is from 1 to 10. |
|---|---|
| raw | (Optional) Allows to enter VPN Gateway Trustpoint in raw
                                          						form. |
| trustpoint | (Optional) Allows to enter VPN Gateway Trustpoint in IOS
                                          						format. |
| leaf | Get the 1st leaf cert of the Trustpoint. |
| root | Get the root cert of the Trustpoint. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(3)T | Cisco Unified CME 8.5 | This command was introduced. |

| Command | Description |
|---|---|
| vpn-grouptrustpoint | Defines a vpn-group. |