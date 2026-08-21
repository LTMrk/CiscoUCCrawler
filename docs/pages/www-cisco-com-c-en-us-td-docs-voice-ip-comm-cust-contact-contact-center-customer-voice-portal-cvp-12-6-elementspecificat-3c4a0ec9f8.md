---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-elementspecificat-3c4a0ec9f8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/elementspecification/guide/ccvp_b_1261-element-specifications-guide/ccvp_mp_pc65c8f2_00_phone_with_confirm.html
retrieved_at: 2026-08-21T17:25:48.493978+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1)

Updated: February 18, 2020

Chapter: Phone_With_Confirm

## Chapter: Phone_With_Confirm

# Phone_With_Confirm

The Phone_With_Confirm voice element captures a phone
                                    				number input from the caller, and presents a confirmation menu allowing the
                                    				caller to either accept their entry or re-enter the phone number. The phone
                                    				number can be spoken or entered using the keypad. The captured value will be
                                    				stored in element data as a string. The string may contain a number of digits
                                    				and an optional character "x" to indicate a phone number with an extension. Using speech
                                    				input, the entire phone number (including the extension) may be spoken in
                                    				natural language. Using DTMF entry, the caller can enter an extension by
                                    				pressing the * keypress followed by the extension.

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

false

both

The type of
                                          				  entry allowed for input. Possible values are: voice | dtmf | both.

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

collect_max_noinput_count

(Phone Max
                                          				  NoInput Count)

int ≥ 0

Yes

true

true

3

The maximum
                                          				  number of noinput events allowed during phone input capture. 0 = infinite
                                          				  noinputs allowed.

collect_max_nomatch_count

(Phone Max
                                          				  NoMatch Count)

int ≥ 0

Yes

true

false

3

The maximum
                                          				  number of nomatch events allowed during phone input capture. 0 = infinite
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
                                          				  number of noinput events allowed during phone input confirmation. 0 = infinite
                                          				  noinputs allowed.

confirm_max_nomatch_count

(Confirm
                                          				  Max NoMatch Count)

int ≥ 0

Yes

true

false

3

The maximum
                                          				  number of nomatch events allowed during phone input confirmation. 0 = infinite
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

(Phone
                                          				  Confidence Level)

decimal (0.0
                                          				  – 1.0)

Yes

true

true

0.40

The
                                          				  confidence level threshold to use during phone capture.

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
                                          				  confidence level threshold to use during confirmation.

Modal

(Disable
                                          				  Hotlinks)

boolean

Yes

true

true

false

If set to
                                          				  true, only the grammars of the current Phone_With_Confirm element (the builtin
                                          				  phone and boolean grammars) will be enabled for the duration of the element.
                                          				  Otherwise all active grammars will be enabled.

secure_logging

(Secure
                                          				  Logging)

boolean

Yes

true

true

false

If set to true, user DTMF input for the element is considered
                                          				  secure and the attributes utterance, interpretation, value, nbestUtteranceX and
                                          				  nbestInterpretationX are masked in VXML server logs. The format used to render
                                          				  secure element attributes is to add a _secureLogging suffix. For example nbestUtterance1_secureLogging,***** .

Maxnbest

(Maxnbest)

int ≥ 1

Yes

true

true

1

The maximum
                                          				  number of speech recognition results that can be generated per voice input.

Refer to the
                                          				  Element Data table that follows for information about nbestUtteranceX and
                                          				  nbestInterpretationX.

## Element Data

Name

Type

Notes

Value

string

The number captured and stored as a whole or
                                          decimal number with an optional minus sign.

value_confidence

float

This is the confidence value of the captured utterance. When n-best
                                          recognition is enabled, this stores the confidence score of the top hypothesis
                                          in the n-best list.

nbestLength

int ≥
                                          1

This stores the number of n-best
                                          hypotheses generated by the speech engine.

nbestUtterance1

nbestUtterance2

…

nbestUtteranceX

string

This set of element data stores the captured n-best utterances. While the
                                          maximum number of nbestUtteranceX values is equal to
                                          the maxnbest setting value, the actual number of
                                          these values available is determined by speech recognition at runtime, where nbestUtterance1 holds the utterance of the top
                                          hypothesis in the n-best list and nbestUtteranceX holds the utterance of the last hypothesis.

nbestInterpretation1

nbestInterpretation2

…

nbestInterpretationX

string

This set of element data stores the interpretations
                                          of captured n-best utterances. While the maximum number of nbestInterpretationX values is equal to the maxnbest setting value, the actual number of these
                                          values available is determined by speech recognition at runtime, where nbestInterpretation1 holds the interpretation of the
                                          top hypothesis in the n-best list and nbestInterpretationX holds the interpretation of the
                                          last hypothesis.

nbestConfidence1

nbestConfidence2

…

nbestConfidenceX

float

This set of element data
                                          stores the confidence scores of captured n-best utterances. While the maximum
                                          number of nbestConfidenceX values is equal to the maxnbest setting value, the actual number of these
                                          values available is determined by speech recognition at runtime, where nbestConfidence1 holds the confidence score of the
                                          top hypothesis in the n-best list and nbestConfidenceX holds the confidence score of the
                                          last hypothesis.

nbestInputmode1

nbestInputmode2

…

nbestInputmodeX

string

This set of element
                                          data stores the input modes of captured n-best
                                          utterances.

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

The phone number captured was
                                          confirmed.

## Audio Groups

### Phone Capture

Name (Label)

Req'd

Max1

Notes

collect_initial_audio_group

(Phone Initial)

Yes

Yes

Played when the voice
                                             element first begins.

collect_noinput_audio_group

(Phone NoInput)

No

No

Played when a noinput event
                                             occurs.

collect_nomatch_audio_group

(Phone NoMatch)

No

No

Played when a nomatch event
                                             occurs.

collect_help_audio_group

(Phone Help)

No

No

Played when the caller
                                             asked for help. If not specified, help is treated as a nomatch by
                                             default.

### Phone Confirm

Name (Label)

Req'd

Max1

Notes

confirm_initial_audio_group

(Confirm Initial)

Yes

Yes

Played when confirmation first begins.

confirm_noinput_audio_group

(Confirm NoInput)

No

No

Played when a noinput event occurs during confirmation. The
                                             				  noinput event count corresponds to the audio group count.

confirm_nomatch_audio_group

(Confirm NoMatch)

No

No

Played when a nomatch event occurs during confirmation. The
                                             				  nomatch event count corresponds to the audio group count.

confirm_help_audio_group

(Confirm Help)

No

No

Played when a help event occurs during confirmation. The help
                                             				  event count corresponds to the audio group count.

disconfirmed_audio_group

(Disconfirmed)

No

No

Played after the caller disconfirms a captured phone entry. Upon
                                             				  reaching the max_disconfirmed_count , the prompt content
                                             				  should be about exiting with the max_disconfirmed exit state.

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

Number Capture

com.audium.server.voiceElement.phone.MBasicPhoneWithConfirm

## Events

Name (Label)

Notes

Event Type

You can select Java Exception , VXML Event , or Hotlink as event handler for this element.

| The Phone_With_Confirm voice element captures a phone
                                    				number input from the caller, and presents a confirmation menu allowing the
                                    				caller to either accept their entry or re-enter the phone number. The phone
                                    				number can be spoken or entered using the keypad. The captured value will be
                                    				stored in element data as a string. The string may contain a number of digits
                                    				and an optional character "x" to indicate a phone number with an extension. Using speech
                                    				input, the entire phone number (including the extension) may be spoken in
                                    				natural language. Using DTMF entry, the caller can enter an extension by
                                    				pressing the * keypress followed by the extension. |
|---|

| Name (Label) | Type | Req'd | Single Setting Value | Sub. Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| inputmode (Input Mode) | string enum | Yes | true | false | both | The type of
                                          				  entry allowed for input. Possible values are: voice \| dtmf \| both. |
| noinput_timeout (Noinput
                                          				  Timeout) | string | Yes | true | true | 5s | The maximum time allowed for silence or no keypress before a noinput event is thrown. Possible values are standard time designations
                                          including both a non-negative number and a time unit, for example, 3s (for seconds) or 3000ms (for milliseconds). Default
                                          = 5s. |
| collect_max_noinput_count (Phone Max
                                          				  NoInput Count) | int ≥ 0 | Yes | true | true | 3 | The maximum
                                          				  number of noinput events allowed during phone input capture. 0 = infinite
                                          				  noinputs allowed. |
| collect_max_nomatch_count (Phone Max
                                          				  NoMatch Count) | int ≥ 0 | Yes | true | false | 3 | The maximum
                                          				  number of nomatch events allowed during phone input capture. 0 = infinite
                                          				  nomatches allowed. |
| confirm_max_noinput_count (Confirm Max
                                          				  NoInput Count) | int ≥ 0 | Yes | true | true | 3 | The maximum
                                          				  number of noinput events allowed during phone input confirmation. 0 = infinite
                                          				  noinputs allowed. |
| confirm_max_nomatch_count (Confirm
                                          				  Max NoMatch Count) | int ≥ 0 | Yes | true | false | 3 | The maximum
                                          				  number of nomatch events allowed during phone input confirmation. 0 = infinite
                                          				  nomatches allowed. |
| max_disconfirmed_count (Max
                                          				  Disconfirmed Count) | int ≥ 0 | Yes | true | false | 3 | The maximum
                                          				  number of times a caller is allowed to disconfirm a captured input. 0 =
                                          				  infinite disconfirmations allowed. |
| collect_confidence_level (Phone
                                          				  Confidence Level) | decimal (0.0
                                          				  – 1.0) | Yes | true | true | 0.40 | The
                                          				  confidence level threshold to use during phone capture. |
| confirm_confidence_level (Confirm
                                          				  Confidence Level) | decimal (0.0
                                          				  – 1.0) | Yes | true | true | 0.50 | The
                                          				  confidence level threshold to use during confirmation. |
| Modal (Disable
                                          				  Hotlinks) | boolean | Yes | true | true | false | If set to
                                          				  true, only the grammars of the current Phone_With_Confirm element (the builtin
                                          				  phone and boolean grammars) will be enabled for the duration of the element.
                                          				  Otherwise all active grammars will be enabled. |
| secure_logging (Secure
                                          				  Logging) | boolean | Yes | true | true | false | If set to true, user DTMF input for the element is considered
                                          				  secure and the attributes utterance, interpretation, value, nbestUtteranceX and
                                          				  nbestInterpretationX are masked in VXML server logs. The format used to render
                                          				  secure element attributes is to add a _secureLogging suffix. For example nbestUtterance1_secureLogging,***** . |
| Maxnbest (Maxnbest) | int ≥ 1 | Yes | true | true | 1 | The maximum
                                          				  number of speech recognition results that can be generated per voice input. |

| Refer to the
                                          				  Element Data table that follows for information about nbestUtteranceX and
                                          				  nbestInterpretationX. |
|---|

| Name | Type | Notes |
|---|---|---|
| Value | string | The number captured and stored as a whole or
                                          decimal number with an optional minus sign. |
| value_confidence | float | This is the confidence value of the captured utterance. When n-best
                                          recognition is enabled, this stores the confidence score of the top hypothesis
                                          in the n-best list. |
| nbestLength | int ≥
                                          1 | This stores the number of n-best
                                          hypotheses generated by the speech engine. |
| nbestUtterance1 nbestUtterance2 … nbestUtteranceX | string | This set of element data stores the captured n-best utterances. While the
                                          maximum number of nbestUtteranceX values is equal to
                                          the maxnbest setting value, the actual number of
                                          these values available is determined by speech recognition at runtime, where nbestUtterance1 holds the utterance of the top
                                          hypothesis in the n-best list and nbestUtteranceX holds the utterance of the last hypothesis. |
| nbestInterpretation1 nbestInterpretation2 … nbestInterpretationX | string | This set of element data stores the interpretations
                                          of captured n-best utterances. While the maximum number of nbestInterpretationX values is equal to the maxnbest setting value, the actual number of these
                                          values available is determined by speech recognition at runtime, where nbestInterpretation1 holds the interpretation of the
                                          top hypothesis in the n-best list and nbestInterpretationX holds the interpretation of the
                                          last hypothesis. |
| nbestConfidence1 nbestConfidence2 … nbestConfidenceX | float | This set of element data
                                          stores the confidence scores of captured n-best utterances. While the maximum
                                          number of nbestConfidenceX values is equal to the maxnbest setting value, the actual number of these
                                          values available is determined by speech recognition at runtime, where nbestConfidence1 holds the confidence score of the
                                          top hypothesis in the n-best list and nbestConfidenceX holds the confidence score of the
                                          last hypothesis. |
| nbestInputmode1 nbestInputmode2 … nbestInputmodeX | string | This set of element
                                          data stores the input modes of captured n-best
                                          utterances. |

| Name | Notes |
|---|---|
| max_nomatch | The maximum number of nomatch events has occurred. If the nomatch max
                                          count is 0, this exit state will never occur. |
| max_noinput | The maximum number of noinput events has occurred. If the noinput max
                                          count is 0, this exit state will never occur. |
| max_disconfirmed | The maximum number of disconfirmations has
                                          occurred. If the max disconfirmed count is set to 0, this exit state will never
                                          occur. |
| done | The phone number captured was
                                          confirmed. |

| Name (Label) | Req'd | Max1 | Notes |
|---|---|---|---|
| collect_initial_audio_group (Phone Initial) | Yes | Yes | Played when the voice
                                             element first begins. |
| collect_noinput_audio_group (Phone NoInput) | No | No | Played when a noinput event
                                             occurs. |
| collect_nomatch_audio_group (Phone NoMatch) | No | No | Played when a nomatch event
                                             occurs. |
| collect_help_audio_group (Phone Help) | No | No | Played when the caller
                                             asked for help. If not specified, help is treated as a nomatch by
                                             default. |

| Name (Label) | Req'd | Max1 | Notes |
|---|---|---|---|
| confirm_initial_audio_group (Confirm Initial) | Yes | Yes | Played when confirmation first begins. |
| confirm_noinput_audio_group (Confirm NoInput) | No | No | Played when a noinput event occurs during confirmation. The
                                             				  noinput event count corresponds to the audio group count. |
| confirm_nomatch_audio_group (Confirm NoMatch) | No | No | Played when a nomatch event occurs during confirmation. The
                                             				  nomatch event count corresponds to the audio group count. |
| confirm_help_audio_group (Confirm Help) | No | No | Played when a help event occurs during confirmation. The help
                                             				  event count corresponds to the audio group count. |
| disconfirmed_audio_group (Disconfirmed) | No | No | Played after the caller disconfirms a captured phone entry. Upon
                                             				  reaching the max_disconfirmed_count , the prompt content
                                             				  should be about exiting with the max_disconfirmed exit state. |

| Name
                                                (Label) | Req'd | Max 1 | Notes |
|---|---|---|---|
| yes_audio_group (Yes) | No | Yes | Played after the caller chooses the yes option. If not specified, no audio will be played when
                                             this option is
                                             chosen. |

| Studio
                                             Element Folder Name | Class Name |
|---|---|
| Number Capture | com.audium.server.voiceElement.phone.MBasicPhoneWithConfirm |

| Name (Label) | Notes |
|---|---|
| Event Type | You can select Java Exception , VXML Event , or Hotlink as event handler for this element. |