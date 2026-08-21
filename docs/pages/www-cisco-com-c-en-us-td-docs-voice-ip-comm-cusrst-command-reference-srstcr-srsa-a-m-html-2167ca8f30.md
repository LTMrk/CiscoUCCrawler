---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cusrst-command-reference-srstcr-srsa-a-m-html-2167ca8f30
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cusrst/command/reference/srstcr/srsa_a_m.html
retrieved_at: 2026-08-21T10:06:47.811248+00:00
---

Cisco Unified SRST and Cisco Unified SIP SRST Command Reference (All Versions)

# Cisco Unified SRST and Cisco Unified SIP SRST Command Reference (All Versions)

## Results

Updated: April 21, 2026

Chapter: Command Reference:
	 A through M

## Chapter: Command Reference:
	 A through M

# Command Reference:
                     	 A through M

This chapter contains commands to configure and maintain Cisco Unified Survivable Remote Site Telephony (SRST) and Cisco Unified
                        SIP SRST. The commands are presented in alphabetical order. Some commands required for configuring Cisco Unified SRST and
                        Cisco Unified SIP SRST may be found in other Cisco IOS command references. Use the command reference primary index or search
                        online to find these commands.

## access-code

To configure trunk access codes for each type of line so that the
                              		  Cisco IP phones can access the trunk lines only during Cisco Unified
                              		  Communications Manager fallback when the Cisco Unified SRST feature is enabled,
                              		  use the access-code command in call-manager-fallback
                              		  configuration mode. To remove the telephone access code configuration from the
                              		  Cisco IP phones, use the no form of this command.

### FXO and EandM Line Types

access-code { fxo | e&m } dial-string

no access-code { fxo | e&m } dial-string

### BRI and PRI Line Types

access-code { bri | pri } dial-string [ direct-inward-dial ]

no access-code { bri | pri } [dial-string] [ direct-inward-dial ]

### Syntax Description

fxo

Enables a Foreign Exchange Office (FXO) interface.

e&m

Enables an analog ear and mouth (E&M) interface.

dial-string

Sets up dial access codes for each specified line type by
                                          						creating dial peers.

bri

Enables a BRI interface.

pri

Enables a PRI interface.

direct-inward-dial

(Optional) Enables direct inward dialing on a POTS dial
                                          						peer.

### Command Default

No default behavior or values.

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.1(5)YD

Cisco Unified SRST 1.0

This command was introduced on the following platforms:
                                          						Cisco 2600 series and Cisco 3600 series multiservice routers, and Cisco IAD2420
                                          						series IADs.

12.2(2)XT

Cisco Unified SRST 2.0

This command was implemented on Cisco 1750 and Cisco 1751
                                          						multiservice routers.

12.2(8)T

Cisco Unified SRST 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers.

### Usage Guidelines

The access-code command configures trunk access
                              		  codes for each type of line—BRI, E&M, FXO, and PRI—so that the Cisco IP
                              		  phones can access the trunk lines during Cisco Unified Communications Manager
                              		  fallback when Cisco Unified SRST is enabled. This provides systemwide access.

The access-code command creates temporary POTS
                              		  voice dial peers for all the selected types of voice ports during Cisco Unified
                              		  Communications Manager fallback. Use this command only if your normal network
                              		  dial-plan configuration prevents you from configuring permanent POTS voice dial
                              		  peers to provide trunk access for use in the fallback mode. When the access-code command is used, it is important
                              		  to ensure that all ports covered by the command have valid trunk connections.
                              		  Selection between ports for outgoing calls is random.

The dial string is used to set up temporary dial peers for each
                              		  specified line type. If there are multiple lines of the same type, a dial peer
                              		  is set up for each line. The dial peers are active only during Cisco Unified
                              		  Communications Manager fallback when the Cisco Unified SRST feature is enabled.
                              		  The result of this configuration is that all PSTN interfaces of the same type,
                              		  for example BRI, are treated as equivalent, and any port may be selected to
                              		  place the outgoing PSTN call. The direct-inward-dial keyword enables you to set
                              		  direct-inward-dialing access for PRI and BRI trunk lines.

## Examples

The following example sets the access-code command for BRI 8:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# access-code bri 8 direct-inward-dial The following example sets the access-code command for E&M 8:
Router(config)# call-manager-fallback Router(config-cm-fallback)# access-code e&m 8
```

The following example sets the access-code command for FXO 9:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# access-code fxo 9
```

The following example sets the access-code command for PRI 9:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# access-code pri 9 direct-inward-dial
```

### Related Commands

Command

Description

call-manager-fallback

Enables Cisco Unified SRST feature support and enters
                                          						call-manager-fallback configuration mode.

## addon

To define whether a phone type supports add-on modules, use the addon command in ephone-type configuration
                              		  mode. To reset to the default value, use the no form of this command.

addon

no addon

### Syntax Description

This command has no arguments or keywords.

### Command Default

Disabled (phone type does not support add-on modules).

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

Cisco Unified CME 7.0 Cisco Unified SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

This command specifies that add-on modules, such as the Cisco Unified
                              		  IP Phone 7915 Expansion Module, are supported by the type of phone being added
                              		  with the phone-type template.

## Examples

The following example shows that expansion modules are supported for
                              		  the phone being added with an ephone-type template:

```
Router(config)# ephone-type 7965 Router(config-ephone-type)# addon
```

### Related Commands

Command

Description

device-id

Specifies the device ID for a phone type in an ephone-type
                                          						template.

device-name

Assigns a name to a phone type in an ephone-type template.

## address (voice emergency response location)

To define the civic address for an ERL that is used for the ALI
                              		  database upload, use the address command in voice emergency response
                              		  location mode. To remove this definition, use the no form of the command. This command is
                              		  optional.

address string

no address

### Syntax Description

string

String (1-247 characters) used to identify an ERL’s civic
                                          						address.

### Command Default

The civic address is not defined.

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

This command creates a comma separated text entry of the ERL’s civic
                              		  address. The address information must be entered to conform with the NENA-2
                              		  Data Record specifications or the recommendations by the service provider.

## Examples

In this example, a civic address is displayed for ERL 60.

```
voice emergency response location 60
subnet 1 209.165.200.224 255.255.0.0
elin 1 4085550100
name Cookies and More Incorporated,
address I,408,5550100,,11902,,,Main Street,Emerald City,CA,Idina Menzel,1,,,,,,
```

### Related Commands

Command

Description

elin

Specifies a PSTN number that will replace the caller’s
                                          						extension.

name

Specifies a string (up to 30-characters) used internally to
                                          						identify or describe the emergency response location.

subnet

Defines which IP phones are part of this ERL.

## after-hour exempt (voice register pool)

To specify that a particular voice register pool does not have any of
                              		  its outgoing calls blocked, even though global system call blocking is enabled,
                              		  use the after-hours exempt command in voice register pool configuration mode. To return to
                              		  the default, use the no form of this command.

after-hour exempt

no after-hour exempt

### Syntax Description

This command has no arguments or keywords.

### Command Default

Disabled (global call blocking remains active, as configured).

### Command Modes

Voice register pool configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4 Cisco SRST 3.4

This command was introduced.

### Usage Guidelines

This command exempts individual Cisco SIP phones and phone extensions
                              		  in a voice register pool from call blocking.

Call blocking on Cisco IP phones is defined in the following way.
                              		  First, define one or more patterns of outgoing digits by using the after-hours block pattern command in either telephony-service configuration mode for
                              		  Cisco Unified CME or in call-manager-fallback configuration mode for Cisco
                              		  Unified SIP SRST. Next, define one or more time periods during which calls that
                              		  match those patterns are to be blocked are by using the after-hours date or after-hours day command or both. By default, all Cisco IP
                              		  phones in a Cisco Unified CME or Cisco Unified SIP SRST system are restricted
                              		  during the specified time if at least one pattern and at least one time period
                              		  are defined.

A phone extension is exempt as long as the after-hour exempt command is configured in voice register dn
                              		  or in voice register pool configuration mode.

## Examples

The following example shows how to configure a SIP phone, specified
                              		  by the voice register pool command, so that outgoing calls are not
                              		  blocked:

```
Router(config)# voice register pool 23 Router(config-register-pool)# after-hour exempt
```

The following example shows how to specify that outgoing calls from
                              		  extension 5001 under voice register pool 2 are not blocked:

```
Router(config)# voice register pool 2 Router(config-register-pool)# number 5001 Router(config-register-pool)# after-hour exempt
```

### Related Commands

Command

Description

after-hours block pattern

Defines a pattern of digits for blocking outgoing calls
                                          						from IP phones.

after-hours block pattern (call-manager- fallback)

Defines a pattern of digits for blocking outgoing calls
                                          						from IP phones.

after-hours date

Defines a recurring period based on date during which
                                          						outgoing calls that match defined block patterns are blocked on IP phones.

after-hours date (call-manager- fallback)

Defines a recurring period based on date during which
                                          						outgoing calls that match defined block patterns are blocked on IP phones.

after-hours day

Defines a recurring period based on day of the week during
                                          						which outgoing calls that match defined block patterns are blocked on IP
                                          						phones.

after-hours day (call-manager- fallback)

Defines a recurring period based on day of the week during
                                          						which outgoing calls that match defined block patterns are blocked on IP
                                          						phones.

after-hour exempt (voice register dn)

Specifies that an individual extension on a SIP phone does
                                          						not have any of its outgoing calls blocked even though global system call
                                          						blocking is enabled.

call-manager-fallback

Enables Cisco Unified SIP SRST support and enter
                                          						call-manager-fallback configuration mode.

id (voice register pool)

Explicitly identifies a locally available individual Cisco
                                          						SIP IP phone, or when running Cisco Unified SIP SRST, set of Cisco Unified SIP
                                          						IP phones.

telephony-service

Enters telephony-service configuration mode to configure a
                                          						Cisco Unified Communications Manager Express (Cisco Unified CME) system.

voice register dn

Enters voice register dn configuration mode to define an
                                          						extension for a SIP phone line.

voice register pool

Enters voice register pool configuration mode for Cisco SIP
                                          						IP phones.

## after-hours block pattern (call-manager-fallback)

To define a pattern of outgoing digits for call blocking from IP
                              		  phones, use the after-hours block pattern command in call-manager-fallback configuration mode. To delete
                              		  a call-blocking pattern, use the no form of this command.

after-hours block pattern pattern-tag pattern [7-24]

no after-hours block pattern pattern-tag

### Syntax Description

pattern- tag

Identifier for a call-blocking pattern. Up to 32
                                          						call-blocking patterns can be defined in separate commands.

pattern

Outgoing call digits to be matched for blocking.

7-24

(Optional) If the 7-24 keyword is specified, the pattern is always blocked,
                                          						7 days a week, 24 hours a day. If the 7-24 keyword is not specified, the
                                          						pattern is blocked during the days and dates that are defined with the after-hours day and after-hours date commands.

### Command Default

No pattern is defined.

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco Unified SRST 3.0

This command was introduced.

12.3(4)T

Cisco Unified SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

15.3(2)T

Cisco Unified CME 9.5

This command was modified to include regular expressions as
                                          						a value for the pattern argument.

### Usage Guidelines

Call blocking on IP phones is defined in the following way. First,
                              		  one or more patterns of outgoing digits are defined using the after-hours block pattern command. Next, one or more time periods
                              		  during which calls that match those patterns are to be blocked are defined
                              		  using the after-hours date or after-hours day command or both. By default, all IP phones in
                              		  a Cisco Unified SRST system are restricted during the specified time if at
                              		  least one pattern and at least one time period are defined.

Blocked calls return a fast-busy tone to the user for approximately
                              		  10 seconds before the call is terminated and the line is returned to on-hook
                              		  status.

In Cisco Unified SRST 9.5, support for afterhours pattern blocking is
                              		  extended to regular expression patterns for dial plans on Cisco Unified SIP and
                              		  Cisco Unified SCCP IP phones. With this support, users can add a combination of
                              		  fixed dial plans and regular expression-based dial plans.

When a call is initiated after hours, the dialed number is matched
                              		  against a combination of dial plans. If a match is found, the call is blocked.

To enable regular expression patterns to be included when configuring
                              		  afterhours pattern blocking, the after-hours block pattern command is modified to include regular
                              		  expressions as a value for the pattern argument.

## Examples

The following example defines pattern 1, which blocks international
                              		  calls after hours for a Cisco Unified SRST system that requires dialing 9 for
                              		  external calls:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# after-hours block pattern 1 9011
```

The following example shows how to configure several afterhours block
                              		  patterns of regular expressions:

```
Router# configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)# call-manager-fallback Router(config-telephony)# after-hours block pattern 1 ?
  WORD  Specific block pattern or a regular expression for after-hour block
        pattern
Router(config-cm-fallback)# after-hours block pattern 1 1234 Router(config-cm-fallback)# after-hours block pattern 2 .T Router(config-cm-fallback)# after-hours block pattern 3 987654([1-3])+ Router(config-cm-fallback)# after-hours block pattern 4 98765432[1-9] Router(config-cm-fallback)# after-hours block pattern 5 98765(432|422|456)
```

### Related Commands

Command

Description

after-hours date (call- manager-fallback)

Defines a recurring period based on date during which
                                          						outgoing calls that match defined block patterns are blocked on IP phones.

after-hours day (call- manager-fallback)

Defines a recurring period based on day of the week during
                                          						which outgoing calls that match defined block patterns are blocked on IP
                                          						phones.

## after-hours date (call-manager-fallback)

To define a recurring period based on date during which outgoing
                              		  calls that match defined block patterns are blocked on IP phones, use the after-hours date command in call-manager-fallback configuration mode. To delete
                              		  a defined time period, use the no form of this command.

after-hours date month date start-time stop-time

no after-hours date month date

### Syntax Description

month

Abbreviated month. The following abbreviations for month
                                          						are valid: jan , feb , mar , apr , may , jun , jul , aug , sep , oct , nov , dec .

date

Date of the month. Range is from 1 to 31.

start-time stop-time

Beginning and ending times for call blocking, in an HH:MM
                                          						format using a 24-hour clock. The stop time must be greater than the start
                                          						time. The value 24:00 is not valid. If 00:00 is entered as a stop time, it is
                                          						changed to 23:59. If 00:00 is entered for both start time and stop time, calls
                                          						are blocked for the entire 24-hour period on the specified date.

### Command Default

No time period based on date is defined for call blocking.

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco Unified SRST 3.0

This command was introduced.

12.3(4)T

Cisco Unified SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

Call blocking on IP phones is defined in the following way. First,
                              		  one or more patterns of outgoing digits are defined using the after-hours block pattern command. Next, one or more time periods
                              		  during which calls that match those patterns are to be blocked are defined
                              		  using the after-hours date or after-hours day command or both. By default, all IP phones in
                              		  a Cisco Unified SRST system are restricted during the specified time if at
                              		  least one pattern and at least one time period are defined.

Call blocking for the time period that is defined in this command
                              		  recurs annually on the date specified in the command.

## Examples

The following example defines January 1 as an entire day on which
                              		  calls that match the pattern specified in the after-hours block pattern command are blocked:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# after-hours date jan 1 00:00 00:00
```

### Related Commands

Command

Description

after-hours block pattern (call-manager- fallback)

Defines a pattern of digits for blocking outgoing calls
                                          						from IP phones.

after-hours day (call- manager-fallback)

Defines a recurring period based on day of the week during
                                          						which outgoing calls that match defined block patterns are blocked on IP
                                          						phones.

## after-hours day (call-manager-fallback)

To define a recurring period based on date during which outgoing
                              		  calls that match defined block patterns are blocked on IP phones, use the after-hours date command in call-manager-fallback configuration mode. To delete
                              		  a defined time period, use the no form of this command.

after-hours date month date start-time stop-time

no after-hours date month date

### Syntax Description

month

Abbreviated month. The following abbreviations for month
                                          						are valid: jan , feb , mar , apr , may , jun , jul , aug , sep , oct , nov , dec .

date

Date of the month. Range is from 1 to 31.

start-time stop-time

Beginning and ending times for call blocking, in an HH:MM
                                          						format using a 24-hour clock. The stop time must be greater than the start
                                          						time. The value 24:00 is not valid. If 00:00 is entered as a stop time, it is
                                          						changed to 23:59. If 00:00 is entered for both start time and stop time, calls
                                          						are blocked for the entire 24-hour period on the specified date.

### Command Default

No time period based on date is defined for call blocking.

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco Unified SRST 3.0

This command was introduced.

12.3(4)T

Cisco Unified SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

Call blocking on IP phones is defined in the following way. First,
                              		  one or more patterns of outgoing digits are defined using the after-hours block pattern command. Next, one or more time periods
                              		  during which calls that match those patterns are to be blocked are defined
                              		  using the after-hours date or after-hours day command or both. By default, all IP phones in
                              		  a Cisco Unified SRST system are restricted during the specified time if at
                              		  least one pattern and at least one time period are defined.

Call blocking for the time period that is defined in this command
                              		  recurs annually on the date specified in the command.

## Examples

The following example defines January 1 as an entire day on which
                              		  calls that match the pattern specified in the after-hours block pattern command are blocked:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# after-hours date jan 1 00:00 00:00
```

### Related Commands

Command

Description

after-hours block pattern (call- manager-fallback)

Defines a pattern of digits for blocking outgoing calls
                                          						from IP phones.

after-hours day (call- manager-fallback)

Defines a recurring period based on day of the week during
                                          						which outgoing calls that match defined block patterns are blocked on IP
                                          						phones.

## alias (call-manager-fallback)

To provide a mechanism for rerouting calls to telephone numbers that
                              		  are unavailable during Cisco Unified Communications Manager fallback, use the alias command in call-manager-fallback configuration mode. To disable
                              		  rerouting of unmatched call destination calls, use the no form of this command.

alias tag number-pattern to alternate-number [ preference preference-value ] [ cfw number timeout timeout-value ] [ huntstop ]

no alias tag number-pattern to alternate-number [ preference preference-value ] [ cfw number timeout timeout-value ] [ huntstop ]

### Syntax Description

tag

Identifier for alias rule range. The range is from 1 to 50.

number-pattern

Pattern to match the incoming telephone number. This
                                          						pattern may include wildcards. A number-pattern can be used multiple
                                          						times.

to

Connects the tag number pattern to the alternate number.

alternate-number

Alternate telephone number to route incoming calls to match
                                          						the number pattern. The alternate number has to be a specific extension that
                                          						belongs to an IP phone that is actively registered on the Cisco Unified SRST
                                          						router. The alternate telephone number can be used in multiple alias commands.

preference

(Optional) Assigns a dial-peer preference value to the
                                          						alias. Use with the max-dn command.

preference-value

(Optional) Preference value of the associated dial peer.
                                          						The range is from 0 to 10.

cfw number

(Optional) Allows users to set call forward busy and call
                                          						forward no answer to a set string and override globally configured call forward
                                          						settings.

timeout timeout-value

(Optional) Sets the ring no-answer timeout duration for
                                          						call forwarding, in seconds. Range is from 3 to 60000. The cfw keyword assumes that you want
                                          						to forward calls to the same number for both busy and no-answer call forward
                                          						cases. The timeout-value applies only to the no-answer call
                                          						forward case. There is no timeout required for a busy call forward situation.

huntstop

(Optional) Stops call hunting after trying the alternate-number . This keyword only
                                          						has an effect if the global command no huntstop is set.

### Command Default

No default behavior or values.

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(2)XT

Cisco Unified SRST 2.0

This command was introduced on the following platforms:
                                          						Cisco 1750, Cisco 1751, Cisco 2600 series and Cisco 3600 series multiservice
                                          						routers, and Cisco IAD2420 series IADs.

12.2(8)T

Cisco Unified SRST 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers.

12.2(8)T1

Cisco Unified SRST 2.0

This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers.

12.2(11)T

Cisco Unified SRST 2.01

This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers. The preference keyword was added.

12.3(11)T

Cisco Unified SRST 3.2

The cfw keyword was added. The maximum number of alias commands used for creating
                                          						calls to telephone numbers that are unavailable during Cisco Unified
                                          						Communications Manager fallback was increased to 50. The alternate-number argument can be
                                          						used in multiple alias commands.

### Usage Guidelines

The alias command provides a mechanism for
                              		  rerouting calls to telephone numbers that are unavailable during fallback. Up
                              		  to 50 sets of rerouting alias rules can be created for calls to telephone
                              		  numbers that are unavailable during Cisco Unified Communications Manager
                              		  fallback. Sets of alias rules are created using the alias command. An alias is activated when a
                              		  telephone registers that has a phone number matching a configured alternate-number alias. Under that condition, an incoming call
                              		  is rerouted to the alternate number. The alternate-number argument can be used in multiple alias commands, allowing you to reroute
                              		  multiple different numbers to the same target number.

The configured alternate-number must be a specific E.164
                              		  phone number or extension that belongs to an IP phone registered on the Cisco
                              		  Unified SRST router. When an IP phone registers with a number that matches an alternate-number , an additional POTS dial
                              		  peer is created. The destination pattern is set to the initial configured number-pattern , and the POTS dial peer voice
                              		  port is set to match the voice port associated with the alternate-number .

If other IP phones register with specific phone numbers within the
                              		  range of the initial number-pattern , the call is routed back to
                              		  the IP phone rather than to the alternate-number (according to normal
                              		  dial-peer longest-match, preference, and huntstop rules).

The cfw keyword allows you to configure a call
                              		  forward destination for calls that are busy or not answered. Call forward no
                              		  answer is defined as when the phone rings for a few seconds and the call is not
                              		  answered, it is forwarded to the configured destination. Call forward busy and
                              		  call forward no answer can be configured to a set string and override globally
                              		  configured call forward settings.

You can also create a specific call forwarding path for a particular
                              		  number. The benefit of using the cfw keyword is that during SRST, you can
                              		  reroute calls from otherwise unreachable numbers onto phones that are
                              		  available. Basic hunt groups can be established with call-forwarding rules so
                              		  that if the first SRST phone is busy, you can forward the call to a second SRST
                              		  phone.

The cfw keyword also allows you to alias a phone
                              		  number to itself, permitting setting of per-phone number forwarding. An example
                              		  of aliasing a number to itself follows. If a phone registers with extension
                              		  1001, a dial peer that routes calls to the phone is automatically created for
                              		  1001. If the call-manager-fallback dial-peer preference (set with the max-dn command) for this initial dial peer is
                              		  set to 2, the dial peer uses 2 as its preference setting.

Then, use the alias command to alias the phone number to itself:

```
alias 1 1001 to 1001 preference 1 cfw 2001 timeout 20
```

In this example, you have created a second dial peer for 1001 to
                              		  route calls to 1001, but that has preference 1 and call forwarding to 2001.
                              		  Because the preference on the dial peer created by the alias command is now a lower numeric value
                              		  than the preference that the dial peer first created, all calls come initially
                              		  to the dial peer created by the alias command. In that way the calls are
                              		  subject to the forwarding as set by the alias command, instead of any call forwarding that may have been set
                              		  globally.

The alias huntstop keyword is relevant only if you have
                              		  also set the global no huntstop command under call-manager-fallback.
                              		  Also, you may need to set the global no huntstop if you have multiple alias commands with the
                              		  same number-pattern , and you want to enable hunting on
                              		  busy between the aliases. That is, one alias for number-pattern is tried, and then if that
                              		  phone is busy, the second alias for number-pattern is tried.

The alias huntstop keyword allows you to turn huntstop
                              		  behavior back on for an individual alias, if huntstop is turned off globally by
                              		  the no huntstop command. Setting the huntstop keyword on an individual alias stops
                              		  hunting at the alias, making the alias the final member of the hunt sequence.

## Examples

In the following example, alias 1 is configured to route calls to
                              		  extensions 6000 through 6099 to extension 5001 using a dial peer with a
                              		  preference value of 2. Extensions 6000 through 6099 are a subset of IP phones
                              		  without fallback service. During fallback, calls to these extensions are routed
                              		  to 5001.

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# alias 1 60.. to 5001 preference 2
```

In the following example, alias 1 is set up to route calls coming
                              		  into extensions 5000 through 5999 to extension 6000. The routing occurs when
                              		  extensions 5000 through 5999 are unavailable during Cisco Unified
                              		  Communications Manager fallback.

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# alias 1 5... to 6000
```

The following example sets the preference keyword in the alias command to a lower preference value
                              		  than the preference number created by the max-dn command. Setting a lower value allows
                              		  the cfw keyword to take effect. The incoming call
                              		  to extension 1000 hunts to alias because it has a lower preference, and
                              		  no-answer/busy calls to 1000 are forwarded to 2000. All incoming calls to other
                              		  extensions in SRST mode are forwarded to 3000 after 10 seconds.

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# alias 1 1000 to 1000 preference 1 cfw 2000 timeout 10 Router(config-cm-fallback)# max-dn 10 preference 2 Router(config-cm-fallback)# call-forward busy 3000 Router(config-cm-fallback)# call-forward noan 3000 timeout 10
```

### Related Commands

Command

Description

call-manager-fallback

Enables Cisco Unified SRST feature support and enters
                                          						call-manager-fallback configuration mode.

default-destination

Assigns a default destination number for incoming telephone
                                          						calls on the Cisco Unified SRST router.

max-dn (call- manager-fallback)

Sets the maximum possible number of virtual voice ports
                                          						that can be supported by a router and activates dual-line mode.

show dialplan number

Displays which outgoing dial peer is reached when a
                                          						particular phone number is dialed.

## alias (voice register pool)

To allow Cisco Session Initiation Protocol (SIP) IP phones to handle
                              		  inbound PSTN calls to telephone numbers that are unavailable when the main
                              		  proxy is not available, use the alias command in voice register pool configuration mode. To disable
                              		  rerouting of unmatched call destination calls, use the no form of this command.

alias tag pattern to target [ preference value ]

no alias tag

### Syntax Description

tag

Number from 1 to 5 and the distinguishing factor when there
                                          						are multiple alias commands.

pattern

Prefix number that represents a pattern against which to
                                          						match the incoming telephone number. It may include wildcards.

to

Connects the number pattern to the target (alternate number).

target

Target number. An alternate telephone number to route
                                          						incoming calls that match the number pattern. The target must be a full E.164
                                          						number.

preference value

(Optional) Assigns a dial-peer preference value to the
                                          						alias. The value argument is the value of the associated dial
                                          						peer. The range is from 1 to 10. There is no default.

### Command Default

None

### Command Modes

Voice register pool configuration

## Command History

Release

Product Version

Modification

12.2(15)ZJ

Cisco SIP SRST 3.0

This command was introduced to Cisco Unified.

12.3(4)T

Cisco SIP SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

The alias command services calls placed to telephone numbers that are
                              		  unavailable because the main proxy is not available. The alias command is activated when a Cisco SIP IP phone that has an
                              		  extension number matching the target number registers.

When a phone with the target number registers, calls that match the
                              		  number pattern are rerouted to the target number. The target number must be a
                              		  local phone number to enable rerouting of a range of number patterns. When a
                              		  Cisco SIP IP phone registers with a target number, an additional VoIP dial peer
                              		  is created using the target number IP address as a session target and
                              		  destination pattern as configured with the alias pattern command. For the alias command to work, the VoIP dial peer
                              		  must be set with a translation rule to translate the called number to the
                              		  target number. Translation rules can be configured under voice register pool
                              		  configuration mode.

If other Cisco SIP IP phones register that have specific phone
                              		  numbers that fall within the alias range or if another static dial peer exists
                              		  for this pattern, the call is routed using the appropriate dial peer in
                              		  preference to being rerouted to this alternate alias number (according to
                              		  normal dial-peer longest-match, preference, and huntstop rules).

## Examples

The following example configures calls to numbers in the 5000 to 5099
                              		  range that are not otherwise explicitly resolved to a specific extension number
                              		  to be routed to the phone with extension 5001. Phone calls intended for phones
                              		  that are not given fallback service can then be redirected to the specified
                              		  extension number.

```
Router(config)# voice register pool Router(config-register-pool)# alias 1 50.. to 5001
```

### Related Commands

Command

Description

id (voice register pool)

Explicitly identifies a locally available individual Cisco
                                          						SIP IP phone or set of Cisco SIP IP phones.

show dial-peer voice

Displays information for voice dial peers.

translate-outgoing (voice register pool)

Applies a translation rule to manipulate dialed digits on
                                          						an outbound POTS or VoIP call leg.

voice register pool

Enables SIP SRST voice register pool configuration
                                          						commands.

## allow-hash-in-dn(voice register global)

To allow the
                              		  insertion of '#' at any place in voice register dn, use the allow-hash-in-dn command in voice register global
                              		  mode. To disable this, use the no form of
                              		  this command.

allow-hash-in-dn

no allow-hash-in-dn

### Syntax Description

allow-hash-in-dn

Allow
                                          						the insertion of hash at all places in voice register dn.

### Command Default

This command is
                              		  disabled by default.

### Command Modes

Voice register global configuration

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

15.6(2)T

Cisco
                                          						SIP SRST 11.0

This
                                          						command was introduced.

### Usage Guidelines

Before this
                              		  command was introduced, the characters supported in voice register dn were 0-9,
                              		  +, and *. The new command is enabled whenever the user requires the insertion
                              		  of # in voice register dn. The command is disabled by default. You can
                              		  configure this command only in Cisco Unified SRST and Cisco Unified E-SRST
                              		  modes. The character # can be inserted at any place in voice register dn. When
                              		  this command is enabled, users are required to change the default termination
                              		  character(#) to another valid character using ?dial-peer
                                    				terminator? command under configuration mode.

## Examples

The following
                              		  example shows how to enable the command in mode E-SRST, SRST and how to change
                              		  the default terminator:

```
Router(config)#voice register global
Router(config-register-global)#mode esrst
Router(config-register-global)#allow-hash-in-dn

Router(config)#voice register global
Router(config-register-global)#no mode [Default SRST mode]
Router(config-register-global)#allow-hash-in-dn

Router(config)#dial-peer terminator ?
WORD Terminator character: '0'-'9', 'A'-'F', '*', or '#'

Router(config)#dial-peer terminator *
```

### Related Commands

Command

Description

dial-peer terminator

Configures the character used as a terminator for
                                          						variable-length dialed numbers.

## application (call-manager-fallback)

To select the session-level application for all Cisco IP phone lines
                              		  served by the Cisco Unified SRST router, use the application command in call-manager-fallback configuration mode. To disable
                              		  this application, use the no form of this command.

application application-name

no application application-name

### Syntax Description

application-name

Interactive voice response (IVR) application name.

### Command Default

DEFAULT system session application

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco Unified SRST 3.0

This command was introduced.

12.3(4)T

Cisco Unified SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

Use this command to assign a Tool Command Language (Tcl) IVR
                              		  application to all IP phones served by the Cisco Unified SRST router.

## Examples

The following example selects a Tcl IVR application named “app-xfer”
                              		  for all IP phones served by the Cisco Unified SRST router:

```
Router(config)# call-manager-fallback Router(config-cm-fallback) application app-xfer
```

### Related Commands

Command

Description

call-manager-fallback

Enables Cisco Unified SRST and enters call-manager-fallback
                                          						configuration mode.

## application (voice register global)

To select the session-level application for all dial peers associated
                              		  with Session Initiation Protocol (SIP) phones, use the application command in voice register global configuration mode. To disable
                              		  use of the application, use the no form of this command.

application application-name

no application

### Syntax Description

application-name

Interactive voice response (IVR) application name.

### Command Default

Default application on router

### Command Modes

Voice register global configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was introduced.

### Usage Guidelines

During Cisco Unified Communications Manager Express (Cisco Unified
                              		  CME) or Cisco Unified Session Initiation Protocol (SIP) Survivable Remote Site
                              		  Telephony (SRST) registration, a dial peer is created for each SIP phone and
                              		  that dial peer includes the default session application. The application command allows you to change the
                              		  default application for all dial peers associated with the Cisco SIP IP phones,
                              		  if desired. The applied application (or TCL IVR script) must support call
                              		  redirection. Use the show call application voice summary command to display a list of applications.

The application command in voice register pool
                              		  configuration mode takes precedence over this command in voice register global
                              		  configuration mode.

## Examples

The following example shows how to set the Tcl IVR application
                              		  globally for all SIP phones:

```
Router(config)# voice register global Router(config-register-global)# mode cme Router(config-register-global)# application sipapp2
```

### Related Commands

Command

Description

application (dial-peer)

Enables a specific application on a dial peer.

application (voice register pool)

Selects the session-level application for the dial peer
                                          						associated an individual SIP phone in a Cisco Unified CME environment or for a
                                          						group of phones in a Cisco Unified SIP SRST environment.

id (voice register pool)

Explicitly identifies a locally available individual Cisco
                                          						SIP IP phone, or when running Cisco Unified SIP SRST, set of Cisco SIP IP
                                          						phones.

mode (voice register global)

Enables the mode for provisioning SIP phones in a Cisco
                                          						Unified CME system.

show call application voice summary

Displays information about voice applications.

show dial-peer voice

Displays information for dial peers.

voice register global

Enters voice register global configuration mode in order to
                                          						set global parameters for all supported Cisco SIP phones in a Cisco Unified CME
                                          						or Cisco Unified SIP SRST environment.

voice register pool

Enters voice register pool configuration mode for SIP
                                          						phones.

## application (voice register pool)

To select the session-level application for the dial peer associated
                              		  with an individual Session Initiation Protocol (SIP) phone in a Cisco Unified
                              		  Communications Manager Express (Cisco Unified CME) environment or for a group
                              		  of phones in a Cisco Unified SIP Survivable Remote Site Telephony (SRST)
                              		  environment, use the application command in voice register pool configuration mode. To disable
                              		  use of the application, use the no form of this command.

application application-name

no application

### Syntax Description

application-name

Name of the selected interactive voice response (IVR)
                                          						application name.

### Command Default

Default application on router

### Command Modes

Voice register pool configuration

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

During Cisco Unified CME or Cisco Unified SIP SRST registration, a
                              		  dial peer is created for each SIP phone and that dial peer includes the default
                              		  session application. The application command allows you to change the
                              		  default application for all dial peers associated with the Cisco SIP IP phones,
                              		  if desired. The applied application (or TCL IVR script) must support call
                              		  redirection. Use the show call application voice summary command to display a list of applications.

The application command in voice register pool
                              		  configuration mode takes precedence over this command in voice register global
                              		  configuration mode.

## Examples

The following example shows how to set the IVR application for the
                              		  SIP phone specified by the voice register pool command:

```
Router(config)# voice register pool 1 Router(config-register-pool) application sipapp2
```

The following partial sample output from the show running-config command shows that voice register pool 1 has been set up to use
                              		  the SIP.app application:

```
voice register pool 1 
 id network 172.16.0.0 mask 255.255.0.0
 application SIP.app
 voice-class codec 1
```

### Related Commands

Command

Description

application (dial-peer)

Enables a specific application on a dial peer.

application (voice register global)

Selects the session-level application for all dial peers
                                          						associated with SIP phones.

id (voice register pool)

Explicitly identifies a locally available individual Cisco
                                          						SIP IP phone, or when running Cisco Unified SIP SRST, set of Cisco SIP IP
                                          						phones.

mode (voice register global)

Enables the mode for provisioning SIP phones in a Cisco
                                          						Unified CME system.

show call application voice summary

Displays information about voice applications.

show dial-peer voice

Displays information for dial peers.

voice register global

Enters voice register global configuration mode in order to
                                          						set global parameters for all supported Cisco SIP phones in a Cisco Unified CME
                                          						or Cisco Unified SIP SRST environment.

voice register pool

Enters voice register pool configuration mode for SIP
                                          						phones.

## attempted-registrations size

To set the size of the table that shows a number of
                              		  attempted-registrations, use the attempted- registrations command in voice
                              		  register global mode. To set the size of attempted-registrations table to its
                              		  default value, use the no form of this command.

attempted-registrations size size

no attempted-registrations size

### Syntax Description

size

Number of entries in attempted registrations table. Size
                                          						range from 0 to 50.

### Command Default

The default size for attempted registration table is 10.

### Command Modes

voice register global

## Command History

Cisco IOS Release

Cisco Product

Modification

15.1(2)T

Cisco Unified CME 8.1 Cisco Unified SRST 8.1

This command was introduced.

### Usage Guidelines

Use this command to define the size of the table that stores
                              		  information related to SIP phones that attempt to register with Cisco Unified
                              		  CME or Cisco Unified SRST and fail. The default size of an attempted
                              		  registration table is 10. The minimum size of attempted registration table is
                              		  0. Use the attempted-registration size 0 when you do not wish to store any
                              		  information about phones attempting to register with the Cisco Unified CME or
                              		  Cisco Unified SRST and fail. The maximum size of attempted registration table
                              		  is 50.

When the current number of entries in the table is more than the new
                              		  size that is being configured, system prompts the user for the following
                              		  confirmation, “This will remove x old entries from the table. Proceed? Yes/No
                              		  ?”. The default user confirmation is “No”. Where “x” represents the number of
                              		  entries that will be deleted. The old entries are classified on basis of the
                              		  time-stamp of the latest register attempt made by the phone.

During rollback, the user confirmation is not sought and the target
                              		  configuration is applied. If the current number of entries in the table is more
                              		  than the default value of the table size, then entries in excess of the default
                              		  table size are cleared before reverting to the target table size.

For example, if the configured table size is 40 and there are
                              		  currently 35 entries in the table, any change in the size of the attempted
                              		  registration table during rollback removes 25 oldest entries leaving only the
                              		  default (10) entries before making the table size equal to the size in target
                              		  configuration.

## Examples

The following example shows attempted-registrations size:

```
Router# conf t
Router(config)#voice register global
Router(config-register-global)#attempted-registrations size 15
!
```

### Related Commands

Command

Description

clear voice register attempted- registrations

Allows to delete entries in attempted-registration table.

show voice register attempted-registrations

Displays details of phones that attempted to register and
                                          						failed.

## audible-tone

To configure
                              		  audible tones to indicate successful join and unjoin and login and logout from
                              		  any hunt group, use the audible-tone command in ephone or ephone-template configuration
                              		  mode. To revert to the default behavior of not playing any audible tone, use
                              		  the no form of
                              		  this command.

audible-tone

no audible-tone

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

By default, this
                              		  feature is disabled.

### Command Modes

Ephone configuration (config-ephone)

Ephone-template configuration (config-ephone-template)

## Command History

This
                                       					 command was introduced.

### Usage Guidelines

Use the audible-tone command to set an audible tone to confirm successful
                              		  join and unjoin and log in and log out from specific hunt groups.

## Examples

The following
                              		  example shows how to configure audible tone in ephone configuration mode:

```
Router(config)# ephone 1 Router(config-ephone)# audible-tone
```

The following
                              		  example shows how to configure audible tone in ephone-template configuration
                              		  mode:

```
Router(config)# ephone-template 1 Router(config-ephone-template)# audible-tone
```

### Related Commands

Command

Description

ephone-hunt group

Configures an ephone hunt group in Cisco Unified SRST.

voice-hunt group

Configures a voice hunt group in Cisco Unified SRST.

## authenticate (voice register global)

To define the authenticate mode for SIP phones in a Cisco Unified CME
                              		  or Cisco Unified SRST system, use the authenticate command in voice register global configuration mode. To return
                              		  to the default, use the no form of this command.

### Cisco IOS Release 12.4(11)XJ and later releases

authenticate { credential tag location | ood-refer | presence | realm string | register }

no authenticate { credential tag location | ood-refer | presence | realm string | register }

### Cisco IOS Release 12.4(4)T

authenticate [ all ] [ realm string ]

no authenticate [ all ] [ realm string ]

### Syntax Description

credential tag

Number that identifies the credential file to use for
                                          						out-of-dialog REFER (OOD-R) or presence authentication. Range: 1 to 5.

location

Name and location of the credential file in URL format.
                                          						Valid storage locations are TFTP, HTTP, and flash memory.

ood-refer

Incoming OOD-R requests are authenticated using RFC
                                          						2617-based digest authentication.

presence

Incoming presence subscription requests from an external
                                          						presence server are authenticated.

realm string

Realm parameter for challenge and response as specified in
                                          						RFC 2617 is authenticated.

register

All incoming registration requests are challenged and
                                          						authenticated. Valid for Cisco Unified CME only.

### Command Default

Authenticate mode is disabled.

### Command Modes

Voice register global configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4

This command was introduced.

12.4(11)XJ

Cisco Unified CME 4.1 Cisco Unified SRST 4.1

The credential , ood-refer , presence , and register keywords were added. The register keyword replaced the all keyword.

12.4(15)T

Cisco Unified CME 4.1 Cisco Unified SRST 4.1

The modifications to this command were integrated into
                                          						Cisco IOS Release 12.4(15)T.

### Usage Guidelines

The credential keyword allows OOD-R and presence
                              		  service to use credential files for authentication. Up to five text files
                              		  containing username and password pairs can be defined and loaded into the
                              		  system. The contents of these five files are mutually exclusive; the username
                              		  and password pairs must be unique across all the files. For Cisco Unified CME,
                              		  the username and password pairs cannot be the same ones defined for SCCP or SIP
                              		  phones with the username command.

The ood-refer keyword specifies that any OOD-R
                              		  request that passes authentication is authorized to setup calls between referee
                              		  and refer-target if OOD-R is enabled with the refer-ood enable command.

The presence keyword enables digest
                              		  authentication for external watchers. Credentials are verified against a
                              		  credential file stored in flash. This applies to both OOD-R and presence. The
                              		  default is to authenticate all SUBSCRIBE requests from external watchers. An
                              		  external watcher that passes authentication is authorized to subscribe to
                              		  presence service for all lines allowed to be watched.

The register keyword enables authentication for registration requests in
                              		  which the MAC address of the SIP phone cannot be identified by using other
                              		  methods. All incoming register requests are challenged and authenticated. The realm keyword with the string argument specifies the character
                              		  string to be included in the challenge.

## Examples

The following example shows that all registration requests from SIP
                              		  phones in a Cisco Unified CME system must be authenticated:

```
Router(config)# voice register global Router(config-register-global)# mode cme Router(config-register-global)# authenticate register
```

### Related Commands

Command

Description

credential load

Reloads a credential file into flash memory.

mode cme

Enables the mode for provisioning SIP phones in a Cisco
                                          						Unified CME system.

presence-enable

Allows incoming presence subscribe requests from SIP
                                          						trunks.

refer-ood enable

Enables OOD-R processing.

username (ephone)

Defines a username and password for SCCP phones.

username (voice register pool)

Defines a username and password for authenticating SIP
                                          						phones.

## b2bua

To configure a dial peer associated with an individual SIP phone in a
                              		  Cisco Unified Communications Manager Express (Cisco Unified CME) environment or
                              		  a group of phones in a Cisco Unified Session Initiation Protocol (SIP)
                              		  Survivable Remote Site Telephony (SRST) environment to point to Cisco Unity
                              		  Express, use the b2bua command in dial-peer configuration mode. To disable B2BUA call
                              		  flow on the dial peer, use the no form of this command.

b2bua

no b2bua

### Syntax Description

This command has no arguments or keywords.

### Command Default

Disabled

### Command Modes

Dial-peer configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4 and Cisco SIP SRST 3.4

This command was introduced.

### Usage Guidelines

Use the b2bua command to set the Cisco Unified CME source
                              		  address as the 302 redirect contact address for all calls forwarded to Cisco
                              		  Unity Express.

## Examples

The following example shows b2bua included in the configuration for
                              		  voice dial peer 1:

```
dial-peer voice 1 voip
 destination-pattern 4...
 session target ipv4:10.5.49.80
 session protocol sipv2
 dtmf-relay sip-notify
 b2bua
```

### Related Commands

Command

Description

allow-connections

Enables calls between SIP endpoints in a VoIP network.

dial-peer voice

Defines a dial peer and enters dial-peer configuration
                                          						mode.

mode (voice register global)

Enables the mode for provisioning SIP phones in a Cisco
                                          						Unified CME system.

show dial-peer voice

Displays information for dial peers.

source-address (voice register global)

Identifies the IP address and port through which SIP phones
                                          						communicate with a Cisco Unified CME router.

voice register global

Enters voice register global configuration mode in order to
                                          						set global parameters for all supported Cisco SIP phones in a Cisco Unified CME
                                          						or Cisco Unified SIP SRST environment.

## call-forward b2bua all

To enable call forwarding for a Session Initiation Protocol (SIP)
                              		  back-to-back user agent (B2BUA) so that all incoming calls are forwarded to
                              		  another extension, use the call forward b2bua all command in voice register dn or voice register pool configuration mode. To
                              		  disable call forwarding, use the no form of this command.

call-forward b2bua all directory-number

no call-forward b2bua all

### Syntax Description

directory number

Telephone number to which calls are forwarded. Represents a
                                          						fully qualified E.164 number. Maximum length of the telephone number is 32.

### Command Default

Disabled (no incoming call forwarding to another extension).

### Command Modes

Voice register dn configuration Voice register pool configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was introduced.

Cisco Unified SIP SRST 12.8

Introduced support for YANG models.

### Usage Guidelines

You can apply call forward to an individual SIP extension (voice
                              		  register dn) or to the SIP phone on which the extension appears (voice register
                              		  pool). Use this command in voice register pool configuration mode to enable
                              		  call forwarding for all extensions on a SIP phone. Use this command in voice
                              		  register dn configuration mode to enable call forwarding for an individual SIP
                              		  extension.

If information is configured in both voice register dn and voice
                              		  register pool mode, the information under voice register dn mode takes
                              		  precedence.

We recommend that you do not use this command with hunt groups. If
                              		  the command is used, consider removing the phone from any assigned hunt groups
                              		  unless you want to forward calls to all phones in the hunt group.

The call-forward b2bua all command takes precedence over the call-forward b2bua busy and call-forward b2bua noan commands.

## Examples

The following example shows how to forward all incoming calls to
                              		  extension 5001 on directory number 4, to extension 5005.

```
Router(config)# voice register dn 4 Router(config-register-dn)# number 5001 Router(config-register-dn)# call-forward b2bua all 5005
```

The following example shows how to forward all incoming calls for
                              		  extension 5001 on pool number 4, to extension 5005.

```
Router(config)# voice register pool 4 Router(config-register-pool)# number 5001 Router(config-register-pool)# call-forward b2bua all 5005
```

### Related Commands

Command

Description

call-forward b2bua busy

Enables call forwarding for a SIP B2BUA so that incoming
                                          						calls to a busy extension are forwarded to another extension.

call-forward b2bua mailbox

Controls the specific voice-mail box selected in a
                                          						voice-mail system at the end of a call forwarding exchange.

call-forward b2bua noan

Enables call forwarding for a SIP B2BUA so that incoming
                                          						calls to an extension that does not answer after a configured amount of time
                                          						are forwarded to another extension.

call-forward b2bua unreachable

Enables call forwarding for a SIP B2BUA so that incoming
                                          						calls to an extension that is not registered in Cisco Unified CME are forwarded
                                          						to another extension.

call-waiting (voice register pool)

Enables call waiting on a SIP phone.

number (voice register dn)

Associates an extension number with a voice register dn.

voice register dn

Enters voice register dn configuration mode to define an
                                          						extension for a SIP phone line.

voice register pool

Enters voice register pool configuration mode for SIP
                                          						phones.

## call-forward b2bua busy

To enable call forwarding for a Session Initiation Protocol (SIP)
                              		  back-to-back user agent (B2BUA) so that incoming calls to a busy extension are
                              		  forwarded to another extension, use the call forward b2bua busy command in voice register dn or voice register pool configuration mode. To
                              		  disable call forwarding, use the no form of this command.

call-forward b2bua busy directory-number

no call-forward b2bua busy

### Syntax Description

directory number

Telephone number to which calls are forwarded. Represents a
                                          						fully qualified E.164 number. Maximum length of the telephone number is 32.

### Command Default

Disabled (no incoming calls to a busy extension are forwarded).

### Command Modes

Voice register dn configuration Voice register pool configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was introduced.

### Usage Guidelines

The call-forward b2bua busy response is triggered when a call is sent
                              		  to a SIP phone using a VoIP dial peer and a busy response is received back from
                              		  the phone. This command functions only with phones that are registered to a
                              		  Cisco Unified SIP SRST or Cisco Unified CME router.

You can apply call forward to an individual SIP extension (voice
                              		  register dn) or to the SIP phone on which the extension appears (voice register
                              		  pool). Use this command in voice register pool configuration mode to enable
                              		  call forwarding for all extensions on a SIP phone. Use this command in voice
                              		  register dn configuration mode to enable call forwarding for a specific
                              		  extension. If information is configured in both voice register dn and voice
                              		  register pool mode, the information under voice register dn takes precedence.

We recommend that you do not use this command with hunt groups. If
                              		  the command is used, consider removing the phone from any assigned hunt groups,
                              		  unless you want to forward calls to all phones in the hunt group.

The call-forward b2bua all command takes precedence over the call-forward b2bua busy and call-forward b2bua noan commands.

Cisco Unified CME

Call forward busy can also get invoked if a number is unreachable but
                              		  the call forward b2bua unreachable command is not configured.

## Examples

The following example shows how to forward calls from extension 5001
                              		  in pool 4 to extension 5005 when extension 5001 is busy.

```
Router(config)# voice register pool 4 Router(config-register-pool)# number 5001 Router(config-register-pool)# call-forward b2bua busy 5005
```

### Related Commands

Command

Description

call-forward b2bua all

Enables call forwarding for a SIP B2BUA so that all
                                          						incoming calls are forwarded to another extension.

call-forward b2bua mailbox

Controls the specific voice-mail box selected in a
                                          						voice-mail system at the end of a call forwarding exchange.

call-forward b2bua noan

Enables call forwarding for a SIP B2BUA so that incoming
                                          						calls to an extension that does not answer after a configured amount of time
                                          						are forwarded to another extension.

call-forward b2bua unreachable

Enables call forwarding for a SIP B2BUA so that incoming
                                          						calls to an extension that is not registered in Cisco Unified CME are forwarded
                                          						to another extension.

call-waiting (voice register pool)

Enables call waiting on a SIP phone.

number (voice register dn)

Associates an extension number with a voice register dn.

voice register dn

Enters voice register dn configuration mode to define an
                                          						extension for a SIP phone line.

voice register pool

Enters voice register pool configuration mode for SIP
                                          						phones.

## call-forward b2bua mailbox

To control the specific voice-mail box selected in a voice-mail
                              		  system at the end of a call forwarding exchange, use the call forward b2bua mailbox command in voice register dn or voice register pool configuration mode. To
                              		  disable call forwarding, use the no form of this command.

call-forward b2bua mailbox directory-number

no call-forward b2bua mailbox

### Syntax Description

directory number

Telephone number to which calls are forwarded when the
                                          						forwarded destination is busy or does not answer. Represents a fully qualified
                                          						E.164 number. Maximum length of the telephone number is 32.

### Command Default

Disabled (no voice-mail box is selected for call forwarding).

### Command Modes

Voice register dn configuration Voice register pool configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was introduced.

### Usage Guidelines

Use this command to denote the voice-mail box to use at the end of a
                              		  chain of call forwards to busy or no answer destinations. It can be used to
                              		  forward calls to a voice-mail box that has a different number than the
                              		  forwarding extension. A sample of this would be in the case of a shared
                              		  voice-mail box, for instance one between a manager and her assistant. This
                              		  command functions only with phones that are registered to a Cisco Unified CME
                              		  or Cisco Unified SIP SRST router.

If information is configured in both voice register dn and voice
                              		  register pool mode, the information under voice register dn takes precedence.

It is recommended that you do not use the call-forward b2bua mailbox command with hunt groups. If the command
                              		  is used, consider removing the phone from any assigned hunt groups, unless you
                              		  want to forward calls to all phones in the hunt group.

This command is used in conjunction with the call-forward b2bua all , call-forward b2bua busy , and call-forward b2bua noan commands.

## Examples

The following example shows how to forward calls to extension 5005 if
                              		  an incoming call is forwarded to extension 5001 on pool number 4 and extension
                              		  5001 is busy or does not answer.

```
Router(config)# voice register pool 4 Router(config-register-pool)# number 5001 Router(config-register-pool)# call-forward b2bua mailbox 5005
```

### Related Commands

Command

Description

call-forward b2bua all

Enables call forwarding for a SIP B2BUA so that all
                                          						incoming calls are forwarded to another extension.

call-forward b2bua busy

Enables call forwarding for a SIP B2BUA so that incoming
                                          						calls to a busy extension are forwarded to another extension.

call-forward b2bua noan

Enables call forwarding for a SIP B2BUA so that incoming
                                          						calls to an extension that does not answer after a configured amount of time
                                          						are forwarded to another extension.

call-forward b2bua unreachable

Enables call forwarding for a SIP B2BUA so that incoming
                                          						calls to an extension that is not registered in Cisco Unified CME are forwarded
                                          						to another extension.

call-waiting (voice register pool)

Enables call waiting on a SIP phone.

number (voice register dn)

Associates an extension number with a voice register dn.

voice register dn

Enters voice register dn configuration mode to define an
                                          						extension for a SIP phone line.

voice register pool

Enters voice register pool configuration mode for SIP
                                          						phones.

## call-forward b2bua noan

To enable call forwarding for a Session Initiation Protocol (SIP)
                              		  back-to-back user agent (B2BUA) so that incoming calls to an extension that
                              		  does not answer after a configured amount of time are forwarded to another
                              		  extension, use the call forward b2bua noan command in voice register dn or voice register pool configuration mode. To
                              		  disable call forwarding, use the no form of this command.

call-forward b2bua noan directory-number timeout seconds

no call-forward b2bua noan

### Syntax Description

directory number

Telephone number to which calls are forwarded. Represents a
                                          						fully qualified E.164 number. Maximum length of the telephone number is 32.

timeout seconds

Number of seconds that a call can ring with no answer
                                          						before the call is forwarded to another extension. Range is 3 to 60000. Default
                                          						is 20.

### Command Default

Disabled (no incoming calls to an extension that does not answer are
                              		  forwarded).

### Command Modes

Voice register dn configuration Voice register pool configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was introduced.

### Usage Guidelines

This command functions only with phones that are registered to a
                              		  Cisco Unified SIP SRST or Cisco Unified CME router. You can apply call forward
                              		  to an individual SIP extension (voice register dn) or to the SIP phone on which
                              		  the extension appears (voice register pool). Use this command in voice register
                              		  pool configuration mode to enable call forwarding for all extensions on a SIP
                              		  phone. Use this command in voice register dn configuration mode to enable call
                              		  forwarding for a specific extension.

If information is configured in both voice register dn and voice
                              		  register pool mode, the information under voice register dn takes precedence.

We recommend that you do not use this command with hunt groups. If
                              		  the command is used, consider removing the phone from any assigned hunt groups,
                              		  unless you want to forward calls to all phones in the hunt group.

The call-forward b2bua all command takes precedence over the call-forward b2bua busy and call-forward b2bua noan commands.

## Examples

The following example shows how to forward calls to extension 5005
                              		  when extension 5001 on pool number 4 is unanswered. The timeout before the call
                              		  is forwarded to extension 5005 is 10 seconds.

```
Router(config)# voice register pool 4 Router(config-register-pool)# number 5001 Router(config-register-pool)# call-forward b2bua noan 5005 timeout 10
```

### Related Commands

Command

Description

call-forward b2bua all

Enables call forwarding for a SIP B2BUA so that all
                                          						incoming calls are forwarded to another extension.

call-forward b2bua busy

Enables call forwarding for a SIP B2BUA so that incoming
                                          						calls to a busy extension are forwarded to another extension.

call-forward b2bua mailbox

Controls the specific voice-mail box selected in a
                                          						voice-mail system at the end of a call forwarding exchange.

call-forward b2bua unreachable

Enables call forwarding for a SIP B2BUA so that incoming
                                          						calls to an extension that is not registered in Cisco Unified CME are forwarded
                                          						to another extension.

call-waiting (voice register pool)

Enables call waiting on a SIP phone.

number (voice register dn)

Associates an extension number with a voice register dn.

voice register dn

Enters voice register dn configuration mode to define an
                                          						extension for a SIP phone line.

voice register pool

Enters voice register pool configuration mode for SIP
                                          						phones.

## call-forward busy (call-manager-fallback)

To configure call forwarding to another number when a Cisco IP phone
                              		  is busy, use the call-forward busy command in call-manager-fallback
                              		  configuration mode. To disable call forwarding, use the no form of this command.

call-forward busy directory-number

no call-forward busy [directory-number]

### Syntax Description

directory-number

Directory number representing a fully qualified E.164
                                          						number. This number can contain “.” wildcard characters that correspond to the
                                          						right-justified digits in the directory number extension.

### Command Default

No default behavior or values.

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(2)XT

Cisco Unified SRST 2.0

This command was introduced on the following platforms:
                                          						Cisco 1750, Cisco 1751, Cisco 2600 series and Cisco 3600 series multiservice
                                          						routers, and Cisco IAD2420 series IADs.

12.2(8)T

Cisco Unified SRST 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers.

12.2(8)T1

Cisco Unified SRST 2.0

This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers.

12.2(11)T

Cisco Unified SRST 2.1

This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers.

### Usage Guidelines

The call-forward busy command configures call forwarding to another
                              		  number when a Cisco IP phone is busy. The call forwarding mechanism is applied
                              		  globally to all phones that register during fallback.

## Examples

The following example forwards calls to extension number 5005 when an
                              		  incoming call reaches a busy IP phone extension number:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# call-forward busy 5005
```

The following example transforms an extension number for call
                              		  forwarding when the extension number is busy. The call-forward busy command has an argument of 50.., which
                              		  prepends the digits 50 to the last two digits of the called extension. The
                              		  resulting extension is the number to which incoming calls are forwarded when
                              		  the original extension number is busy. For instance, an incoming call to the
                              		  busy extension 6002 will be forwarded to extension 5002, and an incoming call
                              		  to the busy extension 3442 will be forwarded to extension 5042.

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# call-forward busy 50..
```

### Related Commands

Command

Description

call-forward noan

Configures call forwarding to another number when no answer
                                          						is received from the Cisco IP phone.

call-manager-fallback

Enables Cisco Unified SRST feature support and enters
                                          						call-manager-fallback configuration mode.

## call-forward noan (call-manager-fallback)

To configure call forwarding to another number when no answer is
                              		  received from a Cisco IP phone, use the call-forward noan command in call-manager-fallback configuration mode. To disable
                              		  call forwarding, use the no form of this command.

call-forward noan directory-number timeout seconds

no call-forward noan [directory-number]

### Syntax Description

directory-number

Directory number representing a fully qualified E.164
                                          						number or a local extension number. This number can contain “.” wildcard
                                          						characters that correspond to the right-justified digits in the directory
                                          						number extension.

timeout

Sets the ringing no answer timeout duration, which is the
                                          						waiting time (in seconds) before the call is forwarded to another phone.

seconds

Time (in seconds) before call forwarding starts. The range
                                          						is from 3 to 60000.

### Command Default

No default behavior or values.

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(2)XT

Cisco SRST 2.0

This command was introduced on the following platforms:
                                          						Cisco 1750, Cisco 1751, Cisco 2600 series and Cisco 3600 series multiservice
                                          						routers, and Cisco IAD2420 series IADs.

12.2(8)T

Cisco SRST 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers.

12.2(8)T1

Cisco SRST 2.0

This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers.

12.2(11)T

Cisco SRST 2.1

This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers.

### Usage Guidelines

The call-forward noan command configures call forwarding to another
                              		  number when no answer is received from a Cisco IP phone. The call-forwarding
                              		  mechanism is applied globally to all phones that register during fallback. The timeout keyword sets the waiting time before
                              		  the call is forwarded to another phone. The time is set in seconds. The range
                              		  is from 3 to 60,000 seconds.

## Examples

The following example shows how to set call forwarding of incoming
                              		  calls to directory number 5005 when line 1, directory number 5001, does not
                              		  answer. The timeout period before the call is forwarded to directory number
                              		  5005 is set for 10 seconds.

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# call-forward noan 5005 timeout 10
```

The following example shows how to set call forwarding of incoming
                              		  calls to an available extension in the 50xx bank of extensions when line 1,
                              		  directory number 5001, does not answer. The timeout period before the call is forwarded
                              		  to directory number 5005 is set for 10 seconds.

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# call-forward noan 50.. timeout 10
```

### Related Commands

Command

Description

call-forward busy

Configures call forwarding to another number when a Cisco
                                          						IP phone is busy.

call-manager-fallback

Enables Cisco Unified SRST feature support and enters
                                          						call-manager-fallback configuration mode.

## call-forward pattern (call-manager-fallback)

To specify a pattern for calling-party numbers that are able to
                              		  support the ITU-T H.450.3 standard for call forwarding, use the call-forward pattern command in call-manager-fallback configuration mode. To remove
                              		  the pattern, use the no form of this command.

call-forward pattern pattern

no call-forward pattern pattern

### Syntax Description

pattern

String that consists of one or more digits and wildcard
                                          						markers or dots (.) to define a specific pattern. Calling parties that match a
                                          						defined pattern use the H.450.3 standard if they are forwarded. A pattern of .T
                                          						specifies the H.450.3 forwarding standard for all incoming calls.

### Command Default

No default behavior or values.

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco SRST 3.0

This command was introduced.

12.3(4)T

Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

The pattern match in this command is against the phone number of the
                              		  calling party. When a directory number has forwarded its calls and an incoming
                              		  call is received for that number, the SRST router sends an H.450.3 response
                              		  back to the original calling party to request that the call be placed again
                              		  using the forward-to destination.

Calling numbers that do not match the patterns defined with this
                              		  command are forwarded using Cisco-proprietary call forwarding for backward
                              		  compatibility.

## Examples

The following example specifies that all 4-digit directory numbers
                              		  beginning with 4 should use the H.450.3 standard whenever they are forwarded:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# call-forward pattern 4...
```

The following example forwards all calls using the H.450.3 standard:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# call-forward pattern .T
```

### Related Commands

Command

Description

call-manager-fallback

Enables Cisco Unified SRST feature support and enters
                                          						call-manager-fallback configuration mode.

## call-manager-fallback

To enable Cisco Unified SRST support and enter call-manager-fallback
                              		  configuration mode, use the call-manager-fallback command in global
                              		  configuration mode. To disable Cisco Unified SRST support, use the no form of this command.

call-manager-fallback

no call-manager-fallback

### Syntax Description

This command has no arguments or keywords.

### Command Default

No default behavior or values.

### Command Modes

Global configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.1(5)YD

Cisco SRST 1.0

This command was introduced on the following platforms:
                                          						Cisco 2600 series and Cisco 3600 series multiservice routers, and Cisco IAD2420
                                          						series IADs.

12.2(2)XT

Cisco SRST 2.0

This command was implemented on Cisco 1750 and Cisco 1751
                                          						multiservice routers.

12.2(8)T

Cisco SRST 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers.

12.2(8)T1

Cisco SRST 2.0

This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers.

12.2(11)T

Cisco SRST 2.1

This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers.

## Examples

The following example shows how to enter call-manager-fallback
                              		  configuration mode:

```
Router(config)# call-manager-fallback
```

The resulting router prompt is Router(config-cm-fallback)# .

### Related Commands

Command

Description

access-code

Configures trunk access codes for each type of line so that
                                          						the Cisco IP phones can access the trunk lines.

alias

Provides a mechanism for servicing calls to telephone
                                          						numbers that are unavailable during Cisco Unified Communications Manager
                                          						fallback.

call-forward busy

Configures call forwarding to another number when a Cisco
                                          						IP phone is busy.

call-forward noan

Configures call forwarding to another number when no answer
                                          						is received from a Cisco IP phone.

cor

Configures COR on the dial peers associated with directory
                                          						numbers.

default-destination

Assigns a default destination number for incoming telephone
                                          						calls.

dialplan-pattern

Creates a global prefix that can be used to expand the
                                          						abbreviated extension numbers into fully qualified E.164 numbers.

huntstop

Sets huntstop for the dial peers associated with Cisco IP
                                          						phone lines.

ip source-address

Enables the router to receive messages from Cisco IP phones
                                          						through the specified IP addresses and ports.

keepalive

Configures the time interval between sending keepalive
                                          						messages to the router used by Cisco IP phones.

max-dn

Sets the maximum number of directory numbers or virtual
                                          						voice ports that can be supported by the router.

max-ephone

Configures the maximum number of Cisco IP phones that can
                                          						be supported by the router.

reset

Resets Cisco IP phones.

timeouts interdigit

Configures the interdigit timeout value for all Cisco IP
                                          						phones attached to the router.

transfer-pattern

Allows transfer of telephone calls by Cisco IP phones to
                                          						other phone numbers.

translate

Applies a translation rule to modify the phone number
                                          						dialed by any Cisco IP phone user during Cisco Unified Communications Manager
                                          						fallback.

voicemail

Configures the telephone number that is speed-dialed when
                                          						the message button on a Cisco IP phone is pressed.

## clear voice moh-group statistics

To clear the display of MOH subsystem statistics information and
                              		  reset the packet counters, use the clear voice moh-group statistics command in privileged EXEC mode.

clear voice moh-group statistics

### Syntax Description

This command has no arguments or keywords

### Command Modes

Privileged EXEC (#)

## Command History

Cisco IOS Release

yCisco Product

Modification

15.0(1)XA

Cisco Unified CME 8.0 Cisco Unified SRST 8.0

This command was introduced.

15.1(1)T

Cisco Unified CME 8.0 Cisco Unified SRST 8.0

This command was integrated into Cisco IOS Release
                                          						15.1(1)T.

### Usage Guidelines

Use this command to clear the display of MOH subsystem statistics
                              		  information displayed by the show voice moh-group statistics command.

We recommend that the clear voice moh-group statistics should be used
                              		  once every two years to reset the packet counters. Each packet counter is of 32
                              		  bit size limit and the largest count a packet counter can hold is 4294967296
                              		  intervals. This means that with 20 milliseconds packet interval (for G.711),
                              		  the counters will restart from 0 any time after 2.72 years (2 years and 8
                              		  months).

## Examples

```
Router# clear voice moh-group statistics 
All moh group stats are cleared
```

### Related Commands

Command

Description

show voice moh-group statistics

Displays the MOH subsystem statistics information

show voice moh-group

Displays the MOH groups configured

## codec g722-64k

To specify that the G.722 codec should be used for Cisco Unified
                              		  Survivable Remote Site Telephony (SRST) mode, use the codec g722-64k command in call-manager-fallback
                              		  configuration mode. To disable this command and restore G.711 as the supported
                              		  codec for SRST mode, use the no form of this command.

codec g722-64k

no codec g722-64k

### Syntax Description

This command has no arguments or keywords.

### Command Default

If the codec g722-64k command is not enabled, the G.711 codec
                              		  is the default for SRST mode.

### Command Modes

Call-manager-fallback configuration (config-cm-fallback)

## Command History

Release

Cisco Products

Modification

15.0(1)M

Cisco Unified SRST 8.0 Cisco Unified SIP SRST 8.0

This command was introduced.

### Usage Guidelines

The G.722 codec should be used for the SRST codec provided the phone
                              		  supports that codec capability. For phones that do not support G.722 codec, the
                              		  phones will fall back to the G.711 codec.

## Examples

The following example shows how to enable support for the G.722 codec
                              		  for SRST mode:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# codec g722-64k
```

### Related Commands

Command

Description

call-manager-fallback

Enters call-manager-fallback configuration mode.

## conference
                        	 max-length

To allow Cisco
                              		  Unified SRST conferencing only if the number of dialed digits are within the
                              		  maximum length limit, use the conference
                                    				max-length command. To remove the configuration, use the no form of
                              		  this command.

conference max-length <value>

no conference max-length

## Syntax Description

Maximum
                                       					 number of digits that can be dialed. The range is from 3 to 16.

### Command Default

No default value
                              		  is defined for conferencing.

### Command Modes

voice register pool (config-register-pool)

## Command History

This
                                       					 command was introduced.

### Usage Guidelines

Use the conference
                                    				max-length command to configure, the Cisco Unified SRST to allow
                              		  conferencing, only if the dialed digits are within the maximum length limit.

## Examples

The following
                              		  example shows how to configure the maximum number of digits that can be dialed
                              		  to make a conference call:

```
Router(config)# voice register pool 1 Router(config-register-pool)# conference max-length 4
```

### Related Commands

Command

Description

conference-pattern blocked

Blocks
                                          						extensions on an ephone or voice register pool from making conference calls to
                                          						patterns defined in the transfer-pattern command.

conference
                                                							 transfer-pattern

Allows
                                          						to conference the transferred calls to phones within the local Cisco Unified
                                          						SRST network.

transfer max-length

Allows
                                          						the transfer of calls to phones within the local Cisco Unified SRST network.

transfer-pattern
                                                							 (call-manager fallback)

Allows
                                          						the transfer of calls to phones outside the local Cisco Unified SRST network.

## conference-pattern
                        	 blocked

To prevent
                              		  extensions on an ephone or a voice register pool from initiating a conference
                              		  to external numbers, use the conference-pattern
                                    				blocked command. Note that the conference-pattern
                                    				blocked command does not impact call transfer functions. To
                              		  remove the configuration, use the no form of
                              		  this command.

conference-pattern blocked

no conference-pattern blocked

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

No default
                              		  behavior or values.

### Command Modes

Ephone configuration (config-ephone)

Voice register pool configuration (config-register-pool)

## Command History

This
                                       					 command was introduced.

### Usage Guidelines

Use the conference-pattern
                                    				blocked command to prevent specific extensions from making
                              		  conference calls to patterns generally allowed through the transfer-pattern command.

## Examples

This example shows
                              		  how this command prevents extensions from making conference calls to patterns
                              		  using the transfer-pattern command.

```
Router(config)# voice regsiter pool 1 Router(config-registetr-pool)# conference-pattern blocked
```

### Related Commands

Command

Description

conference max-length

Allows
                                          						the conferences only if the dialed digits are within the maximum length limit.

conference
                                                							 transfer-pattern

Allows
                                          						to conference the transferred calls to phones within the local Cisco Unified
                                          						SRST network.

transfer-pattern blocked

Block
                                          						extensions on an ephone or voice register pool from making transferring calls
                                          						to patterns defined in the conference pattern-blocked command.

transfer-pattern
                                                							 (call-manager fallback)

Allows
                                          						the transfer of calls to phones outside the local Cisco Unified SRST network.

## conference transfer-pattern (call-manager-fallback)

To apply transfer patterns to a conference call using conference
                              		  softkeys or feature buttons in Cisco Unified SRST, use the conference transfer-pattern command in call-manager-fallback
                              		  configuration mode. To disable the transfer patterns, use the no form of this command.

conference transfer-pattern

no conference transfer-pattern

### Syntax Description

This command has no arguments or keywords.

### Command Default

Transfer patterns do not apply to conference calls.

### Command Modes

Call-manager-fallback configuration (config-cm-fallback)

## Command History

Release

Modification

15.3(2)T

This command was introduced.

### Usage Guidelines

There is no check for the conference numbers for call conferencing.
                              		  To apply transfer patterns for call conferencing, use the conference transfer-pattern command.

When both the transfer-pattern and conference transfer-pattern commands are configured and
                              		  dialed digits match the configured transfer pattern, conference calls are
                              		  allowed. However, when the dialed digits do not match any of the configured
                              		  transfer pattern, the conference call is blocked.

## Examples

The following example applies transfer patterns to conference calls:

```
Router(config)# call-manager-fallback
Router(config-cm-fallback)# transfer-pattern 1234
Router(config-cm-fallback)# conference transfer-pattern
```

### Related Commands

Command

Description

call-manager-fallback

Enters call-manager-fallback configuration mode to enable
                                          						Cisco Unified SRST support.

transfer-pattern

Allows Cisco Unified IP phones to transfer telephone calls
                                          						from callers outside the local IP network to another Cisco Unified IP phone.

## cor
                        	 (call-manager-fallback)

To configure a
                              		  class of restriction (COR) on the dial peers associated with directory numbers,
                              		  use the cor command in call-manager-fallback configuration mode. To disable
                              		  a COR associated with directory numbers, use the no form of
                              		  this command.

cor { incoming | outgoing } cor-list-name [ cor-list-number starting-number-ending-number | default ]

no cor cor-list-name cor-list-number

### Syntax Description

incoming

COR
                                          						list to be used by incoming dial peers.

outgoing

COR
                                          						list to be used by outgoing dial peers.

cor-list-name

COR
                                          						list name.

cor-list-number

COR
                                          						list identifier. The maximum number of COR lists that can be created is 20,
                                          						comprised of incoming or outgoing dial peers. The first six COR lists are
                                          						applied to a range of directory numbers. The directory numbers that do not have
                                          						a COR configuration are assigned to the default COR list, provided that a
                                          						default COR list has been defined.

starting-number - ending-number

Directory number range; for example, 2000 - 2025.

default

Instructs the COR list to assume behavior according to a predefined default COR
                                          						list.

### Command Default

No default
                              		  behavior or values.

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.2(2)XT

Cisco
                                          						SRST 2.0

This
                                          						command was introduced on the following platforms: Cisco 1750, Cisco 1751,
                                          						Cisco 2600 series and Cisco 3600 series multiservice routers, and Cisco IAD2420
                                          						series IADs.

12.2(8)T

Cisco
                                          						SRST 2.0

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T and implemented on the
                                          						Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers.

12.2(8)T1

Cisco
                                          						SRST 2.0

This
                                          						command was implemented on the Cisco 2600-XM and Cisco 2691 routers.

12.2(11)T

Cisco
                                          						SRST 2.01

This
                                          						command was integrated into Cisco IOS Release 12.2(11)T and implemented on the
                                          						Cisco 1760 routers. The default keyword was added.

12.3(11)T

Cisco
                                          						SRST 3.2

The
                                          						maximum number of COR lists that can be created was increased to 20.

### Usage Guidelines

The cor command
                              		  sets the dial-peer COR parameter for dial peers associated with the directory
                              		  numbers created during Cisco Unified Communications Manager fallback. A
                              		  list-based mechanism is provided to assign COR to specific sets of directory
                              		  numbers during Cisco Unified Communications Manager fallback. The COR
                              		  functionality provides the ability to deny certain call attempts on the basis
                              		  of the incoming and outgoing class of restrictions provisioned on the dial
                              		  peers. This functionality provides flexibility in network design, allows users
                              		  to block calls (for example, calls to 900 numbers), and applies different
                              		  restrictions to call attempts from different originators.

COR is used to
                              		  specify which incoming dial peer can use which outgoing dial peer to make a
                              		  call. Each dial peer can be provisioned with an incoming and an outgoing COR
                              		  list.

A default COR
                              		  is assigned to the directory numbers that do not match any COR list number or
                              		  number range. The assigned COR is invoked for the dial peers automatically
                              		  created for each directory number during Cisco Unified Communications Manager
                              		  fallback registration.

You can have up
                              		  to 20 COR lists for each incoming and outgoing call. A default COR is assigned
                              		  to directory numbers that do not match any COR list numbers or number ranges.
                              		  An assigned COR is invoked for the dial peers and created for each directory
                              		  number automatically during Communications Manager fallback registration.

If a COR is
                              		  applied on an incoming dial peer (for incoming calls) and it is a superset or
                              		  is equal to the COR applied to the outgoing dial peer (for outgoing calls), the
                              		  call will go through. Voice ports determine whether a call is considered to be
                              		  incoming or outgoing. If you hook up a phone to an FXS port on a Cisco Unified
                              		  SRST router and try to make a call from that phone, the call will be considered
                              		  an incoming call to the router and voice port. If you make a call to the FXS
                              		  phone, the call will be considered an outgoing call.

By default, an
                              		  incoming call leg has the highest COR priority. The outgoing COR list has the
                              		  lowest. If there is no COR configuration for incoming calls on a dial peer, you
                              		  can make a call from a phone attached to the dial peer, so that the call will
                              		  go out of any dial peer regardless of the COR configuration on that dial peer.
                              		  Incoming and outgoing lists are shown in Table 1 .

COR
                                          					 List on Incoming Dial Peer

COR
                                          					 List on Outgoing Dial Peer

Result

No COR

No COR

Call
                                          					 will succeed.

No COR

COR
                                          					 list applied for outgoing calls

Call
                                          					 will succeed. By default, the incoming dial peer has the highest COR priority
                                          					 when no COR is applied. If you apply no COR for an incoming call leg to a dial
                                          					 peer, the dial peer can make a call out of any other dial peer regardless of
                                          					 the COR configuration on the outgoing dial peer.

COR
                                          					 list applied for incoming calls

No COR

Call
                                          					 will succeed. By default, the outgoing dial peer has the lowest priority.
                                          					 Because there are some COR configurations for incoming calls on the incoming or
                                          					 originating dial peer, it is a superset of the outgoing call’s COR
                                          					 configuration for the outgoing or terminating dial peer.

COR
                                          					 list applied for incoming calls (superset of COR list applied for outgoing
                                          					 calls on the outgoing dial peer)

COR
                                          					 list applied for outgoing calls (subsets of COR list applied for incoming calls
                                          					 on the incoming dial peer)

Call
                                          					 will succeed. The COR list for incoming calls on the incoming dial peer is a
                                          					 superset of the COR list for outgoing calls on the outgoing dial peer.

COR
                                          					 list applied for incoming calls (subset of COR list applied for outgoing calls
                                          					 on the outgoing dial peer)

COR
                                          					 list applied for outgoing calls (supersets of COR list applied for incoming
                                          					 calls on the incoming dial peer)

Call
                                          					 will not succeed. The COR list for incoming calls on the incoming dial peer is
                                          					 not a superset of the COR list for outgoing calls on the outgoing dial peer.

## Examples

The following
                              		  example shows how to set the dial-peer COR parameter for incoming calls to
                              		  Cisco IP phone dial peers and directory numbers created during Cisco Unified
                              		  Communications Manager fallback:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# cor incoming LockforPhoneC 1 5002 – 5010
```

The following
                              		  example shows how to set the dial-peer COR parameter for outgoing calls to
                              		  Cisco IP phone dial peers and directory numbers created during fallback:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# cor outgoing LockforPhoneC 1 5010 – 5020
```

The following
                              		  example shows how to set the dial-peer COR parameter for incoming calls to
                              		  Cisco IP phone dial peers and directory numbers in the default COR list:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# cor incoming LockforPhoneC default
```

The following
                              		  example shows how sub- and super-COR sets are created. First, a custom
                              		  dial-peer COR is created with names declared under it:

```
Router(config)# dial-peer cor custom Router(config-dp-cor)# name 911 Router(config-dp-cor)# name 1800 Router(config-dp-cor)# name 1900 Router(config-dp-cor)# name local_call
```

In the
                              		  following configuration examples, COR lists are created and applied to the dial
                              		  peer.

```
Router(config)# dial-peer cor list call911 Router(config-dp-corlist)# member 911 Router(config)# dial-peer cor list call1800 Router(config-dp-corlist)# member 1800 Router(config)# dial-peer cor list call1900 Router(config-dp-corlist)# member 1900 Router(config)# dial-peer cor list calllocal Router(config-dp-corlist)# member local_call Router(config)# dial-peer cor list engineering Router(config-dp-corlist)# member 911 Router(config-dp-corlist)# member local_call Router(config)# dial-peer cor list manager Router(config-dp-corlist)# member 911 Router(config-dp-corlist)# member 1800 Router(config-dp-corlist)# member 1900 Router(config-dp-corlist)# member local_call Router(config)# dial-peer cor list hr Router(config-dp-corlist)# member 911 Router(config-dp-corlist)# member 1800 Router(config-dp-corlist)# member local_call
```

In the example
                              		  below, five dial peers are configured for destination numbers 734....,
                              		  1800......., 1900......., 316...., and 911. A COR list is applied to each of
                              		  the dial peers.

```
Router(config)# dial-peer voice 1 voip Router(config-dial-peer)# destination pattern 734.... Router(config-dial-peer)# session target ipv4:1.1.1.1 Router(config-dial-peer)# cor outgoing calllocal Router(config)# dial-peer voice 2 voip Router(config-dial-peer)# destination pattern 1800....... Router(config-dial-peer)# session target ipv4:1.1.1.1 Router(config-dial-peer)# cor outgoing call1800 Router(config)# dial-peer voice 3 pots Router(config-dial-peer)# destination pattern 1900....... Router(config-dial-peer)# port 1/0/0 Router(config-dial-peer)# cor outgoing call1900 Router(config)# dial-peer voice 4 pots Router(config-dial-peer)# destination pattern 911 Router(config-dial-peer)# port 1/0/1 Router(config-dial-peer)# cor outgoing call911 Router(config)# dial-peer voice 5 pots Router(config-dial-peer)# destination pattern 316.... Router(config-dial-peer)# port 1/1/0 ! No cor is applied.
```

Finally, the
                              		  COR list is applied to the individual phone numbers.

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# max-conferences 8 Router(config-cm-fallback)# cor incoming engineering 1 1001 - 1001 Router(config-cm-fallback)# cor incoming hr 2 1002 - 1002 Router(config-cm-fallback)# cor incoming manager 3 1003 - 1008
```

The example
                              		  configuration allows for the following:

- Extension 1001 to call
                                 			 408... numbers, 911 and 316....

- Extension 1002 to call
                                 			 408..., 1800 numbers, 911 and 316....

- Extension 1003 through
                                 			 1008 to call all of the possible Cisco Unified SRST router numbers

- All extensions to call
                                 			 316....

### Related Commands

Command

Description

call-manager-fallback

Enables Cisco Unified SRST feature support and enters call-manager-fallback
                                          						configuration mode.

corlist-incoming

Specifies the COR list to be used when a specified dial peer acts as the
                                          						incoming dial peer.

corlist-outgoing

Specifies the COR list to be used by outgoing dial peers.

dial-peer cor list

Defines a COR list name.

## cor (voice register pool)

To configure a class of restriction (COR) on the VoIP dial peers
                              		  associated with directory numbers, use the cor command in voice register pool configuration mode. To disable a COR
                              		  associated with directory numbers, use the no form of this command.

cor { incoming | outgoing } cor-list-name { cor-list-number starting-number [-
                                 					 ending-number] | default }

no cor { incoming | outgoing } cor-list-name cor-list-name { cor-list-number starting-number [-
                                 					 ending-number] | default }

### Syntax Description

incoming

COR list to be used by incoming dial peers.

outgoing

COR list to be used by outgoing dial peers.

cor-list-name

COR list name.

cor-list-number

COR list identifier.

starting-number

Start of a directory number range, if an ending number is
                                          						included. Can also be a standalone number.

-

(Optional) Indicator that a full range is configured.

ending-number

(Optional) End of a directory number range.

default

Instructs the COR list to assume behavior according to a
                                          						predefined default COR list.

### Command Default

None

### Command Modes

Voice register pool configuration

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

This command was added to Cisco Communications Manager
                                          						Express (Cisco CME).

### Usage Guidelines

The cor command sets the dial-peer COR parameter
                              		  for dynamically created VoIP dial peers. A list-based mechanism assigns COR
                              		  parameters to specific set of number ranges. The COR functionality provides the
                              		  ability to deny certain call attempts on the basis of the incoming and outgoing
                              		  class of restrictions provisioned on the dial peers. This functionality
                              		  provides flexibility in network design, allows users to block calls (for
                              		  example, calls to 900 numbers), and applies different restrictions to call
                              		  attempts from different originators.

COR specifies which incoming dial peer can use which outgoing dial
                              		  peer to make a call. Each dial peer can be provisioned with an incoming and an
                              		  outgoing COR list.

A default COR is assigned to the directory numbers that do not match
                              		  any COR list number or number range. During Cisco Unified Session Initiation
                              		  Protocol (SIP) Survivable Remote Site Telephony (SRST) registration, a dial
                              		  peer is created and that dial peer includes a default COR value. The cor command allows you to change the automatically selected
                              		  default.

In dial-peer configuration mode, build your COR list and add members.
                              		  Then in voice register pool configuration mode, use the cor command to apply the name of the dial-peer COR list.

You can have up to four COR lists for the Cisco Unified SIP SRST
                              		  configuration, comprised of incoming or outgoing dial peers. The first four COR
                              		  lists are applied to a range of phone numbers. The phone numbers that do not
                              		  have a COR list configuration are assigned to the default COR list, providing
                              		  that a default COR list has been defined.

## Examples

The following is sample output from the show running-config command:

```
..
voice register pool 1
 id mac 0030.94C2.A22A
 preference 5
 cor incoming call91 1 91011
 translate-outgoing called 1
 proxy 10.2.161.187 preference 1 monitor probe icmp-ping
 alias 1 94... to 91011 preference 8
 voice-class codec 1
.
.
.
dial-peer cor custom
 name 95
 name 94
 name 91
!
dial-peer cor list call91
 member 91
!
dial-peer voice 91500 pots
 corlist incoming call91
 corlist outgoing call91
 destination-pattern 91500
 port 1/0/0
.
.
.
```

### Related Commands

Command

Description

dial-peer cor custom

Specifies that named CORs apply to dial peers.

dial-peer cor list

Defines a COR list name.

id (voice register pool)

Explicitly identifies a locally available individual Cisco
                                          						SIP IP phone, or when running Cisco Unified SIP SRST, set of Cisco SIP IP
                                          						phones.

member (dial-peer cor list)

Adds a member to a dial-peer COR list.

name (dial-peer custom cor)

Provides a name for a custom COR.

show dial-peer voice

Displays information for voice dial peers.

voice register pool

Enables Cisco Unified SIP SRST voice register pool
                                          						configuration commands.

## credentials

To enter
                              		  credentials configuration mode to configure a certificate for a Cisco Unified
                              		  CME CTL provider or for Cisco Unified SRST router communication to Cisco
                              		  Unified Communications Manager, use the credentials command in global configuration mode. To set all commands in
                              		  credentials configuration mode to the default of nonsecure, use the no form of
                              		  this command.

credentials

no credentials

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

Credentials are
                              		  not provided.

### Command Modes

Global configuration

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.3(14)T

Cisco
                                          						SRST 3.3

This
                                          						command was introduced for Cisco Unified SRST.

12.4(4)XC

Cisco
                                          						Unified CME 4.0

This
                                          						command was introduced for Cisco Unified CME.

Cisco
                                          						IOS XE Fuji Release, 16.7.1

Unified SRST 12.1

This
                                          						command was introduced for Unified SRST support on Cisco 4000 Series Integrated
                                          						Services Router.

Cisco IOS XE Dublin
                                                17.10.1a

Cisco Unified SRST 14.3

Introduced support for YANG models.

### Usage Guidelines

This command is
                              		  used to configure credentials service for Cisco Unified CME and Cisco Unified
                              		  SRST.

Cisco Unified CME

This command is
                              		  used with Cisco Unified CME phone authentication to configure a CTL provider on
                              		  each Cisco Unified CME router on which the CTL client is not running. That is,
                              		  if there is a primary and a secondary Cisco Unified CME router and the CTL
                              		  client is running on the primary router, a CTL provider must be configured on
                              		  the secondary router, and vice versa. If the CTL client is running on a router
                              		  that is not a Cisco Unified CME router, CTL providers must be configured on all
                              		  Cisco Unified CME routers.

Credentials
                              		  service for Cisco Unified CME runs on default port 2444.

Cisco Unified SRST

The credential
                              		  server provides certificates to any device that requests a certificate. The
                              		  credentials server does not request any data from a client; thus no
                              		  authentication is necessary. When the client, Cisco Unified Communications
                              		  Manager, requests a certificate, the credentials server provides the
                              		  certificate. Cisco Unified Communications Manager exports the certificate to
                              		  the phone, and the Cisco Unified IP phone holds the SRST router certificate in
                              		  its configuration file. The device certificate for secure SRST routers is
                              		  placed in the configuration file of the Cisco Unified IP phone because the
                              		  entry limit in the certificate trust list (CTL) of Cisco Unified Communications
                              		  Manager is 32.

Credentials
                              		  service for SRST runs on default port 2445. Cisco Unified Communications
                              		  Manager connects to port 2445 on the secure SRST router and retrieves the
                              		  secure SRST device certificate during the TLS handshake.

Activate this
                              		  command on all SRST routers.

Caution

For security
                                          			 reasons, credentials service should be deactivated on all SRST routers after
                                          			 provisioning to Cisco Unified Communications Manager is completed.

## Examples

## Examples

The following
                              		  example configures a CTL provider on the Cisco Unified CME router with the IP
                              		  address 172.19.245.1. CTL providers must be configured on all Cisco Unified CME
                              		  routers on which the CTL client is not running.

```
Router(config)# credentials Router(config-credentials)# ip source-address 172.19.245.1 port 2444 Router(config-credentials)# trustpoint cmeca Router(config-credentials)# ctl-service admin user4 secret 0 c89L8o
```

## Examples

The following
                              		  example enters credentials configuration mode and sets the IP source address
                              		  and the trustpoint:

```
Router(config)# credentials Router(config-credentials)# ip source-address 10.6.21.4 port 2445 Router(config-credentials)# trustpoint srstca
```

### Related Commands

Command

Description

ctl-service admin

Specifies a user name and password to authenticate the CTL client during the
                                          						CTL protocol.

debug credentials

Sets
                                          						debugging on the credentials service that runs between a Cisco Unified CME CTL
                                          						provider the CTL client or between an SRST router and Cisco Unified
                                          						Communications Manager.

ip source-address (credentials)

Enables the Cisco Unified CME or SRST router to receive messages through the
                                          						specified IP address and port.

show credentials

Displays the credentials settings on a Cisco Unified CME or SRST router.

trustpoint (credentials)

Specifies the name of the trustpoint to be associated with a Cisco Unified CME
                                          						CTL provider certificate or with an SRST router certificate.

## date-format (call-manager-fallback)

To set the date display format on all the Cisco IP phones attached to
                              		  the router, use the date-format command in call-manager-fallback
                              		  configuration mode. To disable the date display format, use the no form of this command.

date-format { mm-dd-yy | dd-mm-yy | yy-dd-mm | yy-mm-dd }

no date-format { mm-dd-yy | dd-mm-yy | yy-dd-mm | yy-mm-dd }

### Syntax Description

mm-dd-yy

Sets the date format to month, day, year. Each element
                                          						requires a two-digit number. This format is the default setting.

dd-mm-yy

Sets the date format to day, month, year. Each element
                                          						requires a two-digit number.

yy-dd-mm

Sets the date format to year, day, month. Each element
                                          						requires a two-digit number.

yy-mm-dd

Sets the date format to year, month, day. Each element
                                          						requires a two-digit number.

### Command Default

mm-dd-yy

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(2)XT

Cisco SRST 2.0

This command was introduced on the following platforms:
                                          						Cisco 1750, Cisco 1751, Cisco 2600 series and Cisco 3600 series multiservice
                                          						routers, and Cisco IAD2420 series IADs.

12.2(8)T

Cisco SRST 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers.

12.2(8)T1

Cisco SRST 2.0

This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers.

12.2(11)T

Cisco SRST 2.01

This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers.

12.2(15)ZJ

Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.2(15)ZJ.

12.3(4)T

Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

## Examples

The following example sets the date format:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# date-format mm-dd-yy
```

### Related Commands

Command

Description

call-manager-fallback

Enables Cisco Unified SRST feature support and enters
                                          						call-manager-fallback configuration mode.

## default-destination

To create a default call routing path for incoming calls on Foreign
                              		  Exchange Office (FXO) ports during a WAN outage, use the default-destination command in
                              		  call-manager-fallback configuration mode. To delete the default destination
                              		  number on the Cisco Unified SRST router, use the no form of this command.

default-destination telephone-number

no default-destination telephone-number

### Syntax Description

telephone-number

Telephone number of the default destination.

### Command Default

No default behavior or values.

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.1(5)YD

Cisco SRST 1.0

This command was introduced on the following platforms:
                                          						Cisco 2600 series and Cisco 3600 series multiservice routers, and Cisco IAD2420
                                          						series IADs.

12.2(2)XT

Cisco SRST 2.0

This command was implemented on Cisco 1750 and Cisco 1751
                                          						multiservice routers.

12.2(8)T

Cisco SRST 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers.

12.2(8)T1

Cisco SRST 2.0

This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers.

12.2(11)T

Cisco SRST 2.01

This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers.

### Usage Guidelines

The default-destination command creates a
                              		  temporary Private Line Auto Ringdown (PLAR) connection configuration on FXO
                              		  ports during fallback. The default-destination command has been
                              		  obsoleted by the alias command, which applies to all port
                              		  types. Use of the alias command is recommended over the default-destination command.

## Examples

The following example sets the default destination to 40802:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# default-destination 40802
```

### Related Commands

Command

Description

alias (call-manager- fallback)

Provides a mechanism for servicing calls to telephone
                                          						numbers that are unavailable during Cisco Unified Communications Manager
                                          						fallback.

call-manager-fallback

Enables Cisco Unified SRST feature support and enters
                                          						call-manager-fallback configuration mode.

## description (voice moh-group)

To display a brief description specific to a MOH group, use the description command in voice moh-group
                              		  configuration mode. To remove the description, use the no form of this command.

description string

no description

### Syntax Description

string

An alphanumeric string to add a brief description specific
                                          						to a MOH group. Maximum length: 80 characters including spaces.

### Command Default

No MOH group description is configured.

### Command Modes

V oice moh-group configuration (config-voice-moh-group)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.0(1)XA

Cisco Unified CME 8.0 Cisco Unified SRST 8.0

This command was introduced

15.1(1)T

Cisco Unified CME 8.0 Cisco Unified SRST 8.0

This command was integrated into Cisco IOS Release
                                          						15.1(1)T.

### Usage Guidelines

This command allows you to type a brief text describing a specific
                              		  voice-moh-group. You can use maximum 80 characters, including spaces to
                              		  describe a MOH group.

## Examples

The following example provides a description for voice-moh-group1:

```
Router(config)# 
Router(config-voice-moh-group)#
Router(config-voice-moh-group) descri ption this is a moh group for sales
```

### Related Commands

Command

Description

voice-moh-group

Enter voice-moh-group configuration mode.

moh

Enables music on hold from a flash audio feed

multicast moh

Enables multicast of the music-on-hold audio stream.

extension-range

Specifies the extension range for a clients calling a
                                          						voice-moh-group.

## device-id

To specify the
                              		  device ID of a phone type, use the device-id command in ephone-type configuration mode. To reset to the default value, use
                              		  the no form of
                              		  this command.

device-id number

no device-id

### Syntax Description

number

Device
                                          						ID of the phone type. Range: 1 to 2,147,483,647. Default: 0. See Table 1 for a list of supported device IDs.

### Command Default

Device ID is 0.

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

### Usage Guidelines

This command
                              		  specifies the device ID of the type of phone being added with the ephone-type
                              		  template. If this command is set to the default value of 0, the ephone-type is
                              		  invalid.

Supported
                                          					 Device

device-id

num-buttons

max-presentation

Cisco
                                          					 Unified IP Conference Station 7937G

431

1

6

Nokia E61

376

1

1

## Examples

The following
                              		  example shows the device ID is set to 376 for the Nokia E61 when creating the
                              		  ephone-type template:

```
Router(config)# ephone-type E61 Router(config-ephone-type)# device-id 376 Router(config-ephone-type)# device-name E61 Mobile Phone
```

### Related Commands

Command

Description

device-name

Assigns
                                          						a name to a phone type in an ephone-type template.

load

Associates a type of phone with a phone firmware file.

type

Assigns the phone type to a SCCP phone.

## device-name

To assign a name to a phone type in an ephone-type template, use the device-name command in ephone-type
                              		  configuration mode. To remove the name, use the no form of this command.

device-name name

no device-name

### Syntax Description

name

String that identifies this phone type. Value is any
                                          						alphanumeric string up to 32 characters.

### Command Default

No name is assigned to this phone type.

### Command Modes

Ephone-type configuration (config-ephone-type)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)XZ

Cisco Unified CME 4.3 Cisco Unified SRST 4.3

This command was introduced.

### Usage Guidelines

This command specifies a device name for the type of phone being
                              		  added with the ephone-type template.

## Examples

The following example shows that the name “E61 Mobile Phone” is
                              		  assigned to a phone type when creating the ephone-type template:

```
Router(config)# ephone-type E61 Router(config-ephone-type)# device-id 376 Router(config-ephone-type)# device-name E61 Mobile Phone
```

### Related Commands

Command

Description

device-id

Specifies the device ID for a phone type in an ephone-type
                                          						template.

## device-type

To specify the
                              		  phone type, use the device-type command in ephone-type configuration mode. To reset to the default value, use
                              		  the no form of
                              		  this command.

device-type phone-type

no device-type

### Syntax Description

phone-type

Device
                                          						type of the phone. See Table 1 for a list of supported device types. Default value is the same value entered
                                          						with the ephone-type command.

### Command Default

Device type is
                              		  the same value that is entered with the ephone-type command.

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
                                          						command was integerated into Cisco IOS Release 12.4(20)T.

### Usage Guidelines

This command
                              		  specifies the device type of the phone being added with the ephone-type
                              		  template. The device type is set to the same value as the ephone-type command unless you use this command to change the value.

This command must
                              		  be set to one of the following supported values.

Supported
                                          					 Device

device-id

device-type

num-buttons

max-presentation

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
                                          					 Unified IP Conference Station 7937G

431

7937

1

6

Cisco
                                          					 Unified IP Phone 8941

586

8941

4

3

Cisco
                                          					 Unified IP Phone 8945

585

8945

4

3

Nokia
                                          					 E61

376

E61

1

1

## Examples

The following
                              		  example shows the device type set to 7915 in the ephone-type template for the
                              		  Cisco Unified IP Phone 7915 Expansion Module with 12 buttons:

```
Router(config)# ephone-type 7915-12 addon Router(config-ephone-type)# device-id 227 Router(config-ephone-type)# device-name 7915-12 Router(config-ephone-type)# device-type 7915
```

### Related Commands

Command

Description

device-name

Assigns a name to a phone type in an ephone-type template.

ephone-type

Adds
                                          						a Cisco Unified IP phone type by defining an ephone-type template.

load

Associates a type of phone with a phone firmware file.

type

Assigns the phone type to a SCCP phone.

## dialplan-pattern (call-manager-fallback)

To create a global prefix that can be used to expand the extension
                              		  numbers of inbound and outbound calls into fully qualified E.164 numbers, use
                              		  the dialplan-pattern command in
                              		  call-manager-fallback configuration mode. To disable the dialplan-pattern command settings, use the no form of this command.

dialplan-pattern tag pattern extension-length extension-length [ extension-pattern extension-pattern ] [ no-reg ]

no dialplan-pattern tag [ pattern extension-length extension-length extension-pattern extension-pattern ] [ no-reg ]

### Syntax Description

tag

Dial-plan string tag used before a ten-digit telephone
                                          						number. The tag number is from 1 to 5.

pattern

Dial-plan pattern, such as the area code, the prefix, and
                                          						the first one or two digits of the extension number, plus wildcard markers or
                                          						dots (.) for the remainder of the extension number digits.

extension-length

Sets the number of extension digits that will appear as a
                                          						caller ID.

extension-length

The number of extension digits. The extension length must
                                          						match the setting for IP phones in Cisco Unified Communications Manager mode.
                                          						The range is from 1 to 32.

extension-pattern

(Optional) Sets an extension number’s leading digit pattern
                                          						when it is different from the E.164 telephone number’s leading digits defined
                                          						in the pattern variable.

extension-pattern

(Optional) The extension number’s leading digit pattern.
                                          						Consists of one or more digits and wildcard markers or dots (.). For example,
                                          						5.. would include extensions 500 to 599; 5... would include extensions 5000 to
                                          						5999. The extension pattern must match the setting for IP phones in Cisco
                                          						Unified Communications Manager mode.

no-reg

(Optional) Prevents the E.164 numbers in the dial peer from
                                          						registering with the gatekeeper.

### Command Default

No default behavior or values.

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.1(5)YD

Cisco SRST 1.0

This command was introduced on the Cisco 2600 series and
                                          						Cisco 3600 series multiservice routers and on the Cisco IAD2420 series.

12.2(2)XT

Cisco SRST 2.0

This command was implemented on the Cisco 1750 and Cisco
                                          						1751 multiservice routers.

12.2(8)T

Cisco SRST 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725 and Cisco 3745 routers.

12.2(8)T1

Cisco SRST 2.0

This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers.

12.2(11)T

Cisco SRST 2.01

This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers.

12.2(11)YT

Cisco SRST 2.1

The extension-pattern keyword was
                                          						added.

12.4(20)T

Cisco Unified CME 7.0 Cisco Unified SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

The dialplan-pattern command builds additional
                              		  dial peers. For example, if a hidden POTS dial peer is created, such as the
                              		  following:

```
Router(config)# dial-peer voice 20001 pots Router(config-dial-peer)# destination-pattern 1001 Router(config-dial-peer)# voice-port 50/0/2
```

and a dial-plan pattern is created, such as 40855510.., then an
                              		  additional dial peer will be created that allows calls to both the 1001 and
                              		  4085551001 numbers. For example:

```
Router(config)# dial-peer voice 20002 pots Router(config-dial-peer)# destination-pattern 4085551001 Router(config-dial-peer)# voice-port 50/0/2
```

Both dial peers can be seen with the show dial-peer voice command.

The dialplan-pattern command also creates a
                              		  global prefix that can be used by inbound calls (calls to an IP phone in a
                              		  Cisco Unified SRST system) and outbound calls (calls made from an IP phone in a
                              		  Cisco Unified SRST system) to expand their extension numbers to fully qualified
                              		  E.164 numbers.

For inbound calls (calls to an IP phone in a Cisco Unified SRST
                              		  system) where the calling party number matches the dial-plan pattern, the call
                              		  is considered a local call and has a distinctive ring that identifies the call
                              		  as internal. Any calling party number that does not match the dial-plan pattern
                              		  is considered an external call and has a distinctive ring that is different
                              		  from the internal ringing.

For outbound calls, the dialplan-pattern command converts the calling
                              		  party’s extension number to an E.164 calling party number. Outbound calls that
                              		  do not use an E.164 number and go through a PRI connection to the PSTN may be
                              		  rejected by the PRI link as the calling party identifier.

If there are multiple patterns, called-party numbers are checked in
                              		  numeric order, starting with pattern 1, until a match is found or until the
                              		  last pattern has been checked. The valid dial-plan pattern with the lowest tag
                              		  is used as a prefix to all local Cisco IP phones.

When extension-pattern extension-pattern keyword and
                              		  argument are used, the leading digits of an extension pattern are stripped and
                              		  replaced with the corresponding leading digits of the dial plan. For example,
                              		  the following command maps all extension numbers 4xx to the PSTN number
                              		  40855501xx, so that extension 412 corresponds to 4085550112.

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# dialplan-pattern 1 4085550100 extension-length 3 extension-pattern 4..
```

The number of extension-pattern argument characters must
                              		  match the number set for the extension-length argument. For example, if
                              		  the extension-length is 3, the extension-pattern can be 8.., 1.., 51., and
                              		  so forth.

A dial-plan pattern is required to register the Cisco IP phone lines
                              		  with a gatekeeper. The no-reg keyword provides the option of not
                              		  registering specific numbers to the gatekeeper so that those numbers can be
                              		  used for other telephony services.

## Examples

The following example shows how to create dial-plan pattern 1 for
                              		  extension numbers 5000 to 5099 with a prefix of 408555. If an inbound calling
                              		  party number (4085555044) matches dial-plan pattern 1, the recipient phone will
                              		  display an extension (5044) as the caller ID and use an internal ringing tone.
                              		  If an outbound calling party extension number (5044) matches dial-plan pattern
                              		  1, the calling party extension will be converted to an E.164 number
                              		  (4085555044). The E.164 calling party number will appear as the caller ID.

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# dialplan-pattern 1 40855550.. extension-length 4 extension-pattern 50..
```

In the following example, the dialplan-pattern command creates dial-plan
                              		  pattern 1 for extensions 800 to 899 with the telephone prefix starting with
                              		  4085559. As each number in the extension pattern is declared with the number command, two POTs dial peers are
                              		  created. In the example, they are 801 (an internal office number) and
                              		  4085559001 (an external number).

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# dialplan-pattern 1 40855590.. extension-length 3 extension-pattern 8..
```

The following example shows a configuration for two Cisco Unified
                              		  SRST systems. Each is configured with the same dialplan-pattern commands, but one system
                              		  uses 50.. and the other uses 60.. for extension numbers. Calls from the “50..”
                              		  system to the “60..” system, and vice versa, are treated as internal calls.
                              		  Calls that go across an H.323 network and calls that go to a PSTN through an
                              		  ISDN interface on one of the configured Cisco Unified SRST routers are
                              		  represented as E.164.

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# dialplan-pattern 1 40855550.. extension-length 4 extension-pattern 50.. Router(config-cm-fallback)# dialplan-pattern 2 51055560.. extension-length 4 extension-pattern 60..
```

### Related Commands

Command

Description

call-manager-fallback

Enables Cisco Unified SRST support and enters
                                          						call-manager-fallback configuration mode.

show dial-peer voice

Displays information for voice dial peers.

## digit collect kpml

To enable Key Press Markup Language (KPML) digit collection on a SIP
                              		  phone, use the digit collect kpml command in voice register pool or voice
                              		  register template configuration mode. To disable KPML, use the no form of this command.

digit collect kpml

no digit collect kpml

### Syntax Description

This command has no arguments or keywords.

### Command Default

KPML digit collection is enabled.

### Command Modes

Voice register pool configuration Voice register template configuration

## Command History

Release

Cisco Product

Modification

12.4(11)XJ

Cisco Unified CME 4.1 Cisco Unified SRST 4.1

This command was introduced.

12.4(15)T

Cisco Unified CME 4.1 Cisco Unified SRST 4.1

This command was integrated into Cisco IOS Release
                                          						12.4(15)T.

### Usage Guidelines

KPML is enabled by default for all directory numbers on the phone. A
                              		  dial plan assigned to a phone has priority over KPML. Use the no digit collect kpml command to disable KPML on a phone.

If you use a voice register template to apply a command to a phone
                              		  and you also use the same command in voice register pool configuration mode for
                              		  the same phone, the value that you set in voice register pool configuration
                              		  mode has priority.

KPML is not supported on the Cisco IP Phone 7905, 7912, 7940, or
                              		  7960.

## Examples

The following example shows KPML enabled on SIP phone 4:

```
Router(config)# voice register pool 4 Router(config-register-pool)# digit collect kpml
```

### Related Commands

Command

Description

dialplan

Assigns a dial plan to a SIP phone.

show voice register pool

Displays all configuration information associated with a
                                          						SIP phone.

voice register dialplan

Enters voice register dialplan configuration mode to define
                                          						a dial plan for SIP phones.

## dtmf-relay (voice register pool)

To specify the list of DTMF relay methods that can be used to relay
                              		  dual-tone multifrequency (DTMF) audio tones between Session Initiation Protocol
                              		  (SIP) endpoints, use the dtmf-relay command in voice register pool
                              		  configuration mode. To send the DTMF audio tones as part of an audio stream,
                              		  use the no form of this command.

dtmf-relay [ cisco-rtp ] [ rtp-nte ] [ sip-notify ]

no dtmf-relay

### Syntax Description

cisco-rtp

Forwards DTMF audio tones by using Real-Time Transport
                                          						Protocol (RTP) with a Cisco proprietary payload type. This keyword is supported
                                          						only for dial peers that are created by incoming REGISTERs from a SIP gateway.
                                          						It is not supported for dial peers that are created by a SIP Cisco IP phone.

rtp-nte

Forwards DTMF audio tones by using Real-Time Transport
                                          						Protocol (RTP) with a Named Telephone Event (NTE) payload.

sip-notify

Forwards DTMF audio tones by using SIP-NOTIFY messages.
                                          						This keyword is supported only for dial peers that are created by incoming
                                          						REGISTERs from a SIP gateway. It is not supported for dial peers that are
                                          						created by a SIP Cisco IP phone.

### Command Default

DTMF tones are disabled and sent in-band. That is, they remain in the
                              		  audio stream.

### Command Modes

Voice register pool configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(4)T

Cisco SIP SRST 3.0

This command was introduced.

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was added to Cisco Unified CME.

Cisco Unified SIP SRST 12.8

Introduced support for YANG models.

### Usage Guidelines

During Cisco Unified Session Initiation Protocol (SIP) Survivable
                              		  Remote Site Telephony (SRST) or Cisco Unified CME registration, a dial peer is
                              		  created and that dial peer has a default DTMF relay of in-band.

This command command allows you to change the default to a desired
                              		  value. You must use one or more keywords when configuring this command.

DTMF audio tones are generated when you press a button on a
                              		  Touch-Tone phone. The tones are compressed at one end of the call and when the
                              		  digits are decompressed at the other end, there is a risk that they can become
                              		  distorted. DTMF relay reliably transports the DTMF audio tones generated after
                              		  call establishment out-of-band.

The SIP Notify method sends Notify messages bidirectionally between
                              		  the originating and terminating gateways for a DTMF event during a call. If
                              		  multiple DTMF relay mechanisms are enabled on a SIP dial peer and are
                              		  negotiated successfully, the SIP Notify method takes precedence.

SIP Notify messages are advertised in an Invite message to the remote
                              		  end only if the dtmf-relay command is set.

For SIP calls, the most appropriate methods to transport DTMF tones
                              		  are RTP-NTE or SIP-NOTIFY.

- The sip-notify keyword is available only if the VoIP
                                 			 dial peer is configured for SIP.

## Examples

## Examples

The following example shows how to enable the RTP-NTE and SIP-NOTIFY
                              		  mechanisms for DTMF relay for SIP phone 4:

```
Router(config)# voice register pool 4 Router(config-register-pool)# dtmf-relay rtp-nte sip-notify
```

## Examples

The following is sample output from the show running-config command that shows that voice register pool 1 has been set up
                              		  to send DTMF tones:

```
voice register pool 1 
 application SIP.app
 incoming called-number 308
 voice-class codec 1
 dtmf-relay rtp-nte
```

### Related Commands

Command

Description

dtmf-relay (voice over IP)

Specifies how an H.323 or SIP gateway relays DTMF tones
                                          						between telephony interfaces and an IP network.

## elin

To create a PSTN number that replaces a 911 caller’s extension, use
                              		  the elin command in voice emergency response
                              		  location configuration mode. To remove the number, use the no form of this command.

elin [ 1 | 2 ] number

no elin [ 1 | 2 ]

### Syntax Description

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

Use this command to specify the ELIN, a PSTN number that will replace
                              		  the caller’s extension. The PSAP will see this number and use it to query the
                              		  ALI database to locate the caller. It is also used by the PSAP for callbacks.
                              		  You can optionally configure a second ELIN using the elin 2 command. If two ELINs are configured, the system selects an
                              		  ELIN using a round-robin algorithm. If an ELIN is not defined for the ERL, the
                              		  PSAP will see the original calling number.

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

voice emergency response location

Creates a tag for identifying an ERL for Enhanced 911
                                          						Services.

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

This command specifies an E.164 number to be the default ELIN if the
                              		  911 caller’s IP phone address does not match the subnet of any location in any
                              		  ERL zone. The default ELIN can be an existing ELIN already defined in an ERL or
                              		  it can be unique.

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

This command defines which dial peer is used for 911 callbacks from
                              		  the PSAP. You can define multiple dial peers with this command.

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
                              		  valid ERL configuration, the phone is not associated to an ERL. For IP phones,
                              		  the IP address is used to find the inclusive ERL subnet. For phones is on a
                              		  VoIP trunk or FXS/FXO trunk, the PSAP gets a reorder tone.

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

The zone tag option was added. This command was added for
                                          						Cisco Unified CME.

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

To encrypt the password that is configured on Unified SRST, use the encrypt password command in call-manager-fallback configuration mode. To disable password encryption, use the no form of this command.

encrypt pasword

no encrypt password

### Syntax Description

This command has no arguments or keywords.

### Command Default

This command is enabled by default.

### Command Modes

Call Manager Fallback configuration (config-cm-fallback)

## Command History

Cisco IOS Release

Cisco Product

Modification

Cisco IOS XE Gibraltar 16.11.1a Release

Unified SRST 12.6

The command is introduced.

### Usage Guidelines

The CLI command encrypt password is enabled by default on Unified SRST router. However, it is mandatory to configure key config-key password-encrypt [Master key] and password encryption aes along with encrypt password to support encryption on Unified SRST router.

If the key used to encrypt the password is replaced with a new key (replace key or re-key), then the password is re-encrypted
                                          with the new key.

### Related Commands

Command

Description

call-manager-fallback

Enables Unified SRST feature support and enters call-manager-fallback configuration mode.

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

Cisco Unified CME 7.0 Cisco Unified SRST 7.0

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

### Usage Guidelines

Use this command to specify the amount of time (in minutes) to keep
                              		  emergency caller history for each ELIN. The time can be an integer in the range
                              		  of 2 to 2880 minutes. The default value is 180 minutes.

## Examples

In this example, the ELIN (4085550101) defined in the voice emergency
                              		  response settings configuration will be used if the 911 caller’s IP phone
                              		  address does not match any of the voice emergency response locations. After the
                              		  911 call is placed to the PSAP, the PSAP has 120 minutes to call back 408
                              		  555-0101 to reach the 911 caller. If the call history has expired (after 120
                              		  minutes), any callback is routed to extension 7500.

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

Hexidecimal digits (0-9 or A-F) that define the starting
                                          						extension number in an extension range. Maximum length: 32 digits.

ending-extension

Hexidecimal digits (0-9 or A-F) that define the last
                                          						extension number in an extension range. Value of the ending extensing must be
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
Router(config-voice-moh-group)# moh flahs:/minuet.wav Router(config-voice-moh-group)# description Marketing
Router(cconfig-voice-moh-group)# extension range 1000 to 1999 Router(config-voice-moh-group)# extension range 3000 to 3999 Router(config-voice-moh-group)#
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

Each bellcore-dr keyword supports standard distinctive ringing
                                          						patterns as defined in the standard GR-506-CORE, LSSGR: Signaling for Analog Interfaces .

### Command Default

The default ring sound is an internal ring pattern.

### Command Modes

Voice register global configuration

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

### Related Commands

Command

Description

voice register global

Enters voice register global configuration mode in order to
                                          						set global parameters for all supported Cisco SIP phones in a Cisco Unified
                                          						Communications Manager Express (Cisco Unified CME) or Cisco Unified SIP
                                          						Survivable Remote Site Telephony (SRST) environment.

## group
                        	 phone

To add a phone,
                              		  including a TAPI-based client application, or a softphone on a PC to a VRF
                              		  group for Cisco Unified CME, use the group phone command in ephone or ephone-template
                              		  configuration mode. To remove the configuration, use the no form of
                              		  this command.

group phone group-tag [ tapi group-tag ]

no group phone

### Syntax Description

group-tag

Unique
                                          						identifier of VRF group ranges from 1 to 5.

tapi

(Optional) Add TAPI-based client on the phone being configured to a VRF group.

### Command Default

By default, this
                              		  feature is disabled.

### Command Modes

Ephone configuration (config-ephone)

Ephone-template configuration (config-ephone-template)

Voice register pool

Voice register template

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Products

Modification

12.4(22)T

Cisco
                                          						Unified SRST 7.0(1)

This
                                          						command was introduced.

15.4(3)M

Cisco
                                          						Unified SRST 10.5

This
                                          						command was modified.

### Usage Guidelines

This command
                              		  enables you to configure the voice VRF group for SIP phones.

This command adds
                              		  a softphone on a PC, an IP phone, or a TAPI client on an IP phone to a VRF
                              		  group.

VRF groups for
                              		  users and phones in Cisco Unified CME are created by using the group command
                              		  in telephony-service configuration mode.

All SCCP and SIP
                              		  phones connected to Cisco Unified CME must register through the global voice
                              		  VRF.

TAPI-based client
                              		  on an IP phone and softphones on a PC must register in Cisco Unified CME
                              		  through a data VRF.

Before you can
                              		  use this command, the MAC address for the IP phone being configured must be
                              		  configured by using the mac-address command in ephone configuration mode.

If you use an
                              		  ephone template to apply a command to an ephone and you also use the same
                              		  command in ephone configuration mode, the value that you set in ephone
                              		  configuration mode has priority over the ephone-template configuration.

## Examples

The following
                              		  example shows four phones in three VRF groups, two on data VRFs and one on a
                              		  global voice VRF.

```
telephony-service
 sdspfarm conference mute-on # mute-off #
 sdspfarm units 4
 sdspfarm transcode sessions 10
 sdspfarm tag 1 xcode101
 sdspfarm tag 2 conf103
 group  1 
  ip source-address 209.165.201.1 port 2000
  url directories http://209.165.201.1/localdirectory
 !
 group  2 vrf data-vrf1
  ip source-address 209.165.201.2 port 2000
 !
group  3 vrf data-vrf2
  ip source-address 209.165.201.3 port 2000
 !
.
.
!
ephone-template 1
  group phone 1 tapi 2
ephone-template 2
  group phone 2
...
ephone 1
  mac-address 1111.2222.3333
  ephone-template 1
ephone 2
  mac-address 2222.2222.3333
  ephone-template 2
ephone 3
  mac-address 1111.3333.3333
  group phone 1 tapi 3
ephone 4
  mac-address 1111.2222.4444
  group phone 3
!
```

## Examples

The following
                              		  example shows four phones in three VRF groups, two on data VRFs and one on a
                              		  global voice VRF.

```
Router(config)# voice register template Router(config-telephony)# group-phone <group-tag>
```

### Related Commands

Command

Description

voice register pool

Enters
                                          						voice register pool configuration mode.

voice register
                                                							 template

Enters
                                          						voice register template configuration mode.

ephone-template (ephone)

Applies an ephone template to an ephone configuration.

group (telephony-service)

Creates a VRF group for phones and users in Cisco Unified CME.

mac-address

Associates the MAC address of a Cisco IP phone with an ephone configuration.

## h450 h450-2 timeout (voice service voip)

To specify timeout values for call transfers using the ITU-T H.450.2
                              		  standard, use the h450 h450-2 timeout command in H.323 voice service configuration mode. To return to
                              		  the default values, use the no form of this command.

h450 h450-2 timeout { T1 | T2 | T3 | T4 } milliseconds

no h450 h450-2 timeout { T1 | T2 | T3 | T4 }

### Syntax Description

T1

Timer for identification.

T2

Timer for call setup.

T3

Timer for response initiation.

T4

Timer for response setup.

milliseconds

Number of milliseconds. Range is from 500 to 60000.

### Command Default

T1 timer is 2000 milliseconds. T2 timer is 5000 milliseconds. T3
                              		  timer is 5000 milliseconds. T4 timer is 5000 milliseconds.

### Command Modes

H.323 voice service configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco SRST 3.0

This command was introduced.

12.3(4)T

Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

Use this command with Cisco SRST V3.0 or a later version.

This command is used primarily when the default settings for these
                              		  timers do not match your network delay parameters. See the ITU-T H.450.2
                              		  specification for more information on these timers.

## Examples

The following example defines a T1 timeout of 3000 milliseconds:

```
Router(config)# voice service voip Router(conf-voi-serv)# h323 Router(conf-serv-h323)# h450 h450-2 timeout T1 3000
```

### Related Commands

Command

Description

h323

Enables H.323 voice service configuration commands.

voice service

Enters voice-service configuration mode.

## http client secure-ciphersuite

To set the secure encryption cipher suite for the HTTP client, use the http client secure-ciphersuite command in global configuration mode. To reset to the default, use the no form of this command. All ciphers are selected by default, use the default form of this command.

http client secure-ciphersuite [ 3des_cbc_sha ] [ aes-128-cbc-sha ] [ des_cbc_sha ] [ dhe-rsa-aes-cbc-sha2 ] [ ecdhe-ecdsa-aes-gcm-sha2 ] [ ecdhe-rsa-aes-cbc-sha2 ] [ ecdhe-rsa-aes-gcm-sha2 ] [ null_md5 ] [ rc4_128_md5 ] [ rc4_128_sha ] [ rsa-aes-cbc-sha2 ] [ tls13-aes128-gcm-sha256 ] [ tls13-aes256-gcm-sha384 ] [ tls13-chacha20-poly1305-sha256 ]

no http client secure-ciphersuite

default http client secure-ciphersuite

### Syntax Description

Encryption tls_rsa_with_3des_ede_cbc_sha (TLS1.0) ciphersuite.

Encryption tls_rsa_with_aes_128_cbc_sha (TLS1.2 and below versions) ciphersuite.

Encryption tls_rsa_with_des_cbc_sha (TLS1.0) ciphersuite

Encryption tls_rsa_with_cbc_sha2 (TLS1.2) ciphersuite

Encryption tls_rsa_with_ecdhe-ecdsa-aes-gcm-sha2 (TLS1.2) ciphersuite

Encryption tls_rsa_with_aes-cbd-sha2 (TLS1.2) ciphersuite

Encryption tls_rsa_with_aes-gcm-sha2 (TLS1.2) ciphersuite

Encryption tls_rsa_with_null_md5 (TLS1.0) ciphersuite

Encryption tls_rsa_with_rc4_128_md5 (TLS1.0) ciphersuite

Encryption tls_rsa_with_rc4_128_sha (TLS1.0) ciphersuite

Encryption tls_rsa_with_aes_cbc_sha2 (TLS1.2) ciphersuite

Encryption tls13_aes128_gcm_sha256 (TLS1.3) ciphersuite.

Encryption tls13_aes256_gcm_sha384 (TLS1.3) ciphersuite.

Encryption tls13_chacha20_poly1305_sha256 (TLS1.3) ciphersuite.

### Command Default

Supports all cipher suites.

### Command Modes

Global configuration (config)

## Command History

Cisco IOS Release

Cisco Product

Modification

Cisco IOS XE 17.14.1a

Unified SRST 14.4

This command was modified to support the following TLS version 1.3 ciphers—

tls13-aes128-gcm-sha256

tls13-aes256-gcm-sha384

tls13-chacha20-poly1305-sha256

Introduced support for the TLS version 1.3 ciphers Yang model.

### Usage Guidelines

Use the http client secure-ciphersuite command to configure one or more cipher suites, or sets of encryption and hash algorithms, on the HTTP client. You must include
                              at least one of the keywords and can include more than one. Use the show http client secure status command to display the cipher suites configured.

## Examples

The following example sets the HTTP client to use the 3des_cbc_sha and null_md5 cipher suites:

```
Device(config)# http client secure-ciphersuite 3des_cbc_sha null_md5 HTTP Client Secure Ciphersuite: 3des_cbc_sha null_md5
```

The following example shows how to configure HTTP client to use the TLS version 1.3 cipher suites:

```
Device(config)# http client secure-ciphersuite  tls13-aes128-gcm-sha256 tls13-aes256-gcm-sha384 tls13-chacha20-poly1305-sha256 HTTP Client Secure Ciphersuite: tls13-aes128-gcm-sha256 tls13-aes256-gcm-sha384 tls13-chacha20-poly1305-sha256
```

The following example shows how to configure HTTP client in default mode to use all the supported cipher suites:

```
Device(config)# default http client secure-ciphersuite No TLS ciphersuite selected, default to all
HTTP Client Secure Ciphersuite: aes-128-cbc-sha rsa-aes-cbc-sha2 dhe-rsa-aes-cbc-sha2 ecdhe-rsa-aes-gcm-sha2 ecdhe-rsa-aes-cbc-sha2 
ecdhe-ecdsa-aes-gcm-sha2 tls13-aes128-gcm-sha256 tls13-aes256-gcm-sha384 tls13-chacha20-poly1305-sha256
```

### Related Commands

Command

Description

http client secure-trustpoint

Declares the trustpoint that the HTTP client should use for HTTPS sessions.

show http client secure status

Displays the trustpoint and cipher suites that are configured in the HTTP client.

## huntstop (call-manager-fallback)

To set the huntstop attribute for the dial peers associated with a
                              		  Cisco Unified IP phone during Cisco Unified Communications Manager fallback,
                              		  use the huntstop command in call-manager-fallback
                              		  configuration mode. To disable huntstop, use the no form of this command.

huntstop [channel] 1-8

no huntstop

### Syntax Description

channel

(Optional) For dual-line ephone-dns, keeps incoming calls
                                          						from hunting to the second channel if the first channel is busy or does not
                                          						answer.

1-8

(Optional) For octo-line ephone-dns, keeps incoming calls
                                          						from hunting to the next channel if the last allowable channel is busy or does
                                          						not answer. The default is 8.

### Command Default

Huntstop is enabled by default. For octo-line mode, the default
                              		  number is 8.

### Command Modes

Call-manager-fallback configuration (config-cm-fallback)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.1(5)YD

Cisco SRST 1.0

This command was introduced on the following platforms:
                                          						Cisco 2600 series and Cisco 3600 series multiservice routers, and Cisco IAD2420
                                          						series IADs.

12.2(2)XT

Cisco SRST 2.0

This command was implemented on Cisco 1750 and Cisco 1751
                                          						multiservice routers.

12.2(8)T

Cisco SRST 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers.

12.2(8)T1

Cisco SRST 2.0

This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers.

12.2(11)T

Cisco SRST 2.01

This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers.

12.2(15)ZJ

Cisco SRST 3.0

The channel keyword was added.

12.3(4)T

Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

12.4(15)XZ

Cisco Unified SRST 4.3

The 1-8 argument was added for
                                          						octo-line mode.

12.4(20)T

Cisco Unified CME 7.0 Cisco Unified SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

In call-manager-fallback configuration mode, the huntstop attribute
                              		  by default is set uniformly to all Cisco Unified IP phone lines (for example,
                              		  to all or to none).

## Examples

The following example shows how to disable huntstop for all Cisco
                              		  Unified IP phones:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# no huntstop
```

The following example shows that octo-line is enabled, the maximum
                              		  directory numbers is 12, and huntstop is limited at 6 channels:

```
Router(config)# call-manager-fallback
```

Router(config-cm-fallback)# max-dn 12 octo-line 6

### Related Commands

Command

Description

call-manager-fallback

Enables Cisco Unified SRST support and enters
                                          						call-manager-fallback configuration mode.

huntstop (dial-peer)

Disables all further dial-peer hunting if a call fails
                                          						using hunt groups.

max-dn (call- manager-fallback)

Sets the maximum possible number of virtual voice ports
                                          						that can be supported by a router and activates dual-line mode, octo-line mode,
                                          						or both modes.

## id (voice register pool)

To explicitly identify a locally available individual Cisco SIP IP
                              		  phone, or when running Cisco Unified Session Initiation Protocol (SIP)
                              		  Survivable Remote Site Telephony (SRST), set of Cisco SIP IP phones, use the id command in voice register pool
                              		  configuration mode. To remove local identification, use the no form of this command.

id [ network address mask mask | address mask mask ] [ip address mask mask address mask mask ] [mac address ]

[device-id-name devicename ]

[ phone-number e164-number | extension-number extension-number ]

no id { [ network address mask mask | address mask mask ] | [ip address mask mask address mask mask ] | [mac address ] } [device-id-name devicename ]

[ phone-number e164-number | extension-number extension-number ]

### Syntax Description

network address mask mask | address mask mask

This keyword/argument combination is used to accept SIP
                                          						Register messages for the indicated phone numbers from any IP phone within the
                                          						specified IPv4 and IPv6 subnets. ipv6 address can only be configured
                                          						with an IPv6 address or a dual-stack mode.

ip address mask mask | address mask mask

This keyword/argument combination is used to identify an
                                          						individual phones IPv4 or IPv6 address. ipv6 address can only be
                                          						configured with an IPv6 address or a dual-stack mode.

mac address

The mac address keyword/argument
                                          						combination is used to identify the MAC address of a particular Cisco IP phone.

device-id-name devicename

Defines the device name to be used to download the phone’s
                                          						configuration file.

phone-number e164-number

Configures the phone-number in E.164 format for webex calling user.

extension-number extension-number

Configures extension number for Webex Calling users.

### Command Default

No SIP IP phone is configured.

### Command Modes

Voice register pool configuration (config-register-pool)

## Command History

Release

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

15.3(3)T

Cisco Unified CME 10.0

This command was modified to add the device-id-name devicename keyword-argument
                                          						combination.

Cisco IOS XE Everest 16.6.1

Unified SRST 12.0

This command was modified to add the following
                                          						keyword-argument combinations for network and ip to include support for IPv6
                                          						address: address mask mask .

Cisco Unified SIP SRST 12.8

Introduced support for YANG models.

Cisco IOS XE Cupertino 17.9.1

Cisco Unified SRST 14.3

This command was modified to add the following: phone-number e164-number and extension-number extension-number

### Usage Guidelines

Configure this command before configuring any other command in voice
                              		  register pool configuration mode.

This command allows explicit identification of an individual Cisco
                              		  SIP IP phone to support a degree of authentication, which is required to accept
                              		  registrations, based upon the following:

Verification of the local Layer 2 MAC address using the router’s Address Resolution Protocol (ARP) cache.

Verification of the known single static IP address (or DHCP dynamic IP address within a specific subnet) of the Cisco SIP
                                    IP phone.

When the mac address keyword and argument are used, the IP phone must be in
                              		  the same subnet as that of the router’s LAN interface, such that the phone’s
                              		  MAC address is visible in the router’s ARP cache. Once a MAC address is
                              		  configured for a specific voice register pool, remove the existing MAC address
                              		  before changing to a new MAC address.

## Examples

The following is partial sample output from the show running-config command. The id command identifies the MAC address of a
                              		  particular Cisco IP phone. The output shows that voice register pool 1 has been
                              		  set up to accept SIP Register messages from a specific IP phone through the use
                              		  of the id command.

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

## Examples

The following is sample output from the show command after configuring IPv6 address on Cisco Unified SRST router.

```
voice register pool 1
 id network 2001:420:54FF:13::312:0/117
```

## Examples

The following is sample output from the show phone-number e164-number .

```
voice register pool 10
 id phone-number +15139413701
 dtmf-relay rtp-nte
 voice-class codec 10
```

The following is sample output from the show and extension-number extension-number .

```
voice register pool 10
 id extension-number 3701
 dtmf-relay rtp-nte
 voice-class codec 10
```

### Related Commands

Command

Description

mode (voice register global)

Enables the mode for provisioning SIP phones in a Cisco
                                          						Unified CallManager Express (Cisco Unified CME) system.

## incoming called-number (voice register pool)

To apply incoming called-number parameters to dynamically created
                              		  dial peers, use the incoming called-number command in voice register pool
                              		  configuration mode. To remove incoming called-number parameters from a dial
                              		  peer, use the no form of this command.

incoming called-number [ numbe r ]

no incoming called-number

### Syntax Description

number

(Optional) Sequence of digits that represent a phone number
                                          						prefix.

### Command Default

None

### Command Modes

Voice register pool configuration

## Command History

Release

Cisco Product

Modification

12.2(15)ZJ

Cisco SIP SRST 3.0

This command was introduced.

12.3(4)T

Cisco SIP SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

The id (voice register pool) command must be configured before any
                              		  other voice register pool commands, including the incoming called-number command. The id command identifies a locally available
                              		  individual Cisco SIP IP phone or a set of Cisco SIP IP phones.

## Examples

The following is partial sample output from the show running-config command that applies the prefix 308 to dynamically created dial
                              		  peers:

```
voice register pool 1 
 application SIP.app
 incoming called-number 308
 voice-class codec 1
```

### Related Commands

Command

Description

id (voice register pool)

Explicitly identifies a locally available individual Cisco
                                          						SIP IP phone or set of Cisco SIP IP phones.

incoming called-number (dial-peer)

Specifies an incoming called number of an MMoIP or POTS
                                          						dial peer.

show dial-peer voice

Displays information for voice dial peers.

voice register pool

Enables SIP SRST voice register pool configuration
                                          						commands.

## ip qos dscp (call-manager-fallback)

To set the Differentiated Services Code Point (DSCP) for marking the
                              		  quality of service (QoS) requirements for each packet, use the ip qos dscp command in call-manager-fallback configuration mode. To reset
                              		  to the default value, use the no form of this command.

ip qos dscp { number | af | cs | default | ef } { media | service | signaling | video }

no ip qos dscp { number | af | cs | default | ef } { media | service | signaling | video }

### Syntax Description

number

DSCP value. Range: 0 to 63.

af

Sets DSCP to assured forwarding bit pattern.

- af11 —bit
                                             						  pattern 001010

- af12 —bit
                                             						  pattern 001100

- af13 — bit
                                             						  pattern 001110

- af21 — bit
                                             						  pattern 010010

- af22 — bit
                                             						  pattern 010100

- af23 — bit
                                             						  pattern 010110

- af31 — bit
                                             						  pattern 011010

- af32 — bit
                                             						  pattern 011100

- af33 — bit
                                             						  pattern 011110

- af41 —bit
                                             						  pattern 100010

- af42 —bit
                                             						  pattern 100100

- af43 —bit
                                             						  pattern 100110

cs

Sets DSCP to class-selector codepoint.

- cs1 —codepoint
                                             						  1 (precedence 1)

- cs2 —codepoint
                                             						  2 (precedence 2)

- cs3 —codepoint
                                             						  3 (precedence 3)

- cs4 —codepoint
                                             						  4 (precedence 4)

- cs5 —codepoint
                                             						  5 (precedence 5)

- cs6 —codepoint
                                             						  6 (precedence 6)

- cs7 —codepoint
                                             						  7 (precedence 7)

default

Sets DSCP to default bit pattern of 000000.

ef

Sets DSCP to expedited forwarding bit pattern 101110.

media

Applies DSCP to media payload packets for SCCP phones.

service

Not supported for Cisco Unified SRST.

signaling

Not supported for Cisco Unified SRST.

video

Not supported for Cisco Unified SRST.

### Command Default

DSCP for media is ef .

### Command Modes

Call-manager-fallback configuration (config-cm-fallback)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(22)YB

Cisco Unified SRST 7.1

This command was introduced.

12.4(24)T

Cisco Unified SRST 7.1

This command was integrated into Cisco IOS Release
                                          						12.4(24)T.

### Usage Guidelines

This command allows you to set different priority levels for
                              		  different types of network traffic sent by the Cisco Unified SRST router.
                              		  Differentiated Services is a method of prioritizing specific network traffic
                              		  based on the QoS specified by each packet.

Because Cisco Unified IP Phones get their DSCP information from the
                              		  configuration file that is downloaded to the device, and Cisco Unified SRST
                              		  does not download configuration files to phones during fallback, only the value
                              		  set with the media keyword takes effect for SCCP phones.

If the DSCP is configured for the gateway interface using the service-policy command or in the dial peer
                              		  using the ip qos dscp command, the value set with those commands
                              		  takes precedence over the DSCP value configured with this command.

## Examples

The following example shows DSCP set for different types of packets .

```
call-manager-fallback
 ip qos dscp cs2 media
 ip qos dscp cs1 signal
 ip qos dscp cs3 video
 ip qos dscp cs4 service
```

### Related Commands

Command

Description

ip qos dscp

Sets the DSCP for QoS in a dial peer.

service-policy

Assigns a policy map to an interface that will be used as
                                          						the service policy for the interface.

## ip source-address (call-manager-fallback)

To enable the SRST router to receive messages from Cisco IP phones
                              		  through the specified IP addresses and ports, use the ip source-address command in call-manager-fallback
                              		  configuration mode. To disable the router from receiving messages from Cisco IP
                              		  phones, use the no form of this command.

ip source-address ip-address [ port port ] [ any-match | strict-match ]

no ip source-address [ ip-address port port ] [ any-match | strict-match ]

### Syntax Description

ip-address

The preexisting SRST router IP address, typically one of
                                          						the addresses of the Ethernet port of the local router.

port

(Optional) The port to which the gateway router connects to
                                          						receive messages from the Cisco IP phones.

port

(Optional) The port number. The range is from 2000 to 9999.
                                          						The default is 2000.

any-match

(Optional) Disables strict IP address checking for
                                          						registration. This is the default.

strict-match

(Optional) Requires strict IP address checking for
                                          						registration.

### Command Default

Default port number: 2000 Default server address match: any-match

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.1(5)YD

Cisco SRST 1.0

This command was introduced on the following platforms:
                                          						Cisco 2600 series and Cisco 3600 series multiservice routers, and Cisco IAD2420
                                          						series IADs.

12.2(2)XT

Cisco SRST 2.0

This command was implemented on Cisco 1750 and Cisco 1751
                                          						multiservice routers.

12.2(8)T

Cisco SRST 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers.

12.2(8)T1

Cisco SRST 2.0

This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers.

12.2(11)T

Cisco SRST 2.01

This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers.

### Usage Guidelines

The ip source-address command is a mandatory command. The fallback subsystem does not
                              		  start if the IP address of the Ethernet port to which the phones are connected
                              		  (typically the ethernet interface of the local SRST gateway) is not provided.
                              		  If the port number is not provided, the default value (2000) is used.

Use the any-match keyword to instruct the router to
                              		  permit Cisco IP phone registration even when the IP server address used by the
                              		  phone does not match the IP source address. This option can be used to allow
                              		  registration of Cisco IP phones on different subnets or those with different
                              		  default DHCP routers or different TFTP server addresses.

Use the strict-match keyword to instruct the router to reject Cisco IP phone
                              		  registration attempts if the IP server address used by the phone does not
                              		  exactly match the source address. By dividing the Cisco IP phones into groups
                              		  on different subnets and giving each group different DHCP default-router or
                              		  TFTP server addresses, this option can be used to restrict the number of Cisco
                              		  IP phones allowed to register.

The ip source-address command enables a router to receive
                              		  messages from Cisco IP phones through the specified IP addresses and port. If
                              		  the router receives a registration request from a Cisco IP phone, the router in
                              		  return requests the phone configuration and dial-plan information from the
                              		  Cisco IP phone. This data is stored locally in the memory of the router and is
                              		  used to create voice-port and dial-plan information. The voice-port and
                              		  dial-plan information is used to handle telephony calls to and from the Cisco
                              		  IP phone if the Cisco Unified Communications Manager is unreachable.

## Examples

The following example shows how to set the IP source address and
                              		  port:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# ip source-address 10.6.21.4 port 2002 strict-match
```

### Related Commands

Command

Description

call-manager-fallback

Enables Cisco Unified SRST support and enters
                                          						call-manager-fallback configuration mode.

## ip source-address (credentials)

To enable the Cisco Unified CME or SRST router to receive credential
                              		  service messages through the specified IP address and port, use the ip source-address command in credentials configuration mode. To disable the
                              		  router from receiving messages, use the no form of this command.

ip source-address ip-address [ port [port] ]

no ip source-address

### Syntax Description

ip-address

Router IP address, typically one of the addresses of the
                                          						Ethernet port of the local router.

port port

(Optional) TCP port for credentials service communication.
                                          						Range is from 2000 to 9999. Cisco Unified CME default is 2444. SRST default is
                                          						2445.

### Command Default

Cisco Unified CME default port number: 2444 Cisco Unified SRST
                              		  default port number: 2445

### Command Modes

Credentials configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(14)T

Cisco SRST 3.3

This command was introduced for Cisco Unified SRST.

12.4(4)XC

Cisco Unified CME 4.0

This command was introduced for Cisco Unified CME.

### Usage Guidelines

Cisco Unified CME

This command is used with Cisco Unified CME phone authentication to
                              		  identify a Cisco Unified CME router on which a CTL provider is being
                              		  configured.

Cisco Unified SRST

The ip source-address command is a mandatory command to enable secure SRST. If the
                              		  port number is not provided, the default value (2445) is used. The IP address
                              		  is usually the IP address of the secure SRST router.

## Examples

## Examples

The following example creates a CTL provider on a Cisco Unified CME
                              		  router that is not running the CTL client.

```
Router(config)# credentials Router(config-credentials)# ip source-address 172.19.245.1 port 2444 Router(config-credentials)# trustpoint ctlpv Router(config-credentials)# ctl-service admin user4 secret 0 c89L8o
```

## Examples

The following example enters credentials configuration mode and sets
                              		  the IP source address and port:

```
Router(config)# credentials Router(config-credentials)# ip source-address 10.6.21.4 port 2445
```

### Related Commands

Command

Description

credentials

Enters credentials configuration mode to configure a Cisco
                                          						Unified CME CTL provider certificate or an SRST router certificate.

ctl-service admin

Specifies a user name and password to authenticate the CTL
                                          						client during the CTL protocol.

debug credentials

Sets debugging on the credentials service that runs between
                                          						a Cisco Unified CME CTL provider and the CTL client or between an SRST router
                                          						and Cisco Unified Communications Manager.

show credentials

Displays the credentials settings on a Cisco Unified CME or
                                          						SRST router.

trustpoint (credentials)

Specifies the name of the trustpoint to be associated with
                                          						a Cisco Unified CME CTL provider certificate or with an SRST router
                                          						certificate.

## keepalive (call-manager-fallback)

To configure the time interval between successive keepalive messages
                              		  from Cisco IP phones, use the keepalive command in call-manager-fallback
                              		  configuration mode. To restore to the default interval, use the no form of this command.

keepalive seconds

no keepalive seconds

### Syntax Description

seconds

Keepalive message transmission interval, in seconds. The
                                          						valid range is from 10 to 65535. The default timeout value is 30.

### Command Default

30 seconds

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.1(5)YD

Cisco SRST 1.0

This command was introduced on the following platforms:
                                          						Cisco 2600 series and Cisco 3600 series multiservice routers; and Cisco IAD2420
                                          						series IADs.

12.2(2)XT

Cisco SRST 2.0

This command was implemented on Cisco 1750 and Cisco 1751
                                          						multiservice routers.

12.2(8)T

Cisco SRST 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers.

12.2(8)T1

Cisco SRST 2.0

This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers.

12.2(11)T

Cisco SRST 2.01

This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers.

### Usage Guidelines

The keepalive command configures the time interval between successive
                              		  keepalive messages from Cisco IP phones to the Cisco Unified SRST router. If
                              		  the router fails to receive three successive keepalive messages, it considers
                              		  the Cisco IP phone to be out of service until the phone reregisters.

## Examples

The following example sets the keepalive timeout value to 60 seconds:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# keepalive 60
```

### Related Commands

Command

Description

call-manager-fallback

Enables Cisco Unified SRST feature support and enters
                                          						call-manager-fallback configuration mode.

## limit-dn (call-manager-fallback)

To specify the maximum number of lines available on each Cisco IP
                              		  phone, use the limit-dn command in call-manager-fallback configuration mode. To return
                              		  to the default setting, use the no form of this command.

limit-dn phone-type max-lines

no limit-dn phone-type

### Syntax Description

phone-type

Type of phone. The following phone types are predefined in
                                          						the system:

12SP

12SP+ and 30VIP phones

6901

Cisco Unified IP Phone 6901

6911

Cisco Unified IP Phone 6911

6921

Cisco Unified IP Phone 6921

6941

Cisco Unified IP Phone 6941

6961

Cisco Unified IP Phone 6961

7902

Cisco Unified IP Phone 7902

7905

Cisco Unified IP Phone 7905

7906

Cisco Unified IP Phone 7906

7910

Cisco Unified IP Phone 7910

7911

Cisco Unified IP Phone 7911

7912

Cisco Unified IP Phone 7912

7920

Cisco Unified IP Phone 7920

7921

Cisco Unified IP Phone 7921

7925

Cisco Unified IP Phone 7925

7926

Cisco Unified IP Phone 7926

7931

Cisco Unified IP Phone 7931

7935

Cisco Unified IP Phone 7935

7936

Cisco Unified IP Phone 7936

7937

Cisco Unified IP Phone 7937

7940

Cisco Unified IP Phone 7940

7941

Cisco Unified IP Phone 7941

7941GE

Cisco Unified IP Phone 7941GE

7942

Cisco Unified IP Phone 7942

7945

Cisco Unified IP Phone 7945

7960

Cisco Unified IP Phone 7960

7961

Cisco Unified IP Phone 7961

7961GE

Cisco Unified IP Phone 7961GE

7962

Cisco Unified IP Phone 7962

7965

Cisco Unified IP Phone 7965

7970

Cisco Unified IP Phone 7970

7971

Cisco Unified IP Phone 7971

7975

Cisco Unified IP Phone 7975

7985

Cisco Unified IP Phone 7985

CIPC

CIPC

IP-STE

IP-STE

anl

anl

ata

ata

bri

bri

vgc-phone

vgc-phone

max-lines

Maximum lines setting. The range is from 1 to 34.

### Command Default

No default behavior or values.

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(2)XT

Cisco SRST 2.0

This command was introduced on the following platforms:
                                          						Cisco 1750, Cisco 1751, Cisco 2600 series and Cisco 3600 series multiservice
                                          						routers, and Cisco IAD2420 series IADs.

12.2(8)T

Cisco SRST 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers.

12.2(8)T1

Cisco SRST 2.0

This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers.

12.2(11)T

Cisco SRST 2.01

This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers.

### Usage Guidelines

The limit-dn command specifies the maximum number
                              		  of lines (directory numbers) available for each Cisco IP phone type.

The range of the maximum number of lines is from 1 to 34. If there is
                              		  any active phone with a number greater than the specified limit, warning
                              		  information is displayed for phone reset.

## Examples

The following example shows how to set a directory number limit of 2
                              		  for the Cisco Unified IP Phone 7910:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# limit-dn 7910 2
```

### Related Commands

Command

Description

call-manager-fallback

Enables Cisco Unified SRST support and enters
                                          						call-manager-fallback configuration mode.

## listen-port (SIP)

To configure the listen ports used for SIP protocols, use the listen-port command in voice service voip/sip configuration mode. To reset port use to its default value, use the no form of this command.

listen-port [ non-secure | secure | secure no-client-validation ] port-number

no listen-port [ non-secure | secure | secure no-client-validation ]

### Syntax Description

secure

Specifies the TLS port value.

non-secure

Specifies the TCP/UDP port value.

no-client-validation

Disables mTLS and available only for secure ports.

port-number

Port number. Range: 1–65535. The default for UDP/TCP is 5060; the default for TLS is 5061.

### Command Default

The port number is set to the default value based on the transport layer protocol used.

### Command Modes

SIP configuration mode (config-serv-sip)

## Command History

Release

Modification

12.4(15)XY

This command was introduced.

12.4(20)T

This command was integrated into Cisco IOS Release 12.4(20)T.

Cisco IOS XE Cupertino
                                                17.8.1a

Enhanced listen-port secure command to disable validation of client certificate and configure TLS port for SIP OAuth-based registrations from remote
                                          SIP endpoints.

### Usage Guidelines

The listen-port command is configurable on incoming SIP calls, and is applicable for both TDM-IP gateway and CUBE (IPIPGW). The CUBE gateway port number defined in global configuration will be used for incoming call legs. Before configuring the SIP listen
                              port for TCP/UDP/TLS, the SIP service should be shut down using the shutdown command in SIP configuration mode. If the SIP service is not shut down, the listen-port command flashes an error message saying "shutdown SIP service before changing SIP listen port". This ensures that there are
                              no active calls when the SIP listen port is changed. The non-secure keyword is supported with all IOS images, and both the secure and non-secure keywords are supported with licensed Crypto images.

From Cisco IOS XE Cupertino
                                    17.8.1a onwards, listen-port secure is modified to create a different TLS port to listen to SIP OAuth registration and disable validation of client certificate.

The following restrictions apply:

Configuring the SIP listen port on a dial-peer basis is not supported.

Configuring same listening port for both UDP/TCP and TLS is not allowed.

Configuring the SIP listen port to a port that is already in use is not supported and results in an error message.

Changing SIP listen port when Transport services (TCP/UDP/TLS) are shut down, will not close or reopen the port. The result
                                    is that only the new port number is updated. The new port will be bound when Transport services (TCP/UDP/TLS) is enabled.

## Examples

The following example shows the port number on a Crypto image being changed to port 2000:

```
Router(config-serv-sip)# listen-port secure 10000
```

The following example shows the port number being reset to the TLS default port:

```
Router(config-serv-sip)# no listen-port
```

The following example shows listen-port secure that is modified to create a different TLS port to listen to SIP OAuth registration and disable validation of client certificate:

```
Router(config)#voice service voip
Router(conf-voi-serv)#sip
Router(conf-serv-sip)#listen-port ?
  non-secure  Change UDP/TCP SIP listen Port
  secure      Change TLS SIP listen Port

Router(conf-serv-sip)# listen-port secure ?
<0-65535>             Listen port for mTLS service
no-client-validation  TLS service without client validation

Router(conf-serv-sip)# listen-port secure no-client-validation ?
<cr>           Use default port 5090
<1024-49151>   Specify TLS listen-port
Router(conf-serv-sip)#
```

### Related Commands

Command

Description

shutdown

Disables the port.

## location (voice emergency response zone)

To include a location within an emergency response zone, use the location command in voice emergency response
                              		  zone mode. To assign specific priorites to the locations, use the priority tag.
                              		  To remove the location, use the no form of this command.

location location-tag [priority <1-100>]

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

### Usage Guidelines

This command creates locations within emergency response zones. The
                              		  tag must be the same as the tag that is defined using the voice emergency response location command. This allows routing of 911 calls
                              		  to different PSAPs. Priority is optional and allows searching locations in a
                              		  specified priority order. If there are locations with assigned priorities and
                              		  locations configured without priorities, the prioritized locations are searched
                              		  before those without an assigned priority.

## Examples

The following example shows an assignment of ERLs to two zones, 10
                              		  and 11, to route callers to two different PSAPs. The locations for ERLs in zone
                              		  10 are searched in sequential order for a phone address match. The calls from
                              		  zone 10 have an ELIN from ERLs 8, 9, and 10. The calls from zone 11 have an
                              		  ELIN from ERLs 2, 3, 4, and 5. The locations for ERLs in zone 11 have
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

### Usage Guidelines

This command enables syslog messages to be announced for every 911
                              		  emergency call that is made. The syslog messages can be used by third party
                              		  applications to send pager or e-mail notifications to an in-house support
                              		  number. This command is optional and is enabled by default.

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

Number of minutes a 911 call is associated to an ELIN in
                                          						case of a callback from the 911 operator.

voice emergency response settings

Creates a tag for identifying settings for E911 behavior.

## max registrations (voice register pool)

To set the maximum number of registrations accepted by the voice
                              		  register pool, use the max registrations command in voice register pool
                              		  configuration mode. To disable registration setup, use the no form of this command.

max registrations value

no max registrations

### Syntax Description

value

Digit, beginning with 0, that represents the maximum number
                                          						of registrations. The maximum registration value is platform dependent.

### Command Default

The maximum number of IP phones that can be configured per platform

### Command Modes

Voice register pool configuration

## Command History

Release

Modification

12.2(15)ZJ

This command was introduced.

12.3(4)T

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

12.4(4)T

This command was removed.

### Usage Guidelines

The id (voice register pool) command must be configured before any
                              		  other voice register pool commands, including the max registrations command. The id command identifies a locally available
                              		  individual Cisco SIP IP phone or sets of Cisco SIP IP phones.

If two phones attempt to register the same phone number, only the
                              		  first phone can register the number. You can control which phone is accepted by
                              		  using multiple voice register pools. In general, the best usage is one pool per
                              		  phone; with multiple pools, some flexibility is granted.

## Examples

The following partial sample output from the show running-config command shows that 5 is the maximum number of SIP telephone
                              		  registrations accepted.

```
voice register pool 3
 id network 10.2.161.0 mask 255.255.255.0
 number 1 95... preference 1
 cor outgoing call95 1 95011
 max registrations 5
 voice-class codec 1
```

### Related Commands

Command

Description

id (voice register pool)

Explicitly identifies a locally available individual Cisco
                                          						SIP IP phone or set of Cisco SIP IP phones.

voice register pool

Enables SIP SRST voice register pool configuration
                                          						commands.

## max-conferences (call-manager-fallback)

To set the maximum number of simultaneous three-party conferences
                              		  supported by the router, use the max-conferences command in call-manager-fallback configuration mode. To return
                              		  to the default number of conferences, use the no form of this command.

max-conferences max-no-of-conferences [gain -6 |0 |3 | 6]

no max-conferences max-no-of-conferences

### Syntax Description

max-no-of-conferences

The maximum number of simultaneous three-party conferences
                                          						allowed by the router. The maximum number of three-party conferences is
                                          						platform dependent:

- Cisco 1751
                                             						  router—8

- Cisco 1760
                                             						  router—8

- Cisco 2600
                                             						  series routers—8

- Cisco 2600-XM
                                             						  series routers—8

- Cisco 2801
                                             						  router—8

- Cisco 2811,
                                             						  Cisco 2821, and Cisco 2851 routers—16

- Cisco 3640 and
                                             						  Cisco 3640A routers—8

- Cisco 3660
                                             						  router—16

- Cisco 3725
                                             						  router—16

- Cisco 3745
                                             						  router—16

- Cisco 3800
                                             						  series router—24

gain

(Optional) Increases the sound volume of VoIP and public
                                          						switched telephony network (PSTN) parties joining a conference call. The
                                          						allowable decibel units are -6 db, 0 db, 3 db, and 6 db. The default is -6 db.

### Command Default

The default is half of the number of maximum simultaneous three-party
                              		  conferences allowed per platform.

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco SRST 3.0

This command was introduced.

12.3(4)T

Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

12.3(8)T4

Cisco SRST 3.1

The Cisco 2800 series routers were added.

12.3(11)T

Cisco SRST 3.2

The Cisco 3800 series routers were added.

12.3(11)XL

Cisco SRST 3.2.2

The gain keyword was added.

### Usage Guidelines

The max-conferences command supports three-party
                              		  conferences for local and on-net calls only when all conference participants
                              		  are using the G.711 codec. Conversion between G.711 u-law and a-law is
                              		  supported. Mixing of the media streams is supported by the Cisco IOS processor.
                              		  The maximum number of simultaneous conferences is limited to the
                              		  platform-specific maximum.

The gain keyword's functionality is applied to
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
Router(config)# call-manager-fallback Router(config-cm-fallback)# max-conferences 4 gain 6
```

### Related Commands

Command

Description

call-manager-fallback

Enables Cisco Unified SRST support and enters
                                          						call-manager-fallback configuration mode.

## max-dn (call-manager-fallback)

To set the maximum possible number of directories or virtual voice
                              		  ports that can be supported by a router and to activate dual-line mode,
                              		  octo-line mode, or both modes, use the max-dn command in call-manager-fallback
                              		  configuration mode. To return to the default number of directories or virtual
                              		  voice ports and to deactivate the dual-line mode or octo-line mode, use the no form of this command.

max-dn max-no-of-directories [ dual-line | octo-line ] [ preference preference-order ] [ number octo-line ]

no max-dn

### Syntax Description

max-no-of-directories

Maximum number of directory numbers (dns) or virtual voice
                                          						ports supported by the router. The maximum possible number is
                                          						platform-dependent; see the Cisco IOS command-line interface (CLI) help. The
                                          						default is 0 directory numbers and 1 channel per virtual port.

dual-line

(Optional) Sets all Cisco Unified IP phones connected to a
                                          						Cisco Unified SRST router to one virtual voice port with two channels.

octo-line

(Optional) Sets all Cisco Unified IP phones connected to a
                                          						Cisco Unified SRST router to one virtual voice port with eight channels.

preference preference-order

(Optional) Sets the global preference for creating the VoIP
                                          						dial peers for all directory numbers that are associated with the primary
                                          						number. Range is from 0 to 10. Default is 0, which is the highest preference.

number octo-line

(Optional) Sets the maximum number of octo-line directory
                                          						numbers.

### Command Default

0 directory numbers, 1 channel per virtual port, 8 channels per
                              		  virtual port, 0 preference, 8 numbers

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.1(5)YD

Cisco SRST 1.0

This command was introduced on the following platforms:
                                          						Cisco 2600 series and Cisco 3600 series multiservice routers, and Cisco IAD2420
                                          						series IADs.

12.2(2)XT

Cisco SRST 2.0

This command was implemented on Cisco 1750 and Cisco 1751
                                          						multiservice routers.

12.2(8)T

Cisco SRST 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers.

12.2(8)T1

Cisco SRST 2.0

This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers.

12.2(11)T

Cisco SRST 2.01

This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers.

12.2(15)ZJ

Cisco SRST 3.0

The dual-line keyword was added.

12.3(4)T

Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

12.3(11)T

Cisco SRST 3.2

The preference keyword was added.

12.4(15)XZ

Cisco Unified SRST 4.3

The octo-line keyword and its number argument were added.

12.4(20)T

Cisco Unified SRST 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

The max-dn command limits the number of Cisco
                              		  Unified IP phone directory numbers or virtual voice ports available on the
                              		  router.

The dual-line keyword facilitates call waiting,
                              		  call transfer, and conference functions by allowing two calls to occur on one
                              		  line simultaneously. In dual-line mode, all Cisco Unified IP phones on the
                              		  Cisco Unified SRST router support two channels per virtual voice port.

The octo-line keyword facilitates call waiting,
                              		  call transfer, and conference functions by allowing eight calls to occur on one
                              		  line simultaneously. In octo-line mode, all Cisco Unified IP phones on the
                              		  Cisco Unified SRST router support eight channels per virtual voice port.

During Cisco Unified SRST registration, a dial peer is created and
                              		  that dial peer includes a default preference. The preference keyword allows you to change the default value, if desired.

Setting the preference enables the desired dial peer to be selected
                              		  when multiple dial peers within a hunt group are matched for a dial string.

The alias command also has a preference keyword that sets alias command preference values. Setting the alias command preference keyword allows the default
                              		  preference set with the max-dn command to be overridden. When
                              		  configuring call rerouting with the alias command, set the preference keyword of the max-dn command to a higher numeric preference
                              		  value than the preference set with the alias command.

## Examples

The following example sets the maximum number of directory numbers or
                              		  virtual voice ports to 12, activates dual-line mode, activates octo-line mode,
                              		  and sets the maximum number of dns for octo-mode to 6:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# max-dn 12 dual-line preference 1 octo-line 6
```

### Related Commands

Command

Description

alias (call-manager- fallback)

Provides a mechanism for rerouting calls to telephone
                                          						numbers that are unavailable during Cisco Unified Communications Manager
                                          						fallback.

call-forward busy (call-manager- fallback)

Configures call forwarding to another number when a Cisco
                                          						Unified IP phone is busy.

call-forward noan (call-manager- fallback)

Configures call forwarding to another number when no answer
                                          						is received from a Cisco Unified IP phone.

call-manager-fallback

Enables Cisco Unified SRST feature support and enters
                                          						call-manager-fallback configuration mode.

huntstop (call-manager- fallback)

Sets the huntstop attribute for the dial peers associated
                                          						with a Cisco Unified IP phone during Cisco Unified Communications Manager
                                          						fallback.

huntstop chan num (call-manager- fallback)

Sets the huntstop attribute for the dial peers, for
                                          						dual-line mode or octo-line mode (or both), associated with a Cisco Unified IP
                                          						phone during Cisco Unified Communications Manager fallback.

max-conferences (call- manager-fallback)

Sets the maximum number of simultaneous three-party
                                          						conferences supported by the router.

preference (dial-peer)

Indicates the preferred order of a dial peer within a hunt
                                          						group.

transfer-pattern

Allows Cisco Unified IP phones to transfer telephone calls
                                          						from callers outside the local IP network to another Cisco Unified IP phone.

transfer-system (call- manager-fallback)

Specifies the call transfer method for all Cisco Unified IP
                                          						phones on a Cisco Unified SRST router using the ITU-T H.450.2 standard.

## max-dn (voice register global)

To set the maximum number of SIP phone directory numbers (extensions) that are supported by a Cisco router, use the max-dn command in voice register global configuration mode. To reset to the default, use the no form of this command.

max-dn max-directory-numbers

no max-dn

### Syntax Description

max directory numbers

Maximum number of extensions (ephone-dns) supported by the Cisco router. The maximum number is version and platform dependent;
                                          type ? to display range.

In Cisco CME 3.4 to Cisco Unified CME 7.0 and in Cisco SIP SRST 3.4 to Cisco Unified SIP SRST 7.0: Default is maximum number
                                                supported by platform.

In Cisco Unified CME 7.1 and Cisco Unified SIP SRST 7.1 and later versions: Default is 0.

### Command Default

Before Cisco Unified CME 7.1 and Cisco Unified SIP SRST 7.1, default is maximum number supported by platform.

In Cisco Unified CME 7.1 and Cisco Unified SIP SRST 7.1 and later versions, default is 0.

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

This command was integrated into Cisco IOS release 12.4(24)T.

Cisco Unified SIP SRST 12.8

Introduced support for YANG models.

### Usage Guidelines

This command limits the number of SIP phone directory numbers (extensions) available in a Cisco Unified CME system. The max-dn command is platform specific. It defines the limit for the voice register dn command. The max-pool command similarly limits the number of SIP phones in a Cisco CME system.

You can increase the number of allowable extensions to the maximum; but after the maximum allowable number is configured,
                              you cannot reduce the limit without rebooting the router. You cannot reduce the number of allowable extensions without removing
                              the already-configured directory numbers with dn-tags that have a higher number than the maximum number to be configured.

## Examples

The following example shows how to set the maximum number of directory numbers to 48:

```
Router(config)# voice register global Router(config-register-global)# max-dn 48
```

### Related Commands

Command

Description

voice register dn

Enters voice register dn configuration mode to define an extension for a SIP phone line.

max-pool (voice register global)

Sets the maximum number of SIP voice register pools that are supported in a Cisco SIP SRST or Cisco CME environment.

## max-pool (voice register global)

To set the maximum number of Session Initiation Protocol (SIP) voice register pools that are supported in Cisco Unified SIP
                              SRST, use the max-pool command in voice register global configuration mode ( voice register global ). To reset the maximum number to the default, use the no form of this command.

max-pool max-voice-register-pools

no max-pool

### Syntax Description

max-voice-register-pools

Maximum number of SIP voice register pools supported by the Cisco router. The upper limit of voice register pools is platform-dependent;
                                          type ? for range.

### Command Modes

Voice register global configuration (config-register-global)

## Command History

Cisco IOS Release

Modification

Cisco IOS XE Release 17.2.1v

Command qualified for use in Cisco vManage CLI templates.

Introduced support for YANG models.

### Usage Guidelines

This command limits the number of SIP phones that are supported by Cisco Unified SIP SRST. The max-pool command is platform-specific and defines the limit for the voice register pool command.

The max-dn command similarly limits the number of directory numbers (extensions) in Cisco Unified SIP SRST.

## Examples

```
voice register global
  max-dn   200
  max-pool 100
  system message "SRST mode"
```

### Related Commands

Command

Description

voice register dn

Enters voice register dn configuration mode to define an
                                          						extension for a SIP phone line.

max-dn (voice register global)

Sets the maximum number of SIP voice register pools that
                                          						are supported in a Cisco SIP SRST or Cisco CME environment.

## max-ephones (call-manager-fallback)

To configure the maximum number of Cisco IP phones that can be
                              		  supported by a router, use the max-ephones command in call-manager-fallback
                              		  configuration mode. To return to the default number of Cisco IP phones, use the no form of this command.

max-ephones max-no-of-phones

no max-ephones

### Syntax Description

max-no-of-phones

Maximum number of Cisco IP phones supported by the router.
                                          						The maximum possible number is platform-dependent; refer to Cisco IOS
                                          						command-line interface (CLI) help. The default is 0.

### Command Default

0 Cisco IP phones

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.1(5)YD

Cisco SRST 1.0

This command was introduced on the following platforms:
                                          						Cisco 2600 series and Cisco 3600 series multiservice routers, and Cisco IAD2420
                                          						series IADs.

12.2(2)XT

Cisco SRST 2.0

This command was implemented on Cisco 1750 and Cisco 1751
                                          						multiservice routers.

12.2(8)T

Cisco SRST 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers.

12.2(8)T1

Cisco SRST 2.0

This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers.

12.2(11)T

Cisco SRST 2.01

This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers.

### Usage Guidelines

The max-ephones command limits the number of
                              		  Cisco IP phones supported on the router.

## Examples

The following example sets the maximum number of Cisco IP phones for
                              		  a Cisco router to 24:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# max-ephones 24
```

### Related Commands

Command

Description

call-manager-fallback

Enables Cisco Unified SRST feature support and enters
                                          						call-manager-fallback configuration mode.

## maximum bit-rate (cm-fallback-video)

To set the maximum IP phone video bandwidth, use the maximum bit-rate command in call-manager-fallback video configuration mode. To
                              		  restore the default maximum bit-rate, use the no form of this command.

maximum bit-rate value

no maximum bit-rate

### Syntax Description

value

Sets the maximum IP phone video bandwidth, in kbps. The
                                          						range is 0 to 10000000. The default value is 10000000.

### Command Default

Maximum bit-rate is 1000000.

### Command Modes

Call-manager-fallback video configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)XC

Cisco Unified SRST 4.0

This command was introduced.

### Usage Guidelines

Use this command to set the maximum bit-rate for all video-capable
                              		  phones in a Cisco Unified SRST system.

## Examples

The following example sets a maximum bit-rate of 256 kbps.

```
Router(config)# call-manager-fallback Router(config-call-manager-fallback)# video Router(conf-cm-fallback-video)# maximum bit-rate 256
```

### Related Commands

Command

Description

maximum bit-rate (telephony-service)

Sets the maximum bit-rate for all video-capable phones
                                          						associated with a Cisco Unified CME router.

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
                                          						of presentation lines. Range: 1 to 100. Default: 0. See Table 1 for the number of presentation lines supported by each phone type.

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

num-buttons

max-presentation

Cisco
                                          					 Unified IP Conference Station 7937G

431

1

6

Nokia E61

376

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

## mode esrst

To enable Enhanced
                              		  SRST mode with additional feature support for SCCP phones, use the mode esrst command. To disable the ESRST mode, use the no form of
                              		  this command.

mode esrst

no mode esrst

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

By default, ESRST
                              		  mode is disabled.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

This
                                       					 command was introduced.

### Usage Guidelines

This command
                              		  enables the enhanced SRST mode for SCCP phones.

## Examples

The following
                              		  example shows that esrst mode is enabled:

```
Router(config)# telephony-service Router(config-telephony)# mode esrst
```

### Related Commands

Command

Description

telephony-service

Enters
                                          						telephony-service configuration mode.

voice register global

Enters
                                          						voice register global configuration mode.

## moh (call-manager-fallback)

To enable music on hold (MOH), use the moh command in call-manager-fallback
                              		  configuration mode. To disable music on hold, use the no form of this command.

moh filename

no moh filename

### Syntax Description

filename

Filename of the music file. The music file must be in the
                                          						system flash.

### Command Default

MOH is enabled.

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(2)XT

Cisco SRST 2.0

This command was introduced on the following platforms:
                                          						Cisco 1750, Cisco 1751, Cisco 2600 series and Cisco 3600 series multiservice
                                          						routers, Cisco IAD2420 series IADs.

12.2(8)T

Cisco SRST 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers.

12.2(8)T1

Cisco SRST 2.0

This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers.

12.2(11)T

Cisco SRST 2.01

This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers.

Cisco Unified SIP SRST 12.8

Introduced support for YANG models.

### Usage Guidelines

The moh command allows you to specify the .au and
                              		  .wav format music files that are played to callers who have been put on hold.
                              		  MOH works only for G.711 calls and on-net VoIP and PSTN calls. For all other
                              		  calls, callers hear a periodic tone. For example, internal calls between Cisco
                              		  IP phones do not get MOH; instead callers hear a tone.

MOH can be used as a fallback MOH source when using MOH live feed.
                              		  See the moh-live (call-manager-fallback) command for more information.

## Examples

The following example enables MOH and specifies the music files:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# moh minuet.wav Router(config-cm-fallback)# moh minuet.au
```

### Related Commands

Command

Description

call-manager-fallback

Enables Cisco Unified SRST support and enters
                                          						call-manager-fallback configuration mode.

moh-live (call- manager-fallback)

Specifies that a particular telephone number is to be used
                                          						for an outgoing call that is to be the source for an MOH stream for SRST.

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

V oice moh-group configuration (config-voice-moh-group)

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

## moh-file-buffer (cm-fallback)

To specify a MOH file buffer size, use the moh-file-buffer command in call-manager-fallback configuration mode. To delete
                              		  the moh-file-buffer size, use the no form of this command.

moh-file-buffer file_size

no moh-file-buffer

### Syntax Description

file_size

Specifies a numeric value for the buffer MOH file size
                                          						between 64 KB and 10000 KB.

### Command Default

No moh-file buffer is configured.

### Command Modes

Call-manager-fallback configuration (config-cm-fallback)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.0(1)XA

Cisco Unified SRST 8.0

This command was introduced.

15.1(1)T

Cisco Unified SRST 8.0

This command was integrated into Cisco IOS Release
                                          						15.1(1)T.

### Usage Guidelines

This command allows to set a buffer MOH file size limit for new MOH
                              		  files. You can allocate a MOH file buffer size between 64 KB (8 seconds ) and
                              		  10000 KB (20 minutes, approximately). A large buffer size is desirable to cache
                              		  the largest MOH file and better MOH performance. During memory allocation the
                              		  buffer size is aligned to 16KB. For more information on MOH file caching, see
                              		  show ephone moh command.

The default maximum file buffer size is 64 KB. If the MOH file size
                              		  is too large, it cannot be cached and the buffer size falls back to 64 KB.

## Examples

The following example shows a moh-file-buffer size of 2000 KB
                              		  assigned for future moh files under the call-manager-fallback configuration
                              		  mode.

```
!
!
!
!
call-manager-fallback
 max-conferences 8 gain -6
 transfer-system full-consult
 moh-file-buffer 2000
!
!
line con 0
 exec-timeout 0 0
line aux 0
 --More--
```

### Related Commands

Command

Description

moh-group

Allows to configure a MOH group.

moh

Enables music on hold from a flash audio feed

multicast moh

Enables multicast of the music-on-hold audio stream.

extension-range

Specifies the extension range for a clients calling a
                                          						voice-moh-group.

## moh-live (call-manager-fallback)

To specify that a particular telephone number is to be used for an
                              		  outgoing call that is to be the source for a music on hold (MOH) stream for
                              		  SRST, use the moh-live command in call-manager-fallback
                              		  configuration mode. To disable the source for the MOH stream, use the no form of this command.

moh-live dn-number calling-number out-call outcall-number

no moh-live dn-number calling-number out-call outcall-number

### Syntax Description

dn-number calling-number

Sets the MOH telephone number. The calling-number is a sequence of
                                          						digits that represent a telephone number.

out-call outcall-number

Indicates that the router is calling out for a live feed
                                          						that is to be used for MOH and specifies the number to be called. The outcall-number is a sequence of
                                          						digits that represent a telephone number, typically of an E&M port.

### Command Default

No default behavior or values.

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(11)T

Cisco SRST 3.3

This command was introduced.

### Usage Guidelines

The moh-live command in SRST mode provides
                              		  live-feed MOH streams from an audio device connected to an E&M or FXO port
                              		  to Cisco IP phones.

During SRST, do not change an existing moh-live command. Instead, first remove the
                              		  existing command, and then add in the new command.

To configure MOH from a live feed, you first establish a voice port
                              		  and dial peer for the call and then create a “dummy” phone or directory number.
                              		  The dummy number allows for making and receiving calls, but the number is not
                              		  assigned to a physical phone. It is that number that the MOH system
                              		  automatically dials to establish the MOH feed.

The moh-live command allocates one of the virtual
                              		  voice ports from the pool of virtual voice ports created by the max-dn command. The virtual voice port places
                              		  an outgoing call to the dummy number; that is, the directory number specified
                              		  in the moh-live command. The audio stream obtained
                              		  from the MOH call provides the music-on-hold audio stream.

To activate MOH live feed, set up and connect the physical voice
                              		  port. After setting up the voice port, create a dial peer and give the voice
                              		  port a directory number with the destination-pattern command. The directory
                              		  number is the number that the system uses to access the MOH. To establish the
                              		  MOH feed, connect the music source, such as a CD player to autodial the
                              		  directory number.

MOH can be used as a fallback MOH source when using MOH live feed.
                              		  See the moh (call-manager-fallback) command for more information.

## Examples

The following example configures MOH from a live feed. Note that the
                              		  dial peer references the E&M port that was set with the voice-port command and that the dial-peer number (7777) matches the
                              		  out-call value of the m oh-live command.

```
.
.
.
voice-port 1/0/0
 input gain 3
 auto-cut-through
 operation 4-wire
 signal immediate
!
dial-peer voice 7777 pots
 destination-pattern 7777
 port 2/0/0
!
!
call-manager-fallback
 max-conferences 8
 max-dn 1
 moh-live dn-number 3333 out-call 7777
!
.
.
.
```

### Related Commands

Command

Description

call-manager-fallback

Enables Cisco Unified SRST support and enters
                                          						call-manager-fallback configuration mode.

destination-pattern

Specifies either the prefix or the full E.164 telephone
                                          						number to be used for a dial peer.

moh (call-manager-fallback)

Enables MOH.

## multicast moh (call-manager-fallback)

To enable continuous IP multicast output of music on hold (MOH) from
                              		  a flash MOH file in a branch Cisco Unified SRST router, use the multicast moh command in call-manager-fallback configuration
                              		  mode. To disable continuous IP multicast output of MOH from a flash MOH file in
                              		  a branch Cisco Unified SRST router, use the no form of this command.

multicast moh multicast-address port port [ route ip-address-list ]

no multicast moh multicast-address port port [ route ip-address-list ]

### Syntax Description

multicast-address

Declares the multicast-address header value of the MOH
                                          						packets that are to be multicast.

port

Declares the port header value of the MOH packets that are
                                          						to be multicast.

port

The desired port number.

route

(Optional) Sets the explicit IP address or addresses from
                                          						which the multicast packets will be transmitted.

ip-address-list

(Optional) Declares the IP address or addresses. The
                                          						ip-address-list argument accepts a maximum of four IP address entries separated
                                          						by a space.

### Command Default

If the route keyword is not in the multicast moh command, the ip source-address command value configured for Cisco
                              		  Unified SRST will be used.

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco SRST 3.0

This command was introduced.

12.3(4)T

Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

MOH multicast operates during Cisco Unified Communications Manager
                              		  fallback and normal Cisco Unified Communications Manager service.

Because all branch IP phones are instructed by the central Cisco
                              		  Unified Communications Manager to select and multicast a specific MOH feed, you
                              		  must configure the IP address and port header values to match the MOH multicast
                              		  IP address and port used by the central Cisco Unified Communications Manager’s
                              		  MOH. This makes the MOH from Cisco Unified SRST router appear as if it were
                              		  coming from the central Cisco Unified Communications Manager.

MOH multicast operates with both MOH and MOH live input sources.

## Examples

The following example provides multicast MOH output to the IP phones
                              		  local to SRST. The MOH packets are broadcast to the 239.10.20.30 multicast
                              		  address using port 2000. The MOH packets use the ip source-addres s command
                              		  value configured for Cisco Unified SRST. MOH packets are output only through
                              		  the router interface that matches the SRST router's IP source-address:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# moh music-on-hold-file.au Router(config-cm-fallback)# multicast moh 239.10.20.30 port 2000
```

The following example provides multicast MOH output to the IP phones
                              		  local to SRST. The MOH packets are broadcast to the 239.10.20.30 multicast
                              		  address using port 2000. The MOH packets use the ip source-address command value configured for Cisco
                              		  Unified SRST. MoH packets are output only through the router interfaces that
                              		  match the IP addresses listed using the route keyword option:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# moh music-on-hold-file.au Router(config-cm-fallback)# multicast moh 239.10.20.30 port 2000 route 10.10.20.1 10.10.21.1 10.10.22.1 10.10.23.1
```

### Related Commands

Command

Description

call-manager-fallback

Enables Cisco Unified SRST and enters call-manager-fallback configuration
                                          						mode.

ip source-address (call-manager- fallback)

Enables a router to receive messages from Cisco IP phones
                                          						through the specified IP addresses and ports.

moh (call-manager- fallback)

Enables MOH.

moh-live ( call- manager-fallback)

Specifies that a particular telephone number is to be used
                                          						for an outgoing call that is to be the source for an MOH stream for SRST.

## mwi expires (call-manager-fallback)

Effective with Cisco IOS Releases 12.3(11)T7 and 12.4, the mwi expires command was replaced with the mwi-server command in SIP user-agent
                              		  configuration mode.

To set the expiration timer for registration for the message-waiting
                              		  indication (MWI) client or server, use the mwi expires command in call-manager-fallback configuration mode. To disable
                              		  the timer, use the no form of this command.

mwi expires seconds

no mwi expires seconds

### Syntax Description

seconds

Expiration time, in seconds. Range is from 600 to 99999.
                                          						Default is 86400 (24 hours).

### Command Default

86400 seconds (24 hours)

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco SRST 3.0

This command was introduced.

12.3(4)T

Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

12.3(11)T7 12.4

Cisco SRST 3.3

This command was replaced by the mwi-server command in SIP
                                          						user-agent configuration mode.

## Examples

The following example sets the expiration timer to 1000 seconds:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# mwi expires 1000
```

### Related Commands

Command

Description

mwi relay (call-manager-fallback)

Enables a Cisco Unified SRST router to relay MWI
                                          						notification to remote Cisco IP phones.

## mwi reg-e164 (call-manager-fallback)

To register E.164 numbers rather than extension numbers with a
                              		  Session Interface Protocol (SIP) proxy or registrar, use the mwi reg-e164 command in call-manager-fallback
                              		  configuration mode. To return to the default, use the no form of this command.

mwi reg-e164

no mwi reg-e164

### Syntax Description

This command has no keywords or arguments.

### Command Default

Registering extension numbers with the SIP proxy or registrar.

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(11)T7 12.4

Cisco SRST 3.3

This command was introduced.

### Usage Guidelines

This command is used when setting up extensions to use an external
                              		  SIP-based message-waiting indication (MWI) server. The mwi-server command in SIP user-agent
                              		  configuration mode specifies other settings for MWI service.

## Examples

The following example specifies that E.164 numbers should be used for
                              		  registration with the SIP proxy or registrar:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# mwi reg-e164
```

### Related Commands

Command

Description

mwi-server (SIP user-agent)

Specifies voice-mail server settings on a voice gateway or
                                          						user agent (UA).

## mwi relay (call-manager-fallback)

To enable a Cisco Unified SRST router to relay message-waiting
                              		  indication (MWI) notification to remote Cisco IP phones, use the mwi relay command in call-manager-fallback configuration mode. To disable
                              		  MWI relay, use the no form of this command.

mwi relay

no mwi relay

### Syntax Description

This command has no arguments or keywords.

### Command Default

MWI is not enabled.

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco SRST 3.0

This command was introduced.

12.3(4)T

Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

Use this command to enable the Cisco Unified SRST router to relay MWI
                              		  notification to remote Cisco IP phones. The router at the central site acts as
                              		  a notifier after this command is used.

## Examples

The following example enables MWI relay:

```
Router(config)# call-manager-fallback Router(config-cm-fallback)# mwi relay
```

### Related Commands

Command

Description

mwi expires (call-manager- fallback)

Sets the expiration timer for registration for the client
                                          						or the server.

## mwi sip-server (call-manager-fallback)

Effective with Cisco IOS Releases 12.3(11)T7 and 12.4, the mwi sip-server command was replaced with the mwi-server command in SIP user-agent
                              		  configuration mode and the mwi reg-e164 command in call-manager-fallback
                              		  configuration mode.

To configure the IP address and port number for an external SIP-based
                              		  message-waiting indication (MWI) server, use the mwi sip-server command in call-manager-fallback configuration mode. To disable
                              		  the MWI server functionality, use the no form of this command.

mwi sip-server ip-address [ transport tcp | transport udp ] [ port port-number ] [ reg-e164 ] [ unsolicited ]

no mwi sip-server ip-address

### Syntax Description

ip-address

IP address of the MWI server.

transport tcp

(Optional) Selects TCP as the transport layer protocol.
                                          						This is the default transport protocol.

transport udp

(Optional) Selects UDP as the transport layer protocol.

port port-number

(Optional) Specifies port number for the MWI server. Range
                                          						is from 2000 to 9999. Default is 5060.

reg-e164

(Optional) Registers an E.164 number with a Session
                                          						Interface Protocol (SIP) proxy or registrar rather than an extension number.
                                          						Registering with an extension number is the default.

unsolicited

(Optional) Sends SIP NOTIFY for MWI without any need to
                                          						send a SUBSCRIBE from the Cisco Unified SRST router.

### Command Default

Transport layer protocol: TCP Port number: 5060 (SIP standard port)
                              		  Registration: with an extension number

### Command Modes

Call-manager-fallback configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco SRST 3.0

This command was introduced.

12.3(4)T

Cisco SRST 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

12.3(11)T7 12.4

Cisco SRST 3.3

This command was replaced by the mwi-server command in SIP
                                          						user-agent configuration mode and the mwi reg-e164 command in
                                          						call-manager-fallback configuration mode.

### Usage Guidelines

Use this command to configure the IP address of an external SIP MWI
                              		  server.

The transport tcp keyword is the default setting. The transport udp keyword allows you to integrate with a SIP MWI
                              		  client. The optional port keyword is used to specify a port number
                              		  other than 5060, the default. The default registration is with an extension
                              		  number, so the reg-e164 keyword allows you to register with
                              		  an E.164 ten-digit number.

## Examples

The following example sets MWI for the SIP server and sets individual
                              		  ephone-dn extension numbers to the MWI SIP server’s notification list:

```
Router(config) call-manager-fallback Router(config-cm-fallback) mwi sip-server 192.168.0.5 transport udp
```

### Related Commands

Command

Description

mwi relay (call-manager-fallback)

Enables a Cisco Unified SRST router to relay MWI
                                          						notification to remote Cisco IP phones.

| fxo | Enables a Foreign Exchange Office (FXO) interface. |
|---|---|
| e&m | Enables an analog ear and mouth (E&M) interface. |
| dial-string | Sets up dial access codes for each specified line type by
                                          						creating dial peers. |
| bri | Enables a BRI interface. |
| pri | Enables a PRI interface. |
| direct-inward-dial | (Optional) Enables direct inward dialing on a POTS dial
                                          						peer. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco Unified SRST 1.0 | This command was introduced on the following platforms:
                                          						Cisco 2600 series and Cisco 3600 series multiservice routers, and Cisco IAD2420
                                          						series IADs. |
| 12.2(2)XT | Cisco Unified SRST 2.0 | This command was implemented on Cisco 1750 and Cisco 1751
                                          						multiservice routers. |
| 12.2(8)T | Cisco Unified SRST 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers. |

| Note | The access-code command creates temporary dial
                                       		  peers during Cisco Unified Communications Manager fallback. In many cases, you
                                       		  may already have the local PSTN ports configured with appropriate access codes
                                       		  provided by dial peers (for example, dial 9 to select an FXO PSTN line), in
                                       		  which case this command is not needed. |
|---|---|

| Command | Description |
|---|---|
| call-manager-fallback | Enables Cisco Unified SRST feature support and enters
                                          						call-manager-fallback configuration mode. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco Unified CME 4.3 Cisco Unified SRST 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| device-id | Specifies the device ID for a phone type in an ephone-type
                                          						template. |
| device-name | Assigns a name to a phone type in an ephone-type template. |

| string | String (1-247 characters) used to identify an ERL’s civic
                                          						address. |
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
| elin | Specifies a PSTN number that will replace the caller’s
                                          						extension. |
| name | Specifies a string (up to 30-characters) used internally to
                                          						identify or describe the emergency response location. |
| subnet | Defines which IP phones are part of this ERL. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 Cisco SRST 3.4 | This command was introduced. |

| Note | The id (voice register pool) command is required before Cisco Unified
                                       		  CME or Cisco Unified SIP SRST can accept registrations. Configure the id (voice register pool) command before any other voice register
                                       		  pool command. |
|---|---|

| Command | Description |
|---|---|
| after-hours block pattern | Defines a pattern of digits for blocking outgoing calls
                                          						from IP phones. |
| after-hours block pattern (call-manager- fallback) | Defines a pattern of digits for blocking outgoing calls
                                          						from IP phones. |
| after-hours date | Defines a recurring period based on date during which
                                          						outgoing calls that match defined block patterns are blocked on IP phones. |
| after-hours date (call-manager- fallback) | Defines a recurring period based on date during which
                                          						outgoing calls that match defined block patterns are blocked on IP phones. |
| after-hours day | Defines a recurring period based on day of the week during
                                          						which outgoing calls that match defined block patterns are blocked on IP
                                          						phones. |
| after-hours day (call-manager- fallback) | Defines a recurring period based on day of the week during
                                          						which outgoing calls that match defined block patterns are blocked on IP
                                          						phones. |
| after-hour exempt (voice register dn) | Specifies that an individual extension on a SIP phone does
                                          						not have any of its outgoing calls blocked even though global system call
                                          						blocking is enabled. |
| call-manager-fallback | Enables Cisco Unified SIP SRST support and enter
                                          						call-manager-fallback configuration mode. |
| id (voice register pool) | Explicitly identifies a locally available individual Cisco
                                          						SIP IP phone, or when running Cisco Unified SIP SRST, set of Cisco Unified SIP
                                          						IP phones. |
| telephony-service | Enters telephony-service configuration mode to configure a
                                          						Cisco Unified Communications Manager Express (Cisco Unified CME) system. |
| voice register dn | Enters voice register dn configuration mode to define an
                                          						extension for a SIP phone line. |
| voice register pool | Enters voice register pool configuration mode for Cisco SIP
                                          						IP phones. |

| pattern- tag | Identifier for a call-blocking pattern. Up to 32
                                          						call-blocking patterns can be defined in separate commands. |
|---|---|
| pattern | Outgoing call digits to be matched for blocking. |
| 7-24 | (Optional) If the 7-24 keyword is specified, the pattern is always blocked,
                                          						7 days a week, 24 hours a day. If the 7-24 keyword is not specified, the
                                          						pattern is blocked during the days and dates that are defined with the after-hours day and after-hours date commands. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco Unified SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco Unified SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 15.3(2)T | Cisco Unified CME 9.5 | This command was modified to include regular expressions as
                                          						a value for the pattern argument. |

| Note | In SRST (call-manager-fallback configuration) mode, there is no
                                       		  phone- or pin-based exempt to after-hours call blocking. |
|---|---|

| Command | Description |
|---|---|
| after-hours date (call- manager-fallback) | Defines a recurring period based on date during which
                                          						outgoing calls that match defined block patterns are blocked on IP phones. |
| after-hours day (call- manager-fallback) | Defines a recurring period based on day of the week during
                                          						which outgoing calls that match defined block patterns are blocked on IP
                                          						phones. |

| month | Abbreviated month. The following abbreviations for month
                                          						are valid: jan , feb , mar , apr , may , jun , jul , aug , sep , oct , nov , dec . |
|---|---|
| date | Date of the month. Range is from 1 to 31. |
| start-time stop-time | Beginning and ending times for call blocking, in an HH:MM
                                          						format using a 24-hour clock. The stop time must be greater than the start
                                          						time. The value 24:00 is not valid. If 00:00 is entered as a stop time, it is
                                          						changed to 23:59. If 00:00 is entered for both start time and stop time, calls
                                          						are blocked for the entire 24-hour period on the specified date. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco Unified SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco Unified SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Note | In SRST (call-manager-fallback configuration) mode, there is no
                                       		  phone- or pin-based exempt to after-hours call blocking. |
|---|---|

| Command | Description |
|---|---|
| after-hours block pattern (call-manager- fallback) | Defines a pattern of digits for blocking outgoing calls
                                          						from IP phones. |
| after-hours day (call- manager-fallback) | Defines a recurring period based on day of the week during
                                          						which outgoing calls that match defined block patterns are blocked on IP
                                          						phones. |

| month | Abbreviated month. The following abbreviations for month
                                          						are valid: jan , feb , mar , apr , may , jun , jul , aug , sep , oct , nov , dec . |
|---|---|
| date | Date of the month. Range is from 1 to 31. |
| start-time stop-time | Beginning and ending times for call blocking, in an HH:MM
                                          						format using a 24-hour clock. The stop time must be greater than the start
                                          						time. The value 24:00 is not valid. If 00:00 is entered as a stop time, it is
                                          						changed to 23:59. If 00:00 is entered for both start time and stop time, calls
                                          						are blocked for the entire 24-hour period on the specified date. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco Unified SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco Unified SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Note | In SRST (call-manager-fallback configuration) mode, there is no
                                       		  phone- or pin-based exempt to after-hours call blocking. |
|---|---|

| Command | Description |
|---|---|
| after-hours block pattern (call- manager-fallback) | Defines a pattern of digits for blocking outgoing calls
                                          						from IP phones. |
| after-hours day (call- manager-fallback) | Defines a recurring period based on day of the week during
                                          						which outgoing calls that match defined block patterns are blocked on IP
                                          						phones. |

| tag | Identifier for alias rule range. The range is from 1 to 50. |
|---|---|
| number-pattern | Pattern to match the incoming telephone number. This
                                          						pattern may include wildcards. A number-pattern can be used multiple
                                          						times. |
| to | Connects the tag number pattern to the alternate number. |
| alternate-number | Alternate telephone number to route incoming calls to match
                                          						the number pattern. The alternate number has to be a specific extension that
                                          						belongs to an IP phone that is actively registered on the Cisco Unified SRST
                                          						router. The alternate telephone number can be used in multiple alias commands. |
| preference | (Optional) Assigns a dial-peer preference value to the
                                          						alias. Use with the max-dn command. |
| preference-value | (Optional) Preference value of the associated dial peer.
                                          						The range is from 0 to 10. |
| cfw number | (Optional) Allows users to set call forward busy and call
                                          						forward no answer to a set string and override globally configured call forward
                                          						settings. |
| timeout timeout-value | (Optional) Sets the ring no-answer timeout duration for
                                          						call forwarding, in seconds. Range is from 3 to 60000. The cfw keyword assumes that you want
                                          						to forward calls to the same number for both busy and no-answer call forward
                                          						cases. The timeout-value applies only to the no-answer call
                                          						forward case. There is no timeout required for a busy call forward situation. |
| huntstop | (Optional) Stops call hunting after trying the alternate-number . This keyword only
                                          						has an effect if the global command no huntstop is set. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco Unified SRST 2.0 | This command was introduced on the following platforms:
                                          						Cisco 1750, Cisco 1751, Cisco 2600 series and Cisco 3600 series multiservice
                                          						routers, and Cisco IAD2420 series IADs. |
| 12.2(8)T | Cisco Unified SRST 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers. |
| 12.2(8)T1 | Cisco Unified SRST 2.0 | This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers. |
| 12.2(11)T | Cisco Unified SRST 2.01 | This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers. The preference keyword was added. |
| 12.3(11)T | Cisco Unified SRST 3.2 | The cfw keyword was added. The maximum number of alias commands used for creating
                                          						calls to telephone numbers that are unavailable during Cisco Unified
                                          						Communications Manager fallback was increased to 50. The alternate-number argument can be
                                          						used in multiple alias commands. |

| Note | Globally configured settings are selected under
                                       		  call-manager-fallback and apply to all phones that register for SRST service. |
|---|---|

| Note | The alias command supports all port types and
                                       		  obsoletes the default-destination command. The alias
                                       		  command is recommended over the default-destination command. |
|---|---|

| Command | Description |
|---|---|
| call-manager-fallback | Enables Cisco Unified SRST feature support and enters
                                          						call-manager-fallback configuration mode. |
| default-destination | Assigns a default destination number for incoming telephone
                                          						calls on the Cisco Unified SRST router. |
| max-dn (call- manager-fallback) | Sets the maximum possible number of virtual voice ports
                                          						that can be supported by a router and activates dual-line mode. |
| show dialplan number | Displays which outgoing dial peer is reached when a
                                          						particular phone number is dialed. |

| tag | Number from 1 to 5 and the distinguishing factor when there
                                          						are multiple alias commands. |
|---|---|
| pattern | Prefix number that represents a pattern against which to
                                          						match the incoming telephone number. It may include wildcards. |
| to | Connects the number pattern to the target (alternate number). |
| target | Target number. An alternate telephone number to route
                                          						incoming calls that match the number pattern. The target must be a full E.164
                                          						number. |
| preference value | (Optional) Assigns a dial-peer preference value to the
                                          						alias. The value argument is the value of the associated dial
                                          						peer. The range is from 1 to 10. There is no default. |

| Release | Product Version | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SIP SRST 3.0 | This command was introduced to Cisco Unified. |
| 12.3(4)T | Cisco SIP SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Note | The id (voice register pool) command must be configured before any other voice register pool
                                       		  commands, including the alias command. The id command identifies a locally available individual Cisco SIP IP
                                       		  phone or sets of Cisco SIP IP phones. Before the alias command is configured, translation rules must be set using the translate-outgoing (voice register pool) command. Translation rules are a
                                       		  general-purpose number-manipulation mechanism that perform operations such as
                                       		  automatically adding telephone area and prefix codes to dialed numbers. |
|---|---|

| Command | Description |
|---|---|
| id (voice register pool) | Explicitly identifies a locally available individual Cisco
                                          						SIP IP phone or set of Cisco SIP IP phones. |
| show dial-peer voice | Displays information for voice dial peers. |
| translate-outgoing (voice register pool) | Applies a translation rule to manipulate dialed digits on
                                          						an outbound POTS or VoIP call leg. |
| voice register pool | Enables SIP SRST voice register pool configuration
                                          						commands. |

| allow-hash-in-dn | Allow
                                          						the insertion of hash at all places in voice register dn. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 15.6(2)T | Cisco
                                          						SIP SRST 11.0 | This
                                          						command was introduced. |

| Command | Description |
|---|---|
| dial-peer terminator | Configures the character used as a terminator for
                                          						variable-length dialed numbers. |

| application-name | Interactive voice response (IVR) application name. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco Unified SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco Unified SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| call-manager-fallback | Enables Cisco Unified SRST and enters call-manager-fallback
                                          						configuration mode. |

| application-name | Interactive voice response (IVR) application name. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was introduced. |

| Note | Configure the id (voice register pool) command before any other voice register
                                       		  pool commands, including the application command. The id command identifies a locally available
                                       		  individual Cisco SIP IP phone or set of Cisco SIP IP phones. |
|---|---|

| Command | Description |
|---|---|
| application (dial-peer) | Enables a specific application on a dial peer. |
| application (voice register pool) | Selects the session-level application for the dial peer
                                          						associated an individual SIP phone in a Cisco Unified CME environment or for a
                                          						group of phones in a Cisco Unified SIP SRST environment. |
| id (voice register pool) | Explicitly identifies a locally available individual Cisco
                                          						SIP IP phone, or when running Cisco Unified SIP SRST, set of Cisco SIP IP
                                          						phones. |
| mode (voice register global) | Enables the mode for provisioning SIP phones in a Cisco
                                          						Unified CME system. |
| show call application voice summary | Displays information about voice applications. |
| show dial-peer voice | Displays information for dial peers. |
| voice register global | Enters voice register global configuration mode in order to
                                          						set global parameters for all supported Cisco SIP phones in a Cisco Unified CME
                                          						or Cisco Unified SIP SRST environment. |
| voice register pool | Enters voice register pool configuration mode for SIP
                                          						phones. |

| application-name | Name of the selected interactive voice response (IVR)
                                          						application name. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SIP SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SIP SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(4)T | Cisco CME 3.4 and Cisco SIP SRST 3.4 | This command was added to Cisco CME. |

| Note | Configure the id (voice register pool) command before any other voice register
                                       		  pool commands, including the application command. The id command identifies a locally available
                                       		  individual Cisco SIP IP phone or set of Cisco SIP IP phones. |
|---|---|

| Command | Description |
|---|---|
| application (dial-peer) | Enables a specific application on a dial peer. |
| application (voice register global) | Selects the session-level application for all dial peers
                                          						associated with SIP phones. |
| id (voice register pool) | Explicitly identifies a locally available individual Cisco
                                          						SIP IP phone, or when running Cisco Unified SIP SRST, set of Cisco SIP IP
                                          						phones. |
| mode (voice register global) | Enables the mode for provisioning SIP phones in a Cisco
                                          						Unified CME system. |
| show call application voice summary | Displays information about voice applications. |
| show dial-peer voice | Displays information for dial peers. |
| voice register global | Enters voice register global configuration mode in order to
                                          						set global parameters for all supported Cisco SIP phones in a Cisco Unified CME
                                          						or Cisco Unified SIP SRST environment. |
| voice register pool | Enters voice register pool configuration mode for SIP
                                          						phones. |

| size | Number of entries in attempted registrations table. Size
                                          						range from 0 to 50. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 Cisco Unified SRST 8.1 | This command was introduced. |

| Command | Description |
|---|---|
| clear voice register attempted- registrations | Allows to delete entries in attempted-registration table. |
| show voice register attempted-registrations | Displays details of phones that attempted to register and
                                          						failed. |

| Cisco
                                    				  IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.4(3)M | Cisco Unified Enhanced SRST 10.5 | This
                                       					 command was introduced. |

| Command | Description |
|---|---|
| ephone-hunt group | Configures an ephone hunt group in Cisco Unified SRST. |
| voice-hunt group | Configures a voice hunt group in Cisco Unified SRST. |

| credential tag | Number that identifies the credential file to use for
                                          						out-of-dialog REFER (OOD-R) or presence authentication. Range: 1 to 5. |
|---|---|
| location | Name and location of the credential file in URL format.
                                          						Valid storage locations are TFTP, HTTP, and flash memory. |
| ood-refer | Incoming OOD-R requests are authenticated using RFC
                                          						2617-based digest authentication. |
| presence | Incoming presence subscription requests from an external
                                          						presence server are authenticated. |
| realm string | Realm parameter for challenge and response as specified in
                                          						RFC 2617 is authenticated. |
| register | All incoming registration requests are challenged and
                                          						authenticated. Valid for Cisco Unified CME only. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |
| 12.4(11)XJ | Cisco Unified CME 4.1 Cisco Unified SRST 4.1 | The credential , ood-refer , presence , and register keywords were added. The register keyword replaced the all keyword. |
| 12.4(15)T | Cisco Unified CME 4.1 Cisco Unified SRST 4.1 | The modifications to this command were integrated into
                                          						Cisco IOS Release 12.4(15)T. |

| Command | Description |
|---|---|
| credential load | Reloads a credential file into flash memory. |
| mode cme | Enables the mode for provisioning SIP phones in a Cisco
                                          						Unified CME system. |
| presence-enable | Allows incoming presence subscribe requests from SIP
                                          						trunks. |
| refer-ood enable | Enables OOD-R processing. |
| username (ephone) | Defines a username and password for SCCP phones. |
| username (voice register pool) | Defines a username and password for authenticating SIP
                                          						phones. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 and Cisco SIP SRST 3.4 | This command was introduced. |

| Note | Use the b2bua command to configure Cisco SIP SRST 3.4
                                       		  only after using the allow-connections command to enable B2BUA
                                       		  call flow on the SRST gateway. |
|---|---|

| Command | Description |
|---|---|
| allow-connections | Enables calls between SIP endpoints in a VoIP network. |
| dial-peer voice | Defines a dial peer and enters dial-peer configuration
                                          						mode. |
| mode (voice register global) | Enables the mode for provisioning SIP phones in a Cisco
                                          						Unified CME system. |
| show dial-peer voice | Displays information for dial peers. |
| source-address (voice register global) | Identifies the IP address and port through which SIP phones
                                          						communicate with a Cisco Unified CME router. |
| voice register global | Enters voice register global configuration mode in order to
                                          						set global parameters for all supported Cisco SIP phones in a Cisco Unified CME
                                          						or Cisco Unified SIP SRST environment. |

| directory number | Telephone number to which calls are forwarded. Represents a
                                          						fully qualified E.164 number. Maximum length of the telephone number is 32. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was introduced. |
| Cisco IOS XE Amsterdam 17.2.1r | Cisco Unified SIP SRST 12.8 | Introduced support for YANG models. |

| Note | This command in voice register dn configuration mode is not
                                       		  commonly used for Cisco Unified SIP SRST. |
|---|---|

| Command | Description |
|---|---|
| call-forward b2bua busy | Enables call forwarding for a SIP B2BUA so that incoming
                                          						calls to a busy extension are forwarded to another extension. |
| call-forward b2bua mailbox | Controls the specific voice-mail box selected in a
                                          						voice-mail system at the end of a call forwarding exchange. |
| call-forward b2bua noan | Enables call forwarding for a SIP B2BUA so that incoming
                                          						calls to an extension that does not answer after a configured amount of time
                                          						are forwarded to another extension. |
| call-forward b2bua unreachable | Enables call forwarding for a SIP B2BUA so that incoming
                                          						calls to an extension that is not registered in Cisco Unified CME are forwarded
                                          						to another extension. |
| call-waiting (voice register pool) | Enables call waiting on a SIP phone. |
| number (voice register dn) | Associates an extension number with a voice register dn. |
| voice register dn | Enters voice register dn configuration mode to define an
                                          						extension for a SIP phone line. |
| voice register pool | Enters voice register pool configuration mode for SIP
                                          						phones. |

| directory number | Telephone number to which calls are forwarded. Represents a
                                          						fully qualified E.164 number. Maximum length of the telephone number is 32. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was introduced. |

| Note | This command in voice register dn configuration mode is not
                                       		  commonly used for Cisco Unified SIP SRST. |
|---|---|

| Command | Description |
|---|---|
| call-forward b2bua all | Enables call forwarding for a SIP B2BUA so that all
                                          						incoming calls are forwarded to another extension. |
| call-forward b2bua mailbox | Controls the specific voice-mail box selected in a
                                          						voice-mail system at the end of a call forwarding exchange. |
| call-forward b2bua noan | Enables call forwarding for a SIP B2BUA so that incoming
                                          						calls to an extension that does not answer after a configured amount of time
                                          						are forwarded to another extension. |
| call-forward b2bua unreachable | Enables call forwarding for a SIP B2BUA so that incoming
                                          						calls to an extension that is not registered in Cisco Unified CME are forwarded
                                          						to another extension. |
| call-waiting (voice register pool) | Enables call waiting on a SIP phone. |
| number (voice register dn) | Associates an extension number with a voice register dn. |
| voice register dn | Enters voice register dn configuration mode to define an
                                          						extension for a SIP phone line. |
| voice register pool | Enters voice register pool configuration mode for SIP
                                          						phones. |

| directory number | Telephone number to which calls are forwarded when the
                                          						forwarded destination is busy or does not answer. Represents a fully qualified
                                          						E.164 number. Maximum length of the telephone number is 32. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was introduced. |

| Note | This command in voice register dn configuration mode is not
                                       		  commonly used for Cisco Unified SIP SRST. |
|---|---|

| Command | Description |
|---|---|
| call-forward b2bua all | Enables call forwarding for a SIP B2BUA so that all
                                          						incoming calls are forwarded to another extension. |
| call-forward b2bua busy | Enables call forwarding for a SIP B2BUA so that incoming
                                          						calls to a busy extension are forwarded to another extension. |
| call-forward b2bua noan | Enables call forwarding for a SIP B2BUA so that incoming
                                          						calls to an extension that does not answer after a configured amount of time
                                          						are forwarded to another extension. |
| call-forward b2bua unreachable | Enables call forwarding for a SIP B2BUA so that incoming
                                          						calls to an extension that is not registered in Cisco Unified CME are forwarded
                                          						to another extension. |
| call-waiting (voice register pool) | Enables call waiting on a SIP phone. |
| number (voice register dn) | Associates an extension number with a voice register dn. |
| voice register dn | Enters voice register dn configuration mode to define an
                                          						extension for a SIP phone line. |
| voice register pool | Enters voice register pool configuration mode for SIP
                                          						phones. |

| directory number | Telephone number to which calls are forwarded. Represents a
                                          						fully qualified E.164 number. Maximum length of the telephone number is 32. |
|---|---|
| timeout seconds | Number of seconds that a call can ring with no answer
                                          						before the call is forwarded to another extension. Range is 3 to 60000. Default
                                          						is 20. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was introduced. |

| Note | This command in voice register dn configuration mode is not
                                       		  commonly used for Cisco Unified SIP SRST. |
|---|---|

| Command | Description |
|---|---|
| call-forward b2bua all | Enables call forwarding for a SIP B2BUA so that all
                                          						incoming calls are forwarded to another extension. |
| call-forward b2bua busy | Enables call forwarding for a SIP B2BUA so that incoming
                                          						calls to a busy extension are forwarded to another extension. |
| call-forward b2bua mailbox | Controls the specific voice-mail box selected in a
                                          						voice-mail system at the end of a call forwarding exchange. |
| call-forward b2bua unreachable | Enables call forwarding for a SIP B2BUA so that incoming
                                          						calls to an extension that is not registered in Cisco Unified CME are forwarded
                                          						to another extension. |
| call-waiting (voice register pool) | Enables call waiting on a SIP phone. |
| number (voice register dn) | Associates an extension number with a voice register dn. |
| voice register dn | Enters voice register dn configuration mode to define an
                                          						extension for a SIP phone line. |
| voice register pool | Enters voice register pool configuration mode for SIP
                                          						phones. |

| directory-number | Directory number representing a fully qualified E.164
                                          						number. This number can contain “.” wildcard characters that correspond to the
                                          						right-justified digits in the directory number extension. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco Unified SRST 2.0 | This command was introduced on the following platforms:
                                          						Cisco 1750, Cisco 1751, Cisco 2600 series and Cisco 3600 series multiservice
                                          						routers, and Cisco IAD2420 series IADs. |
| 12.2(8)T | Cisco Unified SRST 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers. |
| 12.2(8)T1 | Cisco Unified SRST 2.0 | This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers. |
| 12.2(11)T | Cisco Unified SRST 2.1 | This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers. |

| Note | You can forward an incoming VoIP call only to destination numbers
                                       		  local to the router. VoIP calls cannot be forwarded to an alternate (on-net)
                                       		  VoIP destination. |
|---|---|

| Command | Description |
|---|---|
| call-forward noan | Configures call forwarding to another number when no answer
                                          						is received from the Cisco IP phone. |
| call-manager-fallback | Enables Cisco Unified SRST feature support and enters
                                          						call-manager-fallback configuration mode. |

| directory-number | Directory number representing a fully qualified E.164
                                          						number or a local extension number. This number can contain “.” wildcard
                                          						characters that correspond to the right-justified digits in the directory
                                          						number extension. |
|---|---|
| timeout | Sets the ringing no answer timeout duration, which is the
                                          						waiting time (in seconds) before the call is forwarded to another phone. |
| seconds | Time (in seconds) before call forwarding starts. The range
                                          						is from 3 to 60000. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco SRST 2.0 | This command was introduced on the following platforms:
                                          						Cisco 1750, Cisco 1751, Cisco 2600 series and Cisco 3600 series multiservice
                                          						routers, and Cisco IAD2420 series IADs. |
| 12.2(8)T | Cisco SRST 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers. |
| 12.2(8)T1 | Cisco SRST 2.0 | This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers. |
| 12.2(11)T | Cisco SRST 2.1 | This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers. |

| Note | An incoming VoIP call can be forwarded only to destination numbers
                                       		  local to the router. VoIP calls cannot be forwarded to an alternate (on-net)
                                       		  VoIP destination. |
|---|---|

| Command | Description |
|---|---|
| call-forward busy | Configures call forwarding to another number when a Cisco
                                          						IP phone is busy. |
| call-manager-fallback | Enables Cisco Unified SRST feature support and enters
                                          						call-manager-fallback configuration mode. |

| pattern | String that consists of one or more digits and wildcard
                                          						markers or dots (.) to define a specific pattern. Calling parties that match a
                                          						defined pattern use the H.450.3 standard if they are forwarded. A pattern of .T
                                          						specifies the H.450.3 forwarding standard for all incoming calls. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| call-manager-fallback | Enables Cisco Unified SRST feature support and enters
                                          						call-manager-fallback configuration mode. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco SRST 1.0 | This command was introduced on the following platforms:
                                          						Cisco 2600 series and Cisco 3600 series multiservice routers, and Cisco IAD2420
                                          						series IADs. |
| 12.2(2)XT | Cisco SRST 2.0 | This command was implemented on Cisco 1750 and Cisco 1751
                                          						multiservice routers. |
| 12.2(8)T | Cisco SRST 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers. |
| 12.2(8)T1 | Cisco SRST 2.0 | This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers. |
| 12.2(11)T | Cisco SRST 2.1 | This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers. |

| Command | Description |
|---|---|
| access-code | Configures trunk access codes for each type of line so that
                                          						the Cisco IP phones can access the trunk lines. |
| alias | Provides a mechanism for servicing calls to telephone
                                          						numbers that are unavailable during Cisco Unified Communications Manager
                                          						fallback. |
| call-forward busy | Configures call forwarding to another number when a Cisco
                                          						IP phone is busy. |
| call-forward noan | Configures call forwarding to another number when no answer
                                          						is received from a Cisco IP phone. |
| cor | Configures COR on the dial peers associated with directory
                                          						numbers. |
| default-destination | Assigns a default destination number for incoming telephone
                                          						calls. |
| dialplan-pattern | Creates a global prefix that can be used to expand the
                                          						abbreviated extension numbers into fully qualified E.164 numbers. |
| huntstop | Sets huntstop for the dial peers associated with Cisco IP
                                          						phone lines. |
| ip source-address | Enables the router to receive messages from Cisco IP phones
                                          						through the specified IP addresses and ports. |
| keepalive | Configures the time interval between sending keepalive
                                          						messages to the router used by Cisco IP phones. |
| max-dn | Sets the maximum number of directory numbers or virtual
                                          						voice ports that can be supported by the router. |
| max-ephone | Configures the maximum number of Cisco IP phones that can
                                          						be supported by the router. |
| reset | Resets Cisco IP phones. |
| timeouts interdigit | Configures the interdigit timeout value for all Cisco IP
                                          						phones attached to the router. |
| transfer-pattern | Allows transfer of telephone calls by Cisco IP phones to
                                          						other phone numbers. |
| translate | Applies a translation rule to modify the phone number
                                          						dialed by any Cisco IP phone user during Cisco Unified Communications Manager
                                          						fallback. |
| voicemail | Configures the telephone number that is speed-dialed when
                                          						the message button on a Cisco IP phone is pressed. |

| Cisco IOS Release | yCisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 Cisco Unified SRST 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 Cisco Unified SRST 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| show voice moh-group statistics | Displays the MOH subsystem statistics information |
| show voice moh-group | Displays the MOH groups configured |

| Release | Cisco Products | Modification |
|---|---|---|
| 15.0(1)M | Cisco Unified SRST 8.0 Cisco Unified SIP SRST 8.0 | This command was introduced. |

| Command | Description |
|---|---|
| call-manager-fallback | Enters call-manager-fallback configuration mode. |

| value | Maximum
                                       					 number of digits that can be dialed. The range is from 3 to 16. |
|---|---|

| Cisco
                                    				  IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.4(3)M | Cisco Unified Enhanced SRST 10.5 | This
                                       					 command was introduced. |

| Command | Description |
|---|---|
| conference-pattern blocked | Blocks
                                          						extensions on an ephone or voice register pool from making conference calls to
                                          						patterns defined in the transfer-pattern command. |
| conference
                                                							 transfer-pattern | Allows
                                          						to conference the transferred calls to phones within the local Cisco Unified
                                          						SRST network. |
| transfer max-length | Allows
                                          						the transfer of calls to phones within the local Cisco Unified SRST network. |
| transfer-pattern
                                                							 (call-manager fallback) | Allows
                                          						the transfer of calls to phones outside the local Cisco Unified SRST network. |

| Cisco
                                    				  IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.4(3)M | Cisco Unified Enhanced SRST 10.5 | This
                                       					 command was introduced. |

| Command | Description |
|---|---|
| conference max-length | Allows
                                          						the conferences only if the dialed digits are within the maximum length limit. |
| conference
                                                							 transfer-pattern | Allows
                                          						to conference the transferred calls to phones within the local Cisco Unified
                                          						SRST network. |
| transfer-pattern blocked | Block
                                          						extensions on an ephone or voice register pool from making transferring calls
                                          						to patterns defined in the conference pattern-blocked command. |
| transfer-pattern
                                                							 (call-manager fallback) | Allows
                                          						the transfer of calls to phones outside the local Cisco Unified SRST network. |

| Release | Modification |
|---|---|
| 15.3(2)T | This command was introduced. |

| Command | Description |
|---|---|
| call-manager-fallback | Enters call-manager-fallback configuration mode to enable
                                          						Cisco Unified SRST support. |
| transfer-pattern | Allows Cisco Unified IP phones to transfer telephone calls
                                          						from callers outside the local IP network to another Cisco Unified IP phone. |

| incoming | COR
                                          						list to be used by incoming dial peers. |
|---|---|
| outgoing | COR
                                          						list to be used by outgoing dial peers. |
| cor-list-name | COR
                                          						list name. |
| cor-list-number | COR
                                          						list identifier. The maximum number of COR lists that can be created is 20,
                                          						comprised of incoming or outgoing dial peers. The first six COR lists are
                                          						applied to a range of directory numbers. The directory numbers that do not have
                                          						a COR configuration are assigned to the default COR list, provided that a
                                          						default COR list has been defined. |
| starting-number - ending-number | Directory number range; for example, 2000 - 2025. |
| default | Instructs the COR list to assume behavior according to a predefined default COR
                                          						list. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco
                                          						SRST 2.0 | This
                                          						command was introduced on the following platforms: Cisco 1750, Cisco 1751,
                                          						Cisco 2600 series and Cisco 3600 series multiservice routers, and Cisco IAD2420
                                          						series IADs. |
| 12.2(8)T | Cisco
                                          						SRST 2.0 | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T and implemented on the
                                          						Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers. |
| 12.2(8)T1 | Cisco
                                          						SRST 2.0 | This
                                          						command was implemented on the Cisco 2600-XM and Cisco 2691 routers. |
| 12.2(11)T | Cisco
                                          						SRST 2.01 | This
                                          						command was integrated into Cisco IOS Release 12.2(11)T and implemented on the
                                          						Cisco 1760 routers. The default keyword was added. |
| 12.3(11)T | Cisco
                                          						SRST 3.2 | The
                                          						maximum number of COR lists that can be created was increased to 20. |

| COR
                                          					 List on Incoming Dial Peer | COR
                                          					 List on Outgoing Dial Peer | Result |
|---|---|---|
| No COR | No COR | Call
                                          					 will succeed. |
| No COR | COR
                                          					 list applied for outgoing calls | Call
                                          					 will succeed. By default, the incoming dial peer has the highest COR priority
                                          					 when no COR is applied. If you apply no COR for an incoming call leg to a dial
                                          					 peer, the dial peer can make a call out of any other dial peer regardless of
                                          					 the COR configuration on the outgoing dial peer. |
| COR
                                          					 list applied for incoming calls | No COR | Call
                                          					 will succeed. By default, the outgoing dial peer has the lowest priority.
                                          					 Because there are some COR configurations for incoming calls on the incoming or
                                          					 originating dial peer, it is a superset of the outgoing call’s COR
                                          					 configuration for the outgoing or terminating dial peer. |
| COR
                                          					 list applied for incoming calls (superset of COR list applied for outgoing
                                          					 calls on the outgoing dial peer) | COR
                                          					 list applied for outgoing calls (subsets of COR list applied for incoming calls
                                          					 on the incoming dial peer) | Call
                                          					 will succeed. The COR list for incoming calls on the incoming dial peer is a
                                          					 superset of the COR list for outgoing calls on the outgoing dial peer. |
| COR
                                          					 list applied for incoming calls (subset of COR list applied for outgoing calls
                                          					 on the outgoing dial peer) | COR
                                          					 list applied for outgoing calls (supersets of COR list applied for incoming
                                          					 calls on the incoming dial peer) | Call
                                          					 will not succeed. The COR list for incoming calls on the incoming dial peer is
                                          					 not a superset of the COR list for outgoing calls on the outgoing dial peer. |

| Command | Description |
|---|---|
| call-manager-fallback | Enables Cisco Unified SRST feature support and enters call-manager-fallback
                                          						configuration mode. |
| corlist-incoming | Specifies the COR list to be used when a specified dial peer acts as the
                                          						incoming dial peer. |
| corlist-outgoing | Specifies the COR list to be used by outgoing dial peers. |
| dial-peer cor list | Defines a COR list name. |

| incoming | COR list to be used by incoming dial peers. |
|---|---|
| outgoing | COR list to be used by outgoing dial peers. |
| cor-list-name | COR list name. |
| cor-list-number | COR list identifier. |
| starting-number | Start of a directory number range, if an ending number is
                                          						included. Can also be a standalone number. |
| - | (Optional) Indicator that a full range is configured. |
| ending-number | (Optional) End of a directory number range. |
| default | Instructs the COR list to assume behavior according to a
                                          						predefined default COR list. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SIP SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SIP SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was added to Cisco Communications Manager
                                          						Express (Cisco CME). |

| Note | Configure the id (voice register pool) command before any other voice register
                                       		  pool commands, including the cor command. The id command identifies a locally available
                                       		  individual Cisco SIP IP phone or set of Cisco SIP IP phones. |
|---|---|

| Command | Description |
|---|---|
| dial-peer cor custom | Specifies that named CORs apply to dial peers. |
| dial-peer cor list | Defines a COR list name. |
| id (voice register pool) | Explicitly identifies a locally available individual Cisco
                                          						SIP IP phone, or when running Cisco Unified SIP SRST, set of Cisco SIP IP
                                          						phones. |
| member (dial-peer cor list) | Adds a member to a dial-peer COR list. |
| name (dial-peer custom cor) | Provides a name for a custom COR. |
| show dial-peer voice | Displays information for voice dial peers. |
| voice register pool | Enables Cisco Unified SIP SRST voice register pool
                                          						configuration commands. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.3(14)T | Cisco
                                          						SRST 3.3 | This
                                          						command was introduced for Cisco Unified SRST. |
| 12.4(4)XC | Cisco
                                          						Unified CME 4.0 | This
                                          						command was introduced for Cisco Unified CME. |
| Cisco
                                          						IOS XE Fuji Release, 16.7.1 | Unified SRST 12.1 | This
                                          						command was introduced for Unified SRST support on Cisco 4000 Series Integrated
                                          						Services Router. |
| Cisco IOS XE Dublin
                                                17.10.1a | Cisco Unified SRST 14.3 | Introduced support for YANG models. |

| Caution | For security
                                          			 reasons, credentials service should be deactivated on all SRST routers after
                                          			 provisioning to Cisco Unified Communications Manager is completed. |
|---|---|

| Command | Description |
|---|---|
| ctl-service admin | Specifies a user name and password to authenticate the CTL client during the
                                          						CTL protocol. |
| debug credentials | Sets
                                          						debugging on the credentials service that runs between a Cisco Unified CME CTL
                                          						provider the CTL client or between an SRST router and Cisco Unified
                                          						Communications Manager. |
| ip source-address (credentials) | Enables the Cisco Unified CME or SRST router to receive messages through the
                                          						specified IP address and port. |
| show credentials | Displays the credentials settings on a Cisco Unified CME or SRST router. |
| trustpoint (credentials) | Specifies the name of the trustpoint to be associated with a Cisco Unified CME
                                          						CTL provider certificate or with an SRST router certificate. |

| mm-dd-yy | Sets the date format to month, day, year. Each element
                                          						requires a two-digit number. This format is the default setting. |
|---|---|
| dd-mm-yy | Sets the date format to day, month, year. Each element
                                          						requires a two-digit number. |
| yy-dd-mm | Sets the date format to year, day, month. Each element
                                          						requires a two-digit number. |
| yy-mm-dd | Sets the date format to year, month, day. Each element
                                          						requires a two-digit number. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco SRST 2.0 | This command was introduced on the following platforms:
                                          						Cisco 1750, Cisco 1751, Cisco 2600 series and Cisco 3600 series multiservice
                                          						routers, and Cisco IAD2420 series IADs. |
| 12.2(8)T | Cisco SRST 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers. |
| 12.2(8)T1 | Cisco SRST 2.0 | This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers. |
| 12.2(11)T | Cisco SRST 2.01 | This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers. |
| 12.2(15)ZJ | Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.2(15)ZJ. |
| 12.3(4)T | Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| call-manager-fallback | Enables Cisco Unified SRST feature support and enters
                                          						call-manager-fallback configuration mode. |

| telephone-number | Telephone number of the default destination. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco SRST 1.0 | This command was introduced on the following platforms:
                                          						Cisco 2600 series and Cisco 3600 series multiservice routers, and Cisco IAD2420
                                          						series IADs. |
| 12.2(2)XT | Cisco SRST 2.0 | This command was implemented on Cisco 1750 and Cisco 1751
                                          						multiservice routers. |
| 12.2(8)T | Cisco SRST 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers. |
| 12.2(8)T1 | Cisco SRST 2.0 | This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers. |
| 12.2(11)T | Cisco SRST 2.01 | This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers. |

| Command | Description |
|---|---|
| alias (call-manager- fallback) | Provides a mechanism for servicing calls to telephone
                                          						numbers that are unavailable during Cisco Unified Communications Manager
                                          						fallback. |
| call-manager-fallback | Enables Cisco Unified SRST feature support and enters
                                          						call-manager-fallback configuration mode. |

| string | An alphanumeric string to add a brief description specific
                                          						to a MOH group. Maximum length: 80 characters including spaces. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 Cisco Unified SRST 8.0 | This command was introduced |
| 15.1(1)T | Cisco Unified CME 8.0 Cisco Unified SRST 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| voice-moh-group | Enter voice-moh-group configuration mode. |
| moh | Enables music on hold from a flash audio feed |
| multicast moh | Enables multicast of the music-on-hold audio stream. |
| extension-range | Specifies the extension range for a clients calling a
                                          						voice-moh-group. |

| number | Device
                                          						ID of the phone type. Range: 1 to 2,147,483,647. Default: 0. See Table 1 for a list of supported device IDs. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco
                                          						Unified CME 4.3 Cisco Unified SRST 4.3 | This
                                          						command was introduced. |

| Supported
                                          					 Device | device-id | num-buttons | max-presentation |
|---|---|---|---|
| Cisco
                                          					 Unified IP Conference Station 7937G | 431 | 1 | 6 |
| Nokia E61 | 376 | 1 | 1 |

| Command | Description |
|---|---|
| device-name | Assigns
                                          						a name to a phone type in an ephone-type template. |
| load | Associates a type of phone with a phone firmware file. |
| type | Assigns the phone type to a SCCP phone. |

| name | String that identifies this phone type. Value is any
                                          						alphanumeric string up to 32 characters. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco Unified CME 4.3 Cisco Unified SRST 4.3 | This command was introduced. |

| Command | Description |
|---|---|
| device-id | Specifies the device ID for a phone type in an ephone-type
                                          						template. |

| phone-type | Device
                                          						type of the phone. See Table 1 for a list of supported device types. Default value is the same value entered
                                          						with the ephone-type command. |
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
                                          						command was integerated into Cisco IOS Release 12.4(20)T. |

| Supported
                                          					 Device | device-id | device-type | num-buttons | max-presentation |
|---|---|---|---|---|
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
                                          					 Unified IP Conference Station 7937G | 431 | 7937 | 1 | 6 |
| Cisco
                                          					 Unified IP Phone 8941 | 586 | 8941 | 4 | 3 |
| Cisco
                                          					 Unified IP Phone 8945 | 585 | 8945 | 4 | 3 |
| Nokia
                                          					 E61 | 376 | E61 | 1 | 1 |

| Command | Description |
|---|---|
| device-name | Assigns a name to a phone type in an ephone-type template. |
| ephone-type | Adds
                                          						a Cisco Unified IP phone type by defining an ephone-type template. |
| load | Associates a type of phone with a phone firmware file. |
| type | Assigns the phone type to a SCCP phone. |

| tag | Dial-plan string tag used before a ten-digit telephone
                                          						number. The tag number is from 1 to 5. |
|---|---|
| pattern | Dial-plan pattern, such as the area code, the prefix, and
                                          						the first one or two digits of the extension number, plus wildcard markers or
                                          						dots (.) for the remainder of the extension number digits. |
| extension-length | Sets the number of extension digits that will appear as a
                                          						caller ID. |
| extension-length | The number of extension digits. The extension length must
                                          						match the setting for IP phones in Cisco Unified Communications Manager mode.
                                          						The range is from 1 to 32. |
| extension-pattern | (Optional) Sets an extension number’s leading digit pattern
                                          						when it is different from the E.164 telephone number’s leading digits defined
                                          						in the pattern variable. |
| extension-pattern | (Optional) The extension number’s leading digit pattern.
                                          						Consists of one or more digits and wildcard markers or dots (.). For example,
                                          						5.. would include extensions 500 to 599; 5... would include extensions 5000 to
                                          						5999. The extension pattern must match the setting for IP phones in Cisco
                                          						Unified Communications Manager mode. |
| no-reg | (Optional) Prevents the E.164 numbers in the dial peer from
                                          						registering with the gatekeeper. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco SRST 1.0 | This command was introduced on the Cisco 2600 series and
                                          						Cisco 3600 series multiservice routers and on the Cisco IAD2420 series. |
| 12.2(2)XT | Cisco SRST 2.0 | This command was implemented on the Cisco 1750 and Cisco
                                          						1751 multiservice routers. |
| 12.2(8)T | Cisco SRST 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725 and Cisco 3745 routers. |
| 12.2(8)T1 | Cisco SRST 2.0 | This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers. |
| 12.2(11)T | Cisco SRST 2.01 | This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers. |
| 12.2(11)YT | Cisco SRST 2.1 | The extension-pattern keyword was
                                          						added. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| call-manager-fallback | Enables Cisco Unified SRST support and enters
                                          						call-manager-fallback configuration mode. |
| show dial-peer voice | Displays information for voice dial peers. |

| Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XJ | Cisco Unified CME 4.1 Cisco Unified SRST 4.1 | This command was introduced. |
| 12.4(15)T | Cisco Unified CME 4.1 Cisco Unified SRST 4.1 | This command was integrated into Cisco IOS Release
                                          						12.4(15)T. |

| Command | Description |
|---|---|
| dialplan | Assigns a dial plan to a SIP phone. |
| show voice register pool | Displays all configuration information associated with a
                                          						SIP phone. |
| voice register dialplan | Enters voice register dialplan configuration mode to define
                                          						a dial plan for SIP phones. |

| cisco-rtp | Forwards DTMF audio tones by using Real-Time Transport
                                          						Protocol (RTP) with a Cisco proprietary payload type. This keyword is supported
                                          						only for dial peers that are created by incoming REGISTERs from a SIP gateway.
                                          						It is not supported for dial peers that are created by a SIP Cisco IP phone. |
|---|---|
| rtp-nte | Forwards DTMF audio tones by using Real-Time Transport
                                          						Protocol (RTP) with a Named Telephone Event (NTE) payload. |
| sip-notify | Forwards DTMF audio tones by using SIP-NOTIFY messages.
                                          						This keyword is supported only for dial peers that are created by incoming
                                          						REGISTERs from a SIP gateway. It is not supported for dial peers that are
                                          						created by a SIP Cisco IP phone. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(4)T | Cisco SIP SRST 3.0 | This command was introduced. |
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was added to Cisco Unified CME. |
| Cisco IOS XE Amsterdam 17.2.1r | Cisco Unified SIP SRST 12.8 | Introduced support for YANG models. |

| Note | The cisco-rtp keyword is a proprietary Cisco
                                       		  implementation. If the proprietary Cisco implementation is not supported, the
                                       		  DTMF relay feature does not function, and the gateway sends DTMF tones in-band. |
|---|---|

| Command | Description |
|---|---|
| dtmf-relay (voice over IP) | Specifies how an H.323 or SIP gateway relays DTMF tones
                                          						between telephony interfaces and an IP network. |

| number | PSTN number that replaces a 911 caller’s extension. |
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
| voice emergency response location | Creates a tag for identifying an ERL for Enhanced 911
                                          						Services. |
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
                                          						Unified SIP SRST 4.2(1) | The zone tag option was added. This command was added for
                                          						Cisco Unified CME. |

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
| Cisco IOS XE Gibraltar 16.11.1a Release | Unified SRST 12.6 | The command is introduced. |

| Note | If the key used to encrypt the password is replaced with a new key (replace key or re-key), then the password is re-encrypted
                                          with the new key. |
|---|---|

| Command | Description |
|---|---|
| call-manager-fallback | Enables Unified SRST feature support and enters call-manager-fallback configuration mode. |

| phone-type | Unique label that identifies the type of phone. Value is
                                          						any alphanumeric string up to 32 characters. |
|---|---|
| addon | (Optional) Phone type is an add-on module, such as the
                                          						Cisco Unified IP Phone 7915 Expansion Module. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco Unified CME 4.3 Cisco Unifieid SRST 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 | This command was integrated into Cisco IOS Release
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

| time | Identifier (2-2880) in minutes for the maximum time the 911
                                          						caller history is available for callback. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XY | Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1) | This command was introduced. |

| Command | Description |
|---|---|
| callback | Default phone number to contact if a 911 callback cannot
                                          						find the last 911 caller from the ERL. |
| elin | E.164 number used as the default ELIN if no matching ERL to
                                          						the 911 caller’s IP phone address is found. |
| logging | Syslog informational message printed to the console every
                                          						time an emergency call is made. |
| voice emergency response settings | Creates a tag for identifying settings for E911 behavior. |

| starting-extension | Hexidecimal digits (0-9 or A-F) that define the starting
                                          						extension number in an extension range. Maximum length: 32 digits. |
|---|---|
| ending-extension | Hexidecimal digits (0-9 or A-F) that define the last
                                          						extension number in an extension range. Value of the ending extensing must be
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

| bellcore-dr1 bellcore-dr2 bellcore-dr3 bellcore-dr4 bellcore-dr5 | Each bellcore-dr keyword supports standard distinctive ringing
                                          						patterns as defined in the standard GR-506-CORE, LSSGR: Signaling for Analog Interfaces . |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was introduced. |

| Command | Description |
|---|---|
| voice register global | Enters voice register global configuration mode in order to
                                          						set global parameters for all supported Cisco SIP phones in a Cisco Unified
                                          						Communications Manager Express (Cisco Unified CME) or Cisco Unified SIP
                                          						Survivable Remote Site Telephony (SRST) environment. |

| group-tag | Unique
                                          						identifier of VRF group ranges from 1 to 5. |
|---|---|
| tapi | (Optional) Add TAPI-based client on the phone being configured to a VRF group. |

| Cisco
                                          						IOS Release | Cisco
                                          						Products | Modification |
|---|---|---|
| 12.4(22)T | Cisco
                                          						Unified SRST 7.0(1) | This
                                          						command was introduced. |
| 15.4(3)M | Cisco
                                          						Unified SRST 10.5 | This
                                          						command was modified. |

| Command | Description |
|---|---|
| voice register pool | Enters
                                          						voice register pool configuration mode. |
| voice register
                                                							 template | Enters
                                          						voice register template configuration mode. |
| ephone-template (ephone) | Applies an ephone template to an ephone configuration. |
| group (telephony-service) | Creates a VRF group for phones and users in Cisco Unified CME. |
| mac-address | Associates the MAC address of a Cisco IP phone with an ephone configuration. |

| T1 | Timer for identification. |
|---|---|
| T2 | Timer for call setup. |
| T3 | Timer for response initiation. |
| T4 | Timer for response setup. |
| milliseconds | Number of milliseconds. Range is from 500 to 60000. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| h323 | Enables H.323 voice service configuration commands. |
| voice service | Enters voice-service configuration mode. |

| 3des-cbc-sha | Encryption tls_rsa_with_3des_ede_cbc_sha (TLS1.0) ciphersuite. |
|---|---|
| aes-128-cbc-sha | Encryption tls_rsa_with_aes_128_cbc_sha (TLS1.2 and below versions) ciphersuite. |
| des-cbc-sha | Encryption tls_rsa_with_des_cbc_sha (TLS1.0) ciphersuite |
| dhe-rsa-aes-cbc-sha2 | Encryption tls_rsa_with_cbc_sha2 (TLS1.2) ciphersuite |
| ecdhe-ecdsa-aes-gcm-sha2 | Encryption tls_rsa_with_ecdhe-ecdsa-aes-gcm-sha2 (TLS1.2) ciphersuite |
| ecdhe-rsa-aes-cbc-sha2 | Encryption tls_rsa_with_aes-cbd-sha2 (TLS1.2) ciphersuite |
| ecdhe-rsa-aes-gcm-sha2 | Encryption tls_rsa_with_aes-gcm-sha2 (TLS1.2) ciphersuite |
| null-md5 | Encryption tls_rsa_with_null_md5 (TLS1.0) ciphersuite |
| rc4-128-md5 | Encryption tls_rsa_with_rc4_128_md5 (TLS1.0) ciphersuite |
| rc4-128-sha | Encryption tls_rsa_with_rc4_128_sha (TLS1.0) ciphersuite |
| rsa-aes-cbc-sha2 | Encryption tls_rsa_with_aes_cbc_sha2 (TLS1.2) ciphersuite |
| tls13-aes128-gcm-sha256 | Encryption tls13_aes128_gcm_sha256 (TLS1.3) ciphersuite. |
| tls13-aes256-gcm-sha384 | Encryption tls13_aes256_gcm_sha384 (TLS1.3) ciphersuite. |
| tls13-chacha20-poly1305-sha256 | Encryption tls13_chacha20_poly1305_sha256 (TLS1.3) ciphersuite. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| Cisco IOS XE 17.14.1a | Unified SRST 14.4 | This command was modified to support the following TLS version 1.3 ciphers— tls13-aes128-gcm-sha256 tls13-aes256-gcm-sha384 tls13-chacha20-poly1305-sha256 Introduced support for the TLS version 1.3 ciphers Yang model. |

| Command | Description |
|---|---|
| http client secure-trustpoint | Declares the trustpoint that the HTTP client should use for HTTPS sessions. |
| show http client secure status | Displays the trustpoint and cipher suites that are configured in the HTTP client. |

| channel | (Optional) For dual-line ephone-dns, keeps incoming calls
                                          						from hunting to the second channel if the first channel is busy or does not
                                          						answer. |
|---|---|
| 1-8 | (Optional) For octo-line ephone-dns, keeps incoming calls
                                          						from hunting to the next channel if the last allowable channel is busy or does
                                          						not answer. The default is 8. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco SRST 1.0 | This command was introduced on the following platforms:
                                          						Cisco 2600 series and Cisco 3600 series multiservice routers, and Cisco IAD2420
                                          						series IADs. |
| 12.2(2)XT | Cisco SRST 2.0 | This command was implemented on Cisco 1750 and Cisco 1751
                                          						multiservice routers. |
| 12.2(8)T | Cisco SRST 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers. |
| 12.2(8)T1 | Cisco SRST 2.0 | This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers. |
| 12.2(11)T | Cisco SRST 2.01 | This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers. |
| 12.2(15)ZJ | Cisco SRST 3.0 | The channel keyword was added. |
| 12.3(4)T | Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(15)XZ | Cisco Unified SRST 4.3 | The 1-8 argument was added for
                                          						octo-line mode. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Note | Use the no huntstop command only if you want to disable
                                       		  huntstop. |
|---|---|

| Command | Description |
|---|---|
| call-manager-fallback | Enables Cisco Unified SRST support and enters
                                          						call-manager-fallback configuration mode. |
| huntstop (dial-peer) | Disables all further dial-peer hunting if a call fails
                                          						using hunt groups. |
| max-dn (call- manager-fallback) | Sets the maximum possible number of virtual voice ports
                                          						that can be supported by a router and activates dual-line mode, octo-line mode,
                                          						or both modes. |

| network address mask mask \| address mask mask | This keyword/argument combination is used to accept SIP
                                          						Register messages for the indicated phone numbers from any IP phone within the
                                          						specified IPv4 and IPv6 subnets. ipv6 address can only be configured
                                          						with an IPv6 address or a dual-stack mode. |
|---|---|---|
| ip address mask mask \| address mask mask | This keyword/argument combination is used to identify an
                                          						individual phones IPv4 or IPv6 address. ipv6 address can only be
                                          						configured with an IPv6 address or a dual-stack mode. |
| mac address | The mac address keyword/argument
                                          						combination is used to identify the MAC address of a particular Cisco IP phone. |
| device-id-name devicename | Defines the device name to be used to download the phone’s
                                          						configuration file. |
| phone-number e164-number | Configures the phone-number in E.164 format for webex calling user. |
| extension-number extension-number | Configures extension number for Webex Calling users. |

| Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SIP SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SIP SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was added to Cisco CME. |
| 15.3(3)T | Cisco Unified CME 10.0 | This command was modified to add the device-id-name devicename keyword-argument
                                          						combination. |
| Cisco IOS XE Everest 16.6.1 | Unified SRST 12.0 | This command was modified to add the following
                                          						keyword-argument combinations for network and ip to include support for IPv6
                                          						address: address mask mask . |
| Cisco IOS XE Amsterdam 17.2.1r | Cisco Unified SIP SRST 12.8 | Introduced support for YANG models. |
| Cisco IOS XE Cupertino 17.9.1 | Cisco Unified SRST 14.3 | This command was modified to add the following: phone-number e164-number and extension-number extension-number |

| Note | For Cisco Unified SIP SRST, this command also allows explicit
                                       		  identification of locally available set of Cisco SIP IP phones. |
|---|---|

| Command | Description |
|---|---|
| mode (voice register global) | Enables the mode for provisioning SIP phones in a Cisco
                                          						Unified CallManager Express (Cisco Unified CME) system. |

| number | (Optional) Sequence of digits that represent a phone number
                                          						prefix. |
|---|---|

| Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SIP SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SIP SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| id (voice register pool) | Explicitly identifies a locally available individual Cisco
                                          						SIP IP phone or set of Cisco SIP IP phones. |
| incoming called-number (dial-peer) | Specifies an incoming called number of an MMoIP or POTS
                                          						dial peer. |
| show dial-peer voice | Displays information for voice dial peers. |
| voice register pool | Enables SIP SRST voice register pool configuration
                                          						commands. |

| number | DSCP value. Range: 0 to 63. |
|---|---|
| af | Sets DSCP to assured forwarding bit pattern. af11 —bit
                                             						  pattern 001010 af12 —bit
                                             						  pattern 001100 af13 — bit
                                             						  pattern 001110 af21 — bit
                                             						  pattern 010010 af22 — bit
                                             						  pattern 010100 af23 — bit
                                             						  pattern 010110 af31 — bit
                                             						  pattern 011010 af32 — bit
                                             						  pattern 011100 af33 — bit
                                             						  pattern 011110 af41 —bit
                                             						  pattern 100010 af42 —bit
                                             						  pattern 100100 af43 —bit
                                             						  pattern 100110 |
| cs | Sets DSCP to class-selector codepoint. cs1 —codepoint
                                             						  1 (precedence 1) cs2 —codepoint
                                             						  2 (precedence 2) cs3 —codepoint
                                             						  3 (precedence 3) cs4 —codepoint
                                             						  4 (precedence 4) cs5 —codepoint
                                             						  5 (precedence 5) cs6 —codepoint
                                             						  6 (precedence 6) cs7 —codepoint
                                             						  7 (precedence 7) |
| default | Sets DSCP to default bit pattern of 000000. |
| ef | Sets DSCP to expedited forwarding bit pattern 101110. |
| media | Applies DSCP to media payload packets for SCCP phones. |
| service | Not supported for Cisco Unified SRST. |
| signaling | Not supported for Cisco Unified SRST. |
| video | Not supported for Cisco Unified SRST. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified SRST 7.1 | This command was introduced. |
| 12.4(24)T | Cisco Unified SRST 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| ip qos dscp | Sets the DSCP for QoS in a dial peer. |
| service-policy | Assigns a policy map to an interface that will be used as
                                          						the service policy for the interface. |

| ip-address | The preexisting SRST router IP address, typically one of
                                          						the addresses of the Ethernet port of the local router. |
|---|---|
| port | (Optional) The port to which the gateway router connects to
                                          						receive messages from the Cisco IP phones. |
| port | (Optional) The port number. The range is from 2000 to 9999.
                                          						The default is 2000. |
| any-match | (Optional) Disables strict IP address checking for
                                          						registration. This is the default. |
| strict-match | (Optional) Requires strict IP address checking for
                                          						registration. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco SRST 1.0 | This command was introduced on the following platforms:
                                          						Cisco 2600 series and Cisco 3600 series multiservice routers, and Cisco IAD2420
                                          						series IADs. |
| 12.2(2)XT | Cisco SRST 2.0 | This command was implemented on Cisco 1750 and Cisco 1751
                                          						multiservice routers. |
| 12.2(8)T | Cisco SRST 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers. |
| 12.2(8)T1 | Cisco SRST 2.0 | This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers. |
| 12.2(11)T | Cisco SRST 2.01 | This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers. |

| Command | Description |
|---|---|
| call-manager-fallback | Enables Cisco Unified SRST support and enters
                                          						call-manager-fallback configuration mode. |

| ip-address | Router IP address, typically one of the addresses of the
                                          						Ethernet port of the local router. |
|---|---|
| port port | (Optional) TCP port for credentials service communication.
                                          						Range is from 2000 to 9999. Cisco Unified CME default is 2444. SRST default is
                                          						2445. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(14)T | Cisco SRST 3.3 | This command was introduced for Cisco Unified SRST. |
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced for Cisco Unified CME. |

| Command | Description |
|---|---|
| credentials | Enters credentials configuration mode to configure a Cisco
                                          						Unified CME CTL provider certificate or an SRST router certificate. |
| ctl-service admin | Specifies a user name and password to authenticate the CTL
                                          						client during the CTL protocol. |
| debug credentials | Sets debugging on the credentials service that runs between
                                          						a Cisco Unified CME CTL provider and the CTL client or between an SRST router
                                          						and Cisco Unified Communications Manager. |
| show credentials | Displays the credentials settings on a Cisco Unified CME or
                                          						SRST router. |
| trustpoint (credentials) | Specifies the name of the trustpoint to be associated with
                                          						a Cisco Unified CME CTL provider certificate or with an SRST router
                                          						certificate. |

| seconds | Keepalive message transmission interval, in seconds. The
                                          						valid range is from 10 to 65535. The default timeout value is 30. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco SRST 1.0 | This command was introduced on the following platforms:
                                          						Cisco 2600 series and Cisco 3600 series multiservice routers; and Cisco IAD2420
                                          						series IADs. |
| 12.2(2)XT | Cisco SRST 2.0 | This command was implemented on Cisco 1750 and Cisco 1751
                                          						multiservice routers. |
| 12.2(8)T | Cisco SRST 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers. |
| 12.2(8)T1 | Cisco SRST 2.0 | This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers. |
| 12.2(11)T | Cisco SRST 2.01 | This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers. |

| Note | The keepalive command is applicable only after a Cisco IP phone has
                                       		  registered with the Cisco Unified SRST-enabled router. |
|---|---|

| Command | Description |
|---|---|
| call-manager-fallback | Enables Cisco Unified SRST feature support and enters
                                          						call-manager-fallback configuration mode. |

| phone-type | Type of phone. The following phone types are predefined in
                                          						the system: |
|---|---|
| 12SP | 12SP+ and 30VIP phones |
| 6901 | Cisco Unified IP Phone 6901 |
| 6911 | Cisco Unified IP Phone 6911 |
| 6921 | Cisco Unified IP Phone 6921 |
| 6941 | Cisco Unified IP Phone 6941 |
| 6961 | Cisco Unified IP Phone 6961 |
| 7902 | Cisco Unified IP Phone 7902 |
| 7905 | Cisco Unified IP Phone 7905 |
| 7906 | Cisco Unified IP Phone 7906 |
| 7910 | Cisco Unified IP Phone 7910 |
| 7911 | Cisco Unified IP Phone 7911 |
| 7912 | Cisco Unified IP Phone 7912 |
| 7920 | Cisco Unified IP Phone 7920 |
| 7921 | Cisco Unified IP Phone 7921 |
| 7925 | Cisco Unified IP Phone 7925 |
| 7926 | Cisco Unified IP Phone 7926 |
| 7931 | Cisco Unified IP Phone 7931 |
| 7935 | Cisco Unified IP Phone 7935 |
| 7936 | Cisco Unified IP Phone 7936 |
| 7937 | Cisco Unified IP Phone 7937 |
| 7940 | Cisco Unified IP Phone 7940 |
| 7941 | Cisco Unified IP Phone 7941 |
| 7941GE | Cisco Unified IP Phone 7941GE |
| 7942 | Cisco Unified IP Phone 7942 |
| 7945 | Cisco Unified IP Phone 7945 |
| 7960 | Cisco Unified IP Phone 7960 |
| 7961 | Cisco Unified IP Phone 7961 |
| 7961GE | Cisco Unified IP Phone 7961GE |
| 7962 | Cisco Unified IP Phone 7962 |
| 7965 | Cisco Unified IP Phone 7965 |
| 7970 | Cisco Unified IP Phone 7970 |
| 7971 | Cisco Unified IP Phone 7971 |
| 7975 | Cisco Unified IP Phone 7975 |
| 7985 | Cisco Unified IP Phone 7985 |
| CIPC | CIPC |
| IP-STE | IP-STE |
| anl | anl |
| ata | ata |
| bri | bri |
| vgc-phone | vgc-phone |
| max-lines | Maximum lines setting. The range is from 1 to 34. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco SRST 2.0 | This command was introduced on the following platforms:
                                          						Cisco 1750, Cisco 1751, Cisco 2600 series and Cisco 3600 series multiservice
                                          						routers, and Cisco IAD2420 series IADs. |
| 12.2(8)T | Cisco SRST 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers. |
| 12.2(8)T1 | Cisco SRST 2.0 | This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers. |
| 12.2(11)T | Cisco SRST 2.01 | This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers. |

| Note | You must specify this value during initial Cisco Unified SRST
                                       		  router configuration, before any Cisco IP phone actually registers with the
                                       		  Cisco Unified SRST router. You can modify the number of lines at a later time. |
|---|---|

| Command | Description |
|---|---|
| call-manager-fallback | Enables Cisco Unified SRST support and enters
                                          						call-manager-fallback configuration mode. |

| secure | Specifies the TLS port value. |
|---|---|
| non-secure | Specifies the TCP/UDP port value. |
| no-client-validation | Disables mTLS and available only for secure ports. |
| port-number | Port number. Range: 1–65535. The default for UDP/TCP is 5060; the default for TLS is 5061. |

| Release | Modification |
|---|---|
| 12.4(15)XY | This command was introduced. |
| 12.4(20)T | This command was integrated into Cisco IOS Release 12.4(20)T. |
| Cisco IOS XE Cupertino
                                                17.8.1a | Enhanced listen-port secure command to disable validation of client certificate and configure TLS port for SIP OAuth-based registrations from remote
                                          SIP endpoints. |

| Command | Description |
|---|---|
| shutdown | Disables the port. |

| location-tag | Identifier for the emergency response zone location. |
|---|---|
| priority 1-100 | Identifier (1-100) for the priority ranking of locations, 1
                                          						being the highest priority. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XY | Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1) | This command was introduced. |

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

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XY | Cisco Unified CME 4.2(1) Cisco Unified SRST 4.2(1) Cisco
                                          						Unified SIP SRST 4.2(1) | This command was introduced. |

| Command | Description |
|---|---|
| callback | Default phone number to contact if a 911 callback cannot
                                          						find the last 911 caller from the ERL. |
| elin | E.164 number used as the default ELIN if no matching ERL to
                                          						the 911 caller’s IP phone address is found. |
| expiry | Number of minutes a 911 call is associated to an ELIN in
                                          						case of a callback from the 911 operator. |
| voice emergency response settings | Creates a tag for identifying settings for E911 behavior. |

| Note | Effective with Cisco IOS Release 12.4(4)T, the max registrations command is not visible in Cisco IOS software. For similar
                                       		  functionality, use the maximum bit-rate (cm-fallback-video) command. |
|---|---|

| value | Digit, beginning with 0, that represents the maximum number
                                          						of registrations. The maximum registration value is platform dependent. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(15)ZJ | This command was introduced. |
| 12.3(4)T | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(4)T | This command was removed. |

| Command | Description |
|---|---|
| id (voice register pool) | Explicitly identifies a locally available individual Cisco
                                          						SIP IP phone or set of Cisco SIP IP phones. |
| voice register pool | Enables SIP SRST voice register pool configuration
                                          						commands. |

| max-no-of-conferences | The maximum number of simultaneous three-party conferences
                                          						allowed by the router. The maximum number of three-party conferences is
                                          						platform dependent: Cisco 1751
                                             						  router—8 Cisco 1760
                                             						  router—8 Cisco 2600
                                             						  series routers—8 Cisco 2600-XM
                                             						  series routers—8 Cisco 2801
                                             						  router—8 Cisco 2811,
                                             						  Cisco 2821, and Cisco 2851 routers—16 Cisco 3640 and
                                             						  Cisco 3640A routers—8 Cisco 3660
                                             						  router—16 Cisco 3725
                                             						  router—16 Cisco 3745
                                             						  router—16 Cisco 3800
                                             						  series router—24 |
|---|---|
| gain | (Optional) Increases the sound volume of VoIP and public
                                          						switched telephony network (PSTN) parties joining a conference call. The
                                          						allowable decibel units are -6 db, 0 db, 3 db, and 6 db. The default is -6 db. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.3(8)T4 | Cisco SRST 3.1 | The Cisco 2800 series routers were added. |
| 12.3(11)T | Cisco SRST 3.2 | The Cisco 3800 series routers were added. |
| 12.3(11)XL | Cisco SRST 3.2.2 | The gain keyword was added. |

| Command | Description |
|---|---|
| call-manager-fallback | Enables Cisco Unified SRST support and enters
                                          						call-manager-fallback configuration mode. |

| max-no-of-directories | Maximum number of directory numbers (dns) or virtual voice
                                          						ports supported by the router. The maximum possible number is
                                          						platform-dependent; see the Cisco IOS command-line interface (CLI) help. The
                                          						default is 0 directory numbers and 1 channel per virtual port. |
|---|---|
| dual-line | (Optional) Sets all Cisco Unified IP phones connected to a
                                          						Cisco Unified SRST router to one virtual voice port with two channels. |
| octo-line | (Optional) Sets all Cisco Unified IP phones connected to a
                                          						Cisco Unified SRST router to one virtual voice port with eight channels. |
| preference preference-order | (Optional) Sets the global preference for creating the VoIP
                                          						dial peers for all directory numbers that are associated with the primary
                                          						number. Range is from 0 to 10. Default is 0, which is the highest preference. |
| number octo-line | (Optional) Sets the maximum number of octo-line directory
                                          						numbers. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco SRST 1.0 | This command was introduced on the following platforms:
                                          						Cisco 2600 series and Cisco 3600 series multiservice routers, and Cisco IAD2420
                                          						series IADs. |
| 12.2(2)XT | Cisco SRST 2.0 | This command was implemented on Cisco 1750 and Cisco 1751
                                          						multiservice routers. |
| 12.2(8)T | Cisco SRST 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers. |
| 12.2(8)T1 | Cisco SRST 2.0 | This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers. |
| 12.2(11)T | Cisco SRST 2.01 | This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers. |
| 12.2(15)ZJ | Cisco SRST 3.0 | The dual-line keyword was added. |
| 12.3(4)T | Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.3(11)T | Cisco SRST 3.2 | The preference keyword was added. |
| 12.4(15)XZ | Cisco Unified SRST 4.3 | The octo-line keyword and its number argument were added. |
| 12.4(20)T | Cisco Unified SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Note | After you specify the maximum number of available directory
                                       		  numbers, you cannot reduce that number of directory numbers or virtual voice
                                       		  ports without rebooting the router. |
|---|---|

| Command | Description |
|---|---|
| alias (call-manager- fallback) | Provides a mechanism for rerouting calls to telephone
                                          						numbers that are unavailable during Cisco Unified Communications Manager
                                          						fallback. |
| call-forward busy (call-manager- fallback) | Configures call forwarding to another number when a Cisco
                                          						Unified IP phone is busy. |
| call-forward noan (call-manager- fallback) | Configures call forwarding to another number when no answer
                                          						is received from a Cisco Unified IP phone. |
| call-manager-fallback | Enables Cisco Unified SRST feature support and enters
                                          						call-manager-fallback configuration mode. |
| huntstop (call-manager- fallback) | Sets the huntstop attribute for the dial peers associated
                                          						with a Cisco Unified IP phone during Cisco Unified Communications Manager
                                          						fallback. |
| huntstop chan num (call-manager- fallback) | Sets the huntstop attribute for the dial peers, for
                                          						dual-line mode or octo-line mode (or both), associated with a Cisco Unified IP
                                          						phone during Cisco Unified Communications Manager fallback. |
| max-conferences (call- manager-fallback) | Sets the maximum number of simultaneous three-party
                                          						conferences supported by the router. |
| preference (dial-peer) | Indicates the preferred order of a dial peer within a hunt
                                          						group. |
| transfer-pattern | Allows Cisco Unified IP phones to transfer telephone calls
                                          						from callers outside the local IP network to another Cisco Unified IP phone. |
| transfer-system (call- manager-fallback) | Specifies the call transfer method for all Cisco Unified IP
                                          						phones on a Cisco Unified SRST router using the ITU-T H.450.2 standard. |

| max directory numbers | Maximum number of extensions (ephone-dns) supported by the Cisco router. The maximum number is version and platform dependent;
                                          type ? to display range. In Cisco CME 3.4 to Cisco Unified CME 7.0 and in Cisco SIP SRST 3.4 to Cisco Unified SIP SRST 7.0: Default is maximum number
                                                supported by platform. In Cisco Unified CME 7.1 and Cisco Unified SIP SRST 7.1 and later versions: Default is 0. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was introduced. |
| 12.4(22)YB | Cisco Unified CME 7.1 Cisco Unified SIP SRST 7.1 | The default value was changed to 0. |
| 12.4(24)T | Cisco Unified CME 7.1 Cisco Unified SIP SRST 7.1 | This command was integrated into Cisco IOS release 12.4(24)T. |
| Cisco IOS XE Amsterdam 17.2.1r | Cisco Unified SIP SRST 12.8 | Introduced support for YANG models. |

| Note | This command can also be used for Cisco Unified SIP SRST. |
|---|---|

| Command | Description |
|---|---|
| voice register dn | Enters voice register dn configuration mode to define an extension for a SIP phone line. |
| max-pool (voice register global) | Sets the maximum number of SIP voice register pools that are supported in a Cisco SIP SRST or Cisco CME environment. |

| max-voice-register-pools | Maximum number of SIP voice register pools supported by the Cisco router. The upper limit of voice register pools is platform-dependent;
                                          type ? for range. |
|---|---|

| Cisco IOS Release | Modification |
|---|---|
| Cisco IOS XE Release 17.2.1v | Command qualified for use in Cisco vManage CLI templates. |
| Cisco IOS XE Amsterdam 17.2.1r | Introduced support for YANG models. |

| Command | Description |
|---|---|
| voice register dn | Enters voice register dn configuration mode to define an
                                          						extension for a SIP phone line. |
| max-dn (voice register global) | Sets the maximum number of SIP voice register pools that
                                          						are supported in a Cisco SIP SRST or Cisco CME environment. |

| max-no-of-phones | Maximum number of Cisco IP phones supported by the router.
                                          						The maximum possible number is platform-dependent; refer to Cisco IOS
                                          						command-line interface (CLI) help. The default is 0. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco SRST 1.0 | This command was introduced on the following platforms:
                                          						Cisco 2600 series and Cisco 3600 series multiservice routers, and Cisco IAD2420
                                          						series IADs. |
| 12.2(2)XT | Cisco SRST 2.0 | This command was implemented on Cisco 1750 and Cisco 1751
                                          						multiservice routers. |
| 12.2(8)T | Cisco SRST 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers. |
| 12.2(8)T1 | Cisco SRST 2.0 | This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers. |
| 12.2(11)T | Cisco SRST 2.01 | This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers. |

| Note | Once you have specified the maximum number of Cisco IP phones, you
                                       		  cannot reduce that number without rebooting the router. |
|---|---|

| Command | Description |
|---|---|
| call-manager-fallback | Enables Cisco Unified SRST feature support and enters
                                          						call-manager-fallback configuration mode. |

| value | Sets the maximum IP phone video bandwidth, in kbps. The
                                          						range is 0 to 10000000. The default value is 10000000. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified SRST 4.0 | This command was introduced. |

| Command | Description |
|---|---|
| maximum bit-rate (telephony-service) | Sets the maximum bit-rate for all video-capable phones
                                          						associated with a Cisco Unified CME router. |

| number | Number
                                          						of presentation lines. Range: 1 to 100. Default: 0. See Table 1 for the number of presentation lines supported by each phone type. |
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
                                          					 Device | device-id | num-buttons | max-presentation |
|---|---|---|---|
| Cisco
                                          					 Unified IP Conference Station 7937G | 431 | 1 | 6 |
| Nokia E61 | 376 | 1 | 1 |

| Command | Description |
|---|---|
| device-id | Specifies the device ID for a phone type in an ephone-type template. |
| num-buttons | Sets
                                          						the number of line buttons supported by a phone type. |
| type | Assigns the phone type to an SCCP phone. |

| Cisco
                                    				  IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.4(3)M | Cisco Unified Enhanced SRST 10.5 | This
                                       					 command was introduced. |

| Command | Description |
|---|---|
| telephony-service | Enters
                                          						telephony-service configuration mode. |
| voice register global | Enters
                                          						voice register global configuration mode. |

| filename | Filename of the music file. The music file must be in the
                                          						system flash. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco SRST 2.0 | This command was introduced on the following platforms:
                                          						Cisco 1750, Cisco 1751, Cisco 2600 series and Cisco 3600 series multiservice
                                          						routers, Cisco IAD2420 series IADs. |
| 12.2(8)T | Cisco SRST 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725, Cisco 3745, and Cisco MC3810-V3 routers. |
| 12.2(8)T1 | Cisco SRST 2.0 | This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691 routers. |
| 12.2(11)T | Cisco SRST 2.01 | This command was integrated into Cisco IOS Release
                                          						12.2(11)T and implemented on the Cisco 1760 routers. |
| Cisco IOS XE Amsterdam 17.2.1r | Cisco Unified SIP SRST 12.8 | Introduced support for YANG models. |

| Note | Music-on-hold files can be .wav or .au file format; however, the
                                       		  file format must contain 8-bit 8-kHz data; for example, CCITT a-law or u-law
                                       		  data format. |
|---|---|

| Command | Description |
|---|---|
| call-manager-fallback | Enables Cisco Unified SRST support and enters
                                          						call-manager-fallback configuration mode. |
| moh-live (call- manager-fallback) | Specifies that a particular telephone number is to be used
                                          						for an outgoing call that is to be the source for an MOH stream for SRST. |

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

| file_size | Specifies a numeric value for the buffer MOH file size
                                          						between 64 KB and 10000 KB. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified SRST 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified SRST 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Note | When live-feed is enabled there is no file caching for MOH-group
                                       		  0. |
|---|---|

| Command | Description |
|---|---|
| moh-group | Allows to configure a MOH group. |
| moh | Enables music on hold from a flash audio feed |
| multicast moh | Enables multicast of the music-on-hold audio stream. |
| extension-range | Specifies the extension range for a clients calling a
                                          						voice-moh-group. |

| dn-number calling-number | Sets the MOH telephone number. The calling-number is a sequence of
                                          						digits that represent a telephone number. |
|---|---|
| out-call outcall-number | Indicates that the router is calling out for a live feed
                                          						that is to be used for MOH and specifies the number to be called. The outcall-number is a sequence of
                                          						digits that represent a telephone number, typically of an E&M port. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(11)T | Cisco SRST 3.3 | This command was introduced. |

| Command | Description |
|---|---|
| call-manager-fallback | Enables Cisco Unified SRST support and enters
                                          						call-manager-fallback configuration mode. |
| destination-pattern | Specifies either the prefix or the full E.164 telephone
                                          						number to be used for a dial peer. |
| moh (call-manager-fallback) | Enables MOH. |

| multicast-address | Declares the multicast-address header value of the MOH
                                          						packets that are to be multicast. |
|---|---|
| port | Declares the port header value of the MOH packets that are
                                          						to be multicast. |
| port | The desired port number. |
| route | (Optional) Sets the explicit IP address or addresses from
                                          						which the multicast packets will be transmitted. |
| ip-address-list | (Optional) Declares the IP address or addresses. The
                                          						ip-address-list argument accepts a maximum of four IP address entries separated
                                          						by a space. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| call-manager-fallback | Enables Cisco Unified SRST and enters call-manager-fallback configuration
                                          						mode. |
| ip source-address (call-manager- fallback) | Enables a router to receive messages from Cisco IP phones
                                          						through the specified IP addresses and ports. |
| moh (call-manager- fallback) | Enables MOH. |
| moh-live ( call- manager-fallback) | Specifies that a particular telephone number is to be used
                                          						for an outgoing call that is to be the source for an MOH stream for SRST. |

| seconds | Expiration time, in seconds. Range is from 600 to 99999.
                                          						Default is 86400 (24 hours). |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.3(11)T7 12.4 | Cisco SRST 3.3 | This command was replaced by the mwi-server command in SIP
                                          						user-agent configuration mode. |

| Command | Description |
|---|---|
| mwi relay (call-manager-fallback) | Enables a Cisco Unified SRST router to relay MWI
                                          						notification to remote Cisco IP phones. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(11)T7 12.4 | Cisco SRST 3.3 | This command was introduced. |

| Command | Description |
|---|---|
| mwi-server (SIP user-agent) | Specifies voice-mail server settings on a voice gateway or
                                          						user agent (UA). |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| mwi expires (call-manager- fallback) | Sets the expiration timer for registration for the client
                                          						or the server. |

| ip-address | IP address of the MWI server. |
|---|---|
| transport tcp | (Optional) Selects TCP as the transport layer protocol.
                                          						This is the default transport protocol. |
| transport udp | (Optional) Selects UDP as the transport layer protocol. |
| port port-number | (Optional) Specifies port number for the MWI server. Range
                                          						is from 2000 to 9999. Default is 5060. |
| reg-e164 | (Optional) Registers an E.164 number with a Session
                                          						Interface Protocol (SIP) proxy or registrar rather than an extension number.
                                          						Registering with an extension number is the default. |
| unsolicited | (Optional) Sends SIP NOTIFY for MWI without any need to
                                          						send a SUBSCRIBE from the Cisco Unified SRST router. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.3(11)T7 12.4 | Cisco SRST 3.3 | This command was replaced by the mwi-server command in SIP
                                          						user-agent configuration mode and the mwi reg-e164 command in
                                          						call-manager-fallback configuration mode. |

| Command | Description |
|---|---|
| mwi relay (call-manager-fallback) | Enables a Cisco Unified SRST router to relay MWI
                                          						notification to remote Cisco IP phones. |