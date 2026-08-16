---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-vcr5-vcr5-cr-book-vcr-v2-html-82e796e0a6
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/vcr5/vcr5-cr-book/vcr-v2.html
retrieved_at: 2026-08-16T23:14:29.884416+00:00
---

Cisco IOS Voice Command Reference - T through Z

# Cisco IOS Voice Command Reference - T through Z

Updated: April 25, 2026

Chapter: voice-class sip error-code-override through vxml version 2.0

## Chapter: voice-class sip error-code-override through vxml version 2.0

# voice-class sip error-code-override through vxml version 2.0

## voice-class sip error-code-override

To configure the Session Initiation Protocol (SIP) error code that a dial peer uses for options-keepalive failures, call
                              spike, or cac-bandwidth failures, use the voice-class sip error-code-override command in dial peer voice configuration mode. To disable the SIP error code configuration, use the no form of this command.

voice-class sip error-code-override { options-keepalive failure | call spike failure | cac-bandwidth failure } { sip-status-code-number | system }

no voice-class sip error-code-override { options-keepalive failure | call spike failure | cac-bandwidth failure }

### Syntax Description

options-keepalive failure

Configures the SIP error code for options-keepalive failures.

call spike failure

Configures the SIP error code for call spike failures.

cac-bandwidth failure

Configures the SIP error code for Call Admission Control bandwidth failures.

sip-status-code-number

The SIP status code that is sent for the options keepalive, call spike, or cac-bandwidth failure. The range is from 400 to
                                          699. The default value is 503. The table below in the “Usage Guidelines” section describes these error codes.

system

Specifies the system configuration used for keepalive, call spike, or cac-bandwidth failures.

### Command Default

By default the SIP error code is not configured.

### Command Modes

Dial peer voice configuration (config-dial-peer)

## Command History

Release

Modification

15.0(1)XA

This command was introduced.

15.1(1)T

This command was integrated into Cisco IOS Release 15.1(1)T.

15.1(3)T

This command was modified. The call spike failure keyword was added.

15.2(2)T

This command was modified. The cac-bandwidth failure keyword was added.

### Usage Guidelines

The voice-class sip error-code-override command in dial peer voice configuration mode configures the error code response for keepalive options, call spike, or cac-bandwidth
                              failures at the dial peer level. The error-code-override command in voice service SIP configuration mode configures the error code responses for options-keepalive, call spike, or
                              cac-bandwidth failures globally.

The table below describes the SIP error codes.

Error Code Number

Description

400

Bad request

401

Unauthorized

402

Payment required

403

Forbidden

404

Not found

408

Request timed out

416

Unsupported Uniform Resource Identifier (URI)

480

Temporarily unavailable

482

Loop detected

484

Address incomplete

486

Busy here

487

Request terminated

488

Not acceptable here

500–599

SIP 5xx—server/service failure

500

Internal server error

502

Bad gateway

503

Service unavailable

600–699

SIP 6xx—global failure

## Examples

The following example shows how to configure the SIP error code for options-keepalive failures using the voice-class sip error-code-override command:

```
Router(config)# dial-peer voice 432 voip system Router(config-dial-peer)# voice-class sip error-code-override options-keepalive failure 502
```

The following example shows how to configure the SIP error code for call spike failures using the voice-class sip error-code-override command:

```
Router(config)# dial-peer voice 432 voip system Router(config-dial-peer)# voice-class sip error-code-override call spike failure 502
```

The following example shows how to configure the SIP error code for Call Admission Control bandwidth failures:

```
Router(config)# dial-peer voice 432 voip system Router(config-dial-peer)# voice-class sip error-code-override cac-bandwidth failure 502
```

### Related Commands

Command

Description

error-code-override

Configures the SIP error code for options-keepalive, call spike, or cac-bandwidth failures in voice service SIP and dial
                                          peer voice configuration mode, respectively.

## voice-class sip g729 annexb-all

To configure settings on a Cisco IOS Session Initiation Protocol (SIP) gateway that determine if a specific dial peer on the
                              gateway treats the G.729br8 codec as superset of G.729r8 and G.729br8 codecs for interoperation with Cisco Unified Communications
                              Manager, use the voice-class sip g729 annexb-all command in dial peer voice configuration mode. To prevent a dial peer from treating the G.729br8 codec as a superset of the
                              G.729r8 and G.729br8 codecs, use the no form of this command.

voice-class sip g729 annexb-all [ system ]

no voice-class sip g729 annexb-all

### Syntax Description

annexb-all

Specifies that the G.729br8 codec is treated as a superset of G.729r8 and G.729br8 codecs to communicate with Cisco Unified
                                          Communications Manager.

system

(Optional) Specifies that the dial peer allow communication between incompatible G.729 codecs according to global settings
                                          configured for this feature on the Cisco IOS SIP gateway.

### Command Default

The dial peer defers to global (system) settings for the Cisco IOS gateway.

### Command Modes

Dial peer voice configuration (config-dial-peer)

## Command History

Release

Modification

12.4(15)XZ

This command was introduced.

12.4(20)T

This command was integrated into Cisco IOS Release 12.4(20)T.

### Usage Guidelines

There are four variations of the G.729 coder-decoder (codec), which fall into two categories:

High Complexity

G.729 (g729r8)--a high complexity algorithm codec on which all other G.729 codec variations are based.

G.729 Annex-B (g729br8 or G.729B)--a variation of the G.729 codec that allows the DSP to detect and measure voice activity
                                    and convey suppressed noise levels for re-creation at the other end. Additionally, the Annex-B codec includes Internet Engineering
                                    Task Force (IETF) voice activity detection (VAD) and comfort noise generation (CNG) functionality.

Medium Complexity

G.729 Annex-A (g729ar8 or G.729A)--a variation of the G.729 codec that sacrifices some voice quality to lessen the load on
                                    the DSP. All platforms that support G.729 also support G.729A.

G.729A Annex-B (g729abr8 or G.729AB)--a variation of the G.729 Annex-B codec that, like G.729B, sacrifices voice quality to
                                    lessen the load on the DSP. Additionally, the G.729AB codec also includes IETF VAD and CNG functionality.

The VAD and CNG functionality is what causes the instability during communication attempts between two DSPs where one DSP
                              is configured with Annex-B (G.729B or G.729AB) and the other without (G.729 or G.729A). All other combinations interoperate.
                              To configure a dial peer on a Cisco IOS SIP gateway for interoperation with Cisco Unified Communications Manager (formerly
                              known as the Cisco CallManager, or CCM), use the voice-class sip g729 annexb-all command in dial peer voice configuration mode to do one of the following:

Override global settings for a Cisco IOS gateway and configure the dial peer to accept and connect calls between two DSPs
                                    with incompatible G.729 codecs.

Specify that an individual dial peer use the global ( system ) settings on the Cisco IOS SIP gateway.

Use the no form of the command to override global settings for the Cisco IOS gateway and specify that the dial peer does not
                                    treat the G.729br8 codec as a superset of G.729r8 and G.729br8 codecs.

Use the g729 annexb-all command in voice service SIP configuration mode to configure the global settings for the Cisco IOS SIP gateway.

## Examples

The following example shows how to configure a dial peer on a Cisco IOS SIP gateway to connect calls between two DSPs using
                              incompatible G.729 codecs, overriding global gateway settings for this feature:

```
Router> enable Router# configure terminal Router(config)# dial-peer voice 1 Router(config-dial-peer)# voice-class sip g729 annexb-all
```

### Related Commands

Command

Description

g729 annexb-all

Configure global settings that determine if a Cisco IOS SIP gateway treats the G.729br8 codec as superset of G.729r8 and G.729br8
                                          codecs.

## voice-class sip history-info

To enable Session Initiation Protocol (SIP) history-info header support on the Cisco IOS gateway at the dial-peer level, use
                              the voice-class sip history-info command in dial peer configuration mode. To disable SIP history-info header support, use the no form of this command.

voice-class sip history-info [ system ]

no voice-class sip history-info

### Syntax Description

system

(Optional) Enables history-info support using global configuration settings.

### Command Default

History-info header support is disabled.

### Command Modes

Dial peer configuration (conf-dial-peer)

## Command History

Release

Modification

12.4(22)T

This command was introduced.

Cisco IOS XE 
                                          Release 3.1S

This command was integrated into Cisco IOS XE Release 3.1S

### Usage Guidelines

Use this command to enable history-info header support at the dial-peer level. The history-info header (as defined in RFC
                              4244) records the call or dialog history. The receiving application uses the history-info header information to determine
                              how and why the call has reached it.

The Cisco IOS SIP gateway cannot use the information in the history-info header to make routing decisions.

## Examples

The following example enables SIP history-info header support at the dial-peer level:

```
Router(config)# dial-peer voice 2 voip Router(config-dial-peer)# voice-class sip history-info
```

The following example enables SIP history-info header support at the dial-peer level using the global configuration settings:

```
Router(config)# dial-peer voice 2 voip Router(config-dial-peer)# voice-class sip history-info system
```

### Related Commands

Command

Description

history-info

Enables SIP history-info header support on Cisco IOS gateway at a global level.

## voice-class sip localhost

To configure individual dial peers to override global settings on
                              		  Cisco IOS voice gateways, Cisco Unified Border Element (Cisco UBE), or Cisco
                              		  Unified Communications Manager Express (Cisco Unified CME) and substitute a
                              		  Domain Name System (DNS) hostname or domain as the localhost name in place of
                              		  the physical IP address in the From, Call-ID, and Remote-Party-ID headers in
                              		  outgoing messages, use the voice-class sip localhost command in dial peer voice configuration
                              		  mode. To disable substitution of a localhost name on a specific dial peer, use
                              		  the no form of this command. To configure a
                              		  specific dial peer to defer to global settings for localhost name substitution,
                              		  use the default form of this command.

voice-class sip localhost dns: [ hostname ] domain [ preferred ]

no voice-class sip localhost

default voice-class sip localhost

### Syntax Description

dns: [ hostname. ] domain

Alphanumeric value representing the DNS domain (consisting
                                          						of the domain name with or without a specific hostname) in place of the
                                          						physical IP address that is used in the host portion of the From, Call-ID, and
                                          						Remote-Party-ID headers in outgoing messages.

This value can be the hostname and the domain separated by
                                          						a period
                                          						( dns: hostname.domain ) or
                                          						just the domain name
                                          						( dns: domain ). In both case,
                                          						the dns: delimiter must be included as
                                          						the first four characters.

preferred

(Optional) Designates the specified DNS hostname as
                                          						preferred.

### Command Default

The dial peer uses the global configuration setting to determine
                              		  whether a DNS localhost name is substituted in place of the physical IP address
                              		  in the From, Call-ID, and Remote-Party-ID headers of outgoing messages.

### Command Modes

Dial peer voice configuration (config-dial-peer)

## Command History

Release

Modification

12.4(2)T

This command was introduced.

15.0(1)XA

This command was modified. The preferred keyword was added to
                                          						specify the preferred localhost if multiple registrars are configured on a SIP
                                          						trunk.

IOS Release XE 2.5

This command was integrated into Cisco IOS XE Release 2.5.

15.1(1)T

This command was integrated into Cisco IOS Release
                                          						15.1(1)T.

### Usage Guidelines

Use the voice-class sip localhost command in dial peer voice configuration
                              		  mode to override the global configuration on Cisco IOS voice gateways, Cisco
                              		  UBEs, or Cisco Unified CME and configure a DNS localhost name to be used in
                              		  place of the physical IP address in the From, Call-ID, and Remote-Party-ID
                              		  headers of outgoing messages on a specific dial peer. When multiple registrars
                              		  are configured for an individual dial peer you can then use the voice-class sip localhost preferred command to specify which host is
                              		  preferred for that dial peer.

To globally configure a localhost name on a Cisco IOS voice gateway,
                              		  Cisco UBE, or Cisco Unified CME, use the localhost command in voice service SIP
                              		  configuration mode. Use the no voice-class sip localhost command to remove localhost name
                              		  configurations for the dial peer and to force the dial peer to use the physical
                              		  IP address in the host portion of the From, Call-ID, and Remote-Party-ID
                              		  headers regardless of the global configuration.

## Examples

The following example shows how to configure dial peer 1 (overriding
                              		  any global configuration) to substitute a domain (no hostname specified) as the
                              		  preferred localhost name in place of the physical IP address in the From,
                              		  Call-ID, and Remote-Party-ID headers of outgoing messages:

```
Router> enable Router# configure terminal Router(config)# dial-peer voice 1 voip Router(config-dial-peer)# voice-class sip localhost dns:example.com preferred
```

The following example shows how to configure dial peer 1 (overriding
                              		  any global configuration) to substitute a specific hostname on a domain as the
                              		  preferred localhost name in place of the physical IP address in the From,
                              		  Call-ID, and Remote-Party-ID headers of outgoing messages:

```
Router> enable Router# configure terminal Router(config)# dial-peer voice 1 voip Router(config-dial-peer)# voice-class sip localhost dns:MyHost.example.com preferred
```

The following example shows how to force dial peer 1 (overriding any
                              		  global configuration) to use the physical IP address in the From, Call-ID, and
                              		  Remote-Party-ID headers of outgoing messages:

```
Router> enable Router# configure terminal Router(config)# dial-peer voice 1 voip Router(config-dial-peer)# no voice-class sip localhost
```

### Related Commands

Command

Description

authentication (dial peer)

Enables SIP digest authentication on an individual dial
                                          						peer.

authentication (SIP UA)

Enables SIP digest authentication.

credentials (SIP UA)

Configures a Cisco UBE to send a SIP registration message
                                          						when in the UP state.

localhost

Configures global settings for substituting a DNS localhost
                                          						name in place of the physical IP address in the From, Call-ID, and
                                          						Remote-Party-ID headers of outgoing messages.

registrar

Enables Cisco IOS SIP gateways to register E.164 numbers on
                                          						behalf of FXS, EFXS, and SCCP phones with an external SIP proxy or SIP
                                          						registrar.

## voice-class sip map resp-code

To configure an individual dial peer on a Cisco Unified Border Element (Cisco UBE) to map specific received Session Initiation
                              Protocol (SIP) provisional response messages to a different SIP provisional response message on the outgoing SIP dial peer,
                              use the voice-class sip map resp-code command in dial peer voice configuration mode. To disable mapping of received SIP provisional response messages on an individual
                              dial peer, use the no form of this command. To configure a specific dial peer to defer to global settings for mapping of incoming SIP provisional
                              response messages, use the default form of this command.

voice-class sip map resp-code 181 to 183

no voice-class sip map resp-code 181 to 183

default voice-class sip map resp-code 181 to 183

### Syntax Description

181

The code representing the specific incoming SIP provisional response messages to be mapped and replaced.

to

The designator for specifying that the specified incoming SIP provisional response message should be mapped to and replaced
                                          with a different SIP provisional response message on the outgoing SIP dial peer.

183

The code representing the specific SIP provisional response message on the outgoing dial peer to which incoming SIP message
                                          responses should be mapped.

### Command Default

Mapping behavior is determined by the global configuration setting, which, if not specifically configured, means that incoming
                              SIP provisional responses are passed, as is to the outbound SIP dial peer.

### Command Modes

Dial peer voice configuration (config-dial-peer)

## Command History

Release

Modification

15.0(1)XA

This command was introduced.

15.1(1)T

This command was integrated into Cisco IOS Release 15.1(1)T.

Cisco IOS XE Release 3.1S

This command was integrated into Cisco IOS XE Release 3.1S.

### Usage Guidelines

Use the voice-class sip map resp-code command in dial peer voice configuration mode to configure an individual dial peer on a Cisco UBE to map incoming SIP 181
                              provisional response messages to SIP 183 provisional response messages on the outgoing SIP dial peer.

If the block command is configured for incoming SIP 181 messages, either globally or at the dial-peer level, the messages may be dropped
                                          before they can be passed or mapped to a different message--even when the voice-class sip map resp-code command is enabled. To globally configure whether and when incoming SIP 181 messages are dropped, use the block command in voice service SIP configuration mode (or use the voice-class sip block command in dial peer voice configuration mode to configure drop settings on individual dial peers).

To configure mapping of SIP provisional response messages globally on a Cisco UBE, use the map resp-code command in voice service SIP configuration mode. To disable mapping of SIP 181 message for an individual dial peer on a Cisco
                              UBE, use the no voice-class sip map resp-code command in voice service SIP configuration mode.

As an example, to enable interworking of SIP endpoints that do not support the handling of SIP 181 provisional response messages,
                              you could use the block command to configure a Cisco UBE to drop SIP 181 provisional response messages received on the SIP trunk or you can use the map resp-code command to configure the Cisco UBE to map the incoming messages to and send out, instead, SIP 183 provisional response messages
                              to the SIP line in Cisco Unified Communications Manager Express (Cisco Unified CME).

This command is supported only for SIP-to-SIP calls and will have no effect on H.323-to-SIP or time-division multiplexing
                                          (TDM)-to-SIP calls.

## Examples

The following example shows how to configure dial peer 1 to map incoming SIP 181 provisional response messages to SIP 183
                              provisional response messages on the outbound dial peer:

```
Router> enable Router# configure terminal Router(config)# dial-peer voice 1 voip Router(config-dial-peer)# voice-class sip map resp-code 181 to 183
```

### Related Commands

Command

Description

block

Configures global settings for dropping specific SIP provisional response messages on a Cisco IOS voice gateway or Cisco UBE.

map resp-code

Configures global settings on a Cisco UBE for mapping specific incoming SIP provisional response messages to a different SIP
                                          response message.

voice-class sip block

Configures an individual dial peer on a Cisco IOS voice gateway or Cisco UBE to drop specified SIP provisional response messages.

## voice-class sip
                        	 midcall-signaling

To configure the
                              		  method used for signaling messages, use the voice-class sip
                                    				midcall-signaling command in SIP configuration mode or dial peer
                              		  configuration mode. To disable the mid-call signaling feature, use the no form of
                              		  this command.

voice-class sip midcall-signaling { passthru media-change | block | preserve-codec }

no voice-class sip midcall-signaling

### Syntax Description

passthru media-change

Passes
                                          						SIP messages that inolve media-change from one IP leg to another IP leg.

block

Blocks
                                          						all SIP messages during mid-call.

preserve-codec

Preserves codec negotiated during call initialization.
                                          						Mid-call codec change is disabled.

### Command Default

Mid
                              		  call-signaling is disabled. Codec negotiation in the middle of a call is
                              		  enabled.

### Command Modes

Dial peer configuration mode (config-dial-peer)

## Command History

Release

Modification

12.4(15)XZ

This
                                          						command was introduced.

12.4(20)T

This
                                          						command was integrated into Cisco IOS Release 12.4(20)T.

Cisco
                                          						IOS XE Release 2.5

This
                                          						command was integrated into Cisco IOS XE Release 2.5.

15.2(1)T

This
                                          						command was integrated into Cisco IOS Release 15.2(1)T. The media-change and block keywords were added.

15.3(2)S, 15.3(1)T

This
                                          						command was modified. The preserve-codec keyword was added.

### Usage Guidelines

The voice-class sip
                                    				midcall-signaling command distinguishes between the way Cisco
                              		  Unified Communications Express and Cisco Unified Border Element handle
                              		  signaling messages. Most SIP-to-SIP video and SIP-to-SIP reinvite based
                              		  supplementary services require the voice-class sip
                                    				midcall-signaling command to be configured before configuring
                              		  other supplementary services. Supplementary service features that are
                              		  functional without configuring voice-class sip
                                    				midcall-signaling include: session refresh, fax, and refer-based
                              		  supplementary services. The voice-class sip
                                    				midcall-signaling command is for SIP-to-SIP calls only. All other
                              		  calls (H323-to-SIP, and H323-to-H323) do not require the voice-class sip
                                    				midcall-signaling command be configured. The allow-connections sip-to-sip command must be configured before the voice-class sip
                                    				midcall-signaling command.

Configuring the
                              		  Session Refresh with Reinvites feature on a dial-peer basis is not supported.

## Examples

The following
                              		  example shows SIP messages configured to passthrough from one IP leg to another
                              		  IP leg:

```
Router(config)# voice service voip Router(conf-voi-serv)# sip Router(conf-serv-sip)# voice-class sip midcall-signaling passthru
```

The following
                              		  example shows SIP messages configured to media passthru from one IP leg to
                              		  another IP leg:

```
Router(config)# voice service voip Router(conf-voi-serv)# sip Router(conf-serv-sip)# voice-class sip midcall-signaling passthru media-change
```

The following
                              		  example shows how to block SIP messages.

```
Router(config)# voice service voip Router(conf-voi-serv)# sip Router(conf-serv-sip)# voice-class sip midcall-signaling block
```

The following
                              		  example shows how to disable codec negotiation in the middle of a call and
                              		  retains the codec negotiated at the start of the call.

```
Router(config)# voice service voip Router(conf-voi-serv)# sip Router(conf-serv-sip)# voice-class sip midcall-signaling preserve-codec
```

### Related Commands

Command

Description

allow-connections

Allows connections between specific types of endpoints in a Cisco Unified BE.

## voice-class sip nat media-keepalive

To enable media keepalive packets when the device is configured behind NAT, use the voice-class sip nat command in dial-peer configuration mode. To disable media, use the no or default form of this command.

voice-class sip nat media-keepalive interval

no voice-class sip nat

default voice-class sip nat

## Syntax Description

Specifies media keepalive to subscriber if it's located behind NAT.

Specifies keepalive interval in seconds. Range is 1—50. Default is 10.

### Command Default

By default, media-keepalive is disabled.

### Command Modes

Dial-peer configuration mode (config-dial-peer)

## Command History

Cisco IOS XE 17.13.1a

Cisco IOS XE Dublin 17.12.2

This command was introduced.

### Usage Guidelines

If the dial-peer is associated with a tenant, the configurations are applied in the following order of preference:

Dial-peer configuration

Tenant configuration

Global configuration

A newly created dial peer remains defined and active until you delete it with the no form of the dial-peer voice command.

## Examples

The following example shows how to configure media keepalive to enable media keepalive packets to be transmitted for the interval
                              specified in seconds:

```
Device(config)# dial-peer voice 999 voip Device(config-dial-peer)# voice-class sip nat media-keepalive 40
```

The voice-class sip nat media-keepalive command takes affect immediately after it is applied.

### Related Commands

Command

Description

nat media-keepalive

Uses the SIP Network Address Translation (NAT) global configuration.

voice class tenant tag

Associates a dial-peer with a specific tenant configuration.

## voice-class sip options-keepalive

To monitor connectivity between Cisco Unified Border Element VoIP
                              		  dial-peers and SIP servers to, use the voice-class sip options-keepalive command in dial peer
                              		  configuration mode. To disable monitoring connectivity, use the no form of this command.

voice-class sip options-keepalive keepalive-group-profile-id { up-interval seconds | down-interval seconds | retry retries }

no voice-class sip options-keepalive

### Syntax Description

keepalive-group-profile-id

Specifies the keepalive group profie id.

up-interval seconds

Number of up-interval seconds allowed to pass before marking the UA as unavailable.The range is 5-1200. The default is 60.

down-interval seconds

Number of down-interval seconds allowed to pass before marking the UA as unavailable.The range is 5-1200. The default is 30.

retry retries

Number of retry attempts before marking the UA as unavailable. The range is 1 to 10. The default is 5 attempts.

### Command Default

The dial-peer is active (UP).

### Command Modes

Dial peer configuration mode (config-dial-peer).

## Command History

Release

Modification

12.4(22)YB

This command was introduced.

15.0(1)M

This command was integrated into Cisco IOS Release
                                          						15.0(1)M.

Introduced support for YANG models.

### Usage Guidelines

Use the voice-class sip options-keepalive command to configure a out-of-dialog (OOD) Options Ping mechanism between any number of destinations. When monitored endpoint
                              heartbeat responses fails, the configured dial-peer is busied out. If there is a alternate dial-peer configured for the same
                              destination pattern, the call is failed over to the next preference dial peer or the on call is rejected with an error cause
                              code.

The response to options ping will be considered unsuccessful and
                              		  dial-peer will be busied out for following scenarios:

Error Code

Description

503

service unavailable

505

sip version not supported

no response

i.e. request timeout

All other error codes, including 400 are considered a valid response
                              		  and the dial peer is not busied out.

## Examples

The following example shows a sample configuration of dial peer 100
                              		  configured to reset:

```
dial-peer voice 100 voip
  voice-class sip options-keepalive up-interval 12 down-interval 65 retry 3
```

### Related Commands

Command

Description

dial-peer voice

Defines a particular dial peer and specifies the method of voice encapsulation.

## voice-class sip options-keepalive profile

To associate the dial peer with the specified keepalive group profile, use the voice-class sip options-keepalive profile command in dial peer configuration mode.

voice-class sip options-keepalive profile keepalive-group-profile-id

## Syntax Description

Specifies the keepalive group profile id.

### Command Default

The dial-peer is active (UP).

### Command Modes

Dial peer configuration mode (config-dial-peer)

## Command History

Release

Modification

This command was introduced.

### Usage Guidelines

The dial peer is monitored by CUBE according to the parameters defined by options-keepalive profile.

## Examples

The following example shows a sample configuration of an outbound SIP dial peer and association with a keepalive profile group:

```
dial-peer voice 123 voip
 session protocol sipv2
!
voice-class sip options-keepalive profile 171
end
```

## voice-class sip outbound-proxy

To configure an outbound proxy, use the voice-class sip outbound-proxy command in dial peer configuration
                              		  mode. To reset the outbound proxy value to its default, use the no form of this command.

voice-class sip outbound-proxy { dhcp | ipv4: ipv4-address | ipv6: [ipv6-address] | dns: host: domain } [:port-number]

no voice-class sip outbound-proxy

### Syntax Description

dhcp

Specifies that the outbound-proxy IP address is retrieved
                                          						from a DHCP server.

ipv4: ipv4-address

Configures proxy on the server, sending all initiating
                                          						requests to the specified IPv4 address destination. The colon is required.

ipv6:[ ipv6-
                                                							 address ]

Configures proxy on the server, sending all initiating
                                          						requests to the specified IPv6 address destination. Brackets must be entered
                                          						around the IPv6 address. The colon is required.

dns: host:domain

Configures proxy on the server, sending all initiating
                                          						requests to the specified domain destination. The colons are required.

: port-number

(Optional) Port number for the Session Initiation Protocol
                                          						(SIP) server. The colon is required.

### Command Default

An outbound proxy is not configured.

### Command Modes

Dial peer configuration (config-dial-peer)

## Command History

Release

Modification

12.4(15)T

This command was introduced.

12.4(22)T

This command was modified. Support for IPv6 was added.

12.4(22)YB

This command was modified. The dhcp keyword was added.

15.0(1)M

This command was integrated in Cisco IOS Release 15.0(1)M.

### Usage Guidelines

The voice-class sip outbound-proxy command, in dial peer configuration
                              		  mode, takes precedence over the command in SIP global configuration mode.

Brackets must be entered around the IPv6 address.

## Examples

The following example shows how to configure the voice-class sip outbound-proxy command on a dial peer to generate an IPv4 address (10.1.1.1)
                              		  as an outbound proxy:

```
Router> enable Router# configure terminal Router(config)# dial - peer voice 111 voip Router(config-dial-peer)# voice-class sip outbound-proxy ipv4:10.1.1.1
```

The following example shows how to configure the voice-class sip outbound-proxy command on a dial peer to generate a domain
                              		  (sipproxy:cisco.com) as an outbound proxy:

```
Router> enable Router# configure terminal Router(config)# dial - peer voice 111 voip Router(config-dial-peer)# voice-class sip outbound-proxy dns:sipproxy:cisco.com
```

The following example shows how to configure the voice-class sip outbound-proxy command on a dial peer to generate an outbound proxy using
                              		  DHCP:

```
Router> enable Router# configure terminal Router(config)# dial - peer voice 111 voip Router(config-dial-peer)# voice-class sip outbound-proxy dhcp
```

### Related Commands

Command

Description

dial - peer voice

Defines a particular dial peer, specifies the method of
                                          						voice encapsulation, and enters dial peer configuration mode.

voice service

Enters voice-service configuration mode and specifies a
                                          						voice encapsulation type.

## voice-class sip preloaded-route

To enable preloaded route support for dial-peer Session Initiation Protocol (SIP) calls, use the voice-class sip preloaded-route command in dial peer voice configuration mode. To reset to the default value, use the no form of this command.

voice-class sip preloaded-route { [ sip-server ] service-route | system }

no voice-class sip preloaded-route

### Syntax Description

sip-server

(Optional) Adds SIP server information to the Route header.

service-route

Adds the Service-Route information to the Route header.

system

Uses the global system value. This is the default.

### Command Default

SIP calls at the dial-peer level use the global configuration level settings.

### Command Modes

Dial peer voice configuration (config-dial-peer)

## Command History

Release

Modification

12.4(22)YB

This command was introduced.

15.0(1)M

This command was integrated into Cisco IOS Release 15.0(1)M.

### Usage Guidelines

The voice-class sip preloaded-route command takes precedence over the preloaded-route command configured in SIP configuration mode. However, if the voice-class sip preloaded-route command is used with the system keyword, the gateway uses the global settings configured by the preloaded-route command.

## Examples

The following example shows how to configure the dial peer to include SIP server and Service-Route information in the Route
                              header:

```
dial-peer voice 102 voip
 voice-class sip preloaded-route sip-server service-route
```

The following example shows how to configure the dial peer to include only Service-Route information in the Route header:

```
dial-peer voice 102 voip
 voice-class sip preloaded-route service-route
```

### Related Commands

Command

Description

preloaded-route

Enables preloaded route support for VoIP SIP calls.

## voice-class sip privacy

To set privacy support at the dial-peer level as defined in RFC 3323, use the voice-class sip privacy command in dial peer configuration mode. To remove privacy support as defined in RFC 3323, use the no form of this command.

voice-class sip privacy { disable | pstn | system | privacy-option [ critical ]}

no voice-class sip privacy

### Syntax Description

disable

Disables the privacy service for this dial peer regardless of prior implementations. When selected, this becomes the only
                                          valid option.

pstn

Requests that the privacy service implements a privacy header using the default Public Switched Telephone Network (PSTN) rules
                                          for privacy (based on information in Octet 3a). When selected, this becomes the only valid option.

system

Uses the global configuration settings to enable the privacy service on this dial peer. When selected, this becomes the only
                                          valid option.

privacy-option

The privacy support options to be set at the dial-peer level. The following keywords can be specified for the privacy-option argument:

header -- Requests that privacy be enforced for all headers in the Session Initiation Protocol (SIP) message that might identify
                                                information about the subscriber.

history -- Requests that the information held in the history-info header is hidden outside the trust domain.

id -- Requests that the Network Asserted Identity that authenticated the user be kept private with respect to SIP entities outside
                                                the trusted domain.

session -- Requests that the information held in the session description is hidden outside the trust domain.

user -- Requests that privacy services provide a user-level privacy function.

The keywords can be used alone, altogether, or in any combination with each other, but each keyword can be used only once.

critical

(Optional) Requests that the privacy service performs the specified service or fail the request.

This optional keyword is only available after at least one of the privacy-option keywords ( header , history , id , session , or user ) has been specified and can be used only once per command.

### Command Default

Privacy support is disabled.

### Command Modes

Dial peer configuration (config-dial-peer)

## Command History

Release

Modification

12.4(15)T

This command was introduced.

12.4(22)T

The history keyword was added to provide support for the history-info header information.

### Usage Guidelines

Use the voice-class sip privacy command to instruct the gateway to add a Proxy-Require header, set to a value supported by RFC 3323, in outgoing SIP request
                              messages at the dial-peer level.

Use the voice-class sip privacy critical command to instruct the gateway to add a Proxy-Require header with the value set to critical. If a user agent sends a request
                              to an intermediary that does not support privacy extensions, the request fails.

The voice-class sip privacy command takes precedence over the privacy command in voice service voip sip configuration mode. However, if the voice-class sip privacy command is used with the system keyword, the gateway uses the settings configured globally by the privacy command.

## Examples

The following example shows how to disable the privacy on dial peer 2:

```
Router> enable Router# configure terminal Router(config)# dial-peer voice 2 voip Router(config-dial-peer)# voice-class sip privacy disable
```

The following example shows how to configure the voice-class sip privacy command so that the information held in the history-info header is hidden outside the trust domain:

```
Router> enable Router# configure terminal Router(config)# dial-peer voice 2 voip Router(config-dial-peer)# voice-class sip privacy history
```

### Related Commands

Command

Description

asserted-id

Sets the privacy level and enables either PAI or PPI privacy headers in outgoing SIP requests or response messages.

calling-info pstn-to-sip

Specifies calling information treatment for PSTN-to-SIP calls.

clid (voice-service-voip)

Passes the network-provided ISDN numbers in an ISDN calling party information element screening indicator field, removes the
                                          calling party name and number from the calling-line identifier in voice service voip configuration mode, or allows a presentation
                                          of the calling number by substituting for the missing Display Name field in the Remote-Party-ID and From headers.

privacy

Sets privacy support at the global level as defined in RFC 3323.

## voice-class sip privacy-policy

To configure the privacy header policy options at the dial-peer level, use the voice-class sip privacy-policy command in dial peer voice configuration mode. To disable privacy-policy options, use the no form of this command.

voice-class sip privacy-policy { passthru | send-always | strip { diversion | history-info }} [ system ]

no voice-class sip privacy-policy { passthru | send-always | strip { diversion | history-info }}

### Syntax Description

passthru

Passes the privacy values from the received message to the next call leg.

send-always

Passes a privacy header with a value of None to the next call leg, if the received message does not contain privacy values
                                          but a privacy header is required.

strip

Strip the diversion or history-info headers received from the next call leg.

diversion

Strip the diversion header received from the next call leg.

history-info

Strip the history-info header received from the next call leg.

system

(Optional) Uses the global configuration settings to configure the dial peer.

### Command Default

No privacy-policy settings are configured.

### Command Modes

Dial peer voice configuration (config-dial-peer)

## Command History

Release

Modification

12.4(22)YB

This command was introduced.

15.0(1)M

This command was integrated into Cisco IOS Release 15.0(1)M.

15.1(2)T

This command was integrated into Cisco IOS Release 15.1(2)T. The strip , diversion , and history-info keywords were added.

### Usage Guidelines

If a received message contains privacy values, use the voice-class sip privacy-policy passthru command to ensure that the privacy values are passed from one call leg to the next. If a received message does not contain
                              privacy values but the privacy header is required, use the voice-class sip privacy-policy send-always command to set the privacy header to None and forward the message to the next call leg. You can configure the system to support
                              both options at the same time.

The voice-class sip privacy-policy command takes precedence over the privacy-policy command in voice service voip sip configuration mode. However, if the voice-class sip privacy-policy command is used with the system keyword, the gateway uses the settings configured globally by the privacy-policy command.

## Examples

The following example shows how to enable the pass-through privacy policy on the dial peer:

```
Router> enable Router# configure terminal Router(config)# dial-peer voice 2611 voip Router(config-dial-peer)# voice-class sip privacy-policy passthru
```

The following example shows how to enable the pass-through, send-always, and strip policies on the dial peer:

```
Router> enable Router# configure terminal Router(config)# dial-peer voice 2611 voip Router(config-dial-peer)# voice-class sip privacy-policy passthru Router(config-dial-peer)# voice-class sip privacy-policy send-always Router(config-dial-peer)# voice-class sip privacy-policy strip diversion Router(config-dial-peer)# voice-class sip privacy-policy strip history-info
```

The following example shows how to enable the send-always privacy policy on the dial peer:

```
Router> enable Router# configure terminal Router(config)# dial-peer voice 2611 voip Router(config-dial-peer)# voice-class sip privacy-policy send-always
```

The following example shows how to enable both the pass-through privacy policy and send-always privacy policies on the dial
                              peer:

```
Router> enable Router# configure terminal Router(config)# dial-peer voice 2611 voip Router(config-dial-peer)# voice-class sip privacy-policy passthru Router(config-dial-peer)# voice-class sip privacy-policy send-always
```

### Related Commands

Command

Description

asserted-id

Sets the privacy level and enables either PAID or PPID privacy headers in outgoing SIP requests or response messages.

privacy-policy

Configures the privacy header policy options at the global configuration level.

## voice-class sip random-contact

To populate the outgoing INVITE message with random-contact information (instead of clear contact information) at the dial-peer
                              level, use the voice-class sip random-contact command in dial peer voice configuration mode. To disable random contact information, use the no form of this command.

voice-class sip random-contact [ system ]

no voice-class sip random-contact

### Syntax Description

system

(Optional) Uses the global configuration settings to populate the INVITE message with random contact information.

### Command Default

Support for random contact at the dial-peer level uses the the global configuration level settings.

### Command Modes

Dial peer voice configuration (config-dial-peer)

## Command History

Release

Modification

12.4(22)YB

This command was introduced.

15.0(1)M

This command was integrated into Cisco IOS Release 15.0(1)M.

### Usage Guidelines

To populate outbound INVITE messages (from the Cisco Unified Border Element) with random-contact information instead of clear-contact
                              information at the dial-peer level, use the voice-class sip random-contact command. This functionality will work only when the Cisco Unified Border Element is configured for SIP registration with
                              random-contact, using the credentials and registrar commands.

The voice-class sip random-contact command takes precedence over the random-contact command in voice service voip sip configuration mode. However, if the voice-class sip random-contact command is used with the system keyword, the gateway uses the settings configured globally by the random-contact command.

## Examples

The following example shows how to populate outbound INVITE messages, at the dial-peer level, with random-contact information:

```
Router> enable Router# configure terminal Router(config)# dial-peer voice 2611 voip Router(config-dial-peer)# voice-class sip random-contact
```

### Related Commands

Command

Description

credentials (sip ua)

Sends a SIP registration message from a Cisco Unified Border Element in the UP state.

registrar

Enables SIP gateways to register E.164 numbers on behalf of FXS, EFXS, and SCCP phones with an external SIP proxy or SIP registrar.

random-contact

Populates the outgoing INVITE message with random contact information at the global level.

## voice-class sip random-request-uri validate

To enable the validation of the called-number based on the random value generated during the registration of the number, at
                              dial-peer configuration level, use the voice-class sip random-request-uri validate command in dial peer voice configuration mode. To disable validation, use the no form of this command.

voice-class sip random-request-uri validate [ system ]

no voice-class sip random-request-uri validate

### Syntax Description

system

(Optional) Uses the global configuration settings to enable called-number validation on this dial peer.

### Command Default

Validation is disabled.

### Command Modes

Dial peer voice configuration (config-dial-peer)

## Command History

Release

Modification

12.4(22)YB

This command was introduced.

15.0(1)M

This command was integrated into Cisco IOS Release 15.0(1)M.

### Usage Guidelines

The system generates a random string when registering a new number. An INVITE message with the P-Called-Party-ID value can
                              have the Request-URI set to this random number. To enable the system to identify the called number from the random number
                              in the Request-URI, use the voice-class sip random-request-uri validate command on the inbound dial peer.

If the P-Called-Party-ID is not set in the INVITE message, the Request URI for that message must contain the called party
                              information (and cannot contain a random number). Therefore validation is performed only on INVITE messages with a P-Called-Party-ID.

The voice-class sip random-request-uri validate command takes precedence over the random-request-uri validate command in voice service voip sip configuration mode. However, if the voice-class sip random-request-uri validate command is used with the system keyword, the gateway uses the settings configured globally by the random-request-uri validate command.

## Examples

The following example shows how to enable call routing based on the P-Called-Party-ID header value at the dial-peer configuration
                              level:

```
Router> enable Router# configure terminal Router(config)# dial-peer voice 2611 voip Router(config-dial-peer)# voice-class sip random-request-uri validate
```

### Related Commands

Command

Description

credentials (sip ua)

Sends a SIP registration message from a Cisco Unified Border Element in the UP state.

random-request-uri validate

Validates the called number based on the random value generated during the registration of the number at the global configuration
                                          level.

registrar

Enables SIP gateways to register E.164 numbers on behalf of FXS, EFXS, and SCCP phones with an external SIP proxy or SIP registrar.

## voice-class sip referto-passing

To disable the modification of the Refer-To header during REFER message pass-through on the Cisco Unified Border Element
                              (UBE) on the specified dial peer, use the voice-class sip referto-passing command in dial peer voice configuration mode. To allow the modification of the Refer-To header during REFER message pass-through
                              on the Cisco UBE, use the no form of this command.

voice-class sip referto-passing [ system ]

no voice-class sip referto-passing

### Syntax Description

system

(Optional) Enables the referto-passing command configured in global configuration mode.

### Command Default

The Refer-To header modification is enabled.

### Command Modes

Dial peer voice configuration (config-dial-peer)

## Command History

Release

Modification

15.2(1)T

This command was introduced.

### Usage Guidelines

The dial peer configuration setting of the voice-class sip referto-passing command takes precedence over the global configuration setting of the referto-passing command. You can use the system keyword to toggle the precedence.

## Examples

The following example shows how to enable REFER message pass-through on the Cisco UBE for dial peer 22:

```
Router(config)# dial-peer voice 22 voip Router(config-dial-peer)# voice-class sip referto-passing
```

### Related Commands

Command

Description

dial-peer voice

Defines a particular dial peer, specifies the method of encapsulation, and enters dial peer voice configuration mode.

referto-passing

Disables dial peer lookup and modification of the Refer-To header when the Cisco UBE passes across a REFER message during
                                          a call transfer

## voice-class sip registration passthrough

To configure Session Initiation Protocol (SIP) registration pass-through options on a dial peer, use the voice-class sip registration passthrough command in dial peer voice configuration mode. To disable the configuration, use the no form of this command.

voice-class sip registration passthrough [ [ static ] [ rate-limit [ expires value ] [ fail-count value ]] [ registrar-index [index] ] | system ]

no voice-class sip registration passthrough

### Syntax Description

static

(Optional) Configures Cisco Unified Border Element (UBE) to use static registrar details for SIP registration. Cisco UBE works
                                          in point-to-point mode when the static keyword is used.

rate-limit

(Optional) Configures SIP registration pass-through rate-limiting options.

expires value

(Optional) Sets the expiry value for rate limiting, in seconds. The range is from 60 to 65535. The default is 3600.

fail-count value

(Optional) Sets the fail-count value for rate limiting. The range is from 2 to 20. The default is 0.

registrar-index

(Optional) Configures the registrar index used for registration pass-through.

index

(Optional) Registration index value. The range is from 1 to 6.

system

(Optional) Uses global registration pass-through configuration to configure the SIP registration pass-through options.

### Command Default

SIP registration pass-through options that are configured at the global level are configured.

### Command Modes

Dial peer voice configuration (config-dial-peer)

## Command History

Release

Modification

15.1(3)T

This command was introduced.

### Usage Guidelines

You can use the voice-class sip registration passthrough command to configure the following SIP pass-through functionalities on a dial peer:

Back-to-back registration facility to register phones for call routing.

Options to configure the rate-limiting values, such as the expiry time, fail-count, and a list of registrars to be used for
                                    registration.

## Examples

The following example shows how to set the registrar index of 1 for the SIP registration pass-through rate limiting:

```
Router# configure terminal Router(config)# dial-peer voice 444 voip Router(config-dial-peer)# voice-class sip registration passthrough static rate-limit registrar-index 1
```

### Related Commands

Command

Description

registration passthrough

Configures SIP registration pass-through options at the global level.

## voice-class sip rel1xx

To enable all Session Initiation Protocol (SIP) provisional responses (other than 100 Trying) to be sent reliably to the remote
                              SIP endpoint, use the voice-class sip rel1xx command in dial-peer configuration mode. To reset to the default, use the no form of this command.

voice-class sip rel1xx { supported value | require value | system | disable }

no sip rel1xx

### Syntax Description

supported value

Supports reliable provisional responses. The value argument may have any value, as long as both the user-agent client (UAC) and user-agent server (UAS) configure it the same.

require value

Requires reliable provisional responses. The value argument may have any value, as long as both the UAC and UAS configure it the same.

system

Uses the value configured in voice service mode. This is the default.

disable

Disables the use of reliable provisional responses.

### Command Default

system

### Command Modes

Dial-peer configuration

## Command History

Release

Modification

12.2(2)XB

This command was introduced.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T. Support for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and
                                          Cisco AS5850 is not included in this release.

12.2(11)T

This command was applicable to the Cisco AS5300, Cisco AS5350, and Cisco AS5400 in this release.

### Usage Guidelines

There are two ways to configure reliable provisional responses:

Dial-peer mode. You can configure reliable provisional responses for the specific dial peer only by using the voice-class sip rel1xx command.

SIP mode. You can configure reliable provisional responses globally by using the rel1xx command.

The use of resource reservation with SIP requires that the reliable provisional feature for SIP be enabled either at the VoIP
                              dial-peer level or globally on the router.

This command applies to the dial peer under which it is used or points to the global configuration for reliable provisional
                              responses. If the command is used with the supported keyword, the SIP gateway uses the Supported header in outgoing SIP INVITE requests. If it is used with the require keyword, the gateway uses the Required header.

This command, in dial-peer configuration mode, takes precedence over the rel1xx command in global configuration mode with one exception: If this command is used with the system keyword, the gateway uses
                              what was configured under the rel1xx command in global configuration mode.

## Examples

The following example shows how to use this command on either an originating or a terminating SIP gateway:

On an originating gateway, all outgoing SIP INVITE requests matching this dial peer contain the Supported header where value is 100rel.

On a terminating gateway, all received SIP  INVITE requests matching this dial peer support reliable provisional responses.

```
Router(config)# dial-peer voice 102 voip Router(config-dial-peer)# voice-class sip rel1xx supported 100rel
```

### Related Commands

Command

Description

rel1xx

Provides provisional responses for calls on all VoIP calls.

## voice-class sip
                        	 requri-passing

To enable the pass through of
                              		  Session Initiation Protocol (SIP) Uniform Resource Locator (URI) headers, use
                              		  the voice-class sip requri-passing command in
                              		  dial peer voice configuration mode. To disable this configuration, use the no form of the command.

voice-class sip requri-passing [ system ]

no voice-class sip requri-passing

## Syntax Description

(Optional)

### Command Default

The pass through of SIP URI
                              		  headers is not enabled.

### Command Modes

Dial peer voice configuration (config-dial-peer)

## Command History

15.4(1)T

This command was introduced.

## Examples

The following example shows how
                              		  to enable the pass through of SIP URI headers using the voice-class sip requri-passing command:

```
Device> enable Device# configure terminal Device(config)# voice class uri mydesturi sip Device(config-voice-uri-class)# host example.com Device(config-voice-uri-class)# exit Device(config)# dial-peer voice 22 voip Device(config-dial-peer)# session protocol sipv2 Device(config)# destination uri mydesturi Device(config-dial-peer)# session target ipv4:10.1.1.2 Device(config-dial-peer)# voice-class sip requri-passing system Device(config-dial-peer)# end
```

### Related Commands

Command

Description

contact-passing

Configures pass-through of the contact header from one leg
                                          						to the other leg for 302 pass-through.

requri-passing

Enables pass through of the host part of the Request-URI and
                                          						To SIP headers.

session target sip-uri

Derives session target from incoming URI.

voice-class sip requri-passing

Enables the pass through of SIP URI headers.

## voice-class sip reset timer expires

To configure an individual dial peer on Cisco Unified Communications Manager Express (Cisco Unified CME), a Cisco IOS voice
                              gateway, or a Cisco Unified Border Element (Cisco UBE) to reset the expires timer upon receipt of a Session Initiation Protocol
                              (SIP) 183 Session In Progress message, use the voice-class sip reset timer expires command in dial peer voice configuration mode. To globally disable resetting of the expires timer upon receipt of SIP 183
                              messages, use the no form of this command.

voice-class sip reset timer expires 183

no voice-class sip reset timer expires 183

### Syntax Description

183

Specifies resetting of the expires timer upon receipt of SIP 183 Session In Progress messages.

### Command Default

The expires timer is not reset after receipt of SIP 183 Session In Progress messages and a session or call that is not connected
                              within the default expiration time (three minutes) is dropped.

### Command Modes

Dial peer voice configuration (config-dial-peer)

## Command History

Release

Modification

15.0(1)XA

This command was introduced.

15.1(1)T

This command was integrated into Cisco IOS Release 15.1(1)T.

### Usage Guidelines

In some scenarios, early media cut-through calls (such as emergency calls) rely on SIP 183 with session description protocol
                              (SDP) Session In Progress messages to keep the session or call alive until receiving a FINAL SIP 200 OK message, which indicates
                              that the call is connected. In these scenarios, the call can time out and be dropped if it does not get connected within the
                              default expiration time (three minutes).

The expires timer default is three minutes. However, you can configure the expiration time to a maximum of 30 minutes using
                                          the timers expires command in SIP user agent (UA) configuration mode.

To prevent early media cut-through calls from being dropped on a specific dial peer because they reach the expires timer limit,
                              use the voice-class sip reset timer expires command in dial peer voice configuration mode.

To globally configure all dial peers on Cisco Unified CME, a Cisco IOS voice gateway, or a Cisco UBE so that the expires timer
                              is reset upon receipt of any SIP 183 message, use the reset timer expires command in voice service SIP configuration mode. To disable resetting of the expires timer on receipt of SIP 183 messages
                              for an individual dial peer, use the no voice-class sip reset timer expires command in dial peer voice configuration mode.

## Examples

The following example shows how to configure dial peer 1 on Cisco Unified CME, a Cisco IOS voice gateway, or a Cisco UBE to
                              reset the expires timer each time a SIP 183 message is received:

```
Router> enable Router# configure terminal Router(config)# dial-peer voice 1 voip Router(config-dial-peer)# voice-class sip reset timer expires 183
```

### Related Commands

Command

Description

reset timer expires

Globally configures Cisco Unified CME, a Cisco IOS voice gateway, or a Cisco UBE to reset the expires timer upon receipt of
                                          a SIP 183 message.

timers expires

Specifies how long a SIP INVITE request remains valid before it times out if no appropriate response is received for keeping
                                          the session alive.

## voice-class sip resource priority dscp-profile

To apply a differentiated services code point (DSCP) profile to a dial peer, use the voice-class sip resource priority dscp-profile in dial peer voice configuration mode. To disable the configuration, use the no form of this command.

voice-class sip resource priority dscp-profile tag

no voice-class sip resource priority dscp-profile

### Syntax Description

tag

DSCP profile group tag number. The range is from 1 to 10000.

### Command Default

A DSCP profile is not applied.

### Command Modes

Dial peer voice configuration (config-dial-peer)

## Command History

Release

Modification

15.2(2)T

This command was introduced.

### Usage Guidelines

You can use the voice-class sip resource priority dscp-profile command to apply the DSCP profile that is configured using the dscp media command for a dial peer.

## Examples

The following example shows how to configure a DSCP profile for a dial peer:

```
Router> enable Router# configure terminal Router(config)# dial-peer voice 4 voip Router(config-dial-peer)# voice-class sip resource priority dscp-profile 1
```

### Related Commands

Command

Description

dial-peer voice

Configures a dial peer and enters dial peer voice configuration mode.

dscp media

Specifies the RPH to DSCP mapping.

## voice-class sip resource priority mode (dial-peer)

To push the user access server (UAS) to operate in a loose or strict mode, use the voice-class sip resource priority mode command in dial peer voice configuration mode. To disable the voice-class sip resource priority mode , use the no form of this command.

voice-class sip resource priority mode [ loose | strict ]

no voice-class sip resource priority mode [ loose | strict ]

### Syntax Description

loose

(Optional) In the loose mode, unknown values of name space or priority values received in the Resource-Priority header in
                                          Session Initiation Protocol (SIP) requests are ignored by the gateway. The request is processed as if the Resource-Priority
                                          header was not present.

strict

(Optional) In the strict mode, unknown values of name space or priority values received in the Resource-Priority header in
                                          SIP requests are rejected by the gateway using a SIP response code 417 (Unknown Resource-Priority) message response. An Accept-Resource-Priority
                                          header enumerating the supported name space and values is included in the 417 message response.

### Command Default

The default value is loose mode .

### Command Modes

Dial peer voice configuration

## Command History

Release

Modification

12.4(2)T

This command was introduced.

### Usage Guidelines

When the no version of this command is executed, the call operates in the loose mode.

## Examples

The following example shows how to set up the voice-class sip resource priority mode command in loose mode:

```
Router(config)# dial-peer voice 102 voip
Router(config-dial-peer)# voice-class sip resource priority mode loose
```

The following example shows how to set up the voice-class sip resource priority mode command in strict mode:

```
Router(config)# dial-peer voice 102 voip
Router(config-dial-peer)# voice-class sip resource priority mode strict
```

### Related Commands

Command

Description

voice-class sip resource priority namespace

Priorities mandatory call prioritization handling for initial original INVITE message requests.

## voice-class sip resource priority namespace (dial-peer)

To prioritize mandatory call prioritization handling for initial original INVITE message requests, use the voice-class sip resource priority namespace command in dial peer voice configuration mode. To disable the voice-class sip resource priority namespace command, use the no form of this command.

voice-class sip resource priority namespace [ drsn | dsn | q735 ]

no voice-class sip resource priority namespace [ drsn | dsn | q735 ]

### Syntax Description

drsn

(Optional) U. S. Defense Red Switched Network (DRSN).

dsn

(Optional) U. S. Defense Switched Network (DSN).

q735

(Optional) International Telecommunications Union, Stage 3 description for community of interest supplementary services using Signaling System No. 7: Multilevel precedence
                                             and preemption, Recommendation Q.735.3 , March 1993.

### Command Default

When the no version of this command is executed using namespace, the Cisco IOS gateway transparently passes the multilevel
                              precedence and preemption (MLPP) values that were received on the PSTN side.

### Command Modes

Dial peer voice configuration

## Command History

Release

Modification

12.4(2)T

This command was introduced.

### Usage Guidelines

When the no version of this command is executed using the namespace, the Cisco IOS gateway transparently passes the multilevel
                              precedence and preemption (MLPP) values that were received on the PSTN side.

## Examples

The following example shows how to set up the voice-class sip resource priority namespace command in the U. S. DSN format name space:

```
Router(config)# dial-peer voice 102 voip Router(config-dial-peer)# voice-class sip resource priority namespace dsn
```

The following example shows how to set up the voice-class sip resource priority namespace command in the U. S. DRSN format name space:

```
Router(config)# dial-peer voice 102 voip Router(config-dial-peer)# voice-class sip resource priority namespace drsn
```

The following example shows how to set up the voice-class sip resource priority namespace command in the Public SS7 Network format name space:

```
Router(config)# dial-peer voice 102 voip Router(config-dial-peer)# voice-class sip resource priority namespace q735
```

### Related Commands

Command

Description

voice-class sip resource priority mode

Pushes the UAS to operate in a loose or strict mode.

## voice-class sip rsvp-fail-policy

To specify the action that takes place at the dial peer level on a Cisco IOS Session Initiation Protocol (SIP) gateway when
                              Resource Reservation Protocol (RSVP) negotiation fails, use the voice-class sip rsvp-fail-policy command in dial peer configuration mode. To reset failure behavior to the default settings, use the no form of this command.

voice-class sip rsvp-fail-policy { video | voice } post-alert { optional keep-alive | mandatory { keep-alive | disconnect retry retry-attempts }} interval seconds

no voice-class sip rsvp-fail-policy { video | voice } post-alert { optional [ keep-alive ] | mandatory [ keep-alive | disconnect retry retry-attempts ]} [ interval seconds ]

### Syntax Description

video

Specifies the video RSVP stream type.

voice

Specifies the audio or fax RSVP stream type.

post-alert

Specifies that behavior takes place only when the call state is post alert.

optional

Specifies that behavior takes place when RSVP fails even if RSVP negotiation is optional.

mandatory

Specifies that behavior takes place when RSVP fails only if RSVP negotiation is mandatory.

keep-alive

Specifies the sending of keepalive messages when RSVP fails.

disconnect

Specifies that the call is disconnected if RSVP fails after the specified number of retry settings.

retry

Specifies the number of reconnection attempts before disconnecting the call.

retry-attempts

The number of retry attempts. Valid entries are from 1 to 100.

interval

Specifies the interval between keepalive or retry attempts.

seconds

The retry interval in seconds. Valid entries are from 5 to 3600.

### Command Default

Keepalive messages are sent at 30-second intervals when a post alert voice or video call fails to negotiate RSVP regardless
                              of the RSVP negotiation setting (mandatory or optional).

### Command Modes

Dial peer configuration (config-dial-peer)

## Command History

Release

Modification

12.4(22)T

This command was introduced.

### Usage Guidelines

Use this command to configure call handling behavior when a call fails RSVP negotiation. You can configure the behavior that
                              takes place for either optional or mandatory RSVP negotiation but the behavior will apply only to calls in a post alert call
                              state. To configure the behavior that takes place when RSVP negotiation fails, use the voice-class sip rsvp-fail-policy command in dial peer configuration mode.

If a call fails RSVP negotiation where negotiation is optional, then RSVP negotiation should be retried using the keepalive
                              function at specified intervals until RSVP negotiation is successful.

If a call fails RSVP negotiation where negotiation is mandatory, then RSVP negotiation should be configured in one of two
                              ways:

The call that failed RSVP negotiation is disconnected after a specified number of attempts to renegotiate RSVP with each retry
                                    taking place at a specified interval. If negotiation succeeds during these retry attempts, counters and timers are reset to
                                    zero.

The call that failed RSVP negotiation is kept alive with keepalive messages sent at specified intervals until negotiation
                                    is successful.

## Examples

The following example shows how to specify sending of keepalive messages at 60-second intervals for a call that fails RSVP
                              negotiation when negotiation is optional:

```
Router(config)# dial-peer voice 102 voip Router(config-dial-peer)# voice-class sip rsvp-fail-policy voice post-alert optional keep-alive interval 60
```

### Related Commands

Command

Description

acc-qos

Defines the acceptable QoS for inbound and outbound calls on a VoIP dial peer.

handle-replaces

Configures fallback to legacy handling of SIP INVITE.

ip qos defending-priority

Configures the RSVP defending priority value.

ip qos dscp

Sets the DSCP value for QoS.

ip qos policy-locator

Configures application-specific reservations (application IDs) used for specifying bandwidth reservations.

ip qos preemption-priority

Configures the RSVP preemption priority value.

req-qos

Requests a particular QoS using RSVP to be used in reaching a specified dial peer in VoIP.

show-sip-ua calls

Displays the active UAC and UAS information on SIP calls.

## voice-class sip send 180 sdp

To configure a Cisco Unified Border Element (Cisco UBE) to map an incoming 180 Session Description Protocol (SDP) message
                              to a 180 SDP message, use the voice-class sip send 180 sdp command in dial peer voice configuration mode or SIP configuration mode. To disable this functionality, use the no form of this command.

voice-class sip send 180 sdp

no voice-class sip send 180 sdp

### Syntax Description

This command has no arguments or keywords.

### Command Default

This command is disabled. Cisco UBE converts an incoming 180 SDP message to a 183 SDP message.

### Command Modes

Dial peer voice configuration (config-dialpeer)

SIP configuration (conf-serv-sip)

## Command History

Release

Modification

15.2(4)M

This command was introduced.

### Usage Guidelines

This command must be enabled at the inbound dial peer. Enable the voice-class sip send 180 sdp command to map a 180 SDP message to a 180 SDP message. When this command is disabled, an incoming 180 SDP (Ringing) message
                              is mapped to a 183 SDP (Session in Progress) message.

## Examples

The following example shows how to configure the voice-class sip send 180 sdp command at dial peer level:

```
Device> enable Device# configure terminal Device(config)# dial peer voice Device(config-dialpeer)# voice-class sip send 180 sdp Device(config-dialpeer)# exit
```

### Related Commands

Command

Description

voice-class sip block

Configures an individual dial peer on a Cisco IOS voice gateway or Cisco UBE to drop (not pass) specific incoming Session
                                          Initiation Protocol (SIP) provisional response messages.

## voice-class sip
                        	 srtp-auth

Effective Cisco IOS XE Everest Releases 16.5.1b, srtp-auth command is deprecated. Although this command is still available in Cisco IOS XE Everest software, executing this command
                                          does not cause any configuration changes. Use voice class srtp-crypto command to configure SRTP connection using preferred crypto-suites. For more information, see voice-class sip srtp-crypto command documentation.

To configure a
                              		  Secure Real-time Transport Protocol (SRTP) connection on Cisco Unified Border
                              		  Element (Cisco UBE) using the preferred crypto suite in the dial peer level,
                              		  use the voice-class sip
                                    				srtp-auth command in dial peer voice configuration mode. To
                              		  disable this configuration, use the no form of
                              		  the command.

voice-class sip srtp-auth { sha-32 | sha-80 | system }

no voice-class sip srtp-auth

## Syntax Description

Allows
                                       					 secure calls with AES_CM_128_HMAC_SHA1_32 authentication suite.

Allows
                                       					 secure calls with AES_CM_128_HMAC_SHA1_80 authentication suite.

Uses the
                                       					 global configuration.

### Command Default

The sha-32 crypto
                              		  suite is configured by default.

### Command Modes

Dial peer voice configuration (config-dial-peer)

## Command History

15.4(1)T

This
                                       					 command was introduced.

Cisco IOS XE Everest 16.5.1b

This command was deprecated.

### Usage Guidelines

Use the system keyword with the voice-class sip srtp-auth command to use the
                              		  crypto suite configured at the global level.

## Examples

The following
                              		  example shows how to configure an SRTP connection on Cisco UBE in the dial peer
                              		  level using the AES_CM_128_HMAC_SHA1_80 crypto suite:

```
Device> enable Device# configure terminal Device(config)# dial-peer voice 15 voip Device(config-dial-peer)# voice-class sip srtp-auth sha1-80
```

### Related Commands

Command

Description

srtp-auth

Configures a Secure Real-time Transport Protocol (SRTP)
                                          						connection on Cisco Unified Border Element (Cisco UBE) in the global level
                                          						using the preferred crypto suite.

show sip-ua srtp

Displays Session
                                          						Initiation Protocol (SIP) user-agent (UA) Secure Real-time Transport Protocol
                                          						(SRTP) information.

## voice-class sip
                        	 srtp-crypto

To assign a
                              		  previously configured crypto-suite selection preference to a dial-peer, use the voice-class sip
                                    				srtp-crypto command. To remove the crypto-suite preference from
                              		  the dial-peer and return to the default preference list, use the no or default form of this command.

voice-class sip srtp-crypto crypto-tag

no voice-class sip srtp-crypto

default voice-class sip srtp-crypto

## Syntax Description

Unique
                                       					 number assigned to the voice class. The range is from 1 to 10000.

This
                                       					 number maps to the tag created using the voice class
                                             						  srtp-crypto command available in global configuration mode.

### Command Default

No crypto-suite
                              		  preference is assigned to the dial-peer.

### Command Modes

dial-peer configuration (config-dial-peer)

## Command History

Cisco IOS XE Everest 16.5.1b

This
                                       					 command was introduced.

### Usage Guidelines

Ensure that an srtp voice-class is created using the voice class srtp-crypto crypto-tag command before executing the voice-class sip srtp-crypto crypto tag command to apply the crypto-tag
                                          			 under global or tenant configuration mode.

You can assign
                              		  only one crypto-tag. If you assign another crypto-tag, the last crypto-tag
                              		  assigned replaces the previous crypto-tag.

## Examples

```
Device enable Device# configure terminal Device(config)# dial-peer voice 300 voip Device(config-dial-peer)# voice-class sip srtp-crypto 102
```

### Related Commands

Command

Description

srtp-crypto

Assigns a previously configured crypto-suite selection preference list globally or to a voice class tenant.

crypto

Specifies the preference for a SRTP cipher-suite that will be offered by Cisco Unified Border Element (CUBE) in the SDP in
                                          offer and answer.

show sip-ua calls

Displays active user agent client (UAC) and user agent server (UAS) information on Session Initiation Protocol (SIP) calls.

show sip-ua srtp

Displays Session Initiation Protocol (SIP) user-agent (UA) Secure Real-time Transport Protocol (SRTP) information.

## voice-class sip srtp negotiate

To enable Secure Real-Time Transport Protocol (SRTP) negotiation so that an individual dial peer on a Cisco IOS Session Initiation
                              Protocol (SIP) gateway can accept and send an RTP Audio/Video Profile (AVP) in response to an RTP Secure AVP offer (also known
                              as an SRTP profile), use the voice-class sip srtp negotiate command in dial peer voice configuration mode. To return to the default (global) SRTP negotiation setting on a dial peer,
                              use the system keyword. To disable SRTP negotiation on a dial peer, use the no form of this command.

voice-class sip srtp negotiate { cisco | system }

no voice-class sip srtp negotiate

### Syntax Description

cisco

Enables an individual dial peer on a Cisco IOS SIP gateway to negotiate the sending and accepting of RTP profiles in response
                                          to SRTP offers, overriding the global setting for the gateway.

system

Specifies that the individual dial peer use global (system) SRTP negotiation settings for the Cisco IOS SIP gateway. This
                                          is the default setting.

### Command Default

SRTP negotiation is determined by global settings for the Cisco IOS gateway ( voice-class sip srtp negotiate system ).

### Command Modes

Dial peer voice configuration (config-dial-peer)

## Command History

Release

Modification

12.4(15)XY

This command was introduced.

12.4(20)T

This command was integrated into Cisco IOS Release 12.4(20)T.

12.4(22)T

Support was extended to the Cisco Unified Border Element.

### Usage Guidelines

The srtp fallback command enables a SIP gateway (or individual dial peer on a SIP gateway) to allow SRTP fallback using SIP 4 xx message responses. With the srtp negotiate command, a SIP gateway can be configured to accept and send an RTP (nonsecure) profile in response to an SRTP profile.

Use the voice-class sip srtp negotiate command in dial peer voice configuration mode to enable SRTP negotiation for an individual dial peer on a Cisco IOS SIP gateway,
                              overriding the global settings on the gateway. Enabling SRTP negotiation allows a dial peer to accept and send nonsecure RTP
                              profiles in response to SRTP offers. To configure global SRTP negotiation settings for a SIP gateway, use the srtp negotiate command in voice service SIP configuration mode.

There are two scenarios for SRTP negotiation when the voice-class sip srtp negotiate command is enabled:

On a SIP dial peer with the srtp fallback command enabled, the dial peer accepts RTP answers to SRTP offers.

On a SIP dial peer with the srtp fallback command disabled, the dial peer allows incoming SRTP calls and responds with an RTP answer.

These behaviors are accomplished using the “X-cisco-srtp-fallback” extension in the supported header of initial SIP messages
                              involved in establishment of the session.

## Examples

The following example shows SRTP negotiation being enabled on a dial peer, overriding global settings:

```
Device(config)# dial-peer voice 1 Device(config-dial-peer)# voice-class sip srtp negotiate cisco
```

### Related Commands

Command

Description

srtp (dial peer)

Specifies that an individual dial peer use SRTP to enable secure calls and, optionally, enables fallback to RTP (overriding
                                          global settings).

srtp (voice)

Specifies use of SRTP to enable secure calls and, optionally, enables fallback to RTP globally on a Cisco IOS SIP gateway.

srtp negotiate

Enables SRTP negotiation globally on a Cisco IOS SIP gateway.

## voice-class sip tel-config to-hdr

To configure the To: Header (to hdr) request Uniform Resource Identifier (URI) to telephone (TEL) format for dial-peer VoIP
                              Session Initiation Protocol (SIP) calls, use the voice-class sip tel-config to-hdr command in dial peer voice configuration mode. To reset to the default, use the no form of this command.

voice-class sip tel-config to-hdr { phone-context | system }

no voice-class sip tel-config to-hdr

### Syntax Description

phone-context

Appends the phone context parameter to the TEL URL on a dial-peer basis.

system

Uses the system value. This is the default.

### Command Default

The To: Header request URIs at the dial-peer level use the global configuration level settings.

### Command Modes

Dial peer voice configuration (config-dial-peer)

## Command History

Release

Modification

12.4(22)YB

This command was introduced.

12.4(24)T

This command was integrated into Cisco IOS Release 12.4(24)T.

### Usage Guidelines

The voice-class sip tel-config to-hdr command takes precedence over the tel-config to-hdr command configured in SIP configuration mode. However, if the voice-class sip tel-config to-hdr command is used with the system keyword, the gateway uses the global settings configured by the tel-config to-hdr command.

## Examples

The following example configures the To: header in TEL format for a dial peer VoIP SIP call, and appends the phone-context
                              parameter:

```
dial-peer voice 102 voip
 voice-class sip tel-config to-hdr phone-context
```

### Related Commands

Command

Description

tel-config to-hdr

Configures the To: Header Request URI to telephone format for VoIP SIP calls.

## voice-class sip
                        	 tenant

To associate a
                              		  dial-peer with a specific tenant configuration, use the voice-class sip tenant command in dial-peer configuration mode. To
                              		  remove the association, use the no form of
                              		  this command.

voice-class sip tenant tag

no voice-class sip tenant tag

### Syntax Description

tag

A
                                          						number used to identify voice-class sip tenant. The range is from 1 to 10000.

### Command Default

No default
                              		  behavior or values.

### Command Modes

Dial peer voice configuration (config-dial-peer)

## Command History

Release

Modification

15.6(2)T and IOS XE Denali 16.3.1

This
                                          						command was introduced.

### Usage Guidelines

Use the voice-class sip tenant <tag> command in dial-peer configuration
                              		  mode to associate the dial-peer with a voice-class sip tenant <tag> . If the dial-peer is associated with a
                              		  tenant, the configurations are applied in the following order of preference:

Dial-peer
                                    				configuration

Tenant
                                    				configuration

Global
                                    				configuration

If there are no
                              		  tenants configured under dial-peer, then configurations are applied using the
                              		  default behavior in the following order:

Dial-peer
                                    				configuration

Global
                                    				configuration

## Examples

The following
                              		  example shows how to configure the voice-class sip tenant <tag> command in dial-peer configuration
                              		  mode:

```
Router(config)# dial-peer voice 10 voip
Router(config-dial-peer)# voice-class sip tenant <tag> Router(config-dial-peer)# end
```

## voice-class sip transport switch

To enable switching between UDP and TCP transport mechanisms for large Session Initiation Protocol (SIP) messages for a specific
                              dial peer, use the voice-class sip transport switch command in dial-peer configuration mode. To disable switching between UDP and TCP transport mechanisms for large SIP messages
                              for a specific dial peer, use the no form of this command.

voice-class sip transport switch udp tcp

no voice-class sip transport switch udp tcp

### Syntax Description

udp

Enables switching transport from UDP on the basis of the size of the SIP request being greater than the MTU size.

tcp

Enables switching transport to TCP.

### Command Default

Disabled.

### Command Modes

Dial-peer configuration

## Command History

Release

Modification

12.3(8)T

This command was introduced.

### Usage Guidelines

The voice-class sip transport switch command takes precedence over the global transport switch command.

## Examples

The following example shows how to set up the voice-class sip transport switch command:

```
Router(config)# dial-peer voice 102 voip Router(config-dial-peer)# voice-class sip transport switch udp tcp
```

### Related Commands

Command

Description

debug ccsip transport

Enables tracing of the SIP transport handler and the TCP or UDP process.

transport switch

Enables switching between transport mechanisms globally if the SIP message is larger than 1300 bytes.

## voice-class sip url

To configure URLs to either the Session Initiation Protocol (SIP), SIP security (SIPS), or telephone (TEL) format for your
                              dial-peer SIP calls, use the voice-class sip url command in dial peer voice configuration mode. To reset to the default value use the no form of this command.

voice-class sip url { sip | sips | tel [ phone-context ] | system }

no voice-class sip url

### Syntax Description

sip

Generates URLs in the SIP format for calls on a dial-peer basis.

sips

Generates URLs in the SIPS format for calls on a dial-peer basis.

tel

Generates URLs in the TEL format for calls on a dial-peer basis.

phone-context

(Optional) Appends the phone context parameter to the TEL URL on a dial-peer basis.

system

Uses the system value. This is the default.

### Command Default

SIP calls at the dial-peer level use the global configuration level settings.

### Command Modes

Dial peer voice configuration (config-dial-peer)

## Command History

Release

Modification

12.2(2)XB

This command was introduced.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T. Support for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and
                                          Cisco AS5850 was not included in this release.

12.2(11)T

This command was implemented on the Cisco AS5300, Cisco AS5350, and Cisco AS5400 platforms.

12.4(6)T

The sips keyword was added.

12.4(22)YB

The phone-context keyword was added.

15.0(1)M

This command was integrated into Cisco IOS Release 15.0(1)M.

### Usage Guidelines

This command affects only user-agent clients (UACs), because it causes the use of a SIP, SIPS, or TEL URL in the request line
                              of outgoing SIP INVITE requests. SIP URLs indicate the originator, recipient, and destination of the SIP request; TEL URLs
                              indicate voice-call connections.

The voice-class sip url command takes precedence over the url command configured in SIP configuration mode. However, if the voice-class sip url command is used with the system keyword, the gateway uses what was globally configured with the url command.

## Examples

The following example shows how to configure the voice-class sip url command to generate URLs in the SIP format:

```
dial-peer voice 102 voip
 voice-class sip url sip
```

The following example shows how to configure the voice-class sip url command to generate URLs in the SIPS format:

```
dial-peer voice 102 voip
 voice-class sip url sips
```

The following example shows how to configure the voice-class sip url command to generate URLs in the TEL format:

```
dial-peer voice 102 voip
 voice-class sip url tel
```

The following example shows how to configure the voice-class sip url command to generate URLs in the TEL format, and append the phone-context parameter:

```
dial-peer voice 102 voip
 voice-class sip url tel phone-context
```

### Related Commands

Command

Description

sip url

Generates URLs in the SIP, SIPS, or TEL format.

url

Configures URLs to either SIP, SIPS, or TEL format.

## voice-class source interface

To allow a loopback interface to be associated with a VoIP or VoIPv6 dial-peer profile, use the voice-class source interface command in dial peer configuration mode. To disable this association, use the no form of this command.

voice-class source interface loopback interface-id [ ipv4-address | ipv6-address ]

no voice-class source interface loopback interface-id [ ipv4-address | ipv6-address ]

### Syntax Description

loopback

Specifies the loopback interface address.

interface-id

Specifies the interface on which the address is to be configured.

ipv4-address

(Optional) IPv4 address used in the loopback interface address.

ipv6-address

(Optional) IPv6 address used in the loopback interface address.

### Command Default

No loopback interface is associated with a VoIPv6 dial-peer profile.

### Command Modes

Dial peer configuration (config-dial-peer)

## Command History

Release

Modification

12.4(22)T

This command was introduced.

### Usage Guidelines

When the voice-class source interface command is configured, the source address of Routing Time Protocol (RTP) generated by the DSPs in the voice gateway is taken
                              from the address configured under the loopback interface. This command is used for policy-based routing (PBR) of RTP packets
                              originated by the gateway. The policy route map is configured under the loopback interface, and then the loopback interface
                              is specified under the VoIP or VoIPv6 dial peer using the voice-class source interface command.

This command only applies to voice gateway scenarios for routers connecting telephony equipment through E1/T1, BRI or analog
                              ports to the IP network. It does not apply to Cisco Unified Border Element (CUBE) in IP to IP voice scenarios (with or without
                              transcoding). PBR for RTP traffic is not implemented in CUBE.

## Examples

The following example associates a loopback interface with a VoIPv6 dial-peer profile:

```
Router(config)# dial-peer voice 1 voip Router (config-dial-peer)# voice-class source interface loopback0
```

### Related Commands

Command

Description

dial-peer voice

Defines a particular dial peer, specifies the method of voice encapsulation, and enters dial
                                          
                                          peer configuration mode.

## voice-class stun-usage

To configure voice class, enter voice class configuration mode called stun-usage and use the voice-class stun-usage command in global, dial-peer, ephone, ephone template, voice register pool, or voice register pool template configuration
                              mode. To disable the voice class, use the no form of this command.

voice-class stun-usage tag

no voice-class stun-usage tag

### Syntax Description

tag

Unique identifier in the range 1 to 10000.

### Command Default

The voice class is not defined.

### Command Modes

Global configuration (config) Dial peer configuration (config-dial-peer) Ephone configuration (config-ephone) Ephone template configuration (config-ephone-template) Voice register pool configuration (config-register-pool) Voice register pool template configuration (config-register-pool)

## Command History

Release

Cisco Product

Modification

12.4(22)T

Cisco Unified CME 7.0

This command was introduced.

15.1(2)T

Cisco Unified CME 8.1

This command was modified. This command can be enabled in ephone summary, ephone template, voice register pool, or voice register
                                          pool template configuration mode.

### Usage Guidelines

When the voice-class stun-usage is removed, the same is removed automatically from the dial-peer, ephone, ephone template,
                              voice register pool, or voice register pool template configurations.

## Examples

The following example shows how to set the voice class stun-usage tag to 10000:

```
Router(config)# voice class stun-usage 10000 Router(config-ephone) # voice class stun-usage 10000 Router(config-voice-register-pool) # voice class stun-usage 10000
```

### Related Commands

Command

Description

stun usage firewall-traversal flowdata

Enables firewall traversal using STUN.

stun flowdata agent-id

Configures the agent ID.

## voice-class tone-signal

To assign a previously configured tone-signal voice class to a voice port, use the voice-class tone-signal command in voice-port configuration mode. To delete a tone-signal voice class, use the no form of this command.

voice-class tone-signal tag

no voice-class tone-signal tag

### Syntax Description

tag

Unique label assigned to the voice class. The tag label maps to the tag label created using the voice class tone-signal global configuration command. Can be up to 32 alphanumeric characters.

### Command Default

Voice ports have no tone-signal voice class assigned.

### Command Modes

Voice-port configuration

## Command History

Release

Modification

12.3(4)XD

This command was introduced.

12.3(7)T

This command was integrated into Cisco IOS Release 12.3(7)T.

### Usage Guidelines

The voice-class tone-signal command is available on an ear and mouth (E&M) voice port only if the signal type for that port is Land Mobile Radio (LMR).
                              Note that the hyphenation in this command differs from the hyphenation used in a similar command, voice class tone-signal , which is used in global configuration mode.

## Examples

The following example assigns a previously configured voice class to voice port 1/1/0:

```
voice-port 1/0/0
 voice-class tone-signal mytones
```

### Related Commands

Command

Description

voice class tone-signal

Enters voice-class configuration mode and assigns an identification tag number for a tone-signal voice class.

## voice-ctl-file

To create a  Cisco Certificate Trust List (CTL) file  for a Cisco Unified Communications Manager (CUCM) cluster  and to enter
                              CTL file configuration mode,  use the voice-ctl-file command in global configuration mode. To remove a  CTL file for a CUCM cluster, use the no form of the command.

voice-ctl-file ctl-file-name

no voice-ctl-file ctl-file-name

## Syntax Description

Name of the CTL  file. A maximum number of 30 characters can be entered for the CTL file name.

### Command Default

None

### Command Modes

Global configuration mode (config)

## Command History

15.3(3)M

This command was introduced.

### Usage Guidelines

The voice-ctl-file command allows you to create an instance of a CTL file for a CUCM cluster. In CTL file configuration mode you can specify
                              the trustpoints to be used for the creation of the CTL file.

## Examples

The following example shows how to create a CTL file instance called “myctl”:

```
Device(config)# voice-ctl-file myctl
```

## voice confirmation-tone

To disable the two-beep confirmation tone for private line, automatic ringdown (PLAR), or PLAR off-premises extension (OPX)
                              connections, use the voice confirmation-tone command in voice-port configuration mode. To enable the two-beep confirmation tone, use the no form of this command.

voice confirmation-tone

no voice confirmation-tone

### Syntax Description

This command has no arguments or keywords.

### Command Default

The two-beep confirmation tone is heard on PLAR and PLAR OPX connections.

### Command Modes

Voice-port configuration

## Command History

Release

Modification

11.3(1)MA

This command was introduced on Cisco MC3810.

### Usage Guidelines

Use this command to disable the two-beep confirmation tone that a caller hears when picking up the handset for PLAR and PLAR
                              OPX connections. This command is valid only if the voice-port connection command is set to PLAR or PLAR OPX.

## Examples

The following example disables the two-beep confirmation tone on voice port 1/0/0:

```
voice-port 1/0/0
 connection plar-opx
 voice confirmation-tone
```

### Related Commands

Command

Description

connection

Specifies a connection mode for a voice port.

## voice dnis-map

To create or modify a Digital Number Identification Service (DNIS) map, use the voice dnis-map command in global configuration mode. To delete a DNIS map, use the no form of this command.

voice dnis-map map-name [url]

no voice dnis-map map-name

### Syntax Description

map-name

Name of the DNIS map.

url

(Optional) URL of an external text file that contains a list of DNIS entries.

### Command Default

No default behavior or values

### Command Modes

Global configuration

## Command History

Release

Modification

12.2(2)XB

This command was introduced on the Cisco AS5300, Cisco AS5350, and Cisco AS5400.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T and implemented on the Cisco 3640 and Cisco 3660.

### Usage Guidelines

A DNIS map is a table of DNIS numbers associated with a single dial peer. For applications such as VoiceXML, using a DNIS
                              map makes it possible to configure a single dial peer for all DNIS numbers used to refer to VoiceXML documents. Keep the following
                              considerations in mind when using voice DNIS maps.

A separate entry must be made for each DNIS entry in a DNIS map. Wildcards are not supported.

If a URL is not supplied, the command enters DNIS-map configuration mode, permitting the entry of DNIS numbers by using the dnis command.

The URL argument points to the location of an external text file containing a list of DNIS entries ( for example: tftp://dnismap.txt). This allows the administrator to maintain a single primary file of all DNIS map entries, if
                                    desired, rather than configuring the DNIS entries on each gateway.

The name of the text file extension is not significant; .doc, .txt, or .cfg are all acceptable because the extension is not
                              checked. The entries in the file should look the same as a DNIS entry configured in Cisco IOS software (for example: dnis
                              5553305 url tftp://global/tickets/movies.vxml).

External text files used for DNIS maps must be stored on TFTP servers; they cannot be stored on HTTP servers.

To associate a DNIS map with a dial peer, use the dnis-map command.

To view the configuration information for DNIS maps, use the show voice dnis-map command.

## Examples

The following example shows how the voice dnis-map command is used to create a DNIS map:

```
voice dnis-map dmap1
```

The following example shows the voice dnis-map command used with a URL that specifies the location of a text file containing
                              the DNIS entries:

```
voice dnis-map dmap2 tftp://keyer/dmap2/dmap2.txt
```

Following is an example of the contents of a text file comprising a DNIS map:

```
!Example dnis-map with 8 entries.
!
dnis 5550112 url tftp://global/ticket/vapptest1.vxml
dnis 5550111 url tftp://global/ticket/vapptest2.vxml
dnis 5550134 url tftp://global/ticket/vapptest3.vxml
dnis 5550178
dnis 5550100
dnis 5550101
dnis 5550102
dnis 5550103
```

### Related Commands

Command

Description

dnis

Adds a DNIS number to a DNIS map.

dnis-map

Associates a DNIS map with a dial peer.

show voice dnis-map

Displays configuration information about DNIS maps.

voice dnis-map load

Reloads a DNIS map that has changed since the previous load.

## voice dnis-map load

To reload a DNIS map that has been modified, use the voice dnis-map load command in privileged EXEC mode. This command does not have a no form.

voice dnis-map load map-name

### Syntax Description

map-name

Name of the DNIS map to reload.

### Command Default

No default behavior or values

### Command Modes

Privileged EXEC

## Command History

Release

Modification

12.2(2)XB

This command was introduced on the Cisco AS5300, Cisco AS5350, and Cisco AS5400.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T and implemented on the Cisco 3640 and Cisco 3660.

### Usage Guidelines

This command reloads a DNIS map residing on an external server. Use this command when the DNIS map file has changed since
                              the previous load.

To create or modify a DNIS map, use the voice dnis-map command.

## Examples

The following example reloads a DNIS map named "mapfile1":

```
Router# voice dnis-map load mapfile1
```

### Related Commands

Command

Description

dnis

Adds a DNIS number to a DNIS map.

dnis-map

Associates a DNIS map with a dial peer.

show voice dnis-map

Displays configuration information about DNIS maps.

voice dnis-map

Enters DNIS map configuration mode to create a DNIS map.

## voice dsp crash-dump

To enable the crash dump feature and to specify the destination file and the file limit, enter the voice dsp crash-dump command in global configuration mode. To disable the feature, use the no form of the command.

voice dsp crash-dump [ destination url | file-limit limit-number ]

no voice dsp crash-dump

### Syntax Description

destination url

Designates a valid file system where crash dump analysis is stored. The url argument must be set to a valid file system.

The destination url can be one of the following

The file on a TFTP server with the following format:
                                                tftp://x.x.x.x/subfolder/filename.

The x.x.x.x value is the IP address of the TFTP server

The file on the flashcard of the router, with the following format: slot0:filename

The digital signal processor (DSP) crash dump feature is disabled when either the crash-dump destination is not specified.

file-limit limit-number

The crash dump file-limit keyword must be set to a non-zero value. The default is that the crash dump capability is turned
                                          off, as the url argument is empty, and the file-number argument is zero.

The limit-number argument may range from 0 (no file will be written) to 99.

The DSP crash dump feature is disabled when the crash-dump file limit is set to 0.

### Command Default

Crash dump capability is turned off.

### Command Modes

Global configuration

## Command History

Release

Modification

12.3(4)T

This command was introduced.

### Usage Guidelines

To configure the router to write a crash dump file, the destination url in the voice dsp crash-dump command must be set to a valid file system, and the crash dump file limit must be set to a non-zero value. The default is
                              that the crash dump capability is turned off, as the url field is empty, and the file limit is zero.

As each crash-dump file is created, the name of the file has a number appended to the end. This number is incremented from
                              1 to up to the file limit for each subsequent crash dump file written. If the router reloads, the number is reset back to
                              1, and so file number 1 is written again. After the file number reaches the maximum file limit, no more files are written.

The file count can be manually reset by setting the file limit to zero and then setting it to a non-zero limit. This has the
                              effect of restarting the count of files written, causing the files 1 to the file limit of 99 to be able to be written again,
                              thus overwriting the original files.

Setting the file-number argument to zero (the default) disables the collection of the dump from the DSP. In this case, the
                              memory is not collected from the DSP, and the stack is not displayed on the console. If the keepalive mechanism detects a
                              crashed DSP, the DSP is simply restarted.

Setting the file-number argument to a non-zero number but having a null destination url causes the dump to be collected and
                              the stack to be displayed on the console, but no dump file is written.

If auto-recovery is turned off for the router, no DSP dump functions are enabled, no keepalive checks are done, and no dumps
                              are collected or written.

Some types of flash need to be completely erased to free up space from deleted files, and some types of flash cannot have
                                          files overwritten with new versions until the entire flash is erased. As a result, you might want to set the file limit so
                                          that only one or two dump files are written to flash. This prevents flash from being filled up.

It is not recommended to write crash dump files to internal flash or bootflash, because these files are normally used to hold
                                          configuration information and Cisco IOS software images. Cisco recommends writing crash dump files to spare flash cards, which
                                          can be inserted into slot 0 or slot 1 on many of the routers. These cards usually do not hold critical information and may
                                          be erased. Additionally, these cards can be conveniently removed from the router and sent to Cisco, so that the crash dump
                                          files can be analyzed.

## Examples

The following example enables the crash dump feature and specifies the destination file in slot 0:

```
Router configure terminal 
Enter configuration commands, one per line.  End with CNTL/Z. 
Router(config)# voice dsp crash-dump destination slot0:banjo-152-s 
Router# end 
1w0d:%SYS-5-CONFIG_I:Configured from console by console
```

Check your configuration by entering the show voice dsp crash-dump command in privileged EXEC configuration mode:

```
Router# show voice dsp crash-dump 
Voice DSP Crash-dump status:
    Destination file url is slot0:banjo-152-s 
File limit is 20 
    Last DSP dump file written was 
          tftp://112.29.248.12/tester/26-152-t2 
    Next DSP dump file written will be slot0:banjo-152-s1
```

### Related Commands

Command

Description

debug voice dsp crash-dump

Displays crash dump debug information.

show voice dsp crash-dump

Displays voice dsp crash dump information.

## voice dsp invalid-msg drop

To drop the invalid Digital Signal Processor (DSP) messages, use the voice dsp invalid-msg drop command in global configuration mode. To disable this feature, use the no form of the command.

voice dsp invalid-msg drop

no voice dsp invalid-msg drop

### Command Default

Invalid DSP messages are not dropped.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

IOS XE Fuji Release 16.8.1

This command was introduced.

### Usage Guidelines

The Voice DSP Control Message Logger feature enables debugging of the logged control messages to examine voice- related problems.
                              Use the voice dsp invalid-msg drop command to drop the messages that are invalid.

## Examples

The following example drops the invalid DSP messages.

```
Router# voice dsp invalid-msg drop
```

## voice echo-canceller extended

To enable the extended G.168 echo canceller (EC) on the Cisco 1700 series, Cisco ICS7750, or Cisco AS5300, use the voice echo-canceller extended command in global configuration mode. To reset to the default, use the no form of this command.

### Cisco 1700 series and Cisco ICS 7750

voice echo-canceller extended

no voice echo-canceller extended

### Cisco AS5300

voice echo-canceller extended [ codec small codec large codec ]

no voice echo-canceller extended

### Syntax Description

codec

(Optional) Defines restricted codecs, both small and large.

small codec

Small footprint codec. Valid values for the codec argument are:

g711

g726

large codec

Large footprint codec. Valid values for the codec argument are:

fax-relay

g723

g728

g729

gsmefr

gsmfr

### Command Default

Proprietary Cisco G.165 EC is enabled.

### Command Modes

Global configuration

## Command History

Release

Modification

12.2(13)T

This command was introduced.

12.3(3)

This command was modified to allow unrestricted codecs on the Cisco AS5300. The codec keyword was made optional.

### Usage Guidelines

Cisco 1700 series and Cisco ICS7750

You do not have to shut down all the voice ports on the Cisco 1700 series or Cisco ICS7750 to switch the echo canceller, but
                              you should make sure that when you switch the echo canceller, there are no active calls on the router.

Because echo cancellation is an invasive process that can minimally degrade voice quality, you should disable this command
                              if it is not needed.

Cisco AS5300

This command is available only on the Cisco AS5300 with C542 or C549 digital signal processor module (DSPM) high-complexity
                              firmware.

The voice echo-canceller extended command enables the extended EC on a Cisco AS5300 using C549 DSP firmware with one channel of voice per DSP and unrestricted
                              codecs. Any codec is supported.

The voice echo-canceller extended codec command enables the extended EC on a Cisco AS5300 using C542 or C549 DSP firmware with two channels of voice per DSP and
                              restricted codecs. Only specific codecs can be used with the extended EC.

If fax-relay is not selected as the large codec, the VoIP dial peer requires that you use the 
                              fax rate disabled command in dial-peer configuration mode.

After choosing the codecs to be supported by the extended echo canceller, either remove all dial peers with different codecs
                              not supported by your new configuration or modify the dial-peer codec selection by selecting a voice codec or fax-relay. When
                              codecs are restricted, only one selection is allowed. You must have a VoIP dial peer configured with an extended EC-compatible
                              codec to ensure voice quality on the connection.

This command is not accepted if there are active calls. If the EC is already in effect and a codec choice is changed, the
                              system scans the dial peers. Any dial peers that do not conform to the new global command settings are changed, and the user
                              is informed of the changes. Similarly, modem relay is incompatible with the extended EC and must be disabled globally for
                              all dial peers.

This command is valid only when the echo-cancel enable command and the 
                                          echo-cancel coverage command are enabled.

## Examples

The following example sets the extended G.168 EC on the Cisco 1700 series or Cisco ICS7750:

```
Router(config)# voice echo-canceller extended
```

The following example sets the extended G.168 EC on the Cisco AS5300 with restricted codecs:

```
Router(config)# voice echo-canceller extended codec small g711 large g726
```

The following example shows an error message that displays when a restricted codec is not allowed:

```
Cannot configure now, dial-peer 8800 is configured with codec=g728, fax rate=disable, modem=passthrough system.If necessary set this command to 'no', re-configure dial-peer codec, fax rate and/or modem. Then re-enter this command.
```

In the above example, dial peer 8800 is misconfigured with a codec type, g728, that was not selected for the large codec type
                              using the voice echo-canceller extended command.

### Related Commands

Command

Description

echo-cancel coverage

Enables the cancellation of voice that is sent out the interface and is received on the same interface.

echo-cancel enable

Enables the cancellation of voice that is sent and received on the same interface.

## voice enum-match-table

To create an ENUM match table for voice calls, use the voice enum-match-table in global configuration mode. To delete the ENUM match table, use the no form of this command.

voice enum-match-table table-number

no voice enum-match-table table-number

### Syntax Description

table-number

Number of the ENUM match table. Range is from 1 to 15. There is no default value.

### Command Default

No default behavior or values

### Command Modes

Global configuration

## Command History

Release

Modification

12.2(11)T

This command was introduced.

### Usage Guidelines

The ENUM match table is a set of rules for matching incoming calls. When a call comes in, its called number is matched against
                              the match pattern of the rule with the highest preference.

If it matches, the replacement pattern is applied to the number. The resulting number and the domain name of the rule are
                              used to make an ENUM query.

If the called number does not match the match pattern, the next rule in order of preference is selected.

## Examples

The following example creates ENUM match table 3 for voice calls:

```
Router(config)# voice enum-match-table 3 Router(config-enum)# rule 1 5/(.*)/ /\1/e164.cisco.com Router(config-enum)# rule 2 4/^9011\(.*\)/ /\1/e164.arpa
```

In this table, rule 1 matches any number. The resulting number is the same as the called number. That number and the domain
                              name "e164.cisco.com" are used to make an ENUM query.

Rule 2 matches any number that starts with 9011. The 9011 is removed from the incoming number. The resulting number and the
                              domain name "e164.arpa" are used for the ENUM query.

Suppose an incoming call has a called number of 4085550112. [Rule 2 is applied] first because it has a higher preference.
                              The first few digits, 4085, do not match the 9011 pattern of rule 2, so [rule 1 is applied] next. The called number matches
                              rule 1, and the resulting number is 4085550112. This number and "e164.cisco.com" form the ENUM query (2.1.2.1.5.5.5.8.0.4.e164.cisco.com).

### Related Commands

Command

Description

rule (ENUM configuration)

Defines the matching, replacement, and rejection patterns for an ENUM match table.

show voice enum-match-table

Displays the configuration of voice ENUM match tables.

test enum

Tests the functionality of an ENUM match table.

## voice hpi capture

To allocate the Host Port Interface (HPI) capture buffer size (in bytes) and to set up or change the destination URL for captured
                              data, use the voice hpi capture command in global configuration mode. To stop all logging and file operations, to disable data transport from the capture
                              buffer, and to automatically set the buffer size to 328, use the no form of this command.

voice hpi capture [ buffer size | destination url ]

no voice hpi capture buffer size

### Syntax Description

buffer size

(Optional) Size of HPI capture buffer, in bytes. Range is from 328 to 9000000. The default is 328.

destination url

(Optional) Destination URL for storing captured data.

### Command Default

328 bytes (no buffer is used if it is not configured explicitly)

### Command Modes

Global configuration

## Command History

Release

Modification

12.2(10)

This command was introduced.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T.

### Usage Guidelines

If you want to change the size of an existing non-zero buffer, you must first reset it to 0 and then change it from 0 to the
                              new size.

The destination url option sets up or changes the destination URL for captured data. To disable data transport from the capture buffer, use the no form of the command. If the buffer is allocated, captured data is sent to the current URL (if it was already configured)
                              until the new URL is specified.

If a new URL differs from the current URL and logging is enabled, the current URL is closed and all further data is sent to
                              the new URL. Entering a blank URL or prefixing the command with no disables data transport from the capture buffer, and (if capture is enabled) captured data is stored in the capture buffer
                              until it reaches its capacity.

Once the buffer-queueing program is running, the transport process attempts to connect to a new or existing "capture destination"
                              URL. A version message is written to the URL, and if the message is successfully received, any further messages placed into
                              the message queue are written to that URL. If a new URL is entered using the voice hpi capture destination url command, the
                              open URL is closed, and the system attempts to write to the new URL. If the new URL does not work, the transport process exits.
                              The transport process is restarted when another URL is entered or the system is restarted.

The buffer size option sets the maximum amount of memory (in bytes) that the capture system allocates for its buffers when
                              it is active. The capture buffer is where the captured messages are stored before they are sent to the URL specified by the
                              capture destination. The system is started by choosing the amount of memory (greater than 0 bytes) that the buffer-queueing
                              system can allocate to the free message pool. HPI messages can then be captured until buffer capacity is reached. Entering 0 for the buffer size and prefixing the command with no stops all logging and file operations and automatically sets the buffer size to 0.

The voice hpi capture command can be saved with the router configuration so that the command is active during router startup. This allows you to
                              capture the HPI messages sent during router bootup before the CLI is enabled. After you have configured the buffer size in
                              the running configuration (valid range is from 328 to 9000000), save it to the startup configuration using the write command or to the TFTP server using the copy run tftp command.

Caution

Using the message logger feature in a production network environment impacts CPU and memory usage on the gateway.

## Examples

The following example changes the size (in bytes) of the HPI capture buffer and initializes the buffer-queueing program:

```
Router# configure terminal Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)# voice hpi capture buffer 40000 Router(config)# end Router#
03:23:31:caplog:caplog_cli_interface:hpi capture buffer size set to 40000 bytes
03:23:31:caplog:caplog_logger_init:TRUE, Started task HPI Logger (PID 64)
03:23:31:caplog:caplog_cache_init:TRUE, malloc_named(39852), 123 elements (each 324 bytes big)
03:23:31:caplog:caplog_logger_proc:Attempting to open ftp://172.23.184.233/c:b-38-117
03:23:32:%SYS-5-CONFIG_I:Configured from console by console
Router#
```

The following example sets the capture destination by entering a destination URL using FTP:

```
Router# configure terminal Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)# voice hpi capture destination ftp://172.23.184.233/c:b-38-117a Router(config)#   
04:05:10:caplog:caplog_cli_interface:hpi capture destination:ftp://172.23.184.233/c:b-38-117a
04:05:10:caplog:caplog_logger_init:TRUE, Started task HPI Logger (PID 19)
04:05:10:caplog:caplog_cache_init:Cache must be at least 324 bytes
04:05:10:caplog:caplog_logger_proc:Terminating...
Router(config)# end Router#
```

### Related Commands

Command

Description

debug hpi

Turns on the debug output for the logger.

show voice hpi capture

Displays the capture status and statistics.

## voice hunt

To configure an originating or tandem router so that it continues dial-peer hunting if it receives a specified disconnect
                              cause code from a destination router, use the voice hunt command in global configuration mode. To configure the router so that it stops dial-peer hunting if it receives a specified
                              disconnect cause code (the default condition), use the no form of this command. To restore the default dial-peer hunt setting, use the default form of this command.

voice hunt { disconnect-cause-code | all }

no voice hunt { disconnect-cause-code | all }

default voice hunt

### Syntax Description

disconnect-cause-code

A code returned from the destination router to indicate why an attempted end-to-end call was unsuccessful. If the specified
                                          disconnect cause code is returned from the last destination endpoint, dial peer hunting is enabled or disabled. The table
                                          below in the "Usage Guidelines" section describes the possible values. You can enter the keyword, decimal value, or hexadecimal
                                          value.

all

Continue dial-peer hunting for all disconnect cause codes returned from the destination endpoint.

default

Restores the default dial-peer hunt setting, that is, the router stops dial-peer hunting if it receives the user-busy or
                                          no-answer disconnect cause code.

### Command Default

The router stops dial-peer hunting if it receives the user-busy or no-answer disconnect cause code.

### Command Modes

Global configuration

## Command History

Release

Modification

12.0(5)T

This command was introduced for VoFR on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. It was also introduced
                                          for VoIP on the Cisco 2600 series and Cisco 3600 series.

12.0(7)T

This command was implemented for VoIP on the Cisco AS5300 and Cisco AS5800.

12.0(7)XK

This command was implemented for VoIP on the Cisco MC3810.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T and implemented for VoIP on the Cisco MC3810.

12.1(3)XI

The invalid-number and unassigned-number keywords were added, and the command name was changed to voice hunt .

12.1(5)T

This command was integrated into Cisco IOS Release 12.1(5)T.

12.2(4)T

Keywords were added for more disconnect cause codes.

12.3(8)T

The disconnect-cause-code argument was modified to accept nonstandard disconnect cause codes.

### Usage Guidelines

This command is used with routers that act as originating or tandem nodes in a VoIP, VoFR, or Voice over ATM environment.

For an outgoing call from an originating VoIP gateway configured for rotary dial-peer hunting, more than one dial peer may
                              match the same destination number. The matching dial peers may have different routes. After the voice call using the first
                              dial peer gets disconnected, it will return a disconnect cause code. To have the router to pick up the next matching dial
                              peer in the rotary group and set up a call, the router must be configure to continue hunting the various routes. Use this
                              command to configure the router’s hunting behavior when specified cause codes are received.

You can use this command to enable and disable dial-peer hunting when nonstandard disconnect cause codes are received. Nonstandard
                              disconnect cause codes are those that are not defined in ITU-T Recommendation Q.931, but are used by service providers. When
                              this command is used to disable dial-peer hunting for a specific disconnect cause code, it appears in the running configuration
                              of the router.

The disconnect cause codes are described in the table below. The decimal and hexadecimal value of the disconnect cause code
                              follows the description of each possible keyword.

While configuring voice hunt , it is necessary to configure reason header override in the sip-ua configuration mode to ensure that correct cause codes are sent to the other leg. For more information on reason header override configuration, see reason-header override command.

Keyword

Description

Decimal

Hex

access-info-discard

Access information discarded.

43

0x2b

all

Continue dial-peer hunting for all disconnect cause codes received from a destination router.

b-cap-not-implemented

Bearer capability not implemented.

65

0x41

b-cap-restrict

Restricted digital information bearer capability only.

70

0x46

b-cap-unauthorized

Bearer capability not authorized.

57

0x39

b-cap-unavail

Bearer capability not available.

58

0x3a

call-awarded

Call awarded.

7

0x7

call-cid-in-use

Call exists, call ID in use.

83

0x53

call-clear

Call cleared.

86

0x56

call-reject

Call rejected.

21

0x15

cell-rate-unavail

Cell rate not available.

37

0x25

channel-unacceptable

Channel unacceptable.

6

0x6

chantype-not-implement

Channel type not implemented.

66

0x42

cid-in-use

Call ID in use.

84

0x54

codec-incompatible

Codec incompatible.

171

0xab

cug-incalls-bar

Closed user group (CUG) incoming calls barred.

55

0x37

cug-outcalls-bar

CUG outgoing calls barred.

53

0x35

dest-incompatible

Destination incompatible.

88

0x58

dest-out-of-order

Destination out of order.

27

0x1b

dest-unroutable

No route to destination.

3

0x3

dsp-error

Digital signal processor (DSP) error.

172

0xac

dtl-trans-not-node-id

Designated transit list (DTL) transit not my node ID.

160

0xa0

facility-not-implemented

Facility not implemented.

69

0x45

facility-not-subscribed

Facility not subscribed.

50

0x32

facility-reject

Facility rejected.

29

0x1d

glare

Glare.

15

0xf

glaring-switch-pri

Glaring switch PRI.

180

0xb4

htspm-oos

Holst Telephony Service Provider Module (HTSPM) out of service.

129

0x81

ie-missing

Mandatory information element missing.

96

0x60

ie-not-implemented

Information element not implemented.

99

0x63

info-class-inconsistent

Inconsistency in information and class.

62

0x3e

interworking

Interworking.

127

0x7f

invalid-call-ref

Invalid call reference value.

81

0x51

invalid-ie

Invalid information element contents.

100

0x64

invalid-msg

Invalid message.

95

0x5f

invalid-number

Invalid number.

28

0x1c

invalid-transit-net

Invalid transit network.

91

0x5b

misdialled-trunk-prefix

Misdialed trunk prefix.

5

0x5

msg-incomp-call-state

Message in incomplete call state.

101

0x65

msg-not-implemented

Message type not implemented.

97

0x61

msgtype-incompatible

Message type not compatible.

98

0x62

net-out-of-order

Network out of order.

38

0x26

next-node-unreachable

Next node unreachable.

128

0x80

no-answer

No user answer.

19

0x13

no-call-suspend

No call suspended.

85

0x55

no-channel

Channel does not exist.

82

0x52

no-circuit

No circuit.

34

0x22

no-cug

Nonexistent CUG.

90

0x5a

no-dsp-channel

No DSP channel.

170

0xaa

no-req-circuit

No requested circuit.

44

0x2c

no-resource

No resource.

47

0x2f

no-response

No user response.

18

0x12

no-voice-resources

No voice resources available.

126

0x7e

non-select-user-clear

Nonselected user clearing.

26

0x1a

normal-call-clear

Normal call clearing.

16

0x10

normal-unspecified

Normal, unspecified.

31

0x1f

not-in-cug

User not in CUG.

87

0x57

number-changeed

Number changed.

22

0x16

param-not-implemented

Nonimplemented parameter passed on.

103

0x67

perm-frame-mode-oos

Permanent frame mode out of service.

39

0x27

perm-frame-mode-oper

Permanent frame mode operational.

40

0x28

precedence-call-block

Precedence call blocked.

46

0x2e

preempt

Preemption.

8

0x8

preempt-reserved

Preemption reserved.

9

0x9

protocol-error

Protocol error.

111

0x6f

qos-unavail

QoS unavailable.

49

0x31

rec-timer-exp

Recovery on timer expiry.

102

0x66

redirect-to-new-destination

Redirect to new destination.

23

0x17

req-vpci-vci-unavail

Requested VPCI VCI not available.

35

0x23

send-infotone

Send information tone.

4

0x4

serv-not-implemented

Service not implemented.

79

0x4f

serv/opt-unavail-unspecified

Service or option not available, unspecified.

63

0x3f

stat-enquiry-resp

Response to status enquiry.

30

0x1e

subscriber-absent

Subscriber absent.

20

0x14

switch-congestion

Switch congestion.

42

0x2a

temp-fail

Temporary failure.

41

0x29

transit-net-unroutable

No route to transit network.

2

0x2

unassigned-number

Unassigned number.

1

0x1

unknown-param-msg-discard

Unrecognized parameter message discarded.

110

0x6e

unsupported-aal-parms

ATM adaptation layer (AAL) parameters not supported.

93

0x5d

user-busy

User busy.

17

0x11

vpci-vci-assign-fail

Virtual path connection identifier virtual channel identifier (VPCI VCI) assignment failure.

36

0x24

vpci-vci-unavail

No VPCI VCI available.

45

0x2d

## Examples

The following example configures the originating or tandem router to continue dial-peer hunting if it receives a user-busy
                              disconnect cause code from a destination router:

```
voice hunt user-busy
```

The following example configures the originating or tandem router to continue dial-peer hunting if it receives an invalid-number
                              disconnect cause code from a destination router:

```
voice hunt 28
```

The following example configures the originating or tandem router to continue dial-peer hunting if it receives a facility-not-subscribed
                              disconnect cause code from a destination router:

```
voice hunt 0x32
```

### Related Commands

Command

Description

huntstop

Disables all further dial-peer hunting if a call fails when using hunt groups.

preference

Indicates the preferred order of a dial peer within a rotary hunt group.

## voice iec syslog

To enable viewing of Internal Error Codes as they are encountered in real time, use the voice iec syslog command in global
                              configuration mode. To disable IEC syslog messages, use the no form of this command.

voice iec syslog

no voice iec syslog

### Syntax Description

This command has no arguments or keywords.

### Command Default

IEC syslog messages are disabled.

### Command Modes

Global configuration

## Command History

Release

Modification

12.3(4)T

This command was introduced.

Introduced support for YANG models.

## Examples

The following example enables IEC syslog messages:

```
Router(config)# voice iec syslog
```

### Related Commands

Command

Description

clear voice statistics

Clears voice statistics, resetting the statistics collection.

show voice statistics iec

Displays iec statistics

show voice statistics interval-tag

Displays interval options available for IEC statistics

voice statistics type iec

Enables collection of IEC statistics

## voice local-bypass

To configure local calls to bypass the digital signal processor (DSP), use the voice local-bypass command in global configuration mode. To direct local calls through the DSP, use the no form of this command.

voice local-bypass

no voice local-bypass

### Syntax Description

This command has no arguments or keywords.

### Command Default

Local calls bypass the DSP.

### Command Modes

Global configuration

## Command History

Release

Modification

11.3(1)MA

This command was introduced.

12.0(7)XK

This command was implemented on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T.

### Usage Guidelines

Local calls (calls between voice ports on a router or concentrator) normally bypass the DSP to minimize use of system resources.
                              Use the no form of the voice local-bypass command if you need to direct local calls through the DSP. Input gain and output attenuation can be configured only if calls
                              are directed through the DSP.

## Examples

The following example configures a Cisco router to pass local calls through the DSP:

```
no voice local-bypass
```

### Related Commands

Command

Description

input gain

Configures a specific input gain value.

output attenuation

Configures a specific output attenuation value.

## voice mlpp

To enter MLPP configuration mode to enable MLPP service, use the voice service command in global configuration mode. To disable
                              MLPP service, use the no form of this command.

voice mlpp

no voice mlpp

### Syntax Description

This command has no keywords or arguments.

### Command Default

No default behavior or values.

### Command Modes

G lobal configuration (config)

## Command History

Cisco IOS Release

Cisco Products

Modification

12.4(22)YB

Cisco Unified CME 7.1

This command was introduced.

12.4(24)T

Cisco Unified CME 7.1

This command was integrated into Cisco IOS Release 12.4(24)T.

Voice-mlpp configuration mode is used for the gateway globally.

## Examples

The following example shows how to enter voice-mlpp configuration mode:

```
Router(config)# voice mlpp Router(config-voice-mlpp)# access-digit
```

### Related Commands

Command

Description

access-digit

Defines the access digit that phone users dial to request a precedence call.

mlpp preemption

Enables calls on an SCCP phone or analog FXS port to be preempted.

preemption trunkgroup

Enables preemption capabilities on a trunk group.

## voicemail (stcapp-fsd)

To designate an SCCP telephony control (STC) application feature speed-dial code to speed dial the voice-mail number, use
                              the voicemail command in STC application feature speed-dial configuration mode. To return the code to its default, use the no form of this command.

voicemail keypad-character

no voicemail

### Syntax Description

keypad-character

One or two digits that can be dialed on a telephone keypad. Range is 0 to 9 for one-digit codes; 00 to 99 for two-digit codes.
                                          Default is 0 (zero) for one-digit codes; 00 (two zeroes) for two-digit codes.

Number of digits depends on the value set with the digit command.

### Command Default

The default voice-mail code is 0 (zero) for one-digit codes; 00 (two zeros) for two-digit codes.

### Command Modes

STC application feature speed-dial configuration

## Command History

Release

Modification

12.4(2)T

This command was introduced.

12.4(6)T

The keypad-character argument was modified to allow two-digit codes.

### Usage Guidelines

This command is used with the STC application, which enables certain features on analog FXS endpoints that use Skinny Client
                              Control Protocol (SCCP) for call control.

To use the speed-dial to voice-mail feature on a phone, dial the feature speed-dial (FSD) prefix and the code that has been
                              configured with this command (or the default if this command was not used). For example, if the FSD prefix is * (the default),
                              and you want to dial the voice-mail phone number, dial *0.

Note that the number that will be speed-dialed for voice mail must be set on Cisco CallManager or the Cisco CallManager Express
                              system.

This command is reset to its default value if you modify the value of the digit command. For example, if you set the digit command to 2, then change the digit command back to its default of 1, the voice-mail FSD code is reset to 0 (zero).

If you set this code to a value that is already in use for another FSD code, you receive a warning message. If you configure
                              a duplicate code, the system implements the first matching feature in the order of precedence shown in the output of the show stcapp feature codes command.

The show running-config command displays nondefault FSD codes only. The show stcapp feature codes command displays all FSD codes.

## Examples

The following example sets an FSD prefix of two pound signs (##) and a voice-mail code of 8. After these values have been
                              configured, a phone user presses ##8 to dial the voice-mail number.

```
Router(config)# stcapp feature speed-dial Router(stcapp-fsd)# prefix ## Router(stcapp-fsd)# voicemail 8 Router(stcapp-fsd)# exit
```

### Related Commands

Command

Description

digit

Designates the number of digits for STC application feature speed-dial codes.

prefix (stcapp-fsd)

Designates a prefix to precede the dialing of an STC application feature speed-dial code.

redial

Designates an STC application feature speed-dial code to dial again the last number that was dialed.

show running-config

Displays current nondefault configuration settings.

show stcapp feature codes

Displays configured and default STC application feature codes.

speed dial

Designates a range of STC application feature speed-dial codes.

stcapp feature speed-dial

Enters STC application feature speed-dial configuration mode to set feature speed-dial codes.

## voice pcm capture

To allocate the number of Pulse Code Modulation (PCM) capture buffers, to set up or change the destination URL for captured
                              data, to enable PCM capture on-demand, and to change the PCM capture trigger string by the user, use the voice pcm capture command in global configuration mode. To stop all logging and file operations, to disable data transport from the capture
                              buffer, and to automatically set the number of buffers to 0, use the no form of this command.

voice pcm capture { buffer number | destination url | on-demand-trigger | user-trigger-string start-string stop-string stream bitmap duration call-duration }

no voice pcm capture { buffer number | destination url | on-demand-trigger | user-trigger-string }

### Syntax Description

buffer number

Allocates the number of PCM capture buffers. The range is from 0 to 200000. The default is 0.

destination url

Specifies the destination URL for storing captured data.

on-demand-trigger

(Optional) Configures PCM capture user trigger on-demand.

user-trigger-string start-string stop-string stream bitmap duration call-duration

(Optional) Configures PCM user trigger string.

start-string —Start string up to 15 characters.

stop-string —Stop string up to 15 characters.

stream —Configures the PCM capture stream bitmap.

bitmap —PCM stream bitmap in hexadecimal. The range is from 1 to FFFFFFF. The default is 7.

duration —Configures the duration for PCM capture.

call-duration —Duration of call. The range is from 0 to 255. The default is 0.

### Command Default

The default values are as follows:

Number of buffers: 0

Start string: 123

Stop string: 456

Stream: 7

Call duration: 0

### Command Modes

Global configuration (config)

## Command History

Release

Modification

15.2(2)T

This command was introduced.

### Usage Guidelines

If you want to change the number of an existing nonzero buffer, you must first reset it to 0 and then change it from 0 to
                              the new number.

The destination url option sets up or changes the destination URL for captured data. To disable data transport from the capture buffer, use the no form of this command. If the buffer is allocated, captured data is sent to the current URL (if it was already configured)
                              until the new URL is specified.

If a new URL differs from the current URL and logging is enabled, the current URL is closed and all further data is sent to
                              the new URL. Entering a blank URL or prefixing the command with no disables data transport from the capture buffer, and (if capture is enabled) captured data is stored in the capture buffer
                              until it reaches its capacity.

Once the buffer-queueing program is running, the transport process attempts to connect to a new or existing “capture destination”
                              URL. A version message is written to the URL, and if the message is successfully received, any further messages placed into
                              the message queue are written to that URL. If a new URL is entered using the voice pcm capture destination url command, the open URL is closed, and the system attempts to write to the new URL. If the new URL does not work, the transport
                              process exits. The transport process is restarted when another URL is entered or the system is restarted.

## Examples

The following example shows how to configure the number of PCM capture buffers:

```
Router> enable Router# configure terminal Router(config)# voice pcm capture buffer 200
```

The following example shows how to configure the destination URL for storing captured data:

```
Router> enable Router# configure terminal Router(config)# voice pcm capture destination tftp://10.0.1.10/acphan/
```

The following example shows how to configure user trigger PCM capture:

```
Router> enable Router# configure terminal Router(config)# voice pcm capture on-demand-trigger
```

The following example shows how to change the default user trigger PCM capture start and stop string, stream, and call duration:

```
Router> enable Router# configure terminal Router(config)# voice pcm capture #132 #543 stream ff duration 230
```

### Related Commands

Command

Description

show voice pcm capture

Displays PCM capture status and statistics.

## voice-phone-proxy

To create a voice phone proxy instance  and to enter phone-proxy configuration mode,  use the voice-phone-proxy command in global configuration mode. To remove a  voice phone proxy instance use the no form of the command.

voice-phone-proxy pp-name

no voice-phone-proxy pp-name

## Syntax Description

The phone proxy instance name.

### Command Default

none

### Command Modes

Global configuration mode (config)

## Command History

15.3(3)M

This command was introduced.

### Usage Guidelines

The voice-phone-proxy command allows you to create an instance of a voice phone proxy. In phone-proxy configuration mode you can specify settings
                              such as the service and server settings for the phone proxy instance.

## Examples

The following example shows how to create a phone proxy instance called first-pp, enter phone-proxy configuration mode, set
                              the description for this instance, and specify a  Certificate Trust List (CTL) file for this cluster:

```
Device(config)# voice-phone-proxy first-pp
Device(config-phone-proxy)# description cluster-test
Device(config-phone-proxy)# ctl-file my-cluster-test-ctl-file
```

## voice-phone-proxy file-buffer

To create the phone proxy buffer files, use the voice-phone-proxy file-buffer command in global configuration mode.

voice-phone-proxy file-buffer size size aging time

### Syntax Description

Buffer size in MB. The range is from 10 to 60.

Checks the age of the phone proxy buffer files.

time

Time in seconds. The range is from 10 to 3600. Based on the set time, the file buffer will be periodically checked.

### Command Default

No default phone proxy exists.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

IOS XE Fuji Release 16.8.1

This command was introduced.

### Usage Guidelines

The maximum buffer size that can be allocated for the phone proxy buffer files is 60 MB. If the buffer size exceeds the threshold
                              value, new phone proxy buffer files cannot be created. To remove the old buffer files, use the command voice-phone-proxy file-buffer size size aging time . Based on the set time, the buffer will be checked at regular intervals and the old phone proxy buffer files will be removed
                              if the buffer size exceeds the maximum limit.

## Examples

The following example sets the file buffer size as 30 MB and checks the file buffer at an interval of 100 seconds.

```
Router (config)# voice-phone-proxy file-buffer size 30 aging 100
```

## voice-phone-proxy tftp-address

To  specify the IP address and VRF name of the TFTP server and to enter phone-proxy configuration mode, use the voice-phone-proxy tftp-address command in global configuration mode. To remove the IP address and VRF name of the TFTP server, use the no form of the command.

voice-phone-proxy tftp-address { ipv4 ipv4-address | ipv6 ipv6-address } [ vrf vrf-name ]

no voice-phone-proxy tftp-address { ipv4 ipv4-address | ipv6 ipv6-address } [ vrf vrf-name ]

## Syntax Description

IPv4 address of the TFTP server.

IPv6 address of the TFTP server.

Name of the TFTP server’s VRF.

### Command Default

No IP address or  VRF name of the TFTP server is specified.

### Command Modes

Global configuration mode (config)

## Command History

15.3(3)M

This command was introduced.

IOS XE Fuji Release 16.8.1

This command was enhanced to add the ipv6 keyword.

## Examples

The following example shows how to specify the IP address and VRF of the TFTP server:

```
Device(config)# phone-proxy tftp-address ipv4 198.51.100.1 vrf vrf1
```

## voiceport

To enable a private line automatic ringdown (PLAR) connection for an analog phone, use the voiceport command in SCCP PLAR configuration mode. To remove PLAR from the voice port, use the no form of this command.

voiceport port-number dial dial-string [ digit dtmf-digits [ wait-connect wait-msecs ] [ interval inter-digit-msecs ]]

no voiceport port-number

### Syntax Description

port-number

Analog foreign exchange station (FXS) voice port number. Range: 2/0 to 2/23.

dial dial-string

String of up to 16 characters that can be dialed on a telephone keypad. Valid characters are 0 through 9, A through D, an
                                          * (asterisk) and # (pound sign). The voice gateway sends this string to the call-control system when the analog phone goes
                                          off hook.

digit dtmf-digits

(Optional) String of up to 16 characters that can be dialed on a telephone keypad. Valid characters are 0 through 9, A through
                                          D, an * (asterisk), # (pound sign), and comma (,). The voice gateway sends this string to the call-control system after the wait-msecs expires. Each comma represents a one second wait.

wait-connect wait-msecs

(Optional) Number of milliseconds that the voice gateway waits after voice cut-through before out-pulsing the DTMF digits.
                                          Range: 0 to 30000, in multiples of 50. Default: 50. If 0, DTMF digits are sent automatically by voice gateway after call is
                                          connected.

interval inter-digit-msecs

(Optional) Number of milliseconds between the DTMF digits. Range: 50 to 500, in multiples of 50. Default: 50.

### Command Default

Disabled (PLAR is not set for the voice port).

### Command Modes

SCCP PLAR configuration

## Command History

Release

Modification

12.4(6)T

This command was introduced.

### Usage Guidelines

This command enables PLAR on analog FXS ports that use Skinny Client Control Protocol (SCCP) for call control. If the digit keyword is not used, DTMF digits are not out-pulsed; the voice port uses a simple PLAR connection and the other keywords
                              are not available.

Voice ports can be configured in any order. For example, you can configure port 2/23 before port 2/0. The show running-config command lists the ports in ascending order.

Before a PLAR port can become operational, the STC application must first be enabled in the corresponding dial-peer using
                              the service stcapp command. If you configure a port for PLAR before enabling the STC application in the dial peer you receive a warning message.

PLAR phones support most of the same features as normal analog phones. The PLAR phone handles incoming calls and supports
                              hookflash for basic supplementary features such as call transfer, call waiting, and conference. The PLAR phone does not support
                              other features such as call forwarding, redial, speed dial, call park, call pick up from a PLAR phone, AMWI, or caller ID.

## Examples

The following example enables the PLAR feature on port 2/0, 2/1, and 2/3. When a phone user picks up the handset on the analog
                              phone connected to port 2/0, the system automatically rings extension 3660 and after waiting 500 milliseconds, dials 1234.
                              The DTMF digits are out-pulsed to the destination port at an interval of 200 milliseconds.

```
Router(config)# sccp plar Router(config-sccp-plar)# voiceport 2/0 dial 3660 digit 1234 wait-connect 500 interval 200 Router(config-sccp-plar)# voiceport 2/1 dial 3264 digit 678,,,9*0,,#123 interval 100 Router(config-sccp-plar)# voiceport 2/3 dial 3478 digit 34567 wait-connect 500
```

### Related Commands

Command

Description

dial-peer voice

Enters dial-peer configuration mode and defines a dial peer.

sccp plar

Enters SCCP PLAR configuration mode.

## voice-port

To enter voice-port configuration mode, use the voice-port command in global configuration mode.

### Cisco 1750 and Cisco 1751

voice-port slot-number / port

### Cisco 2600 series, Cisco 3600 Series, and Cisco 7200 Series

voice-port { slot-number / subunit-number / port | slot / port : ds0-group-no }

### Cisco 2600 and Cisco 3600 Series with a High-Density Analog Network Module (NM-HDA)

slot-number / subunit-number / port voice-port

### Cisco AS5300

voice-port controller-number :D

### Cisco 1750 and Cisco 1751

slot-number

Number of the slot in the router in which the voice interface card (VIC) is installed. Valid entries are from 0 to 2, depending
                                          on the slot in which it has been installed.

port

Voice port number. Valid entries are 0 and 1.

slot-number

Number of the slot in the router in which the VIC is installed. Valid entries are from 0 to 3, depending on the slot in which
                                          it has been installed.

subunit-number

Subunit on the VIC in which the voice port is located. Valid entries are 0 or 1.

port

Voice port number. Valid entries are 0 and 1.

slot

The router location in which the voice port adapter is installed. Valid entries are from 0 to 3.

port:

Indicates the voice interface card location. Valid entries are 0 and 3.

ds0-group-no

Indicates the defined DS0 group number. Each defined DS0 group number is represented on a separate voice port. This allows
                                          you to define individual DS0s on the digital T1/E1 card.

controller-number

T1 or E1 controller.

:D

D channel associated with ISDN PRI.

### Command Default

No default behavior or values

### Command Modes

Global configuration

## Command History

Release

Modification

11.3(1)T

This command was introduced.

11.3(3)T

This command was implemented on the Cisco 2600 series.

12.0(3)T

This command was implemented on the Cisco AS5300.

12.0(7)T

This command was implemented on the Cisco AS5800, Cisco 7200 series, and Cisco 1750. Arguments were added for the Cisco 2600
                                          series and Cisco 3600 series.

12.2(8)T

This command was implemented on Cisco 1751 and Cisco 1760. This command was modified to accommodate the additional ports
                                          of the NM-HDA on the Cisco 2600 series, Cisco 3640, and Cisco 3660.

12.2(2)XN

Support for enhanced MGCP voice gateway interoperability was added to Cisco CallManager Version 3.1 for the Cisco 2600 series,
                                          Cisco 3600 series, and Cisco VG200.

12.2(11)T

This command was integrated into the Cisco IOS Release 12.2(11)T and Cisco CallManager Version 3.2 and implemented on the
                                          Cisco IAD2420 series.

12.2(13)T

This command was integrated into Cisco IOS Release 12.2(13)T. This command does not support the extended echo canceller (EC)
                                          feature on the Cisco AS5300 or the Cisco AS5800.

### Usage Guidelines

Use the voice-port global configuration command to switch to voice-port configuration mode from global configuration mode. Use the exit command to exit voice-port configuration mode and return to global configuration mode.

This command does not support the extended echo canceller (EC) feature on the Cisco AS5300.

## Examples

The following example accesses voice-port configuration mode for port 0, located on subunit 0 on a VIC installed in slot
                              1:

```
voice-port 1/0/0
```

The following example accesses voice-port configuration mode for a Cisco AS5300:

```
voice-port 1:D
```

### Related Commands

Command

Description

dial-peer voice

Enters dial-peer configuration mode and specifies the method of voice encapsulation.

## voice-port (MGCP profile)

The voice-port (MGCP profile) command is replaced by the port (MGCP profile) 
                              command in Cisco IOS Release 12.2(8)T. See the port (MGCP profile)
                              command for more information.

## voice-port busyout

To place all voice ports associated with a serial or ATM interface into a busyout state, use the voice-port busyout command in interface configuration mode. To remove the busyout state on the voice ports associated with this interface, use the no form of this command.

voice-port busyout

no voice-port busyout

### Syntax Description

This command has no arguments or keywords.

### Command Default

The voice ports on the interface are not in busyout state.

### Command Modes

Interface configuration

## Command History

Release

Modification

12.0(3)T

This command was introduced on the Cisco MC3810.

### Usage Guidelines

This command busies out all voice ports associated with the interface, except any voice ports configured to busy out under
                              specific conditions using the busyout monitor and busyout seize commands.

## Examples

The following example places the voice ports associated with serial interface 1 into busyout state:

```
interface serial 1
 voice-port busyout
```

The following example places the voice ports associated with ATM interface 0 into busyout state:

```
interface atm 0
 voice-port busyout
```

### Related Commands

Command

Description

busyout forced

Forces a voice port into the busyout state.

busyout monitor

Places a voice port into the busyout monitor state.

busyout seize

Changes the busyout action for an FXO or FXS voice port.

show voice busyout

Displays information about the voice busyout state.

## voice rtp send-recv

To establish a two-way voice path when the Real-Time Transport Protocol (RTP) channel is opened, use the voice rtp send-recv command in global configuration mode. To reset to the default, use the no form of this command.

voice rtp send-recv

no voice rtp send-recv

### Syntax Description

This command has no arguments or keywords.

### Command Default

The voice path is cut-through in only the backward direction when the RTP channel is opened.

### Command Modes

Global configuration

## Command History

Release

Modification

12.1(5)T

This command was introduced on Cisco 2600 series, Cisco 3600 series, Cisco 7200 series, Cisco 7500 series, Cisco AS5300, Cisco
                                          AS5800, and Cisco MC3810 platforms.

12.2(2)XA

This command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(11)T

This command was integrated into the Cisco IOS Release 12.2(11)T.

### Usage Guidelines

This command should be enabled only when the voice path must be cut-through (established) in both the backward and forward
                              directions before a Connect message is received from the destination switch. This command affects all VoIP calls when it is
                              enabled.

## Examples

The following example enables the voice path to cut-through in both directions when the RTP channel is opened:

```
voice rtp send-recv
```

## voice rtp source-filter

To verify source of a Real-time Transport Protocol (RTP) or RTP Control Protocol (RTCP) stream while receiving the packets
                              for H.323, MGCP, SIP or SCCP protocols, use the voice rtp source-filter command. To disable filtering, use the no form of this command.

The voice rtp source-filter command is applicable only to ISR-G2 (3945e) routers.

voice rtp source-filter

no voice rtp source-filter

### Command Default

Voice RTP source filtering is enabled.

### Command Modes

Voice service voip configuration (conf-voi-serv)

## Command History

15.5(3)M9

15.6(3)M6

This command was introduced.

### Usage Guidelines

Public Switched Telephone Network (PSTN) callers may experience security risk when the IOS gateway receives an invalid RTP
                              stream destined to the same IP address and port of an active call. The invalid stream has a different source IP address and
                              port. The gateway mixes both the valid and invalid RTP streams and plays it to the PSTN caller. Use the voice rtp source-filter command when you want to filter RTP packets with a source IP address and port number that are different from the one negotiated
                              through VOIP signaling.

## Examples

The following example shows how to filter RTP packets:

```
Device> enable Device# configure terminal Device(config)# voice service voip Device(conf-voi-serv)# voice rtp source-filter
```

### Related Commands

Command

Description

voice service voip

Specifies the voice-encapsulation type and enters voice service configuration mode.

voice rtp send-recv

Establishes a two-way voice path when the Real-Time Transport Protocol (RTP) channel is opened.

## voice-service dsp-reservation

To specify the percentage of DSP resources that are reserved strictly for VOIP on the voice card, use the voice-service dsp-reservation command in voice-card configuration. To reset the percentage of DSP resources, use the no form of this command.

voice-service-dsp reservation percentage

no voice-service-dsp reservation percentage

### Syntax Description

percentage

Percentage of DSP resources on this voice card that are reserved for voice services. The remaining DSP resources will be available
                                          for video services.

### Command Default

The default voice reservation is 100%.

### Command Modes

voice-card configuration (config-voicecard)

## Command History

Release

Modification

15.1(4)M

The command was introduced.

### Usage Guidelines

Use this command to reserve a percentage of the voice card for voice services. The remaining DSP resources will be used for
                              video services. A reservation of 100% specified that all DSP resources will be used for voice services.

You can configure a percentage less than 100% only when there is a video license and the appropriate PVDM# modules are installed.

Tip

DSP can become fragmented when you change the percentage of DSP resources reserved for voice services when there are TDM voice
                                          or DSP farm profiles configured. To ensure the best system performance, reload the router when you change the voice-service-dsp-reservation .

## Examples

The following example enters voice-card configuration mode and sets the percentage of DSP resources for voice to 60%:

```
Router(config)# voice card 0 Router(config-voicecard)# voice-service dsp-reservation 60
```

### Related Commands

Command

Description

dspfarm profile

Adds the specified voice card to those participating in a DSP resource pool.

## voice service

To enter voice-service configuration mode and to specify a voice-encapsulation type, use the voice service command in global
                              configuration mode..

voice service { pots | voatm | vofr | voip }

### Syntax Description

pots

Telephony voice service.

voatm

Voice over ATM (VoATM) encapsulation.

vofr

Voice over Frame Relay (VoFR) encapsulation.

voip

Voice over IP (VoIP) encapsulation.

### Command Default

No default behavior or values.

### Command Modes

Global configuration

## Command History

Release

Modification

12.1(1)XA

This command was introduced on the Cisco MC3810.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T.

12.1(3)T

This command was integrated into Cisco IOS Release 12.1(3)T for VoIP on the Cisco 2600 series and the Cisco 3600 series.

12.1(3)XI

This command was implemented on the Cisco AS5300.

12.1(5)T

This command was integrated into Cisco IOS Release 12.1(5)T.

12.1(5)XM

This command was implemented on the Cisco AS5800.

12.1(5)XM2

This command was implemented on the Cisco AS5350 and Cisco AS5400.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(2)T

This command was integrated into Cisco IOS Release 12.2(2)T and implemented on the Cisco 7200 series.

Introduced support for YANG models.

### Usage Guidelines

Voice-service configuration mode is used for packet telephony service commands that affect the gateway globally.

## Examples

The following example enters voice-service configuration mode for VoATM service commands:

```
voice service voatm
```

## voice sip
                        	 sip-profiles

To upgrade or
                              		  downgrade SIP profile configurations to rule format or non-rule format, use voice sip sip-profiles command.

voice sip sip-profiles { upgrade | downgrade }

## Syntax Description

Upgrades
                                       					 all SIP profile configurations to rule format.

downgrades
                                       					 all SIP profile configurations to non-rule format.

### Command Default

none

### Command Modes

Privileged EXEC (#)

## Command History

15.5(2)T,
                                       					 Cisco IOS-XE Release 3.15S

This
                                       					 command was introduced.

## Examples

For upgrading SIP
                              		  profile configurations to rule format:

```
Device# voice sip sip-profiles upgrade
```

For downgrading
                              		  SIP profile configurations to non-rule format:

```
Device# voice sip sip-profiles downgrade
```

## voice sip oauth get-keys

To retrieve OAuth keys from the CUCM, use the voice sip oauth get-keys command.

### Command Default

None.

### Command Modes

SIP configuration mode.

## Command History

Cisco IOS XE Cupertino
                                             17.8.1a

This command was introduced.

### Usage Guidelines

Use the voice sip oauth get-keys command on SRST to get keys from the call manager.

## voice source-group

To define a source IP group for voice calls, use the voice source-group command in global configuration mode. To delete the source IP group, use the no form of this command.

voice source-group name

no voice source-group name

### Syntax Description

name

Name of the IP group. Maximum length of the source IP group name is 31 alphanumeric characters.

### Command Default

No default behavior or values

### Command Modes

Global configuration

## Command History

Release

Modification

12.2(11)T

This command was introduced.

### Usage Guidelines

Use the voice source-group command to assign a name to a set of source IP group characteristics. The terminating gateway uses these characteristics
                              to identify and translate the incoming VoIP call.

Carrier IDs and trunk group labels must not have the same names.

Do not mix carrier IDs and trunk group labels within a source IP group.

A terminating gateway can be configured with carrier ID source IP groups and trunk-group-label source IP groups. Th
                              e name of 
                              the source IP group must be unique to the gateway.

## Examples

The following example initiates source IP group "utah2" for VoIP calls:

```
Router(config)# voice source-group utah2
```

### Related Commands

Command

Description

access-list

Defines a list of source groups for identifying incoming calls.

carrier-id (voice source group)

Specifies the carrier handling a VoIP call.

description (voice source group)

Assigns a disconnect cause to a source IP group.

h323zone-id (voice source group)

Assigns a zone ID to an incoming H.323 call.

translation-profile (source group)

Assigns a translation profile to a source IP group.

trunk-group-label (voice source group)

Specifies the trunk handling a VoIP call.

## voice statistics accounting method

To enable voice accounting statistics to be collected for a specific accounting method list and to specify the pass criteria
                              for call legs, use the voice statistics accounting method command in global configuration mode. To disable the collection of statistics for the accounting method, use the no form of this command.

voice statistics accounting method method-list-name pass { start-interim-stop | start-stop | stop-only }

no voice statistics accounting method method-list-name pass { start-interim-stop | start-stop | stop-only }

### Syntax Description

method-list-name

Name of the accounting method list. The method-list-name argument is the same as that configured using the method command in gateway accounting AAA configuration mode.

pass

The pass criteria for call legs (PSTN or IP) and call directions (inbound or outbound) that is used by the method list.

The definition of pass implies that all start, stop, or interim messages are acknowledged by the designated servers. The definition
                                                      of failure implies that any start, stop, or interim message is rejected or is timed out by the designated servers.

start-interim-stop

All start, interim, and stop pass criteria records are counted.

start-stop

All start and stop pass criteria records are counted.

stop-only

Only stop pass criteria records are counted.

### Command Default

No statistics for the specified accounting method list are collected.

### Command Modes

Global configuration

## Command History

Release

Modification

12.3(4)T

This command was introduced.

## Examples

The following example shows that h323 is specified as the method list and that the pass criterion is stop-only:

```
Router(config)# voice statistics accounting method h323 pass stop-only
```

### Related Commands

Command

Description

method

Specifies the AAA method list name to be used.

show voice statistics csr interval accounting

Displays statistical information by configured intervals for accounting statistics.

show voice statistics csr since-reset accounting

Displays all accounting CSRs since the last reset.

voice statistics display-format separator

Specifies the format for CSR display.

voice statistics field-params

Specifies MCD, lost-packet, packet-latency, and packet-jitter parameters.

voice statistics max-storage-duration

Specifies the maximum time for which CSRs are stored in system memory.

voice statistics push

Specifies an FTP or syslog server for downloading CSRs, the maximum file size, and the maximum message size.

voice statistics time-range

Specifies the time range to collect CSRs.

voice statistics type

Enables the collection of accounting and signaling CSRs.

## voice statistics display-format separator

To configure the display format of the statistics on the gateway, use the voice statistics display-format separator command in global configuration mode. To return the display format of the statistics to the default value, use the no form of this command.

voice statistics display-format separator { space | tab | new-line | char char }

no voice statistics display-format separator { space | tab | new-line | char char }

### Syntax Description

separator

Type of separator used in the displayed format.

space

A space is used for the formatting between each statistic in the displayed output.

tab

A tab is used for the formatting between each statistic in the displayed output.

new-line

A new line is used for the formatting between each statistic in the displayed output.

char char

A character is used for the formatting between each statistic in the displayed output. The char argument is a visible ASCII
                                          character used for the formatting between each statistic in the displayed output.

### Command Default

A comma (,) is the default separator.

### Command Modes

Global configuration

## Command History

Release

Modification

12.3(4)T

This command was introduced.

## Examples

The following example shows that a space is specified as the display separator:

```
Router(config)# voice statistics display-format separator space
```

### Related Commands

Command

Description

voice statistics accounting method

Enables the accounting method and the pass and fail criteria.

voice statistics field-params

Specifies MCD, lost-packet, packet-latency, and packet-jitter parameters.

voice statistics max-storage-duration

Specifies the maximum time for which CSRs are stored in system memory.

voice statistics push

Specifies an FTP or syslog server for downloading CSRs, the maximum file size, and the maximum message size.

voice statistics time-range

Specifies the time range to collect CSRs.

voice statistics type

Enables the collection of accounting and signaling CSRs.

## voice statistics field-params

To configure the parameters of call statistics fields on the gateway, use the voice statistics field-params command in global configuration mode. To return the call statistics parameters to the default values, use the no form of this command.

voice statistics field-params { mcd value | lost-packet value | packet-latency value | packet-jitter value }

no voice statistics field-params { mcd value | lost-packet value | packet-latency value | packet-jitter value }

### Syntax Description

mcd

Minimum call duration. The value argument is an integer that represents the number of milliseconds. Valid values are from
                                          0 to 30. The default is 2.

lost-packet

Lost voice packet threshold. The value argument is an integer that represents milliseconds. Valid values are from 0 to 65535.
                                          The default is 1000.

packet-latency

Voice packet latency threshold. The value argument is an integer that represents milliseconds. Valid values are from 0 to
                                          500. The default is 250.

packet-jitter

Voice packet jitter threshold. The value argument is an integer that represents milliseconds. Valid values are from 0 to 1000.
                                          The default is 250.

### Command Default

MCD is 2 milliseconds.
                              Lost packet threshold is 1000 milliseconds.
                              Packet latency threshold is 250 milliseconds.
                              Packet jitter threshold is 250 milliseconds.

### Command Modes

Global configuration

## Command History

Release

Modification

12.3(4)T

This command was introduced.

## Examples

The following example configures a minimum call duration of 5 milliseconds:

```
Router(config)# voice statistics field-params mcd 5
```

The following example configures a lost packet threshold of 250 milliseconds:

```
Router(config)# voice statistics field-params lost-packet 250
```

The following example configures a packet-latency threshold of 300 milliseconds:

```
Router(config)# voice statistics field-params packet-latency 300
```

The following example configures a packet-jitter threshold of 245 milliseconds:

```
Router(config)# voice statistics field-params packet-jitter 245
```

### Related Commands

Command

Description

voice statistics accounting method

Enables the accounting method and the pass and fail criteria.

voice statistics display-format separator

Specifies the format for CSR display.

voice statistics max-storage-duration

Specifies the maximum time for which CSRs are stored in system memory.

voice statistics push

Specifies an FTP or syslog server for downloading CSRs, the maximum file size, and the maximum message size.

voice statistics time-range

Specifies the time range to collect CSRs.

voice statistics type

Enables the collection of accounting and signaling CSRs.

## voice statistics max-storage-duration

To configure the maximum amount of time for which collected
                              		  statistics are stored in the system memory of the gateway, use the voice statistics max-storage-duration command in global configuration mode. To remove the configured
                              		  maximum storage duration, use the no form of this command.

voice statistics
                                 				  max-storage-duration { day value | hour value |
                                 						minute value }

no voice statistics
                                 				  max-storage-duration { day value | hour value |
                                 						minute value }

### Syntax Description

day

Number of days for which call statistics data are to be
                                          						stored. The value argument has a valid range from 0 to 365.

hour

Number of hours for which call statistics data are to be
                                          						stored. The value argument has a valid range from 0 to 720.

minute

Number of minutes for which call statistics data are to be
                                          						stored. The value argument has a valid range from 0 to 1440.

### Command Default

If no length of time is configured, no memory is allocated for those
                              		  call statistic records that have stopped after the end of their collection
                              		  intervals. If no memory is allocated, only active call statistic record buffers
                              		  are kept in system memory.

### Command Modes

Global configuration

## Command History

Release

Modification

12.3(4)T

This command was introduced.

### Usage Guidelines

The maximum storage duration means the time-to-exist duration of the
                              		  call statistic records on the gateway.

The values entered using this command also apply to the collection of
                              		  VoIP internal error codes (IECs).

## Examples

The following example shows that the maximum storage duration for the
                              		  collection of voice call statistics has been set for 60 minutes:

```
Router(config)# voice statistics max-storage-duration minute 60
```

### Related Commands

Command

Description

voice statistics accounting method

Enables the accounting method and the pass and fail
                                          						criteria.

voice statistics display-format separator

Specifies the format for CSR display.

voice statistics field-params

Specifies MCD, lost-packet, packet-latency, and
                                          						packet-jitter parameters.

voice statistics push

Specifies an FTP or syslog server for downloading CSRs, the
                                          						maximum file size, and the maximum message size.

voice statistics time-range

Specifies the time range to collect CSRs.

voice statistics type

Enables the collection of accounting and signaling CSRs.

## voice statistics push

To configure the method for pushing signaling statistics, VoIP AAA accounting statistics, or Cisco internal error codes (IECs)
                              to an FTP or syslog server, use the voice statistics push command in global configuration mode. To disable the configured push method, use the no form of this command.

{ voice statistics push ftp url ftp-url [ max-file-size value ] | syslog [ max-msg-size value ]}

{ no voice statistics push ftp url ftp-url [ max-file-size value ] | syslog [ max-msg-size value ]}

### Syntax Description

ftp url

URL of the FTP server to which voice statistics are to be pushed. The syntax of the ftp-url argument follows:
                                          ftp://user:password@host:port//directory1/directory2

max-file-size

(Optional) Maximum size of a voice statistics file to be pushed to an FTP server, in bytes. The valid range of the value argument is from 1024 to 4294967296. The default value is 400000000 (4 GB).

syslog

Voice statistics are pushed to a syslog server.

max-msg-size

(Optional) Maximum size of a voice statistics file to be pushed to a syslog server, in bytes. The valid range of the value argument is from 1024 to 4294967296. The default value is 400000000 (4 GB).

### Command Default

Voice statistics are not pushed to an FTP or syslog server.

### Command Modes

Global configuration

## Command History

Release

Modification

12.3(4)T

This command was introduced.

### Usage Guidelines

The gateway configuration should be consistent with the configuration on the FTP or syslog servers. This command may also
                              be used to push Cisco VoIP internal error codes (IECs) to either an FTP server or a syslog server.

## Examples

The following is a configuration example showing a specified FTP server and maximum file size:

```
Router(config)# voice statistics push ftp url ftp://john:doe@abc:23//directory1/directory2 max-file-size 10000
```

### Related Commands

Command

Description

voice statistics accounting method

Enables the accounting method and the pass and fail criteria.

voice statistics display-format separator

Specifies the format for CSR display.

voice statistics field-params

Specifies MCD, lost-packet, packet-latency, and packet-jitter parameters.

voice statistics max-storage-duration

Specifies the maximum time for which CSRs are stored in system memory.

voice statistics time-range

Specifies the time range to collect CSRs.

voice statistics type

Enables the collection of accounting and signaling CSRs.

## voice statistics time-range

To specify a time range to collect statistics from the gateway on a
                              		  periodic basis, since the last reset, or for a specific time duration , use the voice statistics time-range command in global configuration mode. To disable the time-range
                              		  settings, use the no form of this command.

### Statistics Collection on a Periodic Basis

voice statistics
                                 				  time-range periodic interval start hh:mm { days-of-week { Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday | daily | weekday | weekend }} [ end hh:mm { days-of-week | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday | daily | weekday | weekend }]

no voice statistics
                                 				  time-range periodic interval start hh:mm { days-of-week { Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday | daily | weekday | weekend }} [ end hh:mm { days-of-week | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday | daily | weekday | weekend }]

### Statistics Collection Since the Last Reset or Reboot of the
                              			 Gateway

voice statistics time-range since-reset

no voice statistics time-range since-reset

### Statistics Collection at a Specific Time Duration

voice statistics time-range specific start hh : mm day month year end hh : mm day month year

no voice statistics time-range specific start hh : mm day month year end hh : mm day month year

### Syntax Description

Statistics Collection on a Periodic Basis:

periodic

Call statistics are collected for a configured period.

interval

Specifies the periodic interval during which statistics
                                          						will be collected. Valid entries for this value are 5minutes , 15minutes , 30minutes , 60minutes , or 1day .

start/end

Specifies the start and ending periods of the statistics
                                          						collection. If no end time is entered, then the statistics collection continues
                                          						nonstop. By default, there is no end of the collection period.

hh:mm

Specifies the start and ending times for the periodic
                                          						statistics collection in hours and minutes. The times entered must be in
                                          						24-hour format.

days-of-week

Specifies the start and ending days of the week that call
                                          						statistics are collected. You can configure a specific day of the week, or one
                                          						of the following:

daily--Call
                                                						  statistics are collected daily.

weekdays--Call
                                                						  statistics are collected on weekdays only.

weekend--Call
                                                						  statistics are collected on weekends only.

The default value is daily.

Statistics Collection Since the Last Reset or Reboot of the
                                          						Gateway

since-reset

Call statistics are collected only since a reset or reboot
                                          						of the gateway.

Voice statistics collection on the gateway is reset
                                                      						using the clear voice statistics csr command.

Statistics Collection at a Specified Time Duration:

specific

Call statistics are collected for a specific time duration.

start/end

Specifies the start and end times of the statistics
                                          						collection. The required arguments for both the start and end keywords are as
                                          						follows:

hh : mm--Hour and minute. The times entered must be in
                                                						  24-hour format.

day--Day of the
                                                						  month. Valid values are from 1 to 31.

month--Month
                                                						  for the statistics collection to start. Enter the month name, for example,
                                                						  January, or February. The default is the current month.

year--Year.
                                                						  Valid values are from 1993 to 2035. The default is the current year.

No statistics are collected by default.

### Command Modes

Global configuration

## Command History

Release

Modification

12.3(4)T

This command was introduced.

### Usage Guidelines

There should be only one specific or periodic configuration at any
                              		  one time. If a second specific or periodic configuration is configured, the
                              		  request is rejected and a warning message displays. If the no form of the
                              		  command is used during the specific time range, the corresponding collection
                              		  will stop and FTP or syslog messages will not be sent.

## Examples

The following example shows that the time range is periodic and set
                              		  to collect statistics for a 60-minute period on weekdays only beginning at
                              		  12:00 a.m.:

```
Router(config)# voice statistics time-range periodic 60minutes start 12:00 days-of-week weekdays
```

The following example configures the gateway to collect call
                              		  statistics since the last reset (specified with the clear voice statistics csr command) or since the last time the gateway was rebooted:

```
Router(config)# voice statistics time-range since-reset
```

The following example configures the gateway to collect statistics
                              		  from 10:00 a.m. on the first day of January to 12:00 a.m. on the second day of
                              		  January:

```
Router(config) # voice statistics time-range specific start 10:00 1 January 2004 end 12:00 2 January 2004
```

### Related Commands

Command

Description

clear voice statistics

Clears voice statistics, resetting the statistics
                                          						collection.

voice statistics accounting method

Enables the accounting method and the pass and fail
                                          						criteria.

voice statistics display-format separator

Specifies the format for CSR display.

voice statistics field-params

Specifies MCD, lost-packet, packet-latency, and
                                          						packet-jitter parameters.

voice statistics max-storage-duration

Specifies the maximum time for which CSRs are stored in
                                          						system memory.

voice statistics push

Specifies an FTP or syslog server for downloading CSRs, the
                                          						maximum file size, and the maximum message size.

voice statistics type

Enables the collection of accounting and signaling CSRs.

## voice statistics type csr

To configure a gateway to collect VoIP AAA accounting statistics or voice signaling statistics, independently or at the same
                              time, use the voice statistics type csr command in global configuration mode. To disable the counters, use the no form of this command.

voice statistics type csr [ accounting | signaling ]

no voice statistics type csr [ accounting | signaling ]

### Syntax Description

accounting

(Optional) VoIP AAA accounting statistics are collected.

signaling

(Optional) Voice signaling statistics are collected.

### Command Default

No accounting or signaling call statistics records (CSRs) are collected on the gateway.

### Command Modes

Global configuration

## Command History

Release

Modification

12.3(4)T

This command was introduced.

### Usage Guidelines

If you do not specify a keyword, both accounting and signaling CSRs are collected. Accounting and signaling CSR collection
                              can be enabled and disabled independently.

## Examples

The following example shows that both types of CSRs will be collected:

```
Router(config)# voice statistics type csr
```

The following example enables accounting CSRs to be collected:

```
Router(config)# voice statistics type csr accounting
```

The following example enables signaling CSRs to be collected:

```
Router(config)# voice statistics type csr signaling
```

The following example disables the collection of both signaling and accounting CSRs:

```
Router(config)# no voice statistics type csr
```

The following example disables the collection of signaling CSRs only:

```
Router(config)# no voice statistics type csr signaling
```

### Related Commands

Command

Description

voice statistics accounting method

Enables the accounting method and the pass and fail criteria.

voice statistics display-format separator

Specifies the format for CSR display.

voice statistics field-params

Specifies MCD, lost-packet, packet-latency, and packet-jitter parameters.

voice statistics max-storage-duration

Specifies the maximum time for which CSRs are stored in system memory.

voice statistics push

Specifies an FTP or syslog server for downloading CSRs, the maximum file size, and the maximum message size.

voice statistics time range

Specifies the time range to collect CSRs.

## voice statistics type iec

To enable collection of Internal Error Code (IEC) statistics, use the voice statistics type iec command in global configuration
                              mode. To disable IEC statistics collection, use the no form of this command.

voice statistics type iec

no voice statistics type iec

### Syntax Description

This command has no arguments or keywords.

### Command Default

IEC statistics collection is disabled.

### Command Modes

Global configuration.

## Command History

Release

Modification

12.3(4)T

This command was introduced.

Introduced support for YANG models.

## Examples

The following example enables IEC statistics collection:

```
Router(config)# voice statistics type iec
```

### Related Commands

Command

Description

clear voice statistics

Clears voice statistics, resetting the statistics collection.

show voice statistics

Displays voice statistics

show voice statistics interval-tag

Displays interval options available for IEC statistics

voice statistics time-range since-reset

Enables collection of call statistics accumulated since the last resetting of IEC counters

## voice translation-profile

To define a translation profile for voice calls, use the voice translation-profile command in global configuration mode. To delete the translation profile, use the no form of this command.

voice translation-profile name

no voice translation-profile name

### Syntax Description

name

Name of the translation profile. Maximum length of the voice translation profile name is 31 alphanumeric characters.

### Command Default

No default behavior or values

### Command Modes

Global configuration

## Command History

Release

Modification

12.2(11)T

This command was introduced.

### Usage Guidelines

After translation rules are defined, they are grouped into profiles. The profiles collect a set of rules that, taken together,
                              translate the called, calling, and redirected numbers in specific ways. Up to 1000 profiles can be defined. Each profile must
                              have a unique 
                              name
                              .

These profiles are referenced by trunk groups, dial peers, source IP groups, voice ports, and interfaces for handling call
                              translations.

## Examples

The following example initiates translation profile "westcoast" for voice calls. The profile uses translation rules 1, 2,
                              and 3 for various types of calls.

```
Router(config)# voice translation-profile westcoast Router(cfg-translation-profile)# translate calling 2 Router(cfg-translation-profile)# translate called 1 Router(cfg-translation-profile)# translate redirect-called 3
```

### Related Commands

Command

Description

rule (voice translation-rule)

Defines call translation criteria.

show voice translation-profile

Displays one or more translation profiles.

translate (translation profiles)

Associates a translation rule with a voice translation profile.

## voice translation-rule

To define a translation rule for voice calls, use the voice translation-rule command in global configuration mode. To delete the translation rule, use the no form of this command.

voice translation-rule number

no voice translation-rule number

### Syntax Description

number

Number that identifies the translation rule. Range is from 1 to 2147483647.

### Command Default

No default behavior or values

### Command Modes

Global configuration

## Command History

Release

Modification

12.2(11)T

This command was introduced.

### Usage Guidelines

Use the voice translation-rule command to create the definition of a translation rule. Each definition includes up to 15 rules that include SED-like expressions
                              for processing the call translation. A maximum of 128 translation rules are supported.

These translation rules are grouped into profiles that are referenced by trunk groups, dial peers, source IP groups, voice
                              ports, and interfaces.

## Examples

The following example initiates translation rule 150, Which includes two rules:

```
Router(config)# voice translation-rule 150 Router(cfg-translation-rule)# rule 1 reject /^408\(.(\)/ Router(cfg-translation-rule)# rule 2 /\(^...\)853\(...\)/ /\1525\2/
```

### Related Commands

Command

Description

rule (voice translation-rule)

Defines the matching, replacement, and rejection patterns for a translation rule.

show voice translation-rule

Displays the configuration of a translation rule.

## voice vad-time

To change the minimum silence detection time for voice activity detection (VAD), use the voice vad-time command in global configuration mode. To reset to the default, use the no form of this command.

voice vad-time milliseconds

no voice vad-time

### Syntax Description

milliseconds

Waiting period, in milliseconds, before silence detection and suppression of voice-packet transmission. Range is from 250
                                          to 65536. The default is 250.

### Command Default

250 milliseconds

### Command Modes

Global configuration

## Command History

Release

Modification

12.0(7)XK

This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T.

### Usage Guidelines

This command affects all voice ports on a router or concentrator, but it does not affect calls already in progress.

You can use this command in transparent common-channel signaling (CCS) applications in which you want VAD to activate when
                              the voice channel is idle, but not during active calls. With a longer silence detection delay, VAD reacts to the silence of
                              an idle voice channel, but not to pauses in conversation.

This command does not affect voice codecs that have ITU-standardized built-in VAD features--for example, G.729B, G.729AB, G.723.1A.
                              The VAD behavior and parameters of these codecs are defined exclusively by the applicable ITU standard.

## Examples

The following example configures a 20-second delay before VAD silence detection is enabled:

```
voice vad-time 20000
```

### Related Commands

Command

Description

vad (dial peer)

Enables voice activity detection on a network dial peer.

## voice vrf

To configure a voice VRF, use the voice vrf command in global configuration mode. To remove the voice VRF configuration, use the no form of this command.

voice vrf vrfname

no voice vrf vrfname

### Syntax Description

vrfname

A name assigned to the voice vrf.

### Command Default

No voice VRF is configured.

### Command Modes

Global configuration

## Command History

Release

Modification

12.4(11)XJ

This command was introduced.

12.4(15)T

This command was integrated into Cisco IOS Release 12.4(15)T.

### Usage Guidelines

You must create a VRF using the ip vrf vrfname command before you can configure it as a voice VRF.

To ensure there are no active calls on the voice gateway during a VRF change, voices services must be shut down on the voice
                              gateway before you configure or make changes to a voice VRF.

## Examples

The following example shows that a VRF called vrf1 was created and then configured as a voice VRF:

```
ip vrf vrf1
 rd 1:1
 route-target export 1:2
 route-target import 1:2
!
voice vrf vrf1
!
voice service voip
```

### Related Commands

Command

Description

ip vrf

Defines a VPN VRF instance and enters VRF configuration mode.

## voip-incoming translation-profile

To specify a translation profile for all incoming VoIP calls, use the voip-incoming translation-profile command in global configuration mode. To delete the profile, use the no form of this command.

voip-incoming translation-profile name

no voip-incoming translation-profile name

### Syntax Description

name

Name of the translation profile.

### Command Default

No default behavior or values

### Command Modes

Global configuration

## Command History

Release

Modification

12.2(11)T

This command was introduced.

### Usage Guidelines

Use the voip-incoming translation-profile command to globally assign a translation profile for all incoming VoIP calls. The translation profile was previously defined
                              using the voice translation-profile command. The voip-incoming translation-profile command does not require additional steps to complete its definition.

If an H.323 call comes in and the call is associated with a source IP group that is defined with a translation profile, the
                              source IP group translation profile overrides the global translation profile.

## Examples

The following example assigns the translation profile named "global-definition" to all incoming VoIP calls:

```
Router(config)# voip-incoming translation-profile global-definition
```

### Related Commands

Command

Description

show voice translation-profile

Displays the configurations for all voice translation profiles.

test voice translation-rule

Tests the voice translation rule definition.

voice translation-profile

Initiates a translation profile definition.

## voip-incoming translation-rule

To set the incoming translation rule for calls that originate from H.323-compatible clients, use the voip-incoming translation-rule command in global configuration mode. To disable the incoming translation rule, use the no form of this command.

voip-incoming translation-rule { calling | called } name-tag

no voip-incoming translation-rule { calling | called } name-tag

### Syntax Description

name-tag

Tag number by which the rule set is referenced. This is an arbitrarily chosen number. Range is from 1 to 2147483647. There
                                          is no default value.

calling

Automatic number identification (ANI) number or the number of the calling party.

called

Dial Number Information Service (DNIS) number or the number of the called party.

### Command Default

No default behavior or values

### Command Modes

Global configuration

## Command History

Release

Modification

12.0(7)XR1

This command was introduced for VoIP on the Cisco AS5300.

12.0(7)XK

This command was implemented for VoIP on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810.

12.1(1)T

This command was integrated into Cisco IOS Release 12.1(1)T and implemented for VoIP on the Cisco 1750, Cisco AS5300, Cisco
                                          7200 series, and Cisco 7500 series platforms.

12.1(2)T

This command was implemented for VoIP on Cisco MC3810.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T.

### Usage Guidelines

With this command, all IP-based calls are captured and handled, depending on either the calling number or the called number
                              to the specified tag name.

## Examples

The following example identifies the rule set for calls that originate from H.323-compatible clients:

```
Router(config)# voip-incoming translation-rule called 5
```

### Related Commands

Command

Description

numbering-type

Matches one number type for a dial-peer call leg.

rule

Applies a translation rule to a calling party number or a called party number for both incoming and outgoing calls.

show translation-rule

Displays the contents of all the rules that have been configured for a specific translation name.

test translation-rule

Tests the execution of the translation rules on a specific name-tag.

translate

Applies a translation rule to a calling party number or a called party number for incoming calls.

translate-outgoing

Applies a translation rule to a calling party number or a called party number for outgoing calls.

translation-rule

Creates a translation name and enters translation-rule configuration mode.

## voip trunk group

To define or modify a VOIP trunk group and to enter trunk group configuration mode, use the voip trunk group command in global configuration mode. To delete the VOIP trunk group, use the no form of this command.

voip trunk group name

no voip trunk group name

### Syntax Description

name

Name of the voip trunk group. Valid names contain a maximum of 63 alphanumeric characters.

### Command Default

No voip trunk group is defined.

### Command Modes

Global configuration

## Command History

Release

Modification

15.2(2)T

This command was introduced.

### Usage Guidelines

Use the voip trunk group command to define the VOIP trunk and extend serviceability to the trunk. By default, the session protocol of the IP trunk
                              is h323. Up to 1000 trunk groups can be configured on the gateway provided that the gateway has sufficient memory to store
                              the profiles

## Examples

The following example enables creates a VOIP trunk group and enables monitoring.

```
Router(config)# voip trunk group siptrk1 Router(config-voip-trk)# session protocol sipv2 Router(config-voip-trk)# target ipv4: 10.1.1.15 Router(config-voip-trk)# xsvc
```

### Related Commands

Command

Description

show voip trunk group

Displays internal list of voip trunk groups.

xsvc

Enables monitoring on the trunk.

## volume

To set the receiver volume level for a POTS port on a router, use the volume command in dial-peer voice configuration mode. To reset to the default, use the no form of this command.

volume number

no volume number

### Syntax Description

number

A number from 1 to 5 representing decibels (dB) of gain. Range is as follows:

1: -11.99 dB

2: -9.7dB

3: -7.7dB

4: -5.7dB

5: -3.7dB

Default is 3 (-7.7 dB gain).

### Command Default

3 (-7.7  dB gain)

### Command Modes

Dial-peer voice configuration

## Command History

Release

Modification

12.2(8)T

This command was introduced on Cisco 803, Cisco 804, and Cisco 813 routers.

### Usage Guidelines

Set the volume command for each POTS port separately. Setting the volume level affects only the port for which it has been set.

Only the receiver volume is set with this command.

Use the show pots volume command to check the volume status and level.

## Examples

The following example shows a volume level of 4 for POTS port 1 and a volume level of 2 for POTS port 2.

```
dial-peer voice 1 pots
 destination-pattern 5551111
 port 1
 no call-waiting
 ring 0
 volume 4
dial-peer voice 2 pots
 destination-pattern 5552222
 port 2
 no call-waiting
 ring 0
 volume 2
```

### Related Commands

Command

Description

show pots volume

Shows the receiver volume configured for each POTS port on a router.

## vxml allow-star-digit

To configure a Voice Extensible Markup Language (VXML) interpreter to allow the star digit for built-in type digits, use the vxml allow-star-digit command in global configuration mode. To disable the configuration, use the no form of this command.

vxml allow-star-digit

no vxml allow-star-digit

### Syntax Description

This command has no arguments or keywords.

### Command Default

A VXML interpreter is not configured.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

15.0(1)M

This command was introduced in a release earlier than Cisco IOS Release 15.0(1)M.

## Examples

The following example shows how to configure a VXML interpreter to allow the star digit for built-in type digits:

```
Router# configure terminal Router(config)# vxml allow-star-digit
```

### Related Commands

Command

Description

vxml audioerror

Enables throwing an error event when audio playout fails.

vxml version pre2.0

Enables VoiceXML 2.0 features.

## vxml logging-tag

To allow fetching logging tag header in Nuance ASR, use the vxml logging-tag command in global configuration mode. The logging-tag command helps in sending the logging-tag headers to Nuance ASR as part of a RECOGNIZE or SPEAK and SET-PARAM message. The
                              command configuration is enabled by default. To disable the configuration, use the no form of this command.

vxml logging-tag

no vxml logging-tag

This command has no arguments or keywords.

### Command Default

Enabled.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

15.5(3)M7

This command was introduced in the Cisco IOS Release 15.0(3)M7.

### Usage Guidelines

Enabling this command helps the gateway to send the logging-tag headers to Nuance ASR as part of a RECOGNIZE or SPEAK and
                              SET-PARAM message. By default the command is in enable state. If you disable the command, the gateway will not send Logging-tag
                              in RECOGNIZE or SPEAK. But, only SET-PARAM message carries Logging-Tag.

## Examples

The following example disables the vxml logging-tag feature:

```
Router(config)# no vxml logging-tag
```

## vxml audioerror

To enable throwing an error event when audio playout fails, use the vxml audioerror command in global configuration mode. To return to the default, use the no form of this command.

vxml audioerror

no vxml audioerror

### Syntax Description

This command has no arguments or keywords.

### Command Default

An audio error event, error.badfetch, is not thrown when an audio file cannot be played.

### Command Modes

Global configuration

## Command History

Release

Modification

12.4(11)T

This command was introduced.

### Usage Guidelines

Entering this command causes an audio error event, error.badfetch, to be thrown when an audio file cannot be played, for instance,
                              because the file is in an unsupported format, the src attribute references an invalid URI, or the expr attribute evaluates
                              to an invalid URI.

The vxml audioerror command overrides the vxml version 2.0 command, so that if both commands are entered, the audio error event will be thrown when an audio file cannot be played.

## Examples

The following example enables the audio error feature:

```
Router(config)# vxml audioerror
```

### Related Commands

Command

Description

vxml version pre2.0

Enables features compatible with versions earlier than VoiceXML 2.0.

## vxml tree memory

To set the maximum memory size for the VoiceXML parser tree, use the vxml tree memory command in global configuration mode. To reset to the default, use the no form of this command.

vxml tree memory size

no vxml tree memory

### Syntax Description

size

Maximum memory size, in kilobytes. Range is 64 to 100000. Default is 1000.

### Command Default

1000 KB

### Command Modes

Global configuration

## Command History

Release

Modification

12.2(15)T

This command was introduced.

12.4(15)T

The default was changed from 64 to 1000.

### Usage Guidelines

This command limits the memory resources available for parsing VoiceXML documents, preventing large documents from consuming
                              excessive system memory. Increasing the maximum memory size for the VoiceXML tree enables calls to use larger VoiceXML documents.
                              If a VoiceXML document exceeds the limit, the gateway aborts the document execution and the debug vxml error command displays a "vxml malloc fail" error.

In Cisco IOS Release 12.3(4)T and later releases, less memory is consumed when parsing a VoiceXML document because the document
                                          is not stored by the VoiceXML tree.

## Examples

The following example sets the maximum memory size to 128 KB:

```
vxml tree memory 128
```

### Related Commands

Command

Description

debug vxml error

Displays VoiceXML application error messages.

ivr prompt memory

Sets the maximum amount of memory that dynamic audio files (prompts) occupy in memory.

ivr record memory system

Sets the maximum amount of memory for storing all voice recordings on the gateway.

## vxml version 2.0

To enable VoiceXML 2.0 features, use the vxml version 2.0 command in global configuration mode. To return to the default, use the no form of this command.

vxml version 2 . 0

no vxml version 2 . 0

### Syntax Description

This command has no arguments or keywords.

### Command Default

The default VoiceXML behavior is compatible with versions earlier than W3C VoiceXML 2.0 Specification .

### Command Modes

Global configuration

## Command History

Release

Modification

12.4(11)T

This command was introduced.

### Usage Guidelines

This command enables the following VoiceXML features:

An audio error event, error.badfetch, is not thrown when an audio file cannot be played, for instance, because the file is
                                    in an unsupported format, the src attribute references an invalid URI, or the expr attribute evaluates to an invalid URI.

Support for the beep attribute of the <record> element.

Blind transfer compliant with W3C VoiceXML 2.0 and not the same as consultation transfer.

Compatibility with W3C VoiceXML 2.0 Specification.

A semantic error is generated if an undeclared variable is used. You must declare variables before using them.

## Examples

The following example enables VoiceXML version 2.0 features:

```
Router(config)# vxml version 2.0
```

| options-keepalive failure | Configures the SIP error code for options-keepalive failures. |
|---|---|
| call spike failure | Configures the SIP error code for call spike failures. |
| cac-bandwidth failure | Configures the SIP error code for Call Admission Control bandwidth failures. |
| sip-status-code-number | The SIP status code that is sent for the options keepalive, call spike, or cac-bandwidth failure. The range is from 400 to
                                          699. The default value is 503. The table below in the “Usage Guidelines” section describes these error codes. |
| system | Specifies the system configuration used for keepalive, call spike, or cac-bandwidth failures. |

| Release | Modification |
|---|---|
| 15.0(1)XA | This command was introduced. |
| 15.1(1)T | This command was integrated into Cisco IOS Release 15.1(1)T. |
| 15.1(3)T | This command was modified. The call spike failure keyword was added. |
| 15.2(2)T | This command was modified. The cac-bandwidth failure keyword was added. |

| Error Code Number | Description |
|---|---|
| 400 | Bad request |
| 401 | Unauthorized |
| 402 | Payment required |
| 403 | Forbidden |
| 404 | Not found |
| 408 | Request timed out |
| 416 | Unsupported Uniform Resource Identifier (URI) |
| 480 | Temporarily unavailable |
| 482 | Loop detected |
| 484 | Address incomplete |
| 486 | Busy here |
| 487 | Request terminated |
| 488 | Not acceptable here |
| 500–599 | SIP 5xx—server/service failure |
| 500 | Internal server error |
| 502 | Bad gateway |
| 503 | Service unavailable |
| 600–699 | SIP 6xx—global failure |

| Command | Description |
|---|---|
| error-code-override | Configures the SIP error code for options-keepalive, call spike, or cac-bandwidth failures in voice service SIP and dial
                                          peer voice configuration mode, respectively. |

| annexb-all | Specifies that the G.729br8 codec is treated as a superset of G.729r8 and G.729br8 codecs to communicate with Cisco Unified
                                          Communications Manager. |
|---|---|
| system | (Optional) Specifies that the dial peer allow communication between incompatible G.729 codecs according to global settings
                                          configured for this feature on the Cisco IOS SIP gateway. |

| Release | Modification |
|---|---|
| 12.4(15)XZ | This command was introduced. |
| 12.4(20)T | This command was integrated into Cisco IOS Release 12.4(20)T. |

| Command | Description |
|---|---|
| g729 annexb-all | Configure global settings that determine if a Cisco IOS SIP gateway treats the G.729br8 codec as superset of G.729r8 and G.729br8
                                          codecs. |

| system | (Optional) Enables history-info support using global configuration settings. |
|---|---|

| Release | Modification |
|---|---|
| 12.4(22)T | This command was introduced. |
| Cisco IOS XE 
                                          Release 3.1S | This command was integrated into Cisco IOS XE Release 3.1S |

| Note | The Cisco IOS SIP gateway cannot use the information in the history-info header to make routing decisions. |
|---|---|

| Command | Description |
|---|---|
| history-info | Enables SIP history-info header support on Cisco IOS gateway at a global level. |

| dns: [ hostname. ] domain | Alphanumeric value representing the DNS domain (consisting
                                          						of the domain name with or without a specific hostname) in place of the
                                          						physical IP address that is used in the host portion of the From, Call-ID, and
                                          						Remote-Party-ID headers in outgoing messages. This value can be the hostname and the domain separated by
                                          						a period
                                          						( dns: hostname.domain ) or
                                          						just the domain name
                                          						( dns: domain ). In both case,
                                          						the dns: delimiter must be included as
                                          						the first four characters. |
|---|---|
| preferred | (Optional) Designates the specified DNS hostname as
                                          						preferred. |

| Release | Modification |
|---|---|
| 12.4(2)T | This command was introduced. |
| 15.0(1)XA | This command was modified. The preferred keyword was added to
                                          						specify the preferred localhost if multiple registrars are configured on a SIP
                                          						trunk. |
| IOS Release XE 2.5 | This command was integrated into Cisco IOS XE Release 2.5. |
| 15.1(1)T | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| authentication (dial peer) | Enables SIP digest authentication on an individual dial
                                          						peer. |
| authentication (SIP UA) | Enables SIP digest authentication. |
| credentials (SIP UA) | Configures a Cisco UBE to send a SIP registration message
                                          						when in the UP state. |
| localhost | Configures global settings for substituting a DNS localhost
                                          						name in place of the physical IP address in the From, Call-ID, and
                                          						Remote-Party-ID headers of outgoing messages. |
| registrar | Enables Cisco IOS SIP gateways to register E.164 numbers on
                                          						behalf of FXS, EFXS, and SCCP phones with an external SIP proxy or SIP
                                          						registrar. |

| 181 | The code representing the specific incoming SIP provisional response messages to be mapped and replaced. |
|---|---|
| to | The designator for specifying that the specified incoming SIP provisional response message should be mapped to and replaced
                                          with a different SIP provisional response message on the outgoing SIP dial peer. |
| 183 | The code representing the specific SIP provisional response message on the outgoing dial peer to which incoming SIP message
                                          responses should be mapped. |

| Release | Modification |
|---|---|
| 15.0(1)XA | This command was introduced. |
| 15.1(1)T | This command was integrated into Cisco IOS Release 15.1(1)T. |
| Cisco IOS XE Release 3.1S | This command was integrated into Cisco IOS XE Release 3.1S. |

| Note | If the block command is configured for incoming SIP 181 messages, either globally or at the dial-peer level, the messages may be dropped
                                          before they can be passed or mapped to a different message--even when the voice-class sip map resp-code command is enabled. To globally configure whether and when incoming SIP 181 messages are dropped, use the block command in voice service SIP configuration mode (or use the voice-class sip block command in dial peer voice configuration mode to configure drop settings on individual dial peers). |
|---|---|

| Note | This command is supported only for SIP-to-SIP calls and will have no effect on H.323-to-SIP or time-division multiplexing
                                          (TDM)-to-SIP calls. |
|---|---|

| Command | Description |
|---|---|
| block | Configures global settings for dropping specific SIP provisional response messages on a Cisco IOS voice gateway or Cisco UBE. |
| map resp-code | Configures global settings on a Cisco UBE for mapping specific incoming SIP provisional response messages to a different SIP
                                          response message. |
| voice-class sip block | Configures an individual dial peer on a Cisco IOS voice gateway or Cisco UBE to drop specified SIP provisional response messages. |

| passthru media-change | Passes
                                          						SIP messages that inolve media-change from one IP leg to another IP leg. |
|---|---|
| block | Blocks
                                          						all SIP messages during mid-call. |
| preserve-codec | Preserves codec negotiated during call initialization.
                                          						Mid-call codec change is disabled. |

| Release | Modification |
|---|---|
| 12.4(15)XZ | This
                                          						command was introduced. |
| 12.4(20)T | This
                                          						command was integrated into Cisco IOS Release 12.4(20)T. |
| Cisco
                                          						IOS XE Release 2.5 | This
                                          						command was integrated into Cisco IOS XE Release 2.5. |
| 15.2(1)T | This
                                          						command was integrated into Cisco IOS Release 15.2(1)T. The media-change and block keywords were added. |
| 15.3(2)S, 15.3(1)T | This
                                          						command was modified. The preserve-codec keyword was added. |

| Command | Description |
|---|---|
| allow-connections | Allows connections between specific types of endpoints in a Cisco Unified BE. |

| media-keepalive | Specifies media keepalive to subscriber if it's located behind NAT. |
|---|---|
| interval | Specifies keepalive interval in seconds. Range is 1—50. Default is 10. |

| Release | Modification |
|---|---|
| Cisco IOS XE 17.13.1a Cisco IOS XE Dublin 17.12.2 | This command was introduced. |

| Note | The voice-class sip nat media-keepalive command takes affect immediately after it is applied. |
|---|---|

| Command | Description |
|---|---|
| nat media-keepalive | Uses the SIP Network Address Translation (NAT) global configuration. |
| voice class tenant tag | Associates a dial-peer with a specific tenant configuration. |

| keepalive-group-profile-id | Specifies the keepalive group profie id. |
|---|---|
| up-interval seconds | Number of up-interval seconds allowed to pass before marking the UA as unavailable.The range is 5-1200. The default is 60. |
| down-interval seconds | Number of down-interval seconds allowed to pass before marking the UA as unavailable.The range is 5-1200. The default is 30. |
| retry retries | Number of retry attempts before marking the UA as unavailable. The range is 1 to 10. The default is 5 attempts. |

| Release | Modification |
|---|---|
| 12.4(22)YB | This command was introduced. |
| 15.0(1)M | This command was integrated into Cisco IOS Release
                                          						15.0(1)M. |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models. |

| Error Code | Description |
|---|---|
| 503 | service unavailable |
| 505 | sip version not supported |
| no response | i.e. request timeout |

| Command | Description |
|---|---|
| dial-peer voice | Defines a particular dial peer and specifies the method of voice encapsulation. |

| keepalive-group-profile-id | Specifies the keepalive group profile id. |
|---|---|

| Release | Modification |
|---|---|
| Cisco IOS XE Dublin
                                          17.11.1a | This command was introduced. |

| dhcp | Specifies that the outbound-proxy IP address is retrieved
                                          						from a DHCP server. |
|---|---|
| ipv4: ipv4-address | Configures proxy on the server, sending all initiating
                                          						requests to the specified IPv4 address destination. The colon is required. |
| ipv6:[ ipv6-
                                                							 address ] | Configures proxy on the server, sending all initiating
                                          						requests to the specified IPv6 address destination. Brackets must be entered
                                          						around the IPv6 address. The colon is required. |
| dns: host:domain | Configures proxy on the server, sending all initiating
                                          						requests to the specified domain destination. The colons are required. |
| : port-number | (Optional) Port number for the Session Initiation Protocol
                                          						(SIP) server. The colon is required. |

| Release | Modification |
|---|---|
| 12.4(15)T | This command was introduced. |
| 12.4(22)T | This command was modified. Support for IPv6 was added. |
| 12.4(22)YB | This command was modified. The dhcp keyword was added. |
| 15.0(1)M | This command was integrated in Cisco IOS Release 15.0(1)M. |

| Command | Description |
|---|---|
| dial - peer voice | Defines a particular dial peer, specifies the method of
                                          						voice encapsulation, and enters dial peer configuration mode. |
| voice service | Enters voice-service configuration mode and specifies a
                                          						voice encapsulation type. |

| sip-server | (Optional) Adds SIP server information to the Route header. |
|---|---|
| service-route | Adds the Service-Route information to the Route header. |
| system | Uses the global system value. This is the default. |

| Release | Modification |
|---|---|
| 12.4(22)YB | This command was introduced. |
| 15.0(1)M | This command was integrated into Cisco IOS Release 15.0(1)M. |

| Command | Description |
|---|---|
| preloaded-route | Enables preloaded route support for VoIP SIP calls. |

| disable | Disables the privacy service for this dial peer regardless of prior implementations. When selected, this becomes the only
                                          valid option. |
|---|---|
| pstn | Requests that the privacy service implements a privacy header using the default Public Switched Telephone Network (PSTN) rules
                                          for privacy (based on information in Octet 3a). When selected, this becomes the only valid option. |
| system | Uses the global configuration settings to enable the privacy service on this dial peer. When selected, this becomes the only
                                          valid option. |
| privacy-option | The privacy support options to be set at the dial-peer level. The following keywords can be specified for the privacy-option argument: header -- Requests that privacy be enforced for all headers in the Session Initiation Protocol (SIP) message that might identify
                                                information about the subscriber. history -- Requests that the information held in the history-info header is hidden outside the trust domain. id -- Requests that the Network Asserted Identity that authenticated the user be kept private with respect to SIP entities outside
                                                the trusted domain. session -- Requests that the information held in the session description is hidden outside the trust domain. user -- Requests that privacy services provide a user-level privacy function. Note The keywords can be used alone, altogether, or in any combination with each other, but each keyword can be used only once. | Note | The keywords can be used alone, altogether, or in any combination with each other, but each keyword can be used only once. |
| Note | The keywords can be used alone, altogether, or in any combination with each other, but each keyword can be used only once. |
| critical | (Optional) Requests that the privacy service performs the specified service or fail the request. Note This optional keyword is only available after at least one of the privacy-option keywords ( header , history , id , session , or user ) has been specified and can be used only once per command. | Note | This optional keyword is only available after at least one of the privacy-option keywords ( header , history , id , session , or user ) has been specified and can be used only once per command. |
| Note | This optional keyword is only available after at least one of the privacy-option keywords ( header , history , id , session , or user ) has been specified and can be used only once per command. |

| Note | The keywords can be used alone, altogether, or in any combination with each other, but each keyword can be used only once. |
|---|---|

| Note | This optional keyword is only available after at least one of the privacy-option keywords ( header , history , id , session , or user ) has been specified and can be used only once per command. |
|---|---|

| Release | Modification |
|---|---|
| 12.4(15)T | This command was introduced. |
| 12.4(22)T | The history keyword was added to provide support for the history-info header information. |

| Command | Description |
|---|---|
| asserted-id | Sets the privacy level and enables either PAI or PPI privacy headers in outgoing SIP requests or response messages. |
| calling-info pstn-to-sip | Specifies calling information treatment for PSTN-to-SIP calls. |
| clid (voice-service-voip) | Passes the network-provided ISDN numbers in an ISDN calling party information element screening indicator field, removes the
                                          calling party name and number from the calling-line identifier in voice service voip configuration mode, or allows a presentation
                                          of the calling number by substituting for the missing Display Name field in the Remote-Party-ID and From headers. |
| privacy | Sets privacy support at the global level as defined in RFC 3323. |

| passthru | Passes the privacy values from the received message to the next call leg. |
|---|---|
| send-always | Passes a privacy header with a value of None to the next call leg, if the received message does not contain privacy values
                                          but a privacy header is required. |
| strip | Strip the diversion or history-info headers received from the next call leg. |
| diversion | Strip the diversion header received from the next call leg. |
| history-info | Strip the history-info header received from the next call leg. |
| system | (Optional) Uses the global configuration settings to configure the dial peer. |

| Release | Modification |
|---|---|
| 12.4(22)YB | This command was introduced. |
| 15.0(1)M | This command was integrated into Cisco IOS Release 15.0(1)M. |
| 15.1(2)T | This command was integrated into Cisco IOS Release 15.1(2)T. The strip , diversion , and history-info keywords were added. |

| Command | Description |
|---|---|
| asserted-id | Sets the privacy level and enables either PAID or PPID privacy headers in outgoing SIP requests or response messages. |
| privacy-policy | Configures the privacy header policy options at the global configuration level. |

| system | (Optional) Uses the global configuration settings to populate the INVITE message with random contact information. |
|---|---|

| Release | Modification |
|---|---|
| 12.4(22)YB | This command was introduced. |
| 15.0(1)M | This command was integrated into Cisco IOS Release 15.0(1)M. |

| Command | Description |
|---|---|
| credentials (sip ua) | Sends a SIP registration message from a Cisco Unified Border Element in the UP state. |
| registrar | Enables SIP gateways to register E.164 numbers on behalf of FXS, EFXS, and SCCP phones with an external SIP proxy or SIP registrar. |
| random-contact | Populates the outgoing INVITE message with random contact information at the global level. |

| system | (Optional) Uses the global configuration settings to enable called-number validation on this dial peer. |
|---|---|

| Release | Modification |
|---|---|
| 12.4(22)YB | This command was introduced. |
| 15.0(1)M | This command was integrated into Cisco IOS Release 15.0(1)M. |

| Command | Description |
|---|---|
| credentials (sip ua) | Sends a SIP registration message from a Cisco Unified Border Element in the UP state. |
| random-request-uri validate | Validates the called number based on the random value generated during the registration of the number at the global configuration
                                          level. |
| registrar | Enables SIP gateways to register E.164 numbers on behalf of FXS, EFXS, and SCCP phones with an external SIP proxy or SIP registrar. |

| system | (Optional) Enables the referto-passing command configured in global configuration mode. |
|---|---|

| Release | Modification |
|---|---|
| 15.2(1)T | This command was introduced. |

| Command | Description |
|---|---|
| dial-peer voice | Defines a particular dial peer, specifies the method of encapsulation, and enters dial peer voice configuration mode. |
| referto-passing | Disables dial peer lookup and modification of the Refer-To header when the Cisco UBE passes across a REFER message during
                                          a call transfer |

| static | (Optional) Configures Cisco Unified Border Element (UBE) to use static registrar details for SIP registration. Cisco UBE works
                                          in point-to-point mode when the static keyword is used. |
|---|---|
| rate-limit | (Optional) Configures SIP registration pass-through rate-limiting options. |
| expires value | (Optional) Sets the expiry value for rate limiting, in seconds. The range is from 60 to 65535. The default is 3600. |
| fail-count value | (Optional) Sets the fail-count value for rate limiting. The range is from 2 to 20. The default is 0. |
| registrar-index | (Optional) Configures the registrar index used for registration pass-through. |
| index | (Optional) Registration index value. The range is from 1 to 6. |
| system | (Optional) Uses global registration pass-through configuration to configure the SIP registration pass-through options. |

| Release | Modification |
|---|---|
| 15.1(3)T | This command was introduced. |

| Command | Description |
|---|---|
| registration passthrough | Configures SIP registration pass-through options at the global level. |

| supported value | Supports reliable provisional responses. The value argument may have any value, as long as both the user-agent client (UAC) and user-agent server (UAS) configure it the same. |
|---|---|
| require value | Requires reliable provisional responses. The value argument may have any value, as long as both the UAC and UAS configure it the same. |
| system | Uses the value configured in voice service mode. This is the default. |
| disable | Disables the use of reliable provisional responses. |

| Release | Modification |
|---|---|
| 12.2(2)XB | This command was introduced. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T. Support for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and
                                          Cisco AS5850 is not included in this release. |
| 12.2(11)T | This command was applicable to the Cisco AS5300, Cisco AS5350, and Cisco AS5400 in this release. |

| Command | Description |
|---|---|
| rel1xx | Provides provisional responses for calls on all VoIP calls. |

| system | (Optional) |
|---|---|

| Release | Modification |
|---|---|
| 15.4(1)T | This command was introduced. |

| Command | Description |
|---|---|
| contact-passing | Configures pass-through of the contact header from one leg
                                          						to the other leg for 302 pass-through. |
| requri-passing | Enables pass through of the host part of the Request-URI and
                                          						To SIP headers. |
| session target sip-uri | Derives session target from incoming URI. |
| voice-class sip requri-passing | Enables the pass through of SIP URI headers. |

| 183 | Specifies resetting of the expires timer upon receipt of SIP 183 Session In Progress messages. |
|---|---|

| Release | Modification |
|---|---|
| 15.0(1)XA | This command was introduced. |
| 15.1(1)T | This command was integrated into Cisco IOS Release 15.1(1)T. |

| Note | The expires timer default is three minutes. However, you can configure the expiration time to a maximum of 30 minutes using
                                          the timers expires command in SIP user agent (UA) configuration mode. |
|---|---|

| Command | Description |
|---|---|
| reset timer expires | Globally configures Cisco Unified CME, a Cisco IOS voice gateway, or a Cisco UBE to reset the expires timer upon receipt of
                                          a SIP 183 message. |
| timers expires | Specifies how long a SIP INVITE request remains valid before it times out if no appropriate response is received for keeping
                                          the session alive. |

| tag | DSCP profile group tag number. The range is from 1 to 10000. |
|---|---|

| Release | Modification |
|---|---|
| 15.2(2)T | This command was introduced. |

| Command | Description |
|---|---|
| dial-peer voice | Configures a dial peer and enters dial peer voice configuration mode. |
| dscp media | Specifies the RPH to DSCP mapping. |

| loose | (Optional) In the loose mode, unknown values of name space or priority values received in the Resource-Priority header in
                                          Session Initiation Protocol (SIP) requests are ignored by the gateway. The request is processed as if the Resource-Priority
                                          header was not present. |
|---|---|
| strict | (Optional) In the strict mode, unknown values of name space or priority values received in the Resource-Priority header in
                                          SIP requests are rejected by the gateway using a SIP response code 417 (Unknown Resource-Priority) message response. An Accept-Resource-Priority
                                          header enumerating the supported name space and values is included in the 417 message response. |

| Release | Modification |
|---|---|
| 12.4(2)T | This command was introduced. |

| Command | Description |
|---|---|
| voice-class sip resource priority namespace | Priorities mandatory call prioritization handling for initial original INVITE message requests. |

| drsn | (Optional) U. S. Defense Red Switched Network (DRSN). |
|---|---|
| dsn | (Optional) U. S. Defense Switched Network (DSN). |
| q735 | (Optional) International Telecommunications Union, Stage 3 description for community of interest supplementary services using Signaling System No. 7: Multilevel precedence
                                             and preemption, Recommendation Q.735.3 , March 1993. |

| Release | Modification |
|---|---|
| 12.4(2)T | This command was introduced. |

| Command | Description |
|---|---|
| voice-class sip resource priority mode | Pushes the UAS to operate in a loose or strict mode. |

| video | Specifies the video RSVP stream type. |
|---|---|
| voice | Specifies the audio or fax RSVP stream type. |
| post-alert | Specifies that behavior takes place only when the call state is post alert. |
| optional | Specifies that behavior takes place when RSVP fails even if RSVP negotiation is optional. |
| mandatory | Specifies that behavior takes place when RSVP fails only if RSVP negotiation is mandatory. |
| keep-alive | Specifies the sending of keepalive messages when RSVP fails. |
| disconnect | Specifies that the call is disconnected if RSVP fails after the specified number of retry settings. |
| retry | Specifies the number of reconnection attempts before disconnecting the call. |
| retry-attempts | The number of retry attempts. Valid entries are from 1 to 100. |
| interval | Specifies the interval between keepalive or retry attempts. |
| seconds | The retry interval in seconds. Valid entries are from 5 to 3600. |

| Release | Modification |
|---|---|
| 12.4(22)T | This command was introduced. |

| Command | Description |
|---|---|
| acc-qos | Defines the acceptable QoS for inbound and outbound calls on a VoIP dial peer. |
| handle-replaces | Configures fallback to legacy handling of SIP INVITE. |
| ip qos defending-priority | Configures the RSVP defending priority value. |
| ip qos dscp | Sets the DSCP value for QoS. |
| ip qos policy-locator | Configures application-specific reservations (application IDs) used for specifying bandwidth reservations. |
| ip qos preemption-priority | Configures the RSVP preemption priority value. |
| req-qos | Requests a particular QoS using RSVP to be used in reaching a specified dial peer in VoIP. |
| show-sip-ua calls | Displays the active UAC and UAS information on SIP calls. |

| Release | Modification |
|---|---|
| 15.2(4)M | This command was introduced. |

| Command | Description |
|---|---|
| voice-class sip block | Configures an individual dial peer on a Cisco IOS voice gateway or Cisco UBE to drop (not pass) specific incoming Session
                                          Initiation Protocol (SIP) provisional response messages. |

| Note | Effective Cisco IOS XE Everest Releases 16.5.1b, srtp-auth command is deprecated. Although this command is still available in Cisco IOS XE Everest software, executing this command
                                          does not cause any configuration changes. Use voice class srtp-crypto command to configure SRTP connection using preferred crypto-suites. For more information, see voice-class sip srtp-crypto command documentation. |
|---|---|

| sha-32 | Allows
                                       					 secure calls with AES_CM_128_HMAC_SHA1_32 authentication suite. |
|---|---|
| sha-80 | Allows
                                       					 secure calls with AES_CM_128_HMAC_SHA1_80 authentication suite. |
| system | Uses the
                                       					 global configuration. |

| Release | Modification |
|---|---|
| 15.4(1)T | This
                                       					 command was introduced. |
| Cisco IOS XE Everest 16.5.1b | This command was deprecated. |

| Command | Description |
|---|---|
| srtp-auth | Configures a Secure Real-time Transport Protocol (SRTP)
                                          						connection on Cisco Unified Border Element (Cisco UBE) in the global level
                                          						using the preferred crypto suite. |
| show sip-ua srtp | Displays Session
                                          						Initiation Protocol (SIP) user-agent (UA) Secure Real-time Transport Protocol
                                          						(SRTP) information. |

| crypto-tag | Unique
                                       					 number assigned to the voice class. The range is from 1 to 10000. This
                                       					 number maps to the tag created using the voice class
                                             						  srtp-crypto command available in global configuration mode. |
|---|---|

| Release | Modification |
|---|---|
| Cisco IOS XE Everest 16.5.1b | This
                                       					 command was introduced. |

| Note | Ensure that an srtp voice-class is created using the voice class srtp-crypto crypto-tag command before executing the voice-class sip srtp-crypto crypto tag command to apply the crypto-tag
                                          			 under global or tenant configuration mode. |
|---|---|

| Command | Description |
|---|---|
| srtp-crypto | Assigns a previously configured crypto-suite selection preference list globally or to a voice class tenant. |
| crypto | Specifies the preference for a SRTP cipher-suite that will be offered by Cisco Unified Border Element (CUBE) in the SDP in
                                          offer and answer. |
| show sip-ua calls | Displays active user agent client (UAC) and user agent server (UAS) information on Session Initiation Protocol (SIP) calls. |
| show sip-ua srtp | Displays Session Initiation Protocol (SIP) user-agent (UA) Secure Real-time Transport Protocol (SRTP) information. |

| cisco | Enables an individual dial peer on a Cisco IOS SIP gateway to negotiate the sending and accepting of RTP profiles in response
                                          to SRTP offers, overriding the global setting for the gateway. |
|---|---|
| system | Specifies that the individual dial peer use global (system) SRTP negotiation settings for the Cisco IOS SIP gateway. This
                                          is the default setting. |

| Release | Modification |
|---|---|
| 12.4(15)XY | This command was introduced. |
| 12.4(20)T | This command was integrated into Cisco IOS Release 12.4(20)T. |
| 12.4(22)T | Support was extended to the Cisco Unified Border Element. |

| Command | Description |
|---|---|
| srtp (dial peer) | Specifies that an individual dial peer use SRTP to enable secure calls and, optionally, enables fallback to RTP (overriding
                                          global settings). |
| srtp (voice) | Specifies use of SRTP to enable secure calls and, optionally, enables fallback to RTP globally on a Cisco IOS SIP gateway. |
| srtp negotiate | Enables SRTP negotiation globally on a Cisco IOS SIP gateway. |

| phone-context | Appends the phone context parameter to the TEL URL on a dial-peer basis. |
|---|---|
| system | Uses the system value. This is the default. |

| Release | Modification |
|---|---|
| 12.4(22)YB | This command was introduced. |
| 12.4(24)T | This command was integrated into Cisco IOS Release 12.4(24)T. |

| Command | Description |
|---|---|
| tel-config to-hdr | Configures the To: Header Request URI to telephone format for VoIP SIP calls. |

| tag | A
                                          						number used to identify voice-class sip tenant. The range is from 1 to 10000. |
|---|---|

| Release | Modification |
|---|---|
| 15.6(2)T and IOS XE Denali 16.3.1 | This
                                          						command was introduced. |

| udp | Enables switching transport from UDP on the basis of the size of the SIP request being greater than the MTU size. |
|---|---|
| tcp | Enables switching transport to TCP. |

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |

| Command | Description |
|---|---|
| debug ccsip transport | Enables tracing of the SIP transport handler and the TCP or UDP process. |
| transport switch | Enables switching between transport mechanisms globally if the SIP message is larger than 1300 bytes. |

| sip | Generates URLs in the SIP format for calls on a dial-peer basis. |
|---|---|
| sips | Generates URLs in the SIPS format for calls on a dial-peer basis. |
| tel | Generates URLs in the TEL format for calls on a dial-peer basis. |
| phone-context | (Optional) Appends the phone context parameter to the TEL URL on a dial-peer basis. |
| system | Uses the system value. This is the default. |

| Release | Modification |
|---|---|
| 12.2(2)XB | This command was introduced. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T. Support for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and
                                          Cisco AS5850 was not included in this release. |
| 12.2(11)T | This command was implemented on the Cisco AS5300, Cisco AS5350, and Cisco AS5400 platforms. |
| 12.4(6)T | The sips keyword was added. |
| 12.4(22)YB | The phone-context keyword was added. |
| 15.0(1)M | This command was integrated into Cisco IOS Release 15.0(1)M. |

| Command | Description |
|---|---|
| sip url | Generates URLs in the SIP, SIPS, or TEL format. |
| url | Configures URLs to either SIP, SIPS, or TEL format. |

| loopback | Specifies the loopback interface address. |
|---|---|
| interface-id | Specifies the interface on which the address is to be configured. |
| ipv4-address | (Optional) IPv4 address used in the loopback interface address. |
| ipv6-address | (Optional) IPv6 address used in the loopback interface address. |

| Release | Modification |
|---|---|
| 12.4(22)T | This command was introduced. |

| Command | Description |
|---|---|
| dial-peer voice | Defines a particular dial peer, specifies the method of voice encapsulation, and enters dial
                                          
                                          peer configuration mode. |

| tag | Unique identifier in the range 1 to 10000. |
|---|---|

| Release | Cisco Product | Modification |
|---|---|---|
| 12.4(22)T | Cisco Unified CME 7.0 | This command was introduced. |
| 15.1(2)T | Cisco Unified CME 8.1 | This command was modified. This command can be enabled in ephone summary, ephone template, voice register pool, or voice register
                                          pool template configuration mode. |

| Command | Description |
|---|---|
| stun usage firewall-traversal flowdata | Enables firewall traversal using STUN. |
| stun flowdata agent-id | Configures the agent ID. |

| tag | Unique label assigned to the voice class. The tag label maps to the tag label created using the voice class tone-signal global configuration command. Can be up to 32 alphanumeric characters. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)XD | This command was introduced. |
| 12.3(7)T | This command was integrated into Cisco IOS Release 12.3(7)T. |

| Command | Description |
|---|---|
| voice class tone-signal | Enters voice-class configuration mode and assigns an identification tag number for a tone-signal voice class. |

| ctl-file-name | Name of the CTL  file. A maximum number of 30 characters can be entered for the CTL file name. |
|---|---|

| Release | Modification |
|---|---|
| 15.3(3)M | This command was introduced. |

| Release | Modification |
|---|---|
| 11.3(1)MA | This command was introduced on Cisco MC3810. |

| Command | Description |
|---|---|
| connection | Specifies a connection mode for a voice port. |

| map-name | Name of the DNIS map. |
|---|---|
| url | (Optional) URL of an external text file that contains a list of DNIS entries. |

| Release | Modification |
|---|---|
| 12.2(2)XB | This command was introduced on the Cisco AS5300, Cisco AS5350, and Cisco AS5400. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T and implemented on the Cisco 3640 and Cisco 3660. |

| Command | Description |
|---|---|
| dnis | Adds a DNIS number to a DNIS map. |
| dnis-map | Associates a DNIS map with a dial peer. |
| show voice dnis-map | Displays configuration information about DNIS maps. |
| voice dnis-map load | Reloads a DNIS map that has changed since the previous load. |

| map-name | Name of the DNIS map to reload. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(2)XB | This command was introduced on the Cisco AS5300, Cisco AS5350, and Cisco AS5400. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T and implemented on the Cisco 3640 and Cisco 3660. |

| Command | Description |
|---|---|
| dnis | Adds a DNIS number to a DNIS map. |
| dnis-map | Associates a DNIS map with a dial peer. |
| show voice dnis-map | Displays configuration information about DNIS maps. |
| voice dnis-map | Enters DNIS map configuration mode to create a DNIS map. |

| destination url | Designates a valid file system where crash dump analysis is stored. The url argument must be set to a valid file system. The destination url can be one of the following The file on a TFTP server with the following format:
                                                tftp://x.x.x.x/subfolder/filename. The x.x.x.x value is the IP address of the TFTP server The file on the flashcard of the router, with the following format: slot0:filename Note The digital signal processor (DSP) crash dump feature is disabled when either the crash-dump destination is not specified. | Note | The digital signal processor (DSP) crash dump feature is disabled when either the crash-dump destination is not specified. |
|---|---|---|---|
| Note | The digital signal processor (DSP) crash dump feature is disabled when either the crash-dump destination is not specified. |
| file-limit limit-number | The crash dump file-limit keyword must be set to a non-zero value. The default is that the crash dump capability is turned
                                          off, as the url argument is empty, and the file-number argument is zero. The limit-number argument may range from 0 (no file will be written) to 99. Note The DSP crash dump feature is disabled when the crash-dump file limit is set to 0. | Note | The DSP crash dump feature is disabled when the crash-dump file limit is set to 0. |
| Note | The DSP crash dump feature is disabled when the crash-dump file limit is set to 0. |

| Note | The digital signal processor (DSP) crash dump feature is disabled when either the crash-dump destination is not specified. |
|---|---|

| Note | The DSP crash dump feature is disabled when the crash-dump file limit is set to 0. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Note | Some types of flash need to be completely erased to free up space from deleted files, and some types of flash cannot have
                                          files overwritten with new versions until the entire flash is erased. As a result, you might want to set the file limit so
                                          that only one or two dump files are written to flash. This prevents flash from being filled up. |
|---|---|

| Note | It is not recommended to write crash dump files to internal flash or bootflash, because these files are normally used to hold
                                          configuration information and Cisco IOS software images. Cisco recommends writing crash dump files to spare flash cards, which
                                          can be inserted into slot 0 or slot 1 on many of the routers. These cards usually do not hold critical information and may
                                          be erased. Additionally, these cards can be conveniently removed from the router and sent to Cisco, so that the crash dump
                                          files can be analyzed. |
|---|---|

| Command | Description |
|---|---|
| debug voice dsp crash-dump | Displays crash dump debug information. |
| show voice dsp crash-dump | Displays voice dsp crash dump information. |

| Release | Modification |
|---|---|
| IOS XE Fuji Release 16.8.1 | This command was introduced. |

| codec | (Optional) Defines restricted codecs, both small and large. |
|---|---|
| small codec | Small footprint codec. Valid values for the codec argument are: g711 g726 |
| large codec | Large footprint codec. Valid values for the codec argument are: fax-relay g723 g728 g729 gsmefr gsmfr |

| Release | Modification |
|---|---|
| 12.2(13)T | This command was introduced. |
| 12.3(3) | This command was modified to allow unrestricted codecs on the Cisco AS5300. The codec keyword was made optional. |

| Note | This command is valid only when the echo-cancel enable command and the 
                                          echo-cancel coverage command are enabled. |
|---|---|

| Command | Description |
|---|---|
| echo-cancel coverage | Enables the cancellation of voice that is sent out the interface and is received on the same interface. |
| echo-cancel enable | Enables the cancellation of voice that is sent and received on the same interface. |

| table-number | Number of the ENUM match table. Range is from 1 to 15. There is no default value. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |

| Command | Description |
|---|---|
| rule (ENUM configuration) | Defines the matching, replacement, and rejection patterns for an ENUM match table. |
| show voice enum-match-table | Displays the configuration of voice ENUM match tables. |
| test enum | Tests the functionality of an ENUM match table. |

| buffer size | (Optional) Size of HPI capture buffer, in bytes. Range is from 328 to 9000000. The default is 328. |
|---|---|
| destination url | (Optional) Destination URL for storing captured data. |

| Release | Modification |
|---|---|
| 12.2(10) | This command was introduced. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. |

| Caution | Using the message logger feature in a production network environment impacts CPU and memory usage on the gateway. |
|---|---|

| Command | Description |
|---|---|
| debug hpi | Turns on the debug output for the logger. |
| show voice hpi capture | Displays the capture status and statistics. |

| disconnect-cause-code | A code returned from the destination router to indicate why an attempted end-to-end call was unsuccessful. If the specified
                                          disconnect cause code is returned from the last destination endpoint, dial peer hunting is enabled or disabled. The table
                                          below in the "Usage Guidelines" section describes the possible values. You can enter the keyword, decimal value, or hexadecimal
                                          value. |
|---|---|
| all | Continue dial-peer hunting for all disconnect cause codes returned from the destination endpoint. |
| default | Restores the default dial-peer hunt setting, that is, the router stops dial-peer hunting if it receives the user-busy or
                                          no-answer disconnect cause code. |

| Release | Modification |
|---|---|
| 12.0(5)T | This command was introduced for VoFR on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. It was also introduced
                                          for VoIP on the Cisco 2600 series and Cisco 3600 series. |
| 12.0(7)T | This command was implemented for VoIP on the Cisco AS5300 and Cisco AS5800. |
| 12.0(7)XK | This command was implemented for VoIP on the Cisco MC3810. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T and implemented for VoIP on the Cisco MC3810. |
| 12.1(3)XI | The invalid-number and unassigned-number keywords were added, and the command name was changed to voice hunt . |
| 12.1(5)T | This command was integrated into Cisco IOS Release 12.1(5)T. |
| 12.2(4)T | Keywords were added for more disconnect cause codes. |
| 12.3(8)T | The disconnect-cause-code argument was modified to accept nonstandard disconnect cause codes. |

| Note | While configuring voice hunt , it is necessary to configure reason header override in the sip-ua configuration mode to ensure that correct cause codes are sent to the other leg. For more information on reason header override configuration, see reason-header override command. |
|---|---|

| Keyword | Description | Decimal | Hex |
|---|---|---|---|
| access-info-discard | Access information discarded. | 43 | 0x2b |
| all | Continue dial-peer hunting for all disconnect cause codes received from a destination router. |  |  |
| b-cap-not-implemented | Bearer capability not implemented. | 65 | 0x41 |
| b-cap-restrict | Restricted digital information bearer capability only. | 70 | 0x46 |
| b-cap-unauthorized | Bearer capability not authorized. | 57 | 0x39 |
| b-cap-unavail | Bearer capability not available. | 58 | 0x3a |
| call-awarded | Call awarded. | 7 | 0x7 |
| call-cid-in-use | Call exists, call ID in use. | 83 | 0x53 |
| call-clear | Call cleared. | 86 | 0x56 |
| call-reject | Call rejected. | 21 | 0x15 |
| cell-rate-unavail | Cell rate not available. | 37 | 0x25 |
| channel-unacceptable | Channel unacceptable. | 6 | 0x6 |
| chantype-not-implement | Channel type not implemented. | 66 | 0x42 |
| cid-in-use | Call ID in use. | 84 | 0x54 |
| codec-incompatible | Codec incompatible. | 171 | 0xab |
| cug-incalls-bar | Closed user group (CUG) incoming calls barred. | 55 | 0x37 |
| cug-outcalls-bar | CUG outgoing calls barred. | 53 | 0x35 |
| dest-incompatible | Destination incompatible. | 88 | 0x58 |
| dest-out-of-order | Destination out of order. | 27 | 0x1b |
| dest-unroutable | No route to destination. | 3 | 0x3 |
| dsp-error | Digital signal processor (DSP) error. | 172 | 0xac |
| dtl-trans-not-node-id | Designated transit list (DTL) transit not my node ID. | 160 | 0xa0 |
| facility-not-implemented | Facility not implemented. | 69 | 0x45 |
| facility-not-subscribed | Facility not subscribed. | 50 | 0x32 |
| facility-reject | Facility rejected. | 29 | 0x1d |
| glare | Glare. | 15 | 0xf |
| glaring-switch-pri | Glaring switch PRI. | 180 | 0xb4 |
| htspm-oos | Holst Telephony Service Provider Module (HTSPM) out of service. | 129 | 0x81 |
| ie-missing | Mandatory information element missing. | 96 | 0x60 |
| ie-not-implemented | Information element not implemented. | 99 | 0x63 |
| info-class-inconsistent | Inconsistency in information and class. | 62 | 0x3e |
| interworking | Interworking. | 127 | 0x7f |
| invalid-call-ref | Invalid call reference value. | 81 | 0x51 |
| invalid-ie | Invalid information element contents. | 100 | 0x64 |
| invalid-msg | Invalid message. | 95 | 0x5f |
| invalid-number | Invalid number. | 28 | 0x1c |
| invalid-transit-net | Invalid transit network. | 91 | 0x5b |
| misdialled-trunk-prefix | Misdialed trunk prefix. | 5 | 0x5 |
| msg-incomp-call-state | Message in incomplete call state. | 101 | 0x65 |
| msg-not-implemented | Message type not implemented. | 97 | 0x61 |
| msgtype-incompatible | Message type not compatible. | 98 | 0x62 |
| net-out-of-order | Network out of order. | 38 | 0x26 |
| next-node-unreachable | Next node unreachable. | 128 | 0x80 |
| no-answer | No user answer. | 19 | 0x13 |
| no-call-suspend | No call suspended. | 85 | 0x55 |
| no-channel | Channel does not exist. | 82 | 0x52 |
| no-circuit | No circuit. | 34 | 0x22 |
| no-cug | Nonexistent CUG. | 90 | 0x5a |
| no-dsp-channel | No DSP channel. | 170 | 0xaa |
| no-req-circuit | No requested circuit. | 44 | 0x2c |
| no-resource | No resource. | 47 | 0x2f |
| no-response | No user response. | 18 | 0x12 |
| no-voice-resources | No voice resources available. | 126 | 0x7e |
| non-select-user-clear | Nonselected user clearing. | 26 | 0x1a |
| normal-call-clear | Normal call clearing. | 16 | 0x10 |
| normal-unspecified | Normal, unspecified. | 31 | 0x1f |
| not-in-cug | User not in CUG. | 87 | 0x57 |
| number-changeed | Number changed. | 22 | 0x16 |
| param-not-implemented | Nonimplemented parameter passed on. | 103 | 0x67 |
| perm-frame-mode-oos | Permanent frame mode out of service. | 39 | 0x27 |
| perm-frame-mode-oper | Permanent frame mode operational. | 40 | 0x28 |
| precedence-call-block | Precedence call blocked. | 46 | 0x2e |
| preempt | Preemption. | 8 | 0x8 |
| preempt-reserved | Preemption reserved. | 9 | 0x9 |
| protocol-error | Protocol error. | 111 | 0x6f |
| qos-unavail | QoS unavailable. | 49 | 0x31 |
| rec-timer-exp | Recovery on timer expiry. | 102 | 0x66 |
| redirect-to-new-destination | Redirect to new destination. | 23 | 0x17 |
| req-vpci-vci-unavail | Requested VPCI VCI not available. | 35 | 0x23 |
| send-infotone | Send information tone. | 4 | 0x4 |
| serv-not-implemented | Service not implemented. | 79 | 0x4f |
| serv/opt-unavail-unspecified | Service or option not available, unspecified. | 63 | 0x3f |
| stat-enquiry-resp | Response to status enquiry. | 30 | 0x1e |
| subscriber-absent | Subscriber absent. | 20 | 0x14 |
| switch-congestion | Switch congestion. | 42 | 0x2a |
| temp-fail | Temporary failure. | 41 | 0x29 |
| transit-net-unroutable | No route to transit network. | 2 | 0x2 |
| unassigned-number | Unassigned number. | 1 | 0x1 |
| unknown-param-msg-discard | Unrecognized parameter message discarded. | 110 | 0x6e |
| unsupported-aal-parms | ATM adaptation layer (AAL) parameters not supported. | 93 | 0x5d |
| user-busy | User busy. | 17 | 0x11 |
| vpci-vci-assign-fail | Virtual path connection identifier virtual channel identifier (VPCI VCI) assignment failure. | 36 | 0x24 |
| vpci-vci-unavail | No VPCI VCI available. | 45 | 0x2d |

| Command | Description |
|---|---|
| huntstop | Disables all further dial-peer hunting if a call fails when using hunt groups. |
| preference | Indicates the preferred order of a dial peer within a rotary hunt group. |

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |
| Cisco IOS XE Cupertino 17.7.1 | Introduced support for YANG models. |

| Command | Description |
|---|---|
| clear voice statistics | Clears voice statistics, resetting the statistics collection. |
| show voice statistics iec | Displays iec statistics |
| show voice statistics interval-tag | Displays interval options available for IEC statistics |
| voice statistics type iec | Enables collection of IEC statistics |

| Release | Modification |
|---|---|
| 11.3(1)MA | This command was introduced. |
| 12.0(7)XK | This command was implemented on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T. |

| Command | Description |
|---|---|
| input gain | Configures a specific input gain value. |
| output attenuation | Configures a specific output attenuation value. |

| Cisco IOS Release | Cisco Products | Modification |
|---|---|---|
| 12.4(22)YB | Cisco Unified CME 7.1 | This command was introduced. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command was integrated into Cisco IOS Release 12.4(24)T. |

| Command | Description |
|---|---|
| access-digit | Defines the access digit that phone users dial to request a precedence call. |
| mlpp preemption | Enables calls on an SCCP phone or analog FXS port to be preempted. |
| preemption trunkgroup | Enables preemption capabilities on a trunk group. |

| keypad-character | One or two digits that can be dialed on a telephone keypad. Range is 0 to 9 for one-digit codes; 00 to 99 for two-digit codes.
                                          Default is 0 (zero) for one-digit codes; 00 (two zeroes) for two-digit codes. Note Number of digits depends on the value set with the digit command. | Note | Number of digits depends on the value set with the digit command. |
|---|---|---|---|
| Note | Number of digits depends on the value set with the digit command. |

| Note | Number of digits depends on the value set with the digit command. |
|---|---|

| Release | Modification |
|---|---|
| 12.4(2)T | This command was introduced. |
| 12.4(6)T | The keypad-character argument was modified to allow two-digit codes. |

| Command | Description |
|---|---|
| digit | Designates the number of digits for STC application feature speed-dial codes. |
| prefix (stcapp-fsd) | Designates a prefix to precede the dialing of an STC application feature speed-dial code. |
| redial | Designates an STC application feature speed-dial code to dial again the last number that was dialed. |
| show running-config | Displays current nondefault configuration settings. |
| show stcapp feature codes | Displays configured and default STC application feature codes. |
| speed dial | Designates a range of STC application feature speed-dial codes. |
| stcapp feature speed-dial | Enters STC application feature speed-dial configuration mode to set feature speed-dial codes. |

| buffer number | Allocates the number of PCM capture buffers. The range is from 0 to 200000. The default is 0. |
|---|---|
| destination url | Specifies the destination URL for storing captured data. |
| on-demand-trigger | (Optional) Configures PCM capture user trigger on-demand. |
| user-trigger-string start-string stop-string stream bitmap duration call-duration | (Optional) Configures PCM user trigger string. start-string —Start string up to 15 characters. stop-string —Stop string up to 15 characters. stream —Configures the PCM capture stream bitmap. bitmap —PCM stream bitmap in hexadecimal. The range is from 1 to FFFFFFF. The default is 7. duration —Configures the duration for PCM capture. call-duration —Duration of call. The range is from 0 to 255. The default is 0. |

| Release | Modification |
|---|---|
| 15.2(2)T | This command was introduced. |

| Command | Description |
|---|---|
| show voice pcm capture | Displays PCM capture status and statistics. |

| pp-name | The phone proxy instance name. |
|---|---|

| Release | Modification |
|---|---|
| 15.3(3)M | This command was introduced. |

| size size | Buffer size in MB. The range is from 10 to 60. |
|---|---|
| aging | Checks the age of the phone proxy buffer files. |
| time | Time in seconds. The range is from 10 to 3600. Based on the set time, the file buffer will be periodically checked. |

| Release | Modification |
|---|---|
| IOS XE Fuji Release 16.8.1 | This command was introduced. |

| ipv4 ipv4-address | IPv4 address of the TFTP server. |
|---|---|
| ipv6 ipv6-address | IPv6 address of the TFTP server. |
| vrf vrf-name | Name of the TFTP server’s VRF. |

| Release | Modification |
|---|---|
| 15.3(3)M | This command was introduced. |
| IOS XE Fuji Release 16.8.1 | This command was enhanced to add the ipv6 keyword. |

| port-number | Analog foreign exchange station (FXS) voice port number. Range: 2/0 to 2/23. |
|---|---|
| dial dial-string | String of up to 16 characters that can be dialed on a telephone keypad. Valid characters are 0 through 9, A through D, an
                                          * (asterisk) and # (pound sign). The voice gateway sends this string to the call-control system when the analog phone goes
                                          off hook. |
| digit dtmf-digits | (Optional) String of up to 16 characters that can be dialed on a telephone keypad. Valid characters are 0 through 9, A through
                                          D, an * (asterisk), # (pound sign), and comma (,). The voice gateway sends this string to the call-control system after the wait-msecs expires. Each comma represents a one second wait. |
| wait-connect wait-msecs | (Optional) Number of milliseconds that the voice gateway waits after voice cut-through before out-pulsing the DTMF digits.
                                          Range: 0 to 30000, in multiples of 50. Default: 50. If 0, DTMF digits are sent automatically by voice gateway after call is
                                          connected. |
| interval inter-digit-msecs | (Optional) Number of milliseconds between the DTMF digits. Range: 50 to 500, in multiples of 50. Default: 50. |

| Release | Modification |
|---|---|
| 12.4(6)T | This command was introduced. |

| Command | Description |
|---|---|
| dial-peer voice | Enters dial-peer configuration mode and defines a dial peer. |
| sccp plar | Enters SCCP PLAR configuration mode. |

| slot-number | Number of the slot in the router in which the voice interface card (VIC) is installed. Valid entries are from 0 to 2, depending
                                          on the slot in which it has been installed. |
|---|---|
| port | Voice port number. Valid entries are 0 and 1. |

| slot-number | Number of the slot in the router in which the VIC is installed. Valid entries are from 0 to 3, depending on the slot in which
                                          it has been installed. |
|---|---|
| subunit-number | Subunit on the VIC in which the voice port is located. Valid entries are 0 or 1. |
| port | Voice port number. Valid entries are 0 and 1. |
| slot | The router location in which the voice port adapter is installed. Valid entries are from 0 to 3. |
| port: | Indicates the voice interface card location. Valid entries are 0 and 3. |
| ds0-group-no | Indicates the defined DS0 group number. Each defined DS0 group number is represented on a separate voice port. This allows
                                          you to define individual DS0s on the digital T1/E1 card. |

| controller-number | T1 or E1 controller. |
|---|---|
| :D | D channel associated with ISDN PRI. |

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced. |
| 11.3(3)T | This command was implemented on the Cisco 2600 series. |
| 12.0(3)T | This command was implemented on the Cisco AS5300. |
| 12.0(7)T | This command was implemented on the Cisco AS5800, Cisco 7200 series, and Cisco 1750. Arguments were added for the Cisco 2600
                                          series and Cisco 3600 series. |
| 12.2(8)T | This command was implemented on Cisco 1751 and Cisco 1760. This command was modified to accommodate the additional ports
                                          of the NM-HDA on the Cisco 2600 series, Cisco 3640, and Cisco 3660. |
| 12.2(2)XN | Support for enhanced MGCP voice gateway interoperability was added to Cisco CallManager Version 3.1 for the Cisco 2600 series,
                                          Cisco 3600 series, and Cisco VG200. |
| 12.2(11)T | This command was integrated into the Cisco IOS Release 12.2(11)T and Cisco CallManager Version 3.2 and implemented on the
                                          Cisco IAD2420 series. |
| 12.2(13)T | This command was integrated into Cisco IOS Release 12.2(13)T. This command does not support the extended echo canceller (EC)
                                          feature on the Cisco AS5300 or the Cisco AS5800. |

| Note | This command does not support the extended echo canceller (EC) feature on the Cisco AS5300. |
|---|---|

| Command | Description |
|---|---|
| dial-peer voice | Enters dial-peer configuration mode and specifies the method of voice encapsulation. |

| Release | Modification |
|---|---|
| 12.0(3)T | This command was introduced on the Cisco MC3810. |

| Command | Description |
|---|---|
| busyout forced | Forces a voice port into the busyout state. |
| busyout monitor | Places a voice port into the busyout monitor state. |
| busyout seize | Changes the busyout action for an FXO or FXS voice port. |
| show voice busyout | Displays information about the voice busyout state. |

| Release | Modification |
|---|---|
| 12.1(5)T | This command was introduced on Cisco 2600 series, Cisco 3600 series, Cisco 7200 series, Cisco 7500 series, Cisco AS5300, Cisco
                                          AS5800, and Cisco MC3810 platforms. |
| 12.2(2)XA | This command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(11)T | This command was integrated into the Cisco IOS Release 12.2(11)T. |

| Note | The voice rtp source-filter command is applicable only to ISR-G2 (3945e) routers. |
|---|---|

| Release | Modification |
|---|---|
| 15.5(3)M9 15.6(3)M6 | This command was introduced. |

| Command | Description |
|---|---|
| voice service voip | Specifies the voice-encapsulation type and enters voice service configuration mode. |
| voice rtp send-recv | Establishes a two-way voice path when the Real-Time Transport Protocol (RTP) channel is opened. |

| percentage | Percentage of DSP resources on this voice card that are reserved for voice services. The remaining DSP resources will be available
                                          for video services. |
|---|---|

| Release | Modification |
|---|---|
| 15.1(4)M | The command was introduced. |

| Note | You can configure a percentage less than 100% only when there is a video license and the appropriate PVDM# modules are installed. |
|---|---|

| Tip | DSP can become fragmented when you change the percentage of DSP resources reserved for voice services when there are TDM voice
                                          or DSP farm profiles configured. To ensure the best system performance, reload the router when you change the voice-service-dsp-reservation . |
|---|---|

| Command | Description |
|---|---|
| dspfarm profile | Adds the specified voice card to those participating in a DSP resource pool. |

| pots | Telephony voice service. |
|---|---|
| voatm | Voice over ATM (VoATM) encapsulation. |
| vofr | Voice over Frame Relay (VoFR) encapsulation. |
| voip | Voice over IP (VoIP) encapsulation. |

| Release | Modification |
|---|---|
| 12.1(1)XA | This command was introduced on the Cisco MC3810. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T. |
| 12.1(3)T | This command was integrated into Cisco IOS Release 12.1(3)T for VoIP on the Cisco 2600 series and the Cisco 3600 series. |
| 12.1(3)XI | This command was implemented on the Cisco AS5300. |
| 12.1(5)T | This command was integrated into Cisco IOS Release 12.1(5)T. |
| 12.1(5)XM | This command was implemented on the Cisco AS5800. |
| 12.1(5)XM2 | This command was implemented on the Cisco AS5350 and Cisco AS5400. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(2)T | This command was integrated into Cisco IOS Release 12.2(2)T and implemented on the Cisco 7200 series. |
| Cisco IOS XE Amsterdam 17.2.1r | Introduced support for YANG models. |

| upgrade | Upgrades
                                       					 all SIP profile configurations to rule format. |
|---|---|
| downgrade | downgrades
                                       					 all SIP profile configurations to non-rule format. |

| Release | Modification |
|---|---|
| 15.5(2)T,
                                       					 Cisco IOS-XE Release 3.15S | This
                                       					 command was introduced. |

| Release | Modification |
|---|---|
| Cisco IOS XE Cupertino
                                             17.8.1a | This command was introduced. |

| name | Name of the IP group. Maximum length of the source IP group name is 31 alphanumeric characters. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |

| Command | Description |
|---|---|
| access-list | Defines a list of source groups for identifying incoming calls. |
| carrier-id (voice source group) | Specifies the carrier handling a VoIP call. |
| description (voice source group) | Assigns a disconnect cause to a source IP group. |
| h323zone-id (voice source group) | Assigns a zone ID to an incoming H.323 call. |
| translation-profile (source group) | Assigns a translation profile to a source IP group. |
| trunk-group-label (voice source group) | Specifies the trunk handling a VoIP call. |

| method-list-name | Name of the accounting method list. The method-list-name argument is the same as that configured using the method command in gateway accounting AAA configuration mode. |
|---|---|
| pass | The pass criteria for call legs (PSTN or IP) and call directions (inbound or outbound) that is used by the method list. Note The definition of pass implies that all start, stop, or interim messages are acknowledged by the designated servers. The definition
                                                      of failure implies that any start, stop, or interim message is rejected or is timed out by the designated servers. | Note | The definition of pass implies that all start, stop, or interim messages are acknowledged by the designated servers. The definition
                                                      of failure implies that any start, stop, or interim message is rejected or is timed out by the designated servers. |
| Note | The definition of pass implies that all start, stop, or interim messages are acknowledged by the designated servers. The definition
                                                      of failure implies that any start, stop, or interim message is rejected or is timed out by the designated servers. |
| start-interim-stop | All start, interim, and stop pass criteria records are counted. |
| start-stop | All start and stop pass criteria records are counted. |
| stop-only | Only stop pass criteria records are counted. |

| Note | The definition of pass implies that all start, stop, or interim messages are acknowledged by the designated servers. The definition
                                                      of failure implies that any start, stop, or interim message is rejected or is timed out by the designated servers. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Command | Description |
|---|---|
| method | Specifies the AAA method list name to be used. |
| show voice statistics csr interval accounting | Displays statistical information by configured intervals for accounting statistics. |
| show voice statistics csr since-reset accounting | Displays all accounting CSRs since the last reset. |
| voice statistics display-format separator | Specifies the format for CSR display. |
| voice statistics field-params | Specifies MCD, lost-packet, packet-latency, and packet-jitter parameters. |
| voice statistics max-storage-duration | Specifies the maximum time for which CSRs are stored in system memory. |
| voice statistics push | Specifies an FTP or syslog server for downloading CSRs, the maximum file size, and the maximum message size. |
| voice statistics time-range | Specifies the time range to collect CSRs. |
| voice statistics type | Enables the collection of accounting and signaling CSRs. |

| separator | Type of separator used in the displayed format. |
|---|---|
| space | A space is used for the formatting between each statistic in the displayed output. |
| tab | A tab is used for the formatting between each statistic in the displayed output. |
| new-line | A new line is used for the formatting between each statistic in the displayed output. |
| char char | A character is used for the formatting between each statistic in the displayed output. The char argument is a visible ASCII
                                          character used for the formatting between each statistic in the displayed output. |

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Command | Description |
|---|---|
| voice statistics accounting method | Enables the accounting method and the pass and fail criteria. |
| voice statistics field-params | Specifies MCD, lost-packet, packet-latency, and packet-jitter parameters. |
| voice statistics max-storage-duration | Specifies the maximum time for which CSRs are stored in system memory. |
| voice statistics push | Specifies an FTP or syslog server for downloading CSRs, the maximum file size, and the maximum message size. |
| voice statistics time-range | Specifies the time range to collect CSRs. |
| voice statistics type | Enables the collection of accounting and signaling CSRs. |

| mcd | Minimum call duration. The value argument is an integer that represents the number of milliseconds. Valid values are from
                                          0 to 30. The default is 2. |
|---|---|
| lost-packet | Lost voice packet threshold. The value argument is an integer that represents milliseconds. Valid values are from 0 to 65535.
                                          The default is 1000. |
| packet-latency | Voice packet latency threshold. The value argument is an integer that represents milliseconds. Valid values are from 0 to
                                          500. The default is 250. |
| packet-jitter | Voice packet jitter threshold. The value argument is an integer that represents milliseconds. Valid values are from 0 to 1000.
                                          The default is 250. |

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Command | Description |
|---|---|
| voice statistics accounting method | Enables the accounting method and the pass and fail criteria. |
| voice statistics display-format separator | Specifies the format for CSR display. |
| voice statistics max-storage-duration | Specifies the maximum time for which CSRs are stored in system memory. |
| voice statistics push | Specifies an FTP or syslog server for downloading CSRs, the maximum file size, and the maximum message size. |
| voice statistics time-range | Specifies the time range to collect CSRs. |
| voice statistics type | Enables the collection of accounting and signaling CSRs. |

| day | Number of days for which call statistics data are to be
                                          						stored. The value argument has a valid range from 0 to 365. |
|---|---|
| hour | Number of hours for which call statistics data are to be
                                          						stored. The value argument has a valid range from 0 to 720. |
| minute | Number of minutes for which call statistics data are to be
                                          						stored. The value argument has a valid range from 0 to 1440. |

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Command | Description |
|---|---|
| voice statistics accounting method | Enables the accounting method and the pass and fail
                                          						criteria. |
| voice statistics display-format separator | Specifies the format for CSR display. |
| voice statistics field-params | Specifies MCD, lost-packet, packet-latency, and
                                          						packet-jitter parameters. |
| voice statistics push | Specifies an FTP or syslog server for downloading CSRs, the
                                          						maximum file size, and the maximum message size. |
| voice statistics time-range | Specifies the time range to collect CSRs. |
| voice statistics type | Enables the collection of accounting and signaling CSRs. |

| ftp url | URL of the FTP server to which voice statistics are to be pushed. The syntax of the ftp-url argument follows:
                                          ftp://user:password@host:port//directory1/directory2 |
|---|---|
| max-file-size | (Optional) Maximum size of a voice statistics file to be pushed to an FTP server, in bytes. The valid range of the value argument is from 1024 to 4294967296. The default value is 400000000 (4 GB). |
| syslog | Voice statistics are pushed to a syslog server. |
| max-msg-size | (Optional) Maximum size of a voice statistics file to be pushed to a syslog server, in bytes. The valid range of the value argument is from 1024 to 4294967296. The default value is 400000000 (4 GB). |

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Command | Description |
|---|---|
| voice statistics accounting method | Enables the accounting method and the pass and fail criteria. |
| voice statistics display-format separator | Specifies the format for CSR display. |
| voice statistics field-params | Specifies MCD, lost-packet, packet-latency, and packet-jitter parameters. |
| voice statistics max-storage-duration | Specifies the maximum time for which CSRs are stored in system memory. |
| voice statistics time-range | Specifies the time range to collect CSRs. |
| voice statistics type | Enables the collection of accounting and signaling CSRs. |

| Statistics Collection on a Periodic Basis: |
|---|
| periodic | Call statistics are collected for a configured period. |
| interval | Specifies the periodic interval during which statistics
                                          						will be collected. Valid entries for this value are 5minutes , 15minutes , 30minutes , 60minutes , or 1day . |
| start/end | Specifies the start and ending periods of the statistics
                                          						collection. If no end time is entered, then the statistics collection continues
                                          						nonstop. By default, there is no end of the collection period. |
| hh:mm | Specifies the start and ending times for the periodic
                                          						statistics collection in hours and minutes. The times entered must be in
                                          						24-hour format. |
| days-of-week | Specifies the start and ending days of the week that call
                                          						statistics are collected. You can configure a specific day of the week, or one
                                          						of the following: daily--Call
                                                						  statistics are collected daily. weekdays--Call
                                                						  statistics are collected on weekdays only. weekend--Call
                                                						  statistics are collected on weekends only. The default value is daily. |
| Statistics Collection Since the Last Reset or Reboot of the
                                          						Gateway |
| since-reset | Call statistics are collected only since a reset or reboot
                                          						of the gateway. Note Voice statistics collection on the gateway is reset
                                                      						using the clear voice statistics csr command. | Note | Voice statistics collection on the gateway is reset
                                                      						using the clear voice statistics csr command. |
| Note | Voice statistics collection on the gateway is reset
                                                      						using the clear voice statistics csr command. |
| Statistics Collection at a Specified Time Duration: |
| specific | Call statistics are collected for a specific time duration. |
| start/end | Specifies the start and end times of the statistics
                                          						collection. The required arguments for both the start and end keywords are as
                                          						follows: hh : mm--Hour and minute. The times entered must be in
                                                						  24-hour format. day--Day of the
                                                						  month. Valid values are from 1 to 31. month--Month
                                                						  for the statistics collection to start. Enter the month name, for example,
                                                						  January, or February. The default is the current month. year--Year.
                                                						  Valid values are from 1993 to 2035. The default is the current year. |

| Note | Voice statistics collection on the gateway is reset
                                                      						using the clear voice statistics csr command. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Command | Description |
|---|---|
| clear voice statistics | Clears voice statistics, resetting the statistics
                                          						collection. |
| voice statistics accounting method | Enables the accounting method and the pass and fail
                                          						criteria. |
| voice statistics display-format separator | Specifies the format for CSR display. |
| voice statistics field-params | Specifies MCD, lost-packet, packet-latency, and
                                          						packet-jitter parameters. |
| voice statistics max-storage-duration | Specifies the maximum time for which CSRs are stored in
                                          						system memory. |
| voice statistics push | Specifies an FTP or syslog server for downloading CSRs, the
                                          						maximum file size, and the maximum message size. |
| voice statistics type | Enables the collection of accounting and signaling CSRs. |

| accounting | (Optional) VoIP AAA accounting statistics are collected. |
|---|---|
| signaling | (Optional) Voice signaling statistics are collected. |

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Command | Description |
|---|---|
| voice statistics accounting method | Enables the accounting method and the pass and fail criteria. |
| voice statistics display-format separator | Specifies the format for CSR display. |
| voice statistics field-params | Specifies MCD, lost-packet, packet-latency, and packet-jitter parameters. |
| voice statistics max-storage-duration | Specifies the maximum time for which CSRs are stored in system memory. |
| voice statistics push | Specifies an FTP or syslog server for downloading CSRs, the maximum file size, and the maximum message size. |
| voice statistics time range | Specifies the time range to collect CSRs. |

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| clear voice statistics | Clears voice statistics, resetting the statistics collection. |
| show voice statistics | Displays voice statistics |
| show voice statistics interval-tag | Displays interval options available for IEC statistics |
| voice statistics time-range since-reset | Enables collection of call statistics accumulated since the last resetting of IEC counters |

| name | Name of the translation profile. Maximum length of the voice translation profile name is 31 alphanumeric characters. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |
| Cisco IOS XE Amsterdam 17.2.1r | Introduced support for YANG models. |

| Command | Description |
|---|---|
| rule (voice translation-rule) | Defines call translation criteria. |
| show voice translation-profile | Displays one or more translation profiles. |
| translate (translation profiles) | Associates a translation rule with a voice translation profile. |

| number | Number that identifies the translation rule. Range is from 1 to 2147483647. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |
| Cisco IOS XE Amsterdam 17.2.1r | Introduced support for YANG models. |

| Command | Description |
|---|---|
| rule (voice translation-rule) | Defines the matching, replacement, and rejection patterns for a translation rule. |
| show voice translation-rule | Displays the configuration of a translation rule. |

| milliseconds | Waiting period, in milliseconds, before silence detection and suppression of voice-packet transmission. Range is from 250
                                          to 65536. The default is 250. |
|---|---|

| Release | Modification |
|---|---|
| 12.0(7)XK | This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T. |

| Command | Description |
|---|---|
| vad (dial peer) | Enables voice activity detection on a network dial peer. |

| vrfname | A name assigned to the voice vrf. |
|---|---|

| Release | Modification |
|---|---|
| 12.4(11)XJ | This command was introduced. |
| 12.4(15)T | This command was integrated into Cisco IOS Release 12.4(15)T. |

| Command | Description |
|---|---|
| ip vrf | Defines a VPN VRF instance and enters VRF configuration mode. |

| name | Name of the translation profile. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |

| Command | Description |
|---|---|
| show voice translation-profile | Displays the configurations for all voice translation profiles. |
| test voice translation-rule | Tests the voice translation rule definition. |
| voice translation-profile | Initiates a translation profile definition. |

| name-tag | Tag number by which the rule set is referenced. This is an arbitrarily chosen number. Range is from 1 to 2147483647. There
                                          is no default value. |
|---|---|
| calling | Automatic number identification (ANI) number or the number of the calling party. |
| called | Dial Number Information Service (DNIS) number or the number of the called party. |

| Release | Modification |
|---|---|
| 12.0(7)XR1 | This command was introduced for VoIP on the Cisco AS5300. |
| 12.0(7)XK | This command was implemented for VoIP on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. |
| 12.1(1)T | This command was integrated into Cisco IOS Release 12.1(1)T and implemented for VoIP on the Cisco 1750, Cisco AS5300, Cisco
                                          7200 series, and Cisco 7500 series platforms. |
| 12.1(2)T | This command was implemented for VoIP on Cisco MC3810. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. |

| Command | Description |
|---|---|
| numbering-type | Matches one number type for a dial-peer call leg. |
| rule | Applies a translation rule to a calling party number or a called party number for both incoming and outgoing calls. |
| show translation-rule | Displays the contents of all the rules that have been configured for a specific translation name. |
| test translation-rule | Tests the execution of the translation rules on a specific name-tag. |
| translate | Applies a translation rule to a calling party number or a called party number for incoming calls. |
| translate-outgoing | Applies a translation rule to a calling party number or a called party number for outgoing calls. |
| translation-rule | Creates a translation name and enters translation-rule configuration mode. |

| name | Name of the voip trunk group. Valid names contain a maximum of 63 alphanumeric characters. |
|---|---|

| Release | Modification |
|---|---|
| 15.2(2)T | This command was introduced. |

| Command | Description |
|---|---|
| show voip trunk group | Displays internal list of voip trunk groups. |
| xsvc | Enables monitoring on the trunk. |

| number | A number from 1 to 5 representing decibels (dB) of gain. Range is as follows: 1: -11.99 dB 2: -9.7dB 3: -7.7dB 4: -5.7dB 5: -3.7dB Default is 3 (-7.7 dB gain). |
|---|---|

| Release | Modification |
|---|---|
| 12.2(8)T | This command was introduced on Cisco 803, Cisco 804, and Cisco 813 routers. |

| Note | Only the receiver volume is set with this command. |
|---|---|

| Command | Description |
|---|---|
| show pots volume | Shows the receiver volume configured for each POTS port on a router. |

| Release | Modification |
|---|---|
| 15.0(1)M | This command was introduced in a release earlier than Cisco IOS Release 15.0(1)M. |

| Command | Description |
|---|---|
| vxml audioerror | Enables throwing an error event when audio playout fails. |
| vxml version pre2.0 | Enables VoiceXML 2.0 features. |

| Release | Modification |
|---|---|
| 15.5(3)M7 | This command was introduced in the Cisco IOS Release 15.0(3)M7. |

| Release | Modification |
|---|---|
| 12.4(11)T | This command was introduced. |

| Command | Description |
|---|---|
| vxml version pre2.0 | Enables features compatible with versions earlier than VoiceXML 2.0. |

| size | Maximum memory size, in kilobytes. Range is 64 to 100000. Default is 1000. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(15)T | This command was introduced. |
| 12.4(15)T | The default was changed from 64 to 1000. |

| Note | In Cisco IOS Release 12.3(4)T and later releases, less memory is consumed when parsing a VoiceXML document because the document
                                          is not stored by the VoiceXML tree. |
|---|---|

| Command | Description |
|---|---|
| debug vxml error | Displays VoiceXML application error messages. |
| ivr prompt memory | Sets the maximum amount of memory that dynamic audio files (prompts) occupy in memory. |
| ivr record memory system | Sets the maximum amount of memory for storing all voice recordings on the gateway. |

| Release | Modification |
|---|---|
| 12.4(11)T | This command was introduced. |