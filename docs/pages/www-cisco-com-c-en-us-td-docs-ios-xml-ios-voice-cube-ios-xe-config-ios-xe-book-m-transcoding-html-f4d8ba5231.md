---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-transcoding-html-f4d8ba5231
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_transcoding.html
retrieved_at: 2026-08-16T15:50:58.499586+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Transcoding Configuration

## Chapter: Transcoding Configuration

# Transcoding Configuration

## Overview

Transcoding is a process that converts a media stream encoded with one algorithm to another using Digital Signal Processors
                           (DSPs). For example, a media stream encoded using OPUS may be decoded and re-encoded (transcoded) using G.711.

Starting from Cisco IOS XE 17.18.2 release, Cisco Unified Border Element (CUBE) is supported on C8375-E-G2 secure router platform with vDSP (Virtual DSP) enabled.
                                       These secure routers offer software-based DSP capabilities, effectively replacing traditional Packet Voice Digital Signal
                                       Processor Modules (PVDMs). The vDSP delivers software-based DSP resources, enabling the router CPU to handle transcoding,
                                       conferencing, and media termination without dedicated DSP hardware. For details on vDSP installation, upgrade, downgrade configurations,
                                       see Virtual DSP for Secure Routers .

Following vDSP installation, the configuration and monitoring of transcoding services are performed the same as with traditional
                                       PVDM modules.

In high availability configurations, checkpoint for transcoded calls require both the standby system and its DSPs to be ready
                                       when a call begins. Calls that are set up before the standby resources are ready will not be maintained on failover.

LTI-based Transcoding

Internal API is used to access Digital Signal Processor (DSP) resources for transcoding.

Transcoding resources (DSPFARM) and CUBE must be on the same platform.

Only a DSPFARM profile configuration is required. Skinny Client Control Protocol (SCCP) configuration is not required.

No TCP socket is opened and no registration is used.

```
Device(config)# dspfarm profile 1 transcode Device(config-dspfarm-profile)# associate application CUBE
```

DSPs are not used for encryption with IOS XE. As all media is encrypted or decrypted as it leaves or enters the platform,
                                 transcoding may be used for any combination of RTP-RTP, RTP-SRTP, or SRTP-SRTP calls.

Cisco Aggregated Services Routers 1000 Series (ASR 1K)

Cisco 4000 Series-Integrated Services Routers (ISR G3)

Cisco 8200 Catalyst Edge Series

Cisco 8300 Catalyst Edge Series

### Limitations

Video transcoding is not supported. This document only refers to transcoding for CUBE B2BUA calls. Refer to System Configuration Guide for Cisco Unified Communications Manager for UCM MTP details.

SCCP-based transcoding is not supported with IOS XE releases.

Transcoding cannot be used for SRTP-Passthrough calls or when pass-thru content SDP is enabled.

Secure Communications Interoperability Protocol (SCIP) codec transcoding is not supported.

In Cisco IOS XE 17.16.1a release, the Secure Communications Interoperability Protocol (SCIP) feature is available in 'preview’ mode as it includes
                                                limited functionality or incomplete software dependencies. Cisco reserves the right to disable preview features at any time
                                                without notice. Cisco Technical Support provides reasonable effort support for features in preview mode. There is no Service
                                                Level Objective (SLO) in response times for features in preview mode; response times may be slow.

## Configure LTI-Based Transcoding

PVDM4 modules support Opus transcoding.

### SUMMARY STEPS

- enable

- configure terminal

- voice-card voice-interface-slot-number

- dsp services dspfarm

- exit

- dspfarm profile profile-identifier transcode

- codec codec

- maximum sessions sessions

- associate application CUBE

- no shutdown

### DETAILED STEPS

Step 1

enable

### Example:

```
Device> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Device> configure terminal
```

Enters global configuration mode.

Step 3

voice-card voice-interface-slot-number

### Example:

```
Device(config)# voice-card 0/2
```

Configures a voice card and enters voice-card configuration mode.

Step 4

dsp services dspfarm

Enable voice-only DSP services on the Voice Card.

Step 5

exit

Exits the voice-card configuration mode.

Step 6

dspfarm profile profile-identifier transcode

### Example:

```
Device(config)# dspfarm profile 2 transcode
```

profile-identifier - Number that uniquely identifies a profile. Range: 1–65535.

transcode - Enables profile for transcoding.

Step 7

codec codec

### Example:

```
Device(config-dspfarm-profile)# codec opus
```

Step 8

maximum sessions sessions

Step 9

associate application CUBE

Step 10

no shutdown

### Example:

```
Device (config-dsp-farm-profile) # no shutdown
```

## Configuration
                        	 Examples for LTI Based Transcoding

### Example: LTI-based Transcoding

```
! Enabling dspfarm services under voice-card
Device(config)# voice-card 0/2
Device(config-voicecard)# dsp services dspfarm
Device(config-voicecard)# exit
! Configuring dspfarm profile
Device(config)# dspfarm profile 2 transcode
Device(config-dspfarm-profile)# codec g729abr8
Device(config-dspfarm-profile)# codec g729ar8
Device(config-dspfarm-profile)# codec g711alaw
Device(config-dspfarm-profile)# codec g711ulaw
Device(config-dspfarm-profile)# codec g722-64
Device(config-dspfarm-profile)# codec opus
Device(config-dspfarm-profile)# maximum sessions 10
Device(config-dspfarm-profile)# associate application CUBE
Device(config-dspfarm-profile)# no shutdown
```

## Verify Configuration

```
Device#show dspfarm profile   
 Profile ID = 2, Service = TRANSCODING, Resource ID = 2   
 Profile Service Mode : Non Secure 
 Profile Admin State : UP 
 Profile Operation State : ACTIVE 
 Application : CUBE   Status : ASSOCIATED 
 Resource Provider : FLEX_DSPRM   Status : UP 
 Total Number of Resources Configured : 10 
 Total Number of Resources Available : 10 
 Total Number of Resources Out of Service : 0 
 Total Number of Resources Active : 0
 Codec Configuration: num_of_codecs:6 
 Codec : opus, Maximum Packetization Period : 120 
 Codec : g722-64, Maximum Packetization Period : 30 
 Codec : g711ulaw, Maximum Packetization Period : 30 
 Codec : g711alaw, Maximum Packetization Period : 30 
 Codec : g729ar8, Maximum Packetization Period : 60 
 Codec : g729abr8, Maximum Packetization Period : 60
Device#
```

## VoIP Trace Logging

VoIP Trace is used for event logging and debugging of VoIP parameters. Using the VoIP Trace framework, the following information
                           is recorded for transcoded calls at CUBE :

Reservation

Association

Disassociation

The following is a sample output for VoIP Trace logging specific to transcoded calls at CUBE :

```
Apr 16 11:32:42.910: //63/32191ED78080/CUBE_VT/SIP/API: ccsip_xcoder_reserve (0)
Apr 16 11:32:42.926: //63/32191ED78080/CUBE_VT/SIP/API: ccsip_xcoder_associate (0)
Apr 16 11:32:42.942: //63/32191ED78080/CUBE_VT/SIP/API: ccsip_xcoder_disassociate (0)
Apr 16 11:32:42.946: //62/32191ED78080/CUBE_VT/SIP/API: ccsip_xcoder_disassociate (-1)
Apr 16 11:32:42.948: //63/32191ED78080/CUBE_VT/SIP/API: ccsip_xcoder_disassociate_success (0)
Apr 16 11:32:43.910: //66/32191ED78080/CUBE_VT/SIP/API: ccsip_xcoder_reserve (-1)
Apr 16 11:32:44.926: //66/32191ED78080/CUBE_VT/SIP/API: ccsip_xcoder_associate (-1)
```

| Note | Starting from Cisco IOS XE 17.18.2 release, Cisco Unified Border Element (CUBE) is supported on C8375-E-G2 secure router platform with vDSP (Virtual DSP) enabled.
                                       These secure routers offer software-based DSP capabilities, effectively replacing traditional Packet Voice Digital Signal
                                       Processor Modules (PVDMs). The vDSP delivers software-based DSP resources, enabling the router CPU to handle transcoding,
                                       conferencing, and media termination without dedicated DSP hardware. For details on vDSP installation, upgrade, downgrade configurations,
                                       see Virtual DSP for Secure Routers . Following vDSP installation, the configuration and monitoring of transcoding services are performed the same as with traditional
                                       PVDM modules. |
|---|---|

| Note | In high availability configurations, checkpoint for transcoded calls require both the standby system and its DSPs to be ready
                                       when a call begins. Calls that are set up before the standby resources are ready will not be maintained on failover. |
|---|---|

| Note | The following support LTI-based transcoding: Cisco Aggregated Services Routers 1000 Series (ASR 1K) Cisco 4000 Series-Integrated Services Routers (ISR G3) Cisco 8200 Catalyst Edge Series Cisco 8300 Catalyst Edge Series |
|---|---|

| Note | In Cisco IOS XE 17.16.1a release, the Secure Communications Interoperability Protocol (SCIP) feature is available in 'preview’ mode as it includes
                                                limited functionality or incomplete software dependencies. Cisco reserves the right to disable preview features at any time
                                                without notice. Cisco Technical Support provides reasonable effort support for features in preview mode. There is no Service
                                                Level Objective (SLO) in response times for features in preview mode; response times may be slow. |
|---|---|

| Note | PVDM4 modules support Opus transcoding. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device> configure terminal | Enters global configuration mode. |
| Step 3 | voice-card voice-interface-slot-number Example: Device(config)# voice-card 0/2 | Configures a voice card and enters voice-card configuration mode. |
| Step 4 | dsp services dspfarm | Enable voice-only DSP services on the Voice Card. |
| Step 5 | exit | Exits the voice-card configuration mode. |
| Step 6 | dspfarm profile profile-identifier transcode Example: Device(config)# dspfarm profile 2 transcode | Enters a DSP farm profile configuration mode and defines a profile for DSP farm services. profile-identifier - Number that uniquely identifies a profile. Range: 1–65535. transcode - Enables profile for transcoding. |
| Step 7 | codec codec Example: Device(config-dspfarm-profile)# codec opus | Add a list of codecs that you wish to transcode. |
| Step 8 | maximum sessions sessions | Configures maximum number of transcoding sessions. |
| Step 9 | associate application CUBE | Configures an application to the profile for LTI-based transcoding. |
| Step 10 | no shutdown Example: Device (config-dsp-farm-profile) # no shutdown | Allocates DSP resources and associates with the application. |