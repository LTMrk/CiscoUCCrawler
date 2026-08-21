---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmepark-html-898fc0a678
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmepark.html
retrieved_at: 2026-08-21T07:24:42.224129+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Call Park

## Chapter: Call Park

# Call Park

## Information About Call Park

### Call Park
                           	 Enhancements in Cisco Unified CME 7.1

Cisco Unified CME 7.1 adds Call Park support for SIP phones,
                              		introduces Park Reservation Groups, and enhances the Directed Call Park
                              		feature. Park slots can be shared among SCCP and SIP phones. For example, a
                              		call parked on a SCCP phone can be retrieved by a SIP phone on the same
                              		Cisco Unified CME router. Call Park features are available on SCCP and SIP
                              		phones that support the Park soft key. The Park soft key displays on supported
                              		phones by default.

Table describes how
                              		phone users park and retrieve calls in Cisco Unified CME 7.1 and later versions
                              		compared to previous versions. For SCCP phones, the only change is in how users
                              		perform Directed Call Park Retrieval. The Call Park method supported in
                              		previous versions of Cisco Unified CME is enabled by default. You can change
                              		the park and retrieval method only when there are no parked calls.

Feature

Cisco Unified CME 7.1 and Later Versions (SCCP and SIP
                                          					 Phones) 1

Before
                                          					 Cisco Unified CME 7.1 (SCCP Phones Only)

Call Park
                                          					 (Basic)

Press Park
                                          					 soft key to park the call.

Press Park
                                          					 soft key to park the call.

Call Park
                                          					 Retrieval 2

Do one of
                                          					 the following:

Dial
                                                						  the park slot extension (SCCP and SIP).

Press
                                                						  Pickup soft key and dial park-slot extension (SCCP only).

Press
                                                						  Pickup soft key and the asterisk (*) on phone that parked the call (SCCP only).

Do one of
                                          					 the following:

Dial
                                                						  the park slot extension.

Press
                                                						  Pickup soft key and dial park-slot extension.

Press
                                                						  Pickup soft key and the asterisk (*) on phone that parked the call.

Directed
                                          					 Call Park

Press
                                          					 Transfer soft key and dial park-slot extension.

Press
                                          					 Transfer soft key and dial park-slot extension.

Directed
                                          					 Call Park Retrieval

Dial the
                                          					 retrieval FAC and park-slot extension.

Same as
                                          					 Basic Call Park Retrieval.

To enable Call Park
                              		features, see Enable Call Park or Directed Call Park .

### Basic Call
                           	 Park

The Call Park
                              		feature allows a phone user to place a call on hold at a special extension so
                              		it can be retrieved from any other phone in the system. A user parks the call
                              		at the extension, known as the call-park slot, by pressing the Park soft key. Cisco Unified CME chooses the next
                              		available call-park slot and displays that number on the phone. A user on
                              		another phone can then retrieve the call by dialing the extension number of the
                              		call-park slot.

You can define
                              		either a single extension number or a range of extension numbers to use as
                              		call-park slots. Each call-park slot can hold one call at a time so the number
                              		of calls that users can park is equal to the number of slots you create. If the
                              		secondary number is used to group calls together, calls are retrieved in the
                              		order in which they were parked; the call that has been parked the longest is
                              		the first call retrieved from the call-park slot.

A caller who is parked in a park slot hears the music-on-hold (MOH) audio stream if the call uses the G.711 codec or if the
                              call uses G.729 with transcoding; otherwise, callers hear a tone on hold. Users who attempt to park a call at a busy slot
                              hear a busy tone.

Call-park slots can
                              		also be monitored by assigning the call-park slot to a monitor button using the button m command. The line status shows “in use” when a call is parked in the monitored
                              		slot. A call that is parked on the monitored call-park slot can be picked up by
                              		pressing the assigned monitor button.

You can create a
                              		call-park slot that is reserved for use by one extension by assigning that slot
                              		a number whose last two digits are the same as the last two digits of the
                              		extension. When an extension starts to park a call, the system searches first
                              		for a call-park slot that has the same final two digits as the extension. If no
                              		such call-park slot exists, the system chooses an available call-park slot.

Multiple call-park
                              		slots can be created with the same extension number so that more than one call
                              		can be parked for a particular department or group of people at a known
                              		extension number. For example, at a hardware store, calls for the plumbing
                              		department can be parked at extension 101, calls for lighting can be parked at
                              		102, and so forth. Everyone in the plumbing department knows that calls parked
                              		at 101 are for them and can pick up calls from extension 101. When multiple
                              		calls are parked at the same call-park slot number, they are picked up in the
                              		order in which they were parked; that is, the call that has been parked the
                              		longest is the first call picked up from that call-park slot number.

If multiple
                              		call-park slots use the same extension number, you must configure each
                              		ephone-dn that uses the extension number with the no huntstop command, except for the last
                              		ephone-dn to which calls are sent. In addition, each ephone-dn must be
                              		configured with the preference command. The preference numeric values must increase to match the order of the
                              		ephone-dns. That is, the lowest ephone-dn tag park-slot must have the lowest
                              		numeric preference number, and so forth. Without the configuration of the preference and huntstop commands, all calls that are parked after a second call has been parked will
                              		generate a busy signal. The caller who is being transferred to park will hear a
                              		busy signal, while the phone user who parked the call will receive no
                              		indication that the call was lost.

A reminder ring can
                              		be sent to the extension that parked the call by using the timeout keyword with the park-slot command. The timeout keyword and argument set the interval length during which the call-park
                              		reminder ring is timed out or inactive. If the timeout keyword is not used, no reminder ring is sent to the extension that parked the
                              		call. The number of timeout intervals and reminder rings are configured with
                              		the limit keyword
                              		and argument. For example, a limit of 3 timeout intervals sends 2 reminder
                              		rings (interval 1, ring 1, interval 2, ring 2, interval 3). The timeout and limit keywords and arguments also set the maximum time that calls stay parked. For
                              		example, a timeout interval of 10 seconds and a limit of 5 timeout intervals
                              		( park-slot timeout 10 limit
                                    			 5 ) will park calls for approximately 50 seconds.

The reminder ring is
                              		sent only to the extension that parked the call unless the notify keyword is also used to specify an additional extension number to receive a
                              		reminder ring. When an additional extension number is specified using the notify keyword, the phone user at that extension can retrieve a call from this slot by
                              		pressing the PickUp soft key and the asterisk (*) key.

You can define both
                              		the length of the timeout interval for calls parked at a call-park slot and the
                              		number of timeout intervals that should occur before the call is either
                              		recalled or transferred. If you specify a transfer target in the park-slot command, the call is transferred to the specified target after the timeout
                              		intervals expire rather than to the primary number of the parking phone.

If a name has been
                              		specified for the call-park slot using the name command,
                              		that name will be displayed on a recall or transfer rather than an extension
                              		number.

You can also specify
                              		an alternate target extension at which to transfer a parked call if the recall
                              		or transfer target is in use (ringing or connected). For example, a call is
                              		parked at the private park slot for the phone with the primary extension of
                              		2001, as shown in Dedicated Call
                                 		  Park Example . After the timeouts expire, the system attempts to recall the call to
                              		extension 2001, but that line is connected to another call. The system then
                              		transfers the call to the alternate target, extension 3784.

### View Active Parked
                           	 Calls

You can view the
                              		list of active parked calls on SIP and SCCP phones using the phone menu by
                              		pressing the Service button on the phone and navigating to My Phone
                                    			 Apps > Park List .

To recall a call
                              		from the list of parked calls, you can select the desired call and press the Pickup soft key.

To refresh the list
                              		of parked calls you can press the Update soft key in the menu.

Latest parked call
                              		will be displayed on top of the list.

This feature can
                                          		  be configured as PLK button for SCCP and SIP Phone. For more information see Configure Feature Button on a Cisco Unified SCCP Line Key and Configure Feature Button on a Cisco Unified SIP Phone Line Key .

### Configure User
                           	 Interface to View Active List of Parked Calls

This feature
                                 		  enables a user to view the list of active parked calls and is enabled by
                                 		  default.

You must perform
                                             			 this task only if the feature was previously disabled on a phone.

This feature is enabled by default for SCCP and SIP phones. For SCCP phones, this feature can be enabled and disabled. However,
                                             SIP phones do not have the enable or disable option.

Restriction

If there are more than 20 active calls parked, then only the first 20 active parked calls will be displayed.

Dedicated, private call-park slots configured using the reserved-for command are not supported on the phone’s display.

#### Before you begin

Cisco Unified
                                       				CME 10.5 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- ephone phone-tag

- phone-ui park-list

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
Router(config)# ephone 12
```

Enters ephone
                                             				configuration mode.

phone-tag —Unique number that identifies this
                                                   					 ephone during configuration tasks.

Step 4

phone-ui park-list

#### Example:

```
Router(config-ephone)# phone-ui park-list
```

Enables a
                                             				phone user to view the list of active parked calls.

This
                                                   					 command is enabled by default.

Step 5

end

#### Example:

```
Router(config-ephone)# end
```

Exits to
                                             				privileged EXEC mode.

### Directed Call
                           	 Park

The Directed Call
                              		Park feature allows a phone user to transfer a call to a specific call-park
                              		slot using the Transfer soft key. For example, a customer calls a retail store
                              		and asks for the sporting goods department. The operator who answers the call
                              		transfers the call to one of the park-slots associated with the sporting goods
                              		department and pages the sporting goods department to retrieve the call. You
                              		can configure phones that support the directed call-park Busy Lamp Field (BLF)
                              		to monitor the busy and idle status of specific directed call-park slots.

In versions before
                              		Cisco Unified CME 4.0, callers can directly dial call-park slot numbers to be
                              		placed in park. If another call is already parked in the slot, the caller hears
                              		a busy tone.

In Cisco Unified CME
                              		4.0 to Cisco Unified CME 7.0, users retrieve a call from a directed call-park
                              		slot by dialing the park-slot extension or using the PickUp soft key and
                              		dialing the park-slot extension. If no call is parked in the slot, the caller
                              		hears a busy tone.

In Cisco Unified CME
                              		7.1 and later versions, users retrieve a call from a directed call-park slot by
                              		dialing a feature access code (FAC) and the number of the call-park slot.

Cisco Unified CME
                              		supports Directed Call Park from remote phones, however only phones that are
                              		local to the directed call-park slot can retrieve a call.

### Park Reservation Groups

Cisco Unified CME 7.1 and later versions allow you to assign ownership
                              		to call-park slots by using Park Reservation Groups. A park slot configured
                              		with a park reservation group can only be used by phones configured with the
                              		same park reservation group. A park slot without a park reservation group can
                              		be used by any phone not assigned to a park reservation group.

In versions earlier than Cisco Unified CME 7.1, you could reserve a
                              		dedicated call-park slot for a specific phone based on its primary line. All
                              		lines on that phone could use the dedicated park slot. The new Park Reservation
                              		Group feature in Cisco Unified CME 7.1 provides an enhanced method of reserving
                              		park slots that replaces the use of dedicated park slots.

Park reservation groups are not supported for directed call-park slots.

The reservation-group is used so that the phone with a reservation
                                          		  group is allowed to park to park-slot(s) within the same reservation group.

Any phone within the same CME can retrieve any parked calls. So the
                                          		  rule is applied when you park the call, not when you retrieve the call.

### Dedicated
                           	 Call-Park Slots

A dedicated, private
                              		call-park slot can be configured for an ephone using the reserved-for keyword in the park-slot command. The dedicated call-park slot is associated with the primary extension
                              		of the ephone. All extensions on this phone can park calls in the dedicated
                              		park slot. The extensions on this phone are the only extensions that can park a
                              		call in the dedicated park slot. Only one call at a time can be parked in a
                              		park slot; a busy tone is returned to any attempt to park a call in a slot that
                              		is already in use.

Calls can be parked
                              		in dedicated call-park slots using any of the following methods (the extension
                              		doing the parking must be on a phone whose primary extension is associated with
                              		a dedicated park slot).

With an active
                                       			 call, an IP phone user presses the Park soft key.

With an active
                                       			 call, an IP phone user presses the Transfer soft key and a standard or custom
                                       			 FAC (feature access code) for the call-park feature. The standard FAC for call
                                       			 park is **6.

With an active
                                       			 call, an analog phone user presses hookflash and the standard or custom FAC for
                                       			 the call park feature.

An IP phone user
                                       			 presses the Pickup soft key and dials the park-slot number.

An IP phone user
                                       			 presses the New Call soft key and dials the park-slot number.

An analog phone
                                       			 user lifts the handset, presses the standard or custom FAC for directed call
                                       			 pickup, and dials the park-slot number. The standard FAC for directed pickup is
                                       			 **5.

If no dedicated park
                              		slot is found anywhere in the Cisco Unified CME system for an ephone-dn that is
                              		attempting to park a call, the system uses the standard call-park procedure;
                              		that is, the system searches for a preferred park slot (one with an ephone-dn
                              		number that matches the last two digits of the ephone-dn attempting to park the
                              		call) and if none is found, uses any available call-park slot.

Dedicated Call
                                 		  Park Example shows
                              		an example of a dedicated call-park slot.

If the configuration
                              		specifies that a call should be recalled to the parking phone after the timeout
                              		intervals expire, the call is always returned to the phone’s primary extension
                              		number, regardless of which extension on the phone did the parking. Dedicated Call
                                 		  Park Example shows
                              		an ephone that is configured with the extension numbers 2001, 2002, and 2003,
                              		and a private call-park slot at extension 3333. The private park slot has been
                              		set up to recall calls to the parking phone when the parked call’s timeouts
                              		expire. In the example, extension 2003 parks a call using the Park soft key.
                              		When the timeout intervals expire, the call rings back on extension 2001.

The configuration in Dedicated Call
                                 		  Park Example specifies that the call will recall or transfer from the park slot after 3
                              		times the 60-second timeout, or after 180 seconds. Also, before the exhaustion
                              		of the 3 timeouts the phone will receive reminder notifications that a parked
                              		call is waiting. The reminders are sent after each 60-second timeout interval
                              		expires (that is, at 60 seconds and at 120 seconds). You may want to set the timeout command with a limit of 1 instead, so that the call simply parks and recalls or
                              		transfers without sending a reminder ring.

### Call-Park
                           	 Blocking

In Cisco Unified CME
                              		4.0 and later versions, individual ephones can be prevented from making
                              		transfers to call-park slots by using the transfer-park
                                    			 blocked command. This command prevents transfers to park that use
                              		the Transfer soft key and a call-park slot number, while allowing call-parks
                              		that use only the Park soft key. (To prevent use of the Park soft key, use an
                              		ephone template to remove it from the phone. See Customize Softkeys .)

An exception is made
                              		for phones with reserved, or dedicated, park slots. If the transfer-park
                                    			 blocked command is used on an ephone that has a dedicated park
                              		slot, the phone is blocked from parking calls at park slots other than the
                              		phone’s dedicated park slot but can still park calls at its own dedicated park
                              		slot.

### Call-Park Redirect

By default, H.323 and SIP calls that use the call-park feature use
                              		hairpin call forwarding or transfer to park calls and to pick up calls from
                              		park. The call-park system redirect command allows you to
                              		specify that these calls should use H.450 or the SIP Refer method of call
                              		forwarding or transfer. The no form of the command returns the system to
                              		the default behavior.

### Call Park Recall
                           	 Enhancement

In Cisco Unified CME
                              		9.5 and lower versions, a parked call could not be recalled by or transferred
                              		to the phone that put the call in park or the original phone that transferred
                              		the call when the destination phone was offhook or ringing.

In Cisco Unified CME
                              		9.5, the recall force keyword is added to the call-park
                                    			 system command in telephony-service configuration mode to allow a
                              		user to force the recall or transfer of a parked call to the phone that put the
                              		call in park or the phone with the reserved-for number as its primary DN when
                              		the destination phone is available to answer the call. For more configuration
                              		examples, see Example for Configuring Call Park Recall .

Prior to Unified CME 10.5, the ring tones for Call Park Recall and incoming calls were the same. In Unified CME 10.5, a new
                              ring tone is introduced for park recall to assist the user to distinctly identify the type of call. No configurations are
                              required to activate this feature. The ringtone for SCCP endpoints is a feature-ring and for SIP endpoints the ringtone is
                              a Bellcore-dr2.

The Distinctive Call Park Recall feature is supported on all phone families for SCCP endpoints. For SIP phones, the feature
                              is supported on Cisco IP Phone 7800 Series,  8900 Series and 9900 Series phones.

Cisco IP Phone 8800 Series phones do not support Distinctive Call Park Recall feature.

### Park Monitor

In Cisco Unified CME 8.5 and later versions, the park monitor feature
                              		allows you to park a call and monitor the status of the parked call until the
                              		parked call is retrieved or abandoned. When a Cisco Unified SIP IP Phone 8961,
                              		9951, or 9971 parks a call using the park soft key, the park monitoring feature
                              		monitors the status of the parked call. The park monitoring call bubble is not
                              		cleared until the parked call gets retrieved or is abandoned by the parkee.
                              		This parked call can be retrieved using the same call bubble on the parker’s
                              		phone to monitor the status of the parked call.

Once a call is parked, Cisco Unified CME sends a SIP NOTIFY message to
                              		the parker phone indicating the “parked” event along with the park slot number
                              		so that the parker phone can display the park slot number as long as the call
                              		remains parked.

When a parked call is retrieved, Cisco Unified CME sends another SIP
                              		NOTIFY message to the parker phone indicating the “retrieved” event so that the
                              		phone can clear the call bubble. When a parked call is disconnected by the
                              		parkee, Cisco Unified CME sends a SIP NOTIFY message to the parker phone
                              		indicating the “abandoned” event and the parker phone clears the call bubble
                              		upon cancellation of the parked call.

When a parked call is recalled or transferred, Cisco Unified CME sends a
                              		SIP NOTIFY message to the parker phone indicating the “forwarded” event so that
                              		parker phone can clear the call bubble during park, recall, and transfer. You
                              		can also retrieve a parked call from the parker phone by directly selecting the
                              		call bubble or pressing the resume soft key on the phone.

Park Monitor is supported in Cisco IP Phone 7800 Series and Cisco Unified IP Phone 9900 Series. However, Cisco IP Phone 8800
                                          Series do not support Park Monitor feature.

## Configure Call Park

### Enable Call Park
                           	 or Directed Call Park

To enable Call
                                 		  Park on SCCP or SIP phones, perform the following steps.

Restriction

For SIP
                                                   				  phones, the Park soft key is not supported for Cisco Unified IP Phone 7905,
                                                   				  7912, 7921, 7940, or 7960.

Park
                                                   				  Retrieval is supported only on local phones. Phones can park calls remotely to
                                                   				  another Cisco Unified CME router but only phones that are registered to the
                                                   				  local router hosting the call-park slots can retrieve a call.

In versions
                                                   				  earlier than Cisco Unified CME 7.1, Call Park and Directed Call Park shared the
                                                   				  same call-park slots. In Cisco Unified CME 7.1 and later versions, if a user
                                                   				  attempts to transfer a call to a basic park slot when using Directed Call Park,
                                                   				  Cisco Unified CME considers that a Park Retrieval.

A user can
                                                   				  retrieve a parked call on an SCCP phone by pressing the PickUp soft key and
                                                   				  dialing the extension number of the call-park slot or an asterisk (*) only if
                                                   				  the service directed-pickup command is enabled
                                                   				  (default). Otherwise this initiates a local group pickup.

Park
                                                   				  Reservation Groups are not supported with Directed Call Park.

Different
                                                   				  directory numbers with the same extension number must have the same Call Park
                                                   				  configuration.

Calls from
                                                   				  H.323 trunks are not supported on SIP phones.

Hold Pickup
                                                   				  is not supported with the call-park system
                                                         						application command.

#### Before you begin

SIP phones
                                          				require Cisco Unified CME 7.1 or a later version.

IP phone must
                                          				support the Park soft key. The Park soft key displays by default on supported
                                          				SCCP and SIP phones. If previously disabled, you must use the softkeys connected command to enable the Park soft key.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- call-park system { application | redirect }

- fac { standard | custom dpark-retrieval custom-fac }

- exit

- ephone-dn dn-tag [ dual-line ]

- number number [ secondary number ] [ no-reg [ both | primary ]]

- park-slot [ directed ] [ reservation-group group-number ] [ reserved-for extension-number ] [[ timeout seconds limit count ][ notify extension-number [ only ]] [ recall ][ transfer extension-number ][ alternate extension-number ] [ retry seconds limit count ]]

- exit

- ephone phone-tag or voice register pool phone-tag

- park reservation-group group-number

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

call-park system { application | redirect }

#### Example:

```
Router(config-telephony)# call-park system application
```

Defines system
                                             				parameters for the Call Park feature.

application —Enables the Call Park and Directed
                                                   					 Call Park features supported in Cisco Unified CME 7.1 and later versions.

redirect —Specifies that H.323 and SIP calls use
                                                   					 H.450 or the SIP Refer method of call forwarding or transfer to park calls and
                                                   					 pick up calls from park.

Step 5

fac { standard | custom dpark-retrieval custom-fac }

#### Example:

```
Router(config-telephony)# fac custom dpark-retrieval #25
```

Enables
                                             				standard FACs or creates a custom FAC or alias for the Directed Park Retrieval
                                             				feature on SCCP and SIP phones.

Enable
                                                   					 this command to use the Directed Park Retrieval feature in
                                                   					 Cisco Unified CME 7.1 and later versions.

standard —Enables standard FACs for all phones.
                                                   					 Standard FAC for Park Retrieval is **10.

custom —Creates a custom FAC for a feature.

custom-fac —User-defined code to dial using the
                                                   					 keypad on an IP or analog phone. Custom FAC can be up to 256 characters and
                                                   					 contain numbers 0 to 9 and * and #.

Step 6

exit

#### Example:

```
Router(config-telephony)# exit
```

Returns to
                                             				privileged EXEC mode.

Step 7

ephone-dn dn-tag [ dual-line ]

#### Example:

```
Router(config)# ephone-dn 1
```

Enters
                                             				ephone dn configuration mode to define a directory number for an IP phone,
                                             				intercom line, voice port, or a message-waiting indicator (MWI).

dn-tag —identifies a particular directory number
                                                   					 during configuration tasks. Range is 1 to the maximum number of directory
                                                   					 numbers allowed on the router platform. Type ? to display the range.

Step 8

number number [ secondary number ] [ no-reg [ both | primary ]]

#### Example:

```
Router(config-ephone-dn)# number 3001
```

Associates
                                             				an extension number with this directory number.

number —String of up to 16 digits that represents
                                                   					 an extension or E.164 telephone number.

The
                                                         				  primary number must be unique for call-park slots.

Step 9

park-slot [ directed ] [ reservation-group group-number ] [ reserved-for extension-number ] [[ timeout seconds limit count ][ notify extension-number [ only ]] [ recall ][ transfer extension-number ][ alternate extension-number ] [ retry seconds limit count ]]

#### Example:

```
Router(config-ephone-dn)# park-slot directed
```

Creates an
                                             				extension (call-park slot) at which calls can be temporarily held (parked).

directed —(Optional) Enables Directed Call Park
                                                   					 using this extension. This keyword is supported in Cisco Unified CME 7.1 and
                                                   					 later versions.

reservation-group group-number —(Optional) Reserves this slot for
                                                   					 phones configured with the specified reservation group. This is the group
                                                   					 assigned to the phone in Step 12. This keyword is supported in Cisco Unified
                                                   					 CME 7.1 and later versions.

reserved-for extension-number —(Optional) Reserves this slot as
                                                   					 a private park-slot for the phone with the specified extension number as its
                                                   					 primary line.

The reservation-group and reserved-for keywords are mutually exclusive. If
                                                         				  you use the reservation-group keyword, the reserved-for keyword is ignored. The reservation-group is used so
                                                         				  that the phone with a reservation group is allowed to park to park-slot(s)
                                                         				  within the same reservation group. Any phone within the same CME can retrieve
                                                         				  any parked calls. So the rule is applied when you park the call, not when you
                                                         				  retrieve the call.

Step 10

exit

#### Example:

```
Router(config-ephone-dn)# exit
```

Exits
                                             				configuration mode.

Step 11

ephone phone-tag or voice register pool phone-tag

#### Example:

```
Router(config)# ephone 1
```

or

```
Router(config)# voice register pool 1
```

Enters
                                             				ephone configuration mode to set phone-specific parameters for an SCCP phone.

or

Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone.

phone-tag —Unique sequence number that identifies
                                                   					 the phone. Range is version and platform-dependent; type ? to display range.

Step 12

park reservation-group group-number

#### Example:

```
Router(config-ephone)# park reservation-group 1
```

or

```
Router(config-register-pool)# park reservation-group 1
```

(Optional)
                                             				Assigns a call-park reservation group to a phone.

group-number —Unique number that identifies the
                                                   					 reservation group. String can contain up to 32 digits.

This
                                                   					 command can also be configured in ephone-template or voice register template
                                                   					 configuration mode and applied to one or more phones. The phone configuration
                                                   					 has priority over the template configuration.

This
                                                   					 command is supported in Cisco Unified CME 7.1 and later versions.

Step 13

end

#### Example:

```
Router(config-ephone)# end
```

or

```
Router(config-register-pool)# end
```

Exits
                                             				configuration mode.

#### Examples for
                                 		  Basic Call Park, Directed Call Park and Park Reservation Groups

Basic Call
                                    			 Park

The following
                                 		  example shows three basic call-park slots that can be used by either SCCP or
                                 		  SIP phones. Any phone can retrieve calls parked at these extensions.

```
ephone-dn  23 
			  number 8123 
			  park-slot timeout 10 limit 2 recall 
			  description park slot for Sales
			 !
			 ephone-dn  24
			  number 8124
			  park-slot timeout 10 limit 2 recall 
			  description park slot for Sales
			 !
			 ephone-dn  25
			  number 8125
			  park-slot timeout 15 limit 3 recall retry 10 limit 2
			  description park slot for Service
```

Directed Call
                                    			 Park

The following
                                 		  example shows that the enhanced Call Park and Directed Call Park features in
                                 		  Cisco Unified CME 7.1 and later versions is enabled with the call-park system
                                       				application command in telephony-service configuration mode. Two
                                 		  call-park slots, extension 3110 and 3111, can be used to park calls for the
                                 		  pharmacy using Directed Call Park.

```
telephony-service 
			  load 7960-7940 P00308000500 
			  max-ephones 100 
			  max-dn 240 
			  ip source-address 10.7.0.1 port 2000 
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
			 ephone-dn  10 
			  number 3110 
			  park-slot directed 
			  description park-slot for Pharmacy 
			 ! 
			 ephone-dn  11 
			  number 3111 
			  park-slot directed 
			  description park-slot for Pharmacy
```

Park
                                    			 Reservation Groups

The following
                                 		  example shows park reservation groups set up for two call-park slots. Extension
                                 		  8126 is configured for group 1 and assigned to phones 3 and 4. Extension 8127
                                 		  is configured for group 2 and assigned to phones 10 and 11. When calls for the
                                 		  Pharmacy are parked at extension 8126, only phones 3 and 4 can retrieve them.

```
ephone-dn  26 
			  number 8126 
			  park-slot reservation-group 1 timeout 15 limit 2 transfer 8100 
			  description park slot for Pharmacy 
			 ! 
			 ephone-dn  27 
			  number 8127 
			  park-slot reservation-group 2 timeout 15 limit 2 transfer 8100 
			  description park slot for Auto 
			 ! 
			 ! 
			 ephone  3 
			  park reservation-group 1 
			  mac-address 002D.264E.54FA 
			  type 7962 
			  button  1:3 
			 ! 
			 ! 
			 ephone  4 
			  park reservation-group 1 
			  mac-address 0030.94C3.053E 
			  type 7962 
			  button  1:4 
			 ! 
			 ! 
			 ephone  10 
			  park reservation-group 2 
			  mac-address 00E1.CB13.0395 
			  type 7960 
			  button  1:10 
			 ! 
			 ! 
			 ephone  11 
			  park reservation-group 2 
			  mac-address 0016.9DEF.1A70 
			  type 7960 
			  button  1:11
```

### Verify Call
                           	 Park

Step 1

Use the show
                                                				  running-config command to verify your configuration. Call-park
                                          			 slots are listed in the ephone-dn portion of the output.

#### Example:

```
Router# show running-config !
			 ephone-dn  23
			  number 853
			  park-slot timeout 10 limit 1 recall
			  description park slot for Sales
			 !
			 !
			 ephone-dn  24
			  number 8126
			  park-slot reserved-for 126 timeout 10 limit 1 transfer 8145
			 !
			 !
			 ephone-dn  25
			  number 8121 secondary 121
			  park-slot reserved-for 121 timeout 30 limit 1 transfer 8145
			 !
			 !
			 ephone-dn  26
			  number 8136 secondary 136
			  park-slot reserved-for 136 timeout 10 limit 1 recall
			 !
			 !
			 ephone-dn  30  dual-line
			  number 451 secondary 501
			  preference 10
			  huntstop channel
			 !
			 !
			 ephone-dn  31  dual-line
			  number 452 secondary 502
			  preference 10
			  huntstop channel
			 !
```

Step 2

Use the show telephony-service ephone-dn command to display call park
                                          			 configuration information.

#### Example:

```
Router# show telephony-service ephone-dn ephone-dn  26
		   number 8136 secondary 136
		   park-slot reserved-for 136 timeout 10 limit 1 recall
```

### Configure Timeout
                           	 Duration for Recalled Calls

To set a timeout
                                 		  duration for no response for a recalled call, perform the following steps. This
                                 		  command is also applicable to all IP phones where a call in ringing state if
                                 		  not answered, is automatically disconnected after the timeout duration.

This feature is
                                 		  enabled by default. You must perform this task only if the feature was
                                 		  previously disabled on a phone.

#### Before you begin

Cisco Unified CME
                                 		  10.5 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- ephone ring timeouts seconds

- exit

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

ephone ring timeouts seconds

#### Example:

```
Router(config)# ring timeout 25
```

Enters a
                                             				timeout period before disconnecting the call.

Step 4

exit

#### Example:

```
Router(config-ephone)# exit
```

Exits to
                                             				privileged EXEC mode.

#### Example

The following
                                 		  example shows that the ring timeouts command is enabled on phone:

```
ephone-dn 10 dual-line
number 1001
no huntstop
huntstop channel
ephone-dn 11 dual-line
```

### Troubleshooting
                           	 Call Park

Step 1

show ephone-dn park

Use this
                                             				command to display configured call-park slots and their status.

```
Router# show ephone-dn park DN 50 (1560) park-slot state IDLE
Notify to () timeout 30 limit 10
```

Step 2

Use the debug ephone commands to observe messages and states associated with an ephone. For more
                                          			 information, see Cisco Unified CME Command
                                             				Reference .

## Configuration Examples for Call Park

### Example for Configuring Basic Call Park

The following example creates a call-park slot with the number 1560.
                                 		  After a call is parked at this number, the system provides 10 reminder rings at
                                 		  intervals of 30 seconds to the extension that parked the call.

```
ephone-dn 50
number 1560
park-slot timeout 30 limit 10
```

### Example for Blocking Phone From Using Call Park

The following example prevents ephone 25 and extensions 234, 235, and
                                 		  236 from parking calls at any call-park slots.

```
ephone-dn 11
		 number 234
		
		ephone-dn 12
		 number 235
		
		ephone-dn 13
		 number 236
		 
		ephone 25
		 button 1:11 2:12 3:13
		 transfer-park blocked
```

The following example sets up a dedicated park slot for the extensions
                                 		  on ephone 6 and blocks transfers to call park from extensions 2977, 2978, and
                                 		  2979 on that phone. Those extensions can still park calls at the phone’s
                                 		  dedicated park slot by using the Park soft key or the Transfer soft key and the
                                 		  FAC for call park.

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

### Example for Configuring Call-Park Redirect

The following example specifies that H.323 and SIP calls that are
                                 		  parked should use H.450 or the SIP Refer method to when they are parked or
                                 		  picked up.

```
telephony-service
call-park system redirect
```

### Example for Configuring Call Park Recall

The following example shows how to force the recall of a call
                                 		  previously parked when the phone was busy:

```
Router# configure terminal
Router(config)# telephony-service
Router(config-telephony)# call-park system ?
recall       Configure parameters for recall
Router(config-telephony)# call-park system recall ?
force  Force recall for busy call park initiator
Router(config-telephony)# call-park system recall force
```

## Where to Go
                        	 Next

### Controlling
                              		  Use of the Park Soft Key

To block the
                              		  functioning of the call park (Park) soft key without removing the key display,
                              		  create and apply an ephone template that contains the features
                                    				blocked command. For more information, see Customize Softkeys .

To remove the call
                              		  park (Park) soft key from one or more phones, create and apply an ephone
                              		  template that contains the appropriate softkeys command. For more information, see Customize Softkeys .

### Ephone
                              		  Templates

The transfer-park
                                    				blocked command, which blocks transfers to call-park slots, can
                              		  be included in ephone templates that are applied to individual ephones.

The Park soft key
                              		  can be removed from the display of one or more phones by including the
                              		  appropriate softkeys command in an ephone template and applying the template to individual ephones.

For more
                              		  information, see Templates .

### Feature Access
                              		  Codes

Dedicated park
                                       				slot—Standard FAC is **6.

Any available
                                       				park slot—Standard FAC is **6 plus optional park-slot number.

For
                              		  more information about FACs, see Feature Access Codes .

## Feature
                        	 Information for Call Park

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature
                                          					 Name

Cisco Unified CME Version

Feature
                                          					 Information

Call Park
                                          					 Recall Enhancement

9.5

Added
                                          					 recall force keyword to the call-park system command.

Call Park

8.5

Support
                                          					 for Park Monitor was introduced.

7.1

Adds Call
                                          					 Park support for SIP phones, introduces Park Reservation Groups, and enhances
                                          					 Directed Call Park.

4.0

Dedicated
                                          					 call-park slots, alternative recall locations, and call-park blocking were
                                          					 introduced. Direct calls to park slots are now interpreted as attempts to pick
                                          					 up parked calls rather than attempts to be parked at the slot.

3.2.1

Monitoring
                                          					 of call-park slots was introduced.

3.1

Call park
                                          					 was introduced.

| Feature | Cisco Unified CME 7.1 and Later Versions (SCCP and SIP
                                          					 Phones) 1 | Before
                                          					 Cisco Unified CME 7.1 (SCCP Phones Only) |
|---|---|---|
| Call Park
                                          					 (Basic) | Press Park
                                          					 soft key to park the call. | Press Park
                                          					 soft key to park the call. |
| Call Park
                                          					 Retrieval 2 | Do one of
                                          					 the following: Dial
                                                						  the park slot extension (SCCP and SIP). Press
                                                						  Pickup soft key and dial park-slot extension (SCCP only). Press
                                                						  Pickup soft key and the asterisk (*) on phone that parked the call (SCCP only). | Do one of
                                          					 the following: Dial
                                                						  the park slot extension. Press
                                                						  Pickup soft key and dial park-slot extension. Press
                                                						  Pickup soft key and the asterisk (*) on phone that parked the call. |
| Directed
                                          					 Call Park | Press
                                          					 Transfer soft key and dial park-slot extension. | Press
                                          					 Transfer soft key and dial park-slot extension. |
| Directed
                                          					 Call Park Retrieval | Dial the
                                          					 retrieval FAC and park-slot extension. | Same as
                                          					 Basic Call Park Retrieval. |

| Note | This feature can
                                          		  be configured as PLK button for SCCP and SIP Phone. For more information see Configure Feature Button on a Cisco Unified SCCP Line Key and Configure Feature Button on a Cisco Unified SIP Phone Line Key . |
|---|---|

| Note | You must perform
                                             			 this task only if the feature was previously disabled on a phone. This feature is enabled by default for SCCP and SIP phones. For SCCP phones, this feature can be enabled and disabled. However,
                                             SIP phones do not have the enable or disable option. |
|---|---|

| Restriction | If there are more than 20 active calls parked, then only the first 20 active parked calls will be displayed. Dedicated, private call-park slots configured using the reserved-for command are not supported on the phone’s display. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone phone-tag Example: Router(config)# ephone 12 | Enters ephone
                                             				configuration mode. phone-tag —Unique number that identifies this
                                                   					 ephone during configuration tasks. |
| Step 4 | phone-ui park-list Example: Router(config-ephone)# phone-ui park-list | Enables a
                                             				phone user to view the list of active parked calls. This
                                                   					 command is enabled by default. |
| Step 5 | end Example: Router(config-ephone)# end | Exits to
                                             				privileged EXEC mode. |

| Note | The reservation-group is used so that the phone with a reservation
                                          		  group is allowed to park to park-slot(s) within the same reservation group. Any phone within the same CME can retrieve any parked calls. So the
                                          		  rule is applied when you park the call, not when you retrieve the call. |
|---|---|

| Note | Cisco IP Phone 8800 Series phones do not support Distinctive Call Park Recall feature. |
|---|---|

| Note | Park Monitor is supported in Cisco IP Phone 7800 Series and Cisco Unified IP Phone 9900 Series. However, Cisco IP Phone 8800
                                          Series do not support Park Monitor feature. |
|---|---|

| Restriction | For SIP
                                                   				  phones, the Park soft key is not supported for Cisco Unified IP Phone 7905,
                                                   				  7912, 7921, 7940, or 7960. Park
                                                   				  Retrieval is supported only on local phones. Phones can park calls remotely to
                                                   				  another Cisco Unified CME router but only phones that are registered to the
                                                   				  local router hosting the call-park slots can retrieve a call. In versions
                                                   				  earlier than Cisco Unified CME 7.1, Call Park and Directed Call Park shared the
                                                   				  same call-park slots. In Cisco Unified CME 7.1 and later versions, if a user
                                                   				  attempts to transfer a call to a basic park slot when using Directed Call Park,
                                                   				  Cisco Unified CME considers that a Park Retrieval. A user can
                                                   				  retrieve a parked call on an SCCP phone by pressing the PickUp soft key and
                                                   				  dialing the extension number of the call-park slot or an asterisk (*) only if
                                                   				  the service directed-pickup command is enabled
                                                   				  (default). Otherwise this initiates a local group pickup. Park
                                                   				  Reservation Groups are not supported with Directed Call Park. Different
                                                   				  directory numbers with the same extension number must have the same Call Park
                                                   				  configuration. Calls from
                                                   				  H.323 trunks are not supported on SIP phones. Hold Pickup
                                                   				  is not supported with the call-park system
                                                         						application command. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 4 | call-park system { application \| redirect } Example: Router(config-telephony)# call-park system application | Defines system
                                             				parameters for the Call Park feature. application —Enables the Call Park and Directed
                                                   					 Call Park features supported in Cisco Unified CME 7.1 and later versions. redirect —Specifies that H.323 and SIP calls use
                                                   					 H.450 or the SIP Refer method of call forwarding or transfer to park calls and
                                                   					 pick up calls from park. |
| Step 5 | fac { standard \| custom dpark-retrieval custom-fac } Example: Router(config-telephony)# fac custom dpark-retrieval #25 | Enables
                                             				standard FACs or creates a custom FAC or alias for the Directed Park Retrieval
                                             				feature on SCCP and SIP phones. Enable
                                                   					 this command to use the Directed Park Retrieval feature in
                                                   					 Cisco Unified CME 7.1 and later versions. standard —Enables standard FACs for all phones.
                                                   					 Standard FAC for Park Retrieval is **10. custom —Creates a custom FAC for a feature. custom-fac —User-defined code to dial using the
                                                   					 keypad on an IP or analog phone. Custom FAC can be up to 256 characters and
                                                   					 contain numbers 0 to 9 and * and #. |
| Step 6 | exit Example: Router(config-telephony)# exit | Returns to
                                             				privileged EXEC mode. |
| Step 7 | ephone-dn dn-tag [ dual-line ] Example: Router(config)# ephone-dn 1 | Enters
                                             				ephone dn configuration mode to define a directory number for an IP phone,
                                             				intercom line, voice port, or a message-waiting indicator (MWI). dn-tag —identifies a particular directory number
                                                   					 during configuration tasks. Range is 1 to the maximum number of directory
                                                   					 numbers allowed on the router platform. Type ? to display the range. |
| Step 8 | number number [ secondary number ] [ no-reg [ both \| primary ]] Example: Router(config-ephone-dn)# number 3001 | Associates
                                             				an extension number with this directory number. number —String of up to 16 digits that represents
                                                   					 an extension or E.164 telephone number. Note The
                                                         				  primary number must be unique for call-park slots. | Note | The
                                                         				  primary number must be unique for call-park slots. |
| Note | The
                                                         				  primary number must be unique for call-park slots. |
| Step 9 | park-slot [ directed ] [ reservation-group group-number ] [ reserved-for extension-number ] [[ timeout seconds limit count ][ notify extension-number [ only ]] [ recall ][ transfer extension-number ][ alternate extension-number ] [ retry seconds limit count ]] Example: Router(config-ephone-dn)# park-slot directed | Creates an
                                             				extension (call-park slot) at which calls can be temporarily held (parked). directed —(Optional) Enables Directed Call Park
                                                   					 using this extension. This keyword is supported in Cisco Unified CME 7.1 and
                                                   					 later versions. reservation-group group-number —(Optional) Reserves this slot for
                                                   					 phones configured with the specified reservation group. This is the group
                                                   					 assigned to the phone in Step 12. This keyword is supported in Cisco Unified
                                                   					 CME 7.1 and later versions. reserved-for extension-number —(Optional) Reserves this slot as
                                                   					 a private park-slot for the phone with the specified extension number as its
                                                   					 primary line. Note The reservation-group and reserved-for keywords are mutually exclusive. If
                                                         				  you use the reservation-group keyword, the reserved-for keyword is ignored. The reservation-group is used so
                                                         				  that the phone with a reservation group is allowed to park to park-slot(s)
                                                         				  within the same reservation group. Any phone within the same CME can retrieve
                                                         				  any parked calls. So the rule is applied when you park the call, not when you
                                                         				  retrieve the call. | Note | The reservation-group and reserved-for keywords are mutually exclusive. If
                                                         				  you use the reservation-group keyword, the reserved-for keyword is ignored. The reservation-group is used so
                                                         				  that the phone with a reservation group is allowed to park to park-slot(s)
                                                         				  within the same reservation group. Any phone within the same CME can retrieve
                                                         				  any parked calls. So the rule is applied when you park the call, not when you
                                                         				  retrieve the call. |
| Note | The reservation-group and reserved-for keywords are mutually exclusive. If
                                                         				  you use the reservation-group keyword, the reserved-for keyword is ignored. The reservation-group is used so
                                                         				  that the phone with a reservation group is allowed to park to park-slot(s)
                                                         				  within the same reservation group. Any phone within the same CME can retrieve
                                                         				  any parked calls. So the rule is applied when you park the call, not when you
                                                         				  retrieve the call. |
| Step 10 | exit Example: Router(config-ephone-dn)# exit | Exits
                                             				configuration mode. |
| Step 11 | ephone phone-tag or voice register pool phone-tag Example: Router(config)# ephone 1 or Router(config)# voice register pool 1 | Enters
                                             				ephone configuration mode to set phone-specific parameters for an SCCP phone. or Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone. phone-tag —Unique sequence number that identifies
                                                   					 the phone. Range is version and platform-dependent; type ? to display range. |
| Step 12 | park reservation-group group-number Example: Router(config-ephone)# park reservation-group 1 or Router(config-register-pool)# park reservation-group 1 | (Optional)
                                             				Assigns a call-park reservation group to a phone. group-number —Unique number that identifies the
                                                   					 reservation group. String can contain up to 32 digits. This
                                                   					 command can also be configured in ephone-template or voice register template
                                                   					 configuration mode and applied to one or more phones. The phone configuration
                                                   					 has priority over the template configuration. This
                                                   					 command is supported in Cisco Unified CME 7.1 and later versions. |
| Step 13 | end Example: Router(config-ephone)# end or Router(config-register-pool)# end | Exits
                                             				configuration mode. |

| Note | The
                                                         				  primary number must be unique for call-park slots. |
|---|---|

| Note | The reservation-group and reserved-for keywords are mutually exclusive. If
                                                         				  you use the reservation-group keyword, the reserved-for keyword is ignored. The reservation-group is used so
                                                         				  that the phone with a reservation group is allowed to park to park-slot(s)
                                                         				  within the same reservation group. Any phone within the same CME can retrieve
                                                         				  any parked calls. So the rule is applied when you park the call, not when you
                                                         				  retrieve the call. |
|---|---|

| Step 1 | Use the show
                                                				  running-config command to verify your configuration. Call-park
                                          			 slots are listed in the ephone-dn portion of the output. Example: Router# show running-config !
			 ephone-dn  23
			  number 853
			  park-slot timeout 10 limit 1 recall
			  description park slot for Sales
			 !
			 !
			 ephone-dn  24
			  number 8126
			  park-slot reserved-for 126 timeout 10 limit 1 transfer 8145
			 !
			 !
			 ephone-dn  25
			  number 8121 secondary 121
			  park-slot reserved-for 121 timeout 30 limit 1 transfer 8145
			 !
			 !
			 ephone-dn  26
			  number 8136 secondary 136
			  park-slot reserved-for 136 timeout 10 limit 1 recall
			 !
			 !
			 ephone-dn  30  dual-line
			  number 451 secondary 501
			  preference 10
			  huntstop channel
			 !
			 !
			 ephone-dn  31  dual-line
			  number 452 secondary 502
			  preference 10
			  huntstop channel
			 ! |
|---|---|
| Step 2 | Use the show telephony-service ephone-dn command to display call park
                                          			 configuration information. Example: Router# show telephony-service ephone-dn ephone-dn  26
		   number 8136 secondary 136
		   park-slot reserved-for 136 timeout 10 limit 1 recall |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone ring timeouts seconds Example: Router(config)# ring timeout 25 | Enters a
                                             				timeout period before disconnecting the call. |
| Step 4 | exit Example: Router(config-ephone)# exit | Exits to
                                             				privileged EXEC mode. |

| Step 1 | show ephone-dn park Use this
                                             				command to display configured call-park slots and their status. Router# show ephone-dn park DN 50 (1560) park-slot state IDLE
Notify to () timeout 30 limit 10 |
|---|---|
| Step 2 | Use the debug ephone commands to observe messages and states associated with an ephone. For more
                                          			 information, see Cisco Unified CME Command
                                             				Reference . |

| Feature
                                          					 Name | Cisco Unified CME Version | Feature
                                          					 Information |
|---|---|---|
| Call Park
                                          					 Recall Enhancement | 9.5 | Added
                                          					 recall force keyword to the call-park system command. |
| Call Park | 8.5 | Support
                                          					 for Park Monitor was introduced. |
| 7.1 | Adds Call
                                          					 Park support for SIP phones, introduces Park Reservation Groups, and enhances
                                          					 Directed Call Park. |
| 4.0 | Dedicated
                                          					 call-park slots, alternative recall locations, and call-park blocking were
                                          					 introduced. Direct calls to park slots are now interpreted as attempts to pick
                                          					 up parked calls rather than attempts to be parked at the slot. |
| 3.2.1 | Monitoring
                                          					 of call-park slots was introduced. |
| 3.1 | Call park
                                          					 was introduced. |