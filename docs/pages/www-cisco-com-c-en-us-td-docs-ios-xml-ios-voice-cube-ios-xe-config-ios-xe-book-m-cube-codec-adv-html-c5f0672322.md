---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-cube-codec-adv-html-c5f0672322
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_cube-codec-adv.html
retrieved_at: 2026-08-16T15:49:01.137519+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Codec Support and Restrictions

## Chapter: Codec Support and Restrictions

# Codec Support and Restrictions

## Overview

This chapter provides advanced information about the support of and restrictions for using certain codecs with CUBE . For basic information on how to configure codecs, refer to the Overview section.

### Feature Information

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature
                                          				  Information

Cisco IOS XE Bengaluru 17.6.1a

Opus Codec Negotiation

Cisco IOS XE Amsterdam
                                                17.3.1

Opus audio codec support on CUBE was introduced.

The following commands were introduced or modified as part of Opus codec feature:

codec opus [ profile tag ]

codec profile tag profile

codec preference value codec-type [ profile profile-tag ]

rtp payload-type opus payload-type-number

Secure Communications Interoperability Protocol (SCIP) support in CUBE

(This feature is available in 'preview' mode)

Cisco IOS XE 17.16.1a

This feature introduces SCIP audio and video codec support for secure communication on CUBE.

The following commands were modified as part of the SCIP codec feature:

video codec codec-type

codec preference value codec-type

rtp payload-type codec-audio-scip payload-type-number

rtp payload-type codec-video-scip payload-type-number

Preview Features Disclaimer: In Cisco IOS XE 17.16.1a release, the Secure Communications Interoperability Protocol (SCIP) feature is available in 'preview’ mode as it includes
                                             limited functionality or incomplete software dependencies. Cisco reserves the right to disable preview features at any time
                                             without notice. Cisco Technical Support provides reasonable effort support for features in preview mode. There is no Service
                                             Level Objective (SLO) in response times for features in preview mode; response times may be slow.

## OPUS Codec

The Opus interactive speech and audio codec is designed to handle a wide range of interactive audio applications. This includes
                           Voice over IP, video conferencing, and in-game chat. The OPUS codec also supports live, distributed music performances. It
                           scales from low bitrate narrowband speech at 6 kbps to very high-quality stereo music at 510 kbps. Opus uses both Linear Prediction
                           (LP) and Modified Discrete Cosine Transform (MDCT) algorithms to achieve good compression of both speech and music.

Opus codec is only supported for SIP-SIP call scenarios. It is not supported for TDM-SIP or Analog-SIP flows.

### Opus Codec Configuration

You can configure Opus codec handling with the following dial peer and voice class codec commands:

codec opus [ profile tag ] —The CLI command under dial-peer configuration mode is enhanced:

```
router(config)#dial-peer voice 3002 voip
router(config-dial-peer)#codec opus profile 2
```

codec profile tag profile —The CLI command that is configured under global configuration mode is enhanced to configure opus as a supported codec:

```
router(config)#codec profile 2 opus
router(conf-codec-profile)#fmtp "fmtp:114 maxplaybackrate=16000; sprop-maxcapturerate=16000; maxaveragebitrate=20000; stereo=1; sprop-stereo=0; useinbandfec=0; usedtx=0; cbr=0"
router(conf-codec-profile)#exit
```

codec preference value codec-type [ profile profile-tag ] —The CLI command that is configured under voice class configuration mode is enhanced to configure opus as a preferred codec on the dial-peer:

```
router(config)#voice class codec 80
router(config-class)#codec preference 1 opus profile 79
router(config-class)#exit
```

rtp payload-type [ opus number ] —The CLI command that is configured under dial-peer configuration mode is enhanced to configure opus as a supported payload type:

```
router(config)#dial-peer voice 604 voip
router(config-dial-peer)#rtp payload-type opus 126
```

The default payload-type for opus is set to 114.

The default payload-type for cisco-codec-aacld is set to 112.

The CLI command show call active voice [ brief | compact ] is modified to include details on Opus codec in the command output.

The CLI command show sip-ua calls is modified to include details on Opus codec in the command output.

Opus codec profile configuration is optional and can be used to define the initial offer in delayed offer to early offer call
                                    flows. Else, DSP-specific Opus parameters are used if the DSPFARM profile is configured with Opus codec.

Transcoding between Opus and other codecs is available with PVDM4 DSP cards from Cisco IOS XE Bengaluru 17.6.1a onwards. Calls that require Opus transcoding are dropped by earlier releases.

Opus Codec is supported for both secure and nonsecure calls (RTP-to-RTP, SRTP-to-SRTP, SRTP-to-RTP, and RTP-to-SRTP).

Opus supports several clock rates. Only the highest clock rate of 48000 is advertised in the SDP. The following is a sample
                                    configuration of SDP for Opus codec:

```
m=audio 16000 RTP/AVP 114       a=rtpmap:114 opus/48000/2
```

Opus codec defines the optional media format (fmtp) parameters in a call. CUBE passes through the optional fmtp parameters from one side to the other if an Opus codec is configured on both sides of the call.

Opus codec defines the following fmtp parameters:

maxaveragebitrate

maxplaybackrate

stereo

useinbandfec

usedtx

sprop-maxcapturerate

sprop-stereo

cbr

Dynamic payload interworking is enabled by default on CUBE . Configure asymmetric payload [ full ] if CUBE is not required to handle payload interworking. In this scenario, interworking is handled at the endpoints handling the media.

For interworking scenarios that support Opus codec, SDP Offer-Answer by CUBE must include default fmtp parameters that are
                                    required by DSP. The Offer-Answer includes the DSP-specific default parameters only if DSPFARM is configured with Opus codec.

Example:

```
m=audio 4002 RTP/AVP 114 

a=rtpmap:114 opus/48000/2 a=fmtp:114  maxaveragebitrate=32000

a=maxptime:20
```

### Restrictions

The Opus codec option is not available with the Extended Media Forking (XMF) API.

CUBE doesn't support processing of multiple fmtp lines. If the received SDP has multiple fmtp lines, then only the first fmtp
                                    line is passed in the outbound INVITE.

CUBE DSP doesn't support multiframes OPUS RTP packets for transcoding.

## ISAC Codec Support on CUBE

The iSAC codec is an adaptive VoIP codec specially designed to deliver
                           		wideband sound quality in both low- and high-bit rate applications. The iSAC
                           		codec automatically adjusts the bit-rate for the best quality or a fixed bit
                           		rate can be used if the network characteristics are known. This codec is
                           		designed for wideband VoIP communications. The iSAC codec offers better quality
                           		with reduced bandwidth for sideband applications.

### Restrictions

Low complexity is not supported for the iSAC codec.

## AAC-LD MP4A-LATM Codec Support

As part of this feature, CUBE supports the following:

Accept and send MP4A-LATM codec and corresponding FMTP profiles

Configure MP4A-LATM under dial-peer or under voice-class codec as preferred codec

Pass across real-time transport protocol (RTP) media for MP4A-LATM codec without any interworking

Offer pre-configured FMTP profile for MP4A-LATM for DO-EO (Delayed-Offer to Early-Offer) calls

Offer more than one FMTP profile (each with different payload type number) as mentioned by the offering endpoint, so that
                                 the answering endpoint can choose the best option.

Offer only one instance of MP4A-LATM if media forking is applicable. The offered instance is the first one received in the
                                 offer.

Calculate bandwidth for MP4A-LATM on the basis of either “b=TIAS” attribute or “bitrate” parameter in the FMTP attribute.
                                 If none of them are present in the session description protocol (SDP), the default maximum bandwidth, that is, 128 Kbps will
                                 be used for calculation.

The following CUBE features are supported with the MP4A-LATM codec:

Basic call (audio and video) flow-around and flow-through (FA and FT).

Voice Class Codec support in CUBE with codec filtering

SRTP and SRTCP passthrough for SIP-to-SIP calls

Supplementary services

RSVP

Dynamic payload type interworking for DTMF and codec packets for SIP-to-SIP calls

Media Anti-Trombone with SIP signaling control on CUBE

Support for SIP UPDATE message per RFC 3311

RTP Media Loopback

Media forking for IP based calls using Zephyr recording server

CUBE Mid-call Re-INVITE consumption

Signaling forking (Fastweb multile SIP Early Dialog Support, FA and FT)

Maximum bandwidth-based CAC

Media Policing

Box-to-Box High Availability (B2B HA)

Inbox High Availability (Inbox HA)

### Restrictions for AAC-LD MP4A-LATM Codec Support

CUBE does not support the following:

Codec transcoding between MP4A-LATM and other codecs

Dual-tone Multifrequency (DTMF) interworking with MP4A-LATM codec

Non-SIP-SIP, that is, SIP to other service provider interface (SPI) interworking with MP4A-LATM codec

## (Preview) SCIP Codec

Important

In Cisco IOS XE 17.16.1a release, the Secure Communications Interoperability Protocol (SCIP) feature is available in 'preview’ mode as it includes
                                       limited functionality or incomplete software dependencies. Cisco reserves the right to disable preview features at any time
                                       without notice. Cisco Technical Support provides reasonable effort support for features in preview mode. There is no Service
                                       Level Objective (SLO) in response times for features in preview mode; response times may be slow.

Secure Communication Interoperability Protocol (SCIP) is an application layer protocol that provides end-to-end capability
                           exchange, packetization/de-packetization of media, reliable transport, and payload encryption.

It is an international standard for secure signaling message exchange between end devices to establish a secure traffic session.

SCIP handles packetization/de-packetization of the encrypted media and acts as a tunneling protocol. The CUBE receives encrypted
                           SCIP payloads and transparently transmits them to the other end of the call using RTP.

### SCIP Codec Configuration

You can configure SCIP codec handling with the following dial peer and voice class codec commands:

codec codec —The CLI command configured in dial peer configuration mode is enhanced to support scip audio codec.

```
Router(config)# dial-peer voice 10 voip
Router(config-dial-peer)# codec scip
```

video codec codec —The CLI command configured in dial peer or in voice class configuration mode is enhanced to support scip video codec.

```
Router(config)# dial-peer voice 10 voip
Router(config-dial-peer)# video codec scip
```

```
Router(config)# voice class codec 10
Router(config-class)# video codec scip
```

codec preference value codec-type —The CLI command that is configured in voice class configuration mode is enhanced to support scip as a preferred codec on the dial-peer:

```
Router(config)#voice class codec 10
Router(config-class)#codec preference 1 scip
```

rtp payload-type [ codec-audio-scip number ] —The CLI command that is configured in dial-peer configuration mode is enhanced to support scip audio payload type. The default payload-type for codec-audio-scip is 109:

```
Router(config)#dial-peer voice 60 voip
Router(config-dial-peer)#rtp payload-type codec-audio-scip 105
```

rtp payload-type [ codec-video-scip number ] —The CLI command that is configured in dial-peer configuration mode is enhanced to support scip video payload type. The default payload-type for codec-video-scip is 110:

```
Router(config)#dial-peer voice 60 voip
Router(config-dial-peer)#rtp payload-type codec-video-scip 106
```

The CLI command show dial-peer voice tag is modified to display RTP-payload with SCIP audio and video codec configuration details.

The CLI command show call active voice [brief | compact] is modified to display SCIP codec audio details in the command output.

The CLI command show call active video [brief | compact] is modified to display SCIP codec video details in the command output.

The CLI command show sip-ua calls is modified to display Scip codec details in the command output.

The media name in the SDP is audio or video and the encoding name is scip. The following is a sample configuration of SDP
                                    for Scip codec:

An example for a sample SDP audio and video scip:

```
m=audio 10000 RTP/AVP 96
a=rtpmap:96 scip/8000

m=video 10002 RTP/AVP 96
a=rtpmap:96 scip/90000
```

To maintain the same payload type with SCIP codec in outbound call, it is recommended to configure asymmetric payload [full] in global or dial-peer configuration mode.

To pass-through the exact received RTCP content towards outbound direction, it is recommended to configure rtcp all-pass-through in global configuration mode.

Disable Voice Activity Detection (VAD) while configuring in dial-peer and global configuration modes. By default, VAD is enabled.

The following example shows how to configure VAD for a Voice over IP (VoIP) dial peer in global configuration mode:

```
dial-peer voice 200 voip
 vad
```

Do not configure DTMF in dial-peer or in global configuration mode.

### Limitations

CUBE does not support the following:

Bandwidth-based Call Admission Control (CAC) calculation for SCIP audio and video codec.

Transcoding

DTMF interworking

Multiple audio m-lines

Application or image streams with SCIP codec.

### Syslog Messages

From Cisco IOS XE 17.16.1a , the system generates syslog messages for the following scenarios:

#### Transcoding failure for SCIP calls

When an incoming offer message has only SCIP codec and the outbound dial-peer is configured with a different codec, such a
                                 call fails as the transcoder is not supported. Generates the following syslog message:

SIP-3-TRANSCODER_FAILURE: Failed to attach transcoder for call-id = 3

#### SCIP application m-line rejection

CUBE rejects SDP with SCIP application m-line, as application m-line for payload is not supported, generates the following
                                 syslog message:

SIP-3-APPLICATION_MEDIA_FAILURE: Unsupported application m-line for payload = scip, call-id = 32

CUBE supports only application m-line with H224 payload.

#### SIP (SCIP) to TDM call failures

SIP (SCIP codec) to TDM call fails during offer answer negotiation. Generates the following syslog message:

SIP-3-SIP_TDM_FAILURE: Unsupported codec: scip for TDM to SIP Calls, Call-id: 521

#### DTMF Interworking of Inband

SCIP (Inband DTMF) interworking with SCIP (Out-of band DTMF) is not supported, generates a syslog with the following error
                                 string:

SIP-3-DTMF_INTERWORKING_FAILURE: DTMF interworking failure for dtmf1 = inband-voice, dtmf2 = rtp-nte, call-id = 1

| Feature Name | Releases | Feature
                                          				  Information |
|---|---|---|
| Opus Codec Transcoding | Cisco IOS XE Bengaluru 17.6.1a | Transcoding support was introduced for Opus codec. |
| Opus Codec Negotiation | Cisco IOS XE Amsterdam
                                                17.3.1 | Opus audio codec support on CUBE was introduced. The following commands were introduced or modified as part of Opus codec feature: codec opus [ profile tag ] codec profile tag profile codec preference value codec-type [ profile profile-tag ] rtp payload-type opus payload-type-number |
| Secure Communications Interoperability Protocol (SCIP) support in CUBE (This feature is available in 'preview' mode) | Cisco IOS XE 17.16.1a | This feature introduces SCIP audio and video codec support for secure communication on CUBE. The following commands were modified as part of the SCIP codec feature: video codec codec-type codec preference value codec-type rtp payload-type codec-audio-scip payload-type-number rtp payload-type codec-video-scip payload-type-number |

| Note | Preview Features Disclaimer: In Cisco IOS XE 17.16.1a release, the Secure Communications Interoperability Protocol (SCIP) feature is available in 'preview’ mode as it includes
                                             limited functionality or incomplete software dependencies. Cisco reserves the right to disable preview features at any time
                                             without notice. Cisco Technical Support provides reasonable effort support for features in preview mode. There is no Service
                                             Level Objective (SLO) in response times for features in preview mode; response times may be slow. |
|---|---|

| Note | Opus codec is only supported for SIP-SIP call scenarios. It is not supported for TDM-SIP or Analog-SIP flows. |
|---|---|

| Important | In Cisco IOS XE 17.16.1a release, the Secure Communications Interoperability Protocol (SCIP) feature is available in 'preview’ mode as it includes
                                       limited functionality or incomplete software dependencies. Cisco reserves the right to disable preview features at any time
                                       without notice. Cisco Technical Support provides reasonable effort support for features in preview mode. There is no Service
                                       Level Objective (SLO) in response times for features in preview mode; response times may be slow. |
|---|---|

| Note | CUBE supports only application m-line with H224 payload. |
|---|---|