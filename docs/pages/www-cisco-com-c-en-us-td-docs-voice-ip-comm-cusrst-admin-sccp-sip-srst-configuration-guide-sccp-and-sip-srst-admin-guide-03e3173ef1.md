---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cusrst-admin-sccp-sip-srst-configuration-guide-sccp-and-sip-srst-admin-guide-03e3173ef1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cusrst/admin/sccp_sip_srst/configuration/guide/SCCP_and_SIP_SRST_Admin_Guide/srst_setting_up_using_sccp.html
retrieved_at: 2026-08-21T02:49:10.989013+00:00
---

Cisco Unified SRST Administration Guide (All Versions)

# Cisco Unified SRST Administration Guide (All Versions)

Updated: April 25, 2026

Chapter: Setting Up Cisco Unified IP Phones using SCCP

## Chapter: Setting Up Cisco Unified IP Phones using SCCP

# Setting Up Cisco Unified IP Phones using SCCP

This chapter describes how to set up the displays and features that callers will see and use on Cisco Unified IP Phones during
                        Cisco Unified CM fallback.

Ciso Unified IP Phones discussed in this chapter are just examples. For a complete list of IP phones, see Compatibility Information .

## Information About Setting Up Cisco Unified IP Phones

Cisco Unified IP Phone configuration is limited for Cisco Unified SRST because IP phones retain nearly all Cisco Unified CM
                           settings during Cisco Unified CM fallback. You can configure the date format, time format, language, and system messages that
                           appear on Cisco Unified IP Phones during Cisco Unified Communications Manager fallback. All four of these settings have defaults,
                           and the available language options depend on the IP phones and Cisco Unified CM version in use. Also available for configuration
                           is a secondary dial tone, which can be generated when a phone user dials a predefined PSTN access prefix and can be terminated
                           when additional digits are dialed. Dual-line phone configuration is required for dual-line phone operation during Cisco Unified
                           CM fallback.

## How to Set Up Cisco Unified IP Phones

### Configuring Cisco Unified SRST to Support Phone Functions

When the Cisco Unified SRST is enabled, Cisco Unified IP Phones do not have to be reconfigured while in Cisco Unified Communications
                                             Manager fallback mode because phones retain the same configuration that was used with Cisco Unified Communications Manager.

To configure Cisco Unified SRST on the router to support the Cisco Unified IP Phone functions, use the following commands
                                 beginning in global configuration mode.

### SUMMARY STEPS

- call-manager-fallback

- ip source-address ip-address [ port port ] [ any-match | strict-match ]

- max-dn max-directory-numbers [ dual-line ][ preference preference-order ]

- max-ephones max-ephones

- limit-dn phone-type max-lines

- exit

### DETAILED STEPS

Step 1

call-manager-fallback

#### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 2

ip source-address ip-address [ port port ] [ any-match | strict-match ]

#### Example:

```
Router(config-cm-fallback)# ip source-address
10.6.21.4 port 2002 strict-match
```

Enables the router to receive messages from the Cisco IP phones through the specified IP addresses and provides for strict
                                             IP address verification. The default port number is 2000.

Step 3

max-dn max-directory-numbers [ dual-line ][ preference preference-order ]

#### Example:

```
Router(config-cm-fallback)# max-dn 15 dual-line preference 1
```

Sets the maximum number of directory numbers (DNs) or virtual voice ports that can be supported by the router and activates
                                             dual-line mode.

max-directory-numbers :Maximum number of directory numbers (dns) or virtual voice ports supported by the router. The maximum number is platform-dependent.
                                                   The default is 0. See Compatibility Information for further details.

dual-line (Optional). Allows IP phones in Cisco Unified Communications Manager fallback mode to have a virtual voice port with two
                                                   channels.

preference preference-order (Optional). Sets the global preference for creating the VoIP dial peers for all directory numbers that are associated with
                                                   the primary number. Range is from 0 to 10. Default is 0, which is the highest preference.

The alias command also has a preference keyword that sets alias command preference values. Setting the alias command preference keyword allows the default preference set with the max-dn command to be overridden. See the Configuring Call Rerouting section for more information on using the max-dn command with the alias command.

You must reboot the router to reduce the limit of the directory numbers or virtual voice ports after the maximum allowable
                                                         number is configured.

Step 4

max-ephones max-ephones

#### Example:

```
Router(config-cm-fallback)# max-ephones 24
```

Configures the maximum number of Cisco IP phones that can be supported by the router. The default is 0. The maximum number
                                             is platform dependent. See Compatibility Information for further details.

You must reboot the router to reduce the limit of Cisco IP phones after the maximum allowable number is configured.

Step 5

limit-dn phone-type max-lines

#### Example:

```
Router(config-cm-fallback)# limit-dn 7945 2
```

Optional) Limits the directory number lines on Cisco IP phones during Cisco Unified CM fallback.

You must configure this command during initial Cisco Unified SRST router configuration, before any phone actually registers
                                                         with the Cisco Unified SRST router. However, you can modify the number of lines at a later time.

For a list of available phones, see Cisco SRST and SIP SRST Command Reference (All Versions) .

Step 6

exit

#### Example:

```
Router(config-cm-fallback)# exit
```

Exits call-manager-fallback configuration mode.

### Configuring Cisco Unified 8941 and 8945 SCCP IP Phones

To configure Cisco Unified 8941 and 8945 SCCP IP Phones in Unified SRST mode, perform the following commands:

This section is required only in SRST version 8.6 and is not required for version 8.8 and higher.

### SUMMARY STEPS

- enable

- configure terminal

- ephone-type phone-type

- device-id number

- device-type phone-type

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

ephone-type phone-type

#### Example:

```
phone-type
```

Enters phone type to configure.

8941

8945

Step 4

device-id number

#### Example:

```
Router(config-ephone-type)# device-id 586
```

Specifies the device ID for the phone type.

8941—586

8945—585

Step 5

device-type phone-type

#### Example:

```
Router(config-ephone-type)# device-type 8941
```

Specifies the device type for the phone.

8941

8945

Step 6

end

#### Example:

```
Router(config-ephone-type)# end
```

Returns to privileged EXEC mode.

### Verifying That Cisco Unified SRST Is Enabled

To verify that the Cisco Unified SRST feature is enabled, perform the following steps:

Enter the show running-config command to verify the configuration.

Enter the show call-manager-fallback all command to verify that the Cisco Unified SRST feature is enabled.

Use the Settings display on the Cisco IP phones in your network to verify that the default router IP address on the phones
                                    matches the IP address of the Cisco Unified SRST router.

To temporarily block the TCP port 2000 Skinny Client Control Protocol (SCCP) connection for one of the Cisco IP phones to
                                    force the Cisco IP phone to lose its connection to the Cisco Unified Communications Manager and register with the Cisco Unified
                                    SRST router, perform the following steps:

Use the appropriate IP access-list command to temporarily disconnect a Cisco Unified IP Phone from the Cisco Unified Communications Manager. During a WAN connection
                                          failure, when Cisco Unified SRST is enabled, Cisco Unified IP Phones display a message informing you that they are operating
                                          in Cisco Unified Communications Manager fallback mode. The Cisco IP Phone 7960 and Cisco IP Phone 7940 display a “CM Fallback
                                          Service Operating” message, and the Cisco IP Phone 7910 displays a “CM Fallback Service” message when operating in Cisco Unified Communications
                                          Manager fallback mode. When the Cisco Unified Communications Manager is restored, the message goes away and full Cisco IP phone
                                          functionality is restored.

Use the debug ephone register command to observe the registration process of the Cisco IP phone on the Cisco Unified SRST router.

Use the show ephone command to display the Cisco IP phones that have registered to the Cisco Unified SRST router.

Enter the no form of the appropriate access-list command to restore normal service for the phone.

### Configuring IP Phone Clock, Date, and Time Formats

The Cisco Unified IP Phone 7970G and Cisco Unified IP Phone 7971G-GE IP phones obtain the correct timezone from Cisco Unified
                                 Communications Manager. They also receive the Coordinated Universal Time (UTC) time from the SRST router during SRST registration.
                                 When in SRST mode, the phones take the timezone and the UTC time, and apply a timezone offset to produce the correct time
                                 display.

Cisco IP Phone 7960 IP phones and other similar SCCP phones such as the Cisco IP Phone 7940, get their display clock information
                                 from the local time of the SRST router during SRST registration. If the Cisco Unified SRST router is configured to use the
                                 Network Time Protocol (NTP) to automatically sync the Cisco Unified SRST router time from an NTP time server, only UTC time
                                 is delivered to the router. This is because the NTP server could be physically located anywhere in the world, in any timezone.
                                 As it is important to display the correct local time, use the clock timezone command to adjust or offset the Cisco Unified
                                 SRST router time.

The date and time formats that appear on the displays of all Cisco Unified IP Phones in Cisco Unified CM fallback mode are
                                 selected using the date-format and time-format commands as configured below:

### SUMMARY STEPS

- clock timezone zone hours-offset [ minutes-offset ]

- call-manager-fallback

- date-format { mm-dd-yy | dd-mm-yy | yy-dd-mm | yy-mm-dd }

- time-format [ 12 | 24 ]

- exit

### DETAILED STEPS

Step 1

clock timezone zone hours-offset [ minutes-offset ]

#### Example:

```
Router(config)# clock timezone PST -8
```

Sets the time zone for display purposes.

zone : Name of the time zone to be displayed when standard time is in effect. The length of the zone argument is limited to 7 characters.

hours-offset : The number of hour difference from Coordinated Universal Time (UTC).

minutes-offset (Optional). Minutes difference from UTC.

Step 2

call-manager-fallback

#### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 3

date-format { mm-dd-yy | dd-mm-yy | yy-dd-mm | yy-mm-dd }

#### Example:

```
Router(config-cm-fallback)# date-format
yy-dd-mm
```

Sets the date format for IP phone display. The choices are mm-dd-yy , dd-mm-yy , yy-dd-mm , and yy-mm-dd , where

dd : day

mm : month

yy : year

The default is set to mm-dd-yy.

Step 4

time-format [ 12 | 24 ]

#### Example:

```
Router(config-cm-fallback)# time-format 24
```

Sets the time display format on all Cisco Unified IP Phones registered with the router. The default is set to a 12-hour clock.

Step 5

exit

#### Example:

```
Router(config-cm-fallback)# exit
```

Exits call-manager-fallback configuration mode.

#### Example

The following example sets the time zone to Pacific Standard Time (PST), which is 8 hours behind UTC and sets the time display
                                 format to a 24 hour clock:

```
Router(config)# clock timezone PST -8
Rounter(config)# call-manager-fallback
Rounter(config-cm-fallback)# time-format 24
```

### Configuring IP Phone Language Display

During Cisco Unified CM fallback, the language displays shown on Cisco Unified IP Phones default to the ISO-3166 country code
                                 of US (United States). The Cisco Unified IP Phone 7940 and Cisco Unified IP Phone 7960 can be configured for different languages
                                 (character sets and spelling conventions) using the user-locale command.

This configuration option is available in Cisco SRST V2.1 and later versions running under Cisco Unified CM V3.2 and later
                                             versions. Systems with software prior to Cisco Unified SRST V2.1 and Cisco Unified CM V3.2 can use the default country, United
                                             States (US), only.

### SUMMARY STEPS

- call-manager-fallback

- configure terminal

- user-locale country-code

- exit

### DETAILED STEPS

Step 1

call-manager-fallback

#### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

user-locale country-code

#### Example:

```
Router(config-cm-fallback)# user-locale ES
```

Selects a language by country for displays on the Cisco IP Phone 7940 and Cisco IP Phone 7960.

The following ISO-3166 codes are available to Cisco SRST and Cisco Unified SRST systems running under Cisco Communications
                                             Manager V3.2 or later versions:

DE

DK : Danish.

ES : Spanish.

FR : French.

IT : Italian.

JP : Japanese Katakana (available under Cisco Unified Communications Manager V4.0 or later versions).

NL : Dutch.

NO : Norwegian.

PT : Portuguese.

RU : Russian.

SE : Swedish.

US : United States English (default).

Step 4

exit

#### Example:

```
Router(config-cm-fallback)# exit
```

Exits call-manager-fallback configuration mode.

#### Example

The following example offers a configuration for the Portugal user locale:

```
call-manager-fallback
user-locale PT
```

### Configuring Customized System Messages for Cisco Unified IP Phones

Use the system message command to customize the system message displayed on all Cisco Unified IP Phones during Cisco Unified
                                 CM fallback.

One of two keywords, primary and secondary, must be included in the command. The primary keyword is for IP phones that can
                                 support static text messages during fallback. The default display message for primary IP phones in fallback mode is “CM Fallback
                                 Service Operating.”

The secondary keyword is for Cisco Unified IP Phones that do not support static text messages and have a limited display space.
                                 Secondary IP phones flash messages during fallback. The default display message for secondary IP phones in fallback mode is
                                 “CM Fallback Service.”

Changes to the display message will occur immediately after configuration or at the end of each call.

The normal in-service static text message is controlled by Cisco Unified Communications Manager.

### SUMMARY STEPS

- call-manager-fallback

- system message { primary primary-string | secondary secondary-string }

- exit

### DETAILED STEPS

Step 1

call-manager-fallback

#### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 2

system message { primary primary-string | secondary secondary-string }

#### Example:

```
Router(config-cm-fallback)# system message primary Custom Message
```

Declares the text for the system display message on IP phones in fallback mode.

primary primary-string : For Cisco Unified IP Phones that can support static text messages during fallback, such as the Cisco Unified IP Phone 7940
                                                   and Cisco Unified IP Phone 7960 units. A string of approximately 27 to 30 characters is allowed.

secondary secondary-string : For Cisco Unified IP Phones that do not support static text messages, such as the Cisco Unified IP Phone 7910. A string
                                                   of approximately 20 characters is allowed.

Step 3

exit

#### Example:

```
Router(config-cm-fallback)# exit
```

Exits call-manager-fallback configuration mode.

#### Example

The following example sets “SRST V3.0” as the system display message for all Cisco Unified IP Phones on a router:

```
call-manager-fallback
 system message primary SRST V3.0
 system message secondary SRST V3.0
 exit
```

### Configuring a Secondary Dial Tone

A secondary dial tone can be generated when a phone user dials a predefined PSTN access prefix and can be terminated when
                                 additional digits are dialed. An example is when a secondary dial tone is heard after the number 9 is dialed to reach an outside
                                 line.

### SUMMARY STEPS

- call-manager-fallback

- secondary-dialtone digit-string

- exit

### DETAILED STEPS

Step 1

call-manager-fallback

#### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 2

secondary-dialtone digit-string

#### Example:

```
Router(config-cm-fallback)# secondary-dialtone 9
```

Activates a secondary dial tone when a digit string is dialed.

Step 3

exit

#### Example:

```
Router(config-cm-fallback)# exit
```

Exits call-manager-fallback configuration mode.

#### Example

The following example sets the number 8 to trigger a secondary dial tone:

```
call-manager-fallback
secondary-dialtone 8
```

### Configuring Dual-Line Phones

Dual-line phone configuration is required for dual-line phone operation during Cisco Unified CM fallback, see the Enabling Consultative Call Transfer and Forward Using H.450.2 and H.450.3 with Cisco SRST 3.0 section.

Dual-line IP phones are supported during Cisco Unified CM fallback using the max-dn command. Dual-line IP phones have one voice port with two channels to handle two independent calls. This capability enables
                                 call waiting, call transfer, and conference functions on a phone-line button.

In dual-line mode, each IP phone and its associated line button can support one or two calls. Selection of one of two calls
                                 on the same line is made using the blue Navigation button located below the phone display. When one of the dual-line channels
                                 is used on a specific phone, other phones that share the ephone-dn will be unable to use the secondary channel. The secondary
                                 channel will be reserved for use with the primary dual-line channel.

It is recommended that hunting be disabled to the second channel. For more information, see the Configuring Dial-Peer and Channel Hunting section.

### SUMMARY STEPS

- call-manager-fallback

- max-dn max-directory-numbers [ dual-line ][ preference preference-order ]

- exit

### DETAILED STEPS

Step 1

call-manager-fallback

#### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 2

max-dn max-directory-numbers [ dual-line ][ preference preference-order ]

#### Example:

```
Router(config-cm-fallback)# max-dn 15 dual-line preference 1
```

Sets the maximum number of directory numbers (DNs) or virtual voice ports that can be supported by the router and activates
                                             dual-line mode.

max-directory-numbers :Maximum number of directory numbers (dns) or virtual voice ports supported by the router. The maximum number is platform-dependent.
                                                   The default is 0. See Compatibility Information for further details.

dual-line (Optional). Allows IP phones in Cisco Unified Communications Manager fallback mode to have a virtual voice port with two
                                                   channels.

preference preference-order (Optional). Sets the global preference for creating the VoIP dial peers for all directory numbers that are associated with
                                                   the primary number. Range is from 0 to 10. Default is 0, which is the highest preference.

The alias command also has a preference keyword that sets alias command preference values. Setting the alias command preference keyword allows the default preference set with the max-dn command to be overridden. See the Configuring Call Rerouting section for more information on using the max-dn command with the alias command.

Step 3

exit

#### Example:

```
Router(config-cm-fallback)# exit
```

Exits call-manager-fallback configuration mode.

#### Example

The following example sets the maximum number of DNs or virtual voice ports that can be supported by a router to 10 and activates
                                 the dual-line mode for all IP phones in Cisco Unified CM fallback mode:

```
call-manager-fallback
 max-dn 10 dual-line
 exit
```

### Configuring Eight Calls per Button (Octo-Line)

The octo-line feature supports up to eight active calls, both incoming and outgoing, on a single button. Eight incoming calls
                                 to an octo-line directory number ring simultaneously. After an incoming call is answered, the ringing stops and the remaining
                                 seven incoming calls hear a call waiting tone.

After an incoming call on an octo-line directory number is answered, the answering phone is in the connected state. Other
                                 phones that share the directory number are in the remoteMultiline state. A subsequent incoming call sends the call waiting
                                 tone to the phone connected to the call, and sends the ringing tone to the other phones that are in the remoteMultiline state.
                                 All phones sharing the directory number can pick up any of the incoming unanswered calls.

When multiple incoming calls ring on an octo-line directory number that is shared among multiple phones, the ringing tone
                                 stops on the phone that answers the call, and the call waiting tone is heard for other unanswered calls. The multiple instances
                                 of the ringing calls is displayed on other ephones sharing the directory number. After a connected call on an octo-line directory
                                 number is put on-hold, any phone that shares this directory number can pick up the held call. If a phone is in the process
                                 of transferring a call or creating a conference, other phones that share the octo-line directory number cannot steal the call.

As new calls come in on an octo-line, the system searches for the next available idle line using the huntstop chan tag command, where tag is a number from 1 to 8. An idle channel is selected from the lowest number to the highest. When the highest number of allowed
                                 calls is received, the system stops hunting for available channels. Use this command to limit the number of incoming calls
                                 on an octo-line directory number and reserve channels for outgoing calls or features such as call transfer or conference calls.

With the new feature, you can:

Configure only dual-line mode

Configure only octo-line mode

Configure dual-line mode and octo-line mode

Octo-line directory numbers are not supported by the Cisco Unified IP Phone 7902, 7920, or 7931, or by analog phones connected
                                 to Cisco ATA or Cisco VG224.

#### Before you begin

Cisco Unified SRST 7.0/4.3

Cisco Unified CM 6.0

Cisco IOS Release 12.4(15)XZ

### SUMMARY STEPS

- enable

- configure terminal

- call-manager-fallback

- max-dn max-no-of-directories [ dual-line | octo-line ] [ number octo-line ]

- huntstop channel 1-8

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

call-manager-fallback

#### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 4

max-dn max-no-of-directories [ dual-line | octo-line ] [ number octo-line ]

#### Example:

```
Router(config-cm-fallback)# max-dn 15 dual-line
6 octo-line
```

Sets the maximum number of DNs or virtual voice ports that can be supported by the router and activates dual-line mode, octo-line
                                             mode, or both modes.

max-no-of-directories : Maximum number of directory numbers (dns) or virtual voice ports supported by the router. The maximum number is platform-dependent.
                                                   The default is 0.

dual-line : (Optional) Allows IP phones in Cisco Unified Communications Manager fallback mode to have a virtual voice port with two
                                                   channels.

octo-line : (Optional) Allows IP phones in Cisco Unified Communications Manager fallback mode to have a virtual voice port with eight
                                                   channels.

number (Optional): Sets the number of directory numbers for octo-mode.

Step 5

huntstop channel 1-8

#### Example:

```
Router(config-cm-fallback)# huntstop channel 4
```

Enables channel huntstop on an octo-line, which keeps a call from hunting to the next channel of a directory number if the
                                             last allowed channel is busy or does not answer.

number : Number of channels available to accept incoming calls. The remaining channels are reserved for outgoing calls and features
                                                   such as call transfer, call waiting, and conferencing. The range is 1 to 8 and the default is 8.

The command is supported for octo-line directory numbers only.

Step 6

end

#### Example:

```
Router(config)# end
```

Returns to privileged EXEC mode.

#### Example

In the following example, octo-line mode is enabled, there are 8 octo-line directory numbers, there are a maximum of 23 directory
                                 numbers, and a maximum of 6 channels are available for incoming calls:

```
!
call-manager-fallback
max-dn 23 octo-line 8
huntstop channel 6
```

### Configuring the Maximum Number of Calls

To configure the maximum number of calls on a Cisco Unified SCCP IP phone in Cisco Unified SRST 9.0, perform the following
                                 steps.

#### Before you begin

Cisco Unified SRST 9.0 and later versions.

Correct firmware, 9.2(1) or a later version, is installed.

### SUMMARY STEPS

- enable

- configure terminal

- call-manager-fallback

- max-dn max-no-of-directories [ dual-line | octo-line ]

- timeouts busy seconds

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

call-manager-fallback

#### Example:

```
Router(config)# call-manager-fallback
```

Enables Cisco Unified SRST support and enters call-manager-fallback configuration mode.

Step 4

max-dn max-no-of-directories [ dual-line | octo-line ]

#### Example:

```
Router(config-cm-fallback)# max-dn 10 octo-line
```

Sets the maximum possible number of directory numbers or virtual voice ports that can be supported by a router and enables
                                             dual-line mode, octo-line mode, or both modes.

max-no-of-directories —Maximum number of directory numbers or virtual voice ports supported by the router. The maximum possible number is platform-dependent.
                                                   The default is 0 directory numbers and 1 channel per virtual port.

dual-line —(Optional) Sets all Cisco Unified IP phones connected to a Cisco Unified SRST router to one virtual voice port with two channels.

octo-line —(Optional) Sets all Cisco Unified IP phones connected to a Cisco Unified SRST router to one virtual voice port with eight
                                                   channels.

Step 5

timeouts busy seconds

#### Example:

```
Router(config-cm-fallback)# timeouts busy 10
```

Sets the timeout value for call transfers to busy destinations.

seconds —Number of seconds after connection to a busy destination before a transferred call is disconnected. Range is 0 to 30. Default:
                                                   10.

Step 6

end

#### Example:

```
Router(config-cm-fallback)# end
```

Exits configuration mode and enters privileged EXEC mode.

### Troubleshooting

To troubleshoot your Cisco Unified SRST configuration, use the following commands:

To set keepalive debugging for Cisco IP phones, use the debug ephone keepalive command.

To set registration debugging for Cisco IP phones, use the debug ephone register command.

To set state debugging for Cisco IP phones, use the debug ephone state command.

To set detail debugging for Cisco IP phones, use the debug ephone detail command.

To set error debugging for Cisco IP phones, use the debug ephone error command.

To set call statistics debugging for Cisco IP phones, use the debug ephone statistics command.

To provide voice-packet-level debugging and to display the contents of one voice packet in every 1024 voice packets, use the debug ephone pak command.

To provide raw low-level protocol debugging display for all SCCP messages, use the debug ephone raw command.

For further debugging, see Cisco IOS Debug Command Reference .

## How to Set Up Cisco IP Communicator for Cisco Unified SRST

Cisco IP Communicator is a software-based application that delivers enhanced telephony support on personal computers. Cisco
                           IP Communicator appears on a user’s computer monitor as a graphical, display-based IP phone with a color screen, a keypad,
                           feature buttons, and soft keys.

For information about operation, see the Cisco IP Communicator online help and user documentation .

### Prerequisites

You should have the following before you begin this task:

IP address of the Cisco Unified CM (Call Manager) TFTP server

IP address of the Cisco Unified SRST TFTP server

Headset with microphone for your PC (Optional; you can use PC internal speakers and microphone)

Download the latest version of the Cisco IP Communicator software and install it on your PC. The software is available for
                                    download at http://www.cisco.com/cisco/web/download/index.html .

Click Voice and Unified Communication .

Click IP Telephony .

Click IP Phones .

Click Cisco IP Communicator .

(Optional) Attach a headset to your PC.

Start the Cisco IP Communicator software application.

Define the IP address of the Cisco Unified CM as primary TFTP server

Open the Network > User Preferences window .

Enter the IP address of the Cisco Unified CM TFTP server.

Define the IP address of the Cisco Unified SRST as secondary TFTP server

Open the Network > User Preferences window .

Enter the IP address of the Cisco Unified SRST TFTP server.

Ensure that Cisco IP Communicator has at least once registered to Cisco Unified CM. For more details, see Install and Configure IP Communicator with CallManager .

Wait for the Cisco IP Communicator to connect to the Cisco Unified SRST system (upon Cisco Unified CM Failure) and register
                                    itself.

Cisco IP Communicator should have retained the original buttons and numbers for Cisco IP Communicator.

### Verifying Cisco IP Communicator

### SUMMARY STEPS

- Use the show running-config command to display ephone-dn and ephone information associated with this phone.

- After Cisco IP Communicator registers with Cisco Unified SRST, it displays the phone extensions and soft keys in its configuration.
                                 Verify that these are correct.

- Make a local call from the phone and ask someone to call you. Verify that you have a two-way voice path.

### DETAILED STEPS

Step 1

Use the show running-config command to display ephone-dn and ephone information associated with this phone.

Step 2

After Cisco IP Communicator registers with Cisco Unified SRST, it displays the phone extensions and soft keys in its configuration.
                                          Verify that these are correct.

Step 3

Make a local call from the phone and ask someone to call you. Verify that you have a two-way voice path.

### Troubleshooting Cisco IP Communicator

Use the debug ephone detail command to diagnose problems with calls. For more information, see Cisco IOS Debug Command Reference .

## Multicast Music On Hold

For Unified SRST 3.0 and later versions, you can configure the MOH audio stream as a multicast source. A Unified SRST router
                           that is configured for multicast MOH also transmits the audio stream on the physical IP interfaces of the specified router
                           to permit access to the stream by external devices. Certain IP phones do not support multicast MOH because they do not support
                           IP multicast. You can disable multicast MOH to individual phones that do not support multicast. Callers hear a repeating tone
                           when they are placed on hold.

Multicast MOH on Unified SRST is supported for both SIP and SCCP phones. Support is offered for G.711 and G.729 codecs with
                           multicast MOH on Unified SRST. Multicast MOH is supported on Cisco Integrated Services Router Generation 2 (ISR G2) and the
                           Cisco 4000 Series Integrated Services Routers.

For SIP phones to play the Multicast MOH, you need to configure the CLI command moh enable-g711 filename (for example, moh enable-g711 flash:en_bacd_music_on_hold.au or moh g729 flash:SampleAudioSource.g729.wav ). For SCCP phones to play Multicast MOH, you need to configure the CLI command multicast moh ip-address port port-number [ route ip-address-list ] (for example, multicast moh 239.1.1.1 port 2000 ), apart from the CLI command moh f ilename . If both the CLI commands are not configured, SCCP phones will only play tone on hold.

For more information on supporting Multicast MOH with Unified SRST for a scenario where WAN is available, see Information About Using Cisco Unified SRST Gateways as a Multicast MOH Resource .

### Configure Multicast Music On Hold for Unified SRST

#### Before you begin

To configure multicast MOH for Unified SRST, perform the following steps:

Unified SRST 3.0 or later versions.

IP phones do not support multicast at 224.x.x.x addresses.

### SUMMARY STEPS

- enable

- configure terminal

- call-manager-fallback

- moh filename

- multicast moh ip-address port port number [ route ip-address-list ]

- exit

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

call-manager-fallback

#### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 4

moh filename

#### Example:

```
Router(config-cm-fallback)# moh enable-g711
"flash:en_bacd_music_on_hold.au"
```

OR

```
Router(config-cm-fallback)# moh g729
flash:SampleAudioSource.g729.wav
```

Enables music on hold using the specified file.

If you specify a file with this command and later want to use a different file, you must disable use of the first file with
                                                   the no moh command before configuring the second file.

Step 5

multicast moh ip-address port port number [ route ip-address-list ]

#### Example:

```
Router(config-cm-fallback)# multicast moh 239.1.1.1
port 2000
```

Specifies that this audio stream is to be used for multicast and also for MOH.

This command is required to use MOH for internal calls and it must be configured after MOH is enabled with the moh command.

ip-address—Destination IP address for multicast.

port port-number—Media port for multicast. Range is 2000 to 65535. We recommend port 2000 because it is already used for normal
                                                   RTP media transmissions between IP phones and the router.

Valid port numbers for multicast include even numbers that range from 16384 to 32767. (The system reserves odd values.)

route—(Optional) List of explicit router interfaces for the IP multicast packets.

ip-address-list—(Optional) List of up to four explicit routes for multicast MOH. The default is that the MOH multicast stream
                                                   is automatically output on the interfaces that correspond to the address that was configured with the ip source-address command.

For MOH on internal calls, packet flow must be enabled to the subnet on which the phones are located.

Step 6

exit

#### Example:

```
Router(config-cm-fallback)# exit
```

Exits call-manager-fallback configuration mode.

## Where to Go Next

The next step is configuring Cisco Unified IP Phones using SIP. For more information, see the Setting Up Cisco Unified IP Phones using SIP section.

For additional information, see the Related Documents and References section.

| Note | Ciso Unified IP Phones discussed in this chapter are just examples. For a complete list of IP phones, see Compatibility Information . |
|---|---|

| Note | When the Cisco Unified SRST is enabled, Cisco Unified IP Phones do not have to be reconfigured while in Cisco Unified Communications
                                             Manager fallback mode because phones retain the same configuration that was used with Cisco Unified Communications Manager. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 2 | ip source-address ip-address [ port port ] [ any-match \| strict-match ] Example: Router(config-cm-fallback)# ip source-address
10.6.21.4 port 2002 strict-match | Enables the router to receive messages from the Cisco IP phones through the specified IP addresses and provides for strict
                                             IP address verification. The default port number is 2000. |
| Step 3 | max-dn max-directory-numbers [ dual-line ][ preference preference-order ] Example: Router(config-cm-fallback)# max-dn 15 dual-line preference 1 | Sets the maximum number of directory numbers (DNs) or virtual voice ports that can be supported by the router and activates
                                             dual-line mode. max-directory-numbers :Maximum number of directory numbers (dns) or virtual voice ports supported by the router. The maximum number is platform-dependent.
                                                   The default is 0. See Compatibility Information for further details. dual-line (Optional). Allows IP phones in Cisco Unified Communications Manager fallback mode to have a virtual voice port with two
                                                   channels. preference preference-order (Optional). Sets the global preference for creating the VoIP dial peers for all directory numbers that are associated with
                                                   the primary number. Range is from 0 to 10. Default is 0, which is the highest preference. The alias command also has a preference keyword that sets alias command preference values. Setting the alias command preference keyword allows the default preference set with the max-dn command to be overridden. See the Configuring Call Rerouting section for more information on using the max-dn command with the alias command. Note You must reboot the router to reduce the limit of the directory numbers or virtual voice ports after the maximum allowable
                                                         number is configured. | Note | You must reboot the router to reduce the limit of the directory numbers or virtual voice ports after the maximum allowable
                                                         number is configured. |
| Note | You must reboot the router to reduce the limit of the directory numbers or virtual voice ports after the maximum allowable
                                                         number is configured. |
| Step 4 | max-ephones max-ephones Example: Router(config-cm-fallback)# max-ephones 24 | Configures the maximum number of Cisco IP phones that can be supported by the router. The default is 0. The maximum number
                                             is platform dependent. See Compatibility Information for further details. Note You must reboot the router to reduce the limit of Cisco IP phones after the maximum allowable number is configured. | Note | You must reboot the router to reduce the limit of Cisco IP phones after the maximum allowable number is configured. |
| Note | You must reboot the router to reduce the limit of Cisco IP phones after the maximum allowable number is configured. |
| Step 5 | limit-dn phone-type max-lines Example: Router(config-cm-fallback)# limit-dn 7945 2 | Optional) Limits the directory number lines on Cisco IP phones during Cisco Unified CM fallback. Note You must configure this command during initial Cisco Unified SRST router configuration, before any phone actually registers
                                                         with the Cisco Unified SRST router. However, you can modify the number of lines at a later time. For a list of available phones, see Cisco SRST and SIP SRST Command Reference (All Versions) . | Note | You must configure this command during initial Cisco Unified SRST router configuration, before any phone actually registers
                                                         with the Cisco Unified SRST router. However, you can modify the number of lines at a later time. For a list of available phones, see Cisco SRST and SIP SRST Command Reference (All Versions) . |
| Note | You must configure this command during initial Cisco Unified SRST router configuration, before any phone actually registers
                                                         with the Cisco Unified SRST router. However, you can modify the number of lines at a later time. For a list of available phones, see Cisco SRST and SIP SRST Command Reference (All Versions) . |
| Step 6 | exit Example: Router(config-cm-fallback)# exit | Exits call-manager-fallback configuration mode. |

| Note | You must reboot the router to reduce the limit of the directory numbers or virtual voice ports after the maximum allowable
                                                         number is configured. |
|---|---|

| Note | You must reboot the router to reduce the limit of Cisco IP phones after the maximum allowable number is configured. |
|---|---|

| Note | You must configure this command during initial Cisco Unified SRST router configuration, before any phone actually registers
                                                         with the Cisco Unified SRST router. However, you can modify the number of lines at a later time. For a list of available phones, see Cisco SRST and SIP SRST Command Reference (All Versions) . |
|---|---|

| Note | This section is required only in SRST version 8.6 and is not required for version 8.8 and higher. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | ephone-type phone-type Example: phone-type | Enters phone type to configure. 8941 8945 |
| Step 4 | device-id number Example: Router(config-ephone-type)# device-id 586 | Specifies the device ID for the phone type. 8941—586 8945—585 |
| Step 5 | device-type phone-type Example: Router(config-ephone-type)# device-type 8941 | Specifies the device type for the phone. 8941 8945 |
| Step 6 | end Example: Router(config-ephone-type)# end | Returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | clock timezone zone hours-offset [ minutes-offset ] Example: Router(config)# clock timezone PST -8 | Sets the time zone for display purposes. zone : Name of the time zone to be displayed when standard time is in effect. The length of the zone argument is limited to 7 characters. hours-offset : The number of hour difference from Coordinated Universal Time (UTC). minutes-offset (Optional). Minutes difference from UTC. |
| Step 2 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 3 | date-format { mm-dd-yy \| dd-mm-yy \| yy-dd-mm \| yy-mm-dd } Example: Router(config-cm-fallback)# date-format
yy-dd-mm | Sets the date format for IP phone display. The choices are mm-dd-yy , dd-mm-yy , yy-dd-mm , and yy-mm-dd , where dd : day mm : month yy : year The default is set to mm-dd-yy. |
| Step 4 | time-format [ 12 \| 24 ] Example: Router(config-cm-fallback)# time-format 24 | Sets the time display format on all Cisco Unified IP Phones registered with the router. The default is set to a 12-hour clock. |
| Step 5 | exit Example: Router(config-cm-fallback)# exit | Exits call-manager-fallback configuration mode. |

| Note | This configuration option is available in Cisco SRST V2.1 and later versions running under Cisco Unified CM V3.2 and later
                                             versions. Systems with software prior to Cisco Unified SRST V2.1 and Cisco Unified CM V3.2 can use the default country, United
                                             States (US), only. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | user-locale country-code Example: Router(config-cm-fallback)# user-locale ES | Selects a language by country for displays on the Cisco IP Phone 7940 and Cisco IP Phone 7960. The following ISO-3166 codes are available to Cisco SRST and Cisco Unified SRST systems running under Cisco Communications
                                             Manager V3.2 or later versions: DE : German. DK : Danish. ES : Spanish. FR : French. IT : Italian. JP : Japanese Katakana (available under Cisco Unified Communications Manager V4.0 or later versions). NL : Dutch. NO : Norwegian. PT : Portuguese. RU : Russian. SE : Swedish. US : United States English (default). |
| Step 4 | exit Example: Router(config-cm-fallback)# exit | Exits call-manager-fallback configuration mode. |

| Note | The normal in-service static text message is controlled by Cisco Unified Communications Manager. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 2 | system message { primary primary-string \| secondary secondary-string } Example: Router(config-cm-fallback)# system message primary Custom Message | Declares the text for the system display message on IP phones in fallback mode. primary primary-string : For Cisco Unified IP Phones that can support static text messages during fallback, such as the Cisco Unified IP Phone 7940
                                                   and Cisco Unified IP Phone 7960 units. A string of approximately 27 to 30 characters is allowed. secondary secondary-string : For Cisco Unified IP Phones that do not support static text messages, such as the Cisco Unified IP Phone 7910. A string
                                                   of approximately 20 characters is allowed. |
| Step 3 | exit Example: Router(config-cm-fallback)# exit | Exits call-manager-fallback configuration mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 2 | secondary-dialtone digit-string Example: Router(config-cm-fallback)# secondary-dialtone 9 | Activates a secondary dial tone when a digit string is dialed. |
| Step 3 | exit Example: Router(config-cm-fallback)# exit | Exits call-manager-fallback configuration mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 2 | max-dn max-directory-numbers [ dual-line ][ preference preference-order ] Example: Router(config-cm-fallback)# max-dn 15 dual-line preference 1 | Sets the maximum number of directory numbers (DNs) or virtual voice ports that can be supported by the router and activates
                                             dual-line mode. max-directory-numbers :Maximum number of directory numbers (dns) or virtual voice ports supported by the router. The maximum number is platform-dependent.
                                                   The default is 0. See Compatibility Information for further details. dual-line (Optional). Allows IP phones in Cisco Unified Communications Manager fallback mode to have a virtual voice port with two
                                                   channels. preference preference-order (Optional). Sets the global preference for creating the VoIP dial peers for all directory numbers that are associated with
                                                   the primary number. Range is from 0 to 10. Default is 0, which is the highest preference. The alias command also has a preference keyword that sets alias command preference values. Setting the alias command preference keyword allows the default preference set with the max-dn command to be overridden. See the Configuring Call Rerouting section for more information on using the max-dn command with the alias command. |
| Step 3 | exit Example: Router(config-cm-fallback)# exit | Exits call-manager-fallback configuration mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 4 | max-dn max-no-of-directories [ dual-line \| octo-line ] [ number octo-line ] Example: Router(config-cm-fallback)# max-dn 15 dual-line
6 octo-line | Sets the maximum number of DNs or virtual voice ports that can be supported by the router and activates dual-line mode, octo-line
                                             mode, or both modes. max-no-of-directories : Maximum number of directory numbers (dns) or virtual voice ports supported by the router. The maximum number is platform-dependent.
                                                   The default is 0. dual-line : (Optional) Allows IP phones in Cisco Unified Communications Manager fallback mode to have a virtual voice port with two
                                                   channels. octo-line : (Optional) Allows IP phones in Cisco Unified Communications Manager fallback mode to have a virtual voice port with eight
                                                   channels. number (Optional): Sets the number of directory numbers for octo-mode. |
| Step 5 | huntstop channel 1-8 Example: Router(config-cm-fallback)# huntstop channel 4 | Enables channel huntstop on an octo-line, which keeps a call from hunting to the next channel of a directory number if the
                                             last allowed channel is busy or does not answer. number : Number of channels available to accept incoming calls. The remaining channels are reserved for outgoing calls and features
                                                   such as call transfer, call waiting, and conferencing. The range is 1 to 8 and the default is 8. The command is supported for octo-line directory numbers only. |
| Step 6 | end Example: Router(config)# end | Returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enables Cisco Unified SRST support and enters call-manager-fallback configuration mode. |
| Step 4 | max-dn max-no-of-directories [ dual-line \| octo-line ] Example: Router(config-cm-fallback)# max-dn 10 octo-line | Sets the maximum possible number of directory numbers or virtual voice ports that can be supported by a router and enables
                                             dual-line mode, octo-line mode, or both modes. max-no-of-directories —Maximum number of directory numbers or virtual voice ports supported by the router. The maximum possible number is platform-dependent.
                                                   The default is 0 directory numbers and 1 channel per virtual port. dual-line —(Optional) Sets all Cisco Unified IP phones connected to a Cisco Unified SRST router to one virtual voice port with two channels. octo-line —(Optional) Sets all Cisco Unified IP phones connected to a Cisco Unified SRST router to one virtual voice port with eight
                                                   channels. |
| Step 5 | timeouts busy seconds Example: Router(config-cm-fallback)# timeouts busy 10 | Sets the timeout value for call transfers to busy destinations. seconds —Number of seconds after connection to a busy destination before a transferred call is disconnected. Range is 0 to 30. Default:
                                                   10. |
| Step 6 | end Example: Router(config-cm-fallback)# end | Exits configuration mode and enters privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Use the show running-config command to display ephone-dn and ephone information associated with this phone. |  |
| Step 2 | After Cisco IP Communicator registers with Cisco Unified SRST, it displays the phone extensions and soft keys in its configuration.
                                          Verify that these are correct. |  |
| Step 3 | Make a local call from the phone and ask someone to call you. Verify that you have a two-way voice path. |  |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 4 | moh filename Example: Router(config-cm-fallback)# moh enable-g711
"flash:en_bacd_music_on_hold.au" OR Router(config-cm-fallback)# moh g729
flash:SampleAudioSource.g729.wav | Enables music on hold using the specified file. If you specify a file with this command and later want to use a different file, you must disable use of the first file with
                                                   the no moh command before configuring the second file. |
| Step 5 | multicast moh ip-address port port number [ route ip-address-list ] Example: Router(config-cm-fallback)# multicast moh 239.1.1.1
port 2000 | Specifies that this audio stream is to be used for multicast and also for MOH. Note This command is required to use MOH for internal calls and it must be configured after MOH is enabled with the moh command. ip-address—Destination IP address for multicast. port port-number—Media port for multicast. Range is 2000 to 65535. We recommend port 2000 because it is already used for normal
                                                   RTP media transmissions between IP phones and the router. Note Valid port numbers for multicast include even numbers that range from 16384 to 32767. (The system reserves odd values.) route—(Optional) List of explicit router interfaces for the IP multicast packets. ip-address-list—(Optional) List of up to four explicit routes for multicast MOH. The default is that the MOH multicast stream
                                                   is automatically output on the interfaces that correspond to the address that was configured with the ip source-address command. Note For MOH on internal calls, packet flow must be enabled to the subnet on which the phones are located. | Note | This command is required to use MOH for internal calls and it must be configured after MOH is enabled with the moh command. | Note | Valid port numbers for multicast include even numbers that range from 16384 to 32767. (The system reserves odd values.) | Note | For MOH on internal calls, packet flow must be enabled to the subnet on which the phones are located. |
| Note | This command is required to use MOH for internal calls and it must be configured after MOH is enabled with the moh command. |
| Note | Valid port numbers for multicast include even numbers that range from 16384 to 32767. (The system reserves odd values.) |
| Note | For MOH on internal calls, packet flow must be enabled to the subnet on which the phones are located. |
| Step 6 | exit Example: Router(config-cm-fallback)# exit | Exits call-manager-fallback configuration mode. |

| Note | This command is required to use MOH for internal calls and it must be configured after MOH is enabled with the moh command. |
|---|---|

| Note | Valid port numbers for multicast include even numbers that range from 16384 to 32767. (The system reserves odd values.) |
|---|---|

| Note | For MOH on internal calls, packet flow must be enabled to the subnet on which the phones are located. |
|---|---|