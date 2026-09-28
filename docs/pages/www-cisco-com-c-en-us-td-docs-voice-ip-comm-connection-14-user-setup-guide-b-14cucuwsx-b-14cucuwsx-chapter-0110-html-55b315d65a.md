---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-user-setup-guide-b-14cucuwsx-b-14cucuwsx-chapter-0110-html-55b315d65a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/user_setup/guide/b_14cucuwsx/b_14cucuwsx_chapter_0110.html
retrieved_at: 2026-08-17T03:38:45.032654+00:00
---

User Workstation Setup Guide for Cisco Unity Connection Release 14

# User Workstation Setup Guide for Cisco Unity Connection Release 14

Updated: March 31, 2021

Chapter: Setting Up
	 Playback and Recording Devices

## Chapter: Setting Up
	 Playback and Recording Devices

# Setting Up
                     	 Playback and Recording Devices

## Setting Up
                        	 Playback and Recording Devices

### Setting Up
                           	 Playback and Recording Devices for the Media Player

In Unity Connection, Media Player provides the functionality of play, record, upload and download a voice name of a user and
                              greetings using phone .

Media Player supports computer along with phone for recording and playback device. You can select any of the device using
                              Toggle button on the Media Player. By default, computer option is enabled as playback and recording device.

To set the phone as
                              		a recording and playback device, see the section Using
                                 		  Phone as a Recording and Playback Device.

To set the computer as a recording and playback device, see the section Using
                                 		  Computer as a Recording and Playback Device

For more information on the Media Player, see "Media Player in the Messaging Assistant Web Tool" chapter of the User Guide for the Cisco Unity Connection Messaging Assistant Web Tool available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/user/guide/assistant/b_14cucugasst.html .

### Using Phone as a Recording and Playback Device

When users use the phone as a recording and playback device in the web tools that are accessed through the Cisco PCA (and
                              in Cisco Unity Connection Administration), the following events occur:

The user selects the applicable option in the client application to make or play a recording.

The client application asks Unity Connection to place a call to the user extension or URI, and Unity Connection calls the
                                    extension or URI.

When making a recording, the user answers the phone, and begins recording the message, name, or greeting. When the user hangs
                                    up, the client application tells Unity Connection that the recording is finished.

When playing a recording, the user answers the phone, and the client application asks Unity Connection to play the message.
                                    Unity Connection streams the recording by phone.

### Using Computer Microphone and Speakers as the Recording and Playback Devices

When users use a computer microphone and speakers as the recording and playback devices, the following events occur:

The user selects the applicable option in the client application to make or play a recording.

When making a recording, the user begins speaking into the microphone. When the user selects the applicable option in the
                                    client application to stop recording, the client application tells Cisco Unity Connection that the recording is finished.

When playing a recording, Unity Connection streams the message to the client application. Streaming occurs on demand, regardless
                                    of network traffic. The client application begins to play the message through the speakers as soon as a few seconds of the
                                    message are buffered in memory on the user workstation.