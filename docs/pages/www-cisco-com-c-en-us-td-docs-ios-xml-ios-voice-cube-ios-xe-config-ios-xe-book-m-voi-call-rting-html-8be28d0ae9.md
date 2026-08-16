---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-call-rting-html-8be28d0ae9
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-call-rting.html
retrieved_at: 2026-08-16T15:46:11.914025+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Configure Call Routing Logic on Cisco UBE using the History-info Header

## Chapter: Configure Call Routing Logic on Cisco UBE using the History-info Header

# Configure Call Routing Logic on Cisco UBE using the History-info Header

The history-info header has the call or dialog history information. The receiving application uses the history-info header
                        information to determine how and why the call has reached it. SIP IOS GW does not utilize this information in History-Info
                        header. The information stored in the History-Info headers can be used to bypass the dial-peers that were already tried during
                        the course of a call, ensuring that the call is not being redirected again to the same target. The called-numbers and host
                        portion of request URI in History-Info headers will be compared with the matching dial-peers, if incase the comparison succeeds,
                        then those dial-peers will be bypassed.

## Feature Information for Call Routing logic on Cisco UBE using the History-info Header

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

Call routing logic on the Cisco Unified Border Element based on the information embedded in the history-info header

Baseline Functionality

The call-routing logic on Cisco UBE is enhanced by leveraging the information contained in the history-info header of SIP
                                          requests that are retargeted or routed across different domains. This approach uses the history-info header data to skip retargeting
                                          dial-peer entries already indicated within the header.

The following commands were introduced or modified: call-route history-info , and voice class sip call-route history-info

## Configure Call Routing Logic on Cisco UBE using the History-info Header Globally

Perform this task to configure call routing on history-info header at a global level in SIP configuration (conf-serv-sip)
                              mode.

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- sip

- call-route history-info

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

call-route history-info

### Example:

```
Router(conf-serv-sip)# call-route history-info
```

Configures call-route history-info header support globally.

Step 6

exit

### Example:

```
Router(conf-serv-sip)# exit
```

Exits the current mode.

## Configure Call Routing Logic on Cisco UBE using the History-info Header at the Dial-Peer Level

Perform this task to configure call routing on history-info header support at the dial-peer level, in dial peer voice configuration
                              (config-dial-peer) mode.

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice tag voip

- voice-class sip call-route history-info

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

voice-class sip call-route history-info

### Example:

```
Router(config-dial-peer)# voice-class sip call-route history-info
```

Configures call-route history-info header support for a dial peer.

Step 5

exit

### Example:

```
Router(config-dial-peer)# exit
```

Exits the current mode.

| Feature Name | Releases | Feature Information |
|---|---|---|
| Call routing logic on the Cisco Unified Border Element based on the information embedded in the history-info header | Baseline Functionality | The call-routing logic on Cisco UBE is enhanced by leveraging the information contained in the history-info header of SIP
                                          requests that are retargeted or routed across different domains. This approach uses the history-info header data to skip retargeting
                                          dial-peer entries already indicated within the header. The following commands were introduced or modified: call-route history-info , and voice class sip call-route history-info |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enters privileged EXEC mode, or other security level set by a system administrator. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice service voip Example: Router(config)# voice service voip | Enters voice service VoIP configuration mode. |
| Step 4 | sip Example: Router(conf-voi-serv)# sip | Enters SIP configuration mode. |
| Step 5 | call-route history-info Example: Router(conf-serv-sip)# call-route history-info | Configures call-route history-info header support globally. |
| Step 6 | exit Example: Router(conf-serv-sip)# exit | Exits the current mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enters privileged EXEC mode, or other security level set by a system administrator. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | dial-peer voice tag voip Example: Router(config)# dial-peer voice 2 voip | Enters dial peer VoIP configuration mode. |
| Step 4 | voice-class sip call-route history-info Example: Router(config-dial-peer)# voice-class sip call-route history-info | Configures call-route history-info header support for a dial peer. |
| Step 5 | exit Example: Router(config-dial-peer)# exit | Exits the current mode. |