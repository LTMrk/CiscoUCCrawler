---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-5-user-guide-ccvp-b-cf517c84a4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_5/user/guide/ccvp_b_1251-say-it-smart-specifications-for-cisco-unified-customer-voice-portal/ccvp_b_1251-say-it-smart-specifications-for-cisco-unified-customer-voice-portal_chapter_01010.html
retrieved_at: 2026-08-21T03:09:04.671106+00:00
---

Say It Smart Specifications for Cisco Unified Customer Voice Portal, Release 12.5(1)

# Say It Smart Specifications for Cisco Unified Customer Voice Portal, Release 12.5(1)

Updated: February 2, 2020

Chapter: String

## Chapter: String

# String

Plugin
                                    Name:

string

Display Name:

TTS String

Class Name:

com.audium.sayitsmart.plug-ins.AudiumSayItSmartString

## Description

This Say It Smart type
                           		plays back the data sent as input in Text To Speech (TTS). Even when the Use Recorded
                              		  Audio checkbox is checked in Call Studio, the output will be a TTS string
                           		containing the passed data. The input data is unmodified unless it contains
                           		characters not allowed in XML and the TTS content is not contained within CDATA
                           		(this occurs only on some supported voice browsers). These characters will then
                           		be converted to their escaped equivalents (for example "<" is
                           		converted to "&lt;" ).

## Input Formats

Name

(Display Name)

Description

string

(A String)

Any string. The string is modified only when the
                                          string contains characters illegal to XML and the TTS content is not placed
                                          inside CDATA.

## Output Formats

Name

(Display Name)

Input Format
                                             Depends On

Description

tts

(The String in TTS)

string

The data will be read by the TTS
                                          engine.

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

There is no fileset because this type will never involve the playing of
                                          pre-recorded audio files. Every Say It Smart plug-in, though, requires at least
                                          one fileset, so this one is simply named "none" .

## Audio Files

None. The data will always be rendered in TTS.

## Examples

Example #1

Data:

Today’s bingo number is 28.

Input Format:

string

Output Format:

tts

Fileset

none

Playback:

Today’s bingo number is 28 (as TTS).

Example #2

Data:

myfile.wav

Input Format:

string

Output Format:

tts

Fileset

none

Playback:

myfile.wav (as
                                          				  TTS).

| Plugin
                                    Name: | string |
|---|---|
| Display Name: | TTS String |
| Class Name: | com.audium.sayitsmart.plug-ins.AudiumSayItSmartString |

| Note | Important. In Call Studio
                                    		and VXML Server substitution can be used within audio file names and TTS
                                    		content, so one can do with substitution what this plug-in does. Additionally,
                                    		a new Say It Smart plug-in type was introduced: Custom Content, that does what
                                    		this plug-in does and more. As a result, this plug-in should be considered "deprecated" . It
                                    		is still included for backwards compatibility however eventually this plug-in
                                    		will no longer be included in Unified CVP updates, so use one of the above
                                    		solutions instead of using this plug-in. |
|---|---|

| Name (Display Name) | Description |
|---|---|
| string (A String) | Any string. The string is modified only when the
                                          string contains characters illegal to XML and the TTS content is not placed
                                          inside CDATA. |

| Name (Display Name) | Input Format
                                             Depends On | Description |
|---|---|---|
| tts (The String in TTS) | string | The data will be read by the TTS
                                          engine. |

| Name (Display
                                             Name) | Output Format
                                             Depends On | Description |
|---|---|---|
| none (No Fileset) | audio | There is no fileset because this type will never involve the playing of
                                          pre-recorded audio files. Every Say It Smart plug-in, though, requires at least
                                          one fileset, so this one is simply named "none" . |

| Data: | Today’s bingo number is 28. |
|---|---|
| Input Format: | string |
| Output Format: | tts |
| Fileset | none |
| Playback: | Today’s bingo number is 28 (as TTS). |

| Data: | myfile.wav |
|---|---|
| Input Format: | string |
| Output Format: | tts |
| Fileset | none |
| Playback: | myfile.wav (as
                                          				  TTS). |