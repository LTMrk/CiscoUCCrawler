---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-multiple-outbound-dial-peer-html-a35eab5d2a
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/multiple-outbound-dial-peer.html
retrieved_at: 2026-08-16T15:45:55.146508+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Inbound Leg Headers for Outbound Dial-Peer Matching

## Chapter: Inbound Leg Headers for Outbound Dial-Peer Matching

# Inbound Leg Headers for Outbound Dial-Peer Matching

## Overview

The Inbound Leg Headers for Outbound Dial-Peer Matching feature allows you to match and provision an outbound dial peer for
                           an outbound call leg using the headers from an inbound call leg. The following headers of an incoming call leg can be used
                           for outbound dial-peer matching:

VIA (SIP Header)

FROM (SIP Header)

TO (SIP Header)

DIVERSION (SIP Header)

REFERRED BY (SIP Header)

Called Number

Calling Number

Carrier ID

The above headers are retrieved from an incoming INVITE or REFER message and used for outbound dial-peer provisioning.

SIP headers of an INVITE message are saved to an associated call leg. For example, an INVITE message is received for a new
                           call leg A. Then, SIP headers are saved to call leg A itself for outbound dial-peer lookup.

On the other hand, SIP headers of a REFER message are saved to the peer call leg of the associated call leg. For example,
                           call leg A and call leg B are connected in CUBE. The party at Call Leg B makes a blind transfer to the party at Call Leg C.
                           The party at Call Leg B (transferor) makes a blind transfer to the party at call leg C, triggering a SIP REFER message which
                           the party at Call Leg B sends to CUBE for the transfer to C.

### Feature Information

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature
                                          				  Information

Inbound Leg Headers for Outbound Dial-PeerMatching

The
                                          				  following commands were introduced by this feature: destination
                                                						provision-policy , destination
                                                						uri-via , destination
                                                						uri-to , destination
                                                						uri-from , destination
                                                						uri-diversion , destination
                                                						uri-referred-by , show voice class dial-peer
                                                						provision-policy

## Prerequisites for Inbound Leg Headers for Outbound Dial-PeerMatching

CUBE or Voice Gateway must be configured.

## Restrictions for Inbound Leg Headers for Outbound Dial-PeerMatching

The existing header-passing command supports modification of
                                 			 SIP headers of INVITE message by the Tool Command Language (TCL) application.
                                 			 If the above SIP headers are modified by the TCL application, they cannot be
                                 			 used for outbound dial-peer provisioning.

If multiple SIP
                                 			 via headers and diversion headers are found in an incoming INVITE or REFER
                                 			 message, only the top-most via header and top-most diversion header of an
                                 			 incoming INVITE or REFER message are used for outbound dial-peer provisioning.

When an incoming call is matched to an inbound dial peer with an associated provision profile without rules, outbound dial-peer
                                 provisioning is disabled and the incoming call is disconnected by CUBE or voice gateway with cause code "unassigned number
                                 (1)".

## Configuring Inbound Leg Headers for Outbound Dial-PeerMatching

### Before you begin

Necessary pattern
                              		  maps have been configured.

### SUMMARY STEPS

- enable

- configure terminal

- voice class dial-peer provision-policy tag

- (Optional) description string

- preference preference-order first-attribute second-attribute

- exit

- dial-peer voice inbound-dial-peer-tag voip

- destination provision-policy tag

- exit

- dial-peer voice outbound-dial-peer-tag voip

- Configure a
                              			 match command for an outbound dial peer according to the provision policy rule
                              			 attribute configured.

- end

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

voice class dial-peer provision-policy tag

### Example:

```
Device(config)# voice class dial-peer provision-policy 200
```

Creates a
                                          				provision policy profile in which a set of attributes for dial-peer matching
                                          				can be defined.

You can use the shutdown command to deactivate the provision policy and allow normal outbound dial-peer provisioning.

Step 4

(Optional) description string

### Example:

```
Device(voice-class)# description match both calling and called
```

Provides a
                                          				description for the provision policy profile.

Step 5

preference preference-order first-attribute second-attribute

### Example:

```
Device(voice-class)# preference 2 calling called
```

Configures a
                                          				provision policy rule.

You can configure up to two rules. This means up to four attributes can be configured for matching outbound dial peers.

If rules are not configured, outbound dial-peer provisioning is disabled, and an incoming call matched to an inbound dial
                                                peer associated with this profile is disconnected by CUBE or voice gateway with cause code "unassigned number (1)".

Step 6

exit

### Example:

```
Device(voice-class)# exit
```

Exits voice
                                          				class configuration mode and enters global configuration mode.

Step 7

dial-peer voice inbound-dial-peer-tag voip

Step 8

destination provision-policy tag

### Example:

```
Device(config)# dial-peer voice 100 voip
Device(config-dial-peer)# destination provision-policy 200
Device(config)# exit
```

Associates a
                                          				provision policy profile with an inbound dial peer.

Step 9

exit

Step 10

dial-peer voice outbound-dial-peer-tag voip

Step 11

Configure a
                                       			 match command for an outbound dial peer according to the provision policy rule
                                       			 attribute configured.

destination-pattern pattern

destination e164-pattern-map pattern-map-class-id

destination calling
                                                         						  e164-pattern-map pattern-map-class-id

carrier-id
                                                         						  target

destination uri uri-class-tag

destination uri-via uri-class-tag

destination uri-to uri-class-tag

destination
                                                         						  uri-from uri-class-tag

destination
                                                         						  uri-diversion uri-class-tag

destination
                                                         						  uri-referred-by uri-class-tag

### Example:

```
Device(config)# dial-peer voice 300 voip
Device(config-dial-peer)# destination uri-from 200
Device(config)# exit
```

Step 12

end

### Example:

```
Device(config-dial-peer)# end
```

Exits dial
                                          				peer configuration mode and enters privileged EXEC mode.

## Verify Inbound Leg Headers for Outbound Dial-PeerMatching

Use this procedure to verify inbound leg headers so that you can match them to Outbound dial peers.

### SUMMARY STEPS

- show dialplan incall {sip | h323} {calling | called} e164-pattern | include voice

- show dialplan dialpeer inbound-dial-peer-id number e164-pattern [timeout] | include Voice

- show voice class dial-peer provision-policy

### DETAILED STEPS

Step 1

show dialplan incall {sip | h323} {calling | called} e164-pattern | include voice

Displays inbound dial peers based on an incoming calling or called number. Once you have the dial peer number, you can use
                                          it to search for the complete dial-peer details in the running-config.

### Example:

```
Device# show dialplan incall sip calling 3333 | include Voice VoiceOverIpPeer1

Device# show dialplan incall sip calling 4444 | include Voice VoiceOverIpPeer1

Device# show running-config | section dial-peer voice 1 voip dial-peer voice 1 voip
 destination dpg 10000
 incoming calling e164-pattern-map 100
 dtmf-relay rtp-nte
 codec g711ulaw

Device# show dialplan incall sip called 6000 timeout | include Voice VoiceOverIpPeer100

Device# show running-config | section dial-peer voice 100 voip dial-peer voice 100 voip
 incoming called e164-pattern-map 1
 incoming calling e164-pattern-map 1
 dtmf-relay rtp-nte
 codec g711ulaw

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

Step 2

show dialplan dialpeer inbound-dial-peer-id number e164-pattern [timeout] | include Voice

### Example:

```
Device# show dialplan dialpeer 1 number 23457 timeout | include Voice VoiceOverIpPeer100013
VoiceOverIpPeer100012
```

### Example:

```
voice class dial-peer provision-policy 2000
 preference 2 diversion to
!
...
!
dial-peer voice 32555 voip
 session protocol sipv2
 session target ipv4:1.5.14.9
 destination uri-diversion 1
 destination uri-to test2
!
dial-peer voice 32991 voip
 destination provision-policy 2000
 incoming called-number 1234
!

Device# show dialplan dialpeer 32991 number 2234 timeout Macro Exp.: 2234
Enter Diversion header:sip:1234@cisco.com Enter To header:sip:2234@10.0.0.0 VoiceOverIpPeer32134
        peer type = voice, system default peer = FALSE, information type = voice,
        description = `',
```

Step 3

show voice class dial-peer provision-policy

### Example:

```
Device# show voice class dial-peer provision-policy Voice class dial-peer provision-policy: 100		AdminStatus: Up
 Description: match only called

 Pref  Policy Rule
 ----  -----------
 1     called

Voice class dial-peer provision-policy: 101		AdminStatus: Up
 Description: match both calling and called

 Pref  Policy Rule
 ----  -----------
 1     called calling
 
Voice class dial-peer provision-policy: 102		AdminStatus: Up
 Description: match calling first; if no match then match called

 Pref  Policy Rule
 ----  -----------
 1	calling
 2	called

Voice class dial-peer provision-policy: 200		AdminStatus: Up
 Description: match referred-by and via uri; if no match then match request- uri
 
 Pref  Policy Rule
 ----  -----------
 1	referred-by via
 2	uri

voice class dial-peer provision-policy: 300		AdminStatus: Up
 Description: match only request-uri

 Pref  Policy Rule
 ----  -----------
 1	uri

Voice class dial-peer provision-policy: 400		AdminStatus: Up
 Description: match only request uri; if no match then match called

 Pref  Policy Rule
 ----  -----------
 1	uri
 2	called
```

## Configuration
                        	 Example: Inbound Leg Headers for Outbound Dial-Peer Matching

### Example:
                              		  Configuring Inbound Called or Calling Numbers Used for Outbound Dial-Peer
                              		  Matching

```
Device> enable Device# configure terminal Device(config)# voice class dial-peer provision-policy 200 Device(voice-class)# description match both calling and called Device(voice-class)# preference 2 calling called Device(voice-class)# exit Device(config)# voice class e164-pattern-map 300 Device(voice-class)# description patterns Device(voice-class)# e164 5557123 Device(voice-class)# e164 5558123 Device(voice-class)# e164 5559123 Device(voice-class)# exit !Associating the Provision Policy with an Inbound Dial Peer
Device(config)# dial-peer voice 100 voip Device(config-dial-peer)# destination provision-policy 200 Device(config-dial-peer)# end !Associates a Pattern Map with an Outbound Dial Peer.  
! The called number in the SIP headers of the inbound leg is matched to select the below outbound dial peer.
Device(config)# dial-peer voice 200 voip Device(config-dial-peer)# destination e164-pattern-map 300 Device(config-dial-peer)# end
```

### Example:
                              		  Configuring Inbound SIP Headers for Outbound Dial-Peer Matching

```
Device> enable Device# configure terminal Device(config)# voice class dial-peer provision-policy 200 Device(voice-class)# description match both calling and called Device(voice-class)# preference 2 via from Device(voice-class)# exit !Associating the Provision Policy with an Inbound Dial Peer
Device(config)# dial-peer voice 100 voip Device(config-dial-peer)# destination provision-policy 200 Device(config-dial-peer)# end Device(config)# voice class uri 200 sip Device(config-voice-uri-clas)# pattern 25054.. !Associates a Provision Policy with an Outbound Dial Peer.  
The FROM SIP headers of the inbound leg is matched to select the below outbound dial peer.
Device(config)# dial-peer voice 200 voip Device(config-dial-peer)# destination uri-from 200 Device(config-dial-peer)# end
```

| Feature Name | Releases | Feature
                                          				  Information |
|---|---|---|
| Inbound Leg Headers for Outbound Dial-PeerMatching | Baseline Functionality | The
                                          				  following commands were introduced by this feature: destination
                                                						provision-policy , destination
                                                						uri-via , destination
                                                						uri-to , destination
                                                						uri-from , destination
                                                						uri-diversion , destination
                                                						uri-referred-by , show voice class dial-peer
                                                						provision-policy |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enters
                                          				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global
                                          				configuration mode. |
| Step 3 | voice class dial-peer provision-policy tag Example: Device(config)# voice class dial-peer provision-policy 200 | Creates a
                                          				provision policy profile in which a set of attributes for dial-peer matching
                                          				can be defined. You can use the shutdown command to deactivate the provision policy and allow normal outbound dial-peer provisioning. |
| Step 4 | (Optional) description string Example: Device(voice-class)# description match both calling and called | (Optional) Provides a
                                          				description for the provision policy profile. |
| Step 5 | preference preference-order first-attribute second-attribute First
                                                				  Attribute Second Attribute diversion from, referred-by, to, uri,
                                                				  via from diversion, referred-by, to,
                                                				  uri, via referred-by diversion, from, to, uri,
                                                				  via to diversion, referred-by, from, uri, via uri diversion, referred-by, to, from, via, carrier-id via diversion, referred-by, to,
                                                				  uri, from called calling, carrier-id calling called carrier-id called, uri Example: Device(voice-class)# preference 2 calling called | First
                                                				  Attribute | Second Attribute | diversion | from, referred-by, to, uri,
                                                				  via | from | diversion, referred-by, to,
                                                				  uri, via | referred-by | diversion, from, to, uri,
                                                				  via | to | diversion, referred-by, from, uri, via | uri | diversion, referred-by, to, from, via, carrier-id | via | diversion, referred-by, to,
                                                				  uri, from | called | calling, carrier-id | calling | called | carrier-id | called, uri | Configures a
                                          				provision policy rule. You can configure up to two rules. This means up to four attributes can be configured for matching outbound dial peers. If rules are not configured, outbound dial-peer provisioning is disabled, and an incoming call matched to an inbound dial
                                                peer associated with this profile is disconnected by CUBE or voice gateway with cause code "unassigned number (1)". |
| First
                                                				  Attribute | Second Attribute |
| diversion | from, referred-by, to, uri,
                                                				  via |
| from | diversion, referred-by, to,
                                                				  uri, via |
| referred-by | diversion, from, to, uri,
                                                				  via |
| to | diversion, referred-by, from, uri, via |
| uri | diversion, referred-by, to, from, via, carrier-id |
| via | diversion, referred-by, to,
                                                				  uri, from |
| called | calling, carrier-id |
| calling | called |
| carrier-id | called, uri |
| Step 6 | exit Example: Device(voice-class)# exit | Exits voice
                                          				class configuration mode and enters global configuration mode. |
| Step 7 | dial-peer voice inbound-dial-peer-tag voip | Enters dial peer configuration mode for an inbound dial
                                       			 peer. |
| Step 8 | destination provision-policy tag Example: Device(config)# dial-peer voice 100 voip
Device(config-dial-peer)# destination provision-policy 200
Device(config)# exit | Associates a
                                          				provision policy profile with an inbound dial peer. |
| Step 9 | exit | Exits dial peer configuration mode. |
| Step 10 | dial-peer voice outbound-dial-peer-tag voip | Enters dial peer configuration mode for an outbound dial
                                       			 peer. |
| Step 11 | Configure a
                                       			 match command for an outbound dial peer according to the provision policy rule
                                       			 attribute configured. Provision Policy Rule
                                                				  Attribute Dial-peer Match
                                                				  command called destination-pattern pattern destination e164-pattern-map pattern-map-class-id calling destination calling
                                                         						  e164-pattern-map pattern-map-class-id carrier-id carrier-id
                                                         						  target uri destination uri uri-class-tag via destination uri-via uri-class-tag to destination uri-to uri-class-tag from destination
                                                         						  uri-from uri-class-tag diversion destination
                                                         						  uri-diversion uri-class-tag referred-by destination
                                                         						  uri-referred-by uri-class-tag Example: Device(config)# dial-peer voice 300 voip
Device(config-dial-peer)# destination uri-from 200
Device(config)# exit | Provision Policy Rule
                                                				  Attribute | Dial-peer Match
                                                				  command | called | destination-pattern pattern destination e164-pattern-map pattern-map-class-id | calling | destination calling
                                                         						  e164-pattern-map pattern-map-class-id | carrier-id | carrier-id
                                                         						  target | uri | destination uri uri-class-tag | via | destination uri-via uri-class-tag | to | destination uri-to uri-class-tag | from | destination
                                                         						  uri-from uri-class-tag | diversion | destination
                                                         						  uri-diversion uri-class-tag | referred-by | destination
                                                         						  uri-referred-by uri-class-tag | Configure
                                       			 a match command based on any of the four attributes defined in the provision
                                       			 policy rule. |
| Provision Policy Rule
                                                				  Attribute | Dial-peer Match
                                                				  command |
| called | destination-pattern pattern destination e164-pattern-map pattern-map-class-id |
| calling | destination calling
                                                         						  e164-pattern-map pattern-map-class-id |
| carrier-id | carrier-id
                                                         						  target |
| uri | destination uri uri-class-tag |
| via | destination uri-via uri-class-tag |
| to | destination uri-to uri-class-tag |
| from | destination
                                                         						  uri-from uri-class-tag |
| diversion | destination
                                                         						  uri-diversion uri-class-tag |
| referred-by | destination
                                                         						  uri-referred-by uri-class-tag |
| Step 12 | end Example: Device(config-dial-peer)# end | Exits dial
                                          				peer configuration mode and enters privileged EXEC mode. |

| First
                                                				  Attribute | Second Attribute |
|---|---|
| diversion | from, referred-by, to, uri,
                                                				  via |
| from | diversion, referred-by, to,
                                                				  uri, via |
| referred-by | diversion, from, to, uri,
                                                				  via |
| to | diversion, referred-by, from, uri, via |
| uri | diversion, referred-by, to, from, via, carrier-id |
| via | diversion, referred-by, to,
                                                				  uri, from |
| called | calling, carrier-id |
| calling | called |
| carrier-id | called, uri |

| Provision Policy Rule
                                                				  Attribute | Dial-peer Match
                                                				  command |
|---|---|
| called | destination-pattern pattern destination e164-pattern-map pattern-map-class-id |
| calling | destination calling
                                                         						  e164-pattern-map pattern-map-class-id |
| carrier-id | carrier-id
                                                         						  target |
| uri | destination uri uri-class-tag |
| via | destination uri-via uri-class-tag |
| to | destination uri-to uri-class-tag |
| from | destination
                                                         						  uri-from uri-class-tag |
| diversion | destination
                                                         						  uri-diversion uri-class-tag |
| referred-by | destination
                                                         						  uri-referred-by uri-class-tag |

| Step 1 | show dialplan incall {sip \| h323} {calling \| called} e164-pattern \| include voice Displays inbound dial peers based on an incoming calling or called number. Once you have the dial peer number, you can use
                                          it to search for the complete dial-peer details in the running-config. Example: Device# show dialplan incall sip calling 3333 \| include Voice VoiceOverIpPeer1

Device# show dialplan incall sip calling 4444 \| include Voice VoiceOverIpPeer1

Device# show running-config \| section dial-peer voice 1 voip dial-peer voice 1 voip
 destination dpg 10000
 incoming calling e164-pattern-map 100
 dtmf-relay rtp-nte
 codec g711ulaw

Device# show dialplan incall sip called 6000 timeout \| include Voice VoiceOverIpPeer100

Device# show running-config \| section dial-peer voice 100 voip dial-peer voice 100 voip
 incoming called e164-pattern-map 1
 incoming calling e164-pattern-map 1
 dtmf-relay rtp-nte
 codec g711ulaw

Device# show dialplan incall voip calling 23456 VoiceOverIpPeer1234567
        peer type = voice, system default peer = FALSE, information type = voice,
        description = `',
        tag = 1234567, destination-pattern = `',
        destination e164-pattern-map tag = 200 status = valid,
        destination dpg tag = 200 status = valid,
        voice reg type = 0, corresponding tag = 0,
        allow watch = FALSE
        answer-address = `', preference=0, incoming calling e164-pattern-map tag = `200' status = valid,
        CLID Restriction = None |
|---|---|---|---|---|---|---|---|---|---|
| Step 2 | show dialplan dialpeer inbound-dial-peer-id number e164-pattern [timeout] \| include Voice Displays a list of outbound dial peers based on a specified inbound dial peer. This command line will be helpful find a list
                                       of outbound dial peer of a destination dial-peer group. Example: Device# show dialplan dialpeer 1 number 23457 timeout \| include Voice VoiceOverIpPeer100013
VoiceOverIpPeer100012 Example: voice class dial-peer provision-policy 2000
 preference 2 diversion to
!
...
!
dial-peer voice 32555 voip
 session protocol sipv2
 session target ipv4:1.5.14.9
 destination uri-diversion 1
 destination uri-to test2
!
dial-peer voice 32991 voip
 destination provision-policy 2000
 incoming called-number 1234
!

Device# show dialplan dialpeer 32991 number 2234 timeout Macro Exp.: 2234
Enter Diversion header:sip:1234@cisco.com Enter To header:sip:2234@10.0.0.0 VoiceOverIpPeer32134
        peer type = voice, system default peer = FALSE, information type = voice,
        description = `', |
| Step 3 | show voice class dial-peer provision-policy Displays a list of configured provision policies and associated rules. Example: Device# show voice class dial-peer provision-policy Voice class dial-peer provision-policy: 100		AdminStatus: Up
 Description: match only called

 Pref  Policy Rule
 ----  -----------
 1     called

Voice class dial-peer provision-policy: 101		AdminStatus: Up
 Description: match both calling and called

 Pref  Policy Rule
 ----  -----------
 1     called calling
 
Voice class dial-peer provision-policy: 102		AdminStatus: Up
 Description: match calling first; if no match then match called

 Pref  Policy Rule
 ----  -----------
 1	calling
 2	called

Voice class dial-peer provision-policy: 200		AdminStatus: Up
 Description: match referred-by and via uri; if no match then match request- uri
 
 Pref  Policy Rule
 ----  -----------
 1	referred-by via
 2	uri

voice class dial-peer provision-policy: 300		AdminStatus: Up
 Description: match only request-uri

 Pref  Policy Rule
 ----  -----------
 1	uri

Voice class dial-peer provision-policy: 400		AdminStatus: Up
 Description: match only request uri; if no match then match called

 Pref  Policy Rule
 ----  -----------
 1	uri
 2	called |