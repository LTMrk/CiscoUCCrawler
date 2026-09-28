---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-vd-mdp-dialpeer-html-d7db365144
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_vd-mdp-dialpeer.html
retrieved_at: 2026-08-16T15:45:47.067854+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Multiple Pattern Support on a Voice Dial Peer

## Chapter: Multiple Pattern Support on a Voice Dial Peer

# Multiple Pattern Support on a Voice Dial Peer

## Overview

The Multiple Pattern
                           		Support on a Voice Dial Peer feature enables you to configure multiple patterns
                           		on a VoIP dial peer using an E.164 pattern map. A dial peer can be configured
                           		to match multiple patterns to an incoming calling or called number or an
                           		outgoing destination number.

Matching an incoming or outgoing call using a pattern defined in a VoIP dial peer is an existing feature on the Cisco Unified
                           Border Element (Enterprise) and Session Initiation Protocol (SIP) Gateway. You can now support multiple patterns on a VoIP
                           dial peer using an E.164 pattern map. You can create an E.164 pattern map and then link it to one or more VoIP dial peers.

When a pattern is the only source to enable a dial peer, a valid E.164 pattern map enables the linked dial peers, whereas
                           an invalid E.164 pattern map disables the linked dial peers. Additionally, whenever an E.164 pattern map is created or reloaded,
                           one or more dial peers linked with an E.164 pattern map is enabled or disabled based on the validation of a pattern map.

You can match a pattern map to an incoming calling or called number or an outgoing destination number.

When a dial peer has multiple patterns, the pattern with the longest prefix is considered as the matching criteria.

### Feature Information for
                           	 Multiple Pattern Support on a Voice Dial Peer

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature
                                          				  Information

Configuring
                                          				  Multiple Pattern Support on a Voice Dial Peer (Inbound Calls)

Cisco IOS
                                          				  15.4 (1)T

Cisco IOS XE 3.11S

This feature
                                          				  was extended for inbound VoIP dial peers for incoming calling and called
                                          				  numbers.

The following
                                          				  commands were introduced or modified: incoming called
                                                						e164-pattern-map , incoming calling
                                                						e164-pattern-map

Configuring
                                          				  Multiple Pattern Support on a Voice Dial Peer (Outbound Calls)

Cisco IOS
                                          				  15.2(4)M

Cisco IOS XE 3.7S

This feature
                                          				  allows you to add more than one E.164 destination pattern inside a pattern map
                                          				  and configure that pattern map for one or more VoIP dial peers.

This feature
                                          				  is supported for outbound peers only.

The following
                                          				  commands were introduced or modified: destination
                                                						e164-pattern-map , e164 , show voice class
                                                						e164-pattern-map , url , voice class e164-pattern-map
                                                						load , voice class
                                                						e164-pattern-map .

## Restrictions for Multiple
                        	 Pattern Support on a Voice Dial Peer

This feature is
                                    				supported only on a VoIP dial peer.

Duplicate
                                    				patterns cannot be added to a pattern map.

## Configure Multiple Pattern Support

### SUMMARY STEPS

- enable

- configure terminal

- voice class e164-pattern-map pattern-map-id

- Do one of the
                              			 following:

- e164 pattern-map-tag

- url url

- (Optional) description string

- exit

- dial-peer voice dial-peer-id voip

- { destination | incoming
                                    				  called | incoming calling } e164-pattern-map pattern-map-group-id

- end

- (Optional) voice class e164-pattern-map load pattern-map-group-id

- show dial-peer
                                    				  voice [ summary | dial-peer-id ]

### DETAILED STEPS

Step 1

enable

### Example:

```
Device> enable
```

Enters
                                          				privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Device# configure terminal
```

Enters global
                                          				configuration mode.

Step 3

voice class e164-pattern-map pattern-map-id

### Example:

```
Device(config)# voice class e164-pattern-map 1111
```

Creates a
                                          				pattern map for configuring one or multiple E.164 patterns on a dial peer and
                                          				enters voice class configuration mode.

The prefix + sign is stripped during .T destination pattern selection. However, configuring an unrelated or empty E.164 pattern
                                                      in the same dial-peer as the .T pattern will not strip + sign.

Step 4

Do one of the
                                       			 following:

- e164 pattern-map-tag

- url url

### Example:

Using URL text
                                          				file:

```
Device(voice-class)# url http://http-host/config-files/pattern-map.cfg
```

Directly
                                          				specifying match patterns:

```
Device(voice-class)# e164 5557123
```

Configure one
                                          				or more E.164 telephone number prefix match patterns for the pattern map.

Repeat
                                                					 this step for each pattern if you are using the e164 command.

You can
                                                					 specify a file URL containing the patterns for this dial peer using the url url command.
                                                					 You must then load the E.164 telephone prefixes using Step 10. The file can be
                                                					 internal (on the device) or external.

Step 5

(Optional) description string

### Example:

```
Device(voice-class)# description It has 1 entry
```

Provides a
                                          				description for the pattern map.

Step 6

exit

### Example:

```
Device(voice-class)# exit
```

Exits voice
                                          				class configuration mode and enters global configuration mode.

Step 7

dial-peer voice dial-peer-id voip

### Example:

```
Device(config)# dial-peer voice 2222 voip
```

Defines a VoIP
                                          				dial peer and enters dial peer configuration mode.

Step 8

{ destination | incoming
                                             				  called | incoming calling } e164-pattern-map pattern-map-group-id

### Example:

```
Device(config-dial-peer)# incoming calling e164-pattern-map 1111
```

Links a
                                          				pattern-map group with a dial peer.

Use the destination keyword for outbound dial peers.

Use the incoming
                                                      						  called or incoming
                                                      						  calling keywords for inbound dial peers using called or calling
                                                					 numbers.

When both incoming and outgoing dial peers are configured with calling e164-pattern-map , it's essential to apply a provision policy to the incoming dial peer to avoid call failures.

Step 9

end

### Example:

```
Device(config-dial-peer)# end
```

Exits dial
                                          				peer configuration mode and enters privileged EXEC mode.

Step 10

(Optional) voice class e164-pattern-map load pattern-map-group-id

### Example:

```
Device# voice class e164-pattern-map load 1111
```

Loads the
                                          				specified pattern map with E.164 match patterns from a text file configured in
                                          				the pattern map.

This step
                                                					 is required only if patterns have been defined for the specified pattern map
                                                					 using a file URL in Step 4.

Step 11

show dial-peer
                                             				  voice [ summary | dial-peer-id ]

### Example:

```
Device# show dial-peer voice 1111
```

Displays the
                                          				status of a pattern map when the pattern map is associated with a dial peer.

## Verify Multiple Pattern Support

### SUMMARY STEPS

- show voice class
                                    				  e164-pattern-map [ summary | pattern-map-id ]

- show dial-peer
                                    				  voice [ summary | dial-peer-id ]

- show dialplan incall {sip | h323} {calling |
                                    				  called} e164-pattern

### DETAILED STEPS

Step 1

show voice class
                                             				  e164-pattern-map [ summary | pattern-map-id ]

Displays the
                                          				status and contents of a specified pattern map or a status summary of all
                                          				pattern maps.

### Example:

```
Device# show voice class e164-pattern-map 200 e164-pattern-map 200
-----------------------------------------
  It has 1 entries
  It is not populated from a file.
  Map is valid.

E164 pattern
-------------------
200
```

Step 2

show dial-peer
                                             				  voice [ summary | dial-peer-id ]

Displays the
                                          				status of pattern maps associated with all or a specified dial peer.

### Example:

```
Device# show dial-peer voice | include  e164-pattern-map incoming calling e164-pattern-map tag = `200' status = valid,
        destination e164-pattern-map tag = 3000 status = valid,

Device# show dial-peer voice 2222| include  e164-pattern-map incoming calling e164-pattern-map tag = `200' status = valid,
```

Step 3

show dialplan incall {sip | h323} {calling |
                                             				  called} e164-pattern

Displays inbound dial peer details and associated pattern maps
                                          				based on an incoming calling or called number.

### Example:

```
Device# show dialplan incall voip calling 23456 VoiceOverIpPeer1234567
        peer type = voice, system default peer = FALSE, information type = voice,
        description = `',
        tag = 1234567, destination-pattern = `',
        destination e164-pattern-map tag = 200 status = valid,
        destination dpg tag = 200 status = valid,
        voice reg type = 0, corresponding tag = 0,
        allow watch = FALSE
        answer-address = `', preference=0, incoming calling e164-pattern-map tag = `200' status = valid,
        CLID Restriction = None
```

## Configuration Examples for Multiple Pattern Support

### Example:
                              		  Configuring Multiple Patterns for Outbound Dial Peers Using a File URL

```
Device# voice class e164-pattern-map 1111 Device(voice-class)# url http://http-host/config-files/pattern-map.cfg Device(voice-class)# description For Outbound Dial Peer Device(voice-class)# exit Device(config)# dial-peer voice 2222 voip Device(voice-dial-peer)# destination e164-pattern-map 1111 Device(voice-dial-peer)# exit Device(config)# voice class e164-pattern-map load 1111 Device(config)# end
```

### Example:
                              		  Configuring Multiple Patterns for Outbound Dial Peers by Specifying Each E164
                              		  Pattern

```
Device# voice class e164-pattern-map 1112 Device(voice-class)# e164 5557456 Device(voice-class)# e164 5557455 Device(voice-class)# e164 5557454 Device(voice-class)# e164 5557453 Device(voice-class)# e164 5557452 Device(voice-class)# description For Outbound Dial Peer Device(voice-class)# exit Device(config)# dial-peer voice 2222 voip Device(voice-dial-peer)# destination e164-pattern-map 1112 Device(voice-dial-peer)# end !
```

### Example:
                              		  Configuring Multiple Patterns for Inbound Dial Peer

```
Device# voice class e164-pattern-map 1113 Device(voice-class)# url http://http-host/config-files/pattern-map.cfg Device(voice-class)# description For Inbound Dial Peer Device(voice-class)# exit Device(config)# dial-peer voice 2222 voip Device(voice-dial-peer)# incoming calling e164-pattern-map 1113 Device(voice-dial-peer)# exit Device(config)# voice class e164-pattern-map load 1113 Device(config)# end
```

| Feature Name | Releases | Feature
                                          				  Information |
|---|---|---|
| Configuring
                                          				  Multiple Pattern Support on a Voice Dial Peer (Inbound Calls) | Cisco IOS
                                          				  15.4 (1)T Cisco IOS XE 3.11S | This feature
                                          				  was extended for inbound VoIP dial peers for incoming calling and called
                                          				  numbers. The following
                                          				  commands were introduced or modified: incoming called
                                                						e164-pattern-map , incoming calling
                                                						e164-pattern-map |
| Configuring
                                          				  Multiple Pattern Support on a Voice Dial Peer (Outbound Calls) | Cisco IOS
                                          				  15.2(4)M Cisco IOS XE 3.7S | This feature
                                          				  allows you to add more than one E.164 destination pattern inside a pattern map
                                          				  and configure that pattern map for one or more VoIP dial peers. This feature
                                          				  is supported for outbound peers only. The following
                                          				  commands were introduced or modified: destination
                                                						e164-pattern-map , e164 , show voice class
                                                						e164-pattern-map , url , voice class e164-pattern-map
                                                						load , voice class
                                                						e164-pattern-map . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enters
                                          				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global
                                          				configuration mode. |
| Step 3 | voice class e164-pattern-map pattern-map-id Example: Device(config)# voice class e164-pattern-map 1111 | Creates a
                                          				pattern map for configuring one or multiple E.164 patterns on a dial peer and
                                          				enters voice class configuration mode. Note The prefix + sign is stripped during .T destination pattern selection. However, configuring an unrelated or empty E.164 pattern
                                                      in the same dial-peer as the .T pattern will not strip + sign. | Note | The prefix + sign is stripped during .T destination pattern selection. However, configuring an unrelated or empty E.164 pattern
                                                      in the same dial-peer as the .T pattern will not strip + sign. |
| Note | The prefix + sign is stripped during .T destination pattern selection. However, configuring an unrelated or empty E.164 pattern
                                                      in the same dial-peer as the .T pattern will not strip + sign. |
| Step 4 | Do one of the
                                       			 following: e164 pattern-map-tag url url Example: Using URL text
                                          				file: Device(voice-class)# url http://http-host/config-files/pattern-map.cfg Directly
                                          				specifying match patterns: Device(voice-class)# e164 5557123 | Configure one
                                          				or more E.164 telephone number prefix match patterns for the pattern map. Repeat
                                                					 this step for each pattern if you are using the e164 command. You can
                                                					 specify a file URL containing the patterns for this dial peer using the url url command.
                                                					 You must then load the E.164 telephone prefixes using Step 10. The file can be
                                                					 internal (on the device) or external. |
| Step 5 | (Optional) description string Example: Device(voice-class)# description It has 1 entry | (Optional) Provides a
                                          				description for the pattern map. |
| Step 6 | exit Example: Device(voice-class)# exit | Exits voice
                                          				class configuration mode and enters global configuration mode. |
| Step 7 | dial-peer voice dial-peer-id voip Example: Device(config)# dial-peer voice 2222 voip | Defines a VoIP
                                          				dial peer and enters dial peer configuration mode. |
| Step 8 | { destination \| incoming
                                             				  called \| incoming calling } e164-pattern-map pattern-map-group-id Example: Device(config-dial-peer)# incoming calling e164-pattern-map 1111 | Links a
                                          				pattern-map group with a dial peer. Use the destination keyword for outbound dial peers. Use the incoming
                                                      						  called or incoming
                                                      						  calling keywords for inbound dial peers using called or calling
                                                					 numbers. Note When both incoming and outgoing dial peers are configured with calling e164-pattern-map , it's essential to apply a provision policy to the incoming dial peer to avoid call failures. | Note | When both incoming and outgoing dial peers are configured with calling e164-pattern-map , it's essential to apply a provision policy to the incoming dial peer to avoid call failures. |
| Note | When both incoming and outgoing dial peers are configured with calling e164-pattern-map , it's essential to apply a provision policy to the incoming dial peer to avoid call failures. |
| Step 9 | end Example: Device(config-dial-peer)# end | Exits dial
                                          				peer configuration mode and enters privileged EXEC mode. |
| Step 10 | (Optional) voice class e164-pattern-map load pattern-map-group-id Example: Device# voice class e164-pattern-map load 1111 | (Optional) Loads the
                                          				specified pattern map with E.164 match patterns from a text file configured in
                                          				the pattern map. This step
                                                					 is required only if patterns have been defined for the specified pattern map
                                                					 using a file URL in Step 4. |
| Step 11 | show dial-peer
                                             				  voice [ summary \| dial-peer-id ] Example: Device# show dial-peer voice 1111 | Displays the
                                          				status of a pattern map when the pattern map is associated with a dial peer. |

| Note | The prefix + sign is stripped during .T destination pattern selection. However, configuring an unrelated or empty E.164 pattern
                                                      in the same dial-peer as the .T pattern will not strip + sign. |
|---|---|

| Note | When both incoming and outgoing dial peers are configured with calling e164-pattern-map , it's essential to apply a provision policy to the incoming dial peer to avoid call failures. |
|---|---|

| Step 1 | show voice class
                                             				  e164-pattern-map [ summary \| pattern-map-id ] Displays the
                                          				status and contents of a specified pattern map or a status summary of all
                                          				pattern maps. Example: Device# show voice class e164-pattern-map 200 e164-pattern-map 200
-----------------------------------------
  It has 1 entries
  It is not populated from a file.
  Map is valid.

E164 pattern
-------------------
200 |
|---|---|---|
| Step 2 | show dial-peer
                                             				  voice [ summary \| dial-peer-id ] Displays the
                                          				status of pattern maps associated with all or a specified dial peer. Example: Device# show dial-peer voice \| include  e164-pattern-map incoming calling e164-pattern-map tag = `200' status = valid,
        destination e164-pattern-map tag = 3000 status = valid,

Device# show dial-peer voice 2222\| include  e164-pattern-map incoming calling e164-pattern-map tag = `200' status = valid, |
| Step 3 | show dialplan incall {sip \| h323} {calling \|
                                             				  called} e164-pattern Displays inbound dial peer details and associated pattern maps
                                          				based on an incoming calling or called number. Example: Device# show dialplan incall voip calling 23456 VoiceOverIpPeer1234567
        peer type = voice, system default peer = FALSE, information type = voice,
        description = `',
        tag = 1234567, destination-pattern = `',
        destination e164-pattern-map tag = 200 status = valid,
        destination dpg tag = 200 status = valid,
        voice reg type = 0, corresponding tag = 0,
        allow watch = FALSE
        answer-address = `', preference=0, incoming calling e164-pattern-map tag = `200' status = valid,
        CLID Restriction = None |