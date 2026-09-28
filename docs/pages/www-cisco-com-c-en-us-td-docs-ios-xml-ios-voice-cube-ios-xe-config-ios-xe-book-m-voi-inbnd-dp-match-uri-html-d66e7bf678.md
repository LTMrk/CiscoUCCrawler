---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-inbnd-dp-match-uri-html-d66e7bf678
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-inbnd-dp-match-uri.html
retrieved_at: 2026-08-16T15:45:38.125426+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Matching Inbound Dial Peers by URI of Incoming SIP Calls

## Chapter: Matching Inbound Dial Peers by URI of Incoming SIP Calls

# Matching Inbound Dial Peers by URI of Incoming SIP Calls

## Inbound Dial Peer Matching (by URI)

The inbound dial peer matching by URI feature allows you to configure the selection of inbound dial peers by matching parts
                           of the URI sent by a remote (neighboring) SIP entity. The match is done on different parts of the URI like username, IP address,
                           and DNS. This feature configures configuration policies, enforce specific call-treatment, security, and routing policies on
                           each SIP trunk by originating SIP entity.

In a scenario where multiple SIP hops are involved in a call, there would be multiple via headers that are involved, and the
                           topmost via header of an incoming SIP invite represents the last hop that forwarded the SIP request, and the bottom-most via
                           header would represent the originator of the SIP request. This feature supports matching by the last hop that forwarded the
                           request (neighboring SIP entity), which is the topmost via header.

For incoming dial-peer match based on URI, if there are multiple dial-peers matches, then the longest matching dial-peer is
                                       chosen (similar to multiple dial-peers match based on an incoming called number). However for the URI pattern match, there
                                       is no match length and hence this is the least preferred.

### Feature Information

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature
                                          					 Information

Inbound
                                          					 Dial-peer Match Based on Remote IP Address on SIP Trunks

Baseline Functionality

This feature was implemented on the Cisco Unified Border Element.

The
                                          					 following commands were introduced or modified: dial-peer voice , voice-class uri .

## Configure an Inbound Dial Peer to Match on URI

### SUMMARY STEPS

- enable

- configure terminal

- voice class uri voice-class-uri-tag

- Specify a URI field for the voice class:

- host hostname-pattern

- host ipv4: ipv4-address

- host ipv6: ipv6-address

- host dns: dns-address

- pattern uri-pattern

- user-id username-pattern

- exit

- dial-peer voice tag voip

- session protocol sipv2

- incoming uri { from | request | to | via } voice-class-uri-tag

- end

### DETAILED STEPS

Step 1

enable

### Example:

```
Device> enable
```

Enables
                                          				privileged EXEC mode.

Enter your
                                                					 password if prompted.

Step 2

configure terminal

### Example:

```
Device> configure terminal
```

Enters global
                                          				configuration mode.

Step 3

voice class uri voice-class-uri-tag

### Example:

```
Device(config)# voice class uri 200
```

Creates voice class for matching SIP dial peers and enters a voice URI class configuration mode.

Step 4

Specify a URI field for the voice class:

- host hostname-pattern

- host ipv4: ipv4-address

- host ipv6: ipv6-address

- host dns: dns-address

- pattern uri-pattern

- user-id username-pattern

### Example:

```
Device(config-voice-uri-class)# host server1
```

### Example:

```
Device(config-voice-uri-class)# host ipv4:10.0.0.0
```

### Example:

```
Device(config-voice-uri-class)# host dns:xxx.yyy.com
```

You can specify up to ten instances of the host ipv4: , host ipv6: , and host dns: commands.

You can specify only one instance of the host hostname-pattern commands.

Length of uri-pattern , username-pattern , and hostname-pattern must be less than 32.

username-pattern is matched against the username field of the URI.

hostname-pattern is matched against the host field of the URI.

uri-pattern is matched against the entire URI.

Only one instance of the pattern and host commands is possible.

Patterns are case-sensitive.

Step 5

exit

### Example:

```
Device(config-voice-uri-class)# exit
```

Enters global
                                          				configuration mode.

Step 6

dial-peer voice tag voip

### Example:

```
Device(config)# dial-peer voice 6000 voip
```

Enters dial peer
                                          				voice configuration mode.

Step 7

session protocol sipv2

### Example:

```
Device(config-dial-peer)# session protocol sipv2
```

Configures SIP
                                          				as the session protocol type.

Step 8

incoming uri { from | request | to | via } voice-class-uri-tag

### Example:

```
Device(config-dial-peer)# incoming uri via 200
```

Configures the
                                          				voice class with an inbound dial peer, so that it is matches against configured
                                          				URI fields.

Step 9

end

### Example:

```
Device(config-dial-peer)# end
```

Exits dial
                                          				peer voice configuration mode and enters privileged EXEC mode.

## Examples for
                        	 Configuring an Inbound Dial Peer to Match on a URI

### Matching
                              		  Against IPv4 Address and VIA

CUBE is configured
                              		  to use incoming dial-peer 101 for incoming SIP calls from remote SIP endpoint
                              		  having an IP address of 10.10.10.1

```
voice class uri 201 sip
host ipv4:10.10.10.1
 
dial-peer voice 101 voip
 session protocol sipv2
 incoming uri via 201
```

Incoming INVITE
                              		  that can be matched against this dial peer.

```
INVITE sip:123@1.2.3.4:5060 SIP/2.0 Via: SIP/2.0/TCP 10.10.10.1:5093;branch=z9hG4bK-17716-1-0 Via: SIP/2.0/TCP 10.10.14.20:5093;branch=z9hG4bK-28280-1-0
```

### Matching
                              		  Against DNS Name and VIA

CUBE is configured
                              		  to use incoming dial-peer 102 for incoming SIP calls from sample.com or an IP
                              		  address that represents one of the resolved IP address of sample.com.

```
voice class uri 202 sip
host dns:sample.com
 
dial-peer voice 101 voip
 session protocol sipv2
 incoming uri via 202
```

Incoming INVITE
                              		  that can be matched against this dial peer.

```
INVITE sip:123@1.2.3.4:5060 SIP/2.0 Via: SIP/2.0/TCP sample.com;branch=z9hG4bK-17716-1-0
```

```
INVITE sip:123@1.2.3.4:5060 SIP/2.0 Via: SIP/2.0/TCP 10.10.10.25:5093;branch=z9hG4bK-17716-1-0
```

10.10.10.25 is a
                              		  resolved IP address of sample.com.

### Matching
                              		  Against Multiple Attributes and VIA

CUBE is configured
                              		  to use incoming dial-peer 103 for incoming SIP calls from xxx.yyy.com,
                              		  abc.def.com and IP addresses 10.10.10.10, 10.9.10.11 and 10.10.10.10.

```
voice class uri 203 sip
  host dns:xxx.yyy.com
  host dns:abc.def.com
  host ipv4:10.10.10.10
  host ipv4:10.9.10.11
  host ipv4:10.10.10.10

dial-peer voice 103 voip
 session protocol sipv2
 incoming uri via 203
```

Incoming INVITE
                              		  that can be matched against this dial peer.

```
INVITE sip:123@1.2.3.4:5060 SIP/2.0 Via: SIP/2.0/TCP 10.10.10.10:5093;branch=z9hG4bK-17716-1-0 Via: SIP/2.0/TCP 10.10.14.20:5093;branch=z9hG4bK-28280-1-0
```

10.10.10.25 is a
                              		  resolved IP address of sample.com.

| Note | For incoming dial-peer match based on URI, if there are multiple dial-peers matches, then the longest matching dial-peer is
                                       chosen (similar to multiple dial-peers match based on an incoming called number). However for the URI pattern match, there
                                       is no match length and hence this is the least preferred. |
|---|---|

| Feature Name | Releases | Feature
                                          					 Information |
|---|---|---|
| Inbound
                                          					 Dial-peer Match Based on Remote IP Address on SIP Trunks | Baseline Functionality | This feature was implemented on the Cisco Unified Border Element. The
                                          					 following commands were introduced or modified: dial-peer voice , voice-class uri . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables
                                          				privileged EXEC mode. Enter your
                                                					 password if prompted. |
| Step 2 | configure terminal Example: Device> configure terminal | Enters global
                                          				configuration mode. |
| Step 3 | voice class uri voice-class-uri-tag Example: Device(config)# voice class uri 200 | Creates voice class for matching SIP dial peers and enters a voice URI class configuration mode. |
| Step 4 | Specify a URI field for the voice class: host hostname-pattern host ipv4: ipv4-address host ipv6: ipv6-address host dns: dns-address pattern uri-pattern user-id username-pattern Example: Device(config-voice-uri-class)# host server1 Example: Device(config-voice-uri-class)# host ipv4:10.0.0.0 Example: Device(config-voice-uri-class)# host dns:xxx.yyy.com | You can specify up to ten instances of the host ipv4: , host ipv6: , and host dns: commands. You can specify only one instance of the host hostname-pattern commands. Length of uri-pattern , username-pattern , and hostname-pattern must be less than 32. username-pattern is matched against the username field of the URI. hostname-pattern is matched against the host field of the URI. uri-pattern is matched against the entire URI. Only one instance of the pattern and host commands is possible. Note Patterns are case-sensitive. | Note | Patterns are case-sensitive. |
| Note | Patterns are case-sensitive. |
| Step 5 | exit Example: Device(config-voice-uri-class)# exit | Enters global
                                          				configuration mode. |
| Step 6 | dial-peer voice tag voip Example: Device(config)# dial-peer voice 6000 voip | Enters dial peer
                                          				voice configuration mode. |
| Step 7 | session protocol sipv2 Example: Device(config-dial-peer)# session protocol sipv2 | Configures SIP
                                          				as the session protocol type. |
| Step 8 | incoming uri { from \| request \| to \| via } voice-class-uri-tag Example: Device(config-dial-peer)# incoming uri via 200 | Configures the
                                          				voice class with an inbound dial peer, so that it is matches against configured
                                          				URI fields. |
| Step 9 | end Example: Device(config-dial-peer)# end | Exits dial
                                          				peer voice configuration mode and enters privileged EXEC mode. |

| Note | Patterns are case-sensitive. |
|---|---|