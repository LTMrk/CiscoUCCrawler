---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-copy-sip-headers-html-3ca17e4c5e
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_copy_sip_headers.html
retrieved_at: 2026-08-16T15:46:24.453774+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Copy SIP Headers

## Chapter: Copy SIP Headers

# Copy SIP Headers

## Copy SIP Headers

This feature shows
                           		you how outgoing SIP headers can be manipulated using information from incoming
                           		and other outgoing SIP headers.

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

### Copy SIP Header Fields to Another

## Copy From an Incoming Header and Modifying an Outgoing Header

To copy content
                              		  from an incoming header that a device receives to an outgoing header, configure
                              		  a SIP copylist for that header and apply it to an incoming dial peer. A SIP
                              		  profile is configured to copy this incoming header to a user-defined variable
                              		  and apply it to an outgoing header.

### SUMMARY STEPS

- enable

- configure terminal

- voice class sip-copylist tag

- Do one of the following:

- sip-header header-name

- sip-header SIP-Req-URI

- exit

- dial-peer voice inbound-dial-peer-tag voip

- voice-class sip-copylist tag

- exit

- voice class sip-profiles profile-id

- { request | response } message peer-header sip header-to-copy copy header-value-to-match copy-variable

- { request | response } message { sip-header | sdp-header } header-to-modify modify header-value-to-match header-value-to-replace

- exit

- dial-peer voice outbound-dial-peer-tag voip

- voice-class sip-profiles profile-id

- exit

### DETAILED STEPS

Step 1

enable

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

Enters global configuration mode.

Step 3

voice class sip-copylist tag

### Example:

```
Device(config)# voice class sip-copylist 100
```

Configures a list of entities to be sent to a peer call leg and enters voice class configuration mode.

Step 4

Do one of the following:

- sip-header header-name

- sip-header SIP-Req-URI

### Example:

```
Device(config-class)# sip-header To
```

sip-req-uri —Configures Cisco Unified Border Element (UBE) to send a SIP request Uniform Resource Identifier (URI) to the peer call leg.

header-name —Configures Cisco Unified Border Element (UBE) to send the header name specified to the peer call leg.

Step 5

exit

Exits voice class configuration mode.

Step 6

dial-peer voice inbound-dial-peer-tag voip

### Example:

```
Device(config)# dial-peer voice 2 voip
```

Enters the dial peer configuration mode for the specified inbound dial peer.

Step 7

voice-class sip-copylist tag

### Example:

```
Device(config-dial-peer)# voice-class sip-copylist 100
```

Applies the copy list to the dial-peer.

Step 8

exit

Exits to global configuration mode.

Step 9

voice class sip-profiles profile-id

### Example:

```
Device(config)# voice class sip-profiles 10
```

Create a SIP Profile and enters voice class configuration mode.

Step 10

{ request | response } message peer-header sip header-to-copy copy header-value-to-match copy-variable

### Example:

```
Device(config-class)# request INVITE peer-header sip TO copy "sip:(.*)@" u01
```

Step 11

{ request | response } message { sip-header | sdp-header } header-to-modify modify header-value-to-match header-value-to-replace

### Example:

```
Device(config-class)# request INVITE sip-header SIP-Req-URI modify ".*@(.*)" "INVITE sip:\u01@\1"
```

Step 12

exit

Exits to global configuration mode.

Step 13

dial-peer voice outbound-dial-peer-tag voip

### Example:

```
Device(config)# dial-peer voice 2 voip
```

Enters the dial peer configuration mode for the specified outbond dial peer.

Step 14

voice-class sip-profiles profile-id

### Example:

```
Device(config-dial-peer)# voice-class sip-profiles 10
```

SIP Profile is applied to the dial-peer.

Step 15

exit

Exits to global configuration mode.

## Copy From One Outgoing Header to Another

### SUMMARY STEPS

- enable

- configure terminal

- voice class sip-profiles profile-id

- { request | response } message { sip-header | sdp-header } header-to-copy copy header-value-to-match copy-variable

- { request | response } message { sip-header | sdp-header } header-to-modify modify header-value-to-match header-value-to-replace

- end

### DETAILED STEPS

Step 1

enable

Enables
                                          				privileged EXEC mode.

Enter your
                                                					 password if prompted.

Step 2

configure terminal

Enters global
                                          				configuration mode.

Step 3

voice class sip-profiles profile-id

### Example:

```
Device(config)# voice class sip-profiles 10
```

Creates a SIP
                                          				profile and enters voice class configuration mode.

Step 4

{ request | response } message { sip-header | sdp-header } header-to-copy copy header-value-to-match copy-variable

### Example:

```
Device(config-class)# request INVITE sip-header TO copy "sip:(.*)@" u01
```

Step 5

{ request | response } message { sip-header | sdp-header } header-to-modify modify header-value-to-match header-value-to-replace

### Example:

```
Device(config-class)# request INVITE sip-header SIP-Req-URI modify ".*@(.*)" "INVITE sip:\u01@\1"
```

Step 6

end

### Example:

```
Device(config-class)# end
```

Exits voice
                                          				class configuration mode and enters privileged EXEC mode.

### What to do next

Apply the SIP
                              		  Profile to an outbound dial peer.

## Example: Copying
                        	 the To Header into the SIP-Req-URI

### Copying
                              		  Contents from One Header to Another

Given below is a
                              		  scenario in an organization, where the provider has sent only a global
                              		  reference number in the SIP-Req-URI header of the INVITE message, and has
                              		  placed the actual phone destination number only in the To: SIP header. The CUCM
                              		  typically routes on the SIP-Req-URI.

Given below is the
                              		  original SIP message, where the INVITE has a non-routable value of 43565432A5.
                              		  The actual phone destination number is 25555552 and is present in the To: SIP
                              		  header.

Given below is the
                              		  SIP message that is required. Note that 43565432A5 has changed to 25555552 in
                              		  the SIP INVITE.

Because CUBE is a
                              		  back-to-back user agent, the incoming dial peer is matched to the outgoing dial
                              		  peer. The SIP Profile configured below copies the value from the incoming dial
                              		  peer

```
Device# voice class sip-profiles 1 !Copy the To header from the incoming dial peer into variable u01
Device(config-class)# request INVITE peer-header sip TO copy “sip:(.*)@” u01 !Modify the outgoing SIP Invite with this variable.  
Device(config-class)# request INVITE sip-header SIP-Req-URI modify “.*@(.*)” “INVITE sip:\u01@\1″
```

Apply the SIP
                              		  profile to the incoming dial peer.

```
Device(config)# dial-peer voice 99 voip Device(config-dial-peer)# outgoing to CUCM Device(config-dial-peer)# destination-pattern 02555555. Device(config-dial-peer)# session protocol sipv2 Device(config-dial-peer)# session target ipv4:10.1.2.3 !Applying SIP profile to the dial peer
Device(config-dial-peer)# voice-class sip profiles 1 Device(config-dial-peer)# voice-class code 1 Device(config-dial-peer)# dtmf-relay rtp-nte Device(config-dial-peer)# no vad
```

Additionally, if
                              		  you would like to copy the To: Header from the inbound dial peer to the
                              		  outbound dial peer, use a copy list.

```
!Create a copy List
Device(config)# voice class sip-copylist 1 Device(config-class)# sip-header TO Device(config-class)# exit !Apply the copy list to incoming dial peer.
Device(config)# dial-peer voice 1 voip Device(config-dial-peer)# description incoming SIP Trunk Device(config-dial-peer)# session protocol sipv2 Device(config-dial-peer)# session target sip-server Device(config-dial-peer)# incoming uri to TRUNK Device(config-dial-peer)# voice-class code 1 Device(config-dial-peer)# voice-class sip copy-list 1 Device(config)# voice class uri TRUNK sip Device(config-class)# user-id 2555555. Device(config-class)# end
```

| Feature
                                             					 Name | Releases | Feature
                                             					 Information |
|---|---|---|
| Support
                                             					 for conditional header manipulation of SIP headers | Baseline Functionality | This
                                             					 feature modifies the following commands: voice class sip-profiles , response , request , voice-class sip copy-list , sip-header |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal | Enters global configuration mode. |
| Step 3 | voice class sip-copylist tag Example: Device(config)# voice class sip-copylist 100 | Configures a list of entities to be sent to a peer call leg and enters voice class configuration mode. |
| Step 4 | Do one of the following: sip-header header-name sip-header SIP-Req-URI Example: Device(config-class)# sip-header To | Specifies the SIP header to be copied to the peer call leg. sip-req-uri —Configures Cisco Unified Border Element (UBE) to send a SIP request Uniform Resource Identifier (URI) to the peer call leg. header-name —Configures Cisco Unified Border Element (UBE) to send the header name specified to the peer call leg. |
| Step 5 | exit | Exits voice class configuration mode. |
| Step 6 | dial-peer voice inbound-dial-peer-tag voip Example: Device(config)# dial-peer voice 2 voip | Enters the dial peer configuration mode for the specified inbound dial peer. |
| Step 7 | voice-class sip-copylist tag Example: Device(config-dial-peer)# voice-class sip-copylist 100 | Applies the copy list to the dial-peer. |
| Step 8 | exit | Exits to global configuration mode. |
| Step 9 | voice class sip-profiles profile-id Example: Device(config)# voice class sip-profiles 10 | Create a SIP Profile and enters voice class configuration mode. |
| Step 10 | { request \| response } message peer-header sip header-to-copy copy header-value-to-match copy-variable Example: Device(config-class)# request INVITE peer-header sip TO copy "sip:(.*)@" u01 | Copies headers from the corresponding incoming dial peer into a copy variable. |
| Step 11 | { request \| response } message { sip-header \| sdp-header } header-to-modify modify header-value-to-match header-value-to-replace Example: Device(config-class)# request INVITE sip-header SIP-Req-URI modify ".*@(.*)" "INVITE sip:\u01@\1" | Modifies an outgoing SIP or SDP header using the copy variable defined in the previous step. |
| Step 12 | exit | Exits to global configuration mode. |
| Step 13 | dial-peer voice outbound-dial-peer-tag voip Example: Device(config)# dial-peer voice 2 voip | Enters the dial peer configuration mode for the specified outbond dial peer. |
| Step 14 | voice-class sip-profiles profile-id Example: Device(config-dial-peer)# voice-class sip-profiles 10 | SIP Profile is applied to the dial-peer. |
| Step 15 | exit | Exits to global configuration mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable | Enables
                                          				privileged EXEC mode. Enter your
                                                					 password if prompted. |
| Step 2 | configure terminal | Enters global
                                          				configuration mode. |
| Step 3 | voice class sip-profiles profile-id Example: Device(config)# voice class sip-profiles 10 | Creates a SIP
                                          				profile and enters voice class configuration mode. |
| Step 4 | { request \| response } message { sip-header \| sdp-header } header-to-copy copy header-value-to-match copy-variable Example: Device(config-class)# request INVITE sip-header TO copy "sip:(.*)@" u01 | Copies the
                                       			 contents of the specified header from an outbound message into a copy variable. |
| Step 5 | { request \| response } message { sip-header \| sdp-header } header-to-modify modify header-value-to-match header-value-to-replace Example: Device(config-class)# request INVITE sip-header SIP-Req-URI modify ".*@(.*)" "INVITE sip:\u01@\1" | Modifies an
                                       			 outgoing SIP or SDP header using the copy variable defined in the previous
                                       			 step. |
| Step 6 | end Example: Device(config-class)# end | Exits voice
                                          				class configuration mode and enters privileged EXEC mode. |