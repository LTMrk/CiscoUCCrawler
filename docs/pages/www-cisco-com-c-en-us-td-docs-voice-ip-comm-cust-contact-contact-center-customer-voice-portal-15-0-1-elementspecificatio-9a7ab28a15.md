---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-elementspecificatio-9a7ab28a15
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/elementspecification/guide/ccvp_b_150-element-specifications-guide-for-cvp-vxml-and-call-studio/date_with_confirm.html
retrieved_at: 2026-08-21T17:10:47.885914+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 15.0(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 15.0(1)

Updated: April 30, 2025

Chapter: Date_with_Confirm

## Chapter: Date_with_Confirm

# Date_with_Confirm

The Date_With_Confirm voice element captures a date
                                    				input from the caller, and presents a confirmation menu allowing the caller to
                                    				either accept their entry or re-enter the date. The date can be entered using
                                    				DTMF input (in the YYYYMMDD format). It can also be spoken in natural language
                                    				including a month, day and year. The captured value will be stored in element
                                    				data as a fixed-length date string in the YYYYMMDD format. If the year is not
                                    				specified in the input, YYYY is stored as "????" . If the month or the day is not specified, MM and DD
                                    				will be stored as "??" .

## Settings

Name (Label)

Type

Req'd

Single Setting Value

Substitution Allowed

Default

Notes

inputmode

(Input Mode)

string enum

Yes

true

false

both

The type of
                                          				  entry allowed for input. Possible values are: voice | dtmf | both .

noinput_timeout

(Noinput
                                          				  Timeout)

string

Yes

true

true

5s

The maximum time length allowed for silence or no keypress before a noinput event is thrown. Possible values are standard
                                          time designations including both a non-negative number and a time unit, for example, 3s (for seconds) or 3000ms (for milliseconds).
                                          Default = 5s.

collect_max_noinput_count

(Date Max
                                          				  NoInput Count)

int ≥ 0

Yes

true

true

3

The maximum
                                          				  number of noinput events allowed during date input capture. 0 = infinite
                                          				  noinputs allowed.

collect_max_nomatch_count

(Date Max
                                          				  NoMatch Count)

int ≥ 0

Yes

true

false

3

The maximum
                                          				  number of nomatch events allowed during date input capture. 0 = infinite
                                          				  nomatches allowed.

confirm_max_noinput_count

(Confirm Max
                                          				  NoInput Count)

int ≥ 0

Yes

true

true

3

The maximum
                                          				  number of noinput events allowed during date input confirmation. 0 = infinite
                                          				  noinputs allowed.

confirm_max_nomatch_count

(Confirm Max
                                          				  NoMatch Count)

int ≥ 0

Yes

true

false

3

The maximum
                                          				  number of nomatch events allowed during date input confirmation. 0 = infinite
                                          				  nomatches allowed.

max_disconfirmed_count

(Max
                                          				  Disconfirmed Count)

int ≥ 0

Yes

true

false

3

The maximum
                                          				  number of times a caller is allowed to disconfirm a captured input. 0 =
                                          				  infinite disconfirmations allowed.

collect_confidence_level

(Date
                                          				  Confidence Level)

decimal (0.0
                                          				  – 1.0)

Yes

true

false

0.40

The
                                          				  confidence level threshold to use during date capture.

confirm_confidence_level

(Confirm
                                          				  Confidence Level)

decimal (0.0
                                          				  – 1.0)

Yes

true

false

0.50

The
                                          				  confidence level threshold to use during confirmation.

modal

(Disable
                                          				  Hotlinks)

boolean

Yes

true

false

false

If set to
                                          				  true, only the grammars of the current Date_With_Confirm element (the built-in
                                          				  date and boolean grammars) will be enabled for the duration of the element.
                                          				  Otherwise all active grammars will be enabled.

secure_logging

(Secure
                                          				  Logging)

boolean

Yes

true

false

false

If set to true, user DTMF input for the element is considered
                                          				  secure and the attributes utterance, interpretation, value, nbestUtteranceX and
                                          				  nbestInterpretationX are masked in VXML server logs. The format used to render
                                          				  secure element attributes is to add a _secureLogging suffix. For example nbestUtterance1_secureLogging,***** .

maxnbest

(Maxnbest)

int ≥ 1

Yes

true

false

1

The maximum
                                          				  number of speech recognition results that can be generated per voice input.

Refer to the
                              		  following Element Data table for information about nbestUtteranceX and
                              		  nbestInterpretationX.

## Element Data

Name

Type

Notes

value

string

The date stored in the YYYYMMDD format.

value_confidence

float

This is the confidence
                                          value of the captured date utterance. When n-best recognition is enabled, this
                                          stores the confidence score of the top hypothesis in the n-best
                                          list.

confirm_confidence

float

This is the confidence
                                          value of the captured confirm utterance.

nbestLength

int ≥ 1

This
                                          stores the number of n-best hypotheses generated by the speech engine.

nbestUtterance1

nbestUtterance2

…

nbestUtteranceX

string

This set of element data stores the captured n-best
                                          utterances. While the maximum number of nbestUtteranceX values is equal to the
                                          maxnbest setting value, the actual number of these values available is
                                          determined by speech recognition at runtime, where nbestUtterance1 holds the
                                          utterance of the top hypothesis in the n-best list and nbestUtteranceX holds
                                          the utterance of the last hypothesis.

nbestInterpretation1

nbestInterpretation2

…

nbestInterpretationX

string

This set of element data stores the interpretations
                                          of captured n-best utterances. While the maximum number of nbestInterpretationX
                                          values is equal to the maxnbest setting value, the actual number of these
                                          values available is determined by speech recognition at runtime, where
                                          nbestInterpretation1 holds the interpretation of the top hypothesis in the
                                          n-best list and nbestInterpretationX holds the interpretation of the last
                                          hypothesis.

nbestConfidence1

nbestConfidence2

…

nbestConfidenceX

float

This set of element data
                                          stores the confidence scores of captured n-best utterances. While the maximum
                                          number of nbestConfidenceX values is equal to the maxnbest setting value, the
                                          actual number of these values available is determined by speech recognition at
                                          runtime, where nbestConfidence1 holds the confidence score of the top
                                          hypothesis in the n-best list and nbestConfidenceX holds the confidence score
                                          of the last hypothesis.

nbestInputmode1

nbestInputmode2

…

nbestInputmodeX

string

This set of element data
                                          stores the input modes of captured n-best
                                          utterances.

## Exit States

Name

Notes

max_nomatch

The maximum number of nomatch events has occurred. If the max nomatch
                                          count is 0, this exit state will never occur.

max_noinput

The maximum number of noinput events has occurred. If the max noinput
                                          count is 0, this exit state will never occur.

max_disconfirmed

The maximum number of disconfirmations occurred. If
                                          the max_disconfirmed_count is set to 0, this exit
                                          state will never occur.

done

The date captured was
                                          confirmed.

## Audio Groups

### Date Capture

Name
                                                (Label)

Req'd

Max 1

Notes

collect_initial_audio_group

(Date Initial)

Yes

Yes

Played when the voice
                                             element first begins.

collect_noinput_audio_group

(Date NoInput)

No

No

Played when a noinput event
                                             occurs during date input. The noinput event count corresponds to the audio
                                             group count.

collect_nomatch_audio_group

(Date NoMatch)

No

No

Played when a nomatch event
                                             occurs during date input. The nomatch event count corresponds to the audio
                                             group count.

collect_help_audio_group

(Date Help)

No

No

Played when a help event
                                             occurs during date input. The help event count corresponds to the audio group
                                             count. If not specified, a help event is treated as
                                             nomatch.

### Date Confirm

Name (Label)

Req'd

Max 1

Notes

confirm_initial_audio_group

(Confirm Initial)

Yes

Yes

Played when the captured date is confirmed.

confirm_noinput_audio_group

(Confirm NoInput)

No

No

Played when a noinput event occurs during date confirmation. The
                                             				  noinput event count corresponds to the audio group count.

confirm_nomatch_audio_group

(Confirm NoMatch)

No

No

Played when a nomatch event occurs during date confirmation. The
                                             				  nomatch event count corresponds to the audio group count.

confirm_help_audio_group

(Confirm Help)

No

No

Played when a help event occurs during date confirmation. The
                                             				  help event count corresponds to the audio group count. If not specified, by
                                             				  default help is treated as nomatch.

disconfirmed_audio_group (Disconfirmed)

No

No

Played after the caller disconfirms a date entry.

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

Played after the caller chooses the yes option. If not specified, no audio will be played when
                                             this option is
                                             chosen.

## Folder and Class Information

Studio
                                             Element Folder Name

Class Name

Date & Time

com.audium.server.voiceElement.date.MBasicDateWithConfirm

## Events

Name (Label)

Notes

Event Type

You can select Java Exception , VXML Event , or Hotlink as event handler for this element.

| The Date_With_Confirm voice element captures a date
                                    				input from the caller, and presents a confirmation menu allowing the caller to
                                    				either accept their entry or re-enter the date. The date can be entered using
                                    				DTMF input (in the YYYYMMDD format). It can also be spoken in natural language
                                    				including a month, day and year. The captured value will be stored in element
                                    				data as a fixed-length date string in the YYYYMMDD format. If the year is not
                                    				specified in the input, YYYY is stored as "????" . If the month or the day is not specified, MM and DD
                                    				will be stored as "??" . |
|---|

| Name (Label) | Type | Req'd | Single Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| inputmode (Input Mode) | string enum | Yes | true | false | both | The type of
                                          				  entry allowed for input. Possible values are: voice \| dtmf \| both . |
| noinput_timeout (Noinput
                                          				  Timeout) | string | Yes | true | true | 5s | The maximum time length allowed for silence or no keypress before a noinput event is thrown. Possible values are standard
                                          time designations including both a non-negative number and a time unit, for example, 3s (for seconds) or 3000ms (for milliseconds).
                                          Default = 5s. |
| collect_max_noinput_count (Date Max
                                          				  NoInput Count) | int ≥ 0 | Yes | true | true | 3 | The maximum
                                          				  number of noinput events allowed during date input capture. 0 = infinite
                                          				  noinputs allowed. |
| collect_max_nomatch_count (Date Max
                                          				  NoMatch Count) | int ≥ 0 | Yes | true | false | 3 | The maximum
                                          				  number of nomatch events allowed during date input capture. 0 = infinite
                                          				  nomatches allowed. |
| confirm_max_noinput_count (Confirm Max
                                          				  NoInput Count) | int ≥ 0 | Yes | true | true | 3 | The maximum
                                          				  number of noinput events allowed during date input confirmation. 0 = infinite
                                          				  noinputs allowed. |
| confirm_max_nomatch_count (Confirm Max
                                          				  NoMatch Count) | int ≥ 0 | Yes | true | false | 3 | The maximum
                                          				  number of nomatch events allowed during date input confirmation. 0 = infinite
                                          				  nomatches allowed. |
| max_disconfirmed_count (Max
                                          				  Disconfirmed Count) | int ≥ 0 | Yes | true | false | 3 | The maximum
                                          				  number of times a caller is allowed to disconfirm a captured input. 0 =
                                          				  infinite disconfirmations allowed. |
| collect_confidence_level (Date
                                          				  Confidence Level) | decimal (0.0
                                          				  – 1.0) | Yes | true | false | 0.40 | The
                                          				  confidence level threshold to use during date capture. |
| confirm_confidence_level (Confirm
                                          				  Confidence Level) | decimal (0.0
                                          				  – 1.0) | Yes | true | false | 0.50 | The
                                          				  confidence level threshold to use during confirmation. |
| modal (Disable
                                          				  Hotlinks) | boolean | Yes | true | false | false | If set to
                                          				  true, only the grammars of the current Date_With_Confirm element (the built-in
                                          				  date and boolean grammars) will be enabled for the duration of the element.
                                          				  Otherwise all active grammars will be enabled. |
| secure_logging (Secure
                                          				  Logging) | boolean | Yes | true | false | false | If set to true, user DTMF input for the element is considered
                                          				  secure and the attributes utterance, interpretation, value, nbestUtteranceX and
                                          				  nbestInterpretationX are masked in VXML server logs. The format used to render
                                          				  secure element attributes is to add a _secureLogging suffix. For example nbestUtterance1_secureLogging,***** . |
| maxnbest (Maxnbest) | int ≥ 1 | Yes | true | false | 1 | The maximum
                                          				  number of speech recognition results that can be generated per voice input. |

| Name | Type | Notes |
|---|---|---|
| value | string | The date stored in the YYYYMMDD format. |
| value_confidence | float | This is the confidence
                                          value of the captured date utterance. When n-best recognition is enabled, this
                                          stores the confidence score of the top hypothesis in the n-best
                                          list. |
| confirm_confidence | float | This is the confidence
                                          value of the captured confirm utterance. |
| nbestLength | int ≥ 1 | This
                                          stores the number of n-best hypotheses generated by the speech engine. |
| nbestUtterance1 nbestUtterance2 … nbestUtteranceX | string | This set of element data stores the captured n-best
                                          utterances. While the maximum number of nbestUtteranceX values is equal to the
                                          maxnbest setting value, the actual number of these values available is
                                          determined by speech recognition at runtime, where nbestUtterance1 holds the
                                          utterance of the top hypothesis in the n-best list and nbestUtteranceX holds
                                          the utterance of the last hypothesis. |
| nbestInterpretation1 nbestInterpretation2 … nbestInterpretationX | string | This set of element data stores the interpretations
                                          of captured n-best utterances. While the maximum number of nbestInterpretationX
                                          values is equal to the maxnbest setting value, the actual number of these
                                          values available is determined by speech recognition at runtime, where
                                          nbestInterpretation1 holds the interpretation of the top hypothesis in the
                                          n-best list and nbestInterpretationX holds the interpretation of the last
                                          hypothesis. |
| nbestConfidence1 nbestConfidence2 … nbestConfidenceX | float | This set of element data
                                          stores the confidence scores of captured n-best utterances. While the maximum
                                          number of nbestConfidenceX values is equal to the maxnbest setting value, the
                                          actual number of these values available is determined by speech recognition at
                                          runtime, where nbestConfidence1 holds the confidence score of the top
                                          hypothesis in the n-best list and nbestConfidenceX holds the confidence score
                                          of the last hypothesis. |
| nbestInputmode1 nbestInputmode2 … nbestInputmodeX | string | This set of element data
                                          stores the input modes of captured n-best
                                          utterances. |

| Name | Notes |
|---|---|
| max_nomatch | The maximum number of nomatch events has occurred. If the max nomatch
                                          count is 0, this exit state will never occur. |
| max_noinput | The maximum number of noinput events has occurred. If the max noinput
                                          count is 0, this exit state will never occur. |
| max_disconfirmed | The maximum number of disconfirmations occurred. If
                                          the max_disconfirmed_count is set to 0, this exit
                                          state will never occur. |
| done | The date captured was
                                          confirmed. |

| Name
                                                (Label) | Req'd | Max 1 | Notes |
|---|---|---|---|
| collect_initial_audio_group (Date Initial) | Yes | Yes | Played when the voice
                                             element first begins. |
| collect_noinput_audio_group (Date NoInput) | No | No | Played when a noinput event
                                             occurs during date input. The noinput event count corresponds to the audio
                                             group count. |
| collect_nomatch_audio_group (Date NoMatch) | No | No | Played when a nomatch event
                                             occurs during date input. The nomatch event count corresponds to the audio
                                             group count. |
| collect_help_audio_group (Date Help) | No | No | Played when a help event
                                             occurs during date input. The help event count corresponds to the audio group
                                             count. If not specified, a help event is treated as
                                             nomatch. |

| Name (Label) | Req'd | Max 1 | Notes |
|---|---|---|---|
| confirm_initial_audio_group (Confirm Initial) | Yes | Yes | Played when the captured date is confirmed. |
| confirm_noinput_audio_group (Confirm NoInput) | No | No | Played when a noinput event occurs during date confirmation. The
                                             				  noinput event count corresponds to the audio group count. |
| confirm_nomatch_audio_group (Confirm NoMatch) | No | No | Played when a nomatch event occurs during date confirmation. The
                                             				  nomatch event count corresponds to the audio group count. |
| confirm_help_audio_group (Confirm Help) | No | No | Played when a help event occurs during date confirmation. The
                                             				  help event count corresponds to the audio group count. If not specified, by
                                             				  default help is treated as nomatch. |
| disconfirmed_audio_group (Disconfirmed) | No | No | Played after the caller disconfirms a date entry. |

| Name
                                                (Label) | Req'd | Max 1 | Notes |
|---|---|---|---|
| yes_audio_group (Yes) | No | Yes | Played after the caller chooses the yes option. If not specified, no audio will be played when
                                             this option is
                                             chosen. |

| Studio
                                             Element Folder Name | Class Name |
|---|---|
| Date & Time | com.audium.server.voiceElement.date.MBasicDateWithConfirm |

| Name (Label) | Notes |
|---|---|
| Event Type | You can select Java Exception , VXML Event , or Hotlink as event handler for this element. |