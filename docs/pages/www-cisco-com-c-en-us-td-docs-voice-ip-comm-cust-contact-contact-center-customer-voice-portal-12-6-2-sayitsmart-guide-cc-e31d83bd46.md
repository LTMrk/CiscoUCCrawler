---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-12-6-2-sayitsmart-guide-cc-e31d83bd46
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/12-6-2/sayitsmart/guide/ccvp_b_1262-say-it-smart-specifications-for-cisco-unified-customer-voice-portal/ccvp_b_1251-say-it-smart-specifications-for-cisco-unified-customer-voice-portal_chapter_011.html
retrieved_at: 2026-08-21T17:39:35.097653+00:00
---

Say It Smart Specifications for Cisco Unified Customer Voice Portal, Release 12.6(2)

# Say It Smart Specifications for Cisco Unified Customer Voice Portal, Release 12.6(2)

Updated: April 28, 2023

Chapter: Custom Content

## Chapter: Custom Content

# Custom Content

Plugin Name:

literal

Display
                                    Name:

Custom
                                    Content

Class
                                    Name:

com.audium.sayitsmart.plug-ins.AudiumSayItSmartLiteral

## Description

This Say It Smart type was introduced to provide several helpful
                           and time saving features to the application designer and
                           developer:

Provide a way to allow a list of audio
                                 files (with TTS transcripts) of variable length to be played one after the
                                 other in one audio item.

Provide a more direct link to
                                 internal Java classes that may contain dynamic audio content as an alternative
                                 to creating dynamic voice element configurations.

Provide
                                 at least the same functionality as the now "deprecated" File and String Unified
                                 CVP Say It Smart types.

## Input
                        	 Formats

Name

(Display Name)

Description

simple

(String (No Delimiters))

A text string that can represent a single filename or a
                                          						single TTS string.

complex

(FILE:::TTS|||… |||FILE:TTS)

A text string that follows a specific format with delimiters
                                          						in order to represent any number of audio files and TTS transcripts. An audio
                                          						file is separated from its TTS transcript by three colons. Each audio file/TTS
                                          						combination is separated from others by three pipes. Note that each component
                                          						of the combination can be blank if no audio file or TTS content is necessary.
                                          						The audio will be played in the order in which it appears in the string from
                                          						left to right.

resultset

(ResultSetList Object)

A Java ResultSetList object that has been created
                                          						by the Unified CVP Database element as a result of a database query that is
                                          						expected to contain audio information. The result must return two columns, the
                                          						first being the audio file (or null if no audio file is needed) and the
                                          						second column being the TTS transcript for the audio file (or null if there is no TTS transcript). There
                                          						can be any number of strows. The audio will be played in the order in which it
                                          						appears in the result set.

siscontent

(SayItSmartContent Object)

Each Say It Smart plug-in’s Java code creates a SayItSmartContent object to represent audio
                                          						content that is then passed to Unified CVP VXML Server to render into VoiceXML.
                                          						This input format accepts a developer-created object of this type and the
                                          						plug-in will pass this to VXML Server without making any modifications. This
                                          						object can contain any number of audio files, TTS transcripts, and pauses the
                                          						developer desires.

array (String[] Object)

A String array that can contain either a list
                                          						of audio filenames or TTS transcripts (it cannot contain a mixture of audio
                                          						filenames and TTS transcripts). The audio will be played in the order it
                                          						appears in the array.

## Output
                        	 Formats

Name

(Display Name)

Input Format Depends On

Description

standard

(Filename w/ TTS Backup)

complex resultset siscontent

This output format will produce output containing both audio
                                          						files (if defined) and TTS transcripts (if defined), assuming that the TTS
                                          						content may contain Speech Synthesis Markup Language (SSML). This adds some
                                          						additional overhead so use the standard_no_ssml output format if it is
                                          						known that the TTS transcripts do not contain SSML.

standard_no_ssml

(Filename w/ TTS Backup (no SSML))

complex resultset siscontent

This output format will produce output containing both audio
                                          						files (if defined) and TTS transcripts (if defined), assuming that the TTS
                                          						content does not contain SSML. Assuming no SSML makes the process more
                                          						efficient than keeping open the possibility that the TTS content may have SSML
                                          						(as in the standard fileset).

tts

(TTS Only)

simple complex resultset siscontent array

This output format will produce output containing only the
                                          						TTS content of the data, even if it contains audio file content. For the simple
                                          						and array input formats, this output format indicates that the data contains
                                          						only TTS content. This output format assumes the TTS content may contains SSML.
                                          						This adds some additional overhead so use the tts_no_ssml output format if it is known
                                          						that the TTS content does not contain SSML.

tts_no_ssml

(TTS Only (no SSML))

simple complex resultset siscontent array

This output format will produce output containing only the
                                          						TTS content of the data, even if it contains audio file content. For the simple and array input formats, this output format
                                          						indicates that the data contains only TTS content. Assuming no SSML makes the
                                          						process more efficient than keeping open the possibility that the TTS content
                                          						may have SSML (as in the tts fileset).

files

(Filename(s) Only)

simple complex resultset siscontent array

This output format will produce output containing only the
                                          						audio file content of the data, even if it contains TTS content. For the simple and array input formats, this output format
                                          						indicates that the data contains audio files only.

## Filesets

Name

(Display
                                             Name)

Output Format
                                             Depends On

Description

none

(No Fileset)

standard standard_no_ssml tts tts_no_ssml files

This plug-in allows the developer to
                                          specify any amount of audio files, the names of which are determined at
                                          runtime. As a result, there is no need for a fileset. Every Say It Smart
                                          plug-in, though, requires at least one fileset, so this one is simply named none .

## Audio Files

None. The audio files will be determined by the application designer and
                           developer.

## Examples

Example #1

Data:

myGreeting.wav

Input Format:

simple

Output Format:

files

Fileset

none

Playback:

myGreeting.wav (with no TTS backup)

Example #2

Data:

This is some text to speech

Input Format:

simple

Output Format:

tts_no_ssml

Fileset

none

Playback:

"This is some text to speech" (this is read as TTS)

Example #3

Data:

a.wav:::backup for a|||b.wav:::backup for b

Input Format:

complex

Output Format:

standard_no_ssml

Fileset

none

Playback:

a.wav (with TTS backup "backup for a" )

b.wav (with TTS backup "backup for b" )

There are no
                              		  examples of input formats that take Java objects as the data must be created by
                              		  a developer in custom Java code.

| Plugin Name: | literal |
|---|---|
| Display
                                    Name: | Custom
                                    Content |
| Class
                                    Name: | com.audium.sayitsmart.plug-ins.AudiumSayItSmartLiteral |

| Name (Display Name) | Description |
|---|---|
| simple (String (No Delimiters)) | A text string that can represent a single filename or a
                                          						single TTS string. |
| complex (FILE:::TTS\|\|\|… \|\|\|FILE:TTS) | A text string that follows a specific format with delimiters
                                          						in order to represent any number of audio files and TTS transcripts. An audio
                                          						file is separated from its TTS transcript by three colons. Each audio file/TTS
                                          						combination is separated from others by three pipes. Note that each component
                                          						of the combination can be blank if no audio file or TTS content is necessary.
                                          						The audio will be played in the order in which it appears in the string from
                                          						left to right. |
| resultset (ResultSetList Object) | A Java ResultSetList object that has been created
                                          						by the Unified CVP Database element as a result of a database query that is
                                          						expected to contain audio information. The result must return two columns, the
                                          						first being the audio file (or null if no audio file is needed) and the
                                          						second column being the TTS transcript for the audio file (or null if there is no TTS transcript). There
                                          						can be any number of strows. The audio will be played in the order in which it
                                          						appears in the result set. |
| siscontent (SayItSmartContent Object) | Each Say It Smart plug-in’s Java code creates a SayItSmartContent object to represent audio
                                          						content that is then passed to Unified CVP VXML Server to render into VoiceXML.
                                          						This input format accepts a developer-created object of this type and the
                                          						plug-in will pass this to VXML Server without making any modifications. This
                                          						object can contain any number of audio files, TTS transcripts, and pauses the
                                          						developer desires. |
| array (String[] Object) | A String array that can contain either a list
                                          						of audio filenames or TTS transcripts (it cannot contain a mixture of audio
                                          						filenames and TTS transcripts). The audio will be played in the order it
                                          						appears in the array. |

| Name (Display Name) | Input Format Depends On | Description |
|---|---|---|
| standard (Filename w/ TTS Backup) | complex resultset siscontent | This output format will produce output containing both audio
                                          						files (if defined) and TTS transcripts (if defined), assuming that the TTS
                                          						content may contain Speech Synthesis Markup Language (SSML). This adds some
                                          						additional overhead so use the standard_no_ssml output format if it is
                                          						known that the TTS transcripts do not contain SSML. |
| standard_no_ssml (Filename w/ TTS Backup (no SSML)) | complex resultset siscontent | This output format will produce output containing both audio
                                          						files (if defined) and TTS transcripts (if defined), assuming that the TTS
                                          						content does not contain SSML. Assuming no SSML makes the process more
                                          						efficient than keeping open the possibility that the TTS content may have SSML
                                          						(as in the standard fileset). |
| tts (TTS Only) | simple complex resultset siscontent array | This output format will produce output containing only the
                                          						TTS content of the data, even if it contains audio file content. For the simple
                                          						and array input formats, this output format indicates that the data contains
                                          						only TTS content. This output format assumes the TTS content may contains SSML.
                                          						This adds some additional overhead so use the tts_no_ssml output format if it is known
                                          						that the TTS content does not contain SSML. |
| tts_no_ssml (TTS Only (no SSML)) | simple complex resultset siscontent array | This output format will produce output containing only the
                                          						TTS content of the data, even if it contains audio file content. For the simple and array input formats, this output format
                                          						indicates that the data contains only TTS content. Assuming no SSML makes the
                                          						process more efficient than keeping open the possibility that the TTS content
                                          						may have SSML (as in the tts fileset). |
| files (Filename(s) Only) | simple complex resultset siscontent array | This output format will produce output containing only the
                                          						audio file content of the data, even if it contains TTS content. For the simple and array input formats, this output format
                                          						indicates that the data contains audio files only. |

| Name (Display
                                             Name) | Output Format
                                             Depends On | Description |
|---|---|---|
| none (No Fileset) | standard standard_no_ssml tts tts_no_ssml files | This plug-in allows the developer to
                                          specify any amount of audio files, the names of which are determined at
                                          runtime. As a result, there is no need for a fileset. Every Say It Smart
                                          plug-in, though, requires at least one fileset, so this one is simply named none . |

| Data: | myGreeting.wav |
|---|---|
| Input Format: | simple |
| Output Format: | files |
| Fileset | none |
| Playback: | myGreeting.wav (with no TTS backup) |

| Data: | This is some text to speech |
|---|---|
| Input Format: | simple |
| Output Format: | tts_no_ssml |
| Fileset | none |
| Playback: | "This is some text to speech" (this is read as TTS) |

| Data: | a.wav:::backup for a\|\|\|b.wav:::backup for b |
|---|---|---|---|---|
| Input Format: | complex |
| Output Format: | standard_no_ssml |
| Fileset | none |
| Playback: | a.wav (with TTS backup "backup for a" ) b.wav (with TTS backup "backup for b" ) |