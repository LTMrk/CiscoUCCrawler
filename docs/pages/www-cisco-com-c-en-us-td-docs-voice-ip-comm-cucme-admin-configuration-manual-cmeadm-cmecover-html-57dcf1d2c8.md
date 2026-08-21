---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmecover-html-57dcf1d2c8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmecover.html
retrieved_at: 2026-08-21T07:25:02.477875+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Call Coverage Features

## Chapter: Call Coverage Features

# Call Coverage Features

## Information About Call Coverage Features

### Call Coverage
                           	 Summary

Call coverage
                              		features are used to ensure that all incoming calls to Cisco Unified CME are
                              		answered by someone, regardless of whether the called number is busy or does
                              		not answer.

Some
                              		single-dialed-number call coverage features, such as hunt groups, can send
                              		incoming calls to a single extension to a pool of phone agents, while other
                              		features, such as call hunt, call waiting, and call forwarding increase the
                              		chance of a call being answered by giving it another chance for a connection if
                              		the dialed number is not available.

Multiple-dialed-number call coverage features, such as call
                              		pickup, night service, and overlaid directory numbers, provide different ways
                              		for one person to answer incoming calls to multiple numbers.

Any of the call
                              		coverage features can be combined with other call coverage features and with
                              		shared lines and secondary numbers to design the call coverage plan that is
                              		best suited to your needs.

Table 1 summarizes call coverage features.

Feature

Description

Example

How Configured

Call Forwarding

Calls are automatically diverted to a designated number on busy, no answer, all calls, or only during night-service hours.

Extension 3444 is configured to send calls to extension 3555 when it is busy or does not answer.

Enable Call Forwarding for a Directory Number

or

Configure SIP-to-SIP Phone Call Forwarding

Call Hunt

System automatically searches for an available directory number from a matching group of directory numbers until the call
                                          is answered or the hunt is stopped.

Three ephone-dns have the same extension number, 755. One is on the manager’s phone and the others are on the assistants’
                                          phones. Preference and huntstop are used to make sure that calls always come to the manager’s phone first but if they can’t
                                          be answered, they will ring on the first assistant’s phone and if not answered, on the second assistant’s phone.

Configure Call Hunt on SCCP Phones

or

Configure Call Hunt on SIP Phones

Call Pickup

Calls to unstaffed phones can be answered by other phone users using a soft key or by dialing a short code.

Extension 201 and 202 are both in pickup group 22. A call is received by 201, but no one is there to answer. The agent at
                                          202 presses the GPickUp soft key to answer the call.

Enable Call Pickup

Call Waiting

Calls to busy numbers are presented to phone users, giving them the option to answer them or let them be forwarded.

Extension 564 is in conversation when a call-waiting beep is heard. The phone display shows the call is from extension 568
                                          and the phone user decides to let the call go to voice mail.

Configure Call-Waiting Indicator Tone on SCCP Phone

or

Enable Call Waiting on SIP Phones

Cisco CME B-ACD

Calls to a pilot number are automatically answered by an interactive application that presents callers with a menu of choices
                                          before sending them to a queue for a hunt group.

The DID number 555-0125 is the pilot number for the XYZ Company. Incoming calls to this pilot number hear a menu of choices;
                                          they can press 1 for sales, 2 for service, or 3 to leave a message. The call is forwarded appropriately when callers make
                                          a choice.

See Cisco Unified CME B-ACD and Tcl Call-Handling Applications.

Hunt Groups

Calls are forwarded through a pool of agents until answered or sent to a final number.

Extension 200 is a pilot number for the sales department. Extensions 213, 214, and 215 belong to sales agents in the hunt
                                          group. When a call to extension 200 is received, it proceeds through the list of agents until one answers. If all the agents
                                          are busy or do not answer, the call is sent to voice mail.

Configure Ephone-Hunt Groups on SCCP Phones

or

Configure Voice-Hunt Groups

Night Service

Calls to ephone-dns and voice register dns that are not staffed during certain hours can be answered by other phones using
                                          call pickup.

Extension 7544 is the cashier’s desk but the cashier only works until 3 p.m. A call is received at 4:30 p.m. and the service
                                          manager’s phone is notified. The service manager uses call pickup to answer the call.

Configure Night Service on SCCP Phones

Configure Night Service on SIP Phones

Overlaid Ephone-dns

Calls to several numbers can be answered by a single agent or multiple agents.

Extensions 451, 452, and 453 all appear on button 1 of a phone. A call to any of these numbers can be answered from button
                                          1.

Configure Overlaid Ephone-dns on SCCP Phones .

### Out-of- Dialog
                           	 REFER

Out-of-dialog REFER
                              		(OOD-R) allows remote applications to establish calls by sending a REFER
                              		message to Cisco Unified CME without an initial INVITE. After the REFER is
                              		sent, the remainder of the call setup is independent of the application and the
                              		media stream does not flow through the application. The application using OOD-R
                              		triggers a call setup request that specifies the Referee address in the
                              		Request-URI and the Refer-Target in the Refer-To header. The SIP messaging used
                              		to communicate with Cisco Unified CME is independent of the end-user device
                              		protocol which can be SIP, SCCP, H.323, or POTS. Click-to-dial is an example of
                              		an application that can be created using OOD-R.

A click-to-dial
                              		application allows users to combine multiple steps into one click for a call
                              		setup. For example, a user can click a web-based directory application from
                              		their PC to look up a telephone number, off-hook their desktop phone, and dial
                              		the called number. The application initiates the call setup without the user
                              		having to out-dial from their own phone. The directory application sends a
                              		REFER message to Cisco Unified CME which sets up the call between both parties
                              		based on this REFER.

Click-to-Dial
                                 		  Application using Out-of-Dialog REFER shows an example of OOD-R being used by a click-to-dial application. In this
                              		scenario, the following events occur (refer to the event numbers in the
                              		illustration):

Remote user
                                    			 clicks to dial.

Application
                                    			 sends out-of-dialog REFER to Cisco Unified CME 1.

Cisco Unified
                                    			 CME 1 connects to SIP phone 1 (Referee).

Cisco Unified
                                    			 CME 1 sends INVITE to Cisco Unified CME 2.

Cisco Unified
                                    			 CME 2 sends INVITE to SIP phone 2 (Refer-Target) and the call is accepted.

Voice path is
                                    			 created between the two SIP phones.

The initial OOD-R
                              		request can be authenticated and authorized using RFC 2617-based digest
                              		authentication. To support authentication, Cisco Unified CME retrieves the
                              		credential information from a text file stored in flash. This mechanism is used
                              		by Cisco Unified CME in addition to phone-based credentials. The same
                              		credential file can be shared by other services that require request-based
                              		authentication and authorization such as presence service. Up to five
                              		credential files can be configured and loaded into the system. The contents of
                              		these five files are mutually exclusive, meaning the username and password
                              		pairs must be unique across all the files. The username and password pairs must
                              		also be different than those configured for SCCP or SIP phones in a
                              		Cisco Unified CME system.

For configuration
                              		information, see Enable Out-Of-Dialog REFER .

### Call Hunt

Call hunt allows you
                              		to use multiple directory numbers to provide coverage for a single called
                              		number. You do this by assigning the same number to several primary or
                              		secondary ephone-dns or by using wildcards in the number associated with the
                              		directory numbers.

Calls are routed
                              		based on a match between the number dialed and the destination patterns that
                              		are associated with dial peers. Through the use of wildcards in destination
                              		patterns, multiple dial peers can match a particular called number. Call hunt
                              		is the ability to search through the dial peers that match the called number
                              		until the call is answered. Call hunt uses a technique called preference to
                              		control the order in which dial peers are matched to an incoming call and a
                              		technique called huntstop to determine when the search for another matching
                              		peer ends.

In
                              		Cisco Unified CME, incoming calls search through the virtual dial peers that
                              		are automatically created when you define directory numbers. These virtual dial
                              		peers are not directly configurable; you must configure the directory number to
                              		control call hunt for virtual dial peers.

Channel huntstop is
                              		used to stop the search for the two channels of a dual-line directory number.
                              		Channel huntstop keeps incoming calls from hunting to the second channel if the
                              		first channel is busy or does not answer. This keeps the second channel free
                              		for call transfer, call waiting, or three-way conferencing.

Huntstop prevents
                              		hunt-on-busy from redirecting a call from a busy phone into a dial peer that
                              		has been setup with a catch-all default destination.

For configuration
                              		information, see Configure Call Hunt on SCCP Phones or Configure Call Hunt on SIP Phones .

### Call
                           	 Pickup

Call Pickup allows a
                              		phone user to answer a call that is ringing on another phone. Cisco Unified
                              		CME 7.1 introduces Call Pickup features for SIP phones. SCCP phones support
                              		three types of Call Pickup:

Directed Call
                                    			 Pickup—Call pickup, explicit ringing extension. Any local phone user can pick
                                    			 up a ringing call on another phone by pressing a soft key and then dialing the
                                    			 extension. A phone user does not need to belong to a pickup group to use this
                                    			 method. The soft key that the user presses, either GPickUp or PickUp, depends
                                    			 on your configuration.

Group Pickup,
                                    			 Different Group—Call pickup, explicit group ringing extension. A phone user can
                                    			 answer a ringing phone in any pickup group by pressing the GPickUp soft key and
                                    			 then dialing the pickup group number. If there is only one pickup group defined
                                    			 in the Cisco Unified CME system, the phone user can pick up the call simply by
                                    			 pressing the GPickUp soft key. A phone user does not need to belong to a pickup
                                    			 group to use this method.

Local Group
                                    			 Pickup—Call pickup, local group ringing extension. A phone user can pick up a
                                    			 ringing call on another phone by pressing a soft key and then the asterisk (*)
                                    			 if both phones are in the same pickup group. The soft key that the user
                                    			 presses, either GPickUp or PickUp, depends on your configuration.

SIP phones only
                                          		  support local pickup and group pickup. Directed call pickup is not supported.

The specific soft
                              		keys used to access different Call Pickup features on SCCP and SIP phones
                              		depends on the configuration in Cisco Unified CME. See the service
                                    			 directed-pickup command in Cisco Unified CME Command Reference for a
                              		description.

You can assign each
                              		directory number to only one pickup group and a directory number must have a
                              		pickup group configured to use Local Group Pickup. There is no limit to the
                              		number of directory numbers that can be assigned to a single pickup group, or
                              		to the number of pickup groups that can be defined in a Cisco Unified CME
                              		system.

If more than one
                              		call is ringing on the same number, the calls are picked up in the order in
                              		which they were received; the call that has been ringing the longest is the
                              		first call picked up from that extension number. Remote call pickup is not
                              		supported.

Call Pickup features
                              		are enabled globally for all phones through Cisco Unified CME. The PickUp and
                              		GpickUp soft keys display on supported SCCP and SIP phones by default and can
                              		be modified by using a phone template. For configuration information, see Enable Call Pickup .

Call
                                 		  Pickup shows four
                              		call-pickup scenarios.

### Call
                           	 Waiting

Call waiting allows
                              		phone users to be alerted when they receive an incoming call while they are on
                              		another call. Phone users hear a call-waiting tone when another party is trying
                              		to reach them and, on IP phones, see the calling party information on the phone
                              		screen.

Call-waiting calls
                              		to IP phones with soft keys can be answered using the Answer soft key.
                              		Call-waiting calls to analog phones controlled by Cisco Unified CME systems are
                              		answered using hookflash. When phone users answer a call-waiting call, their
                              		original call is automatically put on hold. If a phone user does not respond to
                              		a call-waiting notification, the call is forwarded as specified in the call-forward
                                    			 noan command for that extension.

For an IP phone
                              		running SCCP, call waiting for single-line ephone-dns requires two ephone-dns
                              		to handle the two calls. Call waiting on a dual-line ephone-dn requires only
                              		one ephone-dn because the two channels of the ephone-dn handle the two calls.
                              		The audible call-waiting indicator can be either a call-waiting beep or a
                              		call-waiting ring. For configuration information, see Configure Call-Waiting Indicator Tone on SCCP Phone .

For a SIP phone,
                              		call waiting is automatically enabled when you configure a voice register pool.
                              		For SIP phones directly connected to Cisco Unified CME, call waiting can be
                              		disabled at the phone-level. For configuration information, see Enable Call Waiting on SIP Phones .

For information on
                              		call waiting using Overlaid ephone-dns, see Overlaid Ephone-dns .

#### Call-Waiting Beep
                              	 for SCCP Phones

Call-waiting beeps
                                 		are enabled by default. You can disable the call-waiting beeps that are
                                 		generated from and accepted by directory numbers. If beep generation is
                                 		disabled, incoming calls to the directory number do not generate call-waiting
                                 		beeps. If beep acceptance is disabled, the phone user does not hear beeps when
                                 		using the directory number for an active call.

Table 1 shows the possible beep behaviors of one ephone-dn calling another ephone-dn
                                 		that is connected to another caller.

Ephone-dn 1
                                                				  Configuration

Ephone-dn 2
                                                				  Configuration

Active Call
                                                				  on DN

Incoming
                                                				  Call on DN

Expected
                                                				  Behavior

—

```
no call-waiting beep
```

DN 1

DN 2

No beep

```
no call-waiting beep
```

—

DN 1

DN 2

No beep

—

```
no call-waiting beep generate
```

DN 1

DN 2

No beep

—

```
no call-waiting beep accept
```

DN 1

DN 2

Beep

—

```
no call-waiting beep accept no call-waiting beep generate
```

DN 1

DN 2

No beep

```
no call-waiting beep
```

—

DN 1

DN 1

No beep

```
no call-waiting beep generate
```

—

DN 1

DN 1

No beep

```
no call-waiting beep accept
```

—

DN 1

DN 1

No beep

```
no call-waiting beep accept no call-waiting beep generate
```

—

DN 1

DN 1

No beep

```
no call-waiting beep generate
```

—

DN 1

DN 2

Beep

```
no call-waiting beep accept
```

—

DN 1

DN 2

No beep

—

```
no call-waiting beep
```

DN 1

DN 1

Beep

#### Call-Waiting Ring
                              	 for SCCP Phones

Instead of the
                                 		standard call-waiting beep sound through the handset, you can use a short ring
                                 		for call-waiting notification. The default is for directory numbers to accept
                                 		call interruptions, such as call waiting, and to issue a beeping sound for
                                 		notification.

To use a ring sound,
                                 		the directory number must accept call-waiting indicator tones. For
                                 		configuration information, see Configure Call-Waiting Indicator Tone on SCCP Phone or Enable Call Waiting on SIP Phones .

#### Cancel Call
                              	 Waiting

Cancel Call Waiting
                                 		(CCW) enables an SCCP phone user to disable Call Waiting for a call they
                                 		originate. The user activates CCW, and thereby disables call waiting, by
                                 		pressing the cancel call waiting (CW Off) soft key or by dialing the feature
                                 		access code (FAC) before placing a call. Call Waiting is inactive during that
                                 		call; anyone calling the user receives normal busy treatment and no call
                                 		waiting tone interrupts the user's active call. CCW automatically deactivates
                                 		when the user disconnects from the call. CCW is supported on all lines that
                                 		support the Call Waiting feature, including dual-lines and octo-lines.

This feature is
                                 		supported in Cisco Unified CME 8.0 and later versions for SCCP IP phones and
                                 		SCCP analog phones; it is not supported on SIP phones.

For configuration
                                 		information, see Configure Cancel Call Waiting on SCCP Phone .

### Callback Busy Subscriber

This feature allows callers who dial a busy extension number to request
                              		a callback from the system when the called number is available. Callers can
                              		also request callbacks for extensions that do not answer, and the system will
                              		notify them after the called phone is next used.

There can be only one callback request pending against a particular
                              		extension number, although a caller can initiate more than one callback to
                              		different numbers. If a caller attempts to place a callback request on a number
                              		that already has a pending callback request, the caller hears a fast-busy tone.
                              		If the called number has call forwarding enabled, the callback request is
                              		placed against the final destination number.

No configuration is required for this feature. To display a list of
                              		phones that have pending callback requests, use the show ephone-dn callback command.

### Hunt
                           	 Groups

Hunt groups allow
                              		incoming calls to a specific number (pilot number) to be directed to a defined
                              		group of extension numbers.

Incoming calls are
                              		redirected from the pilot number to the first extension number as defined by
                              		the configuration. If the first number is busy or does not answer, the call is
                              		redirected to the next phone in the list. A call continues to be redirected on
                              		busy or no answer from number to number in the list until it is answered or
                              		until the call reaches the number that is defined as the final number.

The redirect from
                              		one directory number to the next in the list is also known as a hop . You can
                              		set the maximum number of redirects for specific peer or longest-idle hunt
                              		groups, and for the maximum number of redirects allowed in a Cisco Unified CME
                              		system, both inside and outside hunt groups. If a call makes the maximum number
                              		of hops or redirects without being answered, the call is dropped.

In Cisco Unified CME
                              		9.0 and later versions, support for call statistics is added for voice hunt
                              		groups. To write all the ephone and voice hunt group statistics to a file, the ephone-hunt statistics
                                    			 write-all command is enhanced and renamed to hunt-group statistics
                                    			 write-all command. If applicable, the TFTP statistics report
                              		consists of both ephone and voice hunt group statistics.

In Cisco Unified CME
                              		9.5 and later versions, the command hunt-group statistics
                                    			 write-v2 is added to write all ephone hunt group statistics to a
                              		file along with total logged in and logged out time for agents. The command was
                              		enhanced in Unified CME Release 11.5 to add statistics for total logged in and
                              		logged out time for voice hunt group.

The show telephony-service
                                    			 all command is also enhanced to display the total number of
                              		ephone and voice hunt groups that have statistics collection turned on.

The statistics
                                    			 collect command under voice hunt-group configuration mode is
                              		introduced to enable the collection of call statistics for a voice hunt group.

The show voice hunt-group
                                    			 statistics command is introduced to display call statistics from
                              		voice hunt groups.

For Unified CME 11.5
                              		and later versions, the overwrite-dyn-stats (voice
                                    			 hunt-group) command is introduced to overwrite statistics of
                              		previously joined dynamic agent with stats of newly joined dynamic agents for
                              		voice hunt group. The statistics for a dynamic agent are overwritten only when
                              		all the 32 available slots are used. For more information, see Cisco Unified Communications
                                 		  Manager Express Command Reference Guide .

For Unified CME 12.2
                              		and later versions, Sequential, Parallel, Peer, and Longest Idle voice hunt
                              		groups support SIP shared line and mixed shared ine (SIP and SCCP Phones)
                              		directory numbers. All shared line features such as Hold and Remote resume,
                              		Barge, cBarge, Privacy, and calls through B-ACD is supported for calls that are
                              		placed through voice hunt groups.

The following are the known behavior patterns for the voice hunt group enhancement with shared line support, introduced in
                              Unified CME Release 12.2:

When you press the Decline softkey on one of the shared line DNs (configured across phones) in a voice hunt group for an incoming
                                    call, the shared line DNs on the other phones continue ringing. This behavior is typical to shared line DNs in a voice hunt
                                    group. For all shared lines that are not part of a voice hunt group, when you press the Decline softkey, all the corresponding
                                    shared line DNs stop ringing.

Hlog feature is not supported on a shared DN. If a phone configured with Hlog has a shared DN as part of voice hunt group,
                                    then the Hlog functionality is supported only for the other lines that are part of voice hunt group on that phone.

For information on
                              		displaying statistics for hunt groups, see Cisco Unified CME B-ACD and
                                 		  Tcl Call-Handling Applications .

There are four
                              		different types of hunt groups. Each type uses a different strategy to
                              		determine the first number that rings for successive calls to the pilot number,
                              		as described below.

Sequential
                                       				Hunt Groups —Numbers always ring in the left-to-right order in which they
                                    			 are listed when the hunt group is defined. The first number in the list is
                                    			 always the first number to be tried when the pilot number is called. Maximum
                                    			 number of hops is not a configurable parameter for sequential hunt groups. Sequential hunt Group shows an illustrated example.

Peer
                                       				Hunt Groups —The first number to ring is the number to the right of the
                                    			 directory number that was the last to ring when the pilot number was last
                                    			 called. Ringing proceeds in a circular manner, left to right, for the number of
                                    			 hops specified in the hunt group configuration. Peer hunt Group shows an illustrated example.

Longest-idle
                                       				Hunt Groups —Calls go first to the number that has been idle the longest
                                    			 for the number of hops specified when the hunt group was defined. The
                                    			 longest-idle time is determined from the last time that a phone registered,
                                    			 reregistered, or went on-hook. Longest-idle hunt Group shows an illustrated example.

Parallel
                                       				Hunt Groups (Call Blast) —Calls ring all numbers in the hunt group
                                    			 simultaneously.

Ephone Hunt-group
                              		chains can be configured in any length, but the actual number of hops that can
                              		be reached in a chain is determined by the max-redirect command configuration. In the following example, a maximum redirect number 15
                              		or greater must be configured for callers to reach the final 5000 number. If a
                              		lower number is configured, the call disconnects.

```
ephone-hunt 1 sequential
```

```
pilot 8000
```

```
list 8001, 8002, 8003, 8004
```

```
final 9000
```

```
ephone-hunt 2 sequential
```

```
pilot 9000
```

```
list 9001, 9002, 9003, 9004
```

```
final 7000
```

```
ephone-hunt 3 sequential
```

```
pilot 7000
```

```
list 7001, 7002, 7003, 7004
```

```
final 5000
```

Cisco Unified CME
                              		4.3 and later versions support the following Voice Hunt-Group features:

Call Forwarding
                                    			 to a Parallel Voice Hunt-Group (Call Blast)

Call Transfer to
                                    			 a Voice Hunt-Group

Member of Voice
                                    			 Hunt-Group can be a SIP phone, SCCP phone, FXS analog phone, DS0-group,
                                    			 PRI-group, or SIP trunk.

Unified CME supports chaining (nesting) of a voice hunt group with another voice hunt group. The chaining of voice hunt groups
                                    is established by configuring the final number of the first voice hunt group as the pilot number of the second voice hunt
                                    group.

For Unified CME B-ACD, the final destination for voice hunt groups is determined by the B-ACD service.

Unified CME supports the chaining (nesting) of a maximum of two voice hunt groups. The configuration ensures that there is
                                    no looping of calls placed to a voice hunt group.

#### Ephone-Hunt Groups
                              	 and Voice Hunt-Groups Comparison

SIP phones support
                                 		Voice Hunt-Groups. SCCP phones support Ephone-Hunt Groups, and in
                                 		Cisco Unified CME 4.3 and later versions, SCCP phones also support Voice
                                 		Hunt-Groups. Table 1 compares the features of Ephone-Hunt Groups and Voice Hunt-Groups.

Feature

Ephone Hunt

Voice Hunt
                                                				  Group

Endpoints
                                                				  Supported

SCCP only

SIP, SCCP,
                                                				  PSTN, and FXS

Parallel
                                                				  Hunt Groups (Call Blast)

No (for
                                                				  alternative, see Shared- Line Overlays

Yes

Hunt
                                                				  Statistics Support

Yes

Yes

B-ACD
                                                				  Support

Yes

Yes

Shared Line

Yes

Yes

Features
                                                				  such as present-call and login/logout

Yes

Yes (Only
                                                				  for SIP and SCCP phones)

#### Sequential Hunt
                              	 Groups

In a sequential hunt
                                 		group, extensions always ring in the order in which they are listed, left to
                                 		right, when the hunt group is defined. The first number in the list is always
                                 		the first number to be tried when the pilot number is called. Maximum number of
                                 		hops is not a configurable parameter for sequential hunt groups.

From Unified CME
                                 		12.2 onwards, sequential voice hunt groups support shared lines and mixed
                                 		shared lines. When calls are placed on a sequential voice hunt group and a
                                 		shared DN is part of the hunt group, the call is placed sequentially. For the
                                 		shared DN, the call would ring on all phones part of this shared DN. If none of
                                 		the phones answer, then call would continue to the next DN in the hunt group.

Consecutive numbers of the same phone cannot be members of a
                                             		  Sequential Voice Hunt Group when present call idle state (configured using the
                                             		  CLI command present-call idle-phone ) is set to true. The
                                             		  limitation applies to both SIP and SCCP phones.

#### Peer Hunt
                              	 Groups

In a peer hunt
                                 		group, extensions ring in a round-robin order. The first extension to ring is
                                 		the number in the list to the right of the last extension to ring when the
                                 		pilot number was last called. Ringing proceeds in a circular manner, left to
                                 		right, for the number of hops specified when the hunt group was defined.

From Unified CME
                                 		12.2 onwards, peer voice hunt groups support shared and mixed shared lines.
                                 		When calls are placed on a peer voice hunt group and a shared DN is part of the
                                 		hunt group, the call is placed in a round-robin order. For the shared DN, the
                                 		call would ring on all phones part of this shared DN. If none of the phones
                                 		answer, then call would continue to the next DN in the hunt group.

Peer hunt Group illustrates a peer hunt group.

#### Longest-Idle Hunt
                              	 Groups

In a longest-idle
                                 		hunt group, the algorithm for choosing the next extension to receive a call is
                                 		based on a comparison of on-hook time stamps. The extension with the smallest
                                 		on-hook time stamp value is chosen when the next call comes to the hunt group.

The default behavior
                                 		is that an on-hook time stamp value for an extension is updated only when the
                                 		agent answers a call. In Cisco Unified CME 4.0 and later versions, you can
                                 		specify that an on-hook time stamp is updated when a call rings an extension
                                 		and also when a call is answered by an agent.

From Unified CME
                                 		12.2 onwards, longest-idle voice hunt groups support shared lines and mixed
                                 		shared lines. When calls are placed on a longest-idle voice hunt group and a
                                 		shared DN is part of the hunt group, the call is placed based on a comparison
                                 		of on-hook time stamps. For the shared DN, the call would ring on all phones
                                 		part of this shared DN. If none of the phones answer, then call would continue
                                 		to the next DN in the hunt group.

Longest-idle hunt Group illustrates a longest-idle hunt group.

#### Parallel Hunt
                              	 Groups (Call Blast)

In a parallel hunt
                                 		group, calls simultaneously ring multiple phones. Using parallel hunt groups is
                                 		also referred to as application-level forking because it enables the forking of
                                 		a call to multiple destinations. In versions earlier than Cisco Unified
                                 		CME 4.3, only SIP phones support parallel hunt groups. In Unified CME 4.3 and
                                 		later versions, SCCP phones also support voice hunt groups.

You can enable
                                 		functionality similar to parallel hunt groups on SCCP phones by using the
                                 		ephone-dn overlay feature for shared lines. See Shared- Line Overlays .

From Unified CME
                                 		12.2 onwards, parallel voice hunt groups support shared lines and mixed shared
                                 		lines. For parallel voice hunt groups, a maximum of 32 call blasts is
                                 		supported, including shared-line and normal directory numbers. For example,
                                 		consider a voice hunt group configured with 20 directory numbers, including 3
                                 		shared-lines assigned across three different phones. In this scenario, the
                                 		count of shared line directory numbers is considered as 9 (3*3). Then, the
                                 		total count of call blasts in this hunt group is 26 directory numbers(17 + 9).
                                 		When the call blast limit of 32 is exceeded, then call is not placed for those
                                 		voice hunt group directory numbers that exceed the limit.

In the following
                                 		parallel hunt group example, when callers dial extension 1000, extension 1001,
                                 		1002, and so on ring simultaneously. The first extension to answer is
                                 		connected. If none of the extensions answers, the call is forwarded to
                                 		extension 2000, which is the number for the voice-mail service.

```
voice hunt-group 4 parallel
pilot 1000
list 1001, 1002, 1003, 1004
final 2000
timeout 20
```

The number of
                                 		ringing calls that a parallel hunt group can support depends on whether
                                 		call-waiting is enabled on the SIP phones.

If call-waiting is
                                 		enabled (the default), parallel hunt groups support multiple calls up to the
                                 		limit of call-waiting calls supported by a particular SIP phone model. You may
                                 		not want to use unlimited call-waiting, however, with parallel hunt-groups if
                                 		agents do not want a large number of waiting calls when they are already
                                 		handling a call.

If call waiting is
                                 		disabled, parallel hunt groups support only one call at a time in the ringing
                                 		state. After a call is answered (by one of the phones in the hunt group), a
                                 		second call is allowed. The second and subsequent calls ring only the idle
                                 		phones in the hunt group, and bypass the busy phone that answered the first
                                 		call (because this phone is connected to the first call). After the second call
                                 		is answered, a third call is allowed, and so on until all the phones in the
                                 		parallel hunt group are busy. The hunt group does not accept further calls
                                 		until at least one phone returns to the idle/on-hook state.

When two or more
                                 		phones within the same parallel hunt group attempt to answer the same call,
                                 		only one phone can connect to the call. Phones that fail to connect must return
                                 		to the on-hook state before they can receive subsequent calls. Calls that
                                 		arrive before a phone is placed on-hook are not presented to the phone. For
                                 		example, if a second call arrives after Phone 1 has answered the original call,
                                 		but before Phone 2 goes back on-hook, the second call bypasses Phone 2 (because
                                 		it is offhook).

When a phone returns
                                 		to the idle/on-hook state, it does not automatically re-synchronize to the next
                                 		call waiting to be answered. For example, in the previous scenario, if the
                                 		second call is still ringing Phone 3 when Phone 2 goes on-hook, Phone 2 does
                                 		not ring because it was offhook when the second call arrived.

For configuration
                                 		information, see Configure Voice-Hunt Groups .

### View and Join for
                           	 Voice Hunt Groups

You can view voice
                              		hunt group related information on SIP and SCCP phones using the phone menu. The
                              		following information related to hunt groups can be viewed on the phone
                              		display:

Name

Pilot number

Status

If voice hunt groups
                              		have been configured, the user can view the voice hunt group information using
                              		the service button on the phone, by navigating to My Phone
                                    			 Apps > Voice Hunt Groups . On selecting the
                              		voice hunt group option, a list of voice hunt groups will be displayed.

A voice hunt group
                              		includes the name of the hunt group, the pilot number and also the status of
                              		the DN indicating if the DN is a member of the hunt group. This information is
                              		displayed in the following method:

If DN is a
                                    			 static member of the hunt group, then status is displayed with # (hash) symbol.

If DN is dynamic
                                    			 member, the status is displayed with * (asterisk) symbol.

The following
                              		operations can be performed on the phone user interface:

User can join or
                                    			 unjoin to or from voice hunt groups by selecting the Join or Unjoin softkey which is displayed on the voice hunt
                                    			 group page. The user can select the required voice hunt group using the up and
                                    			 down buttons.

User can access
                                    			 the next or previous records of voice hunt groups by selecting the Next / Previous softkey options.

To display voice
                              		hunt-group information on the phone, user needs to configure phone-display command under voice hunt-groups.

#### Restrictions
                                 		  and Limitations

A DN can join
                                       				a maximum of six voice hunt groups.

The displayed
                                       				hunt group information is applicable only for the primary line of the phone.

A primary DN
                                       				can join or unjoin a voice hunt group using the Service button on the phone. If a phone is
                                       				configured with multiple DNs, then DNs other than the primary DN can join the
                                       				voice hunt groups by dialing the FAC standards.

The voice hunt
                                       				group information display feature is applicable only on the phones that support My
                                          				  Phone Apps menu. For example, 78xx, 88xx phone families are
                                       				supported. However, 69xx, 39xx phone families are not supported.

### Enable User
                           	 Interface to View, Join, and Unjoin Voice Hunt Groups on SCCP Phone

This feature
                                 		  enables an SCCP phone user to view information related to the voice hunt groups
                                 		  and join or unjoin voice hunt groups from a menu on their phone. This feature
                                 		  is enabled by default. You must perform this task only if the feature was
                                 		  previously disabled on a phone.

#### Before you begin

Cisco Unified CME
                                 		  10.5 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- ephone phone-tag

- phone-ui voice-hunt-groups

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

ephone phone-tag

#### Example:

```
Router(config)# ephone 12
```

Enters ephone
                                             				configuration mode.

- phone-tag —Unique number
                                                				  that identifies this ephone during configuration tasks.

Step 4

phone-ui voice-hunt-groups

#### Example:

```
Router(config-ephone)# phone-ui voice-hunt-groups
```

Enables a SCCP
                                             				phone user to view information related to voice hunt groups and also join or
                                             				unjoin from voice hunt groups.

- This command is enabled by
                                                				  default.

Step 5

end

#### Example:

```
Router(config-ephone)# end
```

Exits to
                                             				privileged EXEC mode.

#### Example

The following
                                 		  example shows that the voice-hunt-groups command is enabled on an SCCP phone.

```
ephone-dn 10 dual-line
```

```
number 1001
```

```
no huntstop
```

```
huntstop channel
```

```
ephone-dn 11 dual-line
```

### Configure Service
                           	 URL Button On SCCP Phone Line Key

To implement
                                 		  service PLK feature line key buttons on Cisco Unified SCCP Phones, perform the
                                 		  following steps.

### SUMMARY STEPS

- enable

- configure terminal

- ephone template template-tag

- url-button index type | url [ name ]

- exit

- ephone phone-tag

- ephone-template template-tag

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

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ephone template template-tag

#### Example:

```
Router(config)# ephone template 5
```

Enters
                                             				ephone-template configuration mode to create an ephone template.

template-tag —Unique identifier for the ephone template that
                                                   					 is being created. Range: 1 to 10.

Step 4

url-button index type | url [ name ]

#### Example:

```
Router#(config-ephone-template)#url-button 1 myphoneapp
Router(config-ephone-template)#url-button 2 em
Router(config-ephone-template)#url-button 3 snr
Router(config-ephone-template)#url-button 4 voicehuntgroups
Router(config-ephone-template)#url-button 5 park-list
Router(config-ephone-template)#url-button 6 http://www.cisco.com
```

Configures a
                                             				service URL feature button on a line key.

Index —Unique index number. Range: 1 to 8.

type —Type of service PLK button. The following
                                                   					 types of URL service buttons are available:

myphoneapp: My phone application configured under phone user
                                                         						  interface.

em:
                                                         						  Extension Mobility

snr:
                                                         						  Single Number Reach

voicehuntgroups: Voice Hunt Groups Information

park-list: Parked calls

url name —Service URL with maximum length of 31
                                                   					 characters.

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
Router(config)#ephone 36
```

Enters ephone
                                             				configuration mode.

phone-tag —Unique sequence number that identifies
                                                   					 this ephone during configuration tasks.

Step 7

ephone-template template-tag

#### Example:

```
Router(config-ephone)# ephone-template 5
```

Applies an
                                             				ephone template to the ephone that is being configured.

Step 8

end

#### Example:

```
Router(config-ephone)# end
```

Returns to
                                             				privileged EXEC mode.

#### Example

The following
                                 		  example shows three URL buttons configured for line keys:

```
!
!
!
ephone-template 5
url-button 1 em
url-button 2 mphoneapp mphoneapp
url-button 3 snr
url-button 4 voicehuntgroups
url-button 5 park-list
!
ephone 36
ephone-template 5
```

#### What to do next

If you are done
                                 		  configuring the url buttons for phones in Cisco Unified CME, restart the
                                 		  phones.

### Configure Service
                           	 URL Button On SIP Phone Line Key

### SUMMARY STEPS

- enable

- configure terminal

- voice register template template-tag

- url-button [ index number ] [ url location ] [ label ]

- exit

- voice register pool phone-tag

- template template-tag

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

voice register template template-tag

#### Example:

```
Router(config)# voice register template 5
```

Enters
                                             				ephone-template configuration mode to create an ephone template.

- template-tag —Unique
                                                				  identifier for the ephone template that is being created. Range: 1 to 10.

Step 4

url-button [ index number ] [ url location ] [ label ]

#### Example:

```
Router(config-register-temp)url-button 1 http://x.x.x.x:80/CMEserverForPhone/vhg_root_menu VHG_List
```

```
Router(config-register-temp)url-button 2 http://x.x.x.x:80/CMEserverForPhone/park_list Park_List
```

Configures a
                                             				service url feature button on a line key.

x.x.x.x—CME IP address.

Index
                                                   					 number—Unique index number ranging from 1 to 8.

URL location —Location of the URL.

label—A
                                                   					 label name which is displayed on phone.

Step 5

exit

#### Example:

```
Router(config-register-temp)# exit
```

Exits
                                             				ephone-template configuration mode.

Step 6

voice register pool phone-tag

#### Example:

```
Router(config)# voice register pool 12
```

Enters ephone
                                             				configuration mode.

phone-tag —Unique number that identifies this ephone during
                                                   					 configuration tasks.

Step 7

template template-tag

#### Example:

```
Router(config-register-pool)# template 5
```

Applies the
                                             				ephone template to the phone.

template-tag —Unique identifier of the template
                                                   					 that you created in Step 3.

Step 8

end

#### Example:

```
Router(config-register-pool)# end
```

Returns to
                                             				privileged EXEC mode.

#### Example

The following
                                 		  example shows URL buttons configured in the voice register template 1:

```
Router# show run ! voice register template  1
```

```
url-button 1 http://x.x.x.x:80/CMEserverForPhone/vhg_root_menu VHG_List 
url-button 2 http://x.x.x.x:80/CMEserverForPhone/park_list Park_List 
url-button 5 http://www.cisco.com Cisco ! voice register pool 50 !
```

#### What to do next

If you are done
                                 		  configuring the URL buttons for phones in Cisco Unified CME, generate a new
                                 		  configuration file and restart the phones. See Generate Configuration Profiles for SIP Phones .

#### Display Support
                              	 for the Name of a Called Voice Hunt-Group

A voice hunt-group
                                 		is associated with a pilot number. But because there is no association with the
                                 		name of the voice hunt-group when calls are forwarded from the voice hunt-group
                                 		to the final number, the forwarding number is sent without the name of the
                                 		forwarding party. The final number may be in the form of a voice mail, a Basic
                                 		Automatic Call Distribution (BACD) script, or another extension.

In Cisco Unified CME
                                 		9.5, the display of the name of the called voice hunt-group pilot is supported
                                 		by configuring the following command in voice hunt-group or the ephone-hunt
                                 		configuration mode:

[ no ] name “primary pilot
                                       			 name” [ secondary “secondary pilot name” ]

The secondary name
                                 		is optional and when the secondary pilot name is not explicitly configured, the
                                 		primary pilot name is applicable to both pilot numbers.

The following
                                 		example configures the primary pilot name for both the primary and secondary
                                 		pilot numbers:

```
name SALES
```

The following
                                 		example configures different names for the primary and secondary pilot numbers:

```
name SALES secondary SALES-SECONDARY
```

The following
                                 		example associates a two-word name for the primary pilot number and a one-word
                                 		name for the secondary pilot number:

```
name “CUSTOMER SERVICE” secondary CS
```

The following
                                 		example associates a one-word name for the primary pilot number and a two-word
                                 		name for the secondary pilot number:

```
name FINANCE secondary “INTERNAL ACCOUNTING”
```

The following
                                 		example associates two-word names for the primary and secondary pilot numbers:

```
name “INTERNAL CALLER” secondary “EXTERNAL CALLER”
```

For configuration
                                 		information, see Associate a Name with a Called Voice Hunt-Group .

For more
                                 		configuration examples, see Example for Associating a Name with a Called Voice Hunt-Group .

For configuration
                                 		information, see Configure Ephone-Hunt Groups on SCCP Phones .

The following show commands
                                 		are modified to reflect the configured primary and secondary pilot names:

show ephone-hunt

show voice hunt-group

The information
                                 		related to the name of the ephone-hunt group and voice hunt-group are sent to
                                 		the phone and displayed on the phone’s user interface.

Restriction

Display support applies to Cisco Unified SCCP IP phones in voice hunt-group and ephone-hunt configuration modes but are not
                                                   supported in Cisco Unified SIP IP phones.

Called name and called number information displayed on the caller’s phone follows existing behavior, where the called names
                                                   and called numbers are updated so that a sequential hunt reflects the name and number of the ringing phone.

#### Support for Voice
                              	 Hunt Group Descriptions

In Cisco Unified CME
                                 		9.5, a description can be specified for a voice hunt group using the description command in voice hunt-group configuration mode.

For a configuration
                                 		example, see Example for Specifying a Description for a Voice Hunt-Group .

#### Prevent Local Call
                              	 Forwarding to the Final Agent in a Voice Hunt-Groups

Local or internal
                                 		calls are calls originating from a Cisco Unified SIP or Cisco Unified SCCP IP
                                 		phone in the same Cisco Unified CME system.

Before Cisco Unified
                                 		CME 9.5, the no forward
                                       			 local-calls command was configured in ephone-hunt group to
                                 		prevent a local call from being forwarded to the next agent.

In Cisco Unified CME
                                 		9.5, local calls are prevented from being forwarded to the final destination
                                 		using the no forward local-calls
                                       			 to-final command in parallel configuration mode or the sequential
                                 		voice hunt-group configuration mode.

When the no forward local-calls
                                       			 to-final command is configured in sequential voice hunt-group
                                 		configuration mode, local calls to the hunt-group pilot number are sent
                                 		sequentially only to the list of members of the group using the rotary-hunt
                                 		technique. In case all the group members of the voice hunt group are busy, the
                                 		caller hears a busy tone. If any of the group members are available but do not
                                 		answer, the caller hears a ringback tone and is eventually disconnected after
                                 		the specified timeout. The call is not forwarded to the final number.

When the no forward local-calls
                                       			 to-final command is configured in parallel voice hunt-group
                                 		configuration mode, local calls to the hunt-group pilot number are sent
                                 		simultaneously to the list of members of the group using the blast technique.
                                 		In case all the group members of the voice hunt group are busy, the caller
                                 		hears a busy tone. If any of the group members are available but do not answer,
                                 		the caller hears a ringback tone and is eventually disconnected after the
                                 		specified timeout. The call is not forwarded to the final number.

For configuration
                                 		information, see Prevent Local Call Forwarding to Final Agent in Voice Hunt-Groups .

For a configuration
                                 		example, see Example for Preventing Local Call Forwarding in Parallel Voice Hunt-Groups .

#### Enhancement of
                              	 Support for Voice Hunt Group Agent Statistics

Before Cisco Unified
                                 		CME Release 11.5, total logged in and total logged out time statistics were
                                 		supported only for ephone hunt group agents. In Cisco Unified CME 11.5, support
                                 		for Total logged in and Total logged out time statistics is added for voice
                                 		hunt group agents also.

The output of
                                          			 the show
                                                				  voice-hunt tag statistics command is modified to display the additional information in the statistics.

For more
                                 		configuration examples, see Example for Call Statistics From a Voice Hunt Group .

#### Enhancement of
                              	 Support for Ephone-Hunt Group Agent Statistics

Before Cisco Unified
                                 		CME 9.5, statistics were maintained for each ephone hunt group and each
                                 		ephone-hunt group agent. Some of the statistics included the number of maximum
                                 		and minimum agents, average time to answer, average time in a call, and average
                                 		time on hold.

In Cisco Unified CME
                                 		9.5, support for hunt group agent statistics of Cisco Unified SCCP IP phones is
                                 		enhanced to include the following information:

Total logged in
                                       			 time—On an hourly basis, displays the duration (in seconds) since a specific
                                       			 agent logged into a hunt group.

Total logged out
                                       			 time—On an hourly basis, displays the duration (in seconds) since a specific
                                       			 agent logged out of a hunt group.

The output of the show
                                       			 ephone-hunt tag statistics command is modified to display the additional information in the statistics.

For more
                                 		configuration examples, see Example for Displaying Total Logged-In Time and Total Logged-Out Time for Each Hunt-Group Agent .

Restriction

Statistics collection for Cisco Unified SCCP and SIP IP phones in Cisco Unified SRST are not supported.

#### Hunt Group Agent
                              	 Availability Options

Three options
                                 		increase the flexibility of hunt group agents by allowing them to dynamically
                                 		join and leave hunt groups or to temporarily enter a not-ready state in which
                                 		they do not receive calls.

Table 1 compares the following agent availability features:

Comparison Factor

Dynamic Membership

Agent Status Control

Automatic Agent Status Not-Ready

Purpose

Allows an authorized agent to join and leave hunt groups.

Allows an agent to manually activate a toggle to temporarily enter a not-ready state, in which hunt-group calls bypass the
                                             agent’s phone.

Automatically puts an agent’s phone in a not-ready state after a specified number of hunt-group calls are unanswered by the
                                             agent’s phone.

Example

Agent A joins a hunt group at 8 a.m. and takes calls until 1 p.m., when he leaves the hunt group. While Agent A is a member
                                             of the hunt group, he occupies one of the wildcard slots in the list of numbers configured for the hunt group. At 1 p.m.,
                                             Agent B joins the hunt group using the same wildcard slot that Agent A relinquished when he left.

Agent A takes a coffee break at 10 a.m. and puts his phone into a not-ready status while he is on break. When he returns he
                                             puts his phone back into the ready status and immediately starts receiving hunt-group calls again. He retained his wildcard
                                             slot while he was in the not-ready status.

Agent B is suddenly called away from her desk before she can manually put her phone into the not-ready status. After a hunt-group
                                             call is unanswered at Agent B’s phone, the phone is automatically placed in the not-ready status and it is not presented with
                                             further hunt-group calls. When Agent B returns, she manually puts her phone back into the ready status.

Hunt-group slot availability

An agent joining a hunt group occupies a wildcard slot in the hunt group list. An agent leaving the group relinquishes the
                                             slot, which becomes available for another agent.

An agent who enters the not-ready state does not give up a slot in the hunt group. The agent continues to occupy the slot
                                             regardless of whether the agent is in the not-ready status.

An agent who enters the not-ready does not give up a slot in the hunt group. The agent continues to occupy the slot regardless
                                             of whether the agent is in the not-ready status.

Agent activation method

An authorized agent uses a feature access code (FAC) to join a hunt group and a different FAC to leave the hunt group.

An agent uses the HLog soft key to toggle agent status between ready and not ready. Agents can also use the HLog FAC to toggle
                                             between ready and not-ready if FACs are enabled.

If the HLog soft key is not enabled, the DND soft key can be used to put an agent in the not-ready status and the agent will
                                             not receive any calls.

An agent who is a member of a hunt group configured with the auto logout command does not answer the specified number of calls, and the agent’s phone is automatically changed to the not-ready status.
                                             The agent uses the HLog soft key or a FAC to return to the ready status.

If the HLog soft key or FAC has not been enabled in the configuration, the agent uses the DND soft key to return to the ready
                                             status.

Configuration

The system administrator uses the list command to configure up to 20 wildcard slots in a hunt group and uses the ephone-hunt login command to authorize certain directory numbers to use these wildcard slots.

See Configure Ephone-Hunt Groups on SCCP Phones .

The system administrator uses the HLog keyword with the hunt-group logout command to provide an HLog soft key on display phones and uses the fac command to enable standard FACs or create a custom FAC.

See Configure Ephone-Hunt Groups on SCCP Phones .

The system administrator uses the auto logout command to enable automatic agent status not-ready for a hunt group.

This functionality is disabled by default.

See Configure Ephone-Hunt Groups on SCCP Phones .

See Configure Voice-Hunt Groups .

Optional customizations

The system administrator can establish custom FACs for agents to use to enter or leave a hunt group.

The system administrator can use the softkeys commands to change the position or prevent the display of the HLog soft key on individual phones.

The system administrator can use the auto logout command to specify the number of unanswered calls that will trigger an agent status change to not-ready and whether this feature
                                             applies to dynamic hunt-group members, static hunt-group members, or both.

The system administrator can use the hunt-group logout command to specify whether an automatic change to the not-ready status also places a phone in DND mode.

#### Dynamic Ephone
                              	 Hunt Group Membership

Hunt groups allow
                                 		you to set up pools of extension numbers to answer incoming calls. Up to 20
                                 		wildcard slots can be entered in the list of hunt group extension numbers to
                                 		allow dynamic group membership, in which authorized phone users can join a hunt
                                 		group whenever a vacant wildcard slot is available and they can leave when they
                                 		like. Each phone user who joins a group occupies one slot. If no slots are
                                 		available, a user who tries to join a group hears a busy signal.

Allowing dynamic
                                 		membership in a hunt group is a three-step process:

Use the list command
                                       			 in ephone-hunt configuration mode to specify up to 20 wildcard slots in the
                                       			 hunt group.

Use the ephone-hunt
                                             				  login command under each directory number that should be allowed
                                       			 to dynamically join and leave hunt groups. Directory numbers are disallowed
                                       			 from joining ephone hunt groups by default, so you have to explicitly allow
                                       			 this behavior for each directory number that you want to be able to log in to
                                       			 ephone hunt groups.

Use the fac standard command to enable standard FACs or the fac custom command to define custom FACs. FACs must be enabled so that agents can use them
                                       			 to join and leave ephone hunt groups.

To dynamically join
                                 		an ephone hunt group, a phone user dials a standard or custom FAC for joining
                                 		an ephone hunt group. The standard FAC to join an ephone hunt group is *3.

If multiple ephone
                                 		hunt groups have been created that allow dynamic membership, the phone user
                                 		must also dial the ephone hunt group pilot number. For example, if the
                                 		following ephone hunt groups are defined, a phone user dials *38000 to join the
                                 		Sales hunt group:

```
voice hunt-group 24 sequential
pilot 8000
list 8001, 8002, *, *
description Sales Group
final 9000

voice hunt-group 25 sequential
pilot 7000
list 7001, 7002, *, *
description Service Group
final 9000
```

To leave an ephone
                                 		hunt group, a phone user dials the standard or custom FAC. The standard FAC to
                                 		leave an ephone hunt group is #3. See Customize Softkeys .

#### Dynamically Join
                              	 or Unjoin Multiple Voice Hunt Groups

In Cisco Unified CME
                                 		10.5 and later versions, support for phones to dynamically join the voice hunt
                                 		groups is added. This feature is supported on both the SIP and SCCP phones. A
                                 		single DN can dynamically join and unjoin multiple voice hunt groups. You can
                                 		perform this action on a maximum of six different voice hunt groups.

A single SCCP or SIP
                                 		DN can join multiple voice hunt groups dynamically by using the existing FAC
                                 		standards with pilot number of voice hunt groups. A primary DN of a phone can
                                 		also join and unjoin the voice hunt group using the Join or Unjoin soft key
                                 		that are available on the Voice Hunt Group information display page in the My
                                 		Phone App menu by using the service button.

From Cisco Unified
                                 		CME Release 10.5 onwards, a status message is displayed on the SCCP phone when
                                 		a dynamic agent joins a hunt group. The support for status message display for
                                 		a dynamic agent joining a hunt group on the SIP phone is supported from Cisco
                                 		Unified CME Release 11.6 onwards.

If a SIP or mixed
                                 		shared line DN (multi-line) joins multiple voice hunt groups, the phone
                                 		displays the called number information on the phone's interface for 5 seconds.
                                 		For SCCP phones, the voice hunt group-related information is displayed for the
                                 		primary line of the phone.

Hunt groups allow
                                 		you to set up pools of extension numbers to answer incoming calls. You can
                                 		enter up to 32 wildcard slots in the list of voice hunt group extension numbers
                                 		to allow dynamic group membership, in which phone users can join or unjoin a
                                 		voice hunt group whenever a vacant wildcard slot is available. Each phone user
                                 		who joins a group occupies one slot. If no slots are available, a user who
                                 		tries to join a group will fail to join.

Allowing dynamic
                                 		membership in a voice hunt group is a three-step process:

Use the list command
                                       			 in voice-hunt configuration mode to specify up to 32 wildcard slots in the hunt
                                       			 group.

Use the voice-hunt-groups
                                             				  login command under each directory number that should be allowed
                                       			 to dynamically join and unjoin hunt groups. Directory numbers are not allowed
                                       			 from joining voice hunt groups by default, so you have to explicitly allow this
                                       			 behavior for each directory number that you want to be able to join or unjoin a
                                       			 voice hunt groups.

Use the fac standard command to enable standard FACs or the fac custom command to define custom FACs. FACs must be enabled so that agents can use them
                                       			 to join and unjoin hunt groups.

To dynamically join
                                 		a voice hunt group, a phone user dials a standard or custom FAC for joining a
                                 		voice hunt group. The standard FAC to join a voice hunt group is *3.

If multiple voice
                                 		hunt groups have been configured with dynamic agents, the phone user must also
                                 		dial the voice hunt group pilot number. If only one voice hunt group is
                                 		configured with dynamic agent, on SIP phone only FAC is sufficient. Whereas, on
                                 		SCCP phone, pilot number is mandatory. For example, if the following voice hunt
                                 		groups are defined, a phone user dials *38000 to join the Sales hunt group:

```
voice hunt-group 24 sequential
pilot 8000
list 8001, 8002, *, *
description Sales Group
final 9000

voice hunt-group 25 sequential
pilot 7000
list 7001, 7002, *, *
description Service Group
final 9000
```

To unjoin a voice
                                 		hunt group, a phone user dials the standard or custom FAC. The standard FAC to
                                 		unjoin from all the hunt groups is #3. See Customize Softkeys .
                                 		If a DN joins multiple voice hunt groups, then to unjoin from a specific voice
                                 		hunt group the user can dial the standard FAC #4 followed by the pilot number.

From Unified CME 12.2 onwards, SIP, SCCP, and mixed (both SIP and SCCP)
                                 		shared DNs can Join or Unjoin a voice hunt group dynamically.

#### Agent Status
                              	 Control for Ephone Hunt Group

The Agent Status
                                 		Control feature allows ephone hunt group agents to control whether their phones
                                 		are in the ready or not-ready status. A phone in the ready status is available
                                 		to receive calls from the hunt group. A phone in the not-ready status blocks
                                 		calls from the hunt group. Agents should use the not-ready status for short
                                 		breaks or other temporary interruptions during which they do not want to
                                 		receive hunt-group calls.

Agents who put their
                                 		phones into the not-ready status do not relinquish their slots in the hunt
                                 		group list.

Agents use the HLog
                                 		soft key or the DND soft key to put a phone into the not-ready status. When the
                                 		HLog soft key is used to put a phone in the not-ready status, it does not
                                 		receive hunt group calls but can receive other calls. If the DND soft key is
                                 		used, the phone does not receive any calls until it is returned to the ready
                                 		status. The HLog and DND soft keys toggle the feature: if the phone is in the
                                 		ready status, pressing the key puts the phone in the not-ready status and
                                 		vice-versa.

The DND soft key is
                                 		visible on phones by default, but the HLog soft key must be enabled in the
                                 		configuration using the hunt-group
                                       			 logout command, which has the following options:

HLog —Enables
                                       			 both an HLog soft key and a DND soft key on phones in the idle, seized, and
                                       			 connected call states. When you press the HLog soft key, the phone is changed
                                       			 from the ready to not-ready status or from the not-ready to ready status. When
                                       			 the phone is in the not-ready status, it does not receive calls from the hunt
                                       			 group, but it is still able to receive calls that do not come through the hunt
                                       			 group (calls that directly dial its extension). The DND soft key is also
                                       			 available to block all calls to the phone if that is the preferred behavior.

DND —Enables
                                       			 only a DND soft key on phones. The DND soft key also changes a phone from the
                                       			 ready to not-ready status or from the not-ready to ready status, but the phone
                                       			 does not receive any incoming calls, including those from outside hunt groups.

Phones without soft-key displays can use a FAC to toggle their status from ready to not-ready and back to ready. The fac command is configured under telephony-service configuration mode to enable the standard set of FACs or to create custom FACs.
                                 The standard FAC to toggle the not-ready status at the directory number (extension) level is *4 and the standard FAC to toggle
                                 the not-ready status at the ephone level (all directory numbers on the phone) is *5. See Where to Go Next .

#### Agent Status
                              	 Control for Voice Hunt Group

The Agent Status
                                 		Control feature allows voice hunt group agents to control whether their phones
                                 		are in the ready or not-ready status. A phone in the ready status is available
                                 		to receive calls from the hunt group. A phone in the not-ready status blocks
                                 		calls from the hunt group. Agents should use the not-ready status for short
                                 		breaks or other temporary interruptions during which they do not want to
                                 		receive hunt-group calls.

Agents who put their
                                 		phones into the not-ready status do not relinquish their slots in the hunt
                                 		group list.

Agents use the HLog
                                 		softkey or the DND softkey to put a phone into the not-ready status. When the
                                 		HLog softkey is used to put a phone in the not-ready status, it does not
                                 		receive hunt group calls but can receive other calls. When Agent use DND
                                 		button, phone will be put into Not-Ready state and Hunt group calls will not be
                                 		routed. However normal or direct calls are still routed, but without audio
                                 		notifications.

The DND softkey is
                                 		visible on phones by default, but the HLog softkey must be enabled in the
                                 		configuration using the hunt-group
                                       			 logout command, which has the following options:

HLog —Enables
                                       			 both an HLog softkey and a DND softkey on phones in the idle, ringing, and
                                       			 connected call states. When you press the HLog softkey, the phone is changed
                                       			 from the ready to not-ready status or from the not-ready to ready status. When
                                       			 the phone is in the not-ready status, it does not receive calls from the hunt
                                       			 group, but it is still able to receive calls that do not come through the hunt
                                       			 group (calls that directly dial its extension). DND softkey suppresses audio
                                       			 notifications for direct calls.

DND —Enables
                                       			 only a DND softkey on phones. The DND softkey also changes a phone from the
                                       			 ready to not-ready status or from the not-ready to ready status for voice hunt
                                       			 group calls. Phones receive those calls that directly dial the extension.

Phones without
                                 		soft-key displays can use a FAC to toggle their status from ready to not-ready
                                 		and back to ready. The fac command
                                 		configured under telephony-service configuration mode must be used to enable
                                 		the standard set of FACs or to create custom FACs. The standard FAC to toggle
                                 		the not-ready status is *4 and the standard FAC to toggle the not-ready status
                                 		at the phone level (all directory numbers on the phone) is *5. See Where to Go Next .

From Cisco Unified
                                 		CME 10.5 onwards, SCCP and SIP phones are supported with Agent Status Control
                                 		for voice hunt group. SCCP phone can log in or log out to or from voice hunt
                                 		groups using HLog or DND softkeys, or standard or custom FACs, at line-Level as
                                 		well as phone level. Whereas, SIP phones can log in or log out to or from voice
                                 		hunt groups using only standard or custom FACs, only at Line-Level.

From Cisco Unified
                                 		CME Release 11.6 onwards, SIP phones are also supported with agent status
                                 		control, for voice hunt groups with HLog softkeys or FAC. Hence, SIP phones can
                                 		logout or login to voice hunt group using HLog softkey, feature button, or FAC
                                 		at phone level. If the phone is configured with a single line or multiple
                                 		lines, and if these lines are members of a voice hunt group, then phone level
                                 		logout or login results in logout or login of all lines on the phone.

To make HLog
                                 		functionality work with the SIP or SCCP phones, you need to configure the
                                 		command hunt-group logout
                                       			 HLog under telephony-service. Once user is logged out from the
                                 		hunt group, phone displays a message stating that the user is logged out of
                                 		hunt group. When the user is logged in to hunt group, the agent phone displays
                                 		a message stating that the user is logged in to hunt group. For Unified CME
                                 		12.1 and earlier releases, if any directory number that is part of voice hunt
                                 		group is shared across phones, then logout is not allowed at the phone level.

For Unified CME
                                 		12.2 and later releases, if any directory number that is part of voice hunt
                                 		group is a shared-line, then logout is allowed for all lines at the phone
                                 		level, except the shared-line. Shared-line status (always in logged-in state)
                                 		in a voice hunt group cannot be toggled using agent status control
                                 		functionality. While SCCP phones with a mixed shared-line only support line
                                 		level logout of the phone lines (except the shared-line), SIP phones with a
                                 		mixed shared-line support phone level logout of the phone lines (except the
                                 		shared-line).

To enable FAC, you
                                 		need to configure standard or custom FAC under telephony service configuration
                                 		mode using the command fac standard or fac custom .

If phone dn's
                                          			 are not members of a hunt group and phone is configured with an HLog feature
                                          			 button, then phone LED is off for SIP phones and on for SCCP phones.

If a SIP phone
                                          			 is already in logged in state, any newly joining dn of that phone (in any voice
                                          			 hunt group) is automatically in logged in state.

If a SIP phone
                                          			 is already in logged out state, any newly joining dn of that phone (in any
                                          			 voice hunt group) is automatically in logged out state.

Irrespective of
                                          			 whether the SCCP phone is in logged out or logged in state, any dn of that
                                          			 phone joining any voice hunt group retains its previous state (logged out or
                                          			 logged in). For example, if dn 8002 is member of voice hunt group 1 in logged
                                          			 out state, then 8002 remains in logged out state on joining voice hunt group 2.
                                          			 If dn 8001 on the same phone (which was not part of any hunt group) joins any
                                          			 voice hunt group, it is in logged in state.

From Cisco Unified
                                             		  CME Release 11.6 onwards, line level logout or login using FAC *4 is not
                                             		  supported for SIP phones (only supported on SCCP phones). SIP phones only
                                             		  support phone level logout or login using FAC *5.

Use hlog-block command under voice
                                       			 hunt-group for Agent Status Control. If you enable this command
                                 		under voice
                                       			 hunt-group , the logout or login functionality for voice
                                 		hunt-group is disabled. For example, you can use hlog-block command in voice hunt-groups where logout or login functionality using HLog
                                 		softkey (or by using FAC) needs to be restricted. By default, hlog-block command is disabled.

#### Members Logout for
                              	 Ephone Hunt Group

All members configured under an ephone-hunt are initialized with HLogin
                                 		by default. The non-shared static members or agents in an ephone hunt group can
                                 		be configured with the Hlogout initial state using the Members Logout feature.
                                 		You can use the CLI command members logout configured under ephone-hunt
                                 		configuration mode to enable the feature. From Cisco Unified CME Release 9.1,
                                 		members logout is supported for ephone hunt groups.

Members logout cannot be used for shared DNs. Also, this feature is not
                                 		supported if the CLI commands list and hunt-group logout DND are configured.

#### Members Logout for
                              	 Voice Hunt Group

All members
                                 		configured in a voice hunt group are initialized with HLogin by default. The
                                 		non-shared static members or agents in a voice hunt group can be configured
                                 		with the Hlogout initial state using members logout functionality. You can use
                                 		the CLI command members
                                       			 logout configured under voice hunt group configuration mode to
                                 		enable the feature. From Cisco Unified CME Release 11.6, members logout is
                                 		supported in voice hunt groups.

If any member of a
                                 		hunt group in a SIP phone logs out using the CLI command members
                                       			 logout , all other DN's of that phone in any hunt group are also
                                 		logged out. This is because SIP phones only support phone level logout. For
                                 		SCCP phones, only the DN that is configured with the CLI command members
                                       			 logout is logged out from the hunt group. Other member DN's do
                                 		not logout as SCCP phones support line level logout.

Members logout
                                 		cannot be used for shared DNs. The feature is not supported if the CLI command hunt-group logout DND is configured. Also, you cannot configure the CLI
                                 		command members logout if the command list is
                                 		configured.

#### Automatic Agent
                              	 Status Not-Ready for Ephone Hunt Group

Before
                                 		Cisco Unified CME 4.0, this feature was known as Automatic Hunt Group Logout.
                                 		If the auto logout command was enabled for a hunt group, a phone was placed in DND mode when a
                                 		line on the phone did not answer a call for that hunt group within the time
                                 		limit specified in the timeout command.

In
                                 		Cisco Unified CME 4.0 and later versions, the name and behavior of this feature
                                 		has changed, although the Cisco IOS command remains the same. The auto logout command now specifies the number of unanswered hunt group calls after which the
                                 		agent status of an directory number is automatically changed to not-ready. You
                                 		can limit Automatic Agent Status Not-Ready to dynamic hunt group members (those
                                 		who log in using a wildcard slot in the list command)
                                 		or to static hunt group members (those who are explicitly named in the list command), or you can apply this behavior to all hunt group members.

A related command, hunt-group
                                       			 logout , specifies whether the phones that are automatically
                                 		changed to the not-ready status should also be placed into DND mode. Phones in
                                 		the not-ready status do not accept calls from hunt groups, but they do accept
                                 		calls that directly dial their extensions. Phones in DND mode do not accept any
                                 		calls. The default if the hunt-group
                                       			 logout command is not used is that the phones that are
                                 		automatically placed in the not-ready status are also placed in DND mode.

Agents whose phones
                                 		are automatically placed into the not-ready status do not relinquish their
                                 		slots in the hunt group list.

#### Automatic Agent
                              	 Status Not-Ready for Voice Hunt Group

From
                                 		Cisco Unified CME Release 11.6, Automatic Hunt Group Logout is supported on
                                 		voice hunt groups. If the auto logout CLI command is enabled for a hunt group, it specifies the number of successive
                                 		unanswered hunt group calls after which the agent status of an directory number
                                 		is automatically changed to not-ready. The range for the number of unanswered
                                 		rings configured under auto logout command is 1 to 20. If auto logout is not configured with any value, the
                                 		default value of 1 is applied.

When the auto logout command is enabled under voice hunt group, the auto logout behavior applies to
                                 		all hunt group members (including static and dynamic members).

A related command, hunt-group
                                       			 logout , specifies whether the phones are automatically changed to
                                 		the not-ready status. Phones in the not-ready state do not accept calls from
                                 		hunt groups, but they do accept calls that directly dial their extensions.

If hunt group logout
                                       			 HLog is configured, then the DNs of that hunt group will go to
                                 		logout state when the number of unanswered rings specified under auto logout command is exceeded. If hunt group logout
                                       			 DND is configured, then phone goes to DND mode and logs out the
                                 		DND member when the number of unanswered rings specified under auto logout command is exceeded. If any hunt group members are logged out, they can use
                                 		HLog Softkey, FAC, Feature Button, or DND softkey to login again.

Agents whose phones
                                 		are automatically placed into the not-ready status do not relinquish their
                                 		slots in the hunt group list. When an agent returns to ready status, the voice
                                 		hunt group resumes sending calls to the agent’s DN.

Consider a voice
                                 		hunt group in sequential, peer, or longest idle configuration mode with call
                                 		hunt in progress. Then, auto logout count is incremented for agents who do not
                                 		answer the call. The auto logout count is not incremented for agents who answer
                                 		the call. In this scenario, the agent can be either an SCCP DN or a SIP DN.

Consider a voice
                                 		hunt group in parallel configuration mode with call blast in progress to all
                                 		logged in DN’s in the hunt group. If call is answered by any of the agents,
                                 		then the remaining agents in that hunt group will not have auto logout count
                                 		incremented. However, if call is not answered by any of the agents, then the
                                 		auto logout count will be incremented for all the logged in agents. Here, agent
                                 		can be either a SCCP DN or SIP DN.

#### All Agents Logged
                              	 Out Display on SIP Phones

From Unified CME
                                 		12.2 release, All agents
                                    		  logged out status message is displayed on SIP phones. The feature
                                 		is supported on Cisco 8800 Series IP Phones for Unified CME on Cisco 4000
                                 		Series Integrated Services Routers. For example, consider a voice hunt group
                                 		with three directory numbers (DN) 4002, 4003, and 4004, configured in three
                                 		different IP phones. When the last member of the voice hunt group is logged
                                 		out, the message, All agents
                                    		  logged out displays at the line level for all the members in the
                                 		hunt group. If one of the DNs in the voice hunt group with all members logged
                                 		out has call forward all enabled as well, then the line level display on the
                                 		phone toggles between the All agents
                                    		  logged out and the Forwarded
                                    		  to directory
                                       			 number messages. The duration of message display before
                                 		toggling is 1.5 seconds. Localization is supported for the All Agents Logged
                                 		Out Display on SIP Phones. For more information, see the figure.

#### Presentation of
                              	 Calls for Ephone Hunt Group

For phones configured under ephone hunt group configuration mode,
                                 		presentation of calls is supported using the CLI command, present-call . When the CLI command is configured, calls from the
                                 		ephone hunt group are presented only if all lines are on hook or in idle state.

If you configure idle-phone as the sub-mode option of the CLI
                                 		command present-call , calls from the ephone-hunt group are presented only if
                                 		all lines are idle on the phone on which the hunt-group line appears. This
                                 		option does not consider monitored lines that have been configured on the phone
                                 		using the button m command.

If you configure onhook-phone as the sub-mode option of the CLI
                                 		command present-call , calls from the ephone-hunt group are presented only if
                                 		the phone on which the number appears is in onhook state. When this keyword is
                                 		configured, calls in the ringing or hold state that are unrelated to the hunt
                                 		group do not prevent the presentation of calls from the ephone-hunt group.

#### Presentation of
                              	 Calls for Voice Hunt Group

For phones
                                 		configured under voice hunt group configuration mode, presentation of calls is
                                 		supported using the CLI command present-call . The feature is supported from Cisco Unified CME Release
                                 		11.6 onwards. When the present-call CLI command is configured, calls from the voice hunt
                                 		group are presented only if all lines are idle on the phone on which the hunt
                                 		group line appears.

If the present-call CLI command is not configured, voice hunt group calls
                                 		are presented without considering the status of other phone lines on the phone.
                                 		Hence, voice hunt group presents calls to an ephone or voice register pool
                                 		whenever the phone line (ephone-dn or voice register dn) that corresponds to a
                                 		number in a voice hunt group list is available. Hence, when you configure the present-call CLI command, you get the additional control to ensure
                                 		that hunt group calls do not possibly go unanswered.

### Night
                           	 Service

The night-service
                              		feature allows you to provide coverage for unstaffed extensions during hours
                              		that you designate as “night-service” hours. During the night-service hours,
                              		calls to the designated extensions, known as night-service directory numbers or
                              		night-service lines, send a special “burst” ring (for SCCP phones and SIP
                              		phones) to night-service phones that have been specified to receive this
                              		special ring. Phone users at the night-service phones can then use the
                              		call-pickup feature to answer the incoming calls from the night-service
                              		directory numbers.

For example, the
                              		night-service feature can allow an employee working after hours to intercept
                              		and answer calls that are presented to an unattended receptionist’s phone. This
                              		feature is useful for sites at which all incoming public switched telephone
                              		network (PSTN) calls have to be transferred by a receptionist. This is because
                              		all the Direct Inward Dialing (DID) calls are not published to PSTN for Cisco
                              		Unified CME system. When a call arrives at the unattended receptionist’s phone
                              		during hours that are specified as night service, a ring burst notifies a
                              		specified set of phones of the incoming call. A phone user at any of the
                              		night-service phones can intercept the call using the call-pickup feature.
                              		Night-service call notification is sent every 12 seconds until the call is
                              		either answered or aborted.

A user can enter a
                              		night-service code to manually toggle night-service treatment off and on from
                              		any phone that has a line assigned to night service. Before Cisco CME 3.3,
                              		using the night-service code turns night service on or off only for directory
                              		numbers on the phone at which the code is entered. In Cisco CME 3.3 and later
                              		versions, using the night-service code at any phone with a night-service
                              		directory number turns night service on or off for all phones with
                              		night-service directory numbers. From Unified CME 11.5 onwards, night service
                              		feature is supported on SIP phones along with SCCP phones.

Mixed deployment of
                              		SIP and SCCP phones is supported from Cisco Unified CME Release 11.6. Any
                              		combination of SIP and SCCP phones are supported across incoming call,
                              		unstaffed DNs, and agent phones. For DNs in which night service is enabled,
                              		notifications are sent to both SIP and SCCP phones that are designated as night
                              		service agents in a mixed deployment.

Night Service
                                 		  for SCCP Phones illustrates night service for SCCP phones.

Night Service
                                 		  for SIP Phones illustrates night service for SIP phones.

### Overlaid
                           	 Ephone-dns

Overlaid ephone-dns
                              		are directory numbers that share the same button on a phone. Overlaid
                              		ephone-dns can be used to receive incoming calls and place outgoing calls. Up
                              		to 25 ephone-dns can be assigned to a single phone button. They can have the
                              		same extension number or different numbers. The same ephone-dns can appear on
                              		more than one phone and more than one phone can have the same set of overlaid
                              		ephone-dns.

The order in which
                              		overlaid ephone-dns are used by incoming calls can be determined by the call
                              		hunt commands, preference and huntstop . For
                              		example, ephone-dn 1 to ephone-dn 4 have the same extension number, 1001. Three
                              		phones are configured with the button
                                    			 1o1,2,3,4 command. A call to 1001 will ring on the ephone-dn with
                              		the highest preference and display the caller ID on all phones that are on
                              		hook. If another incoming call to 1001 is placed while the first call is active
                              		(and the first ephone-dn with the highest preference is configured with the no huntstop command), the second call will roll over to the ephone-dn with the next-highest
                              		preference, and so forth. For more information, see Call Hunt .

If the ephone-dns
                              		in an ephone-dn overlay use different numbers, incoming calls go to the
                              		ephone-dn with the highest preference. If no preferences are configured, the dial-peer
                                    			 hunt command setting is used to determine which ephone-dns are
                              		used for incoming calls. The default setting for the dial-peer
                                    			 hunt command is to randomly select an ephone-dn that matches the
                              		called number.

To continue or to
                                          		  stop the search for ephone-dns, you must use, respectively, the no huntstop and huntstop commands under the individual ephone-dns. The huntstop setting is applied only
                                          		  to the dial peers affected by the ephone-dn command in telephony-service mode. Dial peers
                                          		  configured in global configuration mode comply with the global configuration
                                          		  huntstop setting.

Overlaid
                                 		  Ephone-dn (Simple Case) shows an overlay set with two directory numbers and one number that is shared
                              		on two phones. Ephone-dn 17 has a default preference value of 0, so it will
                              		receive the first call to extension 1001. The phone user at phone 9 answers the
                              		call, and a second incoming call to extension 1001 can be answered on phone 10
                              		using directory number 18.

When a call is
                              		answered on an ephone-dn, that ephone-dn is no longer available to other phones
                              		that share the ephone-dn in overlay mode. For example, if extension 1001 is
                              		answered by phone 1, caller ID for extension 1001 displays on phone 1 and is
                              		removed from the screens of phone 2 and phone 3. All actions pertaining to the
                              		call to extension 1001 (ephone-dn 17) are displayed on phone 1 only. If phone 1
                              		puts extension 1001 on hold, the other phones will not be able to pick up the
                              		on-hold call using a simple shared-line pickup. In addition, none of the other
                              		four phones will be able to make outgoing calls from the ephone-dn while it is
                              		in use. When phone users press button 1, they will be connected to the next
                              		available ephone-dn listed in the button command. For example, if phone 1 and phone 2 are using ephone-dn 1 and
                              		ephone-dn 2, respectively, phone 3 must pick up ephone-dn 3 for an outgoing
                              		call.

If there are more
                              		phones than ephone-dns associated with an ephone-dn overlay set, it is possible
                              		for some phones to find that all the ephone-dns within their overlay set are in
                              		use by other phones. For example, if five phones have a line button configured
                              		with the button 1o1, 2,
                                    			 3 command, there may be times when all three of the ephone-dns in
                              		the overlay set are in use. When that occurs, the other two phones will not be
                              		able to use an ephone-dn in the overlay set. When all ephone-dns in an overlay
                              		set are in use, phones with this overlay set will display the
                              		remote-line-in-use icon (a picture of a phone with a flashing X through it) for
                              		the corresponding line button. When at least one ephone-dn becomes available
                              		within the overlay set (that is, an ephone-dn is either idle or ringing), the
                              		phone display reverts to showing the status of the available ephone-dn (idle or
                              		ringing).

#### Shared- Line
                              	 Overlays

Dual-line ephone-dns
                                 		can also use overlays. The configuration parameters are the same as for
                                 		single-line ephone-dns, except that the huntstop
                                       			 channel command must be used to keep calls from hunting to the
                                 		ephone-dn’s second channel.

The primary
                                 		ephone-dn in a shared-line overlay set should be unique to the phone to
                                 		guarantee that the phone has a line available for outgoing calls, and to ensure
                                 		that the phone user can obtain dial-tone even when there are no idle lines
                                 		available in the rest of the shared-line overlay set. Use a unique ephone-dn to
                                 		provide for a unique calling party identity on outbound calls made by the phone
                                 		so that the called user can see which specific phone is calling.

The following
                                 		example shows the configuration for a simple shared-line overlay set. The
                                 		primary ephone-dn that is configured for each phone is unique while the
                                 		remaining ephone-dns 10, 11, and 12 are shared in the overlay set on both
                                 		phones.

```
ephone 1
```

```
mac-address 1111.1111.1111
```

```
button 1o1,10,11,12
```

```
!
```

```
ephone 2
```

```
mac-address 2222.2222.2222
```

```
button 1o2,10,11,12
```

A more complex
                                 		directory number configuration mixes overlaid directory numbers with shared
                                 		directory numbers and plain dual-line directory numbers on the same phones. Overlaid
                                    		  Ephone-dn (Complex Case) illustrates the following example of a manager with two assistants. On the
                                 		manager’s phone the same number, 2001, appears on button 1 and button 2. The
                                 		two line appearances of extension 2001 use two single-line directory numbers,
                                 		so the manager can have two active calls on this number simultaneously, one on
                                 		each button. The directory numbers are set up so that button 1 will ring first,
                                 		and if a second call comes in, button 2 will ring. Each assistant has a
                                 		personal directory number and also shares the manager’s directory numbers.
                                 		Assistant 1 has all three directory numbers in an overlay set on one button,
                                 		whereas assistant 2 has one button for the private line and a second button
                                 		with both of the manager’s lines in an overlay set. A sequence of calls might
                                 		be as follows.

An incoming call
                                       			 is answered by the manager on extension 2001 on button 1 (directory number 20).

A second call
                                       			 rings on 2001 and rolls over to the second button on the manager’s phone
                                       			 (directory number 21). It also rings on both assistants’ phones, where it is
                                       			 also directory number 21, a shared directory number.

Assistant 2
                                       			 answers the call. This is a shared overlay line (one directory number, 21, is
                                       			 shared among three phones, and on two of them this directory number is part of
                                       			 an overlay set). Because it is shared with button 2 on the manager’s phone, the
                                       			 manager can see when assistant 2 answers the call.

Assistant 1
                                       			 makes an outgoing call on directory number 22. The button is available because
                                       			 of the additional directory numbers in the overlay set on the assistant 1
                                       			 phone.

At this point, the
                                 		manager is in conversation on directory number 20, assistant 1 is in
                                 		conversation on directory number 22, and assistant 2 is in conversation on
                                 		directory number 21.

For configuration
                                 		information, see Configure Overlaid Ephone-dns on SCCP Phones .

#### Call Waiting for
                              	 Overlaid Ephone-dns

Call waiting allows
                                 		phone users to know that another person is calling them while they are talking
                                 		on the phone. Phone users hear a call-waiting tone indicating that another
                                 		party is trying to reach them. Calls to IP phones with soft keys can be
                                 		answered with the Answer soft key. Calls to analog phones are answered using
                                 		hookflash. When phone users answer a call-waiting call, their original call is
                                 		automatically put on hold. If phone users ignore a call-waiting call, the
                                 		caller is forwarded if call-forward no-answer has been configured.

In Cisco CME 3.2.1
                                 		and later versions, call waiting is available for overlaid ephone-dns. The
                                 		difference in configuration between overlaid ephone-dns with call waiting and
                                 		overlaid ephone-dns without call waiting is that overlaid ephone-dns with call
                                 		waiting use the c keyword in the button command and overlaid ephone-dns without
                                 		call waiting use the o keyword. For configuration information, see Configure Overlaid Ephone-dns on SCCP Phones .

The behavior of
                                 		overlaid ephone-dns with call waiting and overlaid ephone-dns without call
                                 		waiting is the same, except for the following:

Calls to numbers
                                       			 included in overlaid ephone-dns with call waiting will cause inactive phones to
                                       			 ring and active phones connected to other parties to generate auditory
                                       			 call-waiting notification. The default sound is beeping, but you can configure
                                       			 an ephone-dn to use a ringing sound. (See Configure Call-Waiting Indicator Tone on SCCP Phone .)
                                       			 Visual call-waiting notification includes the blinking of handset indicator
                                       			 lights and the display of caller IDs.

For example, if
                                       			 three of four phones are engaged in calls to numbers from the same overlaid
                                       			 ephone-dn with call-waiting and another call comes in, the one inactive phone
                                       			 will ring, and the three active phones will issue auditory and visual
                                       			 call-waiting notification.

In
                                       			 Cisco Unified CME 4.0 and later versions, up to six waiting calls can be
                                       			 displayed on Cisco Unified IP Phone 7940G, 7941G, 7941G-GE, 7960G, 7961G,
                                       			 7961G-GE, 7970G, and 7971G-GE. For all other phones and earlier
                                       			 Cisco Unified CME versions, two calls to numbers in an overlaid ephone-dn set
                                       			 can be announced. Subsequent calls must wait in line until one of the two
                                       			 original calls has ended. The callers who are waiting in the line will hear a
                                       			 ringback tone.

For example, a
                                 		Cisco Unified IP Phone 7910 (maximum two call-waiting calls) has a button
                                 		configured with a set of overlaid ephone-dns with call waiting ( button 1c1,2,3,4 ). A call to ephone-dn 1 is
                                 		answered. A call to ephone-dn 2 generates call-waiting notification. Calls to
                                 		ephone-dn 3 and ephone-dn 4 will wait in line and remain invisible to the phone
                                 		user until one of the two original calls ends. When the call to ephone-dn 1
                                 		ends, the phone user can then talk to the person who called ephone-dn 2. The
                                 		call to ephone-dn 3 issues call-waiting notification while the call to
                                 		ephone-dn 4 waits in line. (The Cisco Unified IP Phone 7960 supports six calls
                                 		waiting.) Phones configured for call waiting do not generate call-waiting
                                 		notification when they are transferring calls or hosting conference calls.

Note that if an
                                 		overlaid ephone-dn has call-forward-no-answer configured, calls to the
                                 		ephone-dn that are unanswered before the no-answer timeout expires are
                                 		forwarded to the configured destination. If call-forward-no-answer is not
                                 		configured, incoming calls receive ringback tones until the calls are answered.

More than one phone
                                 		can use the same set of overlaid ephone-dns. In this case, the call-waiting
                                 		behavior is slightly different. The following example demonstrates call waiting
                                 		for overlaid ephone-dns that are shared on two phones:

```
ephone 1
```

```
button 1c1,2,3,4
```

```
!
```

```
ephone 2
```

```
button 1c1,2,3,4
```

A call to
                                       			 ephone-dn 1 rings on ephone 1 and on ephone 2. Ephone 1 answers, and the call
                                       			 is no longer visible to ephone 2.

A call to
                                       			 ephone-dn 2 issues a call-waiting notification to ephone 1 and rings on ephone
                                       			 2, which answers. The second call is no longer visible to ephone 1.

A call to
                                       			 ephone-dn 3 issues a call-waiting notification to ephone 1 and ephone 2. Ephone
                                       			 1 puts the call to ephone-dn 1 on hold and answers the call to ephone-dn 3. The
                                       			 call to ephone-dn 3 is no longer visible to ephone 2.

A call to
                                       			 ephone-dn 4 is issues a call-waiting notification on ephone 2. The call is not
                                       			 visible on ephone 1 because it has met the two-call maximum by handling the
                                       			 calls to ephone-dn 1 and ephone-dn 3. (Note that the call maximum is six for
                                       			 those phones that are able to handle six call-waiting calls, as previously
                                       			 described.)

Ephone-dns accept
                                             		  call interruptions, such as call waiting, by default. For call waiting to work,
                                             		  the default must be active. For more information, see Configure Call-Waiting Indicator Tone on SCCP Phone .

#### Extend Calls for
                              	 Overlaid Ephone-dns to Other Buttons on the Same Phone

Phones with overlaid
                                 		ephone-dns can use the button command with the x keyword to
                                 		dedicate one or more additional buttons to receive overflow calls. If an
                                 		overlay button is busy, an incoming call to any of the other ephone-dns in the
                                 		overlay set rings on the first available overflow button on each phone that is
                                 		configured to receive the overflow. This feature works only for overlaid
                                 		ephone-dns that are configured with the button command and the o keyword; it
                                 		is not supported with overlaid ephone-dns that are configured using the button command and the c keyword or
                                 		other types of ephone-dns that are not overlaid.

Using the button command with the c keyword
                                 		results in multiple calls on one button (the button is overlaid with multiple
                                 		ephone-dns that have call waiting), whereas using the button command with the o keyword and
                                 		the x keyword
                                 		results in one call per button and calls on multiple buttons.

For example, an
                                 		ephone has an overlay button with ten numbers assigned to it using the button command and the o keyword.
                                 		The next two buttons on the phone are configured using the button command and the x keyword.
                                 		These buttons are reserved to receive additional calls to the overlaid
                                 		extensions on the first button when the first button is in use.

```
ephone 276
```

```
button 1o24,25,26,27,28,29,30,31,32,33 2x1 3x1
```

For configuration
                                 		information, see Configure Overlaid Ephone-dns on SCCP Phones .

## Configure Call Coverage Features

### Configure Call
                           	 Hunt on SCCP Phones

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn dn-tag [ dual-line ]

- number number [ secondary number ] [ no-reg [ both | primary ] ]

- preference preference-order [ secondary secondary-order ]

- no huntstop or huntstop

- huntstop channel

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

ephone-dn dn-tag [ dual-line ]

#### Example:

```
Router(config)# ephone-dn 20 dual-line
```

Enters
                                             				ephone-dn configuration mode for the purpose of configuring a directory number.

Step 4

number number [ secondary number ] [ no-reg [ both | primary ] ]

#### Example:

```
Router(config-ephone-dn)# number 101
```

Associates a
                                             				telephone or extension number with the directory number.

Assign the
                                                   					 same number to several primary or secondary ephone-dns to create a group of
                                                   					 virtual dial peers through which the incoming called number must search.

Step 5

preference preference-order [ secondary secondary-order ]

#### Example:

```
Router(config-ephone-dn)# preference 2
```

Sets the preference value for the ephone-dn.

Default: 0.

Increment the preference order for subsequent ephone-dns with the same number. That is, the first directory number is preference 0 by default and you must specify 1 for the second ephone-dn with the same number, 2 for the next, and so on.

secondary secondary-order —(Optional) Preference value for the secondary number of an ephone-dn. Default is 9.

Step 6

no huntstop or huntstop

#### Example:

```
Router(config-ephone-dn)# no huntstop
```

or

```
Router(config-ephone-dn)# huntstop
```

Explicitly
                                             				enables call hunting behavior for a directory number.

Configure no huntstop for all ephone-dns, except the final ephone-dn, within a set of ephone-dns with
                                                   					 the same number.

Configure the huntstop command for the final ephone-dn within a set of ephone-dns with the same
                                                   					 number.

Step 7

huntstop channel

#### Example:

```
Router(config-ephone-dn)# huntstop channel
```

(Optional)
                                             				Enables channel huntstop, which keeps a call from hunting to the next channel
                                             				of a directory number if the first channel is busy or does not answer.

Required
                                                   					 for dual-line ephone-dns that are used for call hunting.

Step 8

end

#### Example:

```
Router(config-ephone-dn)# end
```

#### What to do next

If you want to collect statistics for hunt groups, see Cisco Unified CME B-ACD and Tcl Call-Handling Applications .

### Verify Call Hunt
                           	 Configuration on SCCP Phones

To verify the
                                 		  configuration for call hunt, perform the following steps.

### SUMMARY STEPS

- show running-config

- show telephony-service ephone-dn

- show telephony-service
                                       				  all or show
                                       				  telephony-service dial-peer

### DETAILED STEPS

Step 1

show running-config

This command
                                             				displays your configuration. Preference and huntstop information is listed in
                                             				the ephone-dn portion of the output.

```
Router# show running-config
```

```
ephone-dn  2  dual-line
```

```
number 126
```

```
description FrontDesk
```

```
name Receptionist
```

```
preference 1
```

```
call-forward busy 500
```

```
huntstop channel
```

```
no huntstop
```

Step 2

show telephony-service ephone-dn

This command
                                             				displays ephone-dn preference and huntstop configuration information.

Step 3

show telephony-service
                                                				  all or show
                                                				  telephony-service dial-peer

These commands
                                             				display preference and huntstop configurations for ephone-dn dial peers.

```
Router# show telephony-service dial-peer
```

```
!
```

```
dial-peer voice 20026 pots
```

```
destination-pattern 5002
```

```
huntstop
```

```
call-forward noan 5001 timeout 45
```

```
port 50/0/2
```

### Configure Call
                           	 Hunt on SIP Phones

To configure the
                                 		  call hunting feature and prevent hunt-on-busy from redirecting a call from a
                                 		  busy phone into a dial peer that has been setup with a catch-all default
                                 		  destination, perform the following steps.

### SUMMARY STEPS

- enable

- configure terminal

- voice register dn dn-tag

- number number

- preference preference-order

- huntstop

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

voice register dn dn-tag

#### Example:

```
Router(config)# voice register dn 1
```

Enters voice
                                             				register dn configuration mode to define a directory number for a SIP phone,
                                             				intercom line, voice port, or an MWI.

Step 4

number number

#### Example:

```
Router(config-register-dn)# number 5001
```

Associates a
                                             				phone number with the directory number.

Assign the
                                                   					 same number to several directory numbers to create a group of virtual dial
                                                   					 peers through which the incoming called number must search.

Step 5

preference preference-order

#### Example:

```
Router(config-register-dn)# preference 4
```

Creates the
                                             				preference order for matching the VoIP dial peers created for the number
                                             				associated with this directory number to establish the hunt strategy for
                                             				incoming calls.

Default is
                                                   					 0, which is the highest preference.

Step 6

huntstop

#### Example:

```
Router(config-register-dn)# huntstop
```

Disables
                                             				call-hunting behavior for an extension on a SIP phone.

Step 7

end

#### Example:

```
Router(config-register-dn)# end
```

Exits
                                             				configuration mode and enters privileged EXEC mode.

#### What to do next

If you want to
                                 		  collect statistics for hunt groups, see Cisco Unified CME B-ACD and Tcl Call-Handling
                                    			 Applications .

### Enable Call
                           	 Pickup

To enable Call
                                 		  Pickup features on SCCP or SIP phones, perform the following steps.

Restriction

SIP phones
                                                   				  that do not support the PickUp and GpickUp soft keys must use feature access
                                                   				  codes (FACs) to access these features.

Different
                                                   				  directory numbers with the same extension number must have the same Pickup
                                                   				  configuration.

A directory
                                                   				  number can be assigned to only one pickup group.

Pickup group
                                                   				  numbers can vary in length, but must have unique leading digits. For example,
                                                   				  if you configure group number 17, you cannot also configure group number 177.
                                                   				  Otherwise a pickup in group 17 is always triggered before the user can enter
                                                   				  the final 7 for 177.

Calls from
                                                   				  H.323 trunks are not supported on SIP phones.

#### Before you begin

It is mandatory to configure the CLI command call-park system application under telephony-service to enable or disable Call Pickup functionality using call pickup feature on SIP phones.

SIP phones require Cisco Unified CME 7.1 or a later version.

The PickUp and GPickUp soft keys display by default on supported SCCP and SIP phones. If previously disabled, you must enable
                                       these soft keys with the softkeys idle command.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- call-park system application

- service directed-pickup [ gpickup ]

- fac { standard | custom pickup { direct | group | local } custom-fac }

- exit

- ephone-dn dn-tag [ dual-line | octo-line ] or voice register dn dn-tag

- pickup-group group-number

- pickup-call
                                       				  any-group

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

Enter your password if prompted.

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

call-park system application

#### Example:

```
Router(config-telephony)# call-park system application
```

Enables or disables Call Pickup functionality using call pickup feature on SIP phones.

Step 5

service directed-pickup [ gpickup ]

#### Example:

```
Router(config-telephony)# service directed-pickup gpickup
```

Enables Directed Call Pickup and modifies the function of the GPickUp and PickUp soft keys.

gpickup —(Optional) Enables using the GPickUp soft key to perform Directed Call Pickup on SCCP phones. This keyword is supported in
                                                   Cisco Unified CME 7.1 and later versions.

This command determines the specific soft keys used to access different Call Pickup features on SCCP and SIP phones. For a
                                                   description, see the service directed-pickup command in the Cisco Unified CME Command Reference .

Step 6

fac { standard | custom pickup { direct | group | local } custom-fac }

#### Example:

```
Router(config-telephony)# fac custom pickup group #35
```

Enables
                                             				standard FACs or creates a custom FAC or alias for Pickup features on SCCP and
                                             				SIP phones.

standard —Enables standard FACs for all phones.
                                                   					 Standard FAC for Park Retrieval is **10.

custom —Creates a custom FAC for a feature.

custom-fac —User-defined code to dial using the
                                                   					 keypad on an IP or analog phone. Custom FAC can be up to 256 characters and
                                                   					 contain numbers 0 to 9 and * and #.

Step 7

exit

#### Example:

```
Router(config-telephony)# exit
```

Returns to
                                             				privileged EXEC mode.

Step 8

ephone-dn dn-tag [ dual-line | octo-line ] or voice register dn dn-tag

#### Example:

```
Router(config)# ephone-dn 20 dual-line
```

or

```
Router(config)# voice register dn 20
```

Enters directory number configuration mode.

Step 9

pickup-group group-number

#### Example:

```
Router(config-ephone-dn)# pickup-group 30
```

or

```
Router(config-register-dn)# pickup-group 30
```

Creates a
                                             				pickup group and assigns the directory number to the group.

group-number —String of up to 32 characters. Group
                                                   					 numbers can vary in length but must have unique leading digits. For example, if
                                                   					 there is a group number 17, there cannot also be a group number 177.

This
                                                   					 command can also be configured in ephone-dn-template configuration mode and
                                                   					 applied to one or more ephone-dns. The ephone-dn configuration has priority
                                                   					 over the template configuration.

Step 10

pickup-call
                                                				  any-group

#### Example:

```
Router(config-ephone-dn)# pickup-call any-group
```

or

```
Router(config-register-dn)# pickup-call any-group
```

Enables a
                                             				phone user to pickup ringing calls on any extension belonging to a pickup group
                                             				by pressing the GPickUp soft key and asterisk (*).

The ringing extension must be configured with a pickup group using the pickup-group command.

If this
                                                   					 command is not configured, the user can pickup calls in other groups by
                                                   					 pressing the GPickUp soft key and dialing the pickup group number.

Step 11

end

#### Example:

```
Router(config-ephone-dn)# end
```

or

```
Router(config-register-dn)# end
```

Exits
                                             				configuration mode.

#### Example

The following
                                 		  example shows the Group Pickup and Local Group Pickup features enabled with the service
                                       				directed-pickup gpickup command. Extension 1005 on phone 5 and extension 1006 on
                                 		  phone 6 are assigned to pickup group 1.

```
telephony-service
load 7960-7940 P00308000500
load E61 SCCP61.8-2-2SR2S
max-ephones 100
max-dn 240
ip source-address 15.7.0.1 port 2000
service directed-pickup gpickup
cnf-file location flash:
cnf-file perphone
voicemail 8900
max-conferences 8 gain -6
call-park system application
transfer-system full-consult
fac standard
create cnf-files version-stamp 7960 Sep 25 2007 21:25:47
!
!
!
ephone-dn 5
number 1005
pickup-group 1
!
!
ephone-dn 6
number 1006
pickup-group 1
!
!
ephone 5
mac-address 0001.2345.6789
type 7962
button 1:5
!
!
!
ephone 6
mac-address 000F.F758.E70E
type 7962
button 1:6
```

### Configure
                           	 Call-Waiting Indicator Tone on SCCP Phone

To specify the
                                 		  type of audible call-waiting indicator on a SCCP phone, perform the following
                                 		  steps. The default is for directory numbers to accept call interruptions, such
                                 		  as call waiting, and to issue a beep tone. Instead of the standard call waiting
                                 		  beep, you can enable a ring tone for call-waiting.

Restriction

The
                                                   				  call-waiting ring option is not supported if the ephone-dn is configured with
                                                   				  the no call-waiting beep
                                                         						accept command.

If you
                                                   				  configure a button to have a silent ring, you will not hear a call-waiting beep
                                                   				  or call-waiting ring regardless of whether the ephone-dn associated with the
                                                   				  button is configured to generate a call-waiting beep or call-waiting ring. To
                                                   				  configure a button for silent ring, see Assign Directory Numbers to SCCP Phones .

The
                                                   				  call-waiting beep volume cannot be adjusted through Cisco Unified CME for the
                                                   				  Cisco Unified IP Phone 7902G, Cisco Unified IP Phone 7905G, Cisco Unified IP
                                                   				  Phone 7912G, Cisco ATA-186, and Cisco ATA-188.

The
                                                   				  call-waiting ring option is not supported on the Cisco Unified IP Phone 7902G,
                                                   				  Cisco Unified IP Phone 7905G, or Cisco Unified IP Phone 7912G.

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn dn-tag [ dual-line ]

- call-waiting beep [ accept | generate ]

- call-waiting ring

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

ephone-dn dn-tag [ dual-line ]

#### Example:

```
Router(config)# ephone-dn 20 dual-line
```

Enters
                                             				ephone-dn configuration mode, creates an ephone-dn, and optionally assigns it
                                             				dual-line status.

Step 4

call-waiting beep [ accept | generate ]

#### Example:

```
Router(config-ephone-dn)# no call-waiting beep accept
```

Enables an
                                             				ephone-dn to generate or accept call-waiting beeps.

Default is
                                                   					 directory number both accepts and generates call-waiting beep.

The beep
                                                   					 is heard only if the other ephone-dn is configured to accept call-waiting beeps
                                                   					 (default).

Step 5

call-waiting ring

#### Example:

```
Router(config-ephone-dn)# call-waiting ring
```

(Optional)
                                             				Enables an ephone-dn to use a ring indicator for call-waiting notification.

To use
                                                   					 this command, do not disable call-waiting beep by using the no call-waiting beep
                                                         						  accept command.

Step 6

end

#### Example:

```
Router(config-ephone-dn)# end
```

Returns to
                                             				privileged EXEC mode.

### Verify Call-Waiting Indicator Tone on SCCP Phone

Step 1

Use the show running-config command to verify your
                                             				configuration. Call-waiting settings are listed in the ephone-dn portion of the
                                             				output. If the no call-waiting beep generate and the no call-waiting beep accept commands are configured, the show running-config command output will display the no call-waiting beep command.

#### Example:

```
Router# show running-config
```

```
!
```

```
ephone-dn 3 dual-line
```

```
number 126
```

```
name Accounting
```

```
preference 2 secondary 9
```

```
huntstop
```

```
huntstop channel
```

```
call-waiting beep
```

```
!
```

Step 2

Use the show telephony-service ephone-dn command to display call-waiting
                                          			 configuration information.

#### Example:

```
Router# show telephony-service ephone-dn
```

```
ephone-dn 1 dual-line
```

```
number 126 secondary 1261
```

```
preference 0 secondary 9
```

```
no huntstop
```

```
huntstop channel
```

```
call-forward busy 500 secondary
```

```
call-forward noan 500 timeout 10
```

```
call-waiting beep
```

### Configure Cancel
                           	 Call Waiting on SCCP Phone

To enable a phone
                                 		  user to cancel call waiting by using the CWOff soft key or a FAC, perform the
                                 		  following steps.

Restriction

Call Waiting
                                                   				  must be disabled by pressing the CWOff soft key or using the FAC before placing
                                                   				  a call; it cannot be activated or deactivated during a call.

The CWOff
                                                   				  soft key is not available when initiating Call Transfer.

#### Before you begin

For information
                                 		  about standard and custom FACs, see Feature Access Codes .

### SUMMARY STEPS

- enable

- configure terminal

- ephone-template template-tag

- softkeys seized { [ CallBack ] [ Cfwdall ] [ CWOff ] [ Endcall ] [ Gpickup ] [ HLog ] [ MeetMe ] [ Pickup ] [ Redial ] }

- exit

- ephone phone-tag

- ephone-template template-tag

- exit

- telephony-service

- fac { standard | custom ccw custom-fac }

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

ephone-template template-tag

#### Example:

```
Router(config)# ephone-template 5
```

Enters
                                             				ephone-template configuration mode to create an ephone template.

template-tag —Unique identifier for the ephone
                                                   					 template. Range: 1 to 20.

Step 4

softkeys seized { [ CallBack ] [ Cfwdall ] [ CWOff ] [ Endcall ] [ Gpickup ] [ HLog ] [ MeetMe ] [ Pickup ] [ Redial ] }

#### Example:

```
Router(config-ephone-template)# softkeys seized CWOff Cfwdall Endcall Redial
```

(Optional)
                                             				Modifies the order and type of soft keys that display on an IP phone during the
                                             				seized call state.

You can
                                                   					 enter any of the keywords in any order.

Default is
                                                   					 all soft keys are displayed in alphabetical order.

Any soft
                                                   					 key that is not explicitly defined is disabled.

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
Router(config)# ephone 12
```

Enters
                                             				ephone configuration mode.

- phone-tag —Unique number that identifies this
                                                				  ephone during configuration tasks.

Step 7

ephone-template template-tag

#### Example:

```
Router(config-ephone)# ephone-template 5
```

Applies the
                                             				ephone template to the phone.

- template-tag —Unique identifier of the ephone
                                                				  template that you created in Step 3 .

Step 8

exit

#### Example:

```
Router(config-ephone)# exit
```

Exits ephone
                                             				configuration mode.

Step 9

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony-service configuration mode.

Step 10

fac { standard | custom ccw custom-fac }

#### Example:

```
Router(config-telephony)# fac custom ccw **8
```

Enables
                                             				standard FACs or creates a custom FAC or alias.

standard —Enables standard FACs for all phones.
                                                   					 Standard FAC for cancel call waiting is *1.

custom —Creates a custom FAC for a FAC type.

custom-fac —User-defined code to be dialed using
                                                   					 the keypad on an IP or analog phone. Custom FAC can be up to 256 characters
                                                   					 long and contain numbers 0 to  9 and * and #.

Step 11

end

#### Example:

```
Router(config-telephony)# end
```

Returns to
                                             				privileged EXEC mode.

#### Example

The following
                                 		  example shows a configuration where the order of the CWOff soft key is modified
                                 		  for the seized call state in ephone template 5 and assigned to ephone 12. A
                                 		  custom FAC for cancel call waiting is set to **8.

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
voicemail 8900
```

```
max-conferences 8 gain -6
```

```
transfer-system full-consult
```

```
fac custom cancel call waiting **8
```

```
!
```

```
!
```

```
ephone-template  5
```

```
softkeys seized CWOff Cfwdall Endcall Redial
```

```
!
```

```
!
```

```
ephone  12
```

```
ephone-template 5
```

```
mac-address 000F.9054.31BD
```

```
type 7960
```

```
button  1:10 2:7
```

### Enable Call
                           	 Waiting on SIP Phones

To enable call
                                 		  waiting on an individual SIP phone, perform the following steps.

#### Before you begin

Cisco Unified CME 3.4 or a later version.

mode cme command must be configured in Cisco Unified CME.

### SUMMARY STEPS

- enable

- configure terminal

- voice register pool pool-tag

- call-waiting

- exit

- voice register
                                       				  global

- hold-alert

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

voice register pool pool-tag

#### Example:

```
Router(config)# voice register pool 3
```

Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone in Cisco Unified CME.

Step 4

call-waiting

#### Example:

```
Router(config-register-pool)# call-waiting
```

Configures
                                             				call waiting on the SIP phone being configured.

- Default: Enabled.

Step 5

exit

#### Example:

```
Router(config-register-pool)# exit
```

Exits voice
                                             				register pool configuration mode.

Step 6

voice register
                                                				  global

#### Example:

```
Router(config)# voice register global
```

Enters voice
                                             				register global configuration mode to set parameters for all supported SIP
                                             				phones in Cisco Unified CME.

Step 7

hold-alert

#### Example:

```
Router(config-register-global)# hold-alert
```

Sets an audible alert notification when a call is on hold on a SIP phone. Default is disabled.

Step 8

end

#### Example:

```
Router(config-register-global)# end
```

Exits to
                                             				privileged EXEC mode.

### Configure
                           	 Ephone-Hunt Groups on SCCP Phones

To define a hunt
                                 		  group and optional agent availability parameters, perform the following steps.

Restriction

The HLog
                                                   				  soft key is available only on display phones. It is not available on
                                                   				  Cisco Unified IP Phones 7902, 7905, and 7912; Cisco IP Communicator; and
                                                   				  Cisco VG224.

Shared
                                                   				  ephone-dns cannot use the Agent Status Control or Automatic Agent Not-Ready
                                                   				  feature.

If directory
                                                   				  numbers that are members of a hunt group are configured for called-name
                                                   				  display, the following restrictions apply:

The primary or secondary pilot number must be defined using at least one wildcard character.

The phone numbers in the list command cannot contain wildcard characters.

If Call Forward All or Call Forward Busy is configured for a hunt group member (directory number), the hunt group ignores
                                                   it.

#### Before you begin

Directory numbers
                                 		  included in a hunt group must be configured in Cisco Unified CME. For
                                 		  configuration information, see Create Directory Numbers for SCCP Phones .

### SUMMARY STEPS

- enable

- configure terminal

- ephone-hunt hunt-tag { longest-idle | peer | sequential }

- pilot number [ secondary number ]

- list number [ , number ... ]

- final final-number

- hops number

- timeout seconds [ , seconds ... ]

- max-timeout seconds

- preference preference-order [ secondary secondary-order ]

- no-reg [ both | pilot ]

- fwd-final { orig-phone | final }

- forward
                                       				  local-calls

- secondary
                                       				  start [ current | next | list-position ]

- present-call { idle-phone | onhook-phone }

- from-ring

- description text-string

- display-logout text-string

- exit

- telephony-service

- max-redirect number

- hunt-group logout { DND | HLog }

- exit

- ephone-dn dn-tag

- ephone-hunt
                                       				  login

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

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ephone-hunt hunt-tag { longest-idle | peer | sequential }

#### Example:

```
Router(config)# ephone-hunt 23 peer
```

Enters
                                             				ephone-hunt configuration mode to define an ephone hunt group.

Cisco CME
                                                   					 3.3 and earlier—Range: 1 to 10

longest-idle —Calls go to the ephone-dn that has been idle
                                                   					 the longest for the number of hops specified when the ephone hunt group was
                                                   					 defined. The longest-idle is determined from the last time that a phone
                                                   					 registered, reregistered, or went on-hook.

peer —First ephone-dn to ring is the number to the right of
                                                   					 the ephone-dn that was the last to ring when the pilot number was last called.
                                                   					 Ringing proceeds in a circular manner, left to right, for the number of hops
                                                   					 specified when the ephone hunt group was defined.

sequential —Ephone-dns ring in the left-to-right order in
                                                   					 which they are listed when the hunt group is defined.

Step 4

pilot number [ secondary number ]

#### Example:

```
Router(config-ephone-hunt)# pilot 5601
```

Defines the
                                             				pilot number, which is the number that callers dial to reach the hunt group.

number —E.164 number up to 27 characters. The dialplan
                                                   					 pattern can be applied to the pilot number.

secondary —(Optional) Defines an additional pilot number for
                                                   					 the ephone hunt group.

Step 5

list number [ , number ... ]

#### Example:

```
Router(config-ephone-hunt)# list 5001, 5002, 5017, 5028
```

Defines the
                                             				list of numbers (from 2 and 20) to which the ephone hunt group redirects the
                                             				incoming calls.

number —E.164 number
                                                   					 up to 27 characters. Primary or secondary number assigned to an ephone-dn.

Step 6

final final-number

#### Example:

```
Router(config-ephone-hunt)# final 6000
```

Defines the
                                             				last number in the ephone hunt group, after which the call is no longer
                                             				redirected. Can be an ephone-dn primary or secondary number, a voice-mail pilot
                                             				number, a pilot number of another hunt group, or an FXS number.

Step 7

hops number

#### Example:

```
Router(config-ephone-hunt)# hops 7
```

(Optional;
                                             				peer and longest-idle hunt groups only) Sets the number of hops before a call
                                             				proceeds to the final number.

number —Number of hops
                                                   					 before the call proceeds to the final ephone-dn. Range is 2 to 20, but the
                                                   					 value must be less than or equal to the number of extensions that are specified
                                                   					 in the list command. Default automatically adjusts to the number of
                                                   					 hunt group members.

Step 8

timeout seconds [ , seconds ... ]

#### Example:

```
Router(config-ephone-hunt)# timeout 7, 10, 15
```

(Optional)
                                             				Sets the number of seconds after which an unanswered call is redirected to the
                                             				next number in the hunt-group list.

seconds —Number of seconds. Range: 3 to 60000.
                                                   					 Multiple entries can be made, separated by commas, that must correspond to the
                                                   					 number of ephone-dns in the list command. Each number in a multiple entry
                                                   					 specifies the time that the corresponding ephone-dn will ring before a call is
                                                   					 forwarded to the next number in the list. If a single number is entered, it is
                                                   					 used for the no-answer period for each ephone-dn.

If this
                                                   					 command is not used, the default is the number of seconds set by the timeouts ringing command, which defaults to 180 seconds. Note
                                                   					 that the default of 180 seconds may be greater than you desire.

Step 9

max-timeout seconds

#### Example:

```
Router(config-ephone-hunt)# max-timeout 25
```

(Optional)
                                             				Sets the maximum combined timeout for the no-answer periods for all ephone-dns
                                             				in the ephone-hunt list. The call proceeds to the final destination when this
                                             				timeout expires, regardless of whether it has completed the hunt cycle.

seconds —Number of seconds. Range is 3 to 60000.

If this
                                                   					 command is not used, the default is that no combined timeout limit is set.

Step 10

preference preference-order [ secondary secondary-order ]

#### Example:

```
Router(config-ephone-hunt)# preference 1
```

(Optional)
                                             				Sets a preference order for the ephone-dn associated with the hunt-group pilot
                                             				number.

preference-order —See the CLI help for a range of
                                                   					 numeric values, where 0 is the highest preference. Default is 0.

secondary secondary-order —(Optional) Preference order for the
                                                   					 secondary pilot number. See the CLI help for a range of numeric values, where 0
                                                   					 is the highest preference. Default is 7.

Step 11

no-reg [ both | pilot ]

#### Example:

```
Router(config-ephone-hunt)# no-reg
```

(Optional)
                                             				Prevents the hunt-group pilot number from registering with an H.323 gatekeeper.
                                             				If this command is not used, the default is that the pilot number registers
                                             				with the H.323 gatekeeper.

both —(Optional) Both
                                                   					 the primary and secondary pilot numbers are not registered.

pilot —(Optional) Only
                                                   					 the primary pilot number is not registered.

In
                                                   					 Cisco CME 3.1 and later versions, if this command is used without the either
                                                   					 the both or pilot keywords, only the secondary number is not
                                                   					 registered.

Step 12

fwd-final { orig-phone | final }

#### Example:

```
Router(config-ephone-hunt)# fwd-final orig-phone
```

(Optional)
                                             				For calls that have been transferred into an ephone hunt group by a local
                                             				extension, determines the final destination of a call that is not answered in
                                             				the hunt group.

final —Forwards the
                                                   					 call to the ephone-dn number that is specified in the final command.

orig-phone —Forwards
                                                   					 the call to the primary directory number of the phone that transferred the call
                                                   					 into the hunt group.

Step 13

forward
                                                				  local-calls

#### Example:

```
Router(config-ephone-hunt)# no forward local-calls
```

(Optional;
                                             				sequential hunt groups only) Specifies that local calls (calls from ephone-dns
                                             				on the same Cisco Unified CME system) will not be forwarded past the first list
                                             				member in a hunt group. If the first member is busy, the internal caller hears
                                             				busy. If the first number does not answer, the internal caller hears ringback.

Step 14

secondary
                                                				  start [ current | next | list-position ]

#### Example:

```
Router(config-ephone-hunt)# secondary start next
```

(Optional)
                                             				For calls that are parked by hunt group member phones, returns them to a
                                             				different entry point in the hunt group (as specified in this command) if the
                                             				calls are recalled from park to the secondary pilot number or transferred from
                                             				park to an ephone-dn that forwards the call to the secondary pilot number.

current —The ephone-dn
                                                   					 that parked the call.

next —The ephone-dn in
                                                   					 the hunt group list that follows the ephone-dn that parked the call.

list-position —The
                                                   					 ephone-dn at the specified position in the list specified by the list command. Range is 1 to 10.

Step 15

present-call { idle-phone | onhook-phone }

#### Example:

```
Router(config-ephone-hunt)# present-call idle-phone
```

(Optional)
                                             				Presents ephone-hunt-group calls only to member phones that are idle or onhook,
                                             				as specified.

idle-phone —A call
                                                   					 from the ephone-hunt group is presented to an ephone only if all lines on the
                                                   					 phone are idle. This option ignores monitored lines that have been configured
                                                   					 on the phone using the button
                                                      						m command.

onhook-phone —A call
                                                   					 from the ephone-hunt group is presented to an ephone only if the phone is in
                                                   					 the on-hook state. When this keyword is configured, calls in the ringing or
                                                   					 hold state that are unrelated to the hunt group do not prevent the presentation
                                                   					 of calls from the ephone-hunt group.

Step 16

from-ring

#### Example:

```
Router(config-ephone-hunt)# from-ring
```

(Optional)
                                             				Specifies that on-hook time stamps should be recorded when calls ring
                                             				extensions and when calls are answered. The default is that on-hook time stamps
                                             				are recorded only when calls are answered.

Step 17

description text-string

#### Example:

```
Router(config-ephone-hunt)# description Marketing Hunt Group
```

(Optional)
                                             				Defines text that will appear in configuration output.

Step 18

display-logout text-string

#### Example:

```
Router(config-ephone-hunt)# display-logout Night Service
```

(Optional)
                                             				Defines text that will appear on IP phones that are members of a hunt group
                                             				when all the hunt-group members are in the not-ready status. This string can be
                                             				used to inform hunt-group members where the calls are being sent when all
                                             				members are unavailable to take calls.

Step 19

exit

#### Example:

```
Router(config-ephone-hunt)# exit
```

Exits
                                             				ephone-hunt configuration mode.

Step 20

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony-service configuration mode.

Step 21

max-redirect number

#### Example:

```
Router(config-telephony)# max-redirect 8
```

(Optional)
                                             				Sets the number of times that a call can be redirected within a
                                             				Cisco Unified CME system.

number —Range is 5 to
                                                   					 20. Default is 10.

Step 22

hunt-group logout { DND | HLog }

#### Example:

```
Router(config-telephony)# hunt-group logout HLog
```

(Optional)
                                             				Specifies whether agent not-ready status applies only to ephone hunt group
                                             				extensions on a phone (HLog mode) or to all extensions on a phone (DND mode).
                                             				Agent not-ready status can activated by an agent using the HLog softkey or a
                                             				FAC, or it can be activated automatically after the number of calls specified
                                             				in the auto
                                                				  logout command are not answered.

The default
                                             				of this command is not used is DND .

DND —When phones are
                                                   					 placed in agent not-ready status, all ephone-dns on the phone will not accept
                                                   					 calls.

HLog —Enables the
                                                   					 display of the HLog soft key. When phones are placed in the agent not-ready
                                                   					 status, only the ephone-dns assigned to ephone hunt groups will not accept
                                                   					 calls.

Step 23

exit

#### Example:

```
Router(config-telephony)# exit
```

Exits
                                             				telephony-service configuration mode.

Step 24

ephone-dn dn-tag

#### Example:

```
Router(config)# ephone-dn 29
```

(Optional)
                                             				Enters ephone-dn configuration mode.

dn-tag —Tag number for
                                                   					 the ephone-dn to be authorized to join and leave ephone hunt groups.

Step 25

ephone-hunt
                                                				  login

#### Example:

```
Router(config-ephone-dn)# ephone-hunt login
```

(Optional)
                                             				Enables this ephone-dn to join and leave ephone hunt groups (dynamic
                                             				membership).

Step 26

end

#### Example:

```
Router(config-ephone-dn)# end
```

Returns to
                                             				privileged EXEC mode.

### Verify Ephone Hunt
                           	 Groups Configuration

Step 1

Use the show
                                                				  running-config command to verify your configuration. Ephone hunt
                                          			 group parameters are listed in the ephone-hunt portion of the output.

#### Example:

```
Router# show running-config
```

```
ephone-hunt 1 longest-idle

pilot 500

list 502, 503, *

max-timeout 30

timeout 10, 10, 10

hops 2

from-ring

fwd-final orig-phone

!

!

ephone-hunt 2 sequential

pilot 600

list 621, *, 623

final 5255348

max-timeout 10

timeout 20, 20, 20

fwd-final orig-phone

!

!

ephone-hunt 77 longest-idle

from-ring

pilot 100

list 101, *, 102

!
```

Step 2

To verify the
                                          			 configuration of ephone hunt group dynamic membership, use the show
                                                				  running-config command. Look at the ephone-hunt portion of the
                                          			 output to ensure at least one wildcard slot is configured. Look at the
                                          			 ephone-dn section to see whether particular ephone-dns are authorized to join
                                          			 ephone hunt groups. Look at the telephony-service section to see whether FACs
                                          			 are enabled.

#### Example:

```
Router# show running-config
```

```
ephone-hunt 1 longest-idle

pilot 500

list 502, 503, *

max-timeout 30

timeout 10, 10, 10

hops 2

from-ring

fwd-final orig-phone

!

!

ephone-dn 2 dual-line

number 126

preference 1

call-forward busy 500

ephone-hunt login

!

telephony-service

fac custom alias 5 *5 to *35000

fac custom ephone-hunt cancel #5
```

Step 3

Use the show ephone-hunt command for detailed information about hunt groups,
                                          			 including dial-peer tag numbers, hunt-group agent status, and on-hook time
                                          			 stamps. This command also displays the dial-peer tag numbers of all ephone-dns
                                          			 that have joined dynamically and are members of the group at the time that the
                                          			 command is run.

#### Example:

```
Router# show ephone-hunt
```

```
Group 1
type: peer
pilot number: 450, peer-tag 20123
list of numbers:
451, aux-number A450A0900, # peers 5, logout 0, down 1
peer-tag dn-tag rna login/logout up/down
[20122 42 0 login up ]
[20121 41 0 login up ]
[20120 40 0 login up ]
[20119 30 0 login up ]
[20118 29 0 login down]
452, aux-number A450A0901, # peers 4, logout 0, down 0
peer-tag dn-tag rna login/logout up/down
[20127 45 0 login up ]
[20126 44 0 login up ]
[20125 43 0 login up ]
[20124 31 0 login up ]
453, aux-number A450A0902, # peers 4, logout 0, down 0
peer-tag dn-tag rna login/logout up/down
[20131 48 0 login up ]
[20130 47 0 login up ]
[20129 46 0 login up ]
[20128 32 0 login up ]
477, aux-number A450A0903, # peers 1, logout 0, down 0
peer-tag dn-tag rna login/logout up/down
[20132 499 0 login up ]
preference: 0
preference (sec): 7
timeout: 3, 3, 3, 3
max timeout : 10
hops: 4
next-to-pick: 1
E.164 register: yes
auto logout: no
stat collect: no
Group 2
type: sequential
pilot number: 601, peer-tag 20098
list of numbers:
123, aux-number A601A0200, # peers 1, logout 0, down 0
peer-tag dn-tag rna login/logout up/down
[20097 56 0 login up ]
622, aux-number A601A0201, # peers 3, logout 0, down 0
peer-tag dn-tag rna login/logout up/down
[20101 112 0 login up ]
[20100 111 0 login up ]
[20099 110 0 login up ]
623, aux-number A601A0202, # peers 3, logout 0, down 0
peer-tag dn-tag rna login/logout up/down
[20104 122 0 login up ]
[20103 121 0 login up ]
[20102 120 0 login up ]
*, aux-number A601A0203, # peers 1, logout 0, down 1
peer-tag dn-tag rna login/logout up/down
[20105 0 0 - down]
*, aux-number A601A0204, # peers 1, logout 0, down 1
peer-tag dn-tag rna login/logout up/down
[20106 0 0 - down]
final number: 5255348
preference: 0
preference (sec): 9
timeout: 5, 5, 5, 5, 5
max timeout : 40
fwd-final: orig-phone
E.164 register: yes
auto logout: no
stat collect: no
Group 3
type: longest-idle
pilot number: 100, peer-tag 20142
list of numbers:
101, aux-number A100A9700, # peers 3, logout 0, down 3
on-hook time stamp 7616, off-hook agents=0
peer-tag dn-tag rna login/logout up/down
[20141 132 0 login down]
[20140 131 0 login down]
[20139 130 0 login down]
*, aux-number A100A9701, # peers 1, logout 0, down 1
on-hook time stamp 7616, off-hook agents=0
peer-tag dn-tag rna login/logout up/down
[20143 0 0 - down]
102, aux-number A100A9702, # peers 2, logout 0, down 2
on-hook time stamp 7616, off-hook agents=0
peer-tag dn-tag rna login/logout up/down
[20145 142 0 login down]
[20144 141 0 login down]
all agents down!
preference: 0
preference (sec): 7
timeout: 100, 100, 100
hops: 0
E.164 register: yes
auto logout: no
stat collect: no
```

### Configure
                           	 Voice-Hunt Groups

To redirect calls
                                 		  for a specific number (pilot number) to a defined group of directory numbers on
                                 		  Cisco Unified SCCP and SIP IP phones, perform the following steps.

Restriction

Before
                                                   				  Cisco Unified CME 4.3, forwarding or transferring to a voice hunt group is not
                                                   				  supported.

In
                                                   				  Cisco Unified CME 4.3 and later versions, Call Forwarding is supported to a
                                                   				  parallel hunt-group (blast hunt group) only.

SIP-to-H.323 calls are not supported.

If Call
                                                   				  Forward All or Call Forward Busy is configured for a hunt group member
                                                   				  (directory number), the hunt group ignores it.

Caller ID
                                                   				  update is not supported for supplementary services.

Voice hunt
                                                   				  groups are subject to the max-redirect restriction.

A pilot
                                                   				  dial peer cannot be used for a voice hunt group and an ephone hunt group at the
                                                   				  same time.

Voice hunt
                                                   				  groups do not support the expansion of pilot numbers using the dialplan-pattern command. To enable external
                                                   				  phones to dial the pilot number, you must configure a secondary pilot number
                                                   				  using a fully qualified E.164 number.

If
                                                   				  call-waiting is enabled (the default), parallel hunt groups support multiple
                                                   				  calls up to the limit of call-waiting calls supported by the particular SIP
                                                   				  phone model. If call waiting is disabled, parallel hunt groups support only one
                                                   				  call at a time in the ringing state. Phones that fail to connect must return to
                                                   				  the on-hook state before they can receive other calls.

A phone
                                                   				  number associated with an FXO port is not supported in parallel hunt groups.

If the
                                                   				  directory number (member of a voice hunt group) is a shared line, agent status
                                                   				  control or HLog is not supported.

From
                                                   				  Unified CME release 11.6 onwards, line level logout or login is not supported
                                                   				  for SIP phones.

DND FAC is
                                                   				  not supported with SIP phones on Unified CME.

Consider
                                                   				  an SCCP DN that is part of both voice hunt group and ephone hunt group. If
                                                   				  voice hunt group is configured with members logout or auto logout, then the
                                                   				  SCCP DN will logout only from voice hunt group. If ephone hunt group is
                                                   				  configured with members logout or auto logout, then the SCCP DN will logout
                                                   				  from both voice hunt group and ephone hunt group.

For Unified CME 12.1 and prior releases, mixed shared lines and
                                                   				  SIP shared lines are not supported with voice hunt groups.

For
                                                   				  parallel voice hunt group, the maximum number of call blasts that can be
                                                   				  supported is limited to 32. This includes the shared-line as well as normal
                                                   				  directory numbers.

Unified CME supports chaining (nesting) of a voice hunt group with another voice hunt group. The chaining of voice hunt groups
                                                   is established by configuring the final number of the first voice hunt group as the pilot number of the second voice hunt
                                                   group.

Unified CME supports the chaining (nesting) of a maximum of two voice hunt groups. The configuration ensures that there is
                                                   no looping of calls placed to a voice hunt group.

#### Before you begin

Cisco Unified CME 3.4 or a later version for SIP phones.

Cisco Unified CME 4.3 or a later version is required to include
                                       				a SCCP phone, FXS analog phone, DS0-group, PRI-group, or SIP trunk in a voice
                                       				hunt-group.

Cisco Unified CME 4.3 or a later version is required for call
                                       				transfer to a voice hunt-group.

Directory
                                       				numbers included in a hunt group must be configured in Cisco Unified CME. For
                                       				configuration information, see Configure Phones to Make Basic Call .

Cisco
                                       				Unified CME 11.6 or later is required to support HLog softkey, feature button,
                                       				and agent status control.

Cisco
                                       				Unified CME 11.6 or later is required to configure present-call , auto logout , and members
                                             					 logout under voice hunt group configuration mode.

Unified CME
                                       				12.2 or later is required to configure mixed shared lines and SIP shared lines
                                       				with voice hunt groups.

### SUMMARY STEPS

- enable

- configure terminal

- voice hunt-group hunt-tag [ longest-idle | parallel | peer | sequential ]

- pilot number [ secondary number ]

- list number

- final number

- preference preference-order [ secondary secondary-order ]

- hops number

- timeout seconds

- present-call idle-phone

- members logout

- auto logout number-of-calls

- exit

- telephony-service

- hunt-group logout { DND HLog }

- exit

- voice register dn tag

- voice-hunt-groups login

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

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice hunt-group hunt-tag [ longest-idle | parallel | peer | sequential ]

#### Example:

```
Router(config)# voice hunt-group 1 longest-idle
```

Enters voice
                                             				hunt-group configuration mode to define a hunt group.

hunt-tag —Unique sequence number of the hunt group
                                                   					 to be configured. Range is 1 to 100.

longest idle —Hunt group in which calls go to the
                                                   					 directory number that has been idle for the longest time.

sequential —Hunt group in which directory numbers
                                                   					 ring in the order in which they are listed, left to right.

parallel —Hunt group in which all directory numbers
                                                   					 ring simultaneously.

peer —Hunt
                                                   					 group in which the call placed to a directory number rings for the next
                                                   					 directory number in line.

To change
                                                   					 the hunt-group type, remove the existing hunt group first by using the no form of
                                                   					 the command; then, recreate the group.

Step 4

pilot number [ secondary number ]

#### Example:

```
Router(config-voice-hunt-group)# pilot number 8100
```

Defines the
                                             				telephone number that callers dial to reach a voice hunt group.

number —String of up to 16 characters that
                                                   					 represents an E.164 telephone number.

Number
                                                   					 string may contain alphabetic characters when the number is to be dialed only
                                                   					 by the Cisco Unified CME router, as with an intercom number, and not from
                                                   					 telephone keypads.

secondary number —(Optional) Keyword and argument combination
                                                   					 defines the number that follows as an additional pilot number for the voice
                                                   					 hunt group.

Secondary numbers can contain wild cards. A wildcard is a period (.), which matches any entered digit.

Step 5

list number

#### Example:

```
Router(config-voice-hunt-group)# list 8000, 8010, 8020, 8030
```

Creates a
                                             				list of extensions that are members of a voice hunt group. To remove a list
                                             				from a router configuration, use the no form of
                                             				this command.

number —List
                                                   					 of extensions to be added as members to the voice hunt group. Separate the
                                                   					 extensions with commas.

Add or
                                                   					 delete all extensions in a hunt-group list at one time. You cannot add or
                                                   					 delete a single number in an existing list.

There
                                                   					 must be from 2 to 10 extensions in the hunt-group list, and each number must be
                                                   					 a primary or secondary number.

Any
                                                   					 number in the list cannot be a pilot number of a parallel hunt group.

Step 6

final number

#### Example:

```
Router(config-voice-hunt-group)# final 8888
```

Defines the
                                             				last extension in a voice hunt group.

If a
                                                   					 final number in one hunt group is configured as a pilot number of another hunt
                                                   					 group, the pilot number of the first hunt group cannot be configured as a final
                                                   					 number in any other hunt group.

This
                                                   					 command is not used for voice hunt groups that are part of a Cisco Unified CME
                                                   					 B-ACD service. The final destination for those groups is determined by the
                                                   					 B-ACD service.

Step 7

preference preference-order [ secondary secondary-order ]

#### Example:

```
Router(config-voice-hunt-group)# preference 6
```

Sets the
                                             				preference order for the directory number associated with a voice hunt-group
                                             				pilot number.

preference-order —Range is 0 to 8, where 0 is the
                                                   					 highest preference and 8 is the lowest preference. Default is 0.

secondary secondary-order— (Optional) Keyword and argument combination is
                                                   					 used to set the preference order for the secondary pilot number. Range is 1 to
                                                   					 8, where 0 is the highest preference and 8 is the lowest preference. Default is
                                                   					 7.

Step 8

hops number

#### Example:

```
Router(config-voice-hunt-group)# hops 2
```

For
                                             				configuring a peer or longest-idle voice hunt group only. Defines the number of
                                             				times that a call can hop to the next number in a peer or longest-idle voice
                                             				hunt group before the call proceeds to the final number.

number —Number of hops. Range is 2 to 10, and the
                                                   					 value must be less than or equal to the number of extensions specified by
                                                   					 the list command.

Default
                                                   					 is the same number as there are destinations defined under the list command.

Step 9

timeout seconds

#### Example:

```
Router(config-voice-hunt-group)# timeout 100
```

Defines the
                                             				number of seconds after which a call that is not answered is redirected to the
                                             				next directory number in a voice hunt-group list.

Default: 180 seconds.

Step 10

present-call idle-phone

#### Example:

```
Router(config-voice-hunt-group)# present-call idle-phone
```

Specifies
                                             				that voice hunt-group calls are presented only if all lines are idle on the
                                             				phone on which the hunt-group line appears.

Step 11

members logout

#### Example:

```
Router(config-voice-hunt-group)# members logout
```

Configures a
                                             				Cisco Unified CME system for all non-shared static members or agents in a voice
                                             				hunt group with the Hlogout initial state.

Step 12

auto logout number-of-calls

#### Example:

```
Router(config-voice-hunt-group)# auto logout 2
```

Enables the
                                             				automatic change of a voice hunt group agent’s voice register dn or ephone-dn
                                             				to not-ready status after a specified number of successive hunt-group calls are
                                             				not answered.

Step 13

exit

#### Example:

```
Router(config-voice-hunt-group)# exit
```

Exits
                                             				voice-hunt-group configuration mode.

Step 14

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony-service configuration mode.

Step 15

hunt-group logout { DND HLog }

#### Example:

```
Router(config-telephony)# hunt-group logout Hlog
```

(Optional)
                                             				Specifies HLog softkey functions. Agent not-ready status can be activated by an
                                             				agent using the HLog softkey or a FAC.

Step 16

exit

#### Example:

```
Router(config-telephony)# exit
```

Exits
                                             				telephony-service configuration mode.

Step 17

voice register dn tag

#### Example:

```
Router(config)# voice register dn 29
```

(Optional)
                                             				Enters voice register dn configuration mode.

tag —Tag
                                                   					 number for voice register dn to be authorized to join and leave voice hunt
                                                   					 groups.

Step 18

voice-hunt-groups login

#### Example:

```
Router(config-register-dn)# voice-hunt-groups login
```

(Optional)
                                             				Enables this voice register dn to join and leave voice hunt groups (dynamic
                                             				membership).

Step 19

end

#### Example:

```
Router(config-register-dn)# end
```

### Verify Voice Hunt
                           	 Groups Configuration

Step 1

Use the show
                                                				  running-config command to verify your configuration. Voice hunt
                                          			 group parameters are listed in the voice-hunt portion of the output.

#### Example:

```
Router# show running-config voice-hunt 1 longest-idle
pilot 500
list 502, 503, *
max-timeout 30
timeout 10, 10, 10
hops 2
from-ring
fwd-final orig-phone
!
!
voice-hunt 2 sequential
pilot 600
list 621, *, 623
final 5255348
max-timeout 10
timeout 20, 20, 20
fwd-final orig-phone
!
!
voice-hunt 77 longest-idle
from-ring
pilot 100
list 101, *, 102
!
```

Step 2

To verify the
                                          			 configuration of voice hunt group dynamic membership, use the show
                                                				  running-config command. Look at the voice-hunt portion of the
                                          			 output to ensure at least one wildcard slot is configured. Look at the voice-dn
                                          			 section to see whether particular ephone-dns are authorized to join voice hunt
                                          			 groups. Look at the telephony-service section to see whether FACs are enabled.

#### Example:

```
Router# show running-config voice-hunt 1 longest-idle
pilot 500
list 502, 503, *
max-timeout 30
timeout 10, 10, 10
hops 2
from-ring
fwd-final orig-phone
!
!
voice-dn 2 dual-line
number 126
preference 1
call-forward busy 500
ephone-hunt login
!
telephony-service
fac custom alias 5 *5 to *35000
fac custom ephone-hunt cancel #5
```

Step 3

Use the show ephone-hunt command for detailed information about hunt groups,
                                          			 including dial-peer tag numbers, hunt-group agent status, and on-hook time
                                          			 stamps. This command also displays the dial-peer tag numbers of all ephone-dns
                                          			 that have joined dynamically and are members of the group at the time that the
                                          			 command is run.

#### Example:

```
Router# show ephone-hunt
```

```
Group 1
type: peer
pilot number: 450, peer-tag 20123
list of numbers:
451, aux-number A450A0900, # peers 5, logout 0, down 1
peer-tag dn-tag rna login/logout up/down
[20122 42 0 login up ]
[20121 41 0 login up ]
[20120 40 0 login up ]
[20119 30 0 login up ]
[20118 29 0 login down]
452, aux-number A450A0901, # peers 4, logout 0, down 0
peer-tag dn-tag rna login/logout up/down
[20127 45 0 login up ]
[20126 44 0 login up ]
[20125 43 0 login up ]
[20124 31 0 login up ]
453, aux-number A450A0902, # peers 4, logout 0, down 0
peer-tag dn-tag rna login/logout up/down
[20131 48 0 login up ]
[20130 47 0 login up ]
[20129 46 0 login up ]
[20128 32 0 login up ]
477, aux-number A450A0903, # peers 1, logout 0, down 0
peer-tag dn-tag rna login/logout up/down
[20132 499 0 login up ]
preference: 0
preference (sec): 7
timeout: 3, 3, 3, 3
max timeout : 10
hops: 4
next-to-pick: 1
E.164 register: yes
auto logout: no
stat collect: no
Group 2
type: sequential
pilot number: 601, peer-tag 20098
list of numbers:
123, aux-number A601A0200, # peers 1, logout 0, down 0
peer-tag dn-tag rna login/logout up/down
[20097 56 0 login up ]
622, aux-number A601A0201, # peers 3, logout 0, down 0
peer-tag dn-tag rna login/logout up/down
[20101 112 0 login up ]
[20100 111 0 login up ]
[20099 110 0 login up ]
623, aux-number A601A0202, # peers 3, logout 0, down 0
peer-tag dn-tag rna login/logout up/down
[20104 122 0 login up ]
[20103 121 0 login up ]
[20102 120 0 login up ]
*, aux-number A601A0203, # peers 1, logout 0, down 1
peer-tag dn-tag rna login/logout up/down
[20105 0 0 - down]
*, aux-number A601A0204, # peers 1, logout 0, down 1
peer-tag dn-tag rna login/logout up/down
[20106 0 0 - down]
final number: 5255348
preference: 0
preference (sec): 9
timeout: 5, 5, 5, 5, 5
max timeout : 40
fwd-final: orig-phone
E.164 register: yes
auto logout: no
stat collect: no
Group 3
type: longest-idle
pilot number: 100, peer-tag 20142
list of numbers:
101, aux-number A100A9700, # peers 3, logout 0, down 3
on-hook time stamp 7616, off-hook agents=0
peer-tag dn-tag rna login/logout up/down
[20141 132 0 login down]
[20140 131 0 login down]
[20139 130 0 login down]
*, aux-number A100A9701, # peers 1, logout 0, down 1
on-hook time stamp 7616, off-hook agents=0
peer-tag dn-tag rna login/logout up/down
[20143 0 0 - down]
102, aux-number A100A9702, # peers 2, logout 0, down 2
on-hook time stamp 7616, off-hook agents=0
peer-tag dn-tag rna login/logout up/down
[20145 142 0 login down]
[20144 141 0 login down]
all agents down!
preference: 0
preference (sec): 7
timeout: 100, 100, 100
hops: 0
E.164 register: yes
auto logout: no
stat collect: no
```

### Enable Audible
                           	 Tone for Successful Login and Logout of a Hunt Group on SCCP Phone

The user can
                                 		  enable playing of audible tone on an SCCP phone to confirm a successful join or
                                 		  unjoin and login or logout from a hunt group (applies to both ephone and voice
                                 		  hunt group). From Cisco Unified CME 10.5 onwards, distinct audible tone will be
                                 		  played for the following scenarios:

- To join and unjoin a hunt
                                    			 group via FAC

- To log in and log out from
                                    			 hunt group via Hlog/DND, or FAC

The audible tone
                                 		  will be played for ephone hunt group and voice hunt group for SCCP Phones.

Restriction

Supports all 79xx phones except for 7926 wireless phones.

#### Before you begin

- Cisco Unified CME 10.5 or a
                                    			 later version

- Ephone or voice hunt group
                                    			 should be configured

- Ephone should be static or
                                    			 dynamic member of hunt group.

### SUMMARY STEPS

- enable

- configure terminal

- ephone phone-tag or ephone-template template-tag

- audible tone

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

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ephone phone-tag or ephone-template template-tag

#### Example:

```
Router(config)# ephone 25
```

Enters ephone configuration mode.

phone-tag —The unique sequence number of the phone that will be notified when an incoming call is received by a night-service ephone-dn
                                                   during a night-service period.

or

Enters ephone-template configuration mode to create an ephone template.

template-tag —Unique identifier for the ephone template that is being created. Range: 1 to 20.

Step 4

audible tone

#### Example:

```
Router(config-ephone)# audible tone
```

Enables playing of audible tone on an SCCP phone to confirm a successful login or logout.

Step 5

end

#### Example:

```
Router(config-ephone)# end
```

#### Example

The following
                                 		  example shows that audible tone is configured in voice register pool
                                 		  configuration mode:

```
!
Router(config)# ephone 1 Router(config-ephone)# device-security-mode none Router(config-ephone)# mac-address 64D8.14A5.C87A Router(config-ephone)# type 7965 Router(config-ephone)# button 1:3 Router(config-ephone)# audible-tone !
```

### Enable the Collection of Call Statistics for Voice Hunt-Groups

To enable the collection of call statistics for voice hunt groups,
                                 		  perform the following steps.

Restriction

Hold and resume statistics are not updated for remote SCCP voice
                                             			 hunt group agents.

#### Before you begin

Cisco Unified CME 9.0 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice hunt-group hunt-tag { longest-idle | parallel | peer | sequential }

- statistics collect

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

voice hunt-group hunt-tag { longest-idle | parallel | peer | sequential }

#### Example:

```
Router(config)# voice hunt-group 60 longest-idle
```

Enters voice hunt-group configuration mode.

- hunt-tag —Unique sequence number that
                                                				  identifies the hunt group. Range: 1 to 100.

- longest-idle —Hunt group in which
                                                				  calls go to the directory number that has been idle the longest.

- parallel —Hunt group in which calls
                                                				  simultaneously ring multiple phones.

- peer —Hunt group in which the first
                                                				  extension to ring is selected round-robin from the list. Ringing proceeds in a
                                                				  circular manner, left to right, for the number of hops specified when the hunt
                                                				  group is defined. The round-robin selection starts with the number left of the
                                                				  number that answered when the hunt-group was last called.

- sequential —Hunt group in which
                                                				  extensions ring in the order in which they are listed, left to right, when the
                                                				  hunt group was defined.

Step 4

statistics collect

#### Example:

```
Router(config-voice-hunt-group)# statistics collect
```

Enables the collection of call statistics for a voice hunt group.

Step 5

end

#### Example:

```
Router(config-voice-hunt-group)# end
```

Exits to privileged EXEC mode.

### Associate a Name
                           	 with a Called Voice Hunt-Group

Restriction

Cisco Unified
                                             			 SIP IP phones are not supported. The display support applies to Cisco Unified
                                             			 SCCP IP phones on voice hunt-group and ephone-hunt configuration modes only.

#### Before you begin

Cisco Unified CME
                                 		  9.5 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice hunt-group hunt-tag { parallel }

- final number

- list number [ , number ... ]

- timeout seconds

- pilot number [ secondary number ]

- name “primary pilot
                                       				  name” [ secondary “secondary pilot
                                       				  name” ]

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

voice hunt-group hunt-tag { parallel }

#### Example:

```
Router(config)# voice hunt-group 20 parallel
```

Creates a hunt
                                             				group for phones in a Cisco Unified CME system.

hunt-tag —Unique sequence number that identifies
                                                   					 the hunt group. Range is 1 to 100.

parallel —Hunt group in which calls simultaneously
                                                   					 ring multiple phones.

Step 4

final number

#### Example:

```
Router(config-voice-hunt-group)# final 4000
```

Defines the
                                             				last extension in a voice hunt group.

- number —Telephone or extension number. Can be an
                                                				  E.164 number, voice-mail number, pilot number of another hunt group, or FXS
                                                				  caller-ID number.

Step 5

list number [ , number ... ]

#### Example:

```
Router(config-voice-hunt-group)# list 3001, 3002, 3003
```

Defines a list
                                             				of extensions that are members of a voice hunt group.

number —Extension or E.164 number assigned to a
                                                   					 phone in Cisco Unified CME. List must contain 2 to 32 numbers.

Step 6

timeout seconds

#### Example:

```
Router(config-voice-hunt-group)# timeout 20
```

Defines the
                                             				number of seconds after which a call that is not answered is redirected to the
                                             				next number in a voice hunt-group list.

seconds —Number of seconds. Range is 3 to 60000.
                                                   					 Default is 180.

Step 7

pilot number [ secondary number ]

#### Example:

```
Router(config-voice-hunt-group)# pilot 4045550110 secondary 3125550120
```

Defines the
                                             				number that callers dial to reach a Cisco Unified CME voice hunt group.

number —String of up to 32 characters that
                                                   					 represents an extension or E.164 telephone number.

secondary number —(Optional) Defines an additional pilot
                                                   					 number for the voice hunt group.

Step 8

name “primary pilot
                                                				  name” [ secondary “secondary pilot
                                                				  name” ]

#### Example:

```
Router(config-voice-hunt-group)# name Hospital secondary “Health Center”
```

Associates a
                                             				name with the called voice hunt group.

“primary pilot
                                                         						  name” —Name for the primary pilot number.

secondary “secondary pilot
                                                         						  name” —(Optional) Name for the secondary pilot number.

### Prevent Local Call Forwarding to Final Agent in Voice
                           	 Hunt-Groups

#### Before you begin

Cisco Unified CME 9.5 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice hunt-group hunt-tag { parallel | sequential }

- [ no ] forward local-calls to-final

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

voice hunt-group hunt-tag { parallel | sequential }

#### Example:

```
Router(config)# voice hunt-group 1 sequential
```

Creates a hunt group for phones in a Cisco Unified CME system.

- hunt-tag —Unique
                                                				  sequence number that identifies the hunt group. Range is 1 to 100.

- parallel —Hunt group in which calls
                                                				  simultaneously ring multiple phones.

- sequential —Hunt group in which
                                                				  extensions ring in the order in which they are listed, left to right, when the
                                                				  hunt group was defined.

Step 4

[ no ] forward local-calls to-final

#### Example:

```
Router(config-voice-hunt-group)# no forward local-calls to-final
```

Prevents local calls from being forwarded to the final destination
                                             				number.

### Configure Night
                           	 Service on SCCP Phones

This procedure
                                 		  defines night-service hours, an optional night-service code, the ephone-dns
                                 		  that trigger the notification process, and the ephones that will receive
                                 		  notification.

Restriction

Night
                                                   				  service notification is not supported on analog endpoints connected to FXS
                                                   				  ports on a Cisco Integrated Services Router (ISR) or Cisco VG224 Analog Phone
                                                   				  Gateway.

In
                                                   				  Cisco Unified CME 4.0 and later versions, silent ringing, configured on the
                                                   				  phone by using the s keyword
                                                   				  with the button command, is suppressed when used with the night service feature. Silent ringing
                                                   				  is overridden and the phone audibly rings during designated night-service
                                                   				  periods.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- night-service day day start-time stop-time

- night-service date month date start-time stop-time

- night-service everyday start-time
                                       				  stop-time

- night-service weekday start-time
                                       				  stop-time

- night-service weekend start-time
                                       				  stop-time

- night-service code digit-string

- timeouts
                                       				  night-service-bell seconds

- exit

- ephone-dn dn-tag

- night-service
                                       				  bell

- exit

- ephone phone-tag

- night-service
                                       				  bell

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

night-service day day start-time stop-time

#### Example:

```
Router(config-telephony)# night-service day mon 19:00 07:00
```

Defines a
                                             				recurring time period associated with a day of the week during which night
                                             				service is active.

day —Day of the week abbreviation. The following are valid
                                                   					 day abbreviations: sun , mon , tue , wed , thu , fri , sat .

start-time stop-time —Beginning and ending times for night
                                                   					 service, in an HH:MM format using a 24-hour clock. If the stop time is a
                                                   					 smaller value than the start time, the stop time occurs the day following the
                                                   					 start time. For example, “mon 19:00 07:00” means “from Monday at 7 p.m. until
                                                   					 Tuesday at 7 a.m.”

Step 5

night-service date month date start-time stop-time

#### Example:

```
Router(config-telephony)# night-service date jan 1 00:00 00:00
```

Defines a
                                             				recurring time period associated with a month and date during which night
                                             				service is active.

month —Month abbreviation. The following are valid month
                                                   					 abbreviations: jan , feb , mar , apr , may , jun , jul , aug , sep , oct , nov , dec .

date —Date of the month. Range is 1 to 31.

start-time stop-time —Beginning and ending times for night
                                                   					 service, in an HH:MM format using a 24-hour clock. The stop time must be
                                                   					 greater than the start time. The value 24:00 is not valid. If 00:00 is entered
                                                   					 as a stop time, it is changed to 23:59. If 00:00 is entered for both start time
                                                   					 and stop time, calls are blocked for the entire 24-hour period on the specified
                                                   					 date.

Step 6

night-service everyday start-time
                                                				  stop-time

#### Example:

```
Router(config-telephony)# night-service everyday 1200 1300
```

Defines a
                                             				recurring night-service time period to be effective everyday.

start-time stop-time —Beginning and ending times for night
                                                   					 service, in an HH:MM format using a 24-hour clock. If the stop time is a
                                                   					 smaller value than the start time, the stop time occurs the day following the
                                                   					 start time. For example, “19:00 07:00” means “from 7 p.m. to 7 a.m. the next
                                                   					 morning.” The value 24:00 is not valid. If 00:00 is entered as a stop time, it
                                                   					 is changed to 23:59. If 00:00 is entered for both start time and stop time, the
                                                   					 night service feature will be activated for the entire 24-hour period.

Step 7

night-service weekday start-time
                                                				  stop-time

#### Example:

```
Router(config-telephony)# night-service weekday 1700 0700
```

Defines a
                                             				recurring night-service time period to be effective on all weekdays.

start-time
                                                      						stop-time —Beginning and ending times for night service, in an HH:MM format
                                                   					 using a 24-hour clock. If the stop time is a smaller value than the start time,
                                                   					 the stop time occurs the day following the start time. For example, “19:00
                                                   					 07:00” means “from 7 p.m. to 7 a.m. the next morning.” The value 24:00 is not
                                                   					 valid. If 00:00 is entered as a stop time, it is changed to 23:59. If 00:00 is
                                                   					 entered for both start time and stop time, the night service feature will be
                                                   					 activated for the entire 24-hour period.

Step 8

night-service weekend start-time
                                                				  stop-time

#### Example:

```
Router(config-telephony)# night-service weekend 00:00 00:00
```

Defines a
                                             				recurring night-service time period to be effective on all weekend days
                                             				(Saturday and Sunday).

start-time
                                                         						  stop-time —Beginning and ending times for night service, in an
                                                   					 HH:MM format using a 24-hour clock. If the stop time is a smaller value than
                                                   					 the start time, the stop time occurs the day following the start time. For
                                                   					 example, “19:00 07:00” means “from 7 p.m. to 7 a.m. the next morning.” The
                                                   					 value 24:00 is not valid. If 00:00 is entered as a stop time, it is changed to
                                                   					 23:59. If 00:00 is entered for both start time and stop time, the night service
                                                   					 feature will be activated for the entire 24-hour period.

Step 9

night-service code digit-string

#### Example:

```
Router(config-telephony)# night-service code *6483
```

Designates
                                             				a code that can be dialed from any night-service line (ephone-dn) to toggle
                                             				night service on and off for all lines assigned to night service in the system.

digit-string —String of up to 16 keypad digits. The
                                                   					 code must begin with an asterisk (*).

Step 10

timeouts
                                                				  night-service-bell seconds

#### Example:

```
Router(config-telephony)# timeouts night-service-bell 15
```

Defines the
                                             				frequency of the night-service notification.

seconds —Range: 4 to 30. Default: 12.

Step 11

exit

#### Example:

```
Router(config-telephony)# exit
```

Exits
                                             				telephony-service configuration mode.

Step 12

ephone-dn dn-tag

#### Example:

```
Router(config)# ephone-dn 55
```

Enters
                                             				ephone-dn configuration mode to define an ephone-dn to receive night-service
                                             				treatment.

Step 13

night-service
                                                				  bell

#### Example:

```
Router(config-ephone-dn)# night-service bell
```

Marks this
                                             				ephone-dn for night-service treatment.

Step 14

exit

#### Example:

```
Router(config-ephone-dn)# exit
```

Exits
                                             				ephone-dn configuration mode.

Step 15

ephone phone-tag

#### Example:

```
Router(config)# ephone 12
```

Enters
                                             				ephone configuration mode.

phone-tag —The unique
                                                   					 sequence number of the phone that will be notified when an incoming call is
                                                   					 received by a night-service ephone-dn during a night-service period.

Step 16

night-service
                                                				  bell

#### Example:

```
Router(config-ephone)# night-service bell
```

Marks this
                                             				phone to receive night-service bell notification when incoming calls are
                                             				received on ephone-dns marked for night service during the night-service time
                                             				period.

Night
                                                   					 service notification is not supported on analog endpoints connected to SCCP FXS
                                                   					 ports on a Cisco ISR or Cisco VG224.

Step 17

end

#### Example:

```
Router(config-ephone)# end
```

Returns to
                                             				privileged EXEC mode.

### Configure Night
                           	 Service on SIP Phones

This procedure
                                 		  defines night-service hours, an optional night-service code, the voice register
                                 		  DNs that trigger the notification process, and the SIP phones (voice register
                                 		  pools) that receive notification. The CLI commands related to night-service in
                                 		  telephony-service are used to make night service feature work on SIP phones.

Restriction

When service directed-pickup
                                                         						gpickup is configured under telephony service, gpickup softkey
                                                   				  has to be used on SCCP phones to pick up the ringing call on night-service
                                                   				  extensions.

#### Before you begin

It is
                                       				mandatory to configure the CLI command service directed-pickup
                                             					 gpickup under telephony-service to pick up calls from SIP phones
                                       				for night service.

It is mandatory to configure the CLI command call-park system application under
                                       				telephony-service to enable or disable Night Service functionality using night
                                       				service code on SIP phones.

It is
                                       				mandatory to configure source IP address, port, and max dn under
                                       				telephony-service configuration to make night service feature work for SIP
                                       				phones.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- night-service
                                       				  day day start-time stop-time

- night-service date month date start-time stop-time

- night-service everyday start-time
                                       				  stop-time

- night-service weekday start-time
                                       				  stop-time

- night-service weekend start-time
                                       				  stop-time

- fac standard

- night-service code digit-string

- call-park system application

- service directed-pickup gpickup

- timeouts
                                       				  night-service-bell seconds

- exit

- voice register
                                       				  dn dn-tag

- night-service
                                       				  bell

- exit

- voice register
                                       				  pool pool -tag | voice register
                                       				  template template-tag

- night-service
                                       				  bell

- voice register
                                       				  pool pool-tag

- template template-tag

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

Enters
                                             				global configuration mode.

Step 3

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony-service configuration mode.

Step 4

night-service
                                                				  day day start-time stop-time

#### Example:

```
Router(config-telephony)# night-service day mon 19:00 07:00
```

Defines a
                                             				recurring time period associated with a day of the week during which night
                                             				service is active.

day —Day of the week
                                                   					 abbreviation. The following are valid day abbreviations: sun , mon , tue , wed , thu , fri , sat .

start-time
                                                      						stop-time —Beginning and ending times for night service, in an HH:MM format
                                                   					 using a 24-hour clock. If the stop time is a smaller value than the start time,
                                                   					 the stop time occurs the day following the start time. For example, “mon 19:00
                                                   					 07:00” means “from Monday at 7 p.m. until Tuesday at 7 a.m.”

Step 5

night-service date month date start-time stop-time

#### Example:

```
Router(config-telephony)# night-service date jan 1 00:00 00:00
```

Defines a
                                             				recurring time period associated with a month and date during which night
                                             				service is active.

month —Month
                                                   					 abbreviation. The following are valid month abbreviations: jan , feb , mar , apr , may , jun , jul , aug , sep , oct , nov , dec .

date —Date of the
                                                   					 month. Range is 1 to 31.

start-time
                                                      						stop-time —Beginning and ending times for night service, in an HH:MM format
                                                   					 using a 24-hour clock. The stop time must be greater than the start time. The
                                                   					 value 24:00 is not valid. If 00:00 is entered as a stop time, it is changed to
                                                   					 23:59. If 00:00 is entered for both start time and stop time, calls are blocked
                                                   					 for the entire 24-hour period on the specified date.

Step 6

night-service everyday start-time
                                                				  stop-time

#### Example:

```
Router(config-telephony)# night-service everyday 1200 1300
```

Defines a
                                             				recurring night-service time period to be effective everyday.

start-time
                                                      						stop-time —Beginning and ending times for night service, in an HH:MM format
                                                   					 using a 24-hour clock. If the stop time is a smaller value than the start time,
                                                   					 the stop time occurs the day following the start time. For example, “19:00
                                                   					 07:00” means “from 7 p.m. to 7 a.m. the next morning.” The value 24:00 is not
                                                   					 valid. If 00:00 is entered as a stop time, it is changed to 23:59. If 00:00 is
                                                   					 entered for both start time and stop time, the night service feature will be
                                                   					 activated for the entire 24-hour period.

Step 7

night-service weekday start-time
                                                				  stop-time

#### Example:

```
Router(config-telephony)# night-service weekday 1700 0700
```

Defines a
                                             				recurring night-service time period to be effective on all weekdays.

start-time
                                                      						stop-time —Beginning and ending times for night service, in an HH:MM format
                                                   					 using a 24-hour clock. If the stop time is a smaller value than the start time,
                                                   					 the stop time occurs the day following the start time. For example, “19:00
                                                   					 07:00” means “from 7 p.m. to 7 a.m. the next morning.” The value 24:00 is not
                                                   					 valid. If 00:00 is entered as a stop time, it is changed to 23:59. If 00:00 is
                                                   					 entered for both start time and stop time, the night service feature will be
                                                   					 activated for the entire 24-hour period.

Step 8

night-service weekend start-time
                                                				  stop-time

#### Example:

```
Router(config-telephony)# night-service weekend 00:00 00:00
```

Defines a
                                             				recurring night-service time period to be effective on all weekend days
                                             				(Saturday and Sunday).

start-time
                                                         						  stop-time —Beginning and ending times for night service, in an
                                                   					 HH:MM format using a 24-hour clock. If the stop time is a smaller value than
                                                   					 the start time, the stop time occurs the day following the start time. For
                                                   					 example, “19:00 07:00” means “from 7 p.m. to 7 a.m. the next morning.” The
                                                   					 value 24:00 is not valid. If 00:00 is entered as a stop time, it is changed to
                                                   					 23:59. If 00:00 is entered for both start time and stop time, the night service
                                                   					 feature will be activated for the entire 24-hour period.

Step 9

fac standard

#### Example:

```
Router(config-telephony)# fac standard
```

(Optional)
                                             				Enables predefined standard feature access codes (FACs) to be enabled. For the
                                             				CLI command night-service code to work, it is mandatory to configure fac standard under telephony-service configuration mode.

Step 10

night-service code digit-string

#### Example:

```
Router(config-telephony)# night-service code *6483
```

Designates
                                             				a code that can be dialed from any night-service line (voice register dn) to
                                             				toggle night service on and off for all lines assigned to night service in the
                                             				system.

digit-string —String of up to 16 keypad digits. The
                                                   					 code must begin with an asterisk (*).

Step 11

call-park system application

#### Example:

```
Router(config-telephony)# call-park system application
```

Enables or disables Night Service functionality using night
                                             				service code on SIP phones.

Step 12

service directed-pickup gpickup

#### Example:

```
Router(config-telephony)# service directed-pickup gpickup
```

Enables Directed Call Pickup and modifies the function of the
                                             				GPickUp and PickUp soft keys.

Step 13

timeouts
                                                				  night-service-bell seconds

#### Example:

```
Router(config-telephony)# timeouts night-service-bell 15
```

Defines the
                                             				frequency of the night-service notification.

seconds —Range: 4 to 30. Default: 12.

Step 14

exit

#### Example:

```
Router(config-telephony)# exit
```

Exits
                                             				telephony-service configuration mode.

Step 15

voice register
                                                				  dn dn-tag

#### Example:

```
Router(config)# voice register dn 10
```

Enters voice
                                             				register dn configuration mode to define a voice register dn to receive
                                             				night-service treatment.

Step 16

night-service
                                                				  bell

#### Example:

```
Router(config-register-dn)# night-service bell
```

Marks this
                                             				voice register dn for night-service treatment.

Step 17

exit

#### Example:

```
Router(config-register-dn)# exit
```

Exits voice
                                             				register dn configuration mode.

Step 18

voice register
                                                				  pool pool -tag | voice register
                                                				  template template-tag

#### Example:

```
Router(config)# voice register pool 10
```

```
Router(config)# voice register template 1
```

Enters pool
                                             				configuration mode (or template configuration mode).

pool-tag —The unique
                                                   					 sequence number of the phone that will be notified when an incoming call is
                                                   					 received by a night-service voice-dn during a night-service period.

Step 19

night-service
                                                				  bell

#### Example:

```
Router(config-register-pool)# night-service bell
```

```
Router(config-register-template)# night-service bell
```

Marks this
                                             				phone to receive night-service bell notification when incoming calls are
                                             				received on voice register dns marked for night service during the
                                             				night-service time period.

Step 20

voice register
                                                				  pool pool-tag

#### Example:

```
Router(config)# voice register pool 10
```

Enters pool
                                             				configuration mode. This step is valid only when the night service
                                             				configuration is under voice register template.

Step 21

template template-tag

#### Example:

```
Router(config-register-pool)# template 1
```

Includes the
                                             				template with night-service bell configured to provide night service treatment
                                             				for this pool. This step is valid only when the night service configuration is
                                             				under voice register template.

Step 22

end

#### Example:

```
Router(config-register-temp)# end
```

Returns to
                                             				privileged EXEC mode.

### Verify Night
                           	 Service Configuration on SCCP Phones

Step 1

Use the show
                                                				  running-config command to verify the night-service parameters,
                                          			 which are listed in the telephony-service portion of the output, or use the show
                                                				  telephony-service command to display the same parameters.

#### Example:

```
Router# show running-config
```

```
telephony-service
```

```
fxo hook-flash
```

```
load 7910 P00403020214
```

```
load 7960-7940 P00303020214
```

```
max-ephones 48
```

```
max-dn 288
```

```
ip source-address 10.50.50.1 port 2000
```

```
application segway0
```

```
caller-id block code *321
```

```
create cnf-files version-stamp 7960 Mar 07 2003 11:19:18
```

```
voicemail 79000
```

```
max-conferences 8
```

```
call-forward pattern .....
```

```
moh minuet.wav
```

```
date-format yy-mm-dd
```

```
transfer-system full-consult
```

```
transfer-pattern .....
```

```
secondary-dialtone 9
```

```
night-service code *1234
```

```
night-service day Tue 00:00 23:00
```

```
night-service day Wed 01:00 23:59
```

```
!
```

```
!
```

```
Router# show telephony-service
```

```
CONFIG (Version=4.0(0))
```

```
=====================
```

```
Version 4.0(0)
```

```
Cisco Unified CallManager Express
```

```
For on-line documentation please see:
```

```
www.cisco.com/en/US/products/sw/voicesw/tsd_products_support_category_home.html
```

```
ip source-address 10.103.3.201 port 2000
```

```
load 7910 P00403020214
```

```
load 7961 TERM41.7-0-1-1
```

```
load 7961GE TERM41.7-0-1-1
```

```
load 7960-7940 P00307020300
```

```
max-ephones 100
```

```
max-dn 500
```

```
max-conferences 8 gain -6
```

```
dspfarm units 2
```

```
dspfarm transcode sessions 4
```

```
dspfarm 1 MTP00059a3d7441
```

```
dspfarm 2
```

```
hunt-group report delay 1 hours
```

```
Number of hunt-group configured: 14
```

```
hunt-group logout DND
```

```
max-redirect 20
```

```
voicemail 7189
```

```
cnf-file location: system:
```

```
cnf-file option: PER-PHONE-TYPE
```

```
network-locale[0] US   (This is the default network locale for this box)
```

```
user-locale[0] US    (This is the default user locale for this box)
```

```
moh flash:music-on-hold.au
```

```
time-format 12
```

```
date-format mm-dd-yy
```

```
timezone 0 Greenwich Standard Time
```

```
secondary-dialtone 9
```

```
call-forward pattern .T
```

```
transfer-pattern 92......
```

```
transfer-pattern 91..........
```

```
transfer-pattern .T
```

```
after-hours block pattern 1 91900 7-24
```

```
after-hours block pattern 2 9976 7-24
```

```
after-hours block pattern 4 91...976.... 7-24
```

```
night-service time is activated
```

```
night-service date Jan 1 00:00 23:59
```

```
night-service day Mon 17:00 07:00
```

```
night-service day Wed 17:00 07:00
```

```
keepalive 30
```

```
timeout interdigit 10
```

```
timeout busy 10
```

```
timeout ringing 100
```

```
caller-id name-only: enable
```

```
system message XYZ Company
```

```
web admin system name xyz password xxxx
```

```
web admin customer name Customer
```

```
edit DN through Web:  enabled.
```

```
edit TIME through web:  enabled.
```

```
Log (table parameters):
```

```
max-size: 150
```

```
retain-timer: 15
```

```
create cnf-files version-stamp Jan 01 2002 00:00:00
```

```
transfer-system full-consult
```

```
multicast moh 239.10.10.1 port 2000
```

```
fxo hook-flash
```

```
local directory service: enabled.
```

Step 2

Use
                                          			 the show
                                                				  running-config command to verify that the correct ephone-dns and
                                          			 ephones are configured with the night-service bell command. You can also use the show telephony-service
                                                				  ephone-dn and show telephony-service
                                                				  ephone commands to display these parameters.

#### Example:

```
Router# show running-config
```

```
ephone-dn 24 dual-line
```

```
number 2548
```

```
description FrontDesk
```

```
night-service bell
```

```
ephone  1
```

```
mac-address 110F.80C0.FE0B
```

```
type 7960 addon 1 7914
```

```
no dnd feature-ring
```

```
keep-conference
```

```
button  1f40 2f41 3f42 4:30
```

```
button  7m20 8m21 9m22 10m23
```

```
button  11m24 12m25 13m26
```

```
night-service bell
```

### Verify Night
                           	 Service Configuration on SIP Phones

Step 1

Use the show running-config |
                                                				  section telephony-service command to verify the night-service parameters that
                                          			 are listed in the telephony-service portion of the output. Use the show
                                                				  telephony-service command to display the same parameters.

#### Example:

```
Router# show running-config | section telephony-service
```

```
telephony-service
 max-ephones 50
 max-dn 50
 ip source-address 10.50.50.1 port 2000
 service phone sshAccess 0
 service phone webAccess 0
 service directed-pickup gpickup
 time-zone 39
 max-conferences 8 gain -6
 call-park system application
 hunt-group report url suffix 0 to 100
 hunt-group report every 1 hours
 hunt-group logout HLog
 transfer-system full-consult night-service weekday 13:17 14:17
 night-service day Sun 00:05 23:59
 night-service day Sat 00:05 23:59 night-service code *6483 Router# show telephony-service max-ephones 50
 max-dn 50
 ip source-address 10.50.50.1 port 2000
 service phone sshAccess 0
 service phone webAccess 0
  time-zone 39
 max-conferences 8 gain -6 call-park system application hunt-group report url suffix 0 to 100
 hunt-group report every 1 hours
 hunt-group logout HLog
 transfer-system full-consult
 night-service time is activated
 night-service weekday 13:17 14:17
 night-service day Sun 00:05 23:59
 night-service day Sat 00:05 23:59
```

Step 2

Use the show voice register dn and show voice register pool command to verify that the correct voice register
                                          			 dns and phones are configured with the night-service bell command.

#### Example:

```
Router# show voice register dn 1
```

```
Dn Tag 1
Config:
 Number is 8001
 Preference is 0
 Huntstop is disabled
 Auto answer is disabled
 Pickup group is 5
 Night Service Bell is enabled
```

```
Router# show voice register pool 5
```

```
Pool Tag 5
Config:
 Mac address is B000.B4BE.F32C
 Type is 8851
 Number list 1 : DN 5
 Proxy Ip address is 0.0.0.0
 DTMF Relay is disabled
 Call Waiting is enabled
 DnD is disabled
 Video is disabled
 Camera is disabled
 Night Service Bell is enabled
 Busy trigger per button value is 2
```

### Configure Overlaid
                           	 Ephone-dns on SCCP Phones

To create
                                 		  ephone-dns, then assign multiple ephone-dns to a single phone button by using
                                 		  the o or c keyword
                                 		  with the button command, perform the following steps.

Restriction

Call waiting
                                                   				  is disabled when you configure ephone-dn overlays using the o keyword
                                                   				  with the button command. To enable call waiting, you must configure ephone-dn overlays using
                                                   				  the c keyword
                                                   				  with the button command.

Rollover of
                                                   				  overlay calls to another phone button by using the x keyword
                                                   				  with the button command only works to expand coverage if the overlay button is configured with
                                                   				  the o keyword in
                                                   				  the button command. Overlay buttons with call waiting that use the c keyword in the button command are not eligible for overlay rollover.

In Cisco
                                                   				  Unified CME 4.0(3), the Cisco Unified IP Phone 7931G cannot support overlays
                                                   				  that contain ephone-dn configured for dual-line mode.

The primary
                                                   				  ephone-dn on each phone in a shared-line overlay set should be an ephone-dn
                                                   				  that is unique to the phone to guarantee that the phone will have a line
                                                   				  available for outgoing calls, and to ensure that the phone user can obtain
                                                   				  dial-tone even when there are no idle lines available in the rest of the
                                                   				  shared-line overlay set. Use a unique ephone-dn in this manner to provide for a
                                                   				  unique calling party identity on outbound calls made by the phone so that the
                                                   				  called user can see which specific phone is calling.

Octo-line
                                                   				  directory numbers are not supported in button overlay sets.

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn phone-tag [ dual-line ]

- number number

- preference preference-order

- no huntstop or huntstop

- huntstop
                                       				  channel

- call-forward
                                       				  noan

- call-forward
                                       				  busy

- exit

- ephone phone-tag

- mac-address mac-address

- button button-number { o | c } dn-tag , dn-tag [ , dn-tag ... ] button-number { x } overlay-button-number

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

ephone-dn phone-tag [ dual-line ]

#### Example:

```
Router(config)# ephone-dn 10 dual-line
```

Enters
                                             				ephone-dn configuration mode to create an extension (ephone-dn) for a
                                             				Cisco Unified IP phone line.

For
                                                   					 shared-line overlay set: Primary ephone-dn on a phone should be an ephone-dn
                                                   					 that is unique to the phone.

Step 4

number number

#### Example:

```
Router(config-ephone-dn)# number 1001
```

Associates a
                                             				telephone or extension number with the ephone-dn.

Step 5

preference preference-order

#### Example:

```
Router(config-ephone-dn)# preference 1
```

Sets dial-peer
                                             				preference order for an ephone-dn.

preference-order —Preference order for the primary
                                                   					 number associated with an extension (ephone-dn). Type ? for a range of numeric options, where 0 is the
                                                   					 highest preference. Default: 0.

Step 6

no huntstop or huntstop

#### Example:

```
Router(config-ephone-dn)# no huntstop 
or
Router(config-ephone-dn)# huntstop
```

Explicitly enables call hunting behavior for a directory number.

Set this command on all ephone-dns in the overlay set except the final instance.

Required to allow call hunting allow call hunting across multiple numbers on the same line button on an IP phone.

or

Disables call hunting behavior for a directory number.

Set this command on the last ephone-dn within a overlay set.

Required to limit the call hunting to an overlay set.

Step 7

huntstop
                                                				  channel

#### Example:

```
Router(config-ephone-dn)# huntstop channel
```

Only for
                                             				dual-line ephone-dns in overlay set; keeps incoming calls from hunting to the
                                             				second channel if the first channel is busy or does not answer.

Reserves
                                                   					 the second channel for outgoing calls, such as a consultation call to be placed
                                                   					 during a call transfer attempt, or for conferencing

Step 8

call-forward
                                                				  noan

#### Example:

```
Router(config-ephone-dn)# call-forward noan
```

(Optional)
                                             				Forwards incoming unanswered call to next line in the overlay set.

Set this
                                                   					 command on all ephone-dns in the overlay set.

Step 9

call-forward
                                                				  busy

#### Example:

```
Router(config-ephone-dn)# call-forward busy
```

(Optional)
                                             				Forwards incoming call if line is busy.

Set this
                                                   					 command on the last ephone-dn in the overlay set only.

Step 10

exit

#### Example:

```
Router(config-ephone-dn)# exit
```

Exits
                                             				ephone-dn configuration mode

Step 11

ephone phone-tag

#### Example:

```
Router(config)# ephone 4
```

Enters
                                             				ephone configuration mode.

phone-tag —Unique sequence number that identifies
                                                   					 the phone to which you are adding an overlay set.

Step 12

mac-address mac-address

#### Example:

```
Router(config-ephone)# mac-address 1234.5678.abcd
```

Specifies
                                             				the MAC address of the registering phone.

Step 13

button button-number { o | c } dn-tag , dn-tag [ , dn-tag ... ] button-number { x } overlay-button-number

#### Example:

```
Router(config-ephone)# button 1o15,16,17,18,19 2c20,21,22 3x1 4x1
```

Creates a
                                             				set of ephone-dns overlaid on a single button.

o —Overlay button.
                                                   					 Multiple ephone-dns share this button. A maximum of 25 ephone-dns can be
                                                   					 specified for a single button, separated by commas.

c —Overlay button with
                                                   					 call-waiting. Multiple ephone-dns share this button. A maximum of 25 ephone-dns
                                                   					 can be specified for a single button, separated by commas.

x —Separator that
                                                   					 creates a rollover button for an overlay button that was defined using the o keyword. When the
                                                   					 overlay button specified in this command is occupied by an active call, a
                                                   					 second call to one of its ephone-dns will be presented on this button.

dn-tag —Unique
                                                   					 identifier previously defined with the ephone-dn command for the ephone-dn to be added to this
                                                   					 overlay set.

overlay-button-number —Number of the overlay button that
                                                   					 should overflow to this button. Note that the button must have been defined
                                                   					 using the o keyword and not the c keyword.

Step 14

end

#### Example:

```
Router(config-ephone)# end
```

Returns to
                                             				privileged EXEC mode.

### Verify Overlaid Ephone-dns Configuration on SCCP Phone

Step 1

Use the show running-config command or the show telephony-service ephone command to
                                          			 view button assignments.

```
Router# show running-config
```

```
ephone  5
```

```
description Cashier1
```

```
mac-address 0117.FBC6.1985
```

```
type 7960
```

```
button  1o4,5,6,200,201,202,203,204,205,206 2x1 3x1
```

Step 2

Use the show ephone overlay command to display the
                                          			 configuration and current status of registered overlay ephone-dns.

Step 3

Use the show dialplan number command to display all
                                          			 the number resolutions of a particular phone number, which allows you to detect
                                          			 whether calls are going to unexpected destinations. This command is useful for
                                          			 troubleshooting cases in which you dial a number but the expected phone does
                                          			 not ring.

### Enable
                           	 Out-Of-Dialog REFER

Restriction

The call
                                                   				  waiting, conferencing, hold, and transfer call features are not supported while
                                                   				  the Refer-Target is ringing.

In a SIP to
                                                   				  SIP scenario, no ringback is heard by the Referee when Refer-Target is ringing.

#### Before you begin

Cisco Unified
                                       				CME 4.1 or a later version.

The
                                       				application that initiates OOD-R, such as a click-to-dial application, and its
                                       				directory server must be installed and configured.

For
                                       				information on the SIP REFER and NOTIFY methods used between the directory
                                       				server and Cisco Unified CME, see RFC 3515 , The Session Initiation Protocol (SIP) Refer
                                       				Method.

For
                                       				information on the message flow Cisco Unified CME uses when initiating a
                                       				session between the Referee and Refer-Target, see RFC 3725 , Best Current Practices for Third Party Call
                                       				Control (3pcc).

### SUMMARY STEPS

- enable

- configure terminal

- sip-ua

- refer-ood enable [ request-limit ]

- exit

- voice register global

- authenticate ood-refer

- authenticate credential tag location

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

sip-ua

#### Example:

```
Router(config)# sip-ua
```

Enters SIP
                                             				user-agent configuration mode to configure the user agent.

Step 4

refer-ood enable [ request-limit ]

#### Example:

```
Router(config-sip-ua)# refer-ood enable 300
```

Enables OOD-R
                                             				processing.

request-limit —Maximum number of concurrent
                                                   					 incoming OOD-R requests that the router can process. Range: 1 to 500. Default:
                                                   					 500.

Step 5

exit

#### Example:

```
Router(config-sip-ua)# exit
```

Exits SIP
                                             				user-agent configuration mode.

Step 6

voice register global

#### Example:

```
Router(config)# voice register global
```

Enters voice
                                             				register global configuration mode to set global parameters for all supported
                                             				SIP phones in a Cisco Unified CME or Cisco Unified SRST environment.

Step 7

authenticate ood-refer

#### Example:

```
Router(config-register-global)# authenticate ood-refer
```

(Optional)
                                             				Enables authentication of incoming OOD-R requests using RFC 2617-based digest
                                             				authentication.

Step 8

authenticate credential tag location

#### Example:

```
Router(config-register-global)# authenticate credential 1 flash:cred1.csv
```

(Optional)
                                             				Specifies the credential file to use for authenticating incoming OOD-R
                                             				requests.

tag —Number that identifies the credential file to
                                                   					 use for OOD-R authentication. Range: 1 to 5.

location —Name and location of the credential file
                                                   					 in URL format. Valid storage locations are TFTP, HTTP, and flash memory.

Step 9

end

#### Example:

```
Router(config-register-global)# end
```

Exits to
                                             				privileged EXEC mode.

#### What to do next

If you are configuring Cisco Unified CME for the first time on this router, you are ready to configure system-level parameters.
                                       See Configure System-Level Parameters .

If you
                                       				modified network parameters for an already configured Cisco Unified CME router,
                                       				you are ready to generate the configuration file to save the modifications. See Generate Configuration Files for Phones .

### Verify OOD-R Configuration

### SUMMARY STEPS

- show running-config

- show sip-ua status refer-ood

### DETAILED STEPS

Step 1

show running-config

This command verifies your configuration.

#### Example:

```
Router# show running-config
!
voice register global
mode cme
source-address 10.1.1.2 port 5060
load 7971 SIP70.8-0-1-11S
load 7970 SIP70.8-0-1-11S
load 7961GE SIP41.8-0-1-0DEV
load 7961 SIP41.8-0-1-0DEV
authenticate ood-refer
authenticate credential 1 tftp://172.18.207.15/labtest/cred1.csv
create profile sync 0004550081249644
.
.
.
sip-ua
refer-ood enable
```

Step 2

show sip-ua status refer-ood

This command displays OOD-R configuration settings.

#### Example:

```
Router# show sip-ua status refer-ood

Maximum allow incoming out-of-dialog refer 500
Current existing incoming out-of-dialog refer dialogs: 1
outgoing out-of-dialog refer dialogs: 0
```

### Troubleshooting
                           	 OOD-R

Step 1

Use the debug ccsip
                                                				  messages command to display the SIP messages exchanged between
                                          			 the SIP UA client and the router.

Step 2

Use the debug voip application
                                                				  oodrefer command to display debugging messages for the OOD-R
                                          			 feature.

## Configuration Examples for Call Coverage Features

### Call Hunt: Examples

#### Example for Setting Ephone-dn Dial-Peer Preference

The following example sets a preference number of 2 for the primary
                                    		  number of ephone-dn 3:

```
ephone-dn 3
```

```
number 3001
```

```
preference 2
```

#### Example for Disabling Huntstop

The following example shows an instance in which huntstop is not
                                    		  desired and is explicitly disabled. In this example, ephone 4 is configured
                                    		  with two lines, each with the same extension number 5001. This is done to allow
                                    		  the second line to provide call waiting notification for extension number 5001
                                    		  when the first line is in use. Setting no huntstop on the first line (ephone-dn 1)
                                    		  allows incoming calls to hunt to the second line (ephone-dn 2) on the same
                                    		  phone when the ephone-dn 1 line is busy.

Ephone-dn 2 has call forwarding set to extension 6000, which
                                    		  corresponds to a locally attached answering machine connected to a foreign
                                    		  exchange station (FXS) voice port. The plain old telephone service (POTS) dial
                                    		  peer for extension 6000 also has the dial-peer huntstop attribute explicitly
                                    		  set to prevent further hunting.

```
ephone-dn 1
 number 5001
 no huntstop
 preference 1
 call-forward noan 6000

ephone-dn 2
 number 5001
 preference 2
 call-forward busy 6000
 call-forward noan 6000

ephone 4
 button 1:1 2:2
 mac-address 0030.94c3.8724
 dial-peer voice 6000 pots
 destination-pattern 6000
 huntstop port 1/0/0
 description answering-machine
```

#### Example for Channel Huntstop

The following is an example that uses the huntstop channel command. It shows a
                                    		  dual-line ephone-dn configuration in which calls do not hunt to the second
                                    		  channel of any ephone-dn, but they do hunt through each ephone-dn’s channel 1
                                    		  in this order: ephone-dn 10, ephone-dn 11, ephone-dn 12.

```
ephone-dn 10 dual-line
```

```
number 1001
```

```
no huntstop
```

```
huntstop channel
```

```
ephone-dn 11 dual-line
```

```
number 1001
```

```
no huntstop
```

```
huntstop channel
```

```
preference 1
```

```
ephone-dn 12 dual-line
```

```
number 1001
```

```
no huntstop
```

```
huntstop channel
```

```
preference 2
```

#### Example for SIP Call Hunt

The following example shows a typical configuration in which huntstop
                                    		  is required. The huntstop command is enabled and prevents
                                    		  calls to extension 5001 from being rerouted to the on-net H.323 dial peer for
                                    		  5... when extension 5001 is busy (three periods are used as wild cards).

```
voice register dn 1
```

```
number 5001
```

```
huntstop
```

```
voice register pool 4
```

```
number 1 dn 1
```

```
id-mac 0030.94c3.8724
```

```
dial-peer voice 5000 voip
```

```
destination-pattern 5...
```

```
session target ipv4:192.168.17.225
```

```
session protocol sipv2
```

### Example for Call
                           	 Pickup

The following
                                 		  example assigns the line that has an ephone-dn tag of 55 to pickup group 2345:

```
ephone-dn 55 
 number 2555 
 pickup-group 2345
```

The following
                                 		  example globally disables directed call pickup and changes the action of the
                                 		  PickUp soft key to perform local group call pickup rather than directed call
                                 		  pickup:

```
telephony-service 
 no service directed-pickup
```

### Example for Call-Waiting Beep

In the following example, ephone-dn 10 neither accepts nor generates a
                                 		  beep, ephone-dn 11 does not accept a beep, and ephone-dn 12 does not generate a
                                 		  beep:

```
ephone-dn 10
 no call-waiting beep
 number 4410

ephone-dn 11
 no call-waiting beep accept
 number 4411

ephone-dn 12
 no call-waiting beep generate
 number 4412
```

### Example for Call-Waiting Ring

The following example specifies that a short ring will indicate a call
                                 		  is waiting for extension 5533:

```
ephone-dn 20
 number 5533
 call-waiting ring
```

### Examples for Hunt Group

#### Example for Sequential Ephone-Hunt Group

The following example defines a sequential ephone hunt group with the
                                    		  pilot number 5600 and the final number 6000, with three numbers in the list of
                                    		  phones that answer for the pilot number:

```
ephone-hunt 2 sequential
```

```
pilot 5600
```

```
list 5621, *, 5623
```

```
final 6000
```

```
max-timeout 10
```

```
timeout 20, 20, 20
```

```
fwd-final  orig-phone
```

#### Example for Peer Ephone-Hunt Group

The following example defines peer ephone hunt group 10 with a pilot
                                    		  number 450, a final number 500, and four numbers in the list. After a call is
                                    		  redirected four times (makes four hops), it is redirected to the final number.

```
ephone-hunt 10 peer
```

```
pilot 450
```

```
list 451, 452, 453, 477
```

```
final 500
```

```
max-timeout 10
```

```
timeout 3, 3, 3, 3
```

#### Example for Longest-idle Ephone-Hunt Group

The following example defines longest-idle ephone hunt group 1 with a
                                    		  pilot number 7501 and 11 numbers in the list. After a call is redirected five
                                    		  times, it is redirected to the final number.

```
ephone-hunt 1 longest-idle
```

```
pilot 7501
```

```
list 7001, 7002, 7023, 7028, 7045, 7062, 7067, 7072, 7079, 7085, 7099
```

```
final 8000
```

```
preference 1
```

```
hops 5
```

```
timeout 20
```

```
no-reg
```

#### Example for Longest-idle Ephone-Hunt Group Using From-Ring
                              	 Option

The following example defines longest-idle ephone hunt group 1 with a
                                    		  pilot number 7501, a final number 8000, and 11 numbers in the list. Because
                                    		  the from-ring command is used, on-hook time stamps
                                    		  will be recorded when calls ring extensions and when calls are answered. After
                                    		  a call is redirected six times (makes six hops), it is redirected to the final
                                    		  number, 8000. The max-redirect command is used to increase the
                                    		  number of redirects that are allowed because the number of hops (six) is larger
                                    		  than the default number of redirects that are allowed in the system (five).

```
ephone-hunt 1 longest-idle
```

```
pilot 7501
```

```
list 7001, 7002, 7023, 7028, 7045, 7062, 7067, 7072, 7079, 7085, 7099
```

```
final 8000
```

```
from-ring
```

```
preference 1
```

```
hops 6
```

```
timeout 20
```

```
telephony-service
```

```
max-redirect 8
```

#### Example for Sequential Hunt Group

In the following parallel hunt-group example, when callers dial
                                    		  extension 1000, extension 1001, 1002, 1003, and 1004 ring simultaneously. The
                                    		  first extension to answer is connected. If none of the extensions answers
                                    		  within 60 seconds, the call is forwarded to extension 2000, which is the number
                                    		  for voice mail.

```
voice hunt-group 4 parallel
```

```
final 2000
```

```
list 1001,1002,1003,1004
```

```
timeout 60
```

```
pilot 1000
```

```
preference 1 secondary 9
```

```
!
```

```
!
```

```
ephone-dn  1  octo-line
```

```
number 1001
```

```
!
```

```
ephone-dn  2
```

```
number 1002
```

```
!
```

```
ephone-dn  3  dual-line
```

```
number 1003
```

```
!
```

```
ephone-dn  4
```

```
number 1004
```

```
!
```

```
!
```

```
ephone  1
```

```
max-calls-per-button 4
```

```
mac-address 02EA.EAEA.0001
```

```
button  1:1
```

```
!
```

```
!
```

```
ephone  2
```

```
mac-address 001C.821C.ED23
```

```
button  1:2
```

```
!
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
button  1:3
```

```
!
```

```
!
```

```
ephone  4
```

```
mac-address 0030.94C3.053E
```

```
button  1:4
```

#### Example for
                              	 Preventing Local Call Forwarding in Parallel Voice Hunt-Groups

The following
                                    		  example shows how to prevent the forwarding of local calls to the final
                                    		  destination in parallel voice hunt-group 1:

```
Router# configure terminal Router(config)# voice hunt-group 1 parallel Router(config-voice-hunt-group)# no forward local-calls to-final
```

#### Example for
                              	 Associating a Name with a Called Voice Hunt-Group

When incoming call
                                    		  A reaches voice hunt group B and lands on final C, extension C does not show
                                    		  the name of the forwarder because the voice hunt group is not configured to
                                    		  display the name. To display the name of the forwarder and the final number,
                                    		  two separate names are required for the primary and secondary pilot numbers.

ephone-hunt

The following is a
                                    		  sample output of the show run command when the primary and secondary pilot names are configured in
                                    		  ephone-hunt configuration mode:

```
ephone-hunt 10 sequential
 pilot 1010 secondary 1020
 list 2004, 2005
 final 2006
 timeout 8, 8 name "EHUNT PRIMARY" secondary "EHUNT SECONDARY" ephone-hunt 11 peer
 pilot 1012 secondary 1022
 list 2004, 2005
 final 2006
 timeout 8, 8 name EHUNT1 secondary EHUNT1-SEC
```

The following is a
                                    		  sample output of the show
                                          				ephone-hunt command when the primary and secondary pilot names
                                    		  are configured in ephone-hunt configuration mode:

```
show ephone-hunt 10
Group 10
type: sequential
pilot number: 1010, peer-tag 20010 pilot name: EHUNT PRIMARY secondary number: 1020, peer-tag 20011 secondary name: EHUNT SECONDARY
```

voice hunt-group

The following
                                    		  example shows how the primary and secondary pilot names are configured in voice
                                    		  hunt-group configuration mode:

```
voice hunt-group 24 parallel
final 097
list 885,886,124,154
timeout 20 
pilot 021 secondary 621
name SALES secondary SALES-SECONDARY
```

The following is a
                                    		  sample output of the show voice
                                          				hunt-group command when the primary and secondary pilot names are
                                    		  configured in voice hunt-group configuration mode:

```
show voice hunt-group 1
Group 1
type: parallel
pilot number: 1000, peer-tag 2147483647
secondary number: 2000, peer-tag 2147483646 pilot name: SALES secondary name: SALES-SECONDARY list of numbers:
		Member Used-by State  Login/Logout
		====== ======  =====  ==========
		2004   2004    up     login
		2005   2005    down   -
preference: 0
preference (sec): 0
timeout: 180
final_number:
stat collect: no
phone-display: no
```

#### Example for
                              	 Specifying a Description for a Voice Hunt-Group

The following
                                    		  example shows how to specify a description for voice hunt-group 12 using the description command and presents the description in the output of the do show run command:

```
Router(config)# voice hunt-group 12 parallel
Router (config-voice-hunt-group)# description ?
 LINE  description for this hunt group
Router (config-voice-hunt-group)# description specific huntgroup description Router (config-voice-hunt-group)# do show run | sec voice hunt-group
voice hunt-group 12 parallel
 timeout 0 description specific huntgroup description
```

#### Example for Logout Display

In the following example, the description is set to “Marketing Hunt
                                    		  Group.” This information will be shown in the configuration output and also on
                                    		  the display of IP phones that are receiving calls from this hunt group. The
                                    		  display-logout message is set to “Night Service,” which will be displayed on IP
                                    		  phones that are members of the hunt group when all the members are logged out.

```
ephone-hunt 17 sequential
```

```
pilot 3000
```

```
list 3011, 3021, 3031
```

```
timeout 10
```

```
final 7600
```

```
description Marketing Hunt Group
```

```
display-logout Night Service
```

#### Example for
                              	 Displaying Total Logged-In Time and Total Logged-Out Time for Each Hunt-Group
                              	 Agent

The following
                                    		  example displays the duration (in sec) since a specific agent logged into and
                                    		  logged out of ephone hunt group 1 from 4:00 a.m. to 5:00 a.m. (0400 to 0500):

```
show ephone-hunt 1 statistics Wed 04:00 - 05:00
	Max Agents: 3
	Min Agents: 3
	Total Calls: 9
	Answered Calls: 7
	Abandoned Calls: 2
	Average Time to Answer (secs): 6
	Longest Time to Answer (secs): 13
	Average Time in Call (secs): 75
	Longest Time in Call (secs): 161
	Average Time before Abandon (secs): 8
	Calls on Hold: 2
	Average Time in Hold (secs): 16
	Longest Time in Hold (secs): 21
	Per agent statistics:
		Agent: 5012
			From Direct Call:
				Total Calls Answered: 3
				Average Time in Call (secs): 70
				Longest Time in Call (secs): 150
				Totals Calls on Hold: 1
				Average Hold Time (secs): 21
				Longest Hold Time (secs): 21
			From Queue:
				Total Calls Answered: 3
				Average Time in Call (secs): 55
				Longest Time in Call (secs): 78
				Total Calls on Hold: 2
				Average Hold Time (secs): 19
				Hold Time (secs): 26 Total logged in Time (secs) : 3000 Total logged out Time (secs) : 600 Agent: 5013
			From Direct Call:
				Calls Answered: 3
				Average Time in Call (secs): 51
				Longest Time in Call (secs): 118
				Totals Calls on Hold: 1
				Average Hold Time (secs): 11
				Longest Hold Time (secs): 11
			From Queue:
				Total Calls Answered: 1
				Average Time in Call (secs): 4
				Longest Time in Call (secs): 4 Total logged in Time (secs) : 3000 Total logged out Time (secs) : 600 Agent: 5014
			From Direct Call:
				Total Calls Answered: 1
				Average Time in Call (secs): 161
				Longest Time in Call (secs): 161
			From Queue:
				Total Calls Answered: 1
				Time in Call (secs): 658
				Longest Time in Call (secs): 658 Total logged in Time (secs) : 3000 Total logged out Time (secs) : 600 Queue related statistics:
		Total calls presented to the queue: 5
		Calls handoff to IOS: 5
		Number of calls in the queue: 0
		Average time to handoff (secs): 2
		Longest time to handoff (secs): 3
		Number of abandoned calls: 0
		Average time before abandon (secs): 0
		Calls forwarded to voice mail: 0
		Calls answered by voice mail: 0
		Number of error calls: 0
```

The per agent
                                                			 statistics are displayed for both static and dynamic agents.

#### Example for Dynamic Membership To Ephone-Hunt

The following example creates four ephone-dns and a hunt group that
                                    		  includes the first ephone-dn and two wildcard slots. The last three ephone-dns
                                    		  are enabled for group hunt dynamic membership. Each of them can join and leave
                                    		  the hunt group whenever one of the wildcard slots is available. Standard FACs
                                    		  have been enabled, and the agents use standard FACs to join (*3) and leave (#3)
                                    		  the hunt group. You can also use the fac command to create custom FACs for these
                                    		  actions if you prefer.

```
ephone-dn 22
```

```
number 4566
```

```
ephone-dn 24
```

```
number 4568
```

```
ephone-hunt login
```

```
ephone-dn 25
```

```
number 4569
```

```
ephone-hunt login
```

```
ephone-dn 26
```

```
number 4570
```

```
ephone-hunt login
```

```
ephone-hunt 1 peer
```

```
list 4566,*,*
```

```
timeout 10
```

```
final 7777
```

```
telephony-service
```

```
fac standard
```

#### Example for
                              	 Dynamic Membership To Voice Hunt-Group

The following
                                    		  example creates one voice register dn and one voice hunt group which includes
                                    		  two wildcard slots. The voice register dn is enabled for group hunt dynamic
                                    		  membership. The DN can join and unjoin the hunt group whenever one of the
                                    		  wildcard slots is available. Standard FACs have been enabled, and the agents
                                    		  use standard FACs to join (*3) and unjoin (#3) the hunt group. You can also use
                                    		  the fac command
                                    		  to create custom FACs for these actions if you prefer.

```
Voice register dn 1 Number 1001 Voice-hunt-groups login Voice hunt-group 1 parallel Pilot number 100 List 1001, 1002, 1003, *, *
```

The following
                                    		  example creates three lines (3 voice register dns and 1 ephone dn) in phones
                                    		  with mixed shared line DNs. Using the three wildcard entries configured, the
                                    		  DNs can join and unjoin the hunt groups. Here, standard FACs have been enabled,
                                    		  and the agents use standard FACs to join (*3) and unjoin (#4) the hunt group.

```
ephone-dn  1  dual-line
 number 1001
 shared-line sip
ephone  1
 device-security-mode none
 mac-address 1111.4444.3301
 type 7970
 button  1:1 

voice register dn  1
 voice-hunt-groups login
 number 1001
 name phone-1
 shared-line max-calls 4

voice register dn  2
 voice-hunt-groups login
 number 2001
 name phone-2
 shared-line max-calls 4

voice register dn  3
 voice-hunt-groups login
 number 2002
 name phone-3
 shared-line max-calls 4

voice register pool  1
 busy-trigger-per-button 2
 id mac 00DA.5527.1BB7
 type 8841
 number 1 dn 1
 number 2 dn 2
 number 3 dn 3
 dtmf-relay rtp-nte
 username cisco1 password cisco
 codec g711ulaw
 no vad 
 
voice register pool  2
 busy-trigger-per-button 2
 id mac 00DA.5527.1BB7
 type 8841
 number 1 dn 1
 number 2 dn 2
 number 3 dn 3
 dtmf-relay rtp-nte
 username cisco1 password cisco
 codec g711ulaw
 no vad
```

#### Example for Agent
                              	 Status Control using SCCP Phones

The following
                                    		  example sets up a peer ephone hunt group. It also establishes the appearance
                                    		  and order of soft keys for phones that are configured with ephone-template 7.
                                    		  These phones will have the HLog key available when they are idle, when they
                                    		  have seized a line, or when they are connected to a call. Phones without
                                    		  softkeys can use the standard HLog codes to toggle ready and not-ready status.

```
ephone-hunt 10 peer
```

```
pilot 450
```

```
list 451, 452, 453, 477
```

```
final 500
```

```
timeout 45
```

```
telephony-service
```

```
hunt-group logout HLog
```

```
fac standard
```

```
ephone-template 7
```

```
softkeys connected Endcall Hold Transfer HLog
```

```
softkeys idle Newcall Redial Pickup Cfwdall HLog
```

```
softkeys seized Endcall Redial Pickup Cfwdall HLog
```

#### Example for Agent
                              	 Status Control using SIP Phones

The following
                                    		  example sets up a peer voice hunt group. It also establishes the appearance and
                                    		  order of soft keys for phones that are configured with voice register template
                                    		  7. These phones will have the HLog key available when idle, when there is a
                                    		  ringIn, or when connected to a call. Phones without softkeys can use the
                                    		  standard HLog codes to toggle ready and not-ready status.

```
voice hunt-group 10 peer
 pilot 450
 list 451, 452, 453, 477
 final 500
 timeout 45
 
telephony-service
 hunt-group logout HLog
 fac standard
 
voice register template 7
 softkeys connected Endcall Hold Transfer HLog
 softkeys idle Newcall Redial Pickup Cfwdall HLog
 softkeys ringIn Answer DND iDivert HLog
```

#### Example for
                              	 Automatic Agent Not-Ready for Ephone Hunt Group

The following
                                    		  example enables automatic status change to not-ready after one unanswered hunt
                                    		  group call (the default) for both dynamic and static hunt group members (the
                                    		  default). It also specifies that the phones which are automatically put into
                                    		  the not-ready status should only be blocked from further hunt-group calls and
                                    		  that they should be able to receive calls that directly dial their extensions.

```
ephone-hunt 3 peer
```

```
pilot 4200
```

```
list 1001, 1002, 1003
```

```
timeout 10
```

```
auto logout
```

```
final 4500
```

```
telephony-service
```

```
hunt-group logout HLog
```

The following
                                    		  example enables automatic status change to not-ready after two unanswered hunt
                                    		  group calls for any ephone-dn that dynamically logs in to the hunt group using
                                    		  the wildcard slot in the hunt group list. Phones that are automatically placed
                                    		  in the not-ready status when they do not answer two hunt-group calls are also
                                    		  placed into DND status (they will also not accept directly dialed calls).

```
ephone-hunt 3 peer
```

```
pilot 4200
```

```
list 1001, 1002, *
```

```
timeout 10
```

```
auto logout 2 dynamic
```

```
final 4500
```

```
telephony-service
```

```
hunt-group logout DND
```

#### Example for
                              	 Automatic Agent Not-Ready for Voice Hunt Group

In the following example, voice hunt-group 1 is configured to permit
                                    		  automatic logout. If hunt group calls that are presented to 1001, 1002, 1003,
                                    		  and 1004 are unanswered (that is, if they ring longer than 40 seconds each),
                                    		  voice register pool 1, voice register pool 2, ephone 1, and ephone 2 are
                                    		  automatically logged out. All unanswered calls are sent to DN 5000.

```
Router(config)# voice register dn 1 Router(config-register-dn)# number 1001 Router(config)# voice register dn 2 Router(config-register-dn)# number 1002 Router(config)# ephone-dn 1 Router(config-ephone-dn)# number 1003 Router(config)# ephone-dn 2 Router(config-ephone-dn)# number 1004 Router(config)# voice register pool 1 Router(config-register-pool)# number 1 dn 1 Router(config)# voice reister pool 2 Router(config-register-pool)# number 1 dn 2 Router(config)# ephone 1 Router(config-ephone)# button 1:1 Router(config)# ephone 2 Router(config-ephone)# button 1:2 Router(config)# voice hunt-group 1 peer Router(config-voice-hunt)# pilot 1111 Router(config-voice-hunt)# list 1001, 1002, 1003, 1004 Router(config-voice-hunt)# final 5000 Router(config-voice-hunt)# timeout 40 Router(config-voice-hunt)# auto logout 4
```

#### Example for Call
                              	 Statistics From a Voice Hunt Group

The following is a
                                    		  sample output from the show voice hunt-group
                                          				statistics command. The output includes direct calls to a voice
                                    		  hunt group number and calls from queue/B-ACD.

```
Router# show voice hunt-group 1 statistics last 1 h Wed 04:00 - 05:00
	Max Agents: 3
	Min Agents: 3
	Total Calls: 9
	Answered Calls: 7
	Abandoned Calls: 2
	Average Time to Answer (secs): 6
	Longest Time to Answer (secs): 13
	Average Time in Call (secs): 75
	Longest Time in Call (secs): 161
	Average Time before Abandon (secs): 8
	Calls on Hold: 2
	Average Time in Hold (secs): 16	
	Longest Time in Hold (secs): 21
	Per agent statistics:
		Agent: 5012
			From Direct Call:
				Total Calls Answered: 3
				Average Time in Call (secs): 70
				Longest Time in Call (secs): 150
				Totals Calls on Hold: 1
				Average Hold Time (secs): 21
				Longest Hold Time (secs): 21
			From Queue:
				Total Calls Answered: 3
				Average Time in Call (secs): 55
				Longest Time in Call (secs): 78
				Total Calls on Hold: 2
				Average Hold Time (secs): 19
				Longest Hold Time (secs): 26
				Total Loged in Time (secs): 3000
				Total Loged out Time (secs): 600
		Agent: 5013
			From Direct Call:
				Total Calls Answered: 3
				Average Time in Call (secs): 51
				Longest Time in Call (secs): 118
				Totals Calls on Hold: 1
				Average Hold Time (secs): 11
				Longest Hold Time (secs): 11
			From Queue:
				Total Calls Answered: 1
				Average Time in Call (secs): 4
				Longest Time in Call (secs): 4
				Total Loged in Time (secs): 3000
				Total Loged out Time (secs): 600
		Agent: 5014
			From Direct Call:
				Total Calls Answered: 1
				Average Time in Call (secs): 161
				Longest Time in Call (secs): 161
			From Queue:
				Total Calls Answered: 1
				Average Time in Call (secs): 658
				Longest Time in Call (secs): 658
				Total Loged in Time (secs): 3000
				Total Loged out Time (secs): 600

	Queue related statistics:
		Total calls presented to the queue: 5
		Calls handoff to IOS: 5
		Number of calls in the queue: 0
		Average time to handoff (secs): 2
		Longest time to handoff (secs): 3
		Number of abandoned calls: 0
		Average time before abandon (secs): 0
		Calls forwarded to voice mail: 0
		Calls answered by voice mail: 0
		Number of error calls: 0
```

#### Example for Night
                              	 Service on SCCP Phones

The following
                                    		  example provides night service before 8 a.m. and after 5 p.m. Monday through
                                    		  Friday, before 8 a.m. and after 1 p.m. on Saturday, and all day Sunday.
                                    		  Extension 1000 is designated as a night-service extension. Incoming calls to
                                    		  extension 1000 during the night-service period ring on extension 1000 and
                                    		  provide night-service notification to phones that are designated as
                                    		  night-service phones. In this example, the night-service phones are ephone 14
                                    		  and ephone 15. The night-service notification consists of a single ring on the
                                    		  phone and a display of “Night Service 1000.” A night-service toggle code has
                                    		  been configured, *6483 (*NITE), by which a phone user can activate or
                                    		  deactivate night-service conditions during the hours of night service.

```
telephony-service
```

```
night-service day mon 17:00 08:00
```

```
night-service day tue 17:00 08:00
```

```
night-service day wed 17:00 08:00
```

```
night-service day thu 17:00 08:00
```

```
night-service day fri 17:00 08:00
```

```
night-service day sat 13:00 12:00
```

```
night-service day sun 12:00 08:00
```

```
night-service code *6483
```

```
!
```

```
ephone-dn 1
```

```
number 1000
```

```
night-service bell
```

```
!
```

```
ephone-dn 2
```

```
number 1001
```

```
night-service bell
```

```
!
```

```
ephone-dn 10
```

```
number 2222
```

```
!
```

```
ephone-dn 11
```

```
number 3333
```

```
!
```

```
ephone 5
```

```
mac-address 1111.2222.0001
```

```
button 1:1 2:2
```

```
!
```

```
ephone 14
```

```
mac-address 1111.2222.0002
```

```
button 1:10
```

```
night-service bell
```

```
!
```

```
ephone 15
```

```
mac-address 1111.2222.0003
```

```
button 1:11
```

```
night-service bell
```

#### Example for Night
                              	 Service on SIP Phones

The following
                                    		  example provides night service everyday before 10:00 am and after 7:00 pm.
                                    		  Incoming calls to extension 3000 during the night-service period ring on
                                    		  extension 3000 and provide night-service notification to phones that are
                                    		  designated as night-service phones. In this example, the night-service phones
                                    		  are pool 2 and pool 3. The night-service notification consists of a single ring
                                    		  on the phone and a display of “Night Service 3000.” A night-service toggle code
                                    		  has been configured, *8765 (*NITE), by which a phone user can activate or
                                    		  deactivate night-service conditions during the hours of night service.

```
telephony-service
night-service everyday 19:00 10:00
night-service code *8765
service directed-pickup gpickup
call-park system application
```

```
voice register dn 1
number 3000
night-service bell
```

```
voice register dn 2
number 3001
night-service bell
```

```
voice register dn 10
number 5555
```

```
voice register dn 11
number 6666
```

```
voice register pool 1
mac-address 1111.2222.0001
number 1 dn 1
number 2 dn 2
```

```
voice register pool 2
mac-address 1111.2222.0002
number 1 dn 10
night-service bell
```

```
voice register pool 3
mac-address 1111.2222.0003
number 1 dn 11
night-service bell
```

#### Examples for Overlaid Ephone-dns

##### Example for Overlaid Ephone-dn

```
ephone-dn 1
 number 1001
 no huntstop
 preference 0

ephone-dn 2
 number 1001
 no huntstop
 preference 1

ephone-dn 3
 number 1001
 huntstop
 preference 2

ephone 10
 button 1o1,2,3
 ephone 11
 button 1o1,2,3

ephone 12
 button 1o1,2,3
```

##### Example for Overlaid Dual-Line Ephone-dn

The following example shows how to overlay dual-line ephone-dns. In
                                       		  addition to using the huntstop and preference commands, you must use the huntstop channel command to prevent calls
                                       		  from hunting to the second channel of an ephone-dn. This example overlays five
                                       		  ephone-dns on button 1 on five different ephones. This allows five separate
                                       		  calls to the same number to be connected simultaneously, while occupying only
                                       		  one button on each phone.

```
ephone-dn 10 dual-line
```

```
number 1001
```

```
no huntstop
```

```
huntstop channel
```

```
preference 0
```

```
ephone-dn 11 dual-line
```

```
number 1001
```

```
no huntstop
```

```
huntstop channel
```

```
preference 1
```

```
ephone-dn 12 dual-line
```

```
number 1001
```

```
no huntstop
```

```
huntstop channel
```

```
preference 2
```

```
ephone-dn 13 dual-line
```

```
number 1001
```

```
preference 3
```

```
no huntstop
```

```
huntstop channel
```

```
ephone-dn 14 dual-line
```

```
number 1001
```

```
preference 4
```

```
huntstop
```

```
huntstop channel
```

```
ephone 33
```

```
mac 00e4.5377.2a33
```

```
button 1o10,11,12,13,14
```

```
ephone 34
```

```
mac 9c33.0033.4d34
```

```
button 1o10,11,12,13,14
```

```
ephone 35
```

```
mac 1100.8c11.3865
```

```
button 1o10,11,12,13,14
```

```
ephone 36
```

```
mac 0111.9c87.3586
```

```
button 1o10,11,12,13,14
```

```
ephone 37
```

```
mac 01a4.8222.3911
```

```
button 1o10,11,12,13,14
```

##### Example for Shared-line Overlaid Ephone-dns

The following is an example of a unique ephone-dn as the primary dn in
                                       		  a simple shared-line overlay configuration. The no huntstop command is configured for all the
                                       		  ephone-dns except ephone-dn 12, the last one in the overlay set. Because the
                                       		  ephone-dns are dual-line dns, the huntstop-channel command is also configured
                                       		  to ensure that the second channel remains free for outgoing calls and for
                                       		  conferencing.

```
ephone-dn 1 dual-line
```

```
number 101
```

```
huntstop-channel
```

```
!
```

```
ephone-dn 2 dual-line
```

```
number 102
```

```
huntstop-channel
```

```
!
```

```
ephone-dn 10 dual-line
```

```
number 201
```

```
no huntstop
```

```
huntstop-channel
```

```
!
```

```
ephone-dn 11 dual-line
```

```
number 201
```

```
no huntstop
```

```
huntstop-channel
```

```
!
```

```
ephone-dn 12 dual-line
```

```
number 201
```

```
huntstop-channel
```

```
!
```

```
!The following ephone configuration includes (unique) ephone-dn 1 as the primary line in a shared-line overlay
```

```
ephone 1
```

```
mac-address 1111.1111.1111
```

```
button 1o1,10,11,12
```

```
!
```

```
!The next ephone configuration includes (unique) ephone-dn 2 as the primary line in another shared-line overlay
```

```
!
```

```
ephone 2
```

```
mac-address 2222.2222.2222
```

```
button 1o2,10,11,12
```

##### Example for Overlaid Ephone-dn with Call Waiting

In following example, button 1 on ephone 1 though ephone 3 uses the
                                       		  same set of overlaid ephone-dns with call waiting that share the number 1111.
                                       		  The button also accept calls to each ephone’s unique (nonshared) ephone-dn
                                       		  number. Note that if ephone-dn 10 and ephone-dn 11 are busy, the call will go
                                       		  to ephone-dn 12. If ephone-dn 12 is busy, the call will go to voice mail.

```
ephone-dn 1 dual-line
```

```
number 1001
```

```
ephone-dn 2 dual-line
```

```
number 1001
```

```
ephone-dn 3 dual-line
```

```
number 1001
```

```
ephone-dn 10 dual-line
```

```
number 1111
```

```
no huntstop
```

```
huntstop channel
```

```
call-forward noan 7000 timeout 30
```

```
ephone-dn 11 dual-line
```

```
number 1111
```

```
preference 1
```

```
no huntstop
```

```
huntstop channel
```

```
call-forward noan 7000 timeout 30
```

```
ephone-dn 12 dual-line
```

```
number 1111
```

```
preference 2
```

```
huntstop channel
```

```
call-forward noan 7000 timeout 30
```

```
call-forward busy 7000
```

```
ephone 1
```

```
button 1c1,10,11,12
```

```
ephone 2
```

```
button 1c2,10,11,12
```

```
ephone 3
```

```
button 1c3,10,11,12
```

##### Example for Overlaid Ephone-dns with Rollover Buttons

The following example configures a “3x3” shared-line setup for three
                                       		  ephones and nine shared lines (ephone-dns 20 to 28). Each ephone has a unique
                                       		  ephone-dn for each of its three buttons (ephone-dns 11 to 13 on ephone 1,
                                       		  ephone-dns 14 to 16 on ephone 2, and ephone-dns 17 to 19 on ephone 3). The rest
                                       		  of the ephone-dns are shared among the three phones. Three phones with three
                                       		  buttons each can take nine calls. The overflow buttons provide the ability for
                                       		  an incoming call to ring on the first available button on each phone.

```
ephone-dn 11
```

```
number 2011
```

```
ephone-dn 12
```

```
number 2012
```

```
ephone-dn 13
```

```
number 2013
```

```
ephone-dn 14
```

```
number 2014
```

```
.
```

```
.
```

```
.
```

```
ephone-dn 28
```

```
number 2028
```

```
ephone 1
```

```
button 1o11,12,13,20,21,22,23,24,25,26,27,28 2x1 3x1
```

```
ephone 2
```

```
button 1o14,15,16,20,21,22,23,24,25,26,27,28 2x1 3x1
```

```
ephone 3
```

```
button 1o17,18,19,20,21,22,23,24,25,26,27,28 2x1 3x1
```

##### Example for
                                 	 Called-Name Display for Voice Hunt Group

The Called-Name
                                       		  Display feature supports the display of the name associated with a called
                                       		  number for incoming calls to IP phones configured on Unified CME. For an
                                       		  example of Called-Name Display for Voice Hunt Group calls, see Example for Called-Name Display for Voice Hunt Group .

##### Example for Called
                                 	 Directory Name Display for Overlaid Ephone-dns

The following
                                       		  example demonstrates the display of a directory name for a called ephone-dn
                                       		  that is part of an overlaid ephone-dn set. For configuration information, see Directory Services .

This configuration
                                       		  of overlaid ephone-dns uses wildcards in the secondary numbers for the
                                       		  ephone-dns. Wildcards allow you to control the display according to the number
                                       		  that was dialed. The example is for a medical answering service with three IP
                                       		  phones that accept calls for nine doctors on one button. When a call to 5550101
                                       		  rings on button 1 on phone 1 to phone 3, “doctor1” is displayed on all three
                                       		  phones.

```
telephony-service
```

```
service dnis dir-lookup
```

```
directory entry 1 5550101 name doctor1
```

```
directory entry 2 5550102 name doctor2
```

```
directory entry 3 5550103 name doctor3
```

```
directory entry 4 5550110 name doctor4
```

```
directory entry 5 5550111 name doctor5
```

```
directory entry 6 5550112 name doctor6
```

```
directory entry 7 5550120 name doctor7
```

```
directory entry 8 5550121 name doctor8
```

```
directory entry 9 5550122 name doctor9
```

```
ephone-dn 1
```

```
number 5500 secondary 555000.
```

```
ephone-dn 2
```

```
number 5501 secondary 555001.
```

```
ephone-dn 3
```

```
number 5502 secondary 555002.
```

```
ephone 1
```

```
button 1o1,2,3
```

```
mac-address 1111.1111.1111
```

```
ephone 2
```

```
button 1o1,2,3
```

```
mac-address 2222.2222.2222
```

```
ephone 3
```

```
button 1o1,2,3
```

```
mac-address 3333.3333.3333
```

The following
                                       		  example shows a hunt-group configuration for a medical answering service with
                                       		  two phones and four doctors. Each phone has two buttons, and each button is
                                       		  assigned two doctors’ numbers. When a patient calls 5550341, Cisco Unified CME
                                       		  matches the hunt-group pilot secondary number (555....), rings button 1 on one
                                       		  of the two phones, and displays “doctor1.” For more information about
                                       		  hunt-group behavior, see Hunt Groups .
                                       		  Note that wildcards are used only in secondary numbers and cannot be used with
                                       		  primary numbers.

```
telephony-service
```

```
service dnis dir-lookup
```

```
max-redirect 20
```

```
directory entry 1 5550341 name doctor1
```

```
directory entry 2 5550772 name doctor1
```

```
directory entry 3 5550263 name doctor3
```

```
directory entry 4 5550150 name doctor4
```

```
ephone-dn 1
```

```
number 1001
```

```
ephone-dn 2
```

```
number 1002
```

```
ephone-dn 3
```

```
number 1003
```

```
ephone-dn 4
```

```
number 104
```

```
ephone 1
```

```
button 1o1,2
```

```
button 2o3,4
```

```
mac-address 1111.1111.1111
```

```
ephone 2
```

```
button 1o1,2
```

```
button 2o3,4
```

```
mac-address 2222.2222.2222
```

```
ephone-hunt 1 peer
```

```
pilot 5100 secondary 555....
```

```
list 1001, 1002, 1003, 1004
```

```
final number 5556000
```

```
hops 5
```

```
preference 1
```

```
timeout 20
```

```
no-reg
```

##### Example for Called
                                 	 Ephone-dn Name Display for Overlaid Ephone-dns

The following
                                       		  example demonstrates the display of the name assigned to the called ephone-dn
                                       		  using the name command.
                                       		  For information about configuring this feature, see Directory Services .

In this example,
                                       		  three phones have button 1 assigned to pick up three shared 800 numbers for
                                       		  three different catalogs.

The default
                                       		  display for the phones is the number of the first ephone-dn listed in the
                                       		  overlay set (18005550100). A call is made to the first ephone-dn (18005550100),
                                       		  and the caller ID (for example, 4085550123) is visible on all phones. The user
                                       		  for phone 1 answers the call. The caller ID (4085550123) remains visible on
                                       		  phone 1, and the displays on phone 2 and phone 3 return to the default display
                                       		  (18005550100). A call to the second ephone-dn (18005550101) is made. The
                                       		  default display on phone 2 and phone 3 is replaced with the called ephone-dn's
                                       		  name (catalog1) and number (18005550101).

```
telephony-service
```

```
service dnis overlay
```

```
ephone-dn 1
```

```
number 18005550100
```

```
ephone-dn 2
```

```
name catalog1
```

```
number 18005550101
```

```
ephone-dn 3
```

```
name catalog2
```

```
number 18005550102
```

```
ephone-dn 4
```

```
name catalog3
```

```
number 18005550103
```

```
ephone 1
```

```
button 1o1,2,3,4
```

```
ephone 2
```

```
button 1o1,2,3,4
```

```
ephone 3
```

```
button 1o1,2,3,4
```

##### Example for OOD-R

```
voice register global
mode cme
source-address 11.1.1.2 port 5060
load 7971 SIP70.8-0-1-11S
load 7970 SIP70.8-0-1-11S
load 7961GE SIP41.8-0-1-0DEV
load 7961 SIP41.8-0-1-0DEV
authenticate ood-refer
authenticate credential 1 tftp://172.18.207.15/labtest/cred1.csv
create profile sync 0004550081249644
...
sip-ua
authentication username
```

## Where to Go
                        	 Next

Dial-Peer Call Hunt and Hunt Groups

Dial peers other than ephone-dn dial peers can be directly configured as hunt groups or rotary groups, in which multiple dial
                           peers can match incoming calls. (These are not the same as Cisco Unified CME ephone hunt groups.) For more information, see
                           the “Hunt Groups” section of the Dial Peers Features and Configuration chapter of Dial Peer Configuration on Voice Gateway Routers .

Called-Name Display

This feature allows
                           		you to specify that the name of the called party, rather than the number,
                           		should be displayed for incoming calls. This feature is very helpful for agents
                           		answering calls for multiple ephone-dns that appear on a single line button in
                           		an ephone-dn overlay set. For more information, see Directory Services .

Soft Key Control

If the hunt-group
                                 			 logout command is used with the HLog keyword,
                           		the HLog soft key appears on phones during the idle, connected, and seized call
                           		states. The HLog soft key is used to toggle an agent from the ready to
                           		not-ready status or from the not-ready to ready status. To move or remove the
                           		HLog soft key on one or more phones, create and apply an ephone template that
                           		contains the appropriate softkeys commands.

From Unified CME
                           		Release 11.6 onwards, HLog keyword is supported with the hunt-group
                                 			 logout command configured under telephony service. On SIP phone,
                           		HLog softkey appears on phone for idle, ringIn, and connected state.

For more
                           		information, see Customize Softkeys .

Feature Access Codes (FACs)

Dynamic membership
                           		allows agents at authorized ephones to join or leave a hunt group using a
                           		feature access code (FAC) after standard or custom FACs are enabled.

In Cisco Unified CME
                           		4.0 and later versions, you can activate call pickup using a feature access
                           		code (FAC) instead of a soft key when standard or custom FACs have been enabled
                           		for your system. The following are the standard FACs for call pickup:

Pickup
                                 			 group—Dial the FAC and a pickup group number to pick up a ringing call in a
                                 			 different pickup group than yours. Standard FAC is **4.

Pickup
                                 			 local—Dial the FAC to pick up a ringing call in your pickup group. Standard FAC
                                 			 is **3.

Pickup
                                 			 direct—Dial the FAC and the extension number to pick up a ringing call at any
                                 			 extension. Standard FAC is **5.

For more information
                           		about FACs, see Feature Access Codes .

Controlling Use of the Pickup Soft Keys

To block the
                           		functioning of the group pickup (GPickUp) or local pickup (Pickup) soft key
                           		without removing the key display, create and apply an ephone template that
                           		contains the features
                                 			 blocked command. For more information, see Configure Call Blocking .

To remove the group
                           		pickup (GPickUp) or local pickup (Pickup) soft key from one or more phones,
                           		create and apply an ephone template that contains the appropriate softkeys command. For more information, see Customize Softkeys .

Ephone-dn Templates

The ephone-hunt
                                 			 login command authorizes an ephone-dn to dynamically join and
                           		leave an ephone hunt group. It can be included in an ephone-dn template that is
                           		applied to one or more individual ephone-dns. For more information, see Templates .

Ephone Hunt Group Statistics Reports

Several different
                           		types of statistics can help you track whether your current ephone hunt groups
                           		are meeting your call coverage needs. These statistics can be displayed
                           		on-screen or written to files.

For more information, see the Cisco Unified CME Basic Automatic Call Distribution and Auto-Attendant Service chapter in Cisco Unified CME B-ACD and Tcl Call-Handling Applications .

Voice Hunt Group Statistics Reports

The hunt-group statistics
                                 			 write-all command writes all the ephone and voice hunt group
                           		statistics to a file.

The hunt-group statistics
                                 			 write-v2 command writes all the ephone and voice hunt group
                           		statistics to a file, along with total logged in and logged out time for
                           		agents.

The statistics
                                 			 collect command enables the collection of call statistics for a
                           		voice hunt group.

The show telephony-service
                                 			 all command displays the total number of ephone and voice hunt
                           		groups that have statistics collection turned on.

The show voice hunt-group
                                 			 statistics command displays call statistics from voice hunt
                           		groups.

For more information, see Cisco Unified Communications Manager Express Command Reference .

Do Not Disturb

The Do Not Disturb
                           		(DND) feature can be used as an alternative to the HLog function for preventing
                           		incoming calls from ringing on a phone. The difference is that HLog prevents
                           		only hunt group calls from ringing, while DND prevents all calls from ringing.
                           		For more information, see Do Not Disturb .

Automatic Call Forwarding During Night-Service

To have an ephone-dn forward all its calls automatically during night-service hours, use the call-forward night-service command. For more information, see Enable Call Forwarding for a Directory Number .

Ephone Templates

The night-service
                                 			 bell command specifies that a phone will receive night-service
                           		notification when calls are received at ephone-dns configured as night-service
                           		ephone-dns. This command can be included in an ephone template that is applied
                           		to one or more individual ephones.

For more
                           		information, see Templates .

## Feature
                        	 Information for Call Coverage Features

The following
                           		table provides release information about the feature or features described in
                           		this module. This table lists only the software release that introduced support
                           		for a given feature in a given software release train. Unless noted otherwise,
                           		subsequent releases of that software release train also support that feature.

Use Cisco Feature
                           		Navigator to find information about platform support and Cisco software image
                           		support. To access Cisco Feature Navigator, go to www.cisco.com/go/cfn .
                           		An account on Cisco.com is not required.

Feature Name

Cisco
                                          				  Unified CME version

Modification

Call Hunt

3.4

Added
                                          				  support for configuring call hunt features on SIP IP phones connected directly
                                          				  to Cisco Unified CME.

3.0

Preference for secondary numbers was introduced.

Huntstop
                                                						was introduced.

1.0

Ephone-dn dial-peer preference was introduced.

Huntstop
                                                						was introduced.

Call Pickup

7.1

Added Call
                                          				  Pickup support for SIP phones.

4.0

The
                                                						ability to globally disable directed call pickup was introduced.

Feature
                                                						access codes for call pickup were introduced.

The
                                                						ability to block call pickup on individual phones was introduced.

3.2

The ability
                                          				  to remove or rearrange soft keys on individual phones was introduced.

3.0

Call pickup
                                          				  groups were introduced.

Call Waiting

8.0

Added Cancel
                                          				  Call Waiting feature.

3.4

Added
                                          				  support for configuring call waiting for SIP phones directly connected to Cisco
                                          				  Unified CME.

Callback
                                          				  Busy Subscriber

3.0

Callback
                                          				  busy subscriber was introduced.

Hunt Groups

12.2

Introduced support for Shared Lines and Mixed Shared Lines (SIP and SCCP
                                          				  phones) on Parallel, Sequential, Peer, and Longest Idle Voice Hunt Groups.

7.0/4.3

Added
                                          				  support for the following:

SCCP
                                                						phones in Voice Hunt-Groups

Call
                                                						Forwarding to a Parallel Voice Hunt-Group (Blast Hunt Group)

Call
                                                						Transfer to a Voice Hunt-Group

Member
                                                						of Voice Hunt-Group can be a SCCP phone, FXS analog phone, DS0-group,
                                                						PRI-group, SIP phone, or SIP trunk

Hunt
                                          				  Groups

4.0

Added
                                          				  support for the following on IP phones running SCCP:

Maximum number of hunt groups in a system was increased from 20
                                                						to 100 and maximum number of agents in a hunt group was increased from 10 to
                                                						20.

Maximum number of hops automatically adjusts to the number of
                                                						agents.

A
                                                						description can be added to phone displays and configuration output to provide
                                                						hunt group information associated with ringing and answered calls.

A
                                                						configurable message can be displayed on agent phones when all agents are in
                                                						the not-ready status to advise the destination to which calls are being
                                                						forwarded or other useful information.

No-answer timeouts can be set individually for each ephone-dn in
                                                						the list and a cumulative no-answer timeout can be set for all ephone-dns.

Automatic logout trigger criterion was changed from exceeding
                                                						the specified timeout to exceeding the specified number of calls. The name of
                                                						this feature was changed from automatic logout to automatic agent status
                                                						not-ready.

Dynamic hunt group membership is introduced. Agents can join and
                                                						leave hunt groups whenever a wildcard slot is available.

Agent
                                                						status control using an HLog soft key or feature access code (FAC) is
                                                						introduced. Agents can put their lines into not-ready state to temporarily
                                                						block hunt group calls without relinquishing their slots in group.

Calls
                                                						can be blocked from agent phones that are not idle or on hook.

Calls
                                                						that are not answered by the hunt group can be returned to the party who
                                                						transferred them into the huntgroup.

Calls
                                                						parked by hunt group agents can be returned to a different entry point.

(Sequential hunt groups only) Local calls to a hunt group can be
                                                						restricted so that they will not be forwarded past the initial agent that is
                                                						rung.

(Longest-idle
                                                						hunt groups only) A new command, the from-ring command, specifies that on-hook time stamps should be updated when a call rings
                                                						an agent and when a call is answered by an agent.

3.4

Added
                                          				  support for configuring hunt groups for SIP phones directly connected to Cisco
                                          				  Unified CME.

3.2.1

Maximum number of hunt groups in a system was increased to 20.

Automatic logout capability was introduced.

3.2

Longest-idle hunt groups were introduced.

3.1

Secondary
                                          				  pilot numbers were introduced.

3.0

Peer and
                                          				  sequential ephone hunt groups were introduced.

Night
                                          				  Service

11.6

Night
                                          				  service support for mixed deployment of SIP and SCCP phone was introduced.

11.5

Night
                                          				  service support for SIP phone was introduced.

4.0

The night-service
                                                						everyday , night-service weekday , and night-service weekend commands were introduced.

3.3

The
                                          				  behavior of the night-service code was changed. Previously, using the
                                          				  night-service code at a phone either enabled or disabled night service for the
                                          				  ephone-dns on that phone. Now, using the night-service code at a phone enables
                                          				  or disables night service for all night-service ephone-dns.

3.0

Night
                                          				  service was introduced.

4.0

The
                                                						number of ephone-dns that can be overlaid on a single button using the button command and the o or c keyword was increased from 10 to 25.

The
                                                						ability to extend calls for overlaid ephone-dns to other buttons (rollover
                                                						buttons) on the same phone was introduced. Rollover buttons are created by
                                                						using the x keyword with the button command.

The
                                                						number of waiting calls that can be displayed for overlaid ephone-dns that have
                                                						call waiting configured has been increased to six for the following phone
                                                						types: Cisco Unified IP Phone 7940G, 7941G, 7941G-GE, 7960G, 7961G, 7961G-GE,
                                                						7970G, and 7971G-GE.

3.2.1

Call
                                          				  waiting for overlaid ephone-dns was introduced and the c keyword was added to
                                          				  the button command.

3.0

Overlaid
                                          				  ephone-dns were introduced and the o keyword was added to the button command.

All Agents
                                          				  Logged Out Message for VHG Phones

12.2

Introduced
                                          				  support for all agents logged out display message for Cisco IP Phone 8800
                                          				  Series on Cisco 4000 Series Integrated Services Routers.

Agent
                                          				  Status Control

12.2

Agent
                                          				  Status Control enhancements was supported.

Voice Hunt
                                          				  Group Enhancements

11.6

Hlog
                                          				  Softkey support for SIP Phones was introduced.

9.0

Allows all
                                          				  ephone and voice hunt group call statistics to be written to a file using the hunt-group statistics
                                                						write-all command.

Preventing
                                          				  Local-Call Forwarding to Final Agent in Voice Hunt Groups

9.5

The no forward
                                                						local-calls command was introduced in ephone-hunt group to
                                          				  prevent a local call from being forwarded to the next agent.

Enhancement of Support for Hunt Group

9.5

Hunt group
                                          				  agent statistics of Cisco Unified SCCP IP phones is enhanced to include Total
                                          				  logged in time and Total logged out.

Total
                                          				  Logged in and Logged out Time Statistics for agent

9.5

Allows all
                                          				  ephone hunt call statistics to be written to a file along with total logged in
                                          				  and logged out time for agents using the hunt-group statistics
                                                						write-v2 command.

Enhancement of Support for Total Logged in and Logged out Time
                                          				  Statistics for Agent

11.5

Allows all
                                          				  voice hunt call statistics to be written to a file along with total logged in
                                          				  and logged out time for agents using the hunt-group statistics
                                                						write-v2 command.

Out-of-Dialog Refer

4.1

Out-of
                                          				  Dialog REFER support was added.

| Feature | Description | Example | How Configured |
|---|---|---|---|
| Call Forwarding | Calls are automatically diverted to a designated number on busy, no answer, all calls, or only during night-service hours. | Extension 3444 is configured to send calls to extension 3555 when it is busy or does not answer. | Enable Call Forwarding for a Directory Number or Configure SIP-to-SIP Phone Call Forwarding |
| Call Hunt | System automatically searches for an available directory number from a matching group of directory numbers until the call
                                          is answered or the hunt is stopped. | Three ephone-dns have the same extension number, 755. One is on the manager’s phone and the others are on the assistants’
                                          phones. Preference and huntstop are used to make sure that calls always come to the manager’s phone first but if they can’t
                                          be answered, they will ring on the first assistant’s phone and if not answered, on the second assistant’s phone. | Configure Call Hunt on SCCP Phones or Configure Call Hunt on SIP Phones |
| Call Pickup | Calls to unstaffed phones can be answered by other phone users using a soft key or by dialing a short code. | Extension 201 and 202 are both in pickup group 22. A call is received by 201, but no one is there to answer. The agent at
                                          202 presses the GPickUp soft key to answer the call. | Enable Call Pickup |
| Call Waiting | Calls to busy numbers are presented to phone users, giving them the option to answer them or let them be forwarded. | Extension 564 is in conversation when a call-waiting beep is heard. The phone display shows the call is from extension 568
                                          and the phone user decides to let the call go to voice mail. | Configure Call-Waiting Indicator Tone on SCCP Phone or Enable Call Waiting on SIP Phones |
| Cisco CME B-ACD | Calls to a pilot number are automatically answered by an interactive application that presents callers with a menu of choices
                                          before sending them to a queue for a hunt group. | The DID number 555-0125 is the pilot number for the XYZ Company. Incoming calls to this pilot number hear a menu of choices;
                                          they can press 1 for sales, 2 for service, or 3 to leave a message. The call is forwarded appropriately when callers make
                                          a choice. | See Cisco Unified CME B-ACD and Tcl Call-Handling Applications. |
| Hunt Groups | Calls are forwarded through a pool of agents until answered or sent to a final number. | Extension 200 is a pilot number for the sales department. Extensions 213, 214, and 215 belong to sales agents in the hunt
                                          group. When a call to extension 200 is received, it proceeds through the list of agents until one answers. If all the agents
                                          are busy or do not answer, the call is sent to voice mail. | Configure Ephone-Hunt Groups on SCCP Phones or Configure Voice-Hunt Groups |
| Night Service | Calls to ephone-dns and voice register dns that are not staffed during certain hours can be answered by other phones using
                                          call pickup. | Extension 7544 is the cashier’s desk but the cashier only works until 3 p.m. A call is received at 4:30 p.m. and the service
                                          manager’s phone is notified. The service manager uses call pickup to answer the call. | Configure Night Service on SCCP Phones Configure Night Service on SIP Phones |
| Overlaid Ephone-dns | Calls to several numbers can be answered by a single agent or multiple agents. | Extensions 451, 452, and 453 all appear on button 1 of a phone. A call to any of these numbers can be answered from button
                                          1. | Configure Overlaid Ephone-dns on SCCP Phones . |

| Note | SIP phones only
                                          		  support local pickup and group pickup. Directed call pickup is not supported. |
|---|---|

| Ephone-dn 1
                                                				  Configuration | Ephone-dn 2
                                                				  Configuration | Active Call
                                                				  on DN | Incoming
                                                				  Call on DN | Expected
                                                				  Behavior |
|---|---|---|---|---|
| — | no call-waiting beep | DN 1 | DN 2 | No beep |
| no call-waiting beep | — | DN 1 | DN 2 | No beep |
| — | no call-waiting beep generate | DN 1 | DN 2 | No beep |
| — | no call-waiting beep accept | DN 1 | DN 2 | Beep |
| — | no call-waiting beep accept no call-waiting beep generate | DN 1 | DN 2 | No beep |
| no call-waiting beep | — | DN 1 | DN 1 | No beep |
| no call-waiting beep generate | — | DN 1 | DN 1 | No beep |
| no call-waiting beep accept | — | DN 1 | DN 1 | No beep |
| no call-waiting beep accept no call-waiting beep generate | — | DN 1 | DN 1 | No beep |
| no call-waiting beep generate | — | DN 1 | DN 2 | Beep |
| no call-waiting beep accept | — | DN 1 | DN 2 | No beep |
| — | no call-waiting beep | DN 1 | DN 1 | Beep |

| Note | For Unified CME B-ACD, the final destination for voice hunt groups is determined by the B-ACD service. |
|---|---|

| Feature | Ephone Hunt | Voice Hunt
                                                				  Group |
|---|---|---|
| Endpoints
                                                				  Supported | SCCP only | SIP, SCCP,
                                                				  PSTN, and FXS |
| Parallel
                                                				  Hunt Groups (Call Blast) | No (for
                                                				  alternative, see Shared- Line Overlays | Yes |
| Hunt
                                                				  Statistics Support | Yes | Yes |
| B-ACD
                                                				  Support | Yes | Yes |
| Shared Line | Yes | Yes |
| Features
                                                				  such as present-call and login/logout | Yes | Yes (Only
                                                				  for SIP and SCCP phones) |

| Note | Consecutive numbers of the same phone cannot be members of a
                                             		  Sequential Voice Hunt Group when present call idle state (configured using the
                                             		  CLI command present-call idle-phone ) is set to true. The
                                             		  limitation applies to both SIP and SCCP phones. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone phone-tag Example: Router(config)# ephone 12 | Enters ephone
                                             				configuration mode. phone-tag —Unique number
                                                				  that identifies this ephone during configuration tasks. |
| Step 4 | phone-ui voice-hunt-groups Example: Router(config-ephone)# phone-ui voice-hunt-groups | Enables a SCCP
                                             				phone user to view information related to voice hunt groups and also join or
                                             				unjoin from voice hunt groups. This command is enabled by
                                                				  default. |
| Step 5 | end Example: Router(config-ephone)# end | Exits to
                                             				privileged EXEC mode. |

| Note | From Cisco Unified CME Release 10.5 onwards, SIP phones will
                                          		  display voice hunt group information, by default. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone template template-tag Example: Router(config)# ephone template 5 | Enters
                                             				ephone-template configuration mode to create an ephone template. template-tag —Unique identifier for the ephone template that
                                                   					 is being created. Range: 1 to 10. |
| Step 4 | url-button index type \| url [ name ] Example: Router#(config-ephone-template)#url-button 1 myphoneapp
Router(config-ephone-template)#url-button 2 em
Router(config-ephone-template)#url-button 3 snr
Router(config-ephone-template)#url-button 4 voicehuntgroups
Router(config-ephone-template)#url-button 5 park-list
Router(config-ephone-template)#url-button 6 http://www.cisco.com | Configures a
                                             				service URL feature button on a line key. Index —Unique index number. Range: 1 to 8. type —Type of service PLK button. The following
                                                   					 types of URL service buttons are available: myphoneapp: My phone application configured under phone user
                                                         						  interface. em:
                                                         						  Extension Mobility snr:
                                                         						  Single Number Reach voicehuntgroups: Voice Hunt Groups Information park-list: Parked calls url name —Service URL with maximum length of 31
                                                   					 characters. |
| Step 5 | exit Example: Router(config-ephone-template)# exit | Exits
                                             				ephone-template configuration mode. |
| Step 6 | ephone phone-tag Example: Router(config)#ephone 36 | Enters ephone
                                             				configuration mode. phone-tag —Unique sequence number that identifies
                                                   					 this ephone during configuration tasks. |
| Step 7 | ephone-template template-tag Example: Router(config-ephone)# ephone-template 5 | Applies an
                                             				ephone template to the ephone that is being configured. |
| Step 8 | end Example: Router(config-ephone)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register template template-tag Example: Router(config)# voice register template 5 | Enters
                                             				ephone-template configuration mode to create an ephone template. template-tag —Unique
                                                				  identifier for the ephone template that is being created. Range: 1 to 10. |
| Step 4 | url-button [ index number ] [ url location ] [ label ] Example: Router(config-register-temp)url-button 1 http://x.x.x.x:80/CMEserverForPhone/vhg_root_menu VHG_List Router(config-register-temp)url-button 2 http://x.x.x.x:80/CMEserverForPhone/park_list Park_List | Configures a
                                             				service url feature button on a line key. x.x.x.x—CME IP address. Index
                                                   					 number—Unique index number ranging from 1 to 8. URL location —Location of the URL. label—A
                                                   					 label name which is displayed on phone. |
| Step 5 | exit Example: Router(config-register-temp)# exit | Exits
                                             				ephone-template configuration mode. |
| Step 6 | voice register pool phone-tag Example: Router(config)# voice register pool 12 | Enters ephone
                                             				configuration mode. phone-tag —Unique number that identifies this ephone during
                                                   					 configuration tasks. |
| Step 7 | template template-tag Example: Router(config-register-pool)# template 5 | Applies the
                                             				ephone template to the phone. template-tag —Unique identifier of the template
                                                   					 that you created in Step 3. |
| Step 8 | end Example: Router(config-register-pool)# end | Returns to
                                             				privileged EXEC mode. |

| Note | Use quotes (")
                                          		when input strings have spaces in between as shown in the next three examples. |
|---|---|

| Restriction | Display support applies to Cisco Unified SCCP IP phones in voice hunt-group and ephone-hunt configuration modes but are not
                                                   supported in Cisco Unified SIP IP phones. Called name and called number information displayed on the caller’s phone follows existing behavior, where the called names
                                                   and called numbers are updated so that a sequential hunt reflects the name and number of the ringing phone. |
|---|---|

| Restriction | Statistics collection for Cisco Unified SCCP and SIP IP phones in Cisco Unified SRST are not supported. |
|---|---|

| Comparison Factor | Dynamic Membership | Agent Status Control | Automatic Agent Status Not-Ready |
|---|---|---|---|
| Purpose | Allows an authorized agent to join and leave hunt groups. | Allows an agent to manually activate a toggle to temporarily enter a not-ready state, in which hunt-group calls bypass the
                                             agent’s phone. | Automatically puts an agent’s phone in a not-ready state after a specified number of hunt-group calls are unanswered by the
                                             agent’s phone. |
| Example | Agent A joins a hunt group at 8 a.m. and takes calls until 1 p.m., when he leaves the hunt group. While Agent A is a member
                                             of the hunt group, he occupies one of the wildcard slots in the list of numbers configured for the hunt group. At 1 p.m.,
                                             Agent B joins the hunt group using the same wildcard slot that Agent A relinquished when he left. | Agent A takes a coffee break at 10 a.m. and puts his phone into a not-ready status while he is on break. When he returns he
                                             puts his phone back into the ready status and immediately starts receiving hunt-group calls again. He retained his wildcard
                                             slot while he was in the not-ready status. | Agent B is suddenly called away from her desk before she can manually put her phone into the not-ready status. After a hunt-group
                                             call is unanswered at Agent B’s phone, the phone is automatically placed in the not-ready status and it is not presented with
                                             further hunt-group calls. When Agent B returns, she manually puts her phone back into the ready status. |
| Hunt-group slot availability | An agent joining a hunt group occupies a wildcard slot in the hunt group list. An agent leaving the group relinquishes the
                                             slot, which becomes available for another agent. | An agent who enters the not-ready state does not give up a slot in the hunt group. The agent continues to occupy the slot
                                             regardless of whether the agent is in the not-ready status. | An agent who enters the not-ready does not give up a slot in the hunt group. The agent continues to occupy the slot regardless
                                             of whether the agent is in the not-ready status. |
| Agent activation method | An authorized agent uses a feature access code (FAC) to join a hunt group and a different FAC to leave the hunt group. | An agent uses the HLog soft key to toggle agent status between ready and not ready. Agents can also use the HLog FAC to toggle
                                             between ready and not-ready if FACs are enabled. If the HLog soft key is not enabled, the DND soft key can be used to put an agent in the not-ready status and the agent will
                                             not receive any calls. | An agent who is a member of a hunt group configured with the auto logout command does not answer the specified number of calls, and the agent’s phone is automatically changed to the not-ready status.
                                             The agent uses the HLog soft key or a FAC to return to the ready status. If the HLog soft key or FAC has not been enabled in the configuration, the agent uses the DND soft key to return to the ready
                                             status. |
| Configuration | The system administrator uses the list command to configure up to 20 wildcard slots in a hunt group and uses the ephone-hunt login command to authorize certain directory numbers to use these wildcard slots. See Configure Ephone-Hunt Groups on SCCP Phones . | The system administrator uses the HLog keyword with the hunt-group logout command to provide an HLog soft key on display phones and uses the fac command to enable standard FACs or create a custom FAC. See Configure Ephone-Hunt Groups on SCCP Phones . | The system administrator uses the auto logout command to enable automatic agent status not-ready for a hunt group. This functionality is disabled by default. See Configure Ephone-Hunt Groups on SCCP Phones . See Configure Voice-Hunt Groups . |
| Optional customizations | The system administrator can establish custom FACs for agents to use to enter or leave a hunt group. | The system administrator can use the softkeys commands to change the position or prevent the display of the HLog soft key on individual phones. | The system administrator can use the auto logout command to specify the number of unanswered calls that will trigger an agent status change to not-ready and whether this feature
                                             applies to dynamic hunt-group members, static hunt-group members, or both. The system administrator can use the hunt-group logout command to specify whether an automatic change to the not-ready status also places a phone in DND mode. |

| Note | The Dynamic
                                          		Membership feature is different from the Agent Status Control feature and the
                                          		Automatic Agent Status Not-Ready feature. Table 1 compares the features. |
|---|---|

| Note | The Agent Status
                                          		Control feature is different from the Dynamic Membership feature and the
                                          		Automatic Agent Status Not-Ready feature. Table 1 compares the features. |
|---|---|

| Note | From Cisco Unified
                                             		  CME Release 11.6 onwards, line level logout or login using FAC *4 is not
                                             		  supported for SIP phones (only supported on SCCP phones). SIP phones only
                                             		  support phone level logout or login using FAC *5. |
|---|---|

| Note | The Agent Status
                                          		Control feature is different from the Dynamic Membership feature and the
                                          		Automatic Agent Status Not-Ready feature. Table 1 compares the features. |
|---|---|

| Note | The Automatic
                                          		Agent Status Not-Ready feature is different from the Dynamic Membership feature
                                          		and the Agent Status Control feature. Table 1 compares the features. |
|---|---|

| Note | The Automatic
                                          		Agent Status Not-Ready feature is different from the Dynamic Membership feature
                                          		and the Agent Status Control feature. Table 1 compares the features. |
|---|---|

| Note | To continue or to
                                          		  stop the search for ephone-dns, you must use, respectively, the no huntstop and huntstop commands under the individual ephone-dns. The huntstop setting is applied only
                                          		  to the dial peers affected by the ephone-dn command in telephony-service mode. Dial peers
                                          		  configured in global configuration mode comply with the global configuration
                                          		  huntstop setting. |
|---|---|

| Note | Ephone-dns accept
                                             		  call interruptions, such as call waiting, by default. For call waiting to work,
                                             		  the default must be active. For more information, see Configure Call-Waiting Indicator Tone on SCCP Phone . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-dn dn-tag [ dual-line ] Example: Router(config)# ephone-dn 20 dual-line | Enters
                                             				ephone-dn configuration mode for the purpose of configuring a directory number. |
| Step 4 | number number [ secondary number ] [ no-reg [ both \| primary ] ] Example: Router(config-ephone-dn)# number 101 | Associates a
                                             				telephone or extension number with the directory number. Assign the
                                                   					 same number to several primary or secondary ephone-dns to create a group of
                                                   					 virtual dial peers through which the incoming called number must search. |
| Step 5 | preference preference-order [ secondary secondary-order ] Example: Router(config-ephone-dn)# preference 2 | Sets the preference value for the ephone-dn. Default: 0. Increment the preference order for subsequent ephone-dns with the same number. That is, the first directory number is preference 0 by default and you must specify 1 for the second ephone-dn with the same number, 2 for the next, and so on. secondary secondary-order —(Optional) Preference value for the secondary number of an ephone-dn. Default is 9. |
| Step 6 | no huntstop or huntstop Example: Router(config-ephone-dn)# no huntstop or Router(config-ephone-dn)# huntstop | Explicitly
                                             				enables call hunting behavior for a directory number. Configure no huntstop for all ephone-dns, except the final ephone-dn, within a set of ephone-dns with
                                                   					 the same number. Configure the huntstop command for the final ephone-dn within a set of ephone-dns with the same
                                                   					 number. |
| Step 7 | huntstop channel Example: Router(config-ephone-dn)# huntstop channel | (Optional)
                                             				Enables channel huntstop, which keeps a call from hunting to the next channel
                                             				of a directory number if the first channel is busy or does not answer. Required
                                                   					 for dual-line ephone-dns that are used for call hunting. |
| Step 8 | end Example: Router(config-ephone-dn)# end |  |

| Step 1 | show running-config This command
                                             				displays your configuration. Preference and huntstop information is listed in
                                             				the ephone-dn portion of the output. Router# show running-config ephone-dn  2  dual-line number 126 description FrontDesk name Receptionist preference 1 call-forward busy 500 huntstop channel no huntstop |
|---|---|
| Step 2 | show telephony-service ephone-dn This command
                                             				displays ephone-dn preference and huntstop configuration information. |
| Step 3 | show telephony-service
                                                				  all or show
                                                				  telephony-service dial-peer These commands
                                             				display preference and huntstop configurations for ephone-dn dial peers. Router# show telephony-service dial-peer ! dial-peer voice 20026 pots destination-pattern 5002 huntstop call-forward noan 5001 timeout 45 port 50/0/2 |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register dn dn-tag Example: Router(config)# voice register dn 1 | Enters voice
                                             				register dn configuration mode to define a directory number for a SIP phone,
                                             				intercom line, voice port, or an MWI. |
| Step 4 | number number Example: Router(config-register-dn)# number 5001 | Associates a
                                             				phone number with the directory number. Assign the
                                                   					 same number to several directory numbers to create a group of virtual dial
                                                   					 peers through which the incoming called number must search. |
| Step 5 | preference preference-order Example: Router(config-register-dn)# preference 4 | Creates the
                                             				preference order for matching the VoIP dial peers created for the number
                                             				associated with this directory number to establish the hunt strategy for
                                             				incoming calls. Default is
                                                   					 0, which is the highest preference. |
| Step 6 | huntstop Example: Router(config-register-dn)# huntstop | Disables
                                             				call-hunting behavior for an extension on a SIP phone. |
| Step 7 | end Example: Router(config-register-dn)# end | Exits
                                             				configuration mode and enters privileged EXEC mode. |

| Restriction | SIP phones
                                                   				  that do not support the PickUp and GpickUp soft keys must use feature access
                                                   				  codes (FACs) to access these features. Different
                                                   				  directory numbers with the same extension number must have the same Pickup
                                                   				  configuration. A directory
                                                   				  number can be assigned to only one pickup group. Pickup group
                                                   				  numbers can vary in length, but must have unique leading digits. For example,
                                                   				  if you configure group number 17, you cannot also configure group number 177.
                                                   				  Otherwise a pickup in group 17 is always triggered before the user can enter
                                                   				  the final 7 for 177. Calls from
                                                   				  H.323 trunks are not supported on SIP phones. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 4 | call-park system application Example: Router(config-telephony)# call-park system application | Enables or disables Call Pickup functionality using call pickup feature on SIP phones. |
| Step 5 | service directed-pickup [ gpickup ] Example: Router(config-telephony)# service directed-pickup gpickup | Enables Directed Call Pickup and modifies the function of the GPickUp and PickUp soft keys. gpickup —(Optional) Enables using the GPickUp soft key to perform Directed Call Pickup on SCCP phones. This keyword is supported in
                                                   Cisco Unified CME 7.1 and later versions. This command determines the specific soft keys used to access different Call Pickup features on SCCP and SIP phones. For a
                                                   description, see the service directed-pickup command in the Cisco Unified CME Command Reference . |
| Step 6 | fac { standard \| custom pickup { direct \| group \| local } custom-fac } Example: Router(config-telephony)# fac custom pickup group #35 | Enables
                                             				standard FACs or creates a custom FAC or alias for Pickup features on SCCP and
                                             				SIP phones. standard —Enables standard FACs for all phones.
                                                   					 Standard FAC for Park Retrieval is **10. custom —Creates a custom FAC for a feature. custom-fac —User-defined code to dial using the
                                                   					 keypad on an IP or analog phone. Custom FAC can be up to 256 characters and
                                                   					 contain numbers 0 to 9 and * and #. |
| Step 7 | exit Example: Router(config-telephony)# exit | Returns to
                                             				privileged EXEC mode. |
| Step 8 | ephone-dn dn-tag [ dual-line \| octo-line ] or voice register dn dn-tag Example: Router(config)# ephone-dn 20 dual-line or Router(config)# voice register dn 20 | Enters directory number configuration mode. |
| Step 9 | pickup-group group-number Example: Router(config-ephone-dn)# pickup-group 30 or Router(config-register-dn)# pickup-group 30 | Creates a
                                             				pickup group and assigns the directory number to the group. group-number —String of up to 32 characters. Group
                                                   					 numbers can vary in length but must have unique leading digits. For example, if
                                                   					 there is a group number 17, there cannot also be a group number 177. This
                                                   					 command can also be configured in ephone-dn-template configuration mode and
                                                   					 applied to one or more ephone-dns. The ephone-dn configuration has priority
                                                   					 over the template configuration. |
| Step 10 | pickup-call
                                                				  any-group Example: Router(config-ephone-dn)# pickup-call any-group or Router(config-register-dn)# pickup-call any-group | Enables a
                                             				phone user to pickup ringing calls on any extension belonging to a pickup group
                                             				by pressing the GPickUp soft key and asterisk (*). The ringing extension must be configured with a pickup group using the pickup-group command. If this
                                                   					 command is not configured, the user can pickup calls in other groups by
                                                   					 pressing the GPickUp soft key and dialing the pickup group number. |
| Step 11 | end Example: Router(config-ephone-dn)# end or Router(config-register-dn)# end | Exits
                                             				configuration mode. |

| Restriction | The
                                                   				  call-waiting ring option is not supported if the ephone-dn is configured with
                                                   				  the no call-waiting beep
                                                         						accept command. If you
                                                   				  configure a button to have a silent ring, you will not hear a call-waiting beep
                                                   				  or call-waiting ring regardless of whether the ephone-dn associated with the
                                                   				  button is configured to generate a call-waiting beep or call-waiting ring. To
                                                   				  configure a button for silent ring, see Assign Directory Numbers to SCCP Phones . The
                                                   				  call-waiting beep volume cannot be adjusted through Cisco Unified CME for the
                                                   				  Cisco Unified IP Phone 7902G, Cisco Unified IP Phone 7905G, Cisco Unified IP
                                                   				  Phone 7912G, Cisco ATA-186, and Cisco ATA-188. The
                                                   				  call-waiting ring option is not supported on the Cisco Unified IP Phone 7902G,
                                                   				  Cisco Unified IP Phone 7905G, or Cisco Unified IP Phone 7912G. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-dn dn-tag [ dual-line ] Example: Router(config)# ephone-dn 20 dual-line | Enters
                                             				ephone-dn configuration mode, creates an ephone-dn, and optionally assigns it
                                             				dual-line status. |
| Step 4 | call-waiting beep [ accept \| generate ] Example: Router(config-ephone-dn)# no call-waiting beep accept | Enables an
                                             				ephone-dn to generate or accept call-waiting beeps. Default is
                                                   					 directory number both accepts and generates call-waiting beep. The beep
                                                   					 is heard only if the other ephone-dn is configured to accept call-waiting beeps
                                                   					 (default). |
| Step 5 | call-waiting ring Example: Router(config-ephone-dn)# call-waiting ring | (Optional)
                                             				Enables an ephone-dn to use a ring indicator for call-waiting notification. To use
                                                   					 this command, do not disable call-waiting beep by using the no call-waiting beep
                                                         						  accept command. |
| Step 6 | end Example: Router(config-ephone-dn)# end | Returns to
                                             				privileged EXEC mode. |

| Step 1 | Use the show running-config command to verify your
                                             				configuration. Call-waiting settings are listed in the ephone-dn portion of the
                                             				output. If the no call-waiting beep generate and the no call-waiting beep accept commands are configured, the show running-config command output will display the no call-waiting beep command. Example: Router# show running-config ! ephone-dn 3 dual-line number 126 name Accounting preference 2 secondary 9 huntstop huntstop channel call-waiting beep ! |
|---|---|
| Step 2 | Use the show telephony-service ephone-dn command to display call-waiting
                                          			 configuration information. Example: Router# show telephony-service ephone-dn ephone-dn 1 dual-line number 126 secondary 1261 preference 0 secondary 9 no huntstop huntstop channel call-forward busy 500 secondary call-forward noan 500 timeout 10 call-waiting beep |

| Restriction | Call Waiting
                                                   				  must be disabled by pressing the CWOff soft key or using the FAC before placing
                                                   				  a call; it cannot be activated or deactivated during a call. The CWOff
                                                   				  soft key is not available when initiating Call Transfer. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-template template-tag Example: Router(config)# ephone-template 5 | Enters
                                             				ephone-template configuration mode to create an ephone template. template-tag —Unique identifier for the ephone
                                                   					 template. Range: 1 to 20. |
| Step 4 | softkeys seized { [ CallBack ] [ Cfwdall ] [ CWOff ] [ Endcall ] [ Gpickup ] [ HLog ] [ MeetMe ] [ Pickup ] [ Redial ] } Example: Router(config-ephone-template)# softkeys seized CWOff Cfwdall Endcall Redial | (Optional)
                                             				Modifies the order and type of soft keys that display on an IP phone during the
                                             				seized call state. You can
                                                   					 enter any of the keywords in any order. Default is
                                                   					 all soft keys are displayed in alphabetical order. Any soft
                                                   					 key that is not explicitly defined is disabled. |
| Step 5 | exit Example: Router(config-ephone-template)# exit | Exits
                                             				ephone-template configuration mode. |
| Step 6 | ephone phone-tag Example: Router(config)# ephone 12 | Enters
                                             				ephone configuration mode. phone-tag —Unique number that identifies this
                                                				  ephone during configuration tasks. |
| Step 7 | ephone-template template-tag Example: Router(config-ephone)# ephone-template 5 | Applies the
                                             				ephone template to the phone. template-tag —Unique identifier of the ephone
                                                				  template that you created in Step 3 . |
| Step 8 | exit Example: Router(config-ephone)# exit | Exits ephone
                                             				configuration mode. |
| Step 9 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 10 | fac { standard \| custom ccw custom-fac } Example: Router(config-telephony)# fac custom ccw **8 | Enables
                                             				standard FACs or creates a custom FAC or alias. standard —Enables standard FACs for all phones.
                                                   					 Standard FAC for cancel call waiting is *1. custom —Creates a custom FAC for a FAC type. custom-fac —User-defined code to be dialed using
                                                   					 the keypad on an IP or analog phone. Custom FAC can be up to 256 characters
                                                   					 long and contain numbers 0 to  9 and * and #. |
| Step 11 | end Example: Router(config-telephony)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register pool pool-tag Example: Router(config)# voice register pool 3 | Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone in Cisco Unified CME. |
| Step 4 | call-waiting Example: Router(config-register-pool)# call-waiting | Configures
                                             				call waiting on the SIP phone being configured. Note This step
                                                      				is included to illustrate how to enable the command if it was previously
                                                      				disabled. Default: Enabled. | Note | This step
                                                      				is included to illustrate how to enable the command if it was previously
                                                      				disabled. |
| Note | This step
                                                      				is included to illustrate how to enable the command if it was previously
                                                      				disabled. |
| Step 5 | exit Example: Router(config-register-pool)# exit | Exits voice
                                             				register pool configuration mode. |
| Step 6 | voice register
                                                				  global Example: Router(config)# voice register global | Enters voice
                                             				register global configuration mode to set parameters for all supported SIP
                                             				phones in Cisco Unified CME. |
| Step 7 | hold-alert Example: Router(config-register-global)# hold-alert | Sets an audible alert notification when a call is on hold on a SIP phone. Default is disabled. |
| Step 8 | end Example: Router(config-register-global)# end | Exits to
                                             				privileged EXEC mode. |

| Note | This step
                                                      				is included to illustrate how to enable the command if it was previously
                                                      				disabled. |
|---|---|

| Restriction | The HLog
                                                   				  soft key is available only on display phones. It is not available on
                                                   				  Cisco Unified IP Phones 7902, 7905, and 7912; Cisco IP Communicator; and
                                                   				  Cisco VG224. Shared
                                                   				  ephone-dns cannot use the Agent Status Control or Automatic Agent Not-Ready
                                                   				  feature. If directory
                                                   				  numbers that are members of a hunt group are configured for called-name
                                                   				  display, the following restrictions apply: The primary or secondary pilot number must be defined using at least one wildcard character. The phone numbers in the list command cannot contain wildcard characters. If Call Forward All or Call Forward Busy is configured for a hunt group member (directory number), the hunt group ignores
                                                   it. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-hunt hunt-tag { longest-idle \| peer \| sequential } Example: Router(config)# ephone-hunt 23 peer | Enters
                                             				ephone-hunt configuration mode to define an ephone hunt group. hunt-tag —Unique sequence number that identifies this hunt
                                                				  group during configuration tasks. Range: 1 to 100. Cisco CME
                                                   					 3.3 and earlier—Range: 1 to 10 longest-idle —Calls go to the ephone-dn that has been idle
                                                   					 the longest for the number of hops specified when the ephone hunt group was
                                                   					 defined. The longest-idle is determined from the last time that a phone
                                                   					 registered, reregistered, or went on-hook. peer —First ephone-dn to ring is the number to the right of
                                                   					 the ephone-dn that was the last to ring when the pilot number was last called.
                                                   					 Ringing proceeds in a circular manner, left to right, for the number of hops
                                                   					 specified when the ephone hunt group was defined. sequential —Ephone-dns ring in the left-to-right order in
                                                   					 which they are listed when the hunt group is defined. |
| Step 4 | pilot number [ secondary number ] Example: Router(config-ephone-hunt)# pilot 5601 | Defines the
                                             				pilot number, which is the number that callers dial to reach the hunt group. number —E.164 number up to 27 characters. The dialplan
                                                   					 pattern can be applied to the pilot number. secondary —(Optional) Defines an additional pilot number for
                                                   					 the ephone hunt group. |
| Step 5 | list number [ , number ... ] Example: Router(config-ephone-hunt)# list 5001, 5002, 5017, 5028 | Defines the
                                             				list of numbers (from 2 and 20) to which the ephone hunt group redirects the
                                             				incoming calls. number —E.164 number
                                                   					 up to 27 characters. Primary or secondary number assigned to an ephone-dn. |
| Step 6 | final final-number Example: Router(config-ephone-hunt)# final 6000 | Defines the
                                             				last number in the ephone hunt group, after which the call is no longer
                                             				redirected. Can be an ephone-dn primary or secondary number, a voice-mail pilot
                                             				number, a pilot number of another hunt group, or an FXS number. Note When a
                                                      				final number is defined as a pilot number of another hunt group, the pilot
                                                      				number of the first hunt group cannot be configured as a final number in any
                                                      				other hunt group. Note This
                                                      				command is not used for ephone hunt groups that are part of a Cisco Unified CME
                                                      				B-ACD service. The final destination for those groups is determined by the
                                                      				B-ACD service. | Note | When a
                                                      				final number is defined as a pilot number of another hunt group, the pilot
                                                      				number of the first hunt group cannot be configured as a final number in any
                                                      				other hunt group. | Note | This
                                                      				command is not used for ephone hunt groups that are part of a Cisco Unified CME
                                                      				B-ACD service. The final destination for those groups is determined by the
                                                      				B-ACD service. |
| Note | When a
                                                      				final number is defined as a pilot number of another hunt group, the pilot
                                                      				number of the first hunt group cannot be configured as a final number in any
                                                      				other hunt group. |
| Note | This
                                                      				command is not used for ephone hunt groups that are part of a Cisco Unified CME
                                                      				B-ACD service. The final destination for those groups is determined by the
                                                      				B-ACD service. |
| Step 7 | hops number Example: Router(config-ephone-hunt)# hops 7 | (Optional;
                                             				peer and longest-idle hunt groups only) Sets the number of hops before a call
                                             				proceeds to the final number. number —Number of hops
                                                   					 before the call proceeds to the final ephone-dn. Range is 2 to 20, but the
                                                   					 value must be less than or equal to the number of extensions that are specified
                                                   					 in the list command. Default automatically adjusts to the number of
                                                   					 hunt group members. |
| Step 8 | timeout seconds [ , seconds ... ] Example: Router(config-ephone-hunt)# timeout 7, 10, 15 | (Optional)
                                             				Sets the number of seconds after which an unanswered call is redirected to the
                                             				next number in the hunt-group list. seconds —Number of seconds. Range: 3 to 60000.
                                                   					 Multiple entries can be made, separated by commas, that must correspond to the
                                                   					 number of ephone-dns in the list command. Each number in a multiple entry
                                                   					 specifies the time that the corresponding ephone-dn will ring before a call is
                                                   					 forwarded to the next number in the list. If a single number is entered, it is
                                                   					 used for the no-answer period for each ephone-dn. If this
                                                   					 command is not used, the default is the number of seconds set by the timeouts ringing command, which defaults to 180 seconds. Note
                                                   					 that the default of 180 seconds may be greater than you desire. |
| Step 9 | max-timeout seconds Example: Router(config-ephone-hunt)# max-timeout 25 | (Optional)
                                             				Sets the maximum combined timeout for the no-answer periods for all ephone-dns
                                             				in the ephone-hunt list. The call proceeds to the final destination when this
                                             				timeout expires, regardless of whether it has completed the hunt cycle. seconds —Number of seconds. Range is 3 to 60000. If this
                                                   					 command is not used, the default is that no combined timeout limit is set. |
| Step 10 | preference preference-order [ secondary secondary-order ] Example: Router(config-ephone-hunt)# preference 1 | (Optional)
                                             				Sets a preference order for the ephone-dn associated with the hunt-group pilot
                                             				number. preference-order —See the CLI help for a range of
                                                   					 numeric values, where 0 is the highest preference. Default is 0. secondary secondary-order —(Optional) Preference order for the
                                                   					 secondary pilot number. See the CLI help for a range of numeric values, where 0
                                                   					 is the highest preference. Default is 7. |
| Step 11 | no-reg [ both \| pilot ] Example: Router(config-ephone-hunt)# no-reg | (Optional)
                                             				Prevents the hunt-group pilot number from registering with an H.323 gatekeeper.
                                             				If this command is not used, the default is that the pilot number registers
                                             				with the H.323 gatekeeper. both —(Optional) Both
                                                   					 the primary and secondary pilot numbers are not registered. pilot —(Optional) Only
                                                   					 the primary pilot number is not registered. In
                                                   					 Cisco CME 3.1 and later versions, if this command is used without the either
                                                   					 the both or pilot keywords, only the secondary number is not
                                                   					 registered. |
| Step 12 | fwd-final { orig-phone \| final } Example: Router(config-ephone-hunt)# fwd-final orig-phone | (Optional)
                                             				For calls that have been transferred into an ephone hunt group by a local
                                             				extension, determines the final destination of a call that is not answered in
                                             				the hunt group. final —Forwards the
                                                   					 call to the ephone-dn number that is specified in the final command. orig-phone —Forwards
                                                   					 the call to the primary directory number of the phone that transferred the call
                                                   					 into the hunt group. |
| Step 13 | forward
                                                				  local-calls Example: Router(config-ephone-hunt)# no forward local-calls | (Optional;
                                             				sequential hunt groups only) Specifies that local calls (calls from ephone-dns
                                             				on the same Cisco Unified CME system) will not be forwarded past the first list
                                             				member in a hunt group. If the first member is busy, the internal caller hears
                                             				busy. If the first number does not answer, the internal caller hears ringback. |
| Step 14 | secondary
                                                				  start [ current \| next \| list-position ] Example: Router(config-ephone-hunt)# secondary start next | (Optional)
                                             				For calls that are parked by hunt group member phones, returns them to a
                                             				different entry point in the hunt group (as specified in this command) if the
                                             				calls are recalled from park to the secondary pilot number or transferred from
                                             				park to an ephone-dn that forwards the call to the secondary pilot number. current —The ephone-dn
                                                   					 that parked the call. next —The ephone-dn in
                                                   					 the hunt group list that follows the ephone-dn that parked the call. list-position —The
                                                   					 ephone-dn at the specified position in the list specified by the list command. Range is 1 to 10. |
| Step 15 | present-call { idle-phone \| onhook-phone } Example: Router(config-ephone-hunt)# present-call idle-phone | (Optional)
                                             				Presents ephone-hunt-group calls only to member phones that are idle or onhook,
                                             				as specified. idle-phone —A call
                                                   					 from the ephone-hunt group is presented to an ephone only if all lines on the
                                                   					 phone are idle. This option ignores monitored lines that have been configured
                                                   					 on the phone using the button
                                                      						m command. onhook-phone —A call
                                                   					 from the ephone-hunt group is presented to an ephone only if the phone is in
                                                   					 the on-hook state. When this keyword is configured, calls in the ringing or
                                                   					 hold state that are unrelated to the hunt group do not prevent the presentation
                                                   					 of calls from the ephone-hunt group. |
| Step 16 | from-ring Example: Router(config-ephone-hunt)# from-ring | (Optional)
                                             				Specifies that on-hook time stamps should be recorded when calls ring
                                             				extensions and when calls are answered. The default is that on-hook time stamps
                                             				are recorded only when calls are answered. |
| Step 17 | description text-string Example: Router(config-ephone-hunt)# description Marketing Hunt Group | (Optional)
                                             				Defines text that will appear in configuration output. |
| Step 18 | display-logout text-string Example: Router(config-ephone-hunt)# display-logout Night Service | (Optional)
                                             				Defines text that will appear on IP phones that are members of a hunt group
                                             				when all the hunt-group members are in the not-ready status. This string can be
                                             				used to inform hunt-group members where the calls are being sent when all
                                             				members are unavailable to take calls. |
| Step 19 | exit Example: Router(config-ephone-hunt)# exit | Exits
                                             				ephone-hunt configuration mode. |
| Step 20 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 21 | max-redirect number Example: Router(config-telephony)# max-redirect 8 | (Optional)
                                             				Sets the number of times that a call can be redirected within a
                                             				Cisco Unified CME system. number —Range is 5 to
                                                   					 20. Default is 10. Note This
                                                      				command is required if the number of hops is greater than 10. | Note | This
                                                      				command is required if the number of hops is greater than 10. |
| Note | This
                                                      				command is required if the number of hops is greater than 10. |
| Step 22 | hunt-group logout { DND \| HLog } Example: Router(config-telephony)# hunt-group logout HLog | (Optional)
                                             				Specifies whether agent not-ready status applies only to ephone hunt group
                                             				extensions on a phone (HLog mode) or to all extensions on a phone (DND mode).
                                             				Agent not-ready status can activated by an agent using the HLog softkey or a
                                             				FAC, or it can be activated automatically after the number of calls specified
                                             				in the auto
                                                				  logout command are not answered. The default
                                             				of this command is not used is DND . DND —When phones are
                                                   					 placed in agent not-ready status, all ephone-dns on the phone will not accept
                                                   					 calls. HLog —Enables the
                                                   					 display of the HLog soft key. When phones are placed in the agent not-ready
                                                   					 status, only the ephone-dns assigned to ephone hunt groups will not accept
                                                   					 calls. |
| Step 23 | exit Example: Router(config-telephony)# exit | Exits
                                             				telephony-service configuration mode. |
| Step 24 | ephone-dn dn-tag Example: Router(config)# ephone-dn 29 | (Optional)
                                             				Enters ephone-dn configuration mode. dn-tag —Tag number for
                                                   					 the ephone-dn to be authorized to join and leave ephone hunt groups. |
| Step 25 | ephone-hunt
                                                				  login Example: Router(config-ephone-dn)# ephone-hunt login | (Optional)
                                             				Enables this ephone-dn to join and leave ephone hunt groups (dynamic
                                             				membership). |
| Step 26 | end Example: Router(config-ephone-dn)# end | Returns to
                                             				privileged EXEC mode. |

| Note | When a
                                                      				final number is defined as a pilot number of another hunt group, the pilot
                                                      				number of the first hunt group cannot be configured as a final number in any
                                                      				other hunt group. |
|---|---|

| Note | This
                                                      				command is not used for ephone hunt groups that are part of a Cisco Unified CME
                                                      				B-ACD service. The final destination for those groups is determined by the
                                                      				B-ACD service. |
|---|---|

| Note | This
                                                      				command is required if the number of hops is greater than 10. |
|---|---|

| Step 1 | Use the show
                                                				  running-config command to verify your configuration. Ephone hunt
                                          			 group parameters are listed in the ephone-hunt portion of the output. Example: Router# show running-config ephone-hunt 1 longest-idle

pilot 500

list 502, 503, *

max-timeout 30

timeout 10, 10, 10

hops 2

from-ring

fwd-final orig-phone

!

!

ephone-hunt 2 sequential

pilot 600

list 621, *, 623

final 5255348

max-timeout 10

timeout 20, 20, 20

fwd-final orig-phone

!

!

ephone-hunt 77 longest-idle

from-ring

pilot 100

list 101, *, 102

! |
|---|---|
| Step 2 | To verify the
                                          			 configuration of ephone hunt group dynamic membership, use the show
                                                				  running-config command. Look at the ephone-hunt portion of the
                                          			 output to ensure at least one wildcard slot is configured. Look at the
                                          			 ephone-dn section to see whether particular ephone-dns are authorized to join
                                          			 ephone hunt groups. Look at the telephony-service section to see whether FACs
                                          			 are enabled. Example: Router# show running-config ephone-hunt 1 longest-idle

pilot 500

list 502, 503, *

max-timeout 30

timeout 10, 10, 10

hops 2

from-ring

fwd-final orig-phone

!

!

ephone-dn 2 dual-line

number 126

preference 1

call-forward busy 500

ephone-hunt login

!

telephony-service

fac custom alias 5 *5 to *35000

fac custom ephone-hunt cancel #5 |
| Step 3 | Use the show ephone-hunt command for detailed information about hunt groups,
                                          			 including dial-peer tag numbers, hunt-group agent status, and on-hook time
                                          			 stamps. This command also displays the dial-peer tag numbers of all ephone-dns
                                          			 that have joined dynamically and are members of the group at the time that the
                                          			 command is run. Example: Router# show ephone-hunt Group 1
type: peer
pilot number: 450, peer-tag 20123
list of numbers:
451, aux-number A450A0900, # peers 5, logout 0, down 1
peer-tag dn-tag rna login/logout up/down
[20122 42 0 login up ]
[20121 41 0 login up ]
[20120 40 0 login up ]
[20119 30 0 login up ]
[20118 29 0 login down]
452, aux-number A450A0901, # peers 4, logout 0, down 0
peer-tag dn-tag rna login/logout up/down
[20127 45 0 login up ]
[20126 44 0 login up ]
[20125 43 0 login up ]
[20124 31 0 login up ]
453, aux-number A450A0902, # peers 4, logout 0, down 0
peer-tag dn-tag rna login/logout up/down
[20131 48 0 login up ]
[20130 47 0 login up ]
[20129 46 0 login up ]
[20128 32 0 login up ]
477, aux-number A450A0903, # peers 1, logout 0, down 0
peer-tag dn-tag rna login/logout up/down
[20132 499 0 login up ]
preference: 0
preference (sec): 7
timeout: 3, 3, 3, 3
max timeout : 10
hops: 4
next-to-pick: 1
E.164 register: yes
auto logout: no
stat collect: no
Group 2
type: sequential
pilot number: 601, peer-tag 20098
list of numbers:
123, aux-number A601A0200, # peers 1, logout 0, down 0
peer-tag dn-tag rna login/logout up/down
[20097 56 0 login up ]
622, aux-number A601A0201, # peers 3, logout 0, down 0
peer-tag dn-tag rna login/logout up/down
[20101 112 0 login up ]
[20100 111 0 login up ]
[20099 110 0 login up ]
623, aux-number A601A0202, # peers 3, logout 0, down 0
peer-tag dn-tag rna login/logout up/down
[20104 122 0 login up ]
[20103 121 0 login up ]
[20102 120 0 login up ]
*, aux-number A601A0203, # peers 1, logout 0, down 1
peer-tag dn-tag rna login/logout up/down
[20105 0 0 - down]
*, aux-number A601A0204, # peers 1, logout 0, down 1
peer-tag dn-tag rna login/logout up/down
[20106 0 0 - down]
final number: 5255348
preference: 0
preference (sec): 9
timeout: 5, 5, 5, 5, 5
max timeout : 40
fwd-final: orig-phone
E.164 register: yes
auto logout: no
stat collect: no
Group 3
type: longest-idle
pilot number: 100, peer-tag 20142
list of numbers:
101, aux-number A100A9700, # peers 3, logout 0, down 3
on-hook time stamp 7616, off-hook agents=0
peer-tag dn-tag rna login/logout up/down
[20141 132 0 login down]
[20140 131 0 login down]
[20139 130 0 login down]
*, aux-number A100A9701, # peers 1, logout 0, down 1
on-hook time stamp 7616, off-hook agents=0
peer-tag dn-tag rna login/logout up/down
[20143 0 0 - down]
102, aux-number A100A9702, # peers 2, logout 0, down 2
on-hook time stamp 7616, off-hook agents=0
peer-tag dn-tag rna login/logout up/down
[20145 142 0 login down]
[20144 141 0 login down]
all agents down!
preference: 0
preference (sec): 7
timeout: 100, 100, 100
hops: 0
E.164 register: yes
auto logout: no
stat collect: no |

| Restriction | Before
                                                   				  Cisco Unified CME 4.3, forwarding or transferring to a voice hunt group is not
                                                   				  supported. In
                                                   				  Cisco Unified CME 4.3 and later versions, Call Forwarding is supported to a
                                                   				  parallel hunt-group (blast hunt group) only. SIP-to-H.323 calls are not supported. If Call
                                                   				  Forward All or Call Forward Busy is configured for a hunt group member
                                                   				  (directory number), the hunt group ignores it. Caller ID
                                                   				  update is not supported for supplementary services. Voice hunt
                                                   				  groups are subject to the max-redirect restriction. A pilot
                                                   				  dial peer cannot be used for a voice hunt group and an ephone hunt group at the
                                                   				  same time. Voice hunt
                                                   				  groups do not support the expansion of pilot numbers using the dialplan-pattern command. To enable external
                                                   				  phones to dial the pilot number, you must configure a secondary pilot number
                                                   				  using a fully qualified E.164 number. If
                                                   				  call-waiting is enabled (the default), parallel hunt groups support multiple
                                                   				  calls up to the limit of call-waiting calls supported by the particular SIP
                                                   				  phone model. If call waiting is disabled, parallel hunt groups support only one
                                                   				  call at a time in the ringing state. Phones that fail to connect must return to
                                                   				  the on-hook state before they can receive other calls. A phone
                                                   				  number associated with an FXO port is not supported in parallel hunt groups. If the
                                                   				  directory number (member of a voice hunt group) is a shared line, agent status
                                                   				  control or HLog is not supported. From
                                                   				  Unified CME release 11.6 onwards, line level logout or login is not supported
                                                   				  for SIP phones. DND FAC is
                                                   				  not supported with SIP phones on Unified CME. Consider
                                                   				  an SCCP DN that is part of both voice hunt group and ephone hunt group. If
                                                   				  voice hunt group is configured with members logout or auto logout, then the
                                                   				  SCCP DN will logout only from voice hunt group. If ephone hunt group is
                                                   				  configured with members logout or auto logout, then the SCCP DN will logout
                                                   				  from both voice hunt group and ephone hunt group. For Unified CME 12.1 and prior releases, mixed shared lines and
                                                   				  SIP shared lines are not supported with voice hunt groups. For
                                                   				  parallel voice hunt group, the maximum number of call blasts that can be
                                                   				  supported is limited to 32. This includes the shared-line as well as normal
                                                   				  directory numbers. Unified CME supports chaining (nesting) of a voice hunt group with another voice hunt group. The chaining of voice hunt groups
                                                   is established by configuring the final number of the first voice hunt group as the pilot number of the second voice hunt
                                                   group. Unified CME supports the chaining (nesting) of a maximum of two voice hunt groups. The configuration ensures that there is
                                                   no looping of calls placed to a voice hunt group. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice hunt-group hunt-tag [ longest-idle \| parallel \| peer \| sequential ] Example: Router(config)# voice hunt-group 1 longest-idle | Enters voice
                                             				hunt-group configuration mode to define a hunt group. hunt-tag —Unique sequence number of the hunt group
                                                   					 to be configured. Range is 1 to 100. longest idle —Hunt group in which calls go to the
                                                   					 directory number that has been idle for the longest time. sequential —Hunt group in which directory numbers
                                                   					 ring in the order in which they are listed, left to right. parallel —Hunt group in which all directory numbers
                                                   					 ring simultaneously. peer —Hunt
                                                   					 group in which the call placed to a directory number rings for the next
                                                   					 directory number in line. To change
                                                   					 the hunt-group type, remove the existing hunt group first by using the no form of
                                                   					 the command; then, recreate the group. |
| Step 4 | pilot number [ secondary number ] Example: Router(config-voice-hunt-group)# pilot number 8100 | Defines the
                                             				telephone number that callers dial to reach a voice hunt group. number —String of up to 16 characters that
                                                   					 represents an E.164 telephone number. Number
                                                   					 string may contain alphabetic characters when the number is to be dialed only
                                                   					 by the Cisco Unified CME router, as with an intercom number, and not from
                                                   					 telephone keypads. secondary number —(Optional) Keyword and argument combination
                                                   					 defines the number that follows as an additional pilot number for the voice
                                                   					 hunt group. Secondary numbers can contain wild cards. A wildcard is a period (.), which matches any entered digit. |
| Step 5 | list number Example: Router(config-voice-hunt-group)# list 8000, 8010, 8020, 8030 | Creates a
                                             				list of extensions that are members of a voice hunt group. To remove a list
                                             				from a router configuration, use the no form of
                                             				this command. number —List
                                                   					 of extensions to be added as members to the voice hunt group. Separate the
                                                   					 extensions with commas. Add or
                                                   					 delete all extensions in a hunt-group list at one time. You cannot add or
                                                   					 delete a single number in an existing list. There
                                                   					 must be from 2 to 10 extensions in the hunt-group list, and each number must be
                                                   					 a primary or secondary number. Any
                                                   					 number in the list cannot be a pilot number of a parallel hunt group. |
| Step 6 | final number Example: Router(config-voice-hunt-group)# final 8888 | Defines the
                                             				last extension in a voice hunt group. If a
                                                   					 final number in one hunt group is configured as a pilot number of another hunt
                                                   					 group, the pilot number of the first hunt group cannot be configured as a final
                                                   					 number in any other hunt group. This
                                                   					 command is not used for voice hunt groups that are part of a Cisco Unified CME
                                                   					 B-ACD service. The final destination for those groups is determined by the
                                                   					 B-ACD service. |
| Step 7 | preference preference-order [ secondary secondary-order ] Example: Router(config-voice-hunt-group)# preference 6 | Sets the
                                             				preference order for the directory number associated with a voice hunt-group
                                             				pilot number. Note We
                                                      				recommend that the parallel hunt-group pilot number be unique in the system.
                                                      				Parallel hunt groups may not work if there are more than one partial or exact
                                                      				dial-peer match. For example, if the pilot number is “8000” and there is
                                                      				another dial peer that matches “8…”. If multiple matches cannot be avoided,
                                                      				give parallel hunt groups the highest priority to run by assigning a lower
                                                      				preference to the other dial peers. Note that 8 is the lowest preference value.
                                                      				By default, dial peers created by parallel hunt groups have a preference of 0. preference-order —Range is 0 to 8, where 0 is the
                                                   					 highest preference and 8 is the lowest preference. Default is 0. secondary secondary-order— (Optional) Keyword and argument combination is
                                                   					 used to set the preference order for the secondary pilot number. Range is 1 to
                                                   					 8, where 0 is the highest preference and 8 is the lowest preference. Default is
                                                   					 7. | Note | We
                                                      				recommend that the parallel hunt-group pilot number be unique in the system.
                                                      				Parallel hunt groups may not work if there are more than one partial or exact
                                                      				dial-peer match. For example, if the pilot number is “8000” and there is
                                                      				another dial peer that matches “8…”. If multiple matches cannot be avoided,
                                                      				give parallel hunt groups the highest priority to run by assigning a lower
                                                      				preference to the other dial peers. Note that 8 is the lowest preference value.
                                                      				By default, dial peers created by parallel hunt groups have a preference of 0. |
| Note | We
                                                      				recommend that the parallel hunt-group pilot number be unique in the system.
                                                      				Parallel hunt groups may not work if there are more than one partial or exact
                                                      				dial-peer match. For example, if the pilot number is “8000” and there is
                                                      				another dial peer that matches “8…”. If multiple matches cannot be avoided,
                                                      				give parallel hunt groups the highest priority to run by assigning a lower
                                                      				preference to the other dial peers. Note that 8 is the lowest preference value.
                                                      				By default, dial peers created by parallel hunt groups have a preference of 0. |
| Step 8 | hops number Example: Router(config-voice-hunt-group)# hops 2 | For
                                             				configuring a peer or longest-idle voice hunt group only. Defines the number of
                                             				times that a call can hop to the next number in a peer or longest-idle voice
                                             				hunt group before the call proceeds to the final number. number —Number of hops. Range is 2 to 10, and the
                                                   					 value must be less than or equal to the number of extensions specified by
                                                   					 the list command. Default
                                                   					 is the same number as there are destinations defined under the list command. |
| Step 9 | timeout seconds Example: Router(config-voice-hunt-group)# timeout 100 | Defines the
                                             				number of seconds after which a call that is not answered is redirected to the
                                             				next directory number in a voice hunt-group list. Default: 180 seconds. |
| Step 10 | present-call idle-phone Example: Router(config-voice-hunt-group)# present-call idle-phone | Specifies
                                             				that voice hunt-group calls are presented only if all lines are idle on the
                                             				phone on which the hunt-group line appears. |
| Step 11 | members logout Example: Router(config-voice-hunt-group)# members logout | Configures a
                                             				Cisco Unified CME system for all non-shared static members or agents in a voice
                                             				hunt group with the Hlogout initial state. |
| Step 12 | auto logout number-of-calls Example: Router(config-voice-hunt-group)# auto logout 2 | Enables the
                                             				automatic change of a voice hunt group agent’s voice register dn or ephone-dn
                                             				to not-ready status after a specified number of successive hunt-group calls are
                                             				not answered. |
| Step 13 | exit Example: Router(config-voice-hunt-group)# exit | Exits
                                             				voice-hunt-group configuration mode. |
| Step 14 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 15 | hunt-group logout { DND HLog } Example: Router(config-telephony)# hunt-group logout Hlog | (Optional)
                                             				Specifies HLog softkey functions. Agent not-ready status can be activated by an
                                             				agent using the HLog softkey or a FAC. |
| Step 16 | exit Example: Router(config-telephony)# exit | Exits
                                             				telephony-service configuration mode. |
| Step 17 | voice register dn tag Example: Router(config)# voice register dn 29 | (Optional)
                                             				Enters voice register dn configuration mode. tag —Tag
                                                   					 number for voice register dn to be authorized to join and leave voice hunt
                                                   					 groups. |
| Step 18 | voice-hunt-groups login Example: Router(config-register-dn)# voice-hunt-groups login | (Optional)
                                             				Enables this voice register dn to join and leave voice hunt groups (dynamic
                                             				membership). |
| Step 19 | end Example: Router(config-register-dn)# end | Exits to
                                          			 privileged EXEC mode. |

| Note | We
                                                      				recommend that the parallel hunt-group pilot number be unique in the system.
                                                      				Parallel hunt groups may not work if there are more than one partial or exact
                                                      				dial-peer match. For example, if the pilot number is “8000” and there is
                                                      				another dial peer that matches “8…”. If multiple matches cannot be avoided,
                                                      				give parallel hunt groups the highest priority to run by assigning a lower
                                                      				preference to the other dial peers. Note that 8 is the lowest preference value.
                                                      				By default, dial peers created by parallel hunt groups have a preference of 0. |
|---|---|

| Step 1 | Use the show
                                                				  running-config command to verify your configuration. Voice hunt
                                          			 group parameters are listed in the voice-hunt portion of the output. Example: Router# show running-config voice-hunt 1 longest-idle
pilot 500
list 502, 503, *
max-timeout 30
timeout 10, 10, 10
hops 2
from-ring
fwd-final orig-phone
!
!
voice-hunt 2 sequential
pilot 600
list 621, *, 623
final 5255348
max-timeout 10
timeout 20, 20, 20
fwd-final orig-phone
!
!
voice-hunt 77 longest-idle
from-ring
pilot 100
list 101, *, 102
! |
|---|---|
| Step 2 | To verify the
                                          			 configuration of voice hunt group dynamic membership, use the show
                                                				  running-config command. Look at the voice-hunt portion of the
                                          			 output to ensure at least one wildcard slot is configured. Look at the voice-dn
                                          			 section to see whether particular ephone-dns are authorized to join voice hunt
                                          			 groups. Look at the telephony-service section to see whether FACs are enabled. Example: Router# show running-config voice-hunt 1 longest-idle
pilot 500
list 502, 503, *
max-timeout 30
timeout 10, 10, 10
hops 2
from-ring
fwd-final orig-phone
!
!
voice-dn 2 dual-line
number 126
preference 1
call-forward busy 500
ephone-hunt login
!
telephony-service
fac custom alias 5 *5 to *35000
fac custom ephone-hunt cancel #5 |
| Step 3 | Use the show ephone-hunt command for detailed information about hunt groups,
                                          			 including dial-peer tag numbers, hunt-group agent status, and on-hook time
                                          			 stamps. This command also displays the dial-peer tag numbers of all ephone-dns
                                          			 that have joined dynamically and are members of the group at the time that the
                                          			 command is run. Example: Router# show ephone-hunt Group 1
type: peer
pilot number: 450, peer-tag 20123
list of numbers:
451, aux-number A450A0900, # peers 5, logout 0, down 1
peer-tag dn-tag rna login/logout up/down
[20122 42 0 login up ]
[20121 41 0 login up ]
[20120 40 0 login up ]
[20119 30 0 login up ]
[20118 29 0 login down]
452, aux-number A450A0901, # peers 4, logout 0, down 0
peer-tag dn-tag rna login/logout up/down
[20127 45 0 login up ]
[20126 44 0 login up ]
[20125 43 0 login up ]
[20124 31 0 login up ]
453, aux-number A450A0902, # peers 4, logout 0, down 0
peer-tag dn-tag rna login/logout up/down
[20131 48 0 login up ]
[20130 47 0 login up ]
[20129 46 0 login up ]
[20128 32 0 login up ]
477, aux-number A450A0903, # peers 1, logout 0, down 0
peer-tag dn-tag rna login/logout up/down
[20132 499 0 login up ]
preference: 0
preference (sec): 7
timeout: 3, 3, 3, 3
max timeout : 10
hops: 4
next-to-pick: 1
E.164 register: yes
auto logout: no
stat collect: no
Group 2
type: sequential
pilot number: 601, peer-tag 20098
list of numbers:
123, aux-number A601A0200, # peers 1, logout 0, down 0
peer-tag dn-tag rna login/logout up/down
[20097 56 0 login up ]
622, aux-number A601A0201, # peers 3, logout 0, down 0
peer-tag dn-tag rna login/logout up/down
[20101 112 0 login up ]
[20100 111 0 login up ]
[20099 110 0 login up ]
623, aux-number A601A0202, # peers 3, logout 0, down 0
peer-tag dn-tag rna login/logout up/down
[20104 122 0 login up ]
[20103 121 0 login up ]
[20102 120 0 login up ]
*, aux-number A601A0203, # peers 1, logout 0, down 1
peer-tag dn-tag rna login/logout up/down
[20105 0 0 - down]
*, aux-number A601A0204, # peers 1, logout 0, down 1
peer-tag dn-tag rna login/logout up/down
[20106 0 0 - down]
final number: 5255348
preference: 0
preference (sec): 9
timeout: 5, 5, 5, 5, 5
max timeout : 40
fwd-final: orig-phone
E.164 register: yes
auto logout: no
stat collect: no
Group 3
type: longest-idle
pilot number: 100, peer-tag 20142
list of numbers:
101, aux-number A100A9700, # peers 3, logout 0, down 3
on-hook time stamp 7616, off-hook agents=0
peer-tag dn-tag rna login/logout up/down
[20141 132 0 login down]
[20140 131 0 login down]
[20139 130 0 login down]
*, aux-number A100A9701, # peers 1, logout 0, down 1
on-hook time stamp 7616, off-hook agents=0
peer-tag dn-tag rna login/logout up/down
[20143 0 0 - down]
102, aux-number A100A9702, # peers 2, logout 0, down 2
on-hook time stamp 7616, off-hook agents=0
peer-tag dn-tag rna login/logout up/down
[20145 142 0 login down]
[20144 141 0 login down]
all agents down!
preference: 0
preference (sec): 7
timeout: 100, 100, 100
hops: 0
E.164 register: yes
auto logout: no
stat collect: no |

| Restriction | Supports all 79xx phones except for 7926 wireless phones. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone phone-tag or ephone-template template-tag Example: Router(config)# ephone 25 | Enters ephone configuration mode. phone-tag —The unique sequence number of the phone that will be notified when an incoming call is received by a night-service ephone-dn
                                                   during a night-service period. or Enters ephone-template configuration mode to create an ephone template. template-tag —Unique identifier for the ephone template that is being created. Range: 1 to 20. |
| Step 4 | audible tone Example: Router(config-ephone)# audible tone | Enables playing of audible tone on an SCCP phone to confirm a successful login or logout. |
| Step 5 | end Example: Router(config-ephone)# end |  |

| Restriction | Hold and resume statistics are not updated for remote SCCP voice
                                             			 hunt group agents. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice hunt-group hunt-tag { longest-idle \| parallel \| peer \| sequential } Example: Router(config)# voice hunt-group 60 longest-idle | Enters voice hunt-group configuration mode. hunt-tag —Unique sequence number that
                                                				  identifies the hunt group. Range: 1 to 100. longest-idle —Hunt group in which
                                                				  calls go to the directory number that has been idle the longest. parallel —Hunt group in which calls
                                                				  simultaneously ring multiple phones. peer —Hunt group in which the first
                                                				  extension to ring is selected round-robin from the list. Ringing proceeds in a
                                                				  circular manner, left to right, for the number of hops specified when the hunt
                                                				  group is defined. The round-robin selection starts with the number left of the
                                                				  number that answered when the hunt-group was last called. sequential —Hunt group in which
                                                				  extensions ring in the order in which they are listed, left to right, when the
                                                				  hunt group was defined. |
| Step 4 | statistics collect Example: Router(config-voice-hunt-group)# statistics collect | Enables the collection of call statistics for a voice hunt group. |
| Step 5 | end Example: Router(config-voice-hunt-group)# end | Exits to privileged EXEC mode. |

| Restriction | Cisco Unified
                                             			 SIP IP phones are not supported. The display support applies to Cisco Unified
                                             			 SCCP IP phones on voice hunt-group and ephone-hunt configuration modes only. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice hunt-group hunt-tag { parallel } Example: Router(config)# voice hunt-group 20 parallel | Creates a hunt
                                             				group for phones in a Cisco Unified CME system. hunt-tag —Unique sequence number that identifies
                                                   					 the hunt group. Range is 1 to 100. parallel —Hunt group in which calls simultaneously
                                                   					 ring multiple phones. |
| Step 4 | final number Example: Router(config-voice-hunt-group)# final 4000 | Defines the
                                             				last extension in a voice hunt group. number —Telephone or extension number. Can be an
                                                				  E.164 number, voice-mail number, pilot number of another hunt group, or FXS
                                                				  caller-ID number. |
| Step 5 | list number [ , number ... ] Example: Router(config-voice-hunt-group)# list 3001, 3002, 3003 | Defines a list
                                             				of extensions that are members of a voice hunt group. number —Extension or E.164 number assigned to a
                                                   					 phone in Cisco Unified CME. List must contain 2 to 32 numbers. |
| Step 6 | timeout seconds Example: Router(config-voice-hunt-group)# timeout 20 | Defines the
                                             				number of seconds after which a call that is not answered is redirected to the
                                             				next number in a voice hunt-group list. seconds —Number of seconds. Range is 3 to 60000.
                                                   					 Default is 180. |
| Step 7 | pilot number [ secondary number ] Example: Router(config-voice-hunt-group)# pilot 4045550110 secondary 3125550120 | Defines the
                                             				number that callers dial to reach a Cisco Unified CME voice hunt group. number —String of up to 32 characters that
                                                   					 represents an extension or E.164 telephone number. secondary number —(Optional) Defines an additional pilot
                                                   					 number for the voice hunt group. |
| Step 8 | name “primary pilot
                                                				  name” [ secondary “secondary pilot
                                                				  name” ] Example: Router(config-voice-hunt-group)# name Hospital secondary “Health Center” | Associates a
                                             				name with the called voice hunt group. “primary pilot
                                                         						  name” —Name for the primary pilot number. secondary “secondary pilot
                                                         						  name” —(Optional) Name for the secondary pilot number. Note Use
                                                      				quotes (") when input strings have spaces in between. | Note | Use
                                                      				quotes (") when input strings have spaces in between. |
| Note | Use
                                                      				quotes (") when input strings have spaces in between. |

| Note | Use
                                                      				quotes (") when input strings have spaces in between. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice hunt-group hunt-tag { parallel \| sequential } Example: Router(config)# voice hunt-group 1 sequential | Creates a hunt group for phones in a Cisco Unified CME system. hunt-tag —Unique
                                                				  sequence number that identifies the hunt group. Range is 1 to 100. parallel —Hunt group in which calls
                                                				  simultaneously ring multiple phones. sequential —Hunt group in which
                                                				  extensions ring in the order in which they are listed, left to right, when the
                                                				  hunt group was defined. |
| Step 4 | [ no ] forward local-calls to-final Example: Router(config-voice-hunt-group)# no forward local-calls to-final | Prevents local calls from being forwarded to the final destination
                                             				number. |

| Restriction | Night
                                                   				  service notification is not supported on analog endpoints connected to FXS
                                                   				  ports on a Cisco Integrated Services Router (ISR) or Cisco VG224 Analog Phone
                                                   				  Gateway. In
                                                   				  Cisco Unified CME 4.0 and later versions, silent ringing, configured on the
                                                   				  phone by using the s keyword
                                                   				  with the button command, is suppressed when used with the night service feature. Silent ringing
                                                   				  is overridden and the phone audibly rings during designated night-service
                                                   				  periods. |
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
| Step 4 | night-service day day start-time stop-time Example: Router(config-telephony)# night-service day mon 19:00 07:00 | Defines a
                                             				recurring time period associated with a day of the week during which night
                                             				service is active. day —Day of the week abbreviation. The following are valid
                                                   					 day abbreviations: sun , mon , tue , wed , thu , fri , sat . start-time stop-time —Beginning and ending times for night
                                                   					 service, in an HH:MM format using a 24-hour clock. If the stop time is a
                                                   					 smaller value than the start time, the stop time occurs the day following the
                                                   					 start time. For example, “mon 19:00 07:00” means “from Monday at 7 p.m. until
                                                   					 Tuesday at 7 a.m.” |
| Step 5 | night-service date month date start-time stop-time Example: Router(config-telephony)# night-service date jan 1 00:00 00:00 | Defines a
                                             				recurring time period associated with a month and date during which night
                                             				service is active. month —Month abbreviation. The following are valid month
                                                   					 abbreviations: jan , feb , mar , apr , may , jun , jul , aug , sep , oct , nov , dec . date —Date of the month. Range is 1 to 31. start-time stop-time —Beginning and ending times for night
                                                   					 service, in an HH:MM format using a 24-hour clock. The stop time must be
                                                   					 greater than the start time. The value 24:00 is not valid. If 00:00 is entered
                                                   					 as a stop time, it is changed to 23:59. If 00:00 is entered for both start time
                                                   					 and stop time, calls are blocked for the entire 24-hour period on the specified
                                                   					 date. |
| Step 6 | night-service everyday start-time
                                                				  stop-time Example: Router(config-telephony)# night-service everyday 1200 1300 | Defines a
                                             				recurring night-service time period to be effective everyday. start-time stop-time —Beginning and ending times for night
                                                   					 service, in an HH:MM format using a 24-hour clock. If the stop time is a
                                                   					 smaller value than the start time, the stop time occurs the day following the
                                                   					 start time. For example, “19:00 07:00” means “from 7 p.m. to 7 a.m. the next
                                                   					 morning.” The value 24:00 is not valid. If 00:00 is entered as a stop time, it
                                                   					 is changed to 23:59. If 00:00 is entered for both start time and stop time, the
                                                   					 night service feature will be activated for the entire 24-hour period. |
| Step 7 | night-service weekday start-time
                                                				  stop-time Example: Router(config-telephony)# night-service weekday 1700 0700 | Defines a
                                             				recurring night-service time period to be effective on all weekdays. start-time
                                                      						stop-time —Beginning and ending times for night service, in an HH:MM format
                                                   					 using a 24-hour clock. If the stop time is a smaller value than the start time,
                                                   					 the stop time occurs the day following the start time. For example, “19:00
                                                   					 07:00” means “from 7 p.m. to 7 a.m. the next morning.” The value 24:00 is not
                                                   					 valid. If 00:00 is entered as a stop time, it is changed to 23:59. If 00:00 is
                                                   					 entered for both start time and stop time, the night service feature will be
                                                   					 activated for the entire 24-hour period. |
| Step 8 | night-service weekend start-time
                                                				  stop-time Example: Router(config-telephony)# night-service weekend 00:00 00:00 | Defines a
                                             				recurring night-service time period to be effective on all weekend days
                                             				(Saturday and Sunday). start-time
                                                         						  stop-time —Beginning and ending times for night service, in an
                                                   					 HH:MM format using a 24-hour clock. If the stop time is a smaller value than
                                                   					 the start time, the stop time occurs the day following the start time. For
                                                   					 example, “19:00 07:00” means “from 7 p.m. to 7 a.m. the next morning.” The
                                                   					 value 24:00 is not valid. If 00:00 is entered as a stop time, it is changed to
                                                   					 23:59. If 00:00 is entered for both start time and stop time, the night service
                                                   					 feature will be activated for the entire 24-hour period. |
| Step 9 | night-service code digit-string Example: Router(config-telephony)# night-service code *6483 | Designates
                                             				a code that can be dialed from any night-service line (ephone-dn) to toggle
                                             				night service on and off for all lines assigned to night service in the system. digit-string —String of up to 16 keypad digits. The
                                                   					 code must begin with an asterisk (*). |
| Step 10 | timeouts
                                                				  night-service-bell seconds Example: Router(config-telephony)# timeouts night-service-bell 15 | Defines the
                                             				frequency of the night-service notification. seconds —Range: 4 to 30. Default: 12. |
| Step 11 | exit Example: Router(config-telephony)# exit | Exits
                                             				telephony-service configuration mode. |
| Step 12 | ephone-dn dn-tag Example: Router(config)# ephone-dn 55 | Enters
                                             				ephone-dn configuration mode to define an ephone-dn to receive night-service
                                             				treatment. |
| Step 13 | night-service
                                                				  bell Example: Router(config-ephone-dn)# night-service bell | Marks this
                                             				ephone-dn for night-service treatment. |
| Step 14 | exit Example: Router(config-ephone-dn)# exit | Exits
                                             				ephone-dn configuration mode. |
| Step 15 | ephone phone-tag Example: Router(config)# ephone 12 | Enters
                                             				ephone configuration mode. phone-tag —The unique
                                                   					 sequence number of the phone that will be notified when an incoming call is
                                                   					 received by a night-service ephone-dn during a night-service period. |
| Step 16 | night-service
                                                				  bell Example: Router(config-ephone)# night-service bell | Marks this
                                             				phone to receive night-service bell notification when incoming calls are
                                             				received on ephone-dns marked for night service during the night-service time
                                             				period. Night
                                                   					 service notification is not supported on analog endpoints connected to SCCP FXS
                                                   					 ports on a Cisco ISR or Cisco VG224. |
| Step 17 | end Example: Router(config-ephone)# end | Returns to
                                             				privileged EXEC mode. |

| Restriction | When service directed-pickup
                                                         						gpickup is configured under telephony service, gpickup softkey
                                                   				  has to be used on SCCP phones to pick up the ringing call on night-service
                                                   				  extensions. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters
                                             				global configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 4 | night-service
                                                				  day day start-time stop-time Example: Router(config-telephony)# night-service day mon 19:00 07:00 | Defines a
                                             				recurring time period associated with a day of the week during which night
                                             				service is active. day —Day of the week
                                                   					 abbreviation. The following are valid day abbreviations: sun , mon , tue , wed , thu , fri , sat . start-time
                                                      						stop-time —Beginning and ending times for night service, in an HH:MM format
                                                   					 using a 24-hour clock. If the stop time is a smaller value than the start time,
                                                   					 the stop time occurs the day following the start time. For example, “mon 19:00
                                                   					 07:00” means “from Monday at 7 p.m. until Tuesday at 7 a.m.” |
| Step 5 | night-service date month date start-time stop-time Example: Router(config-telephony)# night-service date jan 1 00:00 00:00 | Defines a
                                             				recurring time period associated with a month and date during which night
                                             				service is active. month —Month
                                                   					 abbreviation. The following are valid month abbreviations: jan , feb , mar , apr , may , jun , jul , aug , sep , oct , nov , dec . date —Date of the
                                                   					 month. Range is 1 to 31. start-time
                                                      						stop-time —Beginning and ending times for night service, in an HH:MM format
                                                   					 using a 24-hour clock. The stop time must be greater than the start time. The
                                                   					 value 24:00 is not valid. If 00:00 is entered as a stop time, it is changed to
                                                   					 23:59. If 00:00 is entered for both start time and stop time, calls are blocked
                                                   					 for the entire 24-hour period on the specified date. |
| Step 6 | night-service everyday start-time
                                                				  stop-time Example: Router(config-telephony)# night-service everyday 1200 1300 | Defines a
                                             				recurring night-service time period to be effective everyday. start-time
                                                      						stop-time —Beginning and ending times for night service, in an HH:MM format
                                                   					 using a 24-hour clock. If the stop time is a smaller value than the start time,
                                                   					 the stop time occurs the day following the start time. For example, “19:00
                                                   					 07:00” means “from 7 p.m. to 7 a.m. the next morning.” The value 24:00 is not
                                                   					 valid. If 00:00 is entered as a stop time, it is changed to 23:59. If 00:00 is
                                                   					 entered for both start time and stop time, the night service feature will be
                                                   					 activated for the entire 24-hour period. |
| Step 7 | night-service weekday start-time
                                                				  stop-time Example: Router(config-telephony)# night-service weekday 1700 0700 | Defines a
                                             				recurring night-service time period to be effective on all weekdays. start-time
                                                      						stop-time —Beginning and ending times for night service, in an HH:MM format
                                                   					 using a 24-hour clock. If the stop time is a smaller value than the start time,
                                                   					 the stop time occurs the day following the start time. For example, “19:00
                                                   					 07:00” means “from 7 p.m. to 7 a.m. the next morning.” The value 24:00 is not
                                                   					 valid. If 00:00 is entered as a stop time, it is changed to 23:59. If 00:00 is
                                                   					 entered for both start time and stop time, the night service feature will be
                                                   					 activated for the entire 24-hour period. |
| Step 8 | night-service weekend start-time
                                                				  stop-time Example: Router(config-telephony)# night-service weekend 00:00 00:00 | Defines a
                                             				recurring night-service time period to be effective on all weekend days
                                             				(Saturday and Sunday). start-time
                                                         						  stop-time —Beginning and ending times for night service, in an
                                                   					 HH:MM format using a 24-hour clock. If the stop time is a smaller value than
                                                   					 the start time, the stop time occurs the day following the start time. For
                                                   					 example, “19:00 07:00” means “from 7 p.m. to 7 a.m. the next morning.” The
                                                   					 value 24:00 is not valid. If 00:00 is entered as a stop time, it is changed to
                                                   					 23:59. If 00:00 is entered for both start time and stop time, the night service
                                                   					 feature will be activated for the entire 24-hour period. |
| Step 9 | fac standard Example: Router(config-telephony)# fac standard | (Optional)
                                             				Enables predefined standard feature access codes (FACs) to be enabled. For the
                                             				CLI command night-service code to work, it is mandatory to configure fac standard under telephony-service configuration mode. |
| Step 10 | night-service code digit-string Example: Router(config-telephony)# night-service code *6483 | Designates
                                             				a code that can be dialed from any night-service line (voice register dn) to
                                             				toggle night service on and off for all lines assigned to night service in the
                                             				system. digit-string —String of up to 16 keypad digits. The
                                                   					 code must begin with an asterisk (*). |
| Step 11 | call-park system application Example: Router(config-telephony)# call-park system application | Enables or disables Night Service functionality using night
                                             				service code on SIP phones. |
| Step 12 | service directed-pickup gpickup Example: Router(config-telephony)# service directed-pickup gpickup | Enables Directed Call Pickup and modifies the function of the
                                             				GPickUp and PickUp soft keys. |
| Step 13 | timeouts
                                                				  night-service-bell seconds Example: Router(config-telephony)# timeouts night-service-bell 15 | Defines the
                                             				frequency of the night-service notification. seconds —Range: 4 to 30. Default: 12. |
| Step 14 | exit Example: Router(config-telephony)# exit | Exits
                                             				telephony-service configuration mode. |
| Step 15 | voice register
                                                				  dn dn-tag Example: Router(config)# voice register dn 10 | Enters voice
                                             				register dn configuration mode to define a voice register dn to receive
                                             				night-service treatment. |
| Step 16 | night-service
                                                				  bell Example: Router(config-register-dn)# night-service bell | Marks this
                                             				voice register dn for night-service treatment. |
| Step 17 | exit Example: Router(config-register-dn)# exit | Exits voice
                                             				register dn configuration mode. |
| Step 18 | voice register
                                                				  pool pool -tag \| voice register
                                                				  template template-tag Example: Router(config)# voice register pool 10 Router(config)# voice register template 1 | Enters pool
                                             				configuration mode (or template configuration mode). pool-tag —The unique
                                                   					 sequence number of the phone that will be notified when an incoming call is
                                                   					 received by a night-service voice-dn during a night-service period. |
| Step 19 | night-service
                                                				  bell Example: Router(config-register-pool)# night-service bell Router(config-register-template)# night-service bell | Marks this
                                             				phone to receive night-service bell notification when incoming calls are
                                             				received on voice register dns marked for night service during the
                                             				night-service time period. |
| Step 20 | voice register
                                                				  pool pool-tag Example: Router(config)# voice register pool 10 | Enters pool
                                             				configuration mode. This step is valid only when the night service
                                             				configuration is under voice register template. |
| Step 21 | template template-tag Example: Router(config-register-pool)# template 1 | Includes the
                                             				template with night-service bell configured to provide night service treatment
                                             				for this pool. This step is valid only when the night service configuration is
                                             				under voice register template. |
| Step 22 | end Example: Router(config-register-temp)# end | Returns to
                                             				privileged EXEC mode. |

| Step 1 | Use the show
                                                				  running-config command to verify the night-service parameters,
                                          			 which are listed in the telephony-service portion of the output, or use the show
                                                				  telephony-service command to display the same parameters. Example: Router# show running-config telephony-service fxo hook-flash load 7910 P00403020214 load 7960-7940 P00303020214 max-ephones 48 max-dn 288 ip source-address 10.50.50.1 port 2000 application segway0 caller-id block code *321 create cnf-files version-stamp 7960 Mar 07 2003 11:19:18 voicemail 79000 max-conferences 8 call-forward pattern ..... moh minuet.wav date-format yy-mm-dd transfer-system full-consult transfer-pattern ..... secondary-dialtone 9 night-service code *1234 night-service day Tue 00:00 23:00 night-service day Wed 01:00 23:59 ! ! Router# show telephony-service CONFIG (Version=4.0(0)) ===================== Version 4.0(0) Cisco Unified CallManager Express For on-line documentation please see: www.cisco.com/en/US/products/sw/voicesw/tsd_products_support_category_home.html ip source-address 10.103.3.201 port 2000 load 7910 P00403020214 load 7961 TERM41.7-0-1-1 load 7961GE TERM41.7-0-1-1 load 7960-7940 P00307020300 max-ephones 100 max-dn 500 max-conferences 8 gain -6 dspfarm units 2 dspfarm transcode sessions 4 dspfarm 1 MTP00059a3d7441 dspfarm 2 hunt-group report delay 1 hours Number of hunt-group configured: 14 hunt-group logout DND max-redirect 20 voicemail 7189 cnf-file location: system: cnf-file option: PER-PHONE-TYPE network-locale[0] US   (This is the default network locale for this box) user-locale[0] US    (This is the default user locale for this box) moh flash:music-on-hold.au time-format 12 date-format mm-dd-yy timezone 0 Greenwich Standard Time secondary-dialtone 9 call-forward pattern .T transfer-pattern 92...... transfer-pattern 91.......... transfer-pattern .T after-hours block pattern 1 91900 7-24 after-hours block pattern 2 9976 7-24 after-hours block pattern 4 91...976.... 7-24 night-service time is activated night-service date Jan 1 00:00 23:59 night-service day Mon 17:00 07:00 night-service day Wed 17:00 07:00 keepalive 30 timeout interdigit 10 timeout busy 10 timeout ringing 100 caller-id name-only: enable system message XYZ Company web admin system name xyz password xxxx web admin customer name Customer edit DN through Web:  enabled. edit TIME through web:  enabled. Log (table parameters): max-size: 150 retain-timer: 15 create cnf-files version-stamp Jan 01 2002 00:00:00 transfer-system full-consult multicast moh 239.10.10.1 port 2000 fxo hook-flash local directory service: enabled. |
|---|---|
| Step 2 | Use
                                          			 the show
                                                				  running-config command to verify that the correct ephone-dns and
                                          			 ephones are configured with the night-service bell command. You can also use the show telephony-service
                                                				  ephone-dn and show telephony-service
                                                				  ephone commands to display these parameters. Example: Router# show running-config ephone-dn 24 dual-line number 2548 description FrontDesk night-service bell ephone  1 mac-address 110F.80C0.FE0B type 7960 addon 1 7914 no dnd feature-ring keep-conference button  1f40 2f41 3f42 4:30 button  7m20 8m21 9m22 10m23 button  11m24 12m25 13m26 night-service bell |

| Step 1 | Use the show running-config \|
                                                				  section telephony-service command to verify the night-service parameters that
                                          			 are listed in the telephony-service portion of the output. Use the show
                                                				  telephony-service command to display the same parameters. Example: Router# show running-config \| section telephony-service telephony-service
 max-ephones 50
 max-dn 50
 ip source-address 10.50.50.1 port 2000
 service phone sshAccess 0
 service phone webAccess 0
 service directed-pickup gpickup
 time-zone 39
 max-conferences 8 gain -6
 call-park system application
 hunt-group report url suffix 0 to 100
 hunt-group report every 1 hours
 hunt-group logout HLog
 transfer-system full-consult night-service weekday 13:17 14:17
 night-service day Sun 00:05 23:59
 night-service day Sat 00:05 23:59 night-service code *6483 Router# show telephony-service max-ephones 50
 max-dn 50
 ip source-address 10.50.50.1 port 2000
 service phone sshAccess 0
 service phone webAccess 0
  time-zone 39
 max-conferences 8 gain -6 call-park system application hunt-group report url suffix 0 to 100
 hunt-group report every 1 hours
 hunt-group logout HLog
 transfer-system full-consult
 night-service time is activated
 night-service weekday 13:17 14:17
 night-service day Sun 00:05 23:59
 night-service day Sat 00:05 23:59 |
|---|---|---|---|
| Step 2 | Use the show voice register dn and show voice register pool command to verify that the correct voice register
                                          			 dns and phones are configured with the night-service bell command. Example: Router# show voice register dn 1 Dn Tag 1
Config:
 Number is 8001
 Preference is 0
 Huntstop is disabled
 Auto answer is disabled
 Pickup group is 5
 Night Service Bell is enabled Router# show voice register pool 5 Pool Tag 5
Config:
 Mac address is B000.B4BE.F32C
 Type is 8851
 Number list 1 : DN 5
 Proxy Ip address is 0.0.0.0
 DTMF Relay is disabled
 Call Waiting is enabled
 DnD is disabled
 Video is disabled
 Camera is disabled
 Night Service Bell is enabled
 Busy trigger per button value is 2 |

| Restriction | Call waiting
                                                   				  is disabled when you configure ephone-dn overlays using the o keyword
                                                   				  with the button command. To enable call waiting, you must configure ephone-dn overlays using
                                                   				  the c keyword
                                                   				  with the button command. Rollover of
                                                   				  overlay calls to another phone button by using the x keyword
                                                   				  with the button command only works to expand coverage if the overlay button is configured with
                                                   				  the o keyword in
                                                   				  the button command. Overlay buttons with call waiting that use the c keyword in the button command are not eligible for overlay rollover. In Cisco
                                                   				  Unified CME 4.0(3), the Cisco Unified IP Phone 7931G cannot support overlays
                                                   				  that contain ephone-dn configured for dual-line mode. The primary
                                                   				  ephone-dn on each phone in a shared-line overlay set should be an ephone-dn
                                                   				  that is unique to the phone to guarantee that the phone will have a line
                                                   				  available for outgoing calls, and to ensure that the phone user can obtain
                                                   				  dial-tone even when there are no idle lines available in the rest of the
                                                   				  shared-line overlay set. Use a unique ephone-dn in this manner to provide for a
                                                   				  unique calling party identity on outbound calls made by the phone so that the
                                                   				  called user can see which specific phone is calling. Octo-line
                                                   				  directory numbers are not supported in button overlay sets. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-dn phone-tag [ dual-line ] Example: Router(config)# ephone-dn 10 dual-line | Enters
                                             				ephone-dn configuration mode to create an extension (ephone-dn) for a
                                             				Cisco Unified IP phone line. For
                                                   					 shared-line overlay set: Primary ephone-dn on a phone should be an ephone-dn
                                                   					 that is unique to the phone. |
| Step 4 | number number Example: Router(config-ephone-dn)# number 1001 | Associates a
                                             				telephone or extension number with the ephone-dn. |
| Step 5 | preference preference-order Example: Router(config-ephone-dn)# preference 1 | Sets dial-peer
                                             				preference order for an ephone-dn. preference-order —Preference order for the primary
                                                   					 number associated with an extension (ephone-dn). Type ? for a range of numeric options, where 0 is the
                                                   					 highest preference. Default: 0. |
| Step 6 | no huntstop or huntstop Example: Router(config-ephone-dn)# no huntstop 
or
Router(config-ephone-dn)# huntstop | Explicitly enables call hunting behavior for a directory number. Set this command on all ephone-dns in the overlay set except the final instance. Required to allow call hunting allow call hunting across multiple numbers on the same line button on an IP phone. or Disables call hunting behavior for a directory number. Set this command on the last ephone-dn within a overlay set. Required to limit the call hunting to an overlay set. |
| Step 7 | huntstop
                                                				  channel Example: Router(config-ephone-dn)# huntstop channel | Only for
                                             				dual-line ephone-dns in overlay set; keeps incoming calls from hunting to the
                                             				second channel if the first channel is busy or does not answer. Reserves
                                                   					 the second channel for outgoing calls, such as a consultation call to be placed
                                                   					 during a call transfer attempt, or for conferencing |
| Step 8 | call-forward
                                                				  noan Example: Router(config-ephone-dn)# call-forward noan | (Optional)
                                             				Forwards incoming unanswered call to next line in the overlay set. Set this
                                                   					 command on all ephone-dns in the overlay set. |
| Step 9 | call-forward
                                                				  busy Example: Router(config-ephone-dn)# call-forward busy | (Optional)
                                             				Forwards incoming call if line is busy. Set this
                                                   					 command on the last ephone-dn in the overlay set only. |
| Step 10 | exit Example: Router(config-ephone-dn)# exit | Exits
                                             				ephone-dn configuration mode |
| Step 11 | ephone phone-tag Example: Router(config)# ephone 4 | Enters
                                             				ephone configuration mode. phone-tag —Unique sequence number that identifies
                                                   					 the phone to which you are adding an overlay set. |
| Step 12 | mac-address mac-address Example: Router(config-ephone)# mac-address 1234.5678.abcd | Specifies
                                             				the MAC address of the registering phone. |
| Step 13 | button button-number { o \| c } dn-tag , dn-tag [ , dn-tag ... ] button-number { x } overlay-button-number Example: Router(config-ephone)# button 1o15,16,17,18,19 2c20,21,22 3x1 4x1 | Creates a
                                             				set of ephone-dns overlaid on a single button. o —Overlay button.
                                                   					 Multiple ephone-dns share this button. A maximum of 25 ephone-dns can be
                                                   					 specified for a single button, separated by commas. c —Overlay button with
                                                   					 call-waiting. Multiple ephone-dns share this button. A maximum of 25 ephone-dns
                                                   					 can be specified for a single button, separated by commas. x —Separator that
                                                   					 creates a rollover button for an overlay button that was defined using the o keyword. When the
                                                   					 overlay button specified in this command is occupied by an active call, a
                                                   					 second call to one of its ephone-dns will be presented on this button. dn-tag —Unique
                                                   					 identifier previously defined with the ephone-dn command for the ephone-dn to be added to this
                                                   					 overlay set. overlay-button-number —Number of the overlay button that
                                                   					 should overflow to this button. Note that the button must have been defined
                                                   					 using the o keyword and not the c keyword. Note For other
                                                      				keywords, see the button command in the Cisco Unified Communications Manager Express
                                                         				  Command Reference . | Note | For other
                                                      				keywords, see the button command in the Cisco Unified Communications Manager Express
                                                         				  Command Reference . |
| Note | For other
                                                      				keywords, see the button command in the Cisco Unified Communications Manager Express
                                                         				  Command Reference . |
| Step 14 | end Example: Router(config-ephone)# end | Returns to
                                             				privileged EXEC mode. |

| Note | For other
                                                      				keywords, see the button command in the Cisco Unified Communications Manager Express
                                                         				  Command Reference . |
|---|---|

| Step 1 | Use the show running-config command or the show telephony-service ephone command to
                                          			 view button assignments. Router# show running-config ephone  5 description Cashier1 mac-address 0117.FBC6.1985 type 7960 button  1o4,5,6,200,201,202,203,204,205,206 2x1 3x1 |
|---|---|
| Step 2 | Use the show ephone overlay command to display the
                                          			 configuration and current status of registered overlay ephone-dns. |
| Step 3 | Use the show dialplan number command to display all
                                          			 the number resolutions of a particular phone number, which allows you to detect
                                          			 whether calls are going to unexpected destinations. This command is useful for
                                          			 troubleshooting cases in which you dial a number but the expected phone does
                                          			 not ring. |

| Restriction | The call
                                                   				  waiting, conferencing, hold, and transfer call features are not supported while
                                                   				  the Refer-Target is ringing. In a SIP to
                                                   				  SIP scenario, no ringback is heard by the Referee when Refer-Target is ringing. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | sip-ua Example: Router(config)# sip-ua | Enters SIP
                                             				user-agent configuration mode to configure the user agent. |
| Step 4 | refer-ood enable [ request-limit ] Example: Router(config-sip-ua)# refer-ood enable 300 | Enables OOD-R
                                             				processing. request-limit —Maximum number of concurrent
                                                   					 incoming OOD-R requests that the router can process. Range: 1 to 500. Default:
                                                   					 500. |
| Step 5 | exit Example: Router(config-sip-ua)# exit | Exits SIP
                                             				user-agent configuration mode. |
| Step 6 | voice register global Example: Router(config)# voice register global | Enters voice
                                             				register global configuration mode to set global parameters for all supported
                                             				SIP phones in a Cisco Unified CME or Cisco Unified SRST environment. |
| Step 7 | authenticate ood-refer Example: Router(config-register-global)# authenticate ood-refer | (Optional)
                                             				Enables authentication of incoming OOD-R requests using RFC 2617-based digest
                                             				authentication. |
| Step 8 | authenticate credential tag location Example: Router(config-register-global)# authenticate credential 1 flash:cred1.csv | (Optional)
                                             				Specifies the credential file to use for authenticating incoming OOD-R
                                             				requests. tag —Number that identifies the credential file to
                                                   					 use for OOD-R authentication. Range: 1 to 5. location —Name and location of the credential file
                                                   					 in URL format. Valid storage locations are TFTP, HTTP, and flash memory. |
| Step 9 | end Example: Router(config-register-global)# end | Exits to
                                             				privileged EXEC mode. |

| Step 1 | show running-config This command verifies your configuration. Example: Router# show running-config
!
voice register global
mode cme
source-address 10.1.1.2 port 5060
load 7971 SIP70.8-0-1-11S
load 7970 SIP70.8-0-1-11S
load 7961GE SIP41.8-0-1-0DEV
load 7961 SIP41.8-0-1-0DEV
authenticate ood-refer
authenticate credential 1 tftp://172.18.207.15/labtest/cred1.csv
create profile sync 0004550081249644
.
.
.
sip-ua
refer-ood enable |
|---|---|
| Step 2 | show sip-ua status refer-ood This command displays OOD-R configuration settings. Example: Router# show sip-ua status refer-ood

Maximum allow incoming out-of-dialog refer 500
Current existing incoming out-of-dialog refer dialogs: 1
outgoing out-of-dialog refer dialogs: 0 |

| Step 1 | Use the debug ccsip
                                                				  messages command to display the SIP messages exchanged between
                                          			 the SIP UA client and the router. |
|---|---|
| Step 2 | Use the debug voip application
                                                				  oodrefer command to display debugging messages for the OOD-R
                                          			 feature. |

| Note | The per agent
                                                			 statistics are displayed for both static and dynamic agents. |
|---|---|

| Note | The per agent statistics are displayed for both static and dynamic agents. |
|---|---|

| Feature Name | Cisco
                                          				  Unified CME version | Modification |
|---|---|---|
| Call Hunt | 3.4 | Added
                                          				  support for configuring call hunt features on SIP IP phones connected directly
                                          				  to Cisco Unified CME. |
| 3.0 | Preference for secondary numbers was introduced. Huntstop
                                                						was introduced. |
| 1.0 | Ephone-dn dial-peer preference was introduced. Huntstop
                                                						was introduced. |
| Call Pickup | 7.1 | Added Call
                                          				  Pickup support for SIP phones. |
| 4.0 | The
                                                						ability to globally disable directed call pickup was introduced. Feature
                                                						access codes for call pickup were introduced. The
                                                						ability to block call pickup on individual phones was introduced. |
| 3.2 | The ability
                                          				  to remove or rearrange soft keys on individual phones was introduced. |
| 3.0 | Call pickup
                                          				  groups were introduced. |
| Call Waiting | 8.0 | Added Cancel
                                          				  Call Waiting feature. |
| 3.4 | Added
                                          				  support for configuring call waiting for SIP phones directly connected to Cisco
                                          				  Unified CME. |
| Callback
                                          				  Busy Subscriber | 3.0 | Callback
                                          				  busy subscriber was introduced. |
| Hunt Groups | 12.2 | Introduced support for Shared Lines and Mixed Shared Lines (SIP and SCCP
                                          				  phones) on Parallel, Sequential, Peer, and Longest Idle Voice Hunt Groups. |
| 7.0/4.3 | Added
                                          				  support for the following: SCCP
                                                						phones in Voice Hunt-Groups Call
                                                						Forwarding to a Parallel Voice Hunt-Group (Blast Hunt Group) Call
                                                						Transfer to a Voice Hunt-Group Member
                                                						of Voice Hunt-Group can be a SCCP phone, FXS analog phone, DS0-group,
                                                						PRI-group, SIP phone, or SIP trunk |
| Hunt
                                          				  Groups | 4.0 | Added
                                          				  support for the following on IP phones running SCCP: Maximum number of hunt groups in a system was increased from 20
                                                						to 100 and maximum number of agents in a hunt group was increased from 10 to
                                                						20. Maximum number of hops automatically adjusts to the number of
                                                						agents. A
                                                						description can be added to phone displays and configuration output to provide
                                                						hunt group information associated with ringing and answered calls. A
                                                						configurable message can be displayed on agent phones when all agents are in
                                                						the not-ready status to advise the destination to which calls are being
                                                						forwarded or other useful information. No-answer timeouts can be set individually for each ephone-dn in
                                                						the list and a cumulative no-answer timeout can be set for all ephone-dns. Automatic logout trigger criterion was changed from exceeding
                                                						the specified timeout to exceeding the specified number of calls. The name of
                                                						this feature was changed from automatic logout to automatic agent status
                                                						not-ready. Dynamic hunt group membership is introduced. Agents can join and
                                                						leave hunt groups whenever a wildcard slot is available. Agent
                                                						status control using an HLog soft key or feature access code (FAC) is
                                                						introduced. Agents can put their lines into not-ready state to temporarily
                                                						block hunt group calls without relinquishing their slots in group. Calls
                                                						can be blocked from agent phones that are not idle or on hook. Calls
                                                						that are not answered by the hunt group can be returned to the party who
                                                						transferred them into the huntgroup. Calls
                                                						parked by hunt group agents can be returned to a different entry point. (Sequential hunt groups only) Local calls to a hunt group can be
                                                						restricted so that they will not be forwarded past the initial agent that is
                                                						rung. (Longest-idle
                                                						hunt groups only) A new command, the from-ring command, specifies that on-hook time stamps should be updated when a call rings
                                                						an agent and when a call is answered by an agent. |
| 3.4 | Added
                                          				  support for configuring hunt groups for SIP phones directly connected to Cisco
                                          				  Unified CME. |
| 3.2.1 | Maximum number of hunt groups in a system was increased to 20. Automatic logout capability was introduced. |
| 3.2 | Longest-idle hunt groups were introduced. |
| 3.1 | Secondary
                                          				  pilot numbers were introduced. |
| 3.0 | Peer and
                                          				  sequential ephone hunt groups were introduced. |
| Night
                                          				  Service | 11.6 | Night
                                          				  service support for mixed deployment of SIP and SCCP phone was introduced. |
| 11.5 | Night
                                          				  service support for SIP phone was introduced. |
| 4.0 | The night-service
                                                						everyday , night-service weekday , and night-service weekend commands were introduced. |
| 3.3 | The
                                          				  behavior of the night-service code was changed. Previously, using the
                                          				  night-service code at a phone either enabled or disabled night service for the
                                          				  ephone-dns on that phone. Now, using the night-service code at a phone enables
                                          				  or disables night service for all night-service ephone-dns. |
| 3.0 | Night
                                          				  service was introduced. |
| Overlaid Ephone-dns | 4.0 | The
                                                						number of ephone-dns that can be overlaid on a single button using the button command and the o or c keyword was increased from 10 to 25. The
                                                						ability to extend calls for overlaid ephone-dns to other buttons (rollover
                                                						buttons) on the same phone was introduced. Rollover buttons are created by
                                                						using the x keyword with the button command. The
                                                						number of waiting calls that can be displayed for overlaid ephone-dns that have
                                                						call waiting configured has been increased to six for the following phone
                                                						types: Cisco Unified IP Phone 7940G, 7941G, 7941G-GE, 7960G, 7961G, 7961G-GE,
                                                						7970G, and 7971G-GE. |
| 3.2.1 | Call
                                          				  waiting for overlaid ephone-dns was introduced and the c keyword was added to
                                          				  the button command. |
| 3.0 | Overlaid
                                          				  ephone-dns were introduced and the o keyword was added to the button command. |
| All Agents
                                          				  Logged Out Message for VHG Phones | 12.2 | Introduced
                                          				  support for all agents logged out display message for Cisco IP Phone 8800
                                          				  Series on Cisco 4000 Series Integrated Services Routers. |
| Agent
                                          				  Status Control | 12.2 | Agent
                                          				  Status Control enhancements was supported. |
| Voice Hunt
                                          				  Group Enhancements | 11.6 | Hlog
                                          				  Softkey support for SIP Phones was introduced. |
| 9.0 | Allows all
                                          				  ephone and voice hunt group call statistics to be written to a file using the hunt-group statistics
                                                						write-all command. |
| Preventing
                                          				  Local-Call Forwarding to Final Agent in Voice Hunt Groups | 9.5 | The no forward
                                                						local-calls command was introduced in ephone-hunt group to
                                          				  prevent a local call from being forwarded to the next agent. |
| Enhancement of Support for Hunt Group | 9.5 | Hunt group
                                          				  agent statistics of Cisco Unified SCCP IP phones is enhanced to include Total
                                          				  logged in time and Total logged out. |
| Total
                                          				  Logged in and Logged out Time Statistics for agent | 9.5 | Allows all
                                          				  ephone hunt call statistics to be written to a file along with total logged in
                                          				  and logged out time for agents using the hunt-group statistics
                                                						write-v2 command. |
| Enhancement of Support for Total Logged in and Logged out Time
                                          				  Statistics for Agent | 11.5 | Allows all
                                          				  voice hunt call statistics to be written to a file along with total logged in
                                          				  and logged out time for agents using the hunt-group statistics
                                                						write-v2 command. |
| Out-of-Dialog Refer | 4.1 | Out-of
                                          				  Dialog REFER support was added. |