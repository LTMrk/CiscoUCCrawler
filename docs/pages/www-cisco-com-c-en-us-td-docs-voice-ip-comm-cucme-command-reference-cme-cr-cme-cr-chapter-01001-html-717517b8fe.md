---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-command-reference-cme-cr-cme-cr-chapter-01001-html-717517b8fe
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/command/reference/cme_cr/cme_cr_chapter_01001.html
retrieved_at: 2026-08-21T22:56:20.968582+00:00
---

Cisco Unified Communications Manager Express Command Reference

# Cisco Unified Communications Manager Express Command Reference

Updated: July 19, 2018

Chapter: Cisco Unified CME Commands: K

## Chapter: Cisco Unified CME Commands: K

# Cisco Unified CME Commands: K

## keepalive (ephone and ephone-template)

To set the length of the time interval between successive keepalive
                              		  messages from the Cisco Unified CME router to a particular IP phone, use the keepalive command in ephone or
                              		  ephone-template configuration mode. To reset this length to the default value,
                              		  use the no form of this command.

keepalive seconds

no keepalive

### Syntax Description

seconds

Interval time, in seconds. Range is from 10 to 65535.
                                          						Default is 30.

### Command Default

Default is 30 seconds

### Command Modes

Ephone configuration (config-ephone) Ephone-template configuration (config-ephone-template)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)T

Cisco CME 2.1

This command was introduced.

12.4(4)XC

Cisco Unified CME 4.0

This command was made available in ephone-template
                                          						configuration mode.

12.4(9)T

Cisco Unified CME 4.0

This command in ephone-template configuration mode was
                                          						integrated into Cisco IOS Release 12.4(9)T.

### Usage Guidelines

This command allows the keepalive interval to be set for individual
                              		  phones, typically so that wireless phone batteries are not run down too quickly
                              		  by overly frequent keepalive signals.

If the router fails to receive three successive keepalive messages,
                              		  it considers the phone to be out of service until the phone reregisters.

If the keepalive (telephony-service) command and this command are
                              		  set to different time intervals, the value that you set in ephone configuration
                              		  mode has priority for the particular phone only.

If you use an ephone template to apply a command to a phone and you
                              		  also use the same command in ephone configuration mode for the same phone, the
                              		  value that you set in ephone configuration mode has priority.

## Examples

The following example sets the keepalive interval to 300 seconds:

```
Router(config)# ephone 1 Router(config-ephone)# keepalive 300
```

### Related Commands

Command

Description

ephone-template (ephone)

Applies template to ephone being configured.

keepalive (telephony-service)

Sets the time interval for keepalive messages between IP
                                          						phones and the Cisco Unified CME router.

## keepalive (telephony-service)

To set the length of the time interval between successive keepalive
                              		  messages from the Cisco CallManager Express router to IP phones, use the keepalive command in telephony-service
                              		  configuration mode. To reset this length to the default value, use the no form of this command.

keepalive seconds

no keepalive

### Syntax Description

seconds

Interval time, in seconds. Range is from 10 to 65535.
                                          						Default is 30.

### Command Default

Default is 30 seconds.

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

If the router fails to receive three successive keepalive messages,
                              		  it considers the phone to be out of service until the phone reregisters.

If the keepalive (telephony-service) command and the keepalive (ephone) command are set to different time
                              		  intervals, the value that you set in ephone configuration mode has priority for
                              		  the particular phone only.

## Examples

The following example sets the keepalive time interval to 40 seconds:

```
Router(config)# telephony-service Router(config-telephony)# keepalive 40
```

### Related Commands

Command

Description

keepalive (ephone)

Sets the time interval for keepalive messages between a
                                          						particular IP phone and the Cisco CME router.

## keepalive (voice
                        	 register global)

To set the length
                              		  of time interval between successive keepalive messages from SIP phones to the
                              		  Cisco Unified CME router, use the keepalive command in voice register global configuration mode. To reset this timer
                              		  duration to the default value, use the no form of
                              		  this command.

keepalive seconds

no keepalive

### Syntax Description

seconds

Sets the
                                          						time interval, in seconds, between keepalive messages that are sent to the
                                          						router by SIP Phones. If the interval is set to a larger value, it is possible
                                          						for notification to be delayed when the primary router goes down. Range is from
                                          						120 to 65535. Default is 120 seconds.

### Command Default

Default is 120
                              		  seconds.

### Command Modes

Voice register global configuration (config-register-global)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

Cisco
                                          						IOS XE Everest 16.4.1

Cisco
                                          						Unified CME 11.6

This
                                          						command was introduced.

### Usage Guidelines

If the primary
                              		  router fails, a SIP phone will not receive an acknowledgment (200 OK) to its
                              		  REGISTER message to the primary router, and it will immediately failover to the
                              		  secondary Cisco Unified CME router.

## Examples

The following
                              		  example sets the keepalive time interval to 200 seconds:

```
Router(config)# voice register global Router(config-register-global)# keepalive 200
```

### Related Commands

Command

Description

keepalive (telephony-service)

Sets
                                          						the length of the time interval between successive keepalive messages from the
                                          						Cisco Unified CME router to SCCP phones.

## keepalive (voice register session-server)

To define the duration for registrations of external feature servers
                              		  after which the registration expires, use the keepalive command in voice register session-server configuration mode. To
                              		  return to the default, use the no form of this command.

keepalive seconds

no keepalive

### Syntax Description

seconds

Duration for registration, in seconds. Range: 60 to 3600.
                                          						Default: 300.

### Command Default

Default is 300 seconds.

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

Cisco Unified CME 4.2

This command was introduced.

12.4(15)XZ

Cisco Unified CME 4.3

This command was introduced.

12.4(20)T

Cisco Unified CME 7.0

This command was integrated into Cisco IOS Release
                                          						12.4920)T.

### Usage Guidelines

This command defines the duration for registration, in seconds, after
                              		  which the registration expires unless the feature server reregisters before the
                              		  registration expiry.

## Examples

The following partial output shows the configuration for a session
                              		  manager for an external feature server, including a keepalive expiry of 360
                              		  seconds:

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

register id

Creates an ID for explicitly identifying an external
                                          						feature server during Register requests.

## keepalive (vpn-profile)

To specify the duration of time required to generate a keepalive
                              		  message to the VPN concentrator, use the keepalive command in vpn-profile configuration mode.

keepalive seconds

### Syntax Description

seconds

Duration for a vpn-profile session, in seconds. Range: 0 to
                                          						120. Default: 60.

### Command Default

Default is 60 seconds.

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

Use this command to specify the amount of time required to generate a
                              		  keepalive message to the VPN concentrator. The keepalive session ranges from 0
                              		  to 120 seconds. The default keepalive session is 60 seconds.

## Examples

The following example shows the keepalive duration set to 50 seconds
                              		  for vpn-profile 1.

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

## keep-conference

To allow conference initiators to exit from conference calls and to
                              		  either end or maintain the conference for the remaining parties, use the keep-conference command in ephone or ephone-template configuration mode. To
                              		  return to the default, use the no form of this command.

keep-conference [ drop-last ] [ endcall ] [ local-only ]

no keep-conference

### Syntax Description

drop-last

(Optional) The action of the Confrn soft key is changed;
                                          						the conference initiator can press the Confrn soft key (IP phone) or hookflash
                                          						(analog phone) to drop the last party.

endcall

(Optional) The action of the EndCall soft key is changed;
                                          						the conference initiator can hang up or press the EndCall soft key to leave the
                                          						conference and keep the other two parties connected.

local-only

(Optional) The conference initiator can hang up to end the
                                          						conference and leave the other two parties connected only if one of the
                                          						remaining parties is local to the Cisco Unified CME system (an internal
                                          						extension).

### Command Default

A conference initiator can hang up or press the EndCall soft key to
                              		  end a conference and disconnect all parties or press the Confrn soft key to
                              		  drop only the last party that was connected to the conference.

### Command Modes

Ephone configuration (config-ephone) Ephone-template configuration (config-ephone-template)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(11)T

Cisco CME 3.2

This command was introduced.

12.4(4)XC

Cisco Unified CME 4.0

The drop-last and local-only keywords were added, and
                                          						this command was made available in ephone-template configuration mode.

12.4(9)T

Cisco Unified CME 4.0

The drop-last and local-only keywords, and this
                                          						command in ephone-template configuration mode were integrated into Cisco IOS
                                          						Release 12.4(9)T.

### Usage Guidelines

If you use an ephone template to apply a command to a phone and you
                              		  also use the same command in ephone configuration mode for the same phone, the
                              		  value that you set in ephone configuration mode has priority.

If the keep-conference command is configured with no
                              		  keywords, a conference initiator can hang up to leave the conference and the
                              		  other two parties will remain connected. Alternatively, the conference
                              		  initiator can use the EndCall soft key to terminate the conference and
                              		  disconnect all parties.

If the keep-conference command is configured with no
                              		  keywords, a conference initiator can use the Confrn soft key (IP phone) or
                              		  hookflash (analog phone) to break up the conference but stay connected to both
                              		  parties. The oldest call will be put on hold, and the most recent call will be
                              		  actively connected to the initiator. The conference initiator can navigate
                              		  between the two parties by pressing the Hold soft key or the appropriate line
                              		  button on the phone.

If the endcall keyword is used, the conference
                              		  initiator can hang up or press the EndCall soft key to leave the conference
                              		  with the other two parties remaining connected.

In Cisco CME 3.2.3 and later versions, if the keep-conference command is not configured
                              		  (the default) or if the no keep-conference command is used, a conference
                              		  initiator can drop the last party that was added to the conference by pressing
                              		  the Confrn soft key (IP phone) or hookflash (analog phone).

## Examples

In the following example, extension 3555 initiates a three-way
                              		  conference. After the conference is established, extension 3555 can press the
                              		  Confrn soft key to disconnect the last party that was connected and remain
                              		  connected to the first party that was connected. If extension 3555 hangs up
                              		  from the conference, the other two parties remain connected if one of them is
                              		  local to the Cisco Unified CME system.

```
ephone-dn 35
 number 3555
ephone 24
 button 1:35
 keep-conference drop-last local-only
```

In the following example, extension 3666 initiates a three-way
                              		  conference. After the conference is established, extension 3666 can press the
                              		  Confrn soft key to disconnect the last party that was connected and remain
                              		  connected to the first party that was connected. Also, extension 3666 can hang
                              		  up from a three-way conference to terminate the conference and disconnect all
                              		  parties or can press the EndCall soft key to leave the conference and keep the
                              		  other two parties connected.

```
ephone-dn 36
 number 3666
ephone 25
 button 1:36
 keep-conference drop-last endcall
```

In the following example, extension 3777 initiates a three-way
                              		  conference. After the conference is established, extension 3777 can press the
                              		  Confrn soft key to disconnect the last party that was connected and remain
                              		  connected to the first party that was connected. Also, extension 3777 can hang
                              		  up from a three-way conference to terminate the conference and disconnect all
                              		  parties or press the EndCall soft key to leave the conference and keep the
                              		  other two parties connected only if one of the two parties is local to the
                              		  Cisco Unified CME system.

```
ephone-dn 38
 number 3777
ephone 27
 button 1:38
 keep-conference drop-last endcall local-only
```

In the following example, extension 3999 initiates a three-way
                              		  conference. After the conference is established, extension 3999 can hang up to
                              		  terminate the conference and disconnect all parties or press the EndCall soft
                              		  key to leave the conference and keep the other two parties connected only if
                              		  one of the two parties is local to the Cisco Unified CME system.

```
ephone-dn 39
 number 3999
ephone 29
 button 1:39
 keep-conference endcall local-only
```

### Related Commands

Command

Description

ephone-template (ephone)

Applies template to ephone being configured.

max-conferences

Sets the maximum number of three-party conferences
                                          						simultaneously supported by the Cisco Unified CME router.

transfer-system

Specifies the call transfer method for IP phone extensions
                                          						that use the ITU-T H.450.2 standard.

## keep-conference
                        	 (voice register)

To allow IP phone
                              		  conference initiators to exit from conference calls and keep the remaining
                              		  parties connected, use the keep-conference command in voice register pool configuration mode or voice
                              		  register template configuration mode. To disable the keep-conference feature,
                              		  use the no form of
                              		  this command.

keep-conference

no keep-conference

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

Default is
                              		  enabled.

### Command Modes

Voice register pool configuration (config-register-pool)

Voice register template configuration (config-register-temp)

## Command History

Cisco
                                          						IOS Release

Version

Modification

12.4(4)T

Cisco
                                          						CME 3.4

This
                                          						command was introduced.

Cisco
                                          						IOS XE Everest 16.5.1b

Unified CME 11.7

This
                                          						command was supported in voice register template configuration mode.

### Usage Guidelines

When the
                              		  conference initiator hangs up, Cisco Unified Communications Manager Express
                              		  (Cisco Unified CME) executes a call transfer to connect the two remaining
                              		  lines. The remaining calls are transferred without consultation. To facilitate
                              		  call transfer, the transfer-attended command or transfer-blind command must be enabled.

Conference
                              		  initiators can disconnect from their conference calls by pressing the Confrn
                              		  (conference) soft key. When an initiator uses the Confrn soft key to disconnect
                              		  from the conference call, the oldest call leg is put on hold, leaving the
                              		  initiator connected to the most recent call leg. The conference initiator can
                              		  then navigate between the two separate parties by pressing either the Hold soft
                              		  key or the line buttons to select the desired call.

## Examples

The following
                              		  example shows how to configure this command, if it was previously disabled, to
                              		  keep remaining conference legs after the conference initiator hangs up.

```
Router(config)# voice register pool 1 Router(config-register-pool)# keep-conference
```

The following
                              		  example shows how to configure this command under voice register template
                              		  configuration mode.

```
Router(config)# voice register template 1 Router(config-register-template)# keep-conference
```

### Related Commands

Command

Description

conference (voice register template)

Enables
                                          						a soft key for conference in a SIP phone template.

max-conferences

Sets
                                          						the maximum number of three-party conferences simultaneously supported by the
                                          						Cisco CME router.

transfer-attended (voice register template)

Enables
                                          						a soft key for attended transfer in a SIP phone template.

transfer-blind (voice register template)

Enables
                                          						a soft key for blind transfer in a SIP phone template.

voice register template

Enters
                                          						voice register template configuration mode and defines a template of common
                                          						parameters for SIP phones.

## keygen-retry

To specify the number of times that a CAPF server sends a
                              		  key-generation request, use the keygen-retry command in CAPF-server
                              		  configuration mode. To return to the default, use the no form of this command.

keygen-retry number

no keygen-retry

### Syntax Description

number

Number of retries. Range is from 0 to 100. Default is 3.

### Command Default

Number of retries is 3.

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

The following example specifies that the key generation process
                              		  should be tried 5 times.

```
Router(config)# capf-server Router(config-capf-server)# source address 10.10.10.1 Router(config-capf-server)# trustpoint-label server25 Router(config-capf-server)# cert-oper upgrade all Router(config-capf-server)# cert-enroll-trustpoint server12 password 0 x8oWiet Router(config-capf-server)# auth-mode auth-string Router(config-capf-server)# auth-string generate all Router(config-capf-server)# port 3000 Router(config-capf-server)# keygen-retry 5 Router(config-capf-server)# keygen-timeout 45 Router(config-capf-server)# phone-key-size 2048
```

### Related Commands

Command

Description

keygen-timeout

Specifies the number of minutes that the CAPF server waits
                                          						for a key-generation response from a phone.

## keypad-normalize

To impose a 200-millisecond delay before each keypad message from an
                              		  IP phone, use the keypad-normalize command in ephone or
                              		  ephone-template configuration mode. To return to the default, use the no form of this command.

keypad-normalize

no keypad-normalize

### Syntax Description

This command has no keywords or arguments.

### Command Default

Keypad messages are handled as fast as the system can handle them,
                              		  without an imposed delay.

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

### Usage Guidelines

This command normalizes the processing of incoming keypad messages
                              		  from an IP phone so that one message is processed every 200 milliseconds. This
                              		  is useful for handling the personal speed dial (fastdial) feature when the
                              		  destination of the call tends to be slower in accepting the digits, or when
                              		  converting keypad messages into appropriate digit events on the network side,
                              		  such as RFC 2833 digits.

If you use an ephone template to apply a command to a phone and you
                              		  also use the same command in ephone configuration mode for the same phone, the
                              		  value that you set in ephone configuration mode has priority.

## Examples

The following example normalizes the sending of digits from ephone
                              		  43.

```
ephone 43
 button 1:29
 keypad-normalize
```

### Related Commands

Command

Description

ephone-template (ephone)

Applies template to ephone being configured.

## keyphone

To designate a Cisco Unified IP phone as a marked or “key” phone when
                              		  using the Cisco Unified CME eXtensible Markup Language (XML) application
                              		  program interface (API), use the keyphone command in ephone or ephone-template
                              		  configuration mode. To remove the keyphone designation, use the no form of this command.

keyphone

no keyphone

### Syntax Description

This command has no arguments or keywords.

### Command Default

The phone that is being configured is not a “key” phone.

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

This command is used with the XML API to mark a Cisco Unified IP
                              		  phone as a “key” phone to be tracked while using the XML API. The XML API can
                              		  be instructed to report the status of only the “key” phones in the system for
                              		  network management purposes, for example.

If you use an ephone template to apply a command to a phone and you
                              		  also use the same command in ephone configuration mode for the same phone, the
                              		  value that you set in ephone configuration mode has priority.

## Examples

The following example sets the phone with the phone tag of 1 as a
                              		  “key” phone for the XML API:

```
Router(config)# ephone 1 Router(config-ephone)# keyphone
```

### Related Commands

Command

Description

ephone-template (ephone)

Applies template to ephone being configured.

| seconds | Interval time, in seconds. Range is from 10 to 65535.
                                          						Default is 30. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)T | Cisco CME 2.1 | This command was introduced. |
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was made available in ephone-template
                                          						configuration mode. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command in ephone-template configuration mode was
                                          						integrated into Cisco IOS Release 12.4(9)T. |

| Command | Description |
|---|---|
| ephone-template (ephone) | Applies template to ephone being configured. |
| keepalive (telephony-service) | Sets the time interval for keepalive messages between IP
                                          						phones and the Cisco Unified CME router. |

| seconds | Interval time, in seconds. Range is from 10 to 65535.
                                          						Default is 30. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco ITS 1.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |

| Command | Description |
|---|---|
| keepalive (ephone) | Sets the time interval for keepalive messages between a
                                          						particular IP phone and the Cisco CME router. |

| seconds | Sets the
                                          						time interval, in seconds, between keepalive messages that are sent to the
                                          						router by SIP Phones. If the interval is set to a larger value, it is possible
                                          						for notification to be delayed when the primary router goes down. Range is from
                                          						120 to 65535. Default is 120 seconds. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| Cisco
                                          						IOS XE Everest 16.4.1 | Cisco
                                          						Unified CME 11.6 | This
                                          						command was introduced. |

| Command | Description |
|---|---|
| keepalive (telephony-service) | Sets
                                          						the length of the time interval between successive keepalive messages from the
                                          						Cisco Unified CME router to SCCP phones. |

| seconds | Duration for registration, in seconds. Range: 60 to 3600.
                                          						Default: 300. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XW2 | Cisco Unified CME 4.2 | This command was introduced. |
| 12.4(15)XY | Cisco Unified CME 4.2 | This command was introduced. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4920)T. |

| Command | Description |
|---|---|
| register id | Creates an ID for explicitly identifying an external
                                          						feature server during Register requests. |

| seconds | Duration for a vpn-profile session, in seconds. Range: 0 to
                                          						120. Default: 60. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(3)T | Cisco Unified CME 8.5 | This command was introduced. |

| Command | Description |
|---|---|
| vpn-profile | Defines a VPN-profile. |

| drop-last | (Optional) The action of the Confrn soft key is changed;
                                          						the conference initiator can press the Confrn soft key (IP phone) or hookflash
                                          						(analog phone) to drop the last party. Note Analog phones connected to the Cisco Unified CME system
                                                   						through a Cisco VG 224 require Cisco IOS Release 12.3(11)YL1 or a later release
                                                   						to use this feature. | Note | Analog phones connected to the Cisco Unified CME system
                                                   						through a Cisco VG 224 require Cisco IOS Release 12.3(11)YL1 or a later release
                                                   						to use this feature. |
|---|---|---|---|
| Note | Analog phones connected to the Cisco Unified CME system
                                                   						through a Cisco VG 224 require Cisco IOS Release 12.3(11)YL1 or a later release
                                                   						to use this feature. |
| endcall | (Optional) The action of the EndCall soft key is changed;
                                          						the conference initiator can hang up or press the EndCall soft key to leave the
                                          						conference and keep the other two parties connected. Note If this option is not enabled, pressing the EndCall soft
                                                   						key terminates the conference and disconnects all parties. | Note | If this option is not enabled, pressing the EndCall soft
                                                   						key terminates the conference and disconnects all parties. |
| Note | If this option is not enabled, pressing the EndCall soft
                                                   						key terminates the conference and disconnects all parties. |
| local-only | (Optional) The conference initiator can hang up to end the
                                          						conference and leave the other two parties connected only if one of the
                                          						remaining parties is local to the Cisco Unified CME system (an internal
                                          						extension). |

| Note | Analog phones connected to the Cisco Unified CME system
                                                   						through a Cisco VG 224 require Cisco IOS Release 12.3(11)YL1 or a later release
                                                   						to use this feature. |
|---|---|

| Note | If this option is not enabled, pressing the EndCall soft
                                                   						key terminates the conference and disconnects all parties. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(11)T | Cisco CME 3.2 | This command was introduced. |
| 12.4(4)XC | Cisco Unified CME 4.0 | The drop-last and local-only keywords were added, and
                                          						this command was made available in ephone-template configuration mode. |
| 12.4(9)T | Cisco Unified CME 4.0 | The drop-last and local-only keywords, and this
                                          						command in ephone-template configuration mode were integrated into Cisco IOS
                                          						Release 12.4(9)T. |

| Note | This feature uses call transfer to connect the two remaining
                                       		  parties of a conference when a conference initiator leaves the conference. To
                                       		  use this feature, you must configure the transfer-system command using the full-blind , full-consult , or full-consult dss keywords. |
|---|---|

| Note | Analog phones connected to the Cisco Unified CME system through a
                                       		  Cisco VG 224 require Cisco IOS Release 12.3(11)YL1 or a later release to use
                                       		  this feature. |
|---|---|

| Command | Description |
|---|---|
| ephone-template (ephone) | Applies template to ephone being configured. |
| max-conferences | Sets the maximum number of three-party conferences
                                          						simultaneously supported by the Cisco Unified CME router. |
| transfer-system | Specifies the call transfer method for IP phone extensions
                                          						that use the ITU-T H.450.2 standard. |

| Cisco
                                          						IOS Release | Version | Modification |
|---|---|---|
| 12.4(4)T | Cisco
                                          						CME 3.4 | This
                                          						command was introduced. |
| Cisco
                                          						IOS XE Everest 16.5.1b | Unified CME 11.7 | This
                                          						command was supported in voice register template configuration mode. |

| Command | Description |
|---|---|
| conference (voice register template) | Enables
                                          						a soft key for conference in a SIP phone template. |
| max-conferences | Sets
                                          						the maximum number of three-party conferences simultaneously supported by the
                                          						Cisco CME router. |
| transfer-attended (voice register template) | Enables
                                          						a soft key for attended transfer in a SIP phone template. |
| transfer-blind (voice register template) | Enables
                                          						a soft key for blind transfer in a SIP phone template. |
| voice register template | Enters
                                          						voice register template configuration mode and defines a template of common
                                          						parameters for SIP phones. |

| number | Number of retries. Range is from 0 to 100. Default is 3. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| Command | Description |
|---|---|
| keygen-timeout | Specifies the number of minutes that the CAPF server waits
                                          						for a key-generation response from a phone. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| Command | Description |
|---|---|
| ephone-template (ephone) | Applies template to ephone being configured. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was made available in ephone-template
                                          						configuration mode. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command in ephone-template configuration mode was
                                          						integrated into Cisco IOS Release 12.4(9)T. |

| Command | Description |
|---|---|
| ephone-template (ephone) | Applies template to ephone being configured. |