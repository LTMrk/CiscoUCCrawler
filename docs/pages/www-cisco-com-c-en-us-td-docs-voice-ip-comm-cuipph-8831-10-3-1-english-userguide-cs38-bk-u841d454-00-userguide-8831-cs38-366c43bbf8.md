---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8831-10-3-1-english-userguide-cs38-bk-u841d454-00-userguide-8831-cs38-366c43bbf8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8831/10_3_1/english/UserGuide/CS38_BK_U841D454_00_userguide-8831/CS38_BK_U841D454_00_userguide-8831_chapter_0101.html
retrieved_at: 2026-08-21T02:08:44.573352+00:00
---

Cisco Unified IP Conference Phone 8831 and 8831NR User Guide for Cisco Unified Communications Manager

# Cisco Unified IP Conference Phone 8831 and 8831NR User Guide for Cisco Unified Communications Manager

Updated: November 17, 2014

Chapter: Calling
	 Features

## Chapter: Calling
	 Features

# Calling
                     	 Features

## Softkey Feature
                        	 Map

Depending upon how
                              		  your system administrator sets up your phone, not all features may be available
                              		  to you, some features may be accessed from a different softkey, or additional
                              		  softkey features are available.

The
                              		  following table provides a guide to some of the softkey features that are
                              		  commonly available for various call states. Also shown is the function of the
                              		  Call button for the matching state.

Call State

Softkey 1

Softkey 2

Softkey 3

Softkey 4

Call
                                          					 Button

Idle

Redial

New Call

Apps

More1

Off hook

Contacts

Msgs

Fwd All

More2

Ring in

Answer

Divert

Answer

On hook
                                          					 (pre-dial)

Cancel

Call

X

Dial

Off hook

Redial

Cancel

Apps

More1

On hook

Contacts

Msgs

Calls

More2

Ring out

Cancel

Callback

On hook

Connected

Hold

End Call

Apps

More1

On hook

Contacts

Transfer

Conf

More2

ConfList

Park

Top

On hold

Resume

New Call

Apps

More1

Resume

Contacts

Msgs

Divert

Top

Connected
                                          					 (multiple calls)

Hold

End Call

Apps

More1

On hook

Contacts

Swap or
                                          					 Calls

Transfer

More2

Conf

ConfList

Park

Top

The ConfList
                                          			 softkey displays only if you are in a conference.

The Calls
                                          			 softkey displays when more than two calls are connected. Pressing Calls loads a
                                          			 call list.

### Survivable Remote
                           	 Site Telephony Overview

If communication
                              		between the conference station and the Cisco Unified Communications Manager is
                              		interrupted, you receive an alert message on your phone. If you are on an
                              		active call, the call remains established, and you enter a failover situation.
                              		The Survivable Remote Site Telephony (SRST) feature handles this failover.

While in failover,
                              		not all the features of conference station are available. The following table
                              		describes typical features and feature availability. For more information about
                              		feature availability during failover, contact your system administrator.

When the
                              		conference station loses connectivity, it may display a message similar to
                              		this: SRST.
                                 		  Some features unavailable.

New Call

Yes

End Call

Yes

Redial

Yes

Answer

Yes

Hold

Yes

Resume

Yes

Call Forward

No

This also
                                          				applies to other forwarding features such as Call Forward All, Call Forward
                                          				Busy, and Call Forward No Answer.

If you press CFwdAll , the phone does not ring for all incoming calls.

Conference

Yes

Conference to
                                          				Active Calls (Join)

No

The Active
                                             				Calls softkey is not displayed.

Conference
                                          				List

No

Transfer

Yes

Consult only.

Transfer to
                                          				Active Calls (Direct Transfer)

No

Auto Answer

Yes

Call Waiting

Yes

Caller ID

Yes

Audible
                                          				Message Waiting Indicator

Yes

Unified
                                          				Session Presentation

Yes

Conference is
                                          				the only feature supported.

Voicemail

Yes

Your voicemail
                                          				will not be synchronized with other users in the Cisco Unified Communications
                                          				Manager cluster.

To Voicemail
                                          				(Divert)

No

The Divert softkey is not displayed.

Park
                                          				Monitoring

No

The Park softkey is not displayed.

Barge

No

You see the
                                          				message That feature is not currently available .

Enhanced
                                          				Message Waiting Indication

No

Message count
                                          				badges do not appear on the phone screen.

Only the
                                          				Message Waiting icon displays.

Directed Call
                                          				Park

No

The softkey is
                                          				not displayed.

Hold
                                          				Reversion

No

Calls remain
                                          				on hold indefinitely.

Remote Hold

No

Calls appear
                                          				as Local Hold calls.

Meet Me

No

The Meet Me softkey is not displayed.

PickUp

No

The softkey
                                          				causes no action.

Group PickUp

No

The softkey
                                          				causes no action.

Other PickUp

No

The softkey
                                          				causes no action.

Malicious
                                          				Call ID

No

The softkey
                                          				causes no action.

QRT

No

The softkey
                                          				causes no action.

Mobility

No

The softkey
                                          				causes no action.

Privacy

No

The softkey
                                          				causes no action.

Call Back

No

The Call
                                             				Back softkey is not displayed.

## Answer

Answer allows you to answer the oldest call that is available on the conference station, including Hold Reversion and Park
                              Reversion calls that are in an alerting state. Incoming calls always have priority over Held or Park Reversion calls.

When you get a call, you see a notification on the conference station screen. The call notification remains visible for a
                              preset amount of time. If there are multiple, simultaneous incoming calls, an incoming call list window is displayed, and
                              you can select which call to answer.

To answer a call, press Answer or press the Call key.

If an incoming call has been call forwarded from another phone or conference station, you may see additional information to
                              identify that the call has been forwarded. Your system administrator controls the amount of additional information displayed.
                              Additional information can identify the person who forwarded the call to you and the caller information.

When you receive a call, the phone number that displays on the screen contains the string of digits that you can dial to contact
                              the caller. The digit string can contain the following digits, if required:

Code to obtain an outside line (for example, if you have to dial 9)

Long-distance code

Area code

City code

Telephone number

The conference station saves the complete digit string in the call history and you can save the number in your Personal Address
                              Book.

## Call Back

Call Back allows you to receive an audio and a visual notification on your conference station when a busy or unavailable party
                           becomes available.

For more information, contact your system administrator.

### Set Up Call Back
                           	 Notification

Press Call
                                             				back while listening to the busy tone or ring sound.

Press Exit to exit the confirmation screen.

Your phone
                                             				alerts you when the line is free.

Press Call to place the call again.

## Call
                        	 Forward

Call
                              		  Forward allows you to forward incoming calls from the conference station to
                              		  another number.

There
                              		  are two types of call forwarding features that the system administrator can set
                              		  up for the conference station:

Unconditional
                                    				call forwarding (Call Forward All): Applies to all calls that you receive.

Conditional
                                    				call forwarding (Call Forward No Answer, Call Forward Busy, Call Forward No
                                    				Coverage): Applies to certain calls that you receive.

If configured, you can set
                              		  up Call Forward All from the conference station. Call Forward All can also be
                              		  accessed remotely from your Cisco Unified Communications Manager Self Care
                              		  Portal. Conditional call forwarding rules can only be accessed from Cisco
                              		  Unified Communications Manager Self Care Portal.

When
                              		  forwarding calls from your conference station:

Enter the call
                                    				forward target number exactly as you would dial it from the conference station.
                                    				For example, enter an access code or the area code, if necessary.

Call
                                    				forwarding is line specific. If a call reaches you on a line where call
                                    				forwarding is not enabled, the call rings as usual.

For more
                                    				details about the following configurable call forward options, contact your
                                    				system administrator:

Allow
                                          					 calls placed from the call forward target number to the conference station to
                                          					 ring through, rather than be forwarded.

Prevent
                                          					 you from creating a call forward loop or exceeding the maximum number of links
                                          					 in a call forwarding chain.

### Forward
                           	 Calls

Press Fwd
                                             				All .

Enter the
                                          			 target phone number.

To cancel call
                                          			 forwarding, press Fwd
                                             				OFF .

To forward calls remotely or to set conditions on fall forwarding,
                                          			 go to your Cisco Unified Communications Manager Self Care Portal.

## Call Park

Call Park allows you to use the conference station to park (temporarily store) a call. The parked call can be retrieved from
                           another phone in the Cisco Unified Communications Manager system, such as a phone at a coworker’s desk or in a conference
                           room.

You retrieve a parked call by entering the parking number for the call into another phone in the Cisco Unified Communications
                           Manager system.

Your system administrator sets up the parking number for the conference station.

### Park Call

During a call,
                                          			 press the Park .

The conference
                                             				station screen displays the call park number where the system stored your call.

Note the call
                                          			 park number displayed on the screen. This number is used to retrieve the call.

You have a
                                             				limited time to retrieve a parked call before it reverts to ringing at the
                                             				original number.

From any other
                                          			 Cisco Unified IP Phone or conference station in your network, enter the call
                                          			 park number to retrieve the call.

## Call Pickup

Call Pickup allows you to answer a call that is ringing on a coworker’s phone by redirecting the call to your phone.

You might use Call Pickup if you share call-handling tasks with coworkers.

The ways to pick up a call are:

Pickup: Allows you to answer a call that is ringing on another phone within your call pickup group.

If multiple calls are available for pick up, the conference station picks up the oldest call first.

Group Pickup: Allows you to answer a call on a phone that is outside your call pickup group by:

Using a group pickup number that is provided by your system administrator.

Dialing the number of the ringing phone.

Other Pickup: Allows you to answer a call that is ringing on another phone within in your call pickup group or in an associated
                                    call pickup group.

Your system administrator assigns you to a call pickup group and sets the call pickup softkeys.

### Answer Call Using
                           	 Pickup

Press Pickup to transfer a ringing call within your pickup
                                          			 group to the conference station.

If the call
                                          			 rings, press Answer to connect to the call.

### Answer Call Using
                           	 Group Pickup and Group Pickup Number

Press Group
                                             				Pickup to answer a call on a phone outside your pickup group.

Enter the
                                          			 group pickup number.

If the call
                                          			 rings, press Answer to connect to the call.

### Answer Call Using
                           	 Group Pickup and Phone Number

Press Group
                                             				Pickup .

Enter the
                                          			 number of the phone line with the call that you want to pick up.

For example,
                                             				if the call is ringing on line 12345, enter 12345 .

If the call
                                          			 rings, press Answer to connect.

### Answer Call Using
                           	 Other Pickup

Press OPickup to transfer a call in your pickup group or
                                          			 in an associated group to the conference station.

If the call
                                          			 rings, press Answer to connect.

## cBarge

The cBarge feature allows you to add yourself to a call on a shared line and create a standard (ad hoc) conference.

### Join Conference on
                           	 Shared Line

Press cBarge .

You may need
                                             				to press More first.

## Conference

Conference allows you to talk simultaneously with multiple parties.

When you are talking on a call, use Conference to dial another party and add them to the call.

Before completing a conference procedure, you can press Cancel to cancel the procedure.

As the conference host, you can remove individual participants from the conference. You can also view a list of participants.

The conference ends when all the participants hang up.

### Add Third Party to
                           	 Conference

#### Before you begin

Before you can add
                                 		  a party to the conference, you must be on an active call and not on hold.

Press Conf .

Enter the
                                          			 phone number for the party you want to
                                          			 add.

If you have
                                             				several held calls, you can press Calls to display a caller list and add a caller to
                                             				the conference.

After the new
                                          			 party answers, press Conf .

(Optional) Repeat these
                                          			 steps to add more parties, if desired.

### View Conference
                           	 Participants

While in a
                                          			 conference, press ConfList to view a list of the last 16 participants
                                          			 who have joined the conference.

The maximum
                                             				number of participants that can be displayed is 16. If there are more than 16
                                             				participants, only the most recent 16 participants to join display.

### Remove Conference
                           	 Participants

While in a
                                          			 conference, press ConfList to view a list of participants.

Highlight the
                                          			 participant that you want to remove and then press Remove .

Only the
                                                         				  most recent 16 conference participants display.

## Divert

Divert allows you to send an active or ringing call to your voicemail system or to a predetermined phone number. Your system
                           administrator configures this feature and sets the receiving phone number.

### Divert
                           	 Call

Press Divert to send an active call, an incoming call, or
                                          			 a held call to either your voicemail system or to a predetermined phone number
                                          			 set up by your system administrator.

## Do Not
                        	 Disturb

Do Not
                              		  Disturb (DND) allows you to turn off notification of incoming calls. The
                              		  ringer, as well as audible and visual notifications, can be turned off.

Depending on how your administrator has configured this feature,
                              		  incoming calls are either immediately rejected, or the caller information
                              		  displays on screen.

The system administrator
                              		  configures the DND softkey, but you can change your DND options from Cisco
                              		  Unified Communications Manager Self Care Portal.

DND
                              		  interacts with other types of calls:

If both DND
                                    				and Call Forward All are enabled, calls are forwarded without any visual or
                                    				audible confirmation.

DND does not
                                    				affect priority calls.

### Turn DND On and
                           	 Off

Press DND to turn on DND.

Press DND again to turn off DND.

## Enhanced Room
                        	 Coverage

Optional
                              		  microphone extension kits provide enhanced room coverage that can be further
                              		  expanded by linking two units together in Linked Mode. This feature allows you
                              		  to use the conference station in a larger room, or to enhance the audio and
                              		  voice experience for larger groups of in-person attendees.

The Cisco Unified IP Conference Phone 8831 supports wired and wireless microphones. The Cisco Unified IP Conference Phone
                              8831NR supports only wired microphones.

When two
                              		  conference station base units are linked together to expand the audio coverage
                              		  area, one conference station acts as the primary device and the other sound
                              		  base is the dependant or secondary device. In Linked Mode, the primary base
                              		  station supports one or two wireless microphones, or it supports one wired
                              		  microphone. The secondary unit supports only one wired microphone; a wireless
                              		  microphone cannot be connected to a secondary Sound Base. You cannot mix
                              		  microphone types on the devices. Consult the following tables for allowable
                              		  configurations.

Voice, dial tone,
                              		  ringer, and base LED features synchronize between the two devices in Linked
                              		  Mode.

### Pair Wireless
                           	 Microphone

#### Before you begin

The microphone
                                 		  must be in the off state before you can pair it to the conference station. A
                                 		  microphone is off if the microphone's LED is off. To turn off the wireless
                                 		  microphone, hold down the microphone button until the microphone LED turns
                                 		  solid red, then release.

Choose Apps > Admin
                                                				  Settings > Wireless Microphones .

Select either
                                          			 Wireless Microphone 1 or Wireless Microphone 2.

If the
                                             				selected channel is available, a Pair microphone 1? or Pair microphone 2? prompt displays, and the Pair softkey displays.

If a
                                             				microphone is already linked to a particular channel, pairing cannot be
                                             				initiated on the selected channel and the dialog shows that the microphone is
                                             				linked.

Press Pair .

If the channel
                                             				is ready to pair, the pairing process begins and a text message displays.

Put the
                                          			 microphone that corresponds to the selected channel in pairing mode by pressing
                                          			 the microphone's Mute button until the LED lights solid red.

If pairing
                                             				succeeds, the screen reverts to the Wireless Microphones Menu, and the message Mic X Paired Successfully! displays.

If pairing
                                             				times out or fails, the status is updated and you can cancel or retry.

Press Cancel to revert to the Wireless Microphones Menu.

Press Retry to start the pairing process again.

### Unpair Wireless
                           	 Microphone

If you need to
                                 		  connect a wired microphone to the conference station, any wireless microphones
                                 		  must be unpaired first. You can also use this procedure to unpair a microphone
                                 		  that is no longer in use.

This option is
                                             			 not available if the microphone is connected. To enable the unpair command,
                                             			 place the wireless microphone in its charger or turn it off.

Choose Applications > Admin
                                                				  Settings > Wireless Microphones .

Select either
                                          			 Wireless Microphone 1 or Wireless Microphone 2.

If the
                                             				selected channel is paired, the Unpair softkey displays.

Press Unpair .

A verification
                                             				prompt with the options to Cancel or Unpair displays.

Press Unpair to continue to unpair the microphone.

The
                                             				microphone channel's registration information in the base deletes. If you view
                                             				the microphone channel's status in phone info menu, the status value and RFID
                                             				are empty.

Press return
                                          			 to revert to the wireless microphones menu and stop the process.

## Cisco Extension
                        	 Mobility

Cisco
                           		Extension Mobility allows you to temporarily configure a Cisco Unified IP Phone
                           		or Conference Station to use as your own. After you log in to Extension
                           		Mobility, the new device adopts your user profile, features, established
                           		services, and web-based settings. Your system administrator must configure
                           		Extension Mobility for you.

The Cisco
                           		Extension Mobility ChangePIN feature allows you to change your PIN from your
                           		Cisco Unified IP Phone.

Extension
                                             				Mobility automatically logs you out after a certain amount of time. Your system
                                             				administrator establishes this time limit.

Changes that you
                                             				make to your Extension Mobility profile from Cisco Unified Communications
                                             				Manager Self Care Portal take effect immediately if you are logged in to
                                             				Extension Mobility on the physical device; otherwise, changes take effect the
                                             				next time you log in.

Changes that you make to a phone or conference station from Cisco
                                             				Unified Communications Manager Self Care Portal take effect immediately if you
                                             				are logged out of Extension Mobility; otherwise, changes take effect after you
                                             				log out.

Local settings
                                             				controlled by the phone are not maintained in your Extension Mobility profile.

### Enable Extension Mobility

Press Apps .

Select EM Service .

Enter your user ID and PIN.

The user ID and PIN are provided by your system administrator

If prompted, select a device profile.

To sign out, press Apps .

Select Services .

Select EM Service .

At the prompt, press Yes .

## Hold

Hold allows you to put an active call into a held state. Your phone allows one active call at a time; other calls are put
                           on hold.

### Hold Active
                           	 Call

To put an
                                          			 active call on hold, press Hold .

The Hold icon displays as a status icon.

If there is
                                          			 only one call on hold and you are not on an active call, press Resume .

If you are
                                          			 already on an active call, press Swap .

The holding
                                             				call becomes active, and the active call is placed on hold.

### Switch Between
                           	 Active and Multiple Holding Calls

If you are on
                                          			 an active call and there are multiple calls on hold, the Calls softkey becomes available and a call list of
                                          			 holding calls displays on the screen.

Use the
                                          			 Navigation bar to highlight the call you want to make active, press Resume .

The current
                                             				active call is placed on hold and the selected call is now active.

### Hold Active Call
                           	 and Answer New Incoming Call

To place an
                                          			 active call on hold and answer an incoming call, press Answer .

## Hold Reversion

Hold Reversion provides a notification that a call is left on hold. Hold reversion notifications are similar to new call notifications.

An animated icon that appears as an incoming call for two seconds and then as a hold icon for two more seconds.

A single ring that repeats at regular intervals.

The Call button on the DCU flashes green.

The LEDs on the sound base flash green.

### Respond to Hold
                           	 Reversion Notification

Press Answer

## Meet Me
                        	 Conference

If
                              		  enabled by your system administrator, you can call a predetermined number at a
                              		  scheduled time to host or join a Meet Me conference.

The Meet
                              		  Me conference begins when the host connects. Participants who call the
                              		  conference before the host has joined hear a busy tone and must dial again.

The
                                          			 conference ends when all participants hang up; the conference does not
                                          			 automatically end when the host disconnects.

### Host Meet Me
                           	 Conference

Obtain a Meet
                                          			 Me phone number from your system administrator.

Distribute the
                                          			 Meet Me phone number to participants.

When you are
                                          			 ready to start the meeting, press MeetMe .

You may need
                                             				to press More first.

Dial the Meet
                                          			 Me phone number.

### Join Meet Me Conference

Dial the Meet Me phone number provided by the conference host.

If you hear a busy tone, the host has not yet joined the
                                          			 conference. In this case, disconnect and  try your call again.

## Mobile
                        	 Connect

Mobile
                              		  Connect allows you to use your mobile phone to handle calls associated with the
                              		  conference station phone number.

To set up Mobile
                              		  Connect, use the Cisco Unified Communications Manager Self Care Portal to set
                              		  up remote destinations and create access lists to allow or block calls from
                              		  specific phone numbers from being passed to the remote destinations.

When you
                              		  enable Mobile Connect:

The
                                    				conference station and remote destinations receive calls simultaneously.

When you
                                    				answer the call on the conference station, the remote destinations stop
                                    				ringing, disconnect, and display a missed call message.

When you
                                    				answer the call on one remote destination, the other remote destinations and
                                    				the conference station stop ringing, disconnect, and a missed call message
                                    				displays on the other remote destinations.

### Enable Mobile Connect

Press More .

Press Mobility to display the current remote destination status (Enabled or Disabled).

Press Select to change the status.

Press Exit .

### Switch IP Phone
                           	 Call to Mobile Phone

Press More .

Press Mobility .

Select To
                                             				mobile .

Answer the
                                          			 in-progress call on your mobile phone.

You cannot
                                             				use the conference station for any other calls while this call is still in
                                             				progress.

The Call
                                             				button LED lights solid red, and the calling party number displays on the
                                             				phone.

### Switch Mobile Call
                           	 to IP Phone

Press Call on the conference station.

Hang up the
                                          			 call on your mobile phone to disconnect the mobile phone, but not the call.

Press Resume on the conference station within 5 to 10
                                          			 seconds and start talking on the conference station.

## Monitoring and Recording

The Monitoring and Recording feature allows you to monitor
                           		  and record calls. Your system administrator enables this feature, which can be
                           		  set up for automatic recording of all calls or recording of calls on an individual call 
                           		  basis.

You can start or stop a recording by pressing the Record softkey on your phone.

Users might receive audible alerts during call monitoring
                           		  and recording. By default, the person who monitors and records the call does not receive an audible alert.

Secure monitoring and recording is also available. For details on this aspect of the feature, contact your system administrator.

## Multiple Calls per
                        	 Line

The
                              		  conference station has a single line and supports a maximum of six calls.
                              		  Unless you are in a conference, only one call can be connected at any time;
                              		  other calls are automatically placed on hold.

### Multiple Incoming
                           	 Calls

If there is a
                                 		  second incoming call on the line, while the first call rings, a navigable
                                 		  incoming call list window displays on the screen. The call list window updates
                                 		  automatically if there are additional incoming calls, or if an incoming call is
                                 		  cancelled.

### Call Ended on Line
                           	 with Multiple Calls

If there are
                              		multiple calls on the line when a call completes, the next call in the call
                              		list gains focus.

### Outbound Call
                           	 Maximum

The conference
                              		station supports a maximum of 6 outbound calls.

### Answer Second Call
                           	 on Same Line

To answer a
                                          			 second call on your conference station line, press Answer .

### Switch Between
                           	 Calls on Same Line

Press Swap to switch between two calls on the same line.

If there are
                                          			 more than two calls on the line, select a call from the call list and press Resume .

### Create Conference
                           	 with Two Calls on Same Line

With two
                                          			 connected calls on the same line, select a call to make it the active call.

Press Conference .

Press Calls to view the call list and select the caller to
                                          			 add to the conference.

Wait for the
                                          			 call to connect.

Press Conference to add the participant to your call.

(Optional) Repeat to add
                                          			 additional participants.

### Transfer Two Calls
                           	 on Same Line

#### Before you begin

You must be on an
                                 		  active call to transfer calls.

Press Transfer .

Enter phone
                                          			 number for the transfer destination.

When you have
                                             				reached the maximum number of calls for your line, pressing Transfer allows you to select the calls from a list
                                             				of calls on the line.

Wait for the
                                          			 recipient to answer.

Press Transfer again.

### Shared Line

If the conference station is registered on a shared line you can handle multiple calls in the following ways:

If there are two or more remote calls on the shared line, the caller ID field on the conference station indicates the number
                                       of remote calls on the line, and the state of the call. Press Calls to display the call list window.

If at least one call on the shared line is on hold, the Call button LED flashes red. Press Resume to make the call active,
                                       or use the Navigation bar to choose a call to resume from the call list. For example, if a remote call on the shared line
                                       is placed on hold the Call button on your conference station will flash red.

## Mute

Mute allows you to block audio input for the conference station, so that you can hear other parties on the call but they cannot
                           hear you.

Press the Mute button on the Sound Base.

Press the Mute button on the DCU.

If connected, the optional extension microphones can also be used to mute the conference station. In Linked Mode, the Mute
                           button on the secondary sound base behaves the same as the Mute button on the primary unit.

Solid, red base LEDs and red base Mute button:  muted.

Solid, red DCU Mute button: muted.

### Mute IP Phone
                           	 Sound Base

Press Mute to turn Mute on.

Press Mute again to turn Mute off.

### Mute IP Phone
                           	 DCU

Press Mute to turn Mute on.

Press Mute again to turn Mute off.

## On-Hook
                        	 Dialing

On-hook
                           		dialing allows you to enter a phone number before getting a dial tone and then
                           		press the Call button to complete the call.

### Dial Number
                           	 On-Hook

Enter a phone number.

Press Dial .

## Plus Dialing

Plus Dialing allows you to press and hold the star (*) key for at least 1 second to insert a plus 
                           		(+) sign as the first digit in a phone number when dialing an  international number.

A phone number with the + sign in it can be selected and dialed without the need to add digits for international calls.

### Dial International
                           	 Number

#### Before you begin

Before dialing an
                                 		  international call or using Plus Dialing, enter any local access code, such as
                                 		  8 or 9 if applicable.

Press and hold
                                          			 star (*) for at least 1 second.

Dial the
                                          			 international number, including the country code.

## Privacy

If configured, the Privacy feature allows you to prevent others who share your line from seeing information about your calls.
                              Your system administrator configures this feature.

If the phone that shares your line has Privacy enabled, you can make and receive calls using the shared line as usual.

### Enable Privacy on
                           	 Shared Line

#### Before you begin

Before you can use
                                 		  this feature, it must enabled by your system administration.

Press More .

Use the
                                          			 Navigation bar and Select button to scroll to the Private softkey.

- Press Private to enable this feature.

- Press Private to disable this feature if it is currently
                                             				enabled.

## Quality Reporting Tool

Your system administrator may temporarily configure the conference station
                           		with the Quality Reporting Tool (QRT) to troubleshoot performance problems. Invoking the QRT  reports a problem with the
                           current call to the system administrator.

### Report IP Phone
                           	 Problems

Press More .

Use the
                                          			 Navigation bar and Select button to locate and select QRT .

The
                                             				information is sent to your system administrator.

## Redial

Redial allows you to call the most recently dialed phone number.

### Redial
                           	 Number

To redial the
                                          			 last number you called, press Redial .

## Shared
                        	 Lines

Shared
                              		  lines allow you to use one phone number for multiple devices.

A shared
                              		  line is useful if you have multiple devices and want one phone number, share
                              		  call-handling tasks with coworkers, or handle calls on behalf of a manager. The
                              		  other devices that share your line are referred to as remote devices, and a
                              		  call that is being handled by a device that shares your line is referred to as
                              		  a remote call.

When a call comes
                              		  in on the shared line, the conference station rings and your coworker's device
                              		  rings. Either you or your coworker can answer the call, place the call on hold,
                              		  or transfer the call.

Remote in use:
                                       				solid red LED.

Remote hold:
                                       				pulsing red LED

Your call history
                              		  shows the status for all calls on the shared line. For example, if a call rings
                              		  on a shared line and you answer the call, your coworkers who share the line see
                              		  that the call was answered remotely. Your call history identifies calls that
                              		  were Placed, Received, or Missed.

## Transfer

Transfer allows you to redirect a connected call from the conference station to another number.

Before completing a transfer procedure, you can press Cancel to cancel the procedure.

### Transfer Call to
                           	 Another Number

#### Before you begin

The call must be
                                 		  active to be transferred.

Press Transfer .

Enter the
                                          			 destination number.

Wait for the
                                          			 recipient to answer.

Press Transfer again.

The transfer
                                             				completes.

## Cisco WebDialer

Cisco WebDialer allows you to click-to-dial contacts from the Cisco Unified Communications Manager Directory. Your system
                           administrator sets up this feature for you.

### Use WebDialer with
                           	 Another Online Corporate Directory

Sign in to a
                                          			 WebDialer-enabled corporate directory and search for coworkers.

Select the
                                          			 number that you want to dial.

When prompted,
                                          			 enter your user ID and password.

If this is
                                          			 your first time using WebDialer, review the preferences on the Make Call
                                          			 window.

Select Dial .

The call is
                                             				now placed on your phone line.

To end a call,
                                          			 select Hang
                                             				up in the Make Call window or press End
                                             				Call on your conference station.

### Change WebDialer
                           	 Preferences

Sign in to
                                          			 your User Option web pages.

Initiate a
                                          			 call using WebDialer to access the Make Call window.

The Make Call
                                             				window displays the first time that you use WebDialer (after you select the
                                             				number that you want to dial).

Select one of
                                          			 the following options from the Make Call window:

Preferred
                                                				  language: Determines the language used for WebDialer settings and prompts.

Use
                                                				  preferred device: Identifies the Cisco Unified IP Phone (calling device) and
                                                				  directory number (calling line) that you use to place WebDialer calls.

If you have
                                             				one phone with a single line, the appropriate phone and line are automatically
                                             				selected.

If the phone
                                          			 and line do not select automatically, choose a phone or line.

If you have
                                             				more than one phone of the same type, the list identifies the phone by device
                                             				type and MAC address. To display the MAC address on your phone, select Apps > Phone
                                                   					 Information .

If you have an
                                          			 Extension Mobility profile, select Extension Mobility from the Calling Device drop-down
                                          			 menu in the Make Call window.

Ensure that
                                          			 you do not select Do not
                                             				display call information or Disable Auto Close .

Do not
                                                   					 display call confirmation: If selected, the WebDialer Make Call window does not
                                                   					 display the next time WebDialer is used. Calls will automatically dial after
                                                   					 you select a contact from the Cisco directory.

Disable
                                                   					 Auto Close: If selected, the call window does not close automatically after 15
                                                   					 seconds.

## Sign In to the Cisco Unified
                           				Communications Self Care Portal

Your phone is a
                              		  network device that can share information with other network devices in your
                              		  company, including your personal computer. You can use your computer to sign in
                              		  to the Cisco Unified
                                 				Communications Self Care Portal ,
                              		  where you can control features, settings, and services for your phone. For
                              		  example, you can manage your phone display language, set up services, add
                              		  entries to your personal address book, and set up speed-dial codes.

Before you can
                              		  access any of your options, such as speed dial or personal address book, you
                              		  must sign in. When you finish using the portal, sign out.

Some features may not be available for your phone, and thus you can't set the features up in the Self Care Portal.

Sometimes, you can
                              		  access the Cisco Unified
                                 				Communications Self Care Portal without signing in.

For assistance in
                              		  using the portal, see the Cisco Unified
                                    				Communications Self Care Portal User Guide at http://www.cisco.com/en/US/products/sw/voicesw/ps556/products_user_guide_list.html .

Obtain the
                                       			 portal URL, user ID, and default password from your administrator.

Typically, the
                                          				portal URL is http://ip_address or hostname/ucmuser .

Open a web
                                       			 browser on your computer and enter the URL.

If prompted to
                                       			 accept security settings, select Yes or Install Certificate .

Enter your
                                       			 user ID in the Username field.

Enter your
                                       			 password in the Password field.

Select Login .

Select Logout to sign out.

| Call State | Softkey 1 | Softkey 2 | Softkey 3 | Softkey 4 | Call
                                          					 Button |
|---|---|---|---|---|---|
| Idle | Redial | New Call | Apps | More1 | Off hook |
| Contacts | Msgs | Fwd All | More2 |
| Ring in | Answer | Divert |  |  | Answer |
| On hook
                                          					 (pre-dial) | Cancel | Call |  | X | Dial |
| Off hook | Redial | Cancel | Apps | More1 | On hook |
| Contacts | Msgs | Calls | More2 |
| Ring out | Cancel | Callback |  |  | On hook |
| Connected | Hold | End Call | Apps | More1 | On hook |
| Contacts | Transfer | Conf | More2 |
| ConfList | Park |  | Top |
| On hold | Resume | New Call | Apps | More1 | Resume |
| Contacts | Msgs | Divert | Top |
| Connected
                                          					 (multiple calls) | Hold | End Call | Apps | More1 | On hook |
| Contacts | Swap or
                                          					 Calls | Transfer | More2 |
| Conf | ConfList | Park | Top |

| Note | The ConfList
                                          			 softkey displays only if you are in a conference. |
|---|---|

| Note | The Calls
                                          			 softkey displays when more than two calls are connected. Pressing Calls loads a
                                          			 call list. |
|---|---|

| Feature | Supported | Notes |
|---|---|---|
| New Call | Yes |  |
| End Call | Yes |  |
| Redial | Yes |  |
| Answer | Yes |  |
| Hold | Yes |  |
| Resume | Yes |  |
| Call Forward | No | This also
                                          				applies to other forwarding features such as Call Forward All, Call Forward
                                          				Busy, and Call Forward No Answer. If you press CFwdAll , the phone does not ring for all incoming calls. |
| Conference | Yes |  |
| Conference to
                                          				Active Calls (Join) | No | The Active
                                             				Calls softkey is not displayed. |
| Conference
                                          				List | No |  |
| Transfer | Yes | Consult only. |
| Transfer to
                                          				Active Calls (Direct Transfer) | No |  |
| Auto Answer | Yes |  |
| Call Waiting | Yes |  |
| Caller ID | Yes |  |
| Audible
                                          				Message Waiting Indicator | Yes |  |
| Unified
                                          				Session Presentation | Yes | Conference is
                                          				the only feature supported. |
| Voicemail | Yes | Your voicemail
                                          				will not be synchronized with other users in the Cisco Unified Communications
                                          				Manager cluster. |
| To Voicemail
                                          				(Divert) | No | The Divert softkey is not displayed. |
| Park
                                          				Monitoring | No | The Park softkey is not displayed. |
| Barge | No | You see the
                                          				message That feature is not currently available . |
| Enhanced
                                          				Message Waiting Indication | No | Message count
                                          				badges do not appear on the phone screen. Only the
                                          				Message Waiting icon displays. |
| Directed Call
                                          				Park | No | The softkey is
                                          				not displayed. |
| Hold
                                          				Reversion | No | Calls remain
                                          				on hold indefinitely. |
| Remote Hold | No | Calls appear
                                          				as Local Hold calls. |
| Meet Me | No | The Meet Me softkey is not displayed. |
| PickUp | No | The softkey
                                          				causes no action. |
| Group PickUp | No | The softkey
                                          				causes no action. |
| Other PickUp | No | The softkey
                                          				causes no action. |
| Malicious
                                          				Call ID | No | The softkey
                                          				causes no action. |
| QRT | No | The softkey
                                          				causes no action. |
| Mobility | No | The softkey
                                          				causes no action. |
| Privacy | No | The softkey
                                          				causes no action. |
| Call Back | No | The Call
                                             				Back softkey is not displayed. |

| Step 1 | Press Call
                                             				back while listening to the busy tone or ring sound. A
                                          			 confirmation screen displays on the phone. |
|---|---|
| Step 2 | Press Exit to exit the confirmation screen. Your phone
                                             				alerts you when the line is free. |
| Step 3 | Press Call to place the call again. |

| Step 1 | Press Fwd
                                             				All . |
|---|---|
| Step 2 | Enter the
                                          			 target phone number. Depending on
                                          			 how your voicemail system is set up, you may be able to press Msgs to forward all calls to voicemail. A
                                          			 visual confirmation displays on the screen while call forwarding is active. |
| Step 3 | To cancel call
                                          			 forwarding, press Fwd
                                             				OFF . |
| Step 4 | To forward calls remotely or to set conditions on fall forwarding,
                                          			 go to your Cisco Unified Communications Manager Self Care Portal. |

| Step 1 | During a call,
                                          			 press the Park . The conference
                                             				station screen displays the call park number where the system stored your call. |
|---|---|
| Step 2 | Note the call
                                          			 park number displayed on the screen. This number is used to retrieve the call. You have a
                                             				limited time to retrieve a parked call before it reverts to ringing at the
                                             				original number. |
| Step 3 | From any other
                                          			 Cisco Unified IP Phone or conference station in your network, enter the call
                                          			 park number to retrieve the call. |

| Step 1 | Press Pickup to transfer a ringing call within your pickup
                                          			 group to the conference station. |
|---|---|
| Step 2 | If the call
                                          			 rings, press Answer to connect to the call. |

| Step 1 | Press Group
                                             				Pickup to answer a call on a phone outside your pickup group. |
|---|---|
| Step 2 | Enter the
                                          			 group pickup number. |
| Step 3 | If the call
                                          			 rings, press Answer to connect to the call. |

| Step 1 | Press Group
                                             				Pickup . |
|---|---|
| Step 2 | Enter the
                                          			 number of the phone line with the call that you want to pick up. For example,
                                             				if the call is ringing on line 12345, enter 12345 . |
| Step 3 | If the call
                                          			 rings, press Answer to connect. |

| Step 1 | Press OPickup to transfer a call in your pickup group or
                                          			 in an associated group to the conference station. |
|---|---|
| Step 2 | If the call
                                          			 rings, press Answer to connect. |

| Press cBarge . You may need
                                             				to press More first. |
|---|

| Step 1 | Press Conf . |
|---|---|
| Step 2 | Enter the
                                          			 phone number for the party you want to
                                          			 add. If you have
                                             				several held calls, you can press Calls to display a caller list and add a caller to
                                             				the conference. |
| Step 3 | After the new
                                          			 party answers, press Conf . The
                                          			 conference begins. |
| Step 4 | (Optional) Repeat these
                                          			 steps to add more parties, if desired. |

| While in a
                                          			 conference, press ConfList to view a list of the last 16 participants
                                          			 who have joined the conference. The maximum
                                             				number of participants that can be displayed is 16. If there are more than 16
                                             				participants, only the most recent 16 participants to join display. |
|---|

| Step 1 | While in a
                                          			 conference, press ConfList to view a list of participants. |
|---|---|
| Step 2 | Highlight the
                                          			 participant that you want to remove and then press Remove . Note Only the
                                                         				  most recent 16 conference participants display. | Note | Only the
                                                         				  most recent 16 conference participants display. |
| Note | Only the
                                                         				  most recent 16 conference participants display. |

| Note | Only the
                                                         				  most recent 16 conference participants display. |
|---|---|

| Press Divert to send an active call, an incoming call, or
                                          			 a held call to either your voicemail system or to a predetermined phone number
                                          			 set up by your system administrator. |
|---|

| Step 1 | Press DND to turn on DND. Visual
                                          			 confirmation displays briefly. |
|---|---|
| Step 2 | Press DND again to turn off DND. Visual
                                          			 confirmation displays briefly. |

|  | Wired Extension Microphone | Wireless Extension
                                       				  Microphone |
|---|---|---|
| Number and type of
                                       				  connected microphones | 1 or 2 | -- |
| -- | 1 or 2 |

|  | Primary Sound Base | Secondary Sound Base |
|---|---|---|
| Wired Extension Microphone | -- | -- |
| Wired Extension Microphone | -- | 1 |
| Wired Extension Microphone | 1 | -- |
| Wired Extension Microphone | 1 | 1 |
| Wireless Extension
                                       				  Microphone | -- | -- |
| Wireless Extension
                                       				  Microphone | 1 or 2 | -- |

| Note | Use a daisy
                                          			 cable to connect two sound base units in Linked Mode. |
|---|---|

| Step 1 | Choose Apps > Admin
                                                				  Settings > Wireless Microphones . |
|---|---|
| Step 2 | Select either
                                          			 Wireless Microphone 1 or Wireless Microphone 2. If the
                                             				selected channel is available, a Pair microphone 1? or Pair microphone 2? prompt displays, and the Pair softkey displays. If a
                                             				microphone is already linked to a particular channel, pairing cannot be
                                             				initiated on the selected channel and the dialog shows that the microphone is
                                             				linked. |
| Step 3 | Press Pair . If the channel
                                             				is ready to pair, the pairing process begins and a text message displays. |
| Step 4 | Put the
                                          			 microphone that corresponds to the selected channel in pairing mode by pressing
                                          			 the microphone's Mute button until the LED lights solid red. If pairing
                                             				succeeds, the screen reverts to the Wireless Microphones Menu, and the message Mic X Paired Successfully! displays. If pairing
                                             				times out or fails, the status is updated and you can cancel or retry. |
| Step 5 | Press Cancel to revert to the Wireless Microphones Menu. |
| Step 6 | Press Retry to start the pairing process again. |

| Note | This option is
                                             			 not available if the microphone is connected. To enable the unpair command,
                                             			 place the wireless microphone in its charger or turn it off. |
|---|---|

| Step 1 | Choose Applications > Admin
                                                				  Settings > Wireless Microphones . |
|---|---|
| Step 2 | Select either
                                          			 Wireless Microphone 1 or Wireless Microphone 2. If the
                                             				selected channel is paired, the Unpair softkey displays. |
| Step 3 | Press Unpair . A verification
                                             				prompt with the options to Cancel or Unpair displays. |
| Step 4 | Press Unpair to continue to unpair the microphone. The
                                             				microphone channel's registration information in the base deletes. If you view
                                             				the microphone channel's status in phone info menu, the status value and RFID
                                             				are empty. |
| Step 5 | Press return
                                          			 to revert to the wireless microphones menu and stop the process. |

| Note | Extension
                                             				Mobility automatically logs you out after a certain amount of time. Your system
                                             				administrator establishes this time limit. Changes that you
                                             				make to your Extension Mobility profile from Cisco Unified Communications
                                             				Manager Self Care Portal take effect immediately if you are logged in to
                                             				Extension Mobility on the physical device; otherwise, changes take effect the
                                             				next time you log in. Changes that you make to a phone or conference station from Cisco
                                             				Unified Communications Manager Self Care Portal take effect immediately if you
                                             				are logged out of Extension Mobility; otherwise, changes take effect after you
                                             				log out. Local settings
                                             				controlled by the phone are not maintained in your Extension Mobility profile. |
|---|---|

| Step 1 | Press Apps . |
|---|---|
| Step 2 | Select EM Service . |
| Step 3 | Enter your user ID and PIN. The user ID and PIN are provided by your system administrator |
| Step 4 | If prompted, select a device profile. |
| Step 5 | To sign out, press Apps . |
| Step 6 | Select Services . |
| Step 7 | Select EM Service . |
| Step 8 | At the prompt, press Yes . |

| Step 1 | To put an
                                          			 active call on hold, press Hold . The Hold icon displays as a status icon. |
|---|---|
| Step 2 | If there is
                                          			 only one call on hold and you are not on an active call, press Resume . |
| Step 3 | If you are
                                          			 already on an active call, press Swap . The holding
                                             				call becomes active, and the active call is placed on hold. |

| Step 1 | If you are on
                                          			 an active call and there are multiple calls on hold, the Calls softkey becomes available and a call list of
                                          			 holding calls displays on the screen. |
|---|---|
| Step 2 | Use the
                                          			 Navigation bar to highlight the call you want to make active, press Resume . The current
                                             				active call is placed on hold and the selected call is now active. |

| To place an
                                          			 active call on hold and answer an incoming call, press Answer . |
|---|

| Press Answer |
|---|

| Note | The
                                          			 conference ends when all participants hang up; the conference does not
                                          			 automatically end when the host disconnects. |
|---|---|

| Step 1 | Obtain a Meet
                                          			 Me phone number from your system administrator. |
|---|---|
| Step 2 | Distribute the
                                          			 Meet Me phone number to participants. |
| Step 3 | When you are
                                          			 ready to start the meeting, press MeetMe . You may need
                                             				to press More first. |
| Step 4 | Dial the Meet
                                          			 Me phone number. |

| Step 1 | Dial the Meet Me phone number provided by the conference host. |
|---|---|
| Step 2 | If you hear a busy tone, the host has not yet joined the
                                          			 conference. In this case, disconnect and  try your call again. |

| Step 1 | Press More . |
|---|---|
| Step 2 | Press Mobility to display the current remote destination status (Enabled or Disabled). |
| Step 3 | Press Select to change the status. |
| Step 4 | Press Exit . |

| Step 1 | Press More . |
|---|---|
| Step 2 | Press Mobility . |
| Step 3 | Select To
                                             				mobile . |
| Step 4 | Answer the
                                          			 in-progress call on your mobile phone. You cannot
                                             				use the conference station for any other calls while this call is still in
                                             				progress. The Call
                                             				button LED lights solid red, and the calling party number displays on the
                                             				phone. |

| Step 1 | Press Call on the conference station. |
|---|---|
| Step 2 | Hang up the
                                          			 call on your mobile phone to disconnect the mobile phone, but not the call. |
| Step 3 | Press Resume on the conference station within 5 to 10
                                          			 seconds and start talking on the conference station. |

| To answer a
                                          			 second call on your conference station line, press Answer . |
|---|

| Step 1 | Press Swap to switch between two calls on the same line. |
|---|---|
| Step 2 | If there are
                                          			 more than two calls on the line, select a call from the call list and press Resume . |

| Step 1 | With two
                                          			 connected calls on the same line, select a call to make it the active call. The
                                          			 second call is put on hold. |
|---|---|
| Step 2 | Press Conference . |
| Step 3 | Press Calls to view the call list and select the caller to
                                          			 add to the conference. |
| Step 4 | Wait for the
                                          			 call to connect. |
| Step 5 | Press Conference to add the participant to your call. The
                                          			 conference begins. |
| Step 6 | (Optional) Repeat to add
                                          			 additional participants. |

| Step 1 | Press Transfer . |
|---|---|
| Step 2 | Enter phone
                                          			 number for the transfer destination. When you have
                                             				reached the maximum number of calls for your line, pressing Transfer allows you to select the calls from a list
                                             				of calls on the line. |
| Step 3 | Wait for the
                                          			 recipient to answer. |
| Step 4 | Press Transfer again. |

| Step 1 | Press Mute to turn Mute on. The Mute button is backlit by a solid, red light, and
                                          			 the sound base LEDs light red. |
|---|---|
| Step 2 | Press Mute again to turn Mute off. |

| Step 1 | Press Mute to turn Mute on. The Mute button is backlit by a solid, red light, and a
                                          			 mute icon displays on the screen. |
|---|---|
| Step 2 | Press Mute again to turn Mute off. |

| Step 1 | Enter a phone number. |
|---|---|
| Step 2 | Press Dial . |

| Step 1 | Press and hold
                                          			 star (*) for at least 1 second. The plus (+)
                                          			 sign displays as the first digit in the phone number. The
                                          			 corresponding key tone stops to indicate that the * has changed to a + sign. |
|---|---|
| Step 2 | Dial the
                                          			 international number, including the country code. |

| Step 1 | Press More . |
|---|---|
| Step 2 | Use the
                                          			 Navigation bar and Select button to scroll to the Private softkey. Press Private to enable this feature. Press Private to disable this feature if it is currently
                                             				enabled. |

| Step 1 | Press More . |
|---|---|
| Step 2 | Use the
                                          			 Navigation bar and Select button to locate and select QRT . The
                                             				information is sent to your system administrator. |

| To redial the
                                          			 last number you called, press Redial . |
|---|

| Step 1 | Press Transfer . |
|---|---|
| Step 2 | Enter the
                                          			 destination number. |
| Step 3 | Wait for the
                                          			 recipient to answer. |
| Step 4 | Press Transfer again. The transfer
                                             				completes. |

| Step 1 | Sign in to a
                                          			 WebDialer-enabled corporate directory and search for coworkers. |
|---|---|
| Step 2 | Select the
                                          			 number that you want to dial. |
| Step 3 | When prompted,
                                          			 enter your user ID and password. |
| Step 4 | If this is
                                          			 your first time using WebDialer, review the preferences on the Make Call
                                          			 window. |
| Step 5 | Select Dial . The call is
                                             				now placed on your phone line. |
| Step 6 | To end a call,
                                          			 select Hang
                                             				up in the Make Call window or press End
                                             				Call on your conference station. |

| Step 1 | Sign in to
                                          			 your User Option web pages. |
|---|---|
| Step 2 | Initiate a
                                          			 call using WebDialer to access the Make Call window. The Make Call
                                             				window displays the first time that you use WebDialer (after you select the
                                             				number that you want to dial). |
| Step 3 | Select one of
                                          			 the following options from the Make Call window: Preferred
                                                				  language: Determines the language used for WebDialer settings and prompts. Use
                                                				  preferred device: Identifies the Cisco Unified IP Phone (calling device) and
                                                				  directory number (calling line) that you use to place WebDialer calls. If you have
                                             				one phone with a single line, the appropriate phone and line are automatically
                                             				selected. |
| Step 4 | If the phone
                                          			 and line do not select automatically, choose a phone or line. If you have
                                             				more than one phone of the same type, the list identifies the phone by device
                                             				type and MAC address. To display the MAC address on your phone, select Apps > Phone
                                                   					 Information . |
| Step 5 | If you have an
                                          			 Extension Mobility profile, select Extension Mobility from the Calling Device drop-down
                                          			 menu in the Make Call window. |
| Step 6 | Ensure that
                                          			 you do not select Do not
                                             				display call information or Disable Auto Close . Do not
                                                   					 display call confirmation: If selected, the WebDialer Make Call window does not
                                                   					 display the next time WebDialer is used. Calls will automatically dial after
                                                   					 you select a contact from the Cisco directory. Disable
                                                   					 Auto Close: If selected, the call window does not close automatically after 15
                                                   					 seconds. |

| Note | Some features may not be available for your phone, and thus you can't set the features up in the Self Care Portal. |
|---|---|

| Step 1 | Obtain the
                                       			 portal URL, user ID, and default password from your administrator. Typically, the
                                          				portal URL is http://ip_address or hostname/ucmuser . |
|---|---|
| Step 2 | Open a web
                                       			 browser on your computer and enter the URL. |
| Step 3 | If prompted to
                                       			 accept security settings, select Yes or Install Certificate . |
| Step 4 | Enter your
                                       			 user ID in the Username field. |
| Step 5 | Enter your
                                       			 password in the Password field. |
| Step 6 | Select Login . |
| Step 7 | Select Logout to sign out. |