---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-vcr3-vcr3-cr-book-vcr-p2-html-535880a101
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/vcr3/vcr3-cr-book/vcr-p2.html
retrieved_at: 2026-08-16T23:13:52.882006+00:00
---

Cisco IOS Voice Command Reference - K through R

# Cisco IOS Voice Command Reference - K through R

Updated: December 21, 2024

Chapter: periodic-report interval through pulse-digit-detection

## Chapter: periodic-report interval through pulse-digit-detection

# periodic-report interval through pulse-digit-detection

## periodic-report interval

To configure periodic reporting parameters for gateway resource entities, use the periodic-report interval command in voice-class configuration mode. To disable the periodic reporting parameters configuration, use the no form of this command.

periodic-report interval seconds

no periodic-report interval seconds

### Syntax Description

seconds

Periodic interval, in seconds. The range is from 30 to 21600.

### Command Default

The periodic interval report parameters are disabled.

### Command Modes

Voice-class configuration mode (config-class)

## Command History

Release

Modification

15.1(2)T

This command was introduced.

### Usage Guidelines

Use the periodic-report interval command to periodically report the status of the monitoring resources to the external entity. The triggering takes place
                              based on the preconfigured interval value. You can use the statistics collected by this method of reporting to collect information
                              on resource usage.

## Examples

The following example shows how to configure a resource group to trigger reporting every 180 seconds:

```
Router> enable Router# configure terminal Router(config)# voice class resource-group 1 Router(config-class)# periodic-report interval 180
```

### Related Commands

Command

Description

debug rai

Enables debugging for Resource Allocation Indication (RAI).

rai target

Configures the SIP RAI mechanism.

resource (voice)

Configures parameters for monitoring resources, use the resource command in voice-class configuration mode.

show voice class resource-group

Displays the resource group configuration information for a specific resource group or all resource groups.

voice class resource-group

Enters voice-class configuration mode and assigns an identification tag number for a resource group.

## permit hostname (SIP)

To store hostnames
                              		  used during validation of initial incoming INVITE messages, use the permit hostname command in SIP-UA configuration
                              		  mode or voice class tenant configuration mode. To remove a stored hostname, use
                              		  the no form of this
                              		  command.

permit hostname dns: domain-name

no permit hostname

### Syntax Description

dns: domain-name

Domain
                                          						name in DNS format. Domain names can be up to 30 characters in length; domain
                                          						names exceeding 30 characters will be truncated.

### Command Modes

SIP-UA configuration

Voice class tenant configuration (config-class)

## Command History

Release

Modification

12.4(9)T

This
                                          						command was introduced.

15.6(2)T
                                          						and IOS XE Denali 16.3.1

This
                                          						command is now available under voice class tenants.

Cisco IOS XE Dublin
                                                17.10.1a

Introduced support for YANG models.

### Usage Guidelines

The permit hostname command allows you to specify hostnames
                              		  in FQDN (fully qualified domain name) format used during validation of incoming
                              		  initial INVITE messages. The length of the hostname can be up to 30 characters;
                              		  hostnames exceeding 30 characters will be truncated. You can store up to 10
                              		  hostnames by repeating the permit hostname command.

Once configured,
                              		  initial INVITEs with a hostname in the requested Universal Resource Identifier
                              		  (URI) are compared to the configured list of hostnames. If there is a match,
                              		  the INVITE is processed; if there is a mismatch, a "400 Bad Request - Invalid
                              		  Host" is sent, and the call is rejected.

Before Software
                                          			 Release 12.4(9)T, hostnames in incoming INVITE-request messages were only
                                          			 validated when they were in IPv4 format; now you can specify hostnames in fully
                                          			 qualified domain name (FQDN) format.

## Examples

The following
                              		  example show you how to set the hostname to sip.example.com:

```
Router(config)# sip-ua Router(conf-sip-ua)# permit hostname dns:sip.example.com
```

## phone context

To filter out uniform resource identifiers (URIs) that do not contain a phone-context field that matches the configured pattern,
                              use the phone context command in voice URI class configuration mode. To remove the pattern, use the no form of this command.

phone context phone-context-pattern

no phone context

### Syntax Description

phone-context-pattern

Cisco IOS regular expression pattern to match against the phone context field in a SIP or TEL URI. Can be up to 32 characters.

### Command Default

No default behavior or values

### Command Modes

Voice URI class configuration

## Command History

Release

Modification

12.3(4)T

This command was introduced.

### Usage Guidelines

Use this command with at least one other pattern-matching command, such as host , phone number , or user-id ; using it alone does not result in any matches on the voice class.

You cannot use this command if you use the pattern command in the voice class. The pattern command matches on the entire URI, whereas this command matches only a specific field.

## Examples

The following example sets a match on the phone context in the URI voice class:

```
voice class uri 10 tel
 phone number ^408
 phone context 555
```

### Related Commands

Command

Description

destination uri

Specifies the voice class to use for matching the destination URI that is supplied by a voice application.

host

Matches a call based on the host field in a SIP URI.

incoming uri

Specifies the voice class used to match a VoIP dial peer to the URI of an incoming call.

pattern

Matches a call based on the entire SIP or TEL URI.

phone number

Matches a call based on the phone number field in a TEL URI.

show dialplan incall uri

Displays which dial peer is matched for a specific URI in an incoming voice call.

show dialplan uri

Displays which outbound dial peer is matched for a specific destination URI.

user-id

Matches a call based on the user-id field in the SIP URI.

voice class uri

Creates or modifies a voice class for matching dial peers to calls containing a SIP or TEL URI.

## phone number

To match a call based on the phone-number field in a telephone (TEL) uniform resource identifier (URI), use the phone number command in voice URI class configuration mode. To remove the pattern, use the no form of this command.

phone number phone-number-pattern

no phone number

### Syntax Description

phone-number-pattern

Cisco IOS regular expression pattern to match against the phone-number field in a TEL URI. Can be up to 32 characters.

### Command Default

No default behavior or values

### Command Modes

Voice URI class configuration

## Command History

Release

Modification

12.3(4)T

This command was introduced.

### Usage Guidelines

Use this command only in a voice class for TEL URIs.

You cannot use this command if you use the pattern command in the voice class. The pattern command matches on the entire URI, whereas this command matches only a specific field.

## Examples

The following example defines a voice class that matches on the phone number field in a TEL URI:

```
voice class uri r101 tel
 phone number ^408
```

### Related Commands

Command

Description

debug voice uri

Displays debugging messages related to URI voice classes.

destination uri

Specifies the voice class to use for matching the destination URI that is supplied by a voice application.

incoming uri

Specifies the voice class used to match a VoIP dial peer to the URI of an incoming call.

pattern

Matches a call based on the entire SIP or TEL URI.

phone context

Filters out URIs that do not contain a phone-context field that matches the configured pattern.

voice class uri

Creates or modifies a voice class for matching dial peers to calls containing a SIP or TEL URI.

## phone-proxy (dial peer)

To configure the phone proxy for the related dial peer, use the phone-proxy command in dial peer configuration mode. To remove the phone proxy for the related dial peer use the no form of the command.

phone-proxy phone-proxy-name signal-addr ipv4 ipv4-address cucm ipv4 ipv4-address

## Syntax Description

Name of the specific phone proxy.

Specifies the SIP signal IPv4 address of
                                       the access side.

Specifies the call manager server IPv4 address.

### Command Modes

Dial peer configuration (config-dial-peer)

## Command History

15.3(3)M

This command was introduced.

### Usage Guidelines

## Examples

The following example shows how to configure a phone proxy for the related dial peer:

```
Device(config)# dial-peer voice 1 voip
Device(config-dial-peer)# phone-proxy pp signal-addr ipv4 10.0.0.8 cucm ipv4 198.51.100.1
```

## pickup direct

To define a feature code for a Feature Access Code (FAC) to access Pickup Direct on an analog phone, use the pickup direct command in STC application feature access-code configuration mode. To return the code to its default, use the no form of this command.

pickup direct keypad-character

no pickup direct

### Syntax Description

keypad-character

Character string that can be dialed on a telephone keypad (0-9, *, #). Default: 6.

Before Cisco IOS Release 12.4(20)YA, this is a single character. In Cisco IOS Release 12.4(20)YA and later releases, the string
                                          can be any of the following:

A single character (0-9, *, #)

Two digits (00-99)

Two to four characters (0-9, *, #) and the leading or ending character must be an asterisk (*) or number sign (#)

### Command Default

The default value is 6.

### Command Modes

STC application feature access-code configuration (config-stcapp-fac)

## Command History

Release

Modification

12.4(2)T

This command was introduced.

12.4(20)YA

The length of the keypad-character argument was changed to 1 to 4 characters.

12.4(22)T

This command was integrated into Cisco IOS Release 12.4(22)T.

### Usage Guidelines

This command changes the value of the feature code for Pickup Direct from the default (6) to the specified value.

In Cisco IOS Release 12.4(20)YA and later releases, if the length of the keypad-character argument is at least two characters and the leading or ending character of the string is an asterisk (*) or a number sign
                              (#), phone users are not required to dial a prefix to access this feature. Typically, phone users dial a feature access code
                              (FAC) consisting of a prefix plus a feature code, for example **6. If the feature code is 78#, the phone user dials only 78#,
                              without the FAC prefix, to access the corresponding feature.

In Cisco IOS Release 12.4(20)YA and later releases, if you attempt to configure this command with a value that is already
                              configured for another feature code, a speed-dial code, or the Redial FSD, you receive a message. If you configure a duplicate
                              code, the system implements the first matching feature in the order of precedence shown in the output of the show stcapp feature codes command.

In Cisco IOS Release 12.4(20)YA and later releases, if you attempt to configure this command with a value that precludes or
                              is precluded by another FAC, a speed-dial code, or the Redial FSD, you receive a message. If you configure a feature code
                              to a value that precludes or is precluded by another code, the system always executes the call feature with the shortest code
                              and ignores the longer code. For example, #1 will always preclude #12 and #123. You must configure a new value for the precluded
                              code in order to enable phone user access to that feature.

To display a list of all FACs, use the show stcapp feature codes command.

This FAC is not supported by Cisco Unified Communications Manager.

## Examples

The following example shows how to change the value of the feature code for Pickup Direct from the default (6). This configuration
                              also changes the value of the prefix for all FACs from the default (**) to ##. With this configuration, a phone user must
                              press ##3 on the keypad and then the ringing extension number to pick up an incoming call.

```
Router(config)# stcapp feature access-code Router(config-stcapp-fac)# prefix ## Router(config-stcapp-fac)# pickup direct 3 Router(config-stcapp-fac)# exit
```

### Related Commands

Command

Description

pickup group

Defines a feature code for a feature access code (FAC) to Group Call Pickup from another group.

pickup local

Defines a feature code for a feature access code (FAC) to Group Call Pickup from the local group.

prefix (stcapp-fac)

Defines the prefix for feature access codes (FACs).

show stcapp feature codes

Displays all feature access codes (FACs).

stcapp feature access-code

Enables feature access codes (FACs) in STC application and enters STC application feature access-code configuration mode for
                                          changing values of the prefix and features codes from the default.

## pickup group

To define a feature code for a feature access code (FAC) to access Group Call Pickup on an analog phone, use the pickup group command in STC application feature access-code configuration mode. To return the code to its default, use the no form of this command.

pickup group keypad-character

no pickup group

### Syntax Description

keypad-character

Character string that can be dialed on a telephone keypad (0-9, *, #). Default: 4.

Before Cisco IOS Release 12.4(20)YA, this is a single character. In Cisco IOS Release 12.4(20)YA and later releases, the string
                                          can be any of the following:

A single character (0-9, *, #)

Two digits (00-99)

Two to four characters (0-9, *, #) and the leading or ending character must be an asterisk (*) or number sign (#)

### Command Default

The default value is 4.

### Command Modes

STC application feature access-code configuration (config-stcapp-fac)

## Command History

Release

Modification

12.4(2)T

This command was introduced.

12.4(20)YA

The length of the keypad-character argument was changed to 1 to 4 characters.

12.4(22)T

This command was integrated into Cisco IOS Release 12.4(22)T.

### Usage Guidelines

This command changes the value of the feature code for Pickup Direct from the default (4) to the specified value.

In Cisco IOS Release 12.4(20)YA and later releases, if the length of the keypad-character argument is at least two characters and the leading or ending character of the string is an asterisk (*) or a number sign
                              (#), phone users are not required to dial a prefix to access this feature. Typically, phone users dial a special feature access
                              code (FAC) consisting of a prefix plus a feature code, for example **4. If the feature code is 78#, the phone user dials only
                              78#, without the FAC prefix, to access the corresponding feature.

In Cisco IOS Release 12.4(20)YA and later releases, if you attempt to configure this command with a value that is already
                              configured for another feature code, a speed-dial code, or the Redial FSD, you receive a message. If you configure a duplicate
                              code, the system implements the first matching feature in the order of precedence shown in the output of the show stcapp feature codes command.

In Cisco IOS Release 12.4(20)YA and later releases, if you attempt to configure this command with a value that precludes or
                              is precluded by another feature code, a speed-dial code, or the Redial FSD, you receive a message. If you configure a feature
                              code to a value that precludes or is precluded by another code, the system always executes the call feature with the shortest
                              code and ignores the longer code. For example, #1 will always preclude #12 and #123. You must configure a new value for the
                              precluded code in order to enable phone user access to that feature.

To display a list of all FACs, use the show stcapp feature codes command.

## Examples

The following example shows how to change the value of the feature code for Pickup Direct from the default (4). This configuration
                              also changes the value of the prefix for all FACs from the default (**) to ##. After these values are configured, a phone
                              user must press ##3 on the keypad, then the pickup-group number for the ringing extension number to pick up the incoming call.

```
Router(config)# stcapp feature access-code Router(config-stcapp-fac)# prefix ## Router(config-stcapp-fac)# pickup direct 3 Router(config-stcapp-fac)# exit
```

### Related Commands

Command

Description

pickup direct

Defines a feature code for a feature access code (FAC) for Direct Call Pickup of a ringing extension number.

pickup local

Defines a feature code for a feature access code (FAC) for Group Call Pickup to pick up an incoming call from the local group.

prefix (stcapp-fac)

Defines the prefix for feature access codes (FACs).

show stcapp feature codes

Displays all feature access codes (FACs).

stcapp feature access-code

Enables feature access codes (FACs) and enters STC application feature access-code configuration mode for changing values
                                          of the prefix and features codes from the default.

## pickup local

To define a a feature code for a Feature Access Code (FAC) to access Group Call Pickup for a local group on an analog phone,
                              use the pickup local command in STC application feature access-code configuration mode. To return the code to its default, use the no form of this command.

pickup local keypad-character

no pickup local

### Syntax Description

keypad-character

Character string that can be dialed on a telephone keypad. Default: 3.

Before Cisco IOS Release 12.4(20)YA, this is a single character. In Cisco IOS Release 12.5(20)YA and later releases, the string
                                          can be any o the following:

A single character (0-9, *, #)

Two digits (00-99)

Two to four characters (0-9, *, #) and the leading or ending character must be an asterisk (*) or number sign (#)

### Command Default

The default value is 3.

### Command Modes

STC application feature access-code configuration (config-stcapp-fac)

## Command History

Release

Modification

12.4(2)T

This command was introduced.

12.4(20)YA

The length of the keypad-character argument was changed to 1 to 4 characters.

12.4(22)T

This command was integrated into Cisco IOS Release 12.4(22)T.

### Usage Guidelines

This command changes the value of the feature code for Local Group Pickup from the default (3) to the specified value.

In Cisco IOS Release 12.4(20)YA and later releases, if the length of the keypad-character argument is at least two characters and the leading or ending character of the string is an asterisk (*) or a number sign
                              (#), phone users are not required to dial a prefix to access this feature. Typically, phone users dial a special feature access
                              code (FAC) consisting of a prefix plus a feature code, for example **3. If the feature code is 78#, the phone user dials only
                              78#, without the FAC prefix, to access the corresponding feature.

In Cisco IOS Release 12.4(20)YA and later releases, if you attempt to configure this command with a value that is already
                              configured for another feature code or speed-dial code, or for the Redial FSD, you receive a message. If you configure a duplicate
                              code, the system implements the first matching feature in the order of precedence shown in the output of the show stcapp feature codes command.

In Cisco IOS Release 12.4(20)YA and later releases, if you attempt to configure this command with a value that precludes or
                              is precluded by another feature code or speed-dial code, or by the Redial FSD, you receive a message. If you configure a feature
                              code to a value that precludes or is precluded by another code, the system always executes the call feature with the shortest
                              code and ignores the longer code. For example, #1 will always preclude #12 and #123. You must configure a new value for the
                              precluded code in order to enable phone user access to that feature.

To display a list of all FACs, use the show stcapp feature codes command.

## Examples

The following example shows how to change the value of the feature code for Pickup Direct from the default (3). This configuration
                              also changes the value of the prefix for all FACs from the default (**) to ##. With this configuration, a phone user must
                              press ##9 on the keypad to pick up an incoming call in the same group as this extension number.

```
Router(config)# stcapp feature access-code Router(config-stcapp-fac)# prefix ## Router(config-stcapp-fac)# pickup local 9 Router(config-stcapp-fac)# exit
```

### Related Commands

Command

Description

pickup direct

Defines a feature code for a feature access code (FAC) for Direct Call Pickup of a ringing extension number.

pickup group

Defines a feature code for a feature access code (FAC) for Group Call Pickup to pick up an incoming call from another group.

prefix (stcapp-fac)

Defines the prefix for feature access codes (FACs).

show stcapp feature codes

Displays all feature access codes (FACs).

stcapp feature access-code

Enables feature access codes (FACs) in STC application and enters STC application feature access-code configuration mode for
                                          changing values of the prefix and features codes from the default.

## playout-delay (dial peer)

To tune the playout buffer on digital signal processors (DSPs) to accommodate packet jitter caused by switches in the WAN,
                              use the playout - delay command in dial peer configuration mode. To reset the playout buffer to the default, use the no form of this command.

playout-delay { fax milliseconds | maximum milliseconds | minimum { default | low | high } | nominal milliseconds }

no playout-delay { fax | maximum | minimum | nominal }

### Syntax Description

fax milliseconds

Amount of playout delay that the jitter buffer should apply to fax calls, in milliseconds. Range is from 0 to 700. Default
                                          is 300.

maximum milliseconds

(Adaptive mode only) Upper limit of the jitter buffer, or the highest value to which the adaptive delay is set, in milliseconds.

Range is from 40 to 1700, although this value depends on the type of DSP and how the voice card is configured for codec complexity.
                                          (See the codec complexity command.) Default is 200.

If the voice card is configured for high codec complexity, the highest value that can be configured for maximum for compressed codecs is 250 ms. For medium-complexity codec configurations, the highest maximum value is 150 ms.

Voice hardware that does not support the voice card complexity configuration (such as analog voice modules for the Cisco 3600
                                          series router) has an upper limit of 200 ms.

minimum

(Adaptive mode only) Lower limit of the jitter buffer, or the lowest value to which the adaptive delay is set, in milliseconds.
                                          Values are as follows:

default -- 40 ms. Use when there are normal jitter conditions in the network. This is the default.

low -- 10 ms. Use when there are low jitter conditions in the network.

high -- 40 ms. Use when there are high jitter conditions in the network.

nominal milliseconds

Amount of playout delay applied at the beginning of a call by the jitter buffer in the gateway, in milliseconds. In fixed
                                          mode, this is also the maximum size of the jitter buffer throughout the call.

Range is from 0 to 1500, although this value depends on the type of DSP and how the voice card is configured for codec complexity.
                                          Default is 60.

For non-conference calls when you are using DSPware version 4.1.33 or a later version, the following values are allowed.

If the voice card is configured for high codec complexity, the highest value that can be configured for the nominal keyword for compressed codecs is 200 ms.

For medium-complexity codec configurations, the highest nominal value is 150 ms.

nominal milliseconds (continued)

For conference calls when you are using DSPware version 4.1.33 or a later version, the following values are allowed:

The first decoder stream can be assigned a nominal value as high as 200 ms (high-complexity codec) or 150 ms (medium-complexity
                                                codec).

Subsequent decoder streams are limited to the highest nominal value of 150 ms (high-complexity) or 80 ms (medium-complexity).

When the playout-delay mode is configured for fixed operation and setting the expected jitter buffer size with the nominal
                                          value, the minimum effective value for the playout delay will depend on the codec in use and the configured minimum value.

When the playout-delay minimum low is configured the minimum actual jitter buffer size will be 30ms even when setting the nominal to a value lower than 30msec.

When the playout-delay minimum default , the minimum jitter buffer size when running in fixed mode will be 60ms.

When fixed mode is configured, there is a 10msec added to the nominal value when setting the jitter buffer when configured
                                          for G.729 and a 5ms added using G.711

Voice hardware that does not support the voice-card complexity configuration (such as analog voice modules for the Cisco 3600
                                          series router) has an upper limit of 200 ms for the first decoder stream and 150 ms for subsequent decoder streams.

With DSPware versions earlier than 4.1.33, the highest nominal value that can be configured is 150 ms for high-complexity
                                                      codec configurations and analog modules. The highest nominal value for medium-complexity codec configurations is 80 ms.

### Command Default

fax --300 milliseconds maximum --200 milliseconds minimum --default (40 milliseconds) nominal --60 milliseconds

### Command Modes

Dial peer configuration (config-dial-peer)

## Command History

Release

Modification

11.3(1)MA

This command was introduced on the Cisco MC3810.

12.0(7)XK

This command was implemented on the Cisco 2600 series and Cisco 3600 series.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T.

12.1(3)XI

This command was implemented on the Cisco ICS7750.

12.1(5)T

This command was integrated into Cisco IOS Release 12.1(5)T. Support for dial peer configuration mode was added on the following
                                          platforms: Cisco 2600 series, Cisco 3600 series, Cisco 7200 series, Cisco MC3810, Cisco AS5200, Cisco AS5300, Cisco AS5400,
                                          and Cisco AS5800. The minimum keyword was introduced.

12.2(13)T

The fax keyword was introduced.

12.2(13)T8

DSPware version 4.1.33 was implemented.

### Usage Guidelines

Before Cisco IOS Release 12.1(5)T, this command was used in voice-port configuration mode. For Cisco IOS Release 12.1(5)T
                              and later releases, in most cases playout delay should be configured in dial-peer configuration mode on the Voice over IP
                              (VoIP) dial peer that is on the receiving end of the voice traffic that is to be buffered. This dial peer senses network conditions
                              and relays them to the DSPs, which adjust the jitter buffer as necessary. When multiple applications are configured on the
                              gateway, playout delay should be configured in dial-peer configuration mode. When there are numerous dial peers to configure,
                              it might be simpler to configure playout delay on a voice port. If conflicting playout-delay values have been configured on
                              a voice port and on a dial peer, the dial-peer configuration takes precedence.

Playout delay is the amount of time that elapses between the time at which a voice packet is received at the jitter buffer
                              on the DSP and the time at which it is played out to the codec. In most networks with normal jitter conditions, the defaults
                              are adequate and you will not need to configure this command.

In situations in which you want to improve voice quality by reducing jitter or you want to reduce network delay, you can configure
                              playout-delay parameters. The parameters are slightly different for each of the two playout-delay modes, adaptive and fixed
                              (see the playout-delay mode command).

In adaptive mode, the average delay for voice packets varies depending on the amount of interarrival variation that packets
                              have as the call progresses. The jitter buffer grows and shrinks to compensate for jitter and to keep voice packets playing
                              out smoothly, within the maximum and minimum limits that have been configured. The maximum limit establishes the highest value
                              to which the adaptive delay is set. The minimum limit is the low-end threshold for the delay of incoming packets by the adaptive
                              jitter buffer. Algorithms in the DSPs that control the growth and shrinkage of the jitter buffer are weighted toward the improvement
                              of voice quality at the expense of network delay: jitter buffer size increases rapidly in response to spikes in network transmissions
                              and decreases slowly in response to reduced congestion.

In fixed mode, the nominal value is the amount of playout delay applied at the beginning of a call by the jitter buffer in
                              the gateway and is also the maximum size of the jitter buffer throughout the call.

As a general rule, if there is excessive breakup of voice due to jitter with the default playout-delay settings, increase
                              playout delay times. If your network is small and jitter is minimal, decrease playout-delay times for a smaller overall delay.

When there is bursty jitter in the network, voice quality can be degraded even though the jitter buffer is actually adjusting
                              the playout delay correctly. The constant readjustment of playout delay to erratic network conditions causes voice quality
                              problems that are usually alleviated by increasing the minimum playout delay-value in adaptive mode or by increasing the nominal
                              delay for fixed mode.

Use the show call active voice command to display the current delay, as well as high- and low-water marks for delay during a call. Other fields that can
                              help determine the size of a jitter problem are ReceiveDelay, GapFillWith..., LostPackets, EarlyPackets, and LatePackets.
                              The following is sample output from the show call active voice command:

```
VOIP:
 ConnectionId[0xECDE2E7B 0xF46A003F 0x0 0x47070A4]
 IncomingConnectionId[0xECDE2E7B 0xF46A003F 0x0 0x47070A4]
 RemoteIPAddress=192.168.100.101
 RemoteUDPPort=18834
 RoundTripDelay=26 ms
 SelectedQoS=best-effort
 tx_DtmfRelay=inband-voice
 FastConnect=TRUE
 Separate H245 Connection=FALSE
 H245 Tunneling=FALSE
 SessionProtocol=cisco
 SessionTarget=
 OnTimeRvPlayout=417000
 GapFillWithSilence=850 ms
 GapFillWithPrediction=2590 ms
 GapFillWithInterpolation=0 ms
 GapFillWithRedundancy=0 ms
 HiWaterPlayoutDelay=70 ms
 LoWaterPlayoutDelay=29 ms
 ReceiveDelay=39 ms
 LostPackets=0
 EarlyPackets=0
 LatePackets=86
```

## Examples

The following example uses default adaptive mode with a minimum playout delay of 10 ms and a maximum playout delay of 60 ms
                              on VoIP dial peer 80. The size of the jitter buffer is adjusted up and down on the basis of the amount of jitter that the
                              DSP finds, but is never smaller than 10 ms and never larger than 60 ms.

```
dial-peer 80 voip
 playout-delay minimum low
 playout-delay maximum 60
```

### Related Commands

Command

Description

codec complexity

Specifies call density and codec complexity based on the codec standard you are using.

playout-delay (voice-port)

Tunes the playout buffer to accommodate packet jitter caused by switches in the WAN.

playout - delay mode

Selects fixed or adaptive mode for the jitter buffer on DSPs.

show call active voice

Displays active call information for voice calls.

## playout-delay (voice-port)

To tune the playout buffer to accommodate packet jitter caused by switches in the WAN, use the playout - delay command in voice-port configuration mode. To reset the playout buffer to the default, use the no form of this command.

playout-delay { fax | maximum | nominal } milliseconds

no playout-delay { fax | maximum | nominal }

### Syntax Description

fax milliseconds

Amount of playout delay that the jitter buffer should apply to fax calls, in milliseconds. Range is from 0 to 700. Default
                                          is 300.

maximum milliseconds

Delay time that the digital signal processor (DSP) allows before starting to discard voice packets, in milliseconds. Range
                                          is from 40 to 320. Default is 160.

nominal milliseconds

Initial (and minimum allowed) delay time that the DSP inserts before playing out voice packets, in milliseconds. Range is
                                          from 40 to 200. Default is 80.

### Command Default

fax --300 milliseconds maximum --160 milliseconds nominal --80 milliseconds

### Command Modes

Voice-port configuration

## Command History

Release

Modification

11.3(1)MA

This command was introduced on the Cisco MC3810.

12.0(7)XK

This command was implemented on the Cisco 2600 series and Cisco 3600 series.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T.

12.2(13)T

The fax keyword was added.

### Usage Guidelines

If there is excessive breakup of voice due to jitter with the default playout delay settings, increase the delay times. If
                              your network is small and jitter is minimal, decrease the delay times to reduce delay.

Before Cisco IOS Release 12.1(5)T, the playout-delay command was configured in voice-port configuration mode. For Cisco IOS Release 12.1(5)T and later releases, in most cases
                              playout delay should be configured in dial-peer configuration mode on the Voice over IP (VoIP) dial peer that is on the receiving
                              end of the voice traffic that is to be buffered. This dial peer senses network conditions and relays them to the DSPs, which
                              adjust the jitter buffer as necessary. When multiple applications are configured on the gateway, playout delay should be configured
                              in dial-peer configuration mode. When there are numerous dial peers to configure, it might be simpler to configure playout
                              delay on a voice port. If conflicting playout-delay values have been configured on a voice port and on a dial peer, the dial-peer
                              configuration takes precedence.

Playout delay is the amount of time that elapses between the time at which a voice packet is received at the jitter buffer
                              on the DSP and the time at which it is played out to the codec. In most networks with normal jitter conditions, the defaults
                              are adequate and you will not need to configure the playout-delay command.

In situations in which you want to improve voice quality by reducing jitter or you want to reduce network delay, you can configure
                              playout-delay parameters. The parameters are slightly different for each of the two playout-delay modes, adaptive and fixed
                              (see the playout-delay mode command).

In adaptive mode, the average delay for voice packets varies depending on the amount of interarrival variation that packets
                              have as the call progresses. The jitter buffer grows and shrinks to compensate for jitter and to keep voice packets playing
                              out smoothly, within the maximum and minimum limits that have been configured. The maximum limit establishes the highest value
                              to which the adaptive delay will be set. The minimum limit is the low-end threshold for incoming packet delay that is created
                              by the adaptive jitter buffer. Algorithms in the DSPs that control the growth and shrinkage of the jitter buffer are weighted
                              toward the improvement of voice quality at the expense of network delay: jitter buffer size increases rapidly in response
                              to spikes in network transmissions and decreases slowly in response to reduced congestion.

In fixed mode, the nominal value is the amount of playout delay applied at the beginning of a call by the jitter buffer in
                              the gateway and is also the maximum size of the jitter buffer throughout the call.

As a general rule, if there is excessive breakup of voice due to jitter with the default playout-delay settings, increase
                              playout-delay times. If your network is small and jitter is minimal, decrease playout-delay times for a smaller overall delay.

When there is bursty jitter in the network, voice quality can be degraded even though the jitter buffer is actually adjusting
                              the playout delay correctly. The constant readjustment of playout delay to erratic network conditions causes voice quality
                              problems that are usually alleviated by increasing the minimum playout-delay value in adaptive mode or by increasing the nominal
                              delay for fixed mode.

The minimum limit for playout delay is configured using the playout-delay (dial peer) command.

Use the show call active voice command to display the current delay, as well as high- and low-water marks for delay during a call. Other fields that can
                              help determine the size of a jitter problem are GapFillWith..., ReceiveDelay, LostPackets, EarlyPackets, and LatePackets.
                              The following is sample output from the show call active voice command:

```
VOIP:
 ConnectionId[0xECDE2E7B 0xF46A003F 0x0 0x47070A4]
 IncomingConnectionId[0xECDE2E7B 0xF46A003F 0x0 0x47070A4]
 RemoteIPAddress=192.168.100.101
 RemoteUDPPort=18834
 RoundTripDelay=26 ms
 SelectedQoS=best-effort
 tx_DtmfRelay=inband-voice
 FastConnect=TRUE
 Separate H245 Connection=FALSE
 H245 Tunneling=FALSE
 SessionProtocol=cisco
 SessionTarget=
 OnTimeRvPlayout=417000
 GapFillWithSilence=850 ms
 GapFillWithPrediction=2590 ms
 GapFillWithInterpolation=0 ms
 GapFillWithRedundancy=0 ms
 HiWaterPlayoutDelay=70 ms
 LoWaterPlayoutDelay=29 ms
 ReceiveDelay=39 ms
 LostPackets=0
 EarlyPackets=0
 LatePackets=86
```

## Examples

The following example sets nominal playout delay to 80 ms and maximum playout delay to 160 ms on voice port 1/0/0:

```
voice-port 1/0/0
 
playout-delay nominal 80
 playout-delay maximum 160
```

### Related Commands

Command

Description

playout - delay (dial peer)

Tunes the playout buffer on DSPs to accommodate packet jitter caused by switches in the WAN.

playout - delay mode

Selects fixed or adaptive mode for playout delay from the jitter buffer on digital signal processors.

show call active

Shows active call information for voice calls or fax transmissions in progress.

vad

Enables voice activity detection.

## playout-delay mode (dial-peer)

To select fixed or adaptive mode for playout delay from the jitter buffer on digital signal processors (DSPs), use the playout - delay mode command in dial-peer configuration mode. To reset to the default, use the no form of this command.

playout-delay mode { adaptive | fixed }

no playout-delay mode

### Syntax Description

adaptive

Jitter buffer size and amount of playout delay are adjusted during a call, on the basis of current network conditions.

fixed

Jitter buffer size does not adjust during a call; a constant playout delay is added.

### Command Default

Adaptive jitter buffer size

### Command Modes

Dial-peer configuration

## Command History

Release

Modification

12.1(5)T

This command was introduced on the following platforms: Cisco 2600 series, Cisco 3600 series, Cisco MC3810, and Cisco ICS
                                          7750. The no - timestamps keyword was removed.

### Usage Guidelines

Before Cisco IOS Release 12.1(5)T, this command was used only in voice-port configuration mode. For Cisco IOS Release 12.1(5)T
                              and later releases, in most cases playout delay should be configured in dial-peer configuration mode on the VoIP dial peer
                              that is on the receiving end of the voice traffic that is to be buffered. This dial peer senses network conditions and relays
                              them to the DSPs, which adjust the jitter buffer as necessary. When multiple applications are configured on the gateway, playout
                              delay should be configured in dial-peer configuration mode.

Tip

When there are numerous dial peers to configure, it might be simpler to configure playout delay on a voice port. If conflicting
                                          playout delay values have been configured on a voice port and on a dial peer, the dial-peer configuration takes precedence.

In most networks with normal jitter conditions, the default is adequate and you do not need to configure this command.

The default is adaptive mode, in which the average delay for voice packets varies depending on the amount of interarrival
                              variation that packets have as the call progresses. The jitter buffer grows and shrinks to compensate for jitter and to keep
                              voice packets playing out smoothly, within the maximum and minimum limits that have been configured.

Select fixed mode only when you understand your network conditions well, and when you have a network with very poor quality
                              of service (QoS) or when you are interworking with a media server or similar transmission source that tends to create a lot
                              of jitter at the transmission source. In most situations it is better to configure adaptive mode and let the DSP size the
                              jitter buffer according to current conditions.

## Examples

The following example sets adaptive playout-delay mode with a high (80 ms) minimum delay on a VoIP dial peer 80:

```
dial-peer 80 voip
 playout-delay mode adaptive
 playout-delay minimum high
```

### Related Commands

Command

Description

playout - delay

Tunes the jitter buffer on DSPs for playout delay of voice packets.

show call active voice

Displays active call information for voice calls.

## playout-delay mode (voice-port)

To select fixed or adaptive mode for playout delay from the jitter buffer on digital signal processors (DSPs), use the playout - delay mode command in voice port configuration mode. To reset to the default, use the no form of this command.

playout-delay mode { adaptive | fixed }

no playout-delay mode

### Syntax Description

adaptive

Jitter buffer size and amount of playout delay are adjusted during a call, on the basis of current network conditions.

fixed

Jitter buffer size does not adjust during a call; a constant playout delay is added.

### Command Default

Adaptive jitter buffer size

### Command Modes

Voice-port configuration

## Command History

Release

Modification

11.3(1)MA

This command was introduced on the Cisco MC3810.

12.0(7)XK

This command was implemented on the Cisco 2600 and Cisco 3600 series.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T.

12.1(3)XI

This command was implemented on the Cisco ICS 7750. The keyword mode was introduced.

12.1(5)T

This command was integrated into Cisco IOS Release 12.1(5)T and the no - timestamps keyword was removed.

### Usage Guidelines

Before Cisco IOS Release 12.1(5)T, this command was used only in voice-port configuration mode. For Cisco IOS Release 12.1(5)T
                              and later releases, in most cases playout delay should be used in dial-peer configuration mode on the VoIP dial peer that
                              is on the receiving end of the voice traffic that is to be buffered. This dial peer senses network conditions and relays them
                              to the DSPs, which adjust the jitter buffer as necessary. When multiple applications are configured on the gateway, playout
                              delay should be configured in dial-peer configuration mode.

Tip

When there are numerous dial peers to configure, it might be simpler to configure playout delay on a voice port. If conflicting
                                          playout delay values have been configured on a voice port and on a dial peer, the dial-peer configuration takes precedence.

In most networks with normal jitter conditions, the default is adequate and you do not need to configure the playout - delay mode command.

The default is adaptive mode, in which the average delay for voice packets varies depending on the amount of interarrival
                              variation that packets have as the call progresses. The jitter buffer grows and shrinks to compensate for jitter and to keep
                              voice packets playing out smoothly, within the maximum and minimum limits that have been configured.

Select fixed mode only when you understand your network conditions well, and when you have a network with very poor quality
                              of service (QoS) or when you are interworking with a media server or similar transmission source that tends to create a lot
                              of jitter at the transmission source. In most situations it is better to configure adaptive mode and let the DSP size the
                              jitter buffer according to current conditions.

## Examples

The following example sets fixed mode on a Cisco 3640 voice port with a nominal delay of 80 ms.

```
voice-port 1/1/0
 playout-delay mode fixed
 playout-delay nominal 80
```

### Related Commands

Command

Description

playout - delay

Tunes the jitter buffer on DSPs for playout delay of voice packets.

show call active voice

Displays active call information for voice calls.

## police profile

To apply the media bandwidth policing profile to a media class, use the police profile command in media class configuration mode. To disable the configuration, use the no form of this command.

police profile tag

no police profile

### Syntax Description

tag

Media profile police tag. The range is from 1 to 10000.

### Command Default

The media bandwidth policing profile is not applied to a media class.

### Command Modes

Media class configuration (cfg-mediaclass)

## Command History

Release

Modification

15.2(2)T

This command was introduced.

### Usage Guidelines

Applying the media bandwidth policing profile at the dial peer level involves two actions; applying the profile for a media
                              class and then applying the corresponding media class to a dial peer. Use the police profile command to apply the media bandwidth policing profile to a media class.

## Examples

The following example shows how to apply the media bandwidth policing profile to a media class:

```
Router> enable Router# configure terminal Router(config)# media class 1 Router(cfg-mediaclass)# police profile 1
```

### Related Commands

Command

Description

media-class

Applies the media class at the dial peer level.

snmp-server enable traps voice media-policy

Enables SNMP media policy voice traps at the global level.

snmp enable peer-trap media-policy

Enables SNMP media policy voice traps at the dial peer level.

## port (Annex G neighbor BE)

To configure the port number of the neighbor that is used for exchanging Annex G messages, use the port command in Annex G Neighbor BE configuration mode. To remove the port number, use the no form of this command.

port neighbor-port

no port

### Syntax Description

neighbor - port

Port number of the neighbor. This number is used for exchanging Annex G messages. The default port number is 2099.

### Command Default

2099

### Command Modes

Annex G Neighbor BE configuration

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T. Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400
                                          is not included in this release.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T. This command is supported on the Cisco AS5300, Cisco AS5350,
                                          and Cisco AS5400 in this release.

### Usage Guidelines

When cofiguring the no port command the neighbor - port argument is not used.

## Examples

The following example sets a neighbor BE to port number 2010.

```
Router(config-annexg-neigh)# port 2010
```

### Related Commands

Command

Description

advertise (annex g)

Controls the types of descriptors that the BE advertises to its neighbors.

cache

Configures the local BE to cache the descriptors received from its neighbors.

id

Configures the local ID of the neighboring BE.

query - interval

Configures the interval at which the local BE will query the neighboring BE.

## port (dial peer)

To associate a dial peer with a specific voice port, use the port command in dial peer configuration mode. To cancel this association, use the no form of this command.

### Cisco 1750 and Cisco 3700 Series

port slot-number / port

no port slot-number / port

### Cisco 2600 Series, Cisco 3600 Series, and Cisco 7200 Series

port { slot-number / subunit-number / port | slot / port : ds0-group-number }

no port { slot-number / subunit-number / port | slot / port : ds0-group-number }

### Cisco AS5300 and Cisco AS5800

port controller-number :D

no port controller-number :D

### Cisco uBR92x Series

port slot / subunit / port

no port slot / subunit / port

### Cisco 1750 and Cisco 3700 Series

slot - number

Number of the slot in the router in which the voice interface card (VIC) is installed. Valid entries are from 0 to 2, depending
                                          on the slot in which the VIC has been installed.

port

Voice port number. Valid entries are 0 and 1.

slot - number

Number of the slot in the router in which the VIC is installed. Valid entries are from 0 to 3, depending on the slot in which
                                          it has been installed.

subunit - number

Subunit on the VIC in which the voice port is located. Valid entries are 0 and 1.

port

Voice port number. Valid entries are 0 and 1.

slot

Router location in which the voice port adapter is installed. Valid entries are 0 and 3.

port

Voice interface card location. Valid entries are 0 and 3.

ds0 - group - number

The DS0 group number. Each defined DS0 group number is represented on a separate voice port. This allows you to define individual
                                          DS0s on the digital T1/E1 card.

controller - number

The T1 or E1 controller.

:D

Indicates the D channel associated with the ISDN PRI.

slot/subunit/port

The analog voice port. Valid entries for the slot / subunit / port are as follows:

slot -- A router slot in which a voice network module (NM) is installed. Valid entries are router slot numbers for the particular
                                                platform.

subunit -- A VIC in which the voice port is located. Valid entries are 0 and 1. (The VIC fits into the voice network module.)

port-- An analog voice port number. Valid entries are 0 and 1.

### Command Default

No port is configured.

### Command Modes

Dial peer configuration

## Command History

Release

Modification

11.3(1)T

This command was introduced on the Cisco 3600 series.

11.3(3)T

This command was implemented on the Cisco 2600 series.

11.3(1)MA

This command was implemented on the Cisco MC3810.

12.0(3)T

This command was integrated into Cisco IOS Release 12.0(3)T and implemented on the Cisco AS5300.

12.0(4)T

This command was implemented on the Cisco uBR924.

12.0(7)T

This command was implemented on the Cisco AS5800.

12.2(8)T

This command was implemented on the following platforms: Cisco 1751, Cisco 3725, and Cisco 3745.

12.2(13)T

This command was integrated into Cisco IOS Release 12.2(13)T. This command does not support the extended echo canceller (EC)
                                          feature on the Cisco AS5300 or the Cisco AS5800.

12.4(22)T

Support for IPv6 was added.

### Usage Guidelines

This command enables calls that come from a telephony interface to select an incoming dial peer and for calls that come from
                              the VoIP network to match a port with the selected outgoing dial peer.

This command applies only to POTS peers.

This command does not support the extended EC feature on the Cisco AS5300.

## Examples

The following example associates POTS dial peer 10 with voice port 1, which is located on subunit 0 and accessed through
                              port 0:

```
dial-peer voice 10 pots
 port 1/0/0
```

The following example associates POTS dial peer 10 with voice port 0:D:

```
dial-peer voice 10 pots
 port 0:D
```

The following example associates POTS dial peer 10 with voice port 1/0/0:D (T1 card):

```
dial-peer voice 10 pots
 port 1/0/0:D
```

### Related Commands

Command

Description

prefix

Specifies the prefix of the dialed digits for a dial peer.

## port (MGCP profile)

To associate a voice port with the Media Gateway Control Protocol (MGCP) profile that is being configured, use the port command in MGCP profile configuration mode. To disassociate the voice port from the profile, use the no form of this command.

port port-number

no port port-number

### Syntax Description

port - number

Voice port or DS0-group number to be used as an MGCP endpoint associated with an MGCP profile.

### Command Default

No default behavior or values

### Command Modes

MGCP profile configuration

## Command History

Release

Modification

12.2(2)XA

This command was introduced as the voice - port (MGCP profile) command.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T.

12.2(8)T

This command was renamed the port (MGCP profile) command.

### Usage Guidelines

This command is used when values for an MGCP profile are configured.

This command associates a voice port with the MGCP profile that is being defined. To associate multiple voice ports with
                              a profile, repeat this command with different voice port arguments.

This command is not used when the default MGCP profile is configured because the values in the default profile configuration
                              apply to all parameters that have not been otherwise configured for a user-defined MGCP profile.

## Examples

The following example associates an analog voice port with an MGCP profile on a Cisco uBR925 platform:

```
Router(config)# mgcp profile ny110ca Router(config-mgcp-profile)# port 0
```

### Related Commands

Command

Description

mgcp

Starts and allocates resources for the MGCP daemon.

mgcp profile

Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile.

## port (supplementary-service)

To enter the supplementary-service voice-port configuration mode for associating a voice port with STC application supplementary-service
                              features, use the port command in supplementary-service configuration mode. To cancel the association, use the no form of this command.

port port

no port port

### Syntax Description

port

Location of port in Cisco ISR or Cisco VG224 Analog Phone Gateway. Syntax is platform-dependent; type ? to determine.

### Command Default

This command has no default behavior or values.

### Command Modes

Supplementary-service configuration (config-stcapp-suppl-serv)

## Command History

Release

Modification

12.4(20)YA

This command was introduced.

12.4(22)T

This command was integrated into Cisco IOS Release 12.4(22)T.

### Usage Guidelines

This command associates an analog FXS port to STC application supplementary-service features being configured.

## Examples

The following example shows how to enable Hold/Resume on analog endpoints connected to port 2/0 of a Cisco VG224.

```
Router(config)# stcapp supplementary-services Router(config-stcapp-suppl-serv)# port 2/0 Router(config-stcapp-suppl-serv-port)# hold-resume Router(config-stcapp-suppl-serv-port)# end
```

### Related Commands

Command

Description

hold-resume

Enables Hold/Resume in Feature mode on the port being configured.

## port media

To specify the serial interface to which the local video codec is connected for a local video dial peer, use the port media
                              command in video dial-peer configuration mode. To remove any configured locations from the dial peer, use the no form of this command.

port media interface

no port media

### Syntax Description

interface

Serial interface to which the local codec is connected. Valid entries are 0 and 1.

### Command Default

No interface is specified

### Command Modes

Video dial-peer configuration

## Command History

Release

Modification

12.0(5)XK

This command was introduced for ATM video dial-peer configuration on the Cisco MC3810.

12.0(7)T

This command was integrated into Cisco IOS Release 12.0(7)T.

## Examples

The following example specifies serial interface 0 as the specified interface for the codec local video dial peer 10:

```
dial-peer video 10 videocodec
 port media Serial0
```

### Related Commands

Command

Description

port signal

Specifies the slot location of the VDM and the port location of the EIA/TIA-366 interface for signaling.

show dial-peer video

Displays dial-peer configuration.

## port-range

To specify a port range for the TFTP server, use the port-range command in phone-proxy configuration mode. To remove the port-range, use the no form of the command.

port-range min-port max-port

no port-range min-port max-port

## Syntax Description

First port number of the port range.

Last port number of the port range.

### Command Default

No port range is specified.

### Command Modes

Phone-proxy configuration mode (config-pp-pr)

## Command History

15.3(3)M

This command was introduced.

### Usage Guidelines

## Examples

The following example shows how to configure a port range for the TFTP server. The first port number is 30000 and the last
                              port number is 40000:

```
Device(config-pp-pr)# port-range 30000 40000
```

## port signal

To specify the slot location of the video dialing module (VDM) and
                              		  the port location of the EIA/TIA-366 interface for signaling for a local video
                              		  dial peer, use the port signal command in video dial-peer configuration mode.
                              		  To remove any configured locations from the dial peer, use the no form of this command.

port signal slot / port

no port signal

### Syntax Description

slot/

Slot location of the VDM. Valid values are 1 and 2.

port

Port location of the EIA/TIA-366 interface.

### Command Default

No locations are specified

### Command Modes

Video dial-peer configuration

## Command History

Release

Modification

12.0(5)XK

This command was introduced for ATM video dial-peer
                                          						configuration on the Cisco MC3810.

12.0(7)T

This command was integrated into Cisco IOS Release
                                          						12.0(7)T.

## Examples

The following example sets up the VDM and EIA/TIA-366 interface
                              		  locations for the local video dial peer designated as 10:

```
dial-peer video 10 videocodec
 port signal 1/0
```

### Related Commands

Command

Description

port media

Specifies the serial interface to which the local video
                                          						codec is connected.

show dial-peer video

Displays dial-peer configuration.

## pots call-waiting

To enable the local call-waiting feature, use the global configuration pots call - waiting command in global configuration mode. To disable the local call-waiting feature, use the no form of this command.

pots call-waiting { local | remote }

no pots call-waiting { local | remote }

### Syntax Description

local

Enable call waiting on a local basis for the routers.

remote

Rely on the network provider service instead of the router to hold calls.

### Command Default

Remote, in which case the call- holding pattern follows the settings of the service provider rather than those of the router.

### Command Modes

Global configuration

## Command History

Release

Modification

12.1.(2)XF

This command was introduced on the Cisco 800 series.

### Usage Guidelines

To display the call-waiting setting, use the show running-config or show pots status command. The ISDN call waiting service
                              is used if it is available on the ISDN line connected to the router even if local call waiting is configured on the router.
                              That is, if the ISDN line supports call waiting, the local call waiting configuration on the router is ignored.

## Examples

The following example enables local call waiting on a router:

```
pots call-waiting local
```

### Related Commands

Command

Description

call-waiting

Configures call waiting for a specific dial peer.

show pots status

Displays the settings of the physical characteristics and other information on the telephone interfaces of a Cisco 800 series
                                          router.

## pots country

To configure your connected telephones, fax machines, or modems to use country-specific default settings for each physical
                              characteristic, use the pots country command in global configuration mode. To disable the use of country-specific default settings, use the no form of this command.

pots country country

no pots country country

### Syntax Description

country

Country in which your router is located.

### Command Default

A default country is not defined.

### Command Modes

Global configuration

## Command History

Release

Modification

12.0(3)T

This command was introduced on the Cisco 800 series.

### Usage Guidelines

This command applies to the Cisco 800 series routers.

If you need to change a country-specific default setting of a physical characteristic, you can use the associated command
                              listed in the "Related Commands" section. Enter the pots country ? command to get a list of supported countries and the code you must enter to indicate a particular country.

## Examples

The following example specifies that the devices connected to the telephone ports use default settings specific to Germany
                              for the physical characteristics:

```
pots country de
```

### Related Commands

Command

Description

pots dialing - method

Specifies how the Cisco 800 series router collects and sends digits dialed on your connected telephones, fax machines, or
                                          modems.

pots disconnect - supervision

Specifies how a Cisco 800 series router notifies the connected telephones, fax machines, or modems when the calling party
                                          has disconnected.

pots disconnect - time

Specifies the interval in which the disconnect method is applied if telephones, fax machines, or modems connected to a Cisco
                                          800 series router fail to detect that a calling party has disconnected.

pots distinctive - ring - guard - time

Specifies the delay in which a telephone port can be rung after a previous call is disconnected (Cisco 800 series routers).

pots encoding

Specifies the PCM encoding scheme for telephones, fax machines, or modems connected to a Cisco 800 series router.

pots line - type

Specifies the impedance of telephones, fax machines, or modems connected to a Cisco 800 series router.

pots ringing - freq

Specifies the frequency at which telephones, fax machines, or modems connected to a Cisco 800 series router ring.

pots silence - time

Specifies the interval of silence after a calling party disconnects (Cisco 800 series router).

pots tone - source

Specifies the source of dial, ringback, and busy tones for telephones, fax machines, or modems connected to a Cisco 800 series
                                          router.

show pots status

Displays the settings of the telephone port physical characteristics and other information on the telephone interfaces on
                                          a Cisco 800 series router.

## pots dialing-method

To specify how the router collects and sends digits dialed on your connected telephones, fax machines, or modems, use the pots dialing - method command in global configuration mode. To disable the specified dialing method, use the no form of this command.

pots dialing-method { overlap | enblock }

no pots dialing-method { overlap | enblock }

### Syntax Description

overlap

The router sends each digit dialed in a separate message.

enblock

The router collects all digits dialed and sends the digits in one message.

### Command Default

The default depends on the setting of the pots country command. For more information, see the pots country command.

### Command Modes

Global configuration

## Command History

Release

Modification

12.0(3)T

This command was introduced on the Cisco 800 series.

### Usage Guidelines

This command applies to Cisco 800 series routers.

To interrupt the collection and transmission of dialed digits, enter a pound sign (#), or stop dialing digits until the interdigit
                              timer runs out (10 seconds).

## Examples

The following example specifies that the router uses the enblock dialing method:

```
pots dialing-method enblock
```

### Related Commands

Command

Description

pots country

Configures telephones, fax machines, or modems connected to a Cisco 800 series router to use country-specific default settings
                                          for each physical characteristic.

pots disconnect - supervision

Specifies how a Cisco 800 series router notifies the connected telephones, fax machines, or modems when the calling party
                                          has disconnected.

pots disconnect - time

Specifies the interval in which the disconnect method is applied if telephones, fax machines, or modems connected to a Cisco
                                          800 series router fail to detect that a calling party has disconnected.

pots distinctive - ring - guard - time

Specifies the delay in which a telephone port can be rung after a previous call is disconnected (Cisco 800 series routers).

pots encoding

Specifies the PCM encoding scheme for telephones, fax machines, or modems connected to a Cisco 800 series router.

pots line - type

Specifies the impedance of telephones, fax machines, or modems connected to a Cisco 800 series router.

pots ringing - freq

Specifies the frequency at which telephones, fax machines, or modems connected to a Cisco 800 series router ring.

pots silence - time

Specifies the interval of silence after a calling party disconnects (Cisco 800 series router).

pots tone - source

Specifies the source of dial, ringback, and busy tones for telephones, fax machines, or modems connected to a Cisco 800 series
                                          router.

show pots status

Displays the settings of the telephone port physical characteristics and other information on the telephone interfaces on
                                          a Cisco 800 series router.

## pots disconnect-supervision

To specify how a router notifies the connected telephones, fax machines, or modems when the calling party has disconnected,
                              use the pots disconnect - supervision command in global configuration mode. To disable the specified disconnect method, use the no form of this command.

pots disconnect-supervision { osi | reversal }

no pots disconnect-supervision { osi | reversal }

### Syntax Description

osi

Open switching interval (OSI) is the duration for which DC voltage applied between tip and ring conductors of a telephone
                                          port is removed.

reversal

Polarity reversal of tip and ring conductors of a telephone port.

### Command Default

The default depends on the setting of the pots country command. For more information, see the pots country command.

### Command Modes

Global configuration

## Command History

Release

Modification

12.0(3)T

This command was introduced on the Cisco 800 series.

### Usage Guidelines

This command applies to Cisco 800 series routers.

Most countries except Japan typically use the osi option. Japan typically uses the reversal option.

## Examples

The following example specifies that the router uses the OSI disconnect method:

```
pots disconnect-supervision osi
```

### Related Commands

Command

Description

pots country

Configures telephones, fax machines, or modems connected to a Cisco 800 series router to use country-specific default settings
                                          for each physical characteristic.

pots dialing - method

Specifies how the Cisco 800 series router collects and sends digits dialed on your connected telephones, fax machines, or
                                          modems.

pots disconnect - time

Specifies the interval in which the disconnect method is applied if telephones, fax machines, or modems connected to a Cisco
                                          800 series router fail to detect that a calling party has disconnected.

pots distinctive - ring - guard - time

Specifies the delay in which a telephone port can be rung after a previous call is disconnected (Cisco 800 series routers).

pots encoding

Specifies the PCM encoding scheme for telephones, fax machines, or modems connected to a Cisco 800 series router.

pots line - type

Specifies the impedance of telephones, fax machines, or modems connected to a Cisco 800 series router.

pots ringing - freq

Specifies the frequency at which telephones, fax machines, or modems connected to a Cisco 800 series router ring.

pots silence - time

Specifies the interval of silence after a calling party disconnects (Cisco 800 series router).

pots tone - source

Specifies the source of dial, ringback, and busy tones for telephones, fax machines, or modems connected to a Cisco 800 series
                                          router.

show pots status

Displays the settings of the telephone port physical characteristics and other information on the telephone interfaces on
                                          a Cisco 800 series router.

## pots disconnect-time

To specify the interval in which the disconnect method is applied if your connected telephones, fax machines, or modems fail
                              to detect that a calling party has disconnected, use the pots disconnect - time command in global configuration mode. To disable the specified disconnect interval, use the no form of this command.

pots disconnect-time interval

no pots disconnect-time interval

### Syntax Description

interval

Interval, in milliseconds. Range is from 50 to 2000.

### Command Default

The default depends on the setting of the pots country command. For more information, see the pots country command.

### Command Modes

Global configuration

## Command History

Release

Modification

12.0(3)T

This command was introduced on the Cisco 800 series.

### Usage Guidelines

This command applies to Cisco 800 series routers.

The pots disconnect - supervision command configures the disconnect method.

## Examples

The following example specifies that the connected devices apply the configured disconnect method for 100 ms after a calling
                              party disconnects:

```
pots disconnect-time 100
```

### Related Commands

Command

Description

pots country

Configures telephones, fax machines, or modems connected to a Cisco 800 series router to use country-specific default settings
                                          for each physical characteristic.

pots dialing - method

Specifies how the Cisco 800 series router collects and sends digits dialed on your connected telephones, fax machines, or
                                          modems.

pots disconnect - supervision

Specifies how a Cisco 800 series router notifies the connected telephones, fax machines, or modems when the calling party
                                          has disconnected.

pots distinctive - ring - guard - time

Specifies the delay in which a telephone port can be rung after a previous call is disconnected (Cisco 800 series routers).

pots encoding

Specifies the PCM encoding scheme for telephones, fax machines, or modems connected to a Cisco 800 series router.

pots line - type

Specifies the impedance of telephones, fax machines, or modems connected to a Cisco 800 series router.

pots ringing - freq

Specifies the frequency at which telephones, fax machines, or modems connected to a Cisco 800 series router ring.

pots silence - time

Specifies the interval of silence after a calling party disconnects (Cisco 800 series router).

pots tone - source

Specifies the source of dial, ringback, and busy tones for telephones, fax machines, or modems connected to a Cisco 800 series
                                          router.

show pots status

Displays the settings of the telephone port physical characteristics and other information on the telephone interfaces on
                                          a Cisco 800 series router.

## pots distinctive-ring-guard-time

To specify the delay in which a telephone port can be rung after a previous call is disconnected, use the pots distinctive - ring - guard - time command in global configuration mode. To disable the specified delay, use the no form of this command.

pots distinctive-ring-guard-time milliseconds

no pots distinctive-ring-guard-time milliseconds

### Syntax Description

milliseconds

Delay, in milliseconds. Range is from 0 to 1000.

### Command Default

The default depends on the setting of the pots country command. For more information, see the pots country command.

### Command Modes

Global configuration

## Command History

Release

Modification

12.0(3)T

This command was introduced on the Cisco 800 series.

### Usage Guidelines

This command applies to Cisco 800 series routers.

## Examples

The following example specifies that a telephone port can be rung 100 ms after a previous call is disconnected:

```
pots distinctive-ring-guard-time 100
```

### Related Commands

Command

Description

pots country

Configures telephones, fax machines, or modems connected to a Cisco 800 series router to use country-specific default settings
                                          for each physical characteristic.

pots dialing - method

Specifies how the Cisco 800 series router collects and sends digits dialed on your connected telephones, fax machines, or
                                          modems.

pots disconnect - supervision

Specifies how a Cisco 800 series router notifies the connected telephones, fax machines, or modems when the calling party
                                          has disconnected.

pots disconnect - time

Specifies the interval in which the disconnect method is applied if telephones, fax machines, or modems connected to a Cisco
                                          800 series router fail to detect that a calling party has disconnected.

pots encoding

Specifies the PCM encoding scheme for telephones, fax machines, or modems connected to a Cisco 800 series router.

pots line - type

Specifies the impedance of telephones, fax machines, or modems connected to a Cisco 800 series router.

pots ringing - freq

Specifies the frequency at which telephones, fax machines, or modems connected to a Cisco 800 series router ring.

pots silence - time

Specifies the interval of silence after a calling party disconnects (Cisco 800 series router).

pots tone - source

Specifies the source of dial, ringback, and busy tones for telephones, fax machines, or modems connected to a Cisco 800 series
                                          router.

ring

Sets up a distinctive ring for telephones, fax machines, or modems connected to a Cisco 800 series router.

show pots status

Displays the settings of the telephone port physical characteristics and other information on the telephone interfaces on
                                          a Cisco 800 series router.

## pots encoding

To specify the pulse code modulation (PCM) encoding scheme for your connected telephones, fax machines, or modems, use the pots encoding command in global configuration mode. To disable the specified scheme, use the no form of this command.

pots encoding { alaw | ulaw }

no pots encoding { alaw | ulaw }

### Syntax Description

alaw

A-law. International Telecommunication Union Telecommunication Standardization Section (ITU-T) PCM encoding scheme used to
                                          represent analog voice samples as digital values.

ulaw

Mu-law. North American PCM encoding scheme used to represent analog voice samples as digital values.

### Command Default

The default depends on the setting of the pots country command. For more information, see the pots country command.

### Command Modes

Global configuration

## Command History

Release

Modification

12.0(3)T

This command was introduced on the Cisco 800 series.

### Usage Guidelines

This command applies to Cisco 800 series routers.

Europe typically uses a-law. North America typically uses u-law.

## Examples

The following example specifies a-law as the PCM encoding scheme:

```
pots encoding alaw
```

### Related Commands

Command

Description

pots country

Configures telephones, fax machines, or modems connected to a Cisco 800 series router to use country-specific default settings
                                          for each physical characteristic.

pots dialing - method

Specifies how the Cisco 800 series router collects and sends digits dialed on your connected telephones, fax machines, or
                                          modems.

pots disconnect - supervision

Specifies how a Cisco 800 series router notifies the connected telephones, fax machines, or modems when the calling party
                                          has disconnected.

pots disconnect - time

Specifies the interval in which the disconnect method is applied if telephones, fax machines, or modems connected to a Cisco
                                          800 series router fail to detect that a calling party has disconnected.

pots distinctive - ring - guard - time

Specifies the delay in which a telephone port can be rung after a previous call is disconnected (Cisco 800 series routers).

pots line - type

Specifies the impedance of telephones, fax machines, or modems connected to a Cisco 800 series router.

pots ringing - freq

Specifies the frequency at which telephones, fax machines, or modems connected to a Cisco 800 series router ring.

pots silence - time

Specifies the interval of silence after a calling party disconnects (Cisco 800 series router).

pots tone - source

Specifies the source of dial, ringback, and busy tones for telephones, fax machines, or modems connected to a Cisco 800 series
                                          router.

show pots status

Displays the settings of the telephone port physical characteristics and other information on the telephone interfaces on
                                          a Cisco 800 series router.

## pots forwarding-method

To configure the type of call-forwarding method to be used for Euro-ISDN (formerly NET3) switches, use the pots forwarding - method command in global configuration mode. To turn forwarding off, use the no form of this command.

pots forwarding-method { keypad | functional }

no pots forwarding-method { keypad | functional }

### Syntax Description

keypad

Gives forwarding control to the Euro-ISDN switch.

functional

Gives forwarding control to the router. If you select this method, use the dual-tone multifrequency (DTMF) keypad commands
                                          listed in the table below to configure call-forwarding service.

### Command Default

Forwarding is off

### Command Modes

Global configuration

## Command History

Release

Modification

12.2(2)T

This command was introduced.

### Usage Guidelines

Use this command to select the type of forwarding method to be used for Euro-ISDN switches. This command does not affect
                              any other switch types.

You can select one or more call-forwarding services at a time, but keep the following Euro-ISDN switch characteristics in
                              mind:

Call forward unconditional (CFU) redirects a call without restriction and takes precedence over other call-forwarding service
                                    types.

Call forward busy (CFB) redirects a call to another number if the dialed number is busy.

Call forward no reply (CFNR) forwards a call to another number if the dialed number does not answer within a specified period
                                    of time.

If all three call-forwarding services are enabled, CFU overrides CFB and CFNR. The default is that no call-forwarding service
                              is selected.

If you select the functional forwarding method, use the DTMF keypad commands in the table below to configure the call-forwarding service.

Task

DTMF Keypad Command 1

Activate CFU

**21* number #

Deactivate CFU

#21#

Activate CFNR

**61* number #

Deactivate CFNR

#61#

Activate CFB

**67* number #

Deactivate CFB

#67#

When you enable or disable the call-forwarding service, it is enabled or disabled for four basic services: speech, audio
                              at 3.1 kilohertz (kHz), telephony at 3.1 kHz, and telephony at 7 kHz. You should hear a dial tone after you enter the DTMF
                              keypad command when the call-forwarding service is successfully enabled for at least one of the four basic services. If you
                              hear a busy tone, the command is invalid or the switch does not support that service.

## Examples

The following example gives forwarding control to the router:

```
pots forwarding-method functional
```

### Related Commands

Command

Description

pots prefix filter

Sets a filter that prevents a dial prefix from being added to a dialed number when the digits in the dialed number match
                                          the filter.

pots prefix number

Sets a prefix to be added to a called telephone number for analog or modem calls.

## pots line-type

To specify the impedance of your connected telephones, fax machines, or modems, use the pots line - type command in global configuration mode. To disable the specified line type, use the no form of this command.

pots line-type { type1 | type2 | type3 }

no pots line-type { type1 | type2 | type3 }

### Syntax Description

type1

Runs at 600 ohms.

type2

Runs at 900 ohms.

type3

Runs at 300 or 400 ohms.

### Command Default

The default depends on the setting of the pots country command. For more information, see the pots country command.

### Command Modes

Global configuration

## Command History

Release

Modification

12.0(3)T

This command was introduced on the Cisco 800 series.

### Usage Guidelines

This command applies to Cisco 800 series routers.

## Examples

The following example sets the line type to type1:

```
pots line-type type1
```

### Related Commands

Command

Description

pots country

Configures telephones, fax machines, or modems connected to a Cisco 800 series router to use country-specific default settings
                                          for each physical characteristic.

pots dialing - method

Specifies how the Cisco 800 series router collects and sends digits dialed on your connected telephones, fax machines, or
                                          modems.

pots disconnect - supervision

Specifies how a Cisco 800 series router notifies the connected telephones, fax machines, or modems when the calling party
                                          has disconnected.

pots disconnect - time

Specifies the interval in which the disconnect method is applied if telephones, fax machines, or modems connected to a Cisco
                                          800 series router fail to detect that a calling party has disconnected.

pots distinctive - ring - guard - time

Specifies the delay in which a telephone port can be rung after a previous call is disconnected (Cisco 800 series routers).

pots encoding

Specifies the PCM encoding scheme for telephones, fax machines, or modems connected to a Cisco 800 series router.

pots ringing - freq

Specifies the frequency at which telephones, fax machines, or modems connected to a Cisco 800 series router ring.

pots silence - time

Specifies the interval of silence after a calling party disconnects (Cisco 800 series router).

pots tone - source

Specifies the source of dial, ringback, and busy tones for telephones, fax machines, or modems connected to a Cisco 800 series
                                          router.

show pots status

Displays the settings of the telephone port physical characteristics and other information on the telephone interfaces on
                                          a Cisco 800 series router.

## pots prefix filter

To set a filter that prevents a dial prefix from being added to a dialed number when the digits in the dialed number match
                              the filter, use the pots prefix filter command in global configuration mode. To remove the filter, use the no form of this command.

pots prefix filter number

no pots prefix filter number

### Syntax Description

number

Prefix filter numbers, up to a maximum of eight characters.

### Command Default

No default filter is set.

### Command Modes

Global configuration

## Command History

Release

Modification

12.2(2)T

This command was introduced on the Cisco 803 and Cisco 804.

### Usage Guidelines

The pots prefix filter command is used to set a filter for prefix dialing. A maximum of ten filters can be set. Once the maximum number of filters
                              have been configured, an additional filter is not accepted nor does it overwrite any of the existing filters.

To configure a new filter, remove at least one filter using the no pots prefix filter command.

You can set matching criteria for the filter using the * wildcard character. For example, if you configure the filter 1* and
                              a dialed number starts with 1, the called number is not prefixed. Prefix filters can be of variable length. All configured
                              prefix filters are compared to the number dialed, up to the length of the prefix filter. If there is a match, no prefix is
                              added to the dialed number.

## Examples

The following example configures five filters that prevent dial prefixes from being added to dialed numbers:

```
pots prefix filter 192
pots prefix filter 1
pots prefix filter 9
pots prefix filter 0800
pots prefix filter 08456
```

With these filters configured, a prefix is not added to the following dialed numbers:

192	Directory calls

100	Operator services

999	Emergency services

0800...	Toll-free calls

08456...	Calls on an Energis network information controller

### Related Commands

Command

Description

pots forwarding - method

Configures the type of forwarding method to be used for Euro-ISDN (formerly NET3) switches.

pots prefix number

Sets a prefix to be added to a called telephone number for analog or modem calls.

## pots prefix number

To set a prefix to be added to a called telephone number for analog or modem calls, use the pots prefix number command in global configuration mode. To remove the prefix, use the no form of this command.

pots prefix number number

no pots prefix number number

### Syntax Description

number

Prefix, up to a maximum of five digits.

### Command Default

No prefix is associated with the called number for analog or modem calls

### Command Modes

Global configuration

## Command History

Release

Modification

12.2(2)T

This command was introduced on the Cisco 803 and Cisco 804.

### Usage Guidelines

Only one prefix can be configured using this command. If a prefix already exists, the next prefix configured with this command
                              overwrites the old prefix. Prefixes can be of variable length, up to five digits. The no pots prefix number command removes the prefix.

As numbers are dialed on the keypad, a comparison is made to the configured prefix filter. When a match is determined, the
                              number is dialed without adding the prefix. In the unlikely event that the prefix filter has more digits than the dialed number,
                              and the dialed number matches the first digits of the prefix filter, the prefix is not added to the dialed number. For example,
                              if the prefix filter is 5554000 and you dial 555 and stop, the router considers the called number to be 555 and does not add
                              a prefix to the number. This event is unlikely to occur because the number of digits in dialed numbers is typically greater
                              than the number of digits in prefix filters.

## Examples

The following example sets the prefix to 12345:

```
pots prefix number 12345
```

This prefix is added to any number dialed for analog or modem calls that do not match the prefix filter.

### Related Commands

Command

Description

pots prefix filter

Sets a filter that prevents a dial prefix from being added to a dialed number when the digits in the dialed number match the
                                          filter.

## pots ringing-freq

To specify the frequency on the Cisco 800 series router at which connected telephones, fax machines, or modems ring, use the pots ringing - freq command in global configuration mode. To disable the specified frequency, use the no form of this command.

pots ringing-freq { 20Hz | 25Hz | 50Hz }

no pots ringing-freq { 20Hz | 25Hz | 50Hz }

### Syntax Description

20Hz

Connected devices ring at 20 Hz.

25Hz

Connected devices ring at 25 Hz.

50Hz

Connected devices ring at 50 Hz.

### Command Default

The default depends on the setting of the pots country command. For more information, see the pots country command.

### Command Modes

Global configuration

## Command History

Release

Modification

12.0(3)T

This command was introduced on the Cisco 800 series.

### Usage Guidelines

This command applies to Cisco 800 series routers.

## Examples

The following example sets the ringing frequency to 50 Hz:

```
pots ringing-freq 50Hz
```

### Related Commands

Command

Description

pots country

Configures telephones, fax machines, or modems connected to a Cisco 800 series router to use country-specific default settings
                                          for each physical characteristic.

pots dialing - method

Specifies how the Cisco 800 series router collects and sends digits dialed on your connected telephones, fax machines, or
                                          modems.

pots disconnect - supervision

Specifies how a Cisco 800 series router notifies the connected telephones, fax machines, or modems when the calling party
                                          has disconnected.

pots disconnect - time

Specifies the interval in which the disconnect method is applied if telephones, fax machines, or modems connected to a Cisco
                                          800 series router fail to detect that a calling party has disconnected.

pots distinctive - ring - guard - time

Specifies the delay in which a telephone port can be rung after a previous call is disconnected (Cisco 800 series routers).

pots encoding

Specifies the PCM encoding scheme for telephones, fax machines, or modems connected to a Cisco 800 series router.

pots line - type

Specifies the impedance of telephones, fax machines, or modems connected to a Cisco 800 series router.

pots silence - time

Specifies the interval of silence after a calling party disconnects (Cisco 800 series router).

pots tone - source

Specifies the source of dial, ringback, and busy tones for telephones, fax machines, or modems connected to a Cisco 800 series
                                          router.

show pots status

Displays the settings of the telephone port physical characteristics and other information on the telephone interfaces on
                                          a Cisco 800 series router.

## pots silence-time

To specify the interval of silence after a calling party disconnects, use the pots silence - time command in global configuration mode. To disable the specified silence time, use the no form of this command.

pots silence-time interval

no pots silence-time interval

### Syntax Description

interval

Number from 0 to 10 (seconds).

### Command Default

The default depends on the setting of the pots country command. For more information, see the pots country command.

### Command Modes

Global configuration

## Command History

Release

Modification

12.0(3)T

This command was introduced on the Cisco 800 series.

### Usage Guidelines

This command applies to Cisco 800 series routers.

## Examples

The following example sets the interval of silence to 10 seconds:

```
pots silence-time 10
```

### Related Commands

Command

Description

pots country

Configures telephones, fax machines, or modems connected to a Cisco 800 series router to use country-specific default settings
                                          for each physical characteristic.

pots dialing - method

Specifies how the Cisco 800 series router collects and sends digits dialed on your connected telephones, fax machines, or
                                          modems.

pots disconnect - supervision

Specifies how a Cisco 800 series router notifies the connected telephones, fax machines, or modems when the calling party
                                          has disconnected.

pots disconnect - time

Specifies the interval in which the disconnect method is applied if telephones, fax machines, or modems connected to a Cisco
                                          800 series router fail to detect that a calling party has disconnected.

pots distinctive - ring - guard - time

Specifies the delay in which a telephone port can be rung after a previous call is disconnected (Cisco 800 series routers).

pots encoding

Specifies the PCM encoding scheme for telephones, fax machines, or modems connected to a Cisco 800 series router.

pots line - type

Specifies the impedance of telephones, fax machines, or modems connected to a Cisco 800 series router.

pots ringing - freq

Specifies the frequency at which telephones, fax machines, or modems connected to a Cisco 800 series router ring.

pots tone - source

Specifies the source of dial, ringback, and busy tones for telephones, fax machines, or modems connected to a Cisco 800 series
                                          router.

show pots status

Displays the settings of the telephone port physical characteristics and other information on the telephone interfaces on
                                          a Cisco 800 series router.

## pots tone-source

To specify the source of dial, ringback, and busy tones for your connected telephones, fax machines, or modems, use the pots tone - source command in global configuration mode. To disable the specified source, use the no form of this command.

pots tone-source { local | remote }

no pots tone-source { local | remote }

### Syntax Description

local

Router supplies the tones.

remote

Telephone switch supplies the tones.

### Command Default

Local (router supplies the tones)

### Command Modes

Global configuration

## Command History

Release

Modification

12.0(3)T

This command was introduced on the Cisco 800 series.

### Usage Guidelines

This command applies to Cisco 800 series routers.

This command applies only to ISDN lines connected to a EURO-ISDN (NET3) switch.

## Examples

The following example sets the tone source to remote:

```
pots tone-source remote
```

### Related Commands

Command

Description

pots country

Configures telephones, fax machines, or modems connected to a Cisco 800 series router to use country-specific default settings
                                          for each physical characteristic

pots dialing - method

Specifies how the Cisco 800 series router collects and sends digits dialed on your connected telephones, fax machines, or
                                          modems.

pots disconnect - supervision

Specifies how a Cisco 800 series router notifies the connected telephones, fax machines, or modems when the calling party
                                          has disconnected.

pots disconnect - time

Specifies the interval in which the disconnect method is applied if telephones, fax machines, or modems connected to a Cisco
                                          800 series router fail to detect that a calling party has disconnected.

pots distinctive - ring - guard - time

Specifies the delay in which a telephone port can be rung after a previous call is disconnected (Cisco 800 series routers).

pots encoding

Specifies the PCM encoding scheme for telephones, fax machines, or modems connected to a Cisco 800 series router.

pots line - type

Specifies the impedance of telephones, fax machines, or modems connected to a Cisco 800 series router.

pots ringing - freq

Specifies the frequency at which telephones, fax machines, or modems connected to a Cisco 800 series router ring.

pots silence - time

Specifies the interval of silence after a calling party disconnects (Cisco 800 series router).

show pots status

Displays the settings of the telephone port physical characteristics and other information on the telephone interfaces on
                                          a Cisco 800 series router.

## pre-dial delay

To configure a delay on an Foreign Exchange Office (FXO) interface between the beginning of the off-hook state and the initiation
                              of dual-tone multifrequency (DTMF) signaling, use the pre - dial delay command in voice-port configuration mode. To reset to the default, use the no form of the command.

pre-dial delay seconds

no pre-dial delay

### Syntax Description

seconds

Delay, in seconds, before signaling begins. Range is from 0 to 10. Default is 1.

### Command Default

1 second

### Command Modes

Voice-port configuration

## Command History

Release

Modification

11.(7)T

This command was introduced on the Cisco 3600 series.

12.0(2)T

This command was integrated into Cisco IOS Release 12.0(2)T.

### Usage Guidelines

To disable the command, set the delay to 0. When an FXO interface begins to draw loop current (off-hook state), a delay is
                              required between the initial flow of loop current and the beginning of signaling. Some devices initiate signaling too quickly,
                              resulting in redial attempts. This command allows a signaling delay.

## Examples

The following example sets a predial delay value of 3 seconds on the FXO port:

```
voice-port 1/0/0
 pre-dial delay 3
```

### Related Commands

Command

Description

timeouts initial

Configures the initial digit timeout value for a specified voice port.

timing delay - duration

Configures delay dial signal duration for a specified voice port.

## preference (dial-peer)

To indicate the preferred order of an outbound dial peer within a hunt group, use the preference command in dial-peer configuration mode. To remove the preference, use the no form of this command.

preference value

no preference

### Syntax Description

value

An integer from 0 to 10. A lower number indicates a higher preference. The default is 0, which is the highest preference.

### Command Default

The longest matching dial peer supersedes the 
                              preference
                              value.

### Command Modes

Dial-peer configuration (dial-peer)

## Command History

Release

Modification

11.3(1)MA

This command was introduced on the Cisco MC3810.

12.0(3)T

This command was integrated into Cisco IOS Release 12.0(3)T and implemented on the Cisco 2600 series and Cisco 3600 series
                                          routers.

12.0(4)T

This command was modified to support Voice over Frame Relay(VoFR) dial peers on the Cisco 2600 series and Cisco 3600 series
                                          routers.

15.1(3)T

This command was modified. Support for matching different pattern types was modified.

Introduced support for YANG models.

### Usage Guidelines

This command applies to Plain Old Telephone Service(POTS), VoIP, VoFR, and Voice over ATM(VoATM) dial peers.

Use this command to indicate the preferred order for matching dial peers in a hunt group. Setting a preference enables the
                              desired dial peer to be selected when multiple dial peers within a hunt group are matched for a dial string.

If POTS and voice-network peers are mixed in the same hunt group, the POTS dial peers must have priority over the voice-network
                                          dial peers.

The hunting algorithm preference is configurable. For example, to specify that a call processing sequence go to destination
                              A, then to destination B, and finally to destination C, you would assign preferences (0 being the highest preference) to the
                              destinations in the following order:

Preference 0 to A

Preference 1 to B

Preference 2 to C

Use this command only on the same pattern type. For example, destination uri and destination-pattern are two different pattern
                              types. By default, destination uri has higher preference than destination-pattern.

## Examples

The following example shows how to set POTS dial peer 10 to a preference of 1, POTS dial peer 20 to a preference of 2, and
                              VoFR dial peer 30 to a preference of 3:

```
dial-peer voice 10 pots
 destination-pattern 5550150
 preference 1
 exit
dial-peer voice 20 pots
 destination-pattern 5550150
 preference 2
 exit
dial-peer voice 30 vofr
 destination-pattern 5550150
 preference 3
 exit
```

The following examples shows different dial peer configurations:

```
Dialpeer        destpat         preference              session-target
1               4085550148      0 (highest)             jmmurphy-voip
2               408555          0                       sj-voip
3               408555          1 (lower)               backup-sj-voip
4               ..........      1                       0:D     (interface)
5               ..........      0                       anywhere-voip
```

If the destination number is 4085550148, the order of attempts is 1, 2, 3, 5, 4:

```
Dialpeer        destpat         preference
1               408555          0
2               4085550148      1
3               4085550         0
4 				4085550				0
```

The following example shows how to set POTS dial peer 10 for the destination-pattern to a preference of 0, POTS dial peer
                              20 for the destination uri to a preference of 1. Though destination-pattern has higher preference than destination uri, destination
                              uri takes preference:

```
dial-peer voice 10 pots
 destination-pattern 5550158
 preference 0
 exit
dial-peer voice 20 pots
 destination uri 5550158
 preference 1
```

exit

### Related Commands

Command

Description

called-number (dial-peer)

Enables an incoming VoFR call leg to get bridged to the correct POTS call leg when using a static FRF.11 trunk connection.

codec (dial-peer)

Specifies the voice coder rate of speech for a Voice over Frame Relay dial peer.

cptone

Specifies a regional analog voice interface-related tone, ring, and cadence setting.

destination-pattern

Specifies the prefix, the full E.164 telephone number, or an ISDN directory number (depending on the dial plan) to be used
                                          for a dial peer.

destination uri

Specifies the voice class used to match a dial peer to the destination uniform resource identifier (URI).

dtmf-relay (Voice over Frame Relay)

Enables the generation of FRF.11 Annex A frames for a dial peer.

session protocol

Establishes a session protocol for calls between the local and remote routers via the packet network.

session target

Specifies a network-specific address for a specified dial peer or destination gatekeeper.

signal-type

Sets the signaling type to be used when connecting to a dial peer.

## preemption enable

To enable preemption capability on a trunk group, use the preemption enable command in trunk group configuration mode. To disable preemption capabilities, use the no form of this command.

preemption enable

no preemption enable

### Syntax Description

This command has no arguments or keywords.

### Command Default

Preemption is disabled on the trunk group.

### Command Modes

Trunk group configuration

## Command History

Release

Modification

12.4(4)XC

This command was introduced.

12.4(9)T

This command was integrated into Cisco IOS Release 12.4(9)T.

## Examples

The following command example enables preemption capabilities on trunk group test:

```
Router(config)# trunk group test Router(config-trunk-group)# preemption enable
```

### Related Commands

Command

Description

isdn integrate all

Enables integrated mode on an ISDN PRI interface.

max-calls

Sets the maximum number of calls that a trunk group can handle.

preemption guard timer

Defines time for a DDR call and allows time to clear the last call from the channel.

preemption level

Sets the preemption level of the selected outbound dial peer. Voice calls can be preempted by a DDR call with higher preemption
                                          level.

preemption tone timer

Defines the expiry time for the preemption tone for the outgoing call being preempted by a DDR backup call.

## preemption guard timer

To define the time for a DDR call and to allow time to clear the last call from the channel, use the preemption guard timer command in trunk group configuration mode. To disable the preemption guard time, use the no form of this command.

preemption guard timer value

no preemption guard timer

### Syntax Description

value

Number, in milliseconds for the preemption guard timer. The range is 60 to 500. The default is 60.

### Command Default

No preemption guard timer is configured.

### Command Modes

Trunk group configuration

## Command History

Release

Modification

12.4(4)XC

This command was introduced.

12.4(9)T

This command was integrated into Cisco IOS Release 12.4(9)T.

## Examples

The following set of commands configures a 60-millisecond preemption guard timer on the trunk group dial2.

```
Router(config)# trunk group dial2 Router(config-trunk-group)# preemption enable Router(config-trunk-group)# preemption guard timer 60
```

### Related Commands

Command

Description

isdn integrate all

Enables integrated mode on an ISDN PRI interface.

max-calls

Sets the maximum number of calls that a trunk group can handle.

preemption enable

Enables preemption capabilities on a trunk group.

preemption level

Sets the preemption level of the selected outbound dial-peer. Voice calls can be preempted by a DDR call with higher preemption
                                          level.

preemption tone timer

Sets the expiry time for the preemption tone for the outgoing call being preempted by a DDR backup call.

## preemption level

To set the precedence for voice calls to be preempted by a dial-on demand routing (DDR) call for the trunk group, use the preemption level command in dial-peer configuration mode. To restore the default preemption level setting, use the no form of this command

preemption level { flash-override | flash | immediate | priority | routine }

no preemption level

### Syntax Description

flash-override

Sets the precedence for voice calls to preemption level 0 (highest).

flash

Sets the precedence for voice calls to preemption level 1.

immediate

Sets the precedence for voice calls to preemption level 2.

priority

Sets the precedence for voice calls to preemption level 3.

routine

Sets the precedence for voice calls to preemption level 4 (lowest). This is the default.

### Command Default

The preemption level default is routine (lowest).

### Command Modes

Dial-peer configuration

## Command History

Release

Modification

12.4(4)XC

This command was introduced.

12.4(9)T

This command was integrated into Cisco IOS Release 12.4(9)T.

## Examples

The following command example sets a preemption level of flash (level 1) on POTS dial-peer 20:

```
Router(config)# dial-peer voice 20 pots Router(config-dial-peer)# preemption level flash
```

### Related Commands

Command

Description

dialer preemption level

Sets the precedence for voice calls to be preempted by a DDR call for the dialer map.

isdn integrate all

Enables integrated mode on an ISDN PRI interface.

max-calls

Sets the maximum number of calls that a trunk group can handle.

preemption enable

Enables preemption capabilities on a trunk group.

preemption guard timer

Defines time for a DDR call and allows time to clear the last call from the channel.

preemption tone timer

Defines the expiry time for the preemption tone for the outgoing call being preempted by a DDR backup call.

## preemption tone timer

To set the expiry time for the preemption tone for the outgoing call being preempted by a DDR backup call, use the preemption tone timer command in trunk group configuration mode. To clear the expiry time, use the no form of this command.

preemption tone timer seconds

no preemption tone timer

### Syntax Description

seconds

Length of preemption tone, in seconds. Range: 4 to 30. Default: 10.

### Command Default

No preemption tone timer is configured.

### Command Modes

Trunk group configuration

## Command History

Release

Modification

12.4(4)XC

This command was introduced.

12.4(9)T

This command was integrated into Cisco IOS Release 12.4(9)T.

## Examples

The following set of commands configures a 20-second preemption tone timer on trunk group dial2.

```
Router(config)# trunk group dial2 Router(config-trunk-group)# preemption enable Router(config-trunk-group)# preemption tone timer 20
```

### Related Commands

Command

Description

isdn integrate all

Enables integrated mode on an ISDN PRI interface.

max-calls

Sets the maximum number of calls that a trunk group can handle.

preemption enable

Enables preemption capabilities on a trunk group.

preemption level

Sets the preemption level of the selected outbound dial peer. Voice calls can be preempted by a DDR call with higher preemption
                                          level.

## prefix

To specify the prefix of the dialed digits for a dial peer, use the prefix command in dial-peer configuration mode. To disable this feature, use the no form of this command.

prefix string

no prefix

### Syntax Description

string

Integers that represent the prefix of the telephone number associated with the specified dial peer. Valid values are 0 through
                                          9 and a comma (,). Use a comma to include a pause in the prefix.

### Command Default

Null string

### Command Modes

Dial-peer configuration

## Command History

Release

Modification

11.3(1)T

This command was introduced on the Cisco 3600 series.

12.0(4)XJ

This command was implemented on the Cisco AS5300. It and modified for store-and-forward fax.

12.1(1)T

This command was integrated into Cisco IOS Release 12.1(1)T.

12.2(4)T

This command was implemented on the Cisco 1750.

12.2(8)T

This command was implemented on the following platforms: Cisco 1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, and
                                          Cisco 3745.

12.2(13)T

This command was supported in Cisco IOS Release 12.2(13)T and implemented on the Cisco 2600XM, Cisco ICS7750, and Cisco VG200.

### Usage Guidelines

Use this command to specify a prefix for a specific dial peer. When an outgoing call is initiated to this dial peer, the prefix string value is sent to the telephony interface first, before the telephone number associated with the dial peer.

If you want to configure different prefixes for dialed numbers on the same interface, you need to configure different dial
                              peers.

This command is applicable only to plain old telephone service (POTS) dial peers. This command applies to off-ramp store-and-forward
                              fax functions.

## Examples

The following example specifies a prefix of 9 and then a pause:

```
dial-peer voice 10 pots
 prefix 9,
```

The following example specifies a prefix of 5120002:

```
Router(config-dial-peer)# prefix 5120002
```

### Related Commands

Command

Description

answer - address

Specifies the full E.164 telephone number to be used to identify the dial peer of an incoming call.

destination - pattern

Specifies either the prefix or the full E.164 telephone number to be used for a dial peer.

## prefix (Annex G)

To restrict the prefixes for which the gatekeeper should query the
                              		  Annex G border element (BE), use the prefix command in gatekeeper border element configuration mode.

prefix prefix * [ seq | blast ]

### Syntax Description

prefix *

Prefix for which BEs should be queried.

seq

(Optional) Queries are sent out to the neighboring BEs
                                          						sequentially.

blast

(Optional) Queries are sent out to the neighboring BEs
                                          						simultaneously.

### Command Default

Any time a remote zone query occurs, the BE is also queried.

### Command Modes

Gatekeeper border element configuration

## Command History

Release

Modification

12.2(2)XA

This command was introduced.

12.2(4)T

This command was integrated into Cisco IOS Release
                                          						12.2(4)T. Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400 is not
                                          						included in this release.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(11)T

This command was integrated into Cisco IOS Release
                                          						12.2(11)T.

### Usage Guidelines

By default, the gatekeeper sends all remote zone requests to the BE.
                              		  Use this command only if you want to restrict the queries to the BE to a
                              		  specific prefix or set of prefixes.

## Examples

The following example directs the gatekeeper to query the BE using a
                              		  prefix of 408.

```
Router(config-gk-annexg)# prefix 408* seq
```

### Related Commands

Command

Description

h323 - annexg

Enables the BE on the gatekeeper and enters border element
                                          						configuration mode.

## prefix (stcapp-fac)

To define a prefix for feature access codes (FACs) used with the SCCP telephony control (STC) application, use the prefix command in STC application feature access-code configuration mode. To return the prefix to its default, use the no form of this command.

prefix prefix-string

no prefix

### Syntax Description

prefix-string

String of one to five characters that can be dialed on a telephone keypad. String must start with an asterisk (*) or a number
                                          sign (#). Default is **.

### Command Default

The default value is **.

### Command Modes

STC application feature access-code configuration (stcapp-fac)

## Command History

Release

Modification

12.4(2)T

This command was introduced.

### Usage Guidelines

This command modifies the FAC prefix from the default (**) to the specified character string.

Use the show stcapp feature codes command to display a list of all FACs.

## Examples

The following example shows how to change the prefix for FACs from the default value (**) to two number signs (##).

```
Router(config)# stcapp feature access-code Router(stcapp-fac)# prefix ## Router(stcapp-fac)#
```

### Related Commands

Command

Description

call forward all

Defines the feature code in the feature access code (FAC) for forwarding all calls.

call forward cancel

Defines the feature code in the feature access code (FAC) for cancelling Call Forward All.

pickup direct

Defines the feature code in the feature access code (FAC) for Directed Call Pickup.

pickup group

Defines the feature code in the feature access code (FAC) for call pickup from another group.

pickup local

Defines the feature code in the feature access code (FAC) for call pickup from the local group.

show stcapp feature codes

Displays all feature access codes (FACs) and all feature speed-dials (FSDs).

stcapp feature access-code

Enables feature access codes (FACs) in STC application and enters STC application feature access-code configuration mode for
                                          changing values of the prefix and features codes from the default.

## prefix (stcapp-fsd)

To define a prefix for feature speed dials (FSDs) used with the SCCP telephony control (STC) application, use the prefix command in STC application feature speed-dial configuration mode. To return the prefix to its default, use the no form of this command.

prefix prefix-string

no prefix

### Syntax Description

prefix-string

String of one to five characters (0-9, *, #) that can be dialed on a telephone keypad. String must begin with asterisk (*)
                                          or number sign(#). Default is *.

### Command Default

The default value is *.

### Command Modes

STC application feature speed-dial configuration (stcapp-fsd)

## Command History

Release

Modification

12.4(2)T

This command was introduced.

### Usage Guidelines

This command is used with the STC application, which enables certain features on analog FXS endpoints that use Skinny Client
                              Control Protocol (SCCP) for call control. Phone users must dial the feature speed-dial (FSD) prefix string before dialing
                              an FSD speed-dial that dials a telephone number. For example, to dial the telephone number that is stored in speed-dial position
                              3, a phone user dials *2.

Use this command only if you want to change the prefix from its default (*).

The show stcapp feature codes command displays the FSD prefix and all FSD speed-dials.

The following example shows how to change the prefix for FSDs from the default value (*) to three asterisks (***). After this
                              value is configured, a phone user must press***2 on the keypad to dial speed-dial number 2.

```
Router(config)# stcapp feature speed-dial Router(stcapp-fsd)# prefix *** Router(stcapp-fsd)# speed dial from 2 to 7 Router(stcapp-fsd)# redial 9 Router(stcapp-fsd)# voicemail 8 Router(stcapp-fsd)# exit
```

### Related Commands

Command

Description

redial

Defines an speed-dial code to dial again the most-recently dialed number on this phone line.

show stcapp feature codes

Displays all feature access codes (FACs) and all feature speed-dials (FSDs).

speed dial

Designates a range of feature speed-dials (FSDs) in STC application.

stcapp feature access-code

Enables feature speed-dials (FSDs) in STC application and enters STC application feature speed-dial configuration mode for
                                          changing values of the prefix and speed-dial codes from the default.

voicemail (stcapp-fsd)

Defines an speed-dial code to dial the voice-mail number.

## preloaded-route

To enable preloaded
                              		  route support for VoIP Session Initiation Protocol (SIP) calls, use the preloaded-route command in SIP configuration mode
                              		  or voice class tenant configuration mode. To reset to the default, use the no form of this
                              		  command.

preloaded-route [ sip-server ] service-route system

no preloaded-route

### Syntax Description

sip-server

(Optional) Adds SIP server information to the Route header.

service-route

Adds the
                                          						Service-Route information to the Route header.

system

Specifies that the preloaded route support for VoIP Session
                                          						Initiation Protocol (SIP) calls use the global sip-ua value. This keyword is
                                          						available only for the tenant mode to allow it to fallback to the global
                                          						configurations.

### Command Default

Route support is
                              		  not enabled.

### Command Modes

SIP configuration (conf-serv-sip)

Voice class tenant configuration (config-class)

## Command History

Release

Modification

12.4(22)YB

This
                                          						command was introduced.

15.0(1)M

This
                                          						command was integrated into Cisco IOS Release 15.0(1)M.

15.6(2)T and IOS XE Denali 16.3.1

This command was modified to include the keyword: system .

### Usage Guidelines

The voice-class preloaded-route command, in dial-peer configuration
                              		  mode, takes precedence over the preloaded-route command in SIP configuration mode. However, if the voice-class preloaded-route command is configured with the system keyword,
                              		  the gateway uses the global settings configured by the preloaded-route command.

Enter SIP
                              		  configuration mode after entering voice-service VoIP configuration mode, as
                              		  shown in the "Examples" section.

## Examples

The following
                              		  example shows how to configure the system to include SIP server and
                              		  Service-Route information in the Route header:

```
voice service voip
sip
 preloaded-route sip-server service-route
```

The following
                              		  example shows how to configure the system to include only Service-Route
                              		  information in the Route header:

```
voice service voip
sip
 preloaded-route service-route
```

```
Router(config-class)# preloaded-route service-route system
```

### Related Commands

Command

Description

sip

Enters
                                          						SIP configuration mode from voice-service VoIP configuration mode.

voice - class preloaded-route

Enables
                                          						preloaded route support for dial-peer SIP calls.

## presence

To enable presence service and enter presence configuration mode, use the presence command in global configuration mode. To disable presence service, use the no form of this command.

presence

no presence

### Syntax Description

This command has no arguments or keywords.

### Command Default

Presence service is disabled.

### Command Modes

Global configuration (config)

## Command History

Release

Cisco Product

Modification

12.4(11)XJ

Cisco Unified CME 4.1

This command was introduced.

12.4(15)T

Cisco Unified CME 4.1

This command was integrated into Cisco IOS Release 12.4(15)T.

### Usage Guidelines

This command enables the router to perform the following presence functions:

Process presence requests from internal lines to internal lines. Notify internal subscribers of any status change.

Process incoming presence requests from a SIP trunk for internal lines. Notify external subscribers of any status change.

Send presence requests to external presentities on behalf of internal lines. Relay status responses to internal lines.

## Examples

The following example shows how to enable presence and enter presence configuration mode to set the maximum subscriptions
                              to 150:

```
Router(config)# presence Router(config-presence)# max-subscription 150
```

### Related Commands

Command

Description

allow watch

Allows a directory number on a phone registered to Cisco Unified CME to be watched in a presence service.

debug presence

Displays debugging information about the presence service.

max-subscription

Sets the maximum number of concurrent watch sessions that are allowed.

presence enable

Allows the router to accept incoming presence requests.

server

Specifies the IP address of a presence server for sending presence requests from internal watchers to external presence entities.

show presence global

Displays configuration information about the presence service.

show presence subscription

Displays information about active presence subscriptions.

## presence call-list

To enable Busy Lamp Field (BLF) monitoring for call lists and directories on phones registered to the Cisco Unified CME router,
                              use the presence call-list command in ephone, presence, or voice register pool configuration mode. To disable BLF indicators for call lists, use the no form of this command.

presence call-list

no presence call-list

### Syntax Description

This command has no arguments or keywords.

### Command Default

BLF monitoring for call lists is disabled.

### Command Modes

Ephone configuration (config-ephone) Presence configuration (config-presence) Voice register pool configuration (config-register pool)

## Command History

Release

Modification

12.4(11)XJ

This command was introduced.

12.4(15)T

This command was integrated into Cisco IOS Release 12.4(15)T.

### Usage Guidelines

This command enables a phone to monitor the line status of directory numbers listed in a directory or call list, such as a
                              missed calls, placed calls, or received calls list. Using this command in presence mode enables the BLF call-list feature
                              for all phones. To enable the feature for an individual SCCP phone, use this command in ephone configuration mode. To enable
                              the feature for an individual SIP phone, use this command in voice register pool configuration mode.

If this command is disabled globally and enabled in voice register pool or ephone configuration mode, the feature is enabled
                              for that voice register pool or ephone.

If this command is enabled globally, the feature is enabled for all voice register pools and ephones regardless of whether
                              it is enabled or disabled on a specific voice register pool or ephone.

To display a BLF status indicator, the directory number associated with a telephone number or extension must have presence
                              enabled with the allow watch command.

For information on the BLF status indicators that display on specific types of phones, see the Cisco Unified IP Phone documentation for your phone model.

## Examples

The following example shows the BLF call-list feature enabled for ephone 1. The line status of a directory number that appears
                              in a call list or directory is displayed on phone 1 if the directory number has presence enabled.

```
Router(config)# ephone 1 Router(config-ephone)# presence call-list
```

### Related Commands

Command

Description

allow watch

Allows a directory number on a phone registered to Cisco Unified CME to be watched in a presence service.

blf-speed-dial

Enables BLF monitoring for a speed-dial number on a phone registered to Cisco Unified CME.

presence

Enables presence service and enters presence configuration mode.

show presence global

Displays configuration information about the presence service.

## presence enable

To allow incoming presence requests, use the presence enable command in SIP user-agent configuration mode. To block incoming requests, use the no form of this command.

presence enable

no presence enable

### Syntax Description

This command has no arguments or keywords.

### Command Default

Incoming presence requests are blocked.

### Command Modes

SIP UA configuration (config-sip-ua)

## Command History

Release

Modification

12.4(11)XJ

This command was introduced.

12.4(15)T

This command was integrated into Cisco IOS Release 12.4(15)T.

### Usage Guidelines

This command allows the router to accept incoming presence requests (SUBSCRIBE messages) from internal watchers and SIP trunks.
                              It does not impact outgoing presence requests.

## Examples

The following example shows how to allow incoming presence requests:

```
Router(config)# sip-ua Router(config-sip-ua)# presence enable
```

### Related Commands

Command

Description

allow subscribe

Allows internal watchers to monitor external presence entities (directory numbers).

allow watch

Allows a directory number on a phone registered to Cisco Unified CME to be watched in a presence service.

max-subscription

Sets the maximum number of concurrent watch sessions that are allowed.

show presence global

Displays configuration information about the presence service.

show presence subscription

Displays information about active presence subscriptions.

watcher all

Allows external watchers to monitor internal presence entities (directory numbers).

## pri-group (pri-slt)

To specify an ISDN PRI on a channelized T1 or E1 controller, use the pri - group (pri - slt) command in controller configuration mode. To remove the ISDN
                              		  PRI configuration, use the no form of this command.

pri-group [ timeslots timeslot-range [ nfas_d [ backup | none | primary [ nfas_int number ]] [ nfas-group number [ iua as-name ]]]]

no pri-group

### Syntax Description

timeslots timeslot - range

Specifies a single range of timeslot values in the PRI
                                          						goup. For T1, the allowable range is from 1 to 23. For E1, the allowable range
                                          						is from 1 to 31.

nfas_d

Specifies the operation of the D channel timeslot.

backup

(Optional) Specifes that the operation of the D channel
                                          						timeslot on this controller is the NFAS D backup.

none

(Optional) Specifes that the D channel timeslot is used as
                                          						an additional B channel.

primary

Specifies that the D channel timeslot on this controller in
                                          						NFAS D.

nfas_int range

Specifies the provisioned NFAS interface value. Valid
                                          						values range from 0 to 32.

nfas-group number

Specifies the NFAS group and the NFAS group number. Valid
                                          						values range from 0 to 31.

iua as - name

Binds the Non-Facility Associated Signaling (NFAS) group to
                                          						the IDSN User Adaptation Layer (IUA) application server (AS).

### Command Default

No ISDN-PRI group is configured.

### Command Modes

Controller configuration

## Command History

Release

Modification

12.2(11)T

This command was introduced.

12.2(15)T

This command was integrated on the Cisco 2420, Cisco 2600
                                          						series, Cisco 3600 series, and Cisco 3700 series; and Cisco AS5300, Cisco
                                          						AS5350, Cisco AS5400, and Cisco AS5850 network access server (NAS) platforms.

### Usage Guidelines

The pri-group (pri-slt) command provides another way to bind a D
                              		  channel to a specific IUA AS. This option allows the RLM group to be configured
                              		  at the pri-group level instead of in the D channel configuration. For example,
                              		  a typical configuration would look like the following:

```
controller t1 1/0/0
  pri-group timeslots 1-24 nfas_d pri nfas_int 0 nfas_group 1 iua asname
```

Before you enter the pri - group command,
                              		  you must specify an ISDN-PRI switch type and an E1 or T1 controller.

When configuring NFAS, you use an extended version of the pri-group
                              		  command to specify the following values for the associated channelized T1
                              		  controllers configured for ISDN:

The range of PRI
                                    			 timeslots to be under the control of the D channel (timeslot 24).

The function to be
                                    			 performed by timeslot 24 (primary D channel, backup, or none); the latter
                                    			 specifies its use as a B channel.

The group identifier
                                    			 number for the interface under the control of a particular D channel.

The iua keyword is used to bind an NFAS group to the IUA AS.

When binding the D channel to an IUA AS, the as-name must match the name of an AS set up during IUA
                              		  configuration.

Before you can modify a PRI group on a Media Gateway Controller
                              		  (MGC), you must first shut down the D channel.

The following shows how to shut down the D channel:

```
Router# configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)# interface Dchannel3/0:1
Router(config-if)# shutdown
```

## Examples

The following example configures the NFAS primary D channel on one
                              		  channelized T1 controller, and binds the D channel to an IUA AS. This example
                              		  uses the Cisco AS5400 and applies to T1, which has 24 timeslots and is used
                              		  mainly in North America and Japan:

```
Router(config-controller)# pri-group timeslots 1-23 nfas-d primary nfas-int 0 nfas-group 1 iua as5400-4-1
```

The following example applies to E1, which has 32 timeslots and is
                              		  used by the rest of the world:

```
Router(config-controller)# pri-group timeslots 1-31 nfas-d primary nfas-int 0 nfas-group 1 iua as5400-4-1
```

The following example configures ISDN-PRI on all time slots of
                              		  controller E1:

```
Router(config)# controller E1 4/1
Router(config-controller)# pri-group timeslots 1-7,16
```

In the following example, the rlm - timeslot keyword automatically creates interface serial 4/7:11 (4/7:0:11 if you are
                              		  using the CT3 card) for the D channel object on a Cisco AS5350. You can choose
                              		  any timeslot other than 24 to be the virtual container for the D channel
                              		  parameters for ISDN.

```
Router(config-controller)# pri-group timeslots 1-23 nfas-d primary nfas-int 0 nfas-group 0 rlm-timeslot 3
```

### Related Commands

Command

Description

isdn switch - type

Configures the Cisco 2600 series router PRI interface to
                                          						support QSIG signaling.

## pri-group nec-fusion

To configure your NEC PBX to support Fusion Call Control Signaling (FCCS), use the pri - group nec - fusion command in controller configuration mode. To disable FCCS, use the no form of this command.

pri-group nec-fusion { pbx-ip-address | pbx-ip-host-name } pbx-port number

no pri-group nec-fusion { pbx-ip-address | pbx-ip-host-name } pbx-port number

### Syntax Description

pbx - ip - address

IP address of the NEC PBX.

pbx - ip - host - name

Host name of the NEC PBX.

pbx - port number

Port number for the PBX. Range is from 49152 to 65535. Default is 55000. If this value is already in use, the next greater
                                          value is used.

### Command Default

PBX port number: 55000

### Command Modes

Controller configuration

## Command History

Release

Modification

12.0(7)T

This command was introduced on the Cisco AS5300.

12.2(1)

This command was modified to add support for setup messages from a POTS dial peer.

### Usage Guidelines

This command is used only if the PBX in your configuration is an NEC PBX, and if you are configuring it to run FCCS and not
                              QSIG signaling.

## Examples

The following example directs this NEC PBX to use FCCS:

```
pri-group nec-fusion 172.31.255.255 pbx-port 60000
```

### Related Commands

Command

Description

isdn protocol-emulate

Configures the Layer 2 and Layer 3 port protocol of a BRI voice port or a PRI interface to emulate NT (network) or TE (user)
                                          functionality.

isdn switch type

Configures the Cisco AS5300 universal access server PRI interface to support QSIG signaling.

show cdapi

Displays the CDAPI.

show rawmsg

Displays the raw messages owned by the required component.

## pri-group timeslots

To specify an ISDN PRI group on a channelized T1 or E1 controller, and to release the ISDN PRI signaling time slot, use the pri-group timeslots command in controller configuration mode. To remove or change the ISDN PRI configuration, use the no form of this command.

pri-group timeslots timeslot-range [ nfas_d { backup nfas_int number nfas_group number [ service mgcp ] | none nfas_int number nfas_group number [ service mgcp ] | primary nfas_int number nfas_group number [ iua as-name | rlm-group number | service mgcp ]} | service mgcp ] [ voice-dsp ]

no pri-group timeslots timeslot-range [ nfas_d { backup nfas_int number nfas_group number [ service mgcp ] | none nfas_int number nfas_group number [ service mgcp ] | primary nfas_int number nfas_group number [ iua as-name | rlm-group number | service mgcp ]} | service mgcp ] [ voice-dsp ]

### Syntax Description

timeslot-range

A value or range of values for time slots on a T1 or E1 controller that consists of an ISDN PRI group. Use a hyphen to indicate
                                          a range.

Groups of time slot ranges separated by commas (1-4,8-23 for example) are also accepted.

nfas_d

(Optional) Configures the operation of the ISDN PRI D channel.

backup

The D-channel time slot is used as the Non-Facility Associated Signaling (NFAS) D backup.

service mgcp

(Optional) Configures the service type as Media Gateway Control Protocol (MGCP) service.

none

The D-channel time slot is used as an additional B channel.

primary

The D-channel time slot is used as the NFAS D primary.

nfas_int number

Specifies the provisioned NFAS interface as a value. The NFAS interface range is from 0 to 44.

nfas_group number

Specifies the NFAS group. The NFAS group number range is from 0 to 31.

iua as-name

(Optional) Configures the ISDN User Adaptation Layer (IUA) application server (AS) name.

rlm-group number

(Optional) Specifies the Redundant Link Manager (RLM) group and releases the ISDN PRI signaling channel. The RLM group number
                                          range is from 0 to 255.

voice-dsp

(Optional) Configures an ISDN PRI group for voice applications by using the Digital Signal Processor (DSP).

### Command Default

No ISDN PRI group is configured. The switch type is automatically set to the National ISDN switch type ( primary-ni keyword) when the pri-group timeslots command is configured with the rlm-group keyword.

### Command Modes

Controller configuration (config-controller)

## Command History

Release

Modification

11.0

This command was introduced.

11.3

This command was enhanced to support NFAS.

12.0(2)T

This command was implemented on the Cisco MC3810 multiservice concentrator.

12.0(7)XK

This command was implemented on the Cisco 2600 and Cisco 3600 series routers.

12.1(2)T

The modifications in Cisco IOS Release 12.0(7)XK were integrated into Cisco IOS Release 12.1(2)T.

12.2(8)B

This command was modified with the rlm-group subkeyword to support the release of the ISDN PRI signaling channels.

12.2(15)T

The modifications in Cisco IOS Release 12.2(8)B were integrated into Cisco IOS Release 12.2(15)T.

12.4(16)b

This command was modified to ensure that the NFAS primary interface is configured before the NFAS backup or NFAS none interfaces
                                          are configured.

12.4(24)T

Support was extended to provide backup functionality for the NFAS interface in MGCP backhaul mode. With this support, if the
                                          primary interface fails, the backup can become active and calls can be maintained.

15.1(3)T

This command was modified. The voice-dsp keyword was added.

### Usage Guidelines

The pri-group command supports the use of DS0 time slots for 
                              Signaling System 7 (SS7) links, and, therefore, enables the coexistence of SS7 links and PRI voice and data bearer channels
                              on the same T1 or E1 span. In these configurations, the command applies to voice applications.

In SS7-enabled Voice over IP (VoIP) configurations when an RLM group is configured, High-Level Data Link Control (HDLC) resources
                              allocated for ISDN signaling on a digital subscriber line (DSL) interface are released and the signaling slot is converted
                              to a bearer channel (B24). The D channel will be running on IP. The chosen D-channel time slot can still be used by a B channel
                              by using the isdn rlm-group interface configuration command to configure the NFAS groups.

NFAS allows a single D channel to control multiple PRI interfaces. Use of a single D channel to control multiple PRI interfaces
                              frees one B channel on each interface to carry other traffic. A backup D channel can also be configured for use when the primary
                              NFAS D channel fails. When a backup D channel is configured, any hard system failure causes a switchover to the backup D channel
                              and currently connected calls remain connected.

NFAS is supported only with a channelized T1 controller and, as a result, must be ISDN PRI capable. When the channelized T1
                              controllers are configured for ISDN PRI, only the NFAS primary D channel must be configured; its configuration is distributed
                              to all members of the associated NFAS group. Any configuration changes made to the primary D channel will be propagated to
                              all NFAS group members. The primary D-channel interface is the only interface shown after the configuration is written to
                              memory.

The channelized T1 controllers on the router must also be configured for ISDN. The router must connect to either an AT&T 4ESS,
                              Northern Telecom DMS-100 or DMS-250 switch type, or a National ISDN switch type.

The ISDN switch must be provisioned for NFAS. The primary and backup D channels should be configured on separate T1 controllers.
                              The primary, backup, and B-channel members on the respective controllers should have the same configuration as that of the
                              router and ISDN switch. The interface ID assigned to the controllers must match that of the ISDN switch.

You can disable a specified channel or an entire PRI interface, thereby taking it out of service or placing it into one of
                              the other states that is passed in to the switch using the isdn service command.

In the event that a controller belonging to an NFAS group is shut down, all active calls on the controller that is shut down
                              will be cleared (regardless of whether the controller is set to primary, backup, or none), and one of the following events
                              will occur:

If the controller that is shut down is configured as the primary and no backup is configured, all active calls on the group
                                    are cleared.

If the controller that is shut down is configured as the primary, and the active (In service) D channel is the primary and
                                    a backup is configured, then the active D channel changes to the backup controller.

If the controller that is shut down is configured as the primary, and the active D channel is the backup, then the active
                                    D channel remains as the backup controller.

If the controller that is shut down is configured as the backup, and the active D channel is the backup, then the active D
                                    channel changes to the primary controller.

The expected behavior in NFAS when an ISDN D channel (serial interface) is shut down is that ISDN Layer 2 should go down but
                              keep ISDN Layer 1 up, and that the entire interface will go down after the amount of seconds specified for timer T309.

The active D -channel changeover between primary and backup controllers happens only when one of the link fails and not when
                                          the link comes up. The T309 timer is triggered when the changeover takes place.

You must first configure the NFAS primary D channel before configuring the NFAS backup or NFAS none interfaces. If this order
                                          is not followed, this message is displayed:
                                          NFAS backup and NFAS none interfaces are not allowed to be configured without primary. First configure primary D channel.
                                          To remove the NFAS primary D channel after the NFAS backup or NFAS none interfaces are configured, you must remove the NFAS
                                          backup or NFAS none interfaces first, and then remove the NFAS primary D channel.

The voice-dsp keyword is available only on 1-Port and 2-Port HWIC on ISR-G2 (Cisco 2911, Cisco 2921, Cisco 2951, Cisco 3925, Cisco 3925E,
                              Cisco 3945, and Cisco 3945E). This keyword is not available on controller T1 0/1/0 on Voice/WAN(VWIC) interface card.

## Examples

The following example shows how to configure a T1 controller 1/0 for PRI and for the NFAS primary D channel. This primary
                              D channel controls all the B channels in NFAS group 1.

```
controller t1 1/0
 framing esf
 linecode b8zs
 pri-group timeslots 1-24 nfas_d primary nfas_int 0 nfas_group 1
```

The following example shows how to configure an ISDN PRI on T1 slot 1, port 0, and configure voice and data bearer capability
                              on time slots 2 through 6:

```
isdn switch-type primary-4ess
controller t1 1/0
 framing esf
 linecode b8zs
 pri-group timeslots 2-6
```

The following example shows how to configure a standard ISDN PRI interface:

```
! Standard PRI configuration:
controller t1 1
 pri-group timeslots 1-23 nfas_d primary nfas_int 0 nfas_group 0
 exit
! Standard ISDN serial configuration:
interface serial1:23
! Set ISDN parameters:
 isdn T309 4000
 exit
```

The following example shows how to configure a dedicated T1 link for SS7-enabled VoIP:

```
controller T1 1
 pri-group timeslots 1-23 nfas_d primary nfas_int 0 nfas_group 0 
 exit
! In a dedicated configuration, we assume the 24th timeslot will be used by ISDN.
! Serial interface 0:23 is created for configuring ISDN parameters.
interface Serial:24
! The D channel is on the RLM.
 isdn rlm 0
 isdn  T309 4000
 exit
```

The following example shows how to configure a shared T1 link for SS7-enabled VoIP. The rlm-group 0 portion of the pri-group timeslots command releases the ISDN PRI signaling channel.

```
controller T1 1
 pri-group timeslots 1-3 nfas_d primary nfas_int 0 nfas_group 0 rlm-group 0 
 channel group 23 timeslot 24
 end
! D-channel interface is created for configuration of ISDN parameters:
interface Dchannel1
 isdn T309 4000
 end
```

The following example shows how to configure T1 controller 0/2/1 for a PRI with the voice applications option:

```
Router(config)# controller T1 0/2/1 Router(config-controller)# pri-group timeslots 1-24 Router(config-controller)# pri-group timeslots 1-24 voice-dsp
```

### Related Commands

Command

Description

controller

Configures a T1 or E1 controller and enters controller configuration mode.

interface Dchannel

Specifies an ISDN D-channel interface for VoIP applications that require release of the ISDN PRI signaling time slot for RLM
                                          configurations.

interface serial

Specifies a serial interface created on a channelized E1 or channelized T1 controller for ISDN PRI signaling.

isdn rlm-group

Specifies the RLM group number that ISDN will start using.

isdn switch-type

Specifies the central office switch type on the ISDN PRI interface.

isdn timer t309

Changes the value of the T309 timer to clear network connections and releases the B channels when there is no active signaling
                                          channel.

show isdn nfas group

Displays all the members of a specified NFAS group or all NFAS groups.

## primary (gateway accounting file)

To set the primary location for storing the call detail records
                              		  (CDRs) generated for file accounting, use the primary command in gateway accounting file configuration mode. To reset
                              		  to the default, use the no form of this command.

primary { ftp path / filename username username password password | ifs device : filename }

no primary { ftp | ifs }

### Syntax Description

ftp path / filename

Name and location of the file on an external FTP server.
                                          						Filename is limited to 25 characters.

ifs device : filename

Name and location of the file in flash memory or other
                                          						internal file system on this router. Values depend on storage devices available
                                          						on the router, for example flash or slot0. Filename is limited to 25
                                          						characters.

username username

User ID for authentication.

password password

Password user enters for authentication.

### Command Default

Call records are saved to flash:cdr .

### Command Modes

Gateway accounting file configuration (config-gw-accounting-file)

## Command History

Release

Modification

12.4(15)XY

This command was introduced.

12.4(20)T

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

### Usage Guidelines

This command specifies the name and location of the primary file
                              		  where CDRs are stored during the file accounting process. The filename you
                              		  assign is appended with the gateway hostname and time stamp at the time the
                              		  file is created to make the filename unique.

For example, if you specify the filename cdrtest1 on a router with
                              		  the hostname cme-2821, a file is created with the name
                              		  cdrtest1.cme-2821.2007_10_28T22_21_41.000, where 2007_10_28T22_21_41.000 is the
                              		  time that the file was created.

Limit the filename you assign with this command to 25 characters,
                              		  otherwise it could be truncated when the accounting file is created because the
                              		  full filename, including the appended hostname and timestamp, is limited to 63
                              		  characters.

If the file transfer to this primary device fails, the file
                              		  accounting process retries the primary device up to the number of times defined
                              		  by the maximum retry-count command and then switches over to the
                              		  secondary device defined with the secondary command.

To manually switch back to the primary device when it becomes
                              		  available, use the file-acct reset command. The system does not automatically
                              		  switch back to the primary device.

A syslog warning message is generated when flash becomes full.

## Examples

The following example shows the primary location of the accounting
                              		  file is set to an external FTP server and the filename is cdrtest1:

```
gw-accounting file
 primary ftp server1/cdrtest1 username bob password temp
 secondary flash ifs:cdrtest2
 maximum buffer-size  25
 maximum retry-count 3
 maximum fileclose-timer 720
 cdr-format compact
```

The following examples show how the accounting file is named when it
                              		  is created. The router hostname and time stamp are appended to the filename
                              		  that you assign with this command:

```
cme-2821(config)# primary ftp server1/cdrtest1 username bob password temp
```

The name of the accounting file that is created has the following
                              		  format:

cdrtest1.cme-2821.06_04_2007_18_44_51.785

### Related Commands

Command

Description

file-acct flush

Manually flushes the CDRs from the buffer to the accounting
                                          						file.

file-acct reset

Manually switches back to the primary device for file
                                          						accounting.

maximum retry-count

Sets the maximum number of times the router attempts to
                                          						connect to the primary file device before switching to the secondary device.

secondary

Sets the backup location for storing CDRs if the primary
                                          						location becomes unavailable.

## privacy

To set privacy
                              		  support at the global level as defined in RFC 3323, use the privacy command
                              		  in voice service voip sip configuration mode or voice class tenant
                              		  configuration mode. To remove privacy support as defined in RFC 3323, use the no form of this
                              		  command.

privacy { pstn | privacy-option [ critical ]} [system]

no privacy

### Syntax Description

pstn

Requests
                                          						that the privacy service implements a privacy header using the default Public
                                          						Switched Telephone Network (PSTN) rules for privacy (based on information in
                                          						Octet 3a). When selected, this becomes the only valid option.

privacy-option

The
                                          						privacy support options to be set at the global level. The following keywords
                                          						can be specified for the privacy-option argument:

header -- Requests that privacy be enforced for all
                                                							 headers in the Session Initiation Protocol (SIP) message that might identify
                                                							 information about the subscriber.

history -- Requests that the information held in the
                                                							 history-info header is hidden outside the trust domain.

id -- Requests that the Network Asserted Identity
                                                							 that authenticated the user be kept private with respect to SIP entities
                                                							 outside the trusted domain.

session -- Requests that the information held in the
                                                							 session description is hidden outside the trust domain.

user -- Requests that privacy services provide a
                                                							 user-level privacy function.

The
                                                      						  keywords can be used alone, altogether, or in any combination with each other,
                                                      						  but each keyword can be used only once.

critical

(Optional) Requests that the privacy service performs the specified service or
                                          						fail the request.

This
                                                      						  optional keyword is only available after at least one of the privacy-option keywords ( header , history , id , session , or user ) has been
                                                      						  specified and can be used only once per command.

system

Specifies that the privacy support use the global sip-ua value.
                                          						This keyword is available only for the tenant mode to allow it to fallback to
                                          						the global configurations.

### Command Default

Privacy support is
                              		  disabled.

### Command Modes

Voice service voip sip configuration (conf-serv-sip)

Voice class tenant configuration (config-class)

## Command History

Release

Modification

12.4(15)T

This
                                          						command was introduced.

12.4(22)T

The history keyword
                                          						was added to provide support for the history-info header information.

15.6(2)T and IOS XE Denali 16.3.1

This command was modified to include the keyword: system .

Introduced support for YANG models.

### Usage Guidelines

Use the privacy command to instruct the gateway to add a Proxy-Require header set to a value
                              		  supported by RFC 3323 in outgoing SIP request messages.

Use the privacy critical command to instruct the gateway to add a
                              		  Proxy-Require header with the value set to critical. If a user agent sends a
                              		  request to an intermediary that does not support privacy extensions, the
                              		  request fails.

## Examples

The following
                              		  example shows how to set the privacy to PSTN:

```
Router> enable Router# configure terminal Router(config)# voice service voip Router(conf-voi-serv)# sip Router(conf-serv-sip)# privacy pstn
```

The following
                              		  example shows how to set privacy in the voice class tenant configuration mode:

```
Router(config-class)# privacy system
```

### Related Commands

Command

Description

asserted-id

Sets
                                          						the privacy level and enables either PAI or PPI privacy headers in outgoing SIP
                                          						requests or response messages.

calling-info pstn-to-sip

Specifies calling information treatment for PSTN-to-SIP calls.

clid (voice-service-voip)

Passes
                                          						the network-provided ISDN numbers in an ISDN calling party information element
                                          						screening indicator field, removes the calling party name and number from the
                                          						calling-line identifier in voice service voip configuration mode, or allows a
                                          						presentation of the calling number by substituting for the missing Display Name
                                          						field in the Remote-Party-ID and From headers.

voice-class sip privacy

Sets
                                          						privacy support at the dial-peer configuration level as defined in RFC 3323.

## privacy (supplementary-service)

To prevent phones on a shared line from joining active calls, use the privacy command in supplementary-service voice-port configuration mode. To return to the default behavior, use the no form of this command.

privacy { on | off }

no privacy

### Syntax Description

on

Prevents other phones on the shared line to join active calls.

off

Allows other phones on the shared line to join active calls.

### Command Default

The no privacy command implies that a port does not decide on its privacy status. It is not the gateway but the Cisco Unified CM that decides
                              on the privacy status of a port.

### Command Modes

Supplementary-service voice-port configuration mode (config-stcapp-suppl-serv-port)

## Command History

Release

Modification

15.1(3)T

This command was introduced.

### Usage Guidelines

The privacy command enables privacy support on analog endpoints that are connected to Foreign Exchange Station (FXS) ports on a Cisco
                              IOS Voice Gateway, such as a Cisco Integrated Services Router (ISR) or Cisco VG224 Analog Phone Gateway.

Use the privacy command to prevent other phones on the shared line to join active calls.

## Examples

The following example shows how to turn on privacy support on port 2/4 on a Cisco VG224:

```
Router(config)# stcapp supplementary-services Router(config-stcapp-suppl-serv)# port 2/4 Router(config-stcapp-suppl-serv-port)# privacy on Router(config-stcapp-suppl-serv-port)# end
```

### Related Commands

Command

Description

stcapp supplementary-services

Enters supplementary-service configuration mode for configuring STCAPP supplementary-service features on an FXS port.

## privacy-policy

To configure the
                              		  privacy header policy options at the global level, use the privacy-policy command in voice service VoIP SIP configuration mode or voice class tenant
                              		  configuration mode. To disable privacy header policy options, use the no form of this
                              		  command.

privacy-policy { passthru | send-always | strip { diversion | history-info } [system] }

no privacy-policy { passthru | send-always | strip { diversion | history-info } [system] }

### Syntax Description

passthru

Passes
                                          						the privacy values from the received message to the next call leg.

send-always

Passes a
                                          						privacy header with a value of None to the next call leg, if the received
                                          						message does not contain privacy values but a privacy header is required.

strip

Strips
                                          						the diversion or history-info headers received from the next call leg.

diversion

Strips
                                          						the diversion headers received from the next call leg.

history-info

Strips
                                          						the history-info headers received from the next call leg.

system

Specifies that the privacy header policy options use the global
                                          						sip-ua value. This keyword is available only for the tenant mode to allow it to
                                          						fallback to the global configurations.

### Command Default

No privacy-policy
                              		  settings are configured.

### Command Modes

Voice service VoIP SIP configuration (conf-serv-sip)

Voice class tenant configuration (config-class)

## Command History

Release

Modification

12.4(22)YB

This
                                          						command was introduced.

15.0(1)M

This
                                          						command was integrated into Cisco IOS Release 15.0(1)M.

15.1(2)T

This
                                          						command was modified. The strip , diversion , and history-info keywords were added.

15.6(2)T
                                          						and IOS XE Denali 16.3.1

This
                                          						command was modified to include the keyword: system . This
                                          						command is now available under voice class tenants.

Introduced support for YANG models.

### Usage Guidelines

If a received
                              		  message contains privacy values, use the privacy-policy passthru command to ensure that the privacy values
                              		  are passed from one call leg to the next. If the received message does not
                              		  contain privacy values but the privacy header is required, use the privacy-policy send-always command to set the privacy header to
                              		  None and forward the message to the next call leg. If you want to strip the
                              		  diversion and history-info from the headers received from the next call leg,
                              		  use the privacy-policy strip command. You can configure the system to
                              		  support all the options at the same time.

## Examples

The following
                              		  example shows how to enable the pass-through privacy policy:

```
Router> enable Router# configure terminal Router(config)# voice service voip Router(conf-voi-serv)# sip Router(conf-serv-sip)# privacy-policy passthru
```

The following
                              		  example shows how to enable the send-always privacy policy:

```
Router(config-class)# privacy-policy send-always system
```

The following
                              		  example shows how to enable the strip privacy policy:

```
Router> enable Router# configure terminal Router(config)# voice service voip Router(conf-voi-serv)# sip Router(conf-serv-sip)# privacy-policy strip diversion Router(conf-serv-sip)# privacy-policy strip history-info
```

The following
                              		  example shows how to enable the pass-through, send-always privacy, and strip
                              		  policies:

```
Router> enable Router# configure terminal Router(config)# voice service voip Router(conf-voi-serv)# sip Router(conf-serv-sip)# privacy-policy passthru Router(conf-serv-sip)# privacy-policy send-always Router(conf-serv-sip)# privacy-policy strip diversion Router(conf-serv-sip)# privacy-policy strip history-info
```

The following
                              		  example shows how to enable the send-always privacy policy in the voice class
                              		  tenant configuration mode:

### Related Commands

Command

Description

asserted-id

Sets
                                          						the privacy level and enables either PAID or PPID privacy headers in outgoing
                                          						SIP requests or response messages.

voice-class sip privacy-policy

Configures the privacy header policy options at the dial-peer configuration
                                          						level.

## probing interval

To configure the time interval between probing messages sent by the router, use the probing interval command. To reset the time interval to the default number, use the no form of this command.

probing interval [ keepalive | negative ] seconds

### Syntax Description

keepalive

(optional) Configures the time interval between probing messages when the session is in a keepalive state. Range is from 1
                                          to 255 seconds. Default is 5 seconds.

negative

(optional) Configures the time interval between probing messages when the session is in a negative state. Range is from 1
                                          to 20 seconds. Default is 5 seconds.

seconds

Number of seconds between probing message.

### Command Default

The default is 120 seconds between probing messages when the session is in a normal state and 5 seconds between probing messages
                              when the session is in a negative state.

### Command Modes

uc wsapi configuration mode.

## Command History

Release

Modification

15.2(2)T

This command was introduced.

### Usage Guidelines

Use this command to configure the time interval between probing messages sent by the router.

## Examples

The following example sets an interval of 180 seconds for a normal session and 10 seconds when the session is in a negative
                              state.

```
Router(config)# uc wsapi Router(config-uc-wsapi)# probing interval keepalive 180 Router(config-uc-wsapi)# probing interval negative 10
```

### Related Commands

Command

Description

message-exchange

Sets the maximum number of failed message responses before the provider stops sending messages.

probing max-failure

Sets the number of messages that the system will send without receiving a reply before the system unregisters the application.

## probing max-failures

To configure the maximum number of probing messages that the system attempts to send to the application, and the application
                              does not respond to before the system stops the session and unregisters the application, use the probing max-failures command. To reset the maximum to the default number, use the no form of this command.

probing max-failures number

no probing max-failures number

### Syntax Description

number

Maximum number of messages allowed before the system stops the session and unregisters the application. Range is from 1 to
                                          5. Default is 3.

### Command Default

The default is 3.

### Command Modes

uc wsapi configuration mode

## Command History

Release

Modification

15.2(2)T

This command was introduced.

### Usage Guidelines

Use this command to set the maximum number of probing messages sent by the system that the application does not respond to
                              before the system stops the session and unregisters the application session.

## Examples

The following example sets the maximum number of failed messages to 5.

```
Router(config)# uc wsapi Router(config-uc-wsapi)# probing max-failures 5
```

### Related Commands

Command

Description

message-exchange

Sets the maximum number of failed message attempts before the provider stops sending messages.

probing interval

Sets the time interval between probing messages.

## progress_ind

To configure an outbound dial peer on a Cisco IOS voice gateway or Cisco Unified Border Element to override and remove or replace the default progress indicator (PI) in specified call messages, use the progress_ind command in dial peer voice configuration mode. To disable removal or replacement of the default PI in specific call messages,
                              use the no form of this command.

progress_ind { { alert | callproc } { enable pi-number | disable | strip [strip-pi-number] } |  { connect | disconnect | progress | setup } { enable pi-number | disable }}

no progress_ind { alert | callproc | connect | disconnect | progress | setup }

### Syntax Description

alert

Specifies that the configuration applies to call Alert messages.

callproc

Specifies that the configuration applies to Session Initiation Protocol (SIP) 183 Session In Progress (Call_Proceeding) messages.

connect

Specifies that the configuration applies to call Connect messages.

disconnect

Specifies that the configuration applies to call Disconnect messages.

progress

Specifies that the configuration applies to call progress messages.

setup

Specifies that the configuration applies to call setup messages.

enable

Enables user-specified configuration of the progress indicator on the specified call message type.

pi - number

Specifies the PI to be used in place of the default PI. The following are acceptable PI values according to the call message
                                          type:

Alert, Connect, Progress, and SIP 183 Session In Progress messages: 
                                                1, 2, or 8.

Disconnect messages: 8.

Setup messages: 0, 1, or 3.

disable

Disables user-specified configuration of the progress indicator on the specified call message type.

strip

Configures the dial peer to remove all or specific progress indicators in the specified call message type.

This option applies only to call Alert message on POTS dial peers or to call Proceeding messages on VoIP dial peers.

strip-pi - number

(optional) Specifies that only a specific PI is to be removed from the specified call message. The value can be 1, 2, or 8.

### Command Default

This command is disabled on the outbound dial peer and the default progress indicator that is received in the incoming call
                              message is passed intact (it is not intercepted, modified, or removed).

### Command Modes

Dial peer voice configuration (conf-dial-peer)

## Command History

Release

Modification

12.1(3)XI

This command was introduced on the Cisco 2600 series, Cisco 3600 series, Cisco 7200 series, Cisco 7500 series, Cisco MC3810,
                                          Cisco AS5300, and Cisco AS5800.

12.1(5)T

This command was integrated into Cisco IOS Release 12.1(5)T.

12.2(1)

This command was modified. Support was added for setup messages from a POTS dial peer.

12.2(2)XA

This command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T.

15.0(1)XA

This command was modified. Support was added for stripping of PIs in call Alert and SIP 183 Session In Progress (Call_Proceeding)
                                          messages.

15.1(1)T

This command was integrated into Cisco IOS Release 5.1(1)T.

Introduced support for YANG models.

### Usage Guidelines

Before configuring the progress_ind command on an outbound dial peer, you must configure a destination pattern on the dial peer. To configure a destination pattern
                              for an outbound dial peer, use the destination-pattern command in a dial peer voice configuration mode. Once you have set a destination pattern on the dial peer, you can then use
                              the progress_ind command, also in dial peer voice configuration mode, to override and replace or remove the default PI in specific call message
                              types.

You can use the progress_ind command to configure replacement behavior on outbound dial peers on a Cisco IOS voice gateway or CUBE to ensure proper end-to-end signaling of VoIP calls. You can also use this command to configure removal (stripping) of PIs
                              on outbound dial peers on Cisco IOS voice gateways or CUBE s, such as when configuring a Cisco IOS SIP gateway (or SIP-SIP CUBE ) to not generate another SIP 183 Session In Progress messages.

For messages that contain multiple PIs, behavior that is configured using the progress_ind command overrides only the first PI in the message. Also, configuring a replacement PI will not result in an override of
                              the default PI in call progress messages if the Progress message is sent after a backward cut-through event, such as when
                              an Alert message with a PI of 8 was sent before the Progress message.

Use the no progress_ind command in dial peer voice configuration mode to disable PI override configurations on a dial peer on a Cisco IOS voice gateway
                              or CUBE .

## Examples

The following example shows how to configure POTS dial peer 3 to override default PIs in call progress and Connect messages
                              and replace them with a PI of 1:

```
Router(config)# dial-peer voice 3 pots Router(config-dial-peer)# destination-pattern 555 Router(config-dial-peer)# progress_ind progress enable 1 Router(config-dial-peer)# progress_ind connect enable 1
```

The following example configures outbound VoIP dial peer 1 to override SIP 183 Session In Progress messages and to strip out
                              any PIs with a value of 8:

```
Router(config)# dial-peer voice 1 voip Router(config-dial-peer)# destination-pattern 777 Router(config-dial-peer)# progress_ind callproc strip 8
```

### Related Commands

Command

Description

destination-pattern

Specifies the destination pattern (prefix or full E.164 phone number) to be used on an outbound dial peer.

## protocol mode

To configure the Cisco IOS Session Initiation Protocol (SIP) stack, use the protocol mode command in SIP user-agent configuration mode. To disable the configuration, use the no form of this command.

protocol mode { ipv4 | ipv6 | dual-stack [ preference { ipv4 | ipv6 }]}

no protocol mode

### Syntax Description

ipv4

Specifies the IPv4-only mode.

ipv6

Specifies the IPv6-only mode.

dual-stack

Specifies the dual-stack (that is, IPv4 and IPv6) mode.

preference { ipv4 | ipv6

(Optional) Specifies the preferred dual-stack mode, which can be either IPv4 (the default preferred dual-stack mode) or IPv6.

### Command Default

No protocol mode is configured.
                              The Cisco IOS SIP stack operates in IPv4 mode when the no protocol mode or protocol mode ipv4 command is configured.

### Command Modes

SIP user-agent configuration (config-sip-ua)

## Command History

Release

Modification

12.4(22)T

This command was introduced.

15.1(1)T

This command was integrated into Cisco IOS Release 15.1(1)T.

Introduced support for YANG models.

### Usage Guidelines

The protocol mode command is used to configure the Cisco IOS SIP stack in IPv4-only, IPv6-only, or dual-stack mode. For dual-stack mode, the
                              user can (optionally) configure the preferred family, IPv4, or IPv6.

For a particular mode (for example, IPv6-only), the user can configure any address (for example, both IPv4 and IPv6 addresses)
                              and the system will not hide or restrict any commands on the router. SIP chooses the right address for communication based
                              on the configured mode on a per-call basis.

For example, if the domain name system (DNS) reply has both IPv4 and IPv6 addresses and the configured mode is IPv6-only
                              (or IPv4-only), the system discards all IPv4 (or IPv6) addresses and tries the IPv6 (or IPv4) addresses in the order they
                              were received in the DNS reply. If the configured mode is dual-stack, the system first tries the addresses of the preferred
                              family in the order they were received in the DNS reply. If all the addresses fail, the system tries addresses of the other
                              family.

## Examples

The following example configures dual-stack as the protocol mode:

```
Router(config-sip-ua)# protocol mode dual-stack
```

The following example configures IPv6 only as the protocol mode:

```
Router(config-sip-ua)# protocol mode ipv6
```

The following example configures IPv4 only as the protocol mode:

```
Router(config-sip-ua)# protocol mode ipv4
```

The following example configures no protocol mode:

```
Router(config-sip-ua)# no protocol mode
```

### Related Commands

Command

Description

sip ua

Enters SIP user-agent configuration mode.

## protocol rlm port

To configure the RLM port number, use the protocol rlm port RLM configuration command. To disable this function, use the no form of this command.

protocol rlm port port-number

no protocol rlm port port-number

### Syntax Description

port - number

RLM port number. See the table below for the port number choices.

### Command Default

3000

### Command Modes

RLM configuration

## Command History

Release

Modification

11.3(7)

This command was introduced.

### Usage Guidelines

The port number for the basic RLM connection can be reconfigured for the entire RLM group. The table below lists the default
                              RLM port numbers.

Protocol

Port Number

RLM

3000

ISDN

Port[RLM]+1

### Related Commands

Command

Description

clear interface

Resets the hardware logic on an interface.

clear rlm group

Clears all RLM group time stamps to zero.

interface

Defines the IP addresses of the server, configures an interface type, and enters interface configuration mode.

link (RLM)

Specifies the link preference.

retry keepalive

Allows consecutive keepalive failures a certain amount of time before the link is declared down.

server (RLM)

Defines the IP addresses of the server.

show rlm group statistics

Displays the network latency of the RLM group.

show rlm group status

Displays the status of the RLM group.

show rlm group timer

Displays the current RLM group timer values.

shutdown (RLM)

Shuts down all of the links under the RLM group.

timer

Overwrites the default setting of timeout values.

## provider

To configure and
                              		  enable a service provider, use the provider command. To remove the provider, use the no form of this
                              		  command.

provider [ xcc | xsvc | xcdr | xmf ]

no provider [ xcc | xsvc | xcdr | xmf ]

### Syntax Description

xcc

(optional) Enables the XCC service provider.

xsvc

(optional) Enables the XSVC service provider.

xcdr

(optional) Enables the XCDR service provider.

xmf

(optional) Enables the XMF service provider.

### Command Default

No default behavior
                              		  or values.

### Command Modes

uc wsapi configuration mode

uc secure-wsapi

## Command History

Release

Modification

15.2(2)T

This
                                          						command was introduced.

15.3(2)T

xmf keyword was
                                             						  added.

Cisco
                                          						IOS XE Everest 16.6.1

Added
                                          						support for xcc and xsvc service
                                          						providers in secure mode.

### Usage Guidelines

Use this command to
                              		  enable a service provider.

## Examples

The following
                              		  example enables the XCC service provider in nonsecure mode.

```
Router(config)# uc wsapi Router(config-uc-wsapi)# provider xcc Router(config-uc-wsapi-xcc)# no shutdown
```

## Examples

The following
                              		  example enables the XCC service provider in secure mode.

```
Router(config)# uc secure-wsapi Router(config-uc-wsapi)# provider xcc Router(config-uc-wsapi-xcc)# no shutdown
```

### Related Commands

Command

Description

remote-url

Specifies
                                          						the URL of the application.

source-address

Specifies
                                          						the IP address of the provider.

uc wsapi

Enters
                                          						nonsecure Cisco Unified Communication IOS services configuration mode.

uc secure-wsapi

Enters
                                          						secure Cisco Unified Communication IOS services configuration mode.

## proxy h323

To enable the proxy feature on your router, use the proxy h323 command in global configuration mode. To disable the proxy feature, use the no form of this command.

proxy h323

no proxy h323

### Syntax Description

This command has no arguments or keywords.

### Command Default

Disabled

### Command Modes

Global configuration

## Command History

Release

Modification

11.3(2)NA

This command was introduced on the Cisco 2500 series and Cisco 3600 series.

### Usage Guidelines

If the multimedia interface is not enabled using this command or if no gatekeeper is available, starting the proxy allows
                              it to attempt to locate these resources. No calls are accepted until the multimedia interface and the gatekeeper are found.

## Examples

The following example turns on the proxy feature:

```
proxy h323
```

## proxy (media-profile)

To configure IP address or hostname of a WebSocket proxy server in CUBE , use the proxy command in media profile configuration mode. To remove the configuration, use the no form of this command.

proxy { host host port port | ipv4 ip-address port port }

no proxy { host host port port | ipv4 ip-address port port }

### Syntax Description

host

WebSocket proxy server hostname.

ipv4 ip-address

Host IP address of the WebSocket proxy server.

port port

WebSocket proxy server port.

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

If there’s a proxy between the WebSocket speech server and CUBE , the IP address or hostname of the proxy must be configured in media-profile. The proxy command configures the host IP address of the proxy server or the hostname in media profile configuration mode.

If a proxy server is configured, the WebSocket connection must be established with the proxy server itself. It is not possible
                              to establish a direct connection with the speech server.

port port is an optional configuration parameter.

## Examples

The following is a sample configuration for proxy (media-profile) in CUBE :

```
router(cfg-mediaprofile)#proxy ?
host WebSocket proxy server hostname
ip WebSocket proxy server IP address

router(cfg-mediaprofile)#proxy host
router(cfg-mediaprofile)#proxy host abc.com ?
port WebSocket proxy server port
<cr> <cr>

router(cfg-mediaprofile)#proxy host abc.com port ?
<0-65535> proxy server port

router(cfg-mediaprofile)#proxy host abc.com port 3578

router(cfg-mediaprofile)#proxy ipv4 ?
A.B.C.D Specify IP address of proxy server

router(cfg-mediaprofile)#proxy ip 1.1.1.1 ?
port WebSocket proxy server port
<cr> <cr>

router(cfg-mediaprofile)#proxy ip 1.1.1.1 port ?
<0-65535> proxy server port

router(cfg-mediaprofile)#proxy ip 1.1.1.1 port 3456
```

### Related Commands

Command

Description

media profile stream-service

Enables stream service on CUBE .

connection (media-profile)

Configures idle timeout and call threshold for a media profile.

source-ip (media-profile)

Configures local source IP address of a WebSocket connection.

media class

Applies the media class at the dial peer level.

## pulse-digit-detection

To enable pulse digit detection at the beginning of a call, use the pulse-digit-detection command in voice-port configuration mode. To disable pulse digit detection, use the no form of this command.

pulse-digit-detection

no pulse-digit-detection

### Syntax Description

This command has no arguments or keywords.

### Command Default

Pulse digit detection is enabled.

### Command Modes

Voice-port configuration (config-voiceport)

## Command History

Release

Modification

15.0(1)M

This command was introduced.

### Usage Guidelines

Pulse digit detection is disabled at the beginning of a call for any Foreign Exchange Station (FXS) voice port not configured
                              with the no pulse-digit-detection command. By default, pulse digit detection is enabled.

Users should configure the no pulse-digit-detection command only if their equipment generates pulse digits in error when initiating an outbound call.

## Examples

The following example shows how to disable pulse digit detection on voice port 2/0/0:

```
Device> enable Device# configure terminal Device(config)# voice-port 2/0/0 Device(config-voiceport)# no pulse-digit-detection Device(config-voiceport)# end
```

### Related Commands

Command

Description

timing pulse

Specifies the pulse dialing rate for a specified voice port.

| seconds | Periodic interval, in seconds. The range is from 30 to 21600. |
|---|---|

| Release | Modification |
|---|---|
| 15.1(2)T | This command was introduced. |

| Command | Description |
|---|---|
| debug rai | Enables debugging for Resource Allocation Indication (RAI). |
| rai target | Configures the SIP RAI mechanism. |
| resource (voice) | Configures parameters for monitoring resources, use the resource command in voice-class configuration mode. |
| show voice class resource-group | Displays the resource group configuration information for a specific resource group or all resource groups. |
| voice class resource-group | Enters voice-class configuration mode and assigns an identification tag number for a resource group. |

| dns: domain-name | Domain
                                          						name in DNS format. Domain names can be up to 30 characters in length; domain
                                          						names exceeding 30 characters will be truncated. |
|---|---|

| Release | Modification |
|---|---|
| 12.4(9)T | This
                                          						command was introduced. |
| 15.6(2)T
                                          						and IOS XE Denali 16.3.1 | This
                                          						command is now available under voice class tenants. |
| Cisco IOS XE Dublin
                                                17.10.1a | Introduced support for YANG models. |

| Note | Before Software
                                          			 Release 12.4(9)T, hostnames in incoming INVITE-request messages were only
                                          			 validated when they were in IPv4 format; now you can specify hostnames in fully
                                          			 qualified domain name (FQDN) format. |
|---|---|

| phone-context-pattern | Cisco IOS regular expression pattern to match against the phone context field in a SIP or TEL URI. Can be up to 32 characters. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Command | Description |
|---|---|
| destination uri | Specifies the voice class to use for matching the destination URI that is supplied by a voice application. |
| host | Matches a call based on the host field in a SIP URI. |
| incoming uri | Specifies the voice class used to match a VoIP dial peer to the URI of an incoming call. |
| pattern | Matches a call based on the entire SIP or TEL URI. |
| phone number | Matches a call based on the phone number field in a TEL URI. |
| show dialplan incall uri | Displays which dial peer is matched for a specific URI in an incoming voice call. |
| show dialplan uri | Displays which outbound dial peer is matched for a specific destination URI. |
| user-id | Matches a call based on the user-id field in the SIP URI. |
| voice class uri | Creates or modifies a voice class for matching dial peers to calls containing a SIP or TEL URI. |

| phone-number-pattern | Cisco IOS regular expression pattern to match against the phone-number field in a TEL URI. Can be up to 32 characters. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Command | Description |
|---|---|
| debug voice uri | Displays debugging messages related to URI voice classes. |
| destination uri | Specifies the voice class to use for matching the destination URI that is supplied by a voice application. |
| incoming uri | Specifies the voice class used to match a VoIP dial peer to the URI of an incoming call. |
| pattern | Matches a call based on the entire SIP or TEL URI. |
| phone context | Filters out URIs that do not contain a phone-context field that matches the configured pattern. |
| voice class uri | Creates or modifies a voice class for matching dial peers to calls containing a SIP or TEL URI. |

| phone-proxy-name | Name of the specific phone proxy. |
|---|---|
| signal-addr ipv4 ipv4-address | Specifies the SIP signal IPv4 address of
                                       the access side. |
| cucm ipv4 ipv4-address | Specifies the call manager server IPv4 address. |

| Release | Modification |
|---|---|
| 15.3(3)M | This command was introduced. |

| keypad-character | Character string that can be dialed on a telephone keypad (0-9, *, #). Default: 6. Before Cisco IOS Release 12.4(20)YA, this is a single character. In Cisco IOS Release 12.4(20)YA and later releases, the string
                                          can be any of the following: A single character (0-9, *, #) Two digits (00-99) Two to four characters (0-9, *, #) and the leading or ending character must be an asterisk (*) or number sign (#) |
|---|---|

| Release | Modification |
|---|---|
| 12.4(2)T | This command was introduced. |
| 12.4(20)YA | The length of the keypad-character argument was changed to 1 to 4 characters. |
| 12.4(22)T | This command was integrated into Cisco IOS Release 12.4(22)T. |

| Note | This FAC is not supported by Cisco Unified Communications Manager. |
|---|---|

| Command | Description |
|---|---|
| pickup group | Defines a feature code for a feature access code (FAC) to Group Call Pickup from another group. |
| pickup local | Defines a feature code for a feature access code (FAC) to Group Call Pickup from the local group. |
| prefix (stcapp-fac) | Defines the prefix for feature access codes (FACs). |
| show stcapp feature codes | Displays all feature access codes (FACs). |
| stcapp feature access-code | Enables feature access codes (FACs) in STC application and enters STC application feature access-code configuration mode for
                                          changing values of the prefix and features codes from the default. |

| keypad-character | Character string that can be dialed on a telephone keypad (0-9, *, #). Default: 4. Before Cisco IOS Release 12.4(20)YA, this is a single character. In Cisco IOS Release 12.4(20)YA and later releases, the string
                                          can be any of the following: A single character (0-9, *, #) Two digits (00-99) Two to four characters (0-9, *, #) and the leading or ending character must be an asterisk (*) or number sign (#) |
|---|---|

| Release | Modification |
|---|---|
| 12.4(2)T | This command was introduced. |
| 12.4(20)YA | The length of the keypad-character argument was changed to 1 to 4 characters. |
| 12.4(22)T | This command was integrated into Cisco IOS Release 12.4(22)T. |

| Command | Description |
|---|---|
| pickup direct | Defines a feature code for a feature access code (FAC) for Direct Call Pickup of a ringing extension number. |
| pickup local | Defines a feature code for a feature access code (FAC) for Group Call Pickup to pick up an incoming call from the local group. |
| prefix (stcapp-fac) | Defines the prefix for feature access codes (FACs). |
| show stcapp feature codes | Displays all feature access codes (FACs). |
| stcapp feature access-code | Enables feature access codes (FACs) and enters STC application feature access-code configuration mode for changing values
                                          of the prefix and features codes from the default. |

| keypad-character | Character string that can be dialed on a telephone keypad. Default: 3. Before Cisco IOS Release 12.4(20)YA, this is a single character. In Cisco IOS Release 12.5(20)YA and later releases, the string
                                          can be any o the following: A single character (0-9, *, #) Two digits (00-99) Two to four characters (0-9, *, #) and the leading or ending character must be an asterisk (*) or number sign (#) |
|---|---|

| Release | Modification |
|---|---|
| 12.4(2)T | This command was introduced. |
| 12.4(20)YA | The length of the keypad-character argument was changed to 1 to 4 characters. |
| 12.4(22)T | This command was integrated into Cisco IOS Release 12.4(22)T. |

| Command | Description |
|---|---|
| pickup direct | Defines a feature code for a feature access code (FAC) for Direct Call Pickup of a ringing extension number. |
| pickup group | Defines a feature code for a feature access code (FAC) for Group Call Pickup to pick up an incoming call from another group. |
| prefix (stcapp-fac) | Defines the prefix for feature access codes (FACs). |
| show stcapp feature codes | Displays all feature access codes (FACs). |
| stcapp feature access-code | Enables feature access codes (FACs) in STC application and enters STC application feature access-code configuration mode for
                                          changing values of the prefix and features codes from the default. |

| fax milliseconds | Amount of playout delay that the jitter buffer should apply to fax calls, in milliseconds. Range is from 0 to 700. Default
                                          is 300. |
|---|---|
| maximum milliseconds | (Adaptive mode only) Upper limit of the jitter buffer, or the highest value to which the adaptive delay is set, in milliseconds. Range is from 40 to 1700, although this value depends on the type of DSP and how the voice card is configured for codec complexity.
                                          (See the codec complexity command.) Default is 200. If the voice card is configured for high codec complexity, the highest value that can be configured for maximum for compressed codecs is 250 ms. For medium-complexity codec configurations, the highest maximum value is 150 ms. Voice hardware that does not support the voice card complexity configuration (such as analog voice modules for the Cisco 3600
                                          series router) has an upper limit of 200 ms. |
| minimum | (Adaptive mode only) Lower limit of the jitter buffer, or the lowest value to which the adaptive delay is set, in milliseconds.
                                          Values are as follows: default -- 40 ms. Use when there are normal jitter conditions in the network. This is the default. low -- 10 ms. Use when there are low jitter conditions in the network. high -- 40 ms. Use when there are high jitter conditions in the network. |
| nominal milliseconds | Amount of playout delay applied at the beginning of a call by the jitter buffer in the gateway, in milliseconds. In fixed
                                          mode, this is also the maximum size of the jitter buffer throughout the call. Range is from 0 to 1500, although this value depends on the type of DSP and how the voice card is configured for codec complexity.
                                          Default is 60. For non-conference calls when you are using DSPware version 4.1.33 or a later version, the following values are allowed. If the voice card is configured for high codec complexity, the highest value that can be configured for the nominal keyword for compressed codecs is 200 ms. For medium-complexity codec configurations, the highest nominal value is 150 ms. |
| nominal milliseconds (continued) | For conference calls when you are using DSPware version 4.1.33 or a later version, the following values are allowed: The first decoder stream can be assigned a nominal value as high as 200 ms (high-complexity codec) or 150 ms (medium-complexity
                                                codec). Subsequent decoder streams are limited to the highest nominal value of 150 ms (high-complexity) or 80 ms (medium-complexity). When the playout-delay mode is configured for fixed operation and setting the expected jitter buffer size with the nominal
                                          value, the minimum effective value for the playout delay will depend on the codec in use and the configured minimum value. When the playout-delay minimum low is configured the minimum actual jitter buffer size will be 30ms even when setting the nominal to a value lower than 30msec. When the playout-delay minimum default , the minimum jitter buffer size when running in fixed mode will be 60ms. When fixed mode is configured, there is a 10msec added to the nominal value when setting the jitter buffer when configured
                                          for G.729 and a 5ms added using G.711 Voice hardware that does not support the voice-card complexity configuration (such as analog voice modules for the Cisco 3600
                                          series router) has an upper limit of 200 ms for the first decoder stream and 150 ms for subsequent decoder streams. Note With DSPware versions earlier than 4.1.33, the highest nominal value that can be configured is 150 ms for high-complexity
                                                      codec configurations and analog modules. The highest nominal value for medium-complexity codec configurations is 80 ms. | Note | With DSPware versions earlier than 4.1.33, the highest nominal value that can be configured is 150 ms for high-complexity
                                                      codec configurations and analog modules. The highest nominal value for medium-complexity codec configurations is 80 ms. |
| Note | With DSPware versions earlier than 4.1.33, the highest nominal value that can be configured is 150 ms for high-complexity
                                                      codec configurations and analog modules. The highest nominal value for medium-complexity codec configurations is 80 ms. |

| Note | With DSPware versions earlier than 4.1.33, the highest nominal value that can be configured is 150 ms for high-complexity
                                                      codec configurations and analog modules. The highest nominal value for medium-complexity codec configurations is 80 ms. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(1)MA | This command was introduced on the Cisco MC3810. |
| 12.0(7)XK | This command was implemented on the Cisco 2600 series and Cisco 3600 series. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T. |
| 12.1(3)XI | This command was implemented on the Cisco ICS7750. |
| 12.1(5)T | This command was integrated into Cisco IOS Release 12.1(5)T. Support for dial peer configuration mode was added on the following
                                          platforms: Cisco 2600 series, Cisco 3600 series, Cisco 7200 series, Cisco MC3810, Cisco AS5200, Cisco AS5300, Cisco AS5400,
                                          and Cisco AS5800. The minimum keyword was introduced. |
| 12.2(13)T | The fax keyword was introduced. |
| 12.2(13)T8 | DSPware version 4.1.33 was implemented. |

| Command | Description |
|---|---|
| codec complexity | Specifies call density and codec complexity based on the codec standard you are using. |
| playout-delay (voice-port) | Tunes the playout buffer to accommodate packet jitter caused by switches in the WAN. |
| playout - delay mode | Selects fixed or adaptive mode for the jitter buffer on DSPs. |
| show call active voice | Displays active call information for voice calls. |

| fax milliseconds | Amount of playout delay that the jitter buffer should apply to fax calls, in milliseconds. Range is from 0 to 700. Default
                                          is 300. |
|---|---|
| maximum milliseconds | Delay time that the digital signal processor (DSP) allows before starting to discard voice packets, in milliseconds. Range
                                          is from 40 to 320. Default is 160. |
| nominal milliseconds | Initial (and minimum allowed) delay time that the DSP inserts before playing out voice packets, in milliseconds. Range is
                                          from 40 to 200. Default is 80. |

| Release | Modification |
|---|---|
| 11.3(1)MA | This command was introduced on the Cisco MC3810. |
| 12.0(7)XK | This command was implemented on the Cisco 2600 series and Cisco 3600 series. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T. |
| 12.2(13)T | The fax keyword was added. |

| Note | The minimum limit for playout delay is configured using the playout-delay (dial peer) command. |
|---|---|

| Command | Description |
|---|---|
| playout - delay (dial peer) | Tunes the playout buffer on DSPs to accommodate packet jitter caused by switches in the WAN. |
| playout - delay mode | Selects fixed or adaptive mode for playout delay from the jitter buffer on digital signal processors. |
| show call active | Shows active call information for voice calls or fax transmissions in progress. |
| vad | Enables voice activity detection. |

| adaptive | Jitter buffer size and amount of playout delay are adjusted during a call, on the basis of current network conditions. |
|---|---|
| fixed | Jitter buffer size does not adjust during a call; a constant playout delay is added. |

| Release | Modification |
|---|---|
| 12.1(5)T | This command was introduced on the following platforms: Cisco 2600 series, Cisco 3600 series, Cisco MC3810, and Cisco ICS
                                          7750. The no - timestamps keyword was removed. |

| Tip | When there are numerous dial peers to configure, it might be simpler to configure playout delay on a voice port. If conflicting
                                          playout delay values have been configured on a voice port and on a dial peer, the dial-peer configuration takes precedence. |
|---|---|

| Command | Description |
|---|---|
| playout - delay | Tunes the jitter buffer on DSPs for playout delay of voice packets. |
| show call active voice | Displays active call information for voice calls. |

| adaptive | Jitter buffer size and amount of playout delay are adjusted during a call, on the basis of current network conditions. |
|---|---|
| fixed | Jitter buffer size does not adjust during a call; a constant playout delay is added. |

| Release | Modification |
|---|---|
| 11.3(1)MA | This command was introduced on the Cisco MC3810. |
| 12.0(7)XK | This command was implemented on the Cisco 2600 and Cisco 3600 series. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T. |
| 12.1(3)XI | This command was implemented on the Cisco ICS 7750. The keyword mode was introduced. |
| 12.1(5)T | This command was integrated into Cisco IOS Release 12.1(5)T and the no - timestamps keyword was removed. |

| Tip | When there are numerous dial peers to configure, it might be simpler to configure playout delay on a voice port. If conflicting
                                          playout delay values have been configured on a voice port and on a dial peer, the dial-peer configuration takes precedence. |
|---|---|

| Command | Description |
|---|---|
| playout - delay | Tunes the jitter buffer on DSPs for playout delay of voice packets. |
| show call active voice | Displays active call information for voice calls. |

| tag | Media profile police tag. The range is from 1 to 10000. |
|---|---|

| Release | Modification |
|---|---|
| 15.2(2)T | This command was introduced. |

| Command | Description |
|---|---|
| media-class | Applies the media class at the dial peer level. |
| snmp-server enable traps voice media-policy | Enables SNMP media policy voice traps at the global level. |
| snmp enable peer-trap media-policy | Enables SNMP media policy voice traps at the dial peer level. |

| neighbor - port | Port number of the neighbor. This number is used for exchanging Annex G messages. The default port number is 2099. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400
                                          is not included in this release. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. This command is supported on the Cisco AS5300, Cisco AS5350,
                                          and Cisco AS5400 in this release. |

| Command | Description |
|---|---|
| advertise (annex g) | Controls the types of descriptors that the BE advertises to its neighbors. |
| cache | Configures the local BE to cache the descriptors received from its neighbors. |
| id | Configures the local ID of the neighboring BE. |
| query - interval | Configures the interval at which the local BE will query the neighboring BE. |

| slot - number | Number of the slot in the router in which the voice interface card (VIC) is installed. Valid entries are from 0 to 2, depending
                                          on the slot in which the VIC has been installed. |
|---|---|
| port | Voice port number. Valid entries are 0 and 1. |

| slot - number | Number of the slot in the router in which the VIC is installed. Valid entries are from 0 to 3, depending on the slot in which
                                          it has been installed. |
|---|---|
| subunit - number | Subunit on the VIC in which the voice port is located. Valid entries are 0 and 1. |
| port | Voice port number. Valid entries are 0 and 1. |
| slot | Router location in which the voice port adapter is installed. Valid entries are 0 and 3. |
| port | Voice interface card location. Valid entries are 0 and 3. |
| ds0 - group - number | The DS0 group number. Each defined DS0 group number is represented on a separate voice port. This allows you to define individual
                                          DS0s on the digital T1/E1 card. |

| controller - number | The T1 or E1 controller. |
|---|---|
| :D | Indicates the D channel associated with the ISDN PRI. |

| slot/subunit/port | The analog voice port. Valid entries for the slot / subunit / port are as follows: slot -- A router slot in which a voice network module (NM) is installed. Valid entries are router slot numbers for the particular
                                                platform. subunit -- A VIC in which the voice port is located. Valid entries are 0 and 1. (The VIC fits into the voice network module.) port-- An analog voice port number. Valid entries are 0 and 1. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced on the Cisco 3600 series. |
| 11.3(3)T | This command was implemented on the Cisco 2600 series. |
| 11.3(1)MA | This command was implemented on the Cisco MC3810. |
| 12.0(3)T | This command was integrated into Cisco IOS Release 12.0(3)T and implemented on the Cisco AS5300. |
| 12.0(4)T | This command was implemented on the Cisco uBR924. |
| 12.0(7)T | This command was implemented on the Cisco AS5800. |
| 12.2(8)T | This command was implemented on the following platforms: Cisco 1751, Cisco 3725, and Cisco 3745. |
| 12.2(13)T | This command was integrated into Cisco IOS Release 12.2(13)T. This command does not support the extended echo canceller (EC)
                                          feature on the Cisco AS5300 or the Cisco AS5800. |
| 12.4(22)T | Support for IPv6 was added. |

| Note | This command does not support the extended EC feature on the Cisco AS5300. |
|---|---|

| Command | Description |
|---|---|
| prefix | Specifies the prefix of the dialed digits for a dial peer. |

| port - number | Voice port or DS0-group number to be used as an MGCP endpoint associated with an MGCP profile. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced as the voice - port (MGCP profile) command. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. |
| 12.2(8)T | This command was renamed the port (MGCP profile) command. |

| Command | Description |
|---|---|
| mgcp | Starts and allocates resources for the MGCP daemon. |
| mgcp profile | Initiates MGCP profile mode to create and configure a named MGCP profile associated with one or more endpoints or to configure
                                          the default profile. |

| port | Location of port in Cisco ISR or Cisco VG224 Analog Phone Gateway. Syntax is platform-dependent; type ? to determine. |
|---|---|

| Release | Modification |
|---|---|
| 12.4(20)YA | This command was introduced. |
| 12.4(22)T | This command was integrated into Cisco IOS Release 12.4(22)T. |

| Command | Description |
|---|---|
| hold-resume | Enables Hold/Resume in Feature mode on the port being configured. |

| interface | Serial interface to which the local codec is connected. Valid entries are 0 and 1. |
|---|---|

| Release | Modification |
|---|---|
| 12.0(5)XK | This command was introduced for ATM video dial-peer configuration on the Cisco MC3810. |
| 12.0(7)T | This command was integrated into Cisco IOS Release 12.0(7)T. |

| Command | Description |
|---|---|
| port signal | Specifies the slot location of the VDM and the port location of the EIA/TIA-366 interface for signaling. |
| show dial-peer video | Displays dial-peer configuration. |

| min-port | First port number of the port range. |
|---|---|
| max-port | Last port number of the port range. |

| Release | Modification |
|---|---|
| 15.3(3)M | This command was introduced. |

| slot/ | Slot location of the VDM. Valid values are 1 and 2. |
|---|---|
| port | Port location of the EIA/TIA-366 interface. |

| Release | Modification |
|---|---|
| 12.0(5)XK | This command was introduced for ATM video dial-peer
                                          						configuration on the Cisco MC3810. |
| 12.0(7)T | This command was integrated into Cisco IOS Release
                                          						12.0(7)T. |

| Command | Description |
|---|---|
| port media | Specifies the serial interface to which the local video
                                          						codec is connected. |
| show dial-peer video | Displays dial-peer configuration. |

| local | Enable call waiting on a local basis for the routers. |
|---|---|
| remote | Rely on the network provider service instead of the router to hold calls. |

| Release | Modification |
|---|---|
| 12.1.(2)XF | This command was introduced on the Cisco 800 series. |

| Command | Description |
|---|---|
| call-waiting | Configures call waiting for a specific dial peer. |
| show pots status | Displays the settings of the physical characteristics and other information on the telephone interfaces of a Cisco 800 series
                                          router. |

| country | Country in which your router is located. |
|---|---|

| Release | Modification |
|---|---|
| 12.0(3)T | This command was introduced on the Cisco 800 series. |

| Command | Description |
|---|---|
| pots dialing - method | Specifies how the Cisco 800 series router collects and sends digits dialed on your connected telephones, fax machines, or
                                          modems. |
| pots disconnect - supervision | Specifies how a Cisco 800 series router notifies the connected telephones, fax machines, or modems when the calling party
                                          has disconnected. |
| pots disconnect - time | Specifies the interval in which the disconnect method is applied if telephones, fax machines, or modems connected to a Cisco
                                          800 series router fail to detect that a calling party has disconnected. |
| pots distinctive - ring - guard - time | Specifies the delay in which a telephone port can be rung after a previous call is disconnected (Cisco 800 series routers). |
| pots encoding | Specifies the PCM encoding scheme for telephones, fax machines, or modems connected to a Cisco 800 series router. |
| pots line - type | Specifies the impedance of telephones, fax machines, or modems connected to a Cisco 800 series router. |
| pots ringing - freq | Specifies the frequency at which telephones, fax machines, or modems connected to a Cisco 800 series router ring. |
| pots silence - time | Specifies the interval of silence after a calling party disconnects (Cisco 800 series router). |
| pots tone - source | Specifies the source of dial, ringback, and busy tones for telephones, fax machines, or modems connected to a Cisco 800 series
                                          router. |
| show pots status | Displays the settings of the telephone port physical characteristics and other information on the telephone interfaces on
                                          a Cisco 800 series router. |

| overlap | The router sends each digit dialed in a separate message. |
|---|---|
| enblock | The router collects all digits dialed and sends the digits in one message. |

| Release | Modification |
|---|---|
| 12.0(3)T | This command was introduced on the Cisco 800 series. |

| Command | Description |
|---|---|
| pots country | Configures telephones, fax machines, or modems connected to a Cisco 800 series router to use country-specific default settings
                                          for each physical characteristic. |
| pots disconnect - supervision | Specifies how a Cisco 800 series router notifies the connected telephones, fax machines, or modems when the calling party
                                          has disconnected. |
| pots disconnect - time | Specifies the interval in which the disconnect method is applied if telephones, fax machines, or modems connected to a Cisco
                                          800 series router fail to detect that a calling party has disconnected. |
| pots distinctive - ring - guard - time | Specifies the delay in which a telephone port can be rung after a previous call is disconnected (Cisco 800 series routers). |
| pots encoding | Specifies the PCM encoding scheme for telephones, fax machines, or modems connected to a Cisco 800 series router. |
| pots line - type | Specifies the impedance of telephones, fax machines, or modems connected to a Cisco 800 series router. |
| pots ringing - freq | Specifies the frequency at which telephones, fax machines, or modems connected to a Cisco 800 series router ring. |
| pots silence - time | Specifies the interval of silence after a calling party disconnects (Cisco 800 series router). |
| pots tone - source | Specifies the source of dial, ringback, and busy tones for telephones, fax machines, or modems connected to a Cisco 800 series
                                          router. |
| show pots status | Displays the settings of the telephone port physical characteristics and other information on the telephone interfaces on
                                          a Cisco 800 series router. |

| osi | Open switching interval (OSI) is the duration for which DC voltage applied between tip and ring conductors of a telephone
                                          port is removed. |
|---|---|
| reversal | Polarity reversal of tip and ring conductors of a telephone port. |

| Release | Modification |
|---|---|
| 12.0(3)T | This command was introduced on the Cisco 800 series. |

| Command | Description |
|---|---|
| pots country | Configures telephones, fax machines, or modems connected to a Cisco 800 series router to use country-specific default settings
                                          for each physical characteristic. |
| pots dialing - method | Specifies how the Cisco 800 series router collects and sends digits dialed on your connected telephones, fax machines, or
                                          modems. |
| pots disconnect - time | Specifies the interval in which the disconnect method is applied if telephones, fax machines, or modems connected to a Cisco
                                          800 series router fail to detect that a calling party has disconnected. |
| pots distinctive - ring - guard - time | Specifies the delay in which a telephone port can be rung after a previous call is disconnected (Cisco 800 series routers). |
| pots encoding | Specifies the PCM encoding scheme for telephones, fax machines, or modems connected to a Cisco 800 series router. |
| pots line - type | Specifies the impedance of telephones, fax machines, or modems connected to a Cisco 800 series router. |
| pots ringing - freq | Specifies the frequency at which telephones, fax machines, or modems connected to a Cisco 800 series router ring. |
| pots silence - time | Specifies the interval of silence after a calling party disconnects (Cisco 800 series router). |
| pots tone - source | Specifies the source of dial, ringback, and busy tones for telephones, fax machines, or modems connected to a Cisco 800 series
                                          router. |
| show pots status | Displays the settings of the telephone port physical characteristics and other information on the telephone interfaces on
                                          a Cisco 800 series router. |

| interval | Interval, in milliseconds. Range is from 50 to 2000. |
|---|---|

| Release | Modification |
|---|---|
| 12.0(3)T | This command was introduced on the Cisco 800 series. |

| Command | Description |
|---|---|
| pots country | Configures telephones, fax machines, or modems connected to a Cisco 800 series router to use country-specific default settings
                                          for each physical characteristic. |
| pots dialing - method | Specifies how the Cisco 800 series router collects and sends digits dialed on your connected telephones, fax machines, or
                                          modems. |
| pots disconnect - supervision | Specifies how a Cisco 800 series router notifies the connected telephones, fax machines, or modems when the calling party
                                          has disconnected. |
| pots distinctive - ring - guard - time | Specifies the delay in which a telephone port can be rung after a previous call is disconnected (Cisco 800 series routers). |
| pots encoding | Specifies the PCM encoding scheme for telephones, fax machines, or modems connected to a Cisco 800 series router. |
| pots line - type | Specifies the impedance of telephones, fax machines, or modems connected to a Cisco 800 series router. |
| pots ringing - freq | Specifies the frequency at which telephones, fax machines, or modems connected to a Cisco 800 series router ring. |
| pots silence - time | Specifies the interval of silence after a calling party disconnects (Cisco 800 series router). |
| pots tone - source | Specifies the source of dial, ringback, and busy tones for telephones, fax machines, or modems connected to a Cisco 800 series
                                          router. |
| show pots status | Displays the settings of the telephone port physical characteristics and other information on the telephone interfaces on
                                          a Cisco 800 series router. |

| milliseconds | Delay, in milliseconds. Range is from 0 to 1000. |
|---|---|

| Release | Modification |
|---|---|
| 12.0(3)T | This command was introduced on the Cisco 800 series. |

| Command | Description |
|---|---|
| pots country | Configures telephones, fax machines, or modems connected to a Cisco 800 series router to use country-specific default settings
                                          for each physical characteristic. |
| pots dialing - method | Specifies how the Cisco 800 series router collects and sends digits dialed on your connected telephones, fax machines, or
                                          modems. |
| pots disconnect - supervision | Specifies how a Cisco 800 series router notifies the connected telephones, fax machines, or modems when the calling party
                                          has disconnected. |
| pots disconnect - time | Specifies the interval in which the disconnect method is applied if telephones, fax machines, or modems connected to a Cisco
                                          800 series router fail to detect that a calling party has disconnected. |
| pots encoding | Specifies the PCM encoding scheme for telephones, fax machines, or modems connected to a Cisco 800 series router. |
| pots line - type | Specifies the impedance of telephones, fax machines, or modems connected to a Cisco 800 series router. |
| pots ringing - freq | Specifies the frequency at which telephones, fax machines, or modems connected to a Cisco 800 series router ring. |
| pots silence - time | Specifies the interval of silence after a calling party disconnects (Cisco 800 series router). |
| pots tone - source | Specifies the source of dial, ringback, and busy tones for telephones, fax machines, or modems connected to a Cisco 800 series
                                          router. |
| ring | Sets up a distinctive ring for telephones, fax machines, or modems connected to a Cisco 800 series router. |
| show pots status | Displays the settings of the telephone port physical characteristics and other information on the telephone interfaces on
                                          a Cisco 800 series router. |

| alaw | A-law. International Telecommunication Union Telecommunication Standardization Section (ITU-T) PCM encoding scheme used to
                                          represent analog voice samples as digital values. |
|---|---|
| ulaw | Mu-law. North American PCM encoding scheme used to represent analog voice samples as digital values. |

| Release | Modification |
|---|---|
| 12.0(3)T | This command was introduced on the Cisco 800 series. |

| Command | Description |
|---|---|
| pots country | Configures telephones, fax machines, or modems connected to a Cisco 800 series router to use country-specific default settings
                                          for each physical characteristic. |
| pots dialing - method | Specifies how the Cisco 800 series router collects and sends digits dialed on your connected telephones, fax machines, or
                                          modems. |
| pots disconnect - supervision | Specifies how a Cisco 800 series router notifies the connected telephones, fax machines, or modems when the calling party
                                          has disconnected. |
| pots disconnect - time | Specifies the interval in which the disconnect method is applied if telephones, fax machines, or modems connected to a Cisco
                                          800 series router fail to detect that a calling party has disconnected. |
| pots distinctive - ring - guard - time | Specifies the delay in which a telephone port can be rung after a previous call is disconnected (Cisco 800 series routers). |
| pots line - type | Specifies the impedance of telephones, fax machines, or modems connected to a Cisco 800 series router. |
| pots ringing - freq | Specifies the frequency at which telephones, fax machines, or modems connected to a Cisco 800 series router ring. |
| pots silence - time | Specifies the interval of silence after a calling party disconnects (Cisco 800 series router). |
| pots tone - source | Specifies the source of dial, ringback, and busy tones for telephones, fax machines, or modems connected to a Cisco 800 series
                                          router. |
| show pots status | Displays the settings of the telephone port physical characteristics and other information on the telephone interfaces on
                                          a Cisco 800 series router. |

| keypad | Gives forwarding control to the Euro-ISDN switch. |
|---|---|
| functional | Gives forwarding control to the router. If you select this method, use the dual-tone multifrequency (DTMF) keypad commands
                                          listed in the table below to configure call-forwarding service. |

| Release | Modification |
|---|---|
| 12.2(2)T | This command was introduced. |

| Task | DTMF Keypad Command 1 |
|---|---|
| Activate CFU | **21* number # |
| Deactivate CFU | #21# |
| Activate CFNR | **61* number # |
| Deactivate CFNR | #61# |
| Activate CFB | **67* number # |
| Deactivate CFB | #67# |

| Command | Description |
|---|---|
| pots prefix filter | Sets a filter that prevents a dial prefix from being added to a dialed number when the digits in the dialed number match
                                          the filter. |
| pots prefix number | Sets a prefix to be added to a called telephone number for analog or modem calls. |

| type1 | Runs at 600 ohms. |
|---|---|
| type2 | Runs at 900 ohms. |
| type3 | Runs at 300 or 400 ohms. |

| Release | Modification |
|---|---|
| 12.0(3)T | This command was introduced on the Cisco 800 series. |

| Command | Description |
|---|---|
| pots country | Configures telephones, fax machines, or modems connected to a Cisco 800 series router to use country-specific default settings
                                          for each physical characteristic. |
| pots dialing - method | Specifies how the Cisco 800 series router collects and sends digits dialed on your connected telephones, fax machines, or
                                          modems. |
| pots disconnect - supervision | Specifies how a Cisco 800 series router notifies the connected telephones, fax machines, or modems when the calling party
                                          has disconnected. |
| pots disconnect - time | Specifies the interval in which the disconnect method is applied if telephones, fax machines, or modems connected to a Cisco
                                          800 series router fail to detect that a calling party has disconnected. |
| pots distinctive - ring - guard - time | Specifies the delay in which a telephone port can be rung after a previous call is disconnected (Cisco 800 series routers). |
| pots encoding | Specifies the PCM encoding scheme for telephones, fax machines, or modems connected to a Cisco 800 series router. |
| pots ringing - freq | Specifies the frequency at which telephones, fax machines, or modems connected to a Cisco 800 series router ring. |
| pots silence - time | Specifies the interval of silence after a calling party disconnects (Cisco 800 series router). |
| pots tone - source | Specifies the source of dial, ringback, and busy tones for telephones, fax machines, or modems connected to a Cisco 800 series
                                          router. |
| show pots status | Displays the settings of the telephone port physical characteristics and other information on the telephone interfaces on
                                          a Cisco 800 series router. |

| number | Prefix filter numbers, up to a maximum of eight characters. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)T | This command was introduced on the Cisco 803 and Cisco 804. |

| Command | Description |
|---|---|
| pots forwarding - method | Configures the type of forwarding method to be used for Euro-ISDN (formerly NET3) switches. |
| pots prefix number | Sets a prefix to be added to a called telephone number for analog or modem calls. |

| number | Prefix, up to a maximum of five digits. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)T | This command was introduced on the Cisco 803 and Cisco 804. |

| Command | Description |
|---|---|
| pots prefix filter | Sets a filter that prevents a dial prefix from being added to a dialed number when the digits in the dialed number match the
                                          filter. |

| 20Hz | Connected devices ring at 20 Hz. |
|---|---|
| 25Hz | Connected devices ring at 25 Hz. |
| 50Hz | Connected devices ring at 50 Hz. |

| Release | Modification |
|---|---|
| 12.0(3)T | This command was introduced on the Cisco 800 series. |

| Command | Description |
|---|---|
| pots country | Configures telephones, fax machines, or modems connected to a Cisco 800 series router to use country-specific default settings
                                          for each physical characteristic. |
| pots dialing - method | Specifies how the Cisco 800 series router collects and sends digits dialed on your connected telephones, fax machines, or
                                          modems. |
| pots disconnect - supervision | Specifies how a Cisco 800 series router notifies the connected telephones, fax machines, or modems when the calling party
                                          has disconnected. |
| pots disconnect - time | Specifies the interval in which the disconnect method is applied if telephones, fax machines, or modems connected to a Cisco
                                          800 series router fail to detect that a calling party has disconnected. |
| pots distinctive - ring - guard - time | Specifies the delay in which a telephone port can be rung after a previous call is disconnected (Cisco 800 series routers). |
| pots encoding | Specifies the PCM encoding scheme for telephones, fax machines, or modems connected to a Cisco 800 series router. |
| pots line - type | Specifies the impedance of telephones, fax machines, or modems connected to a Cisco 800 series router. |
| pots silence - time | Specifies the interval of silence after a calling party disconnects (Cisco 800 series router). |
| pots tone - source | Specifies the source of dial, ringback, and busy tones for telephones, fax machines, or modems connected to a Cisco 800 series
                                          router. |
| show pots status | Displays the settings of the telephone port physical characteristics and other information on the telephone interfaces on
                                          a Cisco 800 series router. |

| interval | Number from 0 to 10 (seconds). |
|---|---|

| Release | Modification |
|---|---|
| 12.0(3)T | This command was introduced on the Cisco 800 series. |

| Command | Description |
|---|---|
| pots country | Configures telephones, fax machines, or modems connected to a Cisco 800 series router to use country-specific default settings
                                          for each physical characteristic. |
| pots dialing - method | Specifies how the Cisco 800 series router collects and sends digits dialed on your connected telephones, fax machines, or
                                          modems. |
| pots disconnect - supervision | Specifies how a Cisco 800 series router notifies the connected telephones, fax machines, or modems when the calling party
                                          has disconnected. |
| pots disconnect - time | Specifies the interval in which the disconnect method is applied if telephones, fax machines, or modems connected to a Cisco
                                          800 series router fail to detect that a calling party has disconnected. |
| pots distinctive - ring - guard - time | Specifies the delay in which a telephone port can be rung after a previous call is disconnected (Cisco 800 series routers). |
| pots encoding | Specifies the PCM encoding scheme for telephones, fax machines, or modems connected to a Cisco 800 series router. |
| pots line - type | Specifies the impedance of telephones, fax machines, or modems connected to a Cisco 800 series router. |
| pots ringing - freq | Specifies the frequency at which telephones, fax machines, or modems connected to a Cisco 800 series router ring. |
| pots tone - source | Specifies the source of dial, ringback, and busy tones for telephones, fax machines, or modems connected to a Cisco 800 series
                                          router. |
| show pots status | Displays the settings of the telephone port physical characteristics and other information on the telephone interfaces on
                                          a Cisco 800 series router. |

| local | Router supplies the tones. |
|---|---|
| remote | Telephone switch supplies the tones. |

| Release | Modification |
|---|---|
| 12.0(3)T | This command was introduced on the Cisco 800 series. |

| Command | Description |
|---|---|
| pots country | Configures telephones, fax machines, or modems connected to a Cisco 800 series router to use country-specific default settings
                                          for each physical characteristic |
| pots dialing - method | Specifies how the Cisco 800 series router collects and sends digits dialed on your connected telephones, fax machines, or
                                          modems. |
| pots disconnect - supervision | Specifies how a Cisco 800 series router notifies the connected telephones, fax machines, or modems when the calling party
                                          has disconnected. |
| pots disconnect - time | Specifies the interval in which the disconnect method is applied if telephones, fax machines, or modems connected to a Cisco
                                          800 series router fail to detect that a calling party has disconnected. |
| pots distinctive - ring - guard - time | Specifies the delay in which a telephone port can be rung after a previous call is disconnected (Cisco 800 series routers). |
| pots encoding | Specifies the PCM encoding scheme for telephones, fax machines, or modems connected to a Cisco 800 series router. |
| pots line - type | Specifies the impedance of telephones, fax machines, or modems connected to a Cisco 800 series router. |
| pots ringing - freq | Specifies the frequency at which telephones, fax machines, or modems connected to a Cisco 800 series router ring. |
| pots silence - time | Specifies the interval of silence after a calling party disconnects (Cisco 800 series router). |
| show pots status | Displays the settings of the telephone port physical characteristics and other information on the telephone interfaces on
                                          a Cisco 800 series router. |

| seconds | Delay, in seconds, before signaling begins. Range is from 0 to 10. Default is 1. |
|---|---|

| Release | Modification |
|---|---|
| 11.(7)T | This command was introduced on the Cisco 3600 series. |
| 12.0(2)T | This command was integrated into Cisco IOS Release 12.0(2)T. |

| Command | Description |
|---|---|
| timeouts initial | Configures the initial digit timeout value for a specified voice port. |
| timing delay - duration | Configures delay dial signal duration for a specified voice port. |

| value | An integer from 0 to 10. A lower number indicates a higher preference. The default is 0, which is the highest preference. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(1)MA | This command was introduced on the Cisco MC3810. |
| 12.0(3)T | This command was integrated into Cisco IOS Release 12.0(3)T and implemented on the Cisco 2600 series and Cisco 3600 series
                                          routers. |
| 12.0(4)T | This command was modified to support Voice over Frame Relay(VoFR) dial peers on the Cisco 2600 series and Cisco 3600 series
                                          routers. |
| 15.1(3)T | This command was modified. Support for matching different pattern types was modified. |
| Cisco IOS XE Amsterdam 17.2.1r | Introduced support for YANG models. |

| Note | If POTS and voice-network peers are mixed in the same hunt group, the POTS dial peers must have priority over the voice-network
                                          dial peers. |
|---|---|

| Command | Description |
|---|---|
| called-number (dial-peer) | Enables an incoming VoFR call leg to get bridged to the correct POTS call leg when using a static FRF.11 trunk connection. |
| codec (dial-peer) | Specifies the voice coder rate of speech for a Voice over Frame Relay dial peer. |
| cptone | Specifies a regional analog voice interface-related tone, ring, and cadence setting. |
| destination-pattern | Specifies the prefix, the full E.164 telephone number, or an ISDN directory number (depending on the dial plan) to be used
                                          for a dial peer. |
| destination uri | Specifies the voice class used to match a dial peer to the destination uniform resource identifier (URI). |
| dtmf-relay (Voice over Frame Relay) | Enables the generation of FRF.11 Annex A frames for a dial peer. |
| session protocol | Establishes a session protocol for calls between the local and remote routers via the packet network. |
| session target | Specifies a network-specific address for a specified dial peer or destination gatekeeper. |
| signal-type | Sets the signaling type to be used when connecting to a dial peer. |

| Release | Modification |
|---|---|
| 12.4(4)XC | This command was introduced. |
| 12.4(9)T | This command was integrated into Cisco IOS Release 12.4(9)T. |

| Command | Description |
|---|---|
| isdn integrate all | Enables integrated mode on an ISDN PRI interface. |
| max-calls | Sets the maximum number of calls that a trunk group can handle. |
| preemption guard timer | Defines time for a DDR call and allows time to clear the last call from the channel. |
| preemption level | Sets the preemption level of the selected outbound dial peer. Voice calls can be preempted by a DDR call with higher preemption
                                          level. |
| preemption tone timer | Defines the expiry time for the preemption tone for the outgoing call being preempted by a DDR backup call. |

| value | Number, in milliseconds for the preemption guard timer. The range is 60 to 500. The default is 60. |
|---|---|

| Release | Modification |
|---|---|
| 12.4(4)XC | This command was introduced. |
| 12.4(9)T | This command was integrated into Cisco IOS Release 12.4(9)T. |

| Command | Description |
|---|---|
| isdn integrate all | Enables integrated mode on an ISDN PRI interface. |
| max-calls | Sets the maximum number of calls that a trunk group can handle. |
| preemption enable | Enables preemption capabilities on a trunk group. |
| preemption level | Sets the preemption level of the selected outbound dial-peer. Voice calls can be preempted by a DDR call with higher preemption
                                          level. |
| preemption tone timer | Sets the expiry time for the preemption tone for the outgoing call being preempted by a DDR backup call. |

| flash-override | Sets the precedence for voice calls to preemption level 0 (highest). |
|---|---|
| flash | Sets the precedence for voice calls to preemption level 1. |
| immediate | Sets the precedence for voice calls to preemption level 2. |
| priority | Sets the precedence for voice calls to preemption level 3. |
| routine | Sets the precedence for voice calls to preemption level 4 (lowest). This is the default. |

| Release | Modification |
|---|---|
| 12.4(4)XC | This command was introduced. |
| 12.4(9)T | This command was integrated into Cisco IOS Release 12.4(9)T. |

| Command | Description |
|---|---|
| dialer preemption level | Sets the precedence for voice calls to be preempted by a DDR call for the dialer map. |
| isdn integrate all | Enables integrated mode on an ISDN PRI interface. |
| max-calls | Sets the maximum number of calls that a trunk group can handle. |
| preemption enable | Enables preemption capabilities on a trunk group. |
| preemption guard timer | Defines time for a DDR call and allows time to clear the last call from the channel. |
| preemption tone timer | Defines the expiry time for the preemption tone for the outgoing call being preempted by a DDR backup call. |

| seconds | Length of preemption tone, in seconds. Range: 4 to 30. Default: 10. |
|---|---|

| Release | Modification |
|---|---|
| 12.4(4)XC | This command was introduced. |
| 12.4(9)T | This command was integrated into Cisco IOS Release 12.4(9)T. |

| Command | Description |
|---|---|
| isdn integrate all | Enables integrated mode on an ISDN PRI interface. |
| max-calls | Sets the maximum number of calls that a trunk group can handle. |
| preemption enable | Enables preemption capabilities on a trunk group. |
| preemption level | Sets the preemption level of the selected outbound dial peer. Voice calls can be preempted by a DDR call with higher preemption
                                          level. |

| string | Integers that represent the prefix of the telephone number associated with the specified dial peer. Valid values are 0 through
                                          9 and a comma (,). Use a comma to include a pause in the prefix. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced on the Cisco 3600 series. |
| 12.0(4)XJ | This command was implemented on the Cisco AS5300. It and modified for store-and-forward fax. |
| 12.1(1)T | This command was integrated into Cisco IOS Release 12.1(1)T. |
| 12.2(4)T | This command was implemented on the Cisco 1750. |
| 12.2(8)T | This command was implemented on the following platforms: Cisco 1751, Cisco 2600 series, Cisco 3600 series, Cisco 3725, and
                                          Cisco 3745. |
| 12.2(13)T | This command was supported in Cisco IOS Release 12.2(13)T and implemented on the Cisco 2600XM, Cisco ICS7750, and Cisco VG200. |

| Command | Description |
|---|---|
| answer - address | Specifies the full E.164 telephone number to be used to identify the dial peer of an incoming call. |
| destination - pattern | Specifies either the prefix or the full E.164 telephone number to be used for a dial peer. |

| prefix * | Prefix for which BEs should be queried. |
|---|---|
| seq | (Optional) Queries are sent out to the neighboring BEs
                                          						sequentially. |
| blast | (Optional) Queries are sent out to the neighboring BEs
                                          						simultaneously. |

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced. |
| 12.2(4)T | This command was integrated into Cisco IOS Release
                                          						12.2(4)T. Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400 is not
                                          						included in this release. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(11)T | This command was integrated into Cisco IOS Release
                                          						12.2(11)T. |

| Command | Description |
|---|---|
| h323 - annexg | Enables the BE on the gatekeeper and enters border element
                                          						configuration mode. |

| prefix-string | String of one to five characters that can be dialed on a telephone keypad. String must start with an asterisk (*) or a number
                                          sign (#). Default is **. |
|---|---|

| Release | Modification |
|---|---|
| 12.4(2)T | This command was introduced. |

| Command | Description |
|---|---|
| call forward all | Defines the feature code in the feature access code (FAC) for forwarding all calls. |
| call forward cancel | Defines the feature code in the feature access code (FAC) for cancelling Call Forward All. |
| pickup direct | Defines the feature code in the feature access code (FAC) for Directed Call Pickup. |
| pickup group | Defines the feature code in the feature access code (FAC) for call pickup from another group. |
| pickup local | Defines the feature code in the feature access code (FAC) for call pickup from the local group. |
| show stcapp feature codes | Displays all feature access codes (FACs) and all feature speed-dials (FSDs). |
| stcapp feature access-code | Enables feature access codes (FACs) in STC application and enters STC application feature access-code configuration mode for
                                          changing values of the prefix and features codes from the default. |

| prefix-string | String of one to five characters (0-9, *, #) that can be dialed on a telephone keypad. String must begin with asterisk (*)
                                          or number sign(#). Default is *. |
|---|---|

| Release | Modification |
|---|---|
| 12.4(2)T | This command was introduced. |

| Command | Description |
|---|---|
| redial | Defines an speed-dial code to dial again the most-recently dialed number on this phone line. |
| show stcapp feature codes | Displays all feature access codes (FACs) and all feature speed-dials (FSDs). |
| speed dial | Designates a range of feature speed-dials (FSDs) in STC application. |
| stcapp feature access-code | Enables feature speed-dials (FSDs) in STC application and enters STC application feature speed-dial configuration mode for
                                          changing values of the prefix and speed-dial codes from the default. |
| voicemail (stcapp-fsd) | Defines an speed-dial code to dial the voice-mail number. |

| sip-server | (Optional) Adds SIP server information to the Route header. |
|---|---|
| service-route | Adds the
                                          						Service-Route information to the Route header. |
| system | Specifies that the preloaded route support for VoIP Session
                                          						Initiation Protocol (SIP) calls use the global sip-ua value. This keyword is
                                          						available only for the tenant mode to allow it to fallback to the global
                                          						configurations. |

| Release | Modification |
|---|---|
| 12.4(22)YB | This
                                          						command was introduced. |
| 15.0(1)M | This
                                          						command was integrated into Cisco IOS Release 15.0(1)M. |
| 15.6(2)T and IOS XE Denali 16.3.1 | This command was modified to include the keyword: system . |

| Command | Description |
|---|---|
| sip | Enters
                                          						SIP configuration mode from voice-service VoIP configuration mode. |
| voice - class preloaded-route | Enables
                                          						preloaded route support for dial-peer SIP calls. |

| Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XJ | Cisco Unified CME 4.1 | This command was introduced. |
| 12.4(15)T | Cisco Unified CME 4.1 | This command was integrated into Cisco IOS Release 12.4(15)T. |

| Command | Description |
|---|---|
| allow watch | Allows a directory number on a phone registered to Cisco Unified CME to be watched in a presence service. |
| debug presence | Displays debugging information about the presence service. |
| max-subscription | Sets the maximum number of concurrent watch sessions that are allowed. |
| presence enable | Allows the router to accept incoming presence requests. |
| server | Specifies the IP address of a presence server for sending presence requests from internal watchers to external presence entities. |
| show presence global | Displays configuration information about the presence service. |
| show presence subscription | Displays information about active presence subscriptions. |

| Release | Modification |
|---|---|
| 12.4(11)XJ | This command was introduced. |
| 12.4(15)T | This command was integrated into Cisco IOS Release 12.4(15)T. |

| Command | Description |
|---|---|
| allow watch | Allows a directory number on a phone registered to Cisco Unified CME to be watched in a presence service. |
| blf-speed-dial | Enables BLF monitoring for a speed-dial number on a phone registered to Cisco Unified CME. |
| presence | Enables presence service and enters presence configuration mode. |
| show presence global | Displays configuration information about the presence service. |

| Release | Modification |
|---|---|
| 12.4(11)XJ | This command was introduced. |
| 12.4(15)T | This command was integrated into Cisco IOS Release 12.4(15)T. |

| Command | Description |
|---|---|
| allow subscribe | Allows internal watchers to monitor external presence entities (directory numbers). |
| allow watch | Allows a directory number on a phone registered to Cisco Unified CME to be watched in a presence service. |
| max-subscription | Sets the maximum number of concurrent watch sessions that are allowed. |
| show presence global | Displays configuration information about the presence service. |
| show presence subscription | Displays information about active presence subscriptions. |
| watcher all | Allows external watchers to monitor internal presence entities (directory numbers). |

| timeslots timeslot - range | Specifies a single range of timeslot values in the PRI
                                          						goup. For T1, the allowable range is from 1 to 23. For E1, the allowable range
                                          						is from 1 to 31. |
|---|---|
| nfas_d | Specifies the operation of the D channel timeslot. |
| backup | (Optional) Specifes that the operation of the D channel
                                          						timeslot on this controller is the NFAS D backup. |
| none | (Optional) Specifes that the D channel timeslot is used as
                                          						an additional B channel. |
| primary | Specifies that the D channel timeslot on this controller in
                                          						NFAS D. |
| nfas_int range | Specifies the provisioned NFAS interface value. Valid
                                          						values range from 0 to 32. |
| nfas-group number | Specifies the NFAS group and the NFAS group number. Valid
                                          						values range from 0 to 31. |
| iua as - name | Binds the Non-Facility Associated Signaling (NFAS) group to
                                          						the IDSN User Adaptation Layer (IUA) application server (AS). |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |
| 12.2(15)T | This command was integrated on the Cisco 2420, Cisco 2600
                                          						series, Cisco 3600 series, and Cisco 3700 series; and Cisco AS5300, Cisco
                                          						AS5350, Cisco AS5400, and Cisco AS5850 network access server (NAS) platforms. |

| Command | Description |
|---|---|
| isdn switch - type | Configures the Cisco 2600 series router PRI interface to
                                          						support QSIG signaling. |

| pbx - ip - address | IP address of the NEC PBX. |
|---|---|
| pbx - ip - host - name | Host name of the NEC PBX. |
| pbx - port number | Port number for the PBX. Range is from 49152 to 65535. Default is 55000. If this value is already in use, the next greater
                                          value is used. |

| Release | Modification |
|---|---|
| 12.0(7)T | This command was introduced on the Cisco AS5300. |
| 12.2(1) | This command was modified to add support for setup messages from a POTS dial peer. |

| Command | Description |
|---|---|
| isdn protocol-emulate | Configures the Layer 2 and Layer 3 port protocol of a BRI voice port or a PRI interface to emulate NT (network) or TE (user)
                                          functionality. |
| isdn switch type | Configures the Cisco AS5300 universal access server PRI interface to support QSIG signaling. |
| show cdapi | Displays the CDAPI. |
| show rawmsg | Displays the raw messages owned by the required component. |

| timeslot-range | A value or range of values for time slots on a T1 or E1 controller that consists of an ISDN PRI group. Use a hyphen to indicate
                                          a range. Note Groups of time slot ranges separated by commas (1-4,8-23 for example) are also accepted. | Note | Groups of time slot ranges separated by commas (1-4,8-23 for example) are also accepted. |
|---|---|---|---|
| Note | Groups of time slot ranges separated by commas (1-4,8-23 for example) are also accepted. |
| nfas_d | (Optional) Configures the operation of the ISDN PRI D channel. |
| backup | The D-channel time slot is used as the Non-Facility Associated Signaling (NFAS) D backup. |
| service mgcp | (Optional) Configures the service type as Media Gateway Control Protocol (MGCP) service. |
| none | The D-channel time slot is used as an additional B channel. |
| primary | The D-channel time slot is used as the NFAS D primary. |
| nfas_int number | Specifies the provisioned NFAS interface as a value. The NFAS interface range is from 0 to 44. |
| nfas_group number | Specifies the NFAS group. The NFAS group number range is from 0 to 31. |
| iua as-name | (Optional) Configures the ISDN User Adaptation Layer (IUA) application server (AS) name. |
| rlm-group number | (Optional) Specifies the Redundant Link Manager (RLM) group and releases the ISDN PRI signaling channel. The RLM group number
                                          range is from 0 to 255. |
| voice-dsp | (Optional) Configures an ISDN PRI group for voice applications by using the Digital Signal Processor (DSP). |

| Note | Groups of time slot ranges separated by commas (1-4,8-23 for example) are also accepted. |
|---|---|

| Release | Modification |
|---|---|
| 11.0 | This command was introduced. |
| 11.3 | This command was enhanced to support NFAS. |
| 12.0(2)T | This command was implemented on the Cisco MC3810 multiservice concentrator. |
| 12.0(7)XK | This command was implemented on the Cisco 2600 and Cisco 3600 series routers. |
| 12.1(2)T | The modifications in Cisco IOS Release 12.0(7)XK were integrated into Cisco IOS Release 12.1(2)T. |
| 12.2(8)B | This command was modified with the rlm-group subkeyword to support the release of the ISDN PRI signaling channels. |
| 12.2(15)T | The modifications in Cisco IOS Release 12.2(8)B were integrated into Cisco IOS Release 12.2(15)T. |
| 12.4(16)b | This command was modified to ensure that the NFAS primary interface is configured before the NFAS backup or NFAS none interfaces
                                          are configured. |
| 12.4(24)T | Support was extended to provide backup functionality for the NFAS interface in MGCP backhaul mode. With this support, if the
                                          primary interface fails, the backup can become active and calls can be maintained. |
| 15.1(3)T | This command was modified. The voice-dsp keyword was added. |

| Note | The active D -channel changeover between primary and backup controllers happens only when one of the link fails and not when
                                          the link comes up. The T309 timer is triggered when the changeover takes place. |
|---|---|

| Note | You must first configure the NFAS primary D channel before configuring the NFAS backup or NFAS none interfaces. If this order
                                          is not followed, this message is displayed:
                                          NFAS backup and NFAS none interfaces are not allowed to be configured without primary. First configure primary D channel.
                                          To remove the NFAS primary D channel after the NFAS backup or NFAS none interfaces are configured, you must remove the NFAS
                                          backup or NFAS none interfaces first, and then remove the NFAS primary D channel. |
|---|---|

| Command | Description |
|---|---|
| controller | Configures a T1 or E1 controller and enters controller configuration mode. |
| interface Dchannel | Specifies an ISDN D-channel interface for VoIP applications that require release of the ISDN PRI signaling time slot for RLM
                                          configurations. |
| interface serial | Specifies a serial interface created on a channelized E1 or channelized T1 controller for ISDN PRI signaling. |
| isdn rlm-group | Specifies the RLM group number that ISDN will start using. |
| isdn switch-type | Specifies the central office switch type on the ISDN PRI interface. |
| isdn timer t309 | Changes the value of the T309 timer to clear network connections and releases the B channels when there is no active signaling
                                          channel. |
| show isdn nfas group | Displays all the members of a specified NFAS group or all NFAS groups. |

| ftp path / filename | Name and location of the file on an external FTP server.
                                          						Filename is limited to 25 characters. |
|---|---|
| ifs device : filename | Name and location of the file in flash memory or other
                                          						internal file system on this router. Values depend on storage devices available
                                          						on the router, for example flash or slot0. Filename is limited to 25
                                          						characters. |
| username username | User ID for authentication. |
| password password | Password user enters for authentication. |

| Release | Modification |
|---|---|
| 12.4(15)XY | This command was introduced. |
| 12.4(20)T | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |

| Command | Description |
|---|---|
| file-acct flush | Manually flushes the CDRs from the buffer to the accounting
                                          						file. |
| file-acct reset | Manually switches back to the primary device for file
                                          						accounting. |
| maximum retry-count | Sets the maximum number of times the router attempts to
                                          						connect to the primary file device before switching to the secondary device. |
| secondary | Sets the backup location for storing CDRs if the primary
                                          						location becomes unavailable. |

| pstn | Requests
                                          						that the privacy service implements a privacy header using the default Public
                                          						Switched Telephone Network (PSTN) rules for privacy (based on information in
                                          						Octet 3a). When selected, this becomes the only valid option. |
|---|---|
| privacy-option | The
                                          						privacy support options to be set at the global level. The following keywords
                                          						can be specified for the privacy-option argument: header -- Requests that privacy be enforced for all
                                                							 headers in the Session Initiation Protocol (SIP) message that might identify
                                                							 information about the subscriber. history -- Requests that the information held in the
                                                							 history-info header is hidden outside the trust domain. id -- Requests that the Network Asserted Identity
                                                							 that authenticated the user be kept private with respect to SIP entities
                                                							 outside the trusted domain. session -- Requests that the information held in the
                                                							 session description is hidden outside the trust domain. user -- Requests that privacy services provide a
                                                							 user-level privacy function. Note The
                                                      						  keywords can be used alone, altogether, or in any combination with each other,
                                                      						  but each keyword can be used only once. | Note | The
                                                      						  keywords can be used alone, altogether, or in any combination with each other,
                                                      						  but each keyword can be used only once. |
| Note | The
                                                      						  keywords can be used alone, altogether, or in any combination with each other,
                                                      						  but each keyword can be used only once. |
| critical | (Optional) Requests that the privacy service performs the specified service or
                                          						fail the request. Note This
                                                      						  optional keyword is only available after at least one of the privacy-option keywords ( header , history , id , session , or user ) has been
                                                      						  specified and can be used only once per command. | Note | This
                                                      						  optional keyword is only available after at least one of the privacy-option keywords ( header , history , id , session , or user ) has been
                                                      						  specified and can be used only once per command. |
| Note | This
                                                      						  optional keyword is only available after at least one of the privacy-option keywords ( header , history , id , session , or user ) has been
                                                      						  specified and can be used only once per command. |
| system | Specifies that the privacy support use the global sip-ua value.
                                          						This keyword is available only for the tenant mode to allow it to fallback to
                                          						the global configurations. |

| Note | The
                                                      						  keywords can be used alone, altogether, or in any combination with each other,
                                                      						  but each keyword can be used only once. |
|---|---|

| Note | This
                                                      						  optional keyword is only available after at least one of the privacy-option keywords ( header , history , id , session , or user ) has been
                                                      						  specified and can be used only once per command. |
|---|---|

| Release | Modification |
|---|---|
| 12.4(15)T | This
                                          						command was introduced. |
| 12.4(22)T | The history keyword
                                          						was added to provide support for the history-info header information. |
| 15.6(2)T and IOS XE Denali 16.3.1 | This command was modified to include the keyword: system . |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| asserted-id | Sets
                                          						the privacy level and enables either PAI or PPI privacy headers in outgoing SIP
                                          						requests or response messages. |
| calling-info pstn-to-sip | Specifies calling information treatment for PSTN-to-SIP calls. |
| clid (voice-service-voip) | Passes
                                          						the network-provided ISDN numbers in an ISDN calling party information element
                                          						screening indicator field, removes the calling party name and number from the
                                          						calling-line identifier in voice service voip configuration mode, or allows a
                                          						presentation of the calling number by substituting for the missing Display Name
                                          						field in the Remote-Party-ID and From headers. |
| voice-class sip privacy | Sets
                                          						privacy support at the dial-peer configuration level as defined in RFC 3323. |

| on | Prevents other phones on the shared line to join active calls. |
|---|---|
| off | Allows other phones on the shared line to join active calls. |

| Release | Modification |
|---|---|
| 15.1(3)T | This command was introduced. |

| Command | Description |
|---|---|
| stcapp supplementary-services | Enters supplementary-service configuration mode for configuring STCAPP supplementary-service features on an FXS port. |

| passthru | Passes
                                          						the privacy values from the received message to the next call leg. |
|---|---|
| send-always | Passes a
                                          						privacy header with a value of None to the next call leg, if the received
                                          						message does not contain privacy values but a privacy header is required. |
| strip | Strips
                                          						the diversion or history-info headers received from the next call leg. |
| diversion | Strips
                                          						the diversion headers received from the next call leg. |
| history-info | Strips
                                          						the history-info headers received from the next call leg. |
| system | Specifies that the privacy header policy options use the global
                                          						sip-ua value. This keyword is available only for the tenant mode to allow it to
                                          						fallback to the global configurations. |

| Release | Modification |
|---|---|
| 12.4(22)YB | This
                                          						command was introduced. |
| 15.0(1)M | This
                                          						command was integrated into Cisco IOS Release 15.0(1)M. |
| 15.1(2)T | This
                                          						command was modified. The strip , diversion , and history-info keywords were added. |
| 15.6(2)T
                                          						and IOS XE Denali 16.3.1 | This
                                          						command was modified to include the keyword: system . This
                                          						command is now available under voice class tenants. |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| asserted-id | Sets
                                          						the privacy level and enables either PAID or PPID privacy headers in outgoing
                                          						SIP requests or response messages. |
| voice-class sip privacy-policy | Configures the privacy header policy options at the dial-peer configuration
                                          						level. |

| keepalive | (optional) Configures the time interval between probing messages when the session is in a keepalive state. Range is from 1
                                          to 255 seconds. Default is 5 seconds. |
|---|---|
| negative | (optional) Configures the time interval between probing messages when the session is in a negative state. Range is from 1
                                          to 20 seconds. Default is 5 seconds. |
| seconds | Number of seconds between probing message. |

| Release | Modification |
|---|---|
| 15.2(2)T | This command was introduced. |

| Command | Description |
|---|---|
| message-exchange | Sets the maximum number of failed message responses before the provider stops sending messages. |
| probing max-failure | Sets the number of messages that the system will send without receiving a reply before the system unregisters the application. |

| number | Maximum number of messages allowed before the system stops the session and unregisters the application. Range is from 1 to
                                          5. Default is 3. |
|---|---|

| Release | Modification |
|---|---|
| 15.2(2)T | This command was introduced. |

| Command | Description |
|---|---|
| message-exchange | Sets the maximum number of failed message attempts before the provider stops sending messages. |
| probing interval | Sets the time interval between probing messages. |

| alert | Specifies that the configuration applies to call Alert messages. |
|---|---|
| callproc | Specifies that the configuration applies to Session Initiation Protocol (SIP) 183 Session In Progress (Call_Proceeding) messages. |
| connect | Specifies that the configuration applies to call Connect messages. |
| disconnect | Specifies that the configuration applies to call Disconnect messages. |
| progress | Specifies that the configuration applies to call progress messages. |
| setup | Specifies that the configuration applies to call setup messages. |
| enable | Enables user-specified configuration of the progress indicator on the specified call message type. |
| pi - number | Specifies the PI to be used in place of the default PI. The following are acceptable PI values according to the call message
                                          type: Alert, Connect, Progress, and SIP 183 Session In Progress messages: 
                                                1, 2, or 8. Disconnect messages: 8. Setup messages: 0, 1, or 3. |
| disable | Disables user-specified configuration of the progress indicator on the specified call message type. |
| strip | Configures the dial peer to remove all or specific progress indicators in the specified call message type. Note This option applies only to call Alert message on POTS dial peers or to call Proceeding messages on VoIP dial peers. | Note | This option applies only to call Alert message on POTS dial peers or to call Proceeding messages on VoIP dial peers. |
| Note | This option applies only to call Alert message on POTS dial peers or to call Proceeding messages on VoIP dial peers. |
| strip-pi - number | (optional) Specifies that only a specific PI is to be removed from the specified call message. The value can be 1, 2, or 8. |

| Note | This option applies only to call Alert message on POTS dial peers or to call Proceeding messages on VoIP dial peers. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(3)XI | This command was introduced on the Cisco 2600 series, Cisco 3600 series, Cisco 7200 series, Cisco 7500 series, Cisco MC3810,
                                          Cisco AS5300, and Cisco AS5800. |
| 12.1(5)T | This command was integrated into Cisco IOS Release 12.1(5)T. |
| 12.2(1) | This command was modified. Support was added for setup messages from a POTS dial peer. |
| 12.2(2)XA | This command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. |
| 15.0(1)XA | This command was modified. Support was added for stripping of PIs in call Alert and SIP 183 Session In Progress (Call_Proceeding)
                                          messages. |
| 15.1(1)T | This command was integrated into Cisco IOS Release 5.1(1)T. |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| destination-pattern | Specifies the destination pattern (prefix or full E.164 phone number) to be used on an outbound dial peer. |

| ipv4 | Specifies the IPv4-only mode. |
|---|---|
| ipv6 | Specifies the IPv6-only mode. |
| dual-stack | Specifies the dual-stack (that is, IPv4 and IPv6) mode. |
| preference { ipv4 \| ipv6 | (Optional) Specifies the preferred dual-stack mode, which can be either IPv4 (the default preferred dual-stack mode) or IPv6. |

| Release | Modification |
|---|---|
| 12.4(22)T | This command was introduced. |
| 15.1(1)T | This command was integrated into Cisco IOS Release 15.1(1)T. |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| sip ua | Enters SIP user-agent configuration mode. |

| port - number | RLM port number. See the table below for the port number choices. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(7) | This command was introduced. |

| Protocol | Port Number |
|---|---|
| RLM | 3000 |
| ISDN | Port[RLM]+1 |

| Command | Description |
|---|---|
| clear interface | Resets the hardware logic on an interface. |
| clear rlm group | Clears all RLM group time stamps to zero. |
| interface | Defines the IP addresses of the server, configures an interface type, and enters interface configuration mode. |
| link (RLM) | Specifies the link preference. |
| retry keepalive | Allows consecutive keepalive failures a certain amount of time before the link is declared down. |
| server (RLM) | Defines the IP addresses of the server. |
| show rlm group statistics | Displays the network latency of the RLM group. |
| show rlm group status | Displays the status of the RLM group. |
| show rlm group timer | Displays the current RLM group timer values. |
| shutdown (RLM) | Shuts down all of the links under the RLM group. |
| timer | Overwrites the default setting of timeout values. |

| xcc | (optional) Enables the XCC service provider. |
|---|---|
| xsvc | (optional) Enables the XSVC service provider. |
| xcdr | (optional) Enables the XCDR service provider. |
| xmf | (optional) Enables the XMF service provider. |

| Release | Modification |
|---|---|
| 15.2(2)T | This
                                          						command was introduced. |
| 15.3(2)T | xmf keyword was
                                             						  added. |
| Cisco
                                          						IOS XE Everest 16.6.1 | Added
                                          						support for xcc and xsvc service
                                          						providers in secure mode. |

| Note | You can enable
                                       		  only xcc and xsvc service
                                       		  providers in secure mode. |
|---|---|

| Command | Description |
|---|---|
| remote-url | Specifies
                                          						the URL of the application. |
| source-address | Specifies
                                          						the IP address of the provider. |
| uc wsapi | Enters
                                          						nonsecure Cisco Unified Communication IOS services configuration mode. |
| uc secure-wsapi | Enters
                                          						secure Cisco Unified Communication IOS services configuration mode. |

| Release | Modification |
|---|---|
| 11.3(2)NA | This command was introduced on the Cisco 2500 series and Cisco 3600 series. |

| host | WebSocket proxy server hostname. |
|---|---|
| ipv4 ip-address | Host IP address of the WebSocket proxy server. |
| port port | WebSocket proxy server port. |

| Release | Modification |
|---|---|
| Cisco IOS XE Bengaluru 17.6.1a | This command was introduced on Cisco Unified Border Element. |

| Note | port port is an optional configuration parameter. |
|---|---|

| Command | Description |
|---|---|
| media profile stream-service | Enables stream service on CUBE . |
| connection (media-profile) | Configures idle timeout and call threshold for a media profile. |
| source-ip (media-profile) | Configures local source IP address of a WebSocket connection. |
| media class | Applies the media class at the dial peer level. |

| Release | Modification |
|---|---|
| 15.0(1)M | This command was introduced. |

| Note | Users should configure the no pulse-digit-detection command only if their equipment generates pulse digits in error when initiating an outbound call. |
|---|---|

| Command | Description |
|---|---|
| timing pulse | Specifies the pulse dialing rate for a specified voice port. |