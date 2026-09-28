---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-sip-181-call-html-620bfa4ba5
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-sip-181-call.html
retrieved_at: 2026-08-16T15:47:18.824963+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Configure SIP 181 Call is Being Forwarded Message

## Chapter: Configure SIP 181 Call is Being Forwarded Message

# Configure SIP 181 Call is Being Forwarded Message

You can configure support for SIP 181 Call is Being Forwarded messages either globally or on a specific dial-peer. Use the block command in voice service SIP configuration mode to globally configure Cisco IOS voice gateways and Cisco UBEs to drop specified
                        SIP provisional response messages. To configure settings for an individual dial peer, use the voice-class sip block command in dial peer voice configuration mode. Both globally and at the dial peer level, you can also use the sdp keyword to further control when the specified SIP message is dropped based on either the absence or presence of SDP information.

Additionally, you can use commands introduced for this feature to configure a Cisco UBE, either globally or at the dial peer
                        level, to map specific received SIP provisional response messages to a different SIP provisional response message on the outgoing
                        SIP dial peer. To do so, use the map resp-code command in voice service SIP configuration mode for global configuration or, to configure a specific dial peer, use the voice-class sip map resp-code in dial peer voice configuration mode.

## Feature Information for Configuring SIP 181 Call is Being Forwarded Message

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

SIP 181 Call is Being Forwarded Message

Baseline Functionality

This feature allows users to configure support for SIP 181 Call is Being Forwarded messages either globally or on a specific
                                          dial-peer.

This feature includes the following new or modified commands: block , map resp-code , voice-class sip block , voice-class sip map resp-code .

## Configure SIP 181 Call is Being Forwarded Message Globally

Perform this task to configure support for SIP 181 messages at a global level in SIP configuration (conf-serv-sip) mode.

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- sip

- block { 180 | 181 | 183 } [ sdp { absent | present }]

- exit

### DETAILED STEPS

Step 1

enable

### Example:

```
Router> enable
```

Enters privileged EXEC mode, or other security level set by a system administrator.

Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

voice service voip

### Example:

```
Router(config)# voice service voip
```

Enters voice service VoIP configuration mode.

Step 4

sip

### Example:

```
Router(conf-voi-serv)# sip
```

Enters SIP configuration mode.

Step 5

block { 180 | 181 | 183 } [ sdp { absent | present }]

### Example:

```
Router(conf-serv-sip)# block 181 sdp present
```

Configures support of SIP 181 messages globally so that messages are passed as is. The sdp keyword is optional and allows
                                          for dropping or passing of SIP 181 messages based on the presence or absence of SDP.

Step 6

exit

### Example:

```
Router(conf-serv-sip)# exit
```

Exits the current mode.

## Configure SIP 181 Call is Being Forwarded Message at the Dial-Peer Level

Perform this task to configure support for SIP 181 messages at the dial-peer level, in dial peer voice configuration (config-dial-peer)
                              mode.

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice tag voip

- voice-class sip block { 180 | 181 | 183 } [ sdp { absent | present }]

- exit

### DETAILED STEPS

Step 1

enable

### Example:

```
Router> enable
```

Enters privileged EXEC mode, or other security level set by a system administrator.

Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

dial-peer voice tag voip

### Example:

```
Router(config)# dial-peer voice 2 voip
```

Enters dial peer VoIP configuration mode.

Step 4

voice-class sip block { 180 | 181 | 183 } [ sdp { absent | present }]

### Example:

```
Router(config-dial-peer)# voice-class sip block 181 sdp present
```

Configures support of SIP 181 messages on a specific dial peer so that messages are passed as is. The sdp keyword is optional
                                          and allows for dropping or passing of SIP 181 messages based on the presence or absence of SDP.

Step 5

exit

### Example:

```
Router(config-dial-peer)# exit
```

Exits the current mode.

## Configure Mapping of SIP Provisional Response Messages Globally

Perform this task to configure mapping of specific received SIP provisional response messages at a global level in SIP configuration
                              (conf-serv-sip) mode.

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- sip

- map resp-code 181 to 183

- exit

### DETAILED STEPS

Step 1

enable

### Example:

```
Router> enable
```

Enters privileged EXEC mode, or other security level set by a system administrator.

Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

voice service voip

### Example:

```
Router(config)# voice service voip
```

Enters voice service VoIP configuration mode.

Step 4

sip

### Example:

```
Router(conf-voi-serv)# sip
```

Enters SIP configuration mode.

Step 5

map resp-code 181 to 183

### Example:

```
Router(conf-serv-sip)# map resp-code 181 to 183
```

Enables mapping globally of received SIP messages of a specified message type to a different SIP message type.

Step 6

exit

### Example:

```
Router(conf-serv-sip)# exit
```

Exits the current mode.

## Configure Mapping of SIP Provisional Response Messages at the Dial-Peer Level

Perform this task to configure mapping of received SIP provisional response messages at the dial-peer level, in dial peer
                              voice configuration (config-dial-peer) mode.

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice tag voip

- voice-class sip map resp-code 181 to 183

- exit

### DETAILED STEPS

Step 1

enable

### Example:

```
Router> enable
```

Enters privileged EXEC mode, or other security level set by a system administrator.

Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

dial-peer voice tag voip

### Example:

```
Router(config)# dial-peer voice 2 voip
```

Enters dial peer VoIP configuration mode.

Step 4

voice-class sip map resp-code 181 to 183

### Example:

```
Router(config-dial-peer)# voice-class sip map resp-code 181 to 183
```

Enables mapping of received SIP messages of a specified SIP message type on a specific dial peer to a different SIP message
                                          type.

Step 5

exit

### Example:

```
Router(config-dial-peer)# exit
```

Exits the current mode.

| Feature Name | Releases | Feature Information |
|---|---|---|
| SIP 181 Call is Being Forwarded Message | Baseline Functionality | This feature allows users to configure support for SIP 181 Call is Being Forwarded messages either globally or on a specific
                                          dial-peer. This feature includes the following new or modified commands: block , map resp-code , voice-class sip block , voice-class sip map resp-code . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enters privileged EXEC mode, or other security level set by a system administrator. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice service voip Example: Router(config)# voice service voip | Enters voice service VoIP configuration mode. |
| Step 4 | sip Example: Router(conf-voi-serv)# sip | Enters SIP configuration mode. |
| Step 5 | block { 180 \| 181 \| 183 } [ sdp { absent \| present }] Example: Router(conf-serv-sip)# block 181 sdp present | Configures support of SIP 181 messages globally so that messages are passed as is. The sdp keyword is optional and allows
                                          for dropping or passing of SIP 181 messages based on the presence or absence of SDP. |
| Step 6 | exit Example: Router(conf-serv-sip)# exit | Exits the current mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enters privileged EXEC mode, or other security level set by a system administrator. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | dial-peer voice tag voip Example: Router(config)# dial-peer voice 2 voip | Enters dial peer VoIP configuration mode. |
| Step 4 | voice-class sip block { 180 \| 181 \| 183 } [ sdp { absent \| present }] Example: Router(config-dial-peer)# voice-class sip block 181 sdp present | Configures support of SIP 181 messages on a specific dial peer so that messages are passed as is. The sdp keyword is optional
                                          and allows for dropping or passing of SIP 181 messages based on the presence or absence of SDP. |
| Step 5 | exit Example: Router(config-dial-peer)# exit | Exits the current mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enters privileged EXEC mode, or other security level set by a system administrator. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice service voip Example: Router(config)# voice service voip | Enters voice service VoIP configuration mode. |
| Step 4 | sip Example: Router(conf-voi-serv)# sip | Enters SIP configuration mode. |
| Step 5 | map resp-code 181 to 183 Example: Router(conf-serv-sip)# map resp-code 181 to 183 | Enables mapping globally of received SIP messages of a specified message type to a different SIP message type. |
| Step 6 | exit Example: Router(conf-serv-sip)# exit | Exits the current mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enters privileged EXEC mode, or other security level set by a system administrator. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | dial-peer voice tag voip Example: Router(config)# dial-peer voice 2 voip | Enters dial peer VoIP configuration mode. |
| Step 4 | voice-class sip map resp-code 181 to 183 Example: Router(config-dial-peer)# voice-class sip map resp-code 181 to 183 | Enables mapping of received SIP messages of a specified SIP message type on a specific dial peer to a different SIP message
                                          type. |
| Step 5 | exit Example: Router(config-dial-peer)# exit | Exits the current mode. |