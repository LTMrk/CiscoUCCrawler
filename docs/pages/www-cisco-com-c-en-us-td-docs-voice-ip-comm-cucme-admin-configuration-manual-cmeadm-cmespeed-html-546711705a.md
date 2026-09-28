---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmespeed-html-546711705a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmespeed.html
retrieved_at: 2026-08-21T07:24:15.986520+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Speed Dial

## Chapter: Speed Dial

# Speed Dial

## Information About Speed Dial

### Speed Dial
                           	 Summary

Speed Dial
                                             				  Type

Availability
                                             				  of Numbers

Description

How
                                             				  Configured

Local Speed
                                             				  Dial Menu

System-level
                                             				  list of frequently called numbers that can be programmed on all phones.

A maximum of
                                             				  32 numbers can be defined.

Numbers are
                                             				  set up by an administrator using an XML File speeddial.xml, which is placed in
                                             				  the Cisco Unified CME router’s flash memory.

Users invoke
                                             				  entries from the Directories > Local Speed Dial menu on IP phones.

Enable a Local Speed Dial Menu

Personal
                                             				  Speed Dial Menu

Speed dial
                                             				  entries are local to a specific IP phone.

A maximum of
                                             				  24 numbers per phone can be defined.

Users invoke
                                             				  entries from the Directories > Local Services > Personal Speed Dials menu
                                             				  on IP phones.

Enable a Personal Speed Dial Menu on SCCP Phones

Enable a Personal Speed Dial Menu on SIP Phones

Speed Dial
                                             				  Buttons and Abbreviated Dialing

Up to 99
                                             				  speed-dial codes per phone.

For IP
                                             				  phones, the first entries that are set up occupy any unused line buttons and
                                             				  are invoked when a user presses one of these line buttons. Subsequent entries
                                             				  are invoked when a phone user dials the speed-dial code (tag) and the Abbr soft
                                             				  key.

The feature to invoke subsequent entries by dialing the
                                                         					 speed-dial code (tag) and the Abbr soft key is supported only on SCCP phones.

Analog phone
                                             				  users invoke speed dial by entering an asterisk and the speed-dial code (tag)
                                             				  number of the desired entry.

Define Speed-Dial Buttons and Abbreviated Dialing on SCCP Phones

Define Speed-Dial Buttons on SIP Phones

Bulk-Loading
                                             				  Speed Dial Numbers

There can be
                                             				  up to ten text files containing lists of many speed-dial numbers that are
                                             				  loaded into flash, slot, or TFTP locations to be accessed by phone users. The
                                             				  ten files can hold 10,000 numbers.

Phone users
                                             				  dial the following sequence:

prefix-code list-id index [ extension-digits ]

Enable Bulk-Loading Speed-Dial

Monitor-Line
                                             				  Button for Speed Dial

Speed dial
                                             				  entries are local to a specific IP phone.

There can be
                                             				  as many numbers as there are monitor lines on a phone.

IP phone
                                             				  buttons that are configured as monitor lines can be used to speed-dial the line
                                             				  that is being monitored.

No
                                             				  additional configuration required.

Direct
                                             				  Station Select (DSS) Service

All phones
                                             				  on which speed-dial line or monitor line button is configured.

Allows phone
                                             				  user to fast transfer a call by pressing a single speed-dial line or monitor
                                             				  line button.

Enable DSS Service

### Speed Dial Buttons
                           	 and Abbreviated Dialing

In a
                              		Cisco Unified CME system, each phone can have up to 32 local speed-dial numbers
                              		(codes 1 to  32), up to 99 system-level speed-dial numbers (codes 1 to 99), or
                              		a combination of the two. If you program both a local and a system-level
                              		speed-dial number with the same speed-dial code (tag), the local number takes
                              		precedence. Typically you will want to reserve codes 1 to 32 for local,
                              		per-phone speed-dial numbers and use codes 33 to 99 for system-level speed-dial
                              		numbers so that there is no conflict.

On an IP phone,
                              		speed-dial entries are assigned to unused line buttons. Then, after all line
                              		buttons are used, subsequent entries are added but do not have an assigned line
                              		button. The speed-dial entry is not related to the physical button layout of
                              		the phone. Entries are assigned in order of speed-dial tag.

You can create local
                              		speed-dial codes with locked numbers that cannot be changed from the phone. You
                              		can also create empty local speed-dial codes on an IP phone without a telephone
                              		number. These empty speed-dial codes can be changed by the phone user to add a
                              		telephone number.

Changes to
                              		speed-dial entries are saved into the router’s nonvolatile random-access memory
                              		(NVRAM) configuration after a timer-based delay.

For configuration
                              		information, see Define Speed-Dial Buttons and Abbreviated Dialing on SCCP Phones .

### Bulk-Loading Speed
                           	 Dial Numbers

In Cisco Unified CME
                              		4.0 and later versions, up to ten text files containing lists of many
                              		speed-dial numbers can be loaded into flash, slot, or TFTP locations to be
                              		accessed by phone users. The ten files can hold a total of up to 10,000
                              		numbers. Each list holds numbers that are in an appropriate format for dialing
                              		from IP phones and SCCP-enabled analog phones.

Up to ten bulk
                              		speed-dial lists can be created. These lists might be corporate directory
                              		lists, regional lists, or local lists, for example. The speed-dial numbers in
                              		these lists can be system-level (available to all ephones) or personal
                              		(available to one or more specified ephones). Each list receives a unique
                              		speed-dial list ID number (sd-id) between 0 and 9.

Speed-dial list ID
                              		numbers that are not used for global speed-dial lists are available to identify
                              		personal, custom lists that are associated with individual phones.

Bulk speed-dial
                              		lists contain entries of speed-dial codes and the associated phone numbers to
                              		dial. Each entry in a speed-dial list must appear on a separate line. The
                              		fields in each entry are separated by commas (,). A line that begins with a
                              		semicolon (;) is handled as a comment. The format of each entry is shown in the
                              		following line.

```
index , digits ,[ name ],[ hide ],[ append ]
```

Table 1 explains the fields in a bulk speed-dial list entry.

Field

Description

index

Zero-filled
                                             				  number that uniquely identifies this index entry. Maximum length: 4 digits. All
                                             				  index entries must be the same length.

digits

Telephone
                                             				  number to dialed. Represents a fully qualified E.164 number. Use a comma (,) to
                                             				  represent a one-second pause.

name

(Optional)
                                             				  Alphanumeric string to identify a name, up to 30 characters.

hide

(Optional)
                                             				  Enter hide to block the display of the dialed number.

append

(Optional)
                                             				  Enter append to allow additional digits to be appended to
                                             				  this number when dialed.

The following is a
                              		sample bulk speed-dial list:

```
01,5550140,voicemail,hide,append 
90,914085550153,Cisco extension,hide,append 
11,9911,emergency,hide,
91,9911,emergency,hide, 
08,110,Paging,,append
```

To place a call to a
                              		speed-dial entry in a list, the phone user must first dial a prefix, followed
                              		by the list ID number, then the index for the bulk speed-dial list entry to be
                              		called.

For configuration
                              		information, see Enable Bulk-Loading Speed-Dial .

### Monitor-Line Button for Speed Dial

For Cisco CME 3.2 and later versions, a monitor-line button can be used
                              		to speed-dial the monitor line’s number. A monitor line is a line that is
                              		shared by two people. Only one person can make and receive calls on the shared
                              		line at a time, while the other person, whose line is in monitor mode, is able
                              		to see that the line is in use. Speed dialing is available when monitor lines’
                              		lamps are off, indicating that the line is not in use. For example, an
                              		assistant who wants to talk with a manager can press an unlit monitor-line
                              		button to speed-dial the manager’s number.

A monitor-line lamp is off or unlit only when its line is in the idle
                              		call state. The idle state occurs before a call is made and after a call is
                              		completed. For all other call states, the monitor-line lamp is on or lit.

The following example shows a monitor-line configuration. Extension 2311
                              		is the manager’s line, and ephone 1 is the manager’s phone. The manager’s
                              		assistant monitors extension 2311 on button 2 of ephone 2. When the manager is
                              		on the line, the lamp is lit on the assistant’s phone. If the lamp is not lit,
                              		the assistant can speed-dial the manager by pressing button 2.

```
ephone-dn 11
	  number 2311
	  
	 ephone-dn 22
	  number 2322
	 
	 ephone 1
	  button 1:11
	  
	 ephone 2
	  button 1:22 2m11
```

No additional configuration is required to enable a phone user to speed
                              		dial the number of a monitored shared line, when the monitored line is in an
                              		idle call state.

### DSS (Direct
                           	 Station Select) Service

In Cisco Unified CME
                              		4.0(2) and later versions, the DSS (Direct Station Select) Service feature
                              		allows the phone user to press a single speed-dial line button to transfer an
                              		incoming call when the call is in the connected state. This feature is
                              		supported on all phones on which monitor line buttons for speed dial or
                              		speed-dial line buttons are configured.

When the DSS service
                              		is enabled, the system automatically generates a simulated transfer key event
                              		when needed, eliminating the requirement for the phone user to press the
                              		Transfer button.

Disabling the
                              		service changes the behavior of the speed-dial line button on all IP phones so
                              		that a user pressing a speed-dial button in the middle of a connected call will
                              		play out the speed-dial digits into the call without transferring the call.
                              		When DSS service is disabled, the phone user must first press Transfer and then
                              		press the monitor or speed-dial line button to transfer the incoming call.

For configuration
                              		information, see Enable a Local Speed Dial Menu .

### Phone
                           	 User-Interface for Speed Dial and Fast Dial

In Cisco Unified CME
                              		4.3 and later versions, IP phone users can configure their own speed-dial and
                              		fast-dial settings directly from the phone. The speed-dial and fast-dial
                              		settings can be added or modified on the phone by using a menu available with
                              		the Services feature button. Extension Mobility users can add or modify
                              		speed-dial settings in their user profile after logging in. Fast-dial settings
                              		are not configurable from Extension Mobility phones, nor is the logout profile
                              		configurable from the phone.

The speed-dial and fast-dial feature in Unified CME gives phone users the convenience of configuring their speed-dial and
                              fast-dial settings directly from their phones.

The speed-dial and
                              		fast-dial user interface is enabled by default on all phones with displays. You
                              		can disable the capability for an individual phone in Cisco Unified CME to
                              		prevent a phone user from accessing the interface. If a phone's speed-dial or
                              		fast-dial setting is configured with an ephone-template, the configuration from
                              		the phone applies only to the specific phone and does not change the
                              		ephone-template configuration.

For configuration
                              		information, see Enable Phone User Interface for Configuring Speed-Dial and Fast-Dial .

For information on
                              		how phone users configure speed-dial and fast-dial buttons using the phone
                              		user-interface, see the Cisco Unified IP Phone documentation for
                              		Cisco Unified CME.

## Configure Speed Dial

### Enable a Local
                           	 Speed Dial Menu

To enable a local
                                 		  speed-dial menu for all phones, SCCP and SIP, in Cisco Unified CME, perform the
                                 		  following steps:

Restriction

If a speed
                                                      				  dial XML file contains incomplete information, for example the name or
                                                      				  telephone number is missing for an entry, any information in the file that is
                                                      				  listed after the incomplete entry is not displayed when the local speed dial
                                                      				  directory option is used on a phone.

Before
                                                      				  Cisco Unified CME 4.1, local speed-dial menu is not supported on SIP phones.

Before
                                                      				  Cisco CME 3.3, analog phones are limited to nine speed-dial numbers.

#### Before you begin

An XML file called
                                 		  speeddial.xml must be created and copied to the TFTP server application on the
                                 		  Cisco Unified CME router. The contents of speeddial.xml must be valid as
                                 		  defined in the Cisco-specified directory DTD. See Example for Enabling a Local Speed Dial Menu and the Cisco Unified IP Phone Services Application
                                    			 Development Notes .

### SUMMARY STEPS

- enable

- copy tftp flash

- configure terminal

- ip http server

- ip http path flash:

- exit

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router# enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

copy tftp flash

#### Example:

```
Router# copy tftp flash
			 
			 Address or name of remote host []? 172.24.59.11
			 Source filename []? speeddial.xml
			 Destination filename [speeddial.xml]?
			 Accessing tftp://172.24.59.11/speeddial.xml...
			 Erase flash:before copying? [confirm]n
			 Loading speeddial.xml from 172.24.59.11 (via
			 FastEthernet0/0):!
			 [OK - 329 bytes]
			 
			 Verifying checksum...  OK (0xF5DB)
			 329 bytes copied in 0.044 secs (7477 bytes/sec)
```

Copies the
                                             				file from the TFTP server to the router flash memory.

At the
                                                   					 first prompt, enter the IP address or the DNS name of the remote host.

At both
                                                   					 filename prompts, enter speeddial.xml .

At the
                                                   					 prompt to erase flash, enter no .

Step 3

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 4

ip http server

#### Example:

```
Router(config)# ip http server
```

Enables the
                                             				Cisco web-browser user interface on the router.

Step 5

ip http path flash:

#### Example:

```
Router(config)# ip http path flash:
```

Sets the base
                                             				HTTP path to flash memory.

Step 6

exit

#### Example:

```
Router(config)# exit
```

Returns to
                                             				privileged EXEC mode.

### Enable DSS Service

To enable DSS Service for all on all SCCP phones on which monitor line
                                 		  buttons for speed dial or speed-dial line buttons are configured, perform the
                                 		  following steps.

#### Before you begin

Cisco Unified CME 4.0(2) or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- service dss

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

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters telephony-service configuration mode.

Step 4

service dss

#### Example:

```
Router(config-telephony)# service dss
```

Configures DSS (Direct Station Select) service globally for all
                                             				phone users in Cisco Unified CME.

Step 5

end

#### Example:

```
Router(config-telephony)# end
```

Exits configuration mode and enters privileged EXEC mode.

### Enable a Personal
                           	 Speed Dial Menu on SCCP Phones

To enable a
                                 		  personal speed-dial menu, perform the following steps.

Restriction

A personal
                                                      				  speed-dial menu is available only on certain Cisco Unified IP phones, such as
                                                      				  the 7940, 7960, 7960G, 7970G, and 7971G-GE. To determine whether personal
                                                      				  speed-dial menu is supported on your IP phone, see the Cisco Unified CME User Guides for your
                                                      				  IP phone model.

### SUMMARY STEPS

- enable

- configure terminal

- ephone phone-tag

- fastdial dial-tag number name name-string

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router# enable
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

phone-tag —Unique number of the phone for which you
                                                   					 want to program personal speed-dial numbers.

Step 4

fastdial dial-tag number name name-string

#### Example:

```
Router(config-ephone)# fastdial 1 5552 name Sales
```

Creates an
                                             				entry for a personal speed-dial number on this phone.

dial-tag —Unique identifier to identify this entry
                                                   					 during configuration. Range is 1 to 100.

The
                                                               						range for dial-tag is 1 to 24 for Cisco Unified CME versions earlier than 10.5

- number —Telephone number or extension to be dialed.

- name name-string —Label to appear in the Personal Speed
                                                				  Dial menu, containing a string of up to 24 alphanumeric characters. Personal
                                                				  speed dial is handled through an XML request, so characters that have special
                                                				  meaning to HTTP, such as ampersand (&), percent sign (%), semicolon (;),
                                                				  angle brackets (< >), and vertical bars (||), are not allowed.

Step 5

end

#### Example:

```
Router(config-ephone)# end
```

Returns to
                                             				privileged EXEC mode.

### Define Speed-Dial
                           	 Buttons and Abbreviated Dialing on SCCP Phones

To define
                                 		  speed-dial buttons and abbreviated dialing codes, perform the following steps
                                 		  for each speed-dial definition to be configured.

Restriction

On-hook
                                                      				  abbreviated dialing using the Abbr soft key is supported only on the following
                                                      				  phones:

Cisco Unified IP Phone 7905G

Cisco Unified IP Phone 7912G

Cisco Unified IP Phone 7920G

Cisco Unified IP Phone 7970G

Cisco Unified IP Phone 7971G-GE

System-level
                                                      				  speed-dial codes cannot be changed by the phone user, at the phone.

Before
                                                      				  Cisco CME 3.3, analog phones were limited to nine speed-dial numbers.

Before to
                                                      				  Cisco CME 3.3, speed-dial entries that were in excess of the number of physical
                                                      				  phone buttons available were ignored by IP phones.

### SUMMARY STEPS

- enable

- configure terminal

- ephone phone-tag

- speed-dial speed-tag digit-string [ label label-text ]

- restart

- exit

- telephony-service

- directory entry {{ directory-tag number name name }| clear }

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
Router(config)# ephone 55
```

Enters ephone
                                             				configuration mode.

phone-tag —Unique sequence number that identifies
                                                   					 the phone on which you are adding speed-dial capability.

Step 4

speed-dial speed-tag digit-string [ label label-text ]

#### Example:

```
Router(config-ephone)# speed-dial 1 +5001 label “Head Office”
```

Defines a
                                             				unique speed-dial identifier, a digit string to dial, and an optional label to
                                             				display next to the button.

speed-tag —identifier for a speed-dial definition.
                                                   					 Range is 1 to 33.

Step 5

restart

#### Example:

```
Router(config-ephone)# restart
```

Performs a
                                             				fast reboot of this ephone. Does not contact the DHCP or TFTP server for
                                             				updated information.

Step 6

exit

#### Example:

```
Router(config-ephone)# exit
```

Exits
                                             				configuration mode to the next highest mode in the configuration mode
                                             				hierarchy.

Step 7

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony-service configuration mode.

Step 8

directory entry {{ directory-tag number name name }| clear }

#### Example:

```
Router(config-telephony)# directory entry 45 8185550143 name Corp Acctg
```

Adds a
                                             				system-level directory and speed-dial definition.

directory-tag —Digit string that provides a unique
                                                   					 identifier for this entry. Range is 1 to 99.

If the same
                                             				tags 1 through 33 are configured at a phone-level by using speed-dial command, and at a system-level by using this command, the local definition
                                             				takes precedence. To prevent this conflict, we recommend that you use only
                                             				codes 34 to 99 for system-level speed-dial numbers.

Step 9

end

#### Example:

```
Router(config-telephony)# end
```

Returns to
                                             				privileged EXEC mode.

### Enable
                           	 Bulk-Loading Speed-Dial

To enable
                                 		  bulk-loading speed-dial numbers, perform the following steps:

Restriction

Bulk speed
                                                      				  dial is not supported on FXO trunk lines.

#### Before you begin

Cisco Unified CME 4.0 or a letter version.

The bulk
                                          				speed-dial text files containing the lists must be available in a location that
                                          				is available to the Cisco Unified CME router: flash, slot, or TFTP location.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- bulk-speed-dial list list-id location

- bulk-speed-dial prefix prefix-code

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

bulk-speed-dial list list-id location

#### Example:

```
Router(config-telephony)# bulk-speed-dial list 6 flash:sd_dept_0_1_8.txt
```

identifies the
                                             				location of a bulk speed-dial list.

list-id —Digit that identifies the list to be used.
                                                   					 Range is 0 to 9.

location —Location of the bulk speed-dial text file
                                                   					 in URL format. Valid storage locations are TFTP, Slot 0/1, and flash memory.

This command
                                             				can also be configured in ephone configuration mode for specific phones.

Step 5

bulk-speed-dial prefix prefix-code

#### Example:

```
Router(config-telephony)# bulk-speed-dial prefix #7
```

Sets the
                                             				prefix code that phone users dial to access speed-dial numbers from a bulk
                                             				speed-dial list.

prefix-code —One- or two-character access code for
                                                   					 speed dial. Valid characters are digits from 0 to 9, asterisk (*), and pound
                                                   					 sign (#). Default is #.

Step 6

end

#### Example:

```
Router(config-telephony)# end
```

Returns to
                                             				privileged EXEC mode.

### Verify Bulk
                           	 Speed-Dial Parameters on SCCP Phones

show telephony-service bulk-speed-dial

Use this
                                             				command to display information on speed-dial lists.

#### Example:

```
Router# show telephony-service bulk-speed-dial summary List-id    Entries      Size    Reference  url
		      0         40      3840    Global     tftp://192.168.254.254/phonedirs/uut.csv
		      1         20      1920    Global     phoneBook.csv
		      8         15      1440    Global     tftp://192.168.254.254/phonedirs/big.txt
		      9         20      1920    Global     tftp://192.168.254.254/phonedirs/phoneBook.csv
		      6      24879   2388384    ephone-2   tftp://192.168.254.254/phonedirs/big.txt1
		      7         20      1920    ephone-2   phoneBook.csv
		      6      24879   2388384    ephone-3   big.txt1
		      7         20      1920    ephone-3   phoneBook.csv
		
		4 Global List(s) 4 Local List(s)
```

### Enable Phone User
                           	 Interface for Configuring Speed-Dial and Fast-Dial

To enable a phone
                                 		  user to configure speed-dial and fast-dial numbers from a menu on their phone,
                                 		  perform the following steps. This feature is enabled by default. You must
                                 		  perform this task only if the feature was previously disabled on a phone.

Restriction

Extension
                                             			 Mobility users cannot configure fast-dial settings (for personal speed-dial)
                                             			 from their phone.

#### Before you begin

Cisco Unified
                                          				CME 4.3 or a later release.

The Service
                                          				URL must be configured. See Provision URLs for Feature Buttons for SCCP Phones .

### SUMMARY STEPS

- enable

- configure terminal

- ephone phone-tag

- phone-ui speeddial-fastdial

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router# enable
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

phone-ui speeddial-fastdial

#### Example:

```
Router(config-ephone)# phone-ui speeddial-fastdial
```

Enables a
                                             				phone user to configure speed-dial and fast-dial numbers on their phone.

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

#### What to do next

For information on
                                 		  how phone users configure speed dial and fast dial buttons using the UI, see Cisco Unified IP Phone
                                    			 documentation for Cisco Unified CME .

### Define Speed-Dial
                           	 Buttons on SIP Phones

To define
                                 		  speed-dial buttons for Cisco SIP Phones, perform the following steps.

Restriction

Certain SIP
                                                      				  phones, such as the Cisco Unified IP Phone 7960 and 7940, cannot be configured
                                                      				  to enable speed dialing. Phone users with these phones must manually configure
                                                      				  speed-dial numbers by using the user interface at their Cisco Unified IP phone.

On
                                                      				  Cisco Unified IP phones, speed-dial definitions are assigned to available
                                                      				  buttons that have not been assigned to actual extensions. Speed-dial
                                                      				  definitions are assigned in the order of their identifier numbers.

Phones with
                                                      				  Cisco ATA devices are limited to a maximum of nine speed-dial numbers.
                                                      				  Speed-dial numbers cannot be programmed by using the user interface at the
                                                      				  phone.

#### Before you begin

Cisco CME 3.4 or a
                                 		  later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice register pool pool-tag

- speed-dial speed-tag digit-string [ label label-text ]

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router# enable
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
Router(config)# voice register pool 23
```

Enters voice
                                             				register pool configuration mode to set parameters for specified SIP phone.

Step 4

speed-dial speed-tag digit-string [ label label-text ]

#### Example:

```
router(config-register-pool)# speed-dial 2 +5001 label “Head Office”
```

Creates a
                                             				speed-dial definition in Cisco Unified CME for a SIP phone or analog phone that
                                             				uses an analog adapter (ATA).

speed-tag —Unique sequence number that identifies
                                                   					 the speed-dial definition during configuration. Range is 1 to 5.

Step 5

end

#### Example:

```
Router(config-register-pool)# end
```

Exits
                                             				configuration mode and enters privileged EXEC mode.

#### Examples

The following
                                 		  example shows how to set speed-dial button 2 to dial the head office at
                                 		  extension 5001 and locks the setting so that the phone user cannot change the
                                 		  setting at the phone:

```
Router(config)# voice register pool 23 Router(config-register-pool)# speed-dial 2 +5001 label “Head Office”
```

### Enable a Personal
                           	 Speed Dial Menu on SIP Phones

To enable a
                                 		  personal speed-dial menu, perform the following steps.

Restriction

A personal
                                                      				  speed-dial menu is available only on certain Cisco Unified IP phones, such as
                                                      				  the 7811, 7821, 7841, 7861, 8841, and 8861. To determine whether personal
                                                      				  speed-dial menu is supported on your IP phone, see the Cisco Unified CME User
                                                         					 Guides for your IP phone model.

### SUMMARY STEPS

- enable

- configure terminal

- voice register pool pool-tag

- fastdial entry-tag number name name-string

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router# enable
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
Router(config)# voice register pool 1
```

Enters
                                             				voice-register pool configuration mode.

pool-tag —Unique number of the phone for which you
                                                   					 want to program personal speed-dial numbers.

Step 4

fastdial entry-tag number name name-string

#### Example:

```
Router(config-register-pool)# fastdial 1 5552 name Sales
```

Creates an
                                             				entry for a personal speed-dial number on this phone.

entry-tag —Unique identifier to identify this entry
                                                   					 during configuration. Range is 1 to 100.

The range
                                                         				  for entry-tag is 1 to 24 for Cisco Unified CME versions earlier than 10.5.

number —Telephone number or extension to be dialed.

name name-string —Label to appear in the Personal Speed
                                                   					 Dial menu, containing a string of up to 24 alphanumeric characters. Personal
                                                   					 speed dial is handled through an XML request, so characters that have special
                                                   					 meaning to HTTP, such as ampersand (&), percent sign (%), semicolon (;),
                                                   					 angle brackets (< >), and vertical bars (||), are not allowed.

Step 5

end

#### Example:

```
Router(config-register-pool)# end
```

Returns to
                                             				privileged EXEC mode.

## Configuration Examples for Speed Dial

### Example for Enabling a Local Speed Dial Menu

The following commands enable the Cisco web browser and set the HTTP
                                 		  path to flash memory so that the speeddial.xml file in flash memory is
                                 		  accessible to IP phones:

```
ip http server
ip http path flash:
```

The following XML file—speeddial.xml, defines three speed-dial numbers
                                 		  that will appear to the user after they press the Directories button on an IP
                                 		  phone.

```
<CiscoIPPhoneDirectory>
<Title>Local Speed Dial</Title>
<Prompt>Record 1 to 1 of 1 </Prompt>

<DirectoryEntry>
  <Name>Security</Name>
  <Telephone>71111</Telephone>
</DirectoryEntry>

<DirectoryEntry>
 <Name>Marketing</Name>
 <Telephone>71234</Telephone>
</DirectoryEntry>

<DirectoryEntry>
 <Name>Tech Support</Name>
  <Telephone>71432</Telephone>
</DirectoryEntry>

</CiscoIPPhoneDirectory>
```

### Example for Configuring Personal Speed Dial Menu on SIP Phone

The following example creates a directory of three personal speed-dial
                                 		  listings for one IP phone:

```
ephone 1
		 fastdial 1 5489 name Marketing
		 fastdial 2 12125550155 name NY Sales
		 fastdial 3 12135550112 name LA Sales
```

### Example for Configuring Speed-Dial Buttons and Abbreviated
                           	 Dialing

The following example defines two locked speed-dial numbers with
                                 		  labels to appear next to the speed-dial buttons on ephone 1. These speed-dial
                                 		  definitions are assigned to the next empty buttons after all extensions are
                                 		  assigned. For instance, if two extensions are assigned on the
                                 		  Cisco Unified IP Phones 7960 and 7960G, these speed-dial definitions appear on
                                 		  the third and fourth buttons.

This example also defines two system-level speed-dial numbers with the directory entry command. One is a local
                                 		  extension and the other is a ten-digit telephone number.

```
ephone 1
		 mac-address 1234.5678.ABCD
		 button 1:24 2:25
		 speed-dial 1 +5002 label Receptionist
		 speed-dial 2 +5001 label Security
		
		telephony-service
		 directory entry 34 5003 name Accounting
		 directory entry 45 8185550143 name Corp Acctg
```

### Example for Configuring Bulk-Loading Speed Dial

The following example changes the default bulk speed-dial prefix to #7
                                 		  and enables global bulk speed-dial list number 6 for all phones. It also
                                 		  enables a personal bulk speed-dial list for ephone 25.

```
telephony-service
		 bulk-speed-dial list 6 flash:sd_dept_01_1_87.txt
		 bulk-speed-dial prefix #7
		
		ephone-dn 3
		 number 2555
		
		ephone-dn 4
		 number 2557
		
		ephone 25
		 button 1:3 2:4
		 bulk-speed-dial list 7 flash:lmi_sd_list_08_24_95.txt
```

### Example for Configuring Speed-Dial and Fast-Dial User
                           	 Interface

The following example shows that the user interface for speed-dial and
                                 		  fast-dial configuration is disabled on phone 12:

```
ephone  12
		 no phone-ui speeddial-fastdial
		 ephone-template 5
		 mac-address 000F.9054.31BD
		 type 7960
		 button  1:10 2:7
```

## Where to Go
                        	 Next

If you are finished creating or modifying speed-dial configurations for individual phones, you must reboot phones to download
                           the modified configuration. See Reset and Restart Cisco Unified IP Phones .

### DSS Call
                              		  Transfer

Monitor-line
                              		  button speed dial, also known as direct station select (DSS) call transfer,
                              		  allows you to use a monitored line button to speed-dial a call to that
                              		  extension. If you want to allow consultation during DSS transfers, see Information About Call Transfer and Forward .

## Feature
                        	 Information for Speed Dial

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Cisco Unified CME Version

Feature Information

Speed Dial

4.3

Added user interface on SCCP phones for programming Speed Dial
                                          					 and Fast Dial.

4.1

Added support for local and personal speed-dial menus for SIP
                                          					 phones in Cisco Unified CME.

4.0(2)

Added support for DSS Service which allows phone user to fast
                                          					 transfer a call by pressing a single speed-dial line or monitor line button.

4.0

Added support for bulk speed-dial list for SCCP phones in
                                          					 Cisco Unified CME.

3.4

Added support for speed dial buttons on SIP phones in
                                          					 Cisco Unified CME.

3.0

Added support for personal speed-dial from SCCP phones in
                                                						  Cisco Unified CME.

Number of speed-dial definitions that can be created was
                                                						  increased from 4 to 33.

The ability to program speed-dial numbers at the phone was
                                                						  introduced.

The ability to lock speed-dial numbers was introduced.

1.0

Speed dial using the speed-dial command was introduced.

| Speed Dial
                                             				  Type | Availability
                                             				  of Numbers | Description | How
                                             				  Configured |
|---|---|---|---|
| Local Speed
                                             				  Dial Menu | System-level
                                             				  list of frequently called numbers that can be programmed on all phones. A maximum of
                                             				  32 numbers can be defined. Numbers are
                                             				  set up by an administrator using an XML File speeddial.xml, which is placed in
                                             				  the Cisco Unified CME router’s flash memory. | Users invoke
                                             				  entries from the Directories > Local Speed Dial menu on IP phones. | Enable a Local Speed Dial Menu |
| Personal
                                             				  Speed Dial Menu | Speed dial
                                             				  entries are local to a specific IP phone. A maximum of
                                             				  24 numbers per phone can be defined. | Users invoke
                                             				  entries from the Directories > Local Services > Personal Speed Dials menu
                                             				  on IP phones. | Enable a Personal Speed Dial Menu on SCCP Phones Enable a Personal Speed Dial Menu on SIP Phones |
| Speed Dial
                                             				  Buttons and Abbreviated Dialing | Up to 99
                                             				  speed-dial codes per phone. | For IP
                                             				  phones, the first entries that are set up occupy any unused line buttons and
                                             				  are invoked when a user presses one of these line buttons. Subsequent entries
                                             				  are invoked when a phone user dials the speed-dial code (tag) and the Abbr soft
                                             				  key. Note The feature to invoke subsequent entries by dialing the
                                                         					 speed-dial code (tag) and the Abbr soft key is supported only on SCCP phones. Analog phone
                                             				  users invoke speed dial by entering an asterisk and the speed-dial code (tag)
                                             				  number of the desired entry. | Note | The feature to invoke subsequent entries by dialing the
                                                         					 speed-dial code (tag) and the Abbr soft key is supported only on SCCP phones. | Define Speed-Dial Buttons and Abbreviated Dialing on SCCP Phones Define Speed-Dial Buttons on SIP Phones |
| Note | The feature to invoke subsequent entries by dialing the
                                                         					 speed-dial code (tag) and the Abbr soft key is supported only on SCCP phones. |
| Bulk-Loading
                                             				  Speed Dial Numbers | There can be
                                             				  up to ten text files containing lists of many speed-dial numbers that are
                                             				  loaded into flash, slot, or TFTP locations to be accessed by phone users. The
                                             				  ten files can hold 10,000 numbers. | Phone users
                                             				  dial the following sequence: prefix-code list-id index [ extension-digits ] | Enable Bulk-Loading Speed-Dial |
| Monitor-Line
                                             				  Button for Speed Dial | Speed dial
                                             				  entries are local to a specific IP phone. There can be
                                             				  as many numbers as there are monitor lines on a phone. | IP phone
                                             				  buttons that are configured as monitor lines can be used to speed-dial the line
                                             				  that is being monitored. | No
                                             				  additional configuration required. |
| Direct
                                             				  Station Select (DSS) Service | All phones
                                             				  on which speed-dial line or monitor line button is configured. | Allows phone
                                             				  user to fast transfer a call by pressing a single speed-dial line or monitor
                                             				  line button. | Enable DSS Service |

| Note | The feature to invoke subsequent entries by dialing the
                                                         					 speed-dial code (tag) and the Abbr soft key is supported only on SCCP phones. |
|---|---|

| Field | Description |
|---|---|
| index | Zero-filled
                                             				  number that uniquely identifies this index entry. Maximum length: 4 digits. All
                                             				  index entries must be the same length. |
| digits | Telephone
                                             				  number to dialed. Represents a fully qualified E.164 number. Use a comma (,) to
                                             				  represent a one-second pause. |
| name | (Optional)
                                             				  Alphanumeric string to identify a name, up to 30 characters. |
| hide | (Optional)
                                             				  Enter hide to block the display of the dialed number. |
| append | (Optional)
                                             				  Enter append to allow additional digits to be appended to
                                             				  this number when dialed. |

| Restriction | If a speed
                                                      				  dial XML file contains incomplete information, for example the name or
                                                      				  telephone number is missing for an entry, any information in the file that is
                                                      				  listed after the incomplete entry is not displayed when the local speed dial
                                                      				  directory option is used on a phone. Before
                                                      				  Cisco Unified CME 4.1, local speed-dial menu is not supported on SIP phones. Before
                                                      				  Cisco CME 3.3, analog phones are limited to nine speed-dial numbers. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router# enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | copy tftp flash Example: Router# copy tftp flash
			 
			 Address or name of remote host []? 172.24.59.11
			 Source filename []? speeddial.xml
			 Destination filename [speeddial.xml]?
			 Accessing tftp://172.24.59.11/speeddial.xml...
			 Erase flash:before copying? [confirm]n
			 Loading speeddial.xml from 172.24.59.11 (via
			 FastEthernet0/0):!
			 [OK - 329 bytes]
			 
			 Verifying checksum...  OK (0xF5DB)
			 329 bytes copied in 0.044 secs (7477 bytes/sec) | Copies the
                                             				file from the TFTP server to the router flash memory. At the
                                                   					 first prompt, enter the IP address or the DNS name of the remote host. At both
                                                   					 filename prompts, enter speeddial.xml . At the
                                                   					 prompt to erase flash, enter no . |
| Step 3 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 4 | ip http server Example: Router(config)# ip http server | Enables the
                                             				Cisco web-browser user interface on the router. |
| Step 5 | ip http path flash: Example: Router(config)# ip http path flash: | Sets the base
                                             				HTTP path to flash memory. |
| Step 6 | exit Example: Router(config)# exit | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters telephony-service configuration mode. |
| Step 4 | service dss Example: Router(config-telephony)# service dss | Configures DSS (Direct Station Select) service globally for all
                                             				phone users in Cisco Unified CME. |
| Step 5 | end Example: Router(config-telephony)# end | Exits configuration mode and enters privileged EXEC mode. |

| Restriction | A personal
                                                      				  speed-dial menu is available only on certain Cisco Unified IP phones, such as
                                                      				  the 7940, 7960, 7960G, 7970G, and 7971G-GE. To determine whether personal
                                                      				  speed-dial menu is supported on your IP phone, see the Cisco Unified CME User Guides for your
                                                      				  IP phone model. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router# enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone phone-tag Example: Router(config)# ephone 1 | Enters ephone
                                             				configuration mode. phone-tag —Unique number of the phone for which you
                                                   					 want to program personal speed-dial numbers. |
| Step 4 | fastdial dial-tag number name name-string Example: Router(config-ephone)# fastdial 1 5552 name Sales | Creates an
                                             				entry for a personal speed-dial number on this phone. dial-tag —Unique identifier to identify this entry
                                                   					 during configuration. Range is 1 to 100. Note The
                                                               						range for dial-tag is 1 to 24 for Cisco Unified CME versions earlier than 10.5 number —Telephone number or extension to be dialed. name name-string —Label to appear in the Personal Speed
                                                				  Dial menu, containing a string of up to 24 alphanumeric characters. Personal
                                                				  speed dial is handled through an XML request, so characters that have special
                                                				  meaning to HTTP, such as ampersand (&), percent sign (%), semicolon (;),
                                                				  angle brackets (< >), and vertical bars (\|\|), are not allowed. | Note | The
                                                               						range for dial-tag is 1 to 24 for Cisco Unified CME versions earlier than 10.5 |
| Note | The
                                                               						range for dial-tag is 1 to 24 for Cisco Unified CME versions earlier than 10.5 |
| Step 5 | end Example: Router(config-ephone)# end | Returns to
                                             				privileged EXEC mode. |

| Note | The
                                                               						range for dial-tag is 1 to 24 for Cisco Unified CME versions earlier than 10.5 |
|---|---|

| Restriction | On-hook
                                                      				  abbreviated dialing using the Abbr soft key is supported only on the following
                                                      				  phones: Cisco Unified IP Phone 7905G Cisco Unified IP Phone 7912G Cisco Unified IP Phone 7920G Cisco Unified IP Phone 7970G Cisco Unified IP Phone 7971G-GE System-level
                                                      				  speed-dial codes cannot be changed by the phone user, at the phone. Before
                                                      				  Cisco CME 3.3, analog phones were limited to nine speed-dial numbers. Before to
                                                      				  Cisco CME 3.3, speed-dial entries that were in excess of the number of physical
                                                      				  phone buttons available were ignored by IP phones. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone phone-tag Example: Router(config)# ephone 55 | Enters ephone
                                             				configuration mode. phone-tag —Unique sequence number that identifies
                                                   					 the phone on which you are adding speed-dial capability. |
| Step 4 | speed-dial speed-tag digit-string [ label label-text ] Example: Router(config-ephone)# speed-dial 1 +5001 label “Head Office” | Defines a
                                             				unique speed-dial identifier, a digit string to dial, and an optional label to
                                             				display next to the button. speed-tag —identifier for a speed-dial definition.
                                                   					 Range is 1 to 33. |
| Step 5 | restart Example: Router(config-ephone)# restart | Performs a
                                             				fast reboot of this ephone. Does not contact the DHCP or TFTP server for
                                             				updated information. |
| Step 6 | exit Example: Router(config-ephone)# exit | Exits
                                             				configuration mode to the next highest mode in the configuration mode
                                             				hierarchy. |
| Step 7 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 8 | directory entry {{ directory-tag number name name }\| clear } Example: Router(config-telephony)# directory entry 45 8185550143 name Corp Acctg | Adds a
                                             				system-level directory and speed-dial definition. directory-tag —Digit string that provides a unique
                                                   					 identifier for this entry. Range is 1 to 99. If the same
                                             				tags 1 through 33 are configured at a phone-level by using speed-dial command, and at a system-level by using this command, the local definition
                                             				takes precedence. To prevent this conflict, we recommend that you use only
                                             				codes 34 to 99 for system-level speed-dial numbers. |
| Step 9 | end Example: Router(config-telephony)# end | Returns to
                                             				privileged EXEC mode. |

| Restriction | Bulk speed
                                                      				  dial is not supported on FXO trunk lines. |
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
| Step 4 | bulk-speed-dial list list-id location Example: Router(config-telephony)# bulk-speed-dial list 6 flash:sd_dept_0_1_8.txt | identifies the
                                             				location of a bulk speed-dial list. list-id —Digit that identifies the list to be used.
                                                   					 Range is 0 to 9. location —Location of the bulk speed-dial text file
                                                   					 in URL format. Valid storage locations are TFTP, Slot 0/1, and flash memory. This command
                                             				can also be configured in ephone configuration mode for specific phones. |
| Step 5 | bulk-speed-dial prefix prefix-code Example: Router(config-telephony)# bulk-speed-dial prefix #7 | Sets the
                                             				prefix code that phone users dial to access speed-dial numbers from a bulk
                                             				speed-dial list. prefix-code —One- or two-character access code for
                                                   					 speed dial. Valid characters are digits from 0 to 9, asterisk (*), and pound
                                                   					 sign (#). Default is #. |
| Step 6 | end Example: Router(config-telephony)# end | Returns to
                                             				privileged EXEC mode. |

| show telephony-service bulk-speed-dial Use this
                                             				command to display information on speed-dial lists. Example: Router# show telephony-service bulk-speed-dial summary List-id    Entries      Size    Reference  url
		      0         40      3840    Global     tftp://192.168.254.254/phonedirs/uut.csv
		      1         20      1920    Global     phoneBook.csv
		      8         15      1440    Global     tftp://192.168.254.254/phonedirs/big.txt
		      9         20      1920    Global     tftp://192.168.254.254/phonedirs/phoneBook.csv
		      6      24879   2388384    ephone-2   tftp://192.168.254.254/phonedirs/big.txt1
		      7         20      1920    ephone-2   phoneBook.csv
		      6      24879   2388384    ephone-3   big.txt1
		      7         20      1920    ephone-3   phoneBook.csv
		
		4 Global List(s) 4 Local List(s) |
|---|

| Restriction | Extension
                                             			 Mobility users cannot configure fast-dial settings (for personal speed-dial)
                                             			 from their phone. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router# enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone phone-tag Example: Router(config)# ephone 12 | Enters ephone
                                             				configuration mode. phone-tag —Unique number that identifies this
                                                   					 ephone during configuration tasks. |
| Step 4 | phone-ui speeddial-fastdial Example: Router(config-ephone)# phone-ui speeddial-fastdial | Enables a
                                             				phone user to configure speed-dial and fast-dial numbers on their phone. This
                                                   					 command is enabled by default. |
| Step 5 | end Example: Router(config-ephone)# end | Exits to
                                             				privileged EXEC mode. |

| Restriction | Certain SIP
                                                      				  phones, such as the Cisco Unified IP Phone 7960 and 7940, cannot be configured
                                                      				  to enable speed dialing. Phone users with these phones must manually configure
                                                      				  speed-dial numbers by using the user interface at their Cisco Unified IP phone. On
                                                      				  Cisco Unified IP phones, speed-dial definitions are assigned to available
                                                      				  buttons that have not been assigned to actual extensions. Speed-dial
                                                      				  definitions are assigned in the order of their identifier numbers. Phones with
                                                      				  Cisco ATA devices are limited to a maximum of nine speed-dial numbers.
                                                      				  Speed-dial numbers cannot be programmed by using the user interface at the
                                                      				  phone. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router# enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register pool pool-tag Example: Router(config)# voice register pool 23 | Enters voice
                                             				register pool configuration mode to set parameters for specified SIP phone. |
| Step 4 | speed-dial speed-tag digit-string [ label label-text ] Example: router(config-register-pool)# speed-dial 2 +5001 label “Head Office” | Creates a
                                             				speed-dial definition in Cisco Unified CME for a SIP phone or analog phone that
                                             				uses an analog adapter (ATA). speed-tag —Unique sequence number that identifies
                                                   					 the speed-dial definition during configuration. Range is 1 to 5. |
| Step 5 | end Example: Router(config-register-pool)# end | Exits
                                             				configuration mode and enters privileged EXEC mode. |

| Restriction | A personal
                                                      				  speed-dial menu is available only on certain Cisco Unified IP phones, such as
                                                      				  the 7811, 7821, 7841, 7861, 8841, and 8861. To determine whether personal
                                                      				  speed-dial menu is supported on your IP phone, see the Cisco Unified CME User
                                                         					 Guides for your IP phone model. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router# enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register pool pool-tag Example: Router(config)# voice register pool 1 | Enters
                                             				voice-register pool configuration mode. pool-tag —Unique number of the phone for which you
                                                   					 want to program personal speed-dial numbers. |
| Step 4 | fastdial entry-tag number name name-string Example: Router(config-register-pool)# fastdial 1 5552 name Sales | Creates an
                                             				entry for a personal speed-dial number on this phone. entry-tag —Unique identifier to identify this entry
                                                   					 during configuration. Range is 1 to 100. Note The range
                                                         				  for entry-tag is 1 to 24 for Cisco Unified CME versions earlier than 10.5. number —Telephone number or extension to be dialed. name name-string —Label to appear in the Personal Speed
                                                   					 Dial menu, containing a string of up to 24 alphanumeric characters. Personal
                                                   					 speed dial is handled through an XML request, so characters that have special
                                                   					 meaning to HTTP, such as ampersand (&), percent sign (%), semicolon (;),
                                                   					 angle brackets (< >), and vertical bars (\|\|), are not allowed. | Note | The range
                                                         				  for entry-tag is 1 to 24 for Cisco Unified CME versions earlier than 10.5. |
| Note | The range
                                                         				  for entry-tag is 1 to 24 for Cisco Unified CME versions earlier than 10.5. |
| Step 5 | end Example: Router(config-register-pool)# end | Returns to
                                             				privileged EXEC mode. |

| Note | The range
                                                         				  for entry-tag is 1 to 24 for Cisco Unified CME versions earlier than 10.5. |
|---|---|

| Feature Name | Cisco Unified CME Version | Feature Information |
|---|---|---|
| Speed Dial | 4.3 | Added user interface on SCCP phones for programming Speed Dial
                                          					 and Fast Dial. |
| 4.1 | Added support for local and personal speed-dial menus for SIP
                                          					 phones in Cisco Unified CME. |
| 4.0(2) | Added support for DSS Service which allows phone user to fast
                                          					 transfer a call by pressing a single speed-dial line or monitor line button. |
| 4.0 | Added support for bulk speed-dial list for SCCP phones in
                                          					 Cisco Unified CME. |
| 3.4 | Added support for speed dial buttons on SIP phones in
                                          					 Cisco Unified CME. |
| 3.0 | Added support for personal speed-dial from SCCP phones in
                                                						  Cisco Unified CME. Number of speed-dial definitions that can be created was
                                                						  increased from 4 to 33. The ability to program speed-dial numbers at the phone was
                                                						  introduced. The ability to lock speed-dial numbers was introduced. |
| 1.0 | Speed dial using the speed-dial command was introduced. |