---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-cube-codec-basic-html-3e351556bb
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_cube-codec-basic.html
retrieved_at: 2026-08-16T15:44:56.400274+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Introduction to Codecs

## Chapter: Introduction to Codecs

# Introduction to Codecs

## Overview

A codec is a device or software capable of encoding or decoding a digital data stream or signal. Audio codecs can encode or
                           decode a digital data stream of audio. Video codecs encode or decode digital video streams.

This chapter describes the basics of encoding digital voice samples using codecs and how to configure them.

Cisco Unified Border Element (CUBE) uses codecs to compress digital voice samples to reduce bandwidth usage per call.

Configuring codecs allows the CUBE to act as a demarcation point on a VoIP network and allows calls on a specific dial peer to be established only if the desired
                           codec criteria are satisfied. Also, preferences can be used to determine which codecs are selected over others.

If codec filtering is not required, CUBE also supports transparent codec negotiations. The codec filtering enables negotiations between endpoints with CUBE leaving the codec information untouched.

The following illustrations show how codec negotiation is performed on CUBE . Two VoIP clouds must be interconnected. In this scenario, both VoIP 1 and VoIP 2 networks have G.711 a-law that is configured
                           as the preferred codec.

In the first example, the CUBE router is configured to use the G.729a codec. This can be done by using the appropriate codec command on both VoIP dial peers.
                           When a call is set up, CUBE accepts only G.729a calls, thus influencing the codec negotiation.

In the second example, the CUBE dial peers are configured with a transparent codec and this leaves the codec information that is contained within the call
                           signaling untouched. Because both VoIP 1 and VoIP 2 have G.711 a-law as their first choice, the resulting call is a G.711
                           a-law call.

H.323 protocol is no longer supported from Cisco IOS XE Bengaluru 17.6.1a onwards. Consider using SIP for multimedia applications.

## Restrictions

While using the voice-class codec transparent, only the offer is passed transparently (without filtering). Codec filtering
                           is carried out on SDP content in ANSWER messages. Only the first codec in the offer list is included in the outbound message.

You can use 'pass-thru content sdp,' if you do not want to involve CUBE in the codec negotiation.

## Media Transmission

When a VoIP call is established, the digitized audio and video samples must be transmitted. These samples are often called
                           the media payload. The following media protocols specify the standards related to transmission of media payload in VoIP networks:

Real-Time Transport Protocol (RTP)—RTP is a Layer 4 protocol that is encapsulated inside UDP segments. RTP carries the actual
                                 media voice samples in a call.

Real-Time Control Protocol (RTCP)—RTCP is a companion protocol to RTP. Both RTP and RTCP operate at Layer 4 and are encapsulated
                                 in UDP. RTP and RTCP typically use UDP ports 16384 to 32767, though these ranges may vary according to hardware platform.
                                 RTP uses the even port numbers in that range, whereas RTCP uses the odd port numbers. While RTP is responsible for carrying
                                 the media payload, RTcP carries information about the RTP stream such as latency, jitter, packets, and octets sent and received.

Compressed RTP (CRTP)—One of the challenges with RTP is its overhead. Specifically, the combined IP, UDP, and RTP headers
                                 are approximately 40 bytes in size, whereas a common voice payload size on a VoIP network is only 20 bytes, which includes
                                 20 ms of voice by default. In that case, the header is twice the size of the payload. cRTP is used for RTP header compression
                                 and can reduce the 40-byte header to 2 or 4 bytes in size (depending on whether UDP checksums are in use), as shown in the
                                 figure below.

Secure RTP (SRTP)—To help prevent an attacker from intercepting and decoding or possibly manipulating media packets, SRTP
                                 encrypts RTP packets. In addition, SRTP provides message authentication, integrity checking, and protection against replay
                                 attacks.

VPN technology is used to protect traffic between sites. Sending SRTP via a VPN tunnel results in the encryption of traffic
                                 that is already secure, adding significant overhead and bandwidth needs. It is recommended that SRTP is used for media traffic,
                                 and that is excluded from VPN tunnels. By encrypting media directly on communicating endpoints, it is possible to realise
                                 a more secure solution, that requires less bandwidth and infrastructure investment.

## Voice Activity
                        	 Detection

Voice Activity
                           		Detection (VAD) is a technology that works with the human nature of voice
                           		conversations, mainly that one person listens while the other talks. VAD
                           		classifies traffic as speech, unknown, and silence. Speech and unknown payloads
                           		are transported, but silence is dropped. This accounts for approximately 30
                           		percent savings in bandwidth over time.

VAD can significantly reduce the amount of bandwidth that is required by a media stream. However, VAD has a few negative attributes
                           that must be considered. Because no packets are sent during silence, the listener can get the impression that the talker has
                           been disconnected. Another characteristic is that it takes a moment for VAD to recognize the speech as having started again,
                           and as a result, the first part of the sentence can be clipped. This can be annoying to the listening party. Music on Hold
                           (MoH) and fax can also cause VAD to become ineffective because the media stream is constant.

VAD is enabled by default in CUBE dial peers as long as the codec selected supports it. VAD can be disabled at the VoIP dial
                           peer using the no vad command. Some codecs, such as G.729b and G.729ab, support Comfort Noise Generation (CNG). When VAD is enabled, white noise
                           is played to the listener during times when no packets are received. This leads the listener to believe that call is still
                           connected. Cisco IP Phones and most gateways support CNG.

G.729 Annex-B and
                           		G.723.1 Annex-A include an integrated VAD function, but otherwise performs the
                           		same as G.729 and G.723.1, respectively.

## VoIP Bandwidth
                        	 Requirements

The amount of bandwidth that is required varies by the codec and the transmission media. Two events require bandwidth. The
                           media stream itself requires bandwidth between 17–106 kbps depending on codec, header compression, and Layer 2 and 3 headers.
                           In addition, call signaling must be taken into account. While bandwidth required by call signaling is much smaller, problems
                           occur when this traffic is dropped in congested networks.

The table below gives calculations for the default voice payload sizes in Cisco Unified Communications Manager or CUBE. For
                           additional calculations, including different voice payload sizes and other protocols, use the TAC Voice Bandwidth Codec Calculator (registered customers only). For an explanation of each of the column headings, see the table below.

OPUS

## Supported Audio
                        	 and Video Codecs

The CUBE is required to support the codec used between endpoints. g729r8 is supported by default. All other codecs have to be configured.
                           The following codecs are supported:

Important

In Cisco IOS XE 17.16.1a release, the Secure Communications Interoperability Protocol (SCIP) feature  is available in 'preview’ mode as it includes
                                       limited functionality or incomplete software dependencies. Cisco reserves the right to disable preview features at any time
                                       without notice. Cisco Technical Support provides reasonable effort support for features in preview mode. There is no Service
                                       Level Objective (SLO) in response times for features in preview mode; response times may be slow.

aacld

AACLD 90000 bps

clear-channel

Clear
                                       				  Channel 64000 bps (No voice capabilities: data transport only)

g711alaw

G.711 A Law
                                       				  64000 bps

g711ulaw

G.711 u Law 64000 bps

g722-64

G722-64K
                                       				  64000 bps

g723ar53

G.723.1
                                       				  ANNEX-A 5300 bps (contains built-in VAD that cannot be disabled)

g723ar63

G.723.1
                                       				  ANNEX-A 6300 bps (contains built-in VAD that cannot be disabled)

g723r53

G.723.1
                                       				  5300 bps

g723r63

G.723.1
                                       				  6300 bps

g726r16

G.726 16000
                                       				  bps

g726r24

G.726 24000
                                       				  bps

g726r32

G.726 32000
                                       				  bps

g728

G.728 16000
                                       				  bps

g729br8

G.729
                                       				  ANNEX-B 8000 bps (contains built-in VAD that cannot be disabled)

g729r8

G.729 8000 bps

gsmamr-nb

GSM AMR-NB
                                       				  4750 to 12200 bps (contains built-in VAD that cannot be disabled)

ilbc

iLBC 13330
                                       				  or 15200 bps

isac

iSAC 10 to
                                       				  32 kbps (variable bit-rate)

mp4a-latm

MP4A-LATM
                                       				  upto 128 kbps

opus

Opus upto 510 kbps

transparent

Transparent; uses the endpoint codec

scip

SCIP audio codec

(This feature is available in 'preview' mode)

h261

Video Codec H261

h263

Video Codec H263

h263+

Video Codec H263+

h264

Video Codec H264

mpeg4

Video Codec
                                       				  MPEG-4 ISO/IES 14496-2

scip

Video Codec SCIP

(This feature is available in 'preview' mode)

### Configure Codecs

## Configure Voice Class Codec and Preference Lists

Preferences determine which codecs are selected over others.

A codec voice class is a construct within which a codec preference order is defined. A codec voice class can then be applied
                              to a dial peer, which then follows its preference order.

### SUMMARY STEPS

- enable

- configure terminal

- voice class codec tag

- Add the following for each audio codec you want to configure in the voice class:

- codec preference value codec-type [ profile profile-tag ]

- codec preference value codec-type [ bytes payload-size fixed-bytes ]

- codec preference value isac [ mode {adaptive | independent} [ bit-rate value framesize { 30 | 60 } [fixed] ]]

- codec preference value ilbc [ mode frame-size [ bytes payload-size ]]

- codec preference value mp4-latm [ profile tag ]

- codec preference value scip

- Add the following to configure a video codec:

- video codec codec

- exit

- dial-peer voice number voip

- voice-class codec tag offer-all

- end

### DETAILED STEPS

Step 1

enable

### Example:

```
Device> enable
```

Enables
                                          				privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Device> configure terminal
```

Enters global
                                          				configuration mode.

Step 3

voice class codec tag

### Example:

```
Device(config)# voice class codec 10
```

Enters
                                          				voice-class configuration mode for the specified codec voice class.

Step 4

Add the following for each audio codec you want to configure in the voice class:

- codec preference value codec-type [ profile profile-tag ]

- codec preference value codec-type [ bytes payload-size fixed-bytes ]

- codec preference value isac [ mode {adaptive | independent} [ bit-rate value framesize { 30 | 60 } [fixed] ]]

- codec preference value ilbc [ mode frame-size [ bytes payload-size ]]

- codec preference value mp4-latm [ profile tag ]

- codec preference value scip

Configure a codec within the voice class and specify a preference for the codec. This becomes part of a preference list.

The SCIP feature in Cisco IOS XE 17.16.1a release is available in 'preview’ mode as it includes limited functionality or incomplete software dependencies.

Step 5

Add the following to configure a video codec:

- video codec codec

### Example:

```
video codec h261
```

### Example:

```
video codec scip
```

Step 6

exit

### Example:

```
Device(config-class)# exit
```

Exits the
                                          				current mode.

Enter your password if prompted.

Step 7

dial-peer voice number voip

### Example:

```
Device(config)# dial-peer voice 1 voip
```

Enters dial
                                          				peer configuration mode for the specified VoIP dial peer.

Step 8

voice-class codec tag offer-all

### Example:

```
Device(config-dial-peer)# voice-class codec 10
```

Applies the previously configured voice class and associated codecs to a dial peer.

The offer-all keyword allows the device to offer all codecs configured in a codec voice class.

Step 9

end

### Example:

```
Device(config-dial-peer)# end
```

Returns to
                                          				privileged EXEC mode.

## Configure Audio and Video Codecs at the Dial Peer Level

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice number voip

- Enter one of the following to configure audio codec:

- codec codec [ bytes payload-size fixed-bytes ]

- codec isac [ mode {adaptive | independent} [ bit-rate value framesize { 30 | 60 } [fixed] ]]

- codec ilbc [ mode frame-size [ bytes payload-size ]]

- codec mp4-latm [ profile tag ]

- codec opus [ profile tag ]

- codec scip

- Add the following to configure a video codec:

- video codec codec

- (Optional) Enter one of the following to configure RTP payload type:

- rtp payload-type cisco-codec-isac number

- rtp payload-type cisco-codec-ilbc number

- rtp payload-type cisco-codec-video-h263+ number

- rtp payload-type cisco-codec-video-h264 number

- rtp payload-type opus number

- rtp payload-type codec-audio-scip number

- rtp payload-type codec-video-scip number

- end

### DETAILED STEPS

Step 1

enable

### Example:

```
Device> enable
```

Enables
                                          				privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Device> configure terminal
```

Enters global
                                          				configuration mode.

Step 3

dial-peer voice number voip

### Example:

```
Device(config)# dial-peer voice 1 voip
```

Enters dial
                                          				peer configuration mode for the specified VoIP dial peer.

Step 4

Enter one of the following to configure audio codec:

- codec codec [ bytes payload-size fixed-bytes ]

- codec isac [ mode {adaptive | independent} [ bit-rate value framesize { 30 | 60 } [fixed] ]]

- codec ilbc [ mode frame-size [ bytes payload-size ]]

- codec mp4-latm [ profile tag ]

- codec opus [ profile tag ]

- codec scip

### Example:

```
Device(config-dial-peer)# codec g711alaw
```

### Example:

```
Device(config-dial-peer)# codec isac mode independent
```

Configures an audio codec at the dial peer level.

By default, g729r8, 20-byte payload is configured.

Step 5

Add the following to configure a video codec:

- video codec codec

### Example:

```
Device(config-dial-peer)# video codec h261
```

### Example:

```
Device(config-dial-peer)# video codec scip
```

Configures a video codec at the dial peer level.

Step 6

(Optional) Enter one of the following to configure RTP payload type:

- rtp payload-type cisco-codec-isac number

- rtp payload-type cisco-codec-ilbc number

- rtp payload-type cisco-codec-video-h263+ number

- rtp payload-type cisco-codec-video-h264 number

- rtp payload-type opus number

- rtp payload-type codec-audio-scip number

- rtp payload-type codec-video-scip number

### Example:

```
Device(config-dial-peer)# rtp payload-type opus 114
```

The SCIP feature in Cisco IOS XE 17.16.1a release is available in 'preview’ mode as it includes limited functionality or incomplete software dependencies.

Step 7

end

### Example:

```
Device(config-dial-peer)# end
```

Returns to
                                          				privileged EXEC mode.

## Verify an Audio Call

### SUMMARY STEPS

- show call active voice [compact]

- show call active voice [brief]

### DETAILED STEPS

Step 1

show call active voice [compact]

Displays a
                                          				compact version of call information for voice calls in progress.

### Example:

```
Router# show call active voice compact <callID>  A/O FAX T<sec> Codec       type        Peer Address       IP R<ip>:<udp>
Total call-legs: 2
        23 ANS     T3     mp4a-latm   VOIP        Psipp          9.45.33.11:57210
        24 ORG     T3     mp4a-latm   VOIP        P123           9.45.33.11:57210
```

### Example:

```
Router# show call active voice compact <callID>   A/O FAX T<sec> Codec    type    Peer Address    IP R<ip>:<udp> 
Total call-legs: 2
58 ANS     T11          g711ulaw   VOIP     Psipp 2001:......:230A:6080
59 ORG     T11          g711ulaw   VOIP     P5000110011       10.13.37.150:6090
```

### Example:

```
Router# show call active voice compact <callID>  A/O FAX  T<sec> Codec   type   Peer Address  IP R<ip>:<udp>     VRF
Total call-legs: 2
  350      ANS       T6     scip   VOIP    Psipp        10.43.33.45:6006    NA
  351      ORG       T6     scip   VOIP    P8888        10.43.33.45:6002    NA
```

Step 2

show call active voice [brief]

Displays a brief summary of call information for voice calls in progress.

### Example:

```
Router# show call active voice brief Telephony call-legs: 0
SIP call-legs: 2
H323 call-legs: 0
Call agent controlled call-legs: 0
SCCP call-legs: 0
STCAPP call-legs: 0
Multicast call-legs: 0
Total call-legs: 2
121C : 19 2737820ms.1 (*11:50:45.045 UTC Tue Jul 23 2024) +1010 pid:666 Answer 1234 active
 dur 00:00:12 tx:0/0 rx:0/0 dscp:0 media:0 audio tos:0xB8 video tos:0x0
 IP 10.64.86.70:6008 SRTP: off rtt:0ms pl:0/0ms lost:0/0/0 delay:0/0/0ms scip TextRelay: off Transcoded: No ICE: Off
 media inactive detected:n media contrl rcvd:n/a timestamp:n/a
 long duration call detected:n long duration call duration:n/a timestamp:n/a
 LostPacketRate:0.00 OutOfOrderRate:0.00
 LocalUUID:37110991b54051679f675479a6e93de7
 RemoteUUID:e74b1bf0678e5209915c03a9660cb00f
 VRF: NA
121C : 20 2737820ms.2 (*11:50:45.045 UTC Tue Jul 23 2024) +1010 pid:777 Originate 1111 active
 dur 00:00:12 tx:0/0 rx:0/0 dscp:0 media:0 audio tos:0xB8 video tos:0x0
 IP 10.64.86.70:6004 SRTP: off rtt:0ms pl:0/0ms lost:0/0/0 delay:0/0/0ms scip TextRelay: off Transcoded: No ICE: Off
 media inactive detected:n media contrl rcvd:n/a timestamp:n/a
 long duration call detected:n long duration call duration:n/a timestamp:n/a
 LostPacketRate:0.00 OutOfOrderRate:0.00
 LocalUUID:e74b1bf0678e5209915c03a9660cb00f
 RemoteUUID:37110991b54051679f675479a6e93de7
 VRF: NA
Telephony call-legs: 0
SIP call-legs: 2
H323 call-legs: 0
Call agent controlled call-legs: 0
SCCP call-legs: 0
STCAPP call-legs: 0
Multicast call-legs: 0
Total call-legs: 2
```

## Configuration
                        	 Examples for Codecs

### Example:
                              		  Configuring a Codec at Dial-Peer Level

```
Device(config)# dial-peer voice 5550199 voip Device(config-dial-peer)# incoming called-number 5550199 Device(config-dial-peer)# codec g711ulaw Device(config-dial-peer)# end
```

### Example:
                              		  Configuring a Codec Preference List and Applying it to a Dial Peer

```
Device(config)# voice class codec 100 Device(config-class)# codec preference 1 g711ulaw Device(config-class)# exit Device(config)# dial-peer voice 10 voip Device(config-dial-peer)# voice-class codec 100 Device(config-dial-peer)# end
```

### Example: Configuring a Codec Profile, Codec Preference List and Applying it to a Dial Peer for Opus Codec

```
Device(config)#codec profile 79 opus
Device(conf-codec-profile)#fmtp "fmtp:114 maxplaybackrate=16000; sprop-maxcapturerate=16000; maxaveragebitrate=20000; stereo=1; sprop-stereo=0; useinbandfec=0; usedtx=0"
Device(conf-codec-profile)#exit

Device(config)#voice class codec 80
Device(config-class)#codec preference 1 opus profile 79
Device(config-class)#exit

Device(config)#dial-peer voice 604 voip
Device(config-dial-peer)#rtp payload-type opus 126
Device(config-dial-peer)#voice-class codec 80 offer-all
Device(config-dial-peer)#exit
```

### Example: Configure SCIP audio codec, and SCIP video codec in voice class and apply it to a Dial Peer

The SCIP feature in Cisco IOS XE 17.16.1a release is available in 'preview’ mode as it includes limited functionality or incomplete software dependencies.

```
Device(config)#voice class codec 1
Device(config-class)#codec preference 1 scip
Device(config-class)#video codec scip
Device(config-class)#exit

Device(config)#dial-peer voice 300 voip
Device(config-dial-peer)#rtp payload-type codec-audio-scip 105
Device(config-dial-peer)#rtp payload-type codec-video-scip 106
Device(config-dial-peer)#voice-class codec 1
Device(config-dial-peer)#exit
```

| Note | H.323 protocol is no longer supported from Cisco IOS XE Bengaluru 17.6.1a onwards. Consider using SIP for multimedia applications. |
|---|---|

| Note | You can use 'pass-thru content sdp,' if you do not want to involve CUBE in the codec negotiation. |
|---|---|

| Note | VAD to NO-VAD calls is not supported by Cisco Unified Border Element (CUBE) . This confirms that CUBE cannot generate comfort noise to fill periods of silence. |
|---|---|

| Protocol | Header
                                    				size |
|---|---|
| IP | 20 bytes |
| UDP | 8 bytes |
| RTP | 12 bytes |
| cRTP | Reduces
                                    				size of IP, UDP, RTP to 2 or 4 bytes |

| Codec & Bit Rate (kbps) | Codec Sample Size (Bytes) | Codec Sample Interval (ms) | Mean Opinion Score (MOS) | Voice Payload Size (Bytes) | Voice Payload Size (ms) | Payload Size (ms) Packets Per Second (PPS) | Bandwidth Ethernet (kbps) |
|---|---|---|---|---|---|---|---|
| G.711 (64 kbps) | 80 | 10 | 4.1 | 160 | 20 | 50 | 87.2 |
| G.729 (8 kbps) | 10 | 10 | 3.92 | 20 | 20 | 50 | 31.2 |
| G.723.1 (6.3 kbps) | 24 | 30 | 3.9 | 24 | 30 | 33.3 | 21.9 |
| G.723.1 (5.3 kbps) | 20 | 30 | 3.8 | 20 | 30 | 33.3 | 20.8 |
| G.726 (32 kbps) | 20 | 5 | 3.85 | 80 | 20 | 50 | 55.2 |
| G.726 (24 kbps) | 15 | 5 |  | 60 | 20 | 50 | 47.2 |
| G.728 (16 kbps) | 10 | 5 | 3.61 | 60 | 30 | 33.3 | 31.5 |
| G722_64k(64 kbps) | 80 | 10 | 4.13 | 160 | 20 | 50 | 87.2 |
| ilbc_mode_20(15.2 kbps) | 38 | 20 | 3.95 | 38 | 20 | 50 | 38.4 |
| ilbc_mode_30(13.33 kbps) | 50 | 30 | 3.88 | 50 | 30 | 33.3 | 28.8 |
| OPUS |  |  |  |  |  |  |  |

| Codec Bit Rate (kbps) | Based on the codec, this is the number of bits per second that must be transmitted to deliver a voice call. (codec bit rate
                                    = codec sample size / codec sample interval). |
|---|---|
| Codec Sample Size (Bytes) | Size (Bytes) Based on the
                                    				codec, this is the number of bytes captured by the digital signal processor
                                    				(DSP) at each codec sample interval. For example, the G.729 coder operates on
                                    				sample intervals of 10 ms, corresponding to 10 bytes (80 bits) per sample at a
                                    				bit rate of 8 kbps. (codec bit rate = codec sample size / codec sample
                                    				interval). |
| Codec Sample Interval
                                    				(ms) | This is the sample
                                    				interval at which the codec operates. For example, the G.729 coder operates on
                                    				sample intervals of 10 ms, corresponding to 10 bytes (80 bits) per sample at a
                                    				bit rate of 8 kbps. (codec bit rate = codec sample size / codec sample
                                    				interval). |
| MOS | MOS is a system of
                                    				grading the voice quality of telephone connections. With MOS, a wide range of
                                    				listeners judge the quality of a voice sample on a scale of one (bad) to five
                                    				(excellent). The scores are averaged to provide the MOS for the codec. |
| Voice Payload Size
                                    				(Bytes) | The voice payload size
                                    				represents the number of bytes (or bits) that are filled into a packet. The
                                    				voice payload size must be a multiple of the codec sample size. For example,
                                    				G.729 packets can use 10, 20, 30, 40, 50, or 60 bytes of voice payload size. |
| Voice Payload Size (ms) | Payload Size (ms) The
                                    				voice payload size can also be represented in terms of the codec samples. For
                                    				example, a G.729 voice payload size of 20 ms (two 10 ms codec samples)
                                    				represents a voice payload of 20 bytes [ (20 bytes * 8) / (20 ms) = 8 kbps ] |
| PPS | PPS represents the number of packets that need to be transmitted every second in order to deliver the codec bit rate. For
                                    example, for a G.729 call with voice payload size per packet of 20 bytes (160 bits), 50 packets must be transmitted every
                                    second [50 pps = (8 kbps) / (160 bits per packet) ] |

| Important | In Cisco IOS XE 17.16.1a release, the Secure Communications Interoperability Protocol (SCIP) feature  is available in 'preview’ mode as it includes
                                       limited functionality or incomplete software dependencies. Cisco reserves the right to disable preview features at any time
                                       without notice. Cisco Technical Support provides reasonable effort support for features in preview mode. There is no Service
                                       Level Objective (SLO) in response times for features in preview mode; response times may be slow. |
|---|---|

| Codec Keyword | Codec |
|---|---|
| aacld | AACLD 90000 bps |
| clear-channel | Clear
                                       				  Channel 64000 bps (No voice capabilities: data transport only) |
| g711alaw | G.711 A Law
                                       				  64000 bps |
| g711ulaw | G.711 u Law 64000 bps |
| g722-64 | G722-64K
                                       				  64000 bps |
| g723ar53 | G.723.1
                                       				  ANNEX-A 5300 bps (contains built-in VAD that cannot be disabled) |
| g723ar63 | G.723.1
                                       				  ANNEX-A 6300 bps (contains built-in VAD that cannot be disabled) |
| g723r53 | G.723.1
                                       				  5300 bps |
| g723r63 | G.723.1
                                       				  6300 bps |
| g726r16 | G.726 16000
                                       				  bps |
| g726r24 | G.726 24000
                                       				  bps |
| g726r32 | G.726 32000
                                       				  bps |
| g728 | G.728 16000
                                       				  bps |
| g729br8 | G.729
                                       				  ANNEX-B 8000 bps (contains built-in VAD that cannot be disabled) |
| g729r8 | G.729 8000 bps |
| gsmamr-nb | GSM AMR-NB
                                       				  4750 to 12200 bps (contains built-in VAD that cannot be disabled) |
| ilbc | iLBC 13330
                                       				  or 15200 bps |
| isac | iSAC 10 to
                                       				  32 kbps (variable bit-rate) |
| mp4a-latm | MP4A-LATM
                                       				  upto 128 kbps |
| opus | Opus upto 510 kbps |
| transparent | Transparent; uses the endpoint codec |
| scip | SCIP audio codec (This feature is available in 'preview' mode) |

| Codec
                                    				Keyword | Codec |
|---|---|
| h261 | Video Codec H261 |
| h263 | Video Codec H263 |
| h263+ | Video Codec H263+ |
| h264 | Video Codec H264 |
| mpeg4 | Video Codec
                                       				  MPEG-4 ISO/IES 14496-2 |
| scip | Video Codec SCIP (This feature is available in 'preview' mode) |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables
                                          				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device> configure terminal | Enters global
                                          				configuration mode. |
| Step 3 | voice class codec tag Example: Device(config)# voice class codec 10 | Enters
                                          				voice-class configuration mode for the specified codec voice class. |
| Step 4 | Add the following for each audio codec you want to configure in the voice class: codec preference value codec-type [ profile profile-tag ] codec preference value codec-type [ bytes payload-size fixed-bytes ] codec preference value isac [ mode {adaptive \| independent} [ bit-rate value framesize { 30 \| 60 } [fixed] ]] codec preference value ilbc [ mode frame-size [ bytes payload-size ]] codec preference value mp4-latm [ profile tag ] codec preference value scip | Configure a codec within the voice class and specify a preference for the codec. This becomes part of a preference list. Note The SCIP feature in Cisco IOS XE 17.16.1a release is available in 'preview’ mode as it includes limited functionality or incomplete software dependencies. | Note | The SCIP feature in Cisco IOS XE 17.16.1a release is available in 'preview’ mode as it includes limited functionality or incomplete software dependencies. |
| Note | The SCIP feature in Cisco IOS XE 17.16.1a release is available in 'preview’ mode as it includes limited functionality or incomplete software dependencies. |
| Step 5 | Add the following to configure a video codec: video codec codec Example: video codec h261 Example: video codec scip | Configures a video codec within the voice class. |
| Step 6 | exit Example: Device(config-class)# exit | Exits the
                                          				current mode. Enter your password if prompted. |
| Step 7 | dial-peer voice number voip Example: Device(config)# dial-peer voice 1 voip | Enters dial
                                          				peer configuration mode for the specified VoIP dial peer. |
| Step 8 | voice-class codec tag offer-all Example: Device(config-dial-peer)# voice-class codec 10 | Applies the previously configured voice class and associated codecs to a dial peer. The offer-all keyword allows the device to offer all codecs configured in a codec voice class. |
| Step 9 | end Example: Device(config-dial-peer)# end | Returns to
                                          				privileged EXEC mode. |

| Note | The SCIP feature in Cisco IOS XE 17.16.1a release is available in 'preview’ mode as it includes limited functionality or incomplete software dependencies. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables
                                          				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device> configure terminal | Enters global
                                          				configuration mode. |
| Step 3 | dial-peer voice number voip Example: Device(config)# dial-peer voice 1 voip | Enters dial
                                          				peer configuration mode for the specified VoIP dial peer. |
| Step 4 | Enter one of the following to configure audio codec: codec codec [ bytes payload-size fixed-bytes ] codec isac [ mode {adaptive \| independent} [ bit-rate value framesize { 30 \| 60 } [fixed] ]] codec ilbc [ mode frame-size [ bytes payload-size ]] codec mp4-latm [ profile tag ] codec opus [ profile tag ] codec scip Example: For g711alaw Codec Device(config-dial-peer)# codec g711alaw Example: For ISAC Codec Device(config-dial-peer)# codec isac mode independent | Configures an audio codec at the dial peer level. By default, g729r8, 20-byte payload is configured. |
| Step 5 | Add the following to configure a video codec: video codec codec Example: For h2621 video codec Device(config-dial-peer)# video codec h261 Example: For scip video codec Device(config-dial-peer)# video codec scip | Configures a video codec at the dial peer level. |
| Step 6 | (Optional) Enter one of the following to configure RTP payload type: rtp payload-type cisco-codec-isac number rtp payload-type cisco-codec-ilbc number rtp payload-type cisco-codec-video-h263+ number rtp payload-type cisco-codec-video-h264 number rtp payload-type opus number rtp payload-type codec-audio-scip number rtp payload-type codec-video-scip number Example: Device(config-dial-peer)# rtp payload-type opus 114 | (Optional) Configures the RTP payload type. Note The SCIP feature in Cisco IOS XE 17.16.1a release is available in 'preview’ mode as it includes limited functionality or incomplete software dependencies. | Note | The SCIP feature in Cisco IOS XE 17.16.1a release is available in 'preview’ mode as it includes limited functionality or incomplete software dependencies. |
| Note | The SCIP feature in Cisco IOS XE 17.16.1a release is available in 'preview’ mode as it includes limited functionality or incomplete software dependencies. |
| Step 7 | end Example: Device(config-dial-peer)# end | Returns to
                                          				privileged EXEC mode. |

| Note | The SCIP feature in Cisco IOS XE 17.16.1a release is available in 'preview’ mode as it includes limited functionality or incomplete software dependencies. |
|---|---|

| Step 1 | show call active voice [compact] Displays a
                                          				compact version of call information for voice calls in progress. Example: Router# show call active voice compact <callID>  A/O FAX T<sec> Codec       type        Peer Address       IP R<ip>:<udp>
Total call-legs: 2
        23 ANS     T3     mp4a-latm   VOIP        Psipp          9.45.33.11:57210
        24 ORG     T3     mp4a-latm   VOIP        P123           9.45.33.11:57210 Example: Router# show call active voice compact <callID>   A/O FAX T<sec> Codec    type    Peer Address    IP R<ip>:<udp> 
Total call-legs: 2
58 ANS     T11          g711ulaw   VOIP     Psipp 2001:......:230A:6080
59 ORG     T11          g711ulaw   VOIP     P5000110011       10.13.37.150:6090 Example: Router# show call active voice compact <callID>  A/O FAX  T<sec> Codec   type   Peer Address  IP R<ip>:<udp>     VRF
Total call-legs: 2
  350      ANS       T6     scip   VOIP    Psipp        10.43.33.45:6006    NA
  351      ORG       T6     scip   VOIP    P8888        10.43.33.45:6002    NA |
|---|---|
| Step 2 | show call active voice [brief] Displays a brief summary of call information for voice calls in progress. Example: Router# show call active voice brief Telephony call-legs: 0
SIP call-legs: 2
H323 call-legs: 0
Call agent controlled call-legs: 0
SCCP call-legs: 0
STCAPP call-legs: 0
Multicast call-legs: 0
Total call-legs: 2
121C : 19 2737820ms.1 (*11:50:45.045 UTC Tue Jul 23 2024) +1010 pid:666 Answer 1234 active
 dur 00:00:12 tx:0/0 rx:0/0 dscp:0 media:0 audio tos:0xB8 video tos:0x0
 IP 10.64.86.70:6008 SRTP: off rtt:0ms pl:0/0ms lost:0/0/0 delay:0/0/0ms scip TextRelay: off Transcoded: No ICE: Off
 media inactive detected:n media contrl rcvd:n/a timestamp:n/a
 long duration call detected:n long duration call duration:n/a timestamp:n/a
 LostPacketRate:0.00 OutOfOrderRate:0.00
 LocalUUID:37110991b54051679f675479a6e93de7
 RemoteUUID:e74b1bf0678e5209915c03a9660cb00f
 VRF: NA
121C : 20 2737820ms.2 (*11:50:45.045 UTC Tue Jul 23 2024) +1010 pid:777 Originate 1111 active
 dur 00:00:12 tx:0/0 rx:0/0 dscp:0 media:0 audio tos:0xB8 video tos:0x0
 IP 10.64.86.70:6004 SRTP: off rtt:0ms pl:0/0ms lost:0/0/0 delay:0/0/0ms scip TextRelay: off Transcoded: No ICE: Off
 media inactive detected:n media contrl rcvd:n/a timestamp:n/a
 long duration call detected:n long duration call duration:n/a timestamp:n/a
 LostPacketRate:0.00 OutOfOrderRate:0.00
 LocalUUID:e74b1bf0678e5209915c03a9660cb00f
 RemoteUUID:37110991b54051679f675479a6e93de7
 VRF: NA
Telephony call-legs: 0
SIP call-legs: 2
H323 call-legs: 0
Call agent controlled call-legs: 0
SCCP call-legs: 0
STCAPP call-legs: 0
Multicast call-legs: 0
Total call-legs: 2 |

| Note | The SCIP feature in Cisco IOS XE 17.16.1a release is available in 'preview’ mode as it includes limited functionality or incomplete software dependencies. |
|---|---|