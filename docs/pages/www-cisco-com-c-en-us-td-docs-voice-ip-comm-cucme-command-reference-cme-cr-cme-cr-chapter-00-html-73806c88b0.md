---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-command-reference-cme-cr-cme-cr-chapter-00-html-73806c88b0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/command/reference/cme_cr/cme_cr_chapter_00.html
retrieved_at: 2026-08-21T20:39:49.152525+00:00
---

Cisco Unified Communications Manager Express Command Reference

# Cisco Unified Communications Manager Express Command Reference

Updated: July 19, 2018

Chapter: Cisco Unified CME Commands: A

## Chapter: Cisco Unified CME Commands: A

# Cisco Unified CME Commands: A

## accept

To allow a
                              		  logical partitioning class of restriction (LPCOR) policy to accept calls
                              		  associated with another resource-group, use the accept command in LPCOR policy configuration mode. To reject calls associated with a
                              		  resource group, use the no form of
                              		  this command.

accept lpcor-group [ fac ]

no accept lpcor-group

### Syntax Description

lpcor-group

Name of
                                          						the LPCOR resource group.

fac

Enables
                                          						forced authorization code for calls from this resource group.

### Command Default

Calls from other
                              		  resource groups are rejected.

### Command Modes

LPCOR policy configuration (cfg-lpcor-policy)

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

15.1(3)T

Cisco
                                          						Unified CME 8.5

This
                                          						command was modified. The fac keyword was added to the accept command.

### Usage Guidelines

Use this command
                              		  to create a LPCOR policy by specifying the other resource groups from which
                              		  this resource group can accept calls. If a resource group is not explicitly set
                              		  to accept with this command, calls associated with that resource-group policy
                              		  are rejected. You can create one LPCOR policy for each resource group.

If you create a
                              		  LPCOR policy using the voice lpcor policy command and do not explicitly accept any
                              		  other resource groups by using the accept command, that policy blocks all incoming calls associated with any LPCOR
                              		  resource group other than its own. The fac keyword in the accept command
                              		  restricts the caller from routing to a destination LPCOR group without entering
                              		  a valid authorization code.

## Examples

The following
                              		  example shows the LPCOR policy for the resource group named sccp_phone_local.
                              		  It accepts calls from the resource groups analog_phone_local and
                              		  sip_phone_local but rejects calls from the group named analog_phone_remote
                              		  because it is not included in the policy.

```
voice lpcor policy sccp_phone_local
 accept analog_phone_local
 accept sip_phone_local
```

The following
                              		  example shows that sccp_phone_local blocks calls that are associated with any
                              		  other LPCOR policy because its policy does not accept other resource groups.

```
voice lpcor policy sccp_phone_local
```

The following
                              		  example shows that the policy local_phone is configured to not accept any calls
                              		  associated with itself. SIP phone 1 and SCCP phone 2 both belong to the
                              		  local_phone resource group and its policy prevents them from accepting calls
                              		  from each other.

```
voice register pool  1
 lpcor type local
 lpcor incoming local_phone
 lpcor outgoing local_phone
 id mac 0021.A02D.B360
 type 7960
 number 1 dn 1
!
voice lpcor custom
 group 1 local_phone
 group 2 remote_phone
 group 3 analog_phone
!
voice lpcor policy local_phone
 no accept local_phone
 accept analog_phone
!
ephone  2
 lpcor type local
 lpcor incoming local_phone
 lpcor outgoing local_phone
 mac-address 0021.A02D.B580
 type 7960
 button  1:10
```

The following
                              		  example shows that the authorization code is required by callers who belong to
                              		  the LocalUser group and RemoteUser group.

```
!
voice lpcor policy PSTNTrunk
 service fac
 accept Manager
 accept LocalUser fac
 accept RemoteUser fac
 no accept PSTNTrunk
 no accept IPTrunk
```

### Related Commands

Command

Description

show voice lpcor policy

Displays the LPCOR policy for the specified resource group.

voice lpcor custom

Defines the LPCOR resource groups on the Cisco Unified CME router.

voice lpcor policy

Creates a LPCOR policy for a resource group.

## access-digit

To define the access digit that phone users dial to request a
                              		  precedence call, use the access-digit command in voice MLPP configuration mode. To reset to the
                              		  default, use the no form of this command.

access-digit digit

no access-digit

### Syntax Description

digit

Single-digit number users dial. Range: 0 to 9. Default: 0.

### Command Default

Access digit is 0.

### Command Modes

Voice MLPP configuration (config-voice-mlpp)

## Command History

Cisco IOS Release

Modification

12.4(22)YB

This command was introduced.

12.4(24)T

This command was integrated into Cisco IOS Release
                                          						12.4(24)T.

### Usage Guidelines

This command defines the MLPP access digit that a user must dial when
                              		  making a precedence call. Phone users request a precedence call by dialing the
                              		  prefix NP, where N is the preconfigured MLPP access digit and P is the
                              		  requested precedence level, followed by the phone number.

## Examples

The following example shows the MLPP access digit set to 6:

```
Router(config)# voice mlpp Router(config-voice-mlpp)# access-digit 6
```

### Related Commands

Command

Description

mlpp preemption

Enables preemption capability on an SCCP phone or analog
                                          						FXS port.

preemption trunkgroup

Enables preemption capability on a trunk group.

preemption user

Enables preemption capability for all supported phones.

## addons

To define the
                              		  maximum number of add-on modules supported by the new Cisco Unified SIP IP
                              		  phone on Cisco Unified CME, use the addons command in voice register pool mode. To remove the add-on
                              		  modules , use the no form of this command.

addons max-addons

no addons max-addons

### Syntax Description

max-addons

Defines
                                          						the maximum number of addon modules that can be configured while defining the
                                          						pool for the phone. Range is 1 to 3.

### Command Default

The default value
                              		  of the addons is 0. When the reference-pooltype command is configured, the add-on module
                              		  value of the reference phone is inherited.

### Command Modes

Voice Register Pool-type Configuration (config-register-pooltype)

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

### Cisco Unified
                              		  CME

Use this command
                              		  to define the maximum number of addon modules for a Cisco Unified SIP IP phone
                              		  on Cisco Unified CME. When you use the no form of this command, the inherited
                              		  properties of the reference phone takes precedence over the default value.

## Examples

The following
                              		  example shows how to enter voice register pool configuration mode and define
                              		  the maximum number of addon modules for a Cisco Unified SIP IP phone on Cisco
                              		  Unified CME:

```
Router(config)# voice register pool 1 Router(config-register-pool-type)# type 9900 addon 1 CKEM 2 CKEM 3 CKEM Router(config-register-pool-type)# id mac 1234.4567.7891
```

### Related Commands

Command

Description

Adds a
                                          						new Cisco Unified SIP IP phone to Cisco Unified CME.

Defines a phone type for a SIP phone.

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

Use this command to create a comma separated text entry of the ERL’s
                              		  civic address. The address information must be entered to conform with the
                              		  NENA-2 Data Record specifications or the recommendations by the service
                              		  provider.

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

Specifies a string (up to 30 characters) used internally to
                                          						identify or describe the emergency response location.

subnet

Defines which IP phones are part of this ERL.

## addons

To define the
                              		  maximum number of add-on modules supported by the new Cisco Unified SIP IP
                              		  phone on Cisco Unified CME, use the addons command in voice register pool mode. To remove the add-on
                              		  modules , use the no form of this command.

addons max-addons

no addons max-addons

### Syntax Description

max-addons

Defines
                                          						the maximum number of addon modules that can be configured while defining the
                                          						pool for the phone. Range is 1 to 3.

### Command Default

The default value
                              		  of the addons is 0. When the reference-pooltype command is configured, the add-on module
                              		  value of the reference phone is inherited.

### Command Modes

Voice Register Pool-type Configuration (config-register-pooltype)

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

### Cisco Unified
                              		  CME

Use this command
                              		  to define the maximum number of addon modules for a Cisco Unified SIP IP phone
                              		  on Cisco Unified CME. When you use the no form of this command, the inherited
                              		  properties of the reference phone takes precedence over the default value.

## Examples

The following
                              		  example shows how to enter voice register pool configuration mode and define
                              		  the maximum number of addon modules for a Cisco Unified SIP IP phone on Cisco
                              		  Unified CME:

```
Router(config)# voice register pool 1 Router(config-register-pool-type)# type 9900 addon 1 CKEM 2 CKEM 3 CKEM Router(config-register-pool-type)# id mac 1234.4567.7891
```

### Related Commands

Command

Description

Adds a
                                          						new Cisco Unified SIP IP phone to Cisco Unified CME.

Defines a phone type for a SIP phone.

## after-hour exempt

To specify that an individual IP phone in Cisco Unified CME does not
                              		  have any of its outgoing calls blocked even though after-hour call blocking has
                              		  been enabled, use the after-hour exempt command in ephone or ephone-template configuration mode. To
                              		  remove the exemption, use the no form of this command.

after-hour exempt

no after-hour exempt

### Syntax Description

This command has no arguments or keywords.

### Command Default

The SCCP phone is not exempt from call blocking.

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

This command in the ephone-template configuration mode was
                                          						integrated into Cisco IOS 12.4(9)T.

### Usage Guidelines

Use this command to exempt an individual SCCP phone from call
                              		  blocking and enable the phone user to place outgoing calls regardless of
                              		  whether the outgoing called number matches the defined pattern of digits during
                              		  the call blocking periods.

By default, all IP phones in a Cisco Unified CME system are subject
                              		  to call blocking if the Call Blocking feature is configured.

If you use an ephone template to apply a command to a phone and you
                              		  also use the same command in ephone configuration mode for the same phone, the
                              		  value that you set in ephone configuration mode has priority.

## Examples

The following example shows how to configure this phone so that
                              		  outgoing calls are not blocked:

```
Router(config)# ephone 23 Router(config-ephone)# mac 00e0.8646.9242 Router(config-ephone)# button 1:33 Router(config-ephone)# after-hour exempt
```

### Related Commands

Command

Description

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

## after-hour login http

To unblock an individual IP phone in Cisco Unified CME that is
                              		  configured for after-hour call blocking, use the after-hour login http command in ephone, telephony-service or
                              		  ephone-template configuration mode. To disable after-hour login http feature,
                              		  use the no form of the command.

after-hour login htpp

no after-hour login htpp

### Syntax Description

This command has no arguments or keywords.

### Command Default

The after-hour login http feature is not enabled.

### Command Modes

Ephone configuration (config-ephone) Ephone-template configuration (config-ephone-template) T elephony-service configuration (config-telephony)

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

Use this command to log in to a phone to unblock the after hour block
                              		  and enable the phone user to place outgoing calls regardless of whether the
                              		  outgoing called number matches the defined pattern of digits during the call
                              		  blocking periods.

When you configure after-hours login http command, you will
                              		  experience slightly different login behavior compare to the current one. This
                              		  difference is because the after hours login mechanism is enhanced due to some
                              		  UI limitation in the current model. By default, after-hours login http is not
                              		  applied, which mean user will be using the existing after hours login
                              		  mechanism.

By default, all IP phones in a Cisco Unified CME system are subject
                              		  to call blocking if the Call Blocking feature is configured.

If you use an ephone template to apply a command to a phone and you
                              		  also use the same command in ephone configuration mode for the same phone, the
                              		  value that you set in ephone configuration mode has priority.

## Examples

The following example shows how to configure this phone with pin
                              		  login so that outgoing calls are not blocked:

```
Router(config)# ephone 6 Router(config-ephone)# mac 00e0.8646.242 Router(config-ephone)# button 1:33 Router(config-ephone)# Pin 123 Router(config-ephone)# after-hour login http
```

### Related Commands

Command

Description

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

## after-hours block
                        	 pattern

To define a
                              		  pattern of outgoing digits for Call Blocking from IP phones, use the after-hours block pattern command in telephony-service or ephone-template configuration
                              		  mode. To delete a call-blocking pattern, use the no form of
                              		  this command.

after-hours block pattern pattern-tag

no after-hours block pattern pattern-tag

### Syntax Description

pattern-tag

Identifier for a call-blocking pattern. Up to 100 call-blocking patterns can be
                                          						defined in separate commands.

pattern

Outgoing call digits to be matched for blocking, including specific digit
                                          						patterns and general regular expressions.

7-24

(Optional) If the 7-24 keyword is specified, the pattern is always blocked,
                                          						7 days a week, 24 hours a day. If the 7-24 keyword
                                          						is not specified, the pattern is blocked during the days and dates that are
                                          						defined with the after-hours day and after-hours date commands.

### Command Default

No pattern is
                              		  defined.

### Command Modes

Ephone-template (config-ephone-template)

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

12.4(4)T

Cisco
                                          						CME 3.4

Support
                                          						for this command was extended to all SCCP, H.323, SIP, and POTS calls that go
                                          						through the Cisco Unified CME router, including all incoming calls to the
                                          						router, except calls from an exempt phone.

12.4(15)XY

Cisco
                                          						Unified CME 4.2(1)

This
                                          						command was added to ephone-template configuration mode.

12.4(15)XZ

Cisco
                                          						Unified CME 4.3

This
                                          						command was added to ephone-template configuration mode.

12.4(20)T

Cisco
                                          						Unified CME 7.0

This
                                          						command was integrated into Cisco IOS Release 12.4(20)T.

15.3(2)T

Cisco
                                          						Unified CME 9.5

This
                                          						command was modified to include regular expressions as a value for the pattern argument.

### Usage Guidelines

Call Blocking
                              		  on IP phones is defined in the following way. First, one or more patterns of
                              		  outgoing digits (0-9) are defined using the after-hours block pattern command. Next, one or more time periods
                              		  during which calls that match those patterns are to be blocked are defined
                              		  using the after-hours date or after-hours day command or both. By default, all IP phones in
                              		  a Cisco Unified CME system are restricted during the specified time if at least
                              		  one pattern and at least one time period are defined.

Before Cisco
                              		  CME 3.4, Call Blocking is supported on IP phones and on analog phones connected
                              		  to SCCP-controlled analog telephone adaptors (Cisco ATA) or SCCP-controlled
                              		  foreign exchange station (FXS) ports. In Cisco CME 3.4 and later, the
                              		  call-blocking configuration applies to all SCCP, H.323, SIP and POTS calls that
                              		  go through the Cisco Unified CME router. All incoming calls to the router,
                              		  except calls from an exempt phone, are also checked against the after-hours
                              		  configuration.

Individual
                              		  phones can be exempted from call blocking using the after-hour exempt or the after-hours override-code command.

Blocked calls
                              		  return a fast-busy tone to the user for approximately 10 seconds before the
                              		  call is terminated and the line is returned to on-hook status.

In Cisco
                              		  Unified CME 9.5 and Cisco Unified SRST 9.5, support for after-hours pattern
                              		  blocking is extended to regular expression patterns for dial plans on Cisco
                              		  Unified SIP and Cisco Unified SCCP IP phones. With this support, users can add
                              		  a combination of fixed dial plans and regular expression-based dial plans.

When a call is
                              		  initiated after hours, the dialed number is matched against a combination of
                              		  dial plans. If a match is found, the call is blocked.

To enable
                              		  regular expression patterns to be included when configuring after-hours pattern
                              		  blocking, the after-hours block pattern command is modified to include regular
                              		  expressions as a value for the pattern argument.

For a summary of the basic Cisco IOS regular expression characters and their functions, see the Cisco Regular Expression Pattern
                              Matching Characters section of Terminal Services Configuration Guide.

## Examples

The following
                              		  example defines pattern 1, which blocks international calls after hours for a
                              		  Cisco Unified CME system that requires dialing 9 for external calls:

```
Router(config)# telephony-service Router(config-telephony)# after-hours block pattern 1 9011
```

The following
                              		  example shows how to configure several after-hours block patterns of regular
                              		  expressions:

```
Router# configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)# telephony-service 
Router(config-telephony)# after-hours block pattern 1 ?
  WORD  Specific block pattern or a regular expression for after-hour block
        pattern
Router(config-telephony)# after-hours block pattern 1 1234 Router(config-telephony)# after-hours block pattern 2 .T Router(config-telephony)# after-hours block pattern 3 987654([1-3])+ Router(config-telephony)# after-hours block pattern 4 98765432[1-9] Router(config-telephony)# after-hours block pattern 5 98765(432|422|456)
```

### Related Commands

Command

Description

after-hour exempt

Specifies that an IP phone does not have any of its outgoing calls blocked
                                          						although call blocking is defined.

after-hours date

Defines a recurring period based on date during which outgoing calls that match
                                          						defined block patterns are blocked on IP phones.

after-hours day

Defines a recurring period based on day of the week during which outgoing calls
                                          						that match defined block patterns are blocked on IP phones.

after-hours override-code

Specifies that call blocking on an IP phone can be overridden by entering a
                                          						defined code.

after-hours pstn-prefix

Specifies that trunk lines on an IP phone are blocked similarly to that
                                          						configured for nonPSTN lines.

ephone-template (ephone)

Applies template to a SCCP phone.

## after-hours date

To define a recurring period based on date during which outgoing
                              		  calls that match defined block patterns are blocked on IP phones, use the after-hours date command in ephone-template or telephony-service configuration
                              		  mode. To delete a defined time period, use the no form of this command.

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
                                          						format using a 24-hour clock. The stop time that is entered will be the next
                                          						available time that follows the start time. The value 24:00 is not valid. If
                                          						00:00 is entered as a stop time, it is changed to 23:59. If 00:00 is entered
                                          						for both start time and stop time, calls are blocked for the entire 24-hour
                                          						period on the specified date.

### Command Default

No time period based on date is defined for call blocking.

### Command Modes

Ephone-template configuration (config-ephone-temp)

Telephony-service configuration (config-ephone)

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

12.4(15)XY

Cisco Unified CME 4.2(1)

This command was added to ephone-template configuration
                                          						mode.

12.4(15)XZ

Cisco Unified CME 4.3

This command was added to ephone-template configuration
                                          						mode.

12.4(20)T

Cisco Unified CME 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

Use this command to define call blocking that recurs annually on the
                              		  date specified in the command. Call blocking on IP phones is defined as
                              		  follows:

- First, one or more patterns of outgoing digits (0-9) are defined
                                 			 using the after-hours block pattern command.

- Next, one or more time periods during which calls that match those
                                 			 patterns are to be blocked are defined using the after-hours date or a fter-hours da y command or both.

By default, all IP phones in a Cisco Unified CME system are
                              		  restricted during the specified time if at least one pattern and at least one
                              		  time period are defined. Individual IP phones can be exempted from call
                              		  blocking using the after-hour exempt or after-hours override-code commands.

## Examples

The following example defines January 1 as an entire day on which
                              		  calls that match the pattern specified in the after-hours block pattern command are blocked:

```
Router(config)# telephony-service Router(config-telephony)# after-hours date jan 1 00:00 00:00
```

### Related Commands

Command

Description

after-hour exempt

Specifies that an IP phone does not have any of its
                                          						outgoing calls blocked although call blocking is defined.

after-hours block pattern

Defines a pattern of digits (0-9) for blocking outgoing
                                          						calls from IP phones.

after-hours day

Defines a recurring period based on day of the week during
                                          						which outgoing calls that match defined block patterns are blocked on IP
                                          						phones.

after-hours override-code

Specifies that call blocking on an IP phone can be
                                          						overridden by entering a defined set of digits (0-9).

after-hours pstn-prefix

Specifies that trunk lines on an IP phone are blocked
                                          						similarly to that configured for nonPSTN lines.

ephone-template (ephone)

Applies template to SCCP phone.

## after-hours day

To define a recurring period based on day of the week during which
                              		  outgoing calls that match defined block patterns are blocked on IP phones, use
                              		  the after-hours day command in ephone-template or telephony-service configuration
                              		  mode. To delete a defined time period, use the no form of this command.

after-hours day day start-time stop-time

no after-hours day day

### Syntax Description

day

Abbreviated day of the week. The following abbreviations
                                          						for day of the week are valid: sun , mon , tue , wed , thu , fri , sat .

start-time stop-time

Beginning and ending times for call blocking, in an HH:MM
                                          						format using a 24-hour clock. The stop time that is entered will be the next
                                          						available time that follows the start time. The value 24:00 is not valid. If
                                          						00:00 is entered as a stop time, it is changed to 23:59. If 00:00 is entered
                                          						for both start time and stop time, calls are blocked for the entire 24-hour
                                          						period on the specified day.

### Command Default

No time period based on day of the week is defined for call blocking.

### Command Modes

Ephone-template configuration (config-ephone-template)

Telephony-service configuration (config-ephone)

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

12.4(15)XY

Cisco Unified CME 4.2(1)

This command was added to ephone-template configuration
                                          						mode.

12.4(15)XZ

Cisco Unified CME 4.3

This command was added to ephone-template configuration
                                          						mode.

12.4(20)T

Cisco Unified CME 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

Use this command to define call blocking during the hours between the
                              		  start time and stop time on the day of the week that is specified in this
                              		  command. This time period recurs weekly unless it is removed using the no form of this command.

Call blocking on IP phones is defined as follows:

- First, one or more patterns of outgoing digits (0-9) are defined
                                 			 using the after-hours block pattern command.

- Next, one or more time periods during which calls that match those
                                 			 patterns are to be blocked are defined using the after-hours date or after-hours da y command or both.

By default, all IP phones in a Cisco Unified CME system are
                              		  restricted during the specified time if at least one pattern and at least one
                              		  time period are defined. Individual phones can be exempted from call blocking
                              		  using the after-hour exempt or after-hours override-code commands.

## Examples

The following example defines the period from Monday night at 7 p.m.
                              		  to Tuesday morning at 7 a.m. as an after-hours call-blocking period:

```
Router(config)# telephony-service Router(config-telephony)# after-hours day mon 19:00 07:00
```

### Related Commands

Command

Description

after-hour exempt

Specifies that an IP phone does not have any of its
                                          						outgoing calls blocked although call blocking is defined.

after-hours block pattern

Defines a pattern of digits (0-9) for blocking outgoing
                                          						calls from IP phones.

after-hours date

Defines a recurring period based on date during which
                                          						outgoing calls that match defined block patterns are blocked on IP phones.

after-hours override-code

Specifies that call blocking on an IP phone can be
                                          						overridden by entering a defined set of digits (0-9).

after-hours pstn-prefix

Specifies that trunk lines on an IP phone are blocked
                                          						similarly to that configured for nonPSTN lines.

ephone-template (ephone)

Applies template to SCCP phone.

## after-hours override-code

To specify that a defined blocking pattern can be overridden, use the after-hours override-code command in ephone-template or
                              		  telephony-service configuration mode. To remove the exemption, use the no form of this command.

after-hours override-code pattern

no after-hours override-code pattern

### Syntax Description

pattern

Specifies the pattern of digits (0-9) that must be dialed
                                          						by the phone user to override the call blocking rules. The override code is
                                          						provided to the phone user by the system administrator.

### Command Default

No override is defined.

### Command Modes

Ephone-template configuration (config-ephone-template)

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)XY

Cisco Unified CME 4.2(1)

This command was introduced.

12.4(15)XZ

Cisco Unified CME 4.3

This command was added to ephone-template configuration
                                          						mode.

12.4(20)T

Cisco Unified CME 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

Use this command to allow a phone user to override call blocking
                              		  rules and enable the phone user to place outgoing calls regardless of whether
                              		  the outgoing called number matches the defined pattern of digits during the
                              		  call blocking periods.

By default, all IP phones in a Cisco Unified CME system are subject
                              		  to call blocking if the Call Blocking feature is configured. By entering the
                              		  override code as defined by the system administrator, the phone user can
                              		  override all call blocking rules.

The after-hours override-code command, configured by either
                              		  ephone-template or telephony-service, overrides any global telephony-service
                              		  call block configuration. If the after-hour exempt command is configured, it has priority over
                              		  the after-hours override-code command.

## Examples

The following example defines a blocking pattern using
                              		  telephony-service configuration which can be overridden using the override code
                              		  of 1234 :

```
Router(config)# telephony-service Router(config-telephony)# after-hours block pattern 1 91900 Router(config-telephony)# after-hours day mon 19:00 07:00 Router(config-telephony)# after-hours date Jan 25 00:00 07:00 Router(config-telephony)# after-hours override-code 1234
```

### Related Commands

Command

Description

after-hour exempt

Specifies that an IP phone does not have any of its
                                          						outgoing calls blocked although call blocking is defined.

after-hours block pattern

Defines a pattern of digits (0-9) for blocking outgoing
                                          						calls from IP phones.

after-hours date

Defines a recurring period based on date during which
                                          						outgoing calls that match defined block patterns are blocked on IP phones.

after-hours day

Defines a recurring period based on day of the week during
                                          						which outgoing calls that match defined block patterns are blocked on IP
                                          						phones.

after-hours pstn-prefix

Specifies that trunk lines on an IP phone are blocked
                                          						similarly to that configured for non PSTN lines.

ephone-template (ephone)

Applies a template to an ephone.

## after-hours pstn-prefix

To specify that all configured blocking patterns apply to trunk or
                              		  PSTN lines, use the after-hours pstn-prefix command in telephony-service
                              		  configuration mode. To delete call blocking configuration for PSTN lines, use
                              		  the no form of this command.

after-hours pstn-prefix tag pattern

no after-hours pstn-prefix tag pattern

### Syntax Description

tag

Identifier for a PSTN call-blocking pattern. Up to 4
                                          						call-blocking patterns can be defined in separate commands.

pattern

Outgoing call digits (0-9) to be matched for PSTN blocking.

### Command Default

No pattern is defined.

### Command Modes

Telephony-service configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(15)XY

Cisco Unified CME 4.2(1)

This command was introduced.

12.4(15)XZ

Cisco Unified CME 4.3

This command was added to ephone-template configuration
                                          						mode.

12.4(20)T

Cisco Unified CME 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

Use the after-hours pstn-prefix command to indicate that the
                              		  after-hours call blocking patterns are configured to include one or more PSTN
                              		  access digits that are normally dialed by phone users using regular ephone-dn
                              		  lines. For example, the patterns are configured with a leading digit 9 to
                              		  correspond to the conventional “dial 9 for outside line.” The after-hours pstn-prefix command instructs the system to skip
                              		  over the PSTN prefix digits (in the blocking patterns) for calls that are
                              		  dialed directly to the PSTN on ephone-dns that are configured using the trunk
                              		  feature. These lines do not require the user to dial a PSTN access code (for
                              		  example, 9) because they are configured to directly connect to the PSTN FXO
                              		  ports. For example, a user of a regular ephone-dn would dial 9-1-900-xxx-xxxx,
                              		  whereas a user on a trunk ephone-dn would omit the leading 9 and dial only
                              		  1-900-xxx-xxxx. The blocking pattern would be configured as 91900 to restrict calls on regular ephone-dn
                              		  lines, and this pattern would be interpreted as 1900 on ephone-dns configured
                              		  using the trunk feature. If you do not specify the after-hours pstn-prefix command, then no blocking is performed
                              		  on calls dialed on trunk ephone-dn lines.

Call blocking on IP phones is defined as follows:

- First, one or more patterns of outgoing digits (0-9) are defined
                                 			 using the after-hours block pattern command.

- Next, one or more time periods during which calls that match those
                                 			 patterns are to be blocked are defined using the after-hours date, the after-hours day, or both commands.

By default, all IP phones in a Cisco Unified CME system are
                              		  restricted during the specified time if at least one pattern and at least one
                              		  time period are defined.

Blocked calls return a fast-busy tone to the user for approximately
                              		  10 seconds before the call is terminated and the line is returned to on-hook
                              		  status.

## Examples

The following example defines a blocking pattern using
                              		  telephony-service configuration which is applied to a PSTN line:

```
Router(config)# telephony-service Router(config-telephony)# after-hours block pattern 1 91900 Router(config-telephony)# after-hours pstn-prefix 1 9 Router(config-telephony)# after-hours day mon 19:00 07:00 Router(config-telephony)# after-hours date Jan 25 00:00 07:00
```

### Related Commands

Command

Description

after-hour exempt

Specifies that an IP phone does not have any of its
                                          						outgoing calls blocked although call blocking is defined.

after-hours block pattern

Defines a pattern of digits (0-9) for blocking outgoing
                                          						calls from IP phones.

after-hours date

Defines a recurring period based on date during which
                                          						outgoing calls that match defined block patterns are blocked on IP phones.

after-hours day

Defines a recurring period based on day of the week during
                                          						which outgoing calls that match defined block patterns are blocked on IP
                                          						phones.

after-hours override-code

Specifies that call blocking on an IP phone can be
                                          						overridden by entering a defined series of digits (0-9).

## allow watch

To allow a directory number on a phone registered to Cisco Unified
                              		  CME to be watched in a presence service, use the allow watch command in ephone-dn, ephone-dn-template, or
                              		  voice register dn configuration mode. To reset to the default condition, use
                              		  the no form of this command.

allow watch

no allow watch

### Syntax Description

This command has no arguments or keywords.

### Command Default

Watching of the phone line is disabled.

### Command Modes

Ephone-dn configuration (config-ephone) Ephone-dn-template configuration (config-ephone-dn-template) Voice register dn configuration (config-register-dn)

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

This command controls whether a phone line associated with a
                              		  directory number can be watched as part of a presence service. The directory
                              		  number is enabled as a presentity that can be watched by internal and external
                              		  watchers. Presence service must be enabled on Cisco Unified CME. Another phone,
                              		  acting as a watcher, can monitor the status of this phone line when the blf-speed-dial or presence call-list command is enabled for that phone.

If you use an ephone-dn template to apply a command to a directory
                              		  number and you also use the same command in ephone-dn configuration mode, the
                              		  value that you set in ephone-dn configuration mode has priority over the
                              		  ephone-dn template configuration.

## Examples

The following example shows that the extension associated with voice
                              		  register dn 2 can be watched by the phone associated with voice register pool
                              		  1:

```
Router(config)# voice register dn 2 Router(config-register-dn)# number 2102 Router(config-register-dn)# allow watch Router(config)# voice register pool 1 Router(config-register-pool)# id mac 0015.6247.EF90 Router(config-register-pool)# type 7971 Router(config-register-pool)# number 1 dn 2 Router(config-register-pool)# blf-speed-dial 1 2102 label 2102
```

### Related Commands

Command

Description

blf-speed-dial

Enables Busy Lamp Field (BLF) monitoring for a speed-dial
                                          						number on a phone registered to Cisco Unified CME.

presence

Enables presence service and enters presence configuration
                                          						mode.

presence call-list

Enables BLF monitoring for call lists and directories on
                                          						phones registered to Cisco Unified CME.

presence enable

Allows the router to accept incoming presence requests.

show presence global

Displays configuration information about the presence
                                          						service.

show presence subscription

Displays information about active presence subscriptions.

## anonymous block

To enable anonymous call blocking in a SIP phone template, use the anonymous block command in voice register template
                              		  configuration mode. To return to the default, use the no form of this command.

anonymous block

no anonymous block

### Syntax Description

This command has no arguments or keywords.

### Command Default

Disabled

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

This command blocks incoming calls in which the caller is not
                              		  identified. To apply a template to a SIP phone, use the template command in voice register pool
                              		  configuration mode.

## Examples

The following example shows how to set anonymous call blocking in
                              		  template 1:

```
Router(config)# voice register template 1 Router(config-register-temp)# anonymous block
```

### Related Commands

Command

Description

caller-id block (voice register template)

Enables caller-ID blocking for outbound calls from a SIP
                                          						phone.

template (voice register pool)

Applies a template to a SIP phone.

## application (telephony-service)

To select a session-level application for all extensions (ephone-dns)
                              		  in a Cisco Unified CME, use the application command in telephony-service
                              		  configuration mode. To disable use of an application for all extensions, use
                              		  the no form of this command.

application application-name

no application

### Syntax Description

application-name

Interactive voice response (IVR) application name.

### Command Default

No application is selected for all extensions.

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

### Usage Guidelines

Use this command to assign a Tool Command Language (Tcl) IVR
                              		  application to all extensions served by the CME router.

Use the show call application voice summary command to display a list of applications.

## Examples

The following example sets the IVR application for all phones:

```
Router(config)# telephony-service Router(config-telephony) application TCL IVR
```

### Related Commands

Command

Description

show call application voice summary

Displays information about voice applications.

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

Voice register global configuration (config-register-global)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was introduced.

### Usage Guidelines

During Cisco Unified CallManager Express (Cisco Unified CME) or Cisco
                              		  Unified Session Initiation Protocol (SIP) Survivable Remote Site Telephony
                              		  (SRST) registration, a dial peer is created for each SIP phone and that dial
                              		  peer includes the default session application. The application command allows you to change the
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

voice register pool

Enters voice register pool configuration mode for SIP
                                          						phones.

## application (voice register pool)

To select the session-level application for the dial peer associated
                              		  with an individual Session Initiation Protocol (SIP) phone in a Cisco Unified
                              		  CallManager Express (Cisco Unified CME) environment or for a group of phones in
                              		  a Cisco Unified SIP Survivable Remote Site Telephony (SRST) environment, use
                              		  the application command in voice register pool configuration mode. To disable
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

## apply-config

To dynamically apply the phone configuration on Cisco Unified SIP IP
                              		  phones 8961, 9951, and 9971, without restarting the phones, use the apply-config command in voice register global
                              		  and voice register pool configuration modes.

apply-config

### Syntax Description

This command has no arguments or keywords.

### Command Default

Apply-config is not enabled by default.

### Command Modes

Voice register global Voice register pool

## Command History

Cisco IOS Release

Cisco Product

Modification

15.1(4)M

Cisco Unified CME 8.6

This command was introduced.

### Usage Guidelines

Use this command to dynamically apply the phone configuration on
                              		  Cisco Unified SIP IP phones 8961, 9951, and 9971.Once you configure the
                              		  apply-config command, you are not required to restart the phone. The phone
                              		  restarts by itself or dynamically applies the changes to the phone
                              		  configuration without restarting.

## Examples

The following example shows the apply-config command configured in
                              		  voice register pool 5 :

Router# configure terminal

Router(config)#voice register pool 5

Router(config-register-pool)#apply-config

### Related Commands

Command

Description

camera

Enables USB camera capability on Cisco Unified IP Phones
                                          						9951 and 9971

video

Enables video capability on Cisco Unified SIP IP Phones
                                          						9951 and 9971

## ata-ivr-pwd

To define a password to access interactive voice response (IVR) and
                              		  change the default phone settings on Cisco Analog Telephone Adaptors, use the ata-ivr-pwd command in voice register pool
                              		  configuration mode. To return to the default, use the no form of the command.

ata-ivr-pwd [0|6] password

no ata-ivr-pwd

### Syntax Description

password

Four-digit string to be used as password to access IVR.
                                          						Password string must contain numbers 0 to 9.

The 0 in the parameter [0|6] mentioned in the CLI command represents plain, unencrypted text and 6 represents level 6 password
                                          encryption.

### Command Default

No valid password is set.

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

The command was enhanced for password encryption. Password policy is not enforced, as the command supports a four-digit password.

## Examples

The following example shows how 1234 is defined as the password to
                              		  access IVR on Cisco ATA-187:

```
voice service voip
 allow-connections sip to sip
 fax protocol t38 version 0 ls-redundancy 0 hs-redundancy 0 fallback pass-through g711ulaw
voice register pool  11 ata-ivr-pwd 1234 id mac 93FE.12D8.2301
 session-transport tcp
 type ATA-187
number 1 dn 33
 username ata112 password cisco
 codec g711ulaw
```

### Related Commands

Command

Description

voice register pool

Enters voice register pool configuration mode and creates a
                                          						pool configuration for Cisco Unified SIP IP phones in Cisco Unified CME.

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

## attendant-console

To specify the phone number of the MLPP attendant-console service,
                              		  use the attendant-console command in voice MLPP configuration mode. To revert to the
                              		  default, use the no form of this command.

attendant-console number redirect-timer seconds

no attendant-console

### Syntax Description

number

Pilot number of the MLPP attendant-console service, such as
                                          						the Cisco Unified CME basic automatic call distribution (B-ACD) and
                                          						auto-attendant (AA) service.

seconds

Number of seconds that a call rings before being redirected
                                          						to the attendant-console service. Range: 10 to 60.

### Command Default

MLPP call is not diverted to an attendant-console service.

### Command Modes

V oice MLPP configuration (config-voice-mlpp)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(22)YB

Cisco Unified CME 7.1

This command was introduced.

12.4(24)T

—

This command was integrated into Cisco IOS Release
                                          						12.4(24)T.

### Usage Guidelines

This command enables Cisco Unified CME to divert all unanswered
                              		  precedence calls above Routine to the specified target number after the
                              		  specified period of time. This target directory number typically specifies the
                              		  pilot number of the attendant-console service that is used as a destination of
                              		  last resort for forwarded MLPP calls.

## Examples

The following example shows that any MLPP call that is not answered
                              		  after 30 seconds is redirected to extension 81005, which is the extension of
                              		  the BACD queue.

```
Router(config)# voice mlpp Router(config-voice-mlpp)# attendant-console 81005 redirect-timer 30
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

service

Associates a dial peer with an auto-attendant (AA) service.

## audible-tone

To configure
                              		  audible tones to indicate successful join or unjoin and login or logout from
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

Use the audible-tone command to set an audible tone
                              		  to confirm successful join or unjoin and log in or log out from specific hunt
                              		  groups.

## Examples

The following
                              		  example shows how to configure audible tone in ephone configuration mode:

```
Router(config)# ephone 1 Router(config-ephone)# audible-tone
```

The following
                              		  example shows how to configure an audible tone in ephone-template configuration
                              		  mode:

```
Router(config)# ephone-template 1 Router(config-ephone-template)# audible-tone
```

### Related Commands

Command

Description

ephone-hunt group

Configures an ephone hunt group in Cisco Unified CME.

voice-hunt group

Configures a voice hunt group in Cisco Unified CME.

## authen-method

To define authentication method for a vpn-profile, use the authen-method command in vpn-profile configuration mode. To disable the
                              		  authentication method, use the no form of this command.

authen-method [ both | none | password ]

no authen-method

### Syntax Description

both

Requires both user id and password to authenticate.

password

Requires only password to authenticate.

none

Does not allows authentication.

### Command Default

Both User ID and Password are required for authentication.

### Command Modes

Voice service voip (cfg-lpcor-policy)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.1(3)T

Cisco Unified CME 8.5

This command was introduced.

### Usage Guidelines

Use this command to define authentication method for a vpn-profile.
                              		  You can define an authen-method with both user id and password, or you can
                              		  define an authen-method with just password. You can choose to not allow any
                              		  authentication method by configuring authen-method none.

## Examples

The following example shows the authen-method both defined for
                              		  vpn-profile 2:

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
  authen-method both
  password-persistent enable
  host-id-check enable
 vpn-profile 4
  fail-connect-time 50
```

### Related Commands

Command

Description

vpn-profile

Defines a VPN-profile.

## authenticate (voice register global)

To define the authenticate mode for SIP phones in a Cisco Unified CME
                              		  or Cisco Unified SRST system, use the authenticate command in voice register global configuration mode. To return
                              		  to the default, use the no form of this command.

### Cisco IOS Release 12.4(11)XJ and Later Releases

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

Voice register global configuration (config-register-global)

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

## authentication credential

To create an entry for an application’s credential in the database
                              		  used by the Cisco Unified CME authentication server, use the authentication credential command in telephony-service
                              		  configuration mode. To remove the credential, use the no form of this command.

authentication credential application-name password

no authentication credential application-name password

### Syntax Description

application-name

String sent by application to identify itself to the
                                          						server. Length of string: 1 to 15characters.

password

String sent by application to identify itself to the
                                          						server. Length of string: 1 to 15 characters.

The 0 in the parameter [0|6] mentioned in the CLI command represents plain, unencrypted text and 6 represents level 6 password
                                          encryption.

### Command Default

The credential is not stored in the database.

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

Cisco IOS XE Gibraltar 16.11.1a Release

Unified CME 12.6

The command was enhanced for password encryption, based on Unified CME password policy.

### Usage Guidelines

This command stores a credential in the database used by the Cisco
                              		  Unified CME authentication server. The authentication server uses this data to
                              		  authenticate and authorize HTTP requests from IP phones in Cisco Unified CME.

Up to eight credentials can be stored in the database for the Cisco
                              		  Unified CME authentication server.

For applications other than Extension Mobility, the credential must
                              		  be created in the application.

From Unified CME 12.6 onwards, you must configure password encryption using the parameters [0|6] . This in accordance with Unified CME Password Policy. The 0 in the parameter [0|6] mentioned in the CLI command represents
                              plain, unencrypted text and 6 represents level 6 password encryption.

## Examples

The following example shows how to configure IP phones in Cisco
                              		  Unified CME to request authorization from the internal authentication server.
                              		  When the IP phone receives a command from the application, the phone requests
                              		  authorization from the Cisco Unified CME authentication server to execute that
                              		  command. The authorization request from the phone includes the specified
                              		  credential. The authentication server compares the credential in its database
                              		  to the one in the request, and authorizes or rejects the request based on the
                              		  results.

```
Router(config)# telephony-service Router(config-telephony)# authentication credential att psswrd Router(config-telephony)# url authentication http://192.0.2.0/CCMCIP/authenticate.asp att psswrd Router(config-telephony)#
```

### Related Commands

Command

Description

url authentication

Specifies authentication server and credential to be used
                                          						by an application.

## auto assign

To automatically assign an already defined telephone or extension
                              		  number to button 1 of Cisco Unified IP phones as they register for service with
                              		  a Cisco Unified CME router, use the auto assign command in telephony-service configuration mode. To return to the default
                              		  of not automatically assigning dn-tags, use the no form of this command.

auto assign dn-tag to dn-tag [ type phone-type ] [ cfw extension-number timeout seconds ]

no auto assign dn-tag to dn-tag [ type phone-type ] [ cfw extension-number timeout seconds ]

### Syntax Description

dn-tag to dn-tag

Range of ephone-dn tags for already configured ephone-dns,
                                          						from which a tag is assigned to the ephone being created.

The maximum number of directory numbers supported is
                                          						version and platform dependent. Type ? to display the value.

type phone-type

(Optional) Type of Cisco Unified IP phone to which to
                                          						restrict automatic assignment of ephone-dn tags. Valid entries are the
                                          						following:

- 12SP —12SP+ and 30VIP phones.

- 7902 —Cisco Unified IP Phone
                                             						  7902G.

- 7905— Cisco Unified IP Phone
                                             						  7905G.

- 7906— Cisco Unified IP Phone
                                             						  7906G.

- 7910— Cisco Unified IP Phone
                                             						  7910 and 7910G.

- 7911 —Cisco Unified IP Phone
                                             						  7911G.

- 7912— Cisco Unified IP Phone
                                             						  7912G.

- 7920 —Cisco Unified Wireless IP
                                             						  Phone 7920.

- 7921 —Cisco Unified Wireless IP
                                             						  Phone 7921.

- 7931 —Cisco Unified Wireless IP
                                             						  Phone 7931G.

- 7935— Cisco Unified IP
                                             						  Conference Station 7935.

- 7936— Cisco Unified IP
                                             						  Conference Station 7936.

- 7937 —Cisco Unified IP
                                             						  Conference Station 7937

- 7940— Cisco Unified IP Phones
                                             						  7940 and 7940G.

- 7941 —Cisco Unified IP Phone
                                             						  7941G.

- 7941GE —Cisco Unified IP Phone
                                             						  7941G-GE.

- 7942 —Cisco Unified IP Phone
                                             						  7942.

- 7945 —Cisco Unified IP Phone
                                             						  7945.

type phone-type

- 7960— Cisco Unified IP Phones
                                             						  7960 and 7960G.

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

- CIPC —Cisco IP Communicator.

- all —All ephone types.

- anl —Analog gateway.

- ata— Cisco ATA-186 or Cisco
                                             						  ATA-188.

- bri —SCCP gateway.

- vgc-phone —vg248 phone emulation
                                             						  for analog phone.

cfw

(Optional) Automatically assigned ephone-dns are
                                          						provisioned for call-forward busy and no-answer to the specified extension
                                          						number.

extension-number

(Optional) Extension number to which calls are to be
                                          						forwarded on busy and no-answer conditions.

timeout seconds

(Optional; required if the cfw keyword is used) Amount of
                                          						time, in seconds, to wait when a call is not being answered before forwarding
                                          						it. Range: 3 to 60000.

### Command Default

Ephone-dn tags are not automatically assigned to registering Cisco
                              		  Unified IP phones.

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

The 7941 , 7941GE , 7961 , and 7961GE keywords were added.

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

This command wasintegrated into Cisco IOS Release
                                          						12.4(15)T.

12.4(15)T1

Cisco Unified CME 4.1(1)

The 7942 , 7945 , 7962 , 7965 , and 7975 keywords were introduced.

12.4(11)XW3

Cisco Unified CME 4.2

The 7942 , 7945 , 7962 , 7965 , and 7975 keywords were introduced.

12.4(15)XY

Cisco Unified CME 4.2(1)

The 7942 , 7945 , 7962 , 7965 , and 7975 keywords were introduced.

12.4(15)XZ

Cisco Unified CME 4.3

The 7942 , 7945 , 7962 , 7965 , and 7975 keywords were introduced.

12.4(20)T

Cisco Unified CME 7.0

The 7937 keyword was introduced and this command was
                                          						integrated into Cisco IOS Release 12.4(20)T.

### Usage Guidelines

Use this command to create an ephone configuration for a Cisco
                              		  Unified IP phone whose MAC address is not explicitly configured as it registers
                              		  in Cisco Unified CME. The system-created ephone configuration includes the MAC
                              		  address of the Cisco Unified IP phone being registered and an already-defined
                              		  available ephone-dn assigned to button 1 of this phone.

The auto-reg-ephone command must be enabled
                              		  (default) to use this command. If the auto registration feature is disabled, a
                              		  Cisco Unified IP phone whose MAC address is not explicitly configured cannot
                              		  register in Cisco Unified CME.

Before using this command, configure the ephone-dn tags to be
                              		  assigned and define at least one primary number for each dn-tag.

All ephone-dns in a specified range should be of the same type,
                              		  either single-line or dual-line.

Ephone-dn tags to be assigned must belong to normal ephone-dns and
                              		  cannot belong to paging ephone-dns, intercom ephone-dns, music-on-hold (MOH)
                              		  ephone-dns, or message-waiting-indication (MWI) ephone-dns.

The auto assign command cannot create shared lines.

If an insufficient number of dn-tags is available, some ephone
                              		  configurations will not include a telephone or extension number.

Use multiple auto assign commands to assign discontinuous ranges of
                              		  ephone-dn tags and to support multiple types of IP phones. Overlapping ranges
                              		  of dn-tags may be assigned so that they map to more than one type of phone. If
                              		  no type is specified, the values in the range
                              		  are assigned to phones of any type, and if a specific range is assigned for a
                              		  specific phone type, the available ephone-dn tag in that range are used first.

If the phone being registered is connected to a Cisco VG200 series
                              		  analog phone gateway, configuring the

auto assign command will automatically create one ephone
                              		  configuration for each configured port, as the port registers with the Cisco
                              		  Unified CME router. To ensure that the tag-to-port assignment will match the
                              		  numbering order of the physical ports; for example, dn-tags 1 to 24 assigned to
                              		  ports 1 to 24 of a Cisco VG224 analog phone gateway, in that order, we
                              		  recommend that the Cisco Unified CME system be up, running, and configured before you boot the analog phone gateway.

The auto assign command cannot be used for the Cisco
                              		  Unified IP Phone 7914 Expansion Module. Phones with one or more expansion
                              		  modules must be configured manually.

After using this command, reboot the phone for which an ephone is to
                              		  be configured.

This command is also used by the Cisco Unified CME setup tool to
                              		  automatically assign ephone-dns after the tool has gathered information about
                              		  the setup from the user. When lines are assigned by the Cisco Unified CME setup
                              		  tool in keyswitch mode with two ephone-dn entries created for each individual
                              		  extension number, the automatic assignment mechanism assigns both ephone-dn
                              		  entries to an individual ephone associated with an IP phone.

## Examples

The following examples show how to configure the Auto Assign feature,
                              		  including prerequisite commands for configuring the auto assign command.

The following example shows how to enter the ephone-dn configuration
                              		  and create ephone-dns configurations, tags 1-4, each having a single primary
                              		  number:

```
Router(config)# ephone-dn 1 Router(config-ephone-dn)# number 2000 Router(config-ephone-dn)# exit Router(config)# ephone-dn 2 Router(config-ephone-dn)# number 3000 Router(config-ephone-dn)# exit Router(config)# ephone-dn 3 Router(config-ephone-dn)# number 4000 Router(config-ephone-dn)# exit Router(config)# ephone-dn 4 Router(config-ephone-dn)# number 4001 Router(config-ephone-dn)# exit
```

The following example shows how to designate ephone-dn tags 1 to 4
                              		  for automatic assignment to any type of IP phone and then perform a fast reboot
                              		  of all phones:

```
Router(config)# telephony-service Router(config-telephony)# auto assign 1 to 4 Router (config-telephony)# restart all
```

The following example is the partial output from the show ephone registered command listing four registered IP
                              		  phones, to which ephone-dn tags 1 to 4 have been automatically assigned, after
                              		  the phones were booted:

```
Router# show ephone registered ephone-1 Mac:0003.E3E7.F627 TCP socket:[2] activeLine:0 REGISTERED 
mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0
IP:10.0.0.2 51671 Telecaster 7940 keepalive 28 max_line 2
button 1: dn 1 number 2000 
ephone-2 Mac:0030.94C3.F43A TCP socket:[1] activeLine:0 REGISTERED 
mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0
IP:10.0.0.3 50094 Telecaster 7960 keepalive 28 max_line 6
button 1: dn 2 number 3000 
ephone-3 Mac:0003.6B40.99DA TCP socket:[3] activeLine:0 REGISTERED 
mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0
IP:10.0.0.200 51879 Telecaster 7960 keepalive 28 max_line 6
button 1: dn 3 number 4000
ephone-4 Mac:0010.406B.99D9 TCP socket:[4] activeLine:0 REGISTERED 
mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0
IP:10.0.0.012 51879 Telecaster 7960 keepalive 28 max_line 6
button 1: dn 4 number 4001
.
.
.
```

The following example shows how to designate ephone-dn tags 1 to 12
                              		  for automatic assignment to Cisco Unified IP Phone 7910Gs only and ephone-dn
                              		  tags 13 to 20 for automatic assignment to a Cisco Unified IP Phones 7960 and
                              		  7960Gs only, with call forwarding to extension 5001 on busy or after 30 seconds
                              		  of ringing with no answer:

```
Router(config)# telephony-service Router(config-telephony)# auto assign 1 to 12 type 7910 Router(config-telephony)# auto assign 13 to 20 type 7960 cfw 5001 timeout 30
```

### Related Commands

Command

Description

auto-reg-ephone

Enables registration of Cisco Unified IP phones for which
                                          						MAC addresses are not explicitly configured.

number

Associates a telephone or extension number with an
                                          						ephone-dn.

restart (ephone)

Performs a fast reboot of a single phone associated with a
                                          						Cisco Unified CME router.

restart (telephony-service)

Performs a fast reboot of one or all phones associated with
                                          						a Cisco Unified CME router.

show ephone

Displays statistical information about registered Cisco
                                          						Unified IP phones.

show ephone registered

Displays the status of registered phones.

## auto-assign
                        	 (auto-register)

To configure the
                              		  mandatory DN range for automatic registration of SIP phones with the Cisco
                              		  Unified CME system, use the auto-assign command in voice auto register configuration mode. This
                              		  command is a sub-mode CLI of the command auto-register . To disable configuring DN range for auto registration of SIP
                              		  phones, use the no form of
                              		  this command.

auto-assign First DN number to Last DN number

no auto-assign

### Syntax Description

auto-assign First DN
                                                							 number to Last DN
                                                							 number

The
                                          						mandatory range of directory numbers configured for phones auto registering on
                                          						Unified CME. Range: 1 to 4294967295.

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

### Usage Guidelines

This command is a
                              		  sub-mode option of the command auto-register . The command enables the
                              		  administrator to configure the DN range for the SIP phones auto registering on
                              		  Unified CME. For SIP phones to successfully auto register on Unified CME, it is
                              		  mandatory that the DN range is defined. The assigned value of First DN number
                              		  should be greater than zero.

## Examples

The following
                              		  example shows how to configure DN range for auto registration of SIP phones:

```
Router(config)#voice register global
Router(config-register-global)#auto-register
Router(config-voice-auto-register)# ?

VOICE auto register configuration commands: auto-assign Define DN range for auto assignment default Set a command to its defaults exit Exit from voice register group configuration mode no Negate a command or set its defaults password Default password for auto-register phones service-enable Enable SIP phone Auto-Registration template Default template for auto-register phones

Router(config-voice-auto-register)#auto-assign ?
  <1-4294967295> First DN number
Router(config-voice-auto-register)#auto-assign 1 ?
   to to
Router(config-voice-auto-register)#auto-assign 1 to ?
  <1-4294967295> Last DN number
Router(config-voice-auto-register)#auto-assign 1 to 10
```

### Related Commands

Command

Description

service-enable (auto-register)

Temporarily disables the auto registration process, but retains
                                          						the password and DN range configurations. Once auto-register command is
                                          						entered, the service is enabled by default.

password (auto-register)

Configures the mandatory password that administrator sets for
                                          						auto registration of SIP phones on Unified CME.

auto-register

Enables
                                          						automatic registration of SIP phones with the Cisco Unified CME system.

template
                                                							 (auto-register)

Creates a basic configuration template that supports all the
                                          						configurations available on the voice register template.

auto-reg-ephone

Enables automatic registration of ephones with the Cisco Unified CME system.

## auto
                        	 logout

To enable the
                              		  automatic change of an ephone hunt group agent’s ephone-dn to not-ready status
                              		  after a specified number of hunt-group calls are not answered, use the auto logout command in ephone-hunt configuration mode. To disable automatic
                              		  logout, use the no form of
                              		  this command.

auto logout [number-of-calls] [ dynamic | static ]

no auto logout [number-of-calls] [ dynamic | static ]

### Syntax Description

number-of-calls

(Optional) Number of unanswered hunt-group calls to an ephone-dn before the
                                          						ephone-dn is automatically changed to not-ready status. Range is from 1 to 20.
                                          						Default is 1.

dynamic

(Optional) Specifies that this command applies only to dynamic hunt group
                                          						members (those who are specified by an asterisk (*) wildcard in the hunt group
                                          						configuration). If neither the dynamic nor static keyword is used, automatic logout applies to both dynamic and static hunt group
                                          						members.

static

(Optional) Specifies that this command applies only to static hunt group
                                          						members (those whose extension numbers are explicitly named in the hunt group
                                          						configuration). If neither the dynamic nor static keyword is used, automatic logout applies to both dynamic and static hunt group
                                          						members.

### Command Default

Automatic change
                              		  of agent status to not-ready is disabled.

### Command Modes

Ephone-hunt configuration (config-ephone-hunt)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.3(11)XL

Cisco
                                          						CME 3.2.1

This
                                          						command was introduced.

12.3(14)T

Cisco
                                          						CME 3.3

This
                                          						command was integrated into Cisco IOS Release 12.3(14)T.

12.4(4)XC

Cisco
                                          						Unified CME 4.0

The number-of-calls argument and the dynamic and static keywords were added. The criterion for this command was changed from exceeding
                                          						the timeout command limit to exceeding the number of calls specified in this command.

12.4(9)T

Cisco
                                          						Unified CME 4.0

The
                                          						modifications made to this command were integrated into Cisco IOS 12.4(9)T.

### Usage Guidelines

This command is
                              		  valid only for the following Cisco IP phones:

- Cisco
                                 			 Unified IP Phone 7905G

- Cisco
                                 			 Unified IP Phone 7912G

- Cisco
                                 			 Unified IP Phones 7940 and 7940G

- Cisco
                                 			 Unified IP Phones 7960 and 7960G

This command is
                              		  used with the Automatic Agent Status Not-Ready feature for ephone hunt groups,
                              		  which automatically puts an agent’s phone in not-ready status when it exceeds a
                              		  specified limit. The limit at which the Automatic Agent Status Not-Ready
                              		  feature is triggered depends on the Cisco CME version that you are using, as
                              		  follows:

- Cisco CME
                                 			 3.3 and earlier versions—Automatic Agent Status Not-Ready is invoked when an
                                 			 ephone-hunt group call rings longer on a member ephone-dn than the period of
                                 			 time configured in the timeout command in ephone-hunt configuration mode.

- Cisco
                                 			 Unified CME 4.0 and later versions—Automatic Agent Status Not-Ready is invoked
                                 			 when the specified number of ephone-hunt group calls is unanswered by an agent.
                                 			 The default is one call if the number of calls is not explicitly specified.

When Automatic
                              		  Agent Status Not-Ready is specified for an ephone hunt group and it is
                              		  triggered because an ephone-dn member does not answer a specified number of
                              		  ephone hunt group calls, the following actions take place:

- If the hunt-group logout HLog command has been used, the agent is placed in
                                 			 not-ready status. The agent’s phone will not receive further hunt-group calls
                                 			 but will receive calls that directly dial the phone’s extension numbers. An
                                 			 agent in not-ready status can return to ready status by pressing the HLog soft
                                 			 key or by using the HLog feature access code (FAC).

- If the hunt-group logout HLog command has not been used or if the hunt-group logout DND command has been used, the phone on which the
                                 			 ephone-dn appears is placed into Do Not Disturb (DND) mode, in which the
                                 			 ephone-dn does not receive any calls at all, including hunt-group calls. The
                                 			 red lamp on the phone lights to indicate DND status. An agent in DND mode can
                                 			 return to ready status by pressing the DND soft key or by using the DND FAC.

- When an
                                 			 agent returns to ready status, the ephone hunt group resumes sending calls to
                                 			 the agent’s ephone-dn.

You can use the auto logout command with any number of ephone hunt groups, but any
                              		  ephone-dn to which the auto logout command applies must belong to only one ephone. Automatic Agent
                              		  Status Not-Ready is not supported on shared lines.

## Examples

This section
                              		  provides the following examples:

- Cisco CME 3.3 and Earlier
                                 			 Versions

- Cisco Unified CME 4.0 and
                                 			 Later Versions

## Examples

In the
                              		  following example, ephone hunt group 1 is configured to permit automatic
                              		  logout. If hunt group calls that are presented to 1001 and 1002 are unanswered
                              		  (that is, if they ring longer than 40 seconds each), ephone 1 and ephone 2 are
                              		  automatically put into DND mode. All unanswered calls are sent to voice mail
                              		  (5000).

```
Router(config)# ephone-dn 1 Router(config-ephone-dn)# number 1001 Router(config)# ephone-dn 2 Router(config-ephone-dn)# number 1002 Router(config)# ephone-hunt 1 peer Router(config-ephone-hunt)# pilot 1111 Router(config-ephone-hunt)# list 1001, 1002 Router(config-ephone-hunt)# final 5000 Router(config-ephone-hunt)# timeout 40 Router(config-ephone-hunt)# auto logout Router(config)# ephone 1 Router(config-ephone)# button 1:1 Router(config)# ephone 2 Router(config-ephone)# button 1:2
```

## Examples

In the
                              		  following example, Automatic Agent Status Not-Ready is limited to dynamic hunt
                              		  group members who do not answer two consecutive ephone hunt group calls.
                              		  Ephone-dn 33, extension 1003, has dynamically joined ephone-hunt group 1.
                              		  Ephone 3 will be put into DND mode if extension 1003 does not answer two
                              		  consecutive hunt group calls. Ephones 1 and 2 will not be put into DND if they
                              		  do not answer hunt-group calls, because the auto logout command applies only to dynamic hunt-group
                              		  agents.

```
Router(config)# telephony-service Router(config-telephony)# hunt-group logout DND Router(config)# ephone-dn 11 Router(config-ephone-dn)# number 1001 Router(config)# ephone-dn 22 Router(config-ephone-dn)# number 1002 Router(config)# ephone-dn 33 Router(config-ephone-dn)# number 1003 Router(config-ephone-dn)# ephone-hunt login Router(config)# ephone-hunt 1 peer Router(config-ephone-hunt)# pilot 1111 Router(config-ephone-hunt)# list 1001, 1002, * Router(config-ephone-hunt)# final 5000 Router(config-ephone-hunt)# auto logout 2 dynamic Router(config)# ephone 1 Router(config-ephone)# button 1:11 Router(config)# ephone 2 Router(config-ephone)# button 1:22 Router(config)# ephone 3 Router(config-ephone)# button 1:33
```

In the
                              		  following example, Automatic Agent Status Not-Ready cannot be used because all
                              		  of the ephone-dns are shared.

```
Router(config)# ephone-dn 1 Router(config-ephone-dn)# number 1001 Router(config)# ephone-dn 2 Router(config-ephone-dn)# number 1002 Router(config)# ephone-hunt 1 peer Router(config-ephone-hunt)# pilot 1111 Router(config-ephone-hunt)# list 1001, 1002 Router(config-ephone-hunt)# final 6000 Router(config)# ephone 1 Router(config-ephone)# button 1o1,2 Router(config)# ephone 2 Router(config-ephone)# button 1o1,2
```

### Related Commands

Command

Description

hunt-group logout

Enables separate handling of DND and HLog functionality for hunt-group agents
                                          						and the display of an HLog soft key on phones.

timeout

Defines the number of seconds after which a call that is not answered is
                                          						redirected to the next number in a Cisco Unified CME ephone-hunt-group list.

## auto logout (voice
                        	 hunt-group)

To enable the
                              		  automatic change of a voice hunt group agent’s voice register dn or ephone-dn
                              		  to not-ready status after a specified number of hunt-group calls are not
                              		  answered, use the auto logout command in voice hunt group configuration mode. To disable
                              		  automatic logout, use the no form of
                              		  this command.

auto logout [number-of-calls]

no auto logout [number-of-calls]

### Syntax Description

number-of-calls

Number
                                          						of unanswered hunt-group calls to a voice register dn or ephone-dn before the
                                          						DN is automatically changed to not-ready status. Range is 1 to 20. Default is
                                          						1.

### Command Default

Automatic change
                              		  of agent status to not-ready is disabled.

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
                                          						command was introduced.

### Usage Guidelines

This command is
                              		  used with the Automatic Agent Status Not-Ready feature for voice hunt groups,
                              		  which automatically puts an agent’s phone in not-ready status when it exceeds a
                              		  specified limit. The limit at which the Automatic Agent Status Not-Ready
                              		  feature is triggered has to be specified from the range of 1 to 20. If no value
                              		  is defined, the default value of 1 is applied. When an agent returns to ready
                              		  status, the voice hunt group resumes sending calls to the agent’s DN.

When Automatic
                              		  Agent Status Not-Ready is specified for a voice hunt group and it is triggered
                              		  because a DN member does not answer a specified number of voice hunt group
                              		  calls, the following actions take place:

- If the hunt-group logout HLog command is configured, then the DNs of that
                                 			 hunt group switch to not-ready state when the number of successive unanswered
                                 			 hunt group calls specified under auto logout command is matched. When hunt-group logout HLog command is configured, phone level logout
                                 			 happens for SIP phones. However, SCCP phones log out at line level. An agent in
                                 			 not-ready status can return to ready status by pressing the HLog soft key, HLog
                                 			 feature access code (FAC), or Feature Button.

- If the hunt-group logout DND command is configured, then phone switches to
                                 			 DND mode and logs out the member when the number of successive unanswered hunt
                                 			 group calls specified under auto logout command is matched. For hunt-group logout DND command, both SIP and SCCP phones logout at
                                 			 phone level. An agent in not-ready status can return to ready status by
                                 			 pressing the DND softkey.

## Examples

In the following
                              		  example, voice hunt-group 1 is configured to permit automatic logout. If hunt
                              		  group calls that are presented to 1001, 1002, 1003, and 1004 are unanswered
                              		  (that is, if they ring longer than 40 seconds each), voice register pool 1,
                              		  voice register pool 2, ephone 1, and ephone 2 are automatically logged out. All
                              		  unanswered calls are sent to DN 5000.

```
Router(config)# voice register dn 1 Router(config-register-dn)# number 1001 Router(config)# voice register dn 2 Router(config-register-dn)# number 1002 Router(config)# ephone-dn 1 Router(config-ephone-dn)# number 1003 Router(config)# ephone-dn 2 Router(config-ephone-dn)# number 1004 Router(config)# voice register pool 1 Router(config-register-pool)# number 1 dn 1 Router(config)# voice reister pool 2 Router(config-register-pool)# number 1 dn 2 Router(config)# ephone 1 Router(config-ephone)# button 1:1 Router(config)# ephone 2 Router(config-ephone)# button 1:2 Router(config)# voice hunt-group 1 peer Router(config-voice-hunt)# pilot 1111 Router(config-voice-hunt)# list 1001, 1002, 1003, 1004 Router(config-voice-hunt)# final 5000 Router(config-voice-hunt)# timeout 40 Router(config-voice-hunt)# auto logout 4
```

If hunt-group logout HLog is configured under telephony-service for
                              		  this example, then the DN that does not answer 4 successive calls switches to
                              		  not-ready state.

### Related Commands

Command

Description

auto logout

Enables automatic change of an ephone hunt group agent’s ephone-dn to not-ready
                                          						status after a specified number of hunt-group calls are not answered.

## auto-answer

To enable the intercom auto-answer feature on a SIP phone extension,
                              		  use the auto-answer command in voice register dn
                              		  configuration mode. To return to the default, use the no form of this command.

auto-answer

no auto-answer

### Syntax Description

This command has no arguments or keywords.

### Command Default

Disabled

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

This command creates an IP phone line connection that resembles a
                              		  private line, automatic ring-down (PLAR). The auto-answer causes an extension
                              		  (directory number) to operate in auto-dial fashion for outbound calls and auto
                              		  answer-with-mute for inbound calls. If an extension is configured for intercom
                              		  operation, it can be associated with one Cisco IP phone only.

Any caller can dial an intercom extension, and a call to an intercom
                              		  extension that is originated by a nonintercom caller triggers an automatic
                              		  answer exactly like a legitimate intercom call. To prevent nonintercom
                              		  originators from manually dialing an intercom destination, you can use
                              		  alphabetic characters when you assign numbers to intercom extensions by using
                              		  the number command. These characters cannot be
                              		  dialed from a normal phone but can be dialed by preprogrammed intercom
                              		  extensions when calls are made by the router.

Use the reset command to reset an individual SIP
                              		  phone after you make changes to an extension for a SIP phone in Cisco CME.

## Examples

The following example shows how to set the auto-answer feature on SIP
                              		  phone directory number 1:

```
Router(config)# voice register dn 1 Router(config-register-dn) number A5001 Router(config-register-dn) auto-answer
```

### Related Commands

Command

Description

number (voice register dn)

Associates a telephone or extension number with a directory
                                          						number.

reset (voice register global)

Performs a complete reboot of all SIP phones associated
                                          						with a Cisco CME router.

reset (voice register pool)

Performs a complete reboot of a single SIP phone associated
                                          						with a Cisco CME router.

## auto-line

To enable automatic line selection on an IP phone in a Cisco
                              		  CallManager Express (Cisco CME) system, use the auto-line command in ephone configuration mode. To disable automatic line
                              		  selection, use the no form of this command.

auto-line [ button-number [ answer-incoming ] | incoming ]

no auto-line

### Syntax Description

button-number

(Optional) Selects the line associated with the specified
                                          						button when the handset is lifted.

answer-incoming

(Optional) Enables automatic line selection for incoming
                                          						calls on the line associated with the button-number argument.

incoming

(Optional) Enables automatic line selection for incoming
                                          						calls only.

### Command Default

Automatic line selection is enabled.

### Command Modes

Ephone configuration (config ephone)

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

The button-number argument was added.

12.4(4)XC

Cisco Unified CME 4.0

The answer-incoming keyword was added.

12.4(9)T

Cisco Unified CME 4.0

The answer-incoming keyword was
                                          						integrated into Cisco IOS 12.4(9)T.

### Usage Guidelines

Use the auto-line command with no keyword or argument
                              		  enables automatic line selection on the specified ephone. Picking up a handset
                              		  answers the first ringing line or, if no line is ringing, selects the first
                              		  idle line. This is also the default behavior if this command is not used.

Use the auto-line incoming command enables automatic line selection
                              		  for incoming calls only. Picking up the handset answers the first ringing line
                              		  and, if no line is ringing, does not select an idle line for an outgoing call.
                              		  Pressing a line button selects a line for an outgoing call.

Use the auto-line command with the button-number argument specifies the line
                              		  that will automatically be selected when the handset is picked up to make an
                              		  outgoing call. If a button number is specified and the line associated with
                              		  that button is unavailable (because it is a shared line in use on another
                              		  phone), no dial tone is heard when the handset is lifted. You must press an
                              		  available line button to make an outgoing call. Incoming calls must be answered
                              		  by pressing the Answer soft key or pressing the ringing line button.

Use the answer-incoming keyword with the button-number argument enables automatic line
                              		  selection for incoming calls on the specified button. Picking up the handset
                              		  answers the incoming call on the line button associated with the button-number argument.

Use the no auto-line command disables automatic line
                              		  selection on the ephone that is being configured. Pressing the Answer soft key
                              		  answers the first ringing line, and pressing a line button selects a line for
                              		  an outgoing call. Picking up the handset does not answer calls or provide dial
                              		  tone.

## Examples

The following example shows how to disable automatic line selection.
                              		  The phone user must use the Answer soft key or press a line button to answer
                              		  calls, or the phone user must press a line button to initiate outgoing calls.

```
Router(config)# ephone 23 Router(config-ephone)# no auto-line
```

The following example shows how to enable automatic line selection
                              		  for incoming calls only. The phone user picks up the handset to answer the
                              		  first ringing line. To make outgoing calls, the phone user must press a line
                              		  button.

```
Router(config)# ephone 24 Router(config-ephone)# auto-line incoming
```

The following example shows how to enable the automatic selection of
                              		  line button 3 for outgoing calls when the handset is lifted. There is no
                              		  automatic answering of incoming calls; the user presses the Answer soft key or
                              		  presses a line button to answer a call.

```
Router(config)# ephone 26 Router(config-ephone)# auto-line 3
```

The following example shows how to enable the automatic selection of
                              		  line button 3 when the handset is lifted to answer incoming calls or to make
                              		  outgoing calls.

```
Router(config)# ephone 26 Router(config-ephone)# auto-line 3 answer-incoming
```

### Related Commands

Command

Description

ephone

Enters ephone configuration mode.

## auto-network-detect

To enable phones to automatically detect whether they are inside the
                              		  corporate network or not, use the auto-network-detect command in vpn-profile configuration mode.

auto-network-detect [ enable | disable ]

### Syntax Description

enable

Enables auto-network detection option for a vpn-profile.

disable

Disables automatic network detection option for a
                                          						vpn-profile.

### Command Default

Auto-network-detect is disabled.

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

Use this command to configure automatic network detection parameter
                              		  in phones. The auto-network-detect command enables phones to automatically
                              		  detect whether they are inside the corporate network or not. When the
                              		  auto-network detection is enabled, the phone dectects the corporate network and
                              		  does not require a VPN connection to start functioning. Automatic network
                              		  detection is disabled by default.

## Examples

The following example shows auto-network-detect enabled for
                              		  vpn-profile 1:

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

vpn-profile

Defines a VPN-profile.

## auto-register

To enable
                              		  automatic registration of SIP phones with the Cisco Unified CME system, use the auto-register command in voice register global configuration mode. This
                              		  command is the parent CLI, and is used to enter into the auto registration
                              		  configuration mode. To disable automatic registration of SIP phones, use the no form of
                              		  this command.

auto-register

no auto-register

### Syntax Description

auto-register

Enters
                                          						auto registration mode for SIP phones registering on Unified CME.

### Command Default

By default, this
                              		  command is enabled.

### Command Modes

voice register global configuration (config-voice-register-global)

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

This command is
                              		  enabled by default and allows automatic registration of SIP phones on Unified
                              		  CME, provided the administrator configures the password and DN range using the
                              		  relevant sub-mode CLI options. It is mandatory that the password is configured
                              		  before assigning the DN range. The command service-enable is enabled by default when service-enable is enabled.

The no form of
                              		  this command disables the auto registration of phones, and removes the password
                              		  and DN range configurations. To disable auto registration temporarily without
                              		  losing the configurations such as password and DN range, use the sub-mode CLI
                              		  option, no service-enable .

## Examples

The following
                              		  example shows how to temporarily disable auto registration using the no form of
                              		  the sub-mode option, service-enable:

```
Router(config)#voice register global
Router(config-register-global)#auto-register
Router(config-voice-auto-register)# ?

VOICE auto register configuration commands: auto-assign Define DN range for auto assignment default Set a command to its defaults exit Exit from voice register group configuration mode no Negate a command or set its defaults password Default password for auto-register phones service-enable Enable SIP phone Auto-Registration template Default template for auto-register phones
```

### Related Commands

Command

Description

service-enable
                                                							 (auto-register)

Temporarily disables the auto registration process, but retains
                                          						the password and DN range configurations. Once auto-register command is
                                          						entered, the service is enabled by default.

password
                                                							 (auto-register)

Configures the mandatory password that administrator sets for
                                          						auto registration of SIP phones on Unified CME.

auto-assign
                                                							 (auto-register)

Configures the mandatory range of directory numbers for phones
                                          						auto registering on Unified CME.

template
                                                							 (auto-register)

Creates a basic configuration template that supports all the
                                          						configurations available on the voice register template.

auto-reg-ephone

Enables automatic registration of ephones with the Cisco Unified CME system.

## auto-reg-ephone

To enable automatic registration of ephones with the Cisco Unified
                              		  CME system, use the auto-reg-ephone command in telephony-service
                              		  configuration mode. To disable automatic registration, use the no form of this command.

auto-reg-ephone

no auto-reg-ephone

### Syntax Description

This command has no keywords or arguments.

### Command Default

Automatic registration is enabled.

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

This command was integrated into Cisco IOS 12.4(9)T.

### Usage Guidelines

This command is enabled by default and allows automatic registration,
                              		  in which Cisco Unified CME allocates an ephone slot to any ephone that connects
                              		  to it, regardless of whether the ephone appears in the configuration or not.

The no form of this command blocks the automatic
                              		  registration of ephones whose MAC addresses are not explicitly listed in the
                              		  configuration. When automatic registration is blocked, Cisco Unified CME
                              		  records the MAC addresses of phones that attempt to register but cannot because
                              		  they are blocked.

Use the show ephone attempted-registrations command to view the list of phones that have attempted to
                              		  register but have been blocked. Use the clear telephony-service ephone-attempted-registrations command to clear
                              		  the list of phones that have attempted to register but have been blocked.

## Examples

The following example disables automatic registration of ephones that
                              		  are not listed in the configuration:

```
Router(config)# telephony-service Router(config-telephony)# no auto-reg-ephone
```

### Related Commands

Command

Description

clear telephony-service ephone-attempted-registrations

Empties the log of ephones that unsuccessfully attempt to
                                          						register with Cisco Unified CME.

show ephone attempted-registrations

Displays the log of ephones that unsuccessfully attempt to
                                          						register with Cisco Unified CME.

| lpcor-group | Name of
                                          						the LPCOR resource group. |
|---|---|
| fac | Enables
                                          						forced authorization code for calls from this resource group. |

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
| 15.1(3)T | Cisco
                                          						Unified CME 8.5 | This
                                          						command was modified. The fac keyword was added to the accept command. |

| Command | Description |
|---|---|
| show voice lpcor policy | Displays the LPCOR policy for the specified resource group. |
| voice lpcor custom | Defines the LPCOR resource groups on the Cisco Unified CME router. |
| voice lpcor policy | Creates a LPCOR policy for a resource group. |

| digit | Single-digit number users dial. Range: 0 to 9. Default: 0. |
|---|---|

| Cisco IOS Release | Modification |
|---|---|
| 12.4(22)YB | This command was introduced. |
| 12.4(24)T | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Note | Your domain type must support the access digit that you select.
                                       		  For example, the valid range for the DSN is 2 to 9. |
|---|---|

| Command | Description |
|---|---|
| mlpp preemption | Enables preemption capability on an SCCP phone or analog
                                          						FXS port. |
| preemption trunkgroup | Enables preemption capability on a trunk group. |
| preemption user | Enables preemption capability for all supported phones. |

| max-addons | Defines
                                          						the maximum number of addon modules that can be configured while defining the
                                          						pool for the phone. Range is 1 to 3. |
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
| voice register
                                          						pool-type | Adds a
                                          						new Cisco Unified SIP IP phone to Cisco Unified CME. |
| type | Defines a phone type for a SIP phone. |

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
| name | Specifies a string (up to 30 characters) used internally to
                                          						identify or describe the emergency response location. |
| subnet | Defines which IP phones are part of this ERL. |

| max-addons | Defines
                                          						the maximum number of addon modules that can be configured while defining the
                                          						pool for the phone. Range is 1 to 3. |
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
| voice register
                                          						pool-type | Adds a
                                          						new Cisco Unified SIP IP phone to Cisco Unified CME. |
| type | Defines a phone type for a SIP phone. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was made available in ephone-template
                                          						configuration mode. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command in the ephone-template configuration mode was
                                          						integrated into Cisco IOS 12.4(9)T. |

| Command | Description |
|---|---|
| after-hours block pattern | Defines a pattern of digits for blocking outgoing calls
                                          						from IP phones. |
| after-hours date | Defines a recurring period based on date during which
                                          						outgoing calls that match defined block patterns are blocked on IP phones. |
| after-hours day | Defines a recurring period based on day of the week during
                                          						which outgoing calls that match defined block patterns are blocked on IP
                                          						phones. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| after-hours block pattern | Defines a pattern of digits for blocking outgoing calls
                                          						from IP phones. |
| after-hours date | Defines a recurring period based on date during which
                                          						outgoing calls that match defined block patterns are blocked on IP phones. |
| after-hours day | Defines a recurring period based on day of the week during
                                          						which outgoing calls that match defined block patterns are blocked on IP
                                          						phones. |

| pattern-tag | Identifier for a call-blocking pattern. Up to 100 call-blocking patterns can be
                                          						defined in separate commands. |
|---|---|
| pattern | Outgoing call digits to be matched for blocking, including specific digit
                                          						patterns and general regular expressions. |
| 7-24 | (Optional) If the 7-24 keyword is specified, the pattern is always blocked,
                                          						7 days a week, 24 hours a day. If the 7-24 keyword
                                          						is not specified, the pattern is blocked during the days and dates that are
                                          						defined with the after-hours day and after-hours date commands. |

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
| 12.4(4)T | Cisco
                                          						CME 3.4 | Support
                                          						for this command was extended to all SCCP, H.323, SIP, and POTS calls that go
                                          						through the Cisco Unified CME router, including all incoming calls to the
                                          						router, except calls from an exempt phone. |
| 12.4(15)XY | Cisco
                                          						Unified CME 4.2(1) | This
                                          						command was added to ephone-template configuration mode. |
| 12.4(15)XZ | Cisco
                                          						Unified CME 4.3 | This
                                          						command was added to ephone-template configuration mode. |
| 12.4(20)T | Cisco
                                          						Unified CME 7.0 | This
                                          						command was integrated into Cisco IOS Release 12.4(20)T. |
| 15.3(2)T | Cisco
                                          						Unified CME 9.5 | This
                                          						command was modified to include regular expressions as a value for the pattern argument. |

| Note | The maximum
                                       		  length of a regular expression pattern is 32 for both Cisco Unified SIP and
                                       		  Cisco Unified SCCP IP phones. |
|---|---|

| Command | Description |
|---|---|
| after-hour exempt | Specifies that an IP phone does not have any of its outgoing calls blocked
                                          						although call blocking is defined. |
| after-hours date | Defines a recurring period based on date during which outgoing calls that match
                                          						defined block patterns are blocked on IP phones. |
| after-hours day | Defines a recurring period based on day of the week during which outgoing calls
                                          						that match defined block patterns are blocked on IP phones. |
| after-hours override-code | Specifies that call blocking on an IP phone can be overridden by entering a
                                          						defined code. |
| after-hours pstn-prefix | Specifies that trunk lines on an IP phone are blocked similarly to that
                                          						configured for nonPSTN lines. |
| ephone-template (ephone) | Applies template to a SCCP phone. |

| month | Abbreviated month. The following abbreviations for month
                                          						are valid: jan , feb , mar , apr , may , jun , jul , aug , sep , oct , nov , dec . |
|---|---|
| date | Date of the month. Range is from 1 to 31. |
| start-time stop-time | Beginning and ending times for call blocking, in an HH:MM
                                          						format using a 24-hour clock. The stop time that is entered will be the next
                                          						available time that follows the start time. The value 24:00 is not valid. If
                                          						00:00 is entered as a stop time, it is changed to 23:59. If 00:00 is entered
                                          						for both start time and stop time, calls are blocked for the entire 24-hour
                                          						period on the specified date. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(15)XY | Cisco Unified CME 4.2(1) | This command was added to ephone-template configuration
                                          						mode. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was added to ephone-template configuration
                                          						mode. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| after-hour exempt | Specifies that an IP phone does not have any of its
                                          						outgoing calls blocked although call blocking is defined. |
| after-hours block pattern | Defines a pattern of digits (0-9) for blocking outgoing
                                          						calls from IP phones. |
| after-hours day | Defines a recurring period based on day of the week during
                                          						which outgoing calls that match defined block patterns are blocked on IP
                                          						phones. |
| after-hours override-code | Specifies that call blocking on an IP phone can be
                                          						overridden by entering a defined set of digits (0-9). |
| after-hours pstn-prefix | Specifies that trunk lines on an IP phone are blocked
                                          						similarly to that configured for nonPSTN lines. |
| ephone-template (ephone) | Applies template to SCCP phone. |

| day | Abbreviated day of the week. The following abbreviations
                                          						for day of the week are valid: sun , mon , tue , wed , thu , fri , sat . |
|---|---|
| start-time stop-time | Beginning and ending times for call blocking, in an HH:MM
                                          						format using a 24-hour clock. The stop time that is entered will be the next
                                          						available time that follows the start time. The value 24:00 is not valid. If
                                          						00:00 is entered as a stop time, it is changed to 23:59. If 00:00 is entered
                                          						for both start time and stop time, calls are blocked for the entire 24-hour
                                          						period on the specified day. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(15)XY | Cisco Unified CME 4.2(1) | This command was added to ephone-template configuration
                                          						mode. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was added to ephone-template configuration
                                          						mode. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| after-hour exempt | Specifies that an IP phone does not have any of its
                                          						outgoing calls blocked although call blocking is defined. |
| after-hours block pattern | Defines a pattern of digits (0-9) for blocking outgoing
                                          						calls from IP phones. |
| after-hours date | Defines a recurring period based on date during which
                                          						outgoing calls that match defined block patterns are blocked on IP phones. |
| after-hours override-code | Specifies that call blocking on an IP phone can be
                                          						overridden by entering a defined set of digits (0-9). |
| after-hours pstn-prefix | Specifies that trunk lines on an IP phone are blocked
                                          						similarly to that configured for nonPSTN lines. |
| ephone-template (ephone) | Applies template to SCCP phone. |

| pattern | Specifies the pattern of digits (0-9) that must be dialed
                                          						by the phone user to override the call blocking rules. The override code is
                                          						provided to the phone user by the system administrator. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XY | Cisco Unified CME 4.2(1) | This command was introduced. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was added to ephone-template configuration
                                          						mode. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| after-hour exempt | Specifies that an IP phone does not have any of its
                                          						outgoing calls blocked although call blocking is defined. |
| after-hours block pattern | Defines a pattern of digits (0-9) for blocking outgoing
                                          						calls from IP phones. |
| after-hours date | Defines a recurring period based on date during which
                                          						outgoing calls that match defined block patterns are blocked on IP phones. |
| after-hours day | Defines a recurring period based on day of the week during
                                          						which outgoing calls that match defined block patterns are blocked on IP
                                          						phones. |
| after-hours pstn-prefix | Specifies that trunk lines on an IP phone are blocked
                                          						similarly to that configured for non PSTN lines. |
| ephone-template (ephone) | Applies a template to an ephone. |

| tag | Identifier for a PSTN call-blocking pattern. Up to 4
                                          						call-blocking patterns can be defined in separate commands. |
|---|---|
| pattern | Outgoing call digits (0-9) to be matched for PSTN blocking. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XY | Cisco Unified CME 4.2(1) | This command was introduced. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was added to ephone-template configuration
                                          						mode. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| after-hour exempt | Specifies that an IP phone does not have any of its
                                          						outgoing calls blocked although call blocking is defined. |
| after-hours block pattern | Defines a pattern of digits (0-9) for blocking outgoing
                                          						calls from IP phones. |
| after-hours date | Defines a recurring period based on date during which
                                          						outgoing calls that match defined block patterns are blocked on IP phones. |
| after-hours day | Defines a recurring period based on day of the week during
                                          						which outgoing calls that match defined block patterns are blocked on IP
                                          						phones. |
| after-hours override-code | Specifies that call blocking on an IP phone can be
                                          						overridden by entering a defined series of digits (0-9). |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XJ | Cisco Unified CME 4.1 | This command was introduced. |
| 12.4(15)T | Cisco Unified CME 4.1 | This command was integrated into Cisco IOS Release
                                          						12.4(15)T. |

| Command | Description |
|---|---|
| blf-speed-dial | Enables Busy Lamp Field (BLF) monitoring for a speed-dial
                                          						number on a phone registered to Cisco Unified CME. |
| presence | Enables presence service and enters presence configuration
                                          						mode. |
| presence call-list | Enables BLF monitoring for call lists and directories on
                                          						phones registered to Cisco Unified CME. |
| presence enable | Allows the router to accept incoming presence requests. |
| show presence global | Displays configuration information about the presence
                                          						service. |
| show presence subscription | Displays information about active presence subscriptions. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

| Command | Description |
|---|---|
| caller-id block (voice register template) | Enables caller-ID blocking for outbound calls from a SIP
                                          						phone. |
| template (voice register pool) | Applies a template to a SIP phone. |

| application-name | Interactive voice response (IVR) application name. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(11)YT | Cisco ITS 2.1 | This command was introduced. |
| 12.2(15)T | Cisco ITS 2.1 | This command was integrated into Cisco IOS Release
                                          						12.2(15)T. |

| Command | Description |
|---|---|
| show call application voice summary | Displays information about voice applications. |

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
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was added to Cisco CME. |

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

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(4)M | Cisco Unified CME 8.6 | This command was introduced. |

| Command | Description |
|---|---|
| camera | Enables USB camera capability on Cisco Unified IP Phones
                                          						9951 and 9971 |
| video | Enables video capability on Cisco Unified SIP IP Phones
                                          						9951 and 9971 |

| password | Four-digit string to be used as password to access IVR.
                                          						Password string must contain numbers 0 to 9. The 0 in the parameter [0\|6] mentioned in the CLI command represents plain, unencrypted text and 6 represents level 6 password
                                          encryption. |
|---|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.2(2)T | Unified CME 9.0 | This command was introduced. |
| Cisco IOS XE Gibraltar 16.11.1a  Release | Unified CME 12.6 | The command was enhanced for password encryption. Password policy is not enforced, as the command supports a four-digit password. |

| Command | Description |
|---|---|
| voice register pool | Enters voice register pool configuration mode and creates a
                                          						pool configuration for Cisco Unified SIP IP phones in Cisco Unified CME. |

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

| number | Pilot number of the MLPP attendant-console service, such as
                                          						the Cisco Unified CME basic automatic call distribution (B-ACD) and
                                          						auto-attendant (AA) service. |
|---|---|
| seconds | Number of seconds that a call rings before being redirected
                                          						to the attendant-console service. Range: 10 to 60. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |
| 12.4(24)T | — | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| access-digit | Defines the access digit that phone users dial to request a
                                          						precedence call. |
| mlpp preemption | Enables preemption capability on an SCCP phone or analog
                                          						FXS port. |
| service | Associates a dial peer with an auto-attendant (AA) service. |

| Cisco
                                    				  IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.4(3)M | Cisco Unified CME 10.5 | This
                                       					 command was introduced. |

| Command | Description |
|---|---|
| ephone-hunt group | Configures an ephone hunt group in Cisco Unified CME. |
| voice-hunt group | Configures a voice hunt group in Cisco Unified CME. |

| both | Requires both user id and password to authenticate. |
|---|---|
| password | Requires only password to authenticate. |
| none | Does not allows authentication. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(3)T | Cisco Unified CME 8.5 | This command was introduced. |

| Command | Description |
|---|---|
| vpn-profile | Defines a VPN-profile. |

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

| application-name | String sent by application to identify itself to the
                                          						server. Length of string: 1 to 15characters. |
|---|---|
| password | String sent by application to identify itself to the
                                          						server. Length of string: 1 to 15 characters. The 0 in the parameter [0\|6] mentioned in the CLI command represents plain, unencrypted text and 6 represents level 6 password
                                          encryption. |

| Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |
| Cisco IOS XE Gibraltar 16.11.1a Release | Unified CME 12.6 | The command was enhanced for password encryption, based on Unified CME password policy. |

| Note | This command is not required for authorizing requests from
                                       		  Extension Mobility phones in Cisco Unified CME. |
|---|---|

| Command | Description |
|---|---|
| url authentication | Specifies authentication server and credential to be used
                                          						by an application. |

| dn-tag to dn-tag | Range of ephone-dn tags for already configured ephone-dns,
                                          						from which a tag is assigned to the ephone being created. The maximum number of directory numbers supported is
                                          						version and platform dependent. Type ? to display the value. |
|---|---|
| type phone-type | (Optional) Type of Cisco Unified IP phone to which to
                                          						restrict automatic assignment of ephone-dn tags. Valid entries are the
                                          						following: 12SP —12SP+ and 30VIP phones. 7902 —Cisco Unified IP Phone
                                             						  7902G. 7905— Cisco Unified IP Phone
                                             						  7905G. 7906— Cisco Unified IP Phone
                                             						  7906G. 7910— Cisco Unified IP Phone
                                             						  7910 and 7910G. 7911 —Cisco Unified IP Phone
                                             						  7911G. 7912— Cisco Unified IP Phone
                                             						  7912G. 7920 —Cisco Unified Wireless IP
                                             						  Phone 7920. 7921 —Cisco Unified Wireless IP
                                             						  Phone 7921. 7931 —Cisco Unified Wireless IP
                                             						  Phone 7931G. 7935— Cisco Unified IP
                                             						  Conference Station 7935. 7936— Cisco Unified IP
                                             						  Conference Station 7936. 7937 —Cisco Unified IP
                                             						  Conference Station 7937 7940— Cisco Unified IP Phones
                                             						  7940 and 7940G. 7941 —Cisco Unified IP Phone
                                             						  7941G. 7941GE —Cisco Unified IP Phone
                                             						  7941G-GE. 7942 —Cisco Unified IP Phone
                                             						  7942. 7945 —Cisco Unified IP Phone
                                             						  7945. |
| type phone-type | 7960— Cisco Unified IP Phones
                                             						  7960 and 7960G. 7961 —Cisco Unified IP Phone
                                             						  7961G. 7961GE —Cisco Unified IP Phone
                                             						  7961G-GE. 7962 —Cisco Unified IP Phone
                                             						  7962. 7965 —Cisco Unified IP Phone
                                             						  7965. 7970 —Cisco Unified IP Phone
                                             						  7970G. 7971 —Cisco Unified IP Phone
                                             						  7971G-GE. 7975 —Cisco Unified IP Phone
                                             						  7975. 7985 —Cisco Unified IP Phone
                                             						  7985. CIPC —Cisco IP Communicator. all —All ephone types. anl —Analog gateway. ata— Cisco ATA-186 or Cisco
                                             						  ATA-188. bri —SCCP gateway. vgc-phone —vg248 phone emulation
                                             						  for analog phone. Note You can also add a new phone type to your configuration
                                                   						by using the ephone-type command. | Note | You can also add a new phone type to your configuration
                                                   						by using the ephone-type command. |
| Note | You can also add a new phone type to your configuration
                                                   						by using the ephone-type command. |
| cfw | (Optional) Automatically assigned ephone-dns are
                                          						provisioned for call-forward busy and no-answer to the specified extension
                                          						number. |
| extension-number | (Optional) Extension number to which calls are to be
                                          						forwarded on busy and no-answer conditions. |
| timeout seconds | (Optional; required if the cfw keyword is used) Amount of
                                          						time, in seconds, to wait when a call is not being answered before forwarding
                                          						it. Range: 3 to 60000. |

| Note | You can also add a new phone type to your configuration
                                                   						by using the ephone-type command. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.3(7)T | Cisco CME 3.1 | The 7920 and 7936 keywords were added. |
| 12.3(11)XL | Cisco CME 3.2.1 | The 7970 keyword was added. |
| 12.3(14)T | Cisco CME 3.3 | The 7971 keyword was added, and this
                                          						command was integrated into Cisco IOS Release 12.3(14)T. |
| 12.4(4)XC | Cisco Unified CME 4.0 | The 7941 , 7941GE , 7961 , and 7961GE keywords were added. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |
| 12.4(6)XE | Cisco Unified CME 4.0(2) | The 7931 keyword was added. |
| 12.4(4)XC4 | Cisco Unified CME 4.0(3) | The 7931 keyword was added. |
| 12.4(11)T | Cisco Unified CME 4.0(3) | This command was integrated into Cisco IOS Release
                                          						12.4(11)T. |
| 12.4(11)XJ2 | Cisco Unified CME 4.1 | The 7921 and 7985 keywords were introduced. |
| 12.4(15)T | Cisco Unified CME 4.1 | This command wasintegrated into Cisco IOS Release
                                          						12.4(15)T. |
| 12.4(15)T1 | Cisco Unified CME 4.1(1) | The 7942 , 7945 , 7962 , 7965 , and 7975 keywords were introduced. |
| 12.4(11)XW3 | Cisco Unified CME 4.2 | The 7942 , 7945 , 7962 , 7965 , and 7975 keywords were introduced. |
| 12.4(15)XY | Cisco Unified CME 4.2(1) | The 7942 , 7945 , 7962 , 7965 , and 7975 keywords were introduced. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | The 7942 , 7945 , 7962 , 7965 , and 7975 keywords were introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | The 7937 keyword was introduced and this command was
                                          						integrated into Cisco IOS Release 12.4(20)T. |

| Note | Care should be taken when using the auto assign command because this command grants
                                       		  telephony service to any IP phone that attempts to register. If you use the auto assign command, ensure that your network is secure
                                       		  from unauthorized access by unknown IP phones. |
|---|---|

| Command | Description |
|---|---|
| auto-reg-ephone | Enables registration of Cisco Unified IP phones for which
                                          						MAC addresses are not explicitly configured. |
| number | Associates a telephone or extension number with an
                                          						ephone-dn. |
| restart (ephone) | Performs a fast reboot of a single phone associated with a
                                          						Cisco Unified CME router. |
| restart (telephony-service) | Performs a fast reboot of one or all phones associated with
                                          						a Cisco Unified CME router. |
| show ephone | Displays statistical information about registered Cisco
                                          						Unified IP phones. |
| show ephone registered | Displays the status of registered phones. |

| auto-assign First DN
                                                							 number to Last DN
                                                							 number | The
                                          						mandatory range of directory numbers configured for phones auto registering on
                                          						Unified CME. Range: 1 to 4294967295. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 15.6(3)M 16.3.1 | Cisco
                                          						Unified CME 11.5 | This
                                          						command was introduced. |

| Command | Description |
|---|---|
| service-enable (auto-register) | Temporarily disables the auto registration process, but retains
                                          						the password and DN range configurations. Once auto-register command is
                                          						entered, the service is enabled by default. |
| password (auto-register) | Configures the mandatory password that administrator sets for
                                          						auto registration of SIP phones on Unified CME. |
| auto-register | Enables
                                          						automatic registration of SIP phones with the Cisco Unified CME system. |
| template
                                                							 (auto-register) | Creates a basic configuration template that supports all the
                                          						configurations available on the voice register template. |
| auto-reg-ephone | Enables automatic registration of ephones with the Cisco Unified CME system. |

| number-of-calls | (Optional) Number of unanswered hunt-group calls to an ephone-dn before the
                                          						ephone-dn is automatically changed to not-ready status. Range is from 1 to 20.
                                          						Default is 1. |
|---|---|
| dynamic | (Optional) Specifies that this command applies only to dynamic hunt group
                                          						members (those who are specified by an asterisk (*) wildcard in the hunt group
                                          						configuration). If neither the dynamic nor static keyword is used, automatic logout applies to both dynamic and static hunt group
                                          						members. |
| static | (Optional) Specifies that this command applies only to static hunt group
                                          						members (those whose extension numbers are explicitly named in the hunt group
                                          						configuration). If neither the dynamic nor static keyword is used, automatic logout applies to both dynamic and static hunt group
                                          						members. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.3(11)XL | Cisco
                                          						CME 3.2.1 | This
                                          						command was introduced. |
| 12.3(14)T | Cisco
                                          						CME 3.3 | This
                                          						command was integrated into Cisco IOS Release 12.3(14)T. |
| 12.4(4)XC | Cisco
                                          						Unified CME 4.0 | The number-of-calls argument and the dynamic and static keywords were added. The criterion for this command was changed from exceeding
                                          						the timeout command limit to exceeding the number of calls specified in this command. |
| 12.4(9)T | Cisco
                                          						Unified CME 4.0 | The
                                          						modifications made to this command were integrated into Cisco IOS 12.4(9)T. |

| Note | When an
                                       		  agent who is a dynamic member of a hunt group is in not-ready status, the
                                       		  agent’s slot in the ephone hunt group is not relinquished. It remains reserved
                                       		  by the agent until the agent leaves the group. |
|---|---|

| Command | Description |
|---|---|
| hunt-group logout | Enables separate handling of DND and HLog functionality for hunt-group agents
                                          						and the display of an HLog soft key on phones. |
| timeout | Defines the number of seconds after which a call that is not answered is
                                          						redirected to the next number in a Cisco Unified CME ephone-hunt-group list. |

| number-of-calls | Number
                                          						of unanswered hunt-group calls to a voice register dn or ephone-dn before the
                                          						DN is automatically changed to not-ready status. Range is 1 to 20. Default is
                                          						1. |
|---|---|

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
| auto logout | Enables automatic change of an ephone hunt group agent’s ephone-dn to not-ready
                                          						status after a specified number of hunt-group calls are not answered. |

| Cisco IOS Release | Version | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

| Command | Description |
|---|---|
| number (voice register dn) | Associates a telephone or extension number with a directory
                                          						number. |
| reset (voice register global) | Performs a complete reboot of all SIP phones associated
                                          						with a Cisco CME router. |
| reset (voice register pool) | Performs a complete reboot of a single SIP phone associated
                                          						with a Cisco CME router. |

| button-number | (Optional) Selects the line associated with the specified
                                          						button when the handset is lifted. |
|---|---|
| answer-incoming | (Optional) Enables automatic line selection for incoming
                                          						calls on the line associated with the button-number argument. |
| incoming | (Optional) Enables automatic line selection for incoming
                                          						calls only. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.3(7)T | Cisco CME 3.1 | The button-number argument was added. |
| 12.4(4)XC | Cisco Unified CME 4.0 | The answer-incoming keyword was added. |
| 12.4(9)T | Cisco Unified CME 4.0 | The answer-incoming keyword was
                                          						integrated into Cisco IOS 12.4(9)T. |

| Command | Description |
|---|---|
| ephone | Enters ephone configuration mode. |

| enable | Enables auto-network detection option for a vpn-profile. |
|---|---|
| disable | Disables automatic network detection option for a
                                          						vpn-profile. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(3)T | Cisco Unified CME 8.5 | This command was introduced. |

| Command | Description |
|---|---|
| vpn-profile | Defines a VPN-profile. |

| auto-register | Enters
                                          						auto registration mode for SIP phones registering on Unified CME. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 15.6(3)M 16.3.1 | Cisco
                                          						Unified CME 11.5 | This
                                          						command was introduced. |

| Command | Description |
|---|---|
| service-enable
                                                							 (auto-register) | Temporarily disables the auto registration process, but retains
                                          						the password and DN range configurations. Once auto-register command is
                                          						entered, the service is enabled by default. |
| password
                                                							 (auto-register) | Configures the mandatory password that administrator sets for
                                          						auto registration of SIP phones on Unified CME. |
| auto-assign
                                                							 (auto-register) | Configures the mandatory range of directory numbers for phones
                                          						auto registering on Unified CME. |
| template
                                                							 (auto-register) | Creates a basic configuration template that supports all the
                                          						configurations available on the voice register template. |
| auto-reg-ephone | Enables automatic registration of ephones with the Cisco Unified CME system. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS 12.4(9)T. |

| Command | Description |
|---|---|
| clear telephony-service ephone-attempted-registrations | Empties the log of ephones that unsuccessfully attempt to
                                          						register with Cisco Unified CME. |
| show ephone attempted-registrations | Displays the log of ephones that unsuccessfully attempt to
                                          						register with Cisco Unified CME. |