---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-12-6-2-elementspecificatio-a0a7d3bf16
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/12-6-2/elementspecification/guide/ccvp_b_1262-element-specifications-guide/ccvp_mp_na5fd92f_00_number_with_confirm.html
retrieved_at: 2026-08-21T17:19:52.191781+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(2)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(2)

Updated: April 28, 2023

Chapter: Number_with_Confirm

## Chapter: Number_with_Confirm

# Number_with_Confirm

The Number_With_Confirm voice element captures a
                                    				standard number, and presents a confirmation menu allowing the caller to either
                                    				accept their entry or re-enter the number. The number can be spoken or entered
                                    				using the keypad. The resulting value will be stored in element data as a
                                    				decimal value. The number can be negative or positive and can contain a decimal
                                    				point. Using DTMF entry, however, the number is restricted to being positive
                                    				and the decimal point is entered by pressing the * key. Using speech input, the
                                    				number may be spoken naturally.

## Events

Name (Label)

Notes

Event Type

You can select Java Exception , VXML Event , or Hotlink as event handler for this element.

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

The maximum time allowed for silence or no keypress before a noinput event is thrown. Possible values are standard time designations
                                          including both a non-negative number and a time unit, for example, 3s (for seconds) or 3000ms (for milliseconds). Default
                                          = 5s.

number_max_noinput_count

(Number Max
                                          				  NoInput Count)

int ≥ 0

Yes

true

true

3

The maximum
                                          				  number of noinput events allowed during number input capture. 0 = infinite
                                          				  noinputs allowed.

number_max_nomatch_count

(Number Max
                                          				  NoMatch Count)

int ≥ 0

Yes

true

true

3

The maximum
                                          				  number of nomatch events allowed during number input capture. 0 = infinite
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
                                          				  number of noinput events allowed during number input confirmation. 0 = infinite
                                          				  noinputs allowed.

confirm_max_nomatch_count

(Confirm Max
                                          				  NoMatch Count)

int ≥ 0

Yes

true

true

3

The maximum
                                          				  number of nomatch events allowed during number input confirmation. 0 = infinite
                                          				  nomatches allowed.

max_disconfirmed_count

(Max
                                          				  Disconfirmed Count)

int ≥ 0

Yes

true

true

3

The maximum
                                          				  number of times a caller is allowed to disconfirm a captured input. 0 =
                                          				  infinite disconfirmations allowed.

number_confidence_level

(Number
                                          				  Confidence Level)

decimal (0.0
                                          				  – 1.0)

Yes

true

true

0.40

The
                                          				  confidence level threshold to use during number capture.

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

modal

(Disable
                                          				  Hotlinks)

boolean

Yes

true

true

false

If set to true, only the grammars of the current Number_With_Confirm element (the builtin number and boolean grammars) will be enabled for the duration of the element. Otherwise all active grammars
                                          will be enabled.

secure_logging

(Secure
                                          				  Logging)

boolean

Yes

true

true

false

If set to true, user DTMF input for the element is considered secure and the attributes utterance, interpretation, value, nbestUtteranceX and nbestInterpretationX are masked in VXML server logs. The format used to render secure element attributes is to add a _secureLogging suffix. For example nbestUtterance1_secureLogging,***** .

maxnbest

(Maxnbest)

int ≥ 1

Yes

true

true

1

The maximum
                                          				  number of speech recognition results that can be generated per voice input.

dtmf_overlay

(DTMF Overlay)

Boolean

Yes

true

true

false

Setting this property to true will enable the generation of random DTMF digits tone at random duration while DTMF recognition is in progress.

dtmf_overlay supports only the following VoiceXML Gateways, and one of these options must be selected before creating or deploying the
                                                      Call Studio application.

Cisco DTMF

VoiceXML 2.1 Cisco DTMF

dtmf_overlay_interval

(DTMF Overlay Interval)

String

Yes

true

true

1000ms

Time Interval (in ms) between the generation of two DTMF tones. The interval is a random number that is +/-25% of the duration
                                          that is mentioned. For example, if the duration mentioned is 1000ms , the interval will be between between 750ms and 1250ms.

The duration mentioned must be between 500ms (minimum) and 2000ms (maximum).

Refer to the
                              		  Element Data table for information about nbestUtteraceX and
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

This is the confidence value of the captured number utterance. When
                                          n-best recognition is enabled, this stores the confidence score of the top
                                          hypothesis in the n-best list.

confirm_confidence

float

This is the confidence
                                          value of the captured confirm utterance.

nbestLength

int ≥ 1

This stores the number
                                          of n-best hypotheses generated by the speech engine.

nbestUtterance1

nbestUtterance2

…

nbestUtteranceX

string

This set of element data stores the captured n-best utterances. While the maximum number of nbestUtteranceX values is equal to the maxnbest setting value, the actual number of these values available is determined by speech recognition
                                          at runtime, where nbestUtterance1 holds the utterance of the top hypothesis in the n-best list and nbestUtteranceX holds the utterance of the last hypothesis.

nbestInterpretation1

nbestInterpretation2

…

nbestInterpretationX

string

This set of element data stores the interpretations of captured n-best utterances. While the maximum number of nbestInterpretationX values is equal to the maxnbest setting value, the actual number of these values available is determined by speech recognition
                                          at runtime, where nbestInterpretation1 holds the interpretation of the top hypothesis in the n-best list and nbestInterpretationX holds the interpretation of the last hypothesis.

nbestConfidence1

nbestConfidence2

…

nbestConfidenceX

float

This set of element data stores the confidence scores of captured n-best utterances. While the maximum number of nbestConfidenceX values is equal to the maxnbest setting value, the actual number of these values available is determined by speech recognition
                                          at runtime, where nbestConfidence1 holds the confidence score of the top hypothesis in the n-best list and nbestConfidenceX holds the confidence score of the last hypothesis.

nbestInputmode1

nbestInputmode2

…

nbestInputmodeX

string

This set of element data stores the input modes of
                                          captured n-best
                                          utterances.

## Exit States

Name

Notes

max_nomatch

The maximum number of nomatch events has occurred. If the
                                          				  nomatch max count is 0, this exit state will never occur.

max_noinput

The maximum number of noinput events has occurred. If the noinput max count is 0, this exit state will never occur.

max_disconfirmed

The maximum number of disconfirmations has occurred. If the max disconfirmed count is set to 0, this exit state will never
                                          occur.

done

The number captured was confirmed.

## Audio Groups

### Number Capture

Name (Label)

Req'd

Max1

Notes

number_initial_audio_group

(Number Initial)

Yes

Yes

Played when the voice
                                             element first begins.

number_nomatch_audio_group

(Number NoMatch)

No

No

Played when a nomatch event
                                             occurs during number capture.

number_noinput_audio_group

(Number NoInput)

No

No

Played when a noinput event
                                             occurs during number capture.

number_help_audio_group

(Number Help)

No

No

Played when the caller asks
                                             for help during number capture. If not specified, by default help is treated as
                                             a nomatch.

### Number Confirm

Name (Label)

Req'd

Max1

Notes

confirm_initial_audio_group

(Confirm Initial)

Yes

Yes

Played when confirmation first begins.

confirm_nomatch_audio_group

(Confirm NoMatch)

No

No

Played when a nomatch event occurs during confirmation. The
                                             				  nomatch event count corresponds to the audio group count.

confirm_noinput_audio_group

(Confirm NoInput)

No

No

Played when a noinput event occurs during confirmation. The
                                             				  noinput event count corresponds to the audio group count.

confirm_help_audio_group

(Confirm Help)

No

No

Played when a help event occurs during confirmation. The help
                                             				  event count corresponds to the audio group count. If not specified, help throws
                                             				  a nomatch by default.

disconfirmed_audio_group

(Disconfirmed)

No

No

Played after the caller disconfirms a captured number entry.

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

com.audium.server.voiceElement.number.

MBasicNumberWithConfirm

| The Number_With_Confirm voice element captures a
                                    				standard number, and presents a confirmation menu allowing the caller to either
                                    				accept their entry or re-enter the number. The number can be spoken or entered
                                    				using the keypad. The resulting value will be stored in element data as a
                                    				decimal value. The number can be negative or positive and can contain a decimal
                                    				point. Using DTMF entry, however, the number is restricted to being positive
                                    				and the decimal point is entered by pressing the * key. Using speech input, the
                                    				number may be spoken naturally. |
|---|

| Name (Label) | Notes |
|---|---|
| Event Type | You can select Java Exception , VXML Event , or Hotlink as event handler for this element. |

| Name (Label) | Type | Req'd | Single Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| inputmode (Input Mode) | string enum | Yes | true | false | both | The type of
                                          				  entry allowed for input. Possible values are: voice \| dtmf \| both . |
| noinput_timeout (Noinput
                                          				  Timeout) | string | Yes | true | true | 5s | The maximum time allowed for silence or no keypress before a noinput event is thrown. Possible values are standard time designations
                                          including both a non-negative number and a time unit, for example, 3s (for seconds) or 3000ms (for milliseconds). Default
                                          = 5s. |
| number_max_noinput_count (Number Max
                                          				  NoInput Count) | int ≥ 0 | Yes | true | true | 3 | The maximum
                                          				  number of noinput events allowed during number input capture. 0 = infinite
                                          				  noinputs allowed. |
| number_max_nomatch_count (Number Max
                                          				  NoMatch Count) | int ≥ 0 | Yes | true | true | 3 | The maximum
                                          				  number of nomatch events allowed during number input capture. 0 = infinite
                                          				  nomatches allowed. |
| confirm_max_noinput_count (Confirm Max
                                          				  NoInput Count) | int ≥ 0 | Yes | true | true | 3 | The maximum
                                          				  number of noinput events allowed during number input confirmation. 0 = infinite
                                          				  noinputs allowed. |
| confirm_max_nomatch_count (Confirm Max
                                          				  NoMatch Count) | int ≥ 0 | Yes | true | true | 3 | The maximum
                                          				  number of nomatch events allowed during number input confirmation. 0 = infinite
                                          				  nomatches allowed. |
| max_disconfirmed_count (Max
                                          				  Disconfirmed Count) | int ≥ 0 | Yes | true | true | 3 | The maximum
                                          				  number of times a caller is allowed to disconfirm a captured input. 0 =
                                          				  infinite disconfirmations allowed. |
| number_confidence_level (Number
                                          				  Confidence Level) | decimal (0.0
                                          				  – 1.0) | Yes | true | true | 0.40 | The
                                          				  confidence level threshold to use during number capture. |
| confirm_confidence_level (Confirm
                                          				  Confidence Level) | decimal (0.0
                                          				  – 1.0) | Yes | true | true | 0.50 | The
                                          				  confidence level threshold to use during confirmation. |
| modal (Disable
                                          				  Hotlinks) | boolean | Yes | true | true | false | If set to true, only the grammars of the current Number_With_Confirm element (the builtin number and boolean grammars) will be enabled for the duration of the element. Otherwise all active grammars
                                          will be enabled. |
| secure_logging (Secure
                                          				  Logging) | boolean | Yes | true | true | false | If set to true, user DTMF input for the element is considered secure and the attributes utterance, interpretation, value, nbestUtteranceX and nbestInterpretationX are masked in VXML server logs. The format used to render secure element attributes is to add a _secureLogging suffix. For example nbestUtterance1_secureLogging,***** . |
| maxnbest (Maxnbest) | int ≥ 1 | Yes | true | true | 1 | The maximum
                                          				  number of speech recognition results that can be generated per voice input. |
| dtmf_overlay (DTMF Overlay) | Boolean | Yes | true | true | false | Setting this property to true will enable the generation of random DTMF digits tone at random duration while DTMF recognition is in progress. Note dtmf_overlay supports only the following VoiceXML Gateways, and one of these options must be selected before creating or deploying the
                                                      Call Studio application. Cisco DTMF VoiceXML 2.1 Cisco DTMF | Note | dtmf_overlay supports only the following VoiceXML Gateways, and one of these options must be selected before creating or deploying the
                                                      Call Studio application. Cisco DTMF VoiceXML 2.1 Cisco DTMF |
| Note | dtmf_overlay supports only the following VoiceXML Gateways, and one of these options must be selected before creating or deploying the
                                                      Call Studio application. Cisco DTMF VoiceXML 2.1 Cisco DTMF |
| dtmf_overlay_interval (DTMF Overlay Interval) | String | Yes | true | true | 1000ms | Time Interval (in ms) between the generation of two DTMF tones. The interval is a random number that is +/-25% of the duration
                                          that is mentioned. For example, if the duration mentioned is 1000ms , the interval will be between between 750ms and 1250ms. Note The duration mentioned must be between 500ms (minimum) and 2000ms (maximum). | Note | The duration mentioned must be between 500ms (minimum) and 2000ms (maximum). |
| Note | The duration mentioned must be between 500ms (minimum) and 2000ms (maximum). |

| Note | dtmf_overlay supports only the following VoiceXML Gateways, and one of these options must be selected before creating or deploying the
                                                      Call Studio application. Cisco DTMF VoiceXML 2.1 Cisco DTMF |
|---|---|

| Note | The duration mentioned must be between 500ms (minimum) and 2000ms (maximum). |
|---|---|

| Name | Type | Notes |
|---|---|---|
| Value | string | The number captured and stored as a whole or
                                          decimal number with an optional minus sign. |
| value_confidence | float | This is the confidence value of the captured number utterance. When
                                          n-best recognition is enabled, this stores the confidence score of the top
                                          hypothesis in the n-best list. |
| confirm_confidence | float | This is the confidence
                                          value of the captured confirm utterance. |
| nbestLength | int ≥ 1 | This stores the number
                                          of n-best hypotheses generated by the speech engine. |
| nbestUtterance1 nbestUtterance2 … nbestUtteranceX | string | This set of element data stores the captured n-best utterances. While the maximum number of nbestUtteranceX values is equal to the maxnbest setting value, the actual number of these values available is determined by speech recognition
                                          at runtime, where nbestUtterance1 holds the utterance of the top hypothesis in the n-best list and nbestUtteranceX holds the utterance of the last hypothesis. |
| nbestInterpretation1 nbestInterpretation2 … nbestInterpretationX | string | This set of element data stores the interpretations of captured n-best utterances. While the maximum number of nbestInterpretationX values is equal to the maxnbest setting value, the actual number of these values available is determined by speech recognition
                                          at runtime, where nbestInterpretation1 holds the interpretation of the top hypothesis in the n-best list and nbestInterpretationX holds the interpretation of the last hypothesis. |
| nbestConfidence1 nbestConfidence2 … nbestConfidenceX | float | This set of element data stores the confidence scores of captured n-best utterances. While the maximum number of nbestConfidenceX values is equal to the maxnbest setting value, the actual number of these values available is determined by speech recognition
                                          at runtime, where nbestConfidence1 holds the confidence score of the top hypothesis in the n-best list and nbestConfidenceX holds the confidence score of the last hypothesis. |
| nbestInputmode1 nbestInputmode2 … nbestInputmodeX | string | This set of element data stores the input modes of
                                          captured n-best
                                          utterances. |

| Name | Notes |
|---|---|
| max_nomatch | The maximum number of nomatch events has occurred. If the
                                          				  nomatch max count is 0, this exit state will never occur. |
| max_noinput | The maximum number of noinput events has occurred. If the noinput max count is 0, this exit state will never occur. |
| max_disconfirmed | The maximum number of disconfirmations has occurred. If the max disconfirmed count is set to 0, this exit state will never
                                          occur. |
| done | The number captured was confirmed. |

| Note If the number to be captured is a positive whole number and
                                                   				  the input is via DTMF, the number can be entered using this voice element or
                                                   				  the Digits_With_Confirm voice element. | Note | If the number to be captured is a positive whole number and
                                                   				  the input is via DTMF, the number can be entered using this voice element or
                                                   				  the Digits_With_Confirm voice element. |
|---|---|---|
| Note | If the number to be captured is a positive whole number and
                                                   				  the input is via DTMF, the number can be entered using this voice element or
                                                   				  the Digits_With_Confirm voice element. |

| Note | If the number to be captured is a positive whole number and
                                                   				  the input is via DTMF, the number can be entered using this voice element or
                                                   				  the Digits_With_Confirm voice element. |
|---|---|

| Name (Label) | Req'd | Max1 | Notes |
|---|---|---|---|
| number_initial_audio_group (Number Initial) | Yes | Yes | Played when the voice
                                             element first begins. |
| number_nomatch_audio_group (Number NoMatch) | No | No | Played when a nomatch event
                                             occurs during number capture. |
| number_noinput_audio_group (Number NoInput) | No | No | Played when a noinput event
                                             occurs during number capture. |
| number_help_audio_group (Number Help) | No | No | Played when the caller asks
                                             for help during number capture. If not specified, by default help is treated as
                                             a nomatch. |

| Name (Label) | Req'd | Max1 | Notes |
|---|---|---|---|
| confirm_initial_audio_group (Confirm Initial) | Yes | Yes | Played when confirmation first begins. |
| confirm_nomatch_audio_group (Confirm NoMatch) | No | No | Played when a nomatch event occurs during confirmation. The
                                             				  nomatch event count corresponds to the audio group count. |
| confirm_noinput_audio_group (Confirm NoInput) | No | No | Played when a noinput event occurs during confirmation. The
                                             				  noinput event count corresponds to the audio group count. |
| confirm_help_audio_group (Confirm Help) | No | No | Played when a help event occurs during confirmation. The help
                                             				  event count corresponds to the audio group count. If not specified, help throws
                                             				  a nomatch by default. |
| disconfirmed_audio_group (Disconfirmed) | No | No | Played after the caller disconfirms a captured number entry. |

| Name
                                                (Label) | Req'd | Max 1 | Notes |
|---|---|---|---|
| yes_audio_group (Yes) | No | Yes | Played after the caller chooses the yes option. If not specified, no audio will be played when
                                             this option is
                                             chosen. |

| Studio
                                             Element Folder Name | Class Name |
|---|---|
| Number Capture | com.audium.server.voiceElement.number. MBasicNumberWithConfirm |