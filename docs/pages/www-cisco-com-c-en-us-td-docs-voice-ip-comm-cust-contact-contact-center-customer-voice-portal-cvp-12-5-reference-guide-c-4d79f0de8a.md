---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-5-reference-guide-c-4d79f0de8a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_5/reference/guide/ccvp_b_1251-element-specification-guide-cvp/ccvp_mp_r7854156_00_record_with_confirm.html
retrieved_at: 2026-08-21T17:33:54.362683+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.5(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.5(1)

Updated: January 31, 2020

Chapter: Record_With_Confirm

## Chapter: Record_With_Confirm

# Record_With_Confirm

The Record_With_Confirm voice element combines the
                                    functionality of the Record voice element with that of the MenuYesNo voice
                                    element. The voice element records the caller’s voice, then prompts the caller
                                    to confirm that the recording is acceptable. The caller can then accept or
                                    reject the confirmation or ask to have the message replayed. If the caller
                                    accepts the recording, the voice element saves the file just as the Record
                                    voice element does. This voice element contains all settings and audio groups
                                    from both the Record and MenuYesNo voice elements, however audio groups that
                                    are found in both voice elements (nomatch, noinput, and help) are now named
                                    differently for them to be
                                    distinguished.

## Settings

Name (Label)

Type

Req'd

Single Setting Value

Sub. Allowed

Default

Notes

inputmode

(Input Mode)

string enum

Yes

true

true

both

The type of
                                          				  entry allowed for input during confirmation. Possible values are: voice | dtmf | both .

noinput_timeout

(Noinput
                                          				  Timeout)

string

Yes

true

true

5s

The maximum time allowed for silence or no keypress before a noinput event is thrown. Possible values are standard time designations
                                          including both a non-negative number and a time unit, for example, 3s (for seconds) or 3000ms (for milliseconds). Default
                                          = 5s.

record_max_noinput_count

(Record Max
                                          				  NoInput Count)

int ≥ 0

Yes

true

true

3

The maximum
                                          				  number of noinput events allowed during input capture. 0 = infinite noinputs
                                          				  allowed.

confirm_max_noinput_count

(Confirm Max
                                          				  NoInput Count)

int ≥ 0

Yes

true

true

3

The maximum
                                          				  number of noinput events allowed during confirmation. 0 = infinite noinputs
                                          				  allowed.

confirm_max_nomatch_count

(Confirm Max
                                          				  NoMatch Count)

int ≥ 0

Yes

true

true

3

The maximum
                                          				  number of nomatch events allowed during confirmation. 0 = infinite nomatches
                                          				  allowed.

max_disconfirmed_count

(Max
                                          				  Disconfirmed Count)

int ≥ 0

Yes

true

true

3

The maximum
                                          				  number of times a caller is allowed to reject a recording. 0 = infinite
                                          				  disconfirmations allowed.

confirm_confidence_level

(Confirm
                                          				  Confidence Level)

decimal (0.0
                                          				  – 1.0)

Yes

true

true

0.50

The
                                          				  confidence level threshold to use for the confirmation.

start_with_beep

(Start With
                                          				  Beep)

boolean

Yes

true

true

true

Whether or
                                          				  not to play a beep before recording begins.

terminate_on_dtmf

(Terminate
                                          				  On DTMF)

boolean

Yes

true

true

true

Whether or
                                          				  not the caller can end the recording by pressing a touchtone key.

keep_recording_on_hangup

(Keep
                                          				  Recording On Hangup)

boolean

Yes

true

true

false

Whether or
                                          				  not the recording is stored if the caller hung up while making the recording or
                                          				  during the confirmation menu. Default = false.

max_record_time

(Max Record
                                          				  Time)

string

Yes

true

true

180s

The maximum
                                          				  time (in seconds) the recording is allowed to last. Possible values are
                                          				  standard time designations including a positive integer followed by s (for
                                          				  seconds), for example, 30s. Default = 180s.

final_silence

(Final
                                          				  Silence)

string

Yes

true

true

4s

For
                                                         						silence detection to work, you must enable Voice Activity Detection (VAD) in
                                                         						the gateway dial-peers. Manually remove NO VAD from the configuration script
                                                         						and replace it with VAD.

replay

(Replay)

boolean

Yes

true

true

false

Adds an
                                          				  option to replay the confirm initial audio groups.

filename

(Filename)

string

No

true

true

None

The filename
                                          				  of the recording (without extension). If left blank, an auto-generated filename
                                          				  will be used.

file_type

(File Type)

string enum

Yes

true

true

wav

This
                                          				  specifies the audio type of the file that will hold the recording. Possible
                                          				  values are: wav | vox | au | other .

mime_type

(Mime Type)

string

Yes

true

true

None

This
                                          				  specifies the MIME type of the file that will hold the recording, if file_type
                                          				  is set to other .

file_extension

(File
                                          				  Extension)

string

No

true

true

None

This
                                          				  specifies the file extension to use for the recorded file. A file extension
                                          				  different from the file type can be used. For example, with a mime type of vox , the file extension could be set to ulaw .

path

(Path)

string

No

true

true

None

The path to
                                          				  the file that will hold the recording. Either the path, ftp host, or both must
                                          				  be specified.

ftp_host

(FTP Host)

string

No

true

true

None

The domain
                                          				  name of the host to FTP the recording. Either the path, ftp host, or both must
                                          				  be specified.

Secure

(Secure)

boolean

Yes

true

true

false

Whether or
                                          				  not to enable Secure File Transfer protocol (SFTP). Default = false, indicates
                                          				  file transfer happens over FTP by default.

ftp_user

(FTP User)

string

Yes

true

true

None

The user
                                          				  name to use while FTPing the recording, if ftp_host is set.

ftp_password

(FTP
                                          				  Password)

string

Yes

true

true

None

The password
                                          				  to use while FTPing the recording, if ftp_host is set.

ftp_path

(FTP Path)

string

No

true

true

None

The
                                          				  directory in which to FTP the recording, if ftp_host is set.

ftp_in_background

(FTP In
                                          				  Background)

boolean

Yes

true

true

true

Whether or
                                          				  not the FTP is to be performed in the background, if ftp_host is set.

- The path setting does not
                                             					 require a trailing slash. The voice element will determine the appropriate
                                             					 destination. The path may be specified in operating system specific format (for
                                             					 example, on Windows it might be specified as C:\directory\subdirectory\ and on UNIX it might be /usr/local/directory/ ).

- For a recording to be
                                             					 stored, you can choose either to store it locally or remotely. For locally on
                                             					 the VXML server itself, configure only the filename ( myfile ) and the
                                             					 path ( c:/recordings/ ). For remotely on a ftp server,
                                             					 configure the filename ( myfile ) and the FTP details such as: host, user, path,
                                             					 and password. Once your record element is configured, determine the url to
                                             					 access the recording from an external system. Run a simple test by playing the
                                             					 recording from your web browser. Make use of the url:
                                             					 http://<ftpserver>/<ftppath>/filename . Find the correct path to
                                             					 play the audio file and use the same url in the audio element settings.

- If terminate_on_DTMF is false or off, recording will stop only after the voice browser reaches the input timeout.

- Some voice browsers may not
                                             					 accept all options provided for the file_type and mime_type settings. Check your voice browser
                                             					 documentation for information on supported audio types.

- It is important to ensure
                                             					 that VXML Server has permission to save audio files to the specified path.

## Element Data

Name

Type

Notes

filename

string

This stores the filename of the recording (without
                                          the path).

filepath

string

This stores the path to the file holding the
                                          recording (including the filename).

confirm_confidence

float

This is the confidence value of the utterance for the confirmation
                                          menu.

hungUpWhileRecording

boolean

This stores a true if the caller hung up while making the recording or
                                          the confirmation menu, false if
                                          not.

## Exit States

Name

Notes

max_nomatch

The maximum number of nomatch events has occurred. If the nomatch max
                                          count is 0, this exit state will never occur.

max_noinput

The maximum number of noinput events has occurred. If the noinput max
                                          count is 0, this exit state will never occur.

max_disconfirmed

The maximum number of disconfirmations has
                                          occurred. If the max disconfirmed count is set to 0, this exit state will never
                                          occur.

done

The recorded message was
                                          confirmed.

## Audio Groups

### Record Capture

Name (Label)

Req'd

Max1

Notes

record_initial_audio_group

(Record Initial)

Yes

Yes

Played when the voice
                                             element first begins.

record_noinput_audio_group

(Record NoInput)

No

No

Played when a noinput event
                                             occurs during recording.

### Record Confirm

Name
                                                (Label)

Req'd

Max1

Notes

before_confirm_audio_group

(Before Confirm)

No

Yes

Played before the
                                             recording is played back. The recording will be played back after this audio
                                             group is done playing.

after_confirm_audio_group

(After Confirm)

No

Yes

Played after the recording
                                             is played back. At least one of the two confirm prompts must be
                                             specified.

confirm_nomatch_audio_group

(Confirm NoMatch)

No

No

Played when a nomatch event occurs during confirmation.

confirm_noinput_audio_group

(Confirm NoInput)

No

No

Played when a noinput event occurs during confirmation.

confirm_help_audio_group

(Confirm Help)

No

No

Played when the caller asks for help during the
                                             confirmation menu. If not specified, help is treated as a nomatch by
                                             default.

max_disconfirmed_audio_group

(Max Disconfirmed)

No

Yes

Played after the caller disconfirms the recorded entry, upon reaching the max_disconfirmed_count . The prompt should be about
                                             exiting with the max_disconfirmed exit state.

## Folder and Class Information

Studio
                                             Element Folder Name

Class Name

Record

com.audium.server.voiceElement.record.MRecordWithConfirm

## Events

Name (Label)

Notes

Event Handler

You can
                                          				  select either VXML Event or Java Exception as event handler type from the
                                          				  drop-down list.

| The Record_With_Confirm voice element combines the
                                    functionality of the Record voice element with that of the MenuYesNo voice
                                    element. The voice element records the caller’s voice, then prompts the caller
                                    to confirm that the recording is acceptable. The caller can then accept or
                                    reject the confirmation or ask to have the message replayed. If the caller
                                    accepts the recording, the voice element saves the file just as the Record
                                    voice element does. This voice element contains all settings and audio groups
                                    from both the Record and MenuYesNo voice elements, however audio groups that
                                    are found in both voice elements (nomatch, noinput, and help) are now named
                                    differently for them to be
                                    distinguished. |
|---|

| Name (Label) | Type | Req'd | Single Setting Value | Sub. Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| inputmode (Input Mode) | string enum | Yes | true | true | both | The type of
                                          				  entry allowed for input during confirmation. Possible values are: voice \| dtmf \| both . |
| noinput_timeout (Noinput
                                          				  Timeout) | string | Yes | true | true | 5s | The maximum time allowed for silence or no keypress before a noinput event is thrown. Possible values are standard time designations
                                          including both a non-negative number and a time unit, for example, 3s (for seconds) or 3000ms (for milliseconds). Default
                                          = 5s. |
| record_max_noinput_count (Record Max
                                          				  NoInput Count) | int ≥ 0 | Yes | true | true | 3 | The maximum
                                          				  number of noinput events allowed during input capture. 0 = infinite noinputs
                                          				  allowed. |
| confirm_max_noinput_count (Confirm Max
                                          				  NoInput Count) | int ≥ 0 | Yes | true | true | 3 | The maximum
                                          				  number of noinput events allowed during confirmation. 0 = infinite noinputs
                                          				  allowed. |
| confirm_max_nomatch_count (Confirm Max
                                          				  NoMatch Count) | int ≥ 0 | Yes | true | true | 3 | The maximum
                                          				  number of nomatch events allowed during confirmation. 0 = infinite nomatches
                                          				  allowed. |
| max_disconfirmed_count (Max
                                          				  Disconfirmed Count) | int ≥ 0 | Yes | true | true | 3 | The maximum
                                          				  number of times a caller is allowed to reject a recording. 0 = infinite
                                          				  disconfirmations allowed. Note Special
                                                   				  consideration must be taken for the "ivr record memory session" setting on the
                                                   				  gateway: Each time a caller "disconfirms" a recording made while using the
                                                   				  Record_With_Confirm element, the disaffirmed recording(s) remain in memory on
                                                   				  the gateway. Depending on the "ivr record memory session" setting on the
                                                   				  gateway and the configured values for the "Max Disconfirmed Count" and "Max
                                                   				  Record Time" settings in the Record_With_Confirm element, a caller may exhaust
                                                   				  all available memory on the gateway for their session. At which point the
                                                   				  gateway will drop the call. Note In
                                                   				  general, to prevent calls from being dropped while using the
                                                   				  Record_With_Confirm element, the following formula should be adhered to: ("Max
                                                   				  Record Time" in seconds * audio codec bitrate in kilobytes/second) * "Max
                                                   				  Disconfirmed Count" < "ivr record memory session" setting, in kilobytes.
                                                   				  Testing should be done by increasing values for the gateway's "ivr record
                                                   				  memory session" setting until an acceptable amount of audio/retries are
                                                   				  accepted without exhausting the gateway’s session memory (dropped calls). | Note | Special
                                                   				  consideration must be taken for the "ivr record memory session" setting on the
                                                   				  gateway: Each time a caller "disconfirms" a recording made while using the
                                                   				  Record_With_Confirm element, the disaffirmed recording(s) remain in memory on
                                                   				  the gateway. Depending on the "ivr record memory session" setting on the
                                                   				  gateway and the configured values for the "Max Disconfirmed Count" and "Max
                                                   				  Record Time" settings in the Record_With_Confirm element, a caller may exhaust
                                                   				  all available memory on the gateway for their session. At which point the
                                                   				  gateway will drop the call. | Note | In
                                                   				  general, to prevent calls from being dropped while using the
                                                   				  Record_With_Confirm element, the following formula should be adhered to: ("Max
                                                   				  Record Time" in seconds * audio codec bitrate in kilobytes/second) * "Max
                                                   				  Disconfirmed Count" < "ivr record memory session" setting, in kilobytes.
                                                   				  Testing should be done by increasing values for the gateway's "ivr record
                                                   				  memory session" setting until an acceptable amount of audio/retries are
                                                   				  accepted without exhausting the gateway’s session memory (dropped calls). |
| Note | Special
                                                   				  consideration must be taken for the "ivr record memory session" setting on the
                                                   				  gateway: Each time a caller "disconfirms" a recording made while using the
                                                   				  Record_With_Confirm element, the disaffirmed recording(s) remain in memory on
                                                   				  the gateway. Depending on the "ivr record memory session" setting on the
                                                   				  gateway and the configured values for the "Max Disconfirmed Count" and "Max
                                                   				  Record Time" settings in the Record_With_Confirm element, a caller may exhaust
                                                   				  all available memory on the gateway for their session. At which point the
                                                   				  gateway will drop the call. |
| Note | In
                                                   				  general, to prevent calls from being dropped while using the
                                                   				  Record_With_Confirm element, the following formula should be adhered to: ("Max
                                                   				  Record Time" in seconds * audio codec bitrate in kilobytes/second) * "Max
                                                   				  Disconfirmed Count" < "ivr record memory session" setting, in kilobytes.
                                                   				  Testing should be done by increasing values for the gateway's "ivr record
                                                   				  memory session" setting until an acceptable amount of audio/retries are
                                                   				  accepted without exhausting the gateway’s session memory (dropped calls). |
| confirm_confidence_level (Confirm
                                          				  Confidence Level) | decimal (0.0
                                          				  – 1.0) | Yes | true | true | 0.50 | The
                                          				  confidence level threshold to use for the confirmation. |
| start_with_beep (Start With
                                          				  Beep) | boolean | Yes | true | true | true | Whether or
                                          				  not to play a beep before recording begins. |
| terminate_on_dtmf (Terminate
                                          				  On DTMF) | boolean | Yes | true | true | true | Whether or
                                          				  not the caller can end the recording by pressing a touchtone key. |
| keep_recording_on_hangup (Keep
                                          				  Recording On Hangup) | boolean | Yes | true | true | false | Whether or
                                          				  not the recording is stored if the caller hung up while making the recording or
                                          				  during the confirmation menu. Default = false. |
| max_record_time (Max Record
                                          				  Time) | string | Yes | true | true | 180s | The maximum
                                          				  time (in seconds) the recording is allowed to last. Possible values are
                                          				  standard time designations including a positive integer followed by s (for
                                          				  seconds), for example, 30s. Default = 180s. |
| final_silence (Final
                                          				  Silence) | string | Yes | true | true | 4s | The interval
                                          				  of silence (in seconds or milliseconds) that indicates the end of speech.
                                          				  Possible values are standard time designations including both a positive
                                          				  integer and a time unit identifier, for example, 3s (for 3 seconds) or 300ms
                                          				  (for 300 milliseconds). Default = 4s. Note For
                                                         						silence detection to work, you must enable Voice Activity Detection (VAD) in
                                                         						the gateway dial-peers. Manually remove NO VAD from the configuration script
                                                         						and replace it with VAD. | Note | For
                                                         						silence detection to work, you must enable Voice Activity Detection (VAD) in
                                                         						the gateway dial-peers. Manually remove NO VAD from the configuration script
                                                         						and replace it with VAD. |
| Note | For
                                                         						silence detection to work, you must enable Voice Activity Detection (VAD) in
                                                         						the gateway dial-peers. Manually remove NO VAD from the configuration script
                                                         						and replace it with VAD. |
| replay (Replay) | boolean | Yes | true | true | false | Adds an
                                          				  option to replay the confirm initial audio groups. |
| filename (Filename) | string | No | true | true | None | The filename
                                          				  of the recording (without extension). If left blank, an auto-generated filename
                                          				  will be used. |
| file_type (File Type) | string enum | Yes | true | true | wav | This
                                          				  specifies the audio type of the file that will hold the recording. Possible
                                          				  values are: wav \| vox \| au \| other . |
| mime_type (Mime Type) | string | Yes | true | true | None | This
                                          				  specifies the MIME type of the file that will hold the recording, if file_type
                                          				  is set to other . |
| file_extension (File
                                          				  Extension) | string | No | true | true | None | This
                                          				  specifies the file extension to use for the recorded file. A file extension
                                          				  different from the file type can be used. For example, with a mime type of vox , the file extension could be set to ulaw . |
| path (Path) | string | No | true | true | None | The path to
                                          				  the file that will hold the recording. Either the path, ftp host, or both must
                                          				  be specified. |
| ftp_host (FTP Host) | string | No | true | true | None | The domain
                                          				  name of the host to FTP the recording. Either the path, ftp host, or both must
                                          				  be specified. |
| Secure (Secure) | boolean | Yes | true | true | false | Whether or
                                          				  not to enable Secure File Transfer protocol (SFTP). Default = false, indicates
                                          				  file transfer happens over FTP by default. |
| ftp_user (FTP User) | string | Yes | true | true | None | The user
                                          				  name to use while FTPing the recording, if ftp_host is set. |
| ftp_password (FTP
                                          				  Password) | string | Yes | true | true | None | The password
                                          				  to use while FTPing the recording, if ftp_host is set. |
| ftp_path (FTP Path) | string | No | true | true | None | The
                                          				  directory in which to FTP the recording, if ftp_host is set. |
| ftp_in_background (FTP In
                                          				  Background) | boolean | Yes | true | true | true | Whether or
                                          				  not the FTP is to be performed in the background, if ftp_host is set. |

| Note | Special
                                                   				  consideration must be taken for the "ivr record memory session" setting on the
                                                   				  gateway: Each time a caller "disconfirms" a recording made while using the
                                                   				  Record_With_Confirm element, the disaffirmed recording(s) remain in memory on
                                                   				  the gateway. Depending on the "ivr record memory session" setting on the
                                                   				  gateway and the configured values for the "Max Disconfirmed Count" and "Max
                                                   				  Record Time" settings in the Record_With_Confirm element, a caller may exhaust
                                                   				  all available memory on the gateway for their session. At which point the
                                                   				  gateway will drop the call. |
|---|---|

| Note | In
                                                   				  general, to prevent calls from being dropped while using the
                                                   				  Record_With_Confirm element, the following formula should be adhered to: ("Max
                                                   				  Record Time" in seconds * audio codec bitrate in kilobytes/second) * "Max
                                                   				  Disconfirmed Count" < "ivr record memory session" setting, in kilobytes.
                                                   				  Testing should be done by increasing values for the gateway's "ivr record
                                                   				  memory session" setting until an acceptable amount of audio/retries are
                                                   				  accepted without exhausting the gateway’s session memory (dropped calls). |
|---|---|

| Note | For
                                                         						silence detection to work, you must enable Voice Activity Detection (VAD) in
                                                         						the gateway dial-peers. Manually remove NO VAD from the configuration script
                                                         						and replace it with VAD. |
|---|---|

| Note For
                                                   				  settings, for Record_With_Confirm, follow these procedures: The path setting does not
                                             					 require a trailing slash. The voice element will determine the appropriate
                                             					 destination. The path may be specified in operating system specific format (for
                                             					 example, on Windows it might be specified as C:\directory\subdirectory\ and on UNIX it might be /usr/local/directory/ ). For a recording to be
                                             					 stored, you can choose either to store it locally or remotely. For locally on
                                             					 the VXML server itself, configure only the filename ( myfile ) and the
                                             					 path ( c:/recordings/ ). For remotely on a ftp server,
                                             					 configure the filename ( myfile ) and the FTP details such as: host, user, path,
                                             					 and password. Once your record element is configured, determine the url to
                                             					 access the recording from an external system. Run a simple test by playing the
                                             					 recording from your web browser. Make use of the url:
                                             					 http://<ftpserver>/<ftppath>/filename . Find the correct path to
                                             					 play the audio file and use the same url in the audio element settings. If terminate_on_DTMF is false or off, recording will stop only after the voice browser reaches the input timeout. Some voice browsers may not
                                             					 accept all options provided for the file_type and mime_type settings. Check your voice browser
                                             					 documentation for information on supported audio types. It is important to ensure
                                             					 that VXML Server has permission to save audio files to the specified path. | Note | For
                                                   				  settings, for Record_With_Confirm, follow these procedures: |
|---|---|---|
| Note | For
                                                   				  settings, for Record_With_Confirm, follow these procedures: |

| Note | For
                                                   				  settings, for Record_With_Confirm, follow these procedures: |
|---|---|

| Name | Type | Notes |
|---|---|---|
| filename | string | This stores the filename of the recording (without
                                          the path). |
| filepath | string | This stores the path to the file holding the
                                          recording (including the filename). |
| confirm_confidence | float | This is the confidence value of the utterance for the confirmation
                                          menu. |
| hungUpWhileRecording | boolean | This stores a true if the caller hung up while making the recording or
                                          the confirmation menu, false if
                                          not. |

| Name | Notes |
|---|---|
| max_nomatch | The maximum number of nomatch events has occurred. If the nomatch max
                                          count is 0, this exit state will never occur. |
| max_noinput | The maximum number of noinput events has occurred. If the noinput max
                                          count is 0, this exit state will never occur. |
| max_disconfirmed | The maximum number of disconfirmations has
                                          occurred. If the max disconfirmed count is set to 0, this exit state will never
                                          occur. |
| done | The recorded message was
                                          confirmed. |

| Name (Label) | Req'd | Max1 | Notes |
|---|---|---|---|
| record_initial_audio_group (Record Initial) | Yes | Yes | Played when the voice
                                             element first begins. |
| record_noinput_audio_group (Record NoInput) | No | No | Played when a noinput event
                                             occurs during recording. |

| Name
                                                (Label) | Req'd | Max1 | Notes |
|---|---|---|---|
| before_confirm_audio_group (Before Confirm) | No | Yes | Played before the
                                             recording is played back. The recording will be played back after this audio
                                             group is done playing. |
| after_confirm_audio_group (After Confirm) | No | Yes | Played after the recording
                                             is played back. At least one of the two confirm prompts must be
                                             specified. |
| confirm_nomatch_audio_group (Confirm NoMatch) | No | No | Played when a nomatch event occurs during confirmation. |
| confirm_noinput_audio_group (Confirm NoInput) | No | No | Played when a noinput event occurs during confirmation. |
| confirm_help_audio_group (Confirm Help) | No | No | Played when the caller asks for help during the
                                             confirmation menu. If not specified, help is treated as a nomatch by
                                             default. |
| max_disconfirmed_audio_group (Max Disconfirmed) | No | Yes | Played after the caller disconfirms the recorded entry, upon reaching the max_disconfirmed_count . The prompt should be about
                                             exiting with the max_disconfirmed exit state. |

| Studio
                                             Element Folder Name | Class Name |
|---|---|
| Record | com.audium.server.voiceElement.record.MRecordWithConfirm |

| Name (Label) | Notes |
|---|---|
| Event Handler | You can
                                          				  select either VXML Event or Java Exception as event handler type from the
                                          				  drop-down list. |