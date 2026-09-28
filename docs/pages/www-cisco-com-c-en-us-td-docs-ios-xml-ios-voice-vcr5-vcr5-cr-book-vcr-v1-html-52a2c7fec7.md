---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-vcr5-vcr5-cr-book-vcr-v1-html-52a2c7fec7
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/vcr5/vcr5-cr-book/vcr-v1.html
retrieved_at: 2026-08-16T23:16:20.732503+00:00
---

Cisco IOS Voice Command Reference - T through Z

# Cisco IOS Voice Command Reference - T through Z

Updated: April 25, 2026

Chapter: vad (dial peer) through voice-class sip encap clear-channel

## Chapter: vad (dial peer) through voice-class sip encap clear-channel

# vad (dial peer) through voice-class sip encap clear-channel

## vad (dial peer)

To enable voice activity detection (VAD) for calls using a specific dial peer, use the vad command in dial-peer configuration mode. To disable VAD, use the no form of this command.

vad [ aggressive ]

no vad [ aggressive ]

### Syntax Description

aggressive

Reduces noise threshold from -78 to -62 dBm. Available only when session protocol multicast is configured.

### Command Default

VAD is enabled

Aggressive VAD is enabled in multicast dial peers

### Command Modes

Dial-peer configuration

## Command History

Release

Modification

11.3(1)T

This command was introduced on the Cisco 3600 series.

12.0(4)T

This command was implemented as a dial-peer command on Cisco MC3810 (in prior releases, the vad command was available only as a voice-port command).

12.2(11)T

The aggressive keyword was added.

Introduced support for YANG models.

### Usage Guidelines

Use this command to enable voice activity detection. With VAD, voice data packets fall into three categories: speech, silence, and
                              unknown. Speech and unknown packets are sent over the network; silence packets are discarded. The sound quality is slightly
                              degraded with VAD, but the connection monopolizes much less bandwidth. If you use the no form of this command, VAD is disabled and voice data is continuously sent to the IP backbone. When configuring voice gateways
                              to handle fax calls, VAD should be disabled at both ends of the IP network because it can interfere with the successful reception
                              of fax traffic.

When the aggressive keyword is used, the VAD noise threshold is reduced from -78 to -62 dBm. Noise that falls below the -62 dBm threshold is
                              considered to be silence and is not sent over the network. Additionally, unknown packets are considered to be silence and
                              are discarded.

## Examples

The following example enables VAD for a Voice over IP (VoIP) dial peer, starting from global configuration mode:

```
dial-peer voice 200 voip
 vad
```

### Related Commands

Command

Description

comfort-noise

Generates background noise to fill silent gaps during calls if VAD is activated.

dial-peer voice

Enters dial-peer configuration mode, defines the type of dial peer, and defines the tag number associated with a dial peer.

vad (voice-port)

Enables VAD for the calls using a particular voice port.

## vad (SPA-DSP)

To enable or disable voice activity detection (vad) settings configured locally irrespective of the external vad settings,
                              use the vad command in config dspfarm profile mode.

vad { on | off } override

### Syntax Description

on

Enables the local vad settings irrespective of the external vad settings.

off

Disables the local vad settins irrespective of the external vad settings.

override

Overrides the external vad settings with local vad configuration details.

### Command Default

By default, VAD is enabled.

### Command Modes

DSP Farm Profile Configuration Mode (config-dspfarm-profile)

## Command History

Release

Modification

Cisco IOS XE 
                                          Release 3.2S

This command was introduced.

### Usage Guidelines

Use this command to enable voice activity detection locally irrespective of external VAD settings. With VAD, voice data packets
                              fall into three categories: speech, silence, and unknown. Speech and unknown packets are sent over the network; silence packets
                              are discarded. The sound quality is slightly degraded with VAD, but the connection monopolizes much less bandwidth. If you
                              disable VAD, voice data is continuously sent to the IP backbone.

## Examples

The following example enables VAD and overrides external vad settings with local vad settings:

```
Router(config)# dspfarm profile 1 Router(config-dspfarm-profile)# vad on override Router(config-dspfarm-profile)# do show running-config !!!
dspfarm profile 1 transcode
 codec g711ulaw
 codec g711alaw
 codec g729ar8
 codec g729abr8
 maximum sessions 588
 associate application SBC
 vad on override
!
```

The following example disables local vad settings and overrides external vad setting configuration:

```
Router(config)# dspfarm profile 1 Router(config-dspfarm-profile)# vad off override Router(config-dspfarm-profile)# do show running-config !!!
dspfarm profile 1 transcode
 codec g711ulaw
 codec g711alaw
 codec g729ar8
 codec g729abr8
 maximum sessions 588
 associate application SBC
 vad off override
!
```

### Related Commands

Command

Description

dsp services dspfarm

Enables the DSP-farm services.

dspfarm profile

Enters the DSP farm profile configuration mode, and defines a profile for the DSP farm services.

show dspfarm (SPA-DSP)

Displays DSP farm service information, such as operational status and DSP resource allocation for transcoding.

## vbd-playout-delay

To configure the voice-band-detection playout-delay buffer on a Cisco router, use the vbd-playout-delay command in voice service session configuration mode. To disable the buffer, use the no form of this command.

vbd-playout-delay { maximum milliseconds | minimum milliseconds | mode { fixed [ no-timestamps ] | passthrough } | nominal milliseconds }

no vbd-playout-delay

### Syntax Description

maximum

Sets the maximum playout buffer delay, in milliseconds (ms). Range: 40 to 1000. Default: 1000.

milliseconds

Delay time, in milliseconds (ms).

minimum

Sets the minimum playout buffer delay, in ms. Range: 10 to 40. Default: 40.

mode

Configures voice-band-detection playout buffer adaptation mode.

fixed

Sets the jitter buffer to a constant delay.

no-timestamps

(Optional) Fixes the jitter buffer at a constant delay without time stamps.

passthrough

Sets the jitter buffer passthrough mode for clock compensation.

nominal

Sets the nominal playout buffer delay, in ms. Range:10 to 1000. Default: 60.

### Command Default

The voice-band-detection playout-delay buffer is disabled.

### Command Modes

Voice service session configuration (conf-voi-serv-sess)

## Command History

Release

Modification

12.2(8)T

This command was introduced.

12.4(24)T

This command was modified.

The minimum time range value was changed from 4 to 1700 ms to a range of 10  to 40 ms. The default value 4 was increased to
                                                40 ms.

The maximum time value was decreased from 1700 to 1000 ms and the default of 200 was increased to 1000 ms.

The nominal time range value was changed from 0 to 1500 ms to a range of 10 to 1000 ms. The default value of 100 was decreased
                                                to 60 ms.

12.4(24)T6

This command was modified. The no-timestamps keyword was added and passthrough keyword usage guidelines were clarified.

### Usage Guidelines

Use this command to set the playout jitter buffer. When a voice band is detected, the call uses the G.711 codec, and the playout delay
                              values that you set are picked up. The original voice-call parameters are restored after the fax or modem call is completed.
                              The no-timestamps keyword sets the jitter buffer at a constant delay without reading time stamps.

The passthough keyword is a special mode used to handle clock drifting properly. We recommend this keyword only when instructed by your
                                          Cisco representative.

## Examples

The following example configures ATM adaptation layer 2 (AAL2) voice-band-detection playout-delay adaptation mode and sets
                              the mode to fixed:

```
voice service voatm
 session protocol aal2
  vbd-playout-delay mode fixed
```

The following example configures AAL2 voice-band-detection playout-delay adaptation mode and sets the mode at a constant delay
                              without timestamps:

```
voice service voatm
 session protocol aal2
  vbd-playout-delay mode fixed no-timestamps
```

The following example sets the nominal AAL2 voice-band-detection playout-delay buffer to 12 ms:

```
voice service voatm
 session protocol aal2
  vbd-playout-delay nominal 12
```

The following example sets the AAL2 voice-band-detection playout-buffer delay to a maximum of 55 ms:

```
voice service voatm
 session protocol aal2
  vbd-playout-delay maximum 55
```

The following example sets the AAL2 voice-band-detection playout-buffer delay to a minimum of 22 ms:

```
voice service voatm
 session protocol aal2
  vbd-playout-delay minimum 22
```

The following sample output shows the vdb-playout-delay being verified in the running configuration output:

```
Router(conf-voi-serv-sess)# do show run | sec voice service voatm voice service voatm
 !
 session protocol aal2
  vbd-playout-delay minimum 22
```

### Related Commands

Command

Description

voice-service

Specifies the voice encapsulation type and enters voice service configuration mode.

## vbr-rt

To configure the real-time variable bit rate (VBR) for VoATM voice connections, use the vbr-rt command in the appropriate configuration mode. To disable VBR for voice connections, use the no form of this command.

vbr-rt peak-rate average-rate burst

no vbr-rt

### Syntax Description

peak-rate

Peak information rate (PIR) for the voice connection, in kilobytes per second (kbps). If it does not exceed your carrier’s
                                          line rate, set it to the line rate. Range is from 56 to 10000.

average-rate

Average information rate (AIR) for the voice connection, in kbps.

burst

Burst size, in number of cells. Range is from 0 to 65536.

### Command Default

No real-time VBR settings are configured

### Command Modes

ATM Bundle-vc configuration for ATM VC bundle members ATM PVP configuration for an ATM PVP Interface-ATM-VC configuration for an ATM permanent virtual connection (PVC) or switched virtual circuit (SVC) VC-class configuration for a virtual circuit (VC) class

## Command History

Release

Modification

12.0

This command was introduced on the Cisco MC3810.

12.1(5)XM

This command was implemented on Cisco 3600 series routers and modified to support Simple Gateway Control Protocol (SGCP)
                                          and Media Gateway Control Protocol (MGCP).

12.2(2)T

This command was integrated into Cisco IOS Release 12.2(2)T.

12.2(11)T

This command was implemented on the Cisco AS5300 and Cisco AS5850.

Cisco IOS XE Release 2.3

This command was made available in ATM PVP configuration mode.

### Usage Guidelines

This command configures traffic shaping between voice and data PVCs. Traffic shaping is required so that the carrier does
                              not discard calls. To configure voice and data traffic shaping, you must configure the peak, average, and burst options for
                              voice traffic. Configure the burst value if the PVC will carry bursty traffic. Peak, average, and burst values are needed
                              so that the PVC can effectively handle the bandwidth for the number of voice calls.

Calculate the minimum peak, average, and burst values for the number of voice calls as follows:

Peak Value

Peak value = (2 x the maximum number of calls) x 16K = _______________

Average Value

Calculate according to the maximum number of calls that the PVC will carry times the bandwidth per call. The following formulas
                              give you the average rate in kbps:

- G.711 with 40- or 80-byte sample size:

Average value = max calls x 128K = _______________

- G.726 with 40-byte sample size:

Average value = max calls x 85K = _______________

- G.729a with 10-byte sample size:

Average value = max calls x 85K = _______________

- G.711 with 40-byte sample size:

Average value = max calls x 85K = _______________

- G.726 with 40-byte sample size:

Average value = max calls x 43K = _______________

- G.729a with 10-byte sample size:

Average value = max calls x 43K = _______________

If voice activity detection (VAD) is enabled, bandwidth usage is reduced by as much as 12 percent with the maximum number
                              of calls in progress. With fewer calls in progress, bandwidth savings are less.

Burst Value

Set the burst size as large as possible, and never less than the minimum burst size. Guidelines are as follows:

Minimum burst size = 4 x number of voice calls = _______________

Maximum burst size = maximum allowed by the carrier = _______________

When you configure data PVCs that will be traffic shaped with voice PVCs, use AAL5snap encapsulation and calculate the overhead
                              as 1.13 times the voice rate.

## Examples

The following example configures the traffic-shaping rate for ATM PVC 20. Peak, average, and burst rates are calculated based
                              on a maximum of 20 calls on the PVC.

```
pvc 20
 encapsulation aal5mux voice
 vbr-rt 640 320 80
```

### Related Commands

Command

Description

encapsulation aal5

Configures the AAL and encapsulation type for an ATM PVC, SVC, or VC class.

## vcci

To identify a permanent virtual circuit (PVC) to the call agent, use the vcci command in ATM virtual circuit (VC) configuration mode. To restore the default value, use the no form of this command.

vcci pvc-identifier

no vcci

### Syntax Description

pvc-identifier

Identifier for the PVC. Range is from 0 to 32767. There is no default value.

### Command Default

No default behavior or values

### Command Modes

ATM virtual circuit configuration mode

## Command History

Release

Modification

12.1(5)XM

This command was introduced.

12.2(2)T

This command was integrated into Cisco IOS Release 12.2(2)T.

12.2(11)T

This command was implemented on the Cisco AS5300 and Cisco AS5850.

### Usage Guidelines

The pvc-identifier argument is a unique 15-bit value for each PVC. The call agent sets up a call with the gateway by specifying the PVC using the pvc-identifier .

## Examples

The following example shows how to assign a PVC identifier:

```
Router(config-if-atm-vc)# vcci 5278
```

### Related Commands

Command

Description

mgcp

Starts the MGCP daemon.

pvc

Creates an ATM PVC for voice traffic.

## video codec (dial peer)

To assign a video codec to a VoIP dial peer, use the video codec command in dial peer configuration mode. To remove a video codec, use the no form of this command.

video codec { h261 | h263 | h263 | + | h264 | mpeg4 | scip }

no video codec

### Syntax Description

h261

Video Codec H.261

h263

Video Codec H.263

h263+

Video Codec H.263+

h264

Video Codec H.264

mpeg4

Video Codec MPEG-4 ISO/ISE 14496-2

scip

Video Codec SCIP

(This feature is available in 'preview' mode)

### Command Default

No video codec is configured.

### Command Modes

Dial peer configuration (config-dial-peer)

## Command History

Release

Modification

12.4(11)T

This command was introduced.

Cisco IOS XE 17.16.1a

This command was modified to include SCIP video codec type.

This feature is available in 'preview' mode as it includes limited functionality or incomplete software dependencies.

### Usage Guidelines

Use the video codec command to configure a video codec for a VoIP dial peer. If no video codec is configured, the default is transparent codec
                              operation between the endpoints.

## Examples

The following example shows configuration for video codec H.263+ on VoIP dial peer 30:

```
dial-peer voice 30 voip
 video codec h263+
```

## Examples

The following example shows configuration for video codec SCIP on VoIP dial peer 30:

```
dial-peer voice 30 voip
 video codec scip
```

### Related Commands

Command

Description

video codec (voice-class)

Specifies a video codec for a voice class.

## video codec (voice class)

To specify a video codec for a voice class, use the video codec command in voice class configuration mode. To remove the video codec, use the no form of this command.

video codec { h261 | h263 | h263 + | h264 | mpeg4 | scip }

no video codec { h261 | h263 | h263 + | h264 | mpeg4 | scip }

### Syntax Description

h261

Apply this preference to video codec H.261

h263

Apply this preference to video codec H.263

h263+

Apply this preference to video codec H.263+

h264

Apply this preference to video codec H.264

mpeg4

Video Codec MPEG-4 ISO/IES 14496-2

scip

Video Codec SCIP

(This feature is available in 'preview' mode)

### Command Default

No video codec is configured.

### Command Modes

voice class configuration (config-class)

## Command History

Release

Modification

12.4(11)T

This command was introduced.

Cisco IOS XE Dublin
                                                17.10.1a

Introduced support for YANG models.

Cisco IOS XE 17.16.1a

This command was modified to support SCIP video codec type.

This feature is available in 'preview' mode as it includes limited functionality or incomplete software dependencies.

### Usage Guidelines

Use the video codec command to specify one or more video codecs for a voice class.

## Examples

The following example shows configuration of two audio codec preferences and three video codec preferences for voice class
                              codec 10:

```
voice class codec 10
 codec preference 1 g711alaw
 codec preference 2 g722
 video codec h261
 video codec h263
 video codec h264
 video codec mpeg4
```

## Examples

The following example shows configuration of SCIP video codec for voice class codec 1:

```
voice class codec 1
 video codec scip
```

### Related Commands

Command

Description

video codec (dial peer)

Specifies a video codec for a VoIP dial peer.

## video screening

To enable
                              		  transcoding and transsizing between two call legs when configuring SIP, use the video screening command in voice service SIP
                              		  configuration mode or voice class tenant configuration mode. To disable
                              		  transcoding and transsizing, use no form of this
                              		  command.

video screening system

no video screening system

### Syntax Description

system

Specifies
                                          						that transcoding and transsizing use the global sip-ua value. This keyword is
                                          						available only for the tenant mode to allow it to fallback to the global
                                          						configurations.

### Command Default

Video screening is
                              		  disabled.

### Command Modes

Voice service SIP configuration.

Voice class tenant configuration (config-class)

## Command History

Release

Modification

15.1(4)M

The
                                          						command was introduced.

15.6(2)T
                                          						and IOS XE Denali 16.3.1

This
                                          						command was modified to include the keyword: system . This
                                          						command is now available under voice class tenants.

### Usage Guidelines

Use this command to
                              		  enable conversion of video streams if there is a mismatch between two call
                              		  legs.

## Examples

The following
                              		  example enters the voice-card configuration mode and enables video screening:

```
Router(config)# voice service voip Router(config-voicecard)# sip Router((conf-serv-sip)# video screening
```

The following
                              		  example enters the voice-card configuration mode and enables video screening in
                              		  voice class tenant configuration mode:

```
Router(conf-class)# video screening system
```

### Related Commands

Command

Description

codec profile

Defines
                                          						the video capabilities needed for video endpoints.

video codec

Assigns a
                                          						video codec to a VoIP dial peer.

## violation

To specify the action that needs to be performed on any violation in the Differentiated Services Code Point (DSCP) policy,
                              use the violation command in voice class configuration mode. To disable the configuration, use the no form of this command.

violation number action { disconnect | ignore } [ no-syslog ]

no violation number action { disconnect | ignore } [ no-syslog ]

### Syntax Description

number

Number of violations after which the required action needs to be taken. The range is from 1 to 200000. The default value
                                          is 20.

action

Specifies that an action must be performed after the specified number of violations.

disconnect

Disconnects the call after the specified number of violations is exceeded.

ignore

Specifies that no action should be taken after the specified number of violations is exceeded.

no-syslog

(Optional) Specifies not to print messages to the system log when violations occur.

### Command Default

No actions are specified against any violation.

### Command Modes

Voice class configuration (config-class)

## Command History

Release

Modification

15.2(2)T

This command was introduced.

### Usage Guidelines

You can use the violation command to specify the action that needs to be performed on any violation in the DSCP policy. A system log is created by
                              default. You can configure the no-syslog keyword to disable the Cisco Unified Border Element (Cisco UBE) from generating system logs on DSCP policy violation.

Configure a high value for DSCP violations. If you configure a low value such as 5, action will be performed on the call after
                              every five violations and system logs will be generated frequently.

The “100 - Invalid information element contents [Q.850]” message is displayed in the system log when a call is disconnected
                              because of a DSCP policy violation. The cause for disconnecting the call is propagated only to the call leg causing the violation.
                              For example, if the outgoing call leg of a Session Initiation Protocol (SIP)-to-SIP call violates the DSCP policy and the
                              number of violations exceeds the configured number, this call is disconnected with the cause of 100 (Invalid information element
                              contents [Q.850]) to the outgoing call leg and cause 16 (Normal Call Cleaning) to the incoming call leg.

## Examples

The following example shows how to configure a router to print to the system log and disconnect the call if a call exceeds
                              20,000 violations:

```
Router> enable Router# configure terminal Router(config)# voice class dscp-profile 1 Router(config-class)# violation 20000 action disconnect
```

### Related Commands

Command

Description

dscp media

Specifies the RPH to DSCP mapping.

voice class dscp-profile

Configures the DSCP profile.

## violation (media profile)

To specify the action that needs to be performed on any violation in the media bandwidth policy, use the violation command in media profile configuration mode. To disable the configuration, use the no form of this command.

violation number action { disconnect | drop | ignore } [ no-syslog ]

no violation number action { disconnect | drop | ignore } [ no-syslog ]

### Syntax Description

number

Number of violations after which the required action needs to be taken. The range is from 1 to 200000. The default value
                                          is 20.

action

Specifies that an action must be performed after the specified number of violations.

disconnect

Disconnects the call after the specified number of violations is exceeded.

drop

Drops the call after the specified number of violations is exceeded.

ignore

Specifies that no action should be taken after the specified number of violations is exceeded.

no-syslog

(Optional) Specifies not to print messages to the system log when violations occur.

### Command Default

No actions are specified against any violation.

### Command Modes

Media profile configuration (cfg-mediaprofile)

## Command History

Release

Modification

15.2(2)T

This command was introduced.

### Usage Guidelines

You can use the violation command to specify the action that needs to be performed on any violation in the media bandwidth policy. A system log is
                              created by default. You can configure the no-syslog keyword to disable the Cisco Unified Border Element (Cisco UBE) from generating system logs on DSCP policy violation.

Configure a high value for DSCP violations. If you configure a low value such as 5, action will be performed on the call after
                              every five violations and system logs will be generated frequently.

## Examples

The following example shows how to configure a router to print the system log and disconnect the call if a call exceeds 20,000
                              violations:

```
Router> enable Router# configure terminal Router(config)# media profile police 1 Router(cfg-mediaprofile)# violation 20000 action drop
```

### Related Commands

Command

Description

media profile police

Configures the media policing profile.

overhead

Configures the overhead bandwidth percentage above the negotiated bandwidth.

## vmwi

To enable DC voltage or FSK visual message-waiting indictator (VMWI) on a Cisco VG224 onboard analog FXS voice port, use the vmwi command in voice-port configuration mode. To reset VMWI to default, use the no form of this command.

vmwi { dc-voltage | fsk }

no vmwi

### Syntax Description

dc-voltage

DC voltage VMWI is enabled on this FXS port.

fsk

FSK VMWI is enabled on this FXS port. Default.

### Command Default

FSK VMWI is enabled.

### Command Modes

Voice-port configuration (config-voiceport)

## Command History

Release

Modification

12.4(20)YA

This command was introduced.

12.4(22)T

This command was integrated into Cisco IOS Release 12.4(22)T.

### Usage Guidelines

This command with the dc-voltage keyword enables the message-waiting lamp to flash on an analog phone that requires DC voltage to activate a visual indicator.

This command with the fsk keyword enables the message-waiting lamp to flash on an analog phone that requires an FSK message to activate a visual indicator.

DC Voltage VMWI is supported for the SCCP telephony control (STC) application only. For all other applications, such as MGCP,
                              FSK will be used even if you configure the vmwi dc-voltage command on the voice gateway.

## Examples

The example shows how to enable DC Voltage VMWI on port 2/0 on a Cisco VG224.

```
Router(config)# voice-port 2/0 Router(config-voiceport)# vmwi dc-voltage Router(config-voiceport)# end
```

### Related Commands

Command

Description

stcapp

Enables basic SCCP call-control features for FXS analog ports on Cisco IOS voice gateways

## vofr

To enable Voice over Frame Relay (VoFR) on a specific data-link connection identifier (DLCI) and to configure specific subchannels
                              on that DLCI, use the vofr command in frame relay DLCI configuration mode. To disable VoFR on a specific DLCI, use the no form of this command.

### Switched Calls

vofr [ data cid ] [ call-control [cid] ]

no vofr [ data cid ] [ call-control [cid] ]

### Switched Calls to Cisco MC3810 Multiservice Concentrators Running Cisco IOS Releases Release Before 12.0(7)XK and Release
                              12.1(2)T

vofr [ cisco ]

no vofr [ cisco ]

### Cisco-Trunk Permanent Calls

vofr data cid call-control cid

no vofr data cid call-control cid

### FRF.11 Trunk Calls

vofr [ data cid ] [ call-control cid ]

no vofr [ data cid ] [ call-control cid ]

### Syntax Description

data

(Required for Cisco-trunk permanent calls. Optional for switched calls.) Selects a subchannel (CID) for data other than the
                                          default subchannel, which is 4.

cid

(Optional) Specifies the subchannel to be used for data. Range is from 4 to 255. The default is 4. If data is specified, enter a valid CID.

call-control

(Optional) Reserves a subchannel for call-control signaling.

cisco

(Optional) Cisco proprietary voice encapsulation for VoFR with data is carried on CID 4 and call-control on CID 5.

cid

(Optional) Specifies the subchannel to be used for call-control signaling. Valid range is from 4 to 255. The default is 5.
                                          If call-control is specified and a CID is not entered, the default CID is used.

### Command Default

Disabled

### Command Modes

Frame relay DLCI configuration

## Command History

Release

Modification

12.0(3)XG

This command was introduced on Cisco 2600 series, Cisco 3600 series, and Cisco 7200 series routers and Cisco MC3810.

12.0(4)T

This command was integrated into Cisco IOS Release 12.0(4)T.

12.0(7)XK

The use of the cisco option was modified. Beginning in this release, use the cisco option only when configuring connections to Cisco MC3810 running Cisco IOS Releases before 12.0(7)XK and 12.1(2)T.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T.

### Usage Guidelines

The table below lists the different options of the vofr command and which combination of options is used beginning in Cisco IOS Release 12.0(7)XK and Release 12.1(2)T.

Type of Call

Command Combination to Use

Switched call (user dialed or auto-ringdown) to other routers supporting VoFR

vofr [ data cid ] [ call-control [ cid ]] 1

Cisco-trunk permanent call (private-line) to other routers supporting VoFR

vofr data cid call-control cid

FRF.11 trunk call (private-line) to other routers supporting VoFR

vofr [ data cid ] [ call-control cid ] 2

## Examples

The following example, beginning in global configuration mode, shows how to enable VoFR on serial interface 1/1, DLCI 100.
                              The example configures CID 4 for data; no call-control CID is defined.

```
interface serial 1/1
 frame-relay interface-dlci 100
 vofr
```

To configure CID 4 for data and CID 5 for call-control (both defaults), enter the following command:

```
vofr call-control
```

To configure CID 10 for data and CID 15 for call-control, enter the following command:

```
vofr data 10 call-control 15
```

To configure CID 4 for data and CID 15 for call-control, enter the following command:

```
vofr call-control 15
```

To configure CID 10 for data and CID 5 for call-control, enter the following command:

```
vofr data 10 call-control
```

To configure CID 10 for data with no call-control, enter the following command:

```
vofr data 10
```

### Related Commands

Command

Description

class

Assigns a VC class to a PVC.

frame-relay interface-dlci

Assigns a DLCI to a specified Frame Relay subinterface.

## voice

To enable voice resource pool services for resource pool management, use the voice command in service profile configuration mode. To disable voice services, use the no form of this command.

voice

no voice

### Syntax Description

This command has no arguments or keywords.

### Command Default

Disabled

### Command Modes

Service profile configuration mode

## Command History

Release

Modification

12.2(2)XA

This command was introduced on the Cisco AS5350 and AS5400.

12.2(2)XB1

This command was implemented on the Cisco AS5850 platform.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T.

## Examples

The following example shows that voice service is available and enables voice resource pool service using the voice command in service profile configuration mode:

```
Router(config)# resource-pool profile service voip Router(config-service-profile)# ? Service Profile Configuration Commands:
  default   Set a command to its defaults
  exit      Exit from resource-manager configuration mode
  help      Description of the interactive help system
  modem     Configure modem service parameters
  no        Negate a command or set in its defaults
  voice     Configure voice service parameters
Router(config-service-profile)# voice
```

### Related Commands

Command

Description

resource-pool enable

Enables resource pool management.

resource-pool profile service voip

Defines the VoIP service profile for resource pool management.

## voicecap configure

To apply a voicecap on NextPort platforms, use the voicecap configure command in voice-port configuration mode. To remove a voicecap, use the no form of this command.

voicecap configure name

no voicecap configure name

### Syntax Description

name

Designates which voicecaps to use on this voice port.

### Command Default

No default values or behavior

### Command Modes

Voice-port configuration

## Command History

Release

Modification

12.3(4)T

This command was introduced.

### Usage Guidelines

The character value for the name argument must be identical to the value entered when you created the voicecap using the voicecap entry command.

## Examples

The following example configures a voicecap with the name qualityERL:

```
Router> enable Router# configure terminal Router(config)# voicecap entry qualityERL v270=120 Router(config)# voice-port 3/0:D Router(config-voiceport)# voicecap configure qualityERL
```

### Related Commands

Command

Description

voicecap entry

Creates a voicecap on NextPort platforms.

## voicecap entry

To create a voicecap, use the voicecap entry command in global configuration mode. To disable a voicecap, use the no form of this command.

voicecap entry [ name string ]

no voicecap entry [ name string ]

### Syntax Description

name string

(Optional) A word and a string of characters that uniquely identify a voicecap.

The name argument specifies a unique identifier for a voicecap.

The string argument specifies one or more voicecap register entries, similar to a modemcap. Each entry is of the form v index = value , where index refers to a specific V register, and value designates the value for that V register.

### Command Default

No voice caps can be applied to configure firmware.

### Command Modes

Global configuration

## Command History

Release

Modification

12.3(4)T

This command was introduced.

12.3(11)T

This command was integrated into Cisco IOS Release 12.3(11)T.

12.4(4)XC

This command was modified to include GSMAMR-NB codec capability.

12.4(9)T

This command was integrated into Cisco IOS Release 12.4(9)T.

### Usage Guidelines

This command configures firmware through voicecap strings. This command allows you to assign values to specific registers.
                              Voicecaps are applied to specific voice ports at system startup.

The voicecap values can be entered in a DSP-recognizable format called raw format . They can also be entered in standard format , which allows you to use commonly accessible values, such as decibels.

Starting with Cisco IOS Release 12.4(4)XC, this command can be used to configure GSMAMR-NB codecs on Cisco AS5350XM and Cisco
                              AS5400XM platforms. The register values for GSMAMR-NB are shown in the table below.

V-Reg #

Default

Description

Register Values and Additional Notes

0

0

Sets how Adaptive Multi-Rate (AMR) responds to an incoming codec mode request (CMR) that is not a member of the mode set.

0 = Drop the packet with the bad CMR. 1 = Ignore the CMR (do not change rates) but process the rest of the packet data normally.
                                          2 = Change the rate to the highest rate in the mode set lower than the rate requested by the CMR.

1

0

Sets how AMR handles packets with a frame type (AMR rate) that is not a member of the mode set.

0 = Drop the packet with the bad frame-type. 1 = Attempt to decode the packet.

## Examples

The following example creates a voicecap string for a GSMAMR-NB codec named gsmamrnb-ctrl with V register 0 set to 1:

```
Router> enable Router# configure terminal Router(config)# voicecap entry gsmamrnb-ctrl v0=1
```

### Related Commands

Command

Description

voicecap configure

Applies a voicecap to the specified voice ports.

## voice call capacity mir

To set the value for the minimum interval between reporting (MIR), use the voice call capacity mir command in global configuration
                              mode. To turn off these attributes, use the no form of this command.

voice call { carrier | trunk-group | prefix } capacity mir seconds

no voice call { carrier | trunk-group | prefix } capacity mir

### Syntax Description

carrier

Carrier code address family

trunk-group

Trunk group address family

prefix

E.164 prefix

value

Minimum interval, in seconds, with a range of 1 to 3600 seconds and a default of 10. This value cannot be set higher than
                                          the time configured for the capacity update interval.

### Command Default

10 seconds.

### Command Modes

Global configuration

## Command History

Release

Modification

12.3(1)

This command was introduced.

### Usage Guidelines

Because the available circuit (AC) attribute of a destination is very dynamic, reporting of this attribute should be handled
                              carefully. AC should be reported as frequently as possible so that the location server has better information about the resources.
                              However, the location server should not be overwhelmed with too many updates.

All of the AC reporting, called the interesting point of AC, is performed when the specified event happens within the minimum
                              interval between reporting (MIR) time since last reporting. This command sets the amount of time used for the interval to
                              control the number of interesting points that are reported so not to overwhelm the location server with too many AC updates.

The seconds argument cannot be set higher than the time configured for the capacity update interval.

## Examples

The following example shows the minimum interval between reporting for the carrier address family set to 25 seconds:

```
Router(config)# voice call carrier capacity mir 25
```

### Related Commands

Command

Description

capacity update interval (dial peer)

Changes the capacity update for prefixes associated with a dial peer.

capacity update interval (trunk group)

Change the capacity update for carriers or trunk groups.

voice call capacity stw

Set the value for STW.

## voice call capacity reporting

To turn on the reporting of maxima (first derivative) or inflection
                              		  (second derivative) points in available capacity, use the voice call capacity
                              		  reporting command in global configuration mode. To turn off the reporting, use
                              		  the no form of this command.

voice call { carrier | trunk-group | prefix } capacity reporting { maxima | inflection }

no voice call { carrier | trunk-group | prefix } capacity reporting { maxima | inflection }

### Syntax Description

carrier

Carrier code address family.

trunk-group

Trunk group address family.

prefix

E.164 prefix.

maxima

Maxima (first derivative) point in available capacity.

inflection

Inflection (second derivative) point in available capacity.

### Command Default

The capacity reporting function is turned off.

### Command Modes

Global configuration.

## Command History

Release

Modification

12.3(1)

This command was introduced.

### Usage Guidelines

The smoothed curve of the available circuits (AC) has maxima, minima,
                              		  and inflection points. When the curve has reached these points, this represents
                              		  a change in the call rate.

Maximum, minimum and inflection points are illustrated in the figure
                              		  below.

## Examples

The following example shows the reporting of the available capacity
                              		  inflection point on the trunk group is turned on:

```
Router(config)# voice call trunk-group capacity reporting inflection
```

### Related Commands

Command

Description

voice call capacity mir

Sets the values for the minimum interval between reporting
                                          						(MIR) and smoothing transition time for weight (STW).

voice call capacity timer interval

Sets the periodic interval for reporting capacity from
                                          						carrier, trunk group, or prefix databases

voice call trigger hwm

Sets the value for percentage change, low water mark and
                                          						high water mark in the available capacity in the trunk group or prefix
                                          						databases.

## voice call capacity stw

To set the value for smoothing transition time for weight (STW), use the voice call capacity stw command in global configuration
                              mode. To turn off these attributes, use the no form of this command.

voice call { carrier | trunk-group | prefix } capacity stw seconds

no voice call { carrier | trunk-group | prefix } capacity stw

### Syntax Description

carrier

Carrier code address family

trunk-group

Trunk group address family

prefix

E.164 prefix

seconds

Transitions time can be from 0 to 60 seconds with a default of 10.

### Command Default

10 seconds.

### Command Modes

Global configuration.

## Command History

Release

Modification

12.3(1)

This command was introduced.

### Usage Guidelines

Because the available circuit (AC) attribute of a destination is very dynamic, reporting of this attribute should be handled
                              carefully. AC should be reported as frequently as possible so that the location server has better information about the resources.
                              However, the location server should not be overwhelmed with too many updates.

A smoothing algorithm is applied to the quantity of AC being reported. This algorithm eliminates reporting of noise. The degree
                              of smoothing can be configured with the voice call capacity stw command. This command sets the smoothing transition time for
                              weight, which is the time it takes for current smoothed value of AC to come half way between the current smoothed value and
                              the current instantaneous value of AC. Lower stw values speed the smoothed value of AC as it approaches the instantaneous
                              value of AC. When stw is set to 0, the smoothed value is always equal to the instantaneous value of AC.

## Examples

The following example shows the smoothing time for weight for the carrier address family set to 25 seconds:

```
Router(config)# voice call carrier capacity stw 25
```

### Related Commands

Command

Description

capacity update interval (dial peer)

Changes the capacity update for prefixes associated with a dial peer.

capacity update interval (trunk group)

Change the capacity update for carriers or trunk groups.

voice call capacity mir

Set the value for MIR.

## voice call capacity timer interval

To set the periodic interval for reporting capacity from carrier, trunk group, or prefix databases, use the voice call capacity
                              timer interval command in global configuration mode. To turn off the interval, use the no form of this command.

voice call { carrier | trunk-group | prefix } capacity timer interval seconds

no voice call { carrier | trunk-group | prefix } capacity timer interval seconds

### Syntax Description

carrier

Carrier code address family

trunk-group

Trunk group address family

prefix

E.164 prefix

seconds

Value from 10 to 3600 seconds.

### Command Default

25 seconds

### Command Modes

Global configuration

## Command History

Release

Modification

12.3(1)

This command was introduced.

### Usage Guidelines

For the reporting interval, a periodic timer called the capacity update timer handles updates of available circuit (AC) information
                              and can be configured using the voice call capacity timer interval command. For example, if AC has changed since the last
                              reporting, the AC is again reported when the capacity update timer expires.

## Examples

The following example sets the timer interval for the prefixes set at 15 seconds:

```
Router(config)# voice call prefix capacity timer interval 15
```

### Related Commands

Command

Description

voice call capacity mir

Sets the values for the MIR and STW.

voice call capacity reporting

Turns on the reporting of maxima (first derivative) or inflection (second derivative) points in available capacity.

voice call trigger hwm

Sets the value for percentage change, low water mark and high water mark in the available capacity in the trunk group or prefix
                                          databases.

## voice call convert-discpi-to-prog

To convert a disconnect message with a progress indicator (PI) to a progress message, use the voice call convert-discpi-to-prog
                              command in global configuration mode. To return to the default condition, use the no form of this command.

voice call convert-discpi-to-prog [ tunnel-IEs | always [ tunnel-IEs ]]

no voice call convert-discpi-to-prog

### Syntax Description

tunnel-IEs

(Optional) Information elements (IEs) are carried in the progress message.

always

(Optional) Converts disconnect message with a PI to a progress message in both preconnected and connected states.

### Command Default

A disconnect message with a PI is not converted to a progress message.

### Command Modes

Global configuration

## Command History

Release

Modification

12.2(1)

This command was introduced.

12.3(6)

The tunnel-1Es keyword was added.

12.3(4)XQ

The always keyword with the tunnel-IEs keyword were added.

12.3(8)T

The always keyword with the tunnel-IEs keyword were added.

12.3(9)

The always keyword with the tunnel-1Es keyword were added.

### Usage Guidelines

The voice call convert-discpi-to-prog command turns an ISDN disconnect message into a progress message. If you use the tunnel-IEs keyword, the information elements are not dropped when the disconnect message is converted to a progress message.

## Examples

The following example changes a disconnect with PI to a progress message containing information elements (IEs):

```
voice call convert-discpi-to-prog tunnel-IEs
```

The following example changes a disconnect with PI to a progress message in the preconnected and connected states:

```
voice call convert-discpi-to-prog always
```

### Related Commands

Command

Description

disc_pi_off

Enables an H.323 gateway to disconnect a call when it receives a disconnect message with a PI.

## voice call csr data-points

To set the number of call success rate (CSR) data points, use the voice call csr data-points command in global configuration
                              mode. To disable the setting of the CSR data points, use the no form of this command.

voice call { carrier | trunk-group | prefix } csr data-points value

no voice call { carrier | trunk-group | prefix } csr data-points value

### Syntax Description

carrier

Carrier code address family

trunk-group

Trunk group address family

prefix

E.164 prefix

value

Value from 10 to 50 data points. Default is 30 data points.

### Command Default

30 data points

### Command Modes

Global configuration

## Command History

Release

Modification

12.3(1)

This command was introduced.

## Examples

The following example sets the CSR data points for trunk groups at 10:

```
Router(config)# voice call trunk-group csr data-points 10
```

### Related Commands

Command

Description

voice call csr recording interval

Sets the recording interval for the CSR.

voice call csr reporting interval

Sets the reporting interval for the CSR.

## voice call csr recording interval

To set the recording interval for call success rates (CSR), use the voice call csr recording interval command in global configuration
                              mode. To disable the CSR recording interval, use the no form of this command.

voice call { carrier | trunk-group | prefix } csr recording interval minutes

no voice call { carrier | trunk-group | prefix } csr recording interval minutes

### Syntax Description

carrier

Carrier code address family.

trunk-group

Trunk group address family.

prefix

E.164 prefix.

minutes

Value from 10 to 1000 minutes with a default of 60.

### Command Default

60 minutes

### Command Modes

Global configuration

## Command History

Release

Modification

12.3(1)

This command was introduced.

## Examples

The following example sets the CSR recording interval for prefixes at 30 minutes:

```
Router(config)# voice call carrier csr recording interval 30
```

### Related Commands

Command

Description

voice call csr data-points

Sets the number of call success rate (CSR) data points.

voice call csr reporting interval

Sets the reporting interval for CSR.

## voice call csr reporting interval

To set the reporting interval for call success rate (CSR), use the voice call csr reporting interval command in global configuration
                              mode. To disable the CSR recording interval, use the no form of this command.

voice call { carrier | trunk-group | prefix } csr reporting interval seconds

no voice call { carrier | trunk-group | prefix } csr reporting interval seconds

### Syntax Description

carrier

Carrier code address family.

trunk-group

Trunk group address family.

prefix

E.164 prefix.

seconds

Value from 10 to 10000 seconds with a default of 25.

### Command Default

25 seconds

### Command Modes

Global configuration

## Command History

Release

Modification

12.3(1)

This command was introduced.

## Examples

The following example sets the CSR reporting interval for trunk groups at 40 seconds:

```
Router(config)# voice call carrier csr reporting interval 40
```

### Related Commands

Command

Description

voice call csr data-points

Sets the number of CSR data points.

voice call csr recording interval

Sets the recording interval for CSR.

## voice call debug

To debug a voice call, use the voice call debug command in global configuration mode. To disable the short-header setting and return tothe full-guid setting, use the no form of this command.

{ voice call debug full-guid | short-header }

{ no voice call debug full-guid | short-header }

### Syntax Description

full-guid

Displays the GUID in a 16-byte header.

When the no version of this command is input with the full-guid keyword, the short 6-byte version displays. This is the default.

short-header

Displays the CallEntry ID in the header without displaying the GUID or module-specific parameters.

### Command Default

The short 6-byte header displays.

### Command Modes

Global configuration

## Command History

Release

Modification

12.2(11)T

The new debug header was added to the following platforms: Cisco 2600 series, Cisco 3620, Cisco 3640, Cisco 3660 series,
                                          Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5800, Cisco AS5850, and Cisco MC3810.

12.2(15)T

The header-only keyword was replaced by the short-header keyword.

### Usage Guidelines

Despite its nontraditional syntax (trailing rather than preceding "debug"), this is a normal debug command.

You can control the contents of the standardized header. Display options for the header are as follows:

Short 6-byte GUID

Full 16-byte GUID

Short header which contains only the CallEntry ID

The format of the GUID headers is as follows: //CallEntryID/GUID/Module-Dependent-List/Function-name:.

The format of the short header is as follows: //CallEntryID/Function-name:.

When the voice call debug short-header command is entered, the header displays with no GUID or module-specific parameters.
                              When the no voice call debug short-header command is entered, the header, the 6-byte GUID, and module-dependent parameter
                              output displays. The default option is displaying the 6-byte GUID trace.

Using the no form of this command does not turn off debugging.

## Examples

The following is sample output when the full-guid keyword is specified:

```
Router# voice call debug full-guid
!
00:05:12: //1/0E2C8A90-BC00-11D5-8002-DACCFDCEF87D/VTSP:(0:D):0:0:4385/vtsp_insert_cdb: 00:05:12: //-1/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/CCAPI/cc_incr_if_call_volume: 00:05:12: //1/0E2C8A90-BC00-11D5-8002-DACCFDCEF87D/VTSP:(0:D):0:0:4385/vtsp_open_voice_and_set_params:
00:05:12: //1/0E2C8A90-BC00-11D5-8002-DACCFDCEF87D/VTSP:(0:D):0:0:4385/vtsp_modem_proto_from_cdb:
00:05:12: //1/0E2C8A90-BC00-11D5-8002-DACCFDCEF87D/VTSP:(0:D):0:0:4385/set_playout_cdb: 00:05:12: //1/0E2C8A90-BC00-11D5-8002-DACCFDCEF87D/VTSP:(0:D):0:0:4385/vtsp_dsp_echo_canceller_control:
```

The "//-1/" output indicates that CallEntryID for the CCAPI module is not available.

The table below describes significant fields shown in the display.

Field

Description

VTSP:(0:D):0:0:4385

VTSP module, port name, channel number, DSP slot, and DSP channel number.

vtsp_insert_cdb

Function name.

CCAPI

CCAPI module.

The following is sample output when the short-header keyword is specified:

```
Router(config)# voice call debug short-header
!
00:05:12: //1/vtsp_insert_cdb: 
00:05:12: //-1/cc_incr_if_call_volume: 
00:05:12: //1/vtsp_open_voice_and_set_params:
00:05:12: //1/vtsp_modem_proto_from_cdb:
00:05:12: //1/set_playout_cdb: 
00:05:12: //1/vtsp_dsp_echo_canceller_control:
```

The "//-1/" output indicates that CallEntryID for CCAPI is not available.

### Related Commands

Command

Description

debug rtsp api

Displays debug output for the RTSP client API.

debug rtsp client session

Displays debug output for the RTSP client data.

debug rtsp error

Displays error message for RTSP data.

debug rtsp pmh

Displays debug messages for the PMH.

debug rtsp socket

Displays debug output for the RTSP client socket data.

debug voip ccapi error

Traces error logs in the CCAPI.

debug voip ccapi inout

Traces the execution path through the CCAPI.

debug voip ivr all

Displays all IVR messages.

debug voip ivr applib

Displays IVR API libraries being processed.

debug voip ivr callsetup

Displays IVR call setup being processed.

debug voip ivr digitcollect

Displays IVR digits collected during the call.

debug voip ivr dynamic

Displays IVR dynamic prompt play debug.

debug voip ivr error

Displays IVR errors.

debug voip ivr script

Displays IVR script debug.

debug voip ivr settlement

Displays IVR settlement activities.

debug voip ivr states

Displays IVR states.

debug voip ivr tclcommands

Displays the TCL commands used in the script.

debug voip rawmsg

Displays the raw VoIP message.

debug vtsp all

Enables debug vtsp session , debug vtsp error , and debug vtsp dsp .

debug vtsp dsp

Displays messages from the DSP.

debug vtsp error

Displays processing errors in the VTSP.

debug vtsp event

Displays the state of the gateway and the call events.

debug vtsp port

Limits VTSP debug output to a specific voice port.

debug vtsp rtp

Displays the voice telephony RTP packet debugging.

debug vtsp send-nse

Triggers the VTSP software module to send a triple redundant NSE.

debug vtsp session

Traces how the router interacts with the DSP.

debug vtsp stats

Debugs periodic statistical information sent and received from the DSP

debug vtsp vofr subframe

Displays the first 10 bytes of selected VoFR subframes for the interface.

debug vtsp tone

Displays the types of tones generated by the VoIP gateway.

## voice call disc-pi-off

To enable the gateway to treat a disconnect message with progress indicator (PI) like a standard disconnect without a PI,
                              use the voice call disc-pi-off command in global configuration mode. To reset to the default, use the no form of this command.

voice call disc-pi-off

no voice call disc-pi-off

### Syntax Description

This command has no keywords or arguments.

### Command Default

Gateway disconnects incoming call leg when it receives a disconnect message with PI.

### Command Modes

Global configuration

## Command History

Release

Modification

12.3(5)

This command was introduced.

12.3(7)T

This command was integrated into Cisco IOS Release 12.3(7)T.

### Usage Guidelines

Use this command if the gateway is connected to a switch that sends a release immediately after it receives a Disconnect with
                              PI. To properly handle the call, the switch should open a backward voice path and keep the call active. Otherwise the rotary
                              dial peer feature does not work because the incoming call leg is disconnected. Using this command enables the gateway to handle
                              a disconnect with PI like a regular disconnect message so that you can use the rotary dial peer feature.

## Examples

The following example enables the gateway to properly handle a disconnect with PI:

```
voice call disc-pi-off
```

### Related Commands

Command

Description

disc_pi_off

Enables an H.323 gateway to disconnect a call when it receives a disconnect message with a PI.

voice call convert-discpi-to-prog

Converts a disconnect message with a PI to a progress message.

## voice call rate monitor

To enable voice call rate monitoring, use the voice call rate monitor command in voice service configuration mode. To disable voice call monitoring, use the no form of this command.

voice call rate monitor

no voice call rate monitor

### Syntax Description

This command has no arguments or keywords.

### Command Default

Voice call monitoring is disabled.

### Command Modes

Voice service configuration (conf-voi-serv)

## Command History

Release

Modification

15.2(2)T

This command was introduced.

### Usage Guidelines

You can use the voice call rate monitor command to enable the call monitoring functionality for a duration of 60 seconds.

## Examples

The following example shows how to enable voice call rate monitoring on a Cisco Unified Border Element (Cisco UBE):

```
Router# configure terminal Router(config)# voice service voip Router(conf-voi-serv)# voice call rate monitor
```

### Related Commands

Command

Description

show voice call rate

Displays the voice call rate information.

## voice call send-alert

To enable the terminating gateway to send an alert message instead of a progress message after it receives a call setup message,
                              use the voice call send-alert command in global configuration mode. To reset to the default, use the no form of this command.

voice call send-alert

no voice call send-alert

### Syntax Description

This command has no arguments or keywords.

### Command Default

The terminating gateway sends a progress message after it receives a call Setup message.

### Command Modes

Global configuration

## Command History

Release

Modification

12.1(3)XI4

This command was introduced.

12.1(5)T

This command was not supported in this release.

12.1(5.3)T

This command was integrated into Cisco IOS Release 12.1(5.3)T.

12.2(1)

This command was integrated into Cisco IOS Release 12.2.

### Usage Guidelines

In Cisco IOS Release 12.1(3)XI and later, the terminating gateway sends a Progress message with a progress indicator (PI)
                              after it receives a Setup message. Previously, the gateway responded with an Alert message after receiving a call. In some
                              cases, if the terminating switch does not forward the progress message to the originating gateway, the originating gateway
                              does not cut-through the voice path until a Connect is received and the caller does not hear a ringback tone. In these cases,
                              you can use the voice call send-alert command to make the gateway backward compatible with releases earlier than Cisco IOS Release 12.1(3)XI. If you configure the voice call send-alert command, the terminating gateway sends an Alert message after it receives a Setup message from the originating gateway.

To complete calls from a PRI to an FXS interface, configure the voice call send-alert command on the FXS device.

## Examples

The following example configures the gateway to send an Alert message:

```
voice call send-alert
```

### Related Commands

Command

Description

progress_ind

Sets a specific PI in call Setup, Progress, or Connect messages from an H.323 VoIP gateway.

## voice call trap deviation

To configure the percentage deviation for voice call trap parameters, use the voice call trap deviation command in global configuration mode. To disable the configured percentage deviation, use the no form of this command.

voice call trap deviation percent [ vad ]

no voice call trap deviation percent [ vad ]

### Syntax Description

percent

The percentage deviation for trapping calls. The range of acceptable values is 1 to 100. The default is 49.

vad

(Optional) Specifies the deviation for calls with voice activity detection (VAD) turned on.

### Command Default

This command is enabled by default, and the deviation for trapping calls is set to 49 percent.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

12.4(12)

This command was introduced in a release earlier than Cisco IOS Release 12.4(12).

15.0(1)M

The no form of this command was modified.

### Usage Guidelines

Prior to Release 15.0(1)M, if a non-default percent value was configured, it could be disabled by entering the no voice call trap deviation percent command, even if the percent value was not the configured value. For example, if the voice call trap deviation 30 command was configured, the no voice call trap deviation 40 command disabled the initial command.

Beginning in Release 15.0(1)M, the percent value in the no form of the command must match the configured non-default value. For example, if the voice call trap deviation 30 command is configured, the only way to disable it is to enter the no voice call trap deviation 30 command. If the no voice call trap deviation 40 command is entered, the command-line interface displays this message: "Please enter correct deviation."

## Examples

The following example shows how to set the deviation value for trapping calls to 30 percent:

```
Router(config)# voice call trap deviation 30 vad
```

## voice call trigger hwm

To set the value for high water mark in the available capacity in the trunk group or prefix databases, use the voice call
                              trigger hwm command in global configuration mode. To disable the trigger point, use the no form of this command.

voice call { carrier | trunk-group | prefix } trigger hwm percent

no voice call { carrier | trunk-group | prefix } trigger hwm percent

### Syntax Description

carrier

Carrier code address family

trunk-group

Trunk group address family

prefix

E.164 prefix

percent

Value can be 50 to 100 percent with a default of 80. If set to 100, this trigger will be turned off.

### Command Default

80 percent

### Command Modes

Global configuration

## Command History

Release

Modification

12.3(1)

This command was introduced.

### Usage Guidelines

Available circuits are reported when the value of AC goes above a threshold, called the high water mark. This can be configured
                              with the voice call trigger hwm command. When the hwm option is selected and the value is set to 100, no update is sent due
                              to high water mark.

## Examples

The following example sets the trigger for available capacity on trunk groups to send at a high water mark of 75%:

```
Router(config)# voice call trunk-group trigger hwm 75
```

### Related Commands

Command

Description

voice call capacity mir

Sets the values for the minimum interval between reporting (MIR) and smoothing transition time for weight (STW).

voice call capacity reporting

Turns on the reporting of maxima (first derivative) or inflection (second derivative) points in available capacity.

voice call capacity timer interval

Sets the periodic interval for reporting capacity from carrier, trunk group, or prefix databases

voice call trigger lwm

Sets the value for low water mark in the available capacity for carrier, trunk group, or prefix databases

voice call trigger percent-change

Sets the value for percentage change in the available capacity for carrier, trunk group, or prefix databases

## voice call trigger lwm

To set the value for low water mark in the available capacity in the trunk group or prefix databases, use the voice call trigger
                              lwm command in global configuration mode. To disable the trigger point, use the no form of this command.

voice call { carrier | trunk-group | prefix } trigger lwm percent

no voice call { carrier | trunk-group | prefix } trigger lwm percent

### Syntax Description

carrier

Carrier code address family

trunk-group

Trunk group address family

prefix

E.164 prefix

percent

Value can be 0 to 30 percent with a default of 10. If set to 0, this trigger will be turned off.

### Command Default

10 percent

### Command Modes

Global configuration

## Command History

Release

Modification

12.3(1)

This command was introduced.

### Usage Guidelines

Available circuits are reported when the value of AC falls below a threshold, called the low water mark. When the lwm option
                              is selected and the value is set to 0, no update is sent due to low water mark.

## Examples

The following example sets the trigger for available capacity for E.164 prefixes to send at a low water mark of 25%:

```
Router(config)# voice call prefix trigger lwm 25
```

### Related Commands

Command

Description

voice call capacity mir

Sets the values for the minimum interval between reporting (MIR) and smoothing transition time for weight (STW).

voice call capacity reporting

Turns on the reporting of maxima (first derivative) or inflection (second derivative) points in available capacity.

voice call capacity timer interval

Sets the periodic interval for reporting capacity from carrier, trunk group, or prefix databases.

voice call trigger hwm

Sets the value for high water mark in the available capacity for carrier, trunk group, or prefix databases.

voice call trigger percent-change

Sets the value for percentage change in the available capacity for carrier, trunk group, or prefix databases.

## voice call trigger percent-change

To set the value for percentage change, low water mark and high water mark in the available capacity in the trunk group or
                              prefix databases, use the voice call trigger command in global configuration mode. To disable the trigger point, use the no form of this command.

voice call { carrier | trunk-group | prefix } trigger percent-change percent

no voice call { carrier | trunk-group | prefix } trigger percent-change percent

### Syntax Description

carrier

Carrier code address family

trunk-group

Trunk group address family

prefix

E.164 prefix

percent

If percent-change is selected, value can be 0 to 100 percent with a default of 30. If set to 0, this trigger will be turned
                                          off.

If lwm is selected, value can be 0 to 30 percent with a default of 10. If set to 0, this trigger will be turned off.

If hwm is select, value can be 50 to 100 percent with a default of 80. If set to 100, this trigger will be turned off.

### Command Default

30 percent

### Command Modes

Global configuration

## Command History

Release

Modification

12.3(1)

This command was introduced.

### Usage Guidelines

Available circuits are reported when the absolute percent change is above a threshold. When the percent-change option is selected
                              and the value is set to 0, no update for percent change is sent

## Examples

The following example sets the trigger for available capacity on the carrier codes to send at a percentage change of 15%:

```
Router(config)# voice call carrier trigger percent-change 15
```

### Related Commands

Command

Description

voice call capacity mir

Sets the values for the minimum interval between reporting (MIR) and smoothing transition time for weight (STW).

voice call capacity reporting

Turns on the reporting of maxima (first derivative) or inflection (second derivative) points in available capacity.

voice call capacity timer interval

Sets the periodic interval for reporting capacity from carrier, trunk group, or prefix databases

voice call trigger hwm

Sets the value for high water mark in the available capacity for carrier, trunk group, or prefix databases

voice call trigger lwm

Sets the value for low water mark in the available capacity for carrier, trunk group, or prefix databases

## voice-card

To enter voice-card configuration mode and configure a voice card, use the voice-card command in global configuration mode. There is no no form of this command.

voice-card slot

### Syntax Description

slot

Slot number for the card to be configured. The following platform-specific numbering schemes apply:

- 0 is the Advanced Integration Module (AIM) slot in the router chassis.

- 1 is the network module slot in the router chassis.

- A value from 1 to 6 identifies a network module slot in the router chassis.

- 7 is AIM slot 0 in the router chassis.

- 8 is AIM slot 1.

### Command Default

No default behavior or values

### Command Modes

Global configuration

## Command History

Release

Modification

12.0(5)XK

The command was introduced on the Cisco 2600 series and Cisco 3600 series.

12.0(7)T

This command was integrated into Cisco IOS Release 12.0(7)T.

12.0(7)XK

This command was implemented on the Cisco MC3810.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T.

12.2(2)XB

Values for the slot argument were updated to include AIMs.

12.2(8)T

This command was integrated into Cisco IOS Release 12.2(8)T.

12.2(13)T

This command was supported in Cisco IOS Release 12.2(13)T and implemented on the Cisco 1700 series, Cisco 2600XM, Cisco 3700
                                          series, Cisco 7200 series, Cisco 7500 series, Cisco ICS7750, Cisco MC3810, and Cisco VG200.

12.2(15)T

This command was integrated into Cisco IOS Release 12.2(15)T.

### Usage Guidelines

Voice-card configuration mode is used for commands that configure the use of digital signal processing (DSP) resources, such
                              as codec complexity and DSPs. DSP resources can be found in digital T1/E1 packet voice trunk network modules on Cisco 2600
                              series, Cisco 3600 series, and Cisco 3700 series.

Codec complexity is configured in voice-card configuration mode and has the following platform-specific usage guidelines:

On Cisco 2600 series, Cisco 2600XM, Cisco 3660, Cisco 3725, and Cisco 3745, the slot argument corresponds to the physical chassis slot of the network module that has DSP resources to be configured.

DSP resource sharing is also configured in voice-card configuration mode. On the Cisco 2600 series, Cisco 2600XM, Cisco 3660,
                              Cisco 3725, and Cisco 3745 under specific circumstances, configuration of the dspfarm command enters DSP resources on a network module or AIM into a DSP resource pool. Those DSP resources are then available
                              to process voice traffic on a different network module or voice/WAN interface card (VWIC). See the dspfarm (voice-card) command
                              reference for more information about DSP resource sharing.

When running high-complexity images, the system can only process up to 16 voice channels. Those 16 time slots need to be
                                          within a contiguous range (timeslot maximum (TSmax) minus timeslot minimum (TSmin) is less than or equal to 16, where TSmax
                                          and TSmin are the maximum DS0 and minimum DS0 configured for voice).

This command does not have a no form.

## Examples

The following example enters voice-card configuration mode to configure resources on the network module in slot 1:

```
voice-card 1
```

The following example shows how to enter voice-card configuration mode and load high-complexity DSP firmware on voice-card
                              0. The dspfarm command enters the DSP resources on the AIM specified in the voice-card command into the DSP resource pool.

```
voice-card 0
 codec complexity high
 dspfarm
```

### Related Commands

Command

Description

codec complexity

Matches the DSP complexity packaging to the codecs to be supported.

dspfarm (voice-card)

Adds the specified voice card to those participating in a DSP resource pool.

## voice cause-code

To set the internal Q850 cause code mapping for voice and to enter voice cause configuration mode, use the voice cause-code command in global configuration mode. To disable the internal Q850 cause code mapping for voice, use the no form of this command.

voice cause-code

no voice cause-code

### Syntax Description

This command has no arguments or keywords.

### Command Default

Internal Q850 cause code mapping for voice is disabled.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

15.0(1)M

This command was introduced in a release earlier than Cisco IOS Release 15.0(1)M.

Cisco IOS XE Cupertino 17.7.1a

Introduced support for YANG models.

## Examples

The following example shows how to set the cause code mapping for voice:

```
Router> enable Router# configure terminal Router(config)# voice cause-code
```

### Related Commands

Command

Description

voice class codec

Assigns an identification tag number for a codec voice class.

## voice class aaa

To enable dial-peer-based VoIP AAA configurations, use the voice class aaa command in global configuration mode. To disable dial-peer-based VoIP AAA configurations, use the no form of this command.

voice class aaa tag

no voice class aaa tag

### Syntax Description

tag

A number used to identify voice class AAA. The range is from 1 to 10000. There is no default value.

### Command Default

No default behaviors or values

### Command Modes

Global configuration

## Command History

Release

Modification

12.2(11)T

This command was introduced on the Cisco 3660, Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5800, and Cisco AS5850.

### Usage Guidelines

The voice class aaa configuration command sets up a voice service class that allows you to perform dial-peer-based AAA configurations.

The command activates voice class AAA configuration mode. Commands that are configured in voice class AAA configuration mode
                              are listed in the "Related Commands" section.

## Examples

The following example shows AAA configurations in voice class AAA configuration mode. The number assigned to the tag is 1.

```
voice class aaa 1
 authentication method dp
 authorization method dp
 accounting method dp
in-bound
 accounting template temp-dp
```

The following example shows accounting configurations in voice class AAA configuration mode:

```
voice class aaa 2
 accounting method dp-out out-bound
 accounting template temp-dp out-bound
```

### Related Commands

Command

Description

accounting suppress

Disables accounting that is automatically generated by the service provider module for a specific dial peer.

authentication method

Specifies an authentication method for calls coming into the defined dial peer.

authorization method

Specifies an authorization method for calls coming into the defined dial peer.

method

Specifies an accounting method for calls coming into the defined dial peer.

voice-class aaa

Applies properties defined in the voice class to a specific dial peer.

## voice class busyout

To create a voice class for local voice busyout functions, use the voice class busyout command in global 
                              configuration mode. To delete the voice class, use the no form of this command.

voice class busyout tag

no voice class busyout tag

### Syntax Description

tag

Unique identification number assigned to one voice class. Range is 1 to 10000.

### Command Default

No voice class is configured for busyout functions.

### Command Modes

Global configuration

## Command History

Release

Modification

12.1(3)T

This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810.

### Usage Guidelines

You can apply a busyout voice class to multiple voice ports. You can assign only one busyout voice class to a voice port.
                              If a second busyout voice class is assigned to a voice port, the second voice class replaces the one previously assigned.

If you assign a busyout voice class to a voice port, you may not assign separate busyout commands directly to the voice port,
                              such as busyout monitor serial , busyout monitor ethernet , or busyout monitor probe .

## Examples

The following example configures busyout voice class 20, in which the connections to two remote interfaces are monitored by
                              a response time reporter (RTR) probe with a G.711ulaw profile, and voice ports are busied out whenever both links have a packet
                              loss exceeding 10 percent and a packet delay time exceeding 2 seconds:

```
voice class busyout 20
 busyout monitor probe 171.165.202.128 g711u loss 10 delay 2000
 busyout monitor probe 171.165.202.129 g711u loss 10 delay 2000
```

The following example configures busyout voice class 30, in which voice ports are busied out when serial ports 0/0, 1/0, 2/0,
                              and 3/0 go out of service.

```
voice class busyout 30
 busyout monitor serial 0/0
 busyout monitor serial 1/0
 busyout monitor serial 2/0
 busyout monitor serial 3/0
```

### Related Commands

Command

Description

busyout monitor ethernet

Configures a voice port to monitor a local Ethernet interface for events that would trigger a voice-port busyout.

busyout monitor probe

Configures a voice port to enter the busyout state if an RTR probe signal returned from a remote, IP-addressable interface
                                          crosses a specified delay or loss threshold.

busyout monitor serial

Configures a voice port to monitor a serial interface for events that would trigger a voice-port busyout.

show voice busyout

Displays information about the voice busyout state.

## voice class called number

To define a voice class called number or range of numbers, use the voice class called number command in global configuration mode. To remove a voice class called number, use the no form of this command.

voice class called number { inbound | outbound | pool } tag

no voice class called number

### Syntax Description

inbound

Inbound voice class called number.

outbound

Outbound voice class called number.

pool

Voice class called number pool.

tag

Digits that identify a specific inbound or outbound voice class called number or voice class called number pool.

### Command Default

No voice class called number is configured.

### Command Modes

Global configuration

## Command History

Release

Modification

12.4(11)T

This command was introduced.

### Usage Guidelines

Use this command to define one or more static voice class called numbers for inbound and outbound POTS dial peers or a dynamic
                              voice class called number pool. The indexes for a voice class called number are defined with the index (voice class) command.

Enter the voice class called number command in global configuration mode without hyphens. Enter the voice-class called-number command in dial-peer configuration mode with hyphens.

## Examples

The following example shows configuration for an outbound voice class called number:

```
voice class called number outbound 30
 index 1 5550100
 index 2 5550101
 index 3 5550102
 index 4 5550103
```

The following example shows configuration for a voice class called number pool:

```
voice class called number pool 1
 index 1 5550100 - 5550199
```

### Related Commands

Command

Description

show voice class called-number

Displays a specific voice class called number.

voice-class called-number (dial-peer)

Assigns a previously defined voice class called number to an inbound or outbound POTS dial peer.

## voice class cause-code

To configure cause code list parameters for a voice class and to enter cause code configuration mode, use the voice class cause-code command in global configuration mode. To disable the cause code list parameters configuration for a voice class, use the no form of this command.

voice class cause-code number

no voice class cause-code number

### Syntax Description

number

Numeric tag that specifies the voice class cause code. The range is from 1 to 64.

### Command Default

The cause code list parameters are not defined.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

15.0(1)M

This command was introduced in a release earlier than Cisco IOS Release 15.0(1)M.

## Examples

The following example shows how to configure cause code list parameters for voice class 5:

```
Router> enable Router# configure terminal Router(config)# voice class cause-code 5
```

### Related Commands

Command

Description

voice class codec

Assigns an identification tag number for a codec voice class.

## voice class codec

To enter voice-class configuration mode and assign an identification tag number for a codec voice class, use the voice class
                              codec command in global configuration mode. To delete a codec voice class, use the no form of this command.

voice class codec tag

no voice class codec tag

### Syntax Description

tag

Unique number that you assign to the voice class. Range is 1–10000. There is no default.

### Command Default

No default behavior or values

### Command Modes

Global configuration

## Command History

Release

Modification

12.0(2)XH

This command was introduced on the Cisco AS5300.

12.0(7)T

This command was implemented on the Cisco 2600 series and Cisco 3600 series.

12.0(7)XK

This command was implemented on the Cisco MC3810.

12.1(2)T

This command was integrated into Cisco IOS Release 12.1(2)T.

Introduced support for YANG models.

Cisco IOS XE Dublin
                                                17.10.1a

Introduced support for the following YANG models in codec
                                                preference configuration:

g729br8 [bytes <10-244>]

gsmamr-nb [encap | modes |
                                                      packetization-period]

Introduced support for the following YANG model in video
                                                codec configuration:

video codec [h261 | mpeg4]

### Usage Guidelines

This command only creates the voice class for codec selection preference and assigns an identification tag. Use the codec preference command to specify the parameters of the voice class, and use the voice-class codec dial-peer command to apply the voice class to a VoIP dial peer.

The voice class codec command in global configuration mode is entered without a hyphen. The voice-class codec command in dial-peer configuration mode is entered with a hyphen.

transparent is not available under voice class codec in YANG. However, you can configure codec transparent directly under dial-peer.

## Examples

The following example shows how to enter voice-class configuration mode and assign a voice class tag number starting from
                              global configuration mode:

```
voice class codec 10
```

After you enter voice-class configuration mode for codecs, use the codec preference command to specify the parameters of the voice class.

The following example creates preference list 99, which can be applied to any dial peer:

```
voice class codec 99
 codec preference 1 g711alaw
 codec preference 2 g711ulaw bytes 80
 codec preference 3 g723ar53
 codec preference 4 g723ar63 bytes 144
 codec preference 5 g723r53
 codec preference 6 g723r63 bytes 120
 codec preference 7 g726r16
 codec preference 8 g726r24
 codec preference 9 g726r32 bytes 80
 codec preference 10 g728
 codec preference 11 g729br8
 codec preference 12 g729r8 bytes 50
codec preference 13 gsmamr-nb
```

### Related Commands

Command

Description

codec preference

Specifies a list of preferred codecs to use on a dial peer.

test voice port detector

Defines the order of preference in which network dial peers select codecs.

voice-class codec (dial peer)

Assigns a previously configured codec selection preference list to a dial peer.

## voice class custom-cptone

To create a voice class for defining custom call-progress tones to be detected, use the voice class custom-cptone command in global 
                              configuration mode. To delete the voice class, use the no form of this command.

voice class custom-cptone cptone-name

no voice class custom-cptone cptone-name

### Syntax Description

cptone-name

Descriptive identifier for this class of custom call-progress tones that associates this set of custom call-progress tones
                                          with voice ports.

### Command Default

No voice class of custom call-progress tones is created.

### Command Modes

Global configuration

## Command History

Release

Modification

12.1(5)XM

This command was introduced on the Cisco 2600, Cisco 3600, and Cisco MC3810 platforms.

12.2(2)T

This command was implemented on Cisco 1750 access routers and integrated into Cisco IOS Release 12.2(2)T.

### Usage Guidelines

After you create a voice class, you need to define custom call-progress tones for this voice class using the dualtone command.

## Examples

The following example creates a voice class named country-x.

```
voice class custom-cptone country-x
```

The following example deletes the voice class named country-x.

```
no voice class custom-cptone country-x
```

### Related Commands

Command

Description

dualtone

Defines the tone and cadence for a custom call-progress tone.

supervisory custom-cptone

Associates a class of custom call-progress tones with a voice port.

voice class dualtone-detect-params

Modifies the boundaries and limits for call-progress tones.

## voice class dscp-profile

To configure the differentiated services code point (DSCP) profile, use the voice class dscp-profile command in global configuration mode. To disable the configuration, use the no form of this command.

voice class dscp-profile tag

no voice class dscp-profile tag

### Syntax Description

tag

Voice class DSCP tag. The range is from 1 to 10000.

### Command Default

A DSCP profile is not configured.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

15.2(2)T

This command was introduced.

### Usage Guidelines

You can use the voice class dscp-profile command to configure the DSCP profile and then configure DSCP policing and enter voice class configuration mode.

## Examples

The following example shows how to configure a DSCP profile and enter voice class configuration mode:

```
Router> enable Router# configure terminal Router(config)# voice class dscp-profile 1 Router(config-class)# end
```

### Related Commands

Command

Description

dscp media

Specifies the RPH to DSCP mapping.

## voice class dualtone

To create a voice class for Foreign Exchange Office (FXO) supervisory disconnect tone detection parameters, use the voice class dualtone command in global 
                              configuration mode. To delete the voice class, use the no form of this command.

voice class dualtone tag

no voice class dualtone tag

### Syntax Description

tag

Unique identification number assigned to one voice class. Range is from 1 to 10000.

### Command Default

No voice class is configured for tone detection parameters.

### Command Modes

Global configuration

## Command History

Release

Modification

12.1(3)T

This command was introduced on the Cisco 2600 series, Cisco 3600 series, and the Cisco MC3810.

### Usage Guidelines

Use this command first to create the voice class. Then use the supervisory disconnect dualtone voice-class command to assign the voice class to a voice port.

A voice class can define any number of tones to be detected. You need to define a matching tone for each supervisory disconnect
                              tone expected from a PBX or from the public switched telephone network (PSTN).

## Examples

The following example configures voice class dualtone 70, which defines one tone with two frequency components, and does not
                              configure a cadence list:

```
voice class dualtone 100
 freq-pair 1 350 440
 freq-max-deviation 10
 freq-max-power 6
 freq-min-power 25
 freq-power-twist 15
 freq-max-delay 16
 cadence-min-on-time 50
 cadence-max-off-time 400
 cadence-variation 8
 exit
```

The following example configures voice class dualtone 100, which defines one tone with two frequency components, and configures
                              a cadence list:

```
voice class dualtone 100
 freq-pair 1 350 440
 freq-pair 2 480 850
 freq-max-deviation 10
 freq-max-power 6
 freq-min-power 25
 freq-power-twist 15
 freq-max-delay 16
 cadence-min-on-time 50
 cadence-max-off-time 400
 cadence-list 1 100 100 300 300
 cadence-variation 8
 exit
```

The following example configures voice class dualtone 90, which defines three tones, each with two frequency components, and
                              configures two cadence lists:

```
voice class dualtone 90
 freq-pair 1 350 440
 freq-pair 2 480 850
 freq-pair 3 1000 1250
 freq-max-deviation 10
 freq-max-power 6
 freq-min-power 25
 freq-power-twist 15
 freq-max-delay 16
 cadence-min-on-time 50
 cadence-max-off-time 500
 cadence-list 1 100 100 300 300 100 200
 cadence-list 2 100 200 100 400
 cadence-variation 8
 exit
```

### Related Commands

Command

Description

supervisory disconnect dualtone voice-class

Assigns a previously configured voice class for FXO supervisory disconnect tone to a voice port.

## voice class dualtone-detect-params

To create a voice class for defining a set of tolerance limits for the frequency, power, and cadence parameters of the tones
                              to be detected, use the voice class dualtone-detect-params command in global 
                              configuration mode. To delete the voice class, use the no form of this command.

voice class dualtone-detect-params tag

no voice class dualtone-detect-params tag

### Syntax Description

tag

Unique tag identification number assigned to a voice class. Range is from 1 to 10000.

### Command Default

No voice class is configured for defining answer-supervision tolerance limits.

### Command Modes

Global configuration

## Command History

Release

Modification

12.1(5)XM

This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810.

12.2(2)T

This command was implemented on Cisco 1750 routers and integrated into Cisco IOS Release 12.2(2)T.

### Usage Guidelines

Use this command to create a voice class in which you can define maximum and minimum call-progress tone tolerance parameters
                              that you can apply to any voice port. These parameters further define the call-progress tones defined by the voice class custom-cptone command. Use the supervisory dualtone-detect-params command to apply these tolerance parameters to a voice port.

## Examples

The following example creates voice class 70, in which you can specify modified boundaries and limits for call-progress tone
                              detection.

```
voice class dualtone-detect-params 70
freq-max-deviation 25
freq-max-power -5
freq-min-power -20
freq-power-twist 10
freq-max-delay 50
cadence-variation 80
exit
```

### Related Commands

Command

Description

supervisory dualtone-detect-params

Assigns the boundary and detection tolerance parameters defined by the voice class dualtone-detect-params command to a voice port.

voice class custom-cptone

Creates a voice class for defining custom call-progress tones.

## voice class e164-pattern-map

To create an E.164 pattern map that specifies multiple destination E.164 patterns in a dial peer, use the voice class e164-pattern map command in global configuration mode. To remove an E.164 pattern map from a dial peer, use the no form of this command.

voice class e164-pattern-map tag

no voice class e164-pattern-map

### Syntax Description

tag

A number assigned to a voice class E.164 pattern map. The range is from 1 to 10000.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

15.2(4)M

This command was introduced.

Cisco IOS XE Cupertino 17.7.1a

Introduced support for YANG models.

## Examples

The following example shows how to create an E.164 pattern map that specifies multiple destination E.164 patterns in a dial
                              peer:

```
Device(config)# voice class e164-pattern-map 2543
```

### Related Commands

Command

Description

show voice class e164-pattern-map

Displays the configuration of E.164 pattern maps.

voice class e164-pattern-map load

Loads a destination E.164 pattern map that is specified by a text file on a dial peer.

## voice-class dpg

To create a dial-peer group for grouping multiple outbound dial peers, use the voice class dpg command in global configuration mode.

voice class dpg dial-peer-group-id

### Syntax Description

dial-peer-group-id

Assigns a tag for a particular dial-peer group. The range is 1-10000.

### Command Default

Disabled by default.

### Command Modes

Global configuration voice class (config).

## Command History

Release

Modification

Cisco IOS 15.4(1)T

Cisco IOS XE 3.11S

Introduced support for YANG models.

### Usage Guidelines

You can group up to 20 outbound (H.323, SIP or POTS) dial peers into a dial-peer group and configure this dial-peer group
                              as the destination of an inbound dial peer. Once an incoming call is matched by an inbound dial peer with an active destination
                              dial-peer group, dial peers from this group are used to route the incoming call. No other outbound dial-peer provisioning
                              to select outbound dial peers is used.

A preference can be defined for each dial peer in a dial-peer group. This preference is used to decide the order of selection
                              of dial peers from the group for the setup of an outgoing call.

You can also specify various dial-peer hunt mechanisms using the existing dial-peer hunt command. For more information, refer
                              to Configure Outbound Dial-Peer Group as an Inbound Dial-Peer Destination .

## Examples

```
Router(config)#voice class dpg ?
  <1-10000>  Voice class dialpeer group tag

Router(config)#voice class dpg 1 
Router(config-class)#dial-pee
Router(config-class)#dial-peer ?
  <1-1073741823>  Voice dial-peer tag

Router(config-class)#dial-peer 1 ?
  preference  Preference order of this dialpeer in a group
  <cr>        <cr>

Router(config-class)#dial-peer 1 pre
Router(config-class)#dial-peer 1 preference ?
  <0-10>  Preference order

Router(config-class)#dial-peer 1 preference 9
Router(config-class)#
```

### Related Commands

Command

Description

dial-peer voice

destination -pattern

To configure a destination pattern.

## voice class e164-pattern-map load

To load a destination E.164 pattern map that is specified by a text file on a dial peer, use the voice class e164-pattern-map load command in privileged EXEC mode.

voice class e164-pattern-map load tag

### Syntax Description

tag

A number that is assigned to the destination E.164 pattern map. The range is from 1 to 10000.

### Command Default

No default behavior or values.

### Command Modes

Privileged EXEC (#)

## Command History

Release

Modification

15.2(4)M

This command was introduced.

### Usage Guidelines

After creating an E.164 pattern map, you can add destination E.164 pattern entries to the E.164 pattern map and store all
                              the information on the voice gateway or create the E.164 pattern entries in a text file and store the file on the internally
                              or externally supported file system.

## Examples

The following example shows how to reload a particular destination E.164 pattern map on a dial peer:

```
Device# voice class e164-pattern-map load 2543
```

### Related Commands

Command

Description

show voice class e164-pattern-map

Displays the configuration of E.164 pattern maps.

voice class e164-pattern-map

Creates an E.164 pattern map to specify multiple destination E.164 patterns in a dial peer.

## voice class e164-translation

To translate the phone number of the call source into E.164 format, as per the translation rules, use the voice class e164-translation command in global configuration mode.

voice class e164-translation tag

### Syntax Description

tag

The range is from 1 to 10000.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

IOS XE Fuji Release 16.8.1

This command was introduced.

## Examples

The following example translates the input call number with tag 1 into E.164 format.

```
Router(config)# voice class e164-translation 1 Router(config-class)# url ftp://test:test123@8.0.0.200/test_e164.cfg Router(config-class)# ^Z
```

### Related Commands

voice class e164-pattern-map

Creates an E.164 pattern map to specify multiple destination E.164 patterns in dial peer.

voice class e164-pattern-map load

Loads a destination E.164 pattern map that is specified by a text file on a dial peer.

## voice class h323

To create an H.323 voice class that is independent of a dial peer and can be used on multiple dial peers, use the voice class
                              h323 command in global configuration mode. To remove the voice class, use the no form of this command.

voice class h323 tag

no voice class h323

### Syntax Description

tag

Unique number to identify the voice class. Range is from 1 to 10000. There is no default value.

### Command Default

No default behavior or values

### Command Modes

Global configuration

## Command History

Release

Modification

12.1(2)T

This command was introduced on the Cisco 1700, Cisco 2600 series, Cisco 3600 series, Cisco 7200 series, Cisco AS5300, Cisco
                                          uBR910, and Cisco uBR924.

### Usage Guidelines

The voice class h323 command in global configuration mode does not include a hyphen. The voice-class h323 command in dial-peer configuration mode includes a hyphen.

## Examples

The following example demonstrates how a voice class is created and applied to an individual dial peer. Voice class 4 contains
                              a command to disable the capability to detect Cisco CallManager systems in the network (this command is used by Cisco CallManager
                              Express 3.1 and later versions). The example then uses the voice-class h323 command to apply voice class 4 to dial peer 36.

```
Router(config)# voice class h323 4 Router(config-class)# no telephony-service ccm-compatible Router(config-class)# exit Router(config)# dial-peer voice 36 voip Router(config-dial-peer)# destination-pattern 555.... Router(config-dial-peer)# session target ipv4:10.5.6.7 Router(config-dial-peer)# voice-class h323 4
```

### Related Commands

Command

Description

voice-class h323

Assigns an H.323 voice class to a VoIP dial peer.

## voice class media

To configure the media control parameters for voice, use the voice class media command in global configuration mode. To disable the media control parameters for voice, use the no form of this command.

voice class media number

no voice class media number

### Syntax Description

number

Numeric tag that specifies the voice class media. The range is from 1 to 10000.

### Command Default

The media control parameters for voice are not configured.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

15.0(1)M

This command was introduced in a release earlier than Cisco IOS Release 15.0(1)M.

Cisco IOS XE Cupertino 17.7.1a

Introduced support for YANG models.

## Examples

The following example shows how to configure media control parameters for voice:

```
Router> enable Router# configure terminal Router(config)# voice class media 5
```

### Related Commands

Command

Description

voice class codec

Assigns an identification tag number for a codec voice class.

## voice class permanent

To create a voice class for a Cisco trunk or FRF.11 trunk, use the voice class permanent command in global configuration mode. To delete the voice class, use the no form of this command.

voice class permanent tag

no voice class permanent tag

### Syntax Description

tag

Unique number that you assign to the voice class. Range is from 1 to 10000.

### Command Default

No voice class is configured.

### Command Modes

Global configuration

## Command History

Release

Modification

12.0(3)XG

This command was introduced on the Cisco MC3810.

12.0(4)T

This command was integrated into Cisco IOS Release 12.0(4)T.

12.1(3)T

This command was implemented on Cisco 2600 series and Cisco 3600 series.

### Usage Guidelines

The voice class permanent command can be used for Voice over Frame Relay (VoFR), Voice over ATM (VoATM), and Voice over IP (VoIP) trunks.

The voice class permanent command in global configuration mode is entered without a hyphen. The voice-class permanent command in dial-peer and voice-port configuration modes is entered with a hyphen.

## Examples

The following example shows how to create a permanent voice class starting from global configuration mode:

```
voice class permanent 10
 signal keepalive 3
 exit
```

### Related Commands

Command

Description

signal keepalive

Configures the keepalive signaling packet interval for Cisco trunks and FRF.11 trunks.

signal pattern

Configures the ABCD bit pattern for Cisco trunks and FRF.11 trunks.

signal timing idle suppress-voice

Configures the signal timing parameter for the idle state of a call.

signal timing oos

Configures the signal timing parameter for the OOS state of a call.

signal-type

Sets the signaling type for a network dial peer.

voice-class permanent

Assigns a previously configured voice class for a Cisco trunk or FRF.11 trunk to a network dial peer.

## voice class resource-group

To enter voice-class configuration mode and assign an identification tag number for a resource group, use the voice class resource-group command in global configuration mode. To delete a resource group, use the no form of this command.

voice class resource-group tag

no voice class resource-group tag

### Syntax Description

tag

Unique tag to identify the resource. The range is from 1 to 5.

### Command Default

No resource groups are created.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

15.1(2)T

This command was introduced.

### Usage Guidelines

Use the voice class resource-group command to configure parameters along with the threshold values to be monitored for resource groups. When you use the voice class resource-group command, the router enters voice-class configuration mode. You can then group the resources to be monitored and configure
                              parameters such as .

## Examples

The following example shows how to enter voice-class configuration mode and assign identification tag number 5 for a resource
                              group:

```
Router> enable Router# configure terminal Router(config)# voice class resource-group 5
```

### Related Commands

Command

Description

debug rai

Enables debugging for Resource Allocation Indication (RAI).

periodic-report interval

Configures periodic reporting parameters for gateway resource entities.

rai target

Configures the SIP RAI mechanism.

resource (voice)

Configures parameters for monitoring resources.

show voice class resource-group

Displays the resource group configuration information for a specific resource group or all resource groups.

## voice class route-string

To assign a unique identifier tag to a route string, use the voice class route-string command in global configuration mode. To remove the route string, use the no form for this command.

voice class route-string tag

no voice class route-string tag

## Syntax Description

Unique tag to identify the route string. The range is from 1 to 10000.

### Command Default

An identifier tag for the route string is not configured.

### Command Modes

Global configuration (config)

## Command History

15.3(3)M

This command was introduced.

Cisco IOS XE Release 3.10S

This command was integrated into Cisco IOS XE Release 3.10S.

### Usage Guidelines

Use the voice class route-string command to assign a unique identification tag to the route string. You can use this command to enter voice class configuration
                              mode to configure a route string pattern.

## Examples

The following example shows how to assign identification tag 2 for a route string:

```
Device> enable Device# configure terminal Device(config)# voice class route-string 2 Device(config-class)# pattern london.uk.eu
```

## voice class server-group

To enter voice-class configuration mode and configure server groups (groups of IPv4 and IPv6 addresses) which can be referenced
                              from an outbound SIP dial peer, use the voice class server-group command in global configuration mode. To delete a server group, use the no form of this command.

voice class server-group server-group-id

no voice class server-group server-group-id

server-group-id

Unique server group ID to identify the server group. You can configure up to five servers per server group.

### Command Default

No server groups are created.

### Command Modes

Global configuration (config)

Release

Modification

Cisco IOS XE Release 3.11S

15.4(1)T

The following commands were introduced or modified: voice class server-group , description , ipv4 port preference , ipv6 port preference , hunt-scheme , show voice class server-group , shutdown (Server Group) .

The following command is introduced under voice class server-group . huntstop rule-tag resp-code from_resp_code to to_resp_code .

Cisco IOS XE Cupertino 17.7.1a

Introduced support for YANG models.

### Usage Guidelines

Use the voice class server-group command to group IPv4 and IPv6 addresses of servers and configure it as in an outbound SIP dial-peer. When you use the voice class server-group command, the router enters voice-class configuration mode. You can then group the servers and associate them with a SIP outbound
                              dial peer.

## Examples

The following example shows how to enter voice-class configuration mode and assign server group id for a server group:

```
Router> enable Router# configure terminal Router(config)# voice class server-group 2
```

After configuring a voice class server-group, you can configure a server IP address along with an optional port number and
                              preference, as part of this server group along with an optional port number and preference order. You can also configure description,
                              hunt-scheme, and huntstop. You can use the shutdown command to make the server group inactive.

```
Device(config)# voice class server-group 2
Device(config-class)# ipv4 10.1.1.1 preference 1
Device(config-class)# ipv4 10.1.1.2 preference 2
Device(config-class)# ipv4 10.1.1.3 preference 3
Device(config-class)# description It has 3 entries
Device(config-class)# hunt-scheme round-robin
Device(config-class)# huntstop 1 resp-code 400 to 599
Device(config-class)# exit
```

### Related Commands

Command

Description

description

Provides a description for the server group.

hunt-scheme

Defines a hunt method for the order of selection of target server IP addresses (from the IP addresses configured for this
                                          server group) for the setting up of outgoing calls.

shutdown (Server Group)

To make the server group inactive.

show voice class server-group

Displays the configurations for all configured server groups or a specified server group.

## voice class sip-copylist

To configure a list of entities to be sent to the peer call leg, use the voice class sip-copylist command in global configuration mode. To disable the configuration, use the no form of this command.

voice class sip-copylist tag

no voice class sip-copylist tag

### Syntax Description

tag

Voice class Session Initiation Protocol (SIP) copylist tag. The range is from 1 to 10000.

### Command Default

No header is sent to the peer call leg.

### Command Modes

Global configuration (config).

Voice class tenant configuration (config-class).

## Command History

Release

Modification

15.1(3)T

This command was introduced.

Cisco IOS XE Cupertino 17.7.1a

Introduced support for YANG models.

### Usage Guidelines

Use the voice class sip-copylist command to configure Cisco Unified Border Element (UBE) to pass an unsupported parameter present in a mandatory header from
                              one call leg to another of Cisco UBE. You can copy the inbound message headers into variables and pass the headers to the
                              outbound call leg.

## Examples

The following example shows how to configure a SIP list to be sent to the peer call leg:

```
Router(config)# voice class sip-copylist 5
```

### Related Commands

Command

Description

sip-header

Specifies the SIP header to be sent to the peer call leg.

## voice class sip-hdr-passthrulist

To configure a list of headers to pass-through, use the voice class sip-hdr-passthrulist command in global configuration mode. To remove the header pass-through, use the no form of this command.

voice class sip-hdr-passthrulist tag

no voice class sip-hdr-passthrulist tag

## Syntax Description

Unique tag to identify the header. The range is from 1 to 1000.

### Command Default

None

### Command Modes

Global configuration (config)

Voice class tenant configuration (config-class)

## Command History

15.3(3)M

This command was introduced.

Cisco IOS XE Release 3.10S

This command was integrated into Cisco IOS XE Release 3.10S.

Introduced support for YANG models.

### Usage Guidelines

Use the voice class sip-hdr-passthrulist command to configure a list of headers to be passed-through the route string. You can use this command to enter the voice
                              class configuration mode to configure route-string header pass-through.

## Examples

The following example shows how to configure header pass-through with the unique identification tag 2:

```
Device> enable Device# configure terminal Device(config)# voice class sip-hdr-passthrulist 2 Device(config-class)# passthru-hdr x-cisco-dest-route-string Device(config-class)# passthru-hdr Supported Device(config-class)# passthru-hdr Subject
```

## voice class sip-profiles

To configure Session Initiation Protocol (SIP) profiles for a voice class, use the voice class sip-profiles command in global configuration mode. To disable the SIP profiles for a voice class, use the no form of this command.

voice class sip-profiles number

no voice class sip-profiles number

### Syntax Description

number

Numeric tag that specifies the voice class SIP profile. The range is from 1 to 10000.

### Command Default

SIP profiles for a voice class are not configured.

### Command Modes

Global configuration (config).

Voice class tenant configuration (config-class).

## Command History

Release

Modification

15.0(1)M

This command was introduced in a release earlier than Cisco IOS Release 15.0(1)M.

Cisco IOS XE Cupertino 17.7.1a

Introduced support for YANG models.

### Usage Guidelines

The rule option [before] is not available in sip-profile YANG configuration.

voice class sip-profile <tag>

rule [before]

## Examples

The following example shows how to specify SIP profile 2 for a voice class:

```
Router> enable Router# configure terminal Router(config)# voice class sip-profiles 2
```

### Related Commands

Command

Description

voice class codec

Assigns an identification tag number for a codec voice class.

## voice class
                        	 srtp-crypto

To enter voice class configuration mode and assign an identification tag for srtp-crypto voice class, use the voice class srtp-crypto command in global configuration mode. To delete srtp-crypto voice class , use the no form of this command.

voice class srtp-crypto tag

no voice class
                                 				  srtp-crypto tag

## Syntax Description

Unique number that you assign to the srtp-crypto voice class. Range is 1–10000. There is no default.

### Command Default

No default behavior or values.

### Command Modes

Global configuration (config).

## Command History

This
                                       					 command was introduced.

Cisco IOS XE Cupertino 17.7.1a

Cisco IOS XE Dublin
                                             17.10.1a

The YANG model for this command can now be configured under voice register pool .

### Usage Guidelines

This command only
                              		  creates the voice class for srtp-crypto preference selection and assigns an
                              		  identification tag. Use the crypto command under voice class srtp-crypto submode to select the ordered list of
                              		  preferred cipher-suites.

Deleting srtp-crypto voice class using no voice class srtp-crypto tag command removes the srtp-crypto tag (same tag) if configured in global, tenant, and dial-peer configuration mode.

## Examples

```
Device> enable Device# configure terminal Device(config)# voice class srtp-crypto 100
```

### Related Commands

Command

Description

srtp-crypto

Assigns a previously configured crypto-suite selection preference list globally or to a voice class tenant.

crypto

Specifies the preference for an SRTP cipher-suite that will be offered by Cisco Unified Border Element (CUBE) in the SDP in
                                          offer and answer.

show sip-ua calls

Displays active user agent client (UAC) and user agent server (UAS) information on Session Initiation Protocol (SIP) calls.

show sip-ua srtp

Displays Session Initiation Protocol (SIP) user-agent (UA) Secure Real-time Transport Protocol (SRTP) information.

## voice class
                        	 tenant

To enter voice
                              		  class tenant configuration mode and to allow tenants to configure their own
                              		  global configurations for a specific voice class, use the voice class tenant command in global configuration mode. To
                              		  disable the tenant configurations for a voice class, use the no form of
                              		  this command.

voice class tenant tag

no voice class tenant tag

### Syntax Description

tag

A
                                          						number used to identify voice class tenant. The range is from 1 to 10000. There
                                          						is no default value.

### Command Default

No default
                              		  behavior or values.

### Command Modes

Global configuration (config)

## Command History

Release

Modification

15.6(2)T and IOS XE Denali 16.3.1

This
                                          						command was introduced.

Introduced support for YANG models.

### Usage Guidelines

The voice class tenant command sets up a voice service class that
                              		  allows tenants to configure their own sip-specific configurations.

## Examples

The following
                              		  example shows how to configure tenants for a voice class:

```
Device(config)# voice class tenant 1 Device (config-class)# ? aaa – sip-ua AAA related configuration
anat – Allow alternative network address types IPV4 and IPV6
asserted-id – Configure SIP-UA privacy identity settings
……
……
Video – video related function
Warn-header – SIP related config for SIP. SIP warning-header global config
Device (config-voi-tenant)# end
```

## voice class tls-profile

To enable voice class configuration mode, and assign an identification tag for a TLS profile, use the command voice class tls-profile in global cofiguration mode. To remove a tls-profile, use the no form of this command.

no voice class tls-profile tag

### Syntax Description

tag

A number used to identify voice class TLS profile.

The range is 1-10000.

There is no default value.

### Command Default

No default behavior or values

### Command Modes

Global configuration (config)

## Command History

Release

Modification

This command was introduced.

### Usage Guidelines

The command voice class tls-profile enables voice class configuration mode on the router and provides you sub-options to configure commands required for a TLS
                              session. This command allows you to configure under voice class, the options that can be configured at the global level via
                              sip-ua.

The tag associates all the voice class configurations that are made through the command voice class tls-profile tag to the command crypto signaling . Following is the crypto signaling command with tls-profile tag :

crypto signaling { remote-addr ip address subnet mask | default } tls-profile tag

For more information on the updates to the command crypto signaling , see crypto signaling .

## Examples

The following example configures the voice class tls-profile with tag '2' and enables voice class cofiguration mode:

```
Router(config)#voice class tls-profile 2
Router(config-class)#
```

The following section provides details of the sub-commands that can be configured under the command voice class tls-profile tag .

The following example configures CUBE to use the trustpoint trustpoint-name keyword and argument when it establishes or accepts the TLS connection with a remote device:

```
Router(config-class)#trustpoint CUBETP
```

The following example configures client verification trustpoint:

```
Router(config-class)#client-vtp TPname
```

The following example indicates the description for the TLS profile group:

```
Router(config-class)#description tlsgroupname
```

The following example configures the specific size of elliptic curves to be used for a TLS session:

```
Router(config-class)#cipher ecdsa-cipher curve-size 384
```

The following example configures CUBE to perform server identity validation through Common Name (CN) and Subject Alternate Name (SAN) fields in the server certificate:

```
Router(config-class)#cn-san-validate server
```

The following example enables Server Name Indication (SNI) required during the initial TLS handshake process:

```
Router(config-class)#sni send
```

### Related Commands

Command

Description

trustpoint

Creates a trustpoint to store the devices certificate that is generated as part of the enrollment process using Cisco IOS
                                          public-key infrastructure (PKI) commands.

Provides a description for the TLS profile group.

client-vtp

Assigns a client verification trustpoint.

cipher

Configures cipher setting.

cn-san

Enables server identity validation through Common Name (CN) and Subject Alternate Name (SAN) fields in the server certificate
                                          during client-side SIP /TLS connections

sni send

Enables TLS Server Name Indication (SNI) during the initial TLS handshake process.

crypto signaling

Identifies the trustpoint or the tls-profile tag that is used during the TLS handshake process.

## voice class tls-cipher

To configure an ordered set of TLS cipher suites, use voice class tls-cipher command. To disable this command or revert to default, use the no form of this command.

voice class tls-cipher tag

no voice class tls-cipher tag

Specifies the voice class tls-cipher tag.

### Command Default

No default behavior or values

### Command Modes

Global configuration (config)

Release

Modification

This command was introduced.

### Usage Guidelines

The voice class tls-cipher command enables voice class configuration mode on the router, allowing you to configure an ordered list of TLS cipher suites:

## Examples

```
Router(config)#voice class tls-cipher 123

Router(config-class)# cipher ?
    <1-10>  Set the preference order for the cipher-suite (1 = Highest)
	
Router(config-class)#cipher 1 ?

AES128_GCM_SHA256              supported in TLS 1.3 
AES256_GCM_SHA384              supported in TLS 1.3  
CHACHA20_POLY1305_SHA256       supported in TLS 1.3 
DHE_RSA_AES128_GCM_SHA256      supported in TLS 1.2
DHE_RSA_AES256_GCM_SHA384      supported in TLS 1.2
DHE_RSA_WITH_AES_128_CBC_SHA   supported in TLS 1.2 & below
DHE_RSA_WITH_AES_256_CBC_SHA   supported in TLS 1.2 & below
ECDHE_ECDSA_AES128_GCM_SHA256  supported in TLS 1.2
ECDHE_ECDSA_AES256_GCM_SHA384  supported in TLS 1.2
ECDHE_RSA_AES128_GCM_SHA256    supported in TLS 1.2
ECDHE_RSA_AES256_GCM_SHA384    supported in TLS 1.2
RSA_WITH_AES_128_CBC_SHA       supported in TLS 1.2 & below
RSA_WITH_AES_256_CBC_SHA       supported in TLS 1.2 & below

Router(config-class)# cipher 1 ECDHE_RSA_AES256_GCM_SHA384 ?
<cr>   <cr>
Router(config-class)#
```

## voice class tone-signal

To enter voice-class configuration mode and create a tone-signal voice class, use the voice class tone-signal command in global configuration mode. To delete a tone-signal voice class, use the no form of this command.

voice class tone-signal tag

no voice class tone-signal tag

### Syntax Description

tag

Label that uniquely identifies the voice class. Can be up to 32 alphanumeric characters.

### Command Default

No default behavior or values

### Command Modes

Global configuration

## Command History

Release

Modification

12.3(4)XD

This command was introduced.

12.3(7)T

This command was integrated into Cisco IOS Release 12.3(7)T.

### Usage Guidelines

Use the voice class tone-signal command to define wakeup, frequency selection, and guard tones to be played out before and during the voice packets for a
                              specific voice port. Use the inject guard-tone , inject pause , and inject tone commands to define the tone signaling in this class. You can configure up to ten tones in a tone-signal voice class.

To avoid voice loss at the receiving end of an LMR system, the maximum of the sum of the durations of the injected tones and
                              pauses in the voice class should not exceed 1500 milliseconds. You must also use the timing delay-voice tdm command to configure a delay for the voice packet equal to the sum of the durations of all the injected tones and pauses.

Note that the hyphenation in this command differs from the hyphenation used in a similar command, voice-class tone-signal , which is used in voice-port configuration mode.

## Examples

The following example shows how to create a tone-signal voice class starting from global configuration mode:

```
voice class tone-signal mytones
 inject tone 1 1950 3 150
 inject tone 2 2000 0 60
 inject pause 3 60
 inject tone 4 2175 3 150
 inject tone 5 1000 0 50
```

### Related Commands

Command

Description

inject guard-tone

Plays out a guard tone with the voice packet.

inject pause

Specifies a pause between injected tones.

inject tone

Specifies a wakeup or frequency selection tone to be played out before the voice packet.

timing delay-voice tdm

Specifies the delay before a voice packet is played out.

voice-class tone-signal

Assigns a previously configured tone-signal voice class to a voice port.

## voice class uri

To create or modify a voice class for matching dial peers to a Session Initiation Protocol (SIP) or telephone (TEL) uniform
                              resource identifier (URI), use the voice class uri command in global configuration mode. To remove the voice class, use the no form of this command.

voice class uri tag { sip | tel }

no voice class uri tag

### Syntax Description

tag

Label that uniquely identifies the voice class. Can be up to 32 alphanumeric characters.

sip

Voice class for SIP URIs.

tel

Voice class for TEL URIs.

### Command Default

No default behavior or values

### Command Modes

Global configuration

## Command History

Release

Modification

12.3(4)T

This command was introduced.

Cisco IOS XE Cupertino 17.7.1a

### Usage Guidelines

This command takes you to voice URI class configuration mode, where you configure the match characteristics for a URI. The
                                    commands that you enter in this mode define the set of rules by which the URI in a call is matched to a dial peer.

To reference this voice class for incoming calls, use the incoming uri command in the inbound dial peer. To reference this voice class for outgoing calls, use the destination uri command in the outbound dial peer.

Using the no voice class uri command removes the voice class from any dial peer where it is configured with the destination uri or incoming uri commands.

## Examples

The following example defines a voice class for SIP URIs:

```
voice class uri r100 sip
 user-id abc123
 host server1
 phone context 408
```

The following example defines a voice class for TEL URIs:

```
voice class uri r101 tel
 phone number ^408
 phone context 408
```

### Related Commands

Command

Description

debug voice uri

Displays debugging messages related to URI voice classes.

destination uri

Specifies the voice class used to match the dial peer to the destination URI for an outgoing call.

host

Matches a call based on the host field in a SIP URI.

incoming uri

Specifies the voice class used to match a VoIP dial peer to the URI of an incoming call.

pattern

Matches a call based on the entire SIP or TEL URI.

phone context

Filters out URIs that do not contain a phone-context field that matches the configured pattern.

phone number

Matches a call based on the phone number field in a TEL URI.

show dialplan incall uri

Displays which dial peer is matched for a specific URI in an incoming call.

show dialplan uri

Displays which outbound dial peer is matched for a specific destination URI.

user-id

Matches a call based on the user-id field in the SIP URI.

## voice class uri sip preference

To set the preference for selecting a voice class for Session Initiation Protocol (SIP) uniform resource identifiers (URIs),
                              use the voice class uri sip preference command in global configuration mode. To reset to the default, use the no form of this command.

voice class uri sip preference { user-id | host }

no voice class uri sip preference

### Syntax Description

user-id

User-id field is given preference.

host

Host field is given preference.

### Command Default

Host field

### Command Modes

Global configuration

## Command History

Release

Modification

12.3(4)T

This command was introduced.

### Usage Guidelines

Use this command to resolve ties when more than one voice class is matched for a SIP URI. The default is to match on the host
                                    field of the URI.

This command applies globally to all URI voice classes for SIP.

## Examples

The following example defines the preference as the user-id for a SIP voice class:

```
voice class uri sip preference user-id
```

### Related Commands

Command

Description

debug voice uri

Displays debugging messages related to URI voice classes.

destination uri

Specifies the voice class used to match the dial peer to the destination URI for an outgoing call.

host

Matches a call based on the host field in a SIP URI.

incoming uri

Specifies the voice class used to match a VoIP dial peer to the URI of an incoming call.

user-id

Matches a call based on the user-id field in the SIP URI.

show dialplan incall uri

Displays which dial peer is matched for a specific URI in an incoming call.

show dialplan uri

Displays which outbound dial peer is matched for a specific destination URI.

voice class uri

Creates or modifies a voice class for matching dial peers to a SIP or TEL URI.

## voice-class aaa (dial peer)

To apply properties defined in the voice class to a dial peer, use the voice-class aaa command in dial-peer configuration mode. This command does not have a no form.

voice-class aaa tag

### Syntax Description

tag

A number to identify the voice class. Range is from 1 to 10000. There is no default.

### Command Default

No default behaviors or values

### Command Modes

Dial-peer configuration

## Command History

Release

Modification

12.2(11)T

This command was introduced on the Cisco 3660, Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5800, and Cisco AS5850.

### Usage Guidelines

Properties that are configured in voice class AAA configuration mode can be applied to a dial peer by using this command.

## Examples

The following example shows redirecting AAA requests using Digital Number Identification Service (DNIS). You define a voice
                              class to specify the AAA methods and then use this command.

```
voice class aaa 1
  authentication method kz
  authorization method kz
  accounting method kz
!
dial-peer voice 100 voip
  incoming called-number 50..
  session target ipv4:1.5.31.201
  voice-class aaa 1
```

### Related Commands

Command

Description

voice class aaa

Enables dial-peer-based VoIP AAA configurations.

## voice-class called-number (dial peer)

To assign a previously defined voice class called number to an inbound or outbound POTS dial peer, use the voice-class called-number command in dial peer configuration mode. To remove a voice class called number from the dial peer, use the no form of this command.

voice-class called-number [ inbound | outbound ] tag

no voice-class called-number

### Syntax Description

inbound

Assigns an inbound voice class called number to the dial peer.

outbound

Assigns an outbound voice class called number to the dial peer.

tag

Digits that identify a specific voice class called number.

### Command Default

No voice class called number is configured on the dial peer.

### Command Modes

Dial peer configuration

## Command History

Release

Modification

12.4(11)T

This command was introduced.

### Usage Guidelines

Use this command to assign a previously defined voice class called number to a dial peer for a static H.320 secondary call
                              dial plan. Use the inbound keyword for inbound POTS dial peers, and the outbound keyword for outbound POTS dial peers.

The voice class called number command in global configuration mode is entered without hyphens. The voice-class called-number command in dial peer configuration mode is entered with hyphens.

## Examples

The following example shows configuration for an outbound voice class called number outbound on POTS dial peer 22:

```
dial-peer voice 22 pots
 voice-class called-number inbound 300
```

### Related Commands

Command

Description

voice class called number

Defines a voice class called number or range of numbers for H.320 calls.

voice-class called-number-pool

Defines a pool of dynamic voice class called numbers for a voice port.

## voice-class called-number-pool

To assign a previously defined voice class called number pool to a voice port, use the voice-class called-number-pool command in voice class configuration mode. To remove a voice class called number pool from the voice port, use the no form of this command.

voice-class called-number-pool tag

no voice-class called-number-pool

### Syntax Description

tag

Digits that identify a specific voice class called number pool.

### Command Default

No voice class called number pool is assigned to the voice port.

### Command Modes

Voice class configuration

## Command History

Release

Modification

12.4(11)T

This command was introduced.

### Usage Guidelines

Use this command to assign a voice class called number pool to a voice port for a dynamic H.320 secondary call dial plan.

## Examples

The following example shows configuration for voice class called number pool 100 on voice port 1/0/0:

```
voice-port 1/0/0
 voice-class called-number-pool 100
```

### Related Commands

Command

Description

voice class called number

Defines a voice class called number or range of numbers for H.320 calls.

voice-class called-number (dial peer)

Defines a called number or range of called numbers for a POTS dial peer.

## voice-class codec (dial peer)

To assign a previously configured codec selection preference list (codec voice class) to a VoIP dial peer, enter the voice-class codec command in dial-peer configuration mode. To remove the codec preference assignment from the dial peer, use the no form of this command.

voice-class codec tag [ offer-all ]

no voice-class codec

### Syntax Description

tag

Unique number assigned to the voice class. The range is from 1 to 10000.

This tag number maps to the tag number created using the voice class codec command available in global configuration mode.

offer-all

(Optional) Adds all the configured codecs from the voice class codec to the outgoing offer from the Cisco Unified Border Element
                                          (Cisco UBE).

### Command Default

Dial peers have no codec voice class assigned.

### Command Modes

Dial-peer configuration (config-dial-peer)

## Command History

Release

Modification

12.0(2)XH

This command was introduced in Cisco IOS Release 12.0(2)XH and implemented on the Cisco AS5300 series routers.

12.0(7)T

This command was integrated into Cisco IOS Release 12.0(7)T and implemented on the Cisco 2600 series and the Cisco 3600 series.

12.0(7)XK

This command was integrated into Cisco IOS Release 12.0(7)XK and implemented on the Cisco MC3810.

15.1(2)T

This command was modified. The offer-all keyword was added.

Cisco IOS XE Release 2.5

This command was integrated into Cisco IOS XE Release 2.5.

Introduced support for YANG models.

### Usage Guidelines

You can assign one voice class to each VoIP dial peer. If you assign another voice class to a dial peer, the last voice class
                              assigned replaces the previous voice class.

The voice-class codec command in dial-peer configuration mode is entered with a hyphen. The voice class codec command in global configuration mode is entered without a hyphen.

## Examples

The following example shows how to assign a previously configured codec voice class to a dial peer:

```
Router# configure terminal Router(config)# dial-peer voice 100 voip Router(config-dial-peer)# voice-class codec 10 offer-all
```

### Related Commands

Command

Description

show dial-peer voice

Displays the configuration for all dial peers configured on the router.

test voice port detector

Defines the order of preference in which network dial peers select codecs.

voice class codec

Enters voice-class configuration mode and assigns an identification tag number for a codec voice class.

## voice-class h323 (dial peer)

To assign an H.323 voice class to a VoIP dial peer, use the voice-class h323 command in dial-peer configuration mode. To remove
                              the voice class from the dial peer, use the no form of this command.

voice-class h323 tag

no voice-class h323 tag

### Syntax Description

tag

Unique number to identify the voice class. Range is from 1 to 10000.

### Command Default

The dial peer does not use an H.323 voice class.

### Command Modes

Dial-peer configuration

## Command History

Release

Modification

12.1(2)T

This command was introduced.

### Usage Guidelines

The voice class that you assign to the dial peer must be configured using the voice class h323 in global configuration mode.

You can assign one voice class to each VoIP dial peer. If you assign another voice class to a dial peer, the last voice class
                              assigned replaces the previous voice class.

The voice-class h323 command in dial-peer configuration mode includes a hyphen and in global configuration mode does not include
                              a hyphen.

## Examples

The following example demonstrates how a voice class is created and applied to an individual dial peer. Voice class 4 contains
                              a command to disable the capability to detect Cisco CallManager systems in the network (this command is used by Cisco CallManager
                              Express 3.1 and later versions). The example then uses the voice-class h323 command to apply voice class 4 to dial peer 36.

```
Router(config)# voice class h323 4 Router(config-class)# no telephony-service ccm-compatible Router(config-class)# exit Router(config)# dial-peer voice 36 voip Router(config-dial-peer)# destination-pattern 555.... Router(config-dial-peer)# session target ipv4:10.5.6.7 Router(config-dial-peer)# voice-class h323 4
```

### Related Commands

Command

Description

show dial-peer voice

Displays the configuration for all dial peers configured on the router.

voice class h323

Enters voice-class configuration mode and assigns an identification tag number for an H.323 voice class.

## voice-class permanent (dial-peer)

To assign a previously configured voice class for a Cisco trunk or FRF.11 trunk to a network dial peer, use the voice-class permanent command in dial-peer configuration mode. To remove the voice-class assignment from the network dial peer, use the no form of this command.

voice-class permanent tag

no voice-class permanent tag

### Syntax Description

tag

Unique number assigned to the voice class. The tag number maps to the tag number created using the voice class permanent global configuration command. Range is from 1 to 10000.

### Command Default

Network dial peers have no voice class assigned.

### Command Modes

Dial-peer configuration

## Command History

Release

Modification

12.0(3)XG

This command was introduced on Cisco MC3810.

12.0(4)T

This command was integrated into Cisco IOS Release 12.0(4)T.

12.1(3)T

This command was implemented on Cisco 2600 series and Cisco 3600 series.

### Usage Guidelines

You can assign one voice class to any given network dial peer. If you assign another voice class to a dial peer, the last
                              voice class assigned replaces the previous voice class.

You cannot assign a voice class to a plain old telephone service (POTS) dial peer.

The voice-class permanent command in dial-peer configuration mode is entered with a hyphen. The voice class permanent command in global configuration mode is entered without a hyphen.

## Examples

The following example assigns a previously configured voice class to a Voice over Frame Relay (VoFR) network dial peer:

```
dial-peer voice 100 vofr
 voice-class permanent 10
```

### Related Commands

Command

Description

signal keepalive

Configures the keepalive signaling packet interval for Cisco trunks and FRF.11 trunks.

signal pattern

Configures the ABCD bit pattern for Cisco trunks and FRF.11 trunks.

signal timing idle suppress-voice

Configures the signal timing parameter for the idle state of a call.

signal timing oos

Configures the signal timing parameter for the OOS state of a call.

signal-type

Sets the signaling type for a network dial peer.

voice class permanent

Creates a voice class for a Cisco trunk or FRF.11 trunk.

## voice-class permanent (voice-port)

To assign a previously configured voice class for a Cisco trunk or FRF.11 trunk to a voice port, use the voice-class permanent command in voice-port configuration mode. To remove the voice-class assignment from the voice port, use the no form of this command.

voice-class permanent tag

no voice-class permanent tag

### Syntax Description

tag

Unique number assigned to the voice class. The tag number maps to the tag number created using the voice class permanent global configuration command. Range is 1 to 10000.

### Command Default

Voice ports have no voice class assigned.

### Command Modes

Voice-port configuration

## Command History

Release

Modification

12.0(3)XG

This command was introduced on Cisco MC3810.

12.0(4)T

This command was integrated into Cisco IOS Release 12.0(4)T.

12.1(3)T

This command was implemented as a voice-port configuration command on Cisco 2600 series and Cisco 3600 series routers.

### Usage Guidelines

You can assign one voice class to any given voice port. If you assign another voice class to a voice port, the last voice
                              class assigned replaces the previous voice class.

The voice-class permanent command in voice-port configuration mode is entered with a hyphen. The voice class permanent command in global configuration mode is entered without a hyphen.

## Examples

The following example assigns a previously configured voice class to voice port 1/1/0:

```
voice-port 1/1/0
 voice-class permanent 10
```

### Related Commands

Command

Description

signal keepalive

Configures the keepalive signaling packet interval for Cisco trunks and FRF.11 trunks.

signal pattern

Configures the ABCD bit pattern for Cisco trunks and FRF.11 trunks.

signal timing idle suppress-voice

Configures the signal timing parameter for the idle state of a call.

signal timing oos

Configures the signal timing parameter for the OOS state of a call.

signal-type

Sets the signaling type for a network dial peer.

voice class permanent

Creates a voice class for a Cisco trunk or FRF.11 trunk.

## voice-class sip anat

To enable Alternative Network Address Types (ANAT) on a Session Initiation Protocol (SIP) trunk, use the voice-class sip anat command in SIP configuration or dial peer configuration mode. To disable ANAT on SIP trunks, use the no form of this command.

voice-class sip anat [ system ]

no voice-class sip anat [ system ]

### Syntax Description

system

(Optional) Configures ANAT globally.

### Command Default

ANAT is enabled on SIP trunks.

### Command Modes

SIP configuration (conf-serv-sip) Dial peer configuration (config-dial-peer)

## Command History

Release

Modification

12.4(22)T

This command was introduced.

### Usage Guidelines

Both the Cisco IOS SIP gateway and Cisco Unified Border Element are required to support the Session Description Protocol (SDP)
                              ANAT semantics. The bind command allows the use of ANAT semantics in outbound SDP. SDP ANAT semantics are intended to address scenarios that involve
                              different network address families (for example, different IPv4 versions). Media lines grouped using ANAT semantics provide
                              alternative network addresses of different families for a single logical media stream. The entity creating a session description
                              with an ANAT group must be ready to receive or send media over any of the grouped "m" lines.

By default, ANAT is enabled on SIP trunks. However, if the SIP gateway is configured in IPv4-only mode or IPv6-only mode,
                              the gateway will not use ANAT semantics in its SDP offer.

The system keyword configures ANAT on all network dial peers, including the local dial peer. Using the voice-class sip anat command without the system keyword enables ANAT only for the local dial peer.

## Examples

The following example globally enables ANAT on a SIP trunk:

```
Router(config-serv-sip)# voice-class sip anat system
```

The following example enables ANAT on a specified dial peer:

```
Router(config-dial-peer)# voice-class sip anat
```

### Related Commands

Command

Description

bind

Binds the source address for signaling and media packets to the IPv4 or IPv6 address of a specific interface.

## voice-class sip asserted-id

To enable support for the dial-peer-based asserted ID header in incoming Session Initiation Protocol (SIP) requests or response
                              messages, and to send asserted ID privacy information in outgoing SIP requests or response messages, use the voice-class sip asserted-id command in dial-peer configuration mode. To disable the support for the asserted ID header, use the no form of this command.

voice-class sip asserted-id { pai | ppi | system }

no voice-class sip asserted-id

### Syntax Description

pai

(Optional) Enables the P-Asserted-Identity (PAI) privacy header in incoming and outgoing SIP requests or response messages.

ppi

(Optional) Enables the P-Preferred-Identity (PPI) privacy header in incoming SIP requests and outgoing SIP requests or response
                                          messages.

system

(Optional) Uses global-level configuration settings to configure the dial peer.

### Command Default

The privacy information is sent using the Remote-Party-ID (RPID) header or the FROM header.

### Command Modes

Dial-peer configuration (config-dial-peer)

## Command History

Release

Modification

15.1(1)T

This command was introduced.

15.1(3)T

This command was modified. Support for incoming calls was added.

### Usage Guidelines

If you choose the pai keyword or the ppi keyword for incoming messages, the gateway builds the PAI or the PPI header, respectively, into the common SIP stack, thereby
                              sending the call data using the PAI or the PPI header. For outgoing messages, the privacy information is sent on the PAI or
                              PPI header. The pai keyword or the ppi keyword has priority over the Remote-Party-ID (RPID) header, and removes the RPID/FROM header from the outbound message,
                              even if the router is configured to use the RPID header at the global level.

## Examples

The following example shows how to enable support for the PPI header:

```
Router> enable Router# configure terminal Router(config)# dial peer voice 1 Router(conf-voi-serv)# voice-class sip asserted-id ppi
```

### Related Commands

Command

Description

asserted-id

Enables support for the asserted ID header in incoming and outgoing SIP requests or response messages at the global level.

calling-info pstn-to-sip

Specifies calling information treatment for PSTN-to-SIP calls.

privacy

Sets privacy in support of RFC 3323.

## voice-class sip associate registered-number

To associate the preloaded route and outbound proxy details to the registered number in the dail peer configuration mode,
                              use the voice-class sip associate registered-number command in dial peer configuration mode. To remove the association, use the no form of this command.

voice-class sip associate registered-number number [ system ]

no voice-class sip associate registered-number

### Syntax Description

number

Registered number. The number must be between 4 and 32.

system

(Optional) Configures the association globally.

### Command Default

The preloaded route and outbound proxy details are not associated by default.

### Command Modes

Dial peer configuration (config-dial-peer)

## Command History

Release

Modification

15.1(2)T

This command was introduced.

### Usage Guidelines

The voice-class sip associate registered-number command takes precedence over the associate registered-number command in voice service VOIP SIP configuration mode. However, if the voice-class sip associate registered-number command is used with the system keyword, the gateway uses the settings configured globally by the associate registered-number command.

## Examples

The following example shows how to associate a registered number on dial peer.

```
Router> enable Router# configure terminal Router(config)# dial-peer voice 2611 voip Router(config-dial-peer)# voice-class sip associate registered-number 20
```

### Related Commands

Command

Description

associate registered-
                                                number

Associates the preloaded route and outbound proxy details with the registered number in voice service VoIP SIP configuration
                                          mode.

## voice-class sip asymmetric payload

To configure dynamic Session Initiation Protocol (SIP) asymmetric payload support on a dial peer, use the voice-class sip asymmetric payload command in dial peer configuration mode. To disable the configuration, use the no form of this command.

voice-class sip asymmetric payload { dtmf | dynamic-codecs | full | system }

no voice-class sip asymmetric payload

### Syntax Description

dtmf

Provides asymmetric support only for dual-tone multi-frequency (DTMF) payloads.

dynamic-codecs

Provides asymmetric support only for dynamic codec payloads.

full

Provides asymmetric support both for DTMF and dynamic codec payloads.

system

(Optional) Specifies that the asymmetric payload uses the global value.

### Command Default

Disabled (dynamic SIP asymmetric payload support is not enabled).

### Command Modes

Dial peer (config-dial-peer)

## Command History

Release

Modification

12.4(15)T

This command was introduced.

Cisco IOS XE
                                          Release 3.1S

This command was integrated into Cisco IOS Release IOS XE 3.1S

### Usage Guidelines

For the Cisco UBE the SIP asymmetric payload-type is supported for audio/video codecs, DTMF, and NSE. Hence, dtmf and dynamic-codecs keywords are internally mapped to the full keyword to provide asymmetric payload-type support for audio/video codecs , DTMF, and NSE.

## Examples

The following example shows how to configure dynamic SIP asymmetric payload support:

```
Router# configure terminal Router(config)# dial-peer voice 77 voip Router(config-dial-peer)# voice-class sip asymmetric payload full
```

### Related Commands

Command

Description

dial-peer voice

Defines a particular dial peer, specifies the method of voice encapsulation, and enters dial peer configuration mode.

## voice-class sip
                        	 audio forced

To allow only
                              		  audio and image (for T.38 Fax) media types, and drop all other media types
                              		  (such as video and application), use the voice-class sip audio forced command in dial-peer configuration
                              		  mode. To disable, use no form of this command.

voice-class sip audio forced [system]

no voice-class sip audio
                                 				  forced

### Syntax Description

system

(Optional) Uses the global configuration settings to allow only audio and image
                                          						(for T.38 Fax) media types.

### Command Default

Support for audio
                              		  forced at dial-peer level uses the global configuration level settings.

### Command Modes

Dial-peer configuration (config-dial-peer)

## Command History

Cisco IOS
                                       					 15.6(2)T

This
                                       					 command was introduced.

Cisco IOS XE Denali 16.3.1

This command was integrated into Cisco IOS XE Denali 16.3.1.

### Usage Guidelines

Use voice-class sip audio
                                    				forced command on the dial-peer when a particular remote end does
                              		  not support receiving any video or application m-lines in SDP.

## Examples

```
Router> enable
 Router# configure terminal
 Router(config)# dial-peer voice 1 voip
 Router(config-dial-peer)# voice-class sip audio forced
```

## voice-class sip authenticate redirecting-number

To supersede global settings and enable a dial peer on a Cisco IOS voice gateway to authenticate and pass Session Initiation
                              Protocol (SIP) credentials based on the redirecting number of forwarded calls, use the voice-class sip authenticate redirecting-number command in dial peer voice configuration mode. To supersede global settings and specify that a dial peer uses only the calling
                              number of forwarded calls, use the no form of this command. To return a dial peer to the default setting so that the dial peer uses the global setting, use the default form of this command.

voice-class sip authenticate redirecting-number [ system ]

no voice-class sip authenticate redirecting-number

default voice-class sip authenticate redirecting-number

### Syntax Description

system

(Optional) Specifies that the dial peer use whatever setting is configured at the global (voice service SIP) command level
                                          (default).

### Command Default

The dial peer uses the global setting. If the global setting is not specifically configured, the dial peer uses only the calling
                              number of a forwarded call for SIP credentials even when the redirecting number is available for that call.

### Command Modes

Dial peer voice configuration (config-dial-peer)

## Command History

Release

Modification

12.4(24)T

This command was introduced.

### Usage Guidelines

When an INVITE message sent out by the gateway is challenged, it must respond with the appropriate SIP credentials before
                              the call is established. The default global behavior for the gateway is to authenticate and pass SIP credentials based on
                              the calling number and all dial peers on a gateway default to the global setting. However, for forwarded calls, it is sometimes
                              more appropriate to use the redirecting number and this can be specified at either the global or dial peer level (configuring
                              behavior for a specific dial peer supersedes the global setting).

Use the voice-class sip authenticate redirecting-number command in dial peer voice configuration mode to supersede global settings and enable a dial peer to authenticate and pass
                              SIP credentials based on the redirecting number when available. Use the no form of this command to supersede global settings and force a dial peer to authenticate and pass SIP credentials based only
                              on the calling number of forwarded calls. Use the default form of this command to configure the dial peer to use the global setting.

The redirecting number is present only in the headers of forwarded calls. When the voice-class sip authenticate redirecting-number command is disabled or the redirecting number is not available, the dial peer passes SIP credentials that are based on the
                              calling number of the forwarded call. This is also the behavior on dial peers that are configured to use the global setting
                              and the global setting is disabled (default). To enable the global setting (which is used as the default setting for all dial
                              peers on the gateway), use the authenticate redirecting-number command in voice service SIP configuration mode.

## Examples

The following example shows how to enable dial peer 2 to authenticate and pass SIP credentials based on the redirecting number
                              (if available) of a forwarded call when a SIP INVITE message is challenged:

```
Router> enable Router# configure terminal Router(config)# dial-peer voice 2 voip Router(config-dial-peer)# voice-class sip authenticate redirecting-number
```

The following example shows how to force dial peer 2 to authenticate and pass only the calling number of a call even when
                              the global setting is enabled and a redirecting number is available for a call:

```
Router> enable Router# configure terminal Router(config)# dial-peer voice 2 voip Router(config-dial-peer)# no voice-class sip authenticate redirecting-number
```

The following two examples show different ways of setting dial peer 2 to the default setting so that it authenticates and
                              passes either the redirecting or calling number of a call based on the global (system) setting for the gateway:

```
Router> enable Router# configure terminal Router(config)# dial-peer voice 2 voip Router(config-dial-peer)# default voice-class sip authenticate redirecting-number Router> enable Router# configure terminal Router(config)# dial-peer voice 2 voip Router(config-dial-peer)# voice-class sip authenticate redirecting-number system
```

### Related Commands

Command

Description

authenticate redirecting-number

Enables a Cisco IOS voice gateway to authenticate and pass SIP credentials based on the redirecting number when available
                                          instead of the calling number of a forwarded call.

## voice-class sip bind

To bind the source address of a specific interface for a dial-peer on a Session Initiation Protocol (SIP) trunk, use the voice-class sip bind command in dial peer voice configuration mode. To disable bind at the dial-peer level or restore the bind to the global level,
                              use the no form of this command.

voice-class sip bind { control | media | all } source-interface interface-id [ ipv6-address ipv6-address ]

no voice-class sip bind { control | media | all }

### Syntax Description

control

Binds Session Initiation Protocol (SIP) signaling packets.

media

Binds only media packets.

all

Binds SIP signaling and media packets.

source interface interface-id

Specifies an interface as the source address of SIP packets.

ipv6-address ipv6-address

(Optional) Configures the IPv6 address of the interface.

### Command Default

Bind is disabled.

### Command Modes

Dial peer voice configuration (config-dial-peer)

## Command History

Release

Modification

15.1(2)T

This command was introduced.

Introduced support for YANG models.

### Usage Guidelines

Use the voice-class sip bind command in dial peer voice configuration mode to bind the source address for signaling and media packets to the IP address
                              of an interface on Cisco IOS voice gateway.

You can configure multiple IPv6 addresses for an interface and select one address using the ipv6-address keyword.

## Examples

The following example shows how to configure SIP bind command:

```
Router(config)# dial-peer voice 101 voip Router(config-dial-peer)# session protocol sipv2 Router(config-dial-peer)# voice-class sip bind control source-interface GigabitEthernet0/0 ipv6-address 2001:0DB8:0:1::1 Router(config-dial-peer)# voice-class sip bind media source-interface GigabitEthernet0/0 Router(config-dial-peer)# voice-class sip bind all source-interface GigabitEthernet0/0
```

## voice-class sip block

To configure an individual dial peer on a Cisco IOS voice gateway or Cisco Unified Border Element (Cisco UBE) to drop (not
                              pass) specific incoming Session Initiation Protocol (SIP) provisional response messages, use the voice-class sip block command in dial peer voice configuration mode. To disable a configuration to drop incoming SIP provisional response messages
                              on an individual dial peer, use the no form of this command.

voice-class sip block { 180 | 181 | 183 } [ sdp { absent | present } | system ]

no voice-class sip block { 180 | 181 | 183 }

### Syntax Description

180

Specifies that incoming SIP 180 Ringing messages should be dropped (not passed to the other leg).

181

Specifies that incoming SIP 181 Call is Being Forwarded messages should be dropped (not passed to the other leg).

183

Specifies that incoming SIP 183 Session in Progress messages should be dropped (not passed to the other leg).

sdp

(Optional) Specifies that either the presence or absence of Session Description Protocol (SDP) information in the received
                                          response determines when the dropping of specified incoming SIP messages takes place.

absent

Configures the SDP option so that specified incoming SIP messages are dropped only if SDP is absent from the received provisional
                                          response.

present

Configures the SDP option so that specified incoming SIP messages are dropped only if SDP is present in the received provisional
                                          response.

system

Configures the dial peer to use global configuration settings for dropping incoming SIP provisional response messages.

### Command Default

Defaults to the global configuration setting, which, when not specifically configured, means incoming SIP 180, 181, and 183
                              provisional responses are forwarded.

### Command Modes

Dial peer voice configuration (config-dial-peer)

## Command History

Release

Modification

12.4(22)YB

This command was introduced. Only SIP 180 and SIP 183 messages are supported on Cisco UBEs.

15.0(1)M

This command was integrated into Cisco IOS Release 15.0(1)M.

15.0(1)XA

This command was modified. Support was added for SIP 181 messages on the Cisco IOS SIP gateway, SIP-SIP Cisco UBEs, and the
                                          SIP trunk of Cisco Unified Communications Manager Express (Cisco Unified CME).

15.1(1)T

This command was integrated into Cisco IOS Release 15.1(1)T.

Cisco IOS XE Release 3.1S

This command was integrated into Cisco IOS XE Release 3.1S.

### Usage Guidelines

Use the voice-class sip block command in dial peer voice configuration mode to configure a specific dial peer on a Cisco IOS voice gateway or Cisco UBE
                              to override global settings and drop specified SIP provisional response messages. Additionally, you can use the sdp keyword to further control when the specified SIP message is dropped based on either the absence or presence of SDP information.

You can also use the system keyword to configure a specific dial peer to use global configuration settings for dropping incoming SIP provisional response
                              messages. To configure global settings on a Cisco IOS voice gateway or Cisco UBE, use the block command in voice service SIP configuration mode. To disable configurations for dropping specified incoming SIP messages on
                              an individual dial peer, use the no voice-class sip block command in dial peer voice configuration mode.

This command is supported only on outbound dial peers--it is nonoperational if configured on inbound dial peers. You should
                                          configure this command on the outbound SIP leg that sends out the initial INVITE message. Additionally, this feature applies
                                          only to SIP-to-SIP calls and will have no effect on H.323-to-SIP calls.

## Examples

The following example shows how to configure dial peer 1 to override any global configurations and drop specified incoming
                              SIP provisional response messages regardless whether SDP is present:

```
Router> enable Router# configure terminal Router(config)# dial-peer voice 1 voip Router(config-dial-peer)# voice-class sip block 181
```

The following example shows how to configure dial peer 1 to override any global configurations and drop specified incoming
                              SIP provisional response messages only if SDP is present:

```
Router> enable Router# configure terminal Router(config)# dial-peer voice 1 voip Router(config-dial-peer)# voice-class sip block 183 sdp present
```

The following example shows how to configure dial peer 1 to override any global configurations and drop incoming SIP provisional
                              response messages only when SDP is not present:

```
Router> enable Router# configure terminal Router(config)# dial-peer voice 1 voip Router(config-dial-peer)# voice-class sip block 180 sdp absent
```

The following example shows how to configure a dial peer to use the global configuration settings for dropping incoming SIP
                              provisional response messages:

```
Router> enable Router# configure terminal Router(config)# dial-peer voice 1 voip Router(config-dial-peer)# voice-class sip block 181 system
```

The following example shows how to configure a dial peer to pass all incoming SIP provisional response messages regardless
                              of global configuration settings:

```
Router> enable Router# configure terminal Router(config)# dial-peer voice 1 voip Router(config-dial-peer)# no voice-class sip block 180
```

### Related Commands

Command

Description

block

Configures global configuration for dropping specified SIP provisional response messages on a Cisco IOS voice gateway or Cisco
                                          UBE.

map resp-code

Configures global settings on a Cisco UBE for mapping specific incoming SIP provisional response messages to a different SIP
                                          response message.

voice-class sip map resp-code

Configures a specific dial peer on a Cisco UBE to map specific incoming SIP provisional response messages to a different SIP
                                          response message.

## voice-class sip call-route

To enable call routing based on the Destination-Route-String, P-called-party-id and History-Info header values at the dial-peer
                              configuration level, use the voice-class sip call-route command in dial peer voice configuration mode. To disable Header-based routing, use the no form of this command.

voice-class sip call-route { dest-route-string | p-called-party-id | history-info | url } [ system ]

no voice-class sip call-route { dest-route-string | p-called-party-id | history-info | url }

### Syntax Description

dest-route-string

Enables call routing based on the Destination-Route-String.

p-called-party-id

Enables call routing based on the P-Called-Party-Id header.

history-info

Enables call routing based on the History-Info header.

url

Enables call routing based on the URL.

system

(Optional) Uses the global configuration settings to enable call routing based on the header values on this dial peer.

### Command Default

Support for call routing based on the Destination-Route-String, P-Called-Party-Id, History-Info headers and URL at the dial
                              peer level is disabled.

### Command Modes

Dial peer voice configuration (config-dial-peer)

## Command History

Release

Modification

12.4(22)YB

This command was introduced.

15.0(1)M

This command was integrated into Cisco IOS Release 15.0(1)M.

15.1(2)T

This command was modified. The history-info keyword was added.

15.2(1)T

This command was modified. The url keyword was added.

15.3(3)M

This command was modified. The dest-route-string keyword was added.

Cisco IOS XE Release 3.10S

This command was integrated into Cisco IOS XE Release 3.10S.

### Usage Guidelines

Use the voice-class sip call-route command on the inbound dial peer to enable the gateway to route calls based on the received header in a received INVITE message.

The voice-class sip call-route command takes precedence over the call-route command in voice service VoIP SIP configuration mode. However, if the voice-class sip call-route command is used with the system keyword, the gateway uses the settings configured globally by the call-route command.

If multiple call routes are configured, call routing enabled based on destination route string takes precedence over other
                              header configurations. Destination route string configuration is applicable only for outbound dial-peer matching.

## Examples

The following example shows how to enable call routing based on the Destination-Route-String, P-Called-Party-Id, History-Info
                              header values and URL at the dial peer configuration level:

```
Device> enable Device# configure terminal Device(config)# dial-peer voice 2611 voip Device(config-dial-peer)# voice-class sip call-route dest-route-string Device(config-dial-peer)# voice-class sip call-route p-called-party-id Device(config-dial-peer)# voice-class sip call-route history-info Device(config-dial-peer)# voice-class sip call-route url
```

### Related Commands

Command

Description

call-route

Enables call routing based on the Destination-Route-String, P-Called-Party-Id and History-Info header values at the global
                                          configuration level.

## voice-class sip calltype-video

To configure the bearer capability setting on an H.320 dial peer so that it supports unrestricted digital media, use the voice-class sip calltype-video command in dial peer voice configuration mode. To return the bearer capability setting for an H.320 dial peer to the default,
                              use the no form of this command.

voice-class sip calltype-video

no voice-class sip calltype-video

### Syntax Description

This command has no arguments or keywords.

### Command Default

Bearer capability setting for support of unrestricted digital media support is disabled.

### Command Modes

Dial peer voice configuration (config-dial-peer)

## Command History

Release

Modification

12.4(24)T

This command was introduced.

### Usage Guidelines

H.320 dial peers support only voice calls by default. Use the voice-class sip calltype-video command to configure the bearer capability setting, which enables support of unrestricted digital media calls on an H.320
                              dial peer.

## Examples

The following example shows how to configure the bearer capability setting on dial peer 2 so that it supports unrestricted
                              digital media:

```
Router> enable Router# configure terminal Router(config)# dial-peer voice 2 voip Router(config-dial-peer)# voice-class sip call-type video
```

## voice-class sip content sdp version increment

To increment the SDP version for any RE-INVITE with SDP change even if the previous offer sent by CUBE was rejected, use voice-class sip content sdp version increment command in dial-peer configuration mode.

voice-class sip content sdp version increment { system }

system

Uses the system level configuration for sdp version increment

### Command Default

SDP version will not be incremented for any RE-INVITE with SDP change even if the previous offer sent by CUBE was rejected.

### Command Modes

dial-peer configuration mode (config-dial-peer)

## Command History

Cisco IOS 15.5(2)T

Cisco IOS XE 3.15

This command was introduced.

### Usage Guidelines

Use voice-class sip content sdp version increment command to increment the SDP version for any RE-INVITE with SDP change even if the previous offer sent by CUBE was rejected.

## Examples

```
Device> enable Device# configure terminal Device(config)# dial-peer voice 1 voip Device(config-dial-peer)# voice-class sip content sdp version increment
```

## voice-class sip copy-list

To configure a list of entities to be sent to the peer call leg on a dial peer, use the voice-class sip copy-list command in dial peer configuration mode. To disable the configuration, use the no form of this command.

voice-class sip copy-list { tag | system }

no voice-class sip copy-list

### Syntax Description

tag

Tag number of the Session Initiation Protocol (SIP) copy list. The range is from 1 to 10000.

system

Specifies to use the global level configuration to copy the list.

### Command Default

Entries configured at the global level are sent to the peer call leg.

### Command Modes

Dial peer configuration (config-dial-peer)

Voice class tenant

## Command History

Release

Modification

15.1(3)T

This command was introduced.

Cisco IOS XE Cupertino 17.7.1a

Introduced support for YANG models.

### Usage Guidelines

Use the voice-class sip copy-list command to configure Cisco Unified Border Element (UBE) to pass an unsupported parameter present in a mandatory header from
                              one peer call leg to another. You can copy the inbound message headers into variables and pass the headers to the outbound
                              peer call leg.

## Examples

The following example shows how to configure a SIP list to be sent to the peer call leg:

```
Router(config)# dial-peer voice 66 voip Router(config-dial-peer)# voice-class sip copy-list 4
```

### Related Commands

Command

Description

voice class sip-copylist

Configures a list of entities to be sent to the peer call leg.

## voice-class sip e911

To enable SIP E911 system services on a dial peer, use the voice-class sip e911 command in VoIP dialpeer configuration mode. To disable SIP E911 services, use the no form of this command.

voice-class sip e911

no voice-class sip e911

### Syntax Description

This command has no arguments or keywords.

### Command Default

The dial peer uses the global setting.

### Command Modes

VoIP dialpeer configuration mode.

## Command History

Release

Modification

12.4(9)T

This command was introduced.

### Usage Guidelines

The no form of this command sets the dial peer configuration to disable, which indicates that E911 will not be used for this peer.
                              Because the no version of the command causes non default behavior, it can been seen in the show running-config output. See also the voice service voip sip e911 and debug csm neat commands.

## Examples

The following examples enable and disable E911 services on a VoIP dial peer:

```
Router(config)# dial-peer voice 2 Router(config-dial-peer)# voice-class sip e911 *Jun 06 00:47:20.611: setting peer 2 to enable
Router(config-dial-peer)# no voice-class sip e911 *Jun 06 00:49:58.931: setting peer 2 to disable
```

### Related Commands

Command

Description

debug csm neat

Turns on debugging for all Call Switching Module (CSM) Voice over IP (VoIP) calls.

show running-config

Displays the running configuration.

e911

Enables E911 system services for SIP voice service VoIP.

## voice-class sip-event-list

To configure lists of SIP events to be passed through. To disable this feature, use the no form of this command.

voice-class sip-event-list tag

no voice-class sip-event-list tag

### Syntax Description

tag

Event list tag. Range is 1-10000.

### Command Default

No default value.

### Command Modes

Global configuration (config).

Voice class tenant configuration (config-class).

## Command History

Release

Modification

Cisco IOS XE 3.11S

Cisco IOS XE Cupertino 17.7.1a

Introduced support for YANG models.

### Usage Guidelines

Use this command for troubleshooting to determine which SIP event was configured as passed through. To set the sip event,
                              use the voice class sip-event-list command.

To set the voice class sip-event-list in the dial peer, use the voice-class sip pass-thru subscribe-notify-events <event id | all> command.

To set the voice class sip-event-list in the voice service VoIP under sip, use the pass-thru subscribe-notify-events <event id | all> command.

To set the voice class sip-event-list in the voice class tenant, use the pass-thru subscribe-notify-events <event id | all> command.

## Examples

```
Router#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#voice class sip-event-list 12
Router(config-class)#event ?
  WORD  name of event to be added in event list
Router(config-class)#event sipevent1
Router(config-class)#event sipevent2
```

### Related Commands

Command

Description

## voice-class sip
                        	 early-media update block

To block the
                              		  UPDATE requests with SDP in an early dialog, use voice-class sip early-media
                                    				update block command in dial-peer configuration mode. To disable,
                              		  use no form of
                              		  this command.

voice-class sip early-media update block [ re-negotiate ]

no voice-class sip early-media update block [ re-negotiate ]

## Syntax Description

Enables
                                       					 end to end renegotiation if the UPDATE request contains changes in caller ID,
                                       					 transcoder addition or deletion, or video escalation or de-escalation.

### Command Default

CUBE allows
                              		  pass-through of early dialog UPDATE requests from one user agent to the other.

### Command Modes

Dial peer configuration (config-dial-peer)

## Command History

This
                                       					 command was introduced.

### Usage Guidelines

Use voice-class sip early-media update block command on the dial-peer where you want to block the Early Dialog UPDATE
                              		  requests.

Use re-negotiate keyword to enable end to end renegotiation if the UPDATE request contains
                              		  changes in caller ID, transcoder addition or deletion, or video escalation or
                              		  de-escalation.

## Examples

The following
                              		  example shows early dialog update block being configured in dial-peer
                              		  configuration mode:

```
Router(config-dial-peer)# voice-class sip early-media update block
```

## voice-class sip encap clear-channel

To enable RFC 4040-based clear-channel codec negotiation for Session Initiation Protocol (SIP) calls on an individual dial
                              peer, overriding the global setting on a Cisco IOS voice gateway or Cisco Unified Border Element (Cisco UBE), use the voice-class sip encap clear-channel command in dial peer voice configuration mode. To disable RFC 4040-based clear-channel codec negotiation on an individual
                              dial peer for SIP calls on a Cisco IOS voice gateway or Cisco UBE, use the no form of this command.

voice-class sip encap clear-channel [ standard | system ]

no voice-class sip encap clear-channel standard

### Syntax Description

standard

(Optional) Specifies standard RFC 4040 encapsulation.

system

(Optional) Configures the dial peer to use global configuration settings for clear-channel codec negotiation.

### Command Default

The dial peer uses the system configuration. (If the global encap clear-channel standard command is not enabled, then legacy encapsulation [X-CCD/8000] is used for clear-channel codec negotiation.)

### Command Modes

Dial peer voice configuration (config-dial-peer)

## Command History

Release

Modification

15.0(1)XA

This command was introduced.

15.1(1)T

This command was integrated into Cisco IOS Release 15.1(1)T.

### Usage Guidelines

Use the voice-class sip encap clear-channel standard command in dial peer voice configuration mode to override global settings for clear-channel codec negotiation on a Cisco
                              IOS voice gateway or Cisco UBE and enable RFC 4040-based clear-channel codec negotiation [CLEARMODE/8000] for SIP calls on
                              a specific dial peer. RFC 4040-based clear-channel codec negotiation allows dial peers on Cisco IOS voice gateways and Cisco
                              UBEs to successfully interoperate with third-party SIP gateways that do not support legacy Cisco IOS clear-channel codec encapsulation
                              [X-CCD/8000].

When the voice-class sip encap clear-channel standard command is enabled on a specific dial peer on a Cisco IOS voice gateway or Cisco UBE, SIP calls on that dial peer that use
                              the Cisco IOS clear channel codec are translated into calls that use [CLEARMODE/8000] regardless of the global configuration
                              so that the calls do not get rejected when they reach third-party SIP gateways.

You can also use the voice-class sip encap clear-channel system command to configure a specific dial peer to use global configuration settings for clear-channel codec negotiation. To enable
                              RFC 4040 clear-channel codec negotiation for SIP calls globally on a Cisco IOS voice gateway or Cisco UBE, use the encap clear-channel standard command in voice service SIP configuration mode. To override global settings and disable RFC 4040-based clear-channel codec
                              negotiation on a specific dial peer, use the no voice-class sip encap clear-channel standard command in dial peer voice configuration mode.

## Examples

The following example shows how to configure dial peer 1 to override any global configurations and enable RFC 4040-based clear-channel
                              codec negotiation for SIP calls:

```
Router> enable Router# configure terminal Router(config)# dial-peer voice 1 voip Router(config-dial-peer)# voice-class sip encap clear-channel standard
```

The following example shows how to configure dial peer 1 to use the global configuration for clear-channel codec negotiation
                              for SIP calls:

```
Router> enable Router# configure terminal Router(config)# dial-peer voice 1 voip Router(config-dial-peer)# voice-class sip encap clear-channel system
```

### Related Commands

Command

Description

encap clear-channel standard

Enables RFC 4040-based clear-channel codec negotiation for SIP calls globally on a Cisco IOS voice gateway or Cisco UBE.

| aggressive | Reduces noise threshold from -78 to -62 dBm. Available only when session protocol multicast is configured. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(1)T | This command was introduced on the Cisco 3600 series. |
| 12.0(4)T | This command was implemented as a dial-peer command on Cisco MC3810 (in prior releases, the vad command was available only as a voice-port command). |
| 12.2(11)T | The aggressive keyword was added. |
| Cisco IOS XE Bengaluru 17.6.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| comfort-noise | Generates background noise to fill silent gaps during calls if VAD is activated. |
| dial-peer voice | Enters dial-peer configuration mode, defines the type of dial peer, and defines the tag number associated with a dial peer. |
| vad (voice-port) | Enables VAD for the calls using a particular voice port. |

| on | Enables the local vad settings irrespective of the external vad settings. |
|---|---|
| off | Disables the local vad settins irrespective of the external vad settings. |
| override | Overrides the external vad settings with local vad configuration details. |

| Release | Modification |
|---|---|
| Cisco IOS XE 
                                          Release 3.2S | This command was introduced. |

| Command | Description |
|---|---|
| dsp services dspfarm | Enables the DSP-farm services. |
| dspfarm profile | Enters the DSP farm profile configuration mode, and defines a profile for the DSP farm services. |
| show dspfarm (SPA-DSP) | Displays DSP farm service information, such as operational status and DSP resource allocation for transcoding. |

| maximum | Sets the maximum playout buffer delay, in milliseconds (ms). Range: 40 to 1000. Default: 1000. |
|---|---|
| milliseconds | Delay time, in milliseconds (ms). |
| minimum | Sets the minimum playout buffer delay, in ms. Range: 10 to 40. Default: 40. |
| mode | Configures voice-band-detection playout buffer adaptation mode. |
| fixed | Sets the jitter buffer to a constant delay. |
| no-timestamps | (Optional) Fixes the jitter buffer at a constant delay without time stamps. |
| passthrough | Sets the jitter buffer passthrough mode for clock compensation. |
| nominal | Sets the nominal playout buffer delay, in ms. Range:10 to 1000. Default: 60. |

| Release | Modification |
|---|---|
| 12.2(8)T | This command was introduced. |
| 12.4(24)T | This command was modified. The minimum time range value was changed from 4 to 1700 ms to a range of 10  to 40 ms. The default value 4 was increased to
                                                40 ms. The maximum time value was decreased from 1700 to 1000 ms and the default of 200 was increased to 1000 ms. The nominal time range value was changed from 0 to 1500 ms to a range of 10 to 1000 ms. The default value of 100 was decreased
                                                to 60 ms. |
| 12.4(24)T6 | This command was modified. The no-timestamps keyword was added and passthrough keyword usage guidelines were clarified. |

| Note | The passthough keyword is a special mode used to handle clock drifting properly. We recommend this keyword only when instructed by your
                                          Cisco representative. |
|---|---|

| Command | Description |
|---|---|
| voice-service | Specifies the voice encapsulation type and enters voice service configuration mode. |

| peak-rate | Peak information rate (PIR) for the voice connection, in kilobytes per second (kbps). If it does not exceed your carrier’s
                                          line rate, set it to the line rate. Range is from 56 to 10000. |
|---|---|
| average-rate | Average information rate (AIR) for the voice connection, in kbps. |
| burst | Burst size, in number of cells. Range is from 0 to 65536. |

| Release | Modification |
|---|---|
| 12.0 | This command was introduced on the Cisco MC3810. |
| 12.1(5)XM | This command was implemented on Cisco 3600 series routers and modified to support Simple Gateway Control Protocol (SGCP)
                                          and Media Gateway Control Protocol (MGCP). |
| 12.2(2)T | This command was integrated into Cisco IOS Release 12.2(2)T. |
| 12.2(11)T | This command was implemented on the Cisco AS5300 and Cisco AS5850. |
| Cisco IOS XE Release 2.3 | This command was made available in ATM PVP configuration mode. |

| Command | Description |
|---|---|
| encapsulation aal5 | Configures the AAL and encapsulation type for an ATM PVC, SVC, or VC class. |

| pvc-identifier | Identifier for the PVC. Range is from 0 to 32767. There is no default value. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(5)XM | This command was introduced. |
| 12.2(2)T | This command was integrated into Cisco IOS Release 12.2(2)T. |
| 12.2(11)T | This command was implemented on the Cisco AS5300 and Cisco AS5850. |

| Command | Description |
|---|---|
| mgcp | Starts the MGCP daemon. |
| pvc | Creates an ATM PVC for voice traffic. |

| h261 | Video Codec H.261 |
|---|---|
| h263 | Video Codec H.263 |
| h263+ | Video Codec H.263+ |
| h264 | Video Codec H.264 |
| mpeg4 | Video Codec MPEG-4 ISO/ISE 14496-2 |
| scip | Video Codec SCIP (This feature is available in 'preview' mode) |

| Release | Modification |
|---|---|
| 12.4(11)T | This command was introduced. |
| Cisco IOS XE 17.16.1a | This command was modified to include SCIP video codec type. Note This feature is available in 'preview' mode as it includes limited functionality or incomplete software dependencies. | Note | This feature is available in 'preview' mode as it includes limited functionality or incomplete software dependencies. |
| Note | This feature is available in 'preview' mode as it includes limited functionality or incomplete software dependencies. |

| Note | This feature is available in 'preview' mode as it includes limited functionality or incomplete software dependencies. |
|---|---|

| Command | Description |
|---|---|
| video codec (voice-class) | Specifies a video codec for a voice class. |

| h261 | Apply this preference to video codec H.261 |
|---|---|
| h263 | Apply this preference to video codec H.263 |
| h263+ | Apply this preference to video codec H.263+ |
| h264 | Apply this preference to video codec H.264 |
| mpeg4 | Video Codec MPEG-4 ISO/IES 14496-2 |
| scip | Video Codec SCIP (This feature is available in 'preview' mode) |

| Release | Modification |
|---|---|
| 12.4(11)T | This command was introduced. |
| Cisco IOS XE Dublin
                                                17.10.1a | Introduced support for YANG models. |
| Cisco IOS XE 17.16.1a | This command was modified to support SCIP video codec type. Note This feature is available in 'preview' mode as it includes limited functionality or incomplete software dependencies. | Note | This feature is available in 'preview' mode as it includes limited functionality or incomplete software dependencies. |
| Note | This feature is available in 'preview' mode as it includes limited functionality or incomplete software dependencies. |

| Note | This feature is available in 'preview' mode as it includes limited functionality or incomplete software dependencies. |
|---|---|

| Command | Description |
|---|---|
| video codec (dial peer) | Specifies a video codec for a VoIP dial peer. |

| system | Specifies
                                          						that transcoding and transsizing use the global sip-ua value. This keyword is
                                          						available only for the tenant mode to allow it to fallback to the global
                                          						configurations. |
|---|---|

| Release | Modification |
|---|---|
| 15.1(4)M | The
                                          						command was introduced. |
| 15.6(2)T
                                          						and IOS XE Denali 16.3.1 | This
                                          						command was modified to include the keyword: system . This
                                          						command is now available under voice class tenants. |

| Command | Description |
|---|---|
| codec profile | Defines
                                          						the video capabilities needed for video endpoints. |
| video codec | Assigns a
                                          						video codec to a VoIP dial peer. |

| number | Number of violations after which the required action needs to be taken. The range is from 1 to 200000. The default value
                                          is 20. |
|---|---|
| action | Specifies that an action must be performed after the specified number of violations. |
| disconnect | Disconnects the call after the specified number of violations is exceeded. |
| ignore | Specifies that no action should be taken after the specified number of violations is exceeded. |
| no-syslog | (Optional) Specifies not to print messages to the system log when violations occur. |

| Release | Modification |
|---|---|
| 15.2(2)T | This command was introduced. |

| Command | Description |
|---|---|
| dscp media | Specifies the RPH to DSCP mapping. |
| voice class dscp-profile | Configures the DSCP profile. |

| number | Number of violations after which the required action needs to be taken. The range is from 1 to 200000. The default value
                                          is 20. |
|---|---|
| action | Specifies that an action must be performed after the specified number of violations. |
| disconnect | Disconnects the call after the specified number of violations is exceeded. |
| drop | Drops the call after the specified number of violations is exceeded. |
| ignore | Specifies that no action should be taken after the specified number of violations is exceeded. |
| no-syslog | (Optional) Specifies not to print messages to the system log when violations occur. |

| Release | Modification |
|---|---|
| 15.2(2)T | This command was introduced. |

| Command | Description |
|---|---|
| media profile police | Configures the media policing profile. |
| overhead | Configures the overhead bandwidth percentage above the negotiated bandwidth. |

| dc-voltage | DC voltage VMWI is enabled on this FXS port. |
|---|---|
| fsk | FSK VMWI is enabled on this FXS port. Default. |

| Release | Modification |
|---|---|
| 12.4(20)YA | This command was introduced. |
| 12.4(22)T | This command was integrated into Cisco IOS Release 12.4(22)T. |

| Command | Description |
|---|---|
| stcapp | Enables basic SCCP call-control features for FXS analog ports on Cisco IOS voice gateways |

| data | (Required for Cisco-trunk permanent calls. Optional for switched calls.) Selects a subchannel (CID) for data other than the
                                          default subchannel, which is 4. |
|---|---|
| cid | (Optional) Specifies the subchannel to be used for data. Range is from 4 to 255. The default is 4. If data is specified, enter a valid CID. |
| call-control | (Optional) Reserves a subchannel for call-control signaling. |
| cisco | (Optional) Cisco proprietary voice encapsulation for VoFR with data is carried on CID 4 and call-control on CID 5. |
| cid | (Optional) Specifies the subchannel to be used for call-control signaling. Valid range is from 4 to 255. The default is 5.
                                          If call-control is specified and a CID is not entered, the default CID is used. |

| Release | Modification |
|---|---|
| 12.0(3)XG | This command was introduced on Cisco 2600 series, Cisco 3600 series, and Cisco 7200 series routers and Cisco MC3810. |
| 12.0(4)T | This command was integrated into Cisco IOS Release 12.0(4)T. |
| 12.0(7)XK | The use of the cisco option was modified. Beginning in this release, use the cisco option only when configuring connections to Cisco MC3810 running Cisco IOS Releases before 12.0(7)XK and 12.1(2)T. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T. |

| Type of Call | Command Combination to Use |
|---|---|
| Switched call (user dialed or auto-ringdown) to other routers supporting VoFR | vofr [ data cid ] [ call-control [ cid ]] 1 |
| Cisco-trunk permanent call (private-line) to other routers supporting VoFR | vofr data cid call-control cid |
| FRF.11 trunk call (private-line) to other routers supporting VoFR | vofr [ data cid ] [ call-control cid ] 2 |

| Command | Description |
|---|---|
| class | Assigns a VC class to a PVC. |
| frame-relay interface-dlci | Assigns a DLCI to a specified Frame Relay subinterface. |

| Release | Modification |
|---|---|
| 12.2(2)XA | This command was introduced on the Cisco AS5350 and AS5400. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850 platform. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T. |

| Command | Description |
|---|---|
| resource-pool enable | Enables resource pool management. |
| resource-pool profile service voip | Defines the VoIP service profile for resource pool management. |

| name | Designates which voicecaps to use on this voice port. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Command | Description |
|---|---|
| voicecap entry | Creates a voicecap on NextPort platforms. |

| name string | (Optional) A word and a string of characters that uniquely identify a voicecap. The name argument specifies a unique identifier for a voicecap. The string argument specifies one or more voicecap register entries, similar to a modemcap. Each entry is of the form v index = value , where index refers to a specific V register, and value designates the value for that V register. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |
| 12.3(11)T | This command was integrated into Cisco IOS Release 12.3(11)T. |
| 12.4(4)XC | This command was modified to include GSMAMR-NB codec capability. |
| 12.4(9)T | This command was integrated into Cisco IOS Release 12.4(9)T. |

| V-Reg # | Default | Description | Register Values and Additional Notes |
|---|---|---|---|
| 0 | 0 | Sets how Adaptive Multi-Rate (AMR) responds to an incoming codec mode request (CMR) that is not a member of the mode set. | 0 = Drop the packet with the bad CMR. 1 = Ignore the CMR (do not change rates) but process the rest of the packet data normally.
                                          2 = Change the rate to the highest rate in the mode set lower than the rate requested by the CMR. |
| 1 | 0 | Sets how AMR handles packets with a frame type (AMR rate) that is not a member of the mode set. | 0 = Drop the packet with the bad frame-type. 1 = Attempt to decode the packet. |

| Command | Description |
|---|---|
| voicecap configure | Applies a voicecap to the specified voice ports. |

| carrier | Carrier code address family |
|---|---|
| trunk-group | Trunk group address family |
| prefix | E.164 prefix |
| value | Minimum interval, in seconds, with a range of 1 to 3600 seconds and a default of 10. This value cannot be set higher than
                                          the time configured for the capacity update interval. |

| Release | Modification |
|---|---|
| 12.3(1) | This command was introduced. |

| Command | Description |
|---|---|
| capacity update interval (dial peer) | Changes the capacity update for prefixes associated with a dial peer. |
| capacity update interval (trunk group) | Change the capacity update for carriers or trunk groups. |
| voice call capacity stw | Set the value for STW. |

| carrier | Carrier code address family. |
|---|---|
| trunk-group | Trunk group address family. |
| prefix | E.164 prefix. |
| maxima | Maxima (first derivative) point in available capacity. |
| inflection | Inflection (second derivative) point in available capacity. |

| Release | Modification |
|---|---|
| 12.3(1) | This command was introduced. |

| Command | Description |
|---|---|
| voice call capacity mir | Sets the values for the minimum interval between reporting
                                          						(MIR) and smoothing transition time for weight (STW). |
| voice call capacity timer interval | Sets the periodic interval for reporting capacity from
                                          						carrier, trunk group, or prefix databases |
| voice call trigger hwm | Sets the value for percentage change, low water mark and
                                          						high water mark in the available capacity in the trunk group or prefix
                                          						databases. |

| carrier | Carrier code address family |
|---|---|
| trunk-group | Trunk group address family |
| prefix | E.164 prefix |
| seconds | Transitions time can be from 0 to 60 seconds with a default of 10. |

| Release | Modification |
|---|---|
| 12.3(1) | This command was introduced. |

| Command | Description |
|---|---|
| capacity update interval (dial peer) | Changes the capacity update for prefixes associated with a dial peer. |
| capacity update interval (trunk group) | Change the capacity update for carriers or trunk groups. |
| voice call capacity mir | Set the value for MIR. |

| carrier | Carrier code address family |
|---|---|
| trunk-group | Trunk group address family |
| prefix | E.164 prefix |
| seconds | Value from 10 to 3600 seconds. |

| Release | Modification |
|---|---|
| 12.3(1) | This command was introduced. |

| Command | Description |
|---|---|
| voice call capacity mir | Sets the values for the MIR and STW. |
| voice call capacity reporting | Turns on the reporting of maxima (first derivative) or inflection (second derivative) points in available capacity. |
| voice call trigger hwm | Sets the value for percentage change, low water mark and high water mark in the available capacity in the trunk group or prefix
                                          databases. |

| tunnel-IEs | (Optional) Information elements (IEs) are carried in the progress message. |
|---|---|
| always | (Optional) Converts disconnect message with a PI to a progress message in both preconnected and connected states. |

| Release | Modification |
|---|---|
| 12.2(1) | This command was introduced. |
| 12.3(6) | The tunnel-1Es keyword was added. |
| 12.3(4)XQ | The always keyword with the tunnel-IEs keyword were added. |
| 12.3(8)T | The always keyword with the tunnel-IEs keyword were added. |
| 12.3(9) | The always keyword with the tunnel-1Es keyword were added. |

| Command | Description |
|---|---|
| disc_pi_off | Enables an H.323 gateway to disconnect a call when it receives a disconnect message with a PI. |

| carrier | Carrier code address family |
|---|---|
| trunk-group | Trunk group address family |
| prefix | E.164 prefix |
| value | Value from 10 to 50 data points. Default is 30 data points. |

| Release | Modification |
|---|---|
| 12.3(1) | This command was introduced. |

| Command | Description |
|---|---|
| voice call csr recording interval | Sets the recording interval for the CSR. |
| voice call csr reporting interval | Sets the reporting interval for the CSR. |

| carrier | Carrier code address family. |
|---|---|
| trunk-group | Trunk group address family. |
| prefix | E.164 prefix. |
| minutes | Value from 10 to 1000 minutes with a default of 60. |

| Release | Modification |
|---|---|
| 12.3(1) | This command was introduced. |

| Command | Description |
|---|---|
| voice call csr data-points | Sets the number of call success rate (CSR) data points. |
| voice call csr reporting interval | Sets the reporting interval for CSR. |

| carrier | Carrier code address family. |
|---|---|
| trunk-group | Trunk group address family. |
| prefix | E.164 prefix. |
| seconds | Value from 10 to 10000 seconds with a default of 25. |

| Release | Modification |
|---|---|
| 12.3(1) | This command was introduced. |

| Command | Description |
|---|---|
| voice call csr data-points | Sets the number of CSR data points. |
| voice call csr recording interval | Sets the recording interval for CSR. |

| full-guid | Displays the GUID in a 16-byte header. Note When the no version of this command is input with the full-guid keyword, the short 6-byte version displays. This is the default. | Note | When the no version of this command is input with the full-guid keyword, the short 6-byte version displays. This is the default. |
|---|---|---|---|
| Note | When the no version of this command is input with the full-guid keyword, the short 6-byte version displays. This is the default. |
| short-header | Displays the CallEntry ID in the header without displaying the GUID or module-specific parameters. |

| Note | When the no version of this command is input with the full-guid keyword, the short 6-byte version displays. This is the default. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(11)T | The new debug header was added to the following platforms: Cisco 2600 series, Cisco 3620, Cisco 3640, Cisco 3660 series,
                                          Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5800, Cisco AS5850, and Cisco MC3810. |
| 12.2(15)T | The header-only keyword was replaced by the short-header keyword. |

| Note | Using the no form of this command does not turn off debugging. |
|---|---|

| Note | The "//-1/" output indicates that CallEntryID for the CCAPI module is not available. |
|---|---|

| Field | Description |
|---|---|
| VTSP:(0:D):0:0:4385 | VTSP module, port name, channel number, DSP slot, and DSP channel number. |
| vtsp_insert_cdb | Function name. |
| CCAPI | CCAPI module. |

| Note | The "//-1/" output indicates that CallEntryID for CCAPI is not available. |
|---|---|

| Command | Description |
|---|---|
| debug rtsp api | Displays debug output for the RTSP client API. |
| debug rtsp client session | Displays debug output for the RTSP client data. |
| debug rtsp error | Displays error message for RTSP data. |
| debug rtsp pmh | Displays debug messages for the PMH. |
| debug rtsp socket | Displays debug output for the RTSP client socket data. |
| debug voip ccapi error | Traces error logs in the CCAPI. |
| debug voip ccapi inout | Traces the execution path through the CCAPI. |
| debug voip ivr all | Displays all IVR messages. |
| debug voip ivr applib | Displays IVR API libraries being processed. |
| debug voip ivr callsetup | Displays IVR call setup being processed. |
| debug voip ivr digitcollect | Displays IVR digits collected during the call. |
| debug voip ivr dynamic | Displays IVR dynamic prompt play debug. |
| debug voip ivr error | Displays IVR errors. |
| debug voip ivr script | Displays IVR script debug. |
| debug voip ivr settlement | Displays IVR settlement activities. |
| debug voip ivr states | Displays IVR states. |
| debug voip ivr tclcommands | Displays the TCL commands used in the script. |
| debug voip rawmsg | Displays the raw VoIP message. |
| debug vtsp all | Enables debug vtsp session , debug vtsp error , and debug vtsp dsp . |
| debug vtsp dsp | Displays messages from the DSP. |
| debug vtsp error | Displays processing errors in the VTSP. |
| debug vtsp event | Displays the state of the gateway and the call events. |
| debug vtsp port | Limits VTSP debug output to a specific voice port. |
| debug vtsp rtp | Displays the voice telephony RTP packet debugging. |
| debug vtsp send-nse | Triggers the VTSP software module to send a triple redundant NSE. |
| debug vtsp session | Traces how the router interacts with the DSP. |
| debug vtsp stats | Debugs periodic statistical information sent and received from the DSP |
| debug vtsp vofr subframe | Displays the first 10 bytes of selected VoFR subframes for the interface. |
| debug vtsp tone | Displays the types of tones generated by the VoIP gateway. |

| Release | Modification |
|---|---|
| 12.3(5) | This command was introduced. |
| 12.3(7)T | This command was integrated into Cisco IOS Release 12.3(7)T. |

| Command | Description |
|---|---|
| disc_pi_off | Enables an H.323 gateway to disconnect a call when it receives a disconnect message with a PI. |
| voice call convert-discpi-to-prog | Converts a disconnect message with a PI to a progress message. |

| Release | Modification |
|---|---|
| 15.2(2)T | This command was introduced. |

| Command | Description |
|---|---|
| show voice call rate | Displays the voice call rate information. |

| Release | Modification |
|---|---|
| 12.1(3)XI4 | This command was introduced. |
| 12.1(5)T | This command was not supported in this release. |
| 12.1(5.3)T | This command was integrated into Cisco IOS Release 12.1(5.3)T. |
| 12.2(1) | This command was integrated into Cisco IOS Release 12.2. |

| Command | Description |
|---|---|
| progress_ind | Sets a specific PI in call Setup, Progress, or Connect messages from an H.323 VoIP gateway. |

| percent | The percentage deviation for trapping calls. The range of acceptable values is 1 to 100. The default is 49. |
|---|---|
| vad | (Optional) Specifies the deviation for calls with voice activity detection (VAD) turned on. |

| Release | Modification |
|---|---|
| 12.4(12) | This command was introduced in a release earlier than Cisco IOS Release 12.4(12). |
| 15.0(1)M | The no form of this command was modified. |

| carrier | Carrier code address family |
|---|---|
| trunk-group | Trunk group address family |
| prefix | E.164 prefix |
| percent | Value can be 50 to 100 percent with a default of 80. If set to 100, this trigger will be turned off. |

| Release | Modification |
|---|---|
| 12.3(1) | This command was introduced. |

| Command | Description |
|---|---|
| voice call capacity mir | Sets the values for the minimum interval between reporting (MIR) and smoothing transition time for weight (STW). |
| voice call capacity reporting | Turns on the reporting of maxima (first derivative) or inflection (second derivative) points in available capacity. |
| voice call capacity timer interval | Sets the periodic interval for reporting capacity from carrier, trunk group, or prefix databases |
| voice call trigger lwm | Sets the value for low water mark in the available capacity for carrier, trunk group, or prefix databases |
| voice call trigger percent-change | Sets the value for percentage change in the available capacity for carrier, trunk group, or prefix databases |

| carrier | Carrier code address family |
|---|---|
| trunk-group | Trunk group address family |
| prefix | E.164 prefix |
| percent | Value can be 0 to 30 percent with a default of 10. If set to 0, this trigger will be turned off. |

| Release | Modification |
|---|---|
| 12.3(1) | This command was introduced. |

| Command | Description |
|---|---|
| voice call capacity mir | Sets the values for the minimum interval between reporting (MIR) and smoothing transition time for weight (STW). |
| voice call capacity reporting | Turns on the reporting of maxima (first derivative) or inflection (second derivative) points in available capacity. |
| voice call capacity timer interval | Sets the periodic interval for reporting capacity from carrier, trunk group, or prefix databases. |
| voice call trigger hwm | Sets the value for high water mark in the available capacity for carrier, trunk group, or prefix databases. |
| voice call trigger percent-change | Sets the value for percentage change in the available capacity for carrier, trunk group, or prefix databases. |

| carrier | Carrier code address family |
|---|---|
| trunk-group | Trunk group address family |
| prefix | E.164 prefix |
| percent | If percent-change is selected, value can be 0 to 100 percent with a default of 30. If set to 0, this trigger will be turned
                                          off. If lwm is selected, value can be 0 to 30 percent with a default of 10. If set to 0, this trigger will be turned off. If hwm is select, value can be 50 to 100 percent with a default of 80. If set to 100, this trigger will be turned off. |

| Release | Modification |
|---|---|
| 12.3(1) | This command was introduced. |

| Command | Description |
|---|---|
| voice call capacity mir | Sets the values for the minimum interval between reporting (MIR) and smoothing transition time for weight (STW). |
| voice call capacity reporting | Turns on the reporting of maxima (first derivative) or inflection (second derivative) points in available capacity. |
| voice call capacity timer interval | Sets the periodic interval for reporting capacity from carrier, trunk group, or prefix databases |
| voice call trigger hwm | Sets the value for high water mark in the available capacity for carrier, trunk group, or prefix databases |
| voice call trigger lwm | Sets the value for low water mark in the available capacity for carrier, trunk group, or prefix databases |

| slot | Slot number for the card to be configured. The following platform-specific numbering schemes apply: Cisco 2600 series and Cisco 2600XM: 0 is the Advanced Integration Module (AIM) slot in the router chassis. 1 is the network module slot in the router chassis. Cisco 3600 series: A value from 1 to 6 identifies a network module slot in the router chassis. Cisco 3660: 7 is AIM slot 0 in the router chassis. 8 is AIM slot 1. |
|---|---|

| Release | Modification |
|---|---|
| 12.0(5)XK | The command was introduced on the Cisco 2600 series and Cisco 3600 series. |
| 12.0(7)T | This command was integrated into Cisco IOS Release 12.0(7)T. |
| 12.0(7)XK | This command was implemented on the Cisco MC3810. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T. |
| 12.2(2)XB | Values for the slot argument were updated to include AIMs. |
| 12.2(8)T | This command was integrated into Cisco IOS Release 12.2(8)T. |
| 12.2(13)T | This command was supported in Cisco IOS Release 12.2(13)T and implemented on the Cisco 1700 series, Cisco 2600XM, Cisco 3700
                                          series, Cisco 7200 series, Cisco 7500 series, Cisco ICS7750, Cisco MC3810, and Cisco VG200. |
| 12.2(15)T | This command was integrated into Cisco IOS Release 12.2(15)T. |

| Note | When running high-complexity images, the system can only process up to 16 voice channels. Those 16 time slots need to be
                                          within a contiguous range (timeslot maximum (TSmax) minus timeslot minimum (TSmin) is less than or equal to 16, where TSmax
                                          and TSmin are the maximum DS0 and minimum DS0 configured for voice). |
|---|---|

| Command | Description |
|---|---|
| codec complexity | Matches the DSP complexity packaging to the codecs to be supported. |
| dspfarm (voice-card) | Adds the specified voice card to those participating in a DSP resource pool. |

| Release | Modification |
|---|---|
| 15.0(1)M | This command was introduced in a release earlier than Cisco IOS Release 15.0(1)M. |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| voice class codec | Assigns an identification tag number for a codec voice class. |

| tag | A number used to identify voice class AAA. The range is from 1 to 10000. There is no default value. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced on the Cisco 3660, Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5800, and Cisco AS5850. |

| Command | Description |
|---|---|
| accounting suppress | Disables accounting that is automatically generated by the service provider module for a specific dial peer. |
| authentication method | Specifies an authentication method for calls coming into the defined dial peer. |
| authorization method | Specifies an authorization method for calls coming into the defined dial peer. |
| method | Specifies an accounting method for calls coming into the defined dial peer. |
| voice-class aaa | Applies properties defined in the voice class to a specific dial peer. |

| tag | Unique identification number assigned to one voice class. Range is 1 to 10000. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(3)T | This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. |

| Command | Description |
|---|---|
| busyout monitor ethernet | Configures a voice port to monitor a local Ethernet interface for events that would trigger a voice-port busyout. |
| busyout monitor probe | Configures a voice port to enter the busyout state if an RTR probe signal returned from a remote, IP-addressable interface
                                          crosses a specified delay or loss threshold. |
| busyout monitor serial | Configures a voice port to monitor a serial interface for events that would trigger a voice-port busyout. |
| show voice busyout | Displays information about the voice busyout state. |

| inbound | Inbound voice class called number. |
|---|---|
| outbound | Outbound voice class called number. |
| pool | Voice class called number pool. |
| tag | Digits that identify a specific inbound or outbound voice class called number or voice class called number pool. |

| Release | Modification |
|---|---|
| 12.4(11)T | This command was introduced. |

| Note | Enter the voice class called number command in global configuration mode without hyphens. Enter the voice-class called-number command in dial-peer configuration mode with hyphens. |
|---|---|

| Command | Description |
|---|---|
| show voice class called-number | Displays a specific voice class called number. |
| voice-class called-number (dial-peer) | Assigns a previously defined voice class called number to an inbound or outbound POTS dial peer. |

| number | Numeric tag that specifies the voice class cause code. The range is from 1 to 64. |
|---|---|

| Release | Modification |
|---|---|
| 15.0(1)M | This command was introduced in a release earlier than Cisco IOS Release 15.0(1)M. |

| Command | Description |
|---|---|
| voice class codec | Assigns an identification tag number for a codec voice class. |

| tag | Unique number that you assign to the voice class. Range is 1–10000. There is no default. |
|---|---|

| Release | Modification |
|---|---|
| 12.0(2)XH | This command was introduced on the Cisco AS5300. |
| 12.0(7)T | This command was implemented on the Cisco 2600 series and Cisco 3600 series. |
| 12.0(7)XK | This command was implemented on the Cisco MC3810. |
| 12.1(2)T | This command was integrated into Cisco IOS Release 12.1(2)T. |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models. |
| Cisco IOS XE Dublin
                                                17.10.1a | Introduced support for the following YANG models in codec
                                                preference configuration: g729br8 [bytes <10-244>] gsmamr-nb [encap \| modes \|
                                                      packetization-period] Introduced support for the following YANG model in video
                                                codec configuration: video codec [h261 \| mpeg4] |

| Note | The voice class codec command in global configuration mode is entered without a hyphen. The voice-class codec command in dial-peer configuration mode is entered with a hyphen. transparent is not available under voice class codec in YANG. However, you can configure codec transparent directly under dial-peer. |
|---|---|

| Command | Description |
|---|---|
| codec preference | Specifies a list of preferred codecs to use on a dial peer. |
| test voice port detector | Defines the order of preference in which network dial peers select codecs. |
| voice-class codec (dial peer) | Assigns a previously configured codec selection preference list to a dial peer. |

| cptone-name | Descriptive identifier for this class of custom call-progress tones that associates this set of custom call-progress tones
                                          with voice ports. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(5)XM | This command was introduced on the Cisco 2600, Cisco 3600, and Cisco MC3810 platforms. |
| 12.2(2)T | This command was implemented on Cisco 1750 access routers and integrated into Cisco IOS Release 12.2(2)T. |

| Command | Description |
|---|---|
| dualtone | Defines the tone and cadence for a custom call-progress tone. |
| supervisory custom-cptone | Associates a class of custom call-progress tones with a voice port. |
| voice class dualtone-detect-params | Modifies the boundaries and limits for call-progress tones. |

| tag | Voice class DSCP tag. The range is from 1 to 10000. |
|---|---|

| Release | Modification |
|---|---|
| 15.2(2)T | This command was introduced. |

| Command | Description |
|---|---|
| dscp media | Specifies the RPH to DSCP mapping. |

| tag | Unique identification number assigned to one voice class. Range is from 1 to 10000. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(3)T | This command was introduced on the Cisco 2600 series, Cisco 3600 series, and the Cisco MC3810. |

| Command | Description |
|---|---|
| supervisory disconnect dualtone voice-class | Assigns a previously configured voice class for FXO supervisory disconnect tone to a voice port. |

| tag | Unique tag identification number assigned to a voice class. Range is from 1 to 10000. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(5)XM | This command was introduced on the Cisco 2600 series, Cisco 3600 series, and Cisco MC3810. |
| 12.2(2)T | This command was implemented on Cisco 1750 routers and integrated into Cisco IOS Release 12.2(2)T. |

| Command | Description |
|---|---|
| supervisory dualtone-detect-params | Assigns the boundary and detection tolerance parameters defined by the voice class dualtone-detect-params command to a voice port. |
| voice class custom-cptone | Creates a voice class for defining custom call-progress tones. |

| tag | A number assigned to a voice class E.164 pattern map. The range is from 1 to 10000. |
|---|---|

| Release | Modification |
|---|---|
| 15.2(4)M | This command was introduced. |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| show voice class e164-pattern-map | Displays the configuration of E.164 pattern maps. |
| voice class e164-pattern-map load | Loads a destination E.164 pattern map that is specified by a text file on a dial peer. |

| dial-peer-group-id | Assigns a tag for a particular dial-peer group. The range is 1-10000. |
|---|---|

| Release | Modification |
|---|---|
| Cisco IOS 15.4(1)T Cisco IOS XE 3.11S | This command was introduced. |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| dial-peer voice | To define a dial peer. |
| destination -pattern | To configure a destination pattern. |

| tag | A number that is assigned to the destination E.164 pattern map. The range is from 1 to 10000. |
|---|---|

| Release | Modification |
|---|---|
| 15.2(4)M | This command was introduced. |

| Command | Description |
|---|---|
| show voice class e164-pattern-map | Displays the configuration of E.164 pattern maps. |
| voice class e164-pattern-map | Creates an E.164 pattern map to specify multiple destination E.164 patterns in a dial peer. |

| tag | The range is from 1 to 10000. |
|---|---|

| Release | Modification |
|---|---|
| IOS XE Fuji Release 16.8.1 | This command was introduced. |

| voice class e164-pattern-map | Creates an E.164 pattern map to specify multiple destination E.164 patterns in dial peer. |
|---|---|
| voice class e164-pattern-map load | Loads a destination E.164 pattern map that is specified by a text file on a dial peer. |

| tag | Unique number to identify the voice class. Range is from 1 to 10000. There is no default value. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(2)T | This command was introduced on the Cisco 1700, Cisco 2600 series, Cisco 3600 series, Cisco 7200 series, Cisco AS5300, Cisco
                                          uBR910, and Cisco uBR924. |

| Command | Description |
|---|---|
| voice-class h323 | Assigns an H.323 voice class to a VoIP dial peer. |

| number | Numeric tag that specifies the voice class media. The range is from 1 to 10000. |
|---|---|

| Release | Modification |
|---|---|
| 15.0(1)M | This command was introduced in a release earlier than Cisco IOS Release 15.0(1)M. |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| voice class codec | Assigns an identification tag number for a codec voice class. |

| tag | Unique number that you assign to the voice class. Range is from 1 to 10000. |
|---|---|

| Release | Modification |
|---|---|
| 12.0(3)XG | This command was introduced on the Cisco MC3810. |
| 12.0(4)T | This command was integrated into Cisco IOS Release 12.0(4)T. |
| 12.1(3)T | This command was implemented on Cisco 2600 series and Cisco 3600 series. |

| Command | Description |
|---|---|
| signal keepalive | Configures the keepalive signaling packet interval for Cisco trunks and FRF.11 trunks. |
| signal pattern | Configures the ABCD bit pattern for Cisco trunks and FRF.11 trunks. |
| signal timing idle suppress-voice | Configures the signal timing parameter for the idle state of a call. |
| signal timing oos | Configures the signal timing parameter for the OOS state of a call. |
| signal-type | Sets the signaling type for a network dial peer. |
| voice-class permanent | Assigns a previously configured voice class for a Cisco trunk or FRF.11 trunk to a network dial peer. |

| tag | Unique tag to identify the resource. The range is from 1 to 5. |
|---|---|

| Release | Modification |
|---|---|
| 15.1(2)T | This command was introduced. |

| Command | Description |
|---|---|
| debug rai | Enables debugging for Resource Allocation Indication (RAI). |
| periodic-report interval | Configures periodic reporting parameters for gateway resource entities. |
| rai target | Configures the SIP RAI mechanism. |
| resource (voice) | Configures parameters for monitoring resources. |
| show voice class resource-group | Displays the resource group configuration information for a specific resource group or all resource groups. |

| tag | Unique tag to identify the route string. The range is from 1 to 10000. |
|---|---|

| Release | Modification |
|---|---|
| 15.3(3)M | This command was introduced. |
| Cisco IOS XE Release 3.10S | This command was integrated into Cisco IOS XE Release 3.10S. |

| server-group-id | Unique server group ID to identify the server group. You can configure up to five servers per server group. |
|---|---|

| Release | Modification |
|---|---|
| Cisco IOS XE Release 3.11S 15.4(1)T | The following commands were introduced or modified: voice class server-group , description , ipv4 port preference , ipv6 port preference , hunt-scheme , show voice class server-group , shutdown (Server Group) . |
| Cisco IOS XE Bengaluru 17.4.1a | The following command is introduced under voice class server-group . huntstop rule-tag resp-code from_resp_code to to_resp_code . |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| description | Provides a description for the server group. |
| hunt-scheme | Defines a hunt method for the order of selection of target server IP addresses (from the IP addresses configured for this
                                          server group) for the setting up of outgoing calls. |
| shutdown (Server Group) | To make the server group inactive. |
| show voice class server-group | Displays the configurations for all configured server groups or a specified server group. |

| tag | Voice class Session Initiation Protocol (SIP) copylist tag. The range is from 1 to 10000. |
|---|---|

| Release | Modification |
|---|---|
| 15.1(3)T | This command was introduced. |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| sip-header | Specifies the SIP header to be sent to the peer call leg. |

| tag | Unique tag to identify the header. The range is from 1 to 1000. |
|---|---|

| Release | Modification |
|---|---|
| 15.3(3)M | This command was introduced. |
| Cisco IOS XE Release 3.10S | This command was integrated into Cisco IOS XE Release 3.10S. |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models. |

| number | Numeric tag that specifies the voice class SIP profile. The range is from 1 to 10000. |
|---|---|

| Release | Modification |
|---|---|
| 15.0(1)M | This command was introduced in a release earlier than Cisco IOS Release 15.0(1)M. |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models. |

| Note | The rule option [before] is not available in sip-profile YANG configuration. voice class sip-profile <tag> rule [before] |
|---|---|

| Command | Description |
|---|---|
| voice class codec | Assigns an identification tag number for a codec voice class. |

| tag | Unique number that you assign to the srtp-crypto voice class. Range is 1–10000. There is no default. |
|---|---|

| Release | Modification |
|---|---|
| Cisco IOS XE Everest 16.5.1b | This
                                       					 command was introduced. |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models. |
| Cisco IOS XE Dublin
                                             17.10.1a | The YANG model for this command can now be configured under voice register pool . |

| Command | Description |
|---|---|
| srtp-crypto | Assigns a previously configured crypto-suite selection preference list globally or to a voice class tenant. |
| crypto | Specifies the preference for an SRTP cipher-suite that will be offered by Cisco Unified Border Element (CUBE) in the SDP in
                                          offer and answer. |
| show sip-ua calls | Displays active user agent client (UAC) and user agent server (UAS) information on Session Initiation Protocol (SIP) calls. |
| show sip-ua srtp | Displays Session Initiation Protocol (SIP) user-agent (UA) Secure Real-time Transport Protocol (SRTP) information. |

| tag | A
                                          						number used to identify voice class tenant. The range is from 1 to 10000. There
                                          						is no default value. |
|---|---|

| Release | Modification |
|---|---|
| 15.6(2)T and IOS XE Denali 16.3.1 | This
                                          						command was introduced. |
| Cisco IOS XE Bengaluru 17.4.1a | Introduced support for YANG models. |

| tag | A number used to identify voice class TLS profile. The range is 1-10000. There is no default value. |
|---|---|

| Release | Modification |
|---|---|
| Cisco IOS XE Amsterdam 17.3.1a | This command was introduced. |

| Command | Description |
|---|---|
| trustpoint | Creates a trustpoint to store the devices certificate that is generated as part of the enrollment process using Cisco IOS
                                          public-key infrastructure (PKI) commands. |
| description | Provides a description for the TLS profile group. |
| client-vtp | Assigns a client verification trustpoint. |
| cipher | Configures cipher setting. |
| cn-san | Enables server identity validation through Common Name (CN) and Subject Alternate Name (SAN) fields in the server certificate
                                          during client-side SIP /TLS connections |
| sni send | Enables TLS Server Name Indication (SNI) during the initial TLS handshake process. |
| crypto signaling | Identifies the trustpoint or the tls-profile tag that is used during the TLS handshake process. |

| tag | Specifies the voice class tls-cipher tag. |
|---|---|

| Release | Modification |
|---|---|
| Cisco IOS XE Cupertino
                                          17.8.1a | This command was introduced. |

| tag | Label that uniquely identifies the voice class. Can be up to 32 alphanumeric characters. |
|---|---|

| Release | Modification |
|---|---|
| 12.3(4)XD | This command was introduced. |
| 12.3(7)T | This command was integrated into Cisco IOS Release 12.3(7)T. |

| Command | Description |
|---|---|
| inject guard-tone | Plays out a guard tone with the voice packet. |
| inject pause | Specifies a pause between injected tones. |
| inject tone | Specifies a wakeup or frequency selection tone to be played out before the voice packet. |
| timing delay-voice tdm | Specifies the delay before a voice packet is played out. |
| voice-class tone-signal | Assigns a previously configured tone-signal voice class to a voice port. |

| tag | Label that uniquely identifies the voice class. Can be up to 32 alphanumeric characters. |
|---|---|
| sip | Voice class for SIP URIs. |
| tel | Voice class for TEL URIs. |

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| debug voice uri | Displays debugging messages related to URI voice classes. |
| destination uri | Specifies the voice class used to match the dial peer to the destination URI for an outgoing call. |
| host | Matches a call based on the host field in a SIP URI. |
| incoming uri | Specifies the voice class used to match a VoIP dial peer to the URI of an incoming call. |
| pattern | Matches a call based on the entire SIP or TEL URI. |
| phone context | Filters out URIs that do not contain a phone-context field that matches the configured pattern. |
| phone number | Matches a call based on the phone number field in a TEL URI. |
| show dialplan incall uri | Displays which dial peer is matched for a specific URI in an incoming call. |
| show dialplan uri | Displays which outbound dial peer is matched for a specific destination URI. |
| user-id | Matches a call based on the user-id field in the SIP URI. |

| user-id | User-id field is given preference. |
|---|---|
| host | Host field is given preference. |

| Release | Modification |
|---|---|
| 12.3(4)T | This command was introduced. |

| Command | Description |
|---|---|
| debug voice uri | Displays debugging messages related to URI voice classes. |
| destination uri | Specifies the voice class used to match the dial peer to the destination URI for an outgoing call. |
| host | Matches a call based on the host field in a SIP URI. |
| incoming uri | Specifies the voice class used to match a VoIP dial peer to the URI of an incoming call. |
| user-id | Matches a call based on the user-id field in the SIP URI. |
| show dialplan incall uri | Displays which dial peer is matched for a specific URI in an incoming call. |
| show dialplan uri | Displays which outbound dial peer is matched for a specific destination URI. |
| voice class uri | Creates or modifies a voice class for matching dial peers to a SIP or TEL URI. |

| tag | A number to identify the voice class. Range is from 1 to 10000. There is no default. |
|---|---|

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced on the Cisco 3660, Cisco AS5300, Cisco AS5350, Cisco AS5400, Cisco AS5800, and Cisco AS5850. |

| Command | Description |
|---|---|
| voice class aaa | Enables dial-peer-based VoIP AAA configurations. |

| inbound | Assigns an inbound voice class called number to the dial peer. |
|---|---|
| outbound | Assigns an outbound voice class called number to the dial peer. |
| tag | Digits that identify a specific voice class called number. |

| Release | Modification |
|---|---|
| 12.4(11)T | This command was introduced. |

| Note | The voice class called number command in global configuration mode is entered without hyphens. The voice-class called-number command in dial peer configuration mode is entered with hyphens. |
|---|---|

| Command | Description |
|---|---|
| voice class called number | Defines a voice class called number or range of numbers for H.320 calls. |
| voice-class called-number-pool | Defines a pool of dynamic voice class called numbers for a voice port. |

| tag | Digits that identify a specific voice class called number pool. |
|---|---|

| Release | Modification |
|---|---|
| 12.4(11)T | This command was introduced. |

| Command | Description |
|---|---|
| voice class called number | Defines a voice class called number or range of numbers for H.320 calls. |
| voice-class called-number (dial peer) | Defines a called number or range of called numbers for a POTS dial peer. |

| tag | Unique number assigned to the voice class. The range is from 1 to 10000. This tag number maps to the tag number created using the voice class codec command available in global configuration mode. |
|---|---|
| offer-all | (Optional) Adds all the configured codecs from the voice class codec to the outgoing offer from the Cisco Unified Border Element
                                          (Cisco UBE). |

| Release | Modification |
|---|---|
| 12.0(2)XH | This command was introduced in Cisco IOS Release 12.0(2)XH and implemented on the Cisco AS5300 series routers. |
| 12.0(7)T | This command was integrated into Cisco IOS Release 12.0(7)T and implemented on the Cisco 2600 series and the Cisco 3600 series. |
| 12.0(7)XK | This command was integrated into Cisco IOS Release 12.0(7)XK and implemented on the Cisco MC3810. |
| 15.1(2)T | This command was modified. The offer-all keyword was added. |
| Cisco IOS XE Release 2.5 | This command was integrated into Cisco IOS XE Release 2.5. |
| Cisco IOS XE Amsterdam 17.2.1r | Introduced support for YANG models. |

| Note | The voice-class codec command in dial-peer configuration mode is entered with a hyphen. The voice class codec command in global configuration mode is entered without a hyphen. |
|---|---|

| Command | Description |
|---|---|
| show dial-peer voice | Displays the configuration for all dial peers configured on the router. |
| test voice port detector | Defines the order of preference in which network dial peers select codecs. |
| voice class codec | Enters voice-class configuration mode and assigns an identification tag number for a codec voice class. |

| tag | Unique number to identify the voice class. Range is from 1 to 10000. |
|---|---|

| Release | Modification |
|---|---|
| 12.1(2)T | This command was introduced. |

| Command | Description |
|---|---|
| show dial-peer voice | Displays the configuration for all dial peers configured on the router. |
| voice class h323 | Enters voice-class configuration mode and assigns an identification tag number for an H.323 voice class. |

| tag | Unique number assigned to the voice class. The tag number maps to the tag number created using the voice class permanent global configuration command. Range is from 1 to 10000. |
|---|---|

| Release | Modification |
|---|---|
| 12.0(3)XG | This command was introduced on Cisco MC3810. |
| 12.0(4)T | This command was integrated into Cisco IOS Release 12.0(4)T. |
| 12.1(3)T | This command was implemented on Cisco 2600 series and Cisco 3600 series. |

| Command | Description |
|---|---|
| signal keepalive | Configures the keepalive signaling packet interval for Cisco trunks and FRF.11 trunks. |
| signal pattern | Configures the ABCD bit pattern for Cisco trunks and FRF.11 trunks. |
| signal timing idle suppress-voice | Configures the signal timing parameter for the idle state of a call. |
| signal timing oos | Configures the signal timing parameter for the OOS state of a call. |
| signal-type | Sets the signaling type for a network dial peer. |
| voice class permanent | Creates a voice class for a Cisco trunk or FRF.11 trunk. |

| tag | Unique number assigned to the voice class. The tag number maps to the tag number created using the voice class permanent global configuration command. Range is 1 to 10000. |
|---|---|

| Release | Modification |
|---|---|
| 12.0(3)XG | This command was introduced on Cisco MC3810. |
| 12.0(4)T | This command was integrated into Cisco IOS Release 12.0(4)T. |
| 12.1(3)T | This command was implemented as a voice-port configuration command on Cisco 2600 series and Cisco 3600 series routers. |

| Command | Description |
|---|---|
| signal keepalive | Configures the keepalive signaling packet interval for Cisco trunks and FRF.11 trunks. |
| signal pattern | Configures the ABCD bit pattern for Cisco trunks and FRF.11 trunks. |
| signal timing idle suppress-voice | Configures the signal timing parameter for the idle state of a call. |
| signal timing oos | Configures the signal timing parameter for the OOS state of a call. |
| signal-type | Sets the signaling type for a network dial peer. |
| voice class permanent | Creates a voice class for a Cisco trunk or FRF.11 trunk. |

| system | (Optional) Configures ANAT globally. |
|---|---|

| Release | Modification |
|---|---|
| 12.4(22)T | This command was introduced. |

| Command | Description |
|---|---|
| bind | Binds the source address for signaling and media packets to the IPv4 or IPv6 address of a specific interface. |

| pai | (Optional) Enables the P-Asserted-Identity (PAI) privacy header in incoming and outgoing SIP requests or response messages. |
|---|---|
| ppi | (Optional) Enables the P-Preferred-Identity (PPI) privacy header in incoming SIP requests and outgoing SIP requests or response
                                          messages. |
| system | (Optional) Uses global-level configuration settings to configure the dial peer. |

| Release | Modification |
|---|---|
| 15.1(1)T | This command was introduced. |
| 15.1(3)T | This command was modified. Support for incoming calls was added. |

| Command | Description |
|---|---|
| asserted-id | Enables support for the asserted ID header in incoming and outgoing SIP requests or response messages at the global level. |
| calling-info pstn-to-sip | Specifies calling information treatment for PSTN-to-SIP calls. |
| privacy | Sets privacy in support of RFC 3323. |

| number | Registered number. The number must be between 4 and 32. |
|---|---|
| system | (Optional) Configures the association globally. |

| Release | Modification |
|---|---|
| 15.1(2)T | This command was introduced. |

| Command | Description |
|---|---|
| associate registered-
                                                number | Associates the preloaded route and outbound proxy details with the registered number in voice service VoIP SIP configuration
                                          mode. |

| dtmf | Provides asymmetric support only for dual-tone multi-frequency (DTMF) payloads. |
|---|---|
| dynamic-codecs | Provides asymmetric support only for dynamic codec payloads. |
| full | Provides asymmetric support both for DTMF and dynamic codec payloads. |
| system | (Optional) Specifies that the asymmetric payload uses the global value. |

| Release | Modification |
|---|---|
| 12.4(15)T | This command was introduced. |
| Cisco IOS XE
                                          Release 3.1S | This command was integrated into Cisco IOS Release IOS XE 3.1S |

| Command | Description |
|---|---|
| dial-peer voice | Defines a particular dial peer, specifies the method of voice encapsulation, and enters dial peer configuration mode. |

| system | (Optional) Uses the global configuration settings to allow only audio and image
                                          						(for T.38 Fax) media types. |
|---|---|

| Release | Modification |
|---|---|
| Cisco IOS
                                       					 15.6(2)T | This
                                       					 command was introduced. |
| Cisco IOS XE Denali 16.3.1 | This command was integrated into Cisco IOS XE Denali 16.3.1. |

| system | (Optional) Specifies that the dial peer use whatever setting is configured at the global (voice service SIP) command level
                                          (default). |
|---|---|

| Release | Modification |
|---|---|
| 12.4(24)T | This command was introduced. |

| Command | Description |
|---|---|
| authenticate redirecting-number | Enables a Cisco IOS voice gateway to authenticate and pass SIP credentials based on the redirecting number when available
                                          instead of the calling number of a forwarded call. |

| control | Binds Session Initiation Protocol (SIP) signaling packets. |
|---|---|
| media | Binds only media packets. |
| all | Binds SIP signaling and media packets. |
| source interface interface-id | Specifies an interface as the source address of SIP packets. |
| ipv6-address ipv6-address | (Optional) Configures the IPv6 address of the interface. |

| Release | Modification |
|---|---|
| 15.1(2)T | This command was introduced. |
| Cisco IOS XE Amsterdam 17.3.1a | Introduced support for YANG models. |

| 180 | Specifies that incoming SIP 180 Ringing messages should be dropped (not passed to the other leg). |
|---|---|
| 181 | Specifies that incoming SIP 181 Call is Being Forwarded messages should be dropped (not passed to the other leg). |
| 183 | Specifies that incoming SIP 183 Session in Progress messages should be dropped (not passed to the other leg). |
| sdp | (Optional) Specifies that either the presence or absence of Session Description Protocol (SDP) information in the received
                                          response determines when the dropping of specified incoming SIP messages takes place. |
| absent | Configures the SDP option so that specified incoming SIP messages are dropped only if SDP is absent from the received provisional
                                          response. |
| present | Configures the SDP option so that specified incoming SIP messages are dropped only if SDP is present in the received provisional
                                          response. |
| system | Configures the dial peer to use global configuration settings for dropping incoming SIP provisional response messages. |

| Release | Modification |
|---|---|
| 12.4(22)YB | This command was introduced. Only SIP 180 and SIP 183 messages are supported on Cisco UBEs. |
| 15.0(1)M | This command was integrated into Cisco IOS Release 15.0(1)M. |
| 15.0(1)XA | This command was modified. Support was added for SIP 181 messages on the Cisco IOS SIP gateway, SIP-SIP Cisco UBEs, and the
                                          SIP trunk of Cisco Unified Communications Manager Express (Cisco Unified CME). |
| 15.1(1)T | This command was integrated into Cisco IOS Release 15.1(1)T. |
| Cisco IOS XE Release 3.1S | This command was integrated into Cisco IOS XE Release 3.1S. |

| Note | This command is supported only on outbound dial peers--it is nonoperational if configured on inbound dial peers. You should
                                          configure this command on the outbound SIP leg that sends out the initial INVITE message. Additionally, this feature applies
                                          only to SIP-to-SIP calls and will have no effect on H.323-to-SIP calls. |
|---|---|

| Command | Description |
|---|---|
| block | Configures global configuration for dropping specified SIP provisional response messages on a Cisco IOS voice gateway or Cisco
                                          UBE. |
| map resp-code | Configures global settings on a Cisco UBE for mapping specific incoming SIP provisional response messages to a different SIP
                                          response message. |
| voice-class sip map resp-code | Configures a specific dial peer on a Cisco UBE to map specific incoming SIP provisional response messages to a different SIP
                                          response message. |

| dest-route-string | Enables call routing based on the Destination-Route-String. |
|---|---|
| p-called-party-id | Enables call routing based on the P-Called-Party-Id header. |
| history-info | Enables call routing based on the History-Info header. |
| url | Enables call routing based on the URL. |
| system | (Optional) Uses the global configuration settings to enable call routing based on the header values on this dial peer. |

| Release | Modification |
|---|---|
| 12.4(22)YB | This command was introduced. |
| 15.0(1)M | This command was integrated into Cisco IOS Release 15.0(1)M. |
| 15.1(2)T | This command was modified. The history-info keyword was added. |
| 15.2(1)T | This command was modified. The url keyword was added. |
| 15.3(3)M | This command was modified. The dest-route-string keyword was added. |
| Cisco IOS XE Release 3.10S | This command was integrated into Cisco IOS XE Release 3.10S. |

| Command | Description |
|---|---|
| call-route | Enables call routing based on the Destination-Route-String, P-Called-Party-Id and History-Info header values at the global
                                          configuration level. |

| Release | Modification |
|---|---|
| 12.4(24)T | This command was introduced. |

| system | Uses the system level configuration for sdp version increment |
|---|---|

| Release | Modification |
|---|---|
| Cisco IOS 15.5(2)T Cisco IOS XE 3.15 | This command was introduced. |

| tag | Tag number of the Session Initiation Protocol (SIP) copy list. The range is from 1 to 10000. |
|---|---|
| system | Specifies to use the global level configuration to copy the list. |

| Release | Modification |
|---|---|
| 15.1(3)T | This command was introduced. |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
| voice class sip-copylist | Configures a list of entities to be sent to the peer call leg. |

| Release | Modification |
|---|---|
| 12.4(9)T | This command was introduced. |

| Command | Description |
|---|---|
| debug csm neat | Turns on debugging for all Call Switching Module (CSM) Voice over IP (VoIP) calls. |
| show running-config | Displays the running configuration. |
| e911 | Enables E911 system services for SIP voice service VoIP. |

| tag | Event list tag. Range is 1-10000. |
|---|---|

| Release | Modification |
|---|---|
| Cisco IOS XE 3.11S | The command was introduced. |
| Cisco IOS XE Cupertino 17.7.1a | Introduced support for YANG models. |

| Command | Description |
|---|---|
|  |  |

| re-negotiate | Enables
                                       					 end to end renegotiation if the UPDATE request contains changes in caller ID,
                                       					 transcoder addition or deletion, or video escalation or de-escalation. |
|---|---|

| Release | Modification |
|---|---|
| Cisco
                                    				  IOS 15.5(3)M, Cisco IOS-XE 3.16S | This
                                       					 command was introduced. |

| standard | (Optional) Specifies standard RFC 4040 encapsulation. |
|---|---|
| system | (Optional) Configures the dial peer to use global configuration settings for clear-channel codec negotiation. |

| Release | Modification |
|---|---|
| 15.0(1)XA | This command was introduced. |
| 15.1(1)T | This command was integrated into Cisco IOS Release 15.1(1)T. |

| Command | Description |
|---|---|
| encap clear-channel standard | Enables RFC 4040-based clear-channel codec negotiation for SIP calls globally on a Cisco IOS voice gateway or Cisco UBE. |