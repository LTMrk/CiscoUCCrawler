---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmetemps-html-491eb135bb
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmetemps.html
retrieved_at: 2026-08-21T07:25:15.918526+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Templates

## Chapter: Templates

# Templates

## Information About Templates

### Phone
                           	 Templates

An ephone or
                              		voice-register template is a set of features that can be applied to one or more
                              		individual phones using a single command.

Ephone templates
                              		were introduced in Cisco CME 3.2 to manipulate softkey display and order on IP
                              		phones.

In Cisco Unified CME
                              		4.0, ephone templates were significantly enhanced to include a number of
                              		additional phone features. Templates allow you to uniformly and easily
                              		implement the features you select for a set of phones. A maximum of 20 ephone
                              		templates can be created in a Cisco Unified CME system, although an ephone can
                              		have only one template applied to it at a time.

In Cisco Unified CME
                              		4.3 and later versions, an ephone template cannot be applied to a particular
                              		phone unless its configuration file includes its Mac address. If you attempt to
                              		apply a template to a phone for which the MAC address in not configured, a
                              		message appears.

If you use an ephone
                              		template to apply a command to a phone and you also use the same command in
                              		ephone configuration mode for the same phone, the value set in ephone
                              		configuration mode has priority.

Voice-register
                              		templates were introduced in Cisco CME 3.4 to enable sets of features to be
                              		applied to individual SIP Phones that are connected directly in
                              		Cisco Unified CME. Typically, features to be enabled by using a voice-register
                              		template are not configurable in other configuration modes. A maximum 10
                              		voice-register templates can be defined in Cisco Unified CME, although a phone
                              		can have only one template applied to it at a time.

Type ? in ephone-template or voice-register-template configuration mode to display a
                              		list of features that can be implemented by using templates.

For configuration
                              		information, see Create an Ephone Template .

### Ephone-dn
                           	 Templates

Ephone-dn templates
                              		allow you to apply a standard set of features to ephone-dns. A maximum of 15
                              		ephone-dn templates can be created in a Cisco Unified CME system, although an
                              		ephone-dn can have only one template applied to it at a time.

If you use an
                              		ephone-dn template to apply a command to an ephone-dn and you also use the same
                              		command in ephone-dn configuration mode for the same ephone-dn, the value that
                              		you set in ephone-dn configuration mode has priority.

Type ? in ephone-dn-template configuration mode to display a list of features that can
                              		be implemented by using templates.

For configuration
                              		information, see Create an Ephone-dn Template .

## Configure Templates

### Create an Ephone
                           	 Template

To create an
                                 		  ephone template and apply it to a phone, perform the following steps.

#### Before you begin

In
                                          				Cisco Unified CME 4.3 and later versions, the configuration file for a
                                          				particular phone must contain its MAC address before an ephone template can be
                                          				applied to that phone. To explicitly configure a MAC address, use the mac-address command in ephone configuration mode. For configuration information, see Configuring Phones to Make Basic Calls .

It is
                                          				recommended to configure cnf-file per phone before adding ephone-template under
                                          				ephone.

### SUMMARY STEPS

- enable

- configure terminal

- ephone-template template-tag

- command

- exit

- ephone phone-tag

- ephone-template template-tag

- restart

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router# enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ephone-template template-tag

#### Example:

```
Router(config)# ephone-template 15
```

Enters
                                             				ephone-template configuration mode to create an ephone template.

template-tag —Unique identifier for the ephone template that is being created. Range is 1 to 20.

Step 4

command

#### Example:

```
Router(config-ephone-template)# features blocked Park Trnsfer
```

Applies the
                                             				specified command to the ephone template that is being created.

Type ? for a list
                                                      					 of commands that can be used in this step.

Repeat this
                                             				step for each command that you want to add to the ephone template.

Step 5

exit

#### Example:

```
Router(config-ephone-template)# exit
```

Exits
                                             				ephone-template configuration mode.

Step 6

ephone phone-tag

#### Example:

```
Router(config)# ephone 36
```

Enters ephone
                                             				configuration mode.

phone-tag —Unique sequence number that identifies
                                                      					 this ephone during configuration tasks.

Step 7

ephone-template template-tag

#### Example:

```
Router(config-ephone)# ephone-template 15
```

Applies an
                                             				ephone template to the ephone that is being configured.

Step 8

restart

#### Example:

```
Router(config-ephone)# restart
```

Performs a
                                             				fast reboot of this ephone. Does not contact the DHCP or TFTP server for
                                             				updated information.

Restart all
                                                         				  ephones using the restart all command in telephony-service configuration mode.

Step 9

end

#### Example:

```
Router(config-ephone)# end
```

Returns to
                                             				privileged EXEC mode.

### Create an
                           	 Ephone-dn Template

To create an
                                 		  ephone-dn template and apply it to an ephone-dn, perform the following steps:

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn-template template-tag

- command

- exit

- ephone-dn dn-tag

- ephone-dn-template template-tag

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router# enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ephone-dn-template template-tag

#### Example:

```
Router(config)# ephone-dn-template 3
```

Enters
                                             				ephone-dn-template configuration mode to create an ephone-dn template.

template-tag —Unique identifier for the ephone-dn
                                                      					 template that is being created. Range is 1 to 20.

Step 4

command

#### Example:

```
Router(config-ephone-dn-template)# call-forwarding busy 4000
```

Applies the
                                             				specified command to the ephone-dn template that is being created.

Type ? for a list
                                                      					 of commands that can be used in this step.

Repeat this
                                             				step to add more commands to the template.

Step 5

exit

#### Example:

```
Router(config-ephone-dn-template)# exit
```

Exits
                                             				ephone-dn-template configuration mode.

Step 6

ephone-dn dn-tag

#### Example:

```
Router(config)# ephone-dn 23
```

Enters
                                             				ephone-dn configuration mode.

dn-tag —Unique sequence number that identifies this
                                                      					 ephone-dn during configuration tasks.

Step 7

ephone-dn-template template-tag

#### Example:

```
Router(config-ephone-dn)# ephone-dn-template 3
```

Applies an
                                             				ephone-dn template to the ephone-dn that is being configured.

Step 8

end

#### Example:

```
Router(config-ephone-dn)# end
```

Returns to
                                             				privileged EXEC mode.

### Verify Templates
                           	 on SCCP Phones

To view the
                                 		  configuration of a template, and verify to which phone or directory number a
                                 		  template is applied, perform the following steps.

Step 1

show telephony-service ephone

Use is command
                                             				to display information about SCCP phones in Cisco Unified CME, including which
                                             				template-tags are enabled in the configuration for a phone.

```
Router# show telephony-service ephone 1 ephone-dn-template  1
 description Call Center Line 1
 call-forward busy 500
 call-forward noan 500 timeout 10
 pickup-group 33!
!
```

Step 2

show telephony-service ephone-template

Use is command
                                             				to display information about an ephone template in Cisco Unified CME, including
                                             				a list of features enabled in the configuration.

Step 3

show telephony-service ephone-dn

Use is command
                                             				to display information about directory numbers, including which template-tags
                                             				are enabled in the configuration for a directory number.

```
Router# show telephony-service ephone-dn 4 !
ephone-dn  4  dual-line
 number 136
 description Desk4
 ephone-dn template 1
 ephone-hunt login
```

Step 4

show telephony-service ephone-dn-template

Use is command
                                             				to display information about an ephone-dn template in Cisco Unified CME,
                                             				including a list of features enabled in the configuration.

### Create and Apply
                           	 Templates for SIP Phones

To create
                                 		  templates of common features and softkeys that can be applied to individual
                                 		  Cisco SIP Phones, follow the steps in this section.

#### Before you begin

Cisco CME 3.4
                                          				or a later version.

The mode cme
                                          				command must be enabled in Cisco Unified CME.

### SUMMARY STEPS

- enable

- configure terminal

- voice register template template-tag

- command

- exit

- voice register pool pool-tag

- template template-tag

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router# enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice register template template-tag

#### Example:

```
Router(config)# voice register template 1
```

Enters voice
                                             				register template configuration mode to define a template of common parameters
                                             				for SIP phones in Cisco Unified CME.

Range is 1
                                                      					 to 5.

Step 4

command

#### Example:

```
Router(config-register-template)# anonymous block
```

Applies the
                                             				specified command to this template and enables the corresponding feature on any
                                             				supported SIP phone that uses a template in which this command is configure.

Type ? to display
                                                      					 list of commands that can be used in a voice register template.

Repeat this
                                             				step for each feature to be added to this voice register template.

Step 5

exit

#### Example:

```
Router(config-register-template)# exit
```

Exits
                                             				configuration mode to the next highest mode in the configuration mode
                                             				hierarchy.

Step 6

voice register pool pool-tag

#### Example:

```
Router(config)# voice register pool 3
```

Enters voice
                                             				register pool configuration mode to set phone-specific parameters for SIP
                                             				phones.

pool-tag —Unique sequence number of the Cisco  SIP
                                                      					 phone to be configured. Range is 1 to 100 or the upper limit as defined by max-pool command.

Step 7

template template-tag

#### Example:

```
Router(config-register-pool)# voice register pool 1
```

Applies a
                                             				template created with the voice register
                                                   					 template command.

template-tag —Unique sequence number of the
                                                      					 template to be applied to the SIP phone specified by the voice register
                                                            						  pool command. Range is 1 to 5.

Step 8

end

#### Example:

```
Router(config-register-pool)# end
```

Returns to
                                             				privileged EXEC mode.

#### Examples

The following
                                 		  example shows templates 1 and 2 and how to do the following:

Apply
                                          				template 1 to SIP phones 1 to 3.

Apply
                                          				template 2 to SIP phone 4.

Remove a
                                          				previously created template 5 from SIP phone 5.

```
Router(config)# voice register template 1 Router(config-register-temp)# anonymous block Router(config-register-temp)# caller-id block Router(config-register-temp)# voicemail 5001 timeout 15 Router(config)# voice register template 2 Router(config-register-temp)# anonymous block Router(config-register-temp)# caller-id block Router(config-register-temp)# no conference Router(config-register-temp)# no transfer-attended Router(config-register-temp)# voicemail 5005 timeout 15 Router(config)# voice register pool 1 Router(config-register-pool)# template 1 Router(config)# voice register pool 2 Router(config-register-pool)# template 1 Router(config)# voice register pool 3 Router(config-register-pool)# template 1 Router(config)# voice register pool 4 Router(config-register-pool)# template 2 Router(config)# voice register pool 5 Router(config-register-pool)# no template 5
```

## Configuration Examples for Creating Templates

### Example to Block The Use of Park and Transfer Soft Keys Using Ephone
                           	 Template

The following example creates an ephone template to block the use of
                                 		  Park and Transfer soft keys. It is applied to ephone 36 and extension 2333.

```
ephone-template 15
		 features blocked Park Trnsfer
		
		ephone-dn 2
		 number 2333
		
		ephone 36
		 button 1:2
		 ephone-template 15
```

### Example to Set Call Forwarding Using Ephone-dn Template

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

## Where to Go
                        	 Next

### Softkey
                              		  Display

The display of
                              		  soft keys during different call states is managed using ephone templates. For
                              		  more information, see Customize Softkeys .

## Feature
                        	 Information for Creating Templates

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Cisco Unified CME Version

Feature Information

Ephone Templates

4.0

The number of ephone templates that can be created was
                                                   						  increased from 5 to 20.

More commands can be included in ephone templates.

3.2

Ephone templates were introduced to manage soft keys. The only
                                          					 commands that can be used in ephone templates are the softkeys commands.

Ephone-dn Templates

4.0

Ephone-dn templates were introduced.

Phone Templates for SIP Phones

4.1

The maximum number of templates that can be configured was
                                          					 increased from 5 to 10.

3.4

Voice-register templates were introduced for SIP Phones
                                          					 directly connected to a Cisco Unified CME router.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router# enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-template template-tag Example: Router(config)# ephone-template 15 | Enters
                                             				ephone-template configuration mode to create an ephone template. template-tag —Unique identifier for the ephone template that is being created. Range is 1 to 20. |
| Step 4 | command Example: Router(config-ephone-template)# features blocked Park Trnsfer | Applies the
                                             				specified command to the ephone template that is being created. Type ? for a list
                                                      					 of commands that can be used in this step. Repeat this
                                             				step for each command that you want to add to the ephone template. |
| Step 5 | exit Example: Router(config-ephone-template)# exit | Exits
                                             				ephone-template configuration mode. |
| Step 6 | ephone phone-tag Example: Router(config)# ephone 36 | Enters ephone
                                             				configuration mode. phone-tag —Unique sequence number that identifies
                                                      					 this ephone during configuration tasks. |
| Step 7 | ephone-template template-tag Example: Router(config-ephone)# ephone-template 15 | Applies an
                                             				ephone template to the ephone that is being configured. |
| Step 8 | restart Example: Router(config-ephone)# restart | Performs a
                                             				fast reboot of this ephone. Does not contact the DHCP or TFTP server for
                                             				updated information. Note Restart all
                                                         				  ephones using the restart all command in telephony-service configuration mode. | Note | Restart all
                                                         				  ephones using the restart all command in telephony-service configuration mode. |
| Note | Restart all
                                                         				  ephones using the restart all command in telephony-service configuration mode. |
| Step 9 | end Example: Router(config-ephone)# end | Returns to
                                             				privileged EXEC mode. |

| Note | Restart all
                                                         				  ephones using the restart all command in telephony-service configuration mode. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router# enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-dn-template template-tag Example: Router(config)# ephone-dn-template 3 | Enters
                                             				ephone-dn-template configuration mode to create an ephone-dn template. template-tag —Unique identifier for the ephone-dn
                                                      					 template that is being created. Range is 1 to 20. |
| Step 4 | command Example: Router(config-ephone-dn-template)# call-forwarding busy 4000 | Applies the
                                             				specified command to the ephone-dn template that is being created. Type ? for a list
                                                      					 of commands that can be used in this step. Repeat this
                                             				step to add more commands to the template. |
| Step 5 | exit Example: Router(config-ephone-dn-template)# exit | Exits
                                             				ephone-dn-template configuration mode. |
| Step 6 | ephone-dn dn-tag Example: Router(config)# ephone-dn 23 | Enters
                                             				ephone-dn configuration mode. dn-tag —Unique sequence number that identifies this
                                                      					 ephone-dn during configuration tasks. |
| Step 7 | ephone-dn-template template-tag Example: Router(config-ephone-dn)# ephone-dn-template 3 | Applies an
                                             				ephone-dn template to the ephone-dn that is being configured. |
| Step 8 | end Example: Router(config-ephone-dn)# end | Returns to
                                             				privileged EXEC mode. |

| Step 1 | show telephony-service ephone Use is command
                                             				to display information about SCCP phones in Cisco Unified CME, including which
                                             				template-tags are enabled in the configuration for a phone. Router# show telephony-service ephone 1 ephone-dn-template  1
 description Call Center Line 1
 call-forward busy 500
 call-forward noan 500 timeout 10
 pickup-group 33!
! |
|---|---|
| Step 2 | show telephony-service ephone-template Use is command
                                             				to display information about an ephone template in Cisco Unified CME, including
                                             				a list of features enabled in the configuration. |
| Step 3 | show telephony-service ephone-dn Use is command
                                             				to display information about directory numbers, including which template-tags
                                             				are enabled in the configuration for a directory number. Router# show telephony-service ephone-dn 4 !
ephone-dn  4  dual-line
 number 136
 description Desk4
 ephone-dn template 1
 ephone-hunt login |
| Step 4 | show telephony-service ephone-dn-template Use is command
                                             				to display information about an ephone-dn template in Cisco Unified CME,
                                             				including a list of features enabled in the configuration. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router# enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register template template-tag Example: Router(config)# voice register template 1 | Enters voice
                                             				register template configuration mode to define a template of common parameters
                                             				for SIP phones in Cisco Unified CME. Range is 1
                                                      					 to 5. |
| Step 4 | command Example: Router(config-register-template)# anonymous block | Applies the
                                             				specified command to this template and enables the corresponding feature on any
                                             				supported SIP phone that uses a template in which this command is configure. Type ? to display
                                                      					 list of commands that can be used in a voice register template. Repeat this
                                             				step for each feature to be added to this voice register template. |
| Step 5 | exit Example: Router(config-register-template)# exit | Exits
                                             				configuration mode to the next highest mode in the configuration mode
                                             				hierarchy. |
| Step 6 | voice register pool pool-tag Example: Router(config)# voice register pool 3 | Enters voice
                                             				register pool configuration mode to set phone-specific parameters for SIP
                                             				phones. pool-tag —Unique sequence number of the Cisco  SIP
                                                      					 phone to be configured. Range is 1 to 100 or the upper limit as defined by max-pool command. |
| Step 7 | template template-tag Example: Router(config-register-pool)# voice register pool 1 | Applies a
                                             				template created with the voice register
                                                   					 template command. template-tag —Unique sequence number of the
                                                      					 template to be applied to the SIP phone specified by the voice register
                                                            						  pool command. Range is 1 to 5. |
| Step 8 | end Example: Router(config-register-pool)# end | Returns to
                                             				privileged EXEC mode. |

| Feature Name | Cisco Unified CME Version | Feature Information |
|---|---|---|
| Ephone Templates | 4.0 | The number of ephone templates that can be created was
                                                   						  increased from 5 to 20. More commands can be included in ephone templates. |
| 3.2 | Ephone templates were introduced to manage soft keys. The only
                                          					 commands that can be used in ephone templates are the softkeys commands. |
| Ephone-dn Templates | 4.0 | Ephone-dn templates were introduced. |
| Phone Templates for SIP Phones | 4.1 | The maximum number of templates that can be configured was
                                          					 increased from 5 to 10. |
| 3.4 | Voice-register templates were introduced for SIP Phones
                                          					 directly connected to a Cisco Unified CME router. |