---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-sip-configuration-15-mt-sip-config-15-mt-book-voi-sip-hookflash-html-27704bf27f
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/sip/configuration/15-mt/sip-config-15-mt-book/voi-sip-hookflash.html
retrieved_at: 2026-08-20T23:46:02.416481+00:00
---

SIP Configuration Guide, Cisco IOS Release 15M&T

# SIP Configuration Guide, Cisco IOS Release 15M&T

Updated: November 25, 2014

Chapter: Configuring SIP Support for Hookflash

## Chapter: Configuring SIP Support for Hookflash

# Configuring SIP Support for Hookflash

This chapter contains information about the SIP Support for Hookflash feature that allows you to configure IP Centrex supplementary
                        services on SIP-enabled, Foreign Exchange Station (FXS) lines. Supplementary services for the SIP Support for Hookflash feature
                        include the following:

Call hold

Call waiting

Call transfer

3-Way conferencing

Use the service dsapp command to configure supplementary Centrex-like features on FXS phones to interwork with SIP-based soft switches. The SIP
                        Support for Hookflash feature supports the concept of a dual-line (ACTIVE and STANDBY for active and held calls) for FXS calls
                        to support supplementary services. Hookflash triggers supplementary services based on the current state of the call.

You can configure the service dsapp command on individual dial peers, or configure globally for all calls entering the gateway.

## Prerequisites for SIP Support for Hookflash

### All Hookflash Features for FXS Ports

Ensure that the gateway has voice functionality that is configurable for SIP.

Establish a working IP network. For information on configuring IP, see the Cisco IOS IP Configuration Guide , Release 12.3.

Configure VoIP.

## Restrictions for SIP Support for Hookflash

Release by any party other than controller causes the conference to be released when Packet Voice Digital Signal Processor
                                 (DSP) Module (PVDM2) is used.

Release by any party on cascading 3-Way Conference, releases all the calls.

Invocation of features such as Call Hold, Blind Transfer, Semi-Attended Transfers after establishment of 3-Way Conference,
                                 releases all the calls.

Semi-attended transfer is not possible between users connected to gateways using G729 codec with CUCM. With G711 codec,
                                 semi-attended transfer is possible using CUCM.

## Information About SIP Support for Hookflash

Use the service dsapp command to configure supplementary Centrex-like services on FXS phones to interwork with SIP-based softswitches. Hookflash
                           triggers supplementary features based on the current state of the call and provides a simulation of dual-line capability for
                           analog phones to allow one line to be active while the other line is used to control supplementary IP Centrex services. Supplementary
                           services for the SIP Support for Hookflash feature include the following:

### Call Hold

With the Call Hold feature, you can place a call on hold. When you are active with a call and you press hookflash, and there
                              is no call that is waiting, you hear a dial tone.

If there is a call on hold, the hookflash switches between two calls; the call on hold becomes active while the active call
                              is put on hold.

If you have a call on hold and the call hangs up, the call on hold is disconnected.

#### Call Holding Flows

The sequence of placing a call on hold is summarized in the following steps:

User A and user B are active with a call.

By pressing hookflash, user A initiates a call hold.

SIP sends a call hold indication to user B.

User A can now initiate another active call (user C), transfer the active call (call transfer), or respond to a call-waiting
                                       indication.

Use the offer call-hold command in sip-ua configuration mode to configure the method of hold used on the gateway. For detailed information on the offer call-hold command, see the Cisco IOS Voice Command Reference Guide .

User A receives a second dial tone and presses hookflash.

The figure below shows the initiation of the calls hold sequence.

User A and User B reconnect.

The figure below shows the calls on hold resume sequence.

The table below summarizes the hookflash support for Call Hold services.

State

Action

Result

Response to FXS Line

Active call

Hookflash

Call placed on hold for remote party.

Second dial tone for FXS phone.

Call on hold

Hookflash

Active call.

FXS line connects to call.

Call on hold and active call

Hookflash

Active and call on hold are swapped.

FXS line connects to previous held call.

On hook

Active call is dropped.

Held call still active. Reminder ring on FXS line.

Call on hold goes on hook

Call on hold is dropped.

None.

Active call goes on hook

Active call is dropped.

Silence. Reconnects to held call after the value you specify for disc-toggle-time expires. See "How to Configure Disconnect Toggle Time".

### Call Waiting

With the Call Waiting feature, you can receive a second call while you
                              		are on the phone with another call. When you receive a second call, you hear a
                              		call-waiting tone (a tone with a 300 ms duration). Caller ID appears on phones
                              		that support caller ID. You can use hookflash to answer a waiting call and
                              		place the previously active call on hold. By using hookflash, you can toggle
                              		between the active and a call that is on hold. If the Call Waiting feature is
                              		disabled, and you hang up the current call, the second call will hear a busy
                              		tone.

The call-waiting sequence is summarizes in the following steps:

User A is active with a
                                    		  call to user B

User C calls user B

User B presses hookflash.

The call between user A and user B is held.

User B connects to user C.

The figure below shows the call waiting sequence.

The table below summarizes hookflash support for Call Waiting services.

State

Action

Result

Response to FXS Line

Active call and waiting call

Hookflash

Swap active call and waiting call.

FXS line connects to waiting call.

Active call disconnects

Active call is disconnected.

Silence.

Waiting call goes disconnects

Stay connected to active call.

None.

Call disconnects

Active call is dropped.

Reminder ring on FXS line.

### Call Transfers

Call transfers are when active calls are put on hold while a second call is established between two users. After you establish
                              the second call and terminate the active call, the call on hold will hear a ringback. The Call Transfer feature supports all
                              three types of call transfers--blind, semi-attended, and attended.

#### Blind Call Transfer

The following describes a typical Blind call-transfer scenario:

User A calls user B.

User B (transferrer) presses hookflash, places user A (transferee) on hold, and dials user C (transfer-to).

User B will not hear alerting for the time you configure. See "How to Configure Blind Transfer Wait Time".

Before the Blind call transfer trigger timer expires, user B disconnects, and the call between user A and user B is terminated.

User A is transferred to user C and hears a ringback if user C is available. If user C is busy, user A hears a busy tone;
                                       if user C is not busy and answers, user A and user C connect.

The figure below shows the call sequence for a Blind call transfer.

#### Semi-Attended Transfers

The following is a typical semi-attended transfer scenario:

User A calls user B.

User B places user A on hold and dials user C.

After user B hears a ringback and user C rings, user B initiates a transfer, and the call between user A and user B is terminated.

User A is transferred to user C and hears a ringback if user C is available. If user C is busy, user A hears a busy tone.

If user C is not busy and answers, user A and user C connect.

The figure below shows the call details for a semi-attended transfer.

#### Attended Transfers

The following describes a typical attended transfer:

User A calls user B.

User B places user A on hold and dials user C.

After user C answers, user B goes on-hook to initiate a transfer, and the call between user A and user B is terminated.

User A is transferred to user C. If user C is busy when user B calls, user A hears a busy tone.

If user C is not busy and answers, user A and user C connect.

The figure below shows the call details for an attended transfer.

The table below summarizes the hookflash support for Call Transfer services.

State

Action

Result

Response to FXS Line

Active call

Hookflash.

Call placed on hold.

Second dial tone.

Call on hold and outgoing dialed or alerting, or active call

On hook.

Call on hold and active call transferred.

--

Call on hold and outgoing alerting call

Hookflash

Active call dropped.

FXS line connects to call o hold.

### 3-Way Conference

You can use the 3-Way
                              		Conference feature to establish two calls with a single connection so that all
                              		three parties can talk together. If the 3-Way Conference feature is disabled, a
                              		second hookflash will toggle between the two calls.

The 3-Way
                                          		  Conference feature supports only those SIP calls that use the g711 or g729
                                          		  codecs. This feature also supports specification GR-577-CORE.

#### Setting Up a 3-Way
                              	 Conference

The following
                                 		describes a typical 3-way conference scenario:

User A is talking
                                       			 with user B (a second-party call).

User A presses
                                       			 hookflash, receives a dial-tone, and dials user C.

User C answers.
                                       			 User A and user C are active in a second-party call.

User A presses
                                       			 hookflash to activate a 3-way conference.

In other terminology,
                                 		user A is the host or controller; user B is the original call; and user C is
                                 		the add-on.

The 3-Way
                                             		  Conference feature is available when the second-party call is outgoing. If the
                                             		  second-party call is incoming and you press hookflash, the phone toggles
                                             		  between the two calls.

The figure below
                                 		shows the call details for 3-way conferencing.

The table below
                                 		summarizes the hookflash support for 3-way conferencing services.

State

Action

Result

Response to
                                             				  FXS Line

Active call

Hookflash

Call place on
                                             				  hold.

Second dial
                                             				  tone

Call on hold
                                             				  and active call

Join call on
                                             				  hold and active call.

Media mixing
                                             				  of both calls

#### Terminating a 3-Way
                              	 Conference

The table below
                                 		summarizes the termination of a 3-way conference:

State

Action

Result

Response to
                                             				  FXS Line

Active 3-way
                                             				  conference

User A
                                             				  disconnects first

3-Way
                                             				  conference terminates; all users are disconnected.

Dial tone

User B
                                             				  disconnects first

User A and
                                             				  user C establish a second-party call.

FXS line
                                             				  connects user A and user C.

User C
                                             				  disconnects first

User A and
                                             				  user B establish a second-party call.

FXS line
                                             				  connects user A and user B.

User A
                                             				  presses hookflash

User C
                                             				  disconnects and user A and user B establish a second-party call.

FXS line
                                             				  connects user A and user B.

## How to Configure and Associate SIP Support for Hookflash

This section describes the procedures for configuring and associating the SIP Support for Hookflash feature. These procedures
                           include the following:

Configuring supplementary service by using the service dsapp command.

Associating the supplementary services with configured dial peers.

or

Associating the supplementary services as the global default application on a gateway.

This section provides configurations for the following supplementary services and provides configuration for associating supplementary
                           services with dial peers:

### How to Configure Call Hold

### SUMMARY STEPS

- enable

- configure terminal

- application

- service dsapp

- param callHold TRUE

- exit

### DETAILED STEPS

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

application

#### Example:

```
Router(config)# application
```

Enters SIP gateway-application configuration mode.

service dsapp

#### Example:

```
Router(config-app)# service dsapp
```

Enters DSAPP parameters mode.

param callHold TRUE

#### Example:

```
Router(config-app-param)# param callHold TRUE
```

Enables call hold.

exit

#### Example:

```
Router (config-app-param)# exit
```

Exits the current mode.

### How to Configure Call Waiting

To enable call waiting for a DSAPP, follow these steps:

### SUMMARY STEPS

- enable

- configure terminal

- application

- service dsapp

- param callWaiting TRUE

- exit

### DETAILED STEPS

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

application

#### Example:

```
Router(config)# application
```

Enters SIP gateway-application configuration mode.

service dsapp

#### Example:

```
Router(config-app)# service dsapp
```

Enters DSAPP parameters mode.

param callWaiting TRUE

#### Example:

```
Router(config-app-param)# param callWaiting TRUE
```

Enables call waiting.

exit

#### Example:

```
Router (config-app-param)# exit
```

Exits the current mode.

### How to Configure Call Transfer

### SUMMARY STEPS

- enable

- configure terminal

- application

- service dsapp

- param callTransfer TRUE

- exit

### DETAILED STEPS

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

application

#### Example:

```
Router (config)# application
```

Enters SIP gateway-application configuration mode.

service dsapp

#### Example:

```
Router(config-app)# service dsapp
```

Enters DSAPP parameters mode.

param callTransfer TRUE

#### Example:

```
Router(config-app-param)# param callTransfer TRUE
```

Enables call transfer.

exit

#### Example:

```
Router(config-app-param)# exit
```

Exits the current mode.

### How to Configure 3-Way Conferencing

### SUMMARY STEPS

- enable

- configure terminal

- application

- service dsapp

- param callConference TRUE

- exit

### DETAILED STEPS

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

application

#### Example:

```
Router (config)# application
```

Enters SIP gateway-application configuration mode.

service dsapp

#### Example:

```
Router(config-app)# service dsapp
```

Enters DSAPP parameters mode.

param callConference TRUE

#### Example:

```
Router(config-app-param)# param callConference TRUE
```

Enables 3-way conferencing.

exit

#### Example:

```
Router(config-app-param)# exit
```

Exits the current mode.

### How to Configure Disconnect Toggle Time

You can configure the time to wait before switching to a call on hold if an active call disconnects (commonly known as disconnect
                                 toggle time). You can configure a time-to-wait range between 10 (default) and 30 seconds.

### SUMMARY STEPS

- enable

- configure terminal

- application

- service dsapp

- param disc-toggle-time seconds

- exit

### DETAILED STEPS

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

application

#### Example:

```
Router (config)# application
```

Enters SIP gateway-application configuration mode.

service dsapp

#### Example:

```
Router(config-app)# service dsapp
```

Enters DSAPP parameters mode.

param disc-toggle-time seconds

#### Example:

```
Router(config-app-param)# param disc-toggle-time 20
```

Sets the time to wait before switching to a call on hold, if the active call disconnects (disconnect toggle time). You can
                                             specify a disconnect toggle time between 10 (default) and 30 seconds.

exit

#### Example:

```
Router(config-app-param)# exit
```

Exits the current mode.

### How to Configure Blind Transfer Wait Time

To configure the time the system waits before establishing a call, so that you can transfer a call by placing the phone on
                                 hook, proceed with the following steps.

The transferrer will not hear the alert for the time you configure because the system delays the call in case blind transfer
                                             is initiated.

### SUMMARY STEPS

- enable

- configure terminal

- application

- service dsapp

- param blind-xfer-wait-time time

- exit

### DETAILED STEPS

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

application

#### Example:

```
Router(config)# application
```

Enters SIP gateway-application configuration mode.

service dsapp

#### Example:

```
Router(config-app)# service dsapp
```

Enters DSAPP parameters mode.

param blind-xfer-wait-time time

#### Example:

```
Router(config-app-param)# param blind-xfer-wait-time 10
```

Enables call waiting.

exit

#### Example:

```
Router (config-app-param)# exit
```

Exits the current mode.

### How to Associate Services with a Fixed Dial Peer

After you have enabled and customized your services on a gateway by using the service dsapp command, you must associate these services with configured dial peers. You can associate individual dial peers, or alternately,
                                 you can configure these services globally on the gateway (see "How to Associate Services Globally on a Gateway"). If you associate
                                 these services globally, all calls entering from the FXS line side and from the SIP trunk side invoke the service dsapp services.

To configure a fixed dial peer used by DSAPP to set up a call to the SIP server (trunk) side, proceed with the following
                                 steps:

### SUMMARY STEPS

- enable

- configure terminal

- application

- service dsapp

- param dialpeer dial-peer-tag

- exit

### DETAILED STEPS

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

application

#### Example:

```
Router(config)# application
```

Enters SIP gateway-application configuration mode.

service dsapp

#### Example:

```
Router (config-app)# service dsapp
```

Enters DSAPP parameters mode.

param dialpeer dial-peer-tag

#### Example:

```
Router(config-app-param)# param dialpeer 5000
```

Configures a fixed dial peer used by DSAPP to set up a call to the SIP server (trunk) side, where dial-peer-tag is the tag of the dial peer used to place an outgoing call on the IP trunk side. The dial-peer-tag must be the same tag as the dial peer configured to the SIP server.

exit

#### Example:

```
Router(config-app-param)# exit
```

Exits the current mode.

### How to Associate Services Globally on a Gateway

After you have enabled and customized your services on a gateway by using the service dsapp command, you must associate these services with configured dial peers. You can associate individual dial peers ("How to Associate
                                 Services with a Fixed Dial Peer"), or alternately, you can configure these services globally on the gateway. If you associate
                                 these services globally, all calls entering from the FXS line side and from the SIP trunk side will invoke the service dsapp services.

### SUMMARY STEPS

- enable

- configure terminal

- application

- global

- service default dsapp

- exit

### DETAILED STEPS

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

application

#### Example:

```
Router(config)# application
```

Enters SIP gateway-application configuration mode.

global

#### Example:

```
Router (config-app)# global
```

Enters SIP gateway-application-global configuration mode.

service default dsapp

#### Example:

```
Router (config-app-global)# service default dsapp
```

Globally sets dsapp as the default application. All calls entering the gateway (from the FXS line side and the SIP trunk
                                             side) invoke the dsapp application.

exit

#### Example:

```
Router(config-app-global)# exit
```

Exits the current mode.

### Verifying SIP Support for Hookflash

After the 3-way conference is established, perform this task to verify the codec used for the conference.

### SUMMARY STEPS

- enable

- show call active voice compact

### DETAILED STEPS

enable

#### Example:

```
Device> enable
```

Enables privileged EXEC mode.

show call active voice compact

#### Example:

```
Device# show call active voice compact <callID>  A/O FAX T<sec> Codec       type        Peer Address       IP R<ip>:<udp>
Total call-legs: 3
   6358  ANS   T209     g729br8      VOIP        P1006            9.40.3.244:16442
   6359  ORG   T210     g729br8      TELE        P1995
   6363  ORG   T175     g729br8      VOIP        P1111008       9.40.3.245:16386
```

### Troubleshooting SIP Support for Hookflash

You can use the following commands to troubleshoot the SIP Support for Hookflash feature:

debug voice application session

debug ccsip all (SIP message level debug)

debug voice ccapi inout

## Configuration Examples for SIP Support for Hookflash

### Configuring Call Hold Example

```
Gateway# configure terminal Enter configuration commands, one per line. End with CNTL/Z.
Gateway(conf)# application Gateway(config-app)# service dsapp Gateway
(config-app-param)# param callHold TRUE
```

### Configuring Call Waiting Example

```
Gateway# configure terminal Enter configuration commands, one per line. End with CNTL/Z.
Gateway(conf)# application Gateway(config-app)# service dsapp Gateway
(config-app-param)# param callWaiting TRUE
```

### Configuring Call Transfer Example

```
Gateway# configure terminal Enter configuration commands, one per line. End with CNTL/Z.
Gateway(conf)# application Gateway(config-app)# service dsapp Gateway
(config-app-param)# param callTransfer TRUE
```

### Configuring 3-Way Conferencing Example

```
Gateway# configure terminal Enter configuration commands, one per line. End with CNTL/Z.
Gateway(conf)# application Gateway(config-app)# service dsapp Gateway
(config-app-param)# param callConference TRUE
```

### Configuring Disconnect Toggle Time  Example

In this example, a disconnect toggle time is configured; the toggle time specifies the amount of time in seconds the system
                                 waits before committing the call transfer, after the originating call is placed on hook.

```
Gateway# configure terminal Enter configuration commands, one per line. End with CNTL/Z.
Gateway(conf)# application Gateway(config-app)# service dsapp Gateway(config-app-param)# param disc-toggle-time 10
```

### Configuring Blind Transfer Wait Time  Example

In this example, a blind transfer wait time is configured that specifies the amount of time in seconds the system waits before
                                 committing the call transfer after the originating call is placed on hook.

```
Gateway# configure terminal Enter configuration commands, one per line. End with CNTL/Z.
Gateway(conf)# application Gateway(config-app)# service dsapp Gateway(config-app-param)# param blind-xfer-wait-time 10
```

### Configuring a Fixed Dial Peer Used for Outgoing Calls on SIP Trunk Side  Example

In this example, a fixed dial peer is configured to set up the call to the SIP server (trunk) side.

```
Gateway# configure terminal Enter configuration commands, one per line. End with CNTL/Z.
Gateway(conf)# application Gateway(config-app)# service dsapp Gateway(config-app-param)# param dialpeer 5000
```

### Associating Services with a Fixed Dial Peer  Example

In this example, a fixed dial peer is configured to set up the call to the SIP server (trunk) side. The line in bold shows
                                 the dial peer statement.

```
Gateway# show running log .
!
application
 service dsapp
 param dialpeer 1234
 param disc-toggle-time 15
 param callWaiting TRUE
 param callConference TRUE
 param blind-xfer-wait-time 10
 param callTransfer TRUE
!
voice-port 1/0/0
 station-id-name Example1
 station-id number 1234567890
!
voice-port 1/0/1
 station-id-name Example2
 station-id number 1234567891
!
voice-port 1/0/2
 station-id-name Example31
 station-id number 1234567892
!
dial-peer voice 1234 voip
 service dsapp
 destination-pattern.T
 session protocol sipv2
 session target ipv4:10.1.1.1
 dtmf-relay rtp-nte
 codec g711ulaw
!
dial-peer voice 9753 voip
 service dsapp
 destination-pattern.T
 session protocol sipv2
 session target ipv4:15.0.0.15
 dtmf-relay rtp-nte
 codec g729r8
!
dial-peer voice 100 pots
 service dsapp
 destination-pattern.1234567890
 port 1/0/0
 prefix 1234567890
!
dial-peer voice 101 pots
 service dsapp
 destination-pattern.1234567891
 port 1/0/1
 prefix 1234567891
!
dial-peer voice 102 pots
 service dsapp
 destination-pattern.1234567892
 port 1/0/2
 prefix 1234567892
!
!
sip-ua
 registar ipv4:10.1.1.1 expires 3600
!
```

### Associating Services Globally on a Gateway  Example

In this example, the gateway is associated globally with supplementary services. The lines in bold show the dial peer statement.

```
Gateway# show running log .
!
application
 service dsapp
 param disc-toggle-time 15
 param callWaiting TRUE
 param callConference TRUE
 param blind-xfer-wait-time 10
 param callTransfer TRUE
!
voice-port 1/0/0
 station-id-name Example1
 station-id number 1234567890
!
voice-port 1/0/1
 station-id-name Example2
 station-id number 1234567891
!
voice-port 1/0/2
 station-id-name Example31
 station-id number 1234567892
!
dial-peer voice 1234 voip
 service dsapp
 destination-pattern 1800T
 session protocol sipv2
 session target ipv4:10.1.1.1
 dtmf-relay rtp-nte
 codec g729r8
!
dial-peer voice 9753 voip
 service dsapp
 destination-pattern.T
 session protocol sipv2
 session target ipv4:10.1.1.1
 dtmf-relay rtp-nte
 codec g711ulaw
!
dial-peer voice 100 pots
 preference 8
 service dsapp
 destination-pattern.6234567890
 port 1/0/0
 prefix 6234567890
!
dial-peer voice 101 pots
 preference 8
 service dsapp
 destination-pattern.6234567892
 port 1/0/1
 prefix 6234567892
!
dial-peer voice 102 pots
 preference 8
 service dsapp
 destination-pattern.6234567893
 port 1/0/2
 prefix 6234567893
!
!
dial-peer hunt 2
!
sip-ua
 registar ipv4:10.1.1.1 expires 3600
!
```

## Additional References

The following sections provide references related to the SIP Support
                              		  for Hookflash feature.

### MIBs

MIB

MIBs Link

None

To locate and download MIBs for selected platforms, Cisco
                                          						IOS releases, and feature sets, use Cisco MIB Locator found at the following
                                          						URL:

http://www.cisco.com/go/mibs

### Technical Assistance

Description

Link

The Cisco Technical Support website contains thousands of
                                          						pages of searchable technical content, including links to products,
                                          						technologies, solutions, technical tips, and tools. Registered Cisco.com users
                                          						can log in from this page to access even more content.

http://www.cisco.com/techsupport

## Feature Information for SIP Support for Hookflash

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

SIP Support for Hookflash

12.4(11)T

This feature was introduced. SIP Support for Hookflash feature allows you to configure IP Centrex supplementary services
                                          on SIP-enabled, Foreign Exchange Station (FXS) lines.

SIP Support for Hookflash

15.4(2)T

The feature was enhanced to support hookflash using G729 codec for 3-way conference.

| Note | Use the offer call-hold command in sip-ua configuration mode to configure the method of hold used on the gateway. For detailed information on the offer call-hold command, see the Cisco IOS Voice Command Reference Guide . |
|---|---|

| State | Action | Result | Response to FXS Line |
|---|---|---|---|
| Active call | Hookflash | Call placed on hold for remote party. | Second dial tone for FXS phone. |
| Call on hold | Hookflash | Active call. | FXS line connects to call. |
| Call on hold and active call | Hookflash | Active and call on hold are swapped. | FXS line connects to previous held call. |
| On hook | Active call is dropped. | Held call still active. Reminder ring on FXS line. |
| Call on hold goes on hook | Call on hold is dropped. | None. |
| Active call goes on hook | Active call is dropped. | Silence. Reconnects to held call after the value you specify for disc-toggle-time expires. See "How to Configure Disconnect Toggle Time". |

| State | Action | Result | Response to FXS Line |
|---|---|---|---|
| Active call and waiting call | Hookflash | Swap active call and waiting call. | FXS line connects to waiting call. |
| Active call disconnects | Active call is disconnected. | Silence. |
| Waiting call goes disconnects | Stay connected to active call. | None. |
| Call disconnects | Active call is dropped. | Reminder ring on FXS line. |

| Note | User B will not hear alerting for the time you configure. See "How to Configure Blind Transfer Wait Time". |
|---|---|

| State | Action | Result | Response to FXS Line |
|---|---|---|---|
| Active call | Hookflash. | Call placed on hold. | Second dial tone. |
| Call on hold and outgoing dialed or alerting, or active call | On hook. | Call on hold and active call transferred. | -- |
| Call on hold and outgoing alerting call | Hookflash | Active call dropped. | FXS line connects to call o hold. |

| Note | The 3-Way
                                          		  Conference feature supports only those SIP calls that use the g711 or g729
                                          		  codecs. This feature also supports specification GR-577-CORE. |
|---|---|

| Note | The 3-Way
                                             		  Conference feature is available when the second-party call is outgoing. If the
                                             		  second-party call is incoming and you press hookflash, the phone toggles
                                             		  between the two calls. |
|---|---|

| State | Action | Result | Response to
                                             				  FXS Line |
|---|---|---|---|
| Active call | Hookflash | Call place on
                                             				  hold. | Second dial
                                             				  tone |
| Call on hold
                                             				  and active call | Join call on
                                             				  hold and active call. | Media mixing
                                             				  of both calls |

| State | Action | Result | Response to
                                             				  FXS Line |
|---|---|---|---|
| Active 3-way
                                             				  conference | User A
                                             				  disconnects first | 3-Way
                                             				  conference terminates; all users are disconnected. | Dial tone |
| User B
                                             				  disconnects first | User A and
                                             				  user C establish a second-party call. | FXS line
                                             				  connects user A and user C. |
| User C
                                             				  disconnects first | User A and
                                             				  user B establish a second-party call. | FXS line
                                             				  connects user A and user B. |
| User A
                                             				  presses hookflash | User C
                                             				  disconnects and user A and user B establish a second-party call. | FXS line
                                             				  connects user A and user B. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | application Example: Router(config)# application | Enters SIP gateway-application configuration mode. |
| Step 4 | service dsapp Example: Router(config-app)# service dsapp | Enters DSAPP parameters mode. |
| Step 5 | param callHold TRUE Example: Router(config-app-param)# param callHold TRUE | Enables call hold. |
| Step 6 | exit Example: Router (config-app-param)# exit | Exits the current mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | application Example: Router(config)# application | Enters SIP gateway-application configuration mode. |
| Step 4 | service dsapp Example: Router(config-app)# service dsapp | Enters DSAPP parameters mode. |
| Step 5 | param callWaiting TRUE Example: Router(config-app-param)# param callWaiting TRUE | Enables call waiting. |
| Step 6 | exit Example: Router (config-app-param)# exit | Exits the current mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | application Example: Router (config)# application | Enters SIP gateway-application configuration mode. |
| Step 4 | service dsapp Example: Router(config-app)# service dsapp | Enters DSAPP parameters mode. |
| Step 5 | param callTransfer TRUE Example: Router(config-app-param)# param callTransfer TRUE | Enables call transfer. |
| Step 6 | exit Example: Router(config-app-param)# exit | Exits the current mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | application Example: Router (config)# application | Enters SIP gateway-application configuration mode. |
| Step 4 | service dsapp Example: Router(config-app)# service dsapp | Enters DSAPP parameters mode. |
| Step 5 | param callConference TRUE Example: Router(config-app-param)# param callConference TRUE | Enables 3-way conferencing. |
| Step 6 | exit Example: Router(config-app-param)# exit | Exits the current mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | application Example: Router (config)# application | Enters SIP gateway-application configuration mode. |
| Step 4 | service dsapp Example: Router(config-app)# service dsapp | Enters DSAPP parameters mode. |
| Step 5 | param disc-toggle-time seconds Example: Router(config-app-param)# param disc-toggle-time 20 | Sets the time to wait before switching to a call on hold, if the active call disconnects (disconnect toggle time). You can
                                             specify a disconnect toggle time between 10 (default) and 30 seconds. |
| Step 6 | exit Example: Router(config-app-param)# exit | Exits the current mode. |

| Note | The transferrer will not hear the alert for the time you configure because the system delays the call in case blind transfer
                                             is initiated. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | application Example: Router(config)# application | Enters SIP gateway-application configuration mode. |
| Step 4 | service dsapp Example: Router(config-app)# service dsapp | Enters DSAPP parameters mode. |
| Step 5 | param blind-xfer-wait-time time Example: Router(config-app-param)# param blind-xfer-wait-time 10 | Enables call waiting. |
| Step 6 | exit Example: Router (config-app-param)# exit | Exits the current mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | application Example: Router(config)# application | Enters SIP gateway-application configuration mode. |
| Step 4 | service dsapp Example: Router (config-app)# service dsapp | Enters DSAPP parameters mode. |
| Step 5 | param dialpeer dial-peer-tag Example: Router(config-app-param)# param dialpeer 5000 | Configures a fixed dial peer used by DSAPP to set up a call to the SIP server (trunk) side, where dial-peer-tag is the tag of the dial peer used to place an outgoing call on the IP trunk side. The dial-peer-tag must be the same tag as the dial peer configured to the SIP server. |
| Step 6 | exit Example: Router(config-app-param)# exit | Exits the current mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | application Example: Router(config)# application | Enters SIP gateway-application configuration mode. |
| Step 4 | global Example: Router (config-app)# global | Enters SIP gateway-application-global configuration mode. |
| Step 5 | service default dsapp Example: Router (config-app-global)# service default dsapp | Globally sets dsapp as the default application. All calls entering the gateway (from the FXS line side and the SIP trunk
                                             side) invoke the dsapp application. |
| Step 6 | exit Example: Router(config-app-global)# exit | Exits the current mode. |

| Step 1 | enable Example: Device> enable Enables privileged EXEC mode. |
|---|---|
| Step 2 | show call active voice compact Example: Device# show call active voice compact <callID>  A/O FAX T<sec> Codec       type        Peer Address       IP R<ip>:<udp>
Total call-legs: 3
   6358  ANS   T209     g729br8      VOIP        P1006            9.40.3.244:16442
   6359  ORG   T210     g729br8      TELE        P1995
   6363  ORG   T175     g729br8      VOIP        P1111008       9.40.3.245:16386 |

| MIB | MIBs Link |
|---|---|
| None | To locate and download MIBs for selected platforms, Cisco
                                          						IOS releases, and feature sets, use Cisco MIB Locator found at the following
                                          						URL: http://www.cisco.com/go/mibs |

| Description | Link |
|---|---|
| The Cisco Technical Support website contains thousands of
                                          						pages of searchable technical content, including links to products,
                                          						technologies, solutions, technical tips, and tools. Registered Cisco.com users
                                          						can log in from this page to access even more content. | http://www.cisco.com/techsupport |

| Feature Name | Releases | Feature Information |
|---|---|---|
| SIP Support for Hookflash | 12.4(11)T | This feature was introduced. SIP Support for Hookflash feature allows you to configure IP Centrex supplementary services
                                          on SIP-enabled, Foreign Exchange Station (FXS) lines. |
| SIP Support for Hookflash | 15.4(2)T | The feature was enhanced to support hookflash using G729 codec for 3-way conference. |