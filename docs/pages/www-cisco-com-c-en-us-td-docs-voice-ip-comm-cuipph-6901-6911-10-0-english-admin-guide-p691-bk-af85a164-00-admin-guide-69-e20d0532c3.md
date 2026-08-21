---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-6901-6911-10-0-english-admin-guide-p691-bk-af85a164-00-admin-guide-69-e20d0532c3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/6901_6911/10_0/english/admin_guide/P691_BK_AF85A164_00_admin-guide-6901-6911-10_0/P691_BK_AF85A164_00_admin-guide-6901-6911-10_0_chapter_0101.html
retrieved_at: 2026-08-21T14:27:28.372994+00:00
---

Cisco Unified IP Phone 6901 and 6911 Administration Guide for Cisco Unified Communications Manager 10.0 (SCCP and SIP)

# Cisco Unified IP Phone 6901 and 6911 Administration Guide for Cisco Unified Communications Manager 10.0 (SCCP and SIP)

Updated: May 9, 2025

Chapter: Features, Templates, Services, and User Setup

## Chapter: Features, Templates, Services, and User Setup

# Features, Templates, Services, and User Setup

## Features, Templates, Services, and Users Overview

After you install Cisco Unified IP Phones in your network,
                           		configure their network settings, and add them to Cisco Unified Communications
                           		Manager, you use the Cisco Unified Communications Manager Administration
                           		application to configure telephony features, modify phone templates, set up
                           		services, and assign users.

This chapter provides an overview of these configuration and
                           		setup procedures. Cisco Unified Communications Manager documentation provides
                           		detailed instructions for these procedures.

To list supported features for all phones or for a particular
                           		phone model on your Cisco Unified Communications Manager (Unified CM), you can generate
                           		a Unified CM Phone Feature List report with  Cisco Unified Reporting.

For suggestions about how to provide users with information
                           		about features, and what information to provide, see Internal Support Web Site .

For information about setting up phones in non-English
                           		environments, see International User Support .

## Telephony Features
                        	 Available for Cisco Unified IP Phone

After you
                              		  add CiscoUnified IP Phones to CiscoUnifiedCommunications Manager, you can
                              		  add functionality to the phones. The following table includes a list of
                              		  supported telephony features, many of which you can configure using
                              		  CiscoUnifiedCommunications Manager Administration. The Reference column lists
                              		  CiscoUnified Communications Manager, other documentation, and links to
                              		  sections in this document that contains configuration procedures and related
                              		  information.

For
                              		  information about using most of these features on the phone, see Cisco Unified
                                 			 IP Phone 6901 and 6911 User Guide for Cisco Unified Communications Manager
                                 			 (SCCP and SIP) .

CiscoUnified
                                          			 Communications Manager also provides several service parameters that you can
                                          			 use to configure various telephony functions. For more information on accessing
                                          			 and configuring service parameters, see Cisco
                                             				UnifiedCommunications Manager Administration Guide .

For more
                                          			 information about functions of a service, select the name of the parameter or
                                          			 the question mark help button in the Service Parameter Configuration window.

Feature

Description

Configuration reference

Agent
                                          					 Greeting

Allows an
                                          					 agent to create and update a prerecorded greeting that plays at the beginning
                                          					 of a call, such as a customer call, before the agent begins the conversation
                                          					 with the caller. The agent can record greetings and update them, as required.

When a
                                          					 customer calls, both the agent and the customer can hear the prerecorded
                                          					 greeting. The agent can remain on mute until the greeting ends or answer the
                                          					 call over the greeting.

All codecs
                                          					 supported for the phone are supported for Agent Greeting calls.

To enable
                                          					 Agent Greeting in the Cisco Unified CM Administration application,
                                          					 choose Device > Phone , and locate the IP Phone that
                                          					 you want to configure. Scroll to the Device Information Layout pane and set the
                                          					 Built In Bridge field to On or Default.

If Built
                                          					 In Bridge is set to Default, choose System > Service
                                                						  Parameter and select the appropriate Server and
                                          					 Service. Scroll to the Clusterwide Parameters (Device - Phone) pane and set
                                          					 Builtin Bridge Enable to On.

For more
                                          					 information, see:

- Cisco Unified
                                                						  Communications Manager Features and Services Guide , "Barge
                                                						  and Privacy" chapter

- Cisco Unified
                                                						  Communications Manager System Guide , "Cisco
                                                						  Unified IP Phones" chapter

Audible
                                          					 Message Waiting Indicator (AMWI)

A stutter
                                          					 tone from the handset or speakerphone indicates that a user has one or more new
                                          					 voice messages on a line.

For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager System Guide , "Cisco
                                             						Unified IP Phone" chapter.

Auto
                                          					 Answer

(Cisco
                                          					 Unified IP Phone 6911 only)

Connects
                                          					 incoming calls automatically after a ring or two.

Auto
                                          					 Answer works with the speakerphone.

For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager Administration Guide , "Directory Number Configuration" chapter.

Automatic
                                          					 Port Synchronization

(Cisco
                                          					 Unified IP Phone 6911 only)

When the
                                          					 Cisco Unified CM administrator uses the Remote Port Configuration feature to
                                          					 set the speed and duplex function of an IP Phone remotely, loss of packets can
                                          					 occur if one port is slower than the other.

The
                                          					 Automatic Port Synchronization feature synchronizes the ports to the lowest
                                          					 speed among the two ports to eliminate packet loss. When automatic port
                                          					 synchronization is enabled, Cisco recommends that both ports autonegotiate. If
                                          					 one port autonegotiates and the other uses a fixed speed, the phone
                                          					 synchronizes to the fixed port speed.

If both
                                                      						the ports use fixed speed, the Automatic Port Synchronization feature is
                                                      						ineffective. The Remote Port Configuration and Automatic Port Synchronization
                                                      						features are compatible only with IEEE 802.3AF Power of Ethernet (PoE)
                                                      						switches. Switches that support only Cisco Inline Power are not compatible.
                                                      						Enabling this feature on phones that are connected to these types of switches
                                                      						could result in loss of connectivity to Cisco Unified CM if the phone is
                                                      						powered by PoE.

To
                                          					 configure the parameter in the Cisco Unified CM Administration application,
                                          					 choose Device > Phone , select the appropriate IP
                                          					 phones, and scroll to the Product Specific Configuration Layoutpane.

To
                                          					 configure the setting on multiple phones simultaneously, enable Automatic Port
                                          					 Synchronization in one of the following windows:

Enterprise Phone Configuration ( System > Enterprise Phone
                                                      								Configuration )

Common Phone Profile Configuration ( Device > Device
                                                      								Settings > Common Phone Profile )

Block
                                          					 External to External Transfer

Prevents
                                          					 users from transferring an external call to another external number.

For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager Features and Services Guide , "External
                                             						Call Transfer Restrictions" chapter.

Call
                                          					 Forward

Allows
                                          					 users to redirect incoming calls to another number. Call forward options
                                          					 include Call Forward All, Call Forward Busy, Call Forward No Answer, and Call
                                          					 Forward No Coverage.

You hear a
                                          					 stutter tone when off hook if Call Forward All is active on your phone.

For more
                                          					 information, see:

- Cisco Unified
                                                						  Communications Manager Administration Guide , "Directory Number Configuration" chapter

- Cisco Unified
                                                						  Communications Manager System Guide , "Cisco
                                                						  Unified IP Phone" chapter

- Customize User Options Web Pages Options

Call
                                          					 Forward All Loop Breakout

Detects
                                          					 and prevents Call Forward All loops. When a Call Forward All loop is detected,
                                          					 the Call Forward All configuration is ignored and the call rings through.

For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager System Guide , "Cisco
                                             						Unified IP Phone" chapter.

Call
                                          					 Forward All Loop Prevention

Prevents a
                                          					 user from configuring a Call Forward All destination directly on the phone that
                                          					 creates a Call Forward All loop or that creates a Call Forward All chain with
                                          					 more hops than the existing Forward Maximum Hop Count service parameter allows.

For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager System Guide , "Cisco
                                             						Unified IP Phone" chapter.

Call
                                          					 Forward Destination Override

Allows you
                                          					 to override Call Forward All (CFA) in cases where the CFA target places a call
                                          					 to the CFA initiator. This feature allows the CFA target to reach the CFA
                                          					 initiator for important calls. The override works whether the CFA target phone
                                          					 number is internal or external.

For more
                                          					 information, see the Cisco Unified Communications Manager System Guide , "Understanding Directory Numbers" chapter.

Call
                                          					 Pickup

(Cisco
                                          					 Unified IP Phone 6911 only)

Allows
                                          					 users to answer a call ringing on a coworker's phone.

You can
                                          					 configure an audio alert for the primary line on the phone. This alert notifies
                                          					 the users that a call is ringing in their pickup group.

For more
                                          					 information, see the Cisco Unified Communications Manager Features and Services
                                             						Guide , "Call
                                             						Pickup" chapter.

Call
                                          					 Waiting

Indicates
                                          					 and allows users to answer an incoming call while active on another call.

The phone
                                          					 sounds the call waiting tone (single beep) and the line button flashes amber.

For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager System Guide , "Understanding Directory Numbers" chapter.

cBarge

Allows a
                                          					 user to join a nonprivate call on a shared phone line. cBarge adds a user to an
                                          					 existing call and converts it into a conference, allowing the user and other
                                          					 parties to access conference features.

For more
                                          					 information, see:

- Cisco Unified
                                                						  Communications Manager Features and Services Guide , "Barge
                                                						  and Privacy" chapter

- Cisco Unified
                                                						  Communications Manager System Guide , "Cisco
                                                						  Unified IP Phone" chapter

- Cisco
                                                						  UnifiedCommunications Manager Features and Services Guide , "Barge
                                                						  and Privacy 
                                                						" chapter

Cisco
                                          					 Unified Communications Manager Express (Unified CME) Version Negotiation

The Cisco
                                          					 Unified Communication Manager Express uses a special tag in the information
                                          					 sent to the phone to identify itself. This tag enables the phone to provide
                                          					 services to the user that the switch supports.

For more
                                          					 information, see:

Cisco Unified
                                                   							 Communications Manager Express System Administrator Guide

Cisco Unified IP Phone and Cisco Unified Communications Manager Express Interaction

Cisco
                                          					 Unified Video Advantage (CUVA)

(Cisco
                                          					 Unified IP Phone 6911 only)

Allows
                                          					 users to make video calls by using their Cisco Unified IP Phones, personal
                                          					 computers, and external video cameras.

Configure
                                          					 the Video Capabilities and Auto Line Select parameter in the Product Specific
                                          					 Configuration Layout section in Phone Configuration.

Cisco Web
                                          					 Dialer

Allows
                                          					 users to make calls from web and desktop applications.

For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager Features and Services Guide , "Cisco
                                             						Web Dialer" chapter.

Client
                                          					 Matter Code (CMC)

Enables a
                                          					 user to specify that a call relates to a specific client matter.

For more
                                          					 information, see the Cisco
                                             						UnifiedCommunications Manager Features and Services Guide , "Client
                                             						Matter Codes and Forced Authorization Codes" chapter.

Conference

Allows a
                                          					 user to talk simultaneously with multiple parties by calling each participant
                                          					 individually. Conference features include Conference and Meet Me.

Allows a
                                          					 participant (host, initiator, or noninitiator) in a standard (adhoc)
                                          					 conference to add participants; also allows any conference participant to join
                                          					 together two standard conferences on the same line.

Allows a
                                          					 conference host using a Cisco Unified IP Phone 6901 to remove the last
                                          					 participant that joined the conference using the hookflash feature.

The
                                          					 Advance Adhoc Conference service parameter, disabled by default in Cisco
                                          					 Unified Communications Manager, allows you to enable these features.

For
                                          					 information on conferences, see the CiscoUnified Communications Manager System Guide , "Conference Bridges" chapter.

For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager System Guide , "Cisco
                                             						Unified IP Phone" chapter.

Be sure
                                                      						to inform your users if these features are activated.

CTI
                                          					 Applications

A computer
                                          					 telephony integration (CTI) route point can designate a virtual device to
                                          					 receive multiple, simultaneous calls for application-controlled redirection.

For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager Administration Guide , "CTI
                                             						Route Point Configuration" chapter.

EnergyWise

Enables an
                                          					 IP Phone to sleep (power down) and wake (power up) at predetermined times to
                                          					 promote energy savings.

For more
                                          					 information, see EnergyWise Setup on Cisco Unified IP Phone 6901 and 6911 .

Forced
                                          					 Authorization Codes (FAC)

Controls
                                          					 the types of calls that certain users can place.

For more
                                          					 information, see the Cisco
                                             						UnifiedCommunications Manager Features and Services Guide , "Client
                                             						Matter Codes and Forced Authorization Codes" chapter.

Group Call
                                          					 Pickup

(Cisco
                                          					 Unified IP Phone 6911 only)

Allows a
                                          					 user to answer a call that is ringing on a phone in another group.

For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager Features and Services Guide , "Call
                                             						Pickup" chapter.

Hold
                                          					 Status

Enables
                                          					 phones with a shared line to distinguish between the local and remote lines
                                          					 that placed a call on hold.

The Line
                                          					 LED lights green for Local Hold and red for Remote Hold.

No
                                          					 configuration required.

Hold/Resume

Allows the
                                          					 user to move a connected call from an active state to a held state by using the
                                          					 Hold button. The user resumes a held call by pressing the line button, speaker
                                          					 button, or going off hook.

The LED
                                                      						on the line button pulses green when a local call is on hold and the LED pulses
                                                      						red when a remote call is on hold.

No
                                          					 configuration required unless you want to use Music on Hold. For more
                                          					 information, see "Music on
                                             						Hold" in this table.

Jitter
                                          					 Buffer

Handles
                                          					 jitter from 10 milliseconds (ms) to 1000 ms for both audio and video streams.

No
                                          					 configuration required.

Meet Me
                                          					 Conference

(Cisco
                                          					 Unified IP Phone 6911 only)

Allows a
                                          					 user to host a Meet Me conference in which other participants call a
                                          					 predetermined number at a scheduled time.

The user
                                          					 joins a Meet Me conference by pressing the feature button and the Meet Me
                                          					 conference number.

For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager Administration Guide , "Meet Me Number/Pattern
                                             						Configuration" chapter .

Message
                                          					 Waiting

Defines
                                          					 directory numbers for the message waiting on and message waiting off indicator.
                                          					 A directly connected voice message system uses the specified directory number
                                          					 to set or to clear a message waiting indicator for a particular Cisco Unified
                                          					 IP Phone.

For more
                                          					 information, see:

- Cisco Unified
                                                						  Communications Manager Administration Guide , "Message Waiting Configuration" chapter

- Cisco Unified
                                                						  Communications Manager System Guide , "Voice
                                                						  Mail Connectivity to Cisco Unified Communications Manager" chapter

Message
                                          					 Waiting Indicator

A light on
                                          					 the handset that indicates that a user has one or more new voice messages.

For more
                                          					 information, see:

- Cisco Unified
                                                						  Communications Manager Administration Guide , "Message Waiting Configuration" chapter

- Cisco Unified
                                                						  Communications Manager System Guide , "Voice
                                                						  Mail Connectivity to Cisco Unified Communications Manager" chapter

Monitoring
                                          					 and Recording

(Cisco
                                          					 Unified IP Phone 6911 only)

Allows a
                                          					 supervisor to monitor an active call silently. The supervisor cannot be heard
                                          					 by either party on the call. The user may receive an audible alert during a
                                          					 call when it is being monitored.

Callers
                                          					 may also receive an audible alert to indicate that the call is being monitored.
                                          					 The connected parties may also receive an audible alert that indicates the call
                                          					 is secure and is being monitored.

For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager Features and Services Guide , "Monitoring and Recording" chapter.

Multilevel
                                          					 Precedence and Preemption (MLPP)

(SCCP
                                          					 phones only)

Provides a
                                          					 method of prioritizing calls within your phone system. Use this feature when
                                          					 users work in an environment where they need to make and receive urgent or
                                          					 critical calls.

For more
                                          					 information, see the Cisco Unified Communications Manager Features and Services Guide , "Multilevel Precedence and Preemption" chapter.

Music on
                                          					 Hold

Plays
                                          					 music while callers are on hold.

For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager Features and Services Guide , "Music On
                                             						Hold" chapter.

Mute

(Cisco
                                          					 Unified IP Phone 6911 only)

Mutes the
                                          					 microphone on the handset or speakerphone.

No
                                          					 configuration required.

On-hook
                                          					 Call Transfer

Allows a
                                          					 user to press the Transfer button and go on-hook to complete a call transfer.

For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager System Guide , "Cisco
                                             						Unified IP Phones" chapter.

Plus
                                          					 Dialing

Allows the
                                          					 user to dial E.164 numbers prefixed with a plus (+) sign.

To dial
                                          					 the + sign, the user needs to press and hold the star (*) key for at least 1
                                          					 second. This applies to dialing the first digit for the feature in the Cisco
                                          					 Unified IP Phone 6901 and 6911 only works with off-hook dialing.

No
                                          					 configuration required.

Private
                                          					 Line Automated Ringdown (PLAR)

The Cisco
                                          					 UnifiedCommunications Manager administrator can configure a phone number that
                                          					 the Cisco UnifiedIPPhone dials as soon as the handset goes off-hook. This can
                                          					 be useful for phones that are designated for calling emergency or hotline
                                          					 numbers.

For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager Administration Guide , "Directory Number Configuration" chapter.

Redial

Allows
                                          					 users to call the most recently dialed phone number by pressing the Redial
                                          					 button.

No
                                          					 configuration required.

Remote
                                          					 Port Configuration

Allows the
                                          					 administrator to configure the speed and duplex function of the phone Ethernet
                                          					 ports remotely by using Cisco Unified CM Administration. This enhances the
                                          					 performance for large deployments with specific port settings.

If the
                                                      						ports are configured for Remote Port Configuration in Cisco Unified CM, the
                                                      						data cannot be changed on the phone.

To
                                          					 configure the parameter in the Cisco Unified CM Administration application,
                                          					 choose Device > Phone , select the appropriate IP
                                          					 Phone, and scroll to the Product Specific Configuration Layout pane (Switch
                                          					 Port Remote Configuration or PC Port Remote Configuration).

To
                                          					 configure the setting on multiple phones simultaneously, configure the remote
                                          					 configuration in either Enterprise Phone Configuration ( System > Enterprise Phone
                                                						  Configuration ) or Common Phone Profile Configuration
                                          					 ( Device > Device
                                                						  Settings > Common Phone Profile . (Switch Port
                                          					 Remote Configuration or PC Port Remote Configuration).

Shared
                                          					 Line

Allows
                                          					 multiple phones to share the same phone number or allows a user to share a
                                          					 phone number with a coworker.

For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager System Guide , "Understanding Directory Numbers" chapter.

Speed
                                          					 Dialing

(Cisco
                                          					 Unified IP Phone 6911 only)

Dials a
                                          					 specified number that has been previously stored.

You
                                          					 configure this feature on the Cisco Unified Communications Manager. The users
                                          					 access speed dialing using the Feature key and the Feature Code.

For more
                                          					 information see:

- Cisco Unified
                                                						  Communications Manager Administration Guide , "Cisco
                                                						  Unified IP Phone Configuration" chapter

- Cisco Unified
                                                						  Communications Manager System Guide , "Cisco
                                                						  Unified IP Phone" chapter

SSH Access

Allows the
                                          					 administrator to enable or disable the SSH Access setting using Cisco Unified
                                          					 CM Administration.

Enabling
                                          					 Secure Shell (SSH) access allows the phone to accept the SSH connections.

Disabling
                                          					 SSH access blocks SSH access to the phone.

For more
                                          					 information, see UCR 2008 Setup

Time-of-Day Routing

Restricts
                                          					 access to specified telephony features by time period.

For more
                                          					 information, see:

- Cisco Unified
                                                						  Communications Manager Administration Guide , "Time
                                                						  Period Configuration" chapter

- Cisco Unified
                                                						  Communications Manager System Guide , "Time-of-Day Routing" chapter

Time Zone
                                          					 Update

Updates
                                          					 the Cisco Unified IP Phone with time zone changes.

For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager Administration Guide , "Date/Time Group Configuration" chapter.

Transfer

Allows
                                          					 users to redirect connected calls from their phones to another number.

Some
                                          					 JTAPI/TAPI applications are not compatible with the Direct Transfer feature
                                          					 implementation on the Cisco Unified IP Phone.

UCR 2008

(SCCP
                                          					 phones only)

The Cisco
                                          					 Unified IP Phones using SCCP support Unified Capabilities Requirements (UCR)
                                          					 2008 by providing the following functions:

- Support for Federal
                                             						Information Processing Standard (FIPS) 140-2

- Support for 80-bit SRTCP
                                             						Tagging

As an IP
                                          					 Phone administrator, you must set up specific parameters in Cisco Unified
                                          					 Communications Manager Administration.

See UCR 2008 Setup .

Voice
                                          					 messaging system

Enables
                                          					 callers to leave messages if calls are unanswered.

Users
                                          					 access messages using the Message button on the Cisco Unified IP Phone 6911.

Users
                                          					 access messages using the access code on the Cisco Unified IP Phone 6901.

For more
                                          					 information, see:

- Cisco Unified
                                                						  Communications Manager Administration Guide , "Cisco
                                                						  Voice-Mail Port Configuration" chapter.

- Cisco Unified Communications Manager System Guide , "Voice
                                                						  Mail Connectivity to Cisco Unified Communications Manager" chapter.

## Add Users to Cisco Unified Communications Manager

Adding users to CiscoUnifiedCommunications Manager allows
                              		  you to display and maintain information about users and allows each user to
                              		  perform these tasks:

- Create a personal
                                 			 directory.

- Set up speed dial and call
                                 			 forwarding numbers.

You can add users to CiscoUnifiedCommunications Manager
                              		  using one of these following methods:

To add users individually, choose User Management > End User from Cisco Unified Communications Manager.

To add users in batches, use the Bulk Administration Tool. This
                                 			 method also enables you to set an identical default password for all users.

To add users from your corporate Lightweight Directory Access Protocol (LDAP) directory, choose System > LDAP > LDAP
                                       				  System from Cisco Unified Communications Manager.

After you enable synchronization with the LDAP server,
                                                				  you cannot add additional users from CiscoUnifiedCommunicationsManager
                                                				  Administration.

For more information on LDAP, see the "Understanding the Directory" chapter in Cisco Unified Communications Manager System Guide .

To add a user and phone at the same time, choose User
                                       				  Management > User/Phone Add from
                                 			 Cisco Unified Communications Manager.

## User Options Web Pages Management

From the User Options web page, users can customize and
                           		control several phone features and settings. For more information about
                           		User Options web pages, see Cisco Unified IP Phone 6901 and 6911 User Guide for Cisco Unified Communications
                              		  Manager (SCCP and SIP) .

### User Access to User Options Web Pages

Before a user can access the User Options web pages, you
                                 		  must add the user to the standard Cisco Unified Communications Manager End User
                                 		  group and associate the appropriate phone with the user.

Make sure to provide users with the following
                                 		  information about the User Options web pages:

http: //<server_name:portnumber> / ccmuser /,
                                       				where server_name is the host name of the CiscoUnified
                                       				Communications Manager.

These settings correspond to the values you enter when you add
                                       				the user to Cisco Unified Communications Manager (see the Add Users to Cisco Unified Communications Manager ).

For more information, see:

- Cisco Unified
                                       				Communications Manager Administration Guide , "User Group
                                       				Configuration" chapter.

- Cisco Unified
                                       				Communications Manager Administration Guide , "End User Configuration" chapter.

#### Add User to End User Group

To add a user to the Cisco Unified Communications
                                    		  Manager Standard End User group, perform these steps:

Step 1

From Cisco Unified Communications Manager Administration, choose User Management > User
                                                   				  Groups .

The Find and List Users window displays.

Step 2

Enter the appropriate search criteria and click Find .

Step 3

Select the Standard CCM End Users link. The User Group
                                             			 Configuration window for the Standard CCM End Users appears.

Step 4

Select Add End Users to Group . The Find and List
                                             			 Users window appears.

Step 5

Use the Find User drop-down list boxes to find the users that
                                             			 you want to add and click Find .

A list of users that matches your search criteria appears.

Step 6

In the list of records that appear, click the check box next to
                                             			 the users that you want to add to this user group. If the list is long, use the links at the bottom to see more results.

The list of search results does not display users that
                                                            				  already belong to the user group.

Step 7

Choose Add Selected .

#### Associate Phones with Users

You associate phones with users from the Cisco Unified
                                    		  Communications Manager End User window.

Step 1

From Cisco Unified Communications Manager Administration,
                                             			 choose User Management > End
                                                   				  User .

The Find and List Users window appears.

Step 2

Enter the appropriate search criteria and click Find .

Step 3

In the list of records that appear, select the link for the user.

Step 4

Select Device Association .

The User Device Association window appears.

Step 5

Enter the appropriate search criteria and click Find .

Step 6

Choose the device that you want to associate with the user by
                                             			 checking the box to the left of the device.

Step 7

Choose Save Selected/Changes to associate the device
                                             			 with the user.

Step 8

From the Related Links drop-down list in the upper, right corner of
                                             			 the window, select Back to User , and click Go .

The End User Configuration window appears and the associated
                                                				devices that you chose display in the Controlled Devices pane.

Step 9

Choose Save Selected/Changes .

### Customize User Options Web Pages Options

Most options on the User Options web pages appear by
                                 		  default. However, the following options must be set by the system administrator
                                 		  by using Enterprise Parameters Configuration settings in Cisco Unified
                                 		  Communications Manager:

- Show Ring Settings

- Show Call Forwarding

- Show Message Waiting Lamp

- Show Audible Message
                                    			 Waiting Indicator

The settings apply to all User Options web pages at your site.

To specify the options that appear on the User Options web
                                 		  pages, perform these steps:

Step 1

From Cisco Unified Communications Manager, choose System > Enterprise
                                                				  Parameters .

The 
                                             				Enterprise Parameters Configuration window
                                             				appears.

Step 2

In the CCMUser Parameters area, specify whether a parameter
                                          			 appears on the User Options web pages by choosing one of the following values from the
                                          			 Parameter Value drop-down list:

True : Option displays on the User Options web pages
                                                   					 (default except for Show Ring Settings, and Show Call Forwarding).

False : Option does not display on the User Options web
                                                   					 pages.

Show All Settings : All call forward settings display
                                                   					 on the User Options web pages (default).

Hide All Settings : No call forward settings display on
                                                   					 the User Options web pages.

Show Only Call Forward All : Only call forward all
                                                   					 calls displays on the User Options web pages.

## EnergyWise Setup on Cisco Unified IP Phone 6901 and 6911

To reduce power consumption, you can configure the phone to
                              		  sleep (power down) and wake (power up) if your system includes an EnergyWise
                              		  controller (for example, a Cisco Switch with the EnergyWise feature enabled).

You configure settings in Cisco Unified Communications
                              		  Manager to enable EnergyWise and configure sleep and wake times. These
                              		  parameters are closely tied to the phone display configuration parameters.

When EnergyWise is enabled and a sleep time is set, the
                              		  phone sends a request to the switch to wake it up at the configured time. The
                              		  switch sends back either an acceptance or a rejection of the request. If the
                              		  switch rejects the request or if the switch does not reply, the phone does not
                              		  power down. If the switch accepts the request, the idle phone goes to sleep,
                              		  reducing the  power consumption to a predetermined level. A phone that is not
                              		  idle sets an idle timer, and goes to sleep after the timer expires.

At the scheduled wake time, the system restores power to the
                              		  phone, waking it up.

The following table explains the Cisco Unified
                              		  Communications Manager fields that control the EnergyWise settings. You
                              		  configure these fields in Cisco Unified Communications Manager in the Product
                              		  Specific configuration window, by choosing Device > Phone .

Field

Description

Enable Power Save Plus

Selects the schedule of days for which the phone powers down.
                                          					 Select multiple days by pressing and holding the Control key while clicking on the days
                                          					 for the schedule.

By default, no days are selected.

When Enable Power Save is checked, you receive a message to
                                          					 warn about emergency (e911) concerns.

Caution

While Power Save Plus Mode (the mode) is in effect,
                                                      						endpoints configured for the mode are disabled for emergency calling and from
                                                      						receiving inbound calls. By selecting this mode, you agree to the following:
                                                      						(i) You are taking full responsibility for providing alternate methods for
                                                      						emergency calling and receiving calls while the mode is in effect; (ii) Cisco
                                                      						has no liability in connection with your selection of the mode and all
                                                      						liability in connection with enabling the mode is your responsibility; and
                                                      						(iii) you will fully inform users of the effects of the mode on calls, calling
                                                      						and otherwise.

To disable Power Save Plus, you must uncheck the Allow
                                                      						EnergyWise Overrides check box. Leaving the Allow EnergyWise Overrides checked
                                                      						with no days selected in the Enable Power Save Plus field does not disable
                                                      						Power Save Plus.

Phone On Time

Determines when the phone automatically turns on for the days
                                          					 selected in the Enable Power Save Plus field.

Enter the time in this field in 24 hour format, where 00:00 is
                                          					 midnight.

For example, to automatically power up the phone at 7:00 a.m.
                                          					 (0700), enter 7:00. To power up the phone at 2:00 p.m. (1400), enter 14:00.

The default value is 00:00.

Phone Off Time

The time of day that the phone powers down for the days
                                          					 selected in the Enable Power Save Plus field. If the Phone On Time and the
                                          					 Phone Off Time fields contain the same value, the phone does not power down.

Enter the time in this field in 24 hour format, where 00:00 is
                                          					 midnight.

For example, to automatically power down the phone at 7:00
                                          					 a.m. (0700), enter 7:00. To power down the phone at 2:00 p.m. (1400), enter
                                          					 14:00.

The default value is 24:00.

Phone Off Idle Timeout

The length of time that the phone must be idle before the
                                          					 phone powers down.

The range of the field is 20 to 1440 minutes.

The default value is 60 minutes.

Enable Audible Alert

When enabled, instructs the phone to play an audible alert
                                          					 starting at 10 minutes before to the time specified in the Phone Off Time
                                          					 field.

The audible alert uses the phone ringtone, which briefly plays
                                          					 at specific times during the 10-minute alerting period. The alerting ringtone
                                          					 plays at the user’s designated volume level. The audible alert schedule is:

- At 10 minutes
                                             						before power down, play the ringtone four times

- At 7 minutes
                                             						before power down, play the ringtone four times

- At 4 minutes
                                             						before power down, play the ringtone four times

- At 30 seconds
                                             						before power down, play the ringtone 15 times or until the phone powers off

This check box applies only if the Enable Power Save Plus list
                                          					 box has one or more days selected.

EnergyWise Domain

The EnergyWise domain that the phone is in. The maximum length
                                          					 is 127.

EnergyWise Secret

The security secret password that is used to communicate with
                                          					 the endpoints in the EnergyWise domain. The maximum length is 127.

Allow EnergyWise Overrides

This check box determines whether you will allow the
                                          					 EnergyWise domain controller policy to send power-level updates to the phones.
                                          					 The following conditions apply:

The settings in Cisco Unified CM Administration take
                                                						  effect on schedule even if EnergyWise sends an override.

For example, assume the Phone Off Time is set to 22:00 (10:00
                                          					 p.m.), the value in the Phone On Time field is 06:00 (6:00 a.m.), and the
                                          					 Enable Power Save Plus has one or more days selected.

- If EnergyWise
                                             						directs the phone to turn off at 20:00 (8:00 p.m.), that directive will remain
                                             						in effect (assuming no phone user intervention occurs) until the configured
                                             						Phone On Time at 6:00 a.m.

- At 6:00 a.m., the
                                             						phone turns on and resumes receiving the power level changes from the settings
                                             						in Unified Communications Manager.

- To change the
                                             						power level on the phone again, EnergyWise must reissue a new power-level
                                             						change command.

To disable Power Save Plus, you must uncheck the Allow
                                                      						EnergyWise Overrides check box. Leaving the Allow EnergyWise Overrides checked
                                                      						with no days selected in the Enable Power Save Plus field does not disable
                                                      						Power Save Plus.

## UCR 2008 Setup

The parameters that support UCR 2008 reside in Cisco Unified
                              		  Communications Manager Administration. The following table describes the
                              		  parameters and indicates the procedure to change the setting.

Parameter

Administration Path

FIPS Mode

Device > Device
                                                						  Settings > Common Phone Profile

Set Up UCR 2008 in Common Phone Profile

System > Enterprise
                                                						  Phone Configuration

Set Up UCR 2008 in Enterprise Phone Configuration

SSH Access

Device > Phone

Set Up UCR 2008 in Phone

Device > Device
                                                						  Settings > Common Phone Profile

Set Up UCR 2008 in Common Phone Profile

Web Access

Device > Phone

Set Up UCR 2008 in Phone

80-bit SRTCP

Device > Device
                                                						  Settings > Common Phone Profile

Set Up UCR 2008 in Common Phone Profile

System > Enterprise
                                                						  Phone Configuration

Set Up UCR 2008 in Enterprise Phone Configuration

IP Addressing Mode

Device > Device
                                                						  Settings > Common Device
                                                						  Configuration

Set Up UCR 2008 in Common Device Configuration

IP Addressing Mode Preference for Signaling

Device > Device
                                                						Settings > Common Device Configuration

Set Up UCR 2008 in Common Device Configuration

### Set Up UCR 2008 in Phone

Use this procedure to set the following UCR 2008 parameters:

- SSH Access

- Web Access

Step 1

Choose Device > Phone .

Step 2

Set the SSH Access parameter to Disabled .

Step 3

Set the Web Access parameter to Disabled .

Step 4

Select Save .

### Set Up UCR 2008 in Common Phone Profile

Use this procedure to set the following UCR 2008 parameters:

- FIPS Mode

- SSH Access

- 80-bit SRTCP

Step 1

Choose Device > Device
                                                				  Settings > Common Phone Profile .

Step 2

Set the FIPS Mode parameter to Enabled .

Step 3

Set the SSH Access parameter to Disabled .

Step 4

Set the 80-bit SRTCP parameter to Enabled .

Step 5

Select Save .

### Set Up UCR 2008 in Enterprise Phone Configuration

Use this procedure to set the following UCR 2008 parameters:

- FIPS Mode

- 80-bit SRTCP

Step 1

Choose System > Enterprise Phone Configuration .

Step 2

Set the FIPS Mode parameter to Enabled .

Step 3

Set the 80-bit SRTCP parameter to Enabled .

Step 4

Select Save .

### Set Up UCR 2008 in Common Device Configuration

Use this procedure to set the following UCR 2008 parameters:

- IP Addressing Mode

- IP Addressing Mode
                                    			 Preference for Signaling

Step 1

Choose Device > Device
                                                				  Settings > Common Device
                                                				  Configuration .

Step 2

Set the IP Addressing Mode parameter.

Step 3

Set the IP Addressing Mode Preference for Signaling parameter.

Step 4

Select Save .

| Note | CiscoUnified
                                          			 Communications Manager also provides several service parameters that you can
                                          			 use to configure various telephony functions. For more information on accessing
                                          			 and configuring service parameters, see Cisco
                                             				UnifiedCommunications Manager Administration Guide . |
|---|---|

| Note | For more
                                          			 information about functions of a service, select the name of the parameter or
                                          			 the question mark help button in the Service Parameter Configuration window. |
|---|---|

| Feature | Description | Configuration reference |
|---|---|---|
| Agent
                                          					 Greeting | Allows an
                                          					 agent to create and update a prerecorded greeting that plays at the beginning
                                          					 of a call, such as a customer call, before the agent begins the conversation
                                          					 with the caller. The agent can record greetings and update them, as required. When a
                                          					 customer calls, both the agent and the customer can hear the prerecorded
                                          					 greeting. The agent can remain on mute until the greeting ends or answer the
                                          					 call over the greeting. All codecs
                                          					 supported for the phone are supported for Agent Greeting calls. To enable
                                          					 Agent Greeting in the Cisco Unified CM Administration application,
                                          					 choose Device > Phone , and locate the IP Phone that
                                          					 you want to configure. Scroll to the Device Information Layout pane and set the
                                          					 Built In Bridge field to On or Default. If Built
                                          					 In Bridge is set to Default, choose System > Service
                                                						  Parameter and select the appropriate Server and
                                          					 Service. Scroll to the Clusterwide Parameters (Device - Phone) pane and set
                                          					 Builtin Bridge Enable to On. | For more
                                          					 information, see: Cisco Unified
                                                						  Communications Manager Features and Services Guide , "Barge
                                                						  and Privacy" chapter Cisco Unified
                                                						  Communications Manager System Guide , "Cisco
                                                						  Unified IP Phones" chapter |
| Audible
                                          					 Message Waiting Indicator (AMWI) | A stutter
                                          					 tone from the handset or speakerphone indicates that a user has one or more new
                                          					 voice messages on a line. | For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager System Guide , "Cisco
                                             						Unified IP Phone" chapter. |
| Auto
                                          					 Answer (Cisco
                                          					 Unified IP Phone 6911 only) | Connects
                                          					 incoming calls automatically after a ring or two. Auto
                                          					 Answer works with the speakerphone. | For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager Administration Guide , "Directory Number Configuration" chapter. |
| Automatic
                                          					 Port Synchronization (Cisco
                                          					 Unified IP Phone 6911 only) | When the
                                          					 Cisco Unified CM administrator uses the Remote Port Configuration feature to
                                          					 set the speed and duplex function of an IP Phone remotely, loss of packets can
                                          					 occur if one port is slower than the other. The
                                          					 Automatic Port Synchronization feature synchronizes the ports to the lowest
                                          					 speed among the two ports to eliminate packet loss. When automatic port
                                          					 synchronization is enabled, Cisco recommends that both ports autonegotiate. If
                                          					 one port autonegotiates and the other uses a fixed speed, the phone
                                          					 synchronizes to the fixed port speed. Note If both
                                                      						the ports use fixed speed, the Automatic Port Synchronization feature is
                                                      						ineffective. The Remote Port Configuration and Automatic Port Synchronization
                                                      						features are compatible only with IEEE 802.3AF Power of Ethernet (PoE)
                                                      						switches. Switches that support only Cisco Inline Power are not compatible.
                                                      						Enabling this feature on phones that are connected to these types of switches
                                                      						could result in loss of connectivity to Cisco Unified CM if the phone is
                                                      						powered by PoE. | Note | If both
                                                      						the ports use fixed speed, the Automatic Port Synchronization feature is
                                                      						ineffective. The Remote Port Configuration and Automatic Port Synchronization
                                                      						features are compatible only with IEEE 802.3AF Power of Ethernet (PoE)
                                                      						switches. Switches that support only Cisco Inline Power are not compatible.
                                                      						Enabling this feature on phones that are connected to these types of switches
                                                      						could result in loss of connectivity to Cisco Unified CM if the phone is
                                                      						powered by PoE. | To
                                          					 configure the parameter in the Cisco Unified CM Administration application,
                                          					 choose Device > Phone , select the appropriate IP
                                          					 phones, and scroll to the Product Specific Configuration Layoutpane. To
                                          					 configure the setting on multiple phones simultaneously, enable Automatic Port
                                          					 Synchronization in one of the following windows: Enterprise Phone Configuration ( System > Enterprise Phone
                                                      								Configuration ) Common Phone Profile Configuration ( Device > Device
                                                      								Settings > Common Phone Profile ) |
| Note | If both
                                                      						the ports use fixed speed, the Automatic Port Synchronization feature is
                                                      						ineffective. The Remote Port Configuration and Automatic Port Synchronization
                                                      						features are compatible only with IEEE 802.3AF Power of Ethernet (PoE)
                                                      						switches. Switches that support only Cisco Inline Power are not compatible.
                                                      						Enabling this feature on phones that are connected to these types of switches
                                                      						could result in loss of connectivity to Cisco Unified CM if the phone is
                                                      						powered by PoE. |
| Block
                                          					 External to External Transfer | Prevents
                                          					 users from transferring an external call to another external number. | For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager Features and Services Guide , "External
                                             						Call Transfer Restrictions" chapter. |
| Call
                                          					 Forward | Allows
                                          					 users to redirect incoming calls to another number. Call forward options
                                          					 include Call Forward All, Call Forward Busy, Call Forward No Answer, and Call
                                          					 Forward No Coverage. You hear a
                                          					 stutter tone when off hook if Call Forward All is active on your phone. | For more
                                          					 information, see: Cisco Unified
                                                						  Communications Manager Administration Guide , "Directory Number Configuration" chapter Cisco Unified
                                                						  Communications Manager System Guide , "Cisco
                                                						  Unified IP Phone" chapter Customize User Options Web Pages Options |
| Call
                                          					 Forward All Loop Breakout | Detects
                                          					 and prevents Call Forward All loops. When a Call Forward All loop is detected,
                                          					 the Call Forward All configuration is ignored and the call rings through. | For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager System Guide , "Cisco
                                             						Unified IP Phone" chapter. |
| Call
                                          					 Forward All Loop Prevention | Prevents a
                                          					 user from configuring a Call Forward All destination directly on the phone that
                                          					 creates a Call Forward All loop or that creates a Call Forward All chain with
                                          					 more hops than the existing Forward Maximum Hop Count service parameter allows. | For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager System Guide , "Cisco
                                             						Unified IP Phone" chapter. |
| Call
                                          					 Forward Destination Override | Allows you
                                          					 to override Call Forward All (CFA) in cases where the CFA target places a call
                                          					 to the CFA initiator. This feature allows the CFA target to reach the CFA
                                          					 initiator for important calls. The override works whether the CFA target phone
                                          					 number is internal or external. | For more
                                          					 information, see the Cisco Unified Communications Manager System Guide , "Understanding Directory Numbers" chapter. |
| Call
                                          					 Pickup (Cisco
                                          					 Unified IP Phone 6911 only) | Allows
                                          					 users to answer a call ringing on a coworker's phone. You can
                                          					 configure an audio alert for the primary line on the phone. This alert notifies
                                          					 the users that a call is ringing in their pickup group. | For more
                                          					 information, see the Cisco Unified Communications Manager Features and Services
                                             						Guide , "Call
                                             						Pickup" chapter. |
| Call
                                          					 Waiting | Indicates
                                          					 and allows users to answer an incoming call while active on another call. The phone
                                          					 sounds the call waiting tone (single beep) and the line button flashes amber. | For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager System Guide , "Understanding Directory Numbers" chapter. |
| cBarge | Allows a
                                          					 user to join a nonprivate call on a shared phone line. cBarge adds a user to an
                                          					 existing call and converts it into a conference, allowing the user and other
                                          					 parties to access conference features. | For more
                                          					 information, see: Cisco Unified
                                                						  Communications Manager Features and Services Guide , "Barge
                                                						  and Privacy" chapter Cisco Unified
                                                						  Communications Manager System Guide , "Cisco
                                                						  Unified IP Phone" chapter Cisco
                                                						  UnifiedCommunications Manager Features and Services Guide , "Barge
                                                						  and Privacy 
                                                						" chapter |
| Cisco
                                          					 Unified Communications Manager Express (Unified CME) Version Negotiation | The Cisco
                                          					 Unified Communication Manager Express uses a special tag in the information
                                          					 sent to the phone to identify itself. This tag enables the phone to provide
                                          					 services to the user that the switch supports. | For more
                                          					 information, see: Cisco Unified
                                                   							 Communications Manager Express System Administrator Guide Cisco Unified IP Phone and Cisco Unified Communications Manager Express Interaction |
| Cisco
                                          					 Unified Video Advantage (CUVA) (Cisco
                                          					 Unified IP Phone 6911 only) | Allows
                                          					 users to make video calls by using their Cisco Unified IP Phones, personal
                                          					 computers, and external video cameras. | Configure
                                          					 the Video Capabilities and Auto Line Select parameter in the Product Specific
                                          					 Configuration Layout section in Phone Configuration. |
| Cisco Web
                                          					 Dialer | Allows
                                          					 users to make calls from web and desktop applications. | For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager Features and Services Guide , "Cisco
                                             						Web Dialer" chapter. |
| Client
                                          					 Matter Code (CMC) | Enables a
                                          					 user to specify that a call relates to a specific client matter. | For more
                                          					 information, see the Cisco
                                             						UnifiedCommunications Manager Features and Services Guide , "Client
                                             						Matter Codes and Forced Authorization Codes" chapter. |
| Conference | Allows a
                                          					 user to talk simultaneously with multiple parties by calling each participant
                                          					 individually. Conference features include Conference and Meet Me. Allows a
                                          					 participant (host, initiator, or noninitiator) in a standard (adhoc)
                                          					 conference to add participants; also allows any conference participant to join
                                          					 together two standard conferences on the same line. Allows a
                                          					 conference host using a Cisco Unified IP Phone 6901 to remove the last
                                          					 participant that joined the conference using the hookflash feature. | The
                                          					 Advance Adhoc Conference service parameter, disabled by default in Cisco
                                          					 Unified Communications Manager, allows you to enable these features. For
                                          					 information on conferences, see the CiscoUnified Communications Manager System Guide , "Conference Bridges" chapter. For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager System Guide , "Cisco
                                             						Unified IP Phone" chapter. Note Be sure
                                                      						to inform your users if these features are activated. | Note | Be sure
                                                      						to inform your users if these features are activated. |
| Note | Be sure
                                                      						to inform your users if these features are activated. |
| CTI
                                          					 Applications | A computer
                                          					 telephony integration (CTI) route point can designate a virtual device to
                                          					 receive multiple, simultaneous calls for application-controlled redirection. | For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager Administration Guide , "CTI
                                             						Route Point Configuration" chapter. |
| EnergyWise | Enables an
                                          					 IP Phone to sleep (power down) and wake (power up) at predetermined times to
                                          					 promote energy savings. | For more
                                          					 information, see EnergyWise Setup on Cisco Unified IP Phone 6901 and 6911 . |
| Forced
                                          					 Authorization Codes (FAC) | Controls
                                          					 the types of calls that certain users can place. | For more
                                          					 information, see the Cisco
                                             						UnifiedCommunications Manager Features and Services Guide , "Client
                                             						Matter Codes and Forced Authorization Codes" chapter. |
| Group Call
                                          					 Pickup (Cisco
                                          					 Unified IP Phone 6911 only) | Allows a
                                          					 user to answer a call that is ringing on a phone in another group. | For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager Features and Services Guide , "Call
                                             						Pickup" chapter. |
| Hold
                                          					 Status | Enables
                                          					 phones with a shared line to distinguish between the local and remote lines
                                          					 that placed a call on hold. The Line
                                          					 LED lights green for Local Hold and red for Remote Hold. | No
                                          					 configuration required. |
| Hold/Resume | Allows the
                                          					 user to move a connected call from an active state to a held state by using the
                                          					 Hold button. The user resumes a held call by pressing the line button, speaker
                                          					 button, or going off hook. Note The LED
                                                      						on the line button pulses green when a local call is on hold and the LED pulses
                                                      						red when a remote call is on hold. | Note | The LED
                                                      						on the line button pulses green when a local call is on hold and the LED pulses
                                                      						red when a remote call is on hold. | No
                                          					 configuration required unless you want to use Music on Hold. For more
                                          					 information, see "Music on
                                             						Hold" in this table. |
| Note | The LED
                                                      						on the line button pulses green when a local call is on hold and the LED pulses
                                                      						red when a remote call is on hold. |
| Jitter
                                          					 Buffer | Handles
                                          					 jitter from 10 milliseconds (ms) to 1000 ms for both audio and video streams. | No
                                          					 configuration required. |
| Meet Me
                                          					 Conference (Cisco
                                          					 Unified IP Phone 6911 only) | Allows a
                                          					 user to host a Meet Me conference in which other participants call a
                                          					 predetermined number at a scheduled time. The user
                                          					 joins a Meet Me conference by pressing the feature button and the Meet Me
                                          					 conference number. | For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager Administration Guide , "Meet Me Number/Pattern
                                             						Configuration" chapter . |
| Message
                                          					 Waiting | Defines
                                          					 directory numbers for the message waiting on and message waiting off indicator.
                                          					 A directly connected voice message system uses the specified directory number
                                          					 to set or to clear a message waiting indicator for a particular Cisco Unified
                                          					 IP Phone. | For more
                                          					 information, see: Cisco Unified
                                                						  Communications Manager Administration Guide , "Message Waiting Configuration" chapter Cisco Unified
                                                						  Communications Manager System Guide , "Voice
                                                						  Mail Connectivity to Cisco Unified Communications Manager" chapter |
| Message
                                          					 Waiting Indicator | A light on
                                          					 the handset that indicates that a user has one or more new voice messages. | For more
                                          					 information, see: Cisco Unified
                                                						  Communications Manager Administration Guide , "Message Waiting Configuration" chapter Cisco Unified
                                                						  Communications Manager System Guide , "Voice
                                                						  Mail Connectivity to Cisco Unified Communications Manager" chapter |
| Monitoring
                                          					 and Recording (Cisco
                                          					 Unified IP Phone 6911 only) | Allows a
                                          					 supervisor to monitor an active call silently. The supervisor cannot be heard
                                          					 by either party on the call. The user may receive an audible alert during a
                                          					 call when it is being monitored. Callers
                                          					 may also receive an audible alert to indicate that the call is being monitored.
                                          					 The connected parties may also receive an audible alert that indicates the call
                                          					 is secure and is being monitored. | For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager Features and Services Guide , "Monitoring and Recording" chapter. |
| Multilevel
                                          					 Precedence and Preemption (MLPP) (SCCP
                                          					 phones only) | Provides a
                                          					 method of prioritizing calls within your phone system. Use this feature when
                                          					 users work in an environment where they need to make and receive urgent or
                                          					 critical calls. | For more
                                          					 information, see the Cisco Unified Communications Manager Features and Services Guide , "Multilevel Precedence and Preemption" chapter. |
| Music on
                                          					 Hold | Plays
                                          					 music while callers are on hold. | For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager Features and Services Guide , "Music On
                                             						Hold" chapter. |
| Mute (Cisco
                                          					 Unified IP Phone 6911 only) | Mutes the
                                          					 microphone on the handset or speakerphone. | No
                                          					 configuration required. |
| On-hook
                                          					 Call Transfer | Allows a
                                          					 user to press the Transfer button and go on-hook to complete a call transfer. | For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager System Guide , "Cisco
                                             						Unified IP Phones" chapter. |
| Plus
                                          					 Dialing | Allows the
                                          					 user to dial E.164 numbers prefixed with a plus (+) sign. To dial
                                          					 the + sign, the user needs to press and hold the star (*) key for at least 1
                                          					 second. This applies to dialing the first digit for the feature in the Cisco
                                          					 Unified IP Phone 6901 and 6911 only works with off-hook dialing. | No
                                          					 configuration required. |
| Private
                                          					 Line Automated Ringdown (PLAR) | The Cisco
                                          					 UnifiedCommunications Manager administrator can configure a phone number that
                                          					 the Cisco UnifiedIPPhone dials as soon as the handset goes off-hook. This can
                                          					 be useful for phones that are designated for calling emergency or hotline
                                          					 numbers. | For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager Administration Guide , "Directory Number Configuration" chapter. |
| Redial | Allows
                                          					 users to call the most recently dialed phone number by pressing the Redial
                                          					 button. | No
                                          					 configuration required. |
| Remote
                                          					 Port Configuration | Allows the
                                          					 administrator to configure the speed and duplex function of the phone Ethernet
                                          					 ports remotely by using Cisco Unified CM Administration. This enhances the
                                          					 performance for large deployments with specific port settings. Note If the
                                                      						ports are configured for Remote Port Configuration in Cisco Unified CM, the
                                                      						data cannot be changed on the phone. | Note | If the
                                                      						ports are configured for Remote Port Configuration in Cisco Unified CM, the
                                                      						data cannot be changed on the phone. | To
                                          					 configure the parameter in the Cisco Unified CM Administration application,
                                          					 choose Device > Phone , select the appropriate IP
                                          					 Phone, and scroll to the Product Specific Configuration Layout pane (Switch
                                          					 Port Remote Configuration or PC Port Remote Configuration). To
                                          					 configure the setting on multiple phones simultaneously, configure the remote
                                          					 configuration in either Enterprise Phone Configuration ( System > Enterprise Phone
                                                						  Configuration ) or Common Phone Profile Configuration
                                          					 ( Device > Device
                                                						  Settings > Common Phone Profile . (Switch Port
                                          					 Remote Configuration or PC Port Remote Configuration). |
| Note | If the
                                                      						ports are configured for Remote Port Configuration in Cisco Unified CM, the
                                                      						data cannot be changed on the phone. |
| Shared
                                          					 Line | Allows
                                          					 multiple phones to share the same phone number or allows a user to share a
                                          					 phone number with a coworker. | For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager System Guide , "Understanding Directory Numbers" chapter. |
| Speed
                                          					 Dialing (Cisco
                                          					 Unified IP Phone 6911 only) | Dials a
                                          					 specified number that has been previously stored. You
                                          					 configure this feature on the Cisco Unified Communications Manager. The users
                                          					 access speed dialing using the Feature key and the Feature Code. | For more
                                          					 information see: Cisco Unified
                                                						  Communications Manager Administration Guide , "Cisco
                                                						  Unified IP Phone Configuration" chapter Cisco Unified
                                                						  Communications Manager System Guide , "Cisco
                                                						  Unified IP Phone" chapter |
| SSH Access | Allows the
                                          					 administrator to enable or disable the SSH Access setting using Cisco Unified
                                          					 CM Administration. Enabling
                                          					 Secure Shell (SSH) access allows the phone to accept the SSH connections. Disabling
                                          					 SSH access blocks SSH access to the phone. | For more
                                          					 information, see UCR 2008 Setup |
| Time-of-Day Routing | Restricts
                                          					 access to specified telephony features by time period. | For more
                                          					 information, see: Cisco Unified
                                                						  Communications Manager Administration Guide , "Time
                                                						  Period Configuration" chapter Cisco Unified
                                                						  Communications Manager System Guide , "Time-of-Day Routing" chapter |
| Time Zone
                                          					 Update | Updates
                                          					 the Cisco Unified IP Phone with time zone changes. | For more
                                          					 information, see the Cisco
                                             						Unified Communications Manager Administration Guide , "Date/Time Group Configuration" chapter. |
| Transfer | Allows
                                          					 users to redirect connected calls from their phones to another number. | Some
                                          					 JTAPI/TAPI applications are not compatible with the Direct Transfer feature
                                          					 implementation on the Cisco Unified IP Phone. |
| UCR 2008 (SCCP
                                          					 phones only) | The Cisco
                                          					 Unified IP Phones using SCCP support Unified Capabilities Requirements (UCR)
                                          					 2008 by providing the following functions: Support for Federal
                                             						Information Processing Standard (FIPS) 140-2 Support for 80-bit SRTCP
                                             						Tagging As an IP
                                          					 Phone administrator, you must set up specific parameters in Cisco Unified
                                          					 Communications Manager Administration. | See UCR 2008 Setup . |
| Voice
                                          					 messaging system | Enables
                                          					 callers to leave messages if calls are unanswered. Users
                                          					 access messages using the Message button on the Cisco Unified IP Phone 6911. Users
                                          					 access messages using the access code on the Cisco Unified IP Phone 6901. | For more
                                          					 information, see: Cisco Unified
                                                						  Communications Manager Administration Guide , "Cisco
                                                						  Voice-Mail Port Configuration" chapter. Cisco Unified Communications Manager System Guide , "Voice
                                                						  Mail Connectivity to Cisco Unified Communications Manager" chapter. |

| Note | If both
                                                      						the ports use fixed speed, the Automatic Port Synchronization feature is
                                                      						ineffective. The Remote Port Configuration and Automatic Port Synchronization
                                                      						features are compatible only with IEEE 802.3AF Power of Ethernet (PoE)
                                                      						switches. Switches that support only Cisco Inline Power are not compatible.
                                                      						Enabling this feature on phones that are connected to these types of switches
                                                      						could result in loss of connectivity to Cisco Unified CM if the phone is
                                                      						powered by PoE. |
|---|---|

| Note | Be sure
                                                      						to inform your users if these features are activated. |
|---|---|

| Note | The LED
                                                      						on the line button pulses green when a local call is on hold and the LED pulses
                                                      						red when a remote call is on hold. |
|---|---|

| Note | If the
                                                      						ports are configured for Remote Port Configuration in Cisco Unified CM, the
                                                      						data cannot be changed on the phone. |
|---|---|

| Note | After you enable synchronization with the LDAP server,
                                                				  you cannot add additional users from CiscoUnifiedCommunicationsManager
                                                				  Administration. For more information on LDAP, see the "Understanding the Directory" chapter in Cisco Unified Communications Manager System Guide . |
|---|---|

| Step 1 | From Cisco Unified Communications Manager Administration, choose User Management > User
                                                   				  Groups . The Find and List Users window displays. |
|---|---|
| Step 2 | Enter the appropriate search criteria and click Find . |
| Step 3 | Select the Standard CCM End Users link. The User Group
                                             			 Configuration window for the Standard CCM End Users appears. |
| Step 4 | Select Add End Users to Group . The Find and List
                                             			 Users window appears. |
| Step 5 | Use the Find User drop-down list boxes to find the users that
                                             			 you want to add and click Find . A list of users that matches your search criteria appears. |
| Step 6 | In the list of records that appear, click the check box next to
                                             			 the users that you want to add to this user group. If the list is long, use the links at the bottom to see more results. Note The list of search results does not display users that
                                                            				  already belong to the user group. | Note | The list of search results does not display users that
                                                            				  already belong to the user group. |
| Note | The list of search results does not display users that
                                                            				  already belong to the user group. |
| Step 7 | Choose Add Selected . |

| Note | The list of search results does not display users that
                                                            				  already belong to the user group. |
|---|---|

| Step 1 | From Cisco Unified Communications Manager Administration,
                                             			 choose User Management > End
                                                   				  User . The Find and List Users window appears. |
|---|---|
| Step 2 | Enter the appropriate search criteria and click Find . |
| Step 3 | In the list of records that appear, select the link for the user. |
| Step 4 | Select Device Association . The User Device Association window appears. |
| Step 5 | Enter the appropriate search criteria and click Find . |
| Step 6 | Choose the device that you want to associate with the user by
                                             			 checking the box to the left of the device. |
| Step 7 | Choose Save Selected/Changes to associate the device
                                             			 with the user. |
| Step 8 | From the Related Links drop-down list in the upper, right corner of
                                             			 the window, select Back to User , and click Go . The End User Configuration window appears and the associated
                                                				devices that you chose display in the Controlled Devices pane. |
| Step 9 | Choose Save Selected/Changes . |

| Note | The settings apply to all User Options web pages at your site. |
|---|---|

| Step 1 | From Cisco Unified Communications Manager, choose System > Enterprise
                                                				  Parameters . The 
                                             				Enterprise Parameters Configuration window
                                             				appears. |
|---|---|
| Step 2 | In the CCMUser Parameters area, specify whether a parameter
                                          			 appears on the User Options web pages by choosing one of the following values from the
                                          			 Parameter Value drop-down list: True : Option displays on the User Options web pages
                                                   					 (default except for Show Ring Settings, and Show Call Forwarding). False : Option does not display on the User Options web
                                                   					 pages. Show All Settings : All call forward settings display
                                                   					 on the User Options web pages (default). Hide All Settings : No call forward settings display on
                                                   					 the User Options web pages. Show Only Call Forward All : Only call forward all
                                                   					 calls displays on the User Options web pages. |

| Field | Description |
|---|---|
| Enable Power Save Plus | Selects the schedule of days for which the phone powers down.
                                          					 Select multiple days by pressing and holding the Control key while clicking on the days
                                          					 for the schedule. By default, no days are selected. When Enable Power Save is checked, you receive a message to
                                          					 warn about emergency (e911) concerns. Caution While Power Save Plus Mode (the mode) is in effect,
                                                      						endpoints configured for the mode are disabled for emergency calling and from
                                                      						receiving inbound calls. By selecting this mode, you agree to the following:
                                                      						(i) You are taking full responsibility for providing alternate methods for
                                                      						emergency calling and receiving calls while the mode is in effect; (ii) Cisco
                                                      						has no liability in connection with your selection of the mode and all
                                                      						liability in connection with enabling the mode is your responsibility; and
                                                      						(iii) you will fully inform users of the effects of the mode on calls, calling
                                                      						and otherwise. Note To disable Power Save Plus, you must uncheck the Allow
                                                      						EnergyWise Overrides check box. Leaving the Allow EnergyWise Overrides checked
                                                      						with no days selected in the Enable Power Save Plus field does not disable
                                                      						Power Save Plus. | Caution | While Power Save Plus Mode (the mode) is in effect,
                                                      						endpoints configured for the mode are disabled for emergency calling and from
                                                      						receiving inbound calls. By selecting this mode, you agree to the following:
                                                      						(i) You are taking full responsibility for providing alternate methods for
                                                      						emergency calling and receiving calls while the mode is in effect; (ii) Cisco
                                                      						has no liability in connection with your selection of the mode and all
                                                      						liability in connection with enabling the mode is your responsibility; and
                                                      						(iii) you will fully inform users of the effects of the mode on calls, calling
                                                      						and otherwise. | Note | To disable Power Save Plus, you must uncheck the Allow
                                                      						EnergyWise Overrides check box. Leaving the Allow EnergyWise Overrides checked
                                                      						with no days selected in the Enable Power Save Plus field does not disable
                                                      						Power Save Plus. |
| Caution | While Power Save Plus Mode (the mode) is in effect,
                                                      						endpoints configured for the mode are disabled for emergency calling and from
                                                      						receiving inbound calls. By selecting this mode, you agree to the following:
                                                      						(i) You are taking full responsibility for providing alternate methods for
                                                      						emergency calling and receiving calls while the mode is in effect; (ii) Cisco
                                                      						has no liability in connection with your selection of the mode and all
                                                      						liability in connection with enabling the mode is your responsibility; and
                                                      						(iii) you will fully inform users of the effects of the mode on calls, calling
                                                      						and otherwise. |
| Note | To disable Power Save Plus, you must uncheck the Allow
                                                      						EnergyWise Overrides check box. Leaving the Allow EnergyWise Overrides checked
                                                      						with no days selected in the Enable Power Save Plus field does not disable
                                                      						Power Save Plus. |
| Phone On Time | Determines when the phone automatically turns on for the days
                                          					 selected in the Enable Power Save Plus field. Enter the time in this field in 24 hour format, where 00:00 is
                                          					 midnight. For example, to automatically power up the phone at 7:00 a.m.
                                          					 (0700), enter 7:00. To power up the phone at 2:00 p.m. (1400), enter 14:00. The default value is 00:00. |
| Phone Off Time | The time of day that the phone powers down for the days
                                          					 selected in the Enable Power Save Plus field. If the Phone On Time and the
                                          					 Phone Off Time fields contain the same value, the phone does not power down. Enter the time in this field in 24 hour format, where 00:00 is
                                          					 midnight. For example, to automatically power down the phone at 7:00
                                          					 a.m. (0700), enter 7:00. To power down the phone at 2:00 p.m. (1400), enter
                                          					 14:00. The default value is 24:00. |
| Phone Off Idle Timeout | The length of time that the phone must be idle before the
                                          					 phone powers down. The range of the field is 20 to 1440 minutes. The default value is 60 minutes. |
| Enable Audible Alert | When enabled, instructs the phone to play an audible alert
                                          					 starting at 10 minutes before to the time specified in the Phone Off Time
                                          					 field. The audible alert uses the phone ringtone, which briefly plays
                                          					 at specific times during the 10-minute alerting period. The alerting ringtone
                                          					 plays at the user’s designated volume level. The audible alert schedule is: At 10 minutes
                                             						before power down, play the ringtone four times At 7 minutes
                                             						before power down, play the ringtone four times At 4 minutes
                                             						before power down, play the ringtone four times At 30 seconds
                                             						before power down, play the ringtone 15 times or until the phone powers off This check box applies only if the Enable Power Save Plus list
                                          					 box has one or more days selected. |
| EnergyWise Domain | The EnergyWise domain that the phone is in. The maximum length
                                          					 is 127. |
| EnergyWise Secret | The security secret password that is used to communicate with
                                          					 the endpoints in the EnergyWise domain. The maximum length is 127. |
| Allow EnergyWise Overrides | This check box determines whether you will allow the
                                          					 EnergyWise domain controller policy to send power-level updates to the phones.
                                          					 The following conditions apply: The settings in Cisco Unified CM Administration take
                                                						  effect on schedule even if EnergyWise sends an override. For example, assume the Phone Off Time is set to 22:00 (10:00
                                          					 p.m.), the value in the Phone On Time field is 06:00 (6:00 a.m.), and the
                                          					 Enable Power Save Plus has one or more days selected. If EnergyWise
                                             						directs the phone to turn off at 20:00 (8:00 p.m.), that directive will remain
                                             						in effect (assuming no phone user intervention occurs) until the configured
                                             						Phone On Time at 6:00 a.m. At 6:00 a.m., the
                                             						phone turns on and resumes receiving the power level changes from the settings
                                             						in Unified Communications Manager. To change the
                                             						power level on the phone again, EnergyWise must reissue a new power-level
                                             						change command. Note To disable Power Save Plus, you must uncheck the Allow
                                                      						EnergyWise Overrides check box. Leaving the Allow EnergyWise Overrides checked
                                                      						with no days selected in the Enable Power Save Plus field does not disable
                                                      						Power Save Plus. | Note | To disable Power Save Plus, you must uncheck the Allow
                                                      						EnergyWise Overrides check box. Leaving the Allow EnergyWise Overrides checked
                                                      						with no days selected in the Enable Power Save Plus field does not disable
                                                      						Power Save Plus. |
| Note | To disable Power Save Plus, you must uncheck the Allow
                                                      						EnergyWise Overrides check box. Leaving the Allow EnergyWise Overrides checked
                                                      						with no days selected in the Enable Power Save Plus field does not disable
                                                      						Power Save Plus. |

| Caution | While Power Save Plus Mode (the mode) is in effect,
                                                      						endpoints configured for the mode are disabled for emergency calling and from
                                                      						receiving inbound calls. By selecting this mode, you agree to the following:
                                                      						(i) You are taking full responsibility for providing alternate methods for
                                                      						emergency calling and receiving calls while the mode is in effect; (ii) Cisco
                                                      						has no liability in connection with your selection of the mode and all
                                                      						liability in connection with enabling the mode is your responsibility; and
                                                      						(iii) you will fully inform users of the effects of the mode on calls, calling
                                                      						and otherwise. |
|---|---|

| Note | To disable Power Save Plus, you must uncheck the Allow
                                                      						EnergyWise Overrides check box. Leaving the Allow EnergyWise Overrides checked
                                                      						with no days selected in the Enable Power Save Plus field does not disable
                                                      						Power Save Plus. |
|---|---|

| Note | To disable Power Save Plus, you must uncheck the Allow
                                                      						EnergyWise Overrides check box. Leaving the Allow EnergyWise Overrides checked
                                                      						with no days selected in the Enable Power Save Plus field does not disable
                                                      						Power Save Plus. |
|---|---|

| Parameter | Administration Path | Procedure |
|---|---|---|
| FIPS Mode | Device > Device
                                                						  Settings > Common Phone Profile | Set Up UCR 2008 in Common Phone Profile |
| System > Enterprise
                                                						  Phone Configuration | Set Up UCR 2008 in Enterprise Phone Configuration |
| SSH Access | Device > Phone | Set Up UCR 2008 in Phone |
| Device > Device
                                                						  Settings > Common Phone Profile | Set Up UCR 2008 in Common Phone Profile |
| Web Access | Device > Phone | Set Up UCR 2008 in Phone |
| 80-bit SRTCP | Device > Device
                                                						  Settings > Common Phone Profile | Set Up UCR 2008 in Common Phone Profile |
| System > Enterprise
                                                						  Phone Configuration | Set Up UCR 2008 in Enterprise Phone Configuration |
| IP Addressing Mode | Device > Device
                                                						  Settings > Common Device
                                                						  Configuration | Set Up UCR 2008 in Common Device Configuration |
| IP Addressing Mode Preference for Signaling | Device > Device
                                                						Settings > Common Device Configuration | Set Up UCR 2008 in Common Device Configuration |

| Step 1 | Choose Device > Phone . |
|---|---|
| Step 2 | Set the SSH Access parameter to Disabled . |
| Step 3 | Set the Web Access parameter to Disabled . |
| Step 4 | Select Save . |

| Step 1 | Choose Device > Device
                                                				  Settings > Common Phone Profile . |
|---|---|
| Step 2 | Set the FIPS Mode parameter to Enabled . |
| Step 3 | Set the SSH Access parameter to Disabled . |
| Step 4 | Set the 80-bit SRTCP parameter to Enabled . |
| Step 5 | Select Save . |

| Step 1 | Choose System > Enterprise Phone Configuration . |
|---|---|
| Step 2 | Set the FIPS Mode parameter to Enabled . |
| Step 3 | Set the 80-bit SRTCP parameter to Enabled . |
| Step 4 | Select Save . |

| Step 1 | Choose Device > Device
                                                				  Settings > Common Device
                                                				  Configuration . |
|---|---|
| Step 2 | Set the IP Addressing Mode parameter. |
| Step 3 | Set the IP Addressing Mode Preference for Signaling parameter. |
| Step 4 | Select Save . |