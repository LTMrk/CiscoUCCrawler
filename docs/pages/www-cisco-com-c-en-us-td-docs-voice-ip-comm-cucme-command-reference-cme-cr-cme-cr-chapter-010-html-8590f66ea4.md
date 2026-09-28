---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-command-reference-cme-cr-cme-cr-chapter-010-html-8590f66ea4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/command/reference/cme_cr/cme_cr_chapter_010.html
retrieved_at: 2026-08-21T20:40:16.538901+00:00
---

Cisco Unified Communications Manager Express Command Reference

# Cisco Unified Communications Manager Express Command Reference

Updated: July 19, 2018

Chapter: Cisco Unified CME Commands: C

## Chapter: Cisco Unified CME Commands: C

# Cisco Unified CME Commands: C

## call application voice aa-hunt

Effective with Cisco IOS Release 12.3(14)T and later, the call application voice aa-hunt command is replaced by the param aa-hunt command. See the param aa-hunt command for more information.

To declare a Cisco Unified CME basic automatic call distribution
                              		  (B-ACD) menu number and associate it with the pilot number of an ephone hunt
                              		  group, use the call application voice aa-hunt command in global configuration mode. To remove the menu number and the
                              		  ephone hunt group pilot number, use the no form of this command.

call application voice application-name aa-hunt menu-number pilot-number

no call application voice application-name aa-hunt menu-number pilot-number

### Syntax Description

menu-number

Number that callers must dial to reach the pilot number of
                                          						an ephone hunt group. The range is from 1to 10. The default is 1.

application-name

Application name given to the call queue script in the call application voice command.

pilot-number

Ephone hunt group pilot number.

### Command Default

Cisco CME B-ACD menu number 1 is configured, but it has no pilot
                              		  number .

### Command Modes

Global configuration (config)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(11)XL

Cisco CME 3.2.1

This command was introduced.

12.3(14)T

Cisco CME 3.2.2

This command was integrated into Cisco IOS Release
                                          						12.3(14)T.

12.3(14)T

Cisco CME 3.3

This command was replaced with the param aa-hunt command.

### Usage Guidelines

This command is used only with with a version of the Cisco Unified
                              		  CME B-ACD script that is earlier than 2.1.0.0 and is used only with with a
                              		  version of the Cisco Unified CME B-ACD script that is earlier than 2.1.0.0 and
                              		  is valid only for the configuration of Cisco Unified CME B-ACD call queue
                              		  scripts. Up to three menu options are allowed per call queue script. You can
                              		  use any of the allowable numbers in any order.

The call application voice aa-hunt command allows each of the menu options to be associated with
                              		  the pilot number of an ephone hunt group. The menu options are announced by the
                              		  en_bacd_options_menu.au audio file, which you can rerecord. When a caller
                              		  presses a number, the call will go to the pilot number of an ephone hunt group
                              		  so it can be transferred to one of the ephone hunt group’s ephone-dns. It will
                              		  not go to any other ephone hunt group. The order in which ephone-dns are
                              		  selected depends on the ephone hunt group’s search method, which is configured
                              		  with the ephone-hunt command, and whether an ephone-dn
                              		  is busy or not.

If only one menu option is configured, callers will hear a greeting
                              		  and be transferred directly to the pilot number of the corresponding ephone
                              		  hunt group. They do not have to enter a number.

The highest aa-hunt number will automatically be set to zero (0) for
                              		  the operator. In the following example, aa-hunt8 supports the menu option of 0
                              		  and 8.

```
call application voice queue aa-hunt1 1111
call application voice queue aa-hunt3 3333
call application voice queue aa-hunt8 8888
```

If a phone user presses 0 or 8, their call be sent to pilot number
                              		  3333.

For any configuration changes to take effect, you must reload the
                              		  Cisco CME B-ACD scripts.

## Examples

The following example associates three menu numbers with three pilot
                              		  numbers of three ephone hunt groups. Pilot number 1111 is for ephone hunt group
                              		  1 (sales); 2222 is for ephone hunt group 2 (customer service); and 3333 is for
                              		  ephone hunt group 3 (operator). If sales is selected from the AA menu, the call
                              		  will be transferred to 1111 and sent to ephone hunt group 1’s available
                              		  ephone-dns (2001, 2002, 2003, 2004, 2005, 2006).

```
Router(config)# ephone-hunt 1 peer Router(config-ephone-hunt)# pilot 1111 Router(config-ephone-hunt)# list 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010 Router(config)# ephone-hunt 2 peer Router(config-ephone-hunt)# pilot 2222 Router(config-ephone-hunt)# list 2001, 2002, 2003, 2004, 2005, 2006 Router(config)# ephone-hunt 3 peer Router(config-ephone-hunt)# pilot 3333 Router(config-ephone-hunt)# list 3001, 3002, 3003, 3004 Router(config)# call application voice queue flash:app-b-acd-x.x.x.x.tcl Router(config)# call application voice queue aa-hunt1 1111 Router(config)# call application voice queue aa-hunt2 2222 Router(config)# call application voice queue aa-hunt3 3333
```

### Related Commands

Command

Description

call application voice

Defines a name for a voice application and specifies the
                                          						location of the Tcl or VoiceXML document to load for this application.

call application voice aa-pilot

Associates an ephone hunt group with the Cisco CME basic
                                          						service’s AA script by declaring the group’s pilot number.

call application voice welcome-prompt

Assigns an audio file that is used by a Cisco CME B-ACD AA
                                          						script for the welcome greeting.

ephone-dn

Enters ephone-dn configuration mode for the purposes of
                                          						creating and configuring an extension for a Cisco IP phone line.

ephone-hunt

Enters ephone-hunt configuration mode for the purposes of
                                          						creating and configuring a hunt group for use in a Cisco CME system.

pilot

Defines the ephone-dn that callers dial to reach a Cisco
                                          						CME ephone hunt group.

## call application voice aa-name

Effective with Cisco IOS Release 12.3(14)T and later, the call application voice aa-name command is not available in Cisco IOS
                              		  software.

To associate the queue script for Cisco Unified CME basic automatic
                              		  call distribution (B-ACD) with the Cisco Unified CME B-ACD auto-attendant (AA)
                              		  script, use the call application voice aa-name command in global configuration mode. To remove the queue script and AA
                              		  script association, use the no form of this command.

call application voice application-name aa-name aa-script-name

no call application voice application-name aa-name aa-script-name

### Syntax Description

application-name

Application name given to the call queue script in the call application voice command .

aa-script-name

Application name given to the AA script in the call application voice command .

### Command Default

No call queue script and AA script association is
                              		  configured .

### Command Modes

Global configuration (config)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(11)XL

Cisco CME 3.2.1

This command was introduced.

12.3(14)T

Cisco CME 3.2.2

This command was integrated into Cisco IOS Release
                                          						12.3(14)T.

12.3(14)T

Cisco CME 3.3

This command was replaced with the param aa-name command.

### Usage Guidelines

This command is used only with with a version of the Cisco Unified
                              		  CME B-ACD script that is earlier than 2.1.0.0 and is valid only for the
                              		  configuration of Cisco Unified CME B-ACD call queue scripts. Only one AA script
                              		  can be associated with one call queue script.

For any configuration changes to take effect, you must reload the
                              		  Cisco CME B-ACD scripts.

## Examples

The following example associates a call queue script with an AA
                              		  script:

```
Router(config)# call application voice aa flash:app-b-acd-aa-x.x.x.x.tcl Router(config)# call application voice queue flash:app-b-acd-x.x.x.x.tcl Router(config)# call application voice queue aa-name aa
```

### Related Commands

Command

Description

call application voice

Defines a name for a voice application and specifies the
                                          						location of the Tcl or VoiceXML document to load for this application.

call application voice service-name

Associates a Cisco CME B-ACD AA script with a Cisco Unified
                                          						CME B-ACD call queue script.

## call application voice aa-pilot

Effective with Cisco IOS Release 12.3(14)T and later, the call application voice aa-pilot command is replaced by the param aa-pilot command. See the param aa-pilot command for more information.

To assign a pilot number to the Cisco Unified CME basic automatic
                              		  call distribution (B-ACD) service, use the call application voice aa-pilot command in global configuration mode. To remove the Cisco Unified CME
                              		  B-ACD pilot number, use the no form of this command.

call application voice application-name aa-pilot pilot-number

no call application voice application-name aa-pilot pilot-number

### Syntax Description

application-name

Application name given to the auto-attendant (AA) script in
                                          						the call application voice command .

pilot-number

Pilot number for Cisco CME B-ACD.

### Command Default

No Cisco Unified CME B-ACD pilot number is
                              		  configured .

### Command Modes

Global configuration (config)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(11)XL

Cisco CME 3.2.1

This command was introduced.

12.3(14)T

Cisco CME 3.2.2

This command was integrated into Cisco IOS Release
                                          						12.3(14)T.

12.3(14)T

Cisco CME 3.3

This command was replaced by the param aa-pilot command.

### Usage Guidelines

This command is used only with with a version of the Cisco CME B-ACD
                              		  script that is earlier than 2.1.0.0 and is valid only for the configuration of
                              		  Cisco CME B-ACD AA scripts. Only one pilot number can be used for each Cisco
                              		  Unified CME B-ACD service, and the voice ports handling AA must have dial peers
                              		  that will send calls to the pilot number.

For any configuration changes to take effect, you must reload the
                              		  Cisco Unified CME B-ACD scripts.

## Examples

The following example assigns 8005550100 as the pilot number to the
                              		  Cisco Unified CME B-ACD service. Included in this example is the dial-peer
                              		  configuration for the pilot number.

```
Router(config)# call application voice aa flash:app-b-acd-aa-x.x.x.x.tcl Router(config)# call application voice aa aa-pilot 8005550100 Router(config)# dial-peer voice 1000 pots Router(config)# incoming pilot number 8005550100 Router(config)# application aa Router(config)# direct-inward-dial Router(config)# port 1/0:23 Router(config)# forward digits-all Router(config)# call application voice aa aa-pilot 80055501
```

### Related Commands

Command

Description

call application voice

Defines a name for a voice application and specifies the
                                          						location of the Tcl or VoiceXML document to load for this application.

dial-peer voice

Defines a particular dial peer, specifies the method of
                                          						voice encapsulation, and enters dial-peer configuration mode.

ephone-dn

Enters ephone-dn configuration mode for the purposes of
                                          						creating and configuring an extension for a Cisco IP phone line.

ephone-hunt

Enters ephone-hunt configuration mode for the purposes of
                                          						creating and configuring a hunt group for use in a Cisco Unified CME system.

## call application voice call-retry-timer

Effective with Cisco IOS Release 12.3(14)T and later, the call application call-retry-timer command is replaced by the param call-retry-timer command. See the param call-retry-timer command for more information.

To assign the length of time that calls to Cisco Unified CME basic
                              		  automatic call distribution (B-ACD) must wait before attempting to transfer to
                              		  an ephone hunt group pilot number, use the call application voice call-retry-timer command in global configuration mode. To remove the retry time, use the no form of this command.

call application voice application-name call-retry-timer seconds

no call application voice application-name call-retry-timer seconds

### Syntax Description

application-name

Application name given to the auto-attendant (AA) script in
                                          						the call application voice command .

seconds

Number of seconds that a call must wait before attempting
                                          						to transfer an ephone hunt pilot number or voice-mail pilot number. The range
                                          						is from 5 to 30 seconds. The default is 15 seconds.

### Command Default

The retry interval is 15 seconds.

### Command Modes

Global configuration (config)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(11)XL

Cisco CME 3.2.1

This command was introduced.

12.3(14)T

Cisco CME 3.2.2

This command was integrated into Cisco IOS Release
                                          						12.3(14)T.

12.3(14)T

Cisco CME 3.3

This command was replaced by the param call-retry-timer command

### Usage Guidelines

This command is used only with with a version of the Cisco CME B-ACD
                              		  script that is earlier than 2.1.0.0 and is valid only for the configuration of
                              		  Cisco CME B-ACD AA scripts. The following sequence of events might occur:

- An outside call comes into a system configured with Cisco CME
                                 			 B-ACD.

- A menu option is selected that attempts to transfer the call to an
                                 			 ephone hunt group pilot number.

- All of the ephone hunt group’s ephone-dns are busy.

In that case, the call will wait in a queue for the period of time
                              		  set by the call application voice call-retry-timer command and retry to the pilot number.

For any configuration changes to take effect, you must reload the
                              		  Cisco Unified CME B-ACD scripts.

## Examples

The following example shows a configuration that allows outside calls
                              		  to Cisco CME B-ACD to retry an ephone hunt group pilot number every 30 seconds.
                              		  The example shows the configuration for one ephone hunt group, which is
                              		  presented by Cisco CME B-ACD menu as the sales department and uses a simple
                              		  configuration. If a caller selects the sales menu option
                              		  ( ephone-hunt 1 ) and all of the ephone-dns configured in the list command (1001, 1002, 1003, 1004) are
                              		  busy, the call will wait 30 seconds and then retry the pilot number (1111)
                              		  until either an ephone-dn becomes available or a configured amount of time has
                              		  elapsed (see the call application voice max-time-call-retry command).

```
Router(config)# ephone-hunt 1 peer Router(config-ephone-hunt)# pilot 1111 Router(config-ephone-hunt)# list 1001, 1002, 1003, 1004 Router(config)# call application voice aa flash:app-b-acd-aa-x.x.x.x.tcl Router(config)# call application voice aa call-retry-timer 30
```

### Related Commands

Command

Description

ephone-dn

Enters ephone-dn configuration mode for the purposes of
                                          						creating and configuring an extension for a Cisco IP phone line.

ephone-hunt

Enters ephone-hunt configuration mode for the purposes of
                                          						creating and configuring a hunt group for use in a Cisco Unified CME system.

call application voice

Defines a name for a voice application and specifies the
                                          						location of the Tcl or VoiceXML document to load for this application.

call application voice aa-hunt

Declares a Cisco Unified CME B-ACD menu number and
                                          						associates it with the pilot number of an ephone hunt group.

call application voice aa-pilot

Associates an ephone hunt group with the Cisco Unified CME
                                          						basic service’s AA script by declaring the group’s pilot number

call application voice max-time-call-retry

Assigns the maximum length of time for which calls to Cisco
                                          						Unified CME B-ACD can stay in a call queue.

## call application voice dial-by-extension-option

Effective with Cisco IOS Release 12.3(14)T and later, the call application dial-by-extension-option command is replaced by the param dial-by-extension-option command. See the param dial-by-extension-option command for more
                              		  information.

To enable direct extension access and set the access number for Cisco
                              		  Unified CME basic automatic call distribution (B-ACD), use the call application voice dial-by-extension-option command in global configuration mode. To disable direct dial extension
                              		  access and remove the access number, use the no form of this command.

call application voice application-name dial-by-extension number

no call application voice application-name dial-by-extension number

### Syntax Description

application-name

Application name given to the auto-attendant (AA) script in
                                          						the call application voice command .

number

The single digit that callers press to be able to enter an
                                          						extension number from the AA menu. The range is from 1 to 10. There is no
                                          						default.

### Command Default

Direct dial access is disabled. No access number is configured.

### Command Modes

Global configuration (config)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(11)XL

Cisco CME 3.2.1

This command was introduced.

12.3(14)T

Cisco CME 3.2.2

This command was integrated into Cisco IOS Release
                                          						12.3(14)T.

12.3(14)T

Cisco CME 3.3

This command was replaced by the param dial-by-extension-option command.

### Usage Guidelines

This command is used only with with a version of the Cisco Unified
                              		  CME B-ACD script that is earlier than 2.1.0.0 and is valid only for the
                              		  configuration of Cisco Unified CME B-ACD AA scripts. It enables the
                              		  en_bacd_enter_dest.au audio file. The default announcement says, “Please enter
                              		  the extension number you want to reach.” The call application voice dial-by-extension-option command also allows for the configuration of the
                              		  number that callers must press before they can enter the extension
                              		  number that they want to call.

Callers who select the extension access option can then dial any
                              		  extension. If they dial an ephone hunt group ephone-dn or pilot number, their
                              		  call will not be sent to the ephone hunt-group call queue.

## Examples

The following example configures Cisco CME B-ACD to include an option
                              		  that allows callers to press the number 4 so they can dial an extension number.

```
Router(config)# call application voice aa flash:app-b-acd-aa-x.x.x.x.tcl Router(config)# call application voice aa dial-by-extension 4
```

### Related Commands

Command

Description

call application voice

Defines a name for a voice application and specifies the
                                          						location of the Tcl or VoiceXML document to load for this application.

## call application voice drop-through-option

Cisco IOS Release 12.3(14)T and later releases support Cisco Unified
                              		  CME Basic Automatic Call Distribution (B-ACD) and Auto-Attendant (AA) Tcl
                              		  scripts version 2.1.0.0 and greater. In these releases, the
                              		  c all application voice drop-through-option command has been replaced by
                              		  the param drop-through-option command.

## call application voice drop-through-prompt

Cisco IOS Release 12.3(14)T and later releases support Cisco Unified
                              		  CME Basic Automatic Call Distribution (B-ACD) and Auto-Attendant (AA) Tcl
                              		  scripts version 2.1.0.0 and greater. In these releases, the call application voice drop-through-prompt command has been replaced by
                              		  the param drop-through-prompt command.

## call application voice handoff-string

Cisco IOS Release 12.3(14)T and later releases support Cisco Unified
                              		  CME Basic Automatic Call Distribution (B-ACD) and Auto-Attendant (AA) Tcl
                              		  scripts version 2.1.0.0 and greater. In these releases, the call application voice handoff-string command has been replaced by the param handoff-string command.

## call application voice max-extension-length

Cisco IOS Release 12.3(14)T and later releases support Cisco Unified
                              		  CME Basic Automatic Call Distribution (B-ACD) and Auto-Attendant (AA) Tcl
                              		  scripts version 2.1.0.0 and greater. In these releases, the call application voice max-extension-length command has been replaced by
                              		  the param max-extension-length command.

## call application voice max-time-call-retry

Effective with Cisco IOS Release 12.3(14)T and later, the call application voice max-time-call-retry command is replaced by the param max-time-call-retry command. See the param max-time-call-retry command for more information.

To assign the maximum length of time for which calls to Cisco Unified
                              		  CME basic automatic call distribution (B-ACD) can stay in a call queue, use the call application voice max-time-call-retry command in global configuration mode. To remove the maximum length of
                              		  time, use the no form of this command.

call application voice application-name max-time-call-retry seconds

no call application voice application-name max-time-call-retry seconds

### Syntax Description

application-name

Application name given to the auto attendant (AA) script in
                                          						the call application voice command .

seconds

Maximum length of time that the Cisco Unified CME B-ACD AA
                                          						script can keep redialing an ephone hunt group pilot number. The range is from
                                          						0 to 3600 seconds. The default is 600 seconds.

### Command Default

The default maximum length of time that calls can stay in a call queue is 600 seconds.

### Command Modes

Global configuration (config)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(11)XL

Cisco CME 3.2.1

This command was introduced.

12.3(14)T

Cisco CME 3.2.2

This command was integrated into Cisco IOS Release
                                          						12.3(14)T.

12.3(14)T

Cisco CME 3.3

This command was replaced by the param max-time-call-retry command.

### Usage Guidelines

This command is used only with with a version of the Cisco Unified
                              		  CME B-ACD script that is earlier than 2.1.0.0 and is valid only for the
                              		  configuration of Cisco Unified CME B-ACD AA scripts. The call application voice max-time-retry command allows you set a time limit for the redialing of pilot
                              		  numbers under the following circumstances:

- An outside call comes into a system configured with Cisco Unified
                                 			 CME B-ACD.

- A menu option is selected that transfers the call to an ephone
                                 			 hunt-group pilot number.

- All of the ephone hunt group’s ephone-dns are busy.

- The call is sent to a queue and tries the pilot number at
                                 			 intervals of time set by the call application voice call-retry-timer command.

When the time period set by the call application voice max- call-retry command expires, one of the following two events will occur:

- If a voice-mail pilot number has been configured in Cisco Unified
                                 			 CME and mail boxes for hunt group pilot numbers have been configured in a
                                 			 voice-mail application, calls will be transferred to voice mail.

- If voice mail has not been configured, a default message will be
                                 			 played that says, “We are unable to take your call at this time. Please try
                                 			 again at a later time. Thank you for calling.”

## Examples

In the following example, the length of time for which calls can try
                              		  to reach ephone hunt group 1 and ephone hunt group 2 is 90 seconds. If a caller
                              		  selects the AA menu option for either hunt group and all of its ephone-dns
                              		  configured in the list command are busy, the call will keep
                              		  retrying the ephone hunt group’s pilot number until one of the ephone-dns is
                              		  available or 90 seconds has elapsed. When 90 seconds elapses, the call will go
                              		  to voice mail.

```
Router(config)# ephone-hunt 1 peer Router(config-ephone-hunt)# pilot 1111 Router(config-ephone-hunt)# list 1001, 1002, 1003, 1004 Router(config)# ephone-hunt 2peer Router(config-ephone-hunt)# pilot 2222 Router(config-ephone-hunt)# list 2001, 2002, 2003, 2004 Router(config)# call application voice aa flash:app-b-acd-aa-x.x.x.x.tcl Router(config)# call application voice aa max-call-retry-timer 90
```

### Related Commands

Command

Description

call application voice

Defines a name for a voice application and specifies the
                                          						location of the Tcl or VoiceXML document to load for this application.

call application voice call-retry-timer

Assigns the length of time that calls to Cisco Unified CME
                                          						B-ACD must wait before attempting to transfer to an ephone hunt-group pilot
                                          						number or to voice mail.

call application voice max-time-vm-retry

Assigns the maximum number of times that calls to Cisco
                                          						Unified CME B-ACD can attempt to reach voice mail.

ephone-dn

Enters ephone-dn configuration mode for the purposes of
                                          						creating and configuring an extension for a Cisco IP phone line.

ephone-hunt

Enters ephone-hunt configuration mode for the purposes of
                                          						creating and configuring a hunt group for use in a Cisco Unified CME system.

## call application voice max-time-vm-retry

Cisco IOS Release 12.3(14)T and later releases support Cisco Unified
                              		  CME Basic Automatic Call Distribution (B-ACD) and Auto-Attendant (AA) Tcl
                              		  scripts version 2.1.0.0 and greater. In these releases, the call application voice max-time-vm-retry command has been replaced by
                              		  the param max-time-vm-retry command.

## call application voice number-of-hunt-grps

Effective with Cisco IOS Release 12.3(14)T and later, the call application voice number-of-hunt-grps command is replaced by the param number-of-hunt-grps command. See the param number-of-hunt-grps command for more information.

To declare the maximum number of ephone hunt-group menus supported by
                              		  Cisco Unified CME basic automatic call distribution (B-ACD), use the call application voice number-of-hunt-grps command in global configuration mode. To remove the maximum number of
                              		  ephone hunt-group menus supported by Cisco CME B-ACD, use the no form of this command.

call application voice application-name number-of-hunt-grps number

no call application voice application-name number-of-hunt-grps number

### Syntax Description

application-name

Application name given to the auto-attendant (AA) script in
                                          						the call application voice command .

number

Number of hunt groups used by the Cisco Unified CME B-ACD
                                          						AA script and call queue script. The range is from 1 to 3. The default is 3.

### Command Default

Three ephone hunt-group menus are supported by Cisco CME
                              		  B-ACD .

### Command Modes

Global configuration (config)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(11)XL

Cisco CME 3.2.1

This command was introduced.

12.3(14)T

Cisco CME 3.2.2

This command was integrated into Cisco IOS Release
                                          						12.3(14)T.

12.3(14)T

Cisco CME 3.3

This command was replaced by the param number-of-hunt-grps command.

### Usage Guidelines

This command is used only with with a version of the Cisco Unified
                              		  CME B-ACD script that is earlier than 2.1.0.0 and is valid only for the
                              		  configuration of Cisco Unified CME B-ACD AA scripts. The number argument declares the number of ephone
                              		  hunt groups only. The menu option for direct extension access (see the call application voice dial-by-extension-option command) is not included.

## Examples

The following example configures a Cisco Unified CME B-ACD call queue
                              		  script to use three ephone hunt groups and one direct extension access number,
                              		  making the number argument in the call application voice number-of-hunt-grps equal to 3. The ephone-hunt command is used to configure the three ephone hunt groups.
                              		  The call application voice dial-by-extension-option command is used to enable
                              		  direct extension access and set the access number to 1.

```
Router(config)# ephone-hunt 1 peer Router(config-ephone-hunt)# pilot 1111 Router(config-ephone-hunt)# list 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010 Router(config)# ephone-hunt 2 peer Router(config-ephone-hunt)# pilot 2222 Router(config-ephone-hunt)# list 2001, 2002, 2003, 2004, 2005, 2006 Router(config-ephone-hunt)# final 9000 Router(config)# ephone-hunt 3 peer Router(config-ephone-hunt)# pilot 3333 Router(config-ephone-hunt)# list 3001, 3002, 3003, 3004 Router(config)# call application voice aa flash:app-b-acd-aa-x.x.x.x.tcl Router(config)# call application voice aa dial-by-extension 1 Router(config)# call application voice aa number-of-hunt-grps 3
```

### Related Commands

Command

Description

call application voice

Defines a name for a voice application and specifies the
                                          						location of the Tcl or VoiceXML document to load for this application.

call application voice dial-by-extension-option

Enables direct extension access and sets the access number
                                          						for Cisco CME B-ACD.

ephone-hunt

Enters ephone-hunt configuration mode for the purposes of
                                          						creating and configuring a hunt group for use in a Cisco CME system.

## call application voice queue-len

Effective with Cisco IOS Release 12.3(14)T and later, the call application queue-len command is replaced by the param queue-len command. See the param queue-len command for more information.

To set the maximum number of calls allowed for each ephone hunt
                              		  group’s call queue that is used by Cisco Unified CME basic automatic call
                              		  distribution (B-ACD), use the call application voice queue-len command in global configuration mode. To remove the queue-length setting,
                              		  use the no form of this command.

call application voice application-name queue-len number

no call application voice application-name queue-len number

### Command Default

application-name

Application name given to the call queue script in the call application voice command .

number

Number of calls that can be waiting in each ephone hunt
                                          						group’s queue. The range is dependent on your hardware configuration. The range
                                          						is from 1 to 30. The default is 10.

### Command Default

Thirty calls are allowed in each call queue.

### Command Modes

Global configuration (config)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(11)XL

Cisco CME 3.2.1

This command was introduced.

12.3(14)T

Cisco CME 3.2.2

This command was integrated into Cisco IOS Release
                                          						12.3(14)T.

12.3(14)T

Cisco CME 3.3

This command was replaced by the param queue-len command.

### Usage Guidelines

This command is used only with with a version of the Cisco Unified
                              		  CME B-ACD script that is earlier than 2.1.0.0 and is valid only for the
                              		  configuration of Cisco Unified CME B-ACD call queue scripts. The following
                              		  sequence of events might occur:

- An outside call comes into a system configured with Cisco Unified
                                 			 CME B-ACD.

- A menu option is selected that transfers the call to an ephone
                                 			 hunt-group pilot number.

- All of the ephone hunt group’s ephone-dns are busy.

In that case, the call will be sent to a queue for that individual
                              		  hunt group. The number of calls that each ephone hunt group can hold in its
                              		  queue is configured by the call application voice queue-len command.

In the following configuration example, ephone hunt group 1 supports
                              		  two ephone-dns; ephone hunt group 2 supports three ephone-dns; and the queue
                              		  length is 10 for both ephone hunt groups:

```
ephone-hunt 1 peer
 pilot 1111
 list 1001, 1002
ephone-hunt 2 peer
 pilot 2222
 list 2001, 2002, 2003
call application voice queue flash:app-b-acd-x.x.x.x.tcl
call application voice callqueuescriptfilename queue-len 10
```

If ephone hunt group 1’s ephone-dns are busy, ten more calls can be
                              		  made to ephone hunt group 1. During that time, the calls in the queue would
                              		  periodically retry the pilot numbers ( call application voice max-time-retry-timer command) and receive secondary greetings
                              		  ( call application voice second-greeting-time command). If none of the calls has hung up or connected to an
                              		  ephone-dn, the eleventh caller would hear the en_bacd_disconnect.au message and
                              		  a busy signal. The default message is, “We are unable to take your call at this
                              		  time. Please try again at a later time. Thank you for calling.” Includes a
                              		  four-second pause after the message.

For ephone hunt group 2, three calls can be connected to ephone-dns
                              		  2001, 2002, and 2003, and ten calls can be waiting in ephone hunt group 2’s
                              		  queue. If the status remains unchanged, the fourteenth caller hears the
                              		  disconnect message and a busy signal. But if one of the earlier calls
                              		  disconnects (either by leaving the queue or by ending a call), the fourteen
                              		  call enters the queue.

The maximum number of calls allowed in the queues of ephone hunt
                              		  groups must be based on the number of ports or trunks available. For example,
                              		  if you had 20 foreign exchange office (FXO) ports and two ephone hunt groups,
                              		  you could configure a maximum of ten calls per ephone hunt-group queue with the call application voice queue-len 10 command. You could use the same configuration
                              		  if you had a single T1 trunk, which supports 23 channels.

## Examples

The following example configures a Cisco Unified CME B-ACD call queue
                              		  script to allow a maximum of 12 calls to wait in each ephone hunt group’s
                              		  calling queue for ephone-dns to become available:

```
Router(config)# call application voice queue flash:app-b-acd-x.x.x.x.tcl Router(config)# call application voice queue queue-len 12
```

### Related Commands

Command

Description

call application voice

Defines a name for a voice application and specifies the
                                          						location of the Tcl or VoiceXML document to load for this application.

call application voice call-retry-timer

Assigns the length of time that calls to Cisco CME B-ACD
                                          						must wait before attempting to transfer to an ephone hunt-group pilot number or
                                          						to voice mail.

ephone-dn

Enters ephone-dn configuration mode for the purposes of
                                          						creating and configuring an extension for a Cisco IP phone line.

ephone-hunt

Enters ephone-hunt configuration mode for the purposes of
                                          						creating and configuring a hunt group for use in a Cisco CME system.

## call application voice queue-manager-debugs

Effective with Cisco IOS Release 12.3(14)T and later, the call application queue-manager-debugs command is replaced by the param queue-manager-debugs command. See the param aa-hunt command for more information.

To enable or disable the collection of call queue debug information
                              		  from Cisco CallManager Express (Cisco CME) basic automatic call distribution
                              		  (B-ACD), use the call application voice queue-manager-debugs command in global configuration mode. To remove the current setting, use
                              		  the no form of this command with the keyword that
                              		  was used in the previous occurrence of the call application voice queue-manager-debugs command .

call application voice application-name queue-manager-debugs [ 0 | 1 ]

no call application voice application-name queue-manager-debugs [ 0 | 1 ]

### Syntax Description

application-name

Application name given to the call queue script in the call application voice command .

0

Disables debugging.

1

Enables debugging.

### Command Default

The collection of call queue debug information from Cisco CME B-ACD
                              		  is disabled.

### Command Modes

Global configuration (config)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(11)XL

Cisco CME 3.2.1

This command was introduced.

12.3(14)T

Cisco CME 3.2.2

This command was integrated into Cisco IOS Release
                                          						12.3(14)T.

12.3(14)T

Cisco CME 3.3

This command was replaced by the param queue-manager-debugs command.

### Usage Guidelines

This command is used only with with a version of the Cisco CME B-ACD
                              		  script that is earlier than 2.1.0.0 and is valid only for the configuration of
                              		  Cisco CME B-ACD call queue scripts. It enables the collection of data regarding
                              		  call queue activity. It is used in conjunction with the debug voip ivr script command. Both commands must be enabled at the same time.

For any configuration changes to take effect, you must reload the
                              		  Cisco CME B-ACD scripts.

## Examples

The following example configures a Cisco CME B-ACD call queue script
                              		  to enable debugging for the collection of data for the debug voip ivr script command:

```
Router(config)# call application voice queue flash:app-b-acd-x.x.x.x.tcl Router(config)# call application voice queue queue-manager-debugs 1
```

### Related Commands

Command

Description

call application voice

Defines a name for a voice application and specifies the
                                          						location of the Tcl or VoiceXML document to load for this application.

debug voip ivr script

Display debugging messages for IVR scripts.

## call application voice second-greeting-time

Effective with Cisco IOS Release 12.3(14)T and later, the call application voice second-greeting-time command is replaced by the param second-greeting-time command. See the param second-greeting-time command for more information.

To set the delay before the second greeting is played after a caller
                              		  joins a Cisco Unified CME basic automatic call distribution (B-ACD) calling
                              		  queue and set the interval of time at which the second-greeting message is
                              		  repeated, use the call application voice second-greeting-time command in global configuration mode. To remove the second-greeting time,
                              		  use the no form of this command.

call application voice application-name second-greeting-time seconds

no call application voice application-name second-greeting-time seconds

### Syntax Description

application-name

Application name given to the auto-attendant (AA) script in
                                          						the call application voice command .

seconds

Amount of time that second-greeting message must wait
                                          						before it can be played. The range is from 30 to 120 seconds. The default is 60
                                          						seconds.

### Command Default

The second-greeting delay time is 60 seconds.

### Command Modes

Global configuration (config)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(11)XL

Cisco CME 3.2.1

This command was introduced.

12.3(14)T

Cisco CME 3.2.2

This command was integrated into Cisco IOS Release
                                          						12.3(14)T.

12.3(14)T

Cisco CME 3.3

This command was replaced by the param second-greeting-time command.

### Usage Guidelines

This command is used only with with a version of the Cisco Unified
                              		  CME B-ACD script that is earlier than 2.1.0.0 and is valid only for the
                              		  configuration of Cisco Unified CME B-ACD AA scripts. A second greeting is an
                              		  audio message of up to 15 seconds in length. The default announcement is, “All
                              		  agents are currently busy assisting other customers. Continue to hold for
                              		  assistance. Someone will be with you shortly.” The second-greeting message is
                              		  only presented to callers waiting in a CME B-ACD call queue.

The second-greeting time is clocked when the second-greeting message
                              		  begins, not after it ends. For example, if the second greeting were 15 seconds
                              		  in length and the configured second-greeting time were 70 seconds, the greeting
                              		  would begin every 70 seconds, not 85 seconds as if to allow for the 15-second
                              		  message.

For any configuration changes to take effect, you must reload the
                              		  Cisco CME B-ACD scripts.

## Examples

The following example configures a Cisco Unified CME B-ACD AA script
                              		  to allow a second-greeting message to be repeated every 50 seconds as long as a
                              		  call is in a call queue.

```
Router(config)# call application voice aa flash:app-b-acd-aa-x.x.x.x.tcl Router(config)# call application voice AAscriptfilename second-greeting-time 50
```

### Related Commands

Command

Description

call application voice

Defines a name for a voice application and specifies the
                                          						location of the Tcl or VoiceXML document to load for this application.

ephone-dn

Enters ephone-dn configuration mode for the purposes of
                                          						creating and configuring an extension for a Cisco IP phone line.

ephone-hunt

Enters ephone-hunt configuration mode for the purposes of
                                          						creating and configuring a hunt group for use in a Cisco CME system.

## call application voice service-name

Cisco IOS Release 12.3(14)T and later releases support Cisco CME
                              		  Basic Automatic Call Distribution (B-ACD) and Auto-Attendant (AA) Tcl scripts
                              		  version 2.1.0.0 and greater. In these releases, the call application voice service-name command has been replaced by the param service-name command.

## call application voice voice-mail

Effective with Cisco IOS Release 12.3(14)T and later, the call application voice voice-mail command is replaced by the param voice-mail command. See the param voice-mail command for more information.

To assign a pilot number for the Cisco Unified CME basic automatic
                              		  call distribution (B-ACD) service’s voice mail, use the call application voice voice-mail command in global configuration mode. To remove the voice-mail pilot
                              		  number, use the no form of the command.

call application voice application-name voice-mail number

no call application voice application-name voice-mail number

### Syntax Description

application-name

Application name given to the auto attendant (AA) script in
                                          						the call application voice command .

number

Pilot number of the voice mail to which calls to Cisco CME
                                          						B-ACD will be transferred.

### Command Default

No voice-mail pilot number is configured for Cisco Unified CME
                              		  B-ACD .

### Command Modes

Global configuration (config)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(11)XL

Cisco CME 3.2.1

This command was introduced.

12.3(14)T

Cisco CME 3.2.2

This command was integrated into Cisco IOS Release
                                          						12.3(14)T.

12.3(14)T

Cisco CME 3.3

This command was replaced by the param voice-mail command.

### Usage Guidelines

This command is used only with with a version of the Cisco Unified
                              		  CME B-ACD script that is earlier than 2.1.0.0 and is valid only for the
                              		  configuration of Cisco Unified CME B-ACD AA scripts. Only one pilot number is
                              		  allowed per Cisco CME B-ACD service. Calls to the service will be sent to this
                              		  voice mail number.

For any configuration changes to take effect, you must reload the
                              		  Cisco CME B-ACD scripts.

## Examples

The following example configures a Cisco Unified CME B-ACD voice-mail
                              		  pilot number as 5000.

```
Router(config)# call application voice aa flash:app-b-acd-aa-x.x.x.x.tcl Router(config)# call application voice aa voice-mail 5000
```

### Related Commands

Command

Description

call application voice

Defines a name for a voice application and specifies the
                                          						location of the Tcl or VoiceXML document to load for this application.

## call application voice welcome-prompt

Effective with Cisco IOS Release 12.3(14)T and later, the call application voice welcome-prompt command is replaced by the param welcome-prompt command. See the param welcome-prompt command for more information.

To assign an audio file that is used by the Cisco Unified CME basic
                              		  automatic call distribution (B-ACD) auto-attendant (AA) script for the welcome
                              		  greeting, use the call application welcome-prompt command in global configuration mode. To remove the audio file assignment,
                              		  use the no form of this command.

call application voice application-name welcome-prompt _ audio-filename

no call application voice application-name welcome-prompt _ audio-filename

### Syntax Description

application-name

Application name given to the AA script in the call application voice command .

_ audio-filename

Filename of the welcome greeting to be played when callers
                                          						first reach the Cisco Unified CME B-ACD, preceded by the underscore (_)
                                          						character. The filename must not have a language code prefix, such as “en,” for
                                          						English.

### Command Default

The welcome audio file downloaded with Cisco Unified CME B-ACD is
                              		  used for the welcome prompt .

### Command Modes

Global configuration (config)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(11)XL

Cisco CME 3.2.1

This command was introduced.

12.3(14)T

Cisco CME 3.2.2

This command was integrated into Cisco IOS Release
                                          						12.3(14)T.

12.3(14)T

Cisco CME 3.3

This command was replaced by the param welcome-prompt command.

### Usage Guidelines

This command is used only with with a version of the Cisco Unified
                              		  CME B-ACD script that is earlier than 2.1.0.0 and is valid only for the
                              		  configuration of Cisco CME B-ACD AA scripts. The welcome greeting is the
                              		  initial AA response to a caller. The default audio file used is
                              		  en_bacd_welcome.au, which is is downloaded with Cisco CME B-ACD and announces,
                              		  “Thank you for calling,” and includes a two-second pause after the message.

The filename must be preceded by an underscore (_) character. In
                              		  addition, it must not contain a language-code prefix, such as “en” for English.
                              		  For example, for en_bacd_welcome.au, you must configure welcome-prompt _bacd_welcome.au instead of welcome-prompt _en_bacd_welcome.au .

For any configuration changes to take effect, you must reload the
                              		  Cisco CME B-ACD scripts.

## Examples

The following example sets file name en_welcome.au as the welcome
                              		  greeting for Cisco Unified CME B-ACD:

```
Router(config)# call application voice aa flash:app-b-acd-aa-x.x.x.x.tcl Router(config)# call application voice aa welcome-prompt _bacd_welcome_2.au
```

### Related Commands

Command

Description

call application voice

Defines a name for a voice application and specifies the
                                          						location of the Tcl or VoiceXML document to load for this application.

call application voice aa-name

Associates a Cisco CME B-ACD call queue script with a Cisco
                                          						Unified CME B-ACD AA script

call application voice service-name

Associates a Cisco CME B-ACD AA script with a Cisco Unified
                                          						CME B-ACD call queue script.

## callback (voice emergency response settings)

To route an E911 callback to another number (for example, the company
                              		  operator) if the callback cannot find the last 911 caller associated to the
                              		  ELIN, use the callback command in voice emergency response
                              		  settings configuration mode. This command is optional.

callback number

no callback

### Syntax Description

number

Identifier of the E.164 default number to contact if a 911
                                          						callback fails.

### Command Default

A callback number is not defined.

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

Use this command to specify the default number to contact if a 911
                              		  callback cannot find the last 911 caller associated with an ELIN. If no default
                              		  callback number is configured, and the expiry time is exceeded, the 911
                              		  operator may hear a reorder tone or be incorrectly routed.

## Examples

In this example, the ELIN (4085550101) defined in the voice emergency
                              		  response settings configuration is used if the 911 caller’s IP phone address
                              		  does not match any of the voice emergency response locations. After the 911
                              		  call is placed to the PSAP, the PSAP has 120 minutes to call back 408-555-0101
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

elin

E.164 number used as the default ELIN if no matching ERL to
                                          						the 911 caller’s IP phone address is found.

expiry

Number of minutes a 911 call is associated to an ELIN in
                                          						case of a callback from the 911 operator.

logging

Syslog informational message printed to the console every
                                          						time an emergency call is made.

voice emergency response settings

Creates a tag for identifying settings for E911 behavior.

## caller-id

To specify whether to pass the local caller ID or the original caller
                              		  ID with calls from an extension in Cisco Unified CME that is using loopback,
                              		  use the caller id command in ephone-dn configuration mode. To return to the default, use the no form of this command.

caller-id { local | passthrough }

no caller-id { local | passthrough }

### Syntax Description

local

Local caller ID for redirected calls.

passthrough

Original caller ID. Default.

### Command Default

Default is passthrough .

### Command Modes

Ephone-dn configuration (config-ephone)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ3

Cisco CME 3.0

This command was introduced.

12.3(4)T

Cisco CME 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

This command is valid only for ephone-dns that are being used for
                              		  loopback.

This command with the local keyword is applied as follows:

- For transferred calls, caller ID is provided by the original
                                 			 caller-ID information source, such as from a separate loopback-dn that handles
                                 			 inbound calls or from a public switched telephone network interface.

- For forwarded calls, caller ID is provided by the original
                                 			 caller-ID information source or, for local IP phones, is extracted from the
                                 			 redirected information associated with the call.

This command with the passthrough keyword is applied as follows:

- For transferred calls, the caller ID is provided by the original
                                 			 caller-ID information that is obtained from the inbound side of the
                                 			 loopback-dn.

- For forwarded calls, the caller ID is provided by the original
                                 			 caller-ID information of the incoming call.

## Examples

The following example selects local caller ID for redirected calls:

```
Router(config)# ephone-dn 1 Router(config-ephone-dn)# number 5001 Router(config-ephone-dn)# loopback-dn 15 forward 4 Router(config-ephone-dn)# caller-id local Router(config-ephone-dn)# no huntstop
```

### Related Commands

Command

Description

loopback-dn

Creates a virtual loopback voice port (loopback-dn) to
                                          						establish a demarcation point for VoIP voice calls and supplementary services.

## caller-id block (ephone-dn and ephone-dn-template)

To specify caller-ID blocking for outbound calls from a specific
                              		  extension, use the caller id block command in ephone-dn or ephone-dn-template configuration mode. To disable
                              		  caller-ID blocking for outbound calls, use the no form of this command.

caller-id block

no caller-id block

### Syntax Description

This command has no arguments or keywords.

### Command Default

Caller-ID display is not blocked on calls originating from a Cisco
                              		  Unified IP phone.

### Command Modes

Ephone-dn configuration Ephone-dn-template configuration

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

Cisco Unified CME 4.0

This command was made available in ephone-dn-template
                                          						configuration mode.

12.4(9)T

Cisco Unified CME 4.0

This command in ephone-dn-template configuration mode was
                                          						integrated into Cisco IOS Release 12.4(9)T.

### Usage Guidelines

This command sets caller-ID blocking for outbound calls originating
                              		  from a specific extension (ephone-dn). This command requests the far-end
                              		  gateway device to block the display of the calling party information for calls
                              		  received from the ephone-dn that is being configured. This command does not
                              		  affect the ephone-dn calling party information display for inbound calls
                              		  received by the ephone-dn.

If you want caller-ID name or number to be available on local calls
                              		  but not on external calls, use the clid strip name command or the clid strip command in dial-peer configuration mode to
                              		  remove caller-ID name or number from calls to VoIP. In this case, do not also
                              		  use the caller-id block command, which blocks caller-ID information
                              		  on all calls.

If you use an ephone-dn template to apply a command to an ephone-dn
                              		  and you also use the same command in ephone-dn configuration mode for the same
                              		  ephone-dn, the value that you set in ephone-dn configuration mode has priority.

## Examples

The following example shows how to set caller-ID blocking for the
                              		  directory number 5001:

```
Router(config)# ephone-dn 1 Router(config-ephone-dn)# number 5001 Router(config-ephone-dn)# caller-id block
```

The following example uses an ephone-dn template to set caller-ID
                              		  blocking for the directory number 5001:

```
Router(config)# ephone-dn-template 5 Router(config-ephone-dn-template)# caller-id block Router(config-ephone-dn-template)# exit Router(config)# ephone-dn 1 Router(config-ephone-dn)# number 5001 Router(config-ephone-dn)# ephone-dn-template 5
```

### Related Commands

Command

Description

clid strip

Prevents display of caller-ID number on calls to VoIP.

clid strip name

Prevents display of caller-ID name on calls to VoIP.

ephone-dn-template (ephone-dn)

Applies ephone-dn template to an ephone dn.

## caller-id block (voice register template)

To enable caller-ID blocking for outbound calls from a specific SIP
                              		  phone, use the caller id block command in voice register template configuration mode. To disable
                              		  caller-ID blocking, use the no form of this command.

caller-id block

no caller-id block

### Syntax Description

This command has no arguments or keywords.

### Command Default

Caller ID blocking is disabled.

### Command Modes

Voice register template configuration (config-register-temp)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4

This command was introduced.

12.4(11)XJ

Cisco Unified CME 4.1

This command was removed.

12.4(15)T

Cisco Unified CME 4.1

This command was removed in Cisco IOS Release 12.4(15)T.

### Usage Guidelines

This command sets caller-ID blocking for outbound calls originating
                              		  from any SIP phone that uses the specified template. This command requests the
                              		  far-end gateway device to block the display of the calling party information
                              		  for calls received from the specified SIP phone. This command does not affect
                              		  the calling party information displayed for inbound calls received by the SIP
                              		  phone. To apply a template to a SIP phone, use the template command in voice register pool
                              		  configuration mode.

## Examples

The following example shows how to enable caller-ID blocking in
                              		  template 1:

```
Router(config)# voice register template 1 Router(config-register-temp)# caller-id block
```

### Related Commands

Command

Description

anonymous block (voice register template)

Enables anonymous call blocking in a SIP phone template.

template (voice register pool)

Applies a template to a SIP phone.

voice register template

Enters voice register template configuration mode and
                                          						defines a template of common parameters for SIP phones.

## caller-id block code (telephony-service)

To set a code for a user to dial to block the display of caller ID on
                              		  selected outgoing calls from Cisco IP phones, use the caller-id block code command in telephony-service configuration mode. To remove the
                              		  code, use the no form of this command.

caller-id block code code-string

no caller-id block code

### Syntax Description

code-string

Character string to dial to enable blocking of caller ID
                                          						display on selected outgoing calls. The first character must be an asterisk (*)
                                          						and the remaining characters must be digits. The string can contain a maximum
                                          						of 16 characters.

### Command Default

No caller-ID blocking code is defined.

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

Once the caller-ID blocking code has been defined using this command,
                              		  phone users should enter the caller-ID blocking code before dialing any call on
                              		  which they want their caller ID not to display.

## Examples

The following example sets a caller-ID blocking code of *4321:

```
Router(config)# telephony-service Router(config-telephony)# caller-id block code *4321
```

### Related Commands

Command

Description

telephony-service

Enters telephony-service configuration mode.

## call-feature-uri

To specify the uniform resource identifier (URI) for soft keys on SIP
                              		  phones registered to a Cisco Unified CME router, use the call-feature-uri command in voice register global configuration mode. To remove
                              		  a URI association, use the no form of this command.

call-feature-uri { cfwdall | gpickup | pickup } service-uri

no call-feature-uri cfwdall { cfwdall | gpickup | pickup }

### Syntax Description

cfwdall

Call Forward All (CfwdAll) soft key.

gpickup

Group Pickup (GPickUp) soft key.

pickup

Local Pickup (PickUp) soft key.

service-uri

URI that is requested when the specified soft key is
                                          						pressed.

### Command Default

No URI is associated with the soft key.

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

12.4(22)YB

Cisco Unified CME 7.1

The gpickup and pickup keywords were added.

12.4(24)T

Cisco Unified CME 7.1

This command has been integrated into Cisco IOS Release
                                          						12.4(24)T.

### Usage Guidelines

This command updates the service URI for soft keys in the
                              		  configuration file that is downloaded from the Cisco Unified CME router to the
                              		  SIP phones during phone registration.

For Call Forward All, this URI and the call forward number is sent to
                              		  Cisco Unified CME when a user enables Call Forward All from the phone using the
                              		  CfwdAll soft key.

After you configure this command, restart the phone by using the reset or restart command.

This command is not supported on the Cisco Unified IP Phone 7905,
                              		  7912, 7940, or 7960.

## Examples

The following example shows how to specify the URI for the call
                              		  forward all soft key:

```
Router(config)# voice register global Router(config-register-global)# call-feature-uri cfwdall http://10.10.10.11/cfwdall
```

### Related Commands

Command

Description

call-forward b2bua all

Enables call forwarding for a SIP back-to-back user agent
                                          						(B2BUA) so that all incoming calls are forwarded to another extension.

reset (voice register global)

Performs a complete reboot of all SIP phones associated
                                          						with a Cisco Unified CME router.

reset (voice register pool)

Performs a complete reboot of one phone associated with a
                                          						Cisco Unified CME router.

restart (voice register)

Performs a fast restart of one or all SIP phones associated
                                          						with a Cisco Unified CME router.

service directed-pickup

Enables Directed Call Pickup and modifies the function of
                                          						the PickUp and GPickUp soft keys.

## call-forward

To globally apply dialplan-pattern expansion to redirecting numbers
                              		  for extension numbers associated with SCCP IP phones in Cisco Unified CME, use
                              		  the call-forward system command in telephony-service configuration mode. To disable the call-forward system command, use the no form of this command.

call-forward system redirecting-expanded

no call-forward system redirecting-expanded

### Syntax Description

system

Call forward system parameter.

redirecting-expanded

Expand redirecting extensions to an E.164 number.

### Command Default

The redirecting number is not expanded.

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

Use this command to apply dialplan-pattern expansion on a per-system
                              		  basis to individual nonSIP redirecting numbers, including original called and
                              		  last reroute numbers, in a Cisco Unified CME system.

When A calls B, and B forwards the call to C; B is the original
                              		  called number and the last reroute number. If C then forwards or transfers the
                              		  call to another number, C becomes the original called number and the last
                              		  reroute number. The dial-plan pattern expansion is applied to both redirecting
                              		  numbers. Once the number is expanded, it remains expanded during the entire
                              		  call instance.

The dial-plan pattern to be matched must be configured using the dialplan-pattern command.

## Examples

The following example shows how to create a dialplan-pattern for
                              		  expanding calling numbers to an E.164 number and to also apply the expansion
                              		  globally to redirecting numbers.

```
Router(config)# voice register global Router(config-register-global)# dialplan-pattern 1 5105550... extension-length 5 Router(config-register-global)# call-forward system redirecting-expanded
```

### Related Commands

Command

Description

dialplan-pattern

Create global prefix for expanding extension numbers of
                                          						forward-to and transfer-to targets.

show telephony-service dial-peer

Displays dial peer information for extensions in a Cisco
                                          						Unified CME system.

## call-forward (voice register)

To globally apply dialplan-pattern expansion to redirecting numbers
                              		  for extension numbers associated with SIP IP phones in Cisco Unified CME, use
                              		  the call-forward system command in voice register global configuration mode. To disable
                              		  the call-forward system command, use the no form of this command.

call-forward system redirecting-expanded

no call-forward system redirecting-expanded

### Syntax Description

system

Call forward system parameter.

redirecting-expanded

Redirecting extension is to be expanded to an E.164 number.

### Command Default

The redirecting number is not expanded.

### Command Modes

Voice register global configuration (config-register-global)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)XC

Cisco Unified CME 4.0

This command was introduced.

12.4(9)T

Cisco Unified CME 4.0

This command was integrated into Cisco IOS Release 12.4(9).

### Usage Guidelines

Use this command to apply dialplan-pattern expansion on a per-system
                              		  basis to individual SIP redirecting numbers, including original called and last
                              		  reroute numbers, in Cisco Unified CME.

When A calls B, and B forwards the call to C; B is the original
                              		  called number and the last reroute number. If C then forwards or transfers the
                              		  call to another number, C becomes the original called number and the last
                              		  reroute number. The dial-plan pattern expansion is applied to both redirecting
                              		  numbers. Once the number is expanded, it remains expanded during the entire
                              		  call instance.

This command supports call forward using B2BUA only.

The dial-plan pattern to be matched must be configured using the dialplan-pattern command.

## Examples

The following example shows how to create a dialplan-pattern for
                              		  expanding calling numbers of SIP phones to an E.164 number and to also apply
                              		  the expansion globally to SIP redirecting numbers.

```
Router(config)# voice register global Router(config-register-global)# dialplan-pattern 1 5105550... extension-length 5 Router(config-register-global)# call-forward system redirecting-expanded
```

### Related Commands

Command

Description

dialplan-pattern (voice register)

Create global prefix for expanding extension numbers of
                                          						forward-to and transfer-to targets if the target is an extension on a SIP
                                          						phone.

show voice register dial-peer

Displays dial peer information for extensions in a Cisco
                                          						Unified CME system.

## call-forward all

To configure call forwarding so that all incoming calls to a
                              		  directory number are forwarded to another directory number, use the call forward all command in ephone-dn or ephone-dn-template configuration mode. To disable
                              		  call forwarding, use the no form of this command.

call-forward all directory-number

no call-forward all

### Syntax Description

directory number

Directory number to which calls are forwarded. Represents a
                                          						fully qualified E.164 number.

### Command Default

Call forwarding for all calls is not set.

### Command Modes

Ephone-dn configuration (config-ephone-dn) Ephone-dn-template configuration (config-ephone-dn-template)

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

12.4(4)XC

Cisco Unified CME 4.0

This command was made available in ephone-dn-template
                                          						configuration mode.

12.4(9)T

Cisco Unified CME 4.0

This command in ephone-dn-template configuration mode was
                                          						integrated into Cisco IOS Release 12.4(9)T.

### Usage Guidelines

The call forwarding mechanism applies to the individual directory
                              		  number and cannot be configured for individual Cisco Unified IP phones.

If you use an ephone-dn template to apply a command to an ephone-dn
                              		  and you also use the same command in ephone-dn configuration mode for the same
                              		  ephone-dn, the value that you set in ephone-dn configuration mode has priority.

## Examples

The following example shows how to set call forwarding of all calls
                              		  on directory number 5001 to directory number 5005. All incoming calls destined
                              		  for extension 5001 are forwarded to another Cisco IP phone with the extension
                              		  number 5005:

```
Router(config)# ephone-dn 1 Router(config-ephone-dn)# number 5001 Router(config-ephone-dn)# call-forward all 5005
```

The following example uses an ephone-dn template to forward all calls
                              		  for extension 5001 to extension 5005.

```
Router(config)# ephone-dn-template 3 Router(config-ephone-dn-template)# call-forward all 5005 Router(config-ephone-dn-template)# exit Router(config)# ephone-dn 1 Router(config-ephone-dn)# number 5001 Router(config-ephone-dn)# ephone-dn-template 3
```

### Related Commands

Command

Description

call forward busy

Configures call forwarding to another number when a Cisco
                                          						Unified IP phone is busy.

call forward noan

Configures call forwarding to another number when no answer
                                          						is received from a Cisco Unified IP phone.

ephone dn-template (ephone-dn)

Applies template to ephone-dn.

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

Feature is disabled.

### Command Modes

Voice register dn configuration (config-register-dn) Voice register pool configuration (config-register-pool)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was introduced.

12.4(11)XJ

Cisco Unified CME 4.1

This command was removed from voice register pool
                                          						configuration mode for Cisco Unified CME only.

12.4(15)T

Cisco Unified CME 4.1

Command with modifications was integrated into Cisco IOS
                                          						release 12.4(15)T.

### Usage Guidelines

This command in voice register dn configuration mode applies the call
                              		  forward mechanism to a individual SIP extension in Cisco Unified CME or Cisco
                              		  Unified SIP SRST. This command in voice register pool configuration mode is for
                              		  Cisco Unified SIP SRST only and applies to SIP IP phones on which the extension
                              		  appears.

If this command is configured in both the voice register dn and voice
                              		  register pool configuration modes, the configuration under voice register dn
                              		  takes precedence.

We recommend that you do not use this command to configure a SIP
                              		  extension or SIP IP phone that is a member of a hunt group. If this command is
                              		  configured for a member of a hunt group, remove the phone from any hunt group
                              		  to which it is assigned to avoid forwarding calls to all phones in the hunt
                              		  group.

The call-forward b2bua all command takes precedence over the call-forward b2bua busy and call-forward b2bua noan commands.

## Examples

## Examples

The following example shows how to forward all incoming calls to
                              		  extension 5001 on directory number 4, to extension 5005.

```
Router(config)# voice register dn 4 Router(config-register-dn)# number 5001 Router(config-register-dn)# call-forward b2bua all 5005
```

## Examples

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

call-waiting (voice register pool)

Enables call waiting on a SIP phone.

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

Feature is disabled.

### Command Modes

Voice register dn configuration (config-register-dn) Voice register pool configuration (config-register-pool)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was introduced.

12.4(11)XJ

Cisco Unified CME 4.1

This command was removed from voice register pool
                                          						configuration mode for Cisco Unified CME only.

12.4(15)T

Cisco Unified CME 4.1

This command with modifications was integrated into Cisco
                                          						IOS Release 12.4(15)T.

### Usage Guidelines

This command in voice register dn configuration mode applies the call
                              		  forward mechanism to a individual SIP extension in Cisco Unified CME or Cisco
                              		  Unified SIP SRST that is off-hook. This command in voice register pool
                              		  configuration mode is for Cisco Unified SIP SRST only and applies to SIP IP
                              		  phones on which the extension appears.

In Cisco Unified CME, call forward busy is also invoked when a call
                              		  arrives for a destination that is configured but unregistered. A destination is
                              		  considered to be configured if its number is listed under the voice register dn
                              		  configuration.

If this command is configured in both voice register dn and voice
                              		  register pool configuration modes, the configuration under voice register dn
                              		  takes precedence.

We recommend that you do not use this command to configure a SIP
                              		  extension or SIP IP phone that is a member of a hunt group. If this command is
                              		  configured for a member of a hunt group, remove the phone from any hunt group
                              		  to which it is assigned to avoid forwarding calls to all phones in the hunt
                              		  group.

The call-forward b2bua all command takes precedence over the call-forward b2bua busy and call-forward b2bua noan commands.

## Examples

The following example shows how to forward all incoming calls to
                              		  extension 5001 on directory number 4 to extension 5005 when extension 5001 is
                              		  busy.

```
Router(config)# voice register dn 4 Router(config-register-dn)# number 5001 Router(config-register-dn)# call-forward b2bua busy 5005
```

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

call-waiting (voice register pool)

Enables call waiting on a SIP phone.

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

Feature is disabled.

### Command Modes

Voice register dn configuration (config-register-dn) Voice register pool configuration (config-register-pool)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was introduced.

12.4(11)XJ

Cisco Unified CME 4.1

This command was removed from voice register pool
                                          						configuration mode for Cisco Unified CME only.

12.4(15)T

Cisco Unified CME 4.1

This command with modifications was integrated into Cisco
                                          						IOS Release 12.4(15)T

### Usage Guidelines

This command is used to denote the voice-mail box to use at the end
                              		  of a chain of call forwards to busy or no answer destinations. It can be used
                              		  to forward calls to a voice-mail box that has a different number than the
                              		  forwarding extension, such as a shared voice-mail box.

This command in voice register dn configuration mode applies the call
                              		  forward mechanism to a individual SIP extension in Cisco Unified CME or Cisco
                              		  Unified SIP SRST. This command in voice register pool configuration mode is for
                              		  Cisco Unified SIP SRST only and applies to SIP IP phones on which the extension
                              		  appears.

If this command is configured in both the voice register dn and voice
                              		  register pool configuration modes, the configuration under voice register dn
                              		  takes precedence.

We recommend that you do not use this command to configure a SIP
                              		  extension or SIP IP phone that is a member of a hunt group. If this command is
                              		  configured for a member of a hunt group, remove the phone from any hunt group
                              		  to which it is assigned to avoid forwarding calls to all phones in the hunt
                              		  group.

This command is used in conjunction with the call-forward b2bua all , call-forward b2bua busy , and call-forward b2bua noan commands.

## Examples

The following example shows how to forward all incoming calls to
                              		  extension 5005 if an incoming call is forwarded to extension 5001, and
                              		  extension 5001 is busy or does not answer.

```
Router(config)# voice register dn 4 Router(config-register-dn)# number 5001 Router(config-register-dn)# call-forward b2bua mailbox 5005
```

## Examples

The following example shows how to forward calls to extension 5005 if
                              		  an incoming call is forwarded to extension 5001 on pool number 4, and extension
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

## call-forward b2bua
                        	 night-service

To automatically
                              		  forward calls to another number during night-service hours, use the call-forward b2bua night-service command in voice register dn
                              		  configuration mode. To remove the code, use the no form of
                              		  this command.

call-forward b2bua night-service target-number

no call-forward b2bua night-service

### Syntax Description

target-number

Phone
                                          						number to which calls are forwarded.

### Command Default

Calls are not
                              		  forwarded during night-service hours.

### Command Modes

Voice register dn configuration: (config-register-dn)

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

You need to
                              		  configure the night-service bell command under voice register dn.
                              		  Night-service hours are defined using the night-service date and night-service day commands.

A voice register
                              		  dn can have all other types of call forwarding defined at the same time:
                              		  all-calls, no-answer, busy, and night-service. Each type of call forwarding can
                              		  have a different forwarding destination defined in its target-number argument.
                              		  If more than one type of call forwarding is in effect (is active) at one time,
                              		  the precedence order for evaluating the different types is as follows:

call forward
                                    				night-service (only during night service hours)

call forward
                                    				all

call forward
                                    				busy and call forward no answer

## Examples

The following
                              		  example defines a call forward night-service configuration under voice register
                              		  dn :

```
Router(config)# voice register dn tag Router(config-register-dn)# call-forward b2bua night-service
```

### Related Commands

Description

night-service date

Defines a recurring time period associated with a month and day during which
                                          						night service is active.

night-service day

Defines a recurring time period associated with a day of the week during which
                                          						night service is active.

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

Feature is disabled.

### Command Modes

Voice register dn configuration (config-register-dn) Voice register pool configuration (config-register-pool)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4 Cisco SIP SRST 3.4

This command was introduced.

12.4(11)XJ

Cisco Unified CME 4.1

This command was removed from voice register pool
                                          						configuration mode for Cisco Unified CME only.

12.4(15)T

Cisco Unified CME 4.1

This command with modifications was integrated into Cisco
                                          						IOS Release 12.4(15)T.

### Usage Guidelines

This command in voice register dn configuration mode applies the call
                              		  forward mechanism to a individual SIP extension in Cisco Unified CME or Cisco
                              		  Unified SIP SRST that remains unanswered after a specified length of time. This
                              		  command in voice register pool configuration mode is for Cisco Unified SIP SRST
                              		  only and applies to SIP IP phones on which the extension appears.

If this command is configured in both the voice register dn and voice
                              		  register pool configuration modes, the configuration under voice register dn
                              		  takes precedence.

We recommend that you do not use this command to configure a SIP
                              		  extension or SIP IP phone that is a member of a hunt group. If this command is
                              		  configured for a member of a hunt group, remove the phone from any hunt group
                              		  to which it is assigned to avoid forwarding calls to all phones in the hunt
                              		  group.

The call-forward b2bua all command takes precedence over the call-forward b2bua busy and call-forward b2bua noan commands.

## Examples

The following example shows how to forward calls to extension 5005
                              		  when extension 5001 is unanswered. The timeout before the call is forwarded to
                              		  extension 5005 is 10 seconds.

```
Router(config)# voice register pool 4 Router(config-register-pool)# number 5001 Router(config-register-pool)# call-forward b2bua noan 5005 timeout 10
```

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

call-waiting (voice register pool)

Enables call waiting on a SIP phone.

## call-forward b2bua unreachable

To forward calls to a phone that is not registered to Cisco Unified
                              		  CME, use the call forward b2bua unreachable command in voice register dn or voice register pool configuration mode. To
                              		  disable call forwarding, use the no form of this command.

call-forward b2bua unreachable directory-number

no call-forward b2bua unreachable

### Syntax Description

directory number

Telephone number to which calls are forwarded. Represents a
                                          						fully qualified E.164 number.

### Command Default

Feature is disabled

### Command Modes

Voice register dn configuration (config-register-dn) Voice register pool configuration (config-register-pool)

## Command History

Cisco IOS Release

Version

Modification

12.4(4)T

Cisco CME 3.4

This command was introduced.

12.4(11)XJ

Cisco Unified CME 4.1

This command was removed.

12.4(15)T

Cisco Unified CME 4.1

This command was removed in Cisco IOS Release 12.4(15)T.

### Usage Guidelines

Call forward unreachable is triggered when a call arrives for a
                              		  destination that is configured but unregistered with Cisco CME. A destination
                              		  is considered to be configured if its number is listed under the voice register
                              		  pool or voice register dn configurations.

If call forward unreachable is not configured for a pool or directory
                              		  number (DN) register, any calls that match the numbers in that pool or DN
                              		  register will use call forward busy instead.

We recommend that you do not use this command with hunt groups. If
                              		  the command is used, consider removing the phone from any assigned hunt groups,
                              		  unless you want to forward calls to all phones in the hunt group.

## Examples

The following example shows how to forward calls to extension 5005
                              		  when extension 5001 on directory number 4 is unreachable, either because it is
                              		  unplugged or the network between the Cisco router and the extension is
                              		  nonfunctional. The timeout before the call is forwarded to extension 5005 is 10
                              		  seconds.

```
Router(config)# voice register pool 4 Router(config-register-dn)# number 5001 Router(config-register-dn)# call-forward b2bua unreachable 5005 timeout 10
```

### Related Commands

Command

Description

call-forward b2bua all (voice register dn and voice register pool)

Enables call forwarding for a SIP B2BUA so that all
                                          						incoming calls are forwarded to another extension.

call-forward b2bua busy (voice register dn and voice register pool)

Enables call forwarding for a SIP B2BUA so that incoming
                                          						calls to a busy extension are forwarded to another extension.

call-forward b2bua mailbox (voice register dn and voice register pool)

Controls the specific voice-mail box selected in a
                                          						voice-mail system at the end of a call forwarding exchange.

call-forward b2bua noan (voice register dn and voice register pool)

Enables call forwarding for a SIP B2BUA so that incoming
                                          						calls to an extension that does not answer after a configured amount of time
                                          						are forwarded to another extension.

call-waiting (voice register pool)

Enables call waiting on a SIP phone.

number (voice register dn)

Associates an extension number with a voice register dn.

## call-forward busy

To configure call forwarding so that incoming calls to a busy
                              		  extension (ephone-dn) are forwarded to another extension, use the call forward busy command in ephone - dn or ephone-dn-template configuration mode. To
                              		  disable call forwarding, use the no form of this command.

call-forward busy target-number [ primary | secondary ] [ dialplan-pattern ]

no call-forward busy

### Syntax Description

target-number

Phone number to which calls are forwarded.

primary

(Optional) Call forwarding is selectively applied only to
                                          						the dial peer created for the primary number for this ephone-dn.

secondary

(Optional) Call forwarding is selectively applied only to
                                          						the dial peer created for the secondary number for this ephone-dn.

dialplan-pattern

(Optional) Call forwarding is selectively applied only to
                                          						dial peers created for this ephone-dn by the dial-plan pattern.

### Command Default

Call forwarding for a busy extension is not enabled.

### Command Modes

Ephone-dn configuration (config-dn-ephone) Ephone-dn-template configuration (config-ephone-dn-template)

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

12.4(4)XC

Cisco Unified CME 4.0

The primary , secondary , and dialplan-pattern keywords were
                                          						added, and this command was made available in ephone-dn-template configuration
                                          						mode.

12.4(11)T

Cisco Unified CME 4.0

This command with the primary , secondary , and dialplan-pattern keywords added,
                                          						and this command in ephone-dn-template configuration mode was integrated into
                                          						Cisco IOS 12.4(11)T.

### Usage Guidelines

The call forwarding mechanism is applied to an individual extension
                              		  (ephone-dn) and is not applied to the phone on which the extension appears.

Normally, call forwarding is applied to all dial peers that are
                              		  created by the ephone-dn. An ephone-dn can create up to four dial peers:

- A dial peer for the primary number

- A dial peer for the secondary number

- A dial peer for the primary number as expanded by the dialplan-pattern command

- A dial peer for the secondary number as expanded by the dialplan-pattern command

The primary , secondary , and dialplan-pattern keywords allow you to apply
                              		  call forwarding selectively to one or more dial peers based on the exact called
                              		  number that was used to route the call to the ephone-dn. If none of the
                              		  optional keywords is used, call forwarding applies to all dial-peers that are
                              		  defined for the ephone-dn.

An ephone-dn can have all four types of call forwarding defined at
                              		  the same time: all-calls, no-answer, busy, and night-service. Each type of call
                              		  forwarding can have a different forwarding target defined in its target-number argument. If more than one type of call forwarding
                              		  is in effect (is active) at one time, the precedence order for evaluating the
                              		  different types is as follows:

- call forward night service

- call forward all

- call forward busy and call forward no answer

If you use an ephone-dn template to apply a command to an ephone-dn
                              		  and you also use the same command in ephone-dn configuration mode for the same
                              		  ephone-dn, the value that you set in ephone-dn configuration mode has priority.

## Examples

The following example forwards all calls for the ephone-dn 2345 when
                              		  it is busy.

```
Router(config)# ephone-dn 236 Router(config-ephone-dn)# number 2345 Router(config-ephone-dn)# call-forward busy 2000
```

The following example uses an ephone-dn template to forward calls for
                              		  extension 2345 when it is busy.

```
Router(config)# ephone-dn-template 6 Router(config-ephone-dn-template)# call-forward busy 2000 Router(config-ephone-dn-template)# exit Router(config)# ephone-dn 236 Router(config-ephone-dn)# number 2345 Router(config-ephone-dn)# ephone-dn-template 6
```

The following example creates a dial-plan pattern to expand extension
                              		  numbers into E.164 numbers. It then sets call forwarding of incoming calls to
                              		  directory number 5005. In this example, call forwarding on busy is applied only
                              		  when callers dial the primary number for this ephone-dn, 5001.

```
Router(config)# telephony-service Router(config-telephony)# dialplan-pattern 1 40855501.. extension-length 4 extension-pattern 50.. Router(config-telephony)# exit Router(config)# ephone-dn 1 Router(config-ephone-dn)# number 5001 secondary 5002 Router(config-ephone-dn)# call-forward busy 5005 primary
```

### Related Commands

Command

Description

call forward all

Configures call forwarding for all incoming calls to an
                                          						ephone-dn.

call-forward night-service

Configures call forwarding for all incoming calls to an
                                          						ephone-dn during the hours defined for night service.

call forward noan

Configures call forwarding to another number when no answer
                                          						is received from an ephone-dn.

ephone-dn-template (ephone-dn)

Applies template to ephone-dn.

## call-forward max-length

To restrict the number of digits that can be entered using the
                              		  CfwdALL soft key on an IP phone, use the call forward max-length command in ephone-dn or ephone-dn-template configuration mode. To remove a
                              		  restriction on the number of digits that can be entered, use the no form of this command.

call-forward max-length length

no call-forward max-length

### Syntax Description

length

Number of digits that can be entered using the CfwdAll soft
                                          						key on an IP phone.

### Command Default

There is no restriction on the number of digits that can be entered.

### Command Modes

Ephone-dn configuration (config-dn-ephone) Ephone-dn-template configuration (config-ephone-dn-template)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(7)T

Cisco CME 3.1

This command was introduced.

12.4(4)XC

Cisco Unified CME 4.0

This command was made available in ephone-dn-template
                                          						configuration mode.

12.4(11)T

Cisco Unified CME 4.0

This command in ephone-dn-template configuration mode was
                                          						integrated into Cisco IOS Release 12.4(11)T.

### Usage Guidelines

This command can be used to prevent a phone user from using the
                              		  CfwdALL soft key on an IP phone to forward calls to numbers that will incur
                              		  toll charges when they receive forwarded calls.

If the length argument is set to 0, the CfwdALL soft key is completely
                              		  disabled. If the ephone-dn associated with the first line button has an active
                              		  call forward number when this command is used to set the length argument to 0, the CfwdALL soft key
                              		  will be disabled after the next phone restart.

The restriction created by this command does not apply to
                              		  destinations that are entered using the Cisco IOS command-line interface (CLI)
                              		  or the Cisco Unified CME GUI.

If you use an ephone-dn template to apply a command to an ephone-dn
                              		  and you also use the same command in ephone-dn configuration mode for the same
                              		  ephone-dn, the value that you set in ephone-dn configuration mode has priority.

## Examples

The following example restricts the number of digits that a phone
                              		  user can enter using the CfwdALL soft key to four. In this example, extensions
                              		  in the phone user’s Cisco Unified CME system have four digits, so that means
                              		  the user can use the IP phone to forward all calls to any extension in the
                              		  system, but not to any number outside the system.

```
Router(config)# ephone-dn 1 Router(config-ephone-dn)# number 5001 Router(config-ephone-dn)# call-forward max-length 4
```

The following example uses an ephone-dn-template to restrict the
                              		  number of digits that a phone user can enter using the CfwdALL soft key to
                              		  four.

```
Router(config)# ephone-dn-template 4 Router(config-ephone-dn-template)# call-forward max-length 4 Router(config-ephone-dn-template)# exit Router(config)# ephone-dn 1 Router(config-ephone-dn)# number 5001 Router(config-ephone-dn)# ephone-dn-template 4
```

### Related Commands

Command

Description

call-forward all

Configures call forwarding for all incoming calls on one of
                                          						the lines of a Cisco Unified IP phone.

ephone-dn-template (ephone-dn)

Applies an ephone-dn template to an ephone-dn.

## call-forward night-service

To automatically forward calls to another number during night-service
                              		  hours, use the call-forward night-service command in ephone-dn or
                              		  ephone-dn-template configuration mode. To disable automatic call forwarding
                              		  during night service, use the no form of this command.

call-forward night-service target-number

no call-forward night-service

### Syntax Description

target-number

Phone number to which calls are forwarded.

### Command Default

Calls are not forwarded during night-service hours.

### Command Modes

Ephone-dn configuration (config-dn-ephone) Ephone-dn-template configuration (config-ephone-dn-template)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)XC

Cisco Unified CME 4.0

This command was introduced.

12.4(11)T

Cisco Unified CME 4.0

This command was integrated into Cisco IOS Release
                                          						12.4(11)T.

### Usage Guidelines

You must also configure the night-service bell command for this ephone-dn.

Night-service hours are defined using the night-service date and night-service day commands.

An ephone-dn can have all four types of call forwarding defined at
                              		  the same time: all-calls, no-answer, busy, and night-service. Each type of call
                              		  forwarding can have a different forwarding destination defined in its target-number argument. If more than one type of call forwarding
                              		  is in effect (is active) at one time, the precedence order for evaluating the
                              		  different types is as follows:

- call forward night-service

- call forward all

- call forward busy and call forward no answer

If you use an ephone-dn template to apply a command to an ephone-dn
                              		  and you also use the same command in ephone-dn configuration mode for the same
                              		  ephone-dn, the value that you set in ephone-dn configuration mode has priority.

## Examples

The following example establishes night-service hours from 1 p.m.
                              		  Saturday until 8 a.m. Monday. During that time, calls to extension 1000
                              		  (ephone-dn 1) are forwarded to extension 2346. Note that the night-service bell command has also been used for ephone-dn 1.

```
telephony-service
 night-service day sat 13:00 12:00
 night-service day sun 12:00 08:00
 night-service code *1234
!
ephone-dn 1
 number 1000
 night-service bell
 call-forward night-service 2346
!
ephone-dn 2
 number 2346
ephone 12
 button 1:1
ephone 13
 button 1:2
The following example uses an ephone-dn template to apply call forwarding for extension 2876 during the night service hours established in the previous example.
ephone-dn-template 2
 call-forward night-service 2346
ephone-dn 25
 number 2876
 ephone-dn-template 2
```

### Related Commands

Command

Description

call forward all

Configures call forwarding for all incoming calls to an
                                          						ephone-dn.

call forward busy

Configures call forwarding to another number when an
                                          						ephone-dn is busy.

call forward noan

Configures call forwarding to another number when no answer
                                          						is received from an ephone-dn.

night-service bell (ephone-dn)

Marks an ephone-dn for night-service treatment.

night-service date

Defines a recurring time period associated with a month and
                                          						day during which night service is active.

night-service day

Defines a recurring time period associated with a day of
                                          						the week during which night service is active.

## call-forward noan

To configure call forwarding so that incoming calls to an extension
                              		  (ephone-dn) that does not answer are forwarded to another number, use the call forward noan command in ephone - dn or ephone-dn-template configuration mode. To
                              		  disable call forwarding, use the no form of this command.

call-forward noan target-number timeout seconds [ primary | secondary ] [ dialplan-pattern ]

no call-forward noan

### Syntax Description

target-number

Phone number to which calls are forwarded.

timeout seconds

Sets the duration that a call can ring with no answer
                                          						before the call is forwarded to the target number. Range is from 3 to 60000.
                                          						There is no default value.

primary

(Optional) Call forwarding is selectively applied only to
                                          						the dial peer created for the primary number for this ephone-dn.

secondary

(Optional) Call forwarding is selectively applied only to
                                          						the dial peer created for the secondary number for this ephone-dn.

dialplan-pattern

(Optional) Call forwarding is selectively applied only to
                                          						dial peers created for this ephone-dn by the dial-plan pattern.

### Command Default

Call forwarding for an extension that does not answer is not enabled.

### Command Modes

Ephone-dn configuration (config-dn-ephone) Ephone-dn-template configuration (config-ephone-dn-template)

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

12.4(4)XC

Cisco Unified CME 4.0

The primary , secondary , and dialplan-pattern keywords were
                                          						added, and this command was made available in ephone-dn-template configuration
                                          						mode.

12.4(9)T

Cisco Unified CME 4.0

This command with modifications was integrated into Cisco
                                          						IOS Release 12.4(9)T.

### Usage Guidelines

The call forwarding mechanism is applied to an individual extension
                              		  (ephone-dn) and is not applied to the phone on which the extension appears.

Normally, call forwarding is applied to all dial peers that are
                              		  created by the ephone-dn. An ephone-dn can create up to four dial peers:

- A dial peer for the primary number

- A dial peer for the secondary number

- A dial peer for the primary number as expanded by the dialplan-pattern command

- A dial peer for the secondary number as expanded by the dialplan-pattern command

The primary , secondary , and dialplan-pattern keywords allow you to apply
                              		  call forwarding selectively to one or more dial peers based on the exact called
                              		  number that was used to route the call to the ephone-dn. If none of the
                              		  optional keywords is used, call forwarding applies to all dial-peers that are
                              		  defined for the ephone-dn.

An ephone-dn can have all four types of call forwarding defined at
                              		  the same time: all-calls, no-answer, busy, and night-service. Each type of call
                              		  forwarding can have a different forwarding target defined in its target-number argument. If more than one type of call forwarding
                              		  is in effect (is active) at one time, the precedence order for evaluating the
                              		  different types is as follows:

- call forward night service

- call forward all

- call forward busy and call forward no answer

If you use an ephone-dn template to apply a command to an ephone-dn
                              		  and you also use the same command in ephone-dn configuration mode for the same
                              		  ephone-dn, the value that you set in ephone-dn configuration mode has priority.

## Examples

The following example forwards calls for the ephone-dn 2345 when it
                              		  does not answer.

```
Router(config)# ephone-dn 236 Router(config-ephone-dn)# number 2345 Router(config-ephone-dn)# call-forward busy 2000 The following example uses an ephone-dn-template to forward calls for the ephone-dn 2345 when it does not answer.
Router(config)# ephone-dn-template 8 Router(config-ephone-dn-template)# call-forward busy 2000 Router(config-ephone-dn-template)# exit Router(config)# ephone-dn 236 Router(config-ephone-dn)# number 2345 Router(config-ephone-dn)# ephone-dn-template 8
```

The following example creates a dial-plan pattern to expand extension
                              		  numbers into E.164 numbers. It then sets call forwarding of incoming calls to
                              		  directory number 5005. In this example, call forwarding on no answer is applied
                              		  only when callers dial the primary number for this ephone-dn, 5001.

```
Router(config)# telephony-service Router(config-telephony)# dialplan-pattern 1 40855501.. extension-length 4 extension-pattern 50.. Router(config-telephony)# exit Router(config)# ephone-dn 1 Router(config-ephone-dn)# number 5001 secondary 5002 Router(config-ephone-dn)# call-forward noan 5005 primary
```

### Related Commands

Command

Description

call forward all

Configures call forwarding for all incoming calls for an
                                          						ephone-dn.

call forward busy

Configures call forwarding to another number when an
                                          						ephone-dn is busy.

call-forward night-service

Configures call forwarding for all incoming calls to an
                                          						ephone-dn during the hours defined for night service.

ephone-dn-template (ephone-dn)

Applies an ephone-dn-template to an ephone-dn.

## call-forward pattern

To specify a pattern for calling - party numbers that are able to
                              		  support the ITU-T H.450.3 standard for call forwarding, use the call forward pattern command in telephony-service configuration mode. To remove the
                              		  pattern, use the no form of this command.

call-forward pattern pattern

no call-forward pattern pattern

### Syntax Description

pattern

String that consists of one or more digits and wildcard
                                          						markers or dots (.) to define a specific pattern. Calling parties that match a
                                          						defined pattern use the H.450.3 standard if they are forwarded. A pattern of .T
                                          						specifies the H.450.3 forwarding standard for all incoming calls.

### Command Default

No call-forward pattern is defined.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(11)YT

Cisco CME 2.1

This command was introduced.

12.2(15)T

Cisco CME 2.1

This command was integrated into Cisco IOS Release
                                          						12.2(15)T.

### Usage Guidelines

Use this command with Cisco IOS Telephony Services (ITS) V2.1, Cisco
                              		  CallManager Express 3.0, or a later version.

When H.450.3 call forwarding is selected, the router must be
                              		  configured with a Tool Command Language (Tcl) script that supports the H.450.3
                              		  protocol. The Tcl script is loaded on the router by using the call application voice command.

The pattern match in this command is against the phone number of the
                              		  calling party. When an extension number has forwarded its calls and an incoming
                              		  call is received for that number, the router sends an H.450.3 response back to
                              		  the original calling party to request that the call be placed again using the
                              		  forward-to destination.

Calling numbers that do not match the patterns defined using this
                              		  command are forwarded using Cisco-proprietary call forwarding for backward
                              		  compatibility.

## Examples

The following example specifies that all 4-digit directory numbers
                              		  that begin with 4 should use the H.450.3 standard whenever they are forwarded:

```
Router(config)# telephony-service Router(config-telephony)# call-forward pattern 4...
```

The following example forwards all calls that support the H.450.3
                              		  standard:

```
Router(config)# telephony-service Router(config-telephony)# call-forward pattern .T
```

### Related Commands

Command

Description

call application voice

Defines an application, indicates the location of the
                                          						corresponding Tcl files that implement the application, and loads the selected
                                          						Tcl script.

## calling-number local

To replace a calling-party number and name with the forwarding-party
                              		  number and name (the local number and name) in calls forwarded using local
                              		  hairpin call routing, use the calling-number local command in telephony-service configuration mode. To reset to
                              		  the default, use the no form of this command.

calling-number local [ secondary ]

no calling-number local

### Syntax Description

secondary

(Optional) Uses the secondary number associated with the
                                          						forwarding party instead of the primary number. The primary number is the
                                          						default if this keyword is not used.

### Command Default

Calling-party numbers and names are used in forwarded calls.

### Command Modes

Telephony-service configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ3

Cisco CME 3.0

This command was introduced.

12.3(4)T

Cisco CME 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

12.3(15)ZJ4

Cisco CME 3.0

The secondary keyword was introduced.

12.3(14)T

Cisco CME 3.3

Support was added to the default IOS voice application
                                          						framework and dependency on the TCL script was removed.

### Usage Guidelines

In Cisco CME 3.2 and earlier versions, this command is used with the
                              		  Tool Command Language (Tcl) script app-h450-transfer.2.0.0.7 or a later
                              		  version.

In Cisco CME 3.3 and later versions, this command can be used without
                              		  the TCL script because the functionality is integrated into the default IOS
                              		  voice application framework.

If the ephone-dn used by a forwarding party has a secondary number in
                              		  addition to its primary number and neither number is registered with the
                              		  gatekeeper, the primary number is the number that appears as the calling number
                              		  on hairpin-forwarded calls when the calling-number local command is used. If only one of the numbers
                              		  is registered with the gatekeeper, the registered number is the number that
                              		  appears as the calling number. If both numbers are registered with the
                              		  gatekeeper, the primary number is the number that appears as the calling
                              		  number.

If the ephone-dn used by a forwarding party has a secondary number in
                              		  addition to its primary number and the calling-number local secondary command is used, the secondary number is
                              		  the number that appears as the calling number on hairpin-forwarded calls if
                              		  both numbers are registered with the gatekeeper or if both numbers are not
                              		  registered. If only one number is configured to register with the gatekeeper,
                              		  the number that is registered appears as the calling number.

## Examples

The following example specifies use of the name and number of the
                              		  local forwarding party in hairpin-forwarded calls:

```
Router(config)# telephony-service Router(config-telephony)# calling-number local
```

The following examples demonstrate the use of the calling-number local command without the secondary keyword.

- The calling number for hairpin calls forwarded from ephone-dn 1 is
                                 			 1234 in the following example:

```
calling-number local
ephone-dn 1
 number 1234 secondary 4321 no-reg
```

- The calling number for hairpin calls forwarded from ephone-dn 1 is
                                 			 4321 in the following example:

```
calling-number local
ephone-dn 1
 number 1234 secondary 4321 no-reg primary
```

- The calling number for hairpin calls forwarded from ephone-dn 1 is
                                 			 1234 in the following example:

```
calling-number local
ephone-dn 1
 number 1234 secondary 4321 no-reg both
```

or

```
number 1234 secondary 4321
```

The following examples demonstrate the use of the calling-number local secondary command.

- The calling number for hairpin calls forwarded from ephone-dn 1 is
                                 			 1234 in the following example:

```
calling-number local secondary
ephone-dn 1
 number 1234 secondary 4321 no-reg
```

- The calling number for hairpin calls forwarded from ephone-dn 1 is
                                 			 4321 in the following example:

```
calling-number local secondary
ephone-dn 1
 number 1234 secondary 4321 no-reg primary
```

- The calling number for hairpin calls forwarded from ephone-dn 1 is
                                 			 4321 in the following example:

```
calling-number local secondary
ephone-dn 1
 number 1234 secondary 4321 no-reg both
```

or

```
number 1234 secondary 4321
```

## calling-number
                        	 local (voice register global)

To replace a calling-party number and name with the forwarding-party
                              		  number and name (the local number and name) in calls forwarded using local
                              		  hairpin call routing, use the calling-number local command in voice register global configuration mode. To reset
                              		  to the default, use the no form of this command.

calling-number local

no calling-number local

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

Calling-party
                              		  numbers and names are used in forwarded calls. The command is disabled by
                              		  default.

### Command Modes

Voice register global configuration (config-register-global)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

Cisco
                                          						IOS XE Everest 16.6.1

Unified
                                          						CME 12.0

This
                                          						command was introduced.

### Usage Guidelines

Use the CLI
                              		  Command calling-number local in voice register global configuration mode
                              		  so that the number and name of the forwarding party appears as the calling
                              		  number on hairpin-forwarded calls. Once calling-number local is configured under voice register global,
                              		  the calls forwarded from local SIP phones will have the calling-number and name
                              		  of the last forwarded party.

## Examples

The following
                              		  example specifies use of the name and number of the local forwarding party in
                              		  hairpin-forwarded calls:

```
Router(config)# voice register global Router(config-register-global)# calling-number local
```

The following
                              		  examples demonstrate the use of the calling-number local command.

- The calling number for
                                 			 hairpin calls forwarded from voice register dn 1 is 1234 in the following
                                 			 example:

```
voice register global
calling-number local
..
voice register dn 1
 name Phone 1
 number 1234
```

## callqueue-display

To configure call
                              		  waiting notification display on the agent phone as continuous, periodic, or
                              		  off, use the callqueue display command. To set the call waiting notification display to the default state of
                              		  periodic (for voice hunt group) and continuous (for ephone hunt group), use the default form
                              		  of this command.

callqueue display [ continuous | periodic | off ]

default callqueue display

### Command Default

Call waiting
                              		  notification is set to periodic for phones in voice hunt group, and to
                              		  continuous for phones in ephone hunt group. The no form of this command also
                              		  sets the call waiting display to default state.

### Command Modes

Ephone-hunt configuration (config-ephone-hunt)

Voice hunt group configuration (config-voice-hunt-group)

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

The callqueue
                              		  display command is valid for both voice hunt group as well as ephone hunt
                              		  group.

## Examples

The following
                              		  example shows how to set call waiting notification display to periodic in an
                              		  ephone hunt group:

```
Router(config)# ephone-hunt 1 Router(config-ephone-hunt)# call Router(config-ephone-hunt)# callqueue Router(config-ephone-hunt)# callqueue display Router(config-ephone-hunt)# callqueue display periodic
```

The following
                              		  example shows how to set call waiting notification display to continuous in a
                              		  voice hunt group:

```
Router(config)# voice hunt-group 1 Router(config-voice-hunt-group)# callqueue display Router(config-voice-hunt-group)# callqueue display continuous
```

## call-park system

To define system parameters for the Call Park feature, use the call-park system command in telephony-service configuration
                              		  mode. To reset to the default, use the no form of this command.

call-park system { application | redirect }

no call-park system { application | redirect }

### Syntax Description

application

Enables Call Park and Directed Call Park for SCCP and SIP
                                          						phones.

redirect

H.323 and SIP calls use H.450 or the SIP Refer method of
                                          						call forwarding or transfer to park calls and to pick up calls from park.

### Command Default

H.323 and SIP calls use hairpin call forwarding or transfer to park
                              		  calls and to pick up calls from park.

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

12.4(22)YB

Cisco Unified CME 7.1

The application keyword and support for
                                          						SIP phones was added.

12.4(24)T

Cisco Unified CME 7.1

This command has been integrated into Cisco IOS Release
                                          						12.4(24)T.

### Usage Guidelines

The application keyword selects the enhanced Call
                              		  Park method supported in Cisco Unified CME 7.1 and later versions for SCCP and
                              		  SIP phones.

## Examples

The following example specifies that H.323 and SIP calls will use the
                              		  H.450 or SIP Refer method of call forwarding or transfer to park calls and pick
                              		  up calls from park:

```
Router(config)# telephony-service Router(config-telephony)# call-park system redirect
```

### Related Commands

Command

Description

park reservation-group

Assigns a call-park reservation group to a phone.

park-slot

Creates a floating extension at which calls can be
                                          						temporarily parked.

## call-waiting (voice register pool)

To enable call-waiting option on a SIP phone, use the call-waiting command in voice register pool
                              		  configuration mode. To disable call waiting, use the no form of this command.

call-waiting

no call-waiting

### Syntax Description

This command has no arguments or keywords.

### Command Default

Feature is enabled.

### Command Modes

Voice register pool configuration (call-waiting)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4

This command was introduced.

### Usage Guidelines

The call waiting feature is enabled by default on SIP phones. To
                              		  disable call waiting, use the no call-waiting command.

## Examples

The following example shows how to disable call waiting on SIP phone
                              		  1:

```
Router(config)# voice register pool 1 Router(config-register-pool)# no call-waiting
```

### Related Commands

Command

Description

voice register pool

Enters voice register pool configuration mode for SIP
                                          						phones.

## call-waiting beep

To allow call-waiting beeps to be accepted by or generated from an
                              		  ephone-dn, use the call-waiting beep command in ephone-dn or ephone-dn-template configuration mode.
                              		  To disable the acceptance and generation of call-waiting beeps by an ephone-dn,
                              		  use the no form of this command.

call-waiting beep [ accept | generate ]

no call-waiting beep [ accept | generate ]

### Syntax Description

accept

(Optional) Allows call-waiting beeps to be accepted by an
                                          						ephone-dn.

generate

(Optional) Allows call-waiting beeps to be generated by an
                                          						ephone-dn.

### Command Default

Call-waiting beeps are accepted and generated.

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

The call-waiting beep command must be used with the ephone-dn command. The call-waiting beep command is used like a toggle and can be
                              		  switched on and off for each ephone-dn.

A beep can be heard only if both sending and receiving ephone-dns are
                              		  configured to accept call-waiting beeps.

To display how call-waiting beeps are configured, use the show running-confi g command
                              		  in the privileged EXEC configuration mode. If the no call-waiting beep generate and no call-waiting beep accept commands are configured, the show running-config output will display the no call-waiting beep command.

If you configure a button to have a silent ring using the s option of the button command, you will not hear a
                              		  call-waiting beep regardless of whether the ephone-dn associated with the
                              		  button is configured to generate a call-waiting beep.

If you use an ephone-dn template to apply a command to an ephone-dn
                              		  and you also use the same command in ephone-dn configuration mode for the same
                              		  ephone-dn, the value that you set in ephone-dn configuration mode has priority.

## Examples

The following example configures ephone-dn 1 and ephone-dn 2 not to
                              		  accept and not to generate call-waiting beeps:

```
Router(config)# ephone-dn 1 Router(config-ephone-dn)# number 2588 Router(config-ephone-dn)# no call-waiting beep accept Router(config-ephone-dn)# no call-waiting beep generate Router(config-ephone-dn)# exit Router(config)# ephone-dn 2 Router(config-ephone-dn)# number 2589 Router(config-ephone-dn)# no call-waiting beep accept Router(config-ephone-dn)# no call-waiting beep generate Router(config-ephone-dn)# exit
```

The following example uses an ephone-dn template to set the same
                              		  attributes as in the previous example:

```
Router(config)# ephone-dn-template 5 Router(config-ephone-dn-template)# no call-waiting beep accept Router(config-ephone-dn-template)# no call-waiting beep generate Router(config-ephone-dn-template)# exit Router(config)# ephone-dn 1 Router(config-ephone-dn)# number 2588 Router(config-ephone-dn)# ephone-dn-template 5 Router(config-ephone-dn)# exit Router(config)# ephone-dn 2 Router(config-ephone-dn)# number 2589 Router(config-ephone-dn)# ephone-dn-template 5 Router(config-ephone-dn)# exit
```

The following example configures ephone-dn 1 and ephone-dn 2 to
                              		  switch back to accept call-waiting beeps. Ephone-dn 1 and ephone-dn 2 now
                              		  accept but do not generate call-waiting beeps.

```
Router(config)# ephone-dn 1 Router(config-ephone-dn)# call-waiting beep accept Router(config)# ephone-dn 2 Router(config-ephone-dn)# call-waiting beep accept
```

### Related Commands

Command

Description

show running-config

Displays the contents of the currently running
                                          						configuration file or the configuration for a specific interface, or map class
                                          						information.

ephone-dn-template (ephone-dn)

Applies a template to an ephone-dn.

## call-waiting ring

To allow an ephone-dn to use a ring sound for call-waiting
                              		  notification, use the call-waiting ring command in ephone-dn or ephone-dn-template configuration mode.
                              		  To disable the ring notification, use the no form of this command.

call-waiting ring

no call-waiting ring

### Syntax Description

This command has no arguments or keywords.

### Command Default

The ephone-dn accepts call waiting and uses beeps for notification.

### Command Modes

Ephone-dn configuration (config-ephone-dn) Ephone-dn-template configuration (config-ephone-dn-template)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.3(11)XL

Cisco CME 3.2.1

This command was introduced.

12.3(14)T

Cisco CME 3.3

This command was integrated into Cisco IOS Release
                                          						12.3(14)T.

12.4(4)XC

Cisco Unified CME 4.0

This command was made available in ephone-dn-template
                                          						configuration mode.

12.4(9)T

Cisco Unified CME 4.0

This command in ephone-dn-template configuration mode was
                                          						integrated into Cisco IOS Release 12.4(9)T.

### Usage Guidelines

To use a ring sound for call-waiting notification on an ephone-dn,
                              		  you must ensure that the ephone-dn will accept secondary calls while it is
                              		  connected to another line. The acceptance of call waiting is the default
                              		  ephone-dn behavior. However, the no call-waiting beep accept command can change this default so an
                              		  ephone-dn does not accept call waiting. This command must be removed for
                              		  ringing notification to work.

The call-waiting ring command will automatically disable a
                              		  call-waiting beep configuration.

If you configure a button to have a silent ring using the s option of the button command, you will not hear a
                              		  call-waiting ring regardless of whether the ephone-dn associated with the
                              		  button is configured to generate a call-waiting ring.

If you use an ephone-dn template to apply a command to an ephone-dn
                              		  and you also use the same command in ephone-dn configuration mode for the same
                              		  ephone-dn, the value that you set in ephone-dn configuration mode has priority.

## Examples

The following example configures ephone-dn 1 and ephone-dn 2 to use
                              		  ringing for their call-waiting notification:

```
Router(config)# ephone-dn 1 Router(config-ephone-dn)# call-waiting ring Router(config)# ephone-dn 2 Router(config-ephone-dn)# no call-waiting ring
```

The following example uses an ephone-dn template to set the same
                              		  attributes as in the previous example:

```
Router(config)# ephone-dn-template 9 Router(config-ephone-dn-template)# call-waiting ring Router(config-ephone-dn-template)# exit Router(config)# ephone-dn-template 10 Router(config-ephone-dn-template)# no call-waiting ring Router(config-ephone-dn-template)# exit Router(config)# ephone-dn 1 Router(config-ephone-dn)# ephone-dn-template 9 Router(config-ephone-dn)# exit Router(config)# ephone-dn 2 Router(config-ephone-dn)# ephone-dn-template 10 Router(config-ephone-dn)# exit
```

### Related Commands

Command

Description

call-waiting beep

Allows call-waiting beeps to be accepted by or generated
                                          						from an ephone-dn.

ephone-dn-template (ephone-dn)

Applies template to ephone-dn.

## camera

To enable USB camera capability on Cisco Unified IP Phones 9951 and
                              		  9971, use the camera command in voice register global,
                              		  voice register template, and voice register pool configuration modes. To
                              		  disable video capabilities on Cisco Unified IP Phones 9951 and 9971, use the no form of this command.

camera

no camera

### Syntax Description

This command has no arguments or keywords.

### Command Default

USB camera capability is disabled on Cisco Unified IP Phones 9951 and
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

Use this command to enable USB camera capability on Cisco Unified IP
                              		  Phones 9951 and 9971. You need to create profile and apply-config or restart to
                              		  the phone to enable the video capability on phones.

## Examples

The following example shows camera command configured in voice
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
 camera
voice register template  10
!
!
```

The following example shows video and camera commands configured
                              		  under voice register pool 5, you can also configure both camera and video
                              		  commands under voice register template:

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
 camera
!
```

### Related Commands

Command

Description

apply-config

Allows to dynamically apply the phone configuration on
                                          						Cisco Unified SIP IP phones 8961, 9951, and 9971,

## capf-auth-str

To define a string of digits that a user enters at the phone for CAPF
                              		  authentication, use the capf-auth-str command in ephone configuration
                              		  mode. To return to the default, use the no form of this command.

capf-auth-str digit-string

no capf-auth-str

### Syntax Description

digit-string

String of digits that a phone user enters at the phone for
                                          						CAPF authentication.

### Command Default

No authentication string exists for the phone.

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

This command is used with Cisco Unified CME phone authentication to
                              		  create or remove an authentication string (Personal Identification Number or
                              		  PIN) for the specified secure ephone. Use this command if the auth-string keyword is specified in the auth-mode command. Once you specify a CAPF
                              		  authentication string, it becomes part of the ephone configuration. This value
                              		  can also be set globally or per ephone using the auth-string command in CAPF configuration
                              		  mode.

Use the show capf-server auth-str command to display configured
                              		  authentication strings.

When a phone is configured for a certificate upgrade that requires
                              		  auth-string authentication, the CAPF initiation needs to be performed manually
                              		  by the phone user using the following steps:

- Press the Settings button.

- If the configuration is locked, press **# (asterisk, asterisk,
                                 			 pound sign) to unlock it.

- Scroll down the menu and select Security Configuration.

- Scroll down the next menu to LSC and press the Update soft key.

- When prompted for the authentication string, enter the string
                                 			 provided by the system administrator.

## Examples

The following example specifies the type of authentication for ephone
                              		  392 is an authentication string that is entered from the phone, and then
                              		  defines the string as 38593.

```
ephone 392
 button 1:23 2:24 3:25
 device-security-mode authenticated
 cert-oper upgrade auth-mode auth-string
 capf-auto-str 38593
```

### Related Commands

Command

Description

auth-mode

Specifies the type of authentication to use during CAPF
                                          						sessions.

auth-string

Generates or removes authentication strings for one or all
                                          						secure ephones.

show capf-server

Displays configuration and session information for the CAPF
                                          						server.

## capf-server

To enter CAPF-server configuration mode to set CAPF server
                              		  parameters, use the capf-server command in global configuration
                              		  mode. To remove the CAPF server configuration, use the no form of this command.

capf-server

no capf-server

### Syntax Description

This command has no keywords or arguments.

### Command Default

No CAPF server configuration is present.

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

This command is used with Cisco Unified CME phone authentication.

## Examples

The following example sets parameters for the CAPF server:

```
Router(config)# capf-server Router(config-capf-server)# source address 10.10.10.1 Router(config-capf-server)# trustpoint-label server25 Router(config-capf-server)# cert-oper upgrade all Router(config-capf-server)# cert-enroll-trustpoint server12 password 0 x8oWiet Router(config-capf-server)# auth-mode auth-string Router(config-capf-server)# auth-string generate all Router(config-capf-server)# port 3000 Router(config-capf-server)# keygen-retry 5 Router(config-capf-server)# keygen-timeout 45 Router(config-capf-server)# phone-key-size 2048
```

## cert-enroll-trustpoint

To enroll the CAPF with the CA or RA, use the cert-enroll-trustpoint command in CAPF-server
                              		  configuration mode. To remove an enrollment, use the no form of this command.

cert-enroll-trustpoint ca-label password { 0 | 1 } password-string

no cert-enroll-trustpoint

### Syntax Description

ca-label

PKI trustpoint label for the CA or for the RA if an RA is
                                          						being used.

password

Values that follow apply to the password.

0 | 1

Encryption status of the password string that follows.

- 0 —Encrypted.

- 1 —Clear text.

password-string

Alphanumeric challenge password that is required for
                                          						certificate enrollment.

### Command Default

The CAPF server is not enrolled with the CA or RA.

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

The following example specifies that the CAPF server should enroll
                              		  with the trustpoint named server12 (the CA) using the password x8oWiet, which
                              		  should be encrypted:

```
Router(config)# capf-server Router(config-capf-server)# source address 10.10.10.1 Router(config-capf-server)# trustpoint-label server25 Router(config-capf-server)# cert-oper upgrade all Router(config-capf-server)# cert-enroll-trustpoint server12 password 0 x8oWiet Router(config-capf-server)# auth-mode auth-string Router(config-capf-server)# auth-string generate all Router(config-capf-server)# port 3000 Router(config-capf-server)# keygen-retry 5 Router(config-capf-server)# keygen-timeout 45 Router(config-capf-server)# phone-key-size 2048
```

## clear cti session

To tear down the connection between a CSTA client application and
                              		  Cisco Unified CME, use the clear cti session command in privileged EXEC configuration mode.

clear cti session session_id

### Syntax Description

session_id

Unique numeric identifier for the session. String length is
                                          						1 to 10 characters. String value is 1 to 2147483647.

### Command Default

The CTI session between the application and the router is active.

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

This command gracefully disassociates the connection between a CSTA
                              		  application and Cisco Unified CME. Use this command to direct Cisco Unified CME
                              		  to send a SIP BYE for the CSTA call to the application and to clean up the
                              		  session internally. This command does not reset the IP phone.

To disassociate the connection without using this command, you must
                              		  reboot the router or the CSTA client application.

This command has a no form, but the no form has no effect.

To determine the ID for an active CTI session, use the show cti session command.

## Examples

The following example shows how to tear down session 10133 between a
                              		  CSTA client application and Cisco Unified CME:

```
Router# clear cti session 10133 Router#
```

### Related Commands

Command

Description

show cti session

Displays active CTI sessions.

## clear telephony-service conference hardware number

To drop all conference parties and clear the conference call, use the clear telephony-service conference hardware number command in privileged EXEC mode.

clear telephony-service conference hardware number number

### Syntax Description

number

Conference telephone or extension number.

### Command Default

The conference call continues with all current parties.

### Command Modes

Privileged EXEC (#)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(11)XJ2

Cisco Unified CME 4.1

This command was introduced.

12.4(15)T

Cisco Unified CME 4.1

This command was integrated into Cisco IOS Release
                                          						12.4(15)T.

### Usage Guidelines

Use the show telephony-service conference hardware command to display the active hardware
                              		  conferences. Use the clear telephony-service conference hardware number command to clear the desired conference.

## Examples

The following example clears the conference number 1111 and drops all
                              		  its parties:

```
Router# clear telephony-service conference hardware number 1111
```

### Related Commands

Command

Description

show telephony-service conference hardware

Displays information about hardware conferences in a Cisco
                                          						CME system.

## clear telephony-service ephone-attempted-registrations

To empty the log of ephones that unsuccessfully attempt to register
                              		  with Cisco Unified CME, use the clear telephony-service ephone-attempted-registrations command in
                              		  privileged EXEC configuration mode.

clear telephony-service ephone-attempted-registrations

### Syntax Description

This command has no keywords or arguments.

### Command Default

The log continues to accumulate attempted ephone registrations.

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

### Usage Guidelines

The no auto-reg-ephone command blocks the automatic
                              		  registration of ephones whose MAC addresses are not explicitly listed in the
                              		  configuration. When automatic registration is blocked, Cisco Unified CME
                              		  records the MAC addresses of phones that attempt to register but cannot because
                              		  they are blocked.

Use the show ephone attempted-registrations command to view the list of phones that have attempted to
                              		  register but have been blocked. The clear telephony-service ephone-attempted-registrations command clears the
                              		  list.

## Examples

The following example clears the attempted-registrations log.

```
Router# clear telephony-service ephone-attempted-registrations
```

### Related Commands

Command

Description

auto-reg-ephone

Enables automatic registration of ephones with Cisco
                                          						Unified CME.

show ephone attempted-registrations

Displays the log of ephones that unsuccessfully attempt to
                                          						register with Cisco CME.

## clear telephony-service xml-event-log

To clear the event table used for the Cisco Unified CME XML
                              		  application, use the clear telephony-service xml-event-log command in privileged EXEC mode.

clear telephony-service xml-event-log

### Syntax Description

This command has no keywords or arguments.

### Command Default

The XML event table is not cleared.

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

### Usage Guidelines

The show fb-its-log command displays the contents of the
                              		  XML event table.

## Examples

The following example clears the entries from the XML event table:

```
Router# clear telephony-service xml-event-log
```

### Related Commands

Command

Description

show fb-its-log

Displays Cisco Unified CME XML API information.

## clear voice fac statistics

To clear the voice FAC statistics information, use the clear voice
                              		  fac statistics command in user EXEC or privileged EXEC mode.

clear voice fac statistics

### Syntax Description

This command has no arguments or keywords.

### Command Default

No default behavior or value.

### Command Modes

Privileged EXEC.

## Command History

Cisco IOS Release

Cisco Product

Modification

15.1(3)T

Cisco Unified CME 8.5

This command was introduced.

### Usage Guidelines

Use this command to clear the voice Forced Authentication Code (FAC)
                              		  statistics information collected by the system.

```
Router #clear voice fac statistics
```

### Related Commands

Command

Description

show voice fac statistics

Displays details of phones that attempted to register and
                                          						failed.

## clear voice lpcor statistics

To clear all logical partitioning class of restriction (LPCOR)
                              		  statistics that are displayed when the show voice lpcor statistics command is used, use the clear voice lpcor statistics command in privileged EXEC mode.

clear voice lpcor statistics

### Syntax Description

This command has no arguments or keywords.

### Command Default

Statistics continue to increment.

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

This command resets all LPCOR failed-call statistics to 0. Use the show voice lpcor statistics command to display the current
                              		  statistics.

## Examples

The following example resets the LPCOR statistics:

```
Router# clear voice lpcor statistics
```

### Related Commands

Command

Description

show voice lpcor statistics

Displays information about LPCOR policies and calls.

voice lpcor policy

Creates a LPCOR policy for a resource group.

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

## clear voice register attempted-registrations

To clear the attempted-registrations, use the clear voice register
                              		  attempted-registrations command in voice register global mode.

clear voice register attempted registrations [ ip ip-address | mac H . H . H ]

### Syntax Description

ip ip-address

(Optional) IP address of the SIP phone attempting to
                                          						register.

mac H.H.H

(Optional) MAC address of the SIP phone attempting to
                                          						register.

### Command Default

The attempted-registration entries are not cleared.

### Command Modes

Privileged EXEC.

## Command History

Cisco IOS Release

Cisco Product

Modification

15.1(2)T

Cisco Unified CME 8.1

This command was introduced.

### Usage Guidelines

Use this command to delete the entries in the attempted-registration
                              		  table. The clear voice register attempted-registrations command does not alter
                              		  the table size, but clears the existing entries. A user confirmation is sought
                              		  before the cleanup is done.

The primary key to recognize the SIP phones that fail to register is
                              		  through their MAC address (hardware address) and the secondary key is the IP
                              		  address. You can clear the attempted registration entry for a specific phone
                              		  that failed to register by providing its IP address or MAC address and create
                              		  more space for new attempted registration entries in the
                              		  attempted-registrations table. When no options (IP or MAC) are selected, all
                              		  the entries are removed. A user confirmation is sought in such a case, before
                              		  clearing the attempted-registrations table.

The ip keyword allows you to delete entries corresponding to a
                              		  specific IP address. Similarly, the mac keyword allows you to clear the entries
                              		  related to a specific MAC address. User confirmation is not sought if ip or mac
                              		  option is used.

## Examples

```
Router # clear voice regis attempted-registrations
This will clear all the entries. Proceed? Yes/No? [no]: Yes
```

```
Router# clear voice register attempted-registrations ?
  ip   IP Address of the phone
  mac  MAC Address of the phone
```

### Related Commands

Command

Description

attempted-registrations size

Allows to set the size of the attempted-registrations
                                          						table.

show voice register attempted-registration

Displays details of phones that attempted to register and
                                          						failed.

## cnf-file

To specify the generation of different phone configuration files by
                              		  type of phone or by individual phone, use the cnf-file command in telephony-service
                              		  configuration mode. To return to the default, use the no form of this command.

cnf-file { perphonetype | perphone }

no cnf-file { perphonetype | perphone }

### Syntax Description

perphonetype

A separate configuration file is generated for each type of
                                          						phone.

perphone

A separate configuration file is generated for each phone.

### Command Default

A single configuration file is used for all phones.

### Command Modes

Telephony-service (config-telephony)

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

Configuration files can be applied in the following ways:

- Per system—All phones use a single configuration file. This is the
                                 			 default behavior for Cisco Unified CME and does not require you to configure
                                 			 this command. The default user and network locale in a single configuration
                                 			 file are applied to all phones in the Cisco Unified CME system. Alternative and
                                 			 user-defined user and network locales are not supported. To use the per-system
                                 			 option after configuring this command, use the no cnf-file command to reset the option to default
                                 			 behavior.

- Per phone type—Creates separate configuration files for each phone
                                 			 type. For example, all Cisco Unified IP Phone 7960s use XMLDefault7960.cnf.xml,
                                 			 and all Cisco Unified IP Phone 7905s use XMLDefault7905.cnf.xml. All phones of
                                 			 the same type use the same configuration file which is generated using the
                                 			 default user and network locale. This option is not supported if
                                 			 the cnf-file location is configured for system.

- Per phone—Creates a separate configuration file for each phone, by
                                 			 MAC address. For example, a Cisco Unified IP Phone 7960 with the MAC address
                                 			 123.456.789 creates the per-phone configuration file SEP123456789.cnf.xml. The
                                 			 configuration file for a phone is generated with the default user and network
                                 			 locale unless a different user and network locale is applied to the phone using
                                 			 an ephone template. This option is not supported if the location option is
                                 			 system.

To reset the type of configuration file to the default, use the no form of this command and the keyword that
                              		  you previously used to set the type.

This feature is supported only on the following phones:

- Cisco Unified IP Phones 7940 and 7940G

- Cisco Unified IP Phones 7960 and 7960G

- Cisco Unified IP Phone 7970G

- Cisco Unified IP Phone 7971G-GE

## Examples

The following example selects flash memory as the configuration file
                              		  storage location and per-phone as the type of configuration files that the
                              		  system should generate.

```
telephony-service
 cnf-file location flash:
 cnf-file perphone
```

Command

Description

cnf-file location

Specifies a storage location for XML configuration files.

create cnf

Generates the XML configuration files used for provisioning
                                       					 SCCP phones.

## cnf-file location

To specify a storage location for phone configuration files, use the cnf-file location command in telephony-service
                              		  configuration mode. To return to the default, use the no form of this command.

cnf-file location { flash: | slot0: |
                                 					 tftp | tftp-url }

no cnf-file location { flash: | slot0: |
                                 					 tftp | tftp-url }

### Syntax Description

flash:

Router flash memory.

slot0:

Router slot 0 memory.

tftp tftp-url

External TFTP server at the specified URL.

### Command Default

A single phone configuration file is stored in system memory and is
                              		  used by all phones.

### Command Modes

Telephony-service configuration

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

TFTP does not support file deletion. When configuration files are
                              		  updated, they overwrite any existing configuration files with the same name. If
                              		  you change the configuration file location, files are not deleted from the TFTP
                              		  server.

You can specify any of the following locations in which to store
                              		  configuration files:

- System—This is the default. When the system is the storage
                                 			 location, there is only one default configuration file and it is used for all
                                 			 phones in the system. All phones, therefore, use the same user locale and
                                 			 network locale. User-defined user and network locales are not supported. To use
                                 			 the system location, do not use this command to specify a locatio other than
                                 			 system or use the no version of this command to reset the option from a
                                 			 previous, different location.

If VRF Support on Cisco Unified CME is configured and the cnf-file location command is configured for system: , the configuration file for an ephone
                              		  in a VRF group is created in system:/its/vrf<group-tag>/ . The vrf group directory is
                              		  created and appended to the TFTP path automatically. No action is required on
                              		  your part. The location for locale files is not affected. Locale files are
                              		  created in system:/its/.

- Flash or slot 0—When flash or slot 0 memory on the router is the
                                 			 storage location, you can create additional configuration files that can be
                                 			 applied per phone type or per individual phone. Up to five user-defined user
                                 			 and network locales can be used in these configuration files. To store
                                 			 configuration files in flash or slot 0, use the cnf-file location flash: or cnf-file location slot0: command. The generation of configuration
                                 			 files on flash or slot 0 can take up to a minute, depending on the number of
                                 			 files that are being generated.

If VRF Support on Cisco Unified CME is configured and the cnf-file location command is configured as flash: or slot0: , the per phone or per phone type file
                              		  for an ephone in a VRF group is named flash:/its/vrf<group-tag>_<filename> or slot0:/its/vrf<group-tag>_filename> . The vrf group
                              		  directory is created and appended to the TFTP path automatically. No action is
                              		  required on your part. The location for locale files is not affected. Locale
                              		  files are created in flash:/its/ or in slot0:/its

- TFTP—When an external TFTP server is the storage location, you can
                                 			 create additional configuration files that can be applied per phone type or per
                                 			 individual phone. Up to five user-defined user and network locales can be used
                                 			 in these configuration files. To store configuration files on an external TFTP
                                 			 server, use the cnf-file location tftp url command.

## Examples

The following example selects flash memory as the configuration file
                              		  storage location and per-phone as the type of configuration files that the
                              		  system should generate.

```
telephony-service
 cnf-file location flash:
 cnf-file perphone
```

### Related Commands

Command

Description

cnf-file

Specifies the use of different phone configuration files by
                                          						type of phone or by individual phone.

create cnf

Generates the XML configuration files used for provisioning
                                          						SCCP phones.

## codec (ephone)

To select a preferred codec for Cisco Unified CME to use when
                              		  configuring calls for a phone, use the codec command in ephone or ephone-template
                              		  configuration mode. To return to the command default, use the no form of this command.

codec { g711ulaw | g722r64 | g729r8 [ dspfarm-assist ] | ilbc }

no codec

### Syntax Description

g711ulaw

Preferred codec: G.711 micro-law 64K bps.

g722r64

Preferred codec: G.722-64K bps.

g729r8

Preferred codec: G.729-8K bps.

dspfarm-assist

(Optional) DSP-farm resources are used for transcoding the
                                          						segment between the phone and the Cisco Unified CME router if G.711 is
                                          						negotiated for the call.

ilbc

Preferred codec: iLBC 20ms.

### Command Default

G.711 micro-law is the preferred codec.

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

12.4(15)XZ

Cisco Unified CME 4.3

The g722r64 and ilbc keywords were added.

12.4(20)T

Cisco Unified CME 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

This command can be used to help save network bandwidth for a remote
                              		  IP phone.

For calls to phones that are not in the same Cisco Unified CME system
                              		  (such as VoIP calls), the codec is negotiated based on the protocol that is
                              		  used for the call (such as H.323). The Cisco Unified CME system plays no part
                              		  in the negotiation.

The G.722-64K codec is supported on some varieties of phone models.
                              		  Check your phone documentation to make sure the phone supports the G.722-64K
                              		  codecs.

The telephone’s firmware version must support the specified codec. If
                              		  a codec is specified by using this command and a phone does not support the
                              		  preferred codec, then the phone will use the global codec as specified by using
                              		  the codec command in telephony-service
                              		  configuration mode or if the global codec is not supported, G.711 micro-law.

For calls to other phones in the same Cisco Unified CME system, an IP
                              		  phone that is configured to use G.729 will always have its calls set up to use
                              		  G.729. If the phone participates in a call on a line that is shared with a
                              		  phone that is configured for G.729 or is paged together with another phone that
                              		  is configured for G.729, it must use G.729.

When you use the codec command without the dspfarm-assist keyword, you affect only calls
                              		  between two phones on the Cisco Unified CME router (such as between an IP phone
                              		  and another IP phone or between an IP phone and a FXS analog phone). The
                              		  command has no effect on a call directed through a VoIP dial peer unless you
                              		  use the dspfarm-assist keyword.

When you use the g729r8 keyword to select the G.729r8 codec
                              		  for the RTP segment between the IP phone and the Cisco Unified CME router and
                              		  you also use the dspfarm-assist keyword, the router attempts
                              		  to use DSP-farm resources in the following way: If the IP phone is in a VoIP
                              		  call (H.323 or SIP) or a Cisco Unified CME conference in which the codec must
                              		  be set to G.711, the router uses configured DSP-farm resources to attempt to
                              		  return the segment between the phone and the Cisco Unified CME router to G.729.
                              		  Adequate DSP resources must be appropriately configured separately.

f the dspfarm-assist keyword is configured for a
                              		  phone and a DSP resource is not available when needed for transcoding, a phone
                              		  registered to the local Cisco Unified CME router will use G.711 instead of
                              		  G.729r8. This is not true for non-SCCP call legs; if no DSP resource is
                              		  available for the transcoding required for a conference, for example, the
                              		  conference will not be created.

It is recommended that the dspfarm-assist keyword be used sparingly and
                              		  only when absolutely required for bandwidth savings or when you know the phone
                              		  will have few calls that require a G.711 codec.

You should consider your options carefully when deciding to use the dspfarm-assist keyword with the codec command. The benefit is that it allows
                              		  calls to use the G.729r8 codec on the call leg between the IP phone and the
                              		  Cisco Unified CME router, which saves network bandwidth. The disadvantage is
                              		  that for situations requiring G.711 codecs, such as conferencing and Cisco
                              		  Unity Express, DSP resources that can be scarce will be used to transcode the
                              		  call, and delay will be introduced while voice is shuttled to and from the DSP.
                              		  In addition, the overuse of this feature can mask configuration errors in the
                              		  codec selection mechanisms involving dial peers and codec lists.

For information about configuring DSP-farm resources, see the Cisco
                                 			 Unified CME Administrator Guide .

This command can also be configured in ephone-template configuration
                              		  mode. If you use an ephone template to apply a command to a phone and you also
                              		  use the same command in ephone configuration mode for the same phone, the value
                              		  that you set in ephone configuration mode has priority.

## Examples

The following example selects the G.729 codec with DSP farm assist
                              		  for calls that are being configured for ephone 25:

```
ephone 25
 button 1:37
 codec g729r8 dspfarm-assist
```

The following example uses ephone template 1 to apply the G.729 codec
                              		  preference to ephone 25:

```
ephone-template 1
 codec g729r8
ephone 25
 button 1:37
 ephone-template 1
```

### Related Commands

Command

Description

dspfarm (dspfarm)

Enables digital-signal-processor (DSP) farm service

dsp services dspfarm

Specifies the NM-HDV or NM-HDV-FARM on which DSP-farm
                                          						services are to be enabled.

dspfarm transcoder maximum sessions

Specifies the maximum number of transcoding sessions to be
                                          						supported by a DSP farm.

show dspfarm

Displays summary information about DSP resources.

## codec (telephony-service)

To select a default codec for SCCP IP phones in Cisco Unified CME,
                              		  use the codec command in telephony-service
                              		  configuration mode. To disable the codec, use the no form of this command.

codec { g711ulaw | g722r64 }

no codec

### Syntax Description

g711-ulaw

Preferred codec: G.711 micro-law.

g722-64k

Preferred codec: G.722 64K bps.

### Command Default

The default is G.711 micro-law.

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

This command can be used to help save network bandwidth for a remote
                              		  IP phone.

The G.722-64K codec is supported on certain phones only, such as the
                              		  Cisco Unified IP Phone 7906G, 7911G, 7941G-GE, 7942G, 7945G, 7961G-GE, 7962G,
                              		  7965G, and 7975G. Check your phone documentation to make sure your phones
                              		  support the G.722-64K codec.

The telephone firmware version on a Cisco Unified IP phone must
                              		  support the specified codec. If this command is configured and a phone does not
                              		  support the specified codec, the default codec for that phone is G.711
                              		  micro-law.

## Examples

The following example shows how to configure a G.722-64K codec in
                              		  telephony-service configuration mode:

```
Router(config)# telephony-service Router(config-telephony)# codec g722r64 Router(config-telephony)# service phone g722CodecSupport 2 Router(config-telephony)#
```

### Related Commands

Command

Description

service phone

Modifies VendorConfig parameters in configuration files for
                                          						IP phones.

## conference
                        	 (ephone-dn)

To configure a
                              		  conference associated with a directory number, use the conference command in ephone-dn configuration mode. To disable a conference associated
                              		  with a directory number, use the no form of
                              		  this command.

conference { ad-hoc [ video ] |  [ meetme [ video ] [ homogeneous ]] | unlocked }

no conference { ad-hoc [ video ] |  [ meetme [ video ] [ homogenous ]] unlocked }

### Syntax Description

ad-hoc

Configures ad hoc conferences.

video

(Optional) Configures video conferences.

meetme

Configures meet-me conferences.

homogenous

(Optional) Enables a homogeneous video conference in which all participants use
                                          						the same video format.

unlocked

Unlocks
                                          						the meet-me conference bridge.

### Command Default

No conference is
                              		  associated with the directory number.

### Command Modes

Ephone-dn configuration (config-ephone-dn)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.4(11)XJ2

Cisco
                                          						Unified CME 4.1

This
                                          						command was introduced.

12.4(15)T

Cisco
                                          						Unified CME 4.1

This
                                          						command was integrated into Cisco IOS Release 12.4(15)T

15.0(1)XA

Cisco
                                          						Unified CME 8.0

This
                                          						command was modified. The command output was enhanced to display the unlocked
                                          						meet-me conference setting.

15.1(1)T

Cisco
                                          						Unified CME 8.0

This
                                          						command was integrated into Cisco IOS Release 15.1(1)T.

15.1(4)M

Cisco
                                          						Unified CME 8.6

This
                                          						command was modified to configure video conferences.

Cisco
                                          						IOS XE Everest 16.5.1b

Unified CME 11.7

This
                                          						command was integrated into Cisco IOS XE Everest 16.5.1 Release to support
                                          						Cisco 4000 Series Integrated Services Router.

### Usage Guidelines

Ad hoc
                              		  conferences are those that begin as a call between the conference creator and
                              		  another party. The creator then calls other parties and adds them to the
                              		  original call creating a conference.

Meet-me
                              		  conferences have a designated meet-me telephone or extension number that all
                              		  parties call to join the conference. The conference creator initiates the
                              		  meet-me conference by pressing the MeetMe softkey, then dialing the meet-me
                              		  number. Other parties join the conference by dialing the meet-me number.
                              		  Homogenous video conferences only applies to meet-me conferences.

An unlocked
                              		  meet-me conference allows the user to unlock the meet-me conference bridge. All
                              		  DN tags with the same number should be configured with the unlocked option.
                              		  Unlocking the meet-me conference bridge can allow unrestricted and uncontrolled
                              		  access for the external callers. This feature is support only for meet-me
                              		  conferences.

When you unlock
                              		  meet-me conference bridge in Cisco Unified CME, the user can initiate a meet-me
                              		  conference without pressing the MeetMe softkey, which would allow the external
                              		  callers to initiate a meet-me conference.

Use the ephone-dn command to configure enough extensions for your conference needs. Each
                              		  extension can handle two conference parties if the dual-line keyword is used with the ephone-dn command, as shown in the following example. Use the show ephone-dn command to display phone information for
                              		  the extension.

## Examples

The following
                              		  example configures extension 9001 as a four-party meet-me conference number.

```
Router(config)# ephone-dn 1 dual-line Router(config-ephone-dn)# number 9001 Router(config-ephone-dn)# conference meetme Router(config-ephone-dn)# no huntstop Router(config)# ephone-dn 2 dual-line Router(config-ephone-dn)# number 9001 Router(config-ephone-dn)# conference meetme Router(config-ephone-dn)# preference 1
```

You must
                              		  configure additional directory numbers to add more parties to the conference.

### Related Commands

Command

Description

show ephone-dn

Displays phone information for specified dn-tag or for all dn-tags.

## conference (voice register template)

To enable the soft key for conference in a SIP phone template, use
                              		  the conference command in voice register template
                              		  configuration mode. To disable the soft key, use the no form of this command.

conference

no conference

### Syntax Description

This command has no arguments or keywords.

### Command Default

Soft key for conference is enabled.

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

This command enables a soft key for conference in the specified
                              		  template which can then be applied to SIP phones. The conference soft key is
                              		  enabled by default. To disable the conference soft key, use the no conference command. To apply a template to a SIP
                              		  phone, use the template command in voice register pool
                              		  configuration mode.

## Examples

The following example shows how to disable the conference soft key in
                              		  template 1:

```
Router(config)# voice register template 1 Router(config-register-temp)# no conference
```

### Related Commands

Command

Description

template (voice register pool)

Applies a template to a SIP phone.

transfer-attended (voice register template)

Enables a soft key for attended transfer in a SIP phone
                                          						template.

transfer-blind (voice register template)

Enables a soft key for blind transfer in a SIP phone
                                          						template.

voice register pool

Enters voice register pool configuration mode for SIP
                                          						phones.

## conference
                        	 add-mode

To configure the
                              		  mode for adding parties to ad hoc hardware conferences, use the conference add-mode command in ephone or ephone-template
                              		  configuration mode. To return to the default, use the no form of
                              		  this command.

conference add-mode [ creator ]

no conference add-mode [ creator ]

### Syntax Description

creator

Specifies that only the creator can add parties.

### Command Default

Any party can add
                              		  other parties provided the creator remains in the conference.

### Command Modes

Ephone configuration (config-ephone) Ephone-template configuration (config-ephone-template)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.4(11)XJ2

Cisco
                                          						Unified CME 4.1

This
                                          						command was introduced.

12.4(15)T

Cisco
                                          						Unified CME 4.1

This
                                          						command was integrated into Cisco IOS Release 12.4(15)T.

Cisco
                                          						IOS XE Everest 16.5.1b

Unified CME 11.7

Support for this command was introduced on the Cisco 4000 Series
                                          						Integrated Services Routers.

### Usage Guidelines

For more control
                              		  of conference participation, use this command to specify that only the creator
                              		  can add new parties. This configuration ensures that no one can add parties to
                              		  the conference without the creator’s knowledge.

Use this command
                              		  to configure an ephone directly in ephone configuration mode, or use it to
                              		  configure an ephone template in ephone-template configuration mode. Use the ephone-template command in ephone configuration
                              		  mode to apply the ephone template to one or more ephones. Use the show telephony-service ephone command to display the add and drop modes
                              		  for the ephone. Use the show telephony-service ephone-template command to display the ephone
                              		  template.

## Examples

The following
                              		  example configures ad hoc hardware conferences so that only the creator can add
                              		  participants.

```
Router(config)# ephone 1 Router(config-ephone)# conference add-mode creator
```

### Related Commands

Command

Description

ephone-template (ephone)

Applies
                                          						an ephone template to an ephone.

show telephony-service ephone

Displays configuration for the Cisco IP phones.

show telephony-service ephone-template

Displays the contents of ephone-templates.

## conference
                        	 add-mode (voice register)

To configure the
                              		  mode for adding participants to ad-hoc hardware conferences on Cisco Unified
                              		  SIP IP phones, use the conference add-mode command in voice register pool or voice
                              		  register template configuration mode. To return to the default, use the no form of
                              		  this command.

conference add-mode [ creator ]

no conference add-mode

### Syntax Description

creator

(Optional) Specifies that only the conference creator can add participants to
                                          						an ad-hoc hardware conference.

### Command Default

The conference
                              		  creator or any of the participants can add a new participant.

### Command Modes

Voice register pool configuration (config-register-pool)

Voice register template configuration (config-register-temp)

## Command History

Release

Modification

15.2(2)T

This
                                          						command was introduced.

Cisco
                                          						IOS XE Everest 16.5.1b

Support
                                          						for this command was introduced on the Cisco 4000 Series Integrated Services
                                          						Routers.

### Usage Guidelines

Use the conference add-mode creator command to specify that only the conference creator can add new participants.
                              		  This configuration ensures that no one can add participants to the hardware
                              		  conference without the creator’s knowledge.

## Examples

The following
                              		  example shows how to configure the mode so that only the conference creator can
                              		  add new participants to a hardware conference on voice register pool 10:

```
Router(config)# voice register pool 10 Router(config-register-pool)# conference add-mode creator
```

The following
                              		  example shows how to configure the mode so that only the conference creator can
                              		  add new participants to a hardware conference on template 1:

```
Router(config)# voice register template 1 Router(config-register-temp)# conference add-mode creator
```

### Related Commands

Command

Description

voice register pool

Enters
                                          						voice register pool configuration mode and creates a pool configuration for
                                          						Cisco Unified SIP IP phones in Cisco Unified CME.

voice register template

Enters
                                          						voice register template configuration mode and defines a template of common
                                          						parameters for Cisco Unified SIP IP phones.

## conference admin

To configure the ephone as the ad hoc and meet-me hardware conference
                              		  administrator, use the conference admin command in ephone or ephone-template
                              		  configuration mode. To return to the defaults, use the no form of this command.

conference admin

no conference admin

### Syntax Description

This command has no arguments or keywords.

### Command Default

This ephone is not the ad hoc and meet-me hardware conference
                              		  administrator.

### Command Modes

Ephone configuration (config-ephone) Ephone-template configuration (config-ephone-template)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(11)XJ2

Cisco Unified CME 4.1

This command was introduced.

12.4(15)T

Cisco Unified CME 4.1

This command was integrated into Cisco IOS Release
                                          						12.4(15)T

### Usage Guidelines

Use this command to configure an ad hoc and meet-me hardware
                              		  conference administrator. The administrator can:

- Dial in to any conference directly through the conference number

- Use the ConfList soft key to list conference parties

- Remove any party from any conference

The administrator can control the use of conference bridges by
                              		  enforcing time limits and making sure conference bridges are available for
                              		  scheduled meetings.

Use this command to configure an ephone directly in ephone
                              		  configuration mode, or use it to configure an ephone template in
                              		  ephone-template configuration mode. Use the ephone-template command in ephone
                              		  configuration mode to apply the ephone template to one or more ephones. Use the show telephony-service ephone command to display the add and drop modes
                              		  for the ephone. Use the show telephony-service ephone-template command to display the ephone
                              		  template.

## Examples

The following example configures ephone 1 as the ad hoc and meet-me
                              		  hardware conference administrator.

```
Router(config)# ephone 1 Router(config-ephone)# conference admin
```

### Related Commands

Command

Description

ephone-template (ephone)

Applies an ephone template to an ephone.

show telephony-service ephone

Displays configuration for the Cisco IP phones.

show telephony-service ephone-template

Displays the contents of ephone-templates.

## conference admin (voice register)

To assign a Cisco Unified SIP IP phone as the ad-hoc or meet-me
                              		  hardware conference administrator, use the conference admin command in voice register pool or voice
                              		  register template configuration mode. To return to the default, use the no form of this command.

conference admin

no conference admin

### Syntax Description

This command has no arguments or keywords.

### Command Default

The Cisco Unified SIP IP phone is not the conference administrator.

### Command Modes

Voice register pool configuration (config-register-pool)

Voice register template configuration (config-register-temp)

## Command History

Release

Modification

15.2(2)T

This command was introduced.

### Usage Guidelines

Use the conference admin command to assign an ad-hoc or meet-me
                              		  hardware conference administrator. The administrator can:

- Dial in to any conference directly through the conference number.

- Use the ConfList soft key to list conference participants.

- Remove any participant from any conference.

The administrator can control the use of conference bridges by
                              		  enforcing time limits and making sure conference bridges are available for
                              		  scheduled meetings.

## Examples

The following example shows how to configure voice register pool 25
                              		  as the conference administrator:

```
Router(config)# voice register pool 25 Router(config-register-pool)# conference admin
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

## conference
                        	 drop-mode

To configure the
                              		  mode for terminating ad hoc hardware conferences when parties drop out, use the conference drop-mode command in ephone or ephone-template
                              		  configuration mode. To return to the default, use the no form of
                              		  this command.

conference drop-mode [ creator | local ]

no conference drop-mode [ creator | local ]

### Syntax Description

creator

Specifies that the active conference terminates when the creator hangs up.

local

Specifies that the active conference terminates when the last local party in
                                          						the conference hangs up or drops out of the conference.

### Command Default

The conference is
                              		  not dropped, regardless of whether the creator hangs up, provided three parties
                              		  remain in the conference.

### Command Modes

Ephone configuration (config-ephone) Ephone-template configuration (config-ephone-template)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.4(11)XJ2

Cisco
                                          						Unified CME 4.1

This
                                          						command was introduced.

12.4(15)T

Cisco
                                          						Unified CME 4.1

This
                                          						command was integrated into Cisco IOS Release 12.4(15)T

Cisco
                                          						IOS XE Everest 16.5.1b

Unified CME 11.7

Support for this command was introduced on the Cisco 4000 Series
                                          						Integrated Services Routers.

### Usage Guidelines

For more control
                              		  of conference participation, use this command to specify that the conference
                              		  drops when the creator hangs up (see the example). This configuration ensures
                              		  that the conference cannot continue without the creator’s presence.

Use this command
                              		  to configure an ephone directly in ephone configuration mode, or use it to
                              		  configure an ephone template in ephone-template configuration mode. Use the ephone-template command in ephone configuration
                              		  mode to apply the ephone template to one or more ephones. Use the show telephony-service ephone command to display the add and drop modes
                              		  for the ephone. Use the show telephony-service ephone-template command to display the ephone
                              		  template.

## Examples

The following
                              		  example configures ad hoc hardware conferences so that only the creator can add
                              		  participants and the active conference terminates when the creator hangs up.

```
Router(config)# ephone 1 Router(config-ephone)# conference drop-mode creator
```

### Related Commands

Command

Description

ephone-template (ephone)

Applies
                                          						an ephone template to an ephone.

show telephony-service ephone

Displays configuration for the Cisco IP phones.

show telephony-service ephone-template

Displays the contents of ephone-templates.

## conference
                        	 drop-mode (voice register)

To specify who
                              		  can terminate an active ad-hoc hardware conference by hanging up, use the conference drop-mode command in voice register pool or voice
                              		  register template configuration mode. To return to the default, use the no form of
                              		  this command.

conference drop-mode { creator | local }

no conference drop-mode

### Syntax Description

creator

Terminates the active conference when the conference creator hangs up.

local

Terminates the active conference when the last local participant hangs up or
                                          						drops out of the conference.

### Command Default

An active
                              		  conference is never dropped.

### Command Modes

Voice register pool configuration (config-register-pool)

Voice register template configuration (config-register-temp)

## Command History

Release

Modification

15.2(2)T

This
                                          						command was introduced.

Cisco
                                          						IOS XE Everest 16.5.1b

Support
                                          						for this command was introduced on the Cisco 4000 Series Integrated Services
                                          						Routers.

### Usage Guidelines

Use the conference drop-mode creator command to specify that an active hardware conference is terminated when the
                              		  creator hangs up. This configuration ensures that the hardware conference
                              		  cannot continue without the creator’s presence.

## Examples

The following
                              		  example shows how to configure an active conference so that it is terminated
                              		  when the conference creator hangs up:

```
Router(config)# voice register pool 60 Router(config-register-pool)# conference drop-mode creator
```

The following
                              		  example shows how to configure an active conference so that it is terminated
                              		  when the last local participant hangs up or drops out of the conference:

```
Router(config)# voice register template 7 Router(config-register-temp)# conference drop-mode local
```

### Related Commands

Command

Description

voice register pool

Enters
                                          						voice register pool configuration mode and creates a pool configuration for
                                          						Cisco Unified SIP IP phones in Cisco Unified CME.

voice register template

Enters
                                          						voice register template configuration mode and defines a template of common
                                          						parameters for Cisco Unified SIP IP phones.

## conference
                        	 hardware

To configure a
                              		  Cisco Unified CallManager Express system for hardware conferencing only, use
                              		  the conference hardware command in telephony-service
                              		  configuration mode. To return to the default three-party software conferencing,
                              		  use the no form of
                              		  this command.

conference hardware

no conference hardware

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

Three-party ad
                              		  hoc software conferencing.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.4(11)XJ2

Cisco
                                          						Unified CME 4.1

This
                                          						command was introduced.

12.4(15)T

Cisco
                                          						Unified CME 4.1

This
                                          						command was integrated into Cisco IOS Release 12.4(15)T.

Cisco
                                          						IOS XE Everest 16.5.1b

Unified CME 11.7

This
                                          						command was integrated into Cisco IOS XE Everest 16.5.1 Release to support
                                          						Cisco 4000 Series Integrated Services Router.

### Usage Guidelines

Software
                              		  conferencing allows a maximum of three parties in a conference. Use this
                              		  command to take advantage of DSP farm resources for hardware conferencing that
                              		  allows ad hoc conferences with more than three parties.

If you need ad
                              		  hoc hardware conferences, you must use this command to configure DSP farm
                              		  hardware conferencing. You can configure other conferencing features using the conference-join custom-cptone , conference-leave custom-cptone , and maximum conference-participants commands in DSP farm
                              		  profile configuration mode. Use the show dspfarm profile command to display the DSP farm profile.

## Examples

The following
                              		  example configures hardware conferencing as the default for ad hoc conferences
                              		  on this Cisco Unified CallManager Express system:

```
Router(config)# telephony-service Router(config-telephony)# conference hardware
```

### Related Commands

Command

Description

conference-join custom-cptone

Associates a custom call-progress tone to indicate joining a conference with a
                                          						DSP farm profile.

conference-leave custom-cptone

Associates a custom call-progress tone to indicate leaving a conference with a
                                          						DSP farm profile.

maximum conference-participants

Configures the maximum number of conference participants allowed in each
                                          						conference.

show dspfarm profile

Displays configured DSP farm profile information.

## conference
                        	 hardware (voice register global)

To configure
                              		  Cisco Unified Communications Manager Express (Cisco Unified CME) DSPFarm
                              		  hardware-based ad-hoc conferencing, use the conference hardware command in voice register global
                              		  configuration mode. To return to the default, use the no form of
                              		  this command.

conference hardware

no conference hardware

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

Cisco Unified SIP
                              		  IP phone local conference is enabled.

### Command Modes

Voice register global configuration (config-register-global)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

15.2(2)T

Cisco
                                          						Unified CME 9.0

This
                                          						command was introduced.

Cisco
                                          						IOS XE Everest 16.5.1b

Unified CME 11.7

This
                                          						command was integrated into Cisco IOS XE Everest 16.5.1 Release yto support
                                          						Cisco 4000 Series Integrated Services Router.

### Usage Guidelines

Use the conference hardware command in voice register global
                              		  configuration mode to take advantage of DSPfarm resources that allow ad-hoc
                              		  hardware conferences with more than three parties.

Enable hardware
                              		  conferencing in telephony-service configuration mode before configuring
                              		  hardware conferencing in voice register global configuration mode. Otherwise,
                              		  the configuration of hardware conferencing in voice register global
                              		  configuration mode will be rejected.

If you apply any
                              		  changes to the configuration of the hardware conference, you must use the create profile command in voice global configuration mode
                              		  to regenerate the configuration profile files required for Cisco Unified SIP IP
                              		  phones. Then, reboot the phone.

## Examples

The following
                              		  example shows how to configure Cisco Unified CME DSPFarm hardware-based ad-hoc
                              		  conferencing:

```
Router(config)# telephony-service Router(config-telephony)# conference hardware .
Router(config)# voice register global Router(config-register-global)# conference hardware
```

### Related Commands

Command

Description

conference hardware

Configures a Cisco Unified CME system for hardware conferencing only in
                                          						telephony-service configuration mode.

## conference
                        	 max-length

To allow
                              		  conferencing, only if the number of dialed digits are within the max-length
                              		  limit, use the conference
                                    				max-length command. To remove the configuration, use the no form of
                              		  this command.

conference max-length <value>

no conference max-length

## Syntax Description

Maximum
                                       					 number of digits that can be dialed. The range is from 3 to 16.

### Command Default

By default, no
                              		  value is defined for conferencing.

### Command Modes

Ephone  (config-ephone)

Ephone-template ephone  (config-ephone-template)

Voice register pool (config-register-pool)

Voice register template(config-register-temp)

## Command History

This
                                       					 command was introduced.

### Usage Guidelines

Use the conference
                                    				max-length command to configure, the Cisco Unified CME to allow
                              		  conferencing, only if the dialed digits are within the maximum length limit.

## Examples

The following
                              		  example shows how to configure the maximum length of 8 digits that can be
                              		  dialed to make a conference call:

```
Router(config)# ephone 1 Router(config-ephone)# conference max-length 8
```

### Related Commands

Command

Description

conference-pattern blocked

Blocks
                                          						extensions on an ephone or a voice register pool from making conference calls.

conference
                                                							 transfer-pattern

Apply
                                          						transfer -pattern configuration for conference cases.

transfer max-length

Allows
                                          						transfer of calls to phones, where the number of dialed digits are less than
                                          						the maximum length configured.

transfer-pattern
                                                							 (telephony-service)

Allows
                                          						the transfer of calls to phones outside the Cisco Unified CME network.

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

No default values
                              		  are defined.

### Command Modes

Ephone configuration (config-ephone)

Ephone-template configuration (config-ephone-template)

Voice register pool configuration (config-register-pool)

Voice register template configuration (config-register-temp)

## Command History

This
                                       					 command was introduced.

### Usage Guidelines

Use the conference-pattern
                                    				blocked command to prevent specific extensions from making
                              		  conference calls to patterns generally allowed through the transfer-pattern command.

## Examples

The following
                              		  example shows how to prevent extensions from making conference calls using the conference-pattern
                                    				blocked command:

```
Router(config)# ephone 1 Router(config-ephone-template)# conference-pattern blocked
```

### Related Commands

Command

Description

conference max-length

Allows
                                          						conferences to numbers where dialed digits are within the configured maximum
                                          						length value.

conference
                                                							 transfer-pattern

Apply
                                          						transfer-pattern configuration for conference cases.

transfer-pattern blocked

Blocks
                                          						individual phones from transferring calls to nonlocal numbers that have been
                                          						globally enabled for transfer.

transfer-pattern
                                                							 (telephony-service)

Allows
                                          						the transfer of calls to phones outside the Cisco Unified CME network.

## conference transfer-pattern

To configure a Cisco Unified CallManager Express system to apply
                              		  transfer-patter <pattern> to the conference call using conference softkey
                              		  or feature button, use the conference transfer-pattern command in telephony-service
                              		  configuration mode. To return to the default, use the no form of this command.

conference transfer-pattern

no conference transfer-pattern

### Syntax Description

This command has no arguments or keywords.

### Command Default

Transfer-pattern <pattern> does not apply to call conferencing.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.2(4)M

Cisco Unified CME 9.1

This command was introduced.

### Usage Guidelines

There is no check for the conference numbers for call conferencing.
                              		  Use this command to apply transfer-pattern for call conferencing.

## Examples

The following example enables transfer-pattern to be applied for
                              		  conference parties:

```
Router(config)# telephony-service Router(config-telephony)# conference transfer-pattern
```

### Related Commands

Command

Description

telephony-service

Enters telephony-service configuration mode.

## cor (ephone-dn)

This command is now documented as the corlist command. For complete command
                              		  information, see the corlist command page.

## cor (voice
                        	 register)

To configure a
                              		  class of restriction (COR) on the VoIP dial peers associated with directory
                              		  numbers, use the cor command in voice register pool or voice register
                              		  template configuration mode. To disable a COR associated with directory
                              		  numbers, use the no form of
                              		  this command.

cor {incoming | outgoing} cor-list-name 
                                 				  {cor-list-number starting-number [-
                                 				  ending-number] |default }

no cor {incoming | outgoing} cor-list-name 
                                 				  {cor-list-number starting-number [-
                                 				  ending-number]| |default }

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
                                          						list identifier.

starting-number

Start
                                          						of a directory number range, if an ending number is included. Can also be a
                                          						standalone number.

-

(Optional) Indicator that a full range is configured.

ending-number

(Optional) End of a directory number range.

default

Instructs the COR list to assume behavior according to a predefined default COR
                                          						list.

### Command Default

COR is not
                              		  configured on VoIP dial peers.

### Command Modes

Voice register pool configuration (config-register-pool)

Voice register template configuration (config-register-temp)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.2(15)ZJ

Cisco
                                          						SIP SRST 3.0

This
                                          						command was introduced.

12.3(4)T

Cisco
                                          						SIP SRST 3.0

This
                                          						command was integrated into Cisco IOS Release 12.3(4)T.

12.4(4)T

Cisco
                                          						CME 3.4 Cisco SIP SRST 3.4

This
                                          						command was added to Cisco CallManager Express (Cisco CME).

Cisco
                                          						IOS XE Fuji 16.7.1

Unified CME 12.1

This
                                          						command was supported in voice register template configuration mode.

### Usage Guidelines

The cor command
                              		  sets the dial-peer COR parameter for dynamically created VoIP dial peers. A
                              		  list-based mechanism assigns COR parameters to specific set of number ranges.
                              		  The COR functionality provides the ability to deny certain call attempts on the
                              		  basis of the incoming and outgoing class of restrictions provisioned on the
                              		  dial peers. This functionality provides flexibility in network design, allows
                              		  users to block calls (for example, calls to 900 numbers), and applies different
                              		  restrictions to call attempts from different originators.

COR specifies
                              		  which incoming dial peer can use which outgoing dial peer to make a call. Each
                              		  dial peer can be provisioned with an incoming and an outgoing COR list.

A default COR
                              		  is assigned to the directory numbers that do not match any COR list number or
                              		  number range. During Cisco Unified Session Initiation Protocol (SIP) Survivable
                              		  Remote Site Telephony (SRST) registration, a dial peer is created and that dial
                              		  peer includes a default COR value. The cor command allows you to change the automatically selected
                              		  default.

In dial-peer
                              		  configuration mode, build your COR list and add members. Then in voice register
                              		  pool configuration mode, use the cor command to apply the name of the dial-peer COR list.

If the cor command is configured under voice register template and voice
                              		  register pool configuration modes, precedence is for the COR configuration
                              		  under voice register pool configuration mode.

You can have up
                              		  to four COR lists for the Cisco Unified SIP SRST configuration, comprised of
                              		  incoming or outgoing dial peers. The first four COR lists are applied to a
                              		  range of phone numbers. The phone numbers that do not have a COR list
                              		  configuration are assigned to the default COR list, providing that a default
                              		  COR list has been defined.

## Examples

The following
                              		  is sample output from the show running-config command:

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

The following
                              		  is a sample output of the show running-config for COR configured under voice register template configuration
                              		  mode.

```
..
voice register template 1
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
```

### Related Commands

Command

Description

dial-peer cor custom

Specifies that named CORs apply to dial peers.

dial-peer cor list

Defines a COR list name.

id (voice register pool)

Explicitly identifies a locally available individual Cisco SIP IP phone, or
                                          						when running Cisco Unified SIP SRST, set of Cisco SIP IP phones.

member (dial-peer cor list)

Adds
                                          						a member to a dial-peer COR list.

name (dial-peer custom cor)

Provides a name for a custom COR.

show dial-peer voice

Displays information for voice dial peers.

## corlist

This command was previously documented as the cor command.

To apply a class of restriction (COR) to the dial peers associated
                              		  with a Cisco CME extension (ephone-dn), use the corlist command in ephone-dn configuration mode. To disable the COR associated
                              		  with an extension, use the no form of this command.

corlist { incoming | outgoing } corlist-name

no corlist { incoming | outgoing }

### Syntax Description

incoming

Specifies a COR list to be used by incoming dial peers.

outgoing

Specifies a COR list to be used by outgoing dial peers.

corlist - name

COR list name.

### Command Default

No COR is used by the dial peers associated with the extension that
                              		  is being configured.

### Command Modes

Ephone-dn configuration (config-ephone-dn)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(2)XT

Cisco ITS 2.0

This command was introduced on the Cisco 1750, Cisco 1751,
                                          						Cisco 2600 series, Cisco 3600 series, and Cisco IAD2420 series.

12.2(8)T

Cisco ITS 2.0

This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725 and Cisco 3745.

12.2(8)T1

Cisco ITS 2.0

This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691.

12.2(11)T

Cisco ITS 2.01

This command was implemented on the Cisco 1760.

### Usage Guidelines

COR is used to specify which incoming ephone-dn dial peer can use
                              		  which outgoing ephone-dn dial peer to make a call. COR denies certain call
                              		  attempts on the basis of the incoming and outgoing class of restrictions that
                              		  have been provisioned on the dial peers. This functionality provides
                              		  flexibility in network design, allows administrators to block calls (for
                              		  example, calls to 900 numbers), and applies different restrictions to call
                              		  attempts from different originators.

Each dial peer can be provisioned with an incoming and an outgoing
                              		  COR list.

The corlist incoming and corlist outgoing commands in dial-peer configuration mode
                              		  perform these functions for dial peers that are not associated with ephone-dns.
                              		  The dial-peer cor list and member commands define the sets of
                              		  capabilities, or COR lists, that are referred to in the corlist commands.

## Examples

The following example shows how to set a COR parameter for incoming
                              		  calls to dial peers associated with the extension that has the dn-tag 1:

```
Router(config)# ephone-dn 1 Router(config-ephone-dn)# corlist incoming corlist1
```

### Related Commands

Command

Description

corlist incoming

Specifies the COR list to be used when a specified dial
                                          						peer acts as the incoming dial peer.

corlist outgoing

Specifies the COR list to be used by an outgoing dial peer.

dial - peer cor list

Defines a COR list name.

## create cnf-files

To build the eXtensible Markup Language (XML) configuration files
                              		  that are required for IP phones in Cisco Unified CME, use the create cnf - files command in
                              		  telephony-service configuration mode. To remove the configuration files and
                              		  disable the automatic generation of configuration files, use the no form of this command.

create cnf-files

no create cnf-files

### Syntax Description

This command has no arguments or keywords.

### Command Default

Required XML configuration files are not built.

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

This command was modified to interact with the cnf-file command and the cnf-file location command.

12.4(9)T

Cisco Unified CME 4.0

Modifications to this command for interacting with the cnf-file command and the cnf-file location command were integrated into
                                          						Cisco IOS Release 12.4(9)T.

### Usage Guidelines

Use this command to generate the XML configuration files used for
                              		  provisioning SCCP phones and write the files to the location specified with the cnf-file location command.

## Examples

The following example builds the necessary XML configuration files on
                              		  the Cisco Unified CME router:

```
Router(config)# telephony-service Router(config-telephony)# create cnf-files
```

### Related Commands

Command

Description

cnf-file

Specifies the type of configuration file to be created.

cnf-file location

Specifies a storage location for phone configuration files

## create cnf-files (voice-gateway)

To generate the eXtensible Markup Language (XML) configuration files
                              		  that are required to autoconfigure the Cisco voice gateway, use the create cnf - files command in
                              		  voice-gateway configuration mode. To disable the generating of configuration
                              		  files, use the no form of this command.

create cnf-files

no create cnf-files

### Syntax Description

This command has no arguments or keywords.

### Command Default

Required XML configuration files are not built.

### Command Modes

Voice-gateway configuration (config-voice-gateway)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(22)YB

Cisco Unified CME 7.1

This command was introduced.

### Usage Guidelines

Cisco Unified CME writes the XML files generated by this command to
                              		  the location specified with the cnf-file location command, or to the default location in
                              		  system:/its/. The voice gateway downloads its configuration file from Cisco
                              		  Unified CME when you run the autoconfiguration process on the voice gateway.

## Examples

The following example shows that the gateway configuration files are
                              		  generated by Cisco Unified CME:

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

cnf-file location

Specifies a storage location for phone configuration files.

reset (voice-gateway)

Performs a complete reboot of all analog phones associated
                                          						with the voice gateway and registered to Cisco Unified CME.

restart (voice-gateway)

Performs a fast restart of all analog phones associated
                                          						with the voice gateway and registered to Cisco Unified CME.

## create profile (voice register global)

To generate the configuration profile files required for SIP phones,
                              		  use the create profile command in voice register global
                              		  configuration mode. To return to the default, use the no form of this command.

create profile

no create profile

### Syntax Description

This command has no arguments or keywords.

### Command Default

Configuration files are not generated.

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

This command generates the configuration files used for provisioning
                              		  SIP phones and writes the files to the location specified with the tftp-path command.

## Examples

The following example shows how to create the configuration profile:

```
Router(config)# voice register global Router(config-register-global)# mode cme Router(config-register-global)# create profile
```

### Related Commands

Command

Description

file text (voice register global)

Generates ASCII text files for SIP phones.

mode (voice register global)

Enables the mode for provisioning SIP phones in a Cisco
                                          						CallManager Express (Cisco CME) system.

reset (voice register global)

Performs a complete reboot of all SIP phones associated
                                          						with a Cisco CME router.

source-address (voice register global)

Identifies the IP address and port through which SIP phones
                                          						communicate with a Cisco CME router.

tftp-path (voice register global)

Specifies the directory to which the provisioning file for
                                          						SIP phones in a Cisco CallManager Express (Cisco CME) system will be written.

## credentials

To enter
                              		  credentials configuration mode to configure a certificate for a Cisco Unified
                              		  CME CTL provider or for Cisco Unified SRST router communication to Cisco
                              		  Unified CallManager, use the credentials command in global configuration mode. To set all commands in
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

Global configuration (config)

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
                                          						command was introduced for Cisco SRST.

12.4(4)XC

Cisco
                                          						Unified CME 4.0

This
                                          						command was introduced for Cisco Unified CME.

12.4(9)T

Cisco
                                          						Unified CME 4.0

This
                                          						command for Cisco Unified CME was integrated into Cisco IOS Release 12.4(9)T.

Cisco IOS XE Fuji 16.7.1 Release

Unified SRST 12.1

This command was introduced for Unified SRST support on
                                          						Cisco 4000 Series Integrated Services Router.

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
                              		  authentication is necessary. When the client, Cisco Unified CallManager,
                              		  requests a certificate, the credentials server provides the certificate. Cisco
                              		  Unified CallManager exports the certificate to the phone, and the Cisco Unified
                              		  IP phone holds the SRST router certificate in its configuration file. The
                              		  device certificate for secure SRST routers is placed in the configuration file
                              		  of the Cisco Unified IP phone because the entry limit in the certificate trust
                              		  list (CTL) of Cisco Unified CallManager is 32.

Credentials
                              		  service for SRST runs on default port 2445. Cisco Unified CallManager connects
                              		  to port 2445 on the secure SRST router and retrieves the secure SRST device
                              		  certificate during the TLS handshake.

Activate this
                              		  command on all SRST routers.

For security
                                          			 reasons, credentials service should be deactivated on all SRST routers after
                                          			 provisioning to Cisco Unified CallManager is completed.

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
                                          						CallManager.

ip source-address (credentials)

Enables the Cisco Unified CME or SRST router to receive messages through the
                                          						specified IP address and port.

show credentials

Displays the credentials settings on a Cisco Unified CME or SRST router.

trustpoint (credentials)

Specifies the name of the trustpoint to be associated with a Cisco Unified CME
                                          						CTL provider certificate or with an SRST router certificate.

## cti csta mode basic

To set the CTI interface in Cisco Unified CME into basic mode, use
                              		  the cti csta mode basic command in voice-service configuration mode.
                              		  To return to default, use the no form of this command.

cti csta mode basic

no cti csta mode basic

### Syntax Description

This command has no arguments or keywords.

### Command Default

CTI interface is in advanced mode.

### Command Modes

Voice-service configuration (config-voi-serv)

## Command History

Release

Cisco Product

Modification

15.0(1)XA

Cisco Unified CME 8.0

This command was introduced.

15.1(1)T

Cisco Unified CME 8.0

This command was integrated into Cisco IOS Release
                                          						15.1.(1)T.

Cisco IOS XE Gibraltar 16.11.1a Release

Unified CME 12.6

This command was deprecated. It is not supportd on Unified CME 12.6 and later releases.

### Usage Guidelines

This command supresses all enhanced extensions/features, such as
                              		  shared line and shared media, in a CTI message from Cisco Unified CME.

This command is required if the computer-based CSTA client
                              		  application that is interacting with Cisco Unified CME is a Microsoft Office
                              		  Communicator (MOC) client .

## Examples

The following example shows a voice-service configuration with this
                              		  command enabled:

```
!
voice service voip 
 no cti shutdown
 cti csta mode basic
!
```

### Related Commands

Command

Description

cti shutdown

Disables CTI integration.

## cti message device-id suppress-conversion

To suppress the conversion or promotion of all extension numbers
                              		  except the primary number in a CTI message, use the cti message device-id suppress-conversion command in voice-service
                              		  configuration mode. To return to default, use the no form of this command.

cti message device-id suppress-conversion

no cti message device-id suppress-conversion

### Syntax Description

This command has no arguments or keywords.

### Command Default

All SCCP extension numbers are converted or promoted in CTI messages.

### Command Modes

Voice-service configuration (config-voi-serv)

## Command History

Release

Cisco Product

Modification

15.0(1)XA

Cisco Unified CME 8.0

This command was introduced.

15.1(1)T

Cisco Unified CME 8.0

This command was integrated into Cisco IOS Release
                                          						15.1(1)T.

Cisco IOS XE Gibraltar 16.11.1a Release

Unified CME 12.6

This command was deprecated. It is not supportd on Unified CME 12.6 and later releases.

### Usage Guidelines

This command specifies that only the requested (primary) extension
                              		  number is converted or promoted in the outgoing CTI message when an expanded
                              		  number is presented in a RequestSystemStatus from a CSTAclient application. Use
                              		  this command to suppress the conversion or promotion of all secondary numbers
                              		  in a CTI message.

By default, Cisco Unified CME converts or promotes all SCCP primary
                              		  and secondary extension numbers when reporting events.

## Examples

The following example shows the voice-service configuration with this
                              		  command enabled:

```
!
voice service voip 
 no cti shutdown
 cti csta mode basic
 cti message device-id suppress-conversion
```

### Related Commands

Command

Description

cti shutdown

Disables CTI integration.

## cti notify

To force an ephone-dn into a constant “up” state, use the cti notify command in ephone-dn or ephone-dn-template
                              		  configuration mode. To return to default, use the no form of this command.

cti notify

no cti notify

### Syntax Description

This command has no arguments or keywords.

### Command Default

Cisco Unified CME cannot send notifications to the ephone-dn because
                              		  a CTI session cannot be established.

### Command Modes

Ephone-dn configuration (config-ephone-dn)

Ephone-dn-template configuration (config-ephone-dn-template)

## Command History

Release

Cisco Product

Modification

15.0(1)XA

Cisco Unified CME 8.0

This command was introduced.

15.1(1)T

Cisco Unified CME 8.0

This command was integrated into Cisco IOS Release
                                          						15.1(1)T.

Cisco IOS XE Gibraltar 16.11.1a Release

Unified CME 12.6

This command was deprecated. It is not supportd on Unified CME 12.6 and later releases.

### Usage Guidelines

This command forces an ephone-dn into a constant “up” state.

Use this command to permit a CTI session to be established with a
                              		  directory number that is not associated with a physical device, allowing Cisco
                              		  Unified CME to send notifications to the directory number. If a directory
                              		  number is not associated to an ephone configuration that includes the button
                              		  command, a static fwd is applied to the directory number and all incoming calls
                              		  are forwarded to another directory number.

If you use an ephone-dn template to apply this command to a directory
                              		  number and you also use this command in ephone-dn configuration mode for the
                              		  same directory number, the value that you set in ephone-dn configuration mode
                              		  has priority.

## Examples

The following example shows the configuration for ephone-dn 4
                              		  including this command. A CTI session can be established for this directory
                              		  number (204) even though the number is not associated with an ephone
                              		  configuration because this directory number is always “up.”

```
!
ephone-dn  4
 number 204
 cti notify
 cti watch
!
!
ephone  1
 mac-address 001E.4A34.A35F
 type 7961
 button  1:1
!
!
!
ephone  2
 mac-address 000F.8FC7.B681
 type 7960
 button  1:2
!
!
!
ephone  3
 mac-address 0019.E7FF.1E30
 type 7961
 logout-profile 1
!
```

The following example shows how to create the same configuration for
                              		  ephone-dn 4 using this command in ephone-dn template configuration mode and
                              		  then applying the template to the directory number:

```
ephone-dn-template 15
 cti notify
 cti watch
ephone-dn 4
 number 204
 ephone-dn-template 15
```

### Related Commands

Command

Description

ephone-dn-template (ephone-dn)

Applies an ephone-dn template to an ephone-dn.

## cti watch

To allow a CSTA client application to monitor and control a directory
                              		  number in Cisco Unified CME, use the cti watch command in ephone-dn or ephone-dn-template
                              		  configuration mode. To return to default, use the no form of this command.

cti watch

no cti watch

### Syntax Description

This command has no arguments or keywords.

### Command Default

A CSTA client application cannot use the CTI interface to montitor
                              		  and control an ephone-dn in Cisco Unified CME.

### Command Modes

Ephone-dn configuration (config-ephone-dn)

Ephone-dn-template configuration (config-ephone-dn-template)

## Command History

Release

Cisco Product

Modification

15.0(1)XA

Cisco Unified CME 8.0

This command was introduced.

15.1(1)T

Cisco Unified CME 8.0

This command was integrated into Cisco IOS Release
                                          						15.1(1)T.

Cisco IOS XE Gibraltar 16.11.1a Release

Unified CME 12.6

This command was deprecated. It is not supportd on Unified CME 12.6 and later releases.

### Usage Guidelines

This command enables a CSTA client application to monitor and control
                              		  a directory number in Cisco Unified CME.

If you use an ephone-dn template to apply this command to a directory
                              		  number and you also use this command in ephone-dn configuration mode for the
                              		  same directory number, the value that you set in ephone-dn configuration mode
                              		  has priority.

## Examples

The following example shows the configuration for ephone-dn 4 with
                              		  this command configured. The CSTA application can montior and control the
                              		  directory number (204).

```
!
ephone-dn  4
 number 204
 cti notify
 cti watch
```

The following example shows how to create the same configuration for
                              		  ephone-dn 4 using this command in ephone-dn template configuration mode and
                              		  applying the template to the directory number:

```
ephone-dn-template 15
 cti notify
 cti watch
ephone-dn 4
 number 204
 ephone-dn-template 15
```

### Related Commands

Command

Description

ephone-dn-template (ephone-dn)

Applies an ephone-dn template to an ephone-dn

## cti-aware

To bind a session to the CTI subsystem, use the cti aware command in voice session-server configuration mode. To return
                              		  to default, use the no form of this command.

cti-aware

no cti-aware

### Syntax Description

This command has no keywords or arguments.

### Command Default

CTI-register heartbeat continues even after the CTI session is
                              		  shutdown.

### Command Modes

Voice session-server configuration (config-register-fs)

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

Cisco IOS XE Gibraltar 16.11.1a Release

Unified CME 12.6

This command was deprecated. It is not supportd on Unified CME 12.6 and later releases.

### Usage Guidelines

This command causes the CSTA SIP keepalive response to stop if the
                              		  CTI session between Cisco Unified CME and the CSTA client application expires
                              		  or is down for any reason. By default, the CSTA SIP keepalive response
                              		  continues even after the CTI session expires and the CSTA client application is
                              		  unaware that the CTI session is not operational.

## Examples

The following partial output shows the configuration for a session
                              		  manager for a CSTA client application in which this command is configured:

```
router# show running-configuration .
.
.
voice register session-server 1 
 register-id app1 
 keepalive 360
 cti-aware
```

### Related Commands

Command

Description

keepalive (voice register session-server)

Duration for registration after which the registration
                                          						expires unless the feature server or application reregisters before the
                                          						registration expiry.

register-id

Creats an ID for explicitly identifying an external feature
                                          						server or application during Register requests

## ctl-client

To enter CTL-client configuration mode to set parameters for the CTL
                              		  client, use the ctl-client command in global configuration
                              		  mode. To return to the default, use the no form of this command.

ctl-client

no ctl-client

### Syntax Description

This command has no keywords or arguments.

### Command Default

No CTL-client parameters are set.

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

This command is used with Cisco Unified CME phone authentication.

## Examples

The following example defines server IP addresses and trustpoints for
                              		  the CAPF server, the Cisco Unified CME router, and the TFTP server, as well as
                              		  trustpoints for SAST1 and SAST2. It also specifies that a new CTL file should
                              		  be generated.

```
Router(config)# ctl-client Router(config-ctl-client)# server capf 10.2.2.2 trustpoint capftrust Router(config-ctl-client)# server cme 10.2.2.3 trustpoint cmetp Router(config-ctl-client)# server tftp 10.2.2.4 trustpoint tftptp Router(config-ctl-client)# sast1 trustpoint sast1tp Router(config-ctl-client)# sast2 trustpoint sast2tp Router(config-ctl-client)# regenerate
```

## ctl-service admin

To specify a user name and password to authenticate the client during
                              		  the CTL protocol, use the ctl-service admin command in credentials configuration mode. To return to the
                              		  default, use the no form of this command.

ctl-service admin username secret { 0 | 1 } password-string

no ctl-service admin

### Syntax Description

username

Defines the name that will be used to authenticate the
                                          						client.

secret { 0 | 1 }

Defines a character string for login authentication and
                                          						whether it will be encrypted when it is stored in the running configuration.

- 0 —Not encrypted.

- 1 —Encrypted using Message
                                             						  Digest 5 (MD5).

password-string

Character string for login authentication

### Command Default

No user name or password is defined for authentication.

### Command Modes

Credentials configuration (config-credentials)

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

This command is used with Cisco Unified CME phone authentication to
                              		  define a user who will be used to authenticate the CTL client with a CTL
                              		  provider.

## Examples

The following example creates a CTL provider on a Cisco Unified CME
                              		  router that is not running the CTL client.

```
Router(config)# credentials Router(config-credentials)# ip source-address 172.19.245.1 port 2444 Router(config-credentials)# trustpoint ctlpv Router(config-credentials)# ctl-service admin user4 secret 0 c89L8o
```

Command

Description

debug credentials

Sets debugging on the credentials service that runs between a
                                       					 Cisco Unified CME CTL provider and the CTL client or between an SRST router and
                                       					 Cisco Unified CallManager.

show credentials

Displays the credentials settings on a Cisco Unified CME or
                                       					 SRST router.

trustpoint (credentials)

Specifies the name of the trustpoint to be associated with a
                                       					 Cisco Unified CME CTL provider certificate or with an SRST router certificate.

| menu-number | Number that callers must dial to reach the pilot number of
                                          						an ephone hunt group. The range is from 1to 10. The default is 1. |
|---|---|
| application-name | Application name given to the call queue script in the call application voice command. |
| pilot-number | Ephone hunt group pilot number. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(11)XL | Cisco CME 3.2.1 | This command was introduced. |
| 12.3(14)T | Cisco CME 3.2.2 | This command was integrated into Cisco IOS Release
                                          						12.3(14)T. |
| 12.3(14)T | Cisco CME 3.3 | This command was replaced with the param aa-hunt command. |

| Command | Description |
|---|---|
| call application voice | Defines a name for a voice application and specifies the
                                          						location of the Tcl or VoiceXML document to load for this application. |
| call application voice aa-pilot | Associates an ephone hunt group with the Cisco CME basic
                                          						service’s AA script by declaring the group’s pilot number. |
| call application voice welcome-prompt | Assigns an audio file that is used by a Cisco CME B-ACD AA
                                          						script for the welcome greeting. |
| ephone-dn | Enters ephone-dn configuration mode for the purposes of
                                          						creating and configuring an extension for a Cisco IP phone line. |
| ephone-hunt | Enters ephone-hunt configuration mode for the purposes of
                                          						creating and configuring a hunt group for use in a Cisco CME system. |
| pilot | Defines the ephone-dn that callers dial to reach a Cisco
                                          						CME ephone hunt group. |

| application-name | Application name given to the call queue script in the call application voice command . |
|---|---|
| aa-script-name | Application name given to the AA script in the call application voice command . |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(11)XL | Cisco CME 3.2.1 | This command was introduced. |
| 12.3(14)T | Cisco CME 3.2.2 | This command was integrated into Cisco IOS Release
                                          						12.3(14)T. |
| 12.3(14)T | Cisco CME 3.3 | This command was replaced with the param aa-name command. |

| Command | Description |
|---|---|
| call application voice | Defines a name for a voice application and specifies the
                                          						location of the Tcl or VoiceXML document to load for this application. |
| call application voice service-name | Associates a Cisco CME B-ACD AA script with a Cisco Unified
                                          						CME B-ACD call queue script. |

| application-name | Application name given to the auto-attendant (AA) script in
                                          						the call application voice command . |
|---|---|
| pilot-number | Pilot number for Cisco CME B-ACD. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(11)XL | Cisco CME 3.2.1 | This command was introduced. |
| 12.3(14)T | Cisco CME 3.2.2 | This command was integrated into Cisco IOS Release
                                          						12.3(14)T. |
| 12.3(14)T | Cisco CME 3.3 | This command was replaced by the param aa-pilot command. |

| Command | Description |
|---|---|
| call application voice | Defines a name for a voice application and specifies the
                                          						location of the Tcl or VoiceXML document to load for this application. |
| dial-peer voice | Defines a particular dial peer, specifies the method of
                                          						voice encapsulation, and enters dial-peer configuration mode. |
| ephone-dn | Enters ephone-dn configuration mode for the purposes of
                                          						creating and configuring an extension for a Cisco IP phone line. |
| ephone-hunt | Enters ephone-hunt configuration mode for the purposes of
                                          						creating and configuring a hunt group for use in a Cisco Unified CME system. |

| application-name | Application name given to the auto-attendant (AA) script in
                                          						the call application voice command . |
|---|---|
| seconds | Number of seconds that a call must wait before attempting
                                          						to transfer an ephone hunt pilot number or voice-mail pilot number. The range
                                          						is from 5 to 30 seconds. The default is 15 seconds. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(11)XL | Cisco CME 3.2.1 | This command was introduced. |
| 12.3(14)T | Cisco CME 3.2.2 | This command was integrated into Cisco IOS Release
                                          						12.3(14)T. |
| 12.3(14)T | Cisco CME 3.3 | This command was replaced by the param call-retry-timer command |

| Command | Description |
|---|---|
| ephone-dn | Enters ephone-dn configuration mode for the purposes of
                                          						creating and configuring an extension for a Cisco IP phone line. |
| ephone-hunt | Enters ephone-hunt configuration mode for the purposes of
                                          						creating and configuring a hunt group for use in a Cisco Unified CME system. |
| call application voice | Defines a name for a voice application and specifies the
                                          						location of the Tcl or VoiceXML document to load for this application. |
| call application voice aa-hunt | Declares a Cisco Unified CME B-ACD menu number and
                                          						associates it with the pilot number of an ephone hunt group. |
| call application voice aa-pilot | Associates an ephone hunt group with the Cisco Unified CME
                                          						basic service’s AA script by declaring the group’s pilot number |
| call application voice max-time-call-retry | Assigns the maximum length of time for which calls to Cisco
                                          						Unified CME B-ACD can stay in a call queue. |

| application-name | Application name given to the auto-attendant (AA) script in
                                          						the call application voice command . |
|---|---|
| number | The single digit that callers press to be able to enter an
                                          						extension number from the AA menu. The range is from 1 to 10. There is no
                                          						default. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(11)XL | Cisco CME 3.2.1 | This command was introduced. |
| 12.3(14)T | Cisco CME 3.2.2 | This command was integrated into Cisco IOS Release
                                          						12.3(14)T. |
| 12.3(14)T | Cisco CME 3.3 | This command was replaced by the param dial-by-extension-option command. |

| Command | Description |
|---|---|
| call application voice | Defines a name for a voice application and specifies the
                                          						location of the Tcl or VoiceXML document to load for this application. |

| application-name | Application name given to the auto attendant (AA) script in
                                          						the call application voice command . |
|---|---|
| seconds | Maximum length of time that the Cisco Unified CME B-ACD AA
                                          						script can keep redialing an ephone hunt group pilot number. The range is from
                                          						0 to 3600 seconds. The default is 600 seconds. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(11)XL | Cisco CME 3.2.1 | This command was introduced. |
| 12.3(14)T | Cisco CME 3.2.2 | This command was integrated into Cisco IOS Release
                                          						12.3(14)T. |
| 12.3(14)T | Cisco CME 3.3 | This command was replaced by the param max-time-call-retry command. |

| Command | Description |
|---|---|
| call application voice | Defines a name for a voice application and specifies the
                                          						location of the Tcl or VoiceXML document to load for this application. |
| call application voice call-retry-timer | Assigns the length of time that calls to Cisco Unified CME
                                          						B-ACD must wait before attempting to transfer to an ephone hunt-group pilot
                                          						number or to voice mail. |
| call application voice max-time-vm-retry | Assigns the maximum number of times that calls to Cisco
                                          						Unified CME B-ACD can attempt to reach voice mail. |
| ephone-dn | Enters ephone-dn configuration mode for the purposes of
                                          						creating and configuring an extension for a Cisco IP phone line. |
| ephone-hunt | Enters ephone-hunt configuration mode for the purposes of
                                          						creating and configuring a hunt group for use in a Cisco Unified CME system. |

| application-name | Application name given to the auto-attendant (AA) script in
                                          						the call application voice command . |
|---|---|
| number | Number of hunt groups used by the Cisco Unified CME B-ACD
                                          						AA script and call queue script. The range is from 1 to 3. The default is 3. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(11)XL | Cisco CME 3.2.1 | This command was introduced. |
| 12.3(14)T | Cisco CME 3.2.2 | This command was integrated into Cisco IOS Release
                                          						12.3(14)T. |
| 12.3(14)T | Cisco CME 3.3 | This command was replaced by the param number-of-hunt-grps command. |

| Command | Description |
|---|---|
| call application voice | Defines a name for a voice application and specifies the
                                          						location of the Tcl or VoiceXML document to load for this application. |
| call application voice dial-by-extension-option | Enables direct extension access and sets the access number
                                          						for Cisco CME B-ACD. |
| ephone-hunt | Enters ephone-hunt configuration mode for the purposes of
                                          						creating and configuring a hunt group for use in a Cisco CME system. |

| application-name | Application name given to the call queue script in the call application voice command . |
|---|---|
| number | Number of calls that can be waiting in each ephone hunt
                                          						group’s queue. The range is dependent on your hardware configuration. The range
                                          						is from 1 to 30. The default is 10. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(11)XL | Cisco CME 3.2.1 | This command was introduced. |
| 12.3(14)T | Cisco CME 3.2.2 | This command was integrated into Cisco IOS Release
                                          						12.3(14)T. |
| 12.3(14)T | Cisco CME 3.3 | This command was replaced by the param queue-len command. |

| Command | Description |
|---|---|
| call application voice | Defines a name for a voice application and specifies the
                                          						location of the Tcl or VoiceXML document to load for this application. |
| call application voice call-retry-timer | Assigns the length of time that calls to Cisco CME B-ACD
                                          						must wait before attempting to transfer to an ephone hunt-group pilot number or
                                          						to voice mail. |
| ephone-dn | Enters ephone-dn configuration mode for the purposes of
                                          						creating and configuring an extension for a Cisco IP phone line. |
| ephone-hunt | Enters ephone-hunt configuration mode for the purposes of
                                          						creating and configuring a hunt group for use in a Cisco CME system. |

| application-name | Application name given to the call queue script in the call application voice command . |
|---|---|
| 0 | Disables debugging. |
| 1 | Enables debugging. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(11)XL | Cisco CME 3.2.1 | This command was introduced. |
| 12.3(14)T | Cisco CME 3.2.2 | This command was integrated into Cisco IOS Release
                                          						12.3(14)T. |
| 12.3(14)T | Cisco CME 3.3 | This command was replaced by the param queue-manager-debugs command. |

| Command | Description |
|---|---|
| call application voice | Defines a name for a voice application and specifies the
                                          						location of the Tcl or VoiceXML document to load for this application. |
| debug voip ivr script | Display debugging messages for IVR scripts. |

| application-name | Application name given to the auto-attendant (AA) script in
                                          						the call application voice command . |
|---|---|
| seconds | Amount of time that second-greeting message must wait
                                          						before it can be played. The range is from 30 to 120 seconds. The default is 60
                                          						seconds. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(11)XL | Cisco CME 3.2.1 | This command was introduced. |
| 12.3(14)T | Cisco CME 3.2.2 | This command was integrated into Cisco IOS Release
                                          						12.3(14)T. |
| 12.3(14)T | Cisco CME 3.3 | This command was replaced by the param second-greeting-time command. |

| Command | Description |
|---|---|
| call application voice | Defines a name for a voice application and specifies the
                                          						location of the Tcl or VoiceXML document to load for this application. |
| ephone-dn | Enters ephone-dn configuration mode for the purposes of
                                          						creating and configuring an extension for a Cisco IP phone line. |
| ephone-hunt | Enters ephone-hunt configuration mode for the purposes of
                                          						creating and configuring a hunt group for use in a Cisco CME system. |

| application-name | Application name given to the auto attendant (AA) script in
                                          						the call application voice command . |
|---|---|
| number | Pilot number of the voice mail to which calls to Cisco CME
                                          						B-ACD will be transferred. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(11)XL | Cisco CME 3.2.1 | This command was introduced. |
| 12.3(14)T | Cisco CME 3.2.2 | This command was integrated into Cisco IOS Release
                                          						12.3(14)T. |
| 12.3(14)T | Cisco CME 3.3 | This command was replaced by the param voice-mail command. |

| Command | Description |
|---|---|
| call application voice | Defines a name for a voice application and specifies the
                                          						location of the Tcl or VoiceXML document to load for this application. |

| application-name | Application name given to the AA script in the call application voice command . |
|---|---|
| _ audio-filename | Filename of the welcome greeting to be played when callers
                                          						first reach the Cisco Unified CME B-ACD, preceded by the underscore (_)
                                          						character. The filename must not have a language code prefix, such as “en,” for
                                          						English. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(11)XL | Cisco CME 3.2.1 | This command was introduced. |
| 12.3(14)T | Cisco CME 3.2.2 | This command was integrated into Cisco IOS Release
                                          						12.3(14)T. |
| 12.3(14)T | Cisco CME 3.3 | This command was replaced by the param welcome-prompt command. |

| Command | Description |
|---|---|
| call application voice | Defines a name for a voice application and specifies the
                                          						location of the Tcl or VoiceXML document to load for this application. |
| call application voice aa-name | Associates a Cisco CME B-ACD call queue script with a Cisco
                                          						Unified CME B-ACD AA script |
| call application voice service-name | Associates a Cisco CME B-ACD AA script with a Cisco Unified
                                          						CME B-ACD call queue script. |

| number | Identifier of the E.164 default number to contact if a 911
                                          						callback fails. |
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
| elin | E.164 number used as the default ELIN if no matching ERL to
                                          						the 911 caller’s IP phone address is found. |
| expiry | Number of minutes a 911 call is associated to an ELIN in
                                          						case of a callback from the 911 operator. |
| logging | Syslog informational message printed to the console every
                                          						time an emergency call is made. |
| voice emergency response settings | Creates a tag for identifying settings for E911 behavior. |

| local | Local caller ID for redirected calls. |
|---|---|
| passthrough | Original caller ID. Default. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ3 | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| loopback-dn | Creates a virtual loopback voice port (loopback-dn) to
                                          						establish a demarcation point for VoIP voice calls and supplementary services. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco ITS 1.0 | This command was introduced |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was made available in ephone-dn-template
                                          						configuration mode. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command in ephone-dn-template configuration mode was
                                          						integrated into Cisco IOS Release 12.4(9)T. |

| Note | This command is not valid for ephone-dns that are being used for
                                       		  loopback. |
|---|---|

| Command | Description |
|---|---|
| clid strip | Prevents display of caller-ID number on calls to VoIP. |
| clid strip name | Prevents display of caller-ID name on calls to VoIP. |
| ephone-dn-template (ephone-dn) | Applies ephone-dn template to an ephone dn. |

| Note | Effective with Cisco IOS Release 12.4(11)XJ, the caller id block (voice register template) command is not available in Cisco IOS
                                       		  software. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |
| 12.4(11)XJ | Cisco Unified CME 4.1 | This command was removed. |
| 12.4(15)T | Cisco Unified CME 4.1 | This command was removed in Cisco IOS Release 12.4(15)T. |

| Command | Description |
|---|---|
| anonymous block (voice register template) | Enables anonymous call blocking in a SIP phone template. |
| template (voice register pool) | Applies a template to a SIP phone. |
| voice register template | Enters voice register template configuration mode and
                                          						defines a template of common parameters for SIP phones. |

| code-string | Character string to dial to enable blocking of caller ID
                                          						display on selected outgoing calls. The first character must be an asterisk (*)
                                          						and the remaining characters must be digits. The string can contain a maximum
                                          						of 16 characters. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| telephony-service | Enters telephony-service configuration mode. |

| cfwdall | Call Forward All (CfwdAll) soft key. |
|---|---|
| gpickup | Group Pickup (GPickUp) soft key. |
| pickup | Local Pickup (PickUp) soft key. |
| service-uri | URI that is requested when the specified soft key is
                                          						pressed. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XJ | Cisco Unified CME 4.1 | This command was introduced. |
| 12.4(15)T | Cisco Unified CME 4.1 | This command was integrated into Cisco IOS Release
                                          						12.4(15)T. |
| 12.4(22)YB | Cisco Unified CME 7.1 | The gpickup and pickup keywords were added. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command has been integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| call-forward b2bua all | Enables call forwarding for a SIP back-to-back user agent
                                          						(B2BUA) so that all incoming calls are forwarded to another extension. |
| reset (voice register global) | Performs a complete reboot of all SIP phones associated
                                          						with a Cisco Unified CME router. |
| reset (voice register pool) | Performs a complete reboot of one phone associated with a
                                          						Cisco Unified CME router. |
| restart (voice register) | Performs a fast restart of one or all SIP phones associated
                                          						with a Cisco Unified CME router. |
| service directed-pickup | Enables Directed Call Pickup and modifies the function of
                                          						the PickUp and GPickUp soft keys. |

| system | Call forward system parameter. |
|---|---|
| redirecting-expanded | Expand redirecting extensions to an E.164 number. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| Command | Description |
|---|---|
| dialplan-pattern | Create global prefix for expanding extension numbers of
                                          						forward-to and transfer-to targets. |
| show telephony-service dial-peer | Displays dial peer information for extensions in a Cisco
                                          						Unified CME system. |

| system | Call forward system parameter. |
|---|---|
| redirecting-expanded | Redirecting extension is to be expanded to an E.164 number. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release 12.4(9). |

| Command | Description |
|---|---|
| dialplan-pattern (voice register) | Create global prefix for expanding extension numbers of
                                          						forward-to and transfer-to targets if the target is an extension on a SIP
                                          						phone. |
| show voice register dial-peer | Displays dial peer information for extensions in a Cisco
                                          						Unified CME system. |

| directory number | Directory number to which calls are forwarded. Represents a
                                          						fully qualified E.164 number. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco ITS 1.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was made available in ephone-dn-template
                                          						configuration mode. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command in ephone-dn-template configuration mode was
                                          						integrated into Cisco IOS Release 12.4(9)T. |

| Note | The call forward all command takes precedence over the call-forward busy and call-forward noan commands. |
|---|---|

| Command | Description |
|---|---|
| call forward busy | Configures call forwarding to another number when a Cisco
                                          						Unified IP phone is busy. |
| call forward noan | Configures call forwarding to another number when no answer
                                          						is received from a Cisco Unified IP phone. |
| ephone dn-template (ephone-dn) | Applies template to ephone-dn. |

| directory number | Telephone number to which calls are forwarded. Represents a
                                          						fully qualified E.164 number. Maximum length of the telephone number is 32. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was introduced. |
| 12.4(11)XJ | Cisco Unified CME 4.1 | This command was removed from voice register pool
                                          						configuration mode for Cisco Unified CME only. |
| 12.4(15)T | Cisco Unified CME 4.1 | Command with modifications was integrated into Cisco IOS
                                          						release 12.4(15)T. |

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
| call-waiting (voice register pool) | Enables call waiting on a SIP phone. |

| directory number | Telephone number to which calls are forwarded. Represents a
                                          						fully qualified E.164 number. Maximum length of the telephone number is 32. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was introduced. |
| 12.4(11)XJ | Cisco Unified CME 4.1 | This command was removed from voice register pool
                                          						configuration mode for Cisco Unified CME only. |
| 12.4(15)T | Cisco Unified CME 4.1 | This command with modifications was integrated into Cisco
                                          						IOS Release 12.4(15)T. |

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
| call-waiting (voice register pool) | Enables call waiting on a SIP phone. |

| directory number | Telephone number to which calls are forwarded when the
                                          						forwarded destination is busy or does not answer. Represents a fully qualified
                                          						E.164 number. Maximum length of the telephone number is 32. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was introduced. |
| 12.4(11)XJ | Cisco Unified CME 4.1 | This command was removed from voice register pool
                                          						configuration mode for Cisco Unified CME only. |
| 12.4(15)T | Cisco Unified CME 4.1 | This command with modifications was integrated into Cisco
                                          						IOS Release 12.4(15)T |

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

| target-number | Phone
                                          						number to which calls are forwarded. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 15.6(3)M 16.3.1 | Cisco
                                          						Unified CME 11.5 | This
                                          						command was introduced. |

|  | Description |
|---|---|
| night-service date | Defines a recurring time period associated with a month and day during which
                                          						night service is active. |
| night-service day | Defines a recurring time period associated with a day of the week during which
                                          						night service is active. |

| directory number | Telephone number to which calls are forwarded. Represents a
                                          						fully qualified E.164 number. Maximum length of the telephone number is 32. |
|---|---|
| timeout seconds | Number of seconds that a call can ring with no answer
                                          						before the call is forwarded to another extension. Range is 3 to 60000. Default
                                          						is 20. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 Cisco SIP SRST 3.4 | This command was introduced. |
| 12.4(11)XJ | Cisco Unified CME 4.1 | This command was removed from voice register pool
                                          						configuration mode for Cisco Unified CME only. |
| 12.4(15)T | Cisco Unified CME 4.1 | This command with modifications was integrated into Cisco
                                          						IOS Release 12.4(15)T. |

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
| call-waiting (voice register pool) | Enables call waiting on a SIP phone. |

| Note | Effective with Cisco IOS Release 12.4(11)XJ, the call forward b2bua unreachable command is not available in Cisco IOS
                                       		  software. |
|---|---|

| directory number | Telephone number to which calls are forwarded. Represents a
                                          						fully qualified E.164 number. |
|---|---|

| Cisco IOS Release | Version | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |
| 12.4(11)XJ | Cisco Unified CME 4.1 | This command was removed. |
| 12.4(15)T | Cisco Unified CME 4.1 | This command was removed in Cisco IOS Release 12.4(15)T. |

| Command | Description |
|---|---|
| call-forward b2bua all (voice register dn and voice register pool) | Enables call forwarding for a SIP B2BUA so that all
                                          						incoming calls are forwarded to another extension. |
| call-forward b2bua busy (voice register dn and voice register pool) | Enables call forwarding for a SIP B2BUA so that incoming
                                          						calls to a busy extension are forwarded to another extension. |
| call-forward b2bua mailbox (voice register dn and voice register pool) | Controls the specific voice-mail box selected in a
                                          						voice-mail system at the end of a call forwarding exchange. |
| call-forward b2bua noan (voice register dn and voice register pool) | Enables call forwarding for a SIP B2BUA so that incoming
                                          						calls to an extension that does not answer after a configured amount of time
                                          						are forwarded to another extension. |
| call-waiting (voice register pool) | Enables call waiting on a SIP phone. |
| number (voice register dn) | Associates an extension number with a voice register dn. |

| target-number | Phone number to which calls are forwarded. |
|---|---|
| primary | (Optional) Call forwarding is selectively applied only to
                                          						the dial peer created for the primary number for this ephone-dn. |
| secondary | (Optional) Call forwarding is selectively applied only to
                                          						the dial peer created for the secondary number for this ephone-dn. |
| dialplan-pattern | (Optional) Call forwarding is selectively applied only to
                                          						dial peers created for this ephone-dn by the dial-plan pattern. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco ITS 1.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |
| 12.4(4)XC | Cisco Unified CME 4.0 | The primary , secondary , and dialplan-pattern keywords were
                                          						added, and this command was made available in ephone-dn-template configuration
                                          						mode. |
| 12.4(11)T | Cisco Unified CME 4.0 | This command with the primary , secondary , and dialplan-pattern keywords added,
                                          						and this command in ephone-dn-template configuration mode was integrated into
                                          						Cisco IOS 12.4(11)T. |

| Command | Description |
|---|---|
| call forward all | Configures call forwarding for all incoming calls to an
                                          						ephone-dn. |
| call-forward night-service | Configures call forwarding for all incoming calls to an
                                          						ephone-dn during the hours defined for night service. |
| call forward noan | Configures call forwarding to another number when no answer
                                          						is received from an ephone-dn. |
| ephone-dn-template (ephone-dn) | Applies template to ephone-dn. |

| length | Number of digits that can be entered using the CfwdAll soft
                                          						key on an IP phone. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(7)T | Cisco CME 3.1 | This command was introduced. |
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was made available in ephone-dn-template
                                          						configuration mode. |
| 12.4(11)T | Cisco Unified CME 4.0 | This command in ephone-dn-template configuration mode was
                                          						integrated into Cisco IOS Release 12.4(11)T. |

| Command | Description |
|---|---|
| call-forward all | Configures call forwarding for all incoming calls on one of
                                          						the lines of a Cisco Unified IP phone. |
| ephone-dn-template (ephone-dn) | Applies an ephone-dn template to an ephone-dn. |

| target-number | Phone number to which calls are forwarded. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(11)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(11)T. |

| Command | Description |
|---|---|
| call forward all | Configures call forwarding for all incoming calls to an
                                          						ephone-dn. |
| call forward busy | Configures call forwarding to another number when an
                                          						ephone-dn is busy. |
| call forward noan | Configures call forwarding to another number when no answer
                                          						is received from an ephone-dn. |
| night-service bell (ephone-dn) | Marks an ephone-dn for night-service treatment. |
| night-service date | Defines a recurring time period associated with a month and
                                          						day during which night service is active. |
| night-service day | Defines a recurring time period associated with a day of
                                          						the week during which night service is active. |

| target-number | Phone number to which calls are forwarded. |
|---|---|
| timeout seconds | Sets the duration that a call can ring with no answer
                                          						before the call is forwarded to the target number. Range is from 3 to 60000.
                                          						There is no default value. |
| primary | (Optional) Call forwarding is selectively applied only to
                                          						the dial peer created for the primary number for this ephone-dn. |
| secondary | (Optional) Call forwarding is selectively applied only to
                                          						the dial peer created for the secondary number for this ephone-dn. |
| dialplan-pattern | (Optional) Call forwarding is selectively applied only to
                                          						dial peers created for this ephone-dn by the dial-plan pattern. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.1(5)YD | Cisco ITS 1.0 | This command was introduced. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release
                                          						12.2(8)T. |
| 12.4(4)XC | Cisco Unified CME 4.0 | The primary , secondary , and dialplan-pattern keywords were
                                          						added, and this command was made available in ephone-dn-template configuration
                                          						mode. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command with modifications was integrated into Cisco
                                          						IOS Release 12.4(9)T. |

| Command | Description |
|---|---|
| call forward all | Configures call forwarding for all incoming calls for an
                                          						ephone-dn. |
| call forward busy | Configures call forwarding to another number when an
                                          						ephone-dn is busy. |
| call-forward night-service | Configures call forwarding for all incoming calls to an
                                          						ephone-dn during the hours defined for night service. |
| ephone-dn-template (ephone-dn) | Applies an ephone-dn-template to an ephone-dn. |

| pattern | String that consists of one or more digits and wildcard
                                          						markers or dots (.) to define a specific pattern. Calling parties that match a
                                          						defined pattern use the H.450.3 standard if they are forwarded. A pattern of .T
                                          						specifies the H.450.3 forwarding standard for all incoming calls. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(11)YT | Cisco CME 2.1 | This command was introduced. |
| 12.2(15)T | Cisco CME 2.1 | This command was integrated into Cisco IOS Release
                                          						12.2(15)T. |

| Command | Description |
|---|---|
| call application voice | Defines an application, indicates the location of the
                                          						corresponding Tcl files that implement the application, and loads the selected
                                          						Tcl script. |

| secondary | (Optional) Uses the secondary number associated with the
                                          						forwarding party instead of the primary number. The primary number is the
                                          						default if this keyword is not used. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ3 | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |
| 12.3(15)ZJ4 | Cisco CME 3.0 | The secondary keyword was introduced. |
| 12.3(14)T | Cisco CME 3.3 | Support was added to the default IOS voice application
                                          						framework and dependency on the TCL script was removed. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| Cisco
                                          						IOS XE Everest 16.6.1 | Unified
                                          						CME 12.0 | This
                                          						command was introduced. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 15.6(3)M 16.3.1 | Cisco
                                          						Unified CME 11.5 | This
                                          						command was introduced. |

| application | Enables Call Park and Directed Call Park for SCCP and SIP
                                          						phones. |
|---|---|
| redirect | H.323 and SIP calls use H.450 or the SIP Refer method of
                                          						call forwarding or transfer to park calls and to pick up calls from park. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |
| 12.4(22)YB | Cisco Unified CME 7.1 | The application keyword and support for
                                          						SIP phones was added. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command has been integrated into Cisco IOS Release
                                          						12.4(24)T. |

| Command | Description |
|---|---|
| park reservation-group | Assigns a call-park reservation group to a phone. |
| park-slot | Creates a floating extension at which calls can be
                                          						temporarily parked. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

| Command | Description |
|---|---|
| voice register pool | Enters voice register pool configuration mode for SIP
                                          						phones. |

| accept | (Optional) Allows call-waiting beeps to be accepted by an
                                          						ephone-dn. |
|---|---|
| generate | (Optional) Allows call-waiting beeps to be generated by an
                                          						ephone-dn. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(11)T | Cisco CME 3.2 | This command was introduced. |
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was made available in ephone-dn-template
                                          						configuration mode. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command in ephone-dn-template configuration mode was
                                          						integrated into Cisco IOS Release 12.4(9)T. |

| Command | Description |
|---|---|
| show running-config | Displays the contents of the currently running
                                          						configuration file or the configuration for a specific interface, or map class
                                          						information. |
| ephone-dn-template (ephone-dn) | Applies a template to an ephone-dn. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.3(11)XL | Cisco CME 3.2.1 | This command was introduced. |
| 12.3(14)T | Cisco CME 3.3 | This command was integrated into Cisco IOS Release
                                          						12.3(14)T. |
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was made available in ephone-dn-template
                                          						configuration mode. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command in ephone-dn-template configuration mode was
                                          						integrated into Cisco IOS Release 12.4(9)T. |

| Note | The call-waiting ring option cannot be used on the Cisco Unified
                                       		  IP Phone 7902, Cisco Unified IP Phone 7905, or Cisco Unified IP Phone 7912. Do
                                       		  not use the call-waiting ring command for ephone-dns associated with these
                                       		  types of phones. |
|---|---|

| Command | Description |
|---|---|
| call-waiting beep | Allows call-waiting beeps to be accepted by or generated
                                          						from an ephone-dn. |
| ephone-dn-template (ephone-dn) | Applies template to ephone-dn. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(4)M | Cisco Unified CME 8.6 | This command was introduced. |

| Command | Description |
|---|---|
| apply-config | Allows to dynamically apply the phone configuration on
                                          						Cisco Unified SIP IP phones 8961, 9951, and 9971, |

| digit-string | String of digits that a phone user enters at the phone for
                                          						CAPF authentication. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| Command | Description |
|---|---|
| auth-mode | Specifies the type of authentication to use during CAPF
                                          						sessions. |
| auth-string | Generates or removes authentication strings for one or all
                                          						secure ephones. |
| show capf-server | Displays configuration and session information for the CAPF
                                          						server. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| ca-label | PKI trustpoint label for the CA or for the RA if an RA is
                                          						being used. |
|---|---|
| password | Values that follow apply to the password. |
| 0 \| 1 | Encryption status of the password string that follows. 0 —Encrypted. 1 —Clear text. Note This option refers to the way that you want the password
                                                   						to appear in show command output and not to the way that you enter the password
                                                   						in this command. | Note | This option refers to the way that you want the password
                                                   						to appear in show command output and not to the way that you enter the password
                                                   						in this command. |
| Note | This option refers to the way that you want the password
                                                   						to appear in show command output and not to the way that you enter the password
                                                   						in this command. |
| password-string | Alphanumeric challenge password that is required for
                                          						certificate enrollment. |

| Note | This option refers to the way that you want the password
                                                   						to appear in show command output and not to the way that you enter the password
                                                   						in this command. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| session_id | Unique numeric identifier for the session. String length is
                                          						1 to 10 characters. String value is 1 to 2147483647. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| show cti session | Displays active CTI sessions. |

| number | Conference telephone or extension number. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XJ2 | Cisco Unified CME 4.1 | This command was introduced. |
| 12.4(15)T | Cisco Unified CME 4.1 | This command was integrated into Cisco IOS Release
                                          						12.4(15)T. |

| Command | Description |
|---|---|
| show telephony-service conference hardware | Displays information about hardware conferences in a Cisco
                                          						CME system. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| Command | Description |
|---|---|
| auto-reg-ephone | Enables automatic registration of ephones with Cisco
                                          						Unified CME. |
| show ephone attempted-registrations | Displays the log of ephones that unsuccessfully attempt to
                                          						register with Cisco CME. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| Command | Description |
|---|---|
| show fb-its-log | Displays Cisco Unified CME XML API information. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(3)T | Cisco Unified CME 8.5 | This command was introduced. |

| Command | Description |
|---|---|
| show voice fac statistics | Displays details of phones that attempted to register and
                                          						failed. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| show voice lpcor statistics | Displays information about LPCOR policies and calls. |
| voice lpcor policy | Creates a LPCOR policy for a resource group. |

| Cisco IOS Release | yCisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 Cisco Unified SRST 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 Cisco Unified SRST 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| show voice moh-group statistics | Displays the MOH subsystem statistics information |
| show voice moh-group | Displays the MOH groups configured |

| ip ip-address | (Optional) IP address of the SIP phone attempting to
                                          						register. |
|---|---|
| mac H.H.H | (Optional) MAC address of the SIP phone attempting to
                                          						register. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(2)T | Cisco Unified CME 8.1 | This command was introduced. |

| Command | Description |
|---|---|
| attempted-registrations size | Allows to set the size of the attempted-registrations
                                          						table. |
| show voice register attempted-registration | Displays details of phones that attempted to register and
                                          						failed. |

| perphonetype | A separate configuration file is generated for each type of
                                          						phone. |
|---|---|
| perphone | A separate configuration file is generated for each phone. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| Command | Description |
|---|---|
| cnf-file location | Specifies a storage location for XML configuration files. |
| create cnf | Generates the XML configuration files used for provisioning
                                       					 SCCP phones. |

| flash: | Router flash memory. |
|---|---|
| slot0: | Router slot 0 memory. |
| tftp tftp-url | External TFTP server at the specified URL. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| Note | When the storage location chosen is flash and the file system type
                                       		  on this device is Class B(LEFS), make sure to check free space on the device
                                       		  periodically and use the squeeze command to free the space used up by
                                       		  deleted files. Unless you use the squeeze command, the space used by the moved
                                       		  or deleted configuration files cannot be used by other files. |
|---|---|

| Command | Description |
|---|---|
| cnf-file | Specifies the use of different phone configuration files by
                                          						type of phone or by individual phone. |
| create cnf | Generates the XML configuration files used for provisioning
                                          						SCCP phones. |

| g711ulaw | Preferred codec: G.711 micro-law 64K bps. |
|---|---|
| g722r64 | Preferred codec: G.722-64K bps. |
| g729r8 | Preferred codec: G.729-8K bps. |
| dspfarm-assist | (Optional) DSP-farm resources are used for transcoding the
                                          						segment between the phone and the Cisco Unified CME router if G.711 is
                                          						negotiated for the call. Note The dspfarm-assist keyword is ignored
                                                   						if the SCCP endpoint type is ATA, VG224, or VG248. | Note | The dspfarm-assist keyword is ignored
                                                   						if the SCCP endpoint type is ATA, VG224, or VG248. |
| Note | The dspfarm-assist keyword is ignored
                                                   						if the SCCP endpoint type is ATA, VG224, or VG248. |
| ilbc | Preferred codec: iLBC 20ms. |

| Note | The dspfarm-assist keyword is ignored
                                                   						if the SCCP endpoint type is ATA, VG224, or VG248. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | The g722r64 and ilbc keywords were added. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Note | The dspfarm-assist keyword is ignored if the SCCP
                                       		  endpoint type is ATA, VG224, or VG248. |
|---|---|

| Command | Description |
|---|---|
| dspfarm (dspfarm) | Enables digital-signal-processor (DSP) farm service |
| dsp services dspfarm | Specifies the NM-HDV or NM-HDV-FARM on which DSP-farm
                                          						services are to be enabled. |
| dspfarm transcoder maximum sessions | Specifies the maximum number of transcoding sessions to be
                                          						supported by a DSP farm. |
| show dspfarm | Displays summary information about DSP resources. |

| g711-ulaw | Preferred codec: G.711 micro-law. |
|---|---|
| g722-64k | Preferred codec: G.722 64K bps. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(15)XZ | Cisco Unified CME 4.3 | This command was introduced. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| service phone | Modifies VendorConfig parameters in configuration files for
                                          						IP phones. |

| ad-hoc | Configures ad hoc conferences. |
|---|---|
| video | (Optional) Configures video conferences. |
| meetme | Configures meet-me conferences. |
| homogenous | (Optional) Enables a homogeneous video conference in which all participants use
                                          						the same video format. Note The
                                                   						video keyword must be specified in the command. | Note | The
                                                   						video keyword must be specified in the command. |
| Note | The
                                                   						video keyword must be specified in the command. |
| unlocked | Unlocks
                                          						the meet-me conference bridge. |

| Note | The
                                                   						video keyword must be specified in the command. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.4(11)XJ2 | Cisco
                                          						Unified CME 4.1 | This
                                          						command was introduced. |
| 12.4(15)T | Cisco
                                          						Unified CME 4.1 | This
                                          						command was integrated into Cisco IOS Release 12.4(15)T |
| 15.0(1)XA | Cisco
                                          						Unified CME 8.0 | This
                                          						command was modified. The command output was enhanced to display the unlocked
                                          						meet-me conference setting. |
| 15.1(1)T | Cisco
                                          						Unified CME 8.0 | This
                                          						command was integrated into Cisco IOS Release 15.1(1)T. |
| 15.1(4)M | Cisco
                                          						Unified CME 8.6 | This
                                          						command was modified to configure video conferences. |
| Cisco
                                          						IOS XE Everest 16.5.1b | Unified CME 11.7 | This
                                          						command was integrated into Cisco IOS XE Everest 16.5.1 Release to support
                                          						Cisco 4000 Series Integrated Services Router. |

| Note | To configure
                                       		  an unlocked meet-me conference, all ephone-dn tags associated with the same
                                       		  number should have the unlocked option configured. If some of the ephone-dn
                                       		  tags do not have the unlocked option configured, the unlocked meet-me
                                       		  conference may not work properly. |
|---|---|

| Command | Description |
|---|---|
| show ephone-dn | Displays phone information for specified dn-tag or for all dn-tags. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

| Command | Description |
|---|---|
| template (voice register pool) | Applies a template to a SIP phone. |
| transfer-attended (voice register template) | Enables a soft key for attended transfer in a SIP phone
                                          						template. |
| transfer-blind (voice register template) | Enables a soft key for blind transfer in a SIP phone
                                          						template. |
| voice register pool | Enters voice register pool configuration mode for SIP
                                          						phones. |

| creator | Specifies that only the creator can add parties. |
|---|---|

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.4(11)XJ2 | Cisco
                                          						Unified CME 4.1 | This
                                          						command was introduced. |
| 12.4(15)T | Cisco
                                          						Unified CME 4.1 | This
                                          						command was integrated into Cisco IOS Release 12.4(15)T. |
| Cisco
                                          						IOS XE Everest 16.5.1b | Unified CME 11.7 | Support for this command was introduced on the Cisco 4000 Series
                                          						Integrated Services Routers. |

| Command | Description |
|---|---|
| ephone-template (ephone) | Applies
                                          						an ephone template to an ephone. |
| show telephony-service ephone | Displays configuration for the Cisco IP phones. |
| show telephony-service ephone-template | Displays the contents of ephone-templates. |

| creator | (Optional) Specifies that only the conference creator can add participants to
                                          						an ad-hoc hardware conference. |
|---|---|

| Release | Modification |
|---|---|
| 15.2(2)T | This
                                          						command was introduced. |
| Cisco
                                          						IOS XE Everest 16.5.1b | Support
                                          						for this command was introduced on the Cisco 4000 Series Integrated Services
                                          						Routers. |

| Command | Description |
|---|---|
| voice register pool | Enters
                                          						voice register pool configuration mode and creates a pool configuration for
                                          						Cisco Unified SIP IP phones in Cisco Unified CME. |
| voice register template | Enters
                                          						voice register template configuration mode and defines a template of common
                                          						parameters for Cisco Unified SIP IP phones. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XJ2 | Cisco Unified CME 4.1 | This command was introduced. |
| 12.4(15)T | Cisco Unified CME 4.1 | This command was integrated into Cisco IOS Release
                                          						12.4(15)T |

| Command | Description |
|---|---|
| ephone-template (ephone) | Applies an ephone template to an ephone. |
| show telephony-service ephone | Displays configuration for the Cisco IP phones. |
| show telephony-service ephone-template | Displays the contents of ephone-templates. |

| Release | Modification |
|---|---|
| 15.2(2)T | This command was introduced. |

| Command | Description |
|---|---|
| voice register pool | Enters voice register pool configuration mode and creates a
                                          						pool configuration for Cisco Unified SIP IP phones in Cisco Unified CME. |
| voice register template | Enters voice register template configuration mode and
                                          						defines a template of common parameters for Cisco Unified SIP IP phones. |

| creator | Specifies that the active conference terminates when the creator hangs up. |
|---|---|
| local | Specifies that the active conference terminates when the last local party in
                                          						the conference hangs up or drops out of the conference. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.4(11)XJ2 | Cisco
                                          						Unified CME 4.1 | This
                                          						command was introduced. |
| 12.4(15)T | Cisco
                                          						Unified CME 4.1 | This
                                          						command was integrated into Cisco IOS Release 12.4(15)T |
| Cisco
                                          						IOS XE Everest 16.5.1b | Unified CME 11.7 | Support for this command was introduced on the Cisco 4000 Series
                                          						Integrated Services Routers. |

| Command | Description |
|---|---|
| ephone-template (ephone) | Applies
                                          						an ephone template to an ephone. |
| show telephony-service ephone | Displays configuration for the Cisco IP phones. |
| show telephony-service ephone-template | Displays the contents of ephone-templates. |

| creator | Terminates the active conference when the conference creator hangs up. |
|---|---|
| local | Terminates the active conference when the last local participant hangs up or
                                          						drops out of the conference. |

| Release | Modification |
|---|---|
| 15.2(2)T | This
                                          						command was introduced. |
| Cisco
                                          						IOS XE Everest 16.5.1b | Support
                                          						for this command was introduced on the Cisco 4000 Series Integrated Services
                                          						Routers. |

| Command | Description |
|---|---|
| voice register pool | Enters
                                          						voice register pool configuration mode and creates a pool configuration for
                                          						Cisco Unified SIP IP phones in Cisco Unified CME. |
| voice register template | Enters
                                          						voice register template configuration mode and defines a template of common
                                          						parameters for Cisco Unified SIP IP phones. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.4(11)XJ2 | Cisco
                                          						Unified CME 4.1 | This
                                          						command was introduced. |
| 12.4(15)T | Cisco
                                          						Unified CME 4.1 | This
                                          						command was integrated into Cisco IOS Release 12.4(15)T. |
| Cisco
                                          						IOS XE Everest 16.5.1b | Unified CME 11.7 | This
                                          						command was integrated into Cisco IOS XE Everest 16.5.1 Release to support
                                          						Cisco 4000 Series Integrated Services Router. |

| Command | Description |
|---|---|
| conference-join custom-cptone | Associates a custom call-progress tone to indicate joining a conference with a
                                          						DSP farm profile. |
| conference-leave custom-cptone | Associates a custom call-progress tone to indicate leaving a conference with a
                                          						DSP farm profile. |
| maximum conference-participants | Configures the maximum number of conference participants allowed in each
                                          						conference. |
| show dspfarm profile | Displays configured DSP farm profile information. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 15.2(2)T | Cisco
                                          						Unified CME 9.0 | This
                                          						command was introduced. |
| Cisco
                                          						IOS XE Everest 16.5.1b | Unified CME 11.7 | This
                                          						command was integrated into Cisco IOS XE Everest 16.5.1 Release yto support
                                          						Cisco 4000 Series Integrated Services Router. |

| Command | Description |
|---|---|
| conference hardware | Configures a Cisco Unified CME system for hardware conferencing only in
                                          						telephony-service configuration mode. |

| value | Maximum
                                       					 number of digits that can be dialed. The range is from 3 to 16. |
|---|---|

| Cisco
                                    				  IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.4(3)M | Cisco Unified CME 10.5 | This
                                       					 command was introduced. |

| Command | Description |
|---|---|
| conference-pattern blocked | Blocks
                                          						extensions on an ephone or a voice register pool from making conference calls. |
| conference
                                                							 transfer-pattern | Apply
                                          						transfer -pattern configuration for conference cases. |
| transfer max-length | Allows
                                          						transfer of calls to phones, where the number of dialed digits are less than
                                          						the maximum length configured. |
| transfer-pattern
                                                							 (telephony-service) | Allows
                                          						the transfer of calls to phones outside the Cisco Unified CME network. |

| Cisco
                                    				  IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.4(3)M | Cisco Unified CME 10.5 | This
                                       					 command was introduced. |

| Command | Description |
|---|---|
| conference max-length | Allows
                                          						conferences to numbers where dialed digits are within the configured maximum
                                          						length value. |
| conference
                                                							 transfer-pattern | Apply
                                          						transfer-pattern configuration for conference cases. |
| transfer-pattern blocked | Blocks
                                          						individual phones from transferring calls to nonlocal numbers that have been
                                          						globally enabled for transfer. |
| transfer-pattern
                                                							 (telephony-service) | Allows
                                          						the transfer of calls to phones outside the Cisco Unified CME network. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.2(4)M | Cisco Unified CME 9.1 | This command was introduced. |

| Command | Description |
|---|---|
| telephony-service | Enters telephony-service configuration mode. |

| incoming | COR
                                          						list to be used by incoming dial peers. |
|---|---|
| outgoing | COR
                                          						list to be used by outgoing dial peers. |
| cor-list-name | COR
                                          						list name. |
| cor-list-number | COR
                                          						list identifier. |
| starting-number | Start
                                          						of a directory number range, if an ending number is included. Can also be a
                                          						standalone number. |
| - | (Optional) Indicator that a full range is configured. |
| ending-number | (Optional) End of a directory number range. |
| default | Instructs the COR list to assume behavior according to a predefined default COR
                                          						list. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco
                                          						SIP SRST 3.0 | This
                                          						command was introduced. |
| 12.3(4)T | Cisco
                                          						SIP SRST 3.0 | This
                                          						command was integrated into Cisco IOS Release 12.3(4)T. |
| 12.4(4)T | Cisco
                                          						CME 3.4 Cisco SIP SRST 3.4 | This
                                          						command was added to Cisco CallManager Express (Cisco CME). |
| Cisco
                                          						IOS XE Fuji 16.7.1 | Unified CME 12.1 | This
                                          						command was supported in voice register template configuration mode. |

| Note | Configure
                                       		  the id (voice register pool) command before any other voice register
                                       		  pool commands, including the cor command. The id command
                                       		  identifies a locally available individual Cisco SIP IP phone or set of Cisco
                                       		  SIP IP phones. |
|---|---|

| Command | Description |
|---|---|
| dial-peer cor custom | Specifies that named CORs apply to dial peers. |
| dial-peer cor list | Defines a COR list name. |
| id (voice register pool) | Explicitly identifies a locally available individual Cisco SIP IP phone, or
                                          						when running Cisco Unified SIP SRST, set of Cisco SIP IP phones. |
| member (dial-peer cor list) | Adds
                                          						a member to a dial-peer COR list. |
| name (dial-peer custom cor) | Provides a name for a custom COR. |
| show dial-peer voice | Displays information for voice dial peers. |

| incoming | Specifies a COR list to be used by incoming dial peers. |
|---|---|
| outgoing | Specifies a COR list to be used by outgoing dial peers. |
| corlist - name | COR list name. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(2)XT | Cisco ITS 2.0 | This command was introduced on the Cisco 1750, Cisco 1751,
                                          						Cisco 2600 series, Cisco 3600 series, and Cisco IAD2420 series. |
| 12.2(8)T | Cisco ITS 2.0 | This command was integrated into Cisco IOS Release 12.2(8)T
                                          						and implemented on the Cisco 3725 and Cisco 3745. |
| 12.2(8)T1 | Cisco ITS 2.0 | This command was implemented on the Cisco 2600-XM and Cisco
                                          						2691. |
| 12.2(11)T | Cisco ITS 2.01 | This command was implemented on the Cisco 1760. |

| Command | Description |
|---|---|
| corlist incoming | Specifies the COR list to be used when a specified dial
                                          						peer acts as the incoming dial peer. |
| corlist outgoing | Specifies the COR list to be used by an outgoing dial peer. |
| dial - peer cor list | Defines a COR list name. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(11)YT | Cisco ITS 2.1 | This command was introduced. |
| 12.2(15)T | Cisco ITS 2.1 | This command was integrated into Cisco IOS Release
                                          						12.2(15)T. |
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was modified to interact with the cnf-file command and the cnf-file location command. |
| 12.4(9)T | Cisco Unified CME 4.0 | Modifications to this command for interacting with the cnf-file command and the cnf-file location command were integrated into
                                          						Cisco IOS Release 12.4(9)T. |

| Command | Description |
|---|---|
| cnf-file | Specifies the type of configuration file to be created. |
| cnf-file location | Specifies a storage location for phone configuration files |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |

| Command | Description |
|---|---|
| cnf-file location | Specifies a storage location for phone configuration files. |
| reset (voice-gateway) | Performs a complete reboot of all analog phones associated
                                          						with the voice gateway and registered to Cisco Unified CME. |
| restart (voice-gateway) | Performs a fast restart of all analog phones associated
                                          						with the voice gateway and registered to Cisco Unified CME. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

| Command | Description |
|---|---|
| file text (voice register global) | Generates ASCII text files for SIP phones. |
| mode (voice register global) | Enables the mode for provisioning SIP phones in a Cisco
                                          						CallManager Express (Cisco CME) system. |
| reset (voice register global) | Performs a complete reboot of all SIP phones associated
                                          						with a Cisco CME router. |
| source-address (voice register global) | Identifies the IP address and port through which SIP phones
                                          						communicate with a Cisco CME router. |
| tftp-path (voice register global) | Specifies the directory to which the provisioning file for
                                          						SIP phones in a Cisco CallManager Express (Cisco CME) system will be written. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.3(14)T | Cisco
                                          						SRST 3.3 | This
                                          						command was introduced for Cisco SRST. |
| 12.4(4)XC | Cisco
                                          						Unified CME 4.0 | This
                                          						command was introduced for Cisco Unified CME. |
| 12.4(9)T | Cisco
                                          						Unified CME 4.0 | This
                                          						command for Cisco Unified CME was integrated into Cisco IOS Release 12.4(9)T. |
| Cisco IOS XE Fuji 16.7.1 Release | Unified SRST 12.1 | This command was introduced for Unified SRST support on
                                          						Cisco 4000 Series Integrated Services Router. |

| Caution | For security
                                          			 reasons, credentials service should be deactivated on all SRST routers after
                                          			 provisioning to Cisco Unified CallManager is completed. |
|---|---|

| Command | Description |
|---|---|
| ctl-service admin | Specifies a user name and password to authenticate the CTL client during the
                                          						CTL protocol. |
| debug credentials | Sets
                                          						debugging on the credentials service that runs between a Cisco Unified CME CTL
                                          						provider the CTL client or between an SRST router and Cisco Unified
                                          						CallManager. |
| ip source-address (credentials) | Enables the Cisco Unified CME or SRST router to receive messages through the
                                          						specified IP address and port. |
| show credentials | Displays the credentials settings on a Cisco Unified CME or SRST router. |
| trustpoint (credentials) | Specifies the name of the trustpoint to be associated with a Cisco Unified CME
                                          						CTL provider certificate or with an SRST router certificate. |

| Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1.(1)T. |
| Cisco IOS XE Gibraltar 16.11.1a Release | Unified CME 12.6 | This command was deprecated. It is not supportd on Unified CME 12.6 and later releases. |

| Command | Description |
|---|---|
| cti shutdown | Disables CTI integration. |

| Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |
| Cisco IOS XE Gibraltar 16.11.1a Release | Unified CME 12.6 | This command was deprecated. It is not supportd on Unified CME 12.6 and later releases. |

| Command | Description |
|---|---|
| cti shutdown | Disables CTI integration. |

| Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |
| Cisco IOS XE Gibraltar 16.11.1a Release | Unified CME 12.6 | This command was deprecated. It is not supportd on Unified CME 12.6 and later releases. |

| Command | Description |
|---|---|
| ephone-dn-template (ephone-dn) | Applies an ephone-dn template to an ephone-dn. |

| Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |
| Cisco IOS XE Gibraltar 16.11.1a Release | Unified CME 12.6 | This command was deprecated. It is not supportd on Unified CME 12.6 and later releases. |

| Command | Description |
|---|---|
| ephone-dn-template (ephone-dn) | Applies an ephone-dn template to an ephone-dn |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |
| Cisco IOS XE Gibraltar 16.11.1a Release | Unified CME 12.6 | This command was deprecated. It is not supportd on Unified CME 12.6 and later releases. |

| Command | Description |
|---|---|
| keepalive (voice register session-server) | Duration for registration after which the registration
                                          						expires unless the feature server or application reregisters before the
                                          						registration expiry. |
| register-id | Creats an ID for explicitly identifying an external feature
                                          						server or application during Register requests |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| username | Defines the name that will be used to authenticate the
                                          						client. |
|---|---|
| secret { 0 \| 1 } | Defines a character string for login authentication and
                                          						whether it will be encrypted when it is stored in the running configuration. 0 —Not encrypted. 1 —Encrypted using Message
                                             						  Digest 5 (MD5). |
| password-string | Character string for login authentication |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| Command | Description |
|---|---|
| debug credentials | Sets debugging on the credentials service that runs between a
                                       					 Cisco Unified CME CTL provider and the CTL client or between an SRST router and
                                       					 Cisco Unified CallManager. |
| show credentials | Displays the credentials settings on a Cisco Unified CME or
                                       					 SRST router. |
| trustpoint (credentials) | Specifies the name of the trustpoint to be associated with a
                                       					 Cisco Unified CME CTL provider certificate or with an SRST router certificate. |