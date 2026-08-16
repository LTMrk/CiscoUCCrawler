---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-vcr5-vcr5-cr-book-vcr-u1-html-fc23d8b6a3
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/vcr5/vcr5-cr-book/vcr-u1.html
retrieved_at: 2026-08-16T23:14:19.803305+00:00
---

Cisco IOS Voice Command Reference - T through Z

# Cisco IOS Voice Command Reference - T through Z

Updated: April 25, 2026

Chapter: U

## Chapter: U

# U

## uc wsapi

To configure the
                              		  nonsecure Cisco Unified Communication IOS services environment for a specific
                              		  application, use the uc wsapi command. To remove the configuration, use no form of
                              		  this command.

uc wsapi

no uc wsapi

### Syntax Description

This command has
                              		  no arguments or keywords.

### Command Default

This command has no
                              		  default behavior or values.

### Command Modes

EXEC mode

## Command History

Release

Modification

15.2(2)T

This
                                          						command was introduced.

Cisco IOS XE Everest 16.6.1

This command extended support for configuring Cisco Unified
                                          						Communication IOS services environment using HTTPS connection.

Introduced support for YANG models.

### Usage Guidelines

Use uc wsapi command to enter the Cisco Unified Communication IOS services configuration environment in nonsecure mode.

If you intend to move from secure mode to nonsecure mode, remove the
                                          			 existing uc secure-wsapi configuration and reconfigure in nonsecure mode.

## Examples

The following
                              		  example enters the Cisco Unified Communication IOS services configuration:

```
Router(config)# uc wsapi Router(config-uc-wsapi)#
```

### Related Commands

Command

Description

provider

Enables a
                                          						provider service.

## uc
                        	 secure-wsapi

To configure
                              		  secure Cisco Unified Communication IOS services environment for a specific
                              		  application, use the uc secure-wsapi command. To remove the configuration, use no form of
                              		  this command.

uc secure-wsapi

no uc
                                 				  secure-wsapi

### Syntax Description

This command
                              		  has no arguments or keywords.

### Command Default

This command
                              		  has no default behavior or values.

### Command Modes

EXEC mode

## Command History

Cisco
                                       					 IOS XE Everest 16.6.1

This
                                       					 command was introduced.

Introduced support for YANG models.

### Usage Guidelines

Use uc secure-wsapi command to enter the Cisco Unified Communication IOS
                              		  services configuration environment in secure mode.

If you intend
                                          			 to move from nonsecure mode to secure mode, remove the existing uc wsapi configuration and reconfigure in secure mode.

## Examples

The following
                              		  example enters the Cisco Unified Communication IOS services configuration in
                              		  secure mode:

```
Router(config)# uc secure-wsapi Router(config-uc-wsapi)#
```

### Related Commands

Command

Description

provider

Enables a provider service.

## unbundle vfc

To unbundle DSPWare from the VCWare and configure the default file and capability lists with default values, use the unbundle vfc command in privileged EXEC mode.

unbundle [ high-complexity | medium-complexity ] vfc slot-number

### Syntax Description

high - complexity

(Optional) High-complexity firmware set.

medium - complexity

(Optional) Medium-complexity firmware set.

slot - number

Voice feature card (VFC) slot number.

### Command Default

No default behavior or values

### Command Modes

Privileged EXEC

## Command History

Release

Modification

11.3(2)NA

This command was introduced on the Cisco AS5300.

12.0(2)XH

The high - complexity and medium - complexity keywords were added.

12.0(3)T

This command was integrated into Cisco IOS Release 12.0(3)T.

### Usage Guidelines

VFCs come with a single bundled image, VCWare, stored in VFC Flash memory. Use this command to unbundle this bundled image
                              into separate files, which are then written to Flash memory. When VCWare is unbundled, it automatically adds DSPWare to Flash
                              memory, creates both the capability and default file lists, and populates these lists with the default files for that version
                              of VCWare. The default file list includes the files to be used to boot up the system. The capability list defines the available
                              voice codecs for H.323 capability negotiation. These files are used during initial card configuration and for subsequent firmware
                              upgrades.

Before unbundling a VFC software image that you have just copied over to VFC Flash, use the clear vfc command. Unbundling a DSP firmware set rewrites the default-file and capabilities lists. After unbundling, you must reload
                              the router for any changes to take effect.

## Examples

The following example unbundles the high-complexity firmware set into slot 2:

```
Router# unbundle high-complexity vfc 2
```

### Related Commands

Command

Description

clear vfc

Resets the VFC.

copy flash vfc

Copies a new version of VCWare from the Cisco AS5300 motherboard to VFC Flash memory.

copy tftp vfc

Copies a new version of VCWare from a TFTP server to VFC Flash memory.

## update-callerid

To enable sending updates for callerid, use the udpate-callerid command in the Session Initiation Protocol (SIP) configuration mode. To disable this configuration, use the no form of this command.

udpate-callerid

no udpate-callerid

### Syntax Description

### Command Default

Enabled by default.

### Command Modes

Session Initiation Protocol (SIP) configuration mode (conf-voi-serv).

Voice class tenant configuration mode.

## Command History

Release

Modification

15.4(1)T

Cisco IOS XE 3.11S

This command was introduced.

Cisco IOS XE Cupertino 17.7.1a

Introduced support for YANG models.

### Usage Guidelines

By default, update-callerid configuration is enabled at global level and CUBE sends an UPDATE message during call transfer handling on CUBE . If you do not need to send callerid UPDATE, disable this configuration at global level. If specific trunks require callerid
                              UPDATE  to be sent, it can be enabled at tenant level.

## Examples

The following example shows how to enable udpate-callerid using the udpate-callerid command:

```
Device> enable
Device# configure terminal
Device(config)# voice service voip
Device(conf-voi-serv)# sip
Device(conf-serv-sip)# udpate-callerid
Device(conf-serv-sip)# end
```

### Related Commands

Command

Description

## url

To configure the Internet service provider (ISP) address, use the url command in settlement configuration mode. To disable the address, use the no form of this command.

url url-address

no url url-address

### Syntax Description

url-address

URL address. A valid URL address is as follows:
                                          http:// fully qualified domain nam e[: port ]/[ URL ]

### Command Default

No default behavior or values

### Command Modes

Settlement configuration

## Command History

Release

Modification

12.0(4)XH1

This command was introduced on Cisco 2600 series and Cisco 3600 series, and Cisco AS5300.

12.1(1)T

This command was integrated into Cisco IOS Release 12.1(1)T.

12.2(11)T

The settlement configuration for this command was modified. The settlement provider must be shut down before the url command is entered.

### Usage Guidelines

You can configure the address type multiple times. If you configure multiple URLs for the settlement server, the gateway attempts
                              to send the request to each URL in the order in which you configured these addresses.

If the first URL is unsuccessful, the gateway tries the next URL. If the first URL becomes available, the gateway does not
                              switch back until it loops through the list of URLs, for example:

url http://example1.com

url http://example2.com

url http://example3.com

If http://example1.com fails, the gateway sends the request to http://example2.com. If http://example1.com comes back online,
                              the gateway continues to send requests to http://example2.com. Later on, if http://example2 is down, the gateway sends requests
                              to http://example3.com.

When http://servicepoint3.com is down the gateway routes its requests back to http://example1.com.

## Examples

The following example shows four URLs configured for the settlement server:

```
settlement 0
 url http://1.2.3.4/
 url http://1.2.3.4:80/
 url https://1.2.3.4:4444/
 url https://example.com:443/
```

### Related Commands

Command

Description

connection-timeout

Sets the connection timeout.

customer-id

Sets the customer identification.

device-id

Sets the device identification.

encryption

Specifies the encryption method.

max-connection

Sets the maximum simultaneous connections.

response-timeout

Sets the response timeout.

retry-delay

Sets the retry delay.

retry-limit

Sets the connection retry limit.

session-timeout

Sets the session timeout.

settlement

Enters settlement configuration mode.

show settlement

Displays the configuration for all settlement server transactions.

shutdown

Brings up the settlement provider.

no shutdown

Shuts down the settlement provider.

type

Specifies the provider type.

## url (dial peer)

To specify the URL of a text file that has E.164 patterns configured on a destination E.164 pattern map, use the url command in dial-peer configuration mode. To remove the URL of the text file, use the no form of this command.

url url

no url url

### Syntax Description

url

The URL of an internally or an externally stored text file that has been used on an E.164 pattern map.

### Command Default

The URL is not specified for a text file that is configured on an E.164 pattern map.

### Command Modes

Dial peer configuration (config-dial-peer)

## Command History

Release

Modification

15.2(4)M

This command was introduced.

## Examples

The following example shows how to specify the URL of a text file configured on an E.164 pattern map:

```
Device(config)# dial-peer voice 123 voip system Device(config-dial-peer)# url http://http-host/config-files/destination-pattern-map.cfg
```

### Related Commands

Command

Description

destination e164-pattern-map

Links an E.164 pattern map to a dial peer.

e164

Configures an E.164 pattern entry on a destination E.164 pattern map.

show voice class e164-pattern-map

Displays details of the configuration of a voice class E.164 pattern map.

voice class e164-pattern-map load

Loads a destination E.164 pattern map specified by a text file.

## url (SIP)

To configure URLs
                              		  to either the Session Initiation Protocol (SIP), SIP secure (SIPS), or
                              		  telephone (TEL) format for your VoIP SIP calls, use the url command in
                              		  SIP configuration mode voice class tenant configuration mode. To reset to the
                              		  default, use the no form of this
                              		  command.

url { sip | sips | system | tel [ phone-context ]}

no url

### Syntax Description

sip

Generates
                                          						URLs in SIP format for VoIP calls.

sips

Generates
                                          						URLs in SIPS format for VoIP calls.

system

Specifies that the URLs use the global sip-ua value. This
                                          						keyword is available only for the tenant mode to allow it to fallback to the
                                          						global configurations.

tel

Generates
                                          						URLs in TEL format for VoIP calls.

phone-context

(Optional) Appends the phone-context parameter to the TEL URL.

### Command Default

SIP URLs

### Command Modes

SIP configuration (conf-serv-sip).

Voice class tenant configuration (config-class).

## Command History

Release

Modification

12.2(2)XB

This
                                          						command was introduced.

12.2(2)XB1

This
                                          						command was implemented on the Cisco AS5850.

12.2(8)T

This
                                          						command was integrated into Cisco IOS Release 12.2(8)T. Support for the Cisco
                                          						AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 was not included in this
                                          						release.

12.2(11)T

This
                                          						command was implemented on the Cisco AS5300, Cisco AS5350, and Cisco AS5400
                                          						platforms.

12.4(6)T

The sips keyword
                                          						was added.

12.4(22)YB

The phone-context keyword was added.

12.4(24)T

This
                                          						command was integrated into Cisco IOS Release 12.4(24)T.

15.6(2)T
                                          						and IOS XE Denali 16.3.1

This
                                          						command was modified to include the keyword: system . This
                                          						command is now available under voice class tenants.

Introduced support for YANG models.

### Usage Guidelines

This command
                              		  affects only user-agent clients (UACs), because it causes the use of a SIP,
                              		  SIPS, or TEL URL in the request line of outgoing SIP INVITE requests. SIP URLs
                              		  indicate the originator, recipient, and destination of the SIP request; TEL
                              		  URLs indicate voice call connections.

The voice-class sip url command takes precedence over the url command
                              		  configured in SIP global configuration mode. However, if the voice-class sip url command is configured with the system keyword, the gateway uses what was globally configured with the url command.

Enter SIP
                              		  configuration mode after entering voice-service VoIP configuration mode, as
                              		  shown in the "Examples" section.

## Examples

The following
                              		  example generates URLs in SIP format:

```
voice service voip
sip
 url sip
```

The following
                              		  example generates URLs in SIPS format:

```
voice service voip
sip
 url sips
```

The following
                              		  example generates URLs in the voice class tenant configuration mode:

```
Router(config-class)# url system
```

The following
                              		  example generates URLs in TEL format:

```
voice service voip
sip
 url tel
```

The following
                              		  example generates URLs in TEL format and appends the phone-context parameter:

```
voice service voip
sip
 url tel phone-context
```

### Related Commands

Command

Description

sip

Enters
                                          						SIP configuration mode from voice-service VoIP configuration mode.

voice - class sip url

Generates URLs in the SIP, SIPS, or TEL format.

## usage-indication

To enter the Annex G neighbor usage mode used to configure optional usage indicators, use the usage indication command in Annex G neighbor configuration mode. To return to the default setting, use the no form of this command.

usage-indication

no usage-indication

### Syntax Description

This command has no arguments or keywords.

### Command Default

Disabled

### Command Modes

Annex G neighbor

## Command History

Release

Modification

12.2(11)T

This command was introduced.

### Usage Guidelines

Use the usage - indication command to enter the mode to set usage indication characteristics. Repeat this command for each border element neighbor that
                              you configure.

The no shutdown command must be used to enable each service relationship.

## Examples

The following example shows how to enter the Annex G neighbor usage mode:

```
doc-rtr3(config-nxg-neigh-usg)# 
usage-indication
```

### Related Commands

Command

Description

access-policy

Requires that a neighbor be explicitly configured.

inbound ttl

Sets the inbound time-to-live value.

outbound retry-interval

Defines the retry period for attempting to establish the outbound relationship between border elements.

retry interval

Defines the time between delivery attempts.

retry window

Defines for how long a border element will attempt delivery.

shutdown

Enables or disables the border element.

## use-proxy

To enable proxy communications for calls between local and remote zones or the H.225 Annex G border element, use the use - proxy command in gatekeeper configuration mode. To remove either a proxy configuration entry for a remote zone or the H.225 Annex
                              G border element, to disable proxy communications between local and remote zones or H.225 Annex G border element, use the no form of this command.

use-proxy local-zone-name { default | h323-annexg | remote-zone remote-zone-name } { inbound-to | outbound-from } { gateway | terminal }

no use-proxy local-zone-name { default | h323-annexg | remote-zone remote-zone-name } [ { inbound-to | outbound-from } { gateway | terminal }]

### Syntax Description

local - zone - name

Name or zone name of the gatekeeper, which is usually the fully domain-qualified host name of the gatekeeper.

default

Default proxy policy for all calls that are not defined by a use - proxy command with the remote - zone keyword or h323-annexg keyword.

h323-annexg

Proxy policy for calls to or from the H.225 Annex G border element co-located with the gatekeeper.

remote - zone remote - zone - name

Proxy policy for calls to or from a specific remote gatekeeper or zone.

inbound - to

Proxy policy as it applies to calls that are inbound to the local zone from a remote zone. Each use - proxy command defines the policy for only one direction.

outbound - from

Proxy policy as it applies to calls that are outbound from the local zone to a remote zone. Each use - proxy command defines the policy for only one direction.

gateway

Type of local device to which the policy applies. The gateway option applies the policy only to local gateways.

terminal

Type of local device to which the policy applies. The terminal option applies the policy only to local terminals.

### Command Default

The local zone uses proxy for both inbound and outbound calls to and from the local H.323 terminals only. Proxy is not used
                              for both inbound and outbound calls to and from local gateways. For releases prior to Cisco IOS Release 12.3(7)T, both inbound
                              and outbound calls using the H.225 Annex G border element do not use the proxy.

### Command Modes

Gatekeeper configuration

## Command History

Release

Modification

12.0(5)T

This command was introduced on the Cisco AS5300.

12.1(5)XM2

The command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T. Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400
                                          is not included in this release.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T.

12.3(7)T

The h323-annexg keyword was added.

### Usage Guidelines

This command replaces the zone access command used in previous versions of the gatekeeper. When a previous version of a gatekeeper is upgraded, any zone access commands are translated to use - proxy commands. You can use the show gatekeeper zone status command to see the gatekeeper proxy configuration.

If the domain name is cisco.com, the gatekeeper name might be gk1.cisco.com. However, if the gatekeeper is controlling multiple
                              zones, the name of the gatekeeper for each zone should be a unique string.

## Examples

In the following example, the local zone sj.xyz.com is configured to use a proxy for inbound calls from remote zones tokyo.xyz.com
                              and milan.xyz.com to gateways in its local zone. The sj.xyz.com zone is also configured to use a proxy for outbound calls
                              from gateways in its local zone to remote zones tokyo.xyz.com and milan.xyz.com.

```
use-proxy sj.xyz.com remote-zone tokyo.xyz.com inbound-to gateway
use-proxy sj.xyz.com remote-zone tokyo.xyz.com outbound-from gateway
use-proxy sj.xyz.com remote-zone milan.xyz.com inbound-to gateway
use-proxy sj.xyz.com remote-zone milan.xyz.com outbound-from gateway
```

Because the default mode disables proxy communications for all gateway calls, only the gateway calls listed above can use
                              the proxy.

In the following example, the local zone sj.xyz.com uses a proxy for only those calls that are outbound from H.323 terminals
                              in its local zone to the specified remote zone germany.xyz.com:

```
no use-proxy sj.xyz.com default outbound-from terminal
use-proxy sj.xyz.com remote-zone germany.xyz.com outbound-from terminal
```

Any calls inbound to H.323 terminals in the local zone sj.xyz.com from the remote zone germany.xyz.com use the proxy because
                                          the default applies.

The following example removes one or more proxy statements for the remote zone germany.xyz.com from the proxy configuration
                              list:

```
no use-proxy sj.xyz.com remote-zone germany.xyz.com
```

This command removes all special proxy configurations for the remote zone germany.xyz.com. After you enter a command like
                              this, all calls between the local zone (sj.xyz.com) and germany.xyz.com are processed according to the defaults defined by
                              any use - proxy commands that use the default option.

To prohibit proxy use for inbound calls to H.323 terminals in a local zone from a specified remote zone, enter a command similar
                              to the following:

```
no use-proxy sj.xyz.com remote-zone germany.xyz.com inbound-to terminal
```

This command overrides the default and disables proxy use for inbound calls from remote zone germany.xyz.com to all H.323
                              terminals in the local zone sj.xyz.com.

In the following example, the local zone sj.xyz.com is configured to use a proxy for inbound calls and outbound calls that
                              use the H.225 Annex G border element co-located with the gatekeeper:

```
use-proxy sj.xyz.com h323-annexg inbound-to gateway 
use-proxy sj.xyz.com h323-annexg outbound-from gateway
```

In the following example, the local zone sj.xyz.com is configured not to use a proxy for inbound calls and outbound calls
                              that use the H.225 Annex G border element co-located with the gatekeeper:

```
no use-proxy sj.xyz.com h323-annexg inbound-to terminal
no use-proxy sj.xyz.com h323-annexg outbound-from terminal
```

The following example removes one or more proxy statements for the H.225 Annex G border element from the proxy configuration
                              list:

```
no use-proxy sj.xyz.com h323-annexg
```

### Related Commands

Command

Description

show gatekeeper zone status

Displays the status of zones related to a gatekeeper.

## user-id

To match a call based on the user-id field in the Session Initiation Protocol (SIP) uniform resource identifier (URI), use
                              the user-id command in voice URI class configuration mode. To remove the match pattern, use the no form of this command.

user-id username-pattern

no user-id

### Syntax Description

username-pattern

Cisco IOS regular expression pattern to match against the user-id field in a SIP URI. Can be up to 32 characters.

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

You can use this command only in a voice class for SIP URIs.

You cannot use this command if you use the pattern command in the voice class. The pattern command matches on the entire URI, whereas this command matches only a specific field.

## Examples

The following example defines a voice class that matches on the user-id field in a SIP URI:

```
voice class uri r100 sip
 user-id abc123
```

### Related Commands

Command

Description

destination uri

Specifies the voice class used to match the dial peer to the destination URI for an outgoing call.

host

Matches a call based on the host field in a SIP URI.

incoming uri

Specifies the voice class used to match a VoIP dial peer to the URI of an incoming call.

pattern

Matches a call based on the entire SIP or TEL URI.

phone context

Filters out URIs that do not contain a phone-context field that matches the configured pattern.

voice class uri

Creates or modifies a voice class for matching dial peers to calls containing a SIP or TEL URI.

voice class uri sip preference

Sets a preference for selecting voice classes for a SIP URI.

| Release | Modification |
|---|---|
| 15.2(2)T | This
                                          						command was introduced. |
| Cisco IOS XE Everest 16.6.1 | This command extended support for configuring Cisco Unified
                                          						Communication IOS services environment using HTTPS connection. |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models. |

| Note | If you intend to move from secure mode to nonsecure mode, remove the
                                          			 existing uc secure-wsapi configuration and reconfigure in nonsecure mode. |
|---|---|

| Command | Description |
|---|---|
| provider | Enables a
                                          						provider service. |

| Release | Modification |
|---|---|
| Cisco
                                       					 IOS XE Everest 16.6.1 | This
                                       					 command was introduced. |
| Cisco IOS XE Cupertino 17.7.1 | Introduced support for YANG models. |

| Note | If you intend
                                          			 to move from nonsecure mode to secure mode, remove the existing uc wsapi configuration and reconfigure in secure mode. |
|---|---|

| Command | Description |
|---|---|
| provider | Enables a provider service. |

| high - complexity | (Optional) High-complexity firmware set. |
|---|---|
| medium - complexity | (Optional) Medium-complexity firmware set. |
| slot - number | Voice feature card (VFC) slot number. |

| Release | Modification |
|---|---|
| 11.3(2)NA | This command was introduced on the Cisco AS5300. |
| 12.0(2)XH | The high - complexity and medium - complexity keywords were added. |
| 12.0(3)T | This command was integrated into Cisco IOS Release 12.0(3)T. |

| Command | Description |
|---|---|
| clear vfc | Resets the VFC. |
| copy flash vfc | Copies a new version of VCWare from the Cisco AS5300 motherboard to VFC Flash memory. |
| copy tftp vfc | Copies a new version of VCWare from a TFTP server to VFC Flash memory. |

| Release | Modification |
|---|---|
| 15.4(1)T Cisco IOS XE 3.11S | This command was introduced. |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
|  |  |

| url-address | URL address. A valid URL address is as follows:
                                          http:// fully qualified domain nam e[: port ]/[ URL ] |
|---|---|

| Release | Modification |
|---|---|
| 12.0(4)XH1 | This command was introduced on Cisco 2600 series and Cisco 3600 series, and Cisco AS5300. |
| 12.1(1)T | This command was integrated into Cisco IOS Release 12.1(1)T. |
| 12.2(11)T | The settlement configuration for this command was modified. The settlement provider must be shut down before the url command is entered. |

| Command | Description |
|---|---|
| connection-timeout | Sets the connection timeout. |
| customer-id | Sets the customer identification. |
| device-id | Sets the device identification. |
| encryption | Specifies the encryption method. |
| max-connection | Sets the maximum simultaneous connections. |
| response-timeout | Sets the response timeout. |
| retry-delay | Sets the retry delay. |
| retry-limit | Sets the connection retry limit. |
| session-timeout | Sets the session timeout. |
| settlement | Enters settlement configuration mode. |
| show settlement | Displays the configuration for all settlement server transactions. |
| shutdown | Brings up the settlement provider. |
| no shutdown | Shuts down the settlement provider. |
| type | Specifies the provider type. |

| url | The URL of an internally or an externally stored text file that has been used on an E.164 pattern map. |
|---|---|

| Release | Modification |
|---|---|
| 15.2(4)M | This command was introduced. |

| Command | Description |
|---|---|
| destination e164-pattern-map | Links an E.164 pattern map to a dial peer. |
| e164 | Configures an E.164 pattern entry on a destination E.164 pattern map. |
| show voice class e164-pattern-map | Displays details of the configuration of a voice class E.164 pattern map. |
| voice class e164-pattern-map load | Loads a destination E.164 pattern map specified by a text file. |

| sip | Generates
                                          						URLs in SIP format for VoIP calls. |
|---|---|
| sips | Generates
                                          						URLs in SIPS format for VoIP calls. |
| system | Specifies that the URLs use the global sip-ua value. This
                                          						keyword is available only for the tenant mode to allow it to fallback to the
                                          						global configurations. |
| tel | Generates
                                          						URLs in TEL format for VoIP calls. |
| phone-context | (Optional) Appends the phone-context parameter to the TEL URL. |

| Release | Modification |
|---|---|
| 12.2(2)XB | This
                                          						command was introduced. |
| 12.2(2)XB1 | This
                                          						command was implemented on the Cisco AS5850. |
| 12.2(8)T | This
                                          						command was integrated into Cisco IOS Release 12.2(8)T. Support for the Cisco
                                          						AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 was not included in this
                                          						release. |
| 12.2(11)T | This
                                          						command was implemented on the Cisco AS5300, Cisco AS5350, and Cisco AS5400
                                          						platforms. |
| 12.4(6)T | The sips keyword
                                          						was added. |
| 12.4(22)YB | The phone-context keyword was added. |
| 12.4(24)T | This
                                          						command was integrated into Cisco IOS Release 12.4(24)T. |
| 15.6(2)T
                                          						and IOS XE Denali 16.3.1 | This
                                          						command was modified to include the keyword: system . This
                                          						command is now available under voice class tenants. |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| sip | Enters
                                          						SIP configuration mode from voice-service VoIP configuration mode. |
| voice - class sip url | Generates URLs in the SIP, SIPS, or TEL format. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |

| Note | The no shutdown command must be used to enable each service relationship. |
|---|---|

| Command | Description |
|---|---|
| access-policy | Requires that a neighbor be explicitly configured. |
| inbound ttl | Sets the inbound time-to-live value. |
| outbound retry-interval | Defines the retry period for attempting to establish the outbound relationship between border elements. |
| retry interval | Defines the time between delivery attempts. |
| retry window | Defines for how long a border element will attempt delivery. |
| shutdown | Enables or disables the border element. |

| local - zone - name | Name or zone name of the gatekeeper, which is usually the fully domain-qualified host name of the gatekeeper. |
|---|---|
| default | Default proxy policy for all calls that are not defined by a use - proxy command with the remote - zone keyword or h323-annexg keyword. |
| h323-annexg | Proxy policy for calls to or from the H.225 Annex G border element co-located with the gatekeeper. |
| remote - zone remote - zone - name | Proxy policy for calls to or from a specific remote gatekeeper or zone. |
| inbound - to | Proxy policy as it applies to calls that are inbound to the local zone from a remote zone. Each use - proxy command defines the policy for only one direction. |
| outbound - from | Proxy policy as it applies to calls that are outbound from the local zone to a remote zone. Each use - proxy command defines the policy for only one direction. |
| gateway | Type of local device to which the policy applies. The gateway option applies the policy only to local gateways. |
| terminal | Type of local device to which the policy applies. The terminal option applies the policy only to local terminals. |

| Release | Modification |
|---|---|
| 12.0(5)T | This command was introduced on the Cisco AS5300. |
| 12.1(5)XM2 | The command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400
                                          is not included in this release. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. |
| 12.3(7)T | The h323-annexg keyword was added. |

| Note | Any calls inbound to H.323 terminals in the local zone sj.xyz.com from the remote zone germany.xyz.com use the proxy because
                                          the default applies. |
|---|---|

| Command | Description |
|---|---|
| show gatekeeper zone status | Displays the status of zones related to a gatekeeper. |

| username-pattern | Cisco IOS regular expression pattern to match against the user-id field in a SIP URI. Can be up to 32 characters. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Command | Description |
|---|---|
| destination uri | Specifies the voice class used to match the dial peer to the destination URI for an outgoing call. |
| host | Matches a call based on the host field in a SIP URI. |
| incoming uri | Specifies the voice class used to match a VoIP dial peer to the URI of an incoming call. |
| pattern | Matches a call based on the entire SIP or TEL URI. |
| phone context | Filters out URIs that do not contain a phone-context field that matches the configured pattern. |
| voice class uri | Creates or modifies a voice class for matching dial peers to calls containing a SIP or TEL URI. |
| voice class uri sip preference | Sets a preference for selecting voice classes for a SIP URI. |