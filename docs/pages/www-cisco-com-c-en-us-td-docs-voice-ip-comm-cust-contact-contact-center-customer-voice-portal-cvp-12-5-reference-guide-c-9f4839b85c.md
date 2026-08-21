---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-5-reference-guide-c-9f4839b85c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_5/reference/guide/ccvp_b_1251-element-specification-guide-cvp/ccvp_mp_c7ef9a4c_00_currency.html
retrieved_at: 2026-08-21T17:31:57.243552+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.5(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.5(1)

Updated: January 31, 2020

Chapter: Currency

## Chapter: Currency

# Currency

The Currency voice element captures from the caller a currency amount
                                    				in dollars and cents. The currency amount can be entered using the keypad or
                                    				spoken. The captured value will be stored in element data as a decimal value
                                    				(without the $ character).

Utterance

Stored Value

Example

Description

[dollar] "dollar(s)" ("and") [cent] "cent(s)"

D.CC

"thirteen dollars and fifty cents " = 13.50

Dollars are whole numbers >= 0. Cents are from 00 to 99. The
                                    				word and is optional.

[dollar] "dollar(s) "[cent]

D.CC

"thirteen dollars five" = 13.05

Dollars are whole numbers >= 0. Cents are from 00 to 99.

[dollar] "dollar(s)"

D.00

"three hundred fifty" = 350.00

A plain whole number is interpreted as dollars with no cents.

[cent] "cent(s)"

0.CC

"three cents" = 0.03

To specify cents only, the word cents to be uttered. Cents are from 00 to 99.

DTMF Entry

Stored Value

Example

Description

[D]*[CC]

D.CC

3*99 = 3.99

The decimal is represented by the * button.

There are other formats that are possible, particularly when entering via DTMF and inputting incomplete amounts. These inputs
                                    may yield differing results on various voice browsers. The returned variable will always be a decimal value with the appropriate
                                    number of padded zeros, if applicable.

## Settings

Name (Label)

Type

Req'd

Single Setting Value

Substitution Allowed

Default

Notes

Inputmode

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
                                          Default = 5s

max_noinput_count

(Max NoInput
                                          				  Count)

int ≥ 0

Yes

true

true

3

The maximum
                                          				  number of noinput events allowed during currency input capture. 0 = infinite
                                          				  noinputs allowed.

max_nomatch_count

(Max NoMatch
                                          				  Count)

int ≥ 0

Yes

true

true

3

The maximum
                                          				  number of nomatch events allowed during currency input capture. 0 = infinite
                                          				  nomatches allowed.

currency_confidence_level

(Currency
                                          				  Confidence Level)

decimal (0.0
                                          				  to 1.0)

Yes

true

true

0.40

The
                                          				  confidence level threshold to use during currency capture.

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
                                          				  grammars. If set to true, only the currency grammars will be enabled for the
                                          				  duration of the element. Otherwise all active grammars will be enabled.

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

maxnbest

(Maxnbest)

int ≥ 1

Yes

true

true

1

The maximum
                                          				  number of speech recognition results that can be generated per voice input.

## Element Data

Name

Type

Notes

Value

string

The currency amount captured. This will always be
                                          a decimal number with the appropriate number of padded zeros (up to
                                          2).

value_confidence

float

This is the confidence
                                          value of the captured utterance. When n-best recognition is enabled, this
                                          stores the confidence score of the top hypothesis in the n-best
                                          list.

nbestLength

int ≥ 1

This stores the number of n-best hypotheses
                                          generated by the speech engine.

nbestUtterance1

nbestUtterance2

…

nbestUtteranceX

string

This set of element
                                          data stores the captured n-best utterances. While the maximum number of
                                          nbestUtteranceX values is equal to the maxnbest setting value, the actual
                                          number of these values available is determined by speech recognition at
                                          runtime, where nbestUtterance1 holds the utterance of the top hypothesis in the
                                          n-best list and nbestUtteranceX holds the utterance of the last
                                          hypothesis.

nbestInterpretation1

nbestInterpretation2

…

nbestInterpretationX

string

This set of element
                                          data stores the interpretations of captured n-best utterances. While the
                                          maximum number of nbestInterpretationX values is equal to the maxnbest setting
                                          value, the actual number of these values available is determined by speech
                                          recognition at runtime, where nbestInterpretation1 holds the interpretation of
                                          the top hypothesis in the n-best list and nbestInterpretationX holds the
                                          interpretation of the last hypothesis.

nbestConfidence1

nbestConfidence2

…

nbestConfidenceX

float

This set of element data stores the confidence
                                          scores of captured n-best utterances. While the maximum number of
                                          nbestConfidenceX values is equal to the maxnbest setting value, the actual
                                          number of these values available is determined by speech recognition at
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
                                          currency capture was
                                          completed.

## Audio Groups

### Currency Capture

Name
                                                (Label)

Req'd

Max 1

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

Played when the caller asked for help. If not
                                             specified, by default help is treated as a
                                             nomatch.

### End

Name
                                                (Label)

Req'd

Max 1

Notes

done_audio_group

(Done)

No

Yes

Played when the currency
                                             capture is completed and the voice element exits with the done exit
                                             state.

## Folder and Class Information

Studio
                                             Element Folder Name

Class Name

Commerce

com.audium.server.voiceElement.currency.MBasicCurrency

## Events

Name (Label)

Notes

Event Type

You can select Java Exception , VXML Event , or Hotlink as event handler for this element.

| The Currency voice element captures from the caller a currency amount
                                    				in dollars and cents. The currency amount can be entered using the keypad or
                                    				spoken. The captured value will be stored in element data as a decimal value
                                    				(without the $ character). There are several different formats for speaking a currency amount
                                    				or entering it through the keypad. Voice browsers may use different grammars
                                    				and therefore accept different utterances. However, the spoken formats listed
                                    				below should result in the same behavior for all supported browsers. The tables
                                    				below list each input and the value that is stored in the element variable as a
                                    				result. If some data is left out, the system assumes a default value for the
                                    				missing information. Note You cannot use the * character to represent a decimal point in the Currency voice element, if  you have defined it as a termchar in the Root Doc Settings . | Note | You cannot use the * character to represent a decimal point in the Currency voice element, if  you have defined it as a termchar in the Root Doc Settings . |
|---|---|---|
| Note | You cannot use the * character to represent a decimal point in the Currency voice element, if  you have defined it as a termchar in the Root Doc Settings . |

| Note | You cannot use the * character to represent a decimal point in the Currency voice element, if  you have defined it as a termchar in the Root Doc Settings . |
|---|---|

| Utterance | Stored Value | Example | Description |
|---|---|---|---|
| [dollar] "dollar(s)" ("and") [cent] "cent(s)" | D.CC | "thirteen dollars and fifty cents " = 13.50 | Dollars are whole numbers >= 0. Cents are from 00 to 99. The
                                    				word and is optional. |
| [dollar] "dollar(s) "[cent] | D.CC | "thirteen dollars five" = 13.05 | Dollars are whole numbers >= 0. Cents are from 00 to 99. |
| [dollar] "dollar(s)" | D.00 | "three hundred fifty" = 350.00 | A plain whole number is interpreted as dollars with no cents. |
| [cent] "cent(s)" | 0.CC | "three cents" = 0.03 | To specify cents only, the word cents to be uttered. Cents are from 00 to 99. |

| DTMF Entry | Stored Value | Example | Description |
|---|---|---|---|
| [D]*[CC] | D.CC | 3*99 = 3.99 | The decimal is represented by the * button. |

| There are other formats that are possible, particularly when entering via DTMF and inputting incomplete amounts. These inputs
                                    may yield differing results on various voice browsers. The returned variable will always be a decimal value with the appropriate
                                    number of padded zeros, if applicable. |
|---|

| Name (Label) | Type | Req'd | Single Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| Inputmode (Input Mode) | string enum | Yes | true | false | both | The type of
                                          				  entry allowed for input. Possible values are: voice \| dtmf \| both . |
| noinput_timeout (Noinput
                                          				  Timeout) | string | Yes | true | true | 5s | The maximum time length allowed for silence or no keypress before a noinput event is thrown. Possible values are standard
                                          time designations including both a non-negative number and a time unit, for example, 3s (for seconds) or 3000ms (for milliseconds).
                                          Default = 5s |
| max_noinput_count (Max NoInput
                                          				  Count) | int ≥ 0 | Yes | true | true | 3 | The maximum
                                          				  number of noinput events allowed during currency input capture. 0 = infinite
                                          				  noinputs allowed. |
| max_nomatch_count (Max NoMatch
                                          				  Count) | int ≥ 0 | Yes | true | true | 3 | The maximum
                                          				  number of nomatch events allowed during currency input capture. 0 = infinite
                                          				  nomatches allowed. |
| currency_confidence_level (Currency
                                          				  Confidence Level) | decimal (0.0
                                          				  to 1.0) | Yes | true | true | 0.40 | The
                                          				  confidence level threshold to use during currency capture. |
| modal (Disable
                                          				  Hotlinks) | boolean | Yes | true | true | false | Whether or
                                          				  not to temporarily disable all hotlink grammars (global or local) and universal
                                          				  grammars. If set to true, only the currency grammars will be enabled for the
                                          				  duration of the element. Otherwise all active grammars will be enabled. |
| secure_logging (Secure
                                          				  Logging) | boolean | Yes | true | true | false | If set to true, user DTMF input for the element is considered
                                          				  secure and the attributes utterance, interpretation, value, nbestUtteranceX and
                                          				  nbestInterpretationX are masked in VXML server logs. The format used to render
                                          				  secure element attributes is to add a _secureLogging suffix. For example nbestUtterance1_secureLogging,***** . |
| maxnbest (Maxnbest) | int ≥ 1 | Yes | true | true | 1 | The maximum
                                          				  number of speech recognition results that can be generated per voice input. |

| Note Refer to
                                                   				  the Element Data table below for information about nbestUtteranceX and nbestInterpretationX . | Note | Refer to
                                                   				  the Element Data table below for information about nbestUtteranceX and nbestInterpretationX . |
|---|---|---|
| Note | Refer to
                                                   				  the Element Data table below for information about nbestUtteranceX and nbestInterpretationX . |

| Note | Refer to
                                                   				  the Element Data table below for information about nbestUtteranceX and nbestInterpretationX . |
|---|---|

| Name | Type | Notes |
|---|---|---|
| Value | string | The currency amount captured. This will always be
                                          a decimal number with the appropriate number of padded zeros (up to
                                          2). |
| value_confidence | float | This is the confidence
                                          value of the captured utterance. When n-best recognition is enabled, this
                                          stores the confidence score of the top hypothesis in the n-best
                                          list. |
| nbestLength | int ≥ 1 | This stores the number of n-best hypotheses
                                          generated by the speech engine. |
| nbestUtterance1 nbestUtterance2 … nbestUtteranceX | string | This set of element
                                          data stores the captured n-best utterances. While the maximum number of
                                          nbestUtteranceX values is equal to the maxnbest setting value, the actual
                                          number of these values available is determined by speech recognition at
                                          runtime, where nbestUtterance1 holds the utterance of the top hypothesis in the
                                          n-best list and nbestUtteranceX holds the utterance of the last
                                          hypothesis. |
| nbestInterpretation1 nbestInterpretation2 … nbestInterpretationX | string | This set of element
                                          data stores the interpretations of captured n-best utterances. While the
                                          maximum number of nbestInterpretationX values is equal to the maxnbest setting
                                          value, the actual number of these values available is determined by speech
                                          recognition at runtime, where nbestInterpretation1 holds the interpretation of
                                          the top hypothesis in the n-best list and nbestInterpretationX holds the
                                          interpretation of the last hypothesis. |
| nbestConfidence1 nbestConfidence2 … nbestConfidenceX | float | This set of element data stores the confidence
                                          scores of captured n-best utterances. While the maximum number of
                                          nbestConfidenceX values is equal to the maxnbest setting value, the actual
                                          number of these values available is determined by speech recognition at
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
                                          currency capture was
                                          completed. |

| Name
                                                (Label) | Req'd | Max 1 | Notes |
|---|---|---|---|
| initial_audio_group (Initial) | Yes | Yes | Played when the voice
                                             element first begins. |
| nomatch_audio_group (NoMatch) | No | No | Played when a nomatch event
                                             occurs. |
| noinput_audio_group (NoInput) | No | No | Played when a noinput event
                                             occurs. |
| help_audio_group (Help) | No | No | Played when the caller asked for help. If not
                                             specified, by default help is treated as a
                                             nomatch. |

| Name
                                                (Label) | Req'd | Max 1 | Notes |
|---|---|---|---|
| done_audio_group (Done) | No | Yes | Played when the currency
                                             capture is completed and the voice element exits with the done exit
                                             state. |

| Studio
                                             Element Folder Name | Class Name |
|---|---|
| Commerce | com.audium.server.voiceElement.currency.MBasicCurrency |

| Name (Label) | Notes |
|---|---|
| Event Type | You can select Java Exception , VXML Event , or Hotlink as event handler for this element. |