---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-15-design-guide-b-15cucdg-b-15cucdg-chapter-01101-html-8a03dc3dca
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/design/guide/b_15cucdg/b_15cucdg_chapter_01101.html
retrieved_at: 2026-08-17T02:15:43.185014+00:00
---

Design Guide for Cisco Unity Connection 15

# Design Guide for Cisco Unity Connection 15

Updated: August 12, 2025

Chapter: Video
	 Messaging

## Chapter: Video
	 Messaging

# Video
                     	 Messaging

Cisco Media Sense is now end of life and end of support, hence Unity Connection will no longer provide the Video Messaging
                                    feature for users.For more information on Cisco Media Sense EOL, see https://www.cisco.com/c/en/us/products/collateral/customer-collaboration/mediasense/eos-eol-notice-c51-738857.html .

Beginning with
                        		Unity Connection 11.5(1) and later, in addition to audio message, a user or an
                        		outside caller can also send video message to another user using video enabled
                        		endpoint. To record and send a video message, make sure that:

- Video messaging is enabled
                              		  in Unity Connection for the user.

- Endpoint is video enabled.

For more information
                        		on supported video endpoints, see the Video Compatibility Matrix section of the Compatibility
                           		  Matrix for Cisco Unity Connection at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/compatibility/matrix/b_cucclientmtx.html .

A user or an outside
                        		caller can send video message to another user only in case of Ring No Answer
                        		(RNA). If a video enabled user dials a call handler extension, the call remains
                        		an audio call as the call handler neither has a video service account nor it is
                        		associated with any class of service.

Consider the
                        		following figure showing the video messaging architecture when a user or
                        		outside caller sends a video message to the other user in case of RNA.

In the above
                        		figure, a user or an outside caller that is User A dials the extension of User
                        		B but User B does not answer the call, which means RNA. Now the call is
                        		forwarded to the mailbox of User B configured on Unity connection and the video
                        		greeting of User B is played back. After the greeting is played, User A records
                        		and sends the video message to User B and the message gets stored in mailbox of
                        		User B. To access the video message sent by User A, User B sign-ins to the
                        		mailbox on Unity Connection and accesses the video message.

For information managing video messages, see "Managing Video Messages" chapter of User Guide for the Cisco Unity Connection Phone Interface at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/user/guide/phone/b_15cucugphone.html .

Video messaging is
                        		also supported if the Attempt Sign-In, Sub Sign-In, Attempt Forward and
                        		Greetings Administrator routing rule is set for the user.

## Video
                        	 Greeting

Video greeting
                           		feature allows the user to record a greeting in video format from a
                           		video-enabled end point. A user or an outside caller can access the video
                           		greetings only when calling from a video enabled endpoint (for example, a
                           		telephone with video display) to a video enabled user mailbox in Unity
                           		Connection. However, when calling from a non video enabled endpoint, the
                           		callers can only access the audio part of the video greetings. Video greetings
                           		for outside callers is enabled through the class of service of the subscribed
                           		users.

- Standard

- Busy

- Alternate

- Internal

- Closed

- Holiday

## Platform support
                        	 for Video

The video messaging is supported only with 7 vCPU OVA. Each
                           		Unity Connection server (standalone or cluster) can support up to 20 concurrent
                           		video calls.

MediaSense must also be deployed using the larger 7vCPU OVA. The
                           		MediaSense needs to be installed as a single server and cannot be part of a
                           		cluster. A Unity Connection cluster or a single server can be integrated with a
                           		MediaSense server.

The MediaSense server must be co-located with Unity Connection
                           		with 1Gbps connectivity between the servers and less than 10ms Round Trip Time
                           		(RTT) latency. Unity Connection will be profiling further for bandwidth and
                           		higher latency links in later releases to allow for a wider range of deployment
                           		options.

While recording a video message, if the communication between Unity
                                       		  Connection and MediaSense is lost, the call gets converted to audio. If a video
                                       		  call is converted to audio because of no response from MediaSense, it cannot be
                                       		  restored again as a video.

## Blanking
                        	 Files

Due to differing behavior of some video devices, the ‘blanking’
                           		file is used for the video messaging feature. The blanking file fills in the
                           		video RTP stream when Unity Connection and MediaSense would otherwise not be
                           		sending video. Without the blanking file, users may either experience video
                           		window closing on the device or the last received video frame freezing on the
                           		screen.

There is a sample blanking file located at http://www.ciscounitytools.com/Applications/MediaSense/VideoBlankingFiles/

This file needs to be uploaded to the MediaSense that Unity
                           		Connection is integrated with the following information:

Title: CiscoUnityConnectionLogo.mp4

Description: <Enter a brief description>

Filename: CiscoUnityConnectionLogo.mp4

The blanking file must be an MP4 video file with a resolution
                           		640x360 (360p) using H.264 codec at 30 frames per second. The blanking file
                           		needs to include an empty or null audio track. MediaSense requires an audio
                           		track; however silence is preferred for the blanking file so it does not
                           		distract the user during the use of the video messaging.

Due to the Cisco Unified Communications Manager regions settings
                           		in the “Video
                              		  Greetings Operation” section, the blanking files of video greetings and
                           		messages should be recorded at an average or constant bit rate of 600kbps to
                           		allow the administrator to better calculate the bandwidth requirements of the
                           		video messaging deployment.

## Video
                        	 Operation

Unity Connection supports video messaging only with SIP trunk integrations. MediaSense and Unity Connection allows the recording
                           of video greetings and messages up to 1080p (1920x1080), however this offers limited compatibility across the video-enabled
                           phone portfolio and is not a supported configuration as MediaSense does not support transcoding video to reduce the resolution
                           for non-1080p video devices. To restrict video greetings and messages to 360p, Unity Connection leverages the use of Communications
                           Manager's Region configurations. The Unity Connection SIP Trunks need to be put in a region that has the following relationship
                           settings with all other regions containing video-enabled devices that might call Unity Connection and expect video greetings
                           and messages:

Audio Codec Preference List: (Default or Administrator's
                           		Preference)

Maximum Audio Bit Rate: 64 kbps

Maximum Session Bit Rate for Video Calls: 600kbps

Maximum Session Bit Rate for Immersive Video Calls: 600kbps

In Unity Connection 10.5(2) and later, the administrator can
                           		configure any of the following supported video resolution:

360p (640x360)

480p (720x480)

720p (1280x720)

1080p (1920x1080)

The new supported video resolutions allow Unity Connection to
                           		support various video-enabled phone portfolio, however, MediaSense does not
                           		support video transcoding. The administrator needs to configure the video
                           		region settings in Cisco Unified CM, depending on the video resolution selected
                           		in Cisco Unity Connection Administration. To configure video resolution,
                           		navigate to Cisco Unity Connection Administration> Port Group> Port Group
                           		Basics> Change Advertising> Video Resolution.

For an active-standby Unity Connection cluster deployment over a
                           		WAN connection, use the following region settings for the SIP trunk to the
                           		Unity Connection server that is not co-located with MediaSense. This disables
                           		the video greetings using the secondary node. Audio-only greetings continue to
                           		function.

Audio Codec Preference List: (Default or Administrator's
                           		Preference)

Maximum Audio Bit Rate: 64 kbps

Maximum Session Bit Rate for Video Calls: Select "None"

Maximum Session Bit Rate for Immersive Video Calls: Select
                           		“None”

These settings ensure maximum compatibility across the Cisco
                           		video-enabled phone portfolio and provide the best possible experience for
                           		using video messaging.

When recording a video greeting or message, the audio and video
                           		RTP streams are both sent directly to Unity Connection. Unity Connection saves
                           		the audio RTP stream locally as an audio-only version of the video greeting or
                           		message and forks the audio and video RTP streams to MediaSense for recording.
                           		For playback, if the device is video-enabled, Unity Connection instructs
                           		MediaSense to stream the video greeting or message to Unity Connection to be
                           		forked to the device. If MediaSense is not available or unable to playback the
                           		video greetings or messages or if the device calling Unity Connection is not
                           		video-enabled, then Unity Connection plays the audio-only portion of the video
                           		greeting or message that it recorded. The audio-only greeting or message is the
                           		audio track from the video greeting or video message. It is possible to have
                           		different greetings for audio-only callers and video-enabled callers.

## Cisco VCS
                        	 Interoperability

The Unity Connection team has not tested calling through a VCS
                           		or calling from devices registered to a VCS and as such, these call flows are
                           		not supported. At current, the Unity Connection team is aware of an issue with
                           		certain devices registered to a VCS where video is not negotiated and
                           		audio-only greetings are played or recorded. While not currently supported,
                           		Cisco Unified CM registered devices calling through a VCS are typically able to
                           		play and record new video messages or greetings.

## Video Greetings
                        	 Enabled Call Handlers

With Unity Connection 11.x, user can record video greetings for
                           		call handlers. Audio and video greeting for the call handler can be recorded by
                           		the owner assigned to the call handler only.

## Limitations

Video messaging is
                           		not supported in below mentioned scenarios:

- IPv6 format

- Dispatch and Broadcast

- SCCP integration

- Voice User Interface (VUI )

- Cross-Box Transfer

- Cross-Box Login

- Directory handler

- Interview handler

- System call handler

For more information on enabling video messaging, see the Task List for Configuring Video Greetings and Massaging section of the “Video” chapter in the System Administration Guide for Cisco Unity Connection, Release 15, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/administration/guide/b_15cucsag.html .

| Note | Cisco Media Sense is now end of life and end of support, hence Unity Connection will no longer provide the Video Messaging
                                    feature for users.For more information on Cisco Media Sense EOL, see https://www.cisco.com/c/en/us/products/collateral/customer-collaboration/mediasense/eos-eol-notice-c51-738857.html . |
|---|---|

| Note | Once a user is
                                    		  signed in to Unity Connection, even if the video messaging is enabled for a
                                    		  user, the user can not compose a video message. The user can only play the
                                    		  video messages received from the users or outside callers through RNA
                                    		  scenarios. |
|---|---|

| Note | If a video
                                 		messaging enabled user or outside caller records a message, it completely
                                 		depends upon the endpoint if the video call will be established or not. For
                                 		example, if the user records a message on Cisco 8865 or 8845 series video phone
                                 		with the camera shutter closed, no video streaming happens for the message. But
                                 		for other endpoints, a blank video is recorded. |
|---|---|

| Note | Error greetings
                                       		are played as audio only. |
|---|---|

| Note | The
                                    		video messaging is supported in both co-located Unity Connection active-active
                                    		cluster deployment and Unity Connection active-standby cluster deployment over
                                    		the WAN. The video messaging is not supported in an active-active cluster
                                    		deployment over the WAN. |
|---|---|

| Note | While recording a video message, if the communication between Unity
                                       		  Connection and MediaSense is lost, the call gets converted to audio. If a video
                                       		  call is converted to audio because of no response from MediaSense, it cannot be
                                       		  restored again as a video. |
|---|---|