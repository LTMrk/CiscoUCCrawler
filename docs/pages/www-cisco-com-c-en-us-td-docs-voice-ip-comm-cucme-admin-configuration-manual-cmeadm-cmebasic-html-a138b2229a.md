---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmebasic-html-a138b2229a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmebasic.html
retrieved_at: 2026-08-21T07:22:21.144754+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Configuring Phones to Make Basic
	 Calls

## Chapter: Configuring Phones to Make Basic
	 Calls

# Configuring Phones to Make Basic
                     	 Calls

This chapter
                        		describes how to configure Cisco Unified IP phones in Cisco Unified
                        		Communications Manager Express (Cisco Unified CME) so that you can make and
                        		receive basic calls.

Caution

The Interactive
                                    		  Voice Response (IVR) media prompts feature is only available on the IAD2435
                                    		  when running IOS version 15.0(1)M or later.

## Prerequisites for
                        	 Configuring Phones to Make Basic Calls

Cisco IOS
                                 			 software and Cisco Unified CME software, including phone firmware files for
                                 			 Cisco Unified IP phones to be connected to Cisco Unified CME, must be installed
                                 			 in router flash memory. See Install Cisco Unified CME Software .

For
                                 			 Cisco Unified IP phones that are running SIP and are connected directly to
                                 			 Cisco Unified CME, Cisco Unified CME 3.4 or a later version must be installed
                                 			 on the router. See Install Cisco Unified CME Software .

Procedures in Network Parameters and Configure System-Level Parameters must be completed before you start the procedures in this section.

## Restrictions for
                        	 Configuring Phones to Make Basic Calls

When you are
                           		configuring dial peers or ephone-dns, including park slots and conferencing
                           		extensions, on Cisco Integrated Services Router Voice Bundles, the following
                           		message may appear to warn you that free memory is not available:

```
%DIALPEER_DB-3-ADDPEER_MEM_THRESHOLD: Addition of dial-peers limited by available memory
```

To configure more
                           		dial peers or ephone-dns, increase the DRAM in the system. A moderately complex
                           		configuration may exceed the default 256 MB DRAM and require 512 MB DRAM. Note
                           		that many factors contribute to memory usage, in addition to the number of dial
                           		peers and ephone-dns configured.

## Information About Configuring Phones to Make Basic Calls

### Phones in Cisco Unified CME

An ephone, or “Ethernet phone,” for SCCP or a voice-register pool for
                              		SIP is the software configuration for a phone in Cisco Unified CME. This phone
                              		can be either a Cisco Unified IP phone or an analog phone. Each physical phone
                              		in your system must be configured as an ephone or voice-register pool on the
                              		Cisco Unified CME router to receive support in the LAN environment. Each phone
                              		has a unique tag, or sequence number, to identify it during configuration.

For information on the phones supported in Cisco Unified CME Release 8.8 and later versions, see Phone Feature Support Guide for Unified CME, Unified SRST, Unified E-SRST, and Unified Secure SRST .

### Directory Numbers

A directory number, also known as an ephone-dn for SCCP or a
                              		voice-register dn for SIP, is the software configuration in Cisco Unified CME
                              		that represents the line connecting a voice channel to a phone. A directory
                              		number has one or more extension or telephone numbers associated with it to
                              		allow call connections to be made. Generally, a directory number is equivalent
                              		to a phone line, but not always. There are several types of directory numbers,
                              		which have different characteristics.

Each directory number has a unique dn-tag , or sequence number, to identify it
                              		during configuration. Directory numbers are assigned to line buttons on phones
                              		during configuration.

One virtual voice port and one or more dial peers are automatically
                              		created for each directory number, depending on the configuration for SCCP
                              		phones, or for SIP phones, when the phone registers in Cisco Unified CME.

Because each directory number represents a virtual voice port in the
                              		router, the number of directory numbers that you create corresponds to the
                              		number of simultaneous calls that you can have. This means that if you want
                              		more than one call to the same number to be answered simultaneously, you need
                              		multiple directory numbers with the same destination number pattern.

The directory number is the basic building block of a Cisco Unified CME
                              		system. Six different types of directory numbers can be combined in different
                              		ways for different call coverage situations. Each type will help with a
                              		particular type of limitation or call-coverage need. For example, if you want
                              		to keep the number of directory numbers low and provide service to a large
                              		number of people, you might use shared directory numbers. Or if you have a
                              		limited quantity of extension numbers that you can use and you need to have a
                              		large quantity of simultaneous calls, you might create two or more directory
                              		numbers with the same number. The key is knowing how each type of directory
                              		number works and its advantages.

Not all types of directory numbers can be configured for all phones or
                              		for all protocols. In the remaining information about directory numbers, we
                              		have used SCCP in the examples presented but that does not imply exclusivity.
                              		The following sections describe the types of directory numbers in a
                              		Cisco Unified CME system:

#### Single-Line

A single-line directory number has the following characteristics:

Makes one call connection at a time using one phone line button. A single-line directory number has one telephone number associated
                                       with it.

Should be used when phone buttons have a one-to-one correspondence to the PSTN lines that come into a Cisco Unified CME system.

Should be used for lines that are dedicated to intercom, paging, message-waiting indicator (MWI), loopback, and music-on-hold
                                       (MOH) feed sources.

Must have more than one single-line directory number on a phone when used with multiple-line features like call waiting, call
                                       transfer, and conferencing.

Can be combined with dual-line directory numbers on the same phone.

You must make the choice to configure each directory number in your system as either dual-line or single-line when you initially
                                             create configuration entries. If you need to change from single-line to dual-line later, you must delete the configuration
                                             for the directory number, then recreate it.

Single-Line Directory Number shows a single-line directory number for an SCCP phone in Cisco Unified CME.

#### Dual-Line

A dual-line directory number has the following characteristics:

Has one voice port with two channels.

Supported on IP phones that are running SCCP; not supported on IP
                                       			 phones that are running SIP.

Can make two call connections at the same time using one phone line
                                       			 button. A dual-line directory number has two channels for separate call
                                       			 connections.

Can have one number or two numbers (primary and secondary)
                                       			 associated with it.

Should be used for a directory number that needs to use one line
                                       			 button for features like call waiting, call transfer, or conferencing.

Cannot be used for lines that are dedicated to intercom, paging,
                                       			 message-waiting indicator (MWI), loopback, and music-on-hold (MOH) feed
                                       			 sources.

Can be combined with single-line directory numbers on the same
                                       			 phone.

You must make the choice to configure each directory number in your
                                             		  system as either dual-line or single-line when you initially create
                                             		  configuration entries. If you need to change from single-line to dual-line
                                             		  later, you must delete the configuration for the directory number, then
                                             		  recreate it.

Dual-Line Directory Number shows a dual-line directory number for an SCCP phone in Cisco Unified CME.

#### Octo-Line

An octo-line
                                 		directory number supports up to eight active calls, both incoming and outgoing,
                                 		on a single button of a SCCP phone. Unlike a dual-line directory number, which
                                 		is shared exclusively among phones (after a call is answered, that phone owns
                                 		both channels of the dual-line directory number), an octo-line directory number
                                 		can split its channels among other phones that share the directory number. All
                                 		phones are allowed to initiate or receive calls on the idle channels of the
                                 		shared octo-line directory number.

Because octo-line
                                 		directory numbers do not require a different ephone-dn for each active call,
                                 		one octo-line directory number can handle multiple calls. Multiple incoming
                                 		calls to an octo-line directory number ring simultaneously. After a phone
                                 		answers a call, the ringing stops on that phone and the call-waiting tone plays
                                 		for the other incoming calls. When phones share an octo-line directory number,
                                 		incoming calls ring on phones without active calls and these phones can answer
                                 		any of the ringing calls. Phones with an active call hear the call-waiting
                                 		tone.

After a phone
                                 		answers an incoming call, the answering phone is in the connected state. Other
                                 		phones that share the octo-line directory number are in the remote-in-use
                                 		state.

After a connected
                                 		call on an octo-line directory number is put on-hold, any phone that shares
                                 		this directory number can pick up the held call. If a phone user is in the
                                 		process of initiating a call transfer or creating a conference, the call is
                                 		locked and other phones that share the octo-line directory number cannot steal
                                 		the call.

Octo-Line
                                    		  Directory Number shows an octo-line directory number for SCCP phones in Cisco Unified CME.

The Barge and
                                 		Privacy features control whether other phones are allowed to view call
                                 		information or join calls on the shared octo-line directory number.

##### Feature Comparison by Directory Number Line-Mode on SCCP Phones

Table 1 lists some common directory number features and their support based on the type of line mode defined with the ephone-dn command.

Feature

Single-Line

Dual-Line

Octo-Line

Barge

—

—

Yes

Busy Trigger

—

—

Yes

Conferencing (8-party)

—

4 directory numbers

1 directory number

FXO Trunk Optimization

Yes

Yes

—

Huntstop Channel

—

Yes

Yes

Intercom

Yes

—

—

Key System (one call per button)

Yes

—

—

Maximum Calls

—

—

Yes

MWI

Yes

—

—

Overlay directory numbers (c, o, x)

Yes

Yes

—

Paging

Yes

—

—

Park

Yes

—

—

Privacy

—

—

Yes

#### SIP Shared-Line
                              	 (Nonexclusive)

Cisco Unified CME 7.1 and later versions support SIP shared
                                 		lines to allow multiple phones to share a common directory number. All phones
                                 		sharing the directory number can initiate and receive calls at the same time.
                                 		Calls to the shared line ring simultaneously on all phones without active calls
                                 		and any of these phones can answer the incoming calls. After a phone answers a
                                 		call, the ringing stops on all phones and the call-waiting tone plays for other
                                 		incoming calls to the connected phone.

The phone that
                                 		answers an incoming call is in the connected state. Other phones that share the
                                 		directory number are in the remote-in-use state. The first user that answers
                                 		the call on the shared line is connected to the caller and the remaining users
                                 		see the call information and status of the shared line.

Calls on a shared
                                 		line can be put on hold like calls on a non-shared line. When a call is placed
                                 		on hold, other phones with the shared-line directory number receive a hold
                                 		notification so all phones sharing the line are aware of the held call. Any
                                 		shared-line phone user can resume the held call. If the call is placed on hold
                                 		as part of a conference or call transfer operation, the call cannot be resumed
                                 		by other shared-line phone users. The ID of the held call is used by other
                                 		shared-line members to resume the call. Notifications are sent to all
                                 		associated phones when a held call is resumed on a shared line.

Shared lines support
                                 		up to 16 calls, depending on the configuration in Cisco Unified CME, which
                                 		rejects any new call that exceeds the configured limit. For configuration
                                 		information, see Create Directory Numbers for SIP Phones .

The Barge and
                                 		Privacy features control whether other phones are allowed to view call
                                 		information or join calls on the shared-line directory number. See Barge and Privacy .

When the no supplementary-service
                                                   				sip handle-replaces command is configured, SIP shared-line is not
                                             		  supported on CME.

#### Two Directory
                              	 Numbers with One Telephone Number

Two directory
                                 		numbers with one telephone or extension number have the following
                                 		characteristics:

Have the same
                                       			 telephone number but two separate virtual voice ports, and therefore can have
                                       			 two separate call connections.

Can be dual-line
                                       			 (SCCP only) or single-line directory numbers.

Can appear on
                                       			 the same phone on different buttons or on different phones.

Should be used
                                       			 when you want the ability to make more call connections while using fewer
                                       			 numbers.

Two Directory
                                    		  Numbers with One Number on One Phone shows a phone with two buttons that have the same number, extension 1003. Each
                                 		button has a different directory number (button 1 is directory number 13 and
                                 		button 2 is directory number 14), so each button can make one independent call
                                 		connection if the directory numbers are single-line and two call connections
                                 		(for a total of four) if the directory numbers are dual-line.

Two Directory
                                    		  Numbers with One Number on Two Phones shows two phones that each have a button with the same number. Because the
                                 		buttons have different directory numbers, the calls that are connected on these
                                 		buttons are independent of one another. The phone user at phone 4 can make a
                                 		call on extension 1003, and the phone user on phone 5 can receive a different
                                 		call on extension 1003 at the same time.

The two directory
                                 		numbers-with-one-number situation is different than a shared line, which also
                                 		has two buttons with one number but has only one directory number for both of
                                 		them. A shared directory number will have the same call connection at all the
                                 		buttons on which the shared directory number appears. If a call on a shared
                                 		directory number is answered on one phone and then placed on hold, the call can
                                 		be retrieved from the second phone on which the shared directory number
                                 		appears. But when there are two directory numbers with one number, a call
                                 		connection appears only on the phone and button at which the call is made or
                                 		received. In the example in Two Directory
                                    		  Numbers with One Number on Two Phones ,
                                 		if the user at phone 4 makes a call on button 1 and puts it on hold, the call
                                 		can be retrieved only from phone 4. For more information about shared lines,
                                 		see Shared Line (Exclusive) section.

The examples in Two Directory
                                    		  Numbers with One Number on One Phone and Two Directory
                                    		  Numbers with One Number on Two Phones show how two directory numbers with one number are used to provide a small hunt
                                 		group capability. In Two Directory
                                    		  Numbers with One Number on One Phone ,
                                 		if the directory number on button 1 is busy or does not answer, an incoming
                                 		call to extension 1003 rolls over to the directory number associated with
                                 		button 2 because the appropriate related commands are configured. Similarly, if
                                 		button 1 on phone 4 is busy, an incoming call to 1003 rolls over to button 1 on
                                 		phone 5.

#### Dual-Number

A dual-number
                                 		directory number has the following characteristics:

Has two
                                       			 telephone numbers, a primary number and a secondary number.

Can make one
                                       			 call connection if it is a single-line directory number.

Can make two
                                       			 call connections at a time if it is a dual-line directory number (SCCP only).

Should be used
                                       			 when you want to have two different numbers for the same button without using
                                       			 more than one directory number.

Dual-Number
                                    		  Directory shows a directory number that has two numbers, extension 1006 and extension
                                 		1007.

#### Shared Line
                              	 (Exclusive)

An exclusively
                                 		shared directory number has the following characteristics:

Has a line that
                                       			 appears on two different phones but uses the same directory number, and
                                       			 extension or phone number.

Can make one
                                       			 call at a time and that call appears on both phones.

Should be used
                                       			 when you want the capability to answer or pick up a call at more than one
                                       			 phone.

Because this
                                 		directory number is shared exclusively among phones, if the directory number is
                                 		connected to a call on one phone, that directory number is unavailable for
                                 		calls on any other phone. If a call is placed on hold on one phone, it can be
                                 		retrieved on the second phone. This is like having a single-line phone in your
                                 		house with multiple extensions. You can answer the call from any phone on which
                                 		the number appears, and you can pick it up from hold on any phone on which the
                                 		number appears.

Shared
                                    		  Directory Number (Exclusive) shows a shared directory number on phones that are running SCCP. Extension 1008
                                 		appears on both phone 7 and phone 8.

#### Shared Lines with
                              	 Voice Class Codec Support

From Unified CME
                                 		12.2 Release, Unified CME supports voice class codecs (VCC) with SIP shared
                                 		lines. A VCC is a construct within which a codec preference order is defined.
                                 		Preferences defined within the VCC can be used to determine which codecs will
                                 		be selected over others. When a VCC is applied to a dial peer on the Unified
                                 		CME, the dial peer then follows the preference order defined in the VCC.

The VCC
                                 		configuration can be applied for phones having shared line configured on
                                 		Unified CME. However, the voice class codec behavior of SIP trunk remains
                                 		unchanged. It is recommended that the same voice class codec configuration is
                                 		applied on all phones using the shared line directory number. The VCC
                                 		configuration applied under the voice register
                                       			 pool configuration mode is used for filtering the codecs on
                                 		inbound and outbound calls from the phone. If the VCC configuration does not
                                 		have a common codec negotiated, then the call is disconnected. When the codec
                                 		on the incoming SIP trunk is not listed in the VCC, the call is not placed. It
                                 		is mandatory to configure the CLI command supplementary-service
                                       			 media-renegotiate under voice service
                                       			 voip configuration mode for VCC configuration support with SIP
                                 		shared lines. For a sample configuration of VCC with shared line, see Examples for Configuring VCC with Shared Lines .

##### Codec
                                    		  Support

All the codecs
                                    		  listed under the CLI command voice
                                       			 class codec are supported as part of the VCC support for SIP shared
                                    		  lines on Unified CME.

##### Feature
                                    		  Support

Hold and
                                             				Remote Resume

Barge

cBarge

Video

MOH
                                             				Transcoding

Privacy

##### Advantages

Insertion of
                                             				transcoding resource to place a call can be avoided.

##### Restrictions

Transcoding is
                                             				not supported for SIP shared lines with VCC support.

#### Mixed Shared Lines

Cisco Unified CME 9.0 and later versions support the mixed Cisco Unified
                                 		SIP/SCCP shared line. This feature allows Cisco Unified SIP and SCCP IP phones
                                 		to share a common directory number.

The mixed shared line supports up to 16 calls, depending on the
                                 		configuration in Cisco Unified CME, which rejects any new call that exceeds the
                                 		configured limit.

For configuration information, see Create Directory Numbers for SCCP Phones and Create Directory Numbers for SIP Phones .

##### Incoming and Outgoing Calls

All phones sharing the common directory number can initiate and receive
                                    		calls at the same time. Calls to the mixed shared line ring simultaneously on
                                    		all phones without active calls and any of these phones can answer the incoming
                                    		calls. After a phone answers a call, the ringing stops on all phones and the
                                    		call-waiting tone plays for other incoming calls to the connected phone.

The phone that answers an incoming call is in the connected state. Other
                                    		phones that share the common directory number are in the remote-in-use state.
                                    		The first user who answers the call on the mixed shared line is connected to
                                    		the caller and the remaining users see the call information and status of the
                                    		mixed shared line.

When a mixed shared-line user makes an outgoing call on the shared line,
                                    		all the other shared-line users are notified of the outgoing call. When the
                                    		called party answers, the caller is connected while the remaining shared-line
                                    		users see the call information and the status of the call on the mixed shared
                                    		line.

##### Hold and
                                 	 Resume

Calls on a mixed
                                    		shared line can be put on hold like calls on a non-shared line. When a call is
                                    		placed on hold, other phones with the shared-line directory number receive a
                                    		hold notification so all phones sharing the line are aware of the call on hold.
                                    		Any shared-line phone user can resume the call on hold. The ID of the call on
                                    		hold is used by other shared-line members to resume the call. Notifications are
                                    		sent to all associated phones when a call on hold is resumed on a mixed shared
                                    		line. If the call is placed on hold as part of a conference or call transfer
                                    		operation, the resume feature is not allowed.

##### Privacy on Hold

The Privacy on Hold feature prevents other phone users from viewing call
                                    		information or retrieving a call put on hold by another phone sharing a common
                                    		directory number. Only the caller who put the call on hold can see the status
                                    		of the held call.

By default, Privacy on Hold feature is disabled for all phones on a
                                    		shared line. Use the privacy-on-hold command in telephony-service
                                    		configuration mode to enable the Privacy feature for calls that are on hold on
                                    		Cisco Unified SCCP IP phones on a mixed shared line. Use the privacy-on-hold command in voice register
                                    		global configuration mode to enable the Privacy feature for calls that are on
                                    		hold on Cisco Unified SIP IP phones on a mixed shared line.

The no privacy and privacy off commands override the privacy-on-hold command.

##### Call Transfer and Forwarding

Both blind transfer and consult transfer are supported on a mixed shared
                                    		line. A mixed shared line can be the one transferring the call, the one
                                    		receiving the transferred call, or the call being transferred.

There are four types of call forwarding: all calls, no answer, busy, and
                                    		night service. Any of these can be configured under a shared SCCP ephone-dn or
                                    		a shared SIP voice register dn. However, the user must keep the call forwarding
                                    		parameters for the SCCP and SIP lines synchronized with each other. A mixed
                                    		shared line can be the one forwarding the call, the one receiving the forwarded
                                    		call, or the call being forwarded.

For more information, see Configure Call Transfer and Forwarding .

##### Call Pickup

The Call Pickup feature is supported on a mixed shared line and SIP lines only when the call-park system application command is configured in telephony-service configuration mode.

A user can answer a call that:

Originates from a shared line

Rings on a shared line

Originates from one shared line and rings on another shared line

For more information, see Call Pickup .

##### Call Park

The Call Park feature is supported on a mixed shared line and SIP lines only when the call-park system application command is configured in telephony-service configuration mode.

For more information, see Call Park .

##### Message Waiting Indication

SCCP and SIP message-waiting indication (MWI) services are supported on
                                    		Cisco Unity and Cisco Unity voice mails on mixed shared lines:

The following are two ways of registering a mixed shared line for an MWI
                                    		service from a SIP-based MWI server with the shared-line option:

Configure the mwi sip command in ephone-dn or
                                          			 ephone-dn-template configuration mode.

Configure the mwi command in voice register dn
                                          			 configuration mode.

For SCCP MWI service on a mixed shared line, use the mwi { off | on | on-off } command in ephone-dn
                                    		configuration mode to enable a specific Cisco Unified IP phone extension to
                                    		receive MWI notification from an external voice-messaging system.

##### Software Conferencing

A local software conference can be created on a mixed shared line, with
                                    		the mixed shared line acting as a conference creator and a conference
                                    		participant.

For software conferencing on a mixed shared line, other shared-line
                                    		users remain in remote-in-use state and do not see the calls on hold when the
                                    		conference call is put on hold by a mixed-shared-line user acting as the
                                    		conference creator.

Only the conference creator, who put a conference call on hold, can
                                                		  resume the conference call.

##### Dial Plan

A dial plan pattern enables abbreviated extensions to be expanded into
                                    		fully qualified E.164 numbers and builds additional dial peers for the expanded
                                    		numbers it creates.

Features are effectively supported on a mixed shared line when dial-plan
                                    		patterns have matching configurations in telephony-service and voice register
                                    		global configuration modes using the dialplan pattern command.

##### Busy Lamp Field Speed-Dial Monitoring

A mixed shared line only supports directory number-based Busy-Lamp-Field
                                    		(BLF) Speed-Dial monitoring and not device-based monitoring.

##### Restrictions For
                                 	 Mixed Shared Lines

The following
                                    		features are not supported on mixed Cisco Unified SIP/SCCP shared lines:

Single Number
                                          			 Reach

Hardware
                                          			 Conferencing

Remote-resume on
                                          			 a local software conference call

Video calls

Overlay DNs on
                                          			 Cisco Unified SCCP IP phones

###### Feature
                                       		  Support

The following
                                       		  features are supported on mixed Cisco Unified SIP/SCCP shared lines from
                                       		  Unified CME, 12.2:

Hold and
                                             				Resume

Privacy

Barge

cBarge

#### Overlaid Directory Numbers

An overlaid directory number has the following characteristics:

Is a member of an overlay set, which includes all the directory
                                       			 numbers that have been assigned together to a particular phone button.

Can have the same telephone or extension number as other members of
                                       			 the overlay set or different numbers.

Can be single-line or dual-line, but cannot be mixed single-line and
                                       			 dual-line in the same overlay set.

Can be shared on more than one phone.

Overlaid directory numbers provide call coverage similar to shared
                                 		directory numbers because the same number can appear on more than one phone.
                                 		The advantage of using two directory numbers in an overlay arrangement rather
                                 		than as a simple shared line is that a call to the number on one phone does not
                                 		block the use of the same number on the other phone, as would happen if it were
                                 		a shared directory number.

For information about configuring call coverage using overlaid ephone-dns, see Configure Call Coverage Features .

You can overlay up to 25 lines on a single button. A typical use of overlaid directory numbers would be to create a “10x10”
                                 shared line, with 10 lines in an overlay set shared by 10 phones, resulting in the possibility of 10 simultaneous calls to
                                 the same number. For configuration information, see Creating Directory Numbers for a Simple Key System on SCCP Phone .

### Auto Registration of SIP Phones on Cisco Unified CME

Cisco Unified CME supports auto registration of both SIP and SCCP
                              		phones. When the auto registration feature is enabled, the voice register pool and voice register dn commands do not need to be
                              		manually configured for the phones. The configuration is automatically created
                              		when the phone registers.

The auto registration feature for SIP phones is enabled with the auto-register command under voice register global configuration mode. For more information on auto-register command, see Cisco Unified Communications Manager Express Command Reference .

The auto registration of SCCP phones is enabled with the auto-reg-ephone command under telephony-service configuration mode. For more information on auto-register command, see Cisco Unified Communications Manager Express Command Reference .

As part of the auto-register command, certain CLI sub-mode
                              		configuration options are available to the administrator to successfully
                              		register phones using auto-registration on Unified CME.

```
Router(config-register-global)#auto-register
Router(config-voice-auto-register)#
Router(config-voice-auto-register)# ?
VOICE auto register configuration commands:
  auto-assign     Define DN range for auto assignment
  default         Set a command to its defaults
  exit            Exit from voice register group configuration mode
  no              Negate a command or set its defaults
  password        Default password for auto-register phones
  service-enable  Enable SIP phone Auto-Registration
  template        Default template for auto-register phones
```

For details on the configuration steps for auto registration of SIP phones, see Configure Auto Registration for SIP Phones .

Service Enable —If the administrator needs to temporarily disable or
                              		enable auto registration without losing configurations such as DN range, and
                              		password, the no form of the CLI option service-enable is used ( no
                                    			 service-enable ). Once auto-register command is entered, the service
                              		is enabled by default. To re-enable the auto registration feature, use the
                              		command service-enable . It is a sub-mode option in the
                              		CLI command auto-register . To disable auto registration
                              		including removal of configurations such as password and DN range, the no form of the CLI command auto-register (under voice register global) is
                              		used.

```
Router(config)#voice register global
Router(config-register-global)#auto-register
Router(config-voice-auto-register)#no service-enable ?
<cr>
```

Password —As part of the auto registration feature, authentication of
                              		phones registering on Unified CME is enabled. When the phone registers with
                              		Unified CME, it is mandatory for the administrator to configure the password
                              		credentials; username is assigned by default. However, the administrator can
                              		modify the username and password credentials under the corresponding voice
                              		register pool that gets created after auto registration.

```
Router(config)#voice register global
Router(config-register-global)#auto-register
Router(config-voice-auto-register)#password ?
  WORD  Password string
```

It is mandatory that password is configured before DN range
                                          		  (auto-assign) while registering phones using auto registration.

Auto Assign —It is mandatory to define a directory number (DN) range for
                              		auto-registration feature to work. The DN range that can be assigned to phones
                              		registering on Unified CME is configured using auto-assign < first-dn > to < last-dn >,
                              		which is a submode option of the CLI command auto-register (under voice register global ). The DN numbers assigned
                              		to the phones through auto registration are always within the DN range that is
                              		defined. However, ensure that the defined DN range is within the maximum DNs
                              		recommended for the supported platform.

```
Router(config)#voice register global
Router(config-register-global)#auto-register
Router(config-voice-auto-register)#auto-assign ?
  <1-4294967295>  First DN number
Router(config-voice-auto-register)#auto-assign 1001 ?
  <1-4294967295>  Last DN number
Router(config-voice-auto-register)#auto-assign 1001 to 1010
```

The automatic registration feature also provides the administrators with
                              		the option to enhance a predefined DN range. The enhancement of an existing DN
                              		range is supported such that the new first-dn is not greater that the existing
                              		first-dn and the new last-dn is not less than the existing last-dn.

For example, the DN range 8001-8006 can be enhanced as 7999-8006,
                              		8000-8007, but not as 8002-8006 or 8001 to 8005.

```
Router# show running-config | section voice register global 
	 voice register global 
	  mode cme 
	  source-address 8.41.20.1 port 5060 
	 		 auto-register 
	 		 		 password xxxx 
	 		 	 auto-assign 8001 to 8006 
	  max-dn 50 
	  max-pool 40
	 Router(config-register-global)#auto-assign 8002 to 8006
	 Start DN should not be greater than existing First DN 
	 Router(config-register-global)#auto-assign 8001 to 8005  
	 Stop DN should not be less than existing Last DN
```

The DN assigned to phone using the auto registration feature does not
                              		duplicate a manually configured DN. When the defined DN range includes a
                              		previously registered DN, that DN is skipped as part of the auto registration
                              		process. However, when a previously registered DN deregisters and the
                              		corresponding configuration for the DN and pool are removed, it can be assigned
                              		to a phone registering on Unified CME using auto registration. The assignment
                              		of DN range is done in round robin fashion and the first available free DN is
                              		assigned to the phone that is auto registering with Unified CME.

We recommend that administrators choose different DN ranges for
                                          		  manually configured and auto configured phones.

Template —Administrators are provided the option to create a basic
                              		configuration template that can be applied to all phones registering
                              		automatically on Unified CME. This basic configuration template supports all
                              		the configurations currently supported by the voice register template. It is
                              		mandatory that voice register template is configured with the same template
                              		tag.

```
Router(config)#voice register global
Router(config-register-global)#auto-register
Router(config-voice-auto-register)#template ?
  <1-10>  template tag>
Router(config-voice-auto-register)#template 10
```

All phone configurations such as voice-register-pool and
                              		voice-register-dn that are generated as part of the auto registration process
                              		are persistent configurations. These configurations will be available on the
                              		Unified CME even after an event of router reload.

The CLI commands show voice register pool all and show voice register pool all brief distinctly
                              		mention the registration process for phones as registered or unregistered for
                              		manual registration, and registered* or unregistered* for automatic
                              		registration. However, the registration status for auto-registered phones are
                              		reset in the event of a router reload. Then, phone registration status displays
                              		only as registered or unregistered.

#### Syslog Messages

Unified CME generates Syslog messages as part of the registration feature, when the phone registers and unregisters with the
                                 Cisco Unified CME. Also, based on the DN range configured, the administrator gets syslog message providing updates on the
                                 registration status of assigned DNs. The syslog messages that provide updates are generated at two instances; at 80% utilization
                                 of available DNs, and at 100% utilization of DNs.

From Unified CME 12.3 Release (Cisco IOS XE Fuji Release 16.9.1), the following changes are introduced to Syslog messages
                                 printed in Unified CME:

Syslog messages are printed for successful endpoint assignment and unassignment using Extension Assigner (EA) feature.

The device type information in the registration and unregistration syslog messages of Unified CME is printed as DeviceType:Phone-Type

A sample output for Unified CME 12.3 syslog changes is as follows:

```
Successful extension assignment:
=====================
000246: *Apr 23 03:58:46.238: %EXTASSIGNER-6-ASSIGNED: Extension assignment successful for phone:SEP382056447710. New pool(2). Old pool(1).     

Successful extension un-assignment:
=======================
000407: *May  3 07:13:08.876: %EXTASSIGNER-6-UNASSIGNED: Extension unassignment successful for phone:SEP382056447710. Unassigned pool(2).                                    
                                

Phone un-registration:
==============
000300: *Apr 23 03:58:55.128: %SIPPHONE-6-UNREGISTER: VOICE REGISTER POOL-1 has unregistered. Name:SEP382056447710  IP:8.55.0.108  DeviceType:Phone-8851

Phone registration:
============
000310: *Apr 23 03:59:08.054: %SIPPHONE-6-REGISTER: VOICE REGISTER POOL-2 has registered. Name:SEP382056447710  IP:8.55.0.108  DeviceType:Phone-8851
```

The Unified CME system generates the following syslog messages as part
                                 		of auto registration.

Syslog message when phone registers with Unified CME:

```
*Mar 28 21:44:08.795 IST: %SIPPHONE-6-REGISTER: VOICE REGISTER POOL-8 has registered. Name:SEP2834A2823843  IP:8.41.20.58 DeviceType:Phone
```

Syslog message at 80% utilization of DN range:

```
*Mar 28 21:42:25.732 IST: %SIPPHONE-6-AUTOREGISTER80: AUTO-REGISTER: 80% of DN range is consumed
```

Syslog message at 100% utilization of DN range:

```
*Mar 28 21:44:03.328 IST: %SIPPHONE-6-AUTOREGISTER100: AUTO-REGISTER: 100% of DN range is consumed
```

Syslog message when phone unregisters with Unified CME:

```
*Mar 28 18:03:41.748 IST: %SIPPHONE-6-UNREGISTER: VOICE REGISTER POOL-6 has unregistered. Name:SEPB000B4BAF3DA  IP:8.41.20.53  DeviceType:Phone
```

### Monitor Mode for Shared Lines

In Cisco CME 3.0 and later versions, monitor mode for shared lines
                              		provides a visible line status indicating whether the line is in-use or not. A
                              		monitor-line lamp is off or unlit only when its line is in the idle call state.
                              		The idle state occurs before a call is made and after a call is completed. For
                              		all other call states, the monitor line lamp is lit. A receptionist who
                              		monitors the line can see that it is in use and can decide not to send
                              		additional calls to that extension, assuming that other transfer and forwarding
                              		options are available, or to report the information to the caller; for example,
                              		“Sorry, that extension is busy, can I take a message?”

In Cisco CME 3.2 and later versions, consultative transfers can occur during Direct Station Select (DSS) for transferring
                              calls to idle monitored lines. The receptionist who transfers a call from a normal line can press the Transfer button and
                              then press the line button of the monitored line, causing the call to be transferred to the phone number of the monitored
                              line. For information about consultative transfer with DSS, see Configure Call Transfer and Forwarding .

In Cisco Unified CME 4.0(1) and later versions, the line button for a
                              		monitored line can be used as a DSS for a call transfer when the monitored line
                              		is idle or in-use, provided that the call transfer can succeed; for example,
                              		when the monitored line is configured for Call Forward Busy or Call Forward No
                              		Answer.

Typically, Cisco Unified CME does not attempt a transfer that causes
                                          		  the caller (transferee) to hear a busy tone. However, the system does not check
                                          		  the state of subsequent target numbers in the call-forward path when the
                                          		  transferred call is transferred more than once. Multiple transfers can occur
                                          		  because a call-forward-busy target is also busy and configured for Call Forward
                                          		  Busy.

In Cisco Unified CME 4.3 and later versions, a receptionist can use the Transfer to Voicemail feature to transfer a caller
                              directly to a voice-mail extension for a monitored line. For configuration information, see Transfer to Voice Mail .

For configuration information for monitor mode, see Create Directory Numbers for SCCP Phones .

Monitor mode is intended for use only in the context of shared lines so that a receptionist can visually monitor the in-use
                              status of several users’ phone extensions; for example, for Busy Lamp Field (BLF) notification. To monitor all lines on an
                              individual phone so that a receptionist can visually monitor the in-use status of that phone, see Watch Mode for Phones .

For BLF monitoring of speed-dial buttons and directory call-lists, see Configure Presence Service .

### Watch Mode for Phones

In Cisco Unified CME 4.1 and later versions, a line button that is
                              		configured for watch mode on one phone provides BLF notification for all lines
                              		on another phone (watched phone) for which watched directory number is the
                              		primary line. Watch mode allows a phone user, such as a receptionist, to
                              		visually monitor the in-use status of an individual phone. A user can use the
                              		line button that has been set in watch mode as a speed-dial to call the first
                              		extension of the watched phone. The watching phone button displays a red light
                              		when the watched phone is unregistered in a DND state or in an offhook state.
                              		Pressing the button when it is not displaying a red light will dial the number
                              		in the same manner it would for a monitor button or the speed-dial button.
                              		Incoming calls on a line button that is in watch mode do not ring and do not
                              		display caller ID or call-waiting caller ID.

The line button for a watched phone can also be used as a DSS for a call
                              		transfer when the watched phone is idle. In this case, the phone user who
                              		transfers a call from a normal line can press the Transfer button and then
                              		press the line button of the watched directory number, causing the call to be
                              		transferred to the phone number associated with the watched directory number.

For configuration information, see Create Directory Numbers for SCCP Phones .

If the watched directory number is a shared line and the shared line is
                              		not idle on any phone with which it is associated, then in the context of watch
                              		mode, the status of the line button indicates that the watched phone is in use.

For best results when monitoring the status of an individual phone based on a watched directory number, the directory number
                              configured for watch mode should not be a shared line. To monitor a shared line so that a receptionist can visually monitor
                              the in-use status of several users’ phone extensions, see Monitor Mode for Shared Lines .

For BLF monitoring of speed-dial buttons and directory call-lists, see Presence Service .

### PSTN FXO Trunk Lines

In Cisco CME 3.2 and later versions, IP phones running SCCP can be
                              		configured to have buttons for dedicated PSTN FXO trunk lines, also known as
                              		FXO lines. FXO lines may be used by companies whose employees require private
                              		PSTN numbers. For example, a salesperson may need a special number that
                              		customers can call without having to go through a main number. When a call
                              		comes in to the direct number, the salesperson knows that the caller is a
                              		customer. In the salesperson’s absence, the customer can leave a voice mail.
                              		FXO lines can use PSTN service provider voice mail: when the line button is
                              		pressed, the line is seized, allowing the user to hear the stutter dial tone
                              		provided by the PSTN to indicate that voice messages are available.

Because FXO lines behave as private lines, users do not have to dial a
                              		prefix, such as 9 or 8, to reach an outside line. To reach phone users within
                              		the company, FXO-line users must dial numbers that use the company's PSTN
                              		number. For calls to non-PSTN destinations, such as local IP phones, a second
                              		directory number must be provisioned.

Calls placed to or received on an FXO line have restricted
                              		Cisco Unified CME services and cannot be transferred by Cisco Unified CME.
                              		However, phone users are able to access hookflash-controlled PSTN services
                              		using the Flash softkey.

In Cisco Unified CME 4.0(1), the following FXO trunk enhancements were
                              		introduced to improve the keyswitch emulation behavior of PSTN lines on phones
                              		running SCCP in a Cisco Unified CME system:

FXO port monitoring—Allows the line button on IP phones to reliably
                                    			 show the status of an FXO port when the port is in use. The status indicator,
                                    			 either a lamp or an icon, depending on the phone model, accurately displays the
                                    			 status of the FXO port during the duration of the call, even after the call is
                                    			 forwarded or transferred. The same FXO port can be monitored by multiple phones
                                    			 using multiple trunk ephone-dns.

Transfer recall—If a transfer-to phone does not answer after a
                                    			 specified timeout, the call is returned to the phone that initiated the
                                    			 transfer and it resumes ringing on the FXO line button. The directory number
                                    			 must be dual-lined.

Transfer-to button optimization—When an FXO call is transferred to a
                                    			 private extension button on another phone, and that phone has a shared line
                                    			 button for the FXO port, after the transfer is committed and the call is
                                    			 answered, the connected call displays on the FXO line button of the transfer-to
                                    			 phone. This frees up the private extension line on the transfer-to phone. The
                                    			 directory number n must be dual-line.

Dual-line ephone-dns— Directory numbers for FXO lines can now be
                                    			 configured for dual-line to support the FXO monitoring, transfer recall, and
                                    			 transfer-to button optimization features.

For configuration information, see Configure Trunk Lines for a Key System on SCCP Phone .

### Codecs for Cisco Unified CME Phones

In Cisco CME 3.4, support for connecting and provisioning SIP phones was added. The default codec of the POTS dial peer for
                              an SCCP phone is G.711 and the default codec of a VoIP dial peer for a SIP phone is G.729. If neither the SCCP phone nor the
                              SIP phone in Cisco Unified CME is specifically configured to change the codec, calls between the two phones on the same router
                              will produce a busy signal caused by the mismatched default codecs. To avoid codec mismatch, specify the codec for individual
                              IP phones in Cisco Unified CME. Modify the configuration for either SIP or SCCP phones to ensure that the codec for all phones
                              match. Do not modify the configuration for both SIP and SCCP phones. For configuration information, see Configure Codecs of Individual Phones for Calls Between Local Phones .

In Cisco Unified CME 4.3, support for G.722-64K and the Internet Low Bit
                              		Rate Codec (iLBC) was added. This enables Cisco Unified CME to support the same
                              		codecs that are used in newer Cisco Unified IP phones, mobile wireless
                              		networks, and internet telephony without transcoding. This feature provides
                              		support for the following:

iLBC and G.722-capable SIP and SCCP IP phones in Cisco Unified CME.

iLBC-capable SCCP analog endpoints and remote phones in
                                    			 Cisco Unified CME.

Conferencing support for G.722 and ILBC.

Supplementary services, such as transfer, call forward, MOH, support
                                    			 for G.722 and iLBC, including any supplementary services that require
                                    			 transcoding between G.722 and any other codec.

Transcoding for G.722 and iLBC, including G.722 to G.711 and G.722
                                    			 to any other codec.

With the introduction of G.722 and iLBC codecs, there can be a disparity
                              		between codec capabilities of different phones and different firmware versions
                              		on same phone type. For example, when a H.323 call is established, the codec is
                              		negotiated based on the dial-peer codec and the assumption is that the codecs
                              		supported on H.323 side are supported by the phones. This assumption is not
                              		valid after G.722 and ILBC codec are introduced in your network. If the phones
                              		do not support the codecs on the H.323 side, a transcoder is required. To avoid
                              		transcoding in this situation, configure incoming dial-peers so that G.722 and
                              		iLBC codecs are not used for calls to phones that are not capable of supporting
                              		these codecs. Instead, configure these phones for G.729 or G.711. Also, when
                              		configuring shared directory numbers, ensure that phones with the same codec
                              		capabilities are connected to the shared directory number.

#### G.722-64K

Traditional PSTN telephony codecs, including G.711 and G.729, are
                                 		  classified as narrowband codecs because they encode audio signals in a narrow
                                 		  audio bandwidth, giving telephone calls a characteristic “tinny” sound.
                                 		  Wideband codecs, such as G.722, provide a superior voice experience because
                                 		  wideband frequency response is 200 Hz to 7 kHz compared to narrowband frequency
                                 		  response of 300 Hz to 3.4 kHz. At 64 kbps, the G.722 codec offers conferencing
                                 		  performance and good music quality.

A wideband handset for certain Cisco Unified IP phones, such as the Cisco Unified IP Phone 7906G, 7911G, 7941G-GE, 7942G,
                                 7945G, 7961G-GE, 7962G, 7965G, and 7975G, take advantage of the higher voice quality provided by wideband codecs to enhance
                                 end-user experience with high-fidelity wideband audio. When users use a headset that supports wideband, they experience improved
                                 audio sensitivity when the wideband setting on their phones is enabled. You can configure phone-user access to the wideband
                                 headset setting on IP phones by setting the appropriate VendorConfig parameters in the phone’s configuration file. For configuration
                                 information, see Modify Cisco Unified IP Phone Options .

If the system is not configured for a wideband codec, phone users may
                                 		  not detect any additional audio sensitivity, even when they are using a
                                 		  wideband headset.

You can configure the G.722-64K codec at a system-level for all calls through Cisco Unified CME. For configuration information,
                                 see Modify the Global Codec . To configure individual phones and avoid codec mismatch for calls between local phones, see Configure Codecs of Individual Phones for Calls Between Local Phones .

#### iLBC codec

Internet Low Bit Rate Codec (iLBC) enables graceful speech quality
                                 		  degradation in a network where frames get lost. Consider iLBC suitable for
                                 		  real-time communications, such as telephony and video conferencing, streaming
                                 		  audio, archival, and messaging. This codec is widely used by internet telephony
                                 		  softphones.The SIP, SCCP, and MGCP call protocols support use of the iLBC as an
                                 		  audio codec. iLBC provides better voice quality than G.729 but less than G.711.
                                 		  Supporting codecs that have standardized use in other networks, such as iLBC,
                                 		  enables end-to-end IP calls without the need for transcoding.

To configure individual SIP or SCCP phones, including analog endpoints in Cisco Unified CME, and avoid codec mismatch for
                                 calls between local phones, see Configure Codecs of Individual Phones for Calls Between Local Phones .

### Analog
                           	 Phones

Cisco Unified CME
                              		supports analog phones and fax machines using Cisco Analog Telephone Adaptors
                              		(ATAs) or FXS ports in SCCP, H.323 mode, and fax pass-through mode. The FXS
                              		ports used for analog phones or fax can be on a Cisco Unified CME router,
                              		Cisco VG224 voice gateway, or integrated services router (ISR).

This section
                              		provides information on the following topics:

#### Cisco ATAs in SCCP Mode

You can configure the Cisco ATA 186 or Cisco ATA 188 to cost-effectively support analog phones using SCCP in Cisco IOS Release 12.2(11)T
                                 and later versions. Each Cisco ATA enables two analog phones to function as IP phones. For configuration information, see Configure Cisco ATA Support in SCCP Mode .

#### Cisco ATAs in SIP Mode

You can configure the Cisco ATA 187, Cisco ATA 190 or Cisco ATA 191 to cost-effectively support analog phones and FAX using
                                 SIP for Unified CME. The support for Cisco ATA 191 is introduced from Unified CME 12.5 (Cisco IOS XE Gibralter 16.10.1a) Release.
                                 Each Cisco ATA enables two analog phones to function as IP phones. For configuration information, see Configure Cisco ATA Support in SIP Mode .

The following are some of the known restrictions for Cisco ATA 191 on Unified CME:

If both ports of a Cisco ATA 191 are configured as shared line, then a call put on hold on one port cannot be resumed at the
                                       other port.

For Unified CME, a call put on hold on Unified SIP IP Phone cannot be resumed from a Cisco ATA 191.

You cannot configure the same shared line DN on both ports of the Cisco ATA 191. On configuring the same shared line DN on
                                       both the lines of the Cisco ATA 191, second line does not get registered.

##### Cisco ATA 191 on Unified CME

The ATA 191 analog telephone adapter is a telephony-device-to-Ethernet adapter that allows regular analog phones to operate
                                    on IP-based telephony networks. The ATA 191 supports two voice ports, each with an independent phone number. The ATA 191 also
                                    has an RJ-45 10/100BASE-T data port.

Unified CME 12.5 and later release provide native support for Cisco ATA 191. The SIP protocol is supported on Cisco ATA 191.

The ATA 191 supports two lines, but has only a single MAC address. Hence, you must use a shifted MAC address to configure
                                    the  second line on ATA 191. A sample configuration for Line 1 and Line 2 for an ATA 191 is as follows:

```
Line 1 confguration: voice register dn 15
    number 8015
voice register pool 15
    id mac DCEB.941C.F33D
    type ATA-191
    number 1 dn 15
    username abcd password xxxx
    codec g711ulaw Line 2 confguration: voice register dn 16
    number 8016
    voice register pool 16
    id mac EB94.1CF3.3D01
    type ATA-191
    number 1 dn 16
    username uvwx password xxxx
    codec g711ulaw
```

Left shift the MAC address by two places, and append the two removed digits at the end with 01 to define the shifted MAC address.
                                                For example, the MAC address DCEB.941C.F33D is modified to get the shifted MAC address, EB94.1CF3.3D01 .

##### Feature Support for Cisco ATA 191

The Cisco ATA 191 supports the following features on Unified CME:

Hold or Resume—Hold or Resume is invoked using a hookflash for Cisco ATA 191 on Unified CME. For more information on the feature,
                                          see Put a Call on Hold on Your Analog Phone .

Consult or Semi Consult Transfer—To Transfer a call using Cisco ATAT 191 on Unified CME, you need to use hookflash along with
                                          FAC. For information on the feature, see Transfer a Call from Your Analog Phone .

Call Waiting—Call Waiting calls are answered using a hookflash for Cisco ATA 191 on Unified CME. For more information on the
                                          feature, see Answer Call Waiting on Your Analog Phone .

MeetMe Conference—To host a MeetMe Conference on Cisco ATAT 191 on Unified CME, you need to use hookflash along with FAC.
                                          For information on how to invoke the feature, see Host a Meet Me Conference on Your Analog Phone .

Call Forward (All, Busy, No Answer)—Call Forward is invoked using a hookflash for Cisco ATA 191 on Unified CME. For more information
                                          on the feature, see Forward Your Analog Phone Calls to Another Number .

cBarge—cBarge is invoked using a hookflash for Cisco ATA 191 on Unified CME. For more information on the feature, see Call Features and Star Codes for Analog Phones .

Built-in Bridge Conference (BIB)—BIB is invoked using a hookflash for Cisco ATA 191 on Unified CME. For more information on
                                          the feature, see Make a Conference Call from Your Analog Phone .

Call Park—Call Park is invoked using a FAC Code for Cisco ATA 191 on Unified CME. To park a call on Cisco ATA 191 on Unified
                                          CME, you need to transfer the call to the FAC code, **6. For more information, see Call Park .

Call Park Pickup and G-Pickup—To pick up a parked call, dial the park-slot number.

Voice Mail—For Voice Mail support on Cisco ATA 191, you need to go offhook, and dial the voice mail number configured on Unified
                                          CME to access the IVR options.

Fax Transmission (with T.38, Passthrough)—For Fax trasmission to work with Cisco ATA 191 on Unified CME, you need to configure
                                          the CLI command service phone faxMode 0 under telephony-service configuration mode. For information on the feature, see Send and Receive Fax Calls .

Shared Line/Mixed Shared Line—For information on the feature, see Shared Lines on Your Analog Phone .

KPML Dialing—For KPML Dialing support on Cisco ATA 191, you need to go offhook and dial the number.

TCP/UDP Registration

Extension Assigner

Auto Registration

DTMF

Caller ID Blocking

Music On Hold (MOH)

Upgrade or Downgrade Firmware

Redial

WebAccess

SSH

MWI—Cisco ATA 191 plays a stuttered tone instead of MWI

###### Feature Support Restriction

The following are the known feature restrictions for Cisco ATA 191 on Unified CME:

Barge—Cisco ATA 191 cannot barge into an active shared line call (phone limitation). However, non-ATA phones can barge into
                                             Cisco ATA's shared line call.

Hardware Conference is not supported.

Do Not Disturb

Span to PC Port

Speed Dial—For Cisco ATA 191, Abbreviated Dial is supported as Speed Dial. Unified CME does not support Abbreviated Dial.

Secondary CME

Call Waiting with Caller-ID—For Cisco ATA 191, the phone Caller-ID does not display any call waiting notification (only call
                                             waiting tone is supported).

Localization

Shared Line

Both the ports of a Cisco ATA191 cannot be configured with the same Shared Line DN.

Remote Resume is not supported for a Shared Line call placed on hold.

#### FXS Ports in SCCP Mode

FXS ports on Cisco VG224 Voice Gateways and Cisco 2800 Series and Cisco 3800 Series ISRs can be configured for SCCP supplementary
                                 features. For information about using SCCP supplementary features on analog FXS ports on a Cisco IOS gateway under the control
                                 of a Cisco Unified CME router, see Supplementary Services Features for FXS Ports on Cisco IOS Voice Gateways Configuration Guide .

#### FXS Ports in H.323 Mode

FXS ports on platforms that cannot enable SCCP supplementary features
                                 		can use H.323 mode to support call waiting, caller ID, hookflash transfer,
                                 		modem pass-through, fax (T.38, Cisco fax relay, and pass-through), and PLAR.
                                 		These features are provisioned as Cisco IOS voice features and not as
                                 		Cisco Unified CME features.

When using Cisco Unified CME, you can configure FXS ports in H.323
                                             		  mode for call waiting or hookflash transfer, but not both at the same time.

#### Fax Support

Cisco Unified CME 4.0 introduced the use of G.711 fax pass-through for SCCP on the Cisco VG224 voice gateway and Cisco ATA.
                                 In Cisco Unified CME 4.0(3) and later versions, fax relay using the Cisco-proprietary fax protocol is the only supported fax
                                 option for SCCP-controlled FXS ports on the Cisco VG224 and integrated service routers. For more information on fax relay,
                                 see Fax Relay .

##### Cisco ATA-187

Cisco Unified CME 9.0 and later versions provide voice and fax support
                                    		on Cisco ATA-187.

Cisco ATA-187 is a SIP-based analog telephone adaptor that turns
                                    		traditional telephone devices into IP devices. Cisco ATA-187 can connect with a
                                    		regular analog FXS phone or fax machine on one end, while the other end is an
                                    		IP side that uses SIP for signaling and registers to Cisco Unified CME as a
                                    		Cisco Unified SIP IP phone.

Cisco ATA-187 functions as a Cisco Unified SIP IP phone that supports
                                    		T.38 fax relay and fax pass-through, enabling the real-time transmission of fax
                                    		over IP networks. The fax rate is from 7.2 to 14.4 kbps.

For information on how to configure voice and fax support on Cisco ATA-187, see Configure Voice and T.38 Fax Relay on Cisco ATA-187 .

For information on the features supported in Cisco ATA-187, see Phone Feature Support Guide for Unified CME, Unified SRST, Unified E-SRST, and Unified Secure SRST .

For more information on Cisco ATA-187, see Cisco ATA 187 Analog Telephone Adaptor Administration Guide for SIP .

#### Cisco VG202, VG204, and VG224 Auto Configuration

The Auto Configuration feature in Cisco Unified CME 7.1 and later
                                 		versions allows you to automatically configure the Cisco VG202, VG204, and
                                 		VG224 Analog Phone Gateway. You can configure basic voice gateway information
                                 		in Cisco Unified CME, which then generates XML configuration files for the
                                 		gateway and saves the files to either the default location in system:/its/ or
                                 		to a location you define in system memory, flash memory, or an external TFTP
                                 		server. When the voice gateway powers up, it downloads the configuration files
                                 		from Cisco Unified CME and based on the information in the files, the voice
                                 		gateway provisions its analog voice ports and creates the corresponding dial
                                 		peers.

Using this Auto Configuration feature with the existing Auto Assign
                                 		feature allows you to quickly set up analog phones to make basic calls. After
                                 		the voice gateway is properly configured and it downloads its XML configuration
                                 		files from Cisco Unified CME, the SCCP telephony control (STC) application
                                 		registers each configured voice port to Cisco Unified CME.

If you enable the Auto Assign feature, the gateway automatically assigns
                                 		the next available directory number from the pool set by the auto assign command, binds that number to the
                                 		requesting voice port, and creates an ephone entry associated with the voice
                                 		port. The MAC address for the ephone entry is calculated based on the MAC
                                 		address of the gateway and the port number. You can manually assign a directory
                                 		number to each of the voice ports by creating the ephone-dn and corresponding
                                 		ephone entry.

You can initiate a reset or restart of the analog endpoints from
                                 		Cisco Unified CME, which triggers the autoconfiguration process. The voice
                                 		gateway downloads its configuration files from Cisco Unified CME and applies
                                 		the new changes.

For configuration information, see Auto-Configuration for Cisco VG202, VG204, and VG224 .

### Internet Protocol - Secure Telephone Equipment Support

Cisco Unified CME 8.0 adds support for a new secure endpoint, Internet
                              		Protocol - Secure Telephone Equipment (IP-STE). IP-STE is a standalone, V.150.1
                              		capable device which functions like a 7960 phone with secure communication
                              		capability. IP-STE has native state signaling events (SSE / SPRT) support and
                              		supports SCCP protocol. IP-STE uses the device ID 30035 when registering to a
                              		SCCP server. However, only V.150.1 modem relay is implemented in an IP-STE
                              		stack and V150.1 modem passthrough is not supported. Therefore, the response to
                              		capability query from Cisco Unified CME only includes
                              		media_payload_XV150_MR_711U and media_payload_xv150_MR_729A.

For configuration information, see Configure Secure IP Phone (IP-STE) on SCCP Phone .

The following support is added for IP-STE endpoints:

The IP-STE endpoint allows secure communication between
                                    			 gateway-connected legacy analog STE/STU devices and IP STE devices using
                                    			 existing STE devices in voice networks.

Secure voice and secure data modes from STE/STU devices connected to
                                    			 Cisco IOS gateway foreign exchange station (FXS) and BRI ports to an IP-STE.

Support for the state signaling events (SSE) protocol, allowing for
                                    			 modem signaling end-to-end and VoIP to modem over IP (MoIP) transition and
                                    			 operation.

Interoperation between line-side and trunk-side gateways and
                                    			 Cisco Unified CME to determine codec support and V.150.1 negotiation. You can
                                    			 configure gateway-attached devices to support either modem relay, modem
                                    			 pass-through, both modem transport methods, or neither method.

#### Secure Communications Between STU, STE, and IP-STE

Secure Telephone Equipment (STE) and Secure Telephone Units (STUs)
                                 		encrypt voice and data streams with government proprietary algorithms (Type-1
                                 		encryption). To provide support for the legacy STEs and STUs and next
                                 		generation IP Secure Telephone Equipment (IP-STE), voice gateways must be able
                                 		to support voice and data in secure mode within the IP network and be able to
                                 		pass calls within and also to and from government voice networks.

In earlier versions of Cisco Unified CME, Cisco IOS gateways supported
                                 		secure voice and data communication between legacy STE and STU devices using
                                 		modem pass-through method. Cisco Unified CME 8.0 and later versions control the
                                 		secure endpoints by implementing a subset of v.150.1 modem relay protocol and
                                 		ensures secure communications between IP-STE endpoints and STE/STU endpoints.
                                 		This allows Cisco Unified CME SCCP controlled secure endpoints to communicate
                                 		with the IP-STE or legacy endpoints in secure mode.

#### SCCP Media Control
                              	 for Secure Mode

IP-STE endpoints use
                                 		the V.150.1 modem relay transport method using Future Narrow Band Digital
                                 		Terminal (FNBDT) signaling over a V.32 or V.34 data pump for secure
                                 		communication with other legacy STE endpoints. However, IP-STE endpoints cannot
                                 		communicate with STU endpoints because STU endpoints use the modem pass-through
                                 		method using a proprietary data pump and do not support the FNBDT signaling.

Secure communication
                                 		between IP-STE endpoints and legacy STE endpoints support the following
                                 		encryption-capable endpoints:

STE—Specialized
                                       			 encryption-capable analog or BRI phones that can communicate over V.150.1 modem
                                       			 relay or over modem pass-through, also known as Voice Band Data (VBD).

IP-STE—Specialized encryption-capable IP phones that communicate
                                       			 only over V.150.1 modem relay.

STU—Specialized
                                       			 encryption-capable analog phones that operate only over NSE-based modem
                                       			 pass-through connections.

Table 1 lists call scenarios between devices along with modem transport methods that
                                 		the IP-STE endpoints use to communicate with STE endpoints.

Device Type

STU

STE

IP-STE

STU

Pass-through

Pass-through

None

STE

Pass-through

Pass-through

Relay

IP-STE

None

Relay

Relay

#### Secure Communication Between STE, STU, and IP-STE Across SIP
                              	 Trunk

The Secure Device Provisioning (SDP) for SIP end-to end negotiation
                                 		includes four proprietary media types for secure communication between
                                 		Cisco Unified CME and SIP trunk. These proprietary VBD or Modem Relay (MR)
                                 		media types can be encoded into media attributes of SDP media lines. VBD
                                 		capabilities are signaled using the SDP extension mechanism and Cisco
                                 		proprietary nomenclature. MR capabilities are signaled through V.150.1. The
                                 		following example shows VBD capabilities. The SDP syntax are based on RFC 2327
                                 		and V.150.1 Appendix E.

```
a=rtpmap:100 X-NSE/8000
a=rtpmap:118 v150fw/8000
a=sqn:0
a=cdsc:1 audio RTP/AVP 118 0 18
a=cdsc: 4 audio udsprt 120
a=cpar: a=sprtmap: 120 v150mr/8000
```

### Remote Teleworker Phones

IP phones or a Cisco IP Communicator can be connected to a Cisco Unified CME system over a WAN to support teleworkers who
                              have offices that are remote from the Cisco Unified CME router. The maximum number of remote phones that can be supported
                              is determined by the available bandwidth.

IP addressing is a determining factor in the most critical aspect of remote teleworker phone design. The following two scenarios
                              represent the most common designs, the second one is the most common for small and medium businesses:

Remote site IP phones and the hub Cisco Unified CME router use globally routable IP addresses.

Remote site IP phones use NAT with unroutable private IP addresses and the hub Cisco Unified CME router uses a globally routable
                                    address (see Remote Site IP Phones Using NAT ). This scenario results in one-way audio unless you use one of the following workarounds:

Configure static NAT mapping on the remote site router (for example, a Cisco 831 Ethernet Broadband Router) to convert between
                                          a private address and a globally routable address. This solution uses fewer Cisco Unified CME resources, but voice is unencryped
                                          across the WAN.

Configure an IPsec VPN tunnel between the remote site router (For example, a Cisco 831 Ethernet Broadband Router) and the
                                          Cisco Unified CME router. This solution requires Advanced IP Services or higher image on the Cisco Unified CME router if this
                                          router is used to terminate the VPN tunnel. Voice will be encrypted across the WAN. This method will also work with the Cisco VPN
                                          client on a PC to support a Cisco IP Communicator.

#### Media Termination Point for Remote Phones

Media termination point (MTP) configuration is used to ensure that
                                 		Real-Time Transport Protocol (RTP) media packets from remote phones always
                                 		transit through the Cisco Unified CME router. Without the MTP feature, a phone
                                 		that is connected in a call with another phone in the same Cisco Unified CME
                                 		system sends its media packets directly to the other phone, without the packets
                                 		going through the Cisco Unified CME router. MTP forces the packets to be
                                 		sourced from the Cisco Unified CME router.

When this configuration is used to instruct a phone to always send its
                                 		media packets to the Cisco Unified CME router, the router acts as an MTP or
                                 		proxy and forwards the packets to the destination phone. If a firewall is
                                 		present, it can be configured to pass the RTP packets because the router uses a
                                 		specified UDP port for media packets. In this way, RTP packets from remote IP
                                 		phones can be delivered to IP phones on the same system though they must pass
                                 		through a firewall.

You must use the mtp command to explicitly enable MTP for each
                                 		remote phone that sends media packets to Cisco Unified CME.

One factor to consider is whether you are using multicast music on hold
                                 		(MOH) in your system. Multicast packets generally cannot be forwarded to phones
                                 		that are reached over a WAN. The multicast MOH feature checks to see if MTP is
                                 		enabled for a phone and if it is, MOH is not sent to that phone. If you have a
                                 		WAN configuration that can forward multicast packets and you can allow RTP
                                 		packets through your firewall, you can decide not to use MTP.

For configuration information, see Enable Remote Phone .

#### G.729r8 Codec on Remote Phones

You can select the G.729r8 codec on a remote IP phone to help save network bandwidth. The default codec is G.711 mu-law. If
                                 you use the codec g729r8 command without the dspfarm-assist keyword, the use of the G.729 codec is preserved only for calls between two phones on the Cisco Unified CME router (such
                                 as between an IP phone and another IP phone or between an IP phone and an FXS analog phone). The codec g729r8 command has no effect on a call directed through a VoIP dial peer unless the dspfarm-assist keyword is also used.

For configuration information, see Enable Remote Phone .

For information about transcoding behavior when using the G.729r8 codec, see Transcoding When a Remote Phone Uses G.729r8 .

### Busy Trigger and Channel Huntstop for SIP Phones

Cisco Unified CME 7.1 introduced busy trigger and huntstop channel
                              		support for SIP phones, such as the Cisco Unified IP Phone 7941G, 7941GE,
                              		7942G, 7945G, 7961G, 7961GE, 7962G, 7965G, 7970G, 7971GE, 7975G, and 7985. For
                              		these SIP phones, the number of channels supported is limited by the amount of
                              		memory on the phone. To prevent incoming calls from overloading the phone, you
                              		can configure a busy trigger and a channel huntstop for the directory numbers
                              		on the phone.

The Channel Huntstop feature limits the number of channels available for
                              		incoming calls to a directory number. If the number of incoming calls reaches
                              		the configured limit, Cisco Unified CME does not present the next incoming call
                              		to the directory number. This reserves the remaining channels for outgoing
                              		calls or for features, such as call transfer and conferencing.

The Busy Trigger feature limits the calls to a directory number by
                              		triggering a busy response. After the number of active calls, both incoming and
                              		outgoing, reaches the configured limit, Cisco Unified CME forwards the next
                              		incoming call to the Call Forward Busy destination or rejects the call with a
                              		busy tone if Call Forward Busy is not configured.

The busy-trigger limit applies to all directory numbers on a phone. If a
                              		directory number is shared among multiple SIP phones, Cisco Unified CME
                              		presents incoming calls to those phones that have not reached their
                              		busy-trigger limit. Cisco Unified CME initiates the busy trigger for an
                              		incoming call only if all the phones sharing the directory number exceed their
                              		limit.

For configuration information, see Create Directory Numbers for SIP Phones and Assign Directory Numbers to SIP Phones .

### Multiple Calls Per Line

Cisco Unified CME 9.0 provides support for the Multiple Calls Per Line
                              		(MCPL) feature on Cisco Unified 6921, 6941, 6945, and 6961 SIP IP phones and
                              		Cisco Unified 8941 and 8945 SCCP and SIP IP phones.

Before Cisco Unified CME 9.0, the maximum number of calls supported for
                              		every directory number (DN) on Cisco Unified 8941 and 8945 SCCP IP phones was
                              		restricted to two.

With Cisco Unified CME 9.0, the MCPL feature overcomes the limitation on
                              		the maximum number of calls per line.

In Cisco Unified CME 9.0, the MCPL feature is not supported on Cisco
                              		Unified 6921, 6941, 6945, and 6961 SCCP IP phones.

#### Cisco Unified 8941 and 8945 SCCP IP Phones

Before Cisco Unified CME 9.0, Cisco Unified 8941 and 8945 SCCP IP phones
                                 		only supported two incoming calls per line and a third channel was reserved for
                                 		call transfers or conference calls. These phones were also hardcoded with ephone-dn octo-line , huntstop-channel 2, max-calls
                                       			 -per-button 3, and busy-trigger-per-button 2.

In Cisco Unified CME 9.0, you can configure the ephone-dn dn-tag [ dual-line | octo-line ] in global configuration mode
                                 		and the max-calls-per-button and busy-trigger-per-button commands in ephone or
                                 		ephone-template configuration mode for Cisco Unified 8941 and 8945 SCCP IP
                                 		phones to configure a DN and enable the number of calls per DN, set the maximum
                                 		number of calls allowed on an octo-line DN, and set the maximum number of calls
                                 		allowed on an octo-line DN before activating a busy tone.

For configuration information, see Configure the Maximum Number of Calls on SCCP Phone .

#### Cisco Unified 6921, 6941, 6945, 6961, 8941, and 8945 SIP IP
                              	 Phones

In Cisco Unified CME 9.0, the default values for the busy-trigger-per-button command is 1 for the
                                 		Cisco Unified 6921, 6941, 6945, and 6961 SIP IP phones and 2 for the Cisco
                                 		Unified 8941 and 8945 SIP IP phones.

You can configure the maximum number of calls before a phone receives a
                                 		busy tone. For example, if you configure busy-trigger-per-button 2 in voice register
                                 		pool configuration mode for a Cisco Unified 6921, 6941, 6945, or 6961 SIP IP
                                 		phone, the third incoming call to the phone receives a busy tone.

For information on the Busy Trigger feature on Cisco Unified SIP IP phones, see Busy Trigger and Channel Huntstop for SIP Phones .

For configuration information, see Configure the Busy Trigger Limit on SIP Phone .

### Digit Collection
                           	 on SIP Phones

Digit strings dialed
                              		by phone users must be collected and matched against predefined patterns to
                              		place calls to the destination corresponding to the user's input. Before
                              		Cisco Unified CME 4.1, SIP phone users had to press the DIAL softkey or # key
                              		or wait for the interdigit-timeout to trigger call processing. In
                              		Cisco Unified CME 4.1 and later versions, two methods of collecting and
                              		matching digits are supported for SIP phones, depending on the model of phone:

#### Key Press Markup Language Digit Collection

Key Press Markup Language (KPML) uses SIP SUBSCRIBE and NOTIFY methods
                                 		to report user input digit by digit. Each digit dialed by the phone user
                                 		generates its own signaling message to Cisco Unified CME, which performs
                                 		pattern recognition by matching a destination pattern to a dial peer as it
                                 		collects the dialed digits. This process of relaying each digit immediately is
                                 		similar to the process used by SCCP phones. It eliminates the need for the user
                                 		to press the Dial softkey or wait for the interdigit timeout before the digits
                                 		are sent to Cisco Unified CME for processing.

KPML is supported on Cisco Unified IP Phones 7911G, 7941G, 7941GE, 7961G, 7961GE, 7970G, and 7971GE. For configuration information,
                                 see Enable KPML on a SIP Phone .

#### SIP Dial Plans

A dial plan is a set of dial patterns that SIP phones use to determine
                                 		when digit collection is complete after a user goes off-hook and dials a
                                 		destination number. Dial plans allow SIP phones to perform local digit
                                 		collection and recognize dial patterns as user input is collected. After a
                                 		pattern is recognized, the SIP phone sends an INVITE message to
                                 		Cisco Unified CME to initiate the call to the number matching the user's input.
                                 		All of the digits entered by the user are presented as a block to
                                 		Cisco Unified CME for processing. Because digit collection is done by the
                                 		phone, dial plans reduce signaling messages overhead compared to KPML digit
                                 		collection.

SIP dial plans eliminate the need for a user to press the Dial softkey
                                 		or # key or to wait for the interdigit timeout to trigger an outgoing INVITE.
                                 		You configure a SIP dial plan and associate the dial plan with a SIP phone. The
                                 		dial plan is downloaded to the phone in the configuration file.

You can configure SIP dial plans and associate them with the following
                                 		SIP phones:

Cisco Unified IP Phones 7911G, 7941G, 7941GE, 7961G, 7961GE, 7970G,
                                       			 and 7971GE—These phones use dial plans and support KPML. If both a dial plan
                                       			 and KPML are enabled, the dial plan has priority.

If a matching dial plan is not found and KPML is disabled, the user
                                       			 must wait for the interdigit timeout before the SIP NOTIFY message is sent to
                                       			 Cisco Unified CME. Unlike other SIP phones, these phones do not have a Dial
                                       			 softkey to indicate the end of dialing, except when on-hook dialing is used. In
                                       			 this case, the user can press the Dial softkey at any time to send all the
                                       			 dialed digits to Cisco Unified CME.

Cisco Unified IP Phones 7905, 7912, 7940, and 7960—These phones use
                                       			 dial plans and do not support KPML. If you do not configure a SIP dial plan for
                                       			 these phones, or if the dialed digits do not match a dial plan, the user must
                                       			 press the Dial softkey or wait for the interdigit timeout before digits are
                                       			 sent to Cisco Unified CME.

When you reset a phone, the phone requests its configuration files from
                                 		the TFTP server, which builds the appropriate configuration files depending on
                                 		the type of phone.

Cisco Unified IP Phones 7905 and 7912—The dial plan is a field in
                                       			 their configuration files.

Cisco Unified IP Phones 7911G, 7940, 7941G, 7941GE, 7960, 7961G,
                                       			 7961GE, 7970G, and 7971GE—The dial plan is a separate XML file that is pointed
                                       			 to from the normal configuration file.

For configuration information for Cisco Unified CME, see Configure Dial Plans for SIP Phones .

### Session Transport
                           	 Protocol for SIP Phones

In Cisco Unified CME
                              		4.1 and later versions, you can select TCP as the transport protocol for
                              		connecting supported SIP phones to Cisco Unified CME. Previously only UDP was
                              		supported. TCP is selected for individual SIP phones by using the session-transport command in voice register pool
                              		or voice register template configuration mode. For configuration information,
                              		see Select Session-Transport Protocol for a SIP Phone .

### Real-Time Transport Protocol Call Information Display
                           	 Enhancement

Before Cisco Unified CME 8.8, active RTP call information on ephone call
                              		legs were determined only by parsing the show ephone registered or show ephone offhook command output. The show voip rtp connections command showed active
                              		call information in the system but it did not apply to ephone call legs. In
                              		Cisco Unified CME 8.8 and later versions, you can display information on active
                              		RTP calls, including the ephone tag number of the phone with an active call,
                              		the channel of the ephone-dn, and the caller and called party’s numbers for the
                              		connection for both local and remote endpoints, using the show ephone rtp connections command. The output from this command
                              		provides an overview of all the connections in the system, narrowing the
                              		criteria for debugging pulse code modulation and Cisco Unified CME packets
                              		without a sniffer.

When an ephone to non-ephone call is made, information on the
                                          		  non-ephone does not appear in a show ephone rtp connections command output.
                                          		  To display the non-ephone call information, use the show voip rtp connections command.

The following sample output shows all the connected ephones in the Cisco
                              		Unified CME system. The sample output shows five active ephone connections with
                              		one of the phones having the dspfarm-assist keyword configured to transcode
                              		the code on the local leg to the indicated codec. The output also shows four
                              		ephone-to-ephone calls, represented in the CallID columns of both the RTP
                              		connection source and RTP connection destination by zero values.

Normally, a phone can have only one active connection but in the
                              		presence of a whisper intercom call, a phone can have two. In the sample
                              		output, ephone-40 has two active calls: it is receiving both a normal call and
                              		a whisper intercom call. The whisper intercom call is being sent by ephone-6,
                              		which has an invalid LocalIP of 0.0.0.0. The invalid LocalIP indicates that it
                              		does not receive RTP audio because it only has a one-way voice connection to
                              		the whisper intercom call recipient.

```
Router# show ephone rtp connections Ephone RTP active connections :
Ephone    Line  DN Chan  SrcCallID  DstCallID Codec (xcoded?)
    SrcNum DstNum  LocalIP               RemoteIP
ephone-5     1   5    1         15         14 G729 (Y)
    1005  1102  [192.168.1.100]:23192  [192.168.1.1]:2000
ephone-6     2  35    1          0          0       G711Ulaw64k (N) 
    1035  1036  [0.0.0.0]:0  [192.168.1.81]:21256
ephone-40    1 140    1          0          0       G711Ulaw64k (N)
    1140  1141  [192.168.1.81]:21244  [192.168.1.70]:20664
ephone-40    2  36    1          0          0       G711Ulaw64k (N)
    1035  1036  [192.168.1.81]:21256  [192.168.1.1]:2000
ephone-41    1 141    1          0          0       G711Ulaw64k (N)
    1140  1141  [192.168.1.70]:20664  [192.168.1.81]:21244 
Found 5 active ephone RTP connections
```

### Ephone-Type Configuration

In Cisco Unified CME 4.3 and later versions, you can dynamically add a
                              		new phone type to your configuration without upgrading your Cisco IOS software.
                              		New phone models that do not introduce new features can easily be added to your
                              		configuration without requiring a software upgrade.

The ephone-type configuration template is a set of commands that
                              		describe the features supported by a type of phone, such as the particular
                              		phone type's device ID, number of buttons, and security support. Other
                              		phone-related settings under telephony-service, ephone-template, and ephone
                              		configuration mode can override the features set within the ephone-type
                              		template. For example, an ephone-type template can specify that a particular
                              		phone type supports security and another configuration setting can disable this
                              		feature. However, if an ephone-type template specifies that this phone does not
                              		support security, the other configuration cannot enable support for the
                              		security feature.

Cisco Unified CME uses the ephone-type template to generate XML files to
                              		provision the phone. System-defined phone types continue to be supported
                              		without using the ephone-type configuration. Cisco Unified CME checks the
                              		ephone-type against the system-defined phone types. If there is conflict with
                              		the phone type or the device ID, the configuration is rejected.

For configuration information, see Configure Ephone-Type Templates for SCCP Phones .

### 7926G Wireless
                           	 SCCP IP Phone Support

Cisco Unified CME
                              		8.6 adds support for the Cisco Unified 7926G Wireless SCCP IP phone. The 7926G
                              		wireless phone is phone similar to the 7925 wireless phone with a 2D barcode
                              		and EA15 module attached. The 7926G wireless phone is capable of scanning
                              		functionality. For more details on phone features and functionality, see Cisco Unified IP Phone 7900
                                 		  Series User Guide .

Cisco Unified CME
                              		8.6 supports the scanning function on the 7926G SCCP wireless phone using the
                              		ephone built-in device type. Table 1 shows supported values for the ephone-type for 7926G wireless phone.

Supported
                                             					 Device

device-id

device-type

num-buttons

max-presentation

Cisco
                                             					 Unified Wireless IP Phone 7926G

577

7926

6

2

To support service
                                 		  provisioning, an XML file is constructed externally and applied to the
                                 		  ephone-template of the phone. To allow the phone to read the external XML file,
                                 		  you are required to create-cnf and download the XML file to the ephone. For
                                 		  more information on configuring PhoneServices XML file, see Configure Phone Services XML File for Cisco Unified Wireless Phone 7926G .

The following is
                                 		  an example of the <phoneServices> XML file:

```
<phoneServices  useHTTPS="true">  
		<provisioning>0</provisioning>  
		<phoneService  type="1" category="0">  
		<name>Missed Calls</name> 
		<url>Application:Cisco/MissedCalls</url>  
		<vendor></vendor>  
		<version></version>  
		</phoneService>  
		<phoneService  type="0" category="1">  
		<displayName>Store Ops</displayName>  
		<name>Store Ops</name>  
		<url>http://1.4.206.105/Midlets/StoreOps.jad?StoreNumber=1777</url>  
		<http://1.4.206.105/Midlets/StoreOps.jad?StoreNumber=1777%3c/url%3e>  
		<http://1.4.206.105/Midlets/StoreOps.jad?StoreNumber=1777%3c/url%3e>  
		<vendor>CiscoSystems</vendor>  
		<version>0.0.82</version>  
		</phoneService>  
		</phoneServices>
```

### Enhanced Line
                           	 Mode

Enhanced Line Mode allows you to use the buttons on both sides of the phone screen to configure Line Keys (DNs), Feature
                              Buttons, or Speed Dial.

In a scenario where you have Line Keys, Feature Button, and Speed Dial configured under voice register pool configuration mode for phones that are supported on Unified CME, the priority is set as follows:

Line Keys

Speed Dial

Feature Button

From Unified CME Release 12.3, support is introduced for Enhanced Line Mode (ELM) on Cisco IP Phone 8800 Series. The support
                              is introduced for all Cisco IP Phone 8800 Series phones, except Cisco Wireless IP Phone 8821, Cisco Unified IP Conference
                              Phone 8831, and Cisco IP Conference Phone 8832. ELM for Unified CME is supported on the Cisco 4000 Series Integrated Services
                              Routers. For Cisco IP Phone 8800 Series, a maximum of 10 phone buttons can be configured for ELM lines.

For ELM on Unified
                              		CME, you need to configure the CLI command service phone lineMode
                                    			 1 under telephony-service configuration mode to enable
                              		Enhanced Line Mode on phones. The Cisco IP Phone 8800 Series configured on
                              		Unified CME uses the vendor config XML body in the CNF file to verify if the
                              		CLI command service phone lineMode
                                    			 1 is added to enable ELM mode. For a sample configuration of ELM
                              		on Unified CME, see Example for Configuring Enhanced Line Mode on Unified CME .

The CLI command service phone lineMode is case-sensitive, and must be entered exactly as mentioned.

You can enable ELM
                              		on Unified CME using the CLI command service phone
                                    			 lineMode as follows:

```
Router(config)#telephony-service
Router(config-telephony)#service phone lineMode ?
  WORD  enter the phone xml file parameter text for the previously entered
        parameter name
Router(config-telephony)#service phone lineMode 1
Router(config-telephony)#create cnf-files
Router(config-telephony)#end
```

Once you enable service phone lineMode 1 under telephony-service for ELM, you need to create profile and restart the phones under voice register global configuration mode to
                              		enable ELM for the Cisco IP Phone 8800 series phones on Unified CME.

```
Router(config)#voice register global
Router(config-register-global)#create profile
Router(config-register-global)#restart
Router(config-register-global)#end
```

#### Feature
                                 		  Support on Enhanced Line Mode

The following features are supported for ELM on Cisco IP Phone 8800 Series:

HLog

DND

Park

Redial

Mobility

Group Pickup

Meet Me

Mobility

Pickup

Privacy

### KEM Support for Cisco Unified SIP IP Phones

For Unified CME 12.3 and prior releases, KEM support is limited to C-KEM and BE-KEM device types. From Unified CME Release
                              12.5, Key Expansion Module (KEM) device types A-KEM (Audio) and V-KEM (Video) are supported for Cisco IP Phone 8800 Series.
                              The support is introduced for both SLM (Session Line Mode) and ELM (Enhanced Line Mode) configuration. You can switch from
                              SLM to ELM mode to use buttons on both sides of the Cisco IP Phone 8800 Series.

The following endpoints are supported as part of Unified CME Release 12.5:

Cisco IP Phone 8851—Supports upto 2 A-KEM Modules.

Cisco IP Phone 8851NR—Supports upto 2 A-KEM Modules

Cisco IP Phone 8861—Supports upto 3 A-KEM Modules.

Cisco IP Phone 8865—Supports upto 3 V-KEM Modules

An A-KEM or V-KEM Module supports a maximum of 28 lines. Hence, the total number of lines on the supported phone types for
                              Unified CME 12.5 are as follows:

Phone Model

Number of KEM Lines Supported

Line Support (With SLM)

Line Support (With ELM)

8851

56 (2*28)

61 (56+5)

66 (56+10)

8851NR

56(2*28)

61 (56+5)

66 (56+10)

8861

84 (3*28)

89 (84+5)

94 (84+10)

8865

84 (3*28)

89 (84+5)

94 (84+10)

V-KEM is supported only with the 8865 phone type. You need to configure CP-8800-Video to support V-KEM with 8865 phones. You need to configure CP-8800-Audio to support A-KEM with the phone types 8851, 8851NR, and 8861. The phone types 8851, 8851NR, and 8861 also support CKEM and
                              BEKEM.

A mixed deployment of KEM Modules is not supported for any phone type. For example, if the phone type 8861 supports three
                                          KEM modules, then all three KEM modules have to be either CKEM, BEKEM, or CP-8800-Audio.

To enable A-KEM or V-KEM on Unified CME, you need to configure the KEM option for the phone type under voice register pool configuration mode for Unified CME 12.5 and later releases:

```
Router(config)# enable
Router(config)# configure terminal
Router(config)# voice register pool
Router(config-register-pool)# type 8851 addon 1 CP-8800-Audio 2 CP-8800-Audio
Router(config-register-pool)# type 8851NR addon 1 CP-8800-Audio 2 CP-8800-Audio
Router(config-register-pool)# type 8861 addon 1 CP-8800-Audio 2 CP-8800-Audio 3 CP-8800-Audio
Router(config-register-pool)# type 8865 addon 1 CP-8800-Video 2 CP-8800-Video 3 CP-8800-Video
```

To configure KEM on Unified SIP Phones, see Configure KEMs on SIP Phones .

For more information on the KEM support for Cisco Unified 8851/51NR, 8861, 8865, 8961, 9951, and 9971 SIP IP Phones, see Phone Feature Support Guide for Unified CME, Unified SRST, Unified E-SRST, and Unified Secure SRST .

#### Key Mapping

The mapping of configured keys on a phone depends on the number of KEMs
                                 		attached to the phone.

If only one CKEM is attached to a phone and the number of keys configured is 114, only 36 keys on the CKEM are mapped to the
                                 configured keys on the phone. The rest of the keys are not visible on the phone or the KEM. The maximum number of supported
                                 keys on each A-KEM and V-KEM device is 28. For information on A-KEM and V-KEM support, see Table 1 .

#### Call Control

All call control features are supported by KEMs on Cisco Unified SIP IP phones. Any feature that can be configured on the
                                 phone keys can also be configured on the KEM.

#### XML Updates

There is no separate firmware for KEMs, instead they are built in as
                                       			 part of the phones.

The number of XML entries in the configuration file increases with
                                       			 the number of keys configured.

The device type for KEMs is C-KEM, BE-KEM, A-KEM, and V-KEM. The maximum number of supported keys on each C-KEM device is
                                       36. The maximum number of supported keys on each A-KEM and V-KEM device is 28.

#### Restrictions for KEM Support

KEMs are not supported for Cisco Unified SCCP IP phones and Cisco Unified SIP IP phones other than the Cisco Unified 8851/51NR,
                                       8861, 8865, 8961, 9951, and 9971 SIP IP phones.

Features configured on keys are disabled when supported Cisco
                                       			 Unified SIP IP phones are in Cisco Unified SIP SRST.

All Cisco Unified 8851/51NR, 8861, 8865, 8961, 9951, and 9971 SIP IP phone restrictions and limitations apply to KEMs.

All Cisco Unified CME and Cisco Unified SIP SRST feature
                                       			 restrictions and limitations apply to KEMs.

For more information on how the blf-speed-dial , number , and speed-dial commands, in voice register pool configuration mode, have been modified, see Cisco Unified Communications Manager Express Command Reference .

For information on installing KEMs on Cisco Unified IP Phone, see “Installing a Key Expansion Module on the Cisco Unified IP Phone” section of Cisco Unified IP Phone 8961, 9951, and 9971 Administration Guide for Cisco Unified Communications Manager 10.0 .

For information on installing KEMs on Cisco Unified 8811, 8841, 8851, 8851NR, 8865, and 8861 Phones, see Cisco IP Phone Key Expansion Module section of Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager .

### Fast-Track
                           	 Configuration Approach for Cisco Unified SIP IP Phones

In Cisco Unified CME
                              		Release 10.0, the Fast-Track Configuration feature provides a new configuration
                              		utility using which you can input the phone characteristics of a new SIP phone
                              		model. This utility allows you to configure the existing SIP line features to
                              		the new SIP phone models. In the fast-track configuration, an option is
                              		provided to input an existing SIP phone as a reference phone. This feature is
                              		supported only on new SIP phone models that do not need any changes in the
                              		software protocols and the Cisco Unified CME application.

To deploy Cisco
                                          		  Unified SIP IP phones on Cisco Unified CME using the fast-track configuration
                                          		  approach, you require Cisco IOS Release 15.3(3)M or a later release.

#### Forward
                                 		  Compatibility

When a new SIP
                                 		  phone model is configured using the fast-track configuration approach. and the
                                 		  Cisco Unified CME is upgraded to a later version that supports the new SIP
                                 		  phone model, the fast-track configuration pertaining to that SIP phone model is
                                 		  removed automatically. If the Cisco Unified CME is downgraded to a version that
                                 		  does not have the built-in support, the fast-track configuration should be
                                 		  applied again.

To support
                                 		  Fast-Track Configuration feature, the voice register
                                       				pool-type command has been introduced in the global configuration
                                 		  mode. The properties of the new SIP phone can be configured under the voice
                                 		  register pool-type submode. In addition to the explicit configuration of the
                                 		  phone’s properties, the reference-pooltype option can be used to inherit the
                                 		  properties of an existing SIP phone.

#### Localization
                                 		  support

CME supports
                                 		  localization for phones in fast-track mode through locale installer. However,
                                 		  the locale package should have .jar files for a specific phone model to make
                                 		  the feature work.

To use the locale
                                 		  installer, see Locale Installer for Cisco Unified SIP IP Phones .

For new SIP phone
                                 		  models validated using Fast-track configuration and the supported locale
                                 		  package version, see Phone Feature Support Guide
                                    			 for Unified CME, Unified SRST, Unified E-SRST, and Unified Secure SRST .

#### Restrictions
                                 		  for Fast-Track Support

The fast-track
                                       				configuration does not allow you to use the following phone models as reference
                                       				phone:

ATA—Cisco
                                             					 ATA-186 and Cisco ATA-188

7905—Cisco
                                             					 Unified IP Phone 7905 and Cisco Unified IP Phone 7905G

7912—Cisco
                                             					 Unified IP Phone 7912 and Cisco Unified IP Phone 7912G

7940—Cisco
                                             					 Unified IP Phone 7940 and Cisco Unified IP Phone 7940G

7960—Cisco
                                             					 Unified IP Phone 7960 and Cisco Unified IP Phone 7960G

P100—PingTel Xpressa 100

P600—Polycom SoundPoint IP 600

Existing
                                             					 Cisco Unified SIP IP phones are not allowed to be configured as new Cisco
                                             					 Unified SIP IP phones using the fast-track configuration approach.

The
                                             					 reference-pooltype functionality is allowed only on existing SIP phone models.
                                             					 New SIP phone models configured using the fast-track configuration approach
                                             					 cannot be used as a reference phone.

The
                                             					 fast-track configuration approach supports only the XML format and not support
                                             					 the text format for phone configuration.

The
                                             					 fast-track approach does not support the new SIP phone models that have a new
                                             					 call flow, new message flow, or a new configuration file format that are not
                                             					 supported by the Cisco Unified CME.

For configuration
                                 		  information, see Provision SIP Phones to Use the Fast-Track Configuration Approach .

For configuration examples, see Example for Fast-Track Configuration Approach .

## Configure Phones
                        	 for a PBX System

This section
                           		contains the following tasks:

### Create Directory
                           	 Numbers for SCCP Phones

To create a
                                 		  directory number in Cisco Unified CME for a SCCP phone, intercom line, voice
                                 		  port, or a message-waiting indicator (MWI), perform the following steps for
                                 		  each directory number to be created. Each ephone-dn becomes a virtual line, or
                                 		  extension, on which call connections can be made. Each ephone-dn configuration
                                 		  automatically creates one or more virtual dial peers and virtual voice ports to
                                 		  make those call connections.

Restriction

The
                                                   				  Cisco Unified IP Phone 7931G is a SCCP keyset phone and, when configured for a
                                                   				  key system, does not support the dual-line option for a directory number. To
                                                   				  configure a Cisco Unified IP Phone 7931G, see Configure Phones for a Key System .

Octo-line
                                                   				  directory numbers are not supported by the Cisco Unified IP Phone 7902, 7920,
                                                   				  or 7931, or by analog phones connected to the Cisco VG224 or Cisco ATA.

Octo-line
                                                   				  directory numbers are not supported in button overlay sets.

Octo-line
                                                   				  directory numbers do not support the trunk command.

#### Before you begin

Maximum number
                                       				of directory numbers must be changed from the default of 0 by using the max-dn command.

Octo-line
                                       				directory numbers are supported in Cisco Unified CME 4.3 and later versions.

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn dn-tag [ dual-line | octo-line ]

- number number [ secondary number ] [ no-reg [ both | primary ] ]

- huntstop [ channel number ]

- name name

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

ephone-dn dn-tag [ dual-line | octo-line ]

#### Example:

```
Router(config)# ephone-dn 7 octo-line
```

Enters
                                             				ephone-dn configuration mode to create a directory number for a SCCP phone.

dual-line —(Optional) Enables two calls per
                                                   					 directory number. Supports features such as call waiting, call transfer, and
                                                   					 conferencing with a single ephone-dn.

octo-line —(Optional) Enables eight calls per
                                                   					 directory number. Supported in Cisco Unified CME 4.3 and later versions.

To change
                                                   					 the line mode of a directory number, for example from dual-line to octo-line or
                                                   					 the reverse, you must first delete the ephone-dn and then recreate it.

Step 4

number number [ secondary number ] [ no-reg [ both | primary ] ]

#### Example:

```
Router(config-ephone-dn)# number 2001
```

Configures an
                                             				extension number for this directory number.

Configuring a secondary number supports features such as call
                                                   					 waiting, call transfer, and conferencing with a single ephone-dn.

Step 5

huntstop [ channel number ]

#### Example:

```
Router(config-ephone-dn)# huntstop channel 4
```

(Optional)
                                             				Enables Channel Huntstop, which keeps a call from hunting to the next channel
                                             				of a directory number if the first channel is busy or does not answer.

channel number —Number of channels available to accept
                                                   					 incoming calls. Remaining channels are reserved for outgoing calls and features
                                                   					 such as call transfer, call waiting, and conferencing. Range: 1 to 8. Default:
                                                   					 8.

number argument is supported for octo-line directory numbers only.

Step 6

name name

#### Example:

```
Router(config-ephone-dn)# name Smith, John
```

(Optional)
                                             				Associates a name with this directory number.

Name is
                                                   					 used for caller-ID displays and in the local directory listings.

Must
                                                   					 follow the name order that is specified with the directory command.

Step 7

end

#### Example:

```
Router(config-ephone-dn)# end
```

Returns to
                                             				privileged EXEC mode.

#### Example

Example for Nonshared
                                    			 Octo-Line Directory Number

In the following
                                 		  example, ephone-dn 7 is assigned to phone 10 and not shared by any other phone.
                                 		  There are two active calls on ephone-dn 7. Because the busy-trigger-per-button command is set to 2, a
                                 		  third incoming call to extension 2001 is either rejected with a busy tone or
                                 		  forwarded to another destination if Call Forward Busy is configured. The phone
                                 		  user can still make an outgoing call or transfer or conference a call on
                                 		  ephone-dn 7 because the max-calls-per-button command is set to 3, which
                                 		  allows a total of three calls on ephone-dn 7.

```
ephone-dn  7  octo-line
 number 2001 
	name Smith, John 
	huntstop channel 4
! 
! 
ephone  10
 max-calls-per-button 3
 busy-trigger-per-button 2 
 mac-address 00E1.CB13.0395 
 type 7960 
 button  1:7
```

Example for Shared
                                    			 Octo-Line Directory Number

In the following
                                 		  example, ephone-dn 7 is shared between phone 10 and phone 11. There are two
                                 		  active calls on ephone-dn 7. A third incoming call to ephone-dn 7 rings only
                                 		  phone 11 because its busy-trigger-per-button command is set to 3. Phone
                                 		  10 allows a total of three calls, but it rejects the third incoming call
                                 		  because its busy-trigger-per-button command is set to 2. A
                                 		  fourth incoming call to ephone-dn 7 on ephone 11 is either rejected with a busy
                                 		  tone or forwarded to another destination if Call Forward Busy is configured.
                                 		  The phone user can still make an outgoing call or transfer or conference a call
                                 		  on ephone-dn 7 on phone 11 because the max-calls-per-button command is set to 4, which
                                 		  allows a total of four calls on ephone-dn 7 on phone 11.

```
ephone-dn  7  octo-line 
 number 2001 
 name Smith, John 
 huntstop channel 4 
! 
! 
ephone  10 
 max-calls-per-button 3 
 busy-trigger-per-button 2 
 mac-address 00E1.CB13.0395> 
 type 7960
 button  1:7 
! 
! 
! 
ephone  11 
 max-calls-per-button 4 
 busy-trigger-per-button 3 
 mac-address 0016.9DEF.1A70
 type 7960 
 button  1:7
```

#### What to do next

After creating
                                 		  directory numbers, you can assign one or more directory numbers to a Cisco
                                 		  Unified IP Phone. See Assign Directory Numbers to SCCP Phones .

### Configure
                           	 Ephone-Type Templates for SCCP Phones

Restriction

#### Before you begin

Cisco Unified CME
                                 		  4.3 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- ephone-type phone-type [ addon ]

- device-id number

- device-name name

- device-type phone-type

- num-buttons number

- max-presentation number

- addon

- security

- phoneload

- utf8

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

ephone-type phone-type [ addon ]

#### Example:

```
Router(config)# ephone-type E61
```

Enters
                                             				ephone-type configuration mode to create an ephone-type template.

phone-type —Unique label that identifies the type
                                                   					 of IP phone for which the phone-type template is being defined.

addon —(Optional) Phone type is an add-on module,
                                                   					 such as the Cisco Unified IP Phone 7915 Expansion Module.

Step 4

device-id number

#### Example:

```
Router(config-ephone-type)# device-id 376
```

Specifies the
                                             				device ID for the phone type.

This
                                                   					 device ID must match the predefined device ID for the specific phone model.

If this
                                                   					 command is set to the default value of 0, the ephone-type is invalid.

See Table 1 for a list of supported device IDs.

Step 5

device-name name

#### Example:

```
Router(config-ephone-type)# device-name E61 Mobile Phone
```

Assigns a name
                                             				to the phone type.

See Table 1 for a list of supported device types.

Step 6

device-type phone-type

#### Example:

```
Router(config-ephone-type)# device-type E61
```

Specifies the
                                             				device type for the phone.

Step 7

num-buttons number

#### Example:

```
Router(config-ephone-type)# num-buttons 1
```

Number of line
                                             				buttons supported by the phone type.

number —Range: 1 to 100. Default: 0.

See Table 1 for the number of buttons supported by each phone type.

Step 8

max-presentation number

#### Example:

```
Router(config-ephone-type)# max-presentation 1
```

Number of
                                             				call presentation lines supported by the phone type.

number —Range: 1 to 100. Default: 0.

See Table 1 for the number of presentation lines supported by each phone type.

Step 9

addon

#### Example:

```
Router(config-ephone-type)# addon
```

(Optional)
                                             				Specifies that this phone type supports an add-on module, such as the Cisco
                                             				Unified IP Phone 7915 Expansion Module.

Step 10

security

#### Example:

```
Router(config-ephone-type)# security
```

(Optional)
                                             				Specifies that this phone type supports security features.

This
                                                   					 command is enabled by default.

Step 11

phoneload

#### Example:

```
Router(config-ephone-type)# phoneload
```

(Optional)
                                             				Specifies that this phone type requires that the load command be configured.

This
                                                   					 command is enabled by default.

Step 12

utf8

#### Example:

```
Router(config-ephone-type)# utf8
```

(Optional)
                                             				Specifies that this phone type supports UTF8.

This
                                                   					 command is enabled by default.

Step 13

end

#### Example:

```
Router(config-ephone-type)# end
```

Exits to
                                             				privileged EXEC mode.

#### Ephone-Type
                              	 Parameters for Supported Phone Types

Table 1 lists the required device ID, device type, and the maximum number of buttons
                                    		  and call presentation lines that are supported for each phone type that can be
                                    		  added with ephone-type templates.

Supported
                                                					 Device

device-id

device-type

num-buttons

max-presentation

Cisco Unified IP  Phoone 6901

547

6901

1

1

Cisco Unified IP  Phone 6911

548

6911

10

1

Cisco
                                                					 Unified IP Phone 6945

564

6945

4

2

Cisco Unified IP Phone 7915 Expansion Module with 12 buttons

227

7915

12

0
                                                					 (default)

Cisco Unified IP  Phone 7915 Expansion Module with 24 buttons

228

7915

24

0

Cisco Unified IP  Phone 7916 Expansion Module with 12 buttons

229

7916

12

0

Cisco Unified IP  Phone 7916 Expansion Module with 24 buttons

230

7916

24

0

Cisco Unified  Wireless IP Phone  7925

484

7925

6

4

Cisco
                                                					 Unified IP Conference  Station 7937G

431

7937

1

6

Cisco
                                                					 Unified IP Phone 8941

586

8941

4

3

Cisco
                                                					 Unified IP Phone 8945

585

8945

4

3

Cisco
                                                					 Unified IP Phone 8941 with Fast-Track configuration support

586

8941

4

3

Cisco
                                                					 Unified IP Phone 8945 with Fast-Track configuration support

586

8945

4

3

Nokia
                                                					 E61

376

E61

1

1

Example

The following
                                    		  example shows the Nokia E61 added with an ephone-type template, which is then
                                    		  assigned to ephone 2:

```
ephone-type  E61
		 device-id 376
		 device-name E61 Mobile Phone
		 num-buttons 1
		 max-presentation 1
		 no utf8
		 no phoneload
		!
		ephone  2
		 mac-address 001C.821C.ED23
		 type E61
		 button  1:2
```

### Assign Directory
                           	 Numbers to SCCP Phones

This task sets up the initial ephone-dn-to-ephone relationships: how and which extensions appear on each phone. To create
                                 and modify phone-specific parameters for individual SCCP phones, perform the following steps for each SCCP phone to be connected
                                 in Cisco Unified CME.

To create and
                                             			 assign directory numbers to be included in an overlay set, see Configure Overlaid Ephone-dns on SCCP Phones .

Restriction

For Watch
                                                   				  mode. If the watched directory number is associated with several phones, then
                                                   				  the watched phone is the one on which the watched directory number is on button
                                                   				  1 or the one on which the watched directory number is on the button that is
                                                   				  configured by using the auto-line command, with auto-line having priority. For
                                                   				  configuration information, see Automatic Line Selection .

Octo-line
                                                   				  directory numbers are not supported by the Cisco Unified IP Phone 7902, 7920,
                                                   				  or 7931, or by analog phones connected to the Cisco VG224 or Cisco ATA.

Octo-line
                                                   				  directory numbers are not supported in button overlay sets.

#### Before you begin

To configure a
                                       				phone line for Watch (w) mode by using the button command, Cisco Unified CME 4.1 or a later version.

To configure a
                                       				phone line for Monitor (m) mode by using the button command, Cisco CME 3.0 or a later version.

To assign a
                                       				user-defined phone type in Cisco Unified CME 4.3 or a later version, you must
                                       				first create an ephone-type template. See Configure Ephone-Type Templates for SCCP Phones .

### SUMMARY STEPS

- enable

- configure terminal

- ephone phone-tag

- mac-address [ mac-address ]

- type phone-type [ addon 1 module-type [ 2 module-type ] ]

- button button-number { separator } dn-tag [ , dn-tag... ] [ button-number { x } overlay-button-number ] [ button-number... ]

- max-calls-per-button number

- busy-trigger-per-button number

- keypad-normalize

- nte-end-digit-delay [ milliseconds ]

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
Router(config)#ephone 6
```

Enters ephone
                                             				configuration mode.

phone-tag —Unique sequence number that identifies
                                                   					 this ephone during configuration tasks. The maximum number of ephones is
                                                   					 version and platform-specific. Type ? to display
                                                   					 range.

Step 4

mac-address [ mac-address ]

#### Example:

```
Router(config-ephone)#mac-address 2946.3f2.311
```

Specifies the
                                             				MAC address of the IP phone that is being configured.

mac-address —(Optional) For CiscoUnifiedCME 3.0 and
                                                   					 later versions, it is not required to register phones before configuring the
                                                   					 phone because CiscoUnifiedCME can detect MAC addresses and automatically
                                                   					 populate phone configurations with the MAC addresses and phone types for
                                                   					 individual phones. Not supported for voice-mail ports.

Step 5

type phone-type [ addon 1 module-type [ 2 module-type ] ]

#### Example:

```
Router(config-ephone)# type 7960 addon 1 7914
```

Specifies the
                                             				type of phone.

CiscoUnifiedCME 4.0 and later versionsThe only types to which
                                                   					 you can apply an add-on module are 7960 , 7961 , 7961GE , and 7970 .

CiscoCME
                                                   					 3.4 and earlier versionsThe only type to which you can apply an add-on module
                                                   					 is 7960 .

Step 6

button button-number { separator } dn-tag [ , dn-tag... ] [ button-number { x } overlay-button-number ] [ button-number... ]

#### Example:

```
Router(config-ephone)# button 1:10 2:11 3b12 4o13,14,15
```

Associates
                                             				a button number and line characteristics with an extension (ephone-dn). Maximum
                                             				number of buttons is determined by phone type.

The
                                                         				  CiscoUnified IPPhone7910 has only one line button but can be given two
                                                         				  ephone-dn tags.

Step 7

max-calls-per-button number

#### Example:

```
Router(config-ephone)# max-calls-per-button 3
```

(Optional)
                                             				Sets the maximum number of calls, incoming and outgoing, allowed on an
                                             				octo-line directory number on this phone.

number —Range: 1 to 8. Default: 8.

This
                                                   					 command is supported in CiscoUnifiedCME4.3 and later versions.

This
                                                   					 command must be set to a value that is more than or equal to the value set with
                                                   					 the busy-trigger-per-button command.

This
                                                   					 command can also be configured in ephone-template configuration mode and
                                                   					 applied to one or more phones. The ephone configuration has priority over the
                                                   					 ephone-template configuration.

Step 8

busy-trigger-per-button number

#### Example:

```
Router(config-ephone)# busy-trigger-per-button 2
```

(Optional)
                                             				Sets the maximum number of calls allowed on this phones octo-line directory
                                             				numbers before triggering Call Forward Busy or a busy tone.

number —Range: 1 to 8. Default: 0 (disabled).

This
                                                   					 command is supported in CiscoUnifiedCME4.3 and later versions.

After
                                                   					 the number of existing calls, incoming and outgoing, on an octo-line directory
                                                   					 number exceeds the number of calls set with this command, the next incoming
                                                   					 call to the directory number is forwarded to the Call Forward Busy destination
                                                   					 if configured, or the call is rejected with a busy tone.

This
                                                   					 command must be set to a value that is less than or equal to the value set with
                                                   					 the max-calls-per-button command.

This
                                                   					 command can also be configured in ephone-template configuration mode and
                                                   					 applied to one or more phones. The ephone configuration has priority over the
                                                   					 ephone-template configuration.

Step 9

keypad-normalize

#### Example:

```
Router(config-ephone)# keypad-normalize
```

(Optional)
                                             				Imposes a 200-millisecond delay before each keypad message from an IP phone.

When
                                                   					 used with the nte-end-digit-delay command, this command ensures
                                                   					 that the delay configured for a dtmf-end event is always honored.

Step 10

nte-end-digit-delay [ milliseconds ]

#### Example:

```
Router(config-ephone)# nte-end-digit-delay 150
```

(Optional)
                                             				Specifies the amount of time that each digit in the RTP NTE end event in an
                                             				RFC2833 packet is delayed before being sent.

This
                                                   					 command is supported in CiscoUnifiedCME 4.3 and later versions.

milliseconds —length of delay. Range: 10 to 200.
                                                   					 Default: 200.

To
                                                   					 enable the delay, you must also configure the dtmf-interworking
                                                         						  rtp-nte command in voice-service or dial-peer configuration mode.
                                                   					 For information, see Enable DTMF Integration Using RFC 2833 .

This
                                                   					 command can also be configured in ephone-template configuration mode. The value
                                                   					 set in ephone configuration mode has priority over the value set in
                                                   					 ephone-template mode.

Step 11

end

#### Example:

```
Router(config-ephone)# end
```

Returns to
                                             				privileged EXEC mode.

#### Example

Example for assigning
                                    			 directory number to SCCP Phone

The following
                                 		  example assigns extension 2225 in the Accounting Department to button 1 on
                                 		  ephone 2:

```
ephone-dn 25
			 number 2225
			 name Accounting 
			
			 ephone 2 
			 mac-address 00E1.CB13.0395 
			 type 7960
			 button 1:25
```

#### What to do next

If you have
                                       				SIP and SCCP phones connected to the same Cisco Unified CME, see Configure Codecs of Individual Phones for Calls Between Local Phones .

After
                                       				configuring phones in Cisco Unified CME to make basic calls, you are ready to
                                       				generate configuration files for the phones to be connected. See Generate Configuration Files for SCCP Phones .

### Create Directory
                           	 Numbers for SIP Phones

To create a
                                 		  directory number in Cisco Unified CME for a SIP phone, intercom line, voice
                                 		  port, or a message-waiting indicator (MWI), perform the following steps for
                                 		  each directory number to be created.

Restriction

Valid characters in voice register DN include 0–9, '.', '+', '*', and '#'.

The name or label that is associated with a directory number that is configured under voice register dn or voice register global configuration mode cannot contain special characters such as quotes ("), angle brackets (<, >), ampersand (&), and percentage
                                                   (%).

To allow insertion of '#' at any place in voice register DN, the CLI "allow-hash-in-dn" is configured in voice register global
                                                   mode.

When the CLI
                                                   				  "allow-hash-in-dn" is configured, the user is required to change the dial-peer
                                                   				  terminator from '#' (default terminator) to another valid terminator in
                                                   				  configuration mode. The other terminators that are supported include '0'-'9',
                                                   				  'A'-'F', and '*'.

Maximum number of directory numbers that are supported by a router is version and platform dependent.

Call Forward
                                                   				  All, Presence, and message-waiting indication (MWI) features in Cisco Unified
                                                   				  CME 4.1 and later versions require that SIP phones be configured with a
                                                   				  directory number using the dn keyword
                                                   				  with the number command; direct line numbers are not supported.

SIP
                                                   				  endpoints are not supported on H.323 trunks. SIP endpoints are supported on SIP
                                                   				  trunks only.

The Media
                                                   				  Flow-around feature configured with the media
                                                         						flow-around command is not supported by Cisco Unified CME with
                                                   				  SIP phones.

SIP shared-line directory numbers are not supported by the Cisco Unified IP Phone 7902, 7920, 7931, 7940, or 7960, or by analog
                                                   phones connected to the Cisco VG224.

For Unified
                                                   				  CME 12.1 and prior releases, SIP shared-line directory numbers cannot be
                                                   				  members of voice hunt groups.

If this directory number is used as shared line, you can associate the directory number to a maximum of 16 phones.

#### Before you begin

Cisco CME 3.4
                                       				or a later version.

SIP
                                       				shared-line directory numbers are supported in Cisco Unified CME 7.1 and later
                                       				versions.

registrar
                                             					 server command must be configured. For configuration information,
                                       				see Enable Calls in Your VoIP Network .

In
                                       				Cisco Unified CME 7.1 and later versions, the maximum number of directory
                                       				numbers must be changed from the default of 0 by using the max-dn (voice
                                       				register global) command. For configuration information, see Set Up Cisco Unified CME for SIP Phones .

### SUMMARY STEPS

- enable

- configure terminal

- voice register dn dn-tag

- number number

- shared-line [ max-calls number-of-calls ]

- huntstop channel number-of-channels

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
Router(config)# voice register dn 17
```

Enters voice register DN configuration mode to define a directory number for a SIP phone, intercom line, voice port, or a
                                             message-waiting indicator (MWI).

Step 4

number number

#### Example:

```
Router(config-register-dn)# number 7001
```

Defines a
                                             				valid number for a directory number.

Step 5

shared-line [ max-calls number-of-calls ]

#### Example:

```
Router(config-register-dn)# shared-line max-calls 6
```

(Optional)
                                             				Creates a shared-line directory number.

max-calls number-of-calls (Optional)—Maximum number of calls, both incoming and outgoing. Range: 2–16. Default: 2.

Must be
                                                   					 set to a value that is more than or equal to the value set with the busy-trigger-per-button command.

This
                                                   					 command is supported in Cisco Unified CME 7.1 and later versions.

Step 6

huntstop channel number-of-channels

#### Example:

```
Router(config-register-dn)# huntstop channel 3
```

(Optional)
                                             				Enables Channel Huntstop, which keeps a call from hunting to the next channel
                                             				of a directory number if the first channel is busy or does not answer.

number-of-channels —Number of channels available to accept incoming calls on the directory number. Remaining channels are reserved for outgoing
                                                   calls and features, such as Call Transfer, Call Waiting, and Conferencing. Range: 1–50. Default: 0 (disabled).

This
                                                   					 command is supported in Cisco Unified CME 7.1 and later versions.

Step 7

end

#### Example:

```
Router(config-register-dn)# end
```

Exits to
                                             				privileged EXEC mode.

#### Example

Example for assigning
                                    			 directory numbers to SIP Phones

The following
                                 		  example shows directory number 24 configured as a shared line and assigned to
                                 		  phone 124 and phone 125:

```
voice register dn  24 
			  number 8124
			  shared-line max-calls 6
			 !
			 voice register pool  124 
			  id mac 0017.E033.0284 
			  type 7965
			  number 1 dn 24 
			 ! 
			 voice register pool  125
			  id mac 00E1.CB13.0395 
			  type 7965
			 number 1 dn 24
```

### Assign Directory
                           	 Numbers to SIP Phones

This task sets up
                                 		  which extensions appear on each phone. To create and modify phone-specific
                                 		  parameters for individual SIP phones, perform the following steps for each SIP
                                 		  phone to be connected in Cisco Unified CME.

If your
                                             			 Cisco Unified CME system supports SCCP and SIP phones, do not connect your SIP
                                             			 phones to your network until after you have verified the configuration profile
                                             			 for the SIP phone.

### SUMMARY STEPS

- enable

- configure terminal

- voice register pool pool-tag

- id { network address mask mask | ip address mask mask | mac address }

- type phone-type

- number tag dn dn-tag

- busy-trigger-per-button number-of-calls

- username username password password

- dtmf-relay { [ cisco-rtp ] [ rtp-nte ] [ sip-notify ] }

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

voice register pool pool-tag

#### Example:

```
Router(config)# voice register pool 3
```

Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone.

Step 4

id { network address mask mask | ip address mask mask | mac address }

#### Example:

```
Router(config-register-pool)#
			 id mac 0009.A3D4.1234
```

Explicitly
                                             				identifies a locally available individual SIP phone to support a degree of
                                             				authentication.

Step 5

type phone-type

#### Example:

```
Router(config-register-pool)# type 7960-7940
```

Defines a
                                             				phone type for the SIP phone being configured.

Step 6

number tag dn dn-tag

#### Example:

```
Router(config-register-pool)# number 1 dn 17
```

Associates a
                                             				directory number with the SIP phone being configured.

dn dn-tag —identifies the directory number for this
                                                   					 SIP phone as defined by the voice register
                                                         						  dn command.

Step 7

busy-trigger-per-button number-of-calls

#### Example:

```
Router(config-register-pool)# busy-trigger-per-button 2
```

(Optional)
                                             				Sets the maximum number of calls allowed on any of this phone�s directory
                                             				numbers before triggering Call Forward Busy or a busy tone.

number-of-calls —Maximum number of calls allowed
                                                   					 before Cisco Unified CME forwards the next incoming call to the Call Forward
                                                   					 Busy destination, if configured, or rejects the call with a busy tone. Range: 1
                                                   					 to 50.

This
                                                   					 command is supported in Cisco Unified CME 7.1 and later versions.

Step 8

username username password password

#### Example:

```
Router(config-register-pool)# username smith password 123zyx
```

(Optional)
                                             				Required only if authentication is enabled with the authenticate command. Creates an authentication
                                             				credential.

This
                                                         				  command is not for SIP proxy registration. The password will not be encrypted.
                                                         				  All lines in a phone will share the same credential.

username —identifies a local Cisco Unified IP phone
                                                   					 user. Default: Admin.

Step 9

dtmf-relay { [ cisco-rtp ] [ rtp-nte ] [ sip-notify ] }

#### Example:

```
Router(config-register-pool)# dtmf-relay rtp-nte
```

(Optional)
                                             				Specifies a list of DTMF relay methods that can be used by the SIP phone to
                                             				relay DTMF tones.

SIP phones
                                                         				  natively support in-band DTMF relay as specified in RFC 2833.

Step 10

end

#### Example:

```
Router(config-register-pool)# end
```

Returns to
                                             				privileged EXEC mode.

#### Example for
                                 		  configuring SIP Nonshared Line

In the following
                                 		  example, voice register dn 23 is assigned to phone 123. The fourth incoming
                                 		  call to extension 8123 is not presented to the phone because the huntstop
                                       				channel command is set to 3. Because the busy-trigger-per-button command is set to 2 on
                                 		  phone 123 and Call Forward Busy is configured, the third incoming call to
                                 		  extension 8123 is forwarded to extension 8200.

```
voice register dn  23
 number 8123
 call-forward b2bua busy 8200
 huntstop channel 3
!
voice register pool  123
 busy-trigger-per-button 2
 id mac 0009.A3D4.1234
 type 7965
 number 1 dn 23
```

In the following
                                 		  example, voice register dn 24 is shared by phones 124 and 125. The first two
                                 		  incoming calls to extension 8124 ring both phones. A third incoming call rings
                                 		  only phone 125 because its busy-trigger-per-button command is set to 3. The
                                 		  fourth incoming call to extension 8124 triggers Call Forward Busy because the
                                 		  busy trigger limit on all phones is exceeded.

```
voice register dn  24
 number 8124
 call-forward b2bua busy 8200
 shared-line max-calls 6
 huntstop channel 6
!
voice register pool  124
 busy-trigger-per-button 2
 id mac 0017.E033.0284
 type 7965
 number 1 dn 24
!
voice register pool  125
 busy-trigger-per-button 3
 id mac 00E1.CB13.0395
 type 7965
 number 1 dn 24
```

#### What to do next

If you have
                                       				SIP and SCCP phones connected to the same Cisco Unified CME, see Configure Codecs of Individual Phones for Calls Between Local Phones .

If you want
                                       				to select the session-transport protocol for a SIP phone, see Select Session-Transport Protocol for a SIP Phone .

If you are
                                       				finished configuring phones to make basic calls, you are ready to generate
                                       				configuration files for the phones to be connected. See Generate Configuration Profiles for SIP Phones .

### Configure Dial
                           	 Plans for SIP Phones

Dial plans enable
                                 		  SIP phones to recognize digit strings dialed by users. After the phone
                                 		  recognizes a dial pattern, it automatically sends a SIP INVITE message to the
                                 		  Cisco Unified CME to initiate the call and does not require the user to press
                                 		  the Dial key or wait for the interdigit timeout. To define a dial plan for a
                                 		  SIP phone, perform the following steps.

#### Before you begin

Cisco Unified CME 4.1 or a later version.

mode cme command must be enabled in Cisco Unified CME.

### SUMMARY STEPS

- enable

- configure terminal

- voice register dialplan dialplan-tag

- type phone-type

- pattern tag string [ button button-number ] [ timeout seconds ] [ user { ip | phone } ] or filename filename

- exit

- voice register pool pool-tag

- dialplan dialplan-tag

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

voice register dialplan dialplan-tag

#### Example:

```
Router(config)# voice register dialplan 1
```

Enters voice
                                             				register dialplan configuration mode to define a dial plan for SIP phones.

Step 4

type phone-type

#### Example:

```
Router(config-register-dialplan)# type 7905-7912
```

Defines a
                                             				phone type for the SIP dial plan.

7905-7912 —Cisco Unified IP Phone 7905, 7905G,
                                                   					 7912, or 7912G.

7940-7960-others —Cisco Unified IP Phone 7911,
                                                   					 7940, 7940G, 7941, 7941GE, 7960, 7960G, 7961, 7961GE, 7970, or 7971.

The phone
                                                   					 type specified with this command must match the type of phone for which the
                                                   					 dial plan is used. If this phone type does not match the type assigned to the
                                                   					 phone with the type command
                                                   					 in voice register pool mode, the dial-plan configuration file is not generated.

You must
                                                   					 enter this command before using the pattern or filename command in the next step.

Step 5

pattern tag string [ button button-number ] [ timeout seconds ] [ user { ip | phone } ] or filename filename

#### Example:

```
Router(config-register-dialplan)# pattern 1 52...
```

or

```
Router(config-register-dialplan)# filename dialsip
```

Defines a dial
                                             				pattern for a SIP dial plan.

tag —Number that identifies the dial pattern.
                                                   					 Range: 1 to 24.

string —Dial pattern, such as the area code,
                                                   					 prefix, and first one or two digits of the telephone number, plus wildcard
                                                   					 characters or dots (.) for the remainder of the dialed digits.

button button-number —(Optional) Button to which the dial
                                                   					 pattern applies.

timeout seconds —
                                                   					 (Optional) Time, in seconds, that the system waits before dialing the number
                                                   					 entered by the user. Range: 0 to 30. To have the number dialed immediately,
                                                   					 specify 0. If you do not use this parameter, the phone's default interdigit
                                                   					 timeout value is used (10 seconds).

user —(Optional) Tag that automatically gets added
                                                   					 to the dialed number. Do not use this keyword if Cisco Unified CME is the only
                                                   					 SIP call agent.

ip —Uses the
                                                   					 IP address of the user.

phone —Uses
                                                   					 the phone number of the user.

Repeat
                                                   					 this command for each pattern that you want to include in this dial plan.

or

Specifies a
                                             				custom XML file that contains the dial patterns to use for the SIP dial plan.

You must
                                                   					 load the custom XML file must into flash and the filename cannot include the
                                                   					 .xml extension.

The filename command is not supported for the Cisco Unified IP Phone 7905 or 7912.

Step 6

exit

#### Example:

```
Router(config-register-dialplan)# exit
```

Exits
                                             				dialplan configuration mode.

Step 7

voice register pool pool-tag

#### Example:

```
Router(config)# voice register pool 4
```

Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone.

- pool-tag —Unique sequence number of the SIP phone
                                                				  to be configured. Range is version and platform-dependent; type ? to
                                                				  display range. You can modify the upper limit for this argument by using the
                                                				  the max-pool command.

Step 8

dialplan dialplan-tag

#### Example:

```
Router(config-register-pool)# dialplan 1
```

Assigns a
                                             				dial plan to a SIP phone.

dialplan-tag —Number that identifies the dial plan
                                                   					 to use for this SIP phone. This is the number that was used with the voice register
                                                         						  dialplan command in Step 3. Range: 1 to 24.

Step 9

end

#### Example:

```
Router(config-register-global)# end
```

Exits to
                                             				privileged EXEC mode.

#### Examples

The following
                                 		  example shows the configuration for dial plan 1, which is assigned to SIP phone
                                 		  1:

```
voice register dialplan  1 
		 type 7940-7960-others 
		 pattern 1 2... timeout 10 user ip 
		 pattern 2 1234 user ip button 4 
		 pattern 3 65... 
		 pattern 4 1...! 
		! 
		voice register pool  1 
		 id mac 0016.9DEF.1A70 
		 type 7961GE 
		 number 1 dn 1 
		 number 2 dn 2 
		 dialplan 1 
		 dtmf-relay rtp-nte 
		 codec g711ulaw
```

#### Troubleshooting
                              	 Tips for Configuring Dial Plans for SIP

If you create a
                                    		  dial plan by downloading a custom XML dial pattern file to flash and using the filename command, and the XML file contains an error, the dial plan might not work
                                    		  properly on a phone. We recommend creating a dial pattern file using the pattern command.

To remove a dial
                                    		  plan that was created using a custom XML file with the filename command, you must remove the dial plan from the phone, create a new
                                    		  configuration profile, and then use the reset command
                                    		  to reboot the phone. You can use the restart command after removing a dial plan from a phone only if the dial plan was
                                    		  created using the pattern command.

To use KPML if a
                                    		  matching dial plan is not found, when both a dial plan and KPML are enabled on
                                    		  a phone, you must configure a dial pattern with a single wildcard character (.)
                                    		  as the last pattern in the dial plan. For example:

```
voice register dialplan 10
 type 7940-7960-others
 pattern 1 66...
 pattern 2 91.......
```

What to Do Next

If you are done
                                    		  modifying parameters for SIP phones, you must generate a new configuration
                                    		  profile and restart the phones. See Configuration Files for Phones .

### Verify SIP Dial Plan Configuration

Step 1

show voice register dialplan tag

This command displays the configuration information for a specific
                                             				SIP dial plan.

#### Example:

```
Router# show voice register dialplan 1 Dialplan Tag 1
Config:
  Type is 7940-7960-others
  Pattern 1 is 2..., timeout is 10, user option is ip, button is default
  Pattern 2 is 1234, timeout is 0, user option is ip, button is 4
  Pattern 3 is 65..., timeout is 0, user option is phone, button is default
  Pattern 4 is 1..., timeout is 0, user option is phone, button is default
```

Step 2

show voice register pool tag

This command displays the dial plan assigned to a specific SIP
                                             				phone.

#### Example:

```
Router# show voice register pool 29 Pool Tag 29
Config:
  Mac address is 0012.7F54.EDC6
  Number list 1 : DN 29
  Proxy Ip address is 0.0.0.0
  DTMF Relay is disabled
  Call Waiting is enabled
  DnD is disabled
  keep-conference is enabled
  dialplan tag is 1
  kpml signal is enabled
  service-control mechanism is not supported
.
.
.
```

Step 3

show voice register template tag

This command displays the dial plan assigned to a specific
                                             				template.

#### Example:

```
Router# show voice register template 3 Temp Tag 3
Config:
  Attended Transfer is disabled
  Blind Transfer is enabled
  Semi-attended Transfer is enabled
  Conference is enabled
  Caller-ID block is disabled
  DnD control is enabled
  Anonymous call block is disabled
  Voicemail is 62000, timeout 15
  Dialplan Tag is 1
  Transport type is tcp
```

### Enable KPML on a
                           	 SIP Phone

To enable KPML
                                 		  digit collection on a SIP phone, perform the following steps.

Restriction

This feature
                                                   				  is supported only on Cisco Unified IP Phones 7911G, 7941G, 7941GE, 7961G,
                                                   				  7961GE, 7970G, and 7971GE.

A dial plan
                                                   				  assigned to a phone has priority over KPML.

#### Before you begin

Cisco Unified CME
                                 		  4.1 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice register pool pool-tag

- digit collect kpml

- end

- show voice register dial-peers

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

voice register pool pool-tag

#### Example:

```
Router(config)# voice register pool 4
```

Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone.

pool-tag —Unique sequence number of the SIP phone
                                                   					 to be configured. Range is version and platform-dependent; type ? to
                                                   					 display range. You can modify the upper limit for this argument by using the max-pool command.

Step 4

digit collect kpml

#### Example:

```
Router(config-register-pool)# digit collect kpml
```

Enables KPML
                                             				digit collection for the SIP phone.

This command
                                                         				  is enabled by default for supported phones in Cisco Unified CME.

Step 5

end

#### Example:

```
Router(config-register-pool)# end
```

Exits to
                                             				privileged EXEC mode.

Step 6

show voice register dial-peers

#### Example:

```
Router# show voice register dial-peers
```

Displays
                                             				details of all dynamically created VoIP dial peers associated with the Cisco
                                             				Unified CME SIP register, including the defined digit collection method.

#### What to do next

If you are done
                                 		  modifying parameters for SIP phones, you must generate a new configuration
                                 		  profile and restart the phones. See Configuration Files for Phones .

### Select
                           	 Session-Transport Protocol for a SIP Phone

To change the
                                 		  session-transport protocol for a SIP phone from the default of UDP to TCP,
                                 		  perform the following steps.

Restriction

TCP is not
                                                   				  supported as a session-transport protocol for the Cisco Unified IP Phone 7905,
                                                   				  7912, 7940, or 7960. If TCP is assigned to an unsupported phone, calls to that
                                                   				  phone will not complete successfully. However, the phone can originate calls
                                                   				  using UDP, although TCP has been assigned.

#### Before you begin

Cisco Unified CME 4.1 or a later version.

Directory
                                       				number must be assigned to SIP phone to which configuration is to be applied.
                                       				For configuration information, see Assign Directory Numbers to SIP Phones .

### SUMMARY STEPS

- enable

- configure terminal

- voice register pool pool-tag

- session-transport { tcp | udp }

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

voice register pool pool-tag

#### Example:

```
Router(config)# voice register pool 3
```

Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone in Cisco Unified CME.

Step 4

session-transport { tcp | udp }

#### Example:

```
Router(config-register-pool)# session-transport tcp
```

(Optional)
                                             				Specifies the transport layer protocol that a SIP phone uses to connect to
                                             				Cisco Unified CME.

This
                                                   					 command can also be configured in voice register template configuration mode
                                                   					 and applied to one or more phones. The voice register pool configuration has
                                                   					 priority over the voice register template configuration.

Step 5

end

#### Example:

```
Router(config-register-pool)# end
```

Exits voice
                                             				register pool configuration mode and enters privileged EXEC mode.

#### What to do next

If you want to
                                       				disable SIP Proxy registration for an individual directory number, see Disable SIP Proxy Registration for a Directory Number .

If you have
                                       				SIP and SCCP phones connected to the same Cisco Unified CME, see Configure Codecs of Individual Phones for Calls Between Local Phones .

If you are
                                       				finished configuring phones to make basic calls, you are ready to generate
                                       				configuration files for the phones to be connected. See Generate Configuration Profiles for SIP Phones .

### Disable SIP Proxy Registration for a Directory Number

To prevent a particular directory number from registering with an external SIP proxy server, perform the following steps.

Restriction

#### Before you begin

Cisco Unified CME 3.4 or a later version.

Bulk registration is configured at system level. For configuration information, see Configure Bulk Registration .

### SUMMARY STEPS

- enable

- configure terminal

- voice register dn dn-tag

- number number

- no-reg

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

voice register dn dn-tag

#### Example:

```
Router(config-register-global)# voice register dn 1
```

Enters voice register dn configuration mode to define a directory number for a SIP phone, intercom line, voice port, or an
                                             MWI.

Step 4

number number

#### Example:

```
Router(config-register-dn)# number 4085550152
```

Defines a valid number for a directory number to be assigned to a SIP phone in Cisco Unified CME.

Step 5

no-reg

#### Example:

```
Router(config-register-dn)# no-reg
```

Prevents directory number being configured from registering with an external proxy server.

Step 6

end

#### Example:

```
Router(config-register-dn)# end
```

Exits voice register dn configuration mode and enters privileged EXEC mode.

#### What to do next

If you want to configure the G.722-64K codec for all calls through your Cisco Unified CME system, see Modify the Global Codec .

If you have SIP and SCCP phones connected to the same Cisco Unified CME, see Configure Codecs of Individual Phones for Calls Between Local Phones .

If you want to configure individual phones to support some codec other than the system-level codec or some codec other than
                                       the phone s native codec, see Codecs for Cisco Unified CME Phones .

If you are finished configuring phones to make basic calls, you are ready to generate configuration files for the phones to
                                       be connected. See Generate Configuration Profiles for SIP Phones .

### Modify the Global
                           	 Codec

To change the
                                 		  global codec from the default (G.711ulaw) to G.722-64K for all calls through
                                 		  Cisco Unified CME, perform the following steps.

Restriction

#### Before you begin

Cisco Unified CME
                                 		  4.3 or later versions.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- codec { g711-ulaw | g722-64k }

- service phone g722CodecSupport { 0 | 1 | 2 }

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
                                             				telephony service configuration mode to set parameters for SCCP and SIP phones
                                             				in Cisco Unified CME.

Step 4

codec { g711-ulaw | g722-64k }

#### Example:

```
Router(config-telephony)# codec g722-64k
```

Specifies the
                                             				preferred codec for phones in Cisco Unified CME.

Required
                                                   					 only if you want to modify codec from the default (G.711ulaw) to G.722-64K.

Step 5

service phone g722CodecSupport { 0 | 1 | 2 }

#### Example:

```
Router(config)# service phone g722CodecSupport 2
```

Causes all
                                             				phones to advertise the G.722-64K codec to Cisco Unified CME.

Required
                                                   					 only if you configured the codec g722-64k command in telephony-service configuration mode.

g722CodecSupport —Default: 0, phone default set by
                                                   					 manufacturer and equal to enabled or disabled.

Cisco
                                                   					 phone firmware 8.2.1 or a later version is required to support the G.722-64K
                                                   					 codec on G.722-capable SCCP phones.

Cisco
                                                   					 phone firmware 8.3.1 or a later version is required to support the G.722-64K
                                                   					 codec on G.722-capable SIP phones.

For SCCP
                                                   					 only: This command can also be configured in ephone- template configuration
                                                   					 mode and applied to one or more SCCP phones.

Step 6

end

#### Example:

```
Router(config-telephony)# end
```

Exits the
                                             				telephony service configuration mode and enters privileged EXEC mode.

#### What to do next

If you have
                                       				SIP and SCCP phones connected to the same Cisco Unified CME, see Configure Codecs of Individual Phones for Calls Between Local Phones .

If you want to
                                       				configure individual phones to support some codec other than the system-level
                                       				codec or some codec other than the phone s native codec, see Configure Codecs of Individual Phones for Calls Between Local Phones .

If you are
                                       				finished configuring SCCP phones to make basic calls, you are ready to generate
                                       				configuration files for the phones to be connected. See Generate Configuration Files for SCCP Phones .

### Configure Codecs
                           	 of Individual Phones for Calls Between Local Phones

To designate a
                                 		  codec for individual phones to ensure connectivity between a variety of phones
                                 		  connected to the same Cisco Unified CME router, perform the following steps for
                                 		  each SCCP or SIP phone.

Restriction

Not all
                                                   				  phones support all codecs. To verify whether your phone supports a particular
                                                   				  codec, see your phone documentation.

For SIP and
                                                   				  SCCP phones in Cisco Unified CME: Modify the configuration for either SIP or
                                                   				  SCCP phones to ensure that the codec for all phones match. Do not modify the
                                                   				  configuration for both SIP and SCCP phones.

If G.729 is
                                                   				  the desired codec for Cisco ATA-186 and Cisco ATA-188, then only one port of
                                                   				  the Cisco ATA device should be configured in Cisco Unified CME. If a call is
                                                   				  placed to the second port of the Cisco ATA device, it will be disconnected
                                                   				  gracefully. If you want to use both Cisco ATA ports simultaneously, then
                                                   				  configure G.711 in Cisco Unified CME.

If G.722-64K
                                                   				  or iLBC codecs are configured in ephone configuration mode and the phone does
                                                   				  not support the codec, the fallback is the global codec or G.711ulaw if the
                                                   				  global codec is not supported. To configure a global codec, see Modify the Global Codec .

#### Before you begin

For SIP phones
                                       				in Cisco Unified CME: Cisco Unified CME 3.4 or a later version.

For G.722-64K
                                       				and iLBC codecs: Cisco Unified CME 4.3 or a later version.

To support
                                       				G.722-64K on an individual phone: Cisco phone firmware 8.2.1 or a later version
                                       				for SCCP phones and 8.3.1 or a later version for SIP phones. For information
                                       				about upgrading Cisco phone firmware, see Install Cisco Unified CME Software .

To support
                                       				iLBC on an individual phone: Cisco phone firmware 8.3.1 or a later version for
                                       				SCCP and SIP phones. For information about upgrading Cisco phone firmware, see Install Cisco Unified CME Software .

Cisco Unified IP phone to which the codec is to be applied must
                                       				be already configured. For configuration information for SIP phones, see Assign Directory Numbers to SIP Phones .
                                       				For configuration information for SCCP phones, see Assign Directory Numbers to SCCP Phones .

### SUMMARY STEPS

- enable

- configure terminal

- ephone ephone-tag or voice register pool pool-tag

- codec codec-type

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

Enter
                                                   					 your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ephone ephone-tag or voice register pool pool-tag

#### Example:

```
Router(config)# voice register pool 1
```

Enters ephone
                                             				configuration mode to set phone-specific parameters for a SCCP phone in Cisco
                                             				Unified CME.

or

Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone in Cisco Unified CME.

Step 4

codec codec-type

#### Example:

```
Router(config-ephone)# codec g729r8 
or 
Router(config-register-pool)# codec g711alaw
```

Specifies the
                                             				codec for the dial peer for the IP phone being configured.

codec-type —Type ? for a list of codecs.

This
                                                   					 command overrides any previously configured codec selection set with the voice-class codec command.

This
                                                   					 command overrides any previously configured codec selection set with the codec command
                                                   					 in telephony-service configuration mode.

SCCP
                                                   					 only—This command can also be configured in ephone-template configuration mode
                                                   					 and applied to one or more phones.

Step 5

end

#### Example:

```
Router(config-ephone)# end
```

or

```
Router(config-register-pool)# end
```

Exits the
                                             				configuration mode and enters privileged EXEC mode.

#### What to do next

If you want
                                       				to select the session-transport protocol for a SIP phone, see Select Session-Transport Protocol for a SIP Phone .

If you are
                                       				finished configuring SIP phones to make basic calls, you are ready to generate
                                       				configuration files for the phones to be connected. See Generate Configuration Profiles for SIP Phones .

If you are
                                       				finished configuring SCCP phones to make basic calls, you are ready to generate
                                       				configuration files for the phones to be connected. See Generate Configuration Files for SCCP Phones .

## Configure Phones for a Key System

### Creating Directory
                           	 Numbers for a Simple Key System on SCCP Phone

To create a set of
                                 		  directory numbers with the same number to be associated with multiple line
                                 		  buttons on an IP phone and provide support for call waiting and call transfer
                                 		  on a key system phone, perform the following steps.

Restriction

Do not
                                                   				  configure directory numbers for a key system for dual-line mode because this
                                                   				  does not conform to the key system one-call-per-line button usage model for
                                                   				  which the phone is designed.

Provisioning
                                                   				  support for the Cisco Unified IP Phone 7931 is available only in
                                                   				  Cisco Unified CME 4.0(2) and later versions.

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn dn-tag

- number number [ secondary number ] [ no-reg [ both | primary ] ]

- preference preference-order

- no huntstop or huntstop

- mwi-type { visual | audio | both }

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
Router(config)# ephone-dn 11
```

Enters
                                             				ephone-dn configuration mode to create a directory number.

Step 4

number number [ secondary number ] [ no-reg [ both | primary ] ]

#### Example:

```
Router(config-ephone-dn)# number 101
```

Configures a
                                             				valid phone or extension number for this directory number.

Step 5

preference preference-order

#### Example:

```
Router(config-ephone-dn)# preference 1
```

Sets dial-peer
                                             				preference order for a directory number associated with a Cisco Unified IP
                                             				phone.

Default:
                                                   					 0.

Increments
                                                   					 the preference order for all subsequent instances within a set of ephone dns
                                                   					 with the same number to be associated with a key system phone. That is, the
                                                   					 first instance of the directory number is preference 0 by default
                                                   					 and you must specify 1 for the
                                                   					 second instance of the same number, 2 for the
                                                   					 next, and so on. This allows you to create multiple buttons with the same
                                                   					 number on an IP phone.

Required
                                                   					 to support call waiting and call transfer on a key system phone.

Step 6

no huntstop or huntstop

#### Example:

```
Router(config-ephone-dn)# no huntstop
```

or

```
Router(config-ephone-dn)# huntstop
```

Explicitly
                                             				enables call hunting behavior for a directory number.

Configure no huntstop for all instances, except the final instance, within a set of ephone dns with
                                                   					 the same number to be associated with a key system phone.

Required
                                                   					 to allow call hunting across multiple line buttons with the same number on an
                                                   					 IP phone.

or

Disables call
                                             				hunting behavior for a directory number.

Configure
                                                   					 the huntstop command for the final instance within a set of ephone dns with the same number
                                                   					 to be associated with a key system phone.

Required
                                                   					 to limit the call hunting to a set of multiple line buttons with the same
                                                   					 number on an IP phone.

Step 7

mwi-type { visual | audio | both }

#### Example:

```
Router(config-ephone-dn)# mwi-type audible
```

Specifies
                                             				the type of MWI notification to be received.

This
                                                   					 command is supported only by Cisco Unified IP Phone 7931s and Cisco Unified IP
                                                   					 Phone 7911s.

This
                                                   					 command can also be configured in ephone-dn-template configuration mode. The
                                                   					 value set in ephone-dn configuration mode has priority over the value set in
                                                   					 ephone-dn-template mode.

Step 8

end

#### Example:

```
Router(config-ephone-dn)# end
```

Exits to
                                             				privileged EXEC mode.

#### What to do next

The following
                                 		  example shows the configuration for six instances of directory number 101,
                                 		  assigned to the first six buttons of an IP phone:

```
ephone-dn 10 
			  number 101 
			  no huntstop 
			 
			 ephone-dn 11 
			  number 101 
			  preference 1 
			  no huntstop 
			 
			 ephone-dn 12 
			  number 101 
			  preference 2
			  no huntstop
			  
			 ephone-dn 13 
			  number 101
			  preference 3
			  no huntstop 
			 
			 ephone-dn 14 
			  number 101
			  preference 4 
			  no huntstop 
			 
			 ephone-dn 15 
			  number 101 
			  preference 5
			 
			 ephone 1 
			  mac-address 0001.2345.6789> 
			  type 7931 
			  button 1:10 2:11 3:12 4:13 5:14 6:15
```

### Configure Trunk Lines for a Key System on SCCP Phone

To set up trunk lines for your key system, perform only one of the
                              		following procedures:

To only enable direct status monitoring of the FXO port on the line button of the IP phone, see Configure a Simple Key System Phone Trunk Line Configuration on SCCP Phone .

To enable direct status monitoring and allow transferred PSTN FXO line calls to be automatically recalled if the transfer
                                    target does not answer, see Configure an Advanced Key System Phone Trunk Line Configuration on SCCP Phone .

#### Configure a Simple
                              	 Key System Phone Trunk Line Configuration on SCCP Phone

Perform the steps
                                    		  in this section to:

Create
                                          				directory numbers corresponding to each FXO line that allows phones to have
                                          				shared or private lines connected directly to the PSTN.

Enable direct
                                          				status monitoring of the FXO port on the line button of the IP phone. The line
                                          				button indicator, either a lamp or an icon depending on the phone, shows the
                                          				in-use status of the FXO port during the duration of the call.

Restriction

Directory
                                                      				  number with a trunk line cannot be configured for call forward, busy, or no
                                                      				  answer.

Numbers
                                                      				  entered after a trunk line is seized will not be displayed. Only the trunk tag
                                                      				  is displayed on IP phones.

Numbers
                                                      				  entered after trunk line is seized will not appear in call history or call
                                                      				  detail records (CDRs) of a Cisco Unified CME router. Only the trunk tag is
                                                      				  logged for calls made from trunk lines.

FXO trunk
                                                      				  lines do not support the CFwdALL, Transfer, Pickup, GPickUp, Park, CallBack,
                                                      				  and NewCall softkeys.

FXO trunk
                                                      				  lines do not support conference initiator dropoff.

FXO trunk
                                                      				  lines do not support on-hook redial. The phone user must explicitly select the
                                                      				  FXO trunk line before pressing the Redial button.

FXO trunk
                                                      				  lines do not support call transfer to IP phones. However, the call initiator
                                                      				  can conference an FXO line with an IP phone by pressing the Hold button, which
                                                      				  leaves the FXO trunk line and IP phone connected. The conference initiator is
                                                      				  unable to participate in the conference, but can place calls on other lines.

FXO trunk
                                                      				  lines do not support bulk speed dial.

FXO port
                                                      				  monitoring has the following restrictions:

Not
                                                            						supported before Cisco Unified CME 4.0.

Supported only for analog FXO loop-start and ground-start ports
                                                            						and T1/E1 FXO CAS ports. FXS loop-start and ground-start ports and PRI/BRI PSTN
                                                            						trunks are not supported.

Not
                                                            						supported for analog ports on the Cisco VG224 or Cisco ATA 180 Series.

T1 CAS
                                                            						DS0 group must be configured per time slot (cannot bundle more than one time
                                                            						slot into a ds0-group).

Transfer
                                                      				  recall and transfer-to button optimization are supported on dual-line directory
                                                      				  numbers only in Cisco Unified CME 4.0 and later versions.

Transfer-to
                                                      				  button optimization is not supported for call forwarding, call-park recall,
                                                      				  call pickup on hold, or call pickup at alert.

##### Before you begin

FXO port for
                                          				a private line automatic ringdown (PLAR) off-premises extension (OPX)
                                          				connection must be configured; for example:

```
voice-port 1/0/0 
 connection p lar-opx 801 <<----Private number
```

Dial peers
                                          				for FXO port must be configured; for example:

```
dial-peer voice 111 pots
 destination-pattern 811 <<----Trunk-tag
 port 1/0/0
```

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn dn-tag

- number number [ secondary number ] [ no-reg [ both | primary ] ]

- trunk trunk-tag [ timeout seconds ] monitor-port port

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

Enter
                                                      					 your password if prompted.

Step 2

configure terminal

##### Example:

```
Router# configure terminal
```

Enters global
                                                				configuration mode.

Step 3

ephone-dn dn-tag

##### Example:

```
Router(config)# ephone-dn 51
```

Enters
                                                				ephone-dn configuration mode to create a directory number.

Configure this command in the default single line mode, without
                                                      					 the dual-line keyword, when configuring a simple key system trunk line.

Step 4

number number [ secondary number ] [ no-reg [ both | primary ] ]

##### Example:

```
Router(config-ephone-dn)# number 801
```

Configures a
                                                				valid phone or extension number for this directory number.

Step 5

trunk trunk-tag [ timeout seconds ] monitor-port port

##### Example:

```
Router(config-ephone-dn)# trunk 811 monitor-port 1/0/0
```

Associates a
                                                				directory number with an FXO port.

The monitor-port keyword is not supported before Cisco
                                                      					 Unified CME 4.0.

The monitor-port keyword is not supported on directory
                                                      					 numbers for analog ports on the Cisco VG224 or Cisco ATA 180 Series.

Step 6

end

##### Example:

```
Router(config-ephone-dn)# end
```

Returns to
                                                				privileged EXEC mode.

##### Examples

The following
                                    		  example shows the configuration for six instances of directory number 101,
                                    		  assigned to the first six buttons of an IP phone, plus four PSTN line
                                    		  appearances that are assigned to buttons 7 to 10:

```
ephone-dn 10
			  number 101  
			  no huntstop 
			
			 ephone-dn 11 
			  number 101 
			  preference 1 
			  no huntstop 
			 
			 ephone-dn 12 
			  number 101
			  preference 2 
			  no huntstop 
			 
			 ephone-dn 13
			  number 101 
			  preference 3 
			  no huntstop
			  
			 ephone-dn 14
			  number 101
			  preference 4 
			  no huntstop
			 
			 ephone-dn 15 
			  number 101
			  preference 5
			 
			 ephone-dn 51 
			  number 801 
			  trunk 811 monitor-port 1/0/0> 
			 
			 ephone-dn 52
			  number 802 
			  trunk 812 monitor-port 1/0/1 
			 
			 ephone-dn 53 
			  number 803 
			  trunk 813 monitor-port 1/0/2
			 
			 ephone-dn 54
			  number 804 
			  trunk 814 monitor-port 1/0/3 
			
			 ephone 1  
			  mac-address 0001.2345.6789 
			  type 7931
			  button 1:11 2:12 3:13 4:14 5:15 6:16 7:51 8:52 9:53 10:54 
			
			 voice-port 1/0/0
			  connection plar opx 801
			 
			 voice-port 1/0/1
			  connection plar opx 802
			 
			 voice-port 1/0/2 
			  connection plar opx 803 
			  
			 voice-port 1/0/3
			  connection plar opx 804 
			 
			 dial-peer voice 811 pots 
			  destination-pattern 811 
			  port 1/0/0 
			 
			 dial-peer voice 812 pots 
			  destination-pattern 812 
			  port 1/0/1 
			 
			 dial-peer voice 813 pots
			  destination-pattern 813
			  port 1/0/2
			  
			 dial-peer voice 814 pots 
			  destination-pattern 814 
			  port 1/0/3
```

##### What to do next

You are ready to
                                    		  configure each individual phone and assign button numbers, line
                                    		  characteristics, and directory numbers to buttons on the phone. See Configure Individual IP Phones for Key System on SCCP Phone .

#### Configure an
                              	 Advanced Key System Phone Trunk Line Configuration on SCCP Phone

Perform the steps
                                    		  in this section to:

Create
                                          				directory numbers corresponding to each FXO line that allows phones to have
                                          				shared or private lines connected directly to the PSTN.

Enable direct
                                          				status monitoring of the FXO port on the line button of the IP phone. The line
                                          				button indicator, either a lamp or an icon depending on the phone, shows the
                                          				in-use status of the FXO port during the duration of the call.

Allow
                                          				transferred PSTN FXO line calls to be automatically recalled if the transfer
                                          				target does not answer after the specified number of seconds. The call is
                                          				withdrawn from the transfer-to phone and the call resumes ringing on the phone
                                          				that initiated the transfer.

Restriction

Ephone-dn
                                                      				  with a trunk line cannot be configured for call forward, busy, or no answer.

Numbers
                                                      				  entered after a trunk line is seized will not be displayed. Only the trunk tag
                                                      				  is displayed on IP phones.

Numbers
                                                      				  entered after a trunk line is seized will not appear in call history or call
                                                      				  detail records (CDRs) of a Cisco Unified CME router. Only the trunk tag is
                                                      				  logged for calls made from trunk lines.

FXO trunk
                                                      				  lines do not support the CFwdALL, Transfer, Pickup, GPickUp, Park, CallBack,
                                                      				  and NewCall softkeys.

FXO trunk
                                                      				  lines do not support conference initiator dropoff.

FXO trunk
                                                      				  lines do not support on-hook redial. The phone user must explicitly select the
                                                      				  FXO trunk line before pressing the Redial button.

FXO trunk
                                                      				  lines do not support call transfer to IP phones. However, the call initiator
                                                      				  can conference an FXO line with an IP phone by pressing the Hold button, which
                                                      				  leaves the FXO trunk line and IP phone connected. The conference initiator is
                                                      				  unable to participate in the conference, but can place calls on other lines.

FXO trunk
                                                      				  lines do not support bulk speed dial.

FXO port
                                                      				  monitoring has the following restrictions:

Not
                                                            						supported before Cisco Unified CME 4.0.

Supported only for analog FXO loop-start and ground-start ports
                                                            						and T1/E1 FXO CAS ports. FXS loop-start and ground-start ports and PRI/BRI PSTN
                                                            						trunks are not supported.

Not
                                                            						supported for analog ports on the Cisco VG224 or Cisco ATA 180 Series.

T1 CAS
                                                            						DS0 group must be configured per time slot (cannot bundle more than one time
                                                            						slot into a ds0-group).

Transfer
                                                      				  recall and transfer-to button optimization is supported on dual-line directory
                                                      				  numbers only in Cisco Unified CME 4.0 and later.

Transfer-to
                                                      				  button optimization is not supported for call forwarding, call-park recall,
                                                      				  call pickup on hold, or call pickup at alert.

Transfer
                                                      				  recall is not supported for analog ports on the Cisco VG224 or Cisco ATA 180
                                                      				  Series.

##### Before you begin

```
voice-port 1/0/0
 connection plar-opx 801 <<----Private number
```

```
dial-peer voice 111 pots
 destination-pattern 811 <<----Trunk-tag
 port 1/0/0
```

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn dn-tag dual-line

- number number [ secondary number ] [ no-reg [ both | primary ] ]

- trunk digit-string [ timeout seconds ] [ transfer-timeout seconds ] [ monitor-port port ]

- huntstop [ channel ]

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

ephone-dn dn-tag dual-line

##### Example:

```
Router(config)# ephone-dn 51 dual-line
```

Enters
                                                				ephone-dn configuration mode for the purpose of creating and configuring a
                                                				telephone or extension number.

dual-line —Required when configuring an advanced
                                                      					 key system phone trunk line. Dual-line mode provides a second call channel for
                                                      					 the directory number on which to place an outbound consultation call during the
                                                      					 call transfer attempt. This also allows the phone to remain part of the call to
                                                      					 monitor the progress of the transfer attempt and if the transfer is not
                                                      					 answered, to pull the call back to the phone on the original PSTN line button.

Step 4

number number [ secondary number ] [ no-reg [ both | primary ] ]

##### Example:

```
Router(config-ephone-dn)# number 801
```

Configures a
                                                				valid telephone number or extension number for this directory number.

Step 5

trunk digit-string [ timeout seconds ] [ transfer-timeout seconds ] [ monitor-port port ]

##### Example:

```
Router(config-ephone-dn)# trunk 811 transfer-timeout 30 monitor-port 1/0/0
```

Associates
                                                				this directory number with an FXO port.

transfer-timeout seconds —For dual-line ephone-dns only. Range: 5 to 60000.
                                                      					 Default: Disabled.

The monitor-port keyword is not supported before Cisco
                                                      					 Unified CME 4.0.

The monitor-port and transfer-timeout keywords are not supported on
                                                      					 directory numbers for analog ports on the Cisco VG224 or Cisco ATA 180 Series.

Step 6

huntstop [ channel ]

##### Example:

```
Router(config-ephone-dn)# huntstop channel
```

Disables
                                                				call hunting to the second channel of this directory number if the first
                                                				channel is busy or does not answer.

channel —Required when configuring an advanced key
                                                      					 system phone trunk line. Reserves the second channel created by configuring
                                                      					 dual-line mode for the ephone-dn command so that an outbound consultation call can be placed during a call
                                                      					 transfer attempt.

Step 7

end

##### Example:

```
Router(config-ephone-dn)# end
```

Exits to
                                                				privileged EXEC mode.

##### Examples

The following
                                    		  example shows the configuration for six instances of directory number 101,
                                    		  assigned to the first six buttons of an IP phone, plus four PSTN line
                                    		  appearances that are assigned to buttons 7 to 10. These four PSTN line
                                    		  appearances are configured as dual lines to provide a second call channel on
                                    		  which to place an outbound consultation call during a call transfer attempt.
                                    		  This configuration allows the phone to remain part of the call to monitor the
                                    		  progress of the transfer attempt, and if the transfer is not answered, to pull
                                    		  the call back to the phone on the original PSTN line button.

```
ephone-dn 10 
			  number 101  
			  no huntstop
			
			 ephone-dn 11 
			  number 101 
			  preference 1 
			  no huntstop 
			  
			 ephone-dn 12 
			  number 101 
			  preference 2 
			  no huntstop 
			   
			 ephone-dn 13 
			  number 101 
			  preference 3
			  no huntstop 
			  
			 ephone-dn 14 
			  number 101 
			  preference 4 
			  no huntstop
			  
			 ephone-dn 15 
			  number 101
			  preference 5 
			 
			 ephone-dn 51 dual-line 
			  number 801 
			  trunk 811 transfer-timeout 30 monitor-port 1/0/0 
			  huntstop channel 
			 
			 ephone-dn 52 dual-line
			  number 802 
			  trunk 812 transfer-timeout 30 monitor-port 1/0/1 
			  huntstop channel 
			  
			 ephone-dn 53 dual-line
			  number 803 
			  trunk 813 transfer-timeout 30 monitor-port 1/0/2 
			  huntstop channel 
			  
			 ephone-dn 54 dual-line
			  number 804> 
			  trunk 814 transfer-timeout 30 monitor-port 1/0/3 
			  huntstop channel 
			  
			 ephone 1  
			  mac-address 0001.2345.6789 
			  type 7931 
			  button 1:11 2:12 3:13 4:14 5:15 6:16 7:51 8:52 9:53 10:54 
			  
			 voice-port 1/0/0 
			  connection plar opx 801 
			  
			 voice-port 1/0/1 
			  connection plar opx 802 
			 
			 voice-port 1/0/2 
			  connection plar opx 803 
			  
			 voice-port 1/0/3
			  connection plar opx 804 
			  
			 dial-peer voice 811 pots 
			  destination-pattern 811 
			  port 1/0/0 
			  
			 dial-peer voice 812 pots 
			  destination-pattern 812 
			  port 1/0/1 
			 
			 dial-peer voice 813 pots 
			  destination-pattern 813 
			  port 1/0/2 
			  
			 dial-peer voice 814 pots 
			  destination-pattern 814 
			  port 1/0/3
```

### Configure
                           	 Individual IP Phones for Key System on SCCP Phone

To assign button
                                 		  numbers, line characteristics, and directory numbers to buttons on an
                                 		  individual phone that will operate as a key system phone, perform the following
                                 		  steps.

Restriction

Provisioning
                                                   				  for Cisco Unified IP Phone 7931G is available only in Cisco Unified CME 4.0(2)
                                                   				  and later versions.

Cisco Unified IP Phone 7931G can support only one call waiting
                                                   				  overlaid per directory number.

Cisco Unified IP Phone 7931G cannot support overlays that
                                                   				  contain directory numbers configured for dual-line mode.

### SUMMARY STEPS

- enable

- configure terminal

- ephone phone-tag

- mac-address [ mac-address ]

- type phone-type

- button button-number { separator } dn-tag [ ,dn-tag... ] [ button-number { x } overlay-button-number ] [ button-number... ]

- mwi-line line-number

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
Router(config)# ephone 1
```

Enters ephone
                                             				configuration mode.

Step 4

mac-address [ mac-address ]

#### Example:

```
Router(config-ephone)# mac-address 0001.2345.6789
```

Specifies the
                                             				MAC address of the IP phone that is being configured.

Step 5

type phone-type

#### Example:

```
Router(config-ephone)# type 7931
```

Specifies the
                                             				type of phone that is being configured.

Step 6

button button-number { separator } dn-tag [ ,dn-tag... ] [ button-number { x } overlay-button-number ] [ button-number... ]

#### Example:

```
Router(config-ephone)# button 1:11 2:12 3:13 4:14 5:15 6:16 7:51 8:52 9:53 10:54
```

Associates a
                                             				button number and line characteristics with an ephone-dn. Maximum number of
                                             				buttons is determined by phone type.

Tip

The line
                                                         				  button layout for the Cisco Unified IP Phone 7931G is a bottom-up array. Button
                                                         				  1 is at the bottom right of the array and button 24 is at the top left of the
                                                         				  array.

Step 7

mwi-line line-number

#### Example:

```
Router(config-ephone)# mwi-line 3
```

Selects a
                                             				phone line to receive MWI treatment; when a message is waiting for the selected
                                             				line, the message waiting indicator is activated.

line-number —Range: 1 to 34. Default: 1.

Step 8

end

#### Example:

```
Router(config-ephone)# end
```

Exits ephone
                                             				configuration mode and enters privileged EXEC mode.

#### What to do next

If you have
                                       				SIP and SCCP phones connected to the same Cisco Unified CME, see Configure Codecs of Individual Phones for Calls Between Local Phones .

To select a
                                       				fixed-button layout for a Cisco Unified IP Phone 7931G, see Select Button Layout for a Cisco Unified SCCP IP Phone 7931G .

If you are
                                       				finished configuring phones to make basic calls, you are ready to generate
                                       				configuration files for the phones to be connected. See Generate Configuration Files for SCCP Phones .

## Configure Cisco
                        	 ATA, Analog Phone Support, Remote Phones, Cisco IP Communicator, and Secure IP
                        	 Phone (IP-STE)

### Configure Cisco ATA Support in SCCP Mode

To enable an analog phone that uses a Cisco ATA to register with Cisco Unified CME, perform the following steps.

Restriction

Step 1

Install the Cisco ATA.

See the Installing the Cisco ATA chapter in Cisco ATA 186 and Cisco ATA 188 Analog Telephone Adaptor Administrator's Guide for SCCP (version 3.0) .

Step 2

Configure the Cisco ATA.

See the Configuring the Cisco ATA for SCCP chapter in Cisco ATA 186 and Cisco ATA 188 Analog Telephone Adaptor Administrator's Guide for SCCP (version 3.0) .

Step 3

Upgrade the firmware to the latest Cisco ATA image.

If you are using either the v2.14 or v2.14ms Cisco ATA 186 image based on the 2.14 020315a build for H.323/SIP or the 2.14 020415a
                                             build for MGCP or SCCP, you must upgrade to the latest version to install a security patch. This patch fixes a security hole
                                             in the Cisco ATA Web server that allows users to bypass the user interface password.

For information about upgrading firmware, see Install Cisco Unified CME Software . Alternatively, you can use a manual method, as described in the Upgrading the Cisco ATA Signaling Image chapter of Cisco ATA 186 and Cisco ATA 188 Analog Telephone Adaptor Administrator's Guide for SCCP (version 3.0) .

Step 4

Set the following network parameters on the Cisco ATA:

DHCP parameter to 1 (enabled).

TFTP parameter to 1 (enabled).

TFTPURL parameter to the IP address of the router running Cisco Unified CME.

SID0 parameter to a period ( . ) or the MAC address of the Cisco ATA (to enable the first port).

SID1 parameter to a period ( . ) or a modified version the Cisco ATA’s MAC address, with the first two hexadecimal numbers removed and 01 appended to the
                                                   end, if you want to use the second port. For example, if the MAC address of the Cisco ATA is 00012D01073D, set SID1 to 012D01073D01.

Nprintf parameter to the IP address and port number of the host to which all Cisco ATA debug messages are sent. The port number
                                                   is usually set to 9001.

To prevent tampering and unauthorized access to the Cisco ATA 186, you can disable the web-based configuration. However, if
                                                   you disable the web configuration page, you must use either a TFTP server or the voice configuration menu to configure the
                                                   Cisco ATA 186.

Step 5

In Cisco Unified CME, configure analog phones that use a Cisco ATA in the same way as a Cisco Unified IP phone. In the type command, use the ata keyword. For information on how to provision phones, see Create Directory Numbers for SCCP Phones .

#### What to do next

If you have SIP and SCCP phones connected to the same Cisco Unified CME, see Configure Codecs of Individual Phones for Calls Between Local Phones .

To select a fixed-button layout for a Cisco Unified IP Phone 7931G, see Select Button Layout for a Cisco Unified SCCP IP Phone 7931G .

If you are finished configuring phones to make basic calls, you are ready to generate configuration files for the phones to
                                       be connected. See Generate Configuration Files for SCCP Phones and Generate Configuration Profiles for SIP Phones .

### Configure Cisco ATA Support in SIP Mode

Cisco ATA 187, 190, and 191 support SIP mode. To enable an analog phone that uses a Cisco ATA 191 to register with Unified CME,
                                 perform the following steps.

Restriction

For a Cisco ATA that is registered to a Unified CME system to participate in fax calls, it must have its ConnectMode parameter
                                                   set to use the same RTP payload type as the Cisco voice gateway that is performing the Fax pass-through. Cisco voice gateways
                                                   use standard payload type 0/8, which is selected on Cisco ATAs by setting bit 2 of the ConnectMode parameter to 1. For more
                                                   information, see the Configure Fax Services chapter in Cisco ATA 191 Analog Telephone Adapter Administration Guide for Cisco Unified Communications Manager .

If both ports of a Cisco ATA 191 are configured as shared line, then a call put on hold on one port cannot be resumed at the
                                                   other port.

Step 1

Install the Cisco ATA.

See the Install the ATA 191 chapter in Cisco ATA 191 Analog Telephone Adapter Administration Guide for Cisco Unified Communications Manager .

Step 2

Configure the Cisco ATA.

See the Configure the ATA 191 chapter in Cisco ATA 191 Analog Telephone Adapter Administration Guide for Cisco Unified Communications Manager .

Step 3

Upgrade the firmware to the latest Cisco ATA image. For more information, see Configure Firmware Upgrade for ATA in SIP Mode .

Step 4

In Cisco Unified CME, configure analog phones that use a Cisco ATA in the same way as a Cisco Unified IP phone. In the type command that is configured under voice register pool configuration mode, use the ATA-191 keyword. For information on how to provision phones, see Create Directory Numbers for SIP Phones .

#### Configure Firmware Upgrade for ATA in SIP Mode

Cisco ATA 187, 190, and 191 support SIP mode. To configure firmware upgrade for ATA 190 in SIP mode with Unified CME, perform
                                    the following steps.

You can specify the Cisco ATA 191 phone type using the CLI command type as shown:

```
Router(config)# voice register pool 1
Router(config-register-pool)# type ATA-191
```

Step 1

Copy the firmware files to router flash memory.

For example, ATA190.1-1-2-005.loads and ATA190.1-1-2-005.bin.sgn are firmware files for ATA 190.

The firmware file for ATA 12.0(1) tat is supported in Unified CME is cmterm-ata191.12-0-1SR1-1.zip.

Step 2

Create TFTP bindings for the firmware files.

```
Router(confg)#tftp-server Flash:ATA190.1-1-2-005.bin.sgn
Router(confg) tftp-server Flash:ATA190.1-1-2-005.loads
```

Step 3

Specify the load using loads command under voice register global configuration mode.

```
Router(confg)#voice register global
Router(confg-register-global) load ATA-190 ATA190.1-1-2-005
```

Step 4

Configure a pool for ATA phone to be upgraded.

Step 5

Create CNF files using create profile CLI command under voice register global configuration mode.

Step 6

Restart the ATA by unplugging and re-plugging or by executing the reset command.

Cisco ATA 190/191 takes around 5 mins to upgrade the firmware.

```
Router#show voice register pool phone-load
Pool Device Name      Current-Version         Previous-Version
==== ===========      ================        ================
1    SEP34DB²D18001C  Cisco/ATA190-1.1.2(005) Cisco/ATA190-1.1.1(003)
```

### Verify Cisco ATA Support

Use the show ephone ata command to display SCCP phone configurations with the type ata command.

The following is sample output for a Cisco Unified CME configured for
                              		two analog phones using a Cisco ATA with MAC address 000F.F758.E70E:

```
ephone-30 Mac:000F.F758.E70E TCP socket:[2] activeLine:0 REGISTERED in SCCP ver 1 and Server in ver 1
	 mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0 caps:7
	 IP:1.4.188.72 15325 ATA Phone  keepalive 7 max_line 2 dual-line
	 button 1: dn 80 number 8080 CH1   IDLE         CH2 IDLE 
	 
	 ephone-31 Mac:0FF7.58E7.0E01 TCP socket:[3] activeLine:0 REGISTERED in SCCP ver 1 and Server in ver 1
	 mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0 caps:3
	 IP:1.4.188.72 15400 ATA Phone  keepalive 7 max_line 2 dual-line
	 button 1: dn 81 number 8081 CH1   IDLE         CH2 IDLE
```

### Troubleshooting Cisco ATA Support

Use the debug ephone detail command to diagnose problems with analog phones that
                                 		  use Cisco ATAs.

### Call Pickup and
                           	 Group Call Pickup with Cisco ATA

Most of the
                              		procedures for using Cisco ATAs with Cisco Unified CME are the same as those
                              		for using Cisco ATAs with Cisco Unified Communications Manager, as described in
                              		the How to Use
                                 		  Pre-Call and Mid-Call Services chapter of Cisco ATA 186 and Cisco ATA
                                 		  188 Analog Telephone Adaptor Administrator’s Guide for SCCP (version
                                 		  3.0) . However, the call pickup and group call pickup procedures are
                              		different when using Cisco ATAs with Cisco Unified CME, as described below:

#### Call Pickup

When using Cisco
                                 		  ATAs with Cisco Unified CME:

To pickup the
                                       				last parked call, press **3* .

To pickup a
                                       				call on a specific extension, press **3 and enter
                                       				the extension number.

To pickup a
                                       				call from a park slot, press **3 and enter
                                       				the park slot number.

#### Group Call
                                 		  Pickup

When using Cisco
                                 		  ATAs with Cisco Unified CME:

To answer a
                                       				phone within your call pickup group, press **4* .

To answer a
                                       				phone outside of your call pickup group, press **4 and the
                                       				group ID number.

If there is only
                                             			 one pickup group, you do not need to enter the group ID after the **4 to pickup
                                             			 a call.

### Configure Voice
                           	 and T.38 Fax Relay on Cisco ATA-187

Restriction

H.323 trunk
                                                   				  calls are not supported.

Hardware
                                                   				  conferencing with DSPFarm resource is not supported on Cisco ATA-187 in Cisco
                                                   				  Unified CME 9.0. With the correct firmware (9.2(3) or a later version), local
                                                   				  three-way conferencing is supported.

#### Before you begin

Cisco Unified CME
                                 		  9.0 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- authenticate realm string

- exit

- voice service { voip | voatm }

- allow-connections from-type to to-type

- fax protocol t38 [ ls_redundancy value [ hs_redundancy value ] ] [ fallback { cisco | none | pass-through { g711ulaw | g711alaw } } ]

- exit

- voice register pool pool-tag

- id mac address

- type phone-type

- ata-ivr-pwd password

- session-transport { tcp | udp }

- number tag dn dn-tag

- username username [ password password ]

- codec codec-type [ bytes ]

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

voice register global

#### Example:

```
Router(config)# voice register global
```

Enters voice
                                             				register global configuration mode.

Step 4

authenticate realm string

#### Example:

```
Router(config-register-global)# authenticate realm xxxxx
```

realm string —Realm parameter for challenge and response
                                                   					 as specified in RFC 2617 is authenticated.

Step 5

exit

#### Example:

```
Router(config-register-global)# exit
```

Exits voice
                                             				register global configuration mode.

Step 6

voice service { voip | voatm }

#### Example:

```
Router(config)# voice service voip
```

Enters
                                             				voice-service configuration mode to specify a voice encapsulation type.

voip —Specifies Voice over IP (VoIP) parameters.

voatm —Specifies Voice over ATM (VoATM) parameters.

Step 7

allow-connections from-type to to-type

#### Example:

```
Router(config-voi-serv)# allow-connections sip to sip
```

Allows
                                             				connections between specific types of endpoints in a VoIP network.

from-type —Originating endpoint type. The following
                                                   					 choices are valid:

sip —Session Interface Protocol.

to —Indicates that the argument that follows is the
                                                   					 connection target.

to-type —Terminating endpoint type. The following
                                                   					 choices are valid:

sip —Session
                                                         						  Interface Protocol.

Step 8

fax protocol t38 [ ls_redundancy value [ hs_redundancy value ] ] [ fallback { cisco | none | pass-through { g711ulaw | g711alaw } } ]

#### Example:

```
Router(config-voi-serv)# fax protocol t38 ls-redundancy 0 hs-redundancy 0 fallback pass-through g711ulaw
```

Specifies
                                             				the global default ITU-T T.38 standard fax protocol to be used for all VoIP
                                             				dial peers.

ls_redundancy value —(Optional) (T.38 fax relay only) Specifies
                                                   					 the number of redundant T.38 fax packets to be sent for the low-speed
                                                   					 V.21-based T.30 fax machine protocol. Range varies by platform from 0 (no
                                                   					 redundancy) to 5 or 7. Default is 0.

hs_redundancy value —(Optional) (T.38 fax relay only) Specifies
                                                   					 the number of redundant T.38 fax packets to be sent for high-speed V.17, V.27,
                                                   					 and V.29 T.4 or T.6 fax machine image data. Range varies by platform from 0 (no
                                                   					 redundancy) to 2 or 3. Default is 0.

fallback —(Optional) A fallback mode is used to
                                                   					 transfer a fax across a VoIP network if T.38 fax relay could not be
                                                   					 successfully negotiated at the time of the fax transfer.

pass-through —(Optional) The fax stream uses one of
                                                   					 the following high-bandwidth codecs:

g711ulaw —Uses the G.711 u-law codec.

g711alaw —Uses the G.711 a-law codec.

Step 9

exit

#### Example:

```
Router(config-voi-serv)# exit
```

Exits
                                             				voice-service configuration mode.

Step 10

voice register pool pool-tag

#### Example:

```
Router(config)# voice register pool  11
```

Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a Cisco
                                             				Unified SIP phone in Cisco Unified CME.

pool-tag —Unique number assigned to the pool.
                                                   					 Range: 1 to 100.

Step 11

id mac address

#### Example:

```
Router(config-register-pool)# id mac 93FE.12D8.2301
```

identifies a
                                             				locally available Cisco Unified SIP IP phone.

mac address —Identifies the MAC address of a particular
                                                   					 Cisco Unified SIP IP phone.

Step 12

type phone-type

#### Example:

```
Router(config-register-pool)# type ATA-187
```

Defines a
                                             				phone type for the SIP phone being configured.

Step 13

ata-ivr-pwd password

#### Example:

```
Router(config-register-pool)# ata-ivr-pwd 1234
```

(Optional)
                                             				Defines a password to access interactive voice response (IVR) and change the
                                             				default phone settings on Cisco Analog Telephone Adaptors.

password —Four-digit or five-digit string to be
                                                   					 used as password to access IVR. Password string must contain numbers 0 to 9.

Step 14

session-transport { tcp | udp }

#### Example:

```
Router(config-register-pool)# session-transport tcp
```

(Optional)
                                             				Specifies the transport layer protocol that a Cisco Unified SIP IP phone uses
                                             				to connect to Cisco Unified CME.

tcp —Transmission Control Protocol (TCP) is used.

udp —User
                                                   					 Datagram Protocol (UDP) is used. This is the default.

Step 15

number tag dn dn-tag

#### Example:

```
Router(config-register-pool)# number 1 dn 33
```

Indicates
                                             				the E.164 phone numbers that the registrar permits to handle the Register
                                             				message from the Cisco Unified SIP IP phone.

tag —Identifies the telephone number when there are
                                                   					 multiple number commands. Range: 1 to 10.

dn dn-tag —Identifies the directory number tag for
                                                   					 this phone number as defined by the voice register dn command. Range: 1 to 150.

Step 16

username username [ password password ]

#### Example:

```
Router(config-register-pool)# username ata112 password cisco
```

Assigns an
                                             				authentication credential to a phone user so that the SIP phone can register in
                                             				Cisco Unified CME.

username —Username of the local Cisco IP phone
                                                   					 user. Default: Admin.

password —Enables password for the Cisco IP phone
                                                   					 user.

password —Password string.

Step 17

codec codec-type [ bytes ]

#### Example:

```
Router(config-register-pool)# codec g711ulaw
```

Specifies
                                             				the codec to be used when setting up a call for a SIP phone or group of SIP
                                             				phones in Cisco Unified CME.

codec-type —Preferred codec; values are as follows:

g711alaw —G.711 A law 64K bps.

g711ulaw —G.711 micro law 64K bps.

g722r64 —G.722-64K at 64K bps.

g729r8 —G.729 8K bps (default).

ilbc —
                                                         						  internet Low Bitrate Codec (iLBC) at 13,330 bps or 15,200 bps.

Step 18

end

#### Example:

```
Router(config-register-pool)# end
```

Exits to
                                             				privileged EXEC mode.

### Auto-Configuration
                           	 for Cisco VG202, VG204, and VG224

Restriction

#### Before you begin

Cisco Unified
                                       				CME 7.1 or a later version. The Cisco Unified CME router must be configured and
                                       				running before you boot the analog voice gateway. See Set Up Cisco Unified CME for SCCP Phones .

Default
                                       				location of configuration files is system:/its/. To define an alternate
                                       				location at which to save the gateway configuration files, see Define Per-Phone Configuration Files and Alternate Location for SCCP Phones .

To
                                       				automatically assign the next available directory number to the voice port as
                                       				it registers to Cisco Unified CME, and create an ephone entry associated with
                                       				each voice port, enable the auto assign command in Cisco Unified CME.

### SUMMARY STEPS

- enable

- configure terminal

- voice-gateway system tag

- mac-address mac-address

- type { vg202 | vg204 | vg224 }

- voice-port port-range

- network-locale locale-code

- create cnf-files

- reset or restart

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

voice-gateway system tag

#### Example:

```
Router(config)# voice-gateway system 1
```

Enters voice
                                             				gateway configuration mode and creates a voice gateway configuration.

Step 4

mac-address mac-address

#### Example:

```
Router(config-voice-gateway)# mac-address
```

Defines the
                                             				MAC address of the voice gateway to autoconfigure.

Step 5

type { vg202 | vg204 | vg224 }

#### Example:

```
Router(config-voice-gateway)# type vg224
```

Defines the
                                             				type of voice gateway to autoconfigure.

Step 6

voice-port port-range

#### Example:

```
Router(config-voice-gateway)# voice-port 0-23
```

Identifies the
                                             				ports on the voice gateway that register to Cisco Unified CME.

Step 7

network-locale locale-code

#### Example:

```
Router(config-voice-gateway)# network-locale FR
```

Selects a
                                             				geographically specific set of tones and cadences for the voice gateway s
                                             				analog endpoints that register to Cisco Unified CME.

Step 8

create cnf-files

#### Example:

```
Router(config-voice-gateway)# create cnf-files
```

Generates the
                                             				XML configuration files that are required for the voice gateway to
                                             				autoconfigure its analog ports that register to Cisco Unified CME.

Step 9

reset or restart

#### Example:

```
Router(config-voice-gateway)# reset
```

```
Router(config-voice-gateway)# restart
```

(Optional)
                                             				Performs a complete reboot of all analog phones associated with the voice
                                             				gateway and registered to Cisco Unified CME.

or

(Optional)
                                             				Performs a fast restart of all analog phones associated with the voice gateway
                                             				after simple changes to buttons, lines, or speed-dial numbers.

Use
                                                   					 these commands to download new configuration files to the analog phones after
                                                   					 making configuration changes to the phones in Cisco Unified CME.

Step 10

end

#### Example:

```
Router(config-voice-gateway)# end
```

Exits to
                                             				privileged EXEC mode.

#### Example

The following
                                 		  example shows the voice gateway configuration in Cisco Unified CME:

```
voice-gateway system  1 
			  network-locale FR
			  type VG224 
			  mac-address 001F.A30F.8331 
			  voice-port 0-23 
			  create cnf-files
```

#### What to do next

Cisco VG202
                                       				or VG204 voice gateway Enable the gateway for autoconfiguration. See the Auto-Configuration on the Cisco VG202 and Cisco VG204 Voice
                                          				  Gateways section in Cisco VG202 and Cisco VG204
                                          				  Voice Gateways Software Configuration Guide .

Cisco VG224
                                       				analog phone gateway Enable SCCP and the STC application on the gateway. See
                                       				the Configuring FXS Ports for Basic Calls chapter in Supplementary Services
                                          				  Features for FXS Ports on Cisco IOS Voice Gateways Configuration Guide .

### Configure Phones
                           	 on SCCP Controlled Analog (FXS) Ports

Configuring
                                 		  Cisco Unified CME to support calls and features on analog endpoints connected
                                 		  to SCCP controlled analog (FXS) ports is basically the same as configuring any
                                 		  SCCP phone in Cisco Unified CME. This section describes only the steps that
                                 		  have special meaning for phones connected to a Cisco VG224 Analog Phone
                                 		  Gateway.

Restriction

#### Before you begin

For phones
                                       				connected to analog FXS ports on the Cisco VG224 Analog Phone Gateway:
                                       				Cisco CME 3.2.2 or a later version.

For phones
                                       				connected to analog FXS ports on the Cisco Integrated Services Routers (ISR)
                                       				voice gateway: Cisco Unified CME 4.0 or a later version.

Cisco ISR
                                       				voice gateway or Cisco VG224 analog phone gateway is installed and configured
                                       				for operation. For information, see the appropriate Cisco configuration
                                       				documentation.

Prior to
                                       				Cisco IOS Release 12.4(11)T, set the timeouts
                                             					 ringing command to infinity for
                                       				all SCCP-controlled analog ports. In Cisco IOS Release 12.4(11)T and later, the
                                       				default for this command is infinity.

SCCP is
                                       				enabled on the Cisco IOS voice gateway. For configuration information, see Supplementary Services
                                          				  Features for FXS Ports on Cisco IOS Voice Gateways Configuration Guide .

Step 1

Set up
                                          			 ephone-dns for up to 24 endpoints on the Cisco IOS gateway.

Use the ephone-dn command:

#### Example:

```
ephone-dn 1 dual-line 
			  number 1000 
			 . 
			 . 
			 . 
			 ephone-dn 24 dual-line 
			  number 1024
```

Step 2

Set the
                                          			 maximum number of ephones.

Use the max ephones command to set a number equal to or greater than the total number of endpoints
                                             				that you intend to register on the Cisco Unified CME router, including both IP
                                             				and analog endpoints. For example, if you have 6 IP phones and 12 analog
                                             				phones, set the max ephones command to 18 or greater.

Step 3

Assign
                                          			 ephone-dns to ephones.

Use the auto assign command to enable the automatic assignment of an
                                             				available ephone-dn to each phone as the phone contacts the Cisco Unified CME
                                             				router to register.

auto assign 1 to 24 —You do not need to use the type keyword
                                                   					 if you have only analog endpoints to be assigned or if you want all endpoints
                                                   					 to be automatically assigned.

auto assign 1 to 24 type anl —Use the type keyword
                                                   					 if you have other phone types in the system and you want only the analog
                                                   					 endpoints to be assigned to ephone-dns automatically.

An alternative
                                             				to using the auto assign command is to manually assign ephone-dns to ephones (analog phones on FXS
                                             				ports). This method is more complicated, but you might need to use it if you
                                             				want to assign a specific extension number (ephone-dn) to a particular ephone.
                                             				The reason that manual assignment is more complicated is because a unique
                                             				device ID is required for each registering ephone and analog phones do not have
                                             				unique MAC addresses like IP phones do. To create unique device IDs for analog
                                             				phones, the auto assign process uses a particular algorithm. When you make
                                             				manual ephone assignments, you have to use the same algorithm for each phone
                                             				that receives a manual assignment.

The algorithm
                                             				uses the single 12-digit SCCP local interface MAC address on the Cisco IOS
                                             				gateway as the base to create unique 12-digit device IDs for all the FXS ports
                                             				on the Cisco IOS gateway. The rightmost 9 digits of the SCCP local interface
                                             				MAC address are shifted left three places and are used as the leftmost 9 digits
                                             				for all 24 individual device IDs. The remaining 3 digits are the hexadecimal
                                             				translation of the binary representation of the port’s slot number (3 digits),
                                             				subunit number (2 digits), and port number (7 digits). The following example
                                             				shows the use of the algorithm to create a unique device ID for one port:

The MAC
                                                   					 address for the Cisco VG224 SCCP local interface is 000C.8638.5EA6.

The FXS
                                                   					 port has a slot number of 2 (010), a subunit number of 0 (00), and a port
                                                   					 number of 1 (0000001). The binary digits are strung together to become 0100
                                                   					 0000 0001, which is then translated to 401 in hexadecimal to create the final
                                                   					 device ID for the port and ephone.

The
                                                   					 resulting unique device ID for this port is C863.85EA.6401.

When manually
                                             				setting up an ephone configuration for an analog port, assign it just one
                                             				button because the port represents a single-line device. The button command can use the “:” (colon, for normal), “o” (overlay) and “c”
                                             				(call-waiting overlay) modes.

Step 4

Set up feature
                                          			 parameters as desired.

The following
                                             				list includes commonly configured features. For information about supported
                                             				features, see Supplementary Services
                                                				  Features for FXS Ports on Cisco IOS Voice Gateways Configuration Guide .

Call
                                                   					 transfer—To use call transfer from analog endpoints, the transfer-system command must be configured for the full-blind or full-consult keyword in telephony-service configuration mode on the Cisco Unified CME
                                                   					 router. This is the recommended setting for Cisco CME 3.0 and later versions,
                                                   					 but it is not the default.

Call
                                                   					 forwarding—Call forwarding destinations are specified for all, busy, and
                                                   					 no-answer conditions for each ephone-dn using the call-forward
                                                         						  all , call-forward
                                                         						  busy , and call-forward
                                                         						  noan commands in ephone-dn configuration mode.

Call
                                                   					 park—Call-park slots are created using the park-slot command in ephone-dn configuration mode. Phone users must be instructed how to
                                                   					 transfer calls to the call-park slots and use directed pickup to retrieve the
                                                   					 calls.

Call
                                                   					 pickup groups—Extensions are added to pickup groups using the pickup-group command in ephone-dn configuration mode. Phone users must be told which phones
                                                   					 are in which groups.

Caller
                                                   					 ID—Caller names are defined using the name command
                                                   					 in ephone-dn configuration mode. Caller numbers are defined using the number command in ephone-dn configuration mode.

Speed
                                                   					 dial—Numbers to be speed-dialed are stored with their associated speed-dial
                                                   					 codes using the speed-dial command in ephone configuration mode.

Speed
                                                   					 dial to voice mail—The voice-mail number is defined using the voicemail command in telephony-service configuration mode.

Step 5

Set up
                                          			 feature restrictions as desired.

Features
                                             				such as transfer, conference, park, pickup, group pickup (gpickup), and call
                                             				forward all (cfwdall) can be restricted from individual ephones using the
                                             				appropriate Cisco Unified CME softkey template command, even though analog
                                             				phones do not have softkeys. Simply create a template that leaves out the
                                             				softkey that represents the feature you want to restrict and apply the template
                                             				to the ephone for which you want the feature restricted. For more information
                                             				about softkey template customization, see Customize Softkeys .

#### What to do next

If you have
                                       				SIP and SCCP phones connected to the same Cisco Unified CME, see Configure Codecs of Individual Phones for Calls Between Local Phones .

To select a
                                       				fixed-button layout for a Cisco Unified IP Phone 7931G, see Select Button Layout for a Cisco Unified SCCP IP Phone 7931G .

After
                                       				configuring phones in Cisco Unified CME to make basic calls, you are ready to
                                       				generate configuration files for the phones to be connected. See Generate Configuration Files for SCCP Phones .

### Verify Analog Phone Support

Use the following show commands to display information about
                              		analog endpoints.

show ephone anl —Displays MAC address,
                                    			 registration status, ephone-dn, and speed-dial numbers for analog ephones.

show telephony-service ephone-dn —Displays
                                    			 call forward, call waiting, pickup group, and more information about
                                    			 ephone-dns.

show running-config —Displays running
                                    			 configuration nondefault values.

### Enable Remote
                           	 Phone

To enable IP
                                 		  phones or instances of Cisco IP Communicator to connect to a Cisco Unified CME
                                 		  system over a WAN, perform the following steps.

Restriction

Because
                                                   				  Cisco Unified CME is not designed for centralized call processing, remote
                                                   				  phones are supported only for fixed teleworker applications, such as working
                                                   				  from a home office.

Cisco Unified CME does not support CAC for remote SCCP phones,
                                                   				  so voice quality can degrade if a WAN link is oversubscribed. High-bandwidth
                                                   				  data applications used over a WAN can cause degradation of voice quality for
                                                   				  remote IP phones.

Cisco Unified CME does not support Emergency 911 (E911) calls
                                                   				  from remote IP phones. Teleworkers using remote phones connected to
                                                   				  Cisco Unified CME over a WAN should be advised not to use these phones for E911
                                                   				  emergency services because the local public safety answering point (PSAP) will
                                                   				  not be able to obtain valid calling-party information from them.

We recommend
                                                   				  that you make all remote phone users aware of this issue. One way is to place a
                                                   				  label on all remote teleworker phones that reminds users not to place 911
                                                   				  emergency calls on remote IP phones. Remote workers should place any emergency
                                                   				  calls through locally configured hotel, office, or home phones (normal
                                                   				  land-line phones) whenever possible. Inform remote workers that if they must
                                                   				  use remote IP phones for emergency calls, they should be prepared to provide
                                                   				  specific location information to the answering PSAP personnel, including street
                                                   				  address, city, state, and country.

#### Before you begin

The WAN link
                                       				supporting remote teleworker phones should be configured with a Call Admission
                                       				Control (CAC) or Resource Reservation Protocol (RSVP) solution to prevent the
                                       				oversubscription of bandwidth, which can degrade the quality of all voice
                                       				calls.

If DSP farms
                                       				will be used for transcoding, you must configure them separately. See Configure Transcoding Resources .

A SCCP phone
                                       				to be enabled as a remote phone is configured in Cisco Unified CME. For
                                       				configuration information, see Create Directory Numbers for SCCP Phones .

### SUMMARY STEPS

- enable

- configure terminal

- ephone phone-tag

- mtp

- codec { g711ulaw | g722r64 | g729r8 [ dspfarm-assist ] }

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
Router(config)# ephone 36
```

Enters ephone
                                             				configuration mode.

phone-tag —Unique sequence number that identifies
                                                   					 this ephone during configuration tasks.

Step 4

mtp

#### Example:

```
Router(config-ephone)# mtp
```

Sends media
                                             				packets to the Cisco Unified CME router.

Step 5

codec { g711ulaw | g722r64 | g729r8 [ dspfarm-assist ] }

#### Example:

```
Router(config-ephone)# codec g729r8 dspfarm-assist
```

(Optional)
                                             				Selects a preferred codec for setting up calls.

Default:
                                                   					 G.711 mu-law codec.

The g722r64 keyword requires Cisco Unified CME 4.3
                                                   					 and later versions.

dspfarm-assist —Attempts to use DSP-farm resources
                                                   					 for transcoding the segment between the phone and the Cisco Unified CME router
                                                   					 if G.711 is negotiated for the call.

The dspfarm-assist keyword is ignored if the SCCP
                                                         				  endpoint type is ATA, VG224, or VG248.

Step 6

end

#### Example:

```
Router(config-ephone)# end
```

Returns to
                                             				privileged EXEC mode.

#### What to do next

If you have
                                       				SIP and SCCP phones connected to the same Cisco Unified CME, see Configure Codecs of Individual Phones for Calls Between Local Phones .

To select a
                                       				fixed-button layout for a Cisco Unified IP Phone 7931G, see Select Button Layout for a Cisco Unified SCCP IP Phone 7931G .

After
                                       				configuring phones in Cisco Unified CME to make basic calls, you are ready to
                                       				generate configuration files for the phones to be connected. See Generate Configuration Files for SCCP Phones .

### Verify Remote Phones

Use the show running-config command or the show telephony-service ephone command to
                                          			 verify parameter settings for remote ephones.

### Configure
                           	 Cisco IP Communicator Support on SCCP Phone

To enable support
                                 		  for Cisco IP Communicator, perform the following steps.

#### Before you begin

Cisco Unified CME 4.0 or a later version.

IP address of
                                       				the Cisco Unified CME TFTP server.

PC for
                                       				Cisco IP Communicator is installed. For hardware and platform requirements, see
                                       				the appropriate Cisco IP Communicator User
                                          				  Guide .

Audio devices,
                                       				such as headsets and handsets for users, are installed. You can install audio
                                       				devices any time, but the ideal time to do this is before you install and
                                       				launch Cisco IP Communicator.

Directory
                                       				numbers and ephone configuration for Cisco IP Communicator are configured in
                                       				Cisco Unified CME. For information, see Configure Phones for a PBX System .

Step 1

Download Cisco IP Communicator 2.0 or a later version software from the software download site at https://software.cisco.com/download/home/277641082 .

Step 2

Install the
                                          			 software on your PC, then launch the Cisco IP Communicator application.

For
                                             				information, see the Installing and Launching Cisco IP Communicator section in
                                             				the appropriate Cisco IP Communicator User
                                                				  Guide .

Step 3

Complete the
                                          			 configuration and registration tasks on the Cisco IP Communicator as required,
                                          			 including the following:

Configure
                                                				  the IP address of the Cisco Unified CME TFTP server.

Right-click on the Cisco IP Communicator interface, then choose Preferences > Network > Use these TFTP
                                                               								servers .

Enter
                                                         						  the IP address of the Cisco Unified CME TFTP server in the field.

Disable
                                                				  the Optimize for low bandwidth parameter to ensure that Cisco IP Communicator
                                                				  sends voice packets for all calls.

Right-click on the Cisco IP Communicator interface and
                                                         						  choose Preferences > Audio .

Uncheck the checkbox next to Optimize for low bandwidth.

Step 4

Wait for the
                                          			 Cisco IP Communicator application to connect and register to Cisco Unified CME.

Step 5

Test Cisco IP
                                          			 Communicator.

### Verify Cisco IP Communicator Support on SCCP Phone

Step 1

Use the show running-config command to display
                                          			 ephone-dn and ephone information associated with this phone.

Step 2

After Cisco IP Communicator registers with Cisco Unified CME, it
                                          			 displays the phone extensions and softkeys in its configuration. Verify that
                                          			 these are correct.

Step 3

Make a local call from the phone and have someone call you. Verify
                                          			 that you have a two-way voice path.

### Troubleshooting Cisco IP Communicator Support on SCCP Phone

Use the debug ephone detail command to diagnose problems with calls. For more information, see Cisco Unified CME Command Reference .

### Configure Secure
                           	 IP Phone (IP-STE) on SCCP Phone

To configure an
                                 		  IP-STE phone on Cisco Unified CME, perform the following steps.

Restriction

Detection or
                                                   				  conversion between Network Transmission Equipment (NTE) and Session Signaling
                                                   				  Event (SSE) is not supported.

Transcoding
                                                   				  or trans-compress rate support for different Voice Band Data (VBD) and Modem
                                                   				  Relay (MR) media type is not supported.

IP-STE
                                                   				  supports only single-line calls, dual-line and octo-line calls are not
                                                   				  supported.

Speed-dial
                                                   				  can only be configured manually on the IP-STE.

#### Before you begin

Cisco Unified CME
                                 		  8.0 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- ephone phone-tag

- mac-address [ mac-address ]

- type ip-ste

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
Router(config)# ephone 6
```

Enters ephone
                                             				configuration mode.

phone-tag —Unique sequence number that identifies
                                                   					 this ephone during configuration tasks. The maximum number of ephones is
                                                   					 version and platform-specific. Type ? to display
                                                   					 range.

Step 4

mac-address [ mac-address ]

#### Example:

```
Router(config-ephone)# mac-address 2946.3f2.311
```

Specifies the
                                             				MAC address of the IP phone that is being configured.

Step 5

type ip-ste

#### Example:

```
Router(config-ephone)# type ip-ste
```

Specifies the
                                             				type of phone.

Step 6

end

#### Example:

```
Router(config-ephone)# end
```

Returns to
                                             				privileged EXEC mode.

### Configure Phone
                           	 Services XML File for Cisco Unified Wireless Phone 7926G

To configure the
                                 		  phone services XML file for Cisco Unified Wireless phone 7926G, perform the
                                 		  following steps:

#### Before you begin

Cisco Unified CME
                                 		  8.6 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- ephone phone-tag

- mac-address [ mac-address ]

- type phone-type

- button button-number

- ephone-template template
                                       				  tag

- service [ phone parameter name parameter value ] | [ xml-config append phone_service xml filename ]

- telephony-service

- cnf-file perphone

- create
                                       				  cnf-files

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
Router(config)# ephone 1
```

Enters ephone
                                             				configuration mode.

Step 4

mac-address [ mac-address ]

#### Example:

```
Router(config-ephone)# mac-address 0001.2345.6789
```

Specifies the
                                             				MAC address of the IP phone that is being configured.

Step 5

type phone-type

#### Example:

```
Router(config-ephone)# type 7926
```

Specifies the
                                             				type of phone that is being configured.

Step 6

button button-number

#### Example:

```
Router(config-ephone)# button 1:1
```

Creates a set
                                             				of ephone-dns overlaid on a single button.

Step 7

ephone-template template
                                                				  tag

#### Example:

```
Router(config)#ephone-template 5
```

Enters
                                             				ephone-template configuration mode to create an ephone template.

Step 8

service [ phone parameter name parameter value ] | [ xml-config append phone_service xml filename ]

#### Example:

```
Router(config-ephone-template)#service xml-config append flash:7926_phone_services.xml
```

Sets
                                             				parameters for all IP phones that support the configured functionality and to
                                             				which this template is applied.

parameter name —The parameter name is word and
                                                   					 case-sensitive. See Cisco Unified CME Command
                                                      						Reference .

phone_service xml filename —Allows the addition of
                                                   					 a phone services xml file.

Step 9

telephony-service

#### Example:

```
Router(config)telephony-service
```

Enters
                                             				telephony-service configuration mode.

Step 10

cnf-file perphone

#### Example:

```
(config-telephony)# cnf-file perphone
```

Specifies
                                             				that the system generates a separate configuration XML file for each IP phone.

Separate
                                                   					 configuration files for each endpoint are required for security.

Step 11

create
                                                				  cnf-files

#### Example:

```
Router(config-telephony)# create cnf-files
```

Builds XML
                                             				configuration files required for SCCP phones.

Step 12

end

#### Example:

```
Router(config-telephony)#end
```

Returns to
                                             				privileged EXEC mode.

## Configure Phones to Make Basic Call

### Configure Auto
                           	 Registration for SIP Phones

To configure
                                 		  automatic registration of SIP phones with the Cisco Unified CME system, perform
                                 		  the following steps.

Restriction

The DNs
                                                   				  assigned to auto registered phones cannot be configured as shared line DNs.

Only Cisco
                                                   				  Unified 7800 and 8800 series phones are supported with auto registration.

#### Before you begin

Cisco CME 11.5
                                       				or a later version.

It is
                                       				recommended that administrators choose different DN ranges for manually
                                       				configured and auto configured phones.

It is
                                       				mandatory that password is
                                       				configured before DN range ( auto-assign )
                                       				while registering SIP phones using auto registration.

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- auto-register

- password string

- auto-assign First DN number to Last DN number

- service-enable

- template tag

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

voice register global

#### Example:

```
Router(config)# voice register global
```

Enters voice
                                             				register global configuration mode.

Step 4

auto-register

#### Example:

```
Router(config-register-global)# auto-register
```

Enters auto
                                             				registration mode for SIP phones registering with Unified CME.

Step 5

password string

#### Example:

```
Router(config-voice-auto-register)# password cisco
```

Configures the
                                             				default password for SIP phones that auto register.

string —Configures the mandatory word string that
                                                   					 administrator provides for auto registration of phones on Unified CME.

Step 6

auto-assign First DN number to Last DN number

#### Example:

```
Router(config-voice-auto-register)# auto-assign 1 to 10
```

Configures the
                                             				range of directory numbers for phones that auto register on Unified CME.

First DN number to Last DN number —Range is 1 to
                                                   					 4294967295.

Step 7

service-enable

#### Example:

```
Router(config-voice-auto-register)# service-enable
```

Enables the
                                             				auto registration of SIP phones on Unified CME. Once auto-register command is
                                             				entered, the service is enabled by default.

To temporarily
                                             				disable auto registration feature without losing DN and password
                                             				configurations, use the no form of this command.

Step 8

template tag

#### Example:

```
Router(config-voice-auto-register)
template 10
```

Configures a
                                             				basic configuration template that supports all the configurations available on
                                             				the voice register template.

It is
                                                   					 mandatory that voice register template is configured with the same template
                                                   					 tag.

tag —Range is 1 to 10.

Step 9

end

#### Example:

```
Router(config-voice-auto-register)# end
```

Exits to
                                             				privileged EXEC mode.

### Configure a Mixed
                           	 Shared Line

To configure a
                                 		  mixed shared line between Cisco Unified SIP IP and Cisco Unified SCCP IP
                                 		  phones, perform the following steps.

Restriction

Cisco
                                                   				  Unified SCCP trunk-dn is not supported.

Mixed shared
                                                   				  lines can only be configured on one of several common directory numbers.

Mixed shared
                                                   				  lines are not supported in Cisco Unified SRST.

#### Before you begin

Cisco Unified CME
                                 		  9.0 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice register dn dn-tag

- number number

- shared-line [ max-calls number-of-calls ]

- exit

- ephone-dn dn-tag [ dual-line | octo-line ]

- number number

- shared-line
                                       				  sip

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
                                             				register dn configuration mode.

dn-tag —Unique sequence number that identifies a
                                                   					 particular directory number during configuration tasks. Range is 1 to 150 or
                                                   					 the maximum defined by the max-dn command.

Step 4

number number

#### Example:

```
Router(config-register-dn)# number 1001
```

Associates a
                                             				telephone or extension number with a Cisco Unified SIP IP phone in a Cisco
                                             				Unified CME system.

number —String of up to 16 characters that
                                                   					 represents an E.164 telephone number. Normally, the string is composed of
                                                   					 digits, but the string may contain alphabetic characters when the number is
                                                   					 dialed only by the router, as with an intercom number.

Step 5

shared-line [ max-calls number-of-calls ]

#### Example:

```
Router(config-register-dn)# shared-line max-calls 4
```

Creates a
                                             				directory number to be shared by multiple Cisco Unified SIP IP phones.

max-calls number-of-calls —(Optional) Maximum number of
                                                   					 active calls allowed on the shared line. Range: 2 to 16. Default: 2.

Step 6

exit

#### Example:

```
Router(config-register-dn)# exit
```

Exits voice
                                             				register dn configuration mode.

Step 7

ephone-dn dn-tag [ dual-line | octo-line ]

#### Example:

```
Router(config)# ephone-dn 1 octo-line
```

Enters
                                             				ephone-dn configuration mode to configure a directory number for an IP phone
                                             				line.

dn-tag —Unique number that identifies an ephone-dn
                                                   					 during configuration tasks. Range is 1 to the number set by the max-dn command.

dual-line —(Optional) Enables two calls per
                                                   					 directory number.

octo-line —(Optional) Enables eight calls per
                                                   					 directory number.

Step 8

number number

#### Example:

```
Router(config-ephone-dn)# number 1001
```

Associates a
                                             				telephone or extension number with this ephone-dn.

number —String of up to 16 characters that
                                                   					 represents an E.164 telephone number. Normally, the string is composed of
                                                   					 digits, but the string may contain alphabetic characters when the number is
                                                   					 dialed only by the router, as with an intercom number.

Step 9

shared-line
                                                				  sip

#### Example:

```
Router(config-ephone-dn)# shared-line sip
```

Adds an
                                             				ephone-dn as a member of a shared directory number in the database of the
                                             				Shared-Line Service Module for a mixed shared line between Cisco Unified SIP
                                             				and Cisco Unified SCCP IP phones.

Step 10

end

#### Example:

```
Router(config-ephone-dn)# end
```

Exits to
                                             				privileged EXEC mode.

#### Troubleshooting Tips for Mixed Shared Line

Use the debug ephone shared-line-mixed command to
                                    		  display debugging information about mixed shared lines.

### Configure the
                           	 Maximum Number of Calls on SCCP Phone

To configure the
                                 		  maximum number of calls on a Cisco Unified SCCP IP phone in Cisco Unified CME
                                 		  9.0, perform the following steps.

#### Before you begin

Cisco Unified
                                       				CME 9.0 and later versions.

Correct
                                       				firmware, 9.2(1) or a later version, is installed.

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn dn-tag [ dual-line | octo-line ]

- number number

- exit

- ephone phone-tag

- mac-address mac-address

- type phone-type

- busy-trigger-per-button number-of-calls

- max-calls-per-button number-of-calls

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

ephone-dn dn-tag [ dual-line | octo-line ]

#### Example:

```
Router(config)# ephone-dn 6 octo-line
```

Enters
                                             				ephone-dn configuration mode to configure a directory number for an IP phone
                                             				line.

dn-tag —Unique number that identifies an ephone-dn
                                                   					 during configuration tasks. Range is 1 to the number set by the max-dn command.

dual-line —(Optional) Enables two calls per
                                                   					 directory number.

octo-line —(Optional) Enables eight calls per
                                                   					 directory number.

Step 4

number number

#### Example:

```
Router(config-ephone-dn)# number 1007
```

Associates a
                                             				telephone or extension number with an ephone-dn in a Cisco Unified CME.

number —String of up to 16 characters that
                                                   					 represents an E.164 telephone number. Normally the string is composed of
                                                   					 digits, but the string may contain alphabetic characters when the number is
                                                   					 dialed only by the router, as with an intercom number. One or more periods (.)
                                                   					 can be used as wildcard characters.

Step 5

exit

#### Example:

```
Router(config-ephone-dn)# exit
```

Exits
                                             				ephone-dn configuration mode.

Step 6

ephone phone-tag

#### Example:

```
Router(config)# ephone 98
```

Enters ephone
                                             				configuration mode.

phone-tag —Unique sequence number that identifies
                                                   					 this ephone during configuration tasks. The maximum number of ephones is
                                                   					 version and platform-specific. Type ? to display
                                                   					 range.

Step 7

mac-address mac-address

#### Example:

```
Router(config-ephone)# mac-address ABCD.1234.56EF
```

Associates the
                                             				MAC address of a Cisco IP phone with an ephone configuration in a Cisco Unified
                                             				CME.

mac-address —Identifying MAC address of an IP
                                                   					 phone.

Step 8

type phone-type

#### Example:

```
Router(config-ephone)# type 8941
```

Assigns a
                                             				phone type to an SCCP phone.

Step 9

busy-trigger-per-button number-of-calls

#### Example:

```
Router(config-ephone)# busy-trigger-per-button 6
```

Sets the
                                             				maximum number of calls allowed on an octo-line directory number before
                                             				activating Call Forward Busy or a busy tone.

number-of-calls —Maximum number of calls. Range: 1
                                                   					 to 8. Default: 0 (disabled).

Step 10

max-calls-per-button number-of-calls

#### Example:

```
Router(config-ephone)# max-calls-per-button 4
```

Sets the
                                             				maximum number of calls allowed on an octo-line directory number on an SCCP
                                             				phone.

number-of-calls —Maximum number of calls. Range: 1
                                                   					 to 8. Default: 8.

Step 11

end

#### Example:

```
Router(config-ephone)# end
```

Exits
                                             				configuration mode and enters privileged EXEC mode.

### Configure the Busy
                           	 Trigger Limit on SIP Phone

To configure the
                                 		  busy trigger limit on a Cisco Unified SIP IP phone in Cisco Unified CME 9.0,
                                 		  perform the following steps.

Restriction

You cannot
                                             			 configure the maximum number of calls per line. The phone controls the maximum
                                             			 number of outgoing calls.

Table 1 shows the maximum number of outgoing calls allowed by a phone and the maximum
                                             			 number of incoming calls that can be configured using the busy-trigger-per-button command for Cisco Unified
                                             			 6921, 6941, 6945, 6961, 8941, and 8945 SIP IP Phones in Cisco Unified CME 9.0.

Cisco
                                                            						Unified SIP IP Phones

Maximum
                                                            						Number of Outgoing Calls (Controlled by Phones)

Maximum
                                                            						Number of Incoming Calls

Before
                                                            						Busy Tone (Configurable)

6921

12

12

6941

24

24

6945

24

24

6961

72

72

8941

24

24

8945

24

24

#### Before you begin

Cisco Unified
                                       				CME 9.0 and later versions.

Correct
                                       				firmware is installed:

9.2(1) or
                                             					 a later version for Cisco Unified 6921, 6941, 6945 and 6961 SIP IP phones.

9.2(2) or
                                             					 a later version for Cisco Unified 8941 and 8945 SIP IP phones.

### SUMMARY STEPS

- enable

- configure terminal

- voice register pool pool-tag

- type phone-type

- busy-trigger-per-button number

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

voice register pool pool-tag

#### Example:

```
Router(config)# voice register pool 20
```

Enters voice
                                             				register pool configuration mode and creates a pool configuration for a SIP IP
                                             				phone in Cisco Unified CME.

pool-tag —Unique number assigned to the pool. Range
                                             				is 1 to 100.

For Cisco
                                                         				  Unified CME systems, the upper limit for this argument is defined by the max-pool command.

Step 4

type phone-type

#### Example:

```
Router(config-register-pool)# type 6921
```

Defines a
                                             				phone type for a SIP phone.

Step 5

busy-trigger-per-button number

#### Example:

```
Router(config-register-pool)# busy-trigger-per-button 25
```

Sets the
                                             				maximum number of calls allowed on a SIP directory number before activating
                                             				Call Forward Busy or a busy tone.

number —Maximum number of calls. Range: 1 to the
                                                   					 maximum number of incoming calls listed in Step 6. The default values are 1 for
                                                   					 the Cisco Unified 6921, 6941, 6945, and 6961 SIP IP phones and 2 for the Cisco
                                                   					 Unified 8941 and 8945 SIP IP phones.

Step 6

end

#### Example:

```
Router(config-register-pool)# end
```

Exits
                                             				configuration mode and enters privileged EXEC mode.

### Configure KEMs on
                           	 SIP Phones

To configure KEMs for Cisco SIP IP phones, perform the following steps.

#### Before you begin

Unified CME 9.1 or a later version for C-KEM and BE-KEM.

Unified CME 12.5 or a later release for A-KEM and V-KEM.

### SUMMARY STEPS

- enable

- configure terminal

- voice register pool pool-tag

- type phone-type [ addon 1 CKEM | CP-8800-Audio | CP-8800-Video [ 2 CKEM | CP-8800-Audio | CP-8800-Video [ 3 CKEM | CP-8800-Audio | CP-8800-Video ] ] ]

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

voice register pool pool-tag

#### Example:

```
Router(config)# voice register pool 29
```

Enters voice
                                             				register pool configuration mode and creates a pool configuration for a Cisco
                                             				Unified SIP IP phone in Cisco Unified CME.

pool-tag —Unique number assigned to the pool. Range
                                                   					 is 1 to 100.

For Cisco
                                                         				  Unified CME systems, the upper limit for this argument is defined by the max-pool command.

Step 4

type phone-type [ addon 1 CKEM | CP-8800-Audio | CP-8800-Video [ 2 CKEM | CP-8800-Audio | CP-8800-Video [ 3 CKEM | CP-8800-Audio | CP-8800-Video ] ] ]

#### Example:

```
Router(config-register-pool)# type 9971 addon 1 CKEM 2 CKEM 3 CKEM
Router(config-register-pool)# type 8851 addon 1 CP-8800-Audio 2 CP-8800-Audio
Router(config-register-pool)# type 8851NR addon 1 CP-8800-Audio 2 CP-8800-Audio
Router(config-register-pool)# type 8861 addon 1 CP-8800-Audio 2 CP-8800-Audio 3 CP-8800-Audio
Router(config-register-pool)# type 8865 addon 1 CP-8800-Video 2 CP-8800-Video 3 CP-8800-Video
```

Defines a phone type for a Cisco Unified SIP IP phone.

The following keywords increase the number of speed-dial, busy-lamp-field, and directory number keys that can be configured:

addon 1 CKEM —(Optional) Tells the router that a Cisco SIP IP Phone CKEM 36-Button Line Expansion Module is being added to this Cisco Unified
                                                   SIP IP Phone.

This option is available to Cisco Unified 8961, 9951, and 9971 SIP IP phones only.

addon 1 CP-8800-Audio or addon 1 CP-8800-Video —(Optional) Tells the router that a Cisco SIP IP Phone A-KEM or V-KEM is being added to this Cisco Unified SIP IP Phone.

The option addon 1 CP-8800-Audio is available to Cisco Unified 8851, 8851NR, and 8861 SIP IP phones only. The option addon
                                                         1 CP-8800-Video is available only to Unified IP Phone 8865.

2 CKEM (Optional)—Tells the router that a second Cisco SIP IP Phone CKEM 36-Button Line Expansion Module is being added to this
                                                   Cisco Unified SIP IP Phone.

This option is available to Cisco Unified 9951 and 9971 SIP IP phones only.

2 CP-8800-Audio or 2 CP-8800-Video —(Optional) Tells the router that a second Cisco SIP IP Phone A-KEM or V-KEM is being added to this Cisco Unified SIP IP Phone.

The option 2 CP-8800-Audio is available to Cisco Unified 8851, 8851NR, and 8861 SIP IP phones only. The option 2 CP-8800-Video
                                                         is available only to Unified IP Phone 8865.

3 CKEM —(Optional) Tells the router that a third Cisco SIP IP Phone CKEM 36-Button Line Expansion Module is being added to this Cisco
                                                   Unified SIP IP Phone.

This option is available to Cisco Unified 9971 SIP IP phones only.

3 CP-8800-Audio or 3 CP-8800-Video —(Optional) Tells the router that a third Cisco SIP IP Phone A-KEM or V-KEM is being added to this Cisco Unified SIP IP Phone.

The option 3 CP-8800-Audio is available to Cisco Unified 8861 SIP IP phones only. The option 3 CP-8800-Video is available
                                                         only to Unified IP Phone 8865.

### Provision SIP
                           	 Phones to Use the Fast-Track Configuration Approach

To provision the
                                 		  Cisco Unified SIP IP phones using the fast-track configuration approach,
                                 		  perform the following steps.

Restriction

When a new Cisco
                                             			 Unified SIP IP phone is configured on Cisco Unified CME using the fast-track
                                             			 configuration approach, and the Cisco Unified CME is upgraded to a later
                                             			 version that supports the new phone type, the fast-track configuration
                                             			 pertaining to that SIP IP phone is removed automatically.

#### Before you begin

You require Cisco
                                 		  Unified CME Release 10 or a later release.

### SUMMARY STEPS

- enable

- configure terminal

- voice register pool-type pool-type

- addons max-addons

- description string

- gsm-support

- num-lines max-lines

- Phoneload-support

- reference-pooltype phone-type

- telnet-support

- transport { udp | TCP }

- Xml-config { maxNumCalls | busyTrigger | custom }

- exit

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables the
                                             				privileged EXEC mode. Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters the
                                             				global configuration mode.

Step 3

voice register pool-type pool-type

#### Example:

```
Router(config)# voice register pool-type 9900
```

Enters the
                                             				voice register pool configuration mode and creates a pool configuration for a
                                             				Cisco Unified SIP IP phone in Cisco Unified CME.

If the new
                                             				phone type is an existing phone that is supported on Cisco Unified CME release,
                                             				you get the following error message:

```
ERROR: 8945 is built-in phonemodel, cannot be changed
```

Step 4

addons max-addons

#### Example:

```
Router(config-register-pooltype)# addons 3
```

Defines the
                                             				maximum number of add-on modules supported in Cisco Unified SIP IP phones.

max-addons —The maximum allowed value is 3. The
                                                   					 configured add-on modules can be used while defining the pool for the new SIP
                                                   					 phone model using the existing type command as shown below:

```
type <phone-type> [addon 1 module-type [2 module-type]]
```

Step 5

description string

#### Example:

```
Router(config-register-pooltype)# description TEST PHON
```

Defines the
                                             				description string for the new phone type.

Step 6

gsm-support

#### Example:

```
Router(config-register-pooltype)# gsm-support
```

Defines phone
                                             				support for Global System for Mobile Communications (GSM) support.

Step 7

num-lines max-lines

#### Example:

```
Router(config-register-pooltype)# num-lines 12
```

Defines the
                                             				maximum number of lines supported by the new phone.

max-lines —If this parameter is not configured, the
                                                   					 default value 1 is used.

Step 8

Phoneload-support

#### Example:

```
Router(config-register-pooltype)# Phoneload-support
```

Defines phone
                                             				support for firmware download from Cisco Unified CME. You can use the load
                                             				command in the voice register global mode to configure the corresponding phone
                                             				load for the new phone type if it supports phone load.

Step 9

reference-pooltype phone-type

#### Example:

```
voice register pool-type 7821? 
			 description Cisco IP Phone 7821 reference-pooltype 6921
```

Defines the
                                             				nearest phone family from which the SIP IP phone in fast-track mode will
                                             				inherit the properties.

phone-type —Unique number that represents the phone
                                                   					 model.

Default There
                                             				is no reference point to inherit the properties.

Step 10

telnet-support

#### Example:

```
Router(config-register-pooltype)# telnet-support
```

Defines
                                             				phone support for Telnet access.

Step 11

transport { udp | TCP }

#### Example:

```
Router(config-register-pooltype)# transport TCp
```

Defines the
                                             				default transport type supported by the new phone.

If this
                                             				parameter is not configured, UDP is used as the default value. The session-transport command configured at the voice register
                                             				pool takes priority over this configuration.

Step 12

Xml-config { maxNumCalls | busyTrigger | custom }

#### Example:

```
Router(config-register-pooltype)#xml-config busyTrigger 2 
Router(config-register-pooltype)#xml-config maxNumCalls 4
Router(config-register-pooltype)#xml-config custom <test>1</test>
```

Defines the
                                             				phone-specific XML tags to be used in the configuration file.

maxNumCalls —Defines the maximum number of calls allowed
                                                   					 per line.

busyTrigger —Defines the number of calls that triggers
                                                   					 Call Forward Busy per line on the SIP phone.

custom —Defines custom XML tags which can be appended at
                                                   					 the end of the phone specific CNF file.

These
                                             				parameters are used while generating the configuration profile file. CUCME does
                                             				not use these configuration values for any other purpose.

Step 13

exit

#### Example:

```
Router(config-register-pooltype)# exit
```

Exits the
                                             				voice register-pooltype configuration mode.

Step 14

end

#### Example:

```
Router(config)# end
```

Exits the
                                             				privileged EXEC configuration mode.

## SIP Phone Models Validated for CME using Fast-track
                        	 Configuration

For information on the SIP phone models validated for Cisco Unified CME using fast-track configuration, see Phone Feature Support Guide for Unified CME, Unified SRST, Unified E-SRST, and Unified Secure SRST .

## Configuration Examples for Making Basic Calls

This section contains the following examples of the required
                           		Cisco Unified CME configurations with some of the additional options that are
                           		discussed in other modules.

### Example for
                           	 Configuring SCCP Phones for Making Basic Calls

The following is a
                                 		  sample output of the show
                                       				running-config command, showing how an SCCP phone is configured
                                 		  to make basic calls:

```
Router# show running-config version 12.4
service tcp-keepalives-in
service tcp-keepalives-out
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname CME40
!
boot-start-marker
boot-end-marker
!
logging buffered 2000000 debugging
!
no aaa new-model
!
resource policy
!
clock timezone PST -8
clock summer-time PDT recurring
no network-clock-participate slot 2 
voice-card 0
 no dspfarm
 dsp services dspfarm
!
voice-card 2
 dspfarm
!
no ip source-route
ip cef
!
!
!
ip domain name cisco.com
ip multicast-routing 
!
!
ftp-server enable
ftp-server topdir flash:
isdn switch-type primary-5ess
!
!
!
voice service voip 
 allow-connections h323 to sip
 allow-connections sip to h323
 no supplementary-service h450.2
 no supplementary-service h450.3
 h323
  call start slow
!
!
!
controller T1 2/0/0
 framing esf
 linecode b8zs
 pri-group timeslots 1-24
!
controller T1 2/0/1
 framing esf
 linecode b8zs
!
!
interface GigabitEthernet0/0
 ip address 192.168.1.1 255.255.255.0
 ip pim dense-mode
 duplex auto
 speed auto
 media-type rj45
 negotiation auto
!
interface Service-Engine1/0
 ip unnumbered GigabitEthernet0/0
 service-module ip address 192.168.1.2 255.255.255.0
 service-module ip default-gateway 192.168.1.1
!
interface Serial2/0/0:23
 no ip address
 encapsulation hdlc
 isdn switch-type primary-5ess
 isdn incoming-voice voice
 isdn map address ^.* plan unknown type international
 no cdp enable
!
!
ip route 0.0.0.0 0.0.0.0 192.168.1.254
ip route 192.168.1.2 255.255.255.255 Service-Engine1/0
ip route 192.168.2.253 255.255.255.255 10.2.0.1
ip route 192.168.3.254 255.255.255.255 10.2.0.1
!
!
ip http server
ip http authentication local
no ip http secure-server
ip http path flash:
!
!
!
!
tftp-server flash:P00307020300.loads
tftp-server flash:P00307020300.sb2
tftp-server flash:P00307020300.sbn
!
control-plane
!
!
!
voice-port 2/0/0:23
!
!
!
sccp local GigabitEthernet0/0
sccp ccm 192.168.1.1 identifier 1 
sccp
!
sccp ccm group 1
 associate ccm 1 priority 1
 associate profile 1 register MTP0013c49a0cd0
 keepalive retries 5
!
dspfarm profile 1 transcode
 codec g711ulaw
 codec g711alaw
 codec g729ar8
 codec g729abr8
 codec gsmfr
 codec g729r8
 maximum sessions 90
 associate application SCCP
!
!
dial-peer voice 9000 voip
 mailbox-selection last-redirect-num
 destination-pattern 78..
 session protocol sipv2
 session target ipv4:192.168.1.2
 dtmf-relay sip-notify
 codec g711ulaw
 no vad
!
dial-peer voice 2 pots
 incoming called-number .
 direct-inward-dial
 port 2/0/0:23
 forward-digits all
!
dial-peer voice 1 pots
 destination-pattern 9[2-9]......
 port 2/0/0:23
 forward-digits 8
!
dial-peer voice 3 pots
 destination-pattern 91[2-9]..[2-9]......
 port 2/0/0:23
 forward-digits 12!
!
gateway 
 timer receive-rtp 1200
!
!
telephony-service
 load 7960-7940 P00307020300
 max-ephones 100
 max-dn 300
 ip source-address 192.168.1.1 port 2000
 system message CCME 4.0
 sdspfarm units 1
 sdspfarm transcode sessions 128
 sdspfarm tag 1 MTP0013c49a0cd0
 voicemail 7800
 max-conferences 24 gain -6
 call-forward pattern .T
 moh music-on-hold.au
 multicast moh 239.1.1.1 port 2000
 web admin system name admin password sjdfg
 transfer-system full-consult
 transfer-pattern .T
 secondary-dialtone 9
 create cnf-files version-stamp Jan 01 2002 00:00:00
!
!
ephone-dn-template  1
!
!
ephone-template  1
 keep-conference endcall local-only
 codec g729r8 dspfarm-assist
!
!
ephone-template  2
!
!
ephone-dn  1
 number 6001
 call-forward busy 7800
 call-forward noan 7800 timeout 10
!
!
ephone-dn  2
 number 6002
 call-forward busy 7800
 call-forward noan 7800 timeout 10
!
!
ephone-dn  10
 number 6013
 paging ip 239.1.1.1 port 2000
!
!
ephone-dn  20
 number 8000....
 mwi on
!
!
ephone-dn  21
 number 8001....
 mwi off
!
!
!
!
ephone  1
 device-security-mode none
 username "user1"
 mac-address 002D.264E.54FA
 codec g729r8 dspfarm-assist
 type 7970
 button  1:1
!
!
!
ephone  2
 device-security-mode none
 username "user2"
 mac-address 001C.821C.ED23
 type 7960
 button  1:2
!
!
!
line con 0
 stopbits 1
line aux 0
 stopbits 1
line 66
 no activation-character
 no exec
 transport preferred none
 transport input all
 transport output all
line 258
 no activation-character
 no exec
 transport preferred none
 transport input all
 transport output all
line vty 0 4
 exec-timeout 0 0
 privilege level 15
 password sgpxw
 login
!
scheduler allocate 20000 1000
ntp server 192.168.224.18
!
!
end
```

### Example for Configuring SIP Phones for Making Basic Calls

The following is a configuration example for SIP phones running on
                                 		  Cisco Unified CME:

```
voice service voip 
 allow-connections sip to sip
 sip
 registrar server expires max 600 min 60
!
voice class codec 1
 codec preference 1 g711ulaw
!
voice hunt-group 1 parallel
 final 8000
 list 2000,1000,2101
 timeout 20 
 pilot 9000
!
voice hunt-group 2 sequential
 final 1000
 list 2000,2300
 timeout 25 
 pilot 9100 secondary 9200
!
voice hunt-group 3 peer
 final 2300
 list 2100,2200,2101,2201
 timeout 15 
 hops 3
 pilot 9300
 preference 5
!
voice hunt-group 4 longest-idle
 final 2000
 list 2300,2100,2201,2101,2200
 timeout 15 
 hops 5 
 pilot 9400 secondary 9444
 preference 5 secondary 9
!
voice register global
 mode cme
!
 external-ring bellcore-dr3 
!
voice register dn 1
 number 2300
 mwi
!
voice register dn 2
 number 2200
 call-forward b2bua all 1000 
 call-forward b2bua mailbox 2200 
 mwi
!
voice register dn 3
 number 2201
 after-hour exempt
!
voice register dn 4
 number 2100
 call-forward b2bua busy 2000 
 mwi
 
voice register dn 5
 number 2101
 mwi
 
voice register dn 76
 number 2525
 call-forward b2bua unreachable 2300 
 mwi
!
voice register template 1
!
voice register template 2
 no conference enable
 voicemail 7788 timeout 5
!
voice register pool 1
 id mac 000D.ED22.EDFE
 type 7960
 number 1 dn 1
 template 1
 preference 1
 no call-waiting
 codec g711alaw
!
voice register pool 2
 id mac 000D.ED23.CBA0
 type 7960
 number 1 dn 2
 number 2 dn 2
 template 1
 preference 1
!
 dtmf-relay rtp-nte
 speed-dial 3 2001
 speed-dial 4 2201
!
voice register pool 3
 id mac 0030.94C3.053E
 type 7960
 number 1 dn 3
 number 3 dn 3
 template 2
!
voice register pool 5
 id mac 0012.019B.3FD8
 type ATA
 number 1 dn 5
 preference 1
 dtmf-relay rtp-nte
 codec g711alaw
!
voice register pool 6
 id mac 0012.019B.3E88
 type ATA
 number 1 dn 6
 number 2 dn 7
 template 2
 dtmf-relay-rtp-nte
 call-forward b2bua all 7778
!
voice register pool 7
!
voice register pool 8
 id mac 0006.D737.CC42
 type 7940
 number 1 dn 8
 template 2
 preference 1
 codec g711alaw
!
voice-port 1/0/0
!
voice-port 1/0/1
!
dial-peer voice 100 pots
 destination-pattern 2000
 port 1/0/0
!
dial-peer voice 101 pots
 destination-pattern 2010
 port 1/0/1
!
dial-peer voice 1001 voip
 preference 1
 destination-pattern 1...
 session protocol sipv2
 session target ipv4:10.15.6.13
 codec g711ulaw
!
sip-ua
 mwi-server ipv4:1.15.6.200 expires 3600 port 5060 transport udp
!
telephony-service
 load 7960-7940 P0S3-07-2-00
 max-ephones 24
 max-dn 96
 ip source-address 10.15.6.112 port 2000
 create cnf-files version-stamp Aug 24 2004 00:00:00
 max-conferences 8
 after-hours block pattern 1 1...
 after-hours day Mon 17:00 07:00
```

### Example for Disabling a Bulk Registration for a SIP Phone

The following example shows that all phone numbers that match the
                                 		  pattern “408555..” can register with the SIP proxy server (IP address
                                 		  1.5.49.240) except directory number 1, number “4085550101,” for which bulk
                                 		  registration is disabled:

```
voice register global
 mode cme
 bulk 408555….
!
voice register dn 1
 number 4085550101
 no-reg
sip-ua
 registrar ipv4:1.5.49.240
```

### Examples for
                           	 Configuring VCC with Shared Lines

#### Example

The following is a
                                 		  sample configuration for VCC with shared lines, with the same voice class codec
                                 		  configured under the voice register pools.

```
Router# 
 
voice class codec 1
 codec preference 1 g711ulaw
 codec preference 2 g729r8
 codec preference 3 g722-64

voice class codec 2
 codec preference 1 g711ulaw
 codec preference 2 g729r8

voice register pool 1
 busy-trigger-per-button 2
 id mac 08CC.A785.EE9C
 type 8865
 number 1 dn 1
 dtmf-relay rtp-nte
 voice-class codec 1
 username abcd password xxxx
 no vad

voice register pool 2
 busy-trigger-per-button 2
 id mac D42C.4485.D9C2
 type 7861
 number 1 dn 1
 dtmf-relay rtp-nte
 voice-class codec 1
 username uvwx password xxxx
 no vad

dial-peer voice 2 voip
 session protocol sipv2
 incoming called-number 50..
 voice-class codec 2
 dtmf-relay rtp-nte
 no vad
```

### Example for
                           	 Configuring a Mixed Shared Line on a Second Common Directory Number

The following
                                 		  example shows how configuring a mixed shared line on a second common directory
                                 		  number is rejected:

```
Router(config)#ephone-dn 14 octo-line
Router(config-ephone-dn)#number 2502
Router(config-ephone-dn)# shared-line sip Router(config)#ephone-dn 20 octo-line
Router(config-ephone-dn)#number 2502
Router(config-ephone-dn)# shared-line sip DN number already exists in the shared line database
```

### Example for Cisco ATA

The following example shows the configuration for two analog phones
                                 		  using a single Cisco ATA with MAC address 000F.F758.E70E. The analog phone
                                 		  attached to the first port uses the MAC address of the Cisco ATA. The analog
                                 		  phone attached to the second port uses a modified version of the Cisco ATA’s
                                 		  MAC address; the first two hexadecimal numbers are removed and 01 is appended
                                 		  to the end.

```
telephony-service
 conference hardware
 load ATA ATA030203SCCP051201A.zup
!
ephone-dn  80  dual-line
 number 8080
!
ephone-dn  81  dual-line
 number 8081
!
ephone  30
 mac-address 000F.F758.E70E
 type ata
 button  1:80
!
ephone  31
 mac-address 0FF7.58E7.0E01
 type ata
 button  1:81
```

### Example for Cisco ATA in SIP Mode

The following example shows the configuration for an analog phones using a Cisco ATA 190 or ATA 191 with MAC address DCEB.941C.F33D.

```
enable
configure terminal
voice register dn 15
    number 8015
voice register pool 15
    id mac DCEB.941C.F33D
    type ATA-190/ATA-191
    number 1 dn 15
    username abcd password xxxx
    codec g711ulaw
    end
```

### Example for SCCP Analog Phone

The following partial sample output from a Cisco Unified CME
                                 		  configuration sets transfer type to full-blind and sets the voice-mail
                                 		  extension to 5200. Ephone-dn 10 has the extension 4443 and is assigned to
                                 		  Tommy; that number and name will be used for caller-ID displays. The
                                 		  description field under ephone-dn is used to indicate that this ephone-dn is on
                                 		  the Cisco VG224 voice gateway at port 1/3. Extension 4443 is assigned to ephone
                                 		  7, which is an analog phone type with 10 speed-dial numbers.

```
CME_Router# show running-config .
.
.
telephony-service
 load 7910 P00403020214
 load 7960-7940 P00305000301
 load 7905 CP79050101SCCP030530B31
 max-ephones 60
 max-dn 60
 ip source-address 10.8.1.2 port 2000
 auto assign 1 to 60
 create cnf-files version-stamp 7960 Sep 28 2004 17:23:02
 voicemail 5200
 mwi relay
 mwi expires 99999
 max-conferences 8 gain -6
 web admin system name cisco password lab
 web admin customer name ac2 password cisco
 dn-webedit 
 time-webedit 
 transfer-system full-blind
 transfer-pattern 6...
 transfer-pattern 5...
!
!
ephone-dn  10  dual-line
 number 4443 secondary 9191114443
 pickup-group 5
 description vg224-1/3
 name tommy
!
ephone  7
 mac-address C863.9018.0402
 speed-dial 1 4445
 speed-dial 2 4445
 speed-dial 3 4442
 speed-dial 4 4441
 speed-dial 5 6666
 speed-dial 6 1111
 speed-dial 7 1112
 speed-dial 8 9191114441
 speed-dial 9 9191114442
 speed-dial 10 9191114442
 type anl
 button  1:10
```

### Example for Remote Teleworker Phones

The following example shows the configuration for ephone 270, a remote
                                 		  teleworker phone with its codec set to G.729r8. The dspfarm-assist keyword is used to ensure that
                                 		  calls from this phone will use DSP resources to maintain the G.729r8 codec when
                                 		  calls would normally be switched to a G.711 codec.

```
ephone 270
 button 1:36
 mtp
 codec g729r8 dspfarm-assist
 description teleworker remote phone
```

### Example for Secure IP Phone (IP-STE)

The following example shows the configuration for Secure IP Phone
                                 		  IP-STE. IP-STE is the phone type required to configure a secure phone.

```
ephone-dn  1
 number 3001
...
ephone  9
 mac-address 0004.E2B9.1AD1
 max-calls-per-button 1
 type IP-STE
 button  1:1 2:2 3:3 4:4
```

### Example for
                           	 Configuring Phone Services XML File for Cisco Unified Wireless Phone
                           	 7926G

The following
                                 		  example shows phone type 7926 configured in ephone 1 and service xml-config
                                 		  file configured in ephone template 1:

```
!
!
!
telephony-service 
 max-ephones 58 
 max-dn 192 
 ip source-address 1.4.206.105 port 2000 
 cnf-file perphone 
 create cnf-files 
! 
ephone-template 1 service xml-config append flash:7926_phone_services.xml ! 
ephone-dn  1 octo-line 
  number 1001 
! 
ephone  1 
  mac-address AAAA.BBBB.CCCC 
  ephone-template 1 type 7926 button 1:1 
!
```

### Example for Monitoring the Status of Key Expansion Modules

Show commands are used to monitor the status and other details of Key
                                 		  Expansion Modules (KEMs).

The following example demonstrates how the show voice register all command displays KEM details with all the Cisco Unified
                                 		  CME configurations and registration information:

```
show voice register all VOICE REGISTER GLOBAL
=====================
CONFIG [Version=9.1]
========================
............
Pool Tag 5
Config:
  Mac address is B4A4.E328.4698
  Type is 9971 addon 1 CKEM
  Number list 1 : DN 2
  Number list 2 : DN 3
  Proxy Ip address is 0.0.0.0
  DTMF Relay is disabled
  Call Waiting is enabled
  DnD is disabled
  Video is enabled
  Camera is enabled
  Busy trigger per button value is 0
  keep-conference is enabled
  registration expires timer max is 200 and min is 60
  kpml signal is enabled
  Lpcor Type is none
```

The following example demonstrates how the show voice register pool type command
                                 		  displays all the phones configured with add-on KEMs in Cisco Unified CME:

```
Router# show voice register pool type CKEM Pool ID              IP Address      Ln DN  Number               State
==== =============== =============== == === ==================== ============
4    B4A4.E328.4698  9.45.31.111     1  4   5589$                REGISTERED
```

The following example demonstrates how the show voice register pool
                                 		  type summary command displays all the SIP phones (both registered and
                                 		  unregistered) configured with add-on KEMs in Cisco Unified CME:

```
Router# show voice register pool type summary Phone Type    Configured    Registered    Unregistered
==========    ==========    ==========    ============
Unknown type     2            0                2
    7821 			      1            0                1
    9951         1            1                0
    DX650        1		            0                1
======================================================
Total Phones     5	            1                4
======================================================
```

### Cisco IOS Commands
                           	 for Monitoring and Maintaining Cisco Unified CME

To monitor and
                              		maintain Cisco Unified Communications Manager Express (CME), use the following
                              		commands in privileged EXEC mode.

Command

Purpose

```
Router# show call-manager-fallback all
```

Displays
                                             					 the detailed configuration of all the Cisco Unified IP phones, voice ports, and
                                             					 dial peers of the Cisco Unified CME Router.

```
Router# show call-manager-fallback dial-peer
```

Displays
                                             					 the output of the dial peers of the Cisco Unified CME Router.

```
Router# show call-manager-fallback ephone-dn
```

Displays
                                             					 Cisco Unified IP Phone destination numbers when in call manager fallback mode.

```
Router# show call-manager-fallback voice-port
```

Displays
                                             					 output for the voice ports.

```
Router# show dial-peer voice summary
```

Displays a
                                             					 summary of all voice dial peers.

```
Router# show ephone phone
```

Displays
                                             					 Cisco Unified IP Phone status.

```
Router# show ephone offhook
```

Displays
                                             					 Cisco Unified IP Phone status for all phones that are off hook.

```
Router# show ephone registered
```

Displays
                                             					 Cisco Unified IP Phone status for all phones that are currently registered.

```
Router# show ephone remote
```

Displays
                                             					 Cisco Unified IP Phone status for all nonlocal phones (phones that have no
                                             					 Address Resolution Protocol [ARP] entry).

```
Router# show ephone ringing
```

Displays
                                             					 Cisco Unified IP Phone status for all phones that are ringing.

```
Router# show ephone summary
```

Displays a
                                             					 summary of all Cisco Unified IP Phones.

```
Router# show ephone summary brief
```

Displays a
                                             					 brief summary of all Cisco Unified SCCP phones.

```
Router# show ephone summary types
```

Displays a
                                             					 summary of all types of Cisco Unified SCCP phones.

```
Router# show ephone registered summary
```

Displays a
                                             					 summary of all registered Cisco Unified SCCP phones.

```
Router# show ephone unregistered summary
```

Displays a
                                             					 summary of all unregistered Cisco Unified SCCP phones.

```
Router# show ephone telephone-number phone-number
```

Displays
                                             					 Unified IP Phone status for a specific phone number.

```
Router# show ephone unregistered
```

Displays
                                             					 Unified IP Phone status for all unregistered phones.

```
Router# show ephone-dn tag
```

Displays
                                             					 Unified IP Phone destination numbers.

```
Router# show ephone-dn summary
```

Displays
                                             					 a summary of all Cisco Unified IP Phone destination numbers.

```
Router# show ephone-dn loopback
```

Displays
                                             					 Cisco Unified IP Phone destination numbers in loopback mode.

```
Router# show running-config
```

Displays
                                             					 the configuration.

```
Router # show sip-ua status registrar
```

Display
                                             					 SIP registrar clients.

```
Router# show voice port summary
```

Displays
                                             					 a summary of all voice ports.

```
Router # show voice register all
```

Displays
                                             					 all SIP SRST configurations , SIP phone registrations and dial peer info.

```
Router # show voice register global
```

Displays
                                             					 voice register global config.

```
Router # show voice register pool all
```

Displays
                                             					 all config SIP phone voice register pool detail info.

```
Router # show voice register pool type summary
```

Displays
                                             					 a summary of all registered and unregistered Cisco SIP Phones.

```
Router # show voice register pool <tag>
```

Displays
                                             					 specific SIP phone voice register pool detail info.

```
Router # show voice register dial-peers
```

Displays
                                             					 SIP-CME created dial peer.

```
Router # show voice register dn all
```

Displays
                                             					 all config voice register dn detail info.

```
Router # show voice register dn <tag>
```

Displays
                                             					 specific voice register dn detail info.

### Example for Fast-Track Configuration Approach

The following example shows how to enable the new Cisco Unified 9900
                                 		  SIP IP phone to inherit the properties of the Cisco Unified SIP IP phone 9951
                                 		  and overwrite some of the phone’s properties:

```
voice register pool-type 9900
	reference-pooltype  9951  
	description  SIP Phone 9900 addon module
 	num-lines  24
	addons 3
  	no phoneload-support
	xml-config custom "custom-sftp"1"/custom-sftp"

voice register pool 1
	type 9900 addon 1 CKEM 2 CKEM 3 CKEM
	id mac 1234.4567.7891
voice register global
	mode cme
	load 9900 P0S3-06-0-00
```

The following example shows how to inherit the existing properties of
                                 		  a reference phone type (Cisco Unified SIP IP phone 6921) using the fast-track
                                 		  configuration approach.

```
voice register pooltype 6922 
	reference-pooltype 6921 device-name  “SIP Phone 6922”

voice register pool 11
	type 6922
	id mac 1234.4567.7890
```

### Example for Configuring Key Expansion Module for Cisco 8800 Series IP Phones on Unified CME

The following example demonstrates how to configure the type command for phone type 8865 with the KEM option CP-8800-Video to enable Key Expansion Module for Cisco IP Phone 8800 Series on Unified CME 12.5 and later releases:

```
enable
configure terminal
voice register pool
  id mac eeee.ffff.cccc
  type 8865 addon 1 CP-8800-Video 2 CP-8800-Video 3 CP-8800-Video
```

### Example for
                           	 Configuring Enhanced Line Mode on Unified CME

The following
                                 		  example demonstrates how to configure service phone
                                       				lineMode command under telephony-service to enable Enhanced Line Mode
                                 		  feature for Cisco IP Phone 8800 Series on Unified CME:

```
Router#sh run | s tele
	telephony-service
	max-ephones 50
	max-dn 50
	ip source-address 8.40.23.31 port 2000
	service phone sshAccess 0
	service phone webAccess 0
	service phone lineMode 1
	max-conferences 8 gain -6
	call-park system application
	hunt-group logout HLog
	moh enable-g711 "flash:music-on-hold.au"
	moh g729 "flash:SampleAudioSource.g729.wav"
	transfer-system full-consult
	fac standard
	create cnf-files version-stamp Jan 01 2002 00:00:00
```

## Where To Go Next

To select a fixed-button layout for a Cisco Unified IP Phone 7931G, see Select Button Layout for a Cisco Unified SCCP IP Phone 7931G .

After configuring phones in Cisco Unified CME to make basic calls, you are ready to generate configuration files for the phones
                           to be connected to your router. See Generate Configuration Files for Phones .

## Feature
                        	 Information for Configuring Phones to Make Basic Calls

Caution

The Interactive
                                       		  Voice Response (IVR) media prompts feature is only available on the IAD2435
                                       		  when running IOS version 15.0(1)M or later.

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature
                                          					 Name

Cisco Unified CME Versions

Feature
                                          					 Information

Cisco ATA 191

12.5

Introduces native support for Cisco ATA 191 with Unified CME.

Enhanced Line Mode

12.3

Support introduced for Enhanced Line Mode (ELM) on Cisco IP Phone 8800 Series.

Shared
                                          					 Lines with Voice Class Codec Support

12.2

Adds
                                          					 support for shared lines with voice class codec on Unified CME.

KEM Support for Cisco 8000 Series SIP IP Phones

12.5

Supports A-KEM and V-KEM for Cisco IP Phones 8851, 8851NR, 8861, and 8865 Cisco SIP IP Phones.

KEM
                                          					 Support for Cisco Unified 8961, 9951, and 9971 SIP IP Phones

9.1

Increases
                                          					 line key and feature key appearances, speed dials, or programmable buttons on
                                          					 Cisco Unified SIP IP phones.

Cisco
                                          					 ATA-187

9.0

Supports
                                          					 T.38 fax relay and fax pass-through on Cisco ATA-187.

Cisco
                                          					 Unified SIP IP Phones

Adds SIP
                                          					 support for the following phone types:

Cisco
                                                						  Unified 6901 and 6911 IP Phones

Cisco
                                                						  Unified 6921, 6941, 6945, and 6961 IP Phones

Cisco
                                                						  Unified 8941 and 8945 IP Phones

Mixed
                                          					 Shared Lines

Allows
                                          					 Cisco Unified SIP and SCCP IP phones to share a common directory number.

Multiple
                                          					 Calls Per Line

Overcomes
                                          					 the limitation on the maximum number of calls per line.

Real-Time
                                          					 Transport Protocol Call Information Display Enhancement

8.8

Allows you
                                          					 to display information on active RTP calls using the show ephone rtp connections command. The output from this command provides
                                          					 an overview of all the connections in the system, narrowing the criteria for
                                          					 debugging pulse code modulation and Cisco Unified CME packets without a
                                          					 sniffer.

Support
                                          					 for Cisco Unified 3905 SIP IP Phones

Adds
                                          					 support for SIP phones connected to a Cisco Unified CME system.

Support
                                          					 for Cisco Unified 6945, 8941, and 8945 SCCP IP Phones

Adds
                                          					 support for SCCP phones connected to a Cisco Unified CME system.

Support
                                          					 for 7926G Wireless SCCP IP Phone

8.6

Added
                                          					 support for 7926G Wireless SCCP IP Phone.

Secure IP
                                          					 Phones

8.0

Adds
                                          					 support for Secure IP Phone (IP-STE).

SIP Shared
                                          					 Lines

7.1

Adds
                                          					 support for nonexclusive shared lines on SIP phones.

Autoconfiguration for Cisco VG202, VG204, and VG224

Adds
                                          					 autoconfiguration for the Cisco VG202, VG204, and VG224 Analog Phone Gateway.

Ephone-Type Templates

7.0/4.3

Adds
                                          					 support for dynamically adding new phone types without upgrading
                                          					 Cisco IOS software.

Octo-Line Directory Numbers

Adds
                                          					 octo-line directory numbers that support up to eight active calls.

G.722
                                          					 and iLBC Transcoding and Conferencing Support in Cisco Unified CME

Adds
                                          					 support for the G.722-64K and iLBC codecs.

Dial
                                          					 Plans for SIP Phones

4.1

Adds
                                          					 support for dial plans for SIP phones.

KPML

Adds
                                          					 support for KPML for SIP phones.

Session
                                          					 Transport Protocol

Adds
                                          					 selection for session-transport protocol for SIP phones.

Watch
                                          					 Mode

Provides
                                          					 Busy Lamp Field (BLF) notification on a line button that is configured for
                                          					 watch mode on one phone for all lines on another phone (watched phone) for
                                          					 which the watched directory number is the primary line.

Remote
                                          					 Teleworker Phones

4.0

Introduces support for teleworker remote phones.

Analog
                                          					 Phones

4.0

Introduces support for analog phones with SCCP supplementary
                                          					 features using FXS ports on Cisco Integrated Services Routers.

3.2.1

Introduces support for analog phones with SCCP supplementary
                                          					 features using FXS ports on a Cisco VG224 voice gateway.

3.0

Introduces support for Cisco ATA 186 and Cisco ATA 188.

1.0

Introduces support for analog phones in H.323 mode using FXS
                                          					 ports.

Cisco IP
                                          					 Communicator

4.0

Introduces support for Cisco IP Communicator.

Direct
                                          					 FXO Trunk Lines

4.0

Adds
                                          					 enhancements to improve the keyswitch emulation behavior of PSTN lines in a
                                          					 Cisco Unified CME system, including the following:

Status monitoring of the FXO port on the line button of an IP
                                                						  phone.

Transfer recall if a transfer-to phone does not answer after a
                                                						  specified timeout.

Transfer-to button optimization to free up the private extension
                                                						  line on the transfer-to phone

Directory numbers for FXO lines can be configured for dual-line
                                                						  to support the FXO monitoring, transfer recall, and transfer-to button
                                                						  optimization features.

3.2

Introduces direct FXO trunk line capability.

SIP
                                          					 Phones

3.4

Adds
                                          					 support for SIP phones connected to Cisco CME system.

Monitor
                                          					 Mode for Shared Lines

3.0

Provides
                                          					 a visible line status indicating whether the line is in-use or not.

| Caution | The Interactive
                                    		  Voice Response (IVR) media prompts feature is only available on the IAD2435
                                    		  when running IOS version 15.0(1)M or later. |
|---|---|

| Note | You must make the choice to configure each directory number in your system as either dual-line or single-line when you initially
                                             create configuration entries. If you need to change from single-line to dual-line later, you must delete the configuration
                                             for the directory number, then recreate it. |
|---|---|

| Note | You must make the choice to configure each directory number in your
                                             		  system as either dual-line or single-line when you initially create
                                             		  configuration entries. If you need to change from single-line to dual-line
                                             		  later, you must delete the configuration for the directory number, then
                                             		  recreate it. |
|---|---|

| Feature | Single-Line | Dual-Line | Octo-Line |
|---|---|---|---|
| Barge | — | — | Yes |
| Busy Trigger | — | — | Yes |
| Conferencing (8-party) | — | 4 directory numbers | 1 directory number |
| FXO Trunk Optimization | Yes | Yes | — |
| Huntstop Channel | — | Yes | Yes |
| Intercom | Yes | — | — |
| Key System (one call per button) | Yes | — | — |
| Maximum Calls | — | — | Yes |
| MWI | Yes | — | — |
| Overlay directory numbers (c, o, x) | Yes | Yes | — |
| Paging | Yes | — | — |
| Park | Yes | — | — |
| Privacy | — | — | Yes |

| Note | When the no supplementary-service
                                                   				sip handle-replaces command is configured, SIP shared-line is not
                                             		  supported on CME. |
|---|---|

| Note | Transcoding is
                                             		  not supported for Shared Lines. From Unified CME Release 12.2, you can use
                                             		  Voice Class Codec (VCC) with shared lines. |
|---|---|

| Note | Only the conference creator, who put a conference call on hold, can
                                                		  resume the conference call. |
|---|---|

| Note | It is mandatory that password is configured before DN range
                                          		  (auto-assign) while registering phones using auto registration. |
|---|---|

| Note | We recommend that administrators choose different DN ranges for
                                          		  manually configured and auto configured phones. |
|---|---|

| Note | Typically, Cisco Unified CME does not attempt a transfer that causes
                                          		  the caller (transferee) to hear a busy tone. However, the system does not check
                                          		  the state of subsequent target numbers in the call-forward path when the
                                          		  transferred call is transferred more than once. Multiple transfers can occur
                                          		  because a call-forward-busy target is also busy and configured for Call Forward
                                          		  Busy. |
|---|---|

| Note | Left shift the MAC address by two places, and append the two removed digits at the end with 01 to define the shifted MAC address.
                                                For example, the MAC address DCEB.941C.F33D is modified to get the shifted MAC address, EB94.1CF3.3D01 . |
|---|---|

| Note | When using Cisco Unified CME, you can configure FXS ports in H.323
                                             		  mode for call waiting or hookflash transfer, but not both at the same time. |
|---|---|

| Device Type | STU | STE | IP-STE |
|---|---|---|---|
| STU | Pass-through | Pass-through | None |
| STE | Pass-through | Pass-through | Relay |
| IP-STE | None | Relay | Relay |

| Note | When an ephone to non-ephone call is made, information on the
                                          		  non-ephone does not appear in a show ephone rtp connections command output.
                                          		  To display the non-ephone call information, use the show voip rtp connections command. |
|---|---|

| Supported
                                             					 Device | device-id | device-type | num-buttons | max-presentation |
|---|---|---|---|---|
| Cisco
                                             					 Unified Wireless IP Phone 7926G | 577 | 7926 | 6 | 2 |

| Note | The CLI command service phone lineMode is case-sensitive, and must be entered exactly as mentioned. |
|---|---|

| Phone Model | Number of KEM Lines Supported | Line Support (With SLM) | Line Support (With ELM) |
|---|---|---|---|
| 8851 | 56 (2*28) | 61 (56+5) | 66 (56+10) |
| 8851NR | 56(2*28) | 61 (56+5) | 66 (56+10) |
| 8861 | 84 (3*28) | 89 (84+5) | 94 (84+10) |
| 8865 | 84 (3*28) | 89 (84+5) | 94 (84+10) |

| Note | A mixed deployment of KEM Modules is not supported for any phone type. For example, if the phone type 8861 supports three
                                          KEM modules, then all three KEM modules have to be either CKEM, BEKEM, or CP-8800-Audio. |
|---|---|

| Note | To deploy Cisco
                                          		  Unified SIP IP phones on Cisco Unified CME using the fast-track configuration
                                          		  approach, you require Cisco IOS Release 15.3(3)M or a later release. |
|---|---|

| Note | To create and assign directory numbers to be included in an
                                          		  overlay set, see Configure Overlaid Ephone-dns on SCCP Phones . |
|---|---|

| Restriction | The
                                                   				  Cisco Unified IP Phone 7931G is a SCCP keyset phone and, when configured for a
                                                   				  key system, does not support the dual-line option for a directory number. To
                                                   				  configure a Cisco Unified IP Phone 7931G, see Configure Phones for a Key System . Octo-line
                                                   				  directory numbers are not supported by the Cisco Unified IP Phone 7902, 7920,
                                                   				  or 7931, or by analog phones connected to the Cisco VG224 or Cisco ATA. Octo-line
                                                   				  directory numbers are not supported in button overlay sets. Octo-line
                                                   				  directory numbers do not support the trunk command. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-dn dn-tag [ dual-line \| octo-line ] Example: Router(config)# ephone-dn 7 octo-line | Enters
                                             				ephone-dn configuration mode to create a directory number for a SCCP phone. dual-line —(Optional) Enables two calls per
                                                   					 directory number. Supports features such as call waiting, call transfer, and
                                                   					 conferencing with a single ephone-dn. octo-line —(Optional) Enables eight calls per
                                                   					 directory number. Supported in Cisco Unified CME 4.3 and later versions. To change
                                                   					 the line mode of a directory number, for example from dual-line to octo-line or
                                                   					 the reverse, you must first delete the ephone-dn and then recreate it. |
| Step 4 | number number [ secondary number ] [ no-reg [ both \| primary ] ] Example: Router(config-ephone-dn)# number 2001 | Configures an
                                             				extension number for this directory number. Configuring a secondary number supports features such as call
                                                   					 waiting, call transfer, and conferencing with a single ephone-dn. |
| Step 5 | huntstop [ channel number ] Example: Router(config-ephone-dn)# huntstop channel 4 | (Optional)
                                             				Enables Channel Huntstop, which keeps a call from hunting to the next channel
                                             				of a directory number if the first channel is busy or does not answer. channel number —Number of channels available to accept
                                                   					 incoming calls. Remaining channels are reserved for outgoing calls and features
                                                   					 such as call transfer, call waiting, and conferencing. Range: 1 to 8. Default:
                                                   					 8. number argument is supported for octo-line directory numbers only. |
| Step 6 | name name Example: Router(config-ephone-dn)# name Smith, John | (Optional)
                                             				Associates a name with this directory number. Name is
                                                   					 used for caller-ID displays and in the local directory listings. Must
                                                   					 follow the name order that is specified with the directory command. |
| Step 7 | end Example: Router(config-ephone-dn)# end | Returns to
                                             				privileged EXEC mode. |

| Restriction | Ephone-type templates are not supported for system-defined phone
                                          		  types. For a list of system-defined phone types, see the type command
                                          		  in Cisco Unified CME Command
                                             			 Reference . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-type phone-type [ addon ] Example: Router(config)# ephone-type E61 | Enters
                                             				ephone-type configuration mode to create an ephone-type template. phone-type —Unique label that identifies the type
                                                   					 of IP phone for which the phone-type template is being defined. addon —(Optional) Phone type is an add-on module,
                                                   					 such as the Cisco Unified IP Phone 7915 Expansion Module. |
| Step 4 | device-id number Example: Router(config-ephone-type)# device-id 376 | Specifies the
                                             				device ID for the phone type. This
                                                   					 device ID must match the predefined device ID for the specific phone model. If this
                                                   					 command is set to the default value of 0, the ephone-type is invalid. See Table 1 for a list of supported device IDs. |
| Step 5 | device-name name Example: Router(config-ephone-type)# device-name E61 Mobile Phone | Assigns a name
                                             				to the phone type. See Table 1 for a list of supported device types. |
| Step 6 | device-type phone-type Example: Router(config-ephone-type)# device-type E61 | Specifies the
                                             				device type for the phone. |
| Step 7 | num-buttons number Example: Router(config-ephone-type)# num-buttons 1 | Number of line
                                             				buttons supported by the phone type. number —Range: 1 to 100. Default: 0. See Table 1 for the number of buttons supported by each phone type. |
| Step 8 | max-presentation number Example: Router(config-ephone-type)# max-presentation 1 | Number of
                                             				call presentation lines supported by the phone type. number —Range: 1 to 100. Default: 0. See Table 1 for the number of presentation lines supported by each phone type. |
| Step 9 | addon Example: Router(config-ephone-type)# addon | (Optional)
                                             				Specifies that this phone type supports an add-on module, such as the Cisco
                                             				Unified IP Phone 7915 Expansion Module. |
| Step 10 | security Example: Router(config-ephone-type)# security | (Optional)
                                             				Specifies that this phone type supports security features. This
                                                   					 command is enabled by default. |
| Step 11 | phoneload Example: Router(config-ephone-type)# phoneload | (Optional)
                                             				Specifies that this phone type requires that the load command be configured. This
                                                   					 command is enabled by default. |
| Step 12 | utf8 Example: Router(config-ephone-type)# utf8 | (Optional)
                                             				Specifies that this phone type supports UTF8. This
                                                   					 command is enabled by default. |
| Step 13 | end Example: Router(config-ephone-type)# end | Exits to
                                             				privileged EXEC mode. |

| Supported
                                                					 Device | device-id | device-type | num-buttons | max-presentation |
|---|---|---|---|---|
| Cisco Unified IP  Phoone 6901 | 547 | 6901 | 1 | 1 |
| Cisco Unified IP  Phone 6911 | 548 | 6911 | 10 | 1 |
| Cisco
                                                					 Unified IP Phone 6945 | 564 | 6945 | 4 | 2 |
| Cisco Unified IP Phone 7915 Expansion Module with 12 buttons | 227 | 7915 | 12 | 0
                                                					 (default) |
| Cisco Unified IP  Phone 7915 Expansion Module with 24 buttons | 228 | 7915 | 24 | 0 |
| Cisco Unified IP  Phone 7916 Expansion Module with 12 buttons | 229 | 7916 | 12 | 0 |
| Cisco Unified IP  Phone 7916 Expansion Module with 24 buttons | 230 | 7916 | 24 | 0 |
| Cisco Unified  Wireless IP Phone  7925 | 484 | 7925 | 6 | 4 |
| Cisco
                                                					 Unified IP Conference  Station 7937G | 431 | 7937 | 1 | 6 |
| Cisco
                                                					 Unified IP Phone 8941 | 586 | 8941 | 4 | 3 |
| Cisco
                                                					 Unified IP Phone 8945 | 585 | 8945 | 4 | 3 |
| Cisco
                                                					 Unified IP Phone 8941 with Fast-Track configuration support | 586 | 8941 | 4 | 3 |
| Cisco
                                                					 Unified IP Phone 8945 with Fast-Track configuration support | 586 | 8945 | 4 | 3 |
| Nokia
                                                					 E61 | 376 | E61 | 1 | 1 |

| Note | To create and
                                             			 assign directory numbers to be included in an overlay set, see Configure Overlaid Ephone-dns on SCCP Phones . |
|---|---|

| Restriction | For Watch
                                                   				  mode. If the watched directory number is associated with several phones, then
                                                   				  the watched phone is the one on which the watched directory number is on button
                                                   				  1 or the one on which the watched directory number is on the button that is
                                                   				  configured by using the auto-line command, with auto-line having priority. For
                                                   				  configuration information, see Automatic Line Selection . Octo-line
                                                   				  directory numbers are not supported by the Cisco Unified IP Phone 7902, 7920,
                                                   				  or 7931, or by analog phones connected to the Cisco VG224 or Cisco ATA. Octo-line
                                                   				  directory numbers are not supported in button overlay sets. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone phone-tag Example: Router(config)#ephone 6 | Enters ephone
                                             				configuration mode. phone-tag —Unique sequence number that identifies
                                                   					 this ephone during configuration tasks. The maximum number of ephones is
                                                   					 version and platform-specific. Type ? to display
                                                   					 range. |
| Step 4 | mac-address [ mac-address ] Example: Router(config-ephone)#mac-address 2946.3f2.311 | Specifies the
                                             				MAC address of the IP phone that is being configured. mac-address —(Optional) For CiscoUnifiedCME 3.0 and
                                                   					 later versions, it is not required to register phones before configuring the
                                                   					 phone because CiscoUnifiedCME can detect MAC addresses and automatically
                                                   					 populate phone configurations with the MAC addresses and phone types for
                                                   					 individual phones. Not supported for voice-mail ports. |
| Step 5 | type phone-type [ addon 1 module-type [ 2 module-type ] ] Example: Router(config-ephone)# type 7960 addon 1 7914 | Specifies the
                                             				type of phone. CiscoUnifiedCME 4.0 and later versionsThe only types to which
                                                   					 you can apply an add-on module are 7960 , 7961 , 7961GE , and 7970 . CiscoCME
                                                   					 3.4 and earlier versionsThe only type to which you can apply an add-on module
                                                   					 is 7960 . |
| Step 6 | button button-number { separator } dn-tag [ , dn-tag... ] [ button-number { x } overlay-button-number ] [ button-number... ] Example: Router(config-ephone)# button 1:10 2:11 3b12 4o13,14,15 | Associates
                                             				a button number and line characteristics with an extension (ephone-dn). Maximum
                                             				number of buttons is determined by phone type. Note The
                                                         				  CiscoUnified IPPhone7910 has only one line button but can be given two
                                                         				  ephone-dn tags. | Note | The
                                                         				  CiscoUnified IPPhone7910 has only one line button but can be given two
                                                         				  ephone-dn tags. |
| Note | The
                                                         				  CiscoUnified IPPhone7910 has only one line button but can be given two
                                                         				  ephone-dn tags. |
| Step 7 | max-calls-per-button number Example: Router(config-ephone)# max-calls-per-button 3 | (Optional)
                                             				Sets the maximum number of calls, incoming and outgoing, allowed on an
                                             				octo-line directory number on this phone. number —Range: 1 to 8. Default: 8. This
                                                   					 command is supported in CiscoUnifiedCME4.3 and later versions. This
                                                   					 command must be set to a value that is more than or equal to the value set with
                                                   					 the busy-trigger-per-button command. This
                                                   					 command can also be configured in ephone-template configuration mode and
                                                   					 applied to one or more phones. The ephone configuration has priority over the
                                                   					 ephone-template configuration. |
| Step 8 | busy-trigger-per-button number Example: Router(config-ephone)# busy-trigger-per-button 2 | (Optional)
                                             				Sets the maximum number of calls allowed on this phones octo-line directory
                                             				numbers before triggering Call Forward Busy or a busy tone. number —Range: 1 to 8. Default: 0 (disabled). This
                                                   					 command is supported in CiscoUnifiedCME4.3 and later versions. After
                                                   					 the number of existing calls, incoming and outgoing, on an octo-line directory
                                                   					 number exceeds the number of calls set with this command, the next incoming
                                                   					 call to the directory number is forwarded to the Call Forward Busy destination
                                                   					 if configured, or the call is rejected with a busy tone. This
                                                   					 command must be set to a value that is less than or equal to the value set with
                                                   					 the max-calls-per-button command. This
                                                   					 command can also be configured in ephone-template configuration mode and
                                                   					 applied to one or more phones. The ephone configuration has priority over the
                                                   					 ephone-template configuration. |
| Step 9 | keypad-normalize Example: Router(config-ephone)# keypad-normalize | (Optional)
                                             				Imposes a 200-millisecond delay before each keypad message from an IP phone. When
                                                   					 used with the nte-end-digit-delay command, this command ensures
                                                   					 that the delay configured for a dtmf-end event is always honored. |
| Step 10 | nte-end-digit-delay [ milliseconds ] Example: Router(config-ephone)# nte-end-digit-delay 150 | (Optional)
                                             				Specifies the amount of time that each digit in the RTP NTE end event in an
                                             				RFC2833 packet is delayed before being sent. This
                                                   					 command is supported in CiscoUnifiedCME 4.3 and later versions. milliseconds —length of delay. Range: 10 to 200.
                                                   					 Default: 200. To
                                                   					 enable the delay, you must also configure the dtmf-interworking
                                                         						  rtp-nte command in voice-service or dial-peer configuration mode.
                                                   					 For information, see Enable DTMF Integration Using RFC 2833 . This
                                                   					 command can also be configured in ephone-template configuration mode. The value
                                                   					 set in ephone configuration mode has priority over the value set in
                                                   					 ephone-template mode. |
| Step 11 | end Example: Router(config-ephone)# end | Returns to
                                             				privileged EXEC mode. |

| Note | The
                                                         				  CiscoUnified IPPhone7910 has only one line button but can be given two
                                                         				  ephone-dn tags. |
|---|---|

| Restriction | Valid characters in voice register DN include 0–9, '.', '+', '*', and '#'. The name or label that is associated with a directory number that is configured under voice register dn or voice register global configuration mode cannot contain special characters such as quotes ("), angle brackets (<, >), ampersand (&), and percentage
                                                   (%). To allow insertion of '#' at any place in voice register DN, the CLI "allow-hash-in-dn" is configured in voice register global
                                                   mode. When the CLI
                                                   				  "allow-hash-in-dn" is configured, the user is required to change the dial-peer
                                                   				  terminator from '#' (default terminator) to another valid terminator in
                                                   				  configuration mode. The other terminators that are supported include '0'-'9',
                                                   				  'A'-'F', and '*'. Maximum number of directory numbers that are supported by a router is version and platform dependent. Call Forward
                                                   				  All, Presence, and message-waiting indication (MWI) features in Cisco Unified
                                                   				  CME 4.1 and later versions require that SIP phones be configured with a
                                                   				  directory number using the dn keyword
                                                   				  with the number command; direct line numbers are not supported. SIP
                                                   				  endpoints are not supported on H.323 trunks. SIP endpoints are supported on SIP
                                                   				  trunks only. The Media
                                                   				  Flow-around feature configured with the media
                                                         						flow-around command is not supported by Cisco Unified CME with
                                                   				  SIP phones. SIP shared-line directory numbers are not supported by the Cisco Unified IP Phone 7902, 7920, 7931, 7940, or 7960, or by analog
                                                   phones connected to the Cisco VG224. For Unified
                                                   				  CME 12.1 and prior releases, SIP shared-line directory numbers cannot be
                                                   				  members of voice hunt groups. If this directory number is used as shared line, you can associate the directory number to a maximum of 16 phones. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register dn dn-tag Example: Router(config)# voice register dn 17 | Enters voice register DN configuration mode to define a directory number for a SIP phone, intercom line, voice port, or a
                                             message-waiting indicator (MWI). |
| Step 4 | number number Example: Router(config-register-dn)# number 7001 | Defines a
                                             				valid number for a directory number. |
| Step 5 | shared-line [ max-calls number-of-calls ] Example: Router(config-register-dn)# shared-line max-calls 6 | (Optional)
                                             				Creates a shared-line directory number. max-calls number-of-calls (Optional)—Maximum number of calls, both incoming and outgoing. Range: 2–16. Default: 2. Must be
                                                   					 set to a value that is more than or equal to the value set with the busy-trigger-per-button command. This
                                                   					 command is supported in Cisco Unified CME 7.1 and later versions. |
| Step 6 | huntstop channel number-of-channels Example: Router(config-register-dn)# huntstop channel 3 | (Optional)
                                             				Enables Channel Huntstop, which keeps a call from hunting to the next channel
                                             				of a directory number if the first channel is busy or does not answer. number-of-channels —Number of channels available to accept incoming calls on the directory number. Remaining channels are reserved for outgoing
                                                   calls and features, such as Call Transfer, Call Waiting, and Conferencing. Range: 1–50. Default: 0 (disabled). This
                                                   					 command is supported in Cisco Unified CME 7.1 and later versions. |
| Step 7 | end Example: Router(config-register-dn)# end | Exits to
                                             				privileged EXEC mode. |

| Note | If your
                                             			 Cisco Unified CME system supports SCCP and SIP phones, do not connect your SIP
                                             			 phones to your network until after you have verified the configuration profile
                                             			 for the SIP phone. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register pool pool-tag Example: Router(config)# voice register pool 3 | Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone. |
| Step 4 | id { network address mask mask \| ip address mask mask \| mac address } Example: Router(config-register-pool)#
			 id mac 0009.A3D4.1234 | Explicitly
                                             				identifies a locally available individual SIP phone to support a degree of
                                             				authentication. |
| Step 5 | type phone-type Example: Router(config-register-pool)# type 7960-7940 | Defines a
                                             				phone type for the SIP phone being configured. |
| Step 6 | number tag dn dn-tag Example: Router(config-register-pool)# number 1 dn 17 | Associates a
                                             				directory number with the SIP phone being configured. dn dn-tag —identifies the directory number for this
                                                   					 SIP phone as defined by the voice register
                                                         						  dn command. |
| Step 7 | busy-trigger-per-button number-of-calls Example: Router(config-register-pool)# busy-trigger-per-button 2 | (Optional)
                                             				Sets the maximum number of calls allowed on any of this phone�s directory
                                             				numbers before triggering Call Forward Busy or a busy tone. number-of-calls —Maximum number of calls allowed
                                                   					 before Cisco Unified CME forwards the next incoming call to the Call Forward
                                                   					 Busy destination, if configured, or rejects the call with a busy tone. Range: 1
                                                   					 to 50. This
                                                   					 command is supported in Cisco Unified CME 7.1 and later versions. |
| Step 8 | username username password password Example: Router(config-register-pool)# username smith password 123zyx | (Optional)
                                             				Required only if authentication is enabled with the authenticate command. Creates an authentication
                                             				credential. Note This
                                                         				  command is not for SIP proxy registration. The password will not be encrypted.
                                                         				  All lines in a phone will share the same credential. username —identifies a local Cisco Unified IP phone
                                                   					 user. Default: Admin. | Note | This
                                                         				  command is not for SIP proxy registration. The password will not be encrypted.
                                                         				  All lines in a phone will share the same credential. |
| Note | This
                                                         				  command is not for SIP proxy registration. The password will not be encrypted.
                                                         				  All lines in a phone will share the same credential. |
| Step 9 | dtmf-relay { [ cisco-rtp ] [ rtp-nte ] [ sip-notify ] } Example: Router(config-register-pool)# dtmf-relay rtp-nte | (Optional)
                                             				Specifies a list of DTMF relay methods that can be used by the SIP phone to
                                             				relay DTMF tones. Note SIP phones
                                                         				  natively support in-band DTMF relay as specified in RFC 2833. | Note | SIP phones
                                                         				  natively support in-band DTMF relay as specified in RFC 2833. |
| Note | SIP phones
                                                         				  natively support in-band DTMF relay as specified in RFC 2833. |
| Step 10 | end Example: Router(config-register-pool)# end | Returns to
                                             				privileged EXEC mode. |

| Note | This
                                                         				  command is not for SIP proxy registration. The password will not be encrypted.
                                                         				  All lines in a phone will share the same credential. |
|---|---|

| Note | SIP phones
                                                         				  natively support in-band DTMF relay as specified in RFC 2833. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register dialplan dialplan-tag Example: Router(config)# voice register dialplan 1 | Enters voice
                                             				register dialplan configuration mode to define a dial plan for SIP phones. |
| Step 4 | type phone-type Example: Router(config-register-dialplan)# type 7905-7912 | Defines a
                                             				phone type for the SIP dial plan. 7905-7912 —Cisco Unified IP Phone 7905, 7905G,
                                                   					 7912, or 7912G. 7940-7960-others —Cisco Unified IP Phone 7911,
                                                   					 7940, 7940G, 7941, 7941GE, 7960, 7960G, 7961, 7961GE, 7970, or 7971. The phone
                                                   					 type specified with this command must match the type of phone for which the
                                                   					 dial plan is used. If this phone type does not match the type assigned to the
                                                   					 phone with the type command
                                                   					 in voice register pool mode, the dial-plan configuration file is not generated. You must
                                                   					 enter this command before using the pattern or filename command in the next step. |
| Step 5 | pattern tag string [ button button-number ] [ timeout seconds ] [ user { ip \| phone } ] or filename filename Example: Router(config-register-dialplan)# pattern 1 52... or Router(config-register-dialplan)# filename dialsip | Defines a dial
                                             				pattern for a SIP dial plan. tag —Number that identifies the dial pattern.
                                                   					 Range: 1 to 24. string —Dial pattern, such as the area code,
                                                   					 prefix, and first one or two digits of the telephone number, plus wildcard
                                                   					 characters or dots (.) for the remainder of the dialed digits. button button-number —(Optional) Button to which the dial
                                                   					 pattern applies. timeout seconds —
                                                   					 (Optional) Time, in seconds, that the system waits before dialing the number
                                                   					 entered by the user. Range: 0 to 30. To have the number dialed immediately,
                                                   					 specify 0. If you do not use this parameter, the phone's default interdigit
                                                   					 timeout value is used (10 seconds). user —(Optional) Tag that automatically gets added
                                                   					 to the dialed number. Do not use this keyword if Cisco Unified CME is the only
                                                   					 SIP call agent. ip —Uses the
                                                   					 IP address of the user. phone —Uses
                                                   					 the phone number of the user. Repeat
                                                   					 this command for each pattern that you want to include in this dial plan. or Specifies a
                                             				custom XML file that contains the dial patterns to use for the SIP dial plan. You must
                                                   					 load the custom XML file must into flash and the filename cannot include the
                                                   					 .xml extension. The filename command is not supported for the Cisco Unified IP Phone 7905 or 7912. |
| Step 6 | exit Example: Router(config-register-dialplan)# exit | Exits
                                             				dialplan configuration mode. |
| Step 7 | voice register pool pool-tag Example: Router(config)# voice register pool 4 | Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone. pool-tag —Unique sequence number of the SIP phone
                                                				  to be configured. Range is version and platform-dependent; type ? to
                                                				  display range. You can modify the upper limit for this argument by using the
                                                				  the max-pool command. |
| Step 8 | dialplan dialplan-tag Example: Router(config-register-pool)# dialplan 1 | Assigns a
                                             				dial plan to a SIP phone. dialplan-tag —Number that identifies the dial plan
                                                   					 to use for this SIP phone. This is the number that was used with the voice register
                                                         						  dialplan command in Step 3. Range: 1 to 24. |
| Step 9 | end Example: Router(config-register-global)# end | Exits to
                                             				privileged EXEC mode. |

| Step 1 | show voice register dialplan tag This command displays the configuration information for a specific
                                             				SIP dial plan. Example: Router# show voice register dialplan 1 Dialplan Tag 1
Config:
  Type is 7940-7960-others
  Pattern 1 is 2..., timeout is 10, user option is ip, button is default
  Pattern 2 is 1234, timeout is 0, user option is ip, button is 4
  Pattern 3 is 65..., timeout is 0, user option is phone, button is default
  Pattern 4 is 1..., timeout is 0, user option is phone, button is default |
|---|---|
| Step 2 | show voice register pool tag This command displays the dial plan assigned to a specific SIP
                                             				phone. Example: Router# show voice register pool 29 Pool Tag 29
Config:
  Mac address is 0012.7F54.EDC6
  Number list 1 : DN 29
  Proxy Ip address is 0.0.0.0
  DTMF Relay is disabled
  Call Waiting is enabled
  DnD is disabled
  keep-conference is enabled
  dialplan tag is 1
  kpml signal is enabled
  service-control mechanism is not supported
.
.
. |
| Step 3 | show voice register template tag This command displays the dial plan assigned to a specific
                                             				template. Example: Router# show voice register template 3 Temp Tag 3
Config:
  Attended Transfer is disabled
  Blind Transfer is enabled
  Semi-attended Transfer is enabled
  Conference is enabled
  Caller-ID block is disabled
  DnD control is enabled
  Anonymous call block is disabled
  Voicemail is 62000, timeout 15
  Dialplan Tag is 1
  Transport type is tcp |

| Restriction | This feature
                                                   				  is supported only on Cisco Unified IP Phones 7911G, 7941G, 7941GE, 7961G,
                                                   				  7961GE, 7970G, and 7971GE. A dial plan
                                                   				  assigned to a phone has priority over KPML. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register pool pool-tag Example: Router(config)# voice register pool 4 | Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone. pool-tag —Unique sequence number of the SIP phone
                                                   					 to be configured. Range is version and platform-dependent; type ? to
                                                   					 display range. You can modify the upper limit for this argument by using the max-pool command. |
| Step 4 | digit collect kpml Example: Router(config-register-pool)# digit collect kpml | Enables KPML
                                             				digit collection for the SIP phone. Note This command
                                                         				  is enabled by default for supported phones in Cisco Unified CME. | Note | This command
                                                         				  is enabled by default for supported phones in Cisco Unified CME. |
| Note | This command
                                                         				  is enabled by default for supported phones in Cisco Unified CME. |
| Step 5 | end Example: Router(config-register-pool)# end | Exits to
                                             				privileged EXEC mode. |
| Step 6 | show voice register dial-peers Example: Router# show voice register dial-peers | Displays
                                             				details of all dynamically created VoIP dial peers associated with the Cisco
                                             				Unified CME SIP register, including the defined digit collection method. |

| Note | This command
                                                         				  is enabled by default for supported phones in Cisco Unified CME. |
|---|---|

| Restriction | TCP is not
                                                   				  supported as a session-transport protocol for the Cisco Unified IP Phone 7905,
                                                   				  7912, 7940, or 7960. If TCP is assigned to an unsupported phone, calls to that
                                                   				  phone will not complete successfully. However, the phone can originate calls
                                                   				  using UDP, although TCP has been assigned. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register pool pool-tag Example: Router(config)# voice register pool 3 | Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone in Cisco Unified CME. |
| Step 4 | session-transport { tcp \| udp } Example: Router(config-register-pool)# session-transport tcp | (Optional)
                                             				Specifies the transport layer protocol that a SIP phone uses to connect to
                                             				Cisco Unified CME. This
                                                   					 command can also be configured in voice register template configuration mode
                                                   					 and applied to one or more phones. The voice register pool configuration has
                                                   					 priority over the voice register template configuration. |
| Step 5 | end Example: Router(config-register-pool)# end | Exits voice
                                             				register pool configuration mode and enters privileged EXEC mode. |

| Note | When TCP is used as session-transport for the SIP phones, and if
                                          		  the TCP Connection aging timer is less than the SIP Register expire timer; then
                                          		  after every TCP connection aging timer expires, the phone will be reset and
                                          		  will re-register to CME. If this is not desired, then modify the TCP Connection
                                          		  aging timer and/or SIP Register expire timer so that SIP Register expire timer
                                          		  is less than TCP Connection aging timer. |
|---|---|

| Restriction | Phone numbers that are registered under a voice register dn must belong to a SIP phone that is registered in Cisco Unified CME. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice register dn dn-tag Example: Router(config-register-global)# voice register dn 1 | Enters voice register dn configuration mode to define a directory number for a SIP phone, intercom line, voice port, or an
                                             MWI. |
| Step 4 | number number Example: Router(config-register-dn)# number 4085550152 | Defines a valid number for a directory number to be assigned to a SIP phone in Cisco Unified CME. |
| Step 5 | no-reg Example: Router(config-register-dn)# no-reg | Prevents directory number being configured from registering with an external proxy server. |
| Step 6 | end Example: Router(config-register-dn)# end | Exits voice register dn configuration mode and enters privileged EXEC mode. |

| Restriction | If G.722-64K codec is configured globally and a phone does not
                                          		  support the codec, the fallback codec is G.711ulaw. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony service configuration mode to set parameters for SCCP and SIP phones
                                             				in Cisco Unified CME. |
| Step 4 | codec { g711-ulaw \| g722-64k } Example: Router(config-telephony)# codec g722-64k | Specifies the
                                             				preferred codec for phones in Cisco Unified CME. Required
                                                   					 only if you want to modify codec from the default (G.711ulaw) to G.722-64K. |
| Step 5 | service phone g722CodecSupport { 0 \| 1 \| 2 } Example: Router(config)# service phone g722CodecSupport 2 | Causes all
                                             				phones to advertise the G.722-64K codec to Cisco Unified CME. Required
                                                   					 only if you configured the codec g722-64k command in telephony-service configuration mode. g722CodecSupport —Default: 0, phone default set by
                                                   					 manufacturer and equal to enabled or disabled. Cisco
                                                   					 phone firmware 8.2.1 or a later version is required to support the G.722-64K
                                                   					 codec on G.722-capable SCCP phones. Cisco
                                                   					 phone firmware 8.3.1 or a later version is required to support the G.722-64K
                                                   					 codec on G.722-capable SIP phones. For SCCP
                                                   					 only: This command can also be configured in ephone- template configuration
                                                   					 mode and applied to one or more SCCP phones. |
| Step 6 | end Example: Router(config-telephony)# end | Exits the
                                             				telephony service configuration mode and enters privileged EXEC mode. |

| Note | If codec values
                                          		  for the dial peers of an internal connection do not match, the call fails. For
                                          		  calls to external phones, that is, phones that are not in the same
                                          		  Cisco Unified CME, such as VoIP calls, the codec is negotiated based on the
                                          		  protocol that is used for the call, such as H.323. Cisco Unified CME plays no
                                          		  part in the negotiation. |
|---|---|

| Restriction | Not all
                                                   				  phones support all codecs. To verify whether your phone supports a particular
                                                   				  codec, see your phone documentation. For SIP and
                                                   				  SCCP phones in Cisco Unified CME: Modify the configuration for either SIP or
                                                   				  SCCP phones to ensure that the codec for all phones match. Do not modify the
                                                   				  configuration for both SIP and SCCP phones. If G.729 is
                                                   				  the desired codec for Cisco ATA-186 and Cisco ATA-188, then only one port of
                                                   				  the Cisco ATA device should be configured in Cisco Unified CME. If a call is
                                                   				  placed to the second port of the Cisco ATA device, it will be disconnected
                                                   				  gracefully. If you want to use both Cisco ATA ports simultaneously, then
                                                   				  configure G.711 in Cisco Unified CME. If G.722-64K
                                                   				  or iLBC codecs are configured in ephone configuration mode and the phone does
                                                   				  not support the codec, the fallback is the global codec or G.711ulaw if the
                                                   				  global codec is not supported. To configure a global codec, see Modify the Global Codec . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter
                                                   					 your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone ephone-tag or voice register pool pool-tag Example: Router(config)# voice register pool 1 | Enters ephone
                                             				configuration mode to set phone-specific parameters for a SCCP phone in Cisco
                                             				Unified CME. or Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone in Cisco Unified CME. |
| Step 4 | codec codec-type Example: Router(config-ephone)# codec g729r8 
or 
Router(config-register-pool)# codec g711alaw | Specifies the
                                             				codec for the dial peer for the IP phone being configured. codec-type —Type ? for a list of codecs. This
                                                   					 command overrides any previously configured codec selection set with the voice-class codec command. This
                                                   					 command overrides any previously configured codec selection set with the codec command
                                                   					 in telephony-service configuration mode. SCCP
                                                   					 only—This command can also be configured in ephone-template configuration mode
                                                   					 and applied to one or more phones. |
| Step 5 | end Example: Router(config-ephone)# end or Router(config-register-pool)# end | Exits the
                                             				configuration mode and enters privileged EXEC mode. |

| Restriction | Do not
                                                   				  configure directory numbers for a key system for dual-line mode because this
                                                   				  does not conform to the key system one-call-per-line button usage model for
                                                   				  which the phone is designed. Provisioning
                                                   				  support for the Cisco Unified IP Phone 7931 is available only in
                                                   				  Cisco Unified CME 4.0(2) and later versions. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-dn dn-tag Example: Router(config)# ephone-dn 11 | Enters
                                             				ephone-dn configuration mode to create a directory number. |
| Step 4 | number number [ secondary number ] [ no-reg [ both \| primary ] ] Example: Router(config-ephone-dn)# number 101 | Configures a
                                             				valid phone or extension number for this directory number. |
| Step 5 | preference preference-order Example: Router(config-ephone-dn)# preference 1 | Sets dial-peer
                                             				preference order for a directory number associated with a Cisco Unified IP
                                             				phone. Default:
                                                   					 0. Increments
                                                   					 the preference order for all subsequent instances within a set of ephone dns
                                                   					 with the same number to be associated with a key system phone. That is, the
                                                   					 first instance of the directory number is preference 0 by default
                                                   					 and you must specify 1 for the
                                                   					 second instance of the same number, 2 for the
                                                   					 next, and so on. This allows you to create multiple buttons with the same
                                                   					 number on an IP phone. Required
                                                   					 to support call waiting and call transfer on a key system phone. |
| Step 6 | no huntstop or huntstop Example: Router(config-ephone-dn)# no huntstop or Router(config-ephone-dn)# huntstop | Explicitly
                                             				enables call hunting behavior for a directory number. Configure no huntstop for all instances, except the final instance, within a set of ephone dns with
                                                   					 the same number to be associated with a key system phone. Required
                                                   					 to allow call hunting across multiple line buttons with the same number on an
                                                   					 IP phone. or Disables call
                                             				hunting behavior for a directory number. Configure
                                                   					 the huntstop command for the final instance within a set of ephone dns with the same number
                                                   					 to be associated with a key system phone. Required
                                                   					 to limit the call hunting to a set of multiple line buttons with the same
                                                   					 number on an IP phone. |
| Step 7 | mwi-type { visual \| audio \| both } Example: Router(config-ephone-dn)# mwi-type audible | Specifies
                                             				the type of MWI notification to be received. This
                                                   					 command is supported only by Cisco Unified IP Phone 7931s and Cisco Unified IP
                                                   					 Phone 7911s. This
                                                   					 command can also be configured in ephone-dn-template configuration mode. The
                                                   					 value set in ephone-dn configuration mode has priority over the value set in
                                                   					 ephone-dn-template mode. |
| Step 8 | end Example: Router(config-ephone-dn)# end | Exits to
                                             				privileged EXEC mode. |

| Restriction | Directory
                                                      				  number with a trunk line cannot be configured for call forward, busy, or no
                                                      				  answer. Numbers
                                                      				  entered after a trunk line is seized will not be displayed. Only the trunk tag
                                                      				  is displayed on IP phones. Numbers
                                                      				  entered after trunk line is seized will not appear in call history or call
                                                      				  detail records (CDRs) of a Cisco Unified CME router. Only the trunk tag is
                                                      				  logged for calls made from trunk lines. FXO trunk
                                                      				  lines do not support the CFwdALL, Transfer, Pickup, GPickUp, Park, CallBack,
                                                      				  and NewCall softkeys. FXO trunk
                                                      				  lines do not support conference initiator dropoff. FXO trunk
                                                      				  lines do not support on-hook redial. The phone user must explicitly select the
                                                      				  FXO trunk line before pressing the Redial button. FXO trunk
                                                      				  lines do not support call transfer to IP phones. However, the call initiator
                                                      				  can conference an FXO line with an IP phone by pressing the Hold button, which
                                                      				  leaves the FXO trunk line and IP phone connected. The conference initiator is
                                                      				  unable to participate in the conference, but can place calls on other lines. FXO trunk
                                                      				  lines do not support bulk speed dial. FXO port
                                                      				  monitoring has the following restrictions: Not
                                                            						supported before Cisco Unified CME 4.0. Supported only for analog FXO loop-start and ground-start ports
                                                            						and T1/E1 FXO CAS ports. FXS loop-start and ground-start ports and PRI/BRI PSTN
                                                            						trunks are not supported. Not
                                                            						supported for analog ports on the Cisco VG224 or Cisco ATA 180 Series. T1 CAS
                                                            						DS0 group must be configured per time slot (cannot bundle more than one time
                                                            						slot into a ds0-group). Transfer
                                                      				  recall and transfer-to button optimization are supported on dual-line directory
                                                      				  numbers only in Cisco Unified CME 4.0 and later versions. Transfer-to
                                                      				  button optimization is not supported for call forwarding, call-park recall,
                                                      				  call pickup on hold, or call pickup at alert. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                                				privileged EXEC mode. Enter
                                                      					 your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                                				configuration mode. |
| Step 3 | ephone-dn dn-tag Example: Router(config)# ephone-dn 51 | Enters
                                                				ephone-dn configuration mode to create a directory number. Configure this command in the default single line mode, without
                                                      					 the dual-line keyword, when configuring a simple key system trunk line. |
| Step 4 | number number [ secondary number ] [ no-reg [ both \| primary ] ] Example: Router(config-ephone-dn)# number 801 | Configures a
                                                				valid phone or extension number for this directory number. |
| Step 5 | trunk trunk-tag [ timeout seconds ] monitor-port port Example: Router(config-ephone-dn)# trunk 811 monitor-port 1/0/0 | Associates a
                                                				directory number with an FXO port. The monitor-port keyword is not supported before Cisco
                                                      					 Unified CME 4.0. The monitor-port keyword is not supported on directory
                                                      					 numbers for analog ports on the Cisco VG224 or Cisco ATA 180 Series. |
| Step 6 | end Example: Router(config-ephone-dn)# end | Returns to
                                                				privileged EXEC mode. |

| Restriction | Ephone-dn
                                                      				  with a trunk line cannot be configured for call forward, busy, or no answer. Numbers
                                                      				  entered after a trunk line is seized will not be displayed. Only the trunk tag
                                                      				  is displayed on IP phones. Numbers
                                                      				  entered after a trunk line is seized will not appear in call history or call
                                                      				  detail records (CDRs) of a Cisco Unified CME router. Only the trunk tag is
                                                      				  logged for calls made from trunk lines. FXO trunk
                                                      				  lines do not support the CFwdALL, Transfer, Pickup, GPickUp, Park, CallBack,
                                                      				  and NewCall softkeys. FXO trunk
                                                      				  lines do not support conference initiator dropoff. FXO trunk
                                                      				  lines do not support on-hook redial. The phone user must explicitly select the
                                                      				  FXO trunk line before pressing the Redial button. FXO trunk
                                                      				  lines do not support call transfer to IP phones. However, the call initiator
                                                      				  can conference an FXO line with an IP phone by pressing the Hold button, which
                                                      				  leaves the FXO trunk line and IP phone connected. The conference initiator is
                                                      				  unable to participate in the conference, but can place calls on other lines. FXO trunk
                                                      				  lines do not support bulk speed dial. FXO port
                                                      				  monitoring has the following restrictions: Not
                                                            						supported before Cisco Unified CME 4.0. Supported only for analog FXO loop-start and ground-start ports
                                                            						and T1/E1 FXO CAS ports. FXS loop-start and ground-start ports and PRI/BRI PSTN
                                                            						trunks are not supported. Not
                                                            						supported for analog ports on the Cisco VG224 or Cisco ATA 180 Series. T1 CAS
                                                            						DS0 group must be configured per time slot (cannot bundle more than one time
                                                            						slot into a ds0-group). Transfer
                                                      				  recall and transfer-to button optimization is supported on dual-line directory
                                                      				  numbers only in Cisco Unified CME 4.0 and later. Transfer-to
                                                      				  button optimization is not supported for call forwarding, call-park recall,
                                                      				  call pickup on hold, or call pickup at alert. Transfer
                                                      				  recall is not supported for analog ports on the Cisco VG224 or Cisco ATA 180
                                                      				  Series. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                                				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                                				configuration mode. |
| Step 3 | ephone-dn dn-tag dual-line Example: Router(config)# ephone-dn 51 dual-line | Enters
                                                				ephone-dn configuration mode for the purpose of creating and configuring a
                                                				telephone or extension number. dual-line —Required when configuring an advanced
                                                      					 key system phone trunk line. Dual-line mode provides a second call channel for
                                                      					 the directory number on which to place an outbound consultation call during the
                                                      					 call transfer attempt. This also allows the phone to remain part of the call to
                                                      					 monitor the progress of the transfer attempt and if the transfer is not
                                                      					 answered, to pull the call back to the phone on the original PSTN line button. |
| Step 4 | number number [ secondary number ] [ no-reg [ both \| primary ] ] Example: Router(config-ephone-dn)# number 801 | Configures a
                                                				valid telephone number or extension number for this directory number. |
| Step 5 | trunk digit-string [ timeout seconds ] [ transfer-timeout seconds ] [ monitor-port port ] Example: Router(config-ephone-dn)# trunk 811 transfer-timeout 30 monitor-port 1/0/0 | Associates
                                                				this directory number with an FXO port. transfer-timeout seconds —For dual-line ephone-dns only. Range: 5 to 60000.
                                                      					 Default: Disabled. The monitor-port keyword is not supported before Cisco
                                                      					 Unified CME 4.0. The monitor-port and transfer-timeout keywords are not supported on
                                                      					 directory numbers for analog ports on the Cisco VG224 or Cisco ATA 180 Series. |
| Step 6 | huntstop [ channel ] Example: Router(config-ephone-dn)# huntstop channel | Disables
                                                				call hunting to the second channel of this directory number if the first
                                                				channel is busy or does not answer. channel —Required when configuring an advanced key
                                                      					 system phone trunk line. Reserves the second channel created by configuring
                                                      					 dual-line mode for the ephone-dn command so that an outbound consultation call can be placed during a call
                                                      					 transfer attempt. |
| Step 7 | end Example: Router(config-ephone-dn)# end | Exits to
                                                				privileged EXEC mode. |

| Restriction | Provisioning
                                                   				  for Cisco Unified IP Phone 7931G is available only in Cisco Unified CME 4.0(2)
                                                   				  and later versions. Cisco Unified IP Phone 7931G can support only one call waiting
                                                   				  overlaid per directory number. Cisco Unified IP Phone 7931G cannot support overlays that
                                                   				  contain directory numbers configured for dual-line mode. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone phone-tag Example: Router(config)# ephone 1 | Enters ephone
                                             				configuration mode. |
| Step 4 | mac-address [ mac-address ] Example: Router(config-ephone)# mac-address 0001.2345.6789 | Specifies the
                                             				MAC address of the IP phone that is being configured. |
| Step 5 | type phone-type Example: Router(config-ephone)# type 7931 | Specifies the
                                             				type of phone that is being configured. |
| Step 6 | button button-number { separator } dn-tag [ ,dn-tag... ] [ button-number { x } overlay-button-number ] [ button-number... ] Example: Router(config-ephone)# button 1:11 2:12 3:13 4:14 5:15 6:16 7:51 8:52 9:53 10:54 | Associates a
                                             				button number and line characteristics with an ephone-dn. Maximum number of
                                             				buttons is determined by phone type. Tip The line
                                                         				  button layout for the Cisco Unified IP Phone 7931G is a bottom-up array. Button
                                                         				  1 is at the bottom right of the array and button 24 is at the top left of the
                                                         				  array. | Tip | The line
                                                         				  button layout for the Cisco Unified IP Phone 7931G is a bottom-up array. Button
                                                         				  1 is at the bottom right of the array and button 24 is at the top left of the
                                                         				  array. |
| Tip | The line
                                                         				  button layout for the Cisco Unified IP Phone 7931G is a bottom-up array. Button
                                                         				  1 is at the bottom right of the array and button 24 is at the top left of the
                                                         				  array. |
| Step 7 | mwi-line line-number Example: Router(config-ephone)# mwi-line 3 | Selects a
                                             				phone line to receive MWI treatment; when a message is waiting for the selected
                                             				line, the message waiting indicator is activated. line-number —Range: 1 to 34. Default: 1. |
| Step 8 | end Example: Router(config-ephone)# end | Exits ephone
                                             				configuration mode and enters privileged EXEC mode. |

| Tip | The line
                                                         				  button layout for the Cisco Unified IP Phone 7931G is a bottom-up array. Button
                                                         				  1 is at the bottom right of the array and button 24 is at the top left of the
                                                         				  array. |
|---|---|

| Restriction | For a Cisco ATA that is registered to a Cisco Unified CME system to participate in fax calls, it must have its ConnectMode
                                          parameter set to use the same RTP payload type as the Cisco voice gateway that is performing the fax pass-through. Cisco voice
                                          gateways use standard payload type 0/8, which is selected on Cisco ATAs by setting bit 2 of the ConnectMode parameter to 1.
                                          For more information, see the Parameters and Defaults chapter in Cisco ATA 186 and Cisco ATA 188 Analog Telephone Adaptor Administrator's Guide for SCCP (version 3.0) . |
|---|---|

| Step 1 | Install the Cisco ATA. See the Installing the Cisco ATA chapter in Cisco ATA 186 and Cisco ATA 188 Analog Telephone Adaptor Administrator's Guide for SCCP (version 3.0) . |
|---|---|
| Step 2 | Configure the Cisco ATA. See the Configuring the Cisco ATA for SCCP chapter in Cisco ATA 186 and Cisco ATA 188 Analog Telephone Adaptor Administrator's Guide for SCCP (version 3.0) . |
| Step 3 | Upgrade the firmware to the latest Cisco ATA image. If you are using either the v2.14 or v2.14ms Cisco ATA 186 image based on the 2.14 020315a build for H.323/SIP or the 2.14 020415a
                                             build for MGCP or SCCP, you must upgrade to the latest version to install a security patch. This patch fixes a security hole
                                             in the Cisco ATA Web server that allows users to bypass the user interface password. For information about upgrading firmware, see Install Cisco Unified CME Software . Alternatively, you can use a manual method, as described in the Upgrading the Cisco ATA Signaling Image chapter of Cisco ATA 186 and Cisco ATA 188 Analog Telephone Adaptor Administrator's Guide for SCCP (version 3.0) . |
| Step 4 | Set the following network parameters on the Cisco ATA: DHCP parameter to 1 (enabled). TFTP parameter to 1 (enabled). TFTPURL parameter to the IP address of the router running Cisco Unified CME. SID0 parameter to a period ( . ) or the MAC address of the Cisco ATA (to enable the first port). SID1 parameter to a period ( . ) or a modified version the Cisco ATA’s MAC address, with the first two hexadecimal numbers removed and 01 appended to the
                                                   end, if you want to use the second port. For example, if the MAC address of the Cisco ATA is 00012D01073D, set SID1 to 012D01073D01. Nprintf parameter to the IP address and port number of the host to which all Cisco ATA debug messages are sent. The port number
                                                   is usually set to 9001. To prevent tampering and unauthorized access to the Cisco ATA 186, you can disable the web-based configuration. However, if
                                                   you disable the web configuration page, you must use either a TFTP server or the voice configuration menu to configure the
                                                   Cisco ATA 186. |
| Step 5 | In Cisco Unified CME, configure analog phones that use a Cisco ATA in the same way as a Cisco Unified IP phone. In the type command, use the ata keyword. For information on how to provision phones, see Create Directory Numbers for SCCP Phones . |

| Restriction | For a Cisco ATA that is registered to a Unified CME system to participate in fax calls, it must have its ConnectMode parameter
                                                   set to use the same RTP payload type as the Cisco voice gateway that is performing the Fax pass-through. Cisco voice gateways
                                                   use standard payload type 0/8, which is selected on Cisco ATAs by setting bit 2 of the ConnectMode parameter to 1. For more
                                                   information, see the Configure Fax Services chapter in Cisco ATA 191 Analog Telephone Adapter Administration Guide for Cisco Unified Communications Manager . If both ports of a Cisco ATA 191 are configured as shared line, then a call put on hold on one port cannot be resumed at the
                                                   other port. |
|---|---|

| Step 1 | Install the Cisco ATA. See the Install the ATA 191 chapter in Cisco ATA 191 Analog Telephone Adapter Administration Guide for Cisco Unified Communications Manager . |
|---|---|
| Step 2 | Configure the Cisco ATA. See the Configure the ATA 191 chapter in Cisco ATA 191 Analog Telephone Adapter Administration Guide for Cisco Unified Communications Manager . |
| Step 3 | Upgrade the firmware to the latest Cisco ATA image. For more information, see Configure Firmware Upgrade for ATA in SIP Mode . |
| Step 4 | In Cisco Unified CME, configure analog phones that use a Cisco ATA in the same way as a Cisco Unified IP phone. In the type command that is configured under voice register pool configuration mode, use the ATA-191 keyword. For information on how to provision phones, see Create Directory Numbers for SIP Phones . |

| Step 1 | Copy the firmware files to router flash memory. For example, ATA190.1-1-2-005.loads and ATA190.1-1-2-005.bin.sgn are firmware files for ATA 190. The firmware file for ATA 12.0(1) tat is supported in Unified CME is cmterm-ata191.12-0-1SR1-1.zip. |
|---|---|
| Step 2 | Create TFTP bindings for the firmware files. Router(confg)#tftp-server Flash:ATA190.1-1-2-005.bin.sgn
Router(confg) tftp-server Flash:ATA190.1-1-2-005.loads |
| Step 3 | Specify the load using loads command under voice register global configuration mode. Router(confg)#voice register global
Router(confg-register-global) load ATA-190 ATA190.1-1-2-005 |
| Step 4 | Configure a pool for ATA phone to be upgraded. |
| Step 5 | Create CNF files using create profile CLI command under voice register global configuration mode. |
| Step 6 | Restart the ATA by unplugging and re-plugging or by executing the reset command. Cisco ATA 190/191 takes around 5 mins to upgrade the firmware. Verify the new firmware using show voice register pool phone-load CLI command Router#show voice register pool phone-load
Pool Device Name      Current-Version         Previous-Version
==== ===========      ================        ================
1    SEP34DB²D18001C  Cisco/ATA190-1.1.2(005) Cisco/ATA190-1.1.1(003) |

| Note | If there is only
                                             			 one pickup group, you do not need to enter the group ID after the **4 to pickup
                                             			 a call. |
|---|---|

| Restriction | H.323 trunk
                                                   				  calls are not supported. Hardware
                                                   				  conferencing with DSPFarm resource is not supported on Cisco ATA-187 in Cisco
                                                   				  Unified CME 9.0. With the correct firmware (9.2(3) or a later version), local
                                                   				  three-way conferencing is supported. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register global Example: Router(config)# voice register global | Enters voice
                                             				register global configuration mode. |
| Step 4 | authenticate realm string Example: Router(config-register-global)# authenticate realm xxxxx | realm string —Realm parameter for challenge and response
                                                   					 as specified in RFC 2617 is authenticated. |
| Step 5 | exit Example: Router(config-register-global)# exit | Exits voice
                                             				register global configuration mode. |
| Step 6 | voice service { voip \| voatm } Example: Router(config)# voice service voip | Enters
                                             				voice-service configuration mode to specify a voice encapsulation type. voip —Specifies Voice over IP (VoIP) parameters. voatm —Specifies Voice over ATM (VoATM) parameters. |
| Step 7 | allow-connections from-type to to-type Example: Router(config-voi-serv)# allow-connections sip to sip | Allows
                                             				connections between specific types of endpoints in a VoIP network. from-type —Originating endpoint type. The following
                                                   					 choices are valid: sip —Session Interface Protocol. to —Indicates that the argument that follows is the
                                                   					 connection target. to-type —Terminating endpoint type. The following
                                                   					 choices are valid: sip —Session
                                                         						  Interface Protocol. |
| Step 8 | fax protocol t38 [ ls_redundancy value [ hs_redundancy value ] ] [ fallback { cisco \| none \| pass-through { g711ulaw \| g711alaw } } ] Example: Router(config-voi-serv)# fax protocol t38 ls-redundancy 0 hs-redundancy 0 fallback pass-through g711ulaw | Specifies
                                             				the global default ITU-T T.38 standard fax protocol to be used for all VoIP
                                             				dial peers. ls_redundancy value —(Optional) (T.38 fax relay only) Specifies
                                                   					 the number of redundant T.38 fax packets to be sent for the low-speed
                                                   					 V.21-based T.30 fax machine protocol. Range varies by platform from 0 (no
                                                   					 redundancy) to 5 or 7. Default is 0. hs_redundancy value —(Optional) (T.38 fax relay only) Specifies
                                                   					 the number of redundant T.38 fax packets to be sent for high-speed V.17, V.27,
                                                   					 and V.29 T.4 or T.6 fax machine image data. Range varies by platform from 0 (no
                                                   					 redundancy) to 2 or 3. Default is 0. fallback —(Optional) A fallback mode is used to
                                                   					 transfer a fax across a VoIP network if T.38 fax relay could not be
                                                   					 successfully negotiated at the time of the fax transfer. pass-through —(Optional) The fax stream uses one of
                                                   					 the following high-bandwidth codecs: g711ulaw —Uses the G.711 u-law codec. g711alaw —Uses the G.711 a-law codec. |
| Step 9 | exit Example: Router(config-voi-serv)# exit | Exits
                                             				voice-service configuration mode. |
| Step 10 | voice register pool pool-tag Example: Router(config)# voice register pool  11 | Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a Cisco
                                             				Unified SIP phone in Cisco Unified CME. pool-tag —Unique number assigned to the pool.
                                                   					 Range: 1 to 100. |
| Step 11 | id mac address Example: Router(config-register-pool)# id mac 93FE.12D8.2301 | identifies a
                                             				locally available Cisco Unified SIP IP phone. mac address —Identifies the MAC address of a particular
                                                   					 Cisco Unified SIP IP phone. |
| Step 12 | type phone-type Example: Router(config-register-pool)# type ATA-187 | Defines a
                                             				phone type for the SIP phone being configured. |
| Step 13 | ata-ivr-pwd password Example: Router(config-register-pool)# ata-ivr-pwd 1234 | (Optional)
                                             				Defines a password to access interactive voice response (IVR) and change the
                                             				default phone settings on Cisco Analog Telephone Adaptors. password —Four-digit or five-digit string to be
                                                   					 used as password to access IVR. Password string must contain numbers 0 to 9. |
| Step 14 | session-transport { tcp \| udp } Example: Router(config-register-pool)# session-transport tcp | (Optional)
                                             				Specifies the transport layer protocol that a Cisco Unified SIP IP phone uses
                                             				to connect to Cisco Unified CME. tcp —Transmission Control Protocol (TCP) is used. udp —User
                                                   					 Datagram Protocol (UDP) is used. This is the default. |
| Step 15 | number tag dn dn-tag Example: Router(config-register-pool)# number 1 dn 33 | Indicates
                                             				the E.164 phone numbers that the registrar permits to handle the Register
                                             				message from the Cisco Unified SIP IP phone. tag —Identifies the telephone number when there are
                                                   					 multiple number commands. Range: 1 to 10. dn dn-tag —Identifies the directory number tag for
                                                   					 this phone number as defined by the voice register dn command. Range: 1 to 150. |
| Step 16 | username username [ password password ] Example: Router(config-register-pool)# username ata112 password cisco | Assigns an
                                             				authentication credential to a phone user so that the SIP phone can register in
                                             				Cisco Unified CME. username —Username of the local Cisco IP phone
                                                   					 user. Default: Admin. password —Enables password for the Cisco IP phone
                                                   					 user. password —Password string. |
| Step 17 | codec codec-type [ bytes ] Example: Router(config-register-pool)# codec g711ulaw | Specifies
                                             				the codec to be used when setting up a call for a SIP phone or group of SIP
                                             				phones in Cisco Unified CME. codec-type —Preferred codec; values are as follows: g711alaw —G.711 A law 64K bps. g711ulaw —G.711 micro law 64K bps. g722r64 —G.722-64K at 64K bps. g729r8 —G.729 8K bps (default). ilbc —
                                                         						  internet Low Bitrate Codec (iLBC) at 13,330 bps or 15,200 bps. |
| Step 18 | end Example: Router(config-register-pool)# end | Exits to
                                             				privileged EXEC mode. |

| Restriction | Supported only for the Cisco VG202, VG204, and VG224 voice
                                          		  gateways. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice-gateway system tag Example: Router(config)# voice-gateway system 1 | Enters voice
                                             				gateway configuration mode and creates a voice gateway configuration. |
| Step 4 | mac-address mac-address Example: Router(config-voice-gateway)# mac-address | Defines the
                                             				MAC address of the voice gateway to autoconfigure. |
| Step 5 | type { vg202 \| vg204 \| vg224 } Example: Router(config-voice-gateway)# type vg224 | Defines the
                                             				type of voice gateway to autoconfigure. |
| Step 6 | voice-port port-range Example: Router(config-voice-gateway)# voice-port 0-23 | Identifies the
                                             				ports on the voice gateway that register to Cisco Unified CME. |
| Step 7 | network-locale locale-code Example: Router(config-voice-gateway)# network-locale FR | Selects a
                                             				geographically specific set of tones and cadences for the voice gateway s
                                             				analog endpoints that register to Cisco Unified CME. |
| Step 8 | create cnf-files Example: Router(config-voice-gateway)# create cnf-files | Generates the
                                             				XML configuration files that are required for the voice gateway to
                                             				autoconfigure its analog ports that register to Cisco Unified CME. |
| Step 9 | reset or restart Example: Router(config-voice-gateway)# reset or Router(config-voice-gateway)# restart | (Optional)
                                             				Performs a complete reboot of all analog phones associated with the voice
                                             				gateway and registered to Cisco Unified CME. or (Optional)
                                             				Performs a fast restart of all analog phones associated with the voice gateway
                                             				after simple changes to buttons, lines, or speed-dial numbers. Use
                                                   					 these commands to download new configuration files to the analog phones after
                                                   					 making configuration changes to the phones in Cisco Unified CME. |
| Step 10 | end Example: Router(config-voice-gateway)# end | Exits to
                                             				privileged EXEC mode. |

| Restriction | FXS ports on Cisco VG248 analog phone gateways are not supported
                                          		  by Cisco Unified CME. |
|---|---|

| Step 1 | Set up
                                          			 ephone-dns for up to 24 endpoints on the Cisco IOS gateway. Use the ephone-dn command: Example: ephone-dn 1 dual-line 
			  number 1000 
			 . 
			 . 
			 . 
			 ephone-dn 24 dual-line 
			  number 1024 |
|---|---|
| Step 2 | Set the
                                          			 maximum number of ephones. Use the max ephones command to set a number equal to or greater than the total number of endpoints
                                             				that you intend to register on the Cisco Unified CME router, including both IP
                                             				and analog endpoints. For example, if you have 6 IP phones and 12 analog
                                             				phones, set the max ephones command to 18 or greater. |
| Step 3 | Assign
                                          			 ephone-dns to ephones. Use the auto assign command to enable the automatic assignment of an
                                             				available ephone-dn to each phone as the phone contacts the Cisco Unified CME
                                             				router to register. Note The order
                                                      				of ephone-dn assignment is not guaranteed. For example, if you have analog
                                                      				endpoints on ports 2/0 through 2/23 on the Cisco IOS gateway, port 2/0 does not
                                                      				necessarily become ephone 1. Use one of the following commands to enable
                                                      				automatic ephone-dn assignment. auto assign 1 to 24 —You do not need to use the type keyword
                                                   					 if you have only analog endpoints to be assigned or if you want all endpoints
                                                   					 to be automatically assigned. auto assign 1 to 24 type anl —Use the type keyword
                                                   					 if you have other phone types in the system and you want only the analog
                                                   					 endpoints to be assigned to ephone-dns automatically. An alternative
                                             				to using the auto assign command is to manually assign ephone-dns to ephones (analog phones on FXS
                                             				ports). This method is more complicated, but you might need to use it if you
                                             				want to assign a specific extension number (ephone-dn) to a particular ephone.
                                             				The reason that manual assignment is more complicated is because a unique
                                             				device ID is required for each registering ephone and analog phones do not have
                                             				unique MAC addresses like IP phones do. To create unique device IDs for analog
                                             				phones, the auto assign process uses a particular algorithm. When you make
                                             				manual ephone assignments, you have to use the same algorithm for each phone
                                             				that receives a manual assignment. The algorithm
                                             				uses the single 12-digit SCCP local interface MAC address on the Cisco IOS
                                             				gateway as the base to create unique 12-digit device IDs for all the FXS ports
                                             				on the Cisco IOS gateway. The rightmost 9 digits of the SCCP local interface
                                             				MAC address are shifted left three places and are used as the leftmost 9 digits
                                             				for all 24 individual device IDs. The remaining 3 digits are the hexadecimal
                                             				translation of the binary representation of the port’s slot number (3 digits),
                                             				subunit number (2 digits), and port number (7 digits). The following example
                                             				shows the use of the algorithm to create a unique device ID for one port: The MAC
                                                   					 address for the Cisco VG224 SCCP local interface is 000C.8638.5EA6. The FXS
                                                   					 port has a slot number of 2 (010), a subunit number of 0 (00), and a port
                                                   					 number of 1 (0000001). The binary digits are strung together to become 0100
                                                   					 0000 0001, which is then translated to 401 in hexadecimal to create the final
                                                   					 device ID for the port and ephone. The
                                                   					 resulting unique device ID for this port is C863.85EA.6401. When manually
                                             				setting up an ephone configuration for an analog port, assign it just one
                                             				button because the port represents a single-line device. The button command can use the “:” (colon, for normal), “o” (overlay) and “c”
                                             				(call-waiting overlay) modes. Note Once you
                                                      				have assigned ephone-dns to all the ephones that you want to assign manually,
                                                      				you can use the auto assign command to automatically assign the remaining ports. | Note | The order
                                                      				of ephone-dn assignment is not guaranteed. For example, if you have analog
                                                      				endpoints on ports 2/0 through 2/23 on the Cisco IOS gateway, port 2/0 does not
                                                      				necessarily become ephone 1. Use one of the following commands to enable
                                                      				automatic ephone-dn assignment. | Note | Once you
                                                      				have assigned ephone-dns to all the ephones that you want to assign manually,
                                                      				you can use the auto assign command to automatically assign the remaining ports. |
| Note | The order
                                                      				of ephone-dn assignment is not guaranteed. For example, if you have analog
                                                      				endpoints on ports 2/0 through 2/23 on the Cisco IOS gateway, port 2/0 does not
                                                      				necessarily become ephone 1. Use one of the following commands to enable
                                                      				automatic ephone-dn assignment. |
| Note | Once you
                                                      				have assigned ephone-dns to all the ephones that you want to assign manually,
                                                      				you can use the auto assign command to automatically assign the remaining ports. |
| Step 4 | Set up feature
                                          			 parameters as desired. The following
                                             				list includes commonly configured features. For information about supported
                                             				features, see Supplementary Services
                                                				  Features for FXS Ports on Cisco IOS Voice Gateways Configuration Guide . Call
                                                   					 transfer—To use call transfer from analog endpoints, the transfer-system command must be configured for the full-blind or full-consult keyword in telephony-service configuration mode on the Cisco Unified CME
                                                   					 router. This is the recommended setting for Cisco CME 3.0 and later versions,
                                                   					 but it is not the default. Call
                                                   					 forwarding—Call forwarding destinations are specified for all, busy, and
                                                   					 no-answer conditions for each ephone-dn using the call-forward
                                                         						  all , call-forward
                                                         						  busy , and call-forward
                                                         						  noan commands in ephone-dn configuration mode. Call
                                                   					 park—Call-park slots are created using the park-slot command in ephone-dn configuration mode. Phone users must be instructed how to
                                                   					 transfer calls to the call-park slots and use directed pickup to retrieve the
                                                   					 calls. Call
                                                   					 pickup groups—Extensions are added to pickup groups using the pickup-group command in ephone-dn configuration mode. Phone users must be told which phones
                                                   					 are in which groups. Caller
                                                   					 ID—Caller names are defined using the name command
                                                   					 in ephone-dn configuration mode. Caller numbers are defined using the number command in ephone-dn configuration mode. Speed
                                                   					 dial—Numbers to be speed-dialed are stored with their associated speed-dial
                                                   					 codes using the speed-dial command in ephone configuration mode. Speed
                                                   					 dial to voice mail—The voice-mail number is defined using the voicemail command in telephony-service configuration mode. |
| Step 5 | Set up
                                          			 feature restrictions as desired. Features
                                             				such as transfer, conference, park, pickup, group pickup (gpickup), and call
                                             				forward all (cfwdall) can be restricted from individual ephones using the
                                             				appropriate Cisco Unified CME softkey template command, even though analog
                                             				phones do not have softkeys. Simply create a template that leaves out the
                                             				softkey that represents the feature you want to restrict and apply the template
                                             				to the ephone for which you want the feature restricted. For more information
                                             				about softkey template customization, see Customize Softkeys . |

| Note | The order
                                                      				of ephone-dn assignment is not guaranteed. For example, if you have analog
                                                      				endpoints on ports 2/0 through 2/23 on the Cisco IOS gateway, port 2/0 does not
                                                      				necessarily become ephone 1. Use one of the following commands to enable
                                                      				automatic ephone-dn assignment. |
|---|---|

| Note | Once you
                                                      				have assigned ephone-dns to all the ephones that you want to assign manually,
                                                      				you can use the auto assign command to automatically assign the remaining ports. |
|---|---|

| Restriction | Because
                                                   				  Cisco Unified CME is not designed for centralized call processing, remote
                                                   				  phones are supported only for fixed teleworker applications, such as working
                                                   				  from a home office. Cisco Unified CME does not support CAC for remote SCCP phones,
                                                   				  so voice quality can degrade if a WAN link is oversubscribed. High-bandwidth
                                                   				  data applications used over a WAN can cause degradation of voice quality for
                                                   				  remote IP phones. Cisco Unified CME does not support Emergency 911 (E911) calls
                                                   				  from remote IP phones. Teleworkers using remote phones connected to
                                                   				  Cisco Unified CME over a WAN should be advised not to use these phones for E911
                                                   				  emergency services because the local public safety answering point (PSAP) will
                                                   				  not be able to obtain valid calling-party information from them. We recommend
                                                   				  that you make all remote phone users aware of this issue. One way is to place a
                                                   				  label on all remote teleworker phones that reminds users not to place 911
                                                   				  emergency calls on remote IP phones. Remote workers should place any emergency
                                                   				  calls through locally configured hotel, office, or home phones (normal
                                                   				  land-line phones) whenever possible. Inform remote workers that if they must
                                                   				  use remote IP phones for emergency calls, they should be prepared to provide
                                                   				  specific location information to the answering PSAP personnel, including street
                                                   				  address, city, state, and country. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone phone-tag Example: Router(config)# ephone 36 | Enters ephone
                                             				configuration mode. phone-tag —Unique sequence number that identifies
                                                   					 this ephone during configuration tasks. |
| Step 4 | mtp Example: Router(config-ephone)# mtp | Sends media
                                             				packets to the Cisco Unified CME router. |
| Step 5 | codec { g711ulaw \| g722r64 \| g729r8 [ dspfarm-assist ] } Example: Router(config-ephone)# codec g729r8 dspfarm-assist | (Optional)
                                             				Selects a preferred codec for setting up calls. Default:
                                                   					 G.711 mu-law codec. The g722r64 keyword requires Cisco Unified CME 4.3
                                                   					 and later versions. dspfarm-assist —Attempts to use DSP-farm resources
                                                   					 for transcoding the segment between the phone and the Cisco Unified CME router
                                                   					 if G.711 is negotiated for the call. Note The dspfarm-assist keyword is ignored if the SCCP
                                                         				  endpoint type is ATA, VG224, or VG248. | Note | The dspfarm-assist keyword is ignored if the SCCP
                                                         				  endpoint type is ATA, VG224, or VG248. |
| Note | The dspfarm-assist keyword is ignored if the SCCP
                                                         				  endpoint type is ATA, VG224, or VG248. |
| Step 6 | end Example: Router(config-ephone)# end | Returns to
                                             				privileged EXEC mode. |

| Note | The dspfarm-assist keyword is ignored if the SCCP
                                                         				  endpoint type is ATA, VG224, or VG248. |
|---|---|

| Use the show running-config command or the show telephony-service ephone command to
                                          			 verify parameter settings for remote ephones. |
|---|

| Step 1 | Download Cisco IP Communicator 2.0 or a later version software from the software download site at https://software.cisco.com/download/home/277641082 . |
|---|---|
| Step 2 | Install the
                                          			 software on your PC, then launch the Cisco IP Communicator application. For
                                             				information, see the Installing and Launching Cisco IP Communicator section in
                                             				the appropriate Cisco IP Communicator User
                                                				  Guide . |
| Step 3 | Complete the
                                          			 configuration and registration tasks on the Cisco IP Communicator as required,
                                          			 including the following: Configure
                                                				  the IP address of the Cisco Unified CME TFTP server. Right-click on the Cisco IP Communicator interface, then choose Preferences > Network > Use these TFTP
                                                               								servers . Enter
                                                         						  the IP address of the Cisco Unified CME TFTP server in the field. Disable
                                                				  the Optimize for low bandwidth parameter to ensure that Cisco IP Communicator
                                                				  sends voice packets for all calls. Note The
                                                            					 following steps are required to enable Cisco IP Communicator to support the
                                                            					 G.711 codec, which is the fallback codec for Cisco Unified CME. You can
                                                            					 compensate for disabling the optimization parameter by using the codec command
                                                            					 in ephone configuration mode to configure G.729 or another advanced codec as
                                                            					 the preferred codec for Cisco IP Communicator. This helps to ensure that the
                                                            					 codec for a VoIP (For example, SIP or H.323) dial-peer is supported by Cisco IP
                                                            					 Communicator and can prevent audio problems caused by insufficient bandwidth. Right-click on the Cisco IP Communicator interface and
                                                         						  choose Preferences > Audio . Uncheck the checkbox next to Optimize for low bandwidth. | Note | The
                                                            					 following steps are required to enable Cisco IP Communicator to support the
                                                            					 G.711 codec, which is the fallback codec for Cisco Unified CME. You can
                                                            					 compensate for disabling the optimization parameter by using the codec command
                                                            					 in ephone configuration mode to configure G.729 or another advanced codec as
                                                            					 the preferred codec for Cisco IP Communicator. This helps to ensure that the
                                                            					 codec for a VoIP (For example, SIP or H.323) dial-peer is supported by Cisco IP
                                                            					 Communicator and can prevent audio problems caused by insufficient bandwidth. |
| Note | The
                                                            					 following steps are required to enable Cisco IP Communicator to support the
                                                            					 G.711 codec, which is the fallback codec for Cisco Unified CME. You can
                                                            					 compensate for disabling the optimization parameter by using the codec command
                                                            					 in ephone configuration mode to configure G.729 or another advanced codec as
                                                            					 the preferred codec for Cisco IP Communicator. This helps to ensure that the
                                                            					 codec for a VoIP (For example, SIP or H.323) dial-peer is supported by Cisco IP
                                                            					 Communicator and can prevent audio problems caused by insufficient bandwidth. |
| Step 4 | Wait for the
                                          			 Cisco IP Communicator application to connect and register to Cisco Unified CME. |
| Step 5 | Test Cisco IP
                                          			 Communicator. For more
                                          			 information, see Verify Cisco IP Communicator Support on SCCP Phone . |

| Note | The
                                                            					 following steps are required to enable Cisco IP Communicator to support the
                                                            					 G.711 codec, which is the fallback codec for Cisco Unified CME. You can
                                                            					 compensate for disabling the optimization parameter by using the codec command
                                                            					 in ephone configuration mode to configure G.729 or another advanced codec as
                                                            					 the preferred codec for Cisco IP Communicator. This helps to ensure that the
                                                            					 codec for a VoIP (For example, SIP or H.323) dial-peer is supported by Cisco IP
                                                            					 Communicator and can prevent audio problems caused by insufficient bandwidth. |
|---|---|

| Step 1 | Use the show running-config command to display
                                          			 ephone-dn and ephone information associated with this phone. |
|---|---|
| Step 2 | After Cisco IP Communicator registers with Cisco Unified CME, it
                                          			 displays the phone extensions and softkeys in its configuration. Verify that
                                          			 these are correct. |
| Step 3 | Make a local call from the phone and have someone call you. Verify
                                          			 that you have a two-way voice path. |

| Use the debug ephone detail command to diagnose problems with calls. For more information, see Cisco Unified CME Command Reference . |
|---|

| Restriction | Detection or
                                                   				  conversion between Network Transmission Equipment (NTE) and Session Signaling
                                                   				  Event (SSE) is not supported. Transcoding
                                                   				  or trans-compress rate support for different Voice Band Data (VBD) and Modem
                                                   				  Relay (MR) media type is not supported. IP-STE
                                                   				  supports only single-line calls, dual-line and octo-line calls are not
                                                   				  supported. Speed-dial
                                                   				  can only be configured manually on the IP-STE. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone phone-tag Example: Router(config)# ephone 6 | Enters ephone
                                             				configuration mode. phone-tag —Unique sequence number that identifies
                                                   					 this ephone during configuration tasks. The maximum number of ephones is
                                                   					 version and platform-specific. Type ? to display
                                                   					 range. |
| Step 4 | mac-address [ mac-address ] Example: Router(config-ephone)# mac-address 2946.3f2.311 | Specifies the
                                             				MAC address of the IP phone that is being configured. |
| Step 5 | type ip-ste Example: Router(config-ephone)# type ip-ste | Specifies the
                                             				type of phone. |
| Step 6 | end Example: Router(config-ephone)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone phone-tag Example: Router(config)# ephone 1 | Enters ephone
                                             				configuration mode. |
| Step 4 | mac-address [ mac-address ] Example: Router(config-ephone)# mac-address 0001.2345.6789 | Specifies the
                                             				MAC address of the IP phone that is being configured. |
| Step 5 | type phone-type Example: Router(config-ephone)# type 7926 | Specifies the
                                             				type of phone that is being configured. |
| Step 6 | button button-number Example: Router(config-ephone)# button 1:1 | Creates a set
                                             				of ephone-dns overlaid on a single button. |
| Step 7 | ephone-template template
                                                				  tag Example: Router(config)#ephone-template 5 | Enters
                                             				ephone-template configuration mode to create an ephone template. |
| Step 8 | service [ phone parameter name parameter value ] \| [ xml-config append phone_service xml filename ] Example: Router(config-ephone-template)#service xml-config append flash:7926_phone_services.xml | Sets
                                             				parameters for all IP phones that support the configured functionality and to
                                             				which this template is applied. parameter name —The parameter name is word and
                                                   					 case-sensitive. See Cisco Unified CME Command
                                                      						Reference . phone_service xml filename —Allows the addition of
                                                   					 a phone services xml file. |
| Step 9 | telephony-service Example: Router(config)telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 10 | cnf-file perphone Example: (config-telephony)# cnf-file perphone | Specifies
                                             				that the system generates a separate configuration XML file for each IP phone. Separate
                                                   					 configuration files for each endpoint are required for security. |
| Step 11 | create
                                                				  cnf-files Example: Router(config-telephony)# create cnf-files | Builds XML
                                             				configuration files required for SCCP phones. |
| Step 12 | end Example: Router(config-telephony)#end | Returns to
                                             				privileged EXEC mode. |

| Restriction | The DNs
                                                   				  assigned to auto registered phones cannot be configured as shared line DNs. Only Cisco
                                                   				  Unified 7800 and 8800 series phones are supported with auto registration. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register global Example: Router(config)# voice register global | Enters voice
                                             				register global configuration mode. |
| Step 4 | auto-register Example: Router(config-register-global)# auto-register | Enters auto
                                             				registration mode for SIP phones registering with Unified CME. |
| Step 5 | password string Example: Router(config-voice-auto-register)# password cisco | Configures the
                                             				default password for SIP phones that auto register. string —Configures the mandatory word string that
                                                   					 administrator provides for auto registration of phones on Unified CME. |
| Step 6 | auto-assign First DN number to Last DN number Example: Router(config-voice-auto-register)# auto-assign 1 to 10 | Configures the
                                             				range of directory numbers for phones that auto register on Unified CME. First DN number to Last DN number —Range is 1 to
                                                   					 4294967295. |
| Step 7 | service-enable Example: Router(config-voice-auto-register)# service-enable | Enables the
                                             				auto registration of SIP phones on Unified CME. Once auto-register command is
                                             				entered, the service is enabled by default. To temporarily
                                             				disable auto registration feature without losing DN and password
                                             				configurations, use the no form of this command. |
| Step 8 | template tag Example: Router(config-voice-auto-register)
template 10 | Configures a
                                             				basic configuration template that supports all the configurations available on
                                             				the voice register template. It is
                                                   					 mandatory that voice register template is configured with the same template
                                                   					 tag. tag —Range is 1 to 10. |
| Step 9 | end Example: Router(config-voice-auto-register)# end | Exits to
                                             				privileged EXEC mode. |

| Restriction | Cisco
                                                   				  Unified SCCP trunk-dn is not supported. Mixed shared
                                                   				  lines can only be configured on one of several common directory numbers. Mixed shared
                                                   				  lines are not supported in Cisco Unified SRST. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register dn dn-tag Example: Router(config)# voice register dn 1 | Enters voice
                                             				register dn configuration mode. dn-tag —Unique sequence number that identifies a
                                                   					 particular directory number during configuration tasks. Range is 1 to 150 or
                                                   					 the maximum defined by the max-dn command. |
| Step 4 | number number Example: Router(config-register-dn)# number 1001 | Associates a
                                             				telephone or extension number with a Cisco Unified SIP IP phone in a Cisco
                                             				Unified CME system. number —String of up to 16 characters that
                                                   					 represents an E.164 telephone number. Normally, the string is composed of
                                                   					 digits, but the string may contain alphabetic characters when the number is
                                                   					 dialed only by the router, as with an intercom number. |
| Step 5 | shared-line [ max-calls number-of-calls ] Example: Router(config-register-dn)# shared-line max-calls 4 | Creates a
                                             				directory number to be shared by multiple Cisco Unified SIP IP phones. max-calls number-of-calls —(Optional) Maximum number of
                                                   					 active calls allowed on the shared line. Range: 2 to 16. Default: 2. |
| Step 6 | exit Example: Router(config-register-dn)# exit | Exits voice
                                             				register dn configuration mode. |
| Step 7 | ephone-dn dn-tag [ dual-line \| octo-line ] Example: Router(config)# ephone-dn 1 octo-line | Enters
                                             				ephone-dn configuration mode to configure a directory number for an IP phone
                                             				line. dn-tag —Unique number that identifies an ephone-dn
                                                   					 during configuration tasks. Range is 1 to the number set by the max-dn command. dual-line —(Optional) Enables two calls per
                                                   					 directory number. octo-line —(Optional) Enables eight calls per
                                                   					 directory number. |
| Step 8 | number number Example: Router(config-ephone-dn)# number 1001 | Associates a
                                             				telephone or extension number with this ephone-dn. number —String of up to 16 characters that
                                                   					 represents an E.164 telephone number. Normally, the string is composed of
                                                   					 digits, but the string may contain alphabetic characters when the number is
                                                   					 dialed only by the router, as with an intercom number. |
| Step 9 | shared-line
                                                				  sip Example: Router(config-ephone-dn)# shared-line sip | Adds an
                                             				ephone-dn as a member of a shared directory number in the database of the
                                             				Shared-Line Service Module for a mixed shared line between Cisco Unified SIP
                                             				and Cisco Unified SCCP IP phones. |
| Step 10 | end Example: Router(config-ephone-dn)# end | Exits to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-dn dn-tag [ dual-line \| octo-line ] Example: Router(config)# ephone-dn 6 octo-line | Enters
                                             				ephone-dn configuration mode to configure a directory number for an IP phone
                                             				line. dn-tag —Unique number that identifies an ephone-dn
                                                   					 during configuration tasks. Range is 1 to the number set by the max-dn command. dual-line —(Optional) Enables two calls per
                                                   					 directory number. octo-line —(Optional) Enables eight calls per
                                                   					 directory number. |
| Step 4 | number number Example: Router(config-ephone-dn)# number 1007 | Associates a
                                             				telephone or extension number with an ephone-dn in a Cisco Unified CME. number —String of up to 16 characters that
                                                   					 represents an E.164 telephone number. Normally the string is composed of
                                                   					 digits, but the string may contain alphabetic characters when the number is
                                                   					 dialed only by the router, as with an intercom number. One or more periods (.)
                                                   					 can be used as wildcard characters. |
| Step 5 | exit Example: Router(config-ephone-dn)# exit | Exits
                                             				ephone-dn configuration mode. |
| Step 6 | ephone phone-tag Example: Router(config)# ephone 98 | Enters ephone
                                             				configuration mode. phone-tag —Unique sequence number that identifies
                                                   					 this ephone during configuration tasks. The maximum number of ephones is
                                                   					 version and platform-specific. Type ? to display
                                                   					 range. |
| Step 7 | mac-address mac-address Example: Router(config-ephone)# mac-address ABCD.1234.56EF | Associates the
                                             				MAC address of a Cisco IP phone with an ephone configuration in a Cisco Unified
                                             				CME. mac-address —Identifying MAC address of an IP
                                                   					 phone. |
| Step 8 | type phone-type Example: Router(config-ephone)# type 8941 | Assigns a
                                             				phone type to an SCCP phone. |
| Step 9 | busy-trigger-per-button number-of-calls Example: Router(config-ephone)# busy-trigger-per-button 6 | Sets the
                                             				maximum number of calls allowed on an octo-line directory number before
                                             				activating Call Forward Busy or a busy tone. number-of-calls —Maximum number of calls. Range: 1
                                                   					 to 8. Default: 0 (disabled). |
| Step 10 | max-calls-per-button number-of-calls Example: Router(config-ephone)# max-calls-per-button 4 | Sets the
                                             				maximum number of calls allowed on an octo-line directory number on an SCCP
                                             				phone. number-of-calls —Maximum number of calls. Range: 1
                                                   					 to 8. Default: 8. |
| Step 11 | end Example: Router(config-ephone)# end | Exits
                                             				configuration mode and enters privileged EXEC mode. |

| Restriction | You cannot
                                             			 configure the maximum number of calls per line. The phone controls the maximum
                                             			 number of outgoing calls. Table 1 shows the maximum number of outgoing calls allowed by a phone and the maximum
                                             			 number of incoming calls that can be configured using the busy-trigger-per-button command for Cisco Unified
                                             			 6921, 6941, 6945, 6961, 8941, and 8945 SIP IP Phones in Cisco Unified CME 9.0. Table 6. Maximum
                                                      			 Number of Incoming and Outgoing Calls Cisco
                                                            						Unified SIP IP Phones Maximum
                                                            						Number of Outgoing Calls (Controlled by Phones) Maximum
                                                            						Number of Incoming Calls Before
                                                            						Busy Tone (Configurable) 6921 12 12 6941 24 24 6945 24 24 6961 72 72 8941 24 24 8945 24 24 | Cisco
                                                            						Unified SIP IP Phones | Maximum
                                                            						Number of Outgoing Calls (Controlled by Phones) | Maximum
                                                            						Number of Incoming Calls Before
                                                            						Busy Tone (Configurable) | 6921 | 12 | 12 | 6941 | 24 | 24 | 6945 | 24 | 24 | 6961 | 72 | 72 | 8941 | 24 | 24 | 8945 | 24 | 24 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cisco
                                                            						Unified SIP IP Phones | Maximum
                                                            						Number of Outgoing Calls (Controlled by Phones) | Maximum
                                                            						Number of Incoming Calls Before
                                                            						Busy Tone (Configurable) |
| 6921 | 12 | 12 |
| 6941 | 24 | 24 |
| 6945 | 24 | 24 |
| 6961 | 72 | 72 |
| 8941 | 24 | 24 |
| 8945 | 24 | 24 |

| Cisco
                                                            						Unified SIP IP Phones | Maximum
                                                            						Number of Outgoing Calls (Controlled by Phones) | Maximum
                                                            						Number of Incoming Calls Before
                                                            						Busy Tone (Configurable) |
|---|---|---|
| 6921 | 12 | 12 |
| 6941 | 24 | 24 |
| 6945 | 24 | 24 |
| 6961 | 72 | 72 |
| 8941 | 24 | 24 |
| 8945 | 24 | 24 |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register pool pool-tag Example: Router(config)# voice register pool 20 | Enters voice
                                             				register pool configuration mode and creates a pool configuration for a SIP IP
                                             				phone in Cisco Unified CME. pool-tag —Unique number assigned to the pool. Range
                                             				is 1 to 100. Note For Cisco
                                                         				  Unified CME systems, the upper limit for this argument is defined by the max-pool command. | Note | For Cisco
                                                         				  Unified CME systems, the upper limit for this argument is defined by the max-pool command. |
| Note | For Cisco
                                                         				  Unified CME systems, the upper limit for this argument is defined by the max-pool command. |
| Step 4 | type phone-type Example: Router(config-register-pool)# type 6921 | Defines a
                                             				phone type for a SIP phone. |
| Step 5 | busy-trigger-per-button number Example: Router(config-register-pool)# busy-trigger-per-button 25 | Sets the
                                             				maximum number of calls allowed on a SIP directory number before activating
                                             				Call Forward Busy or a busy tone. number —Maximum number of calls. Range: 1 to the
                                                   					 maximum number of incoming calls listed in Step 6. The default values are 1 for
                                                   					 the Cisco Unified 6921, 6941, 6945, and 6961 SIP IP phones and 2 for the Cisco
                                                   					 Unified 8941 and 8945 SIP IP phones. |
| Step 6 | end Example: Router(config-register-pool)# end | Exits
                                             				configuration mode and enters privileged EXEC mode. |

| Note | For Cisco
                                                         				  Unified CME systems, the upper limit for this argument is defined by the max-pool command. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register pool pool-tag Example: Router(config)# voice register pool 29 | Enters voice
                                             				register pool configuration mode and creates a pool configuration for a Cisco
                                             				Unified SIP IP phone in Cisco Unified CME. pool-tag —Unique number assigned to the pool. Range
                                                   					 is 1 to 100. Note For Cisco
                                                         				  Unified CME systems, the upper limit for this argument is defined by the max-pool command. | Note | For Cisco
                                                         				  Unified CME systems, the upper limit for this argument is defined by the max-pool command. |
| Note | For Cisco
                                                         				  Unified CME systems, the upper limit for this argument is defined by the max-pool command. |
| Step 4 | type phone-type [ addon 1 CKEM \| CP-8800-Audio \| CP-8800-Video [ 2 CKEM \| CP-8800-Audio \| CP-8800-Video [ 3 CKEM \| CP-8800-Audio \| CP-8800-Video ] ] ] Example: Router(config-register-pool)# type 9971 addon 1 CKEM 2 CKEM 3 CKEM
Router(config-register-pool)# type 8851 addon 1 CP-8800-Audio 2 CP-8800-Audio
Router(config-register-pool)# type 8851NR addon 1 CP-8800-Audio 2 CP-8800-Audio
Router(config-register-pool)# type 8861 addon 1 CP-8800-Audio 2 CP-8800-Audio 3 CP-8800-Audio
Router(config-register-pool)# type 8865 addon 1 CP-8800-Video 2 CP-8800-Video 3 CP-8800-Video | Defines a phone type for a Cisco Unified SIP IP phone. The following keywords increase the number of speed-dial, busy-lamp-field, and directory number keys that can be configured: addon 1 CKEM —(Optional) Tells the router that a Cisco SIP IP Phone CKEM 36-Button Line Expansion Module is being added to this Cisco Unified
                                                   SIP IP Phone. Note This option is available to Cisco Unified 8961, 9951, and 9971 SIP IP phones only. addon 1 CP-8800-Audio or addon 1 CP-8800-Video —(Optional) Tells the router that a Cisco SIP IP Phone A-KEM or V-KEM is being added to this Cisco Unified SIP IP Phone. Note The option addon 1 CP-8800-Audio is available to Cisco Unified 8851, 8851NR, and 8861 SIP IP phones only. The option addon
                                                         1 CP-8800-Video is available only to Unified IP Phone 8865. 2 CKEM (Optional)—Tells the router that a second Cisco SIP IP Phone CKEM 36-Button Line Expansion Module is being added to this
                                                   Cisco Unified SIP IP Phone. Note This option is available to Cisco Unified 9951 and 9971 SIP IP phones only. 2 CP-8800-Audio or 2 CP-8800-Video —(Optional) Tells the router that a second Cisco SIP IP Phone A-KEM or V-KEM is being added to this Cisco Unified SIP IP Phone. Note The option 2 CP-8800-Audio is available to Cisco Unified 8851, 8851NR, and 8861 SIP IP phones only. The option 2 CP-8800-Video
                                                         is available only to Unified IP Phone 8865. 3 CKEM —(Optional) Tells the router that a third Cisco SIP IP Phone CKEM 36-Button Line Expansion Module is being added to this Cisco
                                                   Unified SIP IP Phone. Note This option is available to Cisco Unified 9971 SIP IP phones only. 3 CP-8800-Audio or 3 CP-8800-Video —(Optional) Tells the router that a third Cisco SIP IP Phone A-KEM or V-KEM is being added to this Cisco Unified SIP IP Phone. Note The option 3 CP-8800-Audio is available to Cisco Unified 8861 SIP IP phones only. The option 3 CP-8800-Video is available
                                                         only to Unified IP Phone 8865. | Note | This option is available to Cisco Unified 8961, 9951, and 9971 SIP IP phones only. | Note | The option addon 1 CP-8800-Audio is available to Cisco Unified 8851, 8851NR, and 8861 SIP IP phones only. The option addon
                                                         1 CP-8800-Video is available only to Unified IP Phone 8865. | Note | This option is available to Cisco Unified 9951 and 9971 SIP IP phones only. | Note | The option 2 CP-8800-Audio is available to Cisco Unified 8851, 8851NR, and 8861 SIP IP phones only. The option 2 CP-8800-Video
                                                         is available only to Unified IP Phone 8865. | Note | This option is available to Cisco Unified 9971 SIP IP phones only. | Note | The option 3 CP-8800-Audio is available to Cisco Unified 8861 SIP IP phones only. The option 3 CP-8800-Video is available
                                                         only to Unified IP Phone 8865. |
| Note | This option is available to Cisco Unified 8961, 9951, and 9971 SIP IP phones only. |
| Note | The option addon 1 CP-8800-Audio is available to Cisco Unified 8851, 8851NR, and 8861 SIP IP phones only. The option addon
                                                         1 CP-8800-Video is available only to Unified IP Phone 8865. |
| Note | This option is available to Cisco Unified 9951 and 9971 SIP IP phones only. |
| Note | The option 2 CP-8800-Audio is available to Cisco Unified 8851, 8851NR, and 8861 SIP IP phones only. The option 2 CP-8800-Video
                                                         is available only to Unified IP Phone 8865. |
| Note | This option is available to Cisco Unified 9971 SIP IP phones only. |
| Note | The option 3 CP-8800-Audio is available to Cisco Unified 8861 SIP IP phones only. The option 3 CP-8800-Video is available
                                                         only to Unified IP Phone 8865. |

| Note | For Cisco
                                                         				  Unified CME systems, the upper limit for this argument is defined by the max-pool command. |
|---|---|

| Note | This option is available to Cisco Unified 8961, 9951, and 9971 SIP IP phones only. |
|---|---|

| Note | The option addon 1 CP-8800-Audio is available to Cisco Unified 8851, 8851NR, and 8861 SIP IP phones only. The option addon
                                                         1 CP-8800-Video is available only to Unified IP Phone 8865. |
|---|---|

| Note | This option is available to Cisco Unified 9951 and 9971 SIP IP phones only. |
|---|---|

| Note | The option 2 CP-8800-Audio is available to Cisco Unified 8851, 8851NR, and 8861 SIP IP phones only. The option 2 CP-8800-Video
                                                         is available only to Unified IP Phone 8865. |
|---|---|

| Note | This option is available to Cisco Unified 9971 SIP IP phones only. |
|---|---|

| Note | The option 3 CP-8800-Audio is available to Cisco Unified 8861 SIP IP phones only. The option 3 CP-8800-Video is available
                                                         only to Unified IP Phone 8865. |
|---|---|

| Restriction | When a new Cisco
                                             			 Unified SIP IP phone is configured on Cisco Unified CME using the fast-track
                                             			 configuration approach, and the Cisco Unified CME is upgraded to a later
                                             			 version that supports the new phone type, the fast-track configuration
                                             			 pertaining to that SIP IP phone is removed automatically. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables the
                                             				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters the
                                             				global configuration mode. |
| Step 3 | voice register pool-type pool-type Example: Router(config)# voice register pool-type 9900 | Enters the
                                             				voice register pool configuration mode and creates a pool configuration for a
                                             				Cisco Unified SIP IP phone in Cisco Unified CME. If the new
                                             				phone type is an existing phone that is supported on Cisco Unified CME release,
                                             				you get the following error message: ERROR: 8945 is built-in phonemodel, cannot be changed |
| Step 4 | addons max-addons Example: Router(config-register-pooltype)# addons 3 | Defines the
                                             				maximum number of add-on modules supported in Cisco Unified SIP IP phones. max-addons —The maximum allowed value is 3. The
                                                   					 configured add-on modules can be used while defining the pool for the new SIP
                                                   					 phone model using the existing type command as shown below: type <phone-type> [addon 1 module-type [2 module-type]] |
| Step 5 | description string Example: Router(config-register-pooltype)# description TEST PHON | Defines the
                                             				description string for the new phone type. |
| Step 6 | gsm-support Example: Router(config-register-pooltype)# gsm-support | Defines phone
                                             				support for Global System for Mobile Communications (GSM) support. |
| Step 7 | num-lines max-lines Example: Router(config-register-pooltype)# num-lines 12 | Defines the
                                             				maximum number of lines supported by the new phone. max-lines —If this parameter is not configured, the
                                                   					 default value 1 is used. |
| Step 8 | Phoneload-support Example: Router(config-register-pooltype)# Phoneload-support | Defines phone
                                             				support for firmware download from Cisco Unified CME. You can use the load
                                             				command in the voice register global mode to configure the corresponding phone
                                             				load for the new phone type if it supports phone load. |
| Step 9 | reference-pooltype phone-type Example: voice register pool-type 7821? 
			 description Cisco IP Phone 7821 reference-pooltype 6921 | Defines the
                                             				nearest phone family from which the SIP IP phone in fast-track mode will
                                             				inherit the properties. phone-type —Unique number that represents the phone
                                                   					 model. Default There
                                             				is no reference point to inherit the properties. |
| Step 10 | telnet-support Example: Router(config-register-pooltype)# telnet-support | Defines
                                             				phone support for Telnet access. |
| Step 11 | transport { udp \| TCP } Example: Router(config-register-pooltype)# transport TCp | Defines the
                                             				default transport type supported by the new phone. If this
                                             				parameter is not configured, UDP is used as the default value. The session-transport command configured at the voice register
                                             				pool takes priority over this configuration. |
| Step 12 | Xml-config { maxNumCalls \| busyTrigger \| custom } Example: Router(config-register-pooltype)#xml-config busyTrigger 2 
Router(config-register-pooltype)#xml-config maxNumCalls 4
Router(config-register-pooltype)#xml-config custom <test>1</test> | Defines the
                                             				phone-specific XML tags to be used in the configuration file. maxNumCalls —Defines the maximum number of calls allowed
                                                   					 per line. busyTrigger —Defines the number of calls that triggers
                                                   					 Call Forward Busy per line on the SIP phone. custom —Defines custom XML tags which can be appended at
                                                   					 the end of the phone specific CNF file. These
                                             				parameters are used while generating the configuration profile file. CUCME does
                                             				not use these configuration values for any other purpose. |
| Step 13 | exit Example: Router(config-register-pooltype)# exit | Exits the
                                             				voice register-pooltype configuration mode. |
| Step 14 | end Example: Router(config)# end | Exits the
                                             				privileged EXEC configuration mode. |

| Command | Purpose |
|---|---|
| Router# show call-manager-fallback all | Displays
                                             					 the detailed configuration of all the Cisco Unified IP phones, voice ports, and
                                             					 dial peers of the Cisco Unified CME Router. |
| Router# show call-manager-fallback dial-peer | Displays
                                             					 the output of the dial peers of the Cisco Unified CME Router. |
| Router# show call-manager-fallback ephone-dn | Displays
                                             					 Cisco Unified IP Phone destination numbers when in call manager fallback mode. |
| Router# show call-manager-fallback voice-port | Displays
                                             					 output for the voice ports. |
| Router# show dial-peer voice summary | Displays a
                                             					 summary of all voice dial peers. |
| Router# show ephone phone | Displays
                                             					 Cisco Unified IP Phone status. |
| Router# show ephone offhook | Displays
                                             					 Cisco Unified IP Phone status for all phones that are off hook. |
| Router# show ephone registered | Displays
                                             					 Cisco Unified IP Phone status for all phones that are currently registered. |
| Router# show ephone remote | Displays
                                             					 Cisco Unified IP Phone status for all nonlocal phones (phones that have no
                                             					 Address Resolution Protocol [ARP] entry). |
| Router# show ephone ringing | Displays
                                             					 Cisco Unified IP Phone status for all phones that are ringing. |
| Router# show ephone summary | Displays a
                                             					 summary of all Cisco Unified IP Phones. |
| Router# show ephone summary brief | Displays a
                                             					 brief summary of all Cisco Unified SCCP phones. |
| Router# show ephone summary types | Displays a
                                             					 summary of all types of Cisco Unified SCCP phones. |
| Router# show ephone registered summary | Displays a
                                             					 summary of all registered Cisco Unified SCCP phones. |
| Router# show ephone unregistered summary | Displays a
                                             					 summary of all unregistered Cisco Unified SCCP phones. |
| Router# show ephone telephone-number phone-number | Displays
                                             					 Unified IP Phone status for a specific phone number. |
| Router# show ephone unregistered | Displays
                                             					 Unified IP Phone status for all unregistered phones. |
| Router# show ephone-dn tag | Displays
                                             					 Unified IP Phone destination numbers. |
| Router# show ephone-dn summary | Displays
                                             					 a summary of all Cisco Unified IP Phone destination numbers. |
| Router# show ephone-dn loopback | Displays
                                             					 Cisco Unified IP Phone destination numbers in loopback mode. |
| Router# show running-config | Displays
                                             					 the configuration. |
| Router # show sip-ua status registrar | Display
                                             					 SIP registrar clients. |
| Router# show voice port summary | Displays
                                             					 a summary of all voice ports. |
| Router # show voice register all | Displays
                                             					 all SIP SRST configurations , SIP phone registrations and dial peer info. |
| Router # show voice register global | Displays
                                             					 voice register global config. |
| Router # show voice register pool all | Displays
                                             					 all config SIP phone voice register pool detail info. |
| Router # show voice register pool type summary | Displays
                                             					 a summary of all registered and unregistered Cisco SIP Phones. |
| Router # show voice register pool <tag> | Displays
                                             					 specific SIP phone voice register pool detail info. |
| Router # show voice register dial-peers | Displays
                                             					 SIP-CME created dial peer. |
| Router # show voice register dn all | Displays
                                             					 all config voice register dn detail info. |
| Router # show voice register dn <tag> | Displays
                                             					 specific voice register dn detail info. |

| Caution | The Interactive
                                       		  Voice Response (IVR) media prompts feature is only available on the IAD2435
                                       		  when running IOS version 15.0(1)M or later. |
|---|---|

| Feature
                                          					 Name | Cisco Unified CME Versions | Feature
                                          					 Information |
|---|---|---|
| Cisco ATA 191 | 12.5 | Introduces native support for Cisco ATA 191 with Unified CME. |
| Enhanced Line Mode | 12.3 | Support introduced for Enhanced Line Mode (ELM) on Cisco IP Phone 8800 Series. |
| Shared
                                          					 Lines with Voice Class Codec Support | 12.2 | Adds
                                          					 support for shared lines with voice class codec on Unified CME. |
| KEM Support for Cisco 8000 Series SIP IP Phones | 12.5 | Supports A-KEM and V-KEM for Cisco IP Phones 8851, 8851NR, 8861, and 8865 Cisco SIP IP Phones. |
| KEM
                                          					 Support for Cisco Unified 8961, 9951, and 9971 SIP IP Phones | 9.1 | Increases
                                          					 line key and feature key appearances, speed dials, or programmable buttons on
                                          					 Cisco Unified SIP IP phones. |
| Cisco
                                          					 ATA-187 | 9.0 | Supports
                                          					 T.38 fax relay and fax pass-through on Cisco ATA-187. |
| Cisco
                                          					 Unified SIP IP Phones |  | Adds SIP
                                          					 support for the following phone types: Cisco
                                                						  Unified 6901 and 6911 IP Phones Cisco
                                                						  Unified 6921, 6941, 6945, and 6961 IP Phones Cisco
                                                						  Unified 8941 and 8945 IP Phones |
| Mixed
                                          					 Shared Lines |  | Allows
                                          					 Cisco Unified SIP and SCCP IP phones to share a common directory number. |
| Multiple
                                          					 Calls Per Line |  | Overcomes
                                          					 the limitation on the maximum number of calls per line. |
| Real-Time
                                          					 Transport Protocol Call Information Display Enhancement | 8.8 | Allows you
                                          					 to display information on active RTP calls using the show ephone rtp connections command. The output from this command provides
                                          					 an overview of all the connections in the system, narrowing the criteria for
                                          					 debugging pulse code modulation and Cisco Unified CME packets without a
                                          					 sniffer. |
| Support
                                          					 for Cisco Unified 3905 SIP IP Phones |  | Adds
                                          					 support for SIP phones connected to a Cisco Unified CME system. |
| Support
                                          					 for Cisco Unified 6945, 8941, and 8945 SCCP IP Phones |  | Adds
                                          					 support for SCCP phones connected to a Cisco Unified CME system. |
| Support
                                          					 for 7926G Wireless SCCP IP Phone | 8.6 | Added
                                          					 support for 7926G Wireless SCCP IP Phone. |
| Secure IP
                                          					 Phones | 8.0 | Adds
                                          					 support for Secure IP Phone (IP-STE). |
| SIP Shared
                                          					 Lines | 7.1 | Adds
                                          					 support for nonexclusive shared lines on SIP phones. |
| Autoconfiguration for Cisco VG202, VG204, and VG224 |  | Adds
                                          					 autoconfiguration for the Cisco VG202, VG204, and VG224 Analog Phone Gateway. |
| Ephone-Type Templates | 7.0/4.3 | Adds
                                          					 support for dynamically adding new phone types without upgrading
                                          					 Cisco IOS software. |
| Octo-Line Directory Numbers |  | Adds
                                          					 octo-line directory numbers that support up to eight active calls. |
| G.722
                                          					 and iLBC Transcoding and Conferencing Support in Cisco Unified CME |  | Adds
                                          					 support for the G.722-64K and iLBC codecs. |
| Dial
                                          					 Plans for SIP Phones | 4.1 | Adds
                                          					 support for dial plans for SIP phones. |
| KPML |  | Adds
                                          					 support for KPML for SIP phones. |
| Session
                                          					 Transport Protocol |  | Adds
                                          					 selection for session-transport protocol for SIP phones. |
| Watch
                                          					 Mode |  | Provides
                                          					 Busy Lamp Field (BLF) notification on a line button that is configured for
                                          					 watch mode on one phone for all lines on another phone (watched phone) for
                                          					 which the watched directory number is the primary line. |
| Remote
                                          					 Teleworker Phones | 4.0 | Introduces support for teleworker remote phones. |
| Analog
                                          					 Phones | 4.0 | Introduces support for analog phones with SCCP supplementary
                                          					 features using FXS ports on Cisco Integrated Services Routers. |
|  | 3.2.1 | Introduces support for analog phones with SCCP supplementary
                                          					 features using FXS ports on a Cisco VG224 voice gateway. |
|  | 3.0 | Introduces support for Cisco ATA 186 and Cisco ATA 188. |
|  | 1.0 | Introduces support for analog phones in H.323 mode using FXS
                                          					 ports. |
| Cisco IP
                                          					 Communicator | 4.0 | Introduces support for Cisco IP Communicator. |
| Direct
                                          					 FXO Trunk Lines | 4.0 | Adds
                                          					 enhancements to improve the keyswitch emulation behavior of PSTN lines in a
                                          					 Cisco Unified CME system, including the following: Status monitoring of the FXO port on the line button of an IP
                                                						  phone. Transfer recall if a transfer-to phone does not answer after a
                                                						  specified timeout. Transfer-to button optimization to free up the private extension
                                                						  line on the transfer-to phone Directory numbers for FXO lines can be configured for dual-line
                                                						  to support the FXO monitoring, transfer recall, and transfer-to button
                                                						  optimization features. |
|  | 3.2 | Introduces direct FXO trunk line capability. |
| SIP
                                          					 Phones | 3.4 | Adds
                                          					 support for SIP phones connected to Cisco CME system. |
| Monitor
                                          					 Mode for Shared Lines | 3.0 | Provides
                                          					 a visible line status indicating whether the line is in-use or not. |