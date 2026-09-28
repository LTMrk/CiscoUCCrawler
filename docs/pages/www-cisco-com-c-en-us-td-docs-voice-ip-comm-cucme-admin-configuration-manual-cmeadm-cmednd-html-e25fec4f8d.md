---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmednd-html-e25fec4f8d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmednd.html
retrieved_at: 2026-08-21T07:23:13.997915+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Do Not
	 Disturb

## Chapter: Do Not
	 Disturb

# Do Not
                     	 Disturb

## Information About Do Not Disturb

### Do Not Disturb on SCCP Phone

The Do Not Disturb (DND) feature allows phone users to disable audible
                              		ringing for incoming calls. When DND is enabled, incoming calls do not ring on
                              		the phone, however there is visual alerting and the call information displays,
                              		and a call can be answered if desired. When a local IP phone calls another
                              		local IP phone that is in the DND state, the message “Ring out DND” displays on
                              		the calling phone indicating that the target phone is in the DND state.

Phone users can toggle DND on and off by using the DND softkey in the
                              		idle or ringing call states. A SSCP phone user can toggle DND on or off in the
                              		ringing state only if DND in not already active on the phone. If DND is already
                              		active when a new call comes in, the SCCP phone user cannot change the DND
                              		state by pressing the DND softkey.

If an SSCP phone user toggles DND on during an incoming call, the DND
                              		state remains active for the current call only. If a SIP phone user toggles DND
                              		on during an incoming call, the DND state remains active during the current
                              		call and for all future calls until the user explicitly toggles DND off.

Pressing the DND softkey during an incoming call forwards the call to
                              		the call-forward no answer destination if Call Forward No Answer is enabled. If
                              		Call Forward is not enabled, pressing the DND softkey disables audible ringing
                              		and visual alerting, but the call information is visible on the phone display.

In Cisco CME 3.2.1 and later versions, DND can be blocked from phones
                              		with the feature-ring function. A feature ring is a triple-pulse ring, a type
                              		of ring cadence in addition to internal call and external call ring cadences.
                              		For example, an internal call in the United States rings for 2 seconds on and 4
                              		seconds off (single-pulse ring), and an external call rings for 0.4 seconds on,
                              		0.2 seconds off, 0.4 seconds on, and 0.2 seconds off (double-pulse ring).

The triple-pulse ring is used as an audio identifier for phone users.
                              		For example, each salesperson in a sales department could have an IP phone with
                              		a button sharing the same set of ephone-dns with the sales staff and another
                              		button for their private line for preferred customers. To help a salesperson
                              		identify an incoming call to his or her private line, the private line can be
                              		configured with the feature-ring function. You can disable the DND function on
                              		feature-ring lines. In the preceding example, salespeople could activate DND on
                              		their phones and still hear calls to their private lines.

### Do Not Disturb on
                           	 SIP Phone

In
                              		Cisco Unified CME 7.1 and later versions, the Do Not Disturb (DND) feature for
                              		SIP phones prevents incoming calls from audibly ringing a phone. When DND is
                              		enabled, the phone flashes an alert to visually indicate an incoming call
                              		instead of ringing and the call can be answered if desired. The message “Do Not
                              		Disturb is active” displays on the phone and calls are logged to the Missed
                              		Calls directory.

In versions earlier
                              		than Cisco Unified CME 7.1, the DND feature blocks incoming calls to a SIP
                              		phone with a busy tone. Cisco Unified CME rejects calls to all lines on the
                              		phone and plays a busy tone to the caller. Received calls are not logged to the
                              		Missed Calls directory on the phone.

DND applies to all
                              		lines on the phone. If DND and Call Forward All are both enabled on a phone,
                              		Call Forward All takes precedence on incoming calls.

You must enable DND
                              		for a SIP phone through Cisco Unified CME. The DND softkey displays by default
                              		on supported SIP phones in both the Ringing and idle states. You can remove or
                              		change the order of this softkey using a voice register template.

A phone user can
                              		toggle DND on and off at the phone by using the DND softkey. If a SIP phone
                              		user activates DND during an incoming call, the DND state remains active during
                              		the current call and for all future calls until the user explicitly toggles DND
                              		off.

If a phone user
                              		toggles DND on or off at the phone, Cisco Unified CME restores the DND state
                              		after the phone resets or restarts, if you save the running configuration
                              		before Cisco Unified CME reboots.

For configuration
                              		information, see Configure Do Not Disturb on SIP Phones .

Table 1 compares the DND configuration for SIP phones with different phone load
                              		versions:

Cisco
                                             				  Unified IP Phone 7911, 7941, 7961, 7970, or 7971 with 8.3 Phone Load

Cisco
                                             				  Unified IP Phone 7911, 7941, 7961, 7970, or 7971 with 8.2 Phone Load or
                                             				  Cisco Unified IP Phone 7940 or 7960

DND support

dnd command in voice register pool mode

dnd command in voice register pool mode

DND softkey
                                             				  display

softkey idle and softkey
                                                   						ringIn command in voice register template mode

dnd-control command in voice register template
                                             				  mode

Behavior
                                             				  when configured

Ringer is
                                             				  turned off for incoming calls. Visual alerting is provided.

Call is
                                             				  rejected and busy tone is played to the caller.

## Configure Do Not Disturb

### Blocking Do Not
                           	 Disturb on SCCP Phone

To block DND on
                                 		  phones that have buttons configured for feature ringing, perform the following
                                 		  steps. DND is enabled by using the DND softkey on Cisco Unified IP phones that
                                 		  support softkeys.

Restriction

Phone users
                                                   				  cannot enable DND for a shared line in a hunt group. The softkey displays in
                                                   				  the idle and ringing states but does not enable DND for shared lines in hunt
                                                   				  groups.

DND is not supported for Analog SCCP devices.

#### Before you begin

Cisco Unified
                                       				3.2.1 or a later version.

Phone line
                                       				must be configured for feature ring with the button f command.

Call-forwarding no-answer must be set for a phone to use DND to
                                       				forward calls. For configuration information, see Configure Call Transfer and Forwarding .
                                       				No other configuration is necessary for basic DND.

### SUMMARY STEPS

- enable

- configure terminal

- ephone phone-tag

- no dnd feature-ring

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

ephone phone-tag

#### Example:

```
Router(config)# ephone 10
```

Enters ephone
                                             				configuration mode.

phone-tag —Unique sequence number that identifies
                                                   					 the ephone to be configured.

Step 4

no dnd feature-ring

#### Example:

```
Router(config-ephone)# no dnd feature-ring
```

Enables
                                             				ringing on phone buttons configured for feature ring when the phone is in DND
                                             				mode.

Step 5

end

#### Example:

```
Router(config-ephone)# end
```

Returns to
                                             				privileged EXEC mode.

#### Example

In the following
                                 		  configuration example, when DND is activated on ephone 1 and ephone 2, button 1
                                 		  will ring, but button 2 will not.

```
ephone-dn 1
 number 1001

ephone-dn 2
 number 1002
 
ephone-dn 10
 number 1110 
 preference 0
 no huntstop

ephone-dn 11
 number 1111
 preference 1

ephone 1
 button 1f1
 button 2o10,11
 no dnd feature-ring 
 
ephone 2
 button 1f2 
 button 2o10,11
 no dnd feature-ring
```

### Verify Do Not Disturb on SCCP Phones

show ephone dnd

Use this command to display a list of SCCP phones that have DND
                                 		  enabled.

```
Router# show ephone dnd ephone-1 Mac:0007.0EA6.353A TCP socket:[1] activeLine:0 REGISTERED
mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0
IP:1.2.205.205 52486 Telecaster 7960  keepalive 2729 max_line 6 DnD
button 1: dn 11 number 60011 CH1 IDLE
```

### Configure Do Not
                           	 Disturb on SIP Phones

To enable the Do
                                 		  Not Disturb (DND) feature on a SIP phone, perform the following steps.

Restriction

In versions
                                                   				  earlier than Cisco Unified CME 7.1, you enable the DND softkey on SIP phones by
                                                   				  using the dnd-control command.

If you
                                                   				  enable DND on the phone and remove the DND softkey, the user cannot toggle DND
                                                   				  off at the phone.

Cisco Unified IP Phone 7911G, 7941G, 7941GE, 7961G, 7961GE,
                                                				7970G, and 7971GE

For SIP
                                                   				  phones using firmware 8.3 or a later version, the DND feature prevents calls
                                                   				  from ringing; it does not block calls or play a busy tone to the caller.

If DND is
                                                   				  disabled by a phone user, it is not enabled after the phone resets or restarts.
                                                   				  DND must be enabled both in Cisco Unified CME and by using the DND
                                                   				  softkey on the phone.

#### Before you begin

Cisco CME 3.4
                                       				or a later version.

Cisco Unified CME 7.1 or a later version to use the DND softkey.

Call-forwarding busy must be set for a SIP IP phone to use DND
                                       				to forward calls. For configuration information, see Configure Call Transfer and Forwarding .

### SUMMARY STEPS

- enable

- configure terminal

- voice register template template-tag

- softkeys idle { [ Cfwdall ] [ DND ] [ Gpickup ] [ Newcall ] [ Pickup ] [ Redial ] }

- softkeys ringIn [ Answer ] [ DND ]

- exit

- voice register
                                       				  pool phone-tag

- dnd

- template template-tag

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

voice register template template-tag

#### Example:

```
Router(config)# voice register template 5
```

Enters
                                             				ephone-template configuration mode to create an ephone template.

template-tag —Unique identifier for the ephone
                                                   					 template that is being created. Range: 1 to 10.

Step 4

softkeys idle { [ Cfwdall ] [ DND ] [ Gpickup ] [ Newcall ] [ Pickup ] [ Redial ] }

#### Example:

```
Router(config-register-temp)# softkeys idle
```

Modifies the
                                             				order and type of softkeys that display on a SIP phone during the idle call
                                             				state.

Step 5

softkeys ringIn [ Answer ] [ DND ]

#### Example:

```
Router(config-register-temp)# softkeys ringin dnd answer
```

Modifies the
                                             				order and type of softkeys that display on a SIP phone during the ringing call
                                             				state.

Step 6

exit

#### Example:

```
Router(config-register-temp)# exit
```

Exits
                                             				ephone-template configuration mode.

Step 7

voice register
                                                				  pool phone-tag

#### Example:

```
Router(config)# voice register pool 1
```

Enters voice
                                             				register pool configuration mode to set parameters for the SIP phone.

Step 8

dnd

#### Example:

```
Router(config-register-pool)# dnd
```

Enables DND
                                             				on the phone.

If Call
                                                   					 Forward No Answer is not configured for the extension, pressing the DND softkey
                                                   					 mutes the ringer for incoming calls.

Step 9

template template-tag

#### Example:

```
Router(config-register-pool)# template 5
```

Applies the
                                             				ephone template to the phone.

template-tag —Unique identifier of the template
                                                   					 that you created in Step 3 .

Step 10

end

#### Example:

```
Router(config-register-pool)# end
```

Returns to
                                             				privileged EXEC mode.

#### Example

The following
                                 		  example shows DND is enabled on phone 130, and the DND softkey is modified in
                                 		  template 6, which is assigned to the phone:

```
voice register template  6
 softkeys idle  Gpickup Pickup DND Redial
 softkeys ringIn  DND Answer 
!
voice register pool  130 
 id mac 001A.A11B.500E 
 type 7941 
 number 1 dn 30 
 template 6
 dnd
```

## Where to Go
                        	 Next

### Agent Status
                              		  Control for Ephone Hunt Groups and Cisco Unified CME B-ACD

Ephone hunt group
                              		  agents can control their ready/not-ready status (their ability to receive
                              		  calls) using the DND function or the HLog function of their phones. When they
                              		  use the DND softkey, they do not receive calls on any extension on their
                              		  phones. When they use the HLog softkey, they do not receive calls on hunt group
                              		  extensions, but they do receive calls on other extensions. For more information
                              		  on agent status control and the HLog function, see Call Coverage Features .

### Call
                              		  Forwarding

To use the DND
                              		  softkey to forward calls, enable call-forwarding no-answer for SCCP phones or
                              		  call-forward busy for SIP IP phones. See Configure Call Transfer and Forwarding .

### Feature Access
                              		  Codes (FACs)

DND can be
                              		  activated and deactivated using a feature access code (FAC) instead of the DND
                              		  softkey when standard or custom FACs are enabled. The following is the standard
                              		  FAC for DND:

DND **7

See Feature Access Codes .

### Softkey
                              		  Display

You can remove or
                              		  change the position of the DND softkey. See Customize Softkeys .

## Feature
                        	 Information for Do Not Disturb

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature
                                             					 Name

Cisco Unified CME Version

Feature
                                             					 Information

Do Not Disturb

7.1

Enhanced
                                             					 DND support on SIP phones to allow incoming calls to visually flash an alert.

3.4

Added
                                             					 support for Do-not-disturb (DND) softkey on SIP phones.

3.2.1

DND bypass
                                             					 for feature-ring phones was introduced.

3.2

DND was
                                             					 introduced.

|  | Cisco
                                             				  Unified IP Phone 7911, 7941, 7961, 7970, or 7971 with 8.3 Phone Load | Cisco
                                             				  Unified IP Phone 7911, 7941, 7961, 7970, or 7971 with 8.2 Phone Load or
                                             				  Cisco Unified IP Phone 7940 or 7960 |
|---|---|---|
| DND support | dnd command in voice register pool mode | dnd command in voice register pool mode |
| DND softkey
                                             				  display | softkey idle and softkey
                                                   						ringIn command in voice register template mode | dnd-control command in voice register template
                                             				  mode |
| Behavior
                                             				  when configured | Ringer is
                                             				  turned off for incoming calls. Visual alerting is provided. | Call is
                                             				  rejected and busy tone is played to the caller. |

| Restriction | Phone users
                                                   				  cannot enable DND for a shared line in a hunt group. The softkey displays in
                                                   				  the idle and ringing states but does not enable DND for shared lines in hunt
                                                   				  groups. DND is not supported for Analog SCCP devices. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone phone-tag Example: Router(config)# ephone 10 | Enters ephone
                                             				configuration mode. phone-tag —Unique sequence number that identifies
                                                   					 the ephone to be configured. |
| Step 4 | no dnd feature-ring Example: Router(config-ephone)# no dnd feature-ring | Enables
                                             				ringing on phone buttons configured for feature ring when the phone is in DND
                                             				mode. |
| Step 5 | end Example: Router(config-ephone)# end | Returns to
                                             				privileged EXEC mode. |

| Restriction | In versions
                                                   				  earlier than Cisco Unified CME 7.1, you enable the DND softkey on SIP phones by
                                                   				  using the dnd-control command. If you
                                                   				  enable DND on the phone and remove the DND softkey, the user cannot toggle DND
                                                   				  off at the phone. Cisco Unified IP Phone 7911G, 7941G, 7941GE, 7961G, 7961GE,
                                                				7970G, and 7971GE For SIP
                                                   				  phones using firmware 8.3 or a later version, the DND feature prevents calls
                                                   				  from ringing; it does not block calls or play a busy tone to the caller. If DND is
                                                   				  disabled by a phone user, it is not enabled after the phone resets or restarts.
                                                   				  DND must be enabled both in Cisco Unified CME and by using the DND
                                                   				  softkey on the phone. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register template template-tag Example: Router(config)# voice register template 5 | Enters
                                             				ephone-template configuration mode to create an ephone template. template-tag —Unique identifier for the ephone
                                                   					 template that is being created. Range: 1 to 10. |
| Step 4 | softkeys idle { [ Cfwdall ] [ DND ] [ Gpickup ] [ Newcall ] [ Pickup ] [ Redial ] } Example: Router(config-register-temp)# softkeys idle | Modifies the
                                             				order and type of softkeys that display on a SIP phone during the idle call
                                             				state. |
| Step 5 | softkeys ringIn [ Answer ] [ DND ] Example: Router(config-register-temp)# softkeys ringin dnd answer | Modifies the
                                             				order and type of softkeys that display on a SIP phone during the ringing call
                                             				state. |
| Step 6 | exit Example: Router(config-register-temp)# exit | Exits
                                             				ephone-template configuration mode. |
| Step 7 | voice register
                                                				  pool phone-tag Example: Router(config)# voice register pool 1 | Enters voice
                                             				register pool configuration mode to set parameters for the SIP phone. |
| Step 8 | dnd Example: Router(config-register-pool)# dnd | Enables DND
                                             				on the phone. If Call
                                                   					 Forward No Answer is not configured for the extension, pressing the DND softkey
                                                   					 mutes the ringer for incoming calls. |
| Step 9 | template template-tag Example: Router(config-register-pool)# template 5 | Applies the
                                             				ephone template to the phone. template-tag —Unique identifier of the template
                                                   					 that you created in Step 3 . |
| Step 10 | end Example: Router(config-register-pool)# end | Returns to
                                             				privileged EXEC mode. |

| Feature
                                             					 Name | Cisco Unified CME Version | Feature
                                             					 Information |
|---|---|---|
| Do Not Disturb | 7.1 | Enhanced
                                             					 DND support on SIP phones to allow incoming calls to visually flash an alert. |
| 3.4 | Added
                                             					 support for Do-not-disturb (DND) softkey on SIP phones. |
| 3.2.1 | DND bypass
                                             					 for feature-ring phones was introduced. |
| 3.2 | DND was
                                             					 introduced. |