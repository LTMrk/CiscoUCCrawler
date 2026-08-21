---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-12-6-2-sayitsmart-guide-cc-77bb90b04a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/12-6-2/sayitsmart/guide/ccvp_b_1262-say-it-smart-specifications-for-cisco-unified-customer-voice-portal/ccvp_b_1251-say-it-smart-specifications-for-cisco-unified-customer-voice-portal_chapter_0110.html
retrieved_at: 2026-08-21T17:39:48.103880+00:00
---

Say It Smart Specifications for Cisco Unified Customer Voice Portal, Release 12.6(2)

# Say It Smart Specifications for Cisco Unified Customer Voice Portal, Release 12.6(2)

Updated: April 28, 2023

Chapter: Filename

## Chapter: Filename

# Filename

Plugin
                                    Name:

file

Display Name:

Filename

Class
                                    Name:

com.audium.sayitsmart.plug-ins.AudiumSayItSmart

## Description

This Say It Smart type
                           		handles the playback of an audio file whose name is passed as input to the
                           		plug-in. In Call Studio, one can specify a file type to apply to all audio
                           		files listed by the Say It Smart type. Filename is no different, the file type
                           		extension specified in Call Studio will be appended to the filename passed to
                           		the plug-in. If the data sent as input already has an extension, Call Studio
                           		file type should be blank. For a TTS backup, the plug-in returns the name of
                           		the audio file since the transcript cannot be known in advance. When trying to
                           		use this type in TTS only mode, it returns a null .

## Input Formats

Name

(Display Name)

Description

string

(A Filename)

Any string (the plug-in does no filename
                                          validation).

## Output Formats

Name

(Display Name)

Input Format
                                             Depends On

Description

audio

(Audio File)

string

A
                                          single audio file whose name is passed to the plug-in.

## Filesets

Name

(Display
                                             Name)

Output Format
                                             Depends On

Description

none

(No Fileset)

audio

The fileset contains only one file: the one to play.

## Audio Files

The only audio file needed is the audio file to play, which is determined
                           dynamically.

## Examples

Example #1

Data:

my file

Input
                                          						Format:

string

Output
                                          						Format:

audio

Fileset

none

Playback:

[Assuming
                                          						an extension of "ulaw" was given in Call Studio] "my
                                             						  file.ulaw"

Example #2

Data:

audio_logo.wav

Input Format:

string

Output Format:

audio

Fileset

none

Playback:

[Assuming an extension of ”wav” was given in Call Studio]
                                          						“audio_logo.wav.wav”

| Plugin
                                    Name: | file |
|---|---|
| Display Name: | Filename |
| Class
                                    Name: | com.audium.sayitsmart.plug-ins.AudiumSayItSmart |

| Note | Important. In Call Studio
                                    		and VXML Server substitution can be used within audio file names and TTS
                                    		content, so one can do with substitution what this plug-in does. Additionally,
                                    		a new Say It Smart plug-in type was introduced: Custom Content, that does what
                                    		this plug-in does and more (such as allowing for a TTS backup). As a result,
                                    		this plug-in should be considered deprecated . It
                                    		is still included for backwards compatibility however eventually this plug-in
                                    		will no longer be included in Unified CVP updates, so use one of the above
                                    		solutions instead of using this plug-in. |
|---|---|

| Name (Display Name) | Description |
|---|---|
| string (A Filename) | Any string (the plug-in does no filename
                                          validation). |

| Name (Display Name) | Input Format
                                             Depends On | Description |
|---|---|---|
| audio (Audio File) | string | A
                                          single audio file whose name is passed to the plug-in. |

| Name (Display
                                             Name) | Output Format
                                             Depends On | Description |
|---|---|---|
| none (No Fileset) | audio | The fileset contains only one file: the one to play. |

| Data: | my file |
|---|---|
| Input
                                          						Format: | string |
| Output
                                          						Format: | audio |
| Fileset | none |
| Playback: | [Assuming
                                          						an extension of "ulaw" was given in Call Studio] "my
                                             						  file.ulaw" |

| Data: | audio_logo.wav |
|---|---|
| Input Format: | string |
| Output Format: | audio |
| Fileset | none |
| Playback: | [Assuming an extension of ”wav” was given in Call Studio]
                                          						“audio_logo.wav.wav” |