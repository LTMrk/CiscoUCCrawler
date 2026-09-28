---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmebarge-html-55ea5ea78a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmebarge.html
retrieved_at: 2026-08-21T07:24:33.744953+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Barge and Privacy

## Chapter: Barge and Privacy

# Barge and Privacy

## Information About Barge and Privacy

### Barge and
                           	 cBarge

The Barge feature
                              		enables phone users who share a directory number to join an active call on the
                              		shared line by pressing a softkey. When the initiator barges into a call, a
                              		conference is created between the barge initiator, the target party, and the
                              		other party connected in the call. Parties see the call information on their
                              		phones and, if the conference join tone is configured, hear a tone.

If a phone that is
                              		using the shared line has Privacy enabled, call information does not appear on
                              		the other phones that share the line and the call cannot be barged. Connected
                              		parties hear the barge tone (single beep) after the conference is set up. When
                              		a party leaves the conference, a barge leave tone is played to the remaining
                              		parties.

From Cisco Unified
                              		CME Release 11.7 onwards, cBarge feature is supported on Cisco 4000 Series
                              		Integrated Services Router.

From Cisco Unified
                              		CME Release 12.0 onwards, cBarge feature is supported with mixed shared line.

Cisco Unified
                                                				IP Phone 69xx series do not support cBarge with Unified CME.

Barge and Cbarge softkeys on SIP Phones are supported only on
                                                				shared lines.

#### Barge (SIP)

Barge uses the built-in conference bridge on the target phone (the phone
                                 		that is being barged) which limits the number of users allowed to barge. A
                                 		barge conference supports up to three parties. If more users want to join a
                                 		call on a SIP shared line, cBarge must be used. The SIP phone requires the
                                 		built-in conference bridge to use Barge. Barge is supported for SIP shared-line
                                 		directory numbers only.

If a phone user barges into a barge conference, the conference is
                                             		  converted to a cBarge conference.

#### cBarge (SCCP and
                              	 SIP)

The cBarge feature uses a shared conference resource which allows more than one person to barge into the call. A cBarge conference
                                 supports the maximum number of parties provisioned on the centralized conference resource. The centralized conference resource
                                 must be provisioned to use cBarge. cBarge is supported on SCCP shared octo-line directory numbers and SIP shared-line directory
                                 numbers.

When any party
                                 		releases from the call, the call remains a conference call if at least three
                                 		participants remain on the line. If only two parties remain in the conference,
                                 		they are reconnected as a point-to-point call, which releases the conference
                                 		bridge resources. When the target party parks the call or joins the call with
                                 		another call, the barge initiator and the other parties remain connected.

Table 1 describes the differences between Barge using a built-in conference bridge and
                                 		cBarge using a shared conference bridge.

Action

Barge—Built-In Conference Bridge at Target Device

cBarge—Shared Conference Bridge

Media break
                                             				  occurs during barge setup

No

Yes

User
                                             				  receives a Barge tone, if configured

Yes

Yes

Displays
                                             				  name at barge initiator phone

To Barge

To Barge

Displays
                                             				  name at target phone

To/From
                                             				  Other

To Barge

Displays
                                             				  name at other phones

To/From
                                             				  Target

To Barge

Allows
                                             				  second barge setup to an already barged call

Yes

Yes

Maximum
                                             				  number of parties

3

Maximum
                                             				  allowed by the shared conference resource.

Initiator
                                             				  releases call

No media
                                             				  interruption occurs for the two original parties.

Media break
                                             				  occurs to release the shared conference bridge when only two parties remain and
                                             				  to reconnect the remaining parties as a point-to-point call.

Target
                                             				  releases call

Media break
                                             				  occurs to reconnect initiator with the other party as a point-to-point call.

Media break
                                             				  occurs to release the shared conference bridge when only two parties remain and
                                             				  to reconnect the remaining parties as a point-to-point call.

Other party
                                             				  releases call

All three
                                             				  parties are released.

Media break
                                             				  occurs to release the shared conference bridge when only two parties remain and
                                             				  to reconnect the remaining parties as a point-to-point call.

Target puts
                                             				  call on hold and performs Transfer, Conference, or Call Park.

Initiator is
                                             				  released.

Initiator
                                             				  and the other party remain connected.

If no conference
                                 		bridge is available, either built-in at the target device for barge or shared
                                 		for cBarge, or the maximum number of participants is reached, Cisco Unified CME
                                 		rejects the barge request and an error message displays on the initiating
                                 		phone.

The barge and cBarge
                                 		soft keys display by default when a phone user presses the shared-line button
                                 		for an active remote-in-use call. The user selects either barge or cBarge to
                                 		join the shared-line call. When there are multiple active calls on the shared
                                 		line, the barge initiator can select which call to join by highlighting the
                                 		call.

You can customize
                                 		the soft key display with a soft key template. For configuration information,
                                 		see Configure the cBarge Soft Key on SCCP Phones or Enable Barge and cBarge Soft Keys on SIP Phones .

Restriction

cBarge operation
                                             		  on an existing ad-hoc or meet-me conference is not supported.

### Privacy and
                           	 Privacy on Hold

The privacy feature
                              		enables phone users to block other users who share a directory number from
                              		seeing call information, resuming a call, or barging into a call on the shared
                              		line. When a phone receives an incoming call on a shared line, the user can
                              		make the call private by pressing the Privacy feature button, which toggles
                              		between on and off to allow the user to alter the privacy setting on their
                              		phone. The privacy state is applied to all new calls and current calls owned by
                              		the phone user.

Privacy is supported
                              		on SCCP octo-line directory numbers and SIP shared-line directory numbers.

Privacy is enabled
                              		for all phones in the system by default. You can disable privacy globally and
                              		enable it only for specific phones, either individually or through an phone
                              		template. You can also enable the privacy button on specific phones. After a
                              		phone with the privacy button enabled registers with Cisco Unified CME, the
                              		line feature button on the phone gets labeled “Privacy,” a status icon
                              		displays, and if the button has a monitor lamp, it lights when privacy is
                              		active. For Extension Mobility phones, you can enable the privacy button in the
                              		user profile and logout profile.

The Privacy on Hold
                              		feature prevents other phone users from viewing call information or retrieving
                              		a call put on hold by another phone sharing the directory number. Privacy on
                              		Hold is disabled for all phones in the system by default. You can enable
                              		Privacy on Hold globally for all phones. To disable Privacy on Hold on
                              		individual phones, you must disable Privacy on those phones.

The Privacy feature
                              		applies to all shared lines on a phone. If a phone has multiple shared lines
                              		and Privacy is enabled, other phones cannot view or barge into calls on any of
                              		the shared lines.

For SCCP
                              		configuration information, see Enable Privacy and Privacy on Hold on SCCP Phones .

For SIP configuration information, see Enable Privacy and Privacy on Hold on SIP Phones .

## Configure Barge and Privacy

### Configure the
                           	 cBarge Soft Key on SCCP Phones

To enable a phone
                                 		  user to join a call on an octo-line directory number by pressing the cBarge
                                 		  soft key, perform the following steps. The cBarge soft key is enabled by
                                 		  default. This task is required only if you want to change the order of the soft
                                 		  key display during the remote-in-use call state.

Restriction

Supported
                                                   				  only on octo-line directory numbers.

Not
                                                   				  supported for meet-me conferences.

Not
                                                   				  supported if phone user is already connected to the same ad hoc conference on
                                                   				  the octo-line.

#### Before you begin

Cisco Unified
                                       				CME 7.0 or a later version.

Octo-line
                                       				directory number is configured. See Create Directory Numbers for SCCP Phones .

Privacy is
                                       				disabled on the phone. See Privacy and Privacy on Hold .

Ad hoc hardware conference resource is configured and ready to use. See Configure Hardware Conferencing .

Join and leave
                                       				tones for hardware conference can be configured as barge entrance and exit
                                       				tones. See Configure Join and Leave Tones .

### SUMMARY STEPS

- enable

- configure terminal

- ephone-template template-tag

- softkeys remote-in-use { [ CBarge ] [ Newcall ] }

- exit

- ephone phone-tag

- ephone-template template-tag

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router# enable
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

ephone-template template-tag

#### Example:

```
Router(config)# ephone-template 5
```

Enters
                                             				ephone-template configuration mode to create an ephone template.

template-tag —Unique identifier for the ephone
                                                   					 template that is being created. Range: 1 to 20.

Step 4

softkeys remote-in-use { [ CBarge ] [ Newcall ] }

#### Example:

```
Router(config-ephone-template)# softkeys remote-in-use CBarge Newcall
```

Modifies the
                                             				order and type of soft keys that display on an IP phone during the
                                             				remote-in-use call state.

Step 5

exit

#### Example:

```
Router(config-ephone-template)# exit
```

Exits
                                             				ephone-template configuration mode.

Step 6

ephone phone-tag

#### Example:

```
Router(config)# ephone 12
```

Enters ephone
                                             				configuration mode.

phone-tag —Unique number that identifies this
                                                   					 ephone during configuration tasks.

Step 7

ephone-template template-tag

#### Example:

```
Router(config-ephone)# ephone-template 5
```

Applies the
                                             				ephone template to the phone.

template-tag —Unique identifier of the ephone
                                                   					 template that you created in Step 3.

Step 8

end

#### Example:

```
Router(config-ephone)# end
```

Exits to
                                             				privileged EXEC mode.

#### Examples

The following
                                 		  example shows that ephone template 5 modifies the soft keys displayed for the
                                 		  remote-in-use call state and it is applied to ephone 12:

```
ephone-template  5
 softkeys remote-in-use  CBarge Newcall
 softkeys hold  Resume Newcall Join
 softkeys connected  TrnsfVM Park Acct ConfList Confrn Endcall Trnsfer Hold
 max-calls-per-button 3
 busy-trigger-per-button 2
!
!
ephone  12
 no phone-ui speeddial-fastdial
 ephone-template 5
 mac-address 000F.9054.31BD
 type 7960
 button  1:10 2:7
```

### Enable Barge and
                           	 cBarge Soft Keys on SIP Phones

A phone user can
                                 		  join a call on a shared line by pressing the Barge or cBarge soft keys. The
                                 		  Barge and cBarge soft keys are enabled by default on supported SIP phones.
                                 		  Perform the following steps only if you want to change the order or appearance
                                 		  of soft keys displayed during the remote-in-use call state.

Restriction

Supported
                                                   				  only on shared lines.

For Unified CME to support Barge functionality on Cisco IP Phone 7800 Series, you need to configure the CLI command service phone LineKeyBarge 2 under telephony-service configuration mode.

```
telephony-service
 service phone LineKeyBarge 2
```

The CLI command service phone LineKeyBarge 2 activates the Line keys on the Cisco IP Phone 7800 Series so that it displays the "remote-in-use" state softkeys correctly.
                                 When the command is not configured, the phones will not display the remote-in-use state softkeys. To update the phone configuration
                                 with the LineKeyBarge option, you need to execute the CLI command create profile under voice register global configuration mode.

If the remote-in-use state softkey configuration has both Barge and cBarge configured, then cBarge is taken as the preferential
                                             feature. The phones will ignore the Barge configuration.

#### Before you begin

Cisco Unified
                                       				CME 7.1 or a later version.

Shared
                                       				directory number is configured. See Create Directory Numbers for SIP Phones .

Ad hoc hardware conference resource is configured and ready to use. See Configure Hardware Conferencing .

Join and leave
                                       				tones for hardware conference can be configured as barge entrance and exit
                                       				tones. See Configure Join and Leave Tones in the Cisco Unified CME System Administrator Guide .

For Barge and
                                       				cBarge to work, privacy needs to be disabled under voice register global using
                                       				the command no
                                             					 privacy . For configuring Privacy, See Enable Privacy and Privacy on Hold on SIP Phones .

### SUMMARY STEPS

- enable

- configure terminal

- voice register template template-tag

- softkeys remote-in-use { [ Barge ] [ Newcall ] [ cBarge ] }

- exit

- voice register pool phone-tag

- template template-tag

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router# enable
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

voice register template template-tag

#### Example:

```
Router(config)# voice register template 5
```

Enters voice
                                             				register template configuration mode to create a voice register template.

template-tag —Unique identifier for the voice
                                                   					 register template that is being created. Range: 1 to 10.

Step 4

softkeys remote-in-use { [ Barge ] [ Newcall ] [ cBarge ] }

#### Example:

```
Router(config-register-temp)# softkeys remote-in-use cBarge Newcall
```

Modifies the
                                             				order and type of soft keys that display on a SIP phone during the
                                             				remote-in-use call state.

Step 5

exit

#### Example:

```
Router(config-register-temp)# exit
```

Exits voice
                                             				register template configuration mode.

Step 6

voice register pool phone-tag

#### Example:

```
Router(config)# voice register pool 12
```

Enters voice
                                             				register pool configuration mode.

phone-tag —Unique number that identifies this voice
                                                   					 register pool during configuration tasks.

Step 7

template template-tag

#### Example:

```
Router(config-register-pool)# template 5
```

Applies the
                                             				voice register template to the phone.

template-tag —Unique identifier of the template
                                                   					 that you created in Step 3

Step 8

end

#### Example:

```
Router(config-register-pool)# end
```

Returns to
                                             				privileged EXEC mode.

#### Examples

The following
                                 		  example shows that voice register template 5 modifies the soft keys displayed
                                 		  for the remote-in-use call state and it is applied to phone 120:

```
voice register template  5
 softkeys hold  Resume Newcall 
 softkeys connected  Trnsfer Park Hold
 softkeys remote-in-use  cBarge Barge 
! 
voice register pool  120 
 id mac 0030.94C2.A22A
 type 7962
 number 1 dn 20
 template 5
```

### Enable Privacy and
                           	 Privacy on Hold on SCCP Phones

To enable Privacy
                                 		  and Privacy on Hold on SCCP phones, perform the following steps.

If all phones
                                       				require access to privacy, leave the system-level privacy (telephony-service) command set to enabled (default value) and leave the
                                       				phone-level privacy (ephone) command set to the default (use system value).

If only
                                       				specific phones require access to privacy, disable privacy at the system-level
                                       				by using the no privacy command in telephony-service configuration mode and enable privacy at the
                                       				phone-level by using the privacy on command in ephone or ephone-template configuration mode.

Enable Privacy
                                       				on Hold at the system-level. To disable Privacy on Hold on individual phones,
                                       				you must disable Privacy on those phones.

Restriction

Privacy and
                                                   				  Privacy on Hold are supported for calls on shared octo-line directory numbers
                                                   				  only.

Privacy and
                                                   				  Privacy on Hold are not supported on the Cisco Unified IP Phone 7935, 7936,
                                                   				  7937, or 7985, Nokia E61, analog phones connected to the Cisco VG224 or
                                                   				  Cisco ATA, or any phone without a display.

#### Before you begin

Cisco Unified
                                       				CME 7.0 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- privacy

- privacy-on-hold

- exit

- ephone phone-tag

- privacy [ off | on ]

- privacy-button

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router# enable
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

privacy

#### Example:

```
Router(config-telephony)# privacy
```

(Optional)
                                             				Enables privacy at the system-level for all phones.

This
                                                   					 command is enabled by default.

To enable
                                                   					 privacy for individual phones only, disable privacy at the system-level with
                                                   					 the no privacy command and enable it for individual phones as shown in Step 8.

Step 5

privacy-on-hold

#### Example:

```
Router(config-telephony)# privacy-on-hold
```

(Optional)
                                             				Enables privacy on hold at the system-level for all phones.

Blocks
                                                   					 phone users on shared lines from viewing call information or retrieving calls
                                                   					 on hold. Default is disabled.

Step 6

exit

#### Example:

```
Router(config-telephony)# exit
```

Exits
                                             				telephony-service configuration mode.

Step 7

ephone phone-tag

#### Example:

```
Router(config)# ephone 10
```

Enters ephone
                                             				configuration mode.

phone-tag —Unique number that identifies this
                                                   					 ephone during configuration tasks.

Step 8

privacy [ off | on ]

#### Example:

```
Router(config-ephone)# privacy on
```

(Optional)
                                             				Modifies privacy support on the specific phone.

off —Disables privacy on the phone.

on —Enables
                                                   					 privacy on the phone.

System-level privacy setting is the default. Use this command
                                                   					 only if you want to modify the system-level setting in Step 4 for a specific
                                                   					 phone.

Using
                                                   					 the no form of
                                                   					 this command to reset to the system-level value.

This
                                                   					 command can also be configured in ephone-template configuration mode and
                                                   					 applied to one or more phones. The ephone configuration has priority over the
                                                   					 ephone-template configuration.

Step 9

privacy-button

#### Example:

```
Router(config-ephone)# privacy-button
```

Enables the
                                             				privacy feature button on the IP phone.

Enable
                                                   					 this command only on phones that share an octo-line directory number.

This
                                                   					 command can also be configured in ephone-template configuration mode and
                                                   					 applied to one or more phones. The ephone configuration has priority over the
                                                   					 ephone-template configuration.

Step 10

end

#### Example:

```
Router(config-ephone)# end
```

Exits to
                                             				privileged EXEC mode.

#### Example

The following
                                 		  example shows privacy disabled at the system-level and enabled on an individual
                                 		  phone. It also shows Privacy on Hold enabled at the system-level.

```
telephony-service
 no privacy
 privacy-on-hold
 max-ephones 100
 max-dn 240
 timeouts transfer-recall 60
 voicemail 8900
 max-conferences 8 gain -6
 transfer-system full-consult
 fac standard
!
!
ephone  10
 privacy on
 privacy-button
 max-calls-per-button 3
 busy-trigger-per-button 2
 mac-address 00E1.CB13.0395
 type 7960
 button  1:7 2:10
```

### Enable Privacy and
                           	 Privacy on Hold on SIP Phones

To enable Privacy
                                 		  and Privacy on Hold on SIP phones, perform the following steps.

To enable
                                       				Privacy on all phones, leave the system-level privacy (voice register global) command set to enabled (default value) and leave the
                                       				phone-level privacy (voice register pool) command set to the default (use system value).

To enable
                                       				Privacy on specific phones only, disable privacy at the system-level by using
                                       				the no privacy command in voice register global configuration mode and enable privacy at the
                                       				phone-level by using the privacy on command in voice register pool or voice register template configuration mode.

To enable
                                       				Privacy on Hold on all phones, enable it at the system-level with the privacy-on-hold command. To disable Privacy on
                                       				Hold on specific phones, disable Privacy on those phones using the privacy off command in voice register pool or voice register template configuration mode.
                                       				Privacy must be enabled to support Privacy on Hold.

Restriction

Privacy and
                                                   				  Privacy on Hold are supported for calls on shared-line directory numbers only.

Privacy and
                                                   				  Privacy on Hold are not supported on the Cisco Unified IP Phone 7935, 7936,
                                                   				  7937, or 7985, Nokia E6, analog phones connected to the Cisco VG224 or
                                                   				  Cisco ATA, or any phone without a display.

#### Before you begin

Cisco Unified
                                       				CME 7.1 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- privacy

- privacy-on-hold

- exit

- voice register pool phone-tag

- privacy { off | on }

- privacy-button

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router# enable
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

Enters
                                             				telephony-service configuration mode.

Step 4

privacy

#### Example:

```
Router(config-register-global)# privacy
```

(Optional)
                                             				Enables privacy at the system-level for all phones.

This
                                                   					 command is enabled by default.

To enable
                                                   					 privacy for individual phones only, disable privacy at the system-level with
                                                   					 the no privacy command and enable it for individual phones as shown in Step 8.

Step 5

privacy-on-hold

#### Example:

```
Router(config-register-global)# privacy-on-hold
```

(Optional)
                                             				Enables privacy on hold at the system-level for all phones.

Blocks
                                                   					 phone users on shared lines from viewing call information or retrieving calls
                                                   					 on hold. Default is disabled.

Step 6

exit

#### Example:

```
Router(config-register-global)# exit
```

Exits voice
                                             				register global configuration mode.

Step 7

voice register pool phone-tag

#### Example:

```
Router(config)# voice register pool 10
```

Enters voice
                                             				register pool configuration mode.

phone-tag —Unique number that identifies this phone
                                                   					 during configuration tasks.

Step 8

privacy { off | on }

#### Example:

```
Router(config-register-pool)# privacy on
```

(Optional)
                                             				Modifies phone-level privacy setting on this phone. The default value is the
                                             				system setting.

off —Sets
                                                   					 privacy state to off on the phone.

on —Sets
                                                   					 privacy state to on for the phone

Use this
                                                   					 command only if you want to modify the system-level setting in Step 4 for a
                                                   					 specific phone.

Using
                                                   					 the no form of
                                                   					 this command to reset to the system-level value.

This
                                                   					 command can also be configured in voice register template configuration mode
                                                   					 and applied to one or more phones. The phone configuration has priority over
                                                   					 the phone template configuration.

Step 9

privacy-button

#### Example:

```
Router(config-register-pool)# privacy-button
```

Enables the
                                             				privacy feature button on the IP phone.

Enable
                                                   					 this command only on phones with a shared-line directory number.

This
                                                   					 command can also be configured in voice register template configuration mode
                                                   					 and applied to one or more phones. The phone configuration has priority over
                                                   					 the phone template configuration.

Step 10

end

#### Example:

```
Router(config-register-pool)# end
```

Returns to
                                             				privileged EXEC mode.

#### Examples

The following
                                 		  example shows privacy disabled at the system-level and enabled on an individual
                                 		  phone. It also shows Privacy on Hold enabled at the system-level.

```
voice register global 
 mode cme
 privacy-on-hold
 no privacy
 max-dn 300 
 max-pool 150 
 voicemail 8900 
!
!
voice register pool  130 
 id mac 001A.A11B.500E 
 type 7941
 number 1 dn 30
 privacy ON
 privacy-button
```

## Feature
                        	 Information for Barge and Privacy

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature
                                          					 Name

Cisco Unified CME Version

Modification

Barge

12.0

Added cBarge support for mixed shared line.

11.7

Added support for cBarge on Cisco 4000 Series Integrated
                                          					 Services Router for Unified CME.

7.1

Added Barge and cBarge support for SIP shared-line directory
                                          					 numbers.

7.0/4.3

Added cBarge support for SCCP shared octo-line directory
                                          					 numbers.

Privacy

7.1

Added
                                          					 support for Privacy on SIP shared-line directory numbers.

7.0/4.3

Added
                                          					 support for Privacy on SCCP shared octo-line directory numbers.

| Note | Cisco Unified
                                                				IP Phone 69xx series do not support cBarge with Unified CME. Barge and Cbarge softkeys on SIP Phones are supported only on
                                                				shared lines. |
|---|---|

| Note | If a phone user barges into a barge conference, the conference is
                                             		  converted to a cBarge conference. |
|---|---|

| Action | Barge—Built-In Conference Bridge at Target Device | cBarge—Shared Conference Bridge |
|---|---|---|
| Media break
                                             				  occurs during barge setup | No | Yes |
| User
                                             				  receives a Barge tone, if configured | Yes | Yes |
| Displays
                                             				  name at barge initiator phone | To Barge | To Barge |
| Displays
                                             				  name at target phone | To/From
                                             				  Other | To Barge |
| Displays
                                             				  name at other phones | To/From
                                             				  Target | To Barge |
| Allows
                                             				  second barge setup to an already barged call | Yes | Yes |
| Maximum
                                             				  number of parties | 3 | Maximum
                                             				  allowed by the shared conference resource. |
| Initiator
                                             				  releases call | No media
                                             				  interruption occurs for the two original parties. | Media break
                                             				  occurs to release the shared conference bridge when only two parties remain and
                                             				  to reconnect the remaining parties as a point-to-point call. |
| Target
                                             				  releases call | Media break
                                             				  occurs to reconnect initiator with the other party as a point-to-point call. | Media break
                                             				  occurs to release the shared conference bridge when only two parties remain and
                                             				  to reconnect the remaining parties as a point-to-point call. |
| Other party
                                             				  releases call | All three
                                             				  parties are released. | Media break
                                             				  occurs to release the shared conference bridge when only two parties remain and
                                             				  to reconnect the remaining parties as a point-to-point call. |
| Target puts
                                             				  call on hold and performs Transfer, Conference, or Call Park. | Initiator is
                                             				  released. | Initiator
                                             				  and the other party remain connected. |

| Restriction | cBarge operation
                                             		  on an existing ad-hoc or meet-me conference is not supported. |
|---|---|

| Restriction | Supported
                                                   				  only on octo-line directory numbers. Not
                                                   				  supported for meet-me conferences. Not
                                                   				  supported if phone user is already connected to the same ad hoc conference on
                                                   				  the octo-line. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router# enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-template template-tag Example: Router(config)# ephone-template 5 | Enters
                                             				ephone-template configuration mode to create an ephone template. template-tag —Unique identifier for the ephone
                                                   					 template that is being created. Range: 1 to 20. |
| Step 4 | softkeys remote-in-use { [ CBarge ] [ Newcall ] } Example: Router(config-ephone-template)# softkeys remote-in-use CBarge Newcall | Modifies the
                                             				order and type of soft keys that display on an IP phone during the
                                             				remote-in-use call state. |
| Step 5 | exit Example: Router(config-ephone-template)# exit | Exits
                                             				ephone-template configuration mode. |
| Step 6 | ephone phone-tag Example: Router(config)# ephone 12 | Enters ephone
                                             				configuration mode. phone-tag —Unique number that identifies this
                                                   					 ephone during configuration tasks. |
| Step 7 | ephone-template template-tag Example: Router(config-ephone)# ephone-template 5 | Applies the
                                             				ephone template to the phone. template-tag —Unique identifier of the ephone
                                                   					 template that you created in Step 3. |
| Step 8 | end Example: Router(config-ephone)# end | Exits to
                                             				privileged EXEC mode. |

| Restriction | Supported
                                                   				  only on shared lines. |
|---|---|

| Note | If the remote-in-use state softkey configuration has both Barge and cBarge configured, then cBarge is taken as the preferential
                                             feature. The phones will ignore the Barge configuration. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router# enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register template template-tag Example: Router(config)# voice register template 5 | Enters voice
                                             				register template configuration mode to create a voice register template. template-tag —Unique identifier for the voice
                                                   					 register template that is being created. Range: 1 to 10. |
| Step 4 | softkeys remote-in-use { [ Barge ] [ Newcall ] [ cBarge ] } Example: Router(config-register-temp)# softkeys remote-in-use cBarge Newcall | Modifies the
                                             				order and type of soft keys that display on a SIP phone during the
                                             				remote-in-use call state. |
| Step 5 | exit Example: Router(config-register-temp)# exit | Exits voice
                                             				register template configuration mode. |
| Step 6 | voice register pool phone-tag Example: Router(config)# voice register pool 12 | Enters voice
                                             				register pool configuration mode. phone-tag —Unique number that identifies this voice
                                                   					 register pool during configuration tasks. |
| Step 7 | template template-tag Example: Router(config-register-pool)# template 5 | Applies the
                                             				voice register template to the phone. template-tag —Unique identifier of the template
                                                   					 that you created in Step 3 |
| Step 8 | end Example: Router(config-register-pool)# end | Returns to
                                             				privileged EXEC mode. |

| Restriction | Privacy and
                                                   				  Privacy on Hold are supported for calls on shared octo-line directory numbers
                                                   				  only. Privacy and
                                                   				  Privacy on Hold are not supported on the Cisco Unified IP Phone 7935, 7936,
                                                   				  7937, or 7985, Nokia E61, analog phones connected to the Cisco VG224 or
                                                   				  Cisco ATA, or any phone without a display. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router# enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 4 | privacy Example: Router(config-telephony)# privacy | (Optional)
                                             				Enables privacy at the system-level for all phones. This
                                                   					 command is enabled by default. To enable
                                                   					 privacy for individual phones only, disable privacy at the system-level with
                                                   					 the no privacy command and enable it for individual phones as shown in Step 8. |
| Step 5 | privacy-on-hold Example: Router(config-telephony)# privacy-on-hold | (Optional)
                                             				Enables privacy on hold at the system-level for all phones. Blocks
                                                   					 phone users on shared lines from viewing call information or retrieving calls
                                                   					 on hold. Default is disabled. |
| Step 6 | exit Example: Router(config-telephony)# exit | Exits
                                             				telephony-service configuration mode. |
| Step 7 | ephone phone-tag Example: Router(config)# ephone 10 | Enters ephone
                                             				configuration mode. phone-tag —Unique number that identifies this
                                                   					 ephone during configuration tasks. |
| Step 8 | privacy [ off \| on ] Example: Router(config-ephone)# privacy on | (Optional)
                                             				Modifies privacy support on the specific phone. off —Disables privacy on the phone. on —Enables
                                                   					 privacy on the phone. System-level privacy setting is the default. Use this command
                                                   					 only if you want to modify the system-level setting in Step 4 for a specific
                                                   					 phone. Using
                                                   					 the no form of
                                                   					 this command to reset to the system-level value. This
                                                   					 command can also be configured in ephone-template configuration mode and
                                                   					 applied to one or more phones. The ephone configuration has priority over the
                                                   					 ephone-template configuration. |
| Step 9 | privacy-button Example: Router(config-ephone)# privacy-button | Enables the
                                             				privacy feature button on the IP phone. Enable
                                                   					 this command only on phones that share an octo-line directory number. This
                                                   					 command can also be configured in ephone-template configuration mode and
                                                   					 applied to one or more phones. The ephone configuration has priority over the
                                                   					 ephone-template configuration. |
| Step 10 | end Example: Router(config-ephone)# end | Exits to
                                             				privileged EXEC mode. |

| Restriction | Privacy and
                                                   				  Privacy on Hold are supported for calls on shared-line directory numbers only. Privacy and
                                                   				  Privacy on Hold are not supported on the Cisco Unified IP Phone 7935, 7936,
                                                   				  7937, or 7985, Nokia E6, analog phones connected to the Cisco VG224 or
                                                   				  Cisco ATA, or any phone without a display. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router# enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register global Example: Router(config)# voice register global | Enters
                                             				telephony-service configuration mode. |
| Step 4 | privacy Example: Router(config-register-global)# privacy | (Optional)
                                             				Enables privacy at the system-level for all phones. This
                                                   					 command is enabled by default. To enable
                                                   					 privacy for individual phones only, disable privacy at the system-level with
                                                   					 the no privacy command and enable it for individual phones as shown in Step 8. |
| Step 5 | privacy-on-hold Example: Router(config-register-global)# privacy-on-hold | (Optional)
                                             				Enables privacy on hold at the system-level for all phones. Blocks
                                                   					 phone users on shared lines from viewing call information or retrieving calls
                                                   					 on hold. Default is disabled. |
| Step 6 | exit Example: Router(config-register-global)# exit | Exits voice
                                             				register global configuration mode. |
| Step 7 | voice register pool phone-tag Example: Router(config)# voice register pool 10 | Enters voice
                                             				register pool configuration mode. phone-tag —Unique number that identifies this phone
                                                   					 during configuration tasks. |
| Step 8 | privacy { off \| on } Example: Router(config-register-pool)# privacy on | (Optional)
                                             				Modifies phone-level privacy setting on this phone. The default value is the
                                             				system setting. off —Sets
                                                   					 privacy state to off on the phone. on —Sets
                                                   					 privacy state to on for the phone Use this
                                                   					 command only if you want to modify the system-level setting in Step 4 for a
                                                   					 specific phone. Using
                                                   					 the no form of
                                                   					 this command to reset to the system-level value. This
                                                   					 command can also be configured in voice register template configuration mode
                                                   					 and applied to one or more phones. The phone configuration has priority over
                                                   					 the phone template configuration. |
| Step 9 | privacy-button Example: Router(config-register-pool)# privacy-button | Enables the
                                             				privacy feature button on the IP phone. Enable
                                                   					 this command only on phones with a shared-line directory number. This
                                                   					 command can also be configured in voice register template configuration mode
                                                   					 and applied to one or more phones. The phone configuration has priority over
                                                   					 the phone template configuration. |
| Step 10 | end Example: Router(config-register-pool)# end | Returns to
                                             				privileged EXEC mode. |

| Feature
                                          					 Name | Cisco Unified CME Version | Modification |
|---|---|---|
| Barge | 12.0 | Added cBarge support for mixed shared line. |
| 11.7 | Added support for cBarge on Cisco 4000 Series Integrated
                                          					 Services Router for Unified CME. |
| 7.1 | Added Barge and cBarge support for SIP shared-line directory
                                          					 numbers. |
| 7.0/4.3 | Added cBarge support for SCCP shared octo-line directory
                                          					 numbers. |
| Privacy | 7.1 | Added
                                          					 support for Privacy on SIP shared-line directory numbers. |
| 7.0/4.3 | Added
                                          					 support for Privacy on SCCP shared octo-line directory numbers. |