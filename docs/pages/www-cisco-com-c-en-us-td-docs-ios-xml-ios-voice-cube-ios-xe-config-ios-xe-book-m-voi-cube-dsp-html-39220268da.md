---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-cube-dsp-html-39220268da
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-cube-dsp.html
retrieved_at: 2026-08-16T15:53:33.057484+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: DSP High Availability Support

## Chapter: DSP High Availability Support

# DSP High Availability Support

## DSP High
                        	 Availability Support

Cisco Unified
                           		Border Element (CUBE) DSP High Availability support for SIP-to-SIP calls is
                           		added for Box-to-Box and Inbox configurations. Earlier, calls that required DSP
                           		resources were not checkpointed. As a result, both the media and signaling
                           		sessions were not preserved after switchover resulting in call failure.

DSP HA is
                                       		  supported only for SIP-to-SIP calls.

### Feature Information

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature
                                             					 Name

Releases

Feature
                                             					 Information

DSP HA Support on CUBE

Baseline Fuctionality

Provides
                                             					 DSP High availability support for SIP-to-SIP calls on Box-to-Box and Inbox
                                             					 redundancies.

## Prerequisites for
                        	 DSP High Availability

LTI Transcoding

DSP HA is supported only on the following routers and its corresponding modules:

Cisco ISR G2 series (PVDM3)

Cisco ASR 1000 series (SPA-DSP)

Cisco ISR 4000 series (PVDM4)

Cisco Catalyst 8200 Edge series

Cisco Catalyst 8300 Edge series

The same type
                                 			 and capacity DSP modules must be used in the Active and Standby CUBE devices
                                 			 (box-to-box)

The DSP modules
                                 			 must be installed in the same slot and subslot in the Active and Standby CUBE
                                 			 devices (box-to-box)

The Active and
                                 			 Standby CUBE devices must have the same DSPFARM configurations (box-to-box)

## Features Supported
                        	 with DSP High Availability

Transcoding with
                                 			 Supplementary Services

Voice Class
                                 			 Codec

G.711 in-band
                                 			 -> RFC2833 (RTP-NTE) DTMF interworking variant

SRTP-RTP
                                 			 Interworking (ISR-G2 only)

Fax calls with
                                 			 transcoder invoked for codec mis-match

## Restrictions for
                        	 DSP High Availability

Media
                                 			 flow-around calls are not supported.

SDP passthrough
                                 			 calls are not supported.

Audio
                                 			 Transrating is not supported.

Call Progress Analysis is not supported.

Dolby Noise Reduction (NR) and Acoustic Shock Protection (ASP) are
                                 			 not supported.

All SCCP-based media resources (Conference bridge, Transcoding, HW MTP, and SW MTP) are not supported with Cisco Unified Border
                                 Element High Availability.

## Tips to Troubleshoot

You can use the
                           		following debug commands to troubleshoot DSP HA:

debug voip dsmp
                                 			 all

debug voip dsm
                                 			 all

debug ccsip
                                 			 message

debug voip
                                 			 ipipgw

debug voip
                                 			 ipipgw high-availability

debug voip
                                 			 high-availability all

debug media resource provisioning all

debug
                                 			 dsp-resource-manager flex dspfarm

debug
                                 			 dsp-resource-manager flex function

debug
                                 			 dsp-resource-manager flex error

## Configuration
                        	 Examples for DSP HA

### Active Configuration

```
----------------
voice-card 0
 dsp services dspfarm

dspfarm profile 2 transcode universal
 codec g711ulaw
 codec g711alaw
 codec g729ar8
 codec g729abr8
 maximum sessions 100
 associate application CUBE
```

### Standby Configuration

```
-----------------
voice-card 0
 dsp services dspfarm

dspfarm profile 2 transcode universal
 codec g711ulaw
 codec g711alaw
 codec g729ar8
 codec g729abr8
 maximum sessions 100
 associate application CUBE
```

The following example shows the DSP HA output for the active and
                              		  standby configurations:

```
On Active:

Mang-Active#show dspfarm dsp active
SLOT   DSP VERSION  STATUS CHNL USE   TYPE    RSC_ID BRIDGE_ID PKTS_TXED PKTS_RXED

0            13    39.0.0          UP         1      USED  xcode     1           16558             3005     3007
0            13    39.0.0          UP         1      USED  xcode     1           16559             3004     3005

Total number of DSPFARM DSP channel(s) 1

On Standby:

Mang-Standby#show dspfarm dsp active
SLOT   DSP VERSION  STATUS CHNL USE   TYPE    RSC_ID BRIDGE_ID PKTS_TXED PKTS_RXED

0           13    39.0.0         UP            1     USED   xcode      1         16558             0        0
0           13    39.0.0         UP            1     USED   xcode      1         16559             0        0 

Total number of DSPFARM DSP channel(s) 1
```

| Note | DSP HA is
                                       		  supported only for SIP-to-SIP calls. |
|---|---|

| Feature
                                             					 Name | Releases | Feature
                                             					 Information |
|---|---|---|
| DSP HA Support on CUBE | Baseline Fuctionality | Provides
                                             					 DSP High availability support for SIP-to-SIP calls on Box-to-Box and Inbox
                                             					 redundancies. |