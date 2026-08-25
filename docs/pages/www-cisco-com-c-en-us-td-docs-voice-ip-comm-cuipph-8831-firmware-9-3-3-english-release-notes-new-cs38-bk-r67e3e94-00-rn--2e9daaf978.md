---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8831-firmware-9-3-3-english-release-notes-new-cs38-bk-r67e3e94-00-rn--2e9daaf978
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8831/firmware/9_3_3/english/release_notes_new/CS38_BK_R67E3E94_00_rn-9_3_3-8831/CS38_BK_R67E3E94_00_rn-9_3_2-8831_chapter_00.html
retrieved_at: 2026-08-25T13:52:30.617720+00:00
---

Cisco Unified IP Conference Phone 8831 Release Notes for Firmware Release 9.3(3)

# Cisco Unified IP Conference Phone 8831 Release Notes for Firmware Release 9.3(3)

Updated: July 10, 2014

Chapter: Cisco Unified IP Conference Phone 8831 Release Notes for Firmware Release 9.3(3)

## Chapter: Cisco Unified IP Conference Phone 8831 Release Notes for Firmware Release 9.3(3)

# Cisco Unified IP Conference Phone 8831 Release Notes for Firmware Release 9.3(3)

## Introduction

These release notes support Cisco Unified IP Conference Phone 8831  running SIP firmware Release 9.3(3).

The following table lists the Cisco Unified Communications Manager release and protocol compatibility for the Cisco Unified
                           IP Phones.

Cisco Unified IP Conference Phone 8831

SIP

Cisco Unified Communications Manager Release 7.1.5 and later

SIP Firmware Release 9.3(3) is designed and tested to interoperate with Cisco call control, most notably Cisco Unified Communications
                                       Manager Release 9.0(1). Although SIP firmware is IETF RFC 3261 compliant, it is not supported by Cisco TAC or Engineering
                                       for use with non-Cisco call control systems.

## Cisco Unified IP Conference Phone 8831

The Cisco Unified IP Conference Phone 8831 is a full-featured single line conference station that provides voice communication
                           over an IP network. It functions much like a digital business phone, allowing you to place and receive calls and to access
                           features such as mute, hold, transfer, speed dial, call forward, and more. In addition, because conference stations connect
                           to your data network, they offer enhanced IP telephony features, including access to network information and services, and
                           customizable features and services.

The conference phone provides a backlit LCD screen, support for up to ten speed-dial numbers, and a variety of other sophisticated
                           functions. Optional  microphone extension kits provide enhanced room coverage that can be further expanded by linking two
                           units together.

In addition to basic call handling features, your conference phone can provide enhanced productivity features that extend
                           your call handling capabilities. Depending on configuration, the phone supports:

Access to network data, XML applications, and web-based services.

Online customizing of conference station features and services from the User Options web pages.

The phone supports seamless firmware upgrade. If two devices are connected in Linked Mode, firmware upgrades are pushed automatically
                           from the primary unit to the secondary unit.

For information on deploying the conference phone, see Cisco Unified IP Conference Phone 8831 Administration Guide for Cisco Unified Communications Manager , "Cisco Unified IP Conference Phone 8831 setup" .

### Language Support

The default language for Cisco Unified IP Conference Phone 8831 with  Firmware Release 9.3(3) is American English. For other
                              locales, if the language does not support certain words and phrases, the phone displays the English phrase.

Cisco provides locale-specific versions of the Cisco Unified Communications Manager Locale Installer on www.cisco.com. Installed
                              by the system administrator, the locale installer allows the user to view and receive the chosen translated text or tones,
                              if applicable, when a user works with supported interfaces.

Cisco may combine multiple network locales in a single locale installer.

For more information on international user support, see Cisco Unified IP Conference Phone 8831 Administration Guide , "Appendix B" , International user support.

For more information on installing locales, see Cisco Unified Communications Operating System Administration Guide, Release 9.1(1) , "Software upgrades" , Locale installation.

## Related
                        	 Documentation

### Cisco IP Phone 8800 Series Documentation

Refer to
                                 		  publications that are specific to your language, phone model, and call control
                                 		  system. Navigate from the following documentation URL:

https://www.cisco.com/c/en/us/products/collaboration-endpoints/unified-ip-phone-8800-series/index.html

The Deployment Guide is located at the following URL:

https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/products-implementation-design-guides-list.html

### Cisco Unified
                              				Communications Manager Documentation

See the Cisco Unified
                                       				Communications Manager Documentation Guide and other publications that are specific to your Cisco Unified
                                    				Communications Manager release. Navigate from the following documentation URL:

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/tsd-products-support-series-home.html

### Cisco Business Edition
                              				6000 Documentation

Refer to the Cisco Business Edition
                                       				6000 Documentation Guide and other publications that are specific to your Cisco Business Edition
                                    				6000 release. Navigate from the following URL:

https://www.cisco.com/c/en/us/support/unified-communications/business-edition-6000/tsd-products-support-series-home.html

## Features Available with Firmware Release 9.3(3)

### Available Telephony Features

After you add Cisco Unified IP Conference Phones to Cisco Unified
                                 				Communications Manager, you can add functionality. The following table includes a
                                 				list of supported telephony features. You can use Cisco Unified Communications
                                 				Manager Administration to configure many of these features. The Reference column
                                 				lists Cisco Unified Communications Manager and other documentation that contains
                                 				configuration procedures and related information.

For information about the use of these features on the phone, see the Cisco
                                    					Unified IP Conference Phone 8831 User Guide .

Cisco Unified Communications Manager Administration also provides several service
                                             					parameters that are used to configure various telephony functions. For more
                                             					information about access and configuration of service parameters, see the Cisco Unified Communications Manager Administration Guide .

For more information on the functions of a service, select the name of the
                                             					parameter or the question mark help button in the Service Parameter
                                             					Configuration window in CUCM Administration.

Feature

Description

Configuration Reference

Agent Greeting

Allows an agent to create and update a prerecorded greeting that
                                             									plays at the beginning of a call, such as a customer call,
                                             									before the agent begins the conversation with the caller. The
                                             									agent can prerecord a single greeting or multiple greetings as
                                             									needed.

To enable Agent Greeting in the Cisco Unified Communications
                                             									Manager Administration application, choose Device > Phone , locate the IP Phone that you want to configure.
                                             									Scroll to the Device Information Layout pane and set
                                             									Built In Bridge to On or Default .

If Built In Bridge is set to Default, in the Cisco Unified
                                             									Communications Manager Administration application, choose System > Service Parameter and select the appropriate Server and Service.
                                             									Scroll to the Clusterwide Parameters (Device - Phone) pane and
                                             									set Builtin Bridge Enable to On .

For more information, see the following:

- Features and
                                                   											Services Guide for Cisco Unified Communications
                                                   											Manager , "Barge and Privacy"

- Cisco Unified
                                                   											Communications Manager System Guide , "Cisco
                                                   											Unified IP Phones"

Any Call Pickup

Allows users to pick up a call on any line in their call pickup
                                             									group, regardless of how the call was routed to the phone.

For more information, see Features and Services Guide for
                                                										Cisco Unified Communications Manager , "Call
                                                										Pickup" chapter.

Audible Message Waiting Indicator (AMWI)

A stutter tone indicates that a user has one or more new voice
                                             									messages on a line.

The stutter tone is line-specific. You hear it only when
                                                         										using the line with the waiting messages.

For more information, see Cisco Unified Communications
                                                										Manager System Guide , "Cisco Unified IP Phones" chapter.

Auto Answer

Connects incoming calls automatically after a ring or two.

For more information, see Cisco Unified Communications
                                                										Manager Administration Guide , "Directory Number
                                                										Setup" chapter.

Auto Pickup

Allows a user to use one-touch pickup functionality for call
                                             									pickup features.

For more information, see Features and Services Guide for
                                                										Cisco Unified Communications Manager , "Call
                                                										Pickup" chapter.

Block External to External Transfer

Prevents users from transferring an external call to another
                                             									external number.

For more information, see Features and Services Guide for
                                                										Cisco Unified Communications Manager , "External
                                                										Call Transfer Restrictions" chapter.

Call Back

Provides users with an audio and visual alert on the phone when a
                                             									busy or unavailable party becomes available.

For more information, see the following:

- Cisco Unified
                                                   											Communications Manager System Guide , "Cisco
                                                   											Unified IP Phones"

- Features and
                                                   											Services Guide for Cisco Unified Communications
                                                   											Manager , "Cisco Call Back"

Call Display Restrictions

Determines the information that will display for calling or
                                             									connected lines, depending on the parties who are involved in
                                             									the call.

For more information, see:

- Cisco Unified
                                                   											Communications Manager Administration Guide , "Cisco Unified IP Phone Setup"

- Cisco Unified
                                                   											Communications Manager System Guide , "Understanding Route Plans"

- Features and
                                                   											Services Guide for Cisco Unified Communications
                                                   											Manager , "Call Display Restrictions"

Call Forward

Allows users to redirect incoming calls to another number. Call
                                             									Forward options include Call Forward All, Call Forward Busy,
                                             									Call Forward No Answer, and Call Forward No Coverage.

For more information, see the following:

- Cisco Unified
                                                   											Communications Manager Administration Guide , "Directory Number Setup"

- Cisco Unified
                                                   											Communications Manager System Guide , "Cisco
                                                   											Unified IP Phones"

Customize Cisco Unified Communications Manager Self Care
                                                   											Portal display

Call Forward All Loop Breakout

Detects and prevents Call Forward All loops. When a Call Forward
                                             									All loop is detected, the Call Forward All configuration is
                                             									ignored and the call rings through.

For more information, see Cisco Unified Communications
                                                										Manager System Guide , "Cisco Unified IP Phones" chapter.

Call Forward All Loop Prevention

Prevents a user from configuring a Call Forward All destination
                                             									directly on the phone that creates a Call Forward All loop or
                                             									that creates a Call Forward All chain with more hops than the
                                             									existing Forward Maximum Hop Count service parameter
                                             									allows.

For more information, see Cisco Unified Communications
                                                										Manager System Guide , "Cisco Unified IP Phones" chapter.

Call Forward Configurable Display

Allows you to specify information that appears on a phone when a
                                             									call is forwarded. This information can include the caller name,
                                             									caller number, redirected number, and original dialed number.

For more information, see the following:

- Cisco Unified
                                                   											Communications Manager Administration Guide , "Directory Number Setup"

- Cisco Unified
                                                   											Communications Manager System Guide , "Cisco
                                                   											Unified IP Phones"

Call Forward Destination Override

Allows you to override Call Forward All (CFA) in cases where the
                                             									CFA target places a call to the CFA initiator. This feature
                                             									allows the CFA target to reach the CFA initiator for important
                                             									calls. The override works whether the CFA target phone number is
                                             									internal or external.

For more information, see the Cisco Unified Communications
                                                										Manager System Guide , "Directory Numbers" chapter.

Call Forward Notification

Allows you to configure the information that the user sees when
                                             									receiving a forwarded call.

For more information, see Call Forward Notification setup.

Call History for Shared Line

Log missed calls for a shared line

Log answered calls for a shared line

For more information, see Enable Call History for shared line.

Call Park

Allows users to park (temporarily store) a call and then retrieve
                                             									the call by using another phone in the Cisco Unified
                                             									Communications Manager system.

For more information, see the Features and Services Guide
                                                										for Cisco Unified Communications Manager , "Call
                                                										Park and Directed Call Park" chapter.

Call Pickup

Allows users to redirect a call that is ringing on another phone
                                             									within their pickup group to their phone.

You can configure an audio and visual alert for the primary line
                                             									on the phone. This alert notifies the users that a call is
                                             									ringing in their pickup group.

For more information, see the Features and Services Guide
                                                										for Cisco Unified Communications Manager , "Call
                                                										Pickup" chapter.

Call Recording

Allows a supervisor to record an active call. The user might hear
                                             									a recording audible alert tone during a call when it is being
                                             									recorded.

When a call is secured, the security status of the call is
                                             									displayed as a lock icon on Cisco Unified IP Phones. The
                                             									connected parties might also hear an audible alert tone that
                                             									indicates the call is secured and is being recorded.

When an active call is being monitored or recorded, you can
                                                         										receive or place intercom calls; however, if you place an
                                                         										intercom call, the active call will be put on hold, which
                                                         										causes the recording session to terminate and the monitoring
                                                         										session to suspend. To resume the monitoring session, the
                                                         										party whose call is being monitored must resume the call.

For more information, see Features and Services Guide for
                                                										Cisco Unified Communications Manager , "Monitoring
                                                										and Recording" chapter.

Call Waiting

Indicates (and allows users to answer) an incoming call that
                                             									rings while on another call. Incoming call information appears
                                             									on the phone display.

For more information, see:

Cisco Unified Communications Manager System
                                                      												Guide , "Directory Numbers"

Phone Call Waiting setup

Caller ID

Caller identification such as a phone number, name, or other
                                             									descriptive text appear on the phone display.

For more information, see:

- Cisco Unified
                                                   											Communications Manager Administration Guide , "Cisco Unified IP Phone Setup"

- Cisco Unified
                                                   											Communications Manager System Guide , "Understanding Route Plans"

- Features and
                                                   											Services Guide for Cisco Unified Communications
                                                   											Manager , "Call Display Restrictions"

- Cisco Unified
                                                   											Communications Manager Administration Guide , "Directory Number Setup"

Caller ID Blocking

Allows a user to block their phone number or email address from
                                             									phones that have caller identification enabled.

For more information, see:

- Cisco Unified
                                                   											Communications Manager System Guide , "Understanding Route Plans"

- Cisco Unified
                                                   											Communications Manager Administration Guide , "Directory Number Setup"

Calling Party Normalization

Calling party normalization presents phone calls to the user with
                                             									a dialable phone number. Any escape codes are added to the
                                             									number so that the user can easily connect to the caller again.
                                             									The dialable number is saved in the call history and can be
                                             									saved in the Personal Address Book.

For more information, see Calling Party Normalization.

cBarge

Allows a user to join a nonprivate call on a shared phone line.
                                             									cBarge adds a user to a call and converts it into a conference,
                                             									allowing the user and other parties to access conference
                                             									features

For more information, see:

- Cisco Unified
                                                   											Communications Manager Administration Guide , "Cisco Unified IP Phone Setup"

- Cisco Unified
                                                   											Communications Manager System Guide , "Cisco
                                                   											Unified IP Phones"

- Features and
                                                   											Services Guide for Cisco Unified Communications
                                                   											Manager , "Barge and Privacy"

Cisco Extension Mobility

Allows users to temporarily access their Cisco Unified IP Phone
                                             									configuration such as line appearances and services from a
                                             									shared Cisco Unified IP Phone by logging into the Cisco
                                             									Extension Mobility service on that phone when they log into the
                                             									Cisco Extension Mobility service on that phone.

Cisco Extension Mobility can be useful if users work from a
                                             									variety of locations within your company or if they share a
                                             									workspace with coworkers.

For more information, see " Extension Mobility" chapter in
                                             									the Cisco Unified Communications Manager Features and
                                                										Services Guide .

Cisco WebDialer

Allows users to make calls from web and desktop applications.

For more information, see Features and Services Guide for
                                                										Cisco Unified Communications Manager , "Web
                                                										Dialer" chapter.

Conference

- Allows a user to
                                                										talk simultaneously with multiple parties by calling each
                                                										participant individually. Conference features include
                                                										Conference and Meet Me.

- Allows a
                                                										noninitiator in a standard (ad hoc) conference to add or
                                                										remove participants; also allows any conference participant
                                                										to join together two standard conferences on the same line.

The service parameter, Advance Adhoc Conference, (disabled by
                                             									default in Cisco Unified Communications Manager Administration)
                                             									allows you to enable these features.

For information on conferences, see Cisco Unified
                                                										Communications Manager System Guide , "Conference
                                                										Bridges" chapter.

For more information, see Cisco Unified Communications
                                                										Manager System Guide , "Cisco Unified IP Phones" chapter.

Be sure to inform your users whether these features are
                                                         										activated.

CTI Applications

A computer telephony integration (CTI) route point can designate
                                             									a virtual device to receive multiple, simultaneous calls for
                                             									application-controlled redirection.

For more information, see Cisco Unified Communications
                                                										Manager Administration Guide , "CTI Route Point
                                                										Setup" chapter.

Device Invoked Recording

Provides end users with the ability to record their telephone
                                             									calls via a softkey.

In addition administrators may continue to record telephone calls
                                             									via the CTI User Interface.

For more information, see Enable Device Invoked Recording.

Directed Call Park

Allows a user to transfer an active call to an available directed
                                             									call park number that the user dials.

If you implement Directed Call Park, avoid configuring the
                                                         										Park softkey. This prevents users from confusing the two
                                                         										Call Park features.

For more information, see Features and Services Guide for
                                                										Cisco Unified Communications Manager , "Call Park
                                                										and Directed Call Park" chapter.

Directed Call Pickup

Allows a user to answer a call that is ringing on a particular
                                             									directory number.

For more information, see Features and Services Guide for
                                                										Cisco Unified Communications Manager , "Call
                                                										Pickup" chapter.

Direct Transfer

Allows users to connect two calls to each other without remaining
                                             									on the line.

For more information, see Cisco Unified Communications
                                                										Manager System Guide , “Cisco Unified IP Phones”
                                             									chapter.

Distinctive Ring

Users can customize how their phone indicates an incoming call
                                             									and a new voice mail message.

For more information, see Features and Services Guide for
                                                										Cisco Unified Communications Manager , "Call
                                                										Pickup" chapter.

Divert

Allows a user to transfer a ringing, connected, or held call
                                             									directly to a voice-messaging system. When a call is diverted,
                                             									the line becomes available to make or receive new calls.

For more information, see Features and Services Guide for
                                                										Cisco Unified Communications Manager , "Immediate
                                                										Divert" chapter.

Do Not Disturb (DND)

When DND is turned on, either no audible rings occur during the
                                             									ringing-in state of a call, or no audible or visual
                                             									notifications of any type occur.

The following DND-related parameters are configurable in
                                             									Cisco Unified Communications Manager Administration:

- Do Not Disturb:
                                                										This check box allows you to enable DND on a per-phone
                                                										basis. Use Cisco Unified Communications Manager
                                                      												Administration > Device > Phone > Phone Configuration .

- DND Incoming Call
                                                										Alert: Choose the type of alert to play, if any, on a phone
                                                										for incoming calls when DND is active. This parameter is
                                                										located on both the Common Phone Profile page and the Phone
                                                										configuration page (Phone Configuration window value takes
                                                										precedence).

For more information, see Features and Services Guide for
                                                										Cisco Unified Communications Manager , "Do Not
                                                										Disturb" chapter.

EnergyWise

Enables an IP Phone to sleep (power down) and wake (power up) at
                                             									predetermined times, to promote energy savings.

For more information, see EnergyWise on the Cisco Unified IP
                                             									Phone setup.

Enhanced Room Coverage

Optional microphone extension kits provide enhanced room coverage
                                             									that can be further expanded by linking two units together in
                                             									Linked Mode.

Cisco Unified IP Conference Phone 8831 User
                                                         												Guide for Cisco Unified Communication
                                                         												Manager , "Conference Phone Link Mode" chapter.

Cisco Unified IP Conference Phone 8831 User
                                                         												Guide for Cisco Unified Communication
                                                         												Manager , "Enhanced Room Coverage" chapter.

Fast Dial Service

Allows a user to enter a Fast Dial code to place a call. Fast
                                             									Dial codes can be assigned to phone numbers or Personal Address
                                             									Book entries. (See "Services" in this table.)

For more information, see Modify phone button template for PAB or
                                             									Fast Dial.

Group Call Pickup

Allows a user to answer a call that is ringing on a directory
                                             									number in another group.

For more information, see Features and Services Guide for
                                                										Cisco Unified Communications Manager , "Call
                                                										Pickup" chapter.

Hold Reversion

Limits the amount of time that a call can be on hold before
                                             									reverting back to the phone that put the call on hold and
                                             									alerting the user.

Reverting calls are distinguished from incoming calls by a single
                                             									ring (or beep, depending on the new call indicator setting for
                                             									the line). This notification repeats at intervals if not
                                             									resumed.

A call that triggers Hold Reversion also displays an animated
                                             									icon in the call bubble.

You can configure call focus priority to favor incoming or
                                             									reverting calls.

For more information about configuring this feature, see Features and Services Guide for Cisco Unified
                                                										Communications Manager , "Hold Reversion" chapter.

Hold Status

Enables phones with a shared line to distinguish between the
                                             									local and remote lines that placed a call on hold.

No configuration is required.

Hold/Resume

Allows the user to move a connected call from an active state to
                                             									a held state.

- Requires no
                                                										configuration, unless you want to use Music On Hold. See "Music On Hold" in this table for information.

- See "Hold
                                                   											Reversion" in this table.

HTTP Download

Enhances the file download process to the phone to use HTTP by
                                             									default. If the HTTP download fails, the phone reverts to using
                                             									the TFTP download.

No configuration is required.

Jitter Buffer

The Jitter Buffer feature handles jitter from 10 milliseconds
                                             									(ms) to 1000 ms for both audio and video streams.

No configuration required.

Linked Mode

Enhances the audio coverage area by using a daisy cable to
                                             									connect two conference phone Sound Base units.

When linked, voice, dial tone, ringer and base LED features are
                                             									synchronized between the two devices.

Cisco Unified IP Conference Phone 8831 User
                                                         												Guide , "Conference Phone Link Mode"

Malicious Caller Identification (MCID)

Allows users to notify the system administrator about suspicious
                                             									calls that are received.

For more information, see:

- Cisco
                                                   											Unified Communications Manager System Guide , "Cisco Unified IP Phones"

- Features and
                                                   											Services Guide for Cisco Unified Communications
                                                   											Manager , "Malicious Call Identification"

Meet Me Conference

Allows a user to host a Meet Me conference in which other
                                             									participants call a predetermined number at a scheduled time.

For more information, see Cisco Unified Communications
                                                										Manager Administration Guide , "Meet-Me Number and
                                                										Pattern Setup" chapter.

Message Waiting

Defines directory numbers for message waiting on and off
                                             									indicators. A directly-connected voice-message system uses the
                                             									specified directory number to set or to clear a message waiting
                                             									indication for a particular Cisco Unified IP Phone.

For more information, see the following:

- Cisco Unified
                                                   											Communications Manager Administration Guide , "Message Waiting Setup"

- Cisco Unified
                                                   											Communications Manager System Guide , "Voice
                                                   											Mail Connectivity to Cisco Unified Communications
                                                   											Manager"

Message Waiting Indicator

Displays a New Voicemail status message on the phone screen.

For more information see:

- Cisco Unified
                                                   											Communications Manager Administration Guide , "Message Waiting Setup"

- Cisco Unified
                                                   											Communications Manager System Guide , "Voice
                                                   											Mail Connectivity to Cisco Unified Communications
                                                   											Manager"

Missed Call Logging

Allows a user to specify whether missed calls will be logged in
                                             									the missed calls directory for a given line appearance.

For more information, see Cisco Unified Communications
                                                										Manager Administration Guide , "Directory Number
                                                										Setup" chapter.

Mobile Connect

Enables users to manage business calls using a single phone
                                             									number and pick up in-progress calls on the desk phone and a
                                             									remote device such as a mobile phone. Users can restrict the
                                             									group of callers according to phone number and time of day.

For more information, see Features and Services Guide for
                                                										Cisco Unified Communications Manager , "Cisco
                                                										Unified Mobility" chapter.

Mobile Voice Access

Extends Mobile Connect capabilities by allowing users to access
                                             									an interactive voice response (IVR) system to originate a call
                                             									from a remote device such as a cellular phone.

For more information, see Features and Services Guide for
                                                										Cisco Unified Communications Manager , "Cisco
                                                										Unified Mobility" chapter.

Monitoring and Recording

Allows a supervisor to silently monitor an active call. The
                                             									supervisor cannot be heard by either party on the call. The user
                                             									might hear a monitoring audible alert tone during a call when it
                                             									is being monitored.

When a call is secured, the security status of the call is
                                             									displayed as a lock icon on Cisco Unified IP Phones. The
                                             									connected parties might also hear an audible alert tone that
                                             									indicates the call is secured and is being monitored.

When an active call is being monitored or recorded, the use
                                                         										can receive or place intercom calls; however, if the user
                                                         										place an intercom call, the active call will be put on hold,
                                                         										which causes the recording session to terminate and the
                                                         										monitoring session to suspend. To resume the monitoring
                                                         										session, the party whose call is being monitored must resume
                                                         										the call.

For more information, see Features and Services Guide for
                                                										Cisco Unified Communications Manager , "Monitoring
                                                										and Recording" chapter.

Mute

Mutes the conference phone from the Sound Base, DCU or connected
                                             									external microphones.

Requires no configuration.

No Alert Name

Makes it easier for end users to identify transferred calls by
                                             									displaying the original caller’s phone number. The call appears
                                             									as an Alert Call followed by the caller’s telephone number.

Requires no configuration.

Onhook Dialing

Allows a user to dial a number without going off hook.

For more information, see Cisco Unified IP Conference Phone
                                                										8831 User Guide .

Other Group Pickup

Allows a user to answer a call ringing on a phone in another
                                             									group that is associated with the user's group.

For more information, see Features and Services Guide for
                                                										Cisco Unified Communications Manager , "Call
                                                										Pickup" chapter.

Phone Display Message for Extension Mobility Users

This feature enhances the phone interface for the Extension
                                             									Mobility user by providing friendly messages.

No configuration required.

Plus Dialing

Allows the user to dial E.164 numbers prefixed with a plus (+)
                                             									 sign.

To dial the + sign, the user needs to press and hold the star (*)
                                             									key for at least 1 second. This applies to dialing the first
                                             									digit for an on-hook (including edit mode) or off-hook call.

No configuration required.

Privacy

Prevents users who share a line from adding themselves to a call
                                             									and from viewing information on their phone display about the
                                             									call of the other user.

For more information, see the following:

- Cisco Unified
                                                   											Communications Manager Administration Guide , "Cisco Unified IP Phone Setup"

- Cisco Unified
                                                   											Communications Manager System Guide , "Cisco
                                                   											Unified IP Phones"

- Features and
                                                   											Services Guide for Cisco Unified Communications
                                                   											Manager , "Barge and Privacy"

Quality Reporting Tool (QRT)

Allows users to submit information about problem phone calls by
                                             									pressing a button. QRT can be configured for either of two user
                                             									modes, depending upon the amount of user interaction desired
                                             									with QRT.

For more information, see:

- Cisco Unified
                                                   											Communications Manager System Guide , "Cisco
                                                   											Unified IP Phones"

- Features and
                                                   											Services Guide for Cisco Unified Communications
                                                   											Manager , "Quality Report Tool"

Redial

Allows users to call the most recently dialed phone number by
                                             									pressing a button or the Redial softkey.

Requires no configuration.

Reroute Direct Calls to Remote Destination to Enterprise Number

Reroutes a direct call to a user's mobile phone to the enterprise
                                             									number (desk phone). For an incoming call to remote destination
                                             									(mobile phone), only remote destination rings; desk phone does
                                             									not ring. When the call is answered on their mobile phone, the
                                             									desk phone displays a Remote In Use message. During these calls,
                                             									users can make use of various features of their mobile phone.

For more information, see the Features and Services Guide
                                                										for Cisco Unified Communications Manager , "Cisco
                                                										Unified Mobility" chapter.

Remote Port Configuration

Allows the administrator to configure the speed and duplex
                                             									function of the phone Ethernet ports remotely by using Cisco
                                             									Unified Communications Manager Administration. This enhances the
                                             									performance for large deployments with specific port settings.

If the ports are configured for Remote Port Configuration in
                                                         										Cisco Unified Communications Manager, the data cannot be
                                                         										changed on the phone.

To configure the parameter in the Cisco Unified Communications
                                             									Manager Administration application, choose Device > Phone , select the appropriate IP phone, and scroll to
                                             									the Product Specific Configuration Layout pane (Switch Port
                                             									Remote Configuration or PC Port Remote Configuration).

To configure the setting on multiple phones simultaneously,
                                             									configure the remote configuration in either Enterprise Phone
                                             									Configuration ( System > Enterprise Phone Configuration ) or Common Phone Profile Configuration ( Device > Device Settings > Common Phone Profile . (Switch Port Remote Configuration or PC Port
                                             									Remote Configuration.)

Ringtone Setting

Identifies ring type used for a line when a phone has another
                                             									active call.

- Cisco
                                                      												Unified Communications Manager Administration
                                                      												Guide , "Directory Number Setup"

Cisco Unified Communications Manager
                                                         												Administration Guide , "Custom Phone
                                                         												Rings"

Secure Conference

- Allows secure
                                                										phones to place conference calls using a secured conference
                                                										bridge.

- As new participants
                                                										are added by using Conf, Join, cBarge, Barge softkeys or
                                                										MeetMe conferencing, the secure call icon displays as long
                                                										as all participants use secure phones.

- The Conference List
                                                										displays the security level of each conference participant.
                                                										Initiators can remove nonsecure participants from the
                                                										Conference List. (Non-initiators can add or remove
                                                										conference participants if the Advanced Adhoc Conference
                                                										Enabled parameter is set.)

For additional information, see the following:

- Cisco Unified
                                                   											Communications Manager System Guide , "Conference Bridges"

- Cisco Unified
                                                   											Communications Manager Administration Guide , "Conference Bridge Setup"

- Cisco Unified
                                                   											Communications Manager Security Guide

Services

Allows you to use the Cisco Unified IP Phone Services
                                             									Configuration menu in Cisco Unified Communications Manager
                                             									Administration to define and maintain the list of phone services
                                             									to which users can subscribe.

For more information refer to:

- Cisco Unified
                                                   											Communications Manager Administration Guide , "Cisco Unified IP Phone Setup"

- Cisco Unified
                                                   											Communications Manager System Guide , "Cisco
                                                   											Unified IP Phone Services"

Shared Line

Allows a user to have multiple phones that share the same phone
                                             									number or allows a user to share a phone number with a coworker.

For more information, see Cisco Unified Communications
                                                										Manager System Guide , "Directory Numbers" chapter.

Time-of-Day Routing

Restricts access to specified telephony features by time period.

For more information, see:

- Cisco Unified
                                                   											Communications Manager Administration Guide , "Time Period Setup"

- Cisco Unified
                                                   											Communications Manager System Guide , "Time-of-Day Routing"

Time Zone Update

Updates the Cisco Unified IP Phone with time zone changes.

For more information, see Cisco Unified Communications
                                                										Manager Administration Guide , "Date and Time Group
                                                										Setup" chapter.

Transfer

Allows users to redirect connected calls from their phones to
                                             									another number.

Some JTAPI/TAPI applications are not compatible with the Join and
                                             									Direct Transfer feature implementation on the conference phone
                                             									and you may need to configure the Join and Direct Transfer
                                             									Policy to disable join and direct transfer on the same line or
                                             									possibly across lines.

Transfer - Direct Transfer

Transfer: The first invocation of Transfer will always initiate a
                                             									new call by using the same directory number, after putting the
                                             									active call on hold.

Direct Transfer: This transfer joins two established calls (call
                                             									is in hold or in connected state) into one call and drops the
                                             									feature initiator from the call. Direct Transfer does not
                                             									initiate a consultation call and does not put the active call on
                                             									hold.

Some JTAPI/TAPI applications are not compatible with the Join and
                                             									Direct Transfer feature implementation on the conference phone
                                             									and you may need to configure the Join and Direct Transfer
                                             									Policy to disable join and direct transfer on the same line or
                                             									possibly across lines. For more information, see the <xref
                                             									Join and Direct Transfer Policy>.

UCR 2008

The conference phone supports Unified Capabilities Requirements
                                             									(UCR) 2008 by providing support for 80-bit SRTCP Tagging.

As an administrator, you must set up specific parameters in Cisco
                                             									Unified Communications Manager Administration.

See UCR 2008 setup.

Voice Message System

Enables callers to leave messages if calls are unanswered.

For more information, see the following:

- Cisco Unified
                                                   											Communications Manager Administration Guide , "Cisco Voice-Mail Port Setup"

- Cisco Unified
                                                   											Communications Manager System Guide , "Voice
                                                   											Mail Connectivity to Cisco Unified Communications
                                                   											Manager"

Wideband Ringtone

The Wideband Ringtone feature supports 10 ringtones: 4 embedded
                                             									in the phone firmware and 6 downloaded from the Cisco Unified
                                             									Communications Manager.

For more information, see the following:

- Cisco Unified
                                                   											Communications Manager Administration Guide , "Directory Number Setup"

Features and Services Guide for Cisco Unified
                                                      												Communications Manager , "Custom Phone
                                                      												Rings"

### Linked
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

## Installation

### Installation Requirements

Before you install the firmware release, you must ensure that your Cisco Unified Communications
                              Manager is running the latest device pack. The applicable device packs are released
                              after the firmware release. After you install a device pack on the Cisco Unified
                              Communications Manager servers in the cluster, you need to reboot all the servers.

If your Cisco Unified Communications Manager does not have the required device pack to support this firmware release, the
                                          firmware may not work correctly.

For information on the Cisco Unified Communications Manager Device Packs, see http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/devpack_comp_mtx.html .

### Install Latest Cisco Unified
                              				Communications Manager Release

Before using the Cisco Unified IP Phone with Cisco Unified
                                    				Communications Manager , your Cisco Unified
                                    				Communications Manager servers must be running a version of the
                                 server software that supports the phones. All Cisco Unified
                                    				Communications Manager servers in the cluster must support the
                                 phones. For information about the minimum Cisco Unified
                                    				Communications Manager software version that the phone requires,
                                 see the introductory sections of these release notes.

For more information on Cisco Unified
                                    				Communications Manager installations and upgrades, see the
                                 documents for your Cisco Unified
                                    				Communications Manager version at
                                 the following location: http://www.cisco.com/en/US/products/sw/voicesw/ps556/prod_installation_guides_list.html

To download and install the Cisco Unified
                                    				Communications Manager version, perform these steps.

Go to the following URL:

http://www.cisco.com/cisco/software/navigator.html?mdfid=268439621&catid=278875240

Choose your Cisco Unified
                                             				Communications Manager version.

Choose the appropriate software type.

Hover over the desired file. When the popup window displays, click the Readme link to open the readme file.

Choose Download or Add to cart for the desired file.

Use the instructions in the readme file to install the updated file on the Cisco Unified
                                             				Communications Manager .

### Install Cisco Unified Communications Manager Device Packs

Device packs are required to enable IP phones in the Cisco Unified Communications Manager database. For information about
                                 compatible device packs, see http://www.cisco.com/en/US/docs/voice_ip_comm/cucm/compat/devpack_comp_mtx.html .

For Cisco Unified Communications Manager 6.0 and later, you must run the device pack and reboot the Cisco Unified Communications
                                 Manager server.

Go to the following URL: .

http://www.cisco.com/cisco/software/navigator.html?mdfid=268439621&flowid=21301

Choose your Cisco Unified Communications Manager version.

Hover over the desired device pack. When the popup window displays, click the Readme link to open the readme file.

Choose Download or Add to cart for the desired device pack.

Use the instructions in the readme file to install the updated device pack on the Cisco Unified Communications Manager.

### Install Firmware Release 9.3(3) on Cisco Unified Communications Manager

#### Before you begin

Before using Cisco Unified IP Phone Firmware Release 9.3(3) with Cisco Unified Communications Manager, you must install the
                                 latest firmware on all Cisco Unified Communications Manager servers in the cluster.

Go to the following URL:

http://www.cisco.com/cisco/software/navigator.html?mdfid=268437892&flowid=5293

Choose Cisco Unified IP Phones 8800 Series .

Choose your phone.

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 9.3(3) .

Select one of the following firmware files, click the Download Now or Add to cart button, and follow the prompts:

cmterm-8831-sip.9-3-3-5.cop.sgn

If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file.

Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink
                                          for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                          firmware:

cmterm-8831-sip.9-3-3-5-readme.html

Follow the instructions in the readme file to install the firmware.

#### Install Firmware Zip Files

cmterm-8831-sip.9-3-3-5.zip

Go to the following URL:

http://www.cisco.com/cisco/software/navigator.html?mdfid=268437892&flowid=5293

Choose Cisco Unified IP Phones 8800 Series .

Choose your phone type.

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 9.3(3) .

Download the relevant zip files.

Unzip the files.

Manually copy the unzipped files to the directory on the TFTP server. See Cisco Unified Communications Operating System Administration Guide for information about how to manually copy the firmware files to the server.

### Install Firmware on Phone

Download the latest firmware load.

cmterm-8831-sip.9-3-3-5.cop.sgn

Login to the Cisco Unified Operating System Administration web page from your web browser.

Select Install/Upgrade from the Software Upgrades menu.

Enter the location values in the Software Location fields for the file.

Select the file from the Options/Upgrades drop-down list.

Click Next and follow the prompts.

Restart the TFTP service on Cisco Unified Communications Manager.

Login to the Cisco Unified Serviceability web page from your web browser.

Select Control Center - Feature Services from the Tools menu.

Click the Cisco TFTP radio button in the CM Services section.

Click the restart icon at the top of the page.

The TFTP server restarts.

### Seamless Firmware Upgrade

The conference phone supports seamless firmware upgrade. Once the firmware is installed on the base unit and it completes
                              its reboot sequence, the firmware on the  display control unit (DCU) upgrades automatically via USB connection. No reboot
                              of the base unit is required after upgrading the firmware on the DCU.

If an optional wireless microphone extension kit is linked to the sound base, its firmware is also automatically upgraded.
                              The wireless microphone performs a reboot after a firmware upgrade, but no reboot of the base unit is required.

If two devices are connected in Linked Mode, firmware upgrades are pushed automatically from the primary unit to the secondary
                              unit.

The device pack for Firmware Release 9.3(3) must be installed on the Cisco Unified Communications Manager prior to firmware
                                          upgrade.

#### Upgrade Sound Base Firmware

The following provides an overview of the steps in the upgrade process.

Install the latest version of the firmware load on Cisco Unified Communications Manager.

cmterm-8831-sip.9-3-3-5.cop.sgn

Restart the TFTP service on Cisco Unified Communications Manager.

Wait for the phone to reboot.

The firmware upgrade is applied and the phone reboots. Your conference phone is ready for use.

#### Display Control Unit Firmware Upgrade

The conference phone supports seamless firmware upgrade. Once the firmware is installed on the Sound Base and it completes
                                 its reboot sequence, the firmware on the  display DCU upgrades automatically over the  USB connection to the Sound Base. No
                                 reboot of the base unit is required after upgrading the firmware on the DCU.

#### Wireless Microphone Firmware Upgrade

If an optional wireless microphone extension kit is linked to the Sound Base, its firmware is  automatically upgraded after
                                 the base unit upgrade is completed. The wireless microphone performs a reboot after a firmware upgrade, but no reboot of the
                                 base unit is required.

## Limitations and Restrictions

### Wireless
                           	 Microphone Region Setting

The
                                 		  default value for the Wireless Microphone Region setting is United States. If
                                 		  you use the device in a locale outside the United States and you configure a
                                 		  wireless microphone to pair with the device, you must change the Wireless
                                 		  Microphone Region setting to your region. This requirement ensures that the
                                 		  wireless microphone does not interfere with local bandwidth usage.

Use Cisco
                                 		  Unified Communications Manager Administration to change the Wireless Microphone
                                 		  Region setting.

#### Set Wireless
                              	 Microphone Region

In Cisco
                                             			 Unified Communications Manager Administration, go to Device > Phone .

Use the Find
                                             			 capability to find the Cisco Unified IP Conference Phone 8831.

In the Product
                                             			 Specific Configuration Layout area of the Phone Configuration window, change
                                             			 the Wireless Microphone Region setting to the region where the device is
                                             			 located. The drop-down list box lists the available regions.

### Phone Behavior
                           	 During Times of Network Congestion

Anything that degrades network performance can affect phone audio and, in some cases, can cause a call to drop. Sources of
                                 network degradation can include, but are not limited to, the following activities:

Administrative
                                       				tasks, such as an internal port scan or security scan

Attacks that
                                       				occur on your network, such as a Denial of Service attack

## Unified
                        	 Communications Manager Endpoints Locale Installer

By default, Cisco
                              		  IP Phones are set up for the English (United States) locale. To use the Cisco
                              		  IP Phones in other locales, you must install the locale-specific version of the
                              		  Unified Communications Manager Endpoints Locale Installer on every Cisco
                              		  Unified Communications Manager server in the cluster. The Locale Installer
                              		  installs the latest translated text for the phone user interface and
                              		  country-specific phone tones on your system so that they are available for the
                              		  Cisco IP Phones.

To access the Locale Installer required for a release, access https://software.cisco.com/download/navigator.html?mdfid=286037605&flowid=46245 , navigate to your phone model, and select the Unified Communications Manager Endpoints Locale Installer link.

For more information, see the documentation for your particular Cisco Unified Communications Manager release.

The latest
                                          			 Locale Installer may not be immediately available; continue to check the
                                          			 website for updates.

## Caveats

This section
                              		  describes the resolved and open caveats, and provides information on accessing
                              		  the Cisco Software Bug Toolkit.

### Access Cisco Bug
                           	 Search

Known problems
                                 		  (bugs) are graded according to severity level. These release notes contain
                                 		  descriptions of the following:

All severity
                                       				level 1 or 2 bugs

Significant
                                       				severity level 3 bugs

You can search for
                                 		  problems by using Cisco Bug Search.

#### Before you begin

To access Cisco Bug
                                 		  Search, you need the following items:

Internet
                                       				connection

Web browser

Cisco.com user
                                       				ID and password

To access Cisco Bug Search, go to:

https://tools.cisco.com/bugsearch

Log in with your
                                          			 Cisco.com user ID and password.

To look for
                                          			 information about a specific problem, enter the bug ID number in the Search for
                                          			 field, then press Enter .

### Open Caveats

The following table lists severity 1, 2, and 3 defects that are open for Cisco Unified IP Conference Phone 8831 with Firmware
                                 Release 9.3(3).

For more information about an individual defect, you can access the online record for the defect by clicking the Identifier
                                 or going to the URL that is shown. You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the table reflects a snapshot of the defects that were open at the time this report
                                 was compiled. For an updated view of open defects, access Bug Toolkit as described in Access Cisco Bug Search .

CSCtz98863

"Redirected" and "Dialed" Number not displayed when receiving CFwd call

CSCuc36050

Phone resets twice on performing "reset all"

CSCuc72874

Clicking noise is heard when pressing mute button

CSCud18915

Issue with start record when it is a supervisor monitoring call

CSCud47672

The LEDs on Base and DCU do not turn on when RTPTx and RTPMTx

CSCud49802

8831 does not play the sound of RTPRx when ring in

CSCud99174

"Not Registered" message always shows while setting up phone through DCU

CSCue01254

Locale: local issues for Arabic

CSCue03730

Misc. locale formatting and translation issues on 8831

CSCue09847

Locale: Network locale summary issues

CSCue39992

Locale: Chosen Ringtone name not translated when changing locale

CSCue42487

Feature "Calling Party Normalization" is broken

CSCue78002

Locale: In HK, Call 2 of 2 is not translated correctly during call

CSCuf52937

LM upgrade failed due to no reboot command from primary

CSCug20247

Can't conf another conference via Calls softkey

## Cisco IP Phone
                        	 Firmware Support Policy

For information on the support policy for phones, see https://cisco.com/go/phonefirmwaresupport .

## Documentation, Service Requests, and Additional Information

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http://www.cisco.com/c/en/us/td/docs/general/whatsnew/whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application.
                           The RSS feeds are a free service and Cisco currently supports RSS Version 2.0.

| Cisco Unified IP Phone | Protocol | Cisco Unified Communications Manager |
|---|---|---|
| Cisco Unified IP Conference Phone 8831 | SIP | Cisco Unified Communications Manager Release 7.1.5 and later |

| Note | SIP Firmware Release 9.3(3) is designed and tested to interoperate with Cisco call control, most notably Cisco Unified Communications
                                       Manager Release 9.0(1). Although SIP firmware is IETF RFC 3261 compliant, it is not supported by Cisco TAC or Engineering
                                       for use with non-Cisco call control systems. |
|---|---|

| Note | Cisco Unified Communications Manager Administration also provides several service
                                             					parameters that are used to configure various telephony functions. For more
                                             					information about access and configuration of service parameters, see the Cisco Unified Communications Manager Administration Guide . For more information on the functions of a service, select the name of the
                                             					parameter or the question mark help button in the Service Parameter
                                             					Configuration window in CUCM Administration. |
|---|---|

| Feature | Description | Configuration Reference |
|---|---|---|
| Agent Greeting | Allows an agent to create and update a prerecorded greeting that
                                             									plays at the beginning of a call, such as a customer call,
                                             									before the agent begins the conversation with the caller. The
                                             									agent can prerecord a single greeting or multiple greetings as
                                             									needed. To enable Agent Greeting in the Cisco Unified Communications
                                             									Manager Administration application, choose Device > Phone , locate the IP Phone that you want to configure.
                                             									Scroll to the Device Information Layout pane and set
                                             									Built In Bridge to On or Default . If Built In Bridge is set to Default, in the Cisco Unified
                                             									Communications Manager Administration application, choose System > Service Parameter and select the appropriate Server and Service.
                                             									Scroll to the Clusterwide Parameters (Device - Phone) pane and
                                             									set Builtin Bridge Enable to On . | For more information, see the following: Features and
                                                   											Services Guide for Cisco Unified Communications
                                                   											Manager , "Barge and Privacy" Cisco Unified
                                                   											Communications Manager System Guide , "Cisco
                                                   											Unified IP Phones" |
| Any Call Pickup | Allows users to pick up a call on any line in their call pickup
                                             									group, regardless of how the call was routed to the phone. | For more information, see Features and Services Guide for
                                                										Cisco Unified Communications Manager , "Call
                                                										Pickup" chapter. |
| Audible Message Waiting Indicator (AMWI) | A stutter tone indicates that a user has one or more new voice
                                             									messages on a line. Note The stutter tone is line-specific. You hear it only when
                                                         										using the line with the waiting messages. | Note | The stutter tone is line-specific. You hear it only when
                                                         										using the line with the waiting messages. | For more information, see Cisco Unified Communications
                                                										Manager System Guide , "Cisco Unified IP Phones" chapter. |
| Note | The stutter tone is line-specific. You hear it only when
                                                         										using the line with the waiting messages. |
| Auto Answer | Connects incoming calls automatically after a ring or two. | For more information, see Cisco Unified Communications
                                                										Manager Administration Guide , "Directory Number
                                                										Setup" chapter. |
| Auto Pickup | Allows a user to use one-touch pickup functionality for call
                                             									pickup features. | For more information, see Features and Services Guide for
                                                										Cisco Unified Communications Manager , "Call
                                                										Pickup" chapter. |
| Block External to External Transfer | Prevents users from transferring an external call to another
                                             									external number. | For more information, see Features and Services Guide for
                                                										Cisco Unified Communications Manager , "External
                                                										Call Transfer Restrictions" chapter. |
| Call Back | Provides users with an audio and visual alert on the phone when a
                                             									busy or unavailable party becomes available. | For more information, see the following: Cisco Unified
                                                   											Communications Manager System Guide , "Cisco
                                                   											Unified IP Phones" Features and
                                                   											Services Guide for Cisco Unified Communications
                                                   											Manager , "Cisco Call Back" |
| Call Display Restrictions | Determines the information that will display for calling or
                                             									connected lines, depending on the parties who are involved in
                                             									the call. | For more information, see: Cisco Unified
                                                   											Communications Manager Administration Guide , "Cisco Unified IP Phone Setup" Cisco Unified
                                                   											Communications Manager System Guide , "Understanding Route Plans" Features and
                                                   											Services Guide for Cisco Unified Communications
                                                   											Manager , "Call Display Restrictions" |
| Call Forward | Allows users to redirect incoming calls to another number. Call
                                             									Forward options include Call Forward All, Call Forward Busy,
                                             									Call Forward No Answer, and Call Forward No Coverage. | For more information, see the following: Cisco Unified
                                                   											Communications Manager Administration Guide , "Directory Number Setup" Cisco Unified
                                                   											Communications Manager System Guide , "Cisco
                                                   											Unified IP Phones" Customize Cisco Unified Communications Manager Self Care
                                                   											Portal display |
| Call Forward All Loop Breakout | Detects and prevents Call Forward All loops. When a Call Forward
                                             									All loop is detected, the Call Forward All configuration is
                                             									ignored and the call rings through. | For more information, see Cisco Unified Communications
                                                										Manager System Guide , "Cisco Unified IP Phones" chapter. |
| Call Forward All Loop Prevention | Prevents a user from configuring a Call Forward All destination
                                             									directly on the phone that creates a Call Forward All loop or
                                             									that creates a Call Forward All chain with more hops than the
                                             									existing Forward Maximum Hop Count service parameter
                                             									allows. | For more information, see Cisco Unified Communications
                                                										Manager System Guide , "Cisco Unified IP Phones" chapter. |
| Call Forward Configurable Display | Allows you to specify information that appears on a phone when a
                                             									call is forwarded. This information can include the caller name,
                                             									caller number, redirected number, and original dialed number. | For more information, see the following: Cisco Unified
                                                   											Communications Manager Administration Guide , "Directory Number Setup" Cisco Unified
                                                   											Communications Manager System Guide , "Cisco
                                                   											Unified IP Phones" |
| Call Forward Destination Override | Allows you to override Call Forward All (CFA) in cases where the
                                             									CFA target places a call to the CFA initiator. This feature
                                             									allows the CFA target to reach the CFA initiator for important
                                             									calls. The override works whether the CFA target phone number is
                                             									internal or external. | For more information, see the Cisco Unified Communications
                                                										Manager System Guide , "Directory Numbers" chapter. |
| Call Forward Notification | Allows you to configure the information that the user sees when
                                             									receiving a forwarded call. | For more information, see Call Forward Notification setup. |
| Call History for Shared Line | Allows you to view shared line activity in the phone Call
                                             									History. This feature will: Log missed calls for a shared line Log answered calls for a shared line | For more information, see Enable Call History for shared line. |
| Call Park | Allows users to park (temporarily store) a call and then retrieve
                                             									the call by using another phone in the Cisco Unified
                                             									Communications Manager system. | For more information, see the Features and Services Guide
                                                										for Cisco Unified Communications Manager , "Call
                                                										Park and Directed Call Park" chapter. |
| Call Pickup | Allows users to redirect a call that is ringing on another phone
                                             									within their pickup group to their phone. You can configure an audio and visual alert for the primary line
                                             									on the phone. This alert notifies the users that a call is
                                             									ringing in their pickup group. | For more information, see the Features and Services Guide
                                                										for Cisco Unified Communications Manager , "Call
                                                										Pickup" chapter. |
| Call Recording | Allows a supervisor to record an active call. The user might hear
                                             									a recording audible alert tone during a call when it is being
                                             									recorded. When a call is secured, the security status of the call is
                                             									displayed as a lock icon on Cisco Unified IP Phones. The
                                             									connected parties might also hear an audible alert tone that
                                             									indicates the call is secured and is being recorded. Note When an active call is being monitored or recorded, you can
                                                         										receive or place intercom calls; however, if you place an
                                                         										intercom call, the active call will be put on hold, which
                                                         										causes the recording session to terminate and the monitoring
                                                         										session to suspend. To resume the monitoring session, the
                                                         										party whose call is being monitored must resume the call. | Note | When an active call is being monitored or recorded, you can
                                                         										receive or place intercom calls; however, if you place an
                                                         										intercom call, the active call will be put on hold, which
                                                         										causes the recording session to terminate and the monitoring
                                                         										session to suspend. To resume the monitoring session, the
                                                         										party whose call is being monitored must resume the call. | For more information, see Features and Services Guide for
                                                										Cisco Unified Communications Manager , "Monitoring
                                                										and Recording" chapter. |
| Note | When an active call is being monitored or recorded, you can
                                                         										receive or place intercom calls; however, if you place an
                                                         										intercom call, the active call will be put on hold, which
                                                         										causes the recording session to terminate and the monitoring
                                                         										session to suspend. To resume the monitoring session, the
                                                         										party whose call is being monitored must resume the call. |
| Call Waiting | Indicates (and allows users to answer) an incoming call that
                                             									rings while on another call. Incoming call information appears
                                             									on the phone display. | For more information, see: Cisco Unified Communications Manager System
                                                      												Guide , "Directory Numbers" Phone Call Waiting setup |
| Caller ID | Caller identification such as a phone number, name, or other
                                             									descriptive text appear on the phone display. | For more information, see: Cisco Unified
                                                   											Communications Manager Administration Guide , "Cisco Unified IP Phone Setup" Cisco Unified
                                                   											Communications Manager System Guide , "Understanding Route Plans" Features and
                                                   											Services Guide for Cisco Unified Communications
                                                   											Manager , "Call Display Restrictions" Cisco Unified
                                                   											Communications Manager Administration Guide , "Directory Number Setup" |
| Caller ID Blocking | Allows a user to block their phone number or email address from
                                             									phones that have caller identification enabled. | For more information, see: Cisco Unified
                                                   											Communications Manager System Guide , "Understanding Route Plans" Cisco Unified
                                                   											Communications Manager Administration Guide , "Directory Number Setup" |
| Calling Party Normalization | Calling party normalization presents phone calls to the user with
                                             									a dialable phone number. Any escape codes are added to the
                                             									number so that the user can easily connect to the caller again.
                                             									The dialable number is saved in the call history and can be
                                             									saved in the Personal Address Book. | For more information, see Calling Party Normalization. |
| cBarge | Allows a user to join a nonprivate call on a shared phone line.
                                             									cBarge adds a user to a call and converts it into a conference,
                                             									allowing the user and other parties to access conference
                                             									features | For more information, see: Cisco Unified
                                                   											Communications Manager Administration Guide , "Cisco Unified IP Phone Setup" Cisco Unified
                                                   											Communications Manager System Guide , "Cisco
                                                   											Unified IP Phones" Features and
                                                   											Services Guide for Cisco Unified Communications
                                                   											Manager , "Barge and Privacy" |
| Cisco Extension Mobility | Allows users to temporarily access their Cisco Unified IP Phone
                                             									configuration such as line appearances and services from a
                                             									shared Cisco Unified IP Phone by logging into the Cisco
                                             									Extension Mobility service on that phone when they log into the
                                             									Cisco Extension Mobility service on that phone. Cisco Extension Mobility can be useful if users work from a
                                             									variety of locations within your company or if they share a
                                             									workspace with coworkers. | For more information, see " Extension Mobility" chapter in
                                             									the Cisco Unified Communications Manager Features and
                                                										Services Guide . |
| Cisco WebDialer | Allows users to make calls from web and desktop applications. | For more information, see Features and Services Guide for
                                                										Cisco Unified Communications Manager , "Web
                                                										Dialer" chapter. |
| Conference | Allows a user to
                                                										talk simultaneously with multiple parties by calling each
                                                										participant individually. Conference features include
                                                										Conference and Meet Me. Allows a
                                                										noninitiator in a standard (ad hoc) conference to add or
                                                										remove participants; also allows any conference participant
                                                										to join together two standard conferences on the same line. | The service parameter, Advance Adhoc Conference, (disabled by
                                             									default in Cisco Unified Communications Manager Administration)
                                             									allows you to enable these features. For information on conferences, see Cisco Unified
                                                										Communications Manager System Guide , "Conference
                                                										Bridges" chapter. For more information, see Cisco Unified Communications
                                                										Manager System Guide , "Cisco Unified IP Phones" chapter. Note Be sure to inform your users whether these features are
                                                         										activated. | Note | Be sure to inform your users whether these features are
                                                         										activated. |
| Note | Be sure to inform your users whether these features are
                                                         										activated. |
| CTI Applications | A computer telephony integration (CTI) route point can designate
                                             									a virtual device to receive multiple, simultaneous calls for
                                             									application-controlled redirection. | For more information, see Cisco Unified Communications
                                                										Manager Administration Guide , "CTI Route Point
                                                										Setup" chapter. |
| Device Invoked Recording | Provides end users with the ability to record their telephone
                                             									calls via a softkey. In addition administrators may continue to record telephone calls
                                             									via the CTI User Interface. | For more information, see Enable Device Invoked Recording. |
| Directed Call Park | Allows a user to transfer an active call to an available directed
                                             									call park number that the user dials. Note If you implement Directed Call Park, avoid configuring the
                                                         										Park softkey. This prevents users from confusing the two
                                                         										Call Park features. | Note | If you implement Directed Call Park, avoid configuring the
                                                         										Park softkey. This prevents users from confusing the two
                                                         										Call Park features. | For more information, see Features and Services Guide for
                                                										Cisco Unified Communications Manager , "Call Park
                                                										and Directed Call Park" chapter. |
| Note | If you implement Directed Call Park, avoid configuring the
                                                         										Park softkey. This prevents users from confusing the two
                                                         										Call Park features. |
| Directed Call Pickup | Allows a user to answer a call that is ringing on a particular
                                             									directory number. | For more information, see Features and Services Guide for
                                                										Cisco Unified Communications Manager , "Call
                                                										Pickup" chapter. |
| Direct Transfer | Allows users to connect two calls to each other without remaining
                                             									on the line. | For more information, see Cisco Unified Communications
                                                										Manager System Guide , “Cisco Unified IP Phones”
                                             									chapter. |
| Distinctive Ring | Users can customize how their phone indicates an incoming call
                                             									and a new voice mail message. | For more information, see Features and Services Guide for
                                                										Cisco Unified Communications Manager , "Call
                                                										Pickup" chapter. |
| Divert | Allows a user to transfer a ringing, connected, or held call
                                             									directly to a voice-messaging system. When a call is diverted,
                                             									the line becomes available to make or receive new calls. | For more information, see Features and Services Guide for
                                                										Cisco Unified Communications Manager , "Immediate
                                                										Divert" chapter. |
| Do Not Disturb (DND) | When DND is turned on, either no audible rings occur during the
                                             									ringing-in state of a call, or no audible or visual
                                             									notifications of any type occur. The following DND-related parameters are configurable in
                                             									Cisco Unified Communications Manager Administration: Do Not Disturb:
                                                										This check box allows you to enable DND on a per-phone
                                                										basis. Use Cisco Unified Communications Manager
                                                      												Administration > Device > Phone > Phone Configuration . DND Incoming Call
                                                										Alert: Choose the type of alert to play, if any, on a phone
                                                										for incoming calls when DND is active. This parameter is
                                                										located on both the Common Phone Profile page and the Phone
                                                										configuration page (Phone Configuration window value takes
                                                										precedence). | For more information, see Features and Services Guide for
                                                										Cisco Unified Communications Manager , "Do Not
                                                										Disturb" chapter. |
| EnergyWise | Enables an IP Phone to sleep (power down) and wake (power up) at
                                             									predetermined times, to promote energy savings. | For more information, see EnergyWise on the Cisco Unified IP
                                             									Phone setup. |
| Enhanced Room Coverage | Optional microphone extension kits provide enhanced room coverage
                                             									that can be further expanded by linking two units together in
                                             									Linked Mode. | For more information see: Cisco Unified IP Conference Phone 8831 User
                                                         												Guide for Cisco Unified Communication
                                                         												Manager , "Conference Phone Link Mode" chapter. Cisco Unified IP Conference Phone 8831 User
                                                         												Guide for Cisco Unified Communication
                                                         												Manager , "Enhanced Room Coverage" chapter. |
| Fast Dial Service | Allows a user to enter a Fast Dial code to place a call. Fast
                                             									Dial codes can be assigned to phone numbers or Personal Address
                                             									Book entries. (See "Services" in this table.) | For more information, see Modify phone button template for PAB or
                                             									Fast Dial. |
| Group Call Pickup | Allows a user to answer a call that is ringing on a directory
                                             									number in another group. | For more information, see Features and Services Guide for
                                                										Cisco Unified Communications Manager , "Call
                                                										Pickup" chapter. |
| Hold Reversion | Limits the amount of time that a call can be on hold before
                                             									reverting back to the phone that put the call on hold and
                                             									alerting the user. Reverting calls are distinguished from incoming calls by a single
                                             									ring (or beep, depending on the new call indicator setting for
                                             									the line). This notification repeats at intervals if not
                                             									resumed. A call that triggers Hold Reversion also displays an animated
                                             									icon in the call bubble. You can configure call focus priority to favor incoming or
                                             									reverting calls. | For more information about configuring this feature, see Features and Services Guide for Cisco Unified
                                                										Communications Manager , "Hold Reversion" chapter. |
| Hold Status | Enables phones with a shared line to distinguish between the
                                             									local and remote lines that placed a call on hold. | No configuration is required. |
| Hold/Resume | Allows the user to move a connected call from an active state to
                                             									a held state. | Requires no
                                                										configuration, unless you want to use Music On Hold. See "Music On Hold" in this table for information. See "Hold
                                                   											Reversion" in this table. |
| HTTP Download | Enhances the file download process to the phone to use HTTP by
                                             									default. If the HTTP download fails, the phone reverts to using
                                             									the TFTP download. | No configuration is required. |
| Jitter Buffer | The Jitter Buffer feature handles jitter from 10 milliseconds
                                             									(ms) to 1000 ms for both audio and video streams. | No configuration required. |
| Linked Mode | Enhances the audio coverage area by using a daisy cable to
                                             									connect two conference phone Sound Base units. When linked, voice, dial tone, ringer and base LED features are
                                             									synchronized between the two devices. | For more information see: Cisco Unified IP Conference Phone 8831 User
                                                         												Guide , "Conference Phone Link Mode" |
| Malicious Caller Identification (MCID) | Allows users to notify the system administrator about suspicious
                                             									calls that are received. | For more information, see: Cisco
                                                   											Unified Communications Manager System Guide , "Cisco Unified IP Phones" Features and
                                                   											Services Guide for Cisco Unified Communications
                                                   											Manager , "Malicious Call Identification" |
| Meet Me Conference | Allows a user to host a Meet Me conference in which other
                                             									participants call a predetermined number at a scheduled time. | For more information, see Cisco Unified Communications
                                                										Manager Administration Guide , "Meet-Me Number and
                                                										Pattern Setup" chapter. |
| Message Waiting | Defines directory numbers for message waiting on and off
                                             									indicators. A directly-connected voice-message system uses the
                                             									specified directory number to set or to clear a message waiting
                                             									indication for a particular Cisco Unified IP Phone. | For more information, see the following: Cisco Unified
                                                   											Communications Manager Administration Guide , "Message Waiting Setup" Cisco Unified
                                                   											Communications Manager System Guide , "Voice
                                                   											Mail Connectivity to Cisco Unified Communications
                                                   											Manager" |
| Message Waiting Indicator | Displays a New Voicemail status message on the phone screen. | For more information see: Cisco Unified
                                                   											Communications Manager Administration Guide , "Message Waiting Setup" Cisco Unified
                                                   											Communications Manager System Guide , "Voice
                                                   											Mail Connectivity to Cisco Unified Communications
                                                   											Manager" |
| Missed Call Logging | Allows a user to specify whether missed calls will be logged in
                                             									the missed calls directory for a given line appearance. | For more information, see Cisco Unified Communications
                                                										Manager Administration Guide , "Directory Number
                                                										Setup" chapter. |
| Mobile Connect | Enables users to manage business calls using a single phone
                                             									number and pick up in-progress calls on the desk phone and a
                                             									remote device such as a mobile phone. Users can restrict the
                                             									group of callers according to phone number and time of day. | For more information, see Features and Services Guide for
                                                										Cisco Unified Communications Manager , "Cisco
                                                										Unified Mobility" chapter. |
| Mobile Voice Access | Extends Mobile Connect capabilities by allowing users to access
                                             									an interactive voice response (IVR) system to originate a call
                                             									from a remote device such as a cellular phone. | For more information, see Features and Services Guide for
                                                										Cisco Unified Communications Manager , "Cisco
                                                										Unified Mobility" chapter. |
| Monitoring and Recording | Allows a supervisor to silently monitor an active call. The
                                             									supervisor cannot be heard by either party on the call. The user
                                             									might hear a monitoring audible alert tone during a call when it
                                             									is being monitored. When a call is secured, the security status of the call is
                                             									displayed as a lock icon on Cisco Unified IP Phones. The
                                             									connected parties might also hear an audible alert tone that
                                             									indicates the call is secured and is being monitored. Note When an active call is being monitored or recorded, the use
                                                         										can receive or place intercom calls; however, if the user
                                                         										place an intercom call, the active call will be put on hold,
                                                         										which causes the recording session to terminate and the
                                                         										monitoring session to suspend. To resume the monitoring
                                                         										session, the party whose call is being monitored must resume
                                                         										the call. | Note | When an active call is being monitored or recorded, the use
                                                         										can receive or place intercom calls; however, if the user
                                                         										place an intercom call, the active call will be put on hold,
                                                         										which causes the recording session to terminate and the
                                                         										monitoring session to suspend. To resume the monitoring
                                                         										session, the party whose call is being monitored must resume
                                                         										the call. | For more information, see Features and Services Guide for
                                                										Cisco Unified Communications Manager , "Monitoring
                                                										and Recording" chapter. |
| Note | When an active call is being monitored or recorded, the use
                                                         										can receive or place intercom calls; however, if the user
                                                         										place an intercom call, the active call will be put on hold,
                                                         										which causes the recording session to terminate and the
                                                         										monitoring session to suspend. To resume the monitoring
                                                         										session, the party whose call is being monitored must resume
                                                         										the call. |
| Mute | Mutes the conference phone from the Sound Base, DCU or connected
                                             									external microphones. | Requires no configuration. |
| No Alert Name | Makes it easier for end users to identify transferred calls by
                                             									displaying the original caller’s phone number. The call appears
                                             									as an Alert Call followed by the caller’s telephone number. | Requires no configuration. |
| Onhook Dialing | Allows a user to dial a number without going off hook. | For more information, see Cisco Unified IP Conference Phone
                                                										8831 User Guide . |
| Other Group Pickup | Allows a user to answer a call ringing on a phone in another
                                             									group that is associated with the user's group. | For more information, see Features and Services Guide for
                                                										Cisco Unified Communications Manager , "Call
                                                										Pickup" chapter. |
| Phone Display Message for Extension Mobility Users | This feature enhances the phone interface for the Extension
                                             									Mobility user by providing friendly messages. | No configuration required. |
| Plus Dialing | Allows the user to dial E.164 numbers prefixed with a plus (+)
                                             									 sign. To dial the + sign, the user needs to press and hold the star (*)
                                             									key for at least 1 second. This applies to dialing the first
                                             									digit for an on-hook (including edit mode) or off-hook call. | No configuration required. |
| Privacy | Prevents users who share a line from adding themselves to a call
                                             									and from viewing information on their phone display about the
                                             									call of the other user. | For more information, see the following: Cisco Unified
                                                   											Communications Manager Administration Guide , "Cisco Unified IP Phone Setup" Cisco Unified
                                                   											Communications Manager System Guide , "Cisco
                                                   											Unified IP Phones" Features and
                                                   											Services Guide for Cisco Unified Communications
                                                   											Manager , "Barge and Privacy" |
| Quality Reporting Tool (QRT) | Allows users to submit information about problem phone calls by
                                             									pressing a button. QRT can be configured for either of two user
                                             									modes, depending upon the amount of user interaction desired
                                             									with QRT. | For more information, see: Cisco Unified
                                                   											Communications Manager System Guide , "Cisco
                                                   											Unified IP Phones" Features and
                                                   											Services Guide for Cisco Unified Communications
                                                   											Manager , "Quality Report Tool" |
| Redial | Allows users to call the most recently dialed phone number by
                                             									pressing a button or the Redial softkey. | Requires no configuration. |
| Reroute Direct Calls to Remote Destination to Enterprise Number | Reroutes a direct call to a user's mobile phone to the enterprise
                                             									number (desk phone). For an incoming call to remote destination
                                             									(mobile phone), only remote destination rings; desk phone does
                                             									not ring. When the call is answered on their mobile phone, the
                                             									desk phone displays a Remote In Use message. During these calls,
                                             									users can make use of various features of their mobile phone. | For more information, see the Features and Services Guide
                                                										for Cisco Unified Communications Manager , "Cisco
                                                										Unified Mobility" chapter. |
| Remote Port Configuration | Allows the administrator to configure the speed and duplex
                                             									function of the phone Ethernet ports remotely by using Cisco
                                             									Unified Communications Manager Administration. This enhances the
                                             									performance for large deployments with specific port settings. Note If the ports are configured for Remote Port Configuration in
                                                         										Cisco Unified Communications Manager, the data cannot be
                                                         										changed on the phone. | Note | If the ports are configured for Remote Port Configuration in
                                                         										Cisco Unified Communications Manager, the data cannot be
                                                         										changed on the phone. | To configure the parameter in the Cisco Unified Communications
                                             									Manager Administration application, choose Device > Phone , select the appropriate IP phone, and scroll to
                                             									the Product Specific Configuration Layout pane (Switch Port
                                             									Remote Configuration or PC Port Remote Configuration). To configure the setting on multiple phones simultaneously,
                                             									configure the remote configuration in either Enterprise Phone
                                             									Configuration ( System > Enterprise Phone Configuration ) or Common Phone Profile Configuration ( Device > Device Settings > Common Phone Profile . (Switch Port Remote Configuration or PC Port
                                             									Remote Configuration.) |
| Note | If the ports are configured for Remote Port Configuration in
                                                         										Cisco Unified Communications Manager, the data cannot be
                                                         										changed on the phone. |
| Ringtone Setting | Identifies ring type used for a line when a phone has another
                                             									active call. | For more information, see the following: Cisco
                                                      												Unified Communications Manager Administration
                                                      												Guide , "Directory Number Setup" Cisco Unified Communications Manager
                                                         												Administration Guide , "Custom Phone
                                                         												Rings" |
| Secure Conference | Allows secure
                                                										phones to place conference calls using a secured conference
                                                										bridge. As new participants
                                                										are added by using Conf, Join, cBarge, Barge softkeys or
                                                										MeetMe conferencing, the secure call icon displays as long
                                                										as all participants use secure phones. The Conference List
                                                										displays the security level of each conference participant.
                                                										Initiators can remove nonsecure participants from the
                                                										Conference List. (Non-initiators can add or remove
                                                										conference participants if the Advanced Adhoc Conference
                                                										Enabled parameter is set.) | For additional information, see the following: Cisco Unified
                                                   											Communications Manager System Guide , "Conference Bridges" Cisco Unified
                                                   											Communications Manager Administration Guide , "Conference Bridge Setup" Cisco Unified
                                                   											Communications Manager Security Guide |
| Services | Allows you to use the Cisco Unified IP Phone Services
                                             									Configuration menu in Cisco Unified Communications Manager
                                             									Administration to define and maintain the list of phone services
                                             									to which users can subscribe. | For more information refer to: Cisco Unified
                                                   											Communications Manager Administration Guide , "Cisco Unified IP Phone Setup" Cisco Unified
                                                   											Communications Manager System Guide , "Cisco
                                                   											Unified IP Phone Services" |
| Shared Line | Allows a user to have multiple phones that share the same phone
                                             									number or allows a user to share a phone number with a coworker. | For more information, see Cisco Unified Communications
                                                										Manager System Guide , "Directory Numbers" chapter. |
| Time-of-Day Routing | Restricts access to specified telephony features by time period. | For more information, see: Cisco Unified
                                                   											Communications Manager Administration Guide , "Time Period Setup" Cisco Unified
                                                   											Communications Manager System Guide , "Time-of-Day Routing" |
| Time Zone Update | Updates the Cisco Unified IP Phone with time zone changes. | For more information, see Cisco Unified Communications
                                                										Manager Administration Guide , "Date and Time Group
                                                										Setup" chapter. |
| Transfer | Allows users to redirect connected calls from their phones to
                                             									another number. | Some JTAPI/TAPI applications are not compatible with the Join and
                                             									Direct Transfer feature implementation on the conference phone
                                             									and you may need to configure the Join and Direct Transfer
                                             									Policy to disable join and direct transfer on the same line or
                                             									possibly across lines. |
| Transfer - Direct Transfer | Transfer: The first invocation of Transfer will always initiate a
                                             									new call by using the same directory number, after putting the
                                             									active call on hold. Direct Transfer: This transfer joins two established calls (call
                                             									is in hold or in connected state) into one call and drops the
                                             									feature initiator from the call. Direct Transfer does not
                                             									initiate a consultation call and does not put the active call on
                                             									hold. | Some JTAPI/TAPI applications are not compatible with the Join and
                                             									Direct Transfer feature implementation on the conference phone
                                             									and you may need to configure the Join and Direct Transfer
                                             									Policy to disable join and direct transfer on the same line or
                                             									possibly across lines. For more information, see the <xref
                                             									Join and Direct Transfer Policy>. |
| UCR 2008 | The conference phone supports Unified Capabilities Requirements
                                             									(UCR) 2008 by providing support for 80-bit SRTCP Tagging. As an administrator, you must set up specific parameters in Cisco
                                             									Unified Communications Manager Administration. | See UCR 2008 setup. |
| Voice Message System | Enables callers to leave messages if calls are unanswered. | For more information, see the following: Cisco Unified
                                                   											Communications Manager Administration Guide , "Cisco Voice-Mail Port Setup" Cisco Unified
                                                   											Communications Manager System Guide , "Voice
                                                   											Mail Connectivity to Cisco Unified Communications
                                                   											Manager" |
| Wideband Ringtone | The Wideband Ringtone feature supports 10 ringtones: 4 embedded
                                             									in the phone firmware and 6 downloaded from the Cisco Unified
                                             									Communications Manager. | For more information, see the following: Cisco Unified
                                                   											Communications Manager Administration Guide , "Directory Number Setup" Features and Services Guide for Cisco Unified
                                                      												Communications Manager , "Custom Phone
                                                      												Rings" |

| Note | The stutter tone is line-specific. You hear it only when
                                                         										using the line with the waiting messages. |
|---|---|

| Note | When an active call is being monitored or recorded, you can
                                                         										receive or place intercom calls; however, if you place an
                                                         										intercom call, the active call will be put on hold, which
                                                         										causes the recording session to terminate and the monitoring
                                                         										session to suspend. To resume the monitoring session, the
                                                         										party whose call is being monitored must resume the call. |
|---|---|

| Note | Be sure to inform your users whether these features are
                                                         										activated. |
|---|---|

| Note | If you implement Directed Call Park, avoid configuring the
                                                         										Park softkey. This prevents users from confusing the two
                                                         										Call Park features. |
|---|---|

| Note | When an active call is being monitored or recorded, the use
                                                         										can receive or place intercom calls; however, if the user
                                                         										place an intercom call, the active call will be put on hold,
                                                         										which causes the recording session to terminate and the
                                                         										monitoring session to suspend. To resume the monitoring
                                                         										session, the party whose call is being monitored must resume
                                                         										the call. |
|---|---|

| Note | If the ports are configured for Remote Port Configuration in
                                                         										Cisco Unified Communications Manager, the data cannot be
                                                         										changed on the phone. |
|---|---|

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

| Note | If your Cisco Unified Communications Manager does not have the required device pack to support this firmware release, the
                                          firmware may not work correctly. |
|---|---|

| Step 1 | Go to the following URL: http://www.cisco.com/cisco/software/navigator.html?mdfid=268439621&catid=278875240 |
|---|---|
| Step 2 | Choose your Cisco Unified
                                             				Communications Manager version. |
| Step 3 | Choose the appropriate software type. |
| Step 4 | Hover over the desired file. When the popup window displays, click the Readme link to open the readme file. |
| Step 5 | Choose Download or Add to cart for the desired file. |
| Step 6 | Use the instructions in the readme file to install the updated file on the Cisco Unified
                                             				Communications Manager . |

| Step 1 | Go to the following URL: . http://www.cisco.com/cisco/software/navigator.html?mdfid=268439621&flowid=21301 |
|---|---|
| Step 2 | Choose your Cisco Unified Communications Manager version. |
| Step 3 | Hover over the desired device pack. When the popup window displays, click the Readme link to open the readme file. |
| Step 4 | Choose Download or Add to cart for the desired device pack. |
| Step 5 | Use the instructions in the readme file to install the updated device pack on the Cisco Unified Communications Manager. |

| Step 1 | Go to the following URL: http://www.cisco.com/cisco/software/navigator.html?mdfid=268437892&flowid=5293 |
|---|---|
| Step 2 | Choose Cisco Unified IP Phones 8800 Series . |
| Step 3 | Choose your phone. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 9.3(3) . |
| Step 6 | Select one of the following firmware files, click the Download Now or Add to cart button, and follow the prompts: cmterm-8831-sip.9-3-3-5.cop.sgn Note If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. | Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Step 7 | Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink
                                          for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                          firmware: cmterm-8831-sip.9-3-3-5-readme.html |
| Step 8 | Follow the instructions in the readme file to install the firmware. |

| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
|---|---|

| Step 1 | Go to the following URL: http://www.cisco.com/cisco/software/navigator.html?mdfid=268437892&flowid=5293 |
|---|---|
| Step 2 | Choose Cisco Unified IP Phones 8800 Series . |
| Step 3 | Choose your phone type. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 9.3(3) . |
| Step 6 | Download the relevant zip files. |
| Step 7 | Unzip the files. |
| Step 8 | Manually copy the unzipped files to the directory on the TFTP server. See Cisco Unified Communications Operating System Administration Guide for information about how to manually copy the firmware files to the server. |

| Step 1 | Download the latest firmware load. cmterm-8831-sip.9-3-3-5.cop.sgn |
|---|---|
| Step 2 | Login to the Cisco Unified Operating System Administration web page from your web browser. |
| Step 3 | Select Install/Upgrade from the Software Upgrades menu. |
| Step 4 | Enter the location values in the Software Location fields for the file. |
| Step 5 | Select the file from the Options/Upgrades drop-down list. |
| Step 6 | Click Next and follow the prompts. |
| Step 7 | Restart the TFTP service on Cisco Unified Communications Manager. Login to the Cisco Unified Serviceability web page from your web browser. Select Control Center - Feature Services from the Tools menu. Click the Cisco TFTP radio button in the CM Services section. Click the restart icon at the top of the page. The TFTP server restarts. |

| Note | The device pack for Firmware Release 9.3(3) must be installed on the Cisco Unified Communications Manager prior to firmware
                                          upgrade. |
|---|---|

| Step 1 | Install the latest version of the firmware load on Cisco Unified Communications Manager. cmterm-8831-sip.9-3-3-5.cop.sgn |
|---|---|
| Step 2 | Restart the TFTP service on Cisco Unified Communications Manager. |
| Step 3 | Wait for the phone to reboot. The firmware upgrade is applied and the phone reboots. Your conference phone is ready for use. |

| Step 1 | In Cisco
                                             			 Unified Communications Manager Administration, go to Device > Phone . |
|---|---|
| Step 2 | Use the Find
                                             			 capability to find the Cisco Unified IP Conference Phone 8831. |
| Step 3 | In the Product
                                             			 Specific Configuration Layout area of the Phone Configuration window, change
                                             			 the Wireless Microphone Region setting to the region where the device is
                                             			 located. The drop-down list box lists the available regions. |

| Note | The latest
                                          			 Locale Installer may not be immediately available; continue to check the
                                          			 website for updates. |
|---|---|

| Step 1 | To access Cisco Bug Search, go to: https://tools.cisco.com/bugsearch |
|---|---|
| Step 2 | Log in with your
                                          			 Cisco.com user ID and password. |
| Step 3 | To look for
                                          			 information about a specific problem, enter the bug ID number in the Search for
                                          			 field, then press Enter . |

| Identifier | Headline |
|---|---|
| CSCtz98863 | "Redirected" and "Dialed" Number not displayed when receiving CFwd call |
| CSCuc36050 | Phone resets twice on performing "reset all" |
| CSCuc72874 | Clicking noise is heard when pressing mute button |
| CSCud18915 | Issue with start record when it is a supervisor monitoring call |
| CSCud47672 | The LEDs on Base and DCU do not turn on when RTPTx and RTPMTx |
| CSCud49802 | 8831 does not play the sound of RTPRx when ring in |
| CSCud99174 | "Not Registered" message always shows while setting up phone through DCU |
| CSCue01254 | Locale: local issues for Arabic |
| CSCue03730 | Misc. locale formatting and translation issues on 8831 |
| CSCue09847 | Locale: Network locale summary issues |
| CSCue39992 | Locale: Chosen Ringtone name not translated when changing locale |
| CSCue42487 | Feature "Calling Party Normalization" is broken |
| CSCue78002 | Locale: In HK, Call 2 of 2 is not translated correctly during call |
| CSCuf52937 | LM upgrade failed due to no reboot command from primary |
| CSCug20247 | Can't conf another conference via Calls softkey |