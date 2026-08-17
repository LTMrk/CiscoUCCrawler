---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-troubleshooting-guide-b-14cuctsg-b-14cuctsg-chapter-01100-html-2df18066de
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/troubleshooting/guide/b_14cuctsg/b_14cuctsg_chapter_01100.html
retrieved_at: 2026-08-17T02:17:16.037716+00:00
---

Troubleshooting Guide for Cisco Unity Connection Release 14

# Troubleshooting Guide for Cisco Unity Connection Release 14

Updated: August 14, 2024

Chapter: Troubleshooting
	 Video Messaging

## Chapter: Troubleshooting
	 Video Messaging

# Troubleshooting
                     	 Video Messaging

## Troubleshooting
                        	 Video Messaging

### Error Message Appears When You Test the Connectivity of Video Services

You may receive the following error messages on the Edit Video Service page of Cisco Unity Connection Administration when
                              you test the connectivity of Unity Connection with the video server:

“Video Server cannot be contacted by pinging.”

If you receive the “Video Server cannot be contacted by pinging.” error message on the Tasks Execution Results page while
                              testing connectivity of Unity Connection with the video server, make sure:

The DNS server is up and running.

The FQDN, IP address, or hostname of the video server entered on the Edit Video Service page is correct.

If the DNS server is not available, make sure that you enter only the IP address in the Video Server Field and the Allow Self
                                                Signed Certificate for Video Servers check box is checked.

The state of video server is active and running.

The system firewall is not blocking ICMP protocol.

“Video server is not responding on the port <port number>.”:

If you receive the “Video server is not responding on the port <port number>.” error message on the Tasks Execution Results
                              page when you test the connectivity of the Unity Connection with video server, make sure that the port number entered on the
                              Edit Video Service page is correct.

“Username or password is incorrect.”:

If you receive the “Username or password is incorrect.” error message on the Tasks Execution Results page when you test the
                              connectivity of the Unity Connection with video server, make sure that the username and password of video server entered on
                              the Edit Video Service page are correct.

“Failure in validating the video server certificates.”:

If you receive the “Failure in validating the video server certificates.” error message on the Tasks Execution Results page
                              when you test the connectivity of the Unity Connection with video server, make sure:

The DNS server is up and running.

The valid video server certificates are uploaded on Unity Connection. If the valid video server certificates are not uploaded,
                                    make sure that the third-party video server certificates are uploaded and the Allow Self Signed Certificate for Video Server
                                    check box is not checked on the New Video Service page.

If the DNS server is not available, make sure that you enter only the IP address in the Video Server field and the Allow Self
                                                Signed Certificate for Video Server check box is checked.

### Error Message Appears When You Test the Connectivity of Video Service Account with Video Services

You may receive the following error messages on the Video Service Accounts Status page of Cisco Unity Connection Administration
                              when you test the connectivity of the video service account (of a user) with video services:

“The Enable Video settings are disabled for this user in the Edit Class of Service page.”

If you receive the “The Enable Video settings are disabled for this user in the Edit Class of Service page.” error message
                              on the Tasks Execution Results page when you test the configuration of video service account with video services, make sure
                              that you have selected the Enable Video settings in the Edit Class of Service page for that user.

“Video service is disabled.”

If you receive the “Video service is disabled.” error message on the Tasks Execution Results page when you test the configuration
                              of the video service account with video services, make sure that you have selected the Enabled option in the Edit Video Service
                              page.

You may receive the same error messages that appeared when testing the connectivity of Unity Connection with video server.
                                    For more information on error messages, see “Error Message Appears When You Test the Connectivity of Video Services” section on page 13-1 .

### Unable to Establish Video Call through Telephone User Interface (TUI)

If a user login via direct sign-in using telephone user interface and is unable to establish a video call, check the following:

The DNS server is up and running. If the DNS server is not available, make sure that you enter only the IP address in the
                                    Video Server field and the Allow Self Signed Certificate for Video Server check box is checked.

Make sure that the Cisco Camera and Video Capabilities options are enabled for the device in Cisco Unified Communications
                                    Manager.

Make sure that the state of video server is up and running using the Test button on the Edit Video Service page.

Make sure that you have restarted the Connection Conversation Manager service after updating the video service.

Check the connectivity of video service account (of a user) with video server.

Check whether the Map Video Service option is enabled in video service account for the user.

Check whether the H.264 video format (or codec) is advertised for integrating with video endpoint.

Make sure that you integrate Unity Connection with Cisco Unified Communications Manager over SIP.

Make sure that the root certificate of video server is uploaded in Tomcat-trust of Unity Connection.

Make sure that each server in a Unity Connection cluster does not exceed the maximum of 25 concurrent video calls.

### Unable to record
                           	 Video greeting or message through Telephone User Interface (TUI)

If a user is unable to record video greetings or messages using
                              		telephone user interface, check whether the state of video server using the
                              		Test button on the Edit Video Service page.

### Unable to playback Video greeting through Telephone User Interface (TUI)

If a user login via direct sign-in using telephone user interface and is unable to playback video greetings, consider the
                              following:

Check whether the state of video server is active and running using the Test button on the Edit Video Service page.

Check whether the My Personal Recording option is enabled for video greetings in the Callers See section for the user.

If the video file on video server is corrupted, re-record the video greeting. A video file is considered corrupted when the
                                    video greeting gets downgraded to audio during playback.

If the response time from DNS is slow, the playback of two subsequent video greetings is delayed.

### Unable to Play Video Greetings When Received Unanswered Call

In case of an unanswered call (“ring-no-answer”), if the called user is unable to play video greeting to the calling user,
                              check the following:

Whether the state of video server is active and running using the Test button on the Edit Video Service page.

Check whether the video service account is created for a user.

Check the connectivity of video service account (of a user) with video server.

Check whether the My Personal Recording option is enabled for video greetings in the Callers See section for the user.

Check whether the Outside Caller option is enabled in the Edit Class of Service page for the called user if the calling user
                                    is an unidentified caller.

### Video Call
                           	 Downgrades to Audio while Recording/Playing Video Message

If the video call
                              		downgrades to audio with the“video services are not available, using audio for
                              		the duration of call” prompt while playing or recording the video message,
                              		check the following:

Whether the
                                    			 state of video server is active and running using the Test button on the Edit Video
                                       				Service page.

Check the error
                                    			 codes sent by the video server.

### Video Playback
                           	 Hangs in Between

If the video
                              		recording hangs while playback, do the following:

Press # button
                                    			 on TUI to end the playback and continue with the call.

Check the
                                    			 conversation logs to diagnose the issue.

### Troubleshooting
                           	 Video Quality of Video Greetings and Messages

If the video quality is poor during the playback of video
                              		greeting or video message, check the following:

Check and reduce the KeyFrame Requests interval mentioned in the Interval in Seconds for sending KeyFrame Requests to End Point
                                       				during recording option. To do this, login to Cisco Unity Connection
                                    			 Administration, navigate to Advanced > Telephony and select Interval in Seconds for sending KeyFrame Requests to End Point
                                       				during recording .

Check and update the value of the session bit rate for video
                                    			 calls in the Maximum Session Bit Rate for Video Calls in Cisco Unified
                                       				Communications Manager option depending on the video resolution settings
                                    			 the administrator have selected in Cisco Unity Connection Administration. To
                                    			 check and update the session bit rate, login to Cisco Unified Communications
                                    			 Manager, navigate to System > Region Information > Region , and update the value of Maximum Session Bit Rate for Video Calls field. To configure
                                    			 video resolution, login to Unity Connection Administration, navigate to Port Group > Port Group Basics > Change Advertising and update the value in the Video Resolution field.

### Error Codes Send by Cisco MediaSense

Unity Connection integrates with Cisco MediaSense video server. You may receive the following error codes at RTMT tool from
                                 Cisco MediaSense.

Error Codes Received by Cisco MediaSense

Error Code

Description

Applicable to

E_MIU_MS_CONNECTOR_FALIURE

If there is no response or error in HTTP response from Cisco MediaSense.

At the time:

Establishing a video call

Recording a video greeting

Playback of video greeting.

E_MIU_MS_AUTHENTICATION_FAILURE

Username or password is incorrect

At the time of establishing a video call using telephone user interface.

E_MIU_MS_REDIRECT_FAIL

If the redirect IP address or hostname is missing in the response, Cisco MediaSense sends response 3000.

At the time of establishing a video call using telephone user interface.

E_MIU_MS_SESSION_ID_NOT_FOUND

If the requested session ID is not available at Cisco Media Sense.

During playback of video greetings

E_MIU_MS_INTERNAL_FAILURE

If the unknown server error is occurred, Cisco MediaSense sends response 5000.

At the time of establishing a video call

E_MIU_MS_ERROR_UNKNOWN

If any request to Cisco MediaSense fails.

At the time of establishing a video call

E_MIU_MS_RESPONSE_CODE_UNKNOWN

If there is no response code or the response code field is completely missing in the response from Cisco MediaSense.

At the time of establishing a video call

For troubleshooting the scenarios received at the time of establishing a video call, see the “Unable to Establish Video Call through Telephone User Interface (TUI)” section on page 13-2 .

For more information on the error codes received from Cisco MediaSense, see the Cisco MediaSense Developer Guide.

| Note | If the DNS server is not available, make sure that you enter only the IP address in the Video Server Field and the Allow Self
                                                Signed Certificate for Video Servers check box is checked. |
|---|---|

| Note | If the DNS server is not available, make sure that you enter only the IP address in the Video Server field and the Allow Self
                                                Signed Certificate for Video Server check box is checked. |
|---|---|

| Error Code | Description | Applicable to |
|---|---|---|
| E_MIU_MS_CONNECTOR_FALIURE | If there is no response or error in HTTP response from Cisco MediaSense. | At the time: Establishing a video call Recording a video greeting Playback of video greeting. |
| E_MIU_MS_AUTHENTICATION_FAILURE | Username or password is incorrect | At the time of establishing a video call using telephone user interface. |
| E_MIU_MS_REDIRECT_FAIL | If the redirect IP address or hostname is missing in the response, Cisco MediaSense sends response 3000. | At the time of establishing a video call using telephone user interface. |
| E_MIU_MS_SESSION_ID_NOT_FOUND | If the requested session ID is not available at Cisco Media Sense. | During playback of video greetings |
| E_MIU_MS_INTERNAL_FAILURE | If the unknown server error is occurred, Cisco MediaSense sends response 5000. | At the time of establishing a video call |
| E_MIU_MS_ERROR_UNKNOWN | If any request to Cisco MediaSense fails. | At the time of establishing a video call |
| E_MIU_MS_RESPONSE_CODE_UNKNOWN | If there is no response code or the response code field is completely missing in the response from Cisco MediaSense. | At the time of establishing a video call |