---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmesoft-html-d668e08985
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmesoft.html
retrieved_at: 2026-08-21T07:24:11.565420+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Customize
	 Softkeys

## Chapter: Customize
	 Softkeys

# Customize
                     	 Softkeys

## Information About Softkeys

### Softkeys on IP
                           	 Phones

You can customize
                              		the display and order of softkeys that appear during various call states on
                              		individual IP phones. Softkeys that are appropriate in each call state are
                              		displayed by default. Using phone templates, you can delete softkeys that would
                              		normally appear or change the order in which the softkeys appear. For example,
                              		you might want to display the CFwdAll and Confrn softkeys on a manager's phone and remove
                              		these softkeys from a receptionist's phone.

You can modify
                              		softkeys for the following call states:

- Alerting—When the remote
                                 		  point is being notified of an incoming call and the status of the remote point
                                 		  is being relayed to the caller as either ringback or busy.

- Connected—When the
                                 		  connection to a remote point is established.

- Hold—When a connected party
                                 		  is still connected but there is temporarily no voice connection.

- Idle—Before a call is made
                                 		  and after a call is completed.

- Seized—When a caller is
                                 		  attempting a call but has not yet been connected.

- Remote-in-Use—When another
                                 		  phone is connected to a call on an octo-line directory number shared by this
                                 		  phone (Cisco Unified CME 4.3 or a later version).

- Ringing—After a call is
                                 		  received and before the call is connected (Cisco Unified CME 4.2 or a later
                                 		  version).

Not all softkeys are
                              		available in all call states. Use the CLI help to see the available softkeys
                              		for each call state. The softkeys are as follows:

- Acct—Short for “account
                                 		  code.” Provides access to configured accounts.

- Answer—Picks up incoming
                                 		  call.

- Barge—Allows a user to
                                 		  join (barge) a call on a SIP shared line (Cisco Unified CME 7.1 or a later
                                 		  version).

- Callback—Requests callback
                                 		  notification when a busy called line becomes free.

- CBarge—Barges (joins) a
                                 		  call on a shared octo-line directory number (Cisco Unified CME 4.3 or a later
                                 		  version).

- CFwdALL—Short for “call
                                 		  forward all.” Forwards all calls.

- ConfList—Lists all parties
                                 		  in a conference (Cisco Unified CME 4.1 or a later version). Press Update softkey to update the list of parties in the
                                 		  conference, for instance, to verify that a party has been removed from the
                                 		  conference. Press Remove softkey to remove the appropriate parties.

- Confrn—Short for
                                 		  “conference.” Connects callers to a conference call.

Details—Lists
                                    			 all the participants in a conference. This softkey is supported only on Cisco
                                    			 7800 Series IP Phones. Press Update to update the list of parties in the
                                    			 conference. Press Remove softkey to remove the appropriate parties.
                                    			 The suboption Remove is available to the conference creator and
                                    			 phones that have conference admin configured.

- DND—Short for “do not
                                 		  disturb.” Enables the do-not-disturb features.

- EndCall—Ends the current
                                 		  call.

- GPickUp—Short for “group
                                 		  call pickup.” Selectively picks up calls coming into a phone number that is a
                                 		  member of a pickup group.

- Flash—Short for
                                 		  “hookflash.” Provides hookflash functionality for public switched telephone
                                 		  network (PSTN) services on calls connected to the PSTN via a foreign exchange
                                 		  office (FXO) port.

- HLog—Places the phone of
                                 		  an ephone-hunt group agent into the not-ready status or, if the phone is in the
                                 		  not-ready status, places the phone into the ready status.

- Hold—Places an active call
                                 		  on hold and resumes the call.

- iDivert—Immediately
                                 		  diverts a call to a voice messaging system (Cisco Unified CME 8.5 or a later
                                 		  version)

- Join—Joins an established
                                 		  call to a conference (Cisco Unified CME 4.1 or a later version).

- LiveRcd—Starts the
                                 		  recording of a call (Cisco Unified CME 4.3 or a later version).

- Login—Provides personal
                                 		  identification number (PIN) access to restricted phone features.

- MeetMe—Initiates a meet-me
                                 		  conference (Cisco Unified CME 4.1 or a later version).

- Mobility—Forwards a call
                                 		  to the PSTN number defined by the Single Number Reach (SNR) feature
                                 		  (Cisco Unified CME 7.1 or a later version).

- NewCall—Opens a line on a
                                 		  speakerphone to place a new call.

- Park—Places an active call
                                 		  on hold so it can be retrieved from another phone in the system.

- PickUp—Selectively picks
                                 		  up calls coming into another extension.

- Redial—Redials the last
                                 		  number dialed.

- Resume—Connects to the
                                 		  call on hold.

- RmLstC—Removes the last
                                 		  party added to a conference. This softkey only works for the conference creator
                                 		  (Cisco Unified CME 4.1 or a later version).

- Select—Selects a call or a
                                 		  conference on which to take action (Cisco Unified CME 4.1 or a later version).

Show
                                    			 detail—Lists all the participants in a conference. This softkey is supported
                                    			 only on Cisco 8800 Series IP Phones. Press Update to update the list of parties in the
                                    			 conference. Press Remove softkey to remove the appropriate parties.
                                    			 The suboption Remove is available to the conference creator and
                                    			 phones that have conference admin configured.

- Trnsfer—Short for “call
                                 		  transfer.” Transfers an active call to another extension.

- TrnsfVM—Transfers a call
                                 		  to a voice-mail extension number (Cisco Unified CME 4.3 or a later version).

You change the
                              		softkey order by defining a phone template and applying the template to one or
                              		more phones. You can create up to 20 phone templates for SCCP phones and 10
                              		templates for SIP phones. Only one template can be applied to a phone. If you
                              		apply a second phone template to a phone that already has a template applied to
                              		it, the second template overwrites the first phone template information. The
                              		new information takes effect only after you generate a new configuration file
                              		and restart the phone; otherwise, the previously configured template remains in
                              		effect.

In Cisco Unified CME
                              		4.1, customizing the softkey display for IP phones running SIP is supported
                              		only for the Cisco Unified IP Phones 7911G, 7941G, 7941GE, 7961G, 7961GE,
                              		7970G, and 7971GE.

For configuration
                              		information, see Customize Softkeys .

#### Softkeys Introduced in Unified CME Release 12.3 and Later Releases

From Unified CME Release 12.3, support is introduced for Cisco IP Conference Phone 7832 and Cisco IP Conference Phone 8832.
                                 The following Softkeys are available on Cisco IP Conference Phone 7832 and Cisco IP Conference Phone 8832:

Recents – Displays the call history.

Contacts – Displays the directory list.

Apps – Displays the service options (My Phone Apps, Extension Mobility).

Favorites – Displays the configured speed dials.

Messages – Provides voicemail accessibility.

Settings – Displays the phone settings options.

The softkeys that are introduced in Unified CME Release 12.3 supports the following templates:

Personal user softkey template

Public user softkey template

The personal template supports all the softkeys necessary to provide full functionality of the phone. The public template
                                 supports a restricted softkey set, which is defined for basic conference room use cases. The personal softkey template is
                                 enabled by configuring the CLI command softkeys personal-conf-user under voice register template configuration mode. You can use the no form of the CLI command softkeys personal-conf-user to switch to the default configuration of public user softkey template. In a scenario where no configuration is provided,
                                 the default configuration of public user softkey template is applied. The softkeys that are introduced in Unified CME Release
                                 12.3 are supported only on Cisco IP Conference Phones 7832 and 8832. Hence, softkeys personal-conf-user is an optional configuration that is required only when the phone template has to be applied to Cisco IP Conference Phones
                                 7832 or 8832. For more information on configuring softkeys for SIP phones, see Modify Softkey Display on SIP Phone .

A personal user softkey template supports the following softkeys, apart from the softkeys supported on a public softkey user
                                 template:

Messages

CfwdAll

DND

Redial

```
voice register template 7
 softkeys personal-conf-user
```

For Unified CME Release 12.7 and later releases, Cisco IP Conference Phone 7832 and Cisco IP Conference Phone 8832 introduces
                                 support for:

Custom softkey template

Custom softkey template is already supported on other SIP phones on Unified CME. Before Unified CME Release 12.7, the support
                                 on Cisco IP Conference Phone 7832 and Cisco IP Conference Phone 8832 was limited to personal user softkey template and public
                                 user softkey template. To enable custom softkey template, configure softkeys command under voice register template configuration mode.

```
voice register template 7
 softkeys hold {[Newcall] {Resume]}
```

For more information on configuration of softkeys, see Modify Softkey Display on SIP Phone .

If you configure softkeys personal-conf-user command under voice register template , personal user softkey template is enabled. If you do not configure any of the softkeys command under voice register template configuration mode, the default public user softkey template is enabled.

### Account Code Entry

The Cisco Unified IP Phones 7940 and 7940G and the Cisco Unified IP
                              		Phones 7960 and 7960G allow phone users to enter account codes during call
                              		setup or when connected to an active call using the Acct softkey. Account codes are inserted into call
                              		detail records (CDRs) on the Cisco Unified CME router for later interpretation
                              		by billing software.

An account code is visible in the output of the show call active command and the show call history command for telephony call
                              		legs and is supported by the CISCO-VOICE-DIAL-CONTROL-MIB. The account code
                              		also appears in the “account-code” RADIUS vendor-specific attribute (VSA) for
                              		voice authentication, authorization, and accounting (AAA).

To enter an account code during call setup or when in a connected state,
                              		press the Acct softkey, enter the account code using the
                              		phone keypad, then press the # key to notify Cisco Unified CME that the last
                              		digit of the code has been entered. The account code digits are processed upon
                              		receipt of the # and appear in the show output after processing.

No configuration is required for this feature.

### Hookflash
                           	 Softkey

The Flash softkey
                              		provides hookflash functionality for calls made on IP phones that use FXO lines
                              		attached to the Cisco Unified CME system. Certain PSTN services, such as
                              		three-way calling and call waiting, require hookflash intervention from a phone
                              		user.

When a Flash softkey
                              		is enabled on an IP phone, it can provide hookflash functionality during all
                              		calls except for local IP-phone-to-IP-phone calls. Hookflash-controlled
                              		services can be activated only if they are supported by the PSTN connection
                              		that is involved in the call. The availability of the Flash softkey does not
                              		guarantee that hookflash-based services are accessible to the phone user.

For configuration
                              		information, see Enable Flash Softkey .

### Feature
                           	 Blocking

In Cisco Unified CME
                              		4.0 and later versions, individual softkey features can be blocked on one or
                              		more phones. You specify the features that you want blocked by adding the features
                                    			 blocked command to an ephone template. The template is then
                              		applied under ephone configuration mode to one or more ephones.

If a feature is
                              		blocked using the features
                                    			 blocked command, the softkey is not removed but it does not
                              		function. For configuration information, see Configure Feature Blocking .

To remove a softkey
                              		display, use the appropriate no softkeys command. See Modify Softkey Display on SCCP Phone .

### Feature Policy
                           	 Softkey Control

Cisco Unified CME
                              		8.5 allows you to control the display of softkeys on the Cisco Unified SIP IP
                              		Phones 8961, 9951, and 9971 using the Feature Policy template. The Feature
                              		Policy template allows you to enable and disable a list of feature softkeys on
                              		Cisco Unified SIP IP Phones 8961, 9951, and 9971. Table 1 lists the controllable feature softkeys
                              		with specific feature IDs and their default state on Cisco Unified SIP IP
                              		Phones 8961, 9951, and 9971.

Feature ID

Feature Name

Description

Default
                                          				  State on CME

1

ForwardAll

Forward all
                                          				  calls

Enabled

2

Park

Parks a call

Enabled

3

iDivert

Divert to
                                          				  Voicemail

Enabled

4

ConfList

Conference
                                          				  List

Disabled

5

SpeedDial

Abbreviated
                                          				  Dial

Disabled

6

Callback

Call back

Disabled

7

Redial

Redial a
                                          				  call

Enabled

8

Barge

Barge into a
                                          				  call

Enabled

Cisco Unified CME
                              		uses the existing softkey command under voice register template configuration mode to control the
                              		controllable feature softkeys on phones. Cisco Unified CME generates a featurePolicy<x>.xml file for each voice
                                 		  register template <x> configured. The list of controllable
                              		softkey configurations are specified in the featurePolicy<x>.xml file. Phones need to
                              		reboot or reset to download the Feature Policy template file. For Cisco IP
                              		phones that do not have a Feature Policy template assigned to them, you can use
                              		the default Feature Policy template file ( featurePolicyDefault.xml file).

### Immediate Divert
                           	 for SIP IP Phones

The immediate divert
                              		(iDivert) feature allows you to immediately divert a call to a voice messaging
                              		system. You can divert a call by pressing the iDivert softkey on Cisco Unified SIP IP phones with
                              		voice messaging systems (Cisco Unity Express or Cisco Unity), such as 7940,
                              		7040G, 7960 G, 7945, 7965, 7975, 8961, 9951, and 9971. When the call is
                              		diverted, the line becomes available to place or receive new calls.

The call that is
                              		diverted using the iDivert feature can be in ringing, active, or hold state.
                              		When the call diversion is successful, the caller receives greetings from the
                              		voice messaging system.

Callers can only
                              		divert the calls to their own voice mailbox. But calls on the receiver side can
                              		be diverted either to the voice mailbox of the caller who invoked the iDivert
                              		feature (last redirected party) or to the voice mailbox of the original called
                              		party.

The iDivert softkey
                              		is added to the phones when they register with Cisco Unified CME using softkeyxxxx.xml file. Cisco Unified CME generates the softkeyxxxx.xml file when the create
                                    			 profile command is executed in voice register global
                              		configuration mode. You can disable or change the position of the iDivert
                              		softkey on the phone’s display using the softkey command. For more information, see Configure Immediate Divert (iDivert) Softkey on SIP Phone .

### Enhanced Immediate Divert (Enhanced iDivert)

The Enhanced iDivert feature is an enhanced version of the iDivert feature supported on Unified CME.

Enhanced iDivert is supported in Unified CME 8.5 and later releases. The support for Enhanced iDivert is across both SIP and
                              SCCP phones. iDivert is supported as a softkey on Cisco Unified IP Phones. The feature is enabled by default on Unified CME,
                              by using the iDivert softkey.

While iDivert immediately diverts a call to a voice messaging system, Enhanced iDivert feature allows you to immediately divert
                              a call to the voice messaging system of the phone you dialed or to the voice messaging system of the phone to which call forward
                              is set.

Consider a scenario with a voice message from Phone A to Phone B registered with Unified CME. Call forward is set from Phone
                              B to Phone C, which is also registered to Unified CME. Both Phone B and C support voice messaging. When the voice message
                              is delivered to the voice messaging server of Unified CME, Phone B forwards the message as it has call-forward mailbox configured. If Phone C presses the iDivert softkey, then Phone A gets an audio prompt. Using the Enhanced iDivert feature, the user at Phone A can decide if the voice
                              message needs to be delivered to Phone A or Phone B.

### Programmable Line
                           	 Keys ( PLK)

The Programmable
                              		Line Key (PLK) feature allows you to program feature buttons or services URL
                              		buttons on line key buttons. You can configure line keys with line buttons,
                              		speed dials, BLF speed dials, feature buttons, and URL buttons.

You can program a
                              		line key to function as a services URL button on your Cisco Unified phone using
                              		the url-button command (see Configure Service URL Line Key Button on SCCP Phone and Configure Service URL Line Key Button on SIP Phone ). Similarly, you can program a line key on your Cisco IP phone to function as
                              		a feature button using the feature-button command (see Configure Feature Buttons on SCCP Phone Line Key and Configure Feature Buttons on SIP Phone Line Key for more information).

You can also program
                              		line keys to function as feature buttons using the user-profile in phones that
                              		have Extension Mobility (EM) enabled on them. For configuring line keys to
                              		function as feature buttons on EM phones, see Cisco Unified IP Phone
                                 		  documentation .

Table 1 lists the softkeys supported as PLKs on various Cisco Unified IP Phone models.

Softkeys
                                             				  Supported as Programmable Line Keys (PLK)

7914, 7915,
                                             				  7916 SCCP Phones

7931 Phone

6900 Series
                                             				  SCCP Phones

7942, 7962,
                                             				  7965, 7975 SIP Phones

8961, 9951,
                                             				  and 9971 SIP Phones

Acct

Supported

Supported

Supported

Not
                                             				  Supported

Not
                                             				  Supported

Call Back

Supported

Supported

Supported

Not
                                             				  Supported

Not
                                             				  Supported

Conference

Supported

Supported

Not
                                             				  Supported 1

Supported

Not
                                             				  Supported

Conference
                                             				  List

Supported

Supported

Supported

Not
                                             				  Supported

Not
                                             				  Supported

Customized
                                             				  URL

Supported

Supported

Supported

Supported

Not
                                             				  Supported

Do Not
                                             				  Disturb

Supported

Supported

Supported

Supported

Supported

End Call

Supported

Supported

Supported

Supported

Not
                                             				  Supported

Extension
                                             				  Mobility

Supported

Supported

Supported

Not
                                             				  Supported

Not
                                             				  Supported

Forward
                                             				  All

Supported

Supported

Supported

Supported

Not
                                             				  Supported

GPickUp

Supported

Supported

Supported

Supported

Supported

Hold

Supported

Not
                                             				  Supported 1

Not
                                             				  Supported 1

Supported

Not
                                             				  Supported

Hook Flash

Supported

Supported

Supported

Not
                                             				  Supported

Not
                                             				  Supported

Hunt Group

Supported

Supported

Supported

Not
                                             				  Supported

Not
                                             				  Supported

Live
                                             				  Record

Supported

Supported

Supported

Not
                                             				  Supported

Not
                                             				  Supported

Login

Supported

Supported

Supported

Not
                                             				  Supported

Not
                                             				  Supported

Meet Me

Supported

Supported

Supported

Not
                                             				  Supported

Not
                                             				  Supported

Mobility

Supported

Supported

Supported

Not
                                             				  Supported

Not
                                             				  Supported

MyPhoneApps

Supported

Supported

Supported

Not
                                             				  Supported

Not
                                             				  Supported

New Call

Supported

Supported

Supported

Supported

Not
                                             				  Supported

Night
                                             				  Service

Supported

Supported

Supported

Not
                                             				  Supported

Not
                                             				  Supported

Park

Supported

Supported

Supported

Supported

Supported

Personal
                                             				  Speed Dial

Not
                                             				  Supported

Not
                                             				  Supported

Not
                                             				  Supported

Not
                                             				  Supported

Not
                                             				  Supported

PickUp

Supported

Supported

Supported

Supported

Supported

Privacy

Supported

Supported

Supported

Supported

Supported

Redial

Supported

Not
                                             				  Supported 1

Supported

Supported

Supported

Remove
                                             				  Last Participant

Supported

Supported

Supported

Not
                                             				  Supported

Not
                                             				  Supported

Reset
                                             				  Phone

Not
                                             				  Supported

Not
                                             				  Supported

Not
                                             				  Supported

Not
                                             				  Supported

Not
                                             				  Supported

Services
                                             				  URL

Not
                                             				  Supported 1

Not
                                             				  Supported 2

Not
                                             				  Supported 3

Not
                                             				  Supported

Not
                                             				  Supported

Speed Dial
                                             				  Buttons

Not
                                             				  Supported

Not
                                             				  Supported

Not
                                             				  Supported

Not
                                             				  Supported

Not
                                             				  Supported

Single
                                             				  Number Reach

Supported

Supported

Supported

Not
                                             				  Supported

Not
                                             				  Supported

Transfer

Supported

Not
                                             				  Supported 1

Not
                                             				  Supported 1

Supported

Not
                                             				  Supported

Transfer
                                             				  to VM

Supported

Supported

Supported

Not
                                             				  Supported

Not
                                             				  Supported

Table 2 lists the PLK features available on the Cisco Unified 6945, 8941, and 8945 SCCP
                              		IP Phones in Cisco Unified CME 8.8.

Softkeys
                                             				  Supported as Programmable Line Keys

Cisco
                                             				  Unified 6945, 8941, and 8945 SCCP IP Phones

Acct

Supported

Call Back

Supported

Cancel
                                             				  Call Waiting

Supported

Conference
                                             				  List

Supported

Customized
                                             				  URL

Supported

Do Not
                                             				  Disturb

Supported

End Call

Supported

Extension
                                             				  Mobility

Supported

Forward
                                             				  All

Supported

Group
                                             				  Pickup

Supported

Hook Flash

Supported

Hunt Group
                                             				  Login (HLog)

Supported

Live
                                             				  Record

Supported

Login

Supported

Meet Me

Supported

Mobility

Supported

My Phone
                                             				  Apps

Supported

New Call

Supported

Night
                                             				  Service

Supported

Park

Supported

Personal
                                             				  Speed Dial

Not
                                             				  Supported

Pickup

Supported

Privacy

Supported

Redial

Supported

Remove
                                             				  Last Participant

Supported

Reset
                                             				  Phone

Not
                                             				  Supported

Services
                                             				  URL

Not
                                             				  Supported

Speed Dial
                                             				  Buttons

Supported

Single
                                             				  Number Reach

Supported

Transfer
                                             				  to VM

Supported

Table 3 lists the PLK features available on the Cisco Unified 6911, 6921, 6941, 6945,
                              		6961, 8941, and 8945 SIP IP Phones in Cisco Unified CME 9.0.

Softkeys
                                             				  Supported as Programmable Line Keys

Cisco
                                             				  Unified 6911 SIP IP Phones

Cisco
                                             				  Unified 6921, 6941, 6945, and 6961 SIP IP Phones

Cisco
                                             				  Unified 8941 and 8945 SIP IP Phone

Acct

Not
                                             				  Supported

Not
                                             				  Supported

Not
                                             				  Supported

Call Back

Not
                                             				  Supported

Not
                                             				  Supported

Not
                                             				  Supported

Conference

Not
                                             				  Supported

Not
                                             				  Applicable 4

Not
                                             				  Applicable 1

Conference
                                             				  List

Not
                                             				  Supported

Supported

Supported

Customized
                                             				  URL

Not
                                             				  Supported

Supported

Not
                                             				  Supported

Do Not
                                             				  Disturb

Not
                                             				  Supported

Supported

Supported

End Call

Not
                                             				  Supported

Supported

Supported

Extension
                                             				  Mobility

Not
                                             				  Supported

Supported

Supported

Forward
                                             				  All

Supported

Supported

Supported

Group
                                             				  Pickup

Supported

Supported

Supported

Hold

Supported

Supported

Supported

Hook Flash

Not
                                             				  Supported

Not
                                             				  Supported

Not
                                             				  Supported

Hunt Group

Not
                                             				  Supported

Not
                                             				  Supported

Not
                                             				  Supported

Live
                                             				  Record

Not
                                             				  Supported

Not
                                             				  Supported

Not
                                             				  Supported

Login

Not
                                             				  Supported

Not
                                             				  Supported

Not
                                             				  Supported

Meet Me

Supported

Supported

Supported

Mobility

Not
                                             				  Supported

Supported

Supported

My Phone
                                             				  Apps

Not
                                             				  Supported

Supported

Supported

New Call

Not
                                             				  Supported

Supported

Supported

Night
                                             				  Service

Not
                                             				  Supported

Not
                                             				  Supported

Not
                                             				  Supported

Park

Not
                                             				  Supported

Supported

Supported

Personal
                                             				  Speed Dial

Not
                                             				  Supported

Not
                                             				  Supported

Not
                                             				  Supported

Pickup

Supported

Supported

Supported

Privacy

Supported

Supported

Supported

Redial

Supported

Supported

Supported

Remove
                                             				  Last Participant

Not
                                             				  Supported

Not
                                             				  Supported

Not
                                             				  Supported

Reset
                                             				  Phone

Not
                                             				  Supported

Not
                                             				  Supported

Not
                                             				  Supported

Services
                                             				  URL

Not
                                             				  Supported

Not
                                             				  Supported

Not
                                             				  Supported

Single
                                             				  Number Reach

Not
                                             				  Supported

Supported

Not
                                             				  Supported

Speed Dial

Supported

Supported

Supported

Transfer

Not
                                             				  Supported

Not
                                             				  Applicable 5

Not
                                             				  Applicable 2

Transfer
                                             				  to VM

Not
                                             				  Supported

Not
                                             				  Supported

Not
                                             				  Supported

Cisco Unified IP
                              		Phones 7902, 7905, 7906, 7910, 7911, 7912, 7935, 7936, 7937, 7940, 7960, and
                              		7985 do not support the PLK feature. The services URL button is not supported
                              		on the following Cisco Unified IP phones: 7920, 7921, 7925 (supports DnD and
                              		Privacy only), 3911, and 3951.

Table 4 lists the PLK features available on the Cisco Unified 7800 and 8800 series SIP
                              		IP Phones from Cisco Unified CME Release 11.0 onwards. As part of Unified CME
                              		Release 11.7, new phone support for Cisco IP Phones 8821, 8845, 8865 was
                              		introduced. With this addition, Unified CME supports all phone models in Cisco
                              		IP Phone 7800 Series and Cisco IP Phone 8800 Series.

Softkeys
                                             				  Supported as Programmable Line Keys

Cisco
                                             				  Unified 7800 Series SIP IP Phones

Cisco
                                             				  Unified 8800 Series SIP IP Phones

Acct

Not
                                             				  Supported

Not
                                             				  Supported

Call Back

Not
                                             				  Supported

Not
                                             				  Supported

Conference

Not
                                             				  Supported

Not
                                             				  Supported

Conference
                                             				  List

Supported

Supported

Customized
                                             				  URL

Not
                                             				  Supported

Not
                                             				  Supported

Do Not
                                             				  Disturb

Supported

Supported

End Call

Supported

Supported

Extension
                                             				  Mobility

Supported

Supported

Forward
                                             				  All

Supported

Supported

Group
                                             				  Pickup

Supported

Supported

Hold

Supported

Supported

Hook Flash

Not
                                             				  Supported

Not
                                             				  Supported

HLog (From
                                             				  Unified CME Release 11.6 onwards)

Supported

Supported

Live
                                             				  Record

Not
                                             				  Supported

Not
                                             				  Supported

Login

Not
                                             				  Supported

Not
                                             				  Supported

Meet Me

Supported

Supported

Mobility

Supported

Supported

My Phone
                                             				  Apps

Supported

Supported

New Call

Supported

Supported

Park

Supported

Supported

Personal
                                             				  Speed Dial

Not
                                             				  Supported

Not
                                             				  Supported

Pickup

Supported

Supported

Privacy

Supported

Supported

Redial

Supported

Supported

Remove
                                             				  Last Participant

Not
                                             				  Supported

Not
                                             				  Supported

Reset
                                             				  Phone

Not
                                             				  Supported

Not
                                             				  Supported

Services
                                             				  URL

Not
                                             				  Supported

Not
                                             				  Supported

Single
                                             				  Number Reach

Not
                                             				  Supported

Not
                                             				  Supported

Speed Dial

Supported

Supported

Transfer

Not
                                             				  Supported

Not
                                             				  Supported

Transfer
                                             				  to VM

Not
                                             				  Supported

Not
                                             				  Supported

Table 5 lists the feature buttons and their corresponding LED behavior. Only features
                              		with radio icons will indicate their state via LED.

Feature

Label/Tagged ID

Label/Extended Tagged ID

Icon

LED
                                             				  Behavior

Redial

Redial/SkRedialTag 0x01

—

Default

—

Hold

Hold/SkHoldTag 0x03

—

Hold

—

Transfer

Transfer/SkTrnsferTag 0x04

—

Transfer

—

Forward
                                             				  All

Forward
                                             				  All/0x2D

Default

—

MeetMe

MeetMe/
                                             				  SkMeetMeConfrn Tag 0x10

—

Default

—

Conference

Conference/SkConfrnTag 0x34

—

Conference

—

Park

Park/SkParkTag 0x0E

—

Default

—

PickUp

PickUp/SkCallPickUpTag 0x11

—

Default

—

GPickUp

—

Group
                                             				  PickUp/0x2F

Default

—

Mobility

—

Mobility/0x2B

Mobility

—

Do Not
                                             				  Disturb

—

Do Not
                                             				  Disturb/0x0f

Radio
                                             				  Button

On—active

Off—inactive

Conference
                                             				  List

—

Conference
                                             				  List/0x34

Default

—

Remove
                                             				  Last Participant

—

Remove
                                             				  Last Participant/0x30

Default

—

CallBack

CallBack/SkCallBackTag 0x41

—

Default

—

New Call

NewCall/SkNewCallTag 0x02

—

Default

—

End Call

—

End
                                             				  Call/0x33

Default

—

Cancel
                                             				  Call Waiting

CW Off

—

Default

—

HLog

—

Hunt
                                             				  Group/0x36

Default

On—hlog in

Off—hlog
                                             				  out

Blink—call
                                             				  in queue at Hlogout state

Privacy

Private/
                                             				  SkPrivacy 0x36

—

Radio
                                             				  Button

On—active

Off—inactive

Acct

Acct/
                                             				  TAGS_ACCT_ 40

TAGS_Acct[]

—

Default

—

Flash

Flash/
                                             				  TAGS_FLASH_ 41

TAGS_Flash[]

—

Default

—

Login

Login/
                                             				  TAGS_LOGIN_ 42

TAGS_Login[]

—

Default

—

TrnsfVM

TrnsfVM/SkTrnsfVMTag 0x3e

—

Default

—

LiveRcd

LiveRcd

—

Default

—

Night
                                             				  Service

Night
                                             				  Service/ TAGS_Night_Service[]

—

Radio
                                             				  Button

On—active

Off—inactive

Myphoneapp
                                             				  URL service

My Phone
                                             				  Apps

—

URL
                                             				  service

—

EM URL
                                             				  service

Extension
                                             				  Mobility

—

URL
                                             				  service

—

SN URL
                                             				  service

Single
                                             				  Number Reach

—

URL
                                             				  service

—

Customized

URL

The
                                             				  configured name

—

URL
                                             				  service

—

## Configure
                        	 Softkeys

### Modify Softkey
                           	 Display on SCCP Phone

To modify the display of softkeys, perform the following steps.

Restriction

- Enable the ConfList and MeetMe softkeys only if you have hardware conferencing configured. For information on conferencing,
                                                see Hardware Conference .

- The third softkey button on
                                                				the Cisco Unified IP Phone 7905G and Cisco Unified IP Phone 7912G is reserved
                                                				for the Message softkey. For these phones’ templates, the third softkey button
                                                				defaults to the Message softkey. For example, the softkeys idle Redial Dnd
                                                      					 Pickup Login Gpickup command configuration displays, in order,
                                                				the Redial, DND, Message, PickUp, Login, and GPickUp softkeys.

- The NewCall softkey cannot
                                                				be disabled on the Cisco Unified IP Phone 7905G or Cisco Unified IP Phone
                                                				7912G.

#### Before you begin

- Cisco CME 3.2 or a later
                                    			 version.

- Cisco Unified CME 4.2 or a
                                    			 later version to enable softkeys during the ringing call state.

- Cisco Unified CME 4.3 or a
                                    			 later version to enable softkeys during the remote-in-use state.

- The HLog softkey must be
                                    			 enabled with the hunt-group logout
                                          				  HLog command before it will be displayed. For more information,
                                    			 see Configure Ephone-Hunt Groups on SCCP Phones .

- The Flash softkey must be
                                    			 enabled with the fxo
                                          				  hook-flash command before it will be displayed. For configuration
                                    			 information, see Enable Flash Softkey .

### SUMMARY STEPS

- enable

- configure terminal

- ephone-template template-tag

- softkeys alerting {[ Acct ] [ Callback ] [ Endcall ]}

- softkeys
                                       				  connected {[ Acct ] [ ConfList ] [ Confrn ] [ Endcall ] [ Flash ] [ Hlog ] [ Hold ] [ Join ] [ LiveRcd ] [ Park ] [ RmLstC ] [ Select ] [ TrnsfVM ] [Trnsfer]}

- softkeys hold {[ Join ] [ Newcall ] [ Resume ] [ Select ]}

- softkeys
                                       				  idle {[ Cfwdall ]
                                 			 [ ConfList ]
                                 			 [ Dnd ]
                                 			 [ Gpickup ]
                                 			 [ Hlog ]
                                 			 [ Join ]
                                 			 [ Login ]
                                 			 [ Newcall ]
                                 			 [ Pickup ]
                                 			 [ Redial ]
                                 			 [ RmLstC ]}

- softkeys
                                       				  remote-in-use {[ CBarge ]
                                 			 [ Newcall ]}

- softkeys
                                       				  ringing {[ Answer ]
                                 			 [ Dnd ]
                                 			 [ HLog ]}

- softkeys seized {[ CallBack ] [ Cfwdall ] [ Endcall ]
                                    				[ Gpickup ] [ Hlog ] [ MeetMe ] [ Pickup ]
                                    				[ Redial ]}

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
Router(config)# ephone-template 15
```

Enters
                                             				ephone-template configuration mode to create an ephone template.

- template-tag—Unique
                                                				  identifier for the ephone template that is being created. Range is 1 to 20.

Step 4

softkeys alerting {[ Acct ] [ Callback ] [ Endcall ]}

#### Example:

```
Router(config-ephone-template)# softkeys alerting Callback Endcall
```

(Optional)
                                             				Configures an ephone template for softkey display during the alerting call
                                             				state.

- You can enter any of the
                                                				  keywords in any order.

- Default is all softkeys are
                                                				  displayed in alphabetical order.

- Any softkey that is not
                                                				  explicitly defined is disabled.

Step 5

softkeys
                                                				  connected {[ Acct ] [ ConfList ] [ Confrn ] [ Endcall ] [ Flash ] [ Hlog ] [ Hold ] [ Join ] [ LiveRcd ] [ Park ] [ RmLstC ] [ Select ] [ TrnsfVM ] [Trnsfer]}

#### Example:

```
Router(config-ephone-template)# softkeys connected Endcall Hold Transfer Hlog
```

(Optional)
                                             				Configures an ephone template for softkey display during the call-connected
                                             				state.

- You can enter any of the
                                                				  keywords in any order.

- Default is all softkeys are
                                                				  displayed in alphabetical order.

- Any softkey that is not
                                                				  explicitly defined is disabled.

Step 6

softkeys hold {[ Join ] [ Newcall ] [ Resume ] [ Select ]}

#### Example:

```
Router(config-ephone-template)# softkeys hold Resume
```

(Optional)
                                             				Configures an ephone template for softkey display during the call-hold state.

- You can enter any of the
                                                				  keywords in any order.

- Default is all softkeys
                                                				  are displayed in alphabetical order.

- Any softkey that is not
                                                				  explicitly defined is disabled.

Step 7

softkeys
                                                				  idle {[ Cfwdall ]
                                          			 [ ConfList ]
                                          			 [ Dnd ]
                                          			 [ Gpickup ]
                                          			 [ Hlog ]
                                          			 [ Join ]
                                          			 [ Login ]
                                          			 [ Newcall ]
                                          			 [ Pickup ]
                                          			 [ Redial ]
                                          			 [ RmLstC ]}

#### Example:

```
Router(config-ephone-template)# softkeys idle Newcall Redial Pickup Cfwdall Hlog
```

(Optional)
                                             				Configures an ephone template for softkey display during the idle state.

- You can enter any of the
                                                				  keywords in any order.

- Default is all softkeys
                                                				  are displayed in alphabetical order.

- Any softkey that is not
                                                				  explicitly defined is disabled.

Step 8

softkeys
                                                				  remote-in-use {[ CBarge ]
                                          			 [ Newcall ]}

#### Example:

```
Router(config-ephone-template)# softkeys remote-in-use CBarge Newcall
```

Modifies the
                                             				order and type of softkeys that display on an IP phone during the remote-in-use
                                             				call state.

Step 9

softkeys
                                                				  ringing {[ Answer ]
                                          			 [ Dnd ]
                                          			 [ HLog ]}

#### Example:

```
Router(config-ephone-template)# softkeys ringing Answer Dnd Hlog
```

(Optional)
                                             				Configures an ephone template for softkey display during the ringing state.

- You can enter any of the
                                                				  keywords in any order.

- Default is all softkeys
                                                				  are displayed in alphabetical order.

- Any softkey that is not
                                                				  explicitly defined is disabled.

Step 10

softkeys seized {[ CallBack ] [ Cfwdall ] [ Endcall ]
                                             				[ Gpickup ] [ Hlog ] [ MeetMe ] [ Pickup ]
                                             				[ Redial ]}

#### Example:

```
Router(config-ephone-template)# softkeys seized Endcall Redial Pickup Cfwdall Hlog
```

(Optional)
                                             				Configures an ephone template for softkey display during the seized state.

- You can enter any of the
                                                				  keywords in any order.

- Default is all softkeys
                                                				  are displayed in alphabetical order.

- Any softkey that is not
                                                				  explicitly defined is disabled.

Step 11

exit

#### Example:

```
Router(config-ephone-template)# exit
```

Exits
                                             				ephone-template configuration mode.

Step 12

ephone phone-tag

#### Example:

```
Router(config)# ephone 36
```

Enters
                                             				ephone configuration mode.

- phone-tag—Unique sequence
                                                				  number that identifies this ephone during configuration tasks.

Step 13

ephone-template template-tag

#### Example:

```
Router(config-ephone)# ephone-template 15
```

Applies an
                                             				ephone template to the ephone that is being configured.

Step 14

end

#### Example:

```
Router(config-ephone)# end
```

Returns to
                                             				privileged EXEC mode.

#### What to do next

If you are done
                                 		  modifying the parameters for phones in Cisco Unified CME, generate a new
                                 		  configuration file and restart the phones. See Generate Configuration Files for SCCP Phones .

### Modify Softkey
                           	 Display on SIP Phone

Restriction

- This feature is supported
                                                   				only for Cisco Unified IP Phones 7911G, 7941G, 7941GE, 7961G, 7961GE, 7970G,
                                                   				and 7971GE.

- You can download a custom
                                                   				softkey XML file from a TFTP server. However, if the softkey XML file contains
                                                   				an error, the softkeys might not work properly on the phone. We recommend the
                                                   				following procedure for creating a softkey template in Cisco Unified CME.

HLog
                                                      				  softkey is supported only on Cisco Unified IP Phones 7800 and 8800 series.

#### Before you begin

### SUMMARY STEPS

- enable

- configure terminal

- voice register template template-tag

- softkeys
                                       				  connected {[ Confrn ]
                                 			 [ Endcall ]
                                 			 [ Hold ] [ Trnsfer ] [ HLog ]
                                    				}

- softkeys hold {[ Newcall ] { Resume ]}

- softkeys idle {[ Cfwdall ]
                                 			 [ Newcall ]
                                 			 [ Redial ]
                                 			 [ HLog ] }

- softkeys
                                       				  seized {[ Cfwdall ] [ Endcall ] [ Redial ]}

- softkeys
                                       				  personal-conf-user

- exit

- voice register pool pool-tag

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
Router(config)# voice register template 9
```

Enters voice
                                             				register template configuration mode to create a SIP phone template.

- template-tag —Range: 1 to 10.

Step 4

softkeys
                                                				  connected {[ Confrn ]
                                          			 [ Endcall ]
                                          			 [ Hold ] [ Trnsfer ] [ HLog ]
                                             				}

#### Example:

```
Router(config-register-template)# softkeys connected Endcall Hold Transfer HLog
```

(Optional)
                                             				Configures a SIP phone template for softkey display during the call-connected
                                             				state.

- You can enter the keywords
                                                				  in any order.

- Default is all softkeys are
                                                				  displayed in alphabetical order.

- Any softkey that is not
                                                				  explicitly defined is disabled.

Step 5

softkeys hold {[ Newcall ] { Resume ]}

#### Example:

```
Router(config-register-template)# softkeys hold Resume
```

(Optional)
                                             				Configures a phone template for softkey display during the call-hold state.

- Default is that the NewCall
                                                				  and Resume softkeys are displayed in alphabetical order.

- Any softkey that is not
                                                				  explicitly defined is disabled.

Step 6

softkeys idle {[ Cfwdall ]
                                          			 [ Newcall ]
                                          			 [ Redial ]
                                          			 [ HLog ] }

#### Example:

```
Router(config-register-template)# softkeys idle Newcall Redial Cfwdall HLog
```

(Optional)
                                             				Configures a phone template for softkey display during the idle state.

- You can enter the keywords
                                                				  in any order.

- Default is all softkeys are
                                                				  displayed in alphabetical order.

- Any softkey that is not
                                                				  explicitly defined is disabled.

Step 7

softkeys
                                                				  seized {[ Cfwdall ] [ Endcall ] [ Redial ]}

#### Example:

```
Router(config-register-template)# softkeys seized Endcall Redial Cfwdall
```

(Optional)
                                             				Configures a phone template for softkey display during the seized state.

- You can enter the keywords
                                                				  in any order.

- Default is all softkeys are
                                                				  displayed in alphabetical order.

- Any softkey that is not
                                                				  explicitly defined is disabled.

Step 8

softkeys
                                                				  personal-conf-user

#### Example:

```
Router(config-register-template)# softkeys personal-conf-user
```

(Optional)
                                             				Configures a personal user phone template for softkey display.

- The CLI command is
                                                				  disabled by default, and applies a public user phone template.

- When you configure the no
                                                				  form of this command, support switches to public user phone template.

When the CLI command softkeys personal-conf-user is
                                                   					 configured, you cannot configure other state specific softkeys.

- The CLI command is
                                                				  supported only for the Cisco IP Conference Phone 7832 and Cisco IP Conference
                                                				  Phone 8832 phone types.

Step 9

exit

#### Example:

```
Router(config-register-template)# exit
```

Exits voice
                                             				register template configuration mode.

Step 10

voice register pool pool-tag

#### Example:

```
Router(config)# voice register pool 36
```

Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone.

Step 11

template template-tag

#### Example:

```
Router(config-register-pool)# template 9
```

Applies a
                                             				SIP phone template to the phone you are configuring.

- template-tag — Template tag that was created with
                                                				  the voice register
                                                      						template command in Step 3 .

Step 12

end

#### Example:

```
Router(config-register-pool)# end
```

Exits to
                                             				privileged EXEC mode.

#### What to do next

If you are done
                                 		  modifying the parameters for phones in Cisco Unified CME, generate a new
                                 		  configuration file and restart the phones. See Generate Configuration Profiles for SIP Phones .

### Verify Softkey
                           	 Configuration

Step 1

show running-config

Use this
                                             				command to verify your configuration. In the following example, the softkey
                                             				display is modified in phone template 7 and the template is applied to SIP
                                             				phone 2. All other phones use the default arrangement of softkeys.

#### Example:

```
Router# show running-config
!
voice register dn 1 dual-line
 ring feature secondary 
 number 126 secondary 1261 
 description Sales
 name Smith
 call-forward busy 500 secondary
 call-forward noan 500 timeout 10
 huntstop channel
 no huntstop
 no forward local-calls
!
!
voice register template 7
 session-transport tcp
 softkeys hold Resume Newcall
 softkeys idle Newcall Redial Cfwdall HLog
 softkeys connected Endcall Trnsfer Confrn Hold Hlog 
 voicemail 52001 timeout 30
.
.
.
voice register pool 2
 id mac 0030.94C2.A22A
 number 1 dn 4 
 template 7
 dialplan 3
!
```

Step 2

show
                                                				  telephony-service ephone-template or show voice register
                                                				  template template-tag

#### Example:

These commands
                                             				display the contents of individual templates.

```
Router# show telephony-service ephone-template
ephone-template 1
softkey ringing Answer Dnd
conference drop-mode never
conference add-mode all
conference admin: No
Always send media packets to this router: No
Preferred codec: g711ulaw
User Locale: US
Network Locale: US
```

or

```
Router# show voice register template 7
Temp Tag 7
Config:
 Attended Transfer is enabled
 Blind Transfer is enabled
 Semi-attended Transfer is enabled
 Conference is enabled
 Caller-ID block is disabled
 DnD control is enabled
 Anonymous call block is disabled
 Voicemail is 52001, timeout 30
 KPML is disabled
 Transport type is tcp
 softkey connected Endcall Trnsfer Confrn Hold HLog
 softkey hold Resume Newcall
 softkey idle Newcall Redial Cfwdall HLog
```

### Enable Flash
                           	 Softkey

Restriction

The IP phone
                                             			 must support softkey display.

#### Before you begin

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- fxo hook-flash

- restart all

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

fxo hook-flash

#### Example:

```
Router(config-telephony)# fxo hook-flash
```

Enables the
                                             				Flash softkey on phones that support softkey display on PSTN calls using an FXO
                                             				port.

Step 5

restart all

#### Example:

```
Router(config-telephony)# restart all
```

Performs a
                                             				fast reboot of all phones associated with this Cisco Unified CME router. Does
                                             				not contact the DHCP or TFTP server for updated information.

Step 6

end

#### Example:

```
Router(config-telephony)# end
```

Returns to
                                             				privileged EXEC mode.

### Verify Flash
                           	 Softkey Configuration

Step 1

Use the show running-config command to display an entire configuration, including
                                          			 Flash softkey, which is listed in the telephony-service portion of the output.

#### Example:

```
Router# show running-config
telephony-service
 fxo hook-flash
 load 7960-7940 P00305000600
 load 7914 S00103020002
 max-ephones 100
 max-dn 500
```

Step 2

Use the show
                                                				  telephony-service command to show only the telephony-service
                                          			 portion of the configuration.

### Configure Feature
                           	 Blocking

#### Before you begin

### SUMMARY STEPS

- enable

- configure terminal

- ephone-template template-tag

- features blocked [ CFwdAll ] [ Confrn ] [ GpickUp ] [ Park ] [ PickUp ] [ Trnsfer ]

- exit

- ephone phone-tag

- ephone-template template-tag

- restart

- Repeat Step 5 to Step 8 for each phone to
                                 			 which the template should be applied.

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
Router(config)# ephone-template 1
```

Enters
                                             				ephone-template configuration mode.

- template-tag —Unique sequence number that
                                                				  identifies this template during configuration tasks. Range is 1 to 20.

Step 4

features blocked [ CFwdAll ] [ Confrn ] [ GpickUp ] [ Park ] [ PickUp ] [ Trnsfer ]

#### Example:

```
Router(config-ephone-template)# features blocked Park Trnsfer
```

Prevents the
                                             				specified softkey from invoking its feature.

- CFwdAll —Call forward all calls.

- Confrn —Conference.

- GpickUp —Group call pickup.

- Park —Call park.

- PickUp —Directed or local call pickup. This
                                                				  includes pickup last-parked call and pickup from another extension or park
                                                				  slot.

- Trnsfer —Call transfer.

Step 5

exit

#### Example:

```
Router(config-ephone-template)# exit
```

Step 6

ephone phone-tag

#### Example:

```
Router(config)# ephone 25
```

Enters ephone
                                             				configuration mode.

- phone-tag —Unique sequence number that identifies
                                                				  this ephone during configuration tasks. The maximum number of ephones for a
                                                				  particular Cisco Unified CME system is version- and platform-specific. For the
                                                				  range of values, see the CLI help.

Step 7

ephone-template template-tag

#### Example:

```
Router(config-ephone)# ephone-template 1
```

Applies an
                                             				ephone template to an ephone.

- template-tag —Template number that you want to
                                                				  apply to this ephone.

Step 8

restart

#### Example:

```
Router(config-ephone)# restart
```

Performs a
                                             				fast reboot of this ephone. Does not contact the DHCP or TFTP server for
                                             				updated information.

Step 9

Repeat Step 5 to Step 8 for each phone to
                                          			 which the template should be applied.

—

Step 10

end

#### Example:

```
Router(config-ephone)# end
```

Returns to
                                             				privileged EXEC mode.

### Verify Block
                           	 Softkey Configuration

Step 1

Use the show
                                                				  running-config command to display the running configuration,
                                          			 including ephone templates and ephone configurations.

Step 2

Use the show telephony-service
                                                				  ephone-template command and the show telephony-service
                                                				  ephone command to display only the contents of ephone templates
                                          			 and the ephone configurations, respectively.

### Configure
                           	 Immediate Divert (iDivert) Softkey on SIP Phone

To configure
                                 		  iDivert softkey (in connected state) on Cisco Unified SIP IP phones, perform
                                 		  the following step.

Restriction

- iDivert feature is disabled
                                                   				when call-forward
                                                      				  all is activated for a phone.

- iDivert feature is not
                                                   				activated for the second call when call-forward
                                                      				  busy is activated for a phone and the phone is busy with the first call.

- If iDivert softkey is
                                                   				pressed before call forward no answer (CFNA) timeout, then the call is
                                                   				forwarded to voice mail.

- The calling and called
                                                   				parties can divert the call to their voice messaging mailboxes if both the
                                                   				parties press the iDivert softkey at the same time. The voice messaging mailbox
                                                   				of the calling party will receive a portion of the outgoing greeting of the
                                                   				called party. Similarly, the voice messaging mailbox of the called party will
                                                   				receive a portion of the outgoing greeting of the calling party.

- iDivert softkey is not
                                                   				supported when SIP phones fall back to SRST mode in Cisco Unified CME.

- iDivert after connect
                                                   				towards the voicemail with transcoding is not supported.

### SUMMARY STEPS

- enable

- configure terminal

- voice register template template-tag

- softkeys connected [Confrn] [Endcall] [Hold]
                                       				  [Trnsfer] [iDivert]

- softkeys hold [Newcall] {Resume] [
                                       				  iDivert]

- softkeys ringing [Answer] [DND]
                                       				  [iDivert]

- exit

- voice register pool pool-tag

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
Router(config)# voice register template 9
```

Enters voice
                                             				register template configuration mode to create a SIP phone template.

- template-tag —Range: 1 to 10.

Step 4

softkeys connected [Confrn] [Endcall] [Hold]
                                                				  [Trnsfer] [iDivert]

#### Example:

```
Router(config-register-template)# softkeys connected Endcall Hold Transfer iDivert
```

(Optional)
                                             				Configures a SIP phone template for softkey display during the call-connected
                                             				state.

- You can enter the keywords
                                                				  in any order.

- Default is all softkeys are
                                                				  displayed in alphabetical order.

- Any softkey that is not
                                                				  explicitly defined is disabled.

Step 5

softkeys hold [Newcall] {Resume] [
                                                				  iDivert]

#### Example:

```
Router(config-register-template)# softkeys hold Newcall Resume
```

(Optional)
                                             				Configures a phone template for softkey display during the call-hold state.

- Default is that the NewCall
                                                				  and Resume softkeys are displayed in alphabetical order.

- Any softkey that is not
                                                				  explicitly defined is disabled.

Step 6

softkeys ringing [Answer] [DND]
                                                				  [iDivert]

#### Example:

```
Router(config-register-temp)# softkeys ringin dnd answer idivert
```

Modifies the
                                             				order and type of softkeys that display on a SIP phone during the ringing call
                                             				state.

Step 7

exit

#### Example:

```
Router(config-register-template)# exit
```

Exits voice
                                             				register template configuration mode.

Step 8

voice register pool pool-tag

#### Example:

```
Router(config)# voice register pool 36
```

Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone.

Step 9

template template-tag

#### Example:

```
Router(config-register-pool)# template 9
```

Applies a SIP
                                             				phone template to the phone you are configuring.

- template-tag — Template tag that was created with
                                                				  the voice register template command in Step 3 .

Step 10

end

#### Example:

```
Router(config-register-pool)# end
```

Exits
                                             				configuration mode.

### Configure Service
                           	 URL Line Key Button on SCCP Phone

### SUMMARY STEPS

- enable

- configure terminal

- ephone template template-tag

- url-button index type | url
                                 			 [name]

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

ephone template template-tag

#### Example:

```
Router(config)# ephone template 5
```

Enters
                                             				ephone-template configuration mode to create an ephone template.

- template-tag —Unique identifier for the ephone
                                                				  template that is being created. Range: 1 to 10.

Step 4

url-button index type | url
                                          			 [name]

#### Example:

```
Router#(config-ephone-template)#url-button 1 myphoneapp
```

```
Router(config-ephone-template)#url-button 2 em
```

```
Router(config-ephone-template)#url-button 3 snr
```

```
Router (config-ephone-template)#url-button 4 http://www.cisco.com
```

Configures a
                                             				service URL button on a line key.

- index —Unique index number. Range: 1 to 8.

myphoneapp: My phone application configured under phone
                                                         						  user interface.

em: Extension Mobility.

snr: Single Number Reach.

- url name —Service
                                                				  URL with maximum length of 31 characters.

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

- phone-tag —Unique sequence number that identifies
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

#### What to do next

If you are done
                                 		  configuring the URL buttons for phones in Cisco Unified CME, restart the
                                 		  phones.

### Configure Service
                           	 URL Line Key Button on SIP Phone

### SUMMARY STEPS

- enable

- configure terminal

- voice register template template-tag

- url-button [ index number ]
                                 			 [ url location ]
                                 			 [ url name ]

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

Enters voice
                                             				register template configuration mode to create a SIP phone template.

- template-tag —Unique identifier for the template
                                                				  that is being created. Range: 1 to 10.

Step 4

url-button [ index number ]
                                          			 [ url location ]
                                          			 [ url name ]

#### Example:

```
Router(config-register-temp)url-button 1 http:// www.cisco.com
```

Configures a
                                             				service URL button on a line key.

- index number —Unique
                                                				  index number. Range: 1 to 8.

- url location —Location of the URL.

- url name —Service
                                                				  URL with maximum length of 31 characters.

Step 5

exit

#### Example:

```
Router(config-register-temp)# exit
```

Exits voice
                                             				register template configuration mode.

Step 6

voice register pool phone-tag

#### Example:

```
Router(config)# voice register pool 12
```

Enters voice
                                             				register pool configuration mode.

- phone-tag —Unique number that identifies this voice
                                                				  register pool during configuration tasks.

Step 7

template template-tag

#### Example:

```
Router(config-register-pool)# template 5
```

Applies the
                                             				SIP phone template to the phone.

- template-tag —Unique identifier of the template
                                                				  that you created in Step 3.

Step 8

end

#### Example:

```
Router(config-register-pool)# end
```

Returns to
                                             				privileged EXEC mode.

#### What to do next

If you are done
                                 		  configuring the URL buttons for phones in Cisco Unified CME, generate a new
                                 		  configuration file and restart the phones. See Generate Configuration Profiles for SIP Phones .

### Configure Feature
                           	 Buttons on SCCP Phone Line Key

Restriction

- Answer, Select, cBarge,
                                                				Join, and Resume features are not supported as PLKs.

- Feature buttons are only
                                                				supported on Cisco Unified IP Phones 6911, 7941, 7942, 7945, 7961, 7962, 7965.
                                                				7970, 7971, and 7975 with SCCP v12 or later versions.

- Any features available
                                                				through hard buttons are not provisioned. Use the show
                                                   				  ephone register detail command to verify why the features buttons are not
                                                				provisioned.

- Not all feature buttons are
                                                				supported on Cisco Unified IP Phone 6911 phone. Call Forward, Pickup, Group
                                                				Pickup, and MeetMe are the only feature buttons supported on the Cisco Unified
                                                				IP Phone 6911.

- The privacy-button command is available on Cisco Unified IP
                                                				phones running a SCCP Version 8 or later versions. The privacy-buttton command is overridden by any other available
                                                				feature buttons.

- Locales are not supported
                                                				on Cisco Unified IP Phone 7914.

- Locales are not supported
                                                				for Cancel Call Waiting or Live Recording feature buttons.

- The feature state for DnD,
                                                				Hlog, Privacy, Login, and Night Service feature buttons are indicated by an
                                                				LED. For a list of LED behavior for PLK, see Table 5

### SUMMARY STEPS

- enable

- configure terminal

- ephone template template-tag

- feature-button index <feature
                                       				  identifier> [ label < label >]

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

ephone template template-tag

#### Example:

```
Router(config)# ephone template 10
```

Enters
                                             				ephone-template configuration mode to create an ephone template.

- template-tag -
                                                				  Unique identifier for the ephone template that is being created. Range: 1 to 10

Step 4

feature-button index <feature
                                                				  identifier> [ label < label >]

#### Example:

```
Router(config-ephone-template)feature-button 1 label hold
```

Configures a
                                             				feature button on a line key.

index - Index number, one from 25 for a specific
                                                   					 feature type.

feature identifier -Feature ID or stimulus ID.

label -Non-default text label.

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
Router(config)# ephone 5
```

Enters ephone
                                             				configuration mode.

phone-tag - Unique sequence number that identifies
                                                   					 this ephone during configuration tasks.

Step 7

ephone-template template-tag

#### Example:

```
Router(config-ephone)# ephone-template 10
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

#### What to do next

If you are done
                                 		  configuring the feature buttons for phones in Cisco Unified CME, restart the
                                 		  phones.

### Configure Feature
                           	 Buttons on SIP Phone Line Key

### SUMMARY STEPS

- enable

- configure terminal

- voice register template template-tag

- feature-button [ index ] [ feature identifier ]

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

Enters voice
                                             				register template configuration mode to create a SIP phone template.

template-tag -Unique identifier for the template
                                                   					 that is being created. Range: 1 to 10.

Feature
                                                         				  button can be configured under voice register pool or voice register template
                                                         				  configuration mode. If both configurations are applied, the feature button
                                                         				  configuration under voice register pool takes precedence.

Step 4

feature-button [ index ] [ feature identifier ]

#### Example:

```
Router(config-voice-register-template)feature-button 1 DnD
```

```
Router(config-voice-register-template)feature-button
 2 EndCall
```

```
Router(config-voice-register-template)feature-button 3 Cfwdall
```

Configures a
                                             				feature button on a line key.

- index —One of the 12 index numbers for a specific
                                                				  feature type.

- feature identifier —Unique identifier for a feature. One of the
                                                				  following feature or stimulus IDs: Redial, Hold, Trnsfer, Cfwdall, Privacy,
                                                				  MeetMe, Confrn, Park, Pickup. Gpickup, Mobility, Dnd, ConfList, RmLstC,
                                                				  CallBack, NewCall, EndCall, HLog, NiteSrv, Acct, Flash, Login, TrnsfVM, or
                                                				  LiveRcd.

Step 5

exit

#### Example:

```
Router(config-register-temp)# exit
```

Exits voice
                                             				register template configuration mode.

Step 6

voice register pool phone-tag

#### Example:

```
Router(config)# voice register pool 12
```

Enters voice
                                             				register pool configuration mode.

- phone-tag —Unique number that identifies this voice
                                                				  register pool during configuration tasks.

Step 7

template template-tag

#### Example:

```
Router(config-register-pool)# template 5
```

Applies the
                                             				template to the phone.

- template-tag —Unique identifier of the template
                                                				  that you created in Step 3.

Step 8

end

#### Example:

```
Router(config-register-pool)# end
```

Returns to
                                             				privileged EXEC mode.

#### What to do next

If you are done
                                 		  configuring the feature buttons for phones in Cisco Unified CME, generate a new
                                 		  configuration file and restart the phones. See Generate Configuration Profiles for SIP Phones

## Configuration Example for Softkeys

### Example for Modifying Softkey Display

The following example modifies the softkey display on four phones by
                                 		  creating two ephone templates. Ephone template 1 is applied to ephone 11, 13,
                                 		  and 15. Template 2 is applied to ephone 34. The softkey displays on all other
                                 		  phones use the default arrangement of keys.

```
ephone-template 1
```

```
softkeys idle Redial Newcall
```

```
softkeys connected Endcall Hold Trnsfer
```

```
ephone-template 2
```

```
softkeys idle Redial Newcall
```

```
softkeys seized Redial Endcall Pickup
```

```
softkeys alerting Redial Endcall
```

```
softkeys connected Endcall Hold Trnsfer
```

```
ephone 11
```

```
ephone-template 1
```

```
ephone 13
```

```
ephone-template 1
```

```
ephone 15
```

```
ephone-template 1
```

```
ephone 34
```

```
ephone-template 2
```

### Example for
                           	 Modifying HLog Softkey for SCCP Phones

The following
                                 		  example establishes the appearance and order of softkeys for phones that are
                                 		  configured with ephone-template 7. The Hlog key is available when a phone is
                                 		  idle, when it has seized a line, or when it is connected to a call. Phones
                                 		  without softkeys can use the standard HLog codes to toggle ready and not-ready
                                 		  status.

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
.
```

```
.
```

```
ephone-template 7
```

```
softkeys connected Endcall Hold Transfer Hlog
```

```
softkeys idle Newcall Redial Pickup Cfwdall Hlog
```

```
softkeys seized Endcall Redial Pickup Cfwdall Hlog
```

### Example for
                           	 Modifying HLog Softkey for SIP Phones

The following
                                 		  example establishes the appearance and order of softkeys for phones that are
                                 		  configured with voice register template 7. The Hlog key is available when a
                                 		  phone is idle, when there is a ringIn, or when it is connected to a call.
                                 		  Phones without softkeys can use the standard HLog codes to toggle ready and
                                 		  not-ready status.

```
telephony-service
 hunt-group logout HLog
 fac standard
.
.
voice register template 7
 softkeys connected Endcall Hold Transfer Hlog
 softkeys idle Newcall Redial Pickup Cfwdall Hlog
 softkeys ringIn Answer DND iDivert Hlog
```

### Example for Enabling Flash Softkey for PSTN Calls

The following example enables the Flash softkey for PSTN calls through
                                 		  an FXO voice port:

```
telephony-service
```

```
fxo hook-flash
```

### Example for Park and Transfer Blocking

The following example blocks the use of Park and Transfer softkeys on
                                 		  extension 2333:

```
ephone-template 1
```

```
features blocked Park Trnsfer
```

```
ephone-dn 2
```

```
number 2333
```

```
ephone 3
```

```
button 1:2
```

```
ephone-template 1
```

### Example for Conference Blocking

The following example blocks the conference feature on extension 2579,
                                 		  which is on an analog phone:

```
ephone-template 1
```

```
features blocked Confrn
```

```
ephone-dn 78
```

```
number 2579
```

```
ephone 3
```

```
ephone-template 1
```

```
mac-address C910.8E47.1282
```

```
type anl
```

```
button 1:78
```

### Example for
                           	 Immediate Divert (iDivert) Configuration

The following
                                 		  example shows iDivert softkey in connected state:

```
Router# show voice register template 1
```

```
Temp Tag 1
```

```
Config:
```

```
Attended Transfer is enabled
```

```
Blind Transfer is enabled
```

```
Semi-attended Transfer is enabled
```

```
Conference is enabled
```

```
Caller-ID block is disabled
```

```
DnD control is enabled
```

```
Anonymous call block is disabled
```

```
Softkeys connected iDivert
```

### Example for Configuring URL Buttons on a SCCP Phone Line Key

The following example shows three URL buttons configured for line
                                 		  keys:

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
ephone-template  5
```

```
url-button 1 em
```

```
url-button 2 mphoneapp mphoneapp
```

```
url-button 3 snr
```

```
!
```

```
ephone  36
```

```
ephone-template 5
```

### Example for Configuring URL Buttons on a SIP Phone Line Key

The following example shows URL buttons configured in voice register
                                 		  template 1:

```
Router# show run ! voice register template  1
```

```
url-button 1 http://9.10.10.254:80/localdirectory/query My_Dir
```

```
url-button 5 http://www.yahoo.com Yahoo
```

```
! voice register pool  50
```

```
!
```

### Example for Configuring Feature Button on a SCCP Phone Line
                           	 Key

The following example shows feature buttons configured for line keys:

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
ephone-template  10
```

```
feature-button 1 Park
```

```
feature-button 2 MeetMe
```

```
feature-button 3 CallBack
```

```
!
```

```
!
```

```
ephone-template 10
```

### Example for
                           	 Configuring Feature Button on a SIP Phone Line Key

The following
                                 		  example shows three feature buttons configured for line keys:

```
voice register template  5
 feature-button 1 DnD
 feature-button 2 EndCall
 feature-button 3 Cfwdall
 feature-button 4 HLog
```

```
! !
```

```
voice register pool 12
```

```
template 5
```

#### Where to Go
                                 		  Next

For more details
                                             			 on HLog functionality, see Call Coverage Features chapter.

If you are done
                                 		  modifying the parameters for phones in CiscoUnifiedCME, generate a new
                                 		  configuration file and restart the phones. For more information, see Generate Configuration Files for Phones .

#### Ephone
                                 		  Templates

The softkeys commands are included in ephone templates that are
                                 		  applied to one or more individual ephones. For more information about
                                 		  templates, see Templates .

#### HLog Softkey

The HLog softkey
                                 		  must be enabled with the hunt-group logout
                                       				HLog command before it will be displayed. For more information,
                                 		  see Configure Call Coverage Features .

## Feature
                        	 Information for Softkeys

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature
                                          					 Name

Cisco Unified CME Version

Feature
                                          					 Information

Account
                                          					 Code Entry

3.0

Account
                                          					 code entry was introduced.

Barge
                                          					 Softkey

4.3

The
                                          					 Barge, LiveRcd, and TrnsfVM softkeys were added.

Conferencing Softkeys

4.1

The
                                          					 ConfList, Join, MeetMe, RmLstC, and Select softkeys were added.

Feature
                                          					 Blocking

4.0

Feature
                                          					 blocking was introduced.

Feature
                                          					 Policy Softkey Control

8.5

Allows
                                          					 control display of softkeys on the Cisco Unified SIP IP Phones 8961, 9951, and
                                          					 9971 using the feature policy template.

Flash
                                          					 Softkey

3.0

Flash
                                          					 softkey was introduced.

Immediate Divert Softkey for SIP Phones

8.5

Added
                                          					 support for iDivert softkey for SIP IP phones.

Programmable Line Keys

8.5

Allows
                                          					 you to configure a feature button or a URL button on a line key on both SIP and
                                          					 SCCP IP Phones.

Programmable Line Keys Enhancement

8.8

Adds
                                          					 support for softkeys as programmable line keys on Cisco Unified 6945, 8941, and
                                          					 8945 SCCP IP Phones.

Programmable Line Keys for Cisco Unified SIP IP Phones

9.0

Adds
                                          					 support for softkeys as programmable line keys on Cisco Unified 6911, 6921,
                                          					 6941, 6945, 6961, 8941, and 8945 SIP IP Phones.

Softkey
                                          					 Display

12.3

Support added for the softkeys 'Recents', 'Contacts', 'Apps',
                                          					 'Favorites', 'Messages', and 'Settings' on Cisco IP Conference Phones 7832 and
                                          					 8832.

11.7

Support added for the softkeys 'Details' on Cisco IP Phone
                                          					 7800 Series, and 'Show detail' on Cisco IP Phone 8800 Series.

11.6

HLog Softkey support for SIP Phone was introduced.

4.1

Configurable softkey display for IP phones running SIP is
                                          					 supported for the Cisco Unified IP Phone 7911G, 7941G, 7941GE, 7961G, 7961GE,
                                          					 7970G, and 7971GE

4.0

An optional HLog softkey was added to the connected, idle, and seized call states.

The ability to customize softkey display in the hold call state was added. The ability to customize softkey display in the
                                                hold call state was added.

3.2

Configurable softkey display (the ability to customize softkey
                                          					 display in the alerting, connected, idle, and seized call states) was
                                          					 introduced.

| Note | If you configure softkeys personal-conf-user command under voice register template , personal user softkey template is enabled. If you do not configure any of the softkeys command under voice register template configuration mode, the default public user softkey template is enabled. |
|---|---|

| Note | If the # key is not pressed, each account code digit is processed
                                       		only after a timer expires. The timer is 30 seconds for the first digit
                                       		entered, then n seconds for each subsequent digit, where n equals the number of seconds configured with the timeouts interdigit (telephony-service) command. The default value for the interdigit timeout is 10 seconds. The
                                       		account code digits do not appear in the show command output until after being
                                       		processed. |
|---|---|

| Feature ID | Feature Name | Description | Default
                                          				  State on CME |
|---|---|---|---|
| 1 | ForwardAll | Forward all
                                          				  calls | Enabled |
| 2 | Park | Parks a call | Enabled |
| 3 | iDivert | Divert to
                                          				  Voicemail | Enabled |
| 4 | ConfList | Conference
                                          				  List | Disabled |
| 5 | SpeedDial | Abbreviated
                                          				  Dial | Disabled |
| 6 | Callback | Call back | Disabled |
| 7 | Redial | Redial a
                                          				  call | Enabled |
| 8 | Barge | Barge into a
                                          				  call | Enabled |

| Note | When button
                                       		layout is not specified, buttons are assigned to the phone lines in the
                                       		following order: line, speed-dial, blf-speed-dial, feature, and services URL
                                       		buttons. |
|---|---|

| Softkeys
                                             				  Supported as Programmable Line Keys (PLK) | 7914, 7915,
                                             				  7916 SCCP Phones | 7931 Phone | 6900 Series
                                             				  SCCP Phones | 7942, 7962,
                                             				  7965, 7975 SIP Phones | 8961, 9951,
                                             				  and 9971 SIP Phones |
|---|---|---|---|---|---|
| Acct | Supported | Supported | Supported | Not
                                             				  Supported | Not
                                             				  Supported |
| Call Back | Supported | Supported | Supported | Not
                                             				  Supported | Not
                                             				  Supported |
| Conference | Supported | Supported | Not
                                             				  Supported 1 | Supported | Not
                                             				  Supported |
| Conference
                                             				  List | Supported | Supported | Supported | Not
                                             				  Supported | Not
                                             				  Supported |
| Customized
                                             				  URL | Supported | Supported | Supported | Supported | Not
                                             				  Supported |
| Do Not
                                             				  Disturb | Supported | Supported | Supported | Supported | Supported |
| End Call | Supported | Supported | Supported | Supported | Not
                                             				  Supported |
| Extension
                                             				  Mobility | Supported | Supported | Supported | Not
                                             				  Supported | Not
                                             				  Supported |
| Forward
                                             				  All | Supported | Supported | Supported | Supported | Not
                                             				  Supported |
| GPickUp | Supported | Supported | Supported | Supported | Supported |
| Hold | Supported | Not
                                             				  Supported 1 | Not
                                             				  Supported 1 | Supported | Not
                                             				  Supported |
| Hook Flash | Supported | Supported | Supported | Not
                                             				  Supported | Not
                                             				  Supported |
| Hunt Group | Supported | Supported | Supported | Not
                                             				  Supported | Not
                                             				  Supported |
| Live
                                             				  Record | Supported | Supported | Supported | Not
                                             				  Supported | Not
                                             				  Supported |
| Login | Supported | Supported | Supported | Not
                                             				  Supported | Not
                                             				  Supported |
| Meet Me | Supported | Supported | Supported | Not
                                             				  Supported | Not
                                             				  Supported |
| Mobility | Supported | Supported | Supported | Not
                                             				  Supported | Not
                                             				  Supported |
| MyPhoneApps | Supported | Supported | Supported | Not
                                             				  Supported | Not
                                             				  Supported |
| New Call | Supported | Supported | Supported | Supported | Not
                                             				  Supported |
| Night
                                             				  Service | Supported | Supported | Supported | Not
                                             				  Supported | Not
                                             				  Supported |
| Park | Supported | Supported | Supported | Supported | Supported |
| Personal
                                             				  Speed Dial | Not
                                             				  Supported | Not
                                             				  Supported | Not
                                             				  Supported | Not
                                             				  Supported | Not
                                             				  Supported |
| PickUp | Supported | Supported | Supported | Supported | Supported |
| Privacy | Supported | Supported | Supported | Supported | Supported |
| Redial | Supported | Not
                                             				  Supported 1 | Supported | Supported | Supported |
| Remove
                                             				  Last Participant | Supported | Supported | Supported | Not
                                             				  Supported | Not
                                             				  Supported |
| Reset
                                             				  Phone | Not
                                             				  Supported | Not
                                             				  Supported | Not
                                             				  Supported | Not
                                             				  Supported | Not
                                             				  Supported |
| Services
                                             				  URL | Not
                                             				  Supported 1 | Not
                                             				  Supported 2 | Not
                                             				  Supported 3 | Not
                                             				  Supported | Not
                                             				  Supported |
| Speed Dial
                                             				  Buttons | Not
                                             				  Supported | Not
                                             				  Supported | Not
                                             				  Supported | Not
                                             				  Supported | Not
                                             				  Supported |
| Single
                                             				  Number Reach | Supported | Supported | Supported | Not
                                             				  Supported | Not
                                             				  Supported |
| Transfer | Supported | Not
                                             				  Supported 1 | Not
                                             				  Supported 1 | Supported | Not
                                             				  Supported |
| Transfer
                                             				  to VM | Supported | Supported | Supported | Not
                                             				  Supported | Not
                                             				  Supported |

| Softkeys
                                             				  Supported as Programmable Line Keys | Cisco
                                             				  Unified 6945, 8941, and 8945 SCCP IP Phones |
|---|---|
| Acct | Supported |
| Call Back | Supported |
| Cancel
                                             				  Call Waiting | Supported |
| Conference
                                             				  List | Supported |
| Customized
                                             				  URL | Supported |
| Do Not
                                             				  Disturb | Supported |
| End Call | Supported |
| Extension
                                             				  Mobility | Supported |
| Forward
                                             				  All | Supported |
| Group
                                             				  Pickup | Supported |
| Hook Flash | Supported |
| Hunt Group
                                             				  Login (HLog) | Supported |
| Live
                                             				  Record | Supported |
| Login | Supported |
| Meet Me | Supported |
| Mobility | Supported |
| My Phone
                                             				  Apps | Supported |
| New Call | Supported |
| Night
                                             				  Service | Supported |
| Park | Supported |
| Personal
                                             				  Speed Dial | Not
                                             				  Supported |
| Pickup | Supported |
| Privacy | Supported |
| Redial | Supported |
| Remove
                                             				  Last Participant | Supported |
| Reset
                                             				  Phone | Not
                                             				  Supported |
| Services
                                             				  URL | Not
                                             				  Supported |
| Speed Dial
                                             				  Buttons | Supported |
| Single
                                             				  Number Reach | Supported |
| Transfer
                                             				  to VM | Supported |

| Softkeys
                                             				  Supported as Programmable Line Keys | Cisco
                                             				  Unified 6911 SIP IP Phones | Cisco
                                             				  Unified 6921, 6941, 6945, and 6961 SIP IP Phones | Cisco
                                             				  Unified 8941 and 8945 SIP IP Phone |
|---|---|---|---|
| Acct | Not
                                             				  Supported | Not
                                             				  Supported | Not
                                             				  Supported |
| Call Back | Not
                                             				  Supported | Not
                                             				  Supported | Not
                                             				  Supported |
| Conference | Not
                                             				  Supported | Not
                                             				  Applicable 4 | Not
                                             				  Applicable 1 |
| Conference
                                             				  List | Not
                                             				  Supported | Supported | Supported |
| Customized
                                             				  URL | Not
                                             				  Supported | Supported | Not
                                             				  Supported |
| Do Not
                                             				  Disturb | Not
                                             				  Supported | Supported | Supported |
| End Call | Not
                                             				  Supported | Supported | Supported |
| Extension
                                             				  Mobility | Not
                                             				  Supported | Supported | Supported |
| Forward
                                             				  All | Supported | Supported | Supported |
| Group
                                             				  Pickup | Supported | Supported | Supported |
| Hold | Supported | Supported | Supported |
| Hook Flash | Not
                                             				  Supported | Not
                                             				  Supported | Not
                                             				  Supported |
| Hunt Group | Not
                                             				  Supported | Not
                                             				  Supported | Not
                                             				  Supported |
| Live
                                             				  Record | Not
                                             				  Supported | Not
                                             				  Supported | Not
                                             				  Supported |
| Login | Not
                                             				  Supported | Not
                                             				  Supported | Not
                                             				  Supported |
| Meet Me | Supported | Supported | Supported |
| Mobility | Not
                                             				  Supported | Supported | Supported |
| My Phone
                                             				  Apps | Not
                                             				  Supported | Supported | Supported |
| New Call | Not
                                             				  Supported | Supported | Supported |
| Night
                                             				  Service | Not
                                             				  Supported | Not
                                             				  Supported | Not
                                             				  Supported |
| Park | Not
                                             				  Supported | Supported | Supported |
| Personal
                                             				  Speed Dial | Not
                                             				  Supported | Not
                                             				  Supported | Not
                                             				  Supported |
| Pickup | Supported | Supported | Supported |
| Privacy | Supported | Supported | Supported |
| Redial | Supported | Supported | Supported |
| Remove
                                             				  Last Participant | Not
                                             				  Supported | Not
                                             				  Supported | Not
                                             				  Supported |
| Reset
                                             				  Phone | Not
                                             				  Supported | Not
                                             				  Supported | Not
                                             				  Supported |
| Services
                                             				  URL | Not
                                             				  Supported | Not
                                             				  Supported | Not
                                             				  Supported |
| Single
                                             				  Number Reach | Not
                                             				  Supported | Supported | Not
                                             				  Supported |
| Speed Dial | Supported | Supported | Supported |
| Transfer | Not
                                             				  Supported | Not
                                             				  Applicable 5 | Not
                                             				  Applicable 2 |
| Transfer
                                             				  to VM | Not
                                             				  Supported | Not
                                             				  Supported | Not
                                             				  Supported |

| Softkeys
                                             				  Supported as Programmable Line Keys | Cisco
                                             				  Unified 7800 Series SIP IP Phones | Cisco
                                             				  Unified 8800 Series SIP IP Phones |
|---|---|---|
| Acct | Not
                                             				  Supported | Not
                                             				  Supported |
| Call Back | Not
                                             				  Supported | Not
                                             				  Supported |
| Conference | Not
                                             				  Supported | Not
                                             				  Supported |
| Conference
                                             				  List | Supported | Supported |
| Customized
                                             				  URL | Not
                                             				  Supported | Not
                                             				  Supported |
| Do Not
                                             				  Disturb | Supported | Supported |
| End Call | Supported | Supported |
| Extension
                                             				  Mobility | Supported | Supported |
| Forward
                                             				  All | Supported | Supported |
| Group
                                             				  Pickup | Supported | Supported |
| Hold | Supported | Supported |
| Hook Flash | Not
                                             				  Supported | Not
                                             				  Supported |
| HLog (From
                                             				  Unified CME Release 11.6 onwards) | Supported | Supported |
| Live
                                             				  Record | Not
                                             				  Supported | Not
                                             				  Supported |
| Login | Not
                                             				  Supported | Not
                                             				  Supported |
| Meet Me | Supported | Supported |
| Mobility | Supported | Supported |
| My Phone
                                             				  Apps | Supported | Supported |
| New Call | Supported | Supported |
| Park | Supported | Supported |
| Personal
                                             				  Speed Dial | Not
                                             				  Supported | Not
                                             				  Supported |
| Pickup | Supported | Supported |
| Privacy | Supported | Supported |
| Redial | Supported | Supported |
| Remove
                                             				  Last Participant | Not
                                             				  Supported | Not
                                             				  Supported |
| Reset
                                             				  Phone | Not
                                             				  Supported | Not
                                             				  Supported |
| Services
                                             				  URL | Not
                                             				  Supported | Not
                                             				  Supported |
| Single
                                             				  Number Reach | Not
                                             				  Supported | Not
                                             				  Supported |
| Speed Dial | Supported | Supported |
| Transfer | Not
                                             				  Supported | Not
                                             				  Supported |
| Transfer
                                             				  to VM | Not
                                             				  Supported | Not
                                             				  Supported |

| Feature | Label/Tagged ID | Label/Extended Tagged ID | Icon | LED
                                             				  Behavior |
|---|---|---|---|---|
| Redial | Redial/SkRedialTag 0x01 | — | Default | — |
| Hold | Hold/SkHoldTag 0x03 | — | Hold | — |
| Transfer | Transfer/SkTrnsferTag 0x04 | — | Transfer | — |
| Forward
                                             				  All |  | Forward
                                             				  All/0x2D | Default | — |
| MeetMe | MeetMe/
                                             				  SkMeetMeConfrn Tag 0x10 | — | Default | — |
| Conference | Conference/SkConfrnTag 0x34 | — | Conference | — |
| Park | Park/SkParkTag 0x0E | — | Default | — |
| PickUp | PickUp/SkCallPickUpTag 0x11 | — | Default | — |
| GPickUp | — | Group
                                             				  PickUp/0x2F | Default | — |
| Mobility | — | Mobility/0x2B | Mobility | — |
| Do Not
                                             				  Disturb | — | Do Not
                                             				  Disturb/0x0f | Radio
                                             				  Button | On—active Off—inactive |
| Conference
                                             				  List | — | Conference
                                             				  List/0x34 | Default | — |
| Remove
                                             				  Last Participant | — | Remove
                                             				  Last Participant/0x30 | Default | — |
| CallBack | CallBack/SkCallBackTag 0x41 | — | Default | — |
| New Call | NewCall/SkNewCallTag 0x02 | — | Default | — |
| End Call | — | End
                                             				  Call/0x33 | Default | — |
| Cancel
                                             				  Call Waiting | CW Off | — | Default | — |
| HLog | — | Hunt
                                             				  Group/0x36 | Default | On—hlog in Off—hlog
                                             				  out Blink—call
                                             				  in queue at Hlogout state |
| Privacy | Private/
                                             				  SkPrivacy 0x36 | — | Radio
                                             				  Button | On—active Off—inactive |
| Acct | Acct/
                                             				  TAGS_ACCT_ 40 TAGS_Acct[] | — | Default | — |
| Flash | Flash/
                                             				  TAGS_FLASH_ 41 TAGS_Flash[] | — | Default | — |
| Login | Login/
                                             				  TAGS_LOGIN_ 42 TAGS_Login[] | — | Default | — |
| TrnsfVM | TrnsfVM/SkTrnsfVMTag 0x3e | — | Default | — |
| LiveRcd | LiveRcd | — | Default | — |
| Night
                                             				  Service | Night
                                             				  Service/ TAGS_Night_Service[] | — | Radio
                                             				  Button | On—active Off—inactive |
| Myphoneapp
                                             				  URL service | My Phone
                                             				  Apps | — | URL
                                             				  service | — |
| EM URL
                                             				  service | Extension
                                             				  Mobility | — | URL
                                             				  service | — |
| SN URL
                                             				  service | Single
                                             				  Number Reach | — | URL
                                             				  service | — |
| Customized URL | The
                                             				  configured name | — | URL
                                             				  service | — |

| Restriction | Enable the ConfList and MeetMe softkeys only if you have hardware conferencing configured. For information on conferencing,
                                                see Hardware Conference . The third softkey button on
                                                				the Cisco Unified IP Phone 7905G and Cisco Unified IP Phone 7912G is reserved
                                                				for the Message softkey. For these phones’ templates, the third softkey button
                                                				defaults to the Message softkey. For example, the softkeys idle Redial Dnd
                                                      					 Pickup Login Gpickup command configuration displays, in order,
                                                				the Redial, DND, Message, PickUp, Login, and GPickUp softkeys. The NewCall softkey cannot
                                                				be disabled on the Cisco Unified IP Phone 7905G or Cisco Unified IP Phone
                                                				7912G. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-template template-tag Example: Router(config)# ephone-template 15 | Enters
                                             				ephone-template configuration mode to create an ephone template. template-tag—Unique
                                                				  identifier for the ephone template that is being created. Range is 1 to 20. |
| Step 4 | softkeys alerting {[ Acct ] [ Callback ] [ Endcall ]} Example: Router(config-ephone-template)# softkeys alerting Callback Endcall | (Optional)
                                             				Configures an ephone template for softkey display during the alerting call
                                             				state. You can enter any of the
                                                				  keywords in any order. Default is all softkeys are
                                                				  displayed in alphabetical order. Any softkey that is not
                                                				  explicitly defined is disabled. |
| Step 5 | softkeys
                                                				  connected {[ Acct ] [ ConfList ] [ Confrn ] [ Endcall ] [ Flash ] [ Hlog ] [ Hold ] [ Join ] [ LiveRcd ] [ Park ] [ RmLstC ] [ Select ] [ TrnsfVM ] [Trnsfer]} Example: Router(config-ephone-template)# softkeys connected Endcall Hold Transfer Hlog | (Optional)
                                             				Configures an ephone template for softkey display during the call-connected
                                             				state. You can enter any of the
                                                				  keywords in any order. Default is all softkeys are
                                                				  displayed in alphabetical order. Any softkey that is not
                                                				  explicitly defined is disabled. |
| Step 6 | softkeys hold {[ Join ] [ Newcall ] [ Resume ] [ Select ]} Example: Router(config-ephone-template)# softkeys hold Resume | (Optional)
                                             				Configures an ephone template for softkey display during the call-hold state. You can enter any of the
                                                				  keywords in any order. Default is all softkeys
                                                				  are displayed in alphabetical order. Any softkey that is not
                                                				  explicitly defined is disabled. |
| Step 7 | softkeys
                                                				  idle {[ Cfwdall ]
                                          			 [ ConfList ]
                                          			 [ Dnd ]
                                          			 [ Gpickup ]
                                          			 [ Hlog ]
                                          			 [ Join ]
                                          			 [ Login ]
                                          			 [ Newcall ]
                                          			 [ Pickup ]
                                          			 [ Redial ]
                                          			 [ RmLstC ]} Example: Router(config-ephone-template)# softkeys idle Newcall Redial Pickup Cfwdall Hlog | (Optional)
                                             				Configures an ephone template for softkey display during the idle state. You can enter any of the
                                                				  keywords in any order. Default is all softkeys
                                                				  are displayed in alphabetical order. Any softkey that is not
                                                				  explicitly defined is disabled. |
| Step 8 | softkeys
                                                				  remote-in-use {[ CBarge ]
                                          			 [ Newcall ]} Example: Router(config-ephone-template)# softkeys remote-in-use CBarge Newcall | Modifies the
                                             				order and type of softkeys that display on an IP phone during the remote-in-use
                                             				call state. |
| Step 9 | softkeys
                                                				  ringing {[ Answer ]
                                          			 [ Dnd ]
                                          			 [ HLog ]} Example: Router(config-ephone-template)# softkeys ringing Answer Dnd Hlog | (Optional)
                                             				Configures an ephone template for softkey display during the ringing state. You can enter any of the
                                                				  keywords in any order. Default is all softkeys
                                                				  are displayed in alphabetical order. Any softkey that is not
                                                				  explicitly defined is disabled. |
| Step 10 | softkeys seized {[ CallBack ] [ Cfwdall ] [ Endcall ]
                                             				[ Gpickup ] [ Hlog ] [ MeetMe ] [ Pickup ]
                                             				[ Redial ]} Example: Router(config-ephone-template)# softkeys seized Endcall Redial Pickup Cfwdall Hlog | (Optional)
                                             				Configures an ephone template for softkey display during the seized state. You can enter any of the
                                                				  keywords in any order. Default is all softkeys
                                                				  are displayed in alphabetical order. Any softkey that is not
                                                				  explicitly defined is disabled. |
| Step 11 | exit Example: Router(config-ephone-template)# exit | Exits
                                             				ephone-template configuration mode. |
| Step 12 | ephone phone-tag Example: Router(config)# ephone 36 | Enters
                                             				ephone configuration mode. phone-tag—Unique sequence
                                                				  number that identifies this ephone during configuration tasks. |
| Step 13 | ephone-template template-tag Example: Router(config-ephone)# ephone-template 15 | Applies an
                                             				ephone template to the ephone that is being configured. |
| Step 14 | end Example: Router(config-ephone)# end | Returns to
                                             				privileged EXEC mode. |

| Restriction | This feature is supported
                                                   				only for Cisco Unified IP Phones 7911G, 7941G, 7941GE, 7961G, 7961GE, 7970G,
                                                   				and 7971GE. You can download a custom
                                                   				softkey XML file from a TFTP server. However, if the softkey XML file contains
                                                   				an error, the softkeys might not work properly on the phone. We recommend the
                                                   				following procedure for creating a softkey template in Cisco Unified CME. HLog
                                                      				  softkey is supported only on Cisco Unified IP Phones 7800 and 8800 series. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register template template-tag Example: Router(config)# voice register template 9 | Enters voice
                                             				register template configuration mode to create a SIP phone template. template-tag —Range: 1 to 10. |
| Step 4 | softkeys
                                                				  connected {[ Confrn ]
                                          			 [ Endcall ]
                                          			 [ Hold ] [ Trnsfer ] [ HLog ]
                                             				} Example: Router(config-register-template)# softkeys connected Endcall Hold Transfer HLog | (Optional)
                                             				Configures a SIP phone template for softkey display during the call-connected
                                             				state. You can enter the keywords
                                                				  in any order. Default is all softkeys are
                                                				  displayed in alphabetical order. Any softkey that is not
                                                				  explicitly defined is disabled. |
| Step 5 | softkeys hold {[ Newcall ] { Resume ]} Example: Router(config-register-template)# softkeys hold Resume | (Optional)
                                             				Configures a phone template for softkey display during the call-hold state. Default is that the NewCall
                                                				  and Resume softkeys are displayed in alphabetical order. Any softkey that is not
                                                				  explicitly defined is disabled. |
| Step 6 | softkeys idle {[ Cfwdall ]
                                          			 [ Newcall ]
                                          			 [ Redial ]
                                          			 [ HLog ] } Example: Router(config-register-template)# softkeys idle Newcall Redial Cfwdall HLog | (Optional)
                                             				Configures a phone template for softkey display during the idle state. You can enter the keywords
                                                				  in any order. Default is all softkeys are
                                                				  displayed in alphabetical order. Any softkey that is not
                                                				  explicitly defined is disabled. |
| Step 7 | softkeys
                                                				  seized {[ Cfwdall ] [ Endcall ] [ Redial ]} Example: Router(config-register-template)# softkeys seized Endcall Redial Cfwdall | (Optional)
                                             				Configures a phone template for softkey display during the seized state. You can enter the keywords
                                                				  in any order. Default is all softkeys are
                                                				  displayed in alphabetical order. Any softkey that is not
                                                				  explicitly defined is disabled. |
| Step 8 | softkeys
                                                				  personal-conf-user Example: Router(config-register-template)# softkeys personal-conf-user | (Optional)
                                             				Configures a personal user phone template for softkey display. The CLI command is
                                                				  disabled by default, and applies a public user phone template. When you configure the no
                                                				  form of this command, support switches to public user phone template. When the CLI command softkeys personal-conf-user is
                                                   					 configured, you cannot configure other state specific softkeys. The CLI command is
                                                				  supported only for the Cisco IP Conference Phone 7832 and Cisco IP Conference
                                                				  Phone 8832 phone types. |
| Step 9 | exit Example: Router(config-register-template)# exit | Exits voice
                                             				register template configuration mode. |
| Step 10 | voice register pool pool-tag Example: Router(config)# voice register pool 36 | Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone. |
| Step 11 | template template-tag Example: Router(config-register-pool)# template 9 | Applies a
                                             				SIP phone template to the phone you are configuring. template-tag — Template tag that was created with
                                                				  the voice register
                                                      						template command in Step 3 . |
| Step 12 | end Example: Router(config-register-pool)# end | Exits to
                                             				privileged EXEC mode. |

| Step 1 | show running-config Use this
                                             				command to verify your configuration. In the following example, the softkey
                                             				display is modified in phone template 7 and the template is applied to SIP
                                             				phone 2. All other phones use the default arrangement of softkeys. Example: Router# show running-config
!
voice register dn 1 dual-line
 ring feature secondary 
 number 126 secondary 1261 
 description Sales
 name Smith
 call-forward busy 500 secondary
 call-forward noan 500 timeout 10
 huntstop channel
 no huntstop
 no forward local-calls
!
!
voice register template 7
 session-transport tcp
 softkeys hold Resume Newcall
 softkeys idle Newcall Redial Cfwdall HLog
 softkeys connected Endcall Trnsfer Confrn Hold Hlog 
 voicemail 52001 timeout 30
.
.
.
voice register pool 2
 id mac 0030.94C2.A22A
 number 1 dn 4 
 template 7
 dialplan 3
! |
|---|---|
| Step 2 | show
                                                				  telephony-service ephone-template or show voice register
                                                				  template template-tag Example: These commands
                                             				display the contents of individual templates. Router# show telephony-service ephone-template
ephone-template 1
softkey ringing Answer Dnd
conference drop-mode never
conference add-mode all
conference admin: No
Always send media packets to this router: No
Preferred codec: g711ulaw
User Locale: US
Network Locale: US or Router# show voice register template 7
Temp Tag 7
Config:
 Attended Transfer is enabled
 Blind Transfer is enabled
 Semi-attended Transfer is enabled
 Conference is enabled
 Caller-ID block is disabled
 DnD control is enabled
 Anonymous call block is disabled
 Voicemail is 52001, timeout 30
 KPML is disabled
 Transport type is tcp
 softkey connected Endcall Trnsfer Confrn Hold HLog
 softkey hold Resume Newcall
 softkey idle Newcall Redial Cfwdall HLog |

| Restriction | The IP phone
                                             			 must support softkey display. |
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
| Step 4 | fxo hook-flash Example: Router(config-telephony)# fxo hook-flash | Enables the
                                             				Flash softkey on phones that support softkey display on PSTN calls using an FXO
                                             				port. Note The Flash
                                                      				softkey display is automatically disabled for local IP-phone-to-IP-phone calls. | Note | The Flash
                                                      				softkey display is automatically disabled for local IP-phone-to-IP-phone calls. |
| Note | The Flash
                                                      				softkey display is automatically disabled for local IP-phone-to-IP-phone calls. |
| Step 5 | restart all Example: Router(config-telephony)# restart all | Performs a
                                             				fast reboot of all phones associated with this Cisco Unified CME router. Does
                                             				not contact the DHCP or TFTP server for updated information. |
| Step 6 | end Example: Router(config-telephony)# end | Returns to
                                             				privileged EXEC mode. |

| Note | The Flash
                                                      				softkey display is automatically disabled for local IP-phone-to-IP-phone calls. |
|---|---|

| Step 1 | Use the show running-config command to display an entire configuration, including
                                          			 Flash softkey, which is listed in the telephony-service portion of the output. Example: Router# show running-config
telephony-service
 fxo hook-flash
 load 7960-7940 P00305000600
 load 7914 S00103020002
 max-ephones 100
 max-dn 500 |
|---|---|
| Step 2 | Use the show
                                                				  telephony-service command to show only the telephony-service
                                          			 portion of the configuration. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-template template-tag Example: Router(config)# ephone-template 1 | Enters
                                             				ephone-template configuration mode. template-tag —Unique sequence number that
                                                				  identifies this template during configuration tasks. Range is 1 to 20. |
| Step 4 | features blocked [ CFwdAll ] [ Confrn ] [ GpickUp ] [ Park ] [ PickUp ] [ Trnsfer ] Example: Router(config-ephone-template)# features blocked Park Trnsfer | Prevents the
                                             				specified softkey from invoking its feature. CFwdAll —Call forward all calls. Confrn —Conference. GpickUp —Group call pickup. Park —Call park. PickUp —Directed or local call pickup. This
                                                				  includes pickup last-parked call and pickup from another extension or park
                                                				  slot. Trnsfer —Call transfer. |
| Step 5 | exit Example: Router(config-ephone-template)# exit | Exits
                                          			 ephone-template configuration mode. |
| Step 6 | ephone phone-tag Example: Router(config)# ephone 25 | Enters ephone
                                             				configuration mode. phone-tag —Unique sequence number that identifies
                                                				  this ephone during configuration tasks. The maximum number of ephones for a
                                                				  particular Cisco Unified CME system is version- and platform-specific. For the
                                                				  range of values, see the CLI help. |
| Step 7 | ephone-template template-tag Example: Router(config-ephone)# ephone-template 1 | Applies an
                                             				ephone template to an ephone. template-tag —Template number that you want to
                                                				  apply to this ephone. Note To view
                                                      				your ephone-template configurations, use the show telephony-service
                                                            					 ephone-template command. | Note | To view
                                                      				your ephone-template configurations, use the show telephony-service
                                                            					 ephone-template command. |
| Note | To view
                                                      				your ephone-template configurations, use the show telephony-service
                                                            					 ephone-template command. |
| Step 8 | restart Example: Router(config-ephone)# restart | Performs a
                                             				fast reboot of this ephone. Does not contact the DHCP or TFTP server for
                                             				updated information. Note If you are
                                                      				applying the template to more than one ephone, you can use the restart all command in telephony-service configuration mode to reboot all the phones so
                                                      				they have the new template information. | Note | If you are
                                                      				applying the template to more than one ephone, you can use the restart all command in telephony-service configuration mode to reboot all the phones so
                                                      				they have the new template information. |
| Note | If you are
                                                      				applying the template to more than one ephone, you can use the restart all command in telephony-service configuration mode to reboot all the phones so
                                                      				they have the new template information. |
| Step 9 | Repeat Step 5 to Step 8 for each phone to
                                          			 which the template should be applied. | — |
| Step 10 | end Example: Router(config-ephone)# end | Returns to
                                             				privileged EXEC mode. |

| Note | To view
                                                      				your ephone-template configurations, use the show telephony-service
                                                            					 ephone-template command. |
|---|---|

| Note | If you are
                                                      				applying the template to more than one ephone, you can use the restart all command in telephony-service configuration mode to reboot all the phones so
                                                      				they have the new template information. |
|---|---|

| Step 1 | Use the show
                                                				  running-config command to display the running configuration,
                                          			 including ephone templates and ephone configurations. |
|---|---|
| Step 2 | Use the show telephony-service
                                                				  ephone-template command and the show telephony-service
                                                				  ephone command to display only the contents of ephone templates
                                          			 and the ephone configurations, respectively. |

| Note | When one
                                          		  participant in a conference (Meetme, Ad Hoc, cBarge, or Join) presses the
                                          		  iDivert softkey, all remaining participants receive an outgoing greeting of the
                                          		  participant who pressed iDivert softkey. |
|---|---|

| Restriction | iDivert feature is disabled
                                                   				when call-forward
                                                      				  all is activated for a phone. iDivert feature is not
                                                   				activated for the second call when call-forward
                                                      				  busy is activated for a phone and the phone is busy with the first call. If iDivert softkey is
                                                   				pressed before call forward no answer (CFNA) timeout, then the call is
                                                   				forwarded to voice mail. The calling and called
                                                   				parties can divert the call to their voice messaging mailboxes if both the
                                                   				parties press the iDivert softkey at the same time. The voice messaging mailbox
                                                   				of the calling party will receive a portion of the outgoing greeting of the
                                                   				called party. Similarly, the voice messaging mailbox of the called party will
                                                   				receive a portion of the outgoing greeting of the calling party. iDivert softkey is not
                                                   				supported when SIP phones fall back to SRST mode in Cisco Unified CME. iDivert after connect
                                                   				towards the voicemail with transcoding is not supported. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register template template-tag Example: Router(config)# voice register template 9 | Enters voice
                                             				register template configuration mode to create a SIP phone template. template-tag —Range: 1 to 10. |
| Step 4 | softkeys connected [Confrn] [Endcall] [Hold]
                                                				  [Trnsfer] [iDivert] Example: Router(config-register-template)# softkeys connected Endcall Hold Transfer iDivert | (Optional)
                                             				Configures a SIP phone template for softkey display during the call-connected
                                             				state. You can enter the keywords
                                                				  in any order. Default is all softkeys are
                                                				  displayed in alphabetical order. Any softkey that is not
                                                				  explicitly defined is disabled. |
| Step 5 | softkeys hold [Newcall] {Resume] [
                                                				  iDivert] Example: Router(config-register-template)# softkeys hold Newcall Resume | (Optional)
                                             				Configures a phone template for softkey display during the call-hold state. Default is that the NewCall
                                                				  and Resume softkeys are displayed in alphabetical order. Any softkey that is not
                                                				  explicitly defined is disabled. |
| Step 6 | softkeys ringing [Answer] [DND]
                                                				  [iDivert] Example: Router(config-register-temp)# softkeys ringin dnd answer idivert | Modifies the
                                             				order and type of softkeys that display on a SIP phone during the ringing call
                                             				state. |
| Step 7 | exit Example: Router(config-register-template)# exit | Exits voice
                                             				register template configuration mode. |
| Step 8 | voice register pool pool-tag Example: Router(config)# voice register pool 36 | Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone. |
| Step 9 | template template-tag Example: Router(config-register-pool)# template 9 | Applies a SIP
                                             				phone template to the phone you are configuring. template-tag — Template tag that was created with
                                                				  the voice register template command in Step 3 . |
| Step 10 | end Example: Router(config-register-pool)# end | Exits
                                             				configuration mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone template template-tag Example: Router(config)# ephone template 5 | Enters
                                             				ephone-template configuration mode to create an ephone template. template-tag —Unique identifier for the ephone
                                                				  template that is being created. Range: 1 to 10. |
| Step 4 | url-button index type \| url
                                          			 [name] Example: Router#(config-ephone-template)#url-button 1 myphoneapp Router(config-ephone-template)#url-button 2 em Router(config-ephone-template)#url-button 3 snr Router (config-ephone-template)#url-button 4 http://www.cisco.com | Configures a
                                             				service URL button on a line key. index —Unique index number. Range: 1 to 8. type —Type of service URL button. The following
                                                				  types of service URL buttons are available: myphoneapp: My phone application configured under phone
                                                         						  user interface. em: Extension Mobility. snr: Single Number Reach. url name —Service
                                                				  URL with maximum length of 31 characters. |
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
| Step 3 | voice register template template-tag Example: Router(config)# voice register template 5 | Enters voice
                                             				register template configuration mode to create a SIP phone template. template-tag —Unique identifier for the template
                                                				  that is being created. Range: 1 to 10. |
| Step 4 | url-button [ index number ]
                                          			 [ url location ]
                                          			 [ url name ] Example: Router(config-register-temp)url-button 1 http:// www.cisco.com | Configures a
                                             				service URL button on a line key. index number —Unique
                                                				  index number. Range: 1 to 8. url location —Location of the URL. url name —Service
                                                				  URL with maximum length of 31 characters. |
| Step 5 | exit Example: Router(config-register-temp)# exit | Exits voice
                                             				register template configuration mode. |
| Step 6 | voice register pool phone-tag Example: Router(config)# voice register pool 12 | Enters voice
                                             				register pool configuration mode. phone-tag —Unique number that identifies this voice
                                                				  register pool during configuration tasks. |
| Step 7 | template template-tag Example: Router(config-register-pool)# template 5 | Applies the
                                             				SIP phone template to the phone. template-tag —Unique identifier of the template
                                                				  that you created in Step 3. |
| Step 8 | end Example: Router(config-register-pool)# end | Returns to
                                             				privileged EXEC mode. |

| Restriction | Answer, Select, cBarge,
                                                				Join, and Resume features are not supported as PLKs. Feature buttons are only
                                                				supported on Cisco Unified IP Phones 6911, 7941, 7942, 7945, 7961, 7962, 7965.
                                                				7970, 7971, and 7975 with SCCP v12 or later versions. Any features available
                                                				through hard buttons are not provisioned. Use the show
                                                   				  ephone register detail command to verify why the features buttons are not
                                                				provisioned. Not all feature buttons are
                                                				supported on Cisco Unified IP Phone 6911 phone. Call Forward, Pickup, Group
                                                				Pickup, and MeetMe are the only feature buttons supported on the Cisco Unified
                                                				IP Phone 6911. The privacy-button command is available on Cisco Unified IP
                                                				phones running a SCCP Version 8 or later versions. The privacy-buttton command is overridden by any other available
                                                				feature buttons. Locales are not supported
                                                				on Cisco Unified IP Phone 7914. Locales are not supported
                                                				for Cancel Call Waiting or Live Recording feature buttons. The feature state for DnD,
                                                				Hlog, Privacy, Login, and Night Service feature buttons are indicated by an
                                                				LED. For a list of LED behavior for PLK, see Table 5 |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone template template-tag Example: Router(config)# ephone template 10 | Enters
                                             				ephone-template configuration mode to create an ephone template. template-tag -
                                                				  Unique identifier for the ephone template that is being created. Range: 1 to 10 |
| Step 4 | feature-button index <feature
                                                				  identifier> [ label < label >] Example: Router(config-ephone-template)feature-button 1 label hold | Configures a
                                             				feature button on a line key. index - Index number, one from 25 for a specific
                                                   					 feature type. feature identifier -Feature ID or stimulus ID. label -Non-default text label. |
| Step 5 | exit Example: Router(config-ephone-template)# exit | Exits
                                             				ephone-template configuration mode. |
| Step 6 | ephone phone-tag Example: Router(config)# ephone 5 | Enters ephone
                                             				configuration mode. phone-tag - Unique sequence number that identifies
                                                   					 this ephone during configuration tasks. |
| Step 7 | ephone-template template-tag Example: Router(config-ephone)# ephone-template 10 | Applies an
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
| Step 3 | voice register template template-tag Example: Router(config)# voice register template 5 | Enters voice
                                             				register template configuration mode to create a SIP phone template. template-tag -Unique identifier for the template
                                                   					 that is being created. Range: 1 to 10. Note Feature
                                                         				  button can be configured under voice register pool or voice register template
                                                         				  configuration mode. If both configurations are applied, the feature button
                                                         				  configuration under voice register pool takes precedence. | Note | Feature
                                                         				  button can be configured under voice register pool or voice register template
                                                         				  configuration mode. If both configurations are applied, the feature button
                                                         				  configuration under voice register pool takes precedence. |
| Note | Feature
                                                         				  button can be configured under voice register pool or voice register template
                                                         				  configuration mode. If both configurations are applied, the feature button
                                                         				  configuration under voice register pool takes precedence. |
| Step 4 | feature-button [ index ] [ feature identifier ] Example: Router(config-voice-register-template)feature-button 1 DnD Router(config-voice-register-template)feature-button
 2 EndCall Router(config-voice-register-template)feature-button 3 Cfwdall | Configures a
                                             				feature button on a line key. index —One of the 12 index numbers for a specific
                                                				  feature type. feature identifier —Unique identifier for a feature. One of the
                                                				  following feature or stimulus IDs: Redial, Hold, Trnsfer, Cfwdall, Privacy,
                                                				  MeetMe, Confrn, Park, Pickup. Gpickup, Mobility, Dnd, ConfList, RmLstC,
                                                				  CallBack, NewCall, EndCall, HLog, NiteSrv, Acct, Flash, Login, TrnsfVM, or
                                                				  LiveRcd. |
| Step 5 | exit Example: Router(config-register-temp)# exit | Exits voice
                                             				register template configuration mode. |
| Step 6 | voice register pool phone-tag Example: Router(config)# voice register pool 12 | Enters voice
                                             				register pool configuration mode. phone-tag —Unique number that identifies this voice
                                                				  register pool during configuration tasks. |
| Step 7 | template template-tag Example: Router(config-register-pool)# template 5 | Applies the
                                             				template to the phone. template-tag —Unique identifier of the template
                                                				  that you created in Step 3. |
| Step 8 | end Example: Router(config-register-pool)# end | Returns to
                                             				privileged EXEC mode. |

| Note | Feature
                                                         				  button can be configured under voice register pool or voice register template
                                                         				  configuration mode. If both configurations are applied, the feature button
                                                         				  configuration under voice register pool takes precedence. |
|---|---|

| Note | For more details
                                             			 on HLog functionality, see Call Coverage Features chapter. |
|---|---|

| Feature
                                          					 Name | Cisco Unified CME Version | Feature
                                          					 Information |
|---|---|---|
| Account
                                          					 Code Entry | 3.0 | Account
                                          					 code entry was introduced. |
| Barge
                                          					 Softkey | 4.3 | The
                                          					 Barge, LiveRcd, and TrnsfVM softkeys were added. |
| Conferencing Softkeys | 4.1 | The
                                          					 ConfList, Join, MeetMe, RmLstC, and Select softkeys were added. |
| Feature
                                          					 Blocking | 4.0 | Feature
                                          					 blocking was introduced. |
| Feature
                                          					 Policy Softkey Control | 8.5 | Allows
                                          					 control display of softkeys on the Cisco Unified SIP IP Phones 8961, 9951, and
                                          					 9971 using the feature policy template. |
| Flash
                                          					 Softkey | 3.0 | Flash
                                          					 softkey was introduced. |
| Immediate Divert Softkey for SIP Phones | 8.5 | Added
                                          					 support for iDivert softkey for SIP IP phones. |
| Programmable Line Keys | 8.5 | Allows
                                          					 you to configure a feature button or a URL button on a line key on both SIP and
                                          					 SCCP IP Phones. |
| Programmable Line Keys Enhancement | 8.8 | Adds
                                          					 support for softkeys as programmable line keys on Cisco Unified 6945, 8941, and
                                          					 8945 SCCP IP Phones. |
| Programmable Line Keys for Cisco Unified SIP IP Phones | 9.0 | Adds
                                          					 support for softkeys as programmable line keys on Cisco Unified 6911, 6921,
                                          					 6941, 6945, 6961, 8941, and 8945 SIP IP Phones. |
| Softkey
                                          					 Display | 12.3 | Support added for the softkeys 'Recents', 'Contacts', 'Apps',
                                          					 'Favorites', 'Messages', and 'Settings' on Cisco IP Conference Phones 7832 and
                                          					 8832. |
| 11.7 | Support added for the softkeys 'Details' on Cisco IP Phone
                                          					 7800 Series, and 'Show detail' on Cisco IP Phone 8800 Series. |
| 11.6 | HLog Softkey support for SIP Phone was introduced. |
| 4.1 | Configurable softkey display for IP phones running SIP is
                                          					 supported for the Cisco Unified IP Phone 7911G, 7941G, 7941GE, 7961G, 7961GE,
                                          					 7970G, and 7971GE |
| 4.0 | An optional HLog softkey was added to the connected, idle, and seized call states. The ability to customize softkey display in the hold call state was added. The ability to customize softkey display in the
                                                hold call state was added. |
| 3.2 | Configurable softkey display (the ability to customize softkey
                                          					 display in the alerting, connected, idle, and seized call states) was
                                          					 introduced. |