---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-condl-header-html-0e8c7391e2
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-condl-header.html
retrieved_at: 2026-08-16T15:46:20.227017+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Manipulate SIP Status-Line Header of SIP Responses

## Chapter: Manipulate SIP Status-Line Header of SIP Responses

# Manipulate SIP Status-Line Header of SIP Responses

## Manipulate SIP Status-Line Header of SIP Responses

The SIP status
                           		line is a SIP response header, and it can be modified like any other SIP
                           		headers of a message. it can either be modified with a user-defined value, or
                           		the status line from an incoming response can be copied to an outgoing SIP
                           		response. The SIP header keyword used for the response status line is SIP-StatusLine .

### Feature Information

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

SIP Profile Enhancements for SIP responses and error codes

Baseline Functionality

This feature extends SIP profiles to allow the following:

Modification of the outgoing SIP response status line.
                                                   						  Previously, only modification of outgoing SIP requests and responses was
                                                   						  possible.

Copying of the incoming SIP response status-line. The information from the peer-leg status-line can then be copied to user-variables
                                                   and applied to the outbound response status-line. This option can be used to pass-thru the error-code and error phrase from
                                                   peer-leg. Previously, only copying of SIP headers were possible.

Before applying a SIP profile to a response from CUBE , the response can be mapped to its corresponding request.

## Copy Incoming SIP Response Status Line to Outgoing SIP Response

To copy content
                              		  from the status line of an incoming SIP response that a device receives to an
                              		  outgoing response, configure a SIP copylist for SIP status line and apply it to
                              		  an incoming dial peer. A SIP profile must be configured to copy the status line
                              		  of an incoming SIP response to a user-defined variable and apply it to an
                              		  outgoing SIP response.

### SUMMARY STEPS

- enable

- configure terminal

- voice class sip-copylist tag

- sip-header SIP-StatusLine

- exit

- dial-peer voice inbound-dial-peer-id voip

- voice-class sip copy-list list-id

- exit

- voice class sip-profiles tag

- response response-code peer-header sip SIP-StatusLine copy match-pattern copy-variable

- response response-code sip-header SIP-StatusLine modify match-pattern copy-variable

- exit

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

Enters global
                                          				configuration mode.

Step 3

voice class sip-copylist tag

### Example:

```
Device(config)# voice class sip-copylist 1
```

Configures a
                                          				list of entities to be sent to the peer call leg and enters voice class
                                          				configuration mode.

Step 4

sip-header SIP-StatusLine

### Example:

```
Device(config-class)# sip-header SIP-StatusLine
```

Specifies
                                          				that the Session Initiation Protocol (SIP) status line header must be sent to
                                          				the peer call leg.

Step 5

exit

### Example:

```
Device(config-class)# exit
```

Exits voice
                                          				class configuration mode and returns to global configuration mode.

Step 6

dial-peer voice inbound-dial-peer-id voip

### Example:

```
Device(config)# dial-peer voice 99 voip
```

Specifies an
                                          				inbound dial peer and enters dial peer configuration mode.

Step 7

voice-class sip copy-list list-id

### Example:

```
Device(config-dial-peer)# voice-class sip copy-list 1
```

Associates
                                          				the SIP copy list with the inbound dial peer.

Step 8

exit

### Example:

```
Device(config-dial-peer)# exit
```

Exits dial
                                          				peer configuration mode and returns to global configuration mode.

Step 9

voice class sip-profiles tag

### Example:

```
Device(config)# voice class sip-profiles 10
```

Enables
                                          				dial peer-based VoIP SIP profile configurations and enters voice class
                                          				configuration mode.

Step 10

response response-code peer-header sip SIP-StatusLine copy match-pattern copy-variable

### Example:

```
Device(config-class)# response ANY peer-header sip SIP-StatusLine copy "(.*)" u01
```

Step 11

response response-code sip-header SIP-StatusLine modify match-pattern copy-variable

### Example:

```
Device(config-class)# response ANY sip-header SIP-StatusLine modify ".*" "\u01"
```

Step 12

exit

### Example:

```
Device(config-class)# exit
```

Exits voice
                                          				class configuration mode and returns to global configuration mode.

### What to do next

Apply the SIP
                              		  profile to the outbound dial peer to copy the SIP response to the outbound leg.

## Modify Status-Line Header of Outgoing SIP Response with User Defined Values

### SUMMARY STEPS

- enable

- configure terminal

- voice class sip-profiles tag

- response response-code [ method method-type ] sip-header SIP-StatusLine modify match-pattern replacement-pattern

- exit

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

Enters global
                                          				configuration mode.

Step 3

voice class sip-profiles tag

### Example:

```
Device(config)# voice class sip-profiles 10
```

Enables dial
                                          				peer-based VoIP SIP profile configurations and enters voice class configuration
                                          				mode.

Step 4

response response-code [ method method-type ] sip-header SIP-StatusLine modify match-pattern replacement-pattern

### Example:

```
Device(config-class)# response 404 sip-header SIP-StatusLine modify "404 Not Found" "404 MyError"
```

Step 5

exit

### Example:

```
Device(config-class)# exit
```

Exits voice
                                          				class configuration mode.

### What to do next

Associate the
                              		  SIP profile with an outbound dial peer.

| Feature Name | Releases | Feature Information |
|---|---|---|
| SIP Profile Enhancements for SIP responses and error codes | Baseline Functionality | This feature extends SIP profiles to allow the following: Modification of the outgoing SIP response status line.
                                                   						  Previously, only modification of outgoing SIP requests and responses was
                                                   						  possible. Copying of the incoming SIP response status-line. The information from the peer-leg status-line can then be copied to user-variables
                                                   and applied to the outbound response status-line. This option can be used to pass-thru the error-code and error phrase from
                                                   peer-leg. Previously, only copying of SIP headers were possible. Before applying a SIP profile to a response from CUBE , the response can be mapped to its corresponding request. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global
                                          				configuration mode. |
| Step 3 | voice class sip-copylist tag Example: Device(config)# voice class sip-copylist 1 | Configures a
                                          				list of entities to be sent to the peer call leg and enters voice class
                                          				configuration mode. |
| Step 4 | sip-header SIP-StatusLine Example: Device(config-class)# sip-header SIP-StatusLine | Specifies
                                          				that the Session Initiation Protocol (SIP) status line header must be sent to
                                          				the peer call leg. |
| Step 5 | exit Example: Device(config-class)# exit | Exits voice
                                          				class configuration mode and returns to global configuration mode. |
| Step 6 | dial-peer voice inbound-dial-peer-id voip Example: Device(config)# dial-peer voice 99 voip | Specifies an
                                          				inbound dial peer and enters dial peer configuration mode. |
| Step 7 | voice-class sip copy-list list-id Example: Device(config-dial-peer)# voice-class sip copy-list 1 | Associates
                                          				the SIP copy list with the inbound dial peer. |
| Step 8 | exit Example: Device(config-dial-peer)# exit | Exits dial
                                          				peer configuration mode and returns to global configuration mode. |
| Step 9 | voice class sip-profiles tag Example: Device(config)# voice class sip-profiles 10 | Enables
                                          				dial peer-based VoIP SIP profile configurations and enters voice class
                                          				configuration mode. |
| Step 10 | response response-code peer-header sip SIP-StatusLine copy match-pattern copy-variable Example: Device(config-class)# response ANY peer-header sip SIP-StatusLine copy "(.*)" u01 | Copies
                                       			 responses from the corresponding incoming call leg into a copy variable. |
| Step 11 | response response-code sip-header SIP-StatusLine modify match-pattern copy-variable Example: Device(config-class)# response ANY sip-header SIP-StatusLine modify ".*" "\u01" | Modifies an
                                       			 outgoing response using the copy variable defined in the previous step. |
| Step 12 | exit Example: Device(config-class)# exit | Exits voice
                                          				class configuration mode and returns to global configuration mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global
                                          				configuration mode. |
| Step 3 | voice class sip-profiles tag Example: Device(config)# voice class sip-profiles 10 | Enables dial
                                          				peer-based VoIP SIP profile configurations and enters voice class configuration
                                          				mode. |
| Step 4 | response response-code [ method method-type ] sip-header SIP-StatusLine modify match-pattern replacement-pattern Example: Modifying
                                          				status line of a SIP header to a user-defined response type: Device(config-class)# response 404 sip-header SIP-StatusLine modify "404 Not Found" "404 MyError" | Modifies SIP status line of a SIP response with user-defined values. |
| Step 5 | exit Example: Device(config-class)# exit | Exits voice
                                          				class configuration mode. |