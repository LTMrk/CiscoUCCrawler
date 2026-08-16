---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-vcr3-vcr3-cr-book-vcr-o1-html-8f6912a808
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/vcr3/vcr3-cr-book/vcr-o1.html
retrieved_at: 2026-08-16T23:18:38.589513+00:00
---

Cisco IOS Voice Command Reference - K through R

# Cisco IOS Voice Command Reference - K through R

Updated: December 21, 2024

Chapter: O

## Chapter: O

# O

## offer call-hold

To specify globally
                              		  how the POTS-SIP gateway should initiate call-hold requests, use the offer call-hold command in SIP user-agent configuration
                              		  mode or voice class tenant configuration mode. To disable a method of
                              		  initiating call hold, use the no form of this
                              		  command.

offer call-hold { conn-addr | direction-attr | system }

no offer call-hold { conn-addr | direction-attr | system }

### Syntax Description

conn-addr

Specifies
                                          						the RFC 2543 method of using the connection address for initiating call-hold
                                          						requests. The RFC 2543 method uses 0.0.0.0.

direction-attr

Specifies
                                          						the current RFC 3264 method of using the direction attribute (a=sendonly) for
                                          						initiating call-hold requests.

system

Specifies how the call-hold requests use the global sip-ua
                                          						value. This keyword is available only for the tenant mode to allow it to
                                          						fallback to the global configurations

### Command Default

direction-attr

### Command Modes

SIP user-agent configuration

Voice class tenant configuration (config-class)

## Command History

Release

Modification

12.3(8)T

This
                                          						command was introduced.

15.6(2)T and IOS XE Denali 16.3.1

This command was modified to include the keyword: system .

### Usage Guidelines

Cisco POTS-SIP
                              		  gateways support receiving call-hold requests in either of the two formats, but
                              		  the direction attribute is recommended. Specifying a call-hold format is only
                              		  available globally with the offer call-hold command; configuration is not available
                              		  at the dial-peer level.

## Examples

The following
                              		  example initiates call hold by configuring the gateway to send a=sendonly in
                              		  the Session Description Protocol ( SDP). Using the direction-attr keyword is the current and preferred
                              		  method to initiate call hold.

```
sip-ua 
 retry invite 3
 offer call-hold direction-attr
```

The following
                              		  example initiates call hold by configuring the gateway to send 0.0.0.0 as the
                              		  IP address in the c=line.

```
sip-ua 
 retry invite 3
 offer call-hold conn-addr
```

The following
                              		  example initiates call hold by configuring the gateway in the voice class
                              		  tenant configuration mode:

```
Router(config-class)# offer call-hold system
```

### Related Commands

Command

Description

show sip-ua status

Displays
                                          						status for the SIP UA.

suspend-resume

Enables
                                          						SIP Suspend and Resume functionality.

## operation

To select a specific cabling scheme for E&M ports, use the operation command in voice-port configuration mode. To restore the
                              		  default, use the no form of this command.

operation { 2-wire | 4-wire }

no operation { 2-wire | 4-wire }

### Syntax Description

2 - wire

Two-wire E&M cabling scheme.

4 - wire

Four-wire E&M cabling scheme.

### Command Default

2-wire E&M cabling scheme

### Command Modes

Voice-port configuration

## Command History

Release

Modification

11.3(1)T

This command was introduced on the Cisco 3600 series.

11.3(1)MA

This command was implemented on the Cisco MC3810.

### Usage Guidelines

This command affects only voice traffic. Signaling is independent of
                              		  2-wire versus 4-wire settings. If the wrong cable scheme is specified, the user
                              		  might get voice traffic in only one direction.

Using this command on a voice port changes the operation of both
                              		  voice ports on a VPM card. The voice port must be shut down and then opened
                              		  again for the new value to take effect.

This command is not applicable to FXS or FXO interfaces because they
                              		  are, by definition, 2-wire interfaces.

## Examples

The following example specifies that an E&M port uses a 4-wire
                              		  cabling scheme:

```
voice-port 1/0/0
 operation 4-wire
```

The following example specifies that an E&M port uses a 2-wire
                              		  cabling scheme:

```
voice-port 1/1
 operation 2-wire
```

## options-ping

To enable in-dialog
                              		  OPTIONS, use the options-ping command in global configuration mode or voice class tenant configuration mode.
                              		  To disable, use the no form of this
                              		  command.

options-ping seconds [system]

no options-ping seconds [system]

### Syntax Description

seconds

Intervals, in seconds OPTIONS transactions are sent. Range is 60-1200, there is
                                          						no default.

system

Specifies
                                          						that the in-dialog OPTIONS, use the global sip-ua value. This keyword is
                                          						available only for the tenant mode to allow it to fallback to the global
                                          						configurations

### Command Default

This command is
                              		  disabled by default.

### Command Modes

Global

Voice class tenant configuration (config-class)

## Command History

Release

Modification

12.4(11)T

This
                                          						command was introduced.

15.6(2)T and IOS XE Denali 16.3.1

This command was modified to include the keyword: system .

Cisco IOS XE Cupertino 17.7.1a

Introduced support for YANG models.

### Usage Guidelines

The in-dialog
                              		  OPTIONS refresh command eanbles an alterante refresh mechanism to RTP/RTCP
                              		  media inactivity timer and session timer can be used on SIP-to-SIP and
                              		  SIP-to-H.323 calls. The refresh with in-dialog OPTIONS method is meant to only
                              		  be hop-to-hop, and not end-to-end. Since session timer achieves similar
                              		  results, the OPTIONs refresh/ping will not take affect when session timer is
                              		  negotiated. The behavior on the H.323 endpoint is as if it was a TDM-SIP call.
                              		  The generating in-dialog OPTIONS is enabled at the global level or dialpeer
                              		  level. The system default setting is disabled. This feature can be use by both
                              		  a TDM voice gateway and an IP-to-IP gateway.

## Examples

The following
                              		  example sets the in-dialog refresh time to 60 seconds:

```
Router(conf-serv-sip)# options-ping
```

The following
                              		  example sets the in-dialog refresh time in the voice class tenant configuration
                              		  mode:

```
Router(conf-class)# options-ping system
```

### Related Commands

Command

Description

options-ping

Enables
                                          						in-dialog OPTIONS at the global level.

options-ping (dial peer)

Enables
                                          						in-dialog OPTIONS on a dial-peer.

## options-ping (dial-peer)

To enable in-dialog OPTIONS, use the options-ping command in global configuration mode. To disable, use the no form of this command.

options-ping seconds

no options-ping seconds

### Syntax Description

seconds

Intervals, in seconds OPTIONS transactions are sent. Range is 60-1200, there is no default.

### Command Default

This command is disabled by default.

### Command Modes

dial peer configuration mode

## Command History

Release

Modification

12.4(11)T

This command was introduced.

### Usage Guidelines

The in-dialog OPTIONS refresh command eanbles an alterante refresh mechanism to RTP/RTCP media inactivity timer and session
                              timer can be used on SIP-to-SIP and SIP-to-H.323 calls. The refresh with in-dialog OPTIONS method is meant to only be hop-to-hop,
                              and not end-to-end. Since session timer achieves similar results, the OPTIONs refresh/ping will not take affect when session
                              timer is negotiated. The behavior on the H.323 endpoint is as if it was a TDM-SIP call. The generating in-dialog OPTIONS is
                              enabled at the global level or dialpeer level. The system default setting is disabled. This feature can be use by both a TDM
                              voice gateway and an IP-to-IP gateway.

## Examples

The following example sets the in-dialog refresh time to 60 seconds:

```
Router(conf-serv-sip)# options-ping 60
```

### Related Commands

Command

Description

options-ping

Enables in-dialog OPTIONS at the global level.

options-ping (dial peer)

Enables in-dialog OPTIONS on a dial-peer.

## outbound-proxy

To configure a
                              		  Session Initiation Protocol (SIP) outbound proxy for outgoing SIP messages
                              		  globally on a Cisco IOS voice gateway, use the outbound-proxy command in voice service SIP
                              		  configuration mode or voice class tenant configuration mode. To globally
                              		  disable forwarding of SIP messages to a SIP outbound proxy globally, use the no form of this
                              		  command.

outbound-proxy { dhcp | ipv4: ip-address [ : port-number | dns: host : domain [ reuse ]]} [system]

no outbound-proxy

### Syntax Description

dhcp

Specifies
                                          						the SIP outbound proxy globally for a Cisco IOS voice gateway; all SIP
                                          						dialog-initiating requests are sent to the SIP server obtained via DHCP.

ipv4 : ip-address

Specifies
                                          						the SIP outbound proxy globally for a Cisco IOS voice gateway; all SIP
                                          						dialog-initiating requests are sent to this IP address. The colon is required.

: port-number

(Optional) The port to which all SIP dialog-initiating requests are sent at the
                                          						specified IP address. Port number ranges from 0 to 65535. The default is 5060.
                                          						The colon is required.

dns : host : domain

Specifies
                                          						the SIP outbound proxy globally for a Cisco IOS voice gateway; all initiating
                                          						requests are sent to the specified destination domain. The colon is required.

reuse

(Optional) Reuses the outbound proxy address established during registration
                                          						for all subsequent registration refreshes and calls.

system

Specifies that the outbound proxy for outgoing SIP messages use
                                          						the global sip-ua value. This keyword is available only for the tenant mode to
                                          						allow it to fallback to the global configurations

### Command Default

The Cisco IOS voice
                              		  gateway does not forward outbound SIP messages to a proxy.

### Command Modes

Voice service VoIP SIP configuration (conf-serv-sip)

Voice class tenant configuration (config-class)

## Command History

Release

Modification

12.4(15)T

This
                                          						command was introduced.

12.4(22)T

Support
                                          						for IPv6 was added.

12.4(22)YB

This
                                          						command was modifed. The dhcp keyword
                                          						was added.

15.0(1)M

This
                                          						command was integrated in Cisco IOS Release 15.0(1)M.

15.1(2)T

This
                                          						command was modified. The reuse keyword
                                          						was added.

15.6(2)T and IOS XE Denali 16.3.1

This command was modified to include the keyword: system .

Introduced support for YANG models.

### Usage Guidelines

You can use the outbound-proxy command in voice service SIP
                              		  configuration mode to specify outbound proxy settings globally for a Cisco IOS
                              		  voice gateway. You can also use the voice-class sip outbound-proxy command in dial peer voice
                              		  configuration mode to configure settings for an individual dial peer that
                              		  override or defer to the global settings for the gateway. However, if both a
                              		  Cisco Unified Communications Manager Express (CME) and a SIP gateway are
                              		  configured on the same router, then there is a scenario that can cause incoming
                              		  SIP messages from line-side phones to be confused with SIP messages coming from
                              		  the network side. To avoid failed calls caused by this scenario, disable the
                              		  SIP outbound proxy setting for all line-side phones on a dial peer using the outbound-proxy system command in voice register global
                              		  configuration mode.

## Examples

The following
                              		  example shows how to specify the SIP outbound proxy globally for a Cisco IOS
                              		  voice gateway using an IP address:

```
Router> enable Router# configure terminal Router(config)# voice service voip Router(conf-voi-serv)# sip Router(conf-serv-sip)# outbound - proxy ipv4 : 10.1.1.1
```

The following
                              		  example shows how to specify the SIP outbound proxy globally for a Cisco IOS
                              		  voice gateway using a destination hostname and domain:

```
Router> enable Router# configure terminal Router(config)# voice service voip Router(conf-voi-serv)# sip Router(conf-serv-sip)# outbound - proxy dns:sipproxy:example.com
```

The following
                              		  example shows how to specify the SIP outbound proxy globally for a Cisco IOS
                              		  voice gateway using the DHCP protocol:

```
Router> enable Router# configure terminal Router(config)# voice service voip Router(conf-voi-serv)# sip Router(conf-serv-sip)# outbound - proxy dhcp
```

The following
                              		  example shows how to specify the SIP outbound proxy globally in the voice class
                              		  tenant configuration mode:

```
Router(config-class)# outbound-proxy system
```

### Related Commands

Command

Description

outbound-proxy system

Specifies whether Cisco Unified CME line-side SIP phones use the outbound proxy
                                          						settings configured globally for a Cisco IOS voice gateway.

voice-class sip outbound-proxy

Configures SIP outbound proxy settings for an individual dial peer that
                                          						override global settings for the Cisco IOS voice gateway.

## outbound retry-interval

To define the retry period for attempting to establish the outbound relationship between border elements, use the outbound retry - interval command in Annex G neighbor service configuration mode. To disable the command, use the no form of this command.

outbound retry-interval interval

no outbound retry-interval

### Syntax Description

interval

Amount of time, in seconds, to establish the outbound relationship. Range is from 1 to 2147483. The default is 30.

### Command Default

30 seconds

### Command Modes

Annex G neighbor service configuration (config-nxg-neigh-svc)

## Command History

Release

Modification

12.2(11)T

This command was introduced.

### Usage Guidelines

Service relationships are defined to be unidirectional. When a service relationship is established between border element
                              A and border element B, A is entitled to send requests to B and expect responses. For B to send requests to A and expect responses,
                              a second service relationship must be established. From A’s perspective, the service relationship it establishes with B is
                              designated as the "outbound" service relationship.

Use this command to set the retry period for attempting to bring up the outbound relationship between border elements.

## Examples

The following example shows how to set the retry interval to 300 seconds (5 minutes):

```
Router(config-nxg-neigh-svc)
# outbound retry-interval 300
```

### Related Commands

Command

Description

access - policy

Requires that a neighbor be explicitly configured.

inbound ttl

Sets the inbound time-to-live value.

retry interval

Defines the time between delivery attempts.

retry window

Defines the total time that a border element will attempt delivery.

service - relationship

Establishes a service relationship between two border elements.

shutdown

Enables or disables the border element.

## outgoing called-number

To configure debug filtering for outgoing called numbers, use the outgoing called-number command in call filter match list
                              configuration mode. To disable, use the no form of this command.

outgoing called-number string

no outgoing called-number string

### Syntax Description

string

Series of digits that specify a pattern for the E.164 or private dialing plan telephone number. Valid entries are the digits
                                          0 to 9, the letters A to D, and the following special characters:

The asterisk (*) and pound sign (#) that appear on standard touchtone dial pads. On the Cisco 3600 series routers only, these
                                                characters cannot be used as leading characters in a string (for example, *650).

Comma (,), which inserts a pause between digits.

Period (.), which matches any entered digit (this character is used as a wildcard). On the Cisco 3600 series routers, the
                                                period cannot be used as a leading character in a string (for example, .650).

Percent sign (%), which indicates that the preceding digit occurred zero or more times; similar to the wildcard usage.

Plus sign (+), which indicates that the preceding digit occurred one or more times.

The plus sign used as part of a digit string is different from the plus sign that can be used in front of a digit string to
                                                      indicate that the string is an E.164 standard number.

Circumflex (^), which indicates a match to the beginning of the string.

Dollar sign ($), which matches the null string at the end of the input string.

Backslash symbol (\), which is followed by a single character; matches that character. Can be used with a single character
                                                with no other significance (matching that character).

Question mark (?), which indicates that the preceding digit occurred zero or one time.

Brackets ( [ ] ), which indicate a range. A range is a sequence of characters enclosed in the brackets; only numeric characters
                                                0 to 9 are allowed in the range.

Parentheses ( ), which indicate a pattern and are the same as the regular expression rule.

### Command Default

No default behavior or values

### Command Modes

Call filter match list configuration

## Command History

Release

Modification

12.3(4)T

This command was introduced.

### Usage Guidelines

The outgoing called number goes out after number translation and expansion.

## Examples

The following example shows the voice call debug filter set to match outgoing called number 8288807:

```
call filter match-list 1 voice
 outgoing called-number 8288807
```

### Related Commands

Command

Description

call filter match-list voice

Create a call filter match list for debugging voice calls.

debug condition match-list

Run a filtered debug on a voice call.

incoming called-number (call filter match list)

Configure debug filtering for incoming called numbers.

incoming calling-number

Configure debug filtering for incoming calling numbers.

incoming dialpeer

Configure debug filtering for the incoming dial peer.

incoming secondary-called-number

Configure debug filtering for incoming called numbers from the second stage of a two-stage scenario.

outgoing calling-number

Configure debug filtering for outgoing calling numbers.

outgoing dialpeer

Configure debug filtering for the outgoing dial peer.

show call filter match-list

Display call filter match lists.

## outgoing calling-number

To configure debug filtering for outgoing calling numbers, use the outgoing calling-number command in call filter match list
                              configuration mode. To disable, use the no form of this command.

outgoing calling-number string

no outgoing calling-number string

### Syntax Description

string

Series of digits that specify a pattern for the E.164 or private dialing plan telephone number. Valid entries are the digits
                                          0 to 9, the letters A to D, and the following special characters:

The asterisk (*) and pound sign (#) that appear on standard touchtone dial pads. On the Cisco 3600 series routers only, these
                                                characters cannot be used as leading characters in a string (for example, *650).

Comma (,), which inserts a pause between digits.

Period (.), which matches any entered digit (this character is used as a wildcard). On the Cisco 3600 series routers, the
                                                period cannot be used as a leading character in a string (for example, .650).

Percent sign (%), which indicates that the preceding digit occurred zero or more times; similar to the wildcard usage.

Plus sign (+), which indicates that the preceding digit occurred one or more times.

The plus sign used as part of a digit string is different from the plus sign that can be used in front of a digit string to
                                                      indicate that the string is an E.164 standard number.

Circumflex (^), which indicates a match to the beginning of the string.

Dollar sign ($), which matches the null string at the end of the input string.

Backslash symbol (\), which is followed by a single character; matches that character. Can be used with a single character
                                                with no other significance (matching that character).

Question mark (?), which indicates that the preceding digit occurred zero or one time.

Brackets ( [ ] ), which indicate a range. A range is a sequence of characters enclosed in the brackets; only numeric characters
                                                0 to 9 are allowed in the range.

Parentheses ( ), which indicate a pattern and are the same as the regular expression rule.

### Command Default

No default behavior or values

### Command Modes

Call filter match list configuration

## Command History

Release

Modification

12.3(4)T

This command was introduced.

### Usage Guidelines

The outgoing calling number goes out after number translation and expansion.

## Examples

The following example shows the voice call debug filter set to match outgoing calling number 5550124:

```
call filter match-list 1 voice
 outgoing calling-number 5550124
```

### Related Commands

Command

Description

call filter match-list voice

Create a call filter match list for debugging voice calls.

debug condition match-list

Run a filtered debug on a voice call.

incoming called-number (call filter match list)

Configure debug filtering for incoming called numbers.

incoming calling-number

Configure debug filtering for incoming calling numbers.

incoming dialpeer

Configure debug filtering for the incoming dial peer.

incoming secondary-called-number

Configure debug filtering for incoming called numbers from the second stage of a two-stage scenario.

outgoing called-number

Configure debug filtering for outgoing called numbers.

outgoing dialpeer

Configure debug filtering for the outgoing dial peer.

show call filter match-list

Display call filter match lists.

## outgoing dialpeer

To configure debug filtering for the outgoing dial peer, use the outgoing dialpeer command in call filter match list configuration mode. To disable, use the no form of this command.

outgoing dialpeer tag

no outgoing dialpeer tag

### Syntax Description

tag

Digits that identify a specific dial peer. Valid entries are 1 to 2,147,483,647.

### Command Default

No default behavior or values

### Command Modes

Call filter match list configuration

## Command History

Release

Modification

12.3(4)T

This command was introduced.

## Examples

The following example shows the voice call debug filter set to match outgoing dial peer 12:

```
call filter match-list 1 voice
 outgoing dialpeer 12
```

### Related Commands

Command

Description

call filter match-list voice

Create a call filter match list for debugging voice calls.

debug condition match-list

Run a filtered debug on a voice call.

incoming called-number (call filter match list)

Configure debug filtering for incoming called numbers.

incoming calling-number

Configure debug filtering for incoming calling numbers.

incoming dialpeer

Configure debug filtering for the incoming dial peer.

incoming port

Configure debug filtering for the incoming port.

outgoing called-number

Configure debug filtering for outgoing called numbers.

outgoing calling-number

Configure debug filtering for outgoing calling numbers.

outgoing port

Configure debug filtering for the outgoing port.

show call filter match-list

Display call filter match lists.

## outgoing media local ipv4

To configure debug filtering for the outgoing media local IPv4 addresses for the voice gateway receiving the media stream,
                              use the outgoing media local ipv4 command in call filter match list configuration mode. To disable, use the no form of this command.

outgoing media local ipv4 ip_address

no outgoing media local ipv4 ip_address

### Syntax Description

ip_address

IP address of the local voice gateway

### Command Default

No default behavior or values

### Command Modes

Call filter match list configuration

## Command History

Release

Modification

12.3(4)T

This command was introduced.

## Examples

The following example shows the voice call debug filter set to match outgoing media on the local voice gateway, which has
                              IP address 192.168.10.255:

```
call filter match-list 1 voice
 outgoing media local ipv4 192.168.10.255
```

### Related Commands

Command

Description

call filter match-list voice

Create a call filter match list for debugging voice calls.

debug condition match-list

Run a filtered debug on a voice call.

incoming media local ipv4

Configure debug filtering for the incoming media IPv4 addresses for calls to the IP side from the local voice gateway.

incoming media remote ipv4

Configure debug filtering for the incoming media IPv4 addresses for calls to the IP side from the remote IP device.

incoming port

Configure debug filtering for the incoming port.

outgoing media remote ipv4

Configure debug filtering for the outgoing media IPv4 addresses for calls to the IP side from the remote IP device.

outgoing port

Configure debug filtering for the outgoing port.

show call filter match-list

Display call filter match lists.

## outgoing media remote ipv4

To configure debug filtering for the outgoing media remote IPv4 addresses for the voice gateway receiving the media stream,
                              use the outgoing media remote ipv4 command in call filter match list configuration mode. To disable, use the no form of this command.

outgoing media remote ipv4 ip_address

no outgoing media remote ipv4 ip_address

### Syntax Description

ip_address

IP address of the remote IP device

### Command Default

No default behavior or values

### Command Modes

Call filter match list configuration

## Command History

Release

Modification

12.3(4)T

This command was introduced.

## Examples

The following example shows the voice call debug filter set to match outgoing media on the remote IP device, which has IP
                              address 192.168.10.255:

```
call filter match-list 1 voice
 outgoing media remote ipv4 192.168.10.255
```

### Related Commands

Command

Description

call filter match-list voice

Create a call filter match list for debugging voice calls.

debug condition match-list

Run a filtered debug on a voice call.

incoming media local ipv4

Configure debug filtering for the incoming media IPv4 addresses for calls to the IP side from the local voice gateway.

incoming media remote ipv4

Configure debug filtering for the incoming media IPv4 addresses for calls to the IP side from the remote IP device.

incoming port

Configure debug filtering for the incoming port.

outgoing media local ipv4

Configure debug filtering for the outgoing media IPv4 addresses for calls to the IP side from the local voice gateway

outgoing port

Configure debug filtering for the outgoing port.

show call filter match-list

Display call filter match lists.

## outgoing port

To configure debug filtering for the outgoing port, use the outgoing
                              		  port command in call filter match list configuration mode. To disable, use the no form of this command.

### Cisco 2600, Cisco 3600, and Cisco 3700 Series

outgoing port { slot-number / subunit-number / port | slot / port : ds0-group-no }

no outgoing port { slot-number / subunit-number / port | slot / port : ds0-group-no }

### Cisco 2600 and Cisco 3600 Series with a High-Density Analog
                              			 Network Module (NM-HDA)

outgoing port { slot-number / subunit-number / port }

no outgoing port { slot-number / subunit-number / port }

### Cisco AS5300

outgoing port controller-number :D

no outgoing port controller-number :D

### Cisco AS5400

outgoing port card / port :D

no outgoing port card / port :D

### Cisco AS5800

outgoing port { shelf / slot / port :D | shelf / slot / parent : port :D }

no outgoing port { shelf / slot / port :D | shelf / slot / parent : port :D }

### Cisco MC3810

outgoing port slot / port

no outgoing port slot / port

### Cisco 2600, Cisco 3600, and Cisco 3700 Series

slot-number

Number of the slot in the router in which the VIC is
                                          						installed. Valid entries are 0 to 3, depending on the slot in which it has been
                                          						installed.

subunit-number

Subunit on the VIC in which the voice port is located.
                                          						Valid entries are 0 or 1.

port

Voice port number. Valid entries are 0 and 1.

slot

The router location in which the voice port adapter is
                                          						installed. Valid entries are 0 to 3.

port:

Indicates the voice interface card location. Valid entries
                                          						are 0 and 3.

ds0-group-no

Indicates the defined DS0 group number. Each defined DS0
                                          						group number is represented on a separate voice port. This allows you to define
                                          						individual DS0s on the digital T1/E1 card.

controller-number

T1 or E1 controller.

:D

D channel associated with ISDN PRI.

card

Specifies the T1 or E1 card. Valid entries for the card argument are 1 to 7.

port

Specifies the voice port number. Valid entries are 0 to 7.

:D

Indicates the D channel associated with ISDN PRI.

shelf

Specifies the T1 or E1 controller on the T1 card, or the T1
                                          						controller on the T3 card. Valid entries for the shelf argument are 0 to 9999.

slot

Specifies the T1 or E1 controller on the T1 card, or the T1
                                          						controller on the T3 card. Valid entries for the slot argument are 0 to 11.

port

Specifies the voice port number.

T1 or E1
                                                						  controller on the T1 card --Valid entries are 0 to 11.

T1 controller
                                                						  on the T3 card--Valid entries are 1 to 28

: port

Specifies the value for the parent argument. The only valid
                                          						entry is 0.

:D

Indicates the D channel associated with ISDN PRI.

slot

The slot argument specifies the number slot in the router
                                          						in which the VIC is installed. The only valid entry is 1.

port

The port variable specifies the voice port number. Valid
                                          						interface ranges are as follows:

T1--ANSI T1.403
                                                						  (1989), Telcordia TR-54016.

E1-- ITU G.703.

Analog
                                                						  voice--Up to six ports (FXS, FXO, E & M).

Digital voice--
                                                						  Single T1/E1 with cross-connect drop and insert, CAS and CCS signaling, PRI
                                                						  QSIG.

Ethernet--Single 10BASE-T.

Serial--Two
                                                						  five-in-one synchronous serial (ANSI EIA/TIA-530, EIA/TIA-232, EIA/TIA-449; ITU
                                                						  V.35, X.21, Bisync, Polled async).

### Command Default

No default behavior or values

### Command Modes

Call filter match list configuration

## Command History

Release

Modification

12.3(4)T

This command was introduced.

## Examples

The following example shows the voice call debug filter set to match
                              		  outgoing port 1/1/1 on a Cisco 3660 voice gateway:

```
call filter match-list 1 voice
 outgoing port 1/1/1
```

### Related Commands

Command

Description

call filter match-list voice

Create a call filter match list for debugging voice calls.

debug condition match-list

Run a filtered debug on a voice call.

incoming port

Configure debug filtering for the incoming port.

show call filter match-list

Display call filter match lists.

## outgoing signaling local ipv4

To configure debug filtering for the outgoing signaling local IPv4 addresses for the gatekeeper managing the signaling, use
                              the outgoing signaling local ipv4 command in call filter match list configuration mode. To disable, use the no form of this command.

outgoing signaling local ipv4 ip_address

no outgoing signaling local ipv4 ip_address

### Syntax Description

ip_address

IP address of the local voice gateway

### Command Default

No default behavior or values

### Command Modes

Call filter match list configuration

## Command History

Release

Modification

12.3(4)T

This command was introduced.

## Examples

The following example shows the voice call debug filter set to match outgoing signaling on the local voice gateway, which
                              has IP address 192.168.10.255:

```
call filter match-list 1 voice
 outgoing signaling local ipv4 192.168.10.255
```

### Related Commands

Command

Description

call filter match-list voice

Create a call filter match list for debugging voice calls.

debug condition match-list

Run a filtered debug on a voice call.

incoming port

Configure debug filtering for the incoming port.

incoming signaling local ipv4

Configure debug filtering for the incoming signaling IPv4 addresses for calls to the IP side from the local voice gateway.

incoming signaling remote ipv4

Configure debug filtering for the incoming signaling IPv4 addresses for calls to the IP side from the remote IP device.

outgoing port

Configure debug filtering for the outgoing port.

outgoing signaling remote ipv4

Configure debug filtering for the outgoing signaling IPv4 addresses for calls to the IP side from the remote IP device.

show call filter match-list

Display call filter match lists.

## outgoing signaling remote ipv4

To configure debug filtering for the outgoing signaling remote IPv4 addresses for the gatekeeper managing the signaling, use
                              the outgoing signaling remote ipv4 command in call filter match list configuration mode. To disable, use the no form of this command.

outgoing signaling remote ipv4 ip_address

no outgoing signaling remote ipv4 ip_address

### Syntax Description

ip_address

IP address of the remote IP device

### Command Default

No default behavior or values

### Command Modes

Call filter match list configuration

## Command History

Release

Modification

12.3(4)T

This command was introduced.

## Examples

The following example shows the voice call debug filter set to match outgoing signaling on the remote IP device, which has
                              IP address 192.168.10.255:

```
call filter match-list 1 voice
 outgoing signaling remote ipv4 192.168.10.255
```

### Related Commands

Command

Description

call filter match-list voice

Create a call filter match list for debugging voice calls.

debug condition match-list

Run a filtered debug on a voice call.

incoming port

Configure debug filtering for the incoming port.

incoming signaling local ipv4

Configure debug filtering for the incoming signaling IPv4 addresses for calls to the IP side from the local voice gateway.

incoming signaling remote ipv4

Configure debug filtering for the incoming signaling IPv4 addresses for calls to the IP side from the remote IP device.

outgoing port

Configure debug filtering for the outgoing port.

outgoing signaling local ipv4

Configure debug filtering for the outgoing signaling IPv4 addresses for calls to the IP side from the local voice gateway.

show call filter match-list

Display call filter match lists.

## output attenuation

To configure a specific output attenuation value or enable automatic gain control, use the output attenuation command in voice-port configuration mode. To disable the selected output attenuation value, use the no form of this command.

output attenuation { decibels | auto-control [auto-dbm] }

no output attenuation { decibels | auto-control [auto-dbm] }

### Syntax Description

decibels

Attenuation, in decibels (dB), at the transmit side of the interface. Range is integers from -6 to 14. The default is 3.

auto-control

Enable automatic gain control.

auto-dbm

(Optional) Target speech level, in decibels per milliwatt (dBm), to be achieved at the transmit side of the interface. Range
                                          is integers from -30 to 3. The default is -9.

### Command Default

For Foreign Exchange Office (FXO), Foreign Exchange Station (FXS), and ear and mouth (E&M) ports: decibels : 3 decibels auto-dbm : -9 dBm

### Command Modes

Voice-port configuration

## Command History

Release

Modification

11.3(1)T

This command was introduced on the Cisco 3600 series.

11.3(1)MA

This command was implemented on the Cisco MC3810.

12.3(4)XD

The range of values for the decibels argument was increased.

12.3(7)T

This command was integrated into Cisco IOS Release 12.3(7)T.

12.3(14)T

This command was implemented on the Cisco 2800 series and Cisco 3800 series.

12.4(2)T

The auto-control keyword and auto-dbm argument were added.

### Usage Guidelines

A system-wide loss plan must be implemented using both the input gain and output attenuation commands. You must consider other equipment (including PBXs) in the system when creating a loss plan. The default value for
                              this command assumes that a standard transmission loss plan is in effect, meaning that there must be an attenuation of -6
                              dB between phones. Connections are implemented to provide -6 dB of attenuation when the input gain and output attenuation commands are configured with the default value of 3 dB.

You cannot increase the gain of a signal to the public switched telephone network (PSTN), but you can decrease it. If the
                              voice level is too high, you can decrease the volume by either decreasing the input gain or increasing the output attenuation.

You can increase the gain of a signal coming into the router. If the voice level is too low, you can increase the input gain
                              by using the input gain command.

The auto-control keyword and auto-dbm argument are available on an ear and mouth (E&M) voice port only if the signal type for that port is Land Mobile Radio (LMR).
                              The auto-control keyword enables automatic gain control, which is performed by the digital signal processor (DSP). Automatic gain control adjusts
                              speech to a comfortable volume when it becomes too loud or too soft. Because of radio network loss and other environmental
                              factors, the speech level arriving at a router from an LMR system could be very low. You can use automatic gain control to
                              ensure that the speech is played back at a more comfortable level. Because the gain is inserted digitally, the background
                              noise can also be amplified. Automatic gain control is implemented as follows:

Output level: -9 dB

Gain range: -12 dB to 20 dB

Attack time (low to high): 30 milliseconds

Attack time (high to low): 8 seconds

## Examples

On the Cisco 3600 series router, the following example configures a 3-dB loss to be inserted at the transmit side of the interface:

```
voice-port 1/0/0
 output attenuation 3
```

On the Cisco 3600 series router, the following example configures a 3-dB gain to be inserted at the transmit side of the interface:

```
voice-port 1/0/0
 output attenuation -3
```

On the Cisco AS5300, the following example configures a 3-dB loss to be inserted at the transmit side of the interface:

```
voice-port 0:D
 output attenuation 3
```

### Related Commands

Command

Description

comfort-noise

Generates background noise to fill silent gaps during calls if VAD is activated.

echo-cancel enable

Enables the cancellation of voice that is sent out the interface and received back on the same interface.

input gain

Configures a specific input gain value or enables automatic gain control for a voice port.

## overhead

To configure the overhead negotiated bandwidth percentage, use the overhead command in media profile configuration mode. To disable the configuration, use the no form of the command.

overhead { audio | video } percentage

no overhead { audio | video }

### Syntax Description

audio

Configures the audio overhead percentage.

video

Configures the video overhead percentage.

percentage

Overhead percentage. The range is from 0 to 50.

### Command Default

Overhead negotiated bandwidth is not configured.

### Command Modes

Media profile configuration (cfg-mediaprofile)

## Command History

Release

Modification

15.2(2)T

This command was introduced.

### Usage Guidelines

The overhead bandwidth is the extra bandwidth apart from the negotiated bandwidth for audio and video calls. Hence, the total
                              policing bandwidth is:

Policing bandwidth = negotiated bandwidth + (1 + % overhead bandwidth)

## Examples

The following example shows how to configure an overhead bandwidth of 10 percent for audio codecs and 20 percent for video
                              codecs:

```
Router> enable Router# configure terminal Router(config)# media profile police 1 Router(cfg-mediaprofile)# overhead audio 10 Router(cfg-mediaprofile)# overhead video 20
```

### Related Commands

Command

Description

media profile police

Configures the media policing profile.

| conn-addr | Specifies
                                          						the RFC 2543 method of using the connection address for initiating call-hold
                                          						requests. The RFC 2543 method uses 0.0.0.0. |
|---|---|
| direction-attr | Specifies
                                          						the current RFC 3264 method of using the direction attribute (a=sendonly) for
                                          						initiating call-hold requests. |
| system | Specifies how the call-hold requests use the global sip-ua
                                          						value. This keyword is available only for the tenant mode to allow it to
                                          						fallback to the global configurations |

| Release | Modification |
|---|---|
| 12.3(8)T | This
                                          						command was introduced. |
| 15.6(2)T and IOS XE Denali 16.3.1 | This command was modified to include the keyword: system . |

| Command | Description |
|---|---|
| show sip-ua status | Displays
                                          						status for the SIP UA. |
| suspend-resume | Enables
                                          						SIP Suspend and Resume functionality. |

| 2 - wire | Two-wire E&M cabling scheme. |
|---|---|
| 4 - wire | Four-wire E&M cabling scheme. |

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced on the Cisco 3600 series. |
| 11.3(1)MA | This command was implemented on the Cisco MC3810. |

| seconds | Intervals, in seconds OPTIONS transactions are sent. Range is 60-1200, there is
                                          						no default. |
|---|---|
| system | Specifies
                                          						that the in-dialog OPTIONS, use the global sip-ua value. This keyword is
                                          						available only for the tenant mode to allow it to fallback to the global
                                          						configurations |

| Release | Modification |
|---|---|
| 12.4(11)T | This
                                          						command was introduced. |
| 15.6(2)T and IOS XE Denali 16.3.1 | This command was modified to include the keyword: system . |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| options-ping | Enables
                                          						in-dialog OPTIONS at the global level. |
| options-ping (dial peer) | Enables
                                          						in-dialog OPTIONS on a dial-peer. |

| seconds | Intervals, in seconds OPTIONS transactions are sent. Range is 60-1200, there is no default. |
|---|---|

| Release | Modification |
|---|---|
| 12.4(11)T | This command was introduced. |

| Command | Description |
|---|---|
| options-ping | Enables in-dialog OPTIONS at the global level. |
| options-ping (dial peer) | Enables in-dialog OPTIONS on a dial-peer. |

| dhcp | Specifies
                                          						the SIP outbound proxy globally for a Cisco IOS voice gateway; all SIP
                                          						dialog-initiating requests are sent to the SIP server obtained via DHCP. |
|---|---|
| ipv4 : ip-address | Specifies
                                          						the SIP outbound proxy globally for a Cisco IOS voice gateway; all SIP
                                          						dialog-initiating requests are sent to this IP address. The colon is required. |
| : port-number | (Optional) The port to which all SIP dialog-initiating requests are sent at the
                                          						specified IP address. Port number ranges from 0 to 65535. The default is 5060.
                                          						The colon is required. |
| dns : host : domain | Specifies
                                          						the SIP outbound proxy globally for a Cisco IOS voice gateway; all initiating
                                          						requests are sent to the specified destination domain. The colon is required. |
| reuse | (Optional) Reuses the outbound proxy address established during registration
                                          						for all subsequent registration refreshes and calls. |
| system | Specifies that the outbound proxy for outgoing SIP messages use
                                          						the global sip-ua value. This keyword is available only for the tenant mode to
                                          						allow it to fallback to the global configurations |

| Release | Modification |
|---|---|
| 12.4(15)T | This
                                          						command was introduced. |
| 12.4(22)T | Support
                                          						for IPv6 was added. |
| 12.4(22)YB | This
                                          						command was modifed. The dhcp keyword
                                          						was added. |
| 15.0(1)M | This
                                          						command was integrated in Cisco IOS Release 15.0(1)M. |
| 15.1(2)T | This
                                          						command was modified. The reuse keyword
                                          						was added. |
| 15.6(2)T and IOS XE Denali 16.3.1 | This command was modified to include the keyword: system . |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| outbound-proxy system | Specifies whether Cisco Unified CME line-side SIP phones use the outbound proxy
                                          						settings configured globally for a Cisco IOS voice gateway. |
| voice-class sip outbound-proxy | Configures SIP outbound proxy settings for an individual dial peer that
                                          						override global settings for the Cisco IOS voice gateway. |

| interval | Amount of time, in seconds, to establish the outbound relationship. Range is from 1 to 2147483. The default is 30. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |

| Command | Description |
|---|---|
| access - policy | Requires that a neighbor be explicitly configured. |
| inbound ttl | Sets the inbound time-to-live value. |
| retry interval | Defines the time between delivery attempts. |
| retry window | Defines the total time that a border element will attempt delivery. |
| service - relationship | Establishes a service relationship between two border elements. |
| shutdown | Enables or disables the border element. |

| string | Series of digits that specify a pattern for the E.164 or private dialing plan telephone number. Valid entries are the digits
                                          0 to 9, the letters A to D, and the following special characters: The asterisk (*) and pound sign (#) that appear on standard touchtone dial pads. On the Cisco 3600 series routers only, these
                                                characters cannot be used as leading characters in a string (for example, *650). Comma (,), which inserts a pause between digits. Period (.), which matches any entered digit (this character is used as a wildcard). On the Cisco 3600 series routers, the
                                                period cannot be used as a leading character in a string (for example, .650). Percent sign (%), which indicates that the preceding digit occurred zero or more times; similar to the wildcard usage. Plus sign (+), which indicates that the preceding digit occurred one or more times. Note The plus sign used as part of a digit string is different from the plus sign that can be used in front of a digit string to
                                                      indicate that the string is an E.164 standard number. Circumflex (^), which indicates a match to the beginning of the string. Dollar sign ($), which matches the null string at the end of the input string. Backslash symbol (\), which is followed by a single character; matches that character. Can be used with a single character
                                                with no other significance (matching that character). Question mark (?), which indicates that the preceding digit occurred zero or one time. Brackets ( [ ] ), which indicate a range. A range is a sequence of characters enclosed in the brackets; only numeric characters
                                                0 to 9 are allowed in the range. Parentheses ( ), which indicate a pattern and are the same as the regular expression rule. | Note | The plus sign used as part of a digit string is different from the plus sign that can be used in front of a digit string to
                                                      indicate that the string is an E.164 standard number. |
|---|---|---|---|
| Note | The plus sign used as part of a digit string is different from the plus sign that can be used in front of a digit string to
                                                      indicate that the string is an E.164 standard number. |

| Note | The plus sign used as part of a digit string is different from the plus sign that can be used in front of a digit string to
                                                      indicate that the string is an E.164 standard number. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Command | Description |
|---|---|
| call filter match-list voice | Create a call filter match list for debugging voice calls. |
| debug condition match-list | Run a filtered debug on a voice call. |
| incoming called-number (call filter match list) | Configure debug filtering for incoming called numbers. |
| incoming calling-number | Configure debug filtering for incoming calling numbers. |
| incoming dialpeer | Configure debug filtering for the incoming dial peer. |
| incoming secondary-called-number | Configure debug filtering for incoming called numbers from the second stage of a two-stage scenario. |
| outgoing calling-number | Configure debug filtering for outgoing calling numbers. |
| outgoing dialpeer | Configure debug filtering for the outgoing dial peer. |
| show call filter match-list | Display call filter match lists. |

| string | Series of digits that specify a pattern for the E.164 or private dialing plan telephone number. Valid entries are the digits
                                          0 to 9, the letters A to D, and the following special characters: The asterisk (*) and pound sign (#) that appear on standard touchtone dial pads. On the Cisco 3600 series routers only, these
                                                characters cannot be used as leading characters in a string (for example, *650). Comma (,), which inserts a pause between digits. Period (.), which matches any entered digit (this character is used as a wildcard). On the Cisco 3600 series routers, the
                                                period cannot be used as a leading character in a string (for example, .650). Percent sign (%), which indicates that the preceding digit occurred zero or more times; similar to the wildcard usage. Plus sign (+), which indicates that the preceding digit occurred one or more times. Note The plus sign used as part of a digit string is different from the plus sign that can be used in front of a digit string to
                                                      indicate that the string is an E.164 standard number. Circumflex (^), which indicates a match to the beginning of the string. Dollar sign ($), which matches the null string at the end of the input string. Backslash symbol (\), which is followed by a single character; matches that character. Can be used with a single character
                                                with no other significance (matching that character). Question mark (?), which indicates that the preceding digit occurred zero or one time. Brackets ( [ ] ), which indicate a range. A range is a sequence of characters enclosed in the brackets; only numeric characters
                                                0 to 9 are allowed in the range. Parentheses ( ), which indicate a pattern and are the same as the regular expression rule. | Note | The plus sign used as part of a digit string is different from the plus sign that can be used in front of a digit string to
                                                      indicate that the string is an E.164 standard number. |
|---|---|---|---|
| Note | The plus sign used as part of a digit string is different from the plus sign that can be used in front of a digit string to
                                                      indicate that the string is an E.164 standard number. |

| Note | The plus sign used as part of a digit string is different from the plus sign that can be used in front of a digit string to
                                                      indicate that the string is an E.164 standard number. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Command | Description |
|---|---|
| call filter match-list voice | Create a call filter match list for debugging voice calls. |
| debug condition match-list | Run a filtered debug on a voice call. |
| incoming called-number (call filter match list) | Configure debug filtering for incoming called numbers. |
| incoming calling-number | Configure debug filtering for incoming calling numbers. |
| incoming dialpeer | Configure debug filtering for the incoming dial peer. |
| incoming secondary-called-number | Configure debug filtering for incoming called numbers from the second stage of a two-stage scenario. |
| outgoing called-number | Configure debug filtering for outgoing called numbers. |
| outgoing dialpeer | Configure debug filtering for the outgoing dial peer. |
| show call filter match-list | Display call filter match lists. |

| tag | Digits that identify a specific dial peer. Valid entries are 1 to 2,147,483,647. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Command | Description |
|---|---|
| call filter match-list voice | Create a call filter match list for debugging voice calls. |
| debug condition match-list | Run a filtered debug on a voice call. |
| incoming called-number (call filter match list) | Configure debug filtering for incoming called numbers. |
| incoming calling-number | Configure debug filtering for incoming calling numbers. |
| incoming dialpeer | Configure debug filtering for the incoming dial peer. |
| incoming port | Configure debug filtering for the incoming port. |
| outgoing called-number | Configure debug filtering for outgoing called numbers. |
| outgoing calling-number | Configure debug filtering for outgoing calling numbers. |
| outgoing port | Configure debug filtering for the outgoing port. |
| show call filter match-list | Display call filter match lists. |

| ip_address | IP address of the local voice gateway |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Command | Description |
|---|---|
| call filter match-list voice | Create a call filter match list for debugging voice calls. |
| debug condition match-list | Run a filtered debug on a voice call. |
| incoming media local ipv4 | Configure debug filtering for the incoming media IPv4 addresses for calls to the IP side from the local voice gateway. |
| incoming media remote ipv4 | Configure debug filtering for the incoming media IPv4 addresses for calls to the IP side from the remote IP device. |
| incoming port | Configure debug filtering for the incoming port. |
| outgoing media remote ipv4 | Configure debug filtering for the outgoing media IPv4 addresses for calls to the IP side from the remote IP device. |
| outgoing port | Configure debug filtering for the outgoing port. |
| show call filter match-list | Display call filter match lists. |

| ip_address | IP address of the remote IP device |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Command | Description |
|---|---|
| call filter match-list voice | Create a call filter match list for debugging voice calls. |
| debug condition match-list | Run a filtered debug on a voice call. |
| incoming media local ipv4 | Configure debug filtering for the incoming media IPv4 addresses for calls to the IP side from the local voice gateway. |
| incoming media remote ipv4 | Configure debug filtering for the incoming media IPv4 addresses for calls to the IP side from the remote IP device. |
| incoming port | Configure debug filtering for the incoming port. |
| outgoing media local ipv4 | Configure debug filtering for the outgoing media IPv4 addresses for calls to the IP side from the local voice gateway |
| outgoing port | Configure debug filtering for the outgoing port. |
| show call filter match-list | Display call filter match lists. |

| slot-number | Number of the slot in the router in which the VIC is
                                          						installed. Valid entries are 0 to 3, depending on the slot in which it has been
                                          						installed. |
|---|---|
| subunit-number | Subunit on the VIC in which the voice port is located.
                                          						Valid entries are 0 or 1. |
| port | Voice port number. Valid entries are 0 and 1. |
| slot | The router location in which the voice port adapter is
                                          						installed. Valid entries are 0 to 3. |
| port: | Indicates the voice interface card location. Valid entries
                                          						are 0 and 3. |
| ds0-group-no | Indicates the defined DS0 group number. Each defined DS0
                                          						group number is represented on a separate voice port. This allows you to define
                                          						individual DS0s on the digital T1/E1 card. |

| controller-number | T1 or E1 controller. |
|---|---|
| :D | D channel associated with ISDN PRI. |

| card | Specifies the T1 or E1 card. Valid entries for the card argument are 1 to 7. |
|---|---|
| port | Specifies the voice port number. Valid entries are 0 to 7. |
| :D | Indicates the D channel associated with ISDN PRI. |

| shelf | Specifies the T1 or E1 controller on the T1 card, or the T1
                                          						controller on the T3 card. Valid entries for the shelf argument are 0 to 9999. |
|---|---|
| slot | Specifies the T1 or E1 controller on the T1 card, or the T1
                                          						controller on the T3 card. Valid entries for the slot argument are 0 to 11. |
| port | Specifies the voice port number. T1 or E1
                                                						  controller on the T1 card --Valid entries are 0 to 11. T1 controller
                                                						  on the T3 card--Valid entries are 1 to 28 |
| : port | Specifies the value for the parent argument. The only valid
                                          						entry is 0. |
| :D | Indicates the D channel associated with ISDN PRI. |

| slot | The slot argument specifies the number slot in the router
                                          						in which the VIC is installed. The only valid entry is 1. |
|---|---|
| port | The port variable specifies the voice port number. Valid
                                          						interface ranges are as follows: T1--ANSI T1.403
                                                						  (1989), Telcordia TR-54016. E1-- ITU G.703. Analog
                                                						  voice--Up to six ports (FXS, FXO, E & M). Digital voice--
                                                						  Single T1/E1 with cross-connect drop and insert, CAS and CCS signaling, PRI
                                                						  QSIG. Ethernet--Single 10BASE-T. Serial--Two
                                                						  five-in-one synchronous serial (ANSI EIA/TIA-530, EIA/TIA-232, EIA/TIA-449; ITU
                                                						  V.35, X.21, Bisync, Polled async). |

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Command | Description |
|---|---|
| call filter match-list voice | Create a call filter match list for debugging voice calls. |
| debug condition match-list | Run a filtered debug on a voice call. |
| incoming port | Configure debug filtering for the incoming port. |
| show call filter match-list | Display call filter match lists. |

| ip_address | IP address of the local voice gateway |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Command | Description |
|---|---|
| call filter match-list voice | Create a call filter match list for debugging voice calls. |
| debug condition match-list | Run a filtered debug on a voice call. |
| incoming port | Configure debug filtering for the incoming port. |
| incoming signaling local ipv4 | Configure debug filtering for the incoming signaling IPv4 addresses for calls to the IP side from the local voice gateway. |
| incoming signaling remote ipv4 | Configure debug filtering for the incoming signaling IPv4 addresses for calls to the IP side from the remote IP device. |
| outgoing port | Configure debug filtering for the outgoing port. |
| outgoing signaling remote ipv4 | Configure debug filtering for the outgoing signaling IPv4 addresses for calls to the IP side from the remote IP device. |
| show call filter match-list | Display call filter match lists. |

| ip_address | IP address of the remote IP device |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Command | Description |
|---|---|
| call filter match-list voice | Create a call filter match list for debugging voice calls. |
| debug condition match-list | Run a filtered debug on a voice call. |
| incoming port | Configure debug filtering for the incoming port. |
| incoming signaling local ipv4 | Configure debug filtering for the incoming signaling IPv4 addresses for calls to the IP side from the local voice gateway. |
| incoming signaling remote ipv4 | Configure debug filtering for the incoming signaling IPv4 addresses for calls to the IP side from the remote IP device. |
| outgoing port | Configure debug filtering for the outgoing port. |
| outgoing signaling local ipv4 | Configure debug filtering for the outgoing signaling IPv4 addresses for calls to the IP side from the local voice gateway. |
| show call filter match-list | Display call filter match lists. |

| decibels | Attenuation, in decibels (dB), at the transmit side of the interface. Range is integers from -6 to 14. The default is 3. |
|---|---|
| auto-control | Enable automatic gain control. |
| auto-dbm | (Optional) Target speech level, in decibels per milliwatt (dBm), to be achieved at the transmit side of the interface. Range
                                          is integers from -30 to 3. The default is -9. |

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced on the Cisco 3600 series. |
| 11.3(1)MA | This command was implemented on the Cisco MC3810. |
| 12.3(4)XD | The range of values for the decibels argument was increased. |
| 12.3(7)T | This command was integrated into Cisco IOS Release 12.3(7)T. |
| 12.3(14)T | This command was implemented on the Cisco 2800 series and Cisco 3800 series. |
| 12.4(2)T | The auto-control keyword and auto-dbm argument were added. |

| Command | Description |
|---|---|
| comfort-noise | Generates background noise to fill silent gaps during calls if VAD is activated. |
| echo-cancel enable | Enables the cancellation of voice that is sent out the interface and received back on the same interface. |
| input gain | Configures a specific input gain value or enables automatic gain control for a voice port. |

| audio | Configures the audio overhead percentage. |
|---|---|
| video | Configures the video overhead percentage. |
| percentage | Overhead percentage. The range is from 0 to 50. |

| Release | Modification |
|---|---|
| 15.2(2)T | This command was introduced. |

| Command | Description |
|---|---|
| media profile police | Configures the media policing profile. |