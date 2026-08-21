---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-12-6-2-elementspecificatio-476aec858b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/12-6-2/elementspecification/guide/ccvp_b_1262-element-specifications-guide/ccvp_mp_acc11dc0_00_audio.html
retrieved_at: 2026-08-21T17:15:14.956032+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(2)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(2)

Updated: April 28, 2023

Chapter: Audio

## Chapter: Audio

# Audio

The Audio voice element simply outputs a VoiceXML page with the contents of a single audio group. The Audio element is used for greetings, error messages and any other time audio is to be played in a situation not associated with
                                    an input state.

## Audio Groups

### Audio Playback

Name (Label)

Max1

Req'd

Notes

initial_audio_group (Initial)

Yes

Yes

The audio group containing the audio to play.

## Custom VoiceXML Properties

Name (Label)

Type

Description

cisco-maxtime

string

Defines the time duration for playing a prompt irrespective of the prompt length. Example: 5s

http.streaming

boolean

Indicates whether media streaming is enabled. Set the value of this parameter to true to enable media streaming.

Streaming is supported only for static URLs using u-law and A-law audio codec.

Streaming supports a maximum of 150 simultaneous callers for a single conference or a maximum of five simultaneous conferences
                                                         each having a maximum of 30 simultaneous callers.

Each caller can hear live streaming for a maximum duration of 30 minutes.

DTMF recognition and buffering are not supported for streaming prompts.

Caller can barge-in the live stream using DTMF if barge-in is enabled.

com.cisco.voicebrowser.streaming.timeout

string

This property defines the maximum time a streaming connection will be active if there are active callers using it. This is
                                       an optional property.

Set the value of this parameter to true to enable streaming timeout.

The maximum streaming timeout duration is 1800 seconds.

http.streaming.useragent

string

This property identifies the user. This is an optional property.

com.cisco.tts-server

string

The property com.cisco.tts-server must be added within the Audio element in Call Studio, with the value assigned as cloudTTS . This configuration directs the Audio element to utilize the cloud-based text-to-speech (TTS) service for speech synthesis
                                       via direct connectivity.

To complete the setup, a valid Config ID provisioned in Control Hub under the Features must also be specified using the CCAI.configId VoiceXML Custom Property within the same the Audio element.

This configuration allows the CVP VoiceXML application to integrate directly with Google TTS service without using the CCAI
                                                   Universal Harness, thereby eliminating the need for on-premises TTS engines.

CCAI.configId

string

This identifies a valid Config ID provisioned in Control Hub under the Features.

## Folder and Class Information

Studio Element Folder Name

Class Name

Top Level

com.audium.server.voiceElement.audio.MAudio

## Events

Name (Label)

Notes

Event Handler

You can
                                          				  select either VXML Event or Java Exception as event handler type from the
                                          				  drop-down list.

| The Audio voice element simply outputs a VoiceXML page with the contents of a single audio group. The Audio element is used for greetings, error messages and any other time audio is to be played in a situation not associated with
                                    an input state. |
|---|

| Name (Label) | Max1 | Req'd | Notes |
|---|---|---|---|
| initial_audio_group (Initial) | Yes | Yes | The audio group containing the audio to play. |

| Name (Label) | Type | Description |
|---|---|---|
| cisco-maxtime | string | Defines the time duration for playing a prompt irrespective of the prompt length. Example: 5s |
| http.streaming | boolean | Indicates whether media streaming is enabled. Set the value of this parameter to true to enable media streaming. Note Streaming is supported only for static URLs using u-law and A-law audio codec. Streaming supports a maximum of 150 simultaneous callers for a single conference or a maximum of five simultaneous conferences
                                                         each having a maximum of 30 simultaneous callers. Each caller can hear live streaming for a maximum duration of 30 minutes. DTMF recognition and buffering are not supported for streaming prompts. Caller can barge-in the live stream using DTMF if barge-in is enabled. | Note | Streaming is supported only for static URLs using u-law and A-law audio codec. Streaming supports a maximum of 150 simultaneous callers for a single conference or a maximum of five simultaneous conferences
                                                         each having a maximum of 30 simultaneous callers. Each caller can hear live streaming for a maximum duration of 30 minutes. DTMF recognition and buffering are not supported for streaming prompts. Caller can barge-in the live stream using DTMF if barge-in is enabled. |
| Note | Streaming is supported only for static URLs using u-law and A-law audio codec. Streaming supports a maximum of 150 simultaneous callers for a single conference or a maximum of five simultaneous conferences
                                                         each having a maximum of 30 simultaneous callers. Each caller can hear live streaming for a maximum duration of 30 minutes. DTMF recognition and buffering are not supported for streaming prompts. Caller can barge-in the live stream using DTMF if barge-in is enabled. |
| com.cisco.voicebrowser.streaming.timeout | string | This property defines the maximum time a streaming connection will be active if there are active callers using it. This is
                                       an optional property. Set the value of this parameter to true to enable streaming timeout. The maximum streaming timeout duration is 1800 seconds. |
| http.streaming.useragent | string | This property identifies the user. This is an optional property. |
| com.cisco.tts-server | string | The property com.cisco.tts-server must be added within the Audio element in Call Studio, with the value assigned as cloudTTS . This configuration directs the Audio element to utilize the cloud-based text-to-speech (TTS) service for speech synthesis
                                       via direct connectivity. To complete the setup, a valid Config ID provisioned in Control Hub under the Features must also be specified using the CCAI.configId VoiceXML Custom Property within the same the Audio element. Note This configuration allows the CVP VoiceXML application to integrate directly with Google TTS service without using the CCAI
                                                   Universal Harness, thereby eliminating the need for on-premises TTS engines. | Note | This configuration allows the CVP VoiceXML application to integrate directly with Google TTS service without using the CCAI
                                                   Universal Harness, thereby eliminating the need for on-premises TTS engines. |
| Note | This configuration allows the CVP VoiceXML application to integrate directly with Google TTS service without using the CCAI
                                                   Universal Harness, thereby eliminating the need for on-premises TTS engines. |
| CCAI.configId | string | This identifies a valid Config ID provisioned in Control Hub under the Features. |

| Note | Streaming is supported only for static URLs using u-law and A-law audio codec. Streaming supports a maximum of 150 simultaneous callers for a single conference or a maximum of five simultaneous conferences
                                                         each having a maximum of 30 simultaneous callers. Each caller can hear live streaming for a maximum duration of 30 minutes. DTMF recognition and buffering are not supported for streaming prompts. Caller can barge-in the live stream using DTMF if barge-in is enabled. |
|---|---|

| Note | This configuration allows the CVP VoiceXML application to integrate directly with Google TTS service without using the CCAI
                                                   Universal Harness, thereby eliminating the need for on-premises TTS engines. |
|---|---|

| Studio Element Folder Name | Class Name |
|---|---|
| Top Level | com.audium.server.voiceElement.audio.MAudio |

| Name (Label) | Notes |
|---|---|
| Event Handler | You can
                                          				  select either VXML Event or Java Exception as event handler type from the
                                          				  drop-down list. |