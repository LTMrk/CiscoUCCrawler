---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-conf-err-resp-html-35871199b7
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-conf-err-resp.html
retrieved_at: 2026-08-16T15:47:10.357819+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Configure an Error Response Code upon an Out-of-Dialog OPTIONS Ping Failure

## Chapter: Configure an Error Response Code upon an Out-of-Dialog OPTIONS Ping Failure

# Configure an Error Response Code upon an Out-of-Dialog OPTIONS Ping Failure

Cisco Unified Border Element (Cisco UBE) provides an option to configure the error response code when a dial peer is busied
                        out because of an Out-of-Dialog OPTIONS ping failure.

The OPTIONS ping mechanism monitors the status of a remote Session Initiation Protocol (SIP) server, proxy or endpoints. Cisco
                        UBE monitors these endpoints periodically. When there is no response from these monitored endpoints, the configured dial peer
                        is busied out. If the dial-peer endpoint is busied out due to an OPTIONS ping failure, the call is passed on to the next dial-peer
                        endpoint if an alternate dial peer is configured for the same destination. Otherwise the error response 404 is sent. This
                        feature provides the option of configuring the error response code to reroute the call. Therefore when a dial peer is busied
                        out due to the OPTIONS ping failure, the SIP error code configured in the inbound dial-peer is sent as a response.

To configure the SIP error code response, perform the following tasks:

Configure an Error Response Code upon an Out-of-Dialog OPTIONS Ping Failure at the Global Level

Configure an Error Response Code upon an Out-of-Dialog OPTIONS Ping Failure at the Dial Peer Level

## Feature Information for Configure an Error Response Code upon an Out-of-Dialog OPTIONS Ping Failure

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

Error Response Code upon an Out-of-Dialog OPTIONS Ping Failure

Baseline Functionality

This feature provides option to configure the error response code when a dial peer is busied out because of an Out-of-Dialog
                                          OPTIONS ping failure.

The following commands were introduced or modified in this release: error-code-override options-keepalive failure , and voice-class sip error-code-override options-keepalive failure

## Prerequisites for Configuring an Error Response Code upon an Out-of-Dialog OPTIONS Ping Failure

The Cisco UBE Out-of-Dialog (OOD) OPTIONS Ping for specified SIP servers or Endpoints feature should be configured before
                                 configuring this error response code for a ping OPTIONS failure.

## Restrictions for Configuring an Error Response Code upon an Out-of-Dialog OPTIONS Ping Failure

The error code configuration will not have any effect if it is configured on the outbound dial peer.

## Configure an Error Response Code upon an Out-of-Dialog OPTIONS Ping Failure at the Global Level

The table below describes the SIP error codes.

Error Code Number

Description

400

Bad Request

401

Unauthorized

402

Payment Required

403

Forbidden

404

Not Found

408

Request Timed Out

416

Unsupported URI

480

Temporarily Unavailable

482

Loop Detected

484

Address Incomplete

486

Busy Here

487

Request Terminated

488

Not Acceptable Here

500-599

SIP 5xx--Server/Service Failure

500

Internal Server Error

502

Bad Gateway

503

Service Unavailable

600-699

SIP 6xx--Global Failure

To configure the error response code for the OPTIONS ping failure to support the Cisco Unified Border Element at the global
                              level, perform the steps in this section.

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- sip

- error-code-override options-keepalive failure sip-status-code-number

- end

### DETAILED STEPS

Step 1

enable

### Example:

```
Router> enable
```

Enables privileged EXEC mode.

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

Enters voice service configuration mode.

Step 4

sip

### Example:

```
Router(conf-voi-serv)# sip
```

Enters voice service SIP configuration mode.

Step 5

error-code-override options-keepalive failure sip-status-code-number

### Example:

```
Router(conf-serv-sip)# error-code-override options-keepalive failure 402
```

Configures the specified SIP error code number.

sip-status-code-number --SIP status code to be sent for an options keepalive failure. Range: 400 to 699. Default: 503.

The table above provides more details about these error codes.

Step 6

end

### Example:

```
Router(conf-serv-sip)# end
```

Exits voice service SIP configuration mode and returns to privileged EXEC mode.

## Configure an Error Response Code upon an Out-of-Dialog OPTIONS Ping Failure at the Dial Peer Level

To configure the error response code for the OPTIONS ping failure to support the Cisco Unified Border Element at the dial-peer
                              level, perform the steps in this section.

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice voice-dial-peer-tag voip

- voice-class sip error-code-error-override options-keepalive failure { sip-status-code-number | system }

- end

### DETAILED STEPS

Step 1

enable

### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

dial-peer voice voice-dial-peer-tag voip

### Example:

```
Router(config)# dial-peer voice 234 voip
```

Enters dial peer voice configuration mode.

Step 4

voice-class sip error-code-error-override options-keepalive failure { sip-status-code-number | system }

### Example:

```
Router(config-dial-peer)# voice-class sip error-code-override options-keepalive failure 500
```

Configures the specified SIP error code number.

sip-status-code-number --SIP status code to be sent for an options keepalive failure. Range: 400 to 699. Default: 503.

Configure an Error Response Code upon an Out-of-Dialog OPTIONS Ping Failure at the Dial Peer Level provides more details about these error codes.

If the system keyword is configured, the global level configuration will override the dial-peer configuration.

Step 5

end

### Example:

```
Router(config-dial-peer)# end
```

Exits dial peer voice configuration mode and returns to privileged EXEC mode.

## Troubleshooting Tips

The following debug commands display any error that occurs with the error code response:

debug ccsip messages-- shows SIP messages.

```
Router# debug ccsip messages SIP Call messages tracing is enabled
```

debug ccsip all --shows all SIP-related debugging.

```
Router# debug ccsip all This may severely impact system performance. Continue? [confirm]
All SIP Call tracing is enabled
```

| Feature Name | Releases | Feature Information |
|---|---|---|
| Error Response Code upon an Out-of-Dialog OPTIONS Ping Failure | Baseline Functionality | This feature provides option to configure the error response code when a dial peer is busied out because of an Out-of-Dialog
                                          OPTIONS ping failure. The following commands were introduced or modified in this release: error-code-override options-keepalive failure , and voice-class sip error-code-override options-keepalive failure |

| Error Code Number | Description |
|---|---|
| 400 | Bad Request |
| 401 | Unauthorized |
| 402 | Payment Required |
| 403 | Forbidden |
| 404 | Not Found |
| 408 | Request Timed Out |
| 416 | Unsupported URI |
| 480 | Temporarily Unavailable |
| 482 | Loop Detected |
| 484 | Address Incomplete |
| 486 | Busy Here |
| 487 | Request Terminated |
| 488 | Not Acceptable Here |
| 500-599 | SIP 5xx--Server/Service Failure |
| 500 | Internal Server Error |
| 502 | Bad Gateway |
| 503 | Service Unavailable |
| 600-699 | SIP 6xx--Global Failure |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice service voip Example: Router(config)# voice service voip | Enters voice service configuration mode. |
| Step 4 | sip Example: Router(conf-voi-serv)# sip | Enters voice service SIP configuration mode. |
| Step 5 | error-code-override options-keepalive failure sip-status-code-number Example: Router(conf-serv-sip)# error-code-override options-keepalive failure 402 | Configures the specified SIP error code number. sip-status-code-number --SIP status code to be sent for an options keepalive failure. Range: 400 to 699. Default: 503. The table above provides more details about these error codes. |
| Step 6 | end Example: Router(conf-serv-sip)# end | Exits voice service SIP configuration mode and returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | dial-peer voice voice-dial-peer-tag voip Example: Router(config)# dial-peer voice 234 voip | Enters dial peer voice configuration mode. |
| Step 4 | voice-class sip error-code-error-override options-keepalive failure { sip-status-code-number \| system } Example: Router(config-dial-peer)# voice-class sip error-code-override options-keepalive failure 500 | Configures the specified SIP error code number. sip-status-code-number --SIP status code to be sent for an options keepalive failure. Range: 400 to 699. Default: 503. Configure an Error Response Code upon an Out-of-Dialog OPTIONS Ping Failure at the Dial Peer Level provides more details about these error codes. Note If the system keyword is configured, the global level configuration will override the dial-peer configuration. | Note | If the system keyword is configured, the global level configuration will override the dial-peer configuration. |
| Note | If the system keyword is configured, the global level configuration will override the dial-peer configuration. |
| Step 5 | end Example: Router(config-dial-peer)# end | Exits dial peer voice configuration mode and returns to privileged EXEC mode. |

| Note | If the system keyword is configured, the global level configuration will override the dial-peer configuration. |
|---|---|