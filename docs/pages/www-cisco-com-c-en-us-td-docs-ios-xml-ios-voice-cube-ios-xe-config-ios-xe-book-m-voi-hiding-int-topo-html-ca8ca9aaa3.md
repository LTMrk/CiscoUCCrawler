---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-hiding-int-topo-html-ca8ca9aaa3
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-hiding-int-topo.html
retrieved_at: 2026-08-16T15:46:41.303448+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Hiding the Internal Topology Information Embedded Within the History-info Header at the Cisco UBE

## Chapter: Hiding the Internal Topology Information Embedded Within the History-info Header at the Cisco UBE

# Hiding the Internal Topology Information Embedded Within the History-info Header at the Cisco UBE

SIP History-info stores information on address, topology and so on. Cisco UBE has the address hiding security feature where
                        only the host section of a History-Info header is masked with the CUBE address. However, it does not hide the topology information
                        like the details of the targets where a request was tried upon. It is important to strip the topology information from Cisco
                        UBE before it is passed on to an external device. When the topology hiding for history-info is enabled, the diversion headers
                        are also stripped from the history-info header. Topology information hiding has to be enabled on both inbound and outbound
                        call legs. For example, if topology informatione is enabled only on the outbound dial-peer, this results in stripping all
                        the History-info headers it received from the inbound leg and it sends just the single History-info header. However, on the
                        inbound leg, all the History-info headers received from the outbound leg will be passed on to the external devices. If this
                        feature is enabled on both inbound and outbound dialpeers, then the History-info headers will be stripped for both inbound
                        and outbound legs of Cisco UBE.

## Feature Information for Hiding Internal Topology in the History-info Header

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

Hiding the Internal Topology Information Embedded Within the History-info Header at the Cisco UBE

Baseline Functionality

This feature enables privacy across the enterprise domain by stripping internal topology information from the history-info
                                          header.

The following commands were introduced or modified: privacy policy , and voice class sip privacy policy

## Restrictions for Hiding the Internal Topology Information

The user needs to be in the same network as the network in which the call is received.

Topology hiding will result in the History-Info headers received on one call leg to be stripped on the other leg and this
                                 could result in the call-routing functionality to disfunction. Hence, topology hiding and call-routing are mutually exclusive
                                 and cannot function together.

## Hiding Internal Toplogy Information in History-info Header at global level

Perform this task to hide topology information in history-info header at a global level in SIP configuration (conf-serv-sip)
                              mode.

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- sip

- privacy policy strip diversion

- privacy policy strip history-info

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

privacy policy strip diversion

### Example:

```
Router(conf-serv-sip)# privacy policy strip history-info
```

Srips the diversion headers received from the next call leg

Step 6

privacy policy strip history-info

### Example:

```
Router(conf-serv-sip)# privacy policy strip history-info
```

Strips the topology information from the history-info header.

Step 7

exit

### Example:

```
Router(conf-serv-sip)# exit
```

Exits the current mode.

## Hiding Internal Toplogy Information in History-info Header at the Dial-Peer Level

Perform this task to hide topology information in history-info header header support at the dial-peer level, in dial peer
                              voice configuration (config-dial-peer) mode.

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice tag voip

- voice class sip privacy policy strip diversion

- voice class sip privacy policy strip history-info

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

voice class sip privacy policy strip diversion

### Example:

```
Router(config-dial-peer)# voice-class sip call-route history-info
```

Srips the diversion headers received from the next call leg.

Step 5

voice class sip privacy policy strip history-info

### Example:

```
Router(conf-serv-sip)# privacy policy strip history-info
```

Strips the topology information from the history-info header.

Step 6

exit

### Example:

```
Router(config-dial-peer)# exit
```

Exits the current mode.

| Feature Name | Releases | Feature Information |
|---|---|---|
| Hiding the Internal Topology Information Embedded Within the History-info Header at the Cisco UBE | Baseline Functionality | This feature enables privacy across the enterprise domain by stripping internal topology information from the history-info
                                          header. The following commands were introduced or modified: privacy policy , and voice class sip privacy policy |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enters privileged EXEC mode, or other security level set by a system administrator. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice service voip Example: Router(config)# voice service voip | Enters voice service VoIP configuration mode. |
| Step 4 | sip Example: Router(conf-voi-serv)# sip | Enters SIP configuration mode. |
| Step 5 | privacy policy strip diversion Example: Router(conf-serv-sip)# privacy policy strip history-info | Srips the diversion headers received from the next call leg |
| Step 6 | privacy policy strip history-info Example: Router(conf-serv-sip)# privacy policy strip history-info | Strips the topology information from the history-info header. |
| Step 7 | exit Example: Router(conf-serv-sip)# exit | Exits the current mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enters privileged EXEC mode, or other security level set by a system administrator. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | dial-peer voice tag voip Example: Router(config)# dial-peer voice 2 voip | Enters dial peer VoIP configuration mode. |
| Step 4 | voice class sip privacy policy strip diversion Example: Router(config-dial-peer)# voice-class sip call-route history-info | Srips the diversion headers received from the next call leg. |
| Step 5 | voice class sip privacy policy strip history-info Example: Router(conf-serv-sip)# privacy policy strip history-info | Strips the topology information from the history-info header. |
| Step 6 | exit Example: Router(config-dial-peer)# exit | Exits the current mode. |