---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmemobl-html-f63a5ce693
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmemobl.html
retrieved_at: 2026-08-21T07:23:23.521237+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Extension Mobility

## Chapter: Extension Mobility

# Extension Mobility

This chapter describes features in Cisco Unified Communications Manager Express (Cisco Unified CME) that provide support for
                        phone mobility for end users.

## Prerequisites for Configuring Extension Mobility

Cisco Unified CME 4.2 or a later version.

To use the phone user interface to configure personal speed dials
                                 			 directly on an Extension Mobility phone, Cisco Unified CME 4.3 or a later
                                 			 version must be installed.

SIP phone support is available with Cisco Unified CME 8.6 or a later
                                 			 version.

## Restrictions for Configuring Extension Mobility

Extension Mobility on remote Unified CME routers isn’t supported. You can log in only to a local Cisco Unified IP phone.

Extension Mobility isn’t supported if you log in to a Cisco Unified IP phone in a different subnet.

## Information About Configuring Extension Mobility

### Extension
                           	 Mobility

Extension Mobility
                              		in Cisco Unified CME 4.2 and later versions provides the benefit of phone
                              		mobility for end users.

A user login service
                              		allows phone users to temporarily access a physical phone other than their own
                              		phone and utilize their personal settings, such as directory number, speed-dial
                              		lists, and services, as if the phone is their own desk phone. The phone user
                              		can make and receive calls on that phone using the same personal directory
                              		number as is on their own desk phone.

Each
                              		Cisco Unified IP phone that is enabled for Extension Mobility is configured
                              		with a logout profile. This profile determines the default appearance of a
                              		phone that is enabled for Extension Mobility when there is no phone user logged
                              		into that phone. Minimally, the logout profile allows calls to emergency
                              		services such as 911. A single logout profile can be applied to multiple
                              		phones.

After a
                              		Cisco Unified IP phone that is enabled for Extension Mobility boots up, the
                              		Services feature button on the phone is configured with a login service URL
                              		hosted by Cisco Unified CME that points to the Extension Mobility Login page.
                              		No feature-button-specifc configuration is required to add Extension Assigner
                              		to the Services feature button. The option for Extension Mobility appears last
                              		in the list of options displayed when the phone user presses the Services
                              		feature button

A phone user logs in
                              		to a Cisco Unified IP phone that is enabled for Extension Mobility by pressing
                              		the Services button or a Unified CCX agent can log in using a Unified CCX Cisco
                              		Agent Desktop. User authentication and authorization is performed by Cisco
                              		Unified CME. If the login is successful, Cisco Unified CME retrieves the
                              		appropriate user profile, based on user name and password match, and replaces
                              		the phone’s logout profile with the user profile.

After the phone user
                              		is logged in, the service URL points to a logout URL hosted by
                              		Cisco Unified CME to provide a logout prompt on the phone. Logging into a
                              		different device automatically closes the first session and start a new session
                              		on the new device. When a phone user is not logged in to any phone, incoming
                              		calls to the phone user’s directory number are sent to the phone user’s voice
                              		mailbox.

For button
                              		appearance, Extension Mobility associates directory numbers then speed-dial
                              		numbers in the logout profile or user profile to phone buttons. The sequence in
                              		which directory numbers are associated is based on line type and ring behavior
                              		as follows: first normal, then silent ring, beep ring, feature ring, monitor
                              		ring, and overlay, followed by speed dials. If the profile contains more
                              		numbers than there are buttons on the physical phone to which the profile is
                              		downloaded, the remaining numbers in the profile are ignored.

For configuration
                              		information, see Enable Extension Mobility .

### Personal Speed
                           	 Dials on an Extension Mobility Phone

Unified CME phone users can use the Cisco IOS CLI commands to configure personal speed dials on an Extension Mobility phone.

In Cisco Unified CME 4.3 and later versions, Extension Mobility users can configure their own speed-dial settings directly
                              on the phone. Speed-dial settings are added or modified on the phone by using a menu available with the Services feature button.
                              Any changes to the speed-dial settings made through the phone user interface are applied to the user’s profile in Extension
                              Mobility. For information about using the phone user interface on a Cisco Unified IP phone, see Cisco Unified IP Phone 7900 Series End-User Guides .

The phone user-interface is enabled by default on all phones with displays. You can disable the capability for an individual
                              phone to prevent a phone user from accessing the interface. For configuration information, see Enable Phone User Interface for Configuring Speed-Dial and Fast-Dial .

### Cisco Unified CME
                           	 Extension Mobility Enhancements

Enhancements to
                              		Extension Mobility in Cisco Unified CME 4.3 include the following:

Configurable
                                    			 Automatic Logout

Automatic Clear
                                    			 Call History

#### Automatic
                                 		  Logout

Cisco Unified CME
                                 		  4.3 and later versions includes an Automatic Timeout feature for Extension
                                 		  Mobility. After an automatic logout is executed, Cisco Unified CME sends the
                                 		  logout profile to the phone and restarts the phone. After an automatic logout,
                                 		  Extension Mobility users can log in again.

You can configure
                                 		  up to three different times on a 24-hour clock for automatically logging out
                                 		  Extension Mobility users based on time-of-day. The system clock triggers an
                                 		  alarm at the specified time and the EM Manager in Cisco Unified CME logs outs
                                 		  every logged in Extension Mobility user in the system. If an Extension Mobility
                                 		  user is using the phone when automatic logout occurs, the user is logged out
                                 		  after the active call is completed.

For configuration
                                 		  information, see Configure Cisco Unified CME for Extension Mobility .

Users log out from
                                 		  Extension Mobility by pressing the Services button and choosing Logout. If a
                                 		  user does not manually log out before leaving the phone, the phone is idle and
                                 		  the individual’s user profile remains loaded on that phone. To automatically
                                 		  log out individual users from idle Extension Mobility phones, configure an
                                 		  idle-duration timer for Extension Mobility. The timer monitors the phone and if
                                 		  the specified maximum idle time is exceeded, the EM Manager logs out the user.
                                 		  The idle-duration timer is reset whenever the phone goes offhook.

For configuration
                                 		  information, see Configure a User Profile .

#### Automatic
                                 		  Clear Call History

In
                                 		  Cisco Unified CME 4.3 and later versions, the EM manager in Cisco Unified CME
                                 		  issues commands to phones to clear call history whenever a user logs out of
                                 		  Extension Mobility. An HTTP GET/POST is sent between the Extension Mobility
                                 		  phone and the authentication server in Cisco Unified CME. The authentication
                                 		  server authorizes the request and the call history is cleared based on the
                                 		  result.

You can configure
                                 		  Cisco Unified CME to disable Automatic Clear Call History. For configuration
                                 		  information, see Configure Cisco Unified CME for Extension Mobility .

### Privacy on an
                           	 Extension Mobility Phone

In Cisco Unified CME
                              		4.3 and later versions, the Privacy feature enables phone users to block other
                              		users from seeing call information or barging into a call on a shared octo-line
                              		directory number. When a phone receives an incoming call on a shared octo-line,
                              		the user can make the call private by pressing the Privacy feature button,
                              		which toggles between on and off to allow the user to alter the privacy setting
                              		on their phone. The privacy state is applied to all new calls and current calls
                              		owned by the phone user.

For Extension
                              		Mobility phones, you can enable the privacy button in the user profile and
                              		logout profile. To enable the privacy button, see Configure a Logout Profile for an IP Phone and Configure a User Profile .

For more information about Privacy, see Barge and Privacy .

### Extension Mobility
                           	 for SIP Phones Enhancement

Cisco Unified CME
                              		8.6 enhances the Extension Mobility feature to allow support for SIP phones.

Extension Mobility
                              		allows you to access any EM enabled physical phone and utilize your own
                              		personal settings, such as directory numbers, speed-dials, after-hour personal
                              		identification number (PIN), and feature button layout, as if the phone is your
                              		own desk phone.

A user login service
                              		allows you to temporarily access a physical phone other than your own phone and
                              		utilize your personal settings, such as directory number, speed-dial lists, and
                              		services, as if the phone is your own desk phone.

The features of
                              		Extension Mobility for SIP phones is identical to SCCP phones, only the
                              		configuration procedure is different. For information on configuring Extension
                              		Mobility for SIP phones, see Configure Extension Mobility for SIP Phones .

You can login to
                                          		  either an SCCP phone or a SIP phone with the same user profile.

Only the normal
                                          		  lines configured in your user profile are applied when you login to a SIP
                                          		  phone. Other lines such as overlay, monitor, and feature-ring lines are
                                          		  ignored.

Only Cfwdall,
                                          		  Confrn, DnD, Endcall, Hold, NewcallGroup Pickup, Park, Privacy, Redial, and
                                          		  Trnsfer feature buttons configured in your user profile will be applied when
                                          		  you login to a SIP phone. Other feature buttons will be ignored.

### MIB Support for
                           	 Extension Mobility in Cisco Unified SCCP IP Phones

In Cisco Unified CME
                              		9.0 and later versions, new MIB objects are added to monitor Cisco Unified SCCP
                              		IP Extension Mobility (EM) phones. These enhancements allow the retrieval of
                              		the following information:

user-profile tag
                                    			 for a Cisco Unified SCCP IP EM phone, when it is logged in

logout-profile
                                    			 tag for a Cisco Unified SCCP IP EM phone

DN and its type,
                                    			 and the overlay or call waiting numbers if applicable, for each user-profile

DN and its type,
                                    			 and the overlay or call waiting numbers if applicable, for each logout-profile

number of Cisco
                                    			 Unified SCCP IP phones configured as EM phones

number of
                                    			 registered Cisco Unified SCCP IP EM phones

Table 1 lists the MIB variables and object identifiers for retrieving the new MIB
                              		database.

MIB
                                          				  Variables

Object
                                          				  identifiers

ccmeEMUserProfileTag

1.3.6.1.4.1.9.9.439.1.1.43.1.19

ccmeEMLogOutProfileTag

1.3.6.1.4.1.9.9.439.1.1.43.1.20

ccmeEMUserDirNumConfTable

1.3.6.1.4.1.9.9.439.1.1.68

ccmeEMUserDirNumConfEntry

1.3.6.1.4.1.9.9.439.1.1.68.1

ccmeEMUserDirNum

1.3.6.1.4.1.9.9.439.1.1.68.1.3

ccmeEMUserDirNumOverlay

1.3.6.1.4.1.9.9.439.1.1.68.1.4

ccmeEMLogoutDirNumConfTable

1.3.6.1.4.1.9.9.439.1.1.69

ccmeEMLogoutDirNumConfEntry

1.3.6.1.4.1.9.9.439.1.1.69.1

ccmeEMLogoutDirNum

1.3.6.1.4.1.9.9.439.1.1.69.1.3

ccmeEMLogoutDirNumOverlay

1.3.6.1.4.1.9.9.439.1.1.69.1.4

ccmeEMphoneTot

1.3.6.1.4.1.9.9.439.1.2.9

ccmeEMphoneTotRegistered

1.3.6.1.4.1.9.9.439.1.2.10

Table 2 provides a description of each of the MIB variables for EM in Cisco Unified
                              		SCCP IP Phones.

MIB
                                          				  Variables

Descriptions

ccmeEMUserProfileTag

User-profile tag for the EM phone

ccmeEMLogOutProfileTag

Logout-profile tag for the EM phone

ccmeEMUserDirNumConfTable

Table of
                                          				  entries for the EM phone’s user profile

ccmeEMUserDirNumConfEntry

A
                                          				  user-profile entry for the EM phone

ccmeEMUserDirNum

A
                                          				  directory number for the user profile

ccmeEMUserDirNumOverlay

Number
                                          				  type for the user profile, including the overlay identifier

ccmeEMLogoutDirNumConfTable

Table of
                                          				  entries for the EM phone’s logout profile

ccmeEMLogoutDirNumConfEntry

A logout
                                          				  entry for the EM phone

ccmeEMLogoutDirNum

A
                                          				  directory number for the logout profile

ccmeEMLogoutDirNumOverlay

Number
                                          				  type for the logout profile, including the overlay identifer

ccmeEMphoneTot

Total
                                          				  number of EM phones

ccmeEMphoneTotRegistered

Total
                                          				  number of registered EM phones

Extension mobility
                              		is supported in Cisco Unified CME but not in Cisco Unified SRST.

## Enable Extension Mobility

### Configure
                           	 Cisco Unified CME for Extension Mobility

To configure
                                 		  Extension Mobility in Cisco Unified CME, perform the following steps.

#### Before you begin

For
                                       				authentication server in Cisco Unified CME, Cisco Unified CME 4.3 or a later
                                       				version.

For Automatic
                                       				Logout, Cisco Unified CME 4.3 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- ip http server

- telephony-service

- url authentication url-address application-name password

- service phone webAccess 0

- authentication credential application-name password

- em
                                       				  keep-history

- em logout time1 [ time2 ] [ time3 ]

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

ip http server

#### Example:

```
Router(config)# ip http server
```

Enables the
                                             				HTTP server on the Cisco Unified CME router that hosts the service URL for the
                                             				Extension Mobility Login and Logout pages.

Step 4

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony-service configuration mode.

Step 5

url authentication url-address application-name password

#### Example:

```
Router(config-telephony)# url authentication http://192.0.2.0/CCMCIP/authenticate.asp secretname psswrd
```

or

To support
                                                				  Extension Mobility and VoiceView
                                                				  Express 3.2 or earlier versions

```
Router(config-telephony)# url authentication http://192.0.2.0/voiceview/authentication/authenticate.do secretname psswrd
```

Instructs
                                             				phones to send HTTP requests to the authentication server and specifies which
                                             				credential to use in the requests.

This
                                                   					 command is supported in Cisco Unified CME 4.3 and later versions. Required to
                                                   					 support Automatic Clear Call history.

URL for
                                                   					 internal authentication server in Cisco Unified CME is http:// CME IP Address /CCMCIP/authenticate.asp .

In
                                                         						  Cisco Unified CME: Configure the url
                                                               								authentication command using the URL for Cisco Unity Express. The
                                                         						  URL for Cisco Unity Express is http:// CUE IP Address /voiceview/authentication/authenticate.do .

In
                                                         						  Cisco Unity Express: Configure the fallback-url command using the URL for the authentication server in Cisco Unified CME.

See Examples .

Step 6

service phone webAccess 0

#### Example:

```
Router(config-telephony)# service phone webAccess 0
```

Enables
                                             				webAccess for IP phones. This is required for 9.x firmware because the web
                                             				server is disabled by default. 8.x firmware and lower had the web server
                                             				enabled by default.

Step 7

authentication credential application-name password

#### Example:

```
Router(config-telephony)#authentication credential secretname psswrd
```

(Optional)
                                             				Creates an entry for an application's credential in the database used by the
                                             				Cisco Unified CME authentication server.

This
                                                   					 command is supported in Cisco Unified CME 4.3 and later versions.

Required
                                                   					 to support requests requests from applications other than Extension Mobility,
                                                   					 such as Cisco VoiceView Express.

Step 8

em
                                                				  keep-history

#### Example:

```
Router(config-telephony)# em keep-history
```

(Optional)
                                             				Specifies that Extension Mobility will keep, and not automatically clear, call
                                             				histories when users log out from Extension Mobility phones.

This
                                                   					 command is supported in Cisco Unified CME 4.3 and later versions.

Default:
                                                   					 Automatic Clear Call History is enabled.

Step 9

em logout time1 [ time2 ] [ time3 ]

#### Example:

```
Router(config-telephony)# em logout 19:00 24:00
```

(Optional)
                                             				Defines up to three time-of-day timers for automatically logging out all
                                             				Extension Mobility users.

This
                                                   					 command is supported in Cisco Unified CME 4.3 and later versions.

time —Time
                                                   					 of day after which logged-in users are automatically logged out from Extension
                                                   					 Mobility. Range: 00:00 to 24:00 on a 24-hour clock.

To
                                                   					 configure a idle-duration timer for automatically logging out an individual
                                                   					 user, see Configure a User Profile .

Step 10

end

#### Example:

```
Router(config-telephony)# end
```

Exits
                                             				configuration mode and returns to privileged EXEC mode.

#### Examples

The following
                                 		  example shows how to configure Cisco Unified CME 4.3 or a later version and
                                 		  Cisco Unity Express 3.2 or an earlier version to support Extension Mobility and
                                 		  Cisco VoiceView Express.

When running
                                             			 Extension Mobility and Cisco VoiceView Express 3.2 or an earlier version, you
                                             			 must also configure the fallback-url command in Cisco Unity Express. For configuration
                                             			 information, see the appropriate Cisco Unity Express
                                                				Administrator Guide .

Cisco Unified CME 4.3 or a later version

```
telephony-service 
 url authentication http://192.0.2.0/voiceview/authentication/authenticate.do secretname psswrd 
 authentication credentials secretname psswrd
```

Cisco Unity
                                 		  Express 3.2 or an earlier version

```
service phone-authentication 
 fallback-url http://192.0.2.0/CCMCIP/authenticate.asp?UserID=secretname&Password=psswrd
```

### Configure a Logout
                           	 Profile for an IP Phone

To create a logout profile to define the default appearance for a Cisco Unified IP phone that is enabled for Extension Mobility,
                                 perform the following steps.

Restriction

For button
                                                   				  appearance, Extension Mobility associates directory numbers, then speed-dial
                                                   				  definitions in the logout profile or user profile to phone buttons. The
                                                   				  sequence in which directory numbers are associated is based on line type and
                                                   				  ring behavior as follows: first normal, then silent ring, beep ring, feature
                                                   				  ring, monitor ring, and overlay, followed by speed dials. If the profile
                                                   				  contains more directory numbers and speed-dial numbers than there are buttons
                                                   				  on the physical phone to which the profile is downloaded, not all numbers are
                                                   				  downloaded to buttons.

The first
                                                   				  number to be configured for line appearance cannot be a monitored directory
                                                   				  number.

The user name parameter of any authentication credential must be unique. Do not use the same value for a user name when you
                                                   configure any two or more authentication credentials in Cisco Unified CME, such as the user name in a logout or user profile
                                                   for Extension Mobility.

#### Before you begin

All directory numbers to be included in a logout profile or a user profile must be already configured in Cisco Unified CME.
                                       For configuration information, see Configure Phones to Make Basic Call .

For Privacy, on extension mobility phones, requires Cisco Unified 4.3 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice logout-profile profile-tag

- user name password password

- number number type type

- speed-dial speed-tag number [ label label ] [ blf ]

- pin number

- privacy-button

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

voice logout-profile profile-tag

#### Example:

```
Router(config)# voice logout-profile 1
```

Enters voice logout-profile configuration mode for creating a logout profile to define the default appearance for a Cisco
                                             Unified IP phone enabled for Extension Mobility.

profile-tag —Unique number that identifies this profile during configuration tasks. Range: 1 to maximum number of phones supported by
                                                   the Cisco Unified CME router. Type ? to display the maximum number.

Step 4

user name password password

#### Example:

```
Router(config-logout-profile)# user 23C2-8 password 43214
```

Creates credential to be used by a TAPI phone device to log into Cisco Unified CME.

name —Unique alphanumeric string to identify a user
                                                   					 for this authentication credential only.

password —Alphanumeric string.

Step 5

number number type type

#### Example:

```
Router(config-logout-profile)# number 3001 type silent-ring
Router(config-logout-profile)# number 3002 type beep-ring
Router(config-logout-profile)# number 3003 type feature-ring
Router(config-logout-profile)# number 3004 type monitor-ring
Router(config-logout-profile)# number 3005,3006 type overlay
Router(config-logout-profile)# number 3007,3008 type cw-overly
```

Creates line
                                             				definition.

number —Directory number to be associated with and displayed next to a button on a Cisco Unified IP phone that is configured with
                                                   this profile.

[ , ...number ]—(Optional) For overlay lines only, with
                                                   					 or without call waiting. The directory number that is the far left in command
                                                   					 list is the highest priority. Can contain up to 25 numbers. Individual numbers
                                                   					 must be separated by commas ( , ).

type type —Denotes characteristics to be associated with
                                                   					 this line. Type ? for list of
                                                   					 options.

Step 6

speed-dial speed-tag number [ label label ] [ blf ]

#### Example:

```
Router(config-logout-profile)# speed-dial 1 2001
Router(config-logout-profile)# speed-dial 2 2002 blf
```

(Optional) Creates speed-dial definition.

speed-tag —Unique sequence number that identifies a speed-dial definition during configuration tasks. Range: 1 to 36.

number —Digits to be dialed when the speed-dial button is pressed.

label label —(Optional) String that contains identifying text to be displayed next to the speed-dial button. Enclose the string in quotation
                                                   marks if the string contains a space.

blf —(Optional) Enables Busy Lamp Field (BLF) monitoring for a speed-dial number.

Step 7

pin number

#### Example:

```
Router(config-logout-profile)# pin 1234
```

Sets a personal identification number (PIN) to be used by a phone user to disable the call blocking configuration for a Cisco
                                             Unified IP phone on which this profile is downloaded.

number —Numeric string containing four to eight digits.

Step 8

privacy-button

#### Example:

```
Router(config-logout-profile)# privacy-button
```

(Optional)
                                             				Enables the privacy feature button on the IP phone.

Enable
                                                   					 this command only on phones that share an octo-line directory number.

This command is supported in Cisco Unified CME 4.3 and later versions.

Step 9

end

#### Example:

```
Router(config-logout-profile)# end
```

Exits to
                                             				privileged EXEC mode.

### Enable an IP Phone
                           	 for Extension Mobility

To enable the
                                 		  Extension Mobility feature on an individual Cisco Unified IP phone in
                                 		  Cisco Unified CME, perform the following steps.

All SCCP Cisco
                                             			 Unified IP phones with displays that support URL provisioning for Feature
                                             			 buttons are supported by Extension Mobility, including the Cisco Unified
                                             			 Wireless IP Phone 7920, Cisco Unified Wireless IP Phone 7921, and Cisco IP
                                             			 Communicator.

Restriction

Extension
                                                   				  Mobility is not supported on Cisco Unified IP phones without phone screens.

Extension
                                                   				  Mobility is not supported for analog devices.

#### Before you begin

HTTP server is
                                       				enabled on the Cisco Unified CME router. For configuration information, see Configure Cisco Unified CME for Extension Mobility .

Logout profile
                                       				to be assigned to a phone must be configured in Cisco Unified CME.

Cisco IP
                                       				Communicator to be enabled for Extension Mobility must be already registered in
                                       				Cisco Unified CME.

### SUMMARY STEPS

- enable

- configure terminal

- ephone phone-tag

- mac-address mac-address

- type phone-type

- logout-profile profile-tag

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

Enables phone
                                             				configuration mode.

phone-tag —Unique number that identifies this phone
                                                   					 during configuration tasks. Range is 1 to maximum number supported phones,
                                                   					 where maximum is platform and version dependent and defined by using the max-ephone command.

Step 4

mac-address mac-address

#### Example:

```
Router(config-ephone)# mac-address 000D.EDAB.3566
```

Associates a
                                             				physical phone with this ephone configuration.

Step 5

type phone-type

#### Example:

```
Router(config-ephone)# type 7960
```

Defines a
                                             				phone type for the phone being configured.

Step 6

logout-profile profile-tag

#### Example:

```
Router(config-ephone)# logout-profile 1
```

Enables
                                             				Cisco Unified IP phone for Extension Mobility and assigns a logout profile to
                                             				this phone.

tag —Unique identifier of logout profile to be used
                                                   					 when no phone user is logged in to this phone. This tag number corresponds to a
                                                   					 tag number created when this logout profile was configured by using the voice
                                                         						  logout-profile command.

Step 7

end

#### Example:

```
Router(config-ephone)# end
```

Exits to
                                             				privileged EXEC mode.

### Configure
                           	 Extension Mobility for SIP Phones

To prepare
                                 		  Extension Mobility for use with SIP phones, perform the following steps.

#### Before you begin

Cisco IOS
                                       				Release 15.1(4)M.

Cisco Unified
                                       				CME 8.6 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- ip http server

- voice register global

- url authentication url-address

- exit

- telephony-service

- authentication credential application-name password

- em keep-history

- em logout time1 [ time2 ] [ time3 ]

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

ip http server

#### Example:

```
Router(config)# ip http server
```

Enables the
                                             				HTTP server on the Cisco Unified CME router which hosts the service URL for the
                                             				Extension Mobility login and logout pages.

Step 4

voice register global

#### Example:

```
Router(config)# voice register global
```

Defines global
                                             				voice register commands.

Step 5

url authentication url-address

#### Example:

```
Router(config-register-global)# url authentication http://192.0.2.0/CCMCIP/authenticate.asp
```

Instructs phones to send HTTP requests to the authentication server and the information at the specified URL is used to validate
                                             requests made to the phone web server.

Required to support Automatic Clear Call history.

URL—URL address for the authentication server in Cisco Unified CME is http:// CME IP Address /CCMCIP/authenticate.asp .

Step 6

exit

#### Example:

```
Router(config-register-global)# exit
```

Exits voice
                                             				register global confiuration mode.

Step 7

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony service configuration mode.

Step 8

authentication credential application-name password

#### Example:

```
Router(config-telephony)# authentication credential application-name password
```

Specifies
                                             				authorized credentials. Use credentials from Step 5.

This step is
                                                         				  needed only when you set the CME internal authentication server as your phone
                                                         				  authentication server in Step 5.

Step 9

em keep-history

#### Example:

```
Router(config-telephony)# em keep-history
```

(Optional)
                                             				Specifies that Extension Mobility will keep, and not automatically clear, call
                                             				histories when users log out from Extension Mobility phones.

Default:
                                                         				  Automatic Clear Call History is enabled.

Step 10

em logout time1 [ time2 ] [ time3 ]

#### Example:

```
Router(config-telephony)# em logout 19:00 24:00
```

(Optional)
                                             				Defines up to three time-of-day timers for automatically logging out all
                                             				Extension Mobility users.

time —Time
                                                   					 of day after which logged-in users are automatically logged out from Extension
                                                   					 Mobility. Range: 00:00 to 24:00 on a 24-hour clock.

Step 11

end

#### Example:

```
Router(config-telephony)# end
```

Returns to
                                             				privileged EXEC mode.

### Enable SIP Phones
                           	 for Extension Mobility

To enable the
                                 		  Extension Mobility feature on a SIP phone in Cisco Unified CME, perform the
                                 		  following steps.

All Cisco
                                             			 Unified SIP phones with displays that support URL provisioning are supported by
                                             			 Extension Mobility.

#### Before you begin

HTTP server is
                                       				enabled on the Cisco Unified CME router.

Default logout
                                       				and user profiles to be assigned to a phone must be configured in Cisco Unified
                                       				CME.

The voice
                                       				register directory numbers in default logout and user profiles must be
                                       				configured in Cisco Unified CME. To configure SIP directory numbers, see Cisco Unified Communications Manager Express Command Reference
                                          				  Guide .

### SUMMARY STEPS

- enable

- configure terminal

- voice register pool pool-tag

- id mac mac-address

- type phone-type

- logout-profile profile-tag

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
Router(config)# voice register pool 22
```

Enables phone
                                             				configuration mode.

pool-tag—Unique number that identifies this register pool during
                                                   					 configuration tasks. Range is 1 to 42.

Step 4

id mac mac-address

#### Example:

```
Router(config-register-pool)# id mac 0123.4567.89AB
```

Associates a
                                             				physical phone with this ephone configuration.

mac-address—mac address of the physical phone

Step 5

type phone-type

#### Example:

```
Router(config-register-pool)# type 7970
```

Defines a
                                             				phone type for the phone being configured.

Step 6

logout-profile profile-tag

#### Example:

```
Router(config-register-pool)# logout-profile 22
```

Enables
                                             				Cisco Unified SIP phone for Extension Mobility and assigns a logout profile to
                                             				this phone.

profile
                                                   					 tag—Unique identifier of a logout profile to be used when no phone user is
                                                   					 logged in to this phone. This tag number corresponds to a tag number created
                                                   					 when this logout profile was configured by using the voice
                                                         						  logout-profile command.

Step 7

end

#### Example:

```
Router(config-ephone)# end
```

Exits to
                                             				privileged EXEC mode.

### Configure a User
                           	 Profile

To configure a
                                 		  user profile for a phone user who logs into a Cisco Unified IP phone that is
                                 		  enabled for Extension Mobility, perform the following steps.

Templates
                                             			 created using the ephone-template and ephone-dn-template commands can be applied to a
                                             			 user profile for Extension Mobility.

Restriction

For button
                                                   				  appearance, Extension Mobility associates directory numbers, then speed-dial
                                                   				  definitions in the logout profile or user profile to phone buttons. The
                                                   				  sequence in which directory numbers are associated is based on line type and
                                                   				  ring behavior as follows: first normal, then silent ring, beep ring, feature
                                                   				  ring, monitor ring, and overlay, followed by speed dials. If the profile
                                                   				  contains more directory numbers and speed-dial numbers than there are buttons
                                                   				  on the physical phone to which the profile is downloaded, not all numbers are
                                                   				  downloaded to buttons.

The first
                                                   				  number to be configured for line appearance cannot be a monitored directory
                                                   				  number.

The user name parameter of any authentication credential must be unique. Do not use the same value for a user name when you
                                                   configure any two or more authentication credentials in Cisco Unified CME, such as the user name in a logout or user profile
                                                   for Extension Mobility.

#### Before you begin

All directory
                                       				numbers to be included in a logout profile or user profile must be already
                                       				configured in Cisco Unified CME. For configuration information, see Configure Phones to Make Basic Call .

For Automatic
                                       				Logout, Cisco Unified CME 4.3 or a later version.

For Privacy on
                                       				extension mobility phones, Cisco Unified CME 4.3 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice user-profile profile-tag

- user name password password

- number number type type

- speed-dial speed-tag number [ label label ] [ blf ]

- pin number

- max-idle-time minutes

- privacy-button

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

voice user-profile profile-tag

#### Example:

```
Router(config)# voice user-profile 1
```

Enters voice
                                             				user-profile configuration mode for configuring a user profile for Extension
                                             				Mobility.

profile-tag —Unique number that identifies this
                                                   					 profile during configuration tasks. Range: 1 to three times the maximum number
                                                   					 supported phones, where maximum is platform dependent. Type ? to display
                                                   					 value.

Step 4

user name password password

#### Example:

```
Router(config-user-profile)# user me password pass123
```

Creates
                                             				credential to be authenticated by Cisco Unified CME before allowing the phone
                                             				user to log into a Cisco Unified IP phone phone enabled for Extension Mobility.

name —Unique alphanumeric string to identify a user
                                                   					 for this authentication credential only.

password —Password for authorized user.

Step 5

number number type type

#### Example:

```
Router(config-user-profile)# number 2001 type silent-ring 
				Router(config-user-profile)# number 2002 type beep-ring 
				Router(config-user-profile)# number 2003 type feature-ring
				Router(config-user-profile)# number 2004 type monitor-ring 
				Router(config-user-profile)# number 2005,2006 type overlay 
				Router(config-user-profile)# number 2007,2008 type cw-overly
```

Creates line
                                             				definition.

number —Directory number to be associated with and
                                                   					 displayed next to a button on a phone that is configured with this profile.

[ , ...number ]—(Optional) For overlay lines only, with
                                                   					 or without call waiting. The directory number that is far left in the command
                                                   					 list is given the highest priority. Can contain up to 25 numbers. Individual
                                                   					 numbers must be separated by commas ( , )

type type —Denotes characteristics to be associated with
                                                   					 this line. Type ? for list of options.

Step 6

speed-dial speed-tag number [ label label ] [ blf ]

#### Example:

```
Router(config-user-profile)# speed-dial 1 3001 
				Router(config-user-profile)# speed-dial 2 3002 blf
```

Creates
                                             				speed-dial definition.

speed-tag —Unique sequence number that identifies a
                                                   					 speed-dial definition during configuration tasks. Range: 1 to 36.

number —Digits to be dialed when the speed-dial
                                                   					 button is pressed.

label label —(Optional) String that contains identifying
                                                   					 text to be displayed next to the speed-dial button. Enclose the string in
                                                   					 quotation marks if the string contains a space.

blf —(Optional) Enables Busy Lamp Field (BLF)
                                                   					 monitoring for a speed-dial number.

Step 7

pin number

#### Example:

```
Router(config-user-profile)# pin 12341
```

Sets a
                                             				personal identification number (PIN) to be used by a phone user to disable the
                                             				call blocking configuration for a Cisco Unified IP phone on which this profile
                                             				is downloaded.

number —Numeric string containing four to eight
                                                   					 digits.

Step 8

max-idle-time minutes

#### Example:

```
Router(config-user-profile)# max-idle-time 30
```

(Optional)
                                             				Creates an idle-duration timer for automatically logging out an Extension
                                             				Mobility user.

This
                                                   					 command is supported in Cisco Unified CME 4.3 and later versions.

minutes —Maximum number of minutes after which a
                                                   					 user is logged out from an idle Extension Mobility phone. Range:1 to 9999.

Step 9

privacy-button

#### Example:

```
Router(config-user-profile)# privacy-button
```

(Optional)
                                             				Enables the privacy feature button on the IP phone.

Enable
                                                   					 this command only on phones that share an octo-line directory number.

This
                                                   					 command is supported in Cisco Unified CME 4.3 and later versions.

Step 10

end

#### Example:

```
Router(config-user-profile)# end
```

Exits to
                                             				privileged EXEC mode.

## Configuration Examples for Extension Mobility

### Example for Configuring Extension Mobility for Use with SIP
                           	 Phones

The following example shows a sample configuration for enabling
                                 		  Extension Mobility for use with SIP phones:

```
Router#en
Router#conf t
Enter configuration commands, one per line.  End with CNTL/Z.

Router(config)#ip http server
Router(config)#voice register global
Router(config-register-global)#$.2.0/CCMCIP/authenticate.asp admin password
Router(config-register-global)#exit
Router(config)#telephony-service
Router(config-telephony)#authentication credential admin password
Router(config-telephony)#em keep-history
Router(config-telephony)#em logout 19:00
Router(config-telephony)#end
```

### Example for
                           	 Configuring SIP Phones for Use with Extension Mobility

The following
                                 		  example shows a sample configuration for enabling a SIP phone to use Extension
                                 		  Mobility:

```
Router#en
Router#conf t
Enter configuration commands, one per line.  End with CNTL/Z.

Router#en
Router#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#voice register pool 1
Router(config-register-pool)#id mac 12.34.56
Router(config-register-pool)#type 7960
Router(config-register-pool)#logout-profile 22
Enabling extension mobility will replace current phone configuration with logout
 profile, continue?? [yes]: y
Router(config-register-pool)#end
```

### Example for Configuring Logout Profile

The following example shows the configuration for a logout profile
                                 		  that defines the default appearance for a Cisco Unified IP phone that is
                                 		  enabled for Extension Mobility. Which lines and speed-dial buttons in this
                                 		  profile are configured on a phone depends on the phone type. For example, for a
                                 		  Cisco Unified IP Phone 7970, all buttons are configured according to logout
                                 		  profile1. However, if the phone is a Cisco Unified IP Phone 7960, all six lines
                                 		  are mapped to phone buttons and the speed dial is ignored because there is no
                                 		  button available for speed dial.

```
voice logout-profile 1
 pin 9999
 user 23C2-8 password 43214
 number 3001 type silent-ring
 number 3002 type beep-ring
 number 3003 type feature-ring
 number 3004 type monitor-ring
 number 3005,3006 type overlay
 number 3007,3008 type cw-overly
 speed-dial 1 2000
 speed-dial 2 2001 blf
```

### Example for Enabling an IP Phone for Extension Mobility

The following example shows the ephone configurations for three IP
                                 		  phones. All three phones are enabled for Extension Mobility and share the same
                                 		  logout profile number 1, to be downloaded when these phones boot and when no
                                 		  phone user is logged into the phone.

```
ephone 1
 mac-address 000D.EDAB.3566
 type 7960
 logout-profile 1
 
ephone 2
 mac-address 0012.DA8A.C43D
 type 7970
 logout-profile 1
 
ephone 3
 mac-address 1200.80FC.9B01
 type 7911
 logout-profile 1
```

### Example for Configuring User Profile

The following example shows the configuration for a user profile to be
                                 		  downloaded when a phone user logs into a Cisco Unified IP phone that is enabled
                                 		  for Extension Mobility. Which lines and speed-dial buttons in this profile are
                                 		  configured on a phone after the user logs in depends on the phone type. For
                                 		  example, if the user logs into a Cisco Unified IP Phone 7970, all buttons are
                                 		  configured according to voice-user profile1. However, if the phone user logs
                                 		  into a Cisco Unified IP Phone 7960, all six lines are mapped to phone buttons
                                 		  and the speed dial is ignored because there is no button available for speed
                                 		  dial.

```
voice user-profile 1
 pin 12345
 user me password pass123
 number 2001 type silent-ring
 number 2002 type beep-ring
 number 2003 type feature-ring
 number 2004 type monitor-ring
 number 2005,2006 type overlay
 number 2007,2008 type cw-overly
 speed-dial 1 3001
 speed-dial 2 3002 blf
```

## Where to Go
                        	 Next

If you created a
                                 			 new or modified an existing logout or user profile, you must restart the phones
                                 			 to propagate the changes. See Reset and Restart Cisco Unified IP Phones .

If you enabled
                                 			 one or more Cisco Unified IP phones for Extension Mobility, generate a new
                                 			 configuration file and restart the phones. See Configuration Files for Phones .

## Feature
                        	 Information for Extension Mobility

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature
                                             					 Name

Cisco Unified CME Version

Modification

MIB
                                             					 Support for Extension Mobility in Cisco Unified SCCP IP Phones

9.0

Adds new
                                             					 MIB objects to monitor Cisco Unified SCCP IP EM phones.

Support
                                             					 for SIP phones

8.6

Adds
                                             					 support for SIP phones.

Extension
                                             					 Mobility Enhancement

7.0/4.3

Adds
                                             					 support for the following:

Automatic Logout, including:

Configurable time-of-day timers for automatically logging out
                                                   						  all Extension Mobility users.

Configurable idle-duration timer for logging out an individual
                                                   						  user from an idle Extension Mobility phone.

Automatic Clear Call History when a user logs out from Extension
                                                   						  Mobility.

Phone
                                             					 User-Interface for Speed Dial

7.0/4.3

Adds a
                                             					 phone user interface allowing Extension Mobility users to configure their own
                                             					 speed-dial settings directly on the phone.

Extension
                                             					 Mobility

4.2

Provides
                                             					 the benefit of phone mobility for end users by enabling the user to log into
                                             					 any local Cisco Unified IP Phone that is enabled for Extension Mobility.

| Note | You can login to
                                          		  either an SCCP phone or a SIP phone with the same user profile. |
|---|---|

| Note | Only the normal
                                          		  lines configured in your user profile are applied when you login to a SIP
                                          		  phone. Other lines such as overlay, monitor, and feature-ring lines are
                                          		  ignored. |
|---|---|

| Note | Only Cfwdall,
                                          		  Confrn, DnD, Endcall, Hold, NewcallGroup Pickup, Park, Privacy, Redial, and
                                          		  Trnsfer feature buttons configured in your user profile will be applied when
                                          		  you login to a SIP phone. Other feature buttons will be ignored. |
|---|---|

| MIB
                                          				  Variables | Object
                                          				  identifiers |
|---|---|
| ccmeEMUserProfileTag | 1.3.6.1.4.1.9.9.439.1.1.43.1.19 |
| ccmeEMLogOutProfileTag | 1.3.6.1.4.1.9.9.439.1.1.43.1.20 |
| ccmeEMUserDirNumConfTable | 1.3.6.1.4.1.9.9.439.1.1.68 |
| ccmeEMUserDirNumConfEntry | 1.3.6.1.4.1.9.9.439.1.1.68.1 |
| ccmeEMUserDirNum | 1.3.6.1.4.1.9.9.439.1.1.68.1.3 |
| ccmeEMUserDirNumOverlay | 1.3.6.1.4.1.9.9.439.1.1.68.1.4 |
| ccmeEMLogoutDirNumConfTable | 1.3.6.1.4.1.9.9.439.1.1.69 |
| ccmeEMLogoutDirNumConfEntry | 1.3.6.1.4.1.9.9.439.1.1.69.1 |
| ccmeEMLogoutDirNum | 1.3.6.1.4.1.9.9.439.1.1.69.1.3 |
| ccmeEMLogoutDirNumOverlay | 1.3.6.1.4.1.9.9.439.1.1.69.1.4 |
| ccmeEMphoneTot | 1.3.6.1.4.1.9.9.439.1.2.9 |
| ccmeEMphoneTotRegistered | 1.3.6.1.4.1.9.9.439.1.2.10 |

| MIB
                                          				  Variables | Descriptions |
|---|---|
| ccmeEMUserProfileTag | User-profile tag for the EM phone |
| ccmeEMLogOutProfileTag | Logout-profile tag for the EM phone |
| ccmeEMUserDirNumConfTable | Table of
                                          				  entries for the EM phone’s user profile |
| ccmeEMUserDirNumConfEntry | A
                                          				  user-profile entry for the EM phone |
| ccmeEMUserDirNum | A
                                          				  directory number for the user profile |
| ccmeEMUserDirNumOverlay | Number
                                          				  type for the user profile, including the overlay identifier |
| ccmeEMLogoutDirNumConfTable | Table of
                                          				  entries for the EM phone’s logout profile |
| ccmeEMLogoutDirNumConfEntry | A logout
                                          				  entry for the EM phone |
| ccmeEMLogoutDirNum | A
                                          				  directory number for the logout profile |
| ccmeEMLogoutDirNumOverlay | Number
                                          				  type for the logout profile, including the overlay identifer |
| ccmeEMphoneTot | Total
                                          				  number of EM phones |
| ccmeEMphoneTotRegistered | Total
                                          				  number of registered EM phones |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ip http server Example: Router(config)# ip http server | Enables the
                                             				HTTP server on the Cisco Unified CME router that hosts the service URL for the
                                             				Extension Mobility Login and Logout pages. |
| Step 4 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 5 | url authentication url-address application-name password Example: Router(config-telephony)# url authentication http://192.0.2.0/CCMCIP/authenticate.asp secretname psswrd or To support
                                                				  Extension Mobility and VoiceView
                                                				  Express 3.2 or earlier versions Router(config-telephony)# url authentication http://192.0.2.0/voiceview/authentication/authenticate.do secretname psswrd | Instructs
                                             				phones to send HTTP requests to the authentication server and specifies which
                                             				credential to use in the requests. This
                                                   					 command is supported in Cisco Unified CME 4.3 and later versions. Required to
                                                   					 support Automatic Clear Call history. URL for
                                                   					 internal authentication server in Cisco Unified CME is http:// CME IP Address /CCMCIP/authenticate.asp . To support Extension
                                                				  Mobility and Cisco VoiceView Express 3.2 or an earlier version only: In
                                                         						  Cisco Unified CME: Configure the url
                                                               								authentication command using the URL for Cisco Unity Express. The
                                                         						  URL for Cisco Unity Express is http:// CUE IP Address /voiceview/authentication/authenticate.do . In
                                                         						  Cisco Unity Express: Configure the fallback-url command using the URL for the authentication server in Cisco Unified CME. See Examples . |
| Step 6 | service phone webAccess 0 Example: Router(config-telephony)# service phone webAccess 0 | Enables
                                             				webAccess for IP phones. This is required for 9.x firmware because the web
                                             				server is disabled by default. 8.x firmware and lower had the web server
                                             				enabled by default. |
| Step 7 | authentication credential application-name password Example: Router(config-telephony)#authentication credential secretname psswrd | (Optional)
                                             				Creates an entry for an application's credential in the database used by the
                                             				Cisco Unified CME authentication server. This
                                                   					 command is supported in Cisco Unified CME 4.3 and later versions. Required
                                                   					 to support requests requests from applications other than Extension Mobility,
                                                   					 such as Cisco VoiceView Express. |
| Step 8 | em
                                                				  keep-history Example: Router(config-telephony)# em keep-history | (Optional)
                                             				Specifies that Extension Mobility will keep, and not automatically clear, call
                                             				histories when users log out from Extension Mobility phones. This
                                                   					 command is supported in Cisco Unified CME 4.3 and later versions. Default:
                                                   					 Automatic Clear Call History is enabled. |
| Step 9 | em logout time1 [ time2 ] [ time3 ] Example: Router(config-telephony)# em logout 19:00 24:00 | (Optional)
                                             				Defines up to three time-of-day timers for automatically logging out all
                                             				Extension Mobility users. This
                                                   					 command is supported in Cisco Unified CME 4.3 and later versions. time —Time
                                                   					 of day after which logged-in users are automatically logged out from Extension
                                                   					 Mobility. Range: 00:00 to 24:00 on a 24-hour clock. To
                                                   					 configure a idle-duration timer for automatically logging out an individual
                                                   					 user, see Configure a User Profile . |
| Step 10 | end Example: Router(config-telephony)# end | Exits
                                             				configuration mode and returns to privileged EXEC mode. |

| Note | When running
                                             			 Extension Mobility and Cisco VoiceView Express 3.2 or an earlier version, you
                                             			 must also configure the fallback-url command in Cisco Unity Express. For configuration
                                             			 information, see the appropriate Cisco Unity Express
                                                				Administrator Guide . |
|---|---|

| Restriction | For button
                                                   				  appearance, Extension Mobility associates directory numbers, then speed-dial
                                                   				  definitions in the logout profile or user profile to phone buttons. The
                                                   				  sequence in which directory numbers are associated is based on line type and
                                                   				  ring behavior as follows: first normal, then silent ring, beep ring, feature
                                                   				  ring, monitor ring, and overlay, followed by speed dials. If the profile
                                                   				  contains more directory numbers and speed-dial numbers than there are buttons
                                                   				  on the physical phone to which the profile is downloaded, not all numbers are
                                                   				  downloaded to buttons. The first
                                                   				  number to be configured for line appearance cannot be a monitored directory
                                                   				  number. The user name parameter of any authentication credential must be unique. Do not use the same value for a user name when you
                                                   configure any two or more authentication credentials in Cisco Unified CME, such as the user name in a logout or user profile
                                                   for Extension Mobility. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice logout-profile profile-tag Example: Router(config)# voice logout-profile 1 | Enters voice logout-profile configuration mode for creating a logout profile to define the default appearance for a Cisco
                                             Unified IP phone enabled for Extension Mobility. profile-tag —Unique number that identifies this profile during configuration tasks. Range: 1 to maximum number of phones supported by
                                                   the Cisco Unified CME router. Type ? to display the maximum number. |
| Step 4 | user name password password Example: Router(config-logout-profile)# user 23C2-8 password 43214 | Creates credential to be used by a TAPI phone device to log into Cisco Unified CME. name —Unique alphanumeric string to identify a user
                                                   					 for this authentication credential only. password —Alphanumeric string. |
| Step 5 | number number type type Example: Router(config-logout-profile)# number 3001 type silent-ring
Router(config-logout-profile)# number 3002 type beep-ring
Router(config-logout-profile)# number 3003 type feature-ring
Router(config-logout-profile)# number 3004 type monitor-ring
Router(config-logout-profile)# number 3005,3006 type overlay
Router(config-logout-profile)# number 3007,3008 type cw-overly | Creates line
                                             				definition. number —Directory number to be associated with and displayed next to a button on a Cisco Unified IP phone that is configured with
                                                   this profile. [ , ...number ]—(Optional) For overlay lines only, with
                                                   					 or without call waiting. The directory number that is the far left in command
                                                   					 list is the highest priority. Can contain up to 25 numbers. Individual numbers
                                                   					 must be separated by commas ( , ). type type —Denotes characteristics to be associated with
                                                   					 this line. Type ? for list of
                                                   					 options. |
| Step 6 | speed-dial speed-tag number [ label label ] [ blf ] Example: Router(config-logout-profile)# speed-dial 1 2001
Router(config-logout-profile)# speed-dial 2 2002 blf | (Optional) Creates speed-dial definition. speed-tag —Unique sequence number that identifies a speed-dial definition during configuration tasks. Range: 1 to 36. number —Digits to be dialed when the speed-dial button is pressed. label label —(Optional) String that contains identifying text to be displayed next to the speed-dial button. Enclose the string in quotation
                                                   marks if the string contains a space. blf —(Optional) Enables Busy Lamp Field (BLF) monitoring for a speed-dial number. |
| Step 7 | pin number Example: Router(config-logout-profile)# pin 1234 | Sets a personal identification number (PIN) to be used by a phone user to disable the call blocking configuration for a Cisco
                                             Unified IP phone on which this profile is downloaded. number —Numeric string containing four to eight digits. |
| Step 8 | privacy-button Example: Router(config-logout-profile)# privacy-button | (Optional)
                                             				Enables the privacy feature button on the IP phone. Enable
                                                   					 this command only on phones that share an octo-line directory number. This command is supported in Cisco Unified CME 4.3 and later versions. |
| Step 9 | end Example: Router(config-logout-profile)# end | Exits to
                                             				privileged EXEC mode. |

| Note | All SCCP Cisco
                                             			 Unified IP phones with displays that support URL provisioning for Feature
                                             			 buttons are supported by Extension Mobility, including the Cisco Unified
                                             			 Wireless IP Phone 7920, Cisco Unified Wireless IP Phone 7921, and Cisco IP
                                             			 Communicator. |
|---|---|

| Restriction | Extension
                                                   				  Mobility is not supported on Cisco Unified IP phones without phone screens. Extension
                                                   				  Mobility is not supported for analog devices. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone phone-tag Example: Router(config)# ephone 1 | Enables phone
                                             				configuration mode. phone-tag —Unique number that identifies this phone
                                                   					 during configuration tasks. Range is 1 to maximum number supported phones,
                                                   					 where maximum is platform and version dependent and defined by using the max-ephone command. |
| Step 4 | mac-address mac-address Example: Router(config-ephone)# mac-address 000D.EDAB.3566 | Associates a
                                             				physical phone with this ephone configuration. |
| Step 5 | type phone-type Example: Router(config-ephone)# type 7960 | Defines a
                                             				phone type for the phone being configured. |
| Step 6 | logout-profile profile-tag Example: Router(config-ephone)# logout-profile 1 | Enables
                                             				Cisco Unified IP phone for Extension Mobility and assigns a logout profile to
                                             				this phone. tag —Unique identifier of logout profile to be used
                                                   					 when no phone user is logged in to this phone. This tag number corresponds to a
                                                   					 tag number created when this logout profile was configured by using the voice
                                                         						  logout-profile command. |
| Step 7 | end Example: Router(config-ephone)# end | Exits to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Note Enter your
                                                         				  password if prompted. | Note | Enter your
                                                         				  password if prompted. |
| Note | Enter your
                                                         				  password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ip http server Example: Router(config)# ip http server | Enables the
                                             				HTTP server on the Cisco Unified CME router which hosts the service URL for the
                                             				Extension Mobility login and logout pages. |
| Step 4 | voice register global Example: Router(config)# voice register global | Defines global
                                             				voice register commands. |
| Step 5 | url authentication url-address Example: Router(config-register-global)# url authentication http://192.0.2.0/CCMCIP/authenticate.asp | Instructs phones to send HTTP requests to the authentication server and the information at the specified URL is used to validate
                                             requests made to the phone web server. Required to support Automatic Clear Call history. URL—URL address for the authentication server in Cisco Unified CME is http:// CME IP Address /CCMCIP/authenticate.asp . |
| Step 6 | exit Example: Router(config-register-global)# exit | Exits voice
                                             				register global confiuration mode. |
| Step 7 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony service configuration mode. |
| Step 8 | authentication credential application-name password Example: Router(config-telephony)# authentication credential application-name password | Specifies
                                             				authorized credentials. Use credentials from Step 5. Note This step is
                                                         				  needed only when you set the CME internal authentication server as your phone
                                                         				  authentication server in Step 5. | Note | This step is
                                                         				  needed only when you set the CME internal authentication server as your phone
                                                         				  authentication server in Step 5. |
| Note | This step is
                                                         				  needed only when you set the CME internal authentication server as your phone
                                                         				  authentication server in Step 5. |
| Step 9 | em keep-history Example: Router(config-telephony)# em keep-history | (Optional)
                                             				Specifies that Extension Mobility will keep, and not automatically clear, call
                                             				histories when users log out from Extension Mobility phones. Note Default:
                                                         				  Automatic Clear Call History is enabled. | Note | Default:
                                                         				  Automatic Clear Call History is enabled. |
| Note | Default:
                                                         				  Automatic Clear Call History is enabled. |
| Step 10 | em logout time1 [ time2 ] [ time3 ] Example: Router(config-telephony)# em logout 19:00 24:00 | (Optional)
                                             				Defines up to three time-of-day timers for automatically logging out all
                                             				Extension Mobility users. time —Time
                                                   					 of day after which logged-in users are automatically logged out from Extension
                                                   					 Mobility. Range: 00:00 to 24:00 on a 24-hour clock. |
| Step 11 | end Example: Router(config-telephony)# end | Returns to
                                             				privileged EXEC mode. |

| Note | Enter your
                                                         				  password if prompted. |
|---|---|

| Note | This step is
                                                         				  needed only when you set the CME internal authentication server as your phone
                                                         				  authentication server in Step 5. |
|---|---|

| Note | Default:
                                                         				  Automatic Clear Call History is enabled. |
|---|---|

| Note | All Cisco
                                             			 Unified SIP phones with displays that support URL provisioning are supported by
                                             			 Extension Mobility. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register pool pool-tag Example: Router(config)# voice register pool 22 | Enables phone
                                             				configuration mode. pool-tag—Unique number that identifies this register pool during
                                                   					 configuration tasks. Range is 1 to 42. |
| Step 4 | id mac mac-address Example: Router(config-register-pool)# id mac 0123.4567.89AB | Associates a
                                             				physical phone with this ephone configuration. mac-address—mac address of the physical phone |
| Step 5 | type phone-type Example: Router(config-register-pool)# type 7970 | Defines a
                                             				phone type for the phone being configured. |
| Step 6 | logout-profile profile-tag Example: Router(config-register-pool)# logout-profile 22 | Enables
                                             				Cisco Unified SIP phone for Extension Mobility and assigns a logout profile to
                                             				this phone. profile
                                                   					 tag—Unique identifier of a logout profile to be used when no phone user is
                                                   					 logged in to this phone. This tag number corresponds to a tag number created
                                                   					 when this logout profile was configured by using the voice
                                                         						  logout-profile command. |
| Step 7 | end Example: Router(config-ephone)# end | Exits to
                                             				privileged EXEC mode. |

| Note | Templates
                                             			 created using the ephone-template and ephone-dn-template commands can be applied to a
                                             			 user profile for Extension Mobility. |
|---|---|

| Restriction | For button
                                                   				  appearance, Extension Mobility associates directory numbers, then speed-dial
                                                   				  definitions in the logout profile or user profile to phone buttons. The
                                                   				  sequence in which directory numbers are associated is based on line type and
                                                   				  ring behavior as follows: first normal, then silent ring, beep ring, feature
                                                   				  ring, monitor ring, and overlay, followed by speed dials. If the profile
                                                   				  contains more directory numbers and speed-dial numbers than there are buttons
                                                   				  on the physical phone to which the profile is downloaded, not all numbers are
                                                   				  downloaded to buttons. The first
                                                   				  number to be configured for line appearance cannot be a monitored directory
                                                   				  number. The user name parameter of any authentication credential must be unique. Do not use the same value for a user name when you
                                                   configure any two or more authentication credentials in Cisco Unified CME, such as the user name in a logout or user profile
                                                   for Extension Mobility. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice user-profile profile-tag Example: Router(config)# voice user-profile 1 | Enters voice
                                             				user-profile configuration mode for configuring a user profile for Extension
                                             				Mobility. profile-tag —Unique number that identifies this
                                                   					 profile during configuration tasks. Range: 1 to three times the maximum number
                                                   					 supported phones, where maximum is platform dependent. Type ? to display
                                                   					 value. |
| Step 4 | user name password password Example: Router(config-user-profile)# user me password pass123 | Creates
                                             				credential to be authenticated by Cisco Unified CME before allowing the phone
                                             				user to log into a Cisco Unified IP phone phone enabled for Extension Mobility. name —Unique alphanumeric string to identify a user
                                                   					 for this authentication credential only. password —Password for authorized user. |
| Step 5 | number number type type Example: Router(config-user-profile)# number 2001 type silent-ring 
				Router(config-user-profile)# number 2002 type beep-ring 
				Router(config-user-profile)# number 2003 type feature-ring
				Router(config-user-profile)# number 2004 type monitor-ring 
				Router(config-user-profile)# number 2005,2006 type overlay 
				Router(config-user-profile)# number 2007,2008 type cw-overly | Creates line
                                             				definition. number —Directory number to be associated with and
                                                   					 displayed next to a button on a phone that is configured with this profile. [ , ...number ]—(Optional) For overlay lines only, with
                                                   					 or without call waiting. The directory number that is far left in the command
                                                   					 list is given the highest priority. Can contain up to 25 numbers. Individual
                                                   					 numbers must be separated by commas ( , ) type type —Denotes characteristics to be associated with
                                                   					 this line. Type ? for list of options. |
| Step 6 | speed-dial speed-tag number [ label label ] [ blf ] Example: Router(config-user-profile)# speed-dial 1 3001 
				Router(config-user-profile)# speed-dial 2 3002 blf | Creates
                                             				speed-dial definition. speed-tag —Unique sequence number that identifies a
                                                   					 speed-dial definition during configuration tasks. Range: 1 to 36. number —Digits to be dialed when the speed-dial
                                                   					 button is pressed. label label —(Optional) String that contains identifying
                                                   					 text to be displayed next to the speed-dial button. Enclose the string in
                                                   					 quotation marks if the string contains a space. blf —(Optional) Enables Busy Lamp Field (BLF)
                                                   					 monitoring for a speed-dial number. |
| Step 7 | pin number Example: Router(config-user-profile)# pin 12341 | Sets a
                                             				personal identification number (PIN) to be used by a phone user to disable the
                                             				call blocking configuration for a Cisco Unified IP phone on which this profile
                                             				is downloaded. number —Numeric string containing four to eight
                                                   					 digits. |
| Step 8 | max-idle-time minutes Example: Router(config-user-profile)# max-idle-time 30 | (Optional)
                                             				Creates an idle-duration timer for automatically logging out an Extension
                                             				Mobility user. This
                                                   					 command is supported in Cisco Unified CME 4.3 and later versions. minutes —Maximum number of minutes after which a
                                                   					 user is logged out from an idle Extension Mobility phone. Range:1 to 9999. |
| Step 9 | privacy-button Example: Router(config-user-profile)# privacy-button | (Optional)
                                             				Enables the privacy feature button on the IP phone. Enable
                                                   					 this command only on phones that share an octo-line directory number. This
                                                   					 command is supported in Cisco Unified CME 4.3 and later versions. |
| Step 10 | end Example: Router(config-user-profile)# end | Exits to
                                             				privileged EXEC mode. |

| Feature
                                             					 Name | Cisco Unified CME Version | Modification |
|---|---|---|
| MIB
                                             					 Support for Extension Mobility in Cisco Unified SCCP IP Phones | 9.0 | Adds new
                                             					 MIB objects to monitor Cisco Unified SCCP IP EM phones. |
| Support
                                             					 for SIP phones | 8.6 | Adds
                                             					 support for SIP phones. |
| Extension
                                             					 Mobility Enhancement | 7.0/4.3 | Adds
                                             					 support for the following: Automatic Logout, including: Configurable time-of-day timers for automatically logging out
                                                   						  all Extension Mobility users. Configurable idle-duration timer for logging out an individual
                                                   						  user from an idle Extension Mobility phone. Automatic Clear Call History when a user logs out from Extension
                                                   						  Mobility. |
| Phone
                                             					 User-Interface for Speed Dial | 7.0/4.3 | Adds a
                                             					 phone user interface allowing Extension Mobility users to configure their own
                                             					 speed-dial settings directly on the phone. |
| Extension
                                             					 Mobility | 4.2 | Provides
                                             					 the benefit of phone mobility for end users by enabling the user to log into
                                             					 any local Cisco Unified IP Phone that is enabled for Extension Mobility. |