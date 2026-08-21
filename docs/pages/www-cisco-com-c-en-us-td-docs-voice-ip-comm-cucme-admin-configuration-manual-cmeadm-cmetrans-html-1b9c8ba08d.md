---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmetrans-html-1b9c8ba08d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmetrans.html
retrieved_at: 2026-08-21T07:24:53.867771+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Call Transfer and
	 Forward

## Chapter: Call Transfer and
	 Forward

# Call Transfer and
                     	 Forward

## Information About Call Transfer and Forward

### Call
                           	 Forward

Call forward
                              		feature diverts calls to a specified number under one or more of the following
                              		conditions:

- All calls—When all-call
                                 		  call forwarding is activated by a phone user, all incoming calls are diverted.
                                 		  The target destination for diverted calls can be specified in the router
                                 		  configuration or by the phone user with a soft key or feature access code. The
                                 		  most recently entered destination is recognized by Cisco Unified CME,
                                 		  regardless of how it was entered.

- No answer—Incoming calls
                                 		  are diverted when the extension does not answer before the timeout expires. The
                                 		  target destination for diverted calls is specified in the router configuration.

- Busy—Incoming calls are
                                 		  diverted when the extension is busy and call waiting is not active. The target
                                 		  destination for diverted calls is specified in the router configuration.

- Night service—All incoming calls are
                                 		  automatically diverted during night-service hours. The target destination for
                                 		  diverted calls is specified in the router configuration.

A directory number
                              		can have all four types of call forwarding defined at the same time with a
                              		different forwarding destination defined for each type of call forwarding. If
                              		more than one type of call forwarding is active at one time, the order for
                              		evaluating the different types is as follows:

- Call forward night-service

- Call forward all

- Call forward busy and call forward
                                 		  no-answer

H.450.3 capabilities
                              		are enabled globally on the router by default, and can be disabled either
                              		globally or for individual dial peers. You can configure incoming patterns for
                              		using the H.450.3 standard. Calling-party numbers that do not match the
                              		patterns defined with this command are forwarded using Cisco-proprietary call
                              		forwarding for backward compatibility. For information about configuring
                              		H.450.3 on a Cisco Unified CME system, see Enable Call Forwarding for a Directory Number .

#### Selective Call
                              	 Forward

You can apply call
                                 		forward to a busy or no-answer directory number based on the number that is
                                 		dialed to reach the directory number: the primary number, the secondary number,
                                 		or either of those numbers expanded by a dial-plan pattern.

Cisco Unified CME
                                 		automatically creates one POTS dial peer for each ephone-dn when it is assigned
                                 		a primary number. If the ephone-dn is assigned a secondary number, it creates a
                                 		second POTS dial peer. If the dialplan-pattern command is used to expand the
                                 		primary and secondary numbers for ephone-dns, it creates two more dial peers,
                                 		resulting in the creation of the following four dial peers for the ephone-dn:

A POTS dial peer
                                       			 for the primary number

A POTS dial peer
                                       			 for the secondary number

A POTS dial peer
                                       			 for the primary number as expanded by the dialplan-pattern command

A POTS dial peer
                                       			 for the secondary number as expanded by the dialplan-pattern command

Call forwarding is
                                 		normally applied to all dial peers created for an ephone-dn. Selective call
                                 		forwarding allows you to apply call forwarding for busy or no-answer calls only
                                 		for the dial peers you have specified, based on the called number that was used
                                 		to route the call to the ephone-dn.

```
For example, the following commands set up a single ephone-dn (ephone-dn 5) with four dial peers:
```

```
telephony-service
```

```
dialplan-pattern 1 40855501.. extension-length 4 extension-pattern 50..
```

```
ephone-dn 5
```

```
number 5066 secondary 5067
```

In this example,
                                 		selective call forwarding can be applied so that calls are forwarded when:

callers dial the
                                       			 primary number 5066.

when callers
                                       			 dial the secondary number 5067.

when callers
                                       			 dial the expanded numbers 4085550166 or 4085550167.

For configuration
                                 		information, see Enable Call Forwarding for a Directory Number .

### Call Forward
                           	 Unregistered

The Call Forward
                              		Unregistered (CFU) feature allows you to forward a call to a different number
                              		if the directory number (DN) is not associated with a phone or if the
                              		associated phone is not registered to Cisco Unified CME. The CFU feature is
                              		very useful for wireless phone users when the wireless phone is out of the
                              		access point or phone shuts down automatically because of an automatic shutdown
                              		feature. The service is not available and the call can be forwarded to the CFU
                              		destination. Any unregistered or floating DN can be forwarded using the CFU
                              		feature.

An unregistered DN
                              		indicates that none of its associated phones are registered to the
                              		Cisco Unified CME. A registered phone will become unregistered when the
                              		Cisco Unified CME sends an unregistration request or responses to a phone's
                              		unregistration request. Cisco Unified CME sends an unregistration request under
                              		the following circumstances:

- When the keepalive timer
                                 		  expires.

- When a user issues a reset or restart
                                 		  command on the phone.

- When an extension mobility (EM) user
                                 		  logs into the phone. (All DNs configured under the logout-profile are
                                 		  unregistered except for the shared ones that are associated with other
                                 		  registered phones.)

- When an EM user logs out of the phone.
                                 		  (All DNs configured under the user-profile are unregistered except for the
                                 		  shared ones that are associated with other registered phones.)

There is always a
                              		gap between the time the phone loses its connection with Cisco Unified CME and
                              		the time when Cisco Unified CME claims the phone is unregistered. The length of
                              		the gap depends on the keepalive timer. Cisco Unified CME considers the phone
                              		as registered and tries to associate DNs until the keepalive timer expires. You
                              		can configure the expiration for the keepalive timer using the registrar server
                              		expires max <seconds> min <seconds> command under sip in voice
                              		service voip mode for SIP IP phones. For more information, see Example for Configuring Keepalive Timer Expiration in SIP Phones .

Cisco Unified CME
                              		8.6 supports the CFU feature on SIP IP phones using the call-forward b2bua
                              		unregistered command under voice register dn tag. The CFU feature supports
                              		overlap dialing and en-bloc dialing. A call to a floating DN is forwarded to
                              		its CFU destination, if configured. Calls to a DN out of service point or
                              		phones losing connection are not forwarded to a CFU number until the phone
                              		becomes unregistered. For more information on configuring call-forward
                              		unregistered, see Example for Configuring Call Forward Unregistered for SIP IP Phones .

### B2BUA Call Forward
                           	 for SIP Devices

Cisco Unified CME 3.4 an d later versions acts as both UA server
                              		and UA client; that is, as a B2BUA. Calls into a SIP phone can be forwarded to
                              		other SIP or SCCP devices (including Cisco Unity or Cisco Unity Express,
                              		third-party voice mail systems, an auto attendant or an IVR system, such as
                              		Cisco Unified IPCC and Cisco Unified IPCC Express). In addition, SCCP phones
                              		can be forwarded to SIP phones.

Cisco Unity or other
                              		voice-messaging systems connected by a SIP trunk or SIP user agent are able to
                              		pass an MWI to a SIP phone when a call is forwarded. The SIP phone then
                              		displays the MWI when indicated by the voice-messaging system.

The call-forward
                              		busy response is triggered when a call is sent to a SIP phone using a VoIP dial
                              		peer and a busy response is received back from the phone. SIP-to-SIP call
                              		forwarding is invoked only if the phone is dialed directly. Call forwarding is
                              		not invoked when the phone number is called through a sequential, longest-idle,
                              		or peer hunt group.

You can configure
                              		call forwarding for an individual directory number, or for every number on a
                              		SIP phone. If the information is configured in both, the information under
                              		voice register dn takes precedence over the information configured under voice
                              		register pool.

For configuration
                              		information, see Configure SIP-to-SIP Phone Call Forwarding .

### Call Forward All
                           	 Synchronization for SIP Phones

The Call Forward All
                              		feature allows users to forward all incoming calls to a phone number that they
                              		specify. This feature is supported on all SIP phones and can be provisioned
                              		from either Cisco Unified CME or the individual SIP phone. Before
                              		Cisco Unified CME 4.1, there was no method for exchanging the Call Forward All
                              		configuration between Cisco Unified CME and the SIP phone. If Call Forward All
                              		was enabled on the phone, the configuration in Cisco Unified CME was not
                              		updated; conversely, the configuration in Cisco Unified CME was not sent to the
                              		phone.

In Cisco Unified CME
                              		4.1 and later, the following enhancements are supported for the
                              		Cisco Unified IP Phone 7911G, 7941G, 7941GE, 7961G, 7961GE, 7970G, and 7971GE
                              		to keep the configuration consistent between Cisco Unified CME and the SIP
                              		phone:

- When Call Forward All is
                                 		  configured on Cisco Unified CME with the call-forward
                                    			 b2bua all command, the configuration is sent to the phone which updates the
                                 		  CfwdAll soft key to indicate that Call forward All is enabled. Because Call
                                 		  Forward All is configured on a per line basis, the CfwdAll soft key is updated
                                 		  only when Call Forward All is enabled for the primary line.

- When a user enables Call Forward All
                                 		  on a phone using the CfwdAll soft key, the uniform resource identifier (URI)
                                 		  for the service (defined with the call-feature-uri command) and the call forward number
                                 		  (unless Call Forward All is disabled) is sent to Cisco Unified CME. It updates
                                 		  its voice register pool and voice register dn configuration with the call-forward
                                    			 b2bua all command to be consistent with the phone configuration.

- Call Forward All supports KPML so that
                                 		  a user does not need to press the Dial or # key, or wait for the interdigit
                                 		  timeout, to configure the Call Forward All number. Cisco Unified CME collects
                                 		  the Call Forward All digits until it finds a match in the dial peers.

For configuration
                              		information, see Configure Call-Forwarding-All Softkey URI on SIP Phones .

### Call Transfer

When you are connected to another party, call transfer allows you to
                              		shift the connection of the other party to a different number. Call transfer
                              		methods must inter-operate with systems in the other networks with which you
                              		interface. Cisco CME 3.2 and later versions provide full call-transfer and
                              		call-forwarding interoperability with call processing systems that support
                              		H.450.2, H.450.3, and H.450.12 standards. For call processing systems that do
                              		not support H.450 standards, Cisco CME 3.2 and later versions provide
                              		VoIP-to-VoIP hairpin call routing.

Call transfers can be blind or consultative. A blind transfer is one in
                              		which the transferring extension connects the caller to a destination extension
                              		before ringback begins. A consultative transfer is one in which the
                              		transferring party either connects the caller to a ringing phone (ringback
                              		heard) or speaks with the third party before connecting the caller to the third
                              		party.

You can configure blind or consultative transfer on a system-wide basis
                              		or for individual extensions. For example, in a system that is set up for
                              		consultative transfer, a specific extension with an auto-attendant that
                              		automatically transfers incoming calls to specific extension numbers can be set
                              		to use blind transfer, because auto-attendants do not use consultative
                              		transfer.

#### Call Transfer
                              	 Blocking

Transfers to all
                                 		numbers except those on local phones are automatically blocked by default.
                                 		During configuration, you can allow transfers to nonlocal numbers. In
                                 		Cisco Unified CME 4.0 and later versions, you can prevent individual phones
                                 		from transferring calls to numbers that are globally enabled for transfer. This
                                 		ensures that individual phones do not incur toll charges by transferring calls
                                 		outside the Cisco Unified CME system. Call transfer blocking can be configured
                                 		for individual phones or configured as part of a template that is applied to a
                                 		set of phones.

Another way to
                                 		eliminate toll charges on call transfers is to limit the number of digits that
                                 		phone users can dial when transferring calls. For example, if you specify a
                                 		maximum of eight digits in the configuration, users who are transferring calls
                                 		can dial one digit for external access and seven digits more, which is
                                 		generally enough for a local number but not a long-distance number. In most
                                 		locations, this plan will limit transfers to nontoll destinations.
                                 		Long-distance calls, which typically require ten digits or more, will not be
                                 		allowed. This configuration is only necessary when global transfer to numbers
                                 		outside the Cisco Unified CME system has been enabled using the transfer-pattern (telephony-service) command.
                                 		Transfers to numbers outside the Cisco Unified CME system are not permitted by
                                 		default.

For configuration
                                 		information, see Configure Call Transfer Options for SCCP Phones .

### Trunk-to-Trunk
                           	 Transfer Blocking for Toll Fraud Prevention on Cisco Unified SIP IP
                           	 Phones

In Cisco Unified CME
                              		4.0 trunk-to-trunk transfer blocking for toll bypass fraud prevention is
                              		supported on Cisco Unified Skinny Client Control Protocol (SCCP) IP phones.

In Cisco Unified CME
                              		9.5, trunk-to-trunk transfer blocking for toll bypass fraud prevention is also
                              		supported on Cisco Unified Session Initiation Protocol (SIP) IP phones.

In Cisco Unified CME
                              		10.5, trunk-to-trunk conference blocking is also supported on Cisco Unified
                              		Skinny Client Control Protocol (SCCP) and Cisco Unified Session Initiation
                              		Protocol (SIP) IP phones.

Table 1 lists the transfer-blocking commands and the appropriate configuration modes
                              		for Cisco Unified CME and Cisco Unified SRST.

Commands

Cisco
                                             				  Unified CME

transfer-pattern

telephony-service

transfer max-length

voice register pool

or

voice register template

transfer-pattern
                                                					 blocked

voice register pool

or

voice register template

conference
                                             				  transfer-pattern

telephony-service

conference max-length

ephone

ephone-template

voice register pool

voice register template

conference-pattern
                                                					 blocked

ephone

ephone-template

voice register pool

voice register template

#### Transfer
                              	 Pattern

The transfer-pattern command for Cisco Unified SCCP IP
                                 		phones is extended to Cisco Unified SIP IP phones.

```
transfer-pattern transfer-pattern [ blind ]
```

With the transfer-pattern command configured, only call
                                 		transfers to numbers that match the configured transfer pattern are allowed to
                                 		take place. With the transfer pattern configured, all or a subset of transfer
                                 		numbers can be dialed and the transfer to a remote party can be initiated.

The following are
                                 		examples of configurable transfer patterns:

.T—This
                                       			 configuration allows call transfers to any destinations with one or more
                                       			 digits, like 123, 877656, or 76548765.

919........—This
                                       			 configuration only allows call transfers to remote numbers beginning with “919”
                                       			 and followed by eight digits, like 91912345678. However, call transfers to
                                       			 9191234 or 919123456789 are not allowed.

##### Backward Compatibility

To maintain backward compatibility, all call transfers from Cisco
                                    		Unified SIP IP phones to any number (local or over trunk) are allowed when no
                                    		transfer patterns are configured through the transfer-pattern , transfer-pattern blocked , or transfer max-length commands.

For Cisco Unified SCCP IP phones, call transfers over trunk continue to
                                    		be blocked when no transfer patterns are configured.

##### Dial Plans

Whatever dial plan is used for external calls, the same numbers should
                                    		be configured as specific numbers using the transfer-pattern command.

If a dial plan requires “9” to be dialed before an external call is
                                    		made, then “9” should be a prefix of the transfer-pattern number. For example,
                                    		12345678 is an external number that requires “9” to be dialed before the
                                    		external call can be made so the transfer-pattern number should be 912345678.

#### Transfer Max-Length

The transfer max-length command is used to indicate
                                 		the maximum length of the number being dialed for a call transfer. When only a
                                 		specific number of digits are to be allowed during a call transfer, a value
                                 		between 3 and 16 is configured. When the number dialed exceeds the maximum
                                 		length configured, then the call transfer is blocked.

For example, the maximum length is configured as 5, then only call
                                 		transfers from Cisco Unified SIP IP phones up to a five-digit directory number
                                 		are allowed. All call transfers to directory numbers with more than five digits
                                 		are blocked.

#### Conference
                              	 Max-Length

Conference calls are allowed when:

both conference transfer-pattern and transfer-pattern commands are configured

dialed digits match the configured transfer pattern

When conference
                                 		max-length command is configured, the Cisco Unified CME will allow the
                                 		conferences only if the dialed digits are within the max-length limit.

If configured, the
                                 		conference max-length command does not impact call transfers.

#### Conference-Pattern
                              	 Blocked

The
                                 		conference-pattern blocked command is used to prevent extensions on an ephone
                                 		or a voice register pool from initiating conferences.

conference
                                                					 max-length

no conference max-length

No
                                                   						conference-pattern blocked (default case)

Allowing/Blocking of conference call depends on configured
                                                					 conference max-length

Allowing/Blocking of conference call depends on configured
                                                					 transfer max-length

conference-pattern blocked

No
                                                					 conference calls allowed for SIP and SCCP phones.

Max-length <= allowed max-length

Max-length > allowed max-length

Transfer

Conference

Transfer

Conference

Transfer max-length + No Conference max-length (use transfer
                                             					 max-length for conference cases too, as conference max-length not configured)

Y

Y

N

N

No transfer max-length + Conference max-length (conference
                                             					 max-length has precedence over transfer max-length for conference)

Y

Y

Y

N

No transfer max-length + Conference max-length (conference
                                             					 max-length has precedence over transfer max-length for conference)

Y

Y

N

N

No transfer max-length + No conference max-length

All transfer and conference calls are allowed.

#### Configure the
                              	 Maximum Number of Digits for a Conference Call

##### Before you begin

Cisco Unified
                                          				CME 10.5 or a later version.

The conference
                                          				transfer-pattern command must be configured.

The
                                          				transfer-pattern command must be configured.

### SUMMARY STEPS

- enable

- configure terminal

- Enter one of the following commands:

- voice register pool pool-tag

- voice register template template-tag

- ephone phone-tag

- ephone template template-tag

- conference
                                          				  max-length value

- exit

### DETAILED STEPS

Step 1

enable

##### Example:

```
Router> enable
```

Enables
                                                				privileged EXEC mode.

- Enter your password if
                                                   				  prompted.

Step 2

configure terminal

##### Example:

```
Router# configure terminal
```

Enters global
                                                				configuration mode.

Step 3

Enter one of the following commands:

- voice register pool pool-tag

- voice register template template-tag

- ephone phone-tag

- ephone template template-tag

##### Example:

```
Router(config)# voice register pool 25
```

Enters voice register pool configuration mode and creates a pool configuration for a Cisco Unified SIP IP phone in Cisco Unified
                                                CME.

pool-tag —Unique number assigned to the pool. Range is 1 to 100.

or

Enters voice register template configuration mode and defines a template of common parameters for Cisco Unified SIP IP phones.

template-tag —Declares a template tag. Range is 1 to 10.

or

Enters ephone configuration mode.

phone-tag —Unique sequence number that identifies this ephone during configuration tasks. The maximum number of ephones is version and
                                                      platform-specific. Type? to display range.

Step 4

conference
                                                   				  max-length value

##### Example:

```
Router(config-register-pool)# conference max-length 6
```

Allows the
                                                				conference calls from Cisco IP phones to specified directory numbers of phones.

- conference
                                                   				  max-length—Specifies the maximum number of digits while making a conference
                                                   				  call. Range is 3 to 16.

Step 5

exit

##### Example:

```
Router(config-register-pool)# exit
```

Exits voice
                                                				register pool configuration mode and enters global configuration mode.

#### Configure
                              	 Conference Blocking Options for Phones

To prevent
                                    		  extensions from making conference calls to directory numbers that are otherwise
                                    		  allowed globally.

##### Before you begin

Cisco Unified
                                          				CME 10.5 or a later version.

The conference
                                          				transfer-pattern command must be configured.

The
                                          				transfer-pattern command must be configured.

### SUMMARY STEPS

- enable

- configure terminal

- Enter one of the following commands:

- voice register pool pool-tag or

- voice register template template-tag

- ephone phone-tag

- ephone template template-tag

- conference-pattern blocked

- exit

### DETAILED STEPS

Step 1

enable

##### Example:

```
Router> enable
```

Enables
                                                				privileged EXEC mode.

- Enter your password if
                                                   				  prompted.

Step 2

configure terminal

##### Example:

```
Router# configure terminal
```

Enters global
                                                				configuration mode.

Step 3

Enter one of the following commands:

- voice register pool pool-tag or

- voice register template template-tag

- ephone phone-tag

- ephone template template-tag

##### Example:

```
Router(config)# voice register pool 25
```

Enters voice register pool configuration mode and creates a pool configuration for a Cisco Unified SIP IP phone in Cisco Unified
                                                CME or for a set of Cisco Unified SIP IP phones in Cisco Unified SIP SRST.

- pool-tag—Unique number assigned to the pool. Range is 1 to 100.

or

Enters voice register template configuration mode and defines a template of common parameters for Cisco Unified SIP IP phones.

- template-tag—Declares a template tag. Range is 1 to 10.

or

Enters ephone configuration mode.

phone-tag—Unique sequence number that identifies this ephone during configuration tasks. The maximum number of ephones is
                                                      version and platform-specific. Type? to display range.

Step 4

conference-pattern blocked

##### Example:

```
Router(config-register-pool)#
```

Blocks
                                                				conference calls to external numbers.

- conference-pattern
                                                   				  block—Prevents extensions on an ephone or a voice register pool from initiating
                                                   				  conferences.

Step 5

exit

##### Example:

```
Router(config-register-pool)# exit
```

Exits voice
                                                				register pool configuration mode.

#### Transfer-Pattern
                              	 Blocked

When the transfer-pattern
                                       			 blocked command is configured for a specific phone, no call
                                 		transfers are allowed from that phone over the trunk.

This feature forces
                                 		unconditional blocking of all call transfers from the specific phone to any
                                 		other non-local numbers (external calls from one trunk to another trunk). No
                                 		call transfers from this specific phone are possible even when a transfer
                                 		pattern matches the dialed digits for transfer.

Table 1 compares the behaviors of Cisco Unified SCCP and SIP IP phones for specific
                                 		configurations.

Configuration

Cisco
                                                				  Unified SCCP IP Phones

Cisco
                                                				  Unified SIP IP Phones

No transfer
                                                				  patterns are configured.

All
                                                				  non-local call transfers are blocked.

All
                                                				  non-local call transfers are allowed for backward compatibility.

Specific
                                                				  transfer patterns are configured.

Call
                                                				  transfers to specific external entities are allowed.

Call
                                                				  transfers to specific external entities are allowed.

The transfer-pattern blocked command is configured.

All
                                                				  non-local call transfers are blocked.

All
                                                				  non-local call transfers are blocked.

#### Conference
                              	 Transfer-Pattern

When both the transfer-pattern and conference
                                    		  transfer-pattern commands are configured and the dialed digits match the
                                 		configured transfer pattern, conference calls are allowed. However, when the
                                 		dialed digits do not match any of the configured transfer pattern, the
                                 		conference call is blocked.

For configuration
                                 		information, see Specify Transfer Patterns for Trunk-to-Trunk Calls and Conferences for SIP and Conference-Pattern Blocked and Conference Max-Length .

For configuration
                                 		examples, see Example for Configuring Conference Transfer Patterns , Example for Configuring Maximum Length of Transfer Number , Example for Configuring Transfer Patterns ,
                                 		and Example for Blocking All Call Transfers .

#### Call Transfer
                              	 Recall on SCCP Phones

The Call Transfer
                                 		Recall feature in Cisco Unified CME 4.3 and later versions returns a
                                 		transferred call to the phone that initiated the transfer if the destination is
                                 		busy or does not answer. After a phone user completes a transfer to a directory
                                 		number on a local phone, if the transfer-to party does not answer before the
                                 		configured recall timer expires, the call is directed back to the transferor
                                 		phone. The message “Transfer Recall From xxxx ” displays
                                 		on the transferor phone.

The transfer-to
                                 		directory number cannot have Call Forward Busy enabled, or it cannot be a hunt
                                 		group pilot number. If the transfer-to directory number has Call Forward No
                                 		Answer (CFNA) enabled, Cisco Unified CME recalls the call only if the
                                 		transfer-recall timeout is set to less than the CFNA timeout. If the
                                 		transfer-recall timeout is set to more than the CFNA timeout, the call is
                                 		forwarded to the CFNA target number after the transfer-to party does not
                                 		answer.

If the transferor
                                 		phone is busy, Cisco Unified CME attempts the recall again after the
                                 		transfer-recall timeout value expires. Cisco Unified CME attempts a recall up
                                 		to three times. If the transferor phone remains busy, the call is disconnected
                                 		after the third recall attempt.

The transferor phone
                                 		and transfer-to phone must be registered to the same Cisco Unified CME, however
                                 		the transferee phone can be remote.

For configuration
                                 		information, see Enable Call Transfer and Forwarding on SCCP Phones at System-Level .

#### Call Transfer
                              	 Recall on SIP Phones

From Unified CME
                                 		11.6 onwards, Call Transfer Recall feature is supported on SIP phones. This
                                 		feature returns a transferred call to the phone that initiated the transfer if
                                 		the destination is busy or does not answer. After a phone user completes a
                                 		transfer to a directory number on a local SIP phone, and if the transfer-to
                                 		party does not answer before the configured recall timer expires, the call is
                                 		directed back to the transferor phone. The message "Transfer Recall From xxxx " displays on the
                                 		transferor phone.

The Call Transfer
                                 		Recall in SIP phones is achieved using the CLI timeouts
                                    		  transfer-recall command in voice register dn or voice register global
                                 		configuration modes.

The transfer-to
                                 		directory number cannot have Call Forward Busy enabled, or it cannot be a hunt
                                 		group pilot number. The transferor phone and transfer-to phone must be
                                 		registered to the same Cisco Unified CME, however the transferee phone can be
                                 		remote. If the transfer-to directory number has Call Forward No Answer (CFNA)
                                 		enabled, Cisco Unified CME recalls the call only if the transfer-recall timeout
                                 		is set to less than the CFNA timeout. If the transfer-recall timeout is set to
                                 		more than the CFNA timeout, the call is forwarded to the CFNA target number
                                 		after the transfer-to party does not answer. If the transfer-recall timeout is
                                 		equal to the CFNA timeout, the call is forwarded to the CFNA target number as
                                 		the CFNA timeout expires before the transfer-recall timeout.

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

When Single Number
                                 		Reach (SNR) is configured in Cisco Unified CME, the desk IP Phone rings first.
                                 		If the desk IP Phone does not answer within the configured SNR timer expiry
                                 		value, the configured remote number (mobile) starts ringing while continuing to
                                 		ring the desk IP Phone. If both the extensions does not answer the call,
                                 		transfer recall is directed back to the transferor phone. Transfer recall does
                                 		not happen if the desk IP Phone or remote phone (mobile) is busy. Also,
                                 		transfer recall does not happen if one of the SNR extensions answers the call.

For configuration
                                 		information, see Enable Call-Transfer Recall on SIP Phones at System-Level .

From Cisco Unified
                                 		CME release 11.6 onwards, call transfer recall feature supports mixed
                                 		deployment of SCCP and SIP phones. In a mixed deployment scenario, you can have
                                 		a SIP phone as transferor and with an SCCP phone being transfer-to or vice
                                 		versa.

In mixed mode, if
                                 		the transfer recall is performed with multiple SIP or SCCP transferors and a
                                 		single transfer-to SCCP phone, transfer recall display messages are displayed
                                 		on both the transferors. Here, transfer recall happens for all the calls when
                                 		the destination is busy or does not answer the call. In the case of single
                                 		transfer-to SIP phones, only the first phone call is recalled even if dual-line
                                 		is configured.

#### Consultative-Transfer Enhancements in Cisco Unified CME 4.3 and
                              	 Later Versions

Cisco Unified CME
                                 		4.3 modifies the digit-collection process for consultative call transfers.
                                 		After a phone user presses the Transfer soft key to make a consultative
                                 		transfer, a new consultative call leg is created and the Transfer soft key is
                                 		not displayed again until the dialed digits of the transfer-to number are
                                 		matched to a transfer pattern and the consultative call leg is in the alerting
                                 		state.

Transfer-to digits
                                 		dialed by the phone user are no longer buffered. The dialed digits, except the
                                 		call park FAC code, are collected on the seized consultative call-leg until the
                                 		digits match a pattern for consultative transfer, blind transfer, park-slot
                                 		transfer, park-slot transfer blocking, or PSTN transfer blocking. The existing
                                 		pattern matching process is unchanged, and you have the option of using this
                                 		new transfer digit-collection method or reverting to the former method.

Before Cisco Unified
                                 		CME 4.3, the consultative transfer feature collects dialed digits on the
                                 		original call leg until the digits either match a transfer pattern or blocking
                                 		pattern. When the transfer-to number is matched, and PSTN blocking is not
                                 		enabled, the original call is put on hold and an idle line or channel is seized
                                 		to send the dialed digits from the buffer.

The method of
                                 		matching a pattern for consultative transfer, blind transfer, park-slot
                                 		transfer, park-slot transfer blocking, PSTN transfer blocking, and after-hours
                                 		blocking remain the same. When the transfer-to number matches the pattern for a
                                 		blind transfer or park-slot transfer, Cisco Unified CME terminates the
                                 		consultative call leg and transfers the call.

After the
                                 		transfer-to digits are collected, if the transfer is not committed before the
                                 		transfer-timeout expires in 30 seconds, the consultation call leg is
                                 		disconnected.

These enhancements
                                 		are supported only if:

- The transfer-system
                                          				full-consult command (default) is set in telephony-service
                                    		  configuration mode.

- The transfer-mode
                                          				consult command (default) is set for the transferor's directory
                                    		  number (ephone-dn).

- An idle line or channel is
                                    		  available for seizing, digit collection, and dialing.

Cisco Unified CME 4.3 and later versions enable these transfer
                                 		enhancements by default.

To revert to the
                                 		digit-collection method used in previous versions of Cisco Unified CME, see Enable Call Transfer and Forwarding on SCCP Phones at System-Level .

#### Consultative
                              	 Transfer With Direct Station Select

Direct Station
                                 		Select (DSS) is a feature that allows a multi-button phone user to transfer
                                 		calls to an idle monitored line by pressing the Transfer key and the
                                 		appropriate monitored line button. A monitored line is one that appears on two
                                 		phones; one phone can use the line to make and receive calls and the other
                                 		phone simply monitors whether the line is in use. For Cisco CME 3.2 and later
                                 		versions, consultative transfers can occur during Direct Station Select
                                 		(transferring calls to idle monitored lines).

If the person
                                 		sharing the monitored line does not want to accept the call, the person
                                 		announcing the call can reconnect to the incoming call by pressing the EndCall
                                 		soft key to terminate the announcement call and pressing the Resume soft key to
                                 		reconnect to the original caller.

Direct Station Select consultative transfer is enabled with the transfer-system full-consult dss command, which defines the call transfer method for all lines served by the router. The transfer-system full-consult dss command supports the keep-conference command. See Configure Hardware Conferencing .

### H.450.2 and
                           	 H.450.3 Support

H.450.2 is a
                              		standard protocol for exchanging call-transfer information across a network,
                              		and H.450.3 is a standard protocol for exchanging call-forwarding information
                              		across a network. Cisco CME 3.0 and later versions support the H.450.2
                              		call-transfer standards and the H.450.3 call-forwarding standards that were
                              		introduced in Cisco ITS V2.1. Using the H.450.2 and H.450.3 standards to manage
                              		call transfer and forwarding in a VoIP network provides the following benefits:

- The final call path from
                                    		the transferred party to the transfer destination is optimal, with no
                                    		hairpinned routes or excessive use of resources.

Call parameters
                                    		  (for example, codec) can be different for the different call legs.

This solution is
                                    		  scalable.

There is no limit
                                    		  to the number of times a call can be transferred.

Considerations for
                              		using the H.450.2 and H.450.3 standards include the following:

Cisco IOS
                                    			 Release 12.2(15)T or a later release is required on all voice gateways in the
                                    			 network.

Support of
                                    			 H.450.2 and H.450.3 is required on all voice gateways in the network. H.450.2
                                    			 and H.450.3 are used regardless of whether the transfer-to or forward-to target
                                    			 is on the same Cisco Unified CME system as the transferring party or the
                                    			 forwarding party, so the transferred party must also support H.450.2 and the
                                    			 forwarded party must also support H.450.3. The exception is calls that can be
                                    			 reoriginated through hairpin call routing or through the use of an H.450 tandem
                                    			 gateway.

Call forwarding
                                    			 over SIP networks uses the 302 Moved
                                       				Temporarily SIP response, which works in a manner similar to the way in
                                    			 which the H.450.3 standard is used for H.323 networks. To enable call
                                    			 forwarding, you must specify a pattern that matches the calling-party numbers
                                    			 of the calls that you want to be able to forward.

Cisco Unified CME supports all SIP Refer method call transfer
                                    			 scenarios, but you must ensure that call transfer is enabled using H.450.2
                                    			 standards.

H.450 standards
                                    			 are not supported by Cisco Unified Communications Manager, Cisco BTS, or
                                    			 Cisco PGW, although hairpin call routing or an H.450 tandem gateway can be set
                                    			 up to handle calls to and from those types of systems.

The following series
                              		of figures depicts a call being transferred using H.450.2 standards. Call Transfer
                                 		  Using H.450.2: A Calls B shows A calling B. Call Transfer
                                 		  Using H.450.2: B Consults with C shows B consulting with C and putting A on hold. Call Transfer
                                 		  Using H.450.2: B Transfers A to C shows that B has connected A and C, and Call Transfer
                                 		  Using H.450.2: A and C Are Connected shows A and C directly connected, with B no longer involved in the call.

#### Tips for Using
                              	 H.450 Standards

Use H.450 standards
                                 		when a network meets the following conditions:

The router that
                                       			 you are configuring uses Cisco CME 3.0 or a later version, or Cisco ITS V2.1.

For Cisco CME
                                       			 3.0 or Cisco ITS V2.1 systems, all endpoints in the network must support
                                       			 H.450.2 and H.450.3 standards. For Cisco CME 3.1 or later systems, if some of
                                       			 the endpoints do not support H.450 standards (for example,
                                       			 Cisco Unified Communications Manager, Cisco BTS, or Cisco PGW), you can use
                                       			 hairpin call routing or an H.450 tandem gateway to handle transfers and
                                       			 forwards with those endpoints. Also, either you must explicitly disable H.450.2
                                       			 and H.450.3 on the dial peers that handle those calls or you must enable
                                       			 H.450.12 capability to automatically detect the calls that support H.450.2 and
                                       			 H.450.3 and those calls that do not.

Support for the
                                 		H.450.2 standard and the H.450.3 standard is enabled by default and can be
                                 		disabled globally or for individual dial peers. For configuration information,
                                 		see Enable Call Transfer and Forwarding on SCCP Phones at System-Level .

#### Transfer Method
                              	 Recommendations by Cisco Unified CME Version

You must specify the
                                 		method to use for call transfers: H.450.2 standard signaling or Cisco
                                 		proprietary signaling, and whether transfers should be blind or allow
                                 		consultation. Table 1 summarizes transfer method recommendations for all Cisco Unified CME versions.

Cisco Unified CME Version

transfer-system Command Default

transfer-system Keyword to Use

Transfer
                                                				  Method Recommendation

4.0 and
                                                				  later

full-consult

full-consult or full-blind

Use H.450.2
                                                				  for call transfer, which is the default for this version. You do not need to
                                                				  use the transfer-system command unless you want to use the full-blind or dss keyword.

Optionally,
                                                				  you can use the proprietary Cisco method by using the transfer-system command with the blind or local-consult keyword.

Use H.450.7
                                                				  for call transfer using QSIG supplementary services

3.0 to 3.3

blind

full-consult or full-blind

Use H.450.2
                                                				  for call transfer. You must explicitly configure the transfer-system command with the full-consult or full-blind keyword because H.450.2 is not the default for
                                                				  this version.

Optionally,
                                                				  you can use the proprietary Cisco method by using the transfer-system command with the blind or local-consult keyword.

2.1

blind

blind or local-consult

Use the
                                                				  Cisco proprietary method, which is the default for this version. You do not
                                                				  need to use the transfer-system command unless you want to use the local-consult keyword.

Optionally,
                                                				  you can use the transfer-system command with the full-consult or full-blind keyword. You must also configure the router with
                                                				  a Tcl script that is contained in the app-h450-transfer.x.x.x.x.zip file. This
                                                				  file is available from the Cisco Unified CME software download website at: Download Software .

Earlier than
                                                				  2.1

blind

blind

Use the
                                                				  Cisco proprietary method, which is the default for this version. You do not
                                                				  need to use the transfer-system command unless you want to use the local-consult keyword.

#### H.450.12
                              	 Support

Cisco CME 3.1 and
                                 		later versions support the H.450.12 call capabilities standard, which provides
                                 		a means to advertise and dynamically discover H.450.2 and H.450.3 capabilities
                                 		in voice gateway endpoints on a call-by-call basis. When discovered, the calls
                                 		associated with non-H.450 endpoints can be directed to use non-H.450 methods
                                 		for transfer and forwarding, such as hairpin call routing or H.450 tandem
                                 		gateway.

When H.450.12 is
                                 		enabled, H.450.2 and H.450.3 services are disabled for call transfers and call
                                 		forwards unless a positive H.450.12 indication is received from all other VoIP
                                 		endpoints involved in the call. If a positive H.450.12 indication is received,
                                 		the router uses the H.450.2 standard for call transfers and the H.450.3
                                 		standard for call forwarding. If a positive H.450.12 indication is not
                                 		received, the router uses the alternative method that you have configured for
                                 		call transfers and forwards, either hairpin call routing or an H.450 tandem
                                 		gateway.

You can have either
                                 		of the following situations in your network:

- All gateway endpoints
                                    		  support H.450.2 and H.450.3 standards. In this situation, no special
                                    		  configuration is required because support for H.450.2 and H.450.3 standards is
                                    		  enabled on the Cisco CME 3.1 or later router by default. H.450.12 capability is
                                    		  disabled by default, but it is not required because all calls can use H.450.2
                                    		  and H.450.3 standards.

Support for
                                             				  the H.450.12 standard is disabled by default and can be enabled globally or for
                                             				  individual dial peers.

If the call
                                             				  does not have H.450 support, it can be handled by a VoIP-to-VoIP connection
                                             				  that you configure using dial peers and Enable H.323-to-H.323 Connection Capabilities .
                                             				  The connection can be used for hairpin call routing or routing to an H.450
                                             				  tandem gateway.

- Explicitly disable H.450.2 and H.450.3
                                          				capability on a global basis or by individual dial peer, which forces all calls
                                          				to be handled by a VoIP-to-VoIP connection that you configure using dial peers
                                          				and the Enable H.323-to-H.323 Connection Capabilities .
                                          				This connection can be used for hairpin call routing or routing to an H.450
                                          				tandem gateway.

#### Hairpin Call
                              	 Routing

Cisco CME 3.1 and
                                 		later supports hairpin call routing using a VoIP-to-VoIP connection to transfer
                                 		and forward calls that cannot use H.450 standards. When a call that originally
                                 		terminated on a voice gateway is transferred or forwarded by a phone or other
                                 		application attached to the gateway, the gateway reoriginates the call and
                                 		routes the call as appropriate, making a VoIP-to-VoIP, or hairpin, connection.
                                 		This approach avoids any protocol dependency on the far-end transferred-party
                                 		endpoint or transfer-destination endpoint. Hairpin routing of transferred and
                                 		forwarded calls also causes the generation of separate billing records for each
                                 		call leg, so that the transferred or forwarded call leg is typically billed to
                                 		the user who initiates the transfer or forward.

In Cisco CME 3.2 and
                                 		later versions, transcoding between G.711 and G.729 is supported when one leg
                                 		of a VoIP-to-VoIP hairpin call uses G.711 and the other leg uses G.729.

Hairpin call routing
                                 		provides the following benefits:

- Call transfer and
                                    		  forwarding is provided to non-H.450 endpoints, such as
                                    		  Cisco Unified Communications Manager, Cisco BTS, or Cisco PGW.

- The network can also
                                    		  contain Cisco CME 3.0 or Cisco ITS 2.1 systems.

Hairpin call routing
                                 		has the following disadvantages:

- End-to-end signaling and
                                    		  media delay are increased significantly.

- A single hairpinned call
                                    		  uses as much WAN bandwidth as two directly connected calls.

VoIP-to-VoIP hairpin
                                 		connections can be made using dial peers if the allow-connections
                                    		  h323 to h323 command is enabled and at least one of the following is true:

- H.450.12 is used to detect
                                    		  calls on which H.450.2 or H.450.3 is not supported by the remote system.

- H.450.2 or H.450.3 is
                                    		  explicitly disabled.

- Cisco Unified CME automatically
                                    		  detects that the remote system is a Cisco Unified Communications Manager.

Hairpin with
                                    		  H.323: A Calls B shows a call that is made from A to B. Hairpin with
                                    		  H.323: Call is Forwarded to C shows that B has forwarded all calls to C. Hairpin with
                                    		  H.323: A is Connected to C via B shows that A and C are connected by an H.323 hairpin.

##### Tips for Using
                                 	 Hairpin Call Routing

Use hairpin call
                                    		routing when a network meets the following three conditions:

The router that
                                          			 you are configuring uses Cisco CME 3.1 or a later version.

Some or all
                                          			 calls require VoIP-to-VoIP routing because they cannot use H.450 standards,
                                          			 which can happen for any of the following reasons:

H.450
                                                				  capabilities have been explicitly disabled on the router.

H.450
                                                				  capabilities do not exist in the network.

H.450
                                                				  capabilities are supported on some endpoints and not supported on other
                                                				  endpoints, including those handled by Cisco Unified Communications Manager,
                                                				  Cisco BTS, and Cisco PGW. When some endpoints support H.450 and others do not,
                                                				  you must enable H.450.12 capabilities on the router to detect which endpoints
                                                				  are H.450-capable or designate some dial peers as H.450-capable. For more
                                                				  information about enabling H.450.12 capabilities, see Enable H.450.12 Capabilities .

No voice gateway
                                          			 is available to act as an H.450 tandem gateway.

For information
                                    		about configuring Cisco Unified CME to forward calls using local hairpin
                                    		routing, see Forward Calls Using Local Hairpin Routing .

Support for
                                    		VoIP-to-VoIP connections is disabled by default and can be enabled globally.
                                    		For configuration information, see Enable H.323-to-H.323 Connection Capabilities .

##### Calling Number
                                 	 Local

In a scenario where
                                    		calls are forwarded using local hairpin call routing, you can use the Calling
                                    		Number Local feature. Calling Number Local replaces a calling-party number and
                                    		name with the forwarding-party number and name (the local number and name). For
                                    		ephone-dns, the CLI command calling-number
                                          			 local is configured under telephony-service configuration to
                                    		enable the feature. For more information, see Cisco Unified Communications
                                       		  Manager Express Command Reference .

From Cisco Unified
                                    		CME Release 12.0 onwards, calling number local feature is supported for voice
                                    		register DNs as well. For voice register DNs, the CLI command calling-number
                                          			 local is configured in voice register global configuration mode.
                                    		For more information, see Cisco Unified Communications
                                       		  Manager Express Command Reference .

When the CLI
                                    		command calling-number
                                          			 local is enabled, the calling number is replaced with the
                                    		forwarding party's number. If the forwarded number is over a trunk, toll
                                    		charges may be applied on the forwarding number.

#### H.450 Tandem
                              	 Gateways

H.450 tandem
                                 		gateways address the limitations of hairpin call routing using a manner similar
                                 		to hairpin call routing but without the double WAN link traversal created by
                                 		hairpin connections. An H.450 tandem gateway is an additional voice gateway
                                 		that serves as a “front-end” for a call processor that does not support the
                                 		H.450 standards, such as Cisco Unified Communications Manager, Cisco BTS
                                 		Softswitch (Cisco BTS), or Cisco PSTN Gateway (Cisco PGW). Transferred and
                                 		forwarded calls that are intended for non-H.450 endpoints are terminated
                                 		instead on the H.450 tandem gateway and reoriginated there for delivery to the
                                 		non-H.450 endpoints. The H.450 tandem gateway can also serve as a PSTN gateway.

An H.450 tandem
                                 		gateway is configured with a dial peer that points to the
                                 		Cisco Unified Communications Manager or other system for which the H.450 tandem
                                 		gateway is serving as a front end. The H.450 tandem voice gateway is also
                                 		configured with dial peers that point to all the Cisco Unified CME systems in
                                 		the private H.450 network. In this way, Cisco Unified CME and the
                                 		Cisco Unified Communications Manager are not directly linked to each other, but
                                 		are instead both linked to an H.450 tandem gateway that provides H.450 services
                                 		to the non-H.450 platform.

An H.450 tandem
                                 		gateway can also work as a PSTN gateway for remote Cisco Unified CME systems
                                 		and for Cisco Unified Communications Manager (or other non-H.450 system). Use
                                 		different inbound dial peers to separate
                                 		Cisco Unified Communications Manager-to-PSTN G.711 calls from tandem
                                 		gateway-to-Cisco Unified CME G.729 calls.

VoIP-to-VoIP
                                 		connections can be made for an H.450 tandem gateway if the allow-connections
                                    		  h323 to h323 command is enabled and one or more of the following is true:

H.450.12 is used
                                       			 to dynamically detect calls on which H.450.2 or H.450.3 is not supported by the
                                       			 remote VoIP system.

H.450.2 or
                                       			 H.450.3 is explicitly disabled.

Cisco CME 3.1 or
                                       			 later automatically detects that the remote system is a
                                       			 Cisco Unified Communications Manager.

For Cisco CME 3.1
                                 		and earlier, the only type of VoIP-to-VoIP connection supported by
                                 		Cisco Unified CME is H.323-to-H.323. For Cisco CME 3.2 and later versions,
                                 		H.323-to-SIP connections are allowed only for Cisco Unified CME systems running
                                 		Cisco Unity Express.

H.450 Tandem
                                    		  Gateway shows a tandem voice gateway that is located between the central hub of the
                                 		network of a CPE-based Cisco CME 3.1 or later network and a
                                 		Cisco Unified Communications Manager network. This topology would work equally
                                 		well with a Cisco BTS or Cisco PGW in place of the
                                 		Cisco Unified Communications Manager.

In the network
                                 		topology in H.450 Tandem
                                    		  Gateway ,
                                 		the following events occur (refer to the event numbers on the illustration):

A call is
                                       			 generated from extension 4002 on phone 2, which is connected to a
                                       			 Cisco Unified Communications Manager. The H.450 tandem gateway receives the
                                       			 H.323 call and, acting as the H.323 endpoint, the H.450 tandem gateway handles
                                       			 the call connection to a Cisco Unified IP phone in a CPE-based Cisco CME 3.1 or
                                       			 later network.

The call is
                                       			 received by extension 1001 on phone 3, which is connected to Cisco Unified CME
                                       			 1. Extension 1001 performs a consultation transfer to extension 2001 on phone
                                       			 5, which is connected to Cisco Unified CME 2.

When extension
                                       			 1001 transfers the call, the H.450 tandem gateway receives an H.450.2 message
                                       			 from extension 1001.

The H.450 tandem
                                       			 gateway terminates the call leg from extension 1001 and reoriginates a call leg
                                       			 to extension 2001, which is connected to Cisco Unified CME 2.

Extension 4002
                                       			 is connected with extension 2001.

##### Tips for Using
                                 	 H.450 Tandem Gateways

Use this procedure
                                    		when a network meets the following conditions:

The router that
                                          			 you are configuring uses Cisco CME 3.1 or a later version.

Some endpoints
                                          			 in the network are not H.450-capable, including those handled by
                                          			 Cisco Unified Communications Manager, Cisco BTS, and Cisco PGW.

Support for
                                    		VoIP-to-VoIP connections is disabled by default and can be enabled globally.
                                    		For more information, see Enable H.323-to-H.323 Connection Capabilities .

Use dial peers to
                                    		set up an H.450 tandem gateway. See Dial Peers .

#### Dial Peers

Dial peers describe
                                 		the virtual interfaces to or from which a call is established. All voice
                                 		technologies use dial peers to define the characteristics associated with a
                                 		call leg. Attributes applied to a call leg include specific quality of service
                                 		(QoS) features, compression/decompression (codec), voice activity detection
                                 		(VAD), and fax rate. Dial peers are also used to establish the routing paths in
                                 		your network, including special routing paths such as hairpins and H.450 tandem
                                 		gateways. Dial peer settings override the global settings for call forward and
                                 		call transfer.

#### Q Signaling
                              	 Supplementary Services

Q Signaling (QSIG)
                                 		is an intelligent inter-PBX signaling system widely adopted by PBX vendors. It
                                 		supports a range of basic services, generic functional procedures, and
                                 		supplementary services. Cisco Unified CME 4.0 introduces supplementary services
                                 		features that allow Cisco Unified CME phones to seamlessly interwork using QSIG
                                 		with phones connected to a PBX. One benefit is that IP phones can use a PBX
                                 		message center with proper MWI notifications. Cisco Unified CME System with PBX illustrates a topology for a Cisco Unified CME system with some phones under
                                 		the control of a PBX.

The following QSIG
                                 		supplementary service features are supported in Cisco Unified CME systems. They
                                 		follow the standards from the European Computer Manufacturers Association
                                 		(ECMA) and the International Organization for Standardization (ISO) on PRI and
                                 		BRI interfaces.

- Basic calls between IP
                                    		  phones and PBX phones.

- Calling Line/Name
                                    		  identification (CLIP/CNIP) presented on an IP phone when called by a PBX phone;
                                    		  in the reverse direction, such information is provided to the called endpoint.

- Connected Line/Name identification
                                    		  (COLP/CONP) information provided when a PBX phone calls an IP phone and is
                                    		  connected; in the reverse direction, such information presented on an IP phone.

- Call Forward using QSIG and H.450.3 to
                                    		  support any combination of IP phone and PBX phone, including an IP phone in the
                                    		  Cisco Unified CME system that is connected to a PBX or an IP phone in another
                                    		  Cisco Unified CME system across an H.323 network.

- Call forward to the PBX message center
                                    		  according to the configured policy. The other two endpoints can be a mixture of
                                    		  IP phone and PBX phones.

- Hairpin call transfer, which
                                    		  interworks with a PBX in transfer-by-join mode. Note that Cisco Unified CME
                                    		  does not support the actual signaling specified for this transfer mode
                                    		  (including the involved FACILITY message service APDUs) which are intended for
                                    		  an informative purpose only and not for the transfer functionality itself. As a
                                    		  transferrer (XOR) host, Cisco Unified CME simply hairpins two call legs to
                                    		  create a connection; as a transferee (XEE) or transfer-to (XTO) host, it will
                                    		  not be aware of a transfer that is taking place on an existing leg. As a
                                    		  result, the final endpoint may not be updated with the accurate identity of its
                                    		  peer. Both blind transfer and consult transfer are supported.

- Message-waiting indicator (MWI)
                                    		  activation or deactivation requests are processed from the PBX message center.

- The PBX message center can be
                                    		  interrogated for the MWI status of a particular ephone-dn.

- A user can
                                    		  retrieve voice messages from a PBX message center by making a normal call to
                                    		  the message center access number.

For information
                                 		about enabling QSIG supplementary services, see Enable H.450.7 and QSIG Supplementary Services at System-Level and Enable H.450.7 and QSIG Supplementary Services on a Dial Peer .

#### Disable SIP
                              	 Supplementary Services for Call Forward and Call Transfer

If a destination
                                 		gateway does not support supplementary services, you can disable REFER messages
                                 		for call transfers and the redirect responses for call forwarding from being
                                 		sent by Cisco Unified CME.

For configuration
                                 		information, see Disable SIP Supplementary Services for Call Forward and Call Transfer .

#### Typical Network Scenarios for Call Transfer and Call
                              	 Forwarding

In a mixed network that involves two or more types of call agents or
                                 		call-control systems, there can be communication protocol discrepancies and
                                 		dependencies, and therefore the opportunity for interoperability errors. These
                                 		discrepancies show up most often when a call is being transferred or forwarded.
                                 		This section provides descriptions of the specific mixed-network scenarios you
                                 		might encounter when configuring a router running Cisco CME 3.1 or a later
                                 		version. Each of the following sections point to the configuration instructions
                                 		necessary to ensure call transfer and forwarding capabilities throughout the
                                 		network.

##### Cisco CME 3.1 or
                                 	 Later and Cisco IOS Gateways

In a network with
                                    		Cisco CME 3.1 or a later version and Cisco IOS gateways, all systems that might
                                    		participate in calls that involve call transfer and call forwarding are capable
                                    		of supporting the H.450.2, H.450.3, and H.450.12 standards. This is the
                                    		simplest environment for operating the Cisco CME 3.1 or later features.

Configuration for
                                    		this type of network consists of:

- Setting up call-transfer
                                       		  and call-forwarding parameters for transfers and forwards that are initiated on
                                       		  this router (H.450.2 and H.450.3 capabilities for transferred parties, transfer
                                       		  destinations, forwarded parties, and forwarding destinations are enabled by
                                       		  default). See Enable Call Transfer and Forwarding on SCCP Phones at System-Level .

- Enabling H.450.12 globally to detect
                                       		  any calls on which H.450.2 and H.450.3 standards are not supported. Although
                                       		  this step is optional, we recommend it. See Enable H.450.12 Capabilities .

- Optionally setting up VoIP-to-VoIP
                                       		  connections (hairpin call routing or H.450 tandem gateway) to route calls that
                                       		  do not support H.450.2 or H.450.3 standards. See Enable H.323-to-H.323 Connection Capabilities .

- Setting up dial peers to manage call
                                       		  legs within the network.

##### Cisco CME 3.0 or
                                 	 an Earlier Version and Cisco IOS Gateways

Before Cisco CME 3.1, H.450.2 and
                                    		H.450.3 standards are used for all calls by default and routers do not support
                                    		the H.450.12 standard.

Configuration for this type of network consists of:

Setting up call-transfer and
                                          			 call-forwarding parameters for transfers and forwards that are initiated on
                                          			 this router (H.450.2 and H.450.3 capabilities for transferred parties, transfer
                                          			 destinations, forwarded parties, and forwarding destinations are enabled by
                                          			 default). See Enable Call Transfer and Forwarding on SCCP Phones at System-Level

Enabling H.450.12 in advertise-only mode on Cisco CME 3.1 or later
                                          			 systems. As each Cisco CME 3.0 system is upgraded to Cisco CME 3.1 or later,
                                          			 enable H.450.12 in advertise-only mode. Note that no checking for H.450.2 or
                                          			 H.450.3 support is done in advertise-only mode. When all Cisco CME 3.0 systems
                                          			 in the network have been upgraded to Cisco CME 3.1 or later, remove the
                                          			 advertise-only restriction. See Enable H.450.12 Capabilities

Optionally setting up VoIP-to-VoIP connections (hairpin call
                                          			 routing or H.450 tandem gateway) to route calls that cannot use H.450.2 or
                                          			 H.450.3 standards. See Enable H.323-to-H.323 Connection Capabilities

Setting up dial peers to manage call legs within the network.

##### Cisco CME 3.1 or
                                 	 Later, Non-H.450 Gateways, and Cisco IOS Gateways

In a network with
                                    		Cisco CME 3.1 or later, non-H.450 gateways, and Cisco IOS gateways, the H.450.2
                                    		and H.450.3 services are provided only to calling endpoints that use H.450.12
                                    		to explicitly indicate that they are capable of H.450.2 and H.450.3 operations.
                                    		Because the Cisco BTS and Cisco PGW do not support the H.450.12 standard, calls
                                    		to and from these systems that involve call transfer or forwarding are handled
                                    		using H.323-to-H.323 hairpin call routing.

Configuration for
                                    		this type of network consists of:

- Setting up call-transfer
                                       		  and call-forwarding parameters for transfers and forwards that are initiated on
                                       		  this router (H.450.2 and H.450.3 capabilities for transferred parties, transfer
                                       		  destinations, forwarded parties, and forwarding destinations are enabled by
                                       		  default). Optionally disable H.450.2 and H.450.3 capabilities on dial peers
                                       		  that point to non-H.450-capable systems such as
                                       		  Cisco Unified Communications Manager, Cisco BTS, or Cisco PGW. See Enable Call Transfer and Forwarding on SCCP Phones at System-Level .

- Enabling H.450.12 to detect
                                       		  any calls on which H.450.2 and H.450.3 standards are not supported, either
                                       		  globally or for specific dial peers. See Enable H.450.12 Capabilities .

- Setting up VoIP-to-VoIP connections
                                       		  (hairpin call routing or H.450 tandem gateway) to route calls that do not
                                       		  support H.450.2 or H.450.3 standards. See Enable H.323-to-H.323 Connection Capabilities .

- Setting up dial peers to manage call
                                       		  legs within the network.

##### Cisco Unified CME,
                                 	 Non-H.450 Gateways, and Cisco IOS Gateways

In a network that
                                    		contains a mix of Cisco Unified CME versions and at least one non-H.450
                                    		gateway, the simplest configuration approach is to globally disable all H.450.2
                                    		and H.450.3 services and force H.323-to-H.323 hairpin call routing for all
                                    		transferred and forwarded calls. In this case, you would enable H.450.12
                                    		detection capabilities globally. Alternatively, you could select to enable
                                    		H.450.12 capability for specific dial peers. In this case, you would not
                                    		configure H.450.12 capability globally; you would leave it in its default
                                    		disabled state.

Configuration for
                                    		this type of network consists of:

- Setting up call-transfer
                                       		  and call-forwarding parameters for transfers and forwards that are initiated on
                                       		  this router (H.450.2 and H.450.3 capabilities for transferred parties, transfer
                                       		  destinations, forwarded parties, and forwarding destinations are enabled by
                                       		  default). See Enable Call Transfer and Forwarding on SCCP Phones at System-Level .

- Enabling H.450.12 to detect
                                       		  any calls on which H.450.2 and H.450.3 standards are not supported, either
                                       		  globally or on specific dial peers. See Enable H.450.12 Capabilities

- Setting up VoIP-to-VoIP connections
                                       		  (hairpin call routing or H.450 tandem gateway) to route all transferred and
                                       		  forwarded calls. See Enable H.323-to-H.323 Connection Capabilities .

- Setting up dial peers to manage call
                                       		  legs within the network.

##### Cisco CME 3.1 or
                                 	 Later, Cisco Unified Communications Manager, and Cisco IOS Gateways

In a network with Cisco CME 3.1 or
                                    		later, Cisco Unified Communications Manager, and Cisco IOS gateways, Cisco CME
                                    		3.1 and later versions support automatic detection of calls to and from Cisco
                                    		Unified Communications Manager using proprietary signaling elements that are
                                    		included with the standard H.323 message exchanges. The Cisco CME 3.1 or later
                                    		system uses these detection results to determine the H.450.2 and H.450.3
                                    		capabilities of calls rather than using H.450.12 supplementary services
                                    		capabilities exchange, which Cisco Unified Communications Manager does not
                                    		support. If a call is detected to be coming from or going to a Cisco Unified
                                    		Communications Manager endpoint, the call is treated as a non-H.450 call. All
                                    		other calls in this type of network are treated as though they support H.450
                                    		standards. Therefore, this type of network should contain only Cisco CME 3.1 or
                                    		later and Cisco Unified Communications Manager call-processing systems.

Configuration for this type of network consists of:

Setting up call-transfer and call-forwarding parameters for
                                          			 transfers and forwards that are initiated on this router (H.450.2 and H.450.3
                                          			 capabilities for transferred parties, transfer destinations, forwarded parties,
                                          			 and forwarding destinations are enabled by default). See Enable Call Transfer and Forwarding on SCCP Phones at System-Level

Enabling H.450.12 to detect any calls on which H.450.2 and H.450.3
                                          			 standards are not supported, either globally or on specific dial peers. See Enable H.450.12 Capabilities

Setting up VoIP-to-VoIP connections (hairpin call routing or H.450
                                          			 tandem gateway) to route all transferred and forwarded calls that are detected
                                          			 as being to or from Cisco Unified Communications Manager. See Enable H.323-to-H.323 Connection Capabilities

Setting up specific parameters for Cisco Unified Communications
                                          			 Manager. See Enable Cisco Unified Communications Manager to Interwork with Cisco Unified CME

Setting up dial peers to manage call legs within the network.

##### Cisco CME 3.0 or
                                 	 an Earlier Version, Cisco Unified Communications Manager, and Cisco IOS
                                 	 Gateways

Calls between the
                                    		Cisco Unified Communications Manager and the older Cisco CME 3.0 or
                                    		Cisco ITS V2.1 networks need special consideration. Because Cisco CME 3.0 and
                                    		Cisco ITS V2.1 systems do not support automatic
                                    		Cisco Unified Communications Manager detection and also do not natively support
                                    		H.323-to-H.323 call routing, alternative arrangements are required for these
                                    		systems.

To configure call
                                    		transfer and forwarding on the Cisco CME 3.0 router, you can select from the
                                    		following three options:

- Use a Tcl script to handle call
                                       		  transfer and forwarding by invoking Tcl-script-based H.323-to-H.323 hairpin
                                       		  call routing (app-h450-transfer.2.0.0.9.tcl or a later version). Enable this
                                       		  script on all VoIP dial peers and also under telephony-service mode, and set
                                       		  the local-hairpin script parameter to 1.

- Use a loopback-dn mechanism.

- Configure a
                                       		  loopback call path using router physical voice ports.

All three options
                                    		force use of H.323-to-H.323 hairpin call routing for all calls regardless of
                                    		whether the call is from a Cisco Unified Communications Manager or other H.323
                                    		endpoint (including Cisco CME 3.1 or later).

## Configure Call Transfer and Forwarding

### Enable Call
                           	 Transfer and Forwarding on SCCP Phones at System-Level

To enable H.450
                                 		  call transfers and forwards for transferring or forwarding parties; that is, to
                                 		  allow transfers and forwards to be initiated from a Cisco Unified CME system,
                                 		  perform the following steps.

Restriction

Call
                                                   				  transfers are handled differently depending on the Cisco Unified CME version.
                                                   				  See Transfer Method Recommendations by Cisco Unified CME Version for recommendations on selecting a transfer method for your Cisco Unified CME
                                                   				  version.

The transfer-system
                                                         						local-consult command is not supported if the transfer-to
                                                   				  destination is on the Cisco ATA, Cisco VG224, or a SCCP-controlled FXS port.

The H.450.2
                                                   				  and H.450.3 standards are not supported by
                                                   				  Cisco Unified Communications Manager, Cisco BTS, or Cisco PGW.

In versions
                                                   				  earlier than Cisco Unified CME 4.2, the caller ID displays correctly only after
                                                   				  connect; caller ID does not display correctly at Call Transfer or Call Forward.

Call-Transfer Recall

Requires
                                                   				  Cisco Unified CME 4.3 or a later version.

Transferor
                                                   				  and transfer-to party must be on the same Cisco Unified CME router; transferee
                                                   				  party can be remote to the Cisco Unified CME router.

Transfer
                                                   				  recall is not supported if the transfer-to party has Call Forward Busy enabled,
                                                   				  or if the transfer-to party is a hunt group pilot number.

If the
                                                   				  transfer-to party has Call Forward No Answer enabled, Cisco Unified CME recalls
                                                   				  a transferred call only if the transfer-recall timeout is set to less than the
                                                   				  timeout value set with the call-forward noan command.

Recall timer
                                                   				  for trunk-line directory number has precedence (set on transferor using trunk command with transfer-timeout keyword) over the transfer-recall timer.
                                                   				  Transfer recall is not initiated for hairpin transfers.

#### Before you begin

Cisco CME 3.0 or a
                                 		  later version, or Cisco ITS V2.1.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- transfer-system { blind | full-blind | full-consult [ dss ] | local-consult }

- transfer-pattern transfer-pattern [ blind ]

- call-forward
                                       				  pattern pattern

- timeouts
                                       				  transfer-recall seconds

- transfer-digit-collect { new-call | orig-call }

- exit

- voice service
                                       				  voip

- supplementary-service
                                       				  h450.2

- supplementary-service
                                       				  h450.3

- exit

- dial-peer voice tag voip

- supplementary-service
                                       				  h450.2

- supplementary-service
                                       				  h450.3

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

- Enter your password if
                                                				  prompted.

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
                                             				telephony-service configuration mode.

Step 4

transfer-system { blind | full-blind | full-consult [ dss ] | local-consult }

#### Example:

```
Router(config-telephony)# transfer-system full-consult
```

Specifies the
                                             				call transfer method.

blind —Calls are transferred without consultation using the
                                                   					 Cisco proprietary method and a single phone line. This is the default in
                                                   					 versions earlier than Cisco Unified CME 4.0.

full-blind —Calls are transferred without consultation using
                                                   					 H.450.2 standard methods.

full-consult —Calls are transferred with consultation using
                                                   					 H.450.2 standard methods and a second phone line if available. Calls fall back
                                                   					 to full-blind if the second line is unavailable. This is the default in
                                                   					 Cisco Unified CME 4.0 and later versions. Transfer-system needs to be set at
                                                   					 full-consult for the “transfer by directory” to work. Transfer by directory is
                                                   					 supported by full-consult or blind transfer. If you want to transfer using
                                                   					 directory/placed/missed/received calls, the transfer-system needs to be set at
                                                   					 full-consult for this to work appropriately. When changed to full-consult, you
                                                   					 can do "blind transfer" by selecting the number from the directory and when the
                                                   					 other phone rings, you can press the softkey "Transfer" and the call will be
                                                   					 transferred to the number selected and then you can hang up.

dss —(Optional) Calls are transferred with consultation to
                                                   					 idle monitored lines. All other call-transfer behavior is identical to
                                                   					 full-consult.

local-consult —Calls are transferred with local consultation
                                                   					 using a second phone line if available. The calls fall back to blind for
                                                   					 nonlocal consultation or nonlocal transfer target. Not supported if transfer-to
                                                   					 destination is on the Cisco ATA, Cisco VG224, or a SCCP-controlled FXS port.

Cisco CME
                                                   					 3.0 and later versions—Use only the full-blind or full-consult keyword.

Before
                                                   					 Cisco CME 3.0—Use the local-consult or blind keyword. (Cisco ITS 2.1 can use the full-blind or full-consult keyword by also using the Tcl script in the
                                                   					 file called app-h450-transfer.x.x.x.x.zip.)

Step 5

transfer-pattern transfer-pattern [ blind ]

#### Example:

```
Router(config-telephony)# transfer-pattern .T
```

Allows
                                             				transfer of telephone calls by Cisco Unified IP phones to specified phone
                                             				number patterns. If no transfer pattern is set, the default is that transfers
                                             				are permitted only to other local IP phones.

transfer-pattern —String of digits for permitted call
                                                   					 transfers. Wildcards are allowed. A pattern of .T transfers all calling parties
                                                   					 using the H.450.2 standard.

blind —(Optional) When
                                                   					 H.450.2 consultative call transfer is configured, forces transfers that match
                                                   					 the pattern specified in this command to be executed as blind transfers.
                                                   					 Overrides settings made using the transfer-system and transfer-mode commands.

Step 6

call-forward
                                                				  pattern pattern

#### Example:

```
Router(config-telephony)# call-forward pattern .T
```

Specifies
                                             				the H.450.3 standard for call forwarding.

pattern —Digits to match for call forwarding using
                                                   					 the H.450.3 standard. If an incoming calling-party number matches the pattern,
                                                   					 it can be forwarded using the H.450.3 standard. A pattern of .T forwards all
                                                   					 calling parties using the H.450.3 standard.

Calling-party numbers that do not match the patterns defined
                                             				with this command are forwarded using Cisco proprietary call forwarding for
                                             				backward compatibility.

Step 7

timeouts
                                                				  transfer-recall seconds

#### Example:

```
Router(config-telephony)# timeouts transfer-recall 30
```

(Optional)
                                             				Enables Cisco Unified CME to recall a transferred call if the transfer-to party
                                             				is busy or does not answer.

seconds —Duration, in seconds, to wait before
                                                   					 recalling a transferred call. Range: 1 to 1800. Default: 0 (disabled).

This command
                                             				is supported in Cisco Unified CME 4.3 and later versions.

This command
                                             				can also be configured in ephone-dn and ephone-dn-template configuration mode.

Step 8

transfer-digit-collect { new-call | orig-call }

#### Example:

```
Router(config-telephony)# transfer-digit-collect orig-call
```

(Optional)
                                             				Selects the digit-collection method used for consultative call transfers.

- new-call —Digits are collected from the new call
                                                				  leg. Default value in Cisco Unified CME 4.3 and later versions.

orig-call —Digits are collected from original
                                                   					 call-leg. Default behavior in versions earlier than Cisco Unified CME 4.3.

This command
                                             				is supported in Cisco Unified CME 4.3 and later versions.

Step 9

exit

#### Example:

```
Router(config-telephony)# exit
```

Exits
                                             				telephony-service configuration mode.

Step 10

voice service
                                                				  voip

#### Example:

```
Router(config)# voice service voip
```

(Optional)
                                             				Enters voice-service configuration mode to establish global call transfer and
                                             				forwarding parameters.

Step 11

supplementary-service
                                                				  h450.2

#### Example:

```
Router(conf-voi-serv)# supplementary-service h450.2
```

(Optional)
                                             				Enables H.450.2 supplementary services capabilities globally.

Default is
                                             				enabled. Use the no form of this command to disable H.450.2 capabilities globally. You can also use
                                             				this command in dial-peer configuration mode to enable H.450.2 services for a
                                             				single dial peer.

Step 12

supplementary-service
                                                				  h450.3

#### Example:

```
Router(conf-voi-serv)# supplementary-service h450.3
```

(Optional)
                                             				Enables H.450.3 supplementary services capabilities globally.

Default is
                                             				enabled. Use the no form of this command to disable H.450.3 capabilities globally. You can also use
                                             				this command in dial-peer configuration mode to enable H.450.3 services for a
                                             				single dial peer.

Step 13

exit

#### Example:

```
Router(conf-voi-serv)# exit
```

(Optional)
                                             				Exits voice-service configuration mode.

Step 14

dial-peer voice tag voip

#### Example:

```
Router(config)# dial-peer voice 1 voip
```

(Optional)
                                             				Enters dial-peer configuration mode.

Step 15

supplementary-service
                                                				  h450.2

#### Example:

```
Router(config-dial-peer)# no supplementary-service h450.2
```

(Optional)
                                             				Enables H.450.2 supplementary services capabilities for an individual dial
                                             				peer.

Default is
                                             				enabled. You can also use this command in voice-service configuration mode to
                                             				enable H.450.2 services globally.

If this
                                                   					 command is enabled globally and enabled on a dial peer, the functionality is
                                                   					 enabled for the dial peer. This is the default.

If this
                                                   					 command is enabled globally and disabled on a dial peer, the functionality is
                                                   					 disabled for the dial peer.

If this
                                                   					 command is disabled globally and either enabled or disabled on a dial peer, the
                                                   					 functionality is disabled for the dial peer.

Step 16

supplementary-service
                                                				  h450.3

#### Example:

```
Router(config-dial-peer)# no supplementary-service h450.3
```

(Optional)
                                             				Enables H.450.3 supplementary services capabilities exchange for an individual
                                             				dial peer.

Default is
                                             				enabled. You can also use this command in voice-service configuration mode to
                                             				enable H.450.3 services globally.

If this
                                                   					 command is enabled globally and enabled on a dial peer, the functionality is
                                                   					 enabled for the dial peer. This is the default configuration.

If this
                                                   					 command is enabled globally and disabled on a dial peer, the functionality is
                                                   					 disabled for the dial peer.

If this
                                                   					 command is disabled globally and either enabled or disabled on a dial peer, the
                                                   					 functionality is disabled for the dial peer.

Step 17

end

#### Example:

```
Router(config-dial-peer)# end
```

Returns to
                                             				privileged EXEC mode.

### Enable
                           	 Call-Transfer Recall on SIP Phones at System-Level

To enable
                                 		  call-transfer recalls to be initiated from a Cisco Unified CME system, perform
                                 		  the following steps.

Transferor
                                                   				  and transfer-to party must be on the same Cisco Unified CME router; transferee
                                                   				  party can be remote to the Cisco Unified CME router.

Transfer
                                                   				  recall is not supported if the transfer-to party has Call Forward Busy enabled,
                                                   				  or if the transfer-to party is a hunt group pilot number.

#### Before you begin

Cisco Unified CME
                                 		  11.6 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- timeouts transfer-recall seconds

- exit

- voice service voip

- no supplementary-service sip refer

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

- Enter your password if
                                                				  prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice register global

#### Example:

```
Router(config)# voice register global
```

Enters voice
                                             				register global configuration mode to set parameters for all supported SIP
                                             				phones in Cisco Unified CME.

Step 4

timeouts transfer-recall seconds

#### Example:

```
Router(config-register-global)# timeouts transfer-recall 30
```

```
Router(config-register-dn)# timeouts transfer-recall 30
```

Enables
                                             				Cisco Unified CME to recall a transferred call if the transfer-to party is busy
                                             				or does not answer in the voice register global configuration mode. You can
                                             				also recall a transferred call in the voice register dn configuration mode.

seconds —Duration, in seconds, to wait before
                                                   					 recalling a transferred call. Range: 1 to 1800. Default: 0 (disabled).

This
                                                   					 command is supported in Cisco Unified CME 11.6 and later versions.

This
                                                   					 command can also be configured in voice register dn or voice register global
                                                   					 configuration modes.

Step 5

exit

#### Example:

```
Router(config-register-global)# exit
```

Exits voice
                                             				register global configuration mode.

Step 6

voice service voip

#### Example:

```
Router(config)# voice service voip
```

(Optional)
                                             				Enters voice-service configuration mode.

Step 7

no supplementary-service sip refer

#### Example:

```
Router(config-voi-serv)# no supplementary-service sip refer
```

Prevents the
                                             				router from forwarding a REFER message to the destination for call-transfer
                                             				recalls.

Step 8

end

#### Example:

```
Router(config-voi-serv)# end
```

Returns to
                                             				privileged EXEC mode.

### Enable Call
                           	 Forwarding for a Directory Number

To define the
                                 		  conditions and target numbers for call forwarding for individual ephone-dns,
                                 		  and set other restrictions for call forwarding, perform the following steps.

Restriction

- Call forwarding is invoked only if that phone is dialed directly. Call forwarding is not invoked when the phone number is
                                                called through a sequential, longest-idle, or peer hunt group.

- If call forwarding is configured for hunt group member, call forward is ignored by the hunt group.

- Calls from an internal extension to an extension which is busy, is forwarded to the SNR destination even if no forward local-calls
                                                is configured under the Directory Number.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- call-forward pattern pattern

- exit

- ephone-dn dn-tag [ dual-line ]

- number number [ secondary number ] [ no-reg [ both | primary ] ]

- call-forward all target-number

- call-forward
                                       				  busy target-number [ primary | secondary ] [ dialplan-pattern ]

- call-forward
                                       				  noan target-number timeout seconds [ primary | secondary ] [ dialplan-pattern ]

- call-forward night-service target-number

- call-forward
                                       				  max-length length

- no forward
                                       				  local-calls

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
Router(config)#
```

Enters
                                             				telephony-service configuration mode.

Step 4

call-forward pattern pattern

#### Example:

```
Router(config-telephony)# call-forward pattern .T
```

Specifies the
                                             				H.450.3 standard for call forwarding. Calling-party numbers that do not match
                                             				the patterns defined with this command are forwarded using Cisco-proprietary
                                             				call forwarding for backward compatibility.

- pattern —Digits to match
                                                				  for call forwarding using the H.450.3 standard. If an incoming calling-party
                                                				  number matches the pattern, it is forwarded using the H.450.3 standard. A
                                                				  pattern of .T forwards all calling parties using the H.450.3 standard.

Step 5

exit

#### Example:

```
Router(config-telephony)# exit
```

Exits
                                             				telephony-service configuration mode.

Step 6

ephone-dn dn-tag [ dual-line ]

#### Example:

```
Router(config)# ephone-dn 20
```

Enters
                                             				ephone-dn configuration mode, creates an ephone-dn, and optionally assigns it
                                             				dual-line status.

- dual-line —(Optional)
                                                				  Enables an ephone-dn with one voice port and two voice channels, which supports
                                                				  features such as call waiting, call transfer, and conferencing with a single
                                                				  ephone-dn.

Step 7

number number [ secondary number ] [ no-reg [ both | primary ] ]

#### Example:

```
Router(config-ephone-dn)# number 2777 secondary 2778
```

Configures a
                                             				valid extension number for this ephone-dn instance.

Step 8

call-forward all target-number

#### Example:

```
Router(config-ephone-dn)# call-forward all 2411
```

Forwards all
                                             				calls for this extension to the specified number.

- target-number —Phone
                                                				  number to which calls are forwarded.

Step 9

call-forward
                                                				  busy target-number [ primary | secondary ] [ dialplan-pattern ]

#### Example:

```
Router(config-ephone-dn)# call-forward busy 2513
```

Forwards
                                             				calls for a busy extension to the specified number.

Step 10

call-forward
                                                				  noan target-number timeout seconds [ primary | secondary ] [ dialplan-pattern ]

#### Example:

```
Router(config-ephone-dn)# call-forward noan 2513 timeout 45
```

Forwards
                                             				calls for an extension that does not answer.

Step 11

call-forward night-service target-number

#### Example:

```
Router(config-ephone-dn)# call-forward night-service 2879
```

Automatically forwards incoming calls to the specified number
                                             				when night service is active.

- target-number —Phone
                                                				  number to which calls are forwarded.

Step 12

call-forward
                                                				  max-length length

#### Example:

```
Router(config-ephone-dn)# call-forward max-length 5
```

(Optional)
                                             				Limits the number of digits that can be entered for a target number when using
                                             				the CfwdAll soft key on an IP phone.

- length —Number of
                                                				  digits that can be entered using the CfwdAll soft key on an IP phone.

Step 13

no forward
                                                				  local-calls

#### Example:

```
Router(config-ephone-dn)# no forward local-calls
```

(Optional)
                                             				Specifies that local calls (calls from ephone-dns on the same Cisco Unified CME
                                             				system) will not be forwarded from this extension.

If this
                                                   					 extension is busy, an internal caller hears a busy signal.

If this
                                                   					 extension does not answer, the internal caller hears ringback.

Step 14

end

#### Example:

```
Router(config-ephone-dn)# end
```

Returns to
                                             				privileged EXEC mode.

### Call Transfer for
                           	 a Directory Number

To enable call
                                 		  transfer for a specific directory number, perform the following steps. This
                                 		  procedure overrides the global setting for blind or consultative transfer for
                                 		  individual directory numbers.

#### Before you begin

Call transfer must
                                 		  be enabled globally. See Enable Call Transfer and Forwarding on SCCP Phones at System-Level .

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn dn-tag [ dual-line ]

- transfer-mode { blind | consult }

- timeouts transfer-recall seconds

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

- Enter your password if
                                                				  prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ephone-dn dn-tag [ dual-line ]

#### Example:

```
Router(config)# ephone-dn 20
```

Enters
                                             				ephone-dn configuration mode, creates an ephone-dn, and optionally assigns it
                                             				dual-line status.

- dual-line —(Optional)
                                                				  Enables an ephone-dn with one voice port and two voice channels, which supports
                                                				  features such as call waiting, call transfer, and conferencing with a single
                                                				  ephone-dn.

Step 4

transfer-mode { blind | consult }

#### Example:

```
Router(config-ephone-dn)# transfer-mode blind
```

Specifies the type of call transfer for an individual directory number using the H.450.2 standard, allowing you to override
                                             the global setting.

- Default: system-level value set with the transfer-system command.

Step 5

timeouts transfer-recall seconds

#### Example:

```
Router(config-ephone-dn)# timeouts transfer-recall 30
```

(Optional)
                                             				Enables call-transfer recall and sets the number of seconds that
                                             				Cisco Unified CME waits before recalling a transferred call if the transfer-to
                                             				party does not answer or is busy.

seconds —Duration, in seconds, to wait before
                                                   					 recalling a transferred call. Range: 1 to 1800. Default: 0 (disabled).

This
                                                   					 command is supported in Cisco Unified CME 4.3 and later versions.

This
                                                   					 command can also be configured in ephone-dn-template and telephony-service
                                                   					 configuration mode.

Step 6

end

#### Example:

```
Router(config-ephone-dn)# end
```

Returns to
                                             				privileged EXEC mode.

### Configure Call
                           	 Transfer Options for SCCP Phones

To specify a
                                 		  maximum number of digits for transfer destinations or block transfers to
                                 		  external destinations by individual phones, perform the following steps.

#### Before you begin

Transfers made
                                       				to speed-dial numbers are not blocked when the transfer-pattern blocked command is used.

Transfers made
                                       				using speed-dial are not blocked by the after-hours
                                          				  block pattern command.

### SUMMARY STEPS

- enable

- configure terminal

- ephone-template template-tag

- transfer-pattern blocked

- transfer max-length digit-length

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

ephone-template template-tag

#### Example:

```
Router(config)# ephone-template 1
```

Enters
                                             				ephone-template configuration mode.

template-tag —Unique number that identifies this template
                                                   					 during configuration tasks. Range: 1 to 20.

Step 4

transfer-pattern blocked

#### Example:

```
Router(config-ephone-template)# transfer-pattern blocked
```

(Optional)
                                             				Prevents directory numbers on the phone to which this template is applied from
                                             				transferring calls to patterns specified in the transfer-pattern (telephony-service) command.

Step 5

transfer max-length digit-length

#### Example:

```
Router(config-ephone-template)# transfer max-length 8
```

(Optional)
                                             				Specifies the maximum number of digits the user can dial when transferring a
                                             				call.

digit-length —Number of digits allowed in a number to which a
                                                   					 call is being transferred. Range: 3 to 16. Default: 16.

Step 6

exit

#### Example:

```
Router(config-ephone-template)# exit
```

Exits
                                             				ephone-template configuration mode.

Step 7

ephone phone-tag

#### Example:

```
Router(config)# ephone 25
```

Enters ephone
                                             				configuration mode.

Step 8

ephone-template template-tag

#### Example:

```
Router(config-ephone)# ephone-template 1
```

Applies a
                                             				template to a phone.

template-tag —Template number that you want to apply to this
                                                   					 phone.

Step 9

restart

#### Example:

```
Router(config-ephone)# restart
```

Performs a
                                             				fast reboot of this phone without contacting the DHCP server for updated
                                             				information.

Repeat Step 6
                                             				to Step 9 for each phone on which you want to limit transfer capabilities.

Step 10

end

#### Example:

```
Router(config-ephone)# end
```

Exits to
                                             				privileged EXEC mode.

### Verify Call
                           	 Transfer for SCCP Phones

Step 1

Use the show
                                                				  running-config command to verify your configuration. Transfer
                                          			 method and patterns are listed in the telephony-service portion of the output.
                                          			 You can also use the show
                                                				  telephony-service command to display this information.

#### Example:

```
Router# show running-config !
telephony-service
fxo hook-flash
load 7910 P00403020214
load 7960-7940 P00305000600
load 7914 S00103020002
load 7905 CP7905040000SCCP040701A
max-ephones 100
max-dn 500
ip source-address 10.115.33.177 port 2000
max-redirect 20
no service directed-pickup
timeouts ringing 10
voicemail 7189
max-conferences 8 gain -6
moh music-on-hold.au
web admin system name cisco password cisco
dn-webedit
time-webedit
transfer-system full-consult
transfer-pattern 92......
transfer-pattern 91..........
transfer-pattern 93......
transfer-pattern 94......
transfer-pattern 95......
transfer-pattern 96......
transfer-pattern 97......
transfer-pattern 98......
transfer-pattern 99......
transfer-pattern .T
secondary-dialtone 9
!
create cnf-files version-stamp 7960 Jul 13 2004 03:39:28
```

Step 2

If you have
                                          			 used the transfer-mode command to override the global transfer mode for an
                                          			 individual ephone-dn, use the show
                                                				  running-config or show telephony-service
                                                				  ephone-dn command to verify that setting.

#### Example:

```
Router# show running-config !
ephone-dn 40 dual-line
number 451
description Main Number
huntstop channel
no huntstop
transfer-mode blind
```

Step 3

Use the show telephony-service
                                                				  ephone-template command to view ephone-template configurations.

### Specify Transfer Patterns for Trunk-to-Trunk Calls and Conferences for
                           	 SIP

Restriction

Call transfer and conference restrictions apply when transfers or
                                             			 conferences are initiated toward external parties, like a PSTN trunk, a SIP
                                             			 trunk, or an H.323 trunk. The restrictions do not apply to transfers to local
                                             			 extensions.

#### Before you begin

Cisco Unified CME 9.5 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- transfer-pattern transfer-pattern

- exit

- Enter one of the following commands:

- voice register pool pool-tag

- voice register template template-tag

- ephone phone tag

- ephone-template template-tag

- transfer max-length max-length

- exit

- telephony-service

- conference transfer-pattern

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

- Enter your password if
                                                				  prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters telephony-service configuration mode for configuring Cisco
                                             				Unified CME.

Step 4

transfer-pattern transfer-pattern

#### Example:

```
Router(config-telephony)# transfer-pattern 1234... Router(config-telephony)# transfer-pattern 2468..
```

Allows the transfer of calls from Cisco IP phones to specified
                                             				directory numbers of phones other than Cisco IP phones.

transfer-pattern —String of digits
                                                   					 for permitted call transfers. Wildcards are allowed. A maximum of 32 transfer
                                                   					 patterns can be entered, using a separate command for each one.

Step 5

exit

#### Example:

```
Router(config-telephony)# exit
```

Exits telephony-service configuration mode and enters global
                                             				configuration mode.

Step 6

Enter one of the following commands:

- voice register pool pool-tag

- voice register template template-tag

- ephone phone tag

- ephone-template template-tag

#### Example:

```
Router(config)# voice register pool 25
```

Enters voice register pool configuration mode and creates a pool configuration for a Cisco Unified SIP IP phone in Cisco Unified
                                             CME or for a set of Cisco Unified SIP IP phones in Cisco Unified SIP SRST.

- pool-tag —Unique number assigned to the pool. Range is 1 to 100.

or

Enters voice register template configuration mode and defines a template of common parameters for Cisco Unified SIP IP phones.

- template-tag —Declares a template tag. Range is 1 to 10.

or

Enters ephone configuration mode.

- phone-tag—Unique sequence number that identifies this ephone during configuration tasks. The maximum number of ephones is
                                                version and platform-specific. Type ? to display range.

Step 7

transfer max-length max-length

#### Example:

```
Router(config-register-pool)# transfer max-length 7
```

(Optional) Specifies the maximum length of the transfer number.

- max-length —Maximum length of the
                                                				  transfer number. Range is 3 to 16.

Step 8

exit

#### Example:

```
Router(config-register-pool)# exit
```

Enters global configuration mode.

Step 9

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters telephony-service configuration mode for configuring Cisco
                                             				Unified CME.

Step 10

conference transfer-pattern

#### Example:

```
Router(config-telephony)# conference transfer-pattern
```

Enables a Cisco Unified CME system to apply transfer patterns to a
                                             				conference call using conference softkeys or feature buttons.

Step 11

end

#### Example:

```
Router(config-telephony)# end
```

Exits telephony-service configuration mode and enters privileged
                                             				EXEC mode.

### Conference
                           	 Max-Length

Conference calls are allowed when:

both conference transfer-pattern and transfer-pattern commands are configured

dialed digits match the configured transfer pattern

When conference
                              		max-length command is configured, the Cisco Unified CME will allow the
                              		conferences only if the dialed digits are within the max-length limit.

If configured, the
                              		conference max-length command does not impact call transfers.

### Block
                           	 Trunk-to-Trunk Call Transfers for SIP

To block call
                                 		  transfers to external destinations, perform the following steps.

Restriction

Call transfer
                                             			 restrictions apply when transfers are initiated toward external parties, like a
                                             			 PSTN trunk, a SIP trunk, or an H.323 trunk. The restrictions do not apply to
                                             			 transfers to local extensions.

#### Before you begin

Cisco Unified CME
                                 		  9.5 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- Enter one of the following commands:

- voice register pool pool-tag

- voice register template template-tag

- transfer-pattern blocked

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

- Enter your password if
                                                				  prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

Enter one of the following commands:

- voice register pool pool-tag

- voice register template template-tag

#### Example:

```
Router(config)# voice register template 5
```

Enters voice register pool configuration mode and creates a pool configuration for a Cisco Unified SIP IP phone in Cisco Unified
                                             CME or for a set of Cisco Unified SIP IP phones in Cisco Unified SIP SRST.

pool-tag —Unique number assigned to the pool. Range is 1 to 100.

Enters voice register template configuration mode and defines a template of common parameters for Cisco Unified SIP IP phones.

template-tag —Declares a template tag. Range is 1 to 10.

Step 4

transfer-pattern blocked

#### Example:

```
Router(config-register-temp)# transfer-pattern blocked
```

Blocks all
                                             				call transfers for a specific Cisco Unified SIP IP phone or a set of Cisco
                                             				Unified SIP IP phone.

Step 5

end

#### Example:

```
Router(config-register-temp)# end
```

Exits voice
                                             				register template configuration mode and enters privileged EXEC mode.

### Enable H.450.12 Capabilities

To enable H.450.12 capabilities globally or by individual dial peer
                                 		  when not all gateway endpoints in your network support H.450.2 and H.450.3
                                 		  standards, perform the following steps. H.450.12 capabilities are disabled by
                                 		  default to minimize the risk of compatibility issues with other types of H.323
                                 		  systems. Settings for individual dial peers override the global setting.

Restriction

Cisco CME 3.0 and earlier versions do not support H.450.12.

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- supplementary-service h450.12 [ advertise-only ]

- exit

- dial-peer voice tag voip

- supplementary-service h450.12

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

- Enter your password if
                                                				  prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

voice service voip

#### Example:

```
Router(config)# voice service voip
```

(Optional) Enters voice service configuration mode to establish
                                             				global call transfer and forwarding parameters.

Step 4

supplementary-service h450.12 [ advertise-only ]

#### Example:

```
Router(conf-voi-serv)# supplementary-service h450.12
```

(Optional) Enables H.450.12 supplementary services capabilities
                                             				globally for VoIP endpoints.

This command enables call-by-call detection of H.450
                                                   					 capabilities when some endpoints in your mixed network are H.450-capable and
                                                   					 other endpoints are not. This command is disabled by default.

advertise-only —(Optional) Advertises
                                                   					 H.450 capabilities to the remote end but does not require H.450.12 responses.
                                                   					 Use this keyword on Cisco CME 3.1 or later systems if you have a mixed network
                                                   					 containing Cisco CME 3.0 systems.

This command is also used in dial-peer configuration mode to
                                             				affect an individual dial peer.

Step 5

exit

#### Example:

```
Router(conf-voi-serv)# exit
```

(Optional) Exits voice-service configuration mode.

Step 6

dial-peer voice tag voip

#### Example:

```
Router(config)# dial-peer voice 1 voip
```

(Optional) Enters dial-peer configuration mode.

Step 7

supplementary-service h450.12

#### Example:

```
Router(config-dial-peer)# supplementary-service h450.12
```

(Optional) Enables H.450.12 supplementary services capabilities
                                             				for an individual dial peer. This command is disabled by default.

This command is also used in voice-service configuration mode to
                                             				enable H.450.12 services globally.

If this command is enabled globally and enabled on a dial
                                                   					 peer, the functionality is enabled for the dial peer.

If this command is enabled globally and disabled on a dial
                                                   					 peer, the functionality is enabled for the dial peer.

If this command is disabled globally and enabled on a dial
                                                   					 peer, the functionality is enabled for the dial peer.

If this command is disabled globally and disabled on a dial
                                                   					 peer, the functionality is disabled for the dial peer. This is the default.

Step 8

end

#### Example:

```
Router(config-dial-peer)# end
```

Returns to privileged EXEC mode.

### Enable
                           	 H.323-to-H.323 Connection Capabilities

Vo IP-to-VoIP c
                                 		  onnections permit the termination and reorigination of transferred and
                                 		  forwarded calls over the VoIP network. VoIP-to-VoIP connections are used for
                                 		  hairpin call routing and for H.450 tandem gateways. The only type of
                                 		  VoIP-to-VoIP connection that is supported by Cisco CME 3.1 or a later version
                                 		  is H.323-to-H.323 connection.

VoIP-to-VoIP
                                 		  connections are disabled on the router by default, and they must be explicitly
                                 		  enabled to make use of hairpin call routing or an H.450 tandem gateway. In
                                 		  addition, you must configure a mechanism to direct transferred or forwarded
                                 		  calls to the hairpin or the H.450 tandem gateway, using one of the following
                                 		  methods:

- Enable H.450.12
                                    			 capabilities globally or on the routes that your transfers and forwards take.
                                    			 See Enable H.450.12 Capabilities .

- Explicitly disable H.450.2
                                    			 and H.450.3 capabilities globally or on the routes that your transfers and
                                    			 forwards take. See Enable Call Transfer and Forwarding on SCCP Phones at System-Level .

Restriction

Codecs on
                                                   				  all the VoIP dial peers of the H.450 tandem gateway must be the same.

Only one
                                                   				  codec type is supported in the VoIP network at a time, and there are only two
                                                   				  codec choices: G.711 (A-law or mu-law) or G.729.

Transcoding
                                                   				  is not supported.

Codec
                                                   				  renegotiation is not supported. For example, if an H.323 call that uses a G.729
                                                   				  codec is received by a Cisco Unified CME system and is forwarded to a
                                                   				  voice-mail system that requires a G.711 codec, the codec cannot be renegotiated
                                                   				  from G.729 to G.711.

H.323-to-SIP
                                                   				  hairpin call routing is supported only with Cisco Unity Express. For more
                                                   				  information, see Integrating Cisco CallManager Express with
                                                      					 Cisco Unity Express .

Cisco Unified Communications Manager must use a media
                                                   				  termination point (MTP), intercluster trunk (ICT) mode, and slow start.

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- allow-connections h323 to h323

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

- Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice service voip

#### Example:

```
Router(config)# voice service voip
```

Enters voice
                                             				service configuration mode to establish global call transfer and forwarding
                                             				parameters.

Step 4

allow-connections h323 to h323

#### Example:

```
Router(conf-voi-serv)# allow-connections h323 to h323
```

Enables
                                             				VoIP-to-VoIP call connections. Use the no form
                                             				of the command to disable VoIP-to-VoIP connections; this is the default.

Step 5

end

#### Example:

```
Router(config-voi-serv)# end
```

Returns to
                                             				privileged EXEC mode.

### Forward Calls
                           	 Using Local Hairpin Routing

When
                                 		  Cisco Unified CME is used to forward calls that originate on phones that do not
                                 		  support the H.450.3 standard such as Cisco Unified Communications Manager
                                 		  phones, local hairpin routing must be used to forward the calls. For calling
                                 		  parties whose numbers match the pattern specified, the system automatically
                                 		  detects whether H.450.3 is supported and uses the appropriate method to forward
                                 		  calls.

To enable hairpin
                                 		  routing, you must denote the originating and terminating legs of the hairpin.
                                 		  To forward calls to Cisco Unity Express, connections must be allowed to a SIP
                                 		  trunk.

Optionally, you
                                 		  can disable the use of H.450.3 but this is not required because the system
                                 		  automatically detects calls on which H.450.3 is not supported and local hairpin
                                 		  routing is required when the calling-party numbers match the pattern specified.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- call-forward pattern pattern

- calling-number local

- exit

- voice service voip

- allow connections from-type to to-type

- supplementary-service h450.3

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
                                             				telephony-service configuration mode.

Step 4

call-forward pattern pattern

#### Example:

```
Router(config-telephony)# call-forward pattern 6000
```

Specifies the
                                             				calling-party numbers for which to allow call forwarding with automatic
                                             				detection of whether H.450.3 is supported. If H.450.3 is supported, H.450.3 is
                                             				used for the forward and, if not, local hairpin is used.

pattern —Digits to match for call forwarding. A pattern of .T
                                                   					 forwards all calling parties.

Step 5

calling-number local

#### Example:

```
Router(config-telephony)# calling-number local
```

(Optional)
                                             				Replaces a calling-party number and name with the forwarding-party (local)
                                             				number and name for hairpin-forwarded calls only.

- Before
                                                				  Cisco CME 3.3, this command must be used with Tool Command Language (Tcl)
                                                				  script app-h450-transfer.2.0.0.7 or a later version. The local-hairpin
                                                				  attribute-value (AV) pair must be set to 1.

Step 6

exit

#### Example:

```
Router(config-telephony)# exit
```

Exits
                                             				telephony-service configuration mode.

Step 7

voice service voip

#### Example:

```
Router(config)# voice service voip
```

Enters
                                             				voice-service configuration mode.

Step 8

allow connections from-type to to-type

#### Example:

```
Router(conf-voi-serv)# allow connections h323 to sip
```

Allows
                                             				connections between specific types of endpoints in a network.

from-type —Originating endpoint type. Valid choices
                                                   					 are h323 and sip .

to-type —Terminating endpoint type. Valid choices
                                                   					 are h323 and sip .

Step 9

supplementary-service h450.3

#### Example:

```
Router(conf-voi-serv)# no supplementary-service h450.3
```

(Optional)
                                             				Enables H.450.3 supplementary services capabilities exchange globally. This is
                                             				the default. Use the no form
                                             				of this command to disable H.450.3 capabilities globally. This command can also
                                             				be used in dial-peer configuration mode to disable H.450.3 functionality for a
                                             				single dial peer.

Step 10

end

#### Example:

```
Router(config-voi-serv)# end
```

Exits to
                                             				privileged EXEC mode.

### Enable H.450.7 and
                           	 QSIG Supplementary Services at System-Level

To enable H.4350.7
                                 		  capabilities and QSIG supplementary services on all dial peers, perform the
                                 		  following steps.

Restriction

QSIG integration supports SCCP phones only.

QSIG integration is exclusive; once QSIG integration is configured, QSIG transit node capability is disabled. There is no
                                                   dial-peer control to enable either transit or originate/terminate capability on a call by call basis.

If you enable QSIG supplementary services at a system-level, you cannot disable the capability on individual dial peers.

#### Before you begin

Cisco Unified CME
                                 		  4.0 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- supplementary-service h450.7

- qsig decode

- exit

- voice service pots

- supplementary-service qsig call-forward

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

- Enter your
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

voice service voip

#### Example:

```
Router(config)# voice service voip
```

Enters VoIP
                                             				voice-service configuration mode to define global call transfer and forwarding
                                             				parameters.

Step 4

supplementary-service h450.7

#### Example:

```
Router(config-voi-serv)# supplementary-service h450.7
```

Enables
                                             				H.450.7 supplementary services capabilities exchange at a system-level.

Step 5

qsig decode

#### Example:

```
Router(config-voi-serv)# qsig decode
```

Enables
                                             				decoding for QSIG supplementary services.

Step 6

exit

#### Example:

```
Router(config-voi-serv)# exit
```

Exits VoIP
                                             				voice-service configuration mode.

Step 7

voice service pots

#### Example:

```
Router(config)# voice service pots
```

Enters POTS
                                             				voice-service configuration mode to define global call transfer and forwarding
                                             				parameters.

Step 8

supplementary-service qsig call-forward

#### Example:

```
Router(config-voi-serv)# supplementary-service qsig call-forward
```

Enables QSIG
                                             				call-forwarding supplementary services (ISO 13873) to forward calls to another
                                             				number.

Step 9

end

#### Example:

```
Router(config-voi-serv)# end
```

Exits to
                                             				privileged EXEC mode.

### Enable H.450.7 and
                           	 QSIG Supplementary Services on a Dial Peer

To enable H.4350.7
                                 		  capabilities and QSIG supplementary services on an individual dial peer,
                                 		  perform the following steps.

Restriction

QSIG
                                                   				  integration supports SCCP phones only.

QSIG
                                                   				  integration is exclusive; once QSIG integration is configured, QSIG transit
                                                   				  node capability is disabled. There is no dial-peer control to enable either
                                                   				  transit or originate/terminate capability on a call by call basis.

If you
                                                   				  enable QSIG supplementary services at a system-level, you cannot enable or
                                                   				  disable the capability on individual dial peers.

#### Before you begin

Cisco Unified CME
                                 		  4.0 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- qsig decode

- exit

- dial-peer voice tag voip

- supplementary-service h450.7

- exit

- dial-peer voice tag pots

- supplementary-service qsig call-forward

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

- Enter your password if
                                                				  prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice service voip

#### Example:

```
Router(config)# voice service voip
```

Enters VoIP
                                             				voice-service configuration mode to define global call transfer and forwarding
                                             				parameters.

Step 4

qsig decode

#### Example:

```
Router(config-voi-serv)# qsig decode
```

Enables
                                             				decoding for QSIG supplementary services.

Step 5

exit

#### Example:

```
Router(config-voi-serv)# exit
```

Exits VoIP
                                             				voice-service configuration mode.

Step 6

dial-peer voice tag voip

#### Example:

```
Router(config)# dial-peer voice 1 voip
```

Enters
                                             				dial-peer configuration mode to define parameters for an individual dial peer.

Step 7

supplementary-service h450.7

#### Example:

```
Router(config-dial-peer)# supplementary-service h450.7
```

Enables
                                             				H.450.7 supplementary services capabilities exchange on a single dial peer.

Step 8

exit

#### Example:

```
Router(config-dial-peer)# exit
```

Exits
                                             				dial-peer configuration mode.

Step 9

dial-peer voice tag pots

#### Example:

```
Router(config)# dial-peer voice 2 pots
```

Enters
                                             				dial-peer configuration mode to define parameters for an individual dial peer.

Step 10

supplementary-service qsig call-forward

#### Example:

```
Router(config-dial-peer)# supplementary-service qsig call-forward
```

Enables QSIG
                                             				call-forwarding supplementary services (ISO 13873) to forward calls to another
                                             				number.

Step 11

end

#### Example:

```
Router(config-dial-peer)# end
```

Exits to
                                             				privileged EXEC mode.

### Disable SIP
                           	 Supplementary Services for Call Forward and Call Transfer

To disable REFER
                                 		  messages for call transfers or redirect responses for call forwarding from
                                 		  being sent to the destination by Cisco Unified CME, perform the following
                                 		  steps. You can disable these supplementary features if the destination gateway
                                 		  does not support them.

Restriction

In
                                                   				  Cisco Unified CME 4.2 and 4.3, when the supplementary-service sip
                                                         						refer command is enabled (default) and both the caller being
                                                   				  transferred (transferee) and the phone making the transfer (transferor) are
                                                   				  SIP, but the transfer-to phone is SCCP, Cisco Unified CME hairpins the call to
                                                   				  the transfer-to phone after receiving the REFER request from transferor instead
                                                   				  of sending the REFER request to the transferee.

#### Before you begin

Cisco Unified CME
                                 		  4.1 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- Enter one of the following commands:

- voice service voip

- dial-peer voice tag voip

- no supplementary-service sip moved-temporarily

- no supplementary-service sip refer

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

- Enter your password if
                                                				  prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

Enter one of the following commands:

- voice service voip

- dial-peer voice tag voip

#### Example:

```
Router(config)# voice service voip or Router(config)# dial-peer voice 99 voip
```

Enters voice-service configuration mode to set global parameters for VoIP features.

or

Enters dial peer configuration mode to set parameters for a specific dial peer.

Step 4

no supplementary-service sip moved-temporarily

#### Example:

```
Router(conf-voi-serv)# no supplementary-service sip moved-temporarily or Router(config-dial-peer)# no supplementary-service sip moved-temporarily
```

Disables SIP
                                             				redirect response for call forwarding either globally or for a dial peer.

Sending
                                             				redirect message to the destination is the default behavior.

Step 5

no supplementary-service sip refer

#### Example:

```
Router(conf-voi-serv)# no supplementary-service sip refer or Router(config-dial-peer)# no supplementary-service sip refer
```

Disables SIP
                                             				REFER message for call transfers either globally or for a dial peer.

Sending REFER
                                             				message to the destination is the default behavior.

Step 6

end

#### Example:

```
Router(config-voi-serv)# end or Router(config-dial-peer)# end
```

Exits to
                                             				privileged EXEC mode.

### Enable Interworking with Cisco Unified Communications Manager

If Cisco CME 3.1 or
                              		later and Cisco Unified Communications Manager are used in the same network,
                              		some additional configuration is necessary, as described in the following
                              		sections:

Configure Cisco CME 3.1 or Later to Interwork with Cisco Unified Communications Manager

Enable Cisco Unified Communications Manager to Interwork with Cisco Unified CME

Troubleshooting Call Transfer and Forward Configuration

Network with
                                 		  Cisco Unified CME and Cisco Unified Communications Manager shows a network containing Cisco Unified CME and Cisco Unified Communications
                              		Manager systems.

Prerequisites

Cisco Unified CME must be configured to forward calls using local hairpin routing. For configuration information, see Forward Calls Using Local Hairpin Routing .

#### Configure
                              	 Cisco CME 3.1 or Later to Interwork with Cisco Unified Communications
                              	 Manager

All of the
                                    		  commands in this section are optional because they are set by default to work
                                    		  with Cisco Unified Communications Manager. They are included here only to
                                    		  explain how to implement optional capabilities or return non default settings
                                    		  to their defaults.

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- h323

- telephony-service ccm-compatible

- h225 h245-address on-connect

- exit

- supplementary-service h225-notify cid-update

- exit

- voice class h323 tag

- telephony-service
                                          				  ccm-compatible

- h225 h245-address
                                          				  on-connect

- exit

- dial-peer
                                          				  voice tag voip

- supplementary-service
                                          				  h225-notify cid-update

- voice-class
                                          				  h323 tag

- end

### DETAILED STEPS

Step 1

enable

##### Example:

```
Router> enable
```

Enables
                                                				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

##### Example:

```
Router# configure terminal
```

Enters global
                                                				configuration mode.

Step 3

voice service voip

##### Example:

```
Router(config)# voice service voip
```

Enters
                                                				voice-service configuration mode to establish global parameters.

Step 4

h323

##### Example:

```
Router(conf-voi-serv)# h323
```

Enters H.323
                                                				voice-service configuration mode.

Step 5

telephony-service ccm-compatible

##### Example:

```
Router(conf-serv-h323)# telephony-service ccm-compatible
```

(Optional)
                                                				Globally enables a Cisco CME 3.1 or later system to detect
                                                				Cisco Unified Communications Manager and exchange calls with it. This is the
                                                				default configuration.

Use the no form of this command to disable Cisco Unified Communications Manager detection
                                                      					 and exchange. We do not recommend using the no form of the command.

Using this
                                                      					 command in an H.323 voice class definition allows you to specify this behavior
                                                      					 for an individual dial peer.

Step 6

h225 h245-address on-connect

##### Example:

```
Router(conf-serv-h323)# h225 h245-address on-connect
```

(Optional)
                                                				Globally enables a delay for the H.225 message exchange of an H.245 transport
                                                				address until a call is connected. The delay allows
                                                				Cisco Unified Communications Manager to generate local ringback for calls to
                                                				Cisco Unified CME phones. This is the default configuration.

The no form of this command disables the delay. We do not recommend using the no form of the command.

Using this
                                                      					 command in an H.323 voice class definition allows you to specify this behavior
                                                      					 for an individual dial peer.

Step 7

exit

##### Example:

```
Router(conf-serv-h323)# exit
```

Exits H.323
                                                				voice-service configuration mode.

Step 8

supplementary-service h225-notify cid-update

##### Example:

```
Router(conf-voi-serv)# supplementary-service h225-notify cid-update
```

(Optional)
                                                				Globally enables H.225 messages with caller-ID updates to be sent to
                                                				Cisco Unified Communications Manager. This is the default configuration.

The no form of the command disables caller-ID update. We do not recommend using the no form of the command.

This command
                                                				is also used in dial-peer configuration mode to affect a single dial peer.

If this
                                                      					 command is enabled globally and enabled on a dial peer, the functionality is
                                                      					 enabled for that dial peer. This is the default.

If this
                                                      					 command is enabled globally and disabled on a dial peer, the functionality is
                                                      					 disabled for that dial peer.

If this
                                                      					 command is disabled globally and either enabled or disabled on a dial peer, the
                                                      					 functionality is disabled for that dial peer.

Step 9

exit

##### Example:

```
Router(config-voice-service)# exit
```

Exits
                                                				voice-service configuration mode.

Step 10

voice class h323 tag

##### Example:

```
Router(config)# voice class h323 48
```

(Optional)
                                                				Creates a voice class that contains commands to be applied to one or more dial
                                                				peers.

Step 11

telephony-service
                                                   				  ccm-compatible

##### Example:

```
Router(config-voice-class)# telephony-service ccm-compatible
```

(Optional)
                                                				Enables the dial peer to exchange calls with a
                                                				Cisco Unified Communications Manager system when this voice class is applied to
                                                				a dial peer. This is the default configuration.

The no form of the command disables call exchange with
                                                      					 Cisco Unified Communications Manager. We do not recommend using the no form of the command.

Step 12

h225 h245-address
                                                   				  on-connect

##### Example:

```
Router(config-voice-class)# h225 h245-address on-connect
```

(Optional)
                                                				Enables the calls that use this dial peer to delay the exchange of H.225
                                                				messages that contain the H.245 transport address until calls are connected,
                                                				when this voice class is applied to a dial peer. The delay allows the playing
                                                				of local ringback for calls from Cisco Unified Communications Manager. This is
                                                				the default configuration.

The no form of this command disables the delay. We do not recommend using the no form of the command.

Step 13

exit

##### Example:

```
Router(config-voice-class)# exit
```

Exits
                                                				voice-class configuration mode.

Step 14

dial-peer
                                                   				  voice tag voip

##### Example:

```
Router(config)# dial-peer voice 28 voip
```

(Optional)
                                                				Enters dial-peer configuration mode to set parameters for an individual dial
                                                				peer.

Step 15

supplementary-service
                                                   				  h225-notify cid-update

##### Example:

```
Router(config-dial-peer)# no supplementary-service h225-notify cid-update
```

(Optional)
                                                				Enables H.225 messages with caller-ID updates to
                                                				Cisco Unified Communications Manager for a specific dial peer. This is the
                                                				default configuration.

The no form of the command disables caller-ID updates. We do not recommend using the no form of the command.

Step 16

voice-class
                                                   				  h323 tag

##### Example:

```
Router(config-dial-peer)# voice-class h323 48
```

(Optional)
                                                				Applies the previously defined voice class with the specified tag number to
                                                				this dial peer.

Step 17

end

##### Example:

```
Router(config-dial-peer)# end
```

Exits to
                                                				privileged EXEC mode.

##### What to do next

Set up Cisco Unified Communications Manager using the configuration
                                    		  procedure in the Enable Cisco Unified Communications Manager to Interwork with Cisco Unified CME .

#### Enable
                              	 Cisco Unified Communications Manager to Interwork with
                              	 Cisco Unified CME

To enable
                                    		  Cisco Unified Communications Manager to interwork with Cisco CME 3.1 or a later
                                    		  version, perform the following steps in addition to the normal
                                    		  Cisco Unified Communications Manager configuration.

Step 1

Set
                                             			 Cisco Unified Communications Manager service parameters. From
                                             			 Cisco Unified Communications Manager Administration, choose Service Parameters.
                                             			 Choose the Cisco Unified Communications Manager service, and make the following
                                             			 settings:

Set the
                                                      					 H323 FastStart Inbound service parameter to False.

Set the
                                                      					 Send H225 User Info Message service parameter to H225 Info for Ring Back.

Step 2

Configure
                                             			 Cisco Unified CME as an ICT in the Cisco Unified Communications Manager
                                             			 network. For information about different intercluster trunk types and
                                             			 configuration instructions, see Cisco Unified Communications Manager
                                                				documentation .

Step 3

Ensure that
                                             			 the Cisco Unified Communications Manager network uses an MTP. The MTP is
                                             			 required to provide DSP resources for transcoding and for sending and receiving
                                             			 G.729 calls to Cisco Unified CME. All media streams between
                                             			 Cisco Unified Communications Manager and Cisco Unified CME must pass through
                                             			 the MTP because Cisco CME  3.1 does not support transcoding. For more
                                             			 information, see Cisco Unified Communications Manager
                                                				documentation .

Step 4

Set up dial
                                             			 peers to establish routing using the instructions in the Dial Peer
                                             			 Configuration on Voice Gateway Routers guide.

#### Troubleshooting
                              	 Call Transfer and Forward Configuration

Step 1

If you
                                             			 encounter lack of ringback on direct calls from a
                                             			 Cisco Unified Communications Manager phone to an IP phone on a
                                             			 Cisco Unified CME system, check the show
                                                   				  running-config command output to ensure that the following two
                                             			 commands do not appear: no h225 h245-address
                                                   				  on-connect and no telephony-service
                                                   				  ccm-compatible . These commands should be enabled, which is their
                                             			 default state.

Step 2

Use the debug h225
                                                   				  asn1 command to display the H.323 messages that are sent from the
                                             			 Cisco Unified CME system to the Cisco Unified Communications Manager system to
                                             			 see if the H.245 address is being sent too early.

Step 3

For calls that
                                             			 are routed using VoIP-to-VoIP connections, use the show voip rtp connections
                                                   				  detail command to display the call identification number, IP
                                             			 addresses, and port numbers involved for all VoIP call legs. This command
                                             			 includes VoIP-to-POTS and VoIP-to-VoIP call legs. The following is sample
                                             			 output for this command:

```
Router# show voip rtp connections detail VoIP RTP active connections :
No. CallId  dstCallId  LocalRTP   RmtRTP   LocalIP    			 	RemoteIP
1   7       8          16586      22346   172.27.82.2     172.29.82.2
2   8       7          17010      16590   172.27.82.2     209.165.202.129

Found 2 active RTP connections
```

Step 4

Use the show call prompt-mem-usage
                                                   				  detail command to see information on ringback tone
                                             			 generation that uses the interactive voice response (IVR) prompt playback
                                             			 mechanism. This ringback is needed for hairpin transfers that are committed
                                             			 during the alerting-of-the-transfer-destination phase of the call and for calls
                                             			 to destinations that do not provide in-band ringback tone, such as IP phones
                                             			 (FXS analog ports do provide in-band ringback tone). Ringback tone is played to
                                             			 the transferred party by the Cisco Unified CME system that performs the
                                             			 transfer (the system attached to the transferring party). The system
                                             			 automatically generates tone prompts as needed based on the network-locale
                                             			 setting for the Cisco Unified CME system.

If you are not
                                                				getting ringback tone when you should, use the show call
                                                      					 prompt-mem-usage command to ensure that the correct prompt is
                                                				loaded and playing. The following sample output indicates that a prompt is
                                                				playing (“Number of prompts playing”) and indicates the country code used for
                                                				the prompt (GB for Great Britain) and the codec.

```
Router# show call prompt-mem-usage detail Prompt memory usage:

 config'd   wait  active  free   mc    total    ms      total
file(s) 0200 0001 -001 00200 00001 00002
memory 02097152 00003000 00000000 02094152 00003000
Prompt load counts: (counters reset 0)
success 0(1st try) 0(2nd try), failure 0
Other mem block usage:
mcDynamic mcReader
gauge 00001 00001
Number of prompts playing: 1
Number of start delays : 0
MCs in the ivr MC sharing table
===============================
Media Content: NoPrompt (0x83C64554)
URL:
cid=0, status=MC_READY size=24184 coding=g711ulaw refCount=0
Media Content: tone://GB_g729_tone_ringback (0x83266EC8)
URL: tone://GB_g729_tone_ringback
```

### Configure
                           	 SIP-to-SIP Phone Call Forwarding

To configure
                                 		  SIP-to-SIP call forwarding using a back-to-back user agent (B2BUA) which allows
                                 		  call forwarding on any dial peer, perform the following steps.

Restriction

SIP-to-SIP
                                                   				  call forwarding is invoked only if that phone is dialed directly. Call
                                                   				  forwarding is not invoked when the phone number is called through a sequential,
                                                   				  longest-idle, or peer hunt group.

If call
                                                   				  forwarding is configured for a hunt group member, call forward is ignored by
                                                   				  the hunt group.

In
                                                   				  Cisco Unified CME 4.1 and later versions, Call Forward All requires SIP phones
                                                   				  to be configured with a directory number (using dn keyword in number command); direct line numbers are not supported.

#### Before you begin

Cisco CME 3.4
                                       				or a later version.

Connections
                                       				between specific types of endpoints in a Cisco IP-to-IP gateway must be
                                       				configured by using the allow-connections command. For configuration information, see Enable Calls in Your VoIP Network .

### SUMMARY STEPS

- enable

- configure terminal

- voice register dn dn-tag

- call-forward b2bua all directory-
                                       				  number

- call-forward b2bua busy directory-
                                       				  number

- call-forward b2bua mailbox directory-
                                       				  number

- call-forward b2bua night-service directory- number

- call-forward b2bua noan directory- number timeout seconds

- call-forward b2bua unreachable directory-
                                       				  number

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

- Enter your password if
                                                				  prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice register dn dn-tag

#### Example:

```
Router(config)# voice register dn 1
```

Enters voice
                                             				register dn mode to define a directory number for a SIP phone, intercom line,
                                             				voice port, or an MWI.

Step 4

call-forward b2bua all directory-
                                                				  number

#### Example:

```
Router(config-register-dn)# call-forward b2bua all 5005
```

Enables call
                                             				forwarding for a SIP back-to-back user agent so that all incoming calls will be
                                             				forwarded to the designated directory-number.

In
                                                   					 Cisco CME 3.4 and Cisco Unified CME 4.0, this command is also available in
                                                   					 voice register pool configuration mode. The configuration under voice register
                                                   					 dn takes precedence over the configuration under voice register pool.

If the call-forward b2bua
                                                         						  all command is configured in voice register pool configuration
                                                   					 mode, it applies to all directory numbers on the phone.

Step 5

call-forward b2bua busy directory-
                                                				  number

#### Example:

```
Router(config-register-dn)# call-forward b2bua busy 5006
```

Enables call
                                             				forwarding for a SIP back-to-back user agent so that incoming calls to an
                                             				extension that is busy will be forwarded to the designated directory number.

- In Cisco CME 3.4 and
                                                				  Cisco Unified CME 4.0, this command is also available in voice register pool
                                                				  configuration mode. The configuration under voice register dn takes precedence
                                                				  over the configuration under voice register pool.

Step 6

call-forward b2bua mailbox directory-
                                                				  number

#### Example:

```
Router(config-register-dn)# call-forward b2bua mailbox 5007
```

Enables call
                                             				forwarding for a SIP back-to-back user agent so that incoming calls that have
                                             				been forwarded to a busy or no-answer extension will be forwarded to the
                                             				recipient’s voice mail.

- In Cisco CME 3.4 and
                                                				  Cisco Unified CME 4.0, this command is also available in voice register pool
                                                				  configuration mode. The configuration under voice register dn takes precedence
                                                				  over the configuration under voice register pool.

Step 7

call-forward b2bua night-service directory- number

#### Example:

```
Router(config-register-dn)# call-forward b2bua night-service 5007
```

Enables call forwarding for a SIP back-to-back user agent so that
                                             				incoming calls that have been forwarded to a busy or no-answer extension will
                                             				be forwarded to the recipient’s voice mail.

- In Cisco CME 3.4 and
                                                				  Cisco Unified CME 4.0, this command is also available in voice register pool
                                                				  configuration mode. The configuration under voice register dn takes precedence
                                                				  over the configuration under voice register pool.

Step 8

call-forward b2bua noan directory- number timeout seconds

#### Example:

```
Router(config-register-dn)# call-forward b2bua noan 5010 timeout 10 or
```

```
Router(config-register-pool)# call-forward b2bua noan 5010 timeout 10
```

Enables call
                                             				forwarding for a SIP back-to-back user agent so that incoming calls to an
                                             				extension that does not answer will be forwarded to the designated directory
                                             				number.

In
                                                   					 Cisco CME 3.4 and Cisco Unified CME 4.0, this command is also available in
                                                   					 voice register pool configuration mode. The configuration under voice register
                                                   					 dn takes precedence over the configuration under voice register pool.

timeout seconds —Duration that a call can ring before it is
                                                   					 forwarded to the destination directory number. Range: 3 to 60000. Default: 20.

Step 9

call-forward b2bua unreachable directory-
                                                				  number

#### Example:

```
Router(config-register-dn)# call-forward b2bua unreachable 5009 or Router(config-register-pool)# call-forward b2bua unreachable 5009
```

(Optional)
                                             				Enables call forwarding for a SIP back-to-back user agent so that calls can be
                                             				forwarded to a phone that has not registered in Cisco Unified CME.

Target
                                                   					 directory-number must be configured in Cisco Unified CME.

In
                                                   					 Cisco CME 3.4 and Cisco Unified CME 4.0, this command is also available in
                                                   					 voice register pool configuration mode. The configuration under voice register
                                                   					 dn takes precedence over the configuration under voice register pool.

This
                                                   					 command was removed in Cisco Unified CME 4.1.

Step 10

end

#### Example:

```
Router(config-register-dn)# end
```

Exits to
                                             				privileged EXEC mode.

### Configure Call Forward Unregistered for SIP IP Phones

#### Before you begin

Cisco Unified CME 8.6 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice register dn tag

- call-forward b2bua unregistered directory-number

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

- Enter your password if
                                                				  prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

voice register dn tag

#### Example:

```
Router(config)#voice register dn 20
```

Enters voice register dn mode to define a directory number for a
                                             				SIP phone, intercom line, voice port, or an MWI.

Step 4

call-forward b2bua unregistered directory-number

#### Example:

```
Router(config-register-dn)#call-forward b2bua unregistered 2345
```

Enables call forwarding for a SIP back-to-back user agent so that
                                             				all incoming calls are forwarded to the unregistered directory-number.

Step 5

end

#### Example:

```
Router(config-ephone)# end
```

Returns to privileged EXEC mode.

#### Troubleshooting
                              	 Tips for Call Forward Unregistered

Use the show dial-peer voice summary command to
                                       			 check whether a CFU dial peer is created or removed.

Enable deb voice reg event , deb voice reg state , and deb voice reg error commands to trace the
                                       			 creation and deletion of the CFU dial peer.

Enable deb voice reg event , deb voip ccapi inout , deb voip app callsetup , deb voip app core , deb voip app state , and deb voip app error commands to trace the
                                       			 call flow for CFU.

### Configure
                           	 Keepalive Timer Expiration in SIP Phones

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- sip

- registrar server [ expires [ max seconds ] [ min seconds ] ]

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

voice service voip

#### Example:

```
Router(conf)# voice service voip
```

Enters
                                             				voice-service configuration mode and specifies voice-over-IP encapsulation.

Step 4

sip

#### Example:

```
Router(conf-serv)# sip
```

Enters SIP
                                             				configuration mode.

Step 5

registrar server [ expires [ max seconds ] [ min seconds ] ]

#### Example:

```
Router(conf-serv-sip)# registrar server expires max 250 min 75
```

Enables SIP
                                             				registrar functionality in Cisco Unified CME.

expires—(Optional) Sets the active time for an incoming
                                                   					 registration.

max
                                                   					 sec—(Optional) Maximum time for a registration to expire, in seconds. Range:
                                                   					 120 to 86400.

min
                                                   					 sec—(Optional) Minimum time for a registration to expire, in seconds.

Step 6

end

#### Example:

```
Router (conf-serv-sip)# end
```

Returns to
                                             				privileged EXEC mode.

### Configure
                           	 Call-Forwarding-All Softkey URI on SIP Phones

To specify the
                                 		  uniform resource identifier (URI) for the call forward all (CfwdAll) softkey on
                                 		  supported SIP phones, perform the following steps. This URI and the call
                                 		  forward number is sent to Cisco Unified CME when a user enables Call Forward
                                 		  All on a SIP phone.

Restriction

- This feature is supported
                                                				only on Cisco Unified IP Phone 7911G, 7941G, 7941GE, 7961G, 7961GE, 7970G, and
                                                				7971GE.

- If a user enables Call
                                                				Forward All using the CfwdAll softkey, it is enabled on the primary line.

#### Before you begin

- Cisco Unified CME 4.1 or a
                                    			 later version.

- The mode cme command must be enabled in Cisco Unified CME.

- Call Forward All must be
                                    			 enabled on the directory number. For information, see Configure SIP-to-SIP Phone Call Forwarding .

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- call-feature-uri cfwdall service-uri

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

- Enter your password if
                                                				  prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice register global

#### Example:

```
Router(config)# voice register global
```

Enters voice
                                             				register global configuration mode to set global parameters for all supported
                                             				SIP phones in a Cisco Unified CME environment.

Step 4

call-feature-uri cfwdall service-uri

#### Example:

```
Router(config-register-global)# call-feature-uri cfwdall http://1.4.212.11/cfwdall
```

Specifies the
                                             				URI for soft keys on SIP phones connected to a Cisco Unified CME router.

Step 5

end

#### Example:

```
Router(config-register-global)# end
```

Exits to
                                             				privileged EXEC mode.

### Specify Number of
                           	 3XX Responses To be Handled on SIP Phones

To specify how
                                 		  many subsequent 3XX responses an originating SIP phone can handle for a single
                                 		  call when the terminating side is a forwarding party which does not use B2BUA,
                                 		  perform the following steps.

#### Before you begin

Cisco CME 3.4
                                       				or a later version.

The mode cme command must be enabled

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- phone-redirect-limit number

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

voice register global

#### Example:

```
Router(config)# voice register global
```

Enters voice
                                             				register global configuration mode to set parameters for all supported SIP
                                             				phones in Cisco Unified CME.

Step 4

phone-redirect-limit number

#### Example:

```
Router(config-register-global)# phone-redirect-limit 8
```

Changes the
                                             				default number of 3XX responses a SIP phone that originates a call can handle
                                             				for a single call.

- Default: 5

Step 5

end

#### Example:

```
Router(config-register-global)# end
```

Exits to
                                             				privileged EXEC mode.

### Configure Call
                           	 Transfer on SIP Phones

To create and
                                 		  apply a template to enable call transfer softkeys on an individual SIP phone in
                                 		  Cisco Unified CME, perform the following steps.

Restriction

Blind transfer is not supported on certain phones such as Cisco Unified IP Phone 7911G, 7941G, 7941GE, 7961G, 7961GE, 7970G,
                                                   or 7971GE.

In Cisco Unified CME 4.1, the soft key display can be customized only for certain IP phones, such as Cisco Unified IP Phone 7911G,
                                                   7941G, 7941GE, 7961G, 7961GE, 7970G, and 7971GE. For configuration information, see Modify Softkey Display on SIP Phone .

#### Before you begin

Cisco CME 3.4 or a
                                 		  later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice register template template-tag

- transfer-attended

- transfer-blind

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

- Range: 1 to 5

Step 4

transfer-attended

#### Example:

```
Router(config-register-template)# transfer-attended
```

Enable a soft
                                             				key for attended transfer on any supported SIP phone that uses a template in
                                             				which this command is configure.

Step 5

transfer-blind

#### Example:

```
Router(config-register-template)# transfer-blind
```

Enable a soft
                                             				key for blind transfer on any supported SIP phone that uses a template in which
                                             				this command is configure.

Step 6

exit

#### Example:

```
Router(config-register-template)# exit
```

Exits
                                             				configuration mode to the next highest mode in the configuration mode
                                             				hierarchy.

Step 7

voice register pool pool-tag

#### Example:

```
Router(config)# voice register pool 3
```

Enters voice
                                             				register pool configuration mode to set phone-specific parameters for SIP
                                             				phones.

Step 8

template template-tag

#### Example:

```
Router(config-register-pool)# voice register pool 1
```

Applies a
                                             				template created with the voice register
                                                   					 template command.

template-tag —Range: 1 to 5

Step 9

end

#### Example:

```
Router(config-register-pool)# end
```

Exits to
                                             				privileged EXEC mode.

## Configuration Examples for Call Transfer and Forwarding

### Example for Configuring H.450.2 and H.450.3 Support

The following example sets all transfers and forwards that are
                                 		  initiated by a Cisco CME 3.0 or later system to use the H.450 standards,
                                 		  globally enables H.450.2 and H.450.3 capabilities, and disables those
                                 		  capabilities for dial peer 37. The supplementary-service commands under voice-service configuration
                                 		  mode are not necessary because these values are the default, but they are shown
                                 		  here for illustration.

```
telephony-service
```

```
transfer-system full-consult
```

```
transfer-pattern .T
```

```
call-forward pattern .T
```

```
!
```

```
voice service voip
```

```
supplementary-service h450.2
```

```
supplementary-service h450.3
```

```
!
```

```
dial-peer voice 37 voip
```

```
destination-pattern 555....
```

```
session target ipv4:10.5.6.7
```

```
no supplementary-service h450.2
```

```
no supplementary-service h450.3
```

### Example for Configuring Basic Call Forwarding

The following example sets up forwarding for extension 2777 to
                                 		  extension 2513 on all calls, busy, and no answer. During night service hours,
                                 		  calls are forwarded to a different number, extension 2879.

```
ephone-dn 20
```

```
number 2777
```

```
call-forward all 2513
```

```
call-forward busy 2513
```

```
call-forward noan 2513 timeout 45
```

```
call-forward night-service 2879
```

### Example for Configuring Call Forwarding Blocked for Local
                           	 Calls

In the following example, extension 2555 is configured to not forward
                                 		  local calls that are internal to the Cisco Unified CME system. Extension 2222
                                 		  dials extension 2555. If 2555 is busy, the caller hears a busy tone. If 2555
                                 		  does not answer, the caller hears ringback. The internal call is not forwarded.

```
ephone-dn 25
```

```
number 2555
```

```
no forward local-calls
```

```
call-forward busy 2244
```

```
call-forward noan 2244 timeout 45
```

### Example for
                           	 Configuring Transfer Patterns

The following
                                 		  example shows how to configure transfer patterns beginning with 1234:

```
Router# configure terminal Router(config)# telephony-service Router(config-telephony)# transfer-pattern 1234
```

### Example for
                           	 Configuring Maximum Length of Transfer Number

The following
                                 		  example shows how to configure the maximum length of the transfer number under
                                 		  voice register pool 1. Because the maximum length is configured as 5, only call
                                 		  transfers to Cisco Unified SIP IP phones with a five-digit directory number are
                                 		  allowed. All call transfers to directory numbers with more than five digits are
                                 		  blocked.

```
Router# configure terminal Router(config)# voice register pool 1 Router(config-register-pool)# transfer max-length 5
```

The following
                                 		  example shows how to configure the maximum length of the transfer number for a
                                 		  set of phones under voice register template 2:

```
Router# configure terminal Router(config)# voice register template 2 Router(config-register-temp)# transfer max-length 10
```

### Example for Configuring Conference Transfer Patterns

The following example configures transfer patterns that allow
                                 		  conference calls:

```
Router# configure terminal Router(config)# telephony-service Router(config-telephony)# transfer-pattern 1357 Router(config-telephony)# transfer-pattern 222 .... Router(config-telephony)# conference transfer-pattern
```

### Example for
                           	 Blocking All Call Transfers

The following
                                 		  example shows how to block all call transfers for voice register pool 5:

```
Router(config)# voice register pool 5 Router(config-register-pool)# transfer-pattern ? blocked  global transfer pattern not allowed Router(config-register-pool)# transfer-pattern blocked
```

The following
                                 		  example shows how to block all call transfers for a set of Cisco Unified SIP IP
                                 		  phones defined by voice register template 9:

```
Router(config)# voice register template 9
Router(config-register-temp)# transfer-pattern ?
blocked  global transfer pattern not allowed
Router(config-register-temp)# transfer-pattern blocked
```

### Example for Configuring Selective Call Forwarding

The following example sets call forwarding on busy and no answer for
                                 		  ephone-dn 38 only for its primary number, 2777. Callers who dial 2778 will hear
                                 		  a busy signal if the ephone-dn is busy or ringback if there is no answer.

```
ephone-dn 38
```

```
number 2777 secondary 2778
```

```
call-forward busy 3000 primary
```

```
call-forward noan 3000 primary timeout 45
```

### Example for Configuring Call Transfer

The following example limits transfers from ephone 6, extension 2977,
                                 		  to numbers containing a maximum of 8 digits.

```
telephony-service
```

```
load 7910 P00403020214
```

```
load 7960-7940 P00305000600
```

```
load 7914 S00103020002
```

```
load 7905 CP7905040000SCCP040701A
```

```
load 7912 CP7912040000SCCP040701A
```

```
max-ephones 100
```

```
max-dn 500
```

```
ip source-address 10.104.8.205 port 2000
```

```
max-redirect 20
```

```
system message XYZ Inc.
```

```
create cnf-files version-stamp 7960 Jul 13 2004 03:39:28
```

```
voicemail 7189
```

```
max-conferences 8 gain -6
```

```
moh music-on-hold.au
```

```
web admin system name admin1 password admin1
```

```
dn-webedit
```

```
time-webedit
```

```
transfer-system full-consult
```

```
transfer-pattern 91..........
```

```
transfer-pattern 92......
```

```
transfer-pattern 93......
```

```
transfer-pattern 94......
```

```
transfer-pattern 95......
```

```
transfer-pattern 96......
```

```
transfer-pattern 97......
```

```
transfer-pattern 98......
```

```
transfer-pattern 99......
```

```
secondary-dialtone 9
```

```
fac standard
```

```
ephone-template 2
```

```
transfer max-length 8
```

```
ephone-dn 4
```

```
number 2977
```

```
ephone 6
```

```
button 1:4
```

```
ephone-template 2
```

### Example for
                           	 Configuring Call Transfer Recall for SCCP Phones

The following
                                 		  example shows that transfer recall is enabled globally. After 60 seconds an
                                 		  unanswered call is forwarded back to the phone that initiated the transfer
                                 		  (transferor).

```
telephony-service
```

```
max-ephones 100
```

```
max-dn 240
```

```
timeouts transfer-recall 60
```

```
max-conferences 8 gain -6
```

```
transfer-system full-consult
```

The following
                                 		  example shows that transfer recall is enabled for extension 1030 (ephone-dn
                                 		  103), which is assigned to ephone 3. If extension 1030 forwards a call and the
                                 		  transfer-to party does not answer, after 60 seconds the unanswered call is sent
                                 		  back to extension 1030 (transferor). The timeouts
                                    			 transfer-recall command can also be set in an ephone-dn template and
                                 		  applied to one or more directory numbers.

```
ephone-dn  103
```

```
number 1030
```

```
name Smith, John
```

```
timeouts transfer-recall 60
```

```
!
```

```
ephone  3
```

```
mac-address 002D.264E.54FA
```

```
type 7962
```

```
button  1:103
```

### Example for
                           	 Configuring Call-Transfer Recall for SIP Phones

The following
                                 		  example shows that transfer recall is enabled globally. After 20 seconds, an
                                 		  unanswered call is forwarded back to the phone that initiated the transfer
                                 		  (transferor).

```
voice register global
 mode cme
 source-address 8.39.17.29 port 5060
 timeouts transfer-recall 20
 max-dn 100
 max-pool 100
 tftp-path flash:
 create profile sync 0342574150542703
 keepalive 140
 auto-register
```

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

### Example for Enabling H.450.12 Capabilities

The following example globally disables H.450.12 capabilities and then
                                 		  enables them only on dial peer 24.

```
voice service voip
```

```
no supplementary-service h450.12
```

```
!
```

```
dial-peer voice 24 voip
```

```
destination-pattern 555....
```

```
session target ipv4:10.5.6.7
```

```
supplementary-service h450.12
```

### Example for Enabling H.450.7 and QSIG Supplementary Services

The following example implements QSIG supplementary services on
                                 		  extension 74367 and globally enables H.450.7 supplementary services and QSIG
                                 		  call-forwarding supplementary services.

```
telephony-service
```

```
voicemail 74398
```

```
transfer-system full-consult
```

```
ephone-dn 25
```

```
number 74367
```

```
mwi qsig
```

```
call-forward all 74000
```

```
voice service voip
```

```
supplementary-service h450.7
```

```
voice service pots
```

```
supplementary-service qsig call-forward
```

### Example for
                           	 Configuring Cisco Unified CME and Cisco Unified Communications Manager in Same
                           	 Network

The following
                                 		  example shows a running configuration for a Cisco CME 3.1 or later router that
                                 		  has a Cisco Unified Communications Manager in its network.

```
Router# show running-config
```

```
version 12.3
```

```
service timestamps debug datetime msec
```

```
service timestamps log datetime msec
```

```
no service password-encryption
```

```
!
```

```
hostname Router
```

```
!
```

```
enable password pswd
```

```
!
```

```
aaa new-model
```

```
!
```

```
!
```

```
aaa session-id common
```

```
no ip subnet-zero
```

```
!
```

```
ip dhcp pool phone1
```

```
host 172.24.82.3 255.255.255.0
```

```
client-identifier 0100.07eb.4629.9e
```

```
default-router 172.24.82.2
```

```
option 150 ip 172.24.82.2
```

```
!
```

```
ip dhcp pool phone2
```

```
host 172.24.82.4 255.255.255.0
```

```
client-identifier 0100.0b5f.f932.58
```

```
default-router 172.24.82.2
```

```
option 150 ip 172.24.82.2
```

```
!
```

```
ip cef
```

```
no ip domain lookup
```

```
no mpls ldp logging neighbor-changes
```

```
no ftp-server write-enable
```

```
!
```

```
voice service voip
```

```
allow-connections h323 to h323
```

```
!
```

```
voice class codec 1
```

```
codec preference 1 g711ulaw
```

```
!
```

```
no voice hpi capture buffer
```

```
no voice hpi capture destination
```

```
!
```

```
interface FastEthernet0/0
```

```
ip address 172.24.82.2 255.255.255.0
```

```
duplex auto
```

```
speed auto
```

```
h323-gateway voip interface
```

```
h323-gateway voip bind srcaddr 172.24.82.2
```

```
!
```

```
ip classless
```

```
ip route 0.0.0.0 0.0.0.0 172.24.82.1
```

```
ip route 192.168.254.254 255.255.255.255 172.24.82.1
```

```
!
```

```
ip http server
```

```
!
```

```
tftp-server flash:P00303020700.bin
```

```
!
```

```
voice-port 1/0/0
```

```
!
```

```
voice-port 1/0/1
```

```
!
```

```
dial-peer cor custom
```

```
!
```

```
dial-peer voice 1001 voip
```

```
description points-to-CCM
```

```
destination-pattern 1.T
```

```
voice-class codec 1
```

```
session target ipv4:172.26.82.10
```

```
!
```

```
dial-peer voice 1002 voip
```

```
description points to router
```

```
destination-pattern 4...
```

```
voice-class codec 1
```

```
session target ipv4:172.25.82.2
```

```
!
```

```
dial-peer voice 1 pots
```

```
destination-pattern 3000
```

```
port 1/0/0
```

```
!
```

```
dial-peer voice 1003 voip
```

```
destination-pattern 26..
```

```
session target ipv4:10.22.22.38
```

```
!
```

```
!
```

```
telephony-service
```

```
load 7960-7940 P00303020700
```

```
max-ephones 48
```

```
max-dn 15
```

```
ip source-address 172.24.82.2 port 2000
```

```
create cnf-files version-stamp Jan 01 2002 00:00:00
```

```
keepalive 10
```

```
max-conferences 4
```

```
moh minuet.au
```

```
transfer-system full-consult
```

```
transfer-pattern ....
```

```
!
```

```
ephone-dn  1
```

```
number 3001
```

```
name abcde-1
```

```
call-forward busy 4001
```

```
!
```

```
ephone-dn  2
```

```
number 3002
```

```
name abcde-2
```

```
!
```

```
ephone-dn  3
```

```
number 3003
```

```
name abcde-3
```

```
!
```

```
ephone-dn  4
```

```
number 3004
```

```
name abcde-4
```

```
!
```

```
ephone  1
```

```
mac-address 0003.EB27.289E
```

```
button  1:1 2:2
```

```
!
```

```
ephone  2
```

```
mac-address 000D.39F9.3A58
```

```
button  1:3 2:4
```

```
!
```

```
line con 0
```

```
exec-timeout 0 0
```

```
logging synchronous
```

```
line aux 0
```

```
line vty 0 4
```

```
password pswd
```

```
!
```

```
end
```

### Example for Configuring H.450 Tandem Gateway Working with
                           	 Cisco Unified CME and Cisco Unified Communications Manager

The following example shows a sample configuration for a Cisco CME 3.1
                                 		  or later system that is linked to an H.450 tandem gateway that serves as a
                                 		  proxy for Cisco Unified Communications Manager.

```
Router# show running-config
```

```
Building configuration...
```

```
Current configuration : 1938 bytes
```

```
!
```

```
version 12.3
```

```
service timestamps debug datetime msec
```

```
service timestamps log datetime msec
```

```
no service password-encryption
```

```
!
```

```
hostname Router
```

```
!
```

```
boot-start-marker
```

```
boot-end-marker
```

```
!
```

```
enable password pswd
```

```
!
```

```
aaa new-model
```

```
!
```

```
aaa session-id common
```

```
no ip subnet-zero
```

```
!
```

```
ip cef
```

```
no ip domain lookup
```

```
no ftp-server write-enable
```

```
no scripting tcl init
```

```
no scripting tcl encdir
```

```
!
```

```
voice call send-alert
```

```
!
```

```
voice service voip
```

```
allow-connections h323 to h323
```

```
supplementary-service h450.12
```

```
h323
```

```
!
```

```
voice class codec 1
```

```
codec preference 1 g711ulaw
```

```
codec preference 2 g729r8
```

```
codec preference 3 g729br8
```

```
!
```

```
interface FastEthernet0/0
```

```
ip address 172.27.82.2 255.255.255.0
```

```
duplex auto
```

```
speed auto
```

```
h323-gateway voip interface
```

```
h323-gateway voip h323-id host24
```

```
!
```

```
ip classless
```

```
ip route 0.0.0.0 0.0.0.0 172.26.82.1
```

```
ip route 0.0.0.0 0.0.0.0 172.27.82.1
```

```
ip http server
```

```
!
```

```
dial-peer cor custom
```

```
!
```

```
dial-peer voice 1001 voip
```

```
description points-to-CCM
```

```
destination-pattern 4...
```

```
session target ipv4:172.24.89.150
```

```
!
```

```
dial-peer voice 1002 voip
```

```
description points to CCME1
```

```
destination-pattern 28..
```

```
session target ipv4:172.24.22.38
```

```
!
```

```
dial-peer voice 1003 voip
```

```
description points to CCME3
```

```
destination-pattern 9...
```

```
session target ipv4:192.168.1.29
```

```
!
```

```
dial-peer voice 1004 voip
```

```
description points to CCME2
```

```
destination-pattern 29..
```

```
session target ipv4:172.24.22.42
```

```
!
```

```
line con 0
```

```
exec-timeout 0 0
```

```
logging synchronous
```

```
line aux 0
```

```
line vty 0 4
```

```
password pswd
```

```
!
```

```
end
```

### Example for Configuring Call Forward to Cisco Unity Express

The following example enables the ability to forward calls that
                                 		  originate from Cisco Unified Communications Manager phones and are routed
                                 		  through a Cisco Unified CME system to a Cisco Unity Express extension. Call
                                 		  forwarding is enabled for all calling parties, H.450.3 is disabled, and
                                 		  connections are allowed to SIP endpoints.

```
telephony-service
```

```
call-forward pattern .T
```

```
voice service voip
```

```
no supplementary-service h450.3
```

```
allow connections from h323 to sip
```

### Example for Configuring Call Forward Unregistered for SIP IP
                           	 Phones

The following example shows CFU configured for voice register dn 20:

```
!
```

```
!
```

```
!
```

```
voice service voip
```

```
allow-connections sip to sip
```

```
sip
```

```
registrar server expires max 250 min 75
```

```
!
```

```
!
```

```
voice register global
```

```
mode cme
```

```
source-address 10.100.109.10 port 5060
```

```
bandwidth video tias-modifier 256 negotiate end-to-end
```

```
max-dn 200
```

```
max-pool 42
```

```
url directory http://1.4.212.11/localdirectory
```

```
create profile sync 0004625832149157
```

```
!
```

```
voice register dn  20
```

```
number 10
```

```
call-forward b2bua unregistered 2345
```

```
!
```

```
voice register pool  1
```

```
number 1 dn 20
```

```
id mac 1111.1111.1111
```

```
camera
```

```
video
```

```
!
```

```
voice register pool  2
```

```
id mac 0009.A3D4.1234
```

### Example for Configuring Keepalive Timer Expiration in SIP
                           	 Phones

The following example shows the minimum and maximum registrar server
                                 		  expiration time for SIP phones:

```
Router#show run
```

```
!
```

```
!
```

```
!
```

```
!
```

```
!
```

```
!
```

```
voice service voip
```

```
allow-connections sip to sip
```

```
sip
```

```
registrar server expires max 250 min 75
```

```
!
```

```
!
```

```
voice register global
```

```
mode cme
```

```
source-address 10.100.109.10 port 5060
```

```
bandwidth video tias-modifier 256 negotiate end-to-end
```

```
max-dn 200
```

## Where to Go
                        	 Next

If you are finished
                           		modifying the configuration, generate a new configuration file and restart the
                           		phones. See Generate Configuration Files for Phones .

Softkeys

To block the
                           		function of the call-forward-all or transfer softkey without removing the key
                           		display or to remove the softkey from one or more phones, see Customize Softkeys .

Feature
                              		  Access Codes (FACs)

Phone users can
                           		activate and deactivate a phone’s call-forward-all setting by using a feature
                           		access code (FAC) instead of a soft key on the phone if standard or custom FACs
                           		have been enabled for your system. The following are the standard FACs for call
                           		forward all:

callfwd all —Call forward all calls. Standard FAC
                                 			 is **1 plus an optional target extension.

callfwd cancel —Cancel call forward all calls.
                                 			 Standard FAC is **2.

For more information
                           		about FACs, see Feature Access Codes .

Night
                              		  Service

Calls can be
                           		automatically forwarded during night service hours, but you must define the
                           		night-service periods, which are the dates or days and hours during which night
                           		service will be active. For instance, you may want to designate night service
                           		periods that include every weeknight between 5 p.m. and 8 a.m. and all day
                           		every Saturday and Sunday. For more information, see Configure Call Coverage Features .

## Feature
                        	 Information for Call Transfer and Forwarding

The following table
                           		provides release information about the feature or features described in this
                           		module. This table lists only the software release that introduced support for
                           		a given feature in a given software release train. Unless noted otherwise,
                           		subsequent releases of that software release train also support that feature.

Use Cisco Feature
                           		Navigator to find information about platform support and Cisco software image
                           		support. To access Cisco Feature Navigator, go to www.cisco.com/go/cfn .
                           		An account on Cisco.com is not required.

Feature
                                       				  Name

Cisco Unified CME Version

Feature
                                       				  Information

Calling Number Local

12.0

Introduced support to configure Calling Number Local feature for
                                       				  Voice Register DNs.

Call
                                       				  Transfer Recall on SIP Phones

11.6

Call
                                       				  Transfer Recall feature returns a transferred call to the phone that initiated
                                       				  the transfer if the destination is busy or does not answer.

Trunk-to-Trunk Transfer Blocking for Toll Fraud Prevention on
                                       				  Cisco Unified SIP IP Phones

9.5

Introduced
                                       				  support Trunk-to-Trunk Transfer Blocking for Toll Fraud Prevention on Cisco
                                       				  Unified SIP IP Phones.

Call
                                       				  Forwarding

4.1

Call
                                             						Forward All synchronization between Cisco Unified CME and SIP phones was added.

Disabling SIP supplementary services for call forward and call
                                             						transfer was added.

4.0

Automatic call forwarding during night service was introduced.

Selective call forwarding was introduced.

Forwarding of local (internal) calls can be blocked.

H.450.7 standards support and QSIG supplementary services
                                             						capability was introduced.

3.4

Calls into
                                       				  a SIP device can be forwarded to other SIP or SCCP devices including
                                       				  Cisco Unity, third- party voice mail systems, or an auto-attendant (AA) or
                                       				  other interactive voice response (IVR) devices. SCCP devices may also be
                                       				  forwarded to SIP devices.

3.1

Number
                                             						of digits that can be entered using the CfwdALL (call-forward all) soft key can
                                             						be limited.

H.450.12 standards support, which provide dynamic detection of
                                             						H.450.2 and H.450.3 capabilities on a call-by-call basis, was introduced.

3.0

CFwdALL soft key was introduced.

Local
                                             						hairpin call routing was supported as an option for networks that cannot
                                             						support H.450 call transfer and forwarding. This feature requires installation
                                             						of the Tcl script app_h450_transfer.2.0.0.8.tcl or a later version.

2.1

Call
                                       				  forwarding using the H.450.3 standard was introduced.

1.0

Call
                                       				  forwarding for all calls, busy conditions, and no-answer conditions was
                                       				  introduced, using a Cisco-proprietary method.

Call
                                       				  Forward Unregistered

8.6

The Call
                                       				  Forward Unregistered (CFU) feature was introduced for SIP phones.

Call
                                       				  Transfer

4.3

Call-Transfer Recall was added.

Consultative Call Transfer digit-collection process was
                                             						modified.

4.1

Disabling SIP supplementary services for call transfer and call
                                             						forward was added.

4.0

Default for the transfer-system command was changed from the blind keyword to the full-consult keyword.

Transfers to phones outside the Cisco Unified CME system can be
                                             						blocked for individual ephones.

Number
                                             						of digits in transfer destination numbers can be limited.

3.4

Support
                                       				  for attended and blind transfer s using SIP IP phone directly connected to
                                       				  Cisco CME.

3.2

Consultative transfer to monitored lines using direct station
                                             						select was introduced.

Transcoding between G.711 and G.729 is supported when one leg of
                                             						a Voice over IP (VoIP)-to-VoIP hairpin call uses G.711 and the other leg uses
                                             						G.729.

3.1

Support
                                       				  was introduced for the following:

Enhancements for VoIP networks which contain a mix of platforms
                                             						that support H.450.2 and H.450.3 standards, such as Cisco CME 3.1,
                                             						Cisco CME 3.0, Cisco ITS V2.1, and platforms that do not support H.450.2 and
                                             						H.450.3 standards, such as Cisco Unified Communications Manager, Cisco BTS
                                             						Softswitch (BTS), and Cisco PSTN Gateway (PGW).

H.450.12 standards, which provide dynamic detection of H.450.2
                                             						and H.450.3 capabilities on a call-by-call basis.

Automatic detection of Cisco Unified Communications Manager
                                             						endpoints.

Hairpin VoIP-to-VoIP call routing and routing to an H.450 tandem
                                             						gateway.

Hairpin call routing does not require a Tcl script.

3.0

Local
                                       				  hairpin call routing was supported as an option for networks that cannot
                                       				  support H.450 call transfer and forwarding. This feature requires installation
                                       				  of the Tcl script app_h450_transfer.2.0.0.8.tcl or a later version.

2.1

Consultative transfer using the ITU-T H.450.2 standard was
                                       				  introduced.

1.0

Call
                                       				  transfer was introduced, using a Cisco proprietary method.

| Note | In earlier
                                       		versions of Cisco Unified CME, a busy tone was played for callers when the
                                       		callers are unable to reach the SCCP phone number. In Cisco Unified CME 8.6 and
                                       		later versions, a fast busy tone is played instead of a busy tone for callers
                                       		who are unable to reach the phone. |
|---|---|

| Commands | Cisco
                                             				  Unified CME |
|---|---|
| transfer-pattern | telephony-service |
| transfer max-length | voice register pool or voice register template |
| transfer-pattern
                                                					 blocked | voice register pool or voice register template |
| conference
                                             				  transfer-pattern | telephony-service |
| conference max-length | ephone ephone-template voice register pool voice register template |
| conference-pattern
                                                					 blocked | ephone ephone-template voice register pool voice register template |

| Note | The call transfer
                                       		and conference restrictions apply when transfers or conferences are initiated
                                       		toward external parties, like a PSTN trunk, a SIP trunk, or an H.323 trunk. The
                                       		restrictions do not apply to transfers to local extensions. |
|---|---|

| Note | The blind keyword
                                          		in the transfer-pattern command applies to Cisco Unified
                                          		SCCP IP phones only and does not apply to Cisco Unified SIP IP phones. |
|---|---|

| Note | In Cisco Unified
                                          		CME 9.5 and later versions, Cisco Unified SIP IP phones and Cisco Unified SCCP
                                          		IP phones registered to the same Cisco Unified CME are considered local and do
                                          		not require transfer-pattern configuration. |
|---|---|

| Note | In Cisco Unified CME 9.5 and later versions, once transfer patterns
                                             		are configured in telephony-service configuration mode, the transfer patterns
                                             		apply to both Cisco Unified SCCP IP phones and Cisco Unified SIP IP phones. |
|---|---|

| Note | If only transfer max length is configured and conference max-length
                                          		is not configured, then transfer max-length takes effect for transfers and
                                          		conferences. |
|---|---|

| Note | If both conference max-length and transfer
                                                			 max-length commands are configured, the conference max-length command takes precedence for
                                          		conferences. |
|---|---|

|  | conference
                                                					 max-length | no conference max-length |
|---|---|---|
| No
                                                   						conference-pattern blocked (default case) | Allowing/Blocking of conference call depends on configured
                                                					 conference max-length | Allowing/Blocking of conference call depends on configured
                                                					 transfer max-length |
| conference-pattern blocked | No
                                                					 conference calls allowed for SIP and SCCP phones. |

|  | Max-length <= allowed max-length | Max-length > allowed max-length |
|---|---|---|
|  | Transfer | Conference | Transfer | Conference |
| Transfer max-length + No Conference max-length (use transfer
                                             					 max-length for conference cases too, as conference max-length not configured) | Y | Y | N | N |
| No transfer max-length + Conference max-length (conference
                                             					 max-length has precedence over transfer max-length for conference) | Y | Y | Y | N |
| No transfer max-length + Conference max-length (conference
                                             					 max-length has precedence over transfer max-length for conference) | Y | Y | N | N |
| No transfer max-length + No conference max-length | All transfer and conference calls are allowed. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                                				privileged EXEC mode. Enter your password if
                                                   				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                                				configuration mode. |
| Step 3 | Enter one of the following commands: voice register pool pool-tag voice register template template-tag ephone phone-tag ephone template template-tag Example: Router(config)# voice register pool 25 | Enters voice register pool configuration mode and creates a pool configuration for a Cisco Unified SIP IP phone in Cisco Unified
                                                CME. pool-tag —Unique number assigned to the pool. Range is 1 to 100. or Enters voice register template configuration mode and defines a template of common parameters for Cisco Unified SIP IP phones. template-tag —Declares a template tag. Range is 1 to 10. or Enters ephone configuration mode. phone-tag —Unique sequence number that identifies this ephone during configuration tasks. The maximum number of ephones is version and
                                                      platform-specific. Type? to display range. |
| Step 4 | conference
                                                   				  max-length value Example: Router(config-register-pool)# conference max-length 6 | Allows the
                                                				conference calls from Cisco IP phones to specified directory numbers of phones. conference
                                                   				  max-length—Specifies the maximum number of digits while making a conference
                                                   				  call. Range is 3 to 16. |
| Step 5 | exit Example: Router(config-register-pool)# exit | Exits voice
                                                				register pool configuration mode and enters global configuration mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                                				privileged EXEC mode. Enter your password if
                                                   				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                                				configuration mode. |
| Step 3 | Enter one of the following commands: voice register pool pool-tag or voice register template template-tag ephone phone-tag ephone template template-tag Example: Router(config)# voice register pool 25 | Enters voice register pool configuration mode and creates a pool configuration for a Cisco Unified SIP IP phone in Cisco Unified
                                                CME or for a set of Cisco Unified SIP IP phones in Cisco Unified SIP SRST. pool-tag—Unique number assigned to the pool. Range is 1 to 100. or Enters voice register template configuration mode and defines a template of common parameters for Cisco Unified SIP IP phones. template-tag—Declares a template tag. Range is 1 to 10. or Enters ephone configuration mode. phone-tag—Unique sequence number that identifies this ephone during configuration tasks. The maximum number of ephones is
                                                      version and platform-specific. Type? to display range. |
| Step 4 | conference-pattern blocked Example: Router(config-register-pool)# | Blocks
                                                				conference calls to external numbers. conference-pattern
                                                   				  block—Prevents extensions on an ephone or a voice register pool from initiating
                                                   				  conferences. |
| Step 5 | exit Example: Router(config-register-pool)# exit | Exits voice
                                                				register pool configuration mode. |

| Configuration | Cisco
                                                				  Unified SCCP IP Phones | Cisco
                                                				  Unified SIP IP Phones |
|---|---|---|
| No transfer
                                                				  patterns are configured. | All
                                                				  non-local call transfers are blocked. | All
                                                				  non-local call transfers are allowed for backward compatibility. |
| Specific
                                                				  transfer patterns are configured. | Call
                                                				  transfers to specific external entities are allowed. | Call
                                                				  transfers to specific external entities are allowed. |
| The transfer-pattern blocked command is configured. | All
                                                				  non-local call transfers are blocked. Note The
                                                         				  configuration reverts to the default, where no transfer patterns are
                                                         				  configured. | Note | The
                                                         				  configuration reverts to the default, where no transfer patterns are
                                                         				  configured. | All
                                                				  non-local call transfers are blocked. Note The
                                                         				  configuration unconditionally blocks all non-local call transfers. It does not
                                                         				  return to the default, where all non-local call transfers are allowed. | Note | The
                                                         				  configuration unconditionally blocks all non-local call transfers. It does not
                                                         				  return to the default, where all non-local call transfers are allowed. |
| Note | The
                                                         				  configuration reverts to the default, where no transfer patterns are
                                                         				  configured. |
| Note | The
                                                         				  configuration unconditionally blocks all non-local call transfers. It does not
                                                         				  return to the default, where all non-local call transfers are allowed. |

| Note | The
                                                         				  configuration reverts to the default, where no transfer patterns are
                                                         				  configured. |
|---|---|

| Note | The
                                                         				  configuration unconditionally blocks all non-local call transfers. It does not
                                                         				  return to the default, where all non-local call transfers are allowed. |
|---|---|

| Cisco Unified CME Version | transfer-system Command Default | transfer-system Keyword to Use | Transfer
                                                				  Method Recommendation |
|---|---|---|---|
| 4.0 and
                                                				  later | full-consult | full-consult or full-blind | Use H.450.2
                                                				  for call transfer, which is the default for this version. You do not need to
                                                				  use the transfer-system command unless you want to use the full-blind or dss keyword. Optionally,
                                                				  you can use the proprietary Cisco method by using the transfer-system command with the blind or local-consult keyword. Use H.450.7
                                                				  for call transfer using QSIG supplementary services |
| 3.0 to 3.3 | blind | full-consult or full-blind | Use H.450.2
                                                				  for call transfer. You must explicitly configure the transfer-system command with the full-consult or full-blind keyword because H.450.2 is not the default for
                                                				  this version. Optionally,
                                                				  you can use the proprietary Cisco method by using the transfer-system command with the blind or local-consult keyword. |
| 2.1 | blind | blind or local-consult | Use the
                                                				  Cisco proprietary method, which is the default for this version. You do not
                                                				  need to use the transfer-system command unless you want to use the local-consult keyword. Optionally,
                                                				  you can use the transfer-system command with the full-consult or full-blind keyword. You must also configure the router with
                                                				  a Tcl script that is contained in the app-h450-transfer.x.x.x.x.zip file. This
                                                				  file is available from the Cisco Unified CME software download website at: Download Software . |
| Earlier than
                                                				  2.1 | blind | blind | Use the
                                                				  Cisco proprietary method, which is the default for this version. You do not
                                                				  need to use the transfer-system command unless you want to use the local-consult keyword. |

| Note | An H.450 tandem
                                          		gateway that is used in a network to support non-H.450-capable call processing
                                          		systems requires the Integrated Voice and Video Services feature license. This
                                          		feature license, which was introduced in March 2004, includes functionality for
                                          		H.323 gatekeeper, IP-to-IP Gateway, and H.450 tandem gateway. With Cisco IOS
                                          		Release 12.3(7)T, an H.323 gatekeeper feature license is required with a
                                          		JSX Cisco IOS image on the selected router. Consult your Cisco Unified CME SE
                                          		regarding the required feature license. With Cisco IOS Release 12.3(7)T, you
                                          		cannot use Cisco Unified CME and H.450 tandem gateway functionality on the same
                                          		router. |
|---|---|

| Note | Cisco Communications Manager Express 3.2 (Cisco CME 3.2) and later
                                          		versions provide full call-transfer and call-forwarding with call processing
                                          		systems on the network that support H.450.2, H.450.3, and H.450.12 standards.
                                          		For interoperability with call processing systems that do not support H.450
                                          		standards, Cisco CME 3.2 and later versions provide VoIP-to-VoIP hairpin call
                                          		routing without requiring the special Tool Command Language (Tcl) script that
                                          		was needed in earlier versions of Cisco Unified CME. |
|---|---|

| Note | If your network
                                             		contains a Cisco Unified Communications Manager, also see the instructions in
                                             		the Enable Interworking with Cisco Unified Communications Manager . |
|---|---|

| Note | Cisco CME 3.0 and
                                             		Cisco ITS V2.1 systems do not have H.450.12 capabilities. |
|---|---|

| Note | If your network
                                             		contains a Cisco Unified Communications Manager, also see the instructions in
                                             		the Enable Interworking with Cisco Unified Communications Manager . |
|---|---|

| Note | H.450.2 and
                                          		  H.450.3 capabilities are enabled by default for transferred or forwarded
                                          		  parties and transfer-destination or forward-destination parties. Dial peer
                                          		  settings override the global setting. |
|---|---|

| Restriction | Call
                                                   				  transfers are handled differently depending on the Cisco Unified CME version.
                                                   				  See Transfer Method Recommendations by Cisco Unified CME Version for recommendations on selecting a transfer method for your Cisco Unified CME
                                                   				  version. The transfer-system
                                                         						local-consult command is not supported if the transfer-to
                                                   				  destination is on the Cisco ATA, Cisco VG224, or a SCCP-controlled FXS port. The H.450.2
                                                   				  and H.450.3 standards are not supported by
                                                   				  Cisco Unified Communications Manager, Cisco BTS, or Cisco PGW. In versions
                                                   				  earlier than Cisco Unified CME 4.2, the caller ID displays correctly only after
                                                   				  connect; caller ID does not display correctly at Call Transfer or Call Forward. Call-Transfer Recall Requires
                                                   				  Cisco Unified CME 4.3 or a later version. Transferor
                                                   				  and transfer-to party must be on the same Cisco Unified CME router; transferee
                                                   				  party can be remote to the Cisco Unified CME router. Transfer
                                                   				  recall is not supported if the transfer-to party has Call Forward Busy enabled,
                                                   				  or if the transfer-to party is a hunt group pilot number. If the
                                                   				  transfer-to party has Call Forward No Answer enabled, Cisco Unified CME recalls
                                                   				  a transferred call only if the transfer-recall timeout is set to less than the
                                                   				  timeout value set with the call-forward noan command. Recall timer
                                                   				  for trunk-line directory number has precedence (set on transferor using trunk command with transfer-timeout keyword) over the transfer-recall timer.
                                                   				  Transfer recall is not initiated for hairpin transfers. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 4 | transfer-system { blind \| full-blind \| full-consult [ dss ] \| local-consult } Example: Router(config-telephony)# transfer-system full-consult | Specifies the
                                             				call transfer method. blind —Calls are transferred without consultation using the
                                                   					 Cisco proprietary method and a single phone line. This is the default in
                                                   					 versions earlier than Cisco Unified CME 4.0. full-blind —Calls are transferred without consultation using
                                                   					 H.450.2 standard methods. full-consult —Calls are transferred with consultation using
                                                   					 H.450.2 standard methods and a second phone line if available. Calls fall back
                                                   					 to full-blind if the second line is unavailable. This is the default in
                                                   					 Cisco Unified CME 4.0 and later versions. Transfer-system needs to be set at
                                                   					 full-consult for the “transfer by directory” to work. Transfer by directory is
                                                   					 supported by full-consult or blind transfer. If you want to transfer using
                                                   					 directory/placed/missed/received calls, the transfer-system needs to be set at
                                                   					 full-consult for this to work appropriately. When changed to full-consult, you
                                                   					 can do "blind transfer" by selecting the number from the directory and when the
                                                   					 other phone rings, you can press the softkey "Transfer" and the call will be
                                                   					 transferred to the number selected and then you can hang up. dss —(Optional) Calls are transferred with consultation to
                                                   					 idle monitored lines. All other call-transfer behavior is identical to
                                                   					 full-consult. local-consult —Calls are transferred with local consultation
                                                   					 using a second phone line if available. The calls fall back to blind for
                                                   					 nonlocal consultation or nonlocal transfer target. Not supported if transfer-to
                                                   					 destination is on the Cisco ATA, Cisco VG224, or a SCCP-controlled FXS port. Cisco CME
                                                   					 3.0 and later versions—Use only the full-blind or full-consult keyword. Before
                                                   					 Cisco CME 3.0—Use the local-consult or blind keyword. (Cisco ITS 2.1 can use the full-blind or full-consult keyword by also using the Tcl script in the
                                                   					 file called app-h450-transfer.x.x.x.x.zip.) |
| Step 5 | transfer-pattern transfer-pattern [ blind ] Example: Router(config-telephony)# transfer-pattern .T | Allows
                                             				transfer of telephone calls by Cisco Unified IP phones to specified phone
                                             				number patterns. If no transfer pattern is set, the default is that transfers
                                             				are permitted only to other local IP phones. transfer-pattern —String of digits for permitted call
                                                   					 transfers. Wildcards are allowed. A pattern of .T transfers all calling parties
                                                   					 using the H.450.2 standard. blind —(Optional) When
                                                   					 H.450.2 consultative call transfer is configured, forces transfers that match
                                                   					 the pattern specified in this command to be executed as blind transfers.
                                                   					 Overrides settings made using the transfer-system and transfer-mode commands. Note For
                                                      				transfers to nonlocal numbers, transfer-pattern digit matching is performed
                                                      				before translation-rule operations. Therefore, you should specify in this
                                                      				command the digits actually entered by phone users before they are translated. | Note | For
                                                      				transfers to nonlocal numbers, transfer-pattern digit matching is performed
                                                      				before translation-rule operations. Therefore, you should specify in this
                                                      				command the digits actually entered by phone users before they are translated. |
| Note | For
                                                      				transfers to nonlocal numbers, transfer-pattern digit matching is performed
                                                      				before translation-rule operations. Therefore, you should specify in this
                                                      				command the digits actually entered by phone users before they are translated. |
| Step 6 | call-forward
                                                				  pattern pattern Example: Router(config-telephony)# call-forward pattern .T | Specifies
                                             				the H.450.3 standard for call forwarding. pattern —Digits to match for call forwarding using
                                                   					 the H.450.3 standard. If an incoming calling-party number matches the pattern,
                                                   					 it can be forwarded using the H.450.3 standard. A pattern of .T forwards all
                                                   					 calling parties using the H.450.3 standard. Calling-party numbers that do not match the patterns defined
                                             				with this command are forwarded using Cisco proprietary call forwarding for
                                             				backward compatibility. Note For
                                                      				forwarding to nonlocal numbers, pattern matching is performed before
                                                      				translation-rule operations. Therefore, you should specify in this command the
                                                      				digits actually entered by phone users before they are translated. | Note | For
                                                      				forwarding to nonlocal numbers, pattern matching is performed before
                                                      				translation-rule operations. Therefore, you should specify in this command the
                                                      				digits actually entered by phone users before they are translated. |
| Note | For
                                                      				forwarding to nonlocal numbers, pattern matching is performed before
                                                      				translation-rule operations. Therefore, you should specify in this command the
                                                      				digits actually entered by phone users before they are translated. |
| Step 7 | timeouts
                                                				  transfer-recall seconds Example: Router(config-telephony)# timeouts transfer-recall 30 | (Optional)
                                             				Enables Cisco Unified CME to recall a transferred call if the transfer-to party
                                             				is busy or does not answer. seconds —Duration, in seconds, to wait before
                                                   					 recalling a transferred call. Range: 1 to 1800. Default: 0 (disabled). This command
                                             				is supported in Cisco Unified CME 4.3 and later versions. This command
                                             				can also be configured in ephone-dn and ephone-dn-template configuration mode. |
| Step 8 | transfer-digit-collect { new-call \| orig-call } Example: Router(config-telephony)# transfer-digit-collect orig-call | (Optional)
                                             				Selects the digit-collection method used for consultative call transfers. new-call —Digits are collected from the new call
                                                				  leg. Default value in Cisco Unified CME 4.3 and later versions. orig-call —Digits are collected from original
                                                   					 call-leg. Default behavior in versions earlier than Cisco Unified CME 4.3. This command
                                             				is supported in Cisco Unified CME 4.3 and later versions. |
| Step 9 | exit Example: Router(config-telephony)# exit | Exits
                                             				telephony-service configuration mode. |
| Step 10 | voice service
                                                				  voip Example: Router(config)# voice service voip | (Optional)
                                             				Enters voice-service configuration mode to establish global call transfer and
                                             				forwarding parameters. |
| Step 11 | supplementary-service
                                                				  h450.2 Example: Router(conf-voi-serv)# supplementary-service h450.2 | (Optional)
                                             				Enables H.450.2 supplementary services capabilities globally. Default is
                                             				enabled. Use the no form of this command to disable H.450.2 capabilities globally. You can also use
                                             				this command in dial-peer configuration mode to enable H.450.2 services for a
                                             				single dial peer. |
| Step 12 | supplementary-service
                                                				  h450.3 Example: Router(conf-voi-serv)# supplementary-service h450.3 | (Optional)
                                             				Enables H.450.3 supplementary services capabilities globally. Default is
                                             				enabled. Use the no form of this command to disable H.450.3 capabilities globally. You can also use
                                             				this command in dial-peer configuration mode to enable H.450.3 services for a
                                             				single dial peer. |
| Step 13 | exit Example: Router(conf-voi-serv)# exit | (Optional)
                                             				Exits voice-service configuration mode. |
| Step 14 | dial-peer voice tag voip Example: Router(config)# dial-peer voice 1 voip | (Optional)
                                             				Enters dial-peer configuration mode. |
| Step 15 | supplementary-service
                                                				  h450.2 Example: Router(config-dial-peer)# no supplementary-service h450.2 | (Optional)
                                             				Enables H.450.2 supplementary services capabilities for an individual dial
                                             				peer. Default is
                                             				enabled. You can also use this command in voice-service configuration mode to
                                             				enable H.450.2 services globally. If this
                                                   					 command is enabled globally and enabled on a dial peer, the functionality is
                                                   					 enabled for the dial peer. This is the default. If this
                                                   					 command is enabled globally and disabled on a dial peer, the functionality is
                                                   					 disabled for the dial peer. If this
                                                   					 command is disabled globally and either enabled or disabled on a dial peer, the
                                                   					 functionality is disabled for the dial peer. |
| Step 16 | supplementary-service
                                                				  h450.3 Example: Router(config-dial-peer)# no supplementary-service h450.3 | (Optional)
                                             				Enables H.450.3 supplementary services capabilities exchange for an individual
                                             				dial peer. Default is
                                             				enabled. You can also use this command in voice-service configuration mode to
                                             				enable H.450.3 services globally. If this
                                                   					 command is enabled globally and enabled on a dial peer, the functionality is
                                                   					 enabled for the dial peer. This is the default configuration. If this
                                                   					 command is enabled globally and disabled on a dial peer, the functionality is
                                                   					 disabled for the dial peer. If this
                                                   					 command is disabled globally and either enabled or disabled on a dial peer, the
                                                   					 functionality is disabled for the dial peer. |
| Step 17 | end Example: Router(config-dial-peer)# end | Returns to
                                             				privileged EXEC mode. |

| Note | For
                                                      				transfers to nonlocal numbers, transfer-pattern digit matching is performed
                                                      				before translation-rule operations. Therefore, you should specify in this
                                                      				command the digits actually entered by phone users before they are translated. |
|---|---|

| Note | For
                                                      				forwarding to nonlocal numbers, pattern matching is performed before
                                                      				translation-rule operations. Therefore, you should specify in this command the
                                                      				digits actually entered by phone users before they are translated. |
|---|---|

| Note | Transferor
                                                   				  and transfer-to party must be on the same Cisco Unified CME router; transferee
                                                   				  party can be remote to the Cisco Unified CME router. Transfer
                                                   				  recall is not supported if the transfer-to party has Call Forward Busy enabled,
                                                   				  or if the transfer-to party is a hunt group pilot number. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register global Example: Router(config)# voice register global | Enters voice
                                             				register global configuration mode to set parameters for all supported SIP
                                             				phones in Cisco Unified CME. |
| Step 4 | timeouts transfer-recall seconds Example: Router(config-register-global)# timeouts transfer-recall 30 Router(config-register-dn)# timeouts transfer-recall 30 | Enables
                                             				Cisco Unified CME to recall a transferred call if the transfer-to party is busy
                                             				or does not answer in the voice register global configuration mode. You can
                                             				also recall a transferred call in the voice register dn configuration mode. seconds —Duration, in seconds, to wait before
                                                   					 recalling a transferred call. Range: 1 to 1800. Default: 0 (disabled). This
                                                   					 command is supported in Cisco Unified CME 11.6 and later versions. This
                                                   					 command can also be configured in voice register dn or voice register global
                                                   					 configuration modes. |
| Step 5 | exit Example: Router(config-register-global)# exit | Exits voice
                                             				register global configuration mode. |
| Step 6 | voice service voip Example: Router(config)# voice service voip | (Optional)
                                             				Enters voice-service configuration mode. |
| Step 7 | no supplementary-service sip refer Example: Router(config-voi-serv)# no supplementary-service sip refer | Prevents the
                                             				router from forwarding a REFER message to the destination for call-transfer
                                             				recalls. |
| Step 8 | end Example: Router(config-voi-serv)# end | Returns to
                                             				privileged EXEC mode. |

| Note | When defining
                                          		  call forwarding to nonlocal numbers, it is important to note that pattern digit
                                          		  matching is performed before translation-rule operations. Therefore, you should
                                          		  specify in this command the digits actually entered by phone users before they
                                          		  are translated. |
|---|---|

| Restriction | Call forwarding is invoked only if that phone is dialed directly. Call forwarding is not invoked when the phone number is
                                                called through a sequential, longest-idle, or peer hunt group. If call forwarding is configured for hunt group member, call forward is ignored by the hunt group. Calls from an internal extension to an extension which is busy, is forwarded to the SNR destination even if no forward local-calls
                                                is configured under the Directory Number. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service Example: Router(config)# | Enters
                                             				telephony-service configuration mode. |
| Step 4 | call-forward pattern pattern Example: Router(config-telephony)# call-forward pattern .T | Specifies the
                                             				H.450.3 standard for call forwarding. Calling-party numbers that do not match
                                             				the patterns defined with this command are forwarded using Cisco-proprietary
                                             				call forwarding for backward compatibility. pattern —Digits to match
                                                				  for call forwarding using the H.450.3 standard. If an incoming calling-party
                                                				  number matches the pattern, it is forwarded using the H.450.3 standard. A
                                                				  pattern of .T forwards all calling parties using the H.450.3 standard. |
| Step 5 | exit Example: Router(config-telephony)# exit | Exits
                                             				telephony-service configuration mode. |
| Step 6 | ephone-dn dn-tag [ dual-line ] Example: Router(config)# ephone-dn 20 | Enters
                                             				ephone-dn configuration mode, creates an ephone-dn, and optionally assigns it
                                             				dual-line status. dual-line —(Optional)
                                                				  Enables an ephone-dn with one voice port and two voice channels, which supports
                                                				  features such as call waiting, call transfer, and conferencing with a single
                                                				  ephone-dn. |
| Step 7 | number number [ secondary number ] [ no-reg [ both \| primary ] ] Example: Router(config-ephone-dn)# number 2777 secondary 2778 | Configures a
                                             				valid extension number for this ephone-dn instance. |
| Step 8 | call-forward all target-number Example: Router(config-ephone-dn)# call-forward all 2411 | Forwards all
                                             				calls for this extension to the specified number. target-number —Phone
                                                				  number to which calls are forwarded. Note After you
                                                      				use this command to specify a target number, the phone user can activate and
                                                      				cancel the call-forward-all state from the phone using the CFwdAll soft key or
                                                      				a feature access code (FAC). | Note | After you
                                                      				use this command to specify a target number, the phone user can activate and
                                                      				cancel the call-forward-all state from the phone using the CFwdAll soft key or
                                                      				a feature access code (FAC). |
| Note | After you
                                                      				use this command to specify a target number, the phone user can activate and
                                                      				cancel the call-forward-all state from the phone using the CFwdAll soft key or
                                                      				a feature access code (FAC). |
| Step 9 | call-forward
                                                				  busy target-number [ primary \| secondary ] [ dialplan-pattern ] Example: Router(config-ephone-dn)# call-forward busy 2513 | Forwards
                                             				calls for a busy extension to the specified number. |
| Step 10 | call-forward
                                                				  noan target-number timeout seconds [ primary \| secondary ] [ dialplan-pattern ] Example: Router(config-ephone-dn)# call-forward noan 2513 timeout 45 | Forwards
                                             				calls for an extension that does not answer. |
| Step 11 | call-forward night-service target-number Example: Router(config-ephone-dn)# call-forward night-service 2879 | Automatically forwards incoming calls to the specified number
                                             				when night service is active. target-number —Phone
                                                				  number to which calls are forwarded. Note Night
                                                      				service must also be configured. See Configure Call Coverage Features . | Note | Night
                                                      				service must also be configured. See Configure Call Coverage Features . |
| Note | Night
                                                      				service must also be configured. See Configure Call Coverage Features . |
| Step 12 | call-forward
                                                				  max-length length Example: Router(config-ephone-dn)# call-forward max-length 5 | (Optional)
                                             				Limits the number of digits that can be entered for a target number when using
                                             				the CfwdAll soft key on an IP phone. length —Number of
                                                				  digits that can be entered using the CfwdAll soft key on an IP phone. |
| Step 13 | no forward
                                                				  local-calls Example: Router(config-ephone-dn)# no forward local-calls | (Optional)
                                             				Specifies that local calls (calls from ephone-dns on the same Cisco Unified CME
                                             				system) will not be forwarded from this extension. If this
                                                   					 extension is busy, an internal caller hears a busy signal. If this
                                                   					 extension does not answer, the internal caller hears ringback. |
| Step 14 | end Example: Router(config-ephone-dn)# end | Returns to
                                             				privileged EXEC mode. |

| Note | After you
                                                      				use this command to specify a target number, the phone user can activate and
                                                      				cancel the call-forward-all state from the phone using the CFwdAll soft key or
                                                      				a feature access code (FAC). |
|---|---|

| Note | Night
                                                      				service must also be configured. See Configure Call Coverage Features . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-dn dn-tag [ dual-line ] Example: Router(config)# ephone-dn 20 | Enters
                                             				ephone-dn configuration mode, creates an ephone-dn, and optionally assigns it
                                             				dual-line status. dual-line —(Optional)
                                                				  Enables an ephone-dn with one voice port and two voice channels, which supports
                                                				  features such as call waiting, call transfer, and conferencing with a single
                                                				  ephone-dn. |
| Step 4 | transfer-mode { blind \| consult } Example: Router(config-ephone-dn)# transfer-mode blind | Specifies the type of call transfer for an individual directory number using the H.450.2 standard, allowing you to override
                                             the global setting. Default: system-level value set with the transfer-system command. |
| Step 5 | timeouts transfer-recall seconds Example: Router(config-ephone-dn)# timeouts transfer-recall 30 | (Optional)
                                             				Enables call-transfer recall and sets the number of seconds that
                                             				Cisco Unified CME waits before recalling a transferred call if the transfer-to
                                             				party does not answer or is busy. seconds —Duration, in seconds, to wait before
                                                   					 recalling a transferred call. Range: 1 to 1800. Default: 0 (disabled). This
                                                   					 command is supported in Cisco Unified CME 4.3 and later versions. This
                                                   					 command can also be configured in ephone-dn-template and telephony-service
                                                   					 configuration mode. |
| Step 6 | end Example: Router(config-ephone-dn)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-template template-tag Example: Router(config)# ephone-template 1 | Enters
                                             				ephone-template configuration mode. template-tag —Unique number that identifies this template
                                                   					 during configuration tasks. Range: 1 to 20. |
| Step 4 | transfer-pattern blocked Example: Router(config-ephone-template)# transfer-pattern blocked | (Optional)
                                             				Prevents directory numbers on the phone to which this template is applied from
                                             				transferring calls to patterns specified in the transfer-pattern (telephony-service) command. Note This
                                                      				command is also available in ephone configuration mode to block external
                                                      				transfers from individual phones without using a template. | Note | This
                                                      				command is also available in ephone configuration mode to block external
                                                      				transfers from individual phones without using a template. |
| Note | This
                                                      				command is also available in ephone configuration mode to block external
                                                      				transfers from individual phones without using a template. |
| Step 5 | transfer max-length digit-length Example: Router(config-ephone-template)# transfer max-length 8 | (Optional)
                                             				Specifies the maximum number of digits the user can dial when transferring a
                                             				call. digit-length —Number of digits allowed in a number to which a
                                                   					 call is being transferred. Range: 3 to 16. Default: 16. |
| Step 6 | exit Example: Router(config-ephone-template)# exit | Exits
                                             				ephone-template configuration mode. |
| Step 7 | ephone phone-tag Example: Router(config)# ephone 25 | Enters ephone
                                             				configuration mode. |
| Step 8 | ephone-template template-tag Example: Router(config-ephone)# ephone-template 1 | Applies a
                                             				template to a phone. template-tag —Template number that you want to apply to this
                                                   					 phone. |
| Step 9 | restart Example: Router(config-ephone)# restart | Performs a
                                             				fast reboot of this phone without contacting the DHCP server for updated
                                             				information. Repeat Step 6
                                             				to Step 9 for each phone on which you want to limit transfer capabilities. |
| Step 10 | end Example: Router(config-ephone)# end | Exits to
                                             				privileged EXEC mode. |

| Note | This
                                                      				command is also available in ephone configuration mode to block external
                                                      				transfers from individual phones without using a template. |
|---|---|

| Step 1 | Use the show
                                                				  running-config command to verify your configuration. Transfer
                                          			 method and patterns are listed in the telephony-service portion of the output.
                                          			 You can also use the show
                                                				  telephony-service command to display this information. Example: Router# show running-config !
telephony-service
fxo hook-flash
load 7910 P00403020214
load 7960-7940 P00305000600
load 7914 S00103020002
load 7905 CP7905040000SCCP040701A
max-ephones 100
max-dn 500
ip source-address 10.115.33.177 port 2000
max-redirect 20
no service directed-pickup
timeouts ringing 10
voicemail 7189
max-conferences 8 gain -6
moh music-on-hold.au
web admin system name cisco password cisco
dn-webedit
time-webedit
transfer-system full-consult
transfer-pattern 92......
transfer-pattern 91..........
transfer-pattern 93......
transfer-pattern 94......
transfer-pattern 95......
transfer-pattern 96......
transfer-pattern 97......
transfer-pattern 98......
transfer-pattern 99......
transfer-pattern .T
secondary-dialtone 9
!
create cnf-files version-stamp 7960 Jul 13 2004 03:39:28 |
|---|---|
| Step 2 | If you have
                                          			 used the transfer-mode command to override the global transfer mode for an
                                          			 individual ephone-dn, use the show
                                                				  running-config or show telephony-service
                                                				  ephone-dn command to verify that setting. Example: Router# show running-config !
ephone-dn 40 dual-line
number 451
description Main Number
huntstop channel
no huntstop
transfer-mode blind |
| Step 3 | Use the show telephony-service
                                                				  ephone-template command to view ephone-template configurations. |

| Restriction | Call transfer and conference restrictions apply when transfers or
                                             			 conferences are initiated toward external parties, like a PSTN trunk, a SIP
                                             			 trunk, or an H.323 trunk. The restrictions do not apply to transfers to local
                                             			 extensions. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters telephony-service configuration mode for configuring Cisco
                                             				Unified CME. |
| Step 4 | transfer-pattern transfer-pattern Example: Router(config-telephony)# transfer-pattern 1234... Router(config-telephony)# transfer-pattern 2468.. | Allows the transfer of calls from Cisco IP phones to specified
                                             				directory numbers of phones other than Cisco IP phones. transfer-pattern —String of digits
                                                   					 for permitted call transfers. Wildcards are allowed. A maximum of 32 transfer
                                                   					 patterns can be entered, using a separate command for each one. |
| Step 5 | exit Example: Router(config-telephony)# exit | Exits telephony-service configuration mode and enters global
                                             				configuration mode. |
| Step 6 | Enter one of the following commands: voice register pool pool-tag voice register template template-tag ephone phone tag ephone-template template-tag Example: Router(config)# voice register pool 25 | Enters voice register pool configuration mode and creates a pool configuration for a Cisco Unified SIP IP phone in Cisco Unified
                                             CME or for a set of Cisco Unified SIP IP phones in Cisco Unified SIP SRST. pool-tag —Unique number assigned to the pool. Range is 1 to 100. or Enters voice register template configuration mode and defines a template of common parameters for Cisco Unified SIP IP phones. template-tag —Declares a template tag. Range is 1 to 10. or Enters ephone configuration mode. phone-tag—Unique sequence number that identifies this ephone during configuration tasks. The maximum number of ephones is
                                                version and platform-specific. Type ? to display range. |
| Step 7 | transfer max-length max-length Example: Router(config-register-pool)# transfer max-length 7 | (Optional) Specifies the maximum length of the transfer number. max-length —Maximum length of the
                                                				  transfer number. Range is 3 to 16. |
| Step 8 | exit Example: Router(config-register-pool)# exit | Enters global configuration mode. |
| Step 9 | telephony-service Example: Router(config)# telephony-service | Enters telephony-service configuration mode for configuring Cisco
                                             				Unified CME. |
| Step 10 | conference transfer-pattern Example: Router(config-telephony)# conference transfer-pattern | Enables a Cisco Unified CME system to apply transfer patterns to a
                                             				conference call using conference softkeys or feature buttons. |
| Step 11 | end Example: Router(config-telephony)# end | Exits telephony-service configuration mode and enters privileged
                                             				EXEC mode. |

| Note | If both conference max-length and transfer
                                             			 max-length commands are configured, the conference max-length command takes precedence for
                                       		conferences. |
|---|---|

| Restriction | Call transfer
                                             			 restrictions apply when transfers are initiated toward external parties, like a
                                             			 PSTN trunk, a SIP trunk, or an H.323 trunk. The restrictions do not apply to
                                             			 transfers to local extensions. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | Enter one of the following commands: voice register pool pool-tag voice register template template-tag Example: Router(config)# voice register template 5 | Enters voice register pool configuration mode and creates a pool configuration for a Cisco Unified SIP IP phone in Cisco Unified
                                             CME or for a set of Cisco Unified SIP IP phones in Cisco Unified SIP SRST. pool-tag —Unique number assigned to the pool. Range is 1 to 100. Enters voice register template configuration mode and defines a template of common parameters for Cisco Unified SIP IP phones. template-tag —Declares a template tag. Range is 1 to 10. |
| Step 4 | transfer-pattern blocked Example: Router(config-register-temp)# transfer-pattern blocked | Blocks all
                                             				call transfers for a specific Cisco Unified SIP IP phone or a set of Cisco
                                             				Unified SIP IP phone. |
| Step 5 | end Example: Router(config-register-temp)# end | Exits voice
                                             				register template configuration mode and enters privileged EXEC mode. |

| Restriction | Cisco CME 3.0 and earlier versions do not support H.450.12. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice service voip Example: Router(config)# voice service voip | (Optional) Enters voice service configuration mode to establish
                                             				global call transfer and forwarding parameters. |
| Step 4 | supplementary-service h450.12 [ advertise-only ] Example: Router(conf-voi-serv)# supplementary-service h450.12 | (Optional) Enables H.450.12 supplementary services capabilities
                                             				globally for VoIP endpoints. This command enables call-by-call detection of H.450
                                                   					 capabilities when some endpoints in your mixed network are H.450-capable and
                                                   					 other endpoints are not. This command is disabled by default. advertise-only —(Optional) Advertises
                                                   					 H.450 capabilities to the remote end but does not require H.450.12 responses.
                                                   					 Use this keyword on Cisco CME 3.1 or later systems if you have a mixed network
                                                   					 containing Cisco CME 3.0 systems. This command is also used in dial-peer configuration mode to
                                             				affect an individual dial peer. |
| Step 5 | exit Example: Router(conf-voi-serv)# exit | (Optional) Exits voice-service configuration mode. |
| Step 6 | dial-peer voice tag voip Example: Router(config)# dial-peer voice 1 voip | (Optional) Enters dial-peer configuration mode. |
| Step 7 | supplementary-service h450.12 Example: Router(config-dial-peer)# supplementary-service h450.12 | (Optional) Enables H.450.12 supplementary services capabilities
                                             				for an individual dial peer. This command is disabled by default. This command is also used in voice-service configuration mode to
                                             				enable H.450.12 services globally. If this command is enabled globally and enabled on a dial
                                                   					 peer, the functionality is enabled for the dial peer. If this command is enabled globally and disabled on a dial
                                                   					 peer, the functionality is enabled for the dial peer. If this command is disabled globally and enabled on a dial
                                                   					 peer, the functionality is enabled for the dial peer. If this command is disabled globally and disabled on a dial
                                                   					 peer, the functionality is disabled for the dial peer. This is the default. |
| Step 8 | end Example: Router(config-dial-peer)# end | Returns to privileged EXEC mode. |

| Restriction | Codecs on
                                                   				  all the VoIP dial peers of the H.450 tandem gateway must be the same. Only one
                                                   				  codec type is supported in the VoIP network at a time, and there are only two
                                                   				  codec choices: G.711 (A-law or mu-law) or G.729. Transcoding
                                                   				  is not supported. Codec
                                                   				  renegotiation is not supported. For example, if an H.323 call that uses a G.729
                                                   				  codec is received by a Cisco Unified CME system and is forwarded to a
                                                   				  voice-mail system that requires a G.711 codec, the codec cannot be renegotiated
                                                   				  from G.729 to G.711. H.323-to-SIP
                                                   				  hairpin call routing is supported only with Cisco Unity Express. For more
                                                   				  information, see Integrating Cisco CallManager Express with
                                                      					 Cisco Unity Express . Cisco Unified Communications Manager must use a media
                                                   				  termination point (MTP), intercluster trunk (ICT) mode, and slow start. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice service voip Example: Router(config)# voice service voip | Enters voice
                                             				service configuration mode to establish global call transfer and forwarding
                                             				parameters. |
| Step 4 | allow-connections h323 to h323 Example: Router(conf-voi-serv)# allow-connections h323 to h323 | Enables
                                             				VoIP-to-VoIP call connections. Use the no form
                                             				of the command to disable VoIP-to-VoIP connections; this is the default. |
| Step 5 | end Example: Router(config-voi-serv)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 4 | call-forward pattern pattern Example: Router(config-telephony)# call-forward pattern 6000 | Specifies the
                                             				calling-party numbers for which to allow call forwarding with automatic
                                             				detection of whether H.450.3 is supported. If H.450.3 is supported, H.450.3 is
                                             				used for the forward and, if not, local hairpin is used. pattern —Digits to match for call forwarding. A pattern of .T
                                                   					 forwards all calling parties. |
| Step 5 | calling-number local Example: Router(config-telephony)# calling-number local | (Optional)
                                             				Replaces a calling-party number and name with the forwarding-party (local)
                                             				number and name for hairpin-forwarded calls only. Before
                                                				  Cisco CME 3.3, this command must be used with Tool Command Language (Tcl)
                                                				  script app-h450-transfer.2.0.0.7 or a later version. The local-hairpin
                                                				  attribute-value (AV) pair must be set to 1. |
| Step 6 | exit Example: Router(config-telephony)# exit | Exits
                                             				telephony-service configuration mode. |
| Step 7 | voice service voip Example: Router(config)# voice service voip | Enters
                                             				voice-service configuration mode. |
| Step 8 | allow connections from-type to to-type Example: Router(conf-voi-serv)# allow connections h323 to sip | Allows
                                             				connections between specific types of endpoints in a network. from-type —Originating endpoint type. Valid choices
                                                   					 are h323 and sip . to-type —Terminating endpoint type. Valid choices
                                                   					 are h323 and sip . |
| Step 9 | supplementary-service h450.3 Example: Router(conf-voi-serv)# no supplementary-service h450.3 | (Optional)
                                             				Enables H.450.3 supplementary services capabilities exchange globally. This is
                                             				the default. Use the no form
                                             				of this command to disable H.450.3 capabilities globally. This command can also
                                             				be used in dial-peer configuration mode to disable H.450.3 functionality for a
                                             				single dial peer. Note If this
                                                      				command is disabled globally and either enabled or disabled on a dial peer, the
                                                      				functionality is disabled for the dial peer. | Note | If this
                                                      				command is disabled globally and either enabled or disabled on a dial peer, the
                                                      				functionality is disabled for the dial peer. |
| Note | If this
                                                      				command is disabled globally and either enabled or disabled on a dial peer, the
                                                      				functionality is disabled for the dial peer. |
| Step 10 | end Example: Router(config-voi-serv)# end | Exits to
                                             				privileged EXEC mode. |

| Note | If this
                                                      				command is disabled globally and either enabled or disabled on a dial peer, the
                                                      				functionality is disabled for the dial peer. |
|---|---|

| Restriction | QSIG integration supports SCCP phones only. QSIG integration is exclusive; once QSIG integration is configured, QSIG transit node capability is disabled. There is no
                                                   dial-peer control to enable either transit or originate/terminate capability on a call by call basis. If you enable QSIG supplementary services at a system-level, you cannot disable the capability on individual dial peers. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                				  password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice service voip Example: Router(config)# voice service voip | Enters VoIP
                                             				voice-service configuration mode to define global call transfer and forwarding
                                             				parameters. |
| Step 4 | supplementary-service h450.7 Example: Router(config-voi-serv)# supplementary-service h450.7 | Enables
                                             				H.450.7 supplementary services capabilities exchange at a system-level. |
| Step 5 | qsig decode Example: Router(config-voi-serv)# qsig decode | Enables
                                             				decoding for QSIG supplementary services. |
| Step 6 | exit Example: Router(config-voi-serv)# exit | Exits VoIP
                                             				voice-service configuration mode. |
| Step 7 | voice service pots Example: Router(config)# voice service pots | Enters POTS
                                             				voice-service configuration mode to define global call transfer and forwarding
                                             				parameters. |
| Step 8 | supplementary-service qsig call-forward Example: Router(config-voi-serv)# supplementary-service qsig call-forward | Enables QSIG
                                             				call-forwarding supplementary services (ISO 13873) to forward calls to another
                                             				number. |
| Step 9 | end Example: Router(config-voi-serv)# end | Exits to
                                             				privileged EXEC mode. |

| Restriction | QSIG
                                                   				  integration supports SCCP phones only. QSIG
                                                   				  integration is exclusive; once QSIG integration is configured, QSIG transit
                                                   				  node capability is disabled. There is no dial-peer control to enable either
                                                   				  transit or originate/terminate capability on a call by call basis. If you
                                                   				  enable QSIG supplementary services at a system-level, you cannot enable or
                                                   				  disable the capability on individual dial peers. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice service voip Example: Router(config)# voice service voip | Enters VoIP
                                             				voice-service configuration mode to define global call transfer and forwarding
                                             				parameters. |
| Step 4 | qsig decode Example: Router(config-voi-serv)# qsig decode | Enables
                                             				decoding for QSIG supplementary services. |
| Step 5 | exit Example: Router(config-voi-serv)# exit | Exits VoIP
                                             				voice-service configuration mode. |
| Step 6 | dial-peer voice tag voip Example: Router(config)# dial-peer voice 1 voip | Enters
                                             				dial-peer configuration mode to define parameters for an individual dial peer. |
| Step 7 | supplementary-service h450.7 Example: Router(config-dial-peer)# supplementary-service h450.7 | Enables
                                             				H.450.7 supplementary services capabilities exchange on a single dial peer. |
| Step 8 | exit Example: Router(config-dial-peer)# exit | Exits
                                             				dial-peer configuration mode. |
| Step 9 | dial-peer voice tag pots Example: Router(config)# dial-peer voice 2 pots | Enters
                                             				dial-peer configuration mode to define parameters for an individual dial peer. |
| Step 10 | supplementary-service qsig call-forward Example: Router(config-dial-peer)# supplementary-service qsig call-forward | Enables QSIG
                                             				call-forwarding supplementary services (ISO 13873) to forward calls to another
                                             				number. |
| Step 11 | end Example: Router(config-dial-peer)# end | Exits to
                                             				privileged EXEC mode. |

| Restriction | In
                                                   				  Cisco Unified CME 4.2 and 4.3, when the supplementary-service sip
                                                         						refer command is enabled (default) and both the caller being
                                                   				  transferred (transferee) and the phone making the transfer (transferor) are
                                                   				  SIP, but the transfer-to phone is SCCP, Cisco Unified CME hairpins the call to
                                                   				  the transfer-to phone after receiving the REFER request from transferor instead
                                                   				  of sending the REFER request to the transferee. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | Enter one of the following commands: voice service voip dial-peer voice tag voip Example: Router(config)# voice service voip or Router(config)# dial-peer voice 99 voip | Enters voice-service configuration mode to set global parameters for VoIP features. or Enters dial peer configuration mode to set parameters for a specific dial peer. |
| Step 4 | no supplementary-service sip moved-temporarily Example: Router(conf-voi-serv)# no supplementary-service sip moved-temporarily or Router(config-dial-peer)# no supplementary-service sip moved-temporarily | Disables SIP
                                             				redirect response for call forwarding either globally or for a dial peer. Sending
                                             				redirect message to the destination is the default behavior. |
| Step 5 | no supplementary-service sip refer Example: Router(conf-voi-serv)# no supplementary-service sip refer or Router(config-dial-peer)# no supplementary-service sip refer | Disables SIP
                                             				REFER message for call transfers either globally or for a dial peer. Sending REFER
                                             				message to the destination is the default behavior. |
| Step 6 | end Example: Router(config-voi-serv)# end or Router(config-dial-peer)# end | Exits to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                                				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                                				configuration mode. |
| Step 3 | voice service voip Example: Router(config)# voice service voip | Enters
                                                				voice-service configuration mode to establish global parameters. |
| Step 4 | h323 Example: Router(conf-voi-serv)# h323 | Enters H.323
                                                				voice-service configuration mode. |
| Step 5 | telephony-service ccm-compatible Example: Router(conf-serv-h323)# telephony-service ccm-compatible | (Optional)
                                                				Globally enables a Cisco CME 3.1 or later system to detect
                                                				Cisco Unified Communications Manager and exchange calls with it. This is the
                                                				default configuration. Use the no form of this command to disable Cisco Unified Communications Manager detection
                                                      					 and exchange. We do not recommend using the no form of the command. Using this
                                                      					 command in an H.323 voice class definition allows you to specify this behavior
                                                      					 for an individual dial peer. |
| Step 6 | h225 h245-address on-connect Example: Router(conf-serv-h323)# h225 h245-address on-connect | (Optional)
                                                				Globally enables a delay for the H.225 message exchange of an H.245 transport
                                                				address until a call is connected. The delay allows
                                                				Cisco Unified Communications Manager to generate local ringback for calls to
                                                				Cisco Unified CME phones. This is the default configuration. The no form of this command disables the delay. We do not recommend using the no form of the command. Using this
                                                      					 command in an H.323 voice class definition allows you to specify this behavior
                                                      					 for an individual dial peer. |
| Step 7 | exit Example: Router(conf-serv-h323)# exit | Exits H.323
                                                				voice-service configuration mode. |
| Step 8 | supplementary-service h225-notify cid-update Example: Router(conf-voi-serv)# supplementary-service h225-notify cid-update | (Optional)
                                                				Globally enables H.225 messages with caller-ID updates to be sent to
                                                				Cisco Unified Communications Manager. This is the default configuration. The no form of the command disables caller-ID update. We do not recommend using the no form of the command. This command
                                                				is also used in dial-peer configuration mode to affect a single dial peer. If this
                                                      					 command is enabled globally and enabled on a dial peer, the functionality is
                                                      					 enabled for that dial peer. This is the default. If this
                                                      					 command is enabled globally and disabled on a dial peer, the functionality is
                                                      					 disabled for that dial peer. If this
                                                      					 command is disabled globally and either enabled or disabled on a dial peer, the
                                                      					 functionality is disabled for that dial peer. |
| Step 9 | exit Example: Router(config-voice-service)# exit | Exits
                                                				voice-service configuration mode. |
| Step 10 | voice class h323 tag Example: Router(config)# voice class h323 48 | (Optional)
                                                				Creates a voice class that contains commands to be applied to one or more dial
                                                				peers. |
| Step 11 | telephony-service
                                                   				  ccm-compatible Example: Router(config-voice-class)# telephony-service ccm-compatible | (Optional)
                                                				Enables the dial peer to exchange calls with a
                                                				Cisco Unified Communications Manager system when this voice class is applied to
                                                				a dial peer. This is the default configuration. The no form of the command disables call exchange with
                                                      					 Cisco Unified Communications Manager. We do not recommend using the no form of the command. |
| Step 12 | h225 h245-address
                                                   				  on-connect Example: Router(config-voice-class)# h225 h245-address on-connect | (Optional)
                                                				Enables the calls that use this dial peer to delay the exchange of H.225
                                                				messages that contain the H.245 transport address until calls are connected,
                                                				when this voice class is applied to a dial peer. The delay allows the playing
                                                				of local ringback for calls from Cisco Unified Communications Manager. This is
                                                				the default configuration. The no form of this command disables the delay. We do not recommend using the no form of the command. |
| Step 13 | exit Example: Router(config-voice-class)# exit | Exits
                                                				voice-class configuration mode. |
| Step 14 | dial-peer
                                                   				  voice tag voip Example: Router(config)# dial-peer voice 28 voip | (Optional)
                                                				Enters dial-peer configuration mode to set parameters for an individual dial
                                                				peer. |
| Step 15 | supplementary-service
                                                   				  h225-notify cid-update Example: Router(config-dial-peer)# no supplementary-service h225-notify cid-update | (Optional)
                                                				Enables H.225 messages with caller-ID updates to
                                                				Cisco Unified Communications Manager for a specific dial peer. This is the
                                                				default configuration. The no form of the command disables caller-ID updates. We do not recommend using the no form of the command. |
| Step 16 | voice-class
                                                   				  h323 tag Example: Router(config-dial-peer)# voice-class h323 48 | (Optional)
                                                				Applies the previously defined voice class with the specified tag number to
                                                				this dial peer. |
| Step 17 | end Example: Router(config-dial-peer)# end | Exits to
                                                				privileged EXEC mode. |

| Step 1 | Set
                                             			 Cisco Unified Communications Manager service parameters. From
                                             			 Cisco Unified Communications Manager Administration, choose Service Parameters.
                                             			 Choose the Cisco Unified Communications Manager service, and make the following
                                             			 settings: Set the
                                                      					 H323 FastStart Inbound service parameter to False. Set the
                                                      					 Send H225 User Info Message service parameter to H225 Info for Ring Back. |
|---|---|
| Step 2 | Configure
                                             			 Cisco Unified CME as an ICT in the Cisco Unified Communications Manager
                                             			 network. For information about different intercluster trunk types and
                                             			 configuration instructions, see Cisco Unified Communications Manager
                                                				documentation . |
| Step 3 | Ensure that
                                             			 the Cisco Unified Communications Manager network uses an MTP. The MTP is
                                             			 required to provide DSP resources for transcoding and for sending and receiving
                                             			 G.729 calls to Cisco Unified CME. All media streams between
                                             			 Cisco Unified Communications Manager and Cisco Unified CME must pass through
                                             			 the MTP because Cisco CME  3.1 does not support transcoding. For more
                                             			 information, see Cisco Unified Communications Manager
                                                				documentation . |
| Step 4 | Set up dial
                                             			 peers to establish routing using the instructions in the Dial Peer
                                             			 Configuration on Voice Gateway Routers guide. |

| Step 1 | If you
                                             			 encounter lack of ringback on direct calls from a
                                             			 Cisco Unified Communications Manager phone to an IP phone on a
                                             			 Cisco Unified CME system, check the show
                                                   				  running-config command output to ensure that the following two
                                             			 commands do not appear: no h225 h245-address
                                                   				  on-connect and no telephony-service
                                                   				  ccm-compatible . These commands should be enabled, which is their
                                             			 default state. |
|---|---|
| Step 2 | Use the debug h225
                                                   				  asn1 command to display the H.323 messages that are sent from the
                                             			 Cisco Unified CME system to the Cisco Unified Communications Manager system to
                                             			 see if the H.245 address is being sent too early. |
| Step 3 | For calls that
                                             			 are routed using VoIP-to-VoIP connections, use the show voip rtp connections
                                                   				  detail command to display the call identification number, IP
                                             			 addresses, and port numbers involved for all VoIP call legs. This command
                                             			 includes VoIP-to-POTS and VoIP-to-VoIP call legs. The following is sample
                                             			 output for this command: Router# show voip rtp connections detail VoIP RTP active connections :
No. CallId  dstCallId  LocalRTP   RmtRTP   LocalIP    			 	RemoteIP
1   7       8          16586      22346   172.27.82.2     172.29.82.2
2   8       7          17010      16590   172.27.82.2     209.165.202.129

Found 2 active RTP connections |
| Step 4 | Use the show call prompt-mem-usage
                                                   				  detail command to see information on ringback tone
                                             			 generation that uses the interactive voice response (IVR) prompt playback
                                             			 mechanism. This ringback is needed for hairpin transfers that are committed
                                             			 during the alerting-of-the-transfer-destination phase of the call and for calls
                                             			 to destinations that do not provide in-band ringback tone, such as IP phones
                                             			 (FXS analog ports do provide in-band ringback tone). Ringback tone is played to
                                             			 the transferred party by the Cisco Unified CME system that performs the
                                             			 transfer (the system attached to the transferring party). The system
                                             			 automatically generates tone prompts as needed based on the network-locale
                                             			 setting for the Cisco Unified CME system. If you are not
                                                				getting ringback tone when you should, use the show call
                                                      					 prompt-mem-usage command to ensure that the correct prompt is
                                                				loaded and playing. The following sample output indicates that a prompt is
                                                				playing (“Number of prompts playing”) and indicates the country code used for
                                                				the prompt (GB for Great Britain) and the codec. Router# show call prompt-mem-usage detail Prompt memory usage:

 config'd   wait  active  free   mc    total    ms      total
file(s) 0200 0001 -001 00200 00001 00002
memory 02097152 00003000 00000000 02094152 00003000
Prompt load counts: (counters reset 0)
success 0(1st try) 0(2nd try), failure 0
Other mem block usage:
mcDynamic mcReader
gauge 00001 00001
Number of prompts playing: 1
Number of start delays : 0
MCs in the ivr MC sharing table
===============================
Media Content: NoPrompt (0x83C64554)
URL:
cid=0, status=MC_READY size=24184 coding=g711ulaw refCount=0
Media Content: tone://GB_g729_tone_ringback (0x83266EC8)
URL: tone://GB_g729_tone_ringback |

| Restriction | SIP-to-SIP
                                                   				  call forwarding is invoked only if that phone is dialed directly. Call
                                                   				  forwarding is not invoked when the phone number is called through a sequential,
                                                   				  longest-idle, or peer hunt group. If call
                                                   				  forwarding is configured for a hunt group member, call forward is ignored by
                                                   				  the hunt group. In
                                                   				  Cisco Unified CME 4.1 and later versions, Call Forward All requires SIP phones
                                                   				  to be configured with a directory number (using dn keyword in number command); direct line numbers are not supported. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register dn dn-tag Example: Router(config)# voice register dn 1 | Enters voice
                                             				register dn mode to define a directory number for a SIP phone, intercom line,
                                             				voice port, or an MWI. |
| Step 4 | call-forward b2bua all directory-
                                                				  number Example: Router(config-register-dn)# call-forward b2bua all 5005 | Enables call
                                             				forwarding for a SIP back-to-back user agent so that all incoming calls will be
                                             				forwarded to the designated directory-number. In
                                                   					 Cisco CME 3.4 and Cisco Unified CME 4.0, this command is also available in
                                                   					 voice register pool configuration mode. The configuration under voice register
                                                   					 dn takes precedence over the configuration under voice register pool. If the call-forward b2bua
                                                         						  all command is configured in voice register pool configuration
                                                   					 mode, it applies to all directory numbers on the phone. |
| Step 5 | call-forward b2bua busy directory-
                                                				  number Example: Router(config-register-dn)# call-forward b2bua busy 5006 | Enables call
                                             				forwarding for a SIP back-to-back user agent so that incoming calls to an
                                             				extension that is busy will be forwarded to the designated directory number. In Cisco CME 3.4 and
                                                				  Cisco Unified CME 4.0, this command is also available in voice register pool
                                                				  configuration mode. The configuration under voice register dn takes precedence
                                                				  over the configuration under voice register pool. |
| Step 6 | call-forward b2bua mailbox directory-
                                                				  number Example: Router(config-register-dn)# call-forward b2bua mailbox 5007 | Enables call
                                             				forwarding for a SIP back-to-back user agent so that incoming calls that have
                                             				been forwarded to a busy or no-answer extension will be forwarded to the
                                             				recipient’s voice mail. In Cisco CME 3.4 and
                                                				  Cisco Unified CME 4.0, this command is also available in voice register pool
                                                				  configuration mode. The configuration under voice register dn takes precedence
                                                				  over the configuration under voice register pool. |
| Step 7 | call-forward b2bua night-service directory- number Example: Router(config-register-dn)# call-forward b2bua night-service 5007 | Enables call forwarding for a SIP back-to-back user agent so that
                                             				incoming calls that have been forwarded to a busy or no-answer extension will
                                             				be forwarded to the recipient’s voice mail. In Cisco CME 3.4 and
                                                				  Cisco Unified CME 4.0, this command is also available in voice register pool
                                                				  configuration mode. The configuration under voice register dn takes precedence
                                                				  over the configuration under voice register pool. |
| Step 8 | call-forward b2bua noan directory- number timeout seconds Example: Router(config-register-dn)# call-forward b2bua noan 5010 timeout 10 or Router(config-register-pool)# call-forward b2bua noan 5010 timeout 10 | Enables call
                                             				forwarding for a SIP back-to-back user agent so that incoming calls to an
                                             				extension that does not answer will be forwarded to the designated directory
                                             				number. In
                                                   					 Cisco CME 3.4 and Cisco Unified CME 4.0, this command is also available in
                                                   					 voice register pool configuration mode. The configuration under voice register
                                                   					 dn takes precedence over the configuration under voice register pool. timeout seconds —Duration that a call can ring before it is
                                                   					 forwarded to the destination directory number. Range: 3 to 60000. Default: 20. |
| Step 9 | call-forward b2bua unreachable directory-
                                                				  number Example: Router(config-register-dn)# call-forward b2bua unreachable 5009 or Router(config-register-pool)# call-forward b2bua unreachable 5009 | (Optional)
                                             				Enables call forwarding for a SIP back-to-back user agent so that calls can be
                                             				forwarded to a phone that has not registered in Cisco Unified CME. Target
                                                   					 directory-number must be configured in Cisco Unified CME. In
                                                   					 Cisco CME 3.4 and Cisco Unified CME 4.0, this command is also available in
                                                   					 voice register pool configuration mode. The configuration under voice register
                                                   					 dn takes precedence over the configuration under voice register pool. This
                                                   					 command was removed in Cisco Unified CME 4.1. |
| Step 10 | end Example: Router(config-register-dn)# end | Exits to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice register dn tag Example: Router(config)#voice register dn 20 | Enters voice register dn mode to define a directory number for a
                                             				SIP phone, intercom line, voice port, or an MWI. |
| Step 4 | call-forward b2bua unregistered directory-number Example: Router(config-register-dn)#call-forward b2bua unregistered 2345 | Enables call forwarding for a SIP back-to-back user agent so that
                                             				all incoming calls are forwarded to the unregistered directory-number. |
| Step 5 | end Example: Router(config-ephone)# end | Returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router# enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice service voip Example: Router(conf)# voice service voip | Enters
                                             				voice-service configuration mode and specifies voice-over-IP encapsulation. |
| Step 4 | sip Example: Router(conf-serv)# sip | Enters SIP
                                             				configuration mode. |
| Step 5 | registrar server [ expires [ max seconds ] [ min seconds ] ] Example: Router(conf-serv-sip)# registrar server expires max 250 min 75 | Enables SIP
                                             				registrar functionality in Cisco Unified CME. expires—(Optional) Sets the active time for an incoming
                                                   					 registration. max
                                                   					 sec—(Optional) Maximum time for a registration to expire, in seconds. Range:
                                                   					 120 to 86400. min
                                                   					 sec—(Optional) Minimum time for a registration to expire, in seconds. |
| Step 6 | end Example: Router (conf-serv-sip)# end | Returns to
                                             				privileged EXEC mode. |

| Restriction | This feature is supported
                                                				only on Cisco Unified IP Phone 7911G, 7941G, 7941GE, 7961G, 7961GE, 7970G, and
                                                				7971GE. If a user enables Call
                                                				Forward All using the CfwdAll softkey, it is enabled on the primary line. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router# enable | Enables
                                             				privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register global Example: Router(config)# voice register global | Enters voice
                                             				register global configuration mode to set global parameters for all supported
                                             				SIP phones in a Cisco Unified CME environment. |
| Step 4 | call-feature-uri cfwdall service-uri Example: Router(config-register-global)# call-feature-uri cfwdall http://1.4.212.11/cfwdall | Specifies the
                                             				URI for soft keys on SIP phones connected to a Cisco Unified CME router. |
| Step 5 | end Example: Router(config-register-global)# end | Exits to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router# enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register global Example: Router(config)# voice register global | Enters voice
                                             				register global configuration mode to set parameters for all supported SIP
                                             				phones in Cisco Unified CME. |
| Step 4 | phone-redirect-limit number Example: Router(config-register-global)# phone-redirect-limit 8 | Changes the
                                             				default number of 3XX responses a SIP phone that originates a call can handle
                                             				for a single call. Default: 5 |
| Step 5 | end Example: Router(config-register-global)# end | Exits to
                                             				privileged EXEC mode. |

| Restriction | Blind transfer is not supported on certain phones such as Cisco Unified IP Phone 7911G, 7941G, 7941GE, 7961G, 7961GE, 7970G,
                                                   or 7971GE. In Cisco Unified CME 4.1, the soft key display can be customized only for certain IP phones, such as Cisco Unified IP Phone 7911G,
                                                   7941G, 7941GE, 7961G, 7961GE, 7970G, and 7971GE. For configuration information, see Modify Softkey Display on SIP Phone . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router# enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register template template-tag Example: Router(config)# voice register template 1 | Enters voice
                                             				register template configuration mode to define a template of common parameters
                                             				for SIP phones in Cisco Unified CME. Range: 1 to 5 |
| Step 4 | transfer-attended Example: Router(config-register-template)# transfer-attended | Enable a soft
                                             				key for attended transfer on any supported SIP phone that uses a template in
                                             				which this command is configure. |
| Step 5 | transfer-blind Example: Router(config-register-template)# transfer-blind | Enable a soft
                                             				key for blind transfer on any supported SIP phone that uses a template in which
                                             				this command is configure. |
| Step 6 | exit Example: Router(config-register-template)# exit | Exits
                                             				configuration mode to the next highest mode in the configuration mode
                                             				hierarchy. |
| Step 7 | voice register pool pool-tag Example: Router(config)# voice register pool 3 | Enters voice
                                             				register pool configuration mode to set phone-specific parameters for SIP
                                             				phones. |
| Step 8 | template template-tag Example: Router(config-register-pool)# voice register pool 1 | Applies a
                                             				template created with the voice register
                                                   					 template command. template-tag —Range: 1 to 5 |
| Step 9 | end Example: Router(config-register-pool)# end | Exits to
                                             				privileged EXEC mode. |

| Feature
                                       				  Name | Cisco Unified CME Version | Feature
                                       				  Information |
|---|---|---|
| Calling Number Local | 12.0 | Introduced support to configure Calling Number Local feature for
                                       				  Voice Register DNs. |
| Call
                                       				  Transfer Recall on SIP Phones | 11.6 | Call
                                       				  Transfer Recall feature returns a transferred call to the phone that initiated
                                       				  the transfer if the destination is busy or does not answer. |
| Trunk-to-Trunk Transfer Blocking for Toll Fraud Prevention on
                                       				  Cisco Unified SIP IP Phones | 9.5 | Introduced
                                       				  support Trunk-to-Trunk Transfer Blocking for Toll Fraud Prevention on Cisco
                                       				  Unified SIP IP Phones. |
| Call
                                       				  Forwarding | 4.1 | Call
                                             						Forward All synchronization between Cisco Unified CME and SIP phones was added. Disabling SIP supplementary services for call forward and call
                                             						transfer was added. |
| 4.0 | Automatic call forwarding during night service was introduced. Selective call forwarding was introduced. Forwarding of local (internal) calls can be blocked. H.450.7 standards support and QSIG supplementary services
                                             						capability was introduced. |
| 3.4 | Calls into
                                       				  a SIP device can be forwarded to other SIP or SCCP devices including
                                       				  Cisco Unity, third- party voice mail systems, or an auto-attendant (AA) or
                                       				  other interactive voice response (IVR) devices. SCCP devices may also be
                                       				  forwarded to SIP devices. |
| 3.1 | Number
                                             						of digits that can be entered using the CfwdALL (call-forward all) soft key can
                                             						be limited. H.450.12 standards support, which provide dynamic detection of
                                             						H.450.2 and H.450.3 capabilities on a call-by-call basis, was introduced. |
| 3.0 | CFwdALL soft key was introduced. Local
                                             						hairpin call routing was supported as an option for networks that cannot
                                             						support H.450 call transfer and forwarding. This feature requires installation
                                             						of the Tcl script app_h450_transfer.2.0.0.8.tcl or a later version. |
| 2.1 | Call
                                       				  forwarding using the H.450.3 standard was introduced. |
| 1.0 | Call
                                       				  forwarding for all calls, busy conditions, and no-answer conditions was
                                       				  introduced, using a Cisco-proprietary method. |
| Call
                                       				  Forward Unregistered | 8.6 | The Call
                                       				  Forward Unregistered (CFU) feature was introduced for SIP phones. |
| Call
                                       				  Transfer | 4.3 | Call-Transfer Recall was added. Consultative Call Transfer digit-collection process was
                                             						modified. |
| 4.1 | Disabling SIP supplementary services for call transfer and call
                                             						forward was added. |
| 4.0 | Default for the transfer-system command was changed from the blind keyword to the full-consult keyword. Transfers to phones outside the Cisco Unified CME system can be
                                             						blocked for individual ephones. Number
                                             						of digits in transfer destination numbers can be limited. |
| 3.4 | Support
                                       				  for attended and blind transfer s using SIP IP phone directly connected to
                                       				  Cisco CME. |
| 3.2 | Consultative transfer to monitored lines using direct station
                                             						select was introduced. Transcoding between G.711 and G.729 is supported when one leg of
                                             						a Voice over IP (VoIP)-to-VoIP hairpin call uses G.711 and the other leg uses
                                             						G.729. |
| 3.1 | Support
                                       				  was introduced for the following: Enhancements for VoIP networks which contain a mix of platforms
                                             						that support H.450.2 and H.450.3 standards, such as Cisco CME 3.1,
                                             						Cisco CME 3.0, Cisco ITS V2.1, and platforms that do not support H.450.2 and
                                             						H.450.3 standards, such as Cisco Unified Communications Manager, Cisco BTS
                                             						Softswitch (BTS), and Cisco PSTN Gateway (PGW). H.450.12 standards, which provide dynamic detection of H.450.2
                                             						and H.450.3 capabilities on a call-by-call basis. Automatic detection of Cisco Unified Communications Manager
                                             						endpoints. Hairpin VoIP-to-VoIP call routing and routing to an H.450 tandem
                                             						gateway. Hairpin call routing does not require a Tcl script. |
| 3.0 | Local
                                       				  hairpin call routing was supported as an option for networks that cannot
                                       				  support H.450 call transfer and forwarding. This feature requires installation
                                       				  of the Tcl script app_h450_transfer.2.0.0.8.tcl or a later version. |
| 2.1 | Consultative transfer using the ITU-T H.450.2 standard was
                                       				  introduced. |
| 1.0 | Call
                                       				  transfer was introduced, using a Cisco proprietary method. |