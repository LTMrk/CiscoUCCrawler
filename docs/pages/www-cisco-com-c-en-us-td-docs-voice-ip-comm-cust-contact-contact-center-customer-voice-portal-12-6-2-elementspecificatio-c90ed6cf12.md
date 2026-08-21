---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-12-6-2-elementspecificatio-c90ed6cf12
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/12-6-2/elementspecification/guide/ccvp_b_1262-element-specifications-guide/ccvp_m_1251-generic-custom-voicexml-properties.html
retrieved_at: 2026-08-21T17:14:54.140113+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(2)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(2)

Updated: April 28, 2023

Chapter: Generic Custom VoiceXML Properties

## Chapter: Generic Custom VoiceXML Properties

- Generic Custom VoiceXML Properties

- Custom VoiceXML Properties

# Generic Custom VoiceXML Properties

You cannot configure the fetchaudio VoiceXML Property in the Root Doc Settings .

## Custom VoiceXML Properties

The following table lists the generic custom VoiceXML properties.

Property

Type

Description

com.cisco.tts-server

String

Allows the document to specify an external media server for text-to-speech operations. The media server is specified in the
                                       form of a URI, and is used in all consecutive ASR operations until the next media server is specified.

It can be defined for:

An entire application or document at the <vxml> level,

A specific dialog at the form or menu level, or

A specific form item.

The media server’s URI can be formatted for Media Resource Control Protocol version 1 (MRCPv1) which uses Real Time Streaming
                                       Protocol (RTSP). For example:

<property name=“com.cisco.tts-server” value=“rtsp://tts-server/synthesizer”/>

The media server’s URI can be formatted for Media Resource Control Protocol version 2 (MRCPv2) which uses Session Initiation
                                       Protocol (SIP). For example:

<property name=“com.cisco.tts-server” value=“sip:mresources@mediaserver.com"/>

There are two ways to specify an external media server for TTS and ASR operations:

Servers configured through administrator page or REST APIs—Media server sessions are created for each call to IVR applications,
                                             regardless of whether an application needs to talk to the media server.

com.cisco.tt-server and com.cisco.asr-server <property> extensions—Media server sessions are created for each call to that
                                             application. If only a small number of applications require TTS/ASR media sessions, you should use the <property> extensions
                                             within those applications to define the external media server URL in the VoiceXML script.

com.cisco.asr-server

String

Allows a document to specify an external media server for automatic speech recognition operations. The media server is specified
                                       in the form of a URI, and is used in all consecutive ASR operations. By default, the media server is selected in round-robin
                                       approach. If you specify a particular media server, then only that specified server is used by overriding the default behavior.

The media server’s URI can be formatted for Media Resource Control Protocol version 1 (MRCPv1) which uses RTSP. For example:

<property name=“com.cisco.asr-server” value=“rtsp://asr-server/recognizer” />

The media server’s URI can be formatted for Media Resource Control Protocol version 2 (MRCPv2) which uses Session Initiation
                                       Protocol (SIP). For example:

<property name=“com.cisco.asr-server” value=“sip:mresources@mediaserver.com"/>

com.cisco.sessionxml.location

String

Allows a document to specify the session xml file location which is used in the SPEAK/RECOGNIZE of MRCPv2 messages.

<property name=“com.cisco.sessionxml.location” value=“/CVP/audio/samplesessionXML.xml” />

This file is a valid optional XML file which contains information required by third-party speech servers. Cisco VVB creates
                                       the MIME body using the content of this file and sends it to third-party servers in MRCPv2 dialog-creating request.

For more information on content of this file, refer to third-party documentation.

com.cisco.secureLogging

Boolean

Allows the user to enable or disable the secure logging functionality to protect sensitive information printed in the logs.
                                       This is applicable for user-input-based VXML elements.

The value can be true or false to enable or disable the user input logging. For example:

<property name="com.cisco.secureLogging" value="true" />

As the property is applicable at field level, the user should be able to enable or disable secure logging in each field in
                                       a single VXML application.

com.cisco.tts.gender

String

Allows the user to personalize their experience by choosing the gender of the voice for text-to-speech (TTS) output within
                                       the framework of Media Resource Control Protocol (MRCP) for TTS systems.

The value can be male or female to define the gender of the voice for text-to-speech (TTS) output. For example:

<property name="com.cisco.tts.gender" value="female" />

When you set the value of the property to "male" or "female" , the TTS system will use a male or female voice, respectively, for synthesizing speech. This can be particularly useful for
                                       applications where the gender of the voice can enhance user interaction.

com.cisco.tts.locale

String

To achieve localization in TTS systems using the Media Resource Control Protocol (MRCP) framework, you can specify properties
                                       that define the language, regional accent, and gender of the selected voice. For example:

```
<property name="com.cisco.tts.gender" value="female"/>

<property name="com.cisco.tts.locale" value="en_US"/>
```

When you set the value of the property to "en-US" , the TTS system will use the language and regional accent corresponding to the specified locale.

Synthesize.cache

Boolean

Whether to cache the prompt for current voice element.

VVB caches the synthesized prompts for faster performance. Set the value of this parameter to false to disable the caching for dynamic prompts.

Synthesize.voiceName

String

Set the voice name for Synthesize operation.

Helps to select the voice and the accent in which the prompts have to be played

Synthesize.voiceGender

String

Set the gender type for Synthesize operation. For example:

<property name="Synthesize.voiceGender" value="male"/>

The Synthesize.voiceGender property is applicable only for cloud based (GRPC) synthesizer and is not supported with MRCP.

com.cisco.protoHeadersRestricted

String

Filters out the specific restricted SIP header to be passed to the VXML Server.

The default value is an empty string (null).

Provide the value as comma separated list for the restricted headers.

maxspeechtimeout

String

Allows the user to set the MRCP Recognition-Timeout property.

Unit: seconds.

Example: 10s, 15s

The default value for the property is 20s.

com.cisco.localTranscribe

Boolean

This VXML property is introduced to give preference to MRPC Server. If the property is set to true, then MRPC Server is used.
                                       By default, Google Transcribe is used.

fetchaudio

String

This VXML property plays audio to the caller while the system is retrieving a document or waiting for the backend process
                                       to complete. This prevents silence during potentially lengthy fetch operations and enhances the caller's experience.

You can configure the VXML property as follows:

fetchaudio : URI of the audio file (usually a .wav file).

| Note | You cannot configure the fetchaudio VoiceXML Property in the Root Doc Settings . |
|---|---|

| Property | Type | Description |
|---|---|---|
| com.cisco.tts-server | String | Allows the document to specify an external media server for text-to-speech operations. The media server is specified in the
                                       form of a URI, and is used in all consecutive ASR operations until the next media server is specified. It can be defined for: An entire application or document at the <vxml> level, A specific dialog at the form or menu level, or A specific form item. The media server’s URI can be formatted for Media Resource Control Protocol version 1 (MRCPv1) which uses Real Time Streaming
                                       Protocol (RTSP). For example: <property name=“com.cisco.tts-server” value=“rtsp://tts-server/synthesizer”/> The media server’s URI can be formatted for Media Resource Control Protocol version 2 (MRCPv2) which uses Session Initiation
                                       Protocol (SIP). For example: <property name=“com.cisco.tts-server” value=“sip:mresources@mediaserver.com"/> There are two ways to specify an external media server for TTS and ASR operations: Servers configured through administrator page or REST APIs—Media server sessions are created for each call to IVR applications,
                                             regardless of whether an application needs to talk to the media server. com.cisco.tt-server and com.cisco.asr-server <property> extensions—Media server sessions are created for each call to that
                                             application. If only a small number of applications require TTS/ASR media sessions, you should use the <property> extensions
                                             within those applications to define the external media server URL in the VoiceXML script. |
| com.cisco.asr-server | String | Allows a document to specify an external media server for automatic speech recognition operations. The media server is specified
                                       in the form of a URI, and is used in all consecutive ASR operations. By default, the media server is selected in round-robin
                                       approach. If you specify a particular media server, then only that specified server is used by overriding the default behavior. The media server’s URI can be formatted for Media Resource Control Protocol version 1 (MRCPv1) which uses RTSP. For example: <property name=“com.cisco.asr-server” value=“rtsp://asr-server/recognizer” /> The media server’s URI can be formatted for Media Resource Control Protocol version 2 (MRCPv2) which uses Session Initiation
                                       Protocol (SIP). For example: <property name=“com.cisco.asr-server” value=“sip:mresources@mediaserver.com"/> |
| com.cisco.sessionxml.location | String | Allows a document to specify the session xml file location which is used in the SPEAK/RECOGNIZE of MRCPv2 messages. <property name=“com.cisco.sessionxml.location” value=“/CVP/audio/samplesessionXML.xml” /> This file is a valid optional XML file which contains information required by third-party speech servers. Cisco VVB creates
                                       the MIME body using the content of this file and sends it to third-party servers in MRCPv2 dialog-creating request. Note For more information on content of this file, refer to third-party documentation. | Note | For more information on content of this file, refer to third-party documentation. |
| Note | For more information on content of this file, refer to third-party documentation. |
| com.cisco.secureLogging | Boolean | Allows the user to enable or disable the secure logging functionality to protect sensitive information printed in the logs.
                                       This is applicable for user-input-based VXML elements. The value can be true or false to enable or disable the user input logging. For example: <property name="com.cisco.secureLogging" value="true" /> As the property is applicable at field level, the user should be able to enable or disable secure logging in each field in
                                       a single VXML application. |
| com.cisco.tts.gender | String | Allows the user to personalize their experience by choosing the gender of the voice for text-to-speech (TTS) output within
                                       the framework of Media Resource Control Protocol (MRCP) for TTS systems. The value can be male or female to define the gender of the voice for text-to-speech (TTS) output. For example: <property name="com.cisco.tts.gender" value="female" /> When you set the value of the property to "male" or "female" , the TTS system will use a male or female voice, respectively, for synthesizing speech. This can be particularly useful for
                                       applications where the gender of the voice can enhance user interaction. |
| com.cisco.tts.locale | String | To achieve localization in TTS systems using the Media Resource Control Protocol (MRCP) framework, you can specify properties
                                       that define the language, regional accent, and gender of the selected voice. For example: <property name="com.cisco.tts.gender" value="female"/>

<property name="com.cisco.tts.locale" value="en_US"/> When you set the value of the property to "en-US" , the TTS system will use the language and regional accent corresponding to the specified locale. |
| Synthesize.cache | Boolean | Whether to cache the prompt for current voice element. VVB caches the synthesized prompts for faster performance. Set the value of this parameter to false to disable the caching for dynamic prompts. |
| Synthesize.voiceName | String | Set the voice name for Synthesize operation. Helps to select the voice and the accent in which the prompts have to be played |
| Synthesize.voiceGender | String | Set the gender type for Synthesize operation. For example: <property name="Synthesize.voiceGender" value="male"/> Note The Synthesize.voiceGender property is applicable only for cloud based (GRPC) synthesizer and is not supported with MRCP. | Note | The Synthesize.voiceGender property is applicable only for cloud based (GRPC) synthesizer and is not supported with MRCP. |
| Note | The Synthesize.voiceGender property is applicable only for cloud based (GRPC) synthesizer and is not supported with MRCP. |
| com.cisco.protoHeadersRestricted | String | Filters out the specific restricted SIP header to be passed to the VXML Server. The default value is an empty string (null). Provide the value as comma separated list for the restricted headers. |
| maxspeechtimeout | String | Allows the user to set the MRCP Recognition-Timeout property. Unit: seconds. Example: 10s, 15s The default value for the property is 20s. |
| com.cisco.localTranscribe | Boolean | This VXML property is introduced to give preference to MRPC Server. If the property is set to true, then MRPC Server is used.
                                       By default, Google Transcribe is used. |
| fetchaudio | String | This VXML property plays audio to the caller while the system is retrieving a document or waiting for the backend process
                                       to complete. This prevents silence during potentially lengthy fetch operations and enhances the caller's experience. You can configure the VXML property as follows: fetchaudio : URI of the audio file (usually a .wav file). |

| Note | For more information on content of this file, refer to third-party documentation. |
|---|---|

| Note | The Synthesize.voiceGender property is applicable only for cloud based (GRPC) synthesizer and is not supported with MRCP. |
|---|---|