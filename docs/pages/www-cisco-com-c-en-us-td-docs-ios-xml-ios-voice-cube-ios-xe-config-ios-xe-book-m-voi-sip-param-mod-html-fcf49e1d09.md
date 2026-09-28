---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-sip-param-mod-html-fcf49e1d09
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-sip-param-mod.html
retrieved_at: 2026-08-16T15:46:29.161427+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: SIP Profiles

## Chapter: SIP Profiles

# SIP Profiles

## Overview

Protocol translation and repair are a key Cisco Unified Border Element (CUBE) function. CUBE can be deployed between two incompatible SIP devices to normalize messaging, ensuring end-to-end compatibility.

Service providers may have policies for which SIP messaging fields should be present (and the values they contain) before
                           a SIP call enters their network. Similarly, enterprises and small businesses may have policies for the information that can
                           enter or exit their networks for policy or security reasons from a service provider SIP trunk.

CUBE Session Initiation Protocol (SIP) profiles change SIP incoming or outgoing messages so that interoperability between incompatible
                           devices can be ensured.

You can configure SIP profiles with rules to add, remove, copy, or modify the SIP, Session Description Protocol (SDP), and
                           peer headers that enter or leave CUBE . The rules in a SIP profile configuration can also be tagged with a unique number. Tagging the rules allows you to insert
                           or delete rules at any position of the existing SIP profile configuration without deleting and reconfiguring the entire voice-class
                           sip profile.

In addition to network policy compliance, CUBE SIP profiles can be used to resolve incompatibilities between SIP devices inside the enterprise network. These are some of
                           the situations in which incompatibilities can arise:

A device rejects an unknown header (value or parameter) instead of ignoring it.

A device sends incorrect data in a SIP message.

A device does not implement (or implements incorrectly) protocol procedures.

A device expects an optional header value or parameter, or an optional protocol procedure that can be implemented in multiple
                                 ways.

A device sends a value or parameter that must be changed or suppressed before it leaves or enters the network.

Variations in the SIP standards on how to achieve certain functions.

The SIP profiles feature on CUBE provides a solution to these incompatibilities and customization issues.

SIP profiles can
                           		also be used to change a header name from the long form to the compact form.
                           		For example, From to f. This can be used as a way to reduce the length of a SIP
                           		message. By default, the device never sends the compact form of the SIP
                           		messages although it receives either the long or the short form.

### Feature Information

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature
                                             					 Name

Releases

Feature
                                             					 Information

SIP
                                             					 Profiles (for inbound messages)

Baseline Functionality

This feature
                                             					 modifies the following commands:

The inbound keyword
                                             					 was added to the sip-profiles and voice-class sip
                                                   						  profiles commands.

### Important
                           	 Characteristics of SIP Profiles

Given below are a
                              		few important notes for SIP Profiles:

Session
                                    			 Initiation Protocol (SIP) and Session Description Protocol (SDP) headers are
                                    			 supported. SDP can be either a standalone body or part of a Multipurpose
                                    			 Internet Mail Extensions (MIME) message.

The rules that are configured for an INVITE message are applied only to the first INVITE of a call. A special REINVITE keyword
                                    is used to manipulate subsequent INVITEs of a call.

Manipulation of SIP headers by outbound SIP profiles occurs as the last step before the message leaves the CUBE device; that is, after destination dial-peer matching has taken place. Changes to the SIP messages are not remembered or
                                    acted on by the CUBE application. The Content-length field is recalculated after the SIP Profiles rules are applied to the outgoing message.

If the ANY keyword is used in place of a header, it indicates that a rule must be applied to any message within the specified category.

SIP header modification can be cryptic. It can sometimes be easier to remove a header and add it back (with the new value),
                                    rather than modifying it.

To include '?' (question-mark) character as part of match-pattern or replace-pattern, you must press "Ctrl+v" keys and then
                                    type '?'. This is needed to treat ‘?’ as an input character itself instead of usual device help prompt.

Regex features like look-ahead , look-behind , operator , non capturing group , and quantifier brackets are not supported (for example, ?! , ?: , ?<= , | , {} , and so on).

For header values used to add, modify or copy a header:

If a whitespace occurs, the entire value must be included between double quotes. For example, “User-Agent: CISCO CUBE”

If double quotes occur, a back slash must prefix the double quotes. For example, “User-Agent: \”CISCO\” CUBE”

Basic regular expressions are supported.

If an incoming SIP message contains certain proprietary attributes, CUBE can copy these unsupported SDP attributes or lines from incoming leg to outgoing leg using a SIP profile rule.

The copy variable can be used in an outbound profile to add or modify the outgoing message.

Copy Variables u01 to u99 are shared by inbound and outbound SIP Profiles.

Inbound SIP Profile:

If the incoming message contains multiple instances of the same header, the header values are stored as a comma separated
                                    list, and this needs to be considered while modifying it.

Modification by an inbound SIP profile takes place before regular SIP call processing happens so that behavior of CUBE would be as if it received the message directly without modification.

If inbound dial peer matching fails as required information could not be extracted from headers (like Request-URI, Via, From
                                    or To) due to issues in them, global level sip-profile config is applied. An example is a request with invalid SIP-Req-URI.

After
                                    			 modification by inbound SIP Profiles, the parameters in SIP message might
                                    			 change, which might change the inbound dial-peer matched when actual dial-peer
                                    			 lookup is done.

In the register
                                    			 pass-through feature, there is only one dial-peer for register and response. So
                                    			 both register from phone and response from registrar would go through the same
                                    			 inbound sip profile under the dial-peer if any.

## Restrictions

Removal or addition of mandatory headers is not supported. You can only modify mandatory headers Mandatory SIP headers include
                                 To, From, Via, CSeq, Call-Id, and Max-Forwards. Mandatory SDP headers include v, o, s, t ,c, and m.

Addition or removal of entire Multipurpose Internet Mail Extensions (MIME) or (Session Description Protocol) SDP bodies from
                                 SIP messages is not supported.

Syntax checking is not performed on SIP messages after SIP profile rules have been applied. Changes that are specified in
                                 the SIP profile should result in valid SIP protocol exchanges.

The header length (including header name) after modification should not exceed 300 characters. Max header length for add value
                                 is approximately 220 characters. Max SDP length is 2048 characters. If any header length exceeds this maximum value after
                                 applying SIP profiles, then the profile is not applied.

If a header-name is changed to its compact form, further SIP profile rules cannot be applied on that header. Thus a SIP profile
                                 rule modifying a header name to its compact form must be the last rule on that header.

The "image" m-line attributes (m=image 16850 udptl t38) cannot be modified using SIP profiles. SIP profiles can be applied
                                 only on audio and video m-lines in SDP.

In a high-availability (HA) scenario, SIP profiles copy variable data is not check-pointed to standby.

Limitations and restrictions of outbound SIP profiles apply to inbound SIP profiles as well.

You cannot configure more than 99 variables for the SIP profiles copy option.

Once a SIP profile is configured using rule tag, you cannot add rules without tags in the same profile and conversely.

If a SIP profile is applied to modify the SDP content of a SIP message, CUBE does not increment the "o=" line version, which
                                 may cause ITSPs to disconnect the call. CUBE does not store the modified SDP after the application of the SIP profile.

Note that manipulation of SIP messages by outbound SIP profiles occurs as the final step before the outgoing message leaves
                                 the CUBE device, and occurs after destination dial-peer matching has taken place. Changes to SIP messages are not remembered
                                 or acted on by CUBE. The Content-length field is recalculated after SIP Profile rules are applied to outgoing messages.

## How to Configure
                        	 SIP Profiles

To use SIP Profiles, you must first configure the profile, then apply it either at the global (all dial-peers), tenant, or
                           dial-peer levels. After a SIP profile is configured, it can be applied as an inbound or outbound profile.

### Configure SIP Profile Rules Using Rule Tags

Configuring SIP profile rules using rule tags, allows you to perform the following tasks:

Add a new rule at a chosen position without having to replace the whole profile.

Modify a specific rule by specifying its rule tag.

Remove a rule by specifying only its rule tag.

Below are the rule tag behaviors that must be considered while using rule tags in a SIP profile configuration:

If a rule is added with the tag of an existing rule, then the existing rule is overwritten with the new rule.

For inserting a rule at the desired position, the SIP profile configuration should be in rule format. In case the SIP profile
                                    is in nonrule format, upgrade the SIP profiles to rule format before inserting a rule.

If a new rule is inserted, the new rule takes the position that is specified in before tag . The subsequent rules are incremented sequentially.

For example:

rule before 10 request INVITE sip-header From modify "(<.*:)(.*@)" "\1gateway@"

When a rule is removed, the tags that are associated with the subsequent rules remain unchanged.

If a rule is added to a vacant tag, the new rule gets associated with the vacant tag and the subsequent rules remain unchanged.

### Upgrade or Downgrade SIP Profile Configurations

You can upgrade SIP profile rules to include rule tags or downgrade to remove them.

### SUMMARY STEPS

- enable

- Enter the
                                 			 following to upgrade SIP profiles configurations to rule-format:

- voice sip sip-profiles upgrade

- Enter the
                                 			 following to downgrade SIP profiles configurations to non-rule format:

- voice sip sip-profiles downgrade

- end

### DETAILED STEPS

Step 1

enable

Enables
                                             				privileged EXEC mode.

Enter
                                                   					 your password if prompted.

Step 2

Enter the
                                          			 following to upgrade SIP profiles configurations to rule-format:

- voice sip sip-profiles upgrade

#### Example:

```
Device# voice sip sip-profiles upgrade
```

Upgrades all
                                             				SIP Profiles to rule-format configurations.

Step 3

Enter the
                                          			 following to downgrade SIP profiles configurations to non-rule format:

- voice sip sip-profiles downgrade

#### Example:

```
Device# voice sip sip-profiles downgrade
```

Downgrades all
                                             				SIP Profiles from rule-format configurations to non-rule format configurations.

Step 4

end

Exits
                                             				privileged EXEC mode.

#### What to do next

Now apply the SIP
                                 		  Profile as an inbound or outbound SIP profile.

### Configure a SIP Profile to Manipulate SIP Request or Response Headers

### SUMMARY STEPS

- enable

- configure terminal

- voice class sip-profiles profile-id

- Enter one of
                                 			 the following to add, remove, modify SIP headers:

- [rule x ] request message { sip-header | sdp-header } header-to-add add header-value-to-add

- [rule x ] request message { sip-header | sdp-header } header-to-remove remove

- [rule x ] request message { sip-header | sdp-header } header-to-modify modify header-value-to-match header-value-to-replace

- Enter one of
                                 			 the following to add, remove, or modify SIP response headers:

- [rule x ] response message [ method method-type ] { sip-header | sdp-header } header-to-add add header-value-to-add

- [rule x ] response message [ method method-type ] { sip-header | sdp-header } header-to-remove remove

- [rule x ] response message [ method method-type ] { sip-header | sdp-header } header-to-modify modify header-value-to-match header-value-to-replace

- end

### DETAILED STEPS

Step 1

enable

Enables
                                             				privileged EXEC mode.

Enter
                                                   					 your password if prompted.

Step 2

configure terminal

Enters global
                                             				configuration mode.

Step 3

voice class sip-profiles profile-id

#### Example:

```
Device(config)# voice class sip-profiles 10
```

Creates a SIP Profile and enters voice class configuration mode.

Step 4

Enter one of
                                          			 the following to add, remove, modify SIP headers:

- [rule x ] request message { sip-header | sdp-header } header-to-add add header-value-to-add

- [rule x ] request message { sip-header | sdp-header } header-to-remove remove

- [rule x ] request message { sip-header | sdp-header } header-to-modify modify header-value-to-match header-value-to-replace

Adds a SIP or SDP header to a SIP request.

Removes a SIP or SDP header from a SIP request.

Modifies a SIP or SDP header in a SIP request.

If the ANY is used, the rule is applied to the specified header when it appears in any message type.

When specifying a profile rule header value:

If a value includes a space, the entire value must be included between double quotes. For example, “User-Agent: CISCO CUBE”

When using double quotes in a value, delimit with a backslash.

Simple regular expressions are supported.

Step 5

Enter one of
                                          			 the following to add, remove, or modify SIP response headers:

- [rule x ] response message [ method method-type ] { sip-header | sdp-header } header-to-add add header-value-to-add

- [rule x ] response message [ method method-type ] { sip-header | sdp-header } header-to-remove remove

- [rule x ] response message [ method method-type ] { sip-header | sdp-header } header-to-modify modify header-value-to-match header-value-to-replace

Adds a SIP or SDP header to a SIP response.

Removes a SIP or SDP header from a SIP response.

Modifies a SIP or SDP header in a SIP response.

All notes in the previous step are applicable here.

Step 6

end

Exits to
                                             				privileged EXEC mode

### Processing Unsupported SDP Headers

To modify SDP headers that CUBE is not natively aware of, first configure SDP pass-through and then make the necessary modifications
                                 through the outbound dial-peer.

Configure CUBE
                                       				to pass-through custom SDP on in-leg.

Define rule to Copy relevant attributes from peer SDP on out leg.

Define rule to Add or Modify attributes in outbound SDP with copied data.

### SUMMARY STEPS

- enable

- configure terminal

- To enable copying of unsupported SDP attribute from incoming leg to outbound leg, you must enable one of the following commands:

In Global VoIP SIP configuration mode

In dial-peer configuration mode (The configuration is applied on the incoming dial-peer)

- voice class sip-profiles profile-id

- Enter one of
                                 			 the following to copy an unsupported SDP line or attribute from peer leg's SDP
                                 			 and add, modify, or remove in the outgoing SDP:

- [rule x ] {request/response} ANY peer-header sdp mline-index index COPY match-pattern copy-variable

- [rule x ] {request/response} ANY sdp-header mline-index index header-name ADD copy-variable

- [rule x ] {request/response} ANY sdp-header mline-index index header-name MODIFY copy-variable + replace-pattern

- [rule x ] { request/response} ANY sdp-header mline-index index header-name REMOVE

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device> enable
```

Enables
                                             				privileged EXEC mode.

Enter
                                                   					 your password if prompted.

Step 2

configure terminal

#### Example:

```
Device# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

To enable copying of unsupported SDP attribute from incoming leg to outbound leg, you must enable one of the following commands:

In Global VoIP SIP configuration mode

In dial-peer configuration mode (The configuration is applied on the incoming dial-peer)

#### Example:

```
Device(config)# voice service voip
Device(conf-voi-serv)# sip
Device(conf-serv-sip)# pass-thru content custom-sdp
```

#### Example:

```
Device(config)# dial-peer voice 2 voip
Device(config-dial-peer)# voice-class sip pass-thru content custom-sdp
```

Enables copying of unsupported SDP attributes per m-line to the peer leg so that it can be used in outgoing SIP messages.

Enabling this command does not enable the SDP Passthrough feature.

Step 4

voice class sip-profiles profile-id

#### Example:

```
Device(config)# voice class sip-profiles 10
```

Voice class sip-profile is configured on the outbound dial-peer or
                                             				as a global configuration.

Creates a
                                             				SIP Profile and enters voice class configuration mode.

Step 5

Enter one of
                                          			 the following to copy an unsupported SDP line or attribute from peer leg's SDP
                                          			 and add, modify, or remove in the outgoing SDP:

- [rule x ] {request/response} ANY peer-header sdp mline-index index COPY match-pattern copy-variable

- [rule x ] {request/response} ANY sdp-header mline-index index header-name ADD copy-variable

- [rule x ] {request/response} ANY sdp-header mline-index index header-name MODIFY copy-variable + replace-pattern

- [rule x ] { request/response} ANY sdp-header mline-index index header-name REMOVE

M-line Index
                                             				values:

0 - A
                                                   					 value of zero represents the session level.

1–6 - A value in the range of one to six represents the m-line number in SDP.

Copy:
                                             				Enables copying of SDP line or attribute from peer leg SDP.

Add: Enables
                                             				adding the copied SDP line or attribute in the outgoing SDP.

Modify:
                                             				Enables modifying SDP line or attribute in the outgoing SDP.

Remove:
                                             				Enables removing SDP line or attribute in the outgoing SDP.

Step 6

end

Exits to
                                             				privileged EXEC mode.

#### Example:
                              	 Configuring SIP Profile Rules (Attribute Passing)

```
rule 10 response ANY peer-header sdp mline-index 4 copy “(a=ixmap:0.*)” u01
rule 20 response ANY sdp-header mline-index 4 a=ixmap add “\u01”
```

#### Example:
                              	 Configuring SIP Profile Rules (Parameter Passing)

```
rule 30 response ANY peer-header sdp mline-index 2 copy "a=fmtp:126 .*(max-fps=....)" u04 
rule 40 response ANY sdp-header mline-index 2 a=fmtp:126 modify ";" ";\u04;"
```

#### Example:
                              	 Configuration to Remove an Attribute

```
rule 50 response ANY sdp-header mline-index 4 a=test REMOVE
```

### Use Non-standard SIP Headers in SIP Profiles

In addition to the standard set of headers available when creating SIP profile rules, it is possible to carry out a similar
                                 set of functions for any other non-standard header.

### SUMMARY STEPS

- enable

- configure terminal

- voice class sip-profiles profile-id

- Enter one of
                                 			 the following to add, copy, remove, or modify non-standard SIP request headers:

- [rule x ] request message sip-header non-standard-header-to-add add non-standard-header-value-to-add

- [rule x ] request message sip-header non-standard-header-to-copy copy non-standard-header-value-to-match copy-variable

- [rule x ] request message sip-header non-standard-header-to-remove remove ]

- [rule x ] request message { sip-header } non-standard-header-to-modify modify non-standard-header-value-to-match non-standard-header-value-to-replace

- Enter one of
                                 			 the following to add, copy, remove, or modify non-standard SIP response
                                 			 headers:

- [rule x ] response message [ method method-type ] sip-header non-standard-header-to-add add non-standard-header-value-to-add

- [rule x ] response message [ method method-type ] sip-header non-standard-header-to-copy copy non-standard-header-value-to-match copy-variable

- [rule x ] response message [ method method-type ] sip-header non-standard-header-to-remove remove

- [rule x ] response message [ method method-type ] sip-header non-standard-header-to-modify modify non-standard-header-value-to-match non-standard-header-value-to-replace

- end

### DETAILED STEPS

Step 1

enable

Enables
                                             				privileged EXEC mode.

Enter
                                                   					 your password if prompted.

Step 2

configure terminal

Enters global
                                             				configuration mode.

Step 3

voice class sip-profiles profile-id

#### Example:

```
Device(config)# voice class sip-profiles 10
```

Creates a SIP
                                             				Profiles and enters voice class configuration mode.

Step 4

Enter one of
                                          			 the following to add, copy, remove, or modify non-standard SIP request headers:

- [rule x ] request message sip-header non-standard-header-to-add add non-standard-header-value-to-add

- [rule x ] request message sip-header non-standard-header-to-copy copy non-standard-header-value-to-match copy-variable

- [rule x ] request message sip-header non-standard-header-to-remove remove ]

- [rule x ] request message { sip-header } non-standard-header-to-modify modify non-standard-header-value-to-match non-standard-header-value-to-replace

Adds a non-standard SIP header to a SIP request.

Copies a non-standard SIP header value to a copy variable.

Removes a non-standard SIP header from a SIP request.

Modifies a non-standard SIP header in a SIP request.

If the ANY message keyword is used, the rule is applied to the specified header when it appears in any message type.

For non-standard-header-value-to-add used to add a non-standard header, non-standard-header-value-to-match or non-standard-header-value-to-replace used to modify a non-standard header when specifying a profile rule header value:

If a value includes a space , the entire value must be included between double quotes. For example, “User-Agent: CISCO CUBE”

When using double quotes in a value, delimit with a backslash.

Simple regular expressions are supported.

Step 5

Enter one of
                                          			 the following to add, copy, remove, or modify non-standard SIP response
                                          			 headers:

- [rule x ] response message [ method method-type ] sip-header non-standard-header-to-add add non-standard-header-value-to-add

- [rule x ] response message [ method method-type ] sip-header non-standard-header-to-copy copy non-standard-header-value-to-match copy-variable

- [rule x ] response message [ method method-type ] sip-header non-standard-header-to-remove remove

- [rule x ] response message [ method method-type ] sip-header non-standard-header-to-modify modify non-standard-header-value-to-match non-standard-header-value-to-replace

Adds a non-standard header to a SIP response message.

Copies
                                                   					 contents from a non-standard SIP header to a SIP response.

Removes a non-standard header to a SIP response.

Modifies a non-standard SIP header in a SIP response.

All
                                                   					 notes from the previous step are applicable here.

Step 6

end

Exits to
                                             				privileged EXEC mode

### Configure a SIP Profile as an Outbound Profile

### SUMMARY STEPS

- enable

- configure terminal

- Apply the SIP
                                 			 profile to a dial peer:

- voice-class sip profiles profile-id in the dial-peer configuration mode.

- sip-profiles profile-id in the global VoIP configuration mode

- end

### DETAILED STEPS

Step 1

enable

Enables
                                             				privileged EXEC mode.

Enter
                                                   					 your password if prompted.

Step 2

configure terminal

Enters global
                                             				configuration mode.

Step 3

Apply the SIP
                                          			 profile to a dial peer:

- voice-class sip profiles profile-id in the dial-peer configuration mode.

- sip-profiles profile-id in the global VoIP configuration mode

#### Example:

```
!Applying SIP profiles to one dial peer only
Device (config)# dial-peer voice 10 voip Device (config-dial-peer)# voice-class sip profiles 30 Device (config-dial-peer)# end
```

#### Example:

```
! Applying SIP profiles globally
Device(config)# voice service voip Device (config-voi-serv)# sip Device (config-voi-sip)# sip-profiles 20 Device (config-voi-sip)# end
```

Step 4

end

Exits to
                                             				privileged EXEC mode .

### Configure a SIP Profile as an Inbound Profile

You can configure a SIP profile as an inbound profile applied globally or to multiple inbound dial peers. Inbound SIP profiles
                                 feature must be enabled before applying it.

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- sip

- sip-profiles
                                       				  inbound

- Apply the
                                 			 SIP profile to a dial peer:

- voice-class sip
                                          					 profiles profile-id inbound in the dial-peer configuration mode.

- sip-profiles profile-id inbound in the global VoIP configuration mode

- end

### DETAILED STEPS

Step 1

enable

Enables
                                             				privileged EXEC mode.

Enter
                                                   					 your password if prompted.

Step 2

configure terminal

Enters
                                             				global configuration mode.

Step 3

voice service voip

#### Example:

```
Device(config)# voice service voip
```

Enters
                                             				global VoIP configuration mode.

Step 4

sip

#### Example:

```
Device(config-voi-serv)# sip
```

Enters
                                             				global VoIP SIP configuration mode.

Step 5

sip-profiles
                                                				  inbound

#### Example:

```
Device(config-voi-sip)# sip-profiles inbound
```

Enables
                                             				inbound SIP profiles feature.

Step 6

Apply the
                                          			 SIP profile to a dial peer:

- voice-class sip
                                                   					 profiles profile-id inbound in the dial-peer configuration mode.

- sip-profiles profile-id inbound in the global VoIP configuration mode

#### Example:

```
!Applying SIP profiles to one dial peer only
Device (config)# dial-peer voice 10 voip Device (config-dial-peer)# voice-class sip profiles 30 inbound Device (config-dial-peer)# end
```

#### Example:

```
! Applying SIP profiles globally
Device(config)# voice service voip Device (config-voi-serv)# sip Device (config-voi-sip)# sip-profiles 20 inbound Device (config-voi-sip)# end
```

Step 7

end

Exits to
                                             				privileged EXEC mode

## Supported SIP Messages

This section provides the CLI options of the SIP messages that you can process with the CUBE SIP profiles feature.

SIP Requests

Supported SIP requests are the following:

```
ACK        sip ack
  ANY        any sip request
  BYE        sip bye
  CANCEL     sip cancel
  COMET      sip comet
  INFO       sip info
  INVITE     sip invite
  NOTIFY     sip notify
  OPTIONS    sip options
  PRACK      sip prack
  PUBLISH    sip publish
  REFER      sip refer
  REGISTER   sip register
  REINVITE   sip reinvite
  SUBSCRIBE  sip subscribe
  UPDATE     sip info
```

SIP Responses

Supported SIP responses are the following:

```
100  Response code 100
  180  Response code 180
  181  Response code 181
  182  Response code 182
  183  Response code 183
  200  Response code 200
  202  Response code 202
  300  Response code 300
  301  Response code 301
  302  Response code 302
  305  Response code 305
  380  Response code 380
  400  Response code 400
  401  Response code 401
  402  Response code 402
  403  Response code 403
  404  Response code 404
  405  Response code 405
  406  Response code 406
  407  Response code 407
  408  Response code 408
  409  Response code 409
  410  Response code 410
  412  Response code 412
  413  Response code 413
  414  Response code 414
  415  Response code 415
  416  Response code 416
  417  Response code 417
  420  Response code 420
  421  Response code 421
  422  Response code 422
  423  Response code 423
  480  Response code 480
  481  Response code 481
  482  Response code 482
  483  Response code 483
  484  Response code 484
  485  Response code 485
  486  Response code 486
  487  Response code 487
  488  Response code 488
  489  Response code 489
  491  Response code 491
  493  Response code 493
  500  Response code 500
  501  Response code 501
  502  Response code 502
  503  Response code 503
  504  Response code 504
  505  Response code 505
  513  Response code 513
  580  Response code 580
  600  Response code 600
  603  Response code 603
  604  Response code 604
  606  Response code 606
  ANY  Any Response
```

SIP Headers

Supported SIP headers are the following:

Non-standard SIP headers are also supported.

```
Accept-Contact            SIP header Accept-Contact
  Accept-Encoding           SIP header Accept-Encoding
  Accept-Header             SIP header Accept
  Accept-Language           SIP header Accept-Language
  Accept-Resource-Priority  SIP header Accept-Resource-Priority
  Alert-Info                SIP header Alert-Info
  Allow-Events              SIP header Allow-Events
  Allow-Header              SIP header Allow
  Also                      SIP header Also
  Authorization             SIP header Authorization
  CC-Diversion              SIP header CC-Diversion
  CC-Redirect               SIP header CC-Redirect
  CSeq                      SIP header CSeq
  Call-ID                   SIP header Call-ID
  Call-Info                 SIP header Call-Info
  Cisco-Gcid                SIP header Cisco-Gcid
  Cisco-Guid                SIP header Cisco-Guid
  Contact                   SIP header contact
  Content-Disposition       SIP header Content-Disposition
  Content-Encoding          SIP header Content-Encoding
  Content-Id                SIP header Content-Id
  Content-Length            SIP header Content-Length
  Content-Type              SIP header Content-Type
  Date                      SIP header Date
  Diversion                 SIP header Diversion
  Event                     SIP header Event
  Expires                   SIP header Expires
  From                      SIP header FROM
  History-Info              SIP header History-Info
  Location                  SIP header Location
  MIME-Version              SIP header MIME-Version
  Max-Forwards              SIP header Max-Forwards
  Min-Expires               SIP header Min-Expires
  Min-SE                    SIP header Min-SE
  Orig-dial-plan            SIP header Orig-dial-plan
  P-Asserted-Identity       SIP header P-Asserted-Identity
  P-Preferred-Identity      SIP header P-Preferred-Identity
  P-RTP-Stat                SIP Header P-RTP-Stat
  Privacy                   SIP header Privacy
  Proxy-Authenticate        SIP header Proxy-Authenticate
  Proxy-Authorization       SIP header Proxy-Authorization
  Proxy-Require             SIP header Proxy-Require
  Rack                      SIP header Rack
  Reason                    SIP header Reason
  Record-Route              SIP header Record-Route
  Refer-To                  SIP header Refer-To
  Referred-By               SIP header Referred-By
  Reject-Contact            SIP header Reject-Contact
  Remote-Party-ID           SIP header Remote-Party-ID
  Replaces                  SIP header Replaces
  Request-Disposition       SIP header Request-Disposition
  Requested-By              SIP header Requested-By
  Require                   SIP header Require
  Resource-Priority         SIP header Resource-Priority
  Retry-After               SIP header Retry-After
  Route                     SIP header Route
  Rseq                      SIP header Rseq
  SIP-ETag                  SIP header SIP-ETag
  SIP-If-Match              SIP header SIP-If-Match
  SIP-Req-URI               SIP Request URI
  SIP-StatusLine            SIP Status-Line
  Server                    SIP header Server
  Session-Expires           SIP header Session-Expires
  Session-Header            SIP header Session
  Session-ID                SIP header Session ID
  Subscription-State        SIP header Subscription-State
  Supported                 SIP header Supported
  Term-dial-plan            SIP header Term-dial-plan
  Timestamp                 SIP header Timestamp
  To                        SIP header TO
  Unsupported               SIP header Unsupported
  User-Agent                SIP header User-Agent
  Via                       SIP header Via
  WORD                      Any other SIP header name
  WWW-Authenticate          SIP header WWW-Authenticate
  Warning                   SIP header Warning
```

SDP Headers

Supported SDP headers are the following:

```
Attribute              SDP header Attribute
  Audio-Attribute        SDP Audio Attribute
  Audio-Bandwidth-Info   SDP Audio Bandwidth Info
  Audio-Connection-Info  SDP Audio Connection Info
  Audio-Encryption-Key   SDP Audio Encript key
  Audio-Media            SDP Audio Media
  Audio-Session-Info     SDP Audio Session Info
  Bandwidth-Key          SDP header Bandwidth-Key
  Connection-Info        SDP header Connection-Info
  Email-Address          SDP header Email-Address
  Encrypt-Key            SDP header Encrypt-Key
  Phone-Number           SDP header Phone-Number
  Repeat-Times           SDP header Repeat-Times
  Session-Info           SDP header Session-info
  Session-Name           SDP header Session-Name
  Session-Owner          SDP header Session
  Time-Adjust-Key        SDP header Time-Adjust-Key
  Time-Header            SDP header Time
  Url-Descriptor         SDP header Url-Descriptor
  Version                SDP Version
  Video-Attribute        SDP Video Attribute
  Video-Bandwidth-Info   SDP Video Bandwidth Info
  Video-Connection-Info  SDP Video Connection Info
  Video-Encryption-Key   SDP Video Encryption Key
  Video-Media            SDP Video Media
  Video-Session-Info     SDP Video Session Info
  mline-index            M-Line index for SDP Line
```

## Verify SIP Profiles

### SUMMARY STEPS

- show dial-peer voice id | include
                                    				  profile

### DETAILED STEPS

show dial-peer voice id | include
                                             				  profile

Displays information related to SIP profiles configured on the
                                          				specified dial peer.

### Example:

```
Device# show dial-peer voice 10 | include sip profile voice class sip profiles = 11
        voice class sip profiles inbound = 10
```

## Troubleshoot SIP Profiles

The following debugs can also be used:

debug ccsip info

debug ccsip feature sip-profiles

debug ccsip error

### SUMMARY STEPS

- debug ccsip all

### DETAILED STEPS

debug ccsip all

### Example:

```
Device# debug ccsip all …
Oct 12 06:51:53.619: //-1/735085DC8F3D/SIP/Info/sipSPIGetShrlPeer: 
                     Try match incoming dialpeer for Calling number:  
                     : sippOct 12 06:51:53.619:  
                     //-1/735085DC8F3D/SIP/Info/sipSPIGetCallConfig:  
                     Peer tag 2 matched for incoming call 
Oct 12 06:51:53.619: //-1/xxxxxxxxxxxx/SIP/Info/sipSPIGetCallConfig: voice class SIP profiles tag is set : 1 Oct 12 06:51:53.619: //-1/735085DC8F3D/SIP/Info/sipSPIGetCallConfig:  
                     Not using Voice Class Codec
Oct 12 06:51:53.619: //-1/735085DC8F3D/SIP/Info/sipSPIGetCallConfig:  
                     xcoder high-density disabled
Oct 12 06:51:53.619: //-1/735085DC8F3D/SIP/Info/sipSPIGetCallConfig:  
                     Flow Mode set to FLOW_THROUGH
```

### Example:

```
Device# debug ccsip all
…
Oct 12 06:51:53.647: //-1/xxxxxxxxxxxx/SIP/Info/
sip_profiles_application_change_sdp_line:
New SDP header is added : b=AS: 1600
Oct 12 06:51:53.647: //-1/xxxxxxxxxxxx/SIP/Info/
sip_profiles_update_content_length:
Content length header before modification :
Content-Length: 290
Oct 12 06:51:53.647: //-1/xxxxxxxxxxxx/SIP/Info/
sip_profiles_update_content_length:
Content length header after modification :
Content-Length: 279
```

### Examples: Adding, Modifying, Removing SIP Profiles

## Example: Adding a SIP, SDP,
                        	 or Peer Header

### Example: Adding
                              		  "b=AS:4000" SDP header to the video-media Header of the INVITE SDP Request
                              		  Messages

```
Device(config)# voice class sip-profiles 10 Device(config-class)# request INVITE sdp-header Video-Bandwidth-Info add "b=AS:4000" Device(config-class)# end
```

### Example: Adding
                              		  "b=AS:4000" SDP header to the video-media Header of the INVITE SDP Request
                              		  Messages in rule format

```
Device(config)# voice class sip-profiles 10 Device(config-class)# rule 1 request INVITE sdp-header Video-Bandwidth-Info add "b=AS:4000" Device(config-class)# end
```

### Example: Adding
                              		  the Retry-After Header to the SIP 480 Response Messages

```
Device(config)# voice class sip-profiles 20 Device(config-class)# response 480 sip-header Retry-After add “Retry-After: 60” Device(config-class)# end
```

### Example: Adding
                              		  the Retry-After Header to the SIP 480 Response Messages in rule format

```
Device(config)# voice class sip-profiles 20 Device(config-class)# rule 1 response 480 sip-header Retry-After add “Retry-After: 60” Device(config-class)# end
```

### Example: Adding
                              		  "User-Agent: SIP-GW-UA" to the User-Agent Field of the 200 Response SIP
                              		  Messages

```
Device(config)# voice class sip-profiles 40 Device(config-class)# response 200 sip-header User-Agent add "User-Agent: SIP-GW-UA" Device(config-class)# end
```

### Example: Adding
                              		  "User-Agent: SIP-GW-UA" to the User-Agent Field of the 200 Response SIP
                              		  Messages in rule format

```
Device(config)# voice class sip-profiles 40 Device(config-class)# rule 1 response 200 sip-header User-Agent add "User-Agent: SIP-GW-UA" Device(config-class)# end
```

### Example: Adding
                              		  "a=ixmap:0 ping" in M-Line number 4 of the INVITE SDP Request Messages

```
Device(config)# voice class sip-profiles 10 Device(config-class)# request INVITE sdp-header mline-index 4 a=ixmap add "a=ixmap:0 ping" Device(config-class)# end
```

## Example: Modifying
                        	 a SIP, SDP, or Peer Header

### Example:
                              		  Modifying SIP-Req-URI of the Header of the INVITE and RE-INVITE SIP Request
                              		  Messages to include "user=phone"

```
Device(config)# voice class sip-profiles 30 Device(config-class)# request INVITE sip-header SIP-Req-URI modify "; SIP/2.0" ";user=phone SIP/2.0" Device(config-class)# request RE-INVITE sip-header SIP-Req-URI modify "; SIP/2.0" ";user=phone SIP/2.0" Device(config-class)# end
```

### Example:
                              		  Modifying SIP-Req-URI of the Header of the INVITE and RE-INVITE SIP Request
                              		  Messages to include "user=phone" in rule format

```
Device(config)# voice class sip-profiles 30 Device(config-class)# rule 1 request INVITE sip-header SIP-Req-URI modify "; SIP/2.0" ";user=phone SIP/2.0" Device(config-class)# rule 2 request RE-INVITE sip-header SIP-Req-URI modify "; SIP/2.0" ";user=phone SIP/2.0" Device(config-class)# end
```

### Modify the
                              		  From Field of a SIP INVITE Request Messages to “gateway@gw-ip-address”
                              		  Format

For example,
                              		  modify 2222000020@10.13.24.7 to gateway@10.13.24.7

```
Device(config)# voice class sip-profiles 20 Device(config-class)# request INVITE sip-header From modify "(<.*:)(.*@)" "\1gateway@"
```

### Modify the
                              		  From Field of a SIP INVITE Request Messages to “gateway@gw-ip-address” Format
                              		  in rule format

For example,
                              		  modify 2222000020@10.13.24.7 to gateway@10.13.24.7

```
Device(config)# voice class sip-profiles 20 Device(config-class)# rule 1 request INVITE sip-header From modify "(<.*:)(.*@)" "\1gateway@"
```

### Replace
                              		  "CiscoSystems-SIP-GW-UserAgent" with "-" in the Originator Header of the SDP in
                              		  INVITE Request Messages

```
Device(config)# voice class sip-profiles 10 Device(config-class)# request INVITE sdp-header Session-Owner modify "CiscoSystems-SIP-GW-UserAgent“ "-"
```

### Replace
                              		  "CiscoSystems-SIP-GW-UserAgent" with "-" in the Originator Header of the SDP in
                              		  INVITE Request Messages in rule format

```
Device(config)# voice class sip-profiles 10 Device(config-class)# rule 1 request INVITE sdp-header Session-Owner modify "CiscoSystems-SIP-GW-UserAgent“ "-"
```

### Convert "sip
                              		  uri" to "tel uri" in Req-URI, From and To Headers of SIP INVITE Request
                              		  Messages

For example,
                              		  modify sip:2222000020@9.13.24.6:5060” to “tel:2222000020

```
Device(config)# voice class sip-profiles 40 Device(config-class)# request INVITE sip-header SIP-Req-URI modify "sip:(.*)@[^ ]+" "tel:\1" Device(config-class)# request INVITE sip-header From modify "<sip:(.*)@.*>" "<tel:\1>" Device(config-class)# request INVITE sip-header To modify "<sip:(.*)@.*>" "<tel:\1>"
```

### Convert "sip
                              		  uri" to "tel uri" in Req-URI, From and To Headers of SIP INVITE Request
                              		  Messagesin rule format

For example,
                              		  modify sip:2222000020@9.13.24.6:5060” to “tel:2222000020

```
Device(config)# voice class sip-profiles 40 Device(config-class)# rule 1 request INVITE sip-header SIP-Req-URI modify "sip:(.*)@[^ ]+" "tel:\1" Device(config-class)# rule 2 request INVITE sip-header From modify "<sip:(.*)@.*>" "<tel:\1>" Device(config-class)# rule 3 request INVITE sip-header To modify "<sip:(.*)@.*>" "<tel:\1>"
```

### Example:
                              		  Change the Audio Attribute Ptime:20 to Ptime:30

Inbound ptime:

```
a=ptime:20
```

Outbound ptime:

```
a=ptime:30
```

```
Device(config)# voice class sip-profiles 103 Device(config-class)# request ANY sdp-header Audio-Attribute modify "a=ptime:20" "a=ptime:30"
```

### Example:
                              		  Modify Audio direction "Audio-Attribute"

Some service
                              		  providers or customer equipment reply to delay offer invites and or re-invites
                              		  that contain a=inactive with a=inactive, a=recvonly, or a=sendonly. This can
                              		  create an issue when trying to transfer or retrieve a call from hold. The
                              		  result is normally one-way audio after hold or resume or transfer or moh is not
                              		  heard. To resolve this issue changing the audio attribute to Sendrecv prevents
                              		  the provider from replaying back with a=inactive, a=recvonly, or a=sendonly.

Case 1:

```
Inbound Audio-Attribute

a=inactive

Outbound Audio-Attribute

a=sendrecv
```

Case 2:

```
Inbound Audio-Attribute

a=recvonly

Outbound Audio-Attribute

a=sendrecv
```

Case 3

```
Inbound Audio-Attribute

a=sendonly

Outbound Audio-Attribute

a=sendrecv
```

```
Device(config)# voice class sip-profiles 104 Device(config-class)# request any sdp-header Audio-Attribute modify "a=inactive" "a=sendrecv" Device(config-class)# request any sdp-header Audio-Attribute modify "a=recvonly" "a=sendrecv" Device(config-class)# request any sdp-header Audio-Attribute modify "a=sendonly" "a=sendrecv" Device(config-class)# response any sdp-header Audio-Attribute modify "a=inactive" "a=sendrecv" Device(config-class)# response any sdp-header Audio-Attribute modify "a=recvonly" "a=sendrecv" Device(config-class)# response any sdp-header Audio-Attribute modify "a=sendonly" "a=sendrecv"
```

### Example:
                              		  Modifying Packetization Mode in a=fmtp line of M-line number 2 of the INVITE
                              		  SDP Request Messages

```
Device(config)# voice class sip-profiles 10 Device(config-class)# request INVITE sdp-header mline-index 2 a=fmtp modify "packetization-mode=1" "packetization-mode=0" Device(config-class)# end
```

## Example: Remove a
                        	 SIP, SDP, or Peer Header

### Remove
                              		  Cisco-Guid SIP header from all Requests and Responses

```
Device(config)# voice class sip-profiles 20 Device(config-class)# request ANY sip-header Cisco-Guid remove Device(config-class)# response ANY sip-header Cisco-Guid remove Device(config-class)# end
```

### Remove Server
                              		  Header from 100 and 180 SIP Response Messages

```
Device(config)# voice class sip-profiles 20 Device(config-class)# response 100 sip-header Server remove Device(config-class)# response 180 sip-header Server remove Device(config-class)# end
```

### Removing a
                              		  SIP Profile rule in rule format configuration

SIP Profile
                              		  configuration in rule format

```
Device(config)# voice class sip-profiles 10 Device(config-class)# rule 1 request any sdp-header Audio-Attribute modify "a=inactive" "a=sendrecv" Device(config-class)# rule 2 request any sdp-header Audio-Attribute modify "a=recvonly" "a=sendrecv" Device(config-class)# end
```

Removing the rule
                              		  using rule tag

```
Device(config)# voice class sip-profiles 10 Device(config-class)# no rule 1 Device(config-class)# end
```

Once the rule is
                              		  removed, the tag belonging to the removed rule remains vacant. The tags
                              		  associated with the subsequent rules are unchanged.

The SIP Profile
                              		  configuration after removing the rule

```
Device(config)# voice class sip-profiles 10 Device(config-class)# rule 2 request any sdp-header Audio-Attribute modify "a=recvonly" "a=sendrecv" Device(config-class)# end
```

### Example: Removing "a=ixmap" in M-Line number 4 of the INVITE SDP
                              		  Request Messages

```
Device(config)# voice class sip-profiles 10 Device(config-class)# request INVITE sdp-header mline-index 4 a=ixmap REMOVE Device(config-class)# end
```

## Example: Inserting
                        	 SIP Profile Rules

### Example:
                              		  Inserting a SIP Profile Rule

Inserting a SIP
                              		  profile rule to a SIP Profile

```
Device(config)# voice class sip-profiles 1 Device(config-class)# rule 1 request INVITE sip-header Contact Modify “(.*)” “\1;temp=xyz” Device(config-class)# rule 2 request INVITE sip-header Supported Add “Supported: ” Device(config-class)# rule before 2 request INVITE sip-header To Modify “(.*)” “\1;temp=abc”
```

The SIP Profile
                              		  after inserting the new rule

```
Device(config)# voice class sip-profiles 1 Device(config-class)# rule 1 request INVITE sip-header Contact Modify “(.*)” “\1;temp=xyz” Device(config-class)# rule 2 request INVITE sip-header To Modify “(.*)” “\1;temp=abc” Device(config-class)# rule 3 request INVITE sip-header Supported Add “Supported: ”
```

## Example: Upgrading
                        	 and Downgrading SIP Profiles automatically

### Upgrading SIP
                              		  Profiles to rule-format

The following is a snippet from show running-config command showing the SIP profiles in non-rule
                              		  format:

```
Device#show running-config | section profiles 1
voice class sip-profiles 1
 request INVITE sip-header Contact Modify “(.*)” “\1;temp=xyz”
 request INVITE sip-header Supported Add “Supported: ”
```

Execute the following command in EXEC (#) mode to upgrade the SIP
                              		  Profiles to rule-format:

```
Device# voice sip sip-profiles upgrade
```

The following is a
                              		  snippet from show running-config command showing the SIP profiles after
                              		  upgrading to rule-format:

```
Device#show running-config | section profiles 1

voice class sip-profiles 1
 rule 1 request INVITE sip-header Contact Modify “(.*)” “\1;temp=xyz”
 rule 2 request INVITE sip-header Supported Add “Supported: ”
```

### Downgrading
                              		  SIP Profiles to non-rule format

The following is a
                              		  snippet from show running-config command showing SIP profiles in rule-format:

```
Device#show running-config | section profiles 1

voice class sip-profiles 1
 rule 1 request INVITE sip-header Contact Modify “(.*)” “\1;temp=xyz”
 rule 2 request INVITE sip-header Supported Add “Supported: ”
```

Execute the following command in EXEC(#) mode to downgrade SIP
                              		  Profiles to non-rule format:

```
Device# voice sip sip-profiles downgrade
```

The following is a
                              		  snippet from show running-config command showing SIP profiles after
                              		  downgrading to non-rule format:

```
Device#show running-config | section profiles 1

voice class sip-profiles 1
 request INVITE sip-header Contact Modify “(.*)” “\1;temp=xyz”
 request INVITE sip-header Supported Add “Supported: ”
```

## Example: Modifying
                        	 Diversion Headers

### Example:
                              		  Modify Diversion Headers from Three-Digit Extensions to Ten Digits.

Most North American service providers require a ten digit diversion header. Prior to Call manager 8.6, Call manager would
                              only send the extension in the diversion header. A SIP profile can be used to make the diversion header ten digits.

Call manager
                              		  version 8.6 and above has the field “Redirecting Party Transformation CSS”
                              		  which lets you expand the diversion header on the call manager.

The SIP profile
                              		  will look for a diversion header containing "<sip:5..." , where ... stands
                              		  for the three-digit extension and then concatenates 9789365 with these three
                              		  digits.

Original Diversion
                              		  Header:

```
Diversion:<sip:5100@161.44.77.193>;privacy=off;reason=unconditional;counter=1;screen=no
```

Modified Diversion
                              		  Header:

```
Diversion: <sip:9789365100@10.86.176.19>;privacy=off;reason=unconditional;counter=1;screen=no
```

```
Device(config)# voice class sip-profiles 101 Device(config-class)# request Invite sip-header Diversion modify "<sip:5(...)@" "<sip:9789365\1@" Device(config-class)# end
```

### Example:
                              		  Create a Diversion header depending on the area code in the From field

Most service
                              		  providers require a redirected call to have a diversion header that contains a
                              		  full 10 digit number that is associated with a SIP trunk group. Sometimes, a
                              		  SIP trunk may cover several different area codes, states, and geographic
                              		  locations. In this scenario, the service provider may require a specific number
                              		  to be placed in the diversion header depending on the calling party number.

In the below
                              		  example, if the From field has an area code of 978 "<sip:978", the SIP
                              		  profile leaves the From field as is and adds a diversion header.

```
Device(config)# voice class sip-profiles 102 Device(config-class)# request INVITE sip-header From modify "From:(.*)<sip:978(.*)@(.*)" "From:\1<sip:978\2@\3\x0ADiversion: <sip:9789365000@10.86.176.19:5060;privacy=off;reason=unconditional;counter=1;screen=no"
```

The below
                              		  diversion header is added. There was no diversion header before this was added:

```
Diversion: <sip:9789365000@10.86.176.19:5060;transport=udp>"
```

## Example: Sample
                        	 SIP Profile Application on SIP Invite Message

The SIP profile
                              		  configured is below:

The SIP INVITE
                              		  message before the SIP profile has been applied is show below:

```
voice class sip-profiles 1
  request INVITE sdp-header Audio-Bandwidth-Info add "b=AS:1600“
  request ANY sip-header Cisco-Guid remove
  request INVITE sdp-header Session-Owner modify "CiscoSystems-SIP-GW-UserAgent" "-“
```

```
INVITE sip:2222000020@9.13.40.250:5060 SIP/2.0
Via: SIP/2.0/UDP 9.13.40.249:5060;branch=z9hG4bK1A203F
From: "sipp " <sip:1111000010@9.13.40.249>;tag=F11AE0-1D8D
To: <sip:2222000020@9.13.40.250>
Date: Mon, 29 Oct 2007 19:02:04 GMT
Call-ID: 4561B116-858811DC-804DEF2E-4CF2D71B@9.13.40.249 Cisco-Guid: 1163870326-2240287196-2152197934-1290983195
Content-Length: 290 v=0 o=CiscoSystemsSIP-GW-UserAgent 6906 8069 IN IP4 9.13.40.249
s=SIP Call
c=IN IP4 9.13.40.249
t=0 0
m=audio 17070 RTP/AVP 0
c=IN IP4 9.13.40.249
a=rtpmap:0 PCMU/8000
a=ptime:20
```

The SIP INVITE message after the SIP profile has been applied is shown below:

The Cisco-Guid has been removed.

CiscoSystemsSIP-GW-UserAgent has been replaced with -.

The Audio-Bandwidth SDP header has been added with the value b=AS:1600.

```
INVITE sip:2222000020@9.13.40.250:5060 SIP/2.0
Via: SIP/2.0/UDP 9.13.40.249:5060;branch=z9hG4bK1A203F
From: "sipp " <sip:1111000010@9.13.40.249>;tag=F11AE0-1D8D
To: <sip:2222000020@9.13.40.250>
Date: Mon, 29 Oct 2007 19:02:04 GMT
Call-ID: 4561B116-858811DC-804DEF2E-4CF2D71B@9.13.40.249
Content-Length: 279

v=0 o=- 6906 8069 IN IP4 9.13.40.249
s=SIP Call
c=IN IP4 9.13.40.249
t=0 0
m=audio 17070 RTP/AVP 0
c=IN IP4 9.13.40.249
a=rtpmap:0 PCMU/8000
a=ptime:20 b=AS:1600
```

## Example: Sample
                        	 SIP Profile for Non-Standard SIP Headers

It is possible to add, copy, modify or delete any SIP header.

```
voice class sip-profiles 1 request INVITE sip-header X-Cisco-Recording-Participant copy "sip:(.*)@" u01 
 request INVITE sip-header X-Cisco-Recording-Participant modify "sip:sipp@" "sip:1000@"  
 request INVITE sip-header My-Info add "My-Info: MF Call" 
 request INVITE sip-header My-Info remove
```

## Example: Copy User-to-User Information from REFER Message

When a call is transferred using REFER, user-to-user content from the originating message is not automatically copied to the
                              triggered INVITE. This example illustrates how SIP profiles can be used to capture this information and pass it to the outbound
                              INVITE, where it is added as a new header.

SIP profile 1210 applied to the incoming dial-peer copies the user-to-user information to a temporary header (x-user). This
                              header is passed to the outbound leg where SIP profile 1211 extracts this information and uses it to create the new INVITE
                              User-to-user header before removing the temporary x-user header.

To ensure that the x-user header is passed to the INVITE message, either use a sip-copylist that is applied to both dial-peers
                              or enable unsupported header pass-through.

```
voice class sip-profiles 1210 request REFER sip-header Refer-To copy "Refer-To:.*User-to-User=(.*)>" u03
request REFER sip-header x-user add "x-user: TEST"
request REFER sip-header x-user modify "x-user: (.*)" "x-user: \u03"
```

```
voice class sip-profiles 1211 request INVITE sip-header x-user copy "x-user: (.*)" u05
request INVITE sip-header User-to-User add "User-to-User: TEST"
request INVITE sip-header User-to-User modify "User-to-User: (.*)" "User-to-User: \u05"
request INVITE sip-header x-user remove
```

| Feature
                                             					 Name | Releases | Feature
                                             					 Information |
|---|---|---|
| SIP
                                             					 Profiles (for inbound messages) | Baseline Functionality | This feature
                                             					 modifies the following commands: The inbound keyword
                                             					 was added to the sip-profiles and voice-class sip
                                                   						  profiles commands. |

| Note | Regex features like look-ahead , look-behind , operator , non capturing group , and quantifier brackets are not supported (for example, ?! , ?: , ?<= , \| , {} , and so on). |
|---|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable | Enables
                                             				privileged EXEC mode. Enter
                                                   					 your password if prompted. |
| Step 2 | Enter the
                                          			 following to upgrade SIP profiles configurations to rule-format: voice sip sip-profiles upgrade Example: In EXEC(#) mode: Device# voice sip sip-profiles upgrade | Upgrades all
                                             				SIP Profiles to rule-format configurations. |
| Step 3 | Enter the
                                          			 following to downgrade SIP profiles configurations to non-rule format: voice sip sip-profiles downgrade Example: In EXEC(#) mode: Device# voice sip sip-profiles downgrade | Downgrades all
                                             				SIP Profiles from rule-format configurations to non-rule format configurations. |
| Step 4 | end | Exits
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable | Enables
                                             				privileged EXEC mode. Enter
                                                   					 your password if prompted. |
| Step 2 | configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice class sip-profiles profile-id Example: Device(config)# voice class sip-profiles 10 | Creates a SIP Profile and enters voice class configuration mode. |
| Step 4 | Enter one of
                                          			 the following to add, remove, modify SIP headers: [rule x ] request message { sip-header \| sdp-header } header-to-add add header-value-to-add [rule x ] request message { sip-header \| sdp-header } header-to-remove remove [rule x ] request message { sip-header \| sdp-header } header-to-modify modify header-value-to-match header-value-to-replace | According
                                          			 to your choice, this step does one of the following: Adds a SIP or SDP header to a SIP request. Removes a SIP or SDP header from a SIP request. Modifies a SIP or SDP header in a SIP request. If the ANY is used, the rule is applied to the specified header when it appears in any message type. When specifying a profile rule header value: If a value includes a space, the entire value must be included between double quotes. For example, “User-Agent: CISCO CUBE” When using double quotes in a value, delimit with a backslash. Simple regular expressions are supported. |
| Step 5 | Enter one of
                                          			 the following to add, remove, or modify SIP response headers: [rule x ] response message [ method method-type ] { sip-header \| sdp-header } header-to-add add header-value-to-add [rule x ] response message [ method method-type ] { sip-header \| sdp-header } header-to-remove remove [rule x ] response message [ method method-type ] { sip-header \| sdp-header } header-to-modify modify header-value-to-match header-value-to-replace | According
                                          			 to your choice, this step does one of the following: Adds a SIP or SDP header to a SIP response. Removes a SIP or SDP header from a SIP response. Modifies a SIP or SDP header in a SIP response. All notes in the previous step are applicable here. |
| Step 6 | end | Exits to
                                             				privileged EXEC mode |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables
                                             				privileged EXEC mode. Enter
                                                   					 your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | To enable copying of unsupported SDP attribute from incoming leg to outbound leg, you must enable one of the following commands: In Global VoIP SIP configuration mode pass-thru content custom-sdp In dial-peer configuration mode (The configuration is applied on the incoming dial-peer) voice-class sip pass-thru content custom-sdp Example: In Global VoIP SIP configuration mode: Device(config)# voice service voip
Device(conf-voi-serv)# sip
Device(conf-serv-sip)# pass-thru content custom-sdp Example: In Dial-peer configuration mode: Device(config)# dial-peer voice 2 voip
Device(config-dial-peer)# voice-class sip pass-thru content custom-sdp | Enables copying of unsupported SDP attributes per m-line to the peer leg so that it can be used in outgoing SIP messages. Note Enabling this command does not enable the SDP Passthrough feature. | Note | Enabling this command does not enable the SDP Passthrough feature. |
| Note | Enabling this command does not enable the SDP Passthrough feature. |
| Step 4 | voice class sip-profiles profile-id Example: Device(config)# voice class sip-profiles 10 | Voice class sip-profile is configured on the outbound dial-peer or
                                             				as a global configuration. Creates a
                                             				SIP Profile and enters voice class configuration mode. |
| Step 5 | Enter one of
                                          			 the following to copy an unsupported SDP line or attribute from peer leg's SDP
                                          			 and add, modify, or remove in the outgoing SDP: [rule x ] {request/response} ANY peer-header sdp mline-index index COPY match-pattern copy-variable [rule x ] {request/response} ANY sdp-header mline-index index header-name ADD copy-variable [rule x ] {request/response} ANY sdp-header mline-index index header-name MODIFY copy-variable + replace-pattern [rule x ] { request/response} ANY sdp-header mline-index index header-name REMOVE | M-line Index
                                             				values: 0 - A
                                                   					 value of zero represents the session level. 1–6 - A value in the range of one to six represents the m-line number in SDP. Copy:
                                             				Enables copying of SDP line or attribute from peer leg SDP. Add: Enables
                                             				adding the copied SDP line or attribute in the outgoing SDP. Modify:
                                             				Enables modifying SDP line or attribute in the outgoing SDP. Remove:
                                             				Enables removing SDP line or attribute in the outgoing SDP. |
| Step 6 | end | Exits to
                                             				privileged EXEC mode. |

| Note | Enabling this command does not enable the SDP Passthrough feature. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable | Enables
                                             				privileged EXEC mode. Enter
                                                   					 your password if prompted. |
| Step 2 | configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice class sip-profiles profile-id Example: Device(config)# voice class sip-profiles 10 | Creates a SIP
                                             				Profiles and enters voice class configuration mode. |
| Step 4 | Enter one of
                                          			 the following to add, copy, remove, or modify non-standard SIP request headers: [rule x ] request message sip-header non-standard-header-to-add add non-standard-header-value-to-add [rule x ] request message sip-header non-standard-header-to-copy copy non-standard-header-value-to-match copy-variable [rule x ] request message sip-header non-standard-header-to-remove remove ] [rule x ] request message { sip-header } non-standard-header-to-modify modify non-standard-header-value-to-match non-standard-header-value-to-replace | According to
                                          			 your choice, this step does one of the following: Adds a non-standard SIP header to a SIP request. Copies a non-standard SIP header value to a copy variable. Removes a non-standard SIP header from a SIP request. Modifies a non-standard SIP header in a SIP request. If the ANY message keyword is used, the rule is applied to the specified header when it appears in any message type. For non-standard-header-value-to-add used to add a non-standard header, non-standard-header-value-to-match or non-standard-header-value-to-replace used to modify a non-standard header when specifying a profile rule header value: If a value includes a space , the entire value must be included between double quotes. For example, “User-Agent: CISCO CUBE” When using double quotes in a value, delimit with a backslash. Simple regular expressions are supported. |
| Step 5 | Enter one of
                                          			 the following to add, copy, remove, or modify non-standard SIP response
                                          			 headers: [rule x ] response message [ method method-type ] sip-header non-standard-header-to-add add non-standard-header-value-to-add [rule x ] response message [ method method-type ] sip-header non-standard-header-to-copy copy non-standard-header-value-to-match copy-variable [rule x ] response message [ method method-type ] sip-header non-standard-header-to-remove remove [rule x ] response message [ method method-type ] sip-header non-standard-header-to-modify modify non-standard-header-value-to-match non-standard-header-value-to-replace | According
                                          			 to your choice, this step does one of the following: Adds a non-standard header to a SIP response message. Copies
                                                   					 contents from a non-standard SIP header to a SIP response. Removes a non-standard header to a SIP response. Modifies a non-standard SIP header in a SIP response. All
                                                   					 notes from the previous step are applicable here. |
| Step 6 | end | Exits to
                                             				privileged EXEC mode |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable | Enables
                                             				privileged EXEC mode. Enter
                                                   					 your password if prompted. |
| Step 2 | configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | Apply the SIP
                                          			 profile to a dial peer: voice-class sip profiles profile-id in the dial-peer configuration mode. sip-profiles profile-id in the global VoIP configuration mode Example: In
                                          			 dial-peer configuration mode !Applying SIP profiles to one dial peer only
Device (config)# dial-peer voice 10 voip Device (config-dial-peer)# voice-class sip profiles 30 Device (config-dial-peer)# end Example: In global
                                          			 VoIP SIP mode ! Applying SIP profiles globally
Device(config)# voice service voip Device (config-voi-serv)# sip Device (config-voi-sip)# sip-profiles 20 Device (config-voi-sip)# end |  |
| Step 4 | end | Exits to
                                             				privileged EXEC mode . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable | Enables
                                             				privileged EXEC mode. Enter
                                                   					 your password if prompted. |
| Step 2 | configure terminal | Enters
                                             				global configuration mode. |
| Step 3 | voice service voip Example: Device(config)# voice service voip | Enters
                                             				global VoIP configuration mode. |
| Step 4 | sip Example: Device(config-voi-serv)# sip | Enters
                                             				global VoIP SIP configuration mode. |
| Step 5 | sip-profiles
                                                				  inbound Example: Device(config-voi-sip)# sip-profiles inbound | Enables
                                             				inbound SIP profiles feature. |
| Step 6 | Apply the
                                          			 SIP profile to a dial peer: voice-class sip
                                                   					 profiles profile-id inbound in the dial-peer configuration mode. sip-profiles profile-id inbound in the global VoIP configuration mode Example: In
                                          			 dial-peer configuration mode !Applying SIP profiles to one dial peer only
Device (config)# dial-peer voice 10 voip Device (config-dial-peer)# voice-class sip profiles 30 inbound Device (config-dial-peer)# end Example: In
                                          			 global VoIP SIP mode ! Applying SIP profiles globally
Device(config)# voice service voip Device (config-voi-serv)# sip Device (config-voi-sip)# sip-profiles 20 inbound Device (config-voi-sip)# end |  |
| Step 7 | end | Exits to
                                             				privileged EXEC mode |

| Note | Non-standard SIP headers are also supported. |
|---|---|

| show dial-peer voice id \| include
                                             				  profile Displays information related to SIP profiles configured on the
                                          				specified dial peer. Example: Device# show dial-peer voice 10 \| include sip profile voice class sip profiles = 11
        voice class sip profiles inbound = 10 |
|---|---|---|

| debug ccsip all This command displays the applied SIP profiles. Example: Applied SIP profile is highlighted in the example below. Device# debug ccsip all …
Oct 12 06:51:53.619: //-1/735085DC8F3D/SIP/Info/sipSPIGetShrlPeer: 
                     Try match incoming dialpeer for Calling number:  
                     : sippOct 12 06:51:53.619:  
                     //-1/735085DC8F3D/SIP/Info/sipSPIGetCallConfig:  
                     Peer tag 2 matched for incoming call 
Oct 12 06:51:53.619: //-1/xxxxxxxxxxxx/SIP/Info/sipSPIGetCallConfig: voice class SIP profiles tag is set : 1 Oct 12 06:51:53.619: //-1/735085DC8F3D/SIP/Info/sipSPIGetCallConfig:  
                     Not using Voice Class Codec
Oct 12 06:51:53.619: //-1/735085DC8F3D/SIP/Info/sipSPIGetCallConfig:  
                     xcoder high-density disabled
Oct 12 06:51:53.619: //-1/735085DC8F3D/SIP/Info/sipSPIGetCallConfig:  
                     Flow Mode set to FLOW_THROUGH This command also displays the modifications that are performed by the SIP profile configuration, by preceding the modification
                                       information with the word sip_profiles, as highlighted in the following example. Example: Device# debug ccsip all
…
Oct 12 06:51:53.647: //-1/xxxxxxxxxxxx/SIP/Info/
sip_profiles_application_change_sdp_line:
New SDP header is added : b=AS: 1600
Oct 12 06:51:53.647: //-1/xxxxxxxxxxxx/SIP/Info/
sip_profiles_update_content_length:
Content length header before modification :
Content-Length: 290
Oct 12 06:51:53.647: //-1/xxxxxxxxxxxx/SIP/Info/
sip_profiles_update_content_length:
Content length header after modification :
Content-Length: 279 |
|---|