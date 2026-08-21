---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cusrst-admin-sccp-sip-srst-configuration-guide-sccp-and-sip-srst-admin-guide-2c7018256e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cusrst/admin/sccp_sip_srst/configuration/guide/SCCP_and_SIP_SRST_Admin_Guide/srst_video_parameters.html
retrieved_at: 2026-08-21T02:49:34.959357+00:00
---

Cisco Unified SRST Administration Guide (All Versions)

# Cisco Unified SRST Administration Guide (All Versions)

Updated: April 25, 2026

Chapter: Setting Video Parameters

## Chapter: Setting Video Parameters

# Setting Video Parameters

This chapter describes how to set video parameters for a Cisco Unified Survivable Remote Site Telephony (SRST) Router.

## Prerequisites for Setting Video Parameters

Ensure that you are using Cisco Unified SRST 4.0 or a later version.

Ensure that you are using Cisco Unified Communications Manager 4.0 or a later version.

Ensure that the Cisco IP phones are registered with the Cisco Unified SRST router. Use the show ephone registered command to verify ephone registration.

Ensure that the connection between the Cisco Unified Video Advantage application and the Cisco Unified IP phone is up.

From a PC with Cisco Unified Video Advantage 1.02 or a later version installed, ensure that the line between the Cisco Unified
                                 Video Advantage and the Cisco Unified IP phone is green. For more information, see Cisco Unified Video Advantage End-User Guides .

Ensure that you install the correct video firmware on the Cisco Unified IP phone. Use the show ephone phone-load command to view current ephone firmware. The following lists the minimum firmware version for video-enabled Cisco Unified
                                 IP phones:

Cisco Unified IP Phone 7940G version 6.0(4)

Cisco Unified IP Phone 7960G version 6.0(4)

Cisco Unified IP Phone 7970G version 6.0(2)

Perform basic Cisco Unified SRST configuration. For more information, see Cisco Unified SRST V4.0: Setting Up the Network.

Perform basic ephone configuration. For more information, see Cisco Unified SRST V4.0: Setting Up Cisco Unified IP Phones.

## Restrictions for Setting Video Parameters

This feature supports only the following video codecs:

H.261

H.263

H.264 (for CUVA from SRST 7.1)

This feature supports only the following video formats:

Common Intermediate Format (CIF): Resolution 352x288

One-Quarter Common Intermediate Format (QCIF): Resolution 176x144

Sub QIF (SQCIF): Resolution 128x96

4CIF: Resolution 704x576

16CIF: Resolution 1408x1152

The call start fast feature does not support an H.323 video connection. You must configure call start slow for H.323 video.

Video capabilities are configured per ephone, not per line.

All call feature controls (for example, mute and hold) apply to both audio and video calls, if applicable.

This feature does not support the following:

Dynamic addition of video capability: The video capability must be present before the call setup starts to allow the video
                                 connection.

T-120 data connection between two SCCP endpoints

Video security

Far-end camera control (FECC) for SCCP endpoints

Video codec renegotiation: The negotiated video codec must match or the call falls back to audio-only. The negotiated codec
                                 for the existing call can be used for an incoming call. Video codec transcoding

When a video-capable endpoint connects to an audio-only endpoint, the call falls back to audio-only. During audio-only calls,
                                 video messages are skipped.

## Information About Setting Video Parameters

This feature allows you to set video parameters for the Cisco Unified SRST to maintain close feature parity with Cisco Unified
                           Communications Manager. When the Cisco Unified SRST is enabled, Cisco Unified IP phones do not have to be reconfigured for
                           video capabilities because all ephones retain the same configuration used with Cisco Unified Communications Manager. However,
                           you must enter call-manager-fallback configuration mode to set video parameters for Cisco Unified SRST. The feature set for
                           video is the same as the Cisco Unified SRST audio calls.

To set video parameters, refer the following concepts:

### Matching Endpoint Capabilities

Cisco Unified SRST stores Endpoint capabilities during the phone registration. These capabilities are used to match with other
                              endpoints during the call setup. Endpoints can update at any time; however, the router recognizes endpoint capability changes
                              only during the call setup. If you add a video feature to a phone, the information about it is updated in the router’s internal
                              data structure. However, the information does not take effect until the next call. If a video feature is revoked, the router
                              continues to view the video capability until the call stops. However, there is no video stream that is exchanged between the
                              two endpoints.

The endpoint capability match is executed every time when an incoming call is set up or an existing call is resumed.

### Retrieving Video Codec Information

Voice gateways use dial-peer configurations to retrieve codec information for audio codecs. Video codec selection is done
                              by the endpoints and is not controlled by the H.323 service-provider interface (SPI) through dial-peer or other configuration.
                              The video-codec information is retrieved from the SCCP endpoint using a capabilities request during the call setup.

### Call Fallback to and Audio-Only Endpoint

When a video-capable endpoint connects to an audio-only endpoint, the call falls back to an audio-only connection. Also, for
                              certain features such as conferencing, where video support is not available, the call falls back to audio-only.

Cisco Unified SRST routers use a call-type flag to indicate whether the call is video-capable or audio-only. The call-type
                              flag is set to video when the video capability is matched or set to audio-only when connecting to an audio-only TDM or an
                              audio-only SIP endpoint.

During an audio-only connection, all video-related media messages are skipped.

### Call Setup for Video Endpoints

The process for handling SCCP video endpoints is the same as that for handling SCCP audio endpoints. The video call must be
                              part of the audio call. If the audio call setup fails, the video call fails.

During call setup for video, media setup handling determines if a video-media path is required or not. If so, the corresponding
                              video-media-path setup actions are taken.

For an SCCP endpoint, video-media-path setup includes sending messages to the endpoints to open a multimedia path and start
                                    the multimedia transmission.

For an H.323 endpoint, video-media-path setup includes an Exchange between the endpoints to open a logical channel for the
                                    video stream.

A call-type flag is set during the call setup on the basis of the endpoint and capability match. After call setup, the call
                              -type flag is used to determine whether an extra video-media path is required. Call signaling is managed by the Cisco Unified
                              Communications Manager Express router, and the media stream is directly connected between the two video-enabled SCCP endpoints
                              on the same router. Video-related commands and flow-control messages are forwarded to the other endpoint. Routers do not interpret
                              these messages.

#### Call Setup Between Two Local SCCP Endpoints

For interoperation between two local SCCP endpoints (that exist on the same router), video call setup uses all existing audio-call-setup
                                 handling, except during the media setup. During the media setup, a message is sent to establish the video-media path. If the
                                 endpoint responds, the video-media path is established and invokes a start-multimedia-transmission function.

#### Call Setup Between SCCP and H.323 Endpoints

Call setup between SCCP and H.323 endpoints is the same as it is between SCCP endpoints except that, if video capability is
                                 selected, the event is posted to the H.323 call leg to send out a video open logical channel (OLC) and the gateway generates
                                 an OLC for the video channel. Because the router needs to both stop and originate the media stream, video must be enabled
                                 on the router before call setup begins.

#### Call Setup Between Two SCCP Endpoints Across an H.323 Network

If the call setup between SCCP endpoints occurs across an H.323 network, the setup is a combination of the processes listed
                                 in the previous two sections. The router controls the video media setup between the two endpoints, and the event is posted
                                 to the H.323 call leg so that the gateway can generate an OLC.

### Flow of the RTP Video Stream

For video streams between two local SCCP endpoints, the Real-Time Transport Protocol (RTP) stream is in flow-around mode.
                              For video streams between SCCP and H.323 endpoints or two SCCP endpoints on different Cisco Unified Communications Manager
                              Express routers, the RTP stream is in flow-through mode.

Media flow-around mode enables RTP packets to stream directly between the endpoints of a VoIP call without the involvement
                                    of the gateway. By default, the gateway receives the incoming media, stops the call, and then reoriginates it on the outbound
                                    call leg. In flow-around mode, only signaling data is passed to the gateway, improving scalability and performance.

Media flow-through mode involves the same video-media path as for an audio call. Media packets flow through the gateway, thus
                                    hiding the networks from each other.

To display information about RTP named-event packets, such as caller-ID number, IP address, and port for both the local and
                              remote endpoints, use the show voip rtp connection command as shown in the following sample output:

```
Router# show voip rtp connections
VoIP RTP active connections :
No. CallId dstCallId LocalRTP RmtRTP LocalIP RemoteIP
1 102 103 18714 18158 10.1.1.1 192.168.1.1
2 105 104 17252 19088 10.1.1.1 192.168.1.1
Found 2 active RTP connections
============================
```

### How to Set Video Parameters for Cisco Unified SRST

When you enable the Cisco Unified SRST, do not reconfigure the Cisco Unified IP phones for video capabilities. All ephones
                              retain the same configuration used with Cisco Unified Communications Manager. However, you can set video parameters for Cisco
                              Unified SRST.

The following are the task for setting Video parameters for Cisco Unified SRST:

#### Configuring Slow Connect Procedures

Video streams require slow-connect procedures for Cisco Unified SRST. H.323 endpoints require a slow connect because the endpoint-capability
                                    match occurs after the connect message.

For more information about slow-connect procedures, see Configuring Quality of Service for Voice.

Use the following procedure to configure slow-connect procedures.

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- h323

- call start slow

### DETAILED STEPS

Step 1

enable

##### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

##### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

voice service voip

##### Example:

```
Router(config)# voice service voip
```

Enters voice-service configuration mode.

Step 4

h323

##### Example:

```
Router(config-voi-serv)# h323
```

Enters H.323 voice-service configuration mode.

Step 5

call start slow

##### Example:

```
Router(config-serv-h323)# call start slow
```

Forces an H.323 gateway to use slow-connect procedures for all VoIP calls.

#### Verifying Cisco Unified SRST

Use the following procedure to verify that the Cisco Unified SRST feature is enabled and to verify Cisco Unified IP phone
                                    configuration settings.

### SUMMARY STEPS

- enable

- show running config

- show call-manager-fallback all

### DETAILED STEPS

Step 1

enable

##### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

show running config

##### Example:

```
Router# show running config
```

Displays the entire contents of the running configuration file.

Step 3

show call-manager-fallback all

##### Example:

```
Router# show call-manager-fallback all
```

Displays the detailed configuration of all Cisco Unified IP phones, directory numbers, voice ports, and dial peers in your
                                                network while in fallback mode.

Use the Settings display on the Cisco Unified IP phones in your network to verify that the default router IP address on the
                                                            phones matches the IP address of the Cisco Unified SRST router.

##### Example

The following example shows output from the show call-manager-fallback all command:

```
Router# show call-manager-fallback all
CONFIG (Version=3.3)
=====================
Version 3.3
For on-line documentation please see:
www.cisco.com/univercd/cc/td/doc/product/access/ip_ph/ip_ks/index.htm
ip source-address 10.1.1.1 port 2000
max-video-bit-rate 384(kbps)
max-ephones 52
max-dn 110
max-conferences 16 gain -6
dspfarm units 0
dspfarm transcode sessions 0
huntstop
dialplan-pattern 1 4084442... extension-length 4
voicemail 6001
moh music-on-hold.au
time-format 24
date-format dd-mm-yy
timezone 0 Greenwich Standard Time
call-forward busy 6001
call-forward noan 6001 timeout 8
call-forward pattern .T
transfer-pattern .T
keepalive 45
timeout interdigit 10
timeout busy 10
timeout ringing 180
caller-id name-only: enable
Limit number of DNs per phone:
7910: 34
7935: 34
7936: 34
7940: 34
7960: 34
7970: 34
Log (table parameters):
max-size: 150
retain-timer: 15
transfer-system full-consult
local directory service: enabled.
ephone-dn 1
number 1001
name 1001
description 1001
label 1001
preference 0 secondary 9
huntstop
call-forward busy 6001
call-forward noan 6001 timeout 8
call-waiting beep
ephone-dn 2
number 1002
name 1002
description 1002
preference 0 secondary 9
huntstop
call-forward busy 6001
call-forward noan 6001 timeout 8
call-waiting beep
ephone-dn 3
preference 0 secondary 9
huntstop
call-waiting beep
ephone-dn 4
preference 0 secondary 9
huntstop
call-waiting beep
ephone-dn 5
preference 0 secondary 9
huntstop
call-waiting beep
ephone-dn 6
preference 0 secondary 9
huntstop
call-waiting beep
ephone-dn 7
preference 0 secondary 9
huntstop
call-waiting beep
ephone-dn 8
preference 0 secondary 9
huntstop
call-waiting beep
ephone-dn 9
preference 0 secondary 9
huntstop
call-waiting beep
ephone-dn 10
preference 0 secondary 9
huntstop
call-waiting beep
ephone-dn 11
preference 0 secondary 9
huntstop
call-waiting beep
ephone-dn 12
preference 0 secondary 9
huntstop
call-waiting beep
ephone-dn 13
preference 0 secondary 9
huntstop
call-waiting beep
ephone-dn 14
preference 0 secondary 9
huntstop
call-waiting beep
ephone-dn 15
preference 0 secondary 9
huntstop
call-waiting beep
ephone-dn 16
preference 0 secondary 9
huntstop
call-waiting beep
ephone-dn 17
preference 0 secondary 9
huntstop
call-waiting beep
ephone-dn 18
preference 0 secondary 9
huntstop
call-waiting beep
ephone-dn 19
preference 0 secondary 9
huntstop
call-waiting beep
ephone-dn 20
preference 0 secondary 9
huntstop
call-waiting beep
Number of Configured ephones 0 (Registered 2)
voice-port 50/0/1
station-id number 1001
station-id name 1001
timeout ringing 8
!
voice-port 50/0/2
station-id number 1002
station-id name 1002
timeout ringing 8
!
voice-port 50/0/3
!
voice-port 50/0/4
!
voice-port 50/0/5
!
voice-port 50/0/6
!
voice-port 50/0/7
!
voice-port 50/0/8
!
voice-port 50/0/9
!
voice-port 50/0/10
!
voice-port 50/0/11
!
voice-port 50/0/12
!
voice-port 50/0/13
!
voice-port 50/0/14
!
voice-port 50/0/15
!
voice-port 50/0/16
!
voice-port 50/0/17
!
voice-port 50/0/18
!
voice-port 50/0/19
!
voice-port 50/0/20
!
dial-peer voice 20055 pots
destination-pattern 1001
huntstop
call-forward busy 6001
call-forward noan 6001
progress_ind setup enable 3
port 50/0/1
dial-peer voice 20056 pots
destination-pattern 1002
huntstop
call-forward busy 6001
call-forward noan 6001
progress_ind setup enable 3
port 50/0/2
dial-peer voice 20057 pots
huntstop
progress_ind setup enable 3
port 50/0/3
dial-peer voice 20058 pots
huntstop
progress_ind setup enable 3
port 50/0/4
dial-peer voice 20059 pots
huntstop
progress_ind setup enable 3
port 50/0/5
dial-peer voice 20060 pots
huntstop
progress_ind setup enable 3
port 50/0/6
dial-peer voice 20061 pots
huntstop
progress_ind setup enable 3
port 50/0/7
dial-peer voice 20062 pots
huntstop
progress_ind setup enable 3
port 50/0/8
dial-peer voice 20063 pots
huntstop
progress_ind setup enable 3
port 50/0/9
dial-peer voice 20064 pots
huntstop
progress_ind setup enable 3
port 50/0/10
dial-peer voice 20065 pots
huntstop
progress_ind setup enable 3
port 50/0/11
dial-peer voice 20066 pots
huntstop
progress_ind setup enable 3
port 50/0/12
dial-peer voice 20067 pots
huntstop
progress_ind setup enable 3
port 50/0/13
dial-peer voice 20068 pots
huntstop
progress_ind setup enable 3
port 50/0/14
dial-peer voice 20069 pots
huntstop
progress_ind setup enable 3
port 50/0/15
dial-peer voice 20070 pots
huntstop
progress_ind setup enable 3
port 50/0/16
dial-peer voice 20071 pots
huntstop
progress_ind setup enable 3
port 50/0/17
dial-peer voice 20072 pots
huntstop
progress_ind setup enable 3
port 50/0/18
dial-peer voice 20073 pots
huntstop
progress_ind setup enable 3
port 50/0/19
dial-peer voice 20074 pots
huntstop
progress_ind setup enable 3
port 50/0/20
tftp-server system:/its/SEPDEFAULT.cnf
tftp-server system:/its/SEPDEFAULT.cnf alias SEPDefault.cnf
tftp-server system:/its/XMLDefault.cnf.xml alias XMLDefault.cnf.xml
tftp-server system:/its/ATADefault.cnf.xml
tftp-server system:/its/united_states/7960-tones.xml alias United_States/7960-tones.xml
tftp-server system:/its/united_states/7960-font.xml alias
English_United_States/7960-font.xml
tftp-server system:/its/united_states/7960-dictionary.xml alias
English_United_States/7960-dictionary.xml
tftp-server system:/its/united_states/7960-kate.xml alias
English_United_States/7960-kate.xml
tftp-server system:/its/united_states/SCCP-dictionary.xml alias
English_United_States/SCCP-dictionary.xml
tftp-server system:/its/XMLDefault7960.cnf.xml alias SEP003094C2772E.cnf.xml
tftp-server system:/its/XMLDefault7960.cnf.xml alias SEP001201372DD1.cnf.xml
tftp-server system:/its/XMLDefault7960.cnf.xml alias SEPFFDD00000001.cnf.xml
tftp-server system:/its/XMLDefault7960.cnf.xml alias SEPFFDD00000002.cnf.xml
tftp-server system:/its/XMLDefault7960.cnf.xml alias SEPFFDD00000003.cnf.xml
tftp-server system:/its/XMLDefault7960.cnf.xml alias SEPFFDD00000004.cnf.xml
tftp-server system:/its/XMLDefault7960.cnf.xml alias SEPFFDD00000005.cnf.xml
tftp-server system:/its/XMLDefault7960.cnf.xml alias SEPFFDD00000006.cnf.xml
tftp-server system:/its/XMLDefault7960.cnf.xml alias SEPFFDD00000007.cnf.xml
tftp-server system:/its/XMLDefault7960.cnf.xml alias SEPFFDD00000008.cnf.xml
tftp-server system:/its/XMLDefault7960.cnf.xml alias SEPFFDD00000009.cnf.xml
tftp-server system:/its/XMLDefault7960.cnf.xml alias SEPFFDD0000000A.cnf.xml
tftp-server system:/its/XMLDefault7960.cnf.xml alias SEPFFDD0000000B.cnf.xml
tftp-server system:/its/XMLDefault7960.cnf.xml alias SEPFFDD0000000C.cnf.xml
tftp-server system:/its/XMLDefault7960.cnf.xml alias SEPFFDD0000000D.cnf.xml
tftp-server system:/its/XMLDefault7960.cnf.xml alias SEPFFDD0000000E.cnf.xml
tftp-server system:/its/XMLDefault7960.cnf.xml alias SEPFFDD0000000F.cnf.xml
tftp-server system:/its/XMLDefault7960.cnf.xml alias SEPFFDD00000010.cnf.xml
tftp-server system:/its/XMLDefault7960.cnf.xml alias SEPFFDD00000011.cnf.xml
tftp-server system:/its/XMLDefault7960.cnf.xml alias SEPFFDD00000012.cnf.xml
```

#### Setting Video Parameters for Cisco Unified SRST

Using the following procedure to set the maximum bit rate for all video-capable phones in a Cisco Unified SRST system.

### SUMMARY STEPS

- enable

- configure terminal

- dcall-manager-fallback

- video

- maximum bit-rate value

### DETAILED STEPS

Step 1

enable

##### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

##### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

dcall-manager-fallback

##### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 4

video

##### Example:

```
Router(config-call-manager-fallback)# video
```

Enters call-manager-fallback video configuration mode.

Step 5

maximum bit-rate value

##### Example:

```
Router(conf-cm-fallback-video)# maximum
bit-rate 256
```

Sets the maximum IP phone video bandwidth, in kbps. The range is 0 to 10000000. The default is 10000000.

##### Example

The following example shows the configuration for video with Cisco Unified SRST:

```
call-manager-fallback
video
maximum bit-rate 384
max-conferences 2 gain -6
transfer-system full-consult
ip source-address 10.0.1.1 port 2000
max-ephones 52
max-dn 110
dialplan-pattern 1 4084442... extension-length 4
transfer-pattern .T
keepalive 45
voicemail 6001
call-forward pattern .T
call-forward busy 6001
call-forward noan 6001 timeout 3
moh music-on-hold.au
time-format 24
date-format dd-mm-yy
!
```

### Troubleshooting Video for Cisco Unified SRST

Use the following commands to troubleshoot Video for Cisco Unified SRST.

For SCCP endpoint troubleshooting, use the following debug commands:

Debug cch323 video: Enables the video debugging trace on the H.323 SPI.

Debug ephone detail: Debugs all Cisco Unified IP phones that are registered to the router and displays error and state levels.

Debug h225 asn1: Displays Abstract Syntax Notation One (ASN.1) contents of H.225 messages that are sent or received.

Debug h245 asn1: Displays ASN.1 contents of H.245 messages that are sent or received.

Debug VoIP CCAPI inout: Displays the execution path through the call-control-application programming interface (CPI).

For ephone troubleshooting, use the following debug commands:

Debug ephone message: Enables message tracing between Cisco ephones.

Debug ephone register: Sets registration debugging for ephones.

Debug ephone video: Sets ephone video traces, which provide information about different video states for the call, including
                                          video capabilities selection, start, and stop.

For basic video-to-video call checking, use the following show commands:

Show call active video: Displays call information for SCCP video CallsInProgress.

Show ephone off hook: Displays information and packet counts for ephones that are currently off hook.

Show VoIP RTP connections: Displays information about RTP named-event packets, such as caller ID number, IP address, and port,
                                          for both the local and remote endpoints.

| Note | The endpoint capability match is executed every time when an incoming call is set up or an existing call is resumed. |
|---|---|

| Note | During an audio-only connection, all video-related media messages are skipped. |
|---|---|

| Note | For more information about slow-connect procedures, see Configuring Quality of Service for Voice. Use the following procedure to configure slow-connect procedures. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice service voip Example: Router(config)# voice service voip | Enters voice-service configuration mode. |
| Step 4 | h323 Example: Router(config-voi-serv)# h323 | Enters H.323 voice-service configuration mode. |
| Step 5 | call start slow Example: Router(config-serv-h323)# call start slow | Forces an H.323 gateway to use slow-connect procedures for all VoIP calls. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | show running config Example: Router# show running config | Displays the entire contents of the running configuration file. |
| Step 3 | show call-manager-fallback all Example: Router# show call-manager-fallback all | Displays the detailed configuration of all Cisco Unified IP phones, directory numbers, voice ports, and dial peers in your
                                                network while in fallback mode. Note Use the Settings display on the Cisco Unified IP phones in your network to verify that the default router IP address on the
                                                            phones matches the IP address of the Cisco Unified SRST router. | Note | Use the Settings display on the Cisco Unified IP phones in your network to verify that the default router IP address on the
                                                            phones matches the IP address of the Cisco Unified SRST router. |
| Note | Use the Settings display on the Cisco Unified IP phones in your network to verify that the default router IP address on the
                                                            phones matches the IP address of the Cisco Unified SRST router. |

| Note | Use the Settings display on the Cisco Unified IP phones in your network to verify that the default router IP address on the
                                                            phones matches the IP address of the Cisco Unified SRST router. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | dcall-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 4 | video Example: Router(config-call-manager-fallback)# video | Enters call-manager-fallback video configuration mode. |
| Step 5 | maximum bit-rate value Example: Router(conf-cm-fallback-video)# maximum
bit-rate 256 | Sets the maximum IP phone video bandwidth, in kbps. The range is 0 to 10000000. The default is 10000000. |