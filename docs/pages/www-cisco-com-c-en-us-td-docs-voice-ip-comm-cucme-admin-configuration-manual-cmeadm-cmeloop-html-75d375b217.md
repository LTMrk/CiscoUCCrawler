---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmeloop-html-75d375b217
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmeloop.html
retrieved_at: 2026-08-21T07:23:43.925615+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Loopback Call Routing

## Chapter: Loopback Call Routing

# Loopback Call Routing

## Information About Loopback Call Routing

### Loopback Call
                           	 Routing

Loopback call
                              		routing in a Cisco Unified CME system is provided through a mechanism called
                              		loopback-dn, which provides a software-based limited emulation of back-to-back
                              		physical voice ports connected together to provide a loopback call-routing path
                              		for voice calls.

Loopback call
                              		routing and loopback-dn restricts the passage of call-transfer and
                              		call-forwarding supplementary service requests through the loopback. Instead of
                              		passing these requests through, the loopback-dn mechanism attempts to service
                              		the requests locally. This allows loopback-dn configurations to be used in call
                              		paths where one of the external devices does not support call transfer or call
                              		forwarding (Cisco-proprietary or H.450-based). Control messages that request
                              		call transfer or call forwarding are intercepted at the loopback virtual port
                              		and serviced on the local voice gateway. If needed, this mechanism creates
                              		VoIP-to-VoIP call-routing paths.

Loopback call
                              		routing may be used for routing H.323 calls to Cisco Unity Express. For
                              		information on configuring Cisco Unity Express, see the Cisco Unity Express documentation.

A preferred
                                          		  alternative to loopback call routing was introduced in Cisco CME 3.1. This
                                          		  alternative blocks H.450-based supplementary service requests by using the
                                          		  following Cisco IOS commands: no supplementary-service
                                                				h450.2 , no supplementary-service
                                                				h450.3 , and supplementary-service
                                                				h450.12 . For more information, see Configure Call Transfer and Forwarding .

Use of loopback-dn
                              		configurations within a VoIP network should be restricted to resolving critical
                              		network interoperability service problems that cannot otherwise be solved.
                              		Loopback-dn configurations are intended for use in VoIP network interworking
                              		where the alternative would be to make use of back-to-back-connected physical
                              		voice ports. Loopback-dn configurations emulate the effect of a back-to-back
                              		physical voice-port arrangement without the expense of the physical voice-port
                              		hardware. Because digital signal processors (DSPs) are not involved in
                              		loopback-dn arrangements, the configuration does not support interworking or
                              		transcoding between calls that use different voice codecs. In many cases, use
                              		of back-to-back physical voice ports that do involve DSPs to resolve VoIP
                              		network interworking issues is preferred, because it introduces fewer
                              		restrictions in terms of supported codecs and call flows.

Loopback call
                              		routing requires two extensions (ephone-dns) to be separately configured, each
                              		as half of a loopback-dn pair. Ephone-dns that are defined as a loopback-dn
                              		pair can only be used for loopback call routing. In addition to defining the
                              		loopback-dn pair, you must specify preference, huntstop, class of restriction
                              		(COR), and translation rules.

## Configure Loopback Call Routing

### Enable Loopback
                           	 Call Routing

To enable loopback
                                 		  call-routing, perform the following steps for each ephone-dn that is part of
                                 		  the loopback-dn pair.

Restriction

Loopback-dns do
                                             			 not support T.38 fax relay.

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn dn-tag

- number number [ secondary number ] [ no-reg [ both | primary ]]

- caller-id { local | passthrough }

- no huntstop

- preference preference-order [ secondary secondary-order ]

- cor { incoming | outgoing } cor-list-name

- translate { called | calling } translation-rule-tag

- loopback-dn dn-tag [ forward number-of-digits | strip number-of-digits ]
                                       				  [ prefix prefix-digit-string ]
                                       				  [ suffix suffix-digit-string ]
                                       				  [ retry seconds ] [ auto-con ] [ codec { g711alaw | g711ulaw }]

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ephone-dn dn-tag

#### Example:

```
Router(config)# ephone-dn 15
```

Enters
                                             				ephone-dn configuration mode, creates an ephone-dn, and optionally assigns it
                                             				dual-line status.

- dn-tag —Unique sequence number that identifies this
                                                				  ephone-dn during configuration tasks. Range is platform- and version-dependent.

Ephone-dns
                                                         				  used for loopback cannot be dual-line ephone-dns.

Step 4

number number [ secondary number ] [ no-reg [ both | primary ]]

#### Example:

```
Router(config-ephone-dn)# number 2001
```

Associates a
                                             				number with this extension (ephone-dn).

number —String of up to 16 digits that represents a
                                                   					 telephone or extension number to be associated with this ephone-dn.

secondary —(Optional) Allows you to associate a
                                                   					 second telephone number with an ephone-dn.

no-reg —(Optional) Specifies that this number
                                                   					 should not register with the H.323 gatekeeper. The no-reg keyword indicates that only the secondary number should not register. The no-reg both keywords indicate that both numbers should not register, and the no-reg
                                                         						  primary keywords indicate that only the primary number should not
                                                   					 register.

Step 5

caller-id { local | passthrough }

#### Example:

```
Router(config-ephone-dn)# caller-id local
```

Specifies
                                             				caller-ID treatment for outbound calls originated from the ephone-dn. The
                                             				default if this command is not used is as follows. For transferred calls,
                                             				caller ID is provided by the number and name fields from the outbound side of
                                             				the loopback-dn. For forwarded calls, caller ID is provided by the original
                                             				caller ID of the incoming call. Settings for the caller-id
                                                   					 block command and translation rules on the outbound side are
                                             				executed.

local —Passes the local caller ID on redirected
                                                   					 calls. This is the preferred usage.

passthrough —Passes the original caller ID on
                                                   					 redirected calls.

Step 6

no huntstop

#### Example:

```
Router(config-ephone-dn)# no huntstop
```

Disables
                                             				huntstop and allows call hunting behavior for an extension (ephone-dn).

Step 7

preference preference-order [ secondary secondary-order ]

#### Example:

```
Router(config-ephone-dn)# preference 1
```

Sets
                                             				dial-peer preference for an extension (ephone-dn).

preference-order —Preference order for the primary
                                                   					 number associated with an extension (ephone-dn). Range is 0 to 10, where 0 is
                                                   					 the highest preference and 10 is the lowest preference. Default is 0.

secondary secondary-order —(Optional) Preference order for the secondary
                                                   					 number associated with the ephone-dn. Range is 0 to 10, where 0 is the highest
                                                   					 preference and 10 is the lowest preference. Default is 9.

Step 8

cor { incoming | outgoing } cor-list-name

#### Example:

```
Router(config-ephone-dn)# cor incoming corlist1
```

Applies a
                                             				class of restriction (COR) to the dial peers associated with an extension. COR
                                             				specifies which incoming dial peer can use which outgoing dial peer to make a
                                             				call. Each dial peer can be provisioned with an incoming and an outgoing COR
                                             				list.

For
                                             				information about COR, see Dial Peer Configuration on
                                                				  Voice Gateway Routers .

Step 9

translate { called | calling } translation-rule-tag

#### Example:

```
Router(config-ephone-dn)# translate called 1
```

Selects an
                                             				existing translation rule and applies it to a calling number or a number that
                                             				has been called. This command enables the manipulation of numbers as part of a
                                             				dial plan to manage overlapping or nonconsecutive numbering schemes.

called —Translates the called number.

calling —Translates the calling number.

translation-rule-tag —Unique sequence number of the
                                                   					 previously defined translation rule. Range is 1 to 2147483647.

This
                                                         				  command requires that you have previously defined appropriate translation rules
                                                         				  using the voice
                                                               						translation-rule and rule commands.

Step 10

loopback-dn dn-tag [ forward number-of-digits | strip number-of-digits ]
                                                				  [ prefix prefix-digit-string ]
                                                				  [ suffix suffix-digit-string ]
                                                				  [ retry seconds ] [ auto-con ] [ codec { g711alaw | g711ulaw }]

#### Example:

```
Router(config-ephone-dn)# loopback-dn 24 forward 15 prefix 415353....
```

Enables
                                             				H.323 call transfer and call forwarding by using hairpin call routing for VoIP
                                             				endpoints that do not support Cisco-proprietary or H.450-based call-transfer
                                             				and call-forwarding.

dn-tag— Unique sequence number that identifies the
                                                   					 ephone-dn that is being paired for loopback with the ephone-dn that is being
                                                   					 configured. The paired ephone-dn must be one that is already defined in the
                                                   					 system.

forward number-of-digits —(Optional) Number of digits in
                                                   					 the original called number to forward to the other ephone-dn in the loopback-dn
                                                   					 pair. Range is 1 to 32. Default is to forward all digits.

strip number-of-digits —(Optional) Number of leading
                                                   					 digits to be stripped from the original called number before forwarding to the
                                                   					 other ephone-dn in the loopback-dn pair. Range is 1 to 32. Default is to not
                                                   					 strip any digits.

prefix prefix-digit-string —(Optional) Defines a string of
                                                   					 digits to add in front of the forwarded called number. Maximum number of digits
                                                   					 in the string is 32. Default is that no prefix is defined.

suffix suffix-digit-string —(Optional) Defines a string of
                                                   					 digits to add to the end of the forwarded called number. Maximum number of
                                                   					 digits in the string is 32. Default is that no suffix is defined. If you add a
                                                   					 suffix that starts with the pound character (#), the string must be enclosed in
                                                   					 quotation marks.

retry seconds —(Optional) Number of seconds to wait
                                                   					 before retrying the loopback target when it is busy or unavailable. Range is 0
                                                   					 to 32767. Default is that retry is disabled and appropriate call-progress tones
                                                   					 are passed to the call originator.

auto-con —(Optional) Immediately connects the call
                                                   					 and provides in-band alerting while waiting for the far-end destination to
                                                   					 answer. Default is that automatic connection is disabled.

codec —(Optional) Explicitly forces the G.711 A-law
                                                   					 or G.711 mu-law voice coding type to be used for calls that pass through the
                                                   					 loopback-dn. This overrides the G.711 coding type that is negotiated for the
                                                   					 call and provides conversion from mu-law to A-law, if needed. Default is that
                                                   					 Real-Time Transport Protocol (RTP) voice packets are passed through the
                                                   					 loopback-dn without considering the G.711 coding type negotiated for the calls.

g711alaw— G.711 A-law, 64000 bits per second, for
                                                   					 T1.

g711ulaw— G.711 mu-law, 64000 bits per second, for
                                                   					 E1.

Step 11

end

#### Example:

```
Router(config-ephone-dn)# end
```

Exits to
                                             				privileged exec mode.

### Verify Loopback Call Routing

Use the show running-config or show telephony-service ephone-dn command to
                                          			 display ephone-dn configurations.

## Configuration Example for Loopback Call Routing

### Example for Enabling Loopback Call Routing

The following example uses ephone-dns 15 and 16 as a loopback-dn pair.
                                 		  Calls are routed through this loopback ephone-dn pair in the following way:

An incoming call to 4085552xxx enters the loopback pair through
                                       				ephone-dn 16 and exits the loopback via ephone-dn 15 as an outgoing call to
                                       				2xxx (based on the forward 4 digits setting).

An incoming call to 6xxx enters the loopback pair through
                                       				ephone-dn 15 and exits the loopback via ephone-dn 16 as an outgoing call to
                                       				4157676xxx (based on the prefix 415767 setting).

```
ephone-dn 15
		 number 6...
		 loopback-dn 16 forward 4 prefix 415767
		 caller-id local
		 no huntstop
		!
		ephone-dn 16
		 number 4085552...
		 loopback-dn 15 forward 4
		 caller-id local
		 no huntstop
```

## Feature
                        	 Information for Loopback Call Routing

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature
                                             					 Name

Cisco Unified CME Version

Feature
                                             					 Information

Loopback
                                             					 Call Routing

2.0

Loopback
                                             					 call routing was introduced.

| Note | A preferred
                                          		  alternative to loopback call routing was introduced in Cisco CME 3.1. This
                                          		  alternative blocks H.450-based supplementary service requests by using the
                                          		  following Cisco IOS commands: no supplementary-service
                                                				h450.2 , no supplementary-service
                                                				h450.3 , and supplementary-service
                                                				h450.12 . For more information, see Configure Call Transfer and Forwarding . |
|---|---|

| Restriction | Loopback-dns do
                                             			 not support T.38 fax relay. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-dn dn-tag Example: Router(config)# ephone-dn 15 | Enters
                                             				ephone-dn configuration mode, creates an ephone-dn, and optionally assigns it
                                             				dual-line status. dn-tag —Unique sequence number that identifies this
                                                				  ephone-dn during configuration tasks. Range is platform- and version-dependent. Note Ephone-dns
                                                         				  used for loopback cannot be dual-line ephone-dns. | Note | Ephone-dns
                                                         				  used for loopback cannot be dual-line ephone-dns. |
| Note | Ephone-dns
                                                         				  used for loopback cannot be dual-line ephone-dns. |
| Step 4 | number number [ secondary number ] [ no-reg [ both \| primary ]] Example: Router(config-ephone-dn)# number 2001 | Associates a
                                             				number with this extension (ephone-dn). number —String of up to 16 digits that represents a
                                                   					 telephone or extension number to be associated with this ephone-dn. secondary —(Optional) Allows you to associate a
                                                   					 second telephone number with an ephone-dn. no-reg —(Optional) Specifies that this number
                                                   					 should not register with the H.323 gatekeeper. The no-reg keyword indicates that only the secondary number should not register. The no-reg both keywords indicate that both numbers should not register, and the no-reg
                                                         						  primary keywords indicate that only the primary number should not
                                                   					 register. |
| Step 5 | caller-id { local \| passthrough } Example: Router(config-ephone-dn)# caller-id local | Specifies
                                             				caller-ID treatment for outbound calls originated from the ephone-dn. The
                                             				default if this command is not used is as follows. For transferred calls,
                                             				caller ID is provided by the number and name fields from the outbound side of
                                             				the loopback-dn. For forwarded calls, caller ID is provided by the original
                                             				caller ID of the incoming call. Settings for the caller-id
                                                   					 block command and translation rules on the outbound side are
                                             				executed. local —Passes the local caller ID on redirected
                                                   					 calls. This is the preferred usage. passthrough —Passes the original caller ID on
                                                   					 redirected calls. |
| Step 6 | no huntstop Example: Router(config-ephone-dn)# no huntstop | Disables
                                             				huntstop and allows call hunting behavior for an extension (ephone-dn). |
| Step 7 | preference preference-order [ secondary secondary-order ] Example: Router(config-ephone-dn)# preference 1 | Sets
                                             				dial-peer preference for an extension (ephone-dn). preference-order —Preference order for the primary
                                                   					 number associated with an extension (ephone-dn). Range is 0 to 10, where 0 is
                                                   					 the highest preference and 10 is the lowest preference. Default is 0. secondary secondary-order —(Optional) Preference order for the secondary
                                                   					 number associated with the ephone-dn. Range is 0 to 10, where 0 is the highest
                                                   					 preference and 10 is the lowest preference. Default is 9. |
| Step 8 | cor { incoming \| outgoing } cor-list-name Example: Router(config-ephone-dn)# cor incoming corlist1 | Applies a
                                             				class of restriction (COR) to the dial peers associated with an extension. COR
                                             				specifies which incoming dial peer can use which outgoing dial peer to make a
                                             				call. Each dial peer can be provisioned with an incoming and an outgoing COR
                                             				list. For
                                             				information about COR, see Dial Peer Configuration on
                                                				  Voice Gateway Routers . |
| Step 9 | translate { called \| calling } translation-rule-tag Example: Router(config-ephone-dn)# translate called 1 | Selects an
                                             				existing translation rule and applies it to a calling number or a number that
                                             				has been called. This command enables the manipulation of numbers as part of a
                                             				dial plan to manage overlapping or nonconsecutive numbering schemes. called —Translates the called number. calling —Translates the calling number. translation-rule-tag —Unique sequence number of the
                                                   					 previously defined translation rule. Range is 1 to 2147483647. Note This
                                                         				  command requires that you have previously defined appropriate translation rules
                                                         				  using the voice
                                                               						translation-rule and rule commands. | Note | This
                                                         				  command requires that you have previously defined appropriate translation rules
                                                         				  using the voice
                                                               						translation-rule and rule commands. |
| Note | This
                                                         				  command requires that you have previously defined appropriate translation rules
                                                         				  using the voice
                                                               						translation-rule and rule commands. |
| Step 10 | loopback-dn dn-tag [ forward number-of-digits \| strip number-of-digits ]
                                                				  [ prefix prefix-digit-string ]
                                                				  [ suffix suffix-digit-string ]
                                                				  [ retry seconds ] [ auto-con ] [ codec { g711alaw \| g711ulaw }] Example: Router(config-ephone-dn)# loopback-dn 24 forward 15 prefix 415353.... | Enables
                                             				H.323 call transfer and call forwarding by using hairpin call routing for VoIP
                                             				endpoints that do not support Cisco-proprietary or H.450-based call-transfer
                                             				and call-forwarding. dn-tag— Unique sequence number that identifies the
                                                   					 ephone-dn that is being paired for loopback with the ephone-dn that is being
                                                   					 configured. The paired ephone-dn must be one that is already defined in the
                                                   					 system. forward number-of-digits —(Optional) Number of digits in
                                                   					 the original called number to forward to the other ephone-dn in the loopback-dn
                                                   					 pair. Range is 1 to 32. Default is to forward all digits. strip number-of-digits —(Optional) Number of leading
                                                   					 digits to be stripped from the original called number before forwarding to the
                                                   					 other ephone-dn in the loopback-dn pair. Range is 1 to 32. Default is to not
                                                   					 strip any digits. prefix prefix-digit-string —(Optional) Defines a string of
                                                   					 digits to add in front of the forwarded called number. Maximum number of digits
                                                   					 in the string is 32. Default is that no prefix is defined. suffix suffix-digit-string —(Optional) Defines a string of
                                                   					 digits to add to the end of the forwarded called number. Maximum number of
                                                   					 digits in the string is 32. Default is that no suffix is defined. If you add a
                                                   					 suffix that starts with the pound character (#), the string must be enclosed in
                                                   					 quotation marks. retry seconds —(Optional) Number of seconds to wait
                                                   					 before retrying the loopback target when it is busy or unavailable. Range is 0
                                                   					 to 32767. Default is that retry is disabled and appropriate call-progress tones
                                                   					 are passed to the call originator. auto-con —(Optional) Immediately connects the call
                                                   					 and provides in-band alerting while waiting for the far-end destination to
                                                   					 answer. Default is that automatic connection is disabled. codec —(Optional) Explicitly forces the G.711 A-law
                                                   					 or G.711 mu-law voice coding type to be used for calls that pass through the
                                                   					 loopback-dn. This overrides the G.711 coding type that is negotiated for the
                                                   					 call and provides conversion from mu-law to A-law, if needed. Default is that
                                                   					 Real-Time Transport Protocol (RTP) voice packets are passed through the
                                                   					 loopback-dn without considering the G.711 coding type negotiated for the calls. g711alaw— G.711 A-law, 64000 bits per second, for
                                                   					 T1. g711ulaw— G.711 mu-law, 64000 bits per second, for
                                                   					 E1. |
| Step 11 | end Example: Router(config-ephone-dn)# end | Exits to
                                             				privileged exec mode. |

| Note | Ephone-dns
                                                         				  used for loopback cannot be dual-line ephone-dns. |
|---|---|

| Note | This
                                                         				  command requires that you have previously defined appropriate translation rules
                                                         				  using the voice
                                                               						translation-rule and rule commands. |
|---|---|

| Use the show running-config or show telephony-service ephone-dn command to
                                          			 display ephone-dn configurations. |
|---|

| Feature
                                             					 Name | Cisco Unified CME Version | Feature
                                             					 Information |
|---|---|---|
| Loopback
                                             					 Call Routing | 2.0 | Loopback
                                             					 call routing was introduced. |