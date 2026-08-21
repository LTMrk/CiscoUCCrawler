---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmevmail-html-69cbb5a620
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmevmail.html
retrieved_at: 2026-08-21T07:22:59.106249+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Voice Mail Integration

## Chapter: Voice Mail Integration

# Voice Mail Integration

This chapter describes how to integrate your voice-mail system with
                        		Cisco Unified Communications Manager Express (Cisco Unified CME).

## Prerequisites for
                        	 Voice Mail Integration

Calls can be
                                 			 successfully completed between phones on the same Cisco Unified CME router.

If your
                                 			 voice-mail system is something other than Cisco Unity Express, such as
                                 			 Cisco Unity, voice mail must be installed and configured on your network.

If your
                                 			 voice-mail system is Cisco Unity Express:

When you order
                                             				Cisco Unity Express, Cisco Unity Express software and the purchased license are
                                             				installed on the module at the factory. Spare modules also ship with the
                                             				software and license installed. If you are adding Cisco Unity Express to an
                                             				existing Cisco router, you will be required to install hardware and software
                                             				components.

Interface
                                       				  module for Cisco Unity Express is installed. For information about the AIM-CUE
                                       				  or NM-CUE, access documents located at http://www.cisco.com/en/US/products/hw/modules/ps2797/prod_installation_guides_list.html .

The recommended Cisco IOS release and feature set plus the necessary Cisco Unified CME phone firmware files to support Cisco
                                       Unity Express are installed on the Cisco Unified CME router.

To determine
                                       				  whether the Cisco IOS software release and Cisco Unified CME software version
                                       				  are compatible with the Cisco Unity Express version, Cisco router model, and
                                       				  Cisco Unity Express hardware that you are using, see Cisco Unity Express
                                          					 Compatibility Matrix .

To verify
                                       				  installed Cisco Unity Express software version, enter the Cisco Unity Express
                                       				  command environment and use the show software
                                             						version user EXEC command. For information about the command
                                       				  environment, see the appropriate Cisco
                                          					 Unity Express CLI Administrator Guide at http://www.cisco.com/en/US/docs/voice_ip_comm/unity_exp/roadmap/cuedocs.html .

The proper
                                       				  license for Cisco Unified CME, not Cisco Unified Communications Manager, is
                                       				  installed. To verify installed license, enter the Cisco Unity Express command
                                       				  environment and use the show software
                                             						license user EXEC command. For information about the command
                                       				  environment, see the appropriate Cisco
                                          					 Unity Express CLI Administrator Guide at http://www.cisco.com/en/US/docs/voice_ip_comm/unity_exp/roadmap/cuedocs.html .

This is an
                                       				  example of the Cisco Unified CME license:

```
se-10-0-0-0> show software licenses Core:
- application mode: CCME
- total usable system ports: 8
 
Voicemail/Auto Attendant:
- max system mailbox capacity time: 6000
- max general delivery mailboxes: 15
- max personal mailboxes: 50
 
Languages:
- max installed languages: 1
- max enabled languages: 1
```

Voicemail
                                       				  and Auto Attendant (AA) applications are configured. For configuration
                                       				  information, see “Configuring the System Using the Initialization Wizard” in the appropriate Cisco Unity Express GUI Administrator Guide at http://www.cisco.com/en/US/docs/voice_ip_comm/unity_exp/roadmap/cuedocs.html .

## Information About Voice-Mail Integration

### Cisco Unity Connection Integration

Cisco Unity Connection transparently integrates messaging and
                              		voice recognition components with your data network to provide continuous
                              		global access to calls and messages. These advanced, convergence-based
                              		communication services help you use voice commands to place calls or listen to
                              		messages in “hands-free” mode and check voice messages from your desktop,
                              		either integrated into an e-mail inbox or from a Web browser.
                              		Cisco Unity Connection also features robust automated-attendant functions that
                              		include intelligent routing and easily customizable call-screening and
                              		message-notification options.

For instructions on
                              		how to integrate Cisco Unified CME with Cisco Unity Connection, see Cisco CallManager Express 3.x
                                 		  Integration Guide for Cisco Unity Connection 1.1 .

### Cisco Unity Express Integration

Cisco Unity Express
                              		offers easy, one-touch access to messages and commonly used voice-mail features
                              		that enable users to reply, forward, and save messages. To improve message
                              		management, users can create alternate greetings, access envelope information,
                              		and mark or play messages based on privacy or urgency. For instructions on how
                              		to configure Cisco Unity Express, see the administrator guides for Cisco Unity Express .

For configuration
                              		information, see “Enabling
                                 		  DTMF Integration Using SIP NOTIFY” .

Cisco Unified CME
                                          		  and Cisco Unity Express must both be configured before they can be integrated.

### Cisco Unity
                           	 Integration

Cisco Unity is a
                              		Microsoft Windows-based communications solution that brings you voice mail and
                              		unified messaging and integrates them with the desktop applications you use
                              		daily. Cisco Unity gives you the ability to access all of your messages, voice,
                              		fax, and e-mail, by using your desktop PC, a touchtone phone, or the Internet.
                              		The Cisco Unity voice mail system supports voice-mail integration with
                              		Cisco Unified CME. This integration requires that you configure the
                              		Cisco Unified CME router and Cisco Unity software to get voice-mail service.

For configuration
                              		instructions, see “Enabling
                                 		  DTMF Integration Using RFC 2833” .

### DTMF Integration
                           	 for Legacy Voice-Mail Applications

For dual-tone
                              		multifrequency (DTMF) integrations, information on how to route incoming or
                              		forwarded calls is sent by a telephone system in the form of DTMF digits. The
                              		DTMF digits are sent in a pattern that is based on the integration file in the
                              		voice-mail system connected to the Cisco Unified CME router. These patterns are
                              		required for DTMF integration of Cisco Unified CME with most voice-mail
                              		systems. Voice-mail systems are designed to respond to DTMF after the system
                              		answers the incoming calls.

After configuring
                              		the DTMF integration patterns on the Cisco Unified CME router, you set up the
                              		integration files on the third-party legacy voice-mail system by following the
                              		instructions in the documents that accompany the voice-mail system. You must
                              		design the DTMF integration patterns appropriately so that the voice-mail
                              		system and the Cisco Unified CME router work with each other.

For configuration
                              		information, see Enabling
                                 		  DTMF Integration for Analog Voice-Mail Applications .

### Mailbox Selection
                           	 Policy

Typically a
                              		voice-mail system uses the number that a caller has dialed to determine the
                              		mailbox to which a call should be sent. However, if a call has been diverted
                              		several times before reaching the voice-mail system, the mailbox that is
                              		selected might vary for different types of voice-mail systems. For example,
                              		Cisco Unity Express uses the last number to which the call was diverted before
                              		it was sent to voice mail as the mailbox number. Cisco Unity and some legacy
                              		PBX systems use the originally called number as the mailbox number.

The Mailbox
                              		Selection Policy feature allows you to provision the following options from the
                              		Cisco Unified CME configuration.

For
                                    			 Cisco Unity Express, you can select the originally dialed number.

For PBX
                                    			 voice-mail systems, you can select the last number to which the call was
                                    			 diverted before it was sent to voice mail. This option is configured on the
                                    			 outgoing dial peer for the voice-mail system's pilot number.

For Cisco Unity
                                    			 voice mail, you can select the last number to which the call was diverted
                                    			 before it was sent to voice mail. This option is configured on the ephone-dn
                                    			 that is associated with the voice-mail pilot number.

To enable Mailbox
                              		Selection Policy, see “SCCP:
                                 		  Setting a Mailbox Selection Policy for Cisco Unity Express or a PBX Voice-Mail
                                 		  Number” or “SCCP:
                                 		  Setting Mailbox Selection Policy for Cisco Unity” .

### RFC 2833 DTMF MTP
                           	 Pass through

In Cisco Unified CME
                              		4.1, the RFC 2833 Dual-Tone Multifrequency (DTMF) Media Termination Point (MTP)
                              		Passthrough feature provides the capability to pass DTMF tones transparently
                              		between SIP endpoints that require transcoding or Resource Reservation Protocol
                              		(RSVP) agents.

This feature
                              		supports DTMF Relay across SIP WAN devices that support RFC 2833, such as
                              		Cisco Unity and SIP trunks. Devices registered to a Cisco Unified CME SIP
                              		back-to-back user agent (B2BUA) can exchange RFC 2833 DTMF MTP with other
                              		devices that are not registered with the Cisco Unified CME SIP B2BUA, or with
                              		devices that are registered in one of the following:

Local or remote
                                    			 Cisco Unified CME

Cisco Unified Communications Manager

Third party
                                    			 proxy

By default, the RFC
                              		2833 DTMF MTP Passthrough feature uses payload type 101 on MTP, and MTP accepts
                              		all the other dynamic payload types if it is indicated by Cisco Unified CME.
                              		For configuration information, see Enabling
                                 		  DTMF Integration Using RFC 2833 .

### MWI Line
                           	 Selection

Message waiting
                              		indicator (MWI) line selection allows you to choose the phone line that is
                              		monitored for voice-mail messages and that lights an indicator when messages
                              		are present.

Before
                              		Cisco Unified CME 4.0, the MWI lamp on a phone running SCCP could be associated
                              		only with the primary line of the phone.

In Cisco Unified CME
                              		4.0 and later versions, you can designate a phone line other than the primary
                              		line to be associated with the MWI lamp. Lines other than the one associated
                              		with the MWI lamp display an envelope icon when a message is waiting. A logical
                              		phone “line” is not the same as a phone button. A button with one or more
                              		directory numbers is considered one line. A button with no directory number
                              		assigned does not count as a line.

In Cisco Unified CME
                              		4.0 and later versions, a SIP directory number that is used for call forward
                              		all, presence BLF status, and MWI features must be configured by using the dn keyword in
                              		the number command; direct line numbers are not supported.

For configuration
                              		information, see SCCP:
                                 		  Configuring a Voice Mailbox Pilot Number or SIP:
                                 		  Configuring a Directory Number for MWI .

### AMWI

The AMWI (Audible
                              		Message Line Indicator) feature provides a special stutter dial tone to
                              		indicate message waiting. This is an accessibility feature for vision-impaired
                              		phone users. The stutter dial tone is defined as 10 ms ON, 100 ms OFF, repeat
                              		10 times, then steady on.

In Cisco Unified CME
                              		4.0(3), you can configure the AMWI feature on the Cisco Unified IP Phone 7911
                              		and Cisco Unified IP Phone 7931G to receive audible, visual, or audible and
                              		visual MWI notification from an external voice-messaging system. AMWI cannot be
                              		enabled unless the number command is already configured for the IP phone to be configured.

Cisco Unified CME
                              		applies the following logic based on the capabilities of the IP phone and how
                              		MWI is configured:

If the phone
                                    			 supports (visual) MWI and MWI is configured for the phone, activate the Message
                                    			 Waiting light.

If the phone
                                    			 supports (visual) MWI only, activate the Message Waiting light regardless of
                                    			 the configuration.

If the phone
                                    			 supports AMWI and AMWI is configured for the phone, send the stutter dial tone
                                    			 to the phone when it goes off-hook.

If the phone
                                    			 supports AMWI only and AMWI is configured, send the stutter dial tone to the
                                    			 phone when it goes off-hook regardless of the configuration.

If a phone supports
                              		(visual) MWI and AMWI and both options are configured for the phone, activate
                              		the Message Waiting light and send the stutter dial tone to the phone when it
                              		goes off-hook.

For configuration
                              		information, see SCCP:
                                 		  Configuring a Phone for MWI Outcall .

### SIP MWI Prefix
                           	 Specification

Central
                              		voice-messaging servers that provide mailboxes for several Cisco Unified CME
                              		sites may use site codes or prefixes to distinguish among similarly numbered
                              		ranges of extensions at different sites. In Cisco Unified CME 4.0 and later
                              		versions, you can specify that your Cisco Unified CME system should accept
                              		unsolicited SIP Notify messages for MWI that include a prefix string as a site
                              		identifier.

For example, an MWI
                              		message might indicate that the central mailbox number 555-0123 has a voice
                              		message. In this example, the digits 555 are set as the prefix string or site
                              		identifier using the mwi prefix command. The local Cisco Unified CME system is able to convert 555-0123 to 0123
                              		and deliver the MWI to the correct phone. Without this prefix string
                              		manipulation, the system would reject an MWI for 555-0123 as not matching the
                              		local Cisco Unified CME extension 0123.

To enable SIP MWI
                              		Prefix Specification, see Enabling
                                 		  SIP MWI Prefix Specification .

### SIP MWI - QSIG
                           	 Translation

In Cisco Unified CME
                              		4.1 and later, the SIP MWI - QSIG Translation feature extends MWI functionality
                              		for SIP MWI and QSIG MWI interoperation to enable sending and receiving MWI
                              		over QSIG to a PBX.

When the SIP
                              		Unsolicited NOTIFY is received from voice mail, the Cisco router translates
                              		this event to activate QSIG MWI to the PBX, via PSTN. The PBX will switch on,
                              		or off, the MWI lamp on the corresponding IP phone. This feature supports only
                              		Unsolicited NOTIFY. Subscribe NOTIFY is not supported by this feature.

In SIP MWI to
                                 		  ISDN QSIG When Voice Mail and Cisco Router are On the Same LAN ,
                              		the Cisco router receives the SIP Unsolicited NOTIFY, performs the protocol
                              		translation, and initiates the QSIG MWI call to the PBX, where it is routed to
                              		the appropriate phone.

It makes no
                              		difference if the SIP Unsolicited NOTIFY is received via LAN or WAN if the PBX
                              		is connected to the Cisco router, and not to the remote voice-mail server.

In SIP MWI to
                                 		  ISDN QSIG When PBX is Connected to a Remote Cisco Router ,
                              		a voice mail server and Cisco Unified CME are connected to the same LAN and a
                              		remote Cisco Unified CME is connected across the WAN. In this scenario, the
                              		protocol translation is performed at the remote Cisco router and the QSIG MWI
                              		message is sent to the PBX.

### VMWI

There are two types
                              		of visual message waiting indicator (VMWI) features: Frequency-shift Keying
                              		(FSK) and DC voltage. The message-waiting lamp can be enabled to flash on an
                              		analog phone that requires an FSK message to activate a visual indicator. The
                              		DC Voltage VMWI feature is used to flash the message-waiting lamp on an analog
                              		phone which requires DC voltage instead of an FSK message. For all other
                              		applications, such as MGCP, FSK VMWI is used even if the voice gateway is
                              		configured for DC voltage VMWI. The configuration for DC voltage VMWI is
                              		supported only for Foreign Exchange Station (FXS) ports on the Cisco VG224
                              		analog voice gateway with analog device version V1.3 and V2.1.

The Cisco VG224 can
                              		only support 12 Ringer Equivalency Number (REN) for ringing 24 onboard analog
                              		FXS voice ports. To support ringing and DC Voltage VMWI for 24 analog voice
                              		ports, stagger-ringing logic is used to maximize the limited REN resource. When
                              		a system runs out of REN because too many voice ports are being rung, the MWI
                              		lamp temporarily turns off to free up REN to ring the voice ports.

DC voltage VMWI is
                              		also temporarily turned off any time the port's operational state is no longer
                              		idle and onhook, such as when one of the following events occur:

Incoming call on
                                    			 voice port

Phone goes off
                                    			 hook

The voice port
                                    			 is shut down or busied out

Once the operational
                              		state of the port changes to idle and onhook again, the MWI lamp resumes
                              		flashing until the application receives a requests to clear it; for example, if
                              		there are no more waiting messages.

For configuration
                              		information, see Transfer
                                 		  to Voice Mail .

### Transfer to Voice
                           	 Mail

The Transfer to
                              		Voice Mail feature allows a phone user to transfer a caller directly to a
                              		voice-mail extension. The user presses the TrnsfVM softkey to place the call on
                              		hold, enters the extension number, and then commits the transfer by pressing
                              		the TrnsfVM softkey again. The caller hears the complete voice mail greeting.
                              		This feature is supported using the TrnsfVM softkey or feature access code
                              		(FAC).

For example, a
                              		receptionist might screen calls for five managers. If a call comes in for a
                              		manager who is not available, the receptionist can transfer the caller to the
                              		manager's voice-mail extension by using the TrnsfVM softkey and the caller
                              		hears the personal greeting of the individual manager.

For configuration
                              		information, see Transfer
                                 		  to Voice Mail .

### Live
                           	 Record

The Live Record
                              		feature enables IP phone users in a Cisco Unified CME system to record a phone
                              		conversation if Cisco Unity Express is the voice mail system. An audible
                              		notification, either by announcement or by periodic beep, alerts participants
                              		that the conversation is being recorded. The playing of the announcement or
                              		beep is under the control of Cisco Unity Express.

Live Record is
                              		supported for two-party calls and ad hoc conferences. In normal record mode,
                              		the conversation is recorded after the LiveRcd softkey is pressed. This puts
                              		the other party on-hold and initiates a call to Cisco Unity Express at the
                              		configured live-record number. To stop the recording session, the phone user
                              		presses the LiveRcd softkey again, which toggles between on and off.

The Live-Record
                              		number is configured globally and must match the number configured in
                              		Cisco Unity Express. You can control the availability of the feature on
                              		individual phones by modifying the display of the LiveRcd softkey using an
                              		ephone template. This feature must be enabled on both Cisco Unified CME and
                              		Cisco Unity Express.

To enable Live
                              		Record in Cisco Unified CME, see SCCP:
                                 		  Configuring Live Record .

### Cisco Unity Express AXL Enhancement

In Cisco Unified CME 7.0(1) and later versions, the Cisco Unity Express
                              		AXL enhancement in Cisco Unified CME provides better administrative integration
                              		between Cisco Unified CME and Cisco Unity Express by automatically
                              		synchronizing passwords.

No configuration is required to enable this feature.

## Configure Voice-Mail Integration

### Configure a Voice
                           	 Mailbox Pilot Number on a SCCP Phone

To configure the
                                 		  telephone number that is speed-dialed when the Message button on a SCCP phone
                                 		  is pressed, perform the following steps.

The same
                                             			 telephone number is configured for voice messaging for all SCCP phones in
                                             			 Cisco Unified CME.

#### Before you begin

Voicemail
                                       				phone number must be a valid number; directory number and number for voicemail
                                       				phone number must be configured.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- voicemail phone-number

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

Enters voice
                                             				register global configuration mode to set parameters for all supported phones
                                             				in Cisco Unified CME.

Step 4

voicemail phone-number

#### Example:

```
Router(config-telephony)# voice mail 0123
```

Defines the
                                             				telephone number that is speed-dialed when the Messages button on a
                                             				Cisco Unified IP phone is pressed.

phone-number— Same phone number is configured for
                                                   					 voice messaging for all SCCP phones in a Cisco Unified CME.

Step 5

end

#### Example:

```
Router(config-telephony)# end
```

Exits to
                                             				privileged EXEC mode.

#### What to do next

(Cisco Unified CME 4.0 or a later version only) To set up a
                                       				mailbox selection policy, see SCCP:
                                          				  Configuring a Mailbox Selection Policy .

To set up DTMF
                                       				integration patterns for connecting to analog voice-mail applications, see Enabling
                                          				  DTMF Integration for Analog Voice-Mail Applications .

To connect to
                                       				a remote SIP-based IVR or Cisco Unity, or to connect to a remote SIP-PSTN that
                                       				goes through the PSTN to a voice-mail or IVR application, see Enabling
                                          				  DTMF Integration Using RFC 2833 .

To connect to
                                       				a Cisco Unity Express system, configure a nonstandard SIP NOTIFY format. See Enabling
                                          				  DTMF Integration Using SIP NOTIFY .

### Configure a
                           	 Mailbox Selection Policy on SCCP Phone

Perform one of the following
                              		tasks, depending on which voice-mail application is used:

Set a Mailbox Selection Policy for Cisco Unity
                                       				Express or a PBX Voice-Mail Number

Set a Mailbox Selection Policy for Cisco
                                       				Unity

#### Set a Mailbox
                              	 Selection Policy for Cisco Unity Express or a PBX Voice-Mail Number

To set a policy
                                    		  for selecting a mailbox for calls from a Cisco Unified CME system that are
                                    		  diverted before being sent to a Cisco Unity Express or PBX voice-mail pilot
                                    		  number, perform the following steps.

Restriction

In the following
                                                			 scenarios, the mailbox selection policy can fail to work properly:

The last
                                                      				  redirecting endpoint is not hosted on Cisco Unified CME. This may rarely occur
                                                      				  with a PBX.

A call is
                                                      				  forwarded across several SIP trunks. Multiple SIP Diversion Headers (stacking
                                                      				  hierarchy) are not supported in Cisco IOS software.

A call is
                                                      				  forwarded across non-Cisco voice gateways that do not support the optional
                                                      				  H450.3 originalCalledNr field.

##### Before you begin

Cisco Unified CME
                                    		  4.0 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice tag voip or dial-peer voice tag pots

- mailbox-selection [ last-redirect-num | orig-called-num ]

- end

### DETAILED STEPS

Step 1

enable

##### Example:

```
Router> enable
```

Enables
                                                				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

##### Example:

```
Router# configure terminal
```

Enters global
                                                				configuration mode.

Step 3

dial-peer voice tag voip or dial-peer voice tag pots

##### Example:

```
Router(config)# dial-peer voice 7000 voip
```

or

```
Router(config)# dial-peer voice 35 pots
```

Enters
                                                				dial-peer configuration mode.

tag —identifies the dial peer. Valid entries are
                                                      					 1 to 2147483647.

Use this
                                                            				  command on the outbound dial peer associated with the pilot number of the
                                                            				  voice-mail system. For systems using Cisco Unity Express, this is a VoIP dial
                                                            				  peer. For systems using PBX-based voice mail, this is a POTS dial peer.

Step 4

mailbox-selection [ last-redirect-num | orig-called-num ]

##### Example:

```
Router(config-dial-peer)# mailbox-selection orig-called-num
```

Sets a policy
                                                				for selecting a mailbox for calls that are diverted before being sent to a
                                                				voice-mail line.

last-redirect-num —(PBX voice mail only) The
                                                      					 mailbox number to which the call will be sent is the last number to divert the
                                                      					 call (the number that sends the call to the voice-mail pilot number).

orig-called-num —(Cisco Unity Express only) The
                                                      					 mailbox number to which the call will be sent is the number that was originally
                                                      					 dialed before the call was diverted.

Step 5

end

##### Example:

```
Router(config-ephone-dn)# end
```

Returns to
                                                				privileged EXEC mode.

##### What to do next

- To use voice
                                       			 mail on a SIP network that connects to a Cisco Unity Express system, configure
                                       			 a nonstandard SIP NOTIFY format. See Enabling
                                          				DTMF Integration Using SIP NOTIFY .

#### Set a Mailbox
                              	 Selection Policy for Cisco Unity

To set a policy
                                    		  for selecting a mailbox for calls that are diverted before being sent to a
                                    		  Cisco Unity voice-mail pilot number, perform the following steps.

Restriction

This feature
                                                			 might not work properly in certain network topologies, including when:

The last
                                                      				  redirecting endpoint is not hosted on Cisco Unified CME. This may rarely occur
                                                      				  with a PBX.

A call is
                                                      				  forwarded across several SIP trunks. Multiple SIP Diversion Headers (stacking
                                                      				  hierarchy) are not supported in Cisco IOS software.

A call is
                                                      				  forwarded across other voice gateways that do not support the optional H450.3
                                                      				  originalCalledNr field.

##### Before you begin

Cisco Unified CME 4.0 or a later version.

Directory
                                          				number to be configured is associated with a voice mailbox.

### SUMMARY STEPS

- enable

- configure terminal

- exit

- ephone-dn dn-tag

- mailbox-selection [ last-redirect-num ]

- end

### DETAILED STEPS

Step 1

enable

##### Example:

```
Router> enable
```

Enables
                                                				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

##### Example:

```
Router# configure terminal
```

Enters global
                                                				configuration mode.

Step 3

exit

##### Example:

```
Router(config-dial-peer)# exit
```

Exits
                                                				dial-peer configuration mode.

Step 4

ephone-dn dn-tag

##### Example:

```
Router(config)# ephone-dn 752
```

Enters
                                                				ephone-dn configuration mode.

Step 5

mailbox-selection [ last-redirect-num ]

##### Example:

```
Router(config-ephone-dn)# mailbox-selection last-redirect-num
```

Sets a policy
                                                				for selecting a mailbox for calls that are diverted before being sent to a
                                                				Cisco Unity voice-mail pilot number.

Step 6

end

##### Example:

```
Router(config-ephone-dn)# end
```

Returns to
                                                				privileged EXEC mode.

##### What to do next

- To use a remote SIP-based IVR or Cisco
                                       			 Unity, or to connect Cisco Unified CME to a remote SIP-PSTN that goes through
                                       			 the PSTN to a voice-mail or IVR application, see Enabling
                                          				DTMF Integration Using RFC 2833 .

### Transfer to Voice
                           	 Mail

To enable a phone
                                 		  user to transfer a call to voice mail by using the TrnsfVM softkey or a FAC,
                                 		  perform the following steps.

Restriction

The TrnsfVM
                                             			 softkey is not supported on the Cisco Unified IP Phone 7905, 7912, or 7921, or
                                             			 analog phones connected to the Cisco VG224 or Cisco ATA. These phones support
                                             			 the trnsfvm FAC.

#### Before you begin

Cisco Unified
                                       				CME 4.3 or a later version.

Cisco Unity Express 3.0 or a later version, installed and
                                       				configured.

For
                                       				information about standard and custom FACs, see Configuring
                                          				  Feature Access Codes .

### SUMMARY STEPS

- enable

- configure terminal

- ephone-template template-tag

- softkeys connected {[ Acct ] [ ConfList ] [ Confrn ] [ Endcall ] [ Flash ] [ HLog ] [ Hold ] [ Join ] [ LiveRcd ] [ Park ] [ RmLstC ] [ Select ] [ TrnsfVM ] [ Trnsfer ]}

- exit

- ephone phone-tag

- ephone-template template-tag

- exit

- telephony-service

- voicemail phone-number

- fac { standard | custom
                                       				  trnsfvm custom-fac }

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

ephone-template template-tag

#### Example:

```
Router(config)# ephone-template 5
```

Enters
                                             				ephone-template configuration mode to create an ephone template.

template-tag —Unique identifier for the ephone
                                                   					 template. Range: 1 to 20.

Step 4

softkeys connected {[ Acct ] [ ConfList ] [ Confrn ] [ Endcall ] [ Flash ] [ HLog ] [ Hold ] [ Join ] [ LiveRcd ] [ Park ] [ RmLstC ] [ Select ] [ TrnsfVM ] [ Trnsfer ]}

#### Example:

```
Router(config-ephone-template)# softkeys connected TrnsfVM Park Acct ConfList Confrn Endcall Trnsfer Hold
```

(Optional)
                                             				Modifies the order and type of softkeys that display on an IP phone during the
                                             				connected call state.

You can
                                                   					 enter any of the keywords in any order.

Default is
                                                   					 all softkeys are displayed in alphabetical order.

Any
                                                   					 softkey that is not explicitly defined is disabled.

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
                                                   					 template that you created in Step 3 .

Step 8

exit

#### Example:

```
Router(config-ephone)# exit
```

Exits ephone
                                             				configuration mode.

Step 9

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony-service configuration mode.

Step 10

voicemail phone-number

#### Example:

```
Router(config-telephony)# voicemail 8900
```

Defines the
                                             				telephone number that is speed-dialed when the Messages button on a
                                             				Cisco Unified IP phone is pressed.

phone-number —Same phone number is configured for
                                                   					 voice messaging for all SCCP phones in a Cisco Unified CME.

Step 11

fac { standard | custom
                                                				  trnsfvm custom-fac }

#### Example:

```
Router(config-telephony)# fac custom trnsfvm #22
```

Enables
                                             				standard FACs or creates a custom FAC or alias.

standard —Enables standard FACs for all phones.
                                                   					 Standard FAC for transfer to voice mail is *6.

custom —Creates a custom FAC for a FAC type.

custom-fac —User-defined code to be dialed using
                                                   					 the keypad on an IP or analog phone. Custom FAC can be up to 256 characters
                                                   					 long and contain numbers 0 to  9 and * and #.

Step 12

end

#### Example:

```
Router(config-telephony)# end
```

Returns to
                                             				privileged EXEC mode.

#### Example

The following
                                 		  example shows a configuration where the display order of the TrnsfVM softkey is
                                 		  modified for the connected call state in ephone template 5 and assigned to
                                 		  ephone 12. A custom FAC for transfer to voice mail is set to #22.

```
telephony-service
 max-ephones 100
 max-dn 240
 timeouts transfer-recall 60
 voicemail 8900
 max-conferences 8 gain -6
 transfer-system full-consult
 fac custom trnsfvm #22
!
!
ephone-template  5
 softkeys connected  TrnsfVM Park Acct ConfList Confrn Endcall Trnsfer Hold
 max-calls-per-button 3
 busy-trigger-per-button 2
!
!
ephone  12
 ephone-template 5
 mac-address 000F.9054.31BD
 type 7960
 button  1:10 2:7
```

#### What to do next

If you are
                                       				finished modifying parameters for phones in Cisco Unified CME, generate a new
                                       				configuration file and restart the phones. See SCCP:
                                          				  Generating Configuration Files for SCCP Phones .

For
                                       				information on how phone users transfer a call to voice mail, see Cisco Unified IP Phone
                                          				  documentation for Cisco Unified CME .

### Configure Live
                           	 Record on SCCP Phones

To configure the
                                 		  Live Record feature so that a phone user can record a conversation by pressing
                                 		  the LiveRcd softkey, perform the followings steps.

Restriction

Only one
                                                   				  live record session is allowed for each conference.

Only the
                                                   				  conference creator can initiate a live record session. In an ad hoc conference,
                                                   				  participants who are not the conference creator cannot start a live record
                                                   				  session. In a two-party call, the party who starts the live record session is
                                                   				  the conference creator.

For legal
                                             			 disclaimer information about this feature, see copyright information section.

#### Before you begin

Cisco Unified
                                       				CME 4.3 or a later version.

Cisco Unity Express 3.0 or a later version, installed and
                                       				configured. For information on configuring Live Record in Cisco Unity Express,
                                       				see Configure Live Record in the Cisco Unity Express Voice-Mail and Auto-Attendant CLI
                                          				  Administrator Guide for 3.0 and Later Versions .

Ad hoc hardware conference resource is configured and ready to use. See Configure Hardware Conferencing .

If phone user
                                       				wants to view the live record session, include ConfList softkey using the softkeys connected command.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- live record number

- voicemail number

- exit

- ephone-dn dn-tag

- number number [ secondary number ] [ no-reg [ both | primary ]]

- call-forward all target-number

- exit

- ephone-template template-tag

- softkeys connected {[ Acct ] [ ConfList ] [ Confrn ] [ Endcall ] [ Flash ] [ HLog ] [ Hold ] [ Join ] [ LiveRcd ] [ Park ] [ RmLstC ] [ Select ] [ TrnsfVM ] [ Trnsfer ]}

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

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony-service configuration mode.

Step 4

live record number

#### Example:

```
Router(config-telephony)# live record 8900
```

Defines the
                                             				extension number that is dialed when the LiveRcd softkey is pressed on an SCCP
                                             				IP phone.

Step 5

voicemail number

#### Example:

```
Router(config-telephony)# voicemail 8000
```

Defines the
                                             				extension number that is speed-dialed when the Messages button is pressed on an
                                             				IP phone.

Number —Cisco Unity Express voice-mail pilot
                                                   					 number.

Step 6

exit

#### Example:

```
Router(config-telephony)# exit
```

Exits
                                             				telephony-service configuration mode.

Step 7

ephone-dn dn-tag

#### Example:

```
Router(config)# ephone-dn 10
```

Creates a
                                             				directory number that forwards all calls to the Cisco Unity Express voice-mail
                                             				pilot number.

Step 8

number number [ secondary number ] [ no-reg [ both | primary ]]

#### Example:

```
Router(config-ephone-dn)# number 8900
```

Assigns an
                                             				extension number to this directory number.

Number —Must
                                                   					 match the Live Record pilot-number configured in Step 4 .

Step 9

call-forward all target-number

#### Example:

```
Router(config-ephone-dn)# call-forward all 8000
```

Forwards all
                                             				calls to this extension to the specified voice-mail number.

target-number —Phone number to which calls are
                                                   					 forwarded. Must match the voice-mail pilot number configured in Step 5 .

Phone
                                                         				  users can activate and cancel the call-forward-all state from the phone using
                                                         				  the CFwdAll softkey or a FAC.

Step 10

exit

#### Example:

```
Router(config-ephone-dn)# exit
```

Exits
                                             				ephone-dn configuration mode.

Step 11

ephone-template template-tag

#### Example:

```
Router(config)# ephone-template 5
```

Enters
                                             				ephone-template configuration mode to create an ephone template.

template-tag —Unique identifier for the ephone
                                                   					 template. Range: 1 to 20.

Step 12

softkeys connected {[ Acct ] [ ConfList ] [ Confrn ] [ Endcall ] [ Flash ] [ HLog ] [ Hold ] [ Join ] [ LiveRcd ] [ Park ] [ RmLstC ] [ Select ] [ TrnsfVM ] [ Trnsfer ]}

#### Example:

```
Router(config-ephone-template)# softkeys connected LiveRcd Confrn Hold Park Trnsfer TrnsfVM
```

Modifies the
                                             				order and type of softkeys that display on an IP phone during the connected
                                             				call state.

Step 13

exit

#### Example:

```
Router(config-ephone-template)# exit
```

Exits
                                             				ephone-template configuration mode.

Step 14

ephone phone-tag

#### Example:

```
Router(config)# ephone 12
```

Enters
                                             				ephone configuration mode.

phone-tag —Unique number that identifies this
                                                   					 ephone during configuration tasks.

Step 15

ephone-template template-tag

#### Example:

```
Router(config-ephone)# ephone-template 5
```

Applies the
                                             				ephone template to the phone.

template-tag —Unique identifier of the ephone
                                                   					 template that you created in Step 11 .

Step 16

end

#### Example:

```
Router(config-ephone)# end
```

Exits to
                                             				privileged EXEC mode.

#### Example

The following
                                 		  example shows Live Record is enabled at the system-level for extension 8900.
                                 		  All incoming calls to extension 8900 are forwarded to the voice-mail pilot
                                 		  number 8000 when the LiveRcd softkey is pressed, as configured under ephone-dn
                                 		  10. Ephone template 5 modifies the display order of the LiveRcd softkey on IP
                                 		  phones.

```
telephony-service
 privacy-on-hold
 max-ephones 100
 max-dn 240
 timeouts transfer-recall 60
 live-record 8900
 voicemail 8000
 max-conferences 8 gain -6
 transfer-system full-consult
 fac standard
!
!
ephone-template  5
 softkeys remote-in-use  CBarge Newcall
 softkeys hold  Resume Newcall Join
 softkeys connected  LiveRcd Confrn Hold Park Trnsfer TrnsfVM
 max-calls-per-button 3
 busy-trigger-per-button 2
!
!
ephone-dn  10
 number 8900
 call-forward all 8000
```

### Configure a Voice
                           	 Mailbox Pilot Number on a SIP Phone

To configure the
                                 		  telephone number that is speed-dialed when the Message button on a SIP phone is
                                 		  pressed, follow the steps in this section.

The same
                                             			 telephone number is configured for voice messaging for all SIP phones in
                                             			 Cisco Unified CME. The call forward
                                                   				  b2bua command enables call forwarding and designates that calls
                                             			 that are forwarded to a busy or no-answer extension be sent to a voicemail box.

#### Before you begin

Directory
                                       				number and number for voicemail phone number must be configured.

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- voicemail phone-number

- exit

- voice register dn dn-tag

- call-forward b2bua busy directory-number

- call-forward b2bua mailbox directory-number

- call-forward b2bua noan directory-number timeout seconds

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

voicemail phone-number

#### Example:

```
Router(config-register-global)# voice mail 1111
```

Defines the
                                             				telephone number that is speed-dialed when the Messages button on a
                                             				Cisco Unified IP phone is pressed.

phone-number— Same phone number is configured for
                                                   					 voice messaging for all SIP phones in a Cisco Unified CME.

Step 5

exit

#### Example:

```
Router(config-register-global)# exit
```

Exits voice
                                             				register global configuration mode.

Step 6

voice register dn dn-tag

#### Example:

```
Router(config)# voice register dn 2
```

Enters voice
                                             				register dn mode to define a directory number for a SIP phone, intercom line,
                                             				voice port, or an MWI.

Step 7

call-forward b2bua busy directory-number

#### Example:

```
Router(config-register-dn)# call-forward b2bua busy 1000
```

Enables call
                                             				forwarding for a SIP back-to-back user agent so that incoming calls to an
                                             				extension that is busy will be forwarded to the designated directory number.

Step 8

call-forward b2bua mailbox directory-number

#### Example:

```
Router(config-register-dn)# call-forward b2bua mailbox 2200
```

Designates the
                                             				voice mailbox to use at the end of a chain of call forwards.

Incoming
                                                   					 calls have been forwarded to a busy or no-answer extension will be forwarded to
                                                   					 the directory-number specified.

Step 9

call-forward b2bua noan directory-number timeout seconds

#### Example:

```
Router(config-register-dn)# call-forward b2bua noan 2201 timeout 15
```

Enables call
                                             				forwarding for a SIP back-to-back user agent so that incoming calls to an
                                             				extension that does not answer will be forwarded to the designated directory
                                             				number.

seconds —Number of seconds that a call can ring
                                                   					 with no answer before the call is forwarded to another extension. Range: 3 to
                                                   					 60000. Default: 20.

Step 10

end

#### Example:

```
Router(config-register-dn)# end
```

Exits to
                                             				privileged EXEC mode.

#### What to do next

To set up
                                       				DTMF integration patterns for connecting to analog voice-mail applications, see Enabling
                                          				  DTMF Integration for Analog Voice-Mail Applications .

To use a
                                       				remote SIP-based IVR or Cisco Unity, or to connect to a remote SIP-PSTN that
                                       				goes through the PSTN to a voice-mail or IVR application, see Enabling
                                          				  DTMF Integration Using RFC 2833 .

To connect
                                       				to a Cisco Unity Express system, configure a nonstandard SIP NOTIFY format, see Enabling
                                          				  DTMF Integration Using SIP NOTIFY .

### Enable DTMF
                           	 Integration

Perform one of the following
                              		tasks, depending on which DTMF-relay method is required:

Enabling DTMF Integration for Analog Voice-Mail
                                       				Applications —To set up DTMF integration patterns for connecting to
                                    			 analog voice-mail applications.

Enabling DTMF Integration Using RFC 2833 —To
                                    			 connect to a remote SIP-based IVR or voice-mail application such as Cisco Unity
                                    			 or when SIP is used to connect Cisco Unified CME to a remote SIP-PSTN voice
                                    			 gateway that goes through the PSTN to a voice-mail or IVR application.

Enabling DTMF Integration Using SIP
                                       				NOTIFY —To configure a SIP dial peer to point to Cisco Unity Express.

#### Enable DTMF
                              	 Integration for Analog Voice-Mail Applications

To set up DTMF
                                    		  integration patterns for analog voice-mail applications, perform the following
                                    		  steps.

You can
                                                			 configure multiple tags and tokens for each pattern, depending on the
                                                			 voice-mail system and type of access.

### SUMMARY STEPS

- enable

- configure terminal

- vm-integration

- pattern direct tag1 { CGN | CDN | FDN } [ tag2 { CGN | CDN | FDN }] [ tag3 { CGN | CDN | FDN }] [ last-tag ]

- pattern ext-to-ext busy tag1 { CGN | CDN | FDN } [ tag2 { CGN | CDN | FDN }] [ tag3 { CGN | CDN | FDN }] [ last-tag ]

- pattern ext-to-ext
                                          				  no-answer tag1 { CGN | CDN | FDN } [ tag2 { CGN | CDN | FDN }] [ tag3 { CGN | CDN | FDN }] [ last-tag ]

- pattern trunk-to-ext busy tag1 { CGN | CDN | FDN } [ tag2 { CGN | CDN | FDN }] [ tag3 { CGN | CDN | FDN }] [ last-tag ]

- pattern trunk-to-ext
                                          				  no-answer tag1 { CGN | CDN | FDN } [ tag2 { CGN | CDN | FDN }] [ tag3 { CGN | CDN | FDN }] [ last-tag ]

- end

### DETAILED STEPS

Step 1

enable

##### Example:

```
Router> enable
```

Enables
                                                				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

##### Example:

```
Router# configure terminal
```

Enters global
                                                				configuration mode.

Step 3

vm-integration

##### Example:

```
Router(config) vm-integration
```

Enters
                                                				voice-mail integration configuration mode and enables voice-mail integration
                                                				with DTMF and an analog voice-mail system.

Step 4

pattern direct tag1 { CGN | CDN | FDN } [ tag2 { CGN | CDN | FDN }] [ tag3 { CGN | CDN | FDN }] [ last-tag ]

##### Example:

```
Router(config-vm-integration) pattern direct 2 CGN *
```

Configures the
                                                				DTMF digit pattern forwarding necessary to activate the voice-mail system when
                                                				the user presses the messages button on the phone.

The tag attribute
                                                      					 is an alphanumeric string fewer than four DTMF digits in length. The
                                                      					 alphanumeric string consists of a combination of four letters (A, B, C, and D),
                                                      					 two symbols (* and #), and ten digits (0 to 9). The tag numbers match the
                                                      					 numbers defined in the voice-mail system’s integration file, immediately
                                                      					 preceding either the number of the calling party, the number of the called
                                                      					 party, or a forwarding number.

The
                                                      					 keywords, CGN , CDN , and FDN ,
                                                      					 configure the type of call information sent to the voice-mail system, such as
                                                      					 calling number (CGN), called number (CDN), or forwarding number (FDN).

Step 5

pattern ext-to-ext busy tag1 { CGN | CDN | FDN } [ tag2 { CGN | CDN | FDN }] [ tag3 { CGN | CDN | FDN }] [ last-tag ]

##### Example:

```
Router(config-vm-integration) pattern ext-to-ext busy 7 FDN * CGN *
```

Configures
                                                				the DTMF digit pattern forwarding necessary to activate the voice-mail system
                                                				when an internal extension attempts to connect to a busy extension and the call
                                                				is forwarded to voice mail.

Step 6

pattern ext-to-ext
                                                   				  no-answer tag1 { CGN | CDN | FDN } [ tag2 { CGN | CDN | FDN }] [ tag3 { CGN | CDN | FDN }] [ last-tag ]

##### Example:

```
Router(config-vm-integration) pattern ext-to-ext no-answer 5 FDN * CGN *
```

Configures
                                                				the DTMF digit pattern forwarding necessary to activate the voice-mail system
                                                				when an internal extension fails to connect to an extension and the call is
                                                				forwarded to voice mail.

Step 7

pattern trunk-to-ext busy tag1 { CGN | CDN | FDN } [ tag2 { CGN | CDN | FDN }] [ tag3 { CGN | CDN | FDN }] [ last-tag ]

##### Example:

```
Router(config-vm-integration) pattern trunk-to-ext busy 6 FDN * CGN *
```

Configures
                                                				the DTMF digit pattern forwarding necessary to activate the voice-mail system
                                                				when an external trunk call reaches a busy extension and the call is forwarded
                                                				to voice mail.

Step 8

pattern trunk-to-ext
                                                   				  no-answer tag1 { CGN | CDN | FDN } [ tag2 { CGN | CDN | FDN }] [ tag3 { CGN | CDN | FDN }] [ last-tag ]

##### Example:

```
Router(config-vm-integration)# pattern trunk-to-ext no-answer 4 FDN * CGN *
```

Configures
                                                				the DTMF digit pattern forwarding necessary to activate the voice-mail system
                                                				when an external trunk call reaches an unanswered extension and the call is
                                                				forwarded to voice mail.

Step 9

end

##### Example:

```
Router(config-vm-integration)# exit
```

Exits
                                                				configuration mode and enters privileged EXEC mode.

##### What to do next

After
                                    		  configuring DTMF relay, you are ready to configure Message Waiting Indicator
                                    		  (MWI) notification for either the MWI outcall, unsolicited notify, or
                                    		  subscribe/notify mechanism. See SCCP:
                                       			 Configuring a Phone for MWI Outcall .

#### Enable DTMF
                              	 Integration Using RFC 2833

To configure a SIP
                                    		  dial peer to point to Cisco Unity and enable SIP dual-tone multifrequency
                                    		  (DTMF) relay using RFC 2833, use the commands in this section on both the
                                    		  originating and terminating gateways.

This DTMF relay
                                    		  method is required in the following situations:

When SIP is
                                          				used to connect Cisco Unified CME to a remote SIP-based IVR or voice-mail
                                          				application such as Cisco Unity.

When SIP is
                                          				used to connect Cisco Unified CME to a remote SIP-PSTN voice gateway that goes
                                          				through the PSTN to a voice-mail or IVR application.

If the T.38 Fax
                                                			 Relay feature is also configured on this IP network, we recommend that you
                                                			 either configure the voice gateways to use a payload type other than PT96 or
                                                			 PT97 for fax relay negotiation, or depending on whether the SIP endpoints
                                                			 support different payload types, configure Cisco Unified CME to use a payload
                                                			 type other than PT96 or PT97 for DTMF.

##### Before you begin

Configure
                                          				the codec or voice-class
                                                					 codec command for transcoding between G.711 and G.729.

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice tag voip

- description string

- destination-pattern string

- session protocol sipv2

- session target { dns : address | ipv4 : destination-address }

- dtmf-relay
                                          				  rtp-nte

- dtmf-interworking
                                          				  rtp-nte

- end

### DETAILED STEPS

Step 1

enable

##### Example:

```
Router> enable
```

Enables
                                                				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

##### Example:

```
Router# configure terminal
```

Enters global
                                                				configuration mode.

Step 3

dial-peer voice tag voip

##### Example:

```
Router (config)# dial-peer voice 123 voip
```

Enters
                                                				dial-peer configuration mode to define a VoIP dial peer for the voice-mail
                                                				system.

tag —Defines the dial peer being configured. Range
                                                      					 is 1 to 2147483647.

Step 4

description string

##### Example:

```
Router (config-voice-dial-peer)# description CU pilot
```

(Optional)
                                                				Associates a description with the dial peer being configured. Enter a string of
                                                				up to 64 characters.

Step 5

destination-pattern string

##### Example:

```
Router (config-voice-dial-peer)# destination-pattern 20
```

Specifies the
                                                				pattern of the numbers that the user must dial to place a call.

string —Prefix or full E.164 number.

Step 6

session protocol sipv2

##### Example:

```
Router (config-voice-dial-peer)# session protocol sipv2
```

Specifies that
                                                				Internet Engineering Task Force (IETF) Session Initiation Protocol (SIP) is
                                                				protocol to be used for calls between local and remote routers using the packet
                                                				network.

Step 7

session target { dns : address | ipv4 : destination-address }

##### Example:

```
Router (config-voice-dial-peer)# session target ipv4:10.8.17.42
```

Designates a
                                                				network-specific address to receive calls from the dial peer being configured.

dns : address —Specifies the DNS address of the
                                                      					 voice-mail system.

ipv4 : destination-
                                                            						  address —Specifies the IP address of the voice-mail system.

Step 8

dtmf-relay
                                                   				  rtp-nte

##### Example:

```
Router (config-voice-dial-peer)# dtmf-relay rtp-nte
```

Sets DTMF
                                                				relay method for the voice dial peer being configured.

rtp-nte —
                                                      					 Provides conversion from the out-of-band SCCP indication to the SIP standard
                                                      					 for DTMF relay (RFC 2833). Forwards DTMF tones by using Real-Time Transport
                                                      					 Protocol (RTP) with the Named Telephone Event (NTE) payload type.

This
                                                      					 command can also be configured in voice-register-pool configuration mode. For
                                                      					 individual phones, the phone-level configuration for this command overrides the
                                                      					 system-level configuration for this command.

The need
                                                            				  to use out-of-band conversion is limited to SCCP phones. SIP phones natively
                                                            				  support in-band.

Step 9

dtmf-interworking
                                                   				  rtp-nte

##### Example:

```
Router (config-voice-dial-peer)# dtmf-interworking rtp-nte
```

(Optional)
                                                				Enables a delay between the dtmf-digit begin and dtmf-digit end events in the
                                                				RFC 2833 packets.

This
                                                      					 command is supported in Cisco IOS Release 12.4(15)XZ and later releases and in
                                                      					 Cisco Unified CME 4.3 and later versions.

This
                                                      					 command can also be configured in voice-service configuration mode.

Step 10

end

##### Example:

```
Router(config-voice-dial-peer)# end
```

Exits to
                                                				privileged EXEC mode.

##### What to do next

After
                                    		  configuring DTMF relay, you are ready to configure Message Waiting Indicator
                                    		  (MWI) notification for either the MWI outcall, unsolicited notify, or
                                    		  subscribe/notify mechanism. See SCCP:
                                       			 Configuring a Phone for MWI Outcall .

#### Enable DTMF
                              	 Integration Using SIP NOTIFY

To configure a SIP
                                    		  dial peer to point to Cisco Unity Express and enable SIP dual-tone
                                    		  multi-frequency (DTMF) relay using SIP NOTIFY format, follow the steps in this
                                    		  task.

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice tag voip

- description string

- destination-pattern string

- b2bua

- session protocol sipv2

- session target { dns : address | ipv4 : destination-address }

- dtmf-relay sip-notify

- codec g711ulaw

- no vad

- end

### DETAILED STEPS

Step 1

enable

##### Example:

```
Router> enable
```

Enables
                                                				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

##### Example:

```
Router# configure terminal#
```

Enters global
                                                				configuration mode.

Step 3

dial-peer voice tag voip

##### Example:

```
Router (config)# dial-peer voice 2 voip
```

Enters
                                                				dial-peer configuration mode to define a VoIP dial peer for the voice-mail
                                                				system.

tag —Defines the dial peer being configured. Range
                                                      					 is 1 to 2147483647.

Step 4

description string

##### Example:

```
Router (config-voice-dial-peer)# description cue pilot
```

(Optional)
                                                				Associates a description with the dial peer being configured. Enter a string of
                                                				up to 64 characters.

Step 5

destination-pattern string

##### Example:

```
Router (config-voice-dial-peer)# destination-pattern 20
```

Specifies the
                                                				pattern of the numbers that the user must dial to place a call.

string —Prefix or full E.164 number.

Step 6

b2bua

##### Example:

```
Router (config-voice-dial-peer)# b2bua
```

(Optional)
                                                				Includes the Cisco Unified CME address as part of contact in 3XX response to
                                                				point to Cisco Unity Express and enables SIP-to-SCCP call forward.

Step 7

session protocol sipv2

##### Example:

```
Router (config-voice-dial-peer)# session protocol sipv2
```

Specifies that
                                                				Internet Engineering Task Force (IETF) Session Initiation Protocol (SIP) is
                                                				protocol to be used for calls between local and remote routers using the packet
                                                				network.

Step 8

session target { dns : address | ipv4 : destination-address }

##### Example:

```
Router (config-voice-dial-peer)# session target ipv4:10.5.49.80
```

Designates a
                                                				network-specific address to receive calls from the dial peer being configured.

dns : address —Specifies the DNS address of the
                                                      					 voice-mail system.

ipv4 : destination- address —Specifies the IP address of
                                                      					 the voice-mail system.

Step 9

dtmf-relay sip-notify

##### Example:

```
Router (config-voice-dial-peer)# dtmf-relay sip-notify
```

Sets the
                                                				DTMF relay method for the voice dial peer being configured.

sip-notify —
                                                      					 Forwards DTMF tones using SIP NOTIFY messages.

This
                                                      					 command can also be configured in voice-register-pool configuration mode. For
                                                      					 individual phones, the phone-level configuration for this command overrides the
                                                      					 system-level configuration for this command.

Step 10

codec g711ulaw

##### Example:

```
Router (config-voice-dial-peer)# codec g711ulaw
```

Specifies
                                                				the voice coder rate of speech for a dial peer being configured.

Step 11

no vad

##### Example:

```
Router (config-voice-dial-peer)# no vad
```

Disables
                                                				voice activity detection (VAD) for the calls using the dial peer being
                                                				configured.

Step 12

end

##### Example:

```
Router(config-voice-dial-peer)# end
```

Exits to
                                                				privileged EXEC mode.

##### What to do next

After
                                    		  configuring DTMF relay, you are ready to configure Message Waiting Indicator
                                    		  (MWI). See SCCP:
                                       			 Configuring a Phone for MWI Outcall .

### Configure a SCCP
                           	 Phone for MWI Outcall

To designate a
                                 		  phone line or directory number on an individual SCCP phone to be monitored for
                                 		  voice-mail messages, or to enable audible MWI, perform the following steps.

Restriction

Audible MWI
                                                   				  is supported only in Cisco Unified CME 4.0(2) and later versions.

Audible MWI
                                                   				  is supported only on Cisco Unified IP Phone 7931G and Cisco Unified IP
                                                   				  Phone 7911.

#### Before you begin

Directory
                                       				number and number for MWI line must be configured.

### SUMMARY STEPS

- enable

- configure terminal

- ephone phone-tag

- mwi-line line-number

- exit

- ephone-dn dn-tag

- mwi { off | on | on-off }

- mwi-type { visual | audio | both }

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
Router(config)# ephone 36
```

Enters ephone
                                             				configuration mode.

Step 4

mwi-line line-number

#### Example:

```
Router(config-ephone)# mwi-line 3
```

(Optional)
                                             				Selects a phone line to receive MWI treatment.

line-number —Number of phone line to receive MWI
                                                   					 notification. Range: 1 to 34. Default: 1.

Step 5

exit

#### Example:

```
Router(config-ephone)# exit
```

Exits ephone
                                             				configuration mode.

Step 6

ephone-dn dn-tag

#### Example:

```
Router(config)# ephone-dn 11
```

Enters
                                             				ephone-dn configuration mode.

Step 7

mwi { off | on | on-off }

#### Example:

```
Router(config-ephone-dn)# mwi on-off
```

(Optional)
                                             				Enables a specific directory number to receive MWI notification from an
                                             				external voice-messaging system.

This command
                                                         				  can also be configured in ephone-dn-template configuration mode. The value that
                                                         				  you set in ephone-dn configuration mode has priority over the value set in
                                                         				  ephone-dn-template mode.

Step 8

mwi-type { visual | audio | both }

#### Example:

```
Router(config-ephone-dn)# mwi-type audible
```

(Optional)
                                             				Specifies which type of MWI notification to be received.

This
                                                         				  command is supported only on the Cisco Unified IP Phone 7931G and Cisco Unified
                                                         				  IP Phone 7911.

This
                                                         				  command can also be configured in ephone-dn-template configuration mode. The
                                                         				  value that you set in ephone-dn configuration mode has priority over the value
                                                         				  set in ephone-dn-template mode. For configuration information, see Ephone-dn
                                                            					 Templates .

Step 9

end

#### Example:

```
Router(config-ephone-dn)# end
```

Returns to
                                             				privileged EXEC mode.

### Enable MWI at the
                           	 System-Level on SIP Phones

To enable a
                                 		  message waiting indicator (MWI) at a system-level, perform the following steps.

#### Before you begin

Cisco CME 3.4
                                       				or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- mwi reg-e164

- mwi stutter

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

mwi reg-e164

#### Example:

```
Router(config-register-global)# mwi reg-e164
```

Registers full
                                             				E.164 number to the MWI server in Cisco Unified CME and enables MWI.

Step 5

mwi stutter

#### Example:

```
Router(config-register-global)# mwi stutter
```

Enables
                                             				Cisco Unified CME router at the central site to relay MWI notification to
                                             				remote SIP phones.

Step 6

end

#### Example:

```
Router(config-register-global)# end
```

Exits to
                                             				privileged EXEC mode.

### Configure a
                           	 Directory Number for MWI on SIP Phones

Perform one of the following
                              		tasks, depending on whether you want to configure MWI outcall or MWI notify
                              		(unsolicited notify or subscribe/notify) for SIP endpoints in
                              		Cisco Unified CME.

SIP: Defining Pilot Call Back Number for MWI Outcall

SIP: Configuring a Directory Number for MWI
                                       				NOTIFY

#### Define Pilot Call
                              	 Back Number for MWI Outcall

To designate a
                                    		  phone line on an individual SIP directory number to be monitored for voice-mail
                                    		  messages, perform the following steps.

Restriction

For Cisco
                                                      				  Unified CME 4.1 and later versions, the Call Forward All, Presence, and MWI
                                                      				  features require that SIP phones must be configured with a directory number by
                                                      				  using the number command with the dn keyword;
                                                      				  direct line numbers are not supported.

##### Before you begin

Cisco CME 3.4
                                          				or a later version.

Directory
                                          				number and number for receiving MWI must be configured.

### SUMMARY STEPS

- enable

- configure terminal

- voice register dn dn-tag

- mwi

- end

### DETAILED STEPS

Step 1

enable

##### Example:

```
Router> enable
```

Enables
                                                				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

##### Example:

```
Router# configure terminal
```

Enters global
                                                				configuration mode.

Step 3

voice register dn dn-tag

##### Example:

```
Router(config)# voice register dn 1
```

Enters voice
                                                				register dn configuration mode to define a directory number for a SIP phone,
                                                				intercom line, voice port, or an MWI.

Step 4

mwi

##### Example:

```
Router(config-register-dn)# mwi
```

Enables a
                                                				specific directory number to receive MWI notification.

Step 5

end

##### Example:

```
Router(config-ephone-dn)# end
```

Exits to
                                                				privileged EXEC mode.

#### Configure a
                              	 Directory Number for MWI NOTIFY

To identify the
                                    		  MWI server and specify a directory number for receiving MWI Subscribe/NOTIFY or
                                    		  MWI Unsolicited NOTIFY, follow the steps in this section.

We recommend
                                                			 using the Subscribe/NOTIFY method instead of an Unsolicited NOTIFY when
                                                			 possible.

Restriction

For Cisco
                                                      				  Unified CME 4.1 and later versions, the Call Forward All, Presence, and MWI
                                                      				  features require that SIP phones must be configured with a directory number by
                                                      				  using the number command with the dn keyword;
                                                      				  direct line numbers are not supported.

The SIP MWI
                                                      				  - QSIG Translation feature in Cisco Unified CME 4.1 does not support Subscribe
                                                      				  NOTIFY.

Cisco Unified IP Phone 7960, 7940, 7905, and 7911 support only
                                                      				  Unsolicited NOTIFY for MWI.

##### Before you begin

Cisco CME 3.4
                                          				or a later version.

For
                                          				Cisco Unified CME 4.0 and later, QSIQ supplementary services must be configured
                                          				on the Cisco router. For information, see Enable H.450.7 and QSIG Supplementary Services at System-Level or Enable H.450.7 and QSIG Supplementary Services on a Dial Peer .

Directory
                                          				number and number for receiving MWI must be configured.

### SUMMARY STEPS

- enable

- configure terminal

- sip-ua

- mwi-server { ipv4 : destination-address | dns : host-name } [ unsolicited ]

- exit

- voice register dn dn-tag

- mwi

- end

### DETAILED STEPS

Step 1

enable

##### Example:

```
Router> enable
```

Enables
                                                				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

##### Example:

```
Router# configure terminal
```

Enters global
                                                				configuration mode.

Step 3

sip-ua

##### Example:

```
Router(config)# sip-ua
```

Enters Session
                                                				Initiation Protocol (SIP) user agent (ua) configuration mode for configuring
                                                				the user agent.

Step 4

mwi-server { ipv4 : destination-address | dns : host-name } [ unsolicited ]

##### Example:

```
Router(config-sip-ua)# mwi-server ipv4:1.5.49.200
```

or

```
Router(config-sip-ua)# mwi-server dns:server.yourcompany.com unsolicited
```

Specifies
                                                				voice-mail server settings on a voice gateway or UA.

The sip-server and mwi expires commands under the telephony-service configuration mode
                                                            				  have been migrated to mwi-server to
                                                            				  support DNS format of the SIP server.

Step 5

exit

##### Example:

```
Router(config-sip-ua)# exit
```

Exits to the
                                                				next highest mode in the configuration mode hierarchy.

Step 6

voice register dn dn-tag

##### Example:

```
Router(config)# voice register dn 1
```

Enters voice
                                                				register dn configuration mode to define a directory number for a SIP phone,
                                                				intercom line, voice port, or an MWI.

Step 7

mwi

##### Example:

```
Router(config-register-dn)# mwi
```

Enables a
                                                				specific directory number to receive MWI notification.

Step 8

end

##### Example:

```
Router(config-register-dn)# end
```

Exits to
                                                				privileged EXEC mode.

### Enable SIP MWI
                           	 Prefix Specification

To accept
                                 		  unsolicited SIP Notify messages for MWI that include a prefix string as a site
                                 		  identifier, perform the following steps.

#### Before you begin

Cisco Unified CME 4.0 or a later version.

Directory
                                       				number for receiving MWI Unsolicited NOTIFY must be configured. For
                                       				information, see SIP:
                                          				  Configuring a Directory Number for MWI NOTIFY .

### SUMMARY STEPS

- enable

- telephony-service

- mwi prefix prefix-string

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

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony-service configuration mode.

Step 3

mwi prefix prefix-string

#### Example:

```
Router(config-telephony)# mwi prefix 555
```

Specifies a
                                             				string of digits that, if present before a known Cisco Unified CME extension
                                             				number, are recognized as a prefix.

- prefix-string —Digit string. The maximum prefix
                                                				  length is 32 digits.

Step 4

end

#### Example:

```
Router(config-telephony)# end
```

Returns to
                                             				privileged EXEC mode.

### Configure VMWI on
                           	 SIP Phones

To enable a VMWI,
                                 		  perform the following steps.

#### Before you begin

Cisco IOS
                                       				Release 12.4(6)T or a later version

### SUMMARY STEPS

- enable

- configure terminal

- voice-port port

- mwi

- vmwi
                                       				  dc-voltage or vmwi fsk

- exit

- sip-ua

- mwi-server { ipv4 : destination-address | dns : host-name } [ unsolicited ]

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

voice-port port

#### Example:

```
Router(config)# voice-port 2/0
```

Enters
                                             				voice-port configuration mode.

port —Syntax is platform-dependent. Type ? to
                                                   					 determine.

Step 4

mwi

#### Example:

```
Router(config-voiceport)# mwi
```

Enables MWI
                                             				for a specified voice port.

Step 5

vmwi
                                                				  dc-voltage or vmwi fsk

#### Example:

```
Router(config-voiceport)# vmwi dc-voltage
```

(Optional)
                                             				Enables DC voltage or FSK VMWI on a Cisco VG224 onboard analog FXS voice port.

You do not
                                             				need to perform this step for the Cisco VG202 and Cisco VG204. They support FSK
                                             				only. VMWI is configured automatically when MWI is configured on the voice
                                             				port.

This step is
                                             				required for the VG224. If an FSK phone is connected to the voice port, use the fsk keyword.
                                             				If a DC voltage phone is connected to the voice port, use the dc-voltage keyword.

Step 6

exit

#### Example:

```
Router(config-sip-ua)# exit
```

Exits to the
                                             				next highest mode in the configuration mode hierarchy.

Step 7

sip-ua

#### Example:

```
Router(config)# sip-ua
```

Enters Session
                                             				Initiation Protocol user agent configuration mode for configuring the user
                                             				agent.

Step 8

mwi-server { ipv4 : destination-address | dns : host-name } [ unsolicited ]

#### Example:

```
Router(config-sip-ua)# mwi-server ipv4:1.5.49.200
```

or

```
Router(config-sip-ua)# mwi-server dns:server.yourcompany.com unsolicited
```

Specifies
                                             				voice-mail server settings on a voice gateway or user agent (ua).

The sip-server and mwi expires commands under the telephony-service configuration mode have been migrated to mwi-server to support DNS format of the Session Initiation Protocol (SIP) server.

Step 9

end

#### Example:

```
Router(config-voiceport)# end
```

Exits
                                             				voice-port configuration mode and returns to privileged EXEC mode.

### Verify Voice-Mail Integration

Press the Messages button on a local phone in Cisco
                                    			 Unified CME and listen for the voice mail greeting.

Dial an unattended local phone and listen for the voice mail
                                    			 greeting.

Leave a test message.

Go to the phone that you called. Verify that the [Message] indicator
                                    			 is lit.

Press the Messages button on this phone and retrieve the
                                    			 voice mail message.

## Configuration Examples for Voice-Mail Integration

### Example for
                           	 Setting up a Mailbox Selection Policy for SCCP Phones

The following
                                 		  example sets a policy to select the mailbox of the originally called number
                                 		  when a call is diverted to a Cisco Unity Express or PBX voice-mail system with
                                 		  the pilot number 7000.

```
dial-peer voice 7000 voip
		 destination-pattern 7000
		 session target ipv4:10.3.34.211
		 codec g711ulaw
		 no vad
		 mailbox-selection orig-called-num
```

The following
                                 		  example sets a policy to select the mailbox of the last number that the call
                                 		  was diverted to before being diverted to a Cisco Unity voice-mail system with
                                 		  the pilot number 8000.

```
ephone-dn 825
		 number 8000
		 mailbox-selection last-redirect-num
```

### Example for Configuring Voice Mailbox for SIP Phones

The following example shows how to configure the call forward b2bua
                                 		  mailbox for SIP endpoints:

```
voice register global
		 voicemail 1234
		!
		voice register dn 2
		 number 2200
		 call-forward b2bua all 1000 
		 call-forward b2bua mailbox 2200 
		 call-forward b2bua noan 2201 timeout 15
		 mwi
```

### Example for Configuring DTMF Integration Using RFC 2833

The following example shows the configuration for DTMF Relay using RFC
                                 		  2833:

```
dial-peer voice 1 voip
		 destination-pattern 4…
		 session target ipv4:10.8.17.42
		 session protocol sipv2
		 dtmf-relay sip-notify rtp-nte
```

### Example for Configuring DTMF Integration Using SIP Notify

The following example shows the configuration for DTMF using SIP
                                 		  Notify:

```
dial-peer voice 1 voip
		 destination-pattern 4…
		 session target ipv4:10.5.49.80
		 session protocol sipv2
		 dtmf-relay sip-notify
		 b2bua
```

### Example for Configuring DTMF Integration for Legacy Voice-Mail
                           	 Applications

The following example sets up DTMF integration for an analog
                                 		  voice-mail system.

```
vm-integration
		pattern direct 2 CGN *
		pattern ext-to-ext busy 7 FDN * CGN *
		pattern ext-to-ext no-answer 5 FDN * CGN *
		pattern trunk-to-ext busy 6 FDN * CGN *
		pattern trunk-to-ext no-answer 4 FDN * CGN *
```

### Example for Enabling SCCP Phone Line for MWI

Line 1—Button 1—Extension 2020

Line 2—Button 2—Extension 2021, 2022, 2023, 2024

Line 3—Button 3—Extension 2021, 2022, 2023, 2024 (rollover line)

Button 4—Unused

Line 4—Button 5—Extension 2025

```
ephone-dn 20
		 number 2020
		
		ephone-dn 21
		number 2021
		
		ephone-dn 22
		number 2022
		
		ephone-dn 23
		 number 2023
		
		ephone-dn 24
		 number 2024
		
		ephone-dn 25
		 number 2025
		
		ephone 18
		button 1:20 2o21,22,23,24,25 3x2 5:26
		 mwi-line 2
```

Line 1—Button 1—Extension 607

Button 2—Unused

Line 2—Button 3—Extension 608

Button 4—Unused

Line 3—Button 5—Extension 609

```
ephone-dn 17
		 number 607
		
		ephone-dn 18
		 number 608
		
		ephone-dn 19
		 number 609
		
		ephone 25
		 button 1:17 3:18 5:19
		 mwi-line 3
```

### Example for Configuring SIP MWI Prefix Specification

The following example identifies the SIP server for MWI notification
                                 		  at the IP address 172.16.14.22. It states that the Cisco Unified CME system
                                 		  will accept unsolicited SIP Notify messages for known mailbox numbers using the
                                 		  prefix 555.

```
sip-ua
		 mwi-server 172.16.14.22 unsolicited
		
		telephony-service
		 mwi prefix 555
```

### Example for Configuring SIP Directory Number for MWI Outcall

The following example shows an MWI callback pilot number:

```
voice register dn
		 number 9000….
		 mwi
```

### Example for Configuring SIP Directory Number for MWI Unsolicited
                           	 Notify

The following example shows how to specify voice-mail server settings
                                 		  on a UA. The example includes the unsolicited keyword, enabling the voice-mail
                                 		  server to send a SIP notification message to the UA if the mailbox status
                                 		  changes and specifies that voice dn 1, number 1234 on the SIP phone in
                                 		  Cisco Unified CME will receive the MWI notification:

```
sip-ua
		 mwi-server dns:server.yourcompany.com expires 60 port 5060 transport udp unsolicited
		
		voice register dn 1
		number 1234
		mwi
```

### Example for Configuring SIP Directory Number for MWI
                           	 Subscribe/NOTIFY

The following example shows how to define an MWI server and specify
                                 		  that directory number 1, number 1234 on a SIP phone in Cisco Unified CME is to
                                 		  receive the MWI notification:

```
sip-ua
		 mwi-server ipv4:1.5.49.200
		
		voice register dn 1
		number 1234
		mwi
```

## Feature
                        	 Information for Voice-Mail Integration

The following table
                           		provides release information about the feature or features described in this
                           		module. This table lists only the software release that introduced support for
                           		a given feature in a given software release train. Unless noted otherwise,
                           		subsequent releases of that software release train also support that feature.

Use Cisco Feature
                           		Navigator to find information about platform support and Cisco software image
                           		support. To access Cisco Feature Navigator, go to www.cisco.com/go/cfn .
                           		An account on Cisco.com is not required

Feature Name

Cisco Unified CME Version

Feature
                                          				  Information

Audible MWI

4.0(2)

Provides
                                          				  support for selecting audible, visual, or audible and visual Message Waiting
                                          				  Indicator (MWI) on supported Cisco Unified IP phones.

Cisco Unity Express AXL Enhancement

7.0(1)

Cisco Unified CME and Cisco Unity Express passwords are
                                          				  automatically synchronized. No configuration is required for this feature.

DTMF
                                          				  Integration

3.4

Added
                                          				  support for voice messaging systems connected via a SIP trunk or SIP user
                                          				  agent.

The standard
                                          				  Subscribe/NOTIFY method is preferred over an Unsolicited NOTIFY.

2.0

DTMF
                                          				  integration patterns were introduced.

Live Record

4.3

Enables IP
                                          				  phone users in a Cisco Unified CME system to record a phone conversation if
                                          				  Cisco Unity Express is the voice mail system.

Mailbox
                                          				  Selection Policy

4.0

Mailbox
                                          				  selection policy was introduced.

MWI

4.0

MWI line
                                          				  selection of a phone line other than the primary line on a SCCP phone was
                                          				  introduced.

3.4

Voice
                                          				  messaging systems (including Cisco Unity) connected via a SIP trunk or SIP user
                                          				  agent can pass a Message Waiting Indicator (MWI) that will be received and
                                          				  understood by a SIP phone directly connected to Cisco Unified CME.

SIP MWI
                                          				  Prefix Specification

4.0

SIP MWI
                                          				  prefix specification was introduced.

SIP MWI -
                                          				  QSIG Translation

4.1

Extends
                                          				  message waiting indicator (MWI) functionality for SIP MWI and QSIG MWI
                                          				  interoperation to enable sending and receiving of MWI over QSIG to PBX.

Transfer to
                                          				  Voice Mail

4.3

Enables a
                                          				  phone user to transfer a caller directly to a voice-mail extension.

| Note | When you order
                                             				Cisco Unity Express, Cisco Unity Express software and the purchased license are
                                             				installed on the module at the factory. Spare modules also ship with the
                                             				software and license installed. If you are adding Cisco Unity Express to an
                                             				existing Cisco router, you will be required to install hardware and software
                                             				components. |
|---|---|

| Note | Cisco Unified CME
                                          		  and Cisco Unity Express must both be configured before they can be integrated. |
|---|---|

| Note | The same
                                             			 telephone number is configured for voice messaging for all SCCP phones in
                                             			 Cisco Unified CME. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters voice
                                             				register global configuration mode to set parameters for all supported phones
                                             				in Cisco Unified CME. |
| Step 4 | voicemail phone-number Example: Router(config-telephony)# voice mail 0123 | Defines the
                                             				telephone number that is speed-dialed when the Messages button on a
                                             				Cisco Unified IP phone is pressed. phone-number— Same phone number is configured for
                                                   					 voice messaging for all SCCP phones in a Cisco Unified CME. |
| Step 5 | end Example: Router(config-telephony)# end | Exits to
                                             				privileged EXEC mode. |

| Restriction | In the following
                                                			 scenarios, the mailbox selection policy can fail to work properly: The last
                                                      				  redirecting endpoint is not hosted on Cisco Unified CME. This may rarely occur
                                                      				  with a PBX. A call is
                                                      				  forwarded across several SIP trunks. Multiple SIP Diversion Headers (stacking
                                                      				  hierarchy) are not supported in Cisco IOS software. A call is
                                                      				  forwarded across non-Cisco voice gateways that do not support the optional
                                                      				  H450.3 originalCalledNr field. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                                				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                                				configuration mode. |
| Step 3 | dial-peer voice tag voip or dial-peer voice tag pots Example: Router(config)# dial-peer voice 7000 voip or Router(config)# dial-peer voice 35 pots | Enters
                                                				dial-peer configuration mode. tag —identifies the dial peer. Valid entries are
                                                      					 1 to 2147483647. Note Use this
                                                            				  command on the outbound dial peer associated with the pilot number of the
                                                            				  voice-mail system. For systems using Cisco Unity Express, this is a VoIP dial
                                                            				  peer. For systems using PBX-based voice mail, this is a POTS dial peer. | Note | Use this
                                                            				  command on the outbound dial peer associated with the pilot number of the
                                                            				  voice-mail system. For systems using Cisco Unity Express, this is a VoIP dial
                                                            				  peer. For systems using PBX-based voice mail, this is a POTS dial peer. |
| Note | Use this
                                                            				  command on the outbound dial peer associated with the pilot number of the
                                                            				  voice-mail system. For systems using Cisco Unity Express, this is a VoIP dial
                                                            				  peer. For systems using PBX-based voice mail, this is a POTS dial peer. |
| Step 4 | mailbox-selection [ last-redirect-num \| orig-called-num ] Example: Router(config-dial-peer)# mailbox-selection orig-called-num | Sets a policy
                                                				for selecting a mailbox for calls that are diverted before being sent to a
                                                				voice-mail line. last-redirect-num —(PBX voice mail only) The
                                                      					 mailbox number to which the call will be sent is the last number to divert the
                                                      					 call (the number that sends the call to the voice-mail pilot number). orig-called-num —(Cisco Unity Express only) The
                                                      					 mailbox number to which the call will be sent is the number that was originally
                                                      					 dialed before the call was diverted. |
| Step 5 | end Example: Router(config-ephone-dn)# end | Returns to
                                                				privileged EXEC mode. |

| Note | Use this
                                                            				  command on the outbound dial peer associated with the pilot number of the
                                                            				  voice-mail system. For systems using Cisco Unity Express, this is a VoIP dial
                                                            				  peer. For systems using PBX-based voice mail, this is a POTS dial peer. |
|---|---|

| Restriction | This feature
                                                			 might not work properly in certain network topologies, including when: The last
                                                      				  redirecting endpoint is not hosted on Cisco Unified CME. This may rarely occur
                                                      				  with a PBX. A call is
                                                      				  forwarded across several SIP trunks. Multiple SIP Diversion Headers (stacking
                                                      				  hierarchy) are not supported in Cisco IOS software. A call is
                                                      				  forwarded across other voice gateways that do not support the optional H450.3
                                                      				  originalCalledNr field. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                                				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                                				configuration mode. |
| Step 3 | exit Example: Router(config-dial-peer)# exit | Exits
                                                				dial-peer configuration mode. |
| Step 4 | ephone-dn dn-tag Example: Router(config)# ephone-dn 752 | Enters
                                                				ephone-dn configuration mode. |
| Step 5 | mailbox-selection [ last-redirect-num ] Example: Router(config-ephone-dn)# mailbox-selection last-redirect-num | Sets a policy
                                                				for selecting a mailbox for calls that are diverted before being sent to a
                                                				Cisco Unity voice-mail pilot number. |
| Step 6 | end Example: Router(config-ephone-dn)# end | Returns to
                                                				privileged EXEC mode. |

| Restriction | The TrnsfVM
                                             			 softkey is not supported on the Cisco Unified IP Phone 7905, 7912, or 7921, or
                                             			 analog phones connected to the Cisco VG224 or Cisco ATA. These phones support
                                             			 the trnsfvm FAC. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-template template-tag Example: Router(config)# ephone-template 5 | Enters
                                             				ephone-template configuration mode to create an ephone template. template-tag —Unique identifier for the ephone
                                                   					 template. Range: 1 to 20. |
| Step 4 | softkeys connected {[ Acct ] [ ConfList ] [ Confrn ] [ Endcall ] [ Flash ] [ HLog ] [ Hold ] [ Join ] [ LiveRcd ] [ Park ] [ RmLstC ] [ Select ] [ TrnsfVM ] [ Trnsfer ]} Example: Router(config-ephone-template)# softkeys connected TrnsfVM Park Acct ConfList Confrn Endcall Trnsfer Hold | (Optional)
                                             				Modifies the order and type of softkeys that display on an IP phone during the
                                             				connected call state. You can
                                                   					 enter any of the keywords in any order. Default is
                                                   					 all softkeys are displayed in alphabetical order. Any
                                                   					 softkey that is not explicitly defined is disabled. |
| Step 5 | exit Example: Router(config-ephone-template)# exit | Exits
                                             				ephone-template configuration mode. |
| Step 6 | ephone phone-tag Example: Router(config)# ephone 12 | Enters ephone
                                             				configuration mode. phone-tag —Unique number that identifies this
                                                   					 ephone during configuration tasks. |
| Step 7 | ephone-template template-tag Example: Router(config-ephone)# ephone-template 5 | Applies the
                                             				ephone template to the phone. template-tag —Unique identifier of the ephone
                                                   					 template that you created in Step 3 . |
| Step 8 | exit Example: Router(config-ephone)# exit | Exits ephone
                                             				configuration mode. |
| Step 9 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 10 | voicemail phone-number Example: Router(config-telephony)# voicemail 8900 | Defines the
                                             				telephone number that is speed-dialed when the Messages button on a
                                             				Cisco Unified IP phone is pressed. phone-number —Same phone number is configured for
                                                   					 voice messaging for all SCCP phones in a Cisco Unified CME. |
| Step 11 | fac { standard \| custom
                                                				  trnsfvm custom-fac } Example: Router(config-telephony)# fac custom trnsfvm #22 | Enables
                                             				standard FACs or creates a custom FAC or alias. standard —Enables standard FACs for all phones.
                                                   					 Standard FAC for transfer to voice mail is *6. custom —Creates a custom FAC for a FAC type. custom-fac —User-defined code to be dialed using
                                                   					 the keypad on an IP or analog phone. Custom FAC can be up to 256 characters
                                                   					 long and contain numbers 0 to  9 and * and #. |
| Step 12 | end Example: Router(config-telephony)# end | Returns to
                                             				privileged EXEC mode. |

| Restriction | Only one
                                                   				  live record session is allowed for each conference. Only the
                                                   				  conference creator can initiate a live record session. In an ad hoc conference,
                                                   				  participants who are not the conference creator cannot start a live record
                                                   				  session. In a two-party call, the party who starts the live record session is
                                                   				  the conference creator. |
|---|---|

| Note | For legal
                                             			 disclaimer information about this feature, see copyright information section. |
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
| Step 4 | live record number Example: Router(config-telephony)# live record 8900 | Defines the
                                             				extension number that is dialed when the LiveRcd softkey is pressed on an SCCP
                                             				IP phone. |
| Step 5 | voicemail number Example: Router(config-telephony)# voicemail 8000 | Defines the
                                             				extension number that is speed-dialed when the Messages button is pressed on an
                                             				IP phone. Number —Cisco Unity Express voice-mail pilot
                                                   					 number. |
| Step 6 | exit Example: Router(config-telephony)# exit | Exits
                                             				telephony-service configuration mode. |
| Step 7 | ephone-dn dn-tag Example: Router(config)# ephone-dn 10 | Creates a
                                             				directory number that forwards all calls to the Cisco Unity Express voice-mail
                                             				pilot number. |
| Step 8 | number number [ secondary number ] [ no-reg [ both \| primary ]] Example: Router(config-ephone-dn)# number 8900 | Assigns an
                                             				extension number to this directory number. Number —Must
                                                   					 match the Live Record pilot-number configured in Step 4 . |
| Step 9 | call-forward all target-number Example: Router(config-ephone-dn)# call-forward all 8000 | Forwards all
                                             				calls to this extension to the specified voice-mail number. target-number —Phone number to which calls are
                                                   					 forwarded. Must match the voice-mail pilot number configured in Step 5 . Note Phone
                                                         				  users can activate and cancel the call-forward-all state from the phone using
                                                         				  the CFwdAll softkey or a FAC. | Note | Phone
                                                         				  users can activate and cancel the call-forward-all state from the phone using
                                                         				  the CFwdAll softkey or a FAC. |
| Note | Phone
                                                         				  users can activate and cancel the call-forward-all state from the phone using
                                                         				  the CFwdAll softkey or a FAC. |
| Step 10 | exit Example: Router(config-ephone-dn)# exit | Exits
                                             				ephone-dn configuration mode. |
| Step 11 | ephone-template template-tag Example: Router(config)# ephone-template 5 | Enters
                                             				ephone-template configuration mode to create an ephone template. template-tag —Unique identifier for the ephone
                                                   					 template. Range: 1 to 20. |
| Step 12 | softkeys connected {[ Acct ] [ ConfList ] [ Confrn ] [ Endcall ] [ Flash ] [ HLog ] [ Hold ] [ Join ] [ LiveRcd ] [ Park ] [ RmLstC ] [ Select ] [ TrnsfVM ] [ Trnsfer ]} Example: Router(config-ephone-template)# softkeys connected LiveRcd Confrn Hold Park Trnsfer TrnsfVM | Modifies the
                                             				order and type of softkeys that display on an IP phone during the connected
                                             				call state. |
| Step 13 | exit Example: Router(config-ephone-template)# exit | Exits
                                             				ephone-template configuration mode. |
| Step 14 | ephone phone-tag Example: Router(config)# ephone 12 | Enters
                                             				ephone configuration mode. phone-tag —Unique number that identifies this
                                                   					 ephone during configuration tasks. |
| Step 15 | ephone-template template-tag Example: Router(config-ephone)# ephone-template 5 | Applies the
                                             				ephone template to the phone. template-tag —Unique identifier of the ephone
                                                   					 template that you created in Step 11 . |
| Step 16 | end Example: Router(config-ephone)# end | Exits to
                                             				privileged EXEC mode. |

| Note | Phone
                                                         				  users can activate and cancel the call-forward-all state from the phone using
                                                         				  the CFwdAll softkey or a FAC. |
|---|---|

| Note | The same
                                             			 telephone number is configured for voice messaging for all SIP phones in
                                             			 Cisco Unified CME. The call forward
                                                   				  b2bua command enables call forwarding and designates that calls
                                             			 that are forwarded to a busy or no-answer extension be sent to a voicemail box. |
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
| Step 4 | voicemail phone-number Example: Router(config-register-global)# voice mail 1111 | Defines the
                                             				telephone number that is speed-dialed when the Messages button on a
                                             				Cisco Unified IP phone is pressed. phone-number— Same phone number is configured for
                                                   					 voice messaging for all SIP phones in a Cisco Unified CME. |
| Step 5 | exit Example: Router(config-register-global)# exit | Exits voice
                                             				register global configuration mode. |
| Step 6 | voice register dn dn-tag Example: Router(config)# voice register dn 2 | Enters voice
                                             				register dn mode to define a directory number for a SIP phone, intercom line,
                                             				voice port, or an MWI. |
| Step 7 | call-forward b2bua busy directory-number Example: Router(config-register-dn)# call-forward b2bua busy 1000 | Enables call
                                             				forwarding for a SIP back-to-back user agent so that incoming calls to an
                                             				extension that is busy will be forwarded to the designated directory number. |
| Step 8 | call-forward b2bua mailbox directory-number Example: Router(config-register-dn)# call-forward b2bua mailbox 2200 | Designates the
                                             				voice mailbox to use at the end of a chain of call forwards. Incoming
                                                   					 calls have been forwarded to a busy or no-answer extension will be forwarded to
                                                   					 the directory-number specified. |
| Step 9 | call-forward b2bua noan directory-number timeout seconds Example: Router(config-register-dn)# call-forward b2bua noan 2201 timeout 15 | Enables call
                                             				forwarding for a SIP back-to-back user agent so that incoming calls to an
                                             				extension that does not answer will be forwarded to the designated directory
                                             				number. seconds —Number of seconds that a call can ring
                                                   					 with no answer before the call is forwarded to another extension. Range: 3 to
                                                   					 60000. Default: 20. |
| Step 10 | end Example: Router(config-register-dn)# end | Exits to
                                             				privileged EXEC mode. |

| Note | You can
                                                			 configure multiple tags and tokens for each pattern, depending on the
                                                			 voice-mail system and type of access. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                                				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                                				configuration mode. |
| Step 3 | vm-integration Example: Router(config) vm-integration | Enters
                                                				voice-mail integration configuration mode and enables voice-mail integration
                                                				with DTMF and an analog voice-mail system. |
| Step 4 | pattern direct tag1 { CGN \| CDN \| FDN } [ tag2 { CGN \| CDN \| FDN }] [ tag3 { CGN \| CDN \| FDN }] [ last-tag ] Example: Router(config-vm-integration) pattern direct 2 CGN * | Configures the
                                                				DTMF digit pattern forwarding necessary to activate the voice-mail system when
                                                				the user presses the messages button on the phone. The tag attribute
                                                      					 is an alphanumeric string fewer than four DTMF digits in length. The
                                                      					 alphanumeric string consists of a combination of four letters (A, B, C, and D),
                                                      					 two symbols (* and #), and ten digits (0 to 9). The tag numbers match the
                                                      					 numbers defined in the voice-mail system’s integration file, immediately
                                                      					 preceding either the number of the calling party, the number of the called
                                                      					 party, or a forwarding number. The
                                                      					 keywords, CGN , CDN , and FDN ,
                                                      					 configure the type of call information sent to the voice-mail system, such as
                                                      					 calling number (CGN), called number (CDN), or forwarding number (FDN). |
| Step 5 | pattern ext-to-ext busy tag1 { CGN \| CDN \| FDN } [ tag2 { CGN \| CDN \| FDN }] [ tag3 { CGN \| CDN \| FDN }] [ last-tag ] Example: Router(config-vm-integration) pattern ext-to-ext busy 7 FDN * CGN * | Configures
                                                				the DTMF digit pattern forwarding necessary to activate the voice-mail system
                                                				when an internal extension attempts to connect to a busy extension and the call
                                                				is forwarded to voice mail. |
| Step 6 | pattern ext-to-ext
                                                   				  no-answer tag1 { CGN \| CDN \| FDN } [ tag2 { CGN \| CDN \| FDN }] [ tag3 { CGN \| CDN \| FDN }] [ last-tag ] Example: Router(config-vm-integration) pattern ext-to-ext no-answer 5 FDN * CGN * | Configures
                                                				the DTMF digit pattern forwarding necessary to activate the voice-mail system
                                                				when an internal extension fails to connect to an extension and the call is
                                                				forwarded to voice mail. |
| Step 7 | pattern trunk-to-ext busy tag1 { CGN \| CDN \| FDN } [ tag2 { CGN \| CDN \| FDN }] [ tag3 { CGN \| CDN \| FDN }] [ last-tag ] Example: Router(config-vm-integration) pattern trunk-to-ext busy 6 FDN * CGN * | Configures
                                                				the DTMF digit pattern forwarding necessary to activate the voice-mail system
                                                				when an external trunk call reaches a busy extension and the call is forwarded
                                                				to voice mail. |
| Step 8 | pattern trunk-to-ext
                                                   				  no-answer tag1 { CGN \| CDN \| FDN } [ tag2 { CGN \| CDN \| FDN }] [ tag3 { CGN \| CDN \| FDN }] [ last-tag ] Example: Router(config-vm-integration)# pattern trunk-to-ext no-answer 4 FDN * CGN * | Configures
                                                				the DTMF digit pattern forwarding necessary to activate the voice-mail system
                                                				when an external trunk call reaches an unanswered extension and the call is
                                                				forwarded to voice mail. |
| Step 9 | end Example: Router(config-vm-integration)# exit | Exits
                                                				configuration mode and enters privileged EXEC mode. |

| Note | If the T.38 Fax
                                                			 Relay feature is also configured on this IP network, we recommend that you
                                                			 either configure the voice gateways to use a payload type other than PT96 or
                                                			 PT97 for fax relay negotiation, or depending on whether the SIP endpoints
                                                			 support different payload types, configure Cisco Unified CME to use a payload
                                                			 type other than PT96 or PT97 for DTMF. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                                				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                                				configuration mode. |
| Step 3 | dial-peer voice tag voip Example: Router (config)# dial-peer voice 123 voip | Enters
                                                				dial-peer configuration mode to define a VoIP dial peer for the voice-mail
                                                				system. tag —Defines the dial peer being configured. Range
                                                      					 is 1 to 2147483647. |
| Step 4 | description string Example: Router (config-voice-dial-peer)# description CU pilot | (Optional)
                                                				Associates a description with the dial peer being configured. Enter a string of
                                                				up to 64 characters. |
| Step 5 | destination-pattern string Example: Router (config-voice-dial-peer)# destination-pattern 20 | Specifies the
                                                				pattern of the numbers that the user must dial to place a call. string —Prefix or full E.164 number. |
| Step 6 | session protocol sipv2 Example: Router (config-voice-dial-peer)# session protocol sipv2 | Specifies that
                                                				Internet Engineering Task Force (IETF) Session Initiation Protocol (SIP) is
                                                				protocol to be used for calls between local and remote routers using the packet
                                                				network. |
| Step 7 | session target { dns : address \| ipv4 : destination-address } Example: Router (config-voice-dial-peer)# session target ipv4:10.8.17.42 | Designates a
                                                				network-specific address to receive calls from the dial peer being configured. dns : address —Specifies the DNS address of the
                                                      					 voice-mail system. ipv4 : destination-
                                                            						  address —Specifies the IP address of the voice-mail system. |
| Step 8 | dtmf-relay
                                                   				  rtp-nte Example: Router (config-voice-dial-peer)# dtmf-relay rtp-nte | Sets DTMF
                                                				relay method for the voice dial peer being configured. rtp-nte —
                                                      					 Provides conversion from the out-of-band SCCP indication to the SIP standard
                                                      					 for DTMF relay (RFC 2833). Forwards DTMF tones by using Real-Time Transport
                                                      					 Protocol (RTP) with the Named Telephone Event (NTE) payload type. This
                                                      					 command can also be configured in voice-register-pool configuration mode. For
                                                      					 individual phones, the phone-level configuration for this command overrides the
                                                      					 system-level configuration for this command. Note The need
                                                            				  to use out-of-band conversion is limited to SCCP phones. SIP phones natively
                                                            				  support in-band. | Note | The need
                                                            				  to use out-of-band conversion is limited to SCCP phones. SIP phones natively
                                                            				  support in-band. |
| Note | The need
                                                            				  to use out-of-band conversion is limited to SCCP phones. SIP phones natively
                                                            				  support in-band. |
| Step 9 | dtmf-interworking
                                                   				  rtp-nte Example: Router (config-voice-dial-peer)# dtmf-interworking rtp-nte | (Optional)
                                                				Enables a delay between the dtmf-digit begin and dtmf-digit end events in the
                                                				RFC 2833 packets. This
                                                      					 command is supported in Cisco IOS Release 12.4(15)XZ and later releases and in
                                                      					 Cisco Unified CME 4.3 and later versions. This
                                                      					 command can also be configured in voice-service configuration mode. |
| Step 10 | end Example: Router(config-voice-dial-peer)# end | Exits to
                                                				privileged EXEC mode. |

| Note | The need
                                                            				  to use out-of-band conversion is limited to SCCP phones. SIP phones natively
                                                            				  support in-band. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                                				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal# | Enters global
                                                				configuration mode. |
| Step 3 | dial-peer voice tag voip Example: Router (config)# dial-peer voice 2 voip | Enters
                                                				dial-peer configuration mode to define a VoIP dial peer for the voice-mail
                                                				system. tag —Defines the dial peer being configured. Range
                                                      					 is 1 to 2147483647. |
| Step 4 | description string Example: Router (config-voice-dial-peer)# description cue pilot | (Optional)
                                                				Associates a description with the dial peer being configured. Enter a string of
                                                				up to 64 characters. |
| Step 5 | destination-pattern string Example: Router (config-voice-dial-peer)# destination-pattern 20 | Specifies the
                                                				pattern of the numbers that the user must dial to place a call. string —Prefix or full E.164 number. |
| Step 6 | b2bua Example: Router (config-voice-dial-peer)# b2bua | (Optional)
                                                				Includes the Cisco Unified CME address as part of contact in 3XX response to
                                                				point to Cisco Unity Express and enables SIP-to-SCCP call forward. |
| Step 7 | session protocol sipv2 Example: Router (config-voice-dial-peer)# session protocol sipv2 | Specifies that
                                                				Internet Engineering Task Force (IETF) Session Initiation Protocol (SIP) is
                                                				protocol to be used for calls between local and remote routers using the packet
                                                				network. |
| Step 8 | session target { dns : address \| ipv4 : destination-address } Example: Router (config-voice-dial-peer)# session target ipv4:10.5.49.80 | Designates a
                                                				network-specific address to receive calls from the dial peer being configured. dns : address —Specifies the DNS address of the
                                                      					 voice-mail system. ipv4 : destination- address —Specifies the IP address of
                                                      					 the voice-mail system. |
| Step 9 | dtmf-relay sip-notify Example: Router (config-voice-dial-peer)# dtmf-relay sip-notify | Sets the
                                                				DTMF relay method for the voice dial peer being configured. sip-notify —
                                                      					 Forwards DTMF tones using SIP NOTIFY messages. This
                                                      					 command can also be configured in voice-register-pool configuration mode. For
                                                      					 individual phones, the phone-level configuration for this command overrides the
                                                      					 system-level configuration for this command. |
| Step 10 | codec g711ulaw Example: Router (config-voice-dial-peer)# codec g711ulaw | Specifies
                                                				the voice coder rate of speech for a dial peer being configured. |
| Step 11 | no vad Example: Router (config-voice-dial-peer)# no vad | Disables
                                                				voice activity detection (VAD) for the calls using the dial peer being
                                                				configured. |
| Step 12 | end Example: Router(config-voice-dial-peer)# end | Exits to
                                                				privileged EXEC mode. |

| Restriction | Audible MWI
                                                   				  is supported only in Cisco Unified CME 4.0(2) and later versions. Audible MWI
                                                   				  is supported only on Cisco Unified IP Phone 7931G and Cisco Unified IP
                                                   				  Phone 7911. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone phone-tag Example: Router(config)# ephone 36 | Enters ephone
                                             				configuration mode. |
| Step 4 | mwi-line line-number Example: Router(config-ephone)# mwi-line 3 | (Optional)
                                             				Selects a phone line to receive MWI treatment. line-number —Number of phone line to receive MWI
                                                   					 notification. Range: 1 to 34. Default: 1. |
| Step 5 | exit Example: Router(config-ephone)# exit | Exits ephone
                                             				configuration mode. |
| Step 6 | ephone-dn dn-tag Example: Router(config)# ephone-dn 11 | Enters
                                             				ephone-dn configuration mode. |
| Step 7 | mwi { off \| on \| on-off } Example: Router(config-ephone-dn)# mwi on-off | (Optional)
                                             				Enables a specific directory number to receive MWI notification from an
                                             				external voice-messaging system. Note This command
                                                         				  can also be configured in ephone-dn-template configuration mode. The value that
                                                         				  you set in ephone-dn configuration mode has priority over the value set in
                                                         				  ephone-dn-template mode. | Note | This command
                                                         				  can also be configured in ephone-dn-template configuration mode. The value that
                                                         				  you set in ephone-dn configuration mode has priority over the value set in
                                                         				  ephone-dn-template mode. |
| Note | This command
                                                         				  can also be configured in ephone-dn-template configuration mode. The value that
                                                         				  you set in ephone-dn configuration mode has priority over the value set in
                                                         				  ephone-dn-template mode. |
| Step 8 | mwi-type { visual \| audio \| both } Example: Router(config-ephone-dn)# mwi-type audible | (Optional)
                                             				Specifies which type of MWI notification to be received. Note This
                                                         				  command is supported only on the Cisco Unified IP Phone 7931G and Cisco Unified
                                                         				  IP Phone 7911. Note This
                                                         				  command can also be configured in ephone-dn-template configuration mode. The
                                                         				  value that you set in ephone-dn configuration mode has priority over the value
                                                         				  set in ephone-dn-template mode. For configuration information, see Ephone-dn
                                                            					 Templates . | Note | This
                                                         				  command is supported only on the Cisco Unified IP Phone 7931G and Cisco Unified
                                                         				  IP Phone 7911. | Note | This
                                                         				  command can also be configured in ephone-dn-template configuration mode. The
                                                         				  value that you set in ephone-dn configuration mode has priority over the value
                                                         				  set in ephone-dn-template mode. For configuration information, see Ephone-dn
                                                            					 Templates . |
| Note | This
                                                         				  command is supported only on the Cisco Unified IP Phone 7931G and Cisco Unified
                                                         				  IP Phone 7911. |
| Note | This
                                                         				  command can also be configured in ephone-dn-template configuration mode. The
                                                         				  value that you set in ephone-dn configuration mode has priority over the value
                                                         				  set in ephone-dn-template mode. For configuration information, see Ephone-dn
                                                            					 Templates . |
| Step 9 | end Example: Router(config-ephone-dn)# end | Returns to
                                             				privileged EXEC mode. |

| Note | This command
                                                         				  can also be configured in ephone-dn-template configuration mode. The value that
                                                         				  you set in ephone-dn configuration mode has priority over the value set in
                                                         				  ephone-dn-template mode. |
|---|---|

| Note | This
                                                         				  command is supported only on the Cisco Unified IP Phone 7931G and Cisco Unified
                                                         				  IP Phone 7911. |
|---|---|

| Note | This
                                                         				  command can also be configured in ephone-dn-template configuration mode. The
                                                         				  value that you set in ephone-dn configuration mode has priority over the value
                                                         				  set in ephone-dn-template mode. For configuration information, see Ephone-dn
                                                            					 Templates . |
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
| Step 4 | mwi reg-e164 Example: Router(config-register-global)# mwi reg-e164 | Registers full
                                             				E.164 number to the MWI server in Cisco Unified CME and enables MWI. |
| Step 5 | mwi stutter Example: Router(config-register-global)# mwi stutter | Enables
                                             				Cisco Unified CME router at the central site to relay MWI notification to
                                             				remote SIP phones. |
| Step 6 | end Example: Router(config-register-global)# end | Exits to
                                             				privileged EXEC mode. |

| Restriction | For Cisco
                                                      				  Unified CME 4.1 and later versions, the Call Forward All, Presence, and MWI
                                                      				  features require that SIP phones must be configured with a directory number by
                                                      				  using the number command with the dn keyword;
                                                      				  direct line numbers are not supported. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                                				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                                				configuration mode. |
| Step 3 | voice register dn dn-tag Example: Router(config)# voice register dn 1 | Enters voice
                                                				register dn configuration mode to define a directory number for a SIP phone,
                                                				intercom line, voice port, or an MWI. |
| Step 4 | mwi Example: Router(config-register-dn)# mwi | Enables a
                                                				specific directory number to receive MWI notification. |
| Step 5 | end Example: Router(config-ephone-dn)# end | Exits to
                                                				privileged EXEC mode. |

| Note | We recommend
                                                			 using the Subscribe/NOTIFY method instead of an Unsolicited NOTIFY when
                                                			 possible. |
|---|---|

| Restriction | For Cisco
                                                      				  Unified CME 4.1 and later versions, the Call Forward All, Presence, and MWI
                                                      				  features require that SIP phones must be configured with a directory number by
                                                      				  using the number command with the dn keyword;
                                                      				  direct line numbers are not supported. The SIP MWI
                                                      				  - QSIG Translation feature in Cisco Unified CME 4.1 does not support Subscribe
                                                      				  NOTIFY. Cisco Unified IP Phone 7960, 7940, 7905, and 7911 support only
                                                      				  Unsolicited NOTIFY for MWI. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                                				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                                				configuration mode. |
| Step 3 | sip-ua Example: Router(config)# sip-ua | Enters Session
                                                				Initiation Protocol (SIP) user agent (ua) configuration mode for configuring
                                                				the user agent. |
| Step 4 | mwi-server { ipv4 : destination-address \| dns : host-name } [ unsolicited ] Example: Router(config-sip-ua)# mwi-server ipv4:1.5.49.200 or Router(config-sip-ua)# mwi-server dns:server.yourcompany.com unsolicited | Specifies
                                                				voice-mail server settings on a voice gateway or UA. Note The sip-server and mwi expires commands under the telephony-service configuration mode
                                                            				  have been migrated to mwi-server to
                                                            				  support DNS format of the SIP server. | Note | The sip-server and mwi expires commands under the telephony-service configuration mode
                                                            				  have been migrated to mwi-server to
                                                            				  support DNS format of the SIP server. |
| Note | The sip-server and mwi expires commands under the telephony-service configuration mode
                                                            				  have been migrated to mwi-server to
                                                            				  support DNS format of the SIP server. |
| Step 5 | exit Example: Router(config-sip-ua)# exit | Exits to the
                                                				next highest mode in the configuration mode hierarchy. |
| Step 6 | voice register dn dn-tag Example: Router(config)# voice register dn 1 | Enters voice
                                                				register dn configuration mode to define a directory number for a SIP phone,
                                                				intercom line, voice port, or an MWI. |
| Step 7 | mwi Example: Router(config-register-dn)# mwi | Enables a
                                                				specific directory number to receive MWI notification. |
| Step 8 | end Example: Router(config-register-dn)# end | Exits to
                                                				privileged EXEC mode. |

| Note | The sip-server and mwi expires commands under the telephony-service configuration mode
                                                            				  have been migrated to mwi-server to
                                                            				  support DNS format of the SIP server. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 3 | mwi prefix prefix-string Example: Router(config-telephony)# mwi prefix 555 | Specifies a
                                             				string of digits that, if present before a known Cisco Unified CME extension
                                             				number, are recognized as a prefix. prefix-string —Digit string. The maximum prefix
                                                				  length is 32 digits. |
| Step 4 | end Example: Router(config-telephony)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice-port port Example: Router(config)# voice-port 2/0 | Enters
                                             				voice-port configuration mode. port —Syntax is platform-dependent. Type ? to
                                                   					 determine. |
| Step 4 | mwi Example: Router(config-voiceport)# mwi | Enables MWI
                                             				for a specified voice port. |
| Step 5 | vmwi
                                                				  dc-voltage or vmwi fsk Example: Router(config-voiceport)# vmwi dc-voltage | (Optional)
                                             				Enables DC voltage or FSK VMWI on a Cisco VG224 onboard analog FXS voice port. You do not
                                             				need to perform this step for the Cisco VG202 and Cisco VG204. They support FSK
                                             				only. VMWI is configured automatically when MWI is configured on the voice
                                             				port. This step is
                                             				required for the VG224. If an FSK phone is connected to the voice port, use the fsk keyword.
                                             				If a DC voltage phone is connected to the voice port, use the dc-voltage keyword. |
| Step 6 | exit Example: Router(config-sip-ua)# exit | Exits to the
                                             				next highest mode in the configuration mode hierarchy. |
| Step 7 | sip-ua Example: Router(config)# sip-ua | Enters Session
                                             				Initiation Protocol user agent configuration mode for configuring the user
                                             				agent. |
| Step 8 | mwi-server { ipv4 : destination-address \| dns : host-name } [ unsolicited ] Example: Router(config-sip-ua)# mwi-server ipv4:1.5.49.200 or Router(config-sip-ua)# mwi-server dns:server.yourcompany.com unsolicited | Specifies
                                             				voice-mail server settings on a voice gateway or user agent (ua). Note The sip-server and mwi expires commands under the telephony-service configuration mode have been migrated to mwi-server to support DNS format of the Session Initiation Protocol (SIP) server. | Note | The sip-server and mwi expires commands under the telephony-service configuration mode have been migrated to mwi-server to support DNS format of the Session Initiation Protocol (SIP) server. |
| Note | The sip-server and mwi expires commands under the telephony-service configuration mode have been migrated to mwi-server to support DNS format of the Session Initiation Protocol (SIP) server. |
| Step 9 | end Example: Router(config-voiceport)# end | Exits
                                             				voice-port configuration mode and returns to privileged EXEC mode. |

| Note | The sip-server and mwi expires commands under the telephony-service configuration mode have been migrated to mwi-server to support DNS format of the Session Initiation Protocol (SIP) server. |
|---|---|

| Feature Name | Cisco Unified CME Version | Feature
                                          				  Information |
|---|---|---|
| Audible MWI | 4.0(2) | Provides
                                          				  support for selecting audible, visual, or audible and visual Message Waiting
                                          				  Indicator (MWI) on supported Cisco Unified IP phones. |
| Cisco Unity Express AXL Enhancement | 7.0(1) | Cisco Unified CME and Cisco Unity Express passwords are
                                          				  automatically synchronized. No configuration is required for this feature. |
| DTMF
                                          				  Integration | 3.4 | Added
                                          				  support for voice messaging systems connected via a SIP trunk or SIP user
                                          				  agent. The standard
                                          				  Subscribe/NOTIFY method is preferred over an Unsolicited NOTIFY. |
| 2.0 | DTMF
                                          				  integration patterns were introduced. |
| Live Record | 4.3 | Enables IP
                                          				  phone users in a Cisco Unified CME system to record a phone conversation if
                                          				  Cisco Unity Express is the voice mail system. |
| Mailbox
                                          				  Selection Policy | 4.0 | Mailbox
                                          				  selection policy was introduced. |
| MWI | 4.0 | MWI line
                                          				  selection of a phone line other than the primary line on a SCCP phone was
                                          				  introduced. |
| 3.4 | Voice
                                          				  messaging systems (including Cisco Unity) connected via a SIP trunk or SIP user
                                          				  agent can pass a Message Waiting Indicator (MWI) that will be received and
                                          				  understood by a SIP phone directly connected to Cisco Unified CME. |
| SIP MWI
                                          				  Prefix Specification | 4.0 | SIP MWI
                                          				  prefix specification was introduced. |
| SIP MWI -
                                          				  QSIG Translation | 4.1 | Extends
                                          				  message waiting indicator (MWI) functionality for SIP MWI and QSIG MWI
                                          				  interoperation to enable sending and receiving of MWI over QSIG to PBX. |
| Transfer to
                                          				  Voice Mail | 4.3 | Enables a
                                          				  phone user to transfer a caller directly to a voice-mail extension. |