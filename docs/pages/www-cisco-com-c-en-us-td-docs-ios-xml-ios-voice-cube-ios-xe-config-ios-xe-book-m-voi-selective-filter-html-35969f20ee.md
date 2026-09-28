---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-selective-filter-html-35969f20ee
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-selective-filter.html
retrieved_at: 2026-08-16T15:47:31.806088+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Selective Filtering of Outgoing Provisional Response on the Cisco Unified Border Element

## Chapter: Selective Filtering of Outgoing Provisional Response on the Cisco Unified Border Element

# Selective Filtering of Outgoing Provisional Response on the Cisco Unified Border Element

This feature adds support on the Cisco Unified Border Element (Cisco UBE) platforms for selective filtering of outgoing provisional
                        responses, including "180-Alerting" and "183-Session In Progress" responses. Selective filtering can be further based on the
                        availability of media information in the received provisional response.

Next Generation Network (NGN) restricts the UNI from sending a 183 response with Session Description Protocol (SDP) toward
                        the NGN network. Cisco Unified Communications Manager always sends a 183 response with SDP responses. It is necessary for
                        the Cisco UBE to block these responses to allow Cisco Unified Communications Manager to interwork within the Next Generation
                        network.

## Feature Information for Selective Filtering of Outgoing Provisional Response on the Cisco Unified Border Element

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

Selective Filtering of Outgoing Provisional Response on the Cisco Unified Border Element

Baseline Functionality

This feature adds support on Cisco UBE for selective filtering of outgoing provisional responses, including "180-Alerting"
                                          and "183-Session In Progress" responses. Selective filtering can be further based on the availability of media information
                                          in the received provisional response.

The following commands were introduced or modified: block , and voice-class sip block .

## Restrictions for Selective Filtering of Outgoing Provisional Response on the Cisco UBE

Blocking 180 and183 responses with or without the SDP requirement is to block 183 with SDP only.

## How to Configure Selective Filtering of Outgoing Provisional Response on the Cisco UBE

### Configure Selective Filtering of Outgoing Provisional Response on the Cisco UBE at the Global Level

To configure Selective Filtering of Outgoing Provisional Response on the Cisco UBE at the global level, perform the steps
                                 in this section:

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- sip

- block 183 sdp absent

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

Enters voice service configuration mode.

Step 4

sip

#### Example:

```
Router(conf-voi-serv)# sip
```

Enters voice service SIP configuration mode.

Step 5

block 183 sdp absent

#### Example:

```
Router(conf-serv-sip)# block 183 sdp absent
```

Filters outgoing provisional responses, including "180-Alerting" and "183-Session In Progress" responses.

Step 6

exit

#### Example:

```
Router(conf-serv-sip)# exit
```

Exits the current mode.

### Configure Selective Filtering of Outgoing Provisional Response on the Cisco UBE at the Dial Peer Level

To configure Selective Filtering of Outgoing Provisional Response on the Cisco UBE at the dial-peer level, configure the outgoing
                                 dial peer as follows:

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice number voip

- voice-class sip block 183 sdp present

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

dial-peer voice number voip

#### Example:

```
Router(config)# dial-peer voice 1 voip
```

Enters dial peer voice configuration mode.

Step 4

voice-class sip block 183 sdp present

#### Example:

```
Router(config-dial-peer)# voice-class sip block 183 sdp present
```

Filters outgoing provisional responses, including "180-Alerting" and "183-Session In Progress" responses.

Step 5

exit

#### Example:

```
Router(config-dial-peer)# exit
```

Exits the current mode.

| Feature Name | Releases | Feature Information |
|---|---|---|
| Selective Filtering of Outgoing Provisional Response on the Cisco Unified Border Element | Baseline Functionality | This feature adds support on Cisco UBE for selective filtering of outgoing provisional responses, including "180-Alerting"
                                          and "183-Session In Progress" responses. Selective filtering can be further based on the availability of media information
                                          in the received provisional response. The following commands were introduced or modified: block , and voice-class sip block . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice service voip Example: Router(config)# voice service voip | Enters voice service configuration mode. |
| Step 4 | sip Example: Router(conf-voi-serv)# sip | Enters voice service SIP configuration mode. |
| Step 5 | block 183 sdp absent Example: Router(conf-serv-sip)# block 183 sdp absent | Filters outgoing provisional responses, including "180-Alerting" and "183-Session In Progress" responses. |
| Step 6 | exit Example: Router(conf-serv-sip)# exit | Exits the current mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | dial-peer voice number voip Example: Router(config)# dial-peer voice 1 voip | Enters dial peer voice configuration mode. |
| Step 4 | voice-class sip block 183 sdp present Example: Router(config-dial-peer)# voice-class sip block 183 sdp present | Filters outgoing provisional responses, including "180-Alerting" and "183-Session In Progress" responses. |
| Step 5 | exit Example: Router(config-dial-peer)# exit | Exits the current mode. |