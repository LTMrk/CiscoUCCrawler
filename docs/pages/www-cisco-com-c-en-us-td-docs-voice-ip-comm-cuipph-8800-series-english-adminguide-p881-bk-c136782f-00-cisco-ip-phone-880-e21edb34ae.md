---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8800-series-english-adminguide-p881-bk-c136782f-00-cisco-ip-phone-880-e21edb34ae
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8800-series/english/adminguide/P881_BK_C136782F_00_cisco-ip-phone-8800_series/P881_BK_C136782F_00_cisco-ip-phone-8811-8841_chapter_01011.html
retrieved_at: 2026-08-21T09:49:19.763814+00:00
---

Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

# Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

Updated: November 6, 2025

Chapter: Phone Features and Setup

## Chapter: Phone Features and Setup

# Phone Features and Setup

## Phone Features and
                        	 Setup Overview

After you install
                           		Cisco IP Phones in your network, configure their network settings, and add them
                           		to Cisco Unified Communications Manager, you must use the Cisco Unified
                           		Communications Manager Administration application to configure telephony
                           		features, optionally modify phone templates, set up services, and assign users.

You can modify
                           		additional settings for the Cisco IP Phone from Cisco Unified Communications
                           		Manager Administration. Use this web-based application to set up phone
                           		registration criteria and calling search spaces, to configure corporate
                           		directories and services, and to modify phone button templates, among other
                           		tasks.

When adding features to the phone line keys, you are limited by the number of line keys available. You cannot add more features
                           than the number of line keys on your phone.

## Cisco IP Phone User Support

If you are a system administrator, you are likely the primary source of information for Cisco IP Phone users in your network
                              or company. It is important to provide current and thorough information to end users.

To successfully use some of the features on the Cisco IP Phone (including Services and voice message system options), users
                              must receive information from you or from your network team or must be able to contact you for assistance. Make sure to provide
                              users with the names of people to contact for assistance and with instructions for contacting those people.

We recommend that you create a web page on your internal support site that provides end users with important information about
                              their Cisco IP Phones.

Consider including the following types of information on this site:

User guides for all Cisco IP Phone models that you support

Information on how to access the Cisco Unified Communications Self Care Portal

List of features supported

User guide or quick reference for your voicemail system

## Telephone
                        	 Features

After you add
                              		  Cisco IP Phones to Cisco Unified Communications Manager, you can add
                              		  functionality to the phones. The following table includes a list of supported
                              		  telephony features, many of which you can configure by using Cisco Unified
                              		  Communications Manager Administration.

For information about using most of these features on the phone, see Cisco IP Phone 8800 Series User Guide . See Feature Buttons and Softkeys for a list of features that can be configured as programmable buttons and dedicated softkeys and feature buttons.

Cisco Unified
                                          			 Communications Manager Administration also provides several service parameters
                                          			 that you can use to configure various telephony functions. For more information
                                          			 on accessing and configuring service parameters, see the 
                                          			 documentation for your particular Cisco Unified Communications Manager release.

For more information on the functions of a service, select the name of the parameter or the question mark (?) help button in the Service Parameter Configuration window.

For more information, see the documentation for your particular Cisco Unified Communications Manager release.

Feature

Description and more information

Abbreviated Dialing

Allows
                                          						users to speed dial a phone number by entering an assigned index code (1-199)
                                          						on the phone keypad.

You
                                                      						  can use Abbreviated Dialing while on-hook or off-hook.

Users
                                          						assign index codes from the Self Care Portal.

Actionable Incoming Call Alert

Provides different options to control the incoming call alerts. You can disable or enable the call alert. You can also activate
                                          or deactivate the caller ID display.

See Actionable Incoming Call Alert, Product Specific Configuration .

AES 256 Encryption Support for Phones

Enhances security by supporting TLS 1.2 and new ciphers. For more information, see Supported Security Features .

Agent
                                          						Greeting

Allows
                                          						an agent to create and update a prerecorded greeting that plays at the
                                          						beginning of a customer call, before the agent begins the conversation with the
                                          						caller. The agent can prerecord a single greeting or multiple ones as needed.

See Enable Agent Greeting .

Always On Mode

Always keeps the DECT connection between the headset and base even when the user is not on a call or playing music.

This feature is supported on Cisco Headset 500 Series.

See Headset template management in Call Manager for more information.

Any Call
                                          						Pickup

Allows
                                          						users to pick up a call on any line in their call pickup group, regardless of
                                          						how the call was routed to the phone.

See call pickup in the documentation for your particular Cisco Unified Communications Manager release.

Application Dial Rules

Convert numbers for shared mobile contacts to network dialable numbers.

See Application Dial Rules .

Assisted
                                          						Directed Call Park

Enables
                                          						users to park a call by pressing only one button using the Direct Park feature.
                                          						Administrators must configure a Busy Lamp Field (BLF) Assisted Directed Call
                                          						Park button. When users press an idle BLF Assisted Directed Call Park button
                                          						for an active call, the active call is parked at the Direct Park slot
                                          						associated with the Assisted Directed Call Park button.

See assisted directed call park in  the documentation for your particular Cisco Unified Communications Manager release.

Audible
                                          						Message Waiting Indicator (AMWI)

A
                                          						stutter tone from the handset, headset, or speakerphone indicates that a user
                                          						has one or more new voice messages on a line.

The
                                                      						  stutter tone is line-specific. You hear it only when using the line with the
                                                      						  waiting messages.

Auto
                                          						Answer

Connects
                                          						incoming calls automatically after a ring or two.

Auto
                                          						Answer works with either the speakerphone or the headset.

See directory number information in the documentation for your particular Cisco Unified Communications Manager release.

Automatic Port Synchronization

Synchronizes ports to the lowest speed between ports of a phone
                                          						to eliminate packet loss.

See Automatic Port Synchronization, Product Specific Configuration .

Auto
                                          						Pickup

Allows a
                                          						user to use one-touch pickup functionality for call pickup features.

See call pickup in the documentation for your particular Cisco Unified Communications Manager release.

Barge

Enables a user to barge into a call by establishing the three-way conference call using the built-in conference bridge of
                                          the target phone.

See "cBarge" in this table.

Block
                                          						External to External Transfer

Prevents users from transferring an external call to another
                                          						external number.

See
                                          						external call transfer information in the documentation for your particular Cisco Unified Communications Manager release.

Bluetooth Multiconnection

Enables the user to pair multiple devices to the phone. The user can then connect a mobile device using Bluetooth and a Bluetooth
                                          headset at the same time.

Cisco IP Phone 8851NR does not support Bluetooth.

Bluetooth Mute Sync for Cisco Headset 700 Series and 900 Series

The mute status between the IP Phone and Cisco headset is synchronized automatically during a call.

Supported on the Cisco IP Phones 8845, 8851, 8861, and 8865, connected with Cisco Headset 720/730/950/980 Series.

Busy
                                          						Lamp Field (BLF)

Allows
                                          						a user to monitor the call state of a directory number associated with a
                                          						speed-dial button on the phone.

See presence information in the documentation for your particular Cisco Unified Communications Manager release.

Busy
                                          						Lamp Field (BLF) Pickup

Provides enhancements to BLF speed dial. Allows you to configure
                                          						a Directory Number (DN) that a user can monitor for incoming calls. When the DN
                                          						receives an incoming call, the system alerts the monitoring user, who can then
                                          						pick up the call.

See call pickup information in the documentation for your particular Cisco Unified Communications Manager release.

Call
                                          						Back

Provides users with an audio and visual alert on the phone when
                                          						a busy or unavailable party becomes available.

See call back information in the documentation for your particular Cisco Unified Communications Manager release.

Call
                                          						Display Restrictions

Determines the information that will display for calling or
                                          						connected lines, depending on the parties who are involved in the call.

See routing plans and call display restriction information in the documentation for your particular Cisco Unified Communications
                                          Manager release.

Call
                                          						Forward

Allows
                                          						users to redirect incoming calls to another number. Call Forward options
                                          						include Call Forward All, Call Forward Busy, Call Forward No Answer, and Call
                                          						Forward No Coverage.

See directory number information in the documentation for your particular Cisco Unified Communications Manager release and Customize the Self Care Portal Display .

Call
                                          						Forward All Loop Breakout

Detects and prevents Call Forward All loops. When a Call Forward
                                          						All loop is detected, the Call Forward All configuration is ignored and the
                                          						call rings through.

Call
                                          						Forward All Loop Prevention

Detects and prevents Call Forward All loops. When a Call Forward
                                          						All loop is detected, the Call Forward All configuration is ignored and the
                                          						call rings through.

Call
                                          						Forward Configurable Display

Prevents a user from configuring a Call Forward All destination
                                          						directly on the phone that creates a Call Forward All loop or that creates a
                                          						Call Forward All chain with more hops than the existing Forward Maximum Hop
                                          						Count service parameter allows.

See directory number information in  the documentation for your particular Cisco Unified Communications Manager release.

Call
                                          						Forward Destination Override

Allows
                                          						you to override Call Forward All (CFA) in cases where the CFA target places a
                                          						call to the CFA initiator. This feature allows the CFA target to reach the CFA
                                          						initiator for important calls. The override works whether the CFA target phone
                                          						number is internal or external.

See
                                          						directory number information in  the documentation for your particular Cisco Unified Communications Manager release.

Call
                                          						Forward Notification

Allows
                                          						you to configure the information that the user sees when receiving a forwarded
                                          						call.

See Set Up Call Forward Notification .

Call
                                          						History for Shared Line

Allows you to view shared line activity in the phone Call History. This feature will:

Log missed calls for a shared line

Log all answered and placed calls for a shared line

Call
                                          						Park

Allows
                                          						users to park (temporarily store) a call and then retrieve the call by using
                                          						another phone in the Cisco Unified Communications Manager system.

You can configure the field Dedicate one line for call park in the Product Specific Configuration Layout pane to park the call to the original line or a different line.

When the field is
                                          									enabled, the parked call remains on the user's line and they can
                                          									use the Resume softkey to pick up the
                                          									call. The user sees the extension number for the parked call on
                                          									the phone display.

When the field is
                                          									disabled, the parked call transfers to the call park line. The
                                          									user's line returns to the idle state and they see the call park
                                          									extension in a pop-up window. The user dials the extension to
                                          									pick up the call.

See
                                          						call park information in the documentation for your particular Cisco Unified Communications Manager release.

Call
                                          						Pickup

Allows
                                          						users to redirect a call that is ringing on another phone within their pickup
                                          						group to their phone.

You
                                          						can configure an audio and visual alert for the primary line on the phone. This
                                          						alert notifies the users that a call is ringing in their pickup group.

See
                                          						call pickup information in   the documentation for your particular Cisco Unified Communications Manager release.

Call
                                          						Recording

Allows
                                          						a supervisor to record an active call. The user might hear a recording audible
                                          						alert tone during a call when it is being recorded.

When a
                                          						call is secured, the security status of the call is displayed as a lock icon on
                                          						Cisco IP Phones. The connected parties might also hear an audible alert tone
                                          						that indicates the call is secured and is being recorded.

When
                                                      						  an active call is being monitored or recorded, the user can receive or place
                                                      						  intercom calls; however, if the user places an intercom call, the active call
                                                      						  is put on hold, which causes the recording session to terminate and the
                                                      						  monitoring session to suspend. To resume the monitoring session, the party
                                                      						  whose call is being monitored must resume the call.

See
                                          						monitoring and recording information in the documentation for your particular Cisco Unified Communications Manager release.

Call
                                          						Waiting

Indicates (and allows users to answer) an incoming call that
                                          						rings while on another call. Incoming call information appears on the phone
                                          						display.

See
                                          						directory number information in the documentation for your particular Cisco Unified Communications Manager release.

Call
                                          						Waiting Ring

Provides Call Waiting users with the option of an audible ring
                                          						instead of the standard beep.

Options are Ring and Ring Once.

See
                                          						directory number information in the documentation for your particular Cisco Unified Communications Manager release.

Caller
                                          						ID

Caller
                                          						identification such as a phone number, name, or other descriptive text appear
                                          						on the phone display.

See routing plan, call display restrictions, and directory number information in the documentation for your particular Cisco
                                          Unified Communications Manager release.

Caller
                                          						ID Blocking

Allows
                                          						a user to block their phone number or email address from phones that have
                                          						caller identification enabled.

See routing plan and directory number information in the documentation for your particular Cisco Unified Communications Manager
                                          release.

Calling Party Normalization

Calling party normalization presents phone calls to the user
                                          						with a dialable phone number. Any escape codes are added to the number so that
                                          						the user can easily connect to the caller again. The dialable number is saved
                                          						in the call history and can be saved in the Personal Address Book.

CAST
                                          						for SIP

Establishes communication between the Cisco Unified Video
                                          						Advantage (CUVA) and the Cisco IP phones to support video on the PC even if the
                                          						IP phone does not have video capability.

cBarge

Allows
                                          						a user to join a nonprivate call on a shared phone line. cBarge adds a user to
                                          						a call and converts it into a conference, allowing the user and other parties
                                          						to access conference features. The conference call is created using the Cisco
                                          						Unified Communications Manager conference bridge functionality.

You must enable both the softkey and the conference bridge functionality for cBarge to function correctly.

In Firmware Release 10.2(2) and later, the cBarge functionality is accessed using the Barge softkey.

For more information, refer to the "Barge" chapter, Feature Configuration Guide for Cisco Unified Communications Manager .

Charge
                                          						a Mobile Device

Allows
                                          						a user to charge a mobile device by connecting it to the USB port of the Cisco
                                          						IP Phone.

See Cisco IP Phone 8800 Series User Guide .

Cisco
                                          						Extension Mobility

Allows
                                          						users access to their Cisco IP Phone configuration such as line
                                          						appearances, services, and speed dials from a shared Cisco IP Phone.

Cisco
                                          						Extension Mobility is useful if people work from a variety of locations
                                          						within your company or if they share a workspace with coworkers.

Cisco
                                          						Extension Mobility Cross Cluster (EMCC)

Enables a user configured in one cluster to log into a Cisco IP
                                          						Phone in another cluster. Users from a home cluster log into a Cisco IP Phone
                                          						at a visiting cluster.

Configure Cisco Extension Mobility on Cisco IP Phones before you
                                                      						  configure EMCC.

Cisco IP Manager Assistant (IPMA)

Provides call routing and other call management features to help
                                          managers and assistants handle phone calls more effectively.

See Set up Cisco IP Manager Assistant .

Cisco IP Phone 8800 Key Expansion Module

Cisco IP Phone 8851/8861 Key Expansion Module

Cisco IP Phone 8865 Key Expansion Module

Provides additional keys by adding an expansion module to the phone.

For additional information, see Cisco IP Phone 7800 and 8800 Series Accessories Guide for Cisco Unified Communications Manager .

Cisco IP Phone 8811 Support

Provides support for the Cisco IP Phone 8811 .

Cisco IP Phone 8851NR Support

Provides support for the Cisco IP Phone 8851NR

Cisco
                                          						Unified Communications Manager Express (Unified CME) Version Negotiation

The
                                          						Cisco Unified Communication Manager Express uses a special tag in the
                                          						information sent to the phone to identify itself. This tag enables the phone to
                                          						provide services to the user that the switch supports.

See:

Cisco Unified
                                                   								Communications Manager Express System Administrator Guide

Cisco Unified Communications Manager Express Interaction

Cisco
                                          						Unified Video Advantage (CUVA)

Allows
                                          						users to make video calls by using a Cisco IP Phone, a personal computer, and a
                                          						video camera.

Configure the Video Capabilities parameter in the Product
                                                      						  Specific Configuration Layout section in Phone Configuration.

See
                                          						the Cisco Unified Video Advantage documentation.

Cisco
                                          						WebDialer

Allows
                                          						users to make calls from web and desktop applications.

Classic Ringtone

Supports ringtones that are embedded in the phone firmware or
                                          						downloaded from the Cisco Unified Communications Manager. The feature makes the
                                          						available ringtones common with other Cisco IP Phones.

See Custom Phone Rings .

Conference

Allows
                                          						a user to talk simultaneously with multiple parties by calling each participant
                                          						individually. Conference features include Conference and Meet Me.

Allows
                                          						a noninitiator in a standard (adhoc) conference to add or remove participants;
                                          						also allows any conference participant to join together two standard
                                          						conferences on the same line.

The
                                          						Advance Adhoc Conference service parameter, disabled by default in Cisco
                                          						Unified Communications Manager Administration, allows you to enable these
                                          						features.

Be
                                                      						  sure to inform your users if these features are activated.

Configurable Energy Efficient Ethernet (EEE) for PC and Switch Port

Provides a method to control EEE functions on personal computer port and switch port by enabling or disabling EEE. The feature
                                          controls both type of ports individually. The default value is Enabled.

See Set Up Energy Efficient Ethernet for Switch and PC Port .

Configurable Font Size

Allows
                                          						users to increase or decrease the maximum number of characters the IP phone
                                          						displays for Call History and Call Screen by changing the font size.

A
                                          						smaller font increases the maximum number of displayed characters, and a larger
                                          						font decreases the maximum number of displayed characters.

CTI
                                          						Applications

A
                                          						computer telephony integration (CTI) route point can designate a virtual device
                                          						to receive multiple, simultaneous calls for application-controlled redirection.

Decline All

Allows
                                          						a user to transfer a ringing, connected, or held call directly to a
                                          						voice-messaging system. When a call is declined, the line becomes available to
                                          						make or receive new calls.

See immediate divert information in the documentation for your particular Cisco Unified Communications Manager release.

Device
                                          						Invoked Recording

Provides end users with the ability to record their telephone
                                          						calls via a softkey.

In
                                          						addition administrators may continue to record telephone calls via the CTI User
                                          						Interface.

See monitoring and recording information in the documentation for your particular Cisco Unified Communications Manager release.

Directed Call Park

Allows
                                          						a user to transfer an active call to an available directed call park number
                                          						that the user dials or speed dials. A Call Park BLF button indicates whether a
                                          						directed call park number is occupied and provides speed-dial access to the
                                          						directed call park number.

If
                                                      						  you implement Directed Call Park, avoid configuring the Park softkey. This
                                                      						  prevents users from confusing the two Call Park features.

See call park information in the documentation for your particular Cisco Unified Communications Manager release.

Display Battery Strength and Signal Strength Icons

Displays the battery and signal strength of the mobile phone on the IP Phone when the mobile phone is connected to the IP
                                          Phone using Bluetooth.

Cisco IP Phone 8851NR does not support Bluetooth.

Distinctive Ring

Users
                                          						can customize how their phone indicates an incoming call and a new voice mail
                                          						message.

See
                                          						call pickup information in the documentation for your particular Cisco Unified Communications Manager release.

Do Not
                                          						Disturb (DND)

When
                                          						DND is turned on, either no audible rings occur during the ringing-in state of
                                          						a call, or no audible or visual notifications of any type occur.

When enabled, the phone header turns red and Do not disturb is displayed on the phone.

If multilevel precedence and preemption (MLPP) is configured and the user receives a precedence call, the phone will ring
                                          with a special ringtone.

See Set Up Do Not Disturb .

Dock Event

Allows a user to set up the call behavior when the headset is lift from the base or is put down on the base.

This feature is supported on Cisco Headset 500 Series.

See Headset template management in Call Manager for more information.

Enable/Disable JAL/TAL

Allows the administrator to control the Join Across Lines (JAL) and Direct Transfer Across Lines (TAL) features.

See Join and Direct Transfer Policy, Product Specific Configuration .

EnergyWise

Enables an IP Phone to sleep (power down) and wake (power up) at
                                          						predetermined times, to promote energy savings.

See Schedule EnergyWise on Cisco IP Phone .

Enhanced Line Mode

Enable Enhanced Line Mode to use the buttons on both sides of the phone screen as line keys.

See Set Up Additional Line Keys

Enhanced Secure Extension Mobility Cross Cluster (EMCC)

Improves the Secure Extension Mobility Cross Cluster (EMCC)
                                          						feature by preserving the network and security configurations on the login
                                          						phone. By so doing, security policies are maintained, network bandwidth is
                                          						preserved and network failure is avoided within the visiting cluster (VC).

Fast
                                          						Dial Service

Allows
                                          						a user to enter a Fast Dial code to place a call. Fast Dial codes can be
                                          						assigned to phone numbers or Personal Address Book entries. See "Services" in this table.

See Modify Phone Button Template for PAB or Fast Dial .

Group
                                          						Call Pickup

Allows
                                          						a user to answer a call that is ringing on a directory number in another group.

See
                                          						call pickup information in the documentation for your particular Cisco Unified Communications Manager release.

Headset Sidetone Control

Allows
                                          						an administrator to set the sidetone level of a wired headset.

Hold
                                          						Reversion

Limits
                                          						the amount of time that a call can be on hold before reverting back to the
                                          						phone that put the call on hold and alerting the user.

Reverting calls are distinguished from incoming calls by a
                                          						single ring (or beep, depending on the new call indicator setting for the
                                          						line). This notification repeats at intervals if not resumed.

A call
                                          						that triggers Hold Reversion also displays an animated icon in the call bubble.
                                          						You can configure call focus priority to favor incoming or reverting calls.

Hold
                                          						Status

Enables phones with a shared line to distinguish between the
                                          						local and remote lines that placed a call on hold.

Hold/Resume

Allows
                                          						the user to move a connected call from an active state to a held state.

No
                                                							 configuration required unless you want to use Music On Hold. See "Music On Hold" in this table for information.

See "Hold Reversion" in this table.

HTTP
                                          						Download

Enhances the file download process to the phone to use HTTP by
                                          						default. If the HTTP download fails, the phone reverts to using the TFTP
                                          						download.

Hunt
                                          						Group

Provides load sharing for calls to a main directory number. A
                                          						hunt group contains a series of directory numbers that can answer the incoming
                                          						calls. When the first directory number in the hunt group is busy, the system
                                          						hunts in a predetermined sequence for the next available directory number in
                                          						the group and directs the call to that phone.

You can have Caller ID (If the Caller ID is configured), Directory Number and Hunt group Pilot Number display on the Incoming Call Alert for the hunt group call. The hunt group number is displayed after the label "Hunt Group.

See hunt group and routing plans information in the documentation for your particular Cisco Unified Communications Manager
                                          release.

Incoming Call Toast Timer

Allows
                                          						you to set the length of time that an incoming call toast (notification)
                                          						appears on the phone screen.

See Incoming Call Toast Timer, Product Specific Configuration .

Intelligent Proximity

Enables users to pair a mobile device with the phone using
                                          						Bluetooth and use the phone to place and receive mobile calls,

See Enable Intelligent Proximity .

Cisco IP Phone 8811, 8841, and 8851NR do not support Bluetooth or Intelligent Proximity.

Intercom

Allows
                                          						users to place and receive intercom calls using programmable phone buttons. You
                                          						can configure intercom line buttons to:

Directly dial a specific intercom extension.

Initiate an intercom call and then prompt the user to enter a valid intercom number.

If
                                                      						  your user logs into the same phone on a daily basis using their Cisco Extension
                                                      						  Mobility profile, assign the phone button template that contains intercom
                                                      						  information to their profile, and assign the phone as the default intercom
                                                      						  device for the intercom line.

IPv6-only Support

Provides support for expanded IP addressing on Cisco IP Phones. IPv4 and IPv6 configuration is recommended and fully supported.
                                          Certain features are not supported in a standalone configuration. Only IPv6 address are assigned.

See Configure Network Settings .

Jitter
                                          						Buffer

The
                                          						Jitter Buffer feature handles jitter from 10 milliseconds (ms) to 1000 ms for
                                          						audio streams.

It runs in an adaptive mode and it dynamically adjusts to the amount of jitter.

Join

Allows
                                          						users to combine two calls that are on one line to create a conference call and
                                          						remain on the call.

Line
                                          						Status for Call Lists

Allows
                                          						the user to see the Line Status availability status of monitored line numbers
                                          						in the Call History list. The Line Status states are

Offline

Available

In
                                                							 use

Do
                                                							 not disturb

See Enable BLF for Call Lists .

Line Status in Corporate Directory

Enables the display of the status of a contact in the Corporate Directory.

Offline

Available

In use

Do not disturb

See Enable BLF for Call Lists .

Line Text Label

Sets a text label for a phone line instead of the directory number.

See Set the Label for a Line .

Log
                                          						out of hunt groups

Allows
                                          						users to log out of a hunt group and temporarily block calls from ringing their
                                          						phone when they are not available to take calls. Logging out of hunt groups
                                          						does not prevent nonhunt group calls from ringing their phone.

See 
                                          						routing plan information in the documentation for your particular Cisco Unified Communications Manager release.

Malicious Caller Identification (MCID)

Allows
                                          						users to notify the system administrator about suspicious calls that are
                                          						received.

Meet
                                          						Me Conference

Allows
                                          						a user to host a Meet Me conference in which other participants call a
                                          						predetermined number at a scheduled time.

Message Waiting

Defines directory numbers for message waiting on and off
                                          						indicators. A directly-connected voice-message system uses the specified
                                          						directory number to set or to clear a message waiting indication for a
                                          						particular Cisco IP Phone.

See message waiting and voice mail information in the documentation for your particular Cisco Unified Communications Manager
                                          release.

Message Waiting Indicator

A
                                          						light on the handset that indicates that a user has one or more new voice
                                          						messages.

See message waiting and voice mail information in the documentation for your particular Cisco Unified Communications Manager
                                          release.

Minimum Ring Volume

Sets a
                                          						minimum ringer volume level for an IP phone.

Missed
                                          						Call Logging

Allows
                                          						a user to specify whether missed calls will be logged in the missed calls
                                          						directory for a given line appearance.

See
                                          						directory number information in the documentation for your particular Cisco Unified Communications Manager release.

Mobile
                                          						Connect

Enables users to manage business calls using a single phone
                                          						number and pick up in-progress calls on the desk phone and a remote device such
                                          						as a mobile phone. Users can restrict the group of callers according to phone
                                          						number and time of day.

See Cisco Unified Mobility information in the documentation for your particular Cisco Unified Communications Manager release.

Mobile and Remote Access
                                             				Through Expressway

Allows remote workers to easily and securely connect into the corporate network without using a virtual private network (VPN)
                                          client tunnel.

See Mobile and Remote Access Through Expressway

Mobile
                                          						Voice Access

Extends Mobile Connect capabilities by allowing users to access
                                          						an interactive voice response (IVR) system to originate a call from a remote
                                          						device such as a cellular phone.

See
                                          						Cisco Unified Mobility in the documentation for your particular Cisco Unified Communications Manager release.

Monitoring and Recording

Allows
                                          						a supervisor to silently monitor an active call. The supervisor cannot be heard
                                          						by either party on the call. The user might hear a monitoring audible alert
                                          						tone during a call when it is being monitored.

When a
                                          						call is secured, the security status of the call is displayed as a lock icon on
                                          						Cisco IP Phones. The connected parties might also hear an audible alert tone
                                          						that indicates the call is secured and is being monitored.

When
                                                      						  an active call is being monitored or recorded, the use can receive or place
                                                      						  intercom calls; however, if the user place an intercom call, the active call
                                                      						  will be put on hold, which causes the recording session to terminate and the
                                                      						  monitoring session to suspend. To resume the monitoring session, the party
                                                      						  whose call is being monitored must resume the call.

Multilevel Precedence and Preemption

Enables the user to make and receive urgent or critical calls in some specialized environments, such as military or government
                                          offices.

See Multilevel Precedence and Preemption .

Multiple Calls Per Line Appearance

Each
                                          						line can support multiple calls. By default, the phone supports two active
                                          						calls per line, and a maximum of six active calls per line. Only one call can
                                          						be connected at any time; other calls are automatically placed on hold.

The
                                          						system allows you to configure maximum calls/busy trigger not more than 6/6.
                                          						Any configuration more than 6/6 is not officially supported.

See
                                          						directory number information in the documentation for your particular Cisco Unified Communications Manager release.

Music
                                          						On Hold

Plays
                                          						music while callers are on hold.

Mute

Mutes
                                          						the handset or headset microphone.

No
                                          						Alert Name

Makes
                                          						it easier for end users to identify transferred calls by displaying the
                                          						original caller’s phone number. The call appears as an Alert Call followed by
                                          						the caller’s telephone number.

Onhook
                                          						Dialing

Allows
                                          						a user to dial a number without going off hook. The user can then either pick
                                          						up the handset or press Dial.

Other
                                          						Group Pickup

Allows
                                          						a user to answer a call ringing on a phone in another group that is associated
                                          						with the user's group.

See
                                          						call pickup information in the documentation for your particular Cisco Unified Communications Manager release.

Phone
                                          						Display Message for Extension Mobility Users

This
                                          						feature enhances the phone interface for the Extension Mobility user by
                                          						providing friendly messages.

Phone Trust List Notification in Cisco Unified Communications Manager

Enables the phone to send an alarm to the Cisco Unified Communications Manager when the Trust List (TL) is updated.

See Supported Security Features .

PLK
                                          						Support for Queue Statistics

The
                                          						PLK Support for Queue Statistics feature enables the users to query the call
                                          						queue statistics for hunt pilots and the information appears on phone screen.

Plus
                                          						Dialing

Allows
                                          						the user to dial E.164 numbers prefixed with a plus (+) sign.

To
                                          						dial the + sign, the user needs to press and hold the star (*) key for at least
                                          						1 second. This applies to dialing the first digit for an on-hook (including
                                          						edit mode) or off-hook call.

Power
                                          						Negotiation over LLDP

Allows the phone to negotiate power using Link Level Endpoint Discovery Protocol (LLDP) and Cisco Discovery Protocol (CDP).

See Power Negotiation, Product Specific Configuration .

Predictive Dialing

Simplifies making a call. The Recents list changes to displays only phone numbers similar to the number being dialed.

Predictive Dialing is enabled when Enhanced Line mode is enabled. Simplified New Call UI must be disabled for Predictive Dialing
                                          to function.

Privacy

Prevents users who share a line from adding themselves to a call
                                          						and from viewing information on their phone display about the call of the other
                                          						user.

See barge and privacy information in the documentation for your particular Cisco Unified Communications Manager release.

Private Line Automated Ringdown (PLAR)

The
                                          						Cisco Unified Communications Manager administrator can configure a phone number
                                          						that the Cisco IP Phone dials as soon as the handset goes off hook. This can be
                                          						useful for phones that are designated for calling emergency or "hotline" numbers.

The administrator can configure a delay
                                          									of up to 15-seconds. This allows the user time to place a call
                                          									before the phone defaults to the hotline number. The timer is
                                          									configurable through the parameter Off Hook To First
                                             										Digit Timer under Device > Device Settings > SIP Profile .

For more information, refer to Feature Configuration Guide for
                                             										Cisco Unified Communications Manager .

Problem Report Tool (PRT)

Submit phone logs or report problems to an administrator.

See Problem Report Tool .

Programmable Feature Buttons

You
                                          						can assign features, such as New Call, Call Back, and Forward All to line
                                          						buttons.

See phone button template information in the documentation for your particular Cisco Unified Communications Manager release.

Quality Reporting Tool (QRT)

Allows
                                          						users to submit information about problem phone calls by pressing a button. QRT
                                          						can be configured for either of two user modes, depending upon the amount of
                                          						user interaction desired with QRT.

Recents

Allows users to see the 150 most recent individual calls and call groups. You can see the recently dialed numbers, missed
                                          calls, and delete a call record.

Redial

Allows
                                          						users to call the most recently dialed phone number by pressing a button or the
                                          						Redial softkey.

Remote
                                          						Port Configuration

Allows
                                          						you to configure the speed and duplex function of the phone Ethernet ports
                                          						remotely by using Cisco Unified Communications Manager Administration. This
                                          						enhances the performance for large deployments with specific port settings.

If
                                                      						  the ports are configured for Remote Port Configuration in Cisco Unified
                                                      						  Communications Manager, the data cannot be changed on the phone.

See Remote Port Configuration, Product Specific Configuration .

Reroute Direct Calls to Remote Destination to Enterprise Number

Reroutes a direct call to a user's mobile phone to the
                                          						enterprise number (desk phone). For an incoming call to remote destination
                                          						(mobile phone), only remote destination rings; desk phone does not ring. When
                                          						the call is answered on their mobile phone, the desk phone displays a Remote In
                                          						Use message. During these calls, users can make use of various features of
                                          						their mobile phone.

See
                                          						the 
                                          						Cisco Unified Mobility information in the documentation for your particular Cisco Unified Communications Manager release.

Remove 'Call Ended' Prompt Timer

Improves the End Call response time by removing the Call ended message display on the phone screen.

Ringtone Setting

Identifies ring type used for a line when a phone has another
                                          						active call.

See directory number information in the documentation for your particular Cisco Unified Communications Manager release and Custom Phone Rings .

RTCP
                                          						Hold For SIP

Ensures that held calls are not dropped by the gateway. The
                                          						gateway checks the status of the RTCP port to determine if a call is active or
                                          						not. By keeping the phone port open, the gateway will not end held calls.

Secure
                                          						Conference

Allows secure phones to place conference calls using a secured conference bridge. As new participants are added by using Confrn,
                                          Join, or Barge softkeys or MeetMe conferencing, the secure call icon displays as long as all participants use secure phones.

The
                                          						Conference List displays the security level of each conference participant.
                                          						Initiators can remove nonsecure participants from the Conference List.
                                          						Noninitiators can add or remove conference participants if the Advanced Adhoc
                                          						Conference Enabled parameter is set.

See conference bridge and security information in the documentation for your particular Cisco Unified Communications Manager
                                          release and Supported Security Features .

Secure
                                          						EMCC

Improves the EMCC feature by providing enhanced security for a
                                          						user logging into their phone from a remote office.

Services

Allows
                                          						you to use the Cisco IP Phone Services Configuration menu in Cisco Unified
                                          						Communications Manager Administration to define and maintain the list of phone
                                          						services to which users can subscribe.

See services information in the documentation for your particular Cisco Unified Communications Manager release.

Services URL button

Allows
                                          						users to access services from a programmable button rather than by using the
                                          						Services menu on a phone.

See services information the documentation for your particular Cisco Unified Communications Manager release.

Show
                                          						Calling ID and Calling Number

The
                                          						phones can display both the calling ID and calling number for incoming calls.
                                          						The IP phone LCD display size limits the length of the calling ID and the
                                          						calling number that display.

The
                                          						Show Calling ID and Calling Number feature applies to the incoming call alert
                                          						only and does not change the function of the Call Forward and Hunt Group
                                          						features.

See "Caller ID" in this table.

Simplify Extension Mobility Login with Cisco Headsets

Enables users to sign into Extension Mobility with their Cisco headsets.

When the phone is in MRA mode, the user can use the headset to sign into the phone.

This feature requires Cisco Unified Communications Manager(UCM) Release 11.5(1)SU8, 11.5(1)SU.9, 12.5(1)SU3, 14.0(1) or later.

For more information, see Feature Configuration Guide for Cisco Unified Communications Manager , Release 11.5(1)SU8 or later, or Release 12.5(1)SU3 or later.

With Cisco Headset 720/730/950/980, user can also sign into Extension Mobility with the headset USB adapter (USB HD adapter
                                          or USB-C adapter).

Simplified Tablet Support

Enables an Android or iOS tablet user to pair the tablet to the phone using Bluetooth and then use the phone for the audio
                                          part of a call on the tablet.

See Enable Intelligent Proximity .

Cisco IP Phone 8851NR does not support Bluetooth.

Speed
                                          						Dial

Dials
                                          						a specified number that has been previously stored.

SSH
                                          						Access

Allows you to enable or disable the SSH Access setting using Cisco Unified Communications Manager Administration. Enabling
                                          the SSH server allows the phone to accept the SSH connections. Disabling the SSH server functionality of the phone blocks
                                          the SSH access to the phone.

See SSH Access, Product Specific Configuration .

Time-of-Day Routing

Restricts access to specified telephony features by time period.

See time period and time-of-day routing information in the documentation for your particular Cisco Unified Communications
                                          Manager release.

Time
                                          						Zone Update

Updates the Cisco IP Phone with time zone changes.

See
                                          						date and time information in the documentation for your particular Cisco Unified Communications Manager release.

Transfer

Allows
                                          						users to redirect connected calls from their phones to another number.

Transfer - Direct Transfer

Transfer: The first invocation of Transfer will always initiate
                                          						a new call by using the same directory number, after putting the active call on
                                          						hold.

The
                                          						user can directly transfer calls using Transfer Active Call Function.

Some
                                          						JTAPI/TAPI applications are not compatible with the Join and Direct Transfer
                                          						feature implementation on the Cisco IP Phone and you may need to configure the
                                          						Join and Direct Transfer Policy to disable join and direct transfer on the same
                                          						line or possibly across lines.

See 
                                          						directory number information in the documentation for your particular Cisco Unified Communications Manager release.

TVS

Trust
                                          						Verification Services (TVS) enables phones to authenticate signed
                                          						configurations and authenticate other servers or peers without increasing the
                                          						size of the Certificate Trust List (CTL) or requiring the downloading of an
                                          						updated CTL file to the phone. TVS is enabled by default.

The
                                          						Security Setting menu on the phone displays the TVS information.

UCR
                                          						2013

The
                                          						Cisco IP Phones support Unified Capabilities Requirements (UCR) 2013 by
                                          						providing the following functions:

Support for Federal Information Processing Standard (FIPS) 140-3

Support for 80-bit SRTCP Tagging

As an
                                          						IP Phone administrator, you must set up specific parameters in Cisco Unified
                                          						Communications Manager Administration.

Unconfigured Primary Line Notification

Alerts the user when the primary line is not configured. The user sees the message Unprovisioned on the phone screen.

User Interface Updates for List, Alert, and Visual Voicemail.

Increases the size of the application window to minimize truncated strings.

Video Mode

Allows a user to select the video display mode for viewing a video conference, depending on the modes configured in the system.

See video information in the documentation for your particular Cisco Unified Communications Manager release.

Available on Cisco IP Phone 8845, 8865, and 8865NR.

Video Support

Enables video support on the phone. The Video Capabilities parameter needs to be enabled for video calls on Cisco Unified
                                          Communications Manager Phone Configuration window. It is enabled by default.

Available on Cisco IP Phone 8845, 8865, and 8865NR.

Video Through PC

Allows users to make video calls by using their Cisco Unified IP Phone, personal computer, and an external video camera.

The feature also allows users to make video calls with Cisco Jabber or Cisco Unified Video Advantage products.

Visual
                                          						Voicemail

Replaces the voicemail audio prompts with a graphical interface.

See Installation and Configuration Guide for Visual Voicemail located at http://www.cisco.com/en/US/partner/products/ps9829/prod_installation_guides_list.html#anchor3 .

Voice
                                          						Message System

Enables callers to leave messages if calls are unanswered.

See voice mail information in the documentation for your particular Cisco Unified Communications Manager release and Set up Visual Voicemail .

VPN

Using SSL, provides a virtual private network (VPN) connection on
                                          the Cisco Unified IP Phone when it is located outside a trusted
                                          network or when network traffic between the phone and Unified
                                          Communications Manager must cross untrusted networks.

Web
                                          						Access Disabled by Default

Enhances security by disabling access to all web services, such
                                          						as HTTP. Users can only access web services if you enable web access.

## Feature Buttons
                        	 and Softkeys

The following table provides information about features that are available on softkeys, features that are available on dedicated
                              feature buttons, and features that you need to configure as programmable feature buttons. A "Supported" entry in the table indicates that the feature is supported for the corresponding button type or softkey. Of the two button
                              types and softkeys, only programmable feature buttons require configuration in Cisco IP Phone administration.

For
                              		  information about configuring programmable feature buttons, see Phone Button Templates .

Feature
                                          					 name

Dedicated
                                          					 feature button

Programmable feature button

Softkey

Alert
                                          					 Calls

Not supported

Supported

Not supported

All Calls

Not supported

Supported

Not supported

Answer

Not supported

Supported

Supported

cBarge

Not supported

Not supported

Supported

Call Back

Not supported

Supported

Supported

Call
                                          					 Forward All

Not supported

Not supported

Supported

Call Park

Not supported

Supported

Supported

Call Park
                                          					 Line Status

Not supported

Supported

Not supported

Call
                                          					 Pickup (Pick Up)

Not supported

Supported

Supported

Call
                                          					 Pickup Line Status

Not supported

Supported

Not supported

Conference

Supported

Not supported

Supported

Divert

Not supported

Not supported

Supported

Do Not
                                          					 Disturb

Not supported

Supported

Supported

Group
                                          					 Pickup (Group Pick Up)

Not supported

Supported

Supported

Hold

Supported

Not supported

Supported

Hunt
                                          					 Groups

Not supported

Supported

Not supported

Intercom

Not supported

Supported

Not supported

Malicious Call Identification (MCID)

Not supported

Supported

Supported

Meet Me

Not supported

Supported

Supported

Merge

Not supported

Not supported

Supported

Mobile
                                          					 Connect (Mobility)

Not supported

Supported

Supported

Mute

Supported

Not supported

Not supported

Other
                                          					 Pickup

Not supported

Supported

Supported

PLK
                                          					 Support for Queue Status

Not supported

Not supported

Supported

Privacy

Not supported

Supported

Not supported

Queue
                                          					 Status

Not supported

Supported

Not supported

Quality
                                          					 Reporting Tool (QRT)

Not supported

Supported

Supported

Record

Not supported

Not supported

Supported

Redial

Not supported

Supported

Supported

Speed
                                          					 Dial

Not supported

Supported

Not supported

Speed
                                          					 Dial Line Status

Not supported

Supported

Not supported

Support
                                          					 for Hold Button on USB Headsets

Not supported

Not supported

Supported

Transfer

Supported

Not supported

Supported

## Phone Feature Configuration

You can set up phones to have a variety of features, based on the needs of your users. You can apply features to all phones,
                              a group of phones, or to individual phones.

When you set up features, the Cisco Unified
                                 				Communications Manager Administration window displays information that is applicable to all phones and information that is applicable to the phone model. The information
                              that is specific to the phone model is in the Product Specific Configuration Layout area of the window.

For information on the fields applicable to all phone models, see the Cisco Unified
                                 				Communications Manager documentation.

When you set a field, the window that you set the field in is important because there is a precedence to the windows. The
                              precedence order is:

Individual phones (highest precedence)

Group of phones

All phones (lowest precedence)

For example, if you don't want a specific set of users to access the phone Web pages, but the rest of your users can access
                              the pages, you:

Enable access to the phone web pages for all users.

Disable access to the phone web pages for each individual user, or set up a user group and disable access to the phone web
                                    pages for the group of users.

If a specific user in the user group did need access to the phone web pages, you could enable it for that particular user.

### Set Up Phone Features for All Phones

Step 1

Sign in to Cisco Unified
                                             				Communications Manager Administration as an administrator.

Step 2

Select System > Enterprise Phone Configuration .

Step 3

Set the fields you want to change.

Step 4

Check the Override Enterprise Settings check box for any changed fields.

Step 5

Click Save .

Step 6

Click Apply Config .

Step 7

Restart the phones.

This will impact all phones in your organization.

### Set Up Phone Features for a Group of Phones

Step 1

Sign in to Cisco Unified
                                             				Communications Manager Administration as an administrator.

Step 2

Select Device > Device Settings > Common Phone Profile .

Step 3

Locate the profile.

Step 4

Navigate to the Product Specific Configuration Layout pane and set the fields.

Step 5

Check the Override Enterprise Settings check box for any changed fields.

Step 6

Click Save .

Step 7

Click Apply Config .

Step 8

Restart the phones.

### Set Up Phone Features for a Single Phone

Step 1

Sign in to Cisco Unified
                                             				Communications Manager Administration as an administrator.

Step 2

Select Device > Phone

Step 3

Locate the phone associated with the user.

Step 4

Navigate to the Product Specific Configuration Layout pane and set the fields.

Step 5

Check the Override Common Settings check box for any changed fields.

Step 6

Click Save .

Step 7

Click Apply Config .

Step 8

Restart the phone.

### Product Specific Configuration

The following table describes the fields in the Product Specific Configuration Layout pane.

Field Name

Field Type

or Choices

Default

Description and Usage Guidelines

Disable Speakerphone

Check box

Unchecked

Turns off the speakerphone capability of the phone.

Disable Speakerphone and Headset

Check box

Unchecked

Turns off the speakerphone and headset capability of the phone.

Disable Handset

Checkbox

Unchecked

Turns off the handset capability of the phone.

PC Port

Enabled

Disabled

Enabled

Controls the ability to use the PC port to connect a computer into the LAN.

Settings Access

Disabled

Enabled

Restricted

Enabled

Enables, disables, or restricts access to the local phone configuration settings in the Settings app.

Disabled—The Settings menu does not display any options.

Enabled—All entries in the Settings menu are accessible.

Restricted—Only the Phone settings menu is accessible.

PC Voice VLAN Access

Enabled

Disabled

Enabled

Indicates whether the phone will allow a device attached to the PC port to access the Voice VLAN.

Disabled—The PC can't send and receive data on the Voice VLAN or from the phone.

Enabled—The PC can send and receive data from the Voice VLAN or from the phone. Set this field to Enabled if an application
                                                   is being run on the PC that to monitor phone traffic. These applications could include monitoring and recording applications,
                                                   and the use of network monitoring software for analysis purposes.

Video Capabilities

Enabled

Disabled

8845, 8865, and 8865NR: Enabled

8811, 8851, 8851NR, 8861: Disabled

Allows users to make video calls by using a Cisco IP Phone, a personal computer, and a video camera.

Web Access

Disabled

Enabled

Disabled

Enables or disables access to the phone web pages through a web browser.

Caution

If you enable this field, you may expose sensitive
                                                         										information about the phone.

Disable TLS 1.0 and TLS 1.1 for Web Access

Disabled

Enabled

Enabled

Controls the use of TLS 1.2 for a web server connection.

Disabled—A phone configured for TLS1.0, TLS 1.1, or TLS1.2 can function as a HTTPs server.

Enabled—Only a phone configured for TLS1.2 can function as a HTTPs server.

TLS Client Min Version

TLS 1.0

TLS 1.1

TLS 1.2

TLS 1.2

Specifies the minimum TLS version required by the phone to establish a TLS connection.

This parameter is available when the phone acts as a client.

If the TLS version on the server side is older than the required minimum TLS version on the phone, the TLS connection will
                                             be rejected.

TLS 1.0 : The TLS client (phone) supports the versions of TLS from 1.0 to 1.2.

TLS 1.1 : The TLS client (phone) supports TLS 1.1 and TLS 1.2.

If the TLS version in server is lower than 1.1, for example, 1.0, then the connection can't be established.

TLS 1.2 : The TLS client (phone) supports TLS 1.2 only.

If the TLS version in server is lower than 1.2, for example, 1.0 or 1.1, then the connection can't be established.

This parameter is unavailable for the wireless networks.

Enbloc Dialing

Disabled

Enabled

Disabled

Controls the dialing method.

Disabled—The Cisco Unified Communications Manager waits for the interdigit timer to expire when there is a dial plan or route
                                                   pattern overlap.

Enabled—The entire dialed string is sent to Cisco Unified Communications Manager once the dialing is complete. To avoid the
                                                   T.302 timer timeout, we recommend that you enable Enbloc Dialing whenever there is a dialplan or route pattern overlap.

Forced Authorization Codes (FAC) or Client Matter Codes (CMC) do not support the Enbloc Dialing. If you use FAC or CMC to
                                             manage call access and accounting, then you cannot use this feature.

Days Display Not Active

Days of the week

Defines the days that the display does not turn on automatically at the time specified in the Display On Time field.

Choose the day or days from the drop-down list. To choose more than one day, Ctrl+click each day that you want.

Display On Time

hh:mm

Defines the Time each day that the display turns on automatically (except on the days specified in the Days Display Not Active
                                             field).

Enter the time in this field in 24 hour format, where 0:00 is midnight.

For example, to automatically turn the display on at 07:00 a.m. (0700), enter 07:00. To turn the display on at 02:00 p.m.
                                             (1400), enter 14:00.

If this field is blank, the display automatically turns on at 0:00.

Display On Duration

hh:mm

Defines the length of time that the display remains on after turning on at the time specified in the Display On Time field.

For example, to keep the display on for 4 hours and 30 minutes after it turns on automatically, enter 04:30.

If this field is blank, the phone turns off at the end of the day (0:00).

If Display On Time is 0:00 and the display on duration is blank (or 24:00), the display does not turn off.

Display Idle Timeout

hh:mm

01:00

Defines the length of time that the phone is idle before the display turns off. Applies only when the display was off as scheduled
                                             and was turned on by a user (by pressing a button on the phone or lifting the handset).

Enter the value in this field in the format hours:minutes.

For example, to turn the display off when the phone is idle for 1 hour and 30 minutes after a user turns the display on, enter
                                             01:30.

For more information, see Set Up Idle Display .

Display On When Incoming Call

Disabled

Enabled

Enabled

Turns the idle display on when there is an incoming call.

Enable Power Save Plus

Days of the week

Defines the schedule of days for which the phone powers off.

Choose the day or days from the drop-down list. To choose more than one day, Ctrl+click each day that you want.

When Enable Power Save Plus is turned on, you receive a message that warns about emergency (e911) concerns.

Caution

While Power Save Plus Mode (the “Mode”) is in effect, endpoints that are configured for the mode are disabled for emergency
                                                         calling and from receiving inbound calls. By selecting this mode, you agree to the following: (i) You take full responsibility
                                                         for providing alternate methods for emergency calling and receiving calls while the mode is in effect; (ii) Cisco has no liability
                                                         in connection with your selection of the mode and all liability in connection with enabling the mode is your responsibility;
                                                         and (iii) You fully inform users of the effects of the mode on calls, calling and otherwise.

To disable Power Save Plus, you must uncheck the Allow EnergyWise Overrides check box. If the Allow EnergyWise Overrides remains
                                             checked but no days are selected in the Enable Power Save Plus field, Power Save Plus is not disabled.

Phone On Time

hh:mm

Determines when the phone automatically turns on for the days that are in the Enable Power Save Plus field.

Enter the time in this field in 24-hour format, where 00:00 is midnight.

For example, to automatically power up the phone at 07:00 a.m. (0700), enter 07:00. To power up the phone at 02:00 p.m. (1400),
                                             enter 14:00.

The default value is blank, which means 00:00.

The Phone On Time must be at least 20 minutes later than the Phone Off Time. For example, if the Phone Off Time is 07:00,
                                             the Phone On Time must be no earlier than 07:20.

Phone Off Time

hh:mm

Identifies the time of day that the phone powers down for the days that are selected in the Enable Power Save Plus field.
                                             If the Phone On Time and the Phone Off Time fields contain the same value, the phone does not power down.

Enter the time in this field in 24-hour format, where 00:00 is midnight.

For example, to automatically power down the phone at 7:00 a.m. (0700), enter 7:00. To power down the phone at 2:00 p.m. (1400),
                                             enter 14:00.

The default value is blank, which means 00:00.

The Phone On Time must be at least 20 minutes later than the Phone Off Time. For example, if the Phone Off Time is 7:00, the
                                             Phone On Time must be no earlier than 7:20.

Phone Off Idle Timeout

20 to 1440 minutes

60

Indicates the length of time that the phone must be idle before the phone powers down.

The timeout occurs under the following conditions:

When the phone was in Power Save Plus mode, as scheduled, and was taken out of Power Save Plus mode because the phone user
                                                   pressed the Select key.

When the phone is repowered by the attached switch.

When the Phone Off Time is reached but the phone is in use.

Enable Audible Alert

Check box

Unchecked

When enabled, instructs the phone to play an audible alert starting 10 minutes before the time that the Phone Off Time field
                                             specifies.

This check box applies only if the Enable Power Save Plus list box has one or more days selected.

EnergyWise Domain

Up to 127 characters

Identifies the EnergyWise domain that the phone is in.

EnergyWise Secret

Up to 127 characters

Identifies the security secret password that is used to communicate with the endpoints in the EnergyWise domain.

Allow EnergyWise Overrides

Check box

Unchecked

Determines whether you allow the EnergyWise domain controller policy to send power level updates to the phones. The following
                                             conditions apply:

One or more days must be selected in the Enable Power Save Plus field.

The settings in Cisco Unified Communications Manager Administration take effect on schedule even if EnergyWise sends an override.

For example, assuming the Phone Off Time is set to 22:00 (10:00 p.m.), the value in the Phone On Time field is 06:00 (6:00
                                             a.m.), and the Enable Power Save Plus has one or more days selected.

If EnergyWise directs the phone to turn off at 20:00 (8:00 p.m.), that directive remains in effect (assuming no phone user
                                                   intervention occurs) until the configured Phone On Time at 6:00 a.m.

At 6:00 a.m., the phone turns on and resumes receiving the power level changes from the settings in Cisco Unified Communications
                                                   Manager Administration.

To change the power level on the phone again, EnergyWise must reissue a new power level change command.

To disable Power Save Plus, you must uncheck the Allow EnergyWise Overrides check box. If the Allow EnergyWise Overrides remains
                                             checked but no days are selected in the Enable Power Save Plus field, Power Save Plus is not disabled.

Join and Direct Transfer Policy

Same line, across line enable

Same line enable only

Same line, across line disable

Same line, across line enable

Controls the ability of a user to join and transfer calls.

Same line, across line enable—Users can directly transfer or join a call on current line to another call on another line.

Same line enable only—Users can only directly transfer or join the calls when both calls are on same line.

Same line, across line disable— Users can't join or transfer calls on the same line. The join and transfer features are disabled
                                                   and the user can't do the direct transfer or join function.

Span to PC Port

Disabled

Enabled

Disabled

Indicates whether the phone forwards packets that are transmitted and received on the network port to the access port.

Recording Tone

Disabled

Enabled

Disabled

Controls the playing of the tone when a user is recording a call.

Recording Tone Local Volume

Integer 0–100

100

Controls the volume of the recording tone to the local user.

Recording Tone Remote Volume

Integer 0–100

50

Controls the volume of the recording tone to the remote user.

Recording Tone Duration

Integer 1–3000 milliseconds

Controls the duration of the recording tone.

Log Server

String of up to 256 characters

Identifies the IPv4 syslog server for phone debug output.

The format for the address is: address:<port>@@base=<0-7>;pfs=<0-1>

Cisco Discovery Protocol (CDP): Switch Port

Disabled

Enabled

Enabled

Controls Cisco Discovery Protocol on the SW port of the phone.

Cisco Discovery Protocol (CDP): PC Port

Disabled

Enabled

Enabled

Controls Cisco Discovery Protocol on the PC port of the phone.

Link Layer Discovery Protocol - Media Endpoint Discover (LLDP-MED): Switch Port

Disabled

Enabled

Enabled

Enables LLDP-MED on the SW port.

Link Layer Discovery Protocol (LLDP): PC Port

Disabled

Enabled

Enabled

Enables LLDP on the PC port.

LLDP Asset ID

String, up to 32 characters

Identifies the asset ID that is assigned to the phone for inventory management.

LLDP Power Priority

Unknown

Low

High

Critical

Unknown

Assigns a phone power priority to the switch, thus enabling the switch to appropriately provide power to the phones.

802.1x Authentication

User Controlled

Enabled

Disabled

User Controlled

Specifies the 802.1x authentication feature status.

User Controlled—The user can configure the 802.1x on the phone.

Disabled—802.1x Authentication is not used.

Enabled—802.1x authentication is used, and you configure the authentication for the phones.

Automatic Port Synchronization

Disabled

Enabled

Disabled

Synchronizes ports to the lowest speed between ports of a phone to eliminate packet loss.

Switch Port Remote Configuration

Disabled

Enabled

Disabled

Allows you to configure the speed and duplex function of the phone SW port remotely. This enhances the performance for large
                                             deployments with specific port settings.

If the SW ports are configured for Remote Port Configuration in Cisco Unified Communications Manager, the data cannot be changed
                                             on the phone.

PC Port Remote Configuration

Disabled

Enabled

Disabled

Allows you to configure the speed and duplex function of the phone PC port remotely. This enhances the performance for large
                                             deployments with specific port settings.

If the ports are configured for Remote Port Configuration in Cisco Unified Communications Manager, the data cannot be changed
                                             on the phone.

SSH Access

Disabled

Enabled

Disabled

Controls the access to the SSH daemon through port 22. Leaving port 22 open leaves the phone vulnerable to Denial of Service
                                             (DoS) attacks.

Incoming Call Toast Timer

0, 3, 4, 5, 6, 7, 8, 9, 10, 15, 30, 60

5

Gives the time, in seconds, that the toast displays. The time includes the fade-in and fade-out times for the window.

0 means that the incoming call toast is disabled.

Ring Locale

Default

Japan

Default

Controls the ringing pattern.

TLS Resumption Timer

Integer 0–3600 seconds

3600

Controls the ability to resume a TLS session without repeating the entire TLS authentication process. If the field is set
                                             to 0, then the TLS session resumption is disabled.

FIPS Mode

Disabled

Enabled

Disabled

Enables or disables the Federal Information Processing Standards (FIPS) mode on the phone.

Record Call Log from Shared Line

Disabled

Enabled

Disabled

Specifies whether to record a shared line call in the call log.

Minimum Ring Volume

0-Silent

1–15

0-Silent

Controls the minimum ring volume for the phone.

You can set a phone so that the ringer cannot be turned off.

Peer Firmware Sharing

Disabled

Enabled

Enabled

Allows the phone to find other phones of the same model on the subnet and share updated firmware files. If the phone has a
                                             new firmware load, it can share that load with the other phones. If one of the other phones has a new firmware load, the phone
                                             can download the firmware from the other phone, instead of from the TFTP server.

Peer firmware sharing:

Limits congestion on TFTP transfers to centralized remove TFTP servers.

Eliminates the need to manually control firmware upgrades.

Reduces phone downtime during upgrades when large numbers of phones are reset simultaneously.

Helps with firmware upgrades in branch or remote office deployment scenarios that run over bandwidth-limited WAN links.

Load Server

String of up to 256 characters

Identifies the alternate IPv4 server that the phone uses to obtain firmware loads and upgrades.

The format for the address is: address:<port>@@base=<0-7>;pfs=<0-1>

IPv6 Load Server

String of up to 256 characters

Identifies the alternate IPv6 server that the phone uses to obtain firmware loads and upgrades.

The format for the address is: [address]:<port>@@base=<0-7>;pfs=<0-1>

Wideband Headset UI Control

Disabled

Enabled

Enabled

Allows the user to use the wideband codec for an analog headset.

Wideband Headset

Disabled

Enabled

Enabled

Enables or disables the use of a Wideband Headset on the phone. Used in conjunction with User Control Wideband Headset.

For more information, see Set Up Wideband Codec .

Wi-Fi

Disabled

Enabled

Enabled

Enables the Cisco IP Phones 8861 and 8865 to connect to the Wi-Fi network.

Phones that do not support this feature do not display the field.

Back USB Port

Disabled

Enabled

8861, 8865, and 8865NR: Enabled

Controls the ability to use the USB port on the back of the Cisco IP Phones 8861 and 8865.

Phones that do not support this feature do not display the field.

Side USB Port

Disabled

Enabled

Enabled

Controls the ability to use the USB port on the side of the Cisco IP Phones 8851, 8851NR, 8861, 8865, and 8865NR.

Phones that do not support this feature do not display the field.

Console Access

Disabled

Enabled

Disabled

Specifies whether the serial console is enabled or disabled.

Bluetooth

Disabled

Enabled

Enabled

Enables or disables the Bluetooth option on the phone. If disabled, the user cannot enable Bluetooth on the phone. Supported
                                             on the Cisco IP Phones 8845, 8851, 8861, and 8865.

Phones that do not support this feature do not display the field.

Allow Bluetooth Contacts Import

Disabled

Enabled

Enabled

Enables the user to import contacts from their connected mobile device using Bluetooth. When disabled, the user cannot import
                                             contacts from their connected mobile device on their phone. Supported on the Cisco IP Phones 8845, 8851, 8861, and 8865.

Phones that do not support this feature do not display the field.

Allow Bluetooth Mobile Handsfree Mode

Disabled

Enabled

Enabled

Enables users to take advantage of the acoustic properties of the phone with their mobile device or tablet. The user pairs
                                             the mobile device or tablet to the phone using Bluetooth. When disabled, the user cannot pair the mobile device or tablet
                                             with their phone.

With a mobile device paired, the user can place and receive mobile calls on the phone. With a tablet, the user can route the
                                             audio from the tablet to the phone.

Users can pair multiple mobile devices, tablets, and a Bluetooth headset to the phone. However, only one device and one headset
                                             can be connected at the same time.

Phones that do not support this feature do not display the field.

Bluetooth Profiles

Handsfree

Human Interface Device

Handsfree

Indicates which Bluetooth profiles on the phone are enabled or disabled.

Phones that do not support this feature do not display the field.

Gratuitous ARP

Disabled

Enabled

Disabled

Enables or disables the ability for the phone to learn MAC addresses from Gratuitous ARP. This capability is required to monitor
                                             or record voice streams.

Show All Calls on Primary Line

Disabled

Enabled

Disabled

Specifies if all calls presented to this phone will be shown on the primary line or not.

The purpose of this field is to make it easier for the end user to see all calls on all lines at a glance rather than having
                                             to choose a line to see the calls on that line. In other words, when multiple lines are configured on the phone, it typically
                                             makes more sense to be able to see all the calls on all lines in one combined display. When this feature is enabled, all calls
                                             will be shown on the primary line, but you can still choose a specific line to filter the display to show only the calls for
                                             that specific line.

HTTPS Server

HTTP and HTTPS enabled

HTTPS only

HTTP and HTTPS enabled

Controls the type of communication to the phone. If you select HTTPS only, phone communication is more secure.

IPv6 Log Server

String of up to 256 characters

Identifies the IPv6 log server.

The format for the address is: [address]:<port>@@base=<0-7>;pfs=<0-1>

Remote Log

Disabled

Enabled

Disabled

Controls the ability to send logs to the syslog server.

Log Profile

Default

Preset

Telephony

SIP

UI

Network

Media

Upgrade

Accessory

Security

Wi-Fi

VPN

Energywise

MobileRemoteAc

Preset

Specifies the predefined logging profile.

Default—Default debug logging level

Preset—Does not overwrite the phone local debug logging setting

Telephony—Logs information about Telephony or call features

SIP—Logs information about SIP signaling

UI—Logs information about the phone user interface

Network—Logs network information

Media—Logs media information

Upgrade—Logs upgrade information

Accessory—Logs accessory information

Security—Logs security information

Wi-Fi—Logs Wi-Fi information

VPN—Logs virtual private network information

Energywise—Logs energy-savings information

MobileRemoteAC—Logs Mobile and Remote Access through Expressway information

Advertise G.722 and iSAC Codecs

Use System Default

Disabled

Enabled

Use System Default

Indicates whether the phone advertises the G.722 and iSAC codecs to the Cisco Unified Communications Manager.

Use System Default—Defers to the setting specified in the enterprise parameter Advertise G.722 Codec.

Disabled—Does not advertise G.722 to the Cisco Unified Communications Manager.

Enabled—Advertises G.722 to the Cisco Unified Communications Manager.

For more information, see the note that follows the table.

Detect Unified CM Connection Failure

Normal

Delayed

Normal

Determines the sensitivity that the phone has for detecting a connection failure to Cisco Unified Communications Manager
                                             (Unified CM), which is the first step before device failover to a backup Unified CM/SRST occurs.

Normal—Detection of a Unified CM connection failure occurs at the standard system rate. Choose this value for faster recognition
                                                   of a Unified CM connection failure.

Delayed—Detection of a Unified CM connection failover occurs approximately four times slower than Normal. Choose this value
                                                   if you prefer failover to be delayed slightly to give the connection the opportunity to reestablish

The precise time difference between Normal and Delayed connection failure detection depends on many variables that are constantly
                                             changing.

This field only applies to the wired Ethernet connection.

Power Negotiation

Disabled

Enabled

Enabled

Allows the phone to negotiate power using Link Level Endpoint Discovery Protocol (LLDP) and Cisco Discovery Protocol (CDP).

Power Negotiation should not be disabled when the phone is connected to a switch that supports power negotiation. If disabled,
                                             the switch could shut off power to the phone.

Provide Dial Tone from Release Button

Disabled

Enabled

Disabled

Controls whether the user hears dial tone when the Release key is pressed.

Disabled—User doesn't hear dial tone.

Enabled—User hears dial tone.

Background Image

String up to 64 characters

Specifies the default wallpaper file. When a default wallpaper is set, the user can't change the phone wallpaper.

Simplified New Call UI

Disabled

Enabled

Disabled

Controls the user interface for off-hook dialing. When enabled, the user cannot select a number from the recent calls list.

When enabled, this field provides a simplified window for the user to place a call. The user does not see the call history
                                             pop-up window that is displayed when the phone is taken off-hook. The pop-up window display is considered useful, so Simplified
                                             New Call UI is disabled by default.

Revert to All Calls

Disabled

Enabled

Disabled

Specifies whether the phone will revert to All Calls after any call ends or not if the call is on a filter other than Primary
                                             line, All Calls, or Alerting Calls.

Show Call History for Selected Line Only

Disabled

Enabled

Disabled

Controls the display of the Recents list.

Disabled—The Recents list shows the call history for all lines.

Enabled—The Recents list shows the call history for the selected line.

Actionable Incoming Call Alert

Disabled

Show for all Incoming Call

Show for Invisible Incoming Call

Show for all Incoming Call

Controls the type of incoming call alert that displays on the phone screen. The purpose of this field is to reduce the number
                                             of button presses that the end user requires to answer a call.

- Disabled—The actionable incoming call alert is disabled and the user sees the traditional incoming call pop-up alert.

Show for all Incoming Call—The actionable incoming call alert displays for all calls regardless of visibility.

Show for Invisible Incoming Call—The actionable incoming call alert displays for calls not shown on the phone. This parameter
                                                   behaves similarly to the incoming call alert pop-up notification.

DF bit

0

1

0

Controls how network packets are sent. Packets can be sent in chunks (fragments) of various sizes.

When the DF bit is set to 1 in the packet header, the network payload does not fragment when going through network devices,
                                             such as switches and routers. Removing fragmenting avoids incorrect parsing on the receiving side, but results in slightly
                                             slower speeds.

The DF bit setting does not apply to ICMP, VPN, VXC VPN, or DHCP traffic.

Default Line Filter

List of comma-separated phone device names

Indicates the list of phones that are in the default filter.

When the default line filter is configured, users see a filter named Daily schedule in Call notifications in the Settings > Preferences menu of the phone. This daily schedule filter is in addition to the preset All Calls filter.

If the default line filter is not configured, the phone checks all provisioned lines. If configured, the phone checks the
                                             lines set on Cisco Unified Communications Manager if the user selects Default filter as the active filter, or if there are
                                             no custom filters.

Custom line filters enable you to filter on high-priority lines to reduce alert activity. You can set the alerting call notification
                                             priority on a subset of lines covered by an alert filter. The custom filter generates either traditional pop-up alerts or
                                             actionable alerts for incoming calls on the selected lines. For each filter, only the covered subset of lines will generate
                                             an alert. This feature provides a way for users with multiple lines to reduce alert activity by filtering and displaying alerts
                                             only from high-priority lines. The end users can configure this themselves. Alternatively, you can program the default line
                                             filter and push the filter down to the phone.

Lowest Alerting Line State Priority

Disabled

Enabled

Disabled

Specifies the alert state when using shared lines.

Disabled—When there is an incoming call alerting on the shared line, the LED/Line state icon reflects the alerting state instead
                                                   of Remote-In-Use.

Enabled—When there is an incoming call alerting on the shared line, the user sees the Remote-In-Use icon.

One Column Display for KEM

Disabled

Enabled

Disabled

Controls the display on the Key Expansion Module.

Disabled—The expansion module uses two-column mode.

Enabled—The expansion module uses one-column mode.

Phones that do not support this feature do not display the field.

Energy Efficient Ethernet (EEE): PC Port

Disabled

Enabled

Disabled

Controls EEE on the PC port.

Energy Efficient Ethernet (EEE): SW Port

Disabled

Enabled

Disabled

Controls EEE on the switch port.

Start Video Port

Defines the start of the port range for video calls.

Phones that do not support this feature do not display the field.

Stop Video Port

Defines the end of the port range for video calls.

Phones that do not support this feature do not display the field.

User Credentials Persistent for Expressway Sign in

Disabled

Enabled

Disabled

Controls if the phone stores the users' sign-in credentials. When disabled, the user is always sees the prompt to sign into
                                             the Expressway server for Mobile and Remote Access (MRA).

If you would like to make it easier for users to log in, you enable this field so that the Expressway login credentials are
                                             persistent. The user then only has to enter their login credentials the first time. Any time after that (when the phone is
                                             powered on off-premise), the login information is prepopulated on the Sign-in screen.

For more information, see the Mobile and Remote Access Through Expressway .

Customer support upload URL

String, up to 256 characters

Provides the URL for the Problem Report Tool (PRT).

If you deploy devices with Mobile and Remote Access through Expressway, you must also add the PRT server address to the HTTP
                                             Server Allow list on the Expressway server.

For more information, see the Mobile and Remote Access Through Expressway .

Web Admin

Disabled

Enabled

Disabled

Enables or disables administrator access to the phone web pages through a web browser

For more information, see the Configure the Administration Page for Phone .

Phones that do not support this feature do not display the field.

Admin Password

String of 8–127 characters

Defines the administrator password when you access the phone web pages as an administrator.

Phones that do not support this feature do not display the field.

WLAN SCEP Server

String of up to 256 characters

Specifies the SCEP Server that the phone uses to obtain certificates for WLAN authentication. Enter the hostname or the IP
                                             address (using standard IP addressing format) of the server.

Phones that do not support this feature do not display the field.

WLAN Root CA Fingerprint (SHA256 or SHA1)

String of up to 95 characters

Specifies the SHA256 or SHA1 fingerprint of the Root CA to use for validation during the SCEP process when issuing certificates
                                             for WLAN authentication. We recommend that you use the SHA256 fingerprint, which can be obtained via OpenSSL (e.g. openssl
                                             x509 -in rootca.cer -noout -sha256 -fingerprint) or using a Web Browser to inspect the certificate details.

Enter the 64 hexadecimal character value for the SHA256 fingerprint or the 40 hexadecimal character value for the SHA1 fingerprint
                                             with a common separator (colon, dash, period, space) or without a separator. If using a separator, then the separator should
                                             be consistently placed after every 2, 4, 8, 16, or 32 hexadecimal characters for a SHA256 fingerprint or every 2, 4, or 8
                                             hexadecimal characters for a SHA1 fingerprint.

Phones that do not support this feature do not display the field.

WLAN Authentication Attempts

Phones that do not support this feature do not display the field.

WLAN Profile 1 Prompt Mode

Disabled

Enabled

Disabled

Phones that do not support this feature do not display the field.

Conference with Active Call in Enhanced line mode

Disabled

Enabled

Disabled

Disabled—The calls in the Active Calls list cannot be filtered by line, and users cannot directly add another person to a
                                                   conference by simply pressing a line key. If there are quite a few calls on the phones, users have to repeatedly press the
                                                   Navigation Cluster button in the calls list to navigate to the target calls.

Enabled—Enhances the user experience to add another person to a conference call. This feature can reduce the steps to find
                                                   the target calls for the users.

If each line has only one call on the phone, users can directly press the line key to add the call on a line to the conference
                                                   call.

If each line has multiple calls on the phone, users can press a line key to only show the calls filtered by the line. Then
                                                   they can quickly navigate to the target calls that will be added to the conference call.

This feature is only available when the "Line Mode" is set to "Enhanced Line Mode".

Line Mode

Session Line Mode

Enhanced Line Mode

Session Line Mode

Controls the line display on the phone.

Session Line Mode—The buttons on one side of the screen are line keys.

Enhanced Line Mode—The buttons on both sides of the phone screen are line keys. Predictive dialing and Actionable incoming
                                                   call alerts are enabled by default in Enhanced line mode.

Admin Configurable Ringer

Disabled

Sunrise

Chirp1

Chirp2

Disabled

Works with "Allow Ringtone Change Through Phone Menu" to control the ringtone and the ability for users to set the ringtone.

If set to Disabled, the administrator's setting of the default ringtone is disabled. In this case, users can always change
                                             a ringtone on their phones no matter whether the "Allow Ringtone Change Through Phone Menu" parameter value is Disabled or
                                             Enabled.

If set to a value other than Disabled, the user's permission of changing a ringtone on the phone depends on the value of "Allow
                                             Ringtone Change Through Phone Menu":

Disabled—Users cannot change the ringtone. In this situation, the Ringtone menu item in the Settings menu is grayed out.

Enabled—Users can change the ringtone on the phone.

Allow Ringtone Change Through Phone Menu

Disabled

Enabled

Disabled

Works with "Admin Configurable Ringer" to control the ability for users to set the ringtone.

The user's choice of ringtone takes precedence over the default ringtone set the administrators. If you still want to change
                                             the ringtone, do the following:

Set the parameter to Disabled, and save to apply the change.

Change the default ringtone in "Admin Configurable Ringer", and save to apply the change. Then the ringtone on the phone will
                                                   be reset to the default ringtone.

Customer Support Use

String of up to 64 characters

Empty

For Cisco TAC use only.

Disable TLS Ciphers

See Disable Transport Layer Security Ciphers .

None

Disables the selected TLS cipher.

Disable more than one cipher suite by selecting and holding the Ctrl key on your computer keyboard.

If you select all of the phone ciphers, then phone TLS service is impacted.

Lower Your Voice Alert

Enabled

Disabled

Enabled

Controls the Lower your voice feature.

Disabled:

The phone doesn't display the Lower
                                                            												your voice menu item in the Settings menu.

Users won't see the message on their screen when
                                                         												they speak loudly.

Enabled:

Users control the feature from the Lower your voice menu item
                                                         												in the Settings menu. By
                                                         												default, the field is set to On .

Mark Call As Spam

Enabled

Disabled

Enabled

Controls the Mark call as spam feature.

Disabled:

The phone doesn't display the Mark
                                                            												spam softkey.

The Spam list item in the Settings menu doesn't
                                                         												display.

If there was a spam list, the list is cleared and
                                                         												can't be recovered.

Enabled:

The phone displays the Mark
                                                            												spam softkey.

The Spam list item in the Settings menu displays.

Dedicate one line for Call Park

Disabled

Enabled

Enabled

Controls whether a parked call occupies one line or not.

For more information, see the Cisco Unified Communications
                                             									Manager documentation.

Line Text Label Display in ELM

Disabled

Enabled

Enabled

Enabled

If the caller's name is configured, it displays the name in the first line of the call session and the local line label in
                                                         the second line.

If the caller's name is not configured, it displays the remote number in the first line and the local line label in the second
                                                         line.

Disabled

If the caller’s name is configured, it displays the name in the first line of the call session and number in the second line.

If the caller's name is not configured, it displays only the remote number.

Codec negotiation involves two steps:

The phone advertises the supported codec to the Cisco Unified Communications Manager. Not all endpoints support the same set
                                                   of codecs.

When the Cisco Unified Communications Manager gets the list of supported codecs from all phones involved in the call attempt,
                                                   it chooses a commonly supported codec based on various factors, including the region pair setting.

### Feature Configuration Best Practices

You can set up the phone features to suit your users' needs. But we have some recommendations for certain situations and deployments
                                 that might help you.

#### High Call Volume Environments

In a high call volume environment, we recommend that you set up some features in a specific way.

Field

Administration Area

Recommended Setting

Always Use Prime Line

Device Information

Off or On

For more information, see Field: Always Use Prime Line .

Actionable Incoming Call Alert

Product Specific Configuration Layout

Show for all Incoming Call

Show All Calls on Primary Line

Product Specific Configuration Layout

Enabled

Revert to All Calls

Product Specific Configuration Layout

Enabled

#### Multiline Environments

In a multiline environment, we recommend that you set up some features in a specific way.

Field

Administration Area

Recommended Setting

Always Use Prime Line

Device Information

Off

For more information, see Field: Always Use Prime Line .

Actionable Incoming Call Alert

Product Specific Configuration Layout

Show for all Incoming Call

Show All Calls on Primary Line

Product Specific Configuration Layout

Enabled

Revert to All Calls

Product Specific Configuration Layout

Enabled

#### Session Line Mode Environment

Enhanced Line Mode is the preferred tool for handling most call environments. However, if Enhanced Line Mode does not suit
                                    your needs, then you can use Session line mode.

Field

Administration Area

Recommended Setting for Session Line Mode

Show All Calls on Primary Line

Product Specific Configuration Layout

Disabled

Revert to All Calls

Product Specific Configuration Layout

Disabled

Actionable Incoming Call Alert

Product Specific Configuration Layout

Enabled by default (Firmware Release 11.5(1) and later).

#### Field: Always Use Prime Line

This field specifies whether the primary line on an IP phone is chosen when a user goes off-hook. If this parameter is set
                                    to True, when a phone goes off-hook, the primary line is chosen and becomes the active line. Even if a call rings on the second
                                    line of the user, when the phone goes off-hook, it makes only the first line active. It does not answer the inbound call on
                                    the second line. In this case, the user must choose the second line to answer the call. The default value is set to False.

The purpose of the Always Use Prime Line field is very similar to the combination of Show All Calls on the Primary Line and
                                    Revert to All Calls when both of those two features are enabled. However, the main difference is that when Always Use Prime
                                    Line is enabled, inbound calls are not answered on the second line. Only dial tone is heard on the prime line. There are certain
                                    high call volume environments where this is the desired user experience. In general, it is best to leave this field disabled
                                    except for high call volume environments that require this feature.

### Disable Transport Layer Security Ciphers

You can disable Transport Layer Security (TLS) ciphers with the Disable TLS Ciphers parameter. This allows you to tailor your security for known vulnerabilities, and to align your network with your company's
                                 policies for ciphers.

None is the default setting.

Disable more than one cipher suite by selecting and holding the Ctrl key on your computer keyboard. If you select all of the phone ciphers, then phone TLS service is impacted. Your choices are:

None

TLS_RSA_WITH_3DES_EDE_CBC_SHA

TLS_RSA_WITH_AES_128_CBC_SHA

TLS_RSA_WITH_AES_256_CBC_SHA

TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256

TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256

TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384

TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384

For more information about phone security, see Cisco IP Phone 7800 and 8800 Series Security Overview White Paper ( https://www.cisco.com/c/en/us/products/collaboration-endpoints/unified-ip-phone-8800-series/white-paper-listing.html ).

### Enable Call History for Shared Line

Allows you to view your shared line activity in the Call History. This feature:

Logs missed calls for a shared line.

Logs all answered and placed calls for a shared line.

#### Before you begin

Disable Privacy before you enable Call History for Shared Line. Otherwise Call History doesn't display the calls other users
                                 answer.

Step 1

In Cisco Unified Communications Manager Administration, select Device > Phone .

Step 2

Locate the phone to be configured.

Step 3

Navigate to the Record Call Log from Shared Line drop-down in the Product Specific Configuration area.

Step 4

Select Enabled from the drop-down list.

Step 5

Select Save .

### Schedule Power Save for Cisco IP Phone

To conserve power and ensure the longevity of the phone screen
                                 		  display, you can set the display to turn off when it is not needed.

You can configure settings in Cisco Unified Communications Manager Administration to turn off the display at a designated
                                 time on some days and all day on other days. For example, you may choose to turn off the display after business hours on weekdays
                                 and all day on Saturdays and Sundays.

You can take any of these actions to turn on the display any
                                 		  time it is off:

Press any button on the phone.

The phone takes the action designated by that button in addition
                                       				to turning on the display.

Lift the handset.

When you turn the display on, it remains on until the phone
                                 		  has remained idle for a designated length of time, then it turns off
                                 		  automatically.

For more information, see Product Specific Configuration

Step 1

In Cisco Unified Communications Manager Administration, select Device > Phone .

Step 2

Locate the phone that you need to set up.

Step 3

Navigate to the Product Specific Configuration area and set the following fields:

Days Display Not Active

Display On Time

Display On Duration

Display Idle Timeout

Field

Description

Days Display Not Active

Days that the display does not turn on automatically at the time specified in the Display On Time field.

Choose the day or days from the drop-down list. To choose more than one day, Ctrl-click each day that you want.

Display On Time

Time each day that the display turns on automatically (except on the days specified in the Days Display Not Active field).

Enter the time in this field in 24-hour format, where 0:00 is midnight.

For example, to automatically turn the display on at 07:00a.m., (0700), enter 07:00 . To turn the display on at 02:00p.m. (1400), enter 14:00 .

If this field is blank, the display will automatically turn on at 0:00.

Display On Duration

Length of time that the display remains on after turning on at the time specified in the Display On Time field.

Enter the value in this field in the format hours:minutes .

For example, to keep the display on for 4 hours and 30 minutes after it turns on automatically, enter 04:30 .

If this field is blank, the phone will turn off at the end of the day (0:00).

If Display On Time is 0:00 and the display on duration is blank (or 24:00), the display will remain on continuously.

Display Idle Timeout

Length of time that the phone is idle before the display turns off. Applies only when the display was off as scheduled and
                                                         was turned on by a user (by pressing a button on the phone or lifting the handset).

Enter the value in this field in the format hours:minutes .

For example, to turn the display off when the phone is idle for 1 hour and 30 minutes after a user turns the display on, enter 01:30 .

The default value is 01:00.

Step 4

Select Save .

Step 5

Select Apply Config .

Step 6

Restart the phone.

### Schedule EnergyWise on Cisco IP Phone

To reduce power consumption, configure the phone to
                                 		  sleep (power down) and wake (power up) if your system includes an EnergyWise
                                 		  controller.

You configure settings in Cisco Unified Communications
                                 		  Manager Administration to enable EnergyWise and configure sleep and wake times.
                                 		  These parameters are closely tied to the phone display configuration
                                 		  parameters.

When EnergyWise is enabled and a sleep time is set, the
                                 		  phone sends a request to the switch to wake it up at the configured time. The
                                 		  switch returns either an acceptance or a rejection of the request. If the
                                 		  switch rejects the request or if the switch does not reply, the phone does not
                                 		  power down. If the switch accepts the request, the idle phone goes to sleep,
                                 		  thus reducing the power consumption to a predetermined level. A phone that is not
                                 		  idle sets an idle timer and goes to sleep after the idle timer expires.

To wake up the phone, press 
                                 		  Select. At the scheduled wake time, the system
                                 		  restores power to the phone, waking it up.

For more information, see Product Specific Configuration

Step 1

From the Cisco Unified Communications Manager Administration, select Device > Phone .

Step 2

Locate the phone that you need to set up.

Step 3

Navigate to the Product Specific Configuration area and set the following fields.

Enable Power Save Plus

Phone On Time

Phone Off Time

Phone Off Idle Timeout

Enable Audible Alert

EnergyWise Domain

EnergyWise Secret

Allow EnergyWise Overrides

Enable Power Save Plus

Selects the schedule of days for which the phone powers off. Select multiple days by pressing and holding the Control key
                                                         while clicking on the days for the schedule.

By default, no days are selected.

When Enable Power Save Plus is checked, you receive a message that warns about emergency (e911) concerns.

Caution

While Power Save Plus Mode (the "Mode" ) is in effect, endpoints that are configured for the mode are disabled for emergency calling and from receiving inbound calls.
                                                                     By selecting this mode, you agree to the following: (i) You take full responsibility for providing alternate methods for emergency
                                                                     calling and receiving calls while the mode is in effect; (ii) Cisco has no liability in connection with your selection of
                                                                     the mode and all liability in connection with enabling the mode is your responsibility; and (iii) You fully inform users of
                                                                     the effects of the mode on calls, calling and otherwise.

To disable Power Save Plus, you must uncheck the Allow EnergyWise Overrides check box. If the Allow EnergyWise Overrides remains
                                                                     checked but no days are selected in the Enable Power Save Plus field, Power Save Plus is not disabled.

Phone On Time

Determines when the phone automatically turns on for the days that are in the Enable Power Save Plus field.

Enter the time in this field in 24-hour format, where 00:00 is midnight.

For example, to automatically power up the phone at 07:00 a.m. (0700), enter 07:00. To power up the phone at 02:00 p.m. (1400),
                                                         enter 14:00.

The default value is blank, which means 00:00.

The Phone On Time must be at least 20 minutes later than the Phone Off Time. For example, if the Phone Off Time is 07:00,
                                                                     the Phone On Time must be no earlier than 07:20.

Phone Off Time

The time of day that the phone powers down for the days that are selected in the Enable Power Save Plus field. If the Phone
                                                         On Time and the Phone Off Time fields contain the same value, the phone does not power down.

Enter the time in this field in 24-hour format, where 00:00 is midnight.

For example, to automatically power down the phone at 7:00 a.m. (0700), enter 7:00. To power down the phone at 2:00 p.m. (1400),
                                                         enter 14:00.

The default value is blank, which means 00:00.

The Phone On Time must be at least 20 minutes later than the Phone Off Time. For example, if the Phone Off Time is 7:00, the
                                                                     Phone On Time must be no earlier than 7:20.

Phone Off Idle Timeout

The length of time that the phone must be idle before the phone powers down.

The timeout occurs under the following conditions:

When the phone was in Power Save Plus mode, as scheduled, and was taken out of Power Save Plus mode because the phone user
                                                               pressed the Select key.

When the phone is repowered by the attached switch.

When the Phone Off Time is reached but the phone is in use.

The range of the field is 20 to 1440 minutes.

The default value is 60 minutes.

Enable Audible Alert

When enabled, instructs the phone to play an audible alert starting 10 minutes before the time that the Phone Off Time field
                                                         specifies.

The audible alert uses the phone ringtone, which briefly plays at specific times during the 10-minute alerting period. The
                                                         alerting ringtone plays at the user-designated volume level. The audible alert schedule is:

At 10 minutes before power down, play the ringtone four times.

At 7 minutes before power down, play the ringtone four times.

At 4 minutes before power down, play the ringtone four times.

At 30 seconds before power down, play the ringtone 15 times or until the phone powers off.

This check box applies only if the Enable Power Save Plus list box has one or more days selected.

EnergyWise Domain

The EnergyWise domain that the phone is in.

The maximum length of this field is 127 characters.

EnergyWise Secret

The security secret password that is used to communicate with the endpoints in the EnergyWise domain.

The maximum length of this field is 127 characters.

Allow EnergyWise Overrides

This check box determines whether you allow the EnergyWise domain controller policy to send power level updates to the phones.
                                                         The following conditions apply:

One or more days must be selected in the Enable Power Save Plus field.

The settings in Cisco Unified Communications Manager Administration take effect on schedule even if EnergyWise sends an override.

For example, assuming the Phone Off Time is set to 22:00 (10:00 p.m.), the value in the Phone On Time field is 06:00 (6:00
                                                         a.m.), and the Enable Power Save Plus has one or more days selected.

If EnergyWise directs the phone to turn off at 20:00 (8:00 p.m.), that directive remains in effect (assuming no phone user
                                                               intervention occurs) until the configured Phone On Time at 6:00 a.m.

At 6:00 a.m., the phone turns on and resumes receiving the power level changes from the settings in Unified Communications
                                                               Manager Administration.

To change the power level on the phone again, EnergyWise must reissue a new power level change command.

To disable Power Save Plus, you must uncheck the Allow EnergyWise Overrides check box. If the Allow EnergyWise Overrides remains
                                                                     checked but no days are selected in the Enable Power Save Plus field, Power Save Plus is not disabled.

Step 4

Select Save .

Step 5

Select Apply Config .

Step 6

Restart the phone.

### Set Up Do Not Disturb

When Do Not Disturb (DND) is turned on, either no audible rings occur during the ringing-in state of a call, or no audible
                                 or visual notifications of any type occur.

When Do Not Disturb (DND) is enabled, the header section of the phone screen changes color, and Do not disturb is displayed on the phone.

You can configure the phone with a phone-button template with DND as one of the selected features.

For more information, see the Do Not Disturb information in the documentation for your particular Cisco Unified Communications
                                 Manager release.

Step 1

In Cisco Unified Communications Manager Administration, select Device > Phone .

Step 2

Locate the phone to be configured.

Step 3

Set the following parameters.

Do Not
                                                   						Disturb: This check box allows you to enable DND on the phone.

DND Option: Ring Off, Call Reject, or Use Common Phone Profile Setting.

Do not choose Call Reject if you want priority (MLPP) calls to ring this phone when DND is turned on.

DND Incoming Call
                                                   						Alert: Choose the type of alert, if any, to play on a phone for incoming calls
                                                   						when DND is active.

This parameter is located on in the Common Phone Profile
                                                               						window and the Phone Configuration window. The Phone Configuration window value
                                                               						takes precedence.

Step 4

Select Save .

### Enable Agent
                           	 Greeting

The Agent Greeting
                                 		  feature allows an agent to create and update a prerecorded greeting that plays
                                 		  at the beginning of a call, such as a customer call, before the agent begins
                                 		  the conversation with the caller. The agent can prerecord a single greeting or
                                 		  multiple greetings, as needed, and create and update the greetings.

When a customer
                                 		  calls, the agent and the caller hear the prerecorded greeting. The agent can
                                 		  remain on mute until the greeting ends or the agent can answer the call over
                                 		  the greeting.

All codecs
                                 		  supported for the phone are supported for Agent Greeting calls.

For more
                                 		  information, see the barge and privacy information in the documentation for your particular Cisco Unified Communications
                                 Manager release.

Step 1

From Cisco
                                          			 Unified Communications Manager Administration, select Device > Phone .

Step 2

Locate the IP
                                          			 phone that you want to configure.

Step 3

Scroll to the
                                          			 Device Information Layout pane and set Built
                                             				In Bridge to On or Default.

Step 4

Select Save .

Step 5

Check the
                                          			 setting of the bridge:

Choose System > Service
                                                      						Parameters .

Select the
                                                				  appropriate Server and Service.

Scroll to
                                                				  the Clusterwide Parameters (Device - Phone) pane and set Builtin Bridge Enable to On.

Select Save .

### Set Up Monitoring and Recording

The Monitoring and Recording feature allows a supervisor to monitor an active call silently. Neither party on the call can
                                 hear the supervisor. The user may receive an
                                 					 audible alert during a call when it is being monitored.

When a call is secure, a lock icon displays. Callers may
                                 					 also receive an audible alert to indicate that the call is being monitored. The
                                 					 connected parties may also receive an audible alert that indicates that the call is
                                 					 secure and is being monitored.

When an active call is being monitored or recorded, the user
                                 					 can receive or place intercom calls; however, if the user places an intercom
                                 					 call, the active call is put on hold. This action causes the recording session to
                                 					 terminate and the monitoring session to suspend. To resume the monitoring
                                 					 session, the person being monitored must resume the call.

For more information, see the monitoring and recording information in the documentation for your particular Cisco Unified
                                 Communications Manager release.

The following procedure adds a user to the standard monitoring user groups.

#### Before you begin

The Cisco Unified Communications Manager must be configured to support Monitoring and Recording.

Step 1

In Cisco Unified Communications Manager Administration, select User Management > Application User .

Step 2

Check the Standard CTI Allow Call Monitoring user group and the Standard CTI Allow Call Recording user groups.

Step 3

Click Add Selected .

Step 4

Click Add to User Group .

Step 5

Add the user phones to the list of Application Users controlled devices.

Step 6

Select Save .

### Set Up Call Forward Notification

You can control the call forward settings.

Step 1

In Cisco
                                          		  Unified Communications Manager Administration, select Device > Phone .

Step 2

Locate the phone to be set up.

Step 3

Configure the Call Forward Notification fields.

Caller Name

When this check box is checked, the caller name displays in
                                                         					 the notification window.

By default, this check box is checked.

Caller Number

When this check box is checked, the caller number displays in
                                                         					 the notification window.

By default, this check box is not checked.

Redirected Number

When this check box is checked, the information about the
                                                         					 caller who last forwarded the call displays in the notification window.

Example: If Caller A calls B, but B has forwarded all calls to
                                                         					 C and C has forwarded all calls to D, the notification box that D sees
                                                         					 contains the phone information for caller C.

By default, this check box is not checked.

Dialed Number

When this check box is checked, the information about the
                                                         					 original recipient of the call displays in the notification window.

Example: If Caller A calls B, but B has forwarded all calls to
                                                         					 C and C has forwarded all calls to D, then the notification box that D sees
                                                         					 contains the phone information for caller B.

By default, this check box is checked.

Step 4

Select Save .

### Enable BLF
                           	 for Call Lists

The BLF for Call Lists field also controls the Line Status for Corporate Directory feature.

Step 1

In the Cisco
                                          			 Unified Communications Manager Administration, select System > Enterprise
                                                				  Parameters .

Step 2

For the BLF for Call Lists field, enable or disable the feature.

By default, the feature is disabled.

Parameters
                                             				that you set in the Product Specific Configuration area may also appear in the
                                             				Device Configuration window for various devices and in the Enterprise Phone
                                             				Configuration window. If you set these same parameters in these other windows
                                             				as well, the setting that takes precedence is determined in the following
                                             				order:

Device
                                                   					 Configuration window settings

Common
                                                   					 Phone Profile window settings

Enterprise
                                                   					 Phone Configuration window settings

Step 3

Select Save .

### Set Up Energy
                           	 Efficient Ethernet for Switch and PC Port

Energy Efficient Ethernet : PC Port: Provides seamless connection with personal computers. Administrator can select Enabled or Disabled options to control
                                          the function.

Energy Efficient Ethernet : Switch Port: Provides seamless connection

For more information, see Product Specific Configuration

Step 1

In Cisco Unified Communications Manager Administration, select one
                                          			 of the following windows:

Device > Phone

Device > Device
                                                         						  Settings > Common Phone Profile

System > Enterprise
                                                         						  Phone Configurations

If you configure the parameter in multiple windows, the precedence
                                             				order is:

Device > Phone

Device > Device
                                                         						  Settings > Common Phone Profile

System > Enterprise
                                                         						  Phone Configurations

Step 2

If required, locate the phone.

Step 3

Set the Energy Efficient Ethernet: PC Port and Energy Efficient Ethernet: Switch Port fields.

Energy Efficient Ethernet: PC Port

Energy Efficient Ethernet: Switch Port

Step 4

Select Save .

Step 5

Select Apply Config .

Step 6

Restart the phone.

### Set Up RTP/sRTP
                           	 Port Range

You configure the
                                 		  Real-Time Transport Protocol (RTP) and secure Real-Time Transport Protocol
                                 		  (sRTP) port values in the SIP profile. RTP and sRTP port values range from 2048
                                 		  to 65535, with a default range of 16384 to 32764. Some port values within the
                                 		  RTP and sRTP port range are designated for other phone services. You cannot
                                 		  configure these ports for RTP and sRTP.

For more
                                 		  information, see SIP Profile information in the documentation for your particular Cisco Unified Communications Manager
                                 release.

Step 1

Select Device > Device
                                                				  Settings > SIP Profile

Step 2

Choose the
                                          			 search criteria to use and click Find .

Step 3

Select the
                                          			 profile to modify.

Step 4

Set the Start
                                          			 Media Port and Stop Media Port to contain the start and end of the port range.

used for
                                                      						the Peer Firmware Sharing (PFS) feature

used for
                                                      						SIP over UDP transport

Do not configure the Stop Media Port to a value over 49150.

Step 5

Click Save .

Step 6

Click Apply
                                             				Config .

### Mobile and Remote Access
                              				Through Expressway

Mobile and Remote Access
                                    				Through Expressway (MRA) lets remote workers easily and securely connect into the corporate network without using a virtual private network (VPN)
                                 client tunnel. Expressway uses Transport Layer Security (TLS) to secure network traffic. For a phone to authenticate an Expressway
                                 certificate and establish a TLS session, a public Certificate Authority that the phone firmware trusts must sign the Expressway
                                 certificate. It is not possible to install or trust other CA certificates on phones for authenticating an Expressway certificate.

The list of CA certificates embedded in the phone firmware is available at http://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/products-technical-reference-list.html .

Mobile and Remote Access
                                    				Through Expressway (MRA)works with Cisco Expressway. You must be familiar with the Cisco Expressway documentation, including the Cisco Expressway Administrator Guide and the Cisco Expressway Basic Configuration Deployment Guide . Cisco Expressway documentation is available at http://www.cisco.com/c/en/us/support/unified-communications/expressway-series/tsd-products-support-series-home.html .

Only the IPv4 protocol is supported for Mobile and Remote Access
                                    				Through Expressway users.

Cisco Preferred Architecture for Enterprise Collaboration, Design Overview

Cisco Preferred Architecture for Enterprise Collaboration, CVD

Unified Communications Mobile and Remote Access via Cisco VCS Deployment Guide

Cisco TelePresence Video Communication Server (VCS), Configuration Guides

Mobile and Remote Access Through Cisco Expressway Deployment Guide

During the phone registration process, the phone synchronizes the displayed date and time with the Network Time Protocol
                                 (NTP) server. With MRA, the DHCP option 42 tag is used to locate the IP addresses of the NTP servers designated for time and
                                 date synchronization. If the DHCP option 42 tag is not found in the configuration information, the phone looks for the 0.tandberg.pool.ntp.org
                                 tag to identify the NTP servers.

After registration, the phone uses information from the SIP message to synchronize the displayed date and time unless an NTP
                                 server is configured in the Cisco Unified Communications Manager phone configuration.

If the phone security profile for any of your phones has TFTP Encrypted Config checked, you cannot use the phone with Mobile
                                             and Remote Access. The MRA solution does not support device interaction with Certificate Authority Proxy Function (CAPF).

Mobile and Remote Access
                                    				Through Expressway supports Enhanced line mode.

SIP OAuth mode is supported for MRA. This mode allows you to use OAuth access tokens for authentication in secure environments.

For SIP OAuth in Mobile and Remote Access (MRA) mode, use only Activation Code
                                             					Onboarding with Mobile and Remote Access when you deploy the phone. Activation
                                             					with a username and password is not supported.

SIP OAuth mode requires Expressway x14.0(1) and later, or Cisco Unified Communications Manager
                                 				14.0(1) and later.

For additional information on SIP OAuth mode see Feature Configuration Guide for Cisco
                                    					Unified Communications Manager , Release 14.0(1) or later.

#### Deployment
                              	 Scenarios

The following sections show various deployment scenarios for Mobile and Remote Access
                                       				Through Expressway .

##### On-Premises User Logs In to the Enterprise Network

After Mobile and Remote Access
                                       				Through Expressway is deployed, log in to the enterprise network when on-premises. The phone detects the network, and registers with Cisco Unified
                                    Communications Manager.

##### Off-Premises User Logs In to the Enterprise Network

When you are away from the office, the phone detects that it is in off-premises mode. The Mobile and Remote Access
                                       				Through Expressway Sign-In window appears, and you connect to the corporate network.

Note the following:

You must have a valid service domain, username, and password to connect to the network.

Reset the service mode to clear the Alternate TFTP setting before you try to access the company network. This clears the Alternate
                                          TFTP Server setting so the phone detects the off-premises network, and it stops the phone from making a VPN connection. Skip
                                          this step if a phone is being deployed for the first time.

If you have DHCP option 150 or option 66 enabled on your network router, you may not be able to sign into the corporate network.
                                          Reset your service mode to enter MRA mode.

##### Off-Premises User Logs In to the Enterprise Network with VPN

When you are off-premises, log in to the enterprise network with VPN, after deploying Mobile and Remote Access
                                       				Through Expressway .

Perform a Basic Reset to reset your phone configurations if your phone experiences an error.

You must configure the Alternate TFTP setting ( Admin settings > Network settings > IPv4 , field Alternate TFTP server 1 ).

#### Media Paths and Interactive Connectivity Establishment

You can deploy Interactive Connectivity Establishment (ICE) to improve the reliability of Mobile and Remote Access (MRA) calls
                                    that cross a firewall or Network Address Translation (NAT). ICE is an optional deployment that uses Serial Tunneling and Traversal
                                    Using Relays around NAT services to select the best media path for a call.

Secondary Turn Server and Turn Server Failover is not supported.

For more information about MRA and ICE, see System Configuration Guide for Cisco Unified Communications Manager, Release 12.0(1) or later. You can also find additional information in the Internet Engineering Task Force (IETF) Request for Comment documents:

Traversal Using Relays around NAT (TURN): Relay Extensions to Session Traversal Utilities for NAT (STUN) (RFC 5766)

Interactive Connectivity Establishment (ICE): A Protocol for Network Address Translator (NAT) Traversal for Offer/Answer Protocols (RFC 5245)

#### Phone Features Available for Mobile and Remote Access
                                 				Through Expressway

Mobile and Remote Access
                                       				Through Expressway provides secure VPN-less access to collaboration services for Cisco mobile and remote users. But to preserve network security,
                                    it limits access to some phone features.

Phone Feature

Phone Firmware Release

Abbreviated Dialing

10.3(1) and later

Answer Oldest

11.5(1)SR1 and later

Assisted Directed Call Park

10.3(1) and later

Auto Answer

11.5(1)SR1 and later

Barge and cBarge

11.5(1)SR1 and later

Busy Lamp Field (BLF)

10.3(1) and later

Busy Lamp Field (BLF) Pickup

10.3(1) and later

Busy Lamp Field (BLF) Speed Dial

10.3(1) and later

Call Back

10.3(1) and later

Call Forward

10.3(1) and later

Call Forward Notification

10.3(1) and later

Call Park

10.3(1) and later

Call Pickup

10.3(1) and later

Cisco Unified Serviceability

11.5(1)SR1 and later

Client Access License (CAL)

11.5(1)SR1 and later

Conference

10.3(1) and later

Conference List / Remove Participant

11.5(1)SR1 and later

Corporate Directory

11.5(1)SR1 and later

CTI Applications (CTI Controlled)

11.5(1)SR1 and later

Direct Transfer

10.3(1) and later

Directed Call Park

10.3(1) and later

Distinctive Ring

11.5(1)SR1 and later

Divert

10.3(1) and later

Enhanced line mode

12.1(1) and later

Divert

10.3(1) and later

Forced Access Codes and Client Matter Codes

11.5(1)SR1 and later

Group Call Pickup

10.3(1) and later

Hold/Resume

10.3(1) and later

Hold Reversion

10.3(1) and later

Immediate Divert

10.3(1) and later

Join

10.3(1) and later

Malicious Caller Identification (MCID)

11.5(1)SR1 and later

Meet Me Conference

10.3(1) and later

Message Waiting Indicator

10.3(1) and later

Mobile Connect

10.3(1) and later

Mobile Voice Access

10.3(1) and later

Multilevel Precedence and Preemption (MLPP)

11.5(1)SR1 and later

Multiline

11.5(1)SR1 and later

Music On Hold

10.3(1) and later

Mute

10.3(1) and later

Network profiles (Automatic)

11.5(1)SR1 and later

Off-hook Dialing

10.3(1) and later

On-hook Dialing

10.3(1) and later

Plus Dialing

10.3(1) and later

Privacy

11.5(1)SR1 and later

Private Line Automated Ringdown (PLAR)

11.5(1)SR1 and later

Redial

10.3(1) and later

Speed Dial (does not support a pause)

10.3(1) and later

Services URL button

11.5(1)SR1 and later

Transfer

10.3(1) and later

Uniform Resource Identifier (URI) Dialing

10.3(1) and later

#### Configure User
                              	 Credentials Persistent for Expressway Sign-In

When a user signs in to
                                    		  the network with Mobile and Remote Access
                                       				Through Expressway ,
                                    		  the user is prompted for a service domain, username, and password. If you enable
                                    		  the User Credentials Persistent for Expressway Sign-In parameter, user login credentials are stored so that they do not
                                    need to reenter this information.
                                    		  This parameter is disabled by default.

You can set up credentials to persist for a single phone, a group of phones, or all phones.

#### Generate a QR Code for MRA Sign-In

Users who have a phone with a camera can scan a QR code to sign into MRA, instead of entering the service domain and their
                                    username manually.

Step 1

Use a QR code generator to generate a QR code with either the service domain, or the service domain and username separated
                                             by a comma. For example: mra.example.com or mra.example.com,username.

Step 2

Print the QR code and provide it to the user.

### Problem Report Tool

Users submit problem reports to you with the Problem Report Tool.

The Problem Report Tool logs are required by Cisco TAC when troubleshooting problems. The logs are cleared if you restart
                                             the phone. Collect the logs before you restart the phones.

To issue
                                 		  a problem report, users access the Problem Report Tool and
                                 		  provide the date and time that the problem occurred, and a description of the problem.

If the phone is in the factory default state. The URL is active for 1 hour. After 1 hour, the user should try to submit the
                                          phone logs again.

If the phone has downloaded a configuration file and the call control system allows web access to the phone.

You must add a server address to the Customer Support Upload URL field on Cisco Unified Communications Manager.

If you are deploying devices with Mobile and Remote Access through Expressway, you must also add the PRT server address to
                                 the HTTP Server Allow list on the Expressway server.

#### Configure a Customer Support Upload URL

You must use a server with an upload script to receive PRT files. The PRT uses an HTTP POST mechanism, with the following
                                    parameters included in the upload (utilizing multipart MIME encoding):

devicename (example: "SEP001122334455" )

serialno (example: "FCH12345ABC" )

username (the username configured in Cisco Unified Communications Manager, the device owner)

prt_file (example: "probrep-20141021-162840.tar.gz" )

A sample script is
                                    		  shown below. This script is provided for reference only. Cisco does not provide
                                    		  support for the upload script installed on a customer's server.

```
<?php

// NOTE: you may need to edit your php.ini file to allow larger
// size file uploads to work.
// Modify the setting for upload_max_filesize
// I used:  upload_max_filesize = 20M

// Retrieve the name of the uploaded file 
$filename = basename($_FILES['prt_file']['name']);

// Get rid of quotes around the device name, serial number and username if they exist
$devicename = $_POST['devicename'];
$devicename = trim($devicename, "'\"");

$serialno = $_POST['serialno'];
$serialno = trim($serialno, "'\"");

$username = $_POST['username'];
$username = trim($username, "'\"");

// where to put the file
$fullfilename = "/var/prtuploads/".$filename;

// If the file upload is unsuccessful, return a 500 error and
// inform the user to try again

if(!move_uploaded_file($_FILES['prt_file']['tmp_name'], $fullfilename)) {
        header("HTTP/1.0 500 Internal Server Error");
        die("Error: You must select a file to upload.");
}

?>
```

The phones only support HTTP URLs.

Step 1

Set up a server that can run your PRT upload script.

Step 2

Write a script that can handle the parameters listed above, or edit the provided sample script to suit your needs.

Step 3

Upload your script to your server.

Step 4

In Cisco Unified Communications Manager, go to the Product Specific
                                             			 Configuration Layout area of the individual device configuration window, Common
                                             			 Phone Profile window, or Enterprise Phone Configuration window.

Step 5

Check Customer support upload URL and
                                             			 enter your upload server URL.

##### Example:

Step 6

Save your changes.

### Set the Label for a Line

You can set up a phone to display a text label instead of the directory number. Use this label to identify the line by name
                                 or function.  For example, if your user shares lines on the phone, you could identify the line with the name of the person
                                 that shares the line.

When adding a label to a key expansion module, only the first 25 characters are displayed on a line.

Step 1

In Cisco Unified Communications Manager Administration, select Device > Phone .

Step 2

Locate the phone to be configured.

Step 3

Locate the line instance and set the Line Text Label field.

Step 4

(Optional) If the label needs to be applied to other devices that share the line, check the Update Shared Device
                                          Settings check box and click Propagate Selected .

Step 5

Select Save .

### Set Up Dual Bank Information

To set up Dual Bank Information, follow these steps:

Step 1

In Cisco Unified Communications Manager Administration,
                                          			 choose Device > Device
                                                				  Defaults .

Step 2

Check the load information in the Inactive Load
                                          				Information field.

Step 3

Choose Bulk
                                                				  Administration > Import/Export > Export > Device
                                                				  Defaults , and schedule an export job.

Step 4

Download the exported tar file and untar it.

Step 5

Check the file format in the exported CSV file and verify that the
                                          			 CSV file has an Inactive Load Information column with the correct value.

The CSV file value must match the Device Default value in the
                                                         				  Cisco Unified Communications Manager Administration window.

### Park
                           	 Monitoring

Park monitoring is
                              		supported only when a Cisco IP phone parks a call. Park monitoring then
                              		monitors the status of a parked call. The park monitoring call bubble does not
                              		clear until the parked call gets retrieved or is abandoned by the parked call.
                              		This parked call can be retrieved by using the same call bubble on the phone
                              		that parked the call.

#### Set Up Park
                              	 Monitoring Timers

Cisco Unified Communications Manager Administration provides
                                    		  three cluster-wide service timer parameters for park monitoring: Park
                                    		  Monitoring Reversion Timer, Park Monitoring Periodic Reversion Timer, and Park
                                    		  Monitoring Forward No Retrieve Timer. Each service parameter includes a default
                                    		  and requires no special configuration. These timer parameters are for park
                                    		  monitoring only; the Call Park Display Timer and Call Park Reversion Timer are
                                    		  not used for park monitoring. See the following table for descriptions of these
                                    		  parameters.

Configure the timers in the Cisco Unified Communications
                                    		  Manager Service Parameters page.

Step 1

In Cisco Unified Communications Manager Administration,
                                             			 choose System > Service
                                                   				  Parameters .

Step 2

Update the Park Monitoring Reversion Timer, Park Monitoring
                                             			 Periodic Reversion Timer, and Park Monitoring Forward No Retrieve Timer fields
                                             			 in the Clusterwide Parameters (Feature-General) pane.

Field

Description

Park Monitoring Reversion Timer

Default is 60 seconds. This parameter determines the number of
                                                            					 seconds that Cisco Unified Communications Manager waits before prompting the
                                                            					 user to retrieve a call that the user parked. This timer starts when the user
                                                            					 presses Park on the phone, and a reminder is issued when the timer expires.

You can override the value that this service parameter
                                                            					 specifies on a per-line basis in the Park Monitoring section of the Directory
                                                            					 Number Configuration window (in Cisco Unified Communications Manager
                                                            					 Administration, choose Call
                                                                  						  Routing > Directory Number ).
                                                            					 Specify a value of 0 to immediately utilize the periodic reversion interval
                                                            					 that the Park Monitoring Periodic Reversion Timer service parameter specifies.
                                                            					 (See the description that follows.) For example, if this parameter is set to
                                                            					 zero and the Park Monitoring Periodic Reversion Timer is set to 15, the user is
                                                            					 immediately prompted about the parked call and every 15 seconds thereafter
                                                            					 until the Park Monitoring Forward No Retrieve Timer (see the description that
                                                            					 follows) expires.

Park Monitoring Periodic Reversion Timer

Default is 30 seconds. This parameter determines the interval
                                                            					 (in seconds) that Cisco Unified Communications Manager waits before prompting
                                                            					 the user again that a call is parked. To connect to the parked call, the user
                                                            					 can simply go off-hook during one of these prompts. Cisco Unified
                                                            					 Communications Manager continues to prompt the user about the parked call as
                                                            					 long as the call remains parked and until the time that the Park Monitoring
                                                            					 Forward No Retrieve Timer (see the description that follows) specifies expires.
                                                            					 Specify a value of 0 to disable periodic prompts about the parked call.

Park Monitoring Forward No Retrieve Timer

Default is 300 seconds. This parameter determines the number
                                                            					 of seconds that park reminder notifications occur before the parked call
                                                            					 forwards to the Park Monitoring Forward No Retrieve destination that is
                                                            					 specified in the parker Directory Number Configuration window. (If no forward
                                                            					 destination is provided in Cisco Unified Communications Manager Administration,
                                                            					 the call returns to the line that parked the call.) This parameter starts when
                                                            					 the time that the Park Monitoring Reversion Timer service parameter specifies
                                                            					 expires. When the Park Monitoring Forward No Retrieve Timer expires, the call
                                                            					 is removed from park and forwards to the specified destination or returns to
                                                            					 the parker line.

#### Set Park
                              	 Monitoring Parameters for Directory Numbers

The
                                    		  Directory Number Configuration window contains a Park Monitoring area where you
                                    		  can configure the three parameters.

Step 1

In Cisco
                                             			 Unified Communications Manager Administration, choose Call
                                                   				  Routing > Directory Number .

Step 2

Set the park
                                             			 monitoring fields as described in the following table.

Park
                                                            						  Monitoring Forward No Retrieve Destination External

When
                                                            						  the parkee is an external party, the call forwards to the specified destination
                                                            						  in the parker Park Monitoring Forward No Retrieve Destination External
                                                            						  parameter. If the Forward No Retrieve Destination External field value is
                                                            						  empty, the parkee is redirected to the parker line.

Park
                                                            						  Monitoring Forward No Retrieve Destination Internal

When
                                                            						  the parkee is an internal party, the call forwards to the specified destination
                                                            						  in the parker’s Park Monitoring Forward No Retrieve Destination Internal
                                                            						  parameter. If the Forward No Retrieve Destination Internal is empty, the parkee
                                                            						  is redirected to the parker line.

Park
                                                            						  Monitoring Reversion Timer

This
                                                            						  parameter determines the number of seconds that Cisco Unified Communications
                                                            						  Manager waits before prompting the user to retrieve a call that the user
                                                            						  parked. This timer starts when the user presses Park on the phone, and a
                                                            						  reminder is issued when the timer expires.

Default: 60 seconds

If you
                                                            						  configure a nonzero value, this value overrides the value of this parameter set
                                                            						  in the Service Parameters window. However, if you configure a value of 0 here,
                                                            						  then the value in the Service Parameters window is used.

#### Set Up Park
                              	 Monitoring for Hunt Lists

When a
                                    		  call that was routed via the hunt list is parked, the Hunt Pilot Park
                                    		  Monitoring Forward No Retrieve Destination parameter value is used (unless it
                                    		  is blank) when the Park Monitoring Forward No Retrieve Timer expires.

Step 1

In Cisco
                                             			 Unified Communications Manager Administration, choose Call
                                                   				  Routing > Route/Hunt > Hunt
                                                   				  Pilot .

Step 2

Set the Hunt
                                             			 Pilot Park Monitoring Forward No Retrieve Destination parameter.

If the Hunt
                                                				Pilot Park Monitoring Forward No Retrieve Destination parameter value is blank,
                                                				the call forwards to the destination that is configured in the Directory Number
                                                				Configuration window when the Park Monitoring Forward No Retrieve Timer
                                                				expires.

### Set Up the Audio and Video Port Range

Audio and video traffic can be sent to different RTP port ranges in order to improve Quality of Service (QoS).

The following fields control the port ranges in the Cisco Unified Communications Manager Administration:

Audio ports

Start Media Port (default: 16384)

Stop Media Port (default: 32766)

Video ports

Minimum: 2048

Maximum: 65535

Stop Video (This is to set the video stop port)

Minimum: 2048

Maximum: 65535

The following rules apply when configuring the video port fields:

After the Start Video RTP Port and Stop Video RTP Port  are configured, the phone uses ports within the video port range for
                                 video traffic. The audio traffic uses the media ports.

If the audio and video port ranges overlap, the overlapped ports carry both audio and video traffic. If the video port range
                                 is not configured correctly, the phone uses the configured audio ports for both audio and video traffic.

For more information, see the documentation for your particular Cisco Unified Communications Manager release.

Step 1

In Cisco Unified Communications Manager Administration, select Device > Device Settings > SIP Profile

Step 2

Set the Start Media Port and  Stop Media Port fields for the audio port range.

Step 3

Select Save .

Step 4

Select one of the following windows:

System > Enterprise Phone Configuration

Device > Device Settings > Common Phone Profile

Device > Phone > Phone Configuration

Step 5

Set the Start Video RTP Port and Stop Video RTP Port fields for the range of ports required.

The following rules apply when configuring the video port fields:

The value in the Stop Video RTP Port field must be larger than the value in the Start Video RTP Port field.

The difference between the Start Video RTP Port field and the Stop Video RTP Port field must be at least 16.

Step 6

Select Save .

### Set up Cisco IP Manager Assistant

Cisco IP Manager Assistant (IPMA) provides call routing and other call
                                 		  management features to help managers and assistants handle phone calls more
                                 		  effectively.

IPMA services must be configured in Cisco Unified Communications
                                 		  Manager before you can access them. For detailed information on configuring
                                 		  IPMA, see the Feature Configuration Guide for Cisco Unified Communications
                                    Manager .

A manager has calls intercepted by
                                          				  the call routing service.

An assistant handles calls on behalf of a
                                          				  manager.

The assistant console is a desktop application assistants can use to perform tasks and manage most features.

IPMA supports two modes of operation: proxy line support and shared
                                 		  line support. Both modes support multiple calls per line for the manager. The
                                 		  IPMA service supports both proxy line and shared line support in a cluster.

In shared-line mode, the manager and assistant share a directory
                                 		  number and calls are handled on the shared line. Both the manager phone and the
                                 		  assistant phone ring when a call is received on the shared line. Shared-line
                                 		  mode does not support default assistant selection, assistant watch, call
                                 		  filtering or divert all calls.

If you configure Cisco IPMA in shared-line mode, the manager and
                                 		  assistant share a directory number; for example, 1701. The assistant handles
                                 		  calls for a manager on the shared directory number. When a manager receives a
                                 		  call on directory number 1701, both the manager phone and the assistant phone
                                 		  rings.

Not all IPMA features are available in shared-line mode including
                                 		  default assistant selection, assistant watch, call filtering, and divert all
                                 		  calls. An assistant cannot see or access these features on the Assistant
                                 		  Console application. The assistant phone does not have the softkey for the
                                 		  Divert All feature. The manager phone does not have the softkeys for Assistant
                                 		  Watch, Call Intercept, or Divert All feature.

In order to access shared-line support on user devices, you must first
                                 		  use Cisco Unified Communications Manager Administration to configure and start
                                 		  the Cisco IP Manager Assistant service.

In proxy-line mode, the assistant handles calls on behalf of a manager
                                 		  using a proxy number. Proxy-line mode supports all IPMA features.

When you configure Cisco IPMA in proxy-line mode, the manager and
                                 		  assistant do not share a directory number. The assistant handles calls for a
                                 		  manager using a proxy number. The proxy number is not the directory number for
                                 		  the manager. It is an alternate number chosen by the system and is used by an assistant to handle manager calls. In proxy-line
                                 mode, a manager and an assistant
                                 		  have access to all features that are available in IPMA, which include default
                                 		  assistant selection, assistant watch, call filtering, and divert all.

In order to access proxy-line support on user devices, you must first
                                 		  use Cisco Unified Communications Manager Administration to configure and start
                                 		  the Cisco IP Manager Assistant service.

Supports manager for proxy mode.

Supports manager for shared mode.

Supports assistant in proxy or in shared mode.

The following table describes the softkeys available in the softkey
                                 		  templates.

Intercept, Set Watch, and Divert All should only be configured for a
                                             			 manager phone in proxy line mode.

The following procedure is an overview of the steps required.

Step 1

Configure the phones and
                                          			 users.

Step 2

Associate the phones to the users.

Step 3

Activate the Cisco IP Manager Assistant service in the Service
                                          			 Activation window.

Step 4

Configure system administration parameters.

Step 5

If required, configure IPMA clusterwide services parameters.

Step 6

(Optional) Configure the user CAPF profile

Step 7

(Optional) Configure the IPMA service parameters for security

Step 8

Stop and restart the IPMA service.

Step 9

Configure phone parameter, manager, and assistant settings,
                                          			 including the softkey templates.

Step 10

Configure Cisco Unified Communications Manager Assistant
                                          			 application.

Step 11

Configure dial rules.

Step 12

Install the Assistant Console application.

Step 13

Configure the manager and assistant console applications.

### Set up Visual
                           	 Voicemail

For
                                                				configuration information, see the Cisco Visual Voicemail documentation at http://www.cisco.com/c/en/us/support/unified-communications/visual-voicemail/model.html .

The Visual Voicemail client is not supported as a midlet on any of the  Cisco IP Phone 8800 phones.

Step 1

In Cisco
                                          			 Unified Communications Manager Administration, choose Device > Device
                                                				  Settings > Phone Services .

Step 2

Select Add
                                             				New to create a new service for Visual Voicemail.

Step 3

In the IP
                                          			 Phone Service Configuration window, enter the following information in their
                                          			 respective fields:

- Service Name—Enter VisualVoiceMail .

- ASCII Service Name—Enter VisualVoiceMail .

- Service URL—Enter as Application:Cisco/VisualVoiceMail .

- Service Category—Select XML Service from the pulldown menu.

- Service Type—Select Messages from the pulldown menu.

Step 4

Check Enable and click Save .

Ensure that
                                                         				  you do not check Enterprise Subscription .

Step 5

In the Service
                                          			 Parameter Information window, click New
                                             				Parameter and enter the following information in their respective
                                          			 fields:

- Parameter Name. Enter
                                                				  voicemail_server.

- Parameter Display Name.
                                                				  Enter voicemail_server.

- Default Value. Enter the
                                                				  hostname of the primary Unity Server.

- Parameter Description

Step 6

Check Parameter is Required and click Save .

Ensure that
                                                         				  you do not check Parameter is a Password (mask contents) .

Step 7

Close the
                                          			 window and select Save again in the Phone Service Configuration
                                          			 window.

#### Set Up Visual
                              	 Voicemail for a Specific User

For
                                                   				configuration information, see the Cisco Visual Voice Mail documentation at http://www.cisco.com/c/en/us/support/unified-communications/visual-voicemail/model.html .

Step 1

In Cisco
                                             			 Unified Communications Manager Administration, choose Device > Phone .

Step 2

Select the
                                             			 device associated to the user you are searching for.

Step 3

In the
                                             			 Related Links drop-down, choose Subscribe/Unsubscribe Services and click Go .

Step 4

Select the
                                             			 VisualVoiceMail Service you created, then choose Next > Subscribe .

#### Visual Voicemail
                              	 Setup for a User Group

To add a batch of Cisco IP
                                 		phones to Cisco Unified Communications Manager with Visual Voicemail
                                 		subscribed, create a phone template in BAT tool for each phone type and in each
                                 		phone template. You can then subscribe to the Visual Voicemail service, and use
                                 		the template to insert the phones.

If you already have your
                                 		Cisco IP phones registered and want to get phones subscribed to the Visual
                                 		Voicemail service, create a phone template in BAT, subscribe to the Visual
                                 		Voicemail service in the template, and then use BAT tool to update phones.

For more
                                 		information, see http://www.cisco.com/c/en/us/support/unified-communications/visual-voicemail/model.html .

### Assured Services SIP

Assured Services SIP(AS-SIP) is a collection of features and protocols that offer a highly secure call flow for Cisco IP Phones
                                 and third-party phones. The following features are collectively known as AS-SIP:

Multilevel Precedence and Preemption (MLPP)

Differentiated Services Code Point (DSCP)

Transport Layer Security (TLS) and Secure Real-time Transport Protocol (SRTP)

Internet Protocol version 6 (IPv6)

AS-SIP is often used with Multilevel Precedence and Preemption (MLPP) to prioritize calls during an emergency. With MLPP,
                                 you assign a priority level to your outgoing calls, from level 1 (low) to level 5 (high). When you receive a call, a precedence
                                 level icon displays on the phone that shows the call priority.

To configure AS-SIP, complete the following tasks on Cisco Unified Communications Manager:

Configure a Digest User—Configure the end user to use digest authentication for SIP requests.

Configure SIP Phone Secure Port—Cisco Unified Communications Manager uses this port to listen to SIP phones for SIP line registrations
                                       over TLS.

Restart Services—After configuring the secure port, restart the Cisco Unified Communications Manager and Cisco CTL Provider
                                       services. Configure SIP Profile for AS-SIP-Configure a SIP profile with SIP settings for your AS-SIP endpoints and for your
                                       SIP trunks. The phone-specific parameters are not downloaded to a third-party AS-SIP phone. They are used only by Cisco Unified
                                       Manager. Third-party phones must locally configure the same settings.

Configure Phone Security Profile for AS-SIP—You can use the phone security profile to assign security settings such as TLS,
                                       SRTP, and digest authentication.

Configure AS-SIP Endpoint—Configure a Cisco IP Phone or a third-party endpoint with AS-SIP support.

Associate Device with End Use—Associate the endpoint with a user.

Configure SIP Trunk Security Profile for AS-SIP—You can use the sip trunk security profile to assign security features such
                                       as TLS or digest authentication to a SIP trunk.

Configure SIP Trunk for AS-SIP—Configure a SIP trunk with AS-SIP support.

Configure AS-SIP Features—Configure additional AS-SIP features such as MLPP, TLS, V.150, and IPv6.

For detailed information about configuring AS-SIP, see the "Configure AS-SIP Endpoints" chapter, System Configuration Guide for Cisco Unified Communications Manager .

### Migration of your Phone to a Multiplatform Phone Directly

You can migrate your enterprise phone to a multiplatform phone easily in one step without using transition firmware load.
                                 All you need is to obtain and authorize the migration license from the server.

For more information, see https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/MPP-conversion/enterprise-to-mpp/cuip_b_conversion-guide-ipphone.html

### Multilevel Precedence and Preemption

Multilevel Precedence and Preemption (MLPP) allows you to prioritize calls during emergencies or other crisis situations.
                                 You assign a priority to your outgoing calls that range from 1 to 5. Incoming calls display an icon that shows the call priority.
                                 Authenticated users can preempt calls either to targeted stations or through fully subscribed TDM trunks.

This capability assures high-ranking personnel of communication to critical organizations and personnel.

MLPP is often used with Assured Services SIP(AS-SIP). For detailed information about configuring MLPP, see the "Configure
                                 Multilevel Precedence and Preemption" chapter, System Configuration Guide for Cisco Unified Communications Manager .

## Set Up Softkey
                        	 Template

Using Cisco
                              		  Unified Communications Manager Administration, you can associate a maximum of
                              		  18 softkeys with applications that are supported by the phone. Cisco Unified
                              		  Communications Manager supports the Standard User and Standard Feature softkey
                              		  template.

An application
                              		  that supports softkeys has one or more standard softkey templates associated
                              		  with it. You modify a standard softkey template by copying it, renaming it, and
                              		  then updating the new template. You can also modify a nonstandard softkey
                              		  template.

The Softkey
                              		  Control parameter shows if softkeys of a phone are controlled by the Softkey Template feature. The Softkey Control parameter
                              		  is a required field.

For more
                              		  information about configuring this feature, see the documentation for your particular Cisco Unified Communications Manager
                              release.

The
                              		  Cisco IP Phones do not support all the softkeys that are configurable
                              		  in Softkey Template Configuration on Cisco Unified Communications Manager
                              		  Administration. Cisco Unified Communications Manager allows you to enable or
                              		  disable some softkeys in the control policy configuration settings. The
                              		  following table lists the features and the softkeys that can be configured on a
                              		  softkey template, and identifies whether it is supported on the Cisco IP Phones.

Cisco Unified
                                          			 Communications Manager allows you to configure any softkey in a softkey
                                          			 template, but unsupported softkeys do not display on the phone.

Feature

Configurable Softkeys in the Softkey Template configuration

Supported
                                          					 as a Softkey

Notes

Answer

Answer
                                          					 (Answer)

Supported

—

Call Back

Call Back
                                          					 (CallBack)

Supported

—

Call
                                          					 Forward All

Forward
                                          					 All (cfwdAll)

Supported

Phone
                                          					 displays Forward all or Forward off.

Call Park

Call Park
                                          					 (Park)

Supported

—

Call
                                          					 Pickup

Pick Up
                                          					 (Pickup)

Supported

—

Barge

Barge

Supported

Barge uses the built-in conference bridge

cBarge

Conference
                                          					 Barge

Supported

cBarge uses the Cisco Unified Communications Manager conference bridge. The softkey label is Barge.

Conference

Conference
                                          					 (Confrn)

Supported

Conference
                                          					 is a dedicated button.

Conference
                                          					 List

Conference
                                          					 List (ConfList)

Supported

Phone
                                          					 displays Show detail.

Divert

Immediate Divert (iDivert)

Supported

Phone
                                          					 displays Decline.

Do Not
                                          					 Disturb

Toggle
                                          					 Do Not Disturb (DND)

Supported

Configure Do Not Disturb as a programmable line button or as a
                                          					 softkey.

End Call

End Call
                                          					 (EndCall)

Supported

—

Group
                                          					 Pickup

Group
                                          					 Pick UP (GPickUp)

Supported

—

Hold

Hold
                                          					 (Hold)

Supported

Hold is
                                          					 a dedicated button.

Hunt
                                          					 Group

HLog
                                          					 (HLog)

Supported

Configure Hunt Group as a programmable feature button.

Join

Join
                                          					 (Join)

Not supported

—

Malicious Call Identification

Toggle
                                          					 Malicious Call Identification (MCID)

Supported

Configure Malicious Call Identification as a programmable
                                          					 feature button or as a softkey.

Meet Me

Meet Me
                                          					 (MeetMe)

Supported

—

Mobile
                                          					 Connect

Mobility
                                          					 (Mobility)

Supported

Configure Mobile Connect as a softkey.

New Call

New Call
                                          					 (NewCall)

Supported

—

Other
                                          					 Pickup

Other
                                          					 Pickup (oPickup)

Supported

—

PLK
                                          					 Support for Queue Statistics

Queue
                                          					 Status

Not supported

—

Quality
                                          					 Reporting Tool

Quality
                                          					 Reporting Tool (QRT)

Supported

Configure Quality Reporting Tool as a programmable feature
                                          					 button or as a softkey.

Redial

Redial
                                          					 (Redial)

Supported

—

Remove
                                          					 Last Conference Participant

Remove
                                          					 Last Conference Participant (Remove)

Not supported

—

Resume

Resume
                                          					 (Resume)

Supported

—

Select

Select
                                          					 (Select)

Not supported

—

Speed
                                          					 Dial

Abbreviated Dial (AbbrDial)

Supported

Phone
                                          					 displays SpeedDial.

Transfer

Transfer
                                          					 (Trfr)

Supported

Transfer
                                          					 is a dedicated button.

Video
                                          					 Mode Command

Video
                                          					 Mode Command (VidMode)

Not supported

—

Step 1

In Cisco
                                       			 Unified Communications Manager Administration, select one of the following windows:

To configure
                                                			 softkey templates, select Device > Device
                                                      				  Settings > SoftkeyTemplate .

To assign a
                                                			 softkey template to a phone, select Device > Phone and configure the Softkey
                                                			 Template field.

Step 2

Save the changes.

## Phone Button Templates

Phone button templates let you assign speed dials and call-handling features to programmable buttons. Call-handling features
                           that can be assigned to buttons include Answer, Mobility, and All Calls.

Ideally, you modify templates before you register phones on the network. In this way, you can access customized phone button
                           template options from Cisco Unified Communications Manager during registration.

### Modify Phone Button Template

For more  information about IP Phone services and configuring line buttons, see  the documentation for your particular Cisco
                                 Unified Communications Manager release.

Step 1

From Cisco Unified Communications Manager Administration, choose Device > Device
                                                				  Settings > Phone Button Template .

Step 2

Click Find .

Step 3

Select the phone model.

Step 4

Select Copy , enter a name for the new template, and
                                          			 then select Save .

The Phone Button Template Configuration window opens.

Step 5

Identify the button that you would like to assign, and select Service URL from the Features drop-down list that associates with the line.

Step 6

Select Save to create a new phone button template
                                          			 that uses the service URL.

Step 7

Choose Device > Phone and open the Phone Configuration window for the phone.

Step 8

Select the new phone button template from the Phone Button
                                          			 Template drop-down list.

Step 9

Select Save to store the change and then select Apply Config to implement the change.

The phone user can now access the  Self Care Portal and
                                             				associate the service with a button on the phone.

### Assign Phone
                           	 Button Template for All Calls

Assign
                                 		  an All Calls button in the phone template for users with multiple shared lines.

When you configure
                                 		  an All Calls button on the phone, users use the All Calls button to:

See a
                                       				consolidated list of current calls from all lines on the phone.

See (under
                                       				Call History) a list of all missed calls from all lines on the phone.

Place a call
                                       				on the user's primary line when the user goes off-hook. All Calls automatically
                                       				defaults to the user primary line for any outgoing call.

Step 1

Modify the
                                          			 phone button template to include the All Calls button.

Step 2

Assign the
                                          			 template to the phone.

### Set Up PAB or Speed Dial as IP Phone Service

You can modify a phone button template to associate a service URL with a programmable button. Doing so provides users with
                                 single-button access to the PAB and Speed Dials. Before you modify the phone button template, you must configure PAB or Speed
                                 Dials as an IP Phone service.   For more information, see the documentation for your particular Cisco Unified Communications
                                 Manager release.

To configure PAB or Speed Dial as an IP Phone service (if it
                                 		  is not already a service), follow these steps:

Step 1

From Cisco Unified Communications Manager Administration, choose Device > Device
                                                				  Settings > Phone Services .

The Find and List IP Phone Services window displays.

Step 2

Click Add New .

The IP Phone Services Configuration window displays.

Step 3

Enter the following settings:

Service Name: Enter Personal Address Book .

Service Description: Enter an optional description of the
                                                   					 service.

Service URL

For PAB, enter the following URL:

http ://<Unified
                                                   						CM-server-name> :8080/ccmpd/login.do?name=#DEVICENAME#&service=pab

For Fast Dial, enter the following URL:

http ://<Unified-CM-server-name> :8080/ccmpd/login.do?name=#DEVICENAME#&service=fd

Secure Service URL

For PAB, enter the following URL:

https ://<Unified
                                                   						CM-server-name> :8443/ccmpd/login.do?name=#DEVICENAME#&service=pab

For Fast Dial, enter the following URL:

https ://<Unified-CM-server-name> :8443/ccmpd/login.do?name=#DEVICENAME#&service=fd

Service Category: Select XML Service .

Service Type: Select Directories .

Enable: Select the check box.

http://<IP_address> or https://<IP_address> (Depends on the protocol that the Cisco IP Phone supports.)

Step 4

Select Save .

If you change the service URL, remove an IP Phone service
                                                         				  parameter, or change the name of a phone service parameter for a phone service
                                                         				  to which users are subscribed, you must click Update Subscriptions to update all
                                                         				  currently subscribed users with the changes; otherwise, users must resubscribe to the
                                                         				  service to rebuild the correct URL.

### Modify Phone Button Template for PAB or Fast Dial

You can modify a phone button template to associate a service URL with a programmable button. Doing so provides users with
                                 single-button access to the PAB and Speed Dials. Before you modify the phone button template, you must configure PAB or Speed
                                 Dials as an IP Phone service.

For more  information about IP Phone services and configuring line buttons, see the documentation for your particular Cisco
                                 Unified Communications Manager release.

Step 1

From Cisco Unified Communications Manager Administration, choose Device > Device
                                                				  Settings > Phone Button Template .

Step 2

Click Find .

Step 3

Select the phone model.

Step 4

Select Copy , enter a name for the new template, and
                                          			 then select Save .

The Phone Button Template Configuration window opens.

Step 5

Identify the button that you would like to assign, and select Service URL from the Features drop-down list that associates with the line.

Step 6

Select Save to create a new phone button template
                                          			 that uses the service URL.

Step 7

Choose Device > Phone and open the Phone Configuration window for the phone.

Step 8

Select the new phone button template from the Phone Button
                                          			 Template drop-down list.

Step 9

Select Save to store the change and then select Apply Config to implement the change.

The phone user can now access the Self Care Portal and
                                             				associate the service with a button on the phone.

## VPN Configuration

A phone is located outside a trusted network

Network traffic between the phone and Cisco Unified Communications Manager crosses an untrusted network

Digital certificates

Passwords

Username and password

To configure any of the VPN features, provision the device on-premises first and then you can deploy the device off-premise.

For more information about certification authentication and working with VPN network, see the Technical Note AnyConnect VPN Phone with Certificate Authentication on an ASA Configuration Example . The URL for this document is http://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/115785-anyconnect-vpn-00.html .

With a password, or username and password approach a user is prompted for sign-in credentials. Set the user sign-in credentials
                              in accordance with your company security policy. You can also configure the Enable Password Persistence setting so that the
                              user password is saved on the phone. The user password is saved until either a failed log-in attempt occurs, a user manually
                              clears the password, or the phone resets or loses power.

Another useful tool is the Enable Auto Network Detection setting. When you enable this check box, the VPN client can only
                              run when it detects that it is outside the corporate network. This setting is disabled by default.

Your Cisco phone supports Cisco SVC IPPhone Client v1.0 as the client type.

For additional information about maintaining, configuring, and operating a virtual private network with a VPN, see Security Guide for Cisco Unified Communications Manager , "Virtual Private Network Setup" chapter. The URL for this document is http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

The Cisco VPN feature uses Secure Sockets Layer (SSL) to preserve network security.

Enter the Alternate TFTP server setting when you're configuring an off-premises phone for SSL VPN to ASA using a built-in
                                          client.

## Set Up Additional Line Keys

### Before you begin

Step 1

In Cisco Unified Communications Manager Administration, select Device > Phone .

Step 2

Locate the phone that you need to set up.

Step 3

Navigate to the Product Specific Configuration area and set the Line Mode field to Enhanced Line Mode .

Step 4

Navigate to the Device Information  area and set the Phone Button Template field to a customized template.

Step 5

Select Apply Config .

Step 6

Select Save .

Step 7

Restart the phone.

### Features Available in Enhanced Line Mode

Enhanced line mode (ELM) can be used with Mobile and Remote Access
                                    				Through Expressway .

ELM can also be used with a rollover line, a call routing configuration in which calls are forwarded to another shared line
                                 if the initial shared line is busy. When ELM is used with a rollover line, recent calls to shared lines are consolidated under
                                 a single directory number. For more information about rollover lines, see Feature Configuration Guide for Cisco Unified Communications Manager for Cisco Unified Communications Manager 12.0(1) or later.

ELM supports most but not all features. Enabling a feature does not imply support. Read the following table to confirm that
                                 a feature is supported.

Feature

Supported

Firmware Release

Answer

Yes

11.5(1) and later

Automatically Answer Calls

Yes

11.5(1) and later

Barge/cBarge

Yes

11.5(1) and later

Directed Call Park with BLF

Yes

12.0(1) and later

Bluetooth Smartphone integration

No

-

Bluetooth USB Headsets

Yes

11.5(1) and later

Call Back

Yes

11.5(1) and later

Call Chaperone

No

-

Call Forward All

Yes

11.5(1) and later

Call Park

Yes

12.0(1) and later

Call Park Line Status

Yes

12.0(1) and later

Call Pickup

Yes

11.5(1) and later

Call Pickup Line Status

Yes

11.5(1) and later

Call Forward All on Multiple Lines

Yes

11.5(1) and later

Cisco Extension Mobility Cross Cluster

Yes

12.0(1) and later supports this feature.

Cisco IP Manager Assistant (IPMA)

No

-

Cisco Unified Communications Manager Express

No

-

Conference

Yes

11.5(1) and later

Computer Telephony Integration (CTI) applications

Yes

11.5(1) and later

Decline

Yes

11.5(1) and later

Device Invoked Recording

Yes

11.5(1)SR1 and later

Do Not Disturb

Yes

11.5(1) and later

Enhanced SRST

No

-

Extension Mobility

Yes

11.5(1) and later

Group Pickup

Yes

12.0(1) and later supports this feature.

Hold

Yes

11.5(1) and later

Hunt Groups

Yes.

12.0(1) and later

Incoming Call Alert with configurable timer

No

-

Intercom

Yes

11.5(1) and later

Key Expansion Module

Cisco IP Phone 8851/8861 Key Expansion Module and Cisco IP Phone 8865 Key Expansion Module support Enhanced Line Mode

12.0(1) and later

Malicious Call Identification (MCID)

Yes

11.5(1) and later

Meet Me

Yes

11.5(1) and later

Mobile Connect

Yes

11.5(1) and later

Multilevel Precedence and Preemption

No

-

Mute

Yes

11.5(1) and later

Other PickUp

Yes

12.0(1) and later

Programmable Line Key (PLK) Support for Queue Status

Yes

11.5(1) and later

Privacy

Yes

11.5(1) and later

Queue Status

Yes

11.5(1) and later

Quality Reporting Tool (QRT)

Yes

11.5(1) and later

Right to Left locale support

No

-

Redial

Yes

11.5(1) and later

Silent Monitoring and Recording

Yes

11.5(1)SR1 and later

Speed Dial

Yes

11.5(1) and later

Survivable Remote Site Telephony (SRST)

Yes

11.5(1) and later

Transfer

Yes

11.5(1) and later

Uniform Resource Identifier (URI) Dialing

Yes

11.5(1) and later

Video Calls

Yes

11.5(1) and later

Visual Voicemail

Yes

11.5(1) and later

Voicemail

Yes

11.5(1) and later

## Set Up TLS
                        	 Resumption Timer

TLS Session
                              		  resumption enables a TLS session to resume without repeating the entire TLS
                              		  authentication process. It can significantly reduce the time taken for TLS
                              		  connection to exchange data.

TLS session
                                       				for SIP signaling: supports resumption

HTTPs client:
                                       				supports resumption

CAPF: supports
                                       				resumption

TVS: supports
                                       				resumption

EAP-TLS: does
                                       				not support resumption

EAP-FAST: does
                                       				not support resumption

VPN client:
                                       				does not support resumption

For more information, see the documentation for your particular Cisco Unified Communications Manager release.

Step 1

In Cisco
                                       			 Unified Communications Manager Administration, select Device > Phone .

Step 2

Set the TLS
                                       			 Resumption Timer parameter.

## Enable Intelligent
                        	 Proximity

Intelligent Proximity
                              		  enables users to take advantage of the acoustic properties of the phone with
                              		  their mobile device or tablet. The user pairs the mobile device or tablet to
                              		  the phone using Bluetooth.

With a mobile device
                              		  paired, the user can place and receive mobile calls on the phone. With a
                              		  tablet, the user can route the audio from the tablet to the phone.

Users can pair multiple
                              		  mobile devices , tablets, and a
                              		  Bluetooth headset to the phone. However, only one device and one headset can be
                              		  connected at the same time.

Step 1

In Cisco
                                       			 Unified Communications Manager Administration, select Phone > Device .

Step 2

Locate the
                                       			 phone you want to modify.

Step 3

Locate the
                                       			 Bluetooth field and set the field to Enabled .

Step 4

Locate the
                                       			 Allow Bluetooth Mobile Handsfree Mode field, and set the field to Enabled .

Step 5

Save the
                                       			 changes and apply them to the phone.

## Video Transmit
                        	 Resolution Setup

Cisco IP Phone 8845, 8865, and 8865NR supports the following video formats:

720p (1280x720)

WVGA(800x480)

360p (640x360)

240p (432x240)

VGA (640x480)

CIF (352x288)

SIF (352x240)

QCIF (176x144)

Cisco IP Phones with video capacity negotiate best resolution for bandwidth based on phone configures or resolution limitations.
                              Example: On a direct 88x5 to 88x5 call, the phones do not send true 720p, they send 800x480. This limitation is purely due
                              to the 5-inch WVGA screen resolution on the 88x5 being 800 x 480.

Video type

Video resolution

Frames per second (fps)

Video bit rate range

720p

1280 x 720

30

1360–2500 kbps

720p

1280 x 720

15

790–1359 kbps

WVGA

800 x 480

30

660–789 kbps

WVGA

800 x 480

15

350–399 kbps

360p

640 x 360

30

400–659 kbps

360p

640 x 360

15

210–349kbps

240p

432 x 240

30

180–209kbps

240p

432 x 240

15

64–179kbps

VGA

640 x 480

30

520–1500kbps

VGA

640 x 480

15

280–519kbps

CIF

352 x 288

30

200–279 kbps

CIF

352 x 288

15

120–199 kbps

SIF

352 x 240

30

200–279 kbps

SIF

352 x 240

15

120–199 kbps

QCIF

176 x 144

30

94–119 kbps

QCIF

176 x 144

15

64–93 kbps

## Headset Management on Older Versions of Cisco Unified Communications Manager

If you have a version of Cisco Unified Communications Manager older than 12.5(1)SU1, you can remotely configure your Cisco
                              headset settings for use with on-premises phones.

Remote headset configuration on Cisco Unified Communication Manager version 10.5(2), 11.0(1), 11.5(1), 12.0(1), and 12.5(1)
                              requires you to download a file from the Cisco Software Download website, edit the file, and then upload the file on the Cisco Unified Communications Manager TFTP server. The file is a JavaScript
                              Object Notification (JSON) file. The updated headset configuration is applied to the enterprise headsets over a 10 to 30-minute
                              time frame to prevent a traffic backlog on the TFTP server.

You can manage and configure headsets through Cisco Unified Communications Manager Administration version 11.5(1)SU7.

Note the following as you work with the JSON file:

The settings aren't applied if you are missing a bracket or brackets in the code. Use an online tool such as JSON Formatter
                                    and check the format.

Set the updatedTime setting to the current epoch time or the configuration is not applied. Alternatively, you can increase the updatedTime value by +1 to make it larger than the previous version.

Do not change the parameter name or the setting will not be applied.

For more information on the TFTP service, see the "Manage Device Firmware" chapter of the Administration Guide for Cisco Unified Communications Manager and IM and Presence Service .

Upgrade your phones to the latest firmware release before you apply the defaultheadsetconfig.json file. The following table describes the default settings you can adjust with the JSON file.

### Download the Default Headset Configuration File

Before configuring the headset parameters remotely, you must download the latest JavaScript Object Notation (JSON) sample
                                 file.

Step 1

Go to the following URL: https://software.cisco.com/download/home/286320550 .

Step 2

Choose Headsets 500 Series .

Step 3

Select your headset series.

Step 4

Choose a release folder and select the zip file.

Step 5

Click the Download or Add to cart button, and follow the prompts.

Step 6

Unzip the file to a directory on your PC.

#### What to do next

### Modify the Default Headset Configuration File

The settings aren't applied if you are missing a bracket or brackets in the code. Use an online tool such as JSON Formatter
                                       and check the format.

Set the " updatedTime " setting to the current epoch time or the configuration is not applied.

Confirm that firmwareName is LATEST or the configurations will not be applied.

Do not change a parameter name or the setting will not be applied.

Step 1

Open the defaultheadsetconfig.json file with a text editor.

Step 2

Edit the updatedTime and the headset parameter values you wish to modify.

A sample script is shown below. This script is provided for reference only. Use it as a guide as you configure your headset
                                             parameters. Use the JSON file that was included with your firmware load.

```
{
  "headsetConfig": {
    "templateConfiguration": {
      "configTemplateVersion": "1", "updatedTime" : 1537299896,
      "reportId": 3,
      "modelSpecificSettings": [
        {
          "modelSeries": "530",
          "models": [
            "520",
            "521",
            "522",
            "530",
            "531",
            "532"
          ],
          "modelFirmware": [
            {
              "firmwareName": "LATEST",
              "latest": true,
              "firmwareParams": [
                {
                  "name": "Speaker Volume",
                  "access": "Both",
                  "usageId": 32, "value" : 7
                },
                {
                  "name": "Microphone Gain",
                  "access": "Both",
                  "usageId": 33, "value" : 2
                },
                {
                  "name": "Sidetone",
                  "access": "Both",
                  "usageId": 34, "value" : 1
                },
                {
                  "name": "Equalizer",
                  "access": "Both",
                  "usageId": 35, "value" : 3
                }
              ]
            }
          ]
        },
        {
          "modelSeries": "560",
          "models": [
            "560",
            "561",
            "562"
          ],
          "modelFirmware": [
            {
              "firmwareName": "LATEST",
              "latest": true,
              "firmwareParams": [
                {
                  "name": "Speaker Volume",
                  "access": "Both",
                  "usageId": 32, "value" : 7
                },
                {
                  "name": "Microphone Gain",
                  "access": "Both",
                  "usageId": 33, "value" : 2
                },
                {
                  "name": "Sidetone",
                  "access": "Both",
                  "usageId": 34, "value" : 1
                },
                {
                  "name": "Equalizer",
                  "access": "Both",
                  "usageId": 35, "value" : 3
                },
                {
                  "name": "Audio Bandwidth",
                  "access": "Admin",
                  "usageId": 36, "value" : 0
                },
                {
                  "name": "Bluetooth",
                  "access": "Admin",
                  "usageId": 39, "value" : 0
                },
                {
                  "name": "DECT Radio Range",
                  "access": "Admin",
                  "usageId": 37, "value" : 0
                }
                {
                   "name": "Conference",
                  "access": "Admin",
                  "usageId": 41, "value" : 0
              ]
            }
          ]
        }
      ]
    }
  }
}
```

Step 3

Save the defaultheadsetconfig.json .

#### What to do next

### Install the Default Configuration File on Cisco Unified Communications Manager

After you edit the defaultheadsetconfig.json file, install it on Cisco Unified Communications Manager using the TFTP File Management tool.

Step 1

From Cisco Unified OS Administration, choose Software Upgrades > TFTP File Management .

Step 2

Select Upload File .

Step 3

Select Choose File and navigate to the defaultheadsetconfig.json file.

Step 4

Select Upload File .

Step 5

Click Close .

### Restart the Cisco TFTP Server

After you upload the defaultheadsetconfig.json file to the TFTP directory, restart the Cisco TFTP server and reset the phones. After about 10–15 minutes, the download process
                                 begins and the new configurations are applied to the headsets. It takes an additional 10 to 30 minutes for the settings to
                                 be applied.

Step 1

Log in to Cisco Unified Serviceability and choose Tools > Control Center - Feature Services .

Step 2

From the Server drop-down list box, choose the server on which the Cisco TFTP service is running.

Step 3

Click the radio button that corresponds to the Cisco TFTP service.

Step 4

Click Restart .

| Note | Cisco Unified
                                          			 Communications Manager Administration also provides several service parameters
                                          			 that you can use to configure various telephony functions. For more information
                                          			 on accessing and configuring service parameters, see the 
                                          			 documentation for your particular Cisco Unified Communications Manager release. For more information on the functions of a service, select the name of the parameter or the question mark (?) help button in the Service Parameter Configuration window. |
|---|---|

| Feature | Description and more information |
|---|---|
| Abbreviated Dialing | Allows
                                          						users to speed dial a phone number by entering an assigned index code (1-199)
                                          						on the phone keypad. Note You
                                                      						  can use Abbreviated Dialing while on-hook or off-hook. Users
                                          						assign index codes from the Self Care Portal. | Note | You
                                                      						  can use Abbreviated Dialing while on-hook or off-hook. |
| Note | You
                                                      						  can use Abbreviated Dialing while on-hook or off-hook. |
| Actionable Incoming Call Alert | Provides different options to control the incoming call alerts. You can disable or enable the call alert. You can also activate
                                          or deactivate the caller ID display. See Actionable Incoming Call Alert, Product Specific Configuration . |
| AES 256 Encryption Support for Phones | Enhances security by supporting TLS 1.2 and new ciphers. For more information, see Supported Security Features . |
| Agent
                                          						Greeting | Allows
                                          						an agent to create and update a prerecorded greeting that plays at the
                                          						beginning of a customer call, before the agent begins the conversation with the
                                          						caller. The agent can prerecord a single greeting or multiple ones as needed. See Enable Agent Greeting . |
| Always On Mode | Always keeps the DECT connection between the headset and base even when the user is not on a call or playing music. This feature is supported on Cisco Headset 500 Series. See Headset template management in Call Manager for more information. |
| Any Call
                                          						Pickup | Allows
                                          						users to pick up a call on any line in their call pickup group, regardless of
                                          						how the call was routed to the phone. See call pickup in the documentation for your particular Cisco Unified Communications Manager release. |
| Application Dial Rules | Convert numbers for shared mobile contacts to network dialable numbers. See Application Dial Rules . |
| Assisted
                                          						Directed Call Park | Enables
                                          						users to park a call by pressing only one button using the Direct Park feature.
                                          						Administrators must configure a Busy Lamp Field (BLF) Assisted Directed Call
                                          						Park button. When users press an idle BLF Assisted Directed Call Park button
                                          						for an active call, the active call is parked at the Direct Park slot
                                          						associated with the Assisted Directed Call Park button. See assisted directed call park in  the documentation for your particular Cisco Unified Communications Manager release. |
| Audible
                                          						Message Waiting Indicator (AMWI) | A
                                          						stutter tone from the handset, headset, or speakerphone indicates that a user
                                          						has one or more new voice messages on a line. Note The
                                                      						  stutter tone is line-specific. You hear it only when using the line with the
                                                      						  waiting messages. | Note | The
                                                      						  stutter tone is line-specific. You hear it only when using the line with the
                                                      						  waiting messages. |
| Note | The
                                                      						  stutter tone is line-specific. You hear it only when using the line with the
                                                      						  waiting messages. |
| Auto
                                          						Answer | Connects
                                          						incoming calls automatically after a ring or two. Auto
                                          						Answer works with either the speakerphone or the headset. See directory number information in the documentation for your particular Cisco Unified Communications Manager release. |
| Automatic Port Synchronization | Synchronizes ports to the lowest speed between ports of a phone
                                          						to eliminate packet loss. See Automatic Port Synchronization, Product Specific Configuration . |
| Auto
                                          						Pickup | Allows a
                                          						user to use one-touch pickup functionality for call pickup features. See call pickup in the documentation for your particular Cisco Unified Communications Manager release. |
| Barge | Enables a user to barge into a call by establishing the three-way conference call using the built-in conference bridge of
                                          the target phone. See "cBarge" in this table. |
| Block
                                          						External to External Transfer | Prevents users from transferring an external call to another
                                          						external number. See
                                          						external call transfer information in the documentation for your particular Cisco Unified Communications Manager release. |
| Bluetooth Multiconnection | Enables the user to pair multiple devices to the phone. The user can then connect a mobile device using Bluetooth and a Bluetooth
                                          headset at the same time. Cisco IP Phone 8851NR does not support Bluetooth. |
| Bluetooth Mute Sync for Cisco Headset 700 Series and 900 Series | The mute status between the IP Phone and Cisco headset is synchronized automatically during a call. Supported on the Cisco IP Phones 8845, 8851, 8861, and 8865, connected with Cisco Headset 720/730/950/980 Series. |
| Busy
                                          						Lamp Field (BLF) | Allows
                                          						a user to monitor the call state of a directory number associated with a
                                          						speed-dial button on the phone. See presence information in the documentation for your particular Cisco Unified Communications Manager release. |
| Busy
                                          						Lamp Field (BLF) Pickup | Provides enhancements to BLF speed dial. Allows you to configure
                                          						a Directory Number (DN) that a user can monitor for incoming calls. When the DN
                                          						receives an incoming call, the system alerts the monitoring user, who can then
                                          						pick up the call. See call pickup information in the documentation for your particular Cisco Unified Communications Manager release. |
| Call
                                          						Back | Provides users with an audio and visual alert on the phone when
                                          						a busy or unavailable party becomes available. See call back information in the documentation for your particular Cisco Unified Communications Manager release. |
| Call
                                          						Display Restrictions | Determines the information that will display for calling or
                                          						connected lines, depending on the parties who are involved in the call. See routing plans and call display restriction information in the documentation for your particular Cisco Unified Communications
                                          Manager release. |
| Call
                                          						Forward | Allows
                                          						users to redirect incoming calls to another number. Call Forward options
                                          						include Call Forward All, Call Forward Busy, Call Forward No Answer, and Call
                                          						Forward No Coverage. See directory number information in the documentation for your particular Cisco Unified Communications Manager release and Customize the Self Care Portal Display . |
| Call
                                          						Forward All Loop Breakout | Detects and prevents Call Forward All loops. When a Call Forward
                                          						All loop is detected, the Call Forward All configuration is ignored and the
                                          						call rings through. |
| Call
                                          						Forward All Loop Prevention | Detects and prevents Call Forward All loops. When a Call Forward
                                          						All loop is detected, the Call Forward All configuration is ignored and the
                                          						call rings through. |
| Call
                                          						Forward Configurable Display | Prevents a user from configuring a Call Forward All destination
                                          						directly on the phone that creates a Call Forward All loop or that creates a
                                          						Call Forward All chain with more hops than the existing Forward Maximum Hop
                                          						Count service parameter allows. See directory number information in  the documentation for your particular Cisco Unified Communications Manager release. |
| Call
                                          						Forward Destination Override | Allows
                                          						you to override Call Forward All (CFA) in cases where the CFA target places a
                                          						call to the CFA initiator. This feature allows the CFA target to reach the CFA
                                          						initiator for important calls. The override works whether the CFA target phone
                                          						number is internal or external. See
                                          						directory number information in  the documentation for your particular Cisco Unified Communications Manager release. |
| Call
                                          						Forward Notification | Allows
                                          						you to configure the information that the user sees when receiving a forwarded
                                          						call. See Set Up Call Forward Notification . |
| Call
                                          						History for Shared Line | Allows you to view shared line activity in the phone Call History. This feature will: Log missed calls for a shared line Log all answered and placed calls for a shared line |
| Call
                                          						Park | Allows
                                          						users to park (temporarily store) a call and then retrieve the call by using
                                          						another phone in the Cisco Unified Communications Manager system. You can configure the field Dedicate one line for call park in the Product Specific Configuration Layout pane to park the call to the original line or a different line. When the field is
                                          									enabled, the parked call remains on the user's line and they can
                                          									use the Resume softkey to pick up the
                                          									call. The user sees the extension number for the parked call on
                                          									the phone display. When the field is
                                          									disabled, the parked call transfers to the call park line. The
                                          									user's line returns to the idle state and they see the call park
                                          									extension in a pop-up window. The user dials the extension to
                                          									pick up the call. See
                                          						call park information in the documentation for your particular Cisco Unified Communications Manager release. |
| Call
                                          						Pickup | Allows
                                          						users to redirect a call that is ringing on another phone within their pickup
                                          						group to their phone. You
                                          						can configure an audio and visual alert for the primary line on the phone. This
                                          						alert notifies the users that a call is ringing in their pickup group. See
                                          						call pickup information in   the documentation for your particular Cisco Unified Communications Manager release. |
| Call
                                          						Recording | Allows
                                          						a supervisor to record an active call. The user might hear a recording audible
                                          						alert tone during a call when it is being recorded. When a
                                          						call is secured, the security status of the call is displayed as a lock icon on
                                          						Cisco IP Phones. The connected parties might also hear an audible alert tone
                                          						that indicates the call is secured and is being recorded. Note When
                                                      						  an active call is being monitored or recorded, the user can receive or place
                                                      						  intercom calls; however, if the user places an intercom call, the active call
                                                      						  is put on hold, which causes the recording session to terminate and the
                                                      						  monitoring session to suspend. To resume the monitoring session, the party
                                                      						  whose call is being monitored must resume the call. See
                                          						monitoring and recording information in the documentation for your particular Cisco Unified Communications Manager release. | Note | When
                                                      						  an active call is being monitored or recorded, the user can receive or place
                                                      						  intercom calls; however, if the user places an intercom call, the active call
                                                      						  is put on hold, which causes the recording session to terminate and the
                                                      						  monitoring session to suspend. To resume the monitoring session, the party
                                                      						  whose call is being monitored must resume the call. |
| Note | When
                                                      						  an active call is being monitored or recorded, the user can receive or place
                                                      						  intercom calls; however, if the user places an intercom call, the active call
                                                      						  is put on hold, which causes the recording session to terminate and the
                                                      						  monitoring session to suspend. To resume the monitoring session, the party
                                                      						  whose call is being monitored must resume the call. |
| Call
                                          						Waiting | Indicates (and allows users to answer) an incoming call that
                                          						rings while on another call. Incoming call information appears on the phone
                                          						display. See
                                          						directory number information in the documentation for your particular Cisco Unified Communications Manager release. |
| Call
                                          						Waiting Ring | Provides Call Waiting users with the option of an audible ring
                                          						instead of the standard beep. Options are Ring and Ring Once. See
                                          						directory number information in the documentation for your particular Cisco Unified Communications Manager release. |
| Caller
                                          						ID | Caller
                                          						identification such as a phone number, name, or other descriptive text appear
                                          						on the phone display. See routing plan, call display restrictions, and directory number information in the documentation for your particular Cisco
                                          Unified Communications Manager release. |
| Caller
                                          						ID Blocking | Allows
                                          						a user to block their phone number or email address from phones that have
                                          						caller identification enabled. See routing plan and directory number information in the documentation for your particular Cisco Unified Communications Manager
                                          release. |
| Calling Party Normalization | Calling party normalization presents phone calls to the user
                                          						with a dialable phone number. Any escape codes are added to the number so that
                                          						the user can easily connect to the caller again. The dialable number is saved
                                          						in the call history and can be saved in the Personal Address Book. |
| CAST
                                          						for SIP | Establishes communication between the Cisco Unified Video
                                          						Advantage (CUVA) and the Cisco IP phones to support video on the PC even if the
                                          						IP phone does not have video capability. |
| cBarge | Allows
                                          						a user to join a nonprivate call on a shared phone line. cBarge adds a user to
                                          						a call and converts it into a conference, allowing the user and other parties
                                          						to access conference features. The conference call is created using the Cisco
                                          						Unified Communications Manager conference bridge functionality. You must enable both the softkey and the conference bridge functionality for cBarge to function correctly. In Firmware Release 10.2(2) and later, the cBarge functionality is accessed using the Barge softkey. For more information, refer to the "Barge" chapter, Feature Configuration Guide for Cisco Unified Communications Manager . |
| Charge
                                          						a Mobile Device | Allows
                                          						a user to charge a mobile device by connecting it to the USB port of the Cisco
                                          						IP Phone. See Cisco IP Phone 8800 Series User Guide . |
| Cisco
                                          						Extension Mobility | Allows
                                          						users access to their Cisco IP Phone configuration such as line
                                          						appearances, services, and speed dials from a shared Cisco IP Phone. Cisco
                                          						Extension Mobility is useful if people work from a variety of locations
                                          						within your company or if they share a workspace with coworkers. |
| Cisco
                                          						Extension Mobility Cross Cluster (EMCC) | Enables a user configured in one cluster to log into a Cisco IP
                                          						Phone in another cluster. Users from a home cluster log into a Cisco IP Phone
                                          						at a visiting cluster. Note Configure Cisco Extension Mobility on Cisco IP Phones before you
                                                      						  configure EMCC. | Note | Configure Cisco Extension Mobility on Cisco IP Phones before you
                                                      						  configure EMCC. |
| Note | Configure Cisco Extension Mobility on Cisco IP Phones before you
                                                      						  configure EMCC. |
| Cisco IP Manager Assistant (IPMA) | Provides call routing and other call management features to help
                                          managers and assistants handle phone calls more effectively. See Set up Cisco IP Manager Assistant . |
| Cisco IP Phone 8800 Key Expansion Module Cisco IP Phone 8851/8861 Key Expansion Module Cisco IP Phone 8865 Key Expansion Module | Provides additional keys by adding an expansion module to the phone. For additional information, see Cisco IP Phone 7800 and 8800 Series Accessories Guide for Cisco Unified Communications Manager . |
| Cisco IP Phone 8811 Support | Provides support for the Cisco IP Phone 8811 . |
| Cisco IP Phone 8851NR Support | Provides support for the Cisco IP Phone 8851NR |
| Cisco
                                          						Unified Communications Manager Express (Unified CME) Version Negotiation | The
                                          						Cisco Unified Communication Manager Express uses a special tag in the
                                          						information sent to the phone to identify itself. This tag enables the phone to
                                          						provide services to the user that the switch supports. See: Cisco Unified
                                                   								Communications Manager Express System Administrator Guide Cisco Unified Communications Manager Express Interaction |
| Cisco
                                          						Unified Video Advantage (CUVA) | Allows
                                          						users to make video calls by using a Cisco IP Phone, a personal computer, and a
                                          						video camera. Note Configure the Video Capabilities parameter in the Product
                                                      						  Specific Configuration Layout section in Phone Configuration. See
                                          						the Cisco Unified Video Advantage documentation. | Note | Configure the Video Capabilities parameter in the Product
                                                      						  Specific Configuration Layout section in Phone Configuration. |
| Note | Configure the Video Capabilities parameter in the Product
                                                      						  Specific Configuration Layout section in Phone Configuration. |
| Cisco
                                          						WebDialer | Allows
                                          						users to make calls from web and desktop applications. |
| Classic Ringtone | Supports ringtones that are embedded in the phone firmware or
                                          						downloaded from the Cisco Unified Communications Manager. The feature makes the
                                          						available ringtones common with other Cisco IP Phones. See Custom Phone Rings . |
| Conference | Allows
                                          						a user to talk simultaneously with multiple parties by calling each participant
                                          						individually. Conference features include Conference and Meet Me. Allows
                                          						a noninitiator in a standard (adhoc) conference to add or remove participants;
                                          						also allows any conference participant to join together two standard
                                          						conferences on the same line. The
                                          						Advance Adhoc Conference service parameter, disabled by default in Cisco
                                          						Unified Communications Manager Administration, allows you to enable these
                                          						features. Note Be
                                                      						  sure to inform your users if these features are activated. | Note | Be
                                                      						  sure to inform your users if these features are activated. |
| Note | Be
                                                      						  sure to inform your users if these features are activated. |
| Configurable Energy Efficient Ethernet (EEE) for PC and Switch Port | Provides a method to control EEE functions on personal computer port and switch port by enabling or disabling EEE. The feature
                                          controls both type of ports individually. The default value is Enabled. See Set Up Energy Efficient Ethernet for Switch and PC Port . |
| Configurable Font Size | Allows
                                          						users to increase or decrease the maximum number of characters the IP phone
                                          						displays for Call History and Call Screen by changing the font size. A
                                          						smaller font increases the maximum number of displayed characters, and a larger
                                          						font decreases the maximum number of displayed characters. |
| CTI
                                          						Applications | A
                                          						computer telephony integration (CTI) route point can designate a virtual device
                                          						to receive multiple, simultaneous calls for application-controlled redirection. |
| Decline All | Allows
                                          						a user to transfer a ringing, connected, or held call directly to a
                                          						voice-messaging system. When a call is declined, the line becomes available to
                                          						make or receive new calls. See immediate divert information in the documentation for your particular Cisco Unified Communications Manager release. |
| Device
                                          						Invoked Recording | Provides end users with the ability to record their telephone
                                          						calls via a softkey. In
                                          						addition administrators may continue to record telephone calls via the CTI User
                                          						Interface. See monitoring and recording information in the documentation for your particular Cisco Unified Communications Manager release. |
| Directed Call Park | Allows
                                          						a user to transfer an active call to an available directed call park number
                                          						that the user dials or speed dials. A Call Park BLF button indicates whether a
                                          						directed call park number is occupied and provides speed-dial access to the
                                          						directed call park number. Note If
                                                      						  you implement Directed Call Park, avoid configuring the Park softkey. This
                                                      						  prevents users from confusing the two Call Park features. See call park information in the documentation for your particular Cisco Unified Communications Manager release. | Note | If
                                                      						  you implement Directed Call Park, avoid configuring the Park softkey. This
                                                      						  prevents users from confusing the two Call Park features. |
| Note | If
                                                      						  you implement Directed Call Park, avoid configuring the Park softkey. This
                                                      						  prevents users from confusing the two Call Park features. |
| Display Battery Strength and Signal Strength Icons | Displays the battery and signal strength of the mobile phone on the IP Phone when the mobile phone is connected to the IP
                                          Phone using Bluetooth. Cisco IP Phone 8851NR does not support Bluetooth. |
| Distinctive Ring | Users
                                          						can customize how their phone indicates an incoming call and a new voice mail
                                          						message. See
                                          						call pickup information in the documentation for your particular Cisco Unified Communications Manager release. |
| Do Not
                                          						Disturb (DND) | When
                                          						DND is turned on, either no audible rings occur during the ringing-in state of
                                          						a call, or no audible or visual notifications of any type occur. When enabled, the phone header turns red and Do not disturb is displayed on the phone. If multilevel precedence and preemption (MLPP) is configured and the user receives a precedence call, the phone will ring
                                          with a special ringtone. See Set Up Do Not Disturb . |
| Dock Event | Allows a user to set up the call behavior when the headset is lift from the base or is put down on the base. This feature is supported on Cisco Headset 500 Series. See Headset template management in Call Manager for more information. |
| Enable/Disable JAL/TAL | Allows the administrator to control the Join Across Lines (JAL) and Direct Transfer Across Lines (TAL) features. See Join and Direct Transfer Policy, Product Specific Configuration . |
| EnergyWise | Enables an IP Phone to sleep (power down) and wake (power up) at
                                          						predetermined times, to promote energy savings. See Schedule EnergyWise on Cisco IP Phone . |
| Enhanced Line Mode | Enable Enhanced Line Mode to use the buttons on both sides of the phone screen as line keys. See Set Up Additional Line Keys |
| Enhanced Secure Extension Mobility Cross Cluster (EMCC) | Improves the Secure Extension Mobility Cross Cluster (EMCC)
                                          						feature by preserving the network and security configurations on the login
                                          						phone. By so doing, security policies are maintained, network bandwidth is
                                          						preserved and network failure is avoided within the visiting cluster (VC). |
| Fast
                                          						Dial Service | Allows
                                          						a user to enter a Fast Dial code to place a call. Fast Dial codes can be
                                          						assigned to phone numbers or Personal Address Book entries. See "Services" in this table. See Modify Phone Button Template for PAB or Fast Dial . |
| Group
                                          						Call Pickup | Allows
                                          						a user to answer a call that is ringing on a directory number in another group. See
                                          						call pickup information in the documentation for your particular Cisco Unified Communications Manager release. |
| Headset Sidetone Control | Allows
                                          						an administrator to set the sidetone level of a wired headset. |
| Hold
                                          						Reversion | Limits
                                          						the amount of time that a call can be on hold before reverting back to the
                                          						phone that put the call on hold and alerting the user. Reverting calls are distinguished from incoming calls by a
                                          						single ring (or beep, depending on the new call indicator setting for the
                                          						line). This notification repeats at intervals if not resumed. A call
                                          						that triggers Hold Reversion also displays an animated icon in the call bubble.
                                          						You can configure call focus priority to favor incoming or reverting calls. |
| Hold
                                          						Status | Enables phones with a shared line to distinguish between the
                                          						local and remote lines that placed a call on hold. |
| Hold/Resume | Allows
                                          						the user to move a connected call from an active state to a held state. No
                                                							 configuration required unless you want to use Music On Hold. See "Music On Hold" in this table for information. See "Hold Reversion" in this table. |
| HTTP
                                          						Download | Enhances the file download process to the phone to use HTTP by
                                          						default. If the HTTP download fails, the phone reverts to using the TFTP
                                          						download. |
| Hunt
                                          						Group | Provides load sharing for calls to a main directory number. A
                                          						hunt group contains a series of directory numbers that can answer the incoming
                                          						calls. When the first directory number in the hunt group is busy, the system
                                          						hunts in a predetermined sequence for the next available directory number in
                                          						the group and directs the call to that phone. You can have Caller ID (If the Caller ID is configured), Directory Number and Hunt group Pilot Number display on the Incoming Call Alert for the hunt group call. The hunt group number is displayed after the label "Hunt Group. See hunt group and routing plans information in the documentation for your particular Cisco Unified Communications Manager
                                          release. |
| Incoming Call Toast Timer | Allows
                                          						you to set the length of time that an incoming call toast (notification)
                                          						appears on the phone screen. See Incoming Call Toast Timer, Product Specific Configuration . |
| Intelligent Proximity | Enables users to pair a mobile device with the phone using
                                          						Bluetooth and use the phone to place and receive mobile calls, See Enable Intelligent Proximity . Cisco IP Phone 8811, 8841, and 8851NR do not support Bluetooth or Intelligent Proximity. |
| Intercom | Allows
                                          						users to place and receive intercom calls using programmable phone buttons. You
                                          						can configure intercom line buttons to: Directly dial a specific intercom extension. Initiate an intercom call and then prompt the user to enter a valid intercom number. Note If
                                                      						  your user logs into the same phone on a daily basis using their Cisco Extension
                                                      						  Mobility profile, assign the phone button template that contains intercom
                                                      						  information to their profile, and assign the phone as the default intercom
                                                      						  device for the intercom line. | Note | If
                                                      						  your user logs into the same phone on a daily basis using their Cisco Extension
                                                      						  Mobility profile, assign the phone button template that contains intercom
                                                      						  information to their profile, and assign the phone as the default intercom
                                                      						  device for the intercom line. |
| Note | If
                                                      						  your user logs into the same phone on a daily basis using their Cisco Extension
                                                      						  Mobility profile, assign the phone button template that contains intercom
                                                      						  information to their profile, and assign the phone as the default intercom
                                                      						  device for the intercom line. |
| IPv6-only Support | Provides support for expanded IP addressing on Cisco IP Phones. IPv4 and IPv6 configuration is recommended and fully supported.
                                          Certain features are not supported in a standalone configuration. Only IPv6 address are assigned. See Configure Network Settings . |
| Jitter
                                          						Buffer | The
                                          						Jitter Buffer feature handles jitter from 10 milliseconds (ms) to 1000 ms for
                                          						audio streams. It runs in an adaptive mode and it dynamically adjusts to the amount of jitter. |
| Join | Allows
                                          						users to combine two calls that are on one line to create a conference call and
                                          						remain on the call. |
| Line
                                          						Status for Call Lists | Allows
                                          						the user to see the Line Status availability status of monitored line numbers
                                          						in the Call History list. The Line Status states are Offline Available In
                                                							 use Do
                                                							 not disturb See Enable BLF for Call Lists . |
| Line Status in Corporate Directory | Enables the display of the status of a contact in the Corporate Directory. Offline Available In use Do not disturb See Enable BLF for Call Lists . |
| Line Text Label | Sets a text label for a phone line instead of the directory number. See Set the Label for a Line . |
| Log
                                          						out of hunt groups | Allows
                                          						users to log out of a hunt group and temporarily block calls from ringing their
                                          						phone when they are not available to take calls. Logging out of hunt groups
                                          						does not prevent nonhunt group calls from ringing their phone. See 
                                          						routing plan information in the documentation for your particular Cisco Unified Communications Manager release. |
| Malicious Caller Identification (MCID) | Allows
                                          						users to notify the system administrator about suspicious calls that are
                                          						received. |
| Meet
                                          						Me Conference | Allows
                                          						a user to host a Meet Me conference in which other participants call a
                                          						predetermined number at a scheduled time. |
| Message Waiting | Defines directory numbers for message waiting on and off
                                          						indicators. A directly-connected voice-message system uses the specified
                                          						directory number to set or to clear a message waiting indication for a
                                          						particular Cisco IP Phone. See message waiting and voice mail information in the documentation for your particular Cisco Unified Communications Manager
                                          release. |
| Message Waiting Indicator | A
                                          						light on the handset that indicates that a user has one or more new voice
                                          						messages. See message waiting and voice mail information in the documentation for your particular Cisco Unified Communications Manager
                                          release. |
| Minimum Ring Volume | Sets a
                                          						minimum ringer volume level for an IP phone. |
| Missed
                                          						Call Logging | Allows
                                          						a user to specify whether missed calls will be logged in the missed calls
                                          						directory for a given line appearance. See
                                          						directory number information in the documentation for your particular Cisco Unified Communications Manager release. |
| Mobile
                                          						Connect | Enables users to manage business calls using a single phone
                                          						number and pick up in-progress calls on the desk phone and a remote device such
                                          						as a mobile phone. Users can restrict the group of callers according to phone
                                          						number and time of day. See Cisco Unified Mobility information in the documentation for your particular Cisco Unified Communications Manager release. |
| Mobile and Remote Access
                                             				Through Expressway | Allows remote workers to easily and securely connect into the corporate network without using a virtual private network (VPN)
                                          client tunnel. See Mobile and Remote Access Through Expressway |
| Mobile
                                          						Voice Access | Extends Mobile Connect capabilities by allowing users to access
                                          						an interactive voice response (IVR) system to originate a call from a remote
                                          						device such as a cellular phone. See
                                          						Cisco Unified Mobility in the documentation for your particular Cisco Unified Communications Manager release. |
| Monitoring and Recording | Allows
                                          						a supervisor to silently monitor an active call. The supervisor cannot be heard
                                          						by either party on the call. The user might hear a monitoring audible alert
                                          						tone during a call when it is being monitored. When a
                                          						call is secured, the security status of the call is displayed as a lock icon on
                                          						Cisco IP Phones. The connected parties might also hear an audible alert tone
                                          						that indicates the call is secured and is being monitored. Note When
                                                      						  an active call is being monitored or recorded, the use can receive or place
                                                      						  intercom calls; however, if the user place an intercom call, the active call
                                                      						  will be put on hold, which causes the recording session to terminate and the
                                                      						  monitoring session to suspend. To resume the monitoring session, the party
                                                      						  whose call is being monitored must resume the call. | Note | When
                                                      						  an active call is being monitored or recorded, the use can receive or place
                                                      						  intercom calls; however, if the user place an intercom call, the active call
                                                      						  will be put on hold, which causes the recording session to terminate and the
                                                      						  monitoring session to suspend. To resume the monitoring session, the party
                                                      						  whose call is being monitored must resume the call. |
| Note | When
                                                      						  an active call is being monitored or recorded, the use can receive or place
                                                      						  intercom calls; however, if the user place an intercom call, the active call
                                                      						  will be put on hold, which causes the recording session to terminate and the
                                                      						  monitoring session to suspend. To resume the monitoring session, the party
                                                      						  whose call is being monitored must resume the call. |
| Multilevel Precedence and Preemption | Enables the user to make and receive urgent or critical calls in some specialized environments, such as military or government
                                          offices. See Multilevel Precedence and Preemption . |
| Multiple Calls Per Line Appearance | Each
                                          						line can support multiple calls. By default, the phone supports two active
                                          						calls per line, and a maximum of six active calls per line. Only one call can
                                          						be connected at any time; other calls are automatically placed on hold. The
                                          						system allows you to configure maximum calls/busy trigger not more than 6/6.
                                          						Any configuration more than 6/6 is not officially supported. See
                                          						directory number information in the documentation for your particular Cisco Unified Communications Manager release. |
| Music
                                          						On Hold | Plays
                                          						music while callers are on hold. |
| Mute | Mutes
                                          						the handset or headset microphone. |
| No
                                          						Alert Name | Makes
                                          						it easier for end users to identify transferred calls by displaying the
                                          						original caller’s phone number. The call appears as an Alert Call followed by
                                          						the caller’s telephone number. |
| Onhook
                                          						Dialing | Allows
                                          						a user to dial a number without going off hook. The user can then either pick
                                          						up the handset or press Dial. |
| Other
                                          						Group Pickup | Allows
                                          						a user to answer a call ringing on a phone in another group that is associated
                                          						with the user's group. See
                                          						call pickup information in the documentation for your particular Cisco Unified Communications Manager release. |
| Phone
                                          						Display Message for Extension Mobility Users | This
                                          						feature enhances the phone interface for the Extension Mobility user by
                                          						providing friendly messages. |
| Phone Trust List Notification in Cisco Unified Communications Manager | Enables the phone to send an alarm to the Cisco Unified Communications Manager when the Trust List (TL) is updated. See Supported Security Features . |
| PLK
                                          						Support for Queue Statistics | The
                                          						PLK Support for Queue Statistics feature enables the users to query the call
                                          						queue statistics for hunt pilots and the information appears on phone screen. |
| Plus
                                          						Dialing | Allows
                                          						the user to dial E.164 numbers prefixed with a plus (+) sign. To
                                          						dial the + sign, the user needs to press and hold the star (*) key for at least
                                          						1 second. This applies to dialing the first digit for an on-hook (including
                                          						edit mode) or off-hook call. |
| Power
                                          						Negotiation over LLDP | Allows the phone to negotiate power using Link Level Endpoint Discovery Protocol (LLDP) and Cisco Discovery Protocol (CDP). See Power Negotiation, Product Specific Configuration . |
| Predictive Dialing | Simplifies making a call. The Recents list changes to displays only phone numbers similar to the number being dialed. Predictive Dialing is enabled when Enhanced Line mode is enabled. Simplified New Call UI must be disabled for Predictive Dialing
                                          to function. |
| Privacy | Prevents users who share a line from adding themselves to a call
                                          						and from viewing information on their phone display about the call of the other
                                          						user. See barge and privacy information in the documentation for your particular Cisco Unified Communications Manager release. |
| Private Line Automated Ringdown (PLAR) | The
                                          						Cisco Unified Communications Manager administrator can configure a phone number
                                          						that the Cisco IP Phone dials as soon as the handset goes off hook. This can be
                                          						useful for phones that are designated for calling emergency or "hotline" numbers. The administrator can configure a delay
                                          									of up to 15-seconds. This allows the user time to place a call
                                          									before the phone defaults to the hotline number. The timer is
                                          									configurable through the parameter Off Hook To First
                                             										Digit Timer under Device > Device Settings > SIP Profile . For more information, refer to Feature Configuration Guide for
                                             										Cisco Unified Communications Manager . |
| Problem Report Tool (PRT) | Submit phone logs or report problems to an administrator. See Problem Report Tool . |
| Programmable Feature Buttons | You
                                          						can assign features, such as New Call, Call Back, and Forward All to line
                                          						buttons. See phone button template information in the documentation for your particular Cisco Unified Communications Manager release. |
| Quality Reporting Tool (QRT) | Allows
                                          						users to submit information about problem phone calls by pressing a button. QRT
                                          						can be configured for either of two user modes, depending upon the amount of
                                          						user interaction desired with QRT. |
| Recents | Allows users to see the 150 most recent individual calls and call groups. You can see the recently dialed numbers, missed
                                          calls, and delete a call record. |
| Redial | Allows
                                          						users to call the most recently dialed phone number by pressing a button or the
                                          						Redial softkey. |
| Remote
                                          						Port Configuration | Allows
                                          						you to configure the speed and duplex function of the phone Ethernet ports
                                          						remotely by using Cisco Unified Communications Manager Administration. This
                                          						enhances the performance for large deployments with specific port settings. Note If
                                                      						  the ports are configured for Remote Port Configuration in Cisco Unified
                                                      						  Communications Manager, the data cannot be changed on the phone. See Remote Port Configuration, Product Specific Configuration . | Note | If
                                                      						  the ports are configured for Remote Port Configuration in Cisco Unified
                                                      						  Communications Manager, the data cannot be changed on the phone. |
| Note | If
                                                      						  the ports are configured for Remote Port Configuration in Cisco Unified
                                                      						  Communications Manager, the data cannot be changed on the phone. |
| Reroute Direct Calls to Remote Destination to Enterprise Number | Reroutes a direct call to a user's mobile phone to the
                                          						enterprise number (desk phone). For an incoming call to remote destination
                                          						(mobile phone), only remote destination rings; desk phone does not ring. When
                                          						the call is answered on their mobile phone, the desk phone displays a Remote In
                                          						Use message. During these calls, users can make use of various features of
                                          						their mobile phone. See
                                          						the 
                                          						Cisco Unified Mobility information in the documentation for your particular Cisco Unified Communications Manager release. |
| Remove 'Call Ended' Prompt Timer | Improves the End Call response time by removing the Call ended message display on the phone screen. |
| Ringtone Setting | Identifies ring type used for a line when a phone has another
                                          						active call. See directory number information in the documentation for your particular Cisco Unified Communications Manager release and Custom Phone Rings . |
| RTCP
                                          						Hold For SIP | Ensures that held calls are not dropped by the gateway. The
                                          						gateway checks the status of the RTCP port to determine if a call is active or
                                          						not. By keeping the phone port open, the gateway will not end held calls. |
| Secure
                                          						Conference | Allows secure phones to place conference calls using a secured conference bridge. As new participants are added by using Confrn,
                                          Join, or Barge softkeys or MeetMe conferencing, the secure call icon displays as long as all participants use secure phones. The
                                          						Conference List displays the security level of each conference participant.
                                          						Initiators can remove nonsecure participants from the Conference List.
                                          						Noninitiators can add or remove conference participants if the Advanced Adhoc
                                          						Conference Enabled parameter is set. See conference bridge and security information in the documentation for your particular Cisco Unified Communications Manager
                                          release and Supported Security Features . |
| Secure
                                          						EMCC | Improves the EMCC feature by providing enhanced security for a
                                          						user logging into their phone from a remote office. |
| Services | Allows
                                          						you to use the Cisco IP Phone Services Configuration menu in Cisco Unified
                                          						Communications Manager Administration to define and maintain the list of phone
                                          						services to which users can subscribe. See services information in the documentation for your particular Cisco Unified Communications Manager release. |
| Services URL button | Allows
                                          						users to access services from a programmable button rather than by using the
                                          						Services menu on a phone. See services information the documentation for your particular Cisco Unified Communications Manager release. |
| Show
                                          						Calling ID and Calling Number | The
                                          						phones can display both the calling ID and calling number for incoming calls.
                                          						The IP phone LCD display size limits the length of the calling ID and the
                                          						calling number that display. The
                                          						Show Calling ID and Calling Number feature applies to the incoming call alert
                                          						only and does not change the function of the Call Forward and Hunt Group
                                          						features. See "Caller ID" in this table. |
| Simplify Extension Mobility Login with Cisco Headsets | Enables users to sign into Extension Mobility with their Cisco headsets. When the phone is in MRA mode, the user can use the headset to sign into the phone. This feature requires Cisco Unified Communications Manager(UCM) Release 11.5(1)SU8, 11.5(1)SU.9, 12.5(1)SU3, 14.0(1) or later. For more information, see Feature Configuration Guide for Cisco Unified Communications Manager , Release 11.5(1)SU8 or later, or Release 12.5(1)SU3 or later. With Cisco Headset 720/730/950/980, user can also sign into Extension Mobility with the headset USB adapter (USB HD adapter
                                          or USB-C adapter). |
| Simplified Tablet Support | Enables an Android or iOS tablet user to pair the tablet to the phone using Bluetooth and then use the phone for the audio
                                          part of a call on the tablet. See Enable Intelligent Proximity . Cisco IP Phone 8851NR does not support Bluetooth. |
| Speed
                                          						Dial | Dials
                                          						a specified number that has been previously stored. |
| SSH
                                          						Access | Allows you to enable or disable the SSH Access setting using Cisco Unified Communications Manager Administration. Enabling
                                          the SSH server allows the phone to accept the SSH connections. Disabling the SSH server functionality of the phone blocks
                                          the SSH access to the phone. See SSH Access, Product Specific Configuration . |
| Time-of-Day Routing | Restricts access to specified telephony features by time period. See time period and time-of-day routing information in the documentation for your particular Cisco Unified Communications
                                          Manager release. |
| Time
                                          						Zone Update | Updates the Cisco IP Phone with time zone changes. See
                                          						date and time information in the documentation for your particular Cisco Unified Communications Manager release. |
| Transfer | Allows
                                          						users to redirect connected calls from their phones to another number. |
| Transfer - Direct Transfer | Transfer: The first invocation of Transfer will always initiate
                                          						a new call by using the same directory number, after putting the active call on
                                          						hold. The
                                          						user can directly transfer calls using Transfer Active Call Function. Some
                                          						JTAPI/TAPI applications are not compatible with the Join and Direct Transfer
                                          						feature implementation on the Cisco IP Phone and you may need to configure the
                                          						Join and Direct Transfer Policy to disable join and direct transfer on the same
                                          						line or possibly across lines. See 
                                          						directory number information in the documentation for your particular Cisco Unified Communications Manager release. |
| TVS | Trust
                                          						Verification Services (TVS) enables phones to authenticate signed
                                          						configurations and authenticate other servers or peers without increasing the
                                          						size of the Certificate Trust List (CTL) or requiring the downloading of an
                                          						updated CTL file to the phone. TVS is enabled by default. The
                                          						Security Setting menu on the phone displays the TVS information. |
| UCR
                                          						2013 | The
                                          						Cisco IP Phones support Unified Capabilities Requirements (UCR) 2013 by
                                          						providing the following functions: Support for Federal Information Processing Standard (FIPS) 140-3 Support for 80-bit SRTCP Tagging As an
                                          						IP Phone administrator, you must set up specific parameters in Cisco Unified
                                          						Communications Manager Administration. |
| Unconfigured Primary Line Notification | Alerts the user when the primary line is not configured. The user sees the message Unprovisioned on the phone screen. |
| User Interface Updates for List, Alert, and Visual Voicemail. | Increases the size of the application window to minimize truncated strings. |
| Video Mode | Allows a user to select the video display mode for viewing a video conference, depending on the modes configured in the system. See video information in the documentation for your particular Cisco Unified Communications Manager release. Available on Cisco IP Phone 8845, 8865, and 8865NR. |
| Video Support | Enables video support on the phone. The Video Capabilities parameter needs to be enabled for video calls on Cisco Unified
                                          Communications Manager Phone Configuration window. It is enabled by default. Available on Cisco IP Phone 8845, 8865, and 8865NR. |
| Video Through PC | Allows users to make video calls by using their Cisco Unified IP Phone, personal computer, and an external video camera. The feature also allows users to make video calls with Cisco Jabber or Cisco Unified Video Advantage products. |
| Visual
                                          						Voicemail | Replaces the voicemail audio prompts with a graphical interface. See Installation and Configuration Guide for Visual Voicemail located at http://www.cisco.com/en/US/partner/products/ps9829/prod_installation_guides_list.html#anchor3 . |
| Voice
                                          						Message System | Enables callers to leave messages if calls are unanswered. See voice mail information in the documentation for your particular Cisco Unified Communications Manager release and Set up Visual Voicemail . |
| VPN | Using SSL, provides a virtual private network (VPN) connection on
                                          the Cisco Unified IP Phone when it is located outside a trusted
                                          network or when network traffic between the phone and Unified
                                          Communications Manager must cross untrusted networks. |
| Web
                                          						Access Disabled by Default | Enhances security by disabling access to all web services, such
                                          						as HTTP. Users can only access web services if you enable web access. |

| Note | You
                                                      						  can use Abbreviated Dialing while on-hook or off-hook. |
|---|---|

| Note | The
                                                      						  stutter tone is line-specific. You hear it only when using the line with the
                                                      						  waiting messages. |
|---|---|

| Note | When
                                                      						  an active call is being monitored or recorded, the user can receive or place
                                                      						  intercom calls; however, if the user places an intercom call, the active call
                                                      						  is put on hold, which causes the recording session to terminate and the
                                                      						  monitoring session to suspend. To resume the monitoring session, the party
                                                      						  whose call is being monitored must resume the call. |
|---|---|

| Note | Configure Cisco Extension Mobility on Cisco IP Phones before you
                                                      						  configure EMCC. |
|---|---|

| Note | Configure the Video Capabilities parameter in the Product
                                                      						  Specific Configuration Layout section in Phone Configuration. |
|---|---|

| Note | Be
                                                      						  sure to inform your users if these features are activated. |
|---|---|

| Note | If
                                                      						  you implement Directed Call Park, avoid configuring the Park softkey. This
                                                      						  prevents users from confusing the two Call Park features. |
|---|---|

| Note | If
                                                      						  your user logs into the same phone on a daily basis using their Cisco Extension
                                                      						  Mobility profile, assign the phone button template that contains intercom
                                                      						  information to their profile, and assign the phone as the default intercom
                                                      						  device for the intercom line. |
|---|---|

| Note | When
                                                      						  an active call is being monitored or recorded, the use can receive or place
                                                      						  intercom calls; however, if the user place an intercom call, the active call
                                                      						  will be put on hold, which causes the recording session to terminate and the
                                                      						  monitoring session to suspend. To resume the monitoring session, the party
                                                      						  whose call is being monitored must resume the call. |
|---|---|

| Note | If
                                                      						  the ports are configured for Remote Port Configuration in Cisco Unified
                                                      						  Communications Manager, the data cannot be changed on the phone. |
|---|---|

| Feature
                                          					 name | Dedicated
                                          					 feature button | Programmable feature button | Softkey |
|---|---|---|---|
| Alert
                                          					 Calls | Not supported | Supported | Not supported |
| All Calls | Not supported | Supported | Not supported |
| Answer | Not supported | Supported | Supported |
| cBarge | Not supported | Not supported | Supported |
| Call Back | Not supported | Supported | Supported |
| Call
                                          					 Forward All | Not supported | Not supported | Supported |
| Call Park | Not supported | Supported | Supported |
| Call Park
                                          					 Line Status | Not supported | Supported | Not supported |
| Call
                                          					 Pickup (Pick Up) | Not supported | Supported | Supported |
| Call
                                          					 Pickup Line Status | Not supported | Supported | Not supported |
| Conference | Supported | Not supported | Supported |
| Divert | Not supported | Not supported | Supported |
| Do Not
                                          					 Disturb | Not supported | Supported | Supported |
| Group
                                          					 Pickup (Group Pick Up) | Not supported | Supported | Supported |
| Hold | Supported | Not supported | Supported |
| Hunt
                                          					 Groups | Not supported | Supported | Not supported |
| Intercom | Not supported | Supported | Not supported |
| Malicious Call Identification (MCID) | Not supported | Supported | Supported |
| Meet Me | Not supported | Supported | Supported |
| Merge | Not supported | Not supported | Supported |
| Mobile
                                          					 Connect (Mobility) | Not supported | Supported | Supported |
| Mute | Supported | Not supported | Not supported |
| Other
                                          					 Pickup | Not supported | Supported | Supported |
| PLK
                                          					 Support for Queue Status | Not supported | Not supported | Supported |
| Privacy | Not supported | Supported | Not supported |
| Queue
                                          					 Status | Not supported | Supported | Not supported |
| Quality
                                          					 Reporting Tool (QRT) | Not supported | Supported | Supported |
| Record | Not supported | Not supported | Supported |
| Redial | Not supported | Supported | Supported |
| Speed
                                          					 Dial | Not supported | Supported | Not supported |
| Speed
                                          					 Dial Line Status | Not supported | Supported | Not supported |
| Support
                                          					 for Hold Button on USB Headsets | Not supported | Not supported | Supported |
| Transfer | Supported | Not supported | Supported |

| Step 1 | Sign in to Cisco Unified
                                             				Communications Manager Administration as an administrator. |
|---|---|
| Step 2 | Select System > Enterprise Phone Configuration . |
| Step 3 | Set the fields you want to change. |
| Step 4 | Check the Override Enterprise Settings check box for any changed fields. |
| Step 5 | Click Save . |
| Step 6 | Click Apply Config . |
| Step 7 | Restart the phones. Note This will impact all phones in your organization. | Note | This will impact all phones in your organization. |
| Note | This will impact all phones in your organization. |

| Note | This will impact all phones in your organization. |
|---|---|

| Step 1 | Sign in to Cisco Unified
                                             				Communications Manager Administration as an administrator. |
|---|---|
| Step 2 | Select Device > Device Settings > Common Phone Profile . |
| Step 3 | Locate the profile. |
| Step 4 | Navigate to the Product Specific Configuration Layout pane and set the fields. |
| Step 5 | Check the Override Enterprise Settings check box for any changed fields. |
| Step 6 | Click Save . |
| Step 7 | Click Apply Config . |
| Step 8 | Restart the phones. |

| Step 1 | Sign in to Cisco Unified
                                             				Communications Manager Administration as an administrator. |
|---|---|
| Step 2 | Select Device > Phone |
| Step 3 | Locate the phone associated with the user. |
| Step 4 | Navigate to the Product Specific Configuration Layout pane and set the fields. |
| Step 5 | Check the Override Common Settings check box for any changed fields. |
| Step 6 | Click Save . |
| Step 7 | Click Apply Config . |
| Step 8 | Restart the phone. |

| Field Name | Field Type or Choices | Default | Description and Usage Guidelines |
|---|---|---|---|
| Disable Speakerphone | Check box | Unchecked | Turns off the speakerphone capability of the phone. |
| Disable Speakerphone and Headset | Check box | Unchecked | Turns off the speakerphone and headset capability of the phone. |
| Disable Handset | Checkbox | Unchecked | Turns off the handset capability of the phone. |
| PC Port | Enabled Disabled | Enabled | Controls the ability to use the PC port to connect a computer into the LAN. |
| Settings Access | Disabled Enabled Restricted | Enabled | Enables, disables, or restricts access to the local phone configuration settings in the Settings app. Disabled—The Settings menu does not display any options. Enabled—All entries in the Settings menu are accessible. Restricted—Only the Phone settings menu is accessible. |
| PC Voice VLAN Access | Enabled Disabled | Enabled | Indicates whether the phone will allow a device attached to the PC port to access the Voice VLAN. Disabled—The PC can't send and receive data on the Voice VLAN or from the phone. Enabled—The PC can send and receive data from the Voice VLAN or from the phone. Set this field to Enabled if an application
                                                   is being run on the PC that to monitor phone traffic. These applications could include monitoring and recording applications,
                                                   and the use of network monitoring software for analysis purposes. |
| Video Capabilities | Enabled Disabled | 8845, 8865, and 8865NR: Enabled 8811, 8851, 8851NR, 8861: Disabled | Allows users to make video calls by using a Cisco IP Phone, a personal computer, and a video camera. |
| Web Access | Disabled Enabled | Disabled | Enables or disables access to the phone web pages through a web browser. Caution If you enable this field, you may expose sensitive
                                                         										information about the phone. | Caution | If you enable this field, you may expose sensitive
                                                         										information about the phone. |
| Caution | If you enable this field, you may expose sensitive
                                                         										information about the phone. |
| Disable TLS 1.0 and TLS 1.1 for Web Access | Disabled Enabled | Enabled | Controls the use of TLS 1.2 for a web server connection. Disabled—A phone configured for TLS1.0, TLS 1.1, or TLS1.2 can function as a HTTPs server. Enabled—Only a phone configured for TLS1.2 can function as a HTTPs server. |
| TLS Client Min Version | TLS 1.0 TLS 1.1 TLS 1.2 | TLS 1.2 | Specifies the minimum TLS version required by the phone to establish a TLS connection. This parameter is available when the phone acts as a client. If the TLS version on the server side is older than the required minimum TLS version on the phone, the TLS connection will
                                             be rejected. TLS 1.0 : The TLS client (phone) supports the versions of TLS from 1.0 to 1.2. TLS 1.1 : The TLS client (phone) supports TLS 1.1 and TLS 1.2. If the TLS version in server is lower than 1.1, for example, 1.0, then the connection can't be established. TLS 1.2 : The TLS client (phone) supports TLS 1.2 only. If the TLS version in server is lower than 1.2, for example, 1.0 or 1.1, then the connection can't be established. Note This parameter is unavailable for the wireless networks. | Note | This parameter is unavailable for the wireless networks. |
| Note | This parameter is unavailable for the wireless networks. |
| Enbloc Dialing | Disabled Enabled | Disabled | Controls the dialing method. Disabled—The Cisco Unified Communications Manager waits for the interdigit timer to expire when there is a dial plan or route
                                                   pattern overlap. Enabled—The entire dialed string is sent to Cisco Unified Communications Manager once the dialing is complete. To avoid the
                                                   T.302 timer timeout, we recommend that you enable Enbloc Dialing whenever there is a dialplan or route pattern overlap. Forced Authorization Codes (FAC) or Client Matter Codes (CMC) do not support the Enbloc Dialing. If you use FAC or CMC to
                                             manage call access and accounting, then you cannot use this feature. |
| Days Display Not Active | Days of the week |  | Defines the days that the display does not turn on automatically at the time specified in the Display On Time field. Choose the day or days from the drop-down list. To choose more than one day, Ctrl+click each day that you want. |
| Display On Time | hh:mm |  | Defines the Time each day that the display turns on automatically (except on the days specified in the Days Display Not Active
                                             field). Enter the time in this field in 24 hour format, where 0:00 is midnight. For example, to automatically turn the display on at 07:00 a.m. (0700), enter 07:00. To turn the display on at 02:00 p.m.
                                             (1400), enter 14:00. If this field is blank, the display automatically turns on at 0:00. |
| Display On Duration | hh:mm |  | Defines the length of time that the display remains on after turning on at the time specified in the Display On Time field. For example, to keep the display on for 4 hours and 30 minutes after it turns on automatically, enter 04:30. If this field is blank, the phone turns off at the end of the day (0:00). If Display On Time is 0:00 and the display on duration is blank (or 24:00), the display does not turn off. |
| Display Idle Timeout | hh:mm | 01:00 | Defines the length of time that the phone is idle before the display turns off. Applies only when the display was off as scheduled
                                             and was turned on by a user (by pressing a button on the phone or lifting the handset). Enter the value in this field in the format hours:minutes. For example, to turn the display off when the phone is idle for 1 hour and 30 minutes after a user turns the display on, enter
                                             01:30. For more information, see Set Up Idle Display . |
| Display On When Incoming Call | Disabled Enabled | Enabled | Turns the idle display on when there is an incoming call. |
| Enable Power Save Plus | Days of the week |  | Defines the schedule of days for which the phone powers off. Choose the day or days from the drop-down list. To choose more than one day, Ctrl+click each day that you want. When Enable Power Save Plus is turned on, you receive a message that warns about emergency (e911) concerns. Caution While Power Save Plus Mode (the “Mode”) is in effect, endpoints that are configured for the mode are disabled for emergency
                                                         calling and from receiving inbound calls. By selecting this mode, you agree to the following: (i) You take full responsibility
                                                         for providing alternate methods for emergency calling and receiving calls while the mode is in effect; (ii) Cisco has no liability
                                                         in connection with your selection of the mode and all liability in connection with enabling the mode is your responsibility;
                                                         and (iii) You fully inform users of the effects of the mode on calls, calling and otherwise. To disable Power Save Plus, you must uncheck the Allow EnergyWise Overrides check box. If the Allow EnergyWise Overrides remains
                                             checked but no days are selected in the Enable Power Save Plus field, Power Save Plus is not disabled. | Caution | While Power Save Plus Mode (the “Mode”) is in effect, endpoints that are configured for the mode are disabled for emergency
                                                         calling and from receiving inbound calls. By selecting this mode, you agree to the following: (i) You take full responsibility
                                                         for providing alternate methods for emergency calling and receiving calls while the mode is in effect; (ii) Cisco has no liability
                                                         in connection with your selection of the mode and all liability in connection with enabling the mode is your responsibility;
                                                         and (iii) You fully inform users of the effects of the mode on calls, calling and otherwise. |
| Caution | While Power Save Plus Mode (the “Mode”) is in effect, endpoints that are configured for the mode are disabled for emergency
                                                         calling and from receiving inbound calls. By selecting this mode, you agree to the following: (i) You take full responsibility
                                                         for providing alternate methods for emergency calling and receiving calls while the mode is in effect; (ii) Cisco has no liability
                                                         in connection with your selection of the mode and all liability in connection with enabling the mode is your responsibility;
                                                         and (iii) You fully inform users of the effects of the mode on calls, calling and otherwise. |
| Phone On Time | hh:mm |  | Determines when the phone automatically turns on for the days that are in the Enable Power Save Plus field. Enter the time in this field in 24-hour format, where 00:00 is midnight. For example, to automatically power up the phone at 07:00 a.m. (0700), enter 07:00. To power up the phone at 02:00 p.m. (1400),
                                             enter 14:00. The default value is blank, which means 00:00. The Phone On Time must be at least 20 minutes later than the Phone Off Time. For example, if the Phone Off Time is 07:00,
                                             the Phone On Time must be no earlier than 07:20. |
| Phone Off Time | hh:mm |  | Identifies the time of day that the phone powers down for the days that are selected in the Enable Power Save Plus field.
                                             If the Phone On Time and the Phone Off Time fields contain the same value, the phone does not power down. Enter the time in this field in 24-hour format, where 00:00 is midnight. For example, to automatically power down the phone at 7:00 a.m. (0700), enter 7:00. To power down the phone at 2:00 p.m. (1400),
                                             enter 14:00. The default value is blank, which means 00:00. The Phone On Time must be at least 20 minutes later than the Phone Off Time. For example, if the Phone Off Time is 7:00, the
                                             Phone On Time must be no earlier than 7:20. |
| Phone Off Idle Timeout | 20 to 1440 minutes | 60 | Indicates the length of time that the phone must be idle before the phone powers down. The timeout occurs under the following conditions: When the phone was in Power Save Plus mode, as scheduled, and was taken out of Power Save Plus mode because the phone user
                                                   pressed the Select key. When the phone is repowered by the attached switch. When the Phone Off Time is reached but the phone is in use. |
| Enable Audible Alert | Check box | Unchecked | When enabled, instructs the phone to play an audible alert starting 10 minutes before the time that the Phone Off Time field
                                             specifies. This check box applies only if the Enable Power Save Plus list box has one or more days selected. |
| EnergyWise Domain | Up to 127 characters |  | Identifies the EnergyWise domain that the phone is in. |
| EnergyWise Secret | Up to 127 characters |  | Identifies the security secret password that is used to communicate with the endpoints in the EnergyWise domain. |
| Allow EnergyWise Overrides | Check box | Unchecked | Determines whether you allow the EnergyWise domain controller policy to send power level updates to the phones. The following
                                             conditions apply: One or more days must be selected in the Enable Power Save Plus field. The settings in Cisco Unified Communications Manager Administration take effect on schedule even if EnergyWise sends an override. For example, assuming the Phone Off Time is set to 22:00 (10:00 p.m.), the value in the Phone On Time field is 06:00 (6:00
                                             a.m.), and the Enable Power Save Plus has one or more days selected. If EnergyWise directs the phone to turn off at 20:00 (8:00 p.m.), that directive remains in effect (assuming no phone user
                                                   intervention occurs) until the configured Phone On Time at 6:00 a.m. At 6:00 a.m., the phone turns on and resumes receiving the power level changes from the settings in Cisco Unified Communications
                                                   Manager Administration. To change the power level on the phone again, EnergyWise must reissue a new power level change command. To disable Power Save Plus, you must uncheck the Allow EnergyWise Overrides check box. If the Allow EnergyWise Overrides remains
                                             checked but no days are selected in the Enable Power Save Plus field, Power Save Plus is not disabled. |
| Join and Direct Transfer Policy | Same line, across line enable Same line enable only Same line, across line disable | Same line, across line enable | Controls the ability of a user to join and transfer calls. Same line, across line enable—Users can directly transfer or join a call on current line to another call on another line. Same line enable only—Users can only directly transfer or join the calls when both calls are on same line. Same line, across line disable— Users can't join or transfer calls on the same line. The join and transfer features are disabled
                                                   and the user can't do the direct transfer or join function. |
| Span to PC Port | Disabled Enabled | Disabled | Indicates whether the phone forwards packets that are transmitted and received on the network port to the access port. |
| Recording Tone | Disabled Enabled | Disabled | Controls the playing of the tone when a user is recording a call. |
| Recording Tone Local Volume | Integer 0–100 | 100 | Controls the volume of the recording tone to the local user. |
| Recording Tone Remote Volume | Integer 0–100 | 50 | Controls the volume of the recording tone to the remote user. |
| Recording Tone Duration | Integer 1–3000 milliseconds |  | Controls the duration of the recording tone. |
| Log Server | String of up to 256 characters |  | Identifies the IPv4 syslog server for phone debug output. The format for the address is: address:<port>@@base=<0-7>;pfs=<0-1> |
| Cisco Discovery Protocol (CDP): Switch Port | Disabled Enabled | Enabled | Controls Cisco Discovery Protocol on the SW port of the phone. |
| Cisco Discovery Protocol (CDP): PC Port | Disabled Enabled | Enabled | Controls Cisco Discovery Protocol on the PC port of the phone. |
| Link Layer Discovery Protocol - Media Endpoint Discover (LLDP-MED): Switch Port | Disabled Enabled | Enabled | Enables LLDP-MED on the SW port. |
| Link Layer Discovery Protocol (LLDP): PC Port | Disabled Enabled | Enabled | Enables LLDP on the PC port. |
| LLDP Asset ID | String, up to 32 characters |  | Identifies the asset ID that is assigned to the phone for inventory management. |
| LLDP Power Priority | Unknown Low High Critical | Unknown | Assigns a phone power priority to the switch, thus enabling the switch to appropriately provide power to the phones. |
| 802.1x Authentication | User Controlled Enabled Disabled | User Controlled | Specifies the 802.1x authentication feature status. User Controlled—The user can configure the 802.1x on the phone. Disabled—802.1x Authentication is not used. Enabled—802.1x authentication is used, and you configure the authentication for the phones. |
| Automatic Port Synchronization | Disabled Enabled | Disabled | Synchronizes ports to the lowest speed between ports of a phone to eliminate packet loss. |
| Switch Port Remote Configuration | Disabled Enabled | Disabled | Allows you to configure the speed and duplex function of the phone SW port remotely. This enhances the performance for large
                                             deployments with specific port settings. If the SW ports are configured for Remote Port Configuration in Cisco Unified Communications Manager, the data cannot be changed
                                             on the phone. |
| PC Port Remote Configuration | Disabled Enabled | Disabled | Allows you to configure the speed and duplex function of the phone PC port remotely. This enhances the performance for large
                                             deployments with specific port settings. If the ports are configured for Remote Port Configuration in Cisco Unified Communications Manager, the data cannot be changed
                                             on the phone. |
| SSH Access | Disabled Enabled | Disabled | Controls the access to the SSH daemon through port 22. Leaving port 22 open leaves the phone vulnerable to Denial of Service
                                             (DoS) attacks. |
| Incoming Call Toast Timer | 0, 3, 4, 5, 6, 7, 8, 9, 10, 15, 30, 60 | 5 | Gives the time, in seconds, that the toast displays. The time includes the fade-in and fade-out times for the window. 0 means that the incoming call toast is disabled. |
| Ring Locale | Default Japan | Default | Controls the ringing pattern. |
| TLS Resumption Timer | Integer 0–3600 seconds | 3600 | Controls the ability to resume a TLS session without repeating the entire TLS authentication process. If the field is set
                                             to 0, then the TLS session resumption is disabled. |
| FIPS Mode | Disabled Enabled | Disabled | Enables or disables the Federal Information Processing Standards (FIPS) mode on the phone. |
| Record Call Log from Shared Line | Disabled Enabled | Disabled | Specifies whether to record a shared line call in the call log. |
| Minimum Ring Volume | 0-Silent 1–15 | 0-Silent | Controls the minimum ring volume for the phone. You can set a phone so that the ringer cannot be turned off. |
| Peer Firmware Sharing | Disabled Enabled | Enabled | Allows the phone to find other phones of the same model on the subnet and share updated firmware files. If the phone has a
                                             new firmware load, it can share that load with the other phones. If one of the other phones has a new firmware load, the phone
                                             can download the firmware from the other phone, instead of from the TFTP server. Peer firmware sharing: Limits congestion on TFTP transfers to centralized remove TFTP servers. Eliminates the need to manually control firmware upgrades. Reduces phone downtime during upgrades when large numbers of phones are reset simultaneously. Helps with firmware upgrades in branch or remote office deployment scenarios that run over bandwidth-limited WAN links. |
| Load Server | String of up to 256 characters |  | Identifies the alternate IPv4 server that the phone uses to obtain firmware loads and upgrades. The format for the address is: address:<port>@@base=<0-7>;pfs=<0-1> |
| IPv6 Load Server | String of up to 256 characters |  | Identifies the alternate IPv6 server that the phone uses to obtain firmware loads and upgrades. The format for the address is: [address]:<port>@@base=<0-7>;pfs=<0-1> |
| Wideband Headset UI Control | Disabled Enabled | Enabled | Allows the user to use the wideband codec for an analog headset. |
| Wideband Headset | Disabled Enabled | Enabled | Enables or disables the use of a Wideband Headset on the phone. Used in conjunction with User Control Wideband Headset. For more information, see Set Up Wideband Codec . |
| Wi-Fi | Disabled Enabled | Enabled | Enables the Cisco IP Phones 8861 and 8865 to connect to the Wi-Fi network. Phones that do not support this feature do not display the field. |
| Back USB Port | Disabled Enabled | 8861, 8865, and 8865NR: Enabled | Controls the ability to use the USB port on the back of the Cisco IP Phones 8861 and 8865. Phones that do not support this feature do not display the field. |
| Side USB Port | Disabled Enabled | Enabled | Controls the ability to use the USB port on the side of the Cisco IP Phones 8851, 8851NR, 8861, 8865, and 8865NR. Phones that do not support this feature do not display the field. |
| Console Access | Disabled Enabled | Disabled | Specifies whether the serial console is enabled or disabled. |
| Bluetooth | Disabled Enabled | Enabled | Enables or disables the Bluetooth option on the phone. If disabled, the user cannot enable Bluetooth on the phone. Supported
                                             on the Cisco IP Phones 8845, 8851, 8861, and 8865. Phones that do not support this feature do not display the field. |
| Allow Bluetooth Contacts Import | Disabled Enabled | Enabled | Enables the user to import contacts from their connected mobile device using Bluetooth. When disabled, the user cannot import
                                             contacts from their connected mobile device on their phone. Supported on the Cisco IP Phones 8845, 8851, 8861, and 8865. Phones that do not support this feature do not display the field. |
| Allow Bluetooth Mobile Handsfree Mode | Disabled Enabled | Enabled | Enables users to take advantage of the acoustic properties of the phone with their mobile device or tablet. The user pairs
                                             the mobile device or tablet to the phone using Bluetooth. When disabled, the user cannot pair the mobile device or tablet
                                             with their phone. With a mobile device paired, the user can place and receive mobile calls on the phone. With a tablet, the user can route the
                                             audio from the tablet to the phone. Users can pair multiple mobile devices, tablets, and a Bluetooth headset to the phone. However, only one device and one headset
                                             can be connected at the same time. Phones that do not support this feature do not display the field. |
| Bluetooth Profiles | Handsfree Human Interface Device | Handsfree | Indicates which Bluetooth profiles on the phone are enabled or disabled. Phones that do not support this feature do not display the field. |
| Gratuitous ARP | Disabled Enabled | Disabled | Enables or disables the ability for the phone to learn MAC addresses from Gratuitous ARP. This capability is required to monitor
                                             or record voice streams. |
| Show All Calls on Primary Line | Disabled Enabled | Disabled | Specifies if all calls presented to this phone will be shown on the primary line or not. The purpose of this field is to make it easier for the end user to see all calls on all lines at a glance rather than having
                                             to choose a line to see the calls on that line. In other words, when multiple lines are configured on the phone, it typically
                                             makes more sense to be able to see all the calls on all lines in one combined display. When this feature is enabled, all calls
                                             will be shown on the primary line, but you can still choose a specific line to filter the display to show only the calls for
                                             that specific line. |
| HTTPS Server | HTTP and HTTPS enabled HTTPS only | HTTP and HTTPS enabled | Controls the type of communication to the phone. If you select HTTPS only, phone communication is more secure. |
| IPv6 Log Server | String of up to 256 characters |  | Identifies the IPv6 log server. The format for the address is: [address]:<port>@@base=<0-7>;pfs=<0-1> |
| Remote Log | Disabled Enabled | Disabled | Controls the ability to send logs to the syslog server. |
| Log Profile | Default Preset Telephony SIP UI Network Media Upgrade Accessory Security Wi-Fi VPN Energywise MobileRemoteAc | Preset | Specifies the predefined logging profile. Default—Default debug logging level Preset—Does not overwrite the phone local debug logging setting Telephony—Logs information about Telephony or call features SIP—Logs information about SIP signaling UI—Logs information about the phone user interface Network—Logs network information Media—Logs media information Upgrade—Logs upgrade information Accessory—Logs accessory information Security—Logs security information Wi-Fi—Logs Wi-Fi information VPN—Logs virtual private network information Energywise—Logs energy-savings information MobileRemoteAC—Logs Mobile and Remote Access through Expressway information |
| Advertise G.722 and iSAC Codecs | Use System Default Disabled Enabled | Use System Default | Indicates whether the phone advertises the G.722 and iSAC codecs to the Cisco Unified Communications Manager. Use System Default—Defers to the setting specified in the enterprise parameter Advertise G.722 Codec. Disabled—Does not advertise G.722 to the Cisco Unified Communications Manager. Enabled—Advertises G.722 to the Cisco Unified Communications Manager. For more information, see the note that follows the table. |
| Detect Unified CM Connection Failure | Normal Delayed | Normal | Determines the sensitivity that the phone has for detecting a connection failure to Cisco Unified Communications Manager
                                             (Unified CM), which is the first step before device failover to a backup Unified CM/SRST occurs. Normal—Detection of a Unified CM connection failure occurs at the standard system rate. Choose this value for faster recognition
                                                   of a Unified CM connection failure. Delayed—Detection of a Unified CM connection failover occurs approximately four times slower than Normal. Choose this value
                                                   if you prefer failover to be delayed slightly to give the connection the opportunity to reestablish The precise time difference between Normal and Delayed connection failure detection depends on many variables that are constantly
                                             changing. This field only applies to the wired Ethernet connection. |
| Power Negotiation | Disabled Enabled | Enabled | Allows the phone to negotiate power using Link Level Endpoint Discovery Protocol (LLDP) and Cisco Discovery Protocol (CDP). Power Negotiation should not be disabled when the phone is connected to a switch that supports power negotiation. If disabled,
                                             the switch could shut off power to the phone. |
| Provide Dial Tone from Release Button | Disabled Enabled | Disabled | Controls whether the user hears dial tone when the Release key is pressed. Disabled—User doesn't hear dial tone. Enabled—User hears dial tone. |
| Background Image | String up to 64 characters |  | Specifies the default wallpaper file. When a default wallpaper is set, the user can't change the phone wallpaper. |
| Simplified New Call UI | Disabled Enabled | Disabled | Controls the user interface for off-hook dialing. When enabled, the user cannot select a number from the recent calls list. When enabled, this field provides a simplified window for the user to place a call. The user does not see the call history
                                             pop-up window that is displayed when the phone is taken off-hook. The pop-up window display is considered useful, so Simplified
                                             New Call UI is disabled by default. |
| Revert to All Calls | Disabled Enabled | Disabled | Specifies whether the phone will revert to All Calls after any call ends or not if the call is on a filter other than Primary
                                             line, All Calls, or Alerting Calls. |
| Show Call History for Selected Line Only | Disabled Enabled | Disabled | Controls the display of the Recents list. Disabled—The Recents list shows the call history for all lines. Enabled—The Recents list shows the call history for the selected line. |
| Actionable Incoming Call Alert | Disabled Show for all Incoming Call Show for Invisible Incoming Call | Show for all Incoming Call | Controls the type of incoming call alert that displays on the phone screen. The purpose of this field is to reduce the number
                                             of button presses that the end user requires to answer a call. Disabled—The actionable incoming call alert is disabled and the user sees the traditional incoming call pop-up alert. Show for all Incoming Call—The actionable incoming call alert displays for all calls regardless of visibility. Show for Invisible Incoming Call—The actionable incoming call alert displays for calls not shown on the phone. This parameter
                                                   behaves similarly to the incoming call alert pop-up notification. |
| DF bit | 0 1 | 0 | Controls how network packets are sent. Packets can be sent in chunks (fragments) of various sizes. When the DF bit is set to 1 in the packet header, the network payload does not fragment when going through network devices,
                                             such as switches and routers. Removing fragmenting avoids incorrect parsing on the receiving side, but results in slightly
                                             slower speeds. The DF bit setting does not apply to ICMP, VPN, VXC VPN, or DHCP traffic. |
| Default Line Filter | List of comma-separated phone device names |  | Indicates the list of phones that are in the default filter. When the default line filter is configured, users see a filter named Daily schedule in Call notifications in the Settings > Preferences menu of the phone. This daily schedule filter is in addition to the preset All Calls filter. If the default line filter is not configured, the phone checks all provisioned lines. If configured, the phone checks the
                                             lines set on Cisco Unified Communications Manager if the user selects Default filter as the active filter, or if there are
                                             no custom filters. Custom line filters enable you to filter on high-priority lines to reduce alert activity. You can set the alerting call notification
                                             priority on a subset of lines covered by an alert filter. The custom filter generates either traditional pop-up alerts or
                                             actionable alerts for incoming calls on the selected lines. For each filter, only the covered subset of lines will generate
                                             an alert. This feature provides a way for users with multiple lines to reduce alert activity by filtering and displaying alerts
                                             only from high-priority lines. The end users can configure this themselves. Alternatively, you can program the default line
                                             filter and push the filter down to the phone. |
| Lowest Alerting Line State Priority | Disabled Enabled | Disabled | Specifies the alert state when using shared lines. Disabled—When there is an incoming call alerting on the shared line, the LED/Line state icon reflects the alerting state instead
                                                   of Remote-In-Use. Enabled—When there is an incoming call alerting on the shared line, the user sees the Remote-In-Use icon. |
| One Column Display for KEM | Disabled Enabled | Disabled | Controls the display on the Key Expansion Module. Disabled—The expansion module uses two-column mode. Enabled—The expansion module uses one-column mode. Phones that do not support this feature do not display the field. |
| Energy Efficient Ethernet (EEE): PC Port | Disabled Enabled | Disabled | Controls EEE on the PC port. |
| Energy Efficient Ethernet (EEE): SW Port | Disabled Enabled | Disabled | Controls EEE on the switch port. |
| Start Video Port |  |  | Defines the start of the port range for video calls. Phones that do not support this feature do not display the field. |
| Stop Video Port |  |  | Defines the end of the port range for video calls. Phones that do not support this feature do not display the field. |
| User Credentials Persistent for Expressway Sign in | Disabled Enabled | Disabled | Controls if the phone stores the users' sign-in credentials. When disabled, the user is always sees the prompt to sign into
                                             the Expressway server for Mobile and Remote Access (MRA). If you would like to make it easier for users to log in, you enable this field so that the Expressway login credentials are
                                             persistent. The user then only has to enter their login credentials the first time. Any time after that (when the phone is
                                             powered on off-premise), the login information is prepopulated on the Sign-in screen. For more information, see the Mobile and Remote Access Through Expressway . |
| Customer support upload URL | String, up to 256 characters |  | Provides the URL for the Problem Report Tool (PRT). If you deploy devices with Mobile and Remote Access through Expressway, you must also add the PRT server address to the HTTP
                                             Server Allow list on the Expressway server. For more information, see the Mobile and Remote Access Through Expressway . |
| Web Admin | Disabled Enabled | Disabled | Enables or disables administrator access to the phone web pages through a web browser For more information, see the Configure the Administration Page for Phone . Phones that do not support this feature do not display the field. |
| Admin Password | String of 8–127 characters |  | Defines the administrator password when you access the phone web pages as an administrator. Phones that do not support this feature do not display the field. |
| WLAN SCEP Server | String of up to 256 characters |  | Specifies the SCEP Server that the phone uses to obtain certificates for WLAN authentication. Enter the hostname or the IP
                                             address (using standard IP addressing format) of the server. Phones that do not support this feature do not display the field. |
| WLAN Root CA Fingerprint (SHA256 or SHA1) | String of up to 95 characters |  | Specifies the SHA256 or SHA1 fingerprint of the Root CA to use for validation during the SCEP process when issuing certificates
                                             for WLAN authentication. We recommend that you use the SHA256 fingerprint, which can be obtained via OpenSSL (e.g. openssl
                                             x509 -in rootca.cer -noout -sha256 -fingerprint) or using a Web Browser to inspect the certificate details. Enter the 64 hexadecimal character value for the SHA256 fingerprint or the 40 hexadecimal character value for the SHA1 fingerprint
                                             with a common separator (colon, dash, period, space) or without a separator. If using a separator, then the separator should
                                             be consistently placed after every 2, 4, 8, 16, or 32 hexadecimal characters for a SHA256 fingerprint or every 2, 4, or 8
                                             hexadecimal characters for a SHA1 fingerprint. Phones that do not support this feature do not display the field. |
| WLAN Authentication Attempts |  |  | Phones that do not support this feature do not display the field. |
| WLAN Profile 1 Prompt Mode | Disabled Enabled | Disabled | Phones that do not support this feature do not display the field. |
| Conference with Active Call in Enhanced line mode | Disabled Enabled | Disabled | Disabled—The calls in the Active Calls list cannot be filtered by line, and users cannot directly add another person to a
                                                   conference by simply pressing a line key. If there are quite a few calls on the phones, users have to repeatedly press the
                                                   Navigation Cluster button in the calls list to navigate to the target calls. Enabled—Enhances the user experience to add another person to a conference call. This feature can reduce the steps to find
                                                   the target calls for the users. If each line has only one call on the phone, users can directly press the line key to add the call on a line to the conference
                                                   call. If each line has multiple calls on the phone, users can press a line key to only show the calls filtered by the line. Then
                                                   they can quickly navigate to the target calls that will be added to the conference call. This feature is only available when the "Line Mode" is set to "Enhanced Line Mode". |
| Line Mode | Session Line Mode Enhanced Line Mode | Session Line Mode | Controls the line display on the phone. Session Line Mode—The buttons on one side of the screen are line keys. Enhanced Line Mode—The buttons on both sides of the phone screen are line keys. Predictive dialing and Actionable incoming
                                                   call alerts are enabled by default in Enhanced line mode. |
| Admin Configurable Ringer | Disabled Sunrise Chirp1 Chirp2 | Disabled | Works with "Allow Ringtone Change Through Phone Menu" to control the ringtone and the ability for users to set the ringtone. If set to Disabled, the administrator's setting of the default ringtone is disabled. In this case, users can always change
                                             a ringtone on their phones no matter whether the "Allow Ringtone Change Through Phone Menu" parameter value is Disabled or
                                             Enabled. If set to a value other than Disabled, the user's permission of changing a ringtone on the phone depends on the value of "Allow
                                             Ringtone Change Through Phone Menu": Disabled—Users cannot change the ringtone. In this situation, the Ringtone menu item in the Settings menu is grayed out. Enabled—Users can change the ringtone on the phone. |
| Allow Ringtone Change Through Phone Menu | Disabled Enabled | Disabled | Works with "Admin Configurable Ringer" to control the ability for users to set the ringtone. The user's choice of ringtone takes precedence over the default ringtone set the administrators. If you still want to change
                                             the ringtone, do the following: Set the parameter to Disabled, and save to apply the change. Change the default ringtone in "Admin Configurable Ringer", and save to apply the change. Then the ringtone on the phone will
                                                   be reset to the default ringtone. |
| Customer Support Use | String of up to 64 characters | Empty | For Cisco TAC use only. |
| Disable TLS Ciphers | See Disable Transport Layer Security Ciphers . | None | Disables the selected TLS cipher. Disable more than one cipher suite by selecting and holding the Ctrl key on your computer keyboard. If you select all of the phone ciphers, then phone TLS service is impacted. |
| Lower Your Voice Alert | Enabled Disabled | Enabled | Controls the Lower your voice feature. Disabled: The phone doesn't display the Lower
                                                            												your voice menu item in the Settings menu. Users won't see the message on their screen when
                                                         												they speak loudly. Enabled: Users control the feature from the Lower your voice menu item
                                                         												in the Settings menu. By
                                                         												default, the field is set to On . |
| Mark Call As Spam | Enabled Disabled | Enabled | Controls the Mark call as spam feature. Disabled: The phone doesn't display the Mark
                                                            												spam softkey. The Spam list item in the Settings menu doesn't
                                                         												display. If there was a spam list, the list is cleared and
                                                         												can't be recovered. Enabled: The phone displays the Mark
                                                            												spam softkey. The Spam list item in the Settings menu displays. |
| Dedicate one line for Call Park | Disabled Enabled | Enabled | Controls whether a parked call occupies one line or not. For more information, see the Cisco Unified Communications
                                             									Manager documentation. |
| Line Text Label Display in ELM | Disabled Enabled | Enabled | Controls the line label display during a call when Enhanced Line Mode is configured Enabled If the caller's name is configured, it displays the name in the first line of the call session and the local line label in
                                                         the second line. If the caller's name is not configured, it displays the remote number in the first line and the local line label in the second
                                                         line. Disabled If the caller’s name is configured, it displays the name in the first line of the call session and number in the second line. If the caller's name is not configured, it displays only the remote number. This field is required. |

| Caution | If you enable this field, you may expose sensitive
                                                         										information about the phone. |
|---|---|

| Note | This parameter is unavailable for the wireless networks. |
|---|---|

| Caution | While Power Save Plus Mode (the “Mode”) is in effect, endpoints that are configured for the mode are disabled for emergency
                                                         calling and from receiving inbound calls. By selecting this mode, you agree to the following: (i) You take full responsibility
                                                         for providing alternate methods for emergency calling and receiving calls while the mode is in effect; (ii) Cisco has no liability
                                                         in connection with your selection of the mode and all liability in connection with enabling the mode is your responsibility;
                                                         and (iii) You fully inform users of the effects of the mode on calls, calling and otherwise. |
|---|---|

| Note | Codec negotiation involves two steps: The phone advertises the supported codec to the Cisco Unified Communications Manager. Not all endpoints support the same set
                                                   of codecs. When the Cisco Unified Communications Manager gets the list of supported codecs from all phones involved in the call attempt,
                                                   it chooses a commonly supported codec based on various factors, including the region pair setting. |
|---|---|

| Field | Administration Area | Recommended Setting |
|---|---|---|
| Always Use Prime Line | Device Information | Off or On For more information, see Field: Always Use Prime Line . |
| Actionable Incoming Call Alert | Product Specific Configuration Layout | Show for all Incoming Call |
| Show All Calls on Primary Line | Product Specific Configuration Layout | Enabled |
| Revert to All Calls | Product Specific Configuration Layout | Enabled |

| Field | Administration Area | Recommended Setting |
|---|---|---|
| Always Use Prime Line | Device Information | Off For more information, see Field: Always Use Prime Line . |
| Actionable Incoming Call Alert | Product Specific Configuration Layout | Show for all Incoming Call |
| Show All Calls on Primary Line | Product Specific Configuration Layout | Enabled |
| Revert to All Calls | Product Specific Configuration Layout | Enabled |

| Field | Administration Area | Recommended Setting for Session Line Mode |
|---|---|---|
| Show All Calls on Primary Line | Product Specific Configuration Layout | Disabled |
| Revert to All Calls | Product Specific Configuration Layout | Disabled |
| Actionable Incoming Call Alert | Product Specific Configuration Layout | Enabled by default (Firmware Release 11.5(1) and later). |

| Step 1 | In Cisco Unified Communications Manager Administration, select Device > Phone . |
|---|---|
| Step 2 | Locate the phone to be configured. |
| Step 3 | Navigate to the Record Call Log from Shared Line drop-down in the Product Specific Configuration area. |
| Step 4 | Select Enabled from the drop-down list. |
| Step 5 | Select Save . |

| Step 1 | In Cisco Unified Communications Manager Administration, select Device > Phone . |
|---|---|
| Step 2 | Locate the phone that you need to set up. |
| Step 3 | Navigate to the Product Specific Configuration area and set the following fields: Days Display Not Active Display On Time Display On Duration Display Idle Timeout Table 3. PowerSave Configuration Fields Field Description Days Display Not Active Days that the display does not turn on automatically at the time specified in the Display On Time field. Choose the day or days from the drop-down list. To choose more than one day, Ctrl-click each day that you want. Display On Time Time each day that the display turns on automatically (except on the days specified in the Days Display Not Active field). Enter the time in this field in 24-hour format, where 0:00 is midnight. For example, to automatically turn the display on at 07:00a.m., (0700), enter 07:00 . To turn the display on at 02:00p.m. (1400), enter 14:00 . If this field is blank, the display will automatically turn on at 0:00. Display On Duration Length of time that the display remains on after turning on at the time specified in the Display On Time field. Enter the value in this field in the format hours:minutes . For example, to keep the display on for 4 hours and 30 minutes after it turns on automatically, enter 04:30 . If this field is blank, the phone will turn off at the end of the day (0:00). Note If Display On Time is 0:00 and the display on duration is blank (or 24:00), the display will remain on continuously. Display Idle Timeout Length of time that the phone is idle before the display turns off. Applies only when the display was off as scheduled and
                                                         was turned on by a user (by pressing a button on the phone or lifting the handset). Enter the value in this field in the format hours:minutes . For example, to turn the display off when the phone is idle for 1 hour and 30 minutes after a user turns the display on, enter 01:30 . The default value is 01:00. | Field | Description | Days Display Not Active | Days that the display does not turn on automatically at the time specified in the Display On Time field. Choose the day or days from the drop-down list. To choose more than one day, Ctrl-click each day that you want. | Display On Time | Time each day that the display turns on automatically (except on the days specified in the Days Display Not Active field). Enter the time in this field in 24-hour format, where 0:00 is midnight. For example, to automatically turn the display on at 07:00a.m., (0700), enter 07:00 . To turn the display on at 02:00p.m. (1400), enter 14:00 . If this field is blank, the display will automatically turn on at 0:00. | Display On Duration | Length of time that the display remains on after turning on at the time specified in the Display On Time field. Enter the value in this field in the format hours:minutes . For example, to keep the display on for 4 hours and 30 minutes after it turns on automatically, enter 04:30 . If this field is blank, the phone will turn off at the end of the day (0:00). Note If Display On Time is 0:00 and the display on duration is blank (or 24:00), the display will remain on continuously. | Note | If Display On Time is 0:00 and the display on duration is blank (or 24:00), the display will remain on continuously. | Display Idle Timeout | Length of time that the phone is idle before the display turns off. Applies only when the display was off as scheduled and
                                                         was turned on by a user (by pressing a button on the phone or lifting the handset). Enter the value in this field in the format hours:minutes . For example, to turn the display off when the phone is idle for 1 hour and 30 minutes after a user turns the display on, enter 01:30 . The default value is 01:00. |
| Field | Description |
| Days Display Not Active | Days that the display does not turn on automatically at the time specified in the Display On Time field. Choose the day or days from the drop-down list. To choose more than one day, Ctrl-click each day that you want. |
| Display On Time | Time each day that the display turns on automatically (except on the days specified in the Days Display Not Active field). Enter the time in this field in 24-hour format, where 0:00 is midnight. For example, to automatically turn the display on at 07:00a.m., (0700), enter 07:00 . To turn the display on at 02:00p.m. (1400), enter 14:00 . If this field is blank, the display will automatically turn on at 0:00. |
| Display On Duration | Length of time that the display remains on after turning on at the time specified in the Display On Time field. Enter the value in this field in the format hours:minutes . For example, to keep the display on for 4 hours and 30 minutes after it turns on automatically, enter 04:30 . If this field is blank, the phone will turn off at the end of the day (0:00). Note If Display On Time is 0:00 and the display on duration is blank (or 24:00), the display will remain on continuously. | Note | If Display On Time is 0:00 and the display on duration is blank (or 24:00), the display will remain on continuously. |
| Note | If Display On Time is 0:00 and the display on duration is blank (or 24:00), the display will remain on continuously. |
| Display Idle Timeout | Length of time that the phone is idle before the display turns off. Applies only when the display was off as scheduled and
                                                         was turned on by a user (by pressing a button on the phone or lifting the handset). Enter the value in this field in the format hours:minutes . For example, to turn the display off when the phone is idle for 1 hour and 30 minutes after a user turns the display on, enter 01:30 . The default value is 01:00. |
| Step 4 | Select Save . |
| Step 5 | Select Apply Config . |
| Step 6 | Restart the phone. |

| Field | Description |
|---|---|
| Days Display Not Active | Days that the display does not turn on automatically at the time specified in the Display On Time field. Choose the day or days from the drop-down list. To choose more than one day, Ctrl-click each day that you want. |
| Display On Time | Time each day that the display turns on automatically (except on the days specified in the Days Display Not Active field). Enter the time in this field in 24-hour format, where 0:00 is midnight. For example, to automatically turn the display on at 07:00a.m., (0700), enter 07:00 . To turn the display on at 02:00p.m. (1400), enter 14:00 . If this field is blank, the display will automatically turn on at 0:00. |
| Display On Duration | Length of time that the display remains on after turning on at the time specified in the Display On Time field. Enter the value in this field in the format hours:minutes . For example, to keep the display on for 4 hours and 30 minutes after it turns on automatically, enter 04:30 . If this field is blank, the phone will turn off at the end of the day (0:00). Note If Display On Time is 0:00 and the display on duration is blank (or 24:00), the display will remain on continuously. | Note | If Display On Time is 0:00 and the display on duration is blank (or 24:00), the display will remain on continuously. |
| Note | If Display On Time is 0:00 and the display on duration is blank (or 24:00), the display will remain on continuously. |
| Display Idle Timeout | Length of time that the phone is idle before the display turns off. Applies only when the display was off as scheduled and
                                                         was turned on by a user (by pressing a button on the phone or lifting the handset). Enter the value in this field in the format hours:minutes . For example, to turn the display off when the phone is idle for 1 hour and 30 minutes after a user turns the display on, enter 01:30 . The default value is 01:00. |

| Note | If Display On Time is 0:00 and the display on duration is blank (or 24:00), the display will remain on continuously. |
|---|---|

| Step 1 | From the Cisco Unified Communications Manager Administration, select Device > Phone . |
|---|---|
| Step 2 | Locate the phone that you need to set up. |
| Step 3 | Navigate to the Product Specific Configuration area and set the following fields. Enable Power Save Plus Phone On Time Phone Off Time Phone Off Idle Timeout Enable Audible Alert EnergyWise Domain EnergyWise Secret Allow EnergyWise Overrides Table 4. EnergyWise Configuration Fields Field Description Enable Power Save Plus Selects the schedule of days for which the phone powers off. Select multiple days by pressing and holding the Control key
                                                         while clicking on the days for the schedule. By default, no days are selected. When Enable Power Save Plus is checked, you receive a message that warns about emergency (e911) concerns. Caution While Power Save Plus Mode (the "Mode" ) is in effect, endpoints that are configured for the mode are disabled for emergency calling and from receiving inbound calls.
                                                                     By selecting this mode, you agree to the following: (i) You take full responsibility for providing alternate methods for emergency
                                                                     calling and receiving calls while the mode is in effect; (ii) Cisco has no liability in connection with your selection of
                                                                     the mode and all liability in connection with enabling the mode is your responsibility; and (iii) You fully inform users of
                                                                     the effects of the mode on calls, calling and otherwise. Note To disable Power Save Plus, you must uncheck the Allow EnergyWise Overrides check box. If the Allow EnergyWise Overrides remains
                                                                     checked but no days are selected in the Enable Power Save Plus field, Power Save Plus is not disabled. Phone On Time Determines when the phone automatically turns on for the days that are in the Enable Power Save Plus field. Enter the time in this field in 24-hour format, where 00:00 is midnight. For example, to automatically power up the phone at 07:00 a.m. (0700), enter 07:00. To power up the phone at 02:00 p.m. (1400),
                                                         enter 14:00. The default value is blank, which means 00:00. Note The Phone On Time must be at least 20 minutes later than the Phone Off Time. For example, if the Phone Off Time is 07:00,
                                                                     the Phone On Time must be no earlier than 07:20. Phone Off Time The time of day that the phone powers down for the days that are selected in the Enable Power Save Plus field. If the Phone
                                                         On Time and the Phone Off Time fields contain the same value, the phone does not power down. Enter the time in this field in 24-hour format, where 00:00 is midnight. For example, to automatically power down the phone at 7:00 a.m. (0700), enter 7:00. To power down the phone at 2:00 p.m. (1400),
                                                         enter 14:00. The default value is blank, which means 00:00. Note The Phone On Time must be at least 20 minutes later than the Phone Off Time. For example, if the Phone Off Time is 7:00, the
                                                                     Phone On Time must be no earlier than 7:20. Phone Off Idle Timeout The length of time that the phone must be idle before the phone powers down. The timeout occurs under the following conditions: When the phone was in Power Save Plus mode, as scheduled, and was taken out of Power Save Plus mode because the phone user
                                                               pressed the Select key. When the phone is repowered by the attached switch. When the Phone Off Time is reached but the phone is in use. The range of the field is 20 to 1440 minutes. The default value is 60 minutes. Enable Audible Alert When enabled, instructs the phone to play an audible alert starting 10 minutes before the time that the Phone Off Time field
                                                         specifies. The audible alert uses the phone ringtone, which briefly plays at specific times during the 10-minute alerting period. The
                                                         alerting ringtone plays at the user-designated volume level. The audible alert schedule is: At 10 minutes before power down, play the ringtone four times. At 7 minutes before power down, play the ringtone four times. At 4 minutes before power down, play the ringtone four times. At 30 seconds before power down, play the ringtone 15 times or until the phone powers off. This check box applies only if the Enable Power Save Plus list box has one or more days selected. EnergyWise Domain The EnergyWise domain that the phone is in. The maximum length of this field is 127 characters. EnergyWise Secret The security secret password that is used to communicate with the endpoints in the EnergyWise domain. The maximum length of this field is 127 characters. Allow EnergyWise Overrides This check box determines whether you allow the EnergyWise domain controller policy to send power level updates to the phones.
                                                         The following conditions apply: One or more days must be selected in the Enable Power Save Plus field. The settings in Cisco Unified Communications Manager Administration take effect on schedule even if EnergyWise sends an override. For example, assuming the Phone Off Time is set to 22:00 (10:00 p.m.), the value in the Phone On Time field is 06:00 (6:00
                                                         a.m.), and the Enable Power Save Plus has one or more days selected. If EnergyWise directs the phone to turn off at 20:00 (8:00 p.m.), that directive remains in effect (assuming no phone user
                                                               intervention occurs) until the configured Phone On Time at 6:00 a.m. At 6:00 a.m., the phone turns on and resumes receiving the power level changes from the settings in Unified Communications
                                                               Manager Administration. To change the power level on the phone again, EnergyWise must reissue a new power level change command. Note To disable Power Save Plus, you must uncheck the Allow EnergyWise Overrides check box. If the Allow EnergyWise Overrides remains
                                                                     checked but no days are selected in the Enable Power Save Plus field, Power Save Plus is not disabled. | Field | Description | Enable Power Save Plus | Selects the schedule of days for which the phone powers off. Select multiple days by pressing and holding the Control key
                                                         while clicking on the days for the schedule. By default, no days are selected. When Enable Power Save Plus is checked, you receive a message that warns about emergency (e911) concerns. Caution While Power Save Plus Mode (the "Mode" ) is in effect, endpoints that are configured for the mode are disabled for emergency calling and from receiving inbound calls.
                                                                     By selecting this mode, you agree to the following: (i) You take full responsibility for providing alternate methods for emergency
                                                                     calling and receiving calls while the mode is in effect; (ii) Cisco has no liability in connection with your selection of
                                                                     the mode and all liability in connection with enabling the mode is your responsibility; and (iii) You fully inform users of
                                                                     the effects of the mode on calls, calling and otherwise. Note To disable Power Save Plus, you must uncheck the Allow EnergyWise Overrides check box. If the Allow EnergyWise Overrides remains
                                                                     checked but no days are selected in the Enable Power Save Plus field, Power Save Plus is not disabled. | Caution | While Power Save Plus Mode (the "Mode" ) is in effect, endpoints that are configured for the mode are disabled for emergency calling and from receiving inbound calls.
                                                                     By selecting this mode, you agree to the following: (i) You take full responsibility for providing alternate methods for emergency
                                                                     calling and receiving calls while the mode is in effect; (ii) Cisco has no liability in connection with your selection of
                                                                     the mode and all liability in connection with enabling the mode is your responsibility; and (iii) You fully inform users of
                                                                     the effects of the mode on calls, calling and otherwise. | Note | To disable Power Save Plus, you must uncheck the Allow EnergyWise Overrides check box. If the Allow EnergyWise Overrides remains
                                                                     checked but no days are selected in the Enable Power Save Plus field, Power Save Plus is not disabled. | Phone On Time | Determines when the phone automatically turns on for the days that are in the Enable Power Save Plus field. Enter the time in this field in 24-hour format, where 00:00 is midnight. For example, to automatically power up the phone at 07:00 a.m. (0700), enter 07:00. To power up the phone at 02:00 p.m. (1400),
                                                         enter 14:00. The default value is blank, which means 00:00. Note The Phone On Time must be at least 20 minutes later than the Phone Off Time. For example, if the Phone Off Time is 07:00,
                                                                     the Phone On Time must be no earlier than 07:20. | Note | The Phone On Time must be at least 20 minutes later than the Phone Off Time. For example, if the Phone Off Time is 07:00,
                                                                     the Phone On Time must be no earlier than 07:20. | Phone Off Time | The time of day that the phone powers down for the days that are selected in the Enable Power Save Plus field. If the Phone
                                                         On Time and the Phone Off Time fields contain the same value, the phone does not power down. Enter the time in this field in 24-hour format, where 00:00 is midnight. For example, to automatically power down the phone at 7:00 a.m. (0700), enter 7:00. To power down the phone at 2:00 p.m. (1400),
                                                         enter 14:00. The default value is blank, which means 00:00. Note The Phone On Time must be at least 20 minutes later than the Phone Off Time. For example, if the Phone Off Time is 7:00, the
                                                                     Phone On Time must be no earlier than 7:20. | Note | The Phone On Time must be at least 20 minutes later than the Phone Off Time. For example, if the Phone Off Time is 7:00, the
                                                                     Phone On Time must be no earlier than 7:20. | Phone Off Idle Timeout | The length of time that the phone must be idle before the phone powers down. The timeout occurs under the following conditions: When the phone was in Power Save Plus mode, as scheduled, and was taken out of Power Save Plus mode because the phone user
                                                               pressed the Select key. When the phone is repowered by the attached switch. When the Phone Off Time is reached but the phone is in use. The range of the field is 20 to 1440 minutes. The default value is 60 minutes. | Enable Audible Alert | When enabled, instructs the phone to play an audible alert starting 10 minutes before the time that the Phone Off Time field
                                                         specifies. The audible alert uses the phone ringtone, which briefly plays at specific times during the 10-minute alerting period. The
                                                         alerting ringtone plays at the user-designated volume level. The audible alert schedule is: At 10 minutes before power down, play the ringtone four times. At 7 minutes before power down, play the ringtone four times. At 4 minutes before power down, play the ringtone four times. At 30 seconds before power down, play the ringtone 15 times or until the phone powers off. This check box applies only if the Enable Power Save Plus list box has one or more days selected. | EnergyWise Domain | The EnergyWise domain that the phone is in. The maximum length of this field is 127 characters. | EnergyWise Secret | The security secret password that is used to communicate with the endpoints in the EnergyWise domain. The maximum length of this field is 127 characters. | Allow EnergyWise Overrides | This check box determines whether you allow the EnergyWise domain controller policy to send power level updates to the phones.
                                                         The following conditions apply: One or more days must be selected in the Enable Power Save Plus field. The settings in Cisco Unified Communications Manager Administration take effect on schedule even if EnergyWise sends an override. For example, assuming the Phone Off Time is set to 22:00 (10:00 p.m.), the value in the Phone On Time field is 06:00 (6:00
                                                         a.m.), and the Enable Power Save Plus has one or more days selected. If EnergyWise directs the phone to turn off at 20:00 (8:00 p.m.), that directive remains in effect (assuming no phone user
                                                               intervention occurs) until the configured Phone On Time at 6:00 a.m. At 6:00 a.m., the phone turns on and resumes receiving the power level changes from the settings in Unified Communications
                                                               Manager Administration. To change the power level on the phone again, EnergyWise must reissue a new power level change command. Note To disable Power Save Plus, you must uncheck the Allow EnergyWise Overrides check box. If the Allow EnergyWise Overrides remains
                                                                     checked but no days are selected in the Enable Power Save Plus field, Power Save Plus is not disabled. | Note | To disable Power Save Plus, you must uncheck the Allow EnergyWise Overrides check box. If the Allow EnergyWise Overrides remains
                                                                     checked but no days are selected in the Enable Power Save Plus field, Power Save Plus is not disabled. |
| Field | Description |
| Enable Power Save Plus | Selects the schedule of days for which the phone powers off. Select multiple days by pressing and holding the Control key
                                                         while clicking on the days for the schedule. By default, no days are selected. When Enable Power Save Plus is checked, you receive a message that warns about emergency (e911) concerns. Caution While Power Save Plus Mode (the "Mode" ) is in effect, endpoints that are configured for the mode are disabled for emergency calling and from receiving inbound calls.
                                                                     By selecting this mode, you agree to the following: (i) You take full responsibility for providing alternate methods for emergency
                                                                     calling and receiving calls while the mode is in effect; (ii) Cisco has no liability in connection with your selection of
                                                                     the mode and all liability in connection with enabling the mode is your responsibility; and (iii) You fully inform users of
                                                                     the effects of the mode on calls, calling and otherwise. Note To disable Power Save Plus, you must uncheck the Allow EnergyWise Overrides check box. If the Allow EnergyWise Overrides remains
                                                                     checked but no days are selected in the Enable Power Save Plus field, Power Save Plus is not disabled. | Caution | While Power Save Plus Mode (the "Mode" ) is in effect, endpoints that are configured for the mode are disabled for emergency calling and from receiving inbound calls.
                                                                     By selecting this mode, you agree to the following: (i) You take full responsibility for providing alternate methods for emergency
                                                                     calling and receiving calls while the mode is in effect; (ii) Cisco has no liability in connection with your selection of
                                                                     the mode and all liability in connection with enabling the mode is your responsibility; and (iii) You fully inform users of
                                                                     the effects of the mode on calls, calling and otherwise. | Note | To disable Power Save Plus, you must uncheck the Allow EnergyWise Overrides check box. If the Allow EnergyWise Overrides remains
                                                                     checked but no days are selected in the Enable Power Save Plus field, Power Save Plus is not disabled. |
| Caution | While Power Save Plus Mode (the "Mode" ) is in effect, endpoints that are configured for the mode are disabled for emergency calling and from receiving inbound calls.
                                                                     By selecting this mode, you agree to the following: (i) You take full responsibility for providing alternate methods for emergency
                                                                     calling and receiving calls while the mode is in effect; (ii) Cisco has no liability in connection with your selection of
                                                                     the mode and all liability in connection with enabling the mode is your responsibility; and (iii) You fully inform users of
                                                                     the effects of the mode on calls, calling and otherwise. |
| Note | To disable Power Save Plus, you must uncheck the Allow EnergyWise Overrides check box. If the Allow EnergyWise Overrides remains
                                                                     checked but no days are selected in the Enable Power Save Plus field, Power Save Plus is not disabled. |
| Phone On Time | Determines when the phone automatically turns on for the days that are in the Enable Power Save Plus field. Enter the time in this field in 24-hour format, where 00:00 is midnight. For example, to automatically power up the phone at 07:00 a.m. (0700), enter 07:00. To power up the phone at 02:00 p.m. (1400),
                                                         enter 14:00. The default value is blank, which means 00:00. Note The Phone On Time must be at least 20 minutes later than the Phone Off Time. For example, if the Phone Off Time is 07:00,
                                                                     the Phone On Time must be no earlier than 07:20. | Note | The Phone On Time must be at least 20 minutes later than the Phone Off Time. For example, if the Phone Off Time is 07:00,
                                                                     the Phone On Time must be no earlier than 07:20. |
| Note | The Phone On Time must be at least 20 minutes later than the Phone Off Time. For example, if the Phone Off Time is 07:00,
                                                                     the Phone On Time must be no earlier than 07:20. |
| Phone Off Time | The time of day that the phone powers down for the days that are selected in the Enable Power Save Plus field. If the Phone
                                                         On Time and the Phone Off Time fields contain the same value, the phone does not power down. Enter the time in this field in 24-hour format, where 00:00 is midnight. For example, to automatically power down the phone at 7:00 a.m. (0700), enter 7:00. To power down the phone at 2:00 p.m. (1400),
                                                         enter 14:00. The default value is blank, which means 00:00. Note The Phone On Time must be at least 20 minutes later than the Phone Off Time. For example, if the Phone Off Time is 7:00, the
                                                                     Phone On Time must be no earlier than 7:20. | Note | The Phone On Time must be at least 20 minutes later than the Phone Off Time. For example, if the Phone Off Time is 7:00, the
                                                                     Phone On Time must be no earlier than 7:20. |
| Note | The Phone On Time must be at least 20 minutes later than the Phone Off Time. For example, if the Phone Off Time is 7:00, the
                                                                     Phone On Time must be no earlier than 7:20. |
| Phone Off Idle Timeout | The length of time that the phone must be idle before the phone powers down. The timeout occurs under the following conditions: When the phone was in Power Save Plus mode, as scheduled, and was taken out of Power Save Plus mode because the phone user
                                                               pressed the Select key. When the phone is repowered by the attached switch. When the Phone Off Time is reached but the phone is in use. The range of the field is 20 to 1440 minutes. The default value is 60 minutes. |
| Enable Audible Alert | When enabled, instructs the phone to play an audible alert starting 10 minutes before the time that the Phone Off Time field
                                                         specifies. The audible alert uses the phone ringtone, which briefly plays at specific times during the 10-minute alerting period. The
                                                         alerting ringtone plays at the user-designated volume level. The audible alert schedule is: At 10 minutes before power down, play the ringtone four times. At 7 minutes before power down, play the ringtone four times. At 4 minutes before power down, play the ringtone four times. At 30 seconds before power down, play the ringtone 15 times or until the phone powers off. This check box applies only if the Enable Power Save Plus list box has one or more days selected. |
| EnergyWise Domain | The EnergyWise domain that the phone is in. The maximum length of this field is 127 characters. |
| EnergyWise Secret | The security secret password that is used to communicate with the endpoints in the EnergyWise domain. The maximum length of this field is 127 characters. |
| Allow EnergyWise Overrides | This check box determines whether you allow the EnergyWise domain controller policy to send power level updates to the phones.
                                                         The following conditions apply: One or more days must be selected in the Enable Power Save Plus field. The settings in Cisco Unified Communications Manager Administration take effect on schedule even if EnergyWise sends an override. For example, assuming the Phone Off Time is set to 22:00 (10:00 p.m.), the value in the Phone On Time field is 06:00 (6:00
                                                         a.m.), and the Enable Power Save Plus has one or more days selected. If EnergyWise directs the phone to turn off at 20:00 (8:00 p.m.), that directive remains in effect (assuming no phone user
                                                               intervention occurs) until the configured Phone On Time at 6:00 a.m. At 6:00 a.m., the phone turns on and resumes receiving the power level changes from the settings in Unified Communications
                                                               Manager Administration. To change the power level on the phone again, EnergyWise must reissue a new power level change command. Note To disable Power Save Plus, you must uncheck the Allow EnergyWise Overrides check box. If the Allow EnergyWise Overrides remains
                                                                     checked but no days are selected in the Enable Power Save Plus field, Power Save Plus is not disabled. | Note | To disable Power Save Plus, you must uncheck the Allow EnergyWise Overrides check box. If the Allow EnergyWise Overrides remains
                                                                     checked but no days are selected in the Enable Power Save Plus field, Power Save Plus is not disabled. |
| Note | To disable Power Save Plus, you must uncheck the Allow EnergyWise Overrides check box. If the Allow EnergyWise Overrides remains
                                                                     checked but no days are selected in the Enable Power Save Plus field, Power Save Plus is not disabled. |
| Step 4 | Select Save . |
| Step 5 | Select Apply Config . |
| Step 6 | Restart the phone. |

| Field | Description |
|---|---|
| Enable Power Save Plus | Selects the schedule of days for which the phone powers off. Select multiple days by pressing and holding the Control key
                                                         while clicking on the days for the schedule. By default, no days are selected. When Enable Power Save Plus is checked, you receive a message that warns about emergency (e911) concerns. Caution While Power Save Plus Mode (the "Mode" ) is in effect, endpoints that are configured for the mode are disabled for emergency calling and from receiving inbound calls.
                                                                     By selecting this mode, you agree to the following: (i) You take full responsibility for providing alternate methods for emergency
                                                                     calling and receiving calls while the mode is in effect; (ii) Cisco has no liability in connection with your selection of
                                                                     the mode and all liability in connection with enabling the mode is your responsibility; and (iii) You fully inform users of
                                                                     the effects of the mode on calls, calling and otherwise. Note To disable Power Save Plus, you must uncheck the Allow EnergyWise Overrides check box. If the Allow EnergyWise Overrides remains
                                                                     checked but no days are selected in the Enable Power Save Plus field, Power Save Plus is not disabled. | Caution | While Power Save Plus Mode (the "Mode" ) is in effect, endpoints that are configured for the mode are disabled for emergency calling and from receiving inbound calls.
                                                                     By selecting this mode, you agree to the following: (i) You take full responsibility for providing alternate methods for emergency
                                                                     calling and receiving calls while the mode is in effect; (ii) Cisco has no liability in connection with your selection of
                                                                     the mode and all liability in connection with enabling the mode is your responsibility; and (iii) You fully inform users of
                                                                     the effects of the mode on calls, calling and otherwise. | Note | To disable Power Save Plus, you must uncheck the Allow EnergyWise Overrides check box. If the Allow EnergyWise Overrides remains
                                                                     checked but no days are selected in the Enable Power Save Plus field, Power Save Plus is not disabled. |
| Caution | While Power Save Plus Mode (the "Mode" ) is in effect, endpoints that are configured for the mode are disabled for emergency calling and from receiving inbound calls.
                                                                     By selecting this mode, you agree to the following: (i) You take full responsibility for providing alternate methods for emergency
                                                                     calling and receiving calls while the mode is in effect; (ii) Cisco has no liability in connection with your selection of
                                                                     the mode and all liability in connection with enabling the mode is your responsibility; and (iii) You fully inform users of
                                                                     the effects of the mode on calls, calling and otherwise. |
| Note | To disable Power Save Plus, you must uncheck the Allow EnergyWise Overrides check box. If the Allow EnergyWise Overrides remains
                                                                     checked but no days are selected in the Enable Power Save Plus field, Power Save Plus is not disabled. |
| Phone On Time | Determines when the phone automatically turns on for the days that are in the Enable Power Save Plus field. Enter the time in this field in 24-hour format, where 00:00 is midnight. For example, to automatically power up the phone at 07:00 a.m. (0700), enter 07:00. To power up the phone at 02:00 p.m. (1400),
                                                         enter 14:00. The default value is blank, which means 00:00. Note The Phone On Time must be at least 20 minutes later than the Phone Off Time. For example, if the Phone Off Time is 07:00,
                                                                     the Phone On Time must be no earlier than 07:20. | Note | The Phone On Time must be at least 20 minutes later than the Phone Off Time. For example, if the Phone Off Time is 07:00,
                                                                     the Phone On Time must be no earlier than 07:20. |
| Note | The Phone On Time must be at least 20 minutes later than the Phone Off Time. For example, if the Phone Off Time is 07:00,
                                                                     the Phone On Time must be no earlier than 07:20. |
| Phone Off Time | The time of day that the phone powers down for the days that are selected in the Enable Power Save Plus field. If the Phone
                                                         On Time and the Phone Off Time fields contain the same value, the phone does not power down. Enter the time in this field in 24-hour format, where 00:00 is midnight. For example, to automatically power down the phone at 7:00 a.m. (0700), enter 7:00. To power down the phone at 2:00 p.m. (1400),
                                                         enter 14:00. The default value is blank, which means 00:00. Note The Phone On Time must be at least 20 minutes later than the Phone Off Time. For example, if the Phone Off Time is 7:00, the
                                                                     Phone On Time must be no earlier than 7:20. | Note | The Phone On Time must be at least 20 minutes later than the Phone Off Time. For example, if the Phone Off Time is 7:00, the
                                                                     Phone On Time must be no earlier than 7:20. |
| Note | The Phone On Time must be at least 20 minutes later than the Phone Off Time. For example, if the Phone Off Time is 7:00, the
                                                                     Phone On Time must be no earlier than 7:20. |
| Phone Off Idle Timeout | The length of time that the phone must be idle before the phone powers down. The timeout occurs under the following conditions: When the phone was in Power Save Plus mode, as scheduled, and was taken out of Power Save Plus mode because the phone user
                                                               pressed the Select key. When the phone is repowered by the attached switch. When the Phone Off Time is reached but the phone is in use. The range of the field is 20 to 1440 minutes. The default value is 60 minutes. |
| Enable Audible Alert | When enabled, instructs the phone to play an audible alert starting 10 minutes before the time that the Phone Off Time field
                                                         specifies. The audible alert uses the phone ringtone, which briefly plays at specific times during the 10-minute alerting period. The
                                                         alerting ringtone plays at the user-designated volume level. The audible alert schedule is: At 10 minutes before power down, play the ringtone four times. At 7 minutes before power down, play the ringtone four times. At 4 minutes before power down, play the ringtone four times. At 30 seconds before power down, play the ringtone 15 times or until the phone powers off. This check box applies only if the Enable Power Save Plus list box has one or more days selected. |
| EnergyWise Domain | The EnergyWise domain that the phone is in. The maximum length of this field is 127 characters. |
| EnergyWise Secret | The security secret password that is used to communicate with the endpoints in the EnergyWise domain. The maximum length of this field is 127 characters. |
| Allow EnergyWise Overrides | This check box determines whether you allow the EnergyWise domain controller policy to send power level updates to the phones.
                                                         The following conditions apply: One or more days must be selected in the Enable Power Save Plus field. The settings in Cisco Unified Communications Manager Administration take effect on schedule even if EnergyWise sends an override. For example, assuming the Phone Off Time is set to 22:00 (10:00 p.m.), the value in the Phone On Time field is 06:00 (6:00
                                                         a.m.), and the Enable Power Save Plus has one or more days selected. If EnergyWise directs the phone to turn off at 20:00 (8:00 p.m.), that directive remains in effect (assuming no phone user
                                                               intervention occurs) until the configured Phone On Time at 6:00 a.m. At 6:00 a.m., the phone turns on and resumes receiving the power level changes from the settings in Unified Communications
                                                               Manager Administration. To change the power level on the phone again, EnergyWise must reissue a new power level change command. Note To disable Power Save Plus, you must uncheck the Allow EnergyWise Overrides check box. If the Allow EnergyWise Overrides remains
                                                                     checked but no days are selected in the Enable Power Save Plus field, Power Save Plus is not disabled. | Note | To disable Power Save Plus, you must uncheck the Allow EnergyWise Overrides check box. If the Allow EnergyWise Overrides remains
                                                                     checked but no days are selected in the Enable Power Save Plus field, Power Save Plus is not disabled. |
| Note | To disable Power Save Plus, you must uncheck the Allow EnergyWise Overrides check box. If the Allow EnergyWise Overrides remains
                                                                     checked but no days are selected in the Enable Power Save Plus field, Power Save Plus is not disabled. |

| Caution | While Power Save Plus Mode (the "Mode" ) is in effect, endpoints that are configured for the mode are disabled for emergency calling and from receiving inbound calls.
                                                                     By selecting this mode, you agree to the following: (i) You take full responsibility for providing alternate methods for emergency
                                                                     calling and receiving calls while the mode is in effect; (ii) Cisco has no liability in connection with your selection of
                                                                     the mode and all liability in connection with enabling the mode is your responsibility; and (iii) You fully inform users of
                                                                     the effects of the mode on calls, calling and otherwise. |
|---|---|

| Note | To disable Power Save Plus, you must uncheck the Allow EnergyWise Overrides check box. If the Allow EnergyWise Overrides remains
                                                                     checked but no days are selected in the Enable Power Save Plus field, Power Save Plus is not disabled. |
|---|---|

| Note | The Phone On Time must be at least 20 minutes later than the Phone Off Time. For example, if the Phone Off Time is 07:00,
                                                                     the Phone On Time must be no earlier than 07:20. |
|---|---|

| Note | The Phone On Time must be at least 20 minutes later than the Phone Off Time. For example, if the Phone Off Time is 7:00, the
                                                                     Phone On Time must be no earlier than 7:20. |
|---|---|

| Note | To disable Power Save Plus, you must uncheck the Allow EnergyWise Overrides check box. If the Allow EnergyWise Overrides remains
                                                                     checked but no days are selected in the Enable Power Save Plus field, Power Save Plus is not disabled. |
|---|---|

| Step 1 | In Cisco Unified Communications Manager Administration, select Device > Phone . |
|---|---|
| Step 2 | Locate the phone to be configured. |
| Step 3 | Set the following parameters. Do Not
                                                   						Disturb: This check box allows you to enable DND on the phone. DND Option: Ring Off, Call Reject, or Use Common Phone Profile Setting. Do not choose Call Reject if you want priority (MLPP) calls to ring this phone when DND is turned on. DND Incoming Call
                                                   						Alert: Choose the type of alert, if any, to play on a phone for incoming calls
                                                   						when DND is active. Note This parameter is located on in the Common Phone Profile
                                                               						window and the Phone Configuration window. The Phone Configuration window value
                                                               						takes precedence. | Note | This parameter is located on in the Common Phone Profile
                                                               						window and the Phone Configuration window. The Phone Configuration window value
                                                               						takes precedence. |
| Note | This parameter is located on in the Common Phone Profile
                                                               						window and the Phone Configuration window. The Phone Configuration window value
                                                               						takes precedence. |
| Step 4 | Select Save . |

| Note | This parameter is located on in the Common Phone Profile
                                                               						window and the Phone Configuration window. The Phone Configuration window value
                                                               						takes precedence. |
|---|---|

| Step 1 | From Cisco
                                          			 Unified Communications Manager Administration, select Device > Phone . |
|---|---|
| Step 2 | Locate the IP
                                          			 phone that you want to configure. |
| Step 3 | Scroll to the
                                          			 Device Information Layout pane and set Built
                                             				In Bridge to On or Default. |
| Step 4 | Select Save . |
| Step 5 | Check the
                                          			 setting of the bridge: Choose System > Service
                                                      						Parameters . Select the
                                                				  appropriate Server and Service. Scroll to
                                                				  the Clusterwide Parameters (Device - Phone) pane and set Builtin Bridge Enable to On. Select Save . |

| Step 1 | In Cisco Unified Communications Manager Administration, select User Management > Application User . |
|---|---|
| Step 2 | Check the Standard CTI Allow Call Monitoring user group and the Standard CTI Allow Call Recording user groups. |
| Step 3 | Click Add Selected . |
| Step 4 | Click Add to User Group . |
| Step 5 | Add the user phones to the list of Application Users controlled devices. |
| Step 6 | Select Save . |

| Step 1 | In Cisco
                                          		  Unified Communications Manager Administration, select Device > Phone . |
|---|---|
| Step 2 | Locate the phone to be set up. |
| Step 3 | Configure the Call Forward Notification fields. Field Description Caller Name When this check box is checked, the caller name displays in
                                                         					 the notification window. By default, this check box is checked. Caller Number When this check box is checked, the caller number displays in
                                                         					 the notification window. By default, this check box is not checked. Redirected Number When this check box is checked, the information about the
                                                         					 caller who last forwarded the call displays in the notification window. Example: If Caller A calls B, but B has forwarded all calls to
                                                         					 C and C has forwarded all calls to D, the notification box that D sees
                                                         					 contains the phone information for caller C. By default, this check box is not checked. Dialed Number When this check box is checked, the information about the
                                                         					 original recipient of the call displays in the notification window. Example: If Caller A calls B, but B has forwarded all calls to
                                                         					 C and C has forwarded all calls to D, then the notification box that D sees
                                                         					 contains the phone information for caller B. By default, this check box is checked. | Field | Description | Caller Name | When this check box is checked, the caller name displays in
                                                         					 the notification window. By default, this check box is checked. | Caller Number | When this check box is checked, the caller number displays in
                                                         					 the notification window. By default, this check box is not checked. | Redirected Number | When this check box is checked, the information about the
                                                         					 caller who last forwarded the call displays in the notification window. Example: If Caller A calls B, but B has forwarded all calls to
                                                         					 C and C has forwarded all calls to D, the notification box that D sees
                                                         					 contains the phone information for caller C. By default, this check box is not checked. | Dialed Number | When this check box is checked, the information about the
                                                         					 original recipient of the call displays in the notification window. Example: If Caller A calls B, but B has forwarded all calls to
                                                         					 C and C has forwarded all calls to D, then the notification box that D sees
                                                         					 contains the phone information for caller B. By default, this check box is checked. |
| Field | Description |
| Caller Name | When this check box is checked, the caller name displays in
                                                         					 the notification window. By default, this check box is checked. |
| Caller Number | When this check box is checked, the caller number displays in
                                                         					 the notification window. By default, this check box is not checked. |
| Redirected Number | When this check box is checked, the information about the
                                                         					 caller who last forwarded the call displays in the notification window. Example: If Caller A calls B, but B has forwarded all calls to
                                                         					 C and C has forwarded all calls to D, the notification box that D sees
                                                         					 contains the phone information for caller C. By default, this check box is not checked. |
| Dialed Number | When this check box is checked, the information about the
                                                         					 original recipient of the call displays in the notification window. Example: If Caller A calls B, but B has forwarded all calls to
                                                         					 C and C has forwarded all calls to D, then the notification box that D sees
                                                         					 contains the phone information for caller B. By default, this check box is checked. |
| Step 4 | Select Save . |

| Field | Description |
|---|---|
| Caller Name | When this check box is checked, the caller name displays in
                                                         					 the notification window. By default, this check box is checked. |
| Caller Number | When this check box is checked, the caller number displays in
                                                         					 the notification window. By default, this check box is not checked. |
| Redirected Number | When this check box is checked, the information about the
                                                         					 caller who last forwarded the call displays in the notification window. Example: If Caller A calls B, but B has forwarded all calls to
                                                         					 C and C has forwarded all calls to D, the notification box that D sees
                                                         					 contains the phone information for caller C. By default, this check box is not checked. |
| Dialed Number | When this check box is checked, the information about the
                                                         					 original recipient of the call displays in the notification window. Example: If Caller A calls B, but B has forwarded all calls to
                                                         					 C and C has forwarded all calls to D, then the notification box that D sees
                                                         					 contains the phone information for caller B. By default, this check box is checked. |

| Step 1 | In the Cisco
                                          			 Unified Communications Manager Administration, select System > Enterprise
                                                				  Parameters . |
|---|---|
| Step 2 | For the BLF for Call Lists field, enable or disable the feature. By default, the feature is disabled. Parameters
                                             				that you set in the Product Specific Configuration area may also appear in the
                                             				Device Configuration window for various devices and in the Enterprise Phone
                                             				Configuration window. If you set these same parameters in these other windows
                                             				as well, the setting that takes precedence is determined in the following
                                             				order: Device
                                                   					 Configuration window settings Common
                                                   					 Phone Profile window settings Enterprise
                                                   					 Phone Configuration window settings |
| Step 3 | Select Save . |

| Note | Administrators must confirm that the Override Check box is checked on all applicable UCM pages or EEE will not function. |
|---|---|

| Step 1 | In Cisco Unified Communications Manager Administration, select one
                                          			 of the following windows: Device > Phone Device > Device
                                                         						  Settings > Common Phone Profile System > Enterprise
                                                         						  Phone Configurations If you configure the parameter in multiple windows, the precedence
                                             				order is: Device > Phone Device > Device
                                                         						  Settings > Common Phone Profile System > Enterprise
                                                         						  Phone Configurations |
|---|---|
| Step 2 | If required, locate the phone. |
| Step 3 | Set the Energy Efficient Ethernet: PC Port and Energy Efficient Ethernet: Switch Port fields. Energy Efficient Ethernet: PC Port Energy Efficient Ethernet: Switch Port |
| Step 4 | Select Save . |
| Step 5 | Select Apply Config . |
| Step 6 | Restart the phone. |

| Step 1 | Select Device > Device
                                                				  Settings > SIP Profile |
|---|---|
| Step 2 | Choose the
                                          			 search criteria to use and click Find . |
| Step 3 | Select the
                                          			 profile to modify. |
| Step 4 | Set the Start
                                          			 Media Port and Stop Media Port to contain the start and end of the port range. The following
                                             				list identifies the UDP ports that are used for other phone services and thus
                                             				not available for RTP and sRTP use: port 4051 used for
                                                      						the Peer Firmware Sharing (PFS) feature port 5060 used for
                                                      						SIP over UDP transport port range 2048  to 49150 Do not configure the Stop Media Port to a value over 49150. |
| Step 5 | Click Save . |
| Step 6 | Click Apply
                                             				Config . |

| Note | If the phone security profile for any of your phones has TFTP Encrypted Config checked, you cannot use the phone with Mobile
                                             and Remote Access. The MRA solution does not support device interaction with Certificate Authority Proxy Function (CAPF). |
|---|---|

| Note | For SIP OAuth in Mobile and Remote Access (MRA) mode, use only Activation Code
                                             					Onboarding with Mobile and Remote Access when you deploy the phone. Activation
                                             					with a username and password is not supported. |
|---|---|

| Phone Feature | Phone Firmware Release |
|---|---|
| Abbreviated Dialing | 10.3(1) and later |
| Answer Oldest | 11.5(1)SR1 and later |
| Assisted Directed Call Park | 10.3(1) and later |
| Auto Answer | 11.5(1)SR1 and later |
| Barge and cBarge | 11.5(1)SR1 and later |
| Busy Lamp Field (BLF) | 10.3(1) and later |
| Busy Lamp Field (BLF) Pickup | 10.3(1) and later |
| Busy Lamp Field (BLF) Speed Dial | 10.3(1) and later |
| Call Back | 10.3(1) and later |
| Call Forward | 10.3(1) and later |
| Call Forward Notification | 10.3(1) and later |
| Call Park | 10.3(1) and later |
| Call Pickup | 10.3(1) and later |
| Cisco Unified Serviceability | 11.5(1)SR1 and later |
| Client Access License (CAL) | 11.5(1)SR1 and later |
| Conference | 10.3(1) and later |
| Conference List / Remove Participant | 11.5(1)SR1 and later |
| Corporate Directory | 11.5(1)SR1 and later |
| CTI Applications (CTI Controlled) | 11.5(1)SR1 and later |
| Direct Transfer | 10.3(1) and later |
| Directed Call Park | 10.3(1) and later |
| Distinctive Ring | 11.5(1)SR1 and later |
| Divert | 10.3(1) and later |
| Enhanced line mode | 12.1(1) and later |
| Divert | 10.3(1) and later |
| Forced Access Codes and Client Matter Codes | 11.5(1)SR1 and later |
| Group Call Pickup | 10.3(1) and later |
| Hold/Resume | 10.3(1) and later |
| Hold Reversion | 10.3(1) and later |
| Immediate Divert | 10.3(1) and later |
| Join | 10.3(1) and later |
| Malicious Caller Identification (MCID) | 11.5(1)SR1 and later |
| Meet Me Conference | 10.3(1) and later |
| Message Waiting Indicator | 10.3(1) and later |
| Mobile Connect | 10.3(1) and later |
| Mobile Voice Access | 10.3(1) and later |
| Multilevel Precedence and Preemption (MLPP) | 11.5(1)SR1 and later |
| Multiline | 11.5(1)SR1 and later |
| Music On Hold | 10.3(1) and later |
| Mute | 10.3(1) and later |
| Network profiles (Automatic) | 11.5(1)SR1 and later |
| Off-hook Dialing | 10.3(1) and later |
| On-hook Dialing | 10.3(1) and later |
| Plus Dialing | 10.3(1) and later |
| Privacy | 11.5(1)SR1 and later |
| Private Line Automated Ringdown (PLAR) | 11.5(1)SR1 and later |
| Redial | 10.3(1) and later |
| Speed Dial (does not support a pause) | 10.3(1) and later |
| Services URL button | 11.5(1)SR1 and later |
| Transfer | 10.3(1) and later |
| Uniform Resource Identifier (URI) Dialing | 10.3(1) and later |

| Step 1 | Use a QR code generator to generate a QR code with either the service domain, or the service domain and username separated
                                             by a comma. For example: mra.example.com or mra.example.com,username. |
|---|---|
| Step 2 | Print the QR code and provide it to the user. |

| Note | The Problem Report Tool logs are required by Cisco TAC when troubleshooting problems. The logs are cleared if you restart
                                             the phone. Collect the logs before you restart the phones. |
|---|---|

| Note | The phones only support HTTP URLs. |
|---|---|

| Step 1 | Set up a server that can run your PRT upload script. |
|---|---|
| Step 2 | Write a script that can handle the parameters listed above, or edit the provided sample script to suit your needs. |
| Step 3 | Upload your script to your server. |
| Step 4 | In Cisco Unified Communications Manager, go to the Product Specific
                                             			 Configuration Layout area of the individual device configuration window, Common
                                             			 Phone Profile window, or Enterprise Phone Configuration window. |
| Step 5 | Check Customer support upload URL and
                                             			 enter your upload server URL. Example: http://example.com/prtscript.php |
| Step 6 | Save your changes. |

| Step 1 | In Cisco Unified Communications Manager Administration, select Device > Phone . |
|---|---|
| Step 2 | Locate the phone to be configured. |
| Step 3 | Locate the line instance and set the Line Text Label field. |
| Step 4 | (Optional) If the label needs to be applied to other devices that share the line, check the Update Shared Device
                                          Settings check box and click Propagate Selected . |
| Step 5 | Select Save . |

| Step 1 | In Cisco Unified Communications Manager Administration,
                                          			 choose Device > Device
                                                				  Defaults . |
|---|---|
| Step 2 | Check the load information in the Inactive Load
                                          				Information field. |
| Step 3 | Choose Bulk
                                                				  Administration > Import/Export > Export > Device
                                                				  Defaults , and schedule an export job. |
| Step 4 | Download the exported tar file and untar it. |
| Step 5 | Check the file format in the exported CSV file and verify that the
                                          			 CSV file has an Inactive Load Information column with the correct value. Note The CSV file value must match the Device Default value in the
                                                         				  Cisco Unified Communications Manager Administration window. | Note | The CSV file value must match the Device Default value in the
                                                         				  Cisco Unified Communications Manager Administration window. |
| Note | The CSV file value must match the Device Default value in the
                                                         				  Cisco Unified Communications Manager Administration window. |

| Note | The CSV file value must match the Device Default value in the
                                                         				  Cisco Unified Communications Manager Administration window. |
|---|---|

| Step 1 | In Cisco Unified Communications Manager Administration,
                                             			 choose System > Service
                                                   				  Parameters . |
|---|---|
| Step 2 | Update the Park Monitoring Reversion Timer, Park Monitoring
                                             			 Periodic Reversion Timer, and Park Monitoring Forward No Retrieve Timer fields
                                             			 in the Clusterwide Parameters (Feature-General) pane. Table 6. Service Parameters for Park Monitoring Field Description Park Monitoring Reversion Timer Default is 60 seconds. This parameter determines the number of
                                                            					 seconds that Cisco Unified Communications Manager waits before prompting the
                                                            					 user to retrieve a call that the user parked. This timer starts when the user
                                                            					 presses Park on the phone, and a reminder is issued when the timer expires. You can override the value that this service parameter
                                                            					 specifies on a per-line basis in the Park Monitoring section of the Directory
                                                            					 Number Configuration window (in Cisco Unified Communications Manager
                                                            					 Administration, choose Call
                                                                  						  Routing > Directory Number ).
                                                            					 Specify a value of 0 to immediately utilize the periodic reversion interval
                                                            					 that the Park Monitoring Periodic Reversion Timer service parameter specifies.
                                                            					 (See the description that follows.) For example, if this parameter is set to
                                                            					 zero and the Park Monitoring Periodic Reversion Timer is set to 15, the user is
                                                            					 immediately prompted about the parked call and every 15 seconds thereafter
                                                            					 until the Park Monitoring Forward No Retrieve Timer (see the description that
                                                            					 follows) expires. Park Monitoring Periodic Reversion Timer Default is 30 seconds. This parameter determines the interval
                                                            					 (in seconds) that Cisco Unified Communications Manager waits before prompting
                                                            					 the user again that a call is parked. To connect to the parked call, the user
                                                            					 can simply go off-hook during one of these prompts. Cisco Unified
                                                            					 Communications Manager continues to prompt the user about the parked call as
                                                            					 long as the call remains parked and until the time that the Park Monitoring
                                                            					 Forward No Retrieve Timer (see the description that follows) specifies expires.
                                                            					 Specify a value of 0 to disable periodic prompts about the parked call. Park Monitoring Forward No Retrieve Timer Default is 300 seconds. This parameter determines the number
                                                            					 of seconds that park reminder notifications occur before the parked call
                                                            					 forwards to the Park Monitoring Forward No Retrieve destination that is
                                                            					 specified in the parker Directory Number Configuration window. (If no forward
                                                            					 destination is provided in Cisco Unified Communications Manager Administration,
                                                            					 the call returns to the line that parked the call.) This parameter starts when
                                                            					 the time that the Park Monitoring Reversion Timer service parameter specifies
                                                            					 expires. When the Park Monitoring Forward No Retrieve Timer expires, the call
                                                            					 is removed from park and forwards to the specified destination or returns to
                                                            					 the parker line. | Field | Description | Park Monitoring Reversion Timer | Default is 60 seconds. This parameter determines the number of
                                                            					 seconds that Cisco Unified Communications Manager waits before prompting the
                                                            					 user to retrieve a call that the user parked. This timer starts when the user
                                                            					 presses Park on the phone, and a reminder is issued when the timer expires. You can override the value that this service parameter
                                                            					 specifies on a per-line basis in the Park Monitoring section of the Directory
                                                            					 Number Configuration window (in Cisco Unified Communications Manager
                                                            					 Administration, choose Call
                                                                  						  Routing > Directory Number ).
                                                            					 Specify a value of 0 to immediately utilize the periodic reversion interval
                                                            					 that the Park Monitoring Periodic Reversion Timer service parameter specifies.
                                                            					 (See the description that follows.) For example, if this parameter is set to
                                                            					 zero and the Park Monitoring Periodic Reversion Timer is set to 15, the user is
                                                            					 immediately prompted about the parked call and every 15 seconds thereafter
                                                            					 until the Park Monitoring Forward No Retrieve Timer (see the description that
                                                            					 follows) expires. | Park Monitoring Periodic Reversion Timer | Default is 30 seconds. This parameter determines the interval
                                                            					 (in seconds) that Cisco Unified Communications Manager waits before prompting
                                                            					 the user again that a call is parked. To connect to the parked call, the user
                                                            					 can simply go off-hook during one of these prompts. Cisco Unified
                                                            					 Communications Manager continues to prompt the user about the parked call as
                                                            					 long as the call remains parked and until the time that the Park Monitoring
                                                            					 Forward No Retrieve Timer (see the description that follows) specifies expires.
                                                            					 Specify a value of 0 to disable periodic prompts about the parked call. | Park Monitoring Forward No Retrieve Timer | Default is 300 seconds. This parameter determines the number
                                                            					 of seconds that park reminder notifications occur before the parked call
                                                            					 forwards to the Park Monitoring Forward No Retrieve destination that is
                                                            					 specified in the parker Directory Number Configuration window. (If no forward
                                                            					 destination is provided in Cisco Unified Communications Manager Administration,
                                                            					 the call returns to the line that parked the call.) This parameter starts when
                                                            					 the time that the Park Monitoring Reversion Timer service parameter specifies
                                                            					 expires. When the Park Monitoring Forward No Retrieve Timer expires, the call
                                                            					 is removed from park and forwards to the specified destination or returns to
                                                            					 the parker line. |
| Field | Description |
| Park Monitoring Reversion Timer | Default is 60 seconds. This parameter determines the number of
                                                            					 seconds that Cisco Unified Communications Manager waits before prompting the
                                                            					 user to retrieve a call that the user parked. This timer starts when the user
                                                            					 presses Park on the phone, and a reminder is issued when the timer expires. You can override the value that this service parameter
                                                            					 specifies on a per-line basis in the Park Monitoring section of the Directory
                                                            					 Number Configuration window (in Cisco Unified Communications Manager
                                                            					 Administration, choose Call
                                                                  						  Routing > Directory Number ).
                                                            					 Specify a value of 0 to immediately utilize the periodic reversion interval
                                                            					 that the Park Monitoring Periodic Reversion Timer service parameter specifies.
                                                            					 (See the description that follows.) For example, if this parameter is set to
                                                            					 zero and the Park Monitoring Periodic Reversion Timer is set to 15, the user is
                                                            					 immediately prompted about the parked call and every 15 seconds thereafter
                                                            					 until the Park Monitoring Forward No Retrieve Timer (see the description that
                                                            					 follows) expires. |
| Park Monitoring Periodic Reversion Timer | Default is 30 seconds. This parameter determines the interval
                                                            					 (in seconds) that Cisco Unified Communications Manager waits before prompting
                                                            					 the user again that a call is parked. To connect to the parked call, the user
                                                            					 can simply go off-hook during one of these prompts. Cisco Unified
                                                            					 Communications Manager continues to prompt the user about the parked call as
                                                            					 long as the call remains parked and until the time that the Park Monitoring
                                                            					 Forward No Retrieve Timer (see the description that follows) specifies expires.
                                                            					 Specify a value of 0 to disable periodic prompts about the parked call. |
| Park Monitoring Forward No Retrieve Timer | Default is 300 seconds. This parameter determines the number
                                                            					 of seconds that park reminder notifications occur before the parked call
                                                            					 forwards to the Park Monitoring Forward No Retrieve destination that is
                                                            					 specified in the parker Directory Number Configuration window. (If no forward
                                                            					 destination is provided in Cisco Unified Communications Manager Administration,
                                                            					 the call returns to the line that parked the call.) This parameter starts when
                                                            					 the time that the Park Monitoring Reversion Timer service parameter specifies
                                                            					 expires. When the Park Monitoring Forward No Retrieve Timer expires, the call
                                                            					 is removed from park and forwards to the specified destination or returns to
                                                            					 the parker line. |

| Field | Description |
|---|---|
| Park Monitoring Reversion Timer | Default is 60 seconds. This parameter determines the number of
                                                            					 seconds that Cisco Unified Communications Manager waits before prompting the
                                                            					 user to retrieve a call that the user parked. This timer starts when the user
                                                            					 presses Park on the phone, and a reminder is issued when the timer expires. You can override the value that this service parameter
                                                            					 specifies on a per-line basis in the Park Monitoring section of the Directory
                                                            					 Number Configuration window (in Cisco Unified Communications Manager
                                                            					 Administration, choose Call
                                                                  						  Routing > Directory Number ).
                                                            					 Specify a value of 0 to immediately utilize the periodic reversion interval
                                                            					 that the Park Monitoring Periodic Reversion Timer service parameter specifies.
                                                            					 (See the description that follows.) For example, if this parameter is set to
                                                            					 zero and the Park Monitoring Periodic Reversion Timer is set to 15, the user is
                                                            					 immediately prompted about the parked call and every 15 seconds thereafter
                                                            					 until the Park Monitoring Forward No Retrieve Timer (see the description that
                                                            					 follows) expires. |
| Park Monitoring Periodic Reversion Timer | Default is 30 seconds. This parameter determines the interval
                                                            					 (in seconds) that Cisco Unified Communications Manager waits before prompting
                                                            					 the user again that a call is parked. To connect to the parked call, the user
                                                            					 can simply go off-hook during one of these prompts. Cisco Unified
                                                            					 Communications Manager continues to prompt the user about the parked call as
                                                            					 long as the call remains parked and until the time that the Park Monitoring
                                                            					 Forward No Retrieve Timer (see the description that follows) specifies expires.
                                                            					 Specify a value of 0 to disable periodic prompts about the parked call. |
| Park Monitoring Forward No Retrieve Timer | Default is 300 seconds. This parameter determines the number
                                                            					 of seconds that park reminder notifications occur before the parked call
                                                            					 forwards to the Park Monitoring Forward No Retrieve destination that is
                                                            					 specified in the parker Directory Number Configuration window. (If no forward
                                                            					 destination is provided in Cisco Unified Communications Manager Administration,
                                                            					 the call returns to the line that parked the call.) This parameter starts when
                                                            					 the time that the Park Monitoring Reversion Timer service parameter specifies
                                                            					 expires. When the Park Monitoring Forward No Retrieve Timer expires, the call
                                                            					 is removed from park and forwards to the specified destination or returns to
                                                            					 the parker line. |

| Step 1 | In Cisco
                                             			 Unified Communications Manager Administration, choose Call
                                                   				  Routing > Directory Number . |
|---|---|
| Step 2 | Set the park
                                             			 monitoring fields as described in the following table. Table 7. Park
                                                      				Monitoring Parameters Field Description Park
                                                            						  Monitoring Forward No Retrieve Destination External When
                                                            						  the parkee is an external party, the call forwards to the specified destination
                                                            						  in the parker Park Monitoring Forward No Retrieve Destination External
                                                            						  parameter. If the Forward No Retrieve Destination External field value is
                                                            						  empty, the parkee is redirected to the parker line. Park
                                                            						  Monitoring Forward No Retrieve Destination Internal When
                                                            						  the parkee is an internal party, the call forwards to the specified destination
                                                            						  in the parker’s Park Monitoring Forward No Retrieve Destination Internal
                                                            						  parameter. If the Forward No Retrieve Destination Internal is empty, the parkee
                                                            						  is redirected to the parker line. Park
                                                            						  Monitoring Reversion Timer This
                                                            						  parameter determines the number of seconds that Cisco Unified Communications
                                                            						  Manager waits before prompting the user to retrieve a call that the user
                                                            						  parked. This timer starts when the user presses Park on the phone, and a
                                                            						  reminder is issued when the timer expires. Default: 60 seconds If you
                                                            						  configure a nonzero value, this value overrides the value of this parameter set
                                                            						  in the Service Parameters window. However, if you configure a value of 0 here,
                                                            						  then the value in the Service Parameters window is used. | Field | Description | Park
                                                            						  Monitoring Forward No Retrieve Destination External | When
                                                            						  the parkee is an external party, the call forwards to the specified destination
                                                            						  in the parker Park Monitoring Forward No Retrieve Destination External
                                                            						  parameter. If the Forward No Retrieve Destination External field value is
                                                            						  empty, the parkee is redirected to the parker line. | Park
                                                            						  Monitoring Forward No Retrieve Destination Internal | When
                                                            						  the parkee is an internal party, the call forwards to the specified destination
                                                            						  in the parker’s Park Monitoring Forward No Retrieve Destination Internal
                                                            						  parameter. If the Forward No Retrieve Destination Internal is empty, the parkee
                                                            						  is redirected to the parker line. | Park
                                                            						  Monitoring Reversion Timer | This
                                                            						  parameter determines the number of seconds that Cisco Unified Communications
                                                            						  Manager waits before prompting the user to retrieve a call that the user
                                                            						  parked. This timer starts when the user presses Park on the phone, and a
                                                            						  reminder is issued when the timer expires. Default: 60 seconds If you
                                                            						  configure a nonzero value, this value overrides the value of this parameter set
                                                            						  in the Service Parameters window. However, if you configure a value of 0 here,
                                                            						  then the value in the Service Parameters window is used. |
| Field | Description |
| Park
                                                            						  Monitoring Forward No Retrieve Destination External | When
                                                            						  the parkee is an external party, the call forwards to the specified destination
                                                            						  in the parker Park Monitoring Forward No Retrieve Destination External
                                                            						  parameter. If the Forward No Retrieve Destination External field value is
                                                            						  empty, the parkee is redirected to the parker line. |
| Park
                                                            						  Monitoring Forward No Retrieve Destination Internal | When
                                                            						  the parkee is an internal party, the call forwards to the specified destination
                                                            						  in the parker’s Park Monitoring Forward No Retrieve Destination Internal
                                                            						  parameter. If the Forward No Retrieve Destination Internal is empty, the parkee
                                                            						  is redirected to the parker line. |
| Park
                                                            						  Monitoring Reversion Timer | This
                                                            						  parameter determines the number of seconds that Cisco Unified Communications
                                                            						  Manager waits before prompting the user to retrieve a call that the user
                                                            						  parked. This timer starts when the user presses Park on the phone, and a
                                                            						  reminder is issued when the timer expires. Default: 60 seconds If you
                                                            						  configure a nonzero value, this value overrides the value of this parameter set
                                                            						  in the Service Parameters window. However, if you configure a value of 0 here,
                                                            						  then the value in the Service Parameters window is used. |

| Field | Description |
|---|---|
| Park
                                                            						  Monitoring Forward No Retrieve Destination External | When
                                                            						  the parkee is an external party, the call forwards to the specified destination
                                                            						  in the parker Park Monitoring Forward No Retrieve Destination External
                                                            						  parameter. If the Forward No Retrieve Destination External field value is
                                                            						  empty, the parkee is redirected to the parker line. |
| Park
                                                            						  Monitoring Forward No Retrieve Destination Internal | When
                                                            						  the parkee is an internal party, the call forwards to the specified destination
                                                            						  in the parker’s Park Monitoring Forward No Retrieve Destination Internal
                                                            						  parameter. If the Forward No Retrieve Destination Internal is empty, the parkee
                                                            						  is redirected to the parker line. |
| Park
                                                            						  Monitoring Reversion Timer | This
                                                            						  parameter determines the number of seconds that Cisco Unified Communications
                                                            						  Manager waits before prompting the user to retrieve a call that the user
                                                            						  parked. This timer starts when the user presses Park on the phone, and a
                                                            						  reminder is issued when the timer expires. Default: 60 seconds If you
                                                            						  configure a nonzero value, this value overrides the value of this parameter set
                                                            						  in the Service Parameters window. However, if you configure a value of 0 here,
                                                            						  then the value in the Service Parameters window is used. |

| Step 1 | In Cisco
                                             			 Unified Communications Manager Administration, choose Call
                                                   				  Routing > Route/Hunt > Hunt
                                                   				  Pilot . |
|---|---|
| Step 2 | Set the Hunt
                                             			 Pilot Park Monitoring Forward No Retrieve Destination parameter. If the Hunt
                                                				Pilot Park Monitoring Forward No Retrieve Destination parameter value is blank,
                                                				the call forwards to the destination that is configured in the Directory Number
                                                				Configuration window when the Park Monitoring Forward No Retrieve Timer
                                                				expires. |

| Step 1 | In Cisco Unified Communications Manager Administration, select Device > Device Settings > SIP Profile |
|---|---|
| Step 2 | Set the Start Media Port and  Stop Media Port fields for the audio port range. |
| Step 3 | Select Save . |
| Step 4 | Select one of the following windows: System > Enterprise Phone Configuration Device > Device Settings > Common Phone Profile Device > Phone > Phone Configuration |
| Step 5 | Set the Start Video RTP Port and Stop Video RTP Port fields for the range of ports required. The following rules apply when configuring the video port fields: The value in the Stop Video RTP Port field must be larger than the value in the Start Video RTP Port field. The difference between the Start Video RTP Port field and the Stop Video RTP Port field must be at least 16. |
| Step 6 | Select Save . |

| Softkey | Call State | Description |
|---|---|---|
| Redirect | Ringing, Connected, On Hold | Divert the selected call to a pre-configured
                                          				  target. |
| Intercept | All states | Divert a call from the assistant's phone to
                                          				  the manager's phone and auto answer it. |
| Set Watch | All states | View the status of call handled by an
                                          				  assistant. |
| TransVM | Ringing, Connected, On Hold | Redirect the selected call to the manager's
                                          				  voice mail. |
| Divert All | All states | Divert all calls that are routed to the
                                          				  manager to a preconfigured target. |

| Note | Intercept, Set Watch, and Divert All should only be configured for a
                                             			 manager phone in proxy line mode. |
|---|---|

| Step 1 | Configure the phones and
                                          			 users. |
|---|---|
| Step 2 | Associate the phones to the users. |
| Step 3 | Activate the Cisco IP Manager Assistant service in the Service
                                          			 Activation window. |
| Step 4 | Configure system administration parameters. |
| Step 5 | If required, configure IPMA clusterwide services parameters. |
| Step 6 | (Optional) Configure the user CAPF profile |
| Step 7 | (Optional) Configure the IPMA service parameters for security |
| Step 8 | Stop and restart the IPMA service. |
| Step 9 | Configure phone parameter, manager, and assistant settings,
                                          			 including the softkey templates. |
| Step 10 | Configure Cisco Unified Communications Manager Assistant
                                          			 application. |
| Step 11 | Configure dial rules. |
| Step 12 | Install the Assistant Console application. |
| Step 13 | Configure the manager and assistant console applications. |

| Note | For
                                                				configuration information, see the Cisco Visual Voicemail documentation at http://www.cisco.com/c/en/us/support/unified-communications/visual-voicemail/model.html . |
|---|---|

| Step 1 | In Cisco
                                          			 Unified Communications Manager Administration, choose Device > Device
                                                				  Settings > Phone Services . |
|---|---|
| Step 2 | Select Add
                                             				New to create a new service for Visual Voicemail. |
| Step 3 | In the IP
                                          			 Phone Service Configuration window, enter the following information in their
                                          			 respective fields: Service Name—Enter VisualVoiceMail . ASCII Service Name—Enter VisualVoiceMail . Service URL—Enter as Application:Cisco/VisualVoiceMail . Service Category—Select XML Service from the pulldown menu. Service Type—Select Messages from the pulldown menu. |
| Step 4 | Check Enable and click Save . Note Ensure that
                                                         				  you do not check Enterprise Subscription . | Note | Ensure that
                                                         				  you do not check Enterprise Subscription . |
| Note | Ensure that
                                                         				  you do not check Enterprise Subscription . |
| Step 5 | In the Service
                                          			 Parameter Information window, click New
                                             				Parameter and enter the following information in their respective
                                          			 fields: Parameter Name. Enter
                                                				  voicemail_server. Parameter Display Name.
                                                				  Enter voicemail_server. Default Value. Enter the
                                                				  hostname of the primary Unity Server. Parameter Description |
| Step 6 | Check Parameter is Required and click Save . Note Ensure that
                                                         				  you do not check Parameter is a Password (mask contents) . | Note | Ensure that
                                                         				  you do not check Parameter is a Password (mask contents) . |
| Note | Ensure that
                                                         				  you do not check Parameter is a Password (mask contents) . |
| Step 7 | Close the
                                          			 window and select Save again in the Phone Service Configuration
                                          			 window. |

| Note | Ensure that
                                                         				  you do not check Enterprise Subscription . |
|---|---|

| Note | Ensure that
                                                         				  you do not check Parameter is a Password (mask contents) . |
|---|---|

| Note | For
                                                   				configuration information, see the Cisco Visual Voice Mail documentation at http://www.cisco.com/c/en/us/support/unified-communications/visual-voicemail/model.html . |
|---|---|

| Step 1 | In Cisco
                                             			 Unified Communications Manager Administration, choose Device > Phone . |
|---|---|
| Step 2 | Select the
                                             			 device associated to the user you are searching for. |
| Step 3 | In the
                                             			 Related Links drop-down, choose Subscribe/Unsubscribe Services and click Go . |
| Step 4 | Select the
                                             			 VisualVoiceMail Service you created, then choose Next > Subscribe . |

| Note | Cisco Unified
                                          			 Communications Manager allows you to configure any softkey in a softkey
                                          			 template, but unsupported softkeys do not display on the phone. |
|---|---|

| Feature | Configurable Softkeys in the Softkey Template configuration | Supported
                                          					 as a Softkey | Notes |
|---|---|---|---|
| Answer | Answer
                                          					 (Answer) | Supported | — |
| Call Back | Call Back
                                          					 (CallBack) | Supported | — |
| Call
                                          					 Forward All | Forward
                                          					 All (cfwdAll) | Supported | Phone
                                          					 displays Forward all or Forward off. |
| Call Park | Call Park
                                          					 (Park) | Supported | — |
| Call
                                          					 Pickup | Pick Up
                                          					 (Pickup) | Supported | — |
| Barge | Barge | Supported | Barge uses the built-in conference bridge |
| cBarge | Conference
                                          					 Barge | Supported | cBarge uses the Cisco Unified Communications Manager conference bridge. The softkey label is Barge. |
| Conference | Conference
                                          					 (Confrn) | Supported | Conference
                                          					 is a dedicated button. |
| Conference
                                          					 List | Conference
                                          					 List (ConfList) | Supported | Phone
                                          					 displays Show detail. |
| Divert | Immediate Divert (iDivert) | Supported | Phone
                                          					 displays Decline. |
| Do Not
                                          					 Disturb | Toggle
                                          					 Do Not Disturb (DND) | Supported | Configure Do Not Disturb as a programmable line button or as a
                                          					 softkey. |
| End Call | End Call
                                          					 (EndCall) | Supported | — |
| Group
                                          					 Pickup | Group
                                          					 Pick UP (GPickUp) | Supported | — |
| Hold | Hold
                                          					 (Hold) | Supported | Hold is
                                          					 a dedicated button. |
| Hunt
                                          					 Group | HLog
                                          					 (HLog) | Supported | Configure Hunt Group as a programmable feature button. |
| Join | Join
                                          					 (Join) | Not supported | — |
| Malicious Call Identification | Toggle
                                          					 Malicious Call Identification (MCID) | Supported | Configure Malicious Call Identification as a programmable
                                          					 feature button or as a softkey. |
| Meet Me | Meet Me
                                          					 (MeetMe) | Supported | — |
| Mobile
                                          					 Connect | Mobility
                                          					 (Mobility) | Supported | Configure Mobile Connect as a softkey. |
| New Call | New Call
                                          					 (NewCall) | Supported | — |
| Other
                                          					 Pickup | Other
                                          					 Pickup (oPickup) | Supported | — |
| PLK
                                          					 Support for Queue Statistics | Queue
                                          					 Status | Not supported | — |
| Quality
                                          					 Reporting Tool | Quality
                                          					 Reporting Tool (QRT) | Supported | Configure Quality Reporting Tool as a programmable feature
                                          					 button or as a softkey. |
| Redial | Redial
                                          					 (Redial) | Supported | — |
| Remove
                                          					 Last Conference Participant | Remove
                                          					 Last Conference Participant (Remove) | Not supported | — |
| Resume | Resume
                                          					 (Resume) | Supported | — |
| Select | Select
                                          					 (Select) | Not supported | — |
| Speed
                                          					 Dial | Abbreviated Dial (AbbrDial) | Supported | Phone
                                          					 displays SpeedDial. |
| Transfer | Transfer
                                          					 (Trfr) | Supported | Transfer
                                          					 is a dedicated button. |
| Video
                                          					 Mode Command | Video
                                          					 Mode Command (VidMode) | Not supported | — |

| Step 1 | In Cisco
                                       			 Unified Communications Manager Administration, select one of the following windows: To configure
                                                			 softkey templates, select Device > Device
                                                      				  Settings > SoftkeyTemplate . To assign a
                                                			 softkey template to a phone, select Device > Phone and configure the Softkey
                                                			 Template field. |
|---|---|
| Step 2 | Save the changes. |

| Step 1 | From Cisco Unified Communications Manager Administration, choose Device > Device
                                                				  Settings > Phone Button Template . |
|---|---|
| Step 2 | Click Find . |
| Step 3 | Select the phone model. |
| Step 4 | Select Copy , enter a name for the new template, and
                                          			 then select Save . The Phone Button Template Configuration window opens. |
| Step 5 | Identify the button that you would like to assign, and select Service URL from the Features drop-down list that associates with the line. |
| Step 6 | Select Save to create a new phone button template
                                          			 that uses the service URL. |
| Step 7 | Choose Device > Phone and open the Phone Configuration window for the phone. |
| Step 8 | Select the new phone button template from the Phone Button
                                          			 Template drop-down list. |
| Step 9 | Select Save to store the change and then select Apply Config to implement the change. The phone user can now access the  Self Care Portal and
                                             				associate the service with a button on the phone. |

| Step 1 | Modify the
                                          			 phone button template to include the All Calls button. |
|---|---|
| Step 2 | Assign the
                                          			 template to the phone. |

| Step 1 | From Cisco Unified Communications Manager Administration, choose Device > Device
                                                				  Settings > Phone Services . The Find and List IP Phone Services window displays. |
|---|---|
| Step 2 | Click Add New . The IP Phone Services Configuration window displays. |
| Step 3 | Enter the following settings: Service Name: Enter Personal Address Book . Service Description: Enter an optional description of the
                                                   					 service. Service URL For PAB, enter the following URL: http ://<Unified
                                                   						CM-server-name> :8080/ccmpd/login.do?name=#DEVICENAME#&service=pab For Fast Dial, enter the following URL: http ://<Unified-CM-server-name> :8080/ccmpd/login.do?name=#DEVICENAME#&service=fd Secure Service URL For PAB, enter the following URL: https ://<Unified
                                                   						CM-server-name> :8443/ccmpd/login.do?name=#DEVICENAME#&service=pab For Fast Dial, enter the following URL: https ://<Unified-CM-server-name> :8443/ccmpd/login.do?name=#DEVICENAME#&service=fd Service Category: Select XML Service . Service Type: Select Directories . Enable: Select the check box. http://<IP_address> or https://<IP_address> (Depends on the protocol that the Cisco IP Phone supports.) |
| Step 4 | Select Save . Note If you change the service URL, remove an IP Phone service
                                                         				  parameter, or change the name of a phone service parameter for a phone service
                                                         				  to which users are subscribed, you must click Update Subscriptions to update all
                                                         				  currently subscribed users with the changes; otherwise, users must resubscribe to the
                                                         				  service to rebuild the correct URL. | Note | If you change the service URL, remove an IP Phone service
                                                         				  parameter, or change the name of a phone service parameter for a phone service
                                                         				  to which users are subscribed, you must click Update Subscriptions to update all
                                                         				  currently subscribed users with the changes; otherwise, users must resubscribe to the
                                                         				  service to rebuild the correct URL. |
| Note | If you change the service URL, remove an IP Phone service
                                                         				  parameter, or change the name of a phone service parameter for a phone service
                                                         				  to which users are subscribed, you must click Update Subscriptions to update all
                                                         				  currently subscribed users with the changes; otherwise, users must resubscribe to the
                                                         				  service to rebuild the correct URL. |

| Note | If you change the service URL, remove an IP Phone service
                                                         				  parameter, or change the name of a phone service parameter for a phone service
                                                         				  to which users are subscribed, you must click Update Subscriptions to update all
                                                         				  currently subscribed users with the changes; otherwise, users must resubscribe to the
                                                         				  service to rebuild the correct URL. |
|---|---|

| Step 1 | From Cisco Unified Communications Manager Administration, choose Device > Device
                                                				  Settings > Phone Button Template . |
|---|---|
| Step 2 | Click Find . |
| Step 3 | Select the phone model. |
| Step 4 | Select Copy , enter a name for the new template, and
                                          			 then select Save . The Phone Button Template Configuration window opens. |
| Step 5 | Identify the button that you would like to assign, and select Service URL from the Features drop-down list that associates with the line. |
| Step 6 | Select Save to create a new phone button template
                                          			 that uses the service URL. |
| Step 7 | Choose Device > Phone and open the Phone Configuration window for the phone. |
| Step 8 | Select the new phone button template from the Phone Button
                                          			 Template drop-down list. |
| Step 9 | Select Save to store the change and then select Apply Config to implement the change. The phone user can now access the Self Care Portal and
                                             				associate the service with a button on the phone. |

| Note | Enter the Alternate TFTP server setting when you're configuring an off-premises phone for SSL VPN to ASA using a built-in
                                          client. |
|---|---|

| Step 1 | In Cisco Unified Communications Manager Administration, select Device > Phone . |
|---|---|
| Step 2 | Locate the phone that you need to set up. |
| Step 3 | Navigate to the Product Specific Configuration area and set the Line Mode field to Enhanced Line Mode . |
| Step 4 | Navigate to the Device Information  area and set the Phone Button Template field to a customized template. |
| Step 5 | Select Apply Config . |
| Step 6 | Select Save . |
| Step 7 | Restart the phone. |

| Feature | Supported | Firmware Release |
|---|---|---|
| Answer | Yes | 11.5(1) and later |
| Automatically Answer Calls | Yes | 11.5(1) and later |
| Barge/cBarge | Yes | 11.5(1) and later |
| Directed Call Park with BLF | Yes | 12.0(1) and later |
| Bluetooth Smartphone integration | No | - |
| Bluetooth USB Headsets | Yes | 11.5(1) and later |
| Call Back | Yes | 11.5(1) and later |
| Call Chaperone | No | - |
| Call Forward All | Yes | 11.5(1) and later |
| Call Park | Yes | 12.0(1) and later |
| Call Park Line Status | Yes | 12.0(1) and later |
| Call Pickup | Yes | 11.5(1) and later |
| Call Pickup Line Status | Yes | 11.5(1) and later |
| Call Forward All on Multiple Lines | Yes | 11.5(1) and later |
| Cisco Extension Mobility Cross Cluster | Yes | 12.0(1) and later supports this feature. |
| Cisco IP Manager Assistant (IPMA) | No | - |
| Cisco Unified Communications Manager Express | No | - |
| Conference | Yes | 11.5(1) and later |
| Computer Telephony Integration (CTI) applications | Yes | 11.5(1) and later |
| Decline | Yes | 11.5(1) and later |
| Device Invoked Recording | Yes | 11.5(1)SR1 and later |
| Do Not Disturb | Yes | 11.5(1) and later |
| Enhanced SRST | No | - |
| Extension Mobility | Yes | 11.5(1) and later |
| Group Pickup | Yes | 12.0(1) and later supports this feature. |
| Hold | Yes | 11.5(1) and later |
| Hunt Groups | Yes. | 12.0(1) and later |
| Incoming Call Alert with configurable timer | No | - |
| Intercom | Yes | 11.5(1) and later |
| Key Expansion Module | Cisco IP Phone 8851/8861 Key Expansion Module and Cisco IP Phone 8865 Key Expansion Module support Enhanced Line Mode | 12.0(1) and later |
| Malicious Call Identification (MCID) | Yes | 11.5(1) and later |
| Meet Me | Yes | 11.5(1) and later |
| Mobile Connect | Yes | 11.5(1) and later |
| Multilevel Precedence and Preemption | No | - |
| Mute | Yes | 11.5(1) and later |
| Other PickUp | Yes | 12.0(1) and later |
| Programmable Line Key (PLK) Support for Queue Status | Yes | 11.5(1) and later |
| Privacy | Yes | 11.5(1) and later |
| Queue Status | Yes | 11.5(1) and later |
| Quality Reporting Tool (QRT) | Yes | 11.5(1) and later |
| Right to Left locale support | No | - |
| Redial | Yes | 11.5(1) and later |
| Silent Monitoring and Recording | Yes | 11.5(1)SR1 and later |
| Speed Dial | Yes | 11.5(1) and later |
| Survivable Remote Site Telephony (SRST) | Yes | 11.5(1) and later |
| Transfer | Yes | 11.5(1) and later |
| Uniform Resource Identifier (URI) Dialing | Yes | 11.5(1) and later |
| Video Calls | Yes | 11.5(1) and later |
| Visual Voicemail | Yes | 11.5(1) and later |
| Voicemail | Yes | 11.5(1) and later |

| Step 1 | In Cisco
                                       			 Unified Communications Manager Administration, select Device > Phone . |
|---|---|
| Step 2 | Set the TLS
                                       			 Resumption Timer parameter. The range for
                                       			 the timer is 0 to 3600 sec. The default value is 3600. If the field is set to
                                       			 0, then TLS session resumption is disabled. |

| Note | This procedure only applies to Bluetooth enabled phones. Cisco IP Phone 8811, 8841, 8851NR, and 8865NR do not support Bluetooth. |
|---|---|

| Step 1 | In Cisco
                                       			 Unified Communications Manager Administration, select Phone > Device . |
|---|---|
| Step 2 | Locate the
                                       			 phone you want to modify. |
| Step 3 | Locate the
                                       			 Bluetooth field and set the field to Enabled . |
| Step 4 | Locate the
                                       			 Allow Bluetooth Mobile Handsfree Mode field, and set the field to Enabled . |
| Step 5 | Save the
                                       			 changes and apply them to the phone. |

| Video type | Video resolution | Frames per second (fps) | Video bit rate range |
|---|---|---|---|
| 720p | 1280 x 720 | 30 | 1360–2500 kbps |
| 720p | 1280 x 720 | 15 | 790–1359 kbps |
| WVGA | 800 x 480 | 30 | 660–789 kbps |
| WVGA | 800 x 480 | 15 | 350–399 kbps |
| 360p | 640 x 360 | 30 | 400–659 kbps |
| 360p | 640 x 360 | 15 | 210–349kbps |
| 240p | 432 x 240 | 30 | 180–209kbps |
| 240p | 432 x 240 | 15 | 64–179kbps |
| VGA | 640 x 480 | 30 | 520–1500kbps |
| VGA | 640 x 480 | 15 | 280–519kbps |
| CIF | 352 x 288 | 30 | 200–279 kbps |
| CIF | 352 x 288 | 15 | 120–199 kbps |
| SIF | 352 x 240 | 30 | 200–279 kbps |
| SIF | 352 x 240 | 15 | 120–199 kbps |
| QCIF | 176 x 144 | 30 | 94–119 kbps |
| QCIF | 176 x 144 | 15 | 64–93 kbps |

| Note | You can manage and configure headsets through Cisco Unified Communications Manager Administration version 11.5(1)SU7. |
|---|---|

| Step 1 | Go to the following URL: https://software.cisco.com/download/home/286320550 . |
|---|---|
| Step 2 | Choose Headsets 500 Series . |
| Step 3 | Select your headset series. |
| Step 4 | Choose a release folder and select the zip file. |
| Step 5 | Click the Download or Add to cart button, and follow the prompts. |
| Step 6 | Unzip the file to a directory on your PC. |

| Step 1 | Open the defaultheadsetconfig.json file with a text editor. |
|---|---|
| Step 2 | Edit the updatedTime and the headset parameter values you wish to modify. A sample script is shown below. This script is provided for reference only. Use it as a guide as you configure your headset
                                             parameters. Use the JSON file that was included with your firmware load. {
  "headsetConfig": {
    "templateConfiguration": {
      "configTemplateVersion": "1", "updatedTime" : 1537299896,
      "reportId": 3,
      "modelSpecificSettings": [
        {
          "modelSeries": "530",
          "models": [
            "520",
            "521",
            "522",
            "530",
            "531",
            "532"
          ],
          "modelFirmware": [
            {
              "firmwareName": "LATEST",
              "latest": true,
              "firmwareParams": [
                {
                  "name": "Speaker Volume",
                  "access": "Both",
                  "usageId": 32, "value" : 7
                },
                {
                  "name": "Microphone Gain",
                  "access": "Both",
                  "usageId": 33, "value" : 2
                },
                {
                  "name": "Sidetone",
                  "access": "Both",
                  "usageId": 34, "value" : 1
                },
                {
                  "name": "Equalizer",
                  "access": "Both",
                  "usageId": 35, "value" : 3
                }
              ]
            }
          ]
        },
        {
          "modelSeries": "560",
          "models": [
            "560",
            "561",
            "562"
          ],
          "modelFirmware": [
            {
              "firmwareName": "LATEST",
              "latest": true,
              "firmwareParams": [
                {
                  "name": "Speaker Volume",
                  "access": "Both",
                  "usageId": 32, "value" : 7
                },
                {
                  "name": "Microphone Gain",
                  "access": "Both",
                  "usageId": 33, "value" : 2
                },
                {
                  "name": "Sidetone",
                  "access": "Both",
                  "usageId": 34, "value" : 1
                },
                {
                  "name": "Equalizer",
                  "access": "Both",
                  "usageId": 35, "value" : 3
                },
                {
                  "name": "Audio Bandwidth",
                  "access": "Admin",
                  "usageId": 36, "value" : 0
                },
                {
                  "name": "Bluetooth",
                  "access": "Admin",
                  "usageId": 39, "value" : 0
                },
                {
                  "name": "DECT Radio Range",
                  "access": "Admin",
                  "usageId": 37, "value" : 0
                }
                {
                   "name": "Conference",
                  "access": "Admin",
                  "usageId": 41, "value" : 0
              ]
            }
          ]
        }
      ]
    }
  }
} |
| Step 3 | Save the defaultheadsetconfig.json . |

| Step 1 | From Cisco Unified OS Administration, choose Software Upgrades > TFTP File Management . |
|---|---|
| Step 2 | Select Upload File . |
| Step 3 | Select Choose File and navigate to the defaultheadsetconfig.json file. |
| Step 4 | Select Upload File . |
| Step 5 | Click Close . |

| Step 1 | Log in to Cisco Unified Serviceability and choose Tools > Control Center - Feature Services . |
|---|---|
| Step 2 | From the Server drop-down list box, choose the server on which the Cisco TFTP service is running. |
| Step 3 | Click the radio button that corresponds to the Cisco TFTP service. |
| Step 4 | Click Restart . |