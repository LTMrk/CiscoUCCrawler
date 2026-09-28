---
doc_id: developer-cisco-com-docs-ios-xe-voip-global-sip-configurations-853c2a11de
source_url: https://developer.cisco.com/docs/ios-xe-voip/global-sip-configurations/
retrieved_at: 2026-08-25T21:02:20.057381+00:00
---

# Global SIP Configurations

You can perform the global SIP configuration, using the voice-service-voip configuration mode. The voice-service-voip mode is a part of Cisco-IOS-XE-voice module. The following operations are allowed in the voice-service-voip mode.

## Prerequisites for voice-service-voip configuration

The type field is the KEY for voice-service-voip configuration. This is a mandatory field to configure other SIP services at global level.

## Select VoIP Service Configuration Mode

To enter into the voice-service-voip configuration mode, follow the x-path provided in the below table.

## Newly Added YANG Models in Release 17.14.1a

YANG models was added for the following CLI:

Voice Service VoIP Configurations:

- nat media-keepalive interval

Voice Class TLS Cipher Configurations:

- cipher cipher-list

Voice Class Tenant Configurations:

- nat media-keepalive interval

## Newly Added YANG Models in Release 17.10.1a

The following YANG models are supported from Cisco IOS XE 17.10.1a:

Voice Class Codec Configurations:

- preference  codec-type g729br8

- preference  codec-type gsmamr-nb

- video codec codec-type h261

- video codec codec-type mpeg4

Voice Class Tenant Configurations:

- disable-early-media

- conn-reuse

- error-code-override

- g729-annexb

- host-registrar

- random-contact

- max-forwards

- handle-replaces

- nat

- notify

- permit hostname

- reason-header

- retry

- srtp negotiate

- xfer target

- timers

Stun Configurations:

- stun flowdata shared-secret

## Newly Added YANG Models in Release Cisco IOS XE 17.8.1a

YANG models were added for the following CLIs:

- tls-profile

- listen-port secure

- listen-port non-secure

## Newly Added YANG Models in Release Cisco IOS XE 17.7.1

The following YANG models are supported from Cisco IOS XE 17.7.1:

- media-address range

- media bulk-stats

- media disable-detailed-stats

- media statistics

- midcal-signalling

- min-se

- conn:reuse

- remote-party-id

- rtpc all-passthru

- rtcp keepalive

- rtp-port range

- supplementary-service media-renegotiate

- localhost

- outbound proxy

- audio forced

- address hiding

- asserted id

- asymmetric payload

- block

- call-route

- call monitor

- call-threshold

- call spike

- call treatment

- codec profile

- contact-passing

- connection reuse

- dtmf-interworking

- gcid

- g729 annexb-override

- http client

- notify

- referto-passing

- rtp-ssrc multiplex

- rtp-medialoop count

- session refresh

- bind

- pass-thru content custom-sdp

- sip-profile

- copy-list

- anat

- options-ping

- early-media update block

- error-code-override

- emergency

- rtp-port range

- authentication

- credentials (SIP UA)

- connection-reuse

- clid

- cpa

- early-offer forced

- header-passing

- host registrar

- error-passthru

- session transport

- set pstn cause

- set sip status

- set sip request

- silent discard

- sip-server

- srtp

- stun usage

- privacy

- privacy-policy

- rel1xx

- url

- untrusted

- requri-passing

- update-callerid

- redirection

- redirect

- registrar

- retry

- codec

- video

- voice class stun-usage

- voice cause-code

- voice iec syslog

- voice class srtp-crypto

- voice statistics iec

- voice class codec

- voice class uri sip preference

- voice class e164-pattern-map

- voice class media

- voice class dpg

- voice class sip-hdr-passthrulist

- voice class sip-event-list

- voice class sip-profiles

- voice class sip-copylist

## Basic SIP Configurations

The voice-service-voip configuration mode allows you to perform the following SIP configurations at global level.

### Basic SIP Configurations and X-path details

## IP Address Trusted List Configuration

Configuring a Trusted IP Address List for Toll-Fraud Prevention.

## SIP Configurations

Configuring Session Initiation Protocol (SIP) registrar and other related values.

### Voice Translation Rule Configurations

### Voice Class Media Configurations

### Voice Class Sip-Event-list Configurations

### Voice Class Tenant Configurations

### Voice Class SIP Headers Passthrough Configurations

### Voice Class Server Group Configurations

### Voice Class Uri Configurations

### Voice Class E164 Pattern Map Configurations

### Voice Class Sip Options Keepalive

### Voice Class Custom-cptone Configurations

### Voice Class TLS Cipher Configurations

You can perform the TLS cipher configurations required for a TLS session, using the ios-voice:tls-cipher configuration mode under ios-voice:class configuration mode. The ios-voice:tls-cipher configuration mode is a part of Cisco-IOS-XE-voice module. The following operations are allowed in the ios-voice:class:tls-cipher configuration mode.

#### Select Voice Class TLS Cipher Configuration Mode

To enter into the ios-voice:tls-cipher configuration mode, follow the X-path provided in the following table.

#### Updated YANG Models in Release 17.14.1a

YANG models were updated for the following CLIs:

- cipher cipher-list

#### Configuration Recommendation

The tls-cipher id field is the KEY for ios-voice:tls-cipher configuration. This is a mandatory field that is required to associate TLS cipher with TLS profile configurations.

#### Voice TLS Cipher Configurations and X-path Details

#### Examples: Voice Class TLS Cipher Configurations

Example for edit-config operation:

Request

Code Snippet

```
< nc: rpc xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " message-id = " urn:uuid:7bfbbf38-ea5f-42ee-a7f6-7a1e1e29c222 " > < nc: edit-config > < nc: target > < nc: running /> </ nc: target > < nc: config > < native xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-native " > < voice xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-voice " > < class > < tls-cipher nc: operation = " create " > < id > 10 </ id > < cipher > < preference > 1 </ preference > < type > DHE_RSA_AES128_GCM_SHA256 </ type > </ cipher > </ tls-cipher > </ class > </ voice > </ native > </ nc: config > </ nc: edit-config > </ nc: rpc >
```

Response

Code Snippet

```
< rpc-reply xmlns = " urn:ietf:params:xml:ns:netconf:base:1.0 " xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " message-id = " urn:uuid:7bfbbf38-ea5f-42ee-a7f6-7a1e1e29c222 " > < ok /> </ rpc-reply >
```

### Voice Class TLS Profile Configurations

You can perform the TLS profile configurations required for a TLS session, using the ios-voice:tls-profile configuration mode under ios-voice:class configuration mode. The ios-voice:tls-profile configuration mode is a part of Cisco-IOS-XE-voice module. The following operations are allowed in the ios-voice:class:tls-profile configuration mode.

#### Select Voice Class TLS Profile Configuration Mode

To enter into the ios-voice:tls-profile configuration mode, follow the x-path provided in the following table.

#### Newly Added YANG Models in Release 17.10.1

YANG models were added for the following CLIs:

- cipher cipher-list

#### Newly Added YANG Models in Release 17.8.1

YANG models were added for the following CLIs:

Voice Class Tenant Configurations

- tls-profile

- listen-port secure

- listen-port non-secure

voice class tls-profile

- cn-san validate client

- cn-san validate bodirectional

- cn-san tag

#### Configuration Recommendation

The tls-profile id field is the KEY for ios-voice:tls-profile configuration. This is a mandatory field that is required to associate TLS profile configurations.

The ios-voice:tls-profile configuration mode allows you to perform the following configurations:

#### Voice TLS Profile Configurations and X-path details

#### Examples: Voice Class TLS Profile Configurations

Following are the examples for TLS Profile Configurations.

Example for edit-config operation:

Request

Code Snippet

```
Sending:

# 637 < nc: rpc xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " message-id = " urn:uuid:18cb23f3-d75e-4050-a4e0-4913bc2a4495 " > < nc: edit-config > < nc: target > < nc: running /> </ nc: target > < nc: config > < native xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-native " > < voice xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-voice " > < class > < tls-profile > < id > 12 </ id > < description > cisco </ description > < trustpoint > cisco </ trustpoint > < client-vtp > cisco </ client-vtp > < cn-san > < validate > < server /> </ validate > </ cn-san > < cipher > < strict-cipher /> </ cipher > < sni > < send /> </ sni > </ tls-profile > </ class > </ voice > </ native > </ nc: config > </ nc: edit-config > </ nc: rpc > ##
```

Response

Code Snippet

```
Received: < rpc-reply xmlns = " urn:ietf:params:xml:ns:netconf:base:1.0 " xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " message-id = " urn:uuid:18cb23f3-d75e-4050-a4e0-4913bc2a4495 " > < ok /> </ rpc-reply >
```

Example for get-config operation:

Request

Code Snippet

```
Sending:

# 445 < nc: rpc xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " message-id = " urn:uuid:7256ded2-4dec-40d6-a7b2-334d4fd902e5 " > < nc: get-config > < nc: source > < nc: running /> </ nc: source > < nc: filter > < native xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-native " > < voice xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-voice " > < class > < tls-profile > < id > 12 </ id > </ tls-profile > </ class > </ voice > </ native > </ nc: filter > </ nc: get-config > </ nc: rpc > ##
```

Response

Code Snippet

Code Snippet - 1

```
< rpc-reply xmlns = " urn:ietf:params:xml:ns:netconf:base:1.0 " xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " message-id = " urn:uuid:7256ded2-4dec-40d6-a7b2-334d4fd902e5 " > < data > < native xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-native " > < voice xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-voice " > < class > < tls-profile > < id > 12 </ id > < description > cisco </ description > < trustpoint > cisco </ trustpoint > < client-vtp > cisco </ client-vtp > < cn-san > < validate > < server /> </ validate > </ cn-san > < cipher > < ecdsa-cipher > < curve-size > 384 </ curve-size > </ ecdsa-cipher > </ cipher > < sni > < send /> </ sni > </ tls-profile > </ class > </ voice > </ native > </ data > </ rpc-reply >
```

```
### Voice Class Codec Configurations ###
```

### Voice Class SIP Profiles Configurations

### Voice Class Dualtone Detect Parameters Configurations

### Voice Class Codec Configurations

### Voice Class SIP Copylist Configurations

### Voice Class Dial-Peer Group Configurations

### Voice Class Stun Usage Configurations

### Voice Class srtp-crypto Configurations

### Voice Statistics Configuration

You can configure voice statistics.

### 'stun' Configuration

The voice-service-voip configuration mode allows you to configure stun parameters, which will help you to configure firewall traversal parameters for VoIP communications.

You can perform the following stun flowdata configurations.

## 'clid' Configuration

The voice-service-voip configuration mode allows you to configure clid parameters. The clid configuration allows you to pass the network-provided ISDN numbers in an ISDN calling party information element screening indicator field, and remove the calling party name and number from the calling-line identifier in voice service voip configuration mode, or allow a presentation of the calling number by substituting for the missing Display Name field in the Remote-Party-ID and From headers.

You can perform the following clid configurations.

## mode border-element license periodicity Configuration

The ios-voice:mode mode allows you to configure license periodicity for the Cisco Unified Border Element (CUBE).

### License Periodicity Configuration

You can perform the following license periodicity configurations for the Cisco Unified Border Element (UBE).

## Examples: Global SIP Configurations

Following are the examples for 'allow-connections' configuration under Global SIP Configuration.

Example for get-config operation:

Request

Code Snippet

```
Sending: < nc: rpc xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " message-id = " urn:uuid:dba4732b-8e8b-432e-8ac0-b04af2d566e4 " > < nc: get-config > < nc: source > < nc: running /> </ nc: source > < nc: filter > < native xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-native " > < voice xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-voice " > < service > < type > voip </ type > < media-recording /> < allow-connections /> < media /> < supplementary-service /> < sip > < call /> < g729 /> </ sip > < fax /> </ service > </ voice > </ native > </ nc: filter > </ nc: get-config > </ nc: rpc > ##
```

Response

Code Snippet

```
Received: < rpc-reply xmlns = " urn:ietf:params:xml:ns:netconf:base:1.0 " xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " message-id = " urn:uuid:dba4732b-8e8b-432e-8ac0-b04af2d566e4 " > < data > < native xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-native " > < voice xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-voice " > < service > < type xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " > voip </ type > < allow-connections > < sip > < to > < sip /> </ to > </ sip > </ allow-connections > < media > < bulk-stats /> </ media > < supplementary-service > < sip > < handle-replaces /> < moved-temporarily /> < refer /> </ sip > </ supplementary-service > < sip > < g729 > < annexb-all /> </ g729 > </ sip > </ service > </ voice > </ native > </ data > </ rpc-reply >
```

Example for edit-config operation:

Request

Code Snippet

```
Sending: < nc: rpc xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " message-id = " urn:uuid:11de8ac8-5685-483c-8e6d-6d218cea8877 " > < nc: edit-config > < nc: target > < nc: running /> </ nc: target > < nc: config > < native xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-native " > < voice xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-voice " > < service > < type > voip </ type > < supplementary-service > < sip nc: operation = " delete " > < handle-replaces nc: operation = " delete " /> < moved-temporarily nc: operation = " delete " /> < refer nc: operation = " delete " /> </ sip > </ supplementary-service > < sip > < g729 nc: operation = " delete " > < annexb-all nc: operation = " delete " /> </ g729 > </ sip > </ service > </ voice > </ native > </ nc: config > </ nc: edit-config > </ nc: rpc >
```

Response

Code Snippet

```
Received: < rpc-reply xmlns = " urn:ietf:params:xml:ns:netconf:base:1.0 " xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " message-id = " urn:uuid:11de8ac8-5685-483c-8e6d-6d218cea8877 " > < ok /> </ rpc-reply >
```

Next

| Operations | X-path |
|---|---|
| get, get-config, edit-config | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"] |

| Object | X-path |
|---|---|
| voice-service-voip | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"] |

| Object | X-path |
|---|---|
| voice-service-voip | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"] |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| allow-connections (SIP to SIP) | To enable IP interworking under Global Configuration mode. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:allow-connections/ios-voice:sip/ios-voice:to/ios-voice:sip | N/A | N/A | This configuration is mandatory to configure other services. |
| cpa | To enable call progress analysis (CPA) algorithm for outbound VoIP calls and to set CPA parameters. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:cpa | N/A | N/A | N/A |
| cpa threshold | To set the CPA threshold in decibels (dB). | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:cpa-config/ios-voice:cpa/ios-voice:threshold | N/A | N/A | N/A |
| cpa threshold (active-signal) | To set the active signal threshold that is related to the measured noise floor level. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:cpa-config/ios-voice:cpa/ios-voice:threshold/ios-voice:active-signal | N/A | N/A | Default: 15db |
| cpa threshold (noise-level) | To set the CPA noise floor level limits. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:cpa-config/ios-voice:cpa/ios-voice:threshold/ios-voice:noise-level | Max: -45dBm0, -50dBm0, -55dBm0, -60dBm0, Min: -55dBm0, -60dBm0, -65dBm0, -70dBm0 | N/A | Max Default: -50dBm0 Min Default: -60dBm0 |
| cpa threshold (term-tone) | To set the answering machine terminating tone thresholds. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:cpa-config/ios-voice:cpa/ios-voice:threshold/ios-voice:term-tone | min-duration in	miliseconds (80-2000), min-freq in hertz (300-2000) | N/A | min-duration Default: 80 min-freq Default: 300 |
| cpa timing | To configure cpa timing parameters. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:cpa-config/ios-voice:cpa/ios-voice:timing | N/A | N/A | N/A |
| cpa timing (live-person) | To configure the maximum waiting time (in milliseconds) that the CPA algorithm uses to determine if the call is answered by a living person. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:cpa-config/ios-voice:cpa/ios-voice:timing/ios-voice:live-person | Min-1, Max-60000 | N/A | Default: 2500 miliseconds |
| cpa timing (noise-period) | To configure the maximum waiting time (in milliseconds) that the CPA algorithm uses to measure the noise floor level at the beginning of the call. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:cpa-config/ios-voice:cpa/ios-voice:timing/ios-voice:noise-period | Min-1, Max-60000 | N/A | Default: 100 miliseconds |
| cpa timing (silent) | To configure the minimum silent duration (in milliseconds) afer active speech is detected for the CPA algorithm to declare that the call is answered by a live human. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:cpa-config/ios-voice:cpa/ios-voice:timing/ios-voice:silent | Min-1, Max-60000 | N/A | Default: 375 miliseconds |
| cpa timing (term-tone) | To configure the maximum waiting time (in milliseconds) that the CPA algorithm uses to wait for the answering machine termination tone after the answering machine is detected. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:cpa-config/ios-voice:cpa/ios-voice:timing/ios-voice:term-tone | Min-1, Max-60000 | N/A | Default: 15000 miliseconds |
| cpa timing (timeout) | To configure the maximum waiting time (in milliseconds) that the CPA algorithm uses to timeout if it does not detect any voice signal. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:cpa-config/ios-voice:cpa/ios-voice:timing/ios-voice:term-tone | Min-1, Max-60000 | N/A | Default: 3000 miliseconds |
| cpa timing (valid-speech) | To configure the minimum voice duration (in milliseconds) for the CPA algorithm to consider it as a valid speech signal. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:cpa-config/ios-voice:cpa/ios-voice:timing/ios-voice:valid-speech | Min-1, Max-60000 | N/A | Default: 112 miliseconds |
| callmonitor | To configure call monitoring messaging functionality on a SIP endpoint in a VoIP network. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:callmonitor | N/A | N/A | N/A |
| media bulk-stats | To enable a periodic process to retrieve bulk call statistics. | /native/ios-voice:voice/ios-voice:service/ios-voice:media/ios-voice:bulk-stats | N/A | N/A | N/A |
| media statistics | To enable media statistics. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:media/ios-voice:statistics | N/A | N/A | N/A |
| media disable-detailed-stats | To disable detailed statistics collection about the calls present. | /native/ios-voice:voice/ios-voice:service/ios-voice:media/ios-voice:disable-detailed-stats | N/A | N/A | N/A |
| media-recording (licenses) (min)-(max) | To allocate media recording licenses. | /native/ios-voice:voice/ios-voice:service/ios-voice:media-recording/ios-voice:licenses | 1 to 500 | N/A | N/A |
| memory-limit | To configure the memory limit for VoIP trace information. | /native/ios-voice:voice/ios-voice:service/ios-voice:trace/ios-voice:memory-limit | Min-10, Max-1000 | N/A | Default: Platform (10% of available platform memory is configured as memory limit.) |
| media-address range | To configure Voice Media IP Address Range. | /native/ios-voice:voice/ios-voice:service/ios-voice:media-address/ios-voice:range | N/A | N/A | N/A |
| media-address range ipv4 start-ipv4-address | To configure starting IP address in the range. | /native/ios-voice:voice/ios-voice:service/ios-voice:media-address/ios-voice:range/ios-voice:ipv4/ios-voice:start-ipv4-address | The value should be a valid IPv4 address. | N/A | N/A |
| media-address range ipv4 end-ipv4-address | To configure ending IP address in the range. | /native/ios-voice:voice/ios-voice:service/ios-voice:media-address/ios-voice:range/ios-voice:ipv4/ios-voice:end-ipv4-address | The value should be a valid IPv4 address. | N/A | N/A |
| media-address range ipv4 port-range min-port | To configure minimum port number. | /native/ios-voice:voice/ios-voice:service/ios-voice:media-address/ios-voice:range/ios-voice:ipv4/ios-voice:port-range/ios-voice:min-port | Min 8000, Max 48198 | N/A | N/A |
| media-address range ipv4 port-range max-port | To configure maximum port number. | /native/ios-voice:voice/ios-voice:service/ios-voice:media-address/ios-voice:range/ios-voice:ipv4/ios-voice:port-range/ios-voice:max-port | Min 8000, Max 48198 | N/A | N/A |
| media-address range ipv4 port-range-extended port-range port min-port | To start media address extended port. | /native/ios-voice:voice/ios-voice:service/ios-voice:media-address/ios-voice:voice-vrf/ios-voice:port-range-extended/ios-voice:port-range/ios-voice:port/ios-voice:min-port | Min 5500, Max 65498 | N/A | N/A |
| media-address range ipv4 port-range-extended port-range port max-port | To stop media address extended port. | /native/ios-voice:voice/ios-voice:service/ios-voice:media-address/ios-voice:voice-vrf/ios-voice:port-range-extended/ios-voice:port-range/ios-voice:port/ios-voice:max-port | Min 5500, Max 65498 | N/A | N/A |
| media-address range ipv6 start-ipv6-address | To configure starting IP address in the range. | /native/ios-voice:voice/ios-voice:service/ios-voice:media-address/ios-voice:range/ios-voice:ipv6/ios-voice:start-ipv6-address | The value should be a valid IPv6 address. | N/A | N/A |
| media-address range ipv6 end-ipv6-address | To configure ending IP address in the range. | /native/ios-voice:voice/ios-voice:service/ios-voice:media-address/ios-voice:range/ios-voice:ipv6/ios-voice:end-ipv6-address | The value should be a valid IPv6 address. | N/A | N/A |
| media-address range ipv6 port-range min-port | To configure minimum port number. | /native/ios-voice:voice/ios-voice:service/ios-voice:media-address/ios-voice:range/ios-voice:ipv6/ios-voice:port-range/ios-voice:min-port | Min 8000, Max 48198 | N/A | N/A |
| media-address range ipv6 port-range max-port | To configure maximum port number. | /native/ios-voice:voice/ios-voice:service/ios-voice:media-address/ios-voice:range/ios-voice:ipv6/ios-voice:port-range/ios-voice:max-port | Min 8000, Max 48198 | N/A | N/A |
| media-address range ipv6 port-range-extended port-range port min-port | To start media address extended port. | /native/ios-voice:voice/ios-voice:service/ios-voice:media-address/ios-voice:range/ios-voice:ipv6/ios-voice:port-range-extended/ios-voice:port-range/ios-voice:port/ios-voice:min-port | Min 5500, Max 65498 | N/A | N/A |
| media-address range ipv6 port-range-extended port-range port max-port | To stop media address extended port. | /native/ios-voice:voice/ios-voice:service/ios-voice:media-address/ios-voice:range/ios-voice:ipv6/ios-voice:port-range-extended/ios-voice:port-range/ios-voice:port/ios-voice:max-port | Min 5500, Max 65498 | N/A | N/A |
| media-address voice-vrf | To associate RTP port-range with VRF. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:media-address/ios-voice:voice-vrf | String | N/A | N/A |
| media-address voice-vrf port-range min-port | To configure minimm VRF port number. | /native/ios-voice:voice/ios-voice:service/ios-voice:media-address/ios-voice:voice-vrf/ios-voice:port-range/ios-voice:min-port | Min 8000, 48198 | N/A | N/A |
| media-address voice-vrf port-range max-port | To configure maximum VRF port number. | /native/ios-voice:voice/ios-voice:service/ios-voice:media-address/ios-voice:voice-vrf/ios-voice:port-range/ios-voice:max-port | Min 8000, 48198 | N/A | N/A |
| media-address voice-vrf port-range-extended port-range port min-port | To start media address extended port. | /native/ios-voice:voice/ios-voice:service/ios-voice:media-address/ios-voice:voice-vrf/ios-voice:port-range-extended/ios-voice:port-range/ios-voice:port/ios-voice:min-port | Min 5500, 65498 | N/A | N/A |
| media-address voice-vrf port-range-extended port-range port max-port | To end media address extended port. | /native/ios-voice:voice/ios-voice:service/ios-voice:media-address/ios-voice:voice-vrf/ios-voice:port-range-extended/ios-voice:port-range/ios-voice:port/ios-voice:max-port | Min 5500, 65498 | N/A | N/A |
| rtp-port range | To specify RTP port-range. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:rtp-port/ios-voice:range | Port Range: 8000-48198 | N/A | N/A |
| rtcp all-pass-through | To pass through all the RTCP packets in datapath. | native/ios-voice:voice/ios-voice:service/ios-voice:rtcp/ios-voice:all-pass-through | N/A | N/A | N/A |
| rtcp keepalive | To generate RTCP keepalive report. | /native/ios-voice:voice/ios-voice:service/ios-voice:rtcp/ios-voice:keepalive | N/A | N/A | N/A |
| supplementary-service sip | To enable SIP supplementary service capabilities for call forwarding and call transfers across a SIP network. | /native/ios-voice:voice/ios-voice:service/ios-voice:supplementary-service/ios-voice:sip | handle-replaces, moved-temporarily, refer | N/A | Default: Enabled |
| supplementary-service media media-renegotiate | To enable or disable media renegotiation. | /native/ios-voice:voice/ios-voice:service/ios-voice:supplementary-service/ios-voice:media-renegotiate | N/A | N/A | N/A |
| shutdown | To shutdown VoIP Trace Serviceability Framework for SIP calls in CUBE. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:trace/ios-voice:shutdown | true, false | N/A | N/A |
| trace | To enable VoIP Trace Servicability Framework for SIP calls in CUBE. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:trace | N/A | N/A | Default: Enabled |
| memory-limit | To configure the memory limit for VoIP trace information. | /native/ios-voice:voice/ios-voice:service/ios-voice:trace/ios-voice:memory-limit | Min-10, Max-1000 | N/A | Default: Platform (10% of available platform memory is configured as memory limit.) |
| address-hiding | To hide signaling and media peer addresses from endpoints other than the gateway. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:address-hiding | N/A | N/A | N/A |
| emergency | To configure list of emergency numbers. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:emergency | N/A | N/A | N/A |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| ip address trusted | To set up toll-fraud prevention support on a device. | /native/ios-voice:voice/ios-voice:service/ios-voice:ip/ios-voice:address/ios-voice:trusted | authenticate, call-block, list | N/A | (For the List option) To delete the Trusted IP list, ensure that all child IP addresses are deleted before deleting the parent IP. |
| ip address trusted list | To setup IP address trusted list of IPv4 and IPv6 addresses for toll fraud prevention. For IPv4, the network-mask argument allows you to define a subnet IP address. | /native/ios-voice:voice/ios-voice:service/ios-voice:ip/ios-voice:address/ios-voice:trusted/ios-voice:list | IPv4 Address, IPv6 Address | N/A | For IPv4, you need to add IPv4 Address Mask. You can add up to 100 IP addresses (IPv4 and IPv6) in the IP address trusted list. Duplicate IP addresses are not allowed. |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| local host | To specify the DNS name for the localhost. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:localhost | String | N/A | The string pattern should be of the form dns:host.domain or dns:host. |
| outbound-proxy address | To configure an outbound SIP proxy server. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:outbound-proxy/ios-voice:address | String | N/A | The string pattern should be in the form of ipv4:[0-255].[0-255].[0-255].[0-255], ipv4:[0-255].[0-255].[0-255].[0-255]:[0-65535], ipv6:[X:X:X:X::X],\n ipv6:[X:X:X:X::X]:[0-65535], or dns:host.domain |
| outbound-proxy dhcp | To provision SIP outbound proxy using DHCP. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:outbound-proxy/ios-voice:dhcp | N/A | N/A | N/A |
| audio forced | To allow only audio/fax, drop all other. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:audio/ios-voice:forced | N/A | N/A | N/A |
| block one-eighty | To block 180 response to Invite message. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:block/ios-voice:one-eighty | N/A | N/A | N/A |
| block one-eighty sdp (absent/present) | To block the 180 response if the SDP is absent or present. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:block/ios-voice:one-eighty/ios-voice:sdp | absent/present | N/A | N/A |
| block one-eighty-one | To block 181 response to Invite message. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:block/ios-voice:one-eighty-one | N/A | N/A | N/A |
| block one-eighty-one sdp (absent/present) | To block the 181 response if the SDP is absent or present. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:block/ios-voice:one-eighty-one/ios-voice:sdp | absent/present | N/A | N/A |
| block one-eighty-three | To block 183 response to Invite message. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:block/ios-voice:one-eighty-three | N/A | N/A | N/A |
| block one-eighty-three sdp (absent/present) | To block the 183 response if the SDP is absent or present. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:block/ios-voice:one-eighty-three/ios-voice:sdp | absent/present | N/A | N/A |
| call-route dest-route-string | To route call based on destination route string. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:call-route/ios-voice:dest-route-string | N/A | N/A | N/A |
| call-route history-info | To route call based on history information. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:call-route/ios-voice:history-info | N/A | N/A | N/A |
| call-route p-called-party-id | To route call based on P-Called-Party-ID. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:call-route/ios-voice:p-called-party-id | N/A | N/A | N/A |
| call-route url | To route call based on URL. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:call-route/ios-voice:url | N/A | N/A | N/A |
| contact-passing | To enable pass through of the contact header from one leg to the other leg in 302 pass-through scenario. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:contact-passing | N/A | N/A | N/A |
| referto-passing | To ensure that refer-to header is unmodified during passthrough. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:referto-passing | N/A | N/A | N/A |
| registrar server | To enable the local Session Initiation Protocol (SIP) registrar. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:registrar/ios-voice:server/ios-voice:expires | expires [max value] [min value], Max value range - 120 to 86400. Min value range - 60 to 3600 | N/A | ./min <= ./max, The value in the minimum field must be less than or equal to the value in the maximum value. |
| call service stop | To shut down SIP service. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:call/ios-voice:service/ios-voice:stop | forced | N/A | The value (forced) for this configuration is optional. |
| g729 annexb-all | To configure SIP gateway to treat the G.729br8 codec as superset of G.729r8 and G.729br8 codecs to interoperate with the CUCM. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:g729 | N/A | N/A | N/A |
| session | To configure SIP Voice Protocol session. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:session | N/A | N/A | N/A |
| session refresh | To enable SIP session timer. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:session/ios-voice:refresh | N/A | N/A | N/A |
| session transport | To configure the SIP signalling transport protocol. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:session/ios-voice:transport | udp, tcp [tls] | N/A | Transport Layer Security (TLS) is an optional value. To enable TLS, ensure that TCP protocol is selected. |
| bind (control) | To bind the source address for signaling to the IPv4 or IPv6 address of a specific interface. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:bind/ios-voice:control/ios-voice:source-interface | source-interface (interface-id) | N/A | For the source-interface-std , select the interface to configure from the interface-choice list. |
| bind (media) | To bind the source address for media to the IPv4 or IPv6 address of a specific interface. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:bind/ios-voice:media/ios-voice:source-interface | source-interface (interface-id) | N/A | For the source-interface-std , select the interface to configure from the interface-choice list. |
| passthru-content custom-sdp | To pass through custom SDP using SIP profiles. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:sip/ios-voice:pass-thru/ios-voice:content/ios-voice:custom-sdp | N/A | N/A | N/A |
| pass-thru content (non-rtp mode) | To configure pass-through sdp mode to non-rtp. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:sip/ios-voice:pass-thru/ios-voice:content/ios-voice:sdp/ios-voice:mode | N/A | N/A | N/A |
| custom-sdp | To configure pass-through custom SDP using SIP Profiles. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:sip/ios-voice:pass-thru/ios-voice:content/ios-voice:custom-sdp | N/A | N/A | N/A |
| unsupp | To configure pass-through all unsupported contents. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:sip/ios-voice:pass-thru/ios-voice:content/ios-voice:unsupp | N/A | N/A | N/A |
| sip-event-list-tag | To configure sip-event-list tag number to be linked as global. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:sip/ios-voice:pass-thru/ios-voice:subscribe-notify-events/ios-voice:sip-event-list-tag | N/A | N/A | N/A |
| all | To configure Pass-through all subscribe/notify events. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:sip/ios-voice:pass-thru/ios-voice:subscribe-notify-events/ios-voice:all | N/A | N/A | N/A |
| untrusted | To discard SIP requests from untrusted sources on an incoming SIP trunk. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:sip/ios-voice:silent-discard/ios-voice:untrusted | N/A | N/A | N/A |
| pai | To enable the P-Asserted-Identity (PAI) privacy header in incoming and outgoing SIP requests or response messages. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:sip/ios-voice:asserted-id/ios-voice:pai | N/A | N/A | N/A |
| ppi | To enable the P-Preferred-Identity (PPI) privacy header in incoming SIP requests and outgoing SIP requests or response messages. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:sip/ios-voice:asserted-id/ios-voice:ppi | N/A | N/A | N/A |
| block | To block all SIP messages during mid-call. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:sip/ios-voice:midcall-signaling/ios-voice:block | N/A | N/A | N/A |
| media-change | To pass SIP messages that involve media-change from one IP leg to another IP leg. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:sip/ios-voice:midcall-signaling/ios-voice:passthru/ios-voice:media-change | N/A | N/A | N/A |
| preserve-codec | To preserve codec negotiated during call initialization  i.e. midcall codec change denial. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:sip/ios-voice:midcall-signaling/ios-voice:preserve-codec | N/A | N/A | Default:Mid-call codec change is disabled. |
| dtmf | To specify the asymmetric payload support is dual-tone multi-frequency(DTMF) only. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:sip/ios-voice:asymmetric/ios-voice:payload/ios-voice:dtmf | N/A | N/A | N/A |
| dynamic-codecs | To specify the asymmetric payload support for dynamic codec payloads only. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:sip/ios-voice:asymmetric/ios-voice:payload/ios-voice:dynamic-codecs | N/A | N/A | N/A |
| full | To specify the asymmetric payload support for both DTMF and dynamic codec payloads. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:sip/ios-voice:asymmetric/ios-voice:payload/ios-voice:full | N/A | N/A | N/A |
| always | To enable end-to-end re-negotiation for all codecs. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"][ios-voice:type="voip"]/ios-voice:sip/ios-voice:early-offer/ios-voice:forced/ios-voice:re-negotiate/ios-voice:always | N/A | N/A | N/A |
| header-passing | To pass the SIP headers to applications. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:sip/ios-voice:header-passing | N/A | N/A | N/A |
| error-passthru | To Pass received error responses from one SIP leg transparently to another SIP leg. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"][ios-voice:type="voip"]/ios-voice:sip/ios-voice:error-passthru | N/A | N/A | N/A |
| max | To configure default registration max expires time. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"][ios-voice:type="voip"]/ios-voice:sip/ios-voice:registrar/ios-voice:server/ios-voice:expires/ios-voice:max | Min-120, Max-86400 | N/A | Default:3600 |
| min | To configure default registration min expires time. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"][ios-voice:type="voip"]/ios-voice:sip/ios-voice:registrar/ios-voice:server/ios-voice:expires/ios-voice:min | Min-60, Max-3600 | N/A | Default:60 |
| privacy privacy-type | To configure SIP UA privacy settings. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:privacy/ios-voice:privacy-type | critical, header, history, id, session, user | N/A | All privacy types can be configured at the same level. |
| privacy pstn | To use default PSTN rules for privacy. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:privacy/ios-voice:pstn | N/A | N/A | N/A |
| privacy-policy passthru | To pass through privacy values received from peer leg. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:privacy-policy/ios-voice:passthru | N/A | N/A | N/A |
| privacy-policy send-always | Privacy header is always sent. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:privacy-policy/ios-voice:send-always | N/A | N/A | N/A |
| privacy-policy strip diversion | To strip diversion header(s) received from peer leg. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:privacy-policy/ios-voice:strip/ios-voice:diversion | N/A | N/A | N/A |
| privacy-policy strip history-info | To strip history info header(s) received from peer leg. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:privacy-policy/ios-voice:strip/ios-voice:history-info | N/A | N/A | N/A |
| rel1xx (disable/require/supported) | To enable all Session Initiation Protocol (SIP) provisional responses (other than 100 Trying) to be sent reliably to the remote SIP endpoint. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:rel1xx | disable/require/supported | N/A | N/A |
| url sip | SIP URL in outgoing request uri. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:url/ios-voice:sip | N/A | N/A | N/A |
| url sips | Secure SIP (sips) URL in outgoing request uri. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:url/ios-voice:sips | N/A | N/A | N/A |
| url tel | TEL URL in outgoing request uri. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:url/ios-voice:tel | N/A | N/A | N/A |
| url tel phone-context | To append phone context to tel url. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:url/ios-voice:tel/ios-voice:phone-context | N/A | N/A | N/A |
| requri-passing | Request URI needs to be passed through. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:requri-passing | N/A | N/A | N/A |
| update-callerid | To enable sending updates for callerid. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:update-callerid | N/A | N/A | N/A |
| sip-profile id | The sip profiles tag number to be linked as global. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:sip/ios-voice:sip-profile/ios-voice:id | Min 1, Max 10000 | N/A | N/A |
| sip-profile inbound | To set this SIP profile as an inbound. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:sip/ios-voice:sip-profile/ios-voice:inbound | N/A | N/A | N/A |
| copy-list | The sip-copylist tag number. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:sip/ios-voice:copy-list | Min 1, Max 10000 | N/A | N/A |
| anat | To allow alternative network address types IPv4 and IPv6. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:anat | true, false | N/A | Default value is false. |
| options-ping | To send OPTION pings to remote end. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:options-ping | Min 60, Max 1200 | N/A | N/A |
| options-ping interval | Intervals in which OPTIONS transactions are sent. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:options-ping/ios-voice:interval | N/A | N/A | N/A |
| early-media update block | To consume SIP update requests with SDP received during an early dialog. | /ios:native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:sip/ios-voice:early-media/ios-voice:update/ios-voice:block | N/A | sip to sip allow connections should be enabled under "voice service voip". | N/A |
| early-media update block re-negotiate | To renegotiate the call if the UPDATE request contains changes in caller ID, transcoder addition or deletion, or video escalation or de-escalation. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:sip/ios-voice:early-media/ios-voice:update/ios-voice:block/ios-voice:re-negotiate | N/A | sip to sip allow connections should be enabled under "voice service voip". | N/A |
| error-code-override cac-bandwidth failure | To configure SIP error code for CAC bandwidth failures. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:sip/ios-voice:error-code-override/ios-voice:cac-bandwidth/ios-voice:failure | N/A | N/A | N/A |
| error-code-override call spike failure | To configure SIP error code for call spike failures. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:sip/ios-voice:error-code-override/ios-voice:call/ios-voice:spike/ios-voice:failure | N/A | N/A | N/A |
| error-code-override cpu failure | To configure SIP error code for CPU failures. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:sip/ios-voice:error-code-override/ios-voice:cpu/ios-voice:failure | N/A | N/A | N/A |
| error-code-override max-conn failure | To configure SIP error code for maximum number of simultaneous connection failures. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:sip/ios-voice:error-code-override/ios-voice:max-conn/ios-voice:failure | N/A | N/A | N/A |
| error-code-override mem failure | To configure SIP error code for memory failures. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:sip/ios-voice:error-code-override/ios-voice:mem/ios-voice:failure | N/A | N/A | N/A |
| error-code-override options-keepalive failure | To configure SIP error code for option-keepalive failures. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:sip/ios-voice:error-code-override/ios-voice:options-keepalive/ios-voice:failure | N/A | N/A | N/A |
| error-code-override sip-shutdown failure | To configure SIP error code for SIP shutdown failures. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:sip/ios-voice:error-code-override/ios-voice:sip-shutdown/ios-voice:failure | N/A | N/A | N/A |
| error-code-override total-calls failure | To configure SIP error code for total call failures. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:sip/ios-voice:error-code-override/ios-voice:total-calls/ios-voice:failure | N/A | N/A | N/A |
| nat-config | To configure global SIP NAT. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:nat-config | N/A | N/A | N/A |
| force-on | To configure all remote subscribers behind NAT device. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:nat-config/ios-voice:force-on | N/A | N/A | N/A |
| auto | To configure subscriber as auto detect in a remote subnet behind NAT. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:nat-config/ios-voice:auto | N/A | N/A | N/A |
| media-keepalive | To configure Media keepalive messages to peer subscribers located outside NAT. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:nat-config/ios-voice:media-keepalive | 10 | N/A | N/A |
| interval | To configure keepalive interval. | /native/ios-voice:voice/ios-voice:service/ios-voice:sip/ios-voice:nat-config/ios-voice:media-keepalive/ios-voice:interval | 1—50 | N/A | N/A |
| fax | To specify the global fax configurations | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:fax | N/A | N/A | N/A |
| fax protocol | To specify the system-wide fax protocol type. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:fax/ios-voice:protocol | cisco protocol is the default. | N/A | N/A |
| fax fallback | To specify the fax transport to use if T.38 cannot be negotiated. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:fax/ios-voice:fallback | N/A | protocol = 't38' | N/A |
| fax codec | To specify the fax pass-through codec. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:fax/ios-voice:codec | N/A | g711alaw, g711ulaw | protocol = 'pass-through' or fallback = 'pass-through' |
| fax ls-redundancy | To specify the t38 low speed redundancy. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:fax/ios-voice:ls-redundancy | Min-0, Max-5 | protocol = 't38' | N/A |
| fax hs-redundancy | To specify the t38 high speed redundancy. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:fax/ios-voice:hs-redundancy | Min-0, Max-2 | protocol = 't38' | N/A |
| fax version | To specify the t38 fax version. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:fax/ios-voice:version | Min-0, Max-3 | protocol = 't38' | N/A |
| modem | To specify global modem commands. | /native/ios-voice:voice/ios-voice:service/ios-voice:modem | N/A | N/A | N/A |
| modem passthrough | To pass modem traffic in-band. | /native/ios-voice:voice/ios-voice:service/ios-voice:modem/ios-voice:passthrough | N/A | N/A | N/A |
| modem passthrough codec | To configure codec used for modem passthrough using NSE. | /native/ios-voice:voice/ios-voice:service/ios-voice:modem/ios-voice:passthrough/ios-voice:nse/ios-voice:codec | N/A | N/A | N/A |
| modem passthrough payload-type | To specify NSE payload type. | /native/ios-voice:voice/ios-voice:service/ios-voice:modem/ios-voice:passthrough/ios-voice:nse/ios-voice:payload-type-conifg/ios-voice:payload-type | value: 98 to 117 | N/A | Default is 100 |
| modem passthrough payload-type codec | To specify codec selection for upspeed. | /native/ios-voice:voice/ios-voice:service/ios-voice:modem/ios-voice:passthrough/ios-voice:nse/ios-voice:payload-type-conifg/ios-voice:codec | N/A | N/A | N/A |
| modem relay gateway-xid | To configure exchange identification negotiation between gateways. | /native/ios-voice:voice/ios-voice:service/ios-voice:modem/ios-voice:relay/ios-voice:gateway-xid | N/A | N/A | N/A |
| modem relay nse codec | To configure Codec selection for upspeed. | /native/ios-voice:voice/ios-voice:service/ios-voice:modem/ios-voice:relay/ios-voice:nse/ios-voice:codec-gw-controller/ios-voice:codec | N/A | N/A | N/A |
| modem relay nse gw-controlled | To configure gateway-controlled media relay. | /native/ios-voice:voice/ios-voice:service/ios-voice:modem/ios-voice:relay/ios-voice:nse/ios-voice:codec-gw-controller/ios-voice:gw-controlled | N/A | N/A | N/A |
| modem relay nse payload-type | To configure payload type value. | /native/ios-voice:voice/ios-voice:service/ios-voice:modem/ios-voice:relay/ios-voice:nse/ios-voice:payload-type-config/ios-voice:payload-type | value: 98 to 117 | N/A | Default is 100 |
| modem relay nse payload-type codec | To configure payload type value. | /native/ios-voice:voice/ios-voice:service/ios-voice:modem/ios-voice:relay/ios-voice:nse/ios-voice:payload-type-config/ios-voice:codec | N/A | N/A | N/A |
| modem relay nse payload-type gw-controlled | To configure gateway-controlled media relay. | /native/ios-voice:voice/ios-voice:service/ios-voice:modem/ios-voice:relay/ios-voice:nse/ios-voice:payload-type-config/ios-voice:gw-controlled | N/A | N/A | N/A |
| modem relay sprt retries | To configure maximum retries for an SPRT packet. | /native/ios-voice:voice/ios-voice:service/ios-voice:modem/ios-voice:relay/ios-voice:sprt/ios-voice:retries | value: 6 to 30 | N/A | N/A |
| modem relay sse v150mer | To enable V 150.1 MER (Applicable only to SIP). | /native/ios-voice:voice/ios-voice:service/ios-voice:modem/ios-voice:relay/ios-voice:sse/ios-voice:v150mer | N/A | N/A | N/A |
| dtmf-interworking (rtp-nte) (standard) | To enable a delay between the dtmf-digit begin and dtmf-digit end events. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:dtmf-interworking | N/A | N/A | N/A |
| gcid | To enable Global Call ID (Gcid) for every call on an outbound leg of a VoIP dial peer for a SIP endpoint. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:gcid | N/A | N/A | N/A |
| notify redirect (ip2ip) (ip2pots) | To send redirect notification to application for handling. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:notify/ios-voice:redirect | N/A | N/A | N/A |
| redirect ip2ip | To redirect SIP phone calls to SIP phone calls globally. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:redirect/ios-voice:ip2ip | N/A | N/A | N/A |
| rtp-media-loop count | To configure the number of media loops before Real-Time Transport Protocol (RTP) voice and video media packets are dropped. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:rtp-media-loop/ios-voice:count | 6 to 21 | N/A | N/A |
| rtp-ssrc multiplex | To multiplex Real-Time Transport Control Protocol (RTCP) packets with RTP packets and to send multiple synchronization source in RTP headers (SSRCs) in a RTP session. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:rtp-ssrc/ios-voice:multiplex | N/A | N/A | N/A |
| srtp-config (fallback) (pass-thru) | To specify that Secure Real-Time Transport Protocol (SRTP) be used to enable secure calls and call fallback. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:srtp/ios-voice:srtp-config | N/A | N/A | N/A |
| srtp-config (fallback) (pass-thru) | To specify that Secure Real-Time Transport Protocol (SRTP) be used to enable secure calls and call fallback. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:srtp/ios-voice:srtp-config | N/A | N/A | N/A |
| rtp-port range port-range min-port | To specify the minimum port number in an RTP port range. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:rtp-port/ios-voice:range/ios-voice:port-range/ios-voice:min-port | Minimum value should be >=8000 | N/A | N/A |
| rtp-port range port-range max-port | To specify the maximum port number in an RTP port range. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:rtp-port/ios-voice:range/ios-voice:port-range/ios-voice:max-port | Maximum value should be <=48198 | N/A | N/A |
| rtp-port range extended min-port | To specify the minimum port number in extended media address ports. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:rtp-port/ios-voice:range/ios-voice:extended/ios-voice:min-port | Minimum value should be >=5500 | N/A | N/A |
| rtp-port range extended max-port | To specify the maximum port number in extended media address ports. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:rtp-port/ios-voice:range/ios-voice:extended/ios-voice:max-port | Maximum value <=65498 | N/A | N/A |
| stun flowdata agent-id-config agent-id | To set authorization agent ID. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:stun/ios-voice:stun/ios-voice:flowdata/ios-voice:agent-id-config/ios-voice:agent-id | Min 0, Max 255 | N/A | N/A |
| stun flowdata agent-id-config boot-count | To set boot count. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:stun/ios-voice:stun/ios-voice:flowdata/ios-voice:agent-id-config/ios-voice:boot-count | Min 0, Max 65535 | N/A | N/A |
| stun flowdata shared-secret tag string | To encrypt the password. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:stun/ios-voice:stun/ios-voice:flowdata/ios-voice:shared-secret-enc/ios-voice:password-string | 0,6,7 | N/A | 0: A tag of 0 specifies an uncrypted shared secret key; 6: Specifies an encrypted shared secret key; 7: Specifies an encrypted shared secret key. |
| stun flowdata shared-secret password password-string | To set the password string. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:stun/ios-voice:stun/ios-voice:flowdata/ios-voice:shared-secret-enc/ios-voice:password-string | String (Min Length 12, Max Length 162) | N/A | N/A |
| stun flowdata catlife-config catlife | To set how often a new CAT token is generated (default value 1270 = (21 min 10 sec)). | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:stun/ios-voice:stun/ios-voice:flowdata/ios-voice:catlife-config/ios-voice:catlife | 30, 70, 150, 310, 630, 1270, 2550 | N/A | N/A |
| stun flowdata catlife-config keepalive | To set how often keepalives are sent (default 30 sec). | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:stun/ios-voice:stun/ios-voice:flowdata/ios-voice:catlife-config/ios-voice:keepalive | 30, 70, 150, 310, 630, 1270, 2550 | N/A | N/A |
| stun flowdata  transaction-timer | To set STUN transaction timer. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:stun/ios-voice:stun/ios-voice:transaction-timer | Min 10, Max 50 | N/A | N/A |
| conn-reuse | To reuse the sip registration tcp connection for the end-point behind a firewall. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:sip/ ios- voice:connreuse | N/A | N/A | N/A |
| min-se | To change the minimum session expiration (Min-SE) header value for all calls that use the Session Initiation Protocol (SIP) session timer. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voatm"][ios-voice:type="voip"]/ios-voice:sip/ios-voice:min-se/ios-voice:min-se-tag | Min-90, Max-86400 | N/A | N/A |
| session-expires | To refresh timer interval for SIP session timer. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"][ios-voice:type="voip"]/ios-voice:sip/ios-voice:min-se/ios-voice:session-expires | N/A | N/A | Session-expires value should be greater than or equal to min-se value. |
| voice cause-code | To set the internal Q850 cause code mapping. | /native/ios-voice:voice/ios-voice:cause-code | N/A | N/A | N/A |
| voice iec syslog | To enable syslog reporting whenever an Internal Error Code (IEC) is triggered. | /native/ios-voice:voice/ios-voice:iec/ios-voice:syslog | N/A | N/A | N/A |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| voice translation-rule | To define a translation rule for voice calls. | /native/ios-voice:voice/ios-voice:translation-rule | rule 1 (actual number) (translated number) | N/A | N/A |
| voice translation-profile | To define a translation profile for voice calls. | /native/ios-voice:voice/ios-voice:translation-profile | name | N/A | N/A |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| voice class media | Numeric tag that specifies the voice class media. | /native/ios-voice:voice/ios-voice:class/ios-voice:media/ios-voice:media-tag | The range is from 1 to 10000 | N/A | N/A |
| media anti-trombone | To enable media anti-trombone for all calls. | /native/ios-voice:voice/ios-voice:class/ios-voice:media[ios-voice:media-tag="101"][ios-voice:media-tag=""]/ios-voice:media/ios-voice:anti-trombone | N/A | N/A | N/A |
| media forking | To enable media forking feature for all calls. | /native/ios-voice:voice/ios-voice:class/ios-voice:media[ios-voice:media-tag="101"][ios-voice:media-tag=""]/ios-voice:media/ios-voice:forking | N/A | N/A | N/A |
| monitor video | To enable video quality monitoring. | /native/ios-voice:voice/ios-voice:class/ios-voice:media[ios-voice:media-tag="101"][ios-voice:media-tag=""]/ios-voice:media/ios-voice:monitor-video | N/A | N/A | N/A |
| stats-disconnect | To defer BYE for last call stats at disconnect. | /native/ios-voice:voice/ios-voice:class/ios-voice:media[ios-voice:media-tag="101"][ios-voice:media-tag=""]/ios-voice:media/ios-voice:stats-disconnect | N/A | N/A | N/A |
| flow-through | The media is to flow through the gateway. | /native/ios-voice:voice/ios-voice:class/ios-voice:media[ios-voice:media-tag="101"][ios-voice:media-tag=""]/ios-voice:media/ios-voice:flow-through | N/A | N/A | Either select flow-through or flow-around, not both. |
| flow-around | The media is to flow around the gateway. | /native/ios-voice:voice/ios-voice:class/ios-voice:media[ios-voice:media-tag="101"][ios-voice:media-tag=""]/ios-voice:media/ios-voice:flow-around | N/A | N/A | Either select flow-through or flow-around, not both. |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| sip-event-list tag | To add event in the list of events to be passed thru. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-event-list[ios-voice:id="1"] | The range is from 1 to 10000 | N/A | N/A |
| event | To add the WORD name of event in the event list. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-event-list[ios-voice:id="1"]/ios-voice:event/ios-voice:event | Min -1, Max-25 | N/A | N/A |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| voice class tenant | To configure a tenant group. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant | N/A | N/A | N/A |
| via-port | To send responses to port present in Via header. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant[ios-voice:id="100"]/ios-voice:connection-reuse/ios-voice:via-port | N/A | N/A | N/A |
| always | To enable end-to-end re-negotiation for all codecs. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant[ios-voice:id="100"]/ios-voice:early-offer/ios-voice:forced/ios-voice:re-negotiate/ios-voice:always | N/A | N/A | N/A |
| header-passing | To pass the SIP headers to applications. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant[ios-voice:id="100"]/ios-voice:header-passing | N/A | N/A | N/A |
| error-passthru | To configure SIP error response pass-thru functionality. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant[ios-voice:id="100"]/ios-voice:error-passthru | N/A | N/A | N/A |
| remote-party-id | To enable remote-party-id support in SIP user agent calls. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant[ios-voice:id="100"]/ios-voice:remote-party-id | N/A | N/A | N/A |
| pai | To use privacy asserted identity. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant[ios-voice:id="100"]/ios-voice:asserted-id/ios-voice:pai | N/A | N/A | N/A |
| ppi | To use privacy preferred identity. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant[ios-voice:id="100"]/ios-voice:asserted-id/ios-voice:ppi | N/A | N/A | N/A |
| block | To block all SIP messages in midcall. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant[ios-voice:id="100"]/ios-voice:midcall-signaling/ios-voice:block | N/A | N/A | N/A |
| media-change | To passthrough only SIP messages which involve media-change. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant[ios-voice:id="100"]/ios-voice:midcall-signaling/ios-voice:passthru/ios-voice:media-change | N/A | N/A | N/A |
| preserve-codec | To preserve initial negotiated codec i.e. midcall codec change denial. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant[ios-voice:id="100"]/ios-voice:midcall-signaling/ios-voice:preserve-codec | N/A | N/A | N/A |
| dtmf | To support asymmetric for dtmf payloads only. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:asymmetric/ios-voice:payload/ios-voice:dtmf | N/A | N/A | N/A |
| dynamic-codecs | To support asymmetric for dynamic codec payloads. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:asymmetric/ios-voice:payload/ios-voice:dynamic-codecs | N/A | N/A | N/A |
| full | To support asymmetric for asymmetric and dynamic codec payloads. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:asymmetric/ios-voice:payload/ios-voice:full | N/A | N/A | N/A |
| authentication auth-with-realm username | To specify the username for authentication. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant[ios-voice:id=]/ios-voice:authentication/ios-voice:auth-with-realm/ios-voice:username | String | N/A | N/A |
| authentication auth-with-realm password encryption | To specify the password encryption type. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant[ios-voice:id=]/ios-voice:authentication/ios-voice:auth-with-realm/ios-voice:password/ios-voice:encryption | 0, 6, 7 | N/A | 0: Specifies an unencrypted password follows; 6: Specifies an encrypted password follows; 7: Specifies a hidden password follows. |
| authentication auth-with-realm password-string | To specify the password entered for authentication. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant[ios-voice:id=]/ios-voice:authentication/ios-voice:auth-with-realm/ios-voice:password/ios-voice:password-string | String | N/A | N/A |
| authentication auth-with-realm realm | To specify the realm at which the credentials are applicable. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant[ios-voice:id=]/ios-voice:authentication/ios-voice:auth-with-realm/ios-voice:realm | String | N/A | N/A |
| authentication username-password username | To specify the username for authentication. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant[ios-voice:id=]/ios-voice:authentication/ios-voice:username-password/ios-voice:username | String (MinLength 4, MaxLength 70) | N/A | N/A |
| authentication username-password password encryption | To specify the password encryption type. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:authentication/ios-voice:username-password/ios-voice:password/ios-voice:encryption | 0, 6, 7 | N/A | 0: Specifies an unencrypted password follows; 6: Specifies an encrypted password follows; 7: Specifies a hidden password follows. |
| authentication username-password password-string | To specify the password entered for authentication. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:authentication/ios-voice:username-password/ios-voice:password/ios-voice:password-string | String | N/A | N/A |
| credentials number-list number | To specify the number which is getting registered. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:credentials/ios-voice:number-list/ios-voice:number | String (MinLength 4, MaxLength 32) | N/A | N/A |
| credentials number-list username | To specify the username of the user for authentication. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:credentials/ios-voice:number-list/ios-voice:username | String (MinLength 4, MaxLength 70) | N/A | N/A |
| credentials number-list password  encryption | To specify the password encryption type. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:credentials/ios-voice:number-list/ios-voice:password/ios-voice:encryption | 0,6,7 | N/A | 0: Specifies an unencrypted password follows; 6: Specifies an encrypted password follows; 7: Specifies a hidden password follows. |
| credentials number-list password password-string | To specify the password for authentication. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:credentials/ios-voice:number-list/ios-voice:password/ios-voice:password-string | String | N/A | N/A |
| credentials number-list realm | To specify the realm at which the credentials are applicable. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:credentials/ios-voice:number-list/ios-voice:realm | String | N/A | You cannot configure same username across two different realms. |
| credentials username-list username | To specify the username of the user for authentication. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:credentials/ios-voice:username-list[ios-voice:username=""] | String (MinLength 4, Max Length 70) | N/A | N/A |
| credentials username-list password encryption | To specify the password encryption type. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:credentials/ios-voice:username-list[ios-voice:username=""]/ios-voice:password/ios-voice:encryption | 0,6,7 | N/A | 0: Specifies an unencrypted password follows; 6: Specifies an encrypted password follows; 7: Specifies a hidden password follows. |
| credentials username-list password password-string | To specify the password for authentication. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:credentials/ios-voice:username-list[ios-voice:username=""]/ios-voice:password/ios-voice:password-string | String | N/A | N/A |
| credentials username-list realm | To specify the realm at which the credentials are applicable. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:credentials/ios-voice:username-list[ios-voice:username=""]/ios-voice:realm | String | N/A | N/A |
| credentials dhcp password encryption | To specify the password encryption type. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:credentials/ios-voice:dhcp/ios-voice:password/ios-voice:encryption | 0, 6, 7 | N/A | 0: Specifies an unencrypted password follows; 6: Specifies an encrypted password follows; 7: Specifies a hidden password follows. |
| credentials dhcp password password-string | To specify the password for authentication. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:credentials/ios-voice:dhcp/ios-voice:password/ios-voice:password-string | String | N/A | N/A |
| credentials dhcp realm | To specify the realm at which the credentials are applicable. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:credentials/ios-voice:dhcp/ios-voice:realm | String | N/A | N/A |
| connection-reuse (via-port) | To use global listener port for sending requests over UDP. Sends responses to the port present in via header. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:connection-reuse/ios-voice:via-port | N/A | N/A | N/A |
| early-offer forced (renegotiate, always) | To configure a list of entities to be sent to the peer call leg. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:copy-list | 1 to 10000 | N/A | N/A |
| pass-thru content (custom SDP) | To configure the pass-through of Session Description Protocol (SDP) from in-leg to the out-leg | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:pass-thru/ios-voice:content/ios-voice:custom-sdp | N/A | N/A | N/A |
| pass-thru content (SDP mode non-rtp) | To configure pass-through sdp mode to non-rtp. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:pass-thru/ios-voice:content/ios-voice:sdp/ios-voice:mode/ios-voice:non-rtp | N/A | N/A | N/A |
| custom-sdp | To configure pass-through custom sdp mode using SIP Profiles. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:pass-thru/ios-voice:content/ios-voice:custom-sdp | N/A | N/A | N/A |
| unsupp | To configure pass-through all unsupported content. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:pass-thru/ios-voice:content/ios-voice:unsupp | N/A | N/A | N/A |
| sip-event-list-tag | To configure sip-event-list tag number to be linked as global. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:pass-thru/ios-voice:subscribe-notify-events/ios-voice:sip-event-list-tag | N/A | N/A | N/A |
| all | To configure Pass-through all subscribe/notify events. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:pass-thru/ios-voice:subscribe-notify-events/ios-voice:all | N/A | N/A | N/A |
| bind (control) | To bind the source address for Session Initiation Protocol (SIP) signaling packets. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:bind/ios-voice:control/ios-voice:source-interface | source-interface (interface id) | N/A | For the 'source-interface std', select the interface to configure from the interface choice list. |
| bind (media) | To bind the source address for Session Initiation Protocol (SIP) media packets. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:bind/ios-voice:media/ios-voice:source-interface | source-interface (interface id) | N/A | For the 'source-interface std', select the interface to configure from the interface choice list. |
| session transport (udp, tcp) | To configure a VoIP dial peer to use TCP or User Datagram Protocol (UDP) as the underlying transport layer protocol for Session Initiation Protocol (SIP) messages. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:session/ios-voice:transport | N/A | N/A | N//A |
| sip-server | To configure a network address for the Session Initiation Protocol (SIP) server interface. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:sip-server | N/A | N/A | N/A |
| srtp-crypto | To configure the voice class srtp-crypto tag. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:srtp-crypto | Min 1, Max 10000 | N/A | N/A |
| privacy privacy-type | To configure SIP UA privacy settings. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:privacy/ios-voice:privacy-type | critical, header, history, id, session, system, user | N/A | All privacy types can be configured at the same level. |
| privacy pstn | To use default Public Switched Telephone Network (PSTN) rules for privacy. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:privacy/ios-voice:pstn | N/A | N/A | N/A |
| privacy-policy passthrough | To pass through privacy values received from peer leg. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:privacy-policy/ios-voice:passthru | N/A | N/A | N/A |
| privacy-policy send-always | Privacy header is always sent. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:privacy-policy/ios-voice:send-always | N/A | N/A | N/A |
| privacy-policy strip diversion | To strip diversion headers received from peer leg. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:privacy-policy/ios-voice:strip/ios-voice:diversion | N/A | N/A | N/A |
| privacy-policy strip history-info | To strip history info headers received from peer leg. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:privacy-policy/ios-voice:strip/ios-voice:history-info | N/A | N/A | N/A |
| rel1xx (disable/require/supported) | To enable all Session Initiation Protocol (SIP) provisional responses (other than 100 Trying) to be sent reliably to the remote SIP endpoint. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:rel1xx | disable/require/supported | N/A | N/A |
| url | URL configuration for request line URL in outgoing INVITE. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:url | N/A | N/A | N/A |
| url sip | SIP URL in outgoing request uri. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:url/ios-voice:sip | N/A | N/A | N/A |
| url sips | SECURE SIP (sips) URL in outgoing request uri. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:url/ios-voice:sips | N/A | N/A | N/A |
| url tel | TEL URL in outgoing request uri. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:url/ios-voice:tel | N/A | N/A | N/A |
| url tel phone-context | To append phone context to telephone url. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:url/ios-voice:tel/ios-voice:phone-context | N/A | N/A | N/A |
| requri-passing | Request URI needs to be passed through. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:requri-passing | N/A | N/A | N/A |
| update-callerid | To enable sending updates for caller id. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:update-callerid | N/A | N/A | N/A |
| anat | To allow alternative network address types IPv4 and IPv6. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:anat | true, false | N/A | Default value is false. |
| early media update block | To consume the SIP UPDATE requests with SDP received during an early dialog. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:early-media/ios-voice:update/ios-voice:block | N/A | sip to sip allow connection should be enabled under "voice service voip". | N/A |
| early media update block re-negotiate | To renegotiate the call if the UPDATE request contains changes in caller ID, transcoder addition or deletion, or video escalation or de-escalation. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:early-media/ios-voice:update/ios-voice:block/ios-voice:re-negotiate | N/A | sip to sip allow connection should be enabled under "voice service voip". | N/A |
| localhost | To specify the DNS name for the localhost. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:localhost | String | N/A | The string pattern should be of the form dns:host.domain or dns:host. |
| outbound-proxy address | To specify an Outbound Proxy Address. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:outbound-proxy/ios-voice:address | String | N/A | The string pattern should be in the form of ipv4:[0-255].[0-255].[0-255].[0-255], ipv4:[0-255].[0-255].[0-255].[0-255]:[0-65535], ipv6:[X:X:X:X::X],\n ipv6:[X:X:X:X::X]:[0-65535], or dns:host.domain |
| outbound-proxy dhcp | To provision SIP outbound proxy using DHCP. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:outbound-proxy/ios-voice:dhcp | N/A | N/A | N/A |
| audio forced | To allow only audio/fax, drop all other. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:audio/ios-voice:forced | N/A | N/A | N/A |
| block one-eighty | To block 180 response to Invite message. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:block/ios-voice:one-eighty | N/A | N/A | N/A |
| block one-eighty sdp (absent/present) | To block the 180 response if the SDP is absent or present. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:block/ios-voice:one-eighty/ios-voice:sdp | absent/present | N/A | N/A |
| block one-eighty-one | To block 181 response to Invite message. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:block/ios-voice:one-eighty-one | N/A | N/A | N/A |
| block one-eighty-one sdp (absent/present) | To block the 181 response if the SDP is absent or present. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:block/ios-voice:one-eighty-one/ios-voice:sdp | absent/present | N/A | N/A |
| block one-eighty-three | To block 183 response to Invite message. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:block/ios-voice:one-eighty-three | N/A | N/A | N/A |
| block one-eighty-three sdp (absent/present) | To block the 183 response if the SDP is absent. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:block/ios-voice:one-eighty-three/ios-voice:sdp | absent/present | N/A | N/A |
| call-route dest-route-string | To route based on dest-route-string. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:call-route/ios-voice:dest-route-string | N/A | N/A | N/A |
| call-route history-info | To route based on history info. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:call-route/ios-voice:history-info | N/A | N/A | N/A |
| call-route p-called-party-id | To route based on P-Called-Party-ID. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:call-route/ios-voice:p-called-party-id | N/A | N/A | N/A |
| call-route url | To route based on URL. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:call-route/ios-voice:url | N/A | N/A | N/A |
| sip-profile id | The sip profiles tag number to be linked as global. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:sip-profile/ios-voice:id | Min 1, Max 10000 | N/A | N/A |
| sip-profile inbound | To set profile as an inbound SIP Profile. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:sip-profile/ios-voice:inbound | N/A | N/A | N/A |
| copy-list | The sip-copylist tag number. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:copy-list | Min 1, Max 10000 | N/A | N/A |
| redirection | To enable call redirection (3xx) handling. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:redirection | N/A | N/A | N/A |
| contact-passing | 302 contact needs to be passed through for Call Forward. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:contact-passing | N/A | N/A | N/A |
| referto-passing | Refer-To needs to be passed through for transfer. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:referto-passing | Integer (Min 1, Max 70) | N/A | N/A |
| max-forwards | To change number of max-forwards for SIP methods. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:max-forwards | Integer (Min 1, max 70) | N/A | N/A |
| xfer target | To configure where to select the xfer target from | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:xfer/ios-voice:target | dial-peer, refer-to | N/A | Default is dial-peer. |
| permit hostname | Permit hostname in Req URI for incoming INVITEs | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant[ios-voice:id=]/ios-voice:permit[ios-voice:hostname=""] | String (format should be either dns:host.domain or dns:domain) | N/A | N/A |
| index id | To specify the rule tag. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:multiple-registrars/ios-voice:index/ios-voice:id | Min 1, Max 6 | N/A | N/A |
| registrar index registrar-config | To specify the registrar server IP address. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:multiple-registrars/ios-voice:index/ios-voice:registrar-config | registrar-ip-address | N/A | N/A |
| registrar index expires | To configure default registration time in seconds. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:multiple-registrars/ios-voice:index/ios-voice:expires | Min 60, Max 65535 | N/A | Default value is 3600. |
| registrar index auth-realm | To specify	the realm for preloaded authorization. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:multiple-registrars/ios-voice:index/ios-voice:auth-realm | String | N/A | N/A |
| registrar index refresh-ratio | To specify the registration refresh ratio in percentage. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:multiple-registrars/ios-voice:index/ios-voice:refresh-ratio | Min 1, Max 100 | N/A | N/A |
| registrar index random-contact | To specify the Random String Contact header used to identify the registration session. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:multiple-registrars/ios-voice:index/ios-voice:random-contact | N/A | N/A | N/A |
| registrar index scheme | To specify the URL scheme. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:multiple-registrars/ios-voice:index/ios-voice:scheme | sip or sips | N/A | Default is sip. |
| registrar index tcp | To use TCP as Transport Layer Protocol. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:multiple-registrars/ios-voice:index/ios-voice:tcp | N/A | N/A | N/A |
| registrar index tls | To use TLS encryption over TCP Transport Layer Protocol. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:multiple-registrars/ios-voice:index/ios-voice:tls | N/A | You can configure TLS only after TCP. | N/A |
| registrar index secondary | To specify a secondary SIP registrar for redundancy if the primary registrar fails. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:multiple-registrars/ios-voice:index/ios-voice:secondary | N/A | N/A | N/A |
| registrar primary-registrar | To configure primary SIP registrar server. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:primary-registrar | N/A | The registrar configurations are mutually exclusive and one of these can exist at a time. 1. Multiple registrars configuration (Index container) 2. Primary/secondary registrars configuration (different containers, but you can configure them together - there will not be any errors) 3. Registrar DHCP. | N/A |
| registrar primary-registrar registrar-config | To specify the primary registrar server IP address. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:primary-registrar/ios-voice:registrar-config | registrar-ip-address | N/A | N/A |
| registrar primary-registrar expires | To configure default registration time in seconds. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:primary-registrar/ios-voice:expires | Min 60, Max 65535 | N/A | Default value is 3600. |
| registrar primary-registrar auth-realm | To specify the realm for preloaded authorization. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:primary-registrar/ios-voice:auth-realm | String | N/A | N/A |
| registrar primary-registrar refresh-ratio | To specify the registration refresh ratio in percentage. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:primary-registrar/ios-voice:refresh-ratio | Min 1, Max 100 | N/A | N/A |
| registrar primary-registrar random-contact | To specify the Random String Contact header used to identify the registration session. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:primary-registrar/ios-voice:random-contact | N/A | N/A | N/A |
| registrar primary-registrar scheme | To specify the URL scheme. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:primary-registrar/ios-voice:scheme | sip or sips | N/A | Default is sip. |
| registrar primary-registrar tcp | To use TCP as Transport Layer Protocol. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:primary-registrar/ios-voice:tcp | N/A | N/A | N/A |
| registrar primary-registrar tls | To use TLS encryption over TCP Transport Layer Protocol. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:primary-registrar/ios-voice:tls | N/A | TLS can be configured only after TCP is configured. | N/A |
| registrar secondary-registrar | To configure secondary SIP registrar server. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:secondary-registrar | N/A | N/A | N/A |
| registrar secondary-registrar registrar-config | To specify the secondary registrar server IP address. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:secondary-registrar/ios-voice:registrar-config | registrar-ip-address | N/A | N/A |
| registrar secondary-registrar expires | To configure default registration time in seconds for the seondary registrar server. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:secondary-registrar/ios-voice:expires | N/A | N/A | N/A |
| registrar secondary-registrar auth-realm | To specify the realm for preloaded authorization. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:secondary-registrar/ios-voice:auth-realm | N/A | N/A | N/A |
| registrar secondary-registrar refresh-ratio | To specify the registration refresh ratio in percentage. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:secondary-registrar/ios-voice:refresh-ratio | Min 1, Max 100 | N/A | N/A |
| registrar secondary-registrar random-contact | To specify the Random String Contact header used to identify the registration session. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:secondary-registrar/ios-voice:random-contact | N/A | N/A | N/A |
| registrar secondary-registrar scheme | To specify the URL scheme. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:secondary-registrar/ios-voice:scheme | sip or sips | N/A | Default is sip. |
| registrar secondary-registrar tcp | To use TCP as Transport Layer Protocol. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:secondary-registrar/ios-voice:tcp | N/A | N/A | Default is UDP. |
| registrar secondary-registrar tls | To use TLS encryption over TCP Transport Layer Protocol. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:secondary-registrar/ios-voice:tls | N/A | TLS can be configured only after TCP is configured. | N/A |
| registrar secondary-registrar secondary | To specify a secondary SIP registrar for redundancy if the primary registrar fails. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:secondary-registrar/ios-voice:secondary | N/A | N/A | N/A |
| registrar dhcp | To specify that the domain name of the registrar server is retrieved from a DHCP server. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:dhcp | N/A | N/A | N/A |
| registrar dhcp expires | To conregistrar figure default registration time in seconds. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:dhcp/ios-voice:expires | Min 60, Max 65535 | N/A | Default value is 3600. |
| registrar dhcp auth-realm | To specify the realm for preloaded authorization. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:dhcp/ios-voice:auth-realm | String | N/A | N/A |
| registrar dhcp refresh-ratio | To specify the registration refresh ratio in percentage. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:dhcp/ios-voice:refresh-ratio | Min 1, Max 100 | N/A | N/A |
| registrar dhcp random-contact | To specify the Random String Contact header used to identify the registration session. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:dhcp/ios-voice:random-contact | N/A | N/A | N/A |
| registrar dhcp scheme | To specify the URL scheme. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:dhcp/ios-voice:random-contact | sip or sips | N/A | Default is sip. |
| registrar dhcp tcp | To use TCP as Transport Layer Protocol. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:dhcp/ios-voice:tcp | N/A | N/A | N/A |
| registrar dhcp tls | To use TLS encryption over TCP Transport Layer Protocol. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:registrar/ios-voice:dhcp/ios-voice:tls | N/A | TLS can be configured only after TCP is configured. | N/A |
| tls-profile tag | To specify tls-profile tag. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant[ios-voice:id=""]/ios-voice:tls-profile | Min 1, Max 10000 | N/A | N/A |
| non-secure port | To specify non-secure port. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant[ios-voice:id=""]/ios-voice:listen-port/ios-voice:non-secure | Min 5000, Max 5500 | N/A | Configure bind under this tenant for the configuration to take effect. |
| secure port | To specify secure port. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant[ios-voice:id=""]/ios-voice:listen-port/ios-voice:secure | Min 1, Max 65535 | N/A | Configure bind under this tenant for the configuration to take effect. |
| g729 annexb override | To override default value if annexb attribute is not present. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:g729-annexb/ios-voice:override | N/A | N/A | N/A |
| reason-header override | To enable reason header to override SIP<->Q850 mappings. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:reason-header/ios-voice:override | N/A | N/A | N/A |
| srtp negotiate cisco | To allow RTP to SRTP offer. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:srtp/ios-voice:negotiate/ios-voice:cisco | N/A | N/A | N/A |
| notify ignore substate | To ignore Subscription-State header. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:notify/ios-voice:ignore/ios-voice:substate | N/A | N/A | N/A |
| notify telephone-event max-duration | To specify maximum time interval between two consecutive NOTIFYs for a single DTMF event. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:notify/ios-voice:telephone-event/ios-voice:max-duration | Integer (Min 40, Max 3000) | N/A | N/A |
| host-registrar | To use sip-ua registrar value in Diversion and Contact header for 3xx messages. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:host-registrar | N/A | N/A | N/A |
| conn-reuse | To reuse the sip registration tcp connection for the end-point behind a firewall. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:conn-reuse | N/A | N/A | N/A |
| disable-early-media | To disable early media cut through. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:disable-early-media | 180 | N/A | N/A |
| random-contact | To use random contact for outgoing calls, if available. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:random-contact | N/A | N/A | N/A |
| handle-replaces | To handle INVITE with REPLACES header at SIP spi. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:handle-replaces | N/A | N/A | N/A |
| nat | To use SIP nat global configuration | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:nat | auto, force-on | N/A | N/A |
| error-code-override cac-bandwidth failure | To configure SIP error code for CAC bandwidth failures. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant[ios-voice:id=]/ios-voice:error-code-override/ios-voice:cac-bandwidth/ios-voice:failure | Integer (Min 400, Max 699) | N/A | N/A |
| error-code-override call spike failure | To configure SIP error code for call spike failures. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:error-code-override/ios-voice:call/ios-voice:spike/ios-voice:failure | Integer (Min 400, Max 699) | N/A | N/A |
| error-code-override cpu failure | To configure SIP error code for CPU failures. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:error-code-override/ios-voice:cpu/ios-voice:failure | Integer (Min 400, Max 699) | N/A | N/A |
| error-code-override max-conn failure | To configure SIP error code for maximum number of simultaneous connection failures. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:error-code-override/ios-voice:max-conn/ios-voice:failure | Integer (Min 400, Max 699) | N/A | N/A |
| error-code-override mem failure | To configure SIP error code for memory failures. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:error-code-override/ios-voice:mem/ios-voice:failure | Integer (Min 400, Max 699) | N/A | N/A |
| error-code-override options-keepalive failure | To configure SIP error code for option-keepalive failures. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:error-code-override/ios-voice:options-keepalive/ios-voice:failure | Integer (Min 400, Max 699) | N/A | N/A |
| error-code-override sip-shutdown failure | To configure SIP error code for SIP shutdown failures. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:error-code-override/ios-voice:sip-shutdown/ios-voice:failure | Integer (Min 400, Max 699) | N/A | N/A |
| error-code-override total-calls failure | To configure SIP error code for total call failures. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:error-code-override/ios-voice:sip-shutdown/ios-voice:failure | Integer (Min 400, Max 699) | N/A | N/A |
| retry bye | To enter BYE retry value. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:retry/ios-voice:bye | Integer (Min 1, Max 10) | N/A | N/A |
| retry cancel | To enter CANCEL retry value. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:retry/ios-voice:cancel | Integer (Min 1, Max 10) | N/A | Default value is 10. |
| retry info | To enter INFO retry value. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:retry/ios-voice:info | Integer (Min 1, Max 10) | N/A | Default value is 6. |
| retry invite | To enter INVITE retry value. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:retry/ios-voice:invite | Integer (Min 1, Max 10) | N/A | Default value is 6. |
| retry notify | To enter NOTIFY retry value. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:retry/ios-voice:notify | Integer (Min 1, Max 10) | N/A | Default value is 10. |
| retry options | To enter OPTIONS retry value. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:retry/ios-voice:options | Integer (Min 1, Max 10) | N/A | Default value is 6. |
| retry prack | To enter PRACK retry value. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:retry/ios-voice:prack | Integer (Min 1, Max 10) | N/A | Default value is 10. |
| retry refer | To enter REFER retry value. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:retry/ios-voice:refer | Integer (Min 1, Max 10) | N/A | Default value is 10. |
| retry register | To enter REGISTER retry value. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:retry/ios-voice:register | Integer (Min 1, Max 10) | N/A | Default value is 6. |
| retry rel1xx | To enter reliable 1xx retry value. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:retry/ios-voice:rel1xx | Integer (Min 1, Max 10) | N/A | Default value is 6. |
| retry response | To enter response retry value. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:retry/ios-voice:response | Integer (Min 1, Max 10) | N/A | Default value is 6. |
| retry subscribe | To enter SUBSCRIBE retry value. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:retry/ios-voice:subscribe | Integer (Min 1, Max 10) | N/A | Default value is 6. |
| retry update | To enter UPDATE retry value. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:retry/ios-voice:update | Integer (Min 1, Max 10) | N/A | Default value is 6. |
| timers buffer-invite | To specify the time to buffer the INVITE while waiting for display info. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:timers/ios-voice:buffer-invite | Integer (Min 50, Max 5000) | N/A | N/A |
| timers connect | To specify wait time to confirm whether a session is connected or not. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:timers/ios-voice:connect | Integer (Min 100, Max 1000) | N/A | Default value is 500. |
| timers connection | To specify connection related timers. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:timers/ios-voice:connection | N/A | N/A | N/A |
| timers disconnect | To specify wait time to confirm whether a session is disconnected or not. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:timers/ios-voice:disconnect | Integer (Min 100, Max 1000) | N/A | Default value is 500. |
| timers dns registrar-cache timer | To specify expiry timer value in seconds for the DNS resolved address cache. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:timers/ios-voice:dns/ios-voice:registrar-cache/ios-voice:time | Integer (Min 60, Max 65535) | N/A | N/A |
| timers dns registrar-cache ttl | To specify timer value to be set off as ttl seconds. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:timers/ios-voice:dns/ios-voice:registrar-cache/ios-voice:ttl | N/A | N/A | N/A |
| timers expires | To specify the time to wait for the expiration of an INVITE request. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:timers/ios-voice:expires | Integer (Min 60000, Max 1800000) | N/A | Default value is 180000. |
| timers hold | To specify the wait time during hold before disconnecting. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:timers/ios-voice:hold | Integer (Min 15, Max 2880) | N/A | Default value is 2880. |
| timers info | To specify the wait time before INFO retransmission. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:timers/ios-voice:info | Integer (Min 100, Max 1000) | N/A | Default value is 500. |
| timers notify | To specify the time to wait before NOTIFY retransmission. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:timers/ios-voice:notify | Integer (Min 100, Max 1000) | N/A | Default value is 500. |
| timers options | To specify the wait time before OPTIONS retransmission. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:timers/ios-voice:options | Integer (Min 100, Max 1000) | N/A | Default value is 500. |
| timers prack | To specify the time to wait before PRACK retransmission. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:timers/ios-voice:prack | Integer (Min 100, Max 1000) | N/A | Default value is 500. |
| timers refer | To specify the time to wait before REFER retransmission. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:timers/ios-voice:refer | Integer (Min 100, Max 1000) | N/A | Default value is 500. |
| timers register | To specify the time to wait before REGISTER retransmission. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:timers/ios-voice:register | Integer (Min 100, Max 1000) | N/A | Default value is 500. |
| timers rel1xx | To specify the wait time before starting reliable 1xx retransmission. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:timers/ios-voice:rel1xx | Integer (Min 100, Max 1000) | N/A | Default value is 500. |
| timers trying | To specify the time to wait for provisional response to INVITE. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:timers/ios-voice:trying | Integer (Min 100, Max 1000) | N/A | Default value is 500. |
| timers update | To spcify the wait time before starting UPDATE retransmission. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:timers/ios-voice:update | Integer (Min 100, Max 1000) | N/A | Default value is 500. |
| nat-config | To configure global SIP NAT. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:nat-config | N/A | N/A | N/A |
| force-on | To configure all remote subscribers behind NAT device. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:nat-config/ios-voice:force-on | N/A | N/A | N/A |
| auto | To configure subscriber as auto detect in a remote subnet behind a NAT. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:nat-config/ios-voice:auto | N/A | N/A | N/A |
| media-keepalive | To configure Media keepalive messages to peer subscribers located outside NAT. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:nat-config/ios-voice:media-keepalive | 10 | N/A | N/A |
| interval | To configure keepalive interval. | /native/ios-voice:voice/ios-voice:class/ios-voice:tenant/ios-voice:nat-config/ios-voice:media-keepalive/ios-voice:interval | 1—50 | N/A | N/A |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| sip-hdr-passthrulist-tag | To configure Voice class sip-hdr-passthrulist tag. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-hdr-passthrulist/ios-voice:sip-hdr-passthrulist-tag | tag (Min 1, Max	10000) | N/A | N/A |
| passthru-hdr | To add header_name of header in p-thru list. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-hdr-passthrulist/ios-voice:passthru-hdr/ios-voice:passthru-hdr | tag (Min 1, Max	25) | N/A | N/A |
| passthru-hdr-unsupp | To enable the pass-thru of all unsupported headers. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-hdr-passthrulist/ios-voice:passthru-hdr-unsupp | N/A | N/A | N/A |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| voice class server group | To enter voice-class configuration mode and configure server groups (groups of IPv4 and IPv6 addresses), which can be referenced from an outbound SIP dial peer. | /native/ios-voice:voice/ios-voice:class/ios-voice:server-group | tag (Min 1, Max 10000) | N/A | Maximum five IP addresses are allowed |
| description | Description of a server group | /native/ios-voice:voice/ios-voice:class/ios-voice:server-group/ios-voice:description | Up to 80 characters describing the server | N/A | N/A |
| hunt-scheme round-robin | Defines a hunt method for the order of selection of target server IP addresses (from the IP addresses configured for this server group) for the setting up of outgoing calls. | /native/ios-voice:voice/ios-voice:class/ios-voice:server-group/ios-voice:hunt-scheme/ios-voice:round-robin | N/A | N/A | N/A |
| huntstop id | To configure the huntstop rule identifier. | /native/ios-voice:voice/ios-voice:class/ios-voice:server-group/ios-voice:huntstop/ios-voice:id | tag (Min 1, Max 10000) | N/A | N/A |
| resp-code-start-range | To specify the startvalue of the responsecode. | /native/ios-voice:voice/ios-voice:class/ios-voice:server-group/ios-voice:huntstop/ios-voice:resp-code/ios-voice:resp-code-start-range | (Min 400,Max 599) | N/A | Overlapping of SIP error response configuration is not permitted. |
| to | To configure the SIP response code range. | /native/ios-voice:voice/ios-voice:class/ios-voice:server-group/ios-voice:huntstop/ios-voice:resp-code/ios-voice:to | N/A | N/A | N/A |
| resp-code-end-range | To specify the end value of the response code. | /native/ios-voice:voice/ios-voice:class/ios-voice:server-group/ios-voice:huntstop/ios-voice:resp-code/ios-voice:resp-code-end-range | (Min 400,Max 599) | N/A | Overlapping of SIP error response configuration is not permitted. |
| IPv4 | To select an IPv4 IP address for the server group | /native/ios-voice:voice/ios-voice:class/ios-voice:server-group/ios-voice:ipv4-address/ios-voice:ipv4/ios-voice:address | The value should be a valid IPv4 address | N/A | N/A |
| IPv4-port | To specify a port of an IPv4 IP address for the server group | /native/ios-voice:voice/ios-voice:class/ios-voice:server-group/ios-voice:ipv4-address/ios-voice:ipv4-addr-port/ios-voice:ipv4/ios-voice:port | Valid port number | N/A | N/A |
| IPv4-preference | To specify preference order of server in a server group | /native/ios-voice:voice/ios-voice:class/ios-voice:server-group/ios-voice:ipv4-address/ios-voice:ipv4-addr-port/ios-voice:ipv4/ios-voice:preference | Valid preference value: Range 0-5 | N/A | Preference value is applicable for both ipv4-address and IPv4-port. |
| IPv6 | To select an IPv6 IP address for the server group | /native/ios-voice:voice/ios-voice:class/ios-voice:server-group/ios-voice:ipv6-address/ios-voice:ipv6/ios-voice:address | Valid IPv6 address | N/A | N/A |
| IPv6-port | To specify a port of an IPv6 IP address for the server group | /native/ios-voice:voice/ios-voice:class/ios-voice:server-group/ios-voice:ipv6-address/ios-voice:ipv6-addr-port/ios-voice:ipv6/ios-voice:port | Valid port number | N/A | N/A |
| IPv6-preference | To specify preference order of server in a server group | /native/ios-voice:voice/ios-voice:class/ios-voice:server-group/ios-voice:ipv6-address/ios-voice:ipv6/ios-voice:preference | Valid preference value. Range 0-5. | N/A | Preference value is applicable for both IPv6-address and Ipv6-port. |
| shutdown | To put server group into inactive state | /native/ios-voice:voice/ios-voice:class/ios-voice:server-group/ios-voice:description | N/A | N/A | N/A |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| uri tag | To configure voice URI class tag. | /native/ios-voice:voice/ios-voice:class/ios-voice:uri/ios-voice:uri[ios-voice:uritag="23"] | tag (32 alphanumeric characters) or sip | N/A | N/A |
| type | To configure voice class type for SIP or TEL. | /native/ios-voice:voice/ios-voice:class/ios-voice:uri/ios-voice:uri[ios-voice:uritag="23"]/ios-voice:type | SIP/TEL | N/A | N/A |
| host | To match a host portion of the URI. | /native/ios-voice:voice/ios-voice:class/ios-voice:uri/ios-voice:uri[ios-voice:uritag="23"][ios-voice:uritag=""][ios-voice:uritag="23"]/ios-voice:host | N/A | N/A | N/A |
| pattern | To match a call based on the entire SIP or TEL URI. | /native/ios-voice:voice/ios-voice:class/ios-voice:uri/ios-voice:uri[ios-voice:uritag="23"][ios-voice:uritag=""][ios-voice:uritag="23"]/ios-voice:pattern | N/A | N/A | N/A |
| user-id | To match a call based on the user-id field in the SIP URI. | /native/ios-voice:voice/ios-voice:class/ios-voice:uri/ios-voice:uri[ios-voice:uritag="23"][ios-voice:uritag=""][ios-voice:uritag="23"]/ios-voice:user-id | N/A | N/A | N/A |
| context | To match the phone-context attribute of the URI. | /native/ios-voice:voice/ios-voice:class/ios-voice:uri/ios-voice:uri[ios-voice:uritag="23"][ios-voice:uritag=""][ios-voice:uritag="23"]/ios-voice:phone/ios-voice:context | N/A | N/A | N/A |
| phone | To match the phone-number attribute of the URI. | /native/ios-voice:voice/ios-voice:class/ios-voice:uri/ios-voice:uri[ios-voice:uritag="23"][ios-voice:uritag=""][ios-voice:uritag="23"]/ios-voice:phone/ios-voice:number | N/A | N/A | N/A |
| sip | To match the phone number portion of the URI. | /native/ios-voice:voice/ios-voice:class/ios-voice:uri/ios-voice:sip | N/A | N/A | N/A |
| preference-choice | To set the preference for selecting a voice class for Session Initiation Protocol (SIP) uniform resource identifiers(URIs). | /native/ios-voice:voice/ios-voice:class/ios-voice:uri/ios-voice:sip/ios-voice:preference | User-id or host | N/A | N/A |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| id | To assign a number to a voice class E.164 pattern map. | /native/ios-voice:voice/ios-voice:class/ios-voice:e164-pattern-map[ios-voice:id="1"] | min-1, max-10000 | N/A | N/A |
| description | To describe the e164 pattern specific map. | /native/ios-voice:voice/ios-voice:class/ios-voice:e164-pattern-map[ios-voice:id="1"]/ios-voice:description | N/A | N/A | N/A |
| e164-tag | To add an E164 into the map. | /native/ios-voice:voice/ios-voice:class/ios-voice:e164-pattern-map[ios-voice:id="1"]/ios-voice:e164/ios-voice:e164-tag | N/A | N/A | N/A |
| url | To set the URL of the file for the map. | /native/ios-voice:voice/ios-voice:class/ios-voice:e164-pattern-map[ios-voice:id="1"]/ios-voice:url | N/A | N/A | Ensure that the given URL file name path must exist in the router. |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| id | To monitor connectivity between Cisco Unified Border Element VoIP dial peers and SIP servers | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-options-keepalive | tag (Min 1, Max 10000) | N/A | N/A |
| description | Description of OPTIONS keepalive profile. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-options-keepalive/ios-voice:description | N/A | N/A | N/A |
| shutdown | To put sip-options keepalive to inactive state | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-options-keepalive/ios-voice:shutdown | N/A | N/A | N/A |
| up-interval | Number of up-interval seconds allowed to pass before marking the UA as unavailable. | native/ios-voice:voice/ios-voice:class/ios-voice:sip-options-keepalive/ios-voice:up-interval | 5 to 1200 | N/A | N/A |
| down-interval | Number of down-interval seconds allowed to pass before marking the UA as unavailable. | native/ios-voice:voice/ios-voice:class/ios-voice:sip-options-keepalive/ios-voice:down-interval | 5 to 1200 | N/A | N/A |
| retry | Retry count for OPTIONS keepalive retransmission. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-options-keepalive/ios-voice:retry | min-1, max-10 | N/A | N/A |
| transport (udp/tcp/tcp tls) | To set up transport layer protocol | native/ios-voice:voice/ios-voice:class/ios-voice:sip-options-keepalive/ios-voice:transport | udp/tcp/tcp tls | N/A | If both UDP and TCP are configured at the same time, the last configured protocol is selected. |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| custom-cptone | To configure customized Call Progress Tones. | /native/ios-voice:voice/ios-voice:class/ios-voice:custom-cptone | id (MinLength	1, MaxLength	20) | N/A | Default: True |
| voice class dualtone | To configure call progress dual tones. | /native/ios-voice:voice/ios-voice:class/ios-voice:custom-cptone/ios-voice:dualtone | id, frequency (min 300, max 3600), and cadence | N/A | Values for ID: busy, conference, disconnect, number un-obtainable, out-of-service, reoder, ringback |

| Operations | X-path |
|---|---|
| get, get-config, edit-config | /native/ios-voice:voice/ios-voice:class/ios-voice:tls-cipher |

| Object | X-path |
|---|---|
| ios-voice:tls-profile | /native/ios-voice:voice/ios-voice:class/ios-voice:tls-cipher |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| id | To configure an ordered list of TLS cipher suite in the voice class configuration mode. | /native/ios-voice:voice/ios-voice:class/ios-voice:tls-cipher[ios-voice:id=] | Min 1, Max 10000 | This id should match with the tls-profile tag. | N/A |
| cipher preference | To set the preference order for the cipher-suite (1 = Highest). | /native/ios-voice:voice/ios-voice:class/ios-voice:tls-cipher/ios-voice:cipher/ios-voice:preference | Min 1, Max 13 | N/A | N/A |
| cipher type | To specify the cipher type for each preference number. | /native/ios-voice:voice/ios-voice:class/ios-voice:tls-cipher/ios-voice:cipher/ios-voice:type | DHE_RSA_AES128_GCM_SHA256 supported in TLS 1.2, DHE_RSA_AES256_GCM_SHA384 supported in TLS 1.2, DHE_RSA_WITH_AES_128_CBC_SHA supported in TLS 1.2 & lower, DHE_RSA_WITH_AES_256_CBC_SHA supported in TLS 1.2 & lower, ECDHE_ECDSA_AES128_GCM_SHA256 supported in TLS 1.2, ECDHE_ECDSA_AES256_GCM_SHA384 supported in TLS 1.2 , ECDHE_RSA_AES128_GCM_SHA256 supported in TLS 1.2, ECDHE_RSA_AES256_GCM_SHA384 supported in TLS 1.2, RSA_WITH_AES_128_CBC_SHA supported in TLS 1.2 & lower, RSA_WITH_AES_256_CBC_SHA supported in TLS 1.2 & lower, AES128_GCM_SHA256 supported in TLS 1.3, AES256_GCM_SHA384 supported in TLS 1.3, CHACHA20_POLY1305_SHA256 supported in TLS 1.3. | N/A | N/A |

| Operations | X-path |
|---|---|
| get, get-config, edit-config | /native/ios-voice:voice/ios-voice:class/ios-voice:tls-profile |

| Object | X-path |
|---|---|
| ios-voice:tls-profile | /native/ios-voice:voice/ios-voice:class/ios-voice:tls-profile |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| id | To associate a TLS profile. | /native/ios-voice:voice/ios-voice:class/ios-voice:tls-profile[ios-voice:id="7"]/ios-voice:id | Min-1, Max-10000 | N/A | N/A |
| description | To define the description for input options. | /native/ios-voice:voice/ios-voice:class/ios-voice:tls-profile[ios-voice:id="7"]/ios-voice:description | MinLength-1, MaxLength-80 | N/A | N/A |
| trustpoint | To define the trustpoint name. | /native/ios-voice:voice/ios-voice:class/ios-voice:tls-profile[ios-voice:id="7"]/ios-voice:trustpoint | MinLength-1, Maxlength-142 | N/A | N/A |
| client-vtp | To set the client verification trustpoint. | /native/ios-voice:voice/ios-voice:class/ios-voice:tls-profile[ios-voice:id="7"]/ios-voice:client-vtp | MinLength-1, MaxLength-142 | N/A | This is for Common Criteria (CC) mode. |
| cn-san validate server | To enable CN/SAN validation of server certificates. | /native/ios-voice:voice/ios-voice:class/ios-voice:tls-profile[ios-voice:id=""]/ios-voice:cn-san/ios-voice:validate/ios-voice:server-config | N/A | N/A | N/A |
| cn-san validate client | To enable CN/SAN validation of client certificates. | /native/ios-voice:voice/ios-voice:class/ios-voice:tls-profile[ios-voice:id=""]/ios-voice:cn-san/ios-voice:validate/ios-voice:client | N/A | N/A | N/A |
| cn-san validate bidirectional | To enable CN/SAN validation of both client and server certificates. | /native/ios-voice:voice/ios-voice:class/ios-voice:tls-profile[ios-voice:id=""]/ios-voice:cn-san/ios-voice:validate/ios-voice:bidirectional | N/A | N/A | N/A |
| cn-san id | To specify the tag of CN-SAN hostname or pattern list entry. | /native/ios-voice:voice/ios-voice:class/ios-voice:tls-profile[ios-voice:id=""]/ios-voice:cn-san/ios-voice:tag[ios-voice:id=""] | Min 1, Max10 | N/A | N/A |
| cn-san-name | To specify the Fully Qualified Domain Name (FQDN) or a wildcard pattern in the form of *.{domain-name}. | /native/ios-voice:voice/ios-voice:class/ios-voice:tls-profile[ios-voice:id=""]/ios-voice:cn-san/ios-voice:tag[ios-voice:id=""]/ios-voice:cn-san-name | N/A | N/A | hostname/pattern |
| cipher ecdsa-cipher curve-size | Size of Elliptic Curve to be used. | /native/ios-voice:voice/ios-voice:class/ios-voice:tls-profile[ios-voice:id="7"]/ios-voice:cipher/ios-voice:ecdsa-cipher/ios-voice:curve-size | 384 | N/A | N/A |
| strict-cipher | To use the ciphers mandated by SIP standards. | /native/ios-voice:voice/ios-voice:class/ios-voice:tls-profile[ios-voice:id="7"]/ios-voice:cipher/ios-voice:strict-cipher | N/A | N/A | N/A |
| cipher cipher-list | To specify the tls-cipher list tag. | /native/ios-voice:voice/ios-voice:class/ios-voice:tls-profile/ios-voice:cipher/ios-voice:cipher-list | String | tls-cipher needs to be configured before attaching it to tls-profile. | N/A |
| sni send | To enable Server Name Indication (SNI) during the initial TLS handshake process | /native/ios-voice:voice/ios-voice:class/ios-voice:tls-profile[ios-voice:id="7"]/ios-voice:sni/ios-voice:send | N/A | N/A | N/A |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| codec codec-tag | To configure voice class codec tag. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec-tag | tag (Min 1, Max	10000) | N/A | N/A |
| preference preference-tag | To set priority order for using the codec. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference/ios-voice:preference-tag | tag (Min 1, Max	24) | N/A | N/A |
| preference codec-type | To specify the type of codec. | native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference/ios-voice:codec-type | g711ulaw, g711alaw, g729r8, ilbc, g722-64, aacld, mp4a-latm, opus, g723ar53, g723ar63, g726r16, g726r24, g726r32, g728, clear-channel, isac, g729br8, gsmamr-nb | N/A | N/A |
| preference profile | To specify the profile tag configured in global codec profile. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference/ios-voice:profile | Min 1, Max 1000000 | N/A | N/A |
| preference fmtp-select-one | To offer only one format of multi-format codec (first by default). | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference/ios-voice:fmtp-select-one | N/A | N/A | N/A |
| preference fmtp-select-one bitrate | Exact match of bitrate value in FMTP paramater. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference/ios-voice:fmtp-select-one/ios-voice:bitrate | Min 16000, Max 128000 | N/A | N/A |
| preference fmtp-select-one max-bitrate | To specify the maximum bitrate allowed. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference/ios-voice:fmtp-select-one/ios-voice:max-bitrate | Min 16000, Max 128000 | N/A | N/A |
| preference g729r8-conf bytes | To specify number of voice data bytes per frame for the codec type g729r8. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference/ios-voice:g729r8-conf/ios-voice:bytes | 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240 | N/A | N/A |
| preference g723-g726-conf bytes | To specify number of voice data bytes per frame for the codec types g723ar53, g723r53, and g726r16. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference/ios-voice:g723-g726-conf/ios-voice:bytes | 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240 | N/A | N/A |
| preference g723-conf bytes | To specify number of voice data bytes per frame for the codec types g723ar63 and g723r63. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference/ios-voice:g723-conf/ios-voice:bytes | 24, 48, 72, 96, 120, 144, 168, 192, 216, 240 | N/A | N/A |
| preference g726r24-conf bytes | To specify number of voice data bytes per frame for the codec type g726r24. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference/ios-voice:g726r24-conf/ios-voice:bytes | 30, 60, 90, 120, 150, 180, 210, 240 | N/A | N/A |
| preference g726r32-conf bytes | To specify number of voice data bytes per frame for the codec type g726r32. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference/ios-voice:g726r32-conf/ios-voice:bytes | 40, 80, 120, 160, 200, 240 | N/A | N/A |
| preference ilbc-conf mode twenty bytes | To specify number of voice data bytes per frame for the codec type ilbc. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference/ios-voice:ilbc-conf/ios-voice:mode/ios-voice:twenty/ios-voice:bytes | 38, 76, 114, 152, 190, 228 | N/A | N/A |
| preference ilbc-conf mode thirty bytes | To specify number of voice data bytes per frame for the codec type ilbc. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference/ios-voice:ilbc-conf/ios-voice:mode/ios-voice:thirty/ios-voice:bytes | 50, 100, 150, 200 | N/A | N/A |
| preference gsmamr-nb-conf encap rfc3267 | To specify RTP encapsulation mentioned in RFC3267. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference/ios-voice:gsmamr-nb-conf/ios-voice:encap/ios-voice:rfc3267 | N/A | N/A | N/A |
| preference gsmamr-nb-conf frame-format conf frame-format | To specify the frame format. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference/ios-voice:gsmamr-nb-conf/ios-voice:frame-format-conf/ios-voice:frame-format | bandwidth-efficient, octet-aligned | N/A | N/A |
| preference gsmamr-nb-conf frame-format compute-crc | To specify the frame format in compute-crc. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference/ios-voice:gsmamr-nb-conf/ios-voice:frame-format-conf/ios-voice:compute-crc | crc, no-crc | N/A | N/A |
| preference gsmamr-nb-conf modes-conf modes | To specify the supported modes. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference/ios-voice:gsmamr-nb-conf/ios-voice:modes-conf/ios-voice:modes | Min 0, Max 7 | N/A | N/A |
| preference gsmamr-nb-conf packetization-period-conf packetization-period | To specify the packetization period in milli seconds. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference/ios-voice:gsmamr-nb-conf/ios-voice:packetization-period-conf/ios-voice:packetization-period | Default value: 20 | N/A | N/A |
| video codec codec-type | To choose a video codec type. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:video/ios-voice:codec/ios-voice:codec-type | h261, h263, h263+, h264, mpeg4 | N/A | N/A |
| video codec profile | To specify the video profile tag configured in global codec profile. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:video/ios-voice:codec/ios-voice:profile | Min 1, Max 1000000 | N/A | N/A |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| voice class sip-profiles id | Voice class sip profiles tag. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:id | id (Min 1, Max 10000) | N/A | N/A |
| sip-profiles rule tag | To specify the rule tag. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:tag | Min 1, Max 1073741823 | N/A | N/A |
| rule response sip-responses | To configure a rule for a particular SIP response. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:sip-responses | 100, 180, 181, 182, 183, 200, 202, 300, 301, 302, 305, 380, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 412, 413, 414, 415, 416, 417, 420, 421, 422, 423, 480, 482, 483, 484, 485, 486, 487, 488, 489, 491, 493, 500, 501, 502, 503, 504, 505, 513, 580, 600, 603, 604, 606, ANY | N/A | N/A |
| response sip-responses method method-name | To map a SIP or SDP response to SIP requests. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:method/ios-voice:method-name | ACK, BYE, CANCEL, COMET, INFO, INVITE, NOTIFY, OPTIONS, PRACK, PUBLISH, REFER, REGISTER, REINVITE, SUBSCRIBE, UPDATE | N/A | N/A |
| response sip-responses method peer-header sdp | SDP Line to be copied from peer leg. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:method/ios-voice:peer-header/ios-voice:sdp | Min 0, Max 6 | N/A | Use media line index 0 for session level. |
| response sip-responses method peer-header sdp mline-index | Media line index to copy from. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:method/ios-voice:peer-header/ios-voice:sdp/ios-voice:mline-index | Min 0, Max 6 | N/A | Use media line index 0 for session level. |
| response sip-responses method peer-header sdp COPY match-pattern | To enable copying of SDP header to match a pattern. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:method/ios-voice:peer-header/ios-voice:sdp/ios-voice:COPY/ios-voice:match-pattern | String | N/A | N/A |
| response sip-responses method peer-header sdp COPY copy-variable | Copy variable. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:method/ios-voice:peer-header/ios-voice:sdp/ios-voice:COPY/ios-voice:copy-variable | String | N/A | Valid range is u01-u99. |
| response sip-responses method peer-header sip SIP-Req-URI | SIP Request URI to be copied from peer leg. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:method/ios-voice:peer-header/ios-voice:sip/ios-voice:SIP-Req-URI | N/A | N/A | N/A |
| response sip-responses method peer-header sip SIP-Req-URI COPY match-pattern | To enable copying of SIP Request URI from the peer leg to match a pattern. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:method/ios-voice:peer-header/ios-voice:sip/ios-voice:SIP-Req-URI/ios-voice:COPY/ios-voice:match-pattern | String | N/A | N/A |
| response sip-responses method peer-header sip SIP-Req-URI COPY copy-variable | Copy variable. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:method/ios-voice:peer-header/ios-voice:sip/ios-voice:SIP-Req-URI/ios-voice:COPY/ios-voice:copy-variable | String | N/A | Valid range is u01 to u99. |
| response sip-responses method peer-header sip SIP-StatusLine | SIP Status Line to be copied from peer leg. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:method/ios-voice:peer-header/ios-voice:sip/ios-voice:SIP-StatusLine | N/A | N/A | N/A |
| response sip-responses method peer-header sip SIP-StatusLine COPY match-pattern | To enable copying of SIP Status Line from the peer leg to match a pattern. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:method/ios-voice:peer-header/ios-voice:sip/ios-voice:SIP-StatusLine/ios-voice:COPY/ios-voice:match-pattern | String | N/A | N/A |
| response sip-responses method peer-header sip SIP-StatusLine COPY copy-variable | Copy variable. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:method/ios-voice:peer-header/ios-voice:sip/ios-voice:SIP-StatusLine/ios-voice:COPY/ios-voice:copy-variable | String | N/A | Valid range is u01 to u99. |
| response si.p-responses method peer-header sip header-name | Header name from which the values needs to be copied. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:method/ios-voice:peer-header/ios-voice:sip/ios-voice:header-name-container/ios-voice:header-name | String | N/A | N/A |
| response sip-responses method peer-header sip COPY match-pattern | To enable copying of header name from the peer leg to match a pattern. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:method/ios-voice:peer-header/ios-voice:sip/ios-voice:header-name-container/ios-voice:COPY/ios-voice:match-pattern | String | N/A | N/A |
| response sip-responses method peer-header sip COPY copy-variable | Copy variable. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:method/ios-voice:peer-header/ios-voice:sip/ios-voice:header-name-container/ios-voice:COPY/ios-voice:copy-variable | String | N/A | Valid range is u01 to u99. |
| response sip-responses peer-header sdp | SDP Line to be copied from peer leg. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:peer-header/ios-voice:sdp | N/A | N/A | N/A |
| response sip-responses peer-header sdp mline-index | Copy SDP Line from a particular media line. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:peer-header/ios-voice:sdp/ios-voice:mline-index | Min 0, Max 6 | N/A | Use media line index 0 for session level. |
| response sip-responses peer-header sdp COPY match-pattern | To enable copying of SDP header from the peer leg to match a pattern. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:peer-header/ios-voice:sdp/ios-voice:COPY/ios-voice:match-pattern | String | N/A | N/A |
| response sip-responses peer-header sdp COPY copy-variable | Copy variable. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:peer-header/ios-voice:sdp/ios-voice:COPY/ios-voice:copy-variable | String | N/A | Valid range is u01 to u99. |
| response sip-responses peer-header sip SIP-Req-URI | SIP Request URI to be copied from peer leg. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:peer-header/ios-voice:sip/ios-voice:SIP-Req-URI | N/A | N/A | N/A |
| response sip-responses peer-header sip SIP-Req-URI COPY match-pattern | To enable copying of SIP Request URI from the peer header to match a pattern. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:peer-header/ios-voice:sip/ios-voice:SIP-Req-URI/ios-voice:COPY/ios-voice:match-pattern | String | N/A | N/A |
| response sip-responses peer-header sip SIP-Req-URI COPY copy-variable | Copy variable. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:peer-header/ios-voice:sip/ios-voice:SIP-Req-URI/ios-voice:COPY/ios-voice:copy-variable | String | N/A | Valid range is u01 to u99. |
| response sip-responses peer-header sip SIP-StatusLine | SIP Status-Line to be copied from peer leg. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:peer-header/ios-voice:sip/ios-voice:SIP-StatusLine | N/A | N/A | N/A |
| response sip-responses peer-header sip SIP-StatusLine COPY match-pattern | To enable copying of SIP Status Line from the peer header to match a pattern. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:peer-header/ios-voice:sip/ios-voice:SIP-StatusLine/ios-voice:COPY/ios-voice:match-pattern | String | N/A | N/A |
| response sip-responses peer-header sip SIP-StatusLine COPY copy-variable | Copy variable. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:peer-header/ios-voice:sip/ios-voice:SIP-StatusLine/ios-voice:COPY/ios-voice:copy-variable | String | N/A | Valid range is u01 to u99. |
| response sip-responses peer-header sip header-name | Header name from which the values needs to be copied. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:peer-header/ios-voice:sip/ios-voice:header-name-container/ios-voice:header-name | String | N/A | N/A |
| response sip-responses peer-header sip header-name COPY match-pattern | To enable copying of header name from the peer header to match a pattern. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:peer-header/ios-voice:sip/ios-voice:header-name-container/ios-voice:COPY/ios-voice:match-pattern | String | N/A | N/A |
| response sip-responses peer-header sip header-name COPY copy-variable | Copy variable. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:peer-header/ios-voice:sip/ios-voice:header-name-container/ios-voice:COPY/ios-voice:copy-variable | String | N/A | Valid range is u01 to u99. |
| response sip-responses sdp-header | To map a SIP response to SDP header requests. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:sdp-header/ios-voice:header | Attribute, Audio-Attribute, Audio-Bandwidth-Info, Audio-Connection-Info, Audio-Encryption-Key, Audio-Media, Audio-Session-Info, Bandwidth-Key, Connection-Info, Email-Address, Encrypt-Key, Phone-Number, Repeat-Times, Session-Info, Session-Name, Session-Owner,  Time-Adjust-Key, Time-Header, Url-Descriptor, Version, Video-Attribute, Video-Bandwidth-Info, Video-Connection-Info, Video-Encryption-Key, Video-Media, Video-Session-Info, mline-index | N/A | N/A |
| response sip-responses sdp-header ADD | To add an SDP header to a SIP response. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:sdp-header/ios-voice:ADD | String | N/A | Audio-Media, Session-Name, Session-Owner, Time-Header, Version, Video- Media do not allow ADD operation. |
| response sip-responses sdp-header MODIFY match-pattern | To modify an SDP header by matching a pattern. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:sdp-header/ios-voice:MODIFY/ios-voice:match-pattern | String | N/A | N/A |
| response sip-responses sdp-header MODIFY replace-pattern | To modify an SDP header by replacing a pattern. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:sdp-header/ios-voice:MODIFY/ios-voice:replace-pattern | String | N/A | N/A |
| response sip-responses sdp-header REMOVE | To remove an SDP header. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:sdp-header/ios-voice:REMOVE | N/A | N/A | Audio-Media, Session-Name, Session-Owner, Time-Header, Version, Video- Media do not allow REMOVE operation. |
| response sip-responses sdp-header COPY match-pattern | To copy an SDP header to match a pattern. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:sdp-header/ios-voice:COPY/ios-voice:match-pattern | String | N/A | N/A |
| response sip-responses sdp-header COPY copy-variable | Copy variable. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:sdp-header/ios-voice:COPY/ios-voice:copy-variable | String | N/A | Valid range is u01 to u99. |
| response sip-responses sip-header | To map a SIP response to SIP header requests. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:sdp-header/ios-voice:header | Accept-Contact, Accept-Encoding, Accept-Header, Accept-Language, Accept-Resource-Priority, Alert-Info,  Allow-Events, Allow-Header, Also, Authorization, CC-Diversion, CC-Redirect, CSeq, Call-ID, Call-Info, Cisco-Gcid, Cisco-Guid, Contact, Content-Disposition, Content-Encoding, Content-Id, Content-Length, Content-Type, Date, Diversion, Event, Expires, From, History-Info, Location, MIME-Version,  Max-Forwards, Min-Expires, Min-SE, Orig-dial-plan, P-Asserted-Identity, P-Preferred-Identity, P-RTP-Stat, Privacy, Proxy-Authenticate, Proxy-Authorization, Proxy-Require, Rack, Reason, Record-Route, Refer-To, Referred-By, Reject-Contact, Remote-Party-ID, Replaces, Request-Disposition, Requested-By, Require, Resource-Priority,  Retry-After, Route, Rseq, SIP-ETag, SIP-If-Match, SIP-Req-URI, SIP-StatusLine, Server, Session-Expires, Session-Header,  Session-ID, Subscription-State, Supported, Term-dial-plan, Timestamp, To, Unsupported, User-Agent,  Via, WORD, WWW-Authenticate,  Warning | N/A | N/A |
| response sip-responses sip-header any-word | To map SIP header to any other SIP header name. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:sip-header/ios-voice:any-word | String | N/A | N/A |
| response sip-responses sip-header ADD | Addition of the header. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:sip-header/ios-voice:ADD | String | N/A | To, From, CSeq, Call-ID, Max-Forwards, Via, SIPReq-URI, SIPStatusLine headers do not allow ADD opeartion. |
| response sip-responses sip-header MODIFY match-pattern | Modification of the header by matching a pattern. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:sip-header/ios-voice:MODIFY/ios-voice:match-pattern | String | N/A | N/A |
| response sip-responses sip-header MODIFY replace-pattern | Modification of the header by replacing a pattern. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:sip-header/ios-voice:MODIFY/ios-voice:replace-pattern | String | N/A | N/A |
| response sip-responses sip-header REMOVE | Removal of the header. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:sip-header/ios-voice:REMOVE | N/A | N/A | To, From, CSeq, Call-ID, Max-Forwards, Via, SIPReq-URI, SIPStatusLine headers do not allow REMOVE opeartion. |
| response sip-responses sip-header COPY match-pattern | To copy the header to match a pattern. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:sip-header/ios-voice:COPY/ios-voice:match-pattern | String | N/A | N/A |
| response sip-responses sip-header COPY copy-variable | Copy variable. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:response/ios-voice:sip-header/ios-voice:COPY/ios-voice:copy-variable | String | N/A | Valid range is u01 to u99. |
| rule request sip-requests | To configure a rule for a particular SIP request. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:request/ios-voice:sip-requests | ACK, BYE, CANCEL, COMET, INFO, INVITE, NOTIFY, OPTIONS, PRACK, PUBLISH, REFER, REGISTER, REINVITE, SUBSCRIBE, UPDATE | N/A | N/A |
| request sip-requests peer-header sdp mline-index | To enable copying of media line index from the peer leg. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:request/ios-voice:peer-header/ios-voice:sdp/ios-voice:mline-index | Min 0, Max 6 | N/A | Use index 0 for session level. |
| request sip-requests peer-header sdp COPY match-pattern | To enable copying SDP header from the peer leg to match a pattern. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:request/ios-voice:peer-header/ios-voice:sdp/ios-voice:COPY/ios-voice:match-pattern | String | N/A | Use index 0 for session level. |
| request sip-requests peer-header sdp COPY copy-variable | Copy variable. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:request/ios-voice:peer-header/ios-voice:sdp/ios-voice:COPY/ios-voice:copy-variable | String | N/A | Valid range is u01 to u99. |
| request sip-requests peer-header sip SIP-Req-URI | SIP Request URI to be copied from peer leg. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:request/ios-voice:peer-header/ios-voice:sip/ios-voice:SIP-Req-URI | N/A | N/A | N/A |
| request sip-requests peer-header sip SIP-Req-URI COPY match-pattern | To enable copying of SIP Req URI to match a pattern. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:request/ios-voice:peer-header/ios-voice:sip/ios-voice:SIP-Req-URI/ios-voice:COPY/ios-voice:match-pattern | String | N/A | N/A |
| request sip-requests peer-header sip SIP-Req-URI COPY copy-variable | Copy variable. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:request/ios-voice:peer-header/ios-voice:sip/ios-voice:SIP-Req-URI/ios-voice:COPY/ios-voice:copy-variable | String | N/A | Valid range is u01 to u99. |
| request sip-requests peer-header sip SIP-StatusLine | SIP Status-Line to be copied from peer leg. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:request/ios-voice:peer-header/ios-voice:sip/ios-voice:SIP-StatusLine | N/A | N/A | N/A |
| request sip-requests peer-header sip SIP-StatusLine COPY match-pattern | To enable copying of SIP Status Line to match a pattern. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:request/ios-voice:peer-header/ios-voice:sip/ios-voice:SIP-StatusLine/ios-voice:COPY/ios-voice:match-pattern | String | N/A | N/A |
| request sip-requests peer-header sip SIP-StatusLine COPY copy-variable | Copy variable. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:request/ios-voice:peer-header/ios-voice:sip/ios-voice:SIP-StatusLine/ios-voice:COPY/ios-voice:copy-variable | String | N/A | Valid range is u01 to u99. |
| request sip-requests peer-header sip header-name | Header name from which the values needs to be copied. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:request/ios-voice:peer-header/ios-voice:sip/ios-voice:header-name-container/ios-voice:header-name | String | N/A | N/A |
| request sip-requests peer-header sip COPY match-pattern | To enable copying of header name to match a pattern. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:request/ios-voice:peer-header/ios-voice:sip/ios-voice:header-name-container/ios-voice:COPY/ios-voice:match-pattern | String | N/A | N/A |
| request sip-requests peer-header sip COPY copy-variable | Copy variable. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:request/ios-voice:peer-header/ios-voice:sip/ios-voice:header-name-container/ios-voice:COPY/ios-voice:copy-variable | String | N/A | Valid range is u01 to u99. |
| request sip-requests sdp-header | To map SIP requests to a SDP header requests. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:request/ios-voice:sdp-header/ios-voice:header | Attribute, Audio-Attribute, Audio-Bandwidth-Info, Audio-Connection-Info, Audio-Encryption-Key, Audio-Media, Audio-Session-Info, Bandwidth-Key, Connection-Info, Email-Address, Encrypt-Key, Phone-Number, Repeat-Times, Session-Info, Session-Name, Session-Owner,  Time-Adjust-Key, Time-Header, Url-Descriptor, Version, Video-Attribute, Video-Bandwidth-Info, Video-Connection-Info, Video-Encryption-Key, Video-Media, Video-Session-Info, mline-index | N/A | N/A |
| request sip-requests sdp-header ADD | Addition of the header. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:request/ios-voice:sdp-header/ios-voice:ADD | String | N/A | Audio-Media, Session-Name, Session-Owner, Time-Header, Version, Video- Media do not allow ADD operation. |
| request sip-requests sdp-header MODIFY match-pattern | Modification of the SDP header by matching a pattern. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:request/ios-voice:sdp-header/ios-voice:MODIFY/ios-voice:match-pattern | String | N/A | N/A |
| request sip-requests sdp-header MODIFY replace-pattern | Modification of the SIP header by replacing a pattern. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:request/ios-voice:sdp-header/ios-voice:MODIFY/ios-voice:replace-pattern | String | N/A | N/A |
| request sip-requests sdp-header REMOVE | Removal of the the SDP header. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:request/ios-voice:sdp-header/ios-voice:REMOVE | N/A | N/A | Audio-Media, Session-Name, Session-Owner, Time-Header, Version, Video- Media do not allow REMOVE operation. |
| request sip-requests sdp-header COPY match-pattern | To copy the header to match a pattern. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:request/ios-voice:sdp-header/ios-voice:COPY/ios-voice:match-pattern | String | N/A | N/A |
| request sip-requests sdp-header COPY copy-variable | Copy variable. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:request/ios-voice:sdp-header/ios-voice:COPY/ios-voice:copy-variable | String | N/A | Valid range is u01 to u99. |
| request sip-requests sip header | To map SIP requests to SIP header requests. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:request/ios-voice:sip-header/ios-voice:header | Accept-Contact, Accept-Encoding, Accept-Header, Accept-Language, Accept-Resource-Priority, Alert-Info,  Allow-Events, Allow-Header, Also, Authorization, CC-Diversion, CC-Redirect, CSeq, Call-ID, Call-Info, Cisco-Gcid, Cisco-Guid, Contact, Content-Disposition, Content-Encoding, Content-Id, Content-Length, Content-Type, Date, Diversion, Event, Expires, From, History-Info, Location, MIME-Version,  Max-Forwards, Min-Expires, Min-SE, Orig-dial-plan, P-Asserted-Identity, P-Preferred-Identity, P-RTP-Stat, Privacy, Proxy-Authenticate, Proxy-Authorization, Proxy-Require, Rack, Reason, Record-Route, Refer-To, Referred-By, Reject-Contact, Remote-Party-ID, Replaces, Request-Disposition, Requested-By, Require, Resource-Priority,  Retry-After, Route, Rseq, SIP-ETag, SIP-If-Match, SIP-Req-URI, SIP-StatusLine, Server, Session-Expires, Session-Header,  Session-ID, Subscription-State, Supported, Term-dial-plan, Timestamp, To, Unsupported, User-Agent,  Via, WORD, WWW-Authenticate,  Warning | N/A | N/A |
| request sip-requests sip header any-word | To map SIP requests to any other SIP header name. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:request/ios-voice:sip-header/ios-voice:any-word | String | N/A | N/A |
| request sip-requests sip header ADD | Addition of a SIP header. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:request/ios-voice:sip-header/ios-voice:ADD | String | N/A | To, From, CSeq, Call-ID, Max-Forwards, Via, SIPReq-URI, SIPStatusLine headers do not allow ADD opeartion. |
| request sip-requests sip header MODIFY match-pattern | Modification of the SIP header by matching a pattern. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:request/ios-voice:sip-header/ios-voice:MODIFY/ios-voice:match-pattern | String | N/A | N/A |
| request sip-requests sip header MODIFY replace-pattern | Modification of the SIP header by replacing a pattern. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:request/ios-voice:sip-header/ios-voice:MODIFY/ios-voice:replace-pattern | String | N/A | N/A |
| request sip-requests sip header REMOVE | Removal of a SIP header. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:request/ios-voice:sip-header/ios-voice:REMOVE | String | N/A | To, From, CSeq, Call-ID, Max-Forwards, Via, SIPReq-URI, SIPStatusLine headers do not allow REMOVE opeartion. |
| request sip-requests sip header COPY match-pattern | To copy a SIP header to match a pattern. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:request/ios-voice:sip-header/ios-voice:COPY/ios-voice:match-pattern | String | N/A | N/A |
| request sip-requests sip header COPY copy-variable | Copy variable. | native/ios-voice:voice/ios-voice:class/ios-voice:sip-profiles/ios-voice:rule/ios-voice:response-request/ios-voice:request/ios-voice:sip-header/ios-voice:COPY/ios-voice:copy-variable | String | N/A | Valid range is u01 to u99. |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| dualtone-detect-params | To configure dual tone detection parameters. | /native/ios-voice:voice/ios-voice:class/ios-voice:dualtone-detect-params | id (Min	1, Max	10000) | N/A | Default: True |
| cadence-variation | To configure cadence variation. | /native/ios-voice:voice/ios-voice:class/ios-voice:dualtone-detect-params/ios-voice:cadence-variation | 0 to 200 | N/A | Default: 10 |
| freq-max-delay | To configure timing difference between two frequencies. | /native/ios-voice:voice/ios-voice:class/ios-voice:dualtone-detect-params/ios-voice:freq-max-delay | 10 to 100 | N/A | Default: 10 |
| freq-max-deviation | To configure maximum frequency deviation allowed for each frequency. | /native/ios-voice:voice/ios-voice:class/ios-voice:dualtone-detect-params/ios-voice:freq-max-deviation | 10 to 125 | N/A | Default: 10 |
| freq-max-power | To configure absolute value of upper limit for tone power per frequency. | /native/ios-voice:voice/ios-voice:class/ios-voice:dualtone-detect-params/ios-voice:freq-max-power | 0 to 20 | N/A | Default: 10 |
| freq-min-power | To configure absolute value of lower limit for tone power per frequency. | /native/ios-voice:voice/ios-voice:class/ios-voice:dualtone-detect-params/ios-voice:freq-min-power | 10 to 35 | N/A | Default: 30 |
| freq-power-twist | To configure the difference between the power of two frequencies. | /native/ios-voice:voice/ios-voice:class/ios-voice:dualtone-detect-params/ios-voice:freq-power-twist | 0 to 15 | N/A | Default: 6 |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| codec codec-tag | To configure voice class codec tag. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec-tag | tag (Min 1, Max	10000) | N/A | N/A |
| preference preference-tag | To set priority order for using the codec. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference/ios-voice:preference-tag | tag (Min 1, Max	24) | N/A | N/A |
| preference codec-type | To specify the type of codec. | native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference/ios-voice:codec-type | aacld, mp4a-latm, opus | N/A | N/A |
| preference profile | To specify the profile tag configured in global codec profile. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference/ios-voice:profile | Min 1, Max 1000000 | N/A | N/A |
| preference fmtp-select-one | To offer only one format of multi-format codec (first by default). | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference/ios-voice:fmtp-select-one | N/A | N/A | N/A |
| preference fmtp-select-one bitrate | Exact match of bitrate value in FMTP paramater. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference/ios-voice:fmtp-select-one/ios-voice:bitrate | Min 16000, Max 128000 | N/A | N/A |
| preference fmtp-select-one max-bitrate | To specify the maximum bitrate allowed. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference/ios-voice:fmtp-select-one/ios-voice:max-bitrate | Min 16000, Max 128000 | N/A | N/A |
| preference g723-g726-conf bytes | To specify number of voice data bytes per frame for the codec types g723ar53, g723r53, and g726r16. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference/ios-voice:g723-g726-conf/ios-voice:bytes | 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240 | N/A | N/A |
| preference g723-conf bytes | To specify number of voice data bytes per frame for the codec types g723ar63 and g723r63. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference/ios-voice:g723-conf/ios-voice:bytes | 24, 48, 72, 96, 120, 144, 168, 192, 216, 240 | N/A | N/A |
| preference g726r24-conf bytes | To specify number of voice data bytes per frame for the codec type g726r24. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference/ios-voice:g726r24-conf/ios-voice:bytes | 30, 60, 90, 120, 150, 180, 210, 240 | N/A | N/A |
| preference g726r32-conf bytes | To specify number of voice data bytes per frame for the codec type g726r32. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference/ios-voice:g726r32-conf/ios-voice:bytes | 40, 80, 120, 160, 200, 240 | N/A | N/A |
| preference ilbc-conf mode twenty bytes | To specify number of voice data bytes per frame for the codec type ilbc. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference/ios-voice:ilbc-conf/ios-voice:mode/ios-voice:twenty/ios-voice:bytes | 38, 76, 114, 152, 190, 228 | N/A | N/A |
| preference ilbc-conf mode thirty bytes | To specify number of voice data bytes per frame for the codec type ilbc. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference/ios-voice:ilbc-conf/ios-voice:mode/ios-voice:thirty/ios-voice:bytes | 50, 100, 150, 200 | N/A | N/A |
| video codec codec-type | To choose a video codec type. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:video/ios-voice:codec/ios-voice:codec-type | h263, h263+, h264 | N/A | N/A |
| video codec profile | To specify the video profile tag configured in global codec profile. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:video/ios-voice:codec/ios-voice:profile | Min 1, Max 1000000 | N/A | N/A |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| voice class sip-copylist sip_copylist_tag | To configure a list of entities to be sent to peer leg. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-copylist | Min 1, Max 10000 | N/A | N/A |
| voice class sip-copylist sip-header SIP-Req-URI | SIP Request URI to be sent to peer leg. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-copylist/ios-voice:sip-header/ios-voice:SIP-Req-URI | N/A | N/A | N/A |
| voice class sip-copylist sip-header SIP-StatusLine | SIP Status-Line to be sent to peer leg. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-copylist/ios-voice:sip-header/ios-voice:SIP-StatusLine | N/A | N/A | N/A |
| voice class sip-copylist sip-header header_name | Header name of header to be sent to peer leg. | /native/ios-voice:voice/ios-voice:class/ios-voice:sip-copylist/ios-voice:sip-header/ios-voice:header_name | String | N/A | N/A |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| voice class dpg id | To create a dial-peer group for grouping multiple outbound dial peers. | /native/ios-voice:voice/ios-voice:class/ios-voice:dpg/ios-voice:id | tag (Min 1, Max 10000) | N/A | N/A |
| dial-peer id | To associate a configured outbound dial peer with this dial-peer group. | /native/ios-voice:voice/ios-voice:class/ios-voice:dpg/ios-voice:dial-peer/ios-voice:id | tag (Min	1, Max	1073741823) | N/A | This is a list of dial peers. |
| dial-peer preference | To configure preference order of this dial peer in this group. | /native/ios-voice:voice/ios-voice:class/ios-voice:dpg/ios-voice:dial-peer/ios-voice:preference | preference (Min 0, Max 10) | N/A | N/A |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| voice class stun-usage id | To set stun usage global parameters . | /native/ios-voice:voice/ios-voice:class/ios-voice:stun-usage | tag (Min 1, Max 10000) | N/A | N/A |
| stun usage firewall-traversal flowdata | To enable firewall traversal using flowdata for VoIP communications. | /native/ios-voice:voice/ios-voice:class/ios-voice:stun-usage/ios-voice:stun/ios-voice:usage/ios-voice:firewall-traversal/ios-voice:flowdata | N/A | N/A | N/A |
| stun usage ice lite | To configure ICE in Ice-Lite mode. | /native/ios-voice:voice/ios-voice:class/ios-voice:stun-usage/ios-voice:stun/ios-voice:usage/ios-voice:ice/ios-voice:lite | N/A | N/A | N/A |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| voice class srtp-crypto id | To configure set of SRTP cipher suites in preferred order | /native/ios-voice:voice/ios-voice:class/ios-voice:srtp-crypto/ios-voice:id | tag (Min 1, Max 10000) | N/A | N/A |
| crypto id | To set the preference order for the cipher suite. | /native/ios-voice:voice/ios-voice:class/ios-voice:srtp-crypto/ios-voice:crypto/ios-voice:id | tag (Min 1, Max 4) | N/A | N/A |
| crypto crypto-type | To specify the cipher suites that are configured. | /native/ios-voice:voice/ios-voice:class/ios-voice:srtp-crypto/ios-voice:crypto/ios-voice:crypto-type | AEAD_AES_128_GCM, AEAD_AES_256_GCM, AES_CM_128_HMAC_SHA1_32, AES_CM_128_HMAC_SHA1_80 | N/A | N/A |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| voice statistics type iec | To display Internal Error Code (IEC) statistics. | /native/ios-voice:voice/ios-voice:statistics/ios-voice:type/ios-voice:iec | N/A | N/A | N/A |
| voice statistics time-range since-reset | To collect statistics since the last reset. | /native/ios-voice:voice/ios-voice:statistics/ios-voice:time-range/ios-voice:since-reset | N/A | N/A | N/A |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| stun | To configure firewall traversal parameters for VoIP communications. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:stun | N/A | N/A | N/A |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| agent-id | To configure the agent id and the boot count to configure call control agents which authorize the flow of traffic. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:stun/ios-voice:stun/ios-voice:flowdata/ios-voice:agent | 0 to 255 | N/A | (Optional) Boot count, Value: 0 to 65535. Default: 0 |
| catlife | To configure the lifetime of the Crypto Acceptance Token (CAT). | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:stun/ios-voice:stun/ios-voice:flowdata/ios-voice:catlife | Default value 1270 = (21 min 10 sec) | N/A | N/A |
| keepalive | To configure the keepalive interval. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:stun/ios-voice:stun/ios-voice:flowdata/ios-voice:catlife/ios-voice:keepalive | 1 to 65535. Default: 10 | Catlife should be configured | Options: 30, 70, 150, 310, 630, and 1270 |
| transaction timer | To set STUN transaction timer. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:stun/ios-voice:stun/ios-voice:transaction-timer | Min 10, Max 50 | N/A | Default value is 10. |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| clid | To configure Caller ID option. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:clid | N/A | N/A | N/A |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| network-provided | Set screen ind in oct3a to network-provided for SIP calls. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:clid/ios-voice:network-provided | N/A | N/A | N/A |
| strip pi -restrict all | To remove calling party name and number when PI restricted for SIP. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:clid/ios-voice:strip/ios-voice:pi-restrict/ios-voice:all | N/A | N/A | N/A |
| substitute name | To configure sub calling num for missing display name for SIP if PI allows. | /native/ios-voice:voice/ios-voice:service[ios-voice:type="voip"]/ios-voice:clid/ios-voice:substitute/ios-voice:name | N/A | N/A | N/A |

| Operations | X-path |
|---|---|
| get, get-config, edit-config | /native/ios-voice:voice/ios-voice:mode/ios-voice:border-element |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| mode border-element license periodicity | To configure mode border-element license periodicity. | /native/ios-voice:voice/ios-voice:mode/ios-voice:border-element/ios-voice:license/ios-voice:periodicity | Min (1 to 59), Hours (1 to 23), and Days (1 to 30) | N/A | N/A |