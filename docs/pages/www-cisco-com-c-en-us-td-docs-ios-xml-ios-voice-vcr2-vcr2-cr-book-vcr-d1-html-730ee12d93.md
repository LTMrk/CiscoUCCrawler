---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-vcr2-vcr2-cr-book-vcr-d1-html-730ee12d93
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/vcr2/vcr2-cr-book/vcr-d1.html
retrieved_at: 2026-08-16T23:16:39.488341+00:00
---

Cisco IOS Voice Command Reference - D through I

# Cisco IOS Voice Command Reference - D through I

Updated: April 25, 2026

Chapter: default (auto-config application) through direct-inward-dial

## Chapter: default (auto-config application) through direct-inward-dial

# default (auto-config application) through direct-inward-dial

## default (auto-config application)

The documentation set for this product strives to use bias-free language. For purposes of this documentation set, bias-free
                                          is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity,
                                          sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language
                                          that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that
                                          is used by a referenced third-party product.

To configure an auto-config application configuration command to its default value, use the default command in auto-config application configuration mode.

default command

### Syntax Description

command

One of the auto-config application configuration commands. Valid choices are as follows:

retries

server

shutdown

timeout

### Command Default

No default behavior or values

### Command Modes

Auto-config application configuration (auto-config-app)

## Command History

Release

Modification

12.3(8)XY

This command was introduced on the Communication Media Module.

12.3(14)T

This command was integrated into Cisco IOS Release 12.3(14)T.

## Examples

The following example shows the default command used to set the number of download retry attempts for an auto-config application to its default value:

```
Router(auto-config-app)# default retries
```

### Related Commands

Command

Description

auto-config

Enables auto-configuration or enters auto-config application configuration mode for the SCCP application.

show auto-config

Displays the current status of auto-config applications.

## default (MGCP profile)

To configure a Media Gateway Control Protocol (MGCP profile) command to its default value, use the default command in MGCP profile configuration mode. To disable the default command, use the no form of the command for that profile parameter.

default command

no default command

### Syntax Description

command

One of the MGCP profile commands. Valid choices are as follows:

call-agent

description (MGCP profile)

max1 lookup

max1 retries

max2 lookup

max2 retries

package persistent

timeout tcrit

timeout tdinit

timeout tdmax

timeout tdmin

timeout thist

timeout tone busy

timeout tone cot1

timeout tone cot2

timeout tone dial

timeout tone dial stutter

timeout tone mwi

timeout tone network congestion

timeout tone reorder

timeout tone ringback

timeout tone ringback connection

timeout tone ringing

timeout tone ringing distinctive

timeout tpar

timeout tsmax

voice-port (MGCP profile)

### Command Default

No default behaviors or values

### Command Modes

MGCP profile configuration (config-mgcp-profile)

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T.

12.2(11)T

This command implemented on the Cisco AS5300 and Cisco AS5850.

### Usage Guidelines

This command is used when configuring values for an MGCP profile.

The default (MGCP profile) command instructs the MGCP profile to use the default value of the specified command whenever the profile is
                              called. This has the same effect as using the no form of the specified command, but the default command clearly specifies which commands are using their default values.

To use the default values for more than one command, enter each command on a separate line.

## Examples

The following example shows how to configure the default values for three MGCP profile commands:

```
Router(config)# mgcp profile newyork Router(config-mgcp-profile)# default max1 retries Router(config-mgcp-profile)# default timeout tdinit Router(config-mgcp-profile)# default timeout tone mwi
```

### Related Commands

Command

Description

mgcp

Starts and allocates resources for the MGCP daemon.

mgcp profile

Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile.

## default (SIP)

To reset a SIP command to its default value, use the default command in SIP configuration mode.

default command

### Syntax Description

command

One of the SIP configuration commands. Valid choices are:

bind : Configures the source address of signaling and media packets to a specific interface’s IP address.

rel1xx : Enables all SIP provisional responses (other than 100 Trying) to be sent reliably to the remote SIP endpoint.

session-transport : Configures the underlying transport layer protocol for SIP messages to TCP or UDP.

url : Configures URLs to either the SIP or TEL format for your voip sip calls.

### Command Default

The default is that binding is disabled ( no bind ).

### Command Modes

Voice service voip-sip configuration (conf-serv-sip)

## Command History

Release

Modification

12.2(2)XB

This command was introduced on the Cisco 2600 series, Cisco 3600 series, Cisco 7200 series, Cisco AS5300, Cisco AS5350, and
                                          Cisco AS5400 platforms.

12.2(2)XB2

This command was implemented on the Cisco AS5850 platform.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T and support was added for the Cisco 3700 series. Cisco AS5300,
                                          Cisco AS5350, Cisco AS5850, and Cisco AS5400 platforms were not supported in this release.

12.2(11)T

Support was added for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 platforms.

Cisco IOS XE Release 2.5

This command was integrated into Cisco IOS XE Release 2.5.

## Examples

The following example shows how to reset the value of the SIP bind command:

```
Router(config)# voice serv voip Router(conf-voi-serv)# sip Router(conf-serv-sip)# default bind
```

### Related Commands

Command

Description

sip

Enter SIP configuration mode from voice-service VoIP configuration mode.

## default-file vfc

To specify an additional (or different) file from the ones in the default file list and stored in voice feature card (VFC)
                              flash memory, use the default file vfc command in global configuration mode. To delete the file from the default file list, use the no form of this command.

default-file filename vfc slot

no default-file filename vfc slot

### Syntax Description

filename

Indicates the file to be retrieved from VFC flash memory and used to boot up the system.

slot

Indicates the slot on the Cisco AS5300 in which the VFC is installed. Range is to 2. There is no default value.

### Command Default

No default behavior or values

### Command Modes

Global configuration (config)

## Command History

Release

Modification

11.3(1)NA

This command was introduced on the Cisco AS5300.

12.0(3)T

This command was integrated into Cisco IOS Release 12.0(3)T.

### Usage Guidelines

When VCWare is unbundled, it automatically adds DSPWare to flash memory, creates both the capability and default file lists,
                              and populates these lists with the default files for that version of VCWare. The default file list includes the files that
                              are used to boot up the system.

Use the default-file vfc command to add a specified file to the default file list, replacing the existing default for that extension type.

## Examples

The following example specifies that the bas-vfc-1.0.14.0.bin file, which is stored in VFC flash memory, be added to the default
                              file list:

```
default-file bas-vfc-1.0.14.0.bin vfc 0
```

### Related Commands

Command

Description

cap-list vfc

Adds a voice codec overlay file to the capability file list.

delete vfc

Deletes a file from VFC flash memory.

## define

To define the transmit and receive bits for North American ear and mouth (E&M), E&M Mercury Exchange Limited Channel-Associated
                              Signaling (MELCAS), and Land Mobile Radio (LMR) voice signaling, use the define command in voice-port configuration mode. To restore the default value, use the no form of this command.

define { tx-bits | rx-bits } { seize | idle } { 0000 | 0001 | 0010 | 0011 | 0100 | 0101 | 0110 | 0111 | 1000 | 1001 | 1010 | 1011 | 1100 | 1101 | 1110 | 1111 }

no define { tx-bits | rx-bits } { seize | idle } { 0000 | 0001 | 0010 | 0011 | 0100 | 0101 | 0110 | 0111 | 1000 | 1001 | 1010 | 1011 | 1100 | 1101 | 1110 | 1111 }

### Syntax Description

tx-bits

The bit pattern applies to the transmit signaling bits.

rx-bits

The bit pattern applies to the receive signaling bits.

seize

The bit pattern defines the seized state.

idle

The bit pattern defines the idle state.

0000 through 1111

Specifies the bit pattern.

### Command Default

The default is to use the preset signaling patterns as defined in American National Standards Institute (ANSI) and European
                              Conference of Postal and Telecommunications Administrations (CEPT) standards, as follows:

- tx-bits idle 0000 (0001 if on E1 trunk)

- tx-bits seize 1111

- rx-bits idle 0000

- rx-bits seize 1111

- tx-bits idle 1101

- tx-bits seize 0101

- rx-bits idle 1101

- rx-bits seize 0101

- tx-bits idle 0000

- tx-bits seize 1111

- rx-bits idle 0000

- rx-bits seize 1111

### Command Modes

Voice-port configuration (config-voiceport)

## Command History

Release

Modification

11.3(1)MA3

This command was introduced on the Cisco MC3810.

12.0(7)XK

This command was implemented on the Cisco 2600 series and Cisco 3600 series.

12.1(2)T

The command was integrated into Cisco IOS Release 12.1(2)T.

12.3(4)XD

The LMR signaling type was added to the signaling types to which this command applies.

12.3(7)T

This command was integrated into Cisco IOS Release 12.3(7)T.

12.3(14)T

This command was implemented on the Cisco 2800 series and Cisco 3800 series.

12.4(2)T

This command was integrated into Cisco IOS Release 12.4(2)T.

### Usage Guidelines

The define command applies to E&M digital voice ports associated with T1/E1 controllers.

Use the define command to match the E&M bit patterns with the attached telephony device. Be careful not to define invalid configurations,
                              such as all 0000 on E1, or identical seized and idle states. Use this command with the ignore command.

In LMR signaling, the define command is used to define polarity on E&M analog and digital voice ports.

## Examples

To configure a voice port on a Cisco 2600 or Cisco 3600 series router that is sending traffic in North American E&M signaling
                              format to convert the signaling to MELCAS format, enter the following commands:

```
voice-port 1/0/0
 define rx-bits idle 1101
 define rx-bits seize 0101
 define tx-bits idle 1101
 define tx-bits seize 0101
```

In this example, reverse polarity is configured on a voice port on a Cisco 3700 series router that is sending traffic in LMR
                              signaling format:

```
voice-port 1/0/0
 define rx-bits idle 1111
 define rx-bits seize 0000
 define tx-bits idle 1111
 define tx-bits seize 0000
```

### Related Commands

Command

Description

condition

Manipulates the signaling bit-pattern for all voice signaling types.

ignore

Configures a North American E&M or E&M MELCAS voice port to ignore specific receive bits.

## delete vfc

To delete a file from voice feature card (VFC) flash memory, use the delete vfc command in privileged EXEC mode.

delete filename vfc slot

### Syntax Description

filename

Specifies the file in VFC flash memory to be deleted.

slot

Specifies the slot on the Cisco AS5300 in which the specified VFC resides. Range is from 0 to 2.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

11.3(1)NA

This command was introduced on the Cisco AS5300.

12.0(3)T

This command was integrated into Cisco IOS Release 12.0(3)T.

### Usage Guidelines

Use the delete vfc command to delete a specific file from VFC flash memory and to remove the file from the default list or capability list if
                              the specified file is included in those lists.

Deleting a file from VFC flash memory does not free the VFC flash memory space that the file occupied. To free VFC flash memory
                                          space, use the erase vfc command.

## Examples

The following example deletes the bas-vfc-1.0.14.0.bin file, which is stored in VFC flash memory of the VFC located in slot
                              0:

```
Router# delete bas-vfc-1.0.14.0.bin vfc 0
```

### Related Commands

Command

Description

default-file vfc

Specifies an additional (or different) file from the ones in the default file list and stored in VFC flash memory.

erase vfc

Erases the flash memory of a specified VFC.

show vfc directory

Displays the list of all files that reside on this VFC.

## description

To specify a description of the digital signal processor (DSP) interface, use the description command in voice-port or DSP farm interface configuration mode. To describe a MGCP profile that is being defined, use the description command in MGCP profile configuration mode. To specify the name or a brief description of a charging profile, use the description command in charging profile configuration mode. To delete a configured description, use the no form of the command in the appropriate configuration mode.

description string

no description

### Syntax Description

string

Character string from 1 to 80 characters for DSP interfaces and MGCP profiles, or from 1 to 99 characters for charging profiles.

### Command Default

Enabled with a null string. The MGCP profile has no default description. Charging profiles have no default description.

### Command Modes

Voice-port configuration (config-voiceport) DSP farm interface configuration (config-dspfarm-profile) MGCP profile configuration (config-mgcp-profile) Charging profile configuration (ch-prof-conf)

### Usage Guidelines

The use of a special character such as '\'(backslash) and a three or more digit number for the character setting like description , results in incorrect translation.

## Command History

Release

Modification

11.3(1)T

This command was introduced on the Cisco 3600 series and Cisco 7200.

11.3(1)MA

This command in voice-port configuration mode was implemented on the Cisco MC3810.

12.0(5)XE

This command in DSP farm interface configuration mode was modified.

12.1(1)T

The DSP farm interface configuration mode modification was integrated into Cisco IOS Release 12.1(1)T.

12.2(2)XA

This command was implemented on the Cisco AS5300.

12.2(11)T

This command was implimented on the Cisco AS5850 and integrated into Cisco IOS Release 12.2(11)T.

12.3(8)XU

This command was introduced in charging profile configuration mode.

12.3(11)YJ

This command in charging profile configuration mode was integrated into Cisco IOS Release 12.3(11)YJ.

12.3(14)YQ

This command in charging profile configuration mode was integrated into Cisco IOS Release 12.3(14)YQ.

12.4(9)T

This was integrated into Cisco IOS Release 12.4(9)T.

12.2(33)SXH

This command was changed to allow the description to contain spaces.

### Usage Guidelines

Use the description command to describe the DSP interface connection or a defined MGCP profile. The information is displayed when a show command is used, and it does not affect the operation of the interface in any way.

In Release 12.2(33)SXH and later releases, you can enter spaces in the description.

## Examples

The following example identifies voice port 1/0/0 as being connected to the purchasing department:

```
voice-port 1/0/0
 description purchasing-dept
```

The following example identifies DSP farm interface 1/0 as being connected to the marketing department:

```
dspint dspfarm 1/0
 description marketing-dept
```

The following example shows a description for an MGCP profile:

```
mgcp profile newyork
 description This is the head sales office in New York.
 dot ...(socket=0)
 S:.
 R:250 NAA09092 Message accepted for delivery
 S:QUIT
 R:221 madeup@abc.com closing connection
 Freeing SMTP ctx at 0x6121D454
 returned from work-routine, context freed
```

The following example describes a charging profile as APN-level default for home users:

```
gprs charging profile
 description APN-level_default_for_home_users
```

### Related Commands

Command

Description

category

Identifies the subscriber category to which a charging profile applies.

cdr suppression

Specifies that CDRs be suppressed as a charging characteristic in a charging profile.

charging profile

Associates a default charging profile to an access point.

content dcca profile

Defines a DCCA client profile in a GGSN charging profile.

content postpaid time

Specifies, as a trigger condition for postpaid users in a charging profile, the time duration limit that when exceeded causes
                                          the GGSN to collect upstream and downstream traffic byte counts and close and update the G-CDR for a particular PDP context.

content postpaid validity

Specifies, as a trigger condition in a charging profile, that the amount of time quota granted to a postpaid user is valid.

content postpaid volume

Specifies, as a trigger condition for postpaid users in a charging profile, the maximum number of bytes that the GGSN maintains
                                          across all containers for a particular PDP context before closing and updating the G-CDR.

content rulebase

Associates a default rule-base ID with a charging profile.

gprs charging characteristics reject

Specifies that create PDP context requests for which no charging profile can be selected be rejected by the GGSN.

gprs charging container time-trigger

Specifies a global time limit that when exceeded by a PDP context causes the GGSN to close and update the G-CDR for that
                                          particular PDP context.

gprs charging profile

Creates a new charging profile (or modifies an existing one) and enters charging profile configuration mode.

limit duration

Specifies, as a trigger condition in a charging profile, the time duration limit that when exceeded causes the GGSN to collect
                                          upstream and downstream traffic byte counts and close and update the G-CDR for a particular PDP context.

limit sgsn-change

Specifies, as a trigger condition in a charging profile, the maximum number of GGSN changes that can occur before closing
                                          and updating the G-CDR for a particular PDP context.

limit volume

Specifies, as a trigger condition in a charging profile, the maximum number of bytes that the GGSN maintains across all containers
                                          for a particular PDP context before closing and updating the G-CDR.

mgcp

Starts and allocates resources for the MGCP daemon.

mgcp profile

Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile.

tariff-time

Specifies that a charging profile use the tariff changes configured using the gprs charging tariff-time global configuration command.

## description (ctl file)

To set a description for the Cisco Certificate Trust List (CTL) file, use the description command in CTL file configuration mode. To remove the description for the CTL file, use the no form of the command.

description description

## Syntax Description

Description of the CTL file. The maximum length of the description is 100 characters.

### Command Default

No description is set.

### Command Modes

CTL file configuration mode (config-ctl-file)

## Command History

15.3(3)M

This command was introduced.

### Usage Guidelines

## Examples

The following example shows how to set a description for the CTL file instance:

```
Device(config)# voice-ctl-file myctl
Device(config-ctl-file)# description ctlfile1
```

## description (dial peer)

To add a description to a dial peer, use the description command in dial peer configuration mode. To remove the description, use the no form of this command.

description string

no description

### Syntax Description

string

Text string up to 64 alphanumeric characters.

### Command Default

Disabled

### Command Modes

Dial peer configuration (config-dial-peer)

## Command History

Release

Modification

12.2(2)T

This command was introduced.

Introduced support for YANG models.

### Usage Guidelines

Use this command to include descriptive text about the dial peer. The description displays in show command output and does not affect the operation of the dial peer.

## Examples

The following example shows a description included in a dial peer:

```
dial-peer voice 1 pots
 description inbound PSTN calls
```

### Related Commands

Command

Description

dial-peer voice

Defines a dial peer.

show dial-peer voice

Displays configuration information for dial peers.

## description (DSP farm profile)

To include a description about the digital signal processor (DSP) farm profile, use the description command in DSP farm profile configuration mode. To remove a description, use the no form of this command.

description text

no description text

### Syntax Description

text

Character string from 1 to 80 characters.

### Command Default

No default behavior or values

### Command Modes

DSP farm profile configuration (config-dspfarm-profile)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

### Usage Guidelines

Use this command to include descriptive text about this DSP farm profile. This information displays in show commands and does not affect the operation of the interface.

## Examples

The following example identifies the DSP farm profile as being designated to the art department:

```
Router(config-dspfarm-profile)# description art dept
```

### Related Commands

Command

Description

codec (DSP farm profile)

Specifies the codecs supported by a DSP farm profile.

dspfarm profile

Enters DSP farm profile configuration mode and defines a profile for DSP farm services.

maximum sessions (DSP Farm profile)

Specifies the maximum number of sessions that need to be supported by the profile.

shutdown (DSP farm profile)

Allocates DSP farm resources and associates with the application.

## description (dspfarm)

To include a specific description about the digital signal processor (DSP) interface, use the description command in DSP farm interface configuration mode. To disable this feature, use the no form of this command.

description string

no description string

### Syntax Description

string

Character string from 1 to 80 characters.

### Command Default

Enabled with a null string.

### Command Modes

DSP farm interface configuration (config-dspfarm-profile)

## Command History

Release

Modification

11.3(1)T

This command was introduced for the Cisco 7200 series routers.

12.0(5)XE

This command was modified to reduce the maximum number of allowable characters in a text string from 255 to 80.

12.1(1)T

This command was integrated into Cisco IOS Release 12.1(1)T.

### Usage Guidelines

Use the description command to include descriptive text about this DSP farm interface connection. This information is displayed when you issue
                              a show command and does not affect the operation of the interface in any way.

## Examples

The following example identifies DSP farm interface 1/0 on the Cisco 7200 series routers router as being connected to the
                              marketing department:

```
dspint dspfarm 1/0
description marketing dept
```

## description (media-profile)

To include a description specific to a media profile in CUBE , use the description command in media profile configuration mode. To remove the description, use the no form of this command.

connection description string

no connection description string

### Syntax Description

string

A description specific to the media profile.

### Command Default

Disabled by default.

### Command Modes

Media Profile configuration mode (cfg-mediaprofile)

## Command History

Release

Modification

Cisco IOS XE Bengaluru 17.6.1a

This command was introduced on Cisco Unified Border Element.

### Usage Guidelines

The description command provides details specific to a media profile.

## Examples

The following is a sample configuration for description (media-profile) in CUBE :

```
router(cfg-mediaprofile)#description ?
WORD Specify hostname or IP address of proxy server

router(cfg-mediaprofile)#description <text>
```

### Related Commands

Command

Description

media profile stream-service

Enables stream service on CUBE .

connection (media-profile)

Configures idle timeout and call threshold for a media profile.

proxy (media-profile)

Configures IP address or hostname of proxy in media profile.

source-ip (media-profile)

Configures local source IP address of a WebSocket connection.

media class

Applies the media class at the dial peer level.

## description (phone proxy)

To specify a description for the phone proxy, use the description command in phone proxy configuration mode. To remove the description, use the no form of the command.

description description

no description

### Syntax Description

This command has no arguments or keywords.

### Command Default

No description is specified.

### Command Modes

Phone proxy configuration mode (config-phone-proxy)

## Command History

15.3(3)M

This command was introduced.

### Usage Guidelines

## Examples

The following example shows how to create a phone proxy instance called first-pp, enter phone-proxy configuration mode, and
                              set the description for this instance:

```
Device(config)# voice-phone-proxy first-pp
Device(config-phone-proxy)# description cluster-test
```

## description (SCCP Cisco CallManager)

To include a description about the Cisco CallManager group, use the description command in SCCP Cisco CallManager configuration mode. To remove a description, use the no form of this command.

description text

no description

### Syntax Description

text

Character string from 1 to 80 characters.

### Command Default

No default behavior or values

### Command Modes

SCCP Cisco CallManager configuration (config-sccp-ccm)

## Command History

Release

Modification

12.3(8)T

This command was introduced.

### Usage Guidelines

Use this command to include descriptive text about a Cisco CallManager group. This information is displayed in show commands and does not affect the operation of the interface.

## Examples

The following example identifies SCCP as being designated to the Boston office:

```
Router(config-sccp-ccm)# description boston office
```

### Related Commands

Command

Description

associate ccm

Associates a Cisco CallManager with a Cisco CallManager group and establishes its priority within the group.

connect retries

Specifies the number of times that a DSP farm attempts to connect to a Cisco CallManager when the current Cisco CallManager
                                          connections fails.

sccp ccm group

Creates a Cisco CallManager group and enters SCCP Cisco CallManager configuration mode.

## description (trunk group)

To add a description to a trunk group, use the description command in trunk group configuration mode. To delete the description, use the no form of this command.

description string

no description string

### Syntax Description

string

Trunk group description. Maximum length is 63 alphanumeric characters.

### Command Default

No default behavior or values

### Command Modes

Trunk group configuration (config-trunk-group)

## Command History

Release

Modification

12.2(11)T

This command was introduced.

## Examples

The following example shows a description for a trunk group:

```
Router(config)# trunk group alpha1 Router(config-trunk-group)# description carrierAgroup1
```

### Related Commands

Command

Description

trunk group

Initiates the definition of a trunk group.

## description (voice class)

To provide a TLS profile group description, and associate it to a TLS profile, use
                              the command description in voice class configuration mode.
                              To delete the TLS profile group description, use no form
                              of this command.

description tls-profile-group-label

no description

### Syntax Description

tls-profile-group-label

Allows you to provide a description for the TLS profile
                                          group.

### Command Default

No default behavior or values

### Command Modes

Voice class configuration (config-class)

## Command History

Release

Modification

This command was introduced under voice class configuration
                                          mode.

### Usage Guidelines

The TLS profile group description is associated to a TLS profile through the command voice class tls-profile tag . The tag associates the TLS profile group description
                              to the command crypto signaling .

## Examples

The following example illustrates how to create a voice class tls-profile and
                              associate a description TLS profile group:

```
Router(config)#voice class tls-profile 2
Router(config-class)#description tlsgroupname
```

### Related Commands

Command

Description

voice class tls-profile

Provides sub-options to configure the commands that are required
                                          for a TLS session.

crypto signaling

Identifies the trustpoint or the tls-profile tag that is used during the TLS handshake
                                          process.

## description (voice source group)

To add a description to a voice source group, use the description command in voice source-group configuration mode. To delete the description, use the no form of this command.

description string

no description string

### Syntax Description

string

Describes a voice source group, Maximum length of the voice source group description is 63 alphanumeric characters.

### Command Default

No default behavior or values

### Command Modes

Voice source-group configuration (cfg-source-grp)

## Command History

Release

Modification

12.2(11)T

This command was introduced.

## Examples

The following example shows a description for a voice source group:

```
Router(config)# voice source-group northern1 Router(cfg-source-grp)# description carrierBgroup3
```

### Related Commands

Command

Description

voice source-group

Defines a source group for voice calls.

## destination e164-pattern-map

To link an E.164 pattern map to a dial peer, use the destination e164-pattern-map command in dial peer configuration mode. To remove the link of an E.164 pattern map from a dial peer, use the no form of this command.

destination e164-pattern-map tag

no destination e164-pattern-map

### Syntax Description

tag

A number that defines a destination E.164 pattern map. The range is from 1 to 10000.

### Command Default

An E.164 pattern map is not linked to a dial peer.

### Command Modes

Dial peer configuration (config-dial-peer)

## Command History

Release

Modification

15.2(4)M

This command was introduced.

### Usage Guidelines

To support dial peer with multiple destination patterns, which involve massive dial peer configuration, use an E.164 destination
                              pattern map. You can create a destination E.164 pattern map and then link it to one or more dial peers. Based on the validation
                              of a pattern map, you can enable or disable one or more dial peers linked to the destination E.164 pattern map. To get the
                              status of the configured E.164 pattern map, use the show dial-peer voice command in dial peer configuration mode.

## Examples

The following example shows how to link an E.164 pattern map to a dial peer:

```
Device(config)# dial-peer voice 123 voip system Device(config-dial-peer)# destination e164-pattern-map 2154
```

### Related Commands

Command

Description

destination-pattern

Specifies either the prefix or the full E.164 telephone number to be used for a dial peer

e164

Configures an E.164 entry on a destination E.164 pattern map.

show dial-peer voice

Displays configuration information and call statistics for dial peers.

url

Specifies the URL of a text file that has E.164 pattern entries configured on a destination E.164 pattern map.

## destination uri

To specify the voice class used to match a dial peer to the destination uniform resource identifier (URI) of an outgoing
                              call, use the destination uri command in dial peer configuration mode. To remove the URI voice class, use the no form of this command.

destination uri tag

no destination uri

### Syntax Description

tag

Alphanumeric label that uniquely identifies the voice class. This tag must be configured with the voice class uri command.

### Command Default

No default behavior or values

### Command Modes

Dial peer configuration (config-dial-peer)

## Command History

Release

Modification

12.3(4)T

This command was introduced.

### Usage Guidelines

Before you use this command, configure the voice class by using the voice class uri command.

This command applies new rules for dial-peer matching. The table below shows the rules and the order in which they are applied
                              when the destination uri command is used. The gateway compares the dial-peer command to the call parameter in its search to match an outbound call
                              to a dial peer. All dial peers are searched based on the first match criteria on . Only if no match is found does the gateway
                              move on to the next criteria on.

Match Order

Cisco IOS Command

Outgoing Call Parameter

1

destination uri and carrier-id target

Application-provided URI and target carrier ID associated with the call

2

destination-pattern and carrier-id target

Called number and target carrier ID associated with the call

3

destination uri

Application-provided URI

4

destination-pattern

Called number

5

carrier-id target

Target carrier ID associated with the call

Calls whose destination is an E.164 number, rather than a URI, use the previously existing dial-peer matching rules. For
                                          information, see the Dial Peer Configuration on Voice Gateway Routers document, Cisco IOS Voice Library.

## Examples

The following example matches the destination URI in the outgoing call by using voice class ab100:

```
dial-peer voice 100 voip
 destination uri ab100
```

### Related Commands

Command

Description

answer-address

Specifies the calling number to match for a dial peer.

debug voice uri

Displays the debugging messages related to URI voice classes.

destination-pattern

Specifies the telephone number to match for a dial peer.

dial-peer voice

Enters dial peer configuration mode to create or modify a dial peer.

incoming uri

Specifies the voice class that a VoIP dial peer uses to match the URI of an incoming call.

pattern

Matches a call based on the entire SIP or TEL URI.

session protocol

Specifies a session protocol for calls between local and remote routers using the packet network.

show dialplan uri

Displays which outbound dial peer is matched for a specific destination URI.

voice class uri

Creates or modifies a voice class for matching dial peers to calls containing a SIP or TEL URI.

## destination-pattern

To specify either
                              		  the prefix or the full E.164 telephone number to be used for a dial peer, use
                              		  the destination-pattern command in dial peer
                              		  configuration mode. To disable the configured prefix or telephone number, use
                              		  the no form of this
                              		  command.

destination-pattern [ + ] string [ T ]

no destination-pattern [ + ] string [ T ]

### Syntax Description

+

(Optional) Character that indicates an E.164 standard number.

string

Series of
                                          						digits that specify a pattern for the E.164 or private dialing plan telephone
                                          						number. Valid entries are the digits 0 through 9, the letters A through D, and
                                          						the following special characters:

The
                                                							 asterisk (*) and pound sign (#) that appear on standard touch-tone dial pads.

Comma
                                                							 (,), which inserts a pause between digits.

Period (.), which matches any entered digit (this character is used as a
                                                							 wildcard).

Percent sign (%), which indicates that the preceding digit occurred zero or
                                                							 more times; similar to the wildcard usage.

Plus
                                                							 sign (+), which indicates that the preceding digit occurred one or more times.

The
                                                      						  plus sign used as part of a digit string is different from the plus sign that
                                                      						  can be used preceding a digit string to indicate that the string is an E.164
                                                      						  standard number.

Circumflex (^), which indicates a match to the beginning of the string.

Dollar sign ($), which matches the null string at the end of the input string.

Backslash symbol (\), which is followed by a single character, and matches that
                                                							 character. Can be used with a single character with no other significance
                                                							 (matching that character).

Question mark (?), which indicates that the preceding digit occurred zero or
                                                							 one time.

Brackets ([ ]), which indicate a range. A range is a sequence of characters
                                                							 enclosed in the brackets; only numeric characters from 0 to 9 are allowed in
                                                							 the range.

Parentheses (( )), which indicate a pattern and are the same as the regular
                                                							 expression rule.

T

(Optional) Control character that indicates that the destination-pattern value is a variable-length
                                          						dial string. Using this control character enables the router to wait until all
                                          						digits are received before routing the call.

### Command Default

The command is
                              		  enabled with a null string.

### Command Modes

Dial peer configuration (config-dial-peer)

## Command History

Release

Modification

11.3(1)T

This
                                          						command was introduced on the Cisco 3600 series.

11.3(1)MA

This
                                          						command was implemented on the Cisco MC3810.

12.0(4)XJ

This
                                          						command was modified for store-and-forward fax.

12.1(1)

The
                                          						command was integrated into Cisco IOS Release 12.1(1).

12.0(7)XR

This
                                          						command was implemented on the Cisco AS5300 and modified to support the plus
                                          						sign, percent sign, question mark, brackets, and parentheses symbols in the
                                          						dial string.

12.0(7)XK

This
                                          						command was modified. Support for the plus sign, percent sign, question mark,
                                          						brackets, and parentheses in the dial string was added to the Cisco 2600
                                          						series, Cisco 3600 series, and Cisco MC3810.

12.1(1)T

This
                                          						command was integrated into Cisco IOS Release 12.1(1)T and implemented on the
                                          						Cisco 1750, Cisco 7200 series, and Cisco 7500 series. The modifications for the
                                          						Cisco MC3810 in Cisco IOS Release12.0(7)XK are not supported in this release.

12.1(2)T

The
                                          						modifications made in Cisco IOS Release 12.0(7)XK for the Cisco MC3810 were
                                          						integrated into Cisco IOS Release 12.1(2)T.

12.2(8)T

This
                                          						command was implemented on the Cisco 1751, Cisco 2600 series and Cisco 3600
                                          						series, Cisco 3725, and Cisco 3745.

12.2(13)T

This
                                          						command was integrated into Cisco IOS Release 12.2(13)T and implemented on the
                                          						Cisco 2600XM, the Cisco ICS7750, and the Cisco VG200.

12.4(22)T

Support
                                          						for IPv6 was added.

Cisco
                                          						IOS XE Release 3.3S

This
                                          						command was integrated into Cisco IOS XE Release 3.3S.

15.2(4)M

This command was modified. With CSCub65380, behavior of dial
                                          						peers with destination-patterns configured with + symbol was rectified. The + symbol is no longer dropped from the dial peers and
                                          						matching occurs as expected

Introduced support for YANG models.

### Usage Guidelines

Use the destination-pattern command to define the E.164
                              		  telephone number for a dial peer.

The pattern you
                              		  configure is used to match dialed digits to a dial peer. The dial peer is then
                              		  used to complete the call. When a router receives voice data, it compares the
                              		  called number (the full E.164 telephone number) in the packet header with the
                              		  number configured as the destination pattern for the voice-telephony peer. The
                              		  router then strips out the left-justified numbers that correspond to the
                              		  destination pattern. If you have configured a prefix, the prefix is prepended
                              		  to the remaining numbers, creating a dial string that the router then dials. If
                              		  all numbers in the destination pattern are stripped out, the user receives a
                              		  dial tone.

There are areas
                              		  in the world (for example, certain European countries) where valid telephone
                              		  numbers can vary in length. Use the optional control character T to indicate that a particular destination-pattern value is a variable-length
                              		  dial string. In this case, the system does not match the dialed numbers until
                              		  the interdigit timeout value has expired.

Cisco IOS
                                          			 software does not verify the validity of the E.164 telephone number; it accepts
                                          			 any series of digits as a valid number.

## Examples

The following
                              		  example shows configuration of the E.164 telephone number 555-0179 for a dial
                              		  peer:

```
dial-peer voice 10 pots
 destination-pattern +5550179
```

The following
                              		  example shows configuration of a destination pattern in which the pattern "43"
                              		  is repeated multiple times preceding the digits "555":

```
dial-peer voice 1 voip
 destination-pattern 555(43)+
```

The following
                              		  example shows configuration of a destination pattern in which the preceding
                              		  digit pattern is repeated multiple times:

```
dial-peer voice 2 voip
 destination-pattern 555%
```

The following
                              		  example shows configuration of a destination pattern in which the possible
                              		  numeric values are between 5550109 and 5550199:

```
dial-peer voice 3 vofr
 destination-pattern 55501[0-9]9
```

The following
                              		  example shows configuration of a destination pattern in which the possible
                              		  numeric values are between 5550439, 5553439, 5555439, 5557439, and 5559439:

```
dial-peer voice 4 voatm
 destination-pattern 555[03579]439
```

The following
                              		  example shows configuration of a destination pattern in which the
                              		  digit-by-digit matching is prevented and the entire string is received:

```
dial-peer voice 2 voip
 destination-pattern 555T
```

### Related Commands

Command

Description

answer-address

Specifies the full E.164 telephone number to be used to identify the dial peer
                                          						of an incoming call.

dial-peer terminator

Designates a special character to be used as a terminator for variable-length
                                          						dialed numbers.

incoming called-number (dial peer)

Specifies a digit string that can be matched by an incoming call to associate
                                          						that call with a dial peer.

prefix

Specifies the prefix of the dialed digits for a dial peer.

timeouts interdigit

Configures the interdigit timeout value for a specified voice port.

## destination-pattern (interface)

To specify the ISDN directory number for the telephone interface, use the destination-pattern command in interface configuration mode. To disable the specified ISDN directory number, use the no form of this command.

destination-pattern isdn

no destination-pattern

### Syntax Description

isdn

Local ISDN directory number assigned by your telephone service provider.

### Command Default

A default ISDN directory number is not defined for this interface.

### Command Modes

Interface configuration (config-if)

## Command History

Release

Modification

12.0(3)T

This command was introduced on the Cisco 800 series.

### Usage Guidelines

This command is applicable to the Cisco 800 series routers.

You must specify this command when creating a dial peer. This command does not work if it is not specified within the context
                              of a dial peer. For information on creating a dial peer, refer to the Cisco 800 Series Routers Software Configuration Guide .

Do not specify an area code with the local ISDN directory number.

## Examples

The following example specifies 555-0101 as the local ISDN directory number:

```
destination-pattern 5550101
```

### Related Commands

Command

Description

dial-peer voice

Enters dial peer configuration mode, defines the type of dial peer, and defines the tag number associated with a dial peer.

no call-waiting

Disables call waiting.

port (dial peer)

Enables an interface on a PA-4R-DTR port adapter to operate as a concentrator port.

ring

Sets up a distinctive ring for telephones, fax machines, or modems connected to a Cisco 800 series router.

show dial-peer voice

Displays configuration information and call statistics for dial peers.

## destination route-string

To configure a destination route string, use the destination route-string command in dial peer configuration mode. To remove the destination route string, use the no form of this command.

destination route-string tag

no destination route-string

## Syntax Description

The route string tag defined by the route string class. The range is from 1 to 10000.

### Command Default

No destination route string is configured.

### Command Modes

Dial peer configuration (config-dial-peer)

## Command History

15.3(3)M

This command was introduced.

Cisco IOS XE Release 3.10S

This command was integrated into Cisco IOS XE Release 3.10S.

### Usage Guidelines

Use the destination route-string command to configure a voice class to match a destination route string. The destination route string defined in dial-peer
                              voice configuration mode is used to match an outbound dial peer.

## Examples

The following example shows how to match the destination route string:

```
Device> enable Device# configure terminal Device(config)# dial-peer voice 100 voip Device(config-dial-peer)# destination route-string 2
```

### Related Commands

Command

Description

voice class route-string

Assigns a unique identifier tag to a route string.

## detect v54 channel-group

To enable V.54 loopback detection for the command sent from the
                              		  remote device, use the detect v54 channel-group command in controller configuration mode. To disable the V.54
                              		  loopback detection, use the no form of this command.

detect v54 channel-group channel-number

no detect v54 channel-group channel-number

### Syntax Description

channel-number

Channel number from 1 to 24 (T1) or from 1 to 31 (E1).

### Command Default

V.54 loopback detection is disabled.

### Command Modes

Controller configuration (config-controller)

## Command History

Release

Modification

12.1(1)T

This command was introduced on the Cisco 2600 series and
                                          						Cisco 3600 series.

### Usage Guidelines

Use the detect v54 channel-group controller configuration command to
                              		  enable V.54 loopback detection. The remote device sends a loopup inband payload
                              		  command sequence in fractional T1 (FT1).

## Examples

The following example sets the loopback detection for
                              		  channel - group 1; then the loopback detection is
                              		  disabled for channel-group 1:

```
detect v54 channel-group 1
no detect v54 channel-group 1
```

### Related Commands

Command

Description

loopback remote v54 channel-group

Activates a remote V.54 loopback for the channel group on
                                          						the far end.

## detect-fax mode

To define fax detection and redirect as local or refer mode, use the detect-fax [ mode {refer | local} ] number command in dial peer configuration mode. To disable the mode of fax detection and redirect, use the no form of this command.

detect-fax [ mode {refer | local} ] number

no detect-fax [ mode {refer | local} ] number

### Syntax Description

number

The directory number of the fax machine.

### Command Default

Fax  mode detection is disabled.

### Command Modes

Dial Peer configuration (config-dial-peer)

## Command History

Release

Modification

This command was introduced for Unified Border Element.

### Usage Guidelines

Use the detect-fax [ mode {refer | local} ] number configuration command to enable detection of fax mode. Also, it refers to the directory number of the fax machine for redirect.

## Examples

The following is a sample configuration of local redirect mode for fax detection in Unified Border Element:

```
dial-peer voice 410 voip
 description "Incoming dial-peer to CUBE for fax"
 session protocol sipv2
 incoming called-number 903309
 codec g711ulaw
 detect-fax mode local 12101 12102

dial-peer voice 411 voip
 description "Outgoing dial-peer to VVB"
 destination-pattern 309903
 session protocol sipv2
 session target ipv4:9.42.25.148 //VVB IP Address
 codec g711ulaw

dial-peer voice 412 voip
 description "Incoming dial-peer for VVB"
 session protocol sipv2
 incoming called-number 309903
 codec g711ulaw
```

### Related Commands

Command

Description

fax-relay (dial peer)

Enables the suppression of call menu (CM) tones or answer (ANS) tones from reaching the Super Group 3 (SG3) fax machines.

## device-id

To identify a gateway associated with a settlement provider, use the device-id command in settlement configuration mode. To reset to the default value, use the no form of this command.

device-id number

no device-id number

### Syntax Description

number

Device ID number as provided by the settlement server. Range is from 0 to 2147483647.

### Command Default

The default device ID is 0.

### Command Modes

Settlement configuration (config-settlement)

## Command History

Release

Modification

12.0(4)XH1

This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco AS5300.

12.1(1)T

This command was integrated into Cisco IOS Release 12.1(1)T.

### Usage Guidelines

Identifying a gateway associated with a settlement provider is optional.

## Examples

The following example sets the device ID to 1000:

```
settlement 0
 device-id 1000
```

### Related Commands

Command

Description

customer-id

Identifies a carrier or Internet service provider with the settlement provider.

settlement

Enters settlement configuration mode.

## dhcp interface

To configure an interface type for Dynamic Host Configuration Protocol (DHCP) provisioning of Session Initiation Protocol
                              (SIP) parameters, use the dhcp interface command in SIP user-agent configuration mode.

dhcp interface type number

### Syntax Description

type

Type of interface to be configured.

number

Port, connector, or interface card number.

The number format varies depending on the network module or line card type and the router’s chassis slot it is installed
                                                      in. The numbers are assigned at the factory at the time of installation or when they are added to a system; they can be displayed
                                                      with the show interfaces command.

### Command Default

No interface type is configured for DHCP provisioning of SIP parameters.

### Command Modes

SIP UA configuration (config-sip-ua)

## Command History

Release

Modification

12.4(22)YB

This command was introduced.

15.0(1)M

This command was integrated in Cisco IOS Release 15.0(1)M.

### Usage Guidelines

Multiple interfaces on the Cisco Unified Border Element can be configured with DHCP. The dhcp interface command specifies which one is the DHCP interface used with SIP.

This command does not have a no form.

The table below displays the keywords that represent the types of interfaces that can be configured with the dhcp interface command. Replace the type argument with the appropriate keyword from the table.

Keyword

Interface Type

ethernet

Ethernet IEEE 802.3 interface.

fastethernet

100-Mbps Ethernet interface. In RITE configuration mode, specifies the outgoing (monitored) interface for exported IP traffic.

gigabitethernet

1000-Mbps Ethernet interface.

tengigabitethernet

10-Gigabit Ethernet interface.

## Examples

The following example configures the Gigabit Ethernet interface of slot 0 port 0 as the DHCP interface for DHCP provisioning
                              of SIP parameters:

```
Router> enable
Router# configure terminal
Router(config)# interface gigabitethernet 0/0 
Router(config-if)# ip address dhcp Router(config-if)# sip-ua
Router(sip-ua)# dhcp interface gigabitethernet 0/0
```

### Related Commands

Command

Description

show interfaces

Displays information about interfaces.

sip-ua

Enters SIP user-agent configuration mode.

## dial-control-mib

To specify attributes for the call history table, use the dial-control-mib command in global configuration mode. To restore the default maximum size or retention time of the call history table, use
                              the no form of this command.

dial-control-mib { max-size table-entries | retain-timer minutes }

no dial-control-mib { max-size table-entries | retain-timer minutes }

### Syntax Description

max-size table-entries

Maximum number of table entries in the call history table. Range is from 0 to 3000.

Specifying a value of 0 prevents any further entries from being added to the table. Any existing table entries will be preserved
                                                      for the duration specified with the retain-timer keyword.

retain-timer minutes

Duration, in minutes, for entries to remain in the call history table. Range is from 0 to 35791.

Specifying a value of 0 prevents any further table entries from being retained, but does not affect any timer currently in
                                                      effect. Therefore, any existing table entries will remain for the duration previously specified with the retain-timer keyword.

### Command Default

The default call history table length is 500 table entries. The default retain timer is 15 minutes.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

11.3(1)T

This command was introduced on the Cisco 3600 series routers.

12.0(1)XA

This command was first applied to the CDR feature on the Cisco MC3810.

12.0(2)T

The command was integrated into Cisco IOS Release 12.0(2)T.

12.3T

The maximum value for the table-entries argument following the max-size keyword was increased to 1200 entries.

12.3(8)T

The maximum value of the minutes argument following the retain-timer keyword was decreased to 35791 minutes.

## Examples

The following example configures the call history table to hold 400 entries, with each entry remaining in the table for 10
                              minutes:

```
dial-control-mib max-size 400
dial-control-mib retain-timer 10
```

## dial-peer cor custom

To specify that named class of restrictions (COR) apply to dial peers, use the dial-peer cor custom command in global configuration mode.

dial-peer cor custom

### Syntax Description

This command has no arguments or keywords.

### Command Default

No default behavior or keywords.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.1(3)T

This command was introduced.

Cisco IOS XE Bengaluru 17.6.1a

Introduced support for YANG models.

### Usage Guidelines

You must use the dial-peer cor custom command and the name command to define the names of capabilities before you can specify COR rules and apply them to specific dial peers.

Examples of possible names might include the following: call1900, call527, call9, and call911.

You can define a maximum of 64 COR names.

## Examples

The following example defines two COR names:

```
dial-peer cor custom
 name samplegroup32
 name samplegroup12
```

The following example defines Webex Calling COR names:

```
dial-peer cor custom
 name wx-calling_Internal
 name wx-calling_Toll-fre
 name wx-calling_National
 name wx-calling_International
 name wx-calling_Operator_Assistance
 name wx-calling_chargeable_Directory_Assistance
 name wx-calling_Special_Sevices1 
 name wx-calling_Special_Sevices2
 name wx-calling_Premium_Sevices1
 name wx-calling_Premium_Sevices2
```

### Related Commands

Command

Description

name (dial peer cor custom)

Provides a name for a custom COR.

## dpg

### Syntax Description

### Command Default

### Command Modes

## Command History

Release

Modification

### Usage Guidelines

## Examples

### Related Commands

Command

Description

## dial-peer cor list

To define a class of restrictions (COR) list name, use the dial-peer cor list command in global configuration mode. To remove a previously defined COR list name, use the no form of this command.

dial-peer cor list list-name

no dial-peer cor list list-name

### Syntax Description

list-name

List name that is applied to incoming or outgoing calls to specific numbers or exchanges.

### Command Default

No default behavior or keywords.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.1(3)T

This command was introduced.

Cisco IOS XE Bengaluru 17.6.1a

Introduced support for YANG models.

### Usage Guidelines

A COR list defines a capability set that is used in the COR checking between incoming and outgoing dial peers.

## Examples

The following example adds two members to the COR list named list1:

```
dial-peer cor list list1
 member 900block
 member 800call
```

### Related Commands

Command

Description

dial-peer cor custom

Specifies that named COR apply to dial peers.

member (dial peer cor list)

Adds a member to a dial peer COR list.

name (dial peer cor custom)

Provides a name for a custom COR.

## dial-peer data

To create a data dial peer and to enter dial-peer configuration mode, use the dial-peer data command in global configuration mode. To remove a data dial peer, use the no form of this command.

dial-peer data tag pots

no dial-peer data tag

### Syntax Description

tag

Specifies the dial-peer identifying number. Range is from 1 to 2147483647.

pots

Specifies an incoming POTS dial peer.

### Command Default

No default behavior or values

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.2(13)T

This command was introduced.

12.4(4)XC

This command was implemented on the Cisco 2600XM series, Cisco 2800 series, Cisco 3700 series, and Cisco 3800 series.

12.4(9)T

This command was integrated into Cisco IOS Release 12.4(9)T.

### Usage Guidelines

A data dial peer should be defined only for incoming data calls. The incoming called-number and shutdown commands on the data dial peer are allowed. However, the following POTS dial-peer commands are disabled on a data dial peer:

answer-address

carrier-id

destination-pattern

information-type

port

trunk-group-label

## Examples

The following example is a data dial-peer configuration:

```
dial-peer data 100 pots
 incoming called-number 100
```

The following example is a voice dial-peer configuration:

```
dial-peer voice 2001 pots
 destination-pattern 2001
 no digit-strip
 port 3/1:1
```

### Related Commands

Command

Description

dial-peer search

Optimizes voice or data dial-peer searches.

incoming called-number

Specifies an incoming called number of an MMoIP or POTS dial peer.

shutdown (dial peer)

Changes the administrative state of a selected dial peer from up to down.

## dial-peer hunt

To specify a hunt selection order for dial peers, use the dial-peer hunt command in global configuration mode. To restore the default selection order, use the no form of this command.

dial-peer hunt hunt-order-number

no dial-peer hunt

### Syntax Description

hunt-order-number

A number from 0 to 7 that selects a predefined hunting selection order:

0--Longest match in phone number, explicit preference, random selection. This is the default hunt order number.

1--Longest match in phone number, explicit preference, least recent use.

2--Explicit preference, longest match in phone number, random selection.

3--Explicit preference, longest match in phone number, least recent use.

4--Least recent use, longest match in phone number, explicit preference.

5--Least recent use, explicit preference, longest match in phone number.

6--Random selection.

7--Least recent use.

### Command Default

The default is the longest match in the phone number, explicit preference, random selection (hunt order number 0).

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.0(7)XK

This command was introduced on the following platforms: Cisco 2600 series, Cisco 3600 series, Cisco 7200 series, Cisco MC3810,
                                          and Cisco AS5300.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T.

### Usage Guidelines

Use the dial-peer hunt dial peer configuration command if you have configured hunt groups. "Longest match in phone number" refers to the destination
                              pattern that matches the greatest number of the dialed digits. "Explicit preference" refers to the preference command setting in the dial-peer configuration. "Least recent use" refers to the destination pattern that has waited the
                              longest since being selected. "Random selection" weights all of the destination patterns equally in a random selection mode.

This command applies to POTS, VoIP, Voice over Frame Relay (VoFR), Voice over ATM (VoATM), and Multimedia Mail over Internet
                              Protocol (MMOIP) dial peers.

## Examples

The following example configures the dial peers to hunt in the following order: (1) longest match in phone number, (2) explicit
                              preference, (3) random selection.

```
dial-peer hunt 0
```

### Related Commands

Command

Description

destination-pattern

Specifies the prefix or the complete telephone number for a dial peer.

preference

Specifies the preferred selection order of a dial peer within a hunt group.

show dial-peer voice

Displays configuration information for dial peers.

## dial-peer inbound
                        	 selection creation-order

To enable incoming
                              		  dial-peer selection without changing the creation order when sorting the
                              		  longest matched numbers, use dial-peer inbound selection creation-order command. To revert to the default behavior, use the no form of
                              		  this command

dial-peer inbound selection creation-order

no dial-peer inbound selection creation-order

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

The default
                              		  behavior does not guarantee that the creation order would be retained for
                              		  multiple dial-peers with the same number of matched digits due to the unstable
                              		  heap sorting algorithm.

### Command Modes

Global configuration (config)

## Command History

Cisco IOS
                                       					 15.6(1)T

This
                                       					 command was introduced.

## Examples

```
Device(config)# dial-peer inbound selection creation-order
```

## dial-peer inbound selection sip-trunk

To enable incoming SIP line-side calls to use the same dial-peer matching rules as SIP trunk-side calls, use the dial-peer inbound selection sip-trunk command in global configuration mode. To revert to the default behavior, use the no form of this command.

dial-peer inbound selection sip-trunk

no dial-peer inbound selection sip-trunk

### Syntax Description

This command has no arguments or keywords.

### Command Default

Disabled (SIP line-side and SIP trunk-side calls use different dial-peer matching rules).

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.4(11)T2

This command was introduced.

### Usage Guidelines

This command applies the same dial-peer matching rules used for calls from SIP trunks to incoming calls from SIP phones (line
                              side). The first table below shows the rules and the order in which they are applied by default to SIP line-side calls. The
                              second table below shows the rules and the order in which they are applied to SIP trunk-side calls and to SIP line-side calls
                              when the dial-peer inbound selection sip-trunk command is used.

The router compares the dial-peer configuration to the call parameter in its search to match an inbound call to a dial peer.
                              All dial peers are searched based on the first match criteria. The router moves on to the next criteria only if no match is
                              found.

Match Order

Cisco IOS Command

Incoming Call Parameter

1

destination-pattern

Calling number

2

answer-address

Calling number

3

incoming called-number

Called number

4

incoming uri request

Request-URI

5

incoming uri to

To URI

6

incoming uri from

From URI

7

carrier-id source

Carrier-is associated with the call

Match Order

Cisco IOS Command

Incoming Call Parameter

1

incoming uri request

Request-URI

2

incoming uri to

To URI

3

incoming uri from

From URI

4

incoming called-number

Called number

5

answer-address

Calling number

6

destination-pattern

Calling number

7

carrier-id source

Carrier-is associated with the call

## Examples

The following example shows SIP line-side calls use the same matching rules as trunk-side calls:

```
dial-peer inbound selection sip-trunk
```

### Related Commands

Command

Description

answer-address

Specifies calling number to match for a dial peer.

destination-pattern

Specifies telephone number to match for a dial peer.

dial-peer voice

Defines a specific dial peer.

incoming called-number

Incoming called number matched to a dial peer.

incoming uri

Specifies the voice class used to match a VoIP dial peer to the uniform resource identifier (URI) of an incoming call.

show dial-peer voice

Displays configuration information for voice dial peers.

## dial-peer no-match disconnect-cause

To disconnect the incoming ISDN or channel associated signaling (CAS) call when no inbound voice or modem dial peer is matched,
                              use the dial-peer no-match disconnect-cause command in global configuration mode. To restore the default incoming call state (call is forwarded to the dialer), use the no form of this command.

dial-peer no-match disconnect-cause cause-code-number

no dial-peer no-match disconnect-cause cause-code-number

### Syntax Description

cause-code-number

An ISDN cause code number. Range is from 1 to 127.

### Command Default

The call is forwarded to the dialer to handle as a modem call.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.2(13)T

This command was introduced.

### Usage Guidelines

By default, calls are forwarded to the dialer to handle as a modem call when no inbound dial peer is matched. The dial-peer no-match disconnect-cause command changes that behavior to disconnect the incoming ISDN or CAS calls when no inbound voice or modem dial peer is matched.

Refer to the ISDN Cause Values table in the Cisco IOS Debug Command Reference for a list of ISDN cause codes.

## Examples

The following example shows that ISDN cause code 47 has been specified to match inbound voice or modem dial peers:

```
dial-peer no-match disconnect-cause 47
```

### Related Commands

Command

Description

show dial-peer voice

Displays configuration information for dial peers.

## dial-peer outbound status-check pots

To check the status of outbound POTS dial peers during call setup and to disallow, for that call, any dial peer whose status
                              is down, use the dial-peer outbound status-check pots command in privileged EXEC mode. To disable status checking, use the no form of this command.

dial-peer outbound status-check pots

no dial-peer outbound status-check pots

### Syntax Description

This command has no arguments or keywords.

### Command Default

No default behavior or values.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

12.3

This command was introduced.

### Usage Guidelines

Use this command to disallow, during call setup, outbound POTS dial peers (except those for e-phones) whose endpoints (voice
                              ports or trunk groups) are down.

When the dial-peer outbound status-check pots command is configured, if the voice-port configured under an outbound POTS dial-peer is down, that dial-peer is excluded while
                              matching the corresponding destination-pattern. Therefore, if there are no other matching outbound POTS dial-peers for the
                              specified destination-pattern, the gateway will disconnect the call with a cause code of 1 (Unallocated/unassigned number),
                              which is mapped to the "404 Not Found" SIP response by default. When the no form of this command is configured, the outbound POTS dial-peer is matched even if the voice-port configured under is down
                              and the gateway disconnects the call with a cause code of 34 (No circuit/channel available), which is mapped to the "503 Service
                              Unavailable" SIP response by default.

"503 Service Unavailable" was the default behavior before the dial-peer outbound status-check pots command was introduced. Users who need the original behavior should configure the no form of this command.

The table below shows conditions under which an outbound POTS dial peer may be up or down.

If a Dial Peer’s...

And If...

Then the Dial Peer Is...

Operational state is up

Its voice port is up

Up

Its trunk groups and any associated trunks are up

Operational state is down

--

Down

Voice port is down

Trunk groups are down

All associated trunks are down

To show or verify the status (up or down) of all or selected dial peers, use the show dial-peer voice command.

## Examples

The following examples of output for the related show dial-peer voice command show the status of all or selected dial peers. You can use the dial-peer outbound status-check pots command to disallow the outbound POTS dial peers that are down.

The following example shows a short summary status for all dial peers. Outbound status is displayed in the OUT STAT field.
                              POTS dial peers 31 and 42 are shown as down.

```
Router# show dial-peer voice summary dial-peer hunt 0
             AD                                    PRE PASS                OUT
TAG    TYPE  MIN  OPER PREFIX    DEST-PATTERN      FER THRU SESS-TARGET    STAT PORT
444    voip  up   up                                0
22     voip  up   up                                0  syst
12     pots  up   up             5550123 0                      up   4/0:15
311    voip  up   up                                0  syst
31     pots  up   up             5550111            0                      down 4/1:15
421    voip  up   up             5550199 0  syst ipv4:1.8.56.2
42     pots  up   up                                0                      down
```

The following example shows the status for dial peer 12. Outbound status is displayed in the Outbound state field. The dial
                              peer is shown as up.

```
Router# show dial-peer voice 12 VoiceEncapPeer12
        peer type = voice, information type = voice,
        description = `',
        tag = 12, destination-pattern = `5550123',
        answer-address = `', preference=0,
        CLID Restriction = None
        CLID Network Number = `'
        CLID Second Number sent 
        source carrier-id = `', target carrier-id = `',
        source trunk-group-label = `',  target trunk-group-label = `',
        numbering Type = `unknown'
        group = 12, Admin state is up, Operation state is up,
        Outbound state is up,                                  <------- display status
        incoming called-number = `', connections/maximum = 0/unlimited,
        DTMF Relay = disabled,
        huntstop = disabled,
        in bound application associated: 'DEFAULT'
        out bound application associated: ''
        dnis-map = 
        permission :both
        incoming COR list:maximum capability
        outgoing COR list:minimum requirement
        Translation profile (Incoming):
		.
		.
		.
```

The following example shows the status for dial peer 31. Outbound status is displayed in the Outbound state field. The dial
                              peer is listed as down.

```
Router# show dial-peer voice 31 VoiceEncapPeer31
        peer type = voice, information type = voice,
        description = `',
        tag = 31, destination-pattern = `5550111',
        answer-address = `', preference=0,
        CLID Restriction = None
        CLID Network Number = `'
        CLID Second Number sent 
        source carrier-id = `', target carrier-id = `',
        source trunk-group-label = `',  target trunk-group-label = `',
        numbering Type = `unknown'
        group = 31, Admin state is up, Operation state is up,
        Outbound state is down,                            <--------- display status
        incoming called-number = `', connections/maximum = 0/unlimited,
        DTMF Relay = disabled,
        huntstop = disabled,
        in bound application associated: 'DEFAULT'
        out bound application associated: ''
        dnis-map = 
        permission :both
        incoming COR list:maximum capability
        outgoing COR list:minimum requirement
        Translation profile (Incoming):
		.
		.
		.
```

For descriptions of other significant fields shown in these outputs, see the show dial-peer voice command.

### Related Commands

Command

Description

show dial-peer voice

Displays information for voice dial peers.

## dial-peer search type

To optimize voice or data dial-peer searches, use the dial-peer search type command in global configuration mode. To disable the search parameters, use the no form of this command.

dial-peer search type { data voice | data voice | none }

no dial-peer search type

### Syntax Description

data

Searches for data dial peers.

none

Searches for all dial peers by order of input.

voice

Searches for voice dial peers.

### Command Default

data and voice

### Command Modes

Global configuration (confing)

## Command History

Release

Modification

12.2(13)T

This command was introduced.

12.4(4)XC

This command was implemented on the Cisco 2600XM series, Cisco 2800 series, Cisco 3700 series, and Cisco 3800 series.

12.4(9)T

This command was integrated into Cisco IOS Release 12.4(9)T.

### Usage Guidelines

The search defines the search preference explicitly. If the data and voice keywords are specified, data dial peers are searched first. If no data dial peers are found, the voice dial peers are searched.

## Examples

The following is sample output that shows that data dial peers are searched first. Then voice dial peers are searched if no
                              data dial peers can be matched for an incoming call:

```
dial-peer search type data voice
```

The following is sample output that shows that voice dial peers are searched first. Then data dial peers are searched if no
                              voice dial peers can be matched for an incoming call:

```
dial-peer search type voice data
```

### Related Commands

Command

Description

dial-peer data

Enable a gateway to process incoming data calls first by assigning the POTS dial peer as data.

## dial-peer terminator

To change the character used as a terminator for variable-length dialed numbers, use the dial-peer terminator command in global configuration mode. To restore the default terminating character, use the no form of this command.

dial-peer terminator character

no dial-peer terminator

### Syntax Description

character

Designates the terminating character for a variable-length dialed number. Valid numbers and characters are # , * , 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , a , b , c , and d . The default is # .

### Command Default

The default terminating character is #.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.0

This command was introduced.

12.0(7)XK

Usage was restricted to variable-length dialed numbers. The command was implemented on the Cisco 2600 series and Cisco 3600
                                          series, and Cisco MC3810.

12.1(2)T

The command was integrated into Cisco IOS Release 12.1(2)T.

### Usage Guidelines

There are certain areas in the world (for example, in certain European countries) where telephone numbers can vary in length.
                              When a dialed-number string has been identified as a variable length dialed number, the system does not place a call until
                              the configured value for the timeouts interdigit command has expired or until the caller dials the terminating character. Use the dial-peer terminator global configuration command to change the terminating character.

## Examples

The following example shows that "9" has been specified as the terminating character for variable-length dialed numbers:

```
dial-peer terminator 9
```

### Related Commands

Command

Description

answer-address

Specifies the full E.164 telephone number to be used to identify the dial peer of an incoming call.

destination-pattern

Specifies the prefix or the complete telephone number for a dial peer.

timeouts interdigit

Configures the interdigit timeout value for a specified voice port.

show dial-peer voice

Displays configuration information for dial peers.

## dial-peer video

To define a video ATM dial peer for a local or remote video codec, to specify video-related encapsulation, and to enter dial
                              peer configuration mode, use the dial-peer video command in global configuration mode. To remove the video dial peer, use the no form of this command.

dial-peer video tag { videocodec | videoatm }

no dial-peer video tag { videocodec | videoatm }

### Syntax Description

tag

Digits that define a particular dial peer. Defines the dial peer and assigns the protocol type to the peer. Range is from
                                          1 to 10000. The tag must be unique on the router.

videocodec

Specifies a local video codec connected to the router.

videoatm

Specifies a remote video codec on the ATM network.

### Command Default

No video dial peer is configured.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.0(5)XK

This command was introduced for ATM interface configuration on the Cisco MC3810.

12.0(7)T

This command was integrated into Cisco IOS Release 12.0(7)T.

### Usage Guidelines

The tag value must be unique to the device.

## Examples

The following example sets up a local video dial peer designated as 10:

```
dial-peer video 10 videocodec
```

### Related Commands

Command

Description

show dial-peer video

Displays dial-peer video configuration.

## dial-peer voice

To define a particular dial peer, to specify the method of voice encapsulation, and to enter dial peer configuration mode,
                              use the dial-peer voice command in global configuration mode. To delete a defined dial peer, use the no form of this command.

### Cisco 1750 and Cisco 1751 Modular Access Routers

dial-peer voice tag { pots | vofr | voip system }

no dial-peer voice tag { pots | vofr | voip system }

### Cisco 2600 Series, Cisco 2600XM, Cisco 3600 Series, Cisco 3700 Series, Cisco 7204VXR and Cisco 7206VXR

dial-peer voice tag { pots | voatm | vofr | voip system }

no dial-peer voice tag { pots | voatm | vofr | voip system }

### Cisco 7200 Series

dial-peer voice tag vofr

no dial-peer voice tag vofr

### Cisco AS5300

dial-peer voice tag { mmoip | pots | vofr | voip system }

no dial-peer voice tag { mmoip | pots | vofr | voip system }

### Syntax Description

tag

Digits that define a particular dial peer. Range is from 1 to 2147483647.

pots

Indicates that this is a POTS peer that uses VoIP encapsulation on the IP backbone.

vofr

Specifies that this is a Voice over Frame Relay (VoFR) dial peer that uses FRF.11 encapsulation on the Frame Relay backbone
                                          network.

voip

Indicates that this is a VoIP peer that uses voice encapsulation on the POTS network.

system

Indicates that this is a system that uses VoIP.

voatm

Specifies that this is a Voice over ATM (VoATM) dial peer that uses real-time ATM adaptation layer 5 (AAL5) voice encapsulation
                                          on the ATM backbone network.

mmoip

Indicates that this is a multimedia mail peer that uses IP encapsulation on the IP backbone.

### Command Default

No dial peer is defined. No method of voice encapsulation is specified.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

11.3(1)T

This command was introduced on the Cisco 3600 series.

11.3(1)MA

This command was implemented on the Cisco MC3810, with support for the pots , voatm , vofr , and vohdlc keywords.

12.0(3)T

This command was implemented on the Cisco AS5300, with support for the pots and voip keywords.

12.0(3)XG

The vofr keyword was added for the Cisco 2600 series and Cisco 3600 series.

12.0(4)T

The vofr keyword was added for the Cisco 7200 series.

12.0(4)XJ

The mmoip keyword was added for the Cisco AS5300. The dial-peer voice command was implemented for store-and-forward fax.

12.0(7)XK

The voip keyword was added for the Cisco MC3810, and the voatm keyword was added for the Cisco 3600 series. Support for the vohdlc keyword on the Cisco MC3810 was removed.

12.1(1)

The mmoip keyword addition in Cisco IOS Release 12.0(4)XJ was integrated into Cisco IOS Release 12.1(1). The dial-peer voice implementation for store-and-forward fax was integrated into Cisco IOS Release 12.1(1).

12.1(2)T

The keyword changes in Cisco IOS Release 12.0(7)XK were integrated into Cisco IOS Release 12.1(2)T.

12.1(5)T

This command was implemented on the Cisco AS5300 and integrated into Cisco IOS Release 12.1(5)T.

12.2(4)T

This command was implemented on the Cisco 1750.

12.2(2)XN

Support for enhanced Media Gateway Control Protocol (MGCP) voice gateway interoperability was added to Cisco CallManager
                                          Version 3.1 for the Cisco 2600 series, Cisco 3600 series, and Cisco VG200.

12.2(8)T

This command was implemented on the Cisco 1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, and Cisco 3745.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T and Cisco CallManager Version 3.2. This command was implemented
                                          on the Cisco IAD2420 series.

12.2(13)T

This command was integrated into Cisco IOS Release 12.2(13)T and implemented on the Cisco 2600XM, Cisco ICS7750, and Cisco
                                          VG200.

12.4(22)T

Support for IPv6 was added.

Introduced support for YANG models.

### Usage Guidelines

Use the dial-peer voice global configuration command to switch to dial peer configuration mode from global configuration mode and to define a particular
                              dial peer. Use the exit command to exit dial peer configuration mode and return to global configuration mode.

A newly created dial peer remains defined and active until you delete it with the no form of the dial-peer voice command. To disable a dial peer, use the no shutdown command in dial peer configuration mode.

In store-and-forward fax on the Cisco AS5300, the POTS dial peer defines the inbound faxing line characteristics from the
                              sending fax device to the receiving Cisco AS5300 and the outbound line characteristics from the sending Cisco AS5300 to the
                              receiving fax device. The Multimedia Mail over Internet Protocol (MMoIP) dial peer defines the inbound faxing line characteristics
                              from the Cisco AS5300 to the receiving Simple Mail Transfer Protocol (SMTP) mail server. This command works with both on-ramp
                              and off-ramp store-and-forward fax functions.

On the Cisco AS5300, MMoIP is available only if you have modem ISDN channel aggregation (MICA) technologies modems.

## Examples

The following example shows how to access dial peer configuration mode and configure a POTS peer identified as dial peer
                              10 and an MMoIP dial peer identified as dial peer 20:

```
dial-peer voice 10 pots
dial-peer voice 20 mmoip
```

The following example deletes the MMoIP peer identified as dial peer 20:

```
no dial-peer voice 20 mmoip
```

The following example shows how the dial-peer voice command is used to configure the extended echo canceller. In this instance, pots indicates that this is a POTS peer using VoIP encapsulation on the IP backbone, and it uses the unique numeric identifier
                              tag 133001.

```
Router(config)# dial-peer voice 133001 pots
```

### Related Commands

Command

Description

codec (dial-peer)

Specifies the voice coder rate of speech for a VoFR dial peer.

destination-pattern

Specifies the prefix, the full E.164 telephone number, or an ISDN directory number to be used for a dial peer.

dtmf-relay (Voice over Frame Relay)

Enables the generation of FRF.11 Annex A frames for a dial peer.

preference

Indicates the preferred order of a dial peer within a rotary hunt group.

sequence-numbers

Enables the generation of sequence numbers in each frame generated by the DSP for VoFR applications.

session protocol

Establishes a session protocol for calls between the local and remote routers via the packet network.

session target

Specifies a network-specific address for a specified dial peer or destination gatekeeper.

shutdown

Changes the administrative state of the selected dial peer from up to down.

## dial-type

To specify the type of out-dialing for voice port interfaces, use the dial-type command in voice-port configuration mode. To disable the selected type of dialing, use the no form of this command.

dial-type { dtmf | pulse | mf }

no dial-type

### Syntax Description

dtmf

Dual tone multifrequency (DTMF) touch-tone dialing.

pulse

Pulse (rotary) dialing.

mf

Multifrequency tone dialing.

### Command Default

DTMF touch-tone dialing

### Command Modes

Voice-port configuration (config-voiceport)

## Command History

Release

Modification

11.3(1)T

This command was introduced on the Cisco 3600 series.

11.3(1)MA3

This command was implemented on the Cisco MC3810, and the pulse keyword was added.

12.0(7)XK

The mf keyword was added.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T.

12.1(5)XM

This command was extended to the merged SGCP/MGCP software image.

12.2(2)T

This command was implemented on the Cisco 7200 series and integrated into Cisco IOS Release 12.2(2)T.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T and implemented on the Cisco AS5300 and Cisco AS5850.

### Usage Guidelines

Use the dial-type command to specify an out-dialing type for a Foreign Exchange Office (FXO) or E&M voice port interface. This command specifies
                              the tone type for digit detection and out-pulsing. This command is not applicable to Foreign Exchange Station (FXS) voice
                              ports because the ports do not generate out-dialing. This command also specifies the detection direction. Multifrequency tone
                              dialing is not supported for FXS and FXO.

Voice ports can always detect DTMF and pulse signals. This command does not affect voice port dialing detection.

The dial - type command affects out-dialing as configured for the dial peer.

If you are using the dial-type command with E&M wink-start signaling, use the dtmf or mf option.

SGCP 1.1+ does not support pulse dialing.

## Examples

The following example shows a voice port configured to support a rotary (pulse tone) dialer:

```
Router(config)# voice-port 1/1 Router(config-voice-port)# dial-type pulse
```

The following example shows a voice port configured to support a DTMF (touch-tone) dialer:

```
Router(config)# voice-port 1/1 Router(config-voice-port)# dial-type dtmf
```

The following example shows a voice port configured to support a multifrequency tone dialer:

```
Router(config)# voice-port 1/1 Router(config-voice-port)# dial-type mf
```

### Related Commands

Command

Description

sgcp

Starts and allocates resources for the SGCP daemon.

sgcp call-agent

Defines the IP address of the default SGCP call agent.

## dialer extsig

To configure an interface to initiate and terminate calls using an external signaling protocol, use the dialer extsig command in interface configuration mode. To discontinue control of the interface by the external signaling protocol, use
                              the no form of this command.

dialer extsig

no dialer extsig

### Syntax Description

This command has no arguments or keywords.

### Command Default

No default behavior or values

### Command Modes

Interface configuration (config-if)

## Command History

Release

Modification

12.2(2)XB

This command was introduced.

12.2(11)T

The command was integrated into Cisco IOS Release 12.2(11)T and implemented on the Cisco AS5850.

### Usage Guidelines

This command is used with the Network Access Server Package for Media Gateway Control Protocol feature. Configuring the dialer in-band command is a prerequisite to using this command. The configuration is blocked for profile dialers.

## Examples

The following example shows an interface to initiate and terminate calls using an external signaling protocol being configured:

```
Router(config)# interface Dialer1 Router(config-if)# dialer extsig
```

### Related Commands

Command

Description

debug dialer

Provides debugging information for two types of dialer information: dial-on-demand events and dial-on-demand traffic.

dialer in-band

Specifies that DDR is to be supported.

extsig mgcp

Configures external signaling control by MGCP for a T1 or E1 trunk controller card.

show dialer

Displays dialer-related information for DNIS, interface, maps, and sessions.

## dialer preemption level

To set the precedence for voice calls to be preempted by a dial-on demand routing (DDR) call for the dialer map, use the dialer preemption level command in map-class dialer configuration mode. To remove the preemption setting, use the no form of this command.

dialer preemption level { flash-override | flash | immediate | priority | routine }

no dialer preemption level { flash-override | flash | immediate | priority | routine }

### Syntax Description

flash-override

Sets the precedence for DDR calls to preemption level 0 (highest).

flash

Sets the precedence for DDR calls to preemption level 1.

immediate

Sets the precedence for DDR calls to preemption level 2.

priority

Sets the precedence for DDR calls to preemption level 3.

routine

Sets the precedence for DDR calls to preemption level 4 (lowest). This is the default.

### Command Default

The preemption level default is routine (lowest).

### Command Modes

Map-class dialer configuration (config-map-class)

## Command History

Release

Modification

12.4(4)XC

This command was introduced.

12.4(9)T

This command was integrated into Cisco IOS Release 12.4(9)T.

## Examples

The following example sets a preemption level of priority (level 3) for the dialer map-class dial1 .

```
Router(config)# map-class dialer dial1 Router(config-map-class)# dialer preemption level priority
```

### Related Commands

Command

Description

dialer map

Configures a serial interface or ISDN interface to call one or multiple sites or to receive calls from multiple sites.

dialer trunkgroup

Defines the dial-on-demand trunk group label for the dialer interface.

map-class dialer

Defines a class of shared configuration parameters associated with the dialer map command for outgoing calls from an ISDN interface and for PPP callback.

preemption enable

Enables preemption capabilities on a trunk group.

preemption level

Sets the preemption level of the selected outbound dial peer. Voice calls can be preempted by a DDR call with higher preemption
                                          level.

preemption tone timer

Defines the expiry time for the preemption tone for the outgoing call being preempted by a DDR backup call.

## dialer trunkgroup

To define the dial-on-demand trunk group label for the dialer interface, use the dialer trunkgroup command in map-class dialer configuration mode. To remove the trunk group label, use the no form of this command.

dialer trunkgroup label

no dialer trunkgroup label

### Syntax Description

label

Unique name for the dialer interface trunk group. Valid names contain a maximum of 63 alphanumeric characters.

### Command Default

No dialer trunk group is defined.

### Command Modes

Map-class dialer configuration (config-map-class)

## Command History

Release

Modification

12.4(4)XC

This command was introduced.

12.4(9)T

This command was integrated into Cisco IOS Release 12.4(9)T.

## Examples

The following example creates a trunk group named 20 for dialer map-class dial1 .

```
Router(config)# map-class dialer dial1 Router(config-map-class)# dialer trunkgroup 20
```

### Related Commands

Command

Description

dialer map

Configures a serial interface or ISDN interface to call one or multiple sites or to receive calls from multiple sites.

map-class dialer

Defines a class of shared configuration parameters associated with the dialer map command for outgoing calls from an ISDN interface and for PPP callback.

show dialer

Displays general diagnostic information for interfaces configured for dial-on-demand routing (DDR).

trunk group

Defines a trunk group (global configuration) and enters trunk group configuration mode.

## digit

To designate the number of digits for SCCP telephony control (STC) application feature speed-dial codes, use the digit command in STC application feature speed-dial configuration mode. To reset to the default, use the no form of this command.

digit number

no digit

### Syntax Description

number

Number of digits for speed-dial codes. Values are 1 or 2. Default is 1.

### Command Default

The default number of digits is 1.

### Command Modes

STC application feature speed-dial configuration (stcapp-fsd

## Command History

Release

Modification

12.4(6)T

This command was introduced.

### Usage Guidelines

This command is used with the STC application, which enables features on analog FXS endpoints that use Skinny Client Control
                              Protocol (SCCP) for call control.

This command determines the number of digits that can be configured for speed-dial codes using the speed dial and voicemail commands. Use this command only if you want to change the number of digits from its default, which is 1. If you modify the
                              value of this command, the speed dial and voicemail commands are reset to their defaults. If you set the value to 2 and then try to configure a single-digit speed-dial code,
                              the system converts the speed-dial code into two digits.

Note that the phone numbers that are stored with various speed-dial codes are configured on the call-control device, such
                              as Cisco CallManager or a Cisco CallManager Express router.

## Examples

The following example sets the number of digits for speed-dial codes to two. It also sets a speed-dial prefix of one pound
                              sign (#) and a speed-dial code range from 5 to 25. After these values are configured, a phone user presses #10 on the keypad
                              to dial the number that was stored with code 10.

```
Router(config)# stcapp feature speed-dial Router(stcapp-fsd)# prefix # Router(stcapp-fsd)# digit 2 Router(stcapp-fsd)# speed dial from 5 to 25
```

### Related Commands

Command

Description

prefix (stcapp-fsd)

Designates a prefix to precede the dialing of an STC application feature speed-dial code.

show stcapp feature codes

Displays configured and default STC application feature access codes.

speed dial

Designates a range of STC application feature speed dial codes.

voicemail

Designates an STC application feature speed-dial code to dial the voice-mail number.

## digit-strip

To enable digit stripping on a POTS dial-peer call leg, use the digit - strip command in dial peer configuration mode. To disable digit stripping on the dial-peer call leg, use the no form of this command.

digit-strip

no digit-strip

### Syntax Description

This command has no arguments or keywords.

### Command Default

Digit stripping is enabled.

### Command Modes

Dial peer configuration (config-dial-peer)

## Command History

Release

Modification

12.0(7)XR1

This command was introduced for VoIP on the Cisco AS5300.

12.0(7)XK

This command was supported for the following voice technologies on the following platforms:

VoIP--(Cisco 2600 series, Cisco 3600 series, Cisco MC3810)

Voice over Frame Relay (VoFR)--Cisco 2600 series, Cisco 3600 series, Cisco MC3810

Voice over ATM (VoATM)--Cisco 3600 series and Cisco MC3810

12.1(1)T

This command was integrated in Cisco IOS Release 12.1(1)T.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T for the following voice technologies on the following platforms:

VoIP (Cisco MC3810)

VoFR (Cisco 2600 series, Cisco 3600 series, and Cisco MC3810)

VoATM (Cisco 3600 series, Cisco MC3810)

### Usage Guidelines

The digit-strip command is supported on POTS dial peers only.

When a called number is received and matched to a POTS dial peer, the matched digits are stripped and the remaining digits
                              are forwarded to the voice interface.

The table below lists a series of dial peers configured with a specific destination pattern and shows the longest matched
                              number after the digit is stripped based on the dial string 408 555-0148.

Dial Peer

Destination Pattern

Preference

Session Target

Longest Matched Number

4085550148

0 (highest)

100-voip

10

408[0-9]550148

0

200-voip

9

408555

0

300-voip

6

408555

1(lower)

400-voip

6

408%

1

500-voip

3

..........

0

600-voip

0

..........

1

1:D (interface)

0

The table below lists a series of dial peers configured with a specific destination pattern and shows the number after the
                              digit strip based on the dial string 408 555-0148 and the different dial-peer symbols applied.

Dial Peer

Destination Pattern

Number After the Digit Strip

1

408555....

0148

2

408555.%

0148

3

408525.+

0148

4

408555.?

0148

5

408555+

0148

6

408555%

50148

7

408555?

50148

8

408555[0-9].%

30148

9

408555(30).%

30148

10

408555(30)%

30148

11

408555..48

30148

## Examples

The following example disables digit stripping on a POTS dial peer:

```
dial-peer voice 100 pots
 no digit-strip
```

### Related Commands

Command

Description

numbering-type

Specifies number type for the VoIP or POTS dial peer.

rule

Applies a translation rule to a calling party number or a called party number for both incoming and outgoing calls.

show translation-rule

Displays the contents of all the rules that have been configured for a specific translation name.

test translation-rule

Tests the execution of the translation rules on a specific name-tag.

translation-rule

Creates a translation name and enters translation-rule configuration mode.

voip-incoming translation-rule

Captures calls that originate from H.323-compatible clients.

## digital-filter

To specify the digital filter to be used before the voice packet is sent from the digital signal processor (DSP) to the network,
                              use the digital-filter command in voice-class configuration mode. To remove the digital filter, use the no form of this command.

digital-filter { 1950hz | 2175hz }

no digital-filter { 1950hz | 2175hz }

### Syntax Description

1950hz

Filter out 1950 Hz frequency.

2175hz

Filter out 2175 Hz frequency.

### Command Default

Digital filtering is disabled.

### Command Modes

Voice-class configuration (config-voice-class)

## Command History

Release

Modification

12.3(4)XD

This command was introduced.

12.3(7)T

This command was integrated into Cisco IOS Release 12.3(7)T.

### Usage Guidelines

The digital-filter command has an effect on an ear and mouth (E&M) voice port only if the signal type for that port is Land Mobile Radio (LMR).
                              The digital filter improves voice quality by preventing transmission of the guard tone with the voice packet from the LMR
                              system to the VoIP network. The guard tone is configured with the inject guard-tone command. The digital filter can be configured to filter out either 2175 Hz or 1950 Hz. Only one of these frequencies can be
                              filtered out at a time. Filtering is performed by the DSP.

## Examples

The following example specifies that 1950 Hz guard tone be filtered out of the voice packet before it is sent from the DSP
                              to the network:

```
voice class tone-signal mytones
 digital-filter 1950hz
```

### Related Commands

Command

Description

inject guard-tone

Plays out a guard tone with the voice packet.

## direct-inward-dial

To enable the direct inward dialing (DID) call treatment for an incoming called number, use the direct-inward-dial command in dial peer configuration mode. To disable DID on the dial peer, use the no form of this command.

direct-inward-dial

no direct-inward-dial

### Syntax Description

This command has no arguments or keywords.

### Command Default

No default behavior or values.

### Command Modes

Dial peer configuration (config-dial-peer)

## Command History

Release

Modification

11.3(1)NA

This command was introduced.

12.0(4)T

This command was modified for store-and-forward fax.

12.1(5)T

This command was integrated into Cisco IOS Release 12.1(5)T.

12.2(4)T

This command was implemented on the Cisco 1750.

12.2(8)T

This command was implemented on the Cisco 1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, and Cisco 3745.

### Usage Guidelines

Use the direct-inward-dial command to enable the DID call treatment for an incoming called number. When this feature is enabled, the incoming call is
                              treated as if the digits were received from the DID trunk. The called number is used to select the outgoing dial peer. No
                              dial tone is presented to the caller.

Use the no form of this command to disable DID on the dial peer. When the command is disabled, the called number is used to
                              select the outgoing dial peer. The caller is prompted for a called number via dial tone.

This command is applicable only to plain old telephone service (POTS) dial peers for on-ramp store-and-forward fax functions.

## Examples

The following example enables DID call treatment for the incoming called number:

```
dial-peer voice 10 pots
 direct-inward-dial
```

| Note | The documentation set for this product strives to use bias-free language. For purposes of this documentation set, bias-free
                                          is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity,
                                          sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language
                                          that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that
                                          is used by a referenced third-party product. |
|---|---|

| command | One of the auto-config application configuration commands. Valid choices are as follows: retries server shutdown timeout |
|---|---|

| Release | Modification |
|---|---|
| 12.3(8)XY | This command was introduced on the Communication Media Module. |
| 12.3(14)T | This command was integrated into Cisco IOS Release 12.3(14)T. |

| Command | Description |
|---|---|
| auto-config | Enables auto-configuration or enters auto-config application configuration mode for the SCCP application. |
| show auto-config | Displays the current status of auto-config applications. |

| command | One of the MGCP profile commands. Valid choices are as follows: call-agent description (MGCP profile) max1 lookup max1 retries max2 lookup max2 retries package persistent timeout tcrit timeout tdinit timeout tdmax timeout tdmin timeout thist timeout tone busy timeout tone cot1 timeout tone cot2 timeout tone dial timeout tone dial stutter timeout tone mwi timeout tone network congestion timeout tone reorder timeout tone ringback timeout tone ringback connection timeout tone ringing timeout tone ringing distinctive timeout tpar timeout tsmax voice-port (MGCP profile) |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(11)T | This command implemented on the Cisco AS5300 and Cisco AS5850. |

| Command | Description |
|---|---|
| mgcp | Starts and allocates resources for the MGCP daemon. |
| mgcp profile | Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile. |

| command | One of the SIP configuration commands. Valid choices are: bind : Configures the source address of signaling and media packets to a specific interface’s IP address. rel1xx : Enables all SIP provisional responses (other than 100 Trying) to be sent reliably to the remote SIP endpoint. session-transport : Configures the underlying transport layer protocol for SIP messages to TCP or UDP. url : Configures URLs to either the SIP or TEL format for your voip sip calls. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XB | This command was introduced on the Cisco 2600 series, Cisco 3600 series, Cisco 7200 series, Cisco AS5300, Cisco AS5350, and
                                          Cisco AS5400 platforms. |
| 12.2(2)XB2 | This command was implemented on the Cisco AS5850 platform. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T and support was added for the Cisco 3700 series. Cisco AS5300,
                                          Cisco AS5350, Cisco AS5850, and Cisco AS5400 platforms were not supported in this release. |
| 12.2(11)T | Support was added for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 platforms. |
| Cisco IOS XE Release 2.5 | This command was integrated into Cisco IOS XE Release 2.5. |

| Command | Description |
|---|---|
| sip | Enter SIP configuration mode from voice-service VoIP configuration mode. |

| filename | Indicates the file to be retrieved from VFC flash memory and used to boot up the system. |
|---|---|
| slot | Indicates the slot on the Cisco AS5300 in which the VFC is installed. Range is to 2. There is no default value. |

| Release | Modification |
|---|---|
| 11.3(1)NA | This command was introduced on the Cisco AS5300. |
| 12.0(3)T | This command was integrated into Cisco IOS Release 12.0(3)T. |

| Command | Description |
|---|---|
| cap-list vfc | Adds a voice codec overlay file to the capability file list. |
| delete vfc | Deletes a file from VFC flash memory. |

| tx-bits | The bit pattern applies to the transmit signaling bits. |
|---|---|
| rx-bits | The bit pattern applies to the receive signaling bits. |
| seize | The bit pattern defines the seized state. |
| idle | The bit pattern defines the idle state. |
| 0000 through 1111 | Specifies the bit pattern. |

| Release | Modification |
|---|---|
| 11.3(1)MA3 | This command was introduced on the Cisco MC3810. |
| 12.0(7)XK | This command was implemented on the Cisco 2600 series and Cisco 3600 series. |
| 12.1(2)T | The command was integrated into Cisco IOS Release 12.1(2)T. |
| 12.3(4)XD | The LMR signaling type was added to the signaling types to which this command applies. |
| 12.3(7)T | This command was integrated into Cisco IOS Release 12.3(7)T. |
| 12.3(14)T | This command was implemented on the Cisco 2800 series and Cisco 3800 series. |
| 12.4(2)T | This command was integrated into Cisco IOS Release 12.4(2)T. |

| Command | Description |
|---|---|
| condition | Manipulates the signaling bit-pattern for all voice signaling types. |
| ignore | Configures a North American E&M or E&M MELCAS voice port to ignore specific receive bits. |

| filename | Specifies the file in VFC flash memory to be deleted. |
|---|---|
| slot | Specifies the slot on the Cisco AS5300 in which the specified VFC resides. Range is from 0 to 2. |

| Release | Modification |
|---|---|
| 11.3(1)NA | This command was introduced on the Cisco AS5300. |
| 12.0(3)T | This command was integrated into Cisco IOS Release 12.0(3)T. |

| Note | Deleting a file from VFC flash memory does not free the VFC flash memory space that the file occupied. To free VFC flash memory
                                          space, use the erase vfc command. |
|---|---|

| Command | Description |
|---|---|
| default-file vfc | Specifies an additional (or different) file from the ones in the default file list and stored in VFC flash memory. |
| erase vfc | Erases the flash memory of a specified VFC. |
| show vfc directory | Displays the list of all files that reside on this VFC. |

| string | Character string from 1 to 80 characters for DSP interfaces and MGCP profiles, or from 1 to 99 characters for charging profiles. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced on the Cisco 3600 series and Cisco 7200. |
| 11.3(1)MA | This command in voice-port configuration mode was implemented on the Cisco MC3810. |
| 12.0(5)XE | This command in DSP farm interface configuration mode was modified. |
| 12.1(1)T | The DSP farm interface configuration mode modification was integrated into Cisco IOS Release 12.1(1)T. |
| 12.2(2)XA | This command was implemented on the Cisco AS5300. |
| 12.2(11)T | This command was implimented on the Cisco AS5850 and integrated into Cisco IOS Release 12.2(11)T. |
| 12.3(8)XU | This command was introduced in charging profile configuration mode. |
| 12.3(11)YJ | This command in charging profile configuration mode was integrated into Cisco IOS Release 12.3(11)YJ. |
| 12.3(14)YQ | This command in charging profile configuration mode was integrated into Cisco IOS Release 12.3(14)YQ. |
| 12.4(9)T | This was integrated into Cisco IOS Release 12.4(9)T. |
| 12.2(33)SXH | This command was changed to allow the description to contain spaces. |

| Command | Description |
|---|---|
| category | Identifies the subscriber category to which a charging profile applies. |
| cdr suppression | Specifies that CDRs be suppressed as a charging characteristic in a charging profile. |
| charging profile | Associates a default charging profile to an access point. |
| content dcca profile | Defines a DCCA client profile in a GGSN charging profile. |
| content postpaid time | Specifies, as a trigger condition for postpaid users in a charging profile, the time duration limit that when exceeded causes
                                          the GGSN to collect upstream and downstream traffic byte counts and close and update the G-CDR for a particular PDP context. |
| content postpaid validity | Specifies, as a trigger condition in a charging profile, that the amount of time quota granted to a postpaid user is valid. |
| content postpaid volume | Specifies, as a trigger condition for postpaid users in a charging profile, the maximum number of bytes that the GGSN maintains
                                          across all containers for a particular PDP context before closing and updating the G-CDR. |
| content rulebase | Associates a default rule-base ID with a charging profile. |
| gprs charging characteristics reject | Specifies that create PDP context requests for which no charging profile can be selected be rejected by the GGSN. |
| gprs charging container time-trigger | Specifies a global time limit that when exceeded by a PDP context causes the GGSN to close and update the G-CDR for that
                                          particular PDP context. |
| gprs charging profile | Creates a new charging profile (or modifies an existing one) and enters charging profile configuration mode. |
| limit duration | Specifies, as a trigger condition in a charging profile, the time duration limit that when exceeded causes the GGSN to collect
                                          upstream and downstream traffic byte counts and close and update the G-CDR for a particular PDP context. |
| limit sgsn-change | Specifies, as a trigger condition in a charging profile, the maximum number of GGSN changes that can occur before closing
                                          and updating the G-CDR for a particular PDP context. |
| limit volume | Specifies, as a trigger condition in a charging profile, the maximum number of bytes that the GGSN maintains across all containers
                                          for a particular PDP context before closing and updating the G-CDR. |
| mgcp | Starts and allocates resources for the MGCP daemon. |
| mgcp profile | Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile. |
| tariff-time | Specifies that a charging profile use the tariff changes configured using the gprs charging tariff-time global configuration command. |

| description | Description of the CTL file. The maximum length of the description is 100 characters. |
|---|---|

| Release | Modification |
|---|---|
| 15.3(3)M | This command was introduced. |

| string | Text string up to 64 alphanumeric characters. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)T | This command was introduced. |
| Cisco IOS XE Amsterdam 17.2.1r | Introduced support for YANG models. |

| Command | Description |
|---|---|
| dial-peer voice | Defines a dial peer. |
| show dial-peer voice | Displays configuration information for dial peers. |

| text | Character string from 1 to 80 characters. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |

| Command | Description |
|---|---|
| codec (DSP farm profile) | Specifies the codecs supported by a DSP farm profile. |
| dspfarm profile | Enters DSP farm profile configuration mode and defines a profile for DSP farm services. |
| maximum sessions (DSP Farm profile) | Specifies the maximum number of sessions that need to be supported by the profile. |
| shutdown (DSP farm profile) | Allocates DSP farm resources and associates with the application. |

| string | Character string from 1 to 80 characters. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced for the Cisco 7200 series routers. |
| 12.0(5)XE | This command was modified to reduce the maximum number of allowable characters in a text string from 255 to 80. |
| 12.1(1)T | This command was integrated into Cisco IOS Release 12.1(1)T. |

| string | A description specific to the media profile. |
|---|---|

| Release | Modification |
|---|---|
| Cisco IOS XE Bengaluru 17.6.1a | This command was introduced on Cisco Unified Border Element. |

| Command | Description |
|---|---|
| media profile stream-service | Enables stream service on CUBE . |
| connection (media-profile) | Configures idle timeout and call threshold for a media profile. |
| proxy (media-profile) | Configures IP address or hostname of proxy in media profile. |
| source-ip (media-profile) | Configures local source IP address of a WebSocket connection. |
| media class | Applies the media class at the dial peer level. |

| Release | Modification |
|---|---|
| 15.3(3)M | This command was introduced. |

| text | Character string from 1 to 80 characters. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |

| Command | Description |
|---|---|
| associate ccm | Associates a Cisco CallManager with a Cisco CallManager group and establishes its priority within the group. |
| connect retries | Specifies the number of times that a DSP farm attempts to connect to a Cisco CallManager when the current Cisco CallManager
                                          connections fails. |
| sccp ccm group | Creates a Cisco CallManager group and enters SCCP Cisco CallManager configuration mode. |

| string | Trunk group description. Maximum length is 63 alphanumeric characters. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |

| Command | Description |
|---|---|
| trunk group | Initiates the definition of a trunk group. |

| tls-profile-group-label | Allows you to provide a description for the TLS profile
                                          group. |
|---|---|

| Release | Modification |
|---|---|
| Cisco IOS XE Amsterdam 17.3.1a | This command was introduced under voice class configuration
                                          mode. |

| Command | Description |
|---|---|
| voice class tls-profile | Provides sub-options to configure the commands that are required
                                          for a TLS session. |
| crypto signaling | Identifies the trustpoint or the tls-profile tag that is used during the TLS handshake
                                          process. |

| string | Describes a voice source group, Maximum length of the voice source group description is 63 alphanumeric characters. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |

| Command | Description |
|---|---|
| voice source-group | Defines a source group for voice calls. |

| tag | A number that defines a destination E.164 pattern map. The range is from 1 to 10000. |
|---|---|

| Release | Modification |
|---|---|
| 15.2(4)M | This command was introduced. |

| Command | Description |
|---|---|
| destination-pattern | Specifies either the prefix or the full E.164 telephone number to be used for a dial peer |
| e164 | Configures an E.164 entry on a destination E.164 pattern map. |
| show dial-peer voice | Displays configuration information and call statistics for dial peers. |
| url | Specifies the URL of a text file that has E.164 pattern entries configured on a destination E.164 pattern map. |

| tag | Alphanumeric label that uniquely identifies the voice class. This tag must be configured with the voice class uri command. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Match Order | Cisco IOS Command | Outgoing Call Parameter |
|---|---|---|
| 1 | destination uri and carrier-id target | Application-provided URI and target carrier ID associated with the call |
| 2 | destination-pattern and carrier-id target | Called number and target carrier ID associated with the call |
| 3 | destination uri | Application-provided URI |
| 4 | destination-pattern | Called number |
| 5 | carrier-id target | Target carrier ID associated with the call |

| Note | Calls whose destination is an E.164 number, rather than a URI, use the previously existing dial-peer matching rules. For
                                          information, see the Dial Peer Configuration on Voice Gateway Routers document, Cisco IOS Voice Library. |
|---|---|

| Command | Description |
|---|---|
| answer-address | Specifies the calling number to match for a dial peer. |
| debug voice uri | Displays the debugging messages related to URI voice classes. |
| destination-pattern | Specifies the telephone number to match for a dial peer. |
| dial-peer voice | Enters dial peer configuration mode to create or modify a dial peer. |
| incoming uri | Specifies the voice class that a VoIP dial peer uses to match the URI of an incoming call. |
| pattern | Matches a call based on the entire SIP or TEL URI. |
| session protocol | Specifies a session protocol for calls between local and remote routers using the packet network. |
| show dialplan uri | Displays which outbound dial peer is matched for a specific destination URI. |
| voice class uri | Creates or modifies a voice class for matching dial peers to calls containing a SIP or TEL URI. |

| + | (Optional) Character that indicates an E.164 standard number. |
|---|---|
| string | Series of
                                          						digits that specify a pattern for the E.164 or private dialing plan telephone
                                          						number. Valid entries are the digits 0 through 9, the letters A through D, and
                                          						the following special characters: The
                                                							 asterisk (*) and pound sign (#) that appear on standard touch-tone dial pads. Comma
                                                							 (,), which inserts a pause between digits. Period (.), which matches any entered digit (this character is used as a
                                                							 wildcard). Percent sign (%), which indicates that the preceding digit occurred zero or
                                                							 more times; similar to the wildcard usage. Plus
                                                							 sign (+), which indicates that the preceding digit occurred one or more times. Note The
                                                      						  plus sign used as part of a digit string is different from the plus sign that
                                                      						  can be used preceding a digit string to indicate that the string is an E.164
                                                      						  standard number. Circumflex (^), which indicates a match to the beginning of the string. Dollar sign ($), which matches the null string at the end of the input string. Backslash symbol (\), which is followed by a single character, and matches that
                                                							 character. Can be used with a single character with no other significance
                                                							 (matching that character). Question mark (?), which indicates that the preceding digit occurred zero or
                                                							 one time. Brackets ([ ]), which indicate a range. A range is a sequence of characters
                                                							 enclosed in the brackets; only numeric characters from 0 to 9 are allowed in
                                                							 the range. Parentheses (( )), which indicate a pattern and are the same as the regular
                                                							 expression rule. | Note | The
                                                      						  plus sign used as part of a digit string is different from the plus sign that
                                                      						  can be used preceding a digit string to indicate that the string is an E.164
                                                      						  standard number. |
| Note | The
                                                      						  plus sign used as part of a digit string is different from the plus sign that
                                                      						  can be used preceding a digit string to indicate that the string is an E.164
                                                      						  standard number. |
| T | (Optional) Control character that indicates that the destination-pattern value is a variable-length
                                          						dial string. Using this control character enables the router to wait until all
                                          						digits are received before routing the call. |

| Note | The
                                                      						  plus sign used as part of a digit string is different from the plus sign that
                                                      						  can be used preceding a digit string to indicate that the string is an E.164
                                                      						  standard number. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(1)T | This
                                          						command was introduced on the Cisco 3600 series. |
| 11.3(1)MA | This
                                          						command was implemented on the Cisco MC3810. |
| 12.0(4)XJ | This
                                          						command was modified for store-and-forward fax. |
| 12.1(1) | The
                                          						command was integrated into Cisco IOS Release 12.1(1). |
| 12.0(7)XR | This
                                          						command was implemented on the Cisco AS5300 and modified to support the plus
                                          						sign, percent sign, question mark, brackets, and parentheses symbols in the
                                          						dial string. |
| 12.0(7)XK | This
                                          						command was modified. Support for the plus sign, percent sign, question mark,
                                          						brackets, and parentheses in the dial string was added to the Cisco 2600
                                          						series, Cisco 3600 series, and Cisco MC3810. |
| 12.1(1)T | This
                                          						command was integrated into Cisco IOS Release 12.1(1)T and implemented on the
                                          						Cisco 1750, Cisco 7200 series, and Cisco 7500 series. The modifications for the
                                          						Cisco MC3810 in Cisco IOS Release12.0(7)XK are not supported in this release. |
| 12.1(2)T | The
                                          						modifications made in Cisco IOS Release 12.0(7)XK for the Cisco MC3810 were
                                          						integrated into Cisco IOS Release 12.1(2)T. |
| 12.2(8)T | This
                                          						command was implemented on the Cisco 1751, Cisco 2600 series and Cisco 3600
                                          						series, Cisco 3725, and Cisco 3745. |
| 12.2(13)T | This
                                          						command was integrated into Cisco IOS Release 12.2(13)T and implemented on the
                                          						Cisco 2600XM, the Cisco ICS7750, and the Cisco VG200. |
| 12.4(22)T | Support
                                          						for IPv6 was added. |
| Cisco
                                          						IOS XE Release 3.3S | This
                                          						command was integrated into Cisco IOS XE Release 3.3S. |
| 15.2(4)M | This command was modified. With CSCub65380, behavior of dial
                                          						peers with destination-patterns configured with + symbol was rectified. The + symbol is no longer dropped from the dial peers and
                                          						matching occurs as expected |
| Cisco IOS XE Amsterdam 17.2.1r | Introduced support for YANG models. |

| Note | Cisco IOS
                                          			 software does not verify the validity of the E.164 telephone number; it accepts
                                          			 any series of digits as a valid number. |
|---|---|

| Command | Description |
|---|---|
| answer-address | Specifies the full E.164 telephone number to be used to identify the dial peer
                                          						of an incoming call. |
| dial-peer terminator | Designates a special character to be used as a terminator for variable-length
                                          						dialed numbers. |
| incoming called-number (dial peer) | Specifies a digit string that can be matched by an incoming call to associate
                                          						that call with a dial peer. |
| prefix | Specifies the prefix of the dialed digits for a dial peer. |
| timeouts interdigit | Configures the interdigit timeout value for a specified voice port. |

| isdn | Local ISDN directory number assigned by your telephone service provider. |
|---|---|

| Release | Modification |
|---|---|
| 12.0(3)T | This command was introduced on the Cisco 800 series. |

| Command | Description |
|---|---|
| dial-peer voice | Enters dial peer configuration mode, defines the type of dial peer, and defines the tag number associated with a dial peer. |
| no call-waiting | Disables call waiting. |
| port (dial peer) | Enables an interface on a PA-4R-DTR port adapter to operate as a concentrator port. |
| ring | Sets up a distinctive ring for telephones, fax machines, or modems connected to a Cisco 800 series router. |
| show dial-peer voice | Displays configuration information and call statistics for dial peers. |

| tag | The route string tag defined by the route string class. The range is from 1 to 10000. |
|---|---|

| Release | Modification |
|---|---|
| 15.3(3)M | This command was introduced. |
| Cisco IOS XE Release 3.10S | This command was integrated into Cisco IOS XE Release 3.10S. |

| Command | Description |
|---|---|
| voice class route-string | Assigns a unique identifier tag to a route string. |

| channel-number | Channel number from 1 to 24 (T1) or from 1 to 31 (E1). |
|---|---|

| Release | Modification |
|---|---|
| 12.1(1)T | This command was introduced on the Cisco 2600 series and
                                          						Cisco 3600 series. |

| Command | Description |
|---|---|
| loopback remote v54 channel-group | Activates a remote V.54 loopback for the channel group on
                                          						the far end. |

| number | The directory number of the fax machine. |
|---|---|

| Release | Modification |
|---|---|
| Cisco IOS XE Amsterdam 17.2.1r | This command was introduced for Unified Border Element. |

| Command | Description |
|---|---|
| fax-relay (dial peer) | Enables the suppression of call menu (CM) tones or answer (ANS) tones from reaching the Super Group 3 (SG3) fax machines. |

| number | Device ID number as provided by the settlement server. Range is from 0 to 2147483647. |
|---|---|

| Release | Modification |
|---|---|
| 12.0(4)XH1 | This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco AS5300. |
| 12.1(1)T | This command was integrated into Cisco IOS Release 12.1(1)T. |

| Command | Description |
|---|---|
| customer-id | Identifies a carrier or Internet service provider with the settlement provider. |
| settlement | Enters settlement configuration mode. |

| type | Type of interface to be configured. |
|---|---|
| number | Port, connector, or interface card number. Note The number format varies depending on the network module or line card type and the router’s chassis slot it is installed
                                                      in. The numbers are assigned at the factory at the time of installation or when they are added to a system; they can be displayed
                                                      with the show interfaces command. | Note | The number format varies depending on the network module or line card type and the router’s chassis slot it is installed
                                                      in. The numbers are assigned at the factory at the time of installation or when they are added to a system; they can be displayed
                                                      with the show interfaces command. |
| Note | The number format varies depending on the network module or line card type and the router’s chassis slot it is installed
                                                      in. The numbers are assigned at the factory at the time of installation or when they are added to a system; they can be displayed
                                                      with the show interfaces command. |

| Note | The number format varies depending on the network module or line card type and the router’s chassis slot it is installed
                                                      in. The numbers are assigned at the factory at the time of installation or when they are added to a system; they can be displayed
                                                      with the show interfaces command. |
|---|---|

| Release | Modification |
|---|---|
| 12.4(22)YB | This command was introduced. |
| 15.0(1)M | This command was integrated in Cisco IOS Release 15.0(1)M. |

| Keyword | Interface Type |
|---|---|
| ethernet | Ethernet IEEE 802.3 interface. |
| fastethernet | 100-Mbps Ethernet interface. In RITE configuration mode, specifies the outgoing (monitored) interface for exported IP traffic. |
| gigabitethernet | 1000-Mbps Ethernet interface. |
| tengigabitethernet | 10-Gigabit Ethernet interface. |

| Command | Description |
|---|---|
| show interfaces | Displays information about interfaces. |
| sip-ua | Enters SIP user-agent configuration mode. |

| max-size table-entries | Maximum number of table entries in the call history table. Range is from 0 to 3000. Note Specifying a value of 0 prevents any further entries from being added to the table. Any existing table entries will be preserved
                                                      for the duration specified with the retain-timer keyword. | Note | Specifying a value of 0 prevents any further entries from being added to the table. Any existing table entries will be preserved
                                                      for the duration specified with the retain-timer keyword. |
|---|---|---|---|
| Note | Specifying a value of 0 prevents any further entries from being added to the table. Any existing table entries will be preserved
                                                      for the duration specified with the retain-timer keyword. |
| retain-timer minutes | Duration, in minutes, for entries to remain in the call history table. Range is from 0 to 35791. Note Specifying a value of 0 prevents any further table entries from being retained, but does not affect any timer currently in
                                                      effect. Therefore, any existing table entries will remain for the duration previously specified with the retain-timer keyword. | Note | Specifying a value of 0 prevents any further table entries from being retained, but does not affect any timer currently in
                                                      effect. Therefore, any existing table entries will remain for the duration previously specified with the retain-timer keyword. |
| Note | Specifying a value of 0 prevents any further table entries from being retained, but does not affect any timer currently in
                                                      effect. Therefore, any existing table entries will remain for the duration previously specified with the retain-timer keyword. |

| Note | Specifying a value of 0 prevents any further entries from being added to the table. Any existing table entries will be preserved
                                                      for the duration specified with the retain-timer keyword. |
|---|---|

| Note | Specifying a value of 0 prevents any further table entries from being retained, but does not affect any timer currently in
                                                      effect. Therefore, any existing table entries will remain for the duration previously specified with the retain-timer keyword. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced on the Cisco 3600 series routers. |
| 12.0(1)XA | This command was first applied to the CDR feature on the Cisco MC3810. |
| 12.0(2)T | The command was integrated into Cisco IOS Release 12.0(2)T. |
| 12.3T | The maximum value for the table-entries argument following the max-size keyword was increased to 1200 entries. |
| 12.3(8)T | The maximum value of the minutes argument following the retain-timer keyword was decreased to 35791 minutes. |

| Release | Modification |
|---|---|
| 12.1(3)T | This command was introduced. |
| Cisco IOS XE Bengaluru 17.6.1a | Introduced support for YANG models. |

| Note | You can define a maximum of 64 COR names. |
|---|---|

| Command | Description |
|---|---|
| name (dial peer cor custom) | Provides a name for a custom COR. |

|  |  |
|---|---|
|  |  |
|  |  |

| Release | Modification |
|---|---|
|  |  |

| Note |  |
|---|---|

| Command | Description |
|---|---|
|  |  |
|  |  |

| list-name | List name that is applied to incoming or outgoing calls to specific numbers or exchanges. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(3)T | This command was introduced. |
| Cisco IOS XE Bengaluru 17.6.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| dial-peer cor custom | Specifies that named COR apply to dial peers. |
| member (dial peer cor list) | Adds a member to a dial peer COR list. |
| name (dial peer cor custom) | Provides a name for a custom COR. |

| tag | Specifies the dial-peer identifying number. Range is from 1 to 2147483647. |
|---|---|
| pots | Specifies an incoming POTS dial peer. |

| Release | Modification |
|---|---|
| 12.2(13)T | This command was introduced. |
| 12.4(4)XC | This command was implemented on the Cisco 2600XM series, Cisco 2800 series, Cisco 3700 series, and Cisco 3800 series. |
| 12.4(9)T | This command was integrated into Cisco IOS Release 12.4(9)T. |

| Command | Description |
|---|---|
| dial-peer search | Optimizes voice or data dial-peer searches. |
| incoming called-number | Specifies an incoming called number of an MMoIP or POTS dial peer. |
| shutdown (dial peer) | Changes the administrative state of a selected dial peer from up to down. |

| hunt-order-number | A number from 0 to 7 that selects a predefined hunting selection order: 0--Longest match in phone number, explicit preference, random selection. This is the default hunt order number. 1--Longest match in phone number, explicit preference, least recent use. 2--Explicit preference, longest match in phone number, random selection. 3--Explicit preference, longest match in phone number, least recent use. 4--Least recent use, longest match in phone number, explicit preference. 5--Least recent use, explicit preference, longest match in phone number. 6--Random selection. 7--Least recent use. |
|---|---|

| Release | Modification |
|---|---|
| 12.0(7)XK | This command was introduced on the following platforms: Cisco 2600 series, Cisco 3600 series, Cisco 7200 series, Cisco MC3810,
                                          and Cisco AS5300. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T. |

| Command | Description |
|---|---|
| destination-pattern | Specifies the prefix or the complete telephone number for a dial peer. |
| preference | Specifies the preferred selection order of a dial peer within a hunt group. |
| show dial-peer voice | Displays configuration information for dial peers. |

| Release | Modification |
|---|---|
| Cisco IOS
                                       					 15.6(1)T | This
                                       					 command was introduced. |

| Release | Modification |
|---|---|
| 12.4(11)T2 | This command was introduced. |

| Match Order | Cisco IOS Command | Incoming Call Parameter |
|---|---|---|
| 1 | destination-pattern | Calling number |
| 2 | answer-address | Calling number |
| 3 | incoming called-number | Called number |
| 4 | incoming uri request | Request-URI |
| 5 | incoming uri to | To URI |
| 6 | incoming uri from | From URI |
| 7 | carrier-id source | Carrier-is associated with the call |

| Match Order | Cisco IOS Command | Incoming Call Parameter |
|---|---|---|
| 1 | incoming uri request | Request-URI |
| 2 | incoming uri to | To URI |
| 3 | incoming uri from | From URI |
| 4 | incoming called-number | Called number |
| 5 | answer-address | Calling number |
| 6 | destination-pattern | Calling number |
| 7 | carrier-id source | Carrier-is associated with the call |

| Command | Description |
|---|---|
| answer-address | Specifies calling number to match for a dial peer. |
| destination-pattern | Specifies telephone number to match for a dial peer. |
| dial-peer voice | Defines a specific dial peer. |
| incoming called-number | Incoming called number matched to a dial peer. |
| incoming uri | Specifies the voice class used to match a VoIP dial peer to the uniform resource identifier (URI) of an incoming call. |
| show dial-peer voice | Displays configuration information for voice dial peers. |

| cause-code-number | An ISDN cause code number. Range is from 1 to 127. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(13)T | This command was introduced. |

| Command | Description |
|---|---|
| show dial-peer voice | Displays configuration information for dial peers. |

| Release | Modification |
|---|---|
| 12.3 | This command was introduced. |

| Note | "503 Service Unavailable" was the default behavior before the dial-peer outbound status-check pots command was introduced. Users who need the original behavior should configure the no form of this command. |
|---|---|

| If a Dial Peer’s... | And If... | Then the Dial Peer Is... |
|---|---|---|
| Operational state is up | Its voice port is up | Up |
| Its trunk groups and any associated trunks are up |
| Operational state is down | -- | Down |
| Voice port is down |
| Trunk groups are down | All associated trunks are down |

| Command | Description |
|---|---|
| show dial-peer voice | Displays information for voice dial peers. |

| data | Searches for data dial peers. |
|---|---|
| none | Searches for all dial peers by order of input. |
| voice | Searches for voice dial peers. |

| Release | Modification |
|---|---|
| 12.2(13)T | This command was introduced. |
| 12.4(4)XC | This command was implemented on the Cisco 2600XM series, Cisco 2800 series, Cisco 3700 series, and Cisco 3800 series. |
| 12.4(9)T | This command was integrated into Cisco IOS Release 12.4(9)T. |

| Command | Description |
|---|---|
| dial-peer data | Enable a gateway to process incoming data calls first by assigning the POTS dial peer as data. |

| character | Designates the terminating character for a variable-length dialed number. Valid numbers and characters are # , * , 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , a , b , c , and d . The default is # . |
|---|---|

| Release | Modification |
|---|---|
| 12.0 | This command was introduced. |
| 12.0(7)XK | Usage was restricted to variable-length dialed numbers. The command was implemented on the Cisco 2600 series and Cisco 3600
                                          series, and Cisco MC3810. |
| 12.1(2)T | The command was integrated into Cisco IOS Release 12.1(2)T. |

| Command | Description |
|---|---|
| answer-address | Specifies the full E.164 telephone number to be used to identify the dial peer of an incoming call. |
| destination-pattern | Specifies the prefix or the complete telephone number for a dial peer. |
| timeouts interdigit | Configures the interdigit timeout value for a specified voice port. |
| show dial-peer voice | Displays configuration information for dial peers. |

| tag | Digits that define a particular dial peer. Defines the dial peer and assigns the protocol type to the peer. Range is from
                                          1 to 10000. The tag must be unique on the router. |
|---|---|
| videocodec | Specifies a local video codec connected to the router. |
| videoatm | Specifies a remote video codec on the ATM network. |

| Release | Modification |
|---|---|
| 12.0(5)XK | This command was introduced for ATM interface configuration on the Cisco MC3810. |
| 12.0(7)T | This command was integrated into Cisco IOS Release 12.0(7)T. |

| Command | Description |
|---|---|
| show dial-peer video | Displays dial-peer video configuration. |

| tag | Digits that define a particular dial peer. Range is from 1 to 2147483647. |
|---|---|
| pots | Indicates that this is a POTS peer that uses VoIP encapsulation on the IP backbone. |
| vofr | Specifies that this is a Voice over Frame Relay (VoFR) dial peer that uses FRF.11 encapsulation on the Frame Relay backbone
                                          network. |
| voip | Indicates that this is a VoIP peer that uses voice encapsulation on the POTS network. |
| system | Indicates that this is a system that uses VoIP. |
| voatm | Specifies that this is a Voice over ATM (VoATM) dial peer that uses real-time ATM adaptation layer 5 (AAL5) voice encapsulation
                                          on the ATM backbone network. |
| mmoip | Indicates that this is a multimedia mail peer that uses IP encapsulation on the IP backbone. |

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced on the Cisco 3600 series. |
| 11.3(1)MA | This command was implemented on the Cisco MC3810, with support for the pots , voatm , vofr , and vohdlc keywords. |
| 12.0(3)T | This command was implemented on the Cisco AS5300, with support for the pots and voip keywords. |
| 12.0(3)XG | The vofr keyword was added for the Cisco 2600 series and Cisco 3600 series. |
| 12.0(4)T | The vofr keyword was added for the Cisco 7200 series. |
| 12.0(4)XJ | The mmoip keyword was added for the Cisco AS5300. The dial-peer voice command was implemented for store-and-forward fax. |
| 12.0(7)XK | The voip keyword was added for the Cisco MC3810, and the voatm keyword was added for the Cisco 3600 series. Support for the vohdlc keyword on the Cisco MC3810 was removed. |
| 12.1(1) | The mmoip keyword addition in Cisco IOS Release 12.0(4)XJ was integrated into Cisco IOS Release 12.1(1). The dial-peer voice implementation for store-and-forward fax was integrated into Cisco IOS Release 12.1(1). |
| 12.1(2)T | The keyword changes in Cisco IOS Release 12.0(7)XK were integrated into Cisco IOS Release 12.1(2)T. |
| 12.1(5)T | This command was implemented on the Cisco AS5300 and integrated into Cisco IOS Release 12.1(5)T. |
| 12.2(4)T | This command was implemented on the Cisco 1750. |
| 12.2(2)XN | Support for enhanced Media Gateway Control Protocol (MGCP) voice gateway interoperability was added to Cisco CallManager
                                          Version 3.1 for the Cisco 2600 series, Cisco 3600 series, and Cisco VG200. |
| 12.2(8)T | This command was implemented on the Cisco 1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, and Cisco 3745. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T and Cisco CallManager Version 3.2. This command was implemented
                                          on the Cisco IAD2420 series. |
| 12.2(13)T | This command was integrated into Cisco IOS Release 12.2(13)T and implemented on the Cisco 2600XM, Cisco ICS7750, and Cisco
                                          VG200. |
| 12.4(22)T | Support for IPv6 was added. |
| Cisco IOS XE Amsterdam 17.2.1r | Introduced support for YANG models. |

| Note | On the Cisco AS5300, MMoIP is available only if you have modem ISDN channel aggregation (MICA) technologies modems. |
|---|---|

| Command | Description |
|---|---|
| codec (dial-peer) | Specifies the voice coder rate of speech for a VoFR dial peer. |
| destination-pattern | Specifies the prefix, the full E.164 telephone number, or an ISDN directory number to be used for a dial peer. |
| dtmf-relay (Voice over Frame Relay) | Enables the generation of FRF.11 Annex A frames for a dial peer. |
| preference | Indicates the preferred order of a dial peer within a rotary hunt group. |
| sequence-numbers | Enables the generation of sequence numbers in each frame generated by the DSP for VoFR applications. |
| session protocol | Establishes a session protocol for calls between the local and remote routers via the packet network. |
| session target | Specifies a network-specific address for a specified dial peer or destination gatekeeper. |
| shutdown | Changes the administrative state of the selected dial peer from up to down. |

| dtmf | Dual tone multifrequency (DTMF) touch-tone dialing. |
|---|---|
| pulse | Pulse (rotary) dialing. |
| mf | Multifrequency tone dialing. |

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced on the Cisco 3600 series. |
| 11.3(1)MA3 | This command was implemented on the Cisco MC3810, and the pulse keyword was added. |
| 12.0(7)XK | The mf keyword was added. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T. |
| 12.1(5)XM | This command was extended to the merged SGCP/MGCP software image. |
| 12.2(2)T | This command was implemented on the Cisco 7200 series and integrated into Cisco IOS Release 12.2(2)T. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T and implemented on the Cisco AS5300 and Cisco AS5850. |

| Command | Description |
|---|---|
| sgcp | Starts and allocates resources for the SGCP daemon. |
| sgcp call-agent | Defines the IP address of the default SGCP call agent. |

| Release | Modification |
|---|---|
| 12.2(2)XB | This command was introduced. |
| 12.2(11)T | The command was integrated into Cisco IOS Release 12.2(11)T and implemented on the Cisco AS5850. |

| Command | Description |
|---|---|
| debug dialer | Provides debugging information for two types of dialer information: dial-on-demand events and dial-on-demand traffic. |
| dialer in-band | Specifies that DDR is to be supported. |
| extsig mgcp | Configures external signaling control by MGCP for a T1 or E1 trunk controller card. |
| show dialer | Displays dialer-related information for DNIS, interface, maps, and sessions. |

| flash-override | Sets the precedence for DDR calls to preemption level 0 (highest). |
|---|---|
| flash | Sets the precedence for DDR calls to preemption level 1. |
| immediate | Sets the precedence for DDR calls to preemption level 2. |
| priority | Sets the precedence for DDR calls to preemption level 3. |
| routine | Sets the precedence for DDR calls to preemption level 4 (lowest). This is the default. |

| Release | Modification |
|---|---|
| 12.4(4)XC | This command was introduced. |
| 12.4(9)T | This command was integrated into Cisco IOS Release 12.4(9)T. |

| Command | Description |
|---|---|
| dialer map | Configures a serial interface or ISDN interface to call one or multiple sites or to receive calls from multiple sites. |
| dialer trunkgroup | Defines the dial-on-demand trunk group label for the dialer interface. |
| map-class dialer | Defines a class of shared configuration parameters associated with the dialer map command for outgoing calls from an ISDN interface and for PPP callback. |
| preemption enable | Enables preemption capabilities on a trunk group. |
| preemption level | Sets the preemption level of the selected outbound dial peer. Voice calls can be preempted by a DDR call with higher preemption
                                          level. |
| preemption tone timer | Defines the expiry time for the preemption tone for the outgoing call being preempted by a DDR backup call. |

| label | Unique name for the dialer interface trunk group. Valid names contain a maximum of 63 alphanumeric characters. |
|---|---|

| Release | Modification |
|---|---|
| 12.4(4)XC | This command was introduced. |
| 12.4(9)T | This command was integrated into Cisco IOS Release 12.4(9)T. |

| Command | Description |
|---|---|
| dialer map | Configures a serial interface or ISDN interface to call one or multiple sites or to receive calls from multiple sites. |
| map-class dialer | Defines a class of shared configuration parameters associated with the dialer map command for outgoing calls from an ISDN interface and for PPP callback. |
| show dialer | Displays general diagnostic information for interfaces configured for dial-on-demand routing (DDR). |
| trunk group | Defines a trunk group (global configuration) and enters trunk group configuration mode. |

| number | Number of digits for speed-dial codes. Values are 1 or 2. Default is 1. |
|---|---|

| Release | Modification |
|---|---|
| 12.4(6)T | This command was introduced. |

| Command | Description |
|---|---|
| prefix (stcapp-fsd) | Designates a prefix to precede the dialing of an STC application feature speed-dial code. |
| show stcapp feature codes | Displays configured and default STC application feature access codes. |
| speed dial | Designates a range of STC application feature speed dial codes. |
| voicemail | Designates an STC application feature speed-dial code to dial the voice-mail number. |

| Release | Modification |
|---|---|
| 12.0(7)XR1 | This command was introduced for VoIP on the Cisco AS5300. |
| 12.0(7)XK | This command was supported for the following voice technologies on the following platforms: VoIP--(Cisco 2600 series, Cisco 3600 series, Cisco MC3810) Voice over Frame Relay (VoFR)--Cisco 2600 series, Cisco 3600 series, Cisco MC3810 Voice over ATM (VoATM)--Cisco 3600 series and Cisco MC3810 |
| 12.1(1)T | This command was integrated in Cisco IOS Release 12.1(1)T. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T for the following voice technologies on the following platforms: VoIP (Cisco MC3810) VoFR (Cisco 2600 series, Cisco 3600 series, and Cisco MC3810) VoATM (Cisco 3600 series, Cisco MC3810) |

| Dial Peer | Destination Pattern | Preference | Session Target | Longest Matched Number |
|---|---|---|---|---|
|  | 4085550148 | 0 (highest) | 100-voip | 10 |
|  | 408[0-9]550148 | 0 | 200-voip | 9 |
|  | 408555 | 0 | 300-voip | 6 |
|  | 408555 | 1(lower) | 400-voip | 6 |
|  | 408% | 1 | 500-voip | 3 |
|  | .......... | 0 | 600-voip | 0 |
|  | .......... | 1 | 1:D (interface) | 0 |

| Dial Peer | Destination Pattern | Number After the Digit Strip |
|---|---|---|
| 1 | 408555.... | 0148 |
| 2 | 408555.% | 0148 |
| 3 | 408525.+ | 0148 |
| 4 | 408555.? | 0148 |
| 5 | 408555+ | 0148 |
| 6 | 408555% | 50148 |
| 7 | 408555? | 50148 |
| 8 | 408555[0-9].% | 30148 |
| 9 | 408555(30).% | 30148 |
| 10 | 408555(30)% | 30148 |
| 11 | 408555..48 | 30148 |

| Command | Description |
|---|---|
| numbering-type | Specifies number type for the VoIP or POTS dial peer. |
| rule | Applies a translation rule to a calling party number or a called party number for both incoming and outgoing calls. |
| show translation-rule | Displays the contents of all the rules that have been configured for a specific translation name. |
| test translation-rule | Tests the execution of the translation rules on a specific name-tag. |
| translation-rule | Creates a translation name and enters translation-rule configuration mode. |
| voip-incoming translation-rule | Captures calls that originate from H.323-compatible clients. |

| 1950hz | Filter out 1950 Hz frequency. |
|---|---|
| 2175hz | Filter out 2175 Hz frequency. |

| Release | Modification |
|---|---|
| 12.3(4)XD | This command was introduced. |
| 12.3(7)T | This command was integrated into Cisco IOS Release 12.3(7)T. |

| Command | Description |
|---|---|
| inject guard-tone | Plays out a guard tone with the voice packet. |

| Release | Modification |
|---|---|
| 11.3(1)NA | This command was introduced. |
| 12.0(4)T | This command was modified for store-and-forward fax. |
| 12.1(5)T | This command was integrated into Cisco IOS Release 12.1(5)T. |
| 12.2(4)T | This command was implemented on the Cisco 1750. |
| 12.2(8)T | This command was implemented on the Cisco 1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, and Cisco 3745. |