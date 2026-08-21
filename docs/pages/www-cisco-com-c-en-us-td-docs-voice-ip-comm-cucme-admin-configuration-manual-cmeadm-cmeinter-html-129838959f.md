---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmeinter-html-129838959f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmeinter.html
retrieved_at: 2026-08-21T07:23:40.218192+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Intercom Lines

## Chapter: Intercom Lines

# Intercom Lines

## Information About Intercom Lines

### Intercom
                           	 Auto-Answer Lines

An intercom line is
                              		a dedicated two-way audio path between two phones. Cisco Unified CME supports
                              		intercom functionality for one-way and press-to-answer voice connections using
                              		a dedicated pair of intercom directory numbers on two phones that speed-dial
                              		each other.

When an intercom
                              		speed dial button is pressed, a call is speed-dialed to the directory that is
                              		the other half of the dedicated pair. The called phone automatically answers
                              		the call in speaker-phone mode with mute activated, providing a one-way voice
                              		path from the initiator to the recipient. A beep is sounded when the call is
                              		auto-answered to alert the recipient to the incoming call. To respond to the
                              		intercom call and open a two-way voice path, the recipient deactivates the mute
                              		function by pressing the Mute button or, on phones such as the Cisco Unified IP
                              		Phone 7910, lifting the handset.

In Cisco CME 3.2.1
                              		and later versions, you can deactivate the speaker-mute function on intercom
                              		calls. For example, if phone user 1 makes an intercom call to phone user 2,
                              		both users hear each other on connection when no-mute is configured. The
                              		benefit is that people who receive intercom calls can be heard without them
                              		having to disable the mute function. The disadvantage is that nearby background
                              		sounds and conversations can be heard the moment a person receives an intercom
                              		call, regardless of whether they are ready to take a call or not.

Intercom lines
                              		cannot be used in shared-line configurations. If a directory number is
                              		configured for intercom operation, it must be associated with one IP phone
                              		only. The intercom attribute causes an IP phone line to operate as an autodial
                              		line for outbound calls and as an autoanswer-with-mute line for inbound calls. Intercom
                                 		  Lines shows an intercom between a receptionist and a manager.

To prevent an
                              		unauthorized phone from dialing an intercom line (and creating a situation in
                              		which a phone automatically answers a nonintercom call), you can assign the
                              		intercom a directory number that includes an alphabetic character. No one can
                              		dial the alphabetic character from a normal phone, but the phone at the other
                              		end of the intercom can be configured to dial the number that contains the
                              		alphabetic character through the Cisco Unified CME router. For example, the
                              		intercom ephone-dns in Intercom
                                 		  Lines are assigned numbers with alphabetic characters so that only the receptionist
                              		can call the manager on his or her intercom line, and no one except the manager
                              		can call the receptionist on his or her intercom line.

An intercom
                                          		  requires the configuration of two ephone-dns, one each on a separate phone.

### Whisper
                           	 Intercom

When a phone user
                              		dials a whisper intercom line, the called phone automatically answers using
                              		speaker-phone mode, providing a one-way voice path from the caller to the
                              		called party, regardless of whether the called party is busy or idle.

Unlike the standard
                              		intercom feature, this feature allows an intercom call to a busy extension. The
                              		calling party can only be heard by the recipient. The original caller on the
                              		receiving phone does not hear the whisper page. The phone receiving a whisper
                              		page displays the extension and name of the party initiating the whisper page
                              		and Cisco Unified CME plays a zipzip tone before the called party hears the
                              		caller's voice. If the called party wants to speak to the caller, the called
                              		party selects the intercom line button on their phone. The lamp for intercom
                              		buttons are colored amber to indicate one-way audio for whisper intercom and
                              		green to indicate two-way audio for standard intercom.

You must configure a
                              		whisper intercom directory number for each phone that requires the Whisper
                              		Intercom feature. A whisper intercom directory number can place calls only to
                              		another whisper intercom directory number. Calls between a whisper intercom
                              		directory number and a standard directory number or intercom directory number
                              		are rejected with a busy tone.

This feature is
                              		supported in Cisco Unified CME 7.1 and later versions. For configuration
                              		information, see Configure Whisper Intercom on SCCP Phones .

### SIP
                           	 Intercom

In Cisco Unified CME
                              		8.8, the SIP Intercom feature is released as part of the 8.3(1) IP Phone
                              		firmware.

The SIP intercom
                              		line provides a one-way voice path from the caller to the called phone. When a
                              		phone user dials the intercom line, the called phone automatically answers the
                              		call in speaker-phone mode with Mute activated. If the called SIP phone is busy
                              		with a connected call or with an outgoing call that has not been connected, the
                              		call is whispered into the called phone.

As soon as the
                              		called phone auto-answers, the intercom call recipient has three options:

Listen to the
                                    			 one-way audio of the intercom caller without answering.

End the call by
                                    			 pressing the speaker-phone button or the EndCall softkey.

Press the
                                    			 intercom button to create a two-way voice path and respond to the intercom
                                    			 caller.

If the called phone
                              		is busy when the intercom call arrives and a response is requested, the active
                              		call is put on hold and the outgoing call that is not connected yet is canceled
                              		before the intercom call is connected for a two-way voice path.

The lamp for the
                                          		  intercom line button displays an amber light for one-way intercom and green for
                                          		  a two-way voice path.

You should configure
                              		an intercom directory number to begin and end an intercom call for each phone
                              		that requires the Intercom feature. For configuration information, see Configure Intercom Call Option on SIP Phones .

However, a standard
                              		directory number without the intercom option configured can also place an
                              		intercom call. The called phone also has the option of responding to the call
                              		by pressing the intercom line button to establish a two-way voice path with the
                              		originator without the intercom option configured.

Table 1 shows the supported SIP-SCCP interactions for the SIP Intercom feature.

Originator

Terminator

Intercom

SIP normal
                                          				  line

SIP intercom
                                          				  line

Supported

SIP intercom
                                          				  line

SIP intercom
                                          				  line

Supported

SIP normal
                                          				  line

SCCP whisper
                                          				  intercom line

Not
                                          				  Supported

SIP intercom
                                          				  line

SCCP whisper
                                          				  intercom line

Not
                                          				  Supported

SCCP normal
                                          				  line

SIP intercom
                                          				  line

Supported

SCCP normal
                                          				  line

SCCP whisper
                                          				  intercom line

Not
                                          				  Supported

SCCP whisper
                                          				  intercom line

SIP intercom
                                          				  line

Not
                                          				  Supported

SCCP whisper
                                          				  intercom line

SCCP whisper
                                          				  intercom line

Supported

SIP normal
                                          				  line

SIP normal
                                          				  line

Not
                                          				  Supported

SIP intercom
                                          				  line

SIP normal
                                          				  line

Not
                                          				  Supported

SCCP normal
                                          				  line

SIP normal
                                          				  line

Not
                                          				  Supported

SCCP
                                          				  intercom line

SIP normal
                                          				  line

Not
                                          				  Supported

SIP normal
                                          				  line

SCCP
                                          				  normal line

Not
                                          				  Supported

SIP
                                          				  intercom line

SCCP
                                          				  normal line

Not
                                          				  Supported

SCCP
                                          				  normal line

SCCP
                                          				  normal line

Not
                                          				  Supported

SCCP
                                          				  intercom line

SCCP
                                          				  normal line

Not
                                          				  Supported

#### Extension
                              	 Number

The extension number
                                 		of an intercom line can be included in an extension mobility user-profile or
                                 		extension mobility logout-profile.

The BLF feature can
                                 		define the extension number of an intercom line as a speed dial on a Cisco
                                 		Unified CME phone, allowing the line status of the intercom line to be
                                 		monitored.

For configuration
                                 		information, see Configure Extension Mobility for SIP Phones .

## Configure Intercom Lines

### Configure an
                           	 Intercom Auto-Answer Line on SCCP Phones

To enable a
                                 		  two-way audio path between two phones, perform the following steps for each
                                 		  Cisco Unified SCCP IP phone at both ends of the two-way voice path.

Restriction

Intercom
                                                      				  lines cannot be dual-line.

If a
                                                      				  directory number is configured for intercom operation, it can be associated
                                                      				  with only one Cisco Unified IP phone.

Each phone,
                                                      				  at both ends of the two-way voice path, requires a separate configuration.

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn dn-tag

- number number

- name name

- intercom extension-number [[ barge-in [ no-mute ] | no-auto-answer | no-mute ] [ label label ]] | label label ]

- exit

- ephone phone-tag

- button button-number : dn-tag [ [ button-number : dn-tag ] ... ]

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
Router(config)# ephone-dn 11
```

Enters
                                             				ephone-dn configuration mode.

Do not use
                                                   					 the dual-line keyword with this command. Intercom ephone-dns
                                                   					 cannot be dual-line.

Step 4

number number

#### Example:

```
Router(config-ephone-dn)# number A2345
```

Assigns a
                                             				valid intercom number.

Using one
                                                   					 or more alphabetic characters in an intercom number ensures that the number can
                                                   					 only be dialed from the one other intercom number that is programmed to dial
                                                   					 this number. The number cannot be dialed from a normal phone if it contains an
                                                   					 alphabetic character.

Step 5

name name

#### Example:

```
Router(config-ephone-dn)# name intercom
```

Sets a name to
                                             				be associated with the ephone-dn.

This name
                                                   					 is used for caller-ID displays and also shows up in the local directory
                                                   					 associated with the ephone-dn.

Step 6

intercom extension-number [[ barge-in [ no-mute ] | no-auto-answer | no-mute ] [ label label ]] | label label ]

#### Example:

```
Router(config-ephone-dn)# intercom A2346 label Security
```

Defines the
                                             				directory number that is speed-dialed for the intercom feature when this line
                                             				is used.

Step 7

exit

#### Example:

```
Router(config-ephone-dn)# exit
```

Exits
                                             				ephone-dn configuration mode.

Step 8

ephone phone-tag

#### Example:

```
Router(config)# ephone 24
```

Enters
                                             				ephone configuration mode.

Step 9

button button-number : dn-tag [ [ button-number : dn-tag ] ... ]

#### Example:

```
Router(config-ephone)# button 1:1 2:4 3:14
```

Assigns a
                                             				button number to the intercom ephone-dn being configured.

Use the
                                                   					 colon separator ( : ) between
                                                   					 the button number and the intercom ephone-dn tag to indicate a normal ring for
                                                   					 the intercom line.

Step 10

end

#### Example:

```
Router(config)# exit
```

Exits ephone
                                             				configuration mode and enters privileged EXEC mode.

### Configure Whisper
                           	 Intercom on SCCP Phones

To enable the
                                 		  Whisper Intercom feature on a directory number, perform the following steps.

Restriction

Single-line
                                                   				  phone models, such as the Cisco Unified IP Phone 7906 or 7911, are not
                                                   				  supported.

Whisper
                                                   				  intercom directory numbers can place calls only to other whisper intercom
                                                   				  numbers.

A directory
                                                   				  number can be configured as either a regular intercom or a whisper intercom,
                                                   				  not both.

Dual-line
                                                   				  and octo-line directory numbers are not supported as intercom lines.

Only one
                                                   				  intercom call, either incoming or outgoing, is allowed on the phone at one
                                                   				  time.

Call
                                                   				  features are not supported on intercom calls.

#### Before you begin

Cisco Unified
                                       				CME 7.1 or a later version.

IP phones
                                       				require SCCP 12.0 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn dn-tag

- whisper-intercom [ label string | speed-dial number [ label string ]]

- end

- show ephone-dn
                                       				  whisper

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
Router(config)# ephone-dn 1
```

Enters ephone
                                             				configuration mode to create a directory number for a SCCP phone.

Step 4

whisper-intercom [ label string | speed-dial number [ label string ]]

#### Example:

```
Router(config-ephone-dn)# whisper intercom
```

Enables
                                             				whisper intercom on a directory number.

label string —(Optional) Alphanumeric label that
                                                   					 identifies the whisper intercom button. String can contain a maximum of 30
                                                   					 characters.

speed-dial number —(Optional) Telephone number to speed dial.

Step 5

end

#### Example:

```
Router(config-ephone-dn)# end
```

Exits to
                                             				privileged EXEC mode.

Step 6

show ephone-dn
                                                				  whisper

#### Example:

```
Router# show ephone-dn whisper
```

Displays
                                             				information about whisper intercom ephone-dns that have been created.

#### Example

The following
                                 		  example shows Whisper Intercom configured on extension 2004:

```
ephone-dn  24
 number 2004
 whisper-intercom label "sales"!
!
!
ephone  24
 mac-address 02EA.EAEA.0001
 button  1:24
```

### Configure an
                           	 Intercom Auto-Answer Line on SIP Phones

To enable the
                                 		  Intercom Auto-Answer feature for Cisco Unified SIP IP phones, perform the
                                 		  following steps for each IP phone at both ends of the two-way voice path.

Restriction

If a
                                                   				  directory number is configured for intercom operation, it can be associated
                                                   				  with only one Cisco Unified IP phone.

Each phone,
                                                   				  at each end of the two-way voice path, requires a separate configuration.

#### Before you begin

Cisco CME 3.4 or
                                 		  a later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice register dn dn-tag

- number number

- auto-answer

- exit

- voice register pool pool-tag

- id { mac address }

- type phone-type

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

voice register dn dn-tag

#### Example:

```
Router(config-register-global)# voice register dn 1
```

Enters voice
                                             				register dn configuration mode to define a directory number for a Cisco Unified
                                             				SIP IP phone, intercom line, voice port, or an MWI.

Step 4

number number

#### Example:

```
Router(config-register-dn)# number A5001
```

Defines a
                                             				valid number for the directory number being configured.

To prevent
                                                   					 non-intercom originators from manually dialing an intercom destination, the
                                                   					 number string can contain alphabetic characters enabling the number to be
                                                   					 dialed only by the Cisco Unified CME router and not from telephone keypads.

Step 5

auto-answer

#### Example:

```
Router(config-register-dn)# auto-answer
```

Enables the
                                             				Intercom Auto-Answer feature on the directory number being configured.

Step 6

exit

#### Example:

```
Router(config-register-dn)# exit
```

Exits voice
                                             				register dn configuration mode.

Step 7

voice register pool pool-tag

#### Example:

```
Router(config)# voice register pool 3
```

Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a Cisco
                                             				Unified SIP IP phone in Cisco Unified CME.

Step 8

id { mac address }

#### Example:

```
Router(config-register-pool)# id mac 0009.A3D4.1234
```

Explicitly
                                             				identifies a locally available individual Cisco Unified SIP IP phone to support
                                             				a degree of authentication.

Step 9

type phone-type

#### Example:

```
Router(config-register-pool)# type 7960-7940
```

Defines a
                                             				phone type for the Cisco Unified SIP IP phone being configured.

Step 10

number tag dn dn-tag

#### Example:

```
Router(config-register-pool)# number 1 dn 17
```

Associates a
                                             				directory number with the Cisco Unified SIP IP phone being configured.

Step 11

end

#### Example:

```
Router(config-register-pool)# end
```

Exits voice
                                             				register pool configuration mode and enters privileged EXEC mode.

### Configure Intercom
                           	 Call Option on SIP Phones

Restriction

The Intercom
                                                      				  feature is not supported on single-line phones because the intercom line cannot
                                                      				  be the primary line of a Cisco Unified CME SIP IP phone.

The intercom
                                                      				  line cannot be shared among SIP phones.

FAC is not
                                                      				  supported on a SIP intercom call because the keys are disabled.

#### Before you begin

Cisco Unified
                                       				CME 8.8 or a later version.

8.3(1) phone
                                       				firmware or a later version is installed on the Cisco Unified SIP IP phone.

### SUMMARY STEPS

- enable

- configure terminal

- voice register dn dn-tag

- number number

- intercom [ speed-dial digit-string ] [ label label-text ]

- exit

- voice register pool pool-tag

- id { network address mask mask | ip address mask mask | mac address }

- type phone-type

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

voice register dn dn-tag

#### Example:

```
Router(config)# voice register dn 4
```

Enters voice
                                             				register dn configuration mode to define an extension for a SIP intercom line.

Step 4

number number

#### Example:

```
Router(config-register-dn)# number 4001
```

Associates a
                                             				telephone or extension number with a Cisco Unified SIP phone in a Cisco Unified
                                             				CME system.

Step 5

intercom [ speed-dial digit-string ] [ label label-text ]

#### Example:

```
Router(config-register-dn)# intercom [ speed-dial 4002 ] [ label intercom4001 ]
```

Enables the
                                             				intercom call option on a Cisco Unified SIP IP phone.

(Optional) speed-dial —Enables the intercom line user to place
                                                   					 a call to a pre-configured destination. If the speed dial is not configured, it
                                                   					 simply initiates a new call on the intercom line and waits for the user to dial
                                                   					 the destination number.

(Optional) label label-text —String that contains identifying text
                                                   					 to be displayed next to the speed dial button. Enclose the string in quotation
                                                   					 marks if the string contains a space.

Step 6

exit

#### Example:

```
Router(config-register-dn)# exit
```

Exits
                                             				configuration mode to the next highest mode in the configuration mode
                                             				hierarchy.

Step 7

voice register pool pool-tag

#### Example:

```
Router(config)# voice register pool 3
```

Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a Cisco
                                             				Unified SIP phone in Cisco Unified CME.

Step 8

id { network address mask mask | ip address mask mask | mac address }

#### Example:

```
Router(config-register-pool)# id mac 0009.A3D4.
```

Explicitly
                                             				identifies a locally available individual Cisco Unified SIP phone to support a
                                             				degree of authentication.

Step 9

type phone-type

#### Example:

```
Router(config-register-pool)# type 7940
```

Defines a
                                             				phone type for the Cisco Unified SIP phone being configured.

Step 10

number tag dn dn-tag

#### Example:

```
Router(config-register-pool)# number 1 dn 17
```

Associates a
                                             				directory number tag with the Cisco Unified SIP IP phone being configured.

Step 11

end

#### Example:

```
Router(config-register-dn)# end
```

Exits to
                                             				privileged EXEC mode.

## Configuration Examples for Intercom Lines

### Example for
                           	 Configuring Intercom Lines

The following
                                 		  example shows an intercom between two Cisco Unified IP phones. In this example,
                                 		  ephone-dn 2 and ephone-dn 4 are normal extensions, while ephone-dn 18 and
                                 		  ephone-dn 19 are set as an intercom pair. Ephone-dn 18 is associated with line
                                 		  button 2 on Cisco Unified IP phone 4. ephone-dn 19 is associated with line
                                 		  button 2 on Cisco Unified IP phone 5. The two ephone-dns provide a two-way
                                 		  intercom between the two Cisco Unified IP phones.

```
ephone-dn 2
 number 5333

ephone-dn 4
 number 5222

ephone-dn 18
 number 5001
 name “intercom”
 intercom 5002 barge-in

ephone-dn 19
 name “intercom”
 number 5002
 intercom 5001 barge-in

ephone 4
 button 1:2 2:18

ephone 5
 button 1:4 2:19
```

### Example for
                           	 Configuring SIP Intercom Support

The following
                                 		  example shows SIP Intercom configured on extension 1001:

```
voice register dn 1
 number 1001
 intercom [speed-dial 1002] [label intercom1001]

voice register pool 1
 id mac 001D.452D.580C
 type 7962
 number 1 dn 2
 number 2 dn 1
```

## Where to Go
                        	 Next

If you are done
                           		modifying parameters for phones in Cisco Unified CME, generate a new
                           		configuration file and restart the phones. See Generate Configuration Files for Phones .

### Paging

The paging feature
                              		  sets up a one-way audio path to deliver information to a group of phones at one
                              		  time. For more information, see Paging .

## Feature
                        	 Information for Intercom Lines

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature
                                             					 Name

Cisco Unified CME Version

Feature
                                             					 Information

SIP
                                             					 Intercom

8.8

Adds
                                             					 intercom support to Cisco Unified SIP IP phones connected to a Cisco Unified
                                             					 CME system.

Whisper
                                             					 Intercom

7.1

Introduces
                                             					 whisper intercom feature.

Intercom
                                             					 Lines

3.4

Adds
                                             					 intercom feature, with no-mute function, for supported Cisco Unified IP phones
                                             					 that are connected to a Cisco Unified CME router and running SIP.

3.2.1

Introduces
                                             					 the no-mute function.

2.0

Introduces
                                             					 the Intercom feature.

| Note | An intercom
                                          		  requires the configuration of two ephone-dns, one each on a separate phone. |
|---|---|

| Note | The lamp for the
                                          		  intercom line button displays an amber light for one-way intercom and green for
                                          		  a two-way voice path. |
|---|---|

| Originator | Terminator | Intercom |
|---|---|---|
| SIP normal
                                          				  line | SIP intercom
                                          				  line | Supported |
| SIP intercom
                                          				  line | SIP intercom
                                          				  line | Supported |
| SIP normal
                                          				  line | SCCP whisper
                                          				  intercom line | Not
                                          				  Supported |
| SIP intercom
                                          				  line | SCCP whisper
                                          				  intercom line | Not
                                          				  Supported |
| SCCP normal
                                          				  line | SIP intercom
                                          				  line | Supported |
| SCCP normal
                                          				  line | SCCP whisper
                                          				  intercom line | Not
                                          				  Supported |
| SCCP whisper
                                          				  intercom line | SIP intercom
                                          				  line | Not
                                          				  Supported |
| SCCP whisper
                                          				  intercom line | SCCP whisper
                                          				  intercom line | Supported |
| SIP normal
                                          				  line | SIP normal
                                          				  line | Not
                                          				  Supported |
| SIP intercom
                                          				  line | SIP normal
                                          				  line | Not
                                          				  Supported |
| SCCP normal
                                          				  line | SIP normal
                                          				  line | Not
                                          				  Supported |
| SCCP
                                          				  intercom line | SIP normal
                                          				  line | Not
                                          				  Supported |
| SIP normal
                                          				  line | SCCP
                                          				  normal line | Not
                                          				  Supported |
| SIP
                                          				  intercom line | SCCP
                                          				  normal line | Not
                                          				  Supported |
| SCCP
                                          				  normal line | SCCP
                                          				  normal line | Not
                                          				  Supported |
| SCCP
                                          				  intercom line | SCCP
                                          				  normal line | Not
                                          				  Supported |

| Restriction | Intercom
                                                      				  lines cannot be dual-line. If a
                                                      				  directory number is configured for intercom operation, it can be associated
                                                      				  with only one Cisco Unified IP phone. Each phone,
                                                      				  at both ends of the two-way voice path, requires a separate configuration. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-dn dn-tag Example: Router(config)# ephone-dn 11 | Enters
                                             				ephone-dn configuration mode. Do not use
                                                   					 the dual-line keyword with this command. Intercom ephone-dns
                                                   					 cannot be dual-line. |
| Step 4 | number number Example: Router(config-ephone-dn)# number A2345 | Assigns a
                                             				valid intercom number. Using one
                                                   					 or more alphabetic characters in an intercom number ensures that the number can
                                                   					 only be dialed from the one other intercom number that is programmed to dial
                                                   					 this number. The number cannot be dialed from a normal phone if it contains an
                                                   					 alphabetic character. |
| Step 5 | name name Example: Router(config-ephone-dn)# name intercom | Sets a name to
                                             				be associated with the ephone-dn. This name
                                                   					 is used for caller-ID displays and also shows up in the local directory
                                                   					 associated with the ephone-dn. |
| Step 6 | intercom extension-number [[ barge-in [ no-mute ] \| no-auto-answer \| no-mute ] [ label label ]] \| label label ] Example: Router(config-ephone-dn)# intercom A2346 label Security | Defines the
                                             				directory number that is speed-dialed for the intercom feature when this line
                                             				is used. |
| Step 7 | exit Example: Router(config-ephone-dn)# exit | Exits
                                             				ephone-dn configuration mode. |
| Step 8 | ephone phone-tag Example: Router(config)# ephone 24 | Enters
                                             				ephone configuration mode. |
| Step 9 | button button-number : dn-tag [ [ button-number : dn-tag ] ... ] Example: Router(config-ephone)# button 1:1 2:4 3:14 | Assigns a
                                             				button number to the intercom ephone-dn being configured. Use the
                                                   					 colon separator ( : ) between
                                                   					 the button number and the intercom ephone-dn tag to indicate a normal ring for
                                                   					 the intercom line. |
| Step 10 | end Example: Router(config)# exit | Exits ephone
                                             				configuration mode and enters privileged EXEC mode. |

| Restriction | Single-line
                                                   				  phone models, such as the Cisco Unified IP Phone 7906 or 7911, are not
                                                   				  supported. Whisper
                                                   				  intercom directory numbers can place calls only to other whisper intercom
                                                   				  numbers. A directory
                                                   				  number can be configured as either a regular intercom or a whisper intercom,
                                                   				  not both. Dual-line
                                                   				  and octo-line directory numbers are not supported as intercom lines. Only one
                                                   				  intercom call, either incoming or outgoing, is allowed on the phone at one
                                                   				  time. Call
                                                   				  features are not supported on intercom calls. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-dn dn-tag Example: Router(config)# ephone-dn 1 | Enters ephone
                                             				configuration mode to create a directory number for a SCCP phone. |
| Step 4 | whisper-intercom [ label string \| speed-dial number [ label string ]] Example: Router(config-ephone-dn)# whisper intercom | Enables
                                             				whisper intercom on a directory number. label string —(Optional) Alphanumeric label that
                                                   					 identifies the whisper intercom button. String can contain a maximum of 30
                                                   					 characters. speed-dial number —(Optional) Telephone number to speed dial. |
| Step 5 | end Example: Router(config-ephone-dn)# end | Exits to
                                             				privileged EXEC mode. |
| Step 6 | show ephone-dn
                                                				  whisper Example: Router# show ephone-dn whisper | Displays
                                             				information about whisper intercom ephone-dns that have been created. |

| Restriction | If a
                                                   				  directory number is configured for intercom operation, it can be associated
                                                   				  with only one Cisco Unified IP phone. Each phone,
                                                   				  at each end of the two-way voice path, requires a separate configuration. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register dn dn-tag Example: Router(config-register-global)# voice register dn 1 | Enters voice
                                             				register dn configuration mode to define a directory number for a Cisco Unified
                                             				SIP IP phone, intercom line, voice port, or an MWI. |
| Step 4 | number number Example: Router(config-register-dn)# number A5001 | Defines a
                                             				valid number for the directory number being configured. To prevent
                                                   					 non-intercom originators from manually dialing an intercom destination, the
                                                   					 number string can contain alphabetic characters enabling the number to be
                                                   					 dialed only by the Cisco Unified CME router and not from telephone keypads. |
| Step 5 | auto-answer Example: Router(config-register-dn)# auto-answer | Enables the
                                             				Intercom Auto-Answer feature on the directory number being configured. |
| Step 6 | exit Example: Router(config-register-dn)# exit | Exits voice
                                             				register dn configuration mode. |
| Step 7 | voice register pool pool-tag Example: Router(config)# voice register pool 3 | Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a Cisco
                                             				Unified SIP IP phone in Cisco Unified CME. |
| Step 8 | id { mac address } Example: Router(config-register-pool)# id mac 0009.A3D4.1234 | Explicitly
                                             				identifies a locally available individual Cisco Unified SIP IP phone to support
                                             				a degree of authentication. |
| Step 9 | type phone-type Example: Router(config-register-pool)# type 7960-7940 | Defines a
                                             				phone type for the Cisco Unified SIP IP phone being configured. |
| Step 10 | number tag dn dn-tag Example: Router(config-register-pool)# number 1 dn 17 | Associates a
                                             				directory number with the Cisco Unified SIP IP phone being configured. |
| Step 11 | end Example: Router(config-register-pool)# end | Exits voice
                                             				register pool configuration mode and enters privileged EXEC mode. |

| Restriction | The Intercom
                                                      				  feature is not supported on single-line phones because the intercom line cannot
                                                      				  be the primary line of a Cisco Unified CME SIP IP phone. The intercom
                                                      				  line cannot be shared among SIP phones. FAC is not
                                                      				  supported on a SIP intercom call because the keys are disabled. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register dn dn-tag Example: Router(config)# voice register dn 4 | Enters voice
                                             				register dn configuration mode to define an extension for a SIP intercom line. |
| Step 4 | number number Example: Router(config-register-dn)# number 4001 | Associates a
                                             				telephone or extension number with a Cisco Unified SIP phone in a Cisco Unified
                                             				CME system. |
| Step 5 | intercom [ speed-dial digit-string ] [ label label-text ] Example: Router(config-register-dn)# intercom [ speed-dial 4002 ] [ label intercom4001 ] | Enables the
                                             				intercom call option on a Cisco Unified SIP IP phone. (Optional) speed-dial —Enables the intercom line user to place
                                                   					 a call to a pre-configured destination. If the speed dial is not configured, it
                                                   					 simply initiates a new call on the intercom line and waits for the user to dial
                                                   					 the destination number. (Optional) label label-text —String that contains identifying text
                                                   					 to be displayed next to the speed dial button. Enclose the string in quotation
                                                   					 marks if the string contains a space. |
| Step 6 | exit Example: Router(config-register-dn)# exit | Exits
                                             				configuration mode to the next highest mode in the configuration mode
                                             				hierarchy. |
| Step 7 | voice register pool pool-tag Example: Router(config)# voice register pool 3 | Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a Cisco
                                             				Unified SIP phone in Cisco Unified CME. |
| Step 8 | id { network address mask mask \| ip address mask mask \| mac address } Example: Router(config-register-pool)# id mac 0009.A3D4. | Explicitly
                                             				identifies a locally available individual Cisco Unified SIP phone to support a
                                             				degree of authentication. |
| Step 9 | type phone-type Example: Router(config-register-pool)# type 7940 | Defines a
                                             				phone type for the Cisco Unified SIP phone being configured. |
| Step 10 | number tag dn dn-tag Example: Router(config-register-pool)# number 1 dn 17 | Associates a
                                             				directory number tag with the Cisco Unified SIP IP phone being configured. |
| Step 11 | end Example: Router(config-register-dn)# end | Exits to
                                             				privileged EXEC mode. |

| Feature
                                             					 Name | Cisco Unified CME Version | Feature
                                             					 Information |
|---|---|---|
| SIP
                                             					 Intercom | 8.8 | Adds
                                             					 intercom support to Cisco Unified SIP IP phones connected to a Cisco Unified
                                             					 CME system. |
| Whisper
                                             					 Intercom | 7.1 | Introduces
                                             					 whisper intercom feature. |
| Intercom
                                             					 Lines | 3.4 | Adds
                                             					 intercom feature, with no-mute function, for supported Cisco Unified IP phones
                                             					 that are connected to a Cisco Unified CME router and running SIP. |
| 3.2.1 | Introduces
                                             					 the no-mute function. |
| 2.0 | Introduces
                                             					 the Intercom feature. |