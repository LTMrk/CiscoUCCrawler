---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-7800-english-adminguide-administration-pa2d-b-7800-mpp-ag-11-pa2d-568a3938bc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/7800/english/adminguide/administration/pa2d_b_7800-mpp-ag-11/pa2d_b_7800-mpp-ag-11_chapter_01011.html
retrieved_at: 2026-09-01T15:41:33.602179+00:00
---

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

# Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

Updated: April 29, 2019

Chapter: Phone Features and Setup

## Chapter: Phone Features and Setup

# Phone Features and Setup

## Phone Features and Setup Overview

After you install
                           		Cisco IP Phones in your network, configure their network settings, and add them
                           		to Third-Party Call Control System, you must use the Third-Party Call Control System to configure telephony
                           		features, optionally modify phone templates, set up services, and assign users.

You can modify
                           		additional settings for the Cisco IP Phone from Third-Party Call Control Configuration Utility. Use this web-based application
                           to set up phone
                           		registration criteria and calling search spaces, to configure corporate
                           		directories and services, and to modify phone button templates, among other
                           		tasks.

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

List of features supported

User guide or quick reference for your voicemail system

## Telephony Features
                        	 for Cisco IP Phone

After you add
                              		  Cisco IP Phones to Third-Party Call Control system, you can add functionality
                              		  to the phones. The following table includes a list of supported telephony
                              		  features, many of which you can configure by using Third-Party Call Control
                              		  system.

The Third-Party Call Control system also provides several service parameters that you can
                                          			 use to configure various telephony functions.

AES 256 Encryption Support for Phones

Enhances security by supporting TLS 1.2 and new ciphers.

Alphanumeric Dialing

Allows users to place a call with alphanumeric characters. You can use these characters for alphanumeric dialing: a-z, A-Z,
                                          0-9, -, _, ., and +.

Any Call Pickup

Allows
                                          						users to pick up a call on any line in their call pickup group, regardless of
                                          						how the call was routed to the phone.

Audio Settings

Configures audio settings for the phone speaker, the handset, and the headsets that are connected to the phone.

Auto Answer

Connects incoming calls automatically after a ring or two.

Auto Answer works with either the speakerphone or the headset.

Blind Transfer

Blind Transfer: This transfer joins two established calls (call is in hold or in connected state) into one call and drops
                                          the feature initiator from the call. Blind Transfer does not initiate a consultation call and does not put the active call
                                          on hold.

Some JTAPI/TAPI applications are not compatible with the Join and Blind Transfer feature implementation on the Cisco IP Phone
                                          and you may need to configure the Join and Direct Transfer Policy to disable join and direct transfer on the same line or
                                          possibly across lines.

Busy Lamp Field (BLF)

Allows user to monitor call state of a directory number.

Busy
                                          						Lamp Field (BLF) Pickup

Allows user to pick up incoming calls to the directory number monitored through BLF.

Call Back

Provides users with an audio and visual alert on the phone when
                                          						a busy or unavailable party becomes available.

Call Display Restrictions

Determines the information that will display for calling or
                                          						connected lines, depending on the parties who are involved in the call. 
                                          					  RPID and PAID caller id handling are supported.

Call Forward

Allows
                                          						users to redirect incoming calls to another number. Call Forward options
                                          						include Call Forward All, Call Forward Busy, Call Forward No Answer.

Call Forward Notification

Allows
                                          						you to configure the information that the user sees when receiving a forwarded
                                          						call.

Call History for Shared Line

Allows you to view shared line activity in the phone Call History. This feature:

Logs missed calls for a shared line.

Logs all answered and placed calls for a shared line.

Call Park

Allows
                                          						users to park (temporarily store) a call and then retrieve the call by using
                                          						another phone.

Call Pickup

Allows
                                          						users to redirect a call that is ringing on another phone within their pickup
                                          						group to their phone.

You
                                          						can configure an audio and visual alert for the primary line on the phone. This
                                          						alert notifies the users that a call is ringing in their pickup group.

Call Waiting

Indicates (and allows users to answer) an incoming call that
                                          						rings while on another call. Incoming call information appears on the phone
                                          						display.

Caller ID

Caller
                                          						identification such as a phone number, name, or other descriptive text appear
                                          						on the phone display.

Caller ID Blocking

Allows
                                          						a user to block their phone number or name from phones that have caller
                                          						identification enabled.

Calling Party Normalization

Calling party normalization presents phone calls to the user
                                          						with a dialable phone number. Any escape codes are added to the number so that
                                          						the user can easily connect to the caller again. The dialable number is saved
                                          						in the call history and can be saved in the Personal Address Book.

Conference

Allows
                                          						a user to talk simultaneously with multiple parties by calling each participant
                                          						individually.

Allows a noninitiator in a standard (ad hoc) conference to add or remove participants; also allows any conference participant
                                          to join together two standard conferences on the same line.

Be
                                                      						  sure to inform your users whether these features are activated.

Configurable RTP/sRTP Port Range

Provides a configurable port range (2048 to 65535) for Real-Time Transport Protocol (RTP) and secure Real-Time Transport Protocol
                                          (sRTP).

The default RTP and sRTP port range is 16384 to 16538.

You configure the RTP and sRTP port range in the SIP Profile.

Directed Call Pickup

Allows a user to pick up a ringing call on a DN directly by pressing the GPickUp softkey and entering the directory number
                                          of the device that is ringing.

Divert

Allows
                                          						a user to transfer a ringing, connected, or held call directly to a
                                          						voice-messaging system. When a call is diverted, the line becomes available to
                                          						make or receive new calls.

Do Not Disturb (DND)

When
                                          						DND is turned on, either no audible rings occur during the ringing-in state of
                                          						a call, or no audible or visual notifications of any type occur.

DND and Call Forward Indication on Non-selected Line Key

Displays the DND and call forward icons next the to the line key label. The line key should be enabled with feature key sync.
                                          The line key should also be enabled with DND or call forward.

Emergency Calls

Enables users to make emergency calls. The emergency services receive the phone's location and a call-back number, to use
                                          when the emergency call unexpectedly disconnects.

Headset Sidetone Control

Allows an administrator to set the sidetone level of a wired headset.

Group Call Pickup

Allows
                                          						a user to answer a call that is ringing on a directory number in another group.

Hold Status

Enables phones with a shared line to distinguish between the
                                          						local and remote lines that placed a call on hold.

Hold/Resume

Allows
                                          						the user to move a connected call from an active state to a held state.

No configurations are required unless you want to use Music On Hold. See "Music On Hold" in this table.

See "Hold Reversion" in this table.

HTTP Download

Enhances the file download process to the phone to use HTTP by
                                          						default. If the HTTP download fails, the phone reverts to using the TFTP
                                          						download.

HTTPS for Phone Services

Increases security by requiring communication using HTTPS.

When the web is in HTTPS mode, the phone is an HTTPS server.

Improve Caller Name and Number Display

Improves the display of caller names and numbers. If the Caller Name is known, then the Caller Number is displayed instead
                                          of Unknown .

Jitter Buffer

The
                                          						Jitter Buffer feature handles jitter from 10 milliseconds (ms) to 1000 ms for
                                          						both audio and video streams.

Join
                                          						Across Lines

Allows
                                          						users to combine calls that are on multiple phone lines to create a conference
                                          						call.

Some
                                          						JTAPI/TAPI applications are not compatible with the Join and Direct Transfer
                                          						feature implementation on the Cisco IP Phone and you may need to configure the
                                          						Join and Direct Transfer Policy to disable join and direct transfer on the same
                                          						line or possibly across lines.

Join

Allows
                                          						users to combine two calls that are on one line to create a conference call and
                                          						remain on the call.

Message Waiting

Defines directory numbers for message waiting on and off
                                          						indicators. A directly-connected voice-message system uses the specified
                                          						directory number to set or to clear a message waiting indication for a
                                          						particular Cisco IP Phone.

Message Waiting Indicator

A light on the handset that indicates that a user has one or more new voice messages.

Minimum Ring Volume

Sets a
                                          						minimum ringer volume level for an IP phone.

Missed
                                          						Call Logging

Allows
                                          						a user to specify whether missed calls will be logged in the missed calls
                                          						directory for a given line appearance.

Multicasting Paging

Enables users to page some or all phones. If the phone is on an active call while a group page starts, the incoming page is
                                          ignored.

Multiple Calls Per Line Appearance

Each
                                          						line can support multiple calls. By default, the phone supports two active
                                          						calls per line, and a maximum of ten active calls per line. Only one call can
                                          						be connected at any time; other calls are automatically placed on hold.

The
                                          						system allows you to configure maximum calls/busy trigger not more than 10/6.
                                          						Any configuration more than 10/6 is not officially supported.

Music
                                          						On Hold

Plays music while callers are on hold.

Mute

Mutes the handset or headset microphone.

No
                                          						Alert Name

Makes
                                          						it easier for end users to identify transferred calls by displaying the
                                          						original caller’s phone number. The call appears as an Alert Call followed by
                                          						the caller’s telephone number.

Pause
                                          						in Speed Dial

Users
                                          						can set up the speed-dial feature to reach destinations that require Forced
                                          						Authorization Code (FAC) or Client Matter Code (CMC), dialing pauses, and
                                          						additional digits (such as a user extension, a meeting access code, or a
                                          						voicemail password) without manual intervention. When the user presses the
                                          						speed dial, the phone establishes the call to the specified DN and sends the
                                          						specified FAC, CMC, and DTMF digits to the destination and inserts the
                                          						necessary dialing pauses.

Peer Firmware Sharing (PFS)

Allows IP Phones located at remote sites to share the firmware files amongst them, which saves bandwidth when the upgrade
                                          process takes place. This feature uses Cisco Peer-to-Peer-Distribution Protocol (CPPDP) which is a Cisco proprietary protocol
                                          used to form a peer-to-peer hierarchy of devices. CPPDP is also used to copy firmware or other files from peer devices to
                                          the neighbouring devices.

PFS aids in firmware upgrades in branch/remote office deployment scenarios that run over bandwidth-limited WAN links.

Provides the following advantages over the traditional upgrade method:

Limits congestion on TFTP transfers to centralized remote TFTP servers

Eliminates the need to manually control firmware upgrades

Reduces phone downtime during upgrades when large numbers of devices are reset simultaneously

The more the number of IP phones, the better it's performance compared to the traditional firmware upgrade method.

Plus
                                          						Dialing

Allows
                                          						the user to dial E.164 numbers prefixed with a plus (+)  sign.

To
                                          						dial the + sign, the user needs to press and hold the star (*) key for at least
                                          						1 second. This applies to dialing the first digit for an on-hook (including
                                          						edit mode) or off-hook call.

Power
                                          						Negotiation over LLDP

Allows
                                          						the phone to negotiate power using Link Level Endpoint Discovery Protocol
                                          						(LLDP) and Cisco Discovery Protocol (CDP).

Problem Reporting Tool

Submits phone logs or reports problems to an administrator.

Programmable Feature Buttons

You can assign features, such as New Call, Call Back, and Forward All to line buttons.

Redial

Allows
                                          						users to call the most recently dialed phone number by pressing a button or the
                                          						Redial softkey.

Remote Customization (RC)

Allows a service provider to customize the phone remotely. There is no need for either the service provider to physically
                                          touch the phone or a user to configure the phone. The service provider can work with a sales engineer at the time of ordering
                                          to set this up.

Ringtone Setting

Identifies ring type used for a line when a phone has another
                                          						active call.

Reverse Name Lookup

Identifies the caller name using the incoming or outgoing call number. You must configure either the LDAP Directory or the
                                          XML directory. You can enable or disable the reverse name lookup using the phone administration web page.

RTCP
                                          						Hold For SIP

Ensures that held calls are not dropped by the gateway. The
                                          						gateway checks the status of the RTCP port to determine if a call is active or
                                          						not. By keeping the phone port open, the gateway will not end held calls.

Serviceability for SIP Endpoints

Enables administrators to quickly and easily gather debug information from
                                          						phones.

This
                                          						feature uses SSH to remotely access each IP phone. SSH must be enabled on each
                                          						phone for this feature to function.

Shared
                                          						Line

Allows
                                          						a user with multiple phones to share the same phone number or allows a user to
                                          						share a phone number with a coworker.

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

Show
                                          						Duration for Call History

Displays the time duration of placed and received calls in the Call History
                                          						details.

If the
                                          						duration is greater than or equal to one hour, the time is displayed in the
                                          						Hour, Minute, Second (HH:MM:SS) format.

If the
                                          						duration is less than one hour, the time is displayed in the Minute, Second
                                          						(MM:SS) format.

If the
                                          						duration is less than one minute, the time is displayed in the Second (SS)
                                          						format.

Silence Incoming Call

Allows you to silence an incoming call by pressing Ignore softkey or by pressing the volume button down.

Speed
                                          						Dial

Dials
                                          						a specified number that has been previously stored.

Time
                                          						Zone Update

Updates the Cisco IP Phone with time zone changes.

Transfer

Allows
                                          						users to redirect connected calls from their phones to another number.

Some
                                          						JTAPI/TAPI applications are not compatible with the Join and Direct Transfer
                                          						feature implementation on the Cisco IP Phone and you may need to configure the
                                          						Join and Direct Transfer Policy to disable join and direct transfer on the same
                                          						line or possibly across lines.

Voice Message System

Enables callers to leave messages if calls are unanswered.

Web Access Enable   by Default

Web services are enabled by default.

XSI call logs display

Allows you to configure a phone to display recent call logs from either the BroadWorks server or the local phone. After you
                                          enable the feature, the Recents screen has a Display recents from menu and the user can choose the XSI call logs or the local call logs.

## Feature Buttons and Softkeys

The following table provides information about features that are available on softkeys, features that are available on dedicated
                              feature buttons, and features that you need to configure as programmable feature buttons. An "X" in the table indicates that the feature is supported for the corresponding button type or softkey. Of the two button types
                              and softkeys, only programmable feature buttons require configuration in Cisco IP Phone administration.

The Cisco IP Phone 7811 does not have programmable feature buttons.

Feature Name

Dedicated Feature Button

Programmable Feature Button

Softkey

Answer

X

X

Call Forward All

X

X

Call Park

X

X

Call Park Line Status

X

Call Pickup (Pick Up)

X

X

Call Pickup Line Status

X

Conference

X

X (only displayed during connected call conference scenario)

Divert

X

Do Not Disturb

X

X

Hold

X

X

Intercom

X

Mute

X

Redial

X

X

Speed Dial

X

X

Speed Dial Line Status

X

Transfer

X

X (only displayed during connected call transfer scenario)

## Enable Users to Configure Features on Line Keys

You can enable users to configure these features on line keys:

Speed dial

Busy Lamp Field (BLF) to monitor a coworker's line, with the following options:

Speed dial to the monitored line

Call pickup from the monitored line

Users can select any available line keys to configure features. They can also select a line key that is functioning as a speed-dial
                              key or as a BLF key. The user's configuration will override any existing configuration for the line key. Users cannot select
                              line keys on which you have configured other features. If a user selects a BLF list key, the phone adjusts the positions of
                              the BLF list keys using the next available line keys.

For the BLF feature options, the phone subscribes to the BLF list URI that you specify (XML parameter BLF_List_URI ), to be notified of changes in the status of the monitored lines. If you do not specify a BLF list URI, the phone subscribes
                              to $USER@$PROXY .

On the phone administration web page, go to Admin Login > Advanced , Voice tab.

To allow features, go to Att Console > General , and configure Customizable PLK Options as described in General .

To enable feature configuration on a line key on the phone, do one of the following:

Go to Voice > Phone .

Set Extension to Disabled in the corresponding Line Key number section.

Go to Voice .

Go to the corresponding Ext number tab.

In the General section, set Line Enable to No .

## Enable Users to Configure Features on Line Keys

You can enable users to configure these features on line keys:

Speed dial

Busy Lamp Field (BLF) to monitor a coworker's line, with the following options:

Speed dial to the monitored line

Call pickup from the monitored line

Users can select any available line keys to configure features. They can also select a line key that is functioning as a speed-dial
                              key or as a BLF key. The user's configuration will override any existing configuration for the line key. Users cannot select
                              line keys on which you have configured other features. If a user selects a BLF list key, the phone adjusts the positions of
                              the BLF list keys using the next available line keys.

For the BLF feature options, the phone subscribes to the BLF list URI that you specify (XML parameter BLF_List_URI ), to be notified of changes in the status of the monitored lines. If you do not specify a BLF list URI, the phone subscribes
                              to $USER@$PROXY .

On the phone administration web page, go to Admin Login > Advanced , Voice tab.

To allow features, go to Att Console > General , and configure Customizable PLK Options as described in General .

To enable feature configuration on a line key on the phone, do one of the following:

Go to Voice > Phone .

Set Extension to Disabled in the corresponding Line Key number section.

Go to Voice .

Go to the corresponding Ext number tab.

In the General section, set Line Enable to No .

## Configure a Speed
                        	 Dial on a Line Key

You can configure
                              		  speed dial on an idle line of a user phone. The user can then use that line key
                              		  to speed-dial a number. When you enable the speed dial on the line key, the
                              		  user sees the speed-dial icon a name for the speed dial line key. The user
                              		  presses the line key to dial the assigned extension.

### Before you begin

Access the phone
                              		  administration web page. See Access the Phone Web Page .

Select Voice > Phone .

Select a Line
                                       			 Key on which to configure speed-dial.

From the
                                       			 Extension pulldown menu, select Disabled to disable the extension.

In the Extended Function field, enter a string in this
                                       			 format:

fnc=sd;ext=9999@$PROXY;nme=xxxx

If
                                          				you configure a phone with alphanumeric dialing feature in which the phone can
                                          				place a call with alphanumeric characters instead of the traditional digits,
                                          				you can enter a string in this format:

fnc=sd;ext=xxxx.yyyy@$PROXY;vid=n;nme=xxxx

where:

- fnc= sd means
                                                				  function=speed dial

ext=
                                                   					 9999 is the phone that the line key calls. Replace 9999 with appropriate phone
                                                   					 number.

ext=
                                                   					 xxxx.yyyy is the phone that the line key calls. Replace xxxx.yyyy with
                                                   					 alphanumeric characters. You can use these characters for alphanumeric dialing:
                                                   					 a-z, A-Z, 0-9, -, _, ., and +.

vid=n is
                                                   					 the line index of the phone.

- nme= XXXX is the name
                                                				  displayed on the phone for the speed-dial line key. Replace XXXX with a name.

You can also
                                          				configure XML service with line key. Enter a string in this format:

fnc=xml;url=http://xml.service.url;nme=name

Click Submit
                                          				All Changes .

## Configure a Speed
                        	 Dial with the Configuration Utility Page

You can configure
                              		  speed dials on the phone with the web interface.

### Before you begin

Access the phone
                              		  administration web page. See Access the Phone Web Page .

Select Voice > User .

In the Speed
                                          				Dial section, enter a name and number that corresponds to the speed
                                       			 dial entry.

Click Submit
                                          				All Changes .

## Speed Dial

Parameter

Description

Speed Dial Name

Indicates the name given to the speed dial.

Speed Dial Number

Indicates the number allocated to the speed dial.

## Enable Conference
                        	 Button with a Star Code

### Before you begin

The phone server must suppport this feature.

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Ext(n) , where n is an extension
                                       			 number.

In the Call
                                          				Features Settings section, select Yes for the Conference Single Hardkey field, enter a star code
                                       			 in the Conference Bridge URL , and press Submit All Changes . For example, you can enter *55
                                       			 to represent the conference bridge URL of a telecom service provider.

You can also
                                          				enable the conference button with a xml file. Enter a string in this format:

```
<Conference_Bridge_URL_1_ ua="na">*55</Conference_Bridge_URL_1_>
```

```
<Conference_Single_Hardkey_1_ ua="na">Yes</Conference_Single_Hardkey_1_>
```

## Set up Extra Line
                        	 Keys

On the
                                       			 Configuration Utility page, click Admin
                                             				  Login > Voice > Phone .

Choose a line
                                       			 key and select an extension to enable it.

Click Submit
                                          				All Changes .

## Configure the Screen Saver with the Phone Web Page

You can configure a screen saver for the phone. When the phone is idle for a specified time, it enters screen saver mode.

Any button press returns the phone to normal mode.

### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

On the phone web page, select Voice > User .

The user can select User Login > Voice > User to add screen saver to the phone.

In the Screen section, set up the fields as described in the following table.

Parameter

Description

Screen Saver Enable

Select Yes to enable a screen saver on the phone. When the phone is idle for a specified time, it enters screen saver mode.

Default: No

Screen Saver Type

Types of screen saver. Options you can choose:

Clock —Displays a digital clock on a plain background.

Download Picture —Displays a picture pushed from the phone webpage.

Logo : Displays a logo on the phone screen. Add a logo image in the Logo URL field.

Screen Saver Wait

Amount of idle time before screen saver displays.

Enter the number of seconds of idle time to elapse before the screen saver starts.

Default: 300

Picture Download URL

URL locating the (.png) file to display on the phone screen background.  If you select picture as as screensaver type, this
                                                      image displays as a screensaver on the phone screen.

When you enter an incorrect URL to download a new wallpaper, the phone fails to upgrade to the newer wallpaper and displays
                                                      the existing downloaded wallpaper. If the phone does not have any wallpaper downloaded earlier, it displays a gray screen.

Logo URL

Enter a URL or path for the location where the logo image is saved. If you select logo as as screensaver type, this image
                                                      displays as a screensaver on the phone screen.

Click Submit All Changes .

## Phone Configuration for Monitoring Other Phones

You can configure the phone to monitor the status of lines on other phones. This feature is useful if users routinely handle
                           calls for colleagues and need to see if they are available to answer calls. The phone monitors each line  on a separate line
                           key. The monitoring line keys function as Busy Lamp Field (BLF) keys. A BLF is an LED that changes color to indicate the status
                           of the monitored line:

LED Color

Meaning

Green

The monitored line is available.

Red

The monitored line is busy.

Blinking red

The monitored line is ringing.

Amber

Error in BLF key configuration.

If the phone is registered to a BroadSoft server, you can set up the phone to monitor multiple users, with a single set of
                           configurations.

### Configure the Phone to Monitor Multiple Users' Lines

#### Before you begin

Make sure that the phone is registered to a BroadSoft server.

You set up a BLF list for a user of the phone on the BroadSoft server.

On the phone administration web page, go to Admin Login > Advanced , Voice > Att Console > General .

Configure BLF List URI , BLF List , and Use Line Keys For BLF List as described in General .

Click Submit All Changes .

## Phone Configuration for Monitoring Other Phones

You can configure the phone to monitor the status of lines on other phones. This feature is useful if users routinely handle
                           calls for colleagues and need to see if they are available to answer calls. The phone monitors each line  on a separate line
                           key. The monitoring line keys function as Busy Lamp Field (BLF) keys. A BLF is an LED that changes color to indicate the status
                           of the monitored line:

LED Color

Meaning

Green

The monitored line is available.

Red

The monitored line is busy.

Blinking red

The monitored line is ringing.

Amber

Error in BLF key configuration.

If the phone is registered to a BroadSoft server, you can set up the phone to monitor multiple users, with a single set of
                           configurations.

### Configure the Phone to Monitor Multiple Users' Lines

#### Before you begin

Make sure that the phone is registered to a BroadSoft server.

You set up a BLF list for a user of the phone on the BroadSoft server.

On the phone administration web page, go to Admin Login > Advanced , Voice > Att Console > General .

Configure BLF List URI , BLF List , and Use Line Keys For BLF List as described in General .

Click Submit All Changes .

### Configure a Line Key on the Phone to Monitor a Single User's Line

You can configure
                                 		  busy lamp field on a phone line when a user needs to monitor a coworker's
                                 		  availability to handle calls.

You can
                                 		  configure the busy lamp field to work with any combination of speed dial or
                                 		  call pickup. For example, busy lamp field alone, busy lamp field and speed
                                 		  dial, busy lamp field and call pickup, or busy lamp field, speed dial, and call
                                 		  pickup can all be configured to work together. But speed dial alone requires a
                                 		  different configuration.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Phone .

Select a line
                                          			 key on which to configure a busy lamp field.

Select Disabled to disable the extension.

In the Extended Function field, enter a string in this
                                          			 format:

fnc=blf;sub=xxxx@$PROXY;usr=yyyy@$PROXY

fnc=blf;sub=xxxx@$PROXY;ext=yyyy@$PROXY

Where:

fnc=blf means function=busy lamp field

sub=the URI to which the SUBSCRIBE message should be sent. For a BroadSoft server, this name must be identical to the name
                                                   defined in the List URI: sip: parameter. xxxx is the name that is defined in List URI: sip : parameter. Replace xxxx with the exact defined name. $PROXY is the server. Replace $PROXY with the server address or name.

usr/ext=the user that the busy lamp field monitors. yyyy is user id of the phone that the busy lamp field monitors. Replace
                                                   yyyy with the exact user id of the monitored phone. $PROXY is the server. Replace $PROXY with the server address or name.

(Optional) You can
                                          			 configure the busy lamp field to work with any combination of speed dial or
                                          			 call pickup. To enable the busy lamp field to work with speed dial or call
                                          			 pickup, enter a string in the following format in the Extended Function field:

fnc=blf+sd+cp;sub=xxxx@$PROXY;usr=yyyy@$PROXY .

Where:

sd= speed dial

cp= call
                                             				pickup

Click Submit
                                             				All Changes .

## Configure Busy Lamp Field with Other Features

You can
                              		  configure busy lamp field to work with other features on your key expansion
                              		  module, such as speed dial, and call pickup. Use the information in the
                              		  following table as a guide when selecting the correct string format.

### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Att Console .

Select a key
                                       			 expansion module line key.

Enter a
                                       			 string in the appropriate format.

Feature

Busy Lamp Field and Speed Dial

fnc=blf+sd;sub=xxx@proxy;ext=monitored userID@proxy .

Busy Lamp Field, Speed Dial, and Call Pickup

fnc=blf+sd+cp;sub=xxx@proxy;ext=monitored userID@proxy .

Busy Lamp Field, Speed Dial, and Park Notification

fnc=blf+sd;sub=xxx@proxy;ext=monitored userID@proxy .

This combination cannot be configured using the extended
                                                      							 function. This combination is supported on Broadsoft servers only and it is
                                                      							 configured using the BLF List and related configuration on the server.

Busy Lamp Field, Speed Dial, Park Notification, and Call Pickup

fnc=blf+sd+cp;sub=xxx@proxy;ext=monitored userID@proxy .

This combination cannot be configured using the extended
                                                      							 function. This combination is supported on Broadsoft servers only and it is
                                                      							 configured using the BLF List and related configuration on the server.

Busy Lamp Field and Park Notification

fnc=blf;sub=xxx@proxy;ext=monitored userID@proxy .

This combination cannot be configured using the extended
                                                      							 function. This combination is supported on Broadsoft servers only and it is
                                                      							 configured using the BLF List and related configuration on the server.

Busy Lamp Field, Park Notification, and Call Pickup

fnc=blf+cp;sub=xxx@proxy;ext=monitored userID@proxy .

This combination cannot be configured using the extended
                                                      							 function. This combination is supported on Broadsoft servers only and it is
                                                      							 configured using the BLF List and related configuration on the server.

Busy Lamp Field and Call Pickup

fnc=blf+cp;sub=xxx@proxy;ext=monitored userID@proxy

Click Submit All Changes .

## Configure
                        	 Alphanumeric Dialing

You can
                              		  configure a phone so that the user of the phone can make a call by dialing
                              		  alphanumeric characters instead of dialing only digits. In the phone web page,
                              		  you can configure alphanumeric dialing with speed-dial, blf, and call pickup.

### Before you begin

Access the phone
                              		  administration web page. See Access the Phone Web Page .

Select Voice > Ext .

In the Enable URI Dialing 1 , select Yes to enable alphanumeric dialing.

In the phone
                                          				page, you can add a string on a line key in this format to enable speed dial
                                          				with alphanumeric dialing capability:

fnc=sd;ext=xxxx.yyyy@$PROXY;nme=yyyy,xxxx

For example:

The above
                                          				example will enable the user to dial "first.dial" to make a call.

The
                                                      				  supported characters that you can use for alphanumeric dialing are a-z, A-Z,
                                                      				  0-9, -, _, ., and +.

Click Submit All Changes .

## Configure a Paging
                        	 Group (Multicast Paging)

You can
                              		  configure multicast paging so that users can page all the phones at once or
                              		  page a group of phones without involving a server. On the Configuration Utility
                              		  page, you configure a phone as a part of a paging group and can subscribe them
                              		  to the same multicast address. This enables users to direct pages to specific
                              		  groups of phones. When you assign each paging group with a unique number, the
                              		  user dials the paging group number to start paging. All phones that are
                              		  subscribed to the same multicast address (also configured on the Configuration
                              		  Utility page) receive the page. The user hears a paging tone of three short
                              		  beeps when there is an incoming paging call.

Keep these things in mind:

Your network must support multicasting so that all devices in the same paging group are able to join the corresponding multicast
                                    group.

Paging groups must use even-numbered port numbers.

If the phone is on an active call when a group page starts, the incoming page is ignored.

Group paging is one way and uses the G711 codec. The paged phone can only listen to the call from the originator.

Incoming pages are ignored when DND is enabled.

When paging occurs, the speaker on the paged phones automatically powers on unless the handset or the headset is in use.

If the phone is on an active call when a group page starts, the incoming page is ignored. When the call ends, the page is
                                    answered, if the page is active.

When multiple pages occur, the pages are answered in chronological order. Until the active page ends, the next page is not
                                    answered.

### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Phone .

In the Multiple Paging Group Parameters section, enter a
                                       			 string in the Group Paging Script field in this format:

pggrp=multicast-address:port;[name=xxxx;]num=yyy;[listen={yes|no}]];

where:

multicast-address = Multicast IP address of the phone that
                                                					 listens for and receives pages.

port = Port on which to page; you must use different, even-number ports for each paging group.

Multicast paging doesn't work with odd-numbered ports.

name (optional) = xxxx is the name of the paging group. Replace xxxx with a name. The name can consist maximum of 64 characters.

num= yyy is a unique number that the user dials to access the paging group. Replace yyy with a number. The number can consist maximum of 64 characters and the allowed range is 1024 to 32767.

listen = Indicates whether the phone listens on the page group. Only the first two groups with listen set to yes listen to group pages. If the field is not defined, the default value is no , so you must set this field to listen to the group pages.

You can add more paging groups by appending to the configuration string. Here is an example of several paging groups.

```
pggrp=224.168.168.168:34560;name=All;num=500;listen=yes;
pggrp=224.168.168.168:34562;name=GroupA;num=501;listen=yes;
pggrp=224.168.168.168:34564;name=GroupB;num=502;
pggrp=224.168.168.168:34566;name=GroupC;num=503;
```

This example creates four paging groups: All , GroupA , GroupB , and GroupC . Users dial 500 to send pages to all phones, 501 to send pages to phones configured as part of the GroupA group, 502 to send pages to phones configured as part of the GroupB group, and 503 to send pages to phones configured as part of the GroupC group. The configured phone receives pages directed to the All and GroupA groups.

Click Submit All Changes .

## Add Priority Paging

You can set paging priority. You no longer need to register the phone to send or receive a page and this feature is known
                              as "Out of Band Paging" feature. You can configure maximum of five paging groups on the phone.

When a paging is initiated during an active call, your user sees an incoming page or outgoing page icons on the phone.

Priority has no impact during a regular page. Only when the phone receives a call during an active page, priority impacts
                              the active call. Following scenarios explain how priority of an active page impacts an active call:

PG_PRI_EMERGENT(Priority 0): If the phone receives a page with priority 0 during a call, the call will be put on hold. After
                                    the paging is complete, the call resumes.

PG_PRI_IMPRORTANT(Priority 1): If the phone receives a page with priority 1 during a call, the call and the page audio is
                                    mixed.

PG_PRI_NORMAL (Priority 2): If the device receives a page with priority 2 during a call, the phone does not display any incoming
                                    page icon on the phone screen and the user only hears a notification tone. Once the call ends and if the page is still active,
                                    the user sees the paging notification on the phone.

PG_PRI_MINOR (Priority 3): If the phone receives a page with priority 3 during a call, the page is ignored.

In the phone web page, select Admin Login > Advanced > Voice > Phone .

In the Multipaging Group Parameters section, enter a string in this format in the Group Paging Script field.

pggrp=multicast-address:port;[name=xxxx;]num=yyy;[listen={yes|no}]];pri=n

where:

multicast-address = Multicast IP address of the phone that listens for and receives pages.

port = Port on which to page; you must use different ports for each paging group.

name (optional) = xxxx is the name of the paging group. Replace xxxx with a name. The name can consist maximum of 64 characters.

num= yyy is a unique number that the user dials to access the paging group. Replace yyy with a number. The number can consist
                                                maximum of 64 characters and the allowed range is 1024 to 32767.

listen = Indicates whether the phone listens on the page group. Only the first two groups with listen set to yes listen to
                                                group pages. If the field is not defined, the default value is no, so you must set this field to listen to the group pages.

pri = n indicates the priority level of the paging. Priority level ranges from 0 to 4.

You can add more paging groups by appending to the configuration string and set the paging priority. Here is an example.

```
pggrp=224.168.168.168:34560;name=All;num=500;listen=yes;pri=0
pggrp=224.168.168.168:34562;name=GroupA;num=501;listen=yes;pri=1
pggrp=224.168.168.168:34564;name=GroupB;num=502;pri=2
pggrp=224.168.168.168:34566;name=GroupC;num=503;pri=3
```

This example creates four paging groups: All, GroupA, GroupB, and GroupC. Users dial 500 to send pages to all phones. If the
                                          phone receives a page on the “All” group during a call, the call will be put on hold.

User dials 501 to send pages to phones configured as part of the GroupA group. If the phone receives a page on the “GroupA”
                                          group during a call, the audio from page and call will be mixed.

User dials 502 to send pages to phones configured as part of the GroupB group. If the phone configured in GroupA receives
                                          a page during an active call, the paging UI will not show up on the device, and a notification tone will be played upon receiving
                                          the page. Once the active call ends, and if the page is still active, the paging UI will show up on the device.

User dials 503 to send pages to phones configured as part of the GroupC group. If the phone configured in GroupC receives
                                          a page during an active call, the page will be ignored.

Click Submit All Changes .

## Call Park

Green LED—Call park is successfully configured.

Amber LED—Call park is not configured.

Red slow blinking LED—A call is parked.

### Configure Call
                           	 Park with Star Codes

You can configure
                                 		  call park so that the user can put a call on hold and then retrieve the call
                                 		  from either the user's phone or another phone.

When configuring
                                 		  call park, the Call Park Code and the Call Unpark Code must match the Feature
                                 		  Access Code configured on the server.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Regional .

Enter *68 in the Call
                                             				Park Code field.

Enter *88 in the Call
                                             				Unpark Code field.

Click Submit
                                             				All Changes .

### Add Call Park to a
                           	 Programmable Line Key

You can add call
                                 		  park to a line key to enable the user to temporarily store and retrieve calls.
                                 		  Call park is supported on private lines and shared lines.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Phone .

Select a line
                                          			 key.

Select Disabled to disable the extension.

In the Extended Function field, enter a string in this
                                          			 format:

For a private line, enter fnc=prk;sub=$USER@$PROXY;nme=CallPark-Slot1 .

For a shared
                                             				line, enter fnc=prk;sub=$USER@$PROXY;nme=Call-Park1;orbit=<DN of primary
                                                				  line> .

where:

fnc= prk
                                                   					 means function=call park

sub=
                                                   					 999999 is the phone to which the call parks. Replace 999999 with a numbers.

nme= XXXX
                                                   					 is the name displayed on the phone for the call park line key. Replace XXXX
                                                   					 with a name.

Click Submit
                                             				All Changes .

## Configuring
                        	 Programmable Softkeys

You can customize
                              		  the softkeys displayed on the phone. The default softkeys (when the phone is in
                              		  an idle state) are Redial, Directory, Call Forward, and Do Not Disturb. Other
                              		  softkeys are available during specific call states (for example, if a call is
                              		  on hold, the Resume softkey displays).

### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Phone .

Under Programmable Softkeys , edit the softkeys depending
                                       			 on the call state that you want the softkey to display. For more information,
                                       			 see Programmable Softkeys .

In the
                                          				Programmable Softkeys section, each phone state is displayed and the softkeys
                                          				that are available to display during that state are listed. Each softkey is
                                          				separated by a semicolon. Softkeys are shown in the format:

```
softkeyname  |[  position  ]
```

where
                                          				softkeyname is the name of the key and position is where the key is displayed
                                          				on the IP phone screen. Positions are numbered, with position one displayed on
                                          				the lower left of the IP phone screen, followed by positions two through four.
                                          				Additional positions (over four) are accessed by pressing the right arrow key
                                          				on the phone. If no position is given for a softkey, the key will float and
                                          				appears in the first available empty position on the IP phone screen.

Click Submit
                                          				All Changes .

### Customize a
                           	 Programmable Softkey

The phone provides
                                 		  sixteen programmable softkeys (fields PSK1 through PSK16). You can define the
                                 		  fields by a speed-dial script.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Phone .

In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes .

Select a
                                          			 programmable softkey number field on which to configure a phone feature.

Enter the
                                          			 string for the programmable soft key. See the different types of programmable
                                          			 softkeys described in Configure Speed Dial on a Programmable Softkey .

Click Submit
                                             				All Changes .

### Configuring Toggling for Programmable SoftKeys

You can configure programmable Softkeys (PSKs) to toggle, or switch between two PSK actions when you want a user to be able
                                 to switch between two star code actions that is defined for a PSK. For example, to configure a call forwarding on or off PSK
                                 that displays on the far lower left of the IP phone screen when the phone is idle.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Phone .

In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes .

To configure a speed dial PSK, enter the following in the PSK number field:

fnc=sd;ext=starcode@$PROXY;nme=name;ext2=starcode@PROXY;nme2=name2

Where:

fnc= function of the key (speed dial)

extensionname=extension being dialed or the star code action to perform

nme= name of the first action

ext2= the second extension being dialed or the star code action to perform

nme2= name of the second action to perform

The name field displays on the softkey on the IP phone screen. We recommend a maximum of 10 characters for a phone. If more characters
                                                         are used, the label might be truncated on the phone screen.

Edit the following:

Idle Key List: Edit the field to add psk1|1 to the beginning of the string; for example:

psk1|1;em_login;acd_login;acd_logout;avail;unavail;

redial;dir;cfwd;dnd;lcr;pickup;gpickup;unpark;em_logout;

PSK1:

In this example, a PSK is configured to toggle between turning call forwarding on and off using the “call forwarding on”
                                                         star code (*72) and the “call forwarding off” star code (*73).

You can also configure an XML service on the programmable soft key. Enter the string in this format:

fnc=xml;url=http://xml.service.url;nme=name

Click Submit All Changes .

### Configure Speed
                           	 Dial on a Programmable Softkey

You can configure
                                 		  programmable softkeys as speed dials. The speed dials can be extensions or
                                 		  phone numbers. You can also configure programmable softkeys with speed dials
                                 		  that perform an action that a vertical service activation code (or a star [*]
                                 		  code) defines. For example, if you configure a programmable softkey with a
                                 		  speed dial for *67, the call is placed on hold.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Phone .

In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes .

To configure a
                                          			 speed dial PSK, enter the following in the PSK number field:

fnc=sd;ext=extensionname/starcode@$PROXY;vid=n;nme=name

Where:

fnc=
                                                   					 function of the key (speed dial)

extensionname=extension being dialed or the star code action to
                                                   					 perform

vid= n
                                                   					 is the extension that the speed dial will dial out

name is
                                                   					 the name of the speed dial being configured

The name field displays on the softkey on the IP phone
                                                         				  screen. We recommend a maximum of 10 characters for a phone. If more characters
                                                         				  are used, the label might be truncated on the phone screen.

Edit the
                                          			 following:

Idle Key List: Edit the field as described in the following example:

redial|1;newcall|2;dnd;psk1

If a
                                                            						  user enters rdeial;newcall;cfwd (redial has been misspelt), the
                                                            						  key list is not updated and the user does not see any change on the LCD.

If a
                                                            						  user enters redial;newcall;cfwd;delchar , the user will not see a
                                                            						  change on the LCD, as the delchar softkey is not allowed in the Idle Key
                                                               							 List . Hence, this is an incorrect configuration of the programmable
                                                            						  softkey list.

PSK1:

In this
                                                         				  example, we are configuring a softkey on a phone as a speed dial number for
                                                         				  extension 5014 (sktest1).

You can also
                                             				configure an XML service on the programmable soft key. Enter the string in this
                                             				format:

fnc=xml;url=http://xml.service.url;nme=name

Click Submit
                                             				All Changes .

### Programmable Softkeys

Keyword

Key Label

Definition

Available Phone Status

acd_login

Agt signin

Logs user in to Automatic Call Distribution (ACD).

Idle

acd_logout

AgtSignOut

Logs user out of ACD.

Idle

answer

Answer

Answers an incoming call.

Ringing

astate

Agt Status

Checks the ACD status.

Idle

avail

Avail

Denotes that a user who is logged in to an ACD server has set his status as available.

Idle

barge

Barge

Allows another user to interrupt a shared call.

Shared-Active, Shared-Held

bargesilent

BargeSilent

Allows another user to interrupt a shared call with the mic disabled.

Shared-Active

bxfer

BlindXfer

Performs a blind call transfer (transfers a call without speaking to the party to whom the call is transferred). Requires
                                             that Blind Xfer Serv is enabled.

Connected

call (or dial)

Call

Calls the selected item in a list.

Dialing Input

call info

Call Info

Show call information

Progressing

cancel

Cancel

Cancels a call (for example, when conferencing a call and the second party is not answering.

Off-Hook

cfwd

Forward / Clr fwd

Forwards all calls to a specified number.

Idle, Off-Hook, Shared-Active, Hold, Shared-Held

crdpause

PauseRec

Pause recording

Connected, Conferencing

crdresume

ResumeRec

Resume recording

Connected, Conferencing

crdstart

Record

Start a recording

Connected, Conferencing

crdstop

StopRec

Stop recording

Connected, Conferencing

conf

Conference

Initiates a conference call. Requires that Conf Server is enabled and there are two or more calls that are active or on hold.

Connected

confLx

Conf line

Conferences active lines on the phone. Requires that Conf Serv is enabled and there are two or more calls that are active
                                             or on hold.

Connected

delchar

delChar - backspace Icon

Deletes a character when entering text.

Dialing Input

dir

Dir

Provides access to phone directories.

Idle, Miss, Off-Hook (no input), Connected, Start-Xfer, Start-Conf, Conferencing, Hold, Ringing, Shared-Active, Shared-Held

disp_code

DispCode

Enter Disposition Code

Idle, Connected, Conferencing, Hold

dnd

DND / Clr Dnd

Sets Do Not Disturb to prevent calls from ringing the phone.

Idle, Off-Hook, Hold, Shared-Active, Shared-Held, Conferencing, Start-Conf, Start-Xfer

emergency

Emergency

Enter emergency number

Connected

em_login (or signin)

Sign in

Logs user in to Extension Mobility.

Idle

em_logout (or signout)

Sign out

Logs user out of Extension Mobility.

Idle

endcall

End call

Ends a call.

Connected, Start-Xfer, Start-Conf, Conferencing, Hold

favorites

Favorites

Provides access to "Speed Dials".

Idle, Miss, Off-Hook (no input), Connected, Start-Xfer, Start-Conf, Conferencing, Hold, Ringing, Shared-Active, Shared-Held

gpickup

GrPickup

Allows user to answer a call ringing on an extension by discovering the number of the ringing extension.

Idle, Off-Hook

hold

Hold

Put a call on Hold.

Connected, Start-Xfer, Start-Conf, Conferencing

ignore

Decline

Ignores an incoming call.

Ringing

ignoresilent

Ignore

Silences an incoming call

Ringing

join

Join

Connects a conference call. If the conference host is user A and users B & C are participants, when A presses "Join", A will
                                             drop off and users B & C will be connected.

Conferencing

lcr

Call Rtn/lcr

Returns the last missed call.

Idle, Missed-Call,Off-Hook (no input)

left

Left arrow icon

Moves the cursor to the left.

Dialing Input

messages

Messages

Provides access to voicemail.

Idle, Miss, Off-Hook (no input), Connected, Start-Xfer, Start-Conf, Conferencing, Hold, Ringing, Shared-Active, Shared-Held

miss

Miss

Displays the list of missed calls.

Missed-Call

newcall

New Call

Begins a new call.

Idle, Hold, Shared-Active, Shared-Held

option

Option

Opens a menu of input options.

Off-Hook

park

Park

Puts a call on hold at a designated "park" number.

Connected

phold

PrivHold

Puts a call on hold on an active shared line.

Connected

pickup

PickUp

Allows a user to answer a call ringing on another extension by entering the extension number.

Idle, Off-Hook

recents

Recents

Displays the All calls list from call history.

Idle, Off-Hook, Shared-Active, Shared-Held

redial

Redial

Displays the redial list.

Idle, Connected, Start-Conf, Start-Xfer, Off-Hook (no input), Hold

resume

Resume

Resumes a call that is on hold.

Hold, Shared-Held

right

Right arrow icon

Moves the cursor to the right.

Dialing (input)

settings

Settings

Provides access to "Information and Settings".

All

starcode

Input Star Code/*code

Displays a list of star codes that can be selected.

Off-Hook, Dialing (input)

trace

Trace

Trigger trace

Idle, Connected, Conferencing, Hold

unavail

Unavail

Denotes that a user who is logged in to an ACD server has set his status as unavailable.

Idle

unpark

Unpark

Resumes a parked call.

Idle, Off-Hook, Connected, Shared-Active

xfer

Transfer

Performs a call transfer. Requires that Attn Xfer Serv is enabled and there is at least one connected call and one idle call.

Connected, Start-Xfer, Start-Conf

xferlx

Xfer line

Transfers an active line on the phone to a called number. Requires that Attn Xfer Serv is enabled and there are two or more
                                             calls that are active or on hold.

Connected

## Configure
                        	 Provisioning Authority

You can set up
                              		  provisioning authority so that users can access their personalized phone
                              		  settings from other phones. For example, people who work different shifts or
                              		  who work at different desks during the week can share an extension, yet have
                              		  their own personalized settings.

The Sign
                                 			 in softkey appears on the phone when you enable provisioning
                              		  authority on the phone. Users enter their usernames and passwords to access
                              		  their personal phone settings. Users can also ignore the sign-in and use the
                              		  phone as a guest. After users sign in, they have access to their personal
                              		  directory numbers on the phone. When the user signs out, the phone reverts to a
                              		  basic profile with limited features.

### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Provisioning .

In the Configuration Profile section, set the Profile Rule field to the phone configuration file's
                                       			 URL.

### Example:

where,

MM– Cisco IP Phone MM Series with Multiplatform Firmware (68, 78, or 88)

MMxx– Cisco specific phone model (for example, 7841,7861, 8845, 8865 or 7832)

Select Admin
                                             				  Login > advanced > Voice > Phone .

Fill in the EM
                                          				Enable and EM
                                          				User Domain fields in the Extension Mobility section, based on the information
                                       			 provided in the phone configuration file.

Set the amount of time (in minutes) that the phone session will last for in the Session Timer(m) field. The phone signs out when the session times out.

Set the
                                       			 amount of time (in seconds) that the user has to cancel the sign-out in Countdown Timer(s) .

Choose input
                                       			 type of the password from the Preferred Password Input Mode field.

For information on
                                          				Extension Mobility fields, see Extension Mobility .

Your user
                                          				can also change the password input type from the phone.

(Optional) If the Programmable Softkey Enable field in the Programmable Softkeys section is set to Yes , add signin to Idle
                                          				Key List .

### Example:

Click Submit
                                          				All Changes .

### Configure
                           	 Provisioning Authority in the Phone Configuration File

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

In the phone
                                          			 configuration file, set the following parameters:

Set the
                                                				  Provisioning Authority profile rules in the Profile_Rule parameters.

#### Example:

```
<Profile_Rule ua="na">("$EMS" eq "mobile" and "$MUID" ne "" and "$MPWD" ne "")?[--uid $MUID$PDOM --pwd $MPWD] http://10.74.121.51:80/dms/CP-8851-3PCC/8851System.xml|http://10.74.121.51:80/dms/CP-8851-3PCC/8851System.xml</Profile_Rule>
```

Set the EM_Enable parameter to Yes .

#### Example:

```
<EM_Enable ua="na">Yes</EM_Enable>
```

Enter the
                                                				  enter the domain for the phone, or the authentication server in the EM_User_Domain parameter.

#### Example:

```
<EM_User_Domain ua="na">@10.74.121.51</EM_User_Domain>
```

Save the
                                          			 configuration file and upload it to your provisioning server.

Select Voice > Provisioning .

Enter the
                                          			 filepath to the configuration file in one of the Profile Rule fields.

#### Example:

Click Submit
                                             				All Changes .

## Enable Hoteling on
                        	 a Phone

Set
                              		  up the hotel feature on Broadworks and set the phone as a host or a guest.

Select Voice > Ext
                                             				  [n] (where [n] is the extension number).

In the Call
                                          				Feature Settings section, set Enable
                                          				Broadsoft Hoteling to Yes .

Set the amount
                                       			 of time (in seconds) that the user can be signed in as a guest on the phone in Hoteling Subscription Expires .

Click Submit
                                          				All Changes .

## Set the User
                        	 Password

Users can set
                              		  their own password on their phones, or you can set a password for them.

### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > System .

Set a password
                                       			 in the User
                                          				Password field.

Click Submit
                                          				All Changes .

## Download Problem
                        	 Reporting Tool Logs

Users
                              		  submit problem reports to you with the Problem Reporting Tool.

If you are working
                              		  with Cisco TAC to troubleshoot a problem, they typically require the logs from
                              		  the Problem Reporting Tool to help resolve the issue.

To issue
                              		  a problem report, users access the Problem Reporting Tool and provide the date
                              		  and time that the problem occurred, and a description of the problem. You need
                              		  to download the problem report from the Configuration Utility page.

### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Info > Debug
                                             				  Info > Device Logs .

In the Problem Reports area, click the problem report file
                                       			 to download.

Save the file
                                       			 to your local system and open the file to access the problem reporting logs.

## Configure PRT
                        	 Upload

You must use a
                              		  server with an upload script to receive the problem reports that the user sends
                              		  from the phone.

If the URL
                                    				specified in the PRT
                                       				  Upload Rule field is valid, users get a notification alert on the
                                    				phone UI saying that they have successfully submitted the problem report.

If the PRT
                                       				  Upload Rule field is empty or has an invalid URL, users get a
                                    				notification alert on the phone UI saying that the data upload failed.

The phone uses an
                              		  HTTP/HTTPS POST mechanism, with parameters similar to an HTTP form-based
                              		  upload. The following parameters are included in the upload (utilizing
                              		  multipart MIME encoding):

devicename
                                    				(example: "SEP001122334455")

serialno
                                    				(example: "FCH12345ABC")

username (The
                                    				user name is either the Station Display Name or the User
                                       				  ID of the extension. The Station Display Name is first considered. If this
                                    				field is empty, then the User
                                       				  ID is chosen.)

prt_file
                                    				(example: "probrep-20141021-162840.tar.gz")

You
                              		  can generate PRT automatically at specific intervals and can define the PRT
                              		  file name.

A sample script
                              		  is shown below. This script is provided for reference only. Cisco does not
                              		  provide support for the upload script installed on a customer's server.

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

### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Provisioning .

In the Problem Report Tool section, set the fields as
                                       			 described in the Problem Report Tool .

You can also
                                          				configure the parameters in the phone configuration file with XML(cfg.xml)
                                          				code. Enter the string in this format:

http://64.101.234.132:8000//Users/abcd/uploads/prt/test-prt.tar.gz

</PRT_Upload_Rule>

<PRT_Upload_Method
                                             				  ua="na">POST</PRT_Upload_Method>

<PRT_Max_Timer
                                             				  ua="na">20</PRT_Max_Timer>

Click Submit
                                          				All Changes .

## Configure a Phone
                        	 to Accept Pages Automatically

The Single Paging
                              		  or Intercom feature enables a user to directly contact another user by phone.
                              		  If the phone of the person being paged has been configured to accept pages
                              		  automatically, the phone does not ring. Instead, a direct connection between
                              		  the two phones is automatically established when paging is initiated.

### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > User .

In the Supplementary Services section, choose Yes for the Auto
                                          				Answer Page field.

Click Submit
                                          				All Changes .

## Server-Configured Paging

You can configure a paging group on a server so that users can page a group of phones. For more details, refer to your server
                           documentation.

## Manage Phones with
                        	 TR-069

You can use the protocols and standards defined in Technical Report 069 (TR-069) to manage phones. TR-069 explains the common
                              platform for management of all phones and other customer-premises equipment (CPE) in large-scale deployments. The platform
                              is independent of phone types and manufacturers.

As a bidirectional SOAP/HTTP-based protocol, TR-069 provides the communication between CPEs and Auto Configuration Servers
                              (ACS).

For TR-069 Enhancements, see TR-069 Parameter Comparison .

### Before you begin

Access the phone
                              		  administration web page. See Access the Phone Web Page .

Select Voice > TR-069 .

Set up the
                                       			 fields as described in TR-069 .

Click Submit All Changes .

## View TR-069 Status

### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Info > Status > TR-069 Status .

You can view status of TR-069 parameters in TR-069 .

## Enable Electronic Hookswitch

The Electronic Hookswitch feature enables users to use headsets that electronically connect a wireless headset to a phone.
                              Typically, the headset requires a base that plugs into the phone and communicates with the headset. Here are the supported
                              headsets:

Plantronics Savi 740

Jabra PRO920

Jabra PRO9400

Sennheiser DW Pro1

### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > User .

Set up the fields as described in Audio Volume .

Click Submit All Changes .

## Report All Phone
                        	 Issues from the Phone Web Page

If you are working
                              		  with Cisco TAC to troubleshoot a problem, they typically require the logs from
                              		  the Problem Reporting Tool to help resolve the issue. You can generate PRT logs
                              		  using the phone web page and upload them to a remote log server.

### Before you begin

Access the phone
                              		  administration web page. See Access the Phone Web Page .

Select Info > Debug
                                             				  Info .

In the Problem Reports section, click Generate PRT .

Enter the
                                       			 following information in the Report
                                          				Problem screen:

Enter the
                                             				  date that you experienced the problem in the Date field. The current date appears in this field
                                             				  by default.

Enter the
                                             				  time that you experienced the problem in the Time field. The current time appears in this field
                                             				  by default.

In the Select Problem drop-down list box, choose the
                                             				  description of the problem from the available options.

Click Submit in the Report
                                          				Problem screen.

The Submit
                                          				button is enabled only if you select a value in the Select Problem drop-down list box.

You get a
                                          				notification alert on the Phone Web page that indicates if the PRT upload was
                                          				successful or not.

## Report a Phone Problem Remotely

You can initiate a phone problem report remotely. The phone generates a problem report using the Cisco Problem Report Tool
                              (PRT), with the problem description "Remote PRT Trigger" . If you have configured an upload rule for problem reports, the phone uploads the problem report according to the upload
                              rule.

You can see the status of the problem report generation and upload on the phone administration web page. When a problem report
                              is successfully generated, you can download the problem report from the phone administration web page.

To initiate a phone problem report remotely, initiate a SIP-NOTIFY message from the server to the phone, with the Event specified as prt-gen .

## PRT Status

Parameter

Description

PRT Generation Status

The location of initiation and status of generation of the most recently initiated problem report.

Problem reports may be initiated from the phone LCD user interface, from the phone administration web page, or remotely. See Report All Phone Issues from the Phone Web Page and Report a Phone Problem Remotely for details.

XML tag in status.xml : PRT_Generation_Status

PRT Upload Status

The status of upload of the most recently initiated problem report.

See Configure PRT Upload for information on configuring an upload rule for problem reports.

XML tag in status.xml : PRT_Upload_Status

## Factory Reset the Phone with the Web UI Button

You can factory reset the phone from the phone web page. The reset only happens if the phone is idle. If the phone is not
                              idle, the phone web page shows a message that the phone is busy and that you need to try again.

### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Admin Login > advanced > Info > Debug Info .

In the Factory Reset section, click Factory Reset .

Click Confirm factory reset .

## Set up a Secure Extension

You can configure an extension to only accept secure calls. If the extension is configured to only accept secure calls then
                              any calls the extension makes will be secure.

You can also configure a secured extension with XML services. Enter a string in this format:

<Secure_Call_Serv ua="na">Yes</Secure_Call_Serv>

<Secure_Call_Option_1_ ua="na">Optional</Secure_Call_Option_1_>

### Before you begin

Make sure that Secure Call Serv is enabled (set to Yes ) in the Supplementary Services area on the Voice > Phone tab.

Make sure that SIP Transport parameter of the extension is set to TLS.

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Ext(n) .

In the Call Feature Settings section, in the Secure Call Option field, choose Optional to retain the current secure call option for the phone, or Required to reject nonsecure calls from other phones.

Click Submit All Changes .

## Capture Packets

### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Info > Debug Info .

In the Problem Report Tool section, click the Start Packet Capture button in the Packet Capture field.

Choose Al to capture all packets that the phone receives and select Host IP Address to capture packets only when source or destination is the IP address of the phone.

Make phone calls to and from the selected phone.

When you want to stop the packet capture, click Stop Packet Capture .

Click Submit .

## Emergency Calls

### Emergency Call Support Background

Emergency call service providers can register a phone's location for each IP-based phone in a company. The location information
                              server (LIS) transfers the emergency response location (ERL) to the phone. The phone stores its location during registration,
                              after the phone restarts, and when a person signs in to the phone. The location entry can specify the street address, building
                              number, floor, room, and other office location information.

When you place an emergency call, the phone transfers the location to the call server. The call server forwards the call and
                              the location to the emergency call service provider. The emergency call service provider forwards the call and a unique call-back
                              number (ELIN) to the emergency services. The emergency service or public safety answering point (PSAP) receives the phone
                              location. The PSAP also receives a number to call you back, if the call disconnects.

See Emergency Call Support Terminology for the terms used to describe emergency calls from the phone.

You insert the following parameters to obtain the phone's location for any phone extension number:

Company Identifier–A Unique number (UUID) assigned to your company by the NG9-1-1 service provider.

Primary Request URL–The HTTPS address of the primary server used to obtain the phone location.

Secondary Request URL–The HTTPS address of a secondary server (backup) used to obtain the phone location.

Emergency Number–A sequence of digits that identify an emergency call. You can specify multiple emergency numbers, by separating
                                    each emergency number with a comma.

Common emergency service numbers include:

North America–911

European countries–112

Hong Kong–999

The phone requests new location information for the following activities:

You register the phone with the call server.

A person restarts the phone and the phone was previously registered with the call server.

A guest signs in to the phone.

You change the network interface used in the SIP registration. For example, change Wi-Fi to Ethernet.

You change the IP address of the phone.

If all of the location servers do not send a location response, the phone re-sends the location request every two minutes.

### Emergency Call Support Terminology

The following terms describe emergency call support for the Cisco Multiplatform Phones.

Emergency Location ID Number (ELIN)–A number used to represent one or more phone extensions that locate the person who dialed
                                       emergency services.

Emergency Response Location (ERL)–A logical location that groups a set of phone extensions.

HTTP Enabled Location Delivery (HELD)–An encrypted protocol that obtains the PIDF-LO location for a phone from a location
                                       information server (LIS).

Location Information Server (LIS)–A server that responds to a SIP-based phone HELD request and provides the phone location
                                       using a HELD XML response.

Emergency Call Service Provider–The company that responds to a phone HELD request with the phone's location. When you make
                                       an emergency call (which carries the phone's location), a call server routes the call to this company The emergency call service
                                       provider adds an ELIN and routes the call to the emergency services (PSAP). If the call is disconnected, the PSAP uses the
                                       ELIN to reconnect with the phone used to make the emergency call.

Public Safety Answering Point (PSAP)–Any emergency service (for example, fire, police, or ambulance) joined to the Emergency
                                       Services IP Network.

Universally Unique Identifier (UUID)–A 128-bit number used to uniquely identify a company using emergency call support.

### Configure a Phone to Make Emergency Calls

#### Before you begin

Obtain the E911 Geolocation Configuration URLs and the company identifier for the phone from your emergency call services
                                       provider. You can use the same Geolocation URLs and company identifier for multiple phone extensions in the same office area.

Access the phone administration web page. See Access the Phone Web Page .

Click the Voice > Ext n , where n is the phone extension number (1-10) of the phone web dialog.

In the Dial Plan area, set the Emergency Number to the digits that correspond to the customer emergency service numbers.

To specify multiple emergency numbers, separate each emergency number with a comma.

In the E911 Geolocation Configuration area, set the Company UUID to the unique customer identifier obtained from your emergency call service provider.

For example:

07072db6-2dd5-4aa1-b2ff-6d588822dd46

Specify the encrypted Primary Request URL to the main georedundant server. This location information server returns the location for this phone.

For example:

https://prod.blueearth.com/e911Locate/held/held_request.action

Specify the encrypted Secondary Request URL for the backup server that can return location information.

For example:

https://prod2.blueearth.com/e911Locate/held/held_request.action

Click Submit All Changes .

## Configure the SIP Transport

For SIP messages, you can either specify the transport protocol of your choice, or, you can let the phone select the appropriate
                              protocol automatically, for each extension.

When you set up automatic selection, the phone determines the transport protocol based on the Name Authority Pointer (NAPTR)
                              records on the DNS server. The phone uses the protocol specified in the record that has the lowest order and preference. When
                              there are multiple records with the same order and preference, the phone looks for a protocol within the records, in the following
                              order of preference: 1. UDP, 2. TCP, and 3. TLS. The phone uses the first protocol that it finds, in that order of preference.

### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Ext(n) , where n is an extension number.

In the SIP Settings section, set the SIP Transport parameter as described in SIP Settings .

Click Submit All Changes .

## Block Non-Proxy SIP Messages to a Phone

You can disable the ability of the phone to receive incoming SIP messages from a non-proxy server. When you enable this feature,
                              the phone only accepts SIP messages from:

proxy server

outbound proxy server

alternative proxy server

alternative outbound proxy server

IN-Dialog message from proxy server and non-proxy server. For example: Call Session dialog and Subscribe dialog

### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > System .

In the System Configuration section, set the Block Nonproxy SIP field as described in the System Configuration .

Click Submit All Changes .

## Configure a Privacy Header

A user privacy header in the SIP message sets user privacy needs from the trusted network.

You can set the user privacy header value for each line extension using the phone web page.

The privacy header options are:

Disabled (default)

none—The user requests that a privacy service applies no privacy functions to this SIP message.

header—The user needs a privacy service to obscure headers which cannot be purged of identifying information.

session—The user requests that a privacy service provide anonymity for the sessions.

user—The user requests a privacy level only by intermediaries.

id—The user requests that the system substitute an id that doesn't reveal the IP address or host name.

### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Extension .

In the SIP Settings section, set the Privacy Header field as described in the SIP Settings .

Click Submit All Changes .

## Enable P-Early-Media Support

You can determine whether to include the P-Early-Media header in the SIP message of outgoing calls. The P-Early-Media header
                              contains the status of the early media stream. If the status indicates that the network is blocking the early media stream,
                              the phone plays the local ringback tone. Otherwise, the phone plays the early media while waiting for the call to be connected.

### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Ext (n) .

In the SIP Settings section, set the P-Early-Media Support field as described in SIP Settings .

Click Submit All Changes .

## Peer Firmware Sharing

Peer Firmware Sharing (PFS) is a firmware distribution model which allows a Cisco IP phone to find other phones of the same
                              model or series on the subnet and share updated firmware files when you need to upgrade multiple phones all at the same time.
                              PFS uses Cisco Peer-to-Peer-Distribution Protocol (CPPDP) which is a Cisco proprietary protocol. With CPPDP, all the devices
                              in the subnet form a peer-to-peer hierarchy, and then copy the firmware or the other files from peer devices to the neighboring
                              devices. To optimize firmware upgrades, a root phone downloads the firmware image from the load server and then transfers
                              the firmware to other phones on the subnet using TCP connections.

Peer firmware sharing:

Limits congestion on TFTP transfers to centralized remove load servers.

Eliminates the need to manually control firmware upgrades.

Reduces phone downtime during upgrades when large numbers of phones are reset simultaneously.

Peer firmware sharing does not function unless multiple phones are set to upgrade at the same time. When a NOTIFY is sent
                                                with Event:resync, it initiates a resync on the phone. Example of an xml that can contain the configurations to initiate the
                                                upgrade:

When you set the Peer Firmware Sharing Log server to an IP address and port, the PFS specific logs are sent to that server
                                                as UDP messages. This setting must be done on each phone. You can then use the log messages when troubleshooting issues related
                                                to PFS.

Peer_Firmware_Sharing_Log_Server specifies UDP Remote syslog server hostname and the port. The port defaults to the default
                              syslog 514.

For example:

```
<Peer_Firmware_Sharing_Log_Server>192.168.5.5</ Peer_Firmware_Sharing_Log_Server>
```

To use this feature, enable PFS on the phones.

### Enable Peer Firmware Sharing

You can enable Peer Firmware Sharing (PFS) when you want a phone to find other phones of the same model or series on the subnet
                                 and share updated firmware files. The phones are organized into a hierarchy and one of the phones in that hierarchy acts as
                                 a root phone. After the hierarchy formation, the root phone downloads the firmware image from the load server and then transfers
                                 the firmware to other phones in the hierarchy.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Provisioning .

In the Firmware Upgrade section, set the Peer Firmware Sharing and the Peer Firmware Sharing Log Server fields as described in Firmware Upgrade .

Click Submit All Changes .

## Profile Authentication

Profile Authentication allows phone users to resynchronize the provisioning profile onto the phone. Authentication information
                              is required while the phone tries to resynchronize and download configuration file for the first time and gets an HTTP or
                              HTTPS 401 authentication error. When you enable this feature, the Profile account setup screen is displayed on the phone for the following situations:

When the HTTP or HTTPs 401 authentication error occurs during first-time provisioning after the phone reboots

When the profile account username and password are empty

When there are no username and password in the Profile Rule

If  the Profile account setup screen is missed or ignored, the user can also access the setup screen through the phone screen menu, or the Setup softkey, which displays only when no line on the phone is registered.

When you disable the feature, the Profile account setup screen doesn't display on the phone.

The username and password in the Profile Rule field have a higher priority than the profile account.

When you provide a correct URL in the Profile Rule field without a username and password, the phone requires authentication or digest to resynchronize the profile. With the
                                    correct profile account, authentication passes. With an incorrect profile account, authentication fails.

When you provide a correct URL in the Profile Rule field with a correct username and password, the phone requires authentication or digest to resynchronize the profile. The
                                    profile account is not used for phone resynchronization. Sign-in is successful.

When you provide a correct URL in the Profile Rule field with an incorrect username and password, the phone requires authentication or digest to resynchronize the profile.
                                    The profile account isn't used for phone resynchronization. Sign-in always fails.

When you provide an incorrect URL in the Profile Rule field, sign-in always fails.

## Specify the Profile Authentication Type

You can specify the profile authentication type from the phone administration web page.

### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Provisioning .

In the Configuration Profile section, set the Profile Authentication Type field as described in the Configuration Profile .

Click Submit All Changes .

## Add Ignore Programmable Soft Key to Silence an Incoming Call

### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Phone .

In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes .

Enter the following values in the Ringing Key List field:

answer|1;ignore|2;ignoresilent|3;

Click Submit All Changes .

## Enable BroadWorks Anywhere

You can configure a phone to allow a call to seamlessly be moved from one desk phone(location) to another mobile phone or
                              desk phone(location).

When you enable this feature, the Anywhere menu is added into the phone screen. The user can use this menu to add multiple phones as locations to the extension. When
                              there is an incoming call in that extension, all the added phones will ring and the user can answer the incoming call from
                              any location. The locations list also gets saved to the BroadWorks XSI server.

### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Ext(n) .

In the XSI Line Service section, set the XSI Host Server , XSI Authentication Type , Login User ID , Login Password , and Anywhere Enable field as described in the XSI Line Service .

If you select SIP Credentials for XSI Authentication Type , you need to enter subsriber Auth ID and Password in the Subscriber Information section.

Click Submit All Changes .

## Sync the Block Caller ID Feature with the Phone and the BroadWords XSI Server

You can sync the Block caller id status on the phone and the Line ID Blocking status on the BroadWorks XSI server. When you enable the synchronization, the changes that the user makes in the Block caller id settings also changes the BroadWorks server settings.

### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Ext(n) .

In the XSI Line Service section, set the Block CID Enable field as described in the XSI Line Service .

Click Submit All Changes .

## Enable Viewing BroadWorks XSI Call Logs on a Line

You can configure a phone to display recent call logs from either the BroadWorks server or the local phone. After you enable
                              the feature, the Recents screen has a Display recents from menu and the user can choose the XSI call logs or the local call logs.

### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Phone .

In the XSI Phone Service section, set the XSI Host Server , XSI Authentication Type , Login User ID , Login Password , and Directory Enable fields as described in XSI Phone Service .

If you select SIP Credentials for XSI Authentication Type , you need to enter SIP Auth ID and SIP Password in this section.

Set the CallLog Associated Line and Display Recents From fields as described in XSI Phone Service .

The Display recents from menu doesn't appear in the Recents phone screen when you set the value of the CallLog Enable field to No ,

Click Submit All Changes .

## DND and Call Forwarding Status Sync

You can configure the settings on the phone administration web page to enable status synchronization of do not disturb (DND)
                              and call forwarding between the phone and the server.

There are two ways to synchronize the feature status:

Feature Key Synchronization (FKS)

XSI Synchronization

FKS uses SIP messages to communicate the feature status. XSI Synchronization uses HTTP messages. If both FKS and XSI synchronization
                              are enabled, FKS takes precedent over XSI synchronization. See the table below for how FKS interacts with XSI synchronization.

Feature Key Sync

DND Enabled

CFWD Enabled

DND Sync

CFWD Sync

Yes

Yes

Yes

Yes (SIP)

Yes (SIP)

Yes

No

No

Yes (SIP)

Yes (SIP)

Yes

No

Yes

Yes (SIP)

Yes (SIP)

Yes

No

No

Yes (SIP)

Yes (SIP)

No

Yes

Yes

Yes (HTTP)

Yes (HTTP)

No

No

Yes

No

Yes (HTTP)

No

Yes

No

Yes (HTTP)

No

No

No

No

No

No

If a line key is configured with FKS or XSI synchronization and is also enabled with DND or call forwarding, the respective
                              DND icon or the call forwarding icon is displayed next to the line key label. If the line key has a missed call, a voice message, or an urgent voicemail
                              alert, the DND icon or the call forwarding icon is also displayed with the alert notification.

### Enable Feature Key Sync

When you enable the Feature Key Synchronization (FKS), the settings of call forwarding and do not disturb (DND) on the server
                                 are synchronized to the phone. The changes in DND and call forwarding settings made on the phone will also be synchronized
                                 to the server.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Select Voice > Ext [n] (where [n] is the extension number).

In the Call Feature Settings section, set the Feature Key Sync field to Yes .

Click Submit All Changes .

### Enable Call Forwarding Status Sync via XSI Service

When call forwarding sync is enabled, the settings related to call forwarding on the server are synchronized to the phone.
                                 The changes in call forwarding settings made on the phone will also be synchronized to the server.

If XSI sync for call forwarding is enabled and the XSI host server or XSI account is not configured correctly, the phone user
                                             can't forward calls on the phone.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Configure the XSI host server and the corresponding credentials on the Voice > Ext (n) tab.

When using Login Credentials for XSI server authentication, enter XSI Host Server , Login User ID , and Login Password in the XSI Line Service section.

When using SIP Credentials for XSI server authentication, enter XSI Host Server and Login User ID in the XSI Line Service section, and Auth ID and Password in the Subscriber Information section.

Disable Feature Key Sync (FKS) in Call Feature Settings section from Voice > Ext (n) .

Select Voice > Ext [n] (where [n] is the extension number).

Set the CFWD Enable field to Yes .

Click Submit All Changes .

### Enable DND Status Sync via XSI Service

When do not disturb (DND) sync is enabled, the DND setting on the server is synchronized to the phone. The changes in DND
                                 setting made on the phone will also be synchronized to the server.

If XSI sync for DND is enabled and the XSI host server or XSI account is not configured correctly, the phone user can't turn
                                             on DND mode on the phone.

#### Before you begin

Access the phone administration web page. See Access the Phone Web Page .

Configure the XSI host server and the corresponding credentials on the Voice > Ext (n) tab.

When using Login Credentials for XSI server authentication, enter XSI Host Server , Login User ID , and Login Password in the XSI Line Service section.

When using SIP Credentials for XSI server authentication, enter XSI Host Server and Login User ID in the XSI Line Service section, and Auth ID and Password in the Subscriber Information section.

Disable Feature Key Synchronization (FKS) in Call Feature Settings section from Voice > Ext (n) .

Select Voice > Ext [n] (where [n] is the extension number).

Set the DND Enable field to Yes .

Click Submit All Changes .

| Note | The Third-Party Call Control system also provides several service parameters that you can
                                          			 use to configure various telephony functions. |
|---|---|

| Feature | Description and More Information |
|---|---|
| AES 256 Encryption Support for Phones | Enhances security by supporting TLS 1.2 and new ciphers. |
| Alphanumeric Dialing | Allows users to place a call with alphanumeric characters. You can use these characters for alphanumeric dialing: a-z, A-Z,
                                          0-9, -, _, ., and +. |
| Any Call Pickup | Allows
                                          						users to pick up a call on any line in their call pickup group, regardless of
                                          						how the call was routed to the phone. |
| Audio Settings | Configures audio settings for the phone speaker, the handset, and the headsets that are connected to the phone. |
| Auto Answer | Connects incoming calls automatically after a ring or two. Auto Answer works with either the speakerphone or the headset. |
| Blind Transfer | Blind Transfer: This transfer joins two established calls (call is in hold or in connected state) into one call and drops
                                          the feature initiator from the call. Blind Transfer does not initiate a consultation call and does not put the active call
                                          on hold. Some JTAPI/TAPI applications are not compatible with the Join and Blind Transfer feature implementation on the Cisco IP Phone
                                          and you may need to configure the Join and Direct Transfer Policy to disable join and direct transfer on the same line or
                                          possibly across lines. |
| Busy Lamp Field (BLF) | Allows user to monitor call state of a directory number. |
| Busy
                                          						Lamp Field (BLF) Pickup | Allows user to pick up incoming calls to the directory number monitored through BLF. |
| Call Back | Provides users with an audio and visual alert on the phone when
                                          						a busy or unavailable party becomes available. |
| Call Display Restrictions | Determines the information that will display for calling or
                                          						connected lines, depending on the parties who are involved in the call. 
                                          					  RPID and PAID caller id handling are supported. |
| Call Forward | Allows
                                          						users to redirect incoming calls to another number. Call Forward options
                                          						include Call Forward All, Call Forward Busy, Call Forward No Answer. |
| Call Forward Notification | Allows
                                          						you to configure the information that the user sees when receiving a forwarded
                                          						call. |
| Call History for Shared Line | Allows you to view shared line activity in the phone Call History. This feature: Logs missed calls for a shared line. Logs all answered and placed calls for a shared line. |
| Call Park | Allows
                                          						users to park (temporarily store) a call and then retrieve the call by using
                                          						another phone. |
| Call Pickup | Allows
                                          						users to redirect a call that is ringing on another phone within their pickup
                                          						group to their phone. You
                                          						can configure an audio and visual alert for the primary line on the phone. This
                                          						alert notifies the users that a call is ringing in their pickup group. |
| Call Waiting | Indicates (and allows users to answer) an incoming call that
                                          						rings while on another call. Incoming call information appears on the phone
                                          						display. |
| Caller ID | Caller
                                          						identification such as a phone number, name, or other descriptive text appear
                                          						on the phone display. |
| Caller ID Blocking | Allows
                                          						a user to block their phone number or name from phones that have caller
                                          						identification enabled. |
| Calling Party Normalization | Calling party normalization presents phone calls to the user
                                          						with a dialable phone number. Any escape codes are added to the number so that
                                          						the user can easily connect to the caller again. The dialable number is saved
                                          						in the call history and can be saved in the Personal Address Book. |
| Conference | Allows
                                          						a user to talk simultaneously with multiple parties by calling each participant
                                          						individually. Allows a noninitiator in a standard (ad hoc) conference to add or remove participants; also allows any conference participant
                                          to join together two standard conferences on the same line. Note Be
                                                      						  sure to inform your users whether these features are activated. | Note | Be
                                                      						  sure to inform your users whether these features are activated. |
| Note | Be
                                                      						  sure to inform your users whether these features are activated. |
| Configurable RTP/sRTP Port Range | Provides a configurable port range (2048 to 65535) for Real-Time Transport Protocol (RTP) and secure Real-Time Transport Protocol
                                          (sRTP). The default RTP and sRTP port range is 16384 to 16538. You configure the RTP and sRTP port range in the SIP Profile. |
| Directed Call Pickup | Allows a user to pick up a ringing call on a DN directly by pressing the GPickUp softkey and entering the directory number
                                          of the device that is ringing. |
| Divert | Allows
                                          						a user to transfer a ringing, connected, or held call directly to a
                                          						voice-messaging system. When a call is diverted, the line becomes available to
                                          						make or receive new calls. |
| Do Not Disturb (DND) | When
                                          						DND is turned on, either no audible rings occur during the ringing-in state of
                                          						a call, or no audible or visual notifications of any type occur. |
| DND and Call Forward Indication on Non-selected Line Key | Displays the DND and call forward icons next the to the line key label. The line key should be enabled with feature key sync.
                                          The line key should also be enabled with DND or call forward. |
| Emergency Calls | Enables users to make emergency calls. The emergency services receive the phone's location and a call-back number, to use
                                          when the emergency call unexpectedly disconnects. |
| Headset Sidetone Control | Allows an administrator to set the sidetone level of a wired headset. |
| Group Call Pickup | Allows
                                          						a user to answer a call that is ringing on a directory number in another group. |
| Hold Status | Enables phones with a shared line to distinguish between the
                                          						local and remote lines that placed a call on hold. |
| Hold/Resume | Allows
                                          						the user to move a connected call from an active state to a held state. No configurations are required unless you want to use Music On Hold. See "Music On Hold" in this table. See "Hold Reversion" in this table. |
| HTTP Download | Enhances the file download process to the phone to use HTTP by
                                          						default. If the HTTP download fails, the phone reverts to using the TFTP
                                          						download. |
| HTTPS for Phone Services | Increases security by requiring communication using HTTPS. Note When the web is in HTTPS mode, the phone is an HTTPS server. | Note | When the web is in HTTPS mode, the phone is an HTTPS server. |
| Note | When the web is in HTTPS mode, the phone is an HTTPS server. |
| Improve Caller Name and Number Display | Improves the display of caller names and numbers. If the Caller Name is known, then the Caller Number is displayed instead
                                          of Unknown . |
| Jitter Buffer | The
                                          						Jitter Buffer feature handles jitter from 10 milliseconds (ms) to 1000 ms for
                                          						both audio and video streams. |
| Join
                                          						Across Lines | Allows
                                          						users to combine calls that are on multiple phone lines to create a conference
                                          						call. Some
                                          						JTAPI/TAPI applications are not compatible with the Join and Direct Transfer
                                          						feature implementation on the Cisco IP Phone and you may need to configure the
                                          						Join and Direct Transfer Policy to disable join and direct transfer on the same
                                          						line or possibly across lines. |
| Join | Allows
                                          						users to combine two calls that are on one line to create a conference call and
                                          						remain on the call. |
| Message Waiting | Defines directory numbers for message waiting on and off
                                          						indicators. A directly-connected voice-message system uses the specified
                                          						directory number to set or to clear a message waiting indication for a
                                          						particular Cisco IP Phone. |
| Message Waiting Indicator | A light on the handset that indicates that a user has one or more new voice messages. |
| Minimum Ring Volume | Sets a
                                          						minimum ringer volume level for an IP phone. |
| Missed
                                          						Call Logging | Allows
                                          						a user to specify whether missed calls will be logged in the missed calls
                                          						directory for a given line appearance. |
| Multicasting Paging | Enables users to page some or all phones. If the phone is on an active call while a group page starts, the incoming page is
                                          ignored. |
| Multiple Calls Per Line Appearance | Each
                                          						line can support multiple calls. By default, the phone supports two active
                                          						calls per line, and a maximum of ten active calls per line. Only one call can
                                          						be connected at any time; other calls are automatically placed on hold. The
                                          						system allows you to configure maximum calls/busy trigger not more than 10/6.
                                          						Any configuration more than 10/6 is not officially supported. |
| Music
                                          						On Hold | Plays music while callers are on hold. |
| Mute | Mutes the handset or headset microphone. |
| No
                                          						Alert Name | Makes
                                          						it easier for end users to identify transferred calls by displaying the
                                          						original caller’s phone number. The call appears as an Alert Call followed by
                                          						the caller’s telephone number. |
| Pause
                                          						in Speed Dial | Users
                                          						can set up the speed-dial feature to reach destinations that require Forced
                                          						Authorization Code (FAC) or Client Matter Code (CMC), dialing pauses, and
                                          						additional digits (such as a user extension, a meeting access code, or a
                                          						voicemail password) without manual intervention. When the user presses the
                                          						speed dial, the phone establishes the call to the specified DN and sends the
                                          						specified FAC, CMC, and DTMF digits to the destination and inserts the
                                          						necessary dialing pauses. |
| Peer Firmware Sharing (PFS) | Allows IP Phones located at remote sites to share the firmware files amongst them, which saves bandwidth when the upgrade
                                          process takes place. This feature uses Cisco Peer-to-Peer-Distribution Protocol (CPPDP) which is a Cisco proprietary protocol
                                          used to form a peer-to-peer hierarchy of devices. CPPDP is also used to copy firmware or other files from peer devices to
                                          the neighbouring devices. PFS aids in firmware upgrades in branch/remote office deployment scenarios that run over bandwidth-limited WAN links. Provides the following advantages over the traditional upgrade method: Limits congestion on TFTP transfers to centralized remote TFTP servers Eliminates the need to manually control firmware upgrades Reduces phone downtime during upgrades when large numbers of devices are reset simultaneously The more the number of IP phones, the better it's performance compared to the traditional firmware upgrade method. |
| Plus
                                          						Dialing | Allows
                                          						the user to dial E.164 numbers prefixed with a plus (+)  sign. To
                                          						dial the + sign, the user needs to press and hold the star (*) key for at least
                                          						1 second. This applies to dialing the first digit for an on-hook (including
                                          						edit mode) or off-hook call. |
| Power
                                          						Negotiation over LLDP | Allows
                                          						the phone to negotiate power using Link Level Endpoint Discovery Protocol
                                          						(LLDP) and Cisco Discovery Protocol (CDP). |
| Problem Reporting Tool | Submits phone logs or reports problems to an administrator. |
| Programmable Feature Buttons | You can assign features, such as New Call, Call Back, and Forward All to line buttons. |
| Redial | Allows
                                          						users to call the most recently dialed phone number by pressing a button or the
                                          						Redial softkey. |
| Remote Customization (RC) | Allows a service provider to customize the phone remotely. There is no need for either the service provider to physically
                                          touch the phone or a user to configure the phone. The service provider can work with a sales engineer at the time of ordering
                                          to set this up. |
| Ringtone Setting | Identifies ring type used for a line when a phone has another
                                          						active call. |
| Reverse Name Lookup | Identifies the caller name using the incoming or outgoing call number. You must configure either the LDAP Directory or the
                                          XML directory. You can enable or disable the reverse name lookup using the phone administration web page. |
| RTCP
                                          						Hold For SIP | Ensures that held calls are not dropped by the gateway. The
                                          						gateway checks the status of the RTCP port to determine if a call is active or
                                          						not. By keeping the phone port open, the gateway will not end held calls. |
| Serviceability for SIP Endpoints | Enables administrators to quickly and easily gather debug information from
                                          						phones. This
                                          						feature uses SSH to remotely access each IP phone. SSH must be enabled on each
                                          						phone for this feature to function. |
| Shared
                                          						Line | Allows
                                          						a user with multiple phones to share the same phone number or allows a user to
                                          						share a phone number with a coworker. |
| Show
                                          						Calling ID and Calling Number | The
                                          						phones can display both the calling ID and calling number for incoming calls.
                                          						The IP phone LCD display size limits the length of the calling ID and the
                                          						calling number that display. The
                                          						Show Calling ID and Calling Number feature applies to the incoming call alert
                                          						only and does not change the function of the Call Forward and Hunt Group
                                          						features. See "Caller ID" in this table. |
| Show
                                          						Duration for Call History | Displays the time duration of placed and received calls in the Call History
                                          						details. If the
                                          						duration is greater than or equal to one hour, the time is displayed in the
                                          						Hour, Minute, Second (HH:MM:SS) format. If the
                                          						duration is less than one hour, the time is displayed in the Minute, Second
                                          						(MM:SS) format. If the
                                          						duration is less than one minute, the time is displayed in the Second (SS)
                                          						format. |
| Silence Incoming Call | Allows you to silence an incoming call by pressing Ignore softkey or by pressing the volume button down. |
| Speed
                                          						Dial | Dials
                                          						a specified number that has been previously stored. |
| Time
                                          						Zone Update | Updates the Cisco IP Phone with time zone changes. |
| Transfer | Allows
                                          						users to redirect connected calls from their phones to another number. Some
                                          						JTAPI/TAPI applications are not compatible with the Join and Direct Transfer
                                          						feature implementation on the Cisco IP Phone and you may need to configure the
                                          						Join and Direct Transfer Policy to disable join and direct transfer on the same
                                          						line or possibly across lines. |
| Voice Message System | Enables callers to leave messages if calls are unanswered. |
| Web Access Enable   by Default | Web services are enabled by default. |
| XSI call logs display | Allows you to configure a phone to display recent call logs from either the BroadWorks server or the local phone. After you
                                          enable the feature, the Recents screen has a Display recents from menu and the user can choose the XSI call logs or the local call logs. |

| Note | Be
                                                      						  sure to inform your users whether these features are activated. |
|---|---|

| Note | When the web is in HTTPS mode, the phone is an HTTPS server. |
|---|---|

| Note | The Cisco IP Phone 7811 does not have programmable feature buttons. |
|---|---|

| Feature Name | Dedicated Feature Button | Programmable Feature Button | Softkey |
|---|---|---|---|
| Answer |  | X | X |
| Call Forward All |  | X | X |
| Call Park |  | X | X |
| Call Park Line Status |  | X |  |
| Call Pickup (Pick Up) |  | X | X |
| Call Pickup Line Status |  | X |  |
| Conference | X |  | X (only displayed during connected call conference scenario) |
| Divert |  |  | X |
| Do Not Disturb |  | X | X |
| Hold | X |  | X |
| Intercom |  | X |  |
| Mute | X |  |  |
| Redial |  | X | X |
| Speed Dial |  | X | X |
| Speed Dial Line Status |  | X |  |
| Transfer | X |  | X (only displayed during connected call transfer scenario) |

| Step 1 | On the phone administration web page, go to Admin Login > Advanced , Voice tab. |
|---|---|
| Step 2 | To allow features, go to Att Console > General , and configure Customizable PLK Options as described in General . |
| Step 3 | To enable feature configuration on a line key on the phone, do one of the following: Disable the extension function for the line key: Go to Voice > Phone . Set Extension to Disabled in the corresponding Line Key number section. Disable service on the corresponding line: Go to Voice . Go to the corresponding Ext number tab. In the General section, set Line Enable to No . |

| Step 1 | On the phone administration web page, go to Admin Login > Advanced , Voice tab. |
|---|---|
| Step 2 | To allow features, go to Att Console > General , and configure Customizable PLK Options as described in General . |
| Step 3 | To enable feature configuration on a line key on the phone, do one of the following: Disable the extension function for the line key: Go to Voice > Phone . Set Extension to Disabled in the corresponding Line Key number section. Disable service on the corresponding line: Go to Voice . Go to the corresponding Ext number tab. In the General section, set Line Enable to No . |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | Select a Line
                                       			 Key on which to configure speed-dial. |
| Step 3 | From the
                                       			 Extension pulldown menu, select Disabled to disable the extension. |
| Step 4 | In the Extended Function field, enter a string in this
                                       			 format: fnc=sd;ext=9999@$PROXY;nme=xxxx If
                                          				you configure a phone with alphanumeric dialing feature in which the phone can
                                          				place a call with alphanumeric characters instead of the traditional digits,
                                          				you can enter a string in this format: fnc=sd;ext=xxxx.yyyy@$PROXY;vid=n;nme=xxxx where: fnc= sd means
                                                				  function=speed dial ext=
                                                   					 9999 is the phone that the line key calls. Replace 9999 with appropriate phone
                                                   					 number. ext=
                                                   					 xxxx.yyyy is the phone that the line key calls. Replace xxxx.yyyy with
                                                   					 alphanumeric characters. You can use these characters for alphanumeric dialing:
                                                   					 a-z, A-Z, 0-9, -, _, ., and +. vid=n is
                                                   					 the line index of the phone. nme= XXXX is the name
                                                				  displayed on the phone for the speed-dial line key. Replace XXXX with a name. You can also
                                          				configure XML service with line key. Enter a string in this format: fnc=xml;url=http://xml.service.url;nme=name |
| Step 5 | Click Submit
                                          				All Changes . |

| Step 1 | Select Voice > User . |
|---|---|
| Step 2 | In the Speed
                                          				Dial section, enter a name and number that corresponds to the speed
                                       			 dial entry. |
| Step 3 | Click Submit
                                          				All Changes . |

| Parameter | Description |
|---|---|
| Speed Dial Name | Indicates the name given to the speed dial. |
| Speed Dial Number | Indicates the number allocated to the speed dial. |

| Step 1 | Select Voice > Ext(n) , where n is an extension
                                       			 number. |
|---|---|
| Step 2 | In the Call
                                          				Features Settings section, select Yes for the Conference Single Hardkey field, enter a star code
                                       			 in the Conference Bridge URL , and press Submit All Changes . For example, you can enter *55
                                       			 to represent the conference bridge URL of a telecom service provider. You can also
                                          				enable the conference button with a xml file. Enter a string in this format: <Conference_Bridge_URL_1_ ua="na">*55</Conference_Bridge_URL_1_> <Conference_Single_Hardkey_1_ ua="na">Yes</Conference_Single_Hardkey_1_> |

| Step 1 | On the
                                       			 Configuration Utility page, click Admin
                                             				  Login > Voice > Phone . |
|---|---|
| Step 2 | Choose a line
                                       			 key and select an extension to enable it. |
| Step 3 | Click Submit
                                          				All Changes . |

| Step 1 | On the phone web page, select Voice > User . The user can select User Login > Voice > User to add screen saver to the phone. |
|---|---|
| Step 2 | In the Screen section, set up the fields as described in the following table. Parameter Description Screen Saver Enable Select Yes to enable a screen saver on the phone. When the phone is idle for a specified time, it enters screen saver mode. Default: No Screen Saver Type Types of screen saver. Options you can choose: Clock —Displays a digital clock on a plain background. Download Picture —Displays a picture pushed from the phone webpage. Logo : Displays a logo on the phone screen. Add a logo image in the Logo URL field. Screen Saver Wait Amount of idle time before screen saver displays. Enter the number of seconds of idle time to elapse before the screen saver starts. Default: 300 Picture Download URL URL locating the (.png) file to display on the phone screen background.  If you select picture as as screensaver type, this
                                                      image displays as a screensaver on the phone screen. When you enter an incorrect URL to download a new wallpaper, the phone fails to upgrade to the newer wallpaper and displays
                                                      the existing downloaded wallpaper. If the phone does not have any wallpaper downloaded earlier, it displays a gray screen. Logo URL Enter a URL or path for the location where the logo image is saved. If you select logo as as screensaver type, this image
                                                      displays as a screensaver on the phone screen. | Parameter | Description | Screen Saver Enable | Select Yes to enable a screen saver on the phone. When the phone is idle for a specified time, it enters screen saver mode. Default: No | Screen Saver Type | Types of screen saver. Options you can choose: Clock —Displays a digital clock on a plain background. Download Picture —Displays a picture pushed from the phone webpage. Logo : Displays a logo on the phone screen. Add a logo image in the Logo URL field. | Screen Saver Wait | Amount of idle time before screen saver displays. Enter the number of seconds of idle time to elapse before the screen saver starts. Default: 300 | Picture Download URL | URL locating the (.png) file to display on the phone screen background.  If you select picture as as screensaver type, this
                                                      image displays as a screensaver on the phone screen. When you enter an incorrect URL to download a new wallpaper, the phone fails to upgrade to the newer wallpaper and displays
                                                      the existing downloaded wallpaper. If the phone does not have any wallpaper downloaded earlier, it displays a gray screen. | Logo URL | Enter a URL or path for the location where the logo image is saved. If you select logo as as screensaver type, this image
                                                      displays as a screensaver on the phone screen. |
| Parameter | Description |
| Screen Saver Enable | Select Yes to enable a screen saver on the phone. When the phone is idle for a specified time, it enters screen saver mode. Default: No |
| Screen Saver Type | Types of screen saver. Options you can choose: Clock —Displays a digital clock on a plain background. Download Picture —Displays a picture pushed from the phone webpage. Logo : Displays a logo on the phone screen. Add a logo image in the Logo URL field. |
| Screen Saver Wait | Amount of idle time before screen saver displays. Enter the number of seconds of idle time to elapse before the screen saver starts. Default: 300 |
| Picture Download URL | URL locating the (.png) file to display on the phone screen background.  If you select picture as as screensaver type, this
                                                      image displays as a screensaver on the phone screen. When you enter an incorrect URL to download a new wallpaper, the phone fails to upgrade to the newer wallpaper and displays
                                                      the existing downloaded wallpaper. If the phone does not have any wallpaper downloaded earlier, it displays a gray screen. |
| Logo URL | Enter a URL or path for the location where the logo image is saved. If you select logo as as screensaver type, this image
                                                      displays as a screensaver on the phone screen. |
| Step 3 | Click Submit All Changes . |

| Parameter | Description |
|---|---|
| Screen Saver Enable | Select Yes to enable a screen saver on the phone. When the phone is idle for a specified time, it enters screen saver mode. Default: No |
| Screen Saver Type | Types of screen saver. Options you can choose: Clock —Displays a digital clock on a plain background. Download Picture —Displays a picture pushed from the phone webpage. Logo : Displays a logo on the phone screen. Add a logo image in the Logo URL field. |
| Screen Saver Wait | Amount of idle time before screen saver displays. Enter the number of seconds of idle time to elapse before the screen saver starts. Default: 300 |
| Picture Download URL | URL locating the (.png) file to display on the phone screen background.  If you select picture as as screensaver type, this
                                                      image displays as a screensaver on the phone screen. When you enter an incorrect URL to download a new wallpaper, the phone fails to upgrade to the newer wallpaper and displays
                                                      the existing downloaded wallpaper. If the phone does not have any wallpaper downloaded earlier, it displays a gray screen. |
| Logo URL | Enter a URL or path for the location where the logo image is saved. If you select logo as as screensaver type, this image
                                                      displays as a screensaver on the phone screen. |

| LED Color | Meaning |
|---|---|
| Green | The monitored line is available. |
| Red | The monitored line is busy. |
| Blinking red | The monitored line is ringing. |
| Amber | Error in BLF key configuration. |

| Step 1 | On the phone administration web page, go to Admin Login > Advanced , Voice > Att Console > General . |
|---|---|
| Step 2 | Configure BLF List URI , BLF List , and Use Line Keys For BLF List as described in General . If you allow users to configure individual BLF keys (see Enable Users to Configure Features on Line Keys ), we recommend setting BLF List to Hide . |
| Step 3 | Click Submit All Changes . |

| LED Color | Meaning |
|---|---|
| Green | The monitored line is available. |
| Red | The monitored line is busy. |
| Blinking red | The monitored line is ringing. |
| Amber | Error in BLF key configuration. |

| Step 1 | On the phone administration web page, go to Admin Login > Advanced , Voice > Att Console > General . |
|---|---|
| Step 2 | Configure BLF List URI , BLF List , and Use Line Keys For BLF List as described in General . If you allow users to configure individual BLF keys (see Enable Users to Configure Features on Line Keys ), we recommend setting BLF List to Hide . |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | Select a line
                                          			 key on which to configure a busy lamp field. |
| Step 3 | Select Disabled to disable the extension. |
| Step 4 | In the Extended Function field, enter a string in this
                                          			 format: fnc=blf;sub=xxxx@$PROXY;usr=yyyy@$PROXY fnc=blf;sub=xxxx@$PROXY;ext=yyyy@$PROXY Where: fnc=blf means function=busy lamp field sub=the URI to which the SUBSCRIBE message should be sent. For a BroadSoft server, this name must be identical to the name
                                                   defined in the List URI: sip: parameter. xxxx is the name that is defined in List URI: sip : parameter. Replace xxxx with the exact defined name. $PROXY is the server. Replace $PROXY with the server address or name. usr/ext=the user that the busy lamp field monitors. yyyy is user id of the phone that the busy lamp field monitors. Replace
                                                   yyyy with the exact user id of the monitored phone. $PROXY is the server. Replace $PROXY with the server address or name. |
| Step 5 | (Optional) You can
                                          			 configure the busy lamp field to work with any combination of speed dial or
                                          			 call pickup. To enable the busy lamp field to work with speed dial or call
                                          			 pickup, enter a string in the following format in the Extended Function field: fnc=blf+sd+cp;sub=xxxx@$PROXY;usr=yyyy@$PROXY . Where: sd= speed dial cp= call
                                             				pickup |
| Step 6 | Click Submit
                                             				All Changes . |

| Step 1 | Select Voice > Att Console . |
|---|---|
| Step 2 | Select a key
                                       			 expansion module line key. |
| Step 3 | Enter a
                                       			 string in the appropriate format. Feature String Format Busy Lamp Field and Speed Dial fnc=blf+sd;sub=xxx@proxy;ext=monitored userID@proxy . Busy Lamp Field, Speed Dial, and Call Pickup fnc=blf+sd+cp;sub=xxx@proxy;ext=monitored userID@proxy . Busy Lamp Field, Speed Dial, and Park Notification fnc=blf+sd;sub=xxx@proxy;ext=monitored userID@proxy . This combination cannot be configured using the extended
                                                      							 function. This combination is supported on Broadsoft servers only and it is
                                                      							 configured using the BLF List and related configuration on the server. Busy Lamp Field, Speed Dial, Park Notification, and Call Pickup fnc=blf+sd+cp;sub=xxx@proxy;ext=monitored userID@proxy . This combination cannot be configured using the extended
                                                      							 function. This combination is supported on Broadsoft servers only and it is
                                                      							 configured using the BLF List and related configuration on the server. Busy Lamp Field and Park Notification fnc=blf;sub=xxx@proxy;ext=monitored userID@proxy . This combination cannot be configured using the extended
                                                      							 function. This combination is supported on Broadsoft servers only and it is
                                                      							 configured using the BLF List and related configuration on the server. Busy Lamp Field, Park Notification, and Call Pickup fnc=blf+cp;sub=xxx@proxy;ext=monitored userID@proxy . This combination cannot be configured using the extended
                                                      							 function. This combination is supported on Broadsoft servers only and it is
                                                      							 configured using the BLF List and related configuration on the server. Busy Lamp Field and Call Pickup fnc=blf+cp;sub=xxx@proxy;ext=monitored userID@proxy | Feature | String Format | Busy Lamp Field and Speed Dial | fnc=blf+sd;sub=xxx@proxy;ext=monitored userID@proxy . | Busy Lamp Field, Speed Dial, and Call Pickup | fnc=blf+sd+cp;sub=xxx@proxy;ext=monitored userID@proxy . | Busy Lamp Field, Speed Dial, and Park Notification | fnc=blf+sd;sub=xxx@proxy;ext=monitored userID@proxy . This combination cannot be configured using the extended
                                                      							 function. This combination is supported on Broadsoft servers only and it is
                                                      							 configured using the BLF List and related configuration on the server. | Busy Lamp Field, Speed Dial, Park Notification, and Call Pickup | fnc=blf+sd+cp;sub=xxx@proxy;ext=monitored userID@proxy . This combination cannot be configured using the extended
                                                      							 function. This combination is supported on Broadsoft servers only and it is
                                                      							 configured using the BLF List and related configuration on the server. | Busy Lamp Field and Park Notification | fnc=blf;sub=xxx@proxy;ext=monitored userID@proxy . This combination cannot be configured using the extended
                                                      							 function. This combination is supported on Broadsoft servers only and it is
                                                      							 configured using the BLF List and related configuration on the server. | Busy Lamp Field, Park Notification, and Call Pickup | fnc=blf+cp;sub=xxx@proxy;ext=monitored userID@proxy . This combination cannot be configured using the extended
                                                      							 function. This combination is supported on Broadsoft servers only and it is
                                                      							 configured using the BLF List and related configuration on the server. | Busy Lamp Field and Call Pickup | fnc=blf+cp;sub=xxx@proxy;ext=monitored userID@proxy |
| Feature | String Format |
| Busy Lamp Field and Speed Dial | fnc=blf+sd;sub=xxx@proxy;ext=monitored userID@proxy . |
| Busy Lamp Field, Speed Dial, and Call Pickup | fnc=blf+sd+cp;sub=xxx@proxy;ext=monitored userID@proxy . |
| Busy Lamp Field, Speed Dial, and Park Notification | fnc=blf+sd;sub=xxx@proxy;ext=monitored userID@proxy . This combination cannot be configured using the extended
                                                      							 function. This combination is supported on Broadsoft servers only and it is
                                                      							 configured using the BLF List and related configuration on the server. |
| Busy Lamp Field, Speed Dial, Park Notification, and Call Pickup | fnc=blf+sd+cp;sub=xxx@proxy;ext=monitored userID@proxy . This combination cannot be configured using the extended
                                                      							 function. This combination is supported on Broadsoft servers only and it is
                                                      							 configured using the BLF List and related configuration on the server. |
| Busy Lamp Field and Park Notification | fnc=blf;sub=xxx@proxy;ext=monitored userID@proxy . This combination cannot be configured using the extended
                                                      							 function. This combination is supported on Broadsoft servers only and it is
                                                      							 configured using the BLF List and related configuration on the server. |
| Busy Lamp Field, Park Notification, and Call Pickup | fnc=blf+cp;sub=xxx@proxy;ext=monitored userID@proxy . This combination cannot be configured using the extended
                                                      							 function. This combination is supported on Broadsoft servers only and it is
                                                      							 configured using the BLF List and related configuration on the server. |
| Busy Lamp Field and Call Pickup | fnc=blf+cp;sub=xxx@proxy;ext=monitored userID@proxy |
| Step 4 | Click Submit All Changes . |

| Feature | String Format |
|---|---|
| Busy Lamp Field and Speed Dial | fnc=blf+sd;sub=xxx@proxy;ext=monitored userID@proxy . |
| Busy Lamp Field, Speed Dial, and Call Pickup | fnc=blf+sd+cp;sub=xxx@proxy;ext=monitored userID@proxy . |
| Busy Lamp Field, Speed Dial, and Park Notification | fnc=blf+sd;sub=xxx@proxy;ext=monitored userID@proxy . This combination cannot be configured using the extended
                                                      							 function. This combination is supported on Broadsoft servers only and it is
                                                      							 configured using the BLF List and related configuration on the server. |
| Busy Lamp Field, Speed Dial, Park Notification, and Call Pickup | fnc=blf+sd+cp;sub=xxx@proxy;ext=monitored userID@proxy . This combination cannot be configured using the extended
                                                      							 function. This combination is supported on Broadsoft servers only and it is
                                                      							 configured using the BLF List and related configuration on the server. |
| Busy Lamp Field and Park Notification | fnc=blf;sub=xxx@proxy;ext=monitored userID@proxy . This combination cannot be configured using the extended
                                                      							 function. This combination is supported on Broadsoft servers only and it is
                                                      							 configured using the BLF List and related configuration on the server. |
| Busy Lamp Field, Park Notification, and Call Pickup | fnc=blf+cp;sub=xxx@proxy;ext=monitored userID@proxy . This combination cannot be configured using the extended
                                                      							 function. This combination is supported on Broadsoft servers only and it is
                                                      							 configured using the BLF List and related configuration on the server. |
| Busy Lamp Field and Call Pickup | fnc=blf+cp;sub=xxx@proxy;ext=monitored userID@proxy |

| Step 1 | Select Voice > Ext . |
|---|---|
| Step 2 | In the Enable URI Dialing 1 , select Yes to enable alphanumeric dialing. In the phone
                                          				page, you can add a string on a line key in this format to enable speed dial
                                          				with alphanumeric dialing capability: fnc=sd;ext=xxxx.yyyy@$PROXY;nme=yyyy,xxxx For example: fnc=sd;ext=first.last@$PROXY;nme=Last,First The above
                                          				example will enable the user to dial "first.dial" to make a call. Note The
                                                      				  supported characters that you can use for alphanumeric dialing are a-z, A-Z,
                                                      				  0-9, -, _, ., and +. | Note | The
                                                      				  supported characters that you can use for alphanumeric dialing are a-z, A-Z,
                                                      				  0-9, -, _, ., and +. |
| Note | The
                                                      				  supported characters that you can use for alphanumeric dialing are a-z, A-Z,
                                                      				  0-9, -, _, ., and +. |
| Step 3 | Click Submit All Changes . |

| Note | The
                                                      				  supported characters that you can use for alphanumeric dialing are a-z, A-Z,
                                                      				  0-9, -, _, ., and +. |
|---|---|

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Multiple Paging Group Parameters section, enter a
                                       			 string in the Group Paging Script field in this format: pggrp=multicast-address:port;[name=xxxx;]num=yyy;[listen={yes\|no}]]; where: multicast-address = Multicast IP address of the phone that
                                                					 listens for and receives pages. port = Port on which to page; you must use different, even-number ports for each paging group. Caution Multicast paging doesn't work with odd-numbered ports. name (optional) = xxxx is the name of the paging group. Replace xxxx with a name. The name can consist maximum of 64 characters. num= yyy is a unique number that the user dials to access the paging group. Replace yyy with a number. The number can consist maximum of 64 characters and the allowed range is 1024 to 32767. listen = Indicates whether the phone listens on the page group. Only the first two groups with listen set to yes listen to group pages. If the field is not defined, the default value is no , so you must set this field to listen to the group pages. You can add more paging groups by appending to the configuration string. Here is an example of several paging groups. pggrp=224.168.168.168:34560;name=All;num=500;listen=yes;
pggrp=224.168.168.168:34562;name=GroupA;num=501;listen=yes;
pggrp=224.168.168.168:34564;name=GroupB;num=502;
pggrp=224.168.168.168:34566;name=GroupC;num=503; This example creates four paging groups: All , GroupA , GroupB , and GroupC . Users dial 500 to send pages to all phones, 501 to send pages to phones configured as part of the GroupA group, 502 to send pages to phones configured as part of the GroupB group, and 503 to send pages to phones configured as part of the GroupC group. The configured phone receives pages directed to the All and GroupA groups. | Caution | Multicast paging doesn't work with odd-numbered ports. |
| Caution | Multicast paging doesn't work with odd-numbered ports. |
| Step 3 | Click Submit All Changes . |

| Caution | Multicast paging doesn't work with odd-numbered ports. |
|---|---|

| Step 1 | In the phone web page, select Admin Login > Advanced > Voice > Phone . |
|---|---|
| Step 2 | In the Multipaging Group Parameters section, enter a string in this format in the Group Paging Script field. pggrp=multicast-address:port;[name=xxxx;]num=yyy;[listen={yes\|no}]];pri=n where: multicast-address = Multicast IP address of the phone that listens for and receives pages. port = Port on which to page; you must use different ports for each paging group. name (optional) = xxxx is the name of the paging group. Replace xxxx with a name. The name can consist maximum of 64 characters. num= yyy is a unique number that the user dials to access the paging group. Replace yyy with a number. The number can consist
                                                maximum of 64 characters and the allowed range is 1024 to 32767. listen = Indicates whether the phone listens on the page group. Only the first two groups with listen set to yes listen to
                                                group pages. If the field is not defined, the default value is no, so you must set this field to listen to the group pages. pri = n indicates the priority level of the paging. Priority level ranges from 0 to 4. You can add more paging groups by appending to the configuration string and set the paging priority. Here is an example. pggrp=224.168.168.168:34560;name=All;num=500;listen=yes;pri=0
pggrp=224.168.168.168:34562;name=GroupA;num=501;listen=yes;pri=1
pggrp=224.168.168.168:34564;name=GroupB;num=502;pri=2
pggrp=224.168.168.168:34566;name=GroupC;num=503;pri=3 This example creates four paging groups: All, GroupA, GroupB, and GroupC. Users dial 500 to send pages to all phones. If the
                                          phone receives a page on the “All” group during a call, the call will be put on hold. User dials 501 to send pages to phones configured as part of the GroupA group. If the phone receives a page on the “GroupA”
                                          group during a call, the audio from page and call will be mixed. User dials 502 to send pages to phones configured as part of the GroupB group. If the phone configured in GroupA receives
                                          a page during an active call, the paging UI will not show up on the device, and a notification tone will be played upon receiving
                                          the page. Once the active call ends, and if the page is still active, the paging UI will show up on the device. User dials 503 to send pages to phones configured as part of the GroupC group. If the phone configured in GroupC receives
                                          a page during an active call, the page will be ignored. |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > Regional . |
|---|---|
| Step 2 | Enter *68 in the Call
                                             				Park Code field. |
| Step 3 | Enter *88 in the Call
                                             				Unpark Code field. |
| Step 4 | Click Submit
                                             				All Changes . |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | Select a line
                                          			 key. |
| Step 3 | Select Disabled to disable the extension. |
| Step 4 | In the Extended Function field, enter a string in this
                                          			 format: For a private line, enter fnc=prk;sub=$USER@$PROXY;nme=CallPark-Slot1 . For a shared
                                             				line, enter fnc=prk;sub=$USER@$PROXY;nme=Call-Park1;orbit=<DN of primary
                                                				  line> . where: fnc= prk
                                                   					 means function=call park sub=
                                                   					 999999 is the phone to which the call parks. Replace 999999 with a numbers. nme= XXXX
                                                   					 is the name displayed on the phone for the call park line key. Replace XXXX
                                                   					 with a name. |
| Step 5 | Click Submit
                                             				All Changes . |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | Under Programmable Softkeys , edit the softkeys depending
                                       			 on the call state that you want the softkey to display. For more information,
                                       			 see Programmable Softkeys . In the
                                          				Programmable Softkeys section, each phone state is displayed and the softkeys
                                          				that are available to display during that state are listed. Each softkey is
                                          				separated by a semicolon. Softkeys are shown in the format: softkeyname  \|[  position  ] where
                                          				softkeyname is the name of the key and position is where the key is displayed
                                          				on the IP phone screen. Positions are numbered, with position one displayed on
                                          				the lower left of the IP phone screen, followed by positions two through four.
                                          				Additional positions (over four) are accessed by pressing the right arrow key
                                          				on the phone. If no position is given for a softkey, the key will float and
                                          				appears in the first available empty position on the IP phone screen. |
| Step 3 | Click Submit
                                          				All Changes . |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes . |
| Step 3 | Select a
                                          			 programmable softkey number field on which to configure a phone feature. |
| Step 4 | Enter the
                                          			 string for the programmable soft key. See the different types of programmable
                                          			 softkeys described in Configure Speed Dial on a Programmable Softkey . |
| Step 5 | Click Submit
                                             				All Changes . |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes . |
| Step 3 | To configure a speed dial PSK, enter the following in the PSK number field: fnc=sd;ext=starcode@$PROXY;nme=name;ext2=starcode@PROXY;nme2=name2 Where: fnc= function of the key (speed dial) extensionname=extension being dialed or the star code action to perform nme= name of the first action ext2= the second extension being dialed or the star code action to perform nme2= name of the second action to perform Note The name field displays on the softkey on the IP phone screen. We recommend a maximum of 10 characters for a phone. If more characters
                                                         are used, the label might be truncated on the phone screen. | Note | The name field displays on the softkey on the IP phone screen. We recommend a maximum of 10 characters for a phone. If more characters
                                                         are used, the label might be truncated on the phone screen. |
| Note | The name field displays on the softkey on the IP phone screen. We recommend a maximum of 10 characters for a phone. If more characters
                                                         are used, the label might be truncated on the phone screen. |
| Step 4 | Edit the following: Idle Key List: Edit the field to add psk1\|1 to the beginning of the string; for example: psk1\|1;em_login;acd_login;acd_logout;avail;unavail; redial;dir;cfwd;dnd;lcr;pickup;gpickup;unpark;em_logout; PSK1: fnc=sd;ext=*72@$PROXY;nme=CFOn;ext2=*73@$PROXY;nme2= CFOff; Note In this example, a PSK is configured to toggle between turning call forwarding on and off using the “call forwarding on”
                                                         star code (*72) and the “call forwarding off” star code (*73). You can also configure an XML service on the programmable soft key. Enter the string in this format: fnc=xml;url=http://xml.service.url;nme=name | Note | In this example, a PSK is configured to toggle between turning call forwarding on and off using the “call forwarding on”
                                                         star code (*72) and the “call forwarding off” star code (*73). |
| Note | In this example, a PSK is configured to toggle between turning call forwarding on and off using the “call forwarding on”
                                                         star code (*72) and the “call forwarding off” star code (*73). |
| Step 5 | Click Submit All Changes . |

| Note | The name field displays on the softkey on the IP phone screen. We recommend a maximum of 10 characters for a phone. If more characters
                                                         are used, the label might be truncated on the phone screen. |
|---|---|

| Note | In this example, a PSK is configured to toggle between turning call forwarding on and off using the “call forwarding on”
                                                         star code (*72) and the “call forwarding off” star code (*73). |
|---|---|

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes . |
| Step 3 | To configure a
                                          			 speed dial PSK, enter the following in the PSK number field: fnc=sd;ext=extensionname/starcode@$PROXY;vid=n;nme=name Where: fnc=
                                                   					 function of the key (speed dial) extensionname=extension being dialed or the star code action to
                                                   					 perform vid= n
                                                   					 is the extension that the speed dial will dial out name is
                                                   					 the name of the speed dial being configured Note The name field displays on the softkey on the IP phone
                                                         				  screen. We recommend a maximum of 10 characters for a phone. If more characters
                                                         				  are used, the label might be truncated on the phone screen. | Note | The name field displays on the softkey on the IP phone
                                                         				  screen. We recommend a maximum of 10 characters for a phone. If more characters
                                                         				  are used, the label might be truncated on the phone screen. |
| Note | The name field displays on the softkey on the IP phone
                                                         				  screen. We recommend a maximum of 10 characters for a phone. If more characters
                                                         				  are used, the label might be truncated on the phone screen. |
| Step 4 | Edit the
                                          			 following: Idle Key List: Edit the field as described in the following example: redial\|1;newcall\|2;dnd;psk1 If the
                                                   					 user incorrectly configures the programmable softkey list features on the
                                                   					 phone, the key list on the phone LCD does not update. For example: If a
                                                            						  user enters rdeial;newcall;cfwd (redial has been misspelt), the
                                                            						  key list is not updated and the user does not see any change on the LCD. If a
                                                            						  user enters redial;newcall;cfwd;delchar , the user will not see a
                                                            						  change on the LCD, as the delchar softkey is not allowed in the Idle Key
                                                               							 List . Hence, this is an incorrect configuration of the programmable
                                                            						  softkey list. PSK1: fnc=sd;ext=5014@$PROXY;nme=sktest1 Note In this
                                                         				  example, we are configuring a softkey on a phone as a speed dial number for
                                                         				  extension 5014 (sktest1). You can also
                                             				configure an XML service on the programmable soft key. Enter the string in this
                                             				format: fnc=xml;url=http://xml.service.url;nme=name | Note | In this
                                                         				  example, we are configuring a softkey on a phone as a speed dial number for
                                                         				  extension 5014 (sktest1). |
| Note | In this
                                                         				  example, we are configuring a softkey on a phone as a speed dial number for
                                                         				  extension 5014 (sktest1). |
| Step 5 | Click Submit
                                             				All Changes . |

| Note | The name field displays on the softkey on the IP phone
                                                         				  screen. We recommend a maximum of 10 characters for a phone. If more characters
                                                         				  are used, the label might be truncated on the phone screen. |
|---|---|

| Note | In this
                                                         				  example, we are configuring a softkey on a phone as a speed dial number for
                                                         				  extension 5014 (sktest1). |
|---|---|

| Keyword | Key Label | Definition | Available Phone Status |
|---|---|---|---|
| acd_login | Agt signin | Logs user in to Automatic Call Distribution (ACD). | Idle |
| acd_logout | AgtSignOut | Logs user out of ACD. | Idle |
| answer | Answer | Answers an incoming call. | Ringing |
| astate | Agt Status | Checks the ACD status. | Idle |
| avail | Avail | Denotes that a user who is logged in to an ACD server has set his status as available. | Idle |
| barge | Barge | Allows another user to interrupt a shared call. | Shared-Active, Shared-Held |
| bargesilent | BargeSilent | Allows another user to interrupt a shared call with the mic disabled. | Shared-Active |
| bxfer | BlindXfer | Performs a blind call transfer (transfers a call without speaking to the party to whom the call is transferred). Requires
                                             that Blind Xfer Serv is enabled. | Connected |
| call (or dial) | Call | Calls the selected item in a list. | Dialing Input |
| call info | Call Info | Show call information | Progressing |
| cancel | Cancel | Cancels a call (for example, when conferencing a call and the second party is not answering. | Off-Hook |
| cfwd | Forward / Clr fwd | Forwards all calls to a specified number. | Idle, Off-Hook, Shared-Active, Hold, Shared-Held |
| crdpause | PauseRec | Pause recording | Connected, Conferencing |
| crdresume | ResumeRec | Resume recording | Connected, Conferencing |
| crdstart | Record | Start a recording | Connected, Conferencing |
| crdstop | StopRec | Stop recording | Connected, Conferencing |
| conf | Conference | Initiates a conference call. Requires that Conf Server is enabled and there are two or more calls that are active or on hold. | Connected |
| confLx | Conf line | Conferences active lines on the phone. Requires that Conf Serv is enabled and there are two or more calls that are active
                                             or on hold. | Connected |
| delchar | delChar - backspace Icon | Deletes a character when entering text. | Dialing Input |
| dir | Dir | Provides access to phone directories. | Idle, Miss, Off-Hook (no input), Connected, Start-Xfer, Start-Conf, Conferencing, Hold, Ringing, Shared-Active, Shared-Held |
| disp_code | DispCode | Enter Disposition Code | Idle, Connected, Conferencing, Hold |
| dnd | DND / Clr Dnd | Sets Do Not Disturb to prevent calls from ringing the phone. | Idle, Off-Hook, Hold, Shared-Active, Shared-Held, Conferencing, Start-Conf, Start-Xfer |
| emergency | Emergency | Enter emergency number | Connected |
| em_login (or signin) | Sign in | Logs user in to Extension Mobility. | Idle |
| em_logout (or signout) | Sign out | Logs user out of Extension Mobility. | Idle |
| endcall | End call | Ends a call. | Connected, Start-Xfer, Start-Conf, Conferencing, Hold |
| favorites | Favorites | Provides access to "Speed Dials". | Idle, Miss, Off-Hook (no input), Connected, Start-Xfer, Start-Conf, Conferencing, Hold, Ringing, Shared-Active, Shared-Held |
| gpickup | GrPickup | Allows user to answer a call ringing on an extension by discovering the number of the ringing extension. | Idle, Off-Hook |
| hold | Hold | Put a call on Hold. | Connected, Start-Xfer, Start-Conf, Conferencing |
| ignore | Decline | Ignores an incoming call. | Ringing |
| ignoresilent | Ignore | Silences an incoming call | Ringing |
| join | Join | Connects a conference call. If the conference host is user A and users B & C are participants, when A presses "Join", A will
                                             drop off and users B & C will be connected. | Conferencing |
| lcr | Call Rtn/lcr | Returns the last missed call. | Idle, Missed-Call,Off-Hook (no input) |
| left | Left arrow icon | Moves the cursor to the left. | Dialing Input |
| messages | Messages | Provides access to voicemail. | Idle, Miss, Off-Hook (no input), Connected, Start-Xfer, Start-Conf, Conferencing, Hold, Ringing, Shared-Active, Shared-Held |
| miss | Miss | Displays the list of missed calls. | Missed-Call |
| newcall | New Call | Begins a new call. | Idle, Hold, Shared-Active, Shared-Held |
| option | Option | Opens a menu of input options. | Off-Hook |
| park | Park | Puts a call on hold at a designated "park" number. | Connected |
| phold | PrivHold | Puts a call on hold on an active shared line. | Connected |
| pickup | PickUp | Allows a user to answer a call ringing on another extension by entering the extension number. | Idle, Off-Hook |
| recents | Recents | Displays the All calls list from call history. | Idle, Off-Hook, Shared-Active, Shared-Held |
| redial | Redial | Displays the redial list. | Idle, Connected, Start-Conf, Start-Xfer, Off-Hook (no input), Hold |
| resume | Resume | Resumes a call that is on hold. | Hold, Shared-Held |
| right | Right arrow icon | Moves the cursor to the right. | Dialing (input) |
| settings | Settings | Provides access to "Information and Settings". | All |
| starcode | Input Star Code/*code | Displays a list of star codes that can be selected. | Off-Hook, Dialing (input) |
| trace | Trace | Trigger trace | Idle, Connected, Conferencing, Hold |
| unavail | Unavail | Denotes that a user who is logged in to an ACD server has set his status as unavailable. | Idle |
| unpark | Unpark | Resumes a parked call. | Idle, Off-Hook, Connected, Shared-Active |
| xfer | Transfer | Performs a call transfer. Requires that Attn Xfer Serv is enabled and there is at least one connected call and one idle call. | Connected, Start-Xfer, Start-Conf |
| xferlx | Xfer line | Transfers an active line on the phone to a called number. Requires that Attn Xfer Serv is enabled and there are two or more
                                             calls that are active or on hold. | Connected |

| Step 1 | Select Voice > Provisioning . |
|---|---|
| Step 2 | In the Configuration Profile section, set the Profile Rule field to the phone configuration file's
                                       			 URL. Example: http://192.0.2.1:80/dms/CP-MMxx-MPP/MMxxSystem.xml where, MM– Cisco IP Phone MM Series with Multiplatform Firmware (68, 78, or 88) MMxx– Cisco specific phone model (for example, 7841,7861, 8845, 8865 or 7832) |
| Step 3 | Select Admin
                                             				  Login > advanced > Voice > Phone . |
| Step 4 | Fill in the EM
                                          				Enable and EM
                                          				User Domain fields in the Extension Mobility section, based on the information
                                       			 provided in the phone configuration file. |
| Step 5 | Set the amount of time (in minutes) that the phone session will last for in the Session Timer(m) field. The phone signs out when the session times out. |
| Step 6 | Set the
                                       			 amount of time (in seconds) that the user has to cancel the sign-out in Countdown Timer(s) . |
| Step 7 | Choose input
                                       			 type of the password from the Preferred Password Input Mode field. For information on
                                          				Extension Mobility fields, see Extension Mobility . Your user
                                          				can also change the password input type from the phone. |
| Step 8 | (Optional) If the Programmable Softkey Enable field in the Programmable Softkeys section is set to Yes , add signin to Idle
                                          				Key List . Example: newcall\|1;signin\|2 |
| Step 9 | Click Submit
                                          				All Changes . |

| Step 1 | In the phone
                                          			 configuration file, set the following parameters: Set the
                                                				  Provisioning Authority profile rules in the Profile_Rule parameters. Example: <Profile_Rule ua="na">("$EMS" eq "mobile" and "$MUID" ne "" and "$MPWD" ne "")?[--uid $MUID$PDOM --pwd $MPWD] http://10.74.121.51:80/dms/CP-8851-3PCC/8851System.xml\|http://10.74.121.51:80/dms/CP-8851-3PCC/8851System.xml</Profile_Rule> Set the EM_Enable parameter to Yes . Example: <EM_Enable ua="na">Yes</EM_Enable> Enter the
                                                				  enter the domain for the phone, or the authentication server in the EM_User_Domain parameter. Example: <EM_User_Domain ua="na">@10.74.121.51</EM_User_Domain> |
|---|---|---|
| Step 2 | Save the
                                          			 configuration file and upload it to your provisioning server. |
| Step 3 | Select Voice > Provisioning . |
| Step 4 | Enter the
                                          			 filepath to the configuration file in one of the Profile Rule fields. Example: http://<SERVER IP ADDRESS>:80/dms/td_8861/8861System.xml |
| Step 5 | Click Submit
                                             				All Changes . |

| Step 1 | Select Voice > Ext
                                             				  [n] (where [n] is the extension number). |
|---|---|
| Step 2 | In the Call
                                          				Feature Settings section, set Enable
                                          				Broadsoft Hoteling to Yes . |
| Step 3 | Set the amount
                                       			 of time (in seconds) that the user can be signed in as a guest on the phone in Hoteling Subscription Expires . |
| Step 4 | Click Submit
                                          				All Changes . |

| Step 1 | Select Voice > System . |
|---|---|
| Step 2 | Set a password
                                       			 in the User
                                          				Password field. |
| Step 3 | Click Submit
                                          				All Changes . |

| Step 1 | Select Info > Debug
                                             				  Info > Device Logs . |
|---|---|
| Step 2 | In the Problem Reports area, click the problem report file
                                       			 to download. |
| Step 3 | Save the file
                                       			 to your local system and open the file to access the problem reporting logs. |

| Step 1 | Select Voice > Provisioning . |
|---|---|
| Step 2 | In the Problem Report Tool section, set the fields as
                                       			 described in the Problem Report Tool . You can also
                                          				configure the parameters in the phone configuration file with XML(cfg.xml)
                                          				code. Enter the string in this format: <PRT_Upload_Rule ua="na"> http://64.101.234.132:8000//Users/abcd/uploads/prt/test-prt.tar.gz </PRT_Upload_Rule> <PRT_Upload_Method
                                             				  ua="na">POST</PRT_Upload_Method> <PRT_Max_Timer
                                             				  ua="na">20</PRT_Max_Timer> |
| Step 3 | Click Submit
                                          				All Changes . |

| Step 1 | Select Voice > User . |
|---|---|
| Step 2 | In the Supplementary Services section, choose Yes for the Auto
                                          				Answer Page field. |
| Step 3 | Click Submit
                                          				All Changes . |

| Step 1 | Select Voice > TR-069 . |
|---|---|
| Step 2 | Set up the
                                       			 fields as described in TR-069 . |
| Step 3 | Click Submit All Changes . |

| Select Info > Status > TR-069 Status . You can view status of TR-069 parameters in TR-069 . |
|---|

| Step 1 | Select Voice > User . |
|---|---|
| Step 2 | Set up the fields as described in Audio Volume . |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Info > Debug
                                             				  Info . |
|---|---|
| Step 2 | In the Problem Reports section, click Generate PRT . |
| Step 3 | Enter the
                                       			 following information in the Report
                                          				Problem screen: Enter the
                                             				  date that you experienced the problem in the Date field. The current date appears in this field
                                             				  by default. Enter the
                                             				  time that you experienced the problem in the Time field. The current time appears in this field
                                             				  by default. In the Select Problem drop-down list box, choose the
                                             				  description of the problem from the available options. |
| Step 4 | Click Submit in the Report
                                          				Problem screen. The Submit
                                          				button is enabled only if you select a value in the Select Problem drop-down list box. You get a
                                          				notification alert on the Phone Web page that indicates if the PRT upload was
                                          				successful or not. |

| To initiate a phone problem report remotely, initiate a SIP-NOTIFY message from the server to the phone, with the Event specified as prt-gen . |
|---|

| Parameter | Description |
|---|---|
| PRT Generation Status | The location of initiation and status of generation of the most recently initiated problem report. Problem reports may be initiated from the phone LCD user interface, from the phone administration web page, or remotely. See Report All Phone Issues from the Phone Web Page and Report a Phone Problem Remotely for details. XML tag in status.xml : PRT_Generation_Status |
| PRT Upload Status | The status of upload of the most recently initiated problem report. See Configure PRT Upload for information on configuring an upload rule for problem reports. XML tag in status.xml : PRT_Upload_Status |

| Step 1 | Select Admin Login > advanced > Info > Debug Info . |
|---|---|
| Step 2 | In the Factory Reset section, click Factory Reset . |
| Step 3 | Click Confirm factory reset . |

| Step 1 | Select Voice > Ext(n) . |
|---|---|
| Step 2 | In the Call Feature Settings section, in the Secure Call Option field, choose Optional to retain the current secure call option for the phone, or Required to reject nonsecure calls from other phones. |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Info > Debug Info . |
|---|---|
| Step 2 | In the Problem Report Tool section, click the Start Packet Capture button in the Packet Capture field. |
| Step 3 | Choose Al to capture all packets that the phone receives and select Host IP Address to capture packets only when source or destination is the IP address of the phone. |
| Step 4 | Make phone calls to and from the selected phone. |
| Step 5 | When you want to stop the packet capture, click Stop Packet Capture . |
| Step 6 | Click Submit . You see a file in the Capture File field. This file contains the filtered packets. |

| Step 1 | Click the Voice > Ext n , where n is the phone extension number (1-10) of the phone web dialog. |
|---|---|
| Step 2 | In the Dial Plan area, set the Emergency Number to the digits that correspond to the customer emergency service numbers. To specify multiple emergency numbers, separate each emergency number with a comma. |
| Step 3 | In the E911 Geolocation Configuration area, set the Company UUID to the unique customer identifier obtained from your emergency call service provider. For example: 07072db6-2dd5-4aa1-b2ff-6d588822dd46 |
| Step 4 | Specify the encrypted Primary Request URL to the main georedundant server. This location information server returns the location for this phone. For example: https://prod.blueearth.com/e911Locate/held/held_request.action |
| Step 5 | Specify the encrypted Secondary Request URL for the backup server that can return location information. For example: https://prod2.blueearth.com/e911Locate/held/held_request.action |
| Step 6 | Click Submit All Changes . |

| Step 1 | Select Voice > Ext(n) , where n is an extension number. |
|---|---|
| Step 2 | In the SIP Settings section, set the SIP Transport parameter as described in SIP Settings . |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > System . |
|---|---|
| Step 2 | In the System Configuration section, set the Block Nonproxy SIP field as described in the System Configuration . |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > Extension . |
|---|---|
| Step 2 | In the SIP Settings section, set the Privacy Header field as described in the SIP Settings . |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > Ext (n) . |
|---|---|
| Step 2 | In the SIP Settings section, set the P-Early-Media Support field as described in SIP Settings . |
| Step 3 | Click Submit All Changes . |

| Note | Peer firmware sharing does not function unless multiple phones are set to upgrade at the same time. When a NOTIFY is sent
                                                with Event:resync, it initiates a resync on the phone. Example of an xml that can contain the configurations to initiate the
                                                upgrade: “Event:resync;profile=" http://10.77.10.141/profile.xml When you set the Peer Firmware Sharing Log server to an IP address and port, the PFS specific logs are sent to that server
                                                as UDP messages. This setting must be done on each phone. You can then use the log messages when troubleshooting issues related
                                                to PFS. |
|---|---|

| Step 1 | Select Voice > Provisioning . |
|---|---|
| Step 2 | In the Firmware Upgrade section, set the Peer Firmware Sharing and the Peer Firmware Sharing Log Server fields as described in Firmware Upgrade . |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > Provisioning . |
|---|---|
| Step 2 | In the Configuration Profile section, set the Profile Authentication Type field as described in the Configuration Profile . |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the Programmable Softkeys section, set the Programmable Softkey Enable to Yes . |
| Step 3 | Enter the following values in the Ringing Key List field: answer\|1;ignore\|2;ignoresilent\|3; |
| Step 4 | Click Submit All Changes . |

| Step 1 | Select Voice > Ext(n) . |
|---|---|
| Step 2 | In the XSI Line Service section, set the XSI Host Server , XSI Authentication Type , Login User ID , Login Password , and Anywhere Enable field as described in the XSI Line Service . If you select SIP Credentials for XSI Authentication Type , you need to enter subsriber Auth ID and Password in the Subscriber Information section. |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > Ext(n) . |
|---|---|
| Step 2 | In the XSI Line Service section, set the Block CID Enable field as described in the XSI Line Service . |
| Step 3 | Click Submit All Changes . |

| Step 1 | Select Voice > Phone . |
|---|---|
| Step 2 | In the XSI Phone Service section, set the XSI Host Server , XSI Authentication Type , Login User ID , Login Password , and Directory Enable fields as described in XSI Phone Service . If you select SIP Credentials for XSI Authentication Type , you need to enter SIP Auth ID and SIP Password in this section. |
| Step 3 | Set the CallLog Associated Line and Display Recents From fields as described in XSI Phone Service . Note The Display recents from menu doesn't appear in the Recents phone screen when you set the value of the CallLog Enable field to No , | Note | The Display recents from menu doesn't appear in the Recents phone screen when you set the value of the CallLog Enable field to No , |
| Note | The Display recents from menu doesn't appear in the Recents phone screen when you set the value of the CallLog Enable field to No , |
| Step 4 | Click Submit All Changes . |

| Note | The Display recents from menu doesn't appear in the Recents phone screen when you set the value of the CallLog Enable field to No , |
|---|---|

| Feature Key Sync | DND Enabled | CFWD Enabled | DND Sync | CFWD Sync |
|---|---|---|---|---|
| Yes | Yes | Yes | Yes (SIP) | Yes (SIP) |
| Yes | No | No | Yes (SIP) | Yes (SIP) |
| Yes | No | Yes | Yes (SIP) | Yes (SIP) |
| Yes | No | No | Yes (SIP) | Yes (SIP) |
| No | Yes | Yes | Yes (HTTP) | Yes (HTTP) |
| No | No | Yes | No | Yes (HTTP) |
| No | Yes | No | Yes (HTTP) | No |
| No | No | No | No | No |

| Step 1 | Select Voice > Ext [n] (where [n] is the extension number). |
|---|---|
| Step 2 | In the Call Feature Settings section, set the Feature Key Sync field to Yes . |
| Step 3 | Click Submit All Changes . |

| Note | If XSI sync for call forwarding is enabled and the XSI host server or XSI account is not configured correctly, the phone user
                                             can't forward calls on the phone. |
|---|---|

| Step 1 | Select Voice > Ext [n] (where [n] is the extension number). |
|---|---|
| Step 2 | Set the CFWD Enable field to Yes . |
| Step 3 | Click Submit All Changes . |

| Note | If XSI sync for DND is enabled and the XSI host server or XSI account is not configured correctly, the phone user can't turn
                                             on DND mode on the phone. |
|---|---|

| Step 1 | Select Voice > Ext [n] (where [n] is the extension number). |
|---|---|
| Step 2 | Set the DND Enable field to Yes . |
| Step 3 | Click Submit All Changes . |