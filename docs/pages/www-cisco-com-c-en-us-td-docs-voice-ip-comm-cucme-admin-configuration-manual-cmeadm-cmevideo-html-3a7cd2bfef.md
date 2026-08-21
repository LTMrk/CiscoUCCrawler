---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmevideo-html-3a7cd2bfef
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmevideo.html
retrieved_at: 2026-08-21T07:24:20.657923+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Video Support

## Chapter: Video Support

# Video Support

## Prerequisites for
                        	 Video Support

H.323 or SIP network for voice calls is operational.

Cisco Unified CME 4.0 or a later version.

Cisco Unified IP phones are registered in Cisco Unified CME.

Connection between Cisco Unified Video Advantage (CUVA) 1.02 or a later version and the Cisco Unified IP Phone is up. From
                                 a PC with CUVA 1.02 or a later version installed, ensure that the line between the CUVA and the Cisco Unified P Phone is green.

Correct video firmware is installed on the Cisco Unified IP Phone.

For Cisco Unified IP Phone 7940G and 7960G, 6.0(4) or a later version.

Cisco Unified IP Phone 7970G, 7.0(3) or a later version.

Cisco Unified IP Phone 7941G and 7961G, 7.0(3) or a later version.

Other video-enabled endpoints registered with a Cisco Unified Communications Manager (Cisco Unified CM) can place video calls
                                       to Cisco Unified IP Phones only if the phones are registered with a Cisco Unified CME and the appropriate video firmware is
                                       installed on the Cisco Unified IP Phone.

## Restrictions for
                        	 Video Support

This feature
                                    			 supports only the following video codecs:

H.261—Cisco
                                          				  Unified CME 4.0 and later versions

H.263—Cisco
                                          				  Unified CME 4.0 and later versions

H.264—Cisco
                                          				  Unified CME 7.1 and later versions

This feature
                                    			 supports only the following video formats:

4CIF—Resolution 704x576

16CIF—Resolution 1408x1152

Common
                                          				  Intermediate Format (CIF)—Resolution 352x288

One-Quarter
                                          				  Common Intermediate Format (QCIF)—Resolution 176x144

Sub QIF
                                          				  (SQCIF)—Resolution 128x96

The call start
                                    			 fast feature is not supported with an H.323 video connection. You must
                                    			 configure call start slow for H.323 video. For configuration information, see Enable Support for Video Streams Across H.323 Networks .

Video
                                    			 capabilities are configured per phone, not per line.

All call feature
                                    			 controls (for example, mute and hold) apply to both audio and video calls, if
                                    			 applicable.

This feature
                                    			 does not support the following:

Dynamic
                                          				  addition of video capability—The video capability must be present before the
                                          				  call setup starts to allow the video connection.

T-120 data
                                          				  connection between two SCCP endpoints.

Video
                                          				  security

Far-end
                                          				  camera control (FECC) for SCCP endpoints.

Video codec
                                          				  renegotiation—The negotiated video codec must match or the call falls back to
                                          				  audio-only. The negotiated codec for the existing call can be used for a new
                                          				  call.

SIP
                                          				  endpoints— When a video-capable SCCP endpoint connects to a SIP endpoint, the
                                          				  call falls back to audio-only (prior to Cisco Unified CME 8.6).

Video
                                          				  supplementary services between Cisco Unified CME and Cisco Unified CM.

If the
                                    			 Cisco Unified CM is configured for Media Termination Point (MTP) transcoding, a
                                    			 video call between Cisco Unified CME and Cisco Unified CM is not supported.

Video telephony
                                    			 is not supported with Cisco Unified CME MTP and codec g729/dspfarm-assist
                                    			 configuration under ephone.

If an SCCP
                                    			 endpoint calls an SCCP endpoint on the local Cisco Unified CME and one of the
                                    			 endpoints transferred across an H.323 network, a video-consult transfer between
                                    			 the Cisco Unified CME systems is not supported.

When a
                                    			 video-capable endpoint connects to an audio-only endpoint, the call falls back
                                    			 to audio-only. During audio-only calls, video messages are skipped.

For
                                    			 Cisco Unified CME, the video capabilities in the vendor configuration firmware
                                    			 is a global configuration. This means that, although video can be enabled per
                                    			 ephone, the video icon shows on all Cisco Unified IP phones supported by
                                    			 Cisco Unified CME.

Because of the
                                    			 extra CPU consumption on RTP-stream mixing, the number of video calls supported
                                    			 on Cisco Unified CME crossing an H.323 network is less than the maximum number
                                    			 of ephones supported.

Cisco Unified CME cannot differentiate audio-only streams and
                                    			 audio-in-video streams. You must configure the DSCP values of audio and video
                                    			 streams in the H.323 dial-peers.

If RSVP is
                                    			 enabled on the Cisco Unified CME, a video call is not supported.

A separate VoIP
                                    			 dial peer, configured for fast-connect procedures, is required to complete a
                                    			 video call from a remote H.323 network to a Cisco Unity Express system.

Video call is
                                    			 enabled on Cisco Unified CME, when the active call is held and resumed.

## Information About Video Support

### Video Support
                           	 Overview

Video support allows
                              		you to pass a video stream, with a voice call, between two video-capable SCCP
                              		endpoints and between SCCP and H.323 endpoints. Through the Cisco Unified CME
                              		router, the video-capable endpoints can communicate with each other locally to
                              		a remote H.323 endpoint through a gateway or through an H.323 network.

Video capabilities
                              		are disabled by default, and enabling video capabilities on Cisco Unified CME
                              		does not automatically enable video on all ephones. You must first enable video
                              		globally for all video-capable SCCP phones associated with a Cisco Unified CME
                              		router and then enable video for each phone individually. Video parameters,
                              		like maximum bit rate, are set at a system level.

For information
                              		about the global configuration for video capabilities, see Enable System-Level Video Capabilities .

For information
                              		about configuring an individual phone for video capabilities, see Enable Video Capabilities on a Phone .

After video is
                                          		  enabled globally, all video-capable ephones display the video icon.

### SIP Trunk Video
                           	 Support

Cisco Unified CME
                              		7.1 adds the following support for video calls:

Support for
                                    			 video calls between SCCP endpoints across different Cisco Unified CME routers
                                    			 connected through a SIP trunk. All previously supported SCCP video endpoints
                                    			 and video codecs are supported.

H.264 video
                                    			 support—H.264 provides high-quality images at low bit rates and is widely used
                                    			 in commercial video conferencing systems. The H.264 codec supports the
                                    			 following video calls:

SCCP to SCCP

SCCP to SIP

SCCP to
                                          				  H.323

Dynamic
                                          				  payload negotiation for H.264 (both SCCP to SIP and SCCP to H323)

Restriction

On Cisco
                                                				Unified CME 8.6, calls made from SIP endpoints across a SIP trunk terminating
                                                				on a non-CME endpoint (such as those controlled by a Cisco Unified CM or video
                                                				conferencing MTU) require the following CLI to be configured to allow video:

```
voice service voip
 sip
   asymmetric payload full
```

The no supplementary-service
                                                      					 sip moved-temporarily and no supplementary-service
                                                      					 sip refer commands are not supported for video calls through a
                                                				SIP trunk.

Supplementary
                                                				services like call hold, call resume and call transfer are not supported on
                                                				video calls between SCCP and SIP endpoints that are registered with CME. The
                                                				call gets converted into audio-only mode when these supplementary services are
                                                				invoked.

No new configuration
                              		is required to support these enhancements. For configuration information, see Configure Video Support .

### Matching Endpoint Capabilities

During phone registration, information about endpoint capabilities is
                              		stored in the Cisco Unified CME. These capabilities are used to match with
                              		other endpoints during call setup. Endpoints can update at any time; however,
                              		the router recognizes endpoint-capability changes only during call setup. If a
                              		video feature is added to a phone, the information about it is updated in the
                              		router’s internal data structure but that information does not become effective
                              		until the next call. If a video feature is removed, the router continues to see
                              		the video capability until the call is terminated but no video stream is
                              		exchanged between the two endpoints.

The endpoint-capability match is executed each time a new call is set
                                          		  up or an existing call is resumed.

### Retrieving Video Codec Information

Voice gateways use dial-peer configurations to retrieve codec
                              		information for audio codecs. Video codec selection is done by the endpoints
                              		and is not controlled by the H.323 service-provider interface (SPI) through
                              		dial-peer or other configuration. The video-codec information is retrieved from
                              		the SCCP endpoint using a capabilities request during call setup.

### Call Fallback to Audio-Only

When a video-capable endpoint connects to an audio-only endpoint, the
                              		call falls back to an audio-only connection. Also, for certain features such as
                              		conferencing, where video support is not available, the call falls back to
                              		audio-only.

Cisco Unified CME routers use a call-type flag to indicate whether the
                              		call is video-capable or audio-only. The call-type flag is set to video when
                              		the video capability is matched or set to audio-only when connecting to an
                              		audio-only TDM or an audio-only SIP endpoint.

During an audio-only connection, all video-related media messages are
                                          		  skipped.

### Call Setup for Video Endpoints

The process for handling SCCP video endpoints is the same as that for
                              		handling SCCP audio endpoints. The video call must be part of the audio call.
                              		If the audio call setup fails, the video call fails.

During the call setup for video, media setup handling determines if a
                              		video-media-path is required. If so, the corresponding video-media-path setup
                              		actions are taken.

For an SCCP endpoint, video-media-path setup includes sending
                                       			 messages to the endpoints to open a multimedia path and start the multimedia
                                       			 transmission.

For an H.323 endpoint, video-media-path setup includes an exchange
                                       			 between the endpoints to open a logical channel for the video stream.

A call-type flag is set during call setup on the basis of the
                              		endpoint-capability match. After call setup, the call-type flag is used to
                              		determine whether an additional video media path is required. Call signaling is
                              		managed by the Cisco Unified CME router and the media stream is directly
                              		connected between the two video-enabled SCCP endpoints on the same router.
                              		Video-related commands and flow-control messages are forwarded to the other
                              		endpoint. Routers do not interpret these messages.

#### Call Setup Between Two Local SCCP Endpoints

For interoperation between two local SCCP endpoints on the same router,
                                 		video call setup uses all existing audio-call-setup handling, except during
                                 		media setup. During media setup, a message is sent to establish the
                                 		video-media-path. If the endpoint responds, the video-media-path is established
                                 		and a start-multimedia-transmission function is called.

#### Call Setup Between SCCP and H.323 Endpoints

Call setup between SCCP and H.323 endpoints is the same as it is between
                                 		SCCP endpoints except that if video capability is selected, the event is posted
                                 		to the H.323 call leg to send out a video open logical channel (OLC) and the
                                 		gateway generates an OLC for the video channel. Because the router needs to
                                 		both terminate and originate the media stream, video must be enabled on the
                                 		router before call setup begins.

#### Call Setup Between
                              	 Two SCCP Endpoints Across an H.323 Network

If call setup
                                 		between SCCP endpoints occurs across an H.323 network, the setup is a
                                 		combination of the processes listed in the previous two sections. The router
                                 		controls the video media setup between the two endpoints and the event is
                                 		posted to the H.323 call leg so that the gateway can generate an OLC.

Because the endpoint
                                 		capability negotiation and match occur after the H.323 connect message, video
                                 		streams over H.323 network require slow-start on call setup procedures for
                                 		Cisco Unified CME. An H.323 network can connect to a remote Cisco Unified CME
                                 		router, Cisco Unified CM, remote IP to IP gateway, or a video-capable H.323
                                 		endpoint. For configuration information, see Enable System-Level Video Capabilities .

### SIP Endpoint Video and Camera Support for Cisco Unified IP Phones
                           	 8961, 9951, and 9971

Cisco Unified CME 8.6 and later versions add phone-based video support
                              		and Universal Serial Bus (USB) camera support for Cisco Unified IP Phones 8961,
                              		9951, and 9971. The Cisco Unified IP Phones 8961, 9951, and 9971 display local
                              		video using the USB camera. Cisco Unified IP Phones 9951 and 9971 with phone
                              		load 9.1.1 decode remote incoming video RTP streams and display the video on
                              		the phone’s display screen. However, the video and USB camera capabilities of
                              		these two phones are disabled on Cisco Unified CME by default and are enabled
                              		by setting up the video and camera parameters in the phone provisioning file.

Cisco Unified CME 8.6 supports local SIP-video-to-SIP-video calls and
                              		SIP-video-to-SCCP-CUVA-video calls on Cisco Unified IP Phones 8961, 9951, and
                              		9971 on the line side. On the trunk side, SIP video call is only supported with
                              		SIP trunk. H323 trunk is not supported for video calls on Cisco Unified IP
                              		Phones 9951 and 9971.

The media path for SIP video call is flow through and media flow-around
                              		is not supported for SIP line in Cisco Unified CME.

#### Video and Camera
                              	 Configuration for Cisco Unified IP Phones

Cisco Unified CME
                                 		uses the video and camera commands to allow video or camera to be enabled per phone, per template, or for
                                 		global configuration. The video and camera commands are configured under the voice register pool, voice register template,
                                 		and voice register global configuration modes. Once the commands are
                                 		configured, the create
                                       			 profile command is required to have the phones provision file
                                 		update with new configuration. For more information on enabling camera and
                                 		video parameters on phones, see Enable Video and Camera Support on Cisco Unified SIP Phones .

The changes in video
                                 		and camera configuration are applied to the phones when Cisco Unified CME sends
                                 		the request to a phone through a service-control event in a SIP NOTIFY message.
                                 		In earlier versions of Cisco Unified CME, SIP phones were required to reset and
                                 		restart to update the new configuration parameters.

In Cisco Unified CME
                                 		8.6 and later versions, you use the apply-config command under voice register pool and voice register global configuration modes
                                 		to dynamically apply the video and camera configuration changes to the phone
                                 		configuration of Cisco Unified IP Phones 8961, 9951, and 9971 without
                                 		restarting or resetting the phones and without causing any service
                                 		interruption.

When Cisco Unified
                                 		IP Phones 8961, 9971 and 9951 receive the apply-config request, the phones
                                 		retrieve the new configuration file from the TFTP server and compare it with
                                 		the existing configuration. The phones may restart themselves if there are any
                                 		changes that requires a restart; otherwise, the phones apply the changes
                                 		dynamically without restarting.

For more
                                 		information, see Apply Video and Camera Configuration to Cisco Unified SIP Phones .

#### Bandwidth Control
                              	 for SIP Video Calls

Video call bandwidth
                                 		control is critical when there is a limit in resources. Typically, video calls
                                 		require much higher bandwidth usage than audio-only calls. Video calls on Cisco
                                 		Unified IP Phones 9951 and 9971 can use up to 1 Mbps for VGA quality video
                                 		compared to 64 kbps plus overhead for a G711 audio call.

In Cisco Unified CME 8.6, the Cisco Unified SIP IP Phones 9951 and 9971 with VGA resolution offer 1-Mbps maximum bit-rate
                                 and answer with a lower value of received offer and 1 Mbps. Phones transmit video resolution and frame rate is set according
                                 to the maximum bandwidth bit-rate negotiated in the SIP offer or answer. Cisco Unified CME controls the SIP global bandwidth
                                 by configuring the bandwidth video tias-modifier bandwidth value [ negotiate end-to-end ] command in voice register global configuration mode. The bandwidth control configuration is applied to the SIP phone dial-peer.

There are no new
                                 		bandwidth changes in the SCCP CUVA side and the bandwidth configuration works
                                 		the same as in earlier versions of Cisco Unified CME.

For more information
                                 		on configuring bandwidth control, see Configure Video Bandwidth Control for SIP to SIP Video Calls .

### Flow of the RTP Video Stream

For video streams between two local SCCP endpoints, the Real-Time
                                 		  Transport Protocol (RTP) stream is in flow-around mode. For video streams
                                 		  between SCCP and H.323 endpoints or two SCCP endpoints on different
                                 		  Cisco Unified CME routers, the RTP stream is in flow-through mode.

Media flow-around mode enables RTP packets to stream directly
                                       				between the endpoints of a VoIP call without the involvement of the gateway. By
                                       				default, the gateway receives the incoming media, terminates the call, and then
                                       				reoriginates it on the outbound call leg. In flow-around mode, only signaling
                                       				data is passed to the gateway, improving scalability and performance.

With flow-through mode, the video media path is the same as for an
                                       				audio call. Media packets flow through the gateway, thus hiding the networks
                                       				from each other.

Use the show voip rtp connection command to display information about RTP named-event packets, such as caller-ID number, IP address, and port for both the
                                 local and remote endpoints, as shown in the following sample output:

```
Router# show voip rtp connections VoIP RTP active connections :
		No. Callid  dstCallid  LocalRTP RmtRTP LocalIP RemoteIP       
		1   102     103        18714    18158  10.1.1.1 192.168.1.1       
		2   105     104        17252    19088  10.1.1.1 192.168.1.1       
		Found 2 active RTP connections
		============================
```

## Configure Video Support

### Enable Video and
                           	 Camera Support on Cisco Unified SIP Phones

To enable video
                                 		  and camera support on Cisco Unified SIP Phones such as 8845, 8865, 9951, and
                                 		  9971, perform the following steps:

Shared line
                                                   				  is not supported.

Video
                                                   				  transfer and forward supplementary service is not supported when no supplementary-service
                                                         						sip refer/move-temporary is configured.

#### Before you begin

Cisco Unified
                                       				CME 8.6 or a later version.

The mode cme command is configured under voice register global configuration mode.

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- camera

- video

- create profile

- exit

- voice register pool pool tag

- id mac address

- camera

- video

- exit

- voice register template template-tag

- camera

- video

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
Router(config)#voice register global
```

Enters voice
                                             				register global configuration mode to set parameters for all supported SIP
                                             				phones in Cisco Unified CME.

Step 4

camera

#### Example:

```
Router(config-register-global)#camera
```

Enables the camera command under voice register global configuration mode.

Step 5

video

#### Example:

```
Router(config-register-global)#video
```

Enables the video command
                                             				under voice register global configuration mode.

Make sure
                                                         				  you configure video command
                                                         				  without configuring the camera command so that Cisco Unified SIP phones can switch from phone-based video
                                                         				  camera to CUVA. If you configure both video and camera commands together, you may need to manually remove the USB camera from Cisco
                                                         				  Unified SIP phones .

Step 6

create profile

#### Example:

```
Router(config-register-global)# create profile
```

Generates
                                             				provisioning files required for SIP phones and writes the file to the location
                                             				specified with the tftp-path command.

Step 7

exit

#### Example:

```
Router(config-register-global)#exit
```

Exits voice
                                             				register global configuration mode.

Step 8

voice register pool pool tag

#### Example:

```
Router(config)#voice register pool 5
```

Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone.

Step 9

id mac address

#### Example:

```
Router(config-register-pool)#id mac 0009.A3D4.1234
```

Explicitly
                                             				identifies a locally available individual SIP phone to support a degree of
                                             				authentication.

Step 10

camera

#### Example:

```
Router(config-register-pool)#camera
```

Enables the camera command under voice register pool configuration mode.

Step 11

video

#### Example:

```
Router(config-register-pool)#video
```

Enables the video command under voice register pool configuration mode.

Step 12

exit

#### Example:

```
Router(config-register-pool)#exit
```

Exits voice
                                             				register pool configuration mode.

Step 13

voice register template template-tag

#### Example:

```
Router(config)voice register template 10
```

Enters voice
                                             				register template configuration mode to define a template of common parameters
                                             				for SIP phones in Cisco Unified CME.

Range: 1
                                                   					 to 5.

Step 14

camera

#### Example:

```
Router(config-register-template)#camera
```

Configures
                                             				the camera command under voice register template configuration mode.

Step 15

video

#### Example:

```
Router(config-register-template)#video
```

Configures
                                             				the video command under voice register template configuration mode.

Step 16

end

#### Example:

```
Router(config-register-template)# end
```

Returns to
                                             				privileged EXEC mode.

#### Examples

The following
                                 		  example shows the camera and video commands configured in voice register global configuration mode:

```
Router#show run
!
!
!
voice service voip
 allow-connections sip to sip
 fax protocol t38 version 0 ls-redundancy 0 hs-redundancy 0 fallback none
!
!
voice register global
 mode cme
 bandwidth video tias-modifier 512000 negotiate end-to-end
 max-pool 10 camera video !
voice register template  10
```

The following
                                 		  example shows the video and camera commands configured under voice register pool 5. You can also configure both camera and video commands under voice register template configuration mode.

```
Router#show run
!
!
voice service voip
 allow-connections sip to sip
 fax protocol t38 version 0 ls-redundancy 0 hs-redundancy 0 fallback none
!
!
voice register global
 mode cme
 bandwidth video tias-modifier 512000 negotiate end-to-end
 max-pool 10

!
voice register pool  1
 id mac 1111.1111.1111
!
voice register pool  4
!
voice register pool  5
 logout-profile 58
 id mac 0009.A3D4.1234 camera video !
```

#### What to do next

To apply the
                                 		  video and camera configuration to your Cisco Unified SIP IP phones, see Apply Video and Camera Configuration to Cisco Unified SIP Phones .

### Apply Video and
                           	 Camera Configuration to Cisco Unified SIP Phones

Apply-config is
                                 		  similar to resetting or restarting the phones and allowing the phones to update
                                 		  phone configuration files. Phones only reboot if needed. To apply video
                                 		  configuration to Cisco Unified IP phones 8845, 8865, 8961, 9951, and 9971,
                                 		  perform the following steps:

#### Before you begin

Cisco Unified CME
                                 		  8.6 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- apply-config

- exit

- voice register pool pool
                                       				  tag

- apply-config

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
Router(config)#voice register global
```

Enters voice
                                             				register global configuration mode to set parameters for all supported SIP
                                             				phones in Cisco Unified CME.

Step 4

apply-config

#### Example:

```
Router(config-register-global)#apply-config
```

Applies
                                             				configuration for the Cisco Unified SIP IP phones and restarts all other SIP
                                             				phones. The apply-config command acts as a reset if configured on any other
                                             				phone type.

Step 5

exit

#### Example:

```
Router(cfg-translation-rule)# exit
```

Exits voice
                                             				register global configuration mode.

Step 6

voice register pool pool
                                                				  tag

#### Example:

```
Router(config)#voice register pool 5
```

Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone.

Step 7

apply-config

#### Example:

```
Router(config-register-pool)#apply-config
```

Applies
                                             				configuration for the Cisco Unified SIP IP phones and restarts all other SIP
                                             				phones.

Step 8

end

#### Example:

```
Router(config-register-pool)# end
```

Returns to
                                             				privileged EXEC mode.

#### Examples

The following
                                 		  example shows the apply-config command configured in voice register pool 5:

```
Router# configure terminal
Router(config)#voice register pool 5
Router(config-register-pool)#apply-config
```

### Configure Video
                           	 Bandwidth Control for SIP to SIP Video Calls

To configure video
                                 		  bandwidth control for SIP to SIP video calls, perform the following steps:

#### Before you begin

Cisco Unified CME
                                 		  8.6 or a later version.

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- bandwidth video tias-modifier bandwidth value [ negotiate end-to-end ]

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
Router(config)#voice register global
```

Enters voice
                                             				register global configuration mode to set parameters for all supported SIP
                                             				phones in Cisco Unified CME.

Step 4

bandwidth video tias-modifier bandwidth value [ negotiate end-to-end ]

#### Example:

```
Router(config-register-global)#bandwidth video tias-modifier 512000 negotiate end-to-end
```

Allows to set
                                             				the maximum video bandwidth bits per second for SIP phones.

bandwidth value —Bandwidth value in bits per
                                                   					 second. Range: 1 to 99999999.

negotiate end-to-end —Bandwidth negotiation policy. Negotiates the minimum SIP-line video bandwidth in SDP end-to-end.

Step 5

end

#### Example:

```
Router(config-register-global)# end
```

Returns to
                                             				privileged EXEC mode.

#### Examples

The following
                                 		  example shows the bandwith video
                                       				tias-modifier command configured under voice register global
                                 		  configuration mode:

```
Router#show run
			 !
			 !
			 !
			 voice service voip
			  allow-connections sip to sip
			 !
			 !
			 voice register global
			  mode cme
			  source-address 10.100.109.10 port 5060
			  bandwidth video tias-modifier 512000 negotiate end-to-end
			  max-dn 200
			  max-pool 42
			  create profile sync 0004625832149157
			 !
			 voice register pool  1
			  id mac 1111.1111.1111
			  camera
			  video
```

### Enable Support for Video Streams Across H.323 Networks

To enable slow connect procedures in Cisco Unified CME for H.323
                                 		  networks and H.323 video endpoints, perform the following steps:

Restriction

Tandberg versions E3.0 and E4.1 and Polycom Release version 7.5.2
                                             			 are the only H.323 video endpoints supported by Cisco Unified CME.

#### Before you begin

For video supplementary services across an H.323 network, H.450
                                 		  (H.450.2, H.450.3, or H.450.1) standard protocol is required.

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- h323

- call start slow

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

voice service voip

#### Example:

```
Router(config)# voice service voip
```

Enters voice-service configuration mode.

Step 4

h323

#### Example:

```
Router(config-voi-serv)# h323
```

Enters H.323 voice-service configuration mode.

Step 5

call start slow

#### Example:

```
Router(config-serv-h323)# call start slow
```

Forces an H.323 gateway to use slow-connect procedures for all
                                             				VoIP calls.

Step 6

end

#### Example:

```
Router(config-serv-h323)# end
```

Returns to privileged EXEC mode.

### Enable
                           	 System-Level Video Capabilities

To enable video
                                 		  capabilities and set video parameters for all video-capable phones associated
                                 		  with a Cisco Unified CME router, perform the following steps:

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- service phone videoCapability { 0 | 1 }

- video

- maximum bit-rate value

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

service phone videoCapability { 0 | 1 }

#### Example:

```
Router(config-telephony)# service phone videoCapability 1
```

Enables or disables video capability parameter for all applicable IP phones associated with a Cisco Unified CME router.

The parameter name is word and case-sensitive.

0 —Disable (default).

1 —Enable.

Step 5

video

#### Example:

```
Router(config-telephony)# video
```

(Optional)
                                             				Enters video configuration mode.

Required
                                                      					 only if you want to modify the maximum value of the video bandwidth for all
                                                      					 video-capable phones.

Step 6

maximum bit-rate value

#### Example:

```
Router(conf-tele-video)# maximum bit-rate 256
```

(Optional)
                                             				Sets the maximum IP phone video bandwidth, in kilobits per second.

value —Range: 0 to 10000000. Default: 10000000.

Step 7

end

#### Example:

```
Router(conf-tele-video)# end
```

Exits to
                                             				privileged EXEC mode.

### Enable Video
                           	 Capabilities on a Phone

To enable video
                                 		  for video-capable phones associated with a Cisco Unified CME router, perform
                                 		  the following steps for each phone.

#### Before you begin

Video
                                       				capabilities are enabled at a system level. See Enable System-Level Video Capabilities .

Use the show ephone
                                             					 registered command to identify individual video-capable SCCP
                                       				phones, by ephone-tag, that are registered in Cisco Unified CME. The following
                                       				example shows that ephone 1 has video capabilities and ephone 2 is an
                                       				audio-only phone:

```
Router# show ephone registered ephone-1 Mac:0011.5C40.75E8 TCP socket:[1] activeLine:0 REGISTERED in SCCP ver 6 + Video and Server in ver 5
mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0 caps:7
IP:10.1.1.6 51833 7970 keepalive 35 max_line 8
button 1: dn 1 number 8003 CH1 IDLE CH2 IDLE ephone-2 Mac:0006.D74B.113D TCP socket:[2] activeLine:0 REGISTERED in SCCP ver 6 and Server in ver 5
mediaActive:0 offhook:0 ringing:0 reset:0 reset_sent:0 paging 0 debug:0 caps:7
IP:10.1.1.4 51123 Telecaster 7960 keepalive 36 max_line 6
button 1: dn 2 number 8004 CH1 IDLE CH2 IDLE 
button 2: dn 4 number 8008 CH1 IDLE CH2 IDLE 
===========================================
```

### SUMMARY STEPS

- enable

- configure terminal

- ephone phone-tag

- video

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
Router(config)# ephone 6
```

Enters ephone
                                             				configuration mode.

phone-tag —Unique sequence number that identifies
                                                   					 an ephone during configuration tasks.

Step 4

video

#### Example:

```
Router(config-ephone)# video
```

Enables video
                                             				capabilities on the specified ephone.

Step 5

end

#### Example:

```
Router(config-ephone)# end
```

Exits ephone
                                             				configuration mode and enters privileged EXEC mode.

### Verify Video
                           	 Support

Use the show
                                                				  running-config command to verify the video settings in the
                                          			 configuration.

See the
                                             				telephony-service portion of the output for commands that configure video
                                             				support on the Cisco Unified CME.

See the ephone
                                             				portion of the output for commands that configure video support for a specific
                                             				ephone.The following example shows the telephony-service portion of the output:

#### Example:

```
telephony-service
			 video eo
			   maximum bit-rate 256 
			  load 7960-7940 P00306000404 
			  max-ephones 24
			  max-dn 24 
			  ip source-address 10.0.180.130 port 2000 
			  service phone videoCapability 1
			  timeouts interdigit 4 
			  timeouts ringing 100 
			  create cnf-files version-stamp Jan 01 2002 00:00:00 
			  keepalive 60
			  max-conferences 4 gain -6 
			  call-park system redirect
			  call-forward pattern .T
			  web admin system name cisco password cisco 
			  web customize load xml.jeff 
			  dn-webedit
			  time-webedit 
			  transfer-system full-consult 
			  transfer-pattern .T
```

The following
                                             				example shows the ephone portion of the output:

```
ephone  6
 video
 mac-address 000F.F7DE.CAA5
 type 7960
 button  1:6
```

### Troubleshooting Video Support

For SCCP endpoint troubleshooting, use the following debug commands:

debug cch323 video —Enables video debugging
                                       			 trace on the H.323 service-provider interface (SPI).

debug ephone detail —Debugs all
                                       			 Cisco Unified IP phones that are registered to the router, and displays error
                                       			 and state levels.

debug h225 asn1 —Displays Abstract Syntax
                                       			 Notation One (ASN.1) contents of H.225 messages that have been sent or
                                       			 received.

debug h245 asn1 —Displays ASN.1 contents of
                                       			 H.245 messages that have been sent or received.

debug voip ccapi inout —Displays the
                                       			 execution path through the call-control application programming interface
                                       			 (CCAPI).

For ephone troubleshooting, use the following debug commands:

debug ephone message Enables message
                                       			 tracing between Cisco Unified IP phones.

debug ephone register —Sets registration
                                       			 debugging for Cisco Unified IP phones.

debug ephone video —Sets ephone video
                                       			 traces, which provide information about different video states for the call,
                                       			 including video capabilities selection, start, and stop.

For basic video-to-video call checking, use the following show commands:

show call active video —Displays call
                                       			 information for SCCP video calls in progress.

show ephone offhook —Displays information
                                       			 and packet counts for ephones that are off-hook.

show ephone registered SCCP —Displays the
                                       			 status of registered ephones.

show ephone summary types —Displays the
                                       			 number of SCCP phones configured along with the number of phones (registered
                                       			 and unregistered) pertaining to each type of phone.

show ephone summary brief —Displays
                                       			 information about the SCCP phones

show ephone registered SCCP
                                             				  summary —Displays information about the unregistered SCCP phones.

show ephone unregistered SCCP
                                             				  summary —Displays information about the unregistered SCCP phones.

show voice register pool type
                                             				  summary —Displays information about all configured SIP phones
                                       			 which includes SIP phones registered or unregistered with CME.

show voip rtp connections —Displays
                                       			 information about RTP named-event packets, such as caller ID number, IP
                                       			 address, and port for both the local and remote endpoints.

## Where to Go
                        	 Next

After enabling video
                           		for video-capable phones in Cisco Unified CME, you must generate a new
                           		configuration file. See Generate Configuration Files for Phones .

## Feature
                        	 Information for Video Support

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature
                                          					 Name

Cisco Unified CME Version

Feature
                                          					 Information

New Phone Support

12.0

Support was added for Cisco IP Phones 8845 and Cisco IP Phone
                                          					 8865 on Cisco Integrated Services Router Generation 2 (T-Train Release,
                                          					 15.7(3)M).

New Phone
                                          					 Support

11.7

Support
                                          					 was added for Cisco IP Phones 8845 and Cisco IP Phone 8865 on Cisco 4000 Series
                                          					 Integration Services Router.

SIP Trunk
                                          					 Video Support

7.1

Support
                                          					 was added for video calls between SCCP endpoints across different
                                          					 Cisco Unified CME routers connected through a SIP trunk.

H.264
                                          					 codec support was added.

Video
                                          					 Support

4.0

Video
                                          					 support was introduced.

| Note | Other video-enabled endpoints registered with a Cisco Unified Communications Manager (Cisco Unified CM) can place video calls
                                       to Cisco Unified IP Phones only if the phones are registered with a Cisco Unified CME and the appropriate video firmware is
                                       installed on the Cisco Unified IP Phone. |
|---|---|

| Note | After video is
                                          		  enabled globally, all video-capable ephones display the video icon. |
|---|---|

| Restriction | On Cisco
                                                				Unified CME 8.6, calls made from SIP endpoints across a SIP trunk terminating
                                                				on a non-CME endpoint (such as those controlled by a Cisco Unified CM or video
                                                				conferencing MTU) require the following CLI to be configured to allow video: voice service voip
 sip
   asymmetric payload full The no supplementary-service
                                                      					 sip moved-temporarily and no supplementary-service
                                                      					 sip refer commands are not supported for video calls through a
                                                				SIP trunk. Supplementary
                                                				services like call hold, call resume and call transfer are not supported on
                                                				video calls between SCCP and SIP endpoints that are registered with CME. The
                                                				call gets converted into audio-only mode when these supplementary services are
                                                				invoked. |
|---|---|

| Note | The endpoint-capability match is executed each time a new call is set
                                          		  up or an existing call is resumed. |
|---|---|

| Note | During an audio-only connection, all video-related media messages are
                                          		  skipped. |
|---|---|

| Note | Shared line
                                                   				  is not supported. Video
                                                   				  transfer and forward supplementary service is not supported when no supplementary-service
                                                         						sip refer/move-temporary is configured. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register global Example: Router(config)#voice register global | Enters voice
                                             				register global configuration mode to set parameters for all supported SIP
                                             				phones in Cisco Unified CME. |
| Step 4 | camera Example: Router(config-register-global)#camera | Enables the camera command under voice register global configuration mode. |
| Step 5 | video Example: Router(config-register-global)#video | Enables the video command
                                             				under voice register global configuration mode. Note Make sure
                                                         				  you configure video command
                                                         				  without configuring the camera command so that Cisco Unified SIP phones can switch from phone-based video
                                                         				  camera to CUVA. If you configure both video and camera commands together, you may need to manually remove the USB camera from Cisco
                                                         				  Unified SIP phones . | Note | Make sure
                                                         				  you configure video command
                                                         				  without configuring the camera command so that Cisco Unified SIP phones can switch from phone-based video
                                                         				  camera to CUVA. If you configure both video and camera commands together, you may need to manually remove the USB camera from Cisco
                                                         				  Unified SIP phones . |
| Note | Make sure
                                                         				  you configure video command
                                                         				  without configuring the camera command so that Cisco Unified SIP phones can switch from phone-based video
                                                         				  camera to CUVA. If you configure both video and camera commands together, you may need to manually remove the USB camera from Cisco
                                                         				  Unified SIP phones . |
| Step 6 | create profile Example: Router(config-register-global)# create profile | Generates
                                             				provisioning files required for SIP phones and writes the file to the location
                                             				specified with the tftp-path command. |
| Step 7 | exit Example: Router(config-register-global)#exit | Exits voice
                                             				register global configuration mode. |
| Step 8 | voice register pool pool tag Example: Router(config)#voice register pool 5 | Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone. |
| Step 9 | id mac address Example: Router(config-register-pool)#id mac 0009.A3D4.1234 | Explicitly
                                             				identifies a locally available individual SIP phone to support a degree of
                                             				authentication. |
| Step 10 | camera Example: Router(config-register-pool)#camera | Enables the camera command under voice register pool configuration mode. |
| Step 11 | video Example: Router(config-register-pool)#video | Enables the video command under voice register pool configuration mode. |
| Step 12 | exit Example: Router(config-register-pool)#exit | Exits voice
                                             				register pool configuration mode. |
| Step 13 | voice register template template-tag Example: Router(config)voice register template 10 | Enters voice
                                             				register template configuration mode to define a template of common parameters
                                             				for SIP phones in Cisco Unified CME. Range: 1
                                                   					 to 5. |
| Step 14 | camera Example: Router(config-register-template)#camera | Configures
                                             				the camera command under voice register template configuration mode. |
| Step 15 | video Example: Router(config-register-template)#video | Configures
                                             				the video command under voice register template configuration mode. |
| Step 16 | end Example: Router(config-register-template)# end | Returns to
                                             				privileged EXEC mode. |

| Note | Make sure
                                                         				  you configure video command
                                                         				  without configuring the camera command so that Cisco Unified SIP phones can switch from phone-based video
                                                         				  camera to CUVA. If you configure both video and camera commands together, you may need to manually remove the USB camera from Cisco
                                                         				  Unified SIP phones . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register global Example: Router(config)#voice register global | Enters voice
                                             				register global configuration mode to set parameters for all supported SIP
                                             				phones in Cisco Unified CME. |
| Step 4 | apply-config Example: Router(config-register-global)#apply-config | Applies
                                             				configuration for the Cisco Unified SIP IP phones and restarts all other SIP
                                             				phones. The apply-config command acts as a reset if configured on any other
                                             				phone type. |
| Step 5 | exit Example: Router(cfg-translation-rule)# exit | Exits voice
                                             				register global configuration mode. |
| Step 6 | voice register pool pool
                                                				  tag Example: Router(config)#voice register pool 5 | Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone. |
| Step 7 | apply-config Example: Router(config-register-pool)#apply-config | Applies
                                             				configuration for the Cisco Unified SIP IP phones and restarts all other SIP
                                             				phones. |
| Step 8 | end Example: Router(config-register-pool)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register global Example: Router(config)#voice register global | Enters voice
                                             				register global configuration mode to set parameters for all supported SIP
                                             				phones in Cisco Unified CME. |
| Step 4 | bandwidth video tias-modifier bandwidth value [ negotiate end-to-end ] Example: Router(config-register-global)#bandwidth video tias-modifier 512000 negotiate end-to-end | Allows to set
                                             				the maximum video bandwidth bits per second for SIP phones. bandwidth value —Bandwidth value in bits per
                                                   					 second. Range: 1 to 99999999. negotiate end-to-end —Bandwidth negotiation policy. Negotiates the minimum SIP-line video bandwidth in SDP end-to-end. |
| Step 5 | end Example: Router(config-register-global)# end | Returns to
                                             				privileged EXEC mode. |

| Restriction | Tandberg versions E3.0 and E4.1 and Polycom Release version 7.5.2
                                             			 are the only H.323 video endpoints supported by Cisco Unified CME. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice service voip Example: Router(config)# voice service voip | Enters voice-service configuration mode. |
| Step 4 | h323 Example: Router(config-voi-serv)# h323 | Enters H.323 voice-service configuration mode. |
| Step 5 | call start slow Example: Router(config-serv-h323)# call start slow | Forces an H.323 gateway to use slow-connect procedures for all
                                             				VoIP calls. |
| Step 6 | end Example: Router(config-serv-h323)# end | Returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 4 | service phone videoCapability { 0 \| 1 } Example: Router(config-telephony)# service phone videoCapability 1 | Enables or disables video capability parameter for all applicable IP phones associated with a Cisco Unified CME router. The parameter name is word and case-sensitive. 0 —Disable (default). 1 —Enable. |
| Step 5 | video Example: Router(config-telephony)# video | (Optional)
                                             				Enters video configuration mode. Required
                                                      					 only if you want to modify the maximum value of the video bandwidth for all
                                                      					 video-capable phones. |
| Step 6 | maximum bit-rate value Example: Router(conf-tele-video)# maximum bit-rate 256 | (Optional)
                                             				Sets the maximum IP phone video bandwidth, in kilobits per second. value —Range: 0 to 10000000. Default: 10000000. |
| Step 7 | end Example: Router(conf-tele-video)# end | Exits to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone phone-tag Example: Router(config)# ephone 6 | Enters ephone
                                             				configuration mode. phone-tag —Unique sequence number that identifies
                                                   					 an ephone during configuration tasks. |
| Step 4 | video Example: Router(config-ephone)# video | Enables video
                                             				capabilities on the specified ephone. |
| Step 5 | end Example: Router(config-ephone)# end | Exits ephone
                                             				configuration mode and enters privileged EXEC mode. |

| Use the show
                                                				  running-config command to verify the video settings in the
                                          			 configuration. See the
                                             				telephony-service portion of the output for commands that configure video
                                             				support on the Cisco Unified CME. See the ephone
                                             				portion of the output for commands that configure video support for a specific
                                             				ephone.The following example shows the telephony-service portion of the output: Example: telephony-service
			 video eo
			   maximum bit-rate 256 
			  load 7960-7940 P00306000404 
			  max-ephones 24
			  max-dn 24 
			  ip source-address 10.0.180.130 port 2000 
			  service phone videoCapability 1
			  timeouts interdigit 4 
			  timeouts ringing 100 
			  create cnf-files version-stamp Jan 01 2002 00:00:00 
			  keepalive 60
			  max-conferences 4 gain -6 
			  call-park system redirect
			  call-forward pattern .T
			  web admin system name cisco password cisco 
			  web customize load xml.jeff 
			  dn-webedit
			  time-webedit 
			  transfer-system full-consult 
			  transfer-pattern .T The following
                                             				example shows the ephone portion of the output: ephone  6
 video
 mac-address 000F.F7DE.CAA5
 type 7960
 button  1:6 |
|---|

| Feature
                                          					 Name | Cisco Unified CME Version | Feature
                                          					 Information |
|---|---|---|
| New Phone Support | 12.0 | Support was added for Cisco IP Phones 8845 and Cisco IP Phone
                                          					 8865 on Cisco Integrated Services Router Generation 2 (T-Train Release,
                                          					 15.7(3)M). |
| New Phone
                                          					 Support | 11.7 | Support
                                          					 was added for Cisco IP Phones 8845 and Cisco IP Phone 8865 on Cisco 4000 Series
                                          					 Integration Services Router. |
| SIP Trunk
                                          					 Video Support | 7.1 | Support
                                          					 was added for video calls between SCCP endpoints across different
                                          					 Cisco Unified CME routers connected through a SIP trunk. H.264
                                          					 codec support was added. |
| Video
                                          					 Support | 4.0 | Video
                                          					 support was introduced. |