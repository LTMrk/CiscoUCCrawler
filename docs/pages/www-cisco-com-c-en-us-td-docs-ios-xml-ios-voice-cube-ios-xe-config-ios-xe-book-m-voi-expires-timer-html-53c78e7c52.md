---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-expires-timer-html-53c78e7c52
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-expires-timer.html
retrieved_at: 2026-08-16T15:47:27.453958+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Expires Timer Reset on Receiving or Sending SIP 183 Message

## Chapter: Expires Timer Reset on Receiving or Sending SIP 183 Message

# Expires Timer Reset on Receiving or Sending SIP 183 Message

This feature enables support for resetting the Expires timer when receiving or sending SIP 183 messages on Cisco Unified
                        Communications Manager Express (Cisco Unified CME), a Cisco IOS voice gateway, or a Cisco Unified Border Element (Cisco UBE).
                        When the terminating device lacks answer supervision or does not send the required SIP 200 OK message within the timer expiry,
                        you can enable this feature to send periodic SIP 183 messages to reset the Expires timer and preserve the call until final
                        response. This feature can be enabled globally or on a specific dial peer. Additionally, you can configure this feature based
                        on the presence or absence of Session Description Protocol (SDP).

For details about enabling this feature, see the reset timer expires and voice-class sip reset timer expires commands in the Cisco IOS Voice Command Reference.

## Feature Information for Configuring Support for Expires Timer Reset on Receiving or Sending SIP 183 Message

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

Support for Expires Timer Reset on Receiving or Sending SIP 183 Message

Baseline Functionality

This feature enables support for resetting the Expires timer upon receipt of SIP 183 messages on Cisco Unified Communications
                                          Manager Express (Cisco Unified CME), a Cisco IOS voice gateway, or a Cisco Unified Border Element (Cisco UBE).

The following commands were introduced or modified: reset timer expires , and voice-class sip reset timer expires

## Prerequisites for Expires Timer Reset on Receiving or Sending SIP 183 Message

Before configuring support for Expires timer reset for SIP 183 on Cisco IOS SIP time-division multiplexing (TDM) gateways,
                           Cisco UBEs, or Cisco Unified CME, verify the SIP configuration within the VoIP network for the appropriate originating and
                           terminating gateways as described in the Cisco IOS SIP Configuration Guide .

## How to Configure Expires Timer Reset on Receiving or Sending SIP 183 Message

To configure the Support for Expires Timer Reset on Receiving or Sending SIP 183 Message feature, complete the tasks in this
                           section. You can enable this feature globally, using the reset timer expires command in voice service SIP configuration mode, or on a specific dial-peer using the voice-class sip reset timer expires command in dial peer voice configuration mode.

### Configure Reset of Expires Timer Globally

Perform this task to enable resetting of the Expires timer at the global level in SIP configuration (conf-serv-sip) mode.

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- sip

- reset timer expires 183

- exit

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

voice service voip

#### Example:

```
Router(config)# voice service voip
```

Enters voice service VoIP configuration mode.

Step 4

sip

#### Example:

```
Router(conf-voi-serv)# sip
```

Enters SIP configuration mode.

Step 5

reset timer expires 183

#### Example:

```
Router(conf-serv-sip)# reset timer expires 183
```

Enables resetting of the Expires timer upon receipt of SIP 183 messages globally.

Step 6

exit

#### Example:

```
Router(conf-serv-sip)# exit
```

Exits the current mode.

### Configure Reset of Expires Timer at the Dial-Peer Level

Perform this task to enable resetting of the Expires timer at the dial-peer level in dial peer voice configuration (config-dial-peer)
                                 mode.

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice tag voip

- voice-class sip reset timer expires 183

- exit

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

dial-peer voice tag voip

#### Example:

```
Router(config)# dial-peer voice 2 voip
```

Enters dial peer VoIP configuration mode.

Step 4

voice-class sip reset timer expires 183

#### Example:

```
Router(config-dial-peer)# voice-class sip reset timer expires 183
```

Enables resetting of the Expires timer upon receipt of SIP 183 messages on a specific dial peer.

Step 5

exit

#### Example:

```
Router(config-dial-peer)# exit
```

Exits the current mode.

| Feature Name | Releases | Feature Information |
|---|---|---|
| Support for Expires Timer Reset on Receiving or Sending SIP 183 Message | Baseline Functionality | This feature enables support for resetting the Expires timer upon receipt of SIP 183 messages on Cisco Unified Communications
                                          Manager Express (Cisco Unified CME), a Cisco IOS voice gateway, or a Cisco Unified Border Element (Cisco UBE). The following commands were introduced or modified: reset timer expires , and voice-class sip reset timer expires |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice service voip Example: Router(config)# voice service voip | Enters voice service VoIP configuration mode. |
| Step 4 | sip Example: Router(conf-voi-serv)# sip | Enters SIP configuration mode. |
| Step 5 | reset timer expires 183 Example: Router(conf-serv-sip)# reset timer expires 183 | Enables resetting of the Expires timer upon receipt of SIP 183 messages globally. |
| Step 6 | exit Example: Router(conf-serv-sip)# exit | Exits the current mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | dial-peer voice tag voip Example: Router(config)# dial-peer voice 2 voip | Enters dial peer VoIP configuration mode. |
| Step 4 | voice-class sip reset timer expires 183 Example: Router(config-dial-peer)# voice-class sip reset timer expires 183 | Enables resetting of the Expires timer upon receipt of SIP 183 messages on a specific dial peer. |
| Step 5 | exit Example: Router(config-dial-peer)# exit | Exits the current mode. |