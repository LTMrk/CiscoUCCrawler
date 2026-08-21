---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-command-reference-cme-cr-cme-cr-chapter-0101-html-0d587a51e2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/command/reference/cme_cr/cme_cr_chapter_0101.html
retrieved_at: 2026-08-21T22:56:03.434326+00:00
---

Cisco Unified Communications Manager Express Command Reference

# Cisco Unified Communications Manager Express Command Reference

Updated: July 19, 2018

Chapter: Cisco Unified CME Commands: F

## Chapter: Cisco Unified CME Commands: F

# Cisco Unified CME Commands: F

## fac

To enable all standard feature access codes (FACs) or to create and
                              		  enable individual custom FACs, use the fac command in telephony-service
                              		  configuration mode. To disable FACs, use the no form of this command.

fac { standard | custom { alias alias-tag | feature }
                              
                              }

fac refer

no fac { {standard | custom {alias alias-tag | feature }

### Syntax Description

standard

All predefined standard FACs are enabled.

custom

User-defined FAC for selecting a particular feature or
                                          						function from the predefined set of features is enabled.

alias

Alternative FAC for dialing an existing FAC or existing FAC
                                          						plus extra digits without removing the existing FAC is enabled.

alias-tag

Unique number that identifies this alias during
                                          						configuration tasks. Range: 0 to 9.

custom-fac

User-defined code to dial using the keypad on an IP or
                                          						analog phone. Code can be up to 256 characters and can contain numbers 0 to 9
                                          						and * and #.

to

Maps custom FAC being configured to specified target.

existing-fac

Already configured custom FAC that is automatically dialed
                                          						when the phone user dials the custom FAC being configured.

extra-digits

(Optional) Additional digits that are automatically dialed
                                          						when the phone user dials the custom FAC being configured. Valid entries are:

- target extension —Telephone or extension
                                             						  number in Cisco Unified CME to which the incoming calls are forwarded. Used
                                             						  with the Call Forward feature.

- group number —Pickup group number, for a
                                             						  group other than the local group number. Used with the Pickup Group feature.

- pickup extension —Telephone or extension
                                             						  number in Cisco Unified CME to be picked up when ringing. To be used with the
                                             						  Pickup Direct feature.

- park-slot number —Number on which calls are to be
                                             						  temporarily parked. Use with the Call Park feature. Target park slot must be
                                             						  already configured in Cisco Unified CME.

- pilot number —Telephone or extension number
                                             						  configured as a the pilot number for an ephone hunt group to be joined. Hunt
                                             						  group to be joined must allow dynamic membership.

feature

Predefined alphabetic string that identifies a particular
                                          						feature or function. Valid entries are:

- callfwd all —Directs system to forward all
                                             						  incoming calls for this telephone or extension number.

- callfwd cancel —Directs system to cancel the
                                             						  call-forward-all selection.

- ccw —Disables the Call Waiting
                                             						  feature.

- dnd —Enables Do Not Disturb
                                             						  (DND) feature on SCCP phones. Not supported for SIP phones.

- dpark-retrieval —Enables
                                             						  Directed Call Park Retrieval feature. Applies to both SIP and SCCP phones.

- ephone-hunt cancel —Leaves an ephone hunt group
                                             						  that is configured to allow dynamic membership.

- ephone-hunt hlog —Activates or deactivates hunt
                                             						  group logout functionality, changing the status of the an ephone-dn for a hunt
                                             						  group agent from ready to not-ready or from not-ready to ready.

- ephone-hunt hlog-phone —Activates or deactivates
                                             						  phone-level hunt group logout functionality, changing the status of all the
                                             						  extensions on a hunt group member phone from ready to not-ready or from
                                             						  not-ready to ready.

- ephone-hunt join —Joins an ephone hunt group that
                                             						  is configured to allow dynamic membership. If multiple hunt groups have been
                                             						  created that allow dynamic membership, the hunt group to be joined is
                                             						  identified by its pilot number.

- park —Enables Call Park feature.

- pickup direct —Picks up a ringing call at any
                                             						  extension. Applies to both SIP and SCCP phones.

- pickup group —Picks up a ringing call in a
                                             						  different pickup group than yours. Applies to both SIP and SCCP phones.

- pickup local —Picks up a ringing call in your
                                             						  pickup group. Applies to both SIP and SCCP phones.

- redial —Redials the last number
                                             						  called.

- trnsfvm —Activates the Transfer
                                             						  to Voice-Mail feature.

- voicemail —Dials the voice-mail
                                             						  number.

### Command Default

FACs are disabled on IP phones.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)XC

Cisco Unified CME 4.0

This command was introduced.

12.4(9)T

Cisco Unified CME 4.0

This command was integrated into Cisco IOS Release
                                          						12.4(9)T.

12.4(15)XZ

Cisco Unified CME 4.3

Standard FAC and trnsfvm keyword for a custom FAC
                                          						were added for transfer to voice mail.

12.4(20)T

Cisco Unified CME 7.0

This command was integrated into Cisco IOS Release
                                          						12.4(20)T.

12.4(22)YB

Cisco Unified CME 7.1

The dpark-retrieval keyword was added
                                          						and support for SIP phones was added for the park direct , park group , and park local keywords.

12.4(24)T

Cisco Unified CME 7.1

This command was integrated into Cisco IOS Release
                                          						12.4(24)T.

15.0(1)XA

Cisco Unified CME 8.0

This command was modified. The ccw keyword was added for a custom
                                          						FAC.

15.1(1)T

Cisco Unified CME 8.0

This command was integrated into Cisco IOS Release
                                          						15.1(1)T.

### Usage Guidelines

Use this command to enable all predefined standard FACs or to create
                              		  one or more custom FACs.

FACs enable phone users to use the keypad on an analog or IP phone
                              		  registered in Cisco Unified CME to select or activate/deactivate a particular
                              		  feature or function from a predefined set of features. For example, a phone
                              		  user might press **1, then press 2345 to forward all incoming calls to
                              		  extension 2345.

Standard FACs and custom FACs are mutually exclusive. You can enable
                              		  all standard FACs or create and enable one or more custom FACs.

Most FACs are valid only immediately after a phone user goes
                              		  off-hook. The only exception is the call-park FAC. The call-park FAC actually
                              		  invokes a call transfer to a park slot. To use the call-park FAC, a phone user
                              		  must have an active call and must press the Transfer soft key (IP phone) or
                              		  hookflash (analog phone) before dialing the call-park FAC. Dialing the FAC for
                              		  the Call Park feature does not use the Park soft key function.

Use the fac standard command to enable all predefined
                              		  standard FACs for all SCCP phones registered in Cisco Unified CME.

Use the fac custom command to create an
                              		  individual custom FAC for selecting a particular feature or function from the
                              		  predefined feature set.

Use the fac custom command with the alias keyword to create an alternative
                              		  (custom) FAC for dialing an existing FAC, or existing FAC plus extra digits
                              		  without removing the existing FAC. For example, an alias can be created to
                              		  allow the phone user to press **1 to forward all incoming calls to a particular
                              		  extension without requiring the phone user to dial the target extension
                              		  number.

To disable all custom FACs, use the fac standard command, which enables all standard
                              		  FACs. To disable all standard FACs or to disable an individual custom FAC, use
                              		  the no form of the fac command.

Use the show telephony-service fac command to display a list of FACs that are
                              		  configured on the Cisco Unified CME router.

## Examples

The following example shows how to enable standard FACs for all
                              		  phones:

```
Router(config)# telephony-service Router(config-telephony)# fac standard fac standard is set!
```

The following example shows the output from the show telephony-service fac command when standard FACs are enabled:

```
Router# show telephony-service fac telephony-service fac standard
 callfwd all **1
 callfwd cancel **2
 pickup local **3
 pickup group **4
 pickup direct **5
 park **6
 dnd **7
 redial **8
 voicemail **9
 ephone-hunt join *3
 ephone-hunt cancel #3
 ephone-hunt hlog *4
 ephone-hunt hlog-phone *5
 trnsfvm *6
 dpark-retrieval **10
 cancel call waiting *1
```

The following example shows how the standard FAC for the Call Forward
                              		  All feature is changed to a custom FAC (#45). Then an alias is created to map a
                              		  second custom FAC to #45 plus an extension (1111). The second custom FAC (#44)
                              		  allows the phone user to press #44 to forward all calls all calls to extension
                              		  1111, without requiring the phone user to dial the extra digits that are the
                              		  extension number.

```
Router(config)# telephony-service Router(config-telephony)# fac custom callfwd all #45 fac callfwd all code has been configured to #45
Router(config-telephony)# fac custom alias 0 #44 to #451111 fac alias0 code has been configurated to #44!
alias0 map code has been configurated to #451111!
```

The following example shows how to create three aliases for the Group
                              		  Pickup feature. The FAC for group pickup is **4. The three new custom FACs are
                              		  #1, #2, and #4 to pickup groups 121, 122, and 124, respectively. This allows a
                              		  phone user to press #1 to pick up calls in group 121, #2 to pick up calls in
                              		  group 122, and #4 to pick up calls in group 124.

```
Router(config)# telephony-service Router(config-telephony)# fac custom pickup group **4 fac pickup group code has been configured to **4
Router(config-telephony)# fac custom alias 1 #1 to **4121 fac alias1 code has been configurated to #1!
alias1 map code has been configurated to **4121!
Router(config-telephony)# fac custom alias 2 #2 to **4122 fac alias2 code has been configurated to #2!
alias2 map code has been configurated to **4122!
Router(config-telephony)# fac custom alias 4 #4 to **4124 fac alias4 code has been configurated to #4!
alias4 map code has been configurated to **4124!
```

The following example shows the output from the show telephony-service fac command when custom FACs are configured:

```
Router# show telephony-service fac telephony-service fac custom
 callfwd all #45
 alias 0 #44 to #451111
 alias 1 #1 to **4121
 alias 2 #2 to **4122
 alias 4 #4 to **4124
```

### Related Commands

Command

Description

show telephony-service fac

Displays list of FACs that are configured on Cisco Unified
                                          						CME.

## fac refer

To send the SIP REFER to a SIP phone. use the fac refer command in voice register global
                              		  configuration mode. To allow Cisco Unified CME to handle the SIP REFER
                              		  internally, use the no form of this command.

fac refer

no fac refer

### Syntax Description

lpcor-group

Name of the LPCOR resource group.

### Command Default

Fac refer is enabled.

### Command Modes

Voice register global configuration (config-register-global)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.1(3)T

Cisco Unified CME 8.5

This command was introduced.

### Usage Guidelines

Use this ommand to control the SIP REFER to be sent to a SIP phone.
                              		  The fac refer command is enabled in Cisco Unified CME by default to allow Cisco
                              		  Unified CME to pass the REFER to the SIP phone, thereby enabling the phone to
                              		  make a new call towards Cisco Unified CME . Cisco Unified CME accepts the new
                              		  invite message as a new call and requires the call transferree to enter a
                              		  forced authorization code (FAC) again.

Use the no fac refer command to allow Cisco Unified CME to handle the
                              		  SIP REFER internally instead of passing the call towards the SIP phone.

## Examples

The following example shows no fac refer configured in voice register
                              		  global:

```
Router#show run
!
voice register global
 no fac refer
```

### Related Commands

Command

Description

show voice register global

Displays all global configuration parameters associated
                                          						with SIP phones.

## fail-connect-time

To specify the maximum time to wait for establishing VPN tunnel
                              		  including establishing of SSL/DTLS and login or connect requests or responses,
                              		  use the fail-connect-time command in vpn-profile configuration mode. To disable the
                              		  fail-connect-time configuration, use the no form of this command.

fail-connect-time seconds

### Syntax Description

seconds

Failure-to-connect time, in seconds. Range: 0 to 600
                                          						seconds. Default: 30 seconds.

### Command Default

Default fail-connect-time is 30 seconds.

### Command Modes

Vpn-profile configuration (conf-vpn-profile)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.1(3)T

Cisco Unified CME 8.5

This command was introduced.

### Usage Guidelines

Use this command to specify the fail-to-connect time for a
                              		  vpn-profile. The fail-to-connect time specifies the maximum time to wait for
                              		  establishing VPN tunnel including establishing of SSL/DTLS and login/connect
                              		  request/response. The fail-to-connect time ranges from 0 seconds to 600
                              		  seconds. The default fail-to-connect time is 30 seconds.

## Examples

The following example shows fail-connect-time set to 50 seconds for
                              		  vpn-profile 4:

```
Router# show run
!
!
voice service voip
 ip address trusted list
  ipv4 20.20.20.1
 vpn-group 1
  vpn-gateway 1 https://9.10.60.254/SSLVPNphone
  vpn-trustpoint 1 trustpoint cme_cert root
  vpn-hash-algorithm sha-1
 vpn-profile 1
  keepalive 50
  host-id-check disable
 vpn-profile 2
  mtu 1300
  password-persistent enable
  host-id-check enable
 vpn-profile 4
  fail-connect-time 50
 sip
!
```

### Related Commands

Command

Description

vpn-profile

Defines a VPN-profile.

## fastdial

To create an
                              		  entry for a personal speed-dial number, use the fastdial command in ephone or ephone-template configuration mode. To delete a
                              		  personal speed-dial number, use the no form of
                              		  this command.

fastdial dial-tag number name name-string

no fastdial dial-tag

### Syntax Description

dial-tag

Unique
                                          						sequence number that ranges from 1 to 100 and is used to identify a particular
                                          						personal speed-dial number during configuration tasks.

number

Telephone number or extension to be dialed.

name name-string

Label
                                          						to appear in the Personal Speed Dial menu, containing a string of up to 24
                                          						alphanumeric characters. Personal speed dial is handled through an XML request,
                                          						so characters that have special meaning to HTTP, such as ampersand (&),
                                          						percent sign (%), semicolon (;), angle brackets (< >), and vertical bars
                                          						(||), are not allowed.

### Command Default

No personal
                              		  speed-dial numbers are present.

### Command Modes

Voice register pool configuration (config-register-pool) Ephone configuration (config-ephone) Ephone-template configuration (config-ephone-template)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

12.2(15)ZJ

Cisco
                                          						CME 3.0

This
                                          						command was introduced.

12.3(4)T

Cisco
                                          						CME 3.0

This
                                          						command was integrated into Cisco IOS Release 12.3(4)T.

12.4(4)XC

Cisco
                                          						Unified CME 4.0

This
                                          						command was made available in ephone-template configuration mode.

12.4(9)T

Cisco
                                          						Unified CME 4.0

This
                                          						command in ephone-template configuration mode was integrated into Cisco IOS
                                          						Release 12.4(9)T.

15.4(3)M

Cisco
                                          						Unified CME 10.5

This
                                          						command was modified to increase the range from 24 to 100.

### Usage Guidelines

This command is
                              		  supported only on certain Cisco Unified IP phones, such as the 7940, 7960,
                              		  7960G, 7970G, and 7971G-GE. To determine whether personal speed-dial menu is
                              		  supported on your IP phone, see the Cisco Unified CME user
                                 			 documentation for your IP phone model.

Phone users
                              		  access personal speed-dial numbers through the Directories > Local Services
                              		  > Personal Speed Dial menu. Personal speed-dial numbers appear on this menu
                              		  in the order in which they are entered during configuration.

If you use an
                              		  ephone template to apply a command to a phone and you also use the same command
                              		  in ephone configuration mode for the same phone, the value that you set in
                              		  ephone configuration mode has priority.

## Examples

The following
                              		  example creates a directory of five personal speed-dial numbers for an IP
                              		  phone:

```
Router(config)# ephone 1 Router(config-ephone)# fastdial 1 5001 name Front Register Router(config-ephone)# fastdial 2 5002 name Security Router(config-ephone)# fastdial 3 5003 name Rear Register Router(config-ephone)# fastdial 4 5004 name Office Router(config-ephone)# fastdial 5 912135550122 Accounting
```

### Related Commands

Command

Description

ephone-template (ephone)

Applies a template to the ephone being configured.

show telephony-service ephone-template

Displays the contents of ephone templates.

## feature-button

To enable feature button configuration on a line key, use the
                              		  feature-button command in ephone, ephone-template, voice user profile, or voice
                              		  logout profile configuration mode. To disable the feature button configuration
                              		  on a line key, use the no form of this command.

feature-button index index <feature identifier> [label <label> ]

no feature-button index index <feature identifier> [label <label> ]

### Syntax Description

index

Index number of a specific feature type. One from the total
                                          						24 feature IDs.

feature identifier

One of the following feature or stimulus IDs: Redial, Hold,
                                          						Trnsfer, Cfwdall, Privacy, MeetMe, Confrn, Park, Pickup. Gpickup, Mobility,
                                          						Dnd, ConfList, RmLstC, CallBack, NewCall, EndCall, HLog, NiteSrv, Acct, Flash,
                                          						Login, TrnsfVM, LiveRcd.

label

Defines non-default text label for PLK button.

### Command Default

No feature-button is configured.

### Command Modes

Ephone configuration (config-ephone) Ephone-template configuration (config-ephone-template) Voice user-profile configuration (config-user-profile) Voice logout-profile configuration (config-logout-profile)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.0(1)XA

Cisco Unified CME 8.0

This command was introduced.

15.1(1)T

Cisco Unified CME 8.0

This command was integrated into Cisco IOS Release
                                          						15.1(1)T.

15.1(3)T

Cisco Unified CME 8.5

This command was modified to configure feature button on a
                                          						phone’s line key. Feature button index number and feature ID keywords were
                                          						added.

15.2(4)M

Cisco Unified CME 9.1

This command was modified to add label < label > for the PLK button.

### Usage Guidelines

Use this command to configure a DnD feature button as a short cut for
                              		  the DnD softkey. This command with the privacy keyword takes precedence over
                              		  the privacy-button command. If a feature-button is configured for DnD, the privacy-button command will be ignored and
                              		  the privacy button must be configured through the feature-button command to
                              		  take effect.

In Cisco Unified CME 8.5 and later versions, the feature-button
                              		  command allows you to program a phone’s line key to function as a feature
                              		  button. You can configure one of the following 24 feature IDs: Redial, Hold,
                              		  Trnsfer, Cfwdall, Privacy, MeetMe, Confrn, Park, Pickup. Gpickup, Mobility,
                              		  Dnd, ConfList, RmLstC, CallBack, NewCall, EndCall, HLog, NiteSrv, Acct, Flash,
                              		  Login, TrnsfVM, LiveRcd

## Examples

The following example shows how to configure feature buttons:

```
Router(config)# ephone 1 Router(config-ephone) feature-button 1 privacy Router(config-ephone) feature-button 2 dnd Router(config-ephone) feature-button 3 Hlog label Agent Hlogout The following example shows feature buttons configured in ephone template 9 and ephone template 10:
Router# show telephony-service ephone-template
ephone-template 9
conference drop-mode never
conference add-mode all
conference admin: No
max-calls-per-button 8
busy-trigger-per-button 0
privacy default
feature-button 1 Endcall
feature-button 3 Mobility
Always send media packets to this router: No
Preferred codec: g711ulaw
keepalive 30 auxiliary 30
User Locale: US
Network Locale: US
lpcor type:
lpcor (incoming):        (outgoing):
ephone-template 10
conference drop-mode never
conference add-mode all
conference admin: No
max-calls-per-button 8
busy-trigger-per-button 0
privacy default
feature-button 1 Park
feature-button 2 MeetMe
feature-button 3 CallBack
button-layout 1 line
button-layout 2-4 speed-dial
button-layout 5-6 blf-speed-dial
MLPP Service Domain Network none (0)
!
```

### Related Commands

Command

Description

privacy-button

Enables the privacy feature button on an IP phone.

show telephony-service ephone

Displays the information about ephone configuration in a
                                          						Cisco CallManager Express (Cisco CME) system.

show telephony-service ephone-dn-template

Displays the information about ephone-template’s
                                          						configurations.

## feature-button
                        	 (voice_register_pool)

To configure
                              		  feature button configuration on a line key, use the feature-button command in
                              		  voice register pool or voice register template configuration mode. To disable
                              		  the feature button configuration on a line key, use the no form of this
                              		  command.

feature-button [ index number feature identifier feature id ]

no feature button [ index number feature identifier feature id ]

### Syntax Description

index

Index
                                          						number of a specific feature type. One from the total 24 feature IDs.

feature
                                          						identifier

One of
                                          						the following feature or stimulus IDs: Redial, Hold, Trnsfer, Cfwdall, Privacy,
                                          						MeetMe, Confrn, Park, Pickup, Gpickup, Mobility, NewCall, EndCall, Dnd,
                                          						ConfList, NewCall, HLog, Trnsfer.

### Command Default

Feature-button
                              		  configuration on a line key is disabled.

### Command Modes

Voice register pool configuration (config-register-pool) Voice register template configuration (config-register-template)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Product

Modification

15.1(3)T

Cisco
                                          						Unified CME 8.5

This
                                          						command was introduced.

### Usage Guidelines

Use this command
                              		  to program a phone’s line key to function as a feature button. You can
                              		  configure one of the following 24 features IDs: Redial, Hold, Trnsfer, Cfwdall,
                              		  Privacy, MeetMe, Confrn, Park, Pickup, Gpickup, Mobility, NewCall, EndCall,
                              		  Dnd, ConfList, NewCall, HLog, Trnsfer. The feature ID list for the command is
                              		  incrementally updated across Unified CME releases.

## Examples

The following
                              		  example shows feature button configured in voice register pool 50:

```
voice register pool  50
 id mac 001E.7AC4.DC73
 feature-button 1 NewCall
 type 7965
 number 1 dn 65
 template 1
 dtmf-relay rtp-nte
 speed-dial 1 2001 label "SD1-2001"
 speed-dial 3 2003 label "SD3-2003"
 blf-speed-dial 1 3001 label "BLFl1-3001"
!
```

### Related Commands

Command

Description

show voice register pool

Displays all configuration information associated with a particular voice
                                          						register pool.

## features blocked

To prevent one or more features from being used on a Cisco Unified
                              		  CME phone, use the features blocked command in ephone-template configuration
                              		  mode. To allow all features to be used, use the no form of this command.

features blocked [ CFwdAll ] [ Confrn ] [ GpickUp ] [ Park ] [ PickUp ] [ Trnsfer ]

no features blocked

### Syntax Description

CFwdAll

Call forward all calls.

Confrn

Conference.

GpickUp

Group call pickup.

Park

Call park.

PickUp

Directed or local call pickup. This includes pickup
                                          						last-parked call and pickup from another extension or park slot.

Trnsfer

Call transfer.

### Command Default

Features are not blocked.

### Command Modes

Ephone-template configuration (config-ephone-template)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)XC

Cisco Unified CME 4.0

This command was introduced.

12.4(9)T

Cisco Unified CME 4.0

This command was integrated into Cisco IOS Release
                                          						12.4(9)T.

### Usage Guidelines

Use this command to specify one or more features to be blocked in an
                              		  ephone template, then apply the template in ephone configuration mode to one or
                              		  more ephones to prevent the use of the specified features by those ephones.
                              		  This feature can be used on IP phones and analog phones. After applying the
                              		  template, any soft keys associated with the blocked features will still be
                              		  visible but will not have any effect.

Use the show telephony-service ephone-template command to display the contents of
                              		  ephone templates.

## Examples

In the following example, call park and call transfer are blocked on
                              		  ephone 3.

```
ephone-template 1
 features blocked Park Trnsfer
ephone-dn 2
 number 2333
ephone 3
 button 1:2
 ephone-template 1
```

The following example blocks the use of the conference feature on
                              		  ephone 3, which is an analog phone, by using a template.

```
ephone-template 1
 features blocked Confrn
ephone-dn 78
 number 2579
ephone  3
 ephone-template 1
 mac-address C910.8E47.1282
 type anl
 button  1:78
```

### Related Commands

Command

Description

ephone-template (ephone)

Applies a template to the ephone being configured.

show telephony-service ephone-template

Displays the contents of ephone templates.

## feed

To enable an audio stream for multicast from a external live audio
                              		  feed connected directly to the router by a foreign exchange office (FXO) or an
                              		  E&M analog voice port, use the feed command in ephone-dn configuration mode.
                              		  To disable the multicast audio stream, use the no form of this command.

feed ip ip-address port port-number [ route ip-address ] [ out-call outcall-number ]

no feed ip

### Syntax Description

ip ip-address

Indicates that a particular audio stream is to be used as a
                                          						multicast source and specifies the destination IP address for multicast.

port port-number

Specifies the media port for multicast. Range is from 2000
                                          						to 65535. Port 2000 is recommended because this port is already used for normal
                                          						Real-Time Transport Protocol (RTP) media transmissions between IP phones and
                                          						the Cisco CallManager Express (Cisco CME) router.

route ip-address

(Optional) Indicates the specific router interface on which
                                          						to transmit the IP multicast packets. The default is that the audio stream is
                                          						automatically output on the interface that corresponds to the address that was
                                          						configured with the ip source-address command.

out-call outcall-number

(Optional) Sets up a call to the outcall number in order to
                                          						connect to a live audio feed. If this keyword is not used, the live feed is
                                          						assumed to derive from an incoming call to the ephone-dn that is being
                                          						configured.

### Command Default

No multicast audio stream is enabled on an extension.

### Command Modes

Ephone-dn configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco CME 3.0

This command was introduced.

12.3(4)T

Cisco CME 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

When this command is used, a connection for a live feed audio stream
                              		  is established as an automatically connected voice call. If the out-call keyword is used, the Cisco CME system calls out to the
                              		  specified number for the audio stream. If the out-call keyword is not used, it is assumed
                              		  that the call is incoming to the ephone-dn. This includes VoIP calls if voice
                              		  activity detection (VAD) is disabled. The typical operation is for the Cisco
                              		  CME ephone-dn to establish a call to a local router E&M voice port.

Connection via E&M is the recommended mechanism because it
                              		  requires minimal external components. The E&M port must be placed in 4-wire
                              		  operation, using E&M immediate signaling and with the auto-cut-through
                              		  option enabled. You directly connect a line-level audio feed (standard audio
                              		  jack) to pins 3 and 6 of an E&M RJ-45 connector. The E&M WAN interface
                              		  card (WIC) has a built-in audio transformer that provides appropriate
                              		  electrical isolation for the external audio source. (The audio connection on
                              		  the E&M port does not require loop current.) The signal immediate and auto-cut-through commands disable E&M
                              		  signaling on this voice port. A G.711 audio packet stream is generated by the
                              		  digital signal processor (DSP) on the E&M port.

If you are using an FXO voice port for live-feed audio stream instead
                              		  of an E&M port, connect the source to the FXO voice port. This connection
                              		  requires an external adapter to supply normal telephone company (telco) battery
                              		  voltage with the correct polarity to the tip-and-ring leads of the FXO port.
                              		  The adapter must also provide transformer-based isolation between the external
                              		  audio source and the tip-and-ring leads of the FXO port.

If the out-call keyword is used, an outbound call to
                              		  the live-feed source is attempted (or reattempted) every 30 seconds until the
                              		  call is connected to the ephone-dn (extension) for which the feed command was configured. Note that this
                              		  ephone-dn is not associated with a physical phone.

The related moh (ephone-dn) and multicast moh commands provide the ability to multicast an audio stream that
                              		  is also being used as the source for Cisco CME system music on hold (MOH).

## Examples

The following example sets up a call to extension 7777 for a live
                              		  audio stream and sends it via multicast:

```
Router(config)# ephone-dn 55 Router(config-ephone-dn)# feed ip 239.1.1.1 port 2000 route 10.10.23.3 out-call 7777
```

### Related Commands

Command

Description

auto-cut-through

Enables call completion when an M-lead response is not
                                          						provided.

ip source-address

Identifies the IP address and port through which IP phones
                                          						communicate with a Cisco CME router.

moh (ephone-dn)

Enables music on hold from a live feed and multicast of the
                                          						MOH audio stream.

moh (telephony-service)

Enables music on hold from an audio file.

multicast moh

Enables multicast of a music-on-hold audio stream.

signal

Specifies the type of signaling for a voice port.

## file text (voice register global)

To generate ASCII text files of the configuration profiles for SIP
                              		  phones, use the file text command in voice register global
                              		  configuration mode. To return to the default, use the no form of this command.

file text

no file text

### Syntax Description

This command has no arguments or keywords.

### Command Default

System directly generates only binary files for configuration
                              		  profiles.

### Command Modes

Voice register global configuration (config-register-global)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4

This command was introduced.

### Usage Guidelines

Use this command to generate an ASCII text fils of the configuration
                              		  profile for Cisco Unified IP Phone 7905s and 7905Gs, Cisco Unified IP Phone
                              		  7912s and 7912Gs, Cisco ATA-186s, or Cisco ATA-188s.

## Examples

The following example shows how to generate an ASCII text file
                              		  version of the configuration profiles for Cisco Unified IP Phone 7905s and
                              		  7905Gs, Cisco Unified IP Phone 7912s and 7912Gs, Cisco ATA-186s, or Cisco
                              		  ATA-188s:

```
Router(config)# voice register global Router(config-register-global)# mode cme Router(config-register-global)# file text Router(config-register-global)# create profile
```

### Related Commands

Command

Description

create profile (voice register global)

Generates the configuration profiles required for SIP
                                          						phone.

show voice register profile

Displays the contents of configuration files that are in
                                          						ASCII text format.

## filename

To specify a custom XML file that contains the dial patterns to use
                              		  for a SIP dial plan, use the filename command in voice register dialplan
                              		  configuration mode. To remove the file, use the no form of this command.

filename filename

no filename

### Syntax Description

filename

Name of the XML file in flash memory.

### Command Default

A custom file is not used for the dial plan.

### Command Modes

Voice register dialplan configuration (config-register-dialplan)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(11)XJ

Cisco Unified CME 4.1

This command was introduced.

12.4(15)T

Cisco Unified CME 4.1

This command was integrated into Cisco IOS Release
                                          						12.4(15)T.

### Usage Guidelines

This command selects a custom XML file containing dial patterns for
                              		  the SIP dial plan. The file specified with this command must be loaded into
                              		  flash memory. You must use the type command to specify the type of phone for
                              		  which the dial plan is being defined before you can use this command. After you
                              		  define a dial plan, assign it to a SIP phone by using the dialplan command.

The pattern command and filename command are mutually exclusive. You
                              		  can use either the pattern command to define dial patterns
                              		  manually, or the filename command to select a custom dial
                              		  pattern file that is loaded in system flash.

If the custom XML file contains any errors, the dial plan might not
                              		  work properly on the phone.

To remove a dial plan that is created using a custom XML file, use
                              		  the reset command after removing the dial plan
                              		  from the phone and creating a new configuration profile. Removing a dial plan
                              		  that uses a dial pattern XML file does not take effect if you restart the phone
                              		  with the restart command.

## Examples

The following example shows that a custom file named sample.xml is
                              		  specified for dial plan 2.

```
Router(config)# voice register dialplan 2 Router(config-register-dialplan)# type 7940-7960-others Router(config-register-dialplan)# filename sample.xml
```

### Related Commands

Command

Description

dialplan

Assigns a dial plan to a SIP phone.

pattern

Defines a dial pattern for a SIP dial plan.

show voice register dialplan

Displays all configuration information for a specific SIP
                                          						dial plan.

type (voice register dialplan)

Defines a phone type for a SIP dial plan.

## final

To define the last extension (ephone-dn) in an ephone hunt group, use
                              		  the final command in ephone-hunt configuration
                              		  mode. To remove this number from the hunt group, use the no form of this command.

final number

no final

### Syntax Description

number

Extension or phone number. Can be an ephone-dn primary or
                                          						secondary number, voice-mail number, pilot number of another hunt group, or FXS
                                          						caller-ID number.

### Command Default

No final number is defined.

### Command Modes

Ephone-hunt configuration (config-ephone-hunt)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco CME 3.0

This command was introduced.

12.3(4)T

Cisco CME 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

This command defines the last extension in a hunt group and the
                              		  destination of incoming calls to a hunt-group pilot number that are unanswered
                              		  after being routed through the directory numbers in the hunt group list.

To avoid an infinite loop, use the max-redirect command.

## Examples

The following example defines ephone-dn 6000 as the last number of
                              		  hunt group number 1:

```
Router(config)# ephone-hunt 1 sequential Router(config-ephone-hunt)# final 6000
```

### Related Commands

Command

Description

fwd-final

Specifies the final destination of an unanswered call that
                                          						has been transferred into a hunt group.

hops

Defines the number of times that a call is redirected to
                                          						the next ephone-dn in a peer ephone-hunt-group list before proceeding to the
                                          						final ephone-dn.

list

Defines the ephone-dns that participate in an ephone hunt
                                          						group.

max-redirect

Changes the number of allowable redirects in a Cisco
                                          						Unified CME system.

no-reg (ephone-hunt)

Specifies that the pilot number of an ephone hunt group
                                          						should not register with the H.323 gatekeeper.

pilot

Defines the ephone-dn that is dialed to reach an ephone
                                          						hunt group.

preference (ephone-hunt)

Sets preference order for the ephone-dn associated with an
                                          						ephone-hunt-group pilot number.

timeout (ephone-hunt)

Sets the number of seconds after which a call that is not
                                          						answered is redirected to the next number in the ephone-hunt-group list.

## final (voice hunt-group)

To define the last extension in a voice hunt group, use the final command in voice hunt-group
                              		  configuration mode. To remove this number from the hunt group, use the no form of this command.

final number

no final

### Syntax Description

number

Telephone or extension number. Can be an E.164 number,
                                          						voice-mail number, pilot number of another hunt group, or FXS caller-ID number.

### Command Default

No final number is defined in the voice hunt group.

### Command Modes

Voice hunt-group configuration (config-voice-hunt-group)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4

This command was introduced.

### Usage Guidelines

This command defines the last extension in a hunt group and the
                              		  destination of incoming calls to a hunt-group pilot number that are unanswered
                              		  after being routed through the directory numbers in the hunt group list.

To avoid an infinite loop, if a final number in one hunt group is
                              		  configured as a pilot number of another hunt group, the pilot number of the
                              		  first hunt group cannot be configured as a final number in any hunt group.

## Examples

The following example shows how to define extension 6000 as the last
                              		  number of hunt group 1:

```
Router(config)# voice hunt-group 1 sequential Router(config-voice-hunt-group)# final 6000
```

### Related Commands

Command

Description

hops (voice hunt-group)

Defines the number of times that a call is redirected to
                                          						the next number in a peer hunt-group list before proceeding to the final
                                          						number.

list (voice hunt-group)

Defines the numbers that participate in a voice hunt group.

max-redirect (voice register global)

Changes the current number of allowable redirects in a
                                          						Cisco CME system.

timeout (voice hunt-group)

Sets the number of seconds after which a call that is not
                                          						answered is redirected to the next number in the hunt-group list.

## forward local-calls

To allow internal (local) calls to be forwarded, use the forward local-calls command in ephone-dn or ephone-hunt
                              		  configuration mode. To prevent internal calls from being forwarded, use the no form of this command.

forward local-calls

no forward local-calls

### Syntax Description

This command has no arguments or keywords.

### Command Default

Internal calls are forwarded as specified in the ephone-dn or
                              		  ephone-hunt configuration of the called party.

### Command Modes

Ephone-dn configuration (config-ephone-dn) Ephone-hunt configuration (config-ephone-hunt)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)XC

Cisco Unified CME 4.0

This command was introduced.

## Command History

12.4(9)T

Cisco Unified CME 4.0

This command was integrated into Cisco IOS Release
                                          						12.4(9)T.

### Usage Guidelines

Internal, or local, calls are defined as those calls that originate
                              		  from other ephone-dns in the same Cisco Unified CME system.

When the no forward local-calls command is used in ephone-dn
                              		  configuration mode, internal calls to that ephone-dn are not forwarded if the
                              		  ephone-dn is busy or does not answer. If the ephone-dn is busy, the caller
                              		  hears a busy signal.If the ephone-dn does not answer, the caller hears a
                              		  ringback signal. The call is not forwarded even if call forwarding is enabled
                              		  for the ephone-dn.

When the no forward local-calls command is used in ephone-hunt
                              		  configuration mode, internal calls to a hunt-group pilot number are sent only
                              		  to the first member of the group. If the first group member is busy, the caller
                              		  hears a busy signal. If the first group member does not answer, the caller
                              		  hears a ringback signal. The call is not forwarded to subsequent hunt group
                              		  members.

## Examples

In the following example, extension 2222 dials the pilot number 3000
                              		  and is forwarded to extension 3011. If 3011 is busy, the caller hears a busy
                              		  tone. If 3011 does not answer, the caller hears ringback. The call is not
                              		  forwarded, even after the timeout expires.

```
ephone-hunt 17 sequential
 pilot 3000
 list 3011, 3021, 3031
 timeout 10
 final 7600
 no forward local-calls
```

In the following example, extension 2222 calls extension 3675 and
                              		  hears ringback or a busy signal. If an external caller reaches extension 3675
                              		  and there is no answer, the call is forwarded to extension 4000.

```
ephone-dn 25
 number 3675
 no forward local-calls
 call-forward noan 4000 timeout 30
```

## forward local-calls (voice hunt-group)

To allow local calls to be forwarded, use the forward local-calls command in voice hunt-group
                              		  configuration mode. To prevent local calls from being forwarded, use the no form of this command.

forward local-calls to-final

no forward local-calls to-final

### Syntax Description

to-final

Prevents local calls from being forwarded to the final
                                          						destination number.

### Command Default

Local calls are forwarded as specified in the voice hunt-group
                              		  configuration of the called party.

### Command Modes

Voice hunt-group configuration (config-voice-hunt-group)

## Command History

Release

Modification

15.3(2)T

This command was introduced.

### Usage Guidelines

Local or internal calls are calls originating from a Cisco Unified
                              		  SIP or Cisco Unified SCCP IP phone in the same Cisco Unified CME system.

Before Cisco Unified CME 9.5, the no forward local-calls command was configured in ephone-hunt
                              		  group to prevent a local call from being forwarded to the next agent.

In Cisco Unified CME 9.5, local calls are prevented from being
                              		  forwarded to the final destination using the no forward local-calls to-final command in parallel or sequential voice hunt-group
                              		  configuration mode.

When the no forward local-calls to-final command is configured in sequential voice hunt-group
                              		  configuration mode, local calls to the hunt-group pilot number are sent
                              		  sequentially only to the list of members of the group using the rotary-hunt
                              		  technique. In case all the group members of the voice hunt group are busy, the
                              		  caller hears a busy tone. If any of the group members are available but do not
                              		  answer, the caller hears a ringback tone and is eventually disconnected after
                              		  the specified timeout. The call is not forwarded to the final destination
                              		  number.

When the no forward local-calls to-final command is configured in parallel voice hunt-group
                              		  configuration mode, local calls to the hunt-group pilot number are sent
                              		  parallely to the list of members of the group using the blast technique. In
                              		  case all the group members of the voice hunt group are busy, the caller hears a
                              		  busy tone. If any of the group members are available but do not answer, the
                              		  caller hears a ringback tone and is eventually disconnected after the specified
                              		  timeout.The call is not forwarded to the final destination number.

## Examples

The following example shows how to prevent the forwarding of local
                              		  calls to the final destination in parallel voice hunt group 1:

```
Router# configure terminal
Router(config)# voice hunt-group 1 parallel
Router(config-voice-hunt-group)# no forward local-calls to-final
```

### Related Commands

Command

Description

voice hunt-group

Enters voice hunt-group configuration mode to create a hunt
                                          						group for phones in a Cisco Unified CME system.

## forwarding local (voice register global)

To use the forwarding-party number and name (the local number and
                              		  name) in calls forwarded using local hairpin call routing on a SIP phone, use
                              		  the forwarding local command in voice register global
                              		  configuration mode. To return to the default, use the no form of this command.

forwarding local

no forwarding local

### Syntax Description

This command has no arguments or keywords.

### Command Default

Calling-party name and number used.

### Command Modes

Voice register global configuration (config-register-global)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)T

Cisco CME 3.4

This command was introduced.

### Usage Guidelines

This command replaces a calling-party number and name with the local
                              		  forwarding-party number and name in hairpinned forwarded calls.

## Examples

The following example shows how to enable local forwarding:

```
Router(config)# voice register global Router(config-register-global)# forwarding local
```

### Related Commands

Command

Description

call-forward b2bua all (voice register dn and voice register pool)

Enables call forwarding for a SIP B2BUA so that all
                                          						incoming calls are forwarded to another extension.

## from-ring

To specify that on-hook time stamps for ephone hunt group agents
                              		  should be updated when calls ring as well as when calls are answered in a
                              		  longest-idle ephone hunt group, use the from-ring command in ephone-hunt
                              		  configuration mode. To return to the default, use the no form of this command.

from-ring

no from-ring

### Syntax Description

This command has no keywords or arguments.

### Command Default

On-hook time stamps are updated only when calls are answered by
                              		  agents.

### Command Modes

Ephone-hunt configuration

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)XC

Cisco Unified CME 4.0

This command was introduced.

12.4(9)T

Cisco Unified CME 4.0

This command was integrated into Cisco IOS Release
                                          						12.4(9)T.

### Usage Guidelines

This command is used only with longest-idle ephone hunt groups. In a
                              		  longest-idle hunt group, the algorithm for choosing the the next agent to
                              		  receive a call is based on a comparison of on-hook time stamps. The agent with
                              		  the smallest on-hook time stamp value is chosen when the next call comes to the
                              		  hunt group.

This command can be used to specify that on-hook time stamps should
                              		  be updated when calls ring agents as well as when calls are answered by agents.

The show ephone-hunt command displays on-hook time stamps.

## Examples

The following example defines longest-idle ephone hunt group 1 with a
                              		  pilot number 7501, a final number 8000, and five numbers in the list. Because
                              		  the from-ring command is used, on-hook time
                              		  stamps will be recorded when calls ring agents as well as when calls are
                              		  answered. After a call is redirected three times (makes six hops), it is
                              		  redirected to the final number, 8000.

```
ephone-hunt 1 longest-idle
 pilot 7501 
 list 7001, 7002, 7023, 7028, 7045
 final 8000 
 from-ring
 hops 3
 timeout 20 
telephony-service
 max-redirect 8
```

### Related Commands

Command

Description

show ephone-hunt

Displays configuration information, current status, and
                                          						statistics for ephone hunt groups.

## fwd-final

To specify the final destination of a call that has been transferred
                              		  into a hunt group and is unanswered, use the fwd-final command in ephone-hunt
                              		  configuration mode. To return to the default, use the no form of this command.

fwd-final { orig-phone | final }

no fwd-final { orig-phone | final }

### Syntax Description

orig-phone

Phone that originally answered a call before transferring
                                          						it to the pilot number of a hunt group.

final

Last extension in the hunt group as specified in the hunt
                                          						group configuration.

### Command Default

Calls are sent to the final number that is specified in the hunt
                              		  group configuration.

### Command Modes

Ephone-hunt configuration (config-ephone)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.4(4)XC

Cisco Unified CME 4.0

This command was introduced.

12.4(9)T

Cisco Unified CME 4.0

This command was integrated into Cisco IOS Release
                                          						12.4(9)T.

### Usage Guidelines

This command is used for routing only unanswered transferred calls.
                              		  Transferred calls are incoming calls to an ephone hunt group that were
                              		  previously answered by a Cisco Unified CME extension and transferred into the
                              		  hunt group.

The orig-phone keyword specifies that an
                              		  unanswered transferred call is routed back to the extension that originally
                              		  answered the call and transferred it to the hunt group.

The final keyword specifies that an unanswered
                              		  transferred call is routed to the last extension in the hunt group as defined
                              		  by using the final command.

## Examples

The following example sets up a peer hunt group with three ephone-dns
                              		  to answer calls. An unanswered transferred call will be routed to the ephone-dn
                              		  that transferred it to the ephone hunt group pilot number. A DID call that
                              		  dials the pilot number directly will be routed to extension 7600 if it is
                              		  unanswered by the hunt group.

```
ephone-hunt 17 peer
 pilot 3000
 list 3011, 3021, 3031
 hops 3
 final 7600
 fwd-final orig-phone
```

### Related Commands

Command

Description

final

Defines the last extension (ephone-dn) in an ephone hunt
                                          						group.

## fxo hook-flash

To enable display of a flash soft key on a Cisco IP Phones 7940 and
                              		  7940G or Cisco IP Phones 7960 and 7960G in a Cisco CallManager Express (Cisco
                              		  CME) system, use the fxo hook-flash command in telephony-service configuration mode. To disable
                              		  display of the flash soft key, use the no form of this command.

fxo hook-flash

no fxo hook-flash

### Syntax Description

This command has no arguments or keywords.

### Command Default

The flash soft key is disabled.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Cisco IOS Release

Cisco Product

Modification

12.2(15)ZJ

Cisco CME 3.0

This command was introduced.

12.3(4)T

Cisco CME 3.0

This command was integrated into Cisco IOS Release
                                          						12.3(4)T.

### Usage Guidelines

Certain public switched telephony network (PSTN) services, such as
                              		  three-way calling and call waiting, require hookflash intervention from the
                              		  phone user. A soft key labeled flash provides this functionality for the Cisco
                              		  IP Phones 7940 and 7940G and the Cisco IP Phones 7960 and 7960G users on
                              		  foreign exchange office (FXO) lines attached to the Cisco CME system. The flash
                              		  soft key is enabled using the fxo hook-flash command.

Once a flash soft key has been enabled on an IP phone, it is
                              		  available to provide hookflash functionality during all calls except local
                              		  IP-phone-to-IP-phone calls. Note that hookflash-controlled services can be
                              		  activated only if they are supported by the PSTN connection that is involved in
                              		  the call. The availability of the flash soft key does not guarantee that
                              		  hookflash-based services are actually accessible to the phone user.

The flash soft key display is automatically disabled for local
                              		  IP-phone-to-IP-phone calls.

This command must be followed by a quick reboot of the phones using
                              		  the restart all command.

## Examples

The following example enables the flash soft key on the Cisco IP
                              		  Phones 7940 and 7940G and the Cisco IP Phones 7960 and 7960G:

```
Router(config)# telephony-service Router(config-telephony)# fxo hook-flash
```

### Related Commands

Command

Description

restart (ephone)

Performs a fast reboot of a single phone associated with a
                                          						Cisco CME router.

restart (telephony-service)

Performs a fast reboot of one or all phones associated with
                                          						a Cisco CME router.

| standard | All predefined standard FACs are enabled. |
|---|---|
| custom | User-defined FAC for selecting a particular feature or
                                          						function from the predefined set of features is enabled. |
| alias | Alternative FAC for dialing an existing FAC or existing FAC
                                          						plus extra digits without removing the existing FAC is enabled. |
| alias-tag | Unique number that identifies this alias during
                                          						configuration tasks. Range: 0 to 9. |
| custom-fac | User-defined code to dial using the keypad on an IP or
                                          						analog phone. Code can be up to 256 characters and can contain numbers 0 to 9
                                          						and * and #. Note ## is not supported for FACs on SIP phones. | Note | ## is not supported for FACs on SIP phones. |
| Note | ## is not supported for FACs on SIP phones. |
| to | Maps custom FAC being configured to specified target. |
| existing-fac | Already configured custom FAC that is automatically dialed
                                          						when the phone user dials the custom FAC being configured. |
| extra-digits | (Optional) Additional digits that are automatically dialed
                                          						when the phone user dials the custom FAC being configured. Valid entries are: target extension —Telephone or extension
                                             						  number in Cisco Unified CME to which the incoming calls are forwarded. Used
                                             						  with the Call Forward feature. group number —Pickup group number, for a
                                             						  group other than the local group number. Used with the Pickup Group feature. pickup extension —Telephone or extension
                                             						  number in Cisco Unified CME to be picked up when ringing. To be used with the
                                             						  Pickup Direct feature. park-slot number —Number on which calls are to be
                                             						  temporarily parked. Use with the Call Park feature. Target park slot must be
                                             						  already configured in Cisco Unified CME. pilot number —Telephone or extension number
                                             						  configured as a the pilot number for an ephone hunt group to be joined. Hunt
                                             						  group to be joined must allow dynamic membership. |
| feature | Predefined alphabetic string that identifies a particular
                                          						feature or function. Valid entries are: callfwd all —Directs system to forward all
                                             						  incoming calls for this telephone or extension number. callfwd cancel —Directs system to cancel the
                                             						  call-forward-all selection. ccw —Disables the Call Waiting
                                             						  feature. dnd —Enables Do Not Disturb
                                             						  (DND) feature on SCCP phones. Not supported for SIP phones. dpark-retrieval —Enables
                                             						  Directed Call Park Retrieval feature. Applies to both SIP and SCCP phones. ephone-hunt cancel —Leaves an ephone hunt group
                                             						  that is configured to allow dynamic membership. ephone-hunt hlog —Activates or deactivates hunt
                                             						  group logout functionality, changing the status of the an ephone-dn for a hunt
                                             						  group agent from ready to not-ready or from not-ready to ready. ephone-hunt hlog-phone —Activates or deactivates
                                             						  phone-level hunt group logout functionality, changing the status of all the
                                             						  extensions on a hunt group member phone from ready to not-ready or from
                                             						  not-ready to ready. ephone-hunt join —Joins an ephone hunt group that
                                             						  is configured to allow dynamic membership. If multiple hunt groups have been
                                             						  created that allow dynamic membership, the hunt group to be joined is
                                             						  identified by its pilot number. park —Enables Call Park feature. pickup direct —Picks up a ringing call at any
                                             						  extension. Applies to both SIP and SCCP phones. pickup group —Picks up a ringing call in a
                                             						  different pickup group than yours. Applies to both SIP and SCCP phones. pickup local —Picks up a ringing call in your
                                             						  pickup group. Applies to both SIP and SCCP phones. redial —Redials the last number
                                             						  called. trnsfvm —Activates the Transfer
                                             						  to Voice-Mail feature. voicemail —Dials the voice-mail
                                             						  number. |

| Note | ## is not supported for FACs on SIP phones. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |
| 12.4(15)XZ | Cisco Unified CME 4.3 | Standard FAC and trnsfvm keyword for a custom FAC
                                          						were added for transfer to voice mail. |
| 12.4(20)T | Cisco Unified CME 7.0 | This command was integrated into Cisco IOS Release
                                          						12.4(20)T. |
| 12.4(22)YB | Cisco Unified CME 7.1 | The dpark-retrieval keyword was added
                                          						and support for SIP phones was added for the park direct , park group , and park local keywords. |
| 12.4(24)T | Cisco Unified CME 7.1 | This command was integrated into Cisco IOS Release
                                          						12.4(24)T. |
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was modified. The ccw keyword was added for a custom
                                          						FAC. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| show telephony-service fac | Displays list of FACs that are configured on Cisco Unified
                                          						CME. |

| lpcor-group | Name of the LPCOR resource group. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(3)T | Cisco Unified CME 8.5 | This command was introduced. |

| Command | Description |
|---|---|
| show voice register global | Displays all global configuration parameters associated
                                          						with SIP phones. |

| seconds | Failure-to-connect time, in seconds. Range: 0 to 600
                                          						seconds. Default: 30 seconds. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.1(3)T | Cisco Unified CME 8.5 | This command was introduced. |

| Command | Description |
|---|---|
| vpn-profile | Defines a VPN-profile. |

| dial-tag | Unique
                                          						sequence number that ranges from 1 to 100 and is used to identify a particular
                                          						personal speed-dial number during configuration tasks. |
|---|---|
| number | Telephone number or extension to be dialed. |
| name name-string | Label
                                          						to appear in the Personal Speed Dial menu, containing a string of up to 24
                                          						alphanumeric characters. Personal speed dial is handled through an XML request,
                                          						so characters that have special meaning to HTTP, such as ampersand (&),
                                          						percent sign (%), semicolon (;), angle brackets (< >), and vertical bars
                                          						(\|\|), are not allowed. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco
                                          						CME 3.0 | This
                                          						command was introduced. |
| 12.3(4)T | Cisco
                                          						CME 3.0 | This
                                          						command was integrated into Cisco IOS Release 12.3(4)T. |
| 12.4(4)XC | Cisco
                                          						Unified CME 4.0 | This
                                          						command was made available in ephone-template configuration mode. |
| 12.4(9)T | Cisco
                                          						Unified CME 4.0 | This
                                          						command in ephone-template configuration mode was integrated into Cisco IOS
                                          						Release 12.4(9)T. |
| 15.4(3)M | Cisco
                                          						Unified CME 10.5 | This
                                          						command was modified to increase the range from 24 to 100. |

| Command | Description |
|---|---|
| ephone-template (ephone) | Applies a template to the ephone being configured. |
| show telephony-service ephone-template | Displays the contents of ephone templates. |

| index | Index number of a specific feature type. One from the total
                                          						24 feature IDs. |
|---|---|
| feature identifier | One of the following feature or stimulus IDs: Redial, Hold,
                                          						Trnsfer, Cfwdall, Privacy, MeetMe, Confrn, Park, Pickup. Gpickup, Mobility,
                                          						Dnd, ConfList, RmLstC, CallBack, NewCall, EndCall, HLog, NiteSrv, Acct, Flash,
                                          						Login, TrnsfVM, LiveRcd. |
| label | Defines non-default text label for PLK button. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |
| 15.1(3)T | Cisco Unified CME 8.5 | This command was modified to configure feature button on a
                                          						phone’s line key. Feature button index number and feature ID keywords were
                                          						added. |
| 15.2(4)M | Cisco Unified CME 9.1 | This command was modified to add label < label > for the PLK button. |

| Command | Description |
|---|---|
| privacy-button | Enables the privacy feature button on an IP phone. |
| show telephony-service ephone | Displays the information about ephone configuration in a
                                          						Cisco CallManager Express (Cisco CME) system. |
| show telephony-service ephone-dn-template | Displays the information about ephone-template’s
                                          						configurations. |

| index | Index
                                          						number of a specific feature type. One from the total 24 feature IDs. |
|---|---|
| feature
                                          						identifier | One of
                                          						the following feature or stimulus IDs: Redial, Hold, Trnsfer, Cfwdall, Privacy,
                                          						MeetMe, Confrn, Park, Pickup, Gpickup, Mobility, NewCall, EndCall, Dnd,
                                          						ConfList, NewCall, HLog, Trnsfer. |

| Cisco
                                          						IOS Release | Cisco
                                          						Product | Modification |
|---|---|---|
| 15.1(3)T | Cisco
                                          						Unified CME 8.5 | This
                                          						command was introduced. |

| Command | Description |
|---|---|
| show voice register pool | Displays all configuration information associated with a particular voice
                                          						register pool. |

| CFwdAll | Call forward all calls. |
|---|---|
| Confrn | Conference. |
| GpickUp | Group call pickup. |
| Park | Call park. |
| PickUp | Directed or local call pickup. This includes pickup
                                          						last-parked call and pickup from another extension or park slot. |
| Trnsfer | Call transfer. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| Command | Description |
|---|---|
| ephone-template (ephone) | Applies a template to the ephone being configured. |
| show telephony-service ephone-template | Displays the contents of ephone templates. |

| ip ip-address | Indicates that a particular audio stream is to be used as a
                                          						multicast source and specifies the destination IP address for multicast. |
|---|---|
| port port-number | Specifies the media port for multicast. Range is from 2000
                                          						to 65535. Port 2000 is recommended because this port is already used for normal
                                          						Real-Time Transport Protocol (RTP) media transmissions between IP phones and
                                          						the Cisco CallManager Express (Cisco CME) router. |
| route ip-address | (Optional) Indicates the specific router interface on which
                                          						to transmit the IP multicast packets. The default is that the audio stream is
                                          						automatically output on the interface that corresponds to the address that was
                                          						configured with the ip source-address command. |
| out-call outcall-number | (Optional) Sets up a call to the outcall number in order to
                                          						connect to a live audio feed. If this keyword is not used, the live feed is
                                          						assumed to derive from an incoming call to the ephone-dn that is being
                                          						configured. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Note | IP phones do not support multicast at 224.x.x.x addresses. |
|---|---|

| Command | Description |
|---|---|
| auto-cut-through | Enables call completion when an M-lead response is not
                                          						provided. |
| ip source-address | Identifies the IP address and port through which IP phones
                                          						communicate with a Cisco CME router. |
| moh (ephone-dn) | Enables music on hold from a live feed and multicast of the
                                          						MOH audio stream. |
| moh (telephony-service) | Enables music on hold from an audio file. |
| multicast moh | Enables multicast of a music-on-hold audio stream. |
| signal | Specifies the type of signaling for a voice port. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

| Command | Description |
|---|---|
| create profile (voice register global) | Generates the configuration profiles required for SIP
                                          						phone. |
| show voice register profile | Displays the contents of configuration files that are in
                                          						ASCII text format. |

| filename | Name of the XML file in flash memory. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(11)XJ | Cisco Unified CME 4.1 | This command was introduced. |
| 12.4(15)T | Cisco Unified CME 4.1 | This command was integrated into Cisco IOS Release
                                          						12.4(15)T. |

| Note | This command is not supported for Cisco Unified IP Phone 7905 or
                                       		  7912. |
|---|---|

| Command | Description |
|---|---|
| dialplan | Assigns a dial plan to a SIP phone. |
| pattern | Defines a dial pattern for a SIP dial plan. |
| show voice register dialplan | Displays all configuration information for a specific SIP
                                          						dial plan. |
| type (voice register dialplan) | Defines a phone type for a SIP dial plan. |

| number | Extension or phone number. Can be an ephone-dn primary or
                                          						secondary number, voice-mail number, pilot number of another hunt group, or FXS
                                          						caller-ID number. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| fwd-final | Specifies the final destination of an unanswered call that
                                          						has been transferred into a hunt group. |
| hops | Defines the number of times that a call is redirected to
                                          						the next ephone-dn in a peer ephone-hunt-group list before proceeding to the
                                          						final ephone-dn. |
| list | Defines the ephone-dns that participate in an ephone hunt
                                          						group. |
| max-redirect | Changes the number of allowable redirects in a Cisco
                                          						Unified CME system. |
| no-reg (ephone-hunt) | Specifies that the pilot number of an ephone hunt group
                                          						should not register with the H.323 gatekeeper. |
| pilot | Defines the ephone-dn that is dialed to reach an ephone
                                          						hunt group. |
| preference (ephone-hunt) | Sets preference order for the ephone-dn associated with an
                                          						ephone-hunt-group pilot number. |
| timeout (ephone-hunt) | Sets the number of seconds after which a call that is not
                                          						answered is redirected to the next number in the ephone-hunt-group list. |

| number | Telephone or extension number. Can be an E.164 number,
                                          						voice-mail number, pilot number of another hunt group, or FXS caller-ID number. |
|---|---|

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

| Command | Description |
|---|---|
| hops (voice hunt-group) | Defines the number of times that a call is redirected to
                                          						the next number in a peer hunt-group list before proceeding to the final
                                          						number. |
| list (voice hunt-group) | Defines the numbers that participate in a voice hunt group. |
| max-redirect (voice register global) | Changes the current number of allowable redirects in a
                                          						Cisco CME system. |
| timeout (voice hunt-group) | Sets the number of seconds after which a call that is not
                                          						answered is redirected to the next number in the hunt-group list. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |

| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |
|---|---|---|

| to-final | Prevents local calls from being forwarded to the final
                                          						destination number. |
|---|---|

| Release | Modification |
|---|---|
| 15.3(2)T | This command was introduced. |

| Command | Description |
|---|---|
| voice hunt-group | Enters voice hunt-group configuration mode to create a hunt
                                          						group for phones in a Cisco Unified CME system. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)T | Cisco CME 3.4 | This command was introduced. |

| Command | Description |
|---|---|
| call-forward b2bua all (voice register dn and voice register pool) | Enables call forwarding for a SIP B2BUA so that all
                                          						incoming calls are forwarded to another extension. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| Command | Description |
|---|---|
| show ephone-hunt | Displays configuration information, current status, and
                                          						statistics for ephone hunt groups. |

| orig-phone | Phone that originally answered a call before transferring
                                          						it to the pilot number of a hunt group. |
|---|---|
| final | Last extension in the hunt group as specified in the hunt
                                          						group configuration. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.4(4)XC | Cisco Unified CME 4.0 | This command was introduced. |
| 12.4(9)T | Cisco Unified CME 4.0 | This command was integrated into Cisco IOS Release
                                          						12.4(9)T. |

| Command | Description |
|---|---|
| final | Defines the last extension (ephone-dn) in an ephone hunt
                                          						group. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 12.2(15)ZJ | Cisco CME 3.0 | This command was introduced. |
| 12.3(4)T | Cisco CME 3.0 | This command was integrated into Cisco IOS Release
                                          						12.3(4)T. |

| Command | Description |
|---|---|
| restart (ephone) | Performs a fast reboot of a single phone associated with a
                                          						Cisco CME router. |
| restart (telephony-service) | Performs a fast reboot of one or all phones associated with
                                          						a Cisco CME router. |