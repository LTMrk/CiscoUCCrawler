---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-12-6-2-elementspecificatio-8642b3330b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/12-6-2/elementspecification/guide/ccvp_b_1262-element-specifications-guide/ccvp_mp_y813230e_00_yes_no_menu.html
retrieved_at: 2026-08-21T17:21:19.389588+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(2)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(2)

Updated: April 28, 2023

Chapter: Yes_No_Menu

## Chapter: Yes_No_Menu

# Yes_No_Menu

## Settings

The Yes_No_Menu voice element presents a yes/no menu. It can be configured to accept DTMF entry (1 for yes and 2 for no) or spoken input
                              ( yes or no and other synonymous utterances, however this is dependent on the voice browser). There is an optional feature that allows
                              the word replay to be spoken (or DTMF button 3) that replays the initial_audio_group . The voice element uses the browser specific VoiceXML builtin grammar for the boolean field type. A separate exit state exists
                              for the yes and no choices (there is no exit state for replay since running of dialog is still within the confines of the
                              voice element).

Name (Label)

Type

Req'd

Single Setting Value

Sub. Allowed

Default

Notes

max_noinput_count

(Max NoInput
                                          				  Count)

int ≥ 0

Yes

true

true

3

0 = infinite
                                          				  noinputs allowed.

max_nomatch_count

(Max NoMatch
                                          				  Count)

int ≥ 0

Yes

true

true

3

0 = infinite
                                          				  nomatches allowed.

inputmode

(Input Mode)

string enum

Yes

true

false

both

The type of
                                          				  entry allowed for input (using speech recognition, DTMF entry, or both).
                                          				  Possible values are: voice | dtmf | both .

replay

(Replay)

boolean

Yes

true

true

false

True adds a replay option which replays the initial prompt.

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

confidence_level

(Confidence
                                          				  Level)

decimal (0.0
                                          				  – 1.0)

Yes

true

true

0.50

The
                                          				  confidence level threshold to use.

modal

(Disable
                                          				  Hotlinks)

boolean

Yes

true

true

false

Whether or
                                          				  not to temporarily disable all hotlink grammars (global or local) and universal
                                          				  grammars. If set to true, only the boolean builtin grammar will be enabled for
                                          				  the duration of the element. Otherwise all active grammars will be enabled.

## Element Data

Name

Type

Notes

value

string

This is the value chosen by the caller. Can be: yes or no .

value_confidence

float

This is the confidence value of the
                                          utterance.

## Exit States

Name

Notes

max_nomatch

The maximum number of nomatch events has occurred. If the nomatch max
                                          count is 0, this exit state will never occur.

max_noinput

The maximum number of noinput events has occurred. If the noinput max
                                          count is 0, this exit state will never occur.

yes

The
                                          utterance was recognized as yes .

no

The
                                          utterance was recognized as no .

## Audio Groups

### Yes / No Capture

Name
                                                (Label)

Req'd

Max1

Notes

initial_audio_group

(Initial)

Yes

Yes

Played when the voice
                                             element first begins.

nomatch_audio_group

(NoMatch)

No

No

Played when a nomatch event
                                             occurs.

noinput_audio_group

(NoInput)

No

No

Played when a noinput event
                                             occurs.

help_audio_group

(Help)

No

No

Played when the caller asks for help. If not
                                             specified, help is treated as a nomatch event by
                                             default.

### End

Name
                                                (Label)

Req'd

Max 1

Notes

yes_audio_group

(Yes)

No

Yes

Played when the caller chose the yes option. If not present, no audio will play when this
                                             option is
                                             chosen.

## Folder and Class Information

Studio
                                             Element Folder Name

Class Name

Menu

com.audium.server.voiceElement.menu.MYesNoMenu

## Events

Name (Label)

Notes

Event Type

You can select Java Exception , VXML Event , or Hotlink as event handler for this element.

| Name (Label) | Type | Req'd | Single Setting Value | Sub. Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| max_noinput_count (Max NoInput
                                          				  Count) | int ≥ 0 | Yes | true | true | 3 | 0 = infinite
                                          				  noinputs allowed. |
| max_nomatch_count (Max NoMatch
                                          				  Count) | int ≥ 0 | Yes | true | true | 3 | 0 = infinite
                                          				  nomatches allowed. |
| inputmode (Input Mode) | string enum | Yes | true | false | both | The type of
                                          				  entry allowed for input (using speech recognition, DTMF entry, or both).
                                          				  Possible values are: voice \| dtmf \| both . |
| replay (Replay) | boolean | Yes | true | true | false | True adds a replay option which replays the initial prompt. |
| noinput_timeout (Noinput
                                          				  Timeout) | string | Yes | true | true | 5s | The maximum time allowed for silence or no keypress before a noinput event is thrown. Possible values are standard time designations
                                          including both a non-negative number and a time unit, for example, 3s (for seconds) or 3000ms (for milliseconds). Default
                                          = 5s. |
| confidence_level (Confidence
                                          				  Level) | decimal (0.0
                                          				  – 1.0) | Yes | true | true | 0.50 | The
                                          				  confidence level threshold to use. |
| modal (Disable
                                          				  Hotlinks) | boolean | Yes | true | true | false | Whether or
                                          				  not to temporarily disable all hotlink grammars (global or local) and universal
                                          				  grammars. If set to true, only the boolean builtin grammar will be enabled for
                                          				  the duration of the element. Otherwise all active grammars will be enabled. |

| Name | Type | Notes |
|---|---|---|
| value | string | This is the value chosen by the caller. Can be: yes or no . |
| value_confidence | float | This is the confidence value of the
                                          utterance. |

| Name | Notes |
|---|---|
| max_nomatch | The maximum number of nomatch events has occurred. If the nomatch max
                                          count is 0, this exit state will never occur. |
| max_noinput | The maximum number of noinput events has occurred. If the noinput max
                                          count is 0, this exit state will never occur. |
| yes | The
                                          utterance was recognized as yes . |
| no | The
                                          utterance was recognized as no . |

| Note | The replay option, when activated, resets all the event counts (noinput
                                       and nomatch). |
|---|---|

| Name
                                                (Label) | Req'd | Max1 | Notes |
|---|---|---|---|
| initial_audio_group (Initial) | Yes | Yes | Played when the voice
                                             element first begins. |
| nomatch_audio_group (NoMatch) | No | No | Played when a nomatch event
                                             occurs. |
| noinput_audio_group (NoInput) | No | No | Played when a noinput event
                                             occurs. |
| help_audio_group (Help) | No | No | Played when the caller asks for help. If not
                                             specified, help is treated as a nomatch event by
                                             default. |

| Name
                                                (Label) | Req'd | Max 1 | Notes |
|---|---|---|---|
| yes_audio_group (Yes) | No | Yes | Played when the caller chose the yes option. If not present, no audio will play when this
                                             option is
                                             chosen. |

| Studio
                                             Element Folder Name | Class Name |
|---|---|
| Menu | com.audium.server.voiceElement.menu.MYesNoMenu |

| Name (Label) | Notes |
|---|---|
| Event Type | You can select Java Exception , VXML Event , or Hotlink as event handler for this element. |