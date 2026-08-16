---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-sip-supp-uri-based-dialing-html-2134c0f466
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/sip-supp-uri-based-dialing.html
retrieved_at: 2026-08-16T15:45:43.126216+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: URI-Based Dialing Enhancements

## Chapter: URI-Based Dialing Enhancements

# URI-Based Dialing Enhancements

## Overview

The URI Dialing feature describes the enhancements that are made to Uniform Resource Identifier (URI)-based dialing on Cisco Unified Border Element (CUBE) for Session Initiation Protocol (SIP) calls. The URI-Based Dialing Enhancements feature includes support for call routing
                           on CUBE when the User Part of the incoming Request-URI is non-E164 (for example, INVITE sip:user@abc.com).

Cisco Unified Communications Manager supports dialing using directory Uniform Resource Identifiers (URIs) for call addressing.
                           Directory URIs follow the username@host format where the host portion is an IPv4 address or a fully qualified domain name.
                           Use a directory URI to identify a directory number. Assign that directory number to a phone, so that Unified Communications
                           Manager can route calls to that phone using the directory URI. URI dialing is available for Session Initiation Protocol (SIP)
                           and Signaling Connection Control Part (SCCP) endpoints that support directory URIs.

The URI Dialing feature extends support for CUBE URI routing of calls. With these enhancements CUBE supports:

URI routing when the User Part of the incoming Request-URI is non-E164 (for example, INVITE sip:user@abc.com).

URI routing when the User Part is not present. The User Part is an optional parameter in the URI (for example, INVITE sip:
                                 abc.com).

Copying the outgoing Request-URI and To header from the inbound Request-URI and To header respectively.

Deriving (optionally) the session target for the outbound dial peer from the host portion of the inbound URI.

URI routing for 302, Refer, and Bye Also scenarios.

Call hunting where the subsequent dial peer is selected based on URI.

Pass through of 302, with the host part of Contact: unmodified.

The minimum supported release of Cisco IOS required for URI-based call routing on dial-peers is Cisco IOS XE Gibraltar Release
                                       16.12. You must configure the 'call-route-url' on the outgoing dial-peers to properly route the refer-to headers based on
                                       the URI matching.

### Feature Information

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature
                                             					 Name

Releases

Feature
                                             					 Information

URI-Based
                                             					 Dialing Enhancements

The following commands were introduced or modified: contact-passing , requri-passing , session target
                                                   						  sip-uri and voice-class sip requri-passing

### Call Flows for
                           	 URI-Based Dialing Enhancements

Case1: URI dialing with username being E164 or non-E164 number and Request-URI host copied from the inbound leg.

Case 2: Incoming Request-URI does not contain user part. The To: header information is also copied from the peer leg when
                              the requri-passing command is enabled.

Case 3: The old behavior of setting the outbound Request-URI to session target is retained when the requri-passing command is not enabled.

Case 4: The session target derived from the host part of the URI. The outgoing INVITE is sent to resolved IP address of the
                              host part of the URI.

Case 5: Pass through of contact URI to request URI.

Case 6: In 302 pass-through, contact header can be passed through from one leg to another by using the contact-passing command.

Case 7: Pass through of refer-to URI to request URI.

Case 8: URI routing based on BYE Also header.

## Configure URI Dialing

### Configure Pass Through of SIP URI Headers

Perform these tasks to configure the pass through of the host part of the Request-Uniform Resource Identifier (URI) and To
                              Session Initiation Protocol (SIP) headers. By default, CUBE sets the host part of the URI to the value configured under the session target of the outbound dial peer. For more information,
                              see Case 1 in the "Call Flows for URI Dialing" section.

#### Configure Pass Though of Request URI and To Header URI (Global Level)

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- sip

- requri-passing

- end

### DETAILED STEPS

Step 1

enable

##### Example:

```
Device> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

##### Example:

```
Device# configure terminal
```

Enters global
                                                				configuration mode.

Step 3

voice service voip

##### Example:

```
Device(config)# voice service voip
```

Specifies
                                                				VoIP encapsulation and enters voice service configuration mode.

Step 4

sip

##### Example:

```
Device(conf-voi-serv)# sip
```

Enters the
                                                				Session Initiation Protocol (SIP) configuration mode.

Step 5

requri-passing

##### Example:

```
Router(conf-serv-sip)# requri-passing
```

Enables pass through of the host part of the Request-URI and To SIP headers. By default, CUBE sets the host part of the URI to the value configured under the session target of the outbound dial peer.

Step 6

end

##### Example:

```
Router(conf-serv-sip)# end
```

Ends the
                                                				current configuration session and returns to privileged EXEC mode.

#### Configure Pass Though of Request URI and to Header URI (Dial Peer Level)

### SUMMARY STEPS

- enable

- configure terminal

- voice class uri tag sip

- host hostname-pattern

- exit

- dial-peer voice tag voip

- session protocol sipv2

- destination uri tag

- session target ipv4: ip-address

- voice-class sip requri-passing [ system ]

- end

### DETAILED STEPS

Step 1

enable

##### Example:

```
Device> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

##### Example:

```
Device# configure terminal
```

Enters global
                                                				configuration mode.

Step 3

voice class uri tag sip

##### Example:

```
Device(config)# voice class uri mydesturi sip
```

Creates a
                                                				voice class for matching dial peers to a Session Initiation Protocol (SIP) and
                                                				enters voice URI class configuration mode.

Step 4

host hostname-pattern

##### Example:

```
Device(config-voice-uri-class)# host example.com
```

Matches a
                                                				call based on the host field in a SIP Uniform Resource Identifier (URI).

Step 5

exit

##### Example:

```
Device(config-voice-uri-class)# exit
```

Exits voice
                                                				URI class configuration mode.

Step 6

dial-peer voice tag voip

##### Example:

```
Device(config)# dial-peer voice 22 voip
```

Defines a
                                                				VoIP dial peer and enters dial peer configuration mode.

Step 7

session protocol sipv2

##### Example:

```
Device(config-dial-peer)# session protocol sipv2
```

Specifies a
                                                				session protocol for calls between local and remote routers using the Internet
                                                				Engineering Task Force (IETF) SIP.

Step 8

destination uri tag

##### Example:

```
Device(config)# destination uri mydesturi
```

Specifies the voice class that is used to match a dial peer to the destination URI of an outgoing call.

Step 9

session target ipv4: ip-address

##### Example:

```
Device(config-dial-peer)# session target ipv4:10.1.1.2
```

Designates
                                                				a network-specific address to receive calls from a VoIP.

Step 10

voice-class sip requri-passing [ system ]

##### Example:

```
Device(config-dial-peer)# voice-class sip requri-passing system
```

Enables the
                                                				pass through of SIP URI headers.

Step 11

end

##### Example:

```
Device(config-dial-peer)# end
```

Ends the
                                                				current configuration session and returns to privileged EXEC mode.

### Configure Pass Through of 302 Contact Header

#### Configure Pass Through of 302 Contact Header (Global Level)

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- sip

- contact-passing

- end

### DETAILED STEPS

Step 1

enable

##### Example:

```
Device> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

##### Example:

```
Device# configure terminal
```

Enters global
                                                				configuration mode.

Step 3

voice service voip

##### Example:

```
Device(config)# voice service voip
```

Specifies
                                                				VoIP encapsulation and enters voice service configuration mode.

Step 4

sip

##### Example:

```
Device(conf-voi-serv)# sip
```

Enters voice
                                                				service SIP configuration mode.

Step 5

contact-passing

##### Example:

```
Router(conf-serv-sip)# contact-passing
```

Enables pass
                                                				through of the contact header from one leg to the other leg in 302 pass through
                                                				scenario.

Step 6

end

##### Example:

```
Router(conf-serv-sip)# end
```

Ends the
                                                				current configuration session and returns to privileged EXEC mode.

#### Configure Pass Through of 302 Contact Header (Dial Peer Level)

### SUMMARY STEPS

- enable

- configure terminal

- voice class uri destination-tag sip

- user-id id-tag

- exit

- voice service voip

- allow-connections sip to sip

- dial-peer voice tag voip

- session protocol sipv2

- destination uri destination-tag

- voice-class sip contact-passing

- end

### DETAILED STEPS

Step 1

enable

##### Example:

```
Device> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

##### Example:

```
Device# configure terminal
```

Enters global
                                                				configuration mode.

Step 3

voice class uri destination-tag sip

##### Example:

```
Device(config)# voice class uri mydesturi sip
```

Creates a
                                                				voice class for matching dial peers to a Session Initiation Protocol (SIP) and
                                                				enters voice URI class configuration mode.

Step 4

user-id id-tag

##### Example:

```
Device(config-voice-uri-class)# user-id 5678
```

Matches a
                                                				call based on the User ID portion of the Uniform Resource Identifier (URI).

Step 5

exit

##### Example:

```
Device(config-voice-uri-class)# exit
```

Exits voice
                                                				URI class configuration mode.

Step 6

voice service voip

##### Example:

```
Device(config)# voice service voip
```

Specifies
                                                				Voice over IP (VoIP) as the voice encapsulation type and enters voice service
                                                				configuration mode.

Step 7

allow-connections sip to sip

##### Example:

```
Device(conf-voi-serv)# allow-connections sip to sip
```

Allows
                                                				connections between SIP endpoints in a VoIP network.

Step 8

dial-peer voice tag voip

##### Example:

```
Device(config)# dial-peer voice 200 voip
```

Defines a
                                                				VoIP dial peer and enters dial peer configuration mode.

Step 9

session protocol sipv2

##### Example:

```
Device(config-dial-peer)# session protocol sipv2
```

Specifies a
                                                				session protocol for calls between local and remote routers using the Internet
                                                				Engineering Task Force (IETF) SIP.

Step 10

destination uri destination-tag

##### Example:

```
Device(config-dial-peer)# destination uri mydesturi
```

Specifies
                                                				the voice class used to match a dial peer to the destination URI of an outgoing
                                                				call.

Step 11

voice-class sip contact-passing

##### Example:

```
Device(config-dial-peer)# voice-class sip contact-passing
```

Enables pass
                                                				through of the contact header from one leg to the other leg in 302 pass through
                                                				scenario.

Step 12

end

##### Example:

```
Device(config-dial-peer)# end
```

Ends the
                                                				current configuration session and returns to privileged EXEC mode.

### Derive the Session Target from URI

Perform this
                                 		  task to derive the session target from the host part of the Uniform Resource
                                 		  Identifier (URI). The outgoing INVITE is sent to the resolved IP address of the
                                 		  host part of the URI. For more information, see Case 4 in the "Call Flows for
                                 		  URI-Based Dialing Enhancements" section.

### SUMMARY STEPS

- enable

- configure terminal

- voice class uri destination-tag sip

- host hostname-pattern

- exit

- dial-peer voice tag voip

- session protocol sipv2

- destination uri destination-tag

- session target sip-uri

- exit

- voice class uri source-tag sip

- host hostname-pattern

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Device# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice class uri destination-tag sip

#### Example:

```
Device(config)# voice class uri mydesturi sip
```

Creates or
                                             				modifies a voice class for matching dial peers to a Session Initiation Protocol
                                             				(SIP) or telephone (TEL) Uniform Resource Identifier (URI) and enters voice URI
                                             				class configuration mode.

Step 4

host hostname-pattern

#### Example:

```
Device(config-voice-uri-class)# host destination.com
```

Matches a
                                             				call based on the host field in a SIP URI.

Step 5

exit

#### Example:

```
Device(config-voice-uri-class)# exit
```

Exits voice
                                             				URI class configuration mode.

Step 6

dial-peer voice tag voip

#### Example:

```
Device(config)# dial-peer voice 25 voip
```

Defines a
                                             				VoIP dial peer and enters dial peer configuration mode.

Step 7

session protocol sipv2

#### Example:

```
Device(config-dial-peer)# session protocol sipv2
```

Specifies a
                                             				session protocol for calls between local and remote routers using the Internet
                                             				Engineering Task Force (IETF) SIP.

Step 8

destination uri destination-tag

#### Example:

```
Device(config-dial-peer)# destination uri mydesturi
```

Specifies
                                             				the voice class used to match a dial peer to the destination URI of an outgoing
                                             				call.

Step 9

session target sip-uri

#### Example:

```
Device(config-dial-peer)# session target sip-uri
```

Derives
                                             				session target from incoming URI.

Step 10

exit

#### Example:

```
Device(config-dial-peer)# exit
```

Exits dial
                                             				peer voice configuration mode.

Step 11

voice class uri source-tag sip

#### Example:

```
Device(config)# voice class uri mysourceuri sip
```

Creates or
                                             				modifies a voice class for matching dial peers to a SIP or TEL URI and enters
                                             				voice URI class configuration mode.

Step 12

host hostname-pattern

#### Example:

```
Device(config-voice-uri-class)# host abc.com
```

Matches a
                                             				call based on the host field in a SIP URI.

Step 13

end

#### Example:

```
Device(config-voice-uri-class)# end
```

Ends the
                                             				current configuration session and returns to privileged EXEC mode.

## Example: Deriving
                        	 Session Target from URI

```
Device> enable Device# configure terminal Device(config)# voice class uri mydesturi sip Device(config-voice-uri-class)# host destination.com Device(config-voice-uri-class)# exit !
Device(config)# dial-peer voice 25 voip Device(config-dial-peer)# session protocol sipv2 Device(config-dial-peer)# destination uri mydesturi Device(config-dial-peer)# session target sip-uri Device(config-dial-peer)# exit !
Device(config)# voice class uri mysourceuri sip Device(config-voice-uri-class)# host abc.com Device(config-voice-uri-class)# end
```

### Example:
                           	 Configuring Pass Though of Request URI and To Header URI

#### Example:
                              	 Configuring Pass Though of Request URI and To Header URI (Global Level)

```
Device> enable Device# configure terminal Device(config)# voice service voip Device(conf-voi-serv)# sip Device(conf-serv-sip)# requri-passing Device(conf-serv-sip)# end
```

#### Example:
                              	 Configuring Pass Though of Request URI and To Header URI (Dial Peer
                              	 Level)

```
! Configuring URI voice class destination
Device(config)# voice class uri mydesturi sip Device(config-voice-uri-class)# host xyz.com Device(config-voice-uri-class)# exit ! Configuring outbound dial peer
Device(config)# dial-peer voice 13 voip Device(config-dial-peer)# session protocol sipv2 Device(config-dial-peer)# destination uri mydesturi Device(config-dial-peer)# session target ipv4:10.1.1.1 Device(config-dial-peer)# voice-class sip requri-passing system Device(config-dial-peer)# end
```

### Example:
                           	 Configuring Pass Through of 302 Contact Header

#### Example:
                              	 Configuring Pass Through of 302 Contact Header (Global Level)

```
Device> enable Device# configure terminal Device(config)# voice service voip Device(conf-voi-serv)# sip Device(conf-serv-sip)# contact-passing Device(conf-serv-sip)# end
```

#### Example:
                              	 Configuring Pass Through of 302 Contact Header (Dial Peer Level)

```
! Configuring URI voice class destination
Device> enable Device# configure terminal Device(config)# voice class uri mydesturi sip Device(config-voice-uri-class)# user-id 5678 Device(config-voice-uri-class)# exit ! Configuring outbound dial peer
Device(config)# voice service voip Device(conf-voi-serv)# allow-connections sip to sip Device(conf-voi-serv)# dial-peer voice 200 voip Device(config-dial-peer)# session protocol sipv2 Device(config-dial-peer)# destination uri mydesturi Device(config-dial-peer)# voice-class sip contact-passing Device(config-dial-peer)# end
```

### Configuration
                           	 Examples for URI-Based Dialing Enhancements

### Example: Deriving
                           	 Session Target from URI

```
Device> enable Device# configure terminal Device(config)# voice class uri mydesturi sip Device(config-voice-uri-class)# host destination.com Device(config-voice-uri-class)# exit !
Device(config)# dial-peer voice 25 voip Device(config-dial-peer)# session protocol sipv2 Device(config-dial-peer)# destination uri mydesturi Device(config-dial-peer)# session target sip-uri Device(config-dial-peer)# exit !
Device(config)# voice class uri mysourceuri sip Device(config-voice-uri-class)# host abc.com Device(config-voice-uri-class)# end
```

## Additional
                        	 References for URI-Based Dialing Enhancements

### Related
                              		  Documents

### Technical
                              		  Assistance

The
                                          						Cisco Support website provides extensive online resources, including
                                          						documentation and tools for troubleshooting and resolving technical issues with
                                          						Cisco products and technologies.

To
                                          						receive security and technical information about your products, you can
                                          						subscribe to various services, such as the Product Alert Tool (accessed from
                                          						Field Notices), the Cisco Technical Services Newsletter, and Really Simple
                                          						Syndication (RSS) Feeds.

Access
                                          						to most tools on the Cisco Support website requires a Cisco.com user ID and
                                          						password.

http://www.cisco.com/support

| Note | The minimum supported release of Cisco IOS required for URI-based call routing on dial-peers is Cisco IOS XE Gibraltar Release
                                       16.12. You must configure the 'call-route-url' on the outgoing dial-peers to properly route the refer-to headers based on
                                       the URI matching. |
|---|---|

| Feature
                                             					 Name | Releases | Feature
                                             					 Information |
|---|---|---|
| URI-Based
                                             					 Dialing Enhancements |  | The following commands were introduced or modified: contact-passing , requri-passing , session target
                                                   						  sip-uri and voice-class sip requri-passing |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global
                                                				configuration mode. |
| Step 3 | voice service voip Example: Device(config)# voice service voip | Specifies
                                                				VoIP encapsulation and enters voice service configuration mode. |
| Step 4 | sip Example: Device(conf-voi-serv)# sip | Enters the
                                                				Session Initiation Protocol (SIP) configuration mode. |
| Step 5 | requri-passing Example: Router(conf-serv-sip)# requri-passing | Enables pass through of the host part of the Request-URI and To SIP headers. By default, CUBE sets the host part of the URI to the value configured under the session target of the outbound dial peer. |
| Step 6 | end Example: Router(conf-serv-sip)# end | Ends the
                                                				current configuration session and returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global
                                                				configuration mode. |
| Step 3 | voice class uri tag sip Example: Device(config)# voice class uri mydesturi sip | Creates a
                                                				voice class for matching dial peers to a Session Initiation Protocol (SIP) and
                                                				enters voice URI class configuration mode. |
| Step 4 | host hostname-pattern Example: Device(config-voice-uri-class)# host example.com | Matches a
                                                				call based on the host field in a SIP Uniform Resource Identifier (URI). |
| Step 5 | exit Example: Device(config-voice-uri-class)# exit | Exits voice
                                                				URI class configuration mode. |
| Step 6 | dial-peer voice tag voip Example: Device(config)# dial-peer voice 22 voip | Defines a
                                                				VoIP dial peer and enters dial peer configuration mode. |
| Step 7 | session protocol sipv2 Example: Device(config-dial-peer)# session protocol sipv2 | Specifies a
                                                				session protocol for calls between local and remote routers using the Internet
                                                				Engineering Task Force (IETF) SIP. |
| Step 8 | destination uri tag Example: Device(config)# destination uri mydesturi | Specifies the voice class that is used to match a dial peer to the destination URI of an outgoing call. |
| Step 9 | session target ipv4: ip-address Example: Device(config-dial-peer)# session target ipv4:10.1.1.2 | Designates
                                                				a network-specific address to receive calls from a VoIP. |
| Step 10 | voice-class sip requri-passing [ system ] Example: Device(config-dial-peer)# voice-class sip requri-passing system | Enables the
                                                				pass through of SIP URI headers. |
| Step 11 | end Example: Device(config-dial-peer)# end | Ends the
                                                				current configuration session and returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global
                                                				configuration mode. |
| Step 3 | voice service voip Example: Device(config)# voice service voip | Specifies
                                                				VoIP encapsulation and enters voice service configuration mode. |
| Step 4 | sip Example: Device(conf-voi-serv)# sip | Enters voice
                                                				service SIP configuration mode. |
| Step 5 | contact-passing Example: Router(conf-serv-sip)# contact-passing | Enables pass
                                                				through of the contact header from one leg to the other leg in 302 pass through
                                                				scenario. |
| Step 6 | end Example: Router(conf-serv-sip)# end | Ends the
                                                				current configuration session and returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global
                                                				configuration mode. |
| Step 3 | voice class uri destination-tag sip Example: Device(config)# voice class uri mydesturi sip | Creates a
                                                				voice class for matching dial peers to a Session Initiation Protocol (SIP) and
                                                				enters voice URI class configuration mode. |
| Step 4 | user-id id-tag Example: Device(config-voice-uri-class)# user-id 5678 | Matches a
                                                				call based on the User ID portion of the Uniform Resource Identifier (URI). |
| Step 5 | exit Example: Device(config-voice-uri-class)# exit | Exits voice
                                                				URI class configuration mode. |
| Step 6 | voice service voip Example: Device(config)# voice service voip | Specifies
                                                				Voice over IP (VoIP) as the voice encapsulation type and enters voice service
                                                				configuration mode. |
| Step 7 | allow-connections sip to sip Example: Device(conf-voi-serv)# allow-connections sip to sip | Allows
                                                				connections between SIP endpoints in a VoIP network. |
| Step 8 | dial-peer voice tag voip Example: Device(config)# dial-peer voice 200 voip | Defines a
                                                				VoIP dial peer and enters dial peer configuration mode. |
| Step 9 | session protocol sipv2 Example: Device(config-dial-peer)# session protocol sipv2 | Specifies a
                                                				session protocol for calls between local and remote routers using the Internet
                                                				Engineering Task Force (IETF) SIP. |
| Step 10 | destination uri destination-tag Example: Device(config-dial-peer)# destination uri mydesturi | Specifies
                                                				the voice class used to match a dial peer to the destination URI of an outgoing
                                                				call. |
| Step 11 | voice-class sip contact-passing Example: Device(config-dial-peer)# voice-class sip contact-passing | Enables pass
                                                				through of the contact header from one leg to the other leg in 302 pass through
                                                				scenario. |
| Step 12 | end Example: Device(config-dial-peer)# end | Ends the
                                                				current configuration session and returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice class uri destination-tag sip Example: Device(config)# voice class uri mydesturi sip | Creates or
                                             				modifies a voice class for matching dial peers to a Session Initiation Protocol
                                             				(SIP) or telephone (TEL) Uniform Resource Identifier (URI) and enters voice URI
                                             				class configuration mode. |
| Step 4 | host hostname-pattern Example: Device(config-voice-uri-class)# host destination.com | Matches a
                                             				call based on the host field in a SIP URI. |
| Step 5 | exit Example: Device(config-voice-uri-class)# exit | Exits voice
                                             				URI class configuration mode. |
| Step 6 | dial-peer voice tag voip Example: Device(config)# dial-peer voice 25 voip | Defines a
                                             				VoIP dial peer and enters dial peer configuration mode. |
| Step 7 | session protocol sipv2 Example: Device(config-dial-peer)# session protocol sipv2 | Specifies a
                                             				session protocol for calls between local and remote routers using the Internet
                                             				Engineering Task Force (IETF) SIP. |
| Step 8 | destination uri destination-tag Example: Device(config-dial-peer)# destination uri mydesturi | Specifies
                                             				the voice class used to match a dial peer to the destination URI of an outgoing
                                             				call. |
| Step 9 | session target sip-uri Example: Device(config-dial-peer)# session target sip-uri | Derives
                                             				session target from incoming URI. |
| Step 10 | exit Example: Device(config-dial-peer)# exit | Exits dial
                                             				peer voice configuration mode. |
| Step 11 | voice class uri source-tag sip Example: Device(config)# voice class uri mysourceuri sip | Creates or
                                             				modifies a voice class for matching dial peers to a SIP or TEL URI and enters
                                             				voice URI class configuration mode. |
| Step 12 | host hostname-pattern Example: Device(config-voice-uri-class)# host abc.com | Matches a
                                             				call based on the host field in a SIP URI. |
| Step 13 | end Example: Device(config-voice-uri-class)# end | Ends the
                                             				current configuration session and returns to privileged EXEC mode. |

| Related Topic | Document Title |
|---|---|
| Voice
                                       					 commands | Cisco IOS Voice Command
                                             						  Reference |
| Cisco IOS commands | Cisco IOS Command List, All Releases |
| SIP
                                       					 configuration tasks | SIP Configuration Guide,
                                             						  Cisco IOS Release 15M&T |

| Description | Link |
|---|---|
| The
                                          						Cisco Support website provides extensive online resources, including
                                          						documentation and tools for troubleshooting and resolving technical issues with
                                          						Cisco products and technologies. To
                                          						receive security and technical information about your products, you can
                                          						subscribe to various services, such as the Product Alert Tool (accessed from
                                          						Field Notices), the Cisco Technical Services Newsletter, and Really Simple
                                          						Syndication (RSS) Feeds. Access
                                          						to most tools on the Cisco Support website requires a Cisco.com user ID and
                                          						password. | http://www.cisco.com/support |