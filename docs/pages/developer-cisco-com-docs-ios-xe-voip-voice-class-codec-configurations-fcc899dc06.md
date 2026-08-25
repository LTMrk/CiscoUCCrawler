---
doc_id: developer-cisco-com-docs-ios-xe-voip-voice-class-codec-configurations-fcc899dc06
source_url: https://developer.cisco.com/docs/ios-xe-voip/voice-class-codec-configurations/
retrieved_at: 2026-08-25T21:02:29.389464+00:00
---

# Voice Class Codec Configurations

You can perform the voice class codec configuration, using the ios-voice:codec configuration mode under ios-voice:voice configuration mode. The ios-voice:codec configuration mode is a part of Cisco-IOS-XE-voice module. The following operations are allowed in the ios-voice:codec configuration mode.

## Select VoIP Service Configuration Mode

To enter into the ios-voice:codec configuration mode, follow the x-path provided in the below table.

## Configuration Recommendations

The voice class codec and codec preference can be configured as follows:

- voice class codec <1-10000>

- codec preference <1-24> g711ulaw

- codec preference <1-24> g711alaw

- codec preference <1-24> g729r8

- codec preference <1-24> ilbc mode

- codec preference <1-24> g722-64

- codec preference <1-24> opus profile <1-1000000>

- codec preference <1-24> scip

You cannot associate the same codec more than once within a codec class. For example, the following is not a supported configuration:

- voice class codec 10

- codec preference 1 g711ulaw

- codec preference 20 g711ulaw

For the codecs g711ulaw, g711alaw and g722-64, you can specify the size of the voice frames as follows:

- codec preference <1-24> g711ulaw [bytes {80,160,240}]

For the codec g729r8, you can specify the size of the voice frames as follows:

- codec preference <1-24> g729r8 [bytes {10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240}]

For the iLBC codec, you can specify the mode and size of the voice frames as follows:

- codec preference <1-24> ilbc mode [20 bytes {38, 76, 114, 152, 190, 228} | 30 bytes {50, 100, 150, 200}]

For the scip video codec, you can specify the codec type as follows:

- video codec scip

The ios-voice:codec configuration mode allows you to perform the following codec configurations:

Codec configurations and X-path details

## Examples: Voice Class Codec Configuration

Following are the examples for Voice Class Codec Configurations.

Example for get-config operation:

Request

Code Snippet

```
Sending: < nc: rpc xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " message-id = " urn:uuid:867dd34c-522e-43c5-84ac-47614eb3b2c7 " > < nc: get-config > < nc: source > < nc: running /> </ nc: source > < nc: filter > < native xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-native " > < voice xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-voice " > < class > < codec > < codec-tag > 1 </ codec-tag > < codec > < preference > < preference-tag > 4 </ preference-tag > </ preference > < preference > < preference-tag > 4 </ preference-tag > </ preference > </ codec > </ codec > </ class > </ voice > </ native > </ nc: filter > </ nc: get-config > </ nc: rpc > ##
```

Response

Code Snippet

```
Received: < rpc-reply xmlns = " urn:ietf:params:xml:ns:netconf:base:1.0 " xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " message-id = " urn:uuid:867dd34c-522e-43c5-84ac-47614eb3b2c7 " > < data > < native xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-native " > < voice xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-voice " > < class > < codec > < codec-tag xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " > 1 </ codec-tag > < codec > < preference > < preference-tag xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " > 4 </ preference-tag > < codec-type > ilbc </ codec-type > </ preference > < preference > < preference-tag xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " > 4 </ preference-tag > < codec-type > ilbc </ codec-type > </ preference > </ codec > </ codec > </ class > </ voice > </ native > </ data > </ rpc-reply >
```

Example for edit-config operation:

Request

Code Snippet

```
Sending: < nc: rpc xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " message-id = " urn:uuid:e10e6a15-e091-4215-958a-d15aeac6ac64 " > < nc: edit-config > < nc: target > < nc: running /> </ nc: target > < nc: config > < native xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-native " > < voice xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-voice " > < class > < codec > < codec-tag > 2 </ codec-tag > < codec > < preference > < preference-tag > 1 </ preference-tag > < codec-type > g722-64 </ codec-type > < bytes > 80 </ bytes > </ preference > </ codec > </ codec > </ class > </ voice > </ native > </ nc: config > </ nc: edit-config > </ nc: rpc > ##
```

Response

Code Snippet

```
Received: < rpc-reply xmlns = " urn:ietf:params:xml:ns:netconf:base:1.0 " xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " message-id = " urn:uuid:e10e6a15-e091-4215-958a-d15aeac6ac64 " > < ok /> </ rpc-reply >
```

Next

| Operations | X-path |
|---|---|
| get, get-config, edit-config | /native/ios-voice:voice/ios-voice:class/ios-voice:codec |

| Object | X-path |
|---|---|
| ios-voice:codec | /native/ios-voice:dial-peer/ios-voice:voice/ios-voice:voice-class/ios-voice:codec |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| voice class codec | To set codec global parameters. | /native/ios-voice:dial-peer/ios-voice:voice/ios-voice:voice-class/ios-voice:codec/ios-voice:codectag | codectag, value: 1 to 10000 | N/A | N/A |
| codec preference (value) (codec-type) | To set priority order for using this codec. | /native/ios-voice:voice/ios-voice:class/ios-voice:codec/ios-voice:codec/ios-voice:preference | value: 1 to 24 | N/A | N/A |