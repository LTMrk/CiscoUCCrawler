---
doc_id: www-cisco-com-c-en-us-support-docs-voice-h323-14069-codec-complexity-html-7a69e117a0
source_url: https://www.cisco.com/c/en/us/support/docs/voice/h323/14069-codec-complexity.html
retrieved_at: 2026-08-20T23:24:36.087696+00:00
---

Understanding Codecs: Complexity, Hardware Support, MOS, and Negotiation

# Understanding Codecs: Complexity, Hardware Support, MOS, and Negotiation

Updated: February 2, 2006

Document ID: 14069

Contents

## Contents

## Introduction

This document provides an overview of the different coder-decoders (codecs) used with Cisco IOS ® Voice over IP (VoIP) gateways. In Cisco IOS Software Releases earlier than 12.0(5)T, VoIP gateways supports only the G.729 and G.711 codecs and only one voice/fax-relay call per digital signal processor (DSP). With the introduction of Cisco IOS Software Release 12.0(5)T, Cisco VoIP gateways support a larger number of codecs and DSP modules. They can also support up to four voice/fax-relay calls per DSP.

For more information on DSPs, refer to Voice Hardware: C542 and C549 Digital Signal Processor (DSP) .

The DSP Calculator tool ( registered customers only) determines the DSP requirements for the Cisco 1751, 1760, 2600XM, 2691, 2800, 3700, and 3800 series router platforms and provides PVDM provisioning suggestions as output. The tool calculates the DSP requirements based on the interface modules, codec configurations, transcoding channels, and conference sessions provided as input. This tool supports different Cisco IOS Software releases valid for the Cisco 1751, 1760, 2600XM, 2691, 2800, 3700, and 3800 platforms.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

This document is not restricted to specific software and hardware versions.

### Conventions

For more information on document conventions, refer to the Cisco Technical Tips Conventions .

## Codec Complexity

Some codec compression techniques require more processing power than others. Codec complexity is broken into two categories named medium and high complexity.

Medium complexity allows the C549 DSPs to process up to four voice/fax-relay calls per DSP and the C5510 DSPs to process up to eight voice/fax-relay calls per DSP.

High complexity allows the C549 DSPs to process up to two voice/fax-relay calls per DSP and the C5510 DSPs to process up to six voice/fax-relay calls per DSP.

Note: The difference between medium and high complexity codecs is the amount of CPU utilization necessary to process the codec algorithm, and therefore, the number of voice channels that can be supported by a single DSP. For this reason, all the medium complexity codecs can also be run in high complexity mode, but fewer (usually half) of the channels are available per DSP.

Note: Fax-relay (2400 bps, 4800 bps, 7200 bps, 9600 bps, 12 kbps, and 14.4 kbps) can use medium or high complexity codecs.

On platforms that support the C549 DSP technology, the codec complexity is configured under the voice-card (for example, the 2600/3600/VG-200 High Density Voice Network Module). Some platforms support only high complexity because they have enough DSPs onboard to support all T1/E1 channels that use the high complexity mode. In order to specify call density and codec complexity according to the codec standard that is used, use the codec complexity command in voice-card configuration mode.

An example of the complexity configuration is shown here:

```
Cisco-router # configure terminal Enter configuration commands, one per line. End with CNTL/Z.
Cisco-router(config)# voice-card 1 Cisco-router(config-voicecard)# codec complexity ? high 	Set codec complexity high. High complexity, lower call density.
	medium 	Set codec complexity medium. Mid range complexity and call density.
	<cr>
Cisco-router(config-voicecard)# codec complexity high
```

On platforms that support C5510 DSP technology, an additional option of flex complexity is available. When you use flex complexity, up to sixteen calls can be completed per DSP. The number of supported calls varies from six to sixteen and is based on the codec used for a call.

An example of the configuration is shown here:

```
Cisco-router# configure terminal Enter configuration commands, one per line.  End with CNTL/Z.
Cisco-router(config)# voice-card 1 Cisco-router(config-voicecard)# codec complexity ? flex    Set codec complexity Flex.  Flex complexity, higher call density.
  high    Set codec complexity high.  High complexity, lower call density.
  medium  Set codec complexity medium.  Mid range complexity and call density.
  <cr>

Cisco-router(config-voicecard)# codec complexity flex
```

This is an excerpt from the show running-config output to determine which complexity is configured:

```
!voice-card 1
  codec complexity high
!
```

This table lists the codec support for various Cisco router platforms.

## Codec Mean Opinion Score (MOS)

Each codec provides a certain quality of speech. The quality of transmitted speech is a subjective response of the listener. A common benchmark used to determine the quality of sound produced by specific codecs is the mean opinion score (MOS). With MOS, a wide range of listeners judge the quality of a voice sample (corresponds to a particular codec) on a scale of 1 (bad) to 5 (excellent). The scores are averaged to provide the MOS for that sample. This table shows the relationship between codecs and MOS scores.

Although it can seem logical from a financial standpoint to convert all calls to low-bit rate codecs to save on infrastructure costs, exercise additional care when you design voice networks with low-bit rate compression. There are drawbacks to compressing voice. One of the main drawbacks is signal distortion due to multiple encodings (called tandem encodings). For example, when a G.729 voice signal is tandem encoded three times, the MOS score drops from 3.92 (very good) to 2.68 (unacceptable). Another drawback is codec-induced delay with low bit-rate codecs.

## G.729 Codec Issues

These two sections clarify many of the common compatibility issues related to the G.729 (8 kbps) codec implementation.

### Cisco Pre-IETF G.729 and Standardized G.729 Implementation

Cisco released a G.729 pre-Internet Engineering Task Force (IETF) codec implementation before the G.729 codec was standardized. In Cisco IOS 12.0(5)T and later, the default bit-ordering of the G.729 codec is changed from the pre-IETF standard to the IETF standardized format. The two formats do not interoperate and result in an unintelligible "gulping sound" to the end-users.

For compatibility with other vendor's G.729 implementations, Cisco IOS Software Release 12.0.5T and later default to the standardized implementation of G.729. For backwards compatibility with Cisco IOS software releases earlier than Cisco IOS Software Release 12.0.5T, enable the pre-IETF G.729 implementation with this command:

```
maui-vgw-01(config)# dial-peer voice 100 voip maui-vgw-01(config-dial-peer)# codec g729r8 pre-ietf
```

The pre-ietf option in this command is not supported in Cisco IOS Release 12.2 and later.

### High Complexity: G.729, G729 Annex-B & Medium Complexity: G.729A, G.729A Annex-B

G.729 is a high complexity algorithm, and G.729A (also known as G.729 Annex-A) is a medium complexity variant of G.729 with slightly lower voice quality. All platforms that support G.729 also support G.729A.

On Cisco IOS gateways, the variant to use (G.729 or G.729A) is related to the codec complexity configuration on the voice card. It does not show up explicitly in the Cisco IOS command line interface (CLI) codec choice. For example, the CLI does not show g729ar8 ("a" code) as a codec option. However, if the voice-card is defined as medium-complexity, then the g729r8 option is the G.729A codec.

Note: For the MC3810, in Cisco IOS Software releases earlier than 12.0.7XK, there is an explicit CLI choice between twenty-four channels of G.729A or twelve channels of G.729.

G.729 Annex-B is a high complexity algorithm, and G.729A Annex-B is a medium complexity variant of G.729 Annex-B with slightly lower voice quality. The difference between the G.729 and G.729 Annex-B codec is that the G.729 Annex-B codec provides built-in IETF voice activity detection (VAD) and Comfort Noise Generation (CNG).

These G.729 codec combinations interoperate:

G.729 and G.729A

G.729 and G.729

G.729A and G.729A

G.729 Annex-B and G.729A Annex-B

G.729 Annex-B and G.729 Annex-B

G.729A Annex-B and G.729A Annex-B

Note: There is no explicit way to configure G.729A on the Cisco 2600/3600/VG-200 NM-1V and NM-2V (voice network module) since these voice modules do not support the "codec complexity" configuration supported on the NM-HDV (High Density Voice Network Module). However, if a G.729A call is set up by another endpoint that terminates on the NM-1V/2V, the call is successfully connected.

## G.723.1 Codec Issues

There are two versions of G.723.1 called Annex-A and non Annex-A. These versions do not interoperate. G.723.1 Annex-A includes a built-in IETF VAD algorithm and CNG.

Also, in Cisco IOS Software Release 12.0(5)T and later, the G.723.1 codec is supported with a 5.3 kbps and 6.3 kbps rate. When a Cisco VoIP gateway sets up a call between devices that use G723.1, it is concerned only that the far-end uses G.723.1. Neither side is concerned with the 5.3 kbps or 6.3 kbps rate that is supported by the other side. This means that, while it is beneficial to have both sides support the same rate, it is possible that one side transmits at 5.3 kbps and the reverse direction transmits at 6.3 kbps. The speed that is used is viewed with the show call active voice brief command as shown here:

```
Cisco-router# show call active voice brief 47 : 494514hs.1 +473 pid:0 Answer active
tx:210/5040 rx:219/4380
IP 5.5.0.1:16534 rtt:3ms pl:890/0ms lost:0/0/0 delay:70/70/70ms g723r63
47 : 494514hs.2 +473 pid:1 Originate 4750001 active
  TX:230/1840 rx:230/8280
  Tele 2/0:0 (35): TX:6870/2290/0ms g723r63 !--- In this example the G.723.1 is operating at 6.3 kbps. noise:0 acom:0 i/0:-79/-5 dBm
```

The G.723.1 standard allow stations to change rates between 6.3 kbps and 5.3 kbps during a call to adjust to network traffic loads. The Cisco VoIP gateways do not support this functionality. But they do understand if the remote device (such as a Cisco IP Phone) transmits at a different rate than was originally negotiated.

These G.723.1 codec combinations interoperate:

G.723.1 (5.3 kbps) and G.723.1 (6.3 kbps)

G.723.1 (5.3 kbps) and G.723.1 (5.3 kbps)

G.723.1 (6.3 kbps) and G.723.1 (6.3 kbps)

G.723.1 Annex-A (5.3 kbps) and G.723.1 Annex-A (6.3 kbps)

G.723.1 Annex-A (5.3 kbps) and G.723.1 Annex-A (5.3 kbps)

G.723.1 Annex-A (6.3 kbps) and G.723.1 Annex-A (6.3 kbps)

## Codec Negotiation

With the introduction of Cisco IOS Software Release 12.0(5)T, Cisco VoIP gateways support the codec negotiation feature. This feature provides the ability for a Cisco VoIP gateway to connect to other VoIP devices without necessarily knowing which codec is used for a call-setup. Also, this feature allows Cisco VoIP gateways to dynamically adjust to changes on remote devices. As long as the codec used by the remote VoIP device matches the capabilities-list of the Cisco VoIP gateway, the VoIP call is completed. Codec negotiation is supported on both the C542 and C549 DSPs. To specify a list of preferred codecs to use on a dial peer, use the codec preference command in voice-class configuration mode.

This example shows how to configure codec negotiation:

```
Cisco-router# configure terminal Cisco-router(config)# voice class codec 1 !--- This sets up class 1 to be assigned to the dial peer. Cisco-router(config-class)# codec preference 1 g723r63 Cisco-router(config-class)# codec preference 2 g729br8 Cisco-router(config-class)# codec preference 3 g711ulaw Cisco-router(config-class)# codec preference 4 g726r32 bytes 240 !--- These commands define the preferred codec list using 1,2,3, !--- and 4 to set the preference. Cisco-router(config)#dial-peer voice 1 voip
Cisco-router(config-dial-peer)# voice-class codec 1 !--- This assigns voice-class codec 1 to the dial-peer Cisco-router(config-dial-peer)#destination-pattern 4723155
Cisco-router(config-dial-peer)#session target ipv4:192.168.100.1
```

## Related Error Messages

### %DSPRM-5-SETCODEC:

The %DSPRM-5-SETCODEC error is due to a high complexity codec configured on a VoIP dial-peer while it still has the voice card set for the default of medium complexity. To fix this problem, you must remove the ds0-group configuration from the controller which causes the voice-port to be removed. After you remove the ds0-group, follow the procedures earlier in this document to change the complexity.

## Related Information

| Medium Complexity (4 calls / dsp) | High Complexity ( 2 calls / dsp) |
|---|---|
| G.711 (a-law and m -law) | G.728 |
| G.726 (all versions) | G.723 (all versions) |
| G.729a, G.729ab (G.729a AnnexB) | G.729, G.729b (G.729-AnnexB) |
| Fax-relay | Fax-relay |

| Codec | 1751/1760 | 26xx/36xx NM-1V/2V | 26xx/36xx NM-HDV | 3700 | 3810 | AS5300 AS5800 | AS5350 AS5400 | 7200 | 7500 | CMM 24FXS | CMM 6T1/E1 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| G.711 a-law and u-law PCM (64 kbps) | 12.0.5XQ1 | Yes | 12.0.5XK1 | Yes | 12.0.7XK | Yes | Yes | 12.0.5XE3 | 12.1.3T | Yes | Yes |
| G.726 ADPCM (32, 24,16 kbps) | 12.1.2T | 12.0.5T | 12.0.5XK1 | Yes | 12.0.7XK | Yes | No | 12.0.5XE3 | 12.1.3T | No | No |
| G.728 LD-CELP (16 kbps) | Yes | 12.0.5T | 12.0.5XK1 | Yes | 12.0.7XK | Yes | No | 12.0.5XE3 | 12.1.3T | No | No |
| G.729 CS-ACELP (8 kbps) | 12.1.2T | Yes | 12.0.5XK1 | Yes | 12.0.7XK | Yes | No | 12.0.5XE3 | 12.1.3T | No | No |
| G.729a CS-ACELP (8 kbps) | 12.0.5XQ1 | Yes | 12.0.5XK1 | Yes | 12.0.7XK | Yes | Yes | 12.0.5XE3 | 12.1.3T | Yes | Yes |
| G.729 Annex-B (8 kbps) [VAD] | Yes | 12.0.5T | 12.0.5XK1 | Yes | 12.0.7XK | Yes | No | 12.0.5XE3 | 12.1.3T | No | No |
| G.729a Annex-B (8 kbps) | Yes | Yes | 12.0.5XK1 | Yes | 12.0.7XK | Yes | Yes | 12.0.5XE3 | 12.1.3T | Yes | Yes |
| G.723.1 MP-MLQ (6.3 kbps) | 12.1.2T | 12.0.5T | 12.0.5XK1 | Yes | 12.0.7XK | Yes | Yes | 12.0.5XE3 | 12.1.3T | No | No |
| G.723.1 ACELP (5.3 kbps) | 12.1.2T | 12.0.5T | 12.0.5XK1 | Yes | 12.0.7XK | Yes | Yes | 12.0.5XE3 | 12.1.3T | No | No |
| G.723.1 Annex-A MP-MLQ (6.3 kbps) | 12.1.2T | 12.0.5T | 12.0.5XK1 | Yes | 12.0.7XK | Yes | Yes | 12.0.5XE3 | 12.1.3T | No | No |
| G.723.1 Annex-A ACELP (5.3 kbps) | 12.1.2T | 12.0.5T | 12.0.5XK1 | Yes | 12.0.7XK | Yes | Yes | 12.0.5XE3 | 12.1.3T | No | No |
| Clear Channel | 12.3(2)XF, 12.3(11)T | Yes | Yes | Yes | 12.3(11)T |  |  | Yes | Yes | No | No |

| Codec Compression Method |
|---|
| PCM = Pulse Code Modulation |
| ADPCM = Adaptive Differential Pulse Code Modulation |
| LDCELP = Low-Delay Code Excited Linear Prediction |
| CS-ACELP = Conjugate-Structure Algebraic-Code-Excited Linear-Prediction |
| MP-MLQ = Multi-Pulse, Multi-Level Quantization |
| ACELP = Algebraic Code Excited Linear Prediction |

| Compression Method | Bit Rate (kbps) | MOS Score | Compression Delay (ms) |
|---|---|---|---|
| G.711 PCM | 64 | 4.1 | 0.75 |
| G.726 ADPCM | 32 | 3.85 | 1 |
| G.728 LD-CELP | 16 | 3.61 | 3 to 5 |
| G.729 CS-ACELP | 8 | 3.92 | 10 |
| G.729 x 2 Encodings | 8 | 3.27 | 10 |
| G.729 x 3 Encodings | 8 | 2.68 | 10 |
| G.729a CS-ACELP | 8 | 3.7 | 10 |
| G.723.1 MP-MLQ | 6.3 | 3.9 | 30 |
| G.723.1 ACELP | 5.3 | 3.65 | 30 |