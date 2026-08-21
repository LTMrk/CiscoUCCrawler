---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmedialp-html-cd073e4d4d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmedialp.html
retrieved_at: 2026-08-21T07:22:44.117980+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Dial Plans

## Chapter: Dial Plans

# Dial Plans

This chapter describes features that enable Cisco Unified Communications
                        		Manager Express (Cisco Unified CME) to expand or manipulate internal extension
                        		numbers so that they conform to numbering plans used by external systems.

## Information About Dial Plans

### Phone Number
                           	 Plan

If you install a
                              		Cisco Unified CME system to replace an older telephony system that had an
                              		established telephone number plan, you can retain the old number plan.
                              		Cisco Unified CME supports flexible extension number lengths and can provide
                              		automatic conversion between extension dialing and E.164 public telephone
                              		number dialing.

When a router
                              		receives a voice call, it selects an outbound dial peer by comparing the called
                              		number (the full E.164 telephone number) in the call information with the
                              		number configured as the destination pattern for the POTS dial peer. The router
                              		then strips out the left-justified numbers corresponding to the destination
                              		pattern matching the called number. If you have configured a prefix, the prefix
                              		will be put in front of the remaining numbers, creating a dial string, which
                              		the router will then dial. If all numbers in the destination pattern are
                              		stripped-out, the user will receive (depending on the attached equipment) a
                              		dial tone.

A successful
                              		Cisco Unified CME system requires a telephone numbering plan that supports
                              		future expansion. The numbering plan also must not overlap or conflict with
                              		other numbers that are on the same VoIP network or are part of a centralized
                              		voice mail system.

Cisco Unified CME supports shared lines and multiple lines configured with the same extension number. This means that you
                              can set up several phones to share an extension number to provide coverage for that number. You can also assign several line
                              buttons on a single phone to the same extension number to create a small hunt group.

If you are
                              		configuring more than one Cisco Unified CME site, you need to decide how calls
                              		between the sites will be handled. Calls between Cisco Unified CME phones can
                              		be routed either through the PSTN or over VoIP. If you are routing calls over
                              		VoIP, you must decide among the following three choices:

You can route
                                    			 calls using a global pool of fixed-length extension numbers. For example, all
                                    			 sites have unique extension numbers in the range 5000 to 5999, and routing is
                                    			 managed by a gatekeeper. If you select this method, assign a subrange of
                                    			 extension numbers to each site so that duplicate number assignment does not
                                    			 result. You will have to keep careful records of which Cisco Unified CME system
                                    			 is assigned which number range.

You can route
                                    			 calls using a local extension number plus a special prefix for each
                                    			 Cisco Unified CME site. This choice allows you to use the same extension
                                    			 numbers at more than one site.

You can use an
                                    			 E.164 PSTN phone number to route calls over VoIP between Cisco Unified CME
                                    			 sites. In this case, intersite callers use the PSTN area code and local prefix
                                    			 to route calls between Cisco Unified CME systems.

If you choose to
                              		have a gatekeeper route calls among multiple Cisco Unified CME systems, you may
                              		face additional restrictions on the extension number formats that you use. For
                              		example, you might be able to register only PSTN-formatted numbers with the
                              		gatekeeper. The gatekeeper might not allow the registration of duplicate
                              		telephone numbers in different Cisco Unified CME systems, but you might be able
                              		to overcome this limitation. Cisco Unified CME allows the selective
                              		registration of either 2- to 5-digit extension numbers or 7- to 10-digit PSTN
                              		numbers, so registering only PSTN numbers might prevent the gatekeeper from
                              		sensing duplicate extensions.

Mapping of public
                              		telephone numbers to internal extension numbers is not restricted to simple
                              		truncation of the digit string. Digit substitutions can be made by defining
                              		dial plan patterns to be matched. For information about dial plans, see Dial Plan Patterns . More
                              		sophisticated number manipulations can be managed with voice translation rules
                              		and voice translation profiles, which are described in the Voice Translation Rules and Profiles section.

In addition, your
                              		selection of a numbering scheme for phones that can be directly dialed from the
                              		PSTN is limited by your need to use the range of extensions that are assigned
                              		to you by the telephone company that provides your connection to the PSTN. For
                              		example, if your telephone company assigns you a range from 408 555-0100 to 408
                              		555-0199, you may assign extension numbers only in the range 100 to 199 if
                              		those extensions are going to have Direct Inward Dialing (DID) access. For more
                              		information about DID, see Direct Inward Dialing Trunk Lines .

### Dial Plan
                           	 Patterns

A dial plan pattern
                              		enables abbreviated extensions to be expanded into fully qualified E.164
                              		numbers. Use dial plan patterns when configuring a network with multiple
                              		Cisco Unified CMEs to ensure that the appropriate calling number, extension or
                              		E.164 number, is provided to the target Cisco Unified CME, and appears on the
                              		phone display of the called phone. In networks that have a single router, you
                              		do not need to use dial plan patterns.

When you define a
                              		directory number for an SCCP phone, the Cisco Unified CME system automatically
                              		creates a POTS dial peer with the ephone-dn endpoint as a destination. For SIP
                              		phones connected directly into Cisco Unified CME, the dial peer is
                              		automatically created when the phone registers. By default, Cisco Unified CME
                              		creates a single POTS dial peer for each directory number.

For example, when
                              		the ephone-dn with the number 1001 was defined, the following POTS dial peer
                              		was automatically created for it:

```
dial-peer voice 20001 pots
	  destination-pattern 1001
	  voice-port 50/0/2
```

A dial plan pattern
                              		builds additional dial peers for the expanded numbers it creates. If a dialplan
                              		pattern is configured and it matches against a directory number, two POTS dial
                              		peers are created, one for the abbreviated number and one for the complete
                              		E.164 direct-dial telephone number.

For example, if you
                              		then define a dial plan pattern that 1001 will match, such as 40855500.., a
                              		second dial peer is created so that calls to both the 0001 and 4085550001
                              		numbers are completed. In this example, the additional dial peer that is
                              		automatically created looks like the following:

```
dial-peer voice 20002 pots
	 destination-pattern 40855510001
	 voice-port 50/0/2
```

In networks with
                              		multiple routers, you may need to use dial plan patterns to expand extensions
                              		to E.164 numbers because local extension numbering schemes can overlap each
                              		other. Networks with multiple routers have authorities such as gatekeepers that
                              		route calls through the network. These authorities require E.164 numbers so
                              		that all numbers in the network are unique. Define dial plan patterns to expand
                              		extension numbers into unique E.164 numbers for registering with a gatekeeper.
                              		For more information on E.164 numbers, see E .164 Enhancements .

If multiple dial
                              		plan patterns are defined, the system matches extension numbers against the
                              		patterns in sequential order, starting with the lowest numbered dial plan
                              		pattern tag first. Once a pattern matches an extension number, the pattern is
                              		used to generate an expanded number. If additional patterns subsequently match
                              		the extension number, they are not used.

### Direct Inward Dialing Trunk Lines

Direct Inward Dialing (DID), is a one-way incoming trunking mechanism,
                              		that allows an external caller to directly reach a specific extension without
                              		the call being served by an attendant or other intervention.

It is a service offered in which the last few (typically three or four)
                              		digits dialed by the caller are forwarded to the called party on a special DID
                              		trunk. For example, all the phone numbers from 555-0000 to 555-0999 could be
                              		assigned to a company with 20 DID trunks. When a caller dials any number in
                              		this range, the call is forwarded on any available trunk. If the caller dialed
                              		555-0234, then the digits 2, 3, and 4 are forwarded. These DID trunks could be
                              		terminated on a PBX, so that the extension 234 gets the call without operator
                              		assistance. This makes it look as though 555-0234 and the other 999 lines all
                              		have direct outside lines, while only requiring 20 trunks to service the 1,000
                              		telephone extensions. Using DID, a company can offer its customers individual
                              		phone numbers for each person or workstation within the company without
                              		requiring a physical line into the PBX for each possible connection. Compared
                              		to regular PBX service, DID saves the cost of a switchboard operator. Calls go
                              		through faster, and callers feel they are calling a person rather than a
                              		company.

Dial plan patterns are required to enable calls to DID numbers. When the
                              		PSTN connects a DID call for “4085550234” to the Cisco Unified CME system, it
                              		also forwards the extension digits “234” to allow the system to route the call.

### Voice Translation
                           	 Rules and Profiles

Translation rules
                              		manipulate dialed numbers to conform to internal or external numbering schemes.
                              		Voice translation profiles allow you to group translation rules together and
                              		apply them to the following types of numbers:

Called numbers
                                    			 (DNIS)

Calling numbers
                                    			 (ANI)

Redirected
                                    			 called numbers

Redirected
                                    			 target numbers—These are transfer-to numbers and call-forwarding final
                                    			 destination numbers. Supported by SIP phones in Cisco Unified CME 4.1 and later
                                    			 versions.

After you define a
                              		set of translation rules and assign them to a translation profile, you can
                              		apply the rules to incoming and outgoing call legs to and from the
                              		Cisco Unified CME router based on the directory number. Translation rules can
                              		perform regular expression matches and replace substrings. A translation rule
                              		replaces a substring of the input number if the number matches the match
                              		pattern, number plan, and type present in the rule.

For configuration
                              		information, see Define Voice Translation Rules in Cisco CME 3.2 and Later Versions .

For examples of
                              		voice translation rules and profiles, see the Voice Translation Rules technical note
                              		and the Number Translation using Voice Translation
                                 		  Profiles technical note.

### Secondary Dial
                           	 Tone

A secondary dial
                              		tone is available for Cisco Unified IP phones connected to Cisco Unified CME.
                              		From Cisco Unified CME Release 11.6 onwards, secondary dial tone is supported
                              		on both SIP phones and SCCP phones.

The secondary dial
                              		tone is generated when a phone user dials a predefined PSTN access prefix and
                              		terminates when additional digits are dialed. An example is when a secondary
                              		dial tone is heard after a PSTN access prefix, such as the number 9, is dialed
                              		to reach an outside line. For SIP phones, a dialplan file is downloaded when
                              		the phone restarts. This dialplan file will have the dialplan pattern
                              		configured. Based on this dialplan pattern, phone would collect the digits or
                              		play secondary dial tone if there is a comma (,) in the pattern. The call is
                              		placed from the phone, when there is matching pattern in the dialplan file.
                              		Also note that when this feature is enabled, KPML digit collection is disabled
                              		on SIP phones.

For configuration
                              		information, see Activate Secondary Dial Tone For SCCP Phones and Activate Secondary Dial Tone for SIP Phones .

### E .164 Enhancements

Cisco Unified CME 8.5 allows you to present a phone number in + E.164
                              		telephone numbering format. E.164 is an International Telecommunication Union
                              		(ITU-T) recommendation that defines the international public telecommunication
                              		numbering plan used in the PSTN and other data networks. E.164 defines the
                              		format of telephone numbers. A leading + E.164 telephone number can have a
                              		maximum of 15 digits and is usually written with a ‘+’ prefix defining the
                              		international access code. To dial such numbers from a normal fixed line phone,
                              		the appropriate international call prefix must be used.

The leading +E.164 number is unique number specified to a phone or a
                              		device. Callers from around the world dial the leading + E.164 phone number to
                              		reach a phone or a device without the need to know local or international
                              		prefix. The leading + E.164 feature also reduces the overall telephony
                              		configuration process by eliminating the need to further translate the
                              		telephone numbers.

#### Phone Registration
                              	 with Leading + E164 Number

In
                                 		Cisco Unified CME, phones register using the leading ‘+’ dialing plan in two
                                 		ways. Phones can either register with the extension number or with leading +
                                 		E.164 number.

When phones are
                                 		registered with extension number, the phones will have a dial peer association
                                 		with the extension number. The dialplan-pattern command is enhanced to allow you
                                 		to configure leading + phone numbers on the dialplan pattern. Once
                                 		dialplan-pattern is configured, there could be an E.164 number dialpeer
                                 		associated with the same phone.

For example, phones
                                 		registered with extension number 1111 can also be reached by dialing
                                 		+13332221111. This phone registration method is beneficial in two ways, that
                                 		is, locally, phones are able to reach each other by just dialing the extension
                                 		numbers and, remotely, phones can dial abbreviated numbers which are translated
                                 		as an E.164 number at the outgoing dial-peer. See Example 1 for more information.

There are instances where phone is registered with Unified CME using
                                             		  the extension number. If the user has to reach the phone using the full +E.164
                                             		  number, a dial peer needs to be configured for the full number. This is
                                             		  applicable only when the extension-length is specified to have the same length
                                             		  as extension number.

When phones are
                                 		registered with a leading + E.164 number, there is only one leading + E.164
                                 		number associated with the phone. The demote option
                                 		in the dialplan-pattern command allows the phone to have
                                 		two dialpeers associated with the same phone. For more information on
                                 		configuring the dialplan-patterns, see Configure Dial Plans .

For example, a phone
                                 		registered with + E.164 phone number +12223331111 will have two dialpeers
                                 		associated with the same phone that is, +122233331111 and 1111. See Example 2 .

##### Example 1

In the following
                                       		  example, phones are registered with extension number 1111 but they can be
                                       		  reached by either dialing the 4-digit extension number, or a leading + E.164
                                       		  number (+122233331111). When the dial-peer pattern is configured, phones can
                                       		  also be reached by dialing its + E.164 number. The phone can be reached by
                                       		  dialing either the 4-digit extension number or the + E.164 number.

```
!
ephone-dn 1
 number 1111
!
ephone 1
 button 1:1
!
telephony-service
 dialplan-pattern 1 +1222333.... extension-length 4
!
voice register dn 1
 number 1235
!
voice register pool 1
 number 1 dn 1
!
voice register global
 dialplan-pattern 1 +1222333.... extension-length 4
```

##### Example 2

In the following
                                       		  example, phones are registered with leading + E.164 number (+122233331111) and
                                       		  the phones can be reached by dialing either the 4-digit extension number or the
                                       		  + E.164 number. In this example, phone can be reached by dialing 1111 or the
                                       		  +E.164 number.

```
!
ephone-dn 1
 number +12223331111

!
ephone 1
 button 1:1

!
telephony-service
 dialplan-pattern 1 +1222333.... extension-length 4 demote

!
voice register dn 1
 number +12223331235

!
voice register pool 1
 number 1 dn 1

!
voice register global
 dialplan-pattern 1 +1222333.... extension-length 4 demote
```

Because the legacy phone does not have a ‘+’ button, you can
                                                   			 configure dialplan-pattern or translation profile.

##### Example 3

In the following example, phones
                                       		  are registered with leading + E.164 number (+12223331111) for SCCP phone and
                                       		  +12223331235 for SIP phone) and the phones can be reached by dialing either the
                                       		  6-digit number or the + E.164 number. The phone number +12223331234 can be
                                       		  reached by dialing either the 6-digit demoted number or the + E.164 number.

```
!
ephone-dn 1
 number +12223331111

!
ephone 1
 button 1:1
!
telephony-service
 dialplan-pattern 1 +1222333.... extension-length 6 demote

!
voice register dn 1
 number +12223331235

!
voice register pool 1
 number 1 dn 1

!
voice register global
 dialplan-pattern 1 +1222333.... extension-length 6 demote
```

After the CLI for demote is configured to extension-length 6, you can
                                       		  dial 331235 for SIP phone, and 331111 for SCCP phone.

#### Callback and
                              	 Calling Number Display

In earlier versions
                                 		of Cisco Unified CME and Cisco Unified SRST, the calling number (number from an
                                 		incoming call ringing on your phone) was used for both callback (number
                                 		displayed under Missed Calls in your local phone directory number) and calling
                                 		numbers. The + E.164 feature in Cisco Unified CME 8.5, allows you to display
                                 		both calling number and callback numbers in appropriate format so that you are
                                 		not required to edit the phone numbers before placing a call. The calling
                                 		number is displayed on the phone when you configure the translation-profile
                                       			 outgoing command in ephone-dn or voice register dn mode.

The translate
                                       			 callback-number configuration in voice translation-profile allows
                                 		you to translate the callback number and display it in E.164 format. The translate callback
                                       			 number configuration is only applicable for outgoing calls on SIP
                                 		and SCCP IP phones. When translate callback
                                       			 number is configured, the extra callback field is displayed and
                                 		if the number matches the translation rule, it is translated. For more
                                 		information see Define Translation Rules for Callback-Number on SIP Phones .

Similarly, in Cisco
                                 		Unified SRST 8.5, you can configure translate
                                       			 calling under voice
                                       			 translation-profile mode to display the calling number. You can
                                 		configure translation-profile
                                       			 outgoing in call-manager-fallback mode or voice register pool to display the callback
                                 		number. You can use translate
                                       			 called command in translation-profile and call-manager-fallback or voice register pool will try to match the called
                                 		number to do the translation. See Enabling Translation Profiles for more
                                 		information.

The leading ‘+’ in
                                 		the E.164 number is stripped from the called and calling numbers if the called
                                 		endpoint or gateway, such as H323 or QSIG gateway, does not support the leading
                                 		‘+’ sign in the E.164 number translation. You can strip the leading ‘+’ sign
                                 		from the number you are calling or a called number using the translation-profile
                                       			 incoming or translation-profile
                                       			 outgoing commands.

## Configure Dial Plans

### Configure SCCP
                           	 Dial Plan Patterns

Tip

In networks that
                                             			 have a single router, you do not need to define dial plan patterns.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- dialplan-pattern tag pattern extension-length length [ extension-pattern epattern ] [ no-reg ]

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

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony-service configuration mode.

Step 4

dialplan-pattern tag pattern extension-length length [ extension-pattern epattern ] [ no-reg ]

#### Example:

```
Router(config-telephony)# dialplan-pattern 1 4085550100 extension-length 3 extension-pattern 4..
```

This example
                                                         				  maps all extension numbers 4xx to the PSTN number 40855501xx, so that extension
                                                         				  412 corresponds to 4085550112.

Maps a digit
                                             				pattern for an abbreviated extension-number prefix to the full E.164 telephone
                                             				number pattern.

Step 5

end

#### Example:

```
Router(config-telephony)# end
```

Exits
                                             				configuration mode and enters privileged EXEC mode.

### Configure SIP Dial
                           	 Plan Patterns

To create and
                                 		  apply a pattern for expanding individual abbreviated SIP extensions into fully
                                 		  qualified E.164 numbers, follow the steps in this section. dial plan pattern
                                 		  expansion affects calling numbers and for call forward using B2BUA,
                                 		  redirecting, including originating and last reroute, numbers for SIP extensions
                                 		  in Cisco Unified CME.

#### Before you begin

Cisco Unified CME
                                 		  4.0 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- dialplan-pattern tag
                                       				  pattern extension-length extension-length [ extension-pattern extension-pattern | no-reg ]

- call-forward system redirecting-expanded

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

voice register global

#### Example:

```
Router(config)# voice register global
```

Enters voice
                                             				register global configuration mode to set parameters for all supported SIP
                                             				phones in Cisco Unified CME.

Step 4

dialplan-pattern tag
                                                				  pattern extension-length extension-length [ extension-pattern extension-pattern | no-reg ]

#### Example:

```
Router(config-register-global)# dialplan-pattern 1 4085550... extension-length 5
```

Defines
                                             				pattern that is used to expand abbreviated extension numbers of SIP calling
                                             				numbers in Cisco Unified CME into fully qualified E.164 numbers.

Step 5

call-forward system redirecting-expanded

#### Example:

```
Router(config-register-global)# call-forward system redirecting-expanded
```

Applies dial
                                             				plan pattern expansion globally to redirecting, including originating and last
                                             				reroute, numbers for SIP extensions in Cisco Unified CME for call forward using
                                             				B2BUA.

Step 6

end

#### Example:

```
Router(config-register-global)# end
```

Exits
                                             				configuration mode and enters privileged EXEC mode.

### Verify Dial Plan
                           	 Patterns

### SUMMARY STEPS

- show telephony-service

- SCCP: show telephony-service
                                       				  dial-peer or SIP: show dial-peer
                                       				  summary

### DETAILED STEPS

Step 1

show telephony-service

Use this
                                             				command to verify dial plan patterns in the configuration.

#### Example:

The following
                                             				example maps the extension pattern 4.. to the last three digits of the dial
                                             				plan pattern 4085550155:

```
telephony-service
 dialplan-pattern 1 4085550155 extension-length 3 extension-pattern 4..
```

Step 2

SCCP: show telephony-service
                                                				  dial-peer or SIP: show dial-peer
                                                				  summary

Use the
                                             				command to display dial peers that are automatically created by the dialplan-pattern command.

Use this
                                             				command display the configuration for all VoIP and POTS dial peers configured
                                             				for a router, including dial peers created by using the dialplan-expansion (voice
                                                   					 register) command.

#### Example:

The following
                                             				example is output from the show dial-peer
                                                   					 summary command displaying information for four dial peers, one
                                             				each for extensions 60001 and 60002 and because the dialplan-expansion command is configured to expand
                                             				6.... to 4085555...., one each for 4085550001 and 4085550002. The latter two
                                             				dial peers will not appear in the running configuration.

```
Router# show dial-peer summary AD                                    PRE PASS                OUT 
TAG    TYPE  MIN  OPER PREFIX    DEST-PATTERN      FER THRU SESS-TARGET    STATT
20010  pots  up   up             60002$             0                       0
20011  pots  up   up             60001$             0                       9
20012  pots  up   up             5105555001$        0                       9
20013  pots  up   up             5105555002$        0                       0
```

### Define Voice
                           	 Translation Rules in Cisco CME 3.2 and Later Versions

To configure
                                             			 translation rules for voice calls in Cisco CME 3.1 and earlier versions, see Cisco IOS Voice, Video, and
                                                				FAX Configuration Guide .

#### Before you begin

SCCP
                                       				support—Cisco CME 3.2 or a later version.

SIP
                                       				support—Cisco Unified CME 4.1 or a later version.

To define up
                                       				to 100 translation rules per translation rule table—Cisco Unified CME 8.6 or a
                                       				later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice translation-rule number

- rule precedence / match-pattern / / replace-pattern /

- exit

- voice translation-profile name

- translate { called | calling | redirect-called | redirect-target } translation-rule-number

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

voice translation-rule number

#### Example:

```
Router(config)# voice translation-rule 1
```

Defines a
                                             				translation rule for voice calls and enters voice translation-rule
                                             				configuration mode.

number—Number that identifies the translation rule. Range: 1 to
                                                   					 2147483647.

Step 4

rule precedence / match-pattern / / replace-pattern /

#### Example:

```
Router(cfg-translation-rule)# rule 1 /^9/ //
```

Defines a
                                             				translation rule.

precedence —Priority of the translation rule.
                                                   					 Range: 1 to 100.

Range
                                                         				  limited to 15 maximum rules in CME 8.5 and earlier versions.

match-pattern —Stream Editor (SED) expression used
                                                   					 to match incoming call information. The slash (/) is a delimiter in the
                                                   					 pattern.

replace-pattern —SED expression used to replace the
                                                   					 match pattern in the call information. The slash (/) is a delimiter in the
                                                   					 pattern.

Step 5

exit

#### Example:

```
Router(cfg-translation-rule)# exit
```

Exits voice
                                             				translation-rule configuration mode.

Step 6

voice translation-profile name

#### Example:

```
Router(config)# voice translation-profile name1
```

Defines a
                                             				translation profile for voice calls.

name —Name of the translation profile. Maximum
                                                   					 length of the voice translation profile name is 31 alphanumeric characters.

Step 7

translate { called | calling | redirect-called | redirect-target } translation-rule-number

#### Example:

```
Router(cfg-translation-profile)# translate called 1
```

Associates a
                                             				translation rule with a voice translation profile.

called —Associates the translation rule with called
                                                   					 numbers.

calling —Associates the translation rule with
                                                   					 calling numbers.

redirect-called —Associates the translation rule with redirected
                                                   					 called numbers.

redirect-target —Associates the translation rule with transfer-to
                                                   					 numbers and call-forwarding final destination numbers. This keyword is
                                                   					 supported by SIP phones in Cisco Unified CME 4.1 and later versions.

translation-rule-number —Reference number of the
                                                   					 translation rule configured in Step 3 .
                                                   					 Range: 1 to 2147483647.

Step 8

end

#### Example:

```
Router(cfg-translation-profile)# end
```

Returns to
                                             				privileged EXEC mode.

#### What to do next

To apply
                                       				voice translation profiles to SCCP phones connected to Cisco Unified CME 3.2 or
                                       				a later version, see Apply Voice Translation Rules on SCCP Phones in Cisco Unified CME 3.2 and Later Versions .

To apply
                                       				voice translation profiles to SIP phones connected to Cisco Unified CME 4.1 or
                                       				a later version, see Apply Voice Translation Rules on SIP Phones in Cisco Unified CME 4.1 and Later .

To apply
                                       				voice translation profiles to SIP phones connected to Cisco CME 3.4 or
                                       				Cisco Unified CME 4.0(x), see Apply Voice Translation Rules on SIP Phones Before Cisco Unified CME 4.1 .

### Apply Voice
                           	 Translation Rules on SCCP Phones in Cisco Unified CME 3.2 and Later
                           	 Versions

To apply a voice
                                 		  translation profile to incoming or outgoing calls to or from a directory number
                                 		  on a SCCP phone, perform the following steps.

#### Before you begin

Cisco CME 3.2
                                       				or a later version.

Voice
                                       				translation profile containing voice translation rules to be applied must be
                                       				already configured. For configuration information, see Define Voice Translation Rules in Cisco CME 3.2 and Later Versions .

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn tag

- translation-profile { incoming | outgoing } name

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

ephone-dn tag

#### Example:

```
Router(config)# ephone-dn 1
```

Enters
                                             				ephone-dn configuration mode to create an extension (ephone-dn) for a
                                             				Cisco Unified IP phone line, an intercom line, a paging line, a voice-mail
                                             				port, or a message-waiting indicator (MWI).

tag —Unique sequence number that identifies this
                                                   					 ephone-dn during configuration tasks. Range is 1 to the maximum number of
                                                   					 ephone-dns allowed on the router platform. See the CLI help for the maximum
                                                   					 value for this argument.

Step 4

translation-profile { incoming | outgoing } name

#### Example:

```
Router(config-ephone-dn)# translation-profile outgoing name1
```

Assigns a
                                             				translation profile for incoming or outgoing call legs to or from
                                             				Cisco Unified IP phones.

You can
                                                   					 also use an ephone-dn template to apply this command to one or more directory
                                                   					 numbers. If you use an ephone-dn template to apply a command and you use the
                                                   					 same command in ephone-dn configuration mode for the same directory number, the
                                                   					 value that you set in ephone-dn configuration mode has priority.

Step 5

end

#### Example:

```
Router(config-ephone-dn)# end
```

Returns to
                                             				privileged EXEC mode.

#### What to do next

If you are done
                                 		  modifying parameters for phones in Cisco Unified CME, generate a new
                                 		  configuration file and restart the phones. See Generate Configuration Files for Phones .

### Apply Translation
                           	 Rules on SCCP Phones Before Cisco Unified CME 3.2

To apply a
                                 		  translation rule to an individual directory number in Cisco CME 3.1 and earlier
                                 		  versions, perform the following steps.

#### Before you begin

Translation rule
                                 		  to be applied must be already configured by using the translation-rule and rule commands. For configuration information, see Cisco IOS Voice, Video, and
                                    			 FAX Configuration Guide .

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn tag

- translate { called | calling } translation-rule-tag

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

ephone-dn tag

#### Example:

```
Router(config)# ephone-dn 1
```

Enters
                                             				ephone-dn configuration mode to create directory number for a Cisco Unified IP
                                             				phone line, an intercom line, a paging line, a voice-mail port, or a
                                             				message-waiting indicator (MWI).

Step 4

translate { called | calling } translation-rule-tag

#### Example:

```
Router(config-ephone-dn)# translate called 1
```

Specifies rule
                                             				to be applied to the directory number being configured.

translation-rule-tag —Reference number of
                                                   					 previously configured translation rule. Range: 1 to 2147483647.

You can
                                                   					 use an ephone-dn template to apply this command to one or more directory
                                                   					 numbers. If you use an ephone-dn template to apply a command to a directory
                                                   					 number and you also use the same command in ephone-dn configuration mode for
                                                   					 the same directory number, the value that you set in ephone-dn configuration
                                                   					 mode has priority.

Step 5

end

#### Example:

```
Router(cfg-translation-profile)# end
```

Exits
                                             				configuration mode and enters privileged EXEC mode.

#### What to do next

If you are done
                                 		  modifying parameters for phones in Cisco Unified CME, generate a new
                                 		  configuration file and restart the phones. See Generate Configuration Files for Phones .

### Apply Voice
                           	 Translation Rules on SIP Phones in Cisco Unified CME 4.1 and Later

To apply a voice
                                 		  translation profile to incoming calls to a directory number on a SIP phone,
                                 		  perform the following steps.

#### Before you begin

Cisco Unified CME 4.1 or a later version.

Voice
                                       				translation profile containing voice translation rules to be applied must be
                                       				already configured. For configuration information, see Define Voice Translation Rules in Cisco CME 3.2 and Later Versions .

### SUMMARY STEPS

- enable

- configure terminal

- voice register dn dn-tag

- translation-profile incoming name

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

voice register dn dn-tag

#### Example:

```
Router(config)# voice register dn 1
```

Enters voice
                                             				register dn configuration mode to define a directory number for a SIP phone,
                                             				intercom line, voice port, or a message-waiting indicator (MWI).

Step 4

translation-profile incoming name

#### Example:

```
Router(config-register-dn)# translation-profile incoming name1
```

Assigns a
                                             				translation profile for incoming call legs to this directory number.

Step 5

end

#### Example:

```
Router(config-register-dn)# end
```

Returns to
                                             				privileged EXEC mode.

#### What to do next

If you are done
                                 		  modifying parameters for phones in Cisco Unified CME, generate a new
                                 		  configuration file and restart the phones. See Generate Configuration Profiles for SIP Phones .

### Apply Voice
                           	 Translation Rules on SIP Phones Before Cisco Unified CME 4.1

To apply an
                                 		  already-configured voice translation rule to modify the number dialed by
                                 		  extensions on a SIP phone, perform the following steps.

#### Before you begin

Cisco CME 3.4
                                       				or a later version.

Voice
                                       				translation rule to be applied must be already configured. For configuration
                                       				information, see Define Voice Translation Rules in Cisco CME 3.2 and Later Versions .

### SUMMARY STEPS

- enable

- configure terminal

- voice register pool pool-tag

- translate-outgoing { called | calling } rule-tag

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

voice register pool pool-tag

#### Example:

```
Router(config)# voice register pool 3
```

Enters voice
                                             				register pool configuration mode to set phone-specific parameters for SIP
                                             				phones.

Step 4

translate-outgoing { called | calling } rule-tag

#### Example:

```
Router(config-register-pool)# translate-outgoing called 1
```

Specifies an
                                             				already configured voice translation rule to be applied to SIP phone being
                                             				configured.

Step 5

end

#### Example:

```
Router(config-register-global)# end
```

Exits
                                             				configuration mode and enters privileged EXEC mode.

#### What to do next

If you are done
                                 		  modifying parameters for phones in Cisco Unified CME, generate a new
                                 		  configuration file and restart the phones. See Generate Configuration Profiles for SIP Phones .

### Verify Voice
                           	 Translation Rules and Profiles

To verify voice translation profiles, and rules, perform the following
                                 		  steps.

### SUMMARY STEPS

- show voice
                                       				  translation-profile [ name ]

- show voice
                                       				  translation-rule [ number ]

- test voice translation-rule number

### DETAILED STEPS

Step 1

show voice
                                                				  translation-profile [ name ]

This command
                                             				displays the configuration of one or all translation profiles.

#### Example:

```
Router# show voice translation-profile profile-8415 Translation Profile: profile-8415
  Rule for Calling number: 4
  Rule for Called number: 1
  Rule for Redirect number: 5
  Rule for Redirect-target number: 2
```

Step 2

show voice
                                                				  translation-rule [ number ]

This command
                                             				displays the configuration of one or all translation rules.

#### Example:

```
Router# show voice translation-rule 6 Translation-rule tag: 6
  Rule 1:
  Match pattern: 65088801..
  Replace pattern: 6508880101
  Match type: none   Replace type: none
  Match plan: none   Replace plan: none
```

Step 3

test voice translation-rule number

This command
                                             				enables you to test your translation rules.

#### Example:

```
Router(config)# voice translation-rule 5 Router(cfg-translation-rule)# rule 1 /201/ /102/ Router(cfg-translation-rule)# exit Router(config)# exit Router# test voice translation-rule 5 2015550101 Matched with rule 5
Original number:2015550101  Translated number:1025550101
Original number type: none    Translated number type: none
Original number plan: none    Translated number plan: none
```

### Activate Secondary
                           	 Dial Tone For SCCP Phones

To activate a
                                 		  secondary dial tone after a phone user dials the specified number, perform the
                                 		  following steps.

#### Before you begin

Cisco CME 3.0
                                       				or a later version.

PSTN access
                                       				prefix must be configured for outbound dial peer.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- secondary-dialtone digit-string

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

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony-service configuration mode.

Step 4

secondary-dialtone digit-string

#### Example:

```
Router(config-telephony)# secondary-dialtone 9
```

Activates a
                                             				secondary dial tone when digit-string is dialed.

digit-string —String of up to 32 digits that, when
                                                   					 dialed, activates a secondary dial tone. Typically, the digit-string is a predefined PSTN access prefix.

Step 5

end

#### Example:

```
Router(config-telephony)# end
```

Returns to
                                             				privileged EXEC mode.

### Activate Secondary
                           	 Dial Tone for SIP Phones

To activate a secondary dial tone after a phone user dials the
                                 		  specified number, perform the following steps.

#### Before you begin

Cisco Unified CME 11.6 or later for SIP phones.

### SUMMARY STEPS

- enable

- configure terminal

- voice register dialplan tag

- type 7940-7960-others

- pattern tag string

- voice register pool tag

- dialplan tag

- voice register global

- create profile

- voice register pool tag

- reset

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

voice register dialplan tag

#### Example:

```
Router(config)# voice register dialplan 1
```

Enters voice register dialplan configuration mode.

tag —Range for dialplan tag is 1 to
                                                   					 24.

Step 4

type 7940-7960-others

#### Example:

```
Router(config-register-dialplan)# type 7940-7960-others
```

Specifies the phone type assigned.

Step 5

pattern tag string

#### Example:

```
Router(config-register-dialplan)# pattern 1 30,
```

Specifies the pattern to be matched while dialing from phone.
                                             				Range is 1 to 24.

tag —Range for pattern tag is 1 to
                                                   					 24.

string —It is the pattern to be
                                                   					 matched while dialing from phone. This string is represented as WORD and the
                                                   					 value of this string can be a combination of [0-9.*#,].

Step 6

voice register pool tag

#### Example:

```
Router(config-register-dialplan)# voice register pool 1
```

Defines the voice register pool tag, and enters the voice register
                                             				pool configuration mode.

Step 7

dialplan tag

#### Example:

```
Router(config-register-pool)# dialplan 1
```

Specifies the dialplan to be attached to the pool.

Step 8

voice register global

#### Example:

```
Router(config-register-pool)# voice register global
```

Enters voice register global configuration mode.

Step 9

create profile

#### Example:

```
Router(config-register-global)# create profile
```

Creates the XML configuration files for the phone.

Step 10

voice register pool tag

#### Example:

```
Router(config-register-global)# voice register pool 1
```

Defines the voice register pool tag, and enters the voice register
                                             				pool configuration mode.

Step 11

reset

#### Example:

```
Router(config-register-pool)# reset
```

Resets the phone for the phone configurations to be applied.

Step 12

end

#### Example:

```
Router(config-register-pool)# end
```

Returns to privileged EXEC mode.

### Define Translation
                           	 Rules for Callback-Number on SIP Phones

#### Before you begin

To define up
                                       				to 100 translation rules per translation rule table—Cisco Unified CME 8.6 or a
                                       				later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice translation-rule number

- rule precedence | match-pattern | replace-pattern |

- exit

- voice translation-profile name

- translate { callback-number | called | calling | redirect-called | redirect-target } translation-rule - number

- exit

- voice register pool phone-tag

- number tag dn dn-tag

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

voice translation-rule number

#### Example:

```
Router(config)# voice translation-rule 10
```

Defines a
                                             				translation rule for voice calls and enters voice translation-rule
                                             				configuration mode.

number —Number that identifies the translation
                                                   					 rule. Range: 1 to 2147483647.

Step 4

rule precedence | match-pattern | replace-pattern |

#### Example:

```
Router(cfg-translation-rule)# rule 1 /^9/ //
```

Defines a
                                             				translation rule.

precedence —Priority of the translation rule.
                                                   					 Range: 1 to 100.

Range
                                                         				  limited to 15 maximum rules in CME 8.5 and earlier versions.

match-pattern —Stream Editor (SED) expression used
                                                   					 to match incoming call information. The slash (/) is a delimiter in the
                                                   					 pattern.

replace-pattern —SED expression used to replace the
                                                   					 match pattern in the call information. The slash (/) is a delimiter in the
                                                   					 pattern.

Step 5

exit

#### Example:

```
Router(cfg-translation-rule)# exit
```

Exits voice
                                             				translation-rule configuration mode.

Step 6

voice translation-profile name

#### Example:

```
Router(config)# voice translation-profile eastern
```

Defines a
                                             				translation profile for voice calls.

name —Name of the translation profile. Maximum
                                                   					 length of the voice translation profile name is 31 alphanumeric characters.

Step 7

translate { callback-number | called | calling | redirect-called | redirect-target } translation-rule - number

#### Example:

```
Router(cfg-translation-profile)# translate callback-number 10
```

Associates a
                                             				translation rule with a voice translation profile.

callback-number—Associates the translation rule with the
                                                   					 callback-number.

called—Associates the translation rule with called numbers.

calling—Associates the translation rule with calling numbers.

redirect-called—Associates the translation rule with redirected
                                                   					 called numbers.

redirect-target—Associates the translation rule with transfer-to
                                                   					 numbers and call-forwarding final destination numbers. This keyword is
                                                   					 supported by SIP phones in Cisco Unified CME 4.1 and later versions.

translation-rule- number —Reference number of the translation rule
                                                   					 configured in Step 3 . Range: 1 to 2147483647

Step 8

exit

#### Example:

```
Router(cfg-translation-profile))# exit
```

Exits voice
                                             				translation-profile configuration mode.

Step 9

voice register pool phone-tag

#### Example:

```
Router(config)# voice register pool 3
```

Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone.

Step 10

number tag dn dn-tag

#### Example:

```
Router(config-register-pool)# number 1 dn 17
```

Associates a
                                             				directory number with the SIP phone being configured.

dn dn-tag —identifies the directory number for this
                                                   					 SIP phone as defined by the voice register dn command.

Step 11

end

#### Example:

```
Router(config-translation-profile)# end
```

Returns to
                                             				privileged EXEC mode.

#### Example

The following
                                 		  examples show translation rules defined for callback-number:

```
!
!
voice service voip
ip address trusted list
  ipv4 20.20.20.1
 media flow-around
 allow-connections sip to sip
!
!
voice translation-rule 10
!
!
voice translation-profile eastcoast
!
voice translation-profile eastern
 translate callback-number 10
!
```

#### What to do next

To apply
                                       				voice translation profiles to SIP phones connected to Cisco Unified CME 4.1 or
                                       				a later version, see Apply Voice Translation Rules on SIP Phones in Cisco Unified CME 4.1 and Later .

## Configuration Examples for Dial Plan Features

### Example for
                           	 Configuring Secondary Dial Tone on SCCP Phones

```
telephony-service
		fxo hook-flash
		load 7910 P00403020214
		load 7960-7940 P00305000600
		load 7914 S00103020002
		load 7905 CP7905040000SCCP040701A
		load 7912 CP7912040000SCCP040701A
		max-ephones 100
		max-dn 500
		ip source-address 10.153.233.41 port 2000
		max-redirect 20
		no service directed-pickup
		timeouts ringing 10
		system message XYZ Company
		voicemail 7189
		max-conferences 8 gain -6
		moh music-on-hold.au
		web admin system name admin1 password admin1
		dn-webedit
		time-webedit
		!
		!
		!
		secondary-dialtone 9
```

### Example for
                           	 Configuring Secondary Dial Tone on SIP Phones

A secondary dial
                                 		  tone is played on the phone when comma (',') is found in the pattern. In this
                                 		  example, secondary dial tone is played after the digit 50.

```
voice register dialplan 1
 type 7940-7960-others
 pattern 1 50,

voice register pool 1
 busy-trigger-per-button 2
 id mac 0C11.6780.52A3
 type 7841
number 1 dn 1 dialplan 1 dtmf-relay rtp-nte
 username cisco1 password cisco
 codec g711ulaw
 no vad
 provision-tag 1
```

### Example for
                           	 Configuring Voice Translation Rules

In the following
                                 		  configuration examples, if a user on Cisco Unified CME 1 dials 94155550100, the
                                 		  call matches on dial peer 9415 and uses translation profile profile-9415 .
                                 		  The called number is translated from 94155550100 to 4155550100, as specified by
                                 		  the translate
                                       				called command using translation rule 1.

If a user on
                                 		  Cisco Unified CME 1 calls a phone on Cisco Unified CME 2 by dialing 5105550120,
                                 		  and the call forward number is 94155550100, Cisco Unified CME 1 attempts to
                                 		  forward the call to 94155550100. A 302 message is then sent to
                                 		  Cisco Unified CME 1 with the “Contact:” field translated to 4155550100. When
                                 		  the 302 reaches Cisco Unified CME 1, it matches the To: field in the 302
                                 		  message (5105550120) with dial peer 510. It does incoming translation from
                                 		  4155550100 to 84155550100, and an INVITE with 84155550100 is sent, which
                                 		  matches dial-peer 8415.

Cisco
                                             						Unified CME 1 with 408555.... dialplan-pattern

Cisco
                                             						Unified CME 2 with 510555.... dialplan-pattern

```
dial-peer voice 9415 voip
 translation-profile outgoing profile-9415
 destination-pattern 9415555....
 session protocol sipv2
 session target ipv4:10.4.187.177
 codec g711ulaw
					 
voice translation-profile profile-9415
 translate called 1
 translate redirect-target 1
					 
voice translation-rule 1
 rule 1 /^9415/ /415/
```

```
dial-peer voice 8415 voip
 translation-profile outgoing profile-8415
 destination-pattern 8415555....
 session protocol sipv2
 session target ipv4:10.4.187.177
 codec g711ulaw

dial-peer voice 510 voip
 translation-profile incoming profile-510
 destination-pattern 510555....
 session protocol sipv2
 session target ipv4:10.4.187.188
 codec g711ulaw

voice translation-profile profile-8415
 translate called 1
 translate redirect-target 2

voice translation-profile profile-510
 translate called 3

voice translation-rule 1
 rule 1 /^9415/ /415/

voice translation-rule 2
 rule 2 /^415/ /9415/

voice translation-rule 3
 rule 1 /^8415/ /415/
```

## Feature
                        	 Information for Dial Plan Features

The following table
                           		provides release information about the feature or features described in this
                           		module. This table lists only the software release that introduced support for
                           		a given feature in a given software release train. Unless noted otherwise,
                           		subsequent releases of that software release train also support that feature.

Use Cisco Feature
                           		Navigator to find information about platform support and Cisco software image
                           		support. To access Cisco Feature Navigator, go to www.cisco.com/go/cfn .
                           		An account on Cisco.com is not required.

Feature Name

Cisco Unified CME Versions

Feature
                                       				  Information

Dial Plan
                                       				  Pattern

4.0

Added
                                       				  support for dial plan pattern expansion for call forward and call transfer when
                                       				  the forward or transfer-to target is an individual abbreviated SIP extension or
                                       				  an extension that appear on a SIP phone.

2.1

Strips
                                       				  leading digit pattern from extension number when expanding an extension to an
                                       				  E.164 telephone number. The length of the extension pattern must equal the
                                       				  value configured for the extension-length argument.

1.0

Adds a
                                       				  prefix to extensions to transform them into E.164 numbers.

E.164
                                       				  Enhancements

8.5

Added
                                       				  support for E.164 enhancements.

Secondary
                                       				  Dial Tone

11.6

Support for
                                       				  Secondary Dial Tone on SIP phones.

3.0

Support for
                                       				  secondary dial tone after dialing specified number string.

Voice
                                       				  Translation Rules

8.6

Added
                                       				  support for an increased number of translation rules per translaiton table. Old
                                       				  value is 15 maximum, new value is 100 maximum.

4.1

Added
                                       				  support for voice translation profiles for incoming call legs to a directory
                                       				  number on a SIP phone.

3.4

Added
                                       				  support for voice translation rules to modify the number dialed by extensions
                                       				  on a SIP phone.

3.2

Adds,
                                       				  removes, or transforms digits for calls going to or originating from specified
                                       				  ephone-dns.

| Note | There are instances where phone is registered with Unified CME using
                                             		  the extension number. If the user has to reach the phone using the full +E.164
                                             		  number, a dial peer needs to be configured for the full number. This is
                                             		  applicable only when the extension-length is specified to have the same length
                                             		  as extension number. |
|---|---|

| Note | Because the legacy phone does not have a ‘+’ button, you can
                                                   			 configure dialplan-pattern or translation profile. |
|---|---|

| Tip | In networks that
                                             			 have a single router, you do not need to define dial plan patterns. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 4 | dialplan-pattern tag pattern extension-length length [ extension-pattern epattern ] [ no-reg ] Example: Router(config-telephony)# dialplan-pattern 1 4085550100 extension-length 3 extension-pattern 4.. Note This example
                                                         				  maps all extension numbers 4xx to the PSTN number 40855501xx, so that extension
                                                         				  412 corresponds to 4085550112. | Note | This example
                                                         				  maps all extension numbers 4xx to the PSTN number 40855501xx, so that extension
                                                         				  412 corresponds to 4085550112. | Maps a digit
                                             				pattern for an abbreviated extension-number prefix to the full E.164 telephone
                                             				number pattern. |
| Note | This example
                                                         				  maps all extension numbers 4xx to the PSTN number 40855501xx, so that extension
                                                         				  412 corresponds to 4085550112. |
| Step 5 | end Example: Router(config-telephony)# end | Exits
                                             				configuration mode and enters privileged EXEC mode. |

| Note | This example
                                                         				  maps all extension numbers 4xx to the PSTN number 40855501xx, so that extension
                                                         				  412 corresponds to 4085550112. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register global Example: Router(config)# voice register global | Enters voice
                                             				register global configuration mode to set parameters for all supported SIP
                                             				phones in Cisco Unified CME. |
| Step 4 | dialplan-pattern tag
                                                				  pattern extension-length extension-length [ extension-pattern extension-pattern \| no-reg ] Example: Router(config-register-global)# dialplan-pattern 1 4085550... extension-length 5 | Defines
                                             				pattern that is used to expand abbreviated extension numbers of SIP calling
                                             				numbers in Cisco Unified CME into fully qualified E.164 numbers. |
| Step 5 | call-forward system redirecting-expanded Example: Router(config-register-global)# call-forward system redirecting-expanded | Applies dial
                                             				plan pattern expansion globally to redirecting, including originating and last
                                             				reroute, numbers for SIP extensions in Cisco Unified CME for call forward using
                                             				B2BUA. |
| Step 6 | end Example: Router(config-register-global)# end | Exits
                                             				configuration mode and enters privileged EXEC mode. |

| Step 1 | show telephony-service Use this
                                             				command to verify dial plan patterns in the configuration. Example: The following
                                             				example maps the extension pattern 4.. to the last three digits of the dial
                                             				plan pattern 4085550155: telephony-service
 dialplan-pattern 1 4085550155 extension-length 3 extension-pattern 4.. |
|---|---|
| Step 2 | SCCP: show telephony-service
                                                				  dial-peer or SIP: show dial-peer
                                                				  summary Use the
                                             				command to display dial peers that are automatically created by the dialplan-pattern command. Use this
                                             				command display the configuration for all VoIP and POTS dial peers configured
                                             				for a router, including dial peers created by using the dialplan-expansion (voice
                                                   					 register) command. Example: The following
                                             				example is output from the show dial-peer
                                                   					 summary command displaying information for four dial peers, one
                                             				each for extensions 60001 and 60002 and because the dialplan-expansion command is configured to expand
                                             				6.... to 4085555...., one each for 4085550001 and 4085550002. The latter two
                                             				dial peers will not appear in the running configuration. Router# show dial-peer summary AD                                    PRE PASS                OUT 
TAG    TYPE  MIN  OPER PREFIX    DEST-PATTERN      FER THRU SESS-TARGET    STATT
20010  pots  up   up             60002$             0                       0
20011  pots  up   up             60001$             0                       9
20012  pots  up   up             5105555001$        0                       9
20013  pots  up   up             5105555002$        0                       0 |

| Note | To configure
                                             			 translation rules for voice calls in Cisco CME 3.1 and earlier versions, see Cisco IOS Voice, Video, and
                                                				FAX Configuration Guide . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice translation-rule number Example: Router(config)# voice translation-rule 1 | Defines a
                                             				translation rule for voice calls and enters voice translation-rule
                                             				configuration mode. number—Number that identifies the translation rule. Range: 1 to
                                                   					 2147483647. |
| Step 4 | rule precedence / match-pattern / / replace-pattern / Example: Router(cfg-translation-rule)# rule 1 /^9/ // | Defines a
                                             				translation rule. precedence —Priority of the translation rule.
                                                   					 Range: 1 to 100. Note Range
                                                         				  limited to 15 maximum rules in CME 8.5 and earlier versions. match-pattern —Stream Editor (SED) expression used
                                                   					 to match incoming call information. The slash (/) is a delimiter in the
                                                   					 pattern. replace-pattern —SED expression used to replace the
                                                   					 match pattern in the call information. The slash (/) is a delimiter in the
                                                   					 pattern. | Note | Range
                                                         				  limited to 15 maximum rules in CME 8.5 and earlier versions. |
| Note | Range
                                                         				  limited to 15 maximum rules in CME 8.5 and earlier versions. |
| Step 5 | exit Example: Router(cfg-translation-rule)# exit | Exits voice
                                             				translation-rule configuration mode. |
| Step 6 | voice translation-profile name Example: Router(config)# voice translation-profile name1 | Defines a
                                             				translation profile for voice calls. name —Name of the translation profile. Maximum
                                                   					 length of the voice translation profile name is 31 alphanumeric characters. |
| Step 7 | translate { called \| calling \| redirect-called \| redirect-target } translation-rule-number Example: Router(cfg-translation-profile)# translate called 1 | Associates a
                                             				translation rule with a voice translation profile. called —Associates the translation rule with called
                                                   					 numbers. calling —Associates the translation rule with
                                                   					 calling numbers. redirect-called —Associates the translation rule with redirected
                                                   					 called numbers. redirect-target —Associates the translation rule with transfer-to
                                                   					 numbers and call-forwarding final destination numbers. This keyword is
                                                   					 supported by SIP phones in Cisco Unified CME 4.1 and later versions. translation-rule-number —Reference number of the
                                                   					 translation rule configured in Step 3 .
                                                   					 Range: 1 to 2147483647. |
| Step 8 | end Example: Router(cfg-translation-profile)# end | Returns to
                                             				privileged EXEC mode. |

| Note | Range
                                                         				  limited to 15 maximum rules in CME 8.5 and earlier versions. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-dn tag Example: Router(config)# ephone-dn 1 | Enters
                                             				ephone-dn configuration mode to create an extension (ephone-dn) for a
                                             				Cisco Unified IP phone line, an intercom line, a paging line, a voice-mail
                                             				port, or a message-waiting indicator (MWI). tag —Unique sequence number that identifies this
                                                   					 ephone-dn during configuration tasks. Range is 1 to the maximum number of
                                                   					 ephone-dns allowed on the router platform. See the CLI help for the maximum
                                                   					 value for this argument. |
| Step 4 | translation-profile { incoming \| outgoing } name Example: Router(config-ephone-dn)# translation-profile outgoing name1 | Assigns a
                                             				translation profile for incoming or outgoing call legs to or from
                                             				Cisco Unified IP phones. You can
                                                   					 also use an ephone-dn template to apply this command to one or more directory
                                                   					 numbers. If you use an ephone-dn template to apply a command and you use the
                                                   					 same command in ephone-dn configuration mode for the same directory number, the
                                                   					 value that you set in ephone-dn configuration mode has priority. |
| Step 5 | end Example: Router(config-ephone-dn)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-dn tag Example: Router(config)# ephone-dn 1 | Enters
                                             				ephone-dn configuration mode to create directory number for a Cisco Unified IP
                                             				phone line, an intercom line, a paging line, a voice-mail port, or a
                                             				message-waiting indicator (MWI). |
| Step 4 | translate { called \| calling } translation-rule-tag Example: Router(config-ephone-dn)# translate called 1 | Specifies rule
                                             				to be applied to the directory number being configured. translation-rule-tag —Reference number of
                                                   					 previously configured translation rule. Range: 1 to 2147483647. You can
                                                   					 use an ephone-dn template to apply this command to one or more directory
                                                   					 numbers. If you use an ephone-dn template to apply a command to a directory
                                                   					 number and you also use the same command in ephone-dn configuration mode for
                                                   					 the same directory number, the value that you set in ephone-dn configuration
                                                   					 mode has priority. |
| Step 5 | end Example: Router(cfg-translation-profile)# end | Exits
                                             				configuration mode and enters privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register dn dn-tag Example: Router(config)# voice register dn 1 | Enters voice
                                             				register dn configuration mode to define a directory number for a SIP phone,
                                             				intercom line, voice port, or a message-waiting indicator (MWI). |
| Step 4 | translation-profile incoming name Example: Router(config-register-dn)# translation-profile incoming name1 | Assigns a
                                             				translation profile for incoming call legs to this directory number. |
| Step 5 | end Example: Router(config-register-dn)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register pool pool-tag Example: Router(config)# voice register pool 3 | Enters voice
                                             				register pool configuration mode to set phone-specific parameters for SIP
                                             				phones. |
| Step 4 | translate-outgoing { called \| calling } rule-tag Example: Router(config-register-pool)# translate-outgoing called 1 | Specifies an
                                             				already configured voice translation rule to be applied to SIP phone being
                                             				configured. |
| Step 5 | end Example: Router(config-register-global)# end | Exits
                                             				configuration mode and enters privileged EXEC mode. |

| Step 1 | show voice
                                                				  translation-profile [ name ] This command
                                             				displays the configuration of one or all translation profiles. Example: Router# show voice translation-profile profile-8415 Translation Profile: profile-8415
  Rule for Calling number: 4
  Rule for Called number: 1
  Rule for Redirect number: 5
  Rule for Redirect-target number: 2 |
|---|---|
| Step 2 | show voice
                                                				  translation-rule [ number ] This command
                                             				displays the configuration of one or all translation rules. Example: Router# show voice translation-rule 6 Translation-rule tag: 6
  Rule 1:
  Match pattern: 65088801..
  Replace pattern: 6508880101
  Match type: none   Replace type: none
  Match plan: none   Replace plan: none |
| Step 3 | test voice translation-rule number This command
                                             				enables you to test your translation rules. Example: Router(config)# voice translation-rule 5 Router(cfg-translation-rule)# rule 1 /201/ /102/ Router(cfg-translation-rule)# exit Router(config)# exit Router# test voice translation-rule 5 2015550101 Matched with rule 5
Original number:2015550101  Translated number:1025550101
Original number type: none    Translated number type: none
Original number plan: none    Translated number plan: none |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 4 | secondary-dialtone digit-string Example: Router(config-telephony)# secondary-dialtone 9 | Activates a
                                             				secondary dial tone when digit-string is dialed. digit-string —String of up to 32 digits that, when
                                                   					 dialed, activates a secondary dial tone. Typically, the digit-string is a predefined PSTN access prefix. |
| Step 5 | end Example: Router(config-telephony)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice register dialplan tag Example: Router(config)# voice register dialplan 1 | Enters voice register dialplan configuration mode. tag —Range for dialplan tag is 1 to
                                                   					 24. |
| Step 4 | type 7940-7960-others Example: Router(config-register-dialplan)# type 7940-7960-others | Specifies the phone type assigned. |
| Step 5 | pattern tag string Example: Router(config-register-dialplan)# pattern 1 30, | Specifies the pattern to be matched while dialing from phone.
                                             				Range is 1 to 24. tag —Range for pattern tag is 1 to
                                                   					 24. string —It is the pattern to be
                                                   					 matched while dialing from phone. This string is represented as WORD and the
                                                   					 value of this string can be a combination of [0-9.*#,]. |
| Step 6 | voice register pool tag Example: Router(config-register-dialplan)# voice register pool 1 | Defines the voice register pool tag, and enters the voice register
                                             				pool configuration mode. |
| Step 7 | dialplan tag Example: Router(config-register-pool)# dialplan 1 | Specifies the dialplan to be attached to the pool. |
| Step 8 | voice register global Example: Router(config-register-pool)# voice register global | Enters voice register global configuration mode. |
| Step 9 | create profile Example: Router(config-register-global)# create profile | Creates the XML configuration files for the phone. |
| Step 10 | voice register pool tag Example: Router(config-register-global)# voice register pool 1 | Defines the voice register pool tag, and enters the voice register
                                             				pool configuration mode. |
| Step 11 | reset Example: Router(config-register-pool)# reset | Resets the phone for the phone configurations to be applied. |
| Step 12 | end Example: Router(config-register-pool)# end | Returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice translation-rule number Example: Router(config)# voice translation-rule 10 | Defines a
                                             				translation rule for voice calls and enters voice translation-rule
                                             				configuration mode. number —Number that identifies the translation
                                                   					 rule. Range: 1 to 2147483647. |
| Step 4 | rule precedence \| match-pattern \| replace-pattern \| Example: Router(cfg-translation-rule)# rule 1 /^9/ // | Defines a
                                             				translation rule. precedence —Priority of the translation rule.
                                                   					 Range: 1 to 100. Note Range
                                                         				  limited to 15 maximum rules in CME 8.5 and earlier versions. match-pattern —Stream Editor (SED) expression used
                                                   					 to match incoming call information. The slash (/) is a delimiter in the
                                                   					 pattern. replace-pattern —SED expression used to replace the
                                                   					 match pattern in the call information. The slash (/) is a delimiter in the
                                                   					 pattern. | Note | Range
                                                         				  limited to 15 maximum rules in CME 8.5 and earlier versions. |
| Note | Range
                                                         				  limited to 15 maximum rules in CME 8.5 and earlier versions. |
| Step 5 | exit Example: Router(cfg-translation-rule)# exit | Exits voice
                                             				translation-rule configuration mode. |
| Step 6 | voice translation-profile name Example: Router(config)# voice translation-profile eastern | Defines a
                                             				translation profile for voice calls. name —Name of the translation profile. Maximum
                                                   					 length of the voice translation profile name is 31 alphanumeric characters. |
| Step 7 | translate { callback-number \| called \| calling \| redirect-called \| redirect-target } translation-rule - number Example: Router(cfg-translation-profile)# translate callback-number 10 | Associates a
                                             				translation rule with a voice translation profile. callback-number—Associates the translation rule with the
                                                   					 callback-number. called—Associates the translation rule with called numbers. calling—Associates the translation rule with calling numbers. redirect-called—Associates the translation rule with redirected
                                                   					 called numbers. redirect-target—Associates the translation rule with transfer-to
                                                   					 numbers and call-forwarding final destination numbers. This keyword is
                                                   					 supported by SIP phones in Cisco Unified CME 4.1 and later versions. translation-rule- number —Reference number of the translation rule
                                                   					 configured in Step 3 . Range: 1 to 2147483647 |
| Step 8 | exit Example: Router(cfg-translation-profile))# exit | Exits voice
                                             				translation-profile configuration mode. |
| Step 9 | voice register pool phone-tag Example: Router(config)# voice register pool 3 | Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone. |
| Step 10 | number tag dn dn-tag Example: Router(config-register-pool)# number 1 dn 17 | Associates a
                                             				directory number with the SIP phone being configured. dn dn-tag —identifies the directory number for this
                                                   					 SIP phone as defined by the voice register dn command. |
| Step 11 | end Example: Router(config-translation-profile)# end | Returns to
                                             				privileged EXEC mode. |

| Note | Range
                                                         				  limited to 15 maximum rules in CME 8.5 and earlier versions. |
|---|---|

| Cisco
                                             						Unified CME 1 with 408555.... dialplan-pattern | Cisco
                                             						Unified CME 2 with 510555.... dialplan-pattern |
|---|---|
| dial-peer voice 9415 voip
 translation-profile outgoing profile-9415
 destination-pattern 9415555....
 session protocol sipv2
 session target ipv4:10.4.187.177
 codec g711ulaw
					 
voice translation-profile profile-9415
 translate called 1
 translate redirect-target 1
					 
voice translation-rule 1
 rule 1 /^9415/ /415/ | dial-peer voice 8415 voip
 translation-profile outgoing profile-8415
 destination-pattern 8415555....
 session protocol sipv2
 session target ipv4:10.4.187.177
 codec g711ulaw

dial-peer voice 510 voip
 translation-profile incoming profile-510
 destination-pattern 510555....
 session protocol sipv2
 session target ipv4:10.4.187.188
 codec g711ulaw

voice translation-profile profile-8415
 translate called 1
 translate redirect-target 2

voice translation-profile profile-510
 translate called 3

voice translation-rule 1
 rule 1 /^9415/ /415/

voice translation-rule 2
 rule 2 /^415/ /9415/

voice translation-rule 3
 rule 1 /^8415/ /415/ |

| Feature Name | Cisco Unified CME Versions | Feature
                                       				  Information |
|---|---|---|
| Dial Plan
                                       				  Pattern | 4.0 | Added
                                       				  support for dial plan pattern expansion for call forward and call transfer when
                                       				  the forward or transfer-to target is an individual abbreviated SIP extension or
                                       				  an extension that appear on a SIP phone. |
| 2.1 | Strips
                                       				  leading digit pattern from extension number when expanding an extension to an
                                       				  E.164 telephone number. The length of the extension pattern must equal the
                                       				  value configured for the extension-length argument. |
| 1.0 | Adds a
                                       				  prefix to extensions to transform them into E.164 numbers. |
| E.164
                                       				  Enhancements | 8.5 | Added
                                       				  support for E.164 enhancements. |
| Secondary
                                       				  Dial Tone | 11.6 | Support for
                                       				  Secondary Dial Tone on SIP phones. |
| 3.0 | Support for
                                       				  secondary dial tone after dialing specified number string. |
| Voice
                                       				  Translation Rules | 8.6 | Added
                                       				  support for an increased number of translation rules per translaiton table. Old
                                       				  value is 15 maximum, new value is 100 maximum. |
| 4.1 | Added
                                       				  support for voice translation profiles for incoming call legs to a directory
                                       				  number on a SIP phone. |
| 3.4 | Added
                                       				  support for voice translation rules to modify the number dialed by extensions
                                       				  on a SIP phone. |
| 3.2 | Adds,
                                       				  removes, or transforms digits for calls going to or originating from specified
                                       				  ephone-dns. |