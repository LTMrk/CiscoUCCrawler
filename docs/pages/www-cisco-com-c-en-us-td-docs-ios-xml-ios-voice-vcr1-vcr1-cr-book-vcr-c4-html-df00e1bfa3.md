---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-vcr1-vcr1-cr-book-vcr-c4-html-df00e1bfa3
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/vcr1/vcr1-cr-book/vcr-c4.html
retrieved_at: 2026-08-16T23:15:41.432283+00:00
---

Cisco IOS Voice Command Reference - A through C

# Cisco IOS Voice Command Reference - A through C

Updated: April 25, 2026

Chapter: caller-id (dial peer) through ccm-manager switchover-to-backup

## Chapter: caller-id (dial peer) through ccm-manager switchover-to-backup

# caller-id (dial peer) through ccm-manager switchover-to-backup

## caller-id (dial peer)

To enable caller ID, use the caller
                              -
                              id command in dial peer configuration mode. To disable caller ID, use the no form of the command.

caller-id

no caller-id

### Syntax Description

This command contains no arguments or keywords.

### Command Default

Caller ID is disabled

### Command Modes

Dial peer configuration (config-dial-peer)

## Command History

Release

Modification

12.1.(2)XF

This command was introduced on the Cisco 800 series routers.

12.1(5)T

This command was integrated into Cisco IOS Release 12.1(5)T.

### Usage Guidelines

This command is available on Cisco 800 series routers that have plain old telephone service (POTS) ports. The command is effective
                              only if you subscribe to caller ID service. If you enable caller ID on a router without subscribing to the caller ID service,
                              caller ID information does not appear on the telephone display.

The configuration of caller ID must match the device connected to the POTS port. That is, if a telephone supports the caller
                              ID feature, use the caller id command to enable the feature. If the telephone does not support the caller ID feature, use the command default or disable
                              the caller ID feature. Odd ringing behavior might occur if the caller ID feature is disabled when it is a supported telephone
                              feature or enabled when it is not a supported telephone feature.

Specific hardware is required to provide full support for the caller ID features. To determine support for these features
                                          in your configuration, review the appropriate hardware documentation and data sheets. This information is available on Cisco.com.

## Examples

The following example enables a router to use the caller ID feature:

```
dial-peer voice 1 pots
 caller-id
```

### Related Commands

Command

Description

block caller

Configures call blocking on caller ID.

debug pots csm csm

Activates events from which an application can determine and display the status and progress of calls to and from POTS ports.

isdn i-number

Configures several terminal devices to use one subscriber line.

pots call waiting

Enables local call waiting on a router.

registered caller ring

Configures the Nariwake service-registered caller ring cadence.

## caller-id alerting dsp-pre-alloc

To statically allocate a digital signal processor (DSP) resource for receiving caller ID information for on-hook (Type 1)
                              caller ID at a receiving Foreign Exchange Office (FXO) voice port, use the caller-id alerting dsp-pre-alloc command in voice-port configuration mode. To disable the command’s effect, use the no form of this command.

caller-id alerting dsp-pre-alloc

no caller-id alerting dsp-pre-alloc

### Syntax Description

This command contains no arguments or keywords.

### Command Default

No preallocation of DSP resources

### Command Modes

Voice-port configuration (config-voiceport)

## Command History

Release

Modification

12.1(2)XH

This command was introduced on the Cisco MC3810, Cisco 2600 series, and Cisco 3600 series.

12.1(3)T

This command was integrated into Cisco IOS Release 12.1(3)T.

### Usage Guidelines

The caller id alerting dsp pre alloc command may be required on an FXO port if the central office uses line polarity reversal to signal the start of caller-ID
                              information transmission. Preallocating a DSP allows the DSP to listen for caller-ID information continuously without requiring
                              an alerting signal from the central office (CO).

This command is the FXO counterpart to the caller id alerting line reversal command, which is applied to the Foreign Exchange Station (sending) end of the caller-ID call.

Specific hardware is required to provide full support for the caller ID features. To determine support for these features
                                          in your configuration, review the appropriate hardware documentation and data sheets. This information is available on Cisco.com.

## Examples

The following example configures a voice port where caller-ID information is received:

```
voice-port 1/0/1
  cptone US
  caller-id enable
  caller-id alerting line-reversal
  caller-id alerting dsp-pre-alloc
```

### Related Commands

Command

Description

caller-id alerting line-reversal

Sets the line-reversal method of caller-ID call alerting.

## caller-id alerting line-reversal

To set the line-reversal alerting method for caller-ID information for on-hook (Type 1) caller ID at a sending Foreign Exchange
                              Station (FXS) voice port, use the caller id alerting line reversal command in voice-port configuration mode. To disable the command’s effect, use the no form of this command.

caller-id alerting line-reversal

no caller-id alerting line-reversal

### Syntax Description

This command has no arguments or keywords.

### Command Default

No line-reversal alert

### Command Modes

Voice-port configuration (config-voiceport)

## Command History

Release

Modification

12.1(2)XH

This command was introduced.

12.1(3)T

This command was integrated into Cisco IOS Release 12.1(3)T.

### Usage Guidelines

This command is required only when the telephone device attached to an FXS port requires the line-reversal method to signal
                              the start of a caller-ID transmission. Use it on FXS voice ports that send caller-ID information.

This command is the FXS counterpart to the caller id alerting dsp pre alloc command, which is applied to the FXO (receiving) end of the caller-ID call with the line-reversal alerting method.

Specific hardware is required to provide full support for the caller ID features. To determine support for these features
                                          in your configuration, review the appropriate hardware documentation and data sheets. This information is available on Cisco.com.

## Examples

The following example configures a voice port from which caller-ID information is sent:

```
voice-port 1/0/1
   cptone US
   station name  A. sample
   station number 4085550111
   caller-id alerting line-reversal
   caller-id alerting dsp-pre-alloc
```

### Related Commands

Command

Description

caller-id alerting dsp-pre-alloc

At the receiving end of a line-reversal alerting caller-ID call, preallocates DSPs for caller ID calls.

## caller-id alerting pre-ring

To set a 250-millisecond prering alerting method for caller ID information for on-hook (Type 1) caller ID at a sending Foreign
                              Exchange Station (FXS) voice port, use the caller-id alerting pre-ring command in voice-port configuration mode. To disable the command, use the no form of this command.

caller-id alerting pre-ring

no caller-id alerting pre-ring

### Syntax Description

This command has no arguments or keywords.

### Command Default

No prering alert

### Command Modes

Voice-port configuration (config-voiceport)

## Command History

Release

Modification

12.1(2)XH

This command was introduced on the Cisco MC3810, Cisco 2600 series, and Cisco 3600 series.

12.1(3)T

This command was integrated into Cisco IOS Release 12.1(3)T.

### Usage Guidelines

This command is required only when the telephone device attached to an FXS port requires the prering (immediate ring) method
                              to signal the start of caller ID transmission. Use it on FXS voice ports that send caller ID information. This command allows
                              the FXS port to send a short prering preceding the normal ring cadence. On an FXO port, an incoming prering (immediate ring)
                              is simply counted as a normal ring using the caller-id alerting ring command.

Specific hardware is required to provide full support for the caller ID features. To determine support for these features
                                          in your configuration, review the appropriate hardware documentation and data sheets. This information is available on Cisco.com.

## Examples

The following example configures a voice port from which caller ID information is sent:

```
voice-port 1/0/1
   cptone US
   station name  A. sample
   station number 4085550111
   caller-id alerting pre-ring
```

### Related Commands

Command

Description

caller-id alerting line-reversal

Enables caller ID operation and sets the line-reversal alerting type at an FXS port.

caller-id alerting ring

Enables caller ID operation and sets an alerting ring type at an FXO or FXS port.

## caller-id alerting ring

To set the ring-cycle method for receiving caller ID information for on-hook (Type 1) caller ID at a receiving Foreign Exchange
                              Office (FXO) or a sending Foreign Exchange Station (FXS) voice port, use the caller id alerting ring command in voice-port configuration mode. To set the command to the default, use the no form of this command.

caller-id alerting ring { 1 | 2 }

no caller-id alerting ring

### Syntax Description

1

Use this setting if your telephone service provider specifies it to provide caller ID alerting (display) after the first ring
                                          at the receiving station. This is the most common setting.

2

Use this setting if your telephone service provider specifies it to provide caller ID alerting (display) after the second
                                          ring. This setting is used in Australia, where the caller ID information is sent following two short rings (double-pulse ring).

### Command Default

1

### Command Modes

Voice-port configuration (config-voiceport)

## Command History

Release

Modification

12.1(2)XH

This command was introduced.

12.1(3)T

This command was integrated into Cisco IOS Release 12.1(3)T.

### Usage Guidelines

This setting is determined by the Bellcore/Telcordia or ETSI standard that your telephone service provider uses for caller
                              ID. Use it on FXO loop-start and ground-start voice ports where caller ID information arrives and on FXS voice ports from
                              which caller ID information is sent.

This setting must match on the sending and receiving ends of the telephone line connection.

Specific hardware is required to provide full support for the caller ID features. To determine support for these features
                                          in your configuration, review the appropriate hardware documentation and data sheets. This information is available on line.

## Examples

The following example configures a voice port where caller ID information is received:

```
voice-port 1/0/1
   cptone US
   caller-id alerting ring 1
```

The following example configures a voice port from which caller ID information is sent:

```
voice-port 1/0/1
   cptone northamerica
   station name A. sample
   station number 4085550111
   caller-id alerting ring 1
```

### Related Commands

Command

Description

caller-id alerting line-reversal

Enables caller ID operation and sets the line-reversal alerting type at an FXS port.

caller-id alerting pre-ring

Enables caller ID operation and sets the pre-ring alerting method at an FXS port.

## caller-id attenuation

To set the attenuation for caller ID at a receiving Foreign Exchange Office (FXO) voice port, use the caller-id attenuation command in voice-port configuration mode. To set the command to the default, use the no form of this command.

caller-id attenuation [attenuation]

no caller-id attenuation

### Syntax Description

attenuation

(Optional) specifies the attenuation, in decibels (dB). Range is from 0 to 64. The default is 14.

### Command Default

The default value is 14 dB, signal level of -14 dBm.

### Command Modes

Voice-port configuration (config-voiceport)

## Command History

Release

Modification

12.1(2)XH

This command was introduced.

12.1(3)T

This command was integrated into Cisco IOS Release 12.1(3)T.

### Usage Guidelines

Use this setting to specify the attenuation for a caller ID FXO port. If the setting is not used, the attenuation is set to
                              14 dB, signal level of -14 dBm.

Specific hardware is required to provide full support for the caller ID features. To determine support for these features
                                          in your configuration, review the appropriate hardware documentation and data sheets. This information is available on line.

## Examples

The following example configures a voice port where caller ID information is received:

```
voice-port 1/0/1
   cptone US
   caller-id attenuation 0
```

## caller-id block

To request the blocking of the display of caller ID information at the far end of a call from calls originated at a Foreign
                              Exchange Station (FXS) port, use the caller-id block command in voice-port configuration mode at the originating FXS voice port. To allow the display of caller ID information,
                              use the no form of this command.

caller-id block

no caller-id block

### Syntax Description

This command has no arguments or keywords.

### Command Default

No blocking of caller ID information

### Command Modes

Voice-port configuration (config-voiceport)

## Command History

Release

Modification

12.1(2)XH

This command was introduced.

12.1(3)T

This command was integrated into Cisco IOS Release 12.1(3)T.

### Usage Guidelines

This command is used on FXS voice ports that are used to originate on-net telephone calls. This command affects all calls
                              sent to a far-end FXS station from the configured originating FXS station. Calling number and called number are provided in
                              the H.225 setup message for VoIP, through the H.225 Octet 3A field. Calling name information is included in a display information
                              element.

Cisco-switched calls using Voice over Frame Relay (VoFR) and Voice over ATM (VoATM) carry calling party information in the
                                          Cisco proprietary setup message. For standards-based, point-to-point VoFR (FRF.11) trunks where transparent signaling is applied
                                          for FXS-to-FXO calls, only pass-through of in-band automatic number identification (ANI) is supported. ANI information is
                                          always unblocked for these communications. Interface technology using transparent channel-associated signaling (CAS) can support
                                          only ANI through Feature Group D (in-band MF signaling). The Caller ID feature cannot be used with fixed point-to-point trunk
                                          connects created using the connection trunk command.

Specific hardware is required to provide full support for the caller ID features. To determine support for these features
                                          in your configuration, review the appropriate hardware documentation and data sheets. This information is available on Cisco.com.

## Examples

The following example configures a voice port from which caller ID information is sent:

```
voice-port 1/0/1
   cptone US
   station name A. sample
   station number 4085550111
   caller-id block
```

### Related Commands

Command

Description

caller-id enable

Enables caller ID operation.

## caller-id enable

To allow the sending or receiving of caller-ID information, use the caller-id enable command in voice-port configuration mode at the sending foreign exchange station (FXS) voice port or the receiving foreign
                              exchange office (FXO) voice port. To disable the sending and receiving of caller-ID information, use the no form of this command.

caller-id enable [ type { 1 | 2 }]

no caller-id enable [ type { 1 | 2 }]

### Syntax Description

type

(Optional) Indicates that the following keyword is a caller-ID type.

1 --Type I only. Type I transmits the signal when the receiving phone is on hook.

2 --Type II only. Type II transmits the signal when the receiving phone is off hook, for instance to display the caller ID of
                                                an incoming call when the receiving phone is busy (call-waiting caller ID).

### Command Default

The sending and receiving of caller-ID information is disabled.

### Command Modes

Voice-port configuration (config-voiceport)

## Command History

Release

Modification

12.1(2)XH

This command was introduced.

12.1(3)T

This command was integrated into Cisco IOS Release 12.1(3)T.

12.3(7)T

The type 1 and type 2 keywords were added.

### Usage Guidelines

This command applies to FXS voice ports that send caller-ID information and to FXO ports that receive caller-ID information.
                              Calling number and called number are provided in the H.225.0 setup message for VoIP through the H.225.0 Octet 3A field. Calling
                              name information is included in a display information element.

Some users that do not have caller ID type II support on their phones hear noise when type II caller ID is enabled. The caller-id enable type 1 command allows only type I on the voice port and disables type II, so that the user does not hear this noise.

If this command is used without the optional type keyword, both type I and type II caller ID are enabled.

The no form of this command also clears all other caller-ID configuration settings for the voice port.

Cisco-switched calls using Voice over Frame Relay (VoFR) and Voice over ATM (VoATM) carry calling-party information in the
                                          Cisco-proprietary setup message. For standards-based, point-to-point VoFR (FRF.11) trunks where transparent signaling is applied
                                          for FXS-to-FXO calls, only pass-through of in-band automatic number identification (ANI) is supported. ANI information is
                                          always unblocked for these communications. Interface technology using transparent channel-associated signaling (CAS) can support
                                          only ANI through Feature Group D (in-band multifrequency signaling). Caller ID cannot be used with fixed point-to-point trunk
                                          connections created using the connection trunk command.

If the station name, station number , or a caller-id alerting command is configured on the voice port, caller ID is automatically enabled, and the caller-id enable command is not necessary.

Specific hardware is required to provide full support for the caller-ID features. To determine support for these features
                                          in your configuration, review the appropriate hardware documentation and data sheets. This information is available on line.

## Examples

The following example configures a Cisco 2600 series or Cisco 3600 series router voice port at which caller-ID information
                              is received:

```
voice-port 1/0/1
 cptone US
 caller-id enable
```

The following example configures a Cisco 2600 series or Cisco 3600 series router voice port from which caller-ID information
                              is sent:

```
voice-port 1/0/1
 cptone northamerica
 station name A. sample
 station number 4085550111
 caller-id enable
```

The following example enables only type I caller ID on port 2/0:

```
voice-port 2/0
 caller-id enable type 1
```

### Related Commands

Command

Description

caller-id alerting line-reversal

Enables caller ID operation and sets the line-reversal alerting type at an FXS port.

caller-id alerting pre-ring

Enables caller ID operation and sets the pre-ring alerting method at an FXS port.

caller-id alerting ring

Enables caller ID operation and sets an alerting ring type at an FXO or FXS port.

caller-id block

Disables the sending of caller ID information from an FXS port.

station name

Enables caller ID operation and sets the name sent from an FXS port.

station number

Enables caller ID operation and sets the number sent from an FXS port.

## caller-id mode

To specify a noncountry, standard caller ID mode, use the caller-id mode command in voice port configuration mode at the sending Foreign Exchange Station (FXS) voice port or at the receiving Foreign
                              Exchange Office (FXO) voice port. To allow the caller-ID mode to be country-specific, use the no form of this command.

caller-id mode { BT | FSK | DTMF { start | end } { # | * | A | B | C | D }}

no caller-id mode

### Syntax Description

BT

Specifies Frequency-Shift Keying (FSK) with Dual Tone Alerting Signal (DTAS) used by British Telecom.

FSK

Specifies FSK before or during a call.

DTMF

Specifies dual tone multifrequency (DTMF) digits with the start and end digit codes.

start

Specifies the start digit code.

end

Specifies the end digit code.

#

Specifies the DTMF digit #.

*

Specifies the DTMF digit *.

A

Specifies the DTMF digit A.

B

Specifies the DTMF digit B.

C

Specifies the DTMF digit C.

D

Specifies the DTMF digit D.

### Command Default

The caller-ID mode is disabled.

### Command Modes

Voice port configuration (config-voiceport)

## Command History

Release

Modification

15.2(1)T

This command was introduced.

### Usage Guidelines

This command applies to FXS voice ports that send caller ID information to FXO ports that receive the caller ID information.
                              The start and end digit codes are applicable only for the DTMF mode.

The command default is based on the cptone setting that specifies a regional voice-interface-related tone, ring, and cadence
                              setting. The no form of this command defaults to a country-specific setting.

Specific hardware is required to provide full support for the caller-ID features. To determine support for these features
                                             in your configuration, review the appropriate hardware documentation and data sheets. This information is available on Cisco.com.

## Examples

The following example configures a noncountry, standard caller ID mode of DTMF with a start code and end code:

```
Device> enable Device# configure terminal Device(config)# voice-port 1/0/1 Device(config-voiceport)# caller-id mode DTMF start A end B Device(config-voiceport)# end
```

### Related Commands

Command

Description

caller-id alerting

Defines the caller ID alerting method.

caller-id attenuation

Configures the attenuation for a caller ID FXO voice port.

caller-id block

Blocks caller ID information.

caller-id enable

Enables caller ID operation.

caller-id format

Specifies the caller ID format.

## cancel-call-waiting

To define a feature code for a Feature Access Code (FAC) to enable the Cancel Call Waiting feature, use the cancel-call-waiting command in STC application feature access-code configuration mode. To reset the feature code to its default, use the no form of this command.

cancel-call-waiting keypad-character

no cancel-call-waiting

### Syntax Description

keypad-character

Character string that can be dialed on a telephone keypad (0-9, *, #). Default: 8.

The string can be any of the following:

A single character (0-9, *, #)

Two digits (00-99)

Two to four characters (0-9, *, #) and the leading or ending character must be an asterisk (*) or number sign (#)

### Command Default

Feature code for Cancel Call Waiting is 8.

### Command Modes

STC application feature access-code configuration (config-stcapp-fac)

## Command History

Release

Modification

15.0(1)XA

This command was introduced.

15.1(1)T

This command was integrated into Cisco IOS Release 15.1(1)T.

### Usage Guidelines

This command changes the default value of the feature code for Cancel Call Waiting (8).

If you attempt to configure this command with a value that is already configured for another FAC, speed-dial code, or the
                              Redial FSD, you receive a message. If you configure a duplicate code, the system implements the first matching feature in
                              the order of precedence shown in the output of the show stcapp feature codes command.

If you attempt to configure this command with a value that precludes or is precluded by another FAC, speed-dial code, or the
                              Redial FSD, you receive a message. If you configure a feature code to a value that precludes or is precluded by another code,
                              the system always executes the call feature with the shortest code and ignores the longer code. For example, #1 will always
                              preclude #12 and #123. You must configure a new value for the precluded code in order to enable phone user access to that
                              feature.

To display a list of all FACs, use the show stcapp feature codes command.

## Examples

The following example shows how to change the value of the feature code for cancel call waiting. With this configuration,
                              a phone user must press **9 on the phone keypad to cancel call waiting.

```
Router(config)# stcapp feature access-code Router(config-stcapp-fac)# cancel-call-waiting **9
```

### Related Commands

Command

Description

prefix (stcapp-fac)

Defines the prefix for FACs.

show stcapp feature codes

Displays all FACs.

## caller-number (dial peer)

To associate a type of ring cadence with a specific caller ID, use the caller number command in dial peer voice configuration mode. To disable the type of ring cadence for a specific caller ID, use the no form of this command.

caller-number number ring cadence

no caller-number number ring cadence

### Syntax Description

number

Caller ID for which the user wants to set the cadence. Twenty numbers along with their respective cadences may be set for
                                          each of the plain old telephone service (POTS) ports.

ring cadence

Ring cadence level. The three cadence levels (0, 1, and 2), which differ in duration and cadence, are as follows:

0 --The ring cadence is 1 second on and 2 seconds off (NTT-defined regular ring).

1 --The ring cadence is 0.25 seconds on, 0.2 seconds off, 0.25 seconds on, and 2.3 seconds off (NTT-defined nonregular ring).

2 --The ring cadence is 0.5 seconds on, 0.25 seconds off, 0.25 seconds on, and 2 seconds off (Cisco-defined nonregular ring).

### Command Default

The router does not associate any caller ID with a cadence level. Therefore, there is no distinctive ring.

### Command Modes

Dial peer voice configuration (config-dial-peer)

## Command History

Release

Modification

12.2(8)T

This command was introduced on the Cisco 803, Cisco 804, and Cisco 813 routers.

### Usage Guidelines

You can enter the caller number command for each POTS port. A maximum of 20 caller IDs can be associated with distinct ring cadences. After 20 numbers per
                              port have been set, you cannot set more numbers (and their ring cadences) for that port until you have removed any of the
                              numbers that have already been set. To remove already-set numbers and their ring cadences, use the no form of the caller number command.

The command must be set within each dial peer. Six dial peers are available, you can specify 20 caller IDs per port, for a
                              maximum of 120 caller ID numbers.

If you have already subscribed to Nariwake service, the priority goes to the Nariwake caller ID cadence.

To disable distinctive ringing based on a caller ID number, configure the no caller number command. Disabling the ringing removes the specific cadence that has been set for that particular number. If you have set
                              20 numbers and their ring cadences, you need to set the no caller number command for each of the 20 numbers.

Use the show running config command to check distinctive ringing status.

## Examples

The following output examples show that three caller ID numbers and their ring cadences have been set for POTS port 1 and
                              that five caller ID numbers and their ring cadences have been set for POTS port 2:

```
dial-peer voice 1 pots
 destination-pattern 5550102
 port 1
 no call-waiting
 ring 0
 volume 4
 caller-number 1111111 ring 2
 caller-number 2222222 ring 1
 caller-number 3333333 ring 1
dial-peer voice 2 pots
 destination-pattern 5550110
 port 2
 no call-waiting
 ring 0
 volume 2
 caller-number 4444444 ring 1
 caller-number 6666666 ring 2
 caller-number 7777777 ring 0
 caller-number 8888888 ring 1
 caller-number 9999999 ring 2
```

### Related Commands

Command

Description

call waiting

Enables call waiting.

volume

Configures the receiver volume level in the router.

## calling-info pstn-to-sip

To specify calling information treatment for public switched telephone network (PSTN) to Session Initiation Protocol (SIP)
                              calls, use the calling-info pstn-to-sip command in SIP user agent configuration mode. To disable calling information treatment for PSTN-to-SIP calls, use the no form of this command.

calling-info pstn-to-sip { unscreened discard |  { from | remote-party-id | asserted-id { name set name | number set number }}}

no calling-info pstn-to-sip

### Syntax Description

unscreened discard

(Optional) Specifies that the calling name and number be discarded.

from name set name

(Optional) Specifies that the display-name of the From header is unconditionally set to the configured ASCII string in the
                                          forwarded INVITE message.

from number set number

(Optional) Specifies that the user part of the From header is unconditionally set to the configured ASCII string in the forwarded
                                          INVITE message.

remote-party-id name set name

(Optional) Specifies that the display-name of the Remote-Party-ID header is unconditionally set to the configured ASCII string
                                          in the forwarded INVITE message.

remote-party-id number set number

(Optional) Specifies that the user part of the Remote-Party-ID header is unconditionally set to the configured ASCII string
                                          in the forwarded INVITE message.

asserted-id name set name

(Optional) Specifies that the display-name in the Asserted-ID header is unconditionally set to the configured ASCII string
                                          in the forwarded INVITE message.

asserted-id number set number

(Optional) Specifies that the user part in the Asserted-ID header is unconditionally set to the configured ASCII string in
                                          the forwarded INVITE message.

### Command Default

This command is disabled.

### Command Modes

SIP UA configuration (config-sip-ua)

## Command History

Release

Modification

12.2(13)T

This command was introduced.

12.4(15)T

The asserted-id keyword was added.

### Usage Guidelines

When a call exits the gateway, the calling-info pstn-to-sip treatments are applied.

## Examples

The following example enables calling information treatment for PSTN-to-SIP calls and sets the company name and number:

```
Router(config-sip-ua)# calling-info pstn-to-sip from name set CompanyA Router(config-sip-ua)# calling-info pstn-to-sip from number set 5550101 Router(config-sip-ua)# exit Router(config)# exit Router# show running-config Building configuration...
.
.
.
!
sip-ua 
 calling-info pstn-to-sip from name set CompanyA
 calling-info pstn-to-sip from number set 5550101
 no remote-party-id
!
.
.
.
```

### Related Commands

Command

Description

asserted-id

Sets the privacy level and enables either P-Asserted-Identity (PAI) or P-Preferred-Identity (PPI) privacy headers in outgoing
                                          SIP requests or response messages.

calling-info sip-to-pstn

Specifies calling information treatment for SIP-to-PSTN calls.

debug ccsip events

Enables tracing of SIP SPI events.

debug ccsip messages

Enables tracing SIP messages exchanged between the SIP UA client and the access server.

debug isdn q931

Displays call setup and teardown of ISDN connections.

debug voice ccapi error

Enables tracing error logs in the call control API.

debug voip ccapi in out

Enables tracing the execution path through the call control API.

## calling-info sip-to-pstn

To specify calling information treatment for Session Initiation Protocol (SIP) to public switched telephone network (PSTN)
                              calls, use the calling-info sip-to-pstn command in SIP user agent configuration mode. To disable calling information treatment for SIP-to-PSTN calls, use the no form of this command.

calling-info sip-to-pstn { unscreened discard | name set name | number set number }

no calling-info sip-to-pstn

### Syntax Description

unscreened discard

(Optional) Specifies that the calling name and number be discarded.

name set name

(Optional) Specifies that the calling name be unconditionally set to the configured ASCII string in the forwarded Setup mesage.

number set number

(Optional) Specifies that the calling number be unconditionally set to the configured ASCII string in the forwarded Setup
                                          message.

### Command Default

This command is disabled.

### Command Modes

SIP user agent configuration (config-sip-ua)

## Command History

Release

Modification

12.2(13)T

This command was introduced.

### Usage Guidelines

When a call enters the gateway, the calling-info sip-to-pstn treatments are applied.

## Examples

The following example enables calling information treatment for SIP-to-PSTN calls and sets the company name to CompanyA and
                              the number to 5550100:

```
Router(config-sip-ua)# calling-info sip-to-pstn name set CompanyA Router(config-sip-ua)# calling-info sip-to-pstn number set 5550100 Router(config-sip-ua)# exit Router(config)# exit Router# show running-config Building configuration...
.
.
.
!
sip-ua 
 calling-info sip-to-pstn name set CompanyA
	 calling-info sip-to-pstn number set 5550100
!
.
.
.
```

### Related Commands

Command

Description

debug ccsip events

Enables tracing of SIP SPI events.

debug ccsip messages

Enables SIP SPI message tracing.

debug isdn q931

Displays call setup and teardown of ISDN connections.

debug voip ccapi in out

Enables tracing the execution path through the call control API.

calling-info pstn-to-sip

Specifies calling information treatment for PSTN-to-SIP calls.

## calling-number outbound

To specify automatic number identification (ANI) to be sent out when T1-channel-associated signaling (T1-CAS) Feature Group
                              D-Exchange Access North American (FGD-EANA) is configured as the signaling type, use the calling-number outbound command in dial peer or voice-port configuration mode. To disable this command, use no form of this command.

calling-number outbound { range string1 string2 | sequence string1 . . . string5 | null }

no calling-number outbound { range string1 string2 | sequence string1 . . . string5 | null }

### Syntax Description

range

Generates the sequence of ANI by rotating through the specified range ( string1 to string2 ).

sequence

Configures a sequence of discrete strings ( string1 ... string5 ) to be passed out as ANI for successive calls using the peer

The ellipses ( ... ) is entered as shown above.

null

Suppresses ANI. If used, no ANI is passed when this dial peer is selected.

string# ...

Valid E.164 telephone number strings. Strings must be of equal length and cannot be more than 32 digits long.

### Command Default

No outbound calling number is specified.

### Command Modes

Dial peer configuration (config-dial-peer) Voice-port configuration (config-voiceport)

## Command History

Release

Modification

12.1(3)T

This command was introduced on the Cisco AS5300.

### Usage Guidelines

This command is effective only for FGD-EANA signaling.

## Examples

Use the calling-number outbound command to enable or disable the passing of ANI on a T1-CAS FGD-EANA configured T1 interface for outgoing calls. Syntax for
                              this command is the same for both voice-port mode and dial peer mode. Examples are given for both modes.

## Examples

```
calling-number outbound range 
string1
 
string2
```

The values string1 and string2 are valid E.164 telephone number strings. Both strings must be of the same length and cannot be more than 32 digits long.
                              Only the last four digits are used for specifying the range ( string1 to string2 ) and for generating the sequence of ANI by rotating through the range until string2 is reached and then starting from string1 again. If strings are fewer than four digits in length, then entire strings are used.

ANI is generated by using the 408555 prefix and by rotating through 0100 to 0101 for each call using this peer.

Dial peer configuration mode:

```
dial-peer voice 1 pots
 calling-number outbound range 4085550100 4085550101
 calling Number Outbound is effective only for fgd_eana signaling
```

Voice-port configuration mode:

```
voice-port 1:D
 calling-number outbound range 4085550100 4085550105
 Calling Number Outbound is effective only for fgd_eana signaling
```

## Examples

```
calling-number outbound sequence 
string1 string2 string3
string4 string5
```

This option configures a sequence of discrete strings ( string1 ... string5 ) to be passed out as ANI for successive calls using the peer. The limit is five strings. All strings must be valid E.164
                              numbers, up to 32 digits in length.

Dial peer configuration mode:

```
dial-peer voice 1 pots
 calling-number outbound sequence 6000 6006 4000 5000 5025
 Calling Number Outbound is effective only for fgd_eana signaling
```

Voice-port configuration mode:

```
voice-port 1:D
 calling-number outbound sequence 6000 6006 4000 5000 5025
 Calling Number Outbound is effective only for fgd_eana signaling
```

## Examples

```
calling-number outbound null
```

This option suppresses ANI. If used, no ANI is passed when this dial peer is selected.

Dial peer configuration mode:

```
dial-peer voice 1 pots
 calling-number outbound null
 Calling Number Outbound is effective only for fgd_eana signaling
```

Voice-port configuration mode:

```
voice-port 1:D
 calling-number outbound null
 Calling Number Outbound is effective only for fgd_eana signaling
```

### Related Commands

Command

Description

info-digits string1

Configures two information digits to be prepended to the ANI string.

## capacity update interval (dial peer)

To change the capacity update for prefixes associated with this dial peer, use the capacity update interval command in dial peer configuration mode. To return to the default, use the no form of this command.

capacity update interval seconds

no capacity update interval seconds

### Syntax Description

seconds

Interval, in seconds, between the sending of periodic capacity updates. This can be a number in the range 10 to 1000. The
                                          default value is 25 seconds.

### Command Default

25 seconds

### Command Modes

Dial peer configuration (config-dial-peer)

## Command History

Release

Modification

12.3(1)

This command was introduced.

### Usage Guidelines

The update interval should be set depending how many updates that are sent. Updates are sent more often when more calls are
                              coming in, which can lead to data getting out of synchrony. If the interval is too short for the number of updates, the location
                              server can be overwhelmed.

If a dial peer gets too much traffic, set the seconds argument to a higher value.

## Examples

The following example shows that POTS dial peer 10 is having the capacity update occur every 35 seconds:

```
Router(config)# dial-peer voice 10 pots Router(config-dial-peer)# capacity update interval 35
```

### Related Commands

Command

Description

dial-peer voice

Enters dial-peer configuration mode and specifies the method of voice-related encapsulation.

## capacity update interval (trunk group)

To change the capacity update for carriers or trunk groups, use the capacity update interval command in trunk group configuration mode. To return to the default, use the no form of this command.

capacity { carrier | trunk-group } update interval seconds

no capacity { carrier | trunk-group }

### Syntax Description

carrier

Carrier capacity.

trunk-group

Trunk group capacity.

seconds

Interval, in seconds, between the sending of periodic capacity updates. This can be a number in the range 10 to 1000. The
                                          default value is 25 seconds.

### Command Default

25 seconds

### Command Modes

Trunk group configuration (config-trunkgroup)

## Command History

Release

Modification

12.3(1)

This command was introduced.

### Usage Guidelines

The update interval should be set depending how many updates that are sent. Updates are sent more often when more calls are
                              coming in, which can lead to data getting out of synchrony. If the interval is too short for the number of updates, the location
                              server can be overwhelmed.

If a dial peer gets too much traffic, set the seconds argument to a higher value.

## Examples

The following example sets the capacity update for trunk group 101 to occur every 45 seconds:

```
Router(config)# trunk group 101 Router(config-trunkgroup)# capacity trunk-group update interval 45
```

### Related Commands

Command

Description

trunk group

Defines the trunk group and enters trunk group configuration mode.

## cap-list vfc

To add a voice codec overlay file to the capability file list, use the cap-list vfc command in global configuration mode. To disable a particular codec overlay file that has been added to the capability list,
                              use the no form of this command.

cap-list filename vfc slot-number

no cap-list filename vfc slot-number

### Syntax Description

filename

Identifies the codec file stored in voice feature card (VFC) flash memory.

slot - number

Identifies the slot where the VFC is installed. Range is 0 to 2. There is no default value.

### Command Default

No default behavior or values

### Command Modes

Global configuration (config)

## Command History

Release

Modification

11.3NA

This command was introduced on the Cisco AS5300.

### Usage Guidelines

When VCWare is unbundled, it automatically adds DSPWare to flash memory, creates both the capability and default file lists,
                              and populates these lists with the default files for the particular version of VCWare. The capability list defines the available
                              voice codecs for H.323 capability negotiation. Use the cap-list vfc command to add the indicated voice codec overlay file (defined by filename ) to the capability file list in flash memory.

## Examples

The following example adds the following codec to the list included in flash memory:

```
config terminal
 cap-list cdc-g711-1.0.14.0.bin vfc 0
```

### Related Commands

Command

Description

default-file vfc

Specifies an additional (or different) file from the ones in the default file list and stored in VFC Flash memory.

## capf-address

To specify the Certificate Authority Proxy Function (CAPF) for a  locally significant certificate (LSC) update, use the capf-address command in phone proxy configuration mode. To remove the CAPF for an LSC update, use the no form of the command.

capf-address ipv4 capf-ipv4-address acc-addr ipv4 access-ipv4-address

no capf-address ipv4 capf-ipv4-address acc-addr ipv4 access-ipv4-address

## Syntax Description

Specifies the IPv4
                                       address as the local address for the CAPF service.

Specifies the access side address used as a CAPF server address.

### Command Default

No CAPF address is specified.

### Command Modes

Phone proxy configuration mode (config-phone-proxy)

## Command History

15.3(3)M

This command was introduced.

### Usage Guidelines

## Examples

The following example shows how to specify a CAPF address for an LSC update. The IPv4
                              address for the for the CAPF service is 198.51.100.101 and the access side address is 192.168.0.109:

```
Device(config)# voice-phone-proxy first-pp
Device(config-phone-proxy)# capf-addr ipv4 198.51.100.101 acc-addr ipv4 192.168.0.109
```

## card type (T1-E1)

To configure a T1
                              		  or E1 card type, use the card type command in
                              		  global configuration mode. To deselect the card type on non-SPA platforms, use
                              		  the no form of this
                              		  command. The no form of this command is not available on the SPA platforms.

card type { t1 | e1 } slot [bay]

no card type { t1 | e1 } slot [bay]

### Channelized T1/E1 Shared Port Adapters

card type { t1 | e1 } slot subslot

### Syntax Description

t1

Specifies
                                          						T1 connectivity of 1.544 Mbps through the telephone switching network, using
                                          						AMI or B8ZS coding.

e1

Specifies
                                          						a wide-area digital transmission scheme used predominantly in Europe that
                                          						carries data at a rate of 2.048 Mbps.

slot

Chassis
                                          						slot number.

Refer to
                                          						the appropriate hardware manual for slot information. For SIPs, refer to the
                                          						platform-specific SPA hardware installation guide or the corresponding
                                          						"Identifying Slots and Subslots for SIPs and SPAs" topic in the
                                          						platform-specific SPA software configuration guide.

bay

(Optional) Card interface bay number in a slot (route switch processor [RSP]
                                          						platform only). This option is not available on other platforms.

subslot

(Channelized T/E1 Shared Port Adapters Only) Secondary slot number on a SPA
                                          						interface processor (SIP) where a SPA is installed.

Refer to
                                          						the platform-specific SPA hardware installation guide and the corresponding
                                          						"Specifying the Interface Address on a SPA" topic in the platform-specific SPA
                                          						software configuration guide for subslot information.

### Command Default

No default behavior
                              		  or values

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.0(5)XE

This
                                          						command was introduced.

12.0(7)T

This
                                          						command was integrated into Cisco IOS Release 12.0(7)T.

12.3(1)

This
                                          						command was integrated into Cisco IOS Release 12.3(1) and support was added for
                                          						Cisco 2610XM, Cisco 2611XM, Cisco 2620XM, Cisco 2621XM, Cisco 2650XM, Cisco
                                          						2651XM, Cisco 2691, Cisco 3631, Cisco 3660, Cisco 3725, and Cisco 3745
                                          						platforms.

12.2S

This
                                          						command was integrated into Cisco IOS Release 12.2S.

12.2(18)SXE

This
                                          						command was integrated into Cisco IOS Release 12.2(18)SXE to support SPAs on
                                          						the Cisco 7600 series routers and Catalyst 6500 series switches.

12.0(31)S

This
                                          						command was integrated into Cisco IOS Release 12.0(31)S to support SPAs on
                                          						Cisco 12000 series routers.

12.2(33)SRA

This command was integrated into Cisco IOS Release
                                          						12.2(33)SRA.

XE 3.18SP

This command was integrated into Cisco NCS 4200 Series.

### Usage Guidelines

Changes made
                              		  using this command on non-SPA platforms, do not take effect unless the reload command is used or the router is rebooted.

Channelized
                                 			 T1/E1 Shared Port Adapters

There is no card
                              		  type when the SPA is inserted for first time. The user must configure this
                              		  command before they can configure individual ports.

The no form of
                              		  this command is not available on the SPA platforms. To change an existing card
                              		  type on SPA platforms, perform the following steps:

Remove the
                                    				SPA from its subslot.

Save the
                                    				configuration.

Reboot the
                                    				router.

Insert the
                                    				new SPA into the subslot.

Configure the
                                    				new card using this command.

## Examples

The following
                              		  example configures T1 data transmission on slot 1 of the router:

```
Router(config)# card type t1 1
```

The following
                              		  example configures all ports of an 8-Port Channelized T1/E1 SPA, seated in slot
                              		  5, subslot 2, in T1 mode:

```
Router(config)# card type t1 5 2
```

### Related Commands

Command

Description

controller

Configures a T1 or E1 controller and enters controller configuration mode.

reload

Reloads
                                          						the operating system.

show controller

Displays the controller state that is specific to controller hardware

show interface serial

Displays the serial interface type and other information.

## card type (T3-E3)

To configure a T3 or E3 card type, use the card type command in global configuration mode. To deselect the card type, use the no form of this comand. The no form of this command is not supported on the 2-Port and 4-Port Clear Channel T3/E3 SPA on Cisco
                              12000 series routers.

### T3 or E3 Controllers

card type { t3 | e3 } slot

no card type { t3 | e3 } slot

### Clear Channel T3/E3 Shared Port Adapters

card type { t3 | e3 } slot subslot

no card type { t3 | e3 } slot subslot

### Clear Channel T3/E3 Shared Port Adapters on Cisco 12000 Series Routers

card type { t3 | e3 } slot subslot

### Syntax Description

t3

Specifies T3 connectivity of 44210 kbps through the network, using B8ZS coding.

e3

Specifies a wide-area digital transmission scheme used predominantly in Europe that carries data at a rate of 34010 kbps.

slot

Slot number of the interface.

subslot

(Clear Channel T3/E3 Shared Port Adapters Only) Secondary slot number on a SIP where a SPA is installed.

Refer to the platform-specific SPA hardware installation guide and the corresponding "Specifying the Interface Address on
                                          a SPA" topic in the platform-specific SPA software configuration guide for subslot information.

### Command Default

No default behavior or values.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.1(1)T

This command was introduced.

12.2(11)YT

This command was integrated into Cisco IOS Release 12.2(11)YT and implemented on the following platforms: Cisco 2650XM, Cisco
                                          2651XM, Cisco 2691, Cisco 3660 series, Cisco 3725, and Cisco 3745 routers.

12.2(15)T

This command was integrated into Cisco IOS Release 12.2(15)T.

12.3(1)

This command was integrated into Cisco IOS Release 12.3(1) and support was added for Cisco 2610XM, Cisco 2611XM, Cisco 2620XM,
                                          Cisco 2621XM, Cisco 2650XM, Cisco 2651XM, Cisco 2691, Cisco 3631, Cisco 3660, Cisco 3725, and Cisco 3745 platforms.

12.2S

This command was integrated into Cisco IOS Release 12.2S.

12.2(25)S3

This command was integrated into Cisco IOS Release 12.2(25)S3 to support SPAs on the Cisco 7304 routers.

12.2(18)SXE

This command was integrated into Cisco IOS Release 12.2(18)SXE to support SPAs on the Cisco 7600 series routers and Catalyst
                                          6500 series switches.

12.0(31)S

This command was integrated into Cisco IOS Release 12.0(31)S to support SPAs on the Cisco 12000 series routers.

12.2(33)SRA

This command was integrated into Cisco IOS Release 12.2(33)SRA.

### Usage Guidelines

Usage guidelines vary slightly from platform to platform as follows:

T3 or E3 Controllers

Once a card type is issued, you enter the no card type command and then another card type command to configure a new card type. You must save the configuration to the NVRAM and reboot the router in order for the
                              new configuration to take effect.

When the router comes up, the software comes up with the new card type. Note that the software will reject the configuration
                              associated with the old controller and old interface. You must configure the new controller and serial interface and save
                              it.

Clear Channel T3/E3 Shared Port Adapters

To change all the SPA ports from T3 to E3, or vice versa, you enter the no card type command and then another card type command to configure a new card type.

When the router comes up, the software comes up with the new card type. Note that the software will reject the configuration
                              associated with the old controller and old interface. You must configure the new controller and serial interface and save
                              it.

Clear Channel T3/E3 Shared Port Adapters on Cisco 12000 Series Routers

The no form of this command is not available on the 2-Port and 4-Port Clear Channel T3/E3 SPA on Cisco 12000 series routers.
                              To change an existing card type on Cisco 12000 series routers, perform the following steps:

Remove the SPA from its subslot.

Save the configuration.

Reboot the router.

Insert the new SPA into the subslot.

Configure the new card using this command.

## Examples

The following example shows T3 data transmission configured in slot 1:

```
Router(config)# card type t3 1
```

The following example configures all ports of 2-Port and 4-Port Clear Channel T3/E3 SPA, seated in slot 5, subslot 2, in
                              T3 mode:

```
Router(config)# card type t3 5 2
```

### Related Commands

Command

Description

controller

Configures a T3 or E3 controller and enters controller configuration mode.

reload

Reloads the operating system.

show interface serial

Displays the serial interface type and other information.

## carrier-id (dial peer)

To specify the carrier associated with a VoIP call in a dial peer, use the carrier - id command in dial peer configuration mode. To delete the source carrier ID, use the no form of this command.

carrier-id { source | target } name

no carrier-id { source | target } name

### Syntax Description

source

Indicates the carrier that the dial peer uses as a matching key for inbound dial-peer matching.

target

Indicates the carrier that the dial peer uses as a matching key for outbound dial-peer matching.

name

Specifies the ID of the carrier to use for the call. Valid carrier IDs contain a maximum of 127 alphanumeric characters.

### Command Default

No default behavior or values

### Command Modes

Dial peer configuration (config-dial-peer)

## Command History

Release

Modification

12.2(11)T

This command was introduced.

### Usage Guidelines

A Gatekeeper Transaction Message Protocol (GKTMP) route server-based application at the terminating gateway uses the source
                              carrier ID to select a target carrier that routes the call over a plain old telephone service (POTS) line.

The terminating gateway uses the target carrier ID to select a dial peer for routing the call over a POTS line.

For IP-to-IP calls, the carrier-id command alone is not an oubound dialpeer match criterion.

## Examples

The following example indicates that dial peer 112 should use carrier ID "east17" for outbound dial-peer matching in the terminating
                              gateway:

```
Router(config)# dial-peer voice 112 pots Router(config-dial-peer)# carrier-id target east17
```

The following example indicates that dial peer 111 should use carrier ID "beta23" for inbound dial-peer matching in the terminating
                              gateway:

```
Router(config)# dial-peer voice 111 voip Router(config-dial-peer)# carrier-id source beta23
```

### Related Commands

Command

Description

translation-profile (dial peer)

Associates a translation profile with a dial peer.

trunkgroup (dial peer)

Assigns a trunk group to a source IP group or dial peer for trunk group label routing.

## carrier-id (global)

To set the carrier ID for trunk groups when a local carrier ID is not configured, use the carrier-id command in global configuration mode. To disable the carrier ID, use the no form of this command.

carrier-id name [ cic ]

no carrier-id name [ cic ]

### Syntax Description

name

Identifier for the carrier ID. Must be four-digit numeric carrier identification code to be advertised as a TRIP carrier family
                                          but can be alphanumeric if used otherwise.

cic

(Optional) Specifies that the carrier ID is a circuit identification code (CIC).

### Command Default

No default behavior or values

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.3(1)

This command was introduced.

### Usage Guidelines

To advertise the carrier as a TRIP carrier family, the cic keyword must be used. When the cic keyword is used, only numeric values can be accepted for the name value. If the cic keyword is not used, the name value can be alphanumeric but is not advertised to TRIP location servers.

## Examples

The following example shows a carrier ID using the circuit identification code:

```
Router(config)# carrier-id 1234 cic
```

### Related Commands

Command

Description

carrier-id (trunk group)

Configures the carrier ID locally on the trunk group.

## carrier-id (trunk group)

To specify the carrier associated with a trunk group, use the carrier - id command in trunk group configuration mode. To delete the source carrier ID, use the no form of this command.

carrier-id name [ cic ]

no carrier-id name [ cic ]

### Syntax Description

name

The ID of the carrier to use for the call. Valid carrier IDs contain a maximum of 127 alphanumeric characters.

To be advertised as a TRIP carrier family, this must be set to a four-digit numeric carrier identification code.

cic

(Optional) Specifies that the carrier ID is a circuit identification code.

### Command Default

No default behavior or values

### Command Modes

Trunk group configuration (config-trunkgroup)

## Command History

Release

Modification

12.2(11)T

This command was introduced.

12.3(1)

The cic keyword was added.

### Usage Guidelines

In a network, calls are routed over incoming trunk groups and outgoing trunk groups. The name arguments identifies the carrier that handles the calls for a specific trunk group. In some cases, the same trunk group may
                              be used to carry both incoming calls and outgoing calls.

The carrier ID configured locally on the trunk group supersedes the globally configured carrier ID.

To advertise the carrier as a TRIP carrier family, the cic keyword must be used. When cic is used, only numeric values can be accepted for the name value. If cic is not used, the name value can be alphanumeric but is not advertised to TRIP location servers.

## Examples

The following example indicates that carrier "alpha1" carries calls for trunk group 5:

```
Router(config)# trunk group 5 Router(config-trunk-group)# carrier-id alpha1
```

The following example shows that the carrier with circuit identification code 1234 carries calls for trunk group 101. This
                              trunk group can carry TRIP advertisements.

```
Router(config)# trunk group 101 Router(config-trunk-group)# carrier-id 1234 cic
```

### Related Commands

Command

Description

carrier-id (global)

Configures the carrier ID globally for all trunk groups.

translation-profile (trunk group)

Associates a translation profile with a trunk group.

trunk group

Initiates the definition of a trunk group.

## carrier-id (voice source group)

To specify the carrier associated with a VoIP call, use the carrier - id command in voice source group configuration mode. To delete the source carrier ID, use the no form of this command.

carrier-id { source | target } name

no carrier-id { source | target } name

### Syntax Description

source

Indicates the carrier ID associated with an incoming VoIP call at the terminating gateway.

target

Indicates the carrier ID used by the terminating gateway to match an outbound dial peer.

name

The ID of the carrier to use for the call. Valid carrier IDs contain a maximum of 127 alphanumeric characters.

### Command Default

No default behavior or values

### Command Modes

Voice source group configuration (cfg-source-grp)

## Command History

Release

Modification

12.2(11)T

This command was introduced.

### Usage Guidelines

A Gatekeeper Transaction Message Protocol (GKTMP) server application at the terminating gateway uses the source carrier ID
                              to select a target carrier that routes the call over a plain old telephone service (POTS) line. The terminating gateway uses
                              the target carrier ID to select a dial peer for routing the call over a POTS line.

If an incoming H.323 VoIP call matches a source IP group that has a target carrier ID, the source IP group’s target carrier
                                          ID overrides the VoIP call’s H.323 setup message.

## Examples

The following example indicates that voice source IP group "group1" should use carrier ID named "source3" for incoming VoIP
                              calls and carrier ID named "target17" for outbound dial-peer matching in the terminating gateway:

```
Router(config)# voice source-group group1 Router(cfg-source-grp)# carrier-id source source3 Router(cfg-source-grp)# carrier-id target target17
```

### Related Commands

Command

Description

voice source-group

Initiates the definition of a source IP group.

## cause-code

To represent internal failures with former and nonstandard H.323 or Session Initiation Protocol (SIP) cause codes, use the cause - code command in voice service VoIP configuration mode. To use standard cause-code categories, use the no form of this command.

cause-code legacy

no cause-code legacy

### Syntax Description

legacy

Sets the internal cause code to the former and nonstandard set of H.323 and SIP values.

### Command Default

The default for SIP and H.323 is to use standard cause-code categories, so the command is disabled.

### Command Modes

Voice service VoIP configuration (config-voi-srv)

## Command History

Release

Modification

12.2(11)T

This command was introduced.

### Usage Guidelines

This command is used for backward compatibility purposes.

## Examples

The following example sets the internal cause codes to the former and nonstandard set of SIP and H.323 values for backward
                              compatibility:

```
Router(config)# voice service voip Router(config-voi-srv)# cause-code legacy
```

### Related Commands

Command

Description

show call history voice

Displays the call history table for voice calls.

## cbarge

To enable idle phones to join an active call on a shared line on a Foreign Exchange Station (FXS) port by going offhook, use
                              the cbarge command in supplementary-service voice-port configuration mode. To return to the command default, use the no form of this command.

cbarge

no cbarge

### Syntax Description

This command has no arguments or keywords.

### Command Default

cBarge is disabled and idle phones are unable to join an active call on a shared line.

### Command Modes

Supplementary-service voice-port configuration mode (config-stcapp-suppl-serv-port)

## Command History

Release

Modification

15.1(3)T

This command was introduced.

### Usage Guidelines

Use the cbarge command to allow one idle IP or analog phone that is connected to the same FXS port to automatically join an active call
                              on the shared line by going offhook.

The hold-resume command must be configured on each port before the cbarge command is configured.

Only one analog phone is allowed to join an active call.

## Examples

The following example shows how to enable idle phones to join active calls on ports 2/2, 2/3, and 2/4 on a Cisco VG224:

```
Router(config)# stcapp supplementary-services Router(config-stcapp-suppl-serv)# port 2/2 Router(config-stcapp-suppl-serv-port)# hold-resume Router(config-stcapp-suppl-serv-port)# cbarge Router(config-stcapp-suppl-serv)# port 2/3 Router(config-stcapp-suppl-serv-port)# hold-resume Router(config-stcapp-suppl-serv-port)# cbarge Router(config-stcapp-suppl-serv)# port 2/4 Router(config-stcapp-suppl-serv-port)# hold-resume Router(config-stcapp-suppl-serv-port)# cbarge Router(config-stcapp-suppl-serv-port)# end
```

### Related Commands

Command

Description

hold-resume

Turns the STCAPP supplementary-service features on and off using hookflash.

stcapp supplementary-services

Enters supplementary-service configuration mode for configuring STCAPP supplementary-service features on an FXS port.

## ccm-manager application redundant-link port

To configure the port number for the redundant link application, use the ccm - manager application redundant - link port command in global configuration mode. To disable the configuration, use the no form of this command.

ccm-manager application redundant-link port number

no ccm-manager application redundant-link port

### Syntax Description

port number

Port number for the transport protocol. The protocol may be User Data Protocol (UDP), Reliable User Datagram Protocol (RDUP),
                                          or TCP. Range is from 0 to 65535, and the specified value must not be a well-known reserved port number such as 1023. The
                                          default is 2428.

### Command Default

Port number: 2428

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.1(3)T

This command was introduced with Cisco CallManager Version 3.0 and the Cisco Voice Gateway 200 (VG200).

12.2(2)XA

The command was implemented on the Cisco 2600 series and Cisco 3600 series.

12.2(4)T

The command was integrated into Cisco IOS Release 12.2(4)T.

### Usage Guidelines

Use this command only when defining an application-specific port other than the default.

## Examples

In the following example, the port number of the redundant link application is 2429:

```
ccm-manager application redundant-link port 2429
```

### Related Commands

Command

Description

ccm-manager redundant-host

Configures the IP address or the DNS name of up to two backup Cisco CallManagers.

ccm-manager switchback

Configures the switchback mode that determines when the primary Cisco CallManager is used if it becomes available again while
                                          a backup Cisco CallManager is being used.

## ccm-manager config

To specify the TFTP server from which the Media Gateway Control Protocol (MGCP) gateway downloads Cisco Unified Communications
                              Manager (Cisco UCM) Extensible Markup Language (XML) configuration files and to enable the download of the configuration,
                              use the ccm-manager config command in global configuration mode. To disable the dial-peer and server configurations, use the no form of this command.

ccm-manager config [ dialpeer-prefix prefix | server { ip-address | name }]

no ccm-manager config [ dialpeer-prefix prefix | server ]

### Syntax Description

dialpeer - prefix prefix

(Optional) Specifies the prefix to use for autogenerated dial peers. Range is 1 to 2147483647. The default is 999.

When manually adding a dial peers prefix, select a prefix number other than the default.

server { ip-address | name }

(Optional) Specifies the IP address or logical name of the TFTP server from which the XML configuration files are downloaded.

The arguments are as follows:

ip-address-- IP address of the TFTP server from which to download the XML configuration files to the local MGCP voice gateway.

name-- Logical (symbolic) name of the TFTP server from which to download XML configuration files to the local MGCP voice gateway.

### Command Default

The configuration download feature is disabled.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.2(2)XN

This command was introduced and implemented on the Cisco 2600 series, Cisco 3600 series, and the Cisco VG200.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T and implemented on the Cisco IAD2420 series.

### Usage Guidelines

The ccm-manager config command is required to enable the download of Cisco UCM XML configuration files. If you separate the MGCP and H.323 dial
                              peers under different dial-peer tags, ensure that the MGCP dial peers are configured before the H.323 dial peers. Direct-inward-dial
                              (DID) is required for E1 PRI dial peers.

To keep manually added dial peers from being deleted from the running configuration when Cisco UCM downloads the configuration
                                          to the gateway, use a dial peer-prefix value other than the default (999).

Do not delete the POTS dial peer created by the automatic download process. However, if a dial peer has been deleted, you
                              can restore the deleted dial peer by entering the following commands to repeat the download of the configuration file:

```
no mgcp
no ccm-manager config
ccm-manager config
mgcp
```

After you enter these commands, use the show ccm-manager config-download command to display the the configuration file downloaded from the TFTP server via the interface specified. The following
                              is an example of the output:

```
Loading sample.cnf.xml from 9.13.22.100 (via GigabitEthernet0/0): !
[OK - 12759 bytes]
```

## Examples

The following example shows how to enable the automatic download of configuration files:

```
ccm-manager config
```

In the following example, the IP address of the TFTP server from which a configuration file is downloaded is identified:

```
ccm-manager config server 10.10.0.21
```

### Related Commands

Command

Description

debug ccm-manager config-download

Displays dialog during configuration download from the Cisco UCM to the gateway.

show ccm-manager config-download

Displays whether the Cisco UCM configuration is enabled.

## ccm-manager download-tones

To configure a Cisco IOS gateway to download a XML configuration file that contains custom tone information from a TFTP server
                              at the time of gateway registration, use the ccm-manager download-tones command in global configuration mode. To disable this functionality, use the no form of this command.

ccm-manager download-tones

no ccm-manager download-tones

### Syntax Description

This command has no arguments or keywords.

### Command Default

Cisco CallManager download tones are disabled.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.2(15)ZJ

This command was introduced.

12.3(4)T

This command was integrated into Cisco IOS Release 12.3(4)T.

## Examples

The following example shows a Cisco IOS gateway being configured to download an XML configuration file that contains custom
                              tone information from a TFTP server:

```
Router(config)# ccm-manager download-tones
```

### Related Commands

Command

Description

cptone

Specifies a regional voice-interface-related tone, ring, and cadence setting.

debug ccm-manager

Displays debugging of Cisco CallManager.

show ccm-manager

Displays a list of Cisco CallManager servers and their current status and availability.

## ccm-manager fallback-mgcp

To enable the gateway fallback feature and allow a Media Gateway Control Protocol (MGCP) voice gateway to provide call processing
                              services when Cisco CallManager is unavailable, use the ccm-manager fallback-mgcp command in global configuration mode. To disable fallback on the MGCP voice gateway, use the no form of this command.

ccm-manager fallback-mgcp

no ccm-manager fallback-mgcp

### Syntax Description

This command has no arguments or keywords.

### Command Default

The gateway fallback feature is enabled

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.2(2)XN

This command was introduced on the Cisco 2600 series, Cisco 3600 series, and the Cisco VG200.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T and Cisco CallManager Version 3.2 and implemented on Cisco IAD2420
                                          series.

12.2(15)ZJ

This command was integrated into Cisco IOS Release 12.2(15)ZJ.

12.3(2)T

This command was implemented on the Cisco 26xxXM, Cisco 2691, Cisco 3640, Cisco 3640A, Cisco 3660, and Cisco 37xx.

### Usage Guidelines

This command causes the gateway to fall back and provide call processing services if connectivity is lost between the gateway
                              and all Cisco CallManager servers. The mode and timing are set by default.

## Examples

The following example enables fallback:

```
Router(config)# ccm-manager fallback-mgcp
```

### Related Commands

Related Command

Purpose

ccm-manager config

Supplies the local MGCP voice gateway with the IP address or logical name of the TFTP server from which to download XML configuration
                                          files and enable the download of the configuration.

debug ccm-manager

Displays debugging information about the Cisco CallManager.

show ccm-manager fallback-mgcp

Displays the status of the MGCP gateway fallback feature.

## ccm-manager fax protocol

To enable fax-relay protocol for endpoints on a gateway, use the ccm-manager fax protocol command in global configuration mode. To disable fax-relay protocol, use the no form of this command.

ccm-manager fax protocol cisco

no ccm-manager fax protocol cisco

### Syntax Description

cisco

Cisco-proprietary fax-relay protocol. This is the only choice.

### Command Default

Cisco-proprietary fax-relay protocol is enabled by default.

### Command Default

Fax relay is enabled.

### Command Modes

Global configuration

## Command History

Release

Modification

12.2(9)T

This command was introduced.

### Usage Guidelines

Use the no form of this command to disable fax relay.

Because fax relay is enabled by default, the show running-config command does not explicitly show it to be enabled.

Fax over IP enables interoperability of traditional analog fax machines with IP telephony networks. In its original form,
                              fax data is digital. For transmission across a traditional public switched telephone network (PSTN), it is converted to analog
                              form. For transmission across the IP (packet) network, it is reconverted to digital form, and then, at the destination fax
                              machine, converted again to analog form.

Most Cisco voice gateways support two methods of transmitting fax traffic across the IP network:

Cisco fax relay--The gateway terminates the T.30 fax signaling. This is the preferred method.

Fax pass-through--The gateway does not distinguish a fax call from a voice call. All Cisco voice gateways support fax pass-through.

## Examples

The following example configures a Media Gateway Control Protocol (MGCP) gateway for Cisco fax relay:

```
Router(config)# ccm-manager fax protocol cisco Router(config)# mgcp fax t38 inhibit
```

The following example configures an MGCP gateway for fax pass-through:

```
Router(config)# ccm-manager fax protocol cisco Router(config)# mgcp modem passthrough voip mode nse Router(config)# mgcp modem passthrough voip codec g711ulaw
```

### Related Commands

Command

Description

debug ccm-manager

Displays debugging of Cisco CallManager.

show ccm-manager

Displays a list of Cisco CallManager servers and their current status and availability.

show running-config

Displays the contents of the currently running configuration file.

## ccm-manager mgcp

To enable the gateway to communicate with Cisco CallManager through the Media Gateway Control Protocol (MGCP) and to supply
                              redundant control agent services, use the ccm - manager mgcp command in global configuration mode. To disable communication with Cisco CallManager and redundant control agent services,
                              use the no form of this command.

ccm-manager mgcp [ codec-all ]

no ccm-manager mgcp [ codec-all ]

### Syntax Description

codec-all

(Optional) Enables all codec on the gateway for the Cisco CallManager.

### Command Default

Cisco CallManager does not communicate with the gateway through MGCP.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.1(3)T

This command was introduced with Cisco CallManager Version 3.0 on the Cisco VG200.

12.2(2)XA

The command was integrated into Cisco IOS Release 12.2(2)XA and implemented on the Cisco 2600 series and Cisco 3600 series.

12.2(2)XN

Support for enhanced MGCP voice gateway interoperability was added to Cisco CallManager Version 3.1 for the Cisco 2600 series,
                                          3600 series, and Cisco VG200.

12.2(4)T

The command was integrated into Cisco IOS Release 12.2(4)T.

12.2(11)T

This command was integrated into the Cisco IOS Release 12.2(11)T and Cisco CallManager Version 3.2 and was implemented on
                                          the Cisco IAD2420 series routers.

12.2(11)YU

This command was integrated into Cisco IOS Release 12.2(11)YU and implemented on the Cisco 1760 gateway.

15.0(1)M

This command was modified in a release earlier than Cisco IOS Release 15.0(1)M. The codec-all keyword was added.

### Usage Guidelines

This command enables the gateway to communicate with Cisco CallManager through MGCP. This command also enables control agent
                              redundancy when a backup Cisco CallManager server is available.

## Examples

In the following example, support for Cisco CallManager and redundancy is enabled within MGCP:

```
Router# configure terminal Router(config)# ccm-manager mgcp
```

### Related Commands

Command

Description

ccm-manager redundant-host

Configures the IP address or the DNS name of up to two backup Cisco CallManagers.

ccm-manager switchback

Configures the switchback mode that determines when the primary Cisco CallManager is used if it becomes available again while
                                          a backup Cisco CallManager is being used.

mgcp

Enables Media Gateway Control Protocol mode.

## ccm-manager music-on-hold

To enable the multicast music-on-hold (MOH) feature on a voice gateway, use the ccm-manager music-on-hold command in global configuration mode. To disable the MOH feature, use the no form of this command.

ccm-manager music-on-hold

no ccm-manager music-on-hold

### Syntax Description

This command has no arguments or keywords.

### Command Default

Disabled

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.2(2)XN

This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco VG200.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T and Cisco CallManager Version 3.2 and implemented on the Cisco
                                          IAD 2420 series routers.

## Examples

The following example shows multicast MOH configured for a MGCP voice gateway:

```
mgcp call-agent 10.0.0.21 2427 service-type mgcp version 0.1
mgcp dtmf-relay voip codec all mode out-of-band
mgcp rtp unreachable timeout 1000
mgcp modem passthrough voip mode cisco
mgcp package-capability rtp-package
mgcp package-capability sst-package
no mgcp timer receive-rtcp
call rsvp-sync
!
ccm-manager redundant-host 10.0.0.21 
ccm-manager mgcp
ccm-manager music-on-hold
ccm-manager config server 10.0.0.21 
!
```

### Related Commands

Command

Description

ccm-manager music-on-hold bind

Enables the multicast MOH feature on a voice gateways.

debug ccm-manager music-on-hold

Displays debugging information for MOH.

show ccm-manager music-on-hold

Displays MOH information.

## ccm-manager music-on-hold bind

To bind the multicast music-on-hold (MOH) feature to an interface type, use the ccm - manager music - on - hold bind command in global configuration mode. To unbind the MOH feature on the interface type, use the no form of this command.

ccm-manager music-on-hold bind type slot/port

no ccm-manager music-on-hold bind type slot/port

### Syntax Description

type

Interface type to which the MOH feature is bound. The options follow:

async -- Asynchronous interface

bvi -- Bridge-Group Virtual Interface

ctunnel -- CTunnel interface

dialer -- Dialer interface

ethernet -- IEEE 802.3

lex -- Lex interface

loopback -- Loopback interface

mfr -- Multilink Frame Relay bundle interface

multilink -- Multilink interface

null -- Null interface

serial -- Serial interface

tunnel -- Tunnel interface

vif -- PGM Multicast Host interface

virtual - FrameRelay --Virtual Frame Relay interface

virtual - Template -- Virtual template interface

virtual - TokenRing -- Virtual Token Ring

slot / port

Number of the slot being configured. See the appropriate hardware manual for slot and port information.

### Command Default

This command is disabled by default, so the MOH feature is not bound to an interface type.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.2(11)T

This command was introduced.

### Usage Guidelines

Use the ccm - manager music - on - hold bind command to bind the multicast music-on-hold (MOH) feature to an interface type. Dynamic configuration of multicast MOH
                              bind is not supported.

## Examples

The following example shows multicast MOH bound to serial interface 0/0:

```
ccm-manager music-on-hold bind serial 0/0
```

### Related Commands

Command

Description

ccm-manager music-on-hold

Enables the MOH feature.

debug ccm-manager music-on-hold

Displays debugging information for MOH.

show ccm-manager music-on-hold

Displays MOH information.

## ccm-manager redundant-host

To configure the IP address or the Domain Name System (DNS) name of one or two backup Cisco CallManager servers, use the ccm-manager redundant-host command in global configuration mode. To disable the use of backup Cisco CallManager servers as call agents, use the no form of this command.

ccm-manager redundant-host { ip-address | dns-name } [ ip-address | dns-name ]

no ccm-manager redundant-host { ip-address | dns-name } [ ip-address | dns-name ]

### Syntax Description

ip - address

IP address of the backup Cisco CallManager server.

dns - name

DNS name of the backup Cisco CallManager server.

### Command Default

If you do not configure a backup Cisco CallManager, the redundancy is disabled.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.1(3)T

This command was introduced with Cisco CallManager Version 3.0 on the Cisco Voice Gateway 200 (VG200).

12.2(2)XA

The command was implemented on the Cisco 2600 series and Cisco 3600 series. The dns-name argument was added.

12.2(4)T

The command was integrated into Cisco IOS Release 12.2(4)T.

12.2(2)XN

Support for enhanced MGCP voice gateway interoperability was added to Cisco CallManager Version 3.1 for the Cisco 2600 series,
                                          3600 series, and the Cisco VG200.

12.2(11)T

This command was integrated into the Cisco IOS Release 12.2(11)T and Cisco CallManager Version 3.2 and implemented on the
                                          Cisco IAD2420 series routers.

### Usage Guidelines

The list of IP addresses or DNS names is an ordered and prioritized list. The Cisco CallManager server that was defined with
                              the mgcp call-agent command has the highest priority--it is the primary Cisco CallManager server. The gateway selects a Cisco CallManager server
                              on the basis of the order of its appearance in this list.

## Examples

In the following example, the IP address 10.0.0.50 is configured as the backup Cisco CallManager :

```
ccm-manager redundant-host 10.0.0.50
```

### Related Commands

Command

Description

ccm-manager application

Configures the port number for the redundant link application.

ccm-manager switchback

Configures the switchback mode that determines when the primary Cisco CallManager is used if it becomes available again while
                                          a backup Cisco CallManager is being used.

ccm-manager switchover-to-backup

Redirects (manually and immediately) a Cisco 2600 series router or Cisco 3600 series router to the backup Cisco CallManager
                                          server.

mgcp call-agent

Defines the Cisco CallManager server as the highest priority.

## ccm-manager sccp

To enable Cisco CallManager autoconfiguration of the Cisco IOS gateway, use the ccm manager sccp command in global configuration mode. To disable autoconfiguration, use the no form of this command.

ccm-manager sccp

no ccm-manager sccp

### Syntax Description

This command has no arguments or keywords.

### Command Default

Autoconfiguration is disabled.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.3(14)T

This command was introduced.

### Usage Guidelines

Use this command to trigger TFTP download of the eXtensible Markup Language (XML) configuration file. Issuing this command
                              immediately triggers the download, and also enables the Skinny Client Control Protocol (SCCP) and SCCP Telephony Control Application
                              (STCAPP), applications that enable Cisco CallManager control of gateway-connected telephony endpoints.

## Examples

The following example enables autoconfiguration of gateway-connected endpoints:

```
Router(config)# ccm-manager sccp
```

### Related Commands

Command

Description

ccm-manager config

Specifies the TFTP server from which the Cisco IOS gateway downloads Cisco CallManager XML configuration files.

ccm-manager sccp local

Selects the local interface for SCCP application use for Cisco CallManager registration.

show ccm-manager config-download

Displays information about the status of the Cisco IOS gateway configuration download.

## ccm-manager sccp local

To select the local interface that the Skinny Client Control Protocol (SCCP) application uses to register with Cisco CallManager,
                              use the ccm-manager sccp local command in global configuration mode. To deselect the interface, use the no form of this command.

ccm-manager sccp local interface-type interface-number

no ccm-manager sccp local interface-type interface-number

### Syntax Description

interface-type

Interface type that the SCCP application uses for Cisco CallManager registration.

interface-number

Interface number that the SCCP application uses for Cisco CallManager registration.

### Command Default

No local interface is selected.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.3(14)T

This command was introduced.

### Usage Guidelines

You must specify this interface before enabling the Cisco CallManager autoconfiguration process. The MAC address of this interface
                              is used to identify gateway endpoints.

## Examples

The following example configures a FastEthernet interface for SCCP application use for Cisco CallManager registration:

```
Router(config)# ccm-manager sccp local fastethernet 0/0
```

### Related Commands

Command

Description

show ccm-manager

Displays a list of Cisco CallManager servers and their current status and availability.

## ccm-manager shut-backhaul-interfaces

To disable ISDN Layer 2 connectivity on a Cisco Call Manager Media Gateway Control Protocol (MGCP) PRI or BRI backhauled trunk
                              when communication is lost between the Cisco Call Manager and the MGCP gateway, use the ccm-manager shut-backhaul-interfaces command in global configuration mode. To restore the default behavior, where ISDN Layer 2 is maintained between the MGCP
                              gateway and the ISDN switch even when no connectivity exists between the MGCP gateway and any Cisco Call Manager, use the no form of this command.

ccm-manager shut-backhaul-interfaces

no ccm-manager shut-backhaul-interfaces

### Syntax Description

This command has no arguments or keywords.

### Command Default

The default behavior is for the ISDN Layer 2 connection to be maintained (to make the Cisco Call Manager MGCP PRI or BRI backhaul
                              continue to function) between the MGCP gateway and the ISDN switch even if no connectivity exists between the MGCP gateway
                              and any Cisco Call Manager.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.4(8)

This command was introduced.

12.4(9)T

This command was integrated into Cisco IOS Release 12.4(9)T.

12.4(3f)

This command was integrated into Cisco IOS Release 12.4(3f).

12.4(5c)

This command was integrated into Cisco IOS Release 12.4(5c).

12.4(7c)

This command was integrated into Cisco IOS Release 12.4(7c).

12.4(4)T5

This command was integrated into Cisco IOS Release 12.4(4)T5.

12.4(6)T4

This command was integrated into Cisco IOS Release 12.4(6)T4.

### Usage Guidelines

Use this command on Cisco IOS voice routers configured for Cisco Call Manager MGCP PRI or BRI backhaul.

Prior to the introduction of the ccm-manager shut-backhaul-interfaces command, a Cisco Call Manager MGCP PRI or BRI backhaul trunk would maintain ISDN Layer 2 connectivity between the MGCP gateway
                              and the ISDN switch in a MULTIPLE_FRAMES_ESTABLISHED state even if Layer 3 Q.931 backhaul connectivity between the Cisco Call
                              Manager and the MGCP gateway was unavailable. This causes problems because the ISDN switch interprets the PRI or BRI trunk
                              as being active and continues to place calls to the MGCP gateway, even though all of the calls fail. After you enter the ccm-manager shut-backhaul-interfaces command, Layer 2 is disabled when connectivity between the Cisco Call Manager and the MGCP gateway is unavailable.

## Examples

The following example disables ISDN Layer 2 connectivity on a Cisco Call Manager MGCP PRI or BRI backhauled trunk when communication
                              is lost between Cisco Call Manager and the MGCP gateway:

```
ccm-manager shut-backhaul-interfaces
```

The following example restores the default behavior (functionality of the ccm-manager shut-backhaul-interfaces command is disabled) so that the ISDN Layer 2 connection is maintained between the MGCP gateway and the ISDN switch, even
                              when no connectivity exists between the MGCP gateway and any Cisco Call Manager:

```
no ccm-manager mgcp
no ccm-manager shut-backhaul-interfaces
ccm-manager mgcp
```

### Related Commands

Command

Description

ccm-manager mgcp

Enables the gateway to communicate with the Cisco Call Manager through the MGCP and to supply redundant control agent services.

## ccm-manager shut-interfaces-tftp-fails

To configure the number of TFTP download failures allowed before the gateway shuts down ports, use the ccm-manager shut-interfaces-tftp-fails command in global configuration mode. To return to the default configuration, use the no form of this command.

ccm-manager shut-interfaces-tftp-fails retries

no ccm-manager shut-interfaces-tftp-fails

### Syntax Description

retries

Number or TFTP retries. Range is from 2 to 10. The default is 2.

### Command Default

Ports shut down after the second TFTP retry. However TFTP download attempts continue.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.4(15)T2

This command was introduced.

12.4(20)T

This command was integrated into Cisco IOS Release 12.4(20)T.

### Usage Guidelines

Use the ccm-manager shut-interfaces-tftp-fails command to configure the number of TFTP download failures allowed before the gateway put the port in a shutdown state.

## Examples

The following example shows a gateway being configured to put the port in a shutdown state after four TFTP download failures:

```
Router(config)# ccm-manager shut-interfaces-tftp-fails 4
```

### Related Commands

Command

Description

show ccm-manager

Displays a list of Cisco Unified Communications Manager servers and their current status and availability.

## ccm-manager switchback

To specify the time when control is to be returned to the primary Cisco CallManager server once it becomes available, use
                              the ccm - manager switchback command in global configuration mode. To reset to the default, use the no form of this command.

ccm-manager switchback { graceful | immediate | never | schedule-time hh : mm | uptime-delay minutes }

no ccm-manager switchback

### Syntax Description

graceful

Specifies that control is returned to the primary Cisco CallManager server after the last active call ends (when there is
                                          no voice call in active setup mode on the gateway). Default value.

immediate

Specifies an immediate switchback to the primary Cisco CallManager server when the TCP link to the primary Cisco CallManager
                                          server is established, regardless of current call conditions.

never

Specifies not to return control to the primary Cisco CallManager server, as long as the secondary is up and running. The gateway
                                          registers to primary if the secondary is down and when the primary is up and running.

schedule - time hh : mm

Specifies an hour and minute, based on a 24-hour clock, when control is returned to the primary Cisco CallManager server.
                                          If the specified time is earlier than the current time, the switchback occurs at the specified time on the following day.

uptime - delay minutes

Specifies the number of minutes the primary Cisco CallManager server must run after the TCP link to is reestablished and control
                                          is returned to that primary call agent. Valid values are from 1 to 1440 (1 minute to 24 hours).

### Command Default

Graceful switchback

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.1(3)T

This command was modified. This command was introduced with Cisco CallManager Version 3.0 on the Cisco VG200.

12.2(2)XA

The command was implemented on the Cisco 2600 series and Cisco 3600 series.

12.2(2)XN

Support for enhanced Media Gateway Control Protocol (MGCP) voice gateway interoperability was added to Cisco CallManager Version
                                          3.1 for the Cisco 2600 series, 3600 series, and the Cisco VG200.

12.2(4)T

The command was integrated into Cisco IOS Release 12.2(4)T.

12.2(11)T

This command was implemented on the Cisco IAD2420 series routers.

15.0(1)M

This command was modified in a release earlier than Cisco IOS Release 15.0(1)M. The never keyword was added.

### Usage Guidelines

This command allows you to configure switchback to the higher priority Cisco CallManager when it becomes available. Switchback
                              allows call control to revert to the original (primary) Cisco CallManager once service has been restored.

## Examples

In the following example, the primary Cisco CallManager is configured to be used as soon as it becomes available:

```
Router# configure terminal Router(config)# ccm-manager switchback immediate
```

### Related Commands

Command

Description

ccm-manager application

Configures the port number for the redundant link application.

ccm-manager redundant-host

Configures the IP address or the DNS name of up to two backup Cisco CallManagers.

ccm-manager switchover-to-backup

Redirects a Cisco 2600 series or Cisco 3600 series router to the backup Cisco CallManager.

## ccm-manager switchover-to-backup

To manually redirect a gateway to the backup Cisco CallManager server, use the ccm-manager switchover-to-backup command in privileged EXEC mode.

ccm-manager switchover-to-backup

### Syntax Description

This command has no arguments or keywords.

### Command Default

No default behavior or values

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.2(2)XN

This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco VG200.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T and Cisco CallManager Version 3.2 and implemented on the Cisco
                                          IAD2420 series.

### Usage Guidelines

Switchover to the backup Cisco CallManager server occurs immediately. This command does not switch the gateway to the backup
                              Cisco CallManager server if you have the ccm-manager switchback command option set to "
                              immediate"
                              and the primary Cisco CallManager server is still running.

## Examples

In the following example, the backup Cisco CallManager server is configured to be used as soon as it becomes available:

```
ccm-manager switchover-to-backup
```

### Related Commands

Command

Description

ccm-manager application redundant-link

Configures the port number for the redundant link application (that is, for the secondary Cisco CallManager server).

ccm-manager redundant-host

Configures the IP address or the DNS name of up to two backup Cisco CallManager servers.

ccm-manager switchback

Specifies the time at which control is returned to the primary Cisco CallManager server once the server is available.

| Release | Modification |
|---|---|
| 12.1.(2)XF | This command was introduced on the Cisco 800 series routers. |
| 12.1(5)T | This command was integrated into Cisco IOS Release 12.1(5)T. |

| Note | Specific hardware is required to provide full support for the caller ID features. To determine support for these features
                                          in your configuration, review the appropriate hardware documentation and data sheets. This information is available on Cisco.com. |
|---|---|

| Command | Description |
|---|---|
| block caller | Configures call blocking on caller ID. |
| debug pots csm csm | Activates events from which an application can determine and display the status and progress of calls to and from POTS ports. |
| isdn i-number | Configures several terminal devices to use one subscriber line. |
| pots call waiting | Enables local call waiting on a router. |
| registered caller ring | Configures the Nariwake service-registered caller ring cadence. |

| Release | Modification |
|---|---|
| 12.1(2)XH | This command was introduced on the Cisco MC3810, Cisco 2600 series, and Cisco 3600 series. |
| 12.1(3)T | This command was integrated into Cisco IOS Release 12.1(3)T. |

| Note | Specific hardware is required to provide full support for the caller ID features. To determine support for these features
                                          in your configuration, review the appropriate hardware documentation and data sheets. This information is available on Cisco.com. |
|---|---|

| Command | Description |
|---|---|
| caller-id alerting line-reversal | Sets the line-reversal method of caller-ID call alerting. |

| Release | Modification |
|---|---|
| 12.1(2)XH | This command was introduced. |
| 12.1(3)T | This command was integrated into Cisco IOS Release 12.1(3)T. |

| Note | Specific hardware is required to provide full support for the caller ID features. To determine support for these features
                                          in your configuration, review the appropriate hardware documentation and data sheets. This information is available on Cisco.com. |
|---|---|

| Command | Description |
|---|---|
| caller-id alerting dsp-pre-alloc | At the receiving end of a line-reversal alerting caller-ID call, preallocates DSPs for caller ID calls. |

| Release | Modification |
|---|---|
| 12.1(2)XH | This command was introduced on the Cisco MC3810, Cisco 2600 series, and Cisco 3600 series. |
| 12.1(3)T | This command was integrated into Cisco IOS Release 12.1(3)T. |

| Note | Specific hardware is required to provide full support for the caller ID features. To determine support for these features
                                          in your configuration, review the appropriate hardware documentation and data sheets. This information is available on Cisco.com. |
|---|---|

| Command | Description |
|---|---|
| caller-id alerting line-reversal | Enables caller ID operation and sets the line-reversal alerting type at an FXS port. |
| caller-id alerting ring | Enables caller ID operation and sets an alerting ring type at an FXO or FXS port. |

| 1 | Use this setting if your telephone service provider specifies it to provide caller ID alerting (display) after the first ring
                                          at the receiving station. This is the most common setting. |
|---|---|
| 2 | Use this setting if your telephone service provider specifies it to provide caller ID alerting (display) after the second
                                          ring. This setting is used in Australia, where the caller ID information is sent following two short rings (double-pulse ring). |

| Release | Modification |
|---|---|
| 12.1(2)XH | This command was introduced. |
| 12.1(3)T | This command was integrated into Cisco IOS Release 12.1(3)T. |

| Note | Specific hardware is required to provide full support for the caller ID features. To determine support for these features
                                          in your configuration, review the appropriate hardware documentation and data sheets. This information is available on line. |
|---|---|

| Command | Description |
|---|---|
| caller-id alerting line-reversal | Enables caller ID operation and sets the line-reversal alerting type at an FXS port. |
| caller-id alerting pre-ring | Enables caller ID operation and sets the pre-ring alerting method at an FXS port. |

| attenuation | (Optional) specifies the attenuation, in decibels (dB). Range is from 0 to 64. The default is 14. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(2)XH | This command was introduced. |
| 12.1(3)T | This command was integrated into Cisco IOS Release 12.1(3)T. |

| Note | Specific hardware is required to provide full support for the caller ID features. To determine support for these features
                                          in your configuration, review the appropriate hardware documentation and data sheets. This information is available on line. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(2)XH | This command was introduced. |
| 12.1(3)T | This command was integrated into Cisco IOS Release 12.1(3)T. |

| Note | Cisco-switched calls using Voice over Frame Relay (VoFR) and Voice over ATM (VoATM) carry calling party information in the
                                          Cisco proprietary setup message. For standards-based, point-to-point VoFR (FRF.11) trunks where transparent signaling is applied
                                          for FXS-to-FXO calls, only pass-through of in-band automatic number identification (ANI) is supported. ANI information is
                                          always unblocked for these communications. Interface technology using transparent channel-associated signaling (CAS) can support
                                          only ANI through Feature Group D (in-band MF signaling). The Caller ID feature cannot be used with fixed point-to-point trunk
                                          connects created using the connection trunk command. |
|---|---|

| Note | Specific hardware is required to provide full support for the caller ID features. To determine support for these features
                                          in your configuration, review the appropriate hardware documentation and data sheets. This information is available on Cisco.com. |
|---|---|

| Command | Description |
|---|---|
| caller-id enable | Enables caller ID operation. |

| type | (Optional) Indicates that the following keyword is a caller-ID type. 1 --Type I only. Type I transmits the signal when the receiving phone is on hook. 2 --Type II only. Type II transmits the signal when the receiving phone is off hook, for instance to display the caller ID of
                                                an incoming call when the receiving phone is busy (call-waiting caller ID). |
|---|---|

| Release | Modification |
|---|---|
| 12.1(2)XH | This command was introduced. |
| 12.1(3)T | This command was integrated into Cisco IOS Release 12.1(3)T. |
| 12.3(7)T | The type 1 and type 2 keywords were added. |

| Note | The no form of this command also clears all other caller-ID configuration settings for the voice port. |
|---|---|

| Note | Cisco-switched calls using Voice over Frame Relay (VoFR) and Voice over ATM (VoATM) carry calling-party information in the
                                          Cisco-proprietary setup message. For standards-based, point-to-point VoFR (FRF.11) trunks where transparent signaling is applied
                                          for FXS-to-FXO calls, only pass-through of in-band automatic number identification (ANI) is supported. ANI information is
                                          always unblocked for these communications. Interface technology using transparent channel-associated signaling (CAS) can support
                                          only ANI through Feature Group D (in-band multifrequency signaling). Caller ID cannot be used with fixed point-to-point trunk
                                          connections created using the connection trunk command. |
|---|---|

| Note | Specific hardware is required to provide full support for the caller-ID features. To determine support for these features
                                          in your configuration, review the appropriate hardware documentation and data sheets. This information is available on line. |
|---|---|

| Command | Description |
|---|---|
| caller-id alerting line-reversal | Enables caller ID operation and sets the line-reversal alerting type at an FXS port. |
| caller-id alerting pre-ring | Enables caller ID operation and sets the pre-ring alerting method at an FXS port. |
| caller-id alerting ring | Enables caller ID operation and sets an alerting ring type at an FXO or FXS port. |
| caller-id block | Disables the sending of caller ID information from an FXS port. |
| station name | Enables caller ID operation and sets the name sent from an FXS port. |
| station number | Enables caller ID operation and sets the number sent from an FXS port. |

| BT | Specifies Frequency-Shift Keying (FSK) with Dual Tone Alerting Signal (DTAS) used by British Telecom. |
|---|---|
| FSK | Specifies FSK before or during a call. |
| DTMF | Specifies dual tone multifrequency (DTMF) digits with the start and end digit codes. |
| start | Specifies the start digit code. |
| end | Specifies the end digit code. |
| # | Specifies the DTMF digit #. |
| * | Specifies the DTMF digit *. |
| A | Specifies the DTMF digit A. |
| B | Specifies the DTMF digit B. |
| C | Specifies the DTMF digit C. |
| D | Specifies the DTMF digit D. |

| Release | Modification |
|---|---|
| 15.2(1)T | This command was introduced. |

| Note | Specific hardware is required to provide full support for the caller-ID features. To determine support for these features
                                             in your configuration, review the appropriate hardware documentation and data sheets. This information is available on Cisco.com. |
|---|---|

| Command | Description |
|---|---|
| caller-id alerting | Defines the caller ID alerting method. |
| caller-id attenuation | Configures the attenuation for a caller ID FXO voice port. |
| caller-id block | Blocks caller ID information. |
| caller-id enable | Enables caller ID operation. |
| caller-id format | Specifies the caller ID format. |

| keypad-character | Character string that can be dialed on a telephone keypad (0-9, *, #). Default: 8. The string can be any of the following: A single character (0-9, *, #) Two digits (00-99) Two to four characters (0-9, *, #) and the leading or ending character must be an asterisk (*) or number sign (#) |
|---|---|

| Release | Modification |
|---|---|
| 15.0(1)XA | This command was introduced. |
| 15.1(1)T | This command was integrated into Cisco IOS Release 15.1(1)T. |

| Command | Description |
|---|---|
| prefix (stcapp-fac) | Defines the prefix for FACs. |
| show stcapp feature codes | Displays all FACs. |

| number | Caller ID for which the user wants to set the cadence. Twenty numbers along with their respective cadences may be set for
                                          each of the plain old telephone service (POTS) ports. |
|---|---|
| ring cadence | Ring cadence level. The three cadence levels (0, 1, and 2), which differ in duration and cadence, are as follows: 0 --The ring cadence is 1 second on and 2 seconds off (NTT-defined regular ring). 1 --The ring cadence is 0.25 seconds on, 0.2 seconds off, 0.25 seconds on, and 2.3 seconds off (NTT-defined nonregular ring). 2 --The ring cadence is 0.5 seconds on, 0.25 seconds off, 0.25 seconds on, and 2 seconds off (Cisco-defined nonregular ring). |

| Release | Modification |
|---|---|
| 12.2(8)T | This command was introduced on the Cisco 803, Cisco 804, and Cisco 813 routers. |

| Note | If you have already subscribed to Nariwake service, the priority goes to the Nariwake caller ID cadence. |
|---|---|

| Command | Description |
|---|---|
| call waiting | Enables call waiting. |
| volume | Configures the receiver volume level in the router. |

| unscreened discard | (Optional) Specifies that the calling name and number be discarded. |
|---|---|
| from name set name | (Optional) Specifies that the display-name of the From header is unconditionally set to the configured ASCII string in the
                                          forwarded INVITE message. |
| from number set number | (Optional) Specifies that the user part of the From header is unconditionally set to the configured ASCII string in the forwarded
                                          INVITE message. |
| remote-party-id name set name | (Optional) Specifies that the display-name of the Remote-Party-ID header is unconditionally set to the configured ASCII string
                                          in the forwarded INVITE message. |
| remote-party-id number set number | (Optional) Specifies that the user part of the Remote-Party-ID header is unconditionally set to the configured ASCII string
                                          in the forwarded INVITE message. |
| asserted-id name set name | (Optional) Specifies that the display-name in the Asserted-ID header is unconditionally set to the configured ASCII string
                                          in the forwarded INVITE message. |
| asserted-id number set number | (Optional) Specifies that the user part in the Asserted-ID header is unconditionally set to the configured ASCII string in
                                          the forwarded INVITE message. |

| Release | Modification |
|---|---|
| 12.2(13)T | This command was introduced. |
| 12.4(15)T | The asserted-id keyword was added. |

| Command | Description |
|---|---|
| asserted-id | Sets the privacy level and enables either P-Asserted-Identity (PAI) or P-Preferred-Identity (PPI) privacy headers in outgoing
                                          SIP requests or response messages. |
| calling-info sip-to-pstn | Specifies calling information treatment for SIP-to-PSTN calls. |
| debug ccsip events | Enables tracing of SIP SPI events. |
| debug ccsip messages | Enables tracing SIP messages exchanged between the SIP UA client and the access server. |
| debug isdn q931 | Displays call setup and teardown of ISDN connections. |
| debug voice ccapi error | Enables tracing error logs in the call control API. |
| debug voip ccapi in out | Enables tracing the execution path through the call control API. |

| unscreened discard | (Optional) Specifies that the calling name and number be discarded. |
|---|---|
| name set name | (Optional) Specifies that the calling name be unconditionally set to the configured ASCII string in the forwarded Setup mesage. |
| number set number | (Optional) Specifies that the calling number be unconditionally set to the configured ASCII string in the forwarded Setup
                                          message. |

| Release | Modification |
|---|---|
| 12.2(13)T | This command was introduced. |

| Command | Description |
|---|---|
| debug ccsip events | Enables tracing of SIP SPI events. |
| debug ccsip messages | Enables SIP SPI message tracing. |
| debug isdn q931 | Displays call setup and teardown of ISDN connections. |
| debug voip ccapi in out | Enables tracing the execution path through the call control API. |
| calling-info pstn-to-sip | Specifies calling information treatment for PSTN-to-SIP calls. |

| range | Generates the sequence of ANI by rotating through the specified range ( string1 to string2 ). |
|---|---|
| sequence | Configures a sequence of discrete strings ( string1 ... string5 ) to be passed out as ANI for successive calls using the peer Note The ellipses ( ... ) is entered as shown above. | Note | The ellipses ( ... ) is entered as shown above. |
| Note | The ellipses ( ... ) is entered as shown above. |
| null | Suppresses ANI. If used, no ANI is passed when this dial peer is selected. |
| string# ... | Valid E.164 telephone number strings. Strings must be of equal length and cannot be more than 32 digits long. |

| Note | The ellipses ( ... ) is entered as shown above. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(3)T | This command was introduced on the Cisco AS5300. |

| Command | Description |
|---|---|
| info-digits string1 | Configures two information digits to be prepended to the ANI string. |

| seconds | Interval, in seconds, between the sending of periodic capacity updates. This can be a number in the range 10 to 1000. The
                                          default value is 25 seconds. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(1) | This command was introduced. |

| Command | Description |
|---|---|
| dial-peer voice | Enters dial-peer configuration mode and specifies the method of voice-related encapsulation. |

| carrier | Carrier capacity. |
|---|---|
| trunk-group | Trunk group capacity. |
| seconds | Interval, in seconds, between the sending of periodic capacity updates. This can be a number in the range 10 to 1000. The
                                          default value is 25 seconds. |

| Release | Modification |
|---|---|
| 12.3(1) | This command was introduced. |

| Command | Description |
|---|---|
| trunk group | Defines the trunk group and enters trunk group configuration mode. |

| filename | Identifies the codec file stored in voice feature card (VFC) flash memory. |
|---|---|
| slot - number | Identifies the slot where the VFC is installed. Range is 0 to 2. There is no default value. |

| Release | Modification |
|---|---|
| 11.3NA | This command was introduced on the Cisco AS5300. |

| Command | Description |
|---|---|
| default-file vfc | Specifies an additional (or different) file from the ones in the default file list and stored in VFC Flash memory. |

| capf-ipv4-address | Specifies the IPv4
                                       address as the local address for the CAPF service. |
|---|---|
| acc-addr ipv4 access-ipv4-address | Specifies the access side address used as a CAPF server address. |

| Release | Modification |
|---|---|
| 15.3(3)M | This command was introduced. |

| t1 | Specifies
                                          						T1 connectivity of 1.544 Mbps through the telephone switching network, using
                                          						AMI or B8ZS coding. |
|---|---|
| e1 | Specifies
                                          						a wide-area digital transmission scheme used predominantly in Europe that
                                          						carries data at a rate of 2.048 Mbps. |
| slot | Chassis
                                          						slot number. Refer to
                                          						the appropriate hardware manual for slot information. For SIPs, refer to the
                                          						platform-specific SPA hardware installation guide or the corresponding
                                          						"Identifying Slots and Subslots for SIPs and SPAs" topic in the
                                          						platform-specific SPA software configuration guide. |
| bay | (Optional) Card interface bay number in a slot (route switch processor [RSP]
                                          						platform only). This option is not available on other platforms. |
| subslot | (Channelized T/E1 Shared Port Adapters Only) Secondary slot number on a SPA
                                          						interface processor (SIP) where a SPA is installed. Refer to
                                          						the platform-specific SPA hardware installation guide and the corresponding
                                          						"Specifying the Interface Address on a SPA" topic in the platform-specific SPA
                                          						software configuration guide for subslot information. |

| Release | Modification |
|---|---|
| 12.0(5)XE | This
                                          						command was introduced. |
| 12.0(7)T | This
                                          						command was integrated into Cisco IOS Release 12.0(7)T. |
| 12.3(1) | This
                                          						command was integrated into Cisco IOS Release 12.3(1) and support was added for
                                          						Cisco 2610XM, Cisco 2611XM, Cisco 2620XM, Cisco 2621XM, Cisco 2650XM, Cisco
                                          						2651XM, Cisco 2691, Cisco 3631, Cisco 3660, Cisco 3725, and Cisco 3745
                                          						platforms. |
| 12.2S | This
                                          						command was integrated into Cisco IOS Release 12.2S. |
| 12.2(18)SXE | This
                                          						command was integrated into Cisco IOS Release 12.2(18)SXE to support SPAs on
                                          						the Cisco 7600 series routers and Catalyst 6500 series switches. |
| 12.0(31)S | This
                                          						command was integrated into Cisco IOS Release 12.0(31)S to support SPAs on
                                          						Cisco 12000 series routers. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release
                                          						12.2(33)SRA. |
| XE 3.18SP | This command was integrated into Cisco NCS 4200 Series. |

| Command | Description |
|---|---|
| controller | Configures a T1 or E1 controller and enters controller configuration mode. |
| reload | Reloads
                                          						the operating system. |
| show controller | Displays the controller state that is specific to controller hardware |
| show interface serial | Displays the serial interface type and other information. |

| t3 | Specifies T3 connectivity of 44210 kbps through the network, using B8ZS coding. |
|---|---|
| e3 | Specifies a wide-area digital transmission scheme used predominantly in Europe that carries data at a rate of 34010 kbps. |
| slot | Slot number of the interface. |
| subslot | (Clear Channel T3/E3 Shared Port Adapters Only) Secondary slot number on a SIP where a SPA is installed. Refer to the platform-specific SPA hardware installation guide and the corresponding "Specifying the Interface Address on
                                          a SPA" topic in the platform-specific SPA software configuration guide for subslot information. |

| Release | Modification |
|---|---|
| 12.1(1)T | This command was introduced. |
| 12.2(11)YT | This command was integrated into Cisco IOS Release 12.2(11)YT and implemented on the following platforms: Cisco 2650XM, Cisco
                                          2651XM, Cisco 2691, Cisco 3660 series, Cisco 3725, and Cisco 3745 routers. |
| 12.2(15)T | This command was integrated into Cisco IOS Release 12.2(15)T. |
| 12.3(1) | This command was integrated into Cisco IOS Release 12.3(1) and support was added for Cisco 2610XM, Cisco 2611XM, Cisco 2620XM,
                                          Cisco 2621XM, Cisco 2650XM, Cisco 2651XM, Cisco 2691, Cisco 3631, Cisco 3660, Cisco 3725, and Cisco 3745 platforms. |
| 12.2S | This command was integrated into Cisco IOS Release 12.2S. |
| 12.2(25)S3 | This command was integrated into Cisco IOS Release 12.2(25)S3 to support SPAs on the Cisco 7304 routers. |
| 12.2(18)SXE | This command was integrated into Cisco IOS Release 12.2(18)SXE to support SPAs on the Cisco 7600 series routers and Catalyst
                                          6500 series switches. |
| 12.0(31)S | This command was integrated into Cisco IOS Release 12.0(31)S to support SPAs on the Cisco 12000 series routers. |
| 12.2(33)SRA | This command was integrated into Cisco IOS Release 12.2(33)SRA. |

| Command | Description |
|---|---|
| controller | Configures a T3 or E3 controller and enters controller configuration mode. |
| reload | Reloads the operating system. |
| show interface serial | Displays the serial interface type and other information. |

| source | Indicates the carrier that the dial peer uses as a matching key for inbound dial-peer matching. |
|---|---|
| target | Indicates the carrier that the dial peer uses as a matching key for outbound dial-peer matching. |
| name | Specifies the ID of the carrier to use for the call. Valid carrier IDs contain a maximum of 127 alphanumeric characters. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |

| Command | Description |
|---|---|
| translation-profile (dial peer) | Associates a translation profile with a dial peer. |
| trunkgroup (dial peer) | Assigns a trunk group to a source IP group or dial peer for trunk group label routing. |

| name | Identifier for the carrier ID. Must be four-digit numeric carrier identification code to be advertised as a TRIP carrier family
                                          but can be alphanumeric if used otherwise. |
|---|---|
| cic | (Optional) Specifies that the carrier ID is a circuit identification code (CIC). |

| Release | Modification |
|---|---|
| 12.3(1) | This command was introduced. |

| Command | Description |
|---|---|
| carrier-id (trunk group) | Configures the carrier ID locally on the trunk group. |

| name | The ID of the carrier to use for the call. Valid carrier IDs contain a maximum of 127 alphanumeric characters. To be advertised as a TRIP carrier family, this must be set to a four-digit numeric carrier identification code. |
|---|---|
| cic | (Optional) Specifies that the carrier ID is a circuit identification code. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |
| 12.3(1) | The cic keyword was added. |

| Command | Description |
|---|---|
| carrier-id (global) | Configures the carrier ID globally for all trunk groups. |
| translation-profile (trunk group) | Associates a translation profile with a trunk group. |
| trunk group | Initiates the definition of a trunk group. |

| source | Indicates the carrier ID associated with an incoming VoIP call at the terminating gateway. |
|---|---|
| target | Indicates the carrier ID used by the terminating gateway to match an outbound dial peer. |
| name | The ID of the carrier to use for the call. Valid carrier IDs contain a maximum of 127 alphanumeric characters. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |

| Note | If an incoming H.323 VoIP call matches a source IP group that has a target carrier ID, the source IP group’s target carrier
                                          ID overrides the VoIP call’s H.323 setup message. |
|---|---|

| Command | Description |
|---|---|
| voice source-group | Initiates the definition of a source IP group. |

| legacy | Sets the internal cause code to the former and nonstandard set of H.323 and SIP values. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |

| Command | Description |
|---|---|
| show call history voice | Displays the call history table for voice calls. |

| Release | Modification |
|---|---|
| 15.1(3)T | This command was introduced. |

| Command | Description |
|---|---|
| hold-resume | Turns the STCAPP supplementary-service features on and off using hookflash. |
| stcapp supplementary-services | Enters supplementary-service configuration mode for configuring STCAPP supplementary-service features on an FXS port. |

| port number | Port number for the transport protocol. The protocol may be User Data Protocol (UDP), Reliable User Datagram Protocol (RDUP),
                                          or TCP. Range is from 0 to 65535, and the specified value must not be a well-known reserved port number such as 1023. The
                                          default is 2428. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(3)T | This command was introduced with Cisco CallManager Version 3.0 and the Cisco Voice Gateway 200 (VG200). |
| 12.2(2)XA | The command was implemented on the Cisco 2600 series and Cisco 3600 series. |
| 12.2(4)T | The command was integrated into Cisco IOS Release 12.2(4)T. |

| Command | Description |
|---|---|
| ccm-manager redundant-host | Configures the IP address or the DNS name of up to two backup Cisco CallManagers. |
| ccm-manager switchback | Configures the switchback mode that determines when the primary Cisco CallManager is used if it becomes available again while
                                          a backup Cisco CallManager is being used. |

| dialpeer - prefix prefix | (Optional) Specifies the prefix to use for autogenerated dial peers. Range is 1 to 2147483647. The default is 999. Note When manually adding a dial peers prefix, select a prefix number other than the default. | Note | When manually adding a dial peers prefix, select a prefix number other than the default. |
|---|---|---|---|
| Note | When manually adding a dial peers prefix, select a prefix number other than the default. |
| server { ip-address \| name } | (Optional) Specifies the IP address or logical name of the TFTP server from which the XML configuration files are downloaded. The arguments are as follows: ip-address-- IP address of the TFTP server from which to download the XML configuration files to the local MGCP voice gateway. name-- Logical (symbolic) name of the TFTP server from which to download XML configuration files to the local MGCP voice gateway. |

| Note | When manually adding a dial peers prefix, select a prefix number other than the default. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XN | This command was introduced and implemented on the Cisco 2600 series, Cisco 3600 series, and the Cisco VG200. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T and implemented on the Cisco IAD2420 series. |

| Note | To keep manually added dial peers from being deleted from the running configuration when Cisco UCM downloads the configuration
                                          to the gateway, use a dial peer-prefix value other than the default (999). |
|---|---|

| Command | Description |
|---|---|
| debug ccm-manager config-download | Displays dialog during configuration download from the Cisco UCM to the gateway. |
| show ccm-manager config-download | Displays whether the Cisco UCM configuration is enabled. |

| Release | Modification |
|---|---|
| 12.2(15)ZJ | This command was introduced. |
| 12.3(4)T | This command was integrated into Cisco IOS Release 12.3(4)T. |

| Command | Description |
|---|---|
| cptone | Specifies a regional voice-interface-related tone, ring, and cadence setting. |
| debug ccm-manager | Displays debugging of Cisco CallManager. |
| show ccm-manager | Displays a list of Cisco CallManager servers and their current status and availability. |

| Release | Modification |
|---|---|
| 12.2(2)XN | This command was introduced on the Cisco 2600 series, Cisco 3600 series, and the Cisco VG200. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T and Cisco CallManager Version 3.2 and implemented on Cisco IAD2420
                                          series. |
| 12.2(15)ZJ | This command was integrated into Cisco IOS Release 12.2(15)ZJ. |
| 12.3(2)T | This command was implemented on the Cisco 26xxXM, Cisco 2691, Cisco 3640, Cisco 3640A, Cisco 3660, and Cisco 37xx. |

| Related Command | Purpose |
|---|---|
| ccm-manager config | Supplies the local MGCP voice gateway with the IP address or logical name of the TFTP server from which to download XML configuration
                                          files and enable the download of the configuration. |
| debug ccm-manager | Displays debugging information about the Cisco CallManager. |
| show ccm-manager fallback-mgcp | Displays the status of the MGCP gateway fallback feature. |

| cisco | Cisco-proprietary fax-relay protocol. This is the only choice. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(9)T | This command was introduced. |

| Command | Description |
|---|---|
| debug ccm-manager | Displays debugging of Cisco CallManager. |
| show ccm-manager | Displays a list of Cisco CallManager servers and their current status and availability. |
| show running-config | Displays the contents of the currently running configuration file. |

| codec-all | (Optional) Enables all codec on the gateway for the Cisco CallManager. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(3)T | This command was introduced with Cisco CallManager Version 3.0 on the Cisco VG200. |
| 12.2(2)XA | The command was integrated into Cisco IOS Release 12.2(2)XA and implemented on the Cisco 2600 series and Cisco 3600 series. |
| 12.2(2)XN | Support for enhanced MGCP voice gateway interoperability was added to Cisco CallManager Version 3.1 for the Cisco 2600 series,
                                          3600 series, and Cisco VG200. |
| 12.2(4)T | The command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(11)T | This command was integrated into the Cisco IOS Release 12.2(11)T and Cisco CallManager Version 3.2 and was implemented on
                                          the Cisco IAD2420 series routers. |
| 12.2(11)YU | This command was integrated into Cisco IOS Release 12.2(11)YU and implemented on the Cisco 1760 gateway. |
| 15.0(1)M | This command was modified in a release earlier than Cisco IOS Release 15.0(1)M. The codec-all keyword was added. |

| Command | Description |
|---|---|
| ccm-manager redundant-host | Configures the IP address or the DNS name of up to two backup Cisco CallManagers. |
| ccm-manager switchback | Configures the switchback mode that determines when the primary Cisco CallManager is used if it becomes available again while
                                          a backup Cisco CallManager is being used. |
| mgcp | Enables Media Gateway Control Protocol mode. |

| Release | Modification |
|---|---|
| 12.2(2)XN | This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco VG200. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T and Cisco CallManager Version 3.2 and implemented on the Cisco
                                          IAD 2420 series routers. |

| Command | Description |
|---|---|
| ccm-manager music-on-hold bind | Enables the multicast MOH feature on a voice gateways. |
| debug ccm-manager music-on-hold | Displays debugging information for MOH. |
| show ccm-manager music-on-hold | Displays MOH information. |

| type | Interface type to which the MOH feature is bound. The options follow: async -- Asynchronous interface bvi -- Bridge-Group Virtual Interface ctunnel -- CTunnel interface dialer -- Dialer interface ethernet -- IEEE 802.3 lex -- Lex interface loopback -- Loopback interface mfr -- Multilink Frame Relay bundle interface multilink -- Multilink interface null -- Null interface serial -- Serial interface tunnel -- Tunnel interface vif -- PGM Multicast Host interface virtual - FrameRelay --Virtual Frame Relay interface virtual - Template -- Virtual template interface virtual - TokenRing -- Virtual Token Ring |
|---|---|
| slot / port | Number of the slot being configured. See the appropriate hardware manual for slot and port information. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |

| Command | Description |
|---|---|
| ccm-manager music-on-hold | Enables the MOH feature. |
| debug ccm-manager music-on-hold | Displays debugging information for MOH. |
| show ccm-manager music-on-hold | Displays MOH information. |

| ip - address | IP address of the backup Cisco CallManager server. |
|---|---|
| dns - name | DNS name of the backup Cisco CallManager server. |

| Release | Modification |
|---|---|
| 12.1(3)T | This command was introduced with Cisco CallManager Version 3.0 on the Cisco Voice Gateway 200 (VG200). |
| 12.2(2)XA | The command was implemented on the Cisco 2600 series and Cisco 3600 series. The dns-name argument was added. |
| 12.2(4)T | The command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(2)XN | Support for enhanced MGCP voice gateway interoperability was added to Cisco CallManager Version 3.1 for the Cisco 2600 series,
                                          3600 series, and the Cisco VG200. |
| 12.2(11)T | This command was integrated into the Cisco IOS Release 12.2(11)T and Cisco CallManager Version 3.2 and implemented on the
                                          Cisco IAD2420 series routers. |

| Command | Description |
|---|---|
| ccm-manager application | Configures the port number for the redundant link application. |
| ccm-manager switchback | Configures the switchback mode that determines when the primary Cisco CallManager is used if it becomes available again while
                                          a backup Cisco CallManager is being used. |
| ccm-manager switchover-to-backup | Redirects (manually and immediately) a Cisco 2600 series router or Cisco 3600 series router to the backup Cisco CallManager
                                          server. |
| mgcp call-agent | Defines the Cisco CallManager server as the highest priority. |

| Release | Modification |
|---|---|
| 12.3(14)T | This command was introduced. |

| Command | Description |
|---|---|
| ccm-manager config | Specifies the TFTP server from which the Cisco IOS gateway downloads Cisco CallManager XML configuration files. |
| ccm-manager sccp local | Selects the local interface for SCCP application use for Cisco CallManager registration. |
| show ccm-manager config-download | Displays information about the status of the Cisco IOS gateway configuration download. |

| interface-type | Interface type that the SCCP application uses for Cisco CallManager registration. |
|---|---|
| interface-number | Interface number that the SCCP application uses for Cisco CallManager registration. |

| Release | Modification |
|---|---|
| 12.3(14)T | This command was introduced. |

| Command | Description |
|---|---|
| show ccm-manager | Displays a list of Cisco CallManager servers and their current status and availability. |

| Release | Modification |
|---|---|
| 12.4(8) | This command was introduced. |
| 12.4(9)T | This command was integrated into Cisco IOS Release 12.4(9)T. |
| 12.4(3f) | This command was integrated into Cisco IOS Release 12.4(3f). |
| 12.4(5c) | This command was integrated into Cisco IOS Release 12.4(5c). |
| 12.4(7c) | This command was integrated into Cisco IOS Release 12.4(7c). |
| 12.4(4)T5 | This command was integrated into Cisco IOS Release 12.4(4)T5. |
| 12.4(6)T4 | This command was integrated into Cisco IOS Release 12.4(6)T4. |

| Command | Description |
|---|---|
| ccm-manager mgcp | Enables the gateway to communicate with the Cisco Call Manager through the MGCP and to supply redundant control agent services. |

| retries | Number or TFTP retries. Range is from 2 to 10. The default is 2. |
|---|---|

| Release | Modification |
|---|---|
| 12.4(15)T2 | This command was introduced. |
| 12.4(20)T | This command was integrated into Cisco IOS Release 12.4(20)T. |

| Command | Description |
|---|---|
| show ccm-manager | Displays a list of Cisco Unified Communications Manager servers and their current status and availability. |

| graceful | Specifies that control is returned to the primary Cisco CallManager server after the last active call ends (when there is
                                          no voice call in active setup mode on the gateway). Default value. |
|---|---|
| immediate | Specifies an immediate switchback to the primary Cisco CallManager server when the TCP link to the primary Cisco CallManager
                                          server is established, regardless of current call conditions. |
| never | Specifies not to return control to the primary Cisco CallManager server, as long as the secondary is up and running. The gateway
                                          registers to primary if the secondary is down and when the primary is up and running. |
| schedule - time hh : mm | Specifies an hour and minute, based on a 24-hour clock, when control is returned to the primary Cisco CallManager server.
                                          If the specified time is earlier than the current time, the switchback occurs at the specified time on the following day. |
| uptime - delay minutes | Specifies the number of minutes the primary Cisco CallManager server must run after the TCP link to is reestablished and control
                                          is returned to that primary call agent. Valid values are from 1 to 1440 (1 minute to 24 hours). |

| Release | Modification |
|---|---|
| 12.1(3)T | This command was modified. This command was introduced with Cisco CallManager Version 3.0 on the Cisco VG200. |
| 12.2(2)XA | The command was implemented on the Cisco 2600 series and Cisco 3600 series. |
| 12.2(2)XN | Support for enhanced Media Gateway Control Protocol (MGCP) voice gateway interoperability was added to Cisco CallManager Version
                                          3.1 for the Cisco 2600 series, 3600 series, and the Cisco VG200. |
| 12.2(4)T | The command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(11)T | This command was implemented on the Cisco IAD2420 series routers. |
| 15.0(1)M | This command was modified in a release earlier than Cisco IOS Release 15.0(1)M. The never keyword was added. |

| Command | Description |
|---|---|
| ccm-manager application | Configures the port number for the redundant link application. |
| ccm-manager redundant-host | Configures the IP address or the DNS name of up to two backup Cisco CallManagers. |
| ccm-manager switchover-to-backup | Redirects a Cisco 2600 series or Cisco 3600 series router to the backup Cisco CallManager. |

| Release | Modification |
|---|---|
| 12.2(2)XN | This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco VG200. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T and Cisco CallManager Version 3.2 and implemented on the Cisco
                                          IAD2420 series. |

| Command | Description |
|---|---|
| ccm-manager application redundant-link | Configures the port number for the redundant link application (that is, for the secondary Cisco CallManager server). |
| ccm-manager redundant-host | Configures the IP address or the DNS name of up to two backup Cisco CallManager servers. |
| ccm-manager switchback | Specifies the time at which control is returned to the primary Cisco CallManager server once the server is available. |