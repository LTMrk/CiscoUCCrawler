---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmeblock-html-5b44a6fc93
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmeblock.html
retrieved_at: 2026-08-21T07:24:38.061948+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Call Blocking

## Chapter: Call Blocking

# Call Blocking

## Information About Call Blocking

### Call Blocking
                           	 Based on Date and Time (After-Hours Toll Bar)

Call blocking to
                              		prevent unauthorized use of phones is implemented by matching dialed numbers
                              		against a pattern of specified digits and matching the time against the time of
                              		day and day of week or date that has been specified for Call Blocking. You can
                              		specify up to 32 patterns of digits for blocking.

When a user attempts
                              		to place a call to digits that match a pattern that has been specified for Call
                              		Blocking during a time period that has been defined for Call Blocking, a fast
                              		busy signal is played for approximately 10 seconds. The call is then terminated
                              		and the line is placed back in on-hook status.

The
                              		Cisco Unified CME session application accesses the current after-hours
                              		configuration and applies it to calls originated by phones that are registered
                              		to the Cisco Unified CME router. Call blocking applies to all IP phones in
                              		Cisco Unified CME, although individual IP phones can be exempted from all call
                              		blocking.

In Cisco CME 3.4 and
                              		later versions, the same time-based call-blocking mechanism that is provided
                              		for SCCP phone and on analog phones connected to SCCP-controlled analog
                              		telephone adaptors (Cisco ATA) or SCCP-controlled foreign exchange station
                              		(FXS) ports is expanded to SIP endpoints.

In Cisco CME 3.4 and
                              		later, call-blocking configuration applies to all SCCP, H.323, SIP and POTS
                              		calls that go through the Cisco Unified CME router. All incoming calls to the
                              		router, except calls from an exempt phone, are also checked against the
                              		after-hours configuration.

Prior to Cisco
                              		Unified CME 4.2(1), all Call Blocking features are implemented globally and
                              		uniformly on each phone in the system. All phones are similarly restricted
                              		according to time, date, location, and other call blocking characteristics.
                              		Call Blocking is not supported on ephone-dns that are configured to use the
                              		trunk feature, and Call Blocking did not apply to second-stage trunk dialing.

In Cisco Unified CME
                              		4.2(1) and later versions, you have the flexibility to set different call block
                              		calendars and call block patterns to phones in different departments, to block
                              		certain trunk dialing as required, and to configure Call Blocking on a
                              		particular SCCP IP phone by creating and applying a template to that phone.

For configuration
                              		information, see Configure Call Blocking .

### After-Hours
                           	 Pattern-Blocking Support for Regular Expressions

In Cisco Unified CME
                              		9.5, support for afterhours pattern blocking is extended to regular expression
                              		patterns for dial plans on Cisco Unified SIP phones and Cisco Unified SCCP IP
                              		phones. With this support, users can add a combination of fixed dial plans and
                              		regular expression-based dial plans.

When a call is
                              		initiated after hours, the dialed number is matched against a combination of
                              		dial plans. If a match is found, the call is blocked.

To enable regular
                              		expression patterns to be included when configuring afterhours pattern
                              		blocking, the after-hours block
                                    			 pattern command is modified to include regular expressions as a
                              		value for the pattern argument in the following command syntax:

after-hours block pattern pattern-tag pattern

telephony-service—For both SCCP and SIP Phones.

ephone-template—For SCCP phones only.

The maximum length
                                          		  of a regular expression pattern is 32 for both Cisco Unified SIP and Cisco
                                          		  Unified SCCP IP phones.

numbers
                                       			 beginning with ‘0’ and ‘00’

numbers
                                       			 beginning with 1800, followed by four digits

numbers
                                       			 9876512340 to 9876512345

after-hours
                                       			 block pattern 1 0*

after-hours
                                       			 block pattern 2 00*

after-hours
                                       			 block pattern 3 1800….

after-hours
                                       			 block pattern 4 987651234[0-5]

There is no change
                                          		  in the number of afterhours patterns that can be added. The maximum number is
                                          		  still 100.

After-hours block
                              		pattern 0* blocks all numbers, and 00* blocks any number starting from 0. 0*
                              		and 00* must not be denoted as regular expressions.

For more
                              		configuration examples, see Example for Configuring After-Hours Block Patterns of Regular Expressions section.

For a summary of the
                              		basic Cisco IOS regular expression characters and their functions, see Cisco Regular Expression
                                 		  Pattern Matching Characters section of Terminal
                                 		  Services Configuration Guide .

### Call Blocking
                           	 Override

directory
                                       			 number—To configure an exception for an individual directory number.

phone-level—To
                                       			 configure an exception for all directory numbers associated to a Cisco Unified
                                       			 IP phone regardless of any configuration for an individual directory number.

dial peer—To
                                       			 configure an exception for a particular dial peer.

Individual phone
                              		users can be allowed to override call blocking associated with designated time
                              		periods by entering personal identification numbers (PINs) that have been
                              		assigned to their phones. For IP phones that support soft keys, such as the
                              		Cisco Unified IP Phone 7940G and the Cisco Unified IP Phone 7960G, the
                              		call-blocking override feature allows individual phone users to override the
                              		call blocking that has been defined for designated time periods. The system
                              		administrator must first assign a personal identification number (PIN) to any
                              		phone that will be allowed to override Call Blocking.

Logging in to a
                              		phone with a PIN only allows the user to override call blocking that is
                              		associated with particular time periods. Blocking patterns that are in effect 7
                              		days a week, 24 hours a day, and they cannot be overridden by using a PIN.

When PINs are
                              		configured for call-blocking override, they are cleared at a specific time of
                              		day or after phones have been idle for a specific amount of time. The time of
                              		day and amount of time can be set by the system administrator, or the defaults
                              		can be accepted.

For configuration
                              		information, see Configure Call Blocking .

### Class of
                           	 Restriction

Class of restriction
                              		(COR) is the capability to deny certain call attempts based on the incoming and
                              		outgoing class of restrictions provisioned on the dial peers. COR specifies
                              		which incoming dial peer can use which outgoing dial peer to make a call. Each
                              		dial peer can be provisioned with an incoming and an outgoing COR list.

COR functionality
                              		provides flexibility in network design by allowing users to block calls (for
                              		example, calls to 900 numbers) and allowing different restrictions to call
                              		attempts from different originators.

For SIP phones,
                              		multiple COR lists can be applied under the voice register
                                 		  pool . A maximum of ten lists (five incoming and five outgoing) can be
                              		defined. The final COR list that is applied depends on the DN that the phone
                              		registers with the CME. This DN should match any one of the ranges defined in
                              		the COR list under the voice register pool.

For SIP Phones on
                              		Unified CME Release 12.1 and later versions, COR lists can be applied under voice register
                                 		  template configuration mode as well. If the COR list is configured
                              		under voice register
                                 		  pool and voice register
                                 		  template , the configuration under voice register
                                 		  pool takes precedence. If the COR list configuration under voice register
                                 		  pool is removed, the configuration under voice register
                                 		  template is applied.

## Configure Call Blocking

### Configure Call
                           	 Blocking

To define blocking
                                 		  patterns and time periods during which calls to matching patterns are blocked
                                 		  for all SCCP and SIP endpoints in Cisco Unified CME, to define blocking
                                 		  patterns to be matched to block calls from PSTN lines, and to deactivate logins
                                 		  on SCCP phones at a specific time or for a specified time period, perform the
                                 		  following steps.

Restriction

Prior to
                                                      				  Cisco CME 3.3, Call Blocking is not supported on analog phones connected to
                                                      				  Cisco ATAs or FXS ports in H.323 mode.

Prior to
                                                      				  Cisco CME 3.4, Call Blocking is not supported on SIP IP phones connected
                                                      				  directly in Cisco Unified CME.

Prior to
                                                      				  Cisco Unified CME 4.2(1), selective Call Blocking on IP phones and PSTN trunk
                                                      				  lines is not supported.

#### Before you begin

Dial-peers are
                                          				configured to provide PSTN access using router voice-ports or H.323/SIP trunk
                                          				connections.

### SUMMARY STEPS

- enable

- configure terminal

- telephony service

- after-hours block pattern pattern-tag pattern [ 7-24 ]

- after-hours date month date start-time stop-time

- after-hours day day
                                       				  start-time stop-time

- after-hours pstn-prefix tag
                                       				  pattern

- login [ timeout [ minutes ]] [ clear time ]

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
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

telephony service

#### Example:

```
Router(config)# telephony service
```

Enters
                                             				telephony service configuration mode.

Step 4

after-hours block pattern pattern-tag pattern [ 7-24 ]

#### Example:

```
Router(config-telephony)# after-hours block pattern 2 91
```

Defines
                                             				pattern to be matched for blocking calls from IP phones.

pattern-tag —Unique number pattern for call
                                                   					 blocking. Define up to 32 call-blocking patterns in separate commands. Range is
                                                   					 1 to 32.

This
                                                   					 command can also be configured in ephone-template configuration mode. The value
                                                   					 set in ephone-template configuration mode has priority over the value set in
                                                   					 telephony-service mode .

Step 5

after-hours date month date start-time stop-time

#### Example:

```
Router(config-telephony)# after-hours date jan 1 0:00 23:59
```

Defines a
                                             				recurring period based on date of month during which outgoing calls that match
                                             				defined block patterns are blocked on IP phones.

Enter
                                                   					 beginning and ending times for call blocking in an HH:MM format using a 24-hour
                                                   					 clock. The stop- time must be greater than the start-time .
                                                   					 The value 24:00 is not valid. If you enter 00:00as a stop time, it is changed
                                                   					 to 23:59. If you enter 00:00 for both start time and stop time, calls are
                                                   					 blocked for the entire 24-hour period on the specified date.

This
                                                   					 command can also be configured in ephone-template configuration mode. The value
                                                   					 set in ephone-template configuration mode has priority over the value set in
                                                   					 telephony-service mode.

Step 6

after-hours day day
                                                				  start-time stop-time

#### Example:

```
Router(config-telephony)# after-hours day sun 0:00 23:59
```

Defines a
                                             				recurring period based on day of the week during which outgoing calls that
                                             				match defined block patterns are blocked on IP phones

Enter
                                                   					 beginning and ending times for call blocking, in an HH:MM format using a
                                                   					 24-hour clock. The stop- time must be greater than the start-time .
                                                   					 The value 24:00 is not valid. If you enter 00:00 as a stop time, it is changed
                                                   					 to 23:59. If you enter 00:00 for both start time and stop time, calls are
                                                   					 blocked for the entire 24-hour period on the specified day.

This
                                                   					 command can also be configured in ephone-template configuration mode. The value
                                                   					 set in ephone-template configuration mode has priority over the value set in
                                                   					 telephony-service mode .

Step 7

after-hours pstn-prefix tag
                                                				  pattern

#### Example:

```
Router(config-telephony)# after-hours pstn_prefix 1 9
```

Defines the
                                             				leading digits of the pattern to be skipped when pattern matching dialed digits
                                             				on a trunk ephone-dn.

tag : Unique
                                                   					 number pattern for PSTN call blocking. Define up to 4 call-blocking patterns in
                                                   					 separate commands. Range is 1-4.

pattern :
                                                   					 identifies the unique leading digits, normally used to dial a trunk PSTN line,
                                                   					 that are blocked by this configuration.

Step 8

login [ timeout [ minutes ]] [ clear time ]

#### Example:

```
Router(config-telephony)# login timeout 120 clear 23:00
```

Deactivates
                                             				all user logins at a specific time or after a designated period of idle time on
                                             				a phone.

For SCCP
                                                   					 phones only. Not supported on SIP endpoints in Cisco Unified CME.

minutes —(Optional) Range: 1 to 1440. Default: 60.
                                                   					 Before Cisco Unified CME 4.1, the minimum value for this argument was 5
                                                   					 minutes.

Step 9

end

#### Example:

```
Router(config-telephony)# end
```

Returns to
                                             				privileged EXEC mode.

### Configure Call
                           	 Blocking Exemption for a Dial Peer

To allow H.323 and
                                 		  SIP trunk calls to utilize the voice gateway in spite of the the after-hours
                                 		  configuration in Cisco Unified CME, follow the steps in this section.

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice tag { pots | voatm | vofr | voip }

- paramspace callsetup after-hours-exempt true

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
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

dial-peer voice tag { pots | voatm | vofr | voip }

#### Example:

```
Router(config)# dial peer voice 501 voip
```

Defines a
                                             				particular dial peer, specifies the method of voice encapsulation, and enters
                                             				dial-peer configuration mode.

Step 4

paramspace callsetup after-hours-exempt true

#### Example:

```
Router(config-dialpeer)# paramspace callsetup after-hours-exempt true
```

Exempts a dial
                                             				peer from Call Blocking configuration.

Step 5

end

#### Example:

```
Router(config-dialpeer)# end
```

or

```
Router(config-register-dn)# end
```

Exits
                                             				configuration mode and enters privileged EXEC mode.

### Configure Call
                           	 Blocking Override for All SCCP Phones

To define the Call
                                 		  Blocking override code to be entered by a phone user to override all
                                 		  call-blocking rules, perform the following steps.

Restriction

Call
                                                      				  Blocking override is supported only on phones that support softkey display.

If the
                                                      				  after-hours override code is the same as the night-service code, after hours
                                                      				  Call Blocking is disabled.

Both
                                                      				  override codes defined in telephony-service and override codes defined in
                                                      				  ephone-template are enabled on all phones.

If a global
                                                      				  telephony-service override code overlaps an ephone-template override code and
                                                      				  contains more digits, an outgoing call is disabled wherever the
                                                      				  telephony-service override code is used on phones with the ephone template
                                                      				  applied. For example, if the telephony-service override code is 6241 and the
                                                      				  ephone-template override code is 62, those phones with the ephone template
                                                      				  applied will sound a fast busy tone if the 6241 override code is dialed.

#### Before you begin

Cisco Unified CME 4.2(1) or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- after-hours override-code pattern

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
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

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony service configuration mode.

Step 4

after-hours override-code pattern

#### Example:

```
Router(config-telephony)# after-hours override-code 1234
```

Defines the
                                             				pattern of digits (0-9) that overrides an after-hours call blocking
                                             				configuration.

pattern : identifies the unique set of digits that,
                                                   					 when dialed after pressing the login soft key, can override the after-hours
                                                   					 call blocking configuration.

This
                                                   					 command can also be configured in ephone-template configuration mode. The value
                                                   					 set in ephone-template configuration mode has priority over the value set in
                                                   					 telephony-service mode.

Step 5

end

#### Example:

```
Router(config-telephony)# end
```

Returns to
                                             				privileged EXEC mode.

### Configure Call
                           	 Blocking Exemption for an Individual SCCP Phone

To exempt all
                                 		  directory numbers associated with an individual SCCP phone from the Call
                                 		  Blocking configuration, follow the steps in this section.

Restriction

Call
                                                      				  Blocking override is supported only on phones that support softkey display.

### SUMMARY STEPS

- enable

- configure terminal

- ephone phone-tag

- after-hour exempt

- pin pin-number

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
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

ephone phone-tag

#### Example:

```
Router(config)# ephone 4
```

Enters ephone
                                             				configuration mode.

phone-tag —The unique sequence number for the phone
                                                   					 that is to be exempt from call blocking.

Step 4

after-hour exempt

#### Example:

```
Router(config-ephone)# after-hour exempt
```

Specifies that
                                             				this phone is exempt from call blocking. Phones exempted in this manner are not
                                             				restricted from any call-blocking patterns and no authentication of the phone
                                             				user is required.

Step 5

pin pin-number

#### Example:

```
Router(config-ephone)# pin 5555
```

Declares a
                                             				personal identification number (PIN) that is used to log into an ephone.

pin-number—N umber from four to eight digits in
                                                   					 length.

Step 6

end

#### Example:

```
Router(config-ephone)# end
```

Returns to
                                             				privileged EXEC mode.

### Configure Call Blocking Exemption for an Individual SIP Phone or
                           	 Directory Number

To exempt all extensions associated with an individual SIP phone or an
                                 		  individual directory number from the Call Blocking configuration, follow the
                                 		  steps in this section.

Restriction

The Login toll-bar override is not supported on SIP IP phones;
                                                      				  there is no pin to bypass blocking on IP phones that are connected to
                                                      				  Cisco Unified CME and running SIP.

### SUMMARY STEPS

- enable

- configure terminal

- voice register pool pool-tag or voice register dn dn-tag

- after-hour exempt

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

voice register pool pool-tag or voice register dn dn-tag

#### Example:

```
Router(config)# voice register pool 1
```

or

```
Router(config)# voice register dn 1
```

Enters voice register pool configuration mode to set parameters
                                             				for specified SIP phone.

or

Enters voice register dn mode to define a directory number for a
                                             				SIP phone, intercom line, voice port, or an MWI.

Step 4

after-hour exempt

#### Example:

```
Router(config-register-pool)# after-hour exempt
```

or

```
Router(config-register-dn)# after-hour exempt
```

Exempts all numbers on a SIP phone from call blocking.

or

Exempts an individual directory number from call blocking.

Step 5

end

#### Example:

```
Router(config-register-pool)# end
```

or

```
Router(config-register-dn)# end
```

Exits configuration mode and enters privileged EXEC mode.

### Verify Call
                           	 Blocking Configuration

Step 1

Use the show
                                                				  running-config command to display an entire configuration,
                                          			 including call-blocking number patterns and time periods and the phones that
                                          			 are marked as exempt from call blocking.

#### Example:

```
telephony-service 
			  fxo hook-flash 
			  load 7960-7940 P00305000600 
			  load 7914 S00103020002 
			  max-ephones 100
			  max-dn 500 
			  ip source-address 10.115.43.121 port 2000 
			  timeouts ringing 10 
			  voicemail 7189 
			  max-conferences 8 gain -6 
			  moh music-on-hold.au 
			  web admin system name sys3 password sys3 
			  dn-webedit 
			  time-webedit  
			  transfer-system full-consult 
			  transfer-pattern .T 
			  secondary-dialtone 9 
			  after-hours block pattern 1 91900 7-24 
			  after-hours block pattern 2 9976 7-24 
			  after-hours block pattern 3 9011 7-24 
			  after-hours block pattern 4 91...976.... 7-24 
			 ! 
			  create cnf-files version-stamp 7960 Jul 13 2004 03:39:28
```

Step 2

Use the show ephone
                                                				  login command to display the login status of all phones.

#### Example:

```
Router# show ephone login ephone 1        Pin enabled:TRUE        Logged-in:FALSE
ephone 2        Pin enabled:FALSE
ephone 3        Pin enabled:FALSE
```

Step 3

The show voice register
                                                				  dial-peer command displays all the dial peers created dynamically
                                          			 by SIP phones that have registered, along with configurations for after hours
                                          			 blocking.

### Apply Class of
                           	 Restriction to a Directory Number on SCCP Phone

To apply a class
                                 		  of restriction to a directory number, perform the following steps.

Restriction

In a Call
                                                      				  Redirection scenario (either Call Forward or Call Forward Busy), when you
                                                      				  select an outgoing dial peer, CUCME considers the Class of Restriction applied
                                                      				  on the originating extension instead of the one applied on the redirecting
                                                      				  extension. This is because the redirecting extension is an intermediate dial
                                                      				  peer that is used temporarily.

#### Before you begin

COR lists must
                                          				be created in dial peers. For information, see Class of Restrictions section in the “Dial
                                             				  Peer Configuration on Voice Gateway Routers” document in the Cisco IOS
                                          				Voice Configuration Library.

Directory
                                          				number to which COR is to be applied must be configured in Cisco Unified CME.
                                          				For configuration information, see Create Directory Numbers for SCCP Phones .

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn dn-tag

- corlist { incoming | outgoing } cor-list-name

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
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

ephone-dn dn-tag

#### Example:

```
Router(config)# ephone-dn 12
```

Enters
                                             				ephone-dn configuration mode.

Step 4

corlist { incoming | outgoing } cor-list-name

#### Example:

```
Router(config-ephone-dn)# corlist outgoing localcor
```

Configures a
                                             				COR on the dial peers associated with an ephone-dn.

Step 5

end

#### Example:

```
Router(config-ephone-dn)# end
```

Returns to
                                             				privileged EXEC mode.

### Apply Class of
                           	 Restriction to Directory Number on SIP Phones

To apply a class
                                 		  of restriction to virtual dial peers for directory numbers associated with a
                                 		  SIP IP phone connected to Cisco Unified CME, perform the following steps.

Restriction

In a Call
                                                      				  Redirection scenario (either Call Forward or Call Forward Busy), when you
                                                      				  select an outgoing dial peer, CUCME considers the Class of Restriction applied
                                                      				  on the originating extension instead of the one applied on the redirecting
                                                      				  extension. This is because the redirecting extension is an intermediate dial
                                                      				  peer that is used temporarily.

#### Before you begin

Cisco unified
                                          				CME 3.4 or a later version.

COR lists must
                                          				be created in dial peers. For information, see Class of Restrictions section in the “Dial
                                             				  Peer Configuration on Voice Gateway Routers” document in the Cisco IOS
                                             				  Voice Configuration Library .

Individual
                                          				phones to which COR is to be applied must be configured in Cisco Unified CME.
                                          				For configuration information, see Create Directory Numbers for SCCP Phones .

The COR list
                                          				configuration under voice
                                             				  register template configuration mode is supported only for Unified CME
                                          				12.1 and later releases.

### SUMMARY STEPS

- enable

- configure terminal

- Enter one of
                                 			 the following commands:

- voice register pool pool-tag

- voice register template template-tag

- cor { incoming | outgoing } cor-list-name { cor-list-number starting-number [ - ending-number ]
                                       				  | default }

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
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

Enter one of
                                          			 the following commands:

- voice register pool pool-tag

- voice register template template-tag

#### Example:

```
Router(config)# voice register pool 3
```

Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone in Cisco Unified CME.

pool-tag —Unique
                                                   					 number assigned to the pool. Range is 1 to 100.

or

Enters voice
                                             				register template configuration mode and defines a template of common
                                             				parameters for Cisco Unified SIP IP phones.

template-tag —Declares
                                                   					 a template tag. Range is 1 to 10.

Step 4

cor { incoming | outgoing } cor-list-name { cor-list-number starting-number [ - ending-number ]
                                                				  | default }

#### Example:

```
Router(config-register-pool)# cor incoming call91191011
```

Configures a
                                             				class of restriction (COR) for the dynamically created VoIP dial peers
                                             				associated with directory numbers and specifies which incoming dial peer can
                                             				use which outgoing dial peer to make a call.

Each dial
                                                   					 peer can be provisioned with an incoming and an outgoing COR list.

Step 5

end

#### Example:

```
Router(config-register-pool)# end
```

Exits
                                             				configuration mode and enters privileged EXEC mode.

### Verify Class of
                           	 Restriction

Step 1

Use the show
                                                				  running-config command or the show telephony-service
                                                				  ephone-dn command to verify whether the COR lists have been
                                          			 applied to the appropriate ephone-dns.

#### Example:

```
Router# show running-config ephone-dn 23
 number 2835
 corlist outgoing 5x
```

Step 2

Use the show dialplan
                                                				  dialpeer command to determine which outbound dial peer is matched
                                          			 for an incoming call, based on the COR criteria and the dialed number specified
                                          			 in the command line. Use the timeout keyword to enable matching variable-length destination patters associated with
                                          			 dial peers. This can increase your chances of finding a match for the dial peer
                                          			 number you specify.

#### Example:

```
Router# show dialplan dialpeer 300 number 1900111
 
VoiceOverIpPeer900
        information type = voice,
        description = `',
        tag = 900, destination-pattern = `1900',
        answer-address = `', preference=0,
        numbering Type = `unknown'
        group = 900, Admin state is up, Operation state is up,
        incoming called-number = `', connections/maximum = 0/unlimited,
        DTMF Relay = disabled,
        modem passthrough = system,
        huntstop = disabled,
        in bound application associated: 'DEFAULT'
        out bound application associated: ''
        dnis-map = 
        permission :both
        incoming COR list:maximum capability
        outgoing COR list:to900
        type = voip, session-target = `ipv4:1.8.50.7',
        technology prefix: 
        settle-call = disabled
        ...
        Time elapsed since last clearing of voice call statistics never
        Connect Time = 0, Charged Units = 0,
        Successful Calls = 0, Failed Calls = 0, Incomplete Calls = 0
        Accepted Calls = 0, Refused Calls = 0,
        Last Disconnect Cause is "",
        Last Disconnect Text is "",
        Last Setup Time = 0.
Matched: 19001111   Digits: 4
Target: ipv4:1.8.50.7
```

Step 3

Use the show dial-peer
                                                				  voice command to display the attributes associated with a
                                          			 particular dial peer.

#### Example:

```
Router# show dial-peer voice 100
 
VoiceEncapPeer100
        information type = voice,
        description = `',
        tag = 100, destination-pattern = `',
        answer-address = `', preference=0,
        numbering Type = `unknown'
        group = 100, Admin state is up, Operation state is up,
        Outbound state is up,
        incoming called-number = `555....', connections/maximum = 0/unlimited,
        DTMF Relay = disabled,
        huntstop = disabled,
        in bound application associated: 'vxml_inb_app'
        out bound application associated: ''
        dnis-map =
        permission :both
        incoming COR list:maximum capability
        outgoing COR list:minimum requirement
        type = pots, prefix = `',
        forward-digits default
        session-target = `', voice-port = `',
        direct-inward-dial = disabled,
        digit_strip = enabled,
        register E.164 number with GK = TRUE
 
        Connect Time = 0, Charged Units = 0,
        Successful Calls = 0, Failed Calls = 0, Incomplete Calls = 0
        Accepted Calls = 0, Refused Calls = 0,
        Last Disconnect Cause is "",
        Last Disconnect Text is "",
        Last Setup Time = 0.
```

## Configuration Examples for Call Blocking

### Example for Configuring Call Blocking

The following example defines several patterns of digits for which
                                 		  outgoing calls are blocked. Patterns 1 and 2, which block calls to external
                                 		  numbers that begin with “1” and “011,” are blocked on Monday through Friday
                                 		  before 7 a.m. and after 7 p.m., on Saturday before 7 a.m. and after 1 p.m., and
                                 		  all day Sunday. Pattern 3 blocks calls to 900 numbers 7 days a week, 24 hours a
                                 		  day. The IP phone with tag number 23 and MAC address 00e0.8646.9242 is not
                                 		  restricted from calling any of the blocked patterns.

```
telephony-service
 after-hours block pattern 1 91
 after-hours block pattern 2 9011
 after-hours block pattern 3 91900 7-24
 after-hours day mon 19:00 07:00
 after-hours day tue 19:00 07:00
 after-hours day wed 19:00 07:00
 after-hours day thu 19:00 07:00
 after-hours day fri 19:00 07:00
 after-hours day sat 13:00 12:00
 after-hours day sun 12:00 07:00
!
ephone 23
 mac 00e0.8646.9242
 button 1:33
 after-hour exempt
!
ephone 24
 mac 2234.1543.6352
 button 1:34
 
The following example deactivates a phone’s login after three hours of idle time and clears all logins at 10 p.m.:
ephone 1
 pin 1000
!
telephony-service
 login timeout 180 clear 2200
```

### Example for Configuring Class of Restriction

The following example shows three dial peers for dialing local
                                 		  destinations, long distance, and 911. COR list user1 can access the dial peers
                                 		  used to call 911 and local destinations. COR list user2 can access all three
                                 		  dial peers. Ephone-dn 1 is assigned COR list user1 to call local destinations
                                 		  and 911, and ephone-dn 2 is assigned COR list user2 to call 911, local
                                 		  destinations, and long distance.

```
dial-peer cor custom 
 name local 
 name longdistance
 name 911 
!
dial-peer cor list call-local 
 member local 
!
dial-peer cor list call-longdistance 
 member longdistance
!
dial-peer cor list call-911
 member 911 
!
dial-peer cor list user1
 member 911 
 member local
!
dial-peer cor list user2 
 member 911 
 member local 
 member longdistance 
!
dial-peer voice 1 pots 
 corlist outgoing call-longdistance 
 destination-pattern 91.......... 
 port 2/0/0
 prefix 1
!
dial-peer voice 2 pots 
 corlist outgoing call-local
 destination-pattern 9[2-9]...... 
 port 2/0/0 
 forward-digits 7
!
dial-peer voice 3 pots 
 corlist outgoing call-911 
 destination-pattern 9911 
 port 2/0/0 
 prefix 911
!
ephone-dn 1 
 corlist incoming user1
 corlist outgoing user1
!
ephone-dn 2 
 corlist incoming user2
 corlist outgoing user2
```

### Example for Configuring After-Hours Block Patterns of Regular
                           	 Expressions

The following example shows how to configure several afterhours block
                                 		  patterns of regular expressions:

```
Router# configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.

Router(config)# telephony-service 

Router(config-telephony)# after-hours block pattern 1 ?
  WORD  Specific block pattern or a regular expression for after-hour block
        pattern

Router(config-telephony)# after-hours block pattern 1 1234 Router(config-telephony)# after-hours block pattern 2 .T Router(config-telephony)# after-hours block pattern 3 987654([1-3])+ Router(config-telephony)# after-hours block pattern 4 98765432[1-9] Router(config-telephony)# after-hours block pattern 5 98765(432|422|456)
```

## Where to Go
                        	 Next

After modifying a
                           		configuration for a Cisco Unified IP phone connected to Cisco Unified CME, you
                           		must reboot the phone to make the changes take effect. For more information,
                           		see Reset and Restart Cisco Unified IP Phones .

### Soft Key
                              		  Control

To move or remove
                              		  the Login soft key on one or more phones, create and apply an ephone template
                              		  that contains the appropriate softkeys commands.

For more
                              		  information, see Customize Softkeys .

### Ephone-dn
                              		  Templates

The corlist command can be included in an ephone-dn template that is applied to one or more
                              		  ephone-dns. For more information, see Templates .

## Feature
                        	 Information for Call Blocking

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature
                                          					 Name

Cisco Unified CME Version

Feature
                                          					 Information

Call
                                          					 Blocking

4.2(1)

Added
                                          					 support for selective call blocking on IP phones and PSTN trunk lines.

3.4

Support for Call Blocking on SIP IP phones connected directly in
                                                						  Cisco Unified CME was introduced.

All
                                                						  incoming calls to the router, except calls from an exempt phone, are also
                                                						  checked against the after-hours configuration.

3.3

Added
                                          					 support for Call Blocking on analog phones connected to Cisco ATAs or FXS ports
                                          					 in H.323 mode.

3.0

Call
                                                						  blocking based on date and time was introduced.

Override of Call Blocking was introduced.

Class of
                                          					 Restriction

12.1

Added
                                          					 support for COR configuration in voice register template configuration mode for
                                          					 Unified CME.

3.4

Added
                                          					 support for COR on SIP IP Phones connected directly in Cisco Unified CME.

2.0

Class of
                                          					 restriction was introduced.

| Note | The maximum length
                                          		  of a regular expression pattern is 32 for both Cisco Unified SIP and Cisco
                                          		  Unified SCCP IP phones. |
|---|---|

| Note | There is no change
                                          		  in the number of afterhours patterns that can be added. The maximum number is
                                          		  still 100. |
|---|---|

| Restriction | Prior to
                                                      				  Cisco CME 3.3, Call Blocking is not supported on analog phones connected to
                                                      				  Cisco ATAs or FXS ports in H.323 mode. Prior to
                                                      				  Cisco CME 3.4, Call Blocking is not supported on SIP IP phones connected
                                                      				  directly in Cisco Unified CME. Prior to
                                                      				  Cisco Unified CME 4.2(1), selective Call Blocking on IP phones and PSTN trunk
                                                      				  lines is not supported. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony service Example: Router(config)# telephony service | Enters
                                             				telephony service configuration mode. |
| Step 4 | after-hours block pattern pattern-tag pattern [ 7-24 ] Example: Router(config-telephony)# after-hours block pattern 2 91 | Defines
                                             				pattern to be matched for blocking calls from IP phones. pattern-tag —Unique number pattern for call
                                                   					 blocking. Define up to 32 call-blocking patterns in separate commands. Range is
                                                   					 1 to 32. This
                                                   					 command can also be configured in ephone-template configuration mode. The value
                                                   					 set in ephone-template configuration mode has priority over the value set in
                                                   					 telephony-service mode . |
| Step 5 | after-hours date month date start-time stop-time Example: Router(config-telephony)# after-hours date jan 1 0:00 23:59 | Defines a
                                             				recurring period based on date of month during which outgoing calls that match
                                             				defined block patterns are blocked on IP phones. Enter
                                                   					 beginning and ending times for call blocking in an HH:MM format using a 24-hour
                                                   					 clock. The stop- time must be greater than the start-time .
                                                   					 The value 24:00 is not valid. If you enter 00:00as a stop time, it is changed
                                                   					 to 23:59. If you enter 00:00 for both start time and stop time, calls are
                                                   					 blocked for the entire 24-hour period on the specified date. This
                                                   					 command can also be configured in ephone-template configuration mode. The value
                                                   					 set in ephone-template configuration mode has priority over the value set in
                                                   					 telephony-service mode. |
| Step 6 | after-hours day day
                                                				  start-time stop-time Example: Router(config-telephony)# after-hours day sun 0:00 23:59 | Defines a
                                             				recurring period based on day of the week during which outgoing calls that
                                             				match defined block patterns are blocked on IP phones Enter
                                                   					 beginning and ending times for call blocking, in an HH:MM format using a
                                                   					 24-hour clock. The stop- time must be greater than the start-time .
                                                   					 The value 24:00 is not valid. If you enter 00:00 as a stop time, it is changed
                                                   					 to 23:59. If you enter 00:00 for both start time and stop time, calls are
                                                   					 blocked for the entire 24-hour period on the specified day. This
                                                   					 command can also be configured in ephone-template configuration mode. The value
                                                   					 set in ephone-template configuration mode has priority over the value set in
                                                   					 telephony-service mode . |
| Step 7 | after-hours pstn-prefix tag
                                                				  pattern Example: Router(config-telephony)# after-hours pstn_prefix 1 9 | Defines the
                                             				leading digits of the pattern to be skipped when pattern matching dialed digits
                                             				on a trunk ephone-dn. tag : Unique
                                                   					 number pattern for PSTN call blocking. Define up to 4 call-blocking patterns in
                                                   					 separate commands. Range is 1-4. pattern :
                                                   					 identifies the unique leading digits, normally used to dial a trunk PSTN line,
                                                   					 that are blocked by this configuration. |
| Step 8 | login [ timeout [ minutes ]] [ clear time ] Example: Router(config-telephony)# login timeout 120 clear 23:00 | Deactivates
                                             				all user logins at a specific time or after a designated period of idle time on
                                             				a phone. For SCCP
                                                   					 phones only. Not supported on SIP endpoints in Cisco Unified CME. minutes —(Optional) Range: 1 to 1440. Default: 60.
                                                   					 Before Cisco Unified CME 4.1, the minimum value for this argument was 5
                                                   					 minutes. |
| Step 9 | end Example: Router(config-telephony)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | dial-peer voice tag { pots \| voatm \| vofr \| voip } Example: Router(config)# dial peer voice 501 voip | Defines a
                                             				particular dial peer, specifies the method of voice encapsulation, and enters
                                             				dial-peer configuration mode. |
| Step 4 | paramspace callsetup after-hours-exempt true Example: Router(config-dialpeer)# paramspace callsetup after-hours-exempt true | Exempts a dial
                                             				peer from Call Blocking configuration. |
| Step 5 | end Example: Router(config-dialpeer)# end or Router(config-register-dn)# end | Exits
                                             				configuration mode and enters privileged EXEC mode. |

| Restriction | Call
                                                      				  Blocking override is supported only on phones that support softkey display. If the
                                                      				  after-hours override code is the same as the night-service code, after hours
                                                      				  Call Blocking is disabled. Both
                                                      				  override codes defined in telephony-service and override codes defined in
                                                      				  ephone-template are enabled on all phones. If a global
                                                      				  telephony-service override code overlaps an ephone-template override code and
                                                      				  contains more digits, an outgoing call is disabled wherever the
                                                      				  telephony-service override code is used on phones with the ephone template
                                                      				  applied. For example, if the telephony-service override code is 6241 and the
                                                      				  ephone-template override code is 62, those phones with the ephone template
                                                      				  applied will sound a fast busy tone if the 6241 override code is dialed. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony service configuration mode. |
| Step 4 | after-hours override-code pattern Example: Router(config-telephony)# after-hours override-code 1234 | Defines the
                                             				pattern of digits (0-9) that overrides an after-hours call blocking
                                             				configuration. pattern : identifies the unique set of digits that,
                                                   					 when dialed after pressing the login soft key, can override the after-hours
                                                   					 call blocking configuration. This
                                                   					 command can also be configured in ephone-template configuration mode. The value
                                                   					 set in ephone-template configuration mode has priority over the value set in
                                                   					 telephony-service mode. |
| Step 5 | end Example: Router(config-telephony)# end | Returns to
                                             				privileged EXEC mode. |

| Restriction | Call
                                                      				  Blocking override is supported only on phones that support softkey display. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone phone-tag Example: Router(config)# ephone 4 | Enters ephone
                                             				configuration mode. phone-tag —The unique sequence number for the phone
                                                   					 that is to be exempt from call blocking. |
| Step 4 | after-hour exempt Example: Router(config-ephone)# after-hour exempt | Specifies that
                                             				this phone is exempt from call blocking. Phones exempted in this manner are not
                                             				restricted from any call-blocking patterns and no authentication of the phone
                                             				user is required. |
| Step 5 | pin pin-number Example: Router(config-ephone)# pin 5555 | Declares a
                                             				personal identification number (PIN) that is used to log into an ephone. pin-number—N umber from four to eight digits in
                                                   					 length. |
| Step 6 | end Example: Router(config-ephone)# end | Returns to
                                             				privileged EXEC mode. |

| Restriction | The Login toll-bar override is not supported on SIP IP phones;
                                                      				  there is no pin to bypass blocking on IP phones that are connected to
                                                      				  Cisco Unified CME and running SIP. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice register pool pool-tag or voice register dn dn-tag Example: Router(config)# voice register pool 1 or Router(config)# voice register dn 1 | Enters voice register pool configuration mode to set parameters
                                             				for specified SIP phone. or Enters voice register dn mode to define a directory number for a
                                             				SIP phone, intercom line, voice port, or an MWI. |
| Step 4 | after-hour exempt Example: Router(config-register-pool)# after-hour exempt or Router(config-register-dn)# after-hour exempt | Exempts all numbers on a SIP phone from call blocking. or Exempts an individual directory number from call blocking. |
| Step 5 | end Example: Router(config-register-pool)# end or Router(config-register-dn)# end | Exits configuration mode and enters privileged EXEC mode. |

| Step 1 | Use the show
                                                				  running-config command to display an entire configuration,
                                          			 including call-blocking number patterns and time periods and the phones that
                                          			 are marked as exempt from call blocking. Example: telephony-service 
			  fxo hook-flash 
			  load 7960-7940 P00305000600 
			  load 7914 S00103020002 
			  max-ephones 100
			  max-dn 500 
			  ip source-address 10.115.43.121 port 2000 
			  timeouts ringing 10 
			  voicemail 7189 
			  max-conferences 8 gain -6 
			  moh music-on-hold.au 
			  web admin system name sys3 password sys3 
			  dn-webedit 
			  time-webedit  
			  transfer-system full-consult 
			  transfer-pattern .T 
			  secondary-dialtone 9 
			  after-hours block pattern 1 91900 7-24 
			  after-hours block pattern 2 9976 7-24 
			  after-hours block pattern 3 9011 7-24 
			  after-hours block pattern 4 91...976.... 7-24 
			 ! 
			  create cnf-files version-stamp 7960 Jul 13 2004 03:39:28 |
|---|---|
| Step 2 | Use the show ephone
                                                				  login command to display the login status of all phones. Example: Router# show ephone login ephone 1        Pin enabled:TRUE        Logged-in:FALSE
ephone 2        Pin enabled:FALSE
ephone 3        Pin enabled:FALSE |
| Step 3 | The show voice register
                                                				  dial-peer command displays all the dial peers created dynamically
                                          			 by SIP phones that have registered, along with configurations for after hours
                                          			 blocking. |

| Restriction | In a Call
                                                      				  Redirection scenario (either Call Forward or Call Forward Busy), when you
                                                      				  select an outgoing dial peer, CUCME considers the Class of Restriction applied
                                                      				  on the originating extension instead of the one applied on the redirecting
                                                      				  extension. This is because the redirecting extension is an intermediate dial
                                                      				  peer that is used temporarily. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-dn dn-tag Example: Router(config)# ephone-dn 12 | Enters
                                             				ephone-dn configuration mode. |
| Step 4 | corlist { incoming \| outgoing } cor-list-name Example: Router(config-ephone-dn)# corlist outgoing localcor | Configures a
                                             				COR on the dial peers associated with an ephone-dn. |
| Step 5 | end Example: Router(config-ephone-dn)# end | Returns to
                                             				privileged EXEC mode. |

| Restriction | In a Call
                                                      				  Redirection scenario (either Call Forward or Call Forward Busy), when you
                                                      				  select an outgoing dial peer, CUCME considers the Class of Restriction applied
                                                      				  on the originating extension instead of the one applied on the redirecting
                                                      				  extension. This is because the redirecting extension is an intermediate dial
                                                      				  peer that is used temporarily. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | Enter one of
                                          			 the following commands: voice register pool pool-tag voice register template template-tag Example: Router(config)# voice register pool 3 | Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone in Cisco Unified CME. pool-tag —Unique
                                                   					 number assigned to the pool. Range is 1 to 100. or Enters voice
                                             				register template configuration mode and defines a template of common
                                             				parameters for Cisco Unified SIP IP phones. template-tag —Declares
                                                   					 a template tag. Range is 1 to 10. |
| Step 4 | cor { incoming \| outgoing } cor-list-name { cor-list-number starting-number [ - ending-number ]
                                                				  \| default } Example: Router(config-register-pool)# cor incoming call91191011 | Configures a
                                             				class of restriction (COR) for the dynamically created VoIP dial peers
                                             				associated with directory numbers and specifies which incoming dial peer can
                                             				use which outgoing dial peer to make a call. Each dial
                                                   					 peer can be provisioned with an incoming and an outgoing COR list. |
| Step 5 | end Example: Router(config-register-pool)# end | Exits
                                             				configuration mode and enters privileged EXEC mode. |

| Step 1 | Use the show
                                                				  running-config command or the show telephony-service
                                                				  ephone-dn command to verify whether the COR lists have been
                                          			 applied to the appropriate ephone-dns. Example: Router# show running-config ephone-dn 23
 number 2835
 corlist outgoing 5x |
|---|---|
| Step 2 | Use the show dialplan
                                                				  dialpeer command to determine which outbound dial peer is matched
                                          			 for an incoming call, based on the COR criteria and the dialed number specified
                                          			 in the command line. Use the timeout keyword to enable matching variable-length destination patters associated with
                                          			 dial peers. This can increase your chances of finding a match for the dial peer
                                          			 number you specify. Example: Router# show dialplan dialpeer 300 number 1900111
 
VoiceOverIpPeer900
        information type = voice,
        description = `',
        tag = 900, destination-pattern = `1900',
        answer-address = `', preference=0,
        numbering Type = `unknown'
        group = 900, Admin state is up, Operation state is up,
        incoming called-number = `', connections/maximum = 0/unlimited,
        DTMF Relay = disabled,
        modem passthrough = system,
        huntstop = disabled,
        in bound application associated: 'DEFAULT'
        out bound application associated: ''
        dnis-map = 
        permission :both
        incoming COR list:maximum capability
        outgoing COR list:to900
        type = voip, session-target = `ipv4:1.8.50.7',
        technology prefix: 
        settle-call = disabled
        ...
        Time elapsed since last clearing of voice call statistics never
        Connect Time = 0, Charged Units = 0,
        Successful Calls = 0, Failed Calls = 0, Incomplete Calls = 0
        Accepted Calls = 0, Refused Calls = 0,
        Last Disconnect Cause is "",
        Last Disconnect Text is "",
        Last Setup Time = 0.
Matched: 19001111   Digits: 4
Target: ipv4:1.8.50.7 |
| Step 3 | Use the show dial-peer
                                                				  voice command to display the attributes associated with a
                                          			 particular dial peer. Example: Router# show dial-peer voice 100
 
VoiceEncapPeer100
        information type = voice,
        description = `',
        tag = 100, destination-pattern = `',
        answer-address = `', preference=0,
        numbering Type = `unknown'
        group = 100, Admin state is up, Operation state is up,
        Outbound state is up,
        incoming called-number = `555....', connections/maximum = 0/unlimited,
        DTMF Relay = disabled,
        huntstop = disabled,
        in bound application associated: 'vxml_inb_app'
        out bound application associated: ''
        dnis-map =
        permission :both
        incoming COR list:maximum capability
        outgoing COR list:minimum requirement
        type = pots, prefix = `',
        forward-digits default
        session-target = `', voice-port = `',
        direct-inward-dial = disabled,
        digit_strip = enabled,
        register E.164 number with GK = TRUE
 
        Connect Time = 0, Charged Units = 0,
        Successful Calls = 0, Failed Calls = 0, Incomplete Calls = 0
        Accepted Calls = 0, Refused Calls = 0,
        Last Disconnect Cause is "",
        Last Disconnect Text is "",
        Last Setup Time = 0. |

| Feature
                                          					 Name | Cisco Unified CME Version | Feature
                                          					 Information |
|---|---|---|
| Call
                                          					 Blocking | 4.2(1) | Added
                                          					 support for selective call blocking on IP phones and PSTN trunk lines. |
| 3.4 | Support for Call Blocking on SIP IP phones connected directly in
                                                						  Cisco Unified CME was introduced. All
                                                						  incoming calls to the router, except calls from an exempt phone, are also
                                                						  checked against the after-hours configuration. |
| 3.3 | Added
                                          					 support for Call Blocking on analog phones connected to Cisco ATAs or FXS ports
                                          					 in H.323 mode. |
| 3.0 | Call
                                                						  blocking based on date and time was introduced. Override of Call Blocking was introduced. |
| Class of
                                          					 Restriction | 12.1 | Added
                                          					 support for COR configuration in voice register template configuration mode for
                                          					 Unified CME. |
| 3.4 | Added
                                          					 support for COR on SIP IP Phones connected directly in Cisco Unified CME. |
| 2.0 | Class of
                                          					 restriction was introduced. |