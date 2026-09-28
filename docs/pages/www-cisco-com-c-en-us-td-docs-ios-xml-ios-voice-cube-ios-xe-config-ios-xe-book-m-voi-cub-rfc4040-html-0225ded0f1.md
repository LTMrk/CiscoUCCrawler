---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-cub-rfc4040-html-0225ded0f1
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-cub-rfc4040.html
retrieved_at: 2026-08-16T15:47:36.014479+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: RFC 4040-Based Clear Channel Codec Negotiation for SIP Calls

## Chapter: RFC 4040-Based Clear Channel Codec Negotiation for SIP Calls

# RFC 4040-Based Clear Channel Codec Negotiation for SIP Calls

The RFC 4040-Based Clear Channel Codec Negotiation for SIP Calls feature globally enables RFC 4040-based clear-channel codec
                        negotiation [CLEARMODE/8000] for SIP calls on a Cisco IOS voice gateway or Cisco UBE. RFC 4040-based clear-channel codec negotiation
                        allows Cisco IOS voice gateways and Cisco UBEs to successfully interoperate with third-party SIP gateways that do not support
                        legacy Cisco IOS clear-channel codec encapsulation [X-CCD/8000].

## Feature Information for RFC 4040-Based Clear Channel Codec Negotiation for SIP Calls

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

RFC 4040-Based Clear Channel Codec Negotiation for SIP Calls

Baseline Functionality

This feature adds support for RFC 4040-based clear channel codec Negotiation for SIP calls.

The following commands were modified: encap clear-channel standard , and voice-class sip encap clear-channel

## Restrictions for RFC 4040-Based Clear Channel Codec Negotiation for SIP Calls

This feature is supported on Cisco IOS SIP time division multiplexing (TDM) gateways and Cisco Unified Border Elements (Cisco
                                 UBEs).

## Information about RFC 4040-Based Clear Channel Codec Negotiation for SIP Calls

When the encap clear-channel standard command is enabled on a Cisco IOS voice gateway or Cisco UBE, calls using the Cisco IOS clear channel codec are translated
                           into calls that use CLEARMODE/8000 so that the calls do not get rejected when they reach third-party SIP gateways.

To enable RFC 4040-based clear-channel codec negotiation for SIP calls on an individual dial peer, overriding the global configuration
                           for the Cisco IOS voice gateway or Cisco UBE, use the voice-class sip encap clear-channel standard command in dial peer voice configuration mode. To globally disable RFC 4040-based clear-channel codec negotiation on a Cisco
                           IOS voice gateway or Cisco UBE, use the no encap clear-channel standard command in voice service SIP configuration mode.

## How to Configure RFC 4040-Based Clear Channel Codec Negotiation for SIP Calls

This feature can be enabled globally for all dial peers or on an individual dial peer (which overrides the global configuration,
                           if one is in effect). Depending on your requirements, complete one of the following tasks:

### Configure RFC 4040-Based Clear Channel Codec Negotiation for SIP Calls Globally for All Dial Peers

To configure RFC 4040-based clear-channel code negotiation globally for all dial peers on a Cisco IOS voice gateway or Cisco
                                 UBE, complete this task:

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- sip

- encap clear-channel standard

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

encap clear-channel standard

#### Example:

```
Router(conf-serv-sip)# encap clear-channel standard
```

Globally enables RFC 4040-based clear-channel codec negotiation [CLEARMODE/8000] for SIP calls on a Cisco IOS voice gateway
                                             or Cisco UBE.

### Configure RFC 4040-Based Clear Channel Codec Negotiation for SIP Calls for a Single Dial Peer

To configure RFC 4040-based clear-channel code negotiation for one dial peer on a Cisco IOS voice gateway or Cisco UBE, complete
                                 this task:

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice 1 voip

- voice-class sip encap clear-channel standard

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

dial-peer voice 1 voip

#### Example:

```
Router(config)# dial-peer voice 1 voip
```

Enters dial peer voice configuration mode.

Step 4

voice-class sip encap clear-channel standard

#### Example:

```
Router(config-dial-peer)# voice-class sip encap clear-channel standard
```

Enables RFC 4040-based clear-channel codec negotiation for SIP calls on an individual dial peer, overriding the global setting
                                             on a Cisco IOS voice gateway or Cisco UBE.

You can also configure a specific dial peer to use global configuration settings for clear-channel codec negotiation.To enable
                                                         this capability, substitute the voice-class sip encap clear-channel system command in this step of the configuration.

| Feature Name | Releases | Feature Information |
|---|---|---|
| RFC 4040-Based Clear Channel Codec Negotiation for SIP Calls | Baseline Functionality | This feature adds support for RFC 4040-based clear channel codec Negotiation for SIP calls. The following commands were modified: encap clear-channel standard , and voice-class sip encap clear-channel |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice service voip Example: Router(config)# voice service voip | Enters voice service configuration mode. |
| Step 4 | sip Example: Router(conf-voi-serv)# sip | Enters voice service SIP configuration mode. |
| Step 5 | encap clear-channel standard Example: Router(conf-serv-sip)# encap clear-channel standard | Globally enables RFC 4040-based clear-channel codec negotiation [CLEARMODE/8000] for SIP calls on a Cisco IOS voice gateway
                                             or Cisco UBE. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | dial-peer voice 1 voip Example: Router(config)# dial-peer voice 1 voip | Enters dial peer voice configuration mode. |
| Step 4 | voice-class sip encap clear-channel standard Example: Router(config-dial-peer)# voice-class sip encap clear-channel standard | Enables RFC 4040-based clear-channel codec negotiation for SIP calls on an individual dial peer, overriding the global setting
                                             on a Cisco IOS voice gateway or Cisco UBE. Note You can also configure a specific dial peer to use global configuration settings for clear-channel codec negotiation.To enable
                                                         this capability, substitute the voice-class sip encap clear-channel system command in this step of the configuration. | Note | You can also configure a specific dial peer to use global configuration settings for clear-channel codec negotiation.To enable
                                                         this capability, substitute the voice-class sip encap clear-channel system command in this step of the configuration. |
| Note | You can also configure a specific dial peer to use global configuration settings for clear-channel codec negotiation.To enable
                                                         this capability, substitute the voice-class sip encap clear-channel system command in this step of the configuration. |

| Note | You can also configure a specific dial peer to use global configuration settings for clear-channel codec negotiation.To enable
                                                         this capability, substitute the voice-class sip encap clear-channel system command in this step of the configuration. |
|---|---|