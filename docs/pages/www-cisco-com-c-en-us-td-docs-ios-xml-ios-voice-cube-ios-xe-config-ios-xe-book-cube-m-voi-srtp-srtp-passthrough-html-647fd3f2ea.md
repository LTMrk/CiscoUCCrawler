---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-cube-m-voi-srtp-srtp-passthrough-html-647fd3f2ea
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/cube_m_voi-srtp-srtp-passthrough.html
retrieved_at: 2026-08-16T15:52:47.677276+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: SRTP-SRTP Pass-Through

## Chapter: SRTP-SRTP Pass-Through

# SRTP-SRTP Pass-Through

## Overview

SRTP-SRTP pass-through feature
                           		allows pass-through of encrypted media from one call-leg to the other.

Cisco Unified Border Element (CUBE) supports SIP calls between endpoints using Transport Layer Security (TLS) for SIP signaling encryption and Secure Real-Time
                           Protocol (SRTP) to provide RTP media encryption. However, these two encryption mechanisms may not be deployed simultaneously,
                           depending on the required call flow invoked on the associated configuration.

The following are conditions of the SRTP Passthrough feature:

SRTP Passthrough must be configured on both legs of the call. If the target adjacency does not support SRTP Passthrough, then
                                 the call is rejected by error message 415 (Unsupported Media Type).

"m= .. RTP/SAVP .." and a="crypto:..." fields coming in on an Invite from one adjacency are passed on in an Invite to the
                                 target adjacency.

"m= ...RTP/SAVP..." is a required field in the Invite to trigger SRTP Passthrough behavior in the CUBE .

### Pass-Through of
                           	 Unsupported Crypto Suites

CUBE supports transparent passthrough of all (supported and unsupported) crypto suites.

CUBE has the ability to pass across crypto attributes (containing any unsupported crypto suites) as well as media packets (encrypted
                              with unsupported crypto suites).

If SRTP pass-thru feature is enabled, media interworking will not be
                              		supported. Ensure that you have symmetric configuration on both the incoming
                              		and outgoing dial-peers to avoid media-related issues.

### Feature Information

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature
                                             					 Name

Releases

Feature
                                             					 Information

Support
                                             					 for SRTP-SRTP Basic calls

Baseline functionality

This
                                             					 feature introduced support for basic SRTP-SRTP pass-through calls.

## Configure
                        	 Pass-Through of Unsupported Crypto Suites for a Specific Dial Peer

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice tag voip

- destination-pattern string

- session protocol sipv2

- session target ipv4: destination-address

- incoming called-number string

- srtp
                                    				  pass-thru

- codec codec

- end

- dial-peer voice tag voip

- Repeat
                              			 Steps 4, 5, 6, and 7 to configure a second dial peer.

- srtp
                                    				  pass-thru

- codec codec

- exit

### DETAILED STEPS

Step 1

enable

### Example:

```
Device> enable
```

Enables
                                          				privileged EXEC mode.

Enter
                                                					 your password if prompted.

Step 2

configure terminal

### Example:

```
Device# configure terminal
```

Enters global configuration mode.

Step 3

dial-peer voice tag voip

### Example:

```
Device(config)# dial-peer voice 201 voip
```

Defines a particular dial peer, to specify the method of voice encapsulation, and enters dial peer voice configuration mode.

Dial peer 201 is defined.

VoIP is shown as the method of encapsulation.

Step 4

destination-pattern string

### Example:

```
Device(config-dial-peer)# destination-pattern 5550111
```

Specifies either the prefix or the full E.164 telephone number to be used for a dial peer string.

In the example, 5550111 is specified as the pattern for the telephone number.

Step 5

session protocol sipv2

### Example:

```
Device(config-dial-peer)# session protocol sipv2
```

Specifies a session protocol for calls between local and remote routers using the packet network.

In the example, the sipv2 keyword is configured so that the dial peer uses the IETF SIP.

Step 6

session target ipv4: destination-address

### Example:

```
Device(config-dial-peer)# session target ipv4:10.13.25.102
```

Designates a network-specific address to receive calls from a VoIP or VoIPv6 dial peer.

In the example, the IP address of the dial peer to receive calls is configured as 10.13.25.102.

Step 7

incoming called-number string

### Example:

```
Device(config-dial-peer)# incoming called-number 5550111
```

Specifies a digit string that can be matched by an incoming call to associate the call with a dial peer.

In the example, 5550111 is specified as the pattern for the E.164 or private dialing plan telephone number.

Step 8

srtp
                                             				  pass-thru

### Example:

```
Device(config-dial-peer)# srtp pass-thru
```

Enables
                                          				transparent passthrough of all crypto suites for a specific dial peer.

Step 9

codec codec

### Example:

```
Device(config-dial-peer)# codec g711ulaw
```

Specifies the voice coder rate of speech for the dial peer.

In the example, G.711 mu-law at 64,000 bps, is specified as the voice coder rate for speech.

Step 10

end

### Example:

```
Device(config-dial-peer)# end
```

Exits dial
                                          				peer voice configuration mode.

Step 11

dial-peer voice tag voip

### Example:

```
Device(config)# dial-peer voice 200 voip
```

Defines a particular dial peer, to specify the method of voice encapsulation, and enters dial peer voice configuration mode.

- Dial peer 200 is defined.

- VoIP is shown as the method of encapsulation.

Step 12

Repeat
                                       			 Steps 4, 5, 6, and 7 to configure a second dial peer.

--

Step 13

srtp
                                             				  pass-thru

### Example:

```
Device(config-dial-peer)# srtp pass-thru
```

Enables
                                          				transparent passthrough of all crypto suites for a specific dial peer.

Step 14

codec codec

### Example:

```
Device(config-dial-peer)# codec g711ulaw
```

Specifies the voice coder rate of speech for the dial peer.

In the example, G.711 mu-law at 64,000 bps, is specified as the voice coder rate for speech.

Step 15

exit

### Example:

```
Device(config-dial-peer)# exit
```

Exits dial
                                          				peer voice configuration mode.

## Configure
                        	 Pass-Through of Unsupported Crypto Suites Globally

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- srtp pass-thru

- end

### DETAILED STEPS

Step 1

enable

### Example:

```
Device> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Device# configure terminal
```

Enters global configuration mode.

Step 3

voice service voip

### Example:

```
Device(config)# voice service voip
```

Enters VoIP voice-service configuration mode.

Step 4

srtp pass-thru

### Example:

```
Device(config-dial-peer)# srtp pass-thru
```

Enables transparent passthrough of all crypto suites globally.

Step 5

end

### Example:

```
Device(config-dial-peer)# end
```

Exits dial peer voice configuration mode.

## Configuration
                        	 Examples for SRTP-SRTP Pass-Through

Example for SRTP=SRTP
                              		  Pass-Through

```
enable
configure terminal
dial-peer voice 201 voip
destination-pattern 5550111
session protocol sipv2
session target ipv4:10.13.25.102
incoming called-number 5550111
srtp
codec g711ulaw
end

dial-peer voice 200 voip
destination-pattern 5550111
session protocol sipv2
session target ipv4:10.13.25.101
incoming called-number 5550111
srtp
codec g711ulaw
end
```

Example for Pass-Through of Unsupported Crypto Suites for a specific
                              		  dial peer

```
enable
configure terminal
dial-peer voice 201 voip
destination-pattern 5550111
session protocol sipv2
session target ipv4:10.13.25.102
incoming called-number 5550111
srtp pass-thru
codec g711ulaw
end

dial-peer voice 200 voip
destination-pattern 5550111
session protocol sipv2
session target ipv4:10.13.25.101
incoming called-number 5550111
srtp pass-thru
codec g711ulaw
end
```

Example for Pass-Through of Unsupported Crypto Suites Globally

```
enable
configure terminal
voice service voip
srtp pass-thru
end
```

| Note | Effective from Cisco IOS XE Everest Release 16.5.1b, CUBE supports AEAD_AES_128_GCM and AEAD_AES_256_GCM crypto-suites. For more information, see SRTP-SRTP Interworking . |
|---|---|

| Feature
                                             					 Name | Releases | Feature
                                             					 Information |
|---|---|---|
| Support
                                             					 for SRTP-SRTP Basic calls | Baseline functionality | This
                                             					 feature introduced support for basic SRTP-SRTP pass-through calls. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables
                                          				privileged EXEC mode. Enter
                                                					 your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | dial-peer voice tag voip Example: Device(config)# dial-peer voice 201 voip | Defines a particular dial peer, to specify the method of voice encapsulation, and enters dial peer voice configuration mode. In the example, the following parameters are set: Dial peer 201 is defined. VoIP is shown as the method of encapsulation. |
| Step 4 | destination-pattern string Example: Device(config-dial-peer)# destination-pattern 5550111 | Specifies either the prefix or the full E.164 telephone number to be used for a dial peer string. In the example, 5550111 is specified as the pattern for the telephone number. |
| Step 5 | session protocol sipv2 Example: Device(config-dial-peer)# session protocol sipv2 | Specifies a session protocol for calls between local and remote routers using the packet network. In the example, the sipv2 keyword is configured so that the dial peer uses the IETF SIP. |
| Step 6 | session target ipv4: destination-address Example: Device(config-dial-peer)# session target ipv4:10.13.25.102 | Designates a network-specific address to receive calls from a VoIP or VoIPv6 dial peer. In the example, the IP address of the dial peer to receive calls is configured as 10.13.25.102. |
| Step 7 | incoming called-number string Example: Device(config-dial-peer)# incoming called-number 5550111 | Specifies a digit string that can be matched by an incoming call to associate the call with a dial peer. In the example, 5550111 is specified as the pattern for the E.164 or private dialing plan telephone number. |
| Step 8 | srtp
                                             				  pass-thru Example: Device(config-dial-peer)# srtp pass-thru | Enables
                                          				transparent passthrough of all crypto suites for a specific dial peer. |
| Step 9 | codec codec Example: Device(config-dial-peer)# codec g711ulaw | Specifies the voice coder rate of speech for the dial peer. In the example, G.711 mu-law at 64,000 bps, is specified as the voice coder rate for speech. |
| Step 10 | end Example: Device(config-dial-peer)# end | Exits dial
                                          				peer voice configuration mode. |
| Step 11 | dial-peer voice tag voip Example: Device(config)# dial-peer voice 200 voip | Defines a particular dial peer, to specify the method of voice encapsulation, and enters dial peer voice configuration mode. In the example, the following parameters are set: Dial peer 200 is defined. VoIP is shown as the method of encapsulation. |
| Step 12 | Repeat
                                       			 Steps 4, 5, 6, and 7 to configure a second dial peer. | -- |
| Step 13 | srtp
                                             				  pass-thru Example: Device(config-dial-peer)# srtp pass-thru | Enables
                                          				transparent passthrough of all crypto suites for a specific dial peer. |
| Step 14 | codec codec Example: Device(config-dial-peer)# codec g711ulaw | Specifies the voice coder rate of speech for the dial peer. In the example, G.711 mu-law at 64,000 bps, is specified as the voice coder rate for speech. |
| Step 15 | exit Example: Device(config-dial-peer)# exit | Exits dial
                                          				peer voice configuration mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | voice service voip Example: Device(config)# voice service voip | Enters VoIP voice-service configuration mode. |
| Step 4 | srtp pass-thru Example: Device(config-dial-peer)# srtp pass-thru | Enables transparent passthrough of all crypto suites globally. |
| Step 5 | end Example: Device(config-dial-peer)# end | Exits dial peer voice configuration mode. |