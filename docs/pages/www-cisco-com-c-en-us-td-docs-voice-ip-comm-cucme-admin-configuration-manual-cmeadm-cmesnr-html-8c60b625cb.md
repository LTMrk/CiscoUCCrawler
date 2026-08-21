---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmesnr-html-8c60b625cb
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmesnr.html
retrieved_at: 2026-08-21T07:24:05.929917+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Single Number Reach

## Chapter: Single Number Reach

# Single Number Reach

## Information About Single Number Reach

### Overview of Single Number Reach

The Single Number Reach (SNR) feature allows users to answer incoming
                              		calls to their extension on either their desktop IP phone or at a remote
                              		destination, such as a mobile phone. Users can pick up active calls on the
                              		desktop phone or the remote phone without losing the connection. This enables
                              		callers to dial a single number to reach the phone user. Calls that are not
                              		answered can be forwarded to voice mail.

Remote destinations may include the following devices:

Mobile (cellular) phones.

Smart phones.

IP phones not belonging to the same Cisco Unified CME router as the
                                    			 desktop phone.

Home phone numbers in the PSTN. Supported PSTN interfaces include
                                    			 PRI, BRI, SIP, and FXO.

For incoming calls to the SNR extension, Cisco Unified CME rings the
                              		desktop IP phone first. If the IP phone does not answer within the configured
                              		amount of time, it rings the configured remote number while continuing to ring
                              		the IP phone. Unanswered calls are sent to a configured voice-mail number.

The IP phone user has these options for handling calls to the SNR
                              		extension:

Pull back the call from the remote phone—Phone user can manually
                                    			 pull back the call to the SNR extension by pressing the Resume softkey, which
                                    			 disconnects the call from the remote phone.

Send the call to remote phone—Phone user can send the call to the
                                    			 remote phone by using the Mobility softkey. While connected to the call, the
                                    			 phone user can press the Mobility softkey and select Send call to mobile . The call is forwarded to
                                    			 the remote phone.

Enable or disable Single Number Reach—While the IP phone is in the
                                    			 idle state, the user can toggle the SNR feature on and off by using the
                                    			 Mobility softkey. If the user disables SNR, Cisco Unified CME does not ring the
                                    			 remote number.

IP phone users can modify their own SNR settings directly from the phone
                              		by using the menu available with the Services feature button. You must enable
                              		the feature on the phone to allow a phone user to access the user interface.

This feature is supported in Cisco Unified CME 7.1 and later versions on
                              		SCCP IP phones that support softkeys.

### SNR Enhancements

Cisco Unified CME 8.5 supports the following enhancements in the Single
                              		Number Reach (SNR) feature:

#### Hardware Conference

In Cisco Unified CME 8.5, you can send a call to a mobile phone after
                                 		joining a hardware conference. After joining the hardware conference, all
                                 		conference callers are blind-transferred to hardware DN. The call character of
                                 		the ephone changes from incoming call to outgoing call and you are able to send
                                 		a call to the mobile.

#### Call Park, Call
                              	 Pickup, and Call Retrieval

In earlier versions
                                 		of Cisco Unified CME, Call Park, Call Pickup, and Call Retrieval features were
                                 		not supported for SNR. Cisco Unified CME 8.5 and later versions allows you to
                                 		park, pickup, or retrieve an SNR call,

Cisco Unified CME
                                 		8.5 enhances the SNR feature to allow you to see the local number on your cell
                                 		phone instead of the calling party number. You can configure the snr calling
                                 		number local command under ephone-dn configuration mode to view the caller ID
                                 		of the SNR phone. For information on configuring SNR calling number local, see Configure Single Number Reach Enhancements on SCCP Phones .

#### Answer Too Soon
                              	 Timer

On non-FXO ports,
                                 		you can set an snr answer too soon timer to prevent the calls from rolling to
                                 		the voice mailbox of your cell phone. When the cell phone rolls to the voice
                                 		mail within the answer too soon timer range (1 to 5 seconds), the mobile phone
                                 		call leg is immediately disconnected. You can configure the snr answer too soon
                                 		command under ephone-dn mode. For more information, see Configure Single Number Reach Enhancements on SCCP Phones .
                                 		The answer-too soon timer is not applicable when sending the call to a mobile.

#### SNR Phone Stops
                              	 Ringing After Mobile Phone Answers

When SNR is deployed
                                 		on non-FXO ports, if cell phone picks up an SNR call, you are connected to the
                                 		call. The ephone stops ringing further and is placed on hold. You can configure
                                 		the snr ring-stop command under ephone-dn configuration mode to stop the ephone
                                 		from ringing and to place the phone on hold. For more information, see Configure Single Number Reach Enhancements on SCCP Phones .

### Single Number Reach for Cisco Unified SIP IP Phones

Before Cisco Unified CME 9.0, the Single Number Reach (SNR) feature
                              		enabled the user to be reached on two numbers: a regular directory number (DN)
                              		on the ephone and a public switched telephone network (PSTN) connection (either
                              		a PRI/BRI/FXO port or a SIP interface). For incoming calls to the ephone, the
                              		Cisco Unified CME called the ephone DN first. When the ephone DN did not answer
                              		within a configured time, the Cisco Unified CME called a preconfigured PSTN
                              		number while continually calling the ephone DN.

In Cisco Unified CME 9.0 and later versions, the following SNR features
                              		are supported for Cisco Unified SIP IP phones:

Enable and disable the Extension Mobility (EM) feature on a Cisco
                                    			 Unified SIP IP phone—Use the Mobility softkey or PLK as a toggle or use the mobility and no mobility commands to enable or disable
                                    			 the Mobility feature on a Cisco Unified SIP IP phone.

Manual pull back of a call on a mobile phone—Use the Resume softkey
                                    			 to manually bring a call back to the SNR DN.

Send a call to a mobile PSTN phone—Send a call to the mobile PSTN
                                    			 phone using the Mobility softkey while the Cisco Unified SIP IP phone is on a
                                    			 call. Select “ Send call to mobile ” and the call is
                                    			 handed off to the mobile phone.

Send a call to a mobile phone regardless of whether the SNR phone is
                                    			 the originating or the terminating side—Ensure that the SNR feature is
                                    			 configured in voice register dn or ephone-dn configuration mode to send a call
                                    			 to a mobile phone regardless of whether the SNR phone is the originating or
                                    			 terminating side. Use the Mobility softkey, select “ Send call to
                                       				mobile ,” and the call is handed off to the mobile phone.

For calls from a PSTN, local, or VoIP phone to a Cisco Unified SIP IP
                              		phone configured as an SNR phone, the Cisco Unified CME calls the SIP SNR or
                              		the mobile phone DN.

When you answer the call on the SIP SNR phone, you can send the call to
                              		the PSTN/BRI/PRI/SIP phone.

When you answer the call on the mobile phone, the Resume softkey is
                              		displayed on the SIP SNR phone and allows the call to be pulled back to the SIP
                              		SNR phone. You can repeatedly pull the call back from the PSTN phone to the SIP
                              		SNR phone or from the SIP SNR phone to the PSTN phone.

If the cfwd-noan keyword is configured and both the mobile
                              		and SIP SNR phones do not answer, the call is redirected to a preconfigured
                              		extension number when the end of a preconfigured time delay is reached.

The following shows how SNR phones configured with Cisco Unified SIP IP
                              		phones behave differently from those configured with Cisco Unified SCCP IP
                              		phones when sending a call to a mobile:

For Cisco Unified SCCP IP phones, the Resume softkey is displayed on the SCCP SNR phone as soon as the call is sent to the
                                    mobile phone.

For Cisco Unified SIP IP phones, the Resume softkey is displayed on the SIP SNR phone as soon as the mobile phone answers
                                    the call.

Cisco Unified CME 9.0 and later supports the SNR feature in Cisco Unified SIP 7906, 7911, 7941, 7942, 7945, 7961, 7962, 7965,
                              7970, 7971, 7975, 8961, 9951, and 9971 IP Phones.

Single Number Reach (SNR) support through MyPhoneApps on Unified CME is available for SIP Phones on the Cisco IP Phones 7800
                                          and 8800 Series.

### Virtual SNR DN for Cisco Unified SCCP IP Phones

A virtual SNR DN is a DN not associated with any registered phone. It
                              		can be called, forwarded to a preconfigured mobile phone, or put on an Auto
                              		Hold state when the mobile phone answers the call or the time delay is reached.
                              		In the Auto Hold state, the DN can either be floating or unregistered. A
                              		floating DN is a DN not configured for any phone while an unregistered DN is
                              		one associated with phones not registered to a Cisco Unified CME system.

Before Cisco Unified CME 9.0, an SNR DN feature did not launch when the
                              		SNR DN was not associated with any registered phone. Although a call could be
                              		forwarded to the mobile phone using the call-forward
                                    			 busy command, the SNR DN had to be configured under a phone.
                              		Users who were assigned floating DNs could not forward calls unless they had a
                              		phone assigned to them.

In Cisco Unified CME 9.0 and later versions, an SNR DN is not required
                              		to be associated with a registered phone to have the SNR DN feature launched. A
                              		call can be made to a virtual SNR DN and the SNR feature can be launched even
                              		when the SNR DN is not associated with any phone. A call to a virtual SNR DN
                              		can be forwarded to an auto-attendant service when the preconfigured mobile
                              		phone is out of service and the voice mail can be retrieved using the telephone
                              		or extension number assigned to the voice mailbox.

Although the virtual SNR DN feature is designed for SNR DNs that are not
                              		associated with registered phones, this feature also supports virtual SNR DNs
                              		that complete phone registration or login and registered DNs that become
                              		virtual when all associated registered phones become unregistered.

## Configure Single Number Reach

### Configure Single
                           	 Number Reach on SCCP Phones

Restriction

Each IP
                                                      				  phone supports only one SNR directory number.

SCCP-controlled analog FXS phones

MLPP
                                                               						calls

Secure
                                                               						calls

Video
                                                               						calls

Hunt
                                                               						group directory numbers (voice or ephone)

MWI
                                                               						directory numbers

Trunk
                                                               						directory numbers

An overlay
                                                      				  set can support only one SNR directory number and that directory number must be
                                                      				  the primary directory number.

Call forward
                                                      				  no answer (CFNA), configured with the call-forward
                                                            						noan command, is disabled if SNR is configured on the directory
                                                      				  number. To forward unanswered calls to voice mail, use the cfwd-noan keyword in the snr command.

Call
                                                      				  forwarding of unanswered calls, configured with the cfwd-noan keyword in the snr command,
                                                      				  is not supported for PSTN calls from FXO trunks because the calls connect
                                                      				  immediately.

Calls from
                                                      				  an internal extension to an extension which is busy, is forwarded to the SNR
                                                      				  destination even if no forward local-calls is configured
                                                      				  under the Directory Number.

Calls always
                                                      				  remain private. If a call is answered on a remote phone, the desktop IP phone
                                                      				  can not listen to the call unless it resumes the call.

U.S. English
                                                      				  is the only locale supported for SNR calls.

#### Before you begin

Cisco Unified
                                       				CME 7.1 or a later version

Cisco IP
                                       				Communicator requires version 2.1.4 or later

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn dn-tag

- number number

- mobility

- snr e164-number delay seconds timeout seconds [ cfwd-noan extension-number ]

- snr calling-number
                                       				  local

- exit

- ephone-template template-tag

- softkeys
                                       				  connected { [ Acct ] [ ConfList ] [ Confrn ] [ Endcall ] [ Flash ] [ HLog ] [ Hold ] [ Join ] [ LiveRcd ] [ Mobility ] [ Park ] [ RmLstC ] [ Select ] [ TrnsfVM ] [ Trnsfer ] }

- softkeys
                                       				  idle { [ Cfwdall ] [ ConfList ] [ Dnd ] [ Gpickup ] [ HLog ] [ Join ] [ Login ] [ Mobility ] [ Newcall ] [ Pickup ] [ Redial ] [ RmLstC ] }

- exit

- ephone phone-tag

- ephone-template template-tag

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
Router(config)# ephone-dn 10
```

Enters
                                             				directory number configuration mode.

Step 4

number number

#### Example:

```
Router(config-ephone-dn)# number 1001
```

Associates an
                                             				extension number with this directory number.

number —String of up to 16 digits that represents
                                                   					 an extension or E.164 telephone number.

Step 5

mobility

#### Example:

```
Router(config-ephone-dn)# mobility
```

Enables the
                                             				Mobility feature on the directory number.

Step 6

snr e164-number delay seconds timeout seconds [ cfwd-noan extension-number ]

#### Example:

```
Router(config-ephone-dn)# snr 4085550133 delay 5 timeout 15 cfwd-noan 2001
```

Enables SNR
                                             				on the extension.

e164-number —E.164 telephone number to ring if IP
                                                   					 phone extension does not answer.

delay seconds —Sets the number of seconds that the call
                                                   					 rings the IP phone before ringing the remote phone. Range is from  0 to 10.
                                                   					 Default: disabled.

timeout seconds —Sets the number of seconds that the call
                                                   					 rings after the configured delay. Call continues to ring for this length of
                                                   					 time on the IP phone even if the remote phone answers the call. Range is from
                                                   					  5 to 60. Default: disabled.

cfwd-noan extension-number —(Optional) Forwards the call to
                                                   					 this target number if the phone does not answer after both the delay and timeout seconds have expired. This is typically the voice-mail number.

The cfwd-noan option is not supported for calls from FXO trunks because the calls connect
                                                         				  immediately.

Step 7

snr calling-number
                                                				  local

#### Example:

```
Router(config-ephone-dn)# snr calling-number local
```

(Optional)
                                             				Replaces the original calling party number with the SNR extension number in the
                                             				caller ID display of the remote phone.

This
                                                   					 command is supported in Cisco Unified CME 8.0 and later versions.

Step 8

exit

#### Example:

```
Router(config-ephone-dn)# exit
```

Exits
                                             				ephone-dn configuration mode.

Step 9

ephone-template template-tag

#### Example:

```
Router(config)# ephone-template 1
```

Enters
                                             				ephone-template configuration mode to create an ephone template.

template-tag —Unique identifier for the ephone
                                                   					 template that is being created. Range is from 1 to 20.

Step 10

softkeys
                                                				  connected { [ Acct ] [ ConfList ] [ Confrn ] [ Endcall ] [ Flash ] [ HLog ] [ Hold ] [ Join ] [ LiveRcd ] [ Mobility ] [ Park ] [ RmLstC ] [ Select ] [ TrnsfVM ] [ Trnsfer ] }

#### Example:

```
Router(config-ephone-template)# softkeys connected endcall hold livercd mobility
```

Modifies the
                                             				order and type of softkeys that display on an IP phone during the connected
                                             				call state.

Pressing
                                                   					 the Mobility softkey during the connected call state forwards the call to the
                                                   					 PSTN number defined in Step 6.

Step 11

softkeys
                                                				  idle { [ Cfwdall ] [ ConfList ] [ Dnd ] [ Gpickup ] [ HLog ] [ Join ] [ Login ] [ Mobility ] [ Newcall ] [ Pickup ] [ Redial ] [ RmLstC ] }

#### Example:

```
Router(config-ephone-template)# softkeys idle dnd gpickup pickup mobility
```

Modifies the
                                             				order and type of softkeys that display on an IP phone during the idle call
                                             				state.

Pressing
                                                   					 the Mobility softkey during the idle call state enables the SNR feature. This
                                                   					 key is a toggle; pressing it a second time disables SNR.

Step 12

exit

#### Example:

```
Router(config-ephone-template)# exit
```

Exits
                                             				ephone-template configuration mode.

Step 13

ephone phone-tag

#### Example:

```
Router(config)# ephone 21
```

Enters
                                             				ephone configuration mode.

phone-tag —Unique number that identifies this
                                                   					 ephone during configuration tasks.

Step 14

ephone-template template-tag

#### Example:

```
Router(config-ephone)# ephone-template 1
```

Applies the
                                             				ephone template to the phone.

template-tag —Unique identifier of the ephone
                                                   					 template that you created in Step 12.

Step 15

end

#### Example:

```
Router(config-ephone-template)# end
```

Exits
                                             				configuration mode.

#### Example

The following
                                 		  example shows extension 1001 is enabled for SNR on IP phone 21. After a call
                                 		  rings at this number for 5 seconds, the call also rings at the remote number
                                 		  4085550133. The call continues ringing on both phones for 15 seconds. If the
                                 		  call is not answered after a total of 20 seconds, the call no longer rings and
                                 		  it is forwarded to the voice-mail number 2001.

```
ephone-template  1
 softkeys idle  Dnd Gpickup Pickup Mobility
 softkeys connected  Endcall Hold LiveRcd Mobility
!
ephone-dn 10
 number 1001
 mobility
 snr 4085550133 delay 5 timeout 15 cfwd-noan 2001
 snr calling-number local
!
!
ephone  21
 mac-address 02EA.EAEA.0001
 ephone-template 1
 button  1:10
```

### Configure Single
                           	 Number Reach Enhancements on SCCP Phones

Restriction

Software
                                                   				  Conference— After a software conference is initiated and committed on an
                                                   				  ephone, you cannot send the call to a mobile phone. You can only enable or
                                                   				  disable mobility after software conference is committed.

SNR Call
                                                   				  Pickup on FXO port— For a call routed through FXO port to the PSTN, the call is
                                                   				  signaled as “connected” as soon as FXO port is seized outbound. The mobile
                                                   				  phone is on FXO interface and the call (session) is in active state as soon as
                                                   				  FXO is in connect state. The ephone will be in ringing state but you can not
                                                   				  pick up the ephone call.

Music on
                                                   				  hold (MOH) is not supported if the SNR call originates from the line side. MOH
                                                   				  is supported on an SNR call if the call originates from the trunk side.

#### Before you begin

Cisco Unified CME
                                 		  8.5 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn dn-tag

- number number [ secondary number ] [ no-reg [ both | primary ] ]

- mobility

- snr calling number local

- snr answer too soon time

- snr ring-stop

- exit

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
Router(config)# ephone-dn 10
```

Enters
                                             				directory number configuration mode.

Step 4

number number [ secondary number ] [ no-reg [ both | primary ] ]

#### Example:

```
Router(config-ephone-dn)# number 1001
```

Associates an
                                             				extension number with this directory number.

number —String of up to 16 digits that represents
                                                   					 an extension or E.164 telephone number.

Step 5

mobility

#### Example:

```
Router(config-ephone-dn)# mobility
```

Enables the
                                             				Mobility feature on the directory number.

Step 6

snr calling number local

#### Example:

```
Router(config-ephone-dn)#snr calling-number local
```

Displays local
                                             				number as calling number on your SNR mobile phone.

Step 7

snr answer too soon time

#### Example:

```
Router(config-ephone-dn)#snr answer-too-soon 4
```

Enables a
                                             				timer for answering the call on SNR mobile phone.

time—Time,
                                                   					 in seconds. Range is from 1 to 5.

Step 8

snr ring-stop

#### Example:

```
Router(config-ephone-dn)#snr ring-stop
```

Allows you to
                                             				stop the IP phone from ringing after the SNR call is answered on a mobile
                                             				phone.

Step 9

exit

#### Example:

```
Router(config-ephone-dn)# exit
```

Exits
                                             				ephone-dn configuration mode.

#### Example

The following
                                 		  example shows SNR enhancements configured for ephone-dn 10:

```
Router#show running config
 !
 !
 telephony-service
  sdspfarm units 1
  sdspfarm tag 1 confprof1
  conference hardware
  max-ephones 262
  max-dn 720
  ip source-address 172.19.153.114 port 2000
  service phone thumbButton PTTH6
  load 7906 SCCP11.8-5-3S.loads
  load 7911 SCCP11.8-5-3S.loads
 !
 ephone-template  6
  feature-button 1 Hold
 !
 !
 ephone-dn  10
  mobility snr calling-number local snr ring-stop snr answer-too-soon 4
```

### Configure Single
                           	 Number Reach on SIP Phones

Restriction

Hardware
                                                   				  Conferencing and Privacy on Hold for Cisco Unified SIP IP phones are not
                                                   				  supported.

Mixed shared
                                                   				  lines between Cisco Unified SIP and SCCP IP phones are not supported.

Subscribe
                                                   				  and Notify modes for SIP shared lines are not supported.

Incoming
                                                   				  calls from the H323 IP trunk are not supported.

Media flow
                                                   				  around for SIP-SIP trunk calls is not supported.

SIP SNR
                                                   				  phones that initiate software conferencing are unable to send or receive calls
                                                   				  to or from mobile phones because the Cisco Unified SIP IP phones are put on
                                                   				  hold after a software conference is committed.

#### Before you begin

Cisco Unified CME
                                 		  9.0 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice register template template-tag

- softkeys idle { [ Cfwdall ] [ DND ] [ Gpickup ] [ Newcall ] [ Pickup ] [ Redial ] }

- softkeys
                                       				  connected { [ Confrn ] [ Endcall ] [ Hold ] [ Park ] [ Trnsfer ] [ iDivert ] }

- exit

- voice register pool pool-tag

- session-transport { tcp }

- exit

- voice register
                                       				  dn dn-tag

- number number

- name name

- mobility

- snr calling-number
                                       				  local

- snr e164-number delay seconds timeout seconds [ cfwd-noan extension-number ]

- snr
                                       				  ring-stop

- snr
                                       				  answer-too-soon time

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
Router(config)# voice register template 1
```

Enters voice
                                             				register template configuration mode.

template-tag —identifier for the template being
                                                   					 created. Range: 1 to 10.

Step 4

softkeys idle { [ Cfwdall ] [ DND ] [ Gpickup ] [ Newcall ] [ Pickup ] [ Redial ] }

#### Example:

```
Router(config-register-temp)# softkeys idle Redial Cfwdall
```

Modifies the
                                             				display of softkeys on Cisco Unified SIP IP phones during the idle call state.

Cfwdall —(Optional) Softkey for “call forward all.”
                                                   					 Forwards all calls.

DND —(Optional) Softkey that enables the
                                                   					 Do-Not-Disturb feature.

Gpickup —(Optional) Softkey that allows a user to
                                                   					 pickup a call that is ringing on another phone.

Newcall —(Optional) Softkey that opens a line on a
                                                   					 speakerphone to place a new call.

Pickup —(Optional) Softkey that allows a user to
                                                   					 pickup a call that is ringing on another phone that is a member of the same
                                                   					 pickup group.

Redial —(Optional) Softkey that redials the last
                                                   					 number dialed.

Step 5

softkeys
                                                				  connected { [ Confrn ] [ Endcall ] [ Hold ] [ Park ] [ Trnsfer ] [ iDivert ] }

#### Example:

```
Router(config-register-temp)# softkeys connected Confrn Hold Endcall
```

Modifies the
                                             				display of softkeys on Cisco Unified SIP IP phones during the connected call
                                             				state.

Confrn —(Optional) Softkey that connects callers to
                                                   					 a conference call.

Endcall —(Optional) Softkey that ends the current
                                                   					 call.

Hold —(Optional) Softkey that places an active call
                                                   					 on hold and resumes the call.

Park —(Optional) Softkey that places an active call
                                                   					 on hold, so it can be retrieved from another phone in the system.

Trnsfer —(Optional) Softkey that transfers active
                                                   					 calls to another extension.

iDivert —(Optional) Softkey that immediately
                                                   					 diverts a call to a voice-messaging system.

Step 6

exit

#### Example:

```
Router(config-register-temp)# exit
```

Exits voice
                                             				register template configuration mode.

Step 7

voice register pool pool-tag

#### Example:

```
Router(config)# voice register pool 10
```

Enters voice
                                             				register pool configuration mode.

pool-tag —Unique number assigned to the pool.
                                                   					 Range: 1 to 100.

For Cisco
                                                         				  Unified CME systems, the upper limit for this argument is defined by the max-pool command.

Step 8

session-transport { tcp }

#### Example:

```
Router(config-register-pool)# session-transport tcp
```

Specifies
                                             				the transport layer protocol that a Cisco Unified SIP IP phone uses to connect
                                             				to Cisco Unified CME.

tcp —Transmission Control Protocol (TCP) is used.

Step 9

exit

#### Example:

```
Router(config-register-pool)# exit
```

Exits voice
                                             				register pool configuration mode.

Step 10

voice register
                                                				  dn dn-tag

#### Example:

```
Router(config)# voice register dn  3
```

Enters voice
                                             				register dn configuration mode.

dn-tag —Unique sequence number that identifies a
                                                   					 particular directory number during configuration tasks. Range is 1 to 150 or
                                                   					 the maximum defined by the max-dn command.

Step 11

number number

#### Example:

```
Router(config-register-dn)# number 1004
```

Associates a
                                             				telephone or extension number with a Cisco Unified SIP IP phone in a Cisco
                                             				Unified CME system.

number —String of up to 16 characters that
                                                   					 represents an E.164 telephone number. Normally, the string is composed of
                                                   					 digits, but the string may contain alphabetic characters when the number is
                                                   					 dialed only by the router, as with an intercom number.

Step 12

name name

#### Example:

```
Router(config-register-dn)# name John Smith
```

Associates a
                                             				name with a directory number in Cisco Unified CME.

name —Name
                                                   					 of the person associated with a given extension. Name must follow the order
                                                   					 specified in the directory (telephony-service) command, either first-name-first or last-name-first .

Step 13

mobility

#### Example:

```
Router(config-register-dn)# mobility
```

Enables the
                                             				Mobility feature on an extension of a Cisco Unified SIP IP phone.

Step 14

snr calling-number
                                                				  local

#### Example:

```
Router(config-register-dn)# snr calling-number local
```

Replaces the
                                             				calling party number displayed on the configured mobile phone with the local
                                             				SNR number.

Step 15

snr e164-number delay seconds timeout seconds [ cfwd-noan extension-number ]

#### Example:

```
Router(config-register-dn)# snr 9900 delay 1 timeout 10
```

Enables the
                                             				SNR feature on an extension of a Cisco Unified SIP IP phone.

e164-number —E.164 telephone number to call when
                                                   					 the Cisco Unified SIP IP phone extension does not answer.

delay seconds —Sets the number of seconds that the Cisco
                                                   					 Unified SIP IP phone rings when called. When the time delay is reached, the
                                                   					 call is transferred to the PSTN phone and the SNR directory number. Range: 0 to
                                                   					 30. Default: 5.

timeout seconds —Sets the number of seconds that the Cisco
                                                   					 Unified SIP IP phone rings after the configured time delay. When the timeout
                                                   					 value is reached, no call is displayed on the phone. You have to use the Resume
                                                   					 softkey to pull back or the Mobility softkey to send the call to a mobile
                                                   					 phone. Range: 30 to 60. Default: 60.

When the
                                                         				  default is enabled, the Cisco Unified SIP IP phone continues to ring for 60
                                                         				  seconds even if the remote phone answers the call.

cfwd-noan extension-number —(Optional) Forwards the call to
                                                   					 the extension number when the phone does not answer after both the time delay
                                                   					 and timeout values are reached. The extension number is typically the voice
                                                   					 mail number.

This
                                                         				  option is not supported for calls from FXO trunks because the calls connect
                                                         				  immediately.

Step 16

snr
                                                				  ring-stop

#### Example:

```
Router(config-register-dn)# snr ring-stop
```

Ends the
                                             				ringing on a Cisco Unified SIP IP phone after the SNR call is answered on the
                                             				configured mobile phone.

Step 17

snr
                                                				  answer-too-soon time

#### Example:

```
Router(config-register-dn)# snr answer-too-soon 2
```

Sets the
                                             				time in which SNR calls are prevented from being diverted to the voice mailbox
                                             				of a mobile phone.

time —Time,
                                                   					 in seconds. Range: 1 to 5.

Step 18

end

#### Example:

```
Router(config-register-dn)# end
```

Exits voice
                                             				register dn configuration mode and enters privileged EXEC mode.

### Configure a
                           	 Virtual SNR DN on SCCP Phones

Restriction

Virtual SNR
                                                   				  DN only supports Cisco Unified SCCP IP phone DNs.

Virtual SNR
                                                   				  DN provides no mid-call support.

Mid-calls
                                                   				  are either of the following:

Calls
                                                         						that arrive before the DN is associated with a registered phone and is still
                                                         						present after the DN is associated with the phone.

Calls
                                                         						that arrive for a registered DN that changes state from registered to virtual
                                                         						and back to registered.

Mid-calls
                                                   				  cannot be pulled back, answered, or terminated from the phone associated with
                                                   				  the DN.

State of the
                                                   				  virtual DN transitions from ringing to hold or remains on hold as a registered
                                                   				  DN.

#### Before you begin

Cisco Unified CME
                                 		  9.0 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn dn-tag

- number number

- mobility

- snr mode [ virtual ]

- snr e164-number delay seconds timeout seconds [ cfwd-noan extension-number ]

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
Router(config)# ephone-dn 10
```

Enters
                                             				ephone-dn configuration mode to configure a directory number for an IP phone
                                             				line.

dn-tag —Unique number that identifies an ephone-dn
                                                   					 during configuration tasks. Range is 1 to the number set by the max-dn command.

Step 4

number number

#### Example:

```
Router(config-ephone-dn)# number 1001
```

Associates a
                                             				telephone or extension number with this ephone-dn.

number —String of up to 16 characters that
                                                   					 represents an E.164 telephone number. Normally, the string is composed of
                                                   					 digits, but the string may contain alphabetic characters when the number is
                                                   					 dialed only by the router, as with an intercom number.

Step 5

mobility

#### Example:

```
Router(config-ephone-dn)# mobility
```

Enables the
                                             				Mobility feature on an extension of a Cisco Unified SCCP IP phone.

Step 6

snr mode [ virtual ]

#### Example:

```
Router(config-ephone-dn)# snr mode virtual
```

Sets the mode
                                             				for the SNR directory number.

virtual —Enables the virtual mode for an SNR DN
                                                   					 when it is unregistered or floating.

Step 7

snr e164-number delay seconds timeout seconds [ cfwd-noan extension-number ]

#### Example:

```
Router(config-ephone-dn)# snr 408550133 delay 5 timeout 15 cfwd-noan 2001
```

Enables the
                                             				Single Number Reach feature on the extension of a Cisco Unified SCCP IP phone.

e164-number —E.164 telephone number to ring if IP
                                                   					 phone extension does not answer.

delay seconds —Sets the number of seconds that the call
                                                   					 rings the IP phone before ringing the remote phone. Range: 0 to 10. Default:
                                                   					 disabled.

timeout seconds —Sets the number of seconds that the call
                                                   					 rings after the configured delay. Call continues to ring for this length of
                                                   					 time on the IP phone even if the remote phone answers the call. Range: 5 to 60.
                                                   					 Default: disabled.

cfwd-noan extension-number —(Optional) Forwards the call to
                                                   					 this target number if the phone does not answer after both the delay and
                                                   					 timeout seconds have expired. This is typically the voice mail number.

Step 8

end

#### Example:

```
Router(config-ephone-dn)# end
```

Exits to
                                             				privileged EXEC mode.

## Feature
                        	 Information for Single Number Reach

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature
                                             					 Name

Cisco Unified CME Version

Modification

Single
                                             					 Number Reach for Cisco Unified SIP IP Phones

9.0

Supports
                                             					 the following SNR features for Cisco Unified SIP IP phones:

Enable
                                                   						  and disable the EM feature.

Manual
                                                   						  pull back of a call on a mobile phone.

Send a
                                                   						  call to a mobile PSTN phone.

Send a
                                                   						  call to a mobile phone regardless of whether the SNR phone is the originating
                                                   						  or the terminating side.

Virtual
                                             					 SNR DN for Cisco Unified SCCP IP Phones

Allows a
                                             					 call to be made to a virtual SNR DN and allows the SNR feature to be launched
                                             					 even when the SNR DN is not associated with any phone.

SNR
                                             					 Enhancements

8.5

Added
                                             					 support for the following SNR enhancements:

Hardware Conference

Call
                                                   						  Park, Call Pickup, and Call Retrieval

Answer
                                                   						  Too Soon Timer

SNR
                                                   						  Phone Stops Ringing After Mobile Phone Answers

Calling
                                             					 Number Local

8.0

Added the snr calling-number
                                                   						  local command to replace the calling party number with the SNR
                                             					 extension in the caller ID display.

Single
                                             					 Number Reach

7.1

Introduced
                                             					 the SNR feature.

| Note | When the Resume softkey is pressed, the call is returned to the SNR
                                       		phone. |
|---|---|

| Note | Single Number Reach (SNR) support through MyPhoneApps on Unified CME is available for SIP Phones on the Cisco IP Phones 7800
                                          and 8800 Series. |
|---|---|

| Restriction | Each IP
                                                      				  phone supports only one SNR directory number. SNR feature
                                                      				  is not supported for the following: SCCP-controlled analog FXS phones MLPP
                                                               						calls Secure
                                                               						calls Video
                                                               						calls Hunt
                                                               						group directory numbers (voice or ephone) MWI
                                                               						directory numbers Trunk
                                                               						directory numbers An overlay
                                                      				  set can support only one SNR directory number and that directory number must be
                                                      				  the primary directory number. Call forward
                                                      				  no answer (CFNA), configured with the call-forward
                                                            						noan command, is disabled if SNR is configured on the directory
                                                      				  number. To forward unanswered calls to voice mail, use the cfwd-noan keyword in the snr command. Call
                                                      				  forwarding of unanswered calls, configured with the cfwd-noan keyword in the snr command,
                                                      				  is not supported for PSTN calls from FXO trunks because the calls connect
                                                      				  immediately. Calls from
                                                      				  an internal extension to an extension which is busy, is forwarded to the SNR
                                                      				  destination even if no forward local-calls is configured
                                                      				  under the Directory Number. Calls always
                                                      				  remain private. If a call is answered on a remote phone, the desktop IP phone
                                                      				  can not listen to the call unless it resumes the call. U.S. English
                                                      				  is the only locale supported for SNR calls. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-dn dn-tag Example: Router(config)# ephone-dn 10 | Enters
                                             				directory number configuration mode. |
| Step 4 | number number Example: Router(config-ephone-dn)# number 1001 | Associates an
                                             				extension number with this directory number. number —String of up to 16 digits that represents
                                                   					 an extension or E.164 telephone number. |
| Step 5 | mobility Example: Router(config-ephone-dn)# mobility | Enables the
                                             				Mobility feature on the directory number. |
| Step 6 | snr e164-number delay seconds timeout seconds [ cfwd-noan extension-number ] Example: Router(config-ephone-dn)# snr 4085550133 delay 5 timeout 15 cfwd-noan 2001 | Enables SNR
                                             				on the extension. e164-number —E.164 telephone number to ring if IP
                                                   					 phone extension does not answer. delay seconds —Sets the number of seconds that the call
                                                   					 rings the IP phone before ringing the remote phone. Range is from  0 to 10.
                                                   					 Default: disabled. timeout seconds —Sets the number of seconds that the call
                                                   					 rings after the configured delay. Call continues to ring for this length of
                                                   					 time on the IP phone even if the remote phone answers the call. Range is from
                                                   					  5 to 60. Default: disabled. cfwd-noan extension-number —(Optional) Forwards the call to
                                                   					 this target number if the phone does not answer after both the delay and timeout seconds have expired. This is typically the voice-mail number. Note The cfwd-noan option is not supported for calls from FXO trunks because the calls connect
                                                         				  immediately. | Note | The cfwd-noan option is not supported for calls from FXO trunks because the calls connect
                                                         				  immediately. |
| Note | The cfwd-noan option is not supported for calls from FXO trunks because the calls connect
                                                         				  immediately. |
| Step 7 | snr calling-number
                                                				  local Example: Router(config-ephone-dn)# snr calling-number local | (Optional)
                                             				Replaces the original calling party number with the SNR extension number in the
                                             				caller ID display of the remote phone. This
                                                   					 command is supported in Cisco Unified CME 8.0 and later versions. |
| Step 8 | exit Example: Router(config-ephone-dn)# exit | Exits
                                             				ephone-dn configuration mode. |
| Step 9 | ephone-template template-tag Example: Router(config)# ephone-template 1 | Enters
                                             				ephone-template configuration mode to create an ephone template. template-tag —Unique identifier for the ephone
                                                   					 template that is being created. Range is from 1 to 20. |
| Step 10 | softkeys
                                                				  connected { [ Acct ] [ ConfList ] [ Confrn ] [ Endcall ] [ Flash ] [ HLog ] [ Hold ] [ Join ] [ LiveRcd ] [ Mobility ] [ Park ] [ RmLstC ] [ Select ] [ TrnsfVM ] [ Trnsfer ] } Example: Router(config-ephone-template)# softkeys connected endcall hold livercd mobility | Modifies the
                                             				order and type of softkeys that display on an IP phone during the connected
                                             				call state. Pressing
                                                   					 the Mobility softkey during the connected call state forwards the call to the
                                                   					 PSTN number defined in Step 6. |
| Step 11 | softkeys
                                                				  idle { [ Cfwdall ] [ ConfList ] [ Dnd ] [ Gpickup ] [ HLog ] [ Join ] [ Login ] [ Mobility ] [ Newcall ] [ Pickup ] [ Redial ] [ RmLstC ] } Example: Router(config-ephone-template)# softkeys idle dnd gpickup pickup mobility | Modifies the
                                             				order and type of softkeys that display on an IP phone during the idle call
                                             				state. Pressing
                                                   					 the Mobility softkey during the idle call state enables the SNR feature. This
                                                   					 key is a toggle; pressing it a second time disables SNR. |
| Step 12 | exit Example: Router(config-ephone-template)# exit | Exits
                                             				ephone-template configuration mode. |
| Step 13 | ephone phone-tag Example: Router(config)# ephone 21 | Enters
                                             				ephone configuration mode. phone-tag —Unique number that identifies this
                                                   					 ephone during configuration tasks. |
| Step 14 | ephone-template template-tag Example: Router(config-ephone)# ephone-template 1 | Applies the
                                             				ephone template to the phone. template-tag —Unique identifier of the ephone
                                                   					 template that you created in Step 12. |
| Step 15 | end Example: Router(config-ephone-template)# end | Exits
                                             				configuration mode. |

| Note | The cfwd-noan option is not supported for calls from FXO trunks because the calls connect
                                                         				  immediately. |
|---|---|

| Restriction | Software
                                                   				  Conference— After a software conference is initiated and committed on an
                                                   				  ephone, you cannot send the call to a mobile phone. You can only enable or
                                                   				  disable mobility after software conference is committed. SNR Call
                                                   				  Pickup on FXO port— For a call routed through FXO port to the PSTN, the call is
                                                   				  signaled as “connected” as soon as FXO port is seized outbound. The mobile
                                                   				  phone is on FXO interface and the call (session) is in active state as soon as
                                                   				  FXO is in connect state. The ephone will be in ringing state but you can not
                                                   				  pick up the ephone call. Music on
                                                   				  hold (MOH) is not supported if the SNR call originates from the line side. MOH
                                                   				  is supported on an SNR call if the call originates from the trunk side. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-dn dn-tag Example: Router(config)# ephone-dn 10 | Enters
                                             				directory number configuration mode. |
| Step 4 | number number [ secondary number ] [ no-reg [ both \| primary ] ] Example: Router(config-ephone-dn)# number 1001 | Associates an
                                             				extension number with this directory number. number —String of up to 16 digits that represents
                                                   					 an extension or E.164 telephone number. |
| Step 5 | mobility Example: Router(config-ephone-dn)# mobility | Enables the
                                             				Mobility feature on the directory number. |
| Step 6 | snr calling number local Example: Router(config-ephone-dn)#snr calling-number local | Displays local
                                             				number as calling number on your SNR mobile phone. |
| Step 7 | snr answer too soon time Example: Router(config-ephone-dn)#snr answer-too-soon 4 | Enables a
                                             				timer for answering the call on SNR mobile phone. time—Time,
                                                   					 in seconds. Range is from 1 to 5. |
| Step 8 | snr ring-stop Example: Router(config-ephone-dn)#snr ring-stop | Allows you to
                                             				stop the IP phone from ringing after the SNR call is answered on a mobile
                                             				phone. |
| Step 9 | exit Example: Router(config-ephone-dn)# exit | Exits
                                             				ephone-dn configuration mode. |

| Restriction | Hardware
                                                   				  Conferencing and Privacy on Hold for Cisco Unified SIP IP phones are not
                                                   				  supported. Mixed shared
                                                   				  lines between Cisco Unified SIP and SCCP IP phones are not supported. Subscribe
                                                   				  and Notify modes for SIP shared lines are not supported. Incoming
                                                   				  calls from the H323 IP trunk are not supported. Media flow
                                                   				  around for SIP-SIP trunk calls is not supported. SIP SNR
                                                   				  phones that initiate software conferencing are unable to send or receive calls
                                                   				  to or from mobile phones because the Cisco Unified SIP IP phones are put on
                                                   				  hold after a software conference is committed. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register template template-tag Example: Router(config)# voice register template 1 | Enters voice
                                             				register template configuration mode. template-tag —identifier for the template being
                                                   					 created. Range: 1 to 10. |
| Step 4 | softkeys idle { [ Cfwdall ] [ DND ] [ Gpickup ] [ Newcall ] [ Pickup ] [ Redial ] } Example: Router(config-register-temp)# softkeys idle Redial Cfwdall | Modifies the
                                             				display of softkeys on Cisco Unified SIP IP phones during the idle call state. Cfwdall —(Optional) Softkey for “call forward all.”
                                                   					 Forwards all calls. DND —(Optional) Softkey that enables the
                                                   					 Do-Not-Disturb feature. Gpickup —(Optional) Softkey that allows a user to
                                                   					 pickup a call that is ringing on another phone. Newcall —(Optional) Softkey that opens a line on a
                                                   					 speakerphone to place a new call. Pickup —(Optional) Softkey that allows a user to
                                                   					 pickup a call that is ringing on another phone that is a member of the same
                                                   					 pickup group. Redial —(Optional) Softkey that redials the last
                                                   					 number dialed. |
| Step 5 | softkeys
                                                				  connected { [ Confrn ] [ Endcall ] [ Hold ] [ Park ] [ Trnsfer ] [ iDivert ] } Example: Router(config-register-temp)# softkeys connected Confrn Hold Endcall | Modifies the
                                             				display of softkeys on Cisco Unified SIP IP phones during the connected call
                                             				state. Confrn —(Optional) Softkey that connects callers to
                                                   					 a conference call. Endcall —(Optional) Softkey that ends the current
                                                   					 call. Hold —(Optional) Softkey that places an active call
                                                   					 on hold and resumes the call. Park —(Optional) Softkey that places an active call
                                                   					 on hold, so it can be retrieved from another phone in the system. Trnsfer —(Optional) Softkey that transfers active
                                                   					 calls to another extension. iDivert —(Optional) Softkey that immediately
                                                   					 diverts a call to a voice-messaging system. |
| Step 6 | exit Example: Router(config-register-temp)# exit | Exits voice
                                             				register template configuration mode. |
| Step 7 | voice register pool pool-tag Example: Router(config)# voice register pool 10 | Enters voice
                                             				register pool configuration mode. pool-tag —Unique number assigned to the pool.
                                                   					 Range: 1 to 100. Note For Cisco
                                                         				  Unified CME systems, the upper limit for this argument is defined by the max-pool command. | Note | For Cisco
                                                         				  Unified CME systems, the upper limit for this argument is defined by the max-pool command. |
| Note | For Cisco
                                                         				  Unified CME systems, the upper limit for this argument is defined by the max-pool command. |
| Step 8 | session-transport { tcp } Example: Router(config-register-pool)# session-transport tcp | Specifies
                                             				the transport layer protocol that a Cisco Unified SIP IP phone uses to connect
                                             				to Cisco Unified CME. tcp —Transmission Control Protocol (TCP) is used. |
| Step 9 | exit Example: Router(config-register-pool)# exit | Exits voice
                                             				register pool configuration mode. |
| Step 10 | voice register
                                                				  dn dn-tag Example: Router(config)# voice register dn  3 | Enters voice
                                             				register dn configuration mode. dn-tag —Unique sequence number that identifies a
                                                   					 particular directory number during configuration tasks. Range is 1 to 150 or
                                                   					 the maximum defined by the max-dn command. |
| Step 11 | number number Example: Router(config-register-dn)# number 1004 | Associates a
                                             				telephone or extension number with a Cisco Unified SIP IP phone in a Cisco
                                             				Unified CME system. number —String of up to 16 characters that
                                                   					 represents an E.164 telephone number. Normally, the string is composed of
                                                   					 digits, but the string may contain alphabetic characters when the number is
                                                   					 dialed only by the router, as with an intercom number. |
| Step 12 | name name Example: Router(config-register-dn)# name John Smith | Associates a
                                             				name with a directory number in Cisco Unified CME. name —Name
                                                   					 of the person associated with a given extension. Name must follow the order
                                                   					 specified in the directory (telephony-service) command, either first-name-first or last-name-first . |
| Step 13 | mobility Example: Router(config-register-dn)# mobility | Enables the
                                             				Mobility feature on an extension of a Cisco Unified SIP IP phone. |
| Step 14 | snr calling-number
                                                				  local Example: Router(config-register-dn)# snr calling-number local | Replaces the
                                             				calling party number displayed on the configured mobile phone with the local
                                             				SNR number. |
| Step 15 | snr e164-number delay seconds timeout seconds [ cfwd-noan extension-number ] Example: Router(config-register-dn)# snr 9900 delay 1 timeout 10 | Enables the
                                             				SNR feature on an extension of a Cisco Unified SIP IP phone. e164-number —E.164 telephone number to call when
                                                   					 the Cisco Unified SIP IP phone extension does not answer. delay seconds —Sets the number of seconds that the Cisco
                                                   					 Unified SIP IP phone rings when called. When the time delay is reached, the
                                                   					 call is transferred to the PSTN phone and the SNR directory number. Range: 0 to
                                                   					 30. Default: 5. timeout seconds —Sets the number of seconds that the Cisco
                                                   					 Unified SIP IP phone rings after the configured time delay. When the timeout
                                                   					 value is reached, no call is displayed on the phone. You have to use the Resume
                                                   					 softkey to pull back or the Mobility softkey to send the call to a mobile
                                                   					 phone. Range: 30 to 60. Default: 60. Note When the
                                                         				  default is enabled, the Cisco Unified SIP IP phone continues to ring for 60
                                                         				  seconds even if the remote phone answers the call. cfwd-noan extension-number —(Optional) Forwards the call to
                                                   					 the extension number when the phone does not answer after both the time delay
                                                   					 and timeout values are reached. The extension number is typically the voice
                                                   					 mail number. Note This
                                                         				  option is not supported for calls from FXO trunks because the calls connect
                                                         				  immediately. | Note | When the
                                                         				  default is enabled, the Cisco Unified SIP IP phone continues to ring for 60
                                                         				  seconds even if the remote phone answers the call. | Note | This
                                                         				  option is not supported for calls from FXO trunks because the calls connect
                                                         				  immediately. |
| Note | When the
                                                         				  default is enabled, the Cisco Unified SIP IP phone continues to ring for 60
                                                         				  seconds even if the remote phone answers the call. |
| Note | This
                                                         				  option is not supported for calls from FXO trunks because the calls connect
                                                         				  immediately. |
| Step 16 | snr
                                                				  ring-stop Example: Router(config-register-dn)# snr ring-stop | Ends the
                                             				ringing on a Cisco Unified SIP IP phone after the SNR call is answered on the
                                             				configured mobile phone. |
| Step 17 | snr
                                                				  answer-too-soon time Example: Router(config-register-dn)# snr answer-too-soon 2 | Sets the
                                             				time in which SNR calls are prevented from being diverted to the voice mailbox
                                             				of a mobile phone. time —Time,
                                                   					 in seconds. Range: 1 to 5. |
| Step 18 | end Example: Router(config-register-dn)# end | Exits voice
                                             				register dn configuration mode and enters privileged EXEC mode. |

| Note | For Cisco
                                                         				  Unified CME systems, the upper limit for this argument is defined by the max-pool command. |
|---|---|

| Note | When the
                                                         				  default is enabled, the Cisco Unified SIP IP phone continues to ring for 60
                                                         				  seconds even if the remote phone answers the call. |
|---|---|

| Note | This
                                                         				  option is not supported for calls from FXO trunks because the calls connect
                                                         				  immediately. |
|---|---|

| Restriction | Virtual SNR
                                                   				  DN only supports Cisco Unified SCCP IP phone DNs. Virtual SNR
                                                   				  DN provides no mid-call support. Mid-calls
                                                   				  are either of the following: Calls
                                                         						that arrive before the DN is associated with a registered phone and is still
                                                         						present after the DN is associated with the phone. Calls
                                                         						that arrive for a registered DN that changes state from registered to virtual
                                                         						and back to registered. Mid-calls
                                                   				  cannot be pulled back, answered, or terminated from the phone associated with
                                                   				  the DN. State of the
                                                   				  virtual DN transitions from ringing to hold or remains on hold as a registered
                                                   				  DN. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-dn dn-tag Example: Router(config)# ephone-dn 10 | Enters
                                             				ephone-dn configuration mode to configure a directory number for an IP phone
                                             				line. dn-tag —Unique number that identifies an ephone-dn
                                                   					 during configuration tasks. Range is 1 to the number set by the max-dn command. |
| Step 4 | number number Example: Router(config-ephone-dn)# number 1001 | Associates a
                                             				telephone or extension number with this ephone-dn. number —String of up to 16 characters that
                                                   					 represents an E.164 telephone number. Normally, the string is composed of
                                                   					 digits, but the string may contain alphabetic characters when the number is
                                                   					 dialed only by the router, as with an intercom number. |
| Step 5 | mobility Example: Router(config-ephone-dn)# mobility | Enables the
                                             				Mobility feature on an extension of a Cisco Unified SCCP IP phone. |
| Step 6 | snr mode [ virtual ] Example: Router(config-ephone-dn)# snr mode virtual | Sets the mode
                                             				for the SNR directory number. virtual —Enables the virtual mode for an SNR DN
                                                   					 when it is unregistered or floating. |
| Step 7 | snr e164-number delay seconds timeout seconds [ cfwd-noan extension-number ] Example: Router(config-ephone-dn)# snr 408550133 delay 5 timeout 15 cfwd-noan 2001 | Enables the
                                             				Single Number Reach feature on the extension of a Cisco Unified SCCP IP phone. e164-number —E.164 telephone number to ring if IP
                                                   					 phone extension does not answer. delay seconds —Sets the number of seconds that the call
                                                   					 rings the IP phone before ringing the remote phone. Range: 0 to 10. Default:
                                                   					 disabled. timeout seconds —Sets the number of seconds that the call
                                                   					 rings after the configured delay. Call continues to ring for this length of
                                                   					 time on the IP phone even if the remote phone answers the call. Range: 5 to 60.
                                                   					 Default: disabled. cfwd-noan extension-number —(Optional) Forwards the call to
                                                   					 this target number if the phone does not answer after both the delay and
                                                   					 timeout seconds have expired. This is typically the voice mail number. |
| Step 8 | end Example: Router(config-ephone-dn)# end | Exits to
                                             				privileged EXEC mode. |

| Feature
                                             					 Name | Cisco Unified CME Version | Modification |
|---|---|---|
| Single
                                             					 Number Reach for Cisco Unified SIP IP Phones | 9.0 | Supports
                                             					 the following SNR features for Cisco Unified SIP IP phones: Enable
                                                   						  and disable the EM feature. Manual
                                                   						  pull back of a call on a mobile phone. Send a
                                                   						  call to a mobile PSTN phone. Send a
                                                   						  call to a mobile phone regardless of whether the SNR phone is the originating
                                                   						  or the terminating side. |
| Virtual
                                             					 SNR DN for Cisco Unified SCCP IP Phones | Allows a
                                             					 call to be made to a virtual SNR DN and allows the SNR feature to be launched
                                             					 even when the SNR DN is not associated with any phone. |
| SNR
                                             					 Enhancements | 8.5 | Added
                                             					 support for the following SNR enhancements: Hardware Conference Call
                                                   						  Park, Call Pickup, and Call Retrieval Answer
                                                   						  Too Soon Timer SNR
                                                   						  Phone Stops Ringing After Mobile Phone Answers |
| Calling
                                             					 Number Local | 8.0 | Added the snr calling-number
                                                   						  local command to replace the calling party number with the SNR
                                             					 extension in the caller ID display. |
| Single
                                             					 Number Reach | 7.1 | Introduced
                                             					 the SNR feature. |