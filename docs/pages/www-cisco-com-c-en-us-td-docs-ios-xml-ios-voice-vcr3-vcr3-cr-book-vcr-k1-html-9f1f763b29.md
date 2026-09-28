---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-vcr3-vcr3-cr-book-vcr-k1-html-9f1f763b29
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/vcr3/vcr3-cr-book/vcr-k1.html
retrieved_at: 2026-08-16T23:18:10.866573+00:00
---

Cisco IOS Voice Command Reference - K through R

# Cisco IOS Voice Command Reference - K through R

Updated: December 21, 2024

Chapter: K

## Chapter: K

# K

## keepalive retries

The documentation set for this product strives to use bias-free language. For purposes of this documentation set, bias-free
                                          is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity,
                                          sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language
                                          that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that
                                          is used by a referenced third-party product.

To set the number of keepalive retries from Skinny Client Control Protocol (SCCP) to Cisco Unified CallManager, use the keepalive retries command in SCCP Cisco CallManager configuration mode. To reset this number to the default value, use the no form of this command.

keepalive retries number

no keepalive retries

### Syntax Description

number

Number of keepalive attempts. Range is 1 to 32. Default is 3.

### Command Default

3 keepalive attempts

### Command Modes

SCCP Cisco CallManager configuration

## Command History

Release

Modification

12.3(8)T

This command was introduced.

Cisco IOS XE Amsterdam 17.2.1r

Introduced support for YANG models.

### Usage Guidelines

Use this command to control the number of keepalive retries before SCCP confirms that the Cisco Unified CallManager link is
                              down. When SCCP confirms that the Cisco Unified CallManager link is down (if the number of keepalive messages sent without
                              receiving an Ack reaches the keepalive retries value), Cisco Unified CallManager switchover is initiated.

The optimum setting for this command depends on the platform and your individual network characteristics. Adjust the keepalive
                                          retries to meet your needs.

## Examples

The following example sets the number of times that a Cisco Unified CallManager retries before confirming that the link is
                              down to seven:

Router(conf-sccp-ccm)
                              # keepalive retries 7

### Related Commands

Command

Description

keepalive timeout

Sets the length of time between keepalive messages from SCCP to Cisco Unified CallManager.

sccp ccm group

Creates a Cisco CallManger group and enters the SCCP Cisco CallManager configuration mode.

## keepalive target

To identify Session Initiation Protocol (SIP) servers that will
                              		  receive keepalive packets from the SIP gateway, use the keepalive target command in SIP user-agent configuration mode. To disable the keepalive target command behavior, use the no form of this command.

keepalive target { { { ipv4: address | ipv6: address } [ :port ] | dns: host } |  [ tcp [ tls ]] |  [ udp ] |  [ secondary ]}

no keepalive target [ secondary ]

### Syntax Description

ipv4: address

IP address (in IP version 4 format) of the primary or
                                          						secondary SIP server to monitor.

ipv6: address

IPv6 address of the primary or secondary SIP server to
                                          						monitor.

: port

(Optional) SIP port number. Default SIP port number is
                                          						5060.

dns: hostname

DNS hostname of the primary or secondary SIP server to
                                          						monitor.

tcp

(Optional) Sends keepalive packets over TCP.

tls

(Optional) Sends keepalive packets over Transport Layer
                                          						Security (TLS).

udp

(Optional) Sends keepalive packets over User Datagram
                                          						Protocol (UDP).

secondary

(Optional) Associates the IP version 4 address or the
                                          						domain name system (DNS) hostname to a secondary SIP server to monitor.

### Command Default

No keepalives are sent by default from SIP gateway to SIP gateway.
                              		  The SIP port number is 5060 by default.

### Command Modes

SIP user-agent configuration (config-sip-ua)

## Command History

Release

Modification

12.4(6)T

This command was introduced.

12.4(22)T

Support for IPv6 was added.

### Usage Guidelines

The primary or secondary SIP server addresses are in the following
                              		  forms: dns:example.sip.com or ipv4:172.16.0.10.

## Examples

The following example sets the primary SIP server address and
                              		  defaults to the UDP transport:

```
sip-ua
 keepalive target ipv4:172.16.0.10
```

The following example sets the primary SIP server address and the
                              		  transport to UDP:

```
sip-ua
 keepalive target ipv4:172.16.0.10 udp
```

The following example sets both the primary and secondary SIP server
                              		  address and the transport to UDP:

```
sip-ua
 keepalive target ipv4:172.16.0.10 udp
 keepalive target ipv4:172.16.0.20 udp secondary
```

The following example sets both the primary and secondary SIP server
                              		  addresses and defaults to the UDP transport:

```
sip-ua
 keepalive target ipv4:172.16.0.10
 keepalive target ipv4:172.16.0.20 secondary
```

The following example sets the primary SIP server address and the
                              		  transport to TCP:

```
sip-ua
 keepalive target ipv4:172.16.0.10 tcp
```

The following example sets both the primary and secondary SIP server
                              		  addresses and the transport to TCP:

```
sip-ua
 keepalive target ipv4:172.16.0.10 tcp
 keepalive target ipv4:172.16.0.20 tcp secondary
```

The following example sets the primary SIP server address and the
                              		  transport to TCP and sets security to TLS mode:

```
sip-ua
 keepalive target ipv4:172.16.0.10 tcp tls
```

The following example sets both the primary and secondary SIP server
                              		  addresses and the transport to TCP and sets security to the TLS mode:

```
sip-ua
 keepalive target ipv4:172.16.0.10 tcp tls
 keepalive target ipv4:172.16.0.20 tcp tls secondary
```

### Related Commands

Command

Description

busyout monitor keepalive

Selects a voice port or ports to be busied out in cases of
                                          						a keepalive failure.

keepalive trigger

Sets the trigger count to the number of Options message
                                          						requests that must consecutively receive responses from the SIP servers in
                                          						order to unbusy the voice ports when in the down state.

retry keepalive

Sets the retry keepalive count for retransmission.

timers keepalive

Sets the timers keepalive interval between sending Options
                                          						message requests when the SIP server is active or down.

## keepalive timeout

To set the length of time between keepalive messages from Skinny Client Control Protocol (SCCP) to Cisco Unified CallManager,
                              use the keepalive timeout command in SCCP Cisco CallManager configuration mode. To reset the length of time to the default value, use the no form of this command.

keepalive timeout seconds

no keepalive timeout

### Syntax Description

seconds

Time between keepalive messages. Range is 1 to 180. Default is 30.

### Command Default

30 seconds

### Command Modes

SCCP Cisco CallManager configuration

## Command History

Release

Modification

12.3(8)T

This command was introduced.

Cisco IOS XE Amsterdam 17.2.1r

Introduced support for YANG models.

### Usage Guidelines

Whenever SCCP sends the keepalive message to the Cisco Unified CallManager, it initiates this timer. Once the timeout occurs,
                              it sends the next keepalive message unless the number of keepalive (messages without an Ack) reaches the number set by the keepalive retries command. As of now, the SCCP protocol uses the value provided by the Cisco Unified CallManager.

The optimum setting for this command depends on the platform and your individual network characteristics. Adjust the keepalive
                                          timeout value to meet your needs.

## Examples

The following example sets the length of time between Cisco Unified CallManager keepalive messages to 120 seconds (2 minutes):

Router(config-sccp-ccm)# k eepalive timeout 120

### Related Commands

Command

Description

keepalive retries

Sets the number of keepalive retries from SCCP to Cisco Unified CallManager.

sccp ccm group

Creates a Cisco CallManger group and enters SCCP Cisco CallManager configuration mode.

## keepalive trigger

The trigger count represents the number of Options message requests that must consecutively receive responses from the SIP
                              servers when in the down state in order to unbusy the voice ports, use the keepalive trigger command in SIP user agent configuration mode. To restore to the default value of 3 seconds, use the no form of this command.

keepalive trigger count

no keepalive trigger count

### Syntax Description

count

Keepalive trigger value in the range from 1 to 10. The default value is 3.

### Command Default

The default value for the keepalive trigger is 3.

### Command Modes

SIP user agent configuration

## Command History

Release

Modification

12.4(6)T

This command was introduced.

### Usage Guidelines

Sets the count to represent the number of Options message requests that must be consecutively receive responses from the SIP
                              servers in order to unbusy the voice ports when in the down state. The default is 3.

## Examples

The following example sets a time interval after the number of Options message requests that must consecutively receive responses
                              from the SIP servers in order to unbusy the voice ports when in the down state. The trigger interval is set to 8 in the following
                              example:

```
sip-ua
 keepalive trigger 8
```

### Related Commands

Command

Description

busyout monitor keepalive

Selects a voice port or ports to be busied out in cases of a keepalive failure.

keepalive target

Identifies a SIP server that will receive keepalive packets from the SIP gateway.

retry keepalive

Sets the retry keepalive for retransmission.

timers keepalive

Sets the time interval between sending Options message requests when the SIP server is active or down.

| Note | The documentation set for this product strives to use bias-free language. For purposes of this documentation set, bias-free
                                          is defined as language that does not imply discrimination based on age, disability, gender, racial identity, ethnic identity,
                                          sexual orientation, socioeconomic status, and intersectionality. Exceptions may be present in the documentation due to language
                                          that is hardcoded in the user interfaces of the product software, language used based on RFP documentation, or language that
                                          is used by a referenced third-party product. |
|---|---|

| number | Number of keepalive attempts. Range is 1 to 32. Default is 3. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |
| Cisco IOS XE Amsterdam 17.2.1r | Introduced support for YANG models. |

| Note | The optimum setting for this command depends on the platform and your individual network characteristics. Adjust the keepalive
                                          retries to meet your needs. |
|---|---|

| Command | Description |
|---|---|
| keepalive timeout | Sets the length of time between keepalive messages from SCCP to Cisco Unified CallManager. |
| sccp ccm group | Creates a Cisco CallManger group and enters the SCCP Cisco CallManager configuration mode. |

| ipv4: address | IP address (in IP version 4 format) of the primary or
                                          						secondary SIP server to monitor. |
|---|---|
| ipv6: address | IPv6 address of the primary or secondary SIP server to
                                          						monitor. |
| : port | (Optional) SIP port number. Default SIP port number is
                                          						5060. |
| dns: hostname | DNS hostname of the primary or secondary SIP server to
                                          						monitor. |
| tcp | (Optional) Sends keepalive packets over TCP. |
| tls | (Optional) Sends keepalive packets over Transport Layer
                                          						Security (TLS). |
| udp | (Optional) Sends keepalive packets over User Datagram
                                          						Protocol (UDP). |
| secondary | (Optional) Associates the IP version 4 address or the
                                          						domain name system (DNS) hostname to a secondary SIP server to monitor. |

| Release | Modification |
|---|---|
| 12.4(6)T | This command was introduced. |
| 12.4(22)T | Support for IPv6 was added. |

| Command | Description |
|---|---|
| busyout monitor keepalive | Selects a voice port or ports to be busied out in cases of
                                          						a keepalive failure. |
| keepalive trigger | Sets the trigger count to the number of Options message
                                          						requests that must consecutively receive responses from the SIP servers in
                                          						order to unbusy the voice ports when in the down state. |
| retry keepalive | Sets the retry keepalive count for retransmission. |
| timers keepalive | Sets the timers keepalive interval between sending Options
                                          						message requests when the SIP server is active or down. |

| seconds | Time between keepalive messages. Range is 1 to 180. Default is 30. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(8)T | This command was introduced. |
| Cisco IOS XE Amsterdam 17.2.1r | Introduced support for YANG models. |

| Note | The optimum setting for this command depends on the platform and your individual network characteristics. Adjust the keepalive
                                          timeout value to meet your needs. |
|---|---|

| Command | Description |
|---|---|
| keepalive retries | Sets the number of keepalive retries from SCCP to Cisco Unified CallManager. |
| sccp ccm group | Creates a Cisco CallManger group and enters SCCP Cisco CallManager configuration mode. |

| count | Keepalive trigger value in the range from 1 to 10. The default value is 3. |
|---|---|

| Release | Modification |
|---|---|
| 12.4(6)T | This command was introduced. |

| Command | Description |
|---|---|
| busyout monitor keepalive | Selects a voice port or ports to be busied out in cases of a keepalive failure. |
| keepalive target | Identifies a SIP server that will receive keepalive packets from the SIP gateway. |
| retry keepalive | Sets the retry keepalive for retransmission. |
| timers keepalive | Sets the time interval between sending Options message requests when the SIP server is active or down. |