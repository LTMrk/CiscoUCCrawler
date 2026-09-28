---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8831-10-3-1-english-adminguide-cs38-bk-ad57597a-00-adminguide-8831-cs-be5a81ffc8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8831/10_3_1/english/AdminGuide/CS38_BK_AD57597A_00_adminguide-8831/CS38_BK_AD57597A_00_adminguide-8831_chapter_0101.html
retrieved_at: 2026-08-21T13:38:06.255351+00:00
---

Cisco Unified IP Conference Phone 8831 and 8831NR Administration Guide

# Cisco Unified IP Conference Phone 8831 and 8831NR Administration Guide

Updated: November 17, 2014

Chapter: Features,
	 Templates, Services, and User Setup

## Chapter: Features,
	 Templates, Services, and User Setup

# Features,
                     	 Templates, Services, and User Setup

## Features,
                        	 Templates, Services, and User Setup Overview

After you install conferences stations in your network, configure
                           		network settings, and add each 
                           		Cisco Unified IP Conference Phone
                           		to Cisco Unified
                              				Communications Manager ,
                           		you must use the Cisco Unified
                              				Communications Manager Administration application to configure telephony features, optionally modify conference phone
                           		templates, set up services, and assign users.

This chapter provides an overview of these configuration and setup
                           		procedures. Cisco Unified
                              				Communications Manager documentation provides detailed instructions for these procedures.

For suggestions about how to provide users with information about
                           		features, and what information to provide, see Internal Support Website .

For information about setting up conference phones in non-English
                           		environments, see International User Support .

## Available
                        	 Telephony Features

After you
                           		add Cisco Unified IP Conference Phones to Cisco Unified Communications Manager, you can
                           		add functionality. The following table includes a list of supported telephony
                           		features. You can use Cisco Unified Communications Manager Administration to
                           		configure many of these features. The Reference column lists Cisco Unified
                           		Communications Manager and other documentation that contains configuration
                           		procedures and related information.

For information about the use of these features on the phone, see the Cisco Unified IP Conference Phone 8831 and 8831NR User Guide .

Cisco Unified
                                       		  Communications Manager Administration also provides several service parameters
                                       		  that are used to configure various telephony functions. For more information
                                       		  about access and configuration of service parameters, see the Cisco
                                          			 Unified Communications Manager Administration Guide .

For more
                                       		  information on the functions of a service, select the name of the parameter or
                                       		  the question mark help button in the Service Parameter Configuration window in
                                       		  CUCM Administration.

Feature

Description

Configuration Reference

Agent
                                       				Greeting

Allows an
                                       				agent to create and update a prerecorded greeting that plays at the beginning
                                       				of a call, such as a customer call, before the agent begins the conversation
                                       				with the caller. The agent can prerecord a single greeting or multiple
                                       				greetings as needed.

To enable
                                       				Agent Greeting in the Cisco Unified Communications Manager Administration
                                       				application, choose Device > Phone , locate the IP Phone that you
                                       				want to configure. Scroll to the Device Information Layout pane and set
                                       				Built In Bridge to On or Default .

If Built In
                                       				Bridge is set to Default, in the Cisco Unified Communications Manager
                                       				Administration application, choose System > Service
                                             					 Parameter and select the appropriate Server and
                                       				Service. Scroll to the Clusterwide Parameters (Device - Phone) pane and set Builtin Bridge Enable to On .

For more
                                       				information, see the following:

- Features and Services
                                             					 Guide for Cisco Unified Communications Manager , "Barge
                                             					 and Privacy"

- Cisco Unified
                                             					 Communications Manager System Guide , "Cisco
                                             					 Unified IP Phones"

Any Call
                                       				Pickup

Allows users
                                       				to pick up a call on any line in their call pickup group, regardless of how the
                                       				call was routed to the phone.

For more
                                       				information, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Call
                                          				  Pickup" chapter.

Audible
                                       				Message Waiting Indicator (AMWI)

A stutter
                                       				tone indicates that a user has one or more new voice messages on a line.

The
                                                   				  stutter tone is line-specific. You hear it only when using the line with the
                                                   				  waiting messages.

For more
                                       				information, see Cisco
                                          				  Unified Communications Manager System Guide , "Cisco
                                          				  Unified IP Phones" chapter.

Auto Answer

Connects
                                       				incoming calls automatically after a ring or two.

For more
                                       				information, see Cisco
                                          				  Unified Communications Manager Administration Guide , "Directory
                                          				  Number Setup" chapter.

Auto Pickup

Allows a
                                       				user to use one-touch pickup functionality for call pickup features.

For more
                                       				information, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Call
                                          				  Pickup" chapter.

Block
                                       				External to External Transfer

Prevents
                                       				users from transferring an external call to another external number.

For more
                                       				information, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "External
                                          				  Call Transfer Restrictions" chapter.

Call Back

Provides
                                       				users with an audio and visual alert on the phone when a busy or unavailable
                                       				party becomes available.

For more
                                       				information, see the following:

- Cisco Unified
                                             					 Communications Manager System Guide , "Cisco
                                             					 Unified IP Phones"

- Features and Services
                                             					 Guide for Cisco Unified Communications Manager , "Cisco
                                             					 Call Back"

Call Display
                                       				Restrictions

Determines
                                       				the information that will display for calling or connected lines, depending on
                                       				the parties who are involved in the call.

For more
                                       				information, see:

- Cisco Unified
                                             					 Communications Manager Administration Guide , "Cisco
                                             					 Unified IP Phone Setup"

- Cisco Unified
                                             					 Communications Manager System Guide , "Understanding Route Plans"

- Features and Services
                                             					 Guide for Cisco Unified Communications Manager , "Call
                                             					 Display Restrictions"

Call Forward

Allows users
                                       				to redirect incoming calls to another number. Call Forward options include Call
                                       				Forward All, Call Forward Busy, Call Forward No Answer, and Call Forward No
                                       				Coverage.

For more
                                       				information, see the following:

- Cisco Unified
                                             					 Communications Manager Administration Guide , "Directory Number Setup"

- Cisco Unified
                                             					 Communications Manager System Guide , "Cisco
                                             					 Unified IP Phones"

Customize Cisco Unified Communications Manager Self Care Portal display

Call Forward
                                       				All Loop Breakout

Detects and
                                       				prevents Call Forward All loops. When a Call Forward All loop is detected, the
                                       				Call Forward All configuration is ignored and the call rings through.

For more
                                       				information, see Cisco
                                          				  Unified Communications Manager System Guide , "Cisco
                                          				  Unified IP Phones" chapter.

Call Forward
                                       				All Loop Prevention

Prevents a
                                       				user from configuring a Call Forward All destination directly on the phone that
                                       				creates a Call Forward All loop or that creates a Call Forward All chain with
                                       				more hops than the existing Forward
                                          				  Maximum Hop Count service parameter allows.

For more
                                       				information, see Cisco
                                          				  Unified Communications Manager System Guide , "Cisco
                                          				  Unified IP Phones" chapter.

Call Forward
                                       				Configurable Display

Allows you
                                       				to specify information that appears on a phone when a call is forwarded. This
                                       				information can include the caller name, caller number, redirected number, and
                                       				original dialed number.

For more
                                       				information, see the following:

- Cisco Unified
                                             					 Communications Manager Administration Guide , "Directory Number Setup"

- Cisco Unified
                                             					 Communications Manager System Guide , "Cisco
                                             					 Unified IP Phones"

Call Forward
                                       				Destination Override

Allows you
                                       				to override Call Forward All (CFA) in cases where the CFA target places a call
                                       				to the CFA initiator. This feature allows the CFA target to reach the CFA
                                       				initiator for important calls. The override works whether the CFA target phone
                                       				number is internal or external.

For more
                                       				information, see the Cisco
                                          				  Unified Communications Manager System Guide , "Directory
                                          				  Numbers" chapter.

Call Forward
                                       				Notification

Allows you
                                       				to configure the information that the user sees when receiving a forwarded
                                       				call.

For more
                                       				information, see Call Forward Notification setup.

Call History
                                       				for Shared Line

Log
                                                					 missed calls for a shared line

Log
                                                					 answered calls for a shared line

For more
                                       				information, see Enable Call History for shared line.

Call Park

Allows users
                                       				to park (temporarily store) a call and then retrieve the call by using another
                                       				phone in the Cisco Unified Communications Manager system.

For more
                                       				information, see the Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Call Park
                                          				  and Directed Call Park" chapter.

Call Pickup

Allows users
                                       				to redirect a call that is ringing on another phone within their pickup group
                                       				to their phone.

You can
                                       				configure an audio and visual alert for the primary line on the phone. This
                                       				alert notifies the users that a call is ringing in their pickup group.

For more
                                       				information, see the Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Call
                                          				  Pickup" chapter.

Call
                                       				Recording

Allows a
                                       				supervisor to record an active call. The user might hear a recording audible
                                       				alert tone during a call when it is being recorded.

When a call
                                       				is secured, the security status of the call is displayed as a lock icon on
                                       				Cisco Unified IP Phones. The connected parties might also hear an audible alert
                                       				tone that indicates the call is secured and is being recorded.

When an
                                                   				  active call is being monitored or recorded, you can receive or place intercom
                                                   				  calls; however, if you place an intercom call, the active call will be put on
                                                   				  hold, which causes the recording session to terminate and the monitoring
                                                   				  session to suspend. To resume the monitoring session, the party whose call is
                                                   				  being monitored must resume the call.

For more
                                       				information, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Monitoring
                                          				  and Recording" chapter.

Call Waiting

Indicates
                                       				(and allows users to answer) an incoming call that rings while on another call.
                                       				Incoming call information appears on the phone display.

For more
                                       				information, see:

Cisco Unified
                                                						Communications Manager System Guide , "Directory Numbers"

Phone
                                             					 Call Waiting setup

Caller ID

Caller
                                       				identification such as a phone number, name, or other descriptive text appear
                                       				on the phone display.

For more
                                       				information, see:

- Cisco Unified
                                             					 Communications Manager Administration Guide , "Cisco
                                             					 Unified IP Phone Setup"

- Cisco Unified
                                             					 Communications Manager System Guide , "Understanding Route Plans"

- Features and Services
                                             					 Guide for Cisco Unified Communications Manager , "Call
                                             					 Display Restrictions"

- Cisco Unified
                                             					 Communications Manager Administration Guide , "Directory Number Setup"

Caller ID
                                       				Blocking

Allows a
                                       				user to block their phone number or email address from phones that have caller
                                       				identification enabled.

For more
                                       				information, see:

- Cisco Unified
                                             					 Communications Manager System Guide , "Understanding Route Plans"

- Cisco Unified
                                             					 Communications Manager Administration Guide , "Directory Number Setup"

Calling
                                       				Party Normalization

Calling
                                       				party normalization presents phone calls to the user with a dialable phone
                                       				number. Any escape codes are added to the number so that the user can easily
                                       				connect to the caller again. The dialable number is saved in the call history
                                       				and can be saved in the Personal Address Book.

For more
                                       				information, see Calling Party Normalization.

cBarge

Allows a
                                       				user to join a nonprivate call on a shared phone line. cBarge adds a user to a
                                       				call and converts it into a conference, allowing the user and other parties to
                                       				access conference features

For more
                                       				information, see:

- Cisco Unified
                                             					 Communications Manager Administration Guide , "Cisco
                                             					 Unified IP Phone Setup"

- Cisco Unified
                                             					 Communications Manager System Guide , "Cisco
                                             					 Unified IP Phones"

- Features and Services
                                             					 Guide for Cisco Unified Communications Manager , "Barge
                                             					 and Privacy"

Cisco
                                       				Extension Mobility

Allows users
                                       				to temporarily access their Cisco Unified IP Phone configuration such as line
                                       				appearances and services from a shared Cisco Unified IP Phone by
                                       				logging into the Cisco Extension Mobility service on that phone when they log
                                       				into the Cisco Extension Mobility service on that phone.

Cisco
                                       				Extension Mobility can be useful if users work from a variety of locations
                                       				within your company or if they share a workspace with coworkers.

For more
                                       				information, see " Extension
                                          				  Mobility" chapter in the Cisco
                                          				  Unified Communications Manager Features and Services Guide .

Cisco
                                       				Unified Communications Manager Express (Unified CME) Version Negotiation

The Cisco
                                       				Unified Communication Manager Express uses a special tag in the information
                                       				sent to the phone to identify itself. This tag enables the phone to provide
                                       				services to the user that the switch supports.

For more
                                       				information, see:

Cisco
                                             					 Unified Communications Manager Express System Administrator Guide

Cisco
                                       				WebDialer

Allows users
                                       				to make calls from web and desktop applications.

For more
                                       				information, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Web
                                          				  Dialer" chapter.

Conference

- Allows a user to talk
                                          				  simultaneously with multiple parties by calling each participant individually.
                                          				  Conference features include Conference and Meet Me.

- Allows a noninitiator in
                                          				  a standard (ad hoc) conference to add or remove participants; also allows any
                                          				  conference participant to join together two standard conferences on the same
                                          				  line.

The service
                                       				parameter, Advance Adhoc Conference, (disabled by default in Cisco Unified
                                       				Communications Manager Administration) allows you to enable these features.

For
                                       				information on conferences, see Cisco Unified Communications Manager System Guide , "Conference
                                          				  Bridges" chapter.

For more
                                       				information, see Cisco
                                          				  Unified Communications Manager System Guide , "Cisco
                                          				  Unified IP Phones" chapter.

Be sure to
                                                   				  inform your users whether these features are activated.

CTI
                                       				Applications

A computer
                                       				telephony integration (CTI) route point can designate a virtual device to
                                       				receive multiple, simultaneous calls for application-controlled redirection.

For more
                                       				information, see Cisco
                                          				  Unified Communications Manager Administration Guide , "CTI Route
                                          				  Point Setup" chapter.

Device
                                       				Invoked Recording

Provides end
                                       				users with the ability to record their telephone calls via a softkey.

In addition
                                       				administrators may continue to record telephone calls via the CTI User
                                       				Interface.

For more
                                       				information, see Enable Device Invoked Recording.

Directed
                                       				Call Park

Allows a user to transfer an active call to an available directed call park number that the user dials.

If you
                                                   				  implement Directed Call Park, avoid configuring the Park softkey. This prevents
                                                   				  users from confusing the two Call Park features.

For more
                                       				information, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Call Park
                                          				  and Directed Call Park" chapter.

Directed
                                       				Call Pickup

Allows a
                                       				user to answer a call that is ringing on a particular directory number.

For more
                                       				information, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Call
                                          				  Pickup" chapter.

Direct
                                       				Transfer

Allows users
                                       				to connect two calls to each other without remaining on the line.

For more
                                       				information, see Cisco
                                          				  Unified Communications Manager System Guide , “Cisco Unified IP Phones”
                                       				chapter.

Distinctive
                                       				Ring

Users can
                                       				customize how their phone indicates an incoming call and a new voice mail
                                       				message.

For more
                                       				information, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Call
                                          				  Pickup" chapter.

Divert

Allows a
                                       				user to transfer a ringing, connected, or held call directly to a
                                       				voice-messaging system. When a call is diverted, the line becomes available to
                                       				make or receive new calls.

For more
                                       				information, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Immediate
                                          				  Divert" chapter.

Do Not
                                       				Disturb (DND)

When DND is
                                       				turned on, either no audible rings occur during the ringing-in state of a call,
                                       				or no audible or visual notifications of any type occur.

The
                                       				following DND-related parameters are configurable in Cisco Unified
                                       				Communications Manager Administration:

- Do Not Disturb: This
                                          				  check box allows you to enable DND on a per-phone basis. Use Cisco Unified
                                                						Communications Manager Administration > Device > Phone > Phone
                                                						Configuration .

- DND Incoming Call Alert:
                                          				  Choose the type of alert to play, if any, on a phone for incoming calls when
                                          				  DND is active. This parameter is located on both the Common Phone Profile page
                                          				  and the Phone configuration page (Phone Configuration window value takes
                                          				  precedence).

For more
                                       				information, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Do Not
                                          				  Disturb" chapter.

EnergyWise

Enables an
                                       				IP Phone to sleep (power down) and wake (power up) at predetermined times, to
                                       				promote energy savings.

For more
                                       				information, see EnergyWise on the Cisco Unified IP Phone setup.

Enhanced
                                       				Room Coverage

Optional
                                       				microphone extension kits provide enhanced room coverage that can be further
                                       				expanded by linking two units together in Linked Mode.

Cisco Unified IP
                                                   						Conference Phone 8831 User Guide for Cisco Unified Communication
                                                   						Manager , "Conference Phone Link Mode" chapter.

Cisco Unified IP
                                                   						Conference Phone 8831 User Guide for Cisco Unified Communication
                                                   						Manager , "Enhanced Room Coverage" chapter.

Fast Dial
                                       				Service

Allows a
                                       				user to enter a Fast Dial code to place a call. Fast Dial codes can be assigned
                                       				to phone numbers or Personal Address Book entries. (See "Services" in this table.)

For more
                                       				information, see Modify phone button template for PAB or Fast Dial.

Group Call
                                       				Pickup

Allows a
                                       				user to answer a call that is ringing on a directory number in another group.

For more
                                       				information, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Call
                                          				  Pickup" chapter.

Hold
                                       				Reversion

Limits the
                                       				amount of time that a call can be on hold before reverting back to the phone
                                       				that put the call on hold and alerting the user.

Reverting
                                       				calls are distinguished from incoming calls by a single ring (or beep,
                                       				depending on the new call indicator setting for the line). This notification
                                       				repeats at intervals if not resumed.

A call that
                                       				triggers Hold Reversion also displays an animated icon in the call bubble.

You can
                                       				configure call focus priority to favor incoming or reverting calls.

For more
                                       				information about configuring this feature, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Hold
                                          				  Reversion" chapter.

Hold Status

Enables
                                       				phones with a shared line to distinguish between the local and remote lines
                                       				that placed a call on hold.

No
                                       				configuration is required.

Hold/Resume

Allows the
                                       				user to move a connected call from an active state to a held state.

- Requires no
                                          				  configuration, unless you want to use Music On Hold. See "Music On
                                             					 Hold" in this table for information.

- See "Hold
                                             					 Reversion" in this table.

HTTP
                                       				Download

Enhances the
                                       				file download process to the phone to use HTTP by default. If the HTTP download
                                       				fails, the phone reverts to using the TFTP download.

No
                                       				configuration is required.

Jitter
                                       				Buffer

The Jitter
                                       				Buffer feature handles jitter from 10 milliseconds (ms) to 1000 ms for both
                                       				audio and video streams.

No
                                       				configuration required.

Linked Mode

Enhances the
                                       				audio coverage area by using a daisy cable to connect two conference phone
                                       				Sound Base units.

When linked,
                                       				voice, dial tone, ringer and base LED features are synchronized between the two
                                       				devices.

Cisco Unified IP
                                                   						Conference Phone 8831 User Guide , "Conference Phone Link Mode"

Malicious
                                       				Caller Identification (MCID)

Allows users
                                       				to notify the system administrator about suspicious calls that are received.

For more
                                       				information, see:

- Cisco
                                             					 Unified Communications Manager System Guide , "Cisco
                                             					 Unified IP Phones"

- Features and Services
                                             					 Guide for Cisco Unified Communications Manager , "Malicious Call Identification"

Meet Me
                                       				Conference

Allows a
                                       				user to host a Meet Me conference in which other participants call a
                                       				predetermined number at a scheduled time.

For more
                                       				information, see Cisco
                                          				  Unified Communications Manager Administration Guide , "Meet-Me
                                          				  Number and Pattern Setup" chapter.

Message
                                       				Waiting

Defines
                                       				directory numbers for message waiting on and off indicators. A
                                       				directly-connected voice-message system uses the specified directory number to
                                       				set or to clear a message waiting indication for a particular Cisco Unified IP
                                       				Phone.

For more
                                       				information, see the following:

- Cisco Unified
                                             					 Communications Manager Administration Guide , "Message
                                             					 Waiting Setup"

- Cisco Unified
                                             					 Communications Manager System Guide , "Voice
                                             					 Mail Connectivity to Cisco Unified Communications Manager"

Message
                                       				Waiting Indicator

Displays a
                                       				New Voicemail status message on the phone screen.

For more
                                       				information see:

- Cisco Unified
                                             					 Communications Manager Administration Guide , "Message
                                             					 Waiting Setup"

- Cisco Unified
                                             					 Communications Manager System Guide , "Voice
                                             					 Mail Connectivity to Cisco Unified Communications Manager"

Missed Call
                                       				Logging

Allows a
                                       				user to specify whether missed calls will be logged in the missed calls
                                       				directory for a given line appearance.

For more
                                       				information, see Cisco
                                          				  Unified Communications Manager Administration Guide , "Directory
                                          				  Number Setup" chapter.

Mobile
                                       				Connect

Enables
                                       				users to manage business calls using a single phone number and pick up
                                       				in-progress calls on the desk phone and a remote device such as a mobile phone.
                                       				Users can restrict the group of callers according to phone number and time of
                                       				day.

For more
                                       				information, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Cisco
                                          				  Unified Mobility" chapter.

Mobile Voice
                                       				Access

Extends
                                       				Mobile Connect capabilities by allowing users to access an interactive voice
                                       				response (IVR) system to originate a call from a remote device such as a
                                       				cellular phone.

For more
                                       				information, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Cisco
                                          				  Unified Mobility" chapter.

Monitoring
                                       				and Recording

Allows a
                                       				supervisor to silently monitor an active call. The supervisor cannot be heard
                                       				by either party on the call. The user might hear a monitoring audible alert
                                       				tone during a call when it is being monitored.

When a call
                                       				is secured, the security status of the call is displayed as a lock icon on
                                       				Cisco Unified IP Phones. The connected parties might also hear an audible alert
                                       				tone that indicates the call is secured and is being monitored.

When an
                                                   				  active call is being monitored or recorded, the use can receive or place
                                                   				  intercom calls; however, if the user place an intercom call, the active call
                                                   				  will be put on hold, which causes the recording session to terminate and the
                                                   				  monitoring session to suspend. To resume the monitoring session, the party
                                                   				  whose call is being monitored must resume the call.

For more
                                       				information, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Monitoring
                                          				  and Recording" chapter.

Mute

Mutes the
                                       				conference phone from the Sound Base, DCU or connected external microphones.

Requires no
                                       				configuration.

No Alert
                                       				Name

Makes it
                                       				easier for end users to identify transferred calls by displaying the original
                                       				caller’s phone number. The call appears as an Alert Call followed by the
                                       				caller’s telephone number.

Requires no
                                       				configuration.

Onhook
                                       				Dialing

Allows a
                                       				user to dial a number without going off hook.

For more
                                       				information, see Cisco
                                          				  Unified IP Conference Phone 8831 User Guide .

Other Group
                                       				Pickup

Allows a
                                       				user to answer a call ringing on a phone in another group that is associated
                                       				with the user's group.

For more
                                       				information, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Call
                                          				  Pickup" chapter.

Phone
                                       				Display Message for Extension Mobility Users

This feature
                                       				enhances the phone interface for the Extension Mobility user by providing
                                       				friendly messages.

No
                                       				configuration required.

Plus Dialing

Allows the
                                       				user to dial E.164 numbers prefixed with a plus (+)  sign.

To dial the
                                       				+ sign, the user needs to press and hold the star (*) key for at least 1
                                       				second. This applies to dialing the first digit for an on-hook (including edit
                                       				mode) or off-hook call.

No
                                       				configuration required.

Privacy

Prevents
                                       				users who share a line from adding themselves to a call and from viewing
                                       				information on their phone display about the call of the other user.

For more
                                       				information, see the following:

- Cisco Unified
                                             					 Communications Manager Administration Guide , "Cisco
                                             					 Unified IP Phone Setup"

- Cisco Unified
                                             					 Communications Manager System Guide , "Cisco
                                             					 Unified IP Phones"

- Features and Services
                                             					 Guide for Cisco Unified Communications Manager , "Barge
                                             					 and Privacy"

Quality
                                       				Reporting Tool (QRT)

Allows users
                                       				to submit information about problem phone calls by pressing a button. QRT can
                                       				be configured for either of two user modes, depending upon the amount of user
                                       				interaction desired with QRT.

For more
                                       				information, see:

- Cisco Unified
                                             					 Communications Manager System Guide , "Cisco
                                             					 Unified IP Phones"

- Features and Services
                                             					 Guide for Cisco Unified Communications Manager , "Quality
                                             					 Report Tool"

Recording Tone

Indicates if a recording tone is enabled for the phone.

For more information, see Recording Tone

Redial

Allows users
                                       				to call the most recently dialed phone number by pressing a button or the
                                       				Redial softkey.

Requires no
                                       				configuration.

Reroute
                                       				Direct Calls to Remote Destination to Enterprise Number

Reroutes a
                                       				direct call to a user's mobile phone to the enterprise number (desk phone). For
                                       				an incoming call to remote destination (mobile phone), only remote destination
                                       				rings; desk phone does not ring. When the call is answered on their mobile
                                       				phone, the desk phone displays a Remote In Use message. During these calls,
                                       				users can make use of various features of their mobile phone.

For more
                                       				information, see the Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Cisco
                                          				  Unified Mobility" chapter.

Remote Port
                                       				Configuration

Allows the
                                       				administrator to configure the speed and duplex function of the phone Ethernet
                                       				ports remotely by using Cisco Unified Communications Manager Administration.
                                       				This enhances the performance for large deployments with specific port
                                       				settings.

If the
                                                   				  ports are configured for Remote Port Configuration in Cisco Unified
                                                   				  Communications Manager, the data cannot be changed on the phone.

To configure
                                       				the parameter in the Cisco Unified Communications Manager Administration
                                       				application, choose Device > Phone , select the appropriate IP
                                       				phone, and scroll to the Product Specific Configuration Layout pane (Switch
                                       				Port Remote Configuration or PC Port Remote Configuration).

To configure
                                       				the setting on multiple phones simultaneously, configure the remote
                                       				configuration in either Enterprise Phone Configuration ( System > Enterprise Phone
                                             					 Configuration ) or Common Phone Profile Configuration
                                       				( Device > Device
                                             					 Settings > Common Phone Profile . (Switch Port
                                       				Remote Configuration or PC Port Remote Configuration.)

Ringtone
                                       				Setting

Identifies
                                       				ring type used for a line when a phone has another active call.

- Cisco Unified
                                                					 Communications Manager Administration Guide , "Directory Number Setup"

Cisco Unified
                                                   						Communications Manager Administration Guide , "Custom
                                                   						Phone Rings"

Secure
                                       				Conference

- Allows secure phones to
                                          				  place conference calls using a secured conference bridge.

- As new participants are
                                          				  added by using Conf, Join, cBarge, Barge softkeys or MeetMe conferencing, the
                                          				  secure call icon displays as long as all participants use secure phones.

- The Conference List
                                          				  displays the security level of each conference participant. Initiators can
                                          				  remove nonsecure participants from the Conference List. (Non-initiators can add
                                          				  or remove conference participants if the Advanced Adhoc Conference Enabled
                                          				  parameter is set.)

For more
                                       				information about security, see Supported Security
                                          				  Features .

For
                                       				additional information, see the following:

- Cisco Unified
                                             					 Communications Manager System Guide , "Conference Bridges"

- Cisco Unified
                                             					 Communications Manager Administration Guide , "Conference Bridge Setup"

- Cisco Unified
                                             					 Communications Manager Security Guide

Services

Allows you
                                       				to use the Cisco Unified IP Phone Services Configuration menu in Cisco
                                       				Unified Communications Manager Administration to define and maintain the list
                                       				of phone services to which users can subscribe.

For more
                                       				information refer to:

- Cisco Unified
                                             					 Communications Manager Administration Guide , "Cisco
                                             					 Unified IP Phone Setup"

- Cisco Unified
                                             					 Communications Manager System Guide , "Cisco
                                             					 Unified IP Phone Services"

Shared Line

Allows a
                                       				user to have multiple phones that share the same phone number or allows a user
                                       				to share a phone number with a coworker.

For more
                                       				information, see Cisco
                                          				  Unified Communications Manager System Guide , "Directory
                                          				  Numbers" chapter.

Special Sequence for Factory Reset

Allows the phone manufacturer to reset the factory parameters.

No configuration required.

Time-of-Day
                                       				Routing

Restricts
                                       				access to specified telephony features by time period.

For more
                                       				information, see:

- Cisco Unified
                                             					 Communications Manager Administration Guide , "Time
                                             					 Period Setup"

- Cisco Unified
                                             					 Communications Manager System Guide , "Time-of-Day Routing"

Time Zone
                                       				Update

Updates the
                                       				Cisco Unified IP Phone with time zone changes.

For more
                                       				information, see Cisco
                                          				  Unified Communications Manager Administration Guide , "Date and
                                          				  Time Group Setup" chapter.

TLS Enhancements

Added in Firmware Release 10.3(1)SR3.

Improved security with the parameter Disable TLS1.0 and TLS1.1 for web access in Cisco Unified Communications Manager. When set to enabled, the phones support only TLS1.2 mode. When set to disabled,
                                       TLS1.0, TLS1.1 and TLS1.2 are supported. This field applies to any phone or group of phones that function as a HTTPs server.

Transfer

Allows users
                                       				to redirect connected calls from their phones to another number.

Some
                                       				JTAPI/TAPI applications are not compatible with the Join and Direct Transfer
                                       				feature implementation on the conference phone and you may need to configure
                                       				the Join and Direct Transfer Policy to disable join and direct transfer on the
                                       				same line or possibly across lines.

Transfer -
                                       				Direct Transfer

Transfer:
                                       				The first invocation of Transfer will always initiate a new call by using the
                                       				same directory number, after putting the active call on hold.

Direct
                                       				Transfer: This transfer joins two established calls (call is in hold or in
                                       				connected state) into one call and drops the feature initiator from the call.
                                       				Direct Transfer does not initiate a consultation call and does not put the
                                       				active call on hold.

Some
                                       				JTAPI/TAPI applications are not compatible with the Join and Direct Transfer
                                       				feature implementation on the conference phone and you may need to configure
                                       				the Join and Direct Transfer Policy to disable join and direct transfer on the
                                       				same line or possibly across lines. For more information, see the <xref Join
                                       				and Direct Transfer Policy>.

UCR 2008

The
                                       				conference phone supports Unified Capabilities Requirements (UCR) 2008 by
                                       				providing support for 80-bit SRTCP Tagging.

As an
                                       				administrator, you must set up specific parameters in Cisco Unified
                                       				Communications Manager Administration.

See UCR 2008
                                       				setup.

Voice
                                       				Message System

Enables
                                       				callers to leave messages if calls are unanswered.

For more
                                       				information, see the following:

- Cisco Unified
                                             					 Communications Manager Administration Guide , "Cisco
                                             					 Voice-Mail Port Setup"

- Cisco Unified
                                             					 Communications Manager System Guide , "Voice
                                             					 Mail Connectivity to Cisco Unified Communications Manager"

Wideband
                                       				Ringtone

The Wideband
                                       				Ringtone feature supports 10 ringtones: 4 embedded in the phone firmware and 6
                                       				downloaded from the Cisco Unified Communications Manager.

For more
                                       				information, see the following:

- Cisco Unified
                                             					 Communications Manager Administration Guide , "Directory Number Setup"

Features and Services
                                                						Guide for Cisco Unified Communications Manager , "Custom
                                                						Phone Rings"

Wireless
                                       				Microphone Frequency Lock

Provides a
                                       				secure DECT frequency for wireless microphones by locking down the Wireless
                                       				Region setting.

No
                                       				configuration required for Firmware release 10.3(1) and later. Earlier releases
                                       				must upgrade to the current release to have the region setting locked.

Once you
                                                   				  have configured the Wireless Region setting, it cannot be updated. Further
                                                   				  configuration of this setting requires an RMA.

## Corporate and
                        	 Personal Directory Setup

Corporate
                                    			 Directory: Supports a global corporate directory that users can access on the
                                    			 conference phone to lookup phone numbers of coworkers. You must enable and
                                    			 configure the corporate directories before they can be used.

Personal
                                    			 Directory: Supports a personal address book (PAB) that allows a user to store a
                                    			 set of personal numbers. You must enable the feature and provide the user with
                                    			 a PIN and User ID to configure the features.

### Corporate
                           	 Directory Setup

Cisco Unified
                              		Communications Manager uses a Lightweight Directory Access Protocol (LDAP)
                              		directory to store authentication and authorization information about users of
                              		Cisco Unified Communications Manager applications that interface with Cisco
                              		Unified Communications Manager. Authentication establishes a user’s right to
                              		access the system. Authorization identifies the telephony resources that a user
                              		is permitted to use, such as a specific teleconference phone extension.

To install and set
                              		up these features, see Installing and
                                 		  Configuring the Cisco Customer Directory Configuration Plugin . This
                              		document guides you through the configuration process for integrating Cisco
                              		Unified Communications Manager with Microsoft Active Directory and Netscape
                              		Directory Server. For more information, see "Understanding
                                 		  Directory Numbers" in the Cisco Unified
                                 		  Communications Manager System Guide .

After the LDAP
                              		directory configuration is complete, users can access the Corporate Directory
                              		service on the conference phone to find co-workers in the corporate directory.

### Personal Directory
                           	 Setup

Personal Address
                                       			 Book (PAB)

Personal Fast
                                       			 Dials (Fast Dials)

From a web
                                       			 browser: Users can access the PAB from Cisco Unified Communications Manager
                                       			 Self Care Portal.

From the
                                       			 conference phone: Users can choose Contacts > Personal
                                             				  Directory to access the PAB and Fast Dials features
                                       			 from their conference phones.

To configure Personal
                              		Directory from a web browser, users must access Cisco Unified Communications
                              		Manager Self Care Portal. You must provide users with a URL and login
                              		information.

## Button
                        	 Templates

Using Cisco Unified
                           		Communications Manager Administration, you can assign button templates to
                           		conference phones. Cisco Unified Communications Manager contains the Standard
                           		8831 button template for the Cisco Unified IP Conference Phone 8831 and 8831NR. When you
                           		assign the Standard 8831 button template to a conference phone, no buttons are
                           		added, but the Privacy softkey can be enabled from this template.

If the button
                           		feature is not configurable using the Button Template it may be a softkey
                           		feature that is configurable using a softkey template. For more information on
                           		softkey templates, see Softkey Templates .

For more information
                           		on button templates, see the Cisco Unified
                              		  Communications Manager Administration Guide and Cisco Unified
                              		  Communications Manager System Guide .

### Add Phone Button Template

To add a button template,

Log on to Cisco Unified Communications Manager Administration.

Select Device > Device Settings > Phone Button Template .

Select Add New .

To assign a button template to a conference phone, choose Device > Phone to select the conference phone.

In the Phone Configuration window, select a button template from the Phone Button Template drop-down list.

## Softkey
                        	 Templates

Using Cisco Unified
                           		Communications Manager Administration, you can manage softkeys associated with
                           		applications that are supported by the conference phone. Cisco Unified
                           		Communications Manager supports the Standard User and Standard Feature softkey
                           		templates.

An application that
                           		supports softkeys can have one or more standard softkey templates associated
                           		with it. You can modify a standard softkey template by making a copy of it,
                           		giving it a new name, and making updates to that copied softkey template. You
                           		can also modify a nonstandard softkey template.

To configure softkey
                           		templates, select Device > Device
                                 			 Settings > Softkey Template from Cisco Unified
                           		Communications Manager Administration. To assign a softkey template to a
                           		conference phone, use the Softkey Template field in the Cisco Unified
                           		Communications Manager Administration Phone Configuration page.

The Cisco Unified IP
                           		Conference Phone does not support all the softkeys that are configurable
                           		in Softkey Template Configuration on Cisco Unified Communications Manager
                           		Administration. The following table lists the features and softkeys that can be
                           		configured on a softkey template, and note whether it is supported on the
                           		conference phone.

Cisco Unified
                                       		  Communications Manager allows you to configure any softkey in a softkey
                                       		  template, but unsupported softkeys do not display on the phone.

Feature

Configurable
                                       				Softkeys in the Softkey Template Configuration

Supported as a
                                       				Softkey

Notes

Answer

Answer
                                       				(Answer)

Yes

—

Barge

Barge (Barge)

Yes

Configure as a
                                       				softkey.

Call Back

Call Back
                                       				(CallBack)

Yes

—

Call Forward
                                       				All

Forward All
                                       				(cfwdAll)

Yes

Phone displays Fwd
                                          				  ALL or Fwd
                                          				  Off .

Call Park

Call Park
                                       				(Park)

Yes

—

Call Pickup

Pick Up
                                       				(Pickup)

Yes

Configure as
                                       				a softkey.

cBarge

Conference
                                       				Barge (cBarge)

Yes

Configure as
                                       				a softkey.

Conference

Conference
                                       				(Conf)

Yes

Phone
                                       				displays Conference when a call is connected.

Conference
                                       				List

Conference
                                       				List (ConfList)

Yes

Phone
                                       				displays ConfList when in a conference.

iDivert

Immediate
                                       				Divert (iDivert)

Yes

Phone
                                       				displays Divert .

Do Not
                                       				Disturb

Toggle Do
                                       				Not Disturb (DND)

Yes

Configure as
                                       				a softkey.

End Call

End Call
                                       				(EndCall)

Yes

Phone
                                       				displays Cancel if the call is not answered.

Group Pickup

Group Pick
                                       				Up (GPickUp)

Yes

Configure as
                                       				a softkey.

Hold

Hold (Hold)

Yes

Join

Join (Join)

No

—

Malicious
                                       				Call Identification

Toggle
                                       				Malicious Call Identification (MCID)

Yes

Configure
                                       				Malicious Call Identification as a softkey.

Meet Me

Meet Me
                                       				(MeetMe)

Yes

Configure as
                                       				a softkey.

Mobile
                                       				Connect

Mobility
                                       				(Mobility)

Yes

Configure
                                       				Mobile Connect as a softkey.

New Call

New Call
                                       				(NewCall)

Yes

Phone
                                       				displays New Call .

Other Pickup

Other Pickup
                                       				(oPickup)

Yes

Configure as
                                       				a softkey.

Quality
                                       				Reporting Tool

Quality
                                       				Reporting Tool (QRT)

Yes

Configure
                                       				Quality Reporting Tool as a softkey.

Redial

Redial
                                       				(Redial)

Yes

Phone
                                       				displays Redial when Off Hook.

Remove Last
                                       				Conference Participant

Remove Last
                                       				Conference Participant (Remove)

Yes

Phone
                                       				displays Remove when a participant is selected.

Resume

Resume
                                       				(Resume)

Yes

—

Transfer

Transfer

Yes

Phone
                                       				displays Transfer when a call is connected.

For more
                           	 information, see Cisco Unified
                              		Communications Manager Administration Guide , "Softkey Template
                              		Configuration" and the Cisco Unified
                              		Communications Manager System Guide , "Softkey
                              		Template" .

### Set Up Softkey
                           	 Templates

Log on to
                                          			 Cisco Unified Communications Manager Administration.

Select Device >
                                             				Device Settings > Softkey Template .

To assign a
                                          			 softkey template to a conference station, choose Device >
                                             				Phone to select the conference station.

In the Phone
                                          			 Configuration window, select a softkey template from the Softkey Template
                                          			 drop-down list.

## Recording
                        	 Tone

The Recording Tone
                              		  feature indicates whether a recording tone is enabled or disabled for the
                              		  phone. If this feature is enabled, all parties on a call hear the tone being
                              		  played, regardless of whether the call is recorded or not. The tone first
                              		  sounds when a call is answered.

Other related
                                          			 parameters — the recording tone frequency (in hz), the duration of the beep
                                          			 tone, and the beep tone interval (how often the beep tone plays) — are defined
                                          			 on a per-Network Locale basis in the xml file that defines tones. This xml file
                                          			 is named tones.xml or g3-tones.xml.

Parameter

Recording
                                          					 Tone Local Volume

Indicates
                                          					 the volume for the recording tone that the local party receives, if the local
                                          					 party phone has the Recording Tone option enabled.

This
                                          					 setting applies for each listening device, including the handset, speakerphone,
                                          					 and headset.

Range: 0
                                          					 percent (no tone) to 100 percent (same level as current volume setting on the
                                          					 phone).

Recording
                                          					 Tone Remote Volume

Indicates
                                          					 the volume for the recording tone that the remote party receives. The remote
                                          					 party is the party who is on a call with the party whose phone has the
                                          					 Recording Tone option enabled.

Range: 0
                                          					 percent to 100 percent. (0 percent is -66 dBM and 100 percent is -3 dBM).

Default:
                                          					 50 percent.

Recording
                                          					 Tone Duration

Indicates
                                          					 the length of time in milliseconds that the tone plays.

If the
                                          					 value is less than one third of the interval, this value overrides the default
                                          					 provided that the Network Locale provides.

Range: 0
                                          					 to 3000

For some
                                                      						Network Locales that use a complex cadence, this setting applies only to the
                                                      						first recording tone.

### Enable Recording
                           	 Tone

#### Before you begin

You must be familiar with the Recording Tone parameters before you
                                 		  enable this feature.

In Cisco Unified
                                          			 Communications Manager Administration, go to Device > Phone .

Select Enable from the pulldown menu In the Recording
                                          			 Tone section.

Enter a value between 0 and 100 per cent in the Recording Tone
                                          			 Local Volume field.

Enter a value between 0 and 100 per cent in the Recording Tone
                                          			 Remote Volume field.

Click Save .

## Enable Device Invoked Recording

Configure the Device Invoked Recording feature from  Cisco Unified Communications Manager. To enable this feature, perform
                              the following steps.

Set the  Built In Bridge to On .

Set Privacy to Off .

Set Recording Option to Selective Call Recording Enabled .

Select the appropriate Recording Profile.

## Enable Call
                        	 History for Shared Line

For the
                                             				purposes of this procedure, all references to a phone, device, or IP Phone
                                             				apply to the conference phone.

Go to Cisco
                                       			 Unified CM Administration and choose Device > Phone .

Find your
                                       			 conference phone in the list of phones associated with the Cisco Unified CM.

Click on the
                                       			 Device Name of the phone.

The Phone
                                          				Configuration window appears.

Go to Product
                                       			 Specific Configuration Layout area and from the Logging Display drop-down list
                                       			 box, choose the applicable profile.

The Disabled
                                          				option is selected by default.

Parameters
                                          				that you set in the Product Specific Configuration area may also appear in the
                                          				Device Configuration window for various devices and in the Enterprise Phone
                                          				Configuration window.

If you set
                                          				these same parameters in these other windows as well, the setting that takes
                                          				precedence is determined in the following order:

Device
                                                					 Configuration window settings

Common
                                                					 Phone Profile window settings

Enterprise
                                                					 Phone Configuration window settings

## Services
                        	 Setup

You can give users
                           		access to Cisco Unified IP Phone Services on the Cisco Unified IP Conference
                           		Phone. These services comprise XML applications that enable the display of
                           		interactive content with text and graphics on the conference phone. Examples of
                           		services include local movie times, stock quotes, and weather reports. Users
                           		access any configured services from the Apps softkey on the conference phone.

You must use
                                    			 Cisco Unified Communications Manager Administration to configure available
                                    			 services.

The user must subscribe to
                                    			 services by using the Cisco Unified Communications Self Care Portal. This
                                    			 web-based application provides a graphical user interface (GUI) for limited,
                                    			 end-user configuration of IP phone applications. However, a user cannot
                                    			 subscribe to any service that you configure as an enterprise subscription.

Before you set up
                           		services, gather the URLs for the sites you want to set up, and verify that
                           		users can access those sites from your corporate IP telephony network.

To set up these
                           		services choose Device > Device
                                 			 Settings > Phone Services from Cisco Unified
                           		Communications Manager. For more information, see the Cisco Unified
                              		  Communications Manager Administration Guide and Cisco Unified
                              		  Communications Manager System Guide .

After you configure
                           		these services, verify that your users have access to Cisco Unified
                           		Communications Manager Self Care Portal, from which they can select and
                           		subscribe to configured services. See IP Phone Features User Subscription and Setup for a summary of the information
                           		that you must provide to end users.

To configure Cisco
                                       		  Extension Mobility services for users, see "Cisco Unified
                                          			 Mobility" , Cisco Unified
                                          			 Communications Manager Features and Services Guide

## Cisco Unified Communications Manager User Addition

Adding users to Cisco Unified Communications Manager allows
                           		you to display and maintain information about users and allows each user to
                           		perform these tasks:

Access the corporate directory and other customized directories from
                                 			 a Cisco Unified IP Phone.

Create a personal directory.

Set up Call Forwarding numbers.

Subscribe to services that are accessible from a Cisco Unified IP
                                 			 Phone.

You can add users to Cisco Unified Communications Manager
                           		using either of these methods:

To add users individually, choose User Management > End
                                       				  User from Cisco Unified Communications Manager
                                 			 Administration.

For more information on  adding users, see 
                                 			 the Cisco Unified Communications Manager Administration
                                    				Guide . For details on user information, see the Cisco Unified
                                    			 Communications Manager System Guide .

To add users in batches, use the Bulk Administration Tool. This
                                 			 method also enables you to set an identical default password for all users.

For more information, see the Cisco Unified Communications Manager Bulk Administration
                                    				Guide .

To add users from your corporate LDAP directory, choose System > LDAP > LDAP System from Cisco Unified Communications Manager Administration.

After the Enable Synchronization from LDAP Server is enabled, you will not be able to add additional users from Cisco Unified
                                             Communications Manager Administration.

For more information on LDAP, see the Cisco Unified
                                    			 Communications Manager System Guide , "Understanding the Directory" .

To add a user and a phone at the same time, choose User Management > User/Phone Add from Cisco Unified Communications Manager.

## Call Waiting
                        	 Setup

The Cisco Unified IP
                           		Conference Phone supports six calls on a single line. With multiple calls per
                           		line, setting up call waiting is simplified on the Cisco Unified Communications
                           		Manager. For more information, see "Understanding
                              		  Directory Numbers" , Cisco Unified
                              		  Communications Manager System Guide .

## Call Forward
                        	 Notification Setup

You set
                              		  up the information that is displayed to the user from within Cisco Unified
                              		  Communications Manager Administration in the Device Configuration window
                              		  ( Device > Phone > Line > Forwarded Call Information
                                    				Display on Device ).

The following
                              		  table describes the Call Forward Notification fields.

Field

Description

Default
                                          					 Checkbox State

Caller
                                          					 Name

When this
                                          					 check box is checked, the caller name displays in the notification window.

Checked

Caller
                                          					 Number

When this
                                          					 check box is checked, the caller number displays in the notification window.

Not
                                          					 checked

Redirected
                                          					 Number

When this
                                          					 check box is checked, the information about the caller who last forwarded the
                                          					 call displays in the notification window.

Example:
                                          					 If Caller A calls B, but B has forwarded all calls to C and C has forwarded all
                                          					 calls to D, the notification box that D sees contains the phone information for
                                          					 caller C.

Not
                                          					 checked

Dialed
                                          					 Number

When this
                                          					 check box is checked, the information about the original recipient of the call
                                          					 displays in the notification window.

Example:
                                          					 If Caller A calls B, but B has forwarded all calls to C and C has forwarded all
                                          					 calls to D, then the notification box that D sees contains the phone
                                          					 information for caller B.

Checked

## Calling Party
                        	 Normalization

In line with E.164
                           		standards, calling party normalization enhances the dialing capabilities of
                           		some phones and improves call back functionality when a call is routed to
                           		multiple geographical locations. That is, the feature ensures that the called
                           		party can return a call without having to modify the directory number in the
                           		call log directories on the phone. Additionally, calling party normalization
                           		allows the user to globalize and localize phone numbers, so the appropriate
                           		calling number presentation displays on the phone.

The conference phone
                           		supports the following functions:

For the final
                                 			 presentation of the calling number to the user, the conference phone screen
                                 			 displays the calling number based on the international, national, or local
                                 			 subscriber numbers.

If the call
                                       				  is an intra-city call, the calling number presented on the conference phone is
                                       				  displayed in the subscriber number format (without the area or city code).

For
                                       				  intercity calls, the calling number is presented in a national number format.

If the call
                                       				  is an international call, the calling number is presented with the E.164
                                       				  format, with the plus (+) prefix digit.

The call logs
                                 			 directories record the calling number in the received and missed call logs with
                                 			 the appropriate escape codes (9/0, 0/1, +). The user can go into directories,
                                 			 and select and dial one of these entries with the escape code without having to
                                 			 edit the number.

Configuring calling
                           		party normalization alleviates issues with toll bypass where the call is routed
                           		to multiple locations over the IP WAN. In addition, it allows Cisco Unified
                           		Communications Manager to distinguish the origin of the call to globalize or
                           		localize the calling party number for the conference phone user.

The conference phone
                           		itself can localize the calling party number. For the phone to localize the
                           		calling party number, you must configure the Calling Party Transformation CSS
                           		or the Use Device Pool Device Calling Party Transformation CSS setting in the
                           		Phone Configuration window.

Depending on your
                           		configuration for globalizing and localizing the calling party number, the
                           		phone user may see a localized number, a globalized number with access codes
                           		and prefixes, or the international escape character, +, in the calling party
                           		number. If a phone supports calling party normalization, the phone can show the
                           		localized calling party number on the conference phone screen and the
                           		globalized number in the call log directories on the conference phone.

In addition, these
                           		devices show both the globalized and localized calling party number in the Call
                           		Details. If a conference phone does not support calling party normalization,
                           		the device shows the localized calling party on the conference phone screen and
                           		in the call log directories on the phone.

For information on
                           		how to configure this feature for your conference phone, see "Calling Party
                              		  Normalization" , Cisco Unified
                              		  Communications Manager Features and Services Guide .

## Incoming Call
                        	 Notification Window Timer Setup

You can
                              		  set the time that the Incoming Call Notification Window, sometimes called a
                              		  toast, displays on the conference phone. You set up the feature from one of the
                              		  following Cisco Unified Communications Manager windows:

Enterprise
                                    				Phone Configuration ( System > Enterprise
                                          					 Phone )

Common Phone
                                    				Profile Configuration ( Device > Device
                                          					 Settings > Common Phone Profile )

Phone
                                    				Configuration ( Device > Phone )

The
                              		  following table describes the Incoming Call Toast Timer.

Field

Description

Incoming
                                          					 Call Toast Timer

Gives the
                                          					 time, in seconds, that the toast displays. The time includes the fade-in and
                                          					 fade-out times for the window.

The
                                          					 possible values are 3, 4, 5, 6, 7, 8, 9, 10, 15, 30, and 60.

5
                                          					 seconds.

## Linked
                        	 Mode

Two conference phone
                           		Sound Base units can be linked together to expand the audio coverage area. One
                           		Sound Base acts as the primary device, and the other unit acts as the dependant
                           		or secondary device.

In Linked Mode, the
                           		primary base station supports either one wireless or one wired microphone. The
                           		secondary unit supports only one wired microphone. You cannot mix microphone
                           		kits: if you plan to connect a microphone to both sound bases, they must both
                           		be wired microphones.

The Cisco Unified IP Conference Phone 8831 supports wired and wireless microphones. The Cisco Unified IP Conference Phone
                           8831NR supports only wired microphones.

The voice, dial
                           		tone, ringer, and base LED features synchronize between the two devices when
                           		linked together. You can link two sound bases while a call is active.

When Linked Mode is
                           		active, the linked mode icon displays in the idle and the call screens.

The following table
                           		summarizes the best practice to follow when deploying your conference phones in
                           		Linked Mode. If the devices are linked in this manner, the system software
                           		automatically detects which device is to be used as the primary and which is
                           		the secondary one.

If a DCU is
                                       		connected to the secondary device, it will display a prompt indicating that it
                                       		is a dummy DCU, but will otherwise not function.

When using a Sound
                                       		Base in Linked Mode, the primary base unit must be connected using the
                                       		CP-PWR-CUBE-3 external power supply.

If two devices are
                           	 linked after both are registered, the user can select which is the primary
                           	 device.

A secondary device
                           	 receives upgrades to firmware seamlessly from the primary device.

### Link Conference Phones

Use a daisy cable to connect two sound base units in Linked mode. This procedure describes the best practice for connecting
                                 the two units.

Connect the DCU to the conference phone to be used as the primary unit.

Connect the network cable to the conference phone to be used as the primary unit.

Connect the power cable to the primary device and plug into a wall plug.

The secondary Sound Base does not need to be plugged into external power, but in Linked Mode the primary unit must be connected
                                             to external power.

Use the provided daisy cable to connect the primary unit to the secondary sound base.

Voice, dial tone, ringer and base LEDs synchronize between the two units.

| Note | Cisco Unified
                                       		  Communications Manager Administration also provides several service parameters
                                       		  that are used to configure various telephony functions. For more information
                                       		  about access and configuration of service parameters, see the Cisco
                                          			 Unified Communications Manager Administration Guide . For more
                                       		  information on the functions of a service, select the name of the parameter or
                                       		  the question mark help button in the Service Parameter Configuration window in
                                       		  CUCM Administration. |
|---|---|

| Feature | Description | Configuration Reference |
|---|---|---|
| Agent
                                       				Greeting | Allows an
                                       				agent to create and update a prerecorded greeting that plays at the beginning
                                       				of a call, such as a customer call, before the agent begins the conversation
                                       				with the caller. The agent can prerecord a single greeting or multiple
                                       				greetings as needed. To enable
                                       				Agent Greeting in the Cisco Unified Communications Manager Administration
                                       				application, choose Device > Phone , locate the IP Phone that you
                                       				want to configure. Scroll to the Device Information Layout pane and set
                                       				Built In Bridge to On or Default . If Built In
                                       				Bridge is set to Default, in the Cisco Unified Communications Manager
                                       				Administration application, choose System > Service
                                             					 Parameter and select the appropriate Server and
                                       				Service. Scroll to the Clusterwide Parameters (Device - Phone) pane and set Builtin Bridge Enable to On . | For more
                                       				information, see the following: Features and Services
                                             					 Guide for Cisco Unified Communications Manager , "Barge
                                             					 and Privacy" Cisco Unified
                                             					 Communications Manager System Guide , "Cisco
                                             					 Unified IP Phones" |
| Any Call
                                       				Pickup | Allows users
                                       				to pick up a call on any line in their call pickup group, regardless of how the
                                       				call was routed to the phone. | For more
                                       				information, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Call
                                          				  Pickup" chapter. |
| Audible
                                       				Message Waiting Indicator (AMWI) | A stutter
                                       				tone indicates that a user has one or more new voice messages on a line. Note The
                                                   				  stutter tone is line-specific. You hear it only when using the line with the
                                                   				  waiting messages. | Note | The
                                                   				  stutter tone is line-specific. You hear it only when using the line with the
                                                   				  waiting messages. | For more
                                       				information, see Cisco
                                          				  Unified Communications Manager System Guide , "Cisco
                                          				  Unified IP Phones" chapter. |
| Note | The
                                                   				  stutter tone is line-specific. You hear it only when using the line with the
                                                   				  waiting messages. |
| Auto Answer | Connects
                                       				incoming calls automatically after a ring or two. | For more
                                       				information, see Cisco
                                          				  Unified Communications Manager Administration Guide , "Directory
                                          				  Number Setup" chapter. |
| Auto Pickup | Allows a
                                       				user to use one-touch pickup functionality for call pickup features. | For more
                                       				information, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Call
                                          				  Pickup" chapter. |
| Block
                                       				External to External Transfer | Prevents
                                       				users from transferring an external call to another external number. | For more
                                       				information, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "External
                                          				  Call Transfer Restrictions" chapter. |
| Call Back | Provides
                                       				users with an audio and visual alert on the phone when a busy or unavailable
                                       				party becomes available. | For more
                                       				information, see the following: Cisco Unified
                                             					 Communications Manager System Guide , "Cisco
                                             					 Unified IP Phones" Features and Services
                                             					 Guide for Cisco Unified Communications Manager , "Cisco
                                             					 Call Back" |
| Call Display
                                       				Restrictions | Determines
                                       				the information that will display for calling or connected lines, depending on
                                       				the parties who are involved in the call. | For more
                                       				information, see: Cisco Unified
                                             					 Communications Manager Administration Guide , "Cisco
                                             					 Unified IP Phone Setup" Cisco Unified
                                             					 Communications Manager System Guide , "Understanding Route Plans" Features and Services
                                             					 Guide for Cisco Unified Communications Manager , "Call
                                             					 Display Restrictions" |
| Call Forward | Allows users
                                       				to redirect incoming calls to another number. Call Forward options include Call
                                       				Forward All, Call Forward Busy, Call Forward No Answer, and Call Forward No
                                       				Coverage. | For more
                                       				information, see the following: Cisco Unified
                                             					 Communications Manager Administration Guide , "Directory Number Setup" Cisco Unified
                                             					 Communications Manager System Guide , "Cisco
                                             					 Unified IP Phones" Customize Cisco Unified Communications Manager Self Care Portal display |
| Call Forward
                                       				All Loop Breakout | Detects and
                                       				prevents Call Forward All loops. When a Call Forward All loop is detected, the
                                       				Call Forward All configuration is ignored and the call rings through. | For more
                                       				information, see Cisco
                                          				  Unified Communications Manager System Guide , "Cisco
                                          				  Unified IP Phones" chapter. |
| Call Forward
                                       				All Loop Prevention | Prevents a
                                       				user from configuring a Call Forward All destination directly on the phone that
                                       				creates a Call Forward All loop or that creates a Call Forward All chain with
                                       				more hops than the existing Forward
                                          				  Maximum Hop Count service parameter allows. | For more
                                       				information, see Cisco
                                          				  Unified Communications Manager System Guide , "Cisco
                                          				  Unified IP Phones" chapter. |
| Call Forward
                                       				Configurable Display | Allows you
                                       				to specify information that appears on a phone when a call is forwarded. This
                                       				information can include the caller name, caller number, redirected number, and
                                       				original dialed number. | For more
                                       				information, see the following: Cisco Unified
                                             					 Communications Manager Administration Guide , "Directory Number Setup" Cisco Unified
                                             					 Communications Manager System Guide , "Cisco
                                             					 Unified IP Phones" |
| Call Forward
                                       				Destination Override | Allows you
                                       				to override Call Forward All (CFA) in cases where the CFA target places a call
                                       				to the CFA initiator. This feature allows the CFA target to reach the CFA
                                       				initiator for important calls. The override works whether the CFA target phone
                                       				number is internal or external. | For more
                                       				information, see the Cisco
                                          				  Unified Communications Manager System Guide , "Directory
                                          				  Numbers" chapter. |
| Call Forward
                                       				Notification | Allows you
                                       				to configure the information that the user sees when receiving a forwarded
                                       				call. | For more
                                       				information, see Call Forward Notification setup. |
| Call History
                                       				for Shared Line | Allows you
                                       				to view shared line activity in the phone Call History. This feature will: Log
                                                					 missed calls for a shared line Log
                                                					 answered calls for a shared line | For more
                                       				information, see Enable Call History for shared line. |
| Call Park | Allows users
                                       				to park (temporarily store) a call and then retrieve the call by using another
                                       				phone in the Cisco Unified Communications Manager system. | For more
                                       				information, see the Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Call Park
                                          				  and Directed Call Park" chapter. |
| Call Pickup | Allows users
                                       				to redirect a call that is ringing on another phone within their pickup group
                                       				to their phone. You can
                                       				configure an audio and visual alert for the primary line on the phone. This
                                       				alert notifies the users that a call is ringing in their pickup group. | For more
                                       				information, see the Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Call
                                          				  Pickup" chapter. |
| Call
                                       				Recording | Allows a
                                       				supervisor to record an active call. The user might hear a recording audible
                                       				alert tone during a call when it is being recorded. When a call
                                       				is secured, the security status of the call is displayed as a lock icon on
                                       				Cisco Unified IP Phones. The connected parties might also hear an audible alert
                                       				tone that indicates the call is secured and is being recorded. Note When an
                                                   				  active call is being monitored or recorded, you can receive or place intercom
                                                   				  calls; however, if you place an intercom call, the active call will be put on
                                                   				  hold, which causes the recording session to terminate and the monitoring
                                                   				  session to suspend. To resume the monitoring session, the party whose call is
                                                   				  being monitored must resume the call. | Note | When an
                                                   				  active call is being monitored or recorded, you can receive or place intercom
                                                   				  calls; however, if you place an intercom call, the active call will be put on
                                                   				  hold, which causes the recording session to terminate and the monitoring
                                                   				  session to suspend. To resume the monitoring session, the party whose call is
                                                   				  being monitored must resume the call. | For more
                                       				information, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Monitoring
                                          				  and Recording" chapter. |
| Note | When an
                                                   				  active call is being monitored or recorded, you can receive or place intercom
                                                   				  calls; however, if you place an intercom call, the active call will be put on
                                                   				  hold, which causes the recording session to terminate and the monitoring
                                                   				  session to suspend. To resume the monitoring session, the party whose call is
                                                   				  being monitored must resume the call. |
| Call Waiting | Indicates
                                       				(and allows users to answer) an incoming call that rings while on another call.
                                       				Incoming call information appears on the phone display. | For more
                                       				information, see: Cisco Unified
                                                						Communications Manager System Guide , "Directory Numbers" Phone
                                             					 Call Waiting setup |
| Caller ID | Caller
                                       				identification such as a phone number, name, or other descriptive text appear
                                       				on the phone display. | For more
                                       				information, see: Cisco Unified
                                             					 Communications Manager Administration Guide , "Cisco
                                             					 Unified IP Phone Setup" Cisco Unified
                                             					 Communications Manager System Guide , "Understanding Route Plans" Features and Services
                                             					 Guide for Cisco Unified Communications Manager , "Call
                                             					 Display Restrictions" Cisco Unified
                                             					 Communications Manager Administration Guide , "Directory Number Setup" |
| Caller ID
                                       				Blocking | Allows a
                                       				user to block their phone number or email address from phones that have caller
                                       				identification enabled. | For more
                                       				information, see: Cisco Unified
                                             					 Communications Manager System Guide , "Understanding Route Plans" Cisco Unified
                                             					 Communications Manager Administration Guide , "Directory Number Setup" |
| Calling
                                       				Party Normalization | Calling
                                       				party normalization presents phone calls to the user with a dialable phone
                                       				number. Any escape codes are added to the number so that the user can easily
                                       				connect to the caller again. The dialable number is saved in the call history
                                       				and can be saved in the Personal Address Book. | For more
                                       				information, see Calling Party Normalization. |
| cBarge | Allows a
                                       				user to join a nonprivate call on a shared phone line. cBarge adds a user to a
                                       				call and converts it into a conference, allowing the user and other parties to
                                       				access conference features | For more
                                       				information, see: Cisco Unified
                                             					 Communications Manager Administration Guide , "Cisco
                                             					 Unified IP Phone Setup" Cisco Unified
                                             					 Communications Manager System Guide , "Cisco
                                             					 Unified IP Phones" Features and Services
                                             					 Guide for Cisco Unified Communications Manager , "Barge
                                             					 and Privacy" |
| Cisco
                                       				Extension Mobility | Allows users
                                       				to temporarily access their Cisco Unified IP Phone configuration such as line
                                       				appearances and services from a shared Cisco Unified IP Phone by
                                       				logging into the Cisco Extension Mobility service on that phone when they log
                                       				into the Cisco Extension Mobility service on that phone. Cisco
                                       				Extension Mobility can be useful if users work from a variety of locations
                                       				within your company or if they share a workspace with coworkers. | For more
                                       				information, see " Extension
                                          				  Mobility" chapter in the Cisco
                                          				  Unified Communications Manager Features and Services Guide . |
| Cisco
                                       				Unified Communications Manager Express (Unified CME) Version Negotiation | The Cisco
                                       				Unified Communication Manager Express uses a special tag in the information
                                       				sent to the phone to identify itself. This tag enables the phone to provide
                                       				services to the user that the switch supports. | For more
                                       				information, see: Cisco
                                             					 Unified Communications Manager Express System Administrator Guide |
| Cisco
                                       				WebDialer | Allows users
                                       				to make calls from web and desktop applications. | For more
                                       				information, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Web
                                          				  Dialer" chapter. |
| Conference | Allows a user to talk
                                          				  simultaneously with multiple parties by calling each participant individually.
                                          				  Conference features include Conference and Meet Me. Allows a noninitiator in
                                          				  a standard (ad hoc) conference to add or remove participants; also allows any
                                          				  conference participant to join together two standard conferences on the same
                                          				  line. | The service
                                       				parameter, Advance Adhoc Conference, (disabled by default in Cisco Unified
                                       				Communications Manager Administration) allows you to enable these features. For
                                       				information on conferences, see Cisco Unified Communications Manager System Guide , "Conference
                                          				  Bridges" chapter. For more
                                       				information, see Cisco
                                          				  Unified Communications Manager System Guide , "Cisco
                                          				  Unified IP Phones" chapter. Note Be sure to
                                                   				  inform your users whether these features are activated. | Note | Be sure to
                                                   				  inform your users whether these features are activated. |
| Note | Be sure to
                                                   				  inform your users whether these features are activated. |
| CTI
                                       				Applications | A computer
                                       				telephony integration (CTI) route point can designate a virtual device to
                                       				receive multiple, simultaneous calls for application-controlled redirection. | For more
                                       				information, see Cisco
                                          				  Unified Communications Manager Administration Guide , "CTI Route
                                          				  Point Setup" chapter. |
| Device
                                       				Invoked Recording | Provides end
                                       				users with the ability to record their telephone calls via a softkey. In addition
                                       				administrators may continue to record telephone calls via the CTI User
                                       				Interface. | For more
                                       				information, see Enable Device Invoked Recording. |
| Directed
                                       				Call Park | Allows a user to transfer an active call to an available directed call park number that the user dials. Note If you
                                                   				  implement Directed Call Park, avoid configuring the Park softkey. This prevents
                                                   				  users from confusing the two Call Park features. | Note | If you
                                                   				  implement Directed Call Park, avoid configuring the Park softkey. This prevents
                                                   				  users from confusing the two Call Park features. | For more
                                       				information, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Call Park
                                          				  and Directed Call Park" chapter. |
| Note | If you
                                                   				  implement Directed Call Park, avoid configuring the Park softkey. This prevents
                                                   				  users from confusing the two Call Park features. |
| Directed
                                       				Call Pickup | Allows a
                                       				user to answer a call that is ringing on a particular directory number. | For more
                                       				information, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Call
                                          				  Pickup" chapter. |
| Direct
                                       				Transfer | Allows users
                                       				to connect two calls to each other without remaining on the line. | For more
                                       				information, see Cisco
                                          				  Unified Communications Manager System Guide , “Cisco Unified IP Phones”
                                       				chapter. |
| Distinctive
                                       				Ring | Users can
                                       				customize how their phone indicates an incoming call and a new voice mail
                                       				message. | For more
                                       				information, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Call
                                          				  Pickup" chapter. |
| Divert | Allows a
                                       				user to transfer a ringing, connected, or held call directly to a
                                       				voice-messaging system. When a call is diverted, the line becomes available to
                                       				make or receive new calls. | For more
                                       				information, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Immediate
                                          				  Divert" chapter. |
| Do Not
                                       				Disturb (DND) | When DND is
                                       				turned on, either no audible rings occur during the ringing-in state of a call,
                                       				or no audible or visual notifications of any type occur. The
                                       				following DND-related parameters are configurable in Cisco Unified
                                       				Communications Manager Administration: Do Not Disturb: This
                                          				  check box allows you to enable DND on a per-phone basis. Use Cisco Unified
                                                						Communications Manager Administration > Device > Phone > Phone
                                                						Configuration . DND Incoming Call Alert:
                                          				  Choose the type of alert to play, if any, on a phone for incoming calls when
                                          				  DND is active. This parameter is located on both the Common Phone Profile page
                                          				  and the Phone configuration page (Phone Configuration window value takes
                                          				  precedence). | For more
                                       				information, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Do Not
                                          				  Disturb" chapter. |
| EnergyWise | Enables an
                                       				IP Phone to sleep (power down) and wake (power up) at predetermined times, to
                                       				promote energy savings. | For more
                                       				information, see EnergyWise on the Cisco Unified IP Phone setup. |
| Enhanced
                                       				Room Coverage | Optional
                                       				microphone extension kits provide enhanced room coverage that can be further
                                       				expanded by linking two units together in Linked Mode. | For more
                                       				information see: Cisco Unified IP
                                                   						Conference Phone 8831 User Guide for Cisco Unified Communication
                                                   						Manager , "Conference Phone Link Mode" chapter. Cisco Unified IP
                                                   						Conference Phone 8831 User Guide for Cisco Unified Communication
                                                   						Manager , "Enhanced Room Coverage" chapter. |
| Fast Dial
                                       				Service | Allows a
                                       				user to enter a Fast Dial code to place a call. Fast Dial codes can be assigned
                                       				to phone numbers or Personal Address Book entries. (See "Services" in this table.) | For more
                                       				information, see Modify phone button template for PAB or Fast Dial. |
| Group Call
                                       				Pickup | Allows a
                                       				user to answer a call that is ringing on a directory number in another group. | For more
                                       				information, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Call
                                          				  Pickup" chapter. |
| Hold
                                       				Reversion | Limits the
                                       				amount of time that a call can be on hold before reverting back to the phone
                                       				that put the call on hold and alerting the user. Reverting
                                       				calls are distinguished from incoming calls by a single ring (or beep,
                                       				depending on the new call indicator setting for the line). This notification
                                       				repeats at intervals if not resumed. A call that
                                       				triggers Hold Reversion also displays an animated icon in the call bubble. You can
                                       				configure call focus priority to favor incoming or reverting calls. | For more
                                       				information about configuring this feature, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Hold
                                          				  Reversion" chapter. |
| Hold Status | Enables
                                       				phones with a shared line to distinguish between the local and remote lines
                                       				that placed a call on hold. | No
                                       				configuration is required. |
| Hold/Resume | Allows the
                                       				user to move a connected call from an active state to a held state. | Requires no
                                          				  configuration, unless you want to use Music On Hold. See "Music On
                                             					 Hold" in this table for information. See "Hold
                                             					 Reversion" in this table. |
| HTTP
                                       				Download | Enhances the
                                       				file download process to the phone to use HTTP by default. If the HTTP download
                                       				fails, the phone reverts to using the TFTP download. | No
                                       				configuration is required. |
| Jitter
                                       				Buffer | The Jitter
                                       				Buffer feature handles jitter from 10 milliseconds (ms) to 1000 ms for both
                                       				audio and video streams. | No
                                       				configuration required. |
| Linked Mode | Enhances the
                                       				audio coverage area by using a daisy cable to connect two conference phone
                                       				Sound Base units. When linked,
                                       				voice, dial tone, ringer and base LED features are synchronized between the two
                                       				devices. | For more
                                       				information see: Cisco Unified IP
                                                   						Conference Phone 8831 User Guide , "Conference Phone Link Mode" |
| Malicious
                                       				Caller Identification (MCID) | Allows users
                                       				to notify the system administrator about suspicious calls that are received. | For more
                                       				information, see: Cisco
                                             					 Unified Communications Manager System Guide , "Cisco
                                             					 Unified IP Phones" Features and Services
                                             					 Guide for Cisco Unified Communications Manager , "Malicious Call Identification" |
| Meet Me
                                       				Conference | Allows a
                                       				user to host a Meet Me conference in which other participants call a
                                       				predetermined number at a scheduled time. | For more
                                       				information, see Cisco
                                          				  Unified Communications Manager Administration Guide , "Meet-Me
                                          				  Number and Pattern Setup" chapter. |
| Message
                                       				Waiting | Defines
                                       				directory numbers for message waiting on and off indicators. A
                                       				directly-connected voice-message system uses the specified directory number to
                                       				set or to clear a message waiting indication for a particular Cisco Unified IP
                                       				Phone. | For more
                                       				information, see the following: Cisco Unified
                                             					 Communications Manager Administration Guide , "Message
                                             					 Waiting Setup" Cisco Unified
                                             					 Communications Manager System Guide , "Voice
                                             					 Mail Connectivity to Cisco Unified Communications Manager" |
| Message
                                       				Waiting Indicator | Displays a
                                       				New Voicemail status message on the phone screen. | For more
                                       				information see: Cisco Unified
                                             					 Communications Manager Administration Guide , "Message
                                             					 Waiting Setup" Cisco Unified
                                             					 Communications Manager System Guide , "Voice
                                             					 Mail Connectivity to Cisco Unified Communications Manager" |
| Missed Call
                                       				Logging | Allows a
                                       				user to specify whether missed calls will be logged in the missed calls
                                       				directory for a given line appearance. | For more
                                       				information, see Cisco
                                          				  Unified Communications Manager Administration Guide , "Directory
                                          				  Number Setup" chapter. |
| Mobile
                                       				Connect | Enables
                                       				users to manage business calls using a single phone number and pick up
                                       				in-progress calls on the desk phone and a remote device such as a mobile phone.
                                       				Users can restrict the group of callers according to phone number and time of
                                       				day. | For more
                                       				information, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Cisco
                                          				  Unified Mobility" chapter. |
| Mobile Voice
                                       				Access | Extends
                                       				Mobile Connect capabilities by allowing users to access an interactive voice
                                       				response (IVR) system to originate a call from a remote device such as a
                                       				cellular phone. | For more
                                       				information, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Cisco
                                          				  Unified Mobility" chapter. |
| Monitoring
                                       				and Recording | Allows a
                                       				supervisor to silently monitor an active call. The supervisor cannot be heard
                                       				by either party on the call. The user might hear a monitoring audible alert
                                       				tone during a call when it is being monitored. When a call
                                       				is secured, the security status of the call is displayed as a lock icon on
                                       				Cisco Unified IP Phones. The connected parties might also hear an audible alert
                                       				tone that indicates the call is secured and is being monitored. Note When an
                                                   				  active call is being monitored or recorded, the use can receive or place
                                                   				  intercom calls; however, if the user place an intercom call, the active call
                                                   				  will be put on hold, which causes the recording session to terminate and the
                                                   				  monitoring session to suspend. To resume the monitoring session, the party
                                                   				  whose call is being monitored must resume the call. | Note | When an
                                                   				  active call is being monitored or recorded, the use can receive or place
                                                   				  intercom calls; however, if the user place an intercom call, the active call
                                                   				  will be put on hold, which causes the recording session to terminate and the
                                                   				  monitoring session to suspend. To resume the monitoring session, the party
                                                   				  whose call is being monitored must resume the call. | For more
                                       				information, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Monitoring
                                          				  and Recording" chapter. |
| Note | When an
                                                   				  active call is being monitored or recorded, the use can receive or place
                                                   				  intercom calls; however, if the user place an intercom call, the active call
                                                   				  will be put on hold, which causes the recording session to terminate and the
                                                   				  monitoring session to suspend. To resume the monitoring session, the party
                                                   				  whose call is being monitored must resume the call. |
| Mute | Mutes the
                                       				conference phone from the Sound Base, DCU or connected external microphones. | Requires no
                                       				configuration. |
| No Alert
                                       				Name | Makes it
                                       				easier for end users to identify transferred calls by displaying the original
                                       				caller’s phone number. The call appears as an Alert Call followed by the
                                       				caller’s telephone number. | Requires no
                                       				configuration. |
| Onhook
                                       				Dialing | Allows a
                                       				user to dial a number without going off hook. | For more
                                       				information, see Cisco
                                          				  Unified IP Conference Phone 8831 User Guide . |
| Other Group
                                       				Pickup | Allows a
                                       				user to answer a call ringing on a phone in another group that is associated
                                       				with the user's group. | For more
                                       				information, see Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Call
                                          				  Pickup" chapter. |
| Phone
                                       				Display Message for Extension Mobility Users | This feature
                                       				enhances the phone interface for the Extension Mobility user by providing
                                       				friendly messages. | No
                                       				configuration required. |
| Plus Dialing | Allows the
                                       				user to dial E.164 numbers prefixed with a plus (+)  sign. To dial the
                                       				+ sign, the user needs to press and hold the star (*) key for at least 1
                                       				second. This applies to dialing the first digit for an on-hook (including edit
                                       				mode) or off-hook call. | No
                                       				configuration required. |
| Privacy | Prevents
                                       				users who share a line from adding themselves to a call and from viewing
                                       				information on their phone display about the call of the other user. | For more
                                       				information, see the following: Cisco Unified
                                             					 Communications Manager Administration Guide , "Cisco
                                             					 Unified IP Phone Setup" Cisco Unified
                                             					 Communications Manager System Guide , "Cisco
                                             					 Unified IP Phones" Features and Services
                                             					 Guide for Cisco Unified Communications Manager , "Barge
                                             					 and Privacy" |
| Quality
                                       				Reporting Tool (QRT) | Allows users
                                       				to submit information about problem phone calls by pressing a button. QRT can
                                       				be configured for either of two user modes, depending upon the amount of user
                                       				interaction desired with QRT. | For more
                                       				information, see: Cisco Unified
                                             					 Communications Manager System Guide , "Cisco
                                             					 Unified IP Phones" Features and Services
                                             					 Guide for Cisco Unified Communications Manager , "Quality
                                             					 Report Tool" |
| Recording Tone | Indicates if a recording tone is enabled for the phone. | For more information, see Recording Tone |
| Redial | Allows users
                                       				to call the most recently dialed phone number by pressing a button or the
                                       				Redial softkey. | Requires no
                                       				configuration. |
| Reroute
                                       				Direct Calls to Remote Destination to Enterprise Number | Reroutes a
                                       				direct call to a user's mobile phone to the enterprise number (desk phone). For
                                       				an incoming call to remote destination (mobile phone), only remote destination
                                       				rings; desk phone does not ring. When the call is answered on their mobile
                                       				phone, the desk phone displays a Remote In Use message. During these calls,
                                       				users can make use of various features of their mobile phone. | For more
                                       				information, see the Features and Services Guide for Cisco Unified Communications
                                          				  Manager , "Cisco
                                          				  Unified Mobility" chapter. |
| Remote Port
                                       				Configuration | Allows the
                                       				administrator to configure the speed and duplex function of the phone Ethernet
                                       				ports remotely by using Cisco Unified Communications Manager Administration.
                                       				This enhances the performance for large deployments with specific port
                                       				settings. Note If the
                                                   				  ports are configured for Remote Port Configuration in Cisco Unified
                                                   				  Communications Manager, the data cannot be changed on the phone. | Note | If the
                                                   				  ports are configured for Remote Port Configuration in Cisco Unified
                                                   				  Communications Manager, the data cannot be changed on the phone. | To configure
                                       				the parameter in the Cisco Unified Communications Manager Administration
                                       				application, choose Device > Phone , select the appropriate IP
                                       				phone, and scroll to the Product Specific Configuration Layout pane (Switch
                                       				Port Remote Configuration or PC Port Remote Configuration). To configure
                                       				the setting on multiple phones simultaneously, configure the remote
                                       				configuration in either Enterprise Phone Configuration ( System > Enterprise Phone
                                             					 Configuration ) or Common Phone Profile Configuration
                                       				( Device > Device
                                             					 Settings > Common Phone Profile . (Switch Port
                                       				Remote Configuration or PC Port Remote Configuration.) |
| Note | If the
                                                   				  ports are configured for Remote Port Configuration in Cisco Unified
                                                   				  Communications Manager, the data cannot be changed on the phone. |
| Ringtone
                                       				Setting | Identifies
                                       				ring type used for a line when a phone has another active call. | For more
                                       				information, see the following: Cisco Unified
                                                					 Communications Manager Administration Guide , "Directory Number Setup" Cisco Unified
                                                   						Communications Manager Administration Guide , "Custom
                                                   						Phone Rings" |
| Secure
                                       				Conference | Allows secure phones to
                                          				  place conference calls using a secured conference bridge. As new participants are
                                          				  added by using Conf, Join, cBarge, Barge softkeys or MeetMe conferencing, the
                                          				  secure call icon displays as long as all participants use secure phones. The Conference List
                                          				  displays the security level of each conference participant. Initiators can
                                          				  remove nonsecure participants from the Conference List. (Non-initiators can add
                                          				  or remove conference participants if the Advanced Adhoc Conference Enabled
                                          				  parameter is set.) | For more
                                       				information about security, see Supported Security
                                          				  Features . For
                                       				additional information, see the following: Cisco Unified
                                             					 Communications Manager System Guide , "Conference Bridges" Cisco Unified
                                             					 Communications Manager Administration Guide , "Conference Bridge Setup" Cisco Unified
                                             					 Communications Manager Security Guide |
| Services | Allows you
                                       				to use the Cisco Unified IP Phone Services Configuration menu in Cisco
                                       				Unified Communications Manager Administration to define and maintain the list
                                       				of phone services to which users can subscribe. | For more
                                       				information refer to: Cisco Unified
                                             					 Communications Manager Administration Guide , "Cisco
                                             					 Unified IP Phone Setup" Cisco Unified
                                             					 Communications Manager System Guide , "Cisco
                                             					 Unified IP Phone Services" |
| Shared Line | Allows a
                                       				user to have multiple phones that share the same phone number or allows a user
                                       				to share a phone number with a coworker. | For more
                                       				information, see Cisco
                                          				  Unified Communications Manager System Guide , "Directory
                                          				  Numbers" chapter. |
| Special Sequence for Factory Reset | Allows the phone manufacturer to reset the factory parameters. | No configuration required. |
| Time-of-Day
                                       				Routing | Restricts
                                       				access to specified telephony features by time period. | For more
                                       				information, see: Cisco Unified
                                             					 Communications Manager Administration Guide , "Time
                                             					 Period Setup" Cisco Unified
                                             					 Communications Manager System Guide , "Time-of-Day Routing" |
| Time Zone
                                       				Update | Updates the
                                       				Cisco Unified IP Phone with time zone changes. | For more
                                       				information, see Cisco
                                          				  Unified Communications Manager Administration Guide , "Date and
                                          				  Time Group Setup" chapter. |
| TLS Enhancements | Added in Firmware Release 10.3(1)SR3. Improved security with the parameter Disable TLS1.0 and TLS1.1 for web access in Cisco Unified Communications Manager. When set to enabled, the phones support only TLS1.2 mode. When set to disabled,
                                       TLS1.0, TLS1.1 and TLS1.2 are supported. This field applies to any phone or group of phones that function as a HTTPs server. |  |
| Transfer | Allows users
                                       				to redirect connected calls from their phones to another number. | Some
                                       				JTAPI/TAPI applications are not compatible with the Join and Direct Transfer
                                       				feature implementation on the conference phone and you may need to configure
                                       				the Join and Direct Transfer Policy to disable join and direct transfer on the
                                       				same line or possibly across lines. |
| Transfer -
                                       				Direct Transfer | Transfer:
                                       				The first invocation of Transfer will always initiate a new call by using the
                                       				same directory number, after putting the active call on hold. Direct
                                       				Transfer: This transfer joins two established calls (call is in hold or in
                                       				connected state) into one call and drops the feature initiator from the call.
                                       				Direct Transfer does not initiate a consultation call and does not put the
                                       				active call on hold. | Some
                                       				JTAPI/TAPI applications are not compatible with the Join and Direct Transfer
                                       				feature implementation on the conference phone and you may need to configure
                                       				the Join and Direct Transfer Policy to disable join and direct transfer on the
                                       				same line or possibly across lines. For more information, see the <xref Join
                                       				and Direct Transfer Policy>. |
| UCR 2008 | The
                                       				conference phone supports Unified Capabilities Requirements (UCR) 2008 by
                                       				providing support for 80-bit SRTCP Tagging. As an
                                       				administrator, you must set up specific parameters in Cisco Unified
                                       				Communications Manager Administration. | See UCR 2008
                                       				setup. |
| Voice
                                       				Message System | Enables
                                       				callers to leave messages if calls are unanswered. | For more
                                       				information, see the following: Cisco Unified
                                             					 Communications Manager Administration Guide , "Cisco
                                             					 Voice-Mail Port Setup" Cisco Unified
                                             					 Communications Manager System Guide , "Voice
                                             					 Mail Connectivity to Cisco Unified Communications Manager" |
| Wideband
                                       				Ringtone | The Wideband
                                       				Ringtone feature supports 10 ringtones: 4 embedded in the phone firmware and 6
                                       				downloaded from the Cisco Unified Communications Manager. | For more
                                       				information, see the following: Cisco Unified
                                             					 Communications Manager Administration Guide , "Directory Number Setup" Features and Services
                                                						Guide for Cisco Unified Communications Manager , "Custom
                                                						Phone Rings" |
| Wireless
                                       				Microphone Frequency Lock | Provides a
                                       				secure DECT frequency for wireless microphones by locking down the Wireless
                                       				Region setting. | No
                                       				configuration required for Firmware release 10.3(1) and later. Earlier releases
                                       				must upgrade to the current release to have the region setting locked. Note Once you
                                                   				  have configured the Wireless Region setting, it cannot be updated. Further
                                                   				  configuration of this setting requires an RMA. | Note | Once you
                                                   				  have configured the Wireless Region setting, it cannot be updated. Further
                                                   				  configuration of this setting requires an RMA. |
| Note | Once you
                                                   				  have configured the Wireless Region setting, it cannot be updated. Further
                                                   				  configuration of this setting requires an RMA. |

| Note | The
                                                   				  stutter tone is line-specific. You hear it only when using the line with the
                                                   				  waiting messages. |
|---|---|

| Note | When an
                                                   				  active call is being monitored or recorded, you can receive or place intercom
                                                   				  calls; however, if you place an intercom call, the active call will be put on
                                                   				  hold, which causes the recording session to terminate and the monitoring
                                                   				  session to suspend. To resume the monitoring session, the party whose call is
                                                   				  being monitored must resume the call. |
|---|---|

| Note | Be sure to
                                                   				  inform your users whether these features are activated. |
|---|---|

| Note | If you
                                                   				  implement Directed Call Park, avoid configuring the Park softkey. This prevents
                                                   				  users from confusing the two Call Park features. |
|---|---|

| Note | When an
                                                   				  active call is being monitored or recorded, the use can receive or place
                                                   				  intercom calls; however, if the user place an intercom call, the active call
                                                   				  will be put on hold, which causes the recording session to terminate and the
                                                   				  monitoring session to suspend. To resume the monitoring session, the party
                                                   				  whose call is being monitored must resume the call. |
|---|---|

| Note | If the
                                                   				  ports are configured for Remote Port Configuration in Cisco Unified
                                                   				  Communications Manager, the data cannot be changed on the phone. |
|---|---|

| Note | Once you
                                                   				  have configured the Wireless Region setting, it cannot be updated. Further
                                                   				  configuration of this setting requires an RMA. |
|---|---|

| Step 1 | Log on to Cisco Unified Communications Manager Administration. |
|---|---|
| Step 2 | Select Device > Device Settings > Phone Button Template . |
| Step 3 | Select Add New . |
| Step 4 | To assign a button template to a conference phone, choose Device > Phone to select the conference phone. |
| Step 5 | In the Phone Configuration window, select a button template from the Phone Button Template drop-down list. |

| Note | Cisco Unified
                                       		  Communications Manager allows you to configure any softkey in a softkey
                                       		  template, but unsupported softkeys do not display on the phone. |
|---|---|

| Feature | Configurable
                                       				Softkeys in the Softkey Template Configuration | Supported as a
                                       				Softkey | Notes |
|---|---|---|---|
| Answer | Answer
                                       				(Answer) | Yes | — |
| Barge | Barge (Barge) | Yes | Configure as a
                                       				softkey. |
| Call Back | Call Back
                                       				(CallBack) | Yes | — |
| Call Forward
                                       				All | Forward All
                                       				(cfwdAll) | Yes | Phone displays Fwd
                                          				  ALL or Fwd
                                          				  Off . |
| Call Park | Call Park
                                       				(Park) | Yes | — |
| Call Pickup | Pick Up
                                       				(Pickup) | Yes | Configure as
                                       				a softkey. |
| cBarge | Conference
                                       				Barge (cBarge) | Yes | Configure as
                                       				a softkey. |
| Conference | Conference
                                       				(Conf) | Yes | Phone
                                       				displays Conference when a call is connected. |
| Conference
                                       				List | Conference
                                       				List (ConfList) | Yes | Phone
                                       				displays ConfList when in a conference. |
| iDivert | Immediate
                                       				Divert (iDivert) | Yes | Phone
                                       				displays Divert . |
| Do Not
                                       				Disturb | Toggle Do
                                       				Not Disturb (DND) | Yes | Configure as
                                       				a softkey. |
| End Call | End Call
                                       				(EndCall) | Yes | Phone
                                       				displays Cancel if the call is not answered. |
| Group Pickup | Group Pick
                                       				Up (GPickUp) | Yes | Configure as
                                       				a softkey. |
| Hold | Hold (Hold) | Yes |  |
| Join | Join (Join) | No | — |
| Malicious
                                       				Call Identification | Toggle
                                       				Malicious Call Identification (MCID) | Yes | Configure
                                       				Malicious Call Identification as a softkey. |
| Meet Me | Meet Me
                                       				(MeetMe) | Yes | Configure as
                                       				a softkey. |
| Mobile
                                       				Connect | Mobility
                                       				(Mobility) | Yes | Configure
                                       				Mobile Connect as a softkey. |
| New Call | New Call
                                       				(NewCall) | Yes | Phone
                                       				displays New Call . |
| Other Pickup | Other Pickup
                                       				(oPickup) | Yes | Configure as
                                       				a softkey. |
| Quality
                                       				Reporting Tool | Quality
                                       				Reporting Tool (QRT) | Yes | Configure
                                       				Quality Reporting Tool as a softkey. |
| Redial | Redial
                                       				(Redial) | Yes | Phone
                                       				displays Redial when Off Hook. |
| Remove Last
                                       				Conference Participant | Remove Last
                                       				Conference Participant (Remove) | Yes | Phone
                                       				displays Remove when a participant is selected. |
| Resume | Resume
                                       				(Resume) | Yes | — |
| Transfer | Transfer | Yes | Phone
                                       				displays Transfer when a call is connected. |

| Step 1 | Log on to
                                          			 Cisco Unified Communications Manager Administration. |
|---|---|
| Step 2 | Select Device >
                                             				Device Settings > Softkey Template . |
| Step 3 | To assign a
                                          			 softkey template to a conference station, choose Device >
                                             				Phone to select the conference station. |
| Step 4 | In the Phone
                                          			 Configuration window, select a softkey template from the Softkey Template
                                          			 drop-down list. |

| Note | Other related
                                          			 parameters — the recording tone frequency (in hz), the duration of the beep
                                          			 tone, and the beep tone interval (how often the beep tone plays) — are defined
                                          			 on a per-Network Locale basis in the xml file that defines tones. This xml file
                                          			 is named tones.xml or g3-tones.xml. |
|---|---|

| Parameter | Note |
|---|---|
| Recording
                                          					 Tone Local Volume | Indicates
                                          					 the volume for the recording tone that the local party receives, if the local
                                          					 party phone has the Recording Tone option enabled. This
                                          					 setting applies for each listening device, including the handset, speakerphone,
                                          					 and headset. Range: 0
                                          					 percent (no tone) to 100 percent (same level as current volume setting on the
                                          					 phone). |
| Recording
                                          					 Tone Remote Volume | Indicates
                                          					 the volume for the recording tone that the remote party receives. The remote
                                          					 party is the party who is on a call with the party whose phone has the
                                          					 Recording Tone option enabled. Range: 0
                                          					 percent to 100 percent. (0 percent is -66 dBM and 100 percent is -3 dBM). Default:
                                          					 50 percent. |
| Recording
                                          					 Tone Duration | Indicates
                                          					 the length of time in milliseconds that the tone plays. If the
                                          					 value is less than one third of the interval, this value overrides the default
                                          					 provided that the Network Locale provides. Range: 0
                                          					 to 3000 Note For some
                                                      						Network Locales that use a complex cadence, this setting applies only to the
                                                      						first recording tone. | Note | For some
                                                      						Network Locales that use a complex cadence, this setting applies only to the
                                                      						first recording tone. |
| Note | For some
                                                      						Network Locales that use a complex cadence, this setting applies only to the
                                                      						first recording tone. |

| Note | For some
                                                      						Network Locales that use a complex cadence, this setting applies only to the
                                                      						first recording tone. |
|---|---|

| Note | You may want to notify your users if you enable this option. The
                                          		  default setting is Disabled. |
|---|---|

| Step 1 | In Cisco Unified
                                          			 Communications Manager Administration, go to Device > Phone . |
|---|---|
| Step 2 | Select Enable from the pulldown menu In the Recording
                                          			 Tone section. |
| Step 3 | Enter a value between 0 and 100 per cent in the Recording Tone
                                          			 Local Volume field. |
| Step 4 | Enter a value between 0 and 100 per cent in the Recording Tone
                                          			 Remote Volume field. |
| Step 5 | Click Save . |

| Step 1 | Set the  Built In Bridge to On . |
|---|---|
| Step 2 | Set Privacy to Off . |
| Step 3 | Set Recording Option to Selective Call Recording Enabled . |
| Step 4 | Select the appropriate Recording Profile. |

| Note | For the
                                             				purposes of this procedure, all references to a phone, device, or IP Phone
                                             				apply to the conference phone. |
|---|---|

| Step 1 | Go to Cisco
                                       			 Unified CM Administration and choose Device > Phone . |
|---|---|
| Step 2 | Find your
                                       			 conference phone in the list of phones associated with the Cisco Unified CM. |
| Step 3 | Click on the
                                       			 Device Name of the phone. The Phone
                                          				Configuration window appears. |
| Step 4 | Go to Product
                                       			 Specific Configuration Layout area and from the Logging Display drop-down list
                                       			 box, choose the applicable profile. The Disabled
                                          				option is selected by default. Parameters
                                          				that you set in the Product Specific Configuration area may also appear in the
                                          				Device Configuration window for various devices and in the Enterprise Phone
                                          				Configuration window. If you set
                                          				these same parameters in these other windows as well, the setting that takes
                                          				precedence is determined in the following order: Device
                                                					 Configuration window settings Common
                                                					 Phone Profile window settings Enterprise
                                                					 Phone Configuration window settings |

| Note | To configure Cisco
                                       		  Extension Mobility services for users, see "Cisco Unified
                                          			 Mobility" , Cisco Unified
                                          			 Communications Manager Features and Services Guide |
|---|---|

| Note | After the Enable Synchronization from LDAP Server is enabled, you will not be able to add additional users from Cisco Unified
                                             Communications Manager Administration. |
|---|---|

| Field | Description | Default
                                          					 Checkbox State |
|---|---|---|
| Caller
                                          					 Name | When this
                                          					 check box is checked, the caller name displays in the notification window. | Checked |
| Caller
                                          					 Number | When this
                                          					 check box is checked, the caller number displays in the notification window. | Not
                                          					 checked |
| Redirected
                                          					 Number | When this
                                          					 check box is checked, the information about the caller who last forwarded the
                                          					 call displays in the notification window. Example:
                                          					 If Caller A calls B, but B has forwarded all calls to C and C has forwarded all
                                          					 calls to D, the notification box that D sees contains the phone information for
                                          					 caller C. | Not
                                          					 checked |
| Dialed
                                          					 Number | When this
                                          					 check box is checked, the information about the original recipient of the call
                                          					 displays in the notification window. Example:
                                          					 If Caller A calls B, but B has forwarded all calls to C and C has forwarded all
                                          					 calls to D, then the notification box that D sees contains the phone
                                          					 information for caller B. | Checked |

| Field | Description | Default Value |
|---|---|---|
| Incoming
                                          					 Call Toast Timer | Gives the
                                          					 time, in seconds, that the toast displays. The time includes the fade-in and
                                          					 fade-out times for the window. The
                                          					 possible values are 3, 4, 5, 6, 7, 8, 9, 10, 15, 30, and 60. | 5
                                          					 seconds. |

| Component | Connect to Primary | Connect to Secondary |
|---|---|---|
| Display Control Unit (DCU) | Yes | No |
| Network cable | Yes | No |
| Wall power | Yes | No |
| Optional Wired Microphone | Yes | Yes |
| Optional Wireless Microphone | Yes | No |

| Note | If a DCU is
                                       		connected to the secondary device, it will display a prompt indicating that it
                                       		is a dummy DCU, but will otherwise not function. |
|---|---|

| Caution | When using a Sound
                                       		Base in Linked Mode, the primary base unit must be connected using the
                                       		CP-PWR-CUBE-3 external power supply. |
|---|---|

| Step 1 | Connect the DCU to the conference phone to be used as the primary unit. |
|---|---|
| Step 2 | Connect the network cable to the conference phone to be used as the primary unit. |
| Step 3 | Connect the power cable to the primary device and plug into a wall plug. The secondary Sound Base does not need to be plugged into external power, but in Linked Mode the primary unit must be connected
                                             to external power. |
| Step 4 | Use the provided daisy cable to connect the primary unit to the secondary sound base. Voice, dial tone, ringer and base LEDs synchronize between the two units. |