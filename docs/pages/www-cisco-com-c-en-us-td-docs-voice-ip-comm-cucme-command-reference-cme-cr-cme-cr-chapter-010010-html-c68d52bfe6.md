---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-command-reference-cme-cr-cme-cr-chapter-010010-html-c68d52bfe6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/command/reference/cme_cr/cme_cr_chapter_010010.html
retrieved_at: 2026-08-21T22:57:10.502739+00:00
---

Cisco Unified Communications Manager Express Command Reference

# Cisco Unified Communications Manager Express Command Reference

Updated: July 19, 2018

Chapter: Cisco Unified CME Commands: T

## Chapter: Cisco Unified CME Commands: T

# Cisco Unified CME Commands: T

## telephony-service

To enter
                              		  telephony-service configuration mode for configuring Cisco Unified CME, use the telephony-service command in global configuration
                              		  mode. To remove the entire Cisco Unified CME configuration for SCCP IP phones,
                              		  use the no form of
                              		  this command.

telephony-service [ setup ]

no telephony-service

### Syntax Description

setup

(Optional) Interactive setup tool for configuring Cisco Unified IP Phone 7910s,
                                          						7940s, and 7960s in Cisco Unified CME.

### Command Default

No Cisco Unified
                              		  CME configuration for SCCP IP phones is present.

### Command Modes

Global configuration (config)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.1(5)YD

Cisco
                                          						ITS 1.0

This
                                          						command was introduced.

12.2(8)T

Cisco
                                          						ITS 2.0

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T.

12.2(15)ZJ

Cisco
                                          						CME 3.0

The setup keyword
                                          						was added.

12.3(4)T

Cisco
                                          						CME 3.0

This
                                          						command was integrated into Cisco IOS Release 12.3(4)T.

### Usage Guidelines

This command
                              		  enters the telephony-service configuration mode for configuring system wide
                              		  parameters for SCCP IP phones in Cisco Unified CME.

Use the setup keyword
                              		  to start the interactive setup tool to automatically configure only Cisco
                              		  Unified IP Phone 7910s, 7940s, and 7960s in Cisco Unified CME.

For alternate
                              		  methods of automatically configuring Cisco Unified CME, including Cisco Unified
                              		  IP Phone 7910s, 7940s, and 7960s and other Cisco Unified IP phones, see the Cisco Unified CME
                                 			 Administrator Guide.

The setup keyword
                              		  is not stored in the router nonvolatile random-access memory (NVRAM).

If you attempt to
                              		  use the setup option
                              		  for a system that already has a telephony-service configuration, the command is
                              		  rejected. To use the setup option
                              		  after an existing telephony-service configuration has been created, first
                              		  remove the existing configuration using the no telephony-service command.

The table shows a
                              		  sample dialog with the Cisco CME setup tool and explains possible responses to
                              		  the Cisco CME setup tool prompts.

Cisco CME
                                          					 Setup Tool Prompt

Description

```
Do you want to setup DHCP service for your IP phones? [yes/no]:
```

If you
                                          					 respond yes, you see the following prompts:

```
IP network for telephony-service DHCP  Pool:
Subnet mask for DHCP network : 
TFTP Server IP address (Option 150) :
Default Router for DHCP Pool :
```

- Yes—Configures the Cisco Unified CME router to act as a Dynamic Host
                                             						Configuration Protocol (DHCP) server, automatically providing IP addresses to
                                             						your IP phones and provisioning the default gateway and TFTP IP addresses to be
                                             						used by the phones. This method creates a single pool of IP addresses. If you
                                             						need a pool for non-IP phones or if the Cisco router cannot act as the DHCP
                                             						router, answer no and manually define the DHCP server.

- No—Indicates that you have already configured DHCP or static IP addresses for
                                             						the IP phones.

```
Do you want to start telephony-service setup? [yes/no]:
```

- Yes— Starts
                                             						the interactive setup tool for configuring Cisco Unified IP Phone 7910s, 7940s,
                                             						and 7960s.

- No —Terminates the Cisco CME setup tool.

```
Enter the IP source address for Cisco CallManager Express:
Enter the Skinny Port for Cisco CallManager Express:  [2000]:
```

IP
                                          					 address on which the router provides Cisco Unified CME services, usually the
                                          					 default gateway for the IP subnet that you are using for the IP phones, and the
                                          					 port for Skinny Client Control Protocol (SCCP) messages.

```
How many IP phones do you want to configure : [0]:
```

Enter
                                          					 the maximum number of IP phones that this Cisco Unified CME system will
                                          					 support. This number can be increased later, to the maximum allowed for this
                                          					 version and your router.

```
Do you want dual-line extensions assigned to phones? [yes for dual-line / no for single-line]:
```

- Yes —Each
                                             						newly registering IP phones is assigned a single number that is associated with
                                             						a single phone button. The system generates a dual-line ephone-dn entry for
                                             						each ephone-dn.

- No —IP
                                             						phones are linked directly to one or more PSTN trunk lines. Using keyswitch
                                             						mode requires manual configuration in addition to using the Cisco CME setup
                                             						tool. The system generates two ephone-dn entries for each ephone-dn, and they
                                             						are both assigned to a single phone.

```
What language do you want on IP phones?
      0  English
      1  French
      2  German
      3  Russian
      4  Spanish
      5  Italian
      6  Dutch
      7  Norwegian
      8  Portuguese
      9  Danish
      10  Swedish
 [0]:
```

Language for IP phone displays, selected from the list.

- Default is 0, English.

```
Which Call Progress tone set do you want on IP phones :     
      0  United States
      1  France
      2  Germany
      3  Russia
      4  Spain
      5  Italy
      6  Netherlands
      7  Norway
      8  Portugal
      9  UK
    10  Denmark
    11  Switzerland
    12  Sweden
    13  Austria
    14  Canada
[0]:
```

Locale
                                          					 for the tone set used to indicate call status or progress, selected from the
                                          					 list.

- Default is 0, United States.

```
What is the first extension number you want to configure :[0]:
```

First
                                          					 number in pool of extension numbers to be created for IP phones connected to
                                          					 the Cisco router to be configured.

- Starting with this number, remaining extension numbers are automatically
                                             						configured in a contiguous manner.

- This
                                             						number must be compatible with your telephone number plan and if you use Direct
                                             						Inward Dialing (DID) service, with public switched telephone network (PSTN)
                                             						numbering requirements.

```
Do you have Direct-Inward-Dial service for all your phones? [yes/no]:
```

- Yes—If you have trunk access to public telephone service by ISDN or VoIP for
                                             						all extension numbers. The system creates an appropriate dial plan.

- No—If you have simple analog phone lines only (for example, foreign exchange
                                             						office [FXO] interfaces) or if you have trunk access for some lines but not all
                                             						lines.

If you
                                          					 answer yes to the previous question, you see the following prompt:

```
Enter the full E.164 number for the first phone:
```

Complete ten-digit telephone number, including area code, that corresponds to
                                          					 the first extension number.

```
Do you want to forward calls to a voice message service? [yes/no]:
```

- Yes—To forward calls to a single voice message service number when an IP phone
                                             						is busy or does not answer. All phone extensions forward their calls to the
                                             						same voice message service pilot number.

- No—Not to forward calls to a single voice message service number. Answer no if
                                             						you do not have a voice message system or if you want to customize
                                             						call-forwarding behavior for each extension.

If you
                                          					 answer yes to the previous question, you see the following prompt:

```
Enter the extension or pilot number of the voice message service:
```

Voice
                                          					 message service pilot number.

- This
                                             						step can be ignored during the setup dialog and manually configured later.

```
Call forward No Answer Timeout: [18]:
```

Timeout, in seconds, after which to forward calls to voice mail if they are not
                                          					 answered.

- Default is 18.

```
Do you wish to change any of the above information? [yes/no]:
```

- Yes —Starts
                                             						the dialog over again without implementing any of the answers that you
                                             						previously gave.

- No —Uses
                                             						specified values to automatically build basic configuration for Cisco Unified
                                             						IP Phone 7910s, 7940s, and 7960s in Cisco Unified CME.

## Examples

The following
                              		  example shows how to enter telephony-service configuration mode for manually
                              		  configuring Cisco Unified CME. This example also includes the for configuring
                              		  the maximum number of phones to 12:

```
Router(config)# telephony-service Router(config-telephony)# max-ephones 12
```

The following
                              		  example shows how to start the Cisco CME setup tool:

```
Router(config)# telephony-service setup
```

## telnet-support

To enable the
                              		  telnet access for the phone, use the telnet-support command in voice register pool-type mode. To disable
                              		  telnet support, use the no form of
                              		  this command.

telnet-support

no telnet-support

### Syntax
                              		  Description

This command has
                              		  no arguments or keywords.

### Command Default

The telnet support
                              		  is not enable. When the reference-pooltype command is configured, the
                              		  telnet-support value of the reference phone is inherited.

### Command Modes

Voice Register Pool Configuration (config-register-pool)`

## Command History

15.3(3)M

Cisco SIP
                                       					 CME 10.0

This
                                       					 command was introduced.

### Usage Guidelines

Use this command
                              		  to enable the telnet access for the phone. When you use the no form of this
                              		  command, the inherited properties of the reference phone takes precedence over
                              		  the default value.

## Examples

The following
                              		  example shows how to specify a description for a phone model using the description command:

```
Router(config)# voice register pool-type 9900 Router(config--register-pool-type)# telnet-support
```

### Related Commands

Command

Description

Adds a new Cisco Unified SIP IP phone to Cisco Unified CME.

## template
                        	 (auto-register)

To create a basic
                              		  configuration template that supports all the configurations available on the
                              		  voice register template, use the template command in voice auto register configuration mode. This
                              		  command is a sub-mode CLI of the command auto-register . To disable creation of the basic configuration template as
                              		  part of the auto registration process , use the no form of
                              		  this command.

template tag

no template

### Syntax Description

template tag

Creates
                                          						a basic configuration template that supports all the configurations available
                                          						on the voice register template. Range: 1 to 10.

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

This command
                              		  provides the option to create a basic configuration template that can be
                              		  applied to all phones registering automatically on Unified CME. It is mandatory
                              		  that voice register template is configured with the same template tag.

## Examples

The following
                              		  example shows how to create a basic configuration template for auto
                              		  registration of SIP phones:

```
Router(config)#voice register global
Router(config-register-global)#auto-register
Router(config-voice-auto-register)# ?

VOICE auto register configuration commands: auto-assign Define DN range for auto assignment default Set a command to its defaults exit Exit from voice register group configuration mode no Negate a command or set its defaults password Default password for auto-register phones service-enable Enable SIP phone Auto-Registration template Default template for auto-register phones

Router(config-voice-auto-register)#template ?   
 <1-10> template tag
Router(config-voice-auto-register)#template 10
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

auto-assign (auto-register)

Configures the mandatory range of directory numbers for phones
                                          						auto registering on Unified CME.

auto-register

Enables
                                          						automatic registration of SIP phones with the Cisco Unified CME system.

auto-reg-ephone

Enables automatic registration of ephones with the Cisco Unified CME system.

## template (voice register pool)

To apply a template to a SIP phone, use the template command in voice register pool
                              		  configuration mode. To remove the template, use the no form of this command.

template template-tag

no template template-tag

### Syntax Description

template-tag

The template tag that was created with the voice register template command in voice register
                                          						global configuration mode. Range is 1 to 5.

### Command Default

Template is not applied to a SIP IP phone.

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

Apply any one of five previously defined templates to a SIP phone.
                              		  Only one template is applied to a SIP phone at one time.

## Examples

The following example shows how to define templates 1 and 2 and apply
                              		  template 1 to SIP phones 1, 2, and 3, and template 2 to SIP phone 4:

```
Router(config)# voice register template 1 Router(config-register-temp)# anonymous block Router(config-register-temp)# caller-id block Router(config-register-temp)# voicemail 5001 timeout 15 Router(config)# voice register template 2 Router(config-register-temp)# anonymous block Router(config-register-temp)# caller-id block Router(config-register-temp)# no conference Router(config-register-temp)# no transfer-attended Router(config-register-temp)# voicemail 5005 timeout 15 Router(config)# voice register pool 1 Router(config-register-pool)# template 1 Router(config)# voice register pool 2 Router(config-register-pool)# template 1 Router(config)# voice register pool 3 Router(config-register-pool)# template 1 Router(config)# voice register pool 4 Router(config-register-pool)# template 2
```

### Related Commands

Description

voice register template

Enters voice register template configuration mode and
                                          						defines a template of common parameters for SIP phones.

## tftp-path (voice register global)

To specify the directory to which the configuring files for SIP
                              		  phones in Cisco Unified CME are written, use the tftp-path command in voice register global
                              		  configuration mode. To return to the default, use the no form of this command.

tftp-path { flash: | slot0: | tftp: | //url }

no tftp-path

### Syntax Description

flash:

Router flash memory.

slot0:

Router slot 0 memory.

tftp://

External TFTP server.

url

URL for external TFTP server.

### Command Default

The default directory is system memory (system:/cme/sipphone/).

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

This command defines the location for configuration files that are
                              		  generated by using the create profile command.

## Examples

The following example shows how to set the path to an HTTP directory
                              		  for an external TFTP server:

```
Router(config)# voice register global Router(config-register-global)# tftp-path tftp://mycompany.com/files/
```

### Related Commands

Command

Description

create profile (voice register global)

Generates the configuration profiles required for SIP
                                          						phones.

reset (voice register global)

Performs a “hard” reboot similar to a power-off-power-on
                                          						sequence for all SIP phones in Cisco Unified CME, including contacting the
                                          						Dynamic Host Configuration Protocol (DHCP) server and the TFTP server for
                                          						updated information.

## tftp-server-credentials trustpoint

To specify the PKI trustpoint that signs the phone configuration
                              		  files, use the tftp-server-credentials trustpoint command in telephony-service
                              		  configuration mode. To return to the default, use the no form of this command.

tftp-server-credentials trustpoint label

no tftp-server-credentials trustpoint

### Syntax Description

label

Name of a configured PKI trustpoint with a valid
                                          						certificate.

### Command Default

No trustpoint is defined for TFTP server communications.

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

This command is used with Cisco Unified CME phone authentication.

## Examples

The following example names the CA trustpoint, server12, as the
                              		  trustpoint that signs the phone configuration files.

```
Router(config)# telephony-service Router(config-telephony)# device-security-mode authenticated Router(config-telephony)# secure-signaling trustpoint server25 Router(config-telephony)# tftp-server-credentials trustpoint server12 Router(config-telephony)# load-cfg-file slot0:Ringlist.xml alias Ringlist.xml sign create Router(config-telephony)# exit
```

## time-format

To select a 12-hour clock or a 24-hour clock for the time display
                              		  format on Cisco IP phones in a Cisco CallManager Express (Cisco CME) system,
                              		  use the time-format command in
                              		  telephony-service configuration mode. To return to the default, use the no form of this command.

time-format { 12 | 24 }

no time-format

### Syntax Description

12

Selects a 12-hour clock. This is the default.

24

Selects a 24-hour clock.

### Command Default

Time is displayed in 12-hour clock format.

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

The following example selects a 24-hour clock for the time display on
                              		  Cisco IP phones:

```
Router(config)# telephony-service Router(config-telephony)# time-format 24
```

### Related Commands

Description

date-format

Selects a format to display the date on Cisco IP phones.

## time-format (voice register global)

To set the time display format on SIP phones in a Cisco CallManager
                              		  Express (Cisco CME) system, use the time format command
                              		  in voice register global configuration mode. To display the time in the default
                              		  format, use the no form of this command.

time-format { 12 | 24 }

no date-format

### Syntax Description

12

Sets time in a 12-hour (AM/PM) clock.

24

Sets time in a 24-hour clock.

### Command Default

Time is displayed in 12-hour clock format.

### Command Modes

Voice register global configuration (config-register-global)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4

This command was introduced.

## Examples

The following example shows how to set the time format to a 24-hour
                              		  clock so that 11:00PM is displayed as 2300.

```
Router(config)# voice register global Router(config-register-global)# time-format 24
```

### Related Commands

Description

voice register global

Enters voice register global configuration mode in order to
                                          						set global parameters for all supported Cisco SIP phones in a Cisco CME or
                                          						Cisco SIP SRST environment.

## timeout (ephone-hunt)

To define the number of seconds after which a call that is not
                              		  answered is redirected to the next number in a hunt-group list in Cisco Unified
                              		  CME, use the timeout command in ephone-hunt configuration
                              		  mode. To return to the default, use the no form of this command.

timeout seconds [,
                                 				  seconds...]

no
                                 				  timeout seconds [,seconds...]

### Syntax Description

seconds

Number of seconds. Range: 3 to 60000. You can enter a
                                          						different value for each hop between ephone-dns in a hunt group. If you enter a
                                          						single value, the value is applied to each hop between ephone-dns in a hunt
                                          						group.

### Command Default

Default is the value of the timeouts ringing which has a default of 180 seconds if it
                              		  is not set to another value.

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

12.4(4)XC

Cisco Unified CME 4.0

This command was modified to accept multiple arguments that
                                          						correspond to the number of ephone-dns configured in the hunt group.

## Command History

12.4(9)T

Cisco Unified CME 4.0

This command with modifications up was integrated into
                                          						Cisco IOS Release 12.4(9)T.

### Usage Guidelines

Use this command to set no-answer timeouts for each hop in a hunt
                              		  group. You can enter a different value for each hop between ephone-dns in a
                              		  hunt group or you enter a single value to be applied to each hop between
                              		  ephone-dns in a hunt group list.

If you configure this command and you also configure the max-timeout for an ephone hunt group, the max-timeout takes precedence over this
                              		  command.

## Examples

The following example defines a no-answer timeout of 10 seconds for
                              		  each hop between ephone-dns in hunt group 25. If extension 1001 does not answer
                              		  in 10 seconds, the call is sent to 1002. If 1002 does not answer in 10 seconds,
                              		  the call is sent to 1003. If 1003 does not answer in 10 seconds, the call is
                              		  sent to the final number.

```
ephone-hunt 25 sequential
 pilot 4200
 list 1001, 1002, 1003
 timeout 10
 final 4500
```

The following example shows a hunt-group configuration with separate
                              		  timeouts, one for each ephone in the hunt-group. If the first extension (1001)
                              		  does not answer in 7 seconds, the call is sent to the second extension (1002).
                              		  If the call is not answered by the second extension in 9 seconds, the call is
                              		  forwarded to the third extension (1003). Extension 1003 has 15 seconds to
                              		  answer before the call is sent to the final number.

```
ephone-hunt 3 peer
 pilot 4200
 list 1001, 1002, 1003
 timeout 7, 9, 15
 final 4500
```

The following example shows the configuration for an ephone hunt
                              		  group for which the max-timeout command is also configured. Using
                              		  this configuration, if the second number is busy, the third extension, 1003,
                              		  has only 13 seconds to answer (20 - 7 = 13) because the value for max-timeout
                              		  is 20 seconds.

```
ephone-hunt 3 peer
 pilot 4200
 list 1001, 1002, 1003
 timeout 7, 9, 15
 max-timeout 20
 final 4500
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
                                          						Cisco Unified CME system.

max-timeout

Sets the maximum combined timeout for the no-answer periods
                                          						for all ephone-dns in an ephone-hunt list,

no-reg (ephone-hunt)

Specifies that the pilot number of an ephone hunt group
                                          						should not register with the H.323 gatekeeper.

pilot

Defines the ephone-dn that callers dial to reach an ephone
                                          						hunt group.

preference (ephone-hunt)

Sets preference order for the ephone-dn associated with an
                                          						ephone-hunt-group pilot number.

## timeout (voice hunt-group)

To define the number of seconds after which a call that is not
                              		  answered is redirected to the next number in a voice hunt-group list, use the timeout command in voice hunt-group
                              		  configuration mode. To return to the default timeout, use the no form of this command.

timeout seconds

no timeout

### Syntax Description

seconds

Number of seconds. Range is 3 to 60000. Default is 180.

### Command Default

Timeout period is 180 seconds.

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

If Call Forward No Answer is configured for a directory number in the
                              		  voice hunt group, set the timeout value of this command to a value that is less
                              		  than the timeout value of the call-forward noan command.

## Examples

The following example shows how to define a no-answer timeout of 15
                              		  seconds for each hop between phones in peer hunt-group 25:

```
Router(config)# voice hunt-group 25 peer Router(config-voice-hunt-group)# timeout 15
```

### Related Commands

Command

Description

call-forward noan

Enables call forwarding so that incoming calls to an
                                          						extension (ephone-dn) that does not answer are forwarded to another number.

final (voice hunt-group)

Defines the last extension in a voice hunt group.

hops (voice hunt-group)

Defines the number of times that a call is redirected to
                                          						the next directory number in a peer voice hunt-group list before proceeding to
                                          						the final directory number.

list (voice hunt-group)

Defines the directory numbers that participate in a hunt
                                          						group.

## timeouts busy

To set the amount of time after which a call is disconnected from a
                              		  busy signal, use the timeouts busy command in telephony-service configuration
                              		  mode. To return to the default value, use the no form of this command.

timeouts busy seconds

no timeouts busy

### Syntax Description

seconds

Number of seconds after connection before a call is
                                          						disconnected from a busy signal. Range is from 0 to 30 seconds. Default is 10.

### Command Default

Timeout busy period is 10 seconds.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(8)T

Cisco ITS 2.0

This command was introduced.

## Examples

The following example sets a busy timeout of 10 seconds:

```
Router(config)# telephony-service Router(config-telephony)# timeouts busy 10
```

### Related Commands

Description

telephony-service

Enters telephony-service configuration mode.

## timeouts interdigit (telephony-service)

To set the interdigit timeout value for all Cisco IP phones in a
                              		  Cisco Unified CME system, use the timeouts interdigit command in telephony-service
                              		  configuration mode. To return to the default value, use the no form of this command.

timeouts interdigit seconds

no timeouts interdigit

### Syntax Description

seconds

Interdigit timeout duration for Cisco IP phones, in
                                          						seconds. Range is from 2 to 120. Default is 10.

### Command Default

Timeout period is 10 seconds.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(2)XB

Cisco ITS 1.0

This command was introduced.

12.2(8)T

Cisco ITS 2.0

This command was integrated into Cisco IOS Release
                                          						12.2(8)T.

### Usage Guidelines

The interdigit timeout timer is activated when the caller enters a
                              		  digit and is restarted each time the caller enters subsequent digits until the
                              		  destination address is identified. This command specifies how long, in seconds,
                              		  the system waits after a caller enters an initial digit or a subsequent digit
                              		  of a dialed string. If the configured timeout value is exceeded before the
                              		  destination address is identified, a tone sounds and the call is terminated.
                              		  The default is 10 seconds.

To disable the timeouts interdigit timer, set the seconds value to zero.

## Examples

The following example sets the interdigit timeout value to 5 seconds
                              		  for all Cisco IP phones:

```
Router(config)# telephony-service Router(config-telephony)# timeouts interdigit 5
```

In this example, 5 seconds is also the elapsed time after which an
                              		  incompletely dialed number times out. For example, if you dial nine digits
                              		  (408555013) instead of the required ten digits (4085550134), you hear a busy
                              		  tone after 5 “timeout” seconds.

### Related Commands

Description

timeouts interdigit (voice-port)

Configures the interdigit timeout value for a specified
                                          						voice port.

## timeouts
                        	 interdigit (voice register global)

To set the
                              		  interdigit timeout value for all Cisco SIP phones in a Cisco Unified CME
                              		  system, use the timeouts interdigit command in voice register global
                              		  configuration mode. To return to the default value, use the no form of
                              		  this command.

timeouts interdigit seconds

no timeouts interdigit

### Syntax Description

seconds

Interdigit timeout duration for Cisco SIP phones, in seconds. Range is from 2
                                          						to 120. Default is 10.

### Command Default

Timeout period is
                              		  10 seconds.

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

The interdigit
                              		  timeout timer is activated when the caller enters a digit and is restarted each
                              		  time the caller enters subsequent digits until the destination address is
                              		  identified. This command specifies how long, in seconds, the system waits after
                              		  a caller enters an initial digit or a subsequent digit of a dialed string. If
                              		  the configured timeout value is exceeded before the destination address is
                              		  identified, a tone sounds and the call is terminated. The default is 10
                              		  seconds.

To disable the
                              		  timeouts interdigit timer, set the seconds value to zero.

## Examples

The following
                              		  example sets the interdigit timeout value to 5 seconds for all Cisco SIP
                              		  phones:

```
Router(config)# voice register global Router(config-register-global)# timeouts interdigit 5
```

### Related Commands

Description

timeouts interdigit (telephoy-service)

Configures the interdigit timeout value for a SCCP phone in Cisco Unified CME
                                          						system.

## timeouts night-service-bell

To specify the interval between two night-service notification bells,
                              		  use the timeouts night-service-bell command in telephony-service configuration mode. To reset to
                              		  the default value, use the no form of this command.

timeouts night-service-bell seconds

no timeouts night-service-bell

### Syntax Description

seconds

Duration, in seconds, between night-service notification
                                          						bells. Range: 4 to 30. Default: 12.

### Command Default

Default is 12 seconds.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(11)XW5

Cisco Unified CME 4.2

This command was introduced.

### Usage Guidelines

This command modifies the repeat interval between two night-service
                              		  notification bells for the same call from the default (12 seconds) to the
                              		  specified number of seconds.

When an ephone-dn is marked for night-service treatment, incoming
                              		  calls that ring during the night-service time period on that directory number
                              		  send a notification to all IP phones that are marked to receive night-service
                              		  bell notification.

## Examples

The following partial output shows that the night-service
                              		  notification bell is configured for 4 seconds between bells for the same call:

```
Router# show running-configuration .
.
.
telephony-service 
.
.
.
 night-service code *1234 
 night-service day Tue 00:00 23:00 
 night-service day Wed 01:00 23:59 
 timeouts night-service-bell 4
! 
!
```

### Related Commands

Command

Description

night-service bell (ephone)

Marks an IP phone to receive night-service bell
                                          						notification when incoming calls are received during night-service time periods
                                          						on ephone-dns that are marked for night service.

night-service bell (ephone-dn)

Marks an ephone-dn to send night-service bell notification
                                          						to designated IP phones during night-service time periods.

## timeouts ringing (telephony-service)

To set the timeout value for ringing in a Cisco CallManager Express
                              		  (Cisco CME) system, use the timeouts ringing command in telephony-service configuration
                              		  mode. To reset the timeout value to the default value, use the no form of this command.

timeouts ringing seconds

no timeouts ringing

### Syntax Description

seconds

Duration, in seconds, for which the Cisco CME system allows
                                          						ringing to continue if a call is not answered. Range is from 5 to 60000.
                                          						Default is 180.

### Command Default

Timeout is 180 seconds.

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

## Examples

The following example allows incoming calls to ring for 600 seconds:

```
Router(config)# telephony-service Router(config-telephony)# timeouts ringing 600
```

### Related Commands

Description

telephony-service

Enters telephony-service configuration mode.

## timeouts transfer-recall

To enable Cisco Unified CME to recall a transferred call if the
                              		  transfer-to party does not answer or is busy, use the timeouts transfer-recall command in ephone-dn, ephone-dn template, or telephony-service
                              		  configuration mode. To reset to the default value, use the no form of this command.

timeouts transfer-recall seconds

no timeouts transfer-recall

### Syntax Description

seconds

Duration, in seconds, to wait before recalling a
                                          						transferred call. Range: 1 to 1800. Default: 0 (disabled).

### Command Default

Transfer recall is disabled (0 seconds).

### Command Modes

Ephone-dn (config-ephone-dn) Ephone-dn template (config-ephone-dn-template) Telephony-service configuration (config-telephony)

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

This command enables Call Transfer Recall and sets the number of
                              		  seconds that Cisco Unified CME waits before sending a transferred call back to
                              		  the phone that initiated the transfer (transferor).

If the transfer-recall timer set with this command expires before the
                              		  transfer-to party answers a call, the call is directed back to the transferor
                              		  and the message, “Transfer Recall From xxxx” displays on the transferor phone.
                              		  After the first recall, the timer restarts. The maximum number of retries is
                              		  two if the transfer-to party remains busy or does not answer. The transferor
                              		  and transfer-to party must be on the same Cisco Unified CME router; the
                              		  transferee party can be remote.

Transfer recall is not supported if the transfer-to party has Call
                              		  Forward Busy configured or is a member of any hunt group. If the transfer-to
                              		  directory number has Call Forward No Answer (CFNA) enabled, Cisco Unified CME
                              		  recalls a transferred call only if the transfer-recall timeout is less than the
                              		  timeout set with the call-forward noan command. If the transfer-recall timeout is
                              		  set to more than the CFNA timeout, the call is forwarded to the CFNA target
                              		  number if the transfer-to party does not answer.

If the transferor is busy at the time of the recall, Cisco Unified
                              		  CME attempts the recall again after the retry timer expires. The maximum number
                              		  of retries is two. If the transferor phone remains busy, the call is
                              		  disconnected after the third recall attempt.

Use this command in telephony-service configuration mode to enable
                              		  the transfer-recall timer at the system level for all directory numbers. Use
                              		  this command in ephone-dn configuration mode to enable the transfer-recall
                              		  timer for a particular directory number, or use the command in ephone-dn
                              		  template mode to apply it to one or more directory numbers.

If you use an ephone-dn template to apply a command to a directory
                              		  number and you also use the same command in ephone-dn configuration mode for
                              		  the same directory number, the value that you set in ephone-dn configuration
                              		  mode has priority. This command, set in telephony-service configuration mode,
                              		  has the lowest priority.

## Examples

The following example shows that transfer recall is enabled for
                              		  extension 1030 (ephone-dn 103), which is assigned to ephone 3. If extension
                              		  1030 forwards a call and the transfer-to party does not answer, after 60
                              		  seconds the unanswered call is sent back to extension 1030 (transferor).

```
ephone-dn  103
 number 1030
 name Smith, John
 timeouts transfer-recall 60
!
ephone  3
 mac-address 002D.264E.54FA
 type 7962
 button  1:103
```

### Related Commands

Command

Description

call-forward busy

Enables call forwarding so that incoming calls to a busy
                                          						extension (ephone-dn) are forwarded to another extension.

call-forward noan

Enables call forwarding so that incoming calls to an
                                          						extension (ephone-dn) that does not answer are forwarded to another number.

transfer-mode

Specifies the call transfer method for an individual
                                          						directory number.

transfer-system

Specifies the call transfer method globally for all
                                          						directory numbers.

trunk

Associates an ephone-dn with a foreign exchange office
                                          						(FXO) port.

## timeouts
                        	 transfer-recall (voice register global)

To enable Cisco
                              		  Unified CME to recall a transferred call if the transfer-to party does not
                              		  answer or is busy, use the timeouts transfer-recall command in voice register global configuration mode. To reset
                              		  to the default value, use the no form of
                              		  this command.

timeouts transfer-recall seconds

no timeouts transfer-recall

### Syntax Description

seconds

Duration, in seconds, to wait before recalling a transferred call. Range: 1 to
                                          						1800. Default: 0 (disabled).

### Command Default

Transfer recall
                              		  is disabled (0 seconds) on a Cisco Unified SIP IP phone.

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

This command
                              		  enables Call Transfer Recall and sets the number of seconds that Cisco Unified
                              		  CME waits before sending a transferred call back to the phone that initiated
                              		  the transfer (transferor).

If the
                              		  transfer-recall timer set with this command expires before the transfer-to
                              		  party answers a call, the call is directed back to the transferor and the
                              		  message, “Transfer Recall From xxxx” displays on the transferor phone. If the
                              		  transferor is busy after the recall, the timer restarts. The maximum number of
                              		  retries is two if the transfer-to party remains busy or does not answer. The
                              		  transferor and transfer-to party must be on the same Cisco Unified CME router;
                              		  the transferee party can be remote.

Transfer recall
                              		  is not supported if the transfer-to party has Call Forward Busy configured or
                              		  is a member of any hunt group. The transferor phone and transfer-to phone must
                              		  be registered to the same Cisco Unified CME, however the transferee phone can
                              		  be remote. If the transfer-to directory number has Call Forward No Answer
                              		  (CFNA) enabled, Cisco Unified CME recalls the call only if the transfer-recall
                              		  timeout is set to less than the CFNA timeout. If the transfer-recall timeout is
                              		  set to more than the CFNA timeout, the call is forwarded to the CFNA target
                              		  number after the transfer-to party does not answer. If the transfer-recall
                              		  timeout is equal to the CFNA timeout, the call is forwarded to the CFNA target
                              		  number as the CFNA timeout expires before the transfer-recall timeout.

When Call Forward
                              		  All is configured in Cisco Unified CME, the call is forwarded directly to call
                              		  forward target number irrespective of whether the phone is busy or idle. In
                              		  this scenario, transfer recall is not applicable after the call is forwarded.

If the transferor
                              		  phone is busy, Cisco Unified CME attempts the recall again after the
                              		  transfer-recall timeout value expires. Cisco Unified CME attempts a recall up
                              		  to three times. If the transferor phone remains busy, the call is disconnected
                              		  after the third recall attempt. Also, if the transferor phone is a shared line,
                              		  and if one of the phones is idle, the transfer recall is directed to the
                              		  transferor phone that is idle.

Use this command
                              		  in voice register global configuration mode to enable the transfer-recall timer
                              		  at the system level for all directory numbers.

The timeouts transfer-recall command in voice register global
                              		  configuration mode has lesser priority than the value that you set in voice
                              		  register dn configuration mode for the same directory number.

## Examples

The following
                              		  example shows that transfer recall is enabled for 20 seconds. If the
                              		  transfer-to party does not answer after 20 seconds, the unanswered call is sent
                              		  back to the (transferor).

```
Router(config)# voice register global
Router(config-register-global)# timeouts transfer-recall 20
```

### Related Commands

Command

Description

timeouts transfer-recall (Ephone-dn (config-ephone-dn) and
                                          						Telephony-service configuration (config-telephony)

Enables
                                          						Cisco Unified CME to recall a transferred call if the transfer-to party does
                                          						not answer or is busy.

## timeouts
                        	 transfer-recall (voice register dn)

To enable Cisco
                              		  Unified CME to recall a transferred call if the transfer-to party does not
                              		  answer or is busy, use the timeouts transfer-recall command in voice register dn configuration mode. To reset to
                              		  the default value, use the no form of
                              		  this command.

timeouts transfer-recall seconds

no timeouts transfer-recall

### Syntax Description

seconds

Duration, in seconds, to wait before recalling a transferred call. Range: 1 to
                                          						1800. Default: 0 (disabled).

### Command Default

Transfer recall
                              		  is disabled (0 seconds) on a Cisco Unified SIP IP phone.

### Command Modes

Voice register dn configuration (config-register-dn)

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

This command
                              		  enables Call Transfer Recall and sets the number of seconds that Cisco Unified
                              		  CME waits before sending a transferred call back to the phone that initiated
                              		  the transfer (transferor).

If the
                              		  transfer-recall timer set with this command expires before the transfer-to
                              		  party answers a call, the call is directed back to the transferor and the
                              		  message, “Transfer Recall From xxxx” displays on the transferor phone. If the
                              		  transferor is busy after the recall, the timer restarts. The maximum number of
                              		  retries is two if the transfer-to party remains busy or does not answer. The
                              		  transferor and transfer-to party must be on the same Cisco Unified CME router;
                              		  the transferee party can be remote.

Transfer recall
                              		  is not supported if the transfer-to party has Call Forward Busy configured or
                              		  is a member of any hunt group. The transferor phone and transfer-to phone must
                              		  be registered to the same Cisco Unified CME, however the transferee phone can
                              		  be remote. If the transfer-to directory number has Call Forward No Answer
                              		  (CFNA) enabled, Cisco Unified CME recalls the call only if the transfer-recall
                              		  timeout is set to less than the CFNA timeout. If the transfer-recall timeout is
                              		  set to more than the CFNA timeout, the call is forwarded to the CFNA target
                              		  number after the transfer-to party does not answer. If the transfer-recall
                              		  timeout is equal to the CFNA timeout, the call is forwarded to the CFNA target
                              		  number as the CFNA timeout expires before the transfer-recall timeout.

When Call Forward
                              		  All is configured in Cisco Unified CME, the call is forwarded directly to call
                              		  forward target number irrespective of whether the phone is busy or idle. In
                              		  this scenario, transfer recall is not applicable after the call is forwarded.

If the transferor
                              		  phone is busy, Cisco Unified CME attempts the recall again after the
                              		  transfer-recall timeout value expires. Cisco Unified CME attempts a recall up
                              		  to three times. If the transferor phone remains busy, the call is disconnected
                              		  after the third recall attempt. Also, if the transferor phone is a shared line,
                              		  and if one of the phones is idle, the transfer recall is directed to the
                              		  transferor phone that is idle.

Use this command
                              		  in voice register dn configuration mode to enable the transfer-recall timer for
                              		  a particular directory number.

If you use the timeouts transfer-recall command in voice register dn
                              		  configuration mode for the same directory number, the value that you set in
                              		  voice register dn configuration mode has priority than the value set in the
                              		  voice register global configuration mode (this has the lowest priority).

## Examples

The following
                              		  example shows that transfer recall is enabled for extension 111 (voice register
                              		  dn 1). If extension 111 forwards a call to voice register dn 2 and the
                              		  transfer-to party does not answer, after 20 seconds the unanswered call is sent
                              		  back to extension 1111 (transferor).

```
voice register dn  1
 timeouts transfer-recall 20
 number 111
voice register dn  2
 number 222
```

### Related Commands

Command

Description

timeouts transfer-recall (Ephone-dn (config-ephone-dn) and
                                          						Telephony-service configuration (config-telephony)

Enables
                                          						Cisco Unified CME to recall a transferred call if the transfer-to party does
                                          						not answer or is busy.

## time-webedit (telephony-service)

To enable the system administrator to set time on the Cisco Unified
                              		  CME router through the web interface, use the time-webedit command in telephony-service
                              		  configuration mode. To disable this feature, use the no form of this command.

time-webedit

no time-webedit

### Syntax Description

This command has no arguments or keywords.

### Command Default

Time-setting through the web interface is disabled.

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

Cisco IOS XE Gibraltar 16.11.1a Release

Unified CME 12.6

The command is deprecated. It is not supported on Unified CME 12.6 and later releases.

### Usage Guidelines

The time-webedit allows a local administrator of the Cisco Unified CME router to
                              		  change and set time through the web-based graphical user interface (GUI).

## Examples

The following example enables web editing of time:

```
Router(config)# telephony-service Router(config-telephony)# time-webedit
```

### Related Commands

Description

dn - webedit

Enables adding of directory numbers through a web
                                          						interface.

telephony-service

Enters telephony-service configuration mode.

## time-zone

To set the time
                              		  zone so that the correct local time is displayed on SCCP Cisco Unified IP
                              		  phones, use the time-zone command in telephony-service configuration mode. To disable a
                              		  time-zone setting configured with the time-zone command and return to the default time zone (Pacific Standard
                              		  Time), use the no form of
                              		  this command.

time-zone number

no time-zone

### Syntax Description

number

Numeric
                                          						code for a named time zone. The following are the selections. The numbers in
                                          						parentheses indicate the offset from Coordinated Universal Time (UTC) in
                                          						minutes.

- 1 —Dateline Standard Time (-720)

- 2 —Samoa
                                             						  Standard Time (-660)

- 3 —Hawaiian
                                             						  Standard Time (-600)

- 4 —Alaskan
                                             						  Standard/Daylight Time (-540)

- 5 —Pacific
                                             						  Standard/Daylight Time (-480)

- 6 —Mountain
                                             						  Standard/Daylight Time (-420)

- 7 —United
                                             						  States (US) Mountain Standard Time (-420)

- 8 —Central
                                             						  Standard/Daylight Time (-360)

- 9 —Mexico
                                             						  Standard/Daylight Time (-360)

- 10 —Canada
                                             						  Central Standard Time (-360)

- 11 —SA Pacific
                                             						  Standard Time (-300)

- 12 —Eastern
                                             						  Standard/Daylight Time (-300)

- 13 —US Eastern
                                             						  Standard Time (-300)

- 14 —Atlantic
                                             						  Standard/Daylight Time (-240)

- 15 —South
                                             						  America (SA) Western Standard Time (-240)

- 16 —Newfoundland Standard/Daylight Time (-210)

- 17 —SA
                                             						  Standard/Daylight Time (-180)

- 18 —SA Eastern
                                             						  Standard Time (-180)

- 19 —Mid-Atlantic Standard/Daylight Time (-120)

- 20 —Azores
                                             						  Standard/Daylight Time (-60)

- 21 —UTC
                                             						  Standard/Daylight Time (+0)

- 22 —Greenwich
                                             						  Standard Time (+0)

- 23 —Western
                                             						  Europe Standard/Daylight Time (+60)

- 24 —GTB
                                             						  (Athens, Istanbul, Minsk) Standard/Daylight Time (+60)

- 25 —Egypt
                                             						  Standard/Daylight Time (+60)

- 26 —Eastern
                                             						  Europe Standard/Daylight Time (+60)

number continued

- 27 —Romance
                                             						  Standard/Daylight Time (+120)

- 28 —Central
                                             						  Europe Standard/Daylight Time (+120)

- 29 —South
                                             						  Africa Standard Time (+120)

- 30 —Jerusalem
                                             						  Standard/Daylight Time (+120)

- 31 —Saudi
                                             						  Arabia Standard Time (+180)

- 32 —Russian
                                             						  Standard/Daylight Time (+180)

- 33 —Iran
                                             						  Standard/Daylight Time (+210)

- 34 —Caucasus
                                             						  Standard/Daylight Time (+240)

- 35 —Arabian
                                             						  Standard Time (+240)

- 36 —Afghanistan Standard Time (+270)

- 37 —West
                                             						  Asia Standard Time (+300)

- 38 —Ekaterinburg Standard Time (+300)

- 39 —India
                                             						  Standard Time (+330)

- 40 —Central
                                             						  Asia Standard Time (+360)

- 41 —Southeast Asia Standard Time (+420)

- 42 —China
                                             						  Standard/Daylight Time (+480)

- 43 —Taipei
                                             						  Standard Time (+480)

- 44 —Tokyo
                                             						  Standard Time (+540)

- 45 —Central
                                             						  Australia Standard/Daylight Time (+570)

- 46 —Australia Central Standard Time (+570)

- 47 —East
                                             						  Australia Standard Time (+600)

- 48 —Australia Eastern Standard/Daylight Time (+600)

- 49 —West
                                             						  Pacific Standard Time (+600)

- 50 —Tasmania
                                             						  Standard/Daylight Time (+600)

- 51 —Central
                                             						  Pacific Standard Time (+660)

- 52 —Fiji
                                             						  Standard Time (+720)

- 53 —New
                                             						  Zealand Standard/Daylight Time (+720)

- 54—Venezuela Standard Time (-270)

- 55—Pacific SA Daylight Time (-180)

- 56—Pacific SA Standard Time (-240)

### Command Default

The default is
                              		  time-zone 5, Pacific Standard/Daylight Time (-480).

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						product

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

### Usage Guidelines

This command
                              		  works with the vendorConfig section of the Sep*.cnf.xml configuration file,
                              		  which is read by the phone firmware when the Cisco IP Phone is booted up.
                              		  Certain phones, such as the Cisco Unified IP Phone 7906 , 7911, 7931, 7941,
                              		  7942, 7945, 7961, 7962, 7965, 7970 , 7971, and 7975, obtain Coordinated
                              		  Universal Time (UTC) from the clock of the Cisco router. To display the correct
                              		  local time, the time display on these phones must be offset by using this
                              		  command.

This command is
                              		  not required for Cisco Unified IP Phone 7902G, 7905G, 7912G, 7920, 7921, 7935,
                              		  7936, 7940, 7960, or 7985G.

For changes to
                              		  the time-zone settings take effect, the Sep*.cnf.xml file must be updated by
                              		  using the create cnf-files command and the Cisco IP phones must
                              		  rebooted by using the reset command.

## Examples

The following
                              		  example sets the Cisco IP Phone 7970 units to Fiji Standard Time:

```
Router(config)# telephony-service Router(config-telephony)# time-zone 53
```

### Related Commands

Command

Description

create cnf-files

Sets
                                          						display and phone functionality for the Cisco IP Phone 7970 units using the
                                          						vendorConfig parameters of the downloaded firmware’s Sep*.cnf.xml configuration
                                          						file.

reset (telephony-service)

Performs a complete reboot of one or all phones associated with a Cisco Unified
                                          						CME router.

## timezone (voice
                        	 register global)

To set the time
                              		  zone used for SIP phones in a Cisco Unified CME system, use the timezone command in voice register global configuration mode. To return to the default,
                              		  use the no form of
                              		  this command.

timezone number

no timezone

### Syntax Description

number

Range
                                          						is 1 to 53. Default is 5, Pacific Standard/Daylight Time

### Command Default

Default is 5,
                              		  Pacific Standard/Daylight Time.

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

### Usage Guidelines

The following
                              		  table lists the supported time zone numbers and the corresponding description.

Number

Description

Offset in
                                          					 Minutes

1

Dateline
                                          					 Standard Time

-720

2

Samoa
                                          					 Standard Time

-660

3

Hawaiian
                                          					 Standard Time

-600

4

Alaskan
                                          					 Standard/Daylight Time

-540

5

Pacific
                                          					 Standard/Daylight Time

-480

6

Mountain
                                          					 Standard/Daylight Time

-420

7

US
                                          					 Mountain Standard Time

-420

8

Central
                                          					 Standard/Daylight Time

-360

9

Mexico
                                          					 Standard/Daylight Time

-360

10

Canada
                                          					 Central Standard Time

-360

11

SA
                                          					 Pacific Standard Time

-300

12

Eastern
                                          					 Standard/Daylight Time

-300

13

US
                                          					 Eastern Standard Time

-300

14

Atlantic Standard/Daylight Time

-240

15

SA
                                          					 Western Standard Time

-240

16

Newfoundland Standard/Daylight Time

-210

17

South
                                          					 America Standard/Daylight Time

-180

18

SA
                                          					 Eastern Standard Time

-180

19

Mid-Atlantic Standard/Daylight Time

-120

20

Azores
                                          					 Standard/Daylight Time

-60

21

GMT
                                          					 Standard/Daylight Time

+0

22

Greenwich Standard Time

+0

23

W.
                                          					 Europe Standard/Daylight Time

+60

24

GTB
                                          					 Standard/Daylight Time

+60

25

Egypt
                                          					 Standard/Daylight Time

+60

26

E.
                                          					 Europe Standard/Daylight Time

+60

27

Romance
                                          					 Standard/Daylight Time

+120

28

Central
                                          					 Europe Standard/Daylight Time

+120

29

South
                                          					 Africa Standard Time

+120

30

Jerusalem Standard/Daylight Time

+120

31

Saudi
                                          					 Arabia Standard Time

+180

32

Russian
                                          					 Standard/Daylight Time

+180

33

Iran
                                          					 Standard/Daylight Time

+210

34

Caucasus Standard/Daylight Time

+240

35

Arabian
                                          					 Standard Time

+240

36

Afghanistan Standard Time

+270

37

West
                                          					 Asia Standard Time

+300

38

Ekaterinburg Standard Time

+300

39

India
                                          					 Standard Time

+330

40

Central
                                          					 Asia Standard Time

+360

41

SE Asia
                                          					 Standard Time

+420

42

China
                                          					 Standard/Daylight Time

+480

43

Taipei
                                          					 Standard Time

+480

44

Tokyo
                                          					 Standard Time

+540

45

Cen.
                                          					 Australia Standard/Daylight Time

+570

46

AUS
                                          					 Central Standard Time

+570

47

E.
                                          					 Australia Standard Time

+600

48

AUS
                                          					 Eastern Standard/Daylight Time

+600

49

West
                                          					 Pacific Standard Time

+600

50

Tasmania Standard/Daylight Time

+600

51

Central
                                          					 Pacific Standard Time

+660

52

Fiji
                                          					 Standard Time

+720

53

New
                                          					 Zealand Standard/Daylight Time

+720

54

Venezuela Standard Time

-270

55

Pacific
                                          					 SA Daylight Time

-180

56

Pacific
                                          					 SA Standard Time

-240

## Examples

The following
                              		  example shows how top set the time zone to 8, Central Standard Daylight Time:

```
Router(config)# voice register global Router(config-register-global)# timezone 8
```

### Related Commands

Command

Description

dst (voice register global)

Sets
                                          						the time period for daylight saving time on SIP phones.

dst auto-adjust (voice register global)

Enables automatic adjustment of daylight saving time on SIP phones.

time-format (voice register global)

Selects a 12-hour clock or a 24-hour clock for the time display format on SIP
                                          						phones in a Cisco CME system

## transfer max-length

To specify the maximum length of the transfer number, use the transfer max-length command in voice register pool or voice
                              		  register template configuration mode. To disable the maximum length, use the no form of this command.

transfer max-length max-length

no transfer max-length max-length

### Syntax Description

max-length

Maximum length of the transfer number. Range is 3 to 16.

### Command Default

No maximum length is specified for the transfer number.

### Command Modes

Voice register pool configuration (config-register-pool)

Voice register template configuration ((config-register-temp)

## Command History

Release

Modification

15.3(2)T

This command was introduced.

### Usage Guidelines

The transfer max-length command is used to indicate the maximum length of the number
                              		  being dialed for a call transfer. When only a specific number of digits are to
                              		  be allowed during a call transfer, a value between 3 and 16 is configured.When
                              		  the number dialed exceeds the maximum length configured, then the call transfer
                              		  is blocked.

## Examples

The following example shows how to configure the maximum length of
                              		  the transfer number under voice register pool 1. Because the maximum length is
                              		  configured as 5, only call transfers to Cisco Unified SIP IP phones with a
                              		  five-digit directory number are allowed. All call transfers to directory
                              		  numbers with more than five digits are blocked.

```
Router# configure terminal
Router(config)# voice register pool 1
Router(config-register-pool)# transfer max-length 5
```

The following example shows how to configure the maximum length of
                              		  the transfer number for a set of phones under voice register template 2:

```
Router# configure terminal
Router(config)# voice register template 2
Router(config-register-temp)# transfer max-length 10
```

Command

Description

voice register pool

Enters voice register pool configuration mode and creates a
                                          						pool configuration for a SIP IP phone in Cisco Unified CME or for a set of SIP
                                          						phones in Cisco Unified SIP SRST

voice register template

Enters voice register template configuration mode and
                                          						defines a template of common parameters for SIP phones.

## transfer-attended (voice register template)

To enable a soft key for attended transfer in a SIP phone template,
                              		  use the transfer-attended command in voice register
                              		  template configuration mode. To disable the soft key, use the no form of this command.

transfer-attended

no transfer-attended

### Syntax Description

This command has no arguments or keywords.

### Command Default

Soft key is enabled.

### Command Modes

Voice register template configuration (config-register-temp)

## Command History

Cisco IOS Release

Cisco product

Modification

12.4(4)T

Cisco CME 3.4

This command was introduced.

### Usage Guidelines

This command enables a soft key for attended transfer in the
                              		  specified template which can then be applied to SIP phones in Cisco CME. The
                              		  attended transfer soft key is enabled by default. To disable the attended
                              		  transfer soft key, use the no transfer-attended command. To apply the template
                              		  to a SIP phone, use the template command in voice register pool
                              		  configuration mode.

A blind transfer is one in which the transferring extension connects
                              		  the caller to a destination extension before ringback begins. A attended
                              		  transfer is one in which the transferring party either connects the caller to a
                              		  ringing phone (ringback heard) or speaks with the third party before connecting
                              		  the caller to the third party.

## Examples

The following example shows how to disable attended transfer in
                              		  template 1:

```
Router(config)# voice register template 1 Router(config-register-temp)# no transfer-attended
```

### Related Commands

Description

conference (voice register template)

Enables the soft key for conference in a SIP phone
                                          						template.

template

Applies a template to a SIP phone.

transfer-blind (voice register template)

Enables a soft key for blind transfer in a SIP phone
                                          						template.

## transfer-blind (voice register template)

To enable a soft key for blind transfer in a SIP phone template, use
                              		  the transfer-blind command in voice register
                              		  template configuration mode. To disable the soft key, use the no form of this command.

transfer-blind

no transfer-blind

### Syntax Description

This command has no arguments or keywords.

### Command Default

Soft key is enabled.

### Command Modes

Voice register template configuration (config-register-template)

## Command History

Cisco IOS Release

Version

Modification

12.4(4)T

Cisco CME 3.4

This command was introduced.

### Usage Guidelines

This command enables a soft key for blind transfer in the specified
                              		  template which can then be applied to SIP phones in Cisco CME. The blind
                              		  transfer soft key is enabled by default. To disable the blind transfer soft
                              		  key, use the no transfer-blind command. To apply the template to a
                              		  SIP phone, use the template command in voice register pool
                              		  configuration mode.

A blind transfer is one in which the transferring extension connects
                              		  the caller to a destination extension before ringback begins. A attended
                              		  transfer is one in which the transferring party either connects the caller to a
                              		  ringing phone (ringback heard) or speaks with the third party before connecting
                              		  the caller to the third party.

## Examples

The following example shows how to disable blind transfer in template
                              		  1:

```
Router(config)# voice register template 1 Router(config-register-temp)# no transfer-blind
```

### Related Commands

Description

conference (voice register template)

Enables the soft key for conference in a SIP phone
                                          						template.

template

Applies a template to a SIP phone.

transfer-attended (voice register template)

Enables the soft key for attended transfer on SIP phones.

## transfer-digit-collect

To select the digit-collection method for consultative
                              		  call-transfers, use the transfer-digit-collect command in
                              		  telephony-service configuration mode for Cisco Unified CME or in
                              		  call-manager-fallback configuration mode for Cisco Unified SRST. To reset to
                              		  the default value, use the no form of this command.

transfer-digit-collect { new-call | orig-call }

no transfer-digit-collect

### Syntax Description

new-call

Dialed digits are collected from new call leg. Default
                                          						value.

orig-call

Dialed digits are collected from original call leg.

### Command Default

Digits are collected from the new consultative call-leg
                              		  ( new-call keyword).

### Command Modes

Telephony-service configuration (config-telephony)

Call-manager-fallback configuration (config-cm-fallback)

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

This command specifies whether the dialed digits of the target number
                              		  are collected on the original call leg or on the new call leg that is created
                              		  when a phone user initiates a consultative call-transfer.

For consultative transfers, a local number is matched on the number command in ephone-dn configuration
                              		  mode; a PSTN number is matched on the transfer-pattern command in telephony service
                              		  mode.

The orig-call keyword selects the method used in
                              		  versions before Cisco Unified CME 4.3 and Cisco Unified SRST 4.3. After a phone
                              		  user presses the Transfer soft key, the dialed digits of the target number are
                              		  collected on the original call leg and buffered until either a local ephone-dn
                              		  or transfer-pattern is matched. When the transfer-to number is matched, the
                              		  original call is put on hold and an idle line or channel is seized to send the
                              		  dialed digits from the buffer.

The new-call keyword selects the default method
                              		  that is used in Cisco Unified CME 4.3 and later versions and Cisco Unified SRST
                              		  4.3 and later versions. The transfer-to digits are collected on a new
                              		  consultative call-leg that is created when the user presses the Transfer soft
                              		  key. The consultative call-leg is seized and the dialed digits are passed on
                              		  without being buffered until the digits are matched and the consultative
                              		  call-leg moves to the alerting state.

The new-call keyword is supported only if:

- The transfer-system full-consult command (default) is set in
                                 			 telephony-service configuration mode.

- The transfer-mode consult command (default) is set for
                                 			 transferor's directory number (ephone-dn).

- An idle line or channel is available for seizing, digit
                                 			 collection, and dialing.

A consultative transfer is one in which the transferring party either
                              		  connects the caller to a ringing phone (ringback heard) or speaks with the
                              		  third party before connecting the caller to the third party.

## Examples

The following example shows the digit-collection set to the method
                              		  used in versions before Cisco Unified CME 4.3 and Cisco Unified SRST 4.3:

```
Router(config)# telephony-service Router(config-telephony)# transfer-digit-collect orig-call
```

### Related Commands

Command

Description

transfer-mode

Specifies the type of call transfer for an individual
                                          						directory number that uses the ITU-T H.450.2 standard.

transfer-pattern (telephony-service)

Allows the transfer of calls to phones outside the local
                                          						Cisco Unified CME network.

transfer - system

Specifies the call transfer method for all IP phones on a
                                          						Cisco Unified CME router using the ITU-T H.450.2 standard.

## transfer-mode

To specify the type of call transfer for an individual IP phone
                              		  extension that uses the ITU-T H.450.2 standard, use the transfer-mode command in ephone-dn
                              		  configuration mode. To remove this specification, use the no form of this command.

transfer-mode { blind | consult }

no transfer-mode

### Syntax Description

blind

Transfers calls without consultation using a single phone
                                          						line.

consult

Transfers calls with consultation using a second phone
                                          						line, if available.

### Command Default

The ephone-dn uses the transfer-system value that was set systemwide.

### Command Modes

Ephone-dn configuration (config-ephone)

## Command History

Cisco IOS Release

Cisco CME Version

Modification

12.2(11)YT

2.1

This command was introduced.

12.2(15)T

2.1

This command was integrated into Cisco IOS Release
                                          						12.2(15)T.

### Usage Guidelines

This command specifies the type of call transfer for an individual
                              		  Cisco IP phone extension that is using the ITU-T H.450.2 protocol. It allows
                              		  you to override the system default transfer-system setting (full-consult or
                              		  full-blind) for that extension.

Call transfers that use H.450.2 can be blind or consultative. A blind
                              		  transfer is one in which the transferring phone connects the caller to a
                              		  destination extension before ringback begins. A consultative transfer is one in
                              		  which the transferring party either connects the caller to a ringing phone
                              		  (ringback heard) or speaks with the third party before connecting the caller to
                              		  the third party.

You can specify blind or consultative transfer on a system-wide basis
                              		  by using the transfer-system command. The system-wide
                              		  setting can then be overridden for individual phone extensions by using the transfer-mode command. For example, in a
                              		  Cisco CallManager Express (Cisco CME) network that is set up for consultative
                              		  transfer, a specific extension with an auto-attendant that automatically
                              		  transfers incoming calls to specific extension numbers can be set to use blind
                              		  transfer, because auto-attendants do not use consultative transfer.

Use this command with Cisco IOS Telephony Services V2.1, Cisco
                              		  CallManager Express 3.0, or a later version.

## Examples

The following example sets blind mode for call transfers from this
                              		  directory number:

```
Router(config)# ephone-dn 21354 Router(config-ephone-dn)# transfer-mode blind
```

### Related Commands

Description

ephone - dn

Enters ephone-dn configuration mode to set directory
                                          						numbers and parameters for individual Cisco IP phone lines.

transfer - system

Specifies the call transfer method for all IP phones on a
                                          						Cisco ITS router using the ITU-T H.450.2 standard.

## transfer-park blocked

To prevent extensions on an ephone from parking calls, use the transfer-park blocked command in ephone or ephone-template
                              		  configuration mode. To return to the default, use the no form of this command.

transfer-park blocked

no transfer-park blocked

### Syntax Description

This command has no arguments or keywords.

### Command Default

Transfer to park is allowed.

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

This command prevents transfers to park that use the Trnsfer soft key
                              		  and a call-park slot number, while allowing call-parks that use only the Park
                              		  soft key. To prevent use of the Park soft key, use an ephone template to remove
                              		  it from the phone.

An exception to this is made for phones with dedicated park slots. If
                              		  the transfer-park blocked command is used on an ephone that has a
                              		  dedicated park slot, the phone is blocked from parking calls at park slots
                              		  other than the dedicated park slot, but is still able to park calls at its own
                              		  dedicated park slot. On an IP phone, the user presses the Trnsfer soft key and
                              		  the call-park feature access code (FAC) to park a call at the phone's dedicated
                              		  park slot. On an analog phone, the user presses hookflash and the call-park
                              		  FAC.

When the transfer-park blocked command is used on an ephone that does not
                              		  have a dedicated park slot, the phone is blocked from parking any calls.

If you use an ephone template to apply a command to a phone and you
                              		  also use the same command in ephone configuration mode for the same phone, the
                              		  value that you set in ephone configuration mode has priority.

## Examples

The following example prevents ephone 25 and extensions 234, 235, and
                              		  236 from parking calls at any call-park slot.

```
ephone-dn 11
 number 234
ephone-dn 12
 number 235
ephone-dn 13
 number 236
ephone 25
 button 1:11 2:12 3:13
 transfer-park blocked
The following example uses an ephone template to prevent ephone 26 and extension 76589 from parking calls at any call-park slot.
ephone-dn 33
 number 76589
ephone-template 1
 transfer-park blocked
ephone 26
 button 1:33
 ephone-template 1
```

The following example sets up a dedicated park slot for the
                              		  extensions on ephone 6 and blocks transfers to call park from extensions 2977,
                              		  2978, and 2979 on that phone. Those extensions can still park calls at the
                              		  phone's dedicated park slot by using the Park soft key or Trnsfer and the
                              		  call-park FAC.

```
ephone-dn 3
 number 2558
 name Park 2977
 park-slot reserved-for 2977 timeout 60 limit 3 recall alternate 3754
ephone-dn 4
 number 2977
ephone-dn 5
 number 2978
ephone-dn 6
 number 2979
ephone 6
 button 1:4 2:5 3:6
 transfer-park blocked
```

## transfer-pattern (telephony-service)

To allow transfer of telephone calls from Cisco IP phones to phones
                              		  other than Cisco IP phones, use the transfer-pattern command in telephony-service
                              		  configuration mode. To disable these transfers, use the no form of this command.

transfer-pattern transfer-pattern [ blind ]

no transfer-pattern

### Syntax Description

transfer-pattern

String of digits for permitted call transfers. Wildcards
                                          						are allowed. A maximum of 32 transfer patterns can be entered, using a separate
                                          						command for each one.

blind

(Optional) When H.450.2 consultative call transfer is used,
                                          						this keyword forces transfers that match the pattern to be executed as blind
                                          						transfers. Overrides settings made using the transfer-system and transfer-mode commands.

### Command Default

Transfer of calls is enabled only to local Cisco IP phones.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco CME Version

Modification

12.1(5)YD

Cisco ITS 1.0

This command was introduced.

12.2(8)T

Cisco ITS 2.0

This command was integrated into Cisco IOS Release
                                          						12.2(8)T.

12.2(15)T

Cisco ITS 2.1

The blind keyword was added.

### Usage Guidelines

This command allows you to transfer calls to “other” phones—that is,
                              		  to non-IP phones and phones outside of your network. A call is then established
                              		  between the transferred party and the new recipient. By default, all Cisco IP
                              		  phone extension numbers are allowed as transfer targets.

The blind keyword is valid only for systems that
                              		  use Cisco IOS Telephony Services V2.1, Cisco CallManager Express 3.0, or a
                              		  later version and applies only to consultative transfers made using the H.450.2
                              		  standard. The blind keyword forces calls that are
                              		  transferred to numbers that match the transfer pattern to be executed as blind
                              		  or full-blind transfers, overriding any settings made using the transfer-system and transfer-mode commands.

When defining transfers to non-local numbers, it is important to note
                              		  that transfer-pattern digit matching is performed before translation-rule
                              		  operations. Therefore, you should specify in this command the digits actually
                              		  entered by phone users before they are translated.

Use of the .T control character for the transfer-pattern argument is not recommended. The .T control character indicates
                              		  a variable-length dial string, which causes Cisco CME to wait for an interdigit
                              		  timeout (default is 10 seconds) before transferring a call. To avoid the
                              		  interdigit timeout, a matching transfer pattern should be used with the transfer-pattern command. For example, use
                              		  the transfer-pattern 9......... command instead of the transfer-pattern .T command.

## Examples

The following example sets a transfer pattern. A maximum of 32
                              		  transfer patterns can be entered. In this example, 55501.. (the two periods are
                              		  wildcards) permits transfers to any number in the range from 555-0100 to
                              		  555-0199.

```
Router(config)# telephony-service Router(config-telephony)# transfer-pattern 55501..
```

### Related Commands

Description

transfer-mode

Specifies the type of call transfer for an individual IP
                                          						phone extension number that uses the ITU-T H.450.2 standard.

transfer-system

Specifies the call transfer method for all Cisco CME
                                          						extensions that use the ITU-T H.450.2 standard.

## transfer-pattern blocked

To block all call transfers for a specific Cisco Unified SIP IP phone
                              		  or a set of Cisco Unified SIP IP phone, use the transfer-pattern blocked command in voice register pool and voice
                              		  register template configuration mode. To allow call transfers, use the no form of this command.

transfer-pattern blocked

no transfer-pattern blocked

### Syntax Description

This command has no arguments or keywords.

### Command Default

Call transfers for a specific Cisco Unified SIP IP phone or a set of
                              		  Cisco Unified SIP IP phone are allowed.

### Command Modes

Voice register pool configuration (config-register-pool)

Voice register template configuration ((config-register-temp)

## Command History

Release

Modification

15.3(2)T

This command was introduced.

### Usage Guidelines

When the transfer-pattern blocked command is configured for a specific
                              		  phone, no call transfers are allowed from that phone over the trunk.

This feature forces unconditional blocking of all call transfers from
                              		  a specific phone to any other non-local numbers (external calls from one trunk
                              		  to another trunk). No call transfers from this specific phone are possible even
                              		  when a transfer pattern matches the dialed digits for transfer.

## Examples

The following example shows how to block all call transfers for voice
                              		  register pool 5:

```
Router(config)# voice register pool 5
Router(config-register-pool)# transfer-pattern ?
  blocked  global transfer pattern not allowed
Router(config-register-pool)# transfer-pattern blocked
```

The following example shows how to block all call transfers for a set
                              		  of Cisco Unified SIP IP phones defined by voice register template 9:

```
Router(config)# voice register template 9
Router(config-register-temp)# transfer-pattern ?
  blocked  global transfer pattern not allowed
Router(config-register-temp)# transfer-pattern blocked
```

### Related Commands

Command

Description

voice register pool

Enters voice register pool configuration mode and creates a
                                          						pool configuration for a Cisco Unified SIP IP phone in Cisco Unified CME or for
                                          						a set of Cisco Unified SIP IP phones in Cisco Unified SIP SRST.

voice register template

Enters voice register template configuration mode and
                                          						defines a template of common parameters for Cisco Unified SIP IP phones.

## transfer-system

To specify the
                              		  call transfer method to be used by Cisco Unified IP phones in Cisco Unified
                              		  CME, use the transfer-system command in telephony-service
                              		  configuration mode. To disable the call transfer method, use the no form of
                              		  this command.

transfer-system { blind | full-blind | full-consult [ dss ] | local-consult }

no transfer-system

### Syntax Description

blind

Transfers calls without consultation using a single phone line and the Cisco
                                          						proprietary method. This is the default for Cisco CME 3.4 and earlier versions.

full-blind

Transfers calls without consultation using H.450.2 standard methods.

full-consult

Transfers calls using H.450.2 with consultation using a second phone line, if
                                          						available. The calls fall back to full-blind if
                                          						a second line is not available. This is the default for Cisco Unified CME 4.0
                                          						and later versions.

dss

Transfers calls with consultation to idle monitor lines. All other
                                          						call-transfer behavior is identical to full-consult.

local-consult

Transfers calls with local consultation using a second phone line, if
                                          						available, or the calls fall back to blind if the target for consultation or
                                          						transfer is not local. This mode is intended for use primarily in Voice over
                                          						Frame Relay (VoFR) networks, because the Cisco VoFR call transfer protocol does
                                          						not support an end-to-end transfer-with-consultation mechanism. Not supported
                                          						if transfer-to destination is on the Cisco ATA, Cisco VG224, or a
                                          						SCCP-controlled FXS port.

### Command Default

For Cisco Unified
                              		  CME 4.0 and later versions, the transfer mode is full-consult .
                              		  For Cisco CME 3.4 and earlier versions, the transfer mode is blind .

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.2(11)YT

Cisco
                                          						ITS 2.1

This
                                          						command was introduced.

12.2(15)T

Cisco
                                          						ITS 2.1

This
                                          						command was integrated into Cisco IOS Release 12.2(15)T.

12.3(11)T

Cisco
                                          						CME 3.2

The dss keyword
                                          						was introduced.

12.4(4)XC

Cisco
                                          						Unified CME 4.0

The
                                          						command default was changed from blind to full-consult .

12.4(9)T

Cisco
                                          						Unified CME 4.0

This
                                          						command with the default of full-consult was integrated into Cisco IOS Release 12.4(9)T.

### Usage Guidelines

Direct station
                              		  select is a functionality that allows a multibutton phone user to transfer
                              		  calls to an idle monitor line by pressing the Transfer key and the appropriate
                              		  monitor button. The dss keyword
                              		  permits consultative call transfer to monitored lines.

Call transfers
                              		  can be blind or consultative. A blind transfer is one in which the transferring
                              		  extension connects the caller to a destination extension before ringback
                              		  begins. A consultative transfer is one in which the transferring party either
                              		  connects the caller to a ringing phone (ringback heard) or speaks with the
                              		  third party before connecting the caller to the third party.

The transfer-system command specifies whether the
                              		  H.450.2 standard or a Cisco proprietary method will be used to communicate call
                              		  transfer information across the network. When you specify use of the H.450.2
                              		  consultative or blind mode of transfer globally by using the transfer-system command (or by using the default),
                              		  you can override this mode for individual ephones by using the transfer-mode command. For example, in a system
                              		  that is set up for consultative transfer, a specific extension with an
                              		  auto-attendant that automatically transfers incoming calls to specific
                              		  extension numbers can be set to use blind transfer, because auto-attendants do
                              		  not use consultative transfer.

Prior to Cisco
                              		  Unified CME 4.0, the default for this command specified the Cisco proprietary
                              		  method. In Cisco Unified CME 4.0, the default was changed to specify the
                              		  H.450.2 standard as the transfer method. Check the following table for
                              		  configuration recommendations for different versions of Cisco Unified CME.

Cisco
                                          					 Product

transfer-system Default

transfer-system to Use

Transfer Method Recommendation

Cisco
                                          					 Unified CME 4.0 and later versions

full-consult

full-consult or full-blind

Use
                                          					 H.450.2 for call transfer. Because this is the default for this version, you do
                                          					 not need to use the transfer-system command unless you want to use the full-blind or dss keyword.

Optionally, you can use the proprietary Cisco method by using the transfer-system command with the blind or local-consult keyword.

Cisco
                                          					 CME 3.0 to 3.3

blind

full-consult or full-blind

Use
                                          					 H.450.2 for call transfer. You must explicitly configure the transfer-system command with the full-consult or full-blind keyword because H.450.2 is not the default for this version.

Optionally, you can use the proprietary Cisco method by using the transfer-system command with the blind or local-consult keyword.

Cisco
                                          					 ITS 2.1 to 3.0

blind

blind or local-consult

Use the
                                          					 Cisco proprietary method. Because this is the default for this version, you do
                                          					 not need to use the transfer-system command unless you want to use the local-consult keyword.

Optionally, you can use the H.450.2 standard for call transfer by using transfer-system command with the full-consult or full-blind keyword. You must also configure the router with a Tcl script that is contained
                                          					 in the file called app-h450-transfer.x.x.x.x.zip. This file is posted on the
                                          					 Cisco Unified CME software download website at http://www.cisco.com/cgi-bin/tablebuild.pl/ip-iostsp .

## Examples

The following
                              		  example sets full consultation as the call transfer method:

```
Router(config)# telephony-service Router(config-telephony)# transfer-system full-consult
```

### Related Commands

Description

transfer-mode

Specifies the type of call transfer for an individual IP phone extension that
                                          						uses the H.450.2 standard.

## translate
                        	 (ephone-dn)

To apply a
                              		  translation rule in order to manipulate the digits that are dialed by users of
                              		  Cisco Unified IP phones, use the translate command in ephone-dn or ephone-dn-template configuration mode. To disable the
                              		  translation rule, use the no form of
                              		  this command.

translate { called | calling } translation-rule-tag

no translate { called | calling }

### Syntax Description

called

Translate the called number.

calling

Translate the calling number.

translation - rule - tag

Unique
                                          						sequence number by which the rule set is referenced. This number is arbitrarily
                                          						chosen. Range is from 1 to 2147483647. There is no default value.

### Command Default

No translation
                              		  rule is applied.

### Command Modes

Ephone-dn configuration (config-ephone-dn) Ephone-dn-template configuration (config-ephone-template-dn)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.2(2)XT

Cisco
                                          						ITS 2.0

This
                                          						command was introduced.

12.2(8)T

Cisco
                                          						ITS 2.0

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T.

12.4(4)XC

Cisco
                                          						Unified CME 4.0

This
                                          						command was made available in ephone-dn-template configuration mode.

12.4(9)T

Cisco
                                          						Unified CME 4.0

This
                                          						command in ephone-dn-template configuration mode was integrated into Cisco IOS
                                          						Release 12.4(9)T.

### Usage Guidelines

This command
                              		  allows you to select a preconfigured translation rule to modify the number
                              		  dialed by a specific extension (Cisco Unified IP phone destination number, or
                              		  ephone-dn). A translation rule is a general-purpose digit-manipulation
                              		  mechanism that performs operations such as automatically adding telephone area
                              		  and prefix codes to dialed numbers. The translation rules are applied to the
                              		  voice ports created by the ephone-dn. The called keyword translates the called number, and the calling keyword translates the calling number.

The translation
                              		  rule mechanism inserts a delay into the dialing process when digits are entered
                              		  that do not explicitly match any of the defined translation rules. This delay
                              		  is set by the interdigit timeout. The translation-rule mechanism uses the delay
                              		  to ensure that it has acquired all of the digits from the phone user before
                              		  making a final decision that there is no translation-rule match available (and
                              		  therefore no translation operation to perform). To avoid this delay, it is
                              		  recommended that you include a dummy translation rule to act as a pass-through
                              		  rule for digit strings that do not require translation. For example, a rule
                              		  like “^5 5” that maps a leading 5 digit into a 5 would be used to prevent the
                              		  translation rule delay being applied to local extension numbers that started
                              		  with a 5.

If you use an
                              		  ephone-dn template to apply a command to an ephone-dn and you also use the same
                              		  command in ephone-dn configuration mode for the same ephone-dn, the value that
                              		  you set in ephone-dn configuration mode has priority.

## Examples

The following
                              		  example applies translation rule 20 to numbers called by extension 46839:

```
Router(config)# translation-rule 20 Router(config-translate)# rule 0 1234 2345 abbreviated Router(config-translate)# exit Router(config)# ephone-dn 1 Router(config-ephone-dn)# number 46839 Router(config-ephone-dn)# translate called 20
```

The following
                              		  example uses an ephone-dn-template to apply translation rule 20 to numbers
                              		  called by extension 46839:

```
Router(config)# translation-rule 20 Router(config-translate)# rule 0 1234 2345 abbreviated Router(config-translate)# exit Router(config)# ephone-dn-template 1 Router(config-ephone-dn-template)# translate called 20 Router(config-ephone-dn-template)# exit Router(config)# ephone-dn 1 Router(config-ephone-dn)# number 46839 Router(config-ephone-dn)# ephone-dn-template 1
```

### Related Commands

Description

rule

Defines a translation rule.

translation - rule

Creates a translation identifier and enters translation-rule configuration
                                          						mode.

## translate callback-number

To assign a translation profile for incoming or outgoing call legs on
                              		  a Cisco IP phone, use the translation-profile command in
                              		  call-manager-fallback configuration mode. To delete the translation profile
                              		  from the voice port, use the no form of this command.

translate callback-number

no translate callblack-number

### Syntax Description

incoming

Specifies that this translation profile handles incoming
                                          						calls.

outgoing

Specifies that this translation profile handles outgoing
                                          						calls.

name

Name of the translation profile.

### Command Default

No default behavior or values.

### Command Modes

Voice translation-profile configuration (cfg-translation-profile)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.1(3)T

Cisco Unified CME 8.5

This command was introduced.

### Usage Guidelines

Use the tranlsate callback-number command to translate a called
                              		  number to E.164 format. The translated number allows a called or calling number
                              		  to be presented in its local form. The translate callback-number command is
                              		  applied when translation-profile is configured on dialpeers, ephone-dn, and
                              		  voice register-dn. The translate callback-number command is effective when the
                              		  configruation setup reached the SCCP and SIP IP phones.

## Examples

The following example shows a configuration in which a translation
                              		  profile called name1 is created with two voice translation rules. Rule1
                              		  consists of associated calling numbers, and rule2 consists of redirected called
                              		  numbers. The Cisco IP phones in SRST mode are configured with name1.

```
voice translation-profile name1
 translation calling rule1
 translation called-direct rule2
call-manager-fallback
 translation-profile incoming name1
```

### Related Commands

Command

Description

show voice translation-profile

Displays the configuration of a translation profile.

translate (call-manager- fallback)

Applies a translation rule to modify the phone number
                                          						dialed or received by any Cisco IP phone user during CallManager fallback.

translation-rule

Creates a translation name and enters translation-rule
                                          						configuration mode to apply rules to the translation name.

voice translation-profile

Defines a translation profile for voice calls.

## translate-outgoing (voice register pool)

To allow an explicit setting of translation rules on the VoIP dial
                              		  peer in order to modify a phone number dialed by any Cisco IP phone user, use
                              		  the translate-outgoing command in voice register
                              		  pool configuration mode. To disable translation rules, use the no form of this command.

translate-outgoing { called | calling } rule-tag

no translate-outgoing { called | calling }

### Syntax Description

called

Called party requires translation.

calling

Calling party requires translation.

rule-tag

The rule-tag is an arbitrarily chosen number by which the
                                          						rule set is

referenced. The range is from 1 to 2147483.

### Command Default

Translation rules are enabled on the VoIP dial peer.

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

Translation rules are a powerful general-purpose number-manipulation
                              		  mechanism that perform operations such as automatically adding telephone area
                              		  and prefix codes to dialed numbers. The translation rules are applied to VoIP
                              		  dial peers created by Cisco Unified Session Initiation Protocol (SIP)
                              		  Survivable Remote Site Telephony (SRST) or Cisco Unified CallManager Express
                              		  (Cisco Unified CME).

During registration, a dial peer is created, and that dial peer
                              		  includes a default translation rule. The translate-outgoing command allows you to
                              		  change the translation rule, if desired. The translate-outgoing command allows you to
                              		  select a preconfigured number translation rule to modify the number dialed by a
                              		  specific extension.

Translation rules must be set by using the translate-outgoing command before the alias command is configured in Cisco Unified
                              		  SIP SRST.

Configure the id (voice register pool) command before any other voice register
                              		  pool commands, including the translate-outgoing command. The id command identifies a locally available individual SIP phone or
                              		  set of SIP phones.

## Examples

## Examples

The following is partial sample output from the show running-config command showing that called-party 1
                              		  requires translation.

```
voice register pool 1
 id mac 0030.94C2.A22A
 preference 5
 cor incoming call91 1 91011
 translate-outgoing called 1
```

## Examples

The following is partial sample output from the show running-config command showing that called-party 1 requires translation.

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

alias (voice register pool)

Allows Cisco SIP IP phones to handle inbound PSTN calls to
                                          						telephone numbers that are unavailable when the main proxy is not available.

id (voice register pool)

Explicitly identifies a locally available individual Cisco
                                          						SIP IP phone, or when running Cisco Unified SIP SRST, set of Cisco SIP IP
                                          						phones.

translate-outgoing (dial-peer)

Applies a translation rule to manipulate dialed digits on
                                          						an outbound POTS or VoIP call leg.

voice register pool

Enters voice register pool configuration mode for SIP
                                          						phones.

## translation-profile

To assign a translation profile for incoming or outgoing call legs on
                              		  a Cisco Unified IP phone, use the translation-profile command in ephone-dn or
                              		  ephone-dn-template configuration mode. To delete the translation profile from
                              		  the voice port, use the no form of this command.

translation-profile { incoming | outgoing } name

no translation-profile { incoming | outgoing } name

### Syntax Description

incoming

Specifies that this translation profile handles incoming
                                          						calls.

outgoing

Specifies that this translation profile handles outgoing
                                          						calls.

name

Name of the translation profile.

### Command Default

No default behavior or values

### Command Modes

Ephone-dn configuration (config-ephone-dn) Ephone-dn-template configuration (config-ephone-dn-template)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(11)T

Cisco CME 3.2

This command was introduced.

12.4(4)XC

Cisco Unified CME 4.0

This command was made available in ephone-dn-template
                                          						configuration mode.

12.4(9)T

Cisco Unified CME 4.0

This command in ephone-dn-template configuration mode was
                                          						integrated into Cisco IOS Release 12.4(9)T.

### Usage Guidelines

Use the translation-profile command to assign a global predefined translation profile to
                              		  an incoming or outgoing call leg.

If you use an ephone-dn template to apply a command to an ephone-dn
                              		  and you also use the same command in ephone-dn configuration mode for the same
                              		  ephone-dn, the value that you set in ephone-dn configuration mode has priority.

## Examples

The following example assigns the translation profile named call_in
                              		  to handle translation of incoming calls and a translation profile named
                              		  call_out to handle outgoing calls:

```
Router(config)# ephone-dn 1 Router(config-ephone-dn)# number 2555 Router(config-ephone-dn)# translation-profile incoming call_in Router(config-ephone-dn)# translation-profile outgoing call_out
```

The following example uses an ephone-dn-template to assign the
                              		  translation profile named call_in to handle translation of incoming calls and
                              		  the translation profile named call_out to handle outgoing calls:

```
Router(config)# ephone-dn-template 10 Router(config-ephone-dn-template)# translation-profile incoming call_in Router(config-ephone-dn-template)# translation-profile outgoing call_out Router(config-ephone-dn-template)# exit Router(config)# ephone-dn 1 Router(config-ephone-dn)# number 2555 Router(config-ephone-dn)# ephone-dn-template 10
```

### Related Commands

Description

s how voice translation-profile

Displays the configuration of a translation profile.

translate

Applies a translation rule to modify the phone number
                                          						dialed or received by any Cisco Unified IP phone user.

translation-rule

Creates a translation name and enters translation-rule
                                          						configuration mode.

voice translation-profile

Defines a translation profile for voice calls.

voice translation-rule

Defines a translation rule for voice calls.

## translation-profile incoming

To assign a translation profile for incoming call legs on a SIP
                              		  phone, use the translation-profile incoming command in voice-register-dn
                              		  configuration mode. To delete the translation profile from the directory
                              		  number, use the no form of this command.

translation-profile incoming name

no translation-profile incoming

### Syntax Description

name

Name of the translation profile to apply to incoming calls
                                          						to this directory number. This is the name argument that was created for
                                          						the profile with the voice translation-profile command.

### Command Default

No translation profile is assigned to the directory number.

### Command Modes

Voice register dn configuration (config-register-dn)

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

Use this command to assign a predefined translation profile to
                              		  incoming call legs on the specified directory number. The translation profile
                              		  that you assign is created by using the voice translation-profile command.

## Examples

The following example shows that the translation profile named
                              		  call_in is assigned to handle translation of incoming calls to directory number
                              		  1:

```
Router(config)# voice register dn 1 Router(config-register-dn)# number 2555 Router(config-register-dn)# translation-profile incoming call_in
```

### Related Commands

Description

s how voice translation-profile

Displays the configuration of a translation profile.

translate (translation profiles)

Associates a translation rule with a voice translation
                                          						profile.

voice translation-profile

Defines a translation profile for voice calls.

voice translation-rule

Defines a translation rule for voice calls.

## transport (voice
                        	 register pool-type)

To define the
                              		  default transport type supported by the new phone, use the transport command in voice register pool-type mode. To remove the description, use the no form of
                              		  this command.

## Syntax Description

(Optional) Selects UDP as
                                       					 the transport layer protocol. This is the default transport protocol.

(Optional) Selects TCP as
                                       					 the transport layer protocol.

### Command Default

The default
                              		  transport protocol is UDP. When the reference-pooltype command is configured,
                              		  the transport value of the reference phone is inherited.

### Command Modes

Voice Register Pool-Type Configuration (config-register-pooltype)

## Command History

15.3(3)M

Cisco SIP
                                       					 CME 10.0

This
                                       					 command was introduced.

### Usage Guidelines

Use this command
                              		  to define the default transport type. If this parameter is not configured, UDP
                              		  is used as default value. Currently, except the CiscoMobile-iOS and
                              		  Jabber-Android, all other phone types uses UDP as default transport type. The
                              		  default transport type will be ignored when the ‘session-transport {udp | tcp}’
                              		  command is configured for the pool.

## Examples

The following
                              		  example shows how to specify a description for a phone model using the
                              		  description command:

```
Router(config)# voice register pool-type 9900 Router(config-register-pool-type)# transport tcp
```

### Related Commands

Command

Description

Adds a new Cisco Unified SIP IP phone to Cisco Unified CME.

## trunk

To associate an ephone-dn with a foreign exchange office (FXO) port,
                              		  use the trunk command in ephone-dn configuration
                              		  mode. To disassociate the ephone-dn from the trunk number, use the no form of this command.

trunk digit-string [ timeout seconds ] [ transfer-timeout seconds ] [ monitor-port port ]

no trunk

### Syntax Description

digit-string

The number of the trunk line.

timeout seconds

(Optional) Interdigit timeout between dialed digits, in
                                          						seconds. Range is 3 to 30. Default is 3.

transfer-timeout seconds

(Optional) Number of seconds that Cisco Unified CME waits
                                          						for the transfer-to party to answer a call after which the call is recalled to
                                          						the phone that initiated the transfer. This keyword is supported for dual-line
                                          						ephone-dns only. Range is 5 to 60000. Default is disabled.

monitor-port port

(Optional) Enables a button lamp or icon that shows that
                                          						the specified port is in use. Port argument is
                                          						platform-dependent; type ? to display syntax.

### Command Default

Ephone-dns are not associated with FXO ports.

### Command Modes

Ephone-dn configuration (config-ephone)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(11)T

Cisco CME 3.2

This command was introduced.

12.4(4)XC

Cisco Unified CME 4.0

The monitor-port and transfer-timeout keywords were
                                          						added and support for dual-line ephone-dns was added.

12.4(9)T

Cisco Unified CME 4.0

This command with modifications was integrated into Cisco
                                          						IOS Release 12.4(9)T.

### Usage Guidelines

Use this command to configure ephone-dns to support FXO lines that
                              		  allow phones to have private lines connected directly to the PSTN. To bind the
                              		  ephone-dn to the FXO port, use the destination pattern configured for the FXO
                              		  line’s POTS dial peer for the digit-string argument.

The timeout seconds argument controls the
                              		  interdigit delay period, during which digits are collected from the user, and
                              		  the delay before the connection to the FXO port is established. The argument
                              		  controls the amount of time that Cisco Unified CME waits to collect digits for
                              		  the dialed number, so that the digits can be included in the redial buffer and
                              		  the Placed Calls directory of the phone. Digits that are entered after the
                              		  timeout period are not included in the redial buffer or in the Placed Calls
                              		  directory on the phone. The timeout parameter does not affect the time used to
                              		  cut through the connection from the phone’s trunk button to the FXO port. The
                              		  phone user must either enter the pound (#) key or wait for this interdigit
                              		  timeout to complete digit collection.

The phone user also has the option to use the phone’s on-hook dialing
                              		  feature so that the phone itself performs complete dial-string digit collection
                              		  before signaling off-hook to the Cisco Unified CME. In this case all digits
                              		  will be included in the Redial and Placed Calls Directory.

The monitor-port keyword enables direct status
                              		  monitoring of the FXO port on the line button of the IP phone. The line button
                              		  indicator, either a lamp or an icon depending on the phone, shows the in-use
                              		  status of the FXO port during the duration of the call.

The transfer-timeout argument enables a
                              		  transferred call to be automatically recalled if the transfer target does not
                              		  answer after the specified number of seconds. The call is withdrawn from the
                              		  transfer-to phone and the call resumes ringing on the phone that initiated the
                              		  transfer.

The monitor-port and transfer-timeout keywords are not supported
                              		  on ephone-dns for analog ports on the Cisco VG 224.

For dual-line ephone-dns, the second channel cannot receive incoming
                              		  calls when the trunk command is configured.

## Examples

The following example shows the configuration for two phones that
                              		  each have a private FXO line button and a shared-line button.

The shared line’s voice ports and dial peers are as follows:

```
Router(config)# voice-port 1/0/1 Router(config-voice-port)# connection plar-opx 1000 Router(config)# dial-peer voice 101 pots Router(config-dial-peer)# destination-pattern 9 Router(config-dial-peer)# port 1/0/1 The private lines’ voice ports and dial peers are as follows:
Router(config)# voice-port 1/1/0 Router(config-voice-port)# connection plar-opx 5550111 Router(config)# dial-peer voice 110 pots Router(config-dial-peer)# destination-pattern 80 Router(config-dial-peer)# port 1/1/0 Router(config)# voice-port 1/1/1 Router(config-voice-port)# connection plar-opx 5550112 Router(config)# dial-peer voice 111 pots Router(config-dial-peer)# destination-pattern 81 Router(config-dial-peer)# port 1/1/1 The following is the configuration for the shared and private ephone-dns:
Router(config)# ephone-dn 1 Router(config-ephone-dn)# number 1000 Router(config-ephone-dn)# name Line1 Router(config-ephone-dn)# no huntstop Router(config)# ephone-dn 2 Router(config-ephone-dn)# number 5550111 Router(config-ephone-dn)# name Private line Router(config-ephone-dn)# trunk 80 Router(config)# ephone-dn 3 Router(config-ephone-dn)# number 5550112 Router(config-ephone-dn)# name Private line Router(config-ephone-dn)# trunk 81
```

The following is the configuration for ephones with button 1 as a
                              		  shared line and button 2 a private line:

```
Router(config)# ephone 1 Router(config-ephone)# mac-address 1111.1111.1101 Router(config-ephone)# button 1:1 2:2 Router(config)# ephone 2 Router(config-ephone)# mac-address 1111.1111.1102 Router(config-ephone)# button 1:1 2:3
```

The following example shows that transferred calls are recalled after
                              		  30 seconds if the destination party does not answer and status monitoring is
                              		  enabled for FXO port 1/1/1.

```
Router(config)# ephone-dn 5 Router(config-ephone-dn)# trunk 801 timeout 5 transfer-timeout 30 monitor-port 1/1/1
```

### Related Commands

Description

destination-number

Specifies a connection mode for a voice port.

## trustpoint (credentials)

To specify the name of the trustpoint to be associated with a Cisco
                              		  Unified CME CTL provider certificate or with the Cisco Unified SRST router
                              		  certificate, use the trustpoint command in credentials
                              		  configuration mode. To change the specified trustpoint, use the no form of this command.

trustpoint trustpoint-name

no trustpoint

### Syntax Description

trustpoint-name

Name of the trustpoint to be associated with the Cisco
                                          						Unified CME CTL provider certificate or the Cisco Unified SRST device
                                          						certificate.

### Command Default

No default behavior or values.

### Command Modes

Credentials configuration (config-credentials)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(14)T

Cisco SRST 3.3

This command was introduced for Cisco SRST.

12.4(4)XC

Cisco Unified CME 4.0

This command was introduced for Cisco Unified CME.

12.4(9)T

Cisco Unified CME 4.0

This command for Cisco Unified CME was integrated into
                                          						Cisco IOS Release 12.4(9)T.

### Usage Guidelines

Cisco Unified CME

This command is used with Cisco Unified CME phone authentication to
                              		  define the trustpoint for the CTL provider. This trustpoint will be used for
                              		  TLS sessions with the CTL client.

Cisco Unified SRST

The name of the trustpoint must be consistent with the trustpoint
                              		  name of the Cisco Unified SRST router.

## Examples

## Examples

The following example sets up a CTL provider on the Cisco Unified CME
                              		  router with the IP address 172.19.245.1.

```
Router(config)# credentials Router(config-credentials)# ip source-address 172.19.245.1 port 2444 Router(config-credentials)# trustpoint ctlpv Router(config-credentials)# ctl-service admin user4 secret 0 c89L8o
```

## Examples

The following example enters credentials configuration mode, sets the
                              		  IP source address and port, and specifies the trustpoint:

```
Router(config)# credentials Router(config-credentials)# ip source-address 10.6.21.4 port 2445 Router(config-credentials)# trustpoint srstca
```

### Related Commands

Description

ctl-service admin

Specifies a user name and password to authenticate the CTL
                                          						client during the CTL protocol.

debug credentials

Sets debugging on the credentials service.

ip source-address (credentials)

Enables the router to receive messages through the
                                          						specified IP address and port.

show credentials

Displays the credentials settings.

## trustpoint-label

To specify the PKI trustpoint label to be used for the TLS connection
                              		  between the CAPF server and the phone, use the trustpoint-label command in CAPF-server
                              		  configuration mode. To return to the default, use the no form of this command.

trustpoint-label label

no trustpoint-label

### Syntax Description

label

Trustpoint name for the CAPF server.

### Command Default

No trustpoint label is specified for TLS connections.

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

This command is used with Cisco Unified CME phone authentication to
                              		  provide a PKI trustpoint name for the CAPF server. This trustpoint label is
                              		  used for the TLS connection between the CAPF server and the phone.

## Examples

The following example defines the CAPF server trustpoint name as
                              		  server25.

```
Router(config)# capf-server Router(config-capf-server)# source address 10.10.10.1 Router(config-capf-server)# trustpoint-label server25 Router(config-capf-server)# cert-oper upgrade all Router(config-capf-server)# cert-enroll-trustpoint server12 password 0 x8oWiet Router(config-capf-server)# auth-mode auth-string Router(config-capf-server)# auth-string generate all Router(config-capf-server)# port 3000 Router(config-capf-server)# keygen-retry 5 Router(config-capf-server)# keygen-timeout 45 Router(config-capf-server)# phone-key-size 2048
```

## type

To assign a phone
                              		  type to an SCCP phone, use the type command
                              		  in ephone or ephone-template configuration mode. To remove a phone type, use
                              		  the no form of
                              		  this command.

type phone-type [ addon 1 module-type [ 2 module-type ]]

no type phone-type [ addon 1 module-type [ 2 module-type ]]

### Syntax Description

phone-type

Type of
                                          						phone. The following phone types are predefined in the system:

- 12SP —12SP+ and 30VIP phones.

- 6901—Cisco Unified IP
                                             						  Phone 6901.

- 6911—Cisco Unified IP
                                             						  Phone 6911.

- 6921— Cisco Unified IP
                                             						  Phone 6921.

- 6941—Cisco Unified IP
                                             						  Phone 6941.

- 6945 —Cisco Unified IP Phone 6945.

- 6961—Cisco Unified IP
                                             						  Phone 6961.

- 7902 —Cisco Unified IP Phone 7902G.

- 7905 —Cisco Unified IP Phone 7905G.

- 7906 —Cisco
                                             						  Unified IP Phone 7906.

- 7910 —Cisco Unified IP Phones 7910 and 7910G.

- 7911 —Cisco Unified IP Phone 7911G.

- 7912 —Cisco
                                             						  Unified IP Phone 7912G.

- 7920 —Cisco
                                             						  Unified IP Phone 7920.

- 7921 —Cisco
                                             						  Unified Wireless IP Phone 7921.

- 7925 —Cisco
                                             						  Unified Wireless IP Phone 7925.

- 7931 —Cisco
                                             						  Unified IP Phone 7931G.

- 7935 —Cisco
                                             						  Unified IP Conference Station 7935.

- 7936 —Cisco
                                             						  Unified IP Conference Station 7936.

- 7937 —Cisco
                                             						  Unified IP Conference Station 7937.

- 7940 —Cisco
                                             						  Unified IP Phone 7940G.

- 7941 —Cisco
                                             						  Unified IP Phone 7941G.

- 7941GE —Cisco
                                             						  Unified IP Phone 7941G-GE.

- 7942 —Cisco
                                             						  Unified IP Phone 7942.

- 7945 —Cisco
                                             						  Unified IP Phone 7945

- 7960 —Cisco
                                             						  Unified IP Phone 7960G.

- 7961 —Cisco
                                             						  Unified IP Phone 7961G.

- 7961GE —Cisco
                                             						  Unified IP Phone 7961G-GE.

- 7962 —Cisco
                                             						  Unified IP Phone 7962.

- 7965 —Cisco
                                             						  Unified IP Phone 7965.

- 7970 — Cisco Unified IP Phone 7970G.

- 7971 —Cisco
                                             						  Unified IP Phone 7971G-GE.

- 7975 —Cisco
                                             						  Unified IP Phone 7975.

- 7985 —Cisco
                                             						  Unified IP Phone 7985.

- 8941 —Cisco
                                             						  Unified IP Phone 8941.

- 8945 —Cisco
                                             						  Unified IP Phone 8945.

- 8961 —Cisco
                                             						  Unified IP Phone 8961.

- 9951 —Cisco
                                             						  Unified IP Phone 9951.

- 9971 —Cisco
                                             						  Unified IP Phone 9971.

- anl —Analog.

- ata —Cisco
                                             						  ATA-186 or Cisco ATA-188.

- bri —SCCP
                                             						  Gateway (BR).

- vgc-phone —VG248 phone emulation for analog phone.

addon 1 module-type

(Optional) Tells the router that an expansion module is being added to this
                                          						Cisco Unified IP Phone and the type of module. Valid entries for module-type are:

- 7914 —Cisco
                                             						  Unified IP Phone 7914 Expansion Module.

- 7915-12 —Cisco Unified IP Phone 7915 12-Button
                                             						  Expansion Module.

- 7915-24 —Cisco Unified IP Phone 7915 24-Button
                                             						  Expansion Module.

- 7916-12 —Cisco Unified IP Phone 7916 12-Button
                                             						  Expansion Module.

- 7916-24 —Cisco Unified IP Phone 7916 24-Button
                                             						  Expansion Module.

2 module-type

(Optional) Tells the router that a second expansion module is being added to
                                          						this Cisco Unified IP Phone and the type of module. Valid entries for module-type are:

- 7914 —Cisco
                                             						  Unified IP Phone 7914 Expansion Module.

- 7915-12 —Cisco Unified IP Phone 7915 12-Button
                                             						  Expansion Module.

- 7915-24 —Cisco Unified IP Phone 7915 24-Button
                                             						  Expansion Module.

- 7916-12 —Cisco Unified IP Phone 7916 12-Button
                                             						  Expansion Module.

- 7916-24 —Cisco Unified IP Phone 7916 24-Button
                                             						  Expansion Module.

### Command Default

No phone type
                              		  or add-on expansion module is defined.

### Command Modes

Ephone configuration (config-ephone) Ephone-template configuration (config-ephone-template)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.2(11)YT

Cisco
                                          						ITS 2.1

This
                                          						command was introduced.

12.2(15)T

Cisco
                                          						ITS 2.1

This
                                          						command was integrated into Cisco IOS Release 12.2(15)T.

12.2(15)ZJ

Cisco
                                          						CME 3.0

The
                                          						following keywords were added to this command: 7902 , 7905 , and 7912 .

12.3(4)T

Cisco
                                          						CME 3.0

This
                                          						command was integrated into Cisco IOS Release 12.3(4)T.

12.3(7)T

Cisco
                                          						CME 3.1

The 7920 and 7936 keywords were added.

12.3(11)XL

Cisco
                                          						CME 3.2(1)

The 7970 keyword was added.

12.3(14)T

Cisco
                                          						CME 3.3

The 7971 keyword was added, and this command was integrated into Cisco IOS Release
                                          						12.3(14)T.

12.4(4)XC

Cisco
                                          						Unified CME 4.0

The 7911 , 7941 , 7941GE , 7961 , and 7961GE keywords were added. This command was made available in ephone-template
                                          						configuration mode.

12.4(9)T

Cisco
                                          						Unified CME 4.0

This
                                          						command was integrated into Cisco IOS Release 12.4(9)T.

12.4(6)XE

Cisco
                                          						Unified CME 4.0(2)

The 7931 keyword was added.

12.4(4)XC4

Cisco
                                          						Unified CME 4.0(3)

The 7931 keyword was added.

12.4(11)T

Cisco
                                          						Unified CME 4.0(3)

This
                                          						command was integrated into Cisco IOS Release 12.4(11)T.

12.4(11)XJ2

Cisco
                                          						Unified CME 4.1

The 7921 and 7985 keywords were introduced.

12.4(15)T

Cisco
                                          						Unified CME 4.1

This
                                          						command was integrated into Cisco IOS Release 12.4(15)T.

12.4(15)T1

Cisco
                                          						Unified CME 4.1(1)

The 7942 , 7945 , 7962 , 7965 , and 7975 keywords were introduced.

12.4(15)XZ

Cisco
                                          						Unified CME 4.3

Support for user-defined phone types created with the ephone-type command was added.

12.4(15)XZ1

Cisco
                                          						Unified CME 4.3

The 7915-12 , 7915-24 , 7916-12 , 7916-24 ,
                                          						and 7937 keywords were added.

12.4(20)T

Cisco
                                          						Unified CME 7.0

The 7915-12 , 7915-24 , 7916-12 , 7916-24 ,
                                          						and 7937 keywords were added and this command was integrated
                                          						into Cisco IOS Release 12.4(20)T.

12.4(20)T1

Cisco
                                          						Unified CME 7.0

The 7925 keyword was added.

15.0(1)XA

Cisco
                                          						Unified CME 8.0

This
                                          						command was modified. The 6921, 6941, 6961, and IP-STE keywords were added.

15.1(1)T

Cisco
                                          						Unified CME 8.0

This
                                          						command was integrated into Cisco IOS Release 15.1(1)T.

15.1(2)T

Cisco
                                          						Unified CME 8.1

This
                                          						command was modified. The 6901 and 6911 keywords were added.

15.2(1)T

Cisco
                                          						Unified CME 8.8

This
                                          						command was modified. The 6945 , 8941 , and 8945 keywords were added.

15.3(3)M

Cisco
                                          						Unified CME 10.0

This
                                          						command was modified. The 7906 , 8961 , 9951 , and 9971 keywords were added.

### Usage Guidelines

Not all phone
                              		  types support add-on expansion modules. For support information, see User
                              		  Documentation for Cisco Unified IP Phones.

This command
                              		  must be followed by a phone reboot using the reset command.

If you use an
                              		  ephone template to apply a command to a phone and you also use the same command
                              		  in ephone configuration mode for the same phone, the value that you set in
                              		  ephone configuration mode has priority.

## Examples

The following
                              		  example defines the IP phone with phone-tag 10 as a Cisco Unified IP Phone
                              		  7960G with two attached Cisco Unified IP Phone 7914 Expansion Modules:

```
Router(config)# ephone 10 Router(config-ephone)# type 7960 addon 1 7914 2 7914
```

The following
                              		  example defines the IP phone with phone-tag 4 as a Cisco ATA device:

```
Router(config)# ephone 4 Router(config-ephone)# mac 1234.87655.234 Router(config-ephone)# type ata
```

The following
                              		  example defines the IP phone with phone-tag 10 as a Cisco Unified IP Phone
                              		  IP-STE:

```
Router(config)# ephone 10 Router(config-ephone)# type IPSTE
```

### Related Commands

Command

Description

ephone-type

Adds
                                          						a Cisco Unified IP phone type by defining a phone-type template.

reset (ephone)

Performs a complete reboot of one phone associated with a Cisco Unified CME
                                          						router.

reset (telephony-service)

Performs a complete reboot of one or all phones associated with a Cisco Unified
                                          						CME router.

## type (voice register dialplan)

To specify a phone type for a SIP dial plan, use the type command in voice register dialplan
                              		  configuration mode. To remove a phone type, use the no form of this command.

type phone-type

no type

### Syntax Description

phone-type

Type of SIP phone for which the dial plan is used. Values
                                          						are:

- 7905-7912 —Cisco Unified IP
                                             						  Phone 7905, 7905G, 7912, or 7912G.

- 7940-7960-others —Cisco Unified
                                             						  IP Phone 7911, 7940, 7940G, 7941, 7942, 7941GE, 7945, 7960, 7960G, 7961,
                                             						  7961GE, 7962, 7965, 7970, 7971, or 7975.

### Command Default

The phone type is not defined.

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

12.4(15)XZ

Cisco Unified CME 4.3

Support for Cisco Unified IP Phone 7942, 7945, 7962, 7965,
                                          						and 7975 was added.

12.4(20)T

Cisco Unified CME 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

This command specifies the type of SIP phone for which the dial plan
                              		  is defined. You must use this command before defining dial patterns with the pattern command or selecting a dial pattern
                              		  file in flash with the filename command.

The phone type specified with this command must match the phone type
                              		  specified with the type command in voice register pool mode. If
                              		  the dial plan type does not match the type assigned to the phone, the dial-plan
                              		  configuration file is not generated.

## Examples

The following example shows a SIP dial plan being defined for a Cisco
                              		  Unified IP Phone 7905 or Cisco Unified IP Phone 7912:

```
Router(config)# voice register dialplan 10 Router(config-register-dialplan)# type 7905-7912 Router(config-register-dialplan)# pattern 52... Router(config-register-dialplan)# pattern 91.......
```

### Related Commands

Command

Description

dialplan

Assigns a dial plan to a SIP phone.

filename

Specifies a custom XML file that contains the dial patterns
                                          						to use for the SIP dial plan.

pattern (voice register dialplan)

Defines a dial pattern for a SIP dial plan.

show voice register dialplan

Displays configuration information for a specific SIP dial
                                          						plan.

type (voice register pool)

Defines a phone type for a SIP phone.

## type (voice
                        	 register pool)

To define a phone
                              		  type for a SIP phone, use the type command
                              		  in voice register pool configuration mode. To remove a phone type, use the no form of
                              		  this command.

type phone-type [ addon 1 CKEM | CP-8800-Audio | CP-8800-Video [ 2 CKEM | CP-8800-Audio | CP-8800-Video [ 3 CKEM | CP-8800-Audio | CP-8800-Video ]]]

no type

### Syntax Description

phone-type

Type of
                                          						SIP phone that is being defined. Valid entries are as follows:

- 3905 —Cisco Unified IP Phone 3905.

- 3951 —Cisco Unified IP Phones 3911 and 3951.

- 6901 —Cisco Unified IP Phone 6901.

- 6911 —Cisco Unified IP Phone 6911.

- 6921 —Cisco Unified IP Phone 6921.

- 6922 —Cisco
                                             						  Unified IP Phone 6922.

- 6941 —Cisco Unified IP Phone 6941.

- 6945 —Cisco Unified IP Phone 6945.

- 6961 —Cisco Unified IP Phone 6961.

- 7821 —Cisco
                                             						  Unified IP Phones 7821.

- 7841 —Cisco Unified IP Phones 7841.

- 7861 —Cisco
                                             						  Unified IP Phones 7861.

- 7905 —Cisco
                                             						  Unified IP Phones 7905 and 7905G.

- 7906 —Cisco Unified IP Phone 7906G.

- 7911 —Cisco Unified IP Phone 7911G.

- 7912 —Cisco IP Phones 7912 and 7912G.

- 7940 —Cisco IP
                                             						  Phones 7940 and 7940G.

- 7941 —Cisco IP
                                             						  Phone 7941G.

- 7941GE —Cisco
                                             						  IP Phone 7941GE.

- 7942 —Cisco
                                             						  Unified IP Phone 7942.

- 7945 —Cisco
                                             						  Unified IP Phone 7945.

- 7960 —Cisco IP
                                             						  Phones 7960 and 7960G.

- 7961 —Cisco IP
                                             						  Phone 7961G.

- 7961GE —Cisco
                                             						  IP Phone 7961GE.

- 7962 —Cisco
                                             						  Unified IP Phone 7962.

- 7965 —Cisco
                                             						  Unified IP Phone 7965.

- 7970 —Cisco IP
                                             						  Phone 7970G.

- 7971 —Cisco IP
                                             						  Phone 7971GE.

- 7975 —Cisco
                                             						  Unified IP Phone 7975.

- 8851 —Cisco Unified IP Phone 8851.

- 8851NR —Cisco Unified IP Phone 8851NR.

- 8861 —Cisco Unified IP Phone 8861.

- 8865 —Cisco  IP Phone 8865.

- 8961 —Cisco
                                             						  Unified IP Phone 8961.

- 9900 —Cisco
                                             						  Unified IP Phone 9900.

- 9951 —Cisco
                                             						  Unified IP Phone 9951.

- 9971 —Cisco
                                             						  Unified IP Phone 9971.

- ATA —Cisco
                                             						  ATA-186 or Cisco ATA-188.

- ATA-187 —Cisco
                                             						  ATA-187.

- ATA-190 —Cisco ATA-190.

- ATA-191 —Cisco ATA-191.

- DX650 —Cisco
                                             						  DX650.

- Jabber-Android —Cisco Jabber App on Android.

- P100 —PingTel
                                             						  Xpressa 100.

- P600 —Polycom
                                             						  SoundPoint 600.

- Jabber-CSF-Client —Cisco
                                             						  Jabber CSF Client.

addon 1 CKEM

(Optional) Tells the router that a Cisco SIP IP Phone CKEM 36-Button Line
                                          						Expansion Module is being added to this Cisco Unified SIP IP phone.

2 CKEM

(Optional) Tells the router that a second Cisco SIP IP Phone CKEM 36-Button
                                          						Line Expansion Module is being added to this Cisco Unified SIP IP phone.

3 CKEM

(Optional) Tells the router that a third Cisco SIP IP Phone CKEM 36-Button Line
                                          						Expansion Module is being added to this Cisco Unified SIP IP phone.

addon 1 CP-8800-Audio or addon 1 CP-8800-Video

(Optional) Tells the router that a Cisco SIP IP Phone 28-Button Line A-KEM or V-KEM is being added to this Cisco Unified SIP
                                          IP Phone.

2 CP-8800-Audio or 2 CP-8800-Video

(Optional) Tells the router that a second Cisco SIP IP Phone A-KEM or V-KEM is being added to this Cisco Unified SIP IP Phone.

2 CP-8800-Audio or 2 CP-8800-Video

(Optional) Tells the router that a second Cisco SIP IP Phone A-KEM or V-KEM is being added to this Cisco Unified SIP IP Phone.

### Command Default

No phone type
                              		  is defined.

### Command Modes

Voice register pool configuration (config-register-pool)

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

This
                                          						command was modified to add the 3951 , 7911 , 7941 , 7941GE , 7961 , 7961GE , 7970 , and 7971 keywords.

12.4(15)T

Cisco
                                          						Unified CME 4.1

The 3951 , 7911 , 7941 , 7941GE , 7961 , 7961GE , 7970 , and 7971 keywords were integrated into Cisco IOS Release 12.4(15)T.

12.4(15)XZ

Cisco
                                          						Unified CME 4.3

This
                                          						command was modified to add the 7942 , 7945 , 7962 , 7965 , and 7975 keywords.

12.4(20)T

Cisco
                                          						Unified CME 7.0

This
                                          						command was integrated into Cisco IOS Release 12.4(20)T.

15.1(3)T

Cisco
                                          						Unified CME8.5

This
                                          						command was modified to add the 8961 , 9951 ,and 9971 keywords.

15.2(1)T

Cisco
                                          						Unified CME 8.8

This
                                          						command was modified to add the 3905 keyword.

15.2(2)T

Cisco
                                          						Unified CME 9.0

This
                                          						command was modified to add the 6901 , 6911 , 6921 , 6941 , 6945 , 6961 , ATA-187 ,
                                          						and Jabber-Android keywords.

15.2(4)M

Cisco
                                          						Unified CME 9.1

This
                                          						command was modified to include the addon 1 CKEM , 2 CKEM , and 3 CKEM keywords.

15.3(3)M

Cisco
                                          						Unified CME 10.0

This
                                          						command was modified to add the 6922 and 9900 keywords.

15.4(3)M

Cisco
                                          						Unified CME 10.5

This
                                          						command was modified. The 78XX , DX650 and Jabber-CSF-Client keywords were
                                          						added.

Cisco IOS XE Gibraltar 16.10.1a Release

Unified CME 12.5

This command was modified. The ATA-191 , CP-8800-Audio , and CP-8800-Video keywords were added.

### Usage Guidelines

The addon 1 CKEM , 2 CKEM , and 3 CKEM keywords increase the number of speed-dial,
                              		  busy-lamp-field, and directory number keys that can be configured.

There are two
                              		  options in removing a Key Expansion Module (KEM) when you have configured all
                              		  three KEMs.

The first
                              		  option is to use the no form of
                              		  the type command, then use the type command to configure only the KEMs to be included. The following example shows
                              		  how the second and third KEMs are removed from the configuration:

```
Router(config)# voice register pool 9 Router(config-register-pool)# type 9971 addon 1 CKEM 2 CKEM 3 CKEM Router(config-register-pool)# no type 9971 addon 1 CKEM 2 CKEM 3 CKEM Router(config-register-pool)# type 9971 addon 1 CKEM
```

The second
                              		  option is to define the same phone type while excluding from the configuration
                              		  the KEM to be removed. For example, you have configured the following:

```
Router(config)# voice register pool 3 Router(config-register-pool)# type 9971 addon 1 CKEM 2 CKEM 3 CKEM
```

To remove the
                              		  third KEM, enter the following:

Router(config-register-pool)# type 9971 addon 1 CKEM 2 CKEM

To remove the
                              		  second KEM, enter the following:

```
Router(config-register-pool)# type 9971 addon 1 CKEM
```

From Unfiied CME 12.5 Release, type phone-type [ addon 1 CKEM | CP-8800-Audio | CP-8800-Video [ 2 CKEM | CP-8800-Audio | CP-8800-Video [ 3 CKEM | CP-8800-Audio | CP-8800-Video ] ] ] configuration is supported. The phone support is extended to Cisco IP Phone 8865 to support the Video KEM CP-8800-Video . Audio KEM CP-8800-Audio support is introduced for the Cisco IP Phone models 8851, 8851 NR, and 8861.

All the configuration characteristics of CKEM discussed here is applicable to CP-8800-Audio and CP-8800-Video .

After
                              		  configuring the phone type, use the create profile command in voice register global
                              		  configuration mode to generate the configuration profile files required for the
                              		  phone and then reset or restart the phone using the reset or restart command, respectively.

## Examples

The following
                              		  example shows how to define a SIP phone with phone-tag 10 as a Cisco Unified IP
                              		  Phone 7960 or Cisco Unified IP Phone 7960G:

```
Router(config)# voice register pool 10 Router(config-register-pool)# type 7960
```

The following is a sample configuration for CP-8800-Audio and CP-8800-Video on the supported phone models for Unified CME 12.5 Release.

```
Router(config-register-pool)# type 8851 addon 1 CP-8800-Audio 2 CP-8800-Audio
Router(config-register-pool)# type 8851NR addon 1 CP-8800-Audio 2 CP-8800-Audio
Router(config-register-pool)# type 8861 addon 1 CP-8800-Audio 2 CP-8800-Audio 3 CP-8800-Audio
Router(config-register-pool)# type 8865 addon 1 CP-8800-Video 2 CP-8800-Video 3 CP-8800-Video
```

### Related Commands

Command

Description

busy-trigger-per-button (voice register pool)

Sets
                                          						the maximum number of calls allowed on a SIP directory number before activating
                                          						Call Forward Busy or a busy tone.

load (voice register global)

Associates a type of Cisco Unified SIP IP phone with a phone firmware file.

reset (voice register global)

Performs a complete reboot of all SIP phones associated with a Cisco Unified
                                          						CME router.

reset (voice register pool)

Performs a complete reboot of one SIP phone associated with a Cisco Unified CME
                                          						router.

restart (voice register)

Performs a fast reset of one or all SIP phones associated with a Cisco Unified
                                          						CME router.

voice register pool

Enters voice register pool configuration mode for SIP phones.

## type (voice-gateway)

To define the type of voice gateway to autoconfigure, use the type command in voice-gateway configuration
                              		  mode. To remove the type from the configuration, use the no form of this command.

type { vg202 | vg204 | vg224 }

no type

### Syntax Description

vg202

Cisco VG202 Voice Gateway with 2 FXS ports.

vg204

Cisco VG204 Voice Gateway with 4 FXS ports.

vg224

Cisco VG224 Voice Gateway with 24 FXS ports.

### Command Default

No type is defined for the voice gateway to be autoconfigured.

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

This command specifies the type of Cisco voice gateway for which you
                              		  are creating an XML configuration file.

## Examples

The following example shows a configuration for the Cisco VG224 voice
                              		  gateway:

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

create cnf-files (voice-gateway)

Generates the XML configuration files that are required to
                                          						autoconfigure the Cisco voice gateway.

mac-address (voice-gateway)

Defines the MAC address of the voice gateway to
                                          						autoconfigure.

voice-port (voice-gateway)

Identifies the ports on the voice gateway that register to
                                          						Cisco Unified CME.

| setup | (Optional) Interactive setup tool for configuring Cisco Unified IP Phone 7910s,
                                          						7940s, and 7960s in Cisco Unified CME. Note This
                                                   						interactive Cisco CME setup tool is restricted to generating basic
                                                   						configuration files for Cisco Unified IP Phone 7910s, 7940s, and 7960s running
                                                   						SCCP protocol only. | Note | This
                                                   						interactive Cisco CME setup tool is restricted to generating basic
                                                   						configuration files for Cisco Unified IP Phone 7910s, 7940s, and 7960s running
                                                   						SCCP protocol only. |
|---|---|---|---|
| Note | This
                                                   						interactive Cisco CME setup tool is restricted to generating basic
                                                   						configuration files for Cisco Unified IP Phone 7910s, 7940s, and 7960s running
                                                   						SCCP protocol only. |

| Note | This
                                                   						interactive Cisco CME setup tool is restricted to generating basic
                                                   						configuration files for Cisco Unified IP Phone 7910s, 7940s, and 7960s running
                                                   						SCCP protocol only. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco
                                          						ITS 1.0 | This
                                          						command was introduced. |
| 12.2(8)T | Cisco
                                          						ITS 2.0 | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T. |
| 12.2(15)ZJ | Cisco
                                          						CME 3.0 | The setup keyword
                                          						was added. |
| 12.3(4)T | Cisco
                                          						CME 3.0 | This
                                          						command was integrated into Cisco IOS Release 12.3(4)T. |

| Note | The
                                       		  voice-gateway system is tied to the telephony service. The telephony-service command must be configured
                                       		  before the voice-gateway system is configured; otherwise, the voice gateway is
                                       		  hidden from the user. |
|---|---|

| Cisco CME
                                          					 Setup Tool Prompt | Description |
|---|---|
| Do you want to setup DHCP service for your IP phones? [yes/no]: If you
                                          					 respond yes, you see the following prompts: IP network for telephony-service DHCP  Pool:
Subnet mask for DHCP network : 
TFTP Server IP address (Option 150) :
Default Router for DHCP Pool : | Yes—Configures the Cisco Unified CME router to act as a Dynamic Host
                                             						Configuration Protocol (DHCP) server, automatically providing IP addresses to
                                             						your IP phones and provisioning the default gateway and TFTP IP addresses to be
                                             						used by the phones. This method creates a single pool of IP addresses. If you
                                             						need a pool for non-IP phones or if the Cisco router cannot act as the DHCP
                                             						router, answer no and manually define the DHCP server. No—Indicates that you have already configured DHCP or static IP addresses for
                                             						the IP phones. |
| Do you want to start telephony-service setup? [yes/no]: | Yes— Starts
                                             						the interactive setup tool for configuring Cisco Unified IP Phone 7910s, 7940s,
                                             						and 7960s. No —Terminates the Cisco CME setup tool. |
| Enter the IP source address for Cisco CallManager Express:
Enter the Skinny Port for Cisco CallManager Express:  [2000]: | IP
                                          					 address on which the router provides Cisco Unified CME services, usually the
                                          					 default gateway for the IP subnet that you are using for the IP phones, and the
                                          					 port for Skinny Client Control Protocol (SCCP) messages. |
| How many IP phones do you want to configure : [0]: | Enter
                                          					 the maximum number of IP phones that this Cisco Unified CME system will
                                          					 support. This number can be increased later, to the maximum allowed for this
                                          					 version and your router. Note The
                                                   					 Cisco CME setup tool associates one number with each newly registering phone.
                                                   					 If you want additional numbers on a phone, manually add them later. | Note | The
                                                   					 Cisco CME setup tool associates one number with each newly registering phone.
                                                   					 If you want additional numbers on a phone, manually add them later. |
| Note | The
                                                   					 Cisco CME setup tool associates one number with each newly registering phone.
                                                   					 If you want additional numbers on a phone, manually add them later. |
| Do you want dual-line extensions assigned to phones? [yes for dual-line / no for single-line]: | Yes —Each
                                             						newly registering IP phones is assigned a single number that is associated with
                                             						a single phone button. The system generates a dual-line ephone-dn entry for
                                             						each ephone-dn. No —IP
                                             						phones are linked directly to one or more PSTN trunk lines. Using keyswitch
                                             						mode requires manual configuration in addition to using the Cisco CME setup
                                             						tool. The system generates two ephone-dn entries for each ephone-dn, and they
                                             						are both assigned to a single phone. |
| What language do you want on IP phones?
      0  English
      1  French
      2  German
      3  Russian
      4  Spanish
      5  Italian
      6  Dutch
      7  Norwegian
      8  Portuguese
      9  Danish
      10  Swedish
 [0]: | Language for IP phone displays, selected from the list. Default is 0, English. |
| Which Call Progress tone set do you want on IP phones :     
      0  United States
      1  France
      2  Germany
      3  Russia
      4  Spain
      5  Italy
      6  Netherlands
      7  Norway
      8  Portugal
      9  UK
    10  Denmark
    11  Switzerland
    12  Sweden
    13  Austria
    14  Canada
[0]: | Locale
                                          					 for the tone set used to indicate call status or progress, selected from the
                                          					 list. Default is 0, United States. |
| What is the first extension number you want to configure :[0]: | First
                                          					 number in pool of extension numbers to be created for IP phones connected to
                                          					 the Cisco router to be configured. Starting with this number, remaining extension numbers are automatically
                                             						configured in a contiguous manner. This
                                             						number must be compatible with your telephone number plan and if you use Direct
                                             						Inward Dialing (DID) service, with public switched telephone network (PSTN)
                                             						numbering requirements. |
| Do you have Direct-Inward-Dial service for all your phones? [yes/no]: | Yes—If you have trunk access to public telephone service by ISDN or VoIP for
                                             						all extension numbers. The system creates an appropriate dial plan. No—If you have simple analog phone lines only (for example, foreign exchange
                                             						office [FXO] interfaces) or if you have trunk access for some lines but not all
                                             						lines. |
| If you
                                          					 answer yes to the previous question, you see the following prompt: Enter the full E.164 number for the first phone: | Complete ten-digit telephone number, including area code, that corresponds to
                                          					 the first extension number. |
| Do you want to forward calls to a voice message service? [yes/no]: | Yes—To forward calls to a single voice message service number when an IP phone
                                             						is busy or does not answer. All phone extensions forward their calls to the
                                             						same voice message service pilot number. No—Not to forward calls to a single voice message service number. Answer no if
                                             						you do not have a voice message system or if you want to customize
                                             						call-forwarding behavior for each extension. |
| If you
                                          					 answer yes to the previous question, you see the following prompt: Enter the extension or pilot number of the voice message service: | Voice
                                          					 message service pilot number. This
                                             						step can be ignored during the setup dialog and manually configured later. |
| Call forward No Answer Timeout: [18]: | Timeout, in seconds, after which to forward calls to voice mail if they are not
                                          					 answered. Default is 18. |
| Do you wish to change any of the above information? [yes/no]: | Yes —Starts
                                             						the dialog over again without implementing any of the answers that you
                                             						previously gave. No —Uses
                                             						specified values to automatically build basic configuration for Cisco Unified
                                             						IP Phone 7910s, 7940s, and 7960s in Cisco Unified CME. |

| Note | The
                                                   					 Cisco CME setup tool associates one number with each newly registering phone.
                                                   					 If you want additional numbers on a phone, manually add them later. |
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

| template tag | Creates
                                          						a basic configuration template that supports all the configurations available
                                          						on the voice register template. Range: 1 to 10. |
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
| auto-assign (auto-register) | Configures the mandatory range of directory numbers for phones
                                          						auto registering on Unified CME. |
| auto-register | Enables
                                          						automatic registration of SIP phones with the Cisco Unified CME system. |
| auto-reg-ephone | Enables automatic registration of ephones with the Cisco Unified CME system. |

| template-tag | The template tag that was created with the voice register template command in voice register
                                          						global configuration mode. Range is 1 to 5. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

|  | Description |
|---|---|
| voice register template | Enters voice register template configuration mode and
                                          						defines a template of common parameters for SIP phones. |

| flash: | Router flash memory. |
|---|---|
| slot0: | Router slot 0 memory. |
| tftp:// | External TFTP server. |
| url | URL for external TFTP server. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

| Command | Description |
|---|---|
| create profile (voice register global) | Generates the configuration profiles required for SIP
                                          						phones. |
| reset (voice register global) | Performs a “hard” reboot similar to a power-off-power-on
                                          						sequence for all SIP phones in Cisco Unified CME, including contacting the
                                          						Dynamic Host Configuration Protocol (DHCP) server and the TFTP server for
                                          						updated information. |

| label | Name of a configured PKI trustpoint with a valid
                                          						certificate. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| 12 | Selects a 12-hour clock. This is the default. |
|---|---|
| 24 | Selects a 24-hour clock. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco ITS 2.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |

|  | Description |
|---|---|
| date-format | Selects a format to display the date on Cisco IP phones. |

| 12 | Sets time in a 12-hour (AM/PM) clock. |
|---|---|
| 24 | Sets time in a 24-hour clock. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

|  | Description |
|---|---|
| voice register global | Enters voice register global configuration mode in order to
                                          						set global parameters for all supported Cisco SIP phones in a Cisco CME or
                                          						Cisco SIP SRST environment. |

| seconds | Number of seconds. Range: 3 to 60000. You can enter a
                                          						different value for each hop between ephone-dns in a hunt group. If you enter a
                                          						single value, the value is applied to each hop between ephone-dns in a hunt
                                          						group. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was modified to accept multiple arguments that
                                          						correspond to the number of ephone-dns configured in the hunt group. |

| 12.4(9)T | Cisco Unified CME 4.0 | This command with modifications up was integrated into
                                          						Cisco IOS Release 12.4(9)T. |
|---|---|---|

|  | Description |
|---|---|
| final | Defines the last ephone-dn in an ephone hunt group. |
| hops | Defines the number of times that a call is redirected to
                                          						the next ephone-dn in a peer ephone-hunt-group list before proceeding to the
                                          						final ephone-dn. |
| list | Defines the ephone-dns that participate in an ephone hunt
                                          						group. |
| max-redirect | Changes the current number of allowable redirects in a
                                          						Cisco Unified CME system. |
| max-timeout | Sets the maximum combined timeout for the no-answer periods
                                          						for all ephone-dns in an ephone-hunt list, |
| no-reg (ephone-hunt) | Specifies that the pilot number of an ephone hunt group
                                          						should not register with the H.323 gatekeeper. |
| pilot | Defines the ephone-dn that callers dial to reach an ephone
                                          						hunt group. |
| preference (ephone-hunt) | Sets preference order for the ephone-dn associated with an
                                          						ephone-hunt-group pilot number. |

| seconds | Number of seconds. Range is 3 to 60000. Default is 180. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

| Command | Description |
|---|---|
| call-forward noan | Enables call forwarding so that incoming calls to an
                                          						extension (ephone-dn) that does not answer are forwarded to another number. |
| final (voice hunt-group) | Defines the last extension in a voice hunt group. |
| hops (voice hunt-group) | Defines the number of times that a call is redirected to
                                          						the next directory number in a peer voice hunt-group list before proceeding to
                                          						the final directory number. |
| list (voice hunt-group) | Defines the directory numbers that participate in a hunt
                                          						group. |

| seconds | Number of seconds after connection before a call is
                                          						disconnected from a busy signal. Range is from 0 to 30 seconds. Default is 10. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(8)T | Cisco ITS 2.0 | This command was introduced. |

|  | Description |
|---|---|
| telephony-service | Enters telephony-service configuration mode. |

| seconds | Interdigit timeout duration for Cisco IP phones, in
                                          						seconds. Range is from 2 to 120. Default is 10. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XB | Cisco ITS 1.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |

|  | Description |
|---|---|
| timeouts interdigit (voice-port) | Configures the interdigit timeout value for a specified
                                          						voice port. |

| seconds | Interdigit timeout duration for Cisco SIP phones, in seconds. Range is from 2
                                          						to 120. Default is 10. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| Cisco
                                          						IOS XE Everest 16.4.1 | Cisco
                                          						Unified CME 11.6 | This
                                          						command was introduced. |

|  | Description |
|---|---|
| timeouts interdigit (telephoy-service) | Configures the interdigit timeout value for a SCCP phone in Cisco Unified CME
                                          						system. |

| seconds | Duration, in seconds, between night-service notification
                                          						bells. Range: 4 to 30. Default: 12. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XW5 | Cisco Unified CME 4.2 | This command was introduced. |

| Command | Description |
|---|---|
| night-service bell (ephone) | Marks an IP phone to receive night-service bell
                                          						notification when incoming calls are received during night-service time periods
                                          						on ephone-dns that are marked for night service. |
| night-service bell (ephone-dn) | Marks an ephone-dn to send night-service bell notification
                                          						to designated IP phones during night-service time periods. |

| seconds | Duration, in seconds, for which the Cisco CME system allows
                                          						ringing to continue if a call is not answered. Range is from 5 to 60000.
                                          						Default is 180. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

|  | Description |
|---|---|
| telephony-service | Enters telephony-service configuration mode. |

| seconds | Duration, in seconds, to wait before recalling a
                                          						transferred call. Range: 1 to 1800. Default: 0 (disabled). |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| call-forward busy | Enables call forwarding so that incoming calls to a busy
                                          						extension (ephone-dn) are forwarded to another extension. |
| call-forward noan | Enables call forwarding so that incoming calls to an
                                          						extension (ephone-dn) that does not answer are forwarded to another number. |
| transfer-mode | Specifies the call transfer method for an individual
                                          						directory number. |
| transfer-system | Specifies the call transfer method globally for all
                                          						directory numbers. |
| trunk | Associates an ephone-dn with a foreign exchange office
                                          						(FXO) port. |

| seconds | Duration, in seconds, to wait before recalling a transferred call. Range: 1 to
                                          						1800. Default: 0 (disabled). |
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
| timeouts transfer-recall (Ephone-dn (config-ephone-dn) and
                                          						Telephony-service configuration (config-telephony) | Enables
                                          						Cisco Unified CME to recall a transferred call if the transfer-to party does
                                          						not answer or is busy. |

| seconds | Duration, in seconds, to wait before recalling a transferred call. Range: 1 to
                                          						1800. Default: 0 (disabled). |
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
| timeouts transfer-recall (Ephone-dn (config-ephone-dn) and
                                          						Telephony-service configuration (config-telephony) | Enables
                                          						Cisco Unified CME to recall a transferred call if the transfer-to party does
                                          						not answer or is busy. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco ITS 2.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |
| Cisco IOS XE Gibraltar 16.11.1a Release | Unified CME 12.6 | The command is deprecated. It is not supported on Unified CME 12.6 and later releases. |

| Note | Cisco discourages this method for setting network time. The router
                                       		  should be set up to automatically synchronize its router clock from a
                                       		  network-based clock source using Network Time Protocol (NTP). In the rare case
                                       		  that a network NTP clock source is not available, the time-webedit can be used to allow manual
                                       		  setting and resetting of the router clock through the Cisco CME GUI. |
|---|---|

|  | Description |
|---|---|
| dn - webedit | Enables adding of directory numbers through a web
                                          						interface. |
| telephony-service | Enters telephony-service configuration mode. |

| number | Numeric
                                          						code for a named time zone. The following are the selections. The numbers in
                                          						parentheses indicate the offset from Coordinated Universal Time (UTC) in
                                          						minutes. Note The
                                                   						time shows incorrectly for phones configured in West Africa during the Summer
                                                   						Time. For West Africa, Summer Time or Daylight Savings Time (DST) is not used.
                                                   						There is no correct time zone in this time zone list to account for this time
                                                   						zone. 1 —Dateline Standard Time (-720) 2 —Samoa
                                             						  Standard Time (-660) 3 —Hawaiian
                                             						  Standard Time (-600) 4 —Alaskan
                                             						  Standard/Daylight Time (-540) 5 —Pacific
                                             						  Standard/Daylight Time (-480) 6 —Mountain
                                             						  Standard/Daylight Time (-420) 7 —United
                                             						  States (US) Mountain Standard Time (-420) 8 —Central
                                             						  Standard/Daylight Time (-360) 9 —Mexico
                                             						  Standard/Daylight Time (-360) 10 —Canada
                                             						  Central Standard Time (-360) 11 —SA Pacific
                                             						  Standard Time (-300) 12 —Eastern
                                             						  Standard/Daylight Time (-300) 13 —US Eastern
                                             						  Standard Time (-300) 14 —Atlantic
                                             						  Standard/Daylight Time (-240) 15 —South
                                             						  America (SA) Western Standard Time (-240) 16 —Newfoundland Standard/Daylight Time (-210) 17 —SA
                                             						  Standard/Daylight Time (-180) 18 —SA Eastern
                                             						  Standard Time (-180) 19 —Mid-Atlantic Standard/Daylight Time (-120) 20 —Azores
                                             						  Standard/Daylight Time (-60) 21 —UTC
                                             						  Standard/Daylight Time (+0) 22 —Greenwich
                                             						  Standard Time (+0) 23 —Western
                                             						  Europe Standard/Daylight Time (+60) 24 —GTB
                                             						  (Athens, Istanbul, Minsk) Standard/Daylight Time (+60) 25 —Egypt
                                             						  Standard/Daylight Time (+60) 26 —Eastern
                                             						  Europe Standard/Daylight Time (+60) | Note | The
                                                   						time shows incorrectly for phones configured in West Africa during the Summer
                                                   						Time. For West Africa, Summer Time or Daylight Savings Time (DST) is not used.
                                                   						There is no correct time zone in this time zone list to account for this time
                                                   						zone. |
|---|---|---|---|
| Note | The
                                                   						time shows incorrectly for phones configured in West Africa during the Summer
                                                   						Time. For West Africa, Summer Time or Daylight Savings Time (DST) is not used.
                                                   						There is no correct time zone in this time zone list to account for this time
                                                   						zone. |

| Note | The
                                                   						time shows incorrectly for phones configured in West Africa during the Summer
                                                   						Time. For West Africa, Summer Time or Daylight Savings Time (DST) is not used.
                                                   						There is no correct time zone in this time zone list to account for this time
                                                   						zone. |
|---|---|

| number continued | 27 —Romance
                                             						  Standard/Daylight Time (+120) 28 —Central
                                             						  Europe Standard/Daylight Time (+120) 29 —South
                                             						  Africa Standard Time (+120) 30 —Jerusalem
                                             						  Standard/Daylight Time (+120) 31 —Saudi
                                             						  Arabia Standard Time (+180) 32 —Russian
                                             						  Standard/Daylight Time (+180) 33 —Iran
                                             						  Standard/Daylight Time (+210) 34 —Caucasus
                                             						  Standard/Daylight Time (+240) 35 —Arabian
                                             						  Standard Time (+240) 36 —Afghanistan Standard Time (+270) 37 —West
                                             						  Asia Standard Time (+300) 38 —Ekaterinburg Standard Time (+300) 39 —India
                                             						  Standard Time (+330) 40 —Central
                                             						  Asia Standard Time (+360) 41 —Southeast Asia Standard Time (+420) 42 —China
                                             						  Standard/Daylight Time (+480) 43 —Taipei
                                             						  Standard Time (+480) 44 —Tokyo
                                             						  Standard Time (+540) 45 —Central
                                             						  Australia Standard/Daylight Time (+570) 46 —Australia Central Standard Time (+570) 47 —East
                                             						  Australia Standard Time (+600) 48 —Australia Eastern Standard/Daylight Time (+600) 49 —West
                                             						  Pacific Standard Time (+600) 50 —Tasmania
                                             						  Standard/Daylight Time (+600) 51 —Central
                                             						  Pacific Standard Time (+660) 52 —Fiji
                                             						  Standard Time (+720) 53 —New
                                             						  Zealand Standard/Daylight Time (+720) 54—Venezuela Standard Time (-270) 55—Pacific SA Daylight Time (-180) 56—Pacific SA Standard Time (-240) |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						product | Modification |
|---|---|---|
| 12.3(11)XL | Cisco
                                          						CME 3.2.1 | This
                                          						command was introduced. |
| 12.3(14)T | Cisco
                                          						CME 3.3 | This
                                          						command was integrated into Cisco IOS Release 12.3(14)T. |

| Command | Description |
|---|---|
| create cnf-files | Sets
                                          						display and phone functionality for the Cisco IP Phone 7970 units using the
                                          						vendorConfig parameters of the downloaded firmware’s Sep*.cnf.xml configuration
                                          						file. |
| reset (telephony-service) | Performs a complete reboot of one or all phones associated with a Cisco Unified
                                          						CME router. |

| number | Range
                                          						is 1 to 53. Default is 5, Pacific Standard/Daylight Time |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco
                                          						CME 3.4 | This
                                          						command was introduced. |

| Number | Description | Offset in
                                          					 Minutes |
|---|---|---|
| 1 | Dateline
                                          					 Standard Time | -720 |
| 2 | Samoa
                                          					 Standard Time | -660 |
| 3 | Hawaiian
                                          					 Standard Time | -600 |
| 4 | Alaskan
                                          					 Standard/Daylight Time | -540 |
| 5 | Pacific
                                          					 Standard/Daylight Time | -480 |
| 6 | Mountain
                                          					 Standard/Daylight Time | -420 |
| 7 | US
                                          					 Mountain Standard Time | -420 |
| 8 | Central
                                          					 Standard/Daylight Time | -360 |
| 9 | Mexico
                                          					 Standard/Daylight Time | -360 |
| 10 | Canada
                                          					 Central Standard Time | -360 |
| 11 | SA
                                          					 Pacific Standard Time | -300 |
| 12 | Eastern
                                          					 Standard/Daylight Time | -300 |
| 13 | US
                                          					 Eastern Standard Time | -300 |
| 14 | Atlantic Standard/Daylight Time | -240 |
| 15 | SA
                                          					 Western Standard Time | -240 |
| 16 | Newfoundland Standard/Daylight Time | -210 |
| 17 | South
                                          					 America Standard/Daylight Time | -180 |
| 18 | SA
                                          					 Eastern Standard Time | -180 |
| 19 | Mid-Atlantic Standard/Daylight Time | -120 |
| 20 | Azores
                                          					 Standard/Daylight Time | -60 |
| 21 | GMT
                                          					 Standard/Daylight Time | +0 |
| 22 | Greenwich Standard Time | +0 |
| 23 | W.
                                          					 Europe Standard/Daylight Time | +60 |
| 24 | GTB
                                          					 Standard/Daylight Time | +60 |
| 25 | Egypt
                                          					 Standard/Daylight Time | +60 |
| 26 | E.
                                          					 Europe Standard/Daylight Time | +60 |
| 27 | Romance
                                          					 Standard/Daylight Time | +120 |
| 28 | Central
                                          					 Europe Standard/Daylight Time | +120 |
| 29 | South
                                          					 Africa Standard Time | +120 |
| 30 | Jerusalem Standard/Daylight Time | +120 |
| 31 | Saudi
                                          					 Arabia Standard Time | +180 |
| 32 | Russian
                                          					 Standard/Daylight Time | +180 |
| 33 | Iran
                                          					 Standard/Daylight Time | +210 |
| 34 | Caucasus Standard/Daylight Time | +240 |
| 35 | Arabian
                                          					 Standard Time | +240 |
| 36 | Afghanistan Standard Time | +270 |
| 37 | West
                                          					 Asia Standard Time | +300 |
| 38 | Ekaterinburg Standard Time | +300 |
| 39 | India
                                          					 Standard Time | +330 |
| 40 | Central
                                          					 Asia Standard Time | +360 |
| 41 | SE Asia
                                          					 Standard Time | +420 |
| 42 | China
                                          					 Standard/Daylight Time | +480 |
| 43 | Taipei
                                          					 Standard Time | +480 |
| 44 | Tokyo
                                          					 Standard Time | +540 |
| 45 | Cen.
                                          					 Australia Standard/Daylight Time | +570 |
| 46 | AUS
                                          					 Central Standard Time | +570 |
| 47 | E.
                                          					 Australia Standard Time | +600 |
| 48 | AUS
                                          					 Eastern Standard/Daylight Time | +600 |
| 49 | West
                                          					 Pacific Standard Time | +600 |
| 50 | Tasmania Standard/Daylight Time | +600 |
| 51 | Central
                                          					 Pacific Standard Time | +660 |
| 52 | Fiji
                                          					 Standard Time | +720 |
| 53 | New
                                          					 Zealand Standard/Daylight Time | +720 |
| 54 | Venezuela Standard Time | -270 |
| 55 | Pacific
                                          					 SA Daylight Time | -180 |
| 56 | Pacific
                                          					 SA Standard Time | -240 |

| Command | Description |
|---|---|
| dst (voice register global) | Sets
                                          						the time period for daylight saving time on SIP phones. |
| dst auto-adjust (voice register global) | Enables automatic adjustment of daylight saving time on SIP phones. |
| time-format (voice register global) | Selects a 12-hour clock or a 24-hour clock for the time display format on SIP
                                          						phones in a Cisco CME system |

| max-length | Maximum length of the transfer number. Range is 3 to 16. |
|---|---|

| Release | Modification |
|---|---|
| 15.3(2)T | This command was introduced. |

| Command | Description |
|---|---|
| voice register pool | Enters voice register pool configuration mode and creates a
                                          						pool configuration for a SIP IP phone in Cisco Unified CME or for a set of SIP
                                          						phones in Cisco Unified SIP SRST |
| voice register template | Enters voice register template configuration mode and
                                          						defines a template of common parameters for SIP phones. |

| Cisco IOS Release | Cisco product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

|  | Description |
|---|---|
| conference (voice register template) | Enables the soft key for conference in a SIP phone
                                          						template. |
| template | Applies a template to a SIP phone. |
| transfer-blind (voice register template) | Enables a soft key for blind transfer in a SIP phone
                                          						template. |

| Cisco IOS Release | Version | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

|  | Description |
|---|---|
| conference (voice register template) | Enables the soft key for conference in a SIP phone
                                          						template. |
| template | Applies a template to a SIP phone. |
| transfer-attended (voice register template) | Enables the soft key for attended transfer on SIP phones. |

| new-call | Dialed digits are collected from new call leg. Default
                                          						value. |
|---|---|
| orig-call | Dialed digits are collected from original call leg. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco Unified CME 4.3 Cisco Unified SRST 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 Cisco Unified SRST 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| transfer-mode | Specifies the type of call transfer for an individual
                                          						directory number that uses the ITU-T H.450.2 standard. |
| transfer-pattern (telephony-service) | Allows the transfer of calls to phones outside the local
                                          						Cisco Unified CME network. |
| transfer - system | Specifies the call transfer method for all IP phones on a
                                          						Cisco Unified CME router using the ITU-T H.450.2 standard. |

| blind | Transfers calls without consultation using a single phone
                                          						line. |
|---|---|
| consult | Transfers calls with consultation using a second phone
                                          						line, if available. |

| Cisco IOS Release | Cisco CME Version | Modification |
|---|---|---|
| 12.2(11)YT | 2.1 | This command was introduced. |
| 12.2(15)T | 2.1 | This command was integrated into Cisco IOS Release
                                          						12.2(15)T. |

|  | Description |
|---|---|
| ephone - dn | Enters ephone-dn configuration mode to set directory
                                          						numbers and parameters for individual Cisco IP phone lines. |
| transfer - system | Specifies the call transfer method for all IP phones on a
                                          						Cisco ITS router using the ITU-T H.450.2 standard. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| transfer-pattern | String of digits for permitted call transfers. Wildcards
                                          						are allowed. A maximum of 32 transfer patterns can be entered, using a separate
                                          						command for each one. |
|---|---|
| blind | (Optional) When H.450.2 consultative call transfer is used,
                                          						this keyword forces transfers that match the pattern to be executed as blind
                                          						transfers. Overrides settings made using the transfer-system and transfer-mode commands. |

| Cisco IOS Release | Cisco CME Version | Modification |
|---|---|---|
| 12.1(5)YD | Cisco ITS 1.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |
| 12.2(15)T | Cisco ITS 2.1 | The blind keyword was added. |

|  | Description |
|---|---|
| transfer-mode | Specifies the type of call transfer for an individual IP
                                          						phone extension number that uses the ITU-T H.450.2 standard. |
| transfer-system | Specifies the call transfer method for all Cisco CME
                                          						extensions that use the ITU-T H.450.2 standard. |

| Release | Modification |
|---|---|
| 15.3(2)T | This command was introduced. |

| Command | Description |
|---|---|
| voice register pool | Enters voice register pool configuration mode and creates a
                                          						pool configuration for a Cisco Unified SIP IP phone in Cisco Unified CME or for
                                          						a set of Cisco Unified SIP IP phones in Cisco Unified SIP SRST. |
| voice register template | Enters voice register template configuration mode and
                                          						defines a template of common parameters for Cisco Unified SIP IP phones. |

| blind | Transfers calls without consultation using a single phone line and the Cisco
                                          						proprietary method. This is the default for Cisco CME 3.4 and earlier versions. |
|---|---|
| full-blind | Transfers calls without consultation using H.450.2 standard methods. |
| full-consult | Transfers calls using H.450.2 with consultation using a second phone line, if
                                          						available. The calls fall back to full-blind if
                                          						a second line is not available. This is the default for Cisco Unified CME 4.0
                                          						and later versions. |
| dss | Transfers calls with consultation to idle monitor lines. All other
                                          						call-transfer behavior is identical to full-consult. |
| local-consult | Transfers calls with local consultation using a second phone line, if
                                          						available, or the calls fall back to blind if the target for consultation or
                                          						transfer is not local. This mode is intended for use primarily in Voice over
                                          						Frame Relay (VoFR) networks, because the Cisco VoFR call transfer protocol does
                                          						not support an end-to-end transfer-with-consultation mechanism. Not supported
                                          						if transfer-to destination is on the Cisco ATA, Cisco VG224, or a
                                          						SCCP-controlled FXS port. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.2(11)YT | Cisco
                                          						ITS 2.1 | This
                                          						command was introduced. |
| 12.2(15)T | Cisco
                                          						ITS 2.1 | This
                                          						command was integrated into Cisco IOS Release 12.2(15)T. |
| 12.3(11)T | Cisco
                                          						CME 3.2 | The dss keyword
                                          						was introduced. |
| 12.4(4)XC | Cisco
                                          						Unified CME 4.0 | The
                                          						command default was changed from blind to full-consult . |
| 12.4(9)T | Cisco
                                          						Unified CME 4.0 | This
                                          						command with the default of full-consult was integrated into Cisco IOS Release 12.4(9)T. |

| Cisco
                                          					 Product | transfer-system Default | transfer-system to Use | Transfer Method Recommendation |
|---|---|---|---|
| Cisco
                                          					 Unified CME 4.0 and later versions | full-consult | full-consult or full-blind | Use
                                          					 H.450.2 for call transfer. Because this is the default for this version, you do
                                          					 not need to use the transfer-system command unless you want to use the full-blind or dss keyword. Optionally, you can use the proprietary Cisco method by using the transfer-system command with the blind or local-consult keyword. |
| Cisco
                                          					 CME 3.0 to 3.3 | blind | full-consult or full-blind | Use
                                          					 H.450.2 for call transfer. You must explicitly configure the transfer-system command with the full-consult or full-blind keyword because H.450.2 is not the default for this version. Optionally, you can use the proprietary Cisco method by using the transfer-system command with the blind or local-consult keyword. |
| Cisco
                                          					 ITS 2.1 to 3.0 | blind | blind or local-consult | Use the
                                          					 Cisco proprietary method. Because this is the default for this version, you do
                                          					 not need to use the transfer-system command unless you want to use the local-consult keyword. Optionally, you can use the H.450.2 standard for call transfer by using transfer-system command with the full-consult or full-blind keyword. You must also configure the router with a Tcl script that is contained
                                          					 in the file called app-h450-transfer.x.x.x.x.zip. This file is posted on the
                                          					 Cisco Unified CME software download website at http://www.cisco.com/cgi-bin/tablebuild.pl/ip-iostsp . |

|  | Description |
|---|---|
| transfer-mode | Specifies the type of call transfer for an individual IP phone extension that
                                          						uses the H.450.2 standard. |

| called | Translate the called number. |
|---|---|
| calling | Translate the calling number. |
| translation - rule - tag | Unique
                                          						sequence number by which the rule set is referenced. This number is arbitrarily
                                          						chosen. Range is from 1 to 2147483647. There is no default value. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco
                                          						ITS 2.0 | This
                                          						command was introduced. |
| 12.2(8)T | Cisco
                                          						ITS 2.0 | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T. |
| 12.4(4)XC | Cisco
                                          						Unified CME 4.0 | This
                                          						command was made available in ephone-dn-template configuration mode. |
| 12.4(9)T | Cisco
                                          						Unified CME 4.0 | This
                                          						command in ephone-dn-template configuration mode was integrated into Cisco IOS
                                          						Release 12.4(9)T. |

| Note | For this
                                       		  command to take effect, appropriate translation rules must have been created at
                                       		  the VoIP configuration level. Use the show voice translation-rule command to view the translation
                                       		  rules that you have defined. For in formation, see the Dial Peer Configuration
                                       		  on Voice Gateway Routers. |
|---|---|

|  | Description |
|---|---|
| rule | Defines a translation rule. |
| translation - rule | Creates a translation identifier and enters translation-rule configuration
                                          						mode. |

| incoming | Specifies that this translation profile handles incoming
                                          						calls. |
|---|---|
| outgoing | Specifies that this translation profile handles outgoing
                                          						calls. |
| name | Name of the translation profile. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(3)T | Cisco Unified CME 8.5 | This command was introduced. |

| Command | Description |
|---|---|
| show voice translation-profile | Displays the configuration of a translation profile. |
| translate (call-manager- fallback) | Applies a translation rule to modify the phone number
                                          						dialed or received by any Cisco IP phone user during CallManager fallback. |
| translation-rule | Creates a translation name and enters translation-rule
                                          						configuration mode to apply rules to the translation name. |
| voice translation-profile | Defines a translation profile for voice calls. |

| called | Called party requires translation. |
|---|---|
| calling | Calling party requires translation. |
| rule-tag | The rule-tag is an arbitrarily chosen number by which the
                                          						rule set is referenced. The range is from 1 to 2147483. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco SIP SRST 3.0 | This command was introduced. |
| 12.3(4)T | Cisco SIP SRST 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was added to Cisco CME. |

|  | Description |
|---|---|
| alias (voice register pool) | Allows Cisco SIP IP phones to handle inbound PSTN calls to
                                          						telephone numbers that are unavailable when the main proxy is not available. |
| id (voice register pool) | Explicitly identifies a locally available individual Cisco
                                          						SIP IP phone, or when running Cisco Unified SIP SRST, set of Cisco SIP IP
                                          						phones. |
| translate-outgoing (dial-peer) | Applies a translation rule to manipulate dialed digits on
                                          						an outbound POTS or VoIP call leg. |
| voice register pool | Enters voice register pool configuration mode for SIP
                                          						phones. |

| incoming | Specifies that this translation profile handles incoming
                                          						calls. |
|---|---|
| outgoing | Specifies that this translation profile handles outgoing
                                          						calls. |
| name | Name of the translation profile. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(11)T | Cisco CME 3.2 | This command was introduced. |
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was made available in ephone-dn-template
                                          						configuration mode. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command in ephone-dn-template configuration mode was
                                          						integrated into Cisco IOS Release 12.4(9)T. |

|  | Description |
|---|---|
| s how voice translation-profile | Displays the configuration of a translation profile. |
| translate | Applies a translation rule to modify the phone number
                                          						dialed or received by any Cisco Unified IP phone user. |
| translation-rule | Creates a translation name and enters translation-rule
                                          						configuration mode. |
| voice translation-profile | Defines a translation profile for voice calls. |
| voice translation-rule | Defines a translation rule for voice calls. |

| name | Name of the translation profile to apply to incoming calls
                                          						to this directory number. This is the name argument that was created for
                                          						the profile with the voice translation-profile command. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XJ | Cisco Unified CME 4.1 | This command was introduced. |
| 12.4(15)T | Cisco Unified CME 4.1 | This command was integrated into Cisco IOS Release
                                          						12.4(15)T. |

|  | Description |
|---|---|
| s how voice translation-profile | Displays the configuration of a translation profile. |
| translate (translation profiles) | Associates a translation rule with a voice translation
                                          						profile. |
| voice translation-profile | Defines a translation profile for voice calls. |
| voice translation-rule | Defines a translation rule for voice calls. |

| udp | (Optional) Selects UDP as
                                       					 the transport layer protocol. This is the default transport protocol. |
|---|---|
| tcp | (Optional) Selects TCP as
                                       					 the transport layer protocol. |

| Cisco
                                    				  IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.3(3)M | Cisco SIP
                                       					 CME 10.0 | This
                                       					 command was introduced. |

| Command | Description |
|---|---|
| voice register pool-type | Adds a new Cisco Unified SIP IP phone to Cisco Unified CME. |

| digit-string | The number of the trunk line. |
|---|---|
| timeout seconds | (Optional) Interdigit timeout between dialed digits, in
                                          						seconds. Range is 3 to 30. Default is 3. |
| transfer-timeout seconds | (Optional) Number of seconds that Cisco Unified CME waits
                                          						for the transfer-to party to answer a call after which the call is recalled to
                                          						the phone that initiated the transfer. This keyword is supported for dual-line
                                          						ephone-dns only. Range is 5 to 60000. Default is disabled. |
| monitor-port port | (Optional) Enables a button lamp or icon that shows that
                                          						the specified port is in use. Port argument is
                                          						platform-dependent; type ? to display syntax. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(11)T | Cisco CME 3.2 | This command was introduced. |
| 12.4(4)XC | Cisco Unified CME 4.0 | The monitor-port and transfer-timeout keywords were
                                          						added and support for dual-line ephone-dns was added. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command with modifications was integrated into Cisco
                                          						IOS Release 12.4(9)T. |

|  | Description |
|---|---|
| destination-number | Specifies a connection mode for a voice port. |

| trustpoint-name | Name of the trustpoint to be associated with the Cisco
                                          						Unified CME CTL provider certificate or the Cisco Unified SRST device
                                          						certificate. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(14)T | Cisco SRST 3.3 | This command was introduced for Cisco SRST. |
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced for Cisco Unified CME. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command for Cisco Unified CME was integrated into
                                          						Cisco IOS Release 12.4(9)T. |

|  | Description |
|---|---|
| ctl-service admin | Specifies a user name and password to authenticate the CTL
                                          						client during the CTL protocol. |
| debug credentials | Sets debugging on the credentials service. |
| ip source-address (credentials) | Enables the router to receive messages through the
                                          						specified IP address and port. |
| show credentials | Displays the credentials settings. |

| label | Trustpoint name for the CAPF server. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |

| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |
|---|---|---|

| phone-type | Type of
                                          						phone. The following phone types are predefined in the system: 12SP —12SP+ and 30VIP phones. 6901—Cisco Unified IP
                                             						  Phone 6901. 6911—Cisco Unified IP
                                             						  Phone 6911. 6921— Cisco Unified IP
                                             						  Phone 6921. 6941—Cisco Unified IP
                                             						  Phone 6941. 6945 —Cisco Unified IP Phone 6945. 6961—Cisco Unified IP
                                             						  Phone 6961. 7902 —Cisco Unified IP Phone 7902G. 7905 —Cisco Unified IP Phone 7905G. 7906 —Cisco
                                             						  Unified IP Phone 7906. 7910 —Cisco Unified IP Phones 7910 and 7910G. 7911 —Cisco Unified IP Phone 7911G. 7912 —Cisco
                                             						  Unified IP Phone 7912G. 7920 —Cisco
                                             						  Unified IP Phone 7920. 7921 —Cisco
                                             						  Unified Wireless IP Phone 7921. 7925 —Cisco
                                             						  Unified Wireless IP Phone 7925. 7931 —Cisco
                                             						  Unified IP Phone 7931G. 7935 —Cisco
                                             						  Unified IP Conference Station 7935. 7936 —Cisco
                                             						  Unified IP Conference Station 7936. 7937 —Cisco
                                             						  Unified IP Conference Station 7937. 7940 —Cisco
                                             						  Unified IP Phone 7940G. 7941 —Cisco
                                             						  Unified IP Phone 7941G. 7941GE —Cisco
                                             						  Unified IP Phone 7941G-GE. |
|---|---|
|  | 7942 —Cisco
                                             						  Unified IP Phone 7942. 7945 —Cisco
                                             						  Unified IP Phone 7945 7960 —Cisco
                                             						  Unified IP Phone 7960G. 7961 —Cisco
                                             						  Unified IP Phone 7961G. 7961GE —Cisco
                                             						  Unified IP Phone 7961G-GE. 7962 —Cisco
                                             						  Unified IP Phone 7962. 7965 —Cisco
                                             						  Unified IP Phone 7965. 7970 — Cisco Unified IP Phone 7970G. 7971 —Cisco
                                             						  Unified IP Phone 7971G-GE. 7975 —Cisco
                                             						  Unified IP Phone 7975. 7985 —Cisco
                                             						  Unified IP Phone 7985. 8941 —Cisco
                                             						  Unified IP Phone 8941. 8945 —Cisco
                                             						  Unified IP Phone 8945. 8961 —Cisco
                                             						  Unified IP Phone 8961. 9951 —Cisco
                                             						  Unified IP Phone 9951. 9971 —Cisco
                                             						  Unified IP Phone 9971. anl —Analog. ata —Cisco
                                             						  ATA-186 or Cisco ATA-188. bri —SCCP
                                             						  Gateway (BR). vgc-phone —VG248 phone emulation for analog phone. Note You can also add a new phone type to your configuration by using the ephone-type command. | Note | You can also add a new phone type to your configuration by using the ephone-type command. |
| Note | You can also add a new phone type to your configuration by using the ephone-type command. |
| addon 1 module-type | (Optional) Tells the router that an expansion module is being added to this
                                          						Cisco Unified IP Phone and the type of module. Valid entries for module-type are: 7914 —Cisco
                                             						  Unified IP Phone 7914 Expansion Module. 7915-12 —Cisco Unified IP Phone 7915 12-Button
                                             						  Expansion Module. 7915-24 —Cisco Unified IP Phone 7915 24-Button
                                             						  Expansion Module. 7916-12 —Cisco Unified IP Phone 7916 12-Button
                                             						  Expansion Module. 7916-24 —Cisco Unified IP Phone 7916 24-Button
                                             						  Expansion Module. Note This keyword is not supported for user-defined phone types created with the ephone-type command. | Note | This keyword is not supported for user-defined phone types created with the ephone-type command. |
| Note | This keyword is not supported for user-defined phone types created with the ephone-type command. |
| 2 module-type | (Optional) Tells the router that a second expansion module is being added to
                                          						this Cisco Unified IP Phone and the type of module. Valid entries for module-type are: 7914 —Cisco
                                             						  Unified IP Phone 7914 Expansion Module. 7915-12 —Cisco Unified IP Phone 7915 12-Button
                                             						  Expansion Module. 7915-24 —Cisco Unified IP Phone 7915 24-Button
                                             						  Expansion Module. 7916-12 —Cisco Unified IP Phone 7916 12-Button
                                             						  Expansion Module. 7916-24 —Cisco Unified IP Phone 7916 24-Button
                                             						  Expansion Module. Note This keyword is not supported for user-defined phone types created with the ephone-type command. | Note | This keyword is not supported for user-defined phone types created with the ephone-type command. |
| Note | This keyword is not supported for user-defined phone types created with the ephone-type command. |

| Note | You can also add a new phone type to your configuration by using the ephone-type command. |
|---|---|

| Note | This keyword is not supported for user-defined phone types created with the ephone-type command. |
|---|---|

| Note | This keyword is not supported for user-defined phone types created with the ephone-type command. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.2(11)YT | Cisco
                                          						ITS 2.1 | This
                                          						command was introduced. |
| 12.2(15)T | Cisco
                                          						ITS 2.1 | This
                                          						command was integrated into Cisco IOS Release 12.2(15)T. |
| 12.2(15)ZJ | Cisco
                                          						CME 3.0 | The
                                          						following keywords were added to this command: 7902 , 7905 , and 7912 . |
| 12.3(4)T | Cisco
                                          						CME 3.0 | This
                                          						command was integrated into Cisco IOS Release 12.3(4)T. |
| 12.3(7)T | Cisco
                                          						CME 3.1 | The 7920 and 7936 keywords were added. |
| 12.3(11)XL | Cisco
                                          						CME 3.2(1) | The 7970 keyword was added. |
| 12.3(14)T | Cisco
                                          						CME 3.3 | The 7971 keyword was added, and this command was integrated into Cisco IOS Release
                                          						12.3(14)T. |
| 12.4(4)XC | Cisco
                                          						Unified CME 4.0 | The 7911 , 7941 , 7941GE , 7961 , and 7961GE keywords were added. This command was made available in ephone-template
                                          						configuration mode. |
| 12.4(9)T | Cisco
                                          						Unified CME 4.0 | This
                                          						command was integrated into Cisco IOS Release 12.4(9)T. |
| 12.4(6)XE | Cisco
                                          						Unified CME 4.0(2) | The 7931 keyword was added. |
| 12.4(4)XC4 | Cisco
                                          						Unified CME 4.0(3) | The 7931 keyword was added. |
| 12.4(11)T | Cisco
                                          						Unified CME 4.0(3) | This
                                          						command was integrated into Cisco IOS Release 12.4(11)T. |
| 12.4(11)XJ2 | Cisco
                                          						Unified CME 4.1 | The 7921 and 7985 keywords were introduced. |
| 12.4(15)T | Cisco
                                          						Unified CME 4.1 | This
                                          						command was integrated into Cisco IOS Release 12.4(15)T. |
| 12.4(15)T1 | Cisco
                                          						Unified CME 4.1(1) | The 7942 , 7945 , 7962 , 7965 , and 7975 keywords were introduced. |
| 12.4(15)XZ | Cisco
                                          						Unified CME 4.3 | Support for user-defined phone types created with the ephone-type command was added. |
| 12.4(15)XZ1 | Cisco
                                          						Unified CME 4.3 | The 7915-12 , 7915-24 , 7916-12 , 7916-24 ,
                                          						and 7937 keywords were added. |
| 12.4(20)T | Cisco
                                          						Unified CME 7.0 | The 7915-12 , 7915-24 , 7916-12 , 7916-24 ,
                                          						and 7937 keywords were added and this command was integrated
                                          						into Cisco IOS Release 12.4(20)T. |
| 12.4(20)T1 | Cisco
                                          						Unified CME 7.0 | The 7925 keyword was added. |
| 15.0(1)XA | Cisco
                                          						Unified CME 8.0 | This
                                          						command was modified. The 6921, 6941, 6961, and IP-STE keywords were added. |
| 15.1(1)T | Cisco
                                          						Unified CME 8.0 | This
                                          						command was integrated into Cisco IOS Release 15.1(1)T. |
| 15.1(2)T | Cisco
                                          						Unified CME 8.1 | This
                                          						command was modified. The 6901 and 6911 keywords were added. |
| 15.2(1)T | Cisco
                                          						Unified CME 8.8 | This
                                          						command was modified. The 6945 , 8941 , and 8945 keywords were added. |
| 15.3(3)M | Cisco
                                          						Unified CME 10.0 | This
                                          						command was modified. The 7906 , 8961 , 9951 , and 9971 keywords were added. |

| Command | Description |
|---|---|
| ephone-type | Adds
                                          						a Cisco Unified IP phone type by defining a phone-type template. |
| reset (ephone) | Performs a complete reboot of one phone associated with a Cisco Unified CME
                                          						router. |
| reset (telephony-service) | Performs a complete reboot of one or all phones associated with a Cisco Unified
                                          						CME router. |

| phone-type | Type of SIP phone for which the dial plan is used. Values
                                          						are: 7905-7912 —Cisco Unified IP
                                             						  Phone 7905, 7905G, 7912, or 7912G. 7940-7960-others —Cisco Unified
                                             						  IP Phone 7911, 7940, 7940G, 7941, 7942, 7941GE, 7945, 7960, 7960G, 7961,
                                             						  7961GE, 7962, 7965, 7970, 7971, or 7975. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XJ | Cisco Unified CME 4.1 | This command was introduced. |
| 12.4(15)T | Cisco Unified CME 4.1 | This command was integrated into Cisco IOS Release
                                          						12.4(15)T. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | Support for Cisco Unified IP Phone 7942, 7945, 7962, 7965,
                                          						and 7975 was added. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| dialplan | Assigns a dial plan to a SIP phone. |
| filename | Specifies a custom XML file that contains the dial patterns
                                          						to use for the SIP dial plan. |
| pattern (voice register dialplan) | Defines a dial pattern for a SIP dial plan. |
| show voice register dialplan | Displays configuration information for a specific SIP dial
                                          						plan. |
| type (voice register pool) | Defines a phone type for a SIP phone. |

| phone-type | Type of
                                          						SIP phone that is being defined. Valid entries are as follows: 3905 —Cisco Unified IP Phone 3905. 3951 —Cisco Unified IP Phones 3911 and 3951. 6901 —Cisco Unified IP Phone 6901. 6911 —Cisco Unified IP Phone 6911. 6921 —Cisco Unified IP Phone 6921. 6922 —Cisco
                                             						  Unified IP Phone 6922. 6941 —Cisco Unified IP Phone 6941. 6945 —Cisco Unified IP Phone 6945. 6961 —Cisco Unified IP Phone 6961. 7821 —Cisco
                                             						  Unified IP Phones 7821. 7841 —Cisco Unified IP Phones 7841. 7861 —Cisco
                                             						  Unified IP Phones 7861. 7905 —Cisco
                                             						  Unified IP Phones 7905 and 7905G. 7906 —Cisco Unified IP Phone 7906G. 7911 —Cisco Unified IP Phone 7911G. 7912 —Cisco IP Phones 7912 and 7912G. 7940 —Cisco IP
                                             						  Phones 7940 and 7940G. 7941 —Cisco IP
                                             						  Phone 7941G. 7941GE —Cisco
                                             						  IP Phone 7941GE. 7942 —Cisco
                                             						  Unified IP Phone 7942. 7945 —Cisco
                                             						  Unified IP Phone 7945. 7960 —Cisco IP
                                             						  Phones 7960 and 7960G. 7961 —Cisco IP
                                             						  Phone 7961G. 7961GE —Cisco
                                             						  IP Phone 7961GE. 7962 —Cisco
                                             						  Unified IP Phone 7962. 7965 —Cisco
                                             						  Unified IP Phone 7965. 7970 —Cisco IP
                                             						  Phone 7970G. 7971 —Cisco IP
                                             						  Phone 7971GE. 7975 —Cisco
                                             						  Unified IP Phone 7975. 8851 —Cisco Unified IP Phone 8851. 8851NR —Cisco Unified IP Phone 8851NR. 8861 —Cisco Unified IP Phone 8861. 8865 —Cisco  IP Phone 8865. 8961 —Cisco
                                             						  Unified IP Phone 8961. 9900 —Cisco
                                             						  Unified IP Phone 9900. 9951 —Cisco
                                             						  Unified IP Phone 9951. 9971 —Cisco
                                             						  Unified IP Phone 9971. ATA —Cisco
                                             						  ATA-186 or Cisco ATA-188. ATA-187 —Cisco
                                             						  ATA-187. ATA-190 —Cisco ATA-190. ATA-191 —Cisco ATA-191. DX650 —Cisco
                                             						  DX650. Jabber-Android —Cisco Jabber App on Android. P100 —PingTel
                                             						  Xpressa 100. P600 —Polycom
                                             						  SoundPoint 600. Jabber-CSF-Client —Cisco
                                             						  Jabber CSF Client. |
|---|---|
| addon 1 CKEM | (Optional) Tells the router that a Cisco SIP IP Phone CKEM 36-Button Line
                                          						Expansion Module is being added to this Cisco Unified SIP IP phone. Note This option is available to Cisco Unified 8961, 9951, and 9971 SIP IP phones
                                                   						only. | Note | This option is available to Cisco Unified 8961, 9951, and 9971 SIP IP phones
                                                   						only. |
| Note | This option is available to Cisco Unified 8961, 9951, and 9971 SIP IP phones
                                                   						only. |
| 2 CKEM | (Optional) Tells the router that a second Cisco SIP IP Phone CKEM 36-Button
                                          						Line Expansion Module is being added to this Cisco Unified SIP IP phone. Note This option is available to Cisco Unified 9951 and 9971 SIP IP phones only. | Note | This option is available to Cisco Unified 9951 and 9971 SIP IP phones only. |
| Note | This option is available to Cisco Unified 9951 and 9971 SIP IP phones only. |
| 3 CKEM | (Optional) Tells the router that a third Cisco SIP IP Phone CKEM 36-Button Line
                                          						Expansion Module is being added to this Cisco Unified SIP IP phone. Note This option is available to Cisco Unified 9971 SIP IP phones only. | Note | This option is available to Cisco Unified 9971 SIP IP phones only. |
| Note | This option is available to Cisco Unified 9971 SIP IP phones only. |
| addon 1 CP-8800-Audio or addon 1 CP-8800-Video | (Optional) Tells the router that a Cisco SIP IP Phone 28-Button Line A-KEM or V-KEM is being added to this Cisco Unified SIP
                                          IP Phone. |
| 2 CP-8800-Audio or 2 CP-8800-Video | (Optional) Tells the router that a second Cisco SIP IP Phone A-KEM or V-KEM is being added to this Cisco Unified SIP IP Phone. |
| 2 CP-8800-Audio or 2 CP-8800-Video | (Optional) Tells the router that a second Cisco SIP IP Phone A-KEM or V-KEM is being added to this Cisco Unified SIP IP Phone. |

| Note | This option is available to Cisco Unified 8961, 9951, and 9971 SIP IP phones
                                                   						only. |
|---|---|

| Note | This option is available to Cisco Unified 9951 and 9971 SIP IP phones only. |
|---|---|

| Note | This option is available to Cisco Unified 9971 SIP IP phones only. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco
                                          						CME 3.4 | This
                                          						command was introduced. |
| 12.4(11)XJ | Cisco
                                          						Unified CME 4.1 | This
                                          						command was modified to add the 3951 , 7911 , 7941 , 7941GE , 7961 , 7961GE , 7970 , and 7971 keywords. |
| 12.4(15)T | Cisco
                                          						Unified CME 4.1 | The 3951 , 7911 , 7941 , 7941GE , 7961 , 7961GE , 7970 , and 7971 keywords were integrated into Cisco IOS Release 12.4(15)T. |
| 12.4(15)XZ | Cisco
                                          						Unified CME 4.3 | This
                                          						command was modified to add the 7942 , 7945 , 7962 , 7965 , and 7975 keywords. |
| 12.4(20)T | Cisco
                                          						Unified CME 7.0 | This
                                          						command was integrated into Cisco IOS Release 12.4(20)T. |
| 15.1(3)T | Cisco
                                          						Unified CME8.5 | This
                                          						command was modified to add the 8961 , 9951 ,and 9971 keywords. |
| 15.2(1)T | Cisco
                                          						Unified CME 8.8 | This
                                          						command was modified to add the 3905 keyword. |
| 15.2(2)T | Cisco
                                          						Unified CME 9.0 | This
                                          						command was modified to add the 6901 , 6911 , 6921 , 6941 , 6945 , 6961 , ATA-187 ,
                                          						and Jabber-Android keywords. |
| 15.2(4)M | Cisco
                                          						Unified CME 9.1 | This
                                          						command was modified to include the addon 1 CKEM , 2 CKEM , and 3 CKEM keywords. |
| 15.3(3)M | Cisco
                                          						Unified CME 10.0 | This
                                          						command was modified to add the 6922 and 9900 keywords. |
| 15.4(3)M | Cisco
                                          						Unified CME 10.5 | This
                                          						command was modified. The 78XX , DX650 and Jabber-CSF-Client keywords were
                                          						added. |
| Cisco IOS XE Gibraltar 16.10.1a Release | Unified CME 12.5 | This command was modified. The ATA-191 , CP-8800-Audio , and CP-8800-Video keywords were added. |

| Note | All the configuration characteristics of CKEM discussed here is applicable to CP-8800-Audio and CP-8800-Video . |
|---|---|

| Note | Cisco
                                       		  Unified CME enables the busy trigger-per-button (voice register pool) command when phone-type 3905 is
                                       		  specified. |
|---|---|

| Command | Description |
|---|---|
| busy-trigger-per-button (voice register pool) | Sets
                                          						the maximum number of calls allowed on a SIP directory number before activating
                                          						Call Forward Busy or a busy tone. |
| load (voice register global) | Associates a type of Cisco Unified SIP IP phone with a phone firmware file. |
| reset (voice register global) | Performs a complete reboot of all SIP phones associated with a Cisco Unified
                                          						CME router. |
| reset (voice register pool) | Performs a complete reboot of one SIP phone associated with a Cisco Unified CME
                                          						router. |
| restart (voice register) | Performs a fast reset of one or all SIP phones associated with a Cisco Unified
                                          						CME router. |
| voice register pool | Enters voice register pool configuration mode for SIP phones. |

| vg202 | Cisco VG202 Voice Gateway with 2 FXS ports. |
|---|---|
| vg204 | Cisco VG204 Voice Gateway with 4 FXS ports. |
| vg224 | Cisco VG224 Voice Gateway with 24 FXS ports. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| create cnf-files (voice-gateway) | Generates the XML configuration files that are required to
                                          						autoconfigure the Cisco voice gateway. |
| mac-address (voice-gateway) | Defines the MAC address of the voice gateway to
                                          						autoconfigure. |
| voice-port (voice-gateway) | Identifies the ports on the voice gateway that register to
                                          						Cisco Unified CME. |