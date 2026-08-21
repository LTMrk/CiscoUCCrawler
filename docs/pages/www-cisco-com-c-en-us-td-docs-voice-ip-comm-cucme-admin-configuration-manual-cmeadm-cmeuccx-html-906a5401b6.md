---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmeuccx-html-906a5401b6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmeuccx.html
retrieved_at: 2026-08-21T07:25:25.863085+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Interoperability
	 with Cisco Unified CCX

## Chapter: Interoperability
	 with Cisco Unified CCX

# Interoperability
                     	 with Cisco Unified CCX

This chapter
                        		describes features in Cisco Unified Communications Manager Express
                        		(Cisco Unified CME) that provide support for interoperability between
                        		Cisco Unified CME and external feature services, such as Cisco Customer
                        		Response Solutions (CRS) with Cisco Unified Contact Center Express
                        		(Cisco Unified CCX).

## Information About
                        	 Interoperability with Cisco Unified CCX

Unified CME 4.2 to Unified CME 8.5 Release versions support interoperability between Cisco Unified CME and Cisco Customer
                           Response Solutions (CRS) with Cisco Unified Call Center Express (Cisco Unified CCX), including enhanced call processing, device
                           and call monitoring, unattended call transfers to multiple call center agents and basic extension mobility, and IP IVR applications.

For Unified CME 8.6 and later releases, CRS with Unified CCX is not supported.

The
                           		Cisco Unified CCX application uses the CRS platform to provide a multimedia
                           		(voice, data, and web). Cisco IP IVR functionality is available with
                           		Cisco Unified CCX and includes prompt-and-collect and call treatment.

Support of Cisco Unified CCX Cisco Agent Desktop for use with Cisco Unified CME

Configuration query and update between Cisco Unified CCX and Cisco Unified CME

SIP-based simple and supplementary call control services including:

Call routing between Cisco Unified CME and Cisco Unified CCX using SIP-based route point

First-party call control for SIP-based simple and supplementary calls

Call monitoring and device monitoring based on SIP presence and dialog event package

Cisco Unified CCX session management of Cisco Unified CME

Cisco Unified CCX device and call monitoring of agent lines and call activities in Cisco Unified CME

Provisioning and
                           		configuration information in Cisco Unified CCX is automatically provided to
                           		Cisco United CME. If the configuration from Cisco Unified CCX is deleted or
                           		must be modified, you can configure the same information in Cisco Unified CME
                           		by using Cisco IOS commands.

For first party call
                           		control, a route point for Cisco CRS is a peer device to Cisco Unified CME
                           		through a SIP trunk. An incoming call to Cisco Unified CME that is targeted to
                           		a call center phone is routed to Cisco Unified CCX through the route point. The
                           		call is placed in a queue and redirected to the most suitable agent by
                           		Cisco Unified CCX.

Supplementary
                           		services such as call hold, blind transfer, and semi-attended transfer are
                           		initiated by Cisco Unified CCX. Existing SIP-based simple and supplementary
                           		service call flow applies except for blind transfers. For blind transfers with
                           		Cisco Unified CCX as the transferrer, Cisco Unified CCX will stay in the active
                           		state until the transfer target answers. It drops out only after the
                           		transferred call is successfully answered. If the transfer target does not
                           		answer when ringing times out, the call is pulled back by Cisco Unified CCX and
                           		rerouted to another agent. This mechanism also applies when the transfer target
                           		is configured with call-forward all or forward no-answer. The forward
                           		configuration is ignored during blind transfer.

When a call moves
                           		between Cisco Unified CCX and Cisco Unified CME because of redirect, transfer,
                           		and conference, the SIP Call-ID continues to change. For call control purposes,
                           		Cisco Unified CME issues a unique Global Call ID (Gcid) for every outbound call
                           		leg. A Gcid remains the same for all legs of the same call in the system, and
                           		is valid for redirect, transfer, and conference events, including 3-party
                           		conferencing when a call center phone acts as a conference host.

Before Cisco IOS
                           		Release 12.4(11)XW6, if the call monitoring module in Cisco Unified CME 4.2
                           		detected a call associated with a non default session application, such as
                           		B-ACD or a TCL script, the module was globally disabled. After the module was
                           		disabled, Cisco Unified CCX administration had to manually re-enable the call
                           		monitoring module after the session completes.

In Cisco IOS Release
                           		12.4(11)XW6 and later releases, the call monitoring module in Cisco Unified CME
                           		does not monitor a call associated with a non default session application, such
                           		as B-ACD or a TCL script, including all calls merged into this call by way of
                           		consult transfer and conference. The module is not disabled and continues to
                           		monitor other calls.

Table 1 contains a list of tasks required to enable operability between
                           		Cisco Unified CME and Cisco Unified CCX, presented in the order in which the
                           		tasks are to be completed. This section contains information about performing
                           		tasks in the first 2 steps in this table and procedures for completing step 3.

For configuration
                           		information, see Configure Interoperability with Cisco Unified CCX .

Step

Task

Name of
                                       				  Document

1

Verify that
                                       				  the appropriate Cisco Unified Communications Manager Express
                                       				  (Cisco Unified CME) version is installed on the router. For compatibility
                                       				  information, see Cisco Unified Contact Center
                                          					 Express (Cisco Unified CCX) Software and Hardware Compatibility Guide .

—

2

Configure
                                       				  the Cisco Unified CME router.

Tip

Note the
                                                   					 XML user ID and password in Cisco Unified CME and router’s IP address.

See
                                       				  "Prerequisites' section in Enable Interoperability with Cisco Unified CCX .

3

Configure
                                       				  Cisco Unified CME to enable interoperability with Cisco Unified CCX.

Configure Interoperability with Cisco Unified CCX

4

Install
                                       				  Cisco Unified Contact Center Express (Cisco Unified CCX) for Cisco Unified CME.

See Cisco
                                          					 Unified Contact Center Express Administration Guide at Configuration Guides .

5

Perform the
                                       				  initial setup of Cisco CRS for Cisco Unified CME.

Tip

When setup
                                                   					 launches, you are asked for the XML user ID and password, known as AXL user in
                                                   					 Cisco CRS, that you created in Cisco Unified CME. You also must enter the
                                                   					 router IP address.

6

Configure
                                       				  Cisco Unified CME telephony subsystem to enable interoperability with
                                       				  Cisco Unified CCX.

“Provisioning Unified CCX
                                          					 for Unified CME” chapter in the appropriate Cisco
                                          					 CRS Administration Guide or Cisco
                                          					 Unified Contact Center Express Administration Guide at Configuration Guides .

7

Create users
                                       				  and assign the agent capability in Cisco CRS.

## Configure Interoperability with Cisco Unified CCX

### Enable
                           	 Interoperability with Cisco Unified CCX

To configure
                                 		  Cisco Unified CME to enable interoperability between Cisco Unified CME and
                                 		  Cisco Unified CCX, perform the following steps.

A single
                                             			 Cisco Unified CME can support multiple session managers.

Restriction

Maximum
                                                      				  number of active Cisco Unified CCX agents supported: 50.

Multi-Party
                                                      				  Ad Hoc and Meet-Me Conferencing are not supported.

The
                                                      				  following incoming calls are supported for deployment of the interoperability
                                                      				  feature: SIP trunk calls from another Cisco Unified CME and all calls from a
                                                      				  PSTN trunk. Other trunks, such H.323, are supported as usual in Cisco Unified
                                                      				  CME, however, not for customer calls to Cisco Unified CCX.

#### Before you begin

Cisco Unified CME version and Cisco IOS release that is
                                          				compatible with your Cisco Unified CCX version. For compatibility information,
                                          				see Cisco Unified Contact Center
                                             				  Express (Cisco Unified CCX) Software and Hardware Compatibility Guide .

XML API must
                                          				be configured to create an AXL username for Cisco Unified CCX access. For
                                          				configuration information, see Configure the XML API .

During the
                                                      				  initial setup of Cisco CRS for Cisco Unified CME, you need the AXL username and
                                                      				  password that was configured using the xml user command in telephony-service
                                                      				  configuration mode. You also need the router IP address that was configured
                                                      				  using the ip
                                                            						source-address command in telephony-service configuration mode.

Agent phones to be connected in Cisco Unified CME must be configured in Cisco Unified CME. When configuring a Cisco Unified CCX
                                          agent phone, use the keep-conference endcall command to enable conference initiators to exit from conference calls and end the conference for the remaining parties. For
                                          configuration information, see Configure Hardware Conferencing .

The
                                          				Cisco Unified CME router must be configured to accept incoming presence
                                          				requests. For configuration information, see Configure Presence Service .

To support
                                          				Desktop Monitoring and Recording, the service phone SpanToPCPort 1 command must be configured in
                                          				telephony-service configuration mode. For configuration information, see Modify Vendor Parameters for All SCCP Phones .

### SUMMARY STEPS

- enable

- configure terminal

- voice call send-alert

- voice service voip

- callmonitor

- gcid

- allow-connections sip to
                                       				  sip

- no supplementary-service
                                       				  sip moved-temporary

- no supplementary-service
                                       				  sip refer

- sip

- registrar server [ expires [ max sec ] [ min sec ]]

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

voice call send-alert

#### Example:

```
Router(config)# voice call send-alert
```

Enables the
                                             				terminating gateway to send an alert message instead of a progress message
                                             				after it receives a call setup message.

Step 4

voice service voip

#### Example:

```
Router(config)# voice service voip
```

Enters
                                             				voice-service configuration mode and specifies voice-over-IP encapsulation.

Step 5

callmonitor

#### Example:

```
Router(config-voi-serv)# callmonitor
```

Enables call
                                             				monitoring messaging functionality.

Used by
                                                      					 Cisco Unified CCX for processing and reporting.

Step 6

gcid

#### Example:

```
Router(config-voi-serv)# gcid
```

Enables Global
                                             				Call-ID (Gcid) for call control purposes.

Used by
                                                      					 Cisco Unified CCX for tracking call.

Step 7

allow-connections sip to
                                                				  sip

#### Example:

```
Router(config-voi-serv)# allow-connections sip to sip
```

Allows
                                             				connections between specific types of endpoints in a VoIP network.

Step 8

no supplementary-service
                                                				  sip moved-temporary

#### Example:

```
Router(config-voi-serv)# no supplementary-service sip moved-temporary
```

Prevents the
                                             				router from sending a redirect response to the destination for call forwarding.

Step 9

no supplementary-service
                                                				  sip refer

#### Example:

```
Router(config-voi-serv)# no supplementary-service sip refer
```

Prevents the
                                             				router from forwarding a REFER message to the destination for call transfers.

Step 10

sip

#### Example:

```
Router(config-voi-serv)# sip
```

Enters SIP
                                             				configuration mode.

Step 11

registrar server [ expires [ max sec ] [ min sec ]]

#### Example:

```
Router(config-voi-sip)# registrar server expires max 600 min 60
```

Enables SIP registrar functionality in Cisco Unified CME.

expires —(Optional) Sets the active time for an incoming registration.

max sec —(Optional) Maximum time for a registration to expire, in seconds. Range: 600 to 86400. Default: 3600. Recommended value:
                                                      600.

Ensure that the registration expiration timeout is set to a value smaller than the TCP connection aging timeout to avoid disconnection
                                                                  from the TCP.

min sec —(Optional) Minimum time for a registration to expire, in seconds. Range: 60 to 3600. Default: 60.

Step 12

end

#### Example:

```
Router(config-voi-serv)# end
```

Exits
                                             				configuration mode and enters privileged EXEC mode.

### Identify Agent
                           	 Directory Numbers in Cisco Unified CME for Session Manager on SCCP
                           	 Phones

To specify which
                                 		  directory numbers, associated with phone lines on Cisco Unified CCX agent
                                 		  phones, can be managed by a session manager, perform the following steps.

Restriction

Only SCCP
                                                      				  phones can be configured as agent phones in Cisco Unified CME. The Cisco VG224
                                                      				  Analog Phone Gateway and analog and SIP phones are supported as usual in
                                                      				  Cisco Unified CME, however, not as Cisco Unified CCX agent phones.

Cisco Unified IP Phone 7931 cannot be configured as an agent
                                                      				  phone in Cisco Unified CME. Cisco Unified IP Phone 7931s are supported as usual
                                                      				  in Cisco Unified CME, however, not as Cisco Unified CCX agent phones.

Shared-line
                                                      				  appearance is not supported on agent phones. A directory number cannot be
                                                      				  associated with more than one physical agent phone at one time.

Overlaid
                                                      				  lines are not supported on agent phones. More than one directory number cannot
                                                      				  be associated with a single line button on an agent phone.

Monitored
                                                      				  mode for a line button is not supported on agent phones. An agent phone cannot
                                                      				  be monitored by another phone.

Cisco
                                                      				  Unified CCX does not support a call event that includes a different directory
                                                      				  number; all call events must include the primary directory number. Call
                                                      				  transfers between phones with single-line directory numbers will cause call
                                                      				  monitoring to fail.

#### Before you begin

Up to eight
                                          				session managers must be configured in Cisco Unified CME.

Directory
                                          				numbers associated with Cisco Unified CCX agent phones must be configured in
                                          				Cisco Unified CME.

Cisco
                                                					 Unified CME 4.2: Directory numbers for agent phones must be configured as dual
                                                					 lines to allow an agent to make two call connections at the same time using one
                                                					 phone line button. Note that if the second line of the dual-line directory
                                                					 number is busy, a transfer event between phones in the solution will fail to
                                                					 complete.

Cisco
                                                					 Unified CME 4.3/7.0 and later versions: We recommend that directory numbers for
                                                					 agent phones be configured as octal lines to help to ensure that a free line
                                                					 with the same directory number is available for a transfer event.

For
                                                					 configuration information, see Configure Phones to Make Basic Call .

### SUMMARY STEPS

- enable

- configure terminal

- ephone-dn dn-tag

- allow watch

- session-server session-server-tag [ ,... session-server-tag ]

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

ephone-dn dn-tag

#### Example:

```
Router(config)# ephone-dn 24
```

Enters
                                             				ephone-dn configuration mode.

dn-tag —Unique ID of an already configured
                                                      					 directory number. The tag number corresponds to a tag number created when this
                                                      					 directory number was initially configured.

Step 4

allow watch

#### Example:

```
Router(config-ephone-dn)# allow watch
```

Allows the phone line associated with this directory number to be
                                             				monitored by a watcher in a presence service.

This command can also be configured in ephone-dn template
                                                      					 configuration mode and applied to one or more phones. The ephone-dn
                                                      					 configuration has priority over the ephone-dn template configuration.

Step 5

session-server session-server-tag [ ,... session-server-tag ]

#### Example:

```
Router(config-ephone-dn)# session-server 1,2,3,4,6
```

Specifies
                                             				which session managers are to monitor the directory number being configured.

session-server-tag —Unique ID session manager,
                                                      					 configured in Cisco Unified CCX and automatically provided to
                                                      					 Cisco Unified CME. Range: 1 to 8.

Tip

If you
                                                                  						do not know the value for session-server-tag , we recommend using 1.

Can
                                                      					 configure up to eight session-server-tags; individual tags must be separated by
                                                      					 commas ( , ).

Each
                                                      					 directory number can be managed by up to eight session managers. Each session
                                                      					 manager can monitor more than one directory number.

Step 6

end

#### Example:

```
Router(config-ephone-dn)# end
```

Exits
                                             				configuration mode and enters privileged EXEC mode.

### Verify
                           	 Registrations and Subscriptions in Cisco Unified CME

Before using the
                                 		  system, verify registrations and subscriptions for Cisco Unified CCX endpoints.

Step 1

Use the show sip status
                                                				  registrar command to verify whether session manager and Cisco CRS
                                          			 route points are registered.

Step 2

Use the show presence subscription
                                                				  summary command to verify whether Cisco CRS route points and
                                          			 Cisco Unified CCX agent directory numbers are subscribed.

The following
                                             				is sample output from the show presence subscription
                                                   					 summary command. The first two rows show the status for two route
                                             				points. The next two are for logged in agent phones.

```
Router# show presence subscription summary Presence Active Subscription Records Summary: 15 subscription
Watcher                  Presentity               SubID Expires SibID  Status
======================== ======================== ====== ======= ====== ======
CRScontrol@10.4.171.81   8101@10.4.171.34         4      3600    0      idle
CRScontrol@10.4.171.81   8201@10.4.171.34         8      3600    0      idle
CRScontrol@10.4.171.81   4016@10.4.171.34         10 3600    0      idle
CRScontrol@10.4.171.81   4020@10.4.171.34         12 3599    0      idle
```

### Re-create a
                           	 Session Manager in Cisco Unified CME

Provisioning and
                                             			 configuration information in Cisco Unified CCX is automatically provided to
                                             			 Cisco United CME. The following task is required only if the configuration from
                                             			 Cisco Unified CCX is deleted or must be modified.

To re-create a
                                 		  session manager in Cisco Unified CME for Cisco Unified CCX, perform the
                                 		  following steps.

### SUMMARY STEPS

- enable

- configure terminal

- voice register session-server session-server-tag

- register id name

- keepalive seconds

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

voice register session-server session-server-tag

#### Example:

```
Router(config)# voice register session-server 1
```

Enters voice
                                             				register session-server configuration mode to enable and configure a session
                                             				manager for an external feature server, such as the Cisco Unified CCX
                                             				application on a Cisco CRS system.

Range: 1
                                                      					 to 8.

A single
                                                      					 Cisco Unified CME can support multiple session managers.

Step 4

register id name

#### Example:

```
Router(config-register-fs)# CRS1
```

(Optional)
                                             				Required only if the configuration from Cisco Unified CCX is deleted or must be
                                             				modified.

name —String for identifying Cisco Unified CCX. Can
                                                      					 contain 1 to 30 alphanumeric characters.

Step 5

keepalive seconds

#### Example:

```
Router(config-register-fs)# keepalive 300
```

(Optional)
                                             				Required only if the configuration from Cisco Unified CCX is deleted or must be
                                             				modified.

Keepalive
                                                      					 duration for registration, in seconds, after which the registration expires
                                                      					 unless Cisco Unified CCX reregisters before the registration expiry.

Range: 60
                                                      					 to 3600. Default: 300.

Default in
                                                         				  Cisco Unified CCX is 120.

Step 6

end

#### Example:

```
Router(config-register-fs)# end
```

Exits
                                             				configuration mode and enters privileged EXEC mode.

### Reconfigure a
                           	 Cisco CRS Route Point as a SIP Endpoint

Provisioning and
                                             			 configuration information in Cisco Unified CCX is automatically provided to
                                             			 Cisco United CME. The following task is required only if the configuration from
                                             			 Cisco Unified CCX is deleted or must be modified.

To reconfigure a
                                 		  Cisco CRS route point as a SIP endpoint in Cisco Unified CME, perform the
                                 		  following steps.

Restriction

Each
                                                      				  Cisco CRS route point can be managed by only one session manager.

Each session
                                                      				  manager can manage more than one Cisco CRS route point.

#### Before you begin

Directory
                                          				numbers associated with Cisco CRS route points must be configured in
                                          				Cisco Unified CME. For configuration information for directory numbers
                                          				associated with SIP endpoints, see Configure Phones to Make Basic Call .

Directory
                                          				numbers associated with Cisco CRS route points must be enabled to be watched.
                                          				For configuration information, see Configure Presence Service .

The mode cme command must be enabled in Cisco Unified CME.

### SUMMARY STEPS

- enable

- configure terminal

- voice register dn dn-tag

- number number

- session-server session-server-tag [ ,... session-server-tag ]

- allow watch

- refer target dial-peer

- exit

- voice register pool pool-tag

- number tag dn dn-tag

- session-server session-server-tag

- codec codec-type

- dtmf-relay
                                       				  sip-notify

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

voice register dn dn-tag

#### Example:

```
Router(config-register-global)# voice register dn 1
```

Enters voice
                                             				register dn configuration mode to define a directory number for a SIP phone,
                                             				intercom line, voice port, or a message-waiting indicator (MWI).

Step 4

number number

#### Example:

```
Router(config-register-dn)# number 2777
```

Defines a
                                             				valid number for a directory number.

Step 5

session-server session-server-tag [ ,... session-server-tag ]

#### Example:

```
Router(config-register-dn)# session-server 1
```

Specifies
                                             				which session managers are to monitor the directory number being configured.

session-server-tag —Unique ID session manager,
                                                      					 configured in Cisco Unified CCX and automatically provided to
                                                      					 Cisco Unified CME. Range: 1 to 8.

Tip

If you
                                                                  						do not know the value for session-server-tag , we recommend using 1.

Can
                                                      					 configure up to eight session-server-tags; individual tags must be separated by
                                                      					 commas ( , ).

Each
                                                      					 directory number can be managed by up to eight session managers. Each session
                                                      					 manager can monitor more than one directory number.

Step 6

allow watch

#### Example:

```
Router(config-register-dn)# allow watch
```

Allows the
                                             				phone line associated with this directory number to be monitored by a watcher
                                             				in a presence service.

Step 7

refer target dial-peer

#### Example:

```
Router(config-register-dn)# refer target dial-peer
```

Enables
                                             				watcher to handle SIP REFER message from this directory number.

target
                                                            						  dial-peer —Refer To portion of message is based on address from
                                                      					 dial peer for this directory number.

Step 8

exit

#### Example:

```
Router(config-register-dn)# exit
```

Exits
                                             				configuration mode to the next highest mode in the configuration mode
                                             				hierarchy.

Step 9

voice register pool pool-tag

#### Example:

```
Router(config)# voice register pool 3
```

Enters voice
                                             				register pool configuration mode to set device-specific parameters for a
                                             				Cisco CRS route point.

- A voice
                                                   				  register pool in Cisco Unified CCX can contain up to 10 individual SIP
                                                   				  endpoints. Subsequent pools are created for additional SIP endpoints.

Step 10

number tag dn dn-tag

#### Example:

```
Router(config-register-pool)# number
			 1 dn 1
```

Associates a
                                             				directory number with the route point being configured.

Step 11

session-server session-server-tag

#### Example:

```
Router(config-register-pool)#
			 session-server 1
```

identifies
                                             				session manager to be used to control the route point being configured.

session-server-tag —Unique number assigned to a
                                                      					 session manager. Range: 1 to 8. The tag number corresponds to a tag number
                                                      					 created by using the voice register
                                                            						  session-server command.

Step 12

codec codec-type

#### Example:

```
Router(config-register-pool)# codec
			 g711ulaw
```

Specifies the codec for the dial peer dynamically created for the route point being configured.

codec-type —g711ulaw is required for Cisco Unified CCX.

Step 13

dtmf-relay
                                                				  sip-notify

#### Example:

```
Router(config-register-pool)#
			 dtmf-relay sip-notify
```

Specifies
                                             				DTMF Relay method to be used by the route point being configured.

Step 14

end

#### Example:

```
Router(config-register-pool)# end
```

Exits
                                             				configuration mode and enters privileged EXEC mode.

## Configuration
                        	 Examples for Interoperability with Cisco Unified CCX

The following
                              		  output from the show
                                    				running-configuration command shows the configuration on a
                              		  Cisco Unified CME router that will interoperate with Cisco Unified CCX.

```
!
version 12.4
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname sb-sj3-3845-uut1
!
boot-start-marker
boot-end-marker
!
card type t1 0 2
card type t1 0 3
logging buffered 1000000
no logging console
enable password password
!
no aaa new-model
network-clock-participate wic 2 
network-clock-participate wic 3 
ip cef
!
!
no ip dhcp use vrf connected
!
!
ip dhcp excluded-address 192.0.2.250 192.0.2.254
!         
ip dhcp pool ephones
   network 192.0.2.0 255.255.255.0
   option 150 ip 192.0.2.254 
   default-router 192.0.2.254
!
!
no ip domain lookup
!
isdn switch-type primary-5ess
voice-card 0
 no dspfarm
!
!
!
!
voice service voip
 gcid
 callmonitor
 allow-connections h323 to h323
 allow-connections h323 to sip
 allow-connections sip to h323
 allow-connections sip to sip
 no supplementary-service sip moved-temporarily
 no supplementary-service sip refer
 sip
  registrar server expires max 120 min 60
!
!
voice class codec 1
 codec preference 1 g711ulaw
 codec preference 2 g729r8
!
!
!
!
!
!
!
!
!
!
voice register global
 mode cme
 source-address 192.0.2.254 port 5060
 max-dn 720
 max-pool 240
 authenticate presence
 authenticate register
 dialplan-pattern 1 511.... extension-length 4
 voicemail 9001
 create profile sync 0000347600391314
!
voice register session-server  1
 keepalive 300
 register-id SB-SJ3-UCCX1_1164774025000
!
voice register dn  1
 session-server 1
 number 8999
 allow watch
 refer target dial-peer
!
voice register dn  2
 session-server 1
 number 8001
 allow watch
 refer target dial-peer
!
voice register dn  3
 session-server 1
 number 8101
 allow watch
 refer target dial-peer
!
voice register dn  11
 number 2011
 name ep-sip-1-11
 mwi
!
voice register dn  12
 number 2012
 name ep-sip-1-12
 mwi
!
voice register dn  16
 number 5016
 name rp-sip-1-16
 label SIP 511-5016
 mwi
!
voice register dn  17
 number 5017
 name rp-sip-1-17
 label SIP 511-5017
 mwi
!
voice register dn  18
 number 5018
 name rp-sip-1-18
 label SIP 511-5018
 mwi
!
voice register pool  1
 session-server 1
 number 1 dn 1
 number 2 dn 2
 number 3 dn 3
 dtmf-relay sip-notify
 codec g711ulaw
!
voice register pool  11
 id mac 1111.0711.2011
 type 7970
 number 1 dn 11
 dtmf-relay rtp-nte
 voice-class codec 1
 username 5112011 password 5112011
!
voice register pool  12
 id mac 1111.0711.2012
 type 7960
 number 1 dn 12
 dtmf-relay rtp-nte
 voice-class codec 1
 username 5112012 password 5112012
!
voice register pool  16
 id mac 0017.0EBC.1500
 type 7961GE
 number 1 dn 16
 dtmf-relay rtp-nte
 voice-class codec 1
 username rp-sip-1-16 password pool16
!
voice register pool  17
 id mac 0016.C7C5.0660
 type 7971
 number 1 dn 17
 dtmf-relay rtp-nte
 voice-class codec 1
 username rp-sip-1-17 password pool17
!
voice register pool  18
 id mac 0015.629E.825D
 type 7971
 number 1 dn 18
 dtmf-relay rtp-nte
 voice-class codec 1
 username rp-sip-1-18 password pool18
!
!
!
!
!
!
!
controller T1 0/2/0
 framing esf
 clock source internal
 linecode b8zs
 pri-group timeslots 1-4,24
!
controller T1 0/2/1
 framing esf
 clock source internal
 linecode b8zs
 pri-group timeslots 1-4,24
!
controller T1 0/3/0
 framing esf
 clock source internal
 linecode b8zs
 ds0-group 0 timeslots 1-4 type e&-immediate-start
!
controller T1 0/3/1
 framing esf
 clock source internal
 linecode b8zs
 ds0-group 0 timeslots 1-4 type e&-immediate-start
vlan internal allocation policy ascending
!
!
!
!
interface GigabitEthernet0/0
 ip address 209.165.201.1 255.255.255.224
 duplex auto
 speed auto
 media-type rj45
!
interface GigabitEthernet0/1
 ip address 192.0.2.254 255.255.255.0
 duplex auto
 speed auto
 media-type rj45
!
interface Serial0/2/0:23
 no ip address
 encapsulation hdlc
 isdn switch-type primary-5ess
 isdn protocol-emulate network
 isdn incoming-voice voice
 no cdp enable
!
interface Serial0/2/1:23
 no ip address
 encapsulation hdlc
 isdn switch-type primary-5ess
 isdn protocol-emulate network
 isdn incoming-voice voice
 no cdp enable
!
interface Service-Engine1/0
 ip unnumbered GigabitEthernet0/0
 service-module ip address 209.165.202.129 255.255.255.224
 service-module ip default-gateway 209.165.201.1
!
ip route 192.0.0.30 255.0.0.0 192.0.0.55
ip route 209.165.202.129 255.255.255.224 Service-Engine1/0
ip route 192.0.2.56 255.255.255.0 209.165.202.2
ip route 192.0.3.74 255.255.255.0 209.165.202.3
ip route 209.165.202.158 255.255.255.224 192.0.0.55
!
!
ip http server
ip http authentication local
ip http path flash:
!
!
ixi transport http
 response size 64
 no shutdown
 request outstanding 1
!
ixi application cme
 no shutdown
!
!
!
control-plane
!
!
!
voice-port 0/0/0
!
voice-port 0/0/1
!
voice-port 0/2/0:23
!
voice-port 0/3/0:0
!
voice-port 0/1/0
!
voice-port 0/1/1
!
voice-port 0/2/1:23
!
voice-port 0/3/1:0
!
!
!
!
!
dial-peer voice 9000 voip
 description ==> This is for internal calls to CUE
 destination-pattern 9...
 voice-class codec 1
 session protocol sipv2
 session target ipv4:209.165.202.129
 dtmf-relay rtp-nte sip-notify
!
dial-peer voice 9001 voip
 description ==> This is for external calls to CUE
 destination-pattern 5119...
 voice-class codec 1
 session protocol sipv2
 session target ipv4:209.165.202.129 
 dtmf-relay rtp-nte sip-notify
!
dial-peer voice 521 voip
 destination-pattern 521....
 voice-class codec 1
 max-redirects 5
 session protocol sipv2
 session target ipv4:209.165.201.2
 dtmf-relay rtp-nte sip-notify
!
dial-peer voice 531 voip
 destination-pattern 531....
 voice-class codec 1
 max-redirects 5
 session protocol sipv2
 session target ipv4:209.165.201.3
 dtmf-relay rtp-nte sip-notify
!
!
presence
 presence call-list
 watcher all
 allow subscribe
!
sip-ua 
 mwi-server ipv4:209.165.202.128 expires 3600 port 5060 transport udp 
 presence enable
!
!
telephony-service
 no auto-reg-ephone
 xml user axluser password axlpass 15 <====AXL username and password for Cisco CRS max-ephones 240
 max-dn 720
 ip source-address 192.0.2.254 port 2000 <====IP address of router system message sb-sj3-3845-uut1
 url services http://192.0.2.252:6293/ipphone/jsp/sciphonexml/IPAgentInitial.jsp
 url authentication http:192.0.2.252:6293/ipphone/jsp/sciphonexml/IPAgentAuthenticate.jsp
 cnf-file perphone
 dialplan-pattern 1 511.... extension-length 4
 voicemail 9001
 max-conferences 8 gain -6
 call-forward pattern .T
 moh flash:music-on-hold.wav
 multicast moh 239.10.10.1 port 2000
 transfer-system full-consult
 transfer-pattern .T
 create cnf-files version-stamp 7960 Jun 18 2007 07:44:25
!
!
ephone-dn  1  dual-line
 session-server 1 
 number 1001
 name ag-1-1
 allow watch
 mwi sip
!
!
ephone-dn  2  dual-line
 session-server 1 
 number 1002
 name ag-1-2
 allow watch
 mwi sip
!
!
ephone-dn  3  dual-line
 session-server 1 
 number 1003
 name ag-1-3
 allow watch
 mwi sip
!
!
ephone-dn  4  dual-line
 session-server 1 
 number 1004
 name ag-1-4
 allow watch
 mwi sip
!
!
ephone-dn  5
 session-server 1 
 number 1005
 name ag-1-5
 allow watch
 mwi sip
!
!
ephone-dn  11  dual-line
 number 3011
 name ep-sccp-1-11
 mwi sip
!
!
ephone-dn  12
 number 3012
 name ep-sccp-1-12
 mwi sip
!
!
ephone-dn  16  dual-line
 number 4016
 label SCCP 511-4016
 name rp-sccp-1-16
 mwi sip
!
!
ephone-dn  17  dual-line
 number 4017
 label SCCP 511-4017
 name rp-sccp-1-17
 mwi sip
!
!
ephone-dn  18  dual-line
 number 4018
 label SCCP 511-4018
 name rp-sccp-1-18
 mwi sip
!
!
ephone-dn  19  dual-line
 number 4019
 label SCCP 511-4019
 name rp-sccp-1-19
 mwi sip
!
!
ephone-dn  20  dual-line
 number 4020
 label SCCP 511-4020
 name rp-sccp-1-20
 mwi sip
!
!
ephone-dn  21  dual-line
 number 4021
 label SCCP 511-4021
 name rp-sccp-1-21
 mwi sip
!
!
ephone-dn  22  dual-line
 number 4022
 label SCCP 511-4022
 name rp-sccp-1-22
 mwi sip
!
!
ephone  1
 mac-address 1111.0711.1001
 type 7970
 keep-conference endcall
 button  1:1
!
!
!
ephone  2
 mac-address 1111.0711.1002
 type 7970
 keep-conference endcall
 button  1:2
!
!
!
ephone  3
 mac-address 1111.0711.1003
 type 7970
 keep-conference endcall
 button  1:3
!
!
!
ephone  4
 mac-address 1111.0711.1004
 type 7970
 keep-conference endcall
 button  1:4
!
!
!
ephone  5
 mac-address 1111.0711.1005
 type 7970
 keep-conference endcall
 button  1:5
!
!
!
ephone  11
 mac-address 1111.0711.3011
 type 7970
 keep-conference endcall
 button  1:11
!
!
!
ephone  12
 mac-address 1111.0711.3012
 type 7960
 keep-conference endcall
 button  1:12
!
!
!
ephone  16
 mac-address 0012.D916.5AD6
 type 7960
 keep-conference endcall
 button  1:16
!
!
!
ephone  17
 mac-address 0013.1AA6.7A9E
 type 7960
 keep-conference endcall
 button  1:17
!
!
!
ephone  18
 mac-address 0012.80F3.B013
 type 7960
 keep-conference endcall
 button  1:18
!
!
!
ephone  19
 mac-address 0013.1A1F.6282
 type 7970
 keep-conference endcall
 button  1:19
!
!
!
ephone  20
 mac-address 0013.195A.00D0
 type 7970
 keep-conference endcall
 button  1:20
!
!
!
ephone  21
 mac-address 0017.0EBC.147C
 type 7961GE
 keep-conference endcall
 button  1:21
!
!
!
ephone  22
 mac-address 0016.C7C5.0578
 type 7971
 keep-conference endcall
 button  1:22
!
!
!
line con 0
 exec-timeout 0 0
 stopbits 1
line aux 0
 stopbits 1
line 66
 no activation-character
 no exec
 transport preferred none
 transport input all
 transport output pad telnet rlogin lapb-ta mop udptn v120
line vty 0 4
 password lab
 login
!
scheduler allocate 20000 1000
!
end
```

### Where to Go
                           	 Next

If you are done
                              		modifying parameters for phones in Cisco Unified CME, generate a new
                              		configuration file and restart the phones. See Generate Configuration Files for Phones .

## Feature
                        	 Information for Interoperability with Cisco Unified CCX

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Cisco Unified CME Version

Modification

Interoperability with Cisco Unified CCX

4.2

Enables interoperability between Cisco Unified CME and Cisco
                                          					 Customer Response Solutions (CRS) 5.0 and later versions with Cisco Unified
                                          					 Contact Center Express (Cisco Unified CCX), including Cisco Unified IP IVR,
                                          					 enhanced call processing, device and call monitoring, unattended call transfers
                                          					 to multiple call center agents, and basic extension mobility.

| Note | For Unified CME 8.6 and later releases, CRS with Unified CCX is not supported. |
|---|---|

| Step | Task | Name of
                                       				  Document |
|---|---|---|
| 1 | Verify that
                                       				  the appropriate Cisco Unified Communications Manager Express
                                       				  (Cisco Unified CME) version is installed on the router. For compatibility
                                       				  information, see Cisco Unified Contact Center
                                          					 Express (Cisco Unified CCX) Software and Hardware Compatibility Guide . | — |
| 2 | Configure
                                       				  the Cisco Unified CME router. Tip Note the
                                                   					 XML user ID and password in Cisco Unified CME and router’s IP address. | Tip | Note the
                                                   					 XML user ID and password in Cisco Unified CME and router’s IP address. | See
                                       				  "Prerequisites' section in Enable Interoperability with Cisco Unified CCX . |
| Tip | Note the
                                                   					 XML user ID and password in Cisco Unified CME and router’s IP address. |
| 3 | Configure
                                       				  Cisco Unified CME to enable interoperability with Cisco Unified CCX. | Configure Interoperability with Cisco Unified CCX |
| 4 | Install
                                       				  Cisco Unified Contact Center Express (Cisco Unified CCX) for Cisco Unified CME. | See Cisco
                                          					 Unified Contact Center Express Administration Guide at Configuration Guides . |
| 5 | Perform the
                                       				  initial setup of Cisco CRS for Cisco Unified CME. Tip When setup
                                                   					 launches, you are asked for the XML user ID and password, known as AXL user in
                                                   					 Cisco CRS, that you created in Cisco Unified CME. You also must enter the
                                                   					 router IP address. | Tip | When setup
                                                   					 launches, you are asked for the XML user ID and password, known as AXL user in
                                                   					 Cisco CRS, that you created in Cisco Unified CME. You also must enter the
                                                   					 router IP address. |
| Tip | When setup
                                                   					 launches, you are asked for the XML user ID and password, known as AXL user in
                                                   					 Cisco CRS, that you created in Cisco Unified CME. You also must enter the
                                                   					 router IP address. |
| 6 | Configure
                                       				  Cisco Unified CME telephony subsystem to enable interoperability with
                                       				  Cisco Unified CCX. | “Provisioning Unified CCX
                                          					 for Unified CME” chapter in the appropriate Cisco
                                          					 CRS Administration Guide or Cisco
                                          					 Unified Contact Center Express Administration Guide at Configuration Guides . |
| 7 | Create users
                                       				  and assign the agent capability in Cisco CRS. |

| Tip | Note the
                                                   					 XML user ID and password in Cisco Unified CME and router’s IP address. |
|---|---|

| Tip | When setup
                                                   					 launches, you are asked for the XML user ID and password, known as AXL user in
                                                   					 Cisco CRS, that you created in Cisco Unified CME. You also must enter the
                                                   					 router IP address. |
|---|---|

| Note | A single
                                             			 Cisco Unified CME can support multiple session managers. |
|---|---|

| Restriction | Maximum
                                                      				  number of active Cisco Unified CCX agents supported: 50. Multi-Party
                                                      				  Ad Hoc and Meet-Me Conferencing are not supported. The
                                                      				  following incoming calls are supported for deployment of the interoperability
                                                      				  feature: SIP trunk calls from another Cisco Unified CME and all calls from a
                                                      				  PSTN trunk. Other trunks, such H.323, are supported as usual in Cisco Unified
                                                      				  CME, however, not for customer calls to Cisco Unified CCX. |
|---|---|

| Note | During the
                                                      				  initial setup of Cisco CRS for Cisco Unified CME, you need the AXL username and
                                                      				  password that was configured using the xml user command in telephony-service
                                                      				  configuration mode. You also need the router IP address that was configured
                                                      				  using the ip
                                                            						source-address command in telephony-service configuration mode. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice call send-alert Example: Router(config)# voice call send-alert | Enables the
                                             				terminating gateway to send an alert message instead of a progress message
                                             				after it receives a call setup message. |
| Step 4 | voice service voip Example: Router(config)# voice service voip | Enters
                                             				voice-service configuration mode and specifies voice-over-IP encapsulation. |
| Step 5 | callmonitor Example: Router(config-voi-serv)# callmonitor | Enables call
                                             				monitoring messaging functionality. Used by
                                                      					 Cisco Unified CCX for processing and reporting. |
| Step 6 | gcid Example: Router(config-voi-serv)# gcid | Enables Global
                                             				Call-ID (Gcid) for call control purposes. Used by
                                                      					 Cisco Unified CCX for tracking call. |
| Step 7 | allow-connections sip to
                                                				  sip Example: Router(config-voi-serv)# allow-connections sip to sip | Allows
                                             				connections between specific types of endpoints in a VoIP network. |
| Step 8 | no supplementary-service
                                                				  sip moved-temporary Example: Router(config-voi-serv)# no supplementary-service sip moved-temporary | Prevents the
                                             				router from sending a redirect response to the destination for call forwarding. |
| Step 9 | no supplementary-service
                                                				  sip refer Example: Router(config-voi-serv)# no supplementary-service sip refer | Prevents the
                                             				router from forwarding a REFER message to the destination for call transfers. |
| Step 10 | sip Example: Router(config-voi-serv)# sip | Enters SIP
                                             				configuration mode. |
| Step 11 | registrar server [ expires [ max sec ] [ min sec ]] Example: Router(config-voi-sip)# registrar server expires max 600 min 60 | Enables SIP registrar functionality in Cisco Unified CME. expires —(Optional) Sets the active time for an incoming registration. max sec —(Optional) Maximum time for a registration to expire, in seconds. Range: 600 to 86400. Default: 3600. Recommended value:
                                                      600. Note Ensure that the registration expiration timeout is set to a value smaller than the TCP connection aging timeout to avoid disconnection
                                                                  from the TCP. min sec —(Optional) Minimum time for a registration to expire, in seconds. Range: 60 to 3600. Default: 60. | Note | Ensure that the registration expiration timeout is set to a value smaller than the TCP connection aging timeout to avoid disconnection
                                                                  from the TCP. |
| Note | Ensure that the registration expiration timeout is set to a value smaller than the TCP connection aging timeout to avoid disconnection
                                                                  from the TCP. |
| Step 12 | end Example: Router(config-voi-serv)# end | Exits
                                             				configuration mode and enters privileged EXEC mode. |

| Note | Ensure that the registration expiration timeout is set to a value smaller than the TCP connection aging timeout to avoid disconnection
                                                                  from the TCP. |
|---|---|

| Restriction | Only SCCP
                                                      				  phones can be configured as agent phones in Cisco Unified CME. The Cisco VG224
                                                      				  Analog Phone Gateway and analog and SIP phones are supported as usual in
                                                      				  Cisco Unified CME, however, not as Cisco Unified CCX agent phones. Cisco Unified IP Phone 7931 cannot be configured as an agent
                                                      				  phone in Cisco Unified CME. Cisco Unified IP Phone 7931s are supported as usual
                                                      				  in Cisco Unified CME, however, not as Cisco Unified CCX agent phones. Shared-line
                                                      				  appearance is not supported on agent phones. A directory number cannot be
                                                      				  associated with more than one physical agent phone at one time. Overlaid
                                                      				  lines are not supported on agent phones. More than one directory number cannot
                                                      				  be associated with a single line button on an agent phone. Monitored
                                                      				  mode for a line button is not supported on agent phones. An agent phone cannot
                                                      				  be monitored by another phone. Cisco
                                                      				  Unified CCX does not support a call event that includes a different directory
                                                      				  number; all call events must include the primary directory number. Call
                                                      				  transfers between phones with single-line directory numbers will cause call
                                                      				  monitoring to fail. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router# enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone-dn dn-tag Example: Router(config)# ephone-dn 24 | Enters
                                             				ephone-dn configuration mode. dn-tag —Unique ID of an already configured
                                                      					 directory number. The tag number corresponds to a tag number created when this
                                                      					 directory number was initially configured. |
| Step 4 | allow watch Example: Router(config-ephone-dn)# allow watch | Allows the phone line associated with this directory number to be
                                             				monitored by a watcher in a presence service. This command can also be configured in ephone-dn template
                                                      					 configuration mode and applied to one or more phones. The ephone-dn
                                                      					 configuration has priority over the ephone-dn template configuration. |
| Step 5 | session-server session-server-tag [ ,... session-server-tag ] Example: Router(config-ephone-dn)# session-server 1,2,3,4,6 | Specifies
                                             				which session managers are to monitor the directory number being configured. session-server-tag —Unique ID session manager,
                                                      					 configured in Cisco Unified CCX and automatically provided to
                                                      					 Cisco Unified CME. Range: 1 to 8. Tip If you
                                                                  						do not know the value for session-server-tag , we recommend using 1. Can
                                                      					 configure up to eight session-server-tags; individual tags must be separated by
                                                      					 commas ( , ). Each
                                                      					 directory number can be managed by up to eight session managers. Each session
                                                      					 manager can monitor more than one directory number. | Tip | If you
                                                                  						do not know the value for session-server-tag , we recommend using 1. |
| Tip | If you
                                                                  						do not know the value for session-server-tag , we recommend using 1. |
| Step 6 | end Example: Router(config-ephone-dn)# end | Exits
                                             				configuration mode and enters privileged EXEC mode. |

| Tip | If you
                                                                  						do not know the value for session-server-tag , we recommend using 1. |
|---|---|

| Step 1 | Use the show sip status
                                                				  registrar command to verify whether session manager and Cisco CRS
                                          			 route points are registered. |
|---|---|
| Step 2 | Use the show presence subscription
                                                				  summary command to verify whether Cisco CRS route points and
                                          			 Cisco Unified CCX agent directory numbers are subscribed. The following
                                             				is sample output from the show presence subscription
                                                   					 summary command. The first two rows show the status for two route
                                             				points. The next two are for logged in agent phones. Router# show presence subscription summary Presence Active Subscription Records Summary: 15 subscription
Watcher                  Presentity               SubID Expires SibID  Status
======================== ======================== ====== ======= ====== ======
CRScontrol@10.4.171.81   8101@10.4.171.34         4      3600    0      idle
CRScontrol@10.4.171.81   8201@10.4.171.34         8      3600    0      idle
CRScontrol@10.4.171.81   4016@10.4.171.34         10 3600    0      idle
CRScontrol@10.4.171.81   4020@10.4.171.34         12 3599    0      idle |

| Note | Provisioning and
                                             			 configuration information in Cisco Unified CCX is automatically provided to
                                             			 Cisco United CME. The following task is required only if the configuration from
                                             			 Cisco Unified CCX is deleted or must be modified. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router# enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register session-server session-server-tag Example: Router(config)# voice register session-server 1 | Enters voice
                                             				register session-server configuration mode to enable and configure a session
                                             				manager for an external feature server, such as the Cisco Unified CCX
                                             				application on a Cisco CRS system. Range: 1
                                                      					 to 8. A single
                                                      					 Cisco Unified CME can support multiple session managers. |
| Step 4 | register id name Example: Router(config-register-fs)# CRS1 | (Optional)
                                             				Required only if the configuration from Cisco Unified CCX is deleted or must be
                                             				modified. name —String for identifying Cisco Unified CCX. Can
                                                      					 contain 1 to 30 alphanumeric characters. |
| Step 5 | keepalive seconds Example: Router(config-register-fs)# keepalive 300 | (Optional)
                                             				Required only if the configuration from Cisco Unified CCX is deleted or must be
                                             				modified. Keepalive
                                                      					 duration for registration, in seconds, after which the registration expires
                                                      					 unless Cisco Unified CCX reregisters before the registration expiry. Range: 60
                                                      					 to 3600. Default: 300. Note Default in
                                                         				  Cisco Unified CCX is 120. | Note | Default in
                                                         				  Cisco Unified CCX is 120. |
| Note | Default in
                                                         				  Cisco Unified CCX is 120. |
| Step 6 | end Example: Router(config-register-fs)# end | Exits
                                             				configuration mode and enters privileged EXEC mode. |

| Note | Default in
                                                         				  Cisco Unified CCX is 120. |
|---|---|

| Note | Provisioning and
                                             			 configuration information in Cisco Unified CCX is automatically provided to
                                             			 Cisco United CME. The following task is required only if the configuration from
                                             			 Cisco Unified CCX is deleted or must be modified. |
|---|---|

| Restriction | Each
                                                      				  Cisco CRS route point can be managed by only one session manager. Each session
                                                      				  manager can manage more than one Cisco CRS route point. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router# enable | Enables
                                             				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register dn dn-tag Example: Router(config-register-global)# voice register dn 1 | Enters voice
                                             				register dn configuration mode to define a directory number for a SIP phone,
                                             				intercom line, voice port, or a message-waiting indicator (MWI). |
| Step 4 | number number Example: Router(config-register-dn)# number 2777 | Defines a
                                             				valid number for a directory number. |
| Step 5 | session-server session-server-tag [ ,... session-server-tag ] Example: Router(config-register-dn)# session-server 1 | Specifies
                                             				which session managers are to monitor the directory number being configured. session-server-tag —Unique ID session manager,
                                                      					 configured in Cisco Unified CCX and automatically provided to
                                                      					 Cisco Unified CME. Range: 1 to 8. Tip If you
                                                                  						do not know the value for session-server-tag , we recommend using 1. Can
                                                      					 configure up to eight session-server-tags; individual tags must be separated by
                                                      					 commas ( , ). Each
                                                      					 directory number can be managed by up to eight session managers. Each session
                                                      					 manager can monitor more than one directory number. | Tip | If you
                                                                  						do not know the value for session-server-tag , we recommend using 1. |
| Tip | If you
                                                                  						do not know the value for session-server-tag , we recommend using 1. |
| Step 6 | allow watch Example: Router(config-register-dn)# allow watch | Allows the
                                             				phone line associated with this directory number to be monitored by a watcher
                                             				in a presence service. |
| Step 7 | refer target dial-peer Example: Router(config-register-dn)# refer target dial-peer | Enables
                                             				watcher to handle SIP REFER message from this directory number. target
                                                            						  dial-peer —Refer To portion of message is based on address from
                                                      					 dial peer for this directory number. |
| Step 8 | exit Example: Router(config-register-dn)# exit | Exits
                                             				configuration mode to the next highest mode in the configuration mode
                                             				hierarchy. |
| Step 9 | voice register pool pool-tag Example: Router(config)# voice register pool 3 | Enters voice
                                             				register pool configuration mode to set device-specific parameters for a
                                             				Cisco CRS route point. A voice
                                                   				  register pool in Cisco Unified CCX can contain up to 10 individual SIP
                                                   				  endpoints. Subsequent pools are created for additional SIP endpoints. |
| Step 10 | number tag dn dn-tag Example: Router(config-register-pool)# number
			 1 dn 1 | Associates a
                                             				directory number with the route point being configured. |
| Step 11 | session-server session-server-tag Example: Router(config-register-pool)#
			 session-server 1 | identifies
                                             				session manager to be used to control the route point being configured. session-server-tag —Unique number assigned to a
                                                      					 session manager. Range: 1 to 8. The tag number corresponds to a tag number
                                                      					 created by using the voice register
                                                            						  session-server command. |
| Step 12 | codec codec-type Example: Router(config-register-pool)# codec
			 g711ulaw | Specifies the codec for the dial peer dynamically created for the route point being configured. codec-type —g711ulaw is required for Cisco Unified CCX. |
| Step 13 | dtmf-relay
                                                				  sip-notify Example: Router(config-register-pool)#
			 dtmf-relay sip-notify | Specifies
                                             				DTMF Relay method to be used by the route point being configured. |
| Step 14 | end Example: Router(config-register-pool)# end | Exits
                                             				configuration mode and enters privileged EXEC mode. |

| Tip | If you
                                                                  						do not know the value for session-server-tag , we recommend using 1. |
|---|---|

| Feature Name | Cisco Unified CME Version | Modification |
|---|---|---|
| Interoperability with Cisco Unified CCX | 4.2 | Enables interoperability between Cisco Unified CME and Cisco
                                          					 Customer Response Solutions (CRS) 5.0 and later versions with Cisco Unified
                                          					 Contact Center Express (Cisco Unified CCX), including Cisco Unified IP IVR,
                                          					 enhanced call processing, device and call monitoring, unattended call transfers
                                          					 to multiple call center agents, and basic extension mobility. |