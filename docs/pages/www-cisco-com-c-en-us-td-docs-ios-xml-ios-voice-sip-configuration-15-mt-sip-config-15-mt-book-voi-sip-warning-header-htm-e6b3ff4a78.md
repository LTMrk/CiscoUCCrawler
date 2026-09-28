---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-sip-configuration-15-mt-sip-config-15-mt-book-voi-sip-warning-header-htm-e6b3ff4a78
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/sip/configuration/15-mt/sip-config-15-mt-book/voi-sip-warning-header.html
retrieved_at: 2026-08-20T23:46:06.025437+00:00
---

SIP Configuration Guide, Cisco IOS Release 15M&T

# SIP Configuration Guide, Cisco IOS Release 15M&T

Updated: November 25, 2014

Chapter: SIP Warning Header

## Chapter: SIP Warning Header

# SIP Warning Header

The Warning Header text and Warning Code in a Session Initiation Protocol (SIP) response are used to point to the exact cause
                        of failure. All system failures are, by default, reported in the warning header of a SIP error response 3xx/4xx/5xx. Reporting
                        of certain failures (categorized as threshold failures), which disclose system capacity can be controlled.

## Finding Feature Information

Your software release may not support all the features documented in this module. For the latest caveats and feature information,
                           see Bug Search Tool and the release notes for your platform and software release. To find information about the features documented in this module,
                           and to see a list of the releases in which each feature is supported, see the feature information table.

Use Cisco Feature Navigator to find information about platform support and Cisco software image support. To access Cisco Feature
                           Navigator, go to www.cisco.com/go/cfn . An account on Cisco.com is not required.

## Information About SIP Warning Header Debugging

The system level failures, which would be enhanced by returning a Warning Header with specific text in the appropriate SIP
                           response to point to the exact cause of failure are as follows:

The warn-header ext-text all command under voice service SIP configuration mode is used to enable or disable SIP warning header debugging. The default
                           behavior is to enable sending notification of all system failures in the SIP warning header.

## How to Configure SIP Warning Header

### Configuring SIP Warning Header Debugging

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- sip

- warn-header ext-text all

- warn-header ext-text suppress threshold-failures

- end

### DETAILED STEPS

enable

#### Example:

```
Device> enable
```

Enters privileged EXEC mode. Enter your password if prompted.

configure terminal

#### Example:

```
Device# configure terminal
```

Enters global configuration mode.

voice service voip

#### Example:

```
Device(config)# voice service voip
```

Enters global VoIP configuration mode.

sip

#### Example:

```
Device(conf-voi-serv)# sip
```

Enters voice service SIP configuration mode.

warn-header ext-text all

#### Example:

```
Device(conf-serv-sip)# warn-header ext-text all
```

Enables sending notification of all system failures in SIP Warning Header.

warn-header ext-text suppress threshold-failures

#### Example:

```
Device(conf-serv-sip)# warn-header ext-text suppress threshold-failures
```

Disables sending notification of threshold failures in SIP Warning Header.

end

#### Example:

```
Device(conf-serv-sip)# end
```

Returns to privileged EXEC mode.

### Troubleshooting and Debugging SIP Warning Header

### SUMMARY STEPS

- enable

- debug ccsip messages

### DETAILED STEPS

enable

#### Example:

```
Device> enable
```

Enables privileged EXEC mode.

debug ccsip messages

Shows all Session Initiation Protocol (SIP) Service Provider
                                             Interface (SPI) message tracing.
                                             This is a sample output showing the SIP response message with SIP
                                             Warning Header.

#### Example:

```
Device# debug ccsip messages

SIP/2.0 500 Internal Server Error Via: SIP/2.0/UDP 9.45.33.11:5081;branch=z9hG4bK-10854-1-0
  From: sipp <sip:111@9.45.33.11:5081>;tag=10854SIPpTag001
  To: sut <sip:222@9.43.29.50:5060>;tag=38404-23F2
  Date: Tue, 05 Feb 2013 05:49:37 GMT
  Call-ID: 1-10854@9.45.33.11
  CSeq: 1 INVITE
  Allow-Events: telephone-event
  Warning: 399 9.43.29.50 "Transcoder Not Configured“  //SIP response message with SIP Warning Header//
  Server: Cisco-SIPGateway/IOS-15.3.20130202.123643.
  Reason: Q.850;cause=16
  Content-Length: 0
```

## Feature Information for SIP Warning Header Enhancements

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

SIP Warning Header Enhancements

15.3(2)T

The Warning Header text and Warning Code in a Session Initiation Protocol (SIP) response are used to point to the exact cause
                                          of failure. All system failures are, by default, reported in the warning header of a SIP error response 3xx/4xx/5xx. Reporting
                                          of certain failures (categorized as threshold failures), which disclose system capacity can be controlled.

| Failure Scenarios | SIP Warning Header Phrase |
|---|---|
| Dial-peer mismatch | “No matching outgoing dial-peer” |
| Spike count exceeds call spike threshold (Threshold Failure) | “Call Spiked. Concurrent calls exceed Spike Count Threshold” |
| Maximum number of connections set per peer exceeded (Threshold Failure) | “Maximum Number of Connections reached” |
| QoS Negotiation | “QoS Negotiation Failure” |
| SRTP fallback failure | “Cannot fallback to RTP. SRTP configured on dial peer” |
| Transcoder not configured | “Transcoder Not Configured” |
| Transcoder reservation failure during SRTP-RTP Interworking | “Transcoder reservation failure during SRTP-RTP I/W” |
| Transcoder reservation for transrating scenario | “Transcoder reservation failure for transrating scenario” |
| SIP Service Shutdown | “SIP Service is Shutdown” |
| Error binding the local IP Address due invalid GW mode | “Local IP Bind Failure. Invalid GW mode of operation” |
| Inconsistent URI Scheme in a SIP Message | “Inconsistent URI scheme in Req-URI/To Header/Contact Header” |
| Join header processing error | “Error parsing Join Header” |
| Proxy-Authorization Header | “Error parsing Proxy-Authorization Header” |
| SIP Registrar disabled | “Registrar is not enabled” |
| SIP Registrar process not up | “Registrar process is not up” |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enters privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | voice service voip Example: Device(config)# voice service voip | Enters global VoIP configuration mode. |
| Step 4 | sip Example: Device(conf-voi-serv)# sip | Enters voice service SIP configuration mode. |
| Step 5 | warn-header ext-text all Example: Device(conf-serv-sip)# warn-header ext-text all | Enables sending notification of all system failures in SIP Warning Header. Note Use the no warn-header ext-text all command to   disable sending notification of all system failures in SIP Warning Header. | Note | Use the no warn-header ext-text all command to   disable sending notification of all system failures in SIP Warning Header. |
| Note | Use the no warn-header ext-text all command to   disable sending notification of all system failures in SIP Warning Header. |
| Step 6 | warn-header ext-text suppress threshold-failures Example: Device(conf-serv-sip)# warn-header ext-text suppress threshold-failures | Disables sending notification of threshold failures in SIP Warning Header. Note Use the no warn-header ext-text suppress threshold-failures command to   enable sending notification of threshold failures in SIP Warning Header. | Note | Use the no warn-header ext-text suppress threshold-failures command to   enable sending notification of threshold failures in SIP Warning Header. |
| Note | Use the no warn-header ext-text suppress threshold-failures command to   enable sending notification of threshold failures in SIP Warning Header. |
| Step 7 | end Example: Device(conf-serv-sip)# end | Returns to privileged EXEC mode. |

| Note | Use the no warn-header ext-text all command to   disable sending notification of all system failures in SIP Warning Header. |
|---|---|

| Note | Use the no warn-header ext-text suppress threshold-failures command to   enable sending notification of threshold failures in SIP Warning Header. |
|---|---|

| Step 1 | enable Example: Device> enable Enables privileged EXEC mode. |
|---|---|
| Step 2 | debug ccsip messages Shows all Session Initiation Protocol (SIP) Service Provider
                                             Interface (SPI) message tracing.
                                             This is a sample output showing the SIP response message with SIP
                                             Warning Header. Example: Device# debug ccsip messages

SIP/2.0 500 Internal Server Error Via: SIP/2.0/UDP 9.45.33.11:5081;branch=z9hG4bK-10854-1-0
  From: sipp <sip:111@9.45.33.11:5081>;tag=10854SIPpTag001
  To: sut <sip:222@9.43.29.50:5060>;tag=38404-23F2
  Date: Tue, 05 Feb 2013 05:49:37 GMT
  Call-ID: 1-10854@9.45.33.11
  CSeq: 1 INVITE
  Allow-Events: telephone-event
  Warning: 399 9.43.29.50 "Transcoder Not Configured“  //SIP response message with SIP Warning Header//
  Server: Cisco-SIPGateway/IOS-15.3.20130202.123643.
  Reason: Q.850;cause=16
  Content-Length: 0 |

| Feature Name | Releases | Feature Information |
|---|---|---|
| SIP Warning Header Enhancements | 15.3(2)T | The Warning Header text and Warning Code in a Session Initiation Protocol (SIP) response are used to point to the exact cause
                                          of failure. All system failures are, by default, reported in the warning header of a SIP error response 3xx/4xx/5xx. Reporting
                                          of certain failures (categorized as threshold failures), which disclose system capacity can be controlled. |