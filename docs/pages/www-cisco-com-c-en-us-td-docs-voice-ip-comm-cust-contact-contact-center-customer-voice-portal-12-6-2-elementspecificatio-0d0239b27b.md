---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-12-6-2-elementspecificatio-0d0239b27b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/12-6-2/elementspecification/guide/ccvp_b_1262-element-specifications-guide/ccvp_mp_df169a0a_00_digits.html
retrieved_at: 2026-08-21T17:19:06.055036+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(2)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(2)

Updated: April 28, 2023

Chapter: Digits

## Chapter: Digits

# Digits

The Digits voice element captures a string of
                                    				numerical digits. It may be used to collect small or large strings of digits.
                                    				The digit string can be spoken or entered using the keypad. The captured value
                                    				will be stored in element data as a string. The string cannot contain any
                                    				non-numerical characters. Using speech input, the number is spoken one digit at
                                    				a time (that is, 49678 is spoken four nine six seven eight ). DTMF input can be terminated by
                                    				a # keypress if desired (if not used, the entry is considered terminated when
                                    				the input timeout has been reached).

With the Digits voice element, the application designer has the
                                    				ability to set length restrictions on the digit string. A minimum and maximum
                                    				length can be given to narrow the criteria. If a string of a specific length is
                                    				required, the minimum and maximum lengths should be set to the same value. If
                                    				fewer digits are entered, a nomatch event will be thrown. A string of digits
                                    				with length greater than the maximum length cannot be entered.

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

String enum

Yes

true

false

both

The type of
                                          				  entry allowed for input. Possible values are: voice | dtmf | both .

noinput_timeout

(Noinput
                                          				  Timeout)

String

Yes

true

true

5s

The maximum time allowed for silence or no keypress before a noinput event is thrown. Possible values are standard time designations
                                          including both a non-negative number and a time unit, for example, 3s (for seconds) or 3000ms (for milliseconds). Default
                                          = 5s.

max_noinput_count

(Digits Max
                                          				  NoInput Count)

int ≥ 0

Yes

true

true

3

The maximum
                                          				  number of noinput events allowed during digits input capture. 0 = infinite
                                          				  noinputs allowed.

max_nomatch_count

(Digits Max
                                          				  NoMatch Count)

int ≥ 0

Yes

true

true

3

The maximum
                                          				  number of nomatch events allowed during digits input capture. 0 = infinite
                                          				  nomatches allowed.

digits_confidence_level

(Digits
                                          				  Confidence Level)

Decimal (0.0 to 1.0)

Yes

true

true

0.40

The
                                          				  confidence level threshold to use during digits capture.

min_digit

(Min Digits)

int > 0

Yes

true

true

None

Minimum
                                          				  number of digits allowed.

max_digit

(Max Digits)

int ≥ 0

Yes

true

true

None

Maximum
                                          				  number of digits allowed.

modal

(Disable
                                          				  Hotlinks)

Boolean

Yes

true

true

false

If set to
                                          				  true, only the grammars of the current Digits element will be enabled for the
                                          				  duration of the element. Otherwise all active grammars will be enabled.

secure_logging

(Secure
                                          				  Logging)

Boolean

Yes

true

true

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
                                          				  following Element Data table for information about nbestUtteranceX and
                                          				  nbestInterpretationX

## Element Data

Name

Type

Notes

Value

string

The digit string value
                                          captured.

value_confidence

float

This is the confidence
                                          value of the captured utterance. When n-best recognition is enabled, this
                                          stores the confidence score of the top hypothesis in the n-best
                                          list.

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
                                          maximum number of nbestUtteranceX values is equal to the maxnbest setting
                                          value, the actual number of these values available is determined by speech
                                          recognition at runtime, where nbestUtterance1 holds the utterance of the top
                                          hypothesis in the n-best list and nbestUtteranceX holds the utterance of the
                                          last hypothesis.

nbestInterpretation1

nbestInterpretation2

…

nbestInterpretationX

string

This set of element data
                                          stores the interpretations of captured n-best utterances. While the maximum
                                          number of nbestInterpretationX values is equal to the maxnbest setting value,
                                          the actual number of these values available is determined by speech recognition
                                          at runtime, where nbestInterpretation1 holds the interpretation of the top
                                          hypothesis in the n-best list and nbestInterpretationX holds the interpretation
                                          of the last hypothesis.

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

The maximum number of nomatch events has occurred. If the nomatch max
                                          count is 0, this exit state will never occur.

max_noinput

The maximum number of noinput events has occurred. If the noinput max
                                          count is 0, this exit state will never occur.

done

The
                                          digit string capture was
                                          completed.

## Audio Groups

### Digits Capture

Name (Label)

Req'd

Max1

Notes

digits_initial_audio_group

(Digits Initial)

Yes

Yes

Played when the voice element first begins.

digits_nomatch_audio_group

(Digits NoMatch)

No

No

Played when a nomatch event occurs.

digits_noinput_audio_group

(Digits NoInput)

No

No

Played when a noinput event occurs.

digits_help_audio_group

(Digits Help)

No

No

Played when the caller asked for help. If not specified, help is treated as a nomatch by default.

### End

Name
                                                (Label)

Req'd

Max1

Notes

done_audio_group

(Done)

No

Yes

Played when the digits
                                             capture is completed and the voice element exits with the done exit
                                             state.

## Folder and Class Information

Studio
                                             Element Folder Name

Class Name

Number Capture

com.audium.server.voiceElement.digit.MBasicDigit

## Events

Name (Label)

Notes

Event Type

You can select Java Exception , VXML Event , or Hotlink as event handler for this element.

| The Digits voice element captures a string of
                                    				numerical digits. It may be used to collect small or large strings of digits.
                                    				The digit string can be spoken or entered using the keypad. The captured value
                                    				will be stored in element data as a string. The string cannot contain any
                                    				non-numerical characters. Using speech input, the number is spoken one digit at
                                    				a time (that is, 49678 is spoken four nine six seven eight ). DTMF input can be terminated by
                                    				a # keypress if desired (if not used, the entry is considered terminated when
                                    				the input timeout has been reached). With the Digits voice element, the application designer has the
                                    				ability to set length restrictions on the digit string. A minimum and maximum
                                    				length can be given to narrow the criteria. If a string of a specific length is
                                    				required, the minimum and maximum lengths should be set to the same value. If
                                    				fewer digits are entered, a nomatch event will be thrown. A string of digits
                                    				with length greater than the maximum length cannot be entered. |
|---|

| Name (Label) | Type | Req'd | Single Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| inputmode (Input Mode) | String enum | Yes | true | false | both | The type of
                                          				  entry allowed for input. Possible values are: voice \| dtmf \| both . |
| noinput_timeout (Noinput
                                          				  Timeout) | String | Yes | true | true | 5s | The maximum time allowed for silence or no keypress before a noinput event is thrown. Possible values are standard time designations
                                          including both a non-negative number and a time unit, for example, 3s (for seconds) or 3000ms (for milliseconds). Default
                                          = 5s. |
| max_noinput_count (Digits Max
                                          				  NoInput Count) | int ≥ 0 | Yes | true | true | 3 | The maximum
                                          				  number of noinput events allowed during digits input capture. 0 = infinite
                                          				  noinputs allowed. |
| max_nomatch_count (Digits Max
                                          				  NoMatch Count) | int ≥ 0 | Yes | true | true | 3 | The maximum
                                          				  number of nomatch events allowed during digits input capture. 0 = infinite
                                          				  nomatches allowed. |
| digits_confidence_level (Digits
                                          				  Confidence Level) | Decimal (0.0 to 1.0) | Yes | true | true | 0.40 | The
                                          				  confidence level threshold to use during digits capture. |
| min_digit (Min Digits) | int > 0 | Yes | true | true | None | Minimum
                                          				  number of digits allowed. |
| max_digit (Max Digits) | int ≥ 0 | Yes | true | true | None | Maximum
                                          				  number of digits allowed. |
| modal (Disable
                                          				  Hotlinks) | Boolean | Yes | true | true | false | If set to
                                          				  true, only the grammars of the current Digits element will be enabled for the
                                          				  duration of the element. Otherwise all active grammars will be enabled. |
| secure_logging (Secure
                                          				  Logging) | Boolean | Yes | true | true | false | If set to true, user DTMF input for the element is considered
                                          				  secure and the attributes utterance, interpretation, value, nbestUtteranceX and
                                          				  nbestInterpretationX are masked in VXML server logs. The format used to render
                                          				  secure element attributes is to add a _secureLogging suffix. For example nbestUtterance1_secureLogging,***** . |
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

| Refer to the
                                          				  following Element Data table for information about nbestUtteranceX and
                                          				  nbestInterpretationX |
|---|

| Name | Type | Notes |
|---|---|---|
| Value | string | The digit string value
                                          captured. |
| value_confidence | float | This is the confidence
                                          value of the captured utterance. When n-best recognition is enabled, this
                                          stores the confidence score of the top hypothesis in the n-best
                                          list. |
| nbestLength | int ≥
                                          1 | This stores the number of n-best
                                          hypotheses generated by the speech engine. |
| nbestUtterance1 nbestUtterance2 … nbestUtteranceX | string | This set of element data stores the captured n-best utterances. While the
                                          maximum number of nbestUtteranceX values is equal to the maxnbest setting
                                          value, the actual number of these values available is determined by speech
                                          recognition at runtime, where nbestUtterance1 holds the utterance of the top
                                          hypothesis in the n-best list and nbestUtteranceX holds the utterance of the
                                          last hypothesis. |
| nbestInterpretation1 nbestInterpretation2 … nbestInterpretationX | string | This set of element data
                                          stores the interpretations of captured n-best utterances. While the maximum
                                          number of nbestInterpretationX values is equal to the maxnbest setting value,
                                          the actual number of these values available is determined by speech recognition
                                          at runtime, where nbestInterpretation1 holds the interpretation of the top
                                          hypothesis in the n-best list and nbestInterpretationX holds the interpretation
                                          of the last hypothesis. |
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
| max_nomatch | The maximum number of nomatch events has occurred. If the nomatch max
                                          count is 0, this exit state will never occur. |
| max_noinput | The maximum number of noinput events has occurred. If the noinput max
                                          count is 0, this exit state will never occur. |
| done | The
                                          digit string capture was
                                          completed. |

| Name (Label) | Req'd | Max1 | Notes |
|---|---|---|---|
| digits_initial_audio_group (Digits Initial) | Yes | Yes | Played when the voice element first begins. |
| digits_nomatch_audio_group (Digits NoMatch) | No | No | Played when a nomatch event occurs. |
| digits_noinput_audio_group (Digits NoInput) | No | No | Played when a noinput event occurs. |
| digits_help_audio_group (Digits Help) | No | No | Played when the caller asked for help. If not specified, help is treated as a nomatch by default. |

| Name
                                                (Label) | Req'd | Max1 | Notes |
|---|---|---|---|
| done_audio_group (Done) | No | Yes | Played when the digits
                                             capture is completed and the voice element exits with the done exit
                                             state. |

| Studio
                                             Element Folder Name | Class Name |
|---|---|
| Number Capture | com.audium.server.voiceElement.digit.MBasicDigit |

| Name (Label) | Notes |
|---|---|
| Event Type | You can select Java Exception , VXML Event , or Hotlink as event handler for this element. |