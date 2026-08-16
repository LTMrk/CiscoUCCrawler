---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-thirdp-guid-recording-html-12f9e24b1e
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_thirdp-guid-recording.html
retrieved_at: 2026-08-16T15:52:22.076817+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Third-Party GUID Capture

## Chapter: Third-Party GUID Capture

# Third-Party GUID Capture

## Overview

The Third-Party GUID Capture for Correlation Between Calls and SIP-based Recording feature provides support for the transmission
                           of globally unique identifiers (GUIDs) received from a third-party private branch exchange (PBX) to the recording server using
                           an established Session Initiation Protocol (SIP) session, making Cisco Unified Border Element (CUBE) recording more interoperable with third-party vendors.

Enterprise call control systems such as the Cisco Unified Communications Manager (CUCM) use globally unique identifiers (GUIDs)
                           to correlate the multiple call legs of a single call. The call can then be forwarded or transferred, creating additional call
                           legs associated with the same GUID. When recording is configured, CUBE initiates a SIP session with a recorder server and
                           forks the media packets it receives or transmits, along with participant information like called number, calling number, Remote
                           Party ID (RPID), and P-Asserted-Identity (PAI).

While the Cisco-Guid header (used by CUCM) is transmitted to the recording server, third-party GUIDs are not. Third-party
                           GUIDs can be received through an INVITE message or a 200 OK message, depending on whether the third-party PBX is initiating
                           the call [caller] or receiving the call [callee].

Forwarding the GUID to the recording server enables correlation between call records of the PBX and the recording server.

Starting from Cisco IOS XE 17.18.1a release, third-party GUID header capture is extended to mid call messages such as midcall INVITE and REFER. This enhancement
                           is necessary to support third-party PBX-controlled call transfers. The third-party GUID header can be received either in the
                           REFER or midcall INVITE request, or in the 200 OK response to a midcall INVITE. Forwarding the midcall GUID updates to the
                           recording server enables correlation between call records of the PBX and the recording server for midcall transfers.

### Feature Information

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

Third-Party GUID capture for correlation between call transfers and SIP-based recording

Cisco IOS XE 17.18.1a

The Third-Party GUID capture for correlation between calls and SIP-based recording feature is extended to support transmission
                                          of globally unique identifiers (GUIDs) to the recording server when received from a third-party private branch exchange (PBX)
                                          during call transfers.

Third-Party GUID Capture for Correlation Between Calls and SIP-based Recording

Baseline Functionality

The Third-Party GUID capture for correlation between calls and SIP-based recording feature provides support for the transmission
                                          of globally unique identifiers (GUIDs) received from a third-party private branch exchange (PBX) to the recording server via
                                          an established SIP session, making CUBE recording more interoperable with third-party vendors.

## Restrictions for Third-Party Header Capture for Correlation Between Calls and SIP-based Recording

The third-party GUID must be received through the following:

INVITE or 200 OK for INVITE: Depending on whether the third-party PBX is initiating the call [caller] or receiving the call
                                       (callee).

REFER request: For call transfers.

Midcall INVITE or 200 OK for midcall INVITE: Depending on when the call transfer is committed.

Other request or response messages are not supported.

The third-party GUID can only be received through the primary inbound call leg, the primary outbound call leg, or the transferred
                                 to call leg.

In a dual forking (two recoders) scenario, during a consult call transfer, the third-party header from the REFER message is
                                 forwarded only to the recording session connected with the transferee.

The third-party header included in midcall INVITEs will only be forwarded to the recorder if a pre-existing recording session
                                 is active.

## Configure Third-Party Header Capture for Correlation Between Calls and SIP-based Recording

To capture the third-party header and forward it to the recording server, you need to copy a third-party header that CUBE
                              receives, configure a SIP copylist for that header, and apply it to the primary inbound, primary outbound, and transferred
                              call leg dial-peer. A SIP profile is configured to copy this incoming header to a user-defined variable and apply it to an
                              outgoing header on the recording leg dial-peer.

In cases where the same headers are received in multiple messages, the headers are forwarded from only one of those messages,
                                          following this order of priority:

REFER

INVITE or mid-call INVITE request

200 OK response of INVITE or mid-call INVITE

### SUMMARY STEPS

- enable

- configure terminal

- voice class sip-copylist tag

- sip-header ThirdParty-headername

- exit

- dial-peer voice inbound-dial-peer-tag voip

- voice class sip-copylist tag

- exit

- voice class sip-profiles profile-id

- rule tag request INVITE peer-header sip header-to-copy copy header-value-to-match copy-variable

- rule tag request INVITE sip-header header-to-add add header-value-to-add

- rule tag request INVITE sip-header header-to-modify modify header-value-to-match header-value-to-replace

- rule tag request REINVITE peer-header sip header-to-copy copy header-value-to-match copy-variable

- rule tag request REINVITE sip-header header-to-add add header-value-to-add

- rule tag request REINVITE sip-header header-to-modify modify header-value-to-match header-value-to-replace

- exit

- dial-peer voice recorder-dial-peer-tag voip

- voice-class sip profiles profile-tag

- end

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

Enters global configuration mode.

Step 3

voice class sip-copylist tag

### Example:

```
Device(config)# voice class sip-copylist 100
```

Configures a list of entities to be sent to a peer call leg and enters voice class configuration mode.

Step 4

sip-header ThirdParty-headername

### Example:

```
Device(config-class)# sip-header Cisco-GUID
```

Specifies that the third-party GUID header must be copied from the inbound dial-peer leg to the outbound dial-peer call leg.

The third-party header name can be configured to any desired header that needs to be forwarded to the SIP recorder for call
                                                      correlation.

Step 5

exit

### Example:

```
Device(config-class)# exit
```

Exits voice class configuration mode.

Step 6

dial-peer voice inbound-dial-peer-tag voip

### Example:

```
Device(config)# dial-peer voice 2 voip
```

Enters inbound dial-peer configuration mode.

Step 7

voice class sip-copylist tag

### Example:

```
Device(config-dial-peer)# voice class sip-copylist 100
```

Applies the copy list to the dial-peer.

Step 8

exit

### Example:

```
Device(config-dial-peer)# exit
```

Exits to global configuration mode.

Step 9

voice class sip-profiles profile-id

### Example:

```
Device(config)# voice class sip-profiles 10
```

Creates a SIP profile and enters voice class configuration mode.

Step 10

rule tag request INVITE peer-header sip header-to-copy copy header-value-to-match copy-variable

### Example:

```
Device(config-class)# rule 1 request INVITE peer-header sip Cisco-GUID copy "(.*)" u01
```

Step 11

rule tag request INVITE sip-header header-to-add add header-value-to-add

### Example:

```
Device(config-class)# rule 2 request INVITE sip-header Unsupported add "Unsupported: Dummy Header"
```

The sip-header: "Unsupported: Dummy Header" is modified to the actual header in the next step.

Step 12

rule tag request INVITE sip-header header-to-modify modify header-value-to-match header-value-to-replace

### Example:

```
Device(config-class)# rule 3 request INVITE sip-header Unsupported modify ".*" "Cisco-GUID: \u01"
```

Step 13

rule tag request REINVITE peer-header sip header-to-copy copy header-value-to-match copy-variable

### Example:

```
Device(config-class)# rule 4 request REINVITE peer-header sip Cisco-GUID copy "(.*)" u03
```

Step 14

rule tag request REINVITE sip-header header-to-add add header-value-to-add

### Example:

```
Device(config-class)# rule 5 request REINVITE sip-header Unsupported add "Unsupported: Dummy Header"
```

Step 15

rule tag request REINVITE sip-header header-to-modify modify header-value-to-match header-value-to-replace

### Example:

```
Device(config-class)# rule 6 request REINVITE sip-header Unsupported modify ".*" "Cisco-GUID: \u03"
```

Step 16

exit

### Example:

```
Device(config-class)# exit
```

Exits to global configuration mode.

Step 17

dial-peer voice recorder-dial-peer-tag voip

### Example:

```
Device(config)# dial-peer voice 3 voip
```

Enters the dial peer configuration mode for the specified outbound recorder dial-peer.

Step 18

voice-class sip profiles profile-tag

### Example:

```
Device(config-dial-peer)# voice-class sip profiles 10
```

Applies the SIP profile to the recording dial-peer.

Step 19

end

### Example:

```
Device(config-dial-peer)# end
```

Exits to privileged EXEC mode.

## Verify Third-Party Header Capture for Correlation Between Calls and SIP-based Recording

Following are the examples for debug ccsip messages command displaying Session Initiation Protocol (SIP) Service Provider Interface (SPI) messages for an INVITE, a mid call
                           INVITE, 200 OK for an INVITE, 200 OK for a mid call INVITE, and REFER messages.

debug ccsip messages for an INVITE, or a mid call INVITE message.

Displays all Session Initiation Protocol (SIP) Service Provider Interface (SPI) messages for an INVITE, or a mid call INVITE
                                 message.

```
Received:
INVITE sip:5678@10.10.10.19:5060 SIP/2.0
Via: SIP/2.0/UDP 10.10.10.16:21000;branch=z9hG4bK-61735-1-10
From:  <sip:5678@10.10.10.16>;tag=1
To:  "sipp " <sip:sipp@10.10.10.19>;tag=2CEB93-575
Call-ID: E2883F8B-191A11F0-8065E68D-1DE0D2BE@10.10.10.19
CSeq: 11 INVITE
Contact: sip:5678@10.10.10.16:21000
Expires: 300
Max-Forwards: 70
Subject: Performance Test
Content-Type: application/sdp Cisco-Guid: 1055557248-0520212713-0000000109-2759698624 Content-Length:   154
```

debug ccsip messages for a 200 OK for an INVITE, or a 200 OK for a mid call INVITE message.

Displays all Session Initiation Protocol (SIP) Service Provider Interface (SPI) messages for a 200 OK message.

```
Received: SIP/2.0 200 OK Via:  SIP/2.0/UDP 9.44.29.32:5060;branch=z9hG4bK121F62
From: "sipp " <sip:1111000010@9.44.29.32>;tag=906F9C-21B9
To: "sut" <sip:4321@9.0.0.120>;tag=30050SIPpTag0111
Call-ID: 67B65D26-473711E3-8029B214-265DCDFE@9.44.29.32
CSeq:  101 INVITE
Contact: <sip:9.0.0.120:6019;transport=UDP> Cisco-Guid: 1055557248-0520212713-0000000109-2759698624 Content-Type: application/sdp
Content-Length:  108
```

debug ccsip messages for a REFER message.

Displays all Session Initiation Protocol (SIP) Service Provider Interface (SPI) messages for a REFER message.

```
Received: REFER sip:2222@10.10.10.19:5060 SIP/2.0 Via: SIP/2.0/UDP 10.10.10.16:10001;branch=z9hG4bK-86781-1-11
From: UAC <sip:1111@10.10.10.16:10001>;tag=86781SIPpTag001
To: UAS <sip:2222@10.10.10.19:5060>;tag=B49877D-C8B
Call-ID: 1-86781@10.10.10.16
Max-Forwards: 70
CSeq: 3 REFER
Contact: <sip:1111@10.10.10.16:10001> Cisco-Guid: 1055557248-0520212713-0011111101-2759698624 Refer-To: <sip:3333@10.10.10.16:3004>
Referred-By: <sip:1111@10.10.10.16:10001>
Content-Length: 0
```

debug ccsip messages for a sent INVITE message towards recorder.

Displays all Session Initiation Protocol (SIP) Service Provider Interface (SPI) messages for a sent INVITE message towards
                                 recorder.

```
Sent: 
INVITE sip:9999@10.10.10.16:50001 SIP/2.0
Via: SIP/2.0/UDP 10.10.10.19:5060;branch=z9hG4bK2133D
From: <sip:10.10.10.19>;tag=32FEB-2025
To: <sip:9999@10.10.10.16>
Date: Sun, 13 Apr 2025 13:39:11 GMT
Call-ID: 84828415-17A311F0-8014C021-736E6C2E@10.10.10.19
Supported: 100rel,timer,resource-priority,replaces,sdp-anat
Require: siprec
Min-SE:  1800 Cisco-Guid: 1055557248-0520212713-00554321101-2759698666 User-Agent: Cisco-SIPGateway/IOS-17.18.20250402.101246
Allow: INVITE, OPTIONS, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY, INFO, REGISTER
CSeq: 101 INVITE
Max-Forwards: 70
Timestamp: 1744551551
Contact: <sip:10.10.10.19:5060>;+sip.src
Expires: 180
Allow-Events: telephone-event
Session-ID: 4de5ee746bea54a7a8b7f5ef9d00683d;remote=00000000000000000000000000000000
Content-Type: multipart/mixed;boundary=uniqueBoundary
Mime-Version: 1.0
Content-Length: 2399
```

## Configuration Examples for Third-Party Header Capture for Correlation between Calls and SIP-based Recording

The third-party header name can be configured to any desired header that needs to be forwarded to the SIP recorder for call
                                          correlation.

```
! Create a copylist 
Device(config)# voice class sip-copylist 100 Device(config-class)# sip-header Cisco-GUID Device(config-class)# exit ! Apply copylist to inbound dial peer so that headers specified in copylist are copied
Device(config)# dial­peer voice 2 voip Device(config-dial-peer)# voice class sip-copylist 100 Device(config-dial-peer)# exit ! SIP profile copies incoming third-party header to a variable from a peer header.  This variable 
! is then used to modify outgoing headers
Device(config)# voice class sip-profiles 10 Device(config-class)# rule 1 request INVITE peer-header sip Cisco-GUID copy "(.*)" u01 Device(config-class)# rule 2 request INVITE sip-header Unsupported add "Unsupported: Dummy Header" Device(config-class)# rule 3 request INVITE sip-header Unsupported modify ".*" "Cisco-GUID: \u01" Device(config-class)# rule 4 request REINVITE peer-header sip Cisco-GUID copy "(.*)" u03 Device(config-class)# rule 5 request REINVITE sip-header Unsupported add "Unsupported: Dummy Header" Device(config-class)# rule 6 request REINVITE sip-header Unsupported modify ".*" "Cisco-GUID: \u03" Device(config-class)# exit ! Apply SIP profile to outbound recorder dial peer
Device(config)# dial-peer voice 3 voip Device(config-dial-peer)# voice-class sip profiles 10 Device(config-dial-peer)# exit
```

| Feature Name | Releases | Feature Information |
|---|---|---|
| Third-Party GUID capture for correlation between call transfers and SIP-based recording | Cisco IOS XE 17.18.1a | The Third-Party GUID capture for correlation between calls and SIP-based recording feature is extended to support transmission
                                          of globally unique identifiers (GUIDs) to the recording server when received from a third-party private branch exchange (PBX)
                                          during call transfers. |
| Third-Party GUID Capture for Correlation Between Calls and SIP-based Recording | Baseline Functionality | The Third-Party GUID capture for correlation between calls and SIP-based recording feature provides support for the transmission
                                          of globally unique identifiers (GUIDs) received from a third-party private branch exchange (PBX) to the recording server via
                                          an established SIP session, making CUBE recording more interoperable with third-party vendors. |

| Note | In cases where the same headers are received in multiple messages, the headers are forwarded from only one of those messages,
                                          following this order of priority: REFER INVITE or mid-call INVITE request 200 OK response of INVITE or mid-call INVITE |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | voice class sip-copylist tag Example: Device(config)# voice class sip-copylist 100 | Configures a list of entities to be sent to a peer call leg and enters voice class configuration mode. |
| Step 4 | sip-header ThirdParty-headername Example: Device(config-class)# sip-header Cisco-GUID | Specifies that the third-party GUID header must be copied from the inbound dial-peer leg to the outbound dial-peer call leg. Note The third-party header name can be configured to any desired header that needs to be forwarded to the SIP recorder for call
                                                      correlation. | Note | The third-party header name can be configured to any desired header that needs to be forwarded to the SIP recorder for call
                                                      correlation. |
| Note | The third-party header name can be configured to any desired header that needs to be forwarded to the SIP recorder for call
                                                      correlation. |
| Step 5 | exit Example: Device(config-class)# exit | Exits voice class configuration mode. |
| Step 6 | dial-peer voice inbound-dial-peer-tag voip Example: Device(config)# dial-peer voice 2 voip | Enters inbound dial-peer configuration mode. |
| Step 7 | voice class sip-copylist tag Example: Device(config-dial-peer)# voice class sip-copylist 100 | Applies the copy list to the dial-peer. |
| Step 8 | exit Example: Device(config-dial-peer)# exit | Exits to global configuration mode. |
| Step 9 | voice class sip-profiles profile-id Example: Device(config)# voice class sip-profiles 10 | Creates a SIP profile and enters voice class configuration mode. |
| Step 10 | rule tag request INVITE peer-header sip header-to-copy copy header-value-to-match copy-variable Example: Device(config-class)# rule 1 request INVITE peer-header sip Cisco-GUID copy "(.*)" u01 | Copies headers from the INVITE message of the incoming dial-peer into a copy variable. |
| Step 11 | rule tag request INVITE sip-header header-to-add add header-value-to-add Example: Device(config-class)# rule 2 request INVITE sip-header Unsupported add "Unsupported: Dummy Header" | Adds a SIP header to a SIP request. Note The sip-header: "Unsupported: Dummy Header" is modified to the actual header in the next step. | Note | The sip-header: "Unsupported: Dummy Header" is modified to the actual header in the next step. |
| Note | The sip-header: "Unsupported: Dummy Header" is modified to the actual header in the next step. |
| Step 12 | rule tag request INVITE sip-header header-to-modify modify header-value-to-match header-value-to-replace Example: Device(config-class)# rule 3 request INVITE sip-header Unsupported modify ".*" "Cisco-GUID: \u01" | Modifies the outgoing header using the copy variable defined in the previous step. |
| Step 13 | rule tag request REINVITE peer-header sip header-to-copy copy header-value-to-match copy-variable Example: Device(config-class)# rule 4 request REINVITE peer-header sip Cisco-GUID copy "(.*)" u03 | Copies headers from the mid call INVITE message of the incoming dial-peer into a copy variable. |
| Step 14 | rule tag request REINVITE sip-header header-to-add add header-value-to-add Example: Device(config-class)# rule 5 request REINVITE sip-header Unsupported add "Unsupported: Dummy Header" | Adds a SIP header to a SIP request. |
| Step 15 | rule tag request REINVITE sip-header header-to-modify modify header-value-to-match header-value-to-replace Example: Device(config-class)# rule 6 request REINVITE sip-header Unsupported modify ".*" "Cisco-GUID: \u03" | Modifies the outgoing header using the copy variable defined in the previous step. |
| Step 16 | exit Example: Device(config-class)# exit | Exits to global configuration mode. |
| Step 17 | dial-peer voice recorder-dial-peer-tag voip Example: Device(config)# dial-peer voice 3 voip | Enters the dial peer configuration mode for the specified outbound recorder dial-peer. |
| Step 18 | voice-class sip profiles profile-tag Example: Device(config-dial-peer)# voice-class sip profiles 10 | Applies the SIP profile to the recording dial-peer. |
| Step 19 | end Example: Device(config-dial-peer)# end | Exits to privileged EXEC mode. |

| Note | The third-party header name can be configured to any desired header that needs to be forwarded to the SIP recorder for call
                                                      correlation. |
|---|---|

| Note | The sip-header: "Unsupported: Dummy Header" is modified to the actual header in the next step. |
|---|---|

| Note | The third-party header name can be configured to any desired header that needs to be forwarded to the SIP recorder for call
                                          correlation. |
|---|---|