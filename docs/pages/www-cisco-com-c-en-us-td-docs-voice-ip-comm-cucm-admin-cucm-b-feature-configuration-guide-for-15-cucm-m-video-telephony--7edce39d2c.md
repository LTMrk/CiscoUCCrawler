---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-cucm-b-feature-configuration-guide-for-15-cucm-m-video-telephony--7edce39d2c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/cucm_b_feature-configuration-guide-for-15/cucm_m_video-telephony.html
retrieved_at: 2026-08-16T16:07:23.128062+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 15 and SUs

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: March 26, 2026

Chapter: Video Telephony

## Chapter: Video Telephony

# Video Telephony

## Video Telephony Overview

Unified Communications Manager supports video telephony and thus unifies the world of voice and video calls. Video endpoints use Unified CM call-handling
                           features and access a unified voice and video solution for dialing and connecting video calls.

The Unified Communications Manager video telephony solution offers these features:

Supports video and video-related features, such as Far-End Camera Control (FECC)

Supports multiple logical channels that are needed to allow the transmission of video streams

Transmits midcall, media-related messages that are needed for video (that is, transmits commands or indications that are needed
                                 for video calls)

Supports H.323, Skinny Client Control Protocol (SCCP), and Session Initiation Protocol (SIP)

Enhances locations and regions to provide Bandwidth Management

Provides serviceability information, such as Call Detail Records (CDRs), about video calls

## Video Telephony Support

The following sections discuss the details of video telephony in the Unified Communications Manager environment.

### Video Calls

The typical video call includes two or three Real-Time Protocol (RTP) streams in each direction (that is, four or six streams).
                              The call can include the following stream types:

Video (H.261, H.263, H.263+, H.264-SVC, X-H.264UC, H.264-AVC, H.265, AV1 and VT Camera wideband video codecs)

Far-End Camera Control (FECC) - Optional

Binary Floor Control Protocols (BFCP)

Call control for video calls operates the same way as the call control that governs all other calls. For more information,
                                          see the Configure Media Resources chapter in the System Configuration Guide . You can also see, Configure Conference Bridges chapter in the System Configuration Guide for details on how Unified Communications Manager can allocate a video conference bridge automatically.

### Real-Time Transport Control Protocol Pass-Through in MTP Topologies

An IOS Media Terminate Point (MTP) before 15.2(2)T, cannot pass-through Real-Time Transport Control Protocol (RTCP) packets
                              and therefore cannot exchange Real-Time Protocol (RTP) feedback data to enhance the RTP transmission. The primary function
                              of RTCP is to provide feedback on media distribution by periodically sending statistics to participants in a streaming multimedia
                              session. RTCP gathers statistics for a media connection and information such as transmitted octet and packet counts, lost
                              packet counts, jitter, and round-trip delay time. An application may use this information to control the quality of service
                              parameters, perhaps by limiting flow or using a different codec.

IOS MTP Version 15.2(2)T and later supports RTCP pass-through capability so that the endpoint in a call with an MTP present
                              can still provide feedback and status on an RTP transmission. RTCP pass-through capability applies to media channels.

The RTCP pass-through feature is not limited to a specific call signaling protocol. For example, it can be SIP-SIP, SIP-nonSIP,
                              or nonSIP-nonSIP.

For Unified CM to allocate an RTCP pass-through capable MTP specifically, the call needs to fulfill the following conditions:

An MTP is requested for a feature that requires the MTP to be in media pass-through mode. For example, TRP, DTMF translation,
                                    IP address V4/V6 translation, and so on. RTCP pass-through is only applicable when the media is in pass-through mode.

The RTCP pass-through MTP needs to be included in the Media Resource Group Lists (MRGL) of the endpoint that sponsors the
                                    MTP. MTP can be inserted by RSVP, TRP, DTMF mismatch reasons.

When the call is capable of establishing video channels, Unified CM attempts to search for an RTCP pass-through capable MTP.
                                    For example, Unified CM picks an RTCP pass-through capable MTP from other non-capable ones in the MRGL. If an RTCP pass-through
                                    capable MTP is not available, then Unified CM stills allocate an MTP for the call.

When the call is capable of establishing an audio channel only, Unified CM does not intentionally request an RTCPpass-through
                                    capable MTP for the non-video calls. However, if the MRGL only contains RTCPpass-through capable MTP(s), then Unified CM inserts
                                    one of those into the audio call.

The call also needs to fulfill the current CAC bandwidth for video calls to have an RTCP pass-through capable MTP.

If a call initially establishes with a non-RTCP pass-through capable MTP (before version 15.2(2)T) present in the call, and
                                          the call escalates into a video-capable call,  Unified CM does not reallocate to an RTCP pass-through capable MTP. In that
                                          case, even though the call has been escalated to a video call, the existing MTP does not allow RTCP packets to be passed through.

### Video Codecs

Common video codecs include H.261, an older video codec, H.263, a newer codec that gets used to provide internet protocol
                              (IP) video, and H.264, a high-quality codec. The system supports H.264 for calls that use the Skinny Client Control Protocol
                              (SCCP), H.323, and SIP on originating and terminating endpoints only. The system also supports regions and locations.

Unified Communications Manager maintains the offerer's video codec ordering preference when making the answer, if possible. H.265 is the preferred video
                              codec is available on the endpoints, otherwise, Unified Communications Manager follows the following codec preference preference order:

Preference Order

Codecs

Description

1

H.265 (HEVC)

Provides higher quality video using lower bandwidth.

2

H.264 (SVC)

Allows rendering of variable quality video from the same media stream, by disregarding a subset of the packets received.

H. 264 SVC is a new annex to the H.264-AVC video compression standard; meaning it is an enhancement on top of H.264-AVC. It
                                                      provides the ability to encapsulate multiple video streams at various frame-rates and resolutions in one container.

3

X-H.264UC (Lync)

Microsoft-Proprietary Variant

4

H.264 (AVC)

Advanced Video Coding

5

H.263

H.263 and H.261 codecs exhibit the following parameters and typical values:

Bit rates range from 64 kb/s to a few mb/s. These bit rates can exist in any multiple of 100 b/s. H.261 and H.263 can function
                                                with bit rates lower than 64 kb/s, but video quality suffers in such cases.

One-quarter Common Interchange Format (QCIF) (Resolution equals 176x144.)

Common Interchange Format (CIF) (Resolution equals 352x288.)

4CIF (Resolution equals 704x576.)

Sub QCIF (SQCIF) (Resolution equals 128x96.)

16CIF (Resolution equals 1408x1152.)

Custom Picture Format

Resolution:

Frame Rate: 15 frames per second (fps), 30 fps

Annexes: F, D, I, J, K, L, P, T, N

6

H.261

The bandwidth of video calls equals the sum of the audio bandwidth and the video bandwidth. The total bandwidth does not include
                              overhead.

A 384-kb/s video call may comprise G.711 at 64 kb/s (for audio) plus 320 kb/s (for video). This sum does not include overhead.
                                 If the audio codec for a video call is G.729 (at 24 kb/s), the video rate increases to maintain a total bandwidth of 384 kb/s.
                                 If the call involves an H.323 endpoint, the H.323 endpoint may use less than the total available video bandwidth. Regardless
                                 of protocol, the endpoint may always choose to send at less than the max bit rate for the call.

#### AV1 Codec Support

AV1 is a next-generation video codec developed by the Alliance for Open Media. The benefits of AV1 are:

Reduced bandwidth consumption and better visual quality by utilizing better compression efficiency compared to other video
                                       encodings

Enables video for users on very low bandwidth networks

Significant screen sharing efficiency improvements over other codecs

Unified Communication Manager supports negotiation of AV1 codec to establish media if endpoints support the AV1 codec.

When both endpoints support Multiple Codecs in Answer, Unified CM negotiates all the matching codecs including AV1 based on
                                 the preference order received. The endpoint will then use one of the codecs from the negotiated codec list for media streaming.
                                 In a low bandwidth environment, the AV1 codec is preferred by the endpoint over other codecs in the negotiated list.

When both the endpoints involved in the call do not support the Multiple Codec in Answer, and the AV1 is the preferred codec
                                 over other codecs, Unified CM selects AV1 as the negotiated codec.

AV1 codec is not yet supported on TelePresence endpoints.

## Video Network

The following illustration provides an example of a video network that uses a single Unified Communications Manager cluster.
                           In a successful video network, any endpoint can call any other endpoint. Video availability only exists if both endpoints
                           are video-enabled. Video capabilities extend across trunks.

The Cisco video conference portfolio comprises the following video bridges:

Cisco TelePresence MCU series

Webex Meeting Server

The Cisco UC Endpoints portfolio comprises the following endpoints that support video:

For more information on Cisco UC Endpoint portfolio that support vedio, see Compatibility Matrix .

Third-party SIP video endpoints are capable of connecting to Cisco Unified Communications Manager as a line-side device or
                                       as a trunk-side device. For more information, see Third-Party SIP Endpoints.

## Video Telephony Configuration Task Flow

To configure video telephony in Cisco Unified Communications Manager Administration follow these steps.

Step 1

Configure regions for video call bandwidth if you use regions for call admission control.

All devices include a default region, which defaults to 384 kb/s for video. You can set the bandwidth setting in Region configuration
                                                      high enough for the desired resolution (For example, increase to 2Mb/s for high-definition video call).

Step 2

Configure locations for video call bandwidth if you use locations for call admission control.

Step 3

(Optional) Configure the RSVP service parameters, or set the RSVP policy in the Location Configuration window if using RSVP for bandwidth
                                       management of SIP video calls.

Step 4

Configure the appropriate conference bridge for your network to use a Cisco video conference bridge.

Step 5

Configure the media resource groups and media resource group lists for the user accordingly to configure a user to use the
                                       video conference bridge instead of using other conference bridges.

Step 6

Configure the H.323 gateways in your system to retry video calls as audio calls (default behavior) or configure AAR groups
                                       and route/hunt lists to use alternate routing for video calls that do not connect.

Step 7

Configure the H.323 phones in your system to retry video calls as audio calls (default behavior) or configure AAR groups and
                                       route/hunt lists to use alternate routing for video calls that do not connect. Choose Enabled for Video Capabilities .

Step 8

Configure the H.323 trunks in your system to retry video calls as audio calls (default behavior) or configure AAR groups and
                                       route/hunt lists to use alternate routing for video calls that do not connect.

Step 9

Configure the Cisco Unified IP Phones that will support video.

Step 10

Configure the third-party SIP endpoints that will support video.

Step 11

Configure the SIP trunks in your system to retry video calls as audio calls (default behavior).

## H.323 Video

H.323 video exhibits the following characteristics:

H.323 endpoints can be configured as H.323 phones, H.323 gateways, or H.323 trunks.

Call forwarding, dial plan, and other call-routing-related features work with H.323 endpoints.

H.323 video endpoints cannot initiate hold, resume, transfer, park, and other similar features.

If an H.323 endpoint supports the empty capability set (ECS), the endpoint can be held, parked, and so forth.

Some vendors implement call setup in such a way that they cannot increase the bandwidth of a call when the call gets transferred
                                    or redirected. In such cases, if the initial call is audio, users may not receive video when they are transferred to a video
                                    endpoint.

No video media termination point (MTP) nor video transcoder currently exists. If an audio transcoder or MTP is inserted into
                                    a call, that call will be audio only. This is true when the IPVC audio transcoding capabilities is not being used. When the
                                    IPVC transcoders are used, you can transcode the audio and send/receive video.

For H.323 video calls, users must specify video call bandwidth.

### H.239-Extended Video Channels in H.323 Call

The extended video channels feature works via H.239
                                 		  protocol and enables multiple video channel support. Cisco Unified Communications Manager supports negotiating an extended video channel
                                 		  using the H.239 protocol in direct point-to-point H.323 calls. This also
                                 		  includes calls across the H.323 intercluster trunk.

Cisco Unified Communications Manager supports all H.239 associated support
                                 		  signals and commands that are specified in the H.239 recommendation.

The following sections describes characteristics which apply
                                 		  to the extended video channels feature.

#### Support for Third-Party H.323 Devices

The extended video channel feature supports H.239 interoperability among third-party video endpoints and Cisco Unified Voice
                                    Conferencing. Cisco Unified Communications Manager allows an extended video channel to be used for presentation and live meeting transmission. This feature focuses on multiple
                                    video channel support via H.245 signaling. The following presentation applications provide basis for this multichannel support:

Natural Presenter package by the third-party vendor video endpoint

People + Content by the third-party vendor Polycom

Both Natural Presenter package and People + Content use the H.239 protocol to negotiate capabilities and define the roles
                                    of the additional video channels.

Natural Presenter package by video endpoint and People + Content by Polycom only support H.239 for the presentation mode.

Be aware that the presentation applications that are offered by video endpoint and Polycom are optional features. You must
                                                have one of these options and H.239 enabled in both caller and callee endpoints to negotiate second video channels or the
                                                call will be limited to a single video channel.

#### H.323 Devices Invoke Presentation Feature

Cisco and Polycom video endpoints allow the user to share presentation materials from various components (for example, VCR,
                                    Projector, PC, and so on). The components can physically connect with the endpoints, and the PC can also run presentation
                                    applications that are provided by the vendor to transmit the presentation image. The source of presentation and the component
                                    connection with the video endpoint are irrelevant to the mechanism of establishing video channels by using H.239.

For details on setting up presentation sources, see the video
                                                			 endpoint user guide.

When two H.239-enabled endpoints attempt to establish a
                                    		  video call, they declare their video capabilities for the main video channel
                                    		  for meeting participants and their extended video capabilities (H.239
                                    		  capabilities) for the second video channel. The following contents comprise
                                    		  H.239 capability signals:

The endpoints send signals to indicate that the devices support
                                          				H.239. They also send associated commands and indication signals for managing
                                          				the second video channel. This enables both the endpoints to be aware that the
                                          				call is capable of opening multiple video channels.

The endpoints sends out one or more extended video codec
                                          				capabilities to express video codec capabilities for second channels. The
                                          				endpoint must specify the role of the second video channel. The defined role
                                          				labels can be

Live-video-This channel gets processed normally and is
                                                					 suitable for live video of people

Presentation-This channel relays a token-managed presentation
                                                					 that is distributed to the devices

After the capabilities have been exchanged, both endpoints
                                    		  immediately open two-way audio channels and the main video channels as in the
                                    		  traditional video calls.

#### Opening Second Video Channels

Depending on the third-party endpoint implementation, the second video channel is handled differently among vendors.

##### Natural Presenter Package by Tandberg

Video endpoints initiates the second video channel on demand. A video endpoint device does not open the second video channel
                                    immediately after the main video channel is established. The second channel gets opened when one of the callers (the presenter)
                                    specifies the source of the presentation and invokes a command to start the presentation.

When a video endpoint user decides to start sharing the presentation, video endpoint requests the other call party to open
                                    an extended video channel for receiving the presentation image; therefore, a video endpoint-video endpoint call has only one-way
                                    second video channel.

##### People + Content by Polycom

Unlike video endpoint, a Polycom video endpoint initiates the second video endpoint immediately as a part of the default mechanism,
                                    after both parties have confirmed that additional video channels can be supported.

The channel established gets automatically if both parties support H.239 and have the extended video channel feature enabled.
                                                However, the additional channel does not show anything until one of the parties start to share presentation.

Polycom initiates a request for the second video channel to the other call party regardless of the usage of the second video
                                                channel; therefore, in a Polycom-Polycom call, two-way video channels get opened between the devices even if only one of them
                                                sends out presentation image/video.

This implementation ensures that both call parties have the second video channel ready for transmission when the call parties
                                                decide to take the token to present something. Although one of the two video channels remains idle (not sending anything),
                                                the Polycom device controls bandwidth to ensure load efficiency.

This difference in handling second video channels does not affect the implementation of H.239. Unified Communications Manager does not initiate any receiving channel request in an H.323-H.323 call. Unified Communications Manager simply relays all channel requests from one terminal to another.

Unified Communications Manager does not enforce two-way transmission for the second set of video channels because this does not represent a requirement
                                                in the H.239 protocol.

#### Call Admission Control (CAC) on Second Video Channels

The following call admission control policies of Cisco Unified Communications Manager get applied to the second video channels:

Cisco Unified Communications Manager restricts the bandwidth usage by the
                                    		  second video channels on the basis of location configuration. When the second
                                    		  video channel is being established, Cisco Unified Communications Manager makes sure that enough video bandwidth stays
                                    		  available within the location pool and reserves bandwidth accordingly. If the
                                    		  required bandwidth is not available, Cisco Unified Communications Manager instructs the channel to reduce the available
                                    		  bandwidth to zero.

No change occurs in the region configuration or policies to
                                    		  support the second video channels.

Traditionally, Cisco Unified Communications Manager region policy has only supported a call with a
                                    		  single video channel and the total bandwidth usage of this call never gets
                                    		  larger than what the region configuration specifies.

If the administrator sets a finite region video bandwidth
                                    		  restriction for an H.239 call, Cisco Unified Communications Manager will violate the region policy because the
                                    		  region value will get used against the bandwidth that is requested for each
                                    		  video channel independently.

##### Example

```
If the region video bandwidth is set to 384Kbps and the audio channel uses 64Kb/s, 
the maximum allowed bandwidth for each video channel will be (384Kb/s - 64Kb/s)= 320Kb/s.   
i.e. the maximum bandwidth to be used by the H.239 call will be (audio bw + 2*(384 - audio 
bw)) = 704Kb/s, which goes beyond the 384Kb/s bandwidth that the region specifies.
```

You should consider relaxing both region and location bandwidth
                                                			 restrictions for H.239 calls, so the H.239 devices are allowed to readjust and
                                                			 balance load for both the video channels without Cisco Unified Communications Manager intervention.

#### Number of Video Channels Allowed

Unified Communications Manager supports only a maximum of two video channels due to the following reasons:

Both Cisco and Polycom only support two video channels, one of which is for main video, and the other is for presentation.

H.239 only defines an Additional Media Channel (AMC) for H.320-based system to partition the traditional H.320 video channel
                                          for the purpose of presentation.

#### H.239 Commands and Indication Messages

Command and Indication (C&I) messages get used for H.239 to manage tokens for the Presentation and Live roles and to permit
                                    devices to request release of video flow control to enable the operation of additional media channels. Cisco Unified Communications Manager supports all the C & I messages. Whenever Cisco Unified Communications Manager receives C&I messages, it relays them to the call party accordingly.

Be aware that the flow control release request and response messages can be used to request that the far end release flow
                                    control, so it allows an endpoint to send the indicated channel at the indicated bit rate.

Be aware that the call party may or may not honor the request as is indicated by flow control release response.

The Presentation role token messages allow an H.239 device to acquire the token for presentation. The other call party may
                                    accept or reject the request. The presenter device sends out a token release message when it is no longer needed.

#### Topology and Protocol Interoperability Limitation

Cisco Unified Communications Manager supports only H.239 in H.323 to H.323 calls. Cisco Unified Communications Manager allows H.239 calls to be established across H.323 intercluster trunk or multiple nodes. If an H.239-enabled device attempts
                                    to make a call with a non-H323 end, the H.239 capabilities will get ignored and the call will get conducted like the traditional
                                    video calls that are supported by Cisco Unified Communications Manager .

Cisco Unified Communications Manager does not support a second video channel when a media termination point or transcoder is inserted into the call. If it happens,
                                    the call will fall back to normal video calls.

#### Midcall Feature Limitation

Cisco Unified Communications Manager supports opening second video channels
                                    		  only in direct H.323 to H.323 calls.

Caution

Do not attempt to invoke any
                                                			 midcall features such as call transfer or hold/resume operations. Doing so can
                                                			 lead to problems and the second video channel can get disconnected.

## Video Support

Unified Communications Manager supports video over H.323, SCCP and SIP protocols.

### Skinny Client Control Protocol Video

Skinny Client Control Protocol video exhibits the following characteristics:

If a phone that is running Skinny Client Control Protocol reports video capabilities, Cisco Unified Communications Manager automatically opens a video channel if the other end supports video.

For Skinny Client Control Protocol video calls, system administration determines video call bandwidth by using regions. The
                                       system does not ask users for bit rate.

### SIP Video

SIP video supports the following video calls by using the
                                 		  SIP Signaling Interface (SSI):

SIP to SIP

SIP to H.323

SIP to SCCP

SIP intercluster trunk

H.323 trunk

Combination of SIP and H.323 trunk

SIP video calls also provide media control functions for
                                 		  video conferencing.

Unified Communications Manager video supports SIP on both SIP trunks and lines support video signaling. SIP supports the H.261, H.263, H.263+, H.264 (AVC),
                                 H.264 (SVC), X-H.264UC (Lync), and AV1 video codecs (it does not support the wideband video codec that the VTA uses).

Only some of the endpoints supports AV1 codec. For more information, see Compatability Matrix .

#### Configuring SIP Devices for Video Calls

Perform the following steps to enable video calls on SIP
                                    		  devices:

##### SIP Trunks

On the Trunk Configuration window in Unified Communications Manager , check the Retry Video Call as Audio check box if you want the call to use audio when the video connection is not available.

Reset the trunk.

##### Third-Party SIP Endpoints

On the Phone Configuration window in Cisco Unified Communications Manager Administration , check the Retry Video Call as Audio check box if you want the call to use audio when the video connection is not available.

Reset the endpoint.

### Cisco Video Conference Bridges

Unified Communications Manager supports a variety of solutions for video conferencing. The following video conference bridges support ad hoc and meet-me
                              video conferencing:

Cisco TelePresence MCU

Cisco TelePresence Conductor

Cisco Meeting Server

#### Cisco TelePresence MCU Video Conference Bridge

Cisco TelePresence MCU is a set of hardware conference bridges for Cisco Unified Communications Manager.

The Cisco TelePresence MCU is a high-definition (HD) multipoint video conferencing bridge. It delivers up to 1080p at 30 frames
                                    per second, full continuous presence for all conferences, full transcoding, and is ideal for mixed HD endpoint environments.
                                    The Cisco TelePresence MCU supports SIP as the signaling call control protocol. It has a built in Web Server that allows for
                                    complete configuration, control, and monitoring of the system and conferences. The Cisco TelePresence MCU provides XML management
                                    API over HTTP.

Cisco TelePresence MCU allows both ad hoc and meet-me voice and video conferencing. Each conference bridge can host several
                                    simultaneous, multiparty conferences. Cisco TelePresence MCU must be configured in Port Reservation mode.

#### Cisco TelePresence Conductor Video Conference Bridge

Cisco TelePresence Conductor provides intelligent conference administrative controls and is scalable, supporting device clustering
                                    for load balancing across MCUs and multiple device availability. Administrators can implement the Cisco TelePresence Conductor
                                    as either an appliance or a virtualized application on VMware with support for Cisco Unified Computing System (Cisco UCS)
                                    platforms or third-party-based platforms. Multiway conferencing, that allows for dynamic two-way to three-way conferencing,
                                    is also supported.

Cisco TelePresence Conductor supports both ad hoc and meet-me voice and video conferencing. Cisco TelePresence Conductor dynamically
                                    selects the most appropriate Cisco TelePresence resource for each new conference. Ad hoc, “MeetMe” and scheduled voice and
                                    video conferences can dynamically grow and exceed the capacity of individual MCUs. One Cisco TelePresence Conductor appliance
                                    or Cisco TelePresence Conductor cluster has a system capacity of 30 MCUs or 2400 MCU ports. Up to three Cisco TelePresence
                                    Conductor appliances or virtualized applications may be clustered to provide greater resilience.

#### Cisco Meeting Server

The Cisco Meeting Server conference bridge solution allows Ad Hoc, Meet-Me, Conference Now, and Rendezvous conferences. This
                                 conference bridge offers premises-based audio, video, and web conferencing, and works with third-party on-premises infrastructure.
                                 It scales for small or large deployments. You can add capacity incrementally as needed, to ensure that you can support the
                                 current and future needs of your organization. This conference bridge provides advanced interoperability. Any number of participants
                                 can create and join meetings from:

Cisco or third-party room or desktop video systems

Cisco Jabber Client

Cisco Meeting App (can be native or with a WebRTC compatible browser)

Skype for Business

A minimum release of Cisco Meeting Server 2.0 is required to use the Cisco Meeting Server conference bridge.

The Cisco Meeting Server supports SIP as the signaling call control protocol. It has a built in Web Server that allows for
                                 complete configuration, control, and monitoring of the system and conferences. The Cisco Meeting Server provides XML management
                                 API over HTTP.

Cisco Meeting Server is enhanced to support AV1 codec and does not support H.265 video codec and Far End Camera Control (FECC).

### Video Encryption

Unified Communications Manager supports encryption of audio, video, and other media streams so long as the individual endpoints involved in the communication
                              also support encryption. Unified CM uses the Secure Real-Time Transport Protocol (SRTP) to encrypt the media streams. Some
                              of the features include:

Support for SIP and H.323 endpoints

Support for encryption of main audio and video line while operating in Media Termination Point (MTP) passthru mode

Support for multiple encryption methods

Support for Session Description Protocol (SDP) crypto-suite session parameters in accordance with RFC 4568

To provide encrypted communications, encryption keys are exchanged between the endpoints and Unified Communications Manager during the SIP call setup. For this reason, the SIP signaling should be encrypted using TLS. During the initial call setup,
                              the video endpoints exchange a list of encryption methods they support, select an encryption suite supported by both endpoints,
                              and exchange encryption keys. If the endpoints cannot agree on a common encryption suite, the media streams are unencrypted
                              and transported using the Real-Time Transport Protocol (RTP).

If the individual endpoints do not support encryption, the communication will take place using RTP.

### Configure Interop with VCS

Perform the following steps on the SIP trunk that connects Unified Communications Manager to Cisco VCS to enable Unified CM to interoperate with a Cisco VCS.

Step 1

From Cisco Unified CM Administration, choose Device > Trunk .

Step 2

Perform one of the following:

- Click Find and select an existing trunk.

- Click Add New to configure a new trunk.

Step 3

In the Trunk Configuration window, choose the Trunk Type , Device Protocol , Trunk Service Type that connects Unified Communications Manager to the Cisco VCS and click Next .

Step 4

In the SIP Profile drop-down list, choose Standard SIP Profile for VCS .

Step 5

In the Normalization Script drop-down list, choose vcs-interop .

Step 6

In the Normalization Script area, leave the Parameter Name and Parameter Value fields empty. If these fields are populated with values, delete the contents of the field.

Step 7

Click Save .

## Video Features

The following video-related features are supported in SIP video networks:

Binary Floor Control Protocol (BFCP)

Encrypted iX Channel

Far End Camera Control (FECC)

### Endpoint Support for the Binary Floor Control Protocol

Unified Communications Manager provides support for the Binary Floor Control Protocol (BFCP) for specific Cisco and third-party video endpoints. BFCP allows
                              users to share a presentation within an ongoing video conversation.

For more information, see chapter Configure Presentation Sharing using BFCP in Feature Configuration Guide for Cisco Unified Communications Manager .

### Encrypted iX Channel

Unified Communications Manager supports an encrypted iX channel. The iX channel provides a reliable channel for multiplexing application media between SIP
                              phones in a video conference. Encrypted iX Channel uses DTLS to add security to your deployment and ensures that the application
                              media is sent over the iX Channel is private and cannot be viewed by intermediate parties who attempt to intercept media.

IOS MTP and RSVP agents in pass through mode also support encrypted iX Channel.

#### Configuration

To enable an encrypted iX Channel on Unified Communications Manager , you must:

Check the Allow iX Application Media check box in the SIP Profile Configuration that is used by any intermediate SIP trunks. This setting turns on the iX channel
                                       negotiation.

Configure the Secure Call Icon Display Policy service parameter to enable a secure lock icon. By default, the setting is All media except BFCP and iX transports must be encrypted .

#### Encryption Modes

There are two types of Session Description Protocol (SDP) offers that Unified Communications Manager supports for iX Channel encryption for encrypted phones. This encryption type is driven by what the endpoints support and
                                    is not a configurable item in the Unified Communications Manager .

Best Effort Encryption —The SDP offer is for an encrypted iX Channel, but falls back to a non-encrypted iX Channel if the SIP peers do not support
                                          it. This approach can be used if encryption is not mandatory in the solution.

For example, encryption is mandatory within the cloud, and not in a single enterprise.

Best-Effort iX Encryption

m=application 12345 UDP/UDT/IX *

a=setup:actpass

a=fingerprint: SHA-1 <key>

Forced Encryption —The SDP offer is for an encrypted iX Channel only. This offer is rejected if the SIP peers do not support iX Channel encryption.
                                          This approach can be used in deployments where encryption is mandatory between endpoints.

For example, encryption is mandatory between the two SIP devices.

Forced iX Encryption

m=application 12345 UDP/DTLS/UDT/IX *

a=setup:actpass

a=fingerprint: SHA-1 <key>

By default, all Cisco IP Phones are set to offer Best Effort iX Encryption. However, you can reset this to Forced Encryption
                                    by setting the Encryption Mode to On within the Product-Specific Configuration of Cisco TelePresence endpoints, or by reconfiguring settings on the Cisco Meeting
                                    Server.

#### Non-Encrypted Modes

Unified Communications Manager enables negotiation of secure active control messages in media path from endpoints in a meeting when the endpoint may not
                                 be deployed in a fully secure mode. For example, if the endpoint is Off-Net and is registered with Unified CM in Mobile and
                                 Remote Access mode.

##### Prerequisite

Before you start using this feature, make sure that:

System adheres to the export compliance requirement

SIP trunk to the conference bridge is secure

Unified CM can negotiate the DTLS information in secure active control messages for non-secure endpoints or softphones and
                                    receive messages in the following ways:

Best Effort Encryption iX to On-Premise registered endpoints or softphones

Forced iX Encryption to Off-Premise registered endpoints or softphones

### Far End Camera Control Protocol Support

The Far End Camera Control (FECC) protocol allows you to control a remote camera. Within video calls, FECC allows the party
                                 at one end of the call to control the camera at the far end. This control can include panning the camera from one side to
                                 the other, tilting the camera, or zooming in and out. For video conferences that use multiple cameras, FECC can be used to
                                 switch from one camera to another.

Unified Communications Manager supports the FECC protocol for video endpoints that are FECC-capable. Cisco Unified Communications Manager supports FECC
                                 for SIP-SIP calls or H.323-H.323 calls, but does not support FECC for SIP-H.323 calls. To support FECC, Unified Communications Manager sets the application media channel through SIP or H.323 signaling. After the media channel is established, the individual
                                 endpoints can communicate the FECC signaling.

## QoS for Video Networks

Cisco Unified Communications Manager contains a number of administrative tools for managing Quality of Service (QoS) for video
                           networks:

Bandwidth Management—Mange bandwidth allocations for specific Regions and Locations

Enhanced Locations Call Admission Control

Session Level Bandwidth Modifiers

Flexible DSCP Markings

Alternate Routing

### Bandwidth Management

Bandwidth allocations for audio and video calls are managed through regions and locations that you configure in Cisco Unified Communications Manager Administration .

The amount of bandwidth available for a specific call must
                                 		  be able to manage the combination of all media streams that are associated with
                                 		  the session, including voice, video, signaling, and any extra media, such as a
                                 		  BFCP presentation. Cisco Unified Communications Manager contains features able to manage bandwidth.

### Enhanced Locations Call Admission Control

Enhanced Locations Call Admission Control (CAC) enables you to control the audio and video quality of calls over a wide-area
                              (IP WAN) link by limiting the number of calls that are allowed on that link at the same time. For example, you can use call
                              admission control to regulate the voice quality on a 56-kb/s frame relay line that connects your main campus and a remote
                              site.

CAC verifies whether there is sufficient bandwidth available to complete a call. CAC can reject calls due to insufficient
                              bandwidth.

In Unified Communications Manager , locations-based call admission control works in conjunction with regions to define the characteristics of a network link.
                              Regions and locations work in the following manner:

Regions allow the bandwidth of video calls to be set. The audio limit on the region may result in filtering out codecs with
                                    higher bit rates. However, for video calls, the video limit constrains the quality (resolution and transmission rate) of the
                                    video.

Locations define the amount of total bandwidth available for all calls on that link. When a call is made on a link the regional
                                    value for that call must be subtracted from the total bandwidth allowed for that link.

For more information about call admission control, see chapter 'Configure Enhanced Locations Call Admission Control' in System Configuration Guide for Cisco Unified Communications Manager

.

### Session Level Bandwidth Modifiers

Unified Communications Manager provides location call admission control support for handling session level bandwidth modifiers. Session level bandwidth
                                 modifiers are communicated as part of the parameters in the SDP portion of the initial SIP signaling. These parameters indicate
                                 the maximum amount of bandwidth each endpoint will support for that type of call. These parameters are used, along with regions
                                 and locations settings, to set the bandwidth for each call.

During the initial call setup, both parties communicate to Unified Communications Manager their maximum allowed bandwidth for the call. Unified Communications Manager passes this communication to the other endpoint, but if the bandwidth that is specified by the endpoint is greater than the
                                 region setting, Unified Communications Manager replaces the value with the region bandwidth value.

Unified Communications Manager uses the following rules to determine the amount of bandwidth to allocate to a specific call:

When Unified Communications Manager receives an Offer or Answer from an endpoint, it checks whether there is a session level bandwidth modifier in the SDP:

If there is a session level bandwidth modifier, Unified Communications Manager retrieves the bandwidth value from the modifier. If there is more than one modifier type, it retrieves the modifier in the
                                             following order of preference: Transport Independent Application Specific (TIAS), Application Specific (AS), Conference Total
                                             (CT).

If there is no session level bandwidth modifier, Unified Communications Manager retrieves the bandwidth value from the sum of the media level bandwidth modifiers.

The allocated bandwidth is the maximum of what the two endpoints support up to the maximum value of the Region setting. The
                                       allocated bandwidth cannot exceed the region setting.

Unified Communications Manager uses the following logic when communicating with endpoints:

When generating an Answer, Early Offer or Re-Invite Offer to an endpoint that contains more than one session level bandwidth
                                       modifier type (TIAS, AS, CT), Unified Communications Manager uses the same bandwidth value for each.

When generating an answer, Unified Communications Manager uses the same session level bandwidth modifier type (TIAS, CT, AS) that was received in the initial offer

For backward compatibility, the older Unified Communications Manager suppresses the Session Level Bandwidth Modifier when a video call is put on hold and music on hold (MOH) is inserted.

### Video Resolution Support for SIP Phones

If the session level bandwidth is greater than 800Kb/s and the imageattr[640 x 480] line in the SDP exists, then VGA is used.

If the session level bandwidth is greater than 800Kb/s and the imageattr[640 x 480] line in the SDP does not exist, then w360p
                                          is used.

If the session level bandwidth is less than 800Kb/s but greater than 480 bits per second and the imageattr[640 x 480] line
                                          exists, then VGA 15 frames per second is used.

If you currently have a Cisco IP Phone model 9951, 9971, or 8961 that supports w360p (640 x 360) video resolution and are
                                             upgrading to Cisco Unified Communications Manager release 8.5(1) or later, you may notice changes in the resolution of video calls. The w360p resolution was introduced at
                                             phone load 9.2(1).

Phone A sends a SIP message with an imageattr line in the SDP.

Cisco Unified Communications Manager deletes the imageattr line in the SDP and then sends the modified SIP message to Phone B.

Phone B attempts to send video with the w360p resolution because there is no imageattr line in the SDP portion of the SIP
                                          header.

Phone A sends a SIP message with the imageattr line in the SDP.

Cisco Unified Communications Manager does not delete the imageattr line and sends the SIP message to Phone B unchanged.

Phone B attempts to send video with the VGA resolution.

### Alternate Routing

If an endpoint cannot obtain the bandwidth that it needs for a video call, a video call retries as an audio call for the default
                                 behavior. To use route/hunt lists or Automated Alternate Routing (AAR) groups to try different paths for such video calls,
                                 uncheck the Retry Video Call as Audio setting in the configuration settings for applicable gateways, trunks, and phones.

For more information, see Configure AAR Group section under Configure Call Routing chapter in the System Configuration Guide for Cisco Unified Communications Manager .

### Flexible DSCP Markings

Differentiated Services Code Point (DSCP) packet marking, is used to specify the class of service for each packet. DSCP marking
                              lets you prioritize certain types of calls or media over other types. For example, you can prioritize audio over video so
                              that, even if you experience network bandwidth issues, audio calls should not experience bandwidth issues.

You can customize DSCP markings in either of these ways:

Configure cluster wide service parameters to set the default DSCP settings for the cluster

(Optional) For a subset of the DSCP categories, you can assign customized DSCP settings to devices via the SIP Profile. For
                                    the devices that use the profile, the customized settings override the service parameter defaults.

For more information on how to configure DSCP markings, see 'Configure Flexible DSCP Marking and Video Promotion' chapter
                              in the Feature Configuration Guide for Cisco Unified Communications Manager .

### Phone Configuration for Video Calls

The following setting for video-enabled devices affects
                                 		  video calls:

Retry Video Call as Audio-By default, this check box remains
                                       				checked. Thus, if an endpoint (phone, gateway, trunk) cannot obtain the
                                       				bandwidth that it needs for a video call, call control retries the call as an
                                       				audio call. This setting applies to the destination devices of video calls.

Video Capabilities Enabled/disabled-This drop-down list box turns
                                       				video capabilities on and off.

### Conference Control for Video Conferencing

Unified Communications Manager supports the following conference controls capabilities:

Roster/Attendee List

Drop Participant

Terminate Conference

Show Conference Chairperson/Controller

Continuous Presence

Unified Communications Manager also supports the following video conference capabilities for Skinny Client Control Protocol (SCCP) phones:

Display controls for video conferences. The SCCP phones can choose to use the continuous presence or voice-activated mode
                                       to view the video conference. When a mode is chosen, a message gets sent to the bridge to indicate which mode to use on the
                                       video channel. Switching between modes does not require renegotiation of media.

Display participant information such as the user name in the video
                                       				stream. The system can use the participant information for other conferencing
                                       				features such as roster.

For more information, see 'Encrypted iX Channel' chapter in the Security Guide for Cisco Unified Communications Manager .

### Video Telephony and Cisco Unified Serviceability

Cisco Unified Serviceability tracks video calls and conferences by updating performance monitoring counters, video bridge counters, and call detail records
                                 (CDRs).

#### Performance Counters

Video telephony events cause updates to the following Cisco Unified Serviceability performance monitoring counters:

##### Cisco CallManager

VCBConferenceActive

VCBConferenceCompleted

VCBConferenceTotal

VCBOutOfConferences

VCBOutOfResources

VCBResourceActive

VCBResourceAvailable

VideoCallsActive

VideoCallsCompleted

VideoOutOfResources

##### Gatekeeper

VideoOutOfResources

##### CiscoH.323

VideoCallsActive

VideoCallsCompleted

##### Cisco Locations

RSVP VideoCallsFailed

RSVP VideoReservationErrorCounts

VideoBandwidthAvailable

VideoBandwidthMaximum

VideoOutOfResources

##### Cisco SIP

VideoCallsActive

VideoCallsCompleted

##### Cisco Vedio Conference Bridge

ConferencesActive

ConferencesAvailable

ConferencesCompleted

ConferencesTotal

OutOfConferences

OutOfResources

ResourceActive

ResourceAvailable

ResourceTotal

#### Video Bridge Counters

Video conference events cause updates to these Cisco video
                                    		  conference bridge performance monitoring counters:

ConferencesActive

ConferencesAvailable

ConferencesCompleted

ConferencesTotal

OutOfConferences

OutOfResources

ResourceActive

ResourceAvailable

ResourceTotal

These counters also display in the Cisco Unified Communications Manager object with the VCB prefix.

#### Call Detail Records (CDRs)

Video telephony events cause updates to Call Detail Records (CDRs) in Cisco Unified Serviceability. These CDRs include the
                                 following information:

origVideoCap_Codec

origVideoCap_Bandwidth

origVideoCap_Resolution

origVideoTransportAddress_IP

origVideoTransportAddress_Port

destVideoCap_Codec

destVideoCap_Bandwidth

destVideoCap_Resolution

destVideoTransportAddress_IP

destVideoTransportAddress_Port

origRSVPStat

destRSVPVideoStat

origVideoCap_Codec_Channel2

origVideoCap_Bandwidth_Channel2

origVideoCap_Resolution_Channel2

origVideoTransportAddress_IP_Channel2

origVideoTransportAddress_Port_Channel2

origVideoChannel_Role_Channel2

destVideoCap_Codec_Channel2

destVideoCap_Bandwidth_Channel2

destVideoCap_Resolution_Channel2

destVideoTransportAddress_IP_Channel2

destVideoTransportAddress_Port_Channel2

destVideoChannel_Role_Channel2

#### Call Management Records (CMRs)

Video telephony events cause updates to Call Management Records (CMRs) in Cisco Unified Serviceability. These CMRs include
                                 the following information:

videoContentType Text String

videoDuration Integer

numberVideoPacketsSent Integer

numberVideoOctetsSent Integer

numberVideoPacketsReceived Integer

numberVideoOctetsReceived Integer

numberVideoPacketsLost Integer

videoAverageJitter Integer

videoRoundTripTime

videoOneWayDelay

videoTransmissionMetrics

| Note | Call control for video calls operates the same way as the call control that governs all other calls. For more information,
                                          see the Configure Media Resources chapter in the System Configuration Guide . You can also see, Configure Conference Bridges chapter in the System Configuration Guide for details on how Unified Communications Manager can allocate a video conference bridge automatically. |
|---|---|

| Note | If a call initially establishes with a non-RTCP pass-through capable MTP (before version 15.2(2)T) present in the call, and
                                          the call escalates into a video-capable call,  Unified CM does not reallocate to an RTCP pass-through capable MTP. In that
                                          case, even though the call has been escalated to a video call, the existing MTP does not allow RTCP packets to be passed through. |
|---|---|

| Preference Order | Codecs | Description |
|---|---|---|
| 1 | H.265 (HEVC) | Provides higher quality video using lower bandwidth. |
| 2 | H.264 (SVC) | Allows rendering of variable quality video from the same media stream, by disregarding a subset of the packets received. Note H. 264 SVC is a new annex to the H.264-AVC video compression standard; meaning it is an enhancement on top of H.264-AVC. It
                                                      provides the ability to encapsulate multiple video streams at various frame-rates and resolutions in one container. | Note | H. 264 SVC is a new annex to the H.264-AVC video compression standard; meaning it is an enhancement on top of H.264-AVC. It
                                                      provides the ability to encapsulate multiple video streams at various frame-rates and resolutions in one container. |
| Note | H. 264 SVC is a new annex to the H.264-AVC video compression standard; meaning it is an enhancement on top of H.264-AVC. It
                                                      provides the ability to encapsulate multiple video streams at various frame-rates and resolutions in one container. |
| 3 | X-H.264UC (Lync) | Microsoft-Proprietary Variant |
| 4 | H.264 (AVC) | Advanced Video Coding |
| 5 | H.263 | H.263 and H.261 codecs exhibit the following parameters and typical values: Bit rates range from 64 kb/s to a few mb/s. These bit rates can exist in any multiple of 100 b/s. H.261 and H.263 can function
                                                with bit rates lower than 64 kb/s, but video quality suffers in such cases. One-quarter Common Interchange Format (QCIF) (Resolution equals 176x144.) Common Interchange Format (CIF) (Resolution equals 352x288.) 4CIF (Resolution equals 704x576.) Sub QCIF (SQCIF) (Resolution equals 128x96.) 16CIF (Resolution equals 1408x1152.) Custom Picture Format Resolution: Frame Rate: 15 frames per second (fps), 30 fps Annexes: F, D, I, J, K, L, P, T, N |
| 6 | H.261 |

| Note | H. 264 SVC is a new annex to the H.264-AVC video compression standard; meaning it is an enhancement on top of H.264-AVC. It
                                                      provides the ability to encapsulate multiple video streams at various frame-rates and resolutions in one container. |
|---|---|

| Note | AV1 codec is not yet supported on TelePresence endpoints. |
|---|---|

| Note | Third-party SIP video endpoints are capable of connecting to Cisco Unified Communications Manager as a line-side device or
                                       as a trunk-side device. For more information, see Third-Party SIP Endpoints. |
|---|---|

| Step 1 | Configure regions for video call bandwidth if you use regions for call admission control. Note All devices include a default region, which defaults to 384 kb/s for video. You can set the bandwidth setting in Region configuration
                                                      high enough for the desired resolution (For example, increase to 2Mb/s for high-definition video call). | Note | All devices include a default region, which defaults to 384 kb/s for video. You can set the bandwidth setting in Region configuration
                                                      high enough for the desired resolution (For example, increase to 2Mb/s for high-definition video call). |
|---|---|---|---|
| Note | All devices include a default region, which defaults to 384 kb/s for video. You can set the bandwidth setting in Region configuration
                                                      high enough for the desired resolution (For example, increase to 2Mb/s for high-definition video call). |
| Step 2 | Configure locations for video call bandwidth if you use locations for call admission control. |
| Step 3 | (Optional) Configure the RSVP service parameters, or set the RSVP policy in the Location Configuration window if using RSVP for bandwidth
                                       management of SIP video calls. |
| Step 4 | Configure the appropriate conference bridge for your network to use a Cisco video conference bridge. |
| Step 5 | Configure the media resource groups and media resource group lists for the user accordingly to configure a user to use the
                                       video conference bridge instead of using other conference bridges. |
| Step 6 | Configure the H.323 gateways in your system to retry video calls as audio calls (default behavior) or configure AAR groups
                                       and route/hunt lists to use alternate routing for video calls that do not connect. |
| Step 7 | Configure the H.323 phones in your system to retry video calls as audio calls (default behavior) or configure AAR groups and
                                       route/hunt lists to use alternate routing for video calls that do not connect. Choose Enabled for Video Capabilities . |
| Step 8 | Configure the H.323 trunks in your system to retry video calls as audio calls (default behavior) or configure AAR groups and
                                       route/hunt lists to use alternate routing for video calls that do not connect. |
| Step 9 | Configure the Cisco Unified IP Phones that will support video. |
| Step 10 | Configure the third-party SIP endpoints that will support video. |
| Step 11 | Configure the SIP trunks in your system to retry video calls as audio calls (default behavior). |

| Note | All devices include a default region, which defaults to 384 kb/s for video. You can set the bandwidth setting in Region configuration
                                                      high enough for the desired resolution (For example, increase to 2Mb/s for high-definition video call). |
|---|---|

| Note | Natural Presenter package by video endpoint and People + Content by Polycom only support H.239 for the presentation mode. Be aware that the presentation applications that are offered by video endpoint and Polycom are optional features. You must
                                                have one of these options and H.239 enabled in both caller and callee endpoints to negotiate second video channels or the
                                                call will be limited to a single video channel. |
|---|---|

| Note | For details on setting up presentation sources, see the video
                                                			 endpoint user guide. |
|---|---|

| Note | The channel established gets automatically if both parties support H.239 and have the extended video channel feature enabled.
                                                However, the additional channel does not show anything until one of the parties start to share presentation. Polycom initiates a request for the second video channel to the other call party regardless of the usage of the second video
                                                channel; therefore, in a Polycom-Polycom call, two-way video channels get opened between the devices even if only one of them
                                                sends out presentation image/video. This implementation ensures that both call parties have the second video channel ready for transmission when the call parties
                                                decide to take the token to present something. Although one of the two video channels remains idle (not sending anything),
                                                the Polycom device controls bandwidth to ensure load efficiency. This difference in handling second video channels does not affect the implementation of H.239. Unified Communications Manager does not initiate any receiving channel request in an H.323-H.323 call. Unified Communications Manager simply relays all channel requests from one terminal to another. Unified Communications Manager does not enforce two-way transmission for the second set of video channels because this does not represent a requirement
                                                in the H.239 protocol. |
|---|---|

| Note | You should consider relaxing both region and location bandwidth
                                                			 restrictions for H.239 calls, so the H.239 devices are allowed to readjust and
                                                			 balance load for both the video channels without Cisco Unified Communications Manager intervention. |
|---|---|

| Note | Be aware that the call party may or may not honor the request as is indicated by flow control release response. |
|---|---|

| Caution | Do not attempt to invoke any
                                                			 midcall features such as call transfer or hold/resume operations. Doing so can
                                                			 lead to problems and the second video channel can get disconnected. |
|---|---|

| Note | Only some of the endpoints supports AV1 codec. For more information, see Compatability Matrix . |
|---|---|

| Note | Cisco Meeting Server is enhanced to support AV1 codec and does not support H.265 video codec and Far End Camera Control (FECC). |
|---|---|

| Note | If the individual endpoints do not support encryption, the communication will take place using RTP. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Trunk . |
|---|---|
| Step 2 | Perform one of the following: Click Find and select an existing trunk. Click Add New to configure a new trunk. |
| Step 3 | In the Trunk Configuration window, choose the Trunk Type , Device Protocol , Trunk Service Type that connects Unified Communications Manager to the Cisco VCS and click Next . |
| Step 4 | In the SIP Profile drop-down list, choose Standard SIP Profile for VCS . |
| Step 5 | In the Normalization Script drop-down list, choose vcs-interop . |
| Step 6 | In the Normalization Script area, leave the Parameter Name and Parameter Value fields empty. If these fields are populated with values, delete the contents of the field. |
| Step 7 | Click Save . |

| Note | If you currently have a Cisco IP Phone model 9951, 9971, or 8961 that supports w360p (640 x 360) video resolution and are
                                             upgrading to Cisco Unified Communications Manager release 8.5(1) or later, you may notice changes in the resolution of video calls. The w360p resolution was introduced at
                                             phone load 9.2(1). |
|---|---|