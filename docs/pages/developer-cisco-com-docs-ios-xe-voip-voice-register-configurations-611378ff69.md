---
doc_id: developer-cisco-com-docs-ios-xe-voip-voice-register-configurations-611378ff69
source_url: https://developer.cisco.com/docs/ios-xe-voip/voice-register-configurations/
retrieved_at: 2026-08-25T21:02:33.557003+00:00
---

# Voice Register Configurations

You can perform the voice register global and pool configurations, using the ios-voice:register configuration mode. The ios-voice:register configuration mode is a part of Cisco-IOS-XE-voice module. The following operations are allowed in the ios-voice:register configuration mode.

## Select Voice Register Configuration Mode

To enter into the ios-voice:register configuration mode, follow the x-path provided in the below table.

## Configuration Recommendations

- The max-dn, max-pool value range is limited by the platform that is being configured.

- There is a dependency between voice class codec and voice register pool configuration.

- Ensure that there is no voice register pool that is associated with a voice class codec that is deleted.

## Voice Register Global Configuration

The ios-voice:register configuration mode allows you to perform the following global configurations:

Voice Register Configurations and X-path details

## Voice Register Pool Configuration

The voice register pool configuration allows you to control which phone registrations are accepted or rejected by a Cisco Unified SIP SRST device.

### Prerequisites for 'ios-voice:register' configuration

- The pool-tag field is the KEY for ios-voice:register pool configuration. This is a mandatory field to configure other pool configurations at global level.

The ios-voice:register configuration mode allows you to perform the following pool configurations:

Voice Register Pool configurations and X-path details

## Examples: Voice Register Configurations

Following are the examples for Voice Register Global and Pool Configurations.

Example for get-config operation:

Request

Code Snippet

```
Sending:

# < nc: rpc xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " message-id = " urn:uuid:1cec4992-d3e5-42d0-994a-361ac2148e93 " > < nc: get-config > < nc: source > < nc: running /> </ nc: source > < nc: filter > < native xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-native " > < voice xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-voice " > < register > < global > < max-dn /> < max-pool /> </ global > </ register > </ voice > </ native > </ nc: filter > </ nc: get-config > </ nc: rpc > ##
```

Response

Code Snippet

```
Received: < rpc-reply xmlns = " urn:ietf:params:xml:ns:netconf:base:1.0 " xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " message-id = " urn:uuid:1cec4992-d3e5-42d0-994a-361ac2148e93 " > < data > < native xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-native " > < voice xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-voice " > < register > < global > < max-dn > 10 </ max-dn > < max-pool > 10 </ max-pool > </ global > </ register > </ voice > </ native > </ data > </ rpc-reply >
```

Example for edit-config operation:

Request

Code Snippet

```
Sending:

# < nc: rpc xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " message-id = " urn:uuid:49bcfa87-4bbf-461f-b488-7ef5c345de8a " > < nc: edit-config > < nc: target > < nc: running /> </ nc: target > < nc: config > < native xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-native " > < voice xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-voice " > < register > < global > < max-dn > 20 </ max-dn > < max-pool > 30 </ max-pool > < system > < message > test </ message > </ system > </ global > </ register > </ voice > </ native > </ nc: config > </ nc: edit-config > </ nc: rpc > ##
```

Response

Code Snippet

```
Received: < rpc-reply xmlns = " urn:ietf:params:xml:ns:netconf:base:1.0 " xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " message-id = " urn:uuid:ae5ec0fb-ca45-4c8b-a984-c3fe8c6aac61 " > < ok /> </ rpc-reply >
```

Next

| Operations | X-path |
|---|---|
| get, get-config, edit-config | /native/ios-voice:voice/ios-voice:register |

| Object | X-path |
|---|---|
| ios-voice:register | /native/ios-voice:voice/ios-voice:register |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| voice register global | To set global parameters. | /native/ios-voice:voice/ios-voice:register/ios-voice:global | max-dn, max-pool, system , max-dn: 1-3500, max-pool: 1-2000 | N/A | N/A |
| max-dn | To configure maximum directory numbers supported. | /native/ios-voice:voice/ios-voice:register/ios-voice:global/ios-voice:max-dn | Min-1, Max-3500 | N/A | N/A |
| max-pool | To configure maximum pools to support. | /native/ios-voice:voice/ios-voice:register/ios-voice:global/ios-voice:max-pool | Min-1, Max-2000 | N/A | Default: 2000 |
| system | To define system message. | /native/ios-voice:voice/ios-voice:register/ios-voice:global/ios-voice:system | N/A | N/A | N/A |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| voice register pool-tag | To create a pool configuration. | /native/ios-voice:voice/ios-voice:register/ios-voice:pool/ios-voice:pool-tag | Min-1, Max-2000 | N/A | N/A |
| call-forward | To define E.164 telephone number for call forward | /native/ios-voice:voice/ios-voice:register/ios-voice:pool[ios-voice:pool-tag="100"]/ios-voice:call-forward | N/A | N/A | N/A |
| b2bua | To define call forward for B2BUA (back-to-back user agent) | /native/ios-voice:voice/ios-voice:register/ios-voice:pool[ios-voice:pool-tag="100"]/ios-voice:call-forward/ios-voice:b2bua | all, busy, mailbox | N/A | N/A |
| noan-config | To configure call forwarding for a SIP B2BUA so that incoming calls to an extension that does not answer after a configured amount of time are forwarded to another extension. | /native/ios-voice:voice/ios-voice:register/ios-voice:pool[ios-voice:pool-tag="100"]/ios-voice:call-forward/ios-voice:b2bua/ios-voice:noan-config | all, busy, mailbox | N/A | N/A |
| id | To define phone or device id | /native/ios-voice:voice/ios-voice:register/ios-voice:pool[ios-voice:pool-tag="100"]/ios-voice:id | N/A | N/A | N/A |
| network | To define phone or device network address | /native/ios-voice:voice/ios-voice:register/ios-voice:pool[ios-voice:pool-tag="100"]/ios-voice:id/ios-voice:network | IP address; IPV4 Address (IPv4 Address Mask), IPV6 Address | N/A | IPV4 Address Pattern: "(([0-9]\|[1-9][0-9]\|1[0-9][0-9]\|2[0-4][0-9]\|25[0-5])\\.){3}([0-9]\|[1-9][0-9]\|1[0-9][0-9]\|2[0-4][0-9]\|25[0-5])(%[\\p{N}\\p{L}]+)?", IPV6 Address Pattern: "((:\|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:\|[0-9a-fA-F]{0,4}))\|(((25[0-5]\|2[0-4][0-9]\|[01]?[0-9]?[0-9])\\.){3}(25[0-5]\|2[0-4][0-9]\|[01]?[0-9]?[0-9])))(/(([0-9])\|([0-9]{2})\|(1[0-1][0-9])\|(12[0-8])))"
"(([^:]+:){6}(([^:]+:[^:]+)\|(.*\\..*)))\|((([^:]+:)*[^:]+)?::(([^:]+:)*[^:]+)?)(/.+)" |
| voice-class | To set global codec parameters. | /native/ios-voice:voice/ios-voice:register/ios-voice:pool[ios-voice:pool-tag="100"]/ios-voice:voice-class | codec, Min-1, Max-10000 | N/A | N/A |
| dtmf-relay | To configure the list of DTMF relay methods that can be used to relay dual-tone multifrequency (DTMF) audio tones between Session Initiation Protocol (SIP) endpoints. | /native/ios-voice:voice/ios-voice:register/ios-voice:pool[ios-voice:pool-tag="100"]/ios-voice:dtmf-relay | rtp-nte, sip-kpml, sip-notify | N/A | N/A |
| cor incoming | To configure COR list to be used by incoming dial peers. | voice register cor incoming: /native/ios-voice:voice/ios-voice:register/ios-voice:pool/ios-voice:cor/ios-voice:incoming | N/A | N/A | N/A |
| list_name | To name COR list to be used by incoming dial peers. | voice register cor incoming: /native/ios-voice:voice/ios-voice:register/ios-voice:pool/ios-voice:cor/ios-voice:incoming/ios-voice:name | String | 'dial-peer cor list' should be configured first. | N/A |
| id | To configure COR list to be used by incoming dial peers. | /native/ios-voice:voice/ios-voice:register/ios-voice:pool/ios-voice:cor/ios-voice:incoming/ios-voice:id | The value can be 1-20 or default. | N/A | N/A |
| list_name id lowerbound | To specify a lower range for a COR list to be used by incoming dial peers. | /native/ios-voice:voice/ios-voice:register/ios-voice:pool/ios-voice:cor/ios-voice:incoming/ios-voice:lowerbound | String | N/A | This can be configured only if the tag 1-20 is chosen above. For default tag, this is not applicable. |
| list_name id lowerbound hyphen | To name COR list to be used by incoming dial peers. | /native/ios-voice:voice/ios-voice:register/ios-voice:pool/ios-voice:cor/ios-voice:incoming/ios-voice:hyphen | N/A | N/A | N/A |
| list_name id lowerbound hyphen upperbound | To configure a range for COR list to be used by incoming dial peers. | /native/ios-voice:voice/ios-voice:register/ios-voice:pool/ios-voice:cor/ios-voice:incoming/ios-voice:upperbound | String | N/A | N/A |
| cor outgoing | To configure COR list to be used by outgoing dial peers. | voice register cor outgoing: /native/ios-voice:voice/ios-voice:register/ios-voice:pool/ios-voice:cor/ios-voice:outgoing | N/A | N/A | N/A |
| list_name | To name COR list to be used by outgoing dial peers. | voice register cor outgoing: /native/ios-voice:voice/ios-voice:register/ios-voice:pool/ios-voice:cor/ios-voice:incoming/ios-voice:name | String | 'dial-peer cor list' should be configured first. | N/A |
| id | To configure COR list to be used by outgoing dial peers. | /native/ios-voice:voice/ios-voice:register/ios-voice:pool/ios-voice:cor/ios-voice:outgoing/ios-voice:id | The value can be 1-20 or default. | N/A | N/A |
| list_name id lowerbound | To specify a lower range for a COR list to be used by outgoing dial peers. | /native/ios-voice:voice/ios-voice:register/ios-voice:pool/ios-voice:cor/ios-voice:outgoing/ios-voice:lowerbound | String | N/A | This can be configured only if the tag 1-20 is chosen above. For default tag, this is not applicable. |
| list_name id lowerbound hyphen | To name COR list to be used by outgoing dial peers. | /native/ios-voice:voice/ios-voice:register/ios-voice:pool/ios-voice:cor/ios-voice:outgoing/ios-voice:hyphen | N/A | N/A | N/A |
| list_name id lowerbound hyphen upperbound | To configure a range for COR list to be used by outgoing dial peers. | /native/ios-voice:voice/ios-voice:register/ios-voice:pool/ios-voice:cor/ios-voice:outgoing/ios-voice:upperbound | String | N/A | N/A |