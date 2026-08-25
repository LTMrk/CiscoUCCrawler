---
doc_id: developer-cisco-com-docs-ios-xe-voip-sip-dial-peer-configurations-078ec1e336
source_url: https://developer.cisco.com/docs/ios-xe-voip/sip-dial-peer-configurations/
retrieved_at: 2026-08-25T21:02:24.915702+00:00
---

# SIP Dial Peer Configurations

## Newly Added YANG Models in Release Cisco IOS XE 17.14.1a

The following YANG models are supported from Cisco IOS XE 17.14.1a:

- voice-class sip nat media-keepalive interval

- voice-class sip srtp negotiate cisco

- voice-class sip conn-reuse

## Newly Added YANG Models in Release Cisco IOS XE 17.7.1

The following YANG models are supported from Cisco IOS XE 17.7.1:

- audio forced

- assert-id

- asymmetric payload

- block

- call-route

- contact-passing

- codec transparent

- cor custom

- cor list

- destination dpg

- early-offer forced

- local host

- referto-passing

- requri-passing

- rel1xx

- rtp payload-type

- reason-header

- redirection

- ios qos dscp

- max-conn

- media profile recorder

- media profile asp

- media profile nr

- media profile video

- media profile steam service

- notify

- progress_ind

- pass-thru content custom sdp

- signaling forward

- sip-hdr-passthrulist

- sip-event-list

- sip profiles

- sip-copylist

- anat

- answer-address

- early-media update block

- error-code override

- outbound-proxy

- update-callerid

- url

- voice-class stun-usage

- voice class uri

- voice class e164 pattern-map

- voice class sip-options keepalive

- voice class server group

- voice class media

## Dial-Peer Voice Configurations

You can perform the SIP dial-peer configuration, using the dial-peer voice (tag) voip configuration mode.  The dial-peer voice (tag) voip configuration mode is a part of Cisco-IOS-XE-voice module. The following operations are allowed in the dial-peer voice (tag) voip configuration mode.

### Select VoIP Service Configuration Mode

To enter into the dial-peer voice (tag) voip configuration mode, follow the x-path provided in the below table.

### Prerequisites for dial-peer voice (tag) voip configuration

The dialpeertag field is the KEY for dial-peer voice (tag) voip configuration. This is a mandatory field to configure other SIP services at dial-peer level.

### Configuration Recommendations

- The dial-peer (tag) value must not overlap with the dynamic dial-peer range.

- The dial-peer (tag) range: 1 to 1073741823

- It is mandatory to configure session protocol sipv2.

- The dtmf-relay configuration allows only to enable the DTMF types.

The dial-peer voice (tag) voip configuration mode allows you to perform the following SIP dial-peer configurations.

### Basic SIP Dial-Peer Configurations and X-path details

#### Voice Class SIP Configurations

#### Voice SIP-Register Configurations

#### Voice Class Stun Usage Configurations

## Dial-Peer COR Configurations

The following operations are allowed in the dial-peer COR configuration mode:

### Select COR Configuration Mode

To enter into the COR configuration mode, follow the x-path provided in the below table.

### Prerequisites for Dial-Peer COR Configuration

dial-peer cor list member is dependent on dial-peer cor custom name . Hence, member created under dial-peer cor list should be the same as name created under dial-peer cor custom .

### Configuration Recommendations

- You need to configure "name" of type string under "dial-peer cor custom" before configuring "dial-peer cor list".

- list_name under dial-peer cor list must follow the [0-9,A-Z,a-z-]*T? pattern.

- Configure "member" under "dial-peer cor list" after you configure "name" under "dial-peer cor custom".

### COR Dial-Peer Configurations and X-Path details

#### Examples: SIP Dial-Peer Configurations

Following are the examples for SIP Dial-Peer Configurations.

Example for get-config operation:

Request

Code Snippet

```
Sending: < nc: rpc xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " message-id = " urn:uuid:7b2fccdd-db09-4e09-b485-8b04e4b6a806 " > < nc: get-config > < nc: source > < nc: running /> </ nc: source > < nc: filter > < native xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-native " > < dial-peer xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-voice " /> </ native > </ nc: filter > </ nc: get-config > </ nc: rpc > ##
```

Response

Code Snippet

```
Received: < rpc-reply xmlns = " urn:ietf:params:xml:ns:netconf:base:1.0 " xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " message-id = " urn:uuid:7b2fccdd-db09-4e09-b485-8b04e4b6a806 " > < data > < native xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-native " > < dial-peer xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-voice " > < voice > < dialpeertag > 11 </ dialpeertag > < type > voip </ type > < incoming > < called-number > 1002 </ called-number > </ incoming > < session > < transport > < tcp /> </ transport > < protocol > sipv2 </ protocol > </ session > </ voice > < voice > < dialpeertag > 12 </ dialpeertag > < type > voip </ type > < destination-pattern > 1002 </ destination-pattern > < session > < transport > < tcp /> </ transport > < protocol > sipv2 </ protocol > < target > < address > ipv4:10.77.91.212 </ address > </ target > </ session > </ voice > < voice > < dialpeertag > 1000 </ dialpeertag > < type > voip </ type > < session > < protocol > sipv2 </ protocol > </ session > </ voice > </ dial-peer > </ native > </ data > </ rpc-reply >
```

Example for edit-config operation:

Request

Code Snippet

```
Sending: < nc: rpc xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " message-id = " urn:uuid:9252a862-55d8-4d4a-8de8-ada770eeba2e " > < nc: edit-config > < nc: target > < nc: running /> </ nc: target > < nc: config > < native xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-native " > < dial-peer xmlns = " http://cisco.com/ns/yang/Cisco-IOS-XE-voice " > < voice > < dialpeertag > 11 </ dialpeertag > < type > voip </ type > < description > test description </ description > < incoming > < called-number > 1223 </ called-number > </ incoming > </ voice > </ dial-peer > </ native > </ nc: config > </ nc: edit-config > </ nc: rpc > ##
```

Response

Code Snippet

```
Received: < rpc-reply xmlns = " urn:ietf:params:xml:ns:netconf:base:1.0 " xmlns: nc = " urn:ietf:params:xml:ns:netconf:base:1.0 " message-id = " urn:uuid:9252a862-55d8-4d4a-8de8-ada770eeba2e " > < ok /> </ rpc-reply >
```

Next

| Operations | X-path |
|---|---|
| get, get-config, edit-config | /native/ios-voice:dial-peer/ios-voice:voice/ios-voice:dialpeertag |

| Object | X-path |
|---|---|
| dial-peer voice (tag) voip | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="100"]/ios-voice:type="voip" |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| corlist incoming | To set the incoming class of restriction lists. | /native/ios-voice:dial-peer/ios-voice:voice/ios-voice:corlist/ios-voice:incoming | WORD incoming Class of Restriction list name | Configure "dial-peer cor list name" before configuring this. | N/A |
| corlist outgoing | To set the outgoing class of restriction lists. | /native/ios-voice:dial-peer/ios-voice:voice/ios-voice:corlist/ios-voice:outgoing | WORD outgoing Class of Restriction list name | Configure "dial-peer cor list name" before configuring this. | N/A |
| description | To add a description to a dial peer, in dial peer configuration mode. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="100"]/ios-voice:description | string, up to 64 alphanumeric characters. | N/A | N/A |
| destination dpg | To add a voice class dpg that is used as the destnation of an inbound dial peer. | /native/ios-voice:dial-peer/ios-voice:voice/ios-voice:destination/ios-voice:dpg | tag (Min 1, Max 10000) | N/A | N/A |
| destination-pattern | To specify either the prefix or the full E.164 telephone number to be used for a dial peer. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="100"]/ios-voice:destination-pattern | N/A | N/A | E164 pattern only. |
| incoming called-number | To specify a digit string that can be matched by an incoming call to associate the call with a dial peer. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="1"]/ios-voice:incoming/ios-voice:called-number | N/A | N/A | N/A |
| incoming called e164-pattern-map | To configure voice class to match incoming destination e164-pattern-map. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="100"]/ios-voice:incoming/ios-voice:called-number/ios-voice:e164-pattern-map | Min-1, Max-10000 | N/A | N/A |
| incoming calling e164-pattern-map | To configure voice class to match incoming destination e164-pattern-map. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="1"]/ios-voice:incoming/ios-voice:calling/ios-voice:e164-pattern-map | Min-1, Max-10000 | N/A | N/A |
| incoming uri from | To match incoming to header. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="1"]/ios-voice:incoming/ios-voice:uri/ios-voice:from | N/A | Session Protocol sipv2(under dial-peer voice voip) must be configured. | N/A |
| incoming uri request | To match incoming request-URI. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="1"]/ios-voice:incoming/ios-voice:uri/ios-voice:request | N/A | Session Protocol sipv2(under dial-peer voice voip) must be configured. | N/A |
| incoming uri to | To match incoming to header. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="1"]/ios-voice:incoming/ios-voice:uri/ios-voice:via | N/A | Session Protocol sipv2(under dial-peer voice voip) must be configured. | N/A |
| incoming uri via | To match incoming topmost Via header. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="1"]/ios-voice:incoming/ios-voice:uri/ios-voice:to | N/A | Session Protocol sipv2(under dial-peer voice voip) must be configured. | N/A |
| vad | To enable voice activity detection for calls using a particular dial peer. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:vad | N/A | Dial peer must be of "voip" type. | N/A |
| vad aggressive | To enable aggressive voice activity detection for calls using a particular dial peer. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:vad/iosvoice:aggressive | N/A | Session protocol must be of "multicast" type. | N/A |
| destination | To configure to match Outbound dial-peer. | /native/ios-voice:dialpeer/ios-voice:voice[iosvoice:dialpeertag="1"]/iosvoice:destination | N/A | N/A | N/A |
| destination calling e164-pattern-map | To configure voice class to match destination e164-pattern-map. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="1"]/ios-voice:destination/ios-voice:calling/ios-voice:e164-pattern-map | Min-1, Max-1000 | N/A | N/A |
| destination e164-pattern-map | To configure voice class to match destination e164-pattern-map. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="1"]/ios-voice:destination/ios-voice:e164-pattern-map | Min-1, Max-1000 | N/A | N/A |
| uri | To configure voice class to match destination URI. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="1"]/ios-voice:destination/ios-voice:uri | N/A | Session Protocol sipv2(under dial-peer voice voip) must be configured. | N/A |
| uri-diversion | To configure voice class uri to match sip diversion header. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="1"]/ios-voice:destination/ios-voice:uri-diversion | N/A | Session Protocol sipv2(under dial-peer voice voip) must be configured. | N/A |
| uri-from | To configure voice class uri to match sip from header. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="1"]/ios-voice:destination/ios-voice:uri-from | N/A | Session Protocol sipv2(under dial-peer voice voip) must be configured. | N/A |
| uri-to | To configure voice class uri to match sip to header. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="1"]/ios-voice:destination/ios-voice:uri-to | N/A | Session Protocol sipv2(under dial-peer voice voip) must be configured. | N/A |
| uri-via | To configure voice class uri to match sip via header. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="1"]/ios-voice:destination/ios-voice:uri-via | N/A | Session Protocol sipv2(under dial-peer voice voip) must be configured. | N/A |
| rtp payloadtype ciscocodec-aacld | To configure Cisco codec AACLD as a supported payload type within the range. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:rtp/ios-voice:payloadtype/ios-voice:cisco-codecaacld | Range: 96-127 | N/A | Default value is 112. |
| rtp payloadtype ciscocodec-ilbc | To configure Cisco codec iLBC as a supported payload type within the range. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:rtp/ios-voice:payloadtype/ios-voice:cisco-codecilbc | Range: 96-127 | N/A | Default value is 116. |
| rtp payloadtype ciscocodec-isac | To configure Cisco codec ISAC as a supported payload type within the range. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:rtp/ios-voice:payloadtype/ios-voice:cisco-codecisac | Range: 96-127 | N/A | Default value is 124. |
| rtp payloadtype ciscocodecmp4a-latm | To configure Cisco codec MP4A-LATM as a supported payload type within the range. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:rtp/ios-voice:payloadtype/ios-voice:cisco-codecmp4a-latm | Range: 96-127 | N/A | Default value is 111. |
| rtp payloadtype ciscocodecvideo-h263-plus | To configure RTP video codec H263+ payload type within the range. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:rtp/ios-voice:payloadtype/ios-voice:cisco-codecvideo-h263-plus | Range: 96-127 | N/A | Default value is 118. |
| rtp payloadtype ciscocodecvideo-h264 | To configure RTP video codec H264 payload type within the range. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:rtp/ios-voice:payloadtype/ios-voice:cisco-codecvideo-h264 | Range: 96-127 | N/A | Default value is 119. |
| rtp payloadtype nse | To configure Named Signalling Event within the range. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:rtp/ios-voice:payloadtype/ios-voice:nse | Range: 96-127 | N/A | Default value is 100. |
| rtp payloadtype opus | To configure opus as a supported payload type within the range. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:rtp/ios-voice:payloadtype/ios-voice:opus | Range: 96-127 | N/A | Default value is 114. |
| rtp payloadtype nte | To configure Named Telephone Event as a supported payload type within the range. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:rtp/ios-voice:payloadtype/ios-voice:nte | Range: 96-127 | N/A | Default value is 101. |
| rtp payload-type codec-audio-scip | To configure scip audio codec as a supported payload type within the range. (The SCIP feature in Cisco IOS XE 17.16.1a release is available in 'preview’ mode as it includes limited functionality or incomplete software dependencies). | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:rtp/ios-voice:payload-type/ios-voice:codec-audio-scip | Range: 96-127 | N/A | Default value is 109. |
| rtp payload-type codec-video-scip | To configure scip video codec as a supported payload type within the range. (The SCIP feature in Cisco IOS XE 17.16.1a release is available in 'preview’ mode as it includes limited functionality or incomplete software dependencies). | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:rtp/ios-voice:payload-type/ios-voice:codec-video-scip | Range: 96-127 | N/A | Default value is 110. |
| ip qos dscpmedia dscp | To specify the IP Differentiated Services Code Point (DSCP) for media. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:ip/ios-voice:qos/iosvoice:dscp-media/iosvoice:dscp | 0-63, af11, af12, af13, af21, af22, af23, af31, af32, af33, af41, af42, af43, cs1, cs2, cs3, cs4, cs5, cs6, cs7, default, ef | N/A | N/A |
| ip qos dscpmedia media | To apply DSCP to media payload packets. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:ip/ios-voice:qos/iosvoice:dscp-media/iosvoice:media | N/A | N/A | N/A |
| ip qos dscp-signaling dscp | To specify the IP DSCP for signaling. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:ip/ios-voice:qos/iosvoice:dscp-signaling/iosvoice:signaling | 0-63, af11, af12, af13, af21, af22, af23, af31, af32, af33, af41, af42, af43, cs1, cs2, cs3, cs4, cs5, cs6, cs7, default, ef | N/A | N/A |
| ip qos dscp-video dscp | To specify the IP DSCP for video. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:ip/ios-voice:qos/iosvoice:dscp-video/iosvoice:dscp | 0-63, af11, af12, af13, af21, af22, af23, af31, af32, af33, af41, af42, af43, cs1, cs2, cs3, cs4, cs5, cs6, cs7, default, ef | N/A | N/A |
| ip qos dscp-video video rsvp-none | To use this DSCP value if RSVP is not configured. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:ip/ios-voice:qos/iosvoice:dscp-video/iosvoice:video/ios-voice:rsvpnone | N/A | N/A | N/A |
| max-conn range | To set the maximum connections per peer, negation sets to unlimited. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:max-conn/iosvoice:range | Min 1, Max 2147483647 | N/A | N/A |
| max-conn exempt-local-media | To exempt local media calls from max-conn value update. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:max-conn/iosvoice:exempt-local-media | N/A | N/A | N/A |
| progress_ind alert disable | To disable Progress Indicator for ALERT. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:progress_ind/iosvoice:alert/ios-voice:disable | N/A | To configure progress_ind, you need to configure destination-pattern on the dial peer. | N/A |
| progress_ind alert enable | To enable Progress Indicator for ALERT. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice: progress_ind/iosvoice:alert/ios-voice:enable | N/A | N/A | N/A |
| progress_ind alert strip value | To specify a value for Progress Indicator. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:progress_ind/iosvoice:alert/iosvoice:strip/ios-voice:value | 1, 2, or 8 | N/A | N/A |
| progress_ind callproc disable | To disable Progress Indicator for CALLPROC. | /native/ios-voice:dialpeer/ ios-voice:voice/iosvoice:progress_ind/iosvoice:callproc/iosvoice:disable | N/A | N/A | N/A |
| progress_ind callproc enable | To enable Progress Indicator for CALLPROC. | /native/ios-voice:dialpeer/ ios-voice:voice/iosvoice:progress_ind/iosvoice:callproc/iosvoice:enable | 1, 2, or 8 | N/A | N/A |
| progress_ind callproc strip value | To specify a value for Progress Indicator. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:progress_ind/iosvoice:callproc/iosvoice:strip/ios-voice:value | 1, 2, or 8 | N/A | N/A |
| progress_ind connect disable | To disable Progress Indicator for CONNECT. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:progress_ind/iosvoice:connect/iosvoice:disable | N/A | N/A | N/A |
| progress_ind connect enable | To enable Progress Indicator for CONNECT. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:progress_ind/iosvoice:connect/iosvoice:enable | 1, 2, or 8 | N/A | N/A |
| progress_ind progress disable | To disable Progress Indicator for PROGRESS. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:progress_ind/iosvoice:progress | N/A | N/A | N/A |
| progress_ind progress enable | To enable Progress Indicator for PROGRESS. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:progress_ind/iosvoice:progress/iosvoice:enable | N/A | N/A | N/A |
| progress_ind disconnect disable | To disable Progress Indicator for DISCONNECT. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:progress_ind/iosvoice:disconnect/iosvoice:disable | N/A | N/A | N/A |
| progress_ind disconnect enable | To enable Progress Indicator for DISCONNECT. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:progress_ind/iosvoice:disconnect/iosvoice:enable | N/A | N/A | N/A |
| progress_ind setup disable | To disable Progress Indicator for SETUP. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:progress_ind/iosvoice:setup/ios-voice:disable | N/A | N/A | N/A |
| progress_ind setup enable | To enable Progress Indicator for SETUP. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:progress_ind/iosvoice:setup/ios-voice:enable | N/A | N/A | N/A |
| answer-address | Uses the calling number to match the incoming call leg to an inbound dial peer. | /native/ios-voice:dialpeer/ios-voice:voice/iosvoice:answer-address | A string of digits including wild cards. | N/A | N/A |
| e164-pattern-map | To configure voice class to match destination e164-pattern-map. | /native/ios-voice:dialpeer/ios-voice:voice[iosvoice:dialpeertag="1"]/iosvoice:destination/iosvoice:calling/ios-voice:e164-pattern-map | N/A | N/A | N/A |
| uri | To configure voice class to match destination URI. | /native/ios-voice:dialpeer/ios-voice:voice[iosvoice:dialpeertag="1"]/iosvoice:destination/iosvoice:uri | N/A | N/A | N/A |
| uri-diversion | To configure voice class uri to match sip diversion header. | /native/ios-voice:dialpeer/ios-voice:voice[iosvoice:dialpeertag="1"]/iosvoice:destination/iosvoice:uri-diversion | N/A | N/A | N/A |
| uri-from | To configure voice class uri to match sip from header. | /native/ios-voice:dialpeer/ios-voice:voice[iosvoice:dialpeertag="1"]/iosvoice:destination/iosvoice:uri-from | N/A | N/A | N/A |
| uri-to | To configure voice class uri to match sip to header. | /native/ios-voice:dialpeer/ios-voice:voice[iosvoice:dialpeertag="1"]/iosvoice:destination/iosvoice:uri-to | N/A | N/A | N/A |
| uri-via | To configure voice class uri to match sip via header. | /native/ios-voice:dialpeer/ios-voice:voice[iosvoice:dialpeertag="1"]/iosvoice:destination/iosvoice:uri-via | N/A | N/A | N/A |
| media-recording | To configure voice class recording parameters. | /native/ios-voice:dial-peer/ios-voice:voice/ios-voice:media-recording/ios-voice:dialpeertag | dial-peer-tag, value: 1 to 1073741823 | N/A | N/A |
| session protocol | To specify a session protocol for calls between local and remote routers using the packet network. | /native/ios-voice:dial-peer/ios-voice:voice/ios-voice:session/ios-voice:protocol | sipv2 | N/A | This is a mandatory configuration. |
| session server-group | To configure voice class server-group. | /native/ios-voice:dial-peer/ios-voice:voice/ios-voice:session/ios-voice:server-group | tag (Min 1, Max 10000) | "voice class server-group tag" should be configured first before associating it here. To perform sever-group configuration under dial-peer, you need to configure sipv2 session protocol first | N/A |
| signaling forward | To enable Signaling payload handling | /native/ios-voice:dial-peer/ios-voice:voice/ios-voice:signaling/ios-voice:forward | conditional, none, rawmsg, unconditional | N/A | N/A |
| session target | To designate a session target for this peer. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="100"]/ios-voice:session/ios-voice:target | address (string), dhcp, registrar | N/A | Pattern to follow for address string is "(loopback:rtp)(dns:. ) (sip-server)(sip-uri)(ipv4:[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+(:[0-9]+)?)(ipv6:\(([0-9A-Fa-f:])+\)(:[0-9]+)?)" |
| huntstop | To enable or disable all dial-peer hunting. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="100"]/ios-voice:huntstop | true, false | N/A | Default: false |
| preference | To configure the preferred order of a dial peer. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="100"]/ios-voice:preference | Min-0, Max-10 | N/A | You can configure digit-drop only when the rtp-nte option is selected. |
| dtmf-relay | To configure transport digits across IP link. Enter relay options in order of preference. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="100"]/ios-voice:dtmf-relay | rtp-nte (digit-drop), sip-info, sip-kpml, sip-notify | N/A | You can configure digit-drop only when the rtp-nte option is selected. |
| translation-profile (incoming, outgoing) | To assign a translation profile to a dial peer. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="100"]/ios-voice:translation-profile | incoming, outgoing | N/A | N/A |
| media | To set media parameters for call. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="12"]/ios-voice:voice-class/ios-voice:media | N/A | N/A | N/A |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| voice-class sip bind (control) | To bind Session Initiation Protocol (SIP) signaling packets. | /native/ios-voice:dial-peer/ios-voice:voice/ios-voice:voice-class/ios-voice:sip/ios-voice:bind/ios-voice:control | source-interface (interface-id) | N/A | For the source-interface-std , select the interface to configure from the interface-choice list. |
| voice-class sip bind (media) | To bind Session Initiation Protocol (SIP) media packets. | /native/ios-voice:dial-peer/ios-voice:voice/ios-voice:voice-class/ios-voice:sip/ios-voice:bind/ios-voice:media | source-interface (interface-id) | N/A | For the source-interface-std , select the interface to configure from the interface-choice list. |
| voice-class sip options-keepalive profile | To set up consolidated OPTIONS keepalive profile | /native/ios-voice:dial-peer/ios-voice:voice/ios-voice:voice-class/ios-voice:sip/ios-voice:options-keepalive/ios-voice:profile | Profile tag (Min 1, Max 10000) | "voice class sip-options-keepalive" should be configured first | N/A |
| pass-thru content (custom SDP) | To configure pass-through custom SDP using SIP profiles. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="2"]/ios-voice:voice-class/ios-voice:sip/ios-voice:pass-thru/ios-voice:content/ios-voice:custom-sdp | N/A | N/A | N/A |
| pass-thru content (SDP mode non-rtp) | To configure pass-through sdp mode to non-rtp. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="2"]/ios-voice:voice-class/ios-voice:sip/ios-voice:pass-thru/ios-voice:content/ios-voice:sdp/ios-voice:mode/ios-voice:non-rtp | N/A | N/A | N/A |
| pass-thru content (unsupp) | To configure pass-through all unsupported content. | /native/ios-voice:dialpeer/ios-voice:voice/ios-voice:voiceclass/ios-voice:sip/ios-voice:passthru/ios-voice:content/ios-voice:unsupp | N/A | N/A | N/A |
| pass-thru headers | To configure the passthrough of a list of headers from a globally configured list. | /native/ios-voice:dialpeer/ios-voice:voice/ios-voice:voice-class/ios-voice:sip/ios-voice:passthru/ios-voice:headers | N/A | N/A | N/A |
| pass-thru headers (unsupp) | To configure pass-through all unsupported headers. | /native/ios-voice:dialpeer/ios-voice:voice/ios-voice:voice-class/ios-voice:sip/ios-voice:passthru/ios-voice:headers/ios-voice:unsupp | N/A | N/A | N/A |
| pass-thru subscribe-notify-events | To configure subscribe/notify event passthrough. | /native/ios-voice:dialpeer/ios-voice:voice/ios-voice:voiceclass/ios-voice:sip/ios-voice:passthru/ios-voice:subscribe-notify-events | N/A | N/A | N/A |
| pass-thru sip-event-list-all | To configure pass-through all subscribe/notify events. | /native/ios-voice:dialpeer/ios-voice:voice/ios-voice:voice-class/ios-voice:sip/ios-voice:passthru/ios-voice:subscribe-notify-events/ios-voice:all | N/A | N/A | N/A |
| voice-class sip tenant | To configure SIP-Tenant parameters. | /native/ios-voice:dial-peer/ios-voice:voice/ios-voice:voice-class/ios-voice:sip/ios-voice:tenant | N/A | N/A | N/A |
| voice-class-media | To set media parameters for call. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="12"]/ios-voice:voice-class/ios-voice:media | N/A | N/A | N/A |
| pai | To use privacy asserted identity. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="1"]/ios-voice:voice-class/ios-voice:sip/ios-voice:asserted-id/ios-voice:pai | N/A | N/A | N/A |
| ppi | To use privacy preferred identity. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="1"]/ios-voice:voice-class/ios-voice:sip/ios-voice:asserted-id/ios-voice:ppi | N/A | N/A | N/A |
| block | To block all SIP messages in midcall. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="1"]/ios-voice:voice-class/ios-voice:sip/ios-voice:midcall-signaling/ios-voice:block | N/A | N/A | N/A |
| media-change | To only passthrough SIP messages which involve media-change. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="1"]/ios-voice:voice-class/ios-voice:sip/ios-voice:midcall-signaling/ios-voice:passthru/ios-voice:media-change | N/A | N/A | N/A |
| preserve-codec | To preserve initial negotiated codec i.e. midcall codec change denial. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="1"]/ios-voice:voice-class/ios-voice:sip/ios-voice:midcall-signaling/ios-voice:preserve-codec | N/A | N/A | N/A |
| always | To enable end-to-end re-negotiation for all codecs. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="1"]/ios-voice:voice-class/ios-voice:sip/ios-voice:early-offer/ios-voice:forced/ios-voice:re-negotiate/ios-voice:always | N/A | N/A | N/A |
| dtmf | To configure asymmetric support for dtmf payloads only. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="1"]/ios-voice:voice-class/ios-voice:sip/ios-voice:asymmetric/ios-voice:payload/ios-voice:dtmf | N/A | N/A | N/A |
| dynamic-codecs | To configure asymmetric support for dynamic codec payloads only. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="1"]/ios-voice:voice-class/ios-voice:sip/ios-voice:asymmetric/ios-voice:payload/ios-voice:dynamic-codecs | N/A | N/A | N/A |
| full | To configure asymmetric support for dynamic codec and dtmf payloads. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="1"]/ios-voice:voice-class/ios-voice:sip/ios-voice:asymmetric/ios-voice:payload/ios-voice:full | N/A | N/A | N/A |
| rel1xx (disable/require/supported) | To enable all Session Initiation Protocol (SIP) provisional responses (other than 100 Trying) to be sent reliably to the remote SIP endpoint. | /native/ios-voice:dial-peer/ios-voice:voice/ios-voice:voice-class/ios-voice:sip/ios-voice:rel1xx | disable/require/supported | N/A | N/A |
| anat | To allow alternative network address types IPv4 and IPv6. | /native/ios-voice:dialpeer/ios-voice:voice/ios-voice:voice-class/ios-voice:sip/ios-voice:anat | true, false | N/A | Deafult value is false. |
| early media update block | To consume the SIP UPDATE requests with SDP received during an early dialog. | /native/ios-voice:dial-peer/ios-voice:voice/ios-voice:voice-class/ios-voice:sip/ios-voice:early-media/ios-voice:update/ios-voice:block | N/A | sip to sip allow connections should be enabled under "voice service voip". | N/A |
| early media update block re-negotiate | To renegotiate the call if the UPDATE request contains changes in caller ID, transcoder addition or deletion, or video escalation or de-escalation. | /native/ios-voice:dial-peer/ios-voice:voice/ios-voice:voice-class/ios-voice:sip/ios-voice:early-media/ios-voice:update/ios-voice:block/ios-voice:re-negotiate | N/A | sip to sip allow connections should be enabled under "voice service voip". | N/A |
| error-code-override cac-bandwidth failure | To configure SIP error code for CAC bandwidth failures. | /native/ios-voice:dialpeer/ios-voice:voice/ios-voice:voice-class/ios-voice:sip/ios-voice:error-code-override/ios-voice:cac-bandwidth/ios-voice:failure | N/A | N/A | N/A |
| error-code-override call spike failure | To configure SIP error code for CAC bandwidth failures. | /native/ios-voice:dialpeer/ios-voice:voice/ios-voice:voice-class/ios-voice:sip/ios-voice:error-code-override/ios-voice:cac-bandwidth/ios-voice:failure | N/A | N/A | N/A |
| error-code-override cpu failure | To configure SIP error code for CPU failures. | /native/ios-voice:dialpeer/ios-voice:voice/ios-voice:voice-class/ios-voice:sip/ios-voice:error-code-override/ios-voice:cpu/ios-voice:failure | N/A | N/A | N/A |
| error-code-override max-conn failure | To configure SIP error code for maximum number of simultaneous connection failures. | /native/iosvoice:dialpeer/ios-voice:voice/ios-voice:voice-class/ios-voice:sip/ios-voice:error-code-override/ios-voice:maxconn/ios-voice:failure | N/A | N/A | N/A |
| error-code-override mem failure | To configure SIP error code for memory failures. | /native/iosvoice:dialpeer/ios-voice:voice/ios-voice:voice-class/ios-voice:sip/ios-voice:error-code-override/ios-voice:mem/ios-voice:failure | N/A | N/A | N/A |
| error-code-override options-keepalive failure | To configure SIP error code for option keepalive failures. | /native/ios-voice:dial-peer/ios-voice:voice/ios-voice:voice-class/ios-voice:sip/ios-voice:error-code-override/ios-voice:options-keepalive/ios-voice:failure | N/A | N/A | N/A |
| error-code-override sip-shutdown failure | To configure SIP error code for SIP shutdown failures. | /native/ios-voice:dial-peer/ios-voice:voice/ios-voice:voice-class/ios-voice:sip/ios-voice:error-code-override/ios-voice:sip-shutdown/ios-voice:failure | N/A | N/A | N/A |
| error-code-override total-calls failure | To configure SIP error code for total call failures. | /native/ios-voice:dial-peer/ios-voice:voice/ios-voice:voice-class/ios-voice:sip/ios-voice:error-code-override/ios-voice:total-calls/ios-voice:failure | N/A | N/A | N/A |
| nat-config | To configure global SIP NAT. | /native/ios-voice:dial-peer/ios-voice:voice/ios-voice:voice-class/ios-voice:sip/ios-voice:nat-config | N/A | N/A | N/A |
| force-on | To configure all remote subscribers behind NAT device. | /native/ios-voice:dial-peer/ios-voice:voice/ios-voice:voice-class/ios-voice:sip/ios-voice:nat-config/ios-voice:force-on | N/A | N/A | N/A |
| auto | To configure subscriber as auto detect in a remote subnet behind a NAT. | /native/ios-voice:dial-peer/ios-voice:voice/ios-voice:voice-class/ios-voice:sip/ios-voice:nat-config/ios-voice:auto | N/A | N/A | N/A |
| media-keepalive | To configure Media keepalive messages to peer subscribers located outside NAT. | /native/ios-voice:dial-peer/ios-voice:voice/ios-voice:voice-class/ios-voice:sip/ios-voice:nat-config/ios-voice:media-keepalive | 10 | N/A | N/A |
| interval | To configure configure Keepalive interval. | /native/ios-voice:dial-peer/ios-voice:voice/ios-voice:voice-class/ios-voice:sip/ios-voice:nat-config/ios-voice:media-keepalive/ios-voice:interval | 1—50 | N/A | N/A |
| srtp | To allow SIP related SRTP options. | /native/ios-voice:dial-peer/ios-voice:voice/ios-voice:voice-class/ios-voice:sip/ios-voice:srtp | N/A | N/A | N/A |
| negotiate | To configure SRTP negotiate options. | /native/ios-voice:dial-peer/ios-voice:voice/ios-voice:voice-class/ios-voice:sip/ios-voice:srtp/ios-voice:negotiate | N/A | N/A | N/A |
| cisco | To allow RTP answer to SRTP offer. | /native/ios-voice:dial-peer/ios-voice:voice/ios-voice:voice-class/ios-voice:sip/ios-voice:srtp/ios-voice:negotiate/ios-voice:cisco | N/A | N/A | N/A |
| conn-reuse | To reuse the TCP connection of a SIP registration for an endpoint behind a firewall. | //native/ios-voice:dial-peer/ios-voice:voice/ios-voice:voice-class/ios-voice:sip/ios-voice:conn-reuse | N/A | N/A | N/A |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| dp-monitor-tag | To configure the dialpeer monitor tag for registration sync. | /native/ios-voice:dial-peer/ios-voice:voice[ios-voice:dialpeertag="1"]/ios-voice:sip-register/ios-voice:reg-sync/ios-voice:dp-monitor-tag | tag (Min 1, Max 	1073741823) | N/A | N/A |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| voice-class stun usage | To set stun usage global parameters. | /native/ios-voice:dial-peer/ios-voice:voice/ios-voice:voice-class/ios-voice:stun-usage | tag (Min 1, Max 10000) | N/A | N/A |

| Operations | X-path |
|---|---|
| get, get-config, edit-config | /native/ios-voice:dial-peer/ios-voice:cor |

| Object | X-path |
|---|---|
| dial-peer voice cor | /native/ios-voice:dial-peer/ios-voice:cor |

| Object | Description | X-path | Value | Prerequisites | Remarks |
|---|---|---|---|---|---|
| cor custom name | To define a name for custom class of restrictions that apply to dial peers. | /native/ios-voice:dial-peer/ios-voice:cor/ios-voice:custom/ios-voice:name | String | N/A | You can create a maximum of 64 names. |
| cor list | To define a list of class of restrictions that apply to dial peers. | /native/ios-voice:dial-peer/ios-voice:cor/ios-voice:list | String | N/A | You can create a maximum of 64 lists. |
| cor list member | To a define a member added to the class of restrictions list. | /native/ios-voice:dial-peer/ios-voice:cor/ios-voice:list/ios-voice:member | N/A | N/A | You can create a maximum of 64 members. |