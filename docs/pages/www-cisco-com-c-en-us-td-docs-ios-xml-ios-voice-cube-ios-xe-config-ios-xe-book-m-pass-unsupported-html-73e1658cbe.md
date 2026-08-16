---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-pass-unsupported-html-73e1658cbe
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_pass_unsupported.html
retrieved_at: 2026-08-16T15:46:33.249490+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Pass Unsupported SIP Headers

## Chapter: Pass Unsupported SIP Headers

# Pass Unsupported SIP Headers

## Overview

This feature is used to pass parameters that are unsupported by Cisco Unified Border Element (CUBE) , but mandatory to the service provider from one leg to another. When a SIP message is received, a check is done for the header,
                           and if it is available, it is copied into a copy list and passed on to the outbound dial peer leg. The feature enables the
                           Cisco Unified Border Element (Cisco UBE) platform to pass through end-to-end headers at a global or dial peer level that are
                           not processed or understood in a Session Initiation Protocol (SIP) trunk to SIP trunk scenario.

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
                                             					 for conditional header manipulation of SIP headers

This
                                             					 feature modifies the following commands: voice class sip-profiles , response , request , voice-class sip copy-list , sip-header

### Prerequisites

Configuring the media
                                          				  flow-around command is required for Session Description Protocol
                                    			 (SDP) pass-through. When flow-around is not configured, the flow-through mode
                                    			 of SDP pass-through will be functional.

When the
                                    			 dial-peer media flow mode is asymmetrically configured, the default behavior is
                                    			 to fall back to SDP pass-through with flow-through.

### Restrictions

When Session Description Protocol (SDP) pass-through is enabled, some of the interworking that the CUBE currently performs cannot be activated. These features include:

Delayed Offer to
                                    			 Early Offer Interworking

Supplementary
                                    			 Services with Triggered Invites

Flow-around calls will not work with SDP pass through

DTMF Interworking
                                    			 Scenarios

Fax
                                    			 Interworking/QoS Negotiation

Transcoding

For configurable
                              		pass-through of SIP INVITE parameters, the following features for Session
                              		Initiation Protocol (SIP)-SIP dial-peer rotary calls are not supported:

Unsupported header pass-through functionality for SIP-SIP dial-peer rotary calls

Unsupported content pass-through functionality for SIP-SIP dial-peer rotary calls

With CSCty41575, the unsupported header and content pass-through functionalities mentioned above are addressed.

## Supported SIP Headers

### Mandatory SIP Headers

The following table provides a list of mandatory headers:

Also

Authorization

Call_ID

CC-Diversion

CC-Redirect

Cisco_Gcid

Cisco_Ccid

Contact

Content-Disposition

Content-Encoding

Content-Length

Content-Type

Cseq

Date

From

Max-Forwards

MIME-Version

P-Asserted-Identity

P-Preferred-Identity

Privacy

Proxy-Authenticate

Proxy-Authorization

Record-Route

Route

Session-Expires

Timestamp

To

User-Agent

Via

WWW-Authenticate

## Unsupported Headers

You can configure CUBE to pass through unsupported headers (headers CUBE cannot understand). The following are some of the
                           examples for SIP headers that are unsupported on CUBE:

P-Early-Media

SIP-Req-URI

## Enable Configurable Pass-Through of SIP INVITE Parameters (Global Level)

Perform this task to configure unsupported content pass-through on a CUBE platform at the global level.

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- sip

- pass-thru { content { sdp | unsupp } | headers { unsupp | list-tag }}

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
Device# configure terminal
```

Enters global
                                          				configuration mode.

Step 3

voice service voip

### Example:

```
Device(config)# voice service voip
```

Enters voice
                                          				service VoIP configuration mode.

Step 4

sip

### Example:

```
Device(conf-voi-serv)# sip
```

Enters SIP
                                          				configuration mode.

Step 5

pass-thru { content { sdp | unsupp } | headers { unsupp | list-tag }}

### Example:

```
Device(conf-serv-sip)# pass-thru content unsupp
```

Passes the
                                          				Session Description Protocol (SDP) transparently from in-leg to the out-leg
                                          				with no media negotiation.

Step 6

end

### Example:

```
Device(conf-serv-sip)# end
```

Ends the
                                          				current configuration session and returns to privileged EXEC mode.

### Example: Enabling
                           	 Configurable Pass-Through of SIP INVITE Parameters (Global Level)

```
Device> enable Device# configure terminal Device(config)# voice service voip Device(conf-voi-serv)# sip Device(conf-serv-sip)# pass-thru content unsupp Device(conf-serv-sip)# end
```

## Enable Configurable Pass-Through of SIP INVITE Parameters (Dial Peer Level)

Perform this task to configure unsupported content pass-through on a CUBE platform at the dial-peer level.

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice tag voip

- voice-class sip pass-thru { content { sdp | unsupp } | headers { unsupp | list tag }} [ system ]

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
Device# configure terminal
```

Enters global
                                          				configuration mode.

Step 3

dial-peer voice tag voip

### Example:

```
Device(config)# dial-peer voice 2 voip
```

Enters dial
                                          				peer VoIP configuration mode.

Step 4

voice-class sip pass-thru { content { sdp | unsupp } | headers { unsupp | list tag }} [ system ]

### Example:

```
Device(config-dial-peer)# voice-class sip pass-thru content sdp
```

Passes the
                                          				Session Description Protocol (SDP) transparently from in-leg to the out-leg
                                          				with no media negotiation.

Step 5

end

### Example:

```
Device(config-dial-peer)# end
```

Ends the
                                          				current configuration session and returns to privileged EXEC mode.

### Example: Enabling
                           	 Configurable Pass-Through of SIP INVITE Parameters (Dial Peer Level)

```
Device> enable Device# configure terminal Device(config)# dial-peer voice 2 voip Device(config-dial-peer)# voice-class sip pass-thru content sdp Device(config-dial-peer)# end
```

## Configure a Route String Header Pass-Through Using Pass-Through List

### SUMMARY STEPS

- enable

- configure terminal

- voice class sip-hdr-passthrulist list-tag

- passthru-hdr header-name

- passthru-hdr-unsupp

- exit

- dial-peer voice tag voip

- description string

- session protocol sipv2

- voice-class sip pass-thru headers list-tag

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
Device# configure terminal
```

Enters global
                                          				configuration mode.

Step 3

voice class sip-hdr-passthrulist list-tag

### Example:

```
Device(config)# voice class sip-hdr-passthrulist 101
```

Configures
                                          				list of headers to be passed through and enters voice class configuration mode.

Step 4

passthru-hdr header-name

### Example:

```
Device(config-class)# passthru-hdr Resource-Priority
```

Adds header
                                          				name to the list of headers to be passed through. Repeat this step for every
                                          				non-mandatory header.

Step 5

passthru-hdr-unsupp

### Example:

```
Device(config-class)# passthru-hdr-unsupp
```

Adds the
                                          				unsupported headers to the list of headers to be passed through.

Step 6

exit

### Example:

```
Device(config-class)# exit
```

Exits the
                                          				current configuration session and returns to global configuration mode.

Step 7

dial-peer voice tag voip

### Example:

```
Device(config)# dial-peer voice 1 voip
```

Enters dial
                                          				peer voice configuration mode.

Step 8

description string

### Example:

```
Device(config-dial-peer)# description inbound-dialpeer
```

Adds
                                          				descriptive information about the dial peer.

Step 9

session protocol sipv2

### Example:

```
Device(config-dial-peer)# session protocol sipv2
```

Configures the
                                          				IETF Session Initiation Protocol (SIP) for the dial peer.

Step 10

voice-class sip pass-thru headers list-tag

### Example:

```
Device(config-dial-peer)# voice-class sip pass-thru headers 101
```

Enables call
                                          				routing based on the destination route string for a dial peer.

Step 11

end

### Example:

```
Device(config-dial-peer)# end
```

Exits the
                                          				current configuration mode and returns to privileged EXEC mode.

## Example:
                        	 Configuring a Route String Header Pass-Through Using Pass-Through List

```
Device> enable Device# configure terminal Device(config)# voice class sip-hdr-passthrulist 101 Device(config-class)# passthru-hdr X-hdr-1 Device(config-class)# passthru-hdr Resource-Priority Device(config-class)# passthru-hdr-unsupp Device(config-class)# exit Device(config)# dial-peer voice 1 voip Device(config-dial-peer)# description inbound-dialpeer Device(config-dial-peer)# session protocol sipv2 Device(config-dial-peer)# voice-class sip pass-thru headers 101 Device(config-dial-peer)# end
```

## Example: Passing a
                        	 Header Not Supported by CUBE

CUBE does not pass
                              		  “x-cisco-tip”. However, certain TelePresence equipments require “TIP”.

The SIP profile
                              		  below will look for "x-cisco-tip" in the inbound contact header then pass it in
                              		  the outbound contact header.

Inbound Contact
                              		  Header

```
Contact: <sip:89016442998@161.44.77.193;transport=udp>;x-cisco-tip
```

Outbound Contact
                              		  Header

```
Contact: <sip:89016442998@10.86.176.19:5060>;x-cisco-tip
```

Create a copylist
                              		  to pass the Contact Header from the incoming message to the outgoing message.
                              		  The “x-cisco-tip” is not copied in this step as it is unsupported by CUBE.

```
!Create a copyList
Device(config)# voice class sip-copylist 1 Device(config-class)# sip-header Contact Device(config-class)# exit !Apply the copylist to incoming dial peer.
Device(config)# dial-peer voice 1 voip Device(config-dial-peer)# description incoming SIP Trunk Device(config-dial-peer)# incoming called-number Device(config-dial-peer)# voice-class sip copy-list 1
```

Create a SIP
                              		  profile that copies “x-cisco-tip” into a variable, and use that variable to
                              		  modify the outgoing Contact header. Apply the SIP profile to an outbound dial
                              		  peer.

```
Device# voice class sip-profiles 3001 !Copy the Contact header from the incoming dial peer into variable u01
Device(config-class)# request INVITE peer-header sip Contact copy "(;x-cisco-tip)" u01 !Modify the outgoing SIP Invite with this variable.  
Device(config-class)# request INVITE sip-header Contact modify "$" "\u01"″ !Apply the SIP Profile to the outgoing dial peer.
Device(config)# dial-peer voice 5000 voip Device(config-dial-peer)# description outbound SIP Device(config-dial-peer)# destination-pattern 5...$ Device(config-dial-peer)# voice-class sip profiles 3001
```

| Feature
                                             					 Name | Releases | Feature
                                             					 Information |
|---|---|---|
| Support
                                             					 for conditional header manipulation of SIP headers | Baseline Functionality | This
                                             					 feature modifies the following commands: voice class sip-profiles , response , request , voice-class sip copy-list , sip-header |

| Note | With CSCty41575, the unsupported header and content pass-through functionalities mentioned above are addressed. |
|---|---|

| Also | Authorization | Call_ID |
|---|---|---|
| CC-Diversion | CC-Redirect | Cisco_Gcid |
| Cisco_Ccid | Contact | Content-Disposition |
| Content-Encoding | Content-Length | Content-Type |
| Cseq | Date | From |
| Max-Forwards | MIME-Version | P-Asserted-Identity |
| P-Preferred-Identity | Privacy | Proxy-Authenticate |
| Proxy-Authorization | Record-Route | Route |
| Session-Expires | Timestamp | To |
| User-Agent | Via | WWW-Authenticate |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables
                                          				privileged EXEC mode. Enter your
                                                					 password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global
                                          				configuration mode. |
| Step 3 | voice service voip Example: Device(config)# voice service voip | Enters voice
                                          				service VoIP configuration mode. |
| Step 4 | sip Example: Device(conf-voi-serv)# sip | Enters SIP
                                          				configuration mode. |
| Step 5 | pass-thru { content { sdp \| unsupp } \| headers { unsupp \| list-tag }} Example: Device(conf-serv-sip)# pass-thru content unsupp | Passes the
                                          				Session Description Protocol (SDP) transparently from in-leg to the out-leg
                                          				with no media negotiation. |
| Step 6 | end Example: Device(conf-serv-sip)# end | Ends the
                                          				current configuration session and returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables
                                          				privileged EXEC mode. Enter your
                                                					 password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global
                                          				configuration mode. |
| Step 3 | dial-peer voice tag voip Example: Device(config)# dial-peer voice 2 voip | Enters dial
                                          				peer VoIP configuration mode. |
| Step 4 | voice-class sip pass-thru { content { sdp \| unsupp } \| headers { unsupp \| list tag }} [ system ] Example: Device(config-dial-peer)# voice-class sip pass-thru content sdp | Passes the
                                          				Session Description Protocol (SDP) transparently from in-leg to the out-leg
                                          				with no media negotiation. |
| Step 5 | end Example: Device(config-dial-peer)# end | Ends the
                                          				current configuration session and returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables
                                          				privileged EXEC mode. Enter your
                                                					 password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global
                                          				configuration mode. |
| Step 3 | voice class sip-hdr-passthrulist list-tag Example: Device(config)# voice class sip-hdr-passthrulist 101 | Configures
                                          				list of headers to be passed through and enters voice class configuration mode. |
| Step 4 | passthru-hdr header-name Example: Device(config-class)# passthru-hdr Resource-Priority | Adds header
                                          				name to the list of headers to be passed through. Repeat this step for every
                                          				non-mandatory header. |
| Step 5 | passthru-hdr-unsupp Example: Device(config-class)# passthru-hdr-unsupp | Adds the
                                          				unsupported headers to the list of headers to be passed through. |
| Step 6 | exit Example: Device(config-class)# exit | Exits the
                                          				current configuration session and returns to global configuration mode. |
| Step 7 | dial-peer voice tag voip Example: Device(config)# dial-peer voice 1 voip | Enters dial
                                          				peer voice configuration mode. |
| Step 8 | description string Example: Device(config-dial-peer)# description inbound-dialpeer | Adds
                                          				descriptive information about the dial peer. |
| Step 9 | session protocol sipv2 Example: Device(config-dial-peer)# session protocol sipv2 | Configures the
                                          				IETF Session Initiation Protocol (SIP) for the dial peer. |
| Step 10 | voice-class sip pass-thru headers list-tag Example: Device(config-dial-peer)# voice-class sip pass-thru headers 101 | Enables call
                                          				routing based on the destination route string for a dial peer. |
| Step 11 | end Example: Device(config-dial-peer)# end | Exits the
                                          				current configuration mode and returns to privileged EXEC mode. |